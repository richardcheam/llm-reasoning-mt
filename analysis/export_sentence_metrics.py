import argparse
import os
import sys
from statistics import mean

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from analysis.phase2_utils import hydrate_run_rows, load_jsonl, resolve_run_metadata, write_jsonl


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--run_dir", type=str, required=True)
    parser.add_argument("--output_file", type=str)
    parser.add_argument(
        "--metrics",
        nargs="+",
        default=["bleu"],
        choices=["bleu", "comet", "metricx"],
        help="Sentence-level metrics to export.",
    )
    parser.add_argument("--dataset_name_or_path", type=str)
    parser.add_argument("--src", type=str)
    parser.add_argument("--tgt", type=str)
    parser.add_argument("--model_name", type=str)
    parser.add_argument("--prompt_type", type=str)
    parser.add_argument("--number_of_shots", type=int)
    parser.add_argument("--decoding_temperature", type=float)
    parser.add_argument(
        "--comet_model_name_or_path",
        type=str,
        default="Unbabel/wmt22-comet-da",
    )
    parser.add_argument(
        "--metricx_model_name_or_path",
        type=str,
        default="google/metricx-24-hybrid-xxl-v2p6",
    )
    parser.add_argument(
        "--metricx_variant",
        type=str,
        choices=["23", "24"],
        default="24",
    )
    parser.add_argument("--metricx_qe", action="store_true")
    parser.add_argument("--max_input_length", type=int, default=1024)
    parser.add_argument("--batch_size", type=int, default=8)
    return parser.parse_args()


def compute_sentence_bleu(records):
    try:
        from sacrebleu.metrics import BLEU
    except ImportError as exc:
        raise RuntimeError(
            "BLEU export requires `sacrebleu` to be installed in the active environment."
        ) from exc

    bleu = BLEU(tokenize="flores200")
    return [
        bleu.sentence_score(
            record["model_translation"], [record["reference_translation"]]
        ).score
        for record in records
    ]


def compute_comet(records, args):
    try:
        import torch
        from comet import download_model, load_from_checkpoint
    except ImportError as exc:
        raise RuntimeError(
            "COMET export requires the `comet` package and its dependencies."
        ) from exc

    model_path = download_model(args.comet_model_name_or_path)
    model = load_from_checkpoint(model_path)
    data = [
        {
            "src": record["source_sentence"],
            "mt": record["model_translation"],
            "ref": record["reference_translation"],
        }
        for record in records
    ]
    model_output = model.predict(
        data,
        batch_size=args.batch_size,
        gpus=1 if torch.cuda.is_available() else 0,
        progress_bar=False,
    )
    return [float(score) for score in model_output.scores]


def compute_metricx(records, args):
    try:
        import numpy as np
        import torch
        import transformers
        from datasets import Dataset
    except ImportError as exc:
        raise RuntimeError(
            "MetricX export requires `numpy`, `torch`, `transformers`, and `datasets`."
        ) from exc

    if args.metricx_variant == "24":
        from comptra.evaluate.metricx24.models import MT5ForRegression
    else:
        from comptra.evaluate.metricx23.models import MT5ForRegression

    tokenizer = transformers.AutoTokenizer.from_pretrained("google/mt5-xl")
    dtype = torch.bfloat16 if torch.cuda.is_available() else torch.float32
    model = MT5ForRegression.from_pretrained(
        args.metricx_model_name_or_path, torch_dtype=dtype
    )
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)
    model.eval()

    ds_dict = {
        "source": [record["source_sentence"] for record in records],
        "hypothesis": [record["model_translation"] for record in records],
    }
    if not args.metricx_qe:
        ds_dict["reference"] = [record["reference_translation"] for record in records]
    ds = Dataset.from_dict(ds_dict)

    def make_input(example):
        if args.metricx_qe:
            example["input"] = (
                "candidate: "
                + example["hypothesis"]
                + " source: "
                + example["source"]
            )
        else:
            example["input"] = (
                "candidate: "
                + example["hypothesis"]
                + " reference: "
                + example["reference"]
            )
        return example

    def tokenize(example):
        return tokenizer(
            example["input"],
            max_length=args.max_input_length,
            truncation=True,
            padding=False,
        )

    def remove_eos(example):
        example["input_ids"] = example["input_ids"][:-1]
        example["attention_mask"] = example["attention_mask"][:-1]
        return example

    ds = ds.map(make_input)
    ds = ds.map(tokenize)
    ds = ds.map(remove_eos)
    ds.set_format(
        type="torch",
        columns=["input_ids", "attention_mask"],
        device=device,
        output_all_columns=True,
    )

    tmp_output_dir = os.path.join(args.run_dir, ".metricx_tmp")
    os.makedirs(tmp_output_dir, exist_ok=True)
    training_args = transformers.TrainingArguments(
        output_dir=tmp_output_dir,
        per_device_eval_batch_size=max(
            1, args.batch_size // max(1, torch.cuda.device_count())
        ),
        dataloader_pin_memory=False,
        report_to="none",
    )
    trainer = transformers.Trainer(model=model, args=training_args)
    predictions, _, _ = trainer.predict(test_dataset=ds)
    return [float(score) for score in np.array(predictions).reshape(-1)]


def main():
    args = parse_args()
    run_file = os.path.join(args.run_dir, "translate_0.jsonl")
    rows = load_jsonl(run_file)
    resolved_metadata = resolve_run_metadata(args.run_dir, rows, args)
    records = hydrate_run_rows(rows, resolved_metadata)

    metric_values = {}
    if "bleu" in args.metrics:
        metric_values["sentence_bleu"] = compute_sentence_bleu(records)
    if "comet" in args.metrics:
        metric_values["comet"] = compute_comet(records, args)
    if "metricx" in args.metrics:
        metric_values["metricx"] = compute_metricx(records, args)

    output_rows = []
    for idx, record in enumerate(records):
        row = {
            "example_id": record["example_id"],
            "sentence_index": record["sentence_index"],
        }
        for metric_name, values in metric_values.items():
            row[metric_name] = values[idx]
        output_rows.append(row)

    output_file = args.output_file or os.path.join(args.run_dir, "sentence_metrics.jsonl")
    write_jsonl(output_file, output_rows)

    print(f"Wrote {len(output_rows)} rows to {output_file}")
    for metric_name, values in metric_values.items():
        if values:
            print(f"{metric_name}: mean={float(mean(values)):.4f}")


if __name__ == "__main__":
    main()
