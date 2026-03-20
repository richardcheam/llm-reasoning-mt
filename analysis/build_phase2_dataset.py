import argparse
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from analysis.phase2_utils import hydrate_run_rows, load_jsonl, resolve_run_metadata, write_jsonl


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--run_dir", type=str, required=True)
    parser.add_argument("--metrics_file", type=str)
    parser.add_argument("--output_file", type=str)
    parser.add_argument("--dataset_name_or_path", type=str)
    parser.add_argument("--src", type=str)
    parser.add_argument("--tgt", type=str)
    parser.add_argument("--model_name", type=str)
    parser.add_argument("--prompt_type", type=str)
    parser.add_argument("--number_of_shots", type=int)
    parser.add_argument("--decoding_temperature", type=float)
    return parser.parse_args()


def load_metrics(metrics_file):
    if metrics_file is None or not os.path.exists(metrics_file):
        return {}

    metric_rows = load_jsonl(metrics_file)
    by_example_id = {}
    by_sentence_index = {}
    for row in metric_rows:
        example_id = row.get("example_id")
        sentence_index = row.get("sentence_index")
        if example_id is not None:
            by_example_id[example_id] = row
        if sentence_index is not None:
            by_sentence_index[sentence_index] = row
    return {"by_example_id": by_example_id, "by_sentence_index": by_sentence_index}


def main():
    args = parse_args()
    run_file = os.path.join(args.run_dir, "translate_0.jsonl")
    rows = load_jsonl(run_file)
    resolved_metadata = resolve_run_metadata(args.run_dir, rows, args)
    records = hydrate_run_rows(rows, resolved_metadata)
    metrics = load_metrics(
        args.metrics_file or os.path.join(args.run_dir, "sentence_metrics.jsonl")
    )

    output_rows = []
    for record in records:
        metric_row = metrics.get("by_example_id", {}).get(record["example_id"])
        if metric_row is None:
            metric_row = metrics.get("by_sentence_index", {}).get(record["sentence_index"])

        evaluation_scores = {}
        if metric_row is not None:
            for key in ["sentence_bleu", "comet", "metricx"]:
                if metric_row.get(key) is not None:
                    evaluation_scores[key] = metric_row[key]

        metadata = dict(record["metadata"])
        metadata["evaluation_scores"] = evaluation_scores

        output_rows.append(
            {
                "example_id": record["example_id"],
                "source_sentence": record["source_sentence"],
                "reference_translation": record["reference_translation"],
                "model_translation": record["model_translation"],
                "reasoning_trace": record["reasoning_trace"],
                "metadata": metadata,
            }
        )

    output_file = args.output_file or os.path.join(args.run_dir, "phase2_dataset.jsonl")
    write_jsonl(output_file, output_rows)
    print(f"Wrote {len(output_rows)} rows to {output_file}")


if __name__ == "__main__":
    main()
