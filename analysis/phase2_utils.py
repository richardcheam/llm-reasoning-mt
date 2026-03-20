import json
import os


def load_jsonl(path):
    rows = []
    with open(path, "r", encoding="utf-8") as fin:
        for line in fin:
            line = line.strip()
            if not line:
                continue
            rows.append(json.loads(line))
    return rows


def write_jsonl(path, rows):
    with open(path, "w", encoding="utf-8") as fout:
        for row in rows:
            fout.write(json.dumps(row, ensure_ascii=False) + "\n")


def read_run_metadata(run_dir):
    metadata_path = os.path.join(run_dir, "run_metadata.json")
    if os.path.exists(metadata_path):
        with open(metadata_path, "r", encoding="utf-8") as fin:
            return json.load(fin)
    return {}


def resolve_run_metadata(run_dir, rows, args):
    metadata = read_run_metadata(run_dir)
    first_row_metadata = rows[0].get("metadata", {}) if rows else {}

    def pick(attr_name, *keys):
        value = getattr(args, attr_name, None)
        if value is not None:
            return value
        for key in keys:
            if key in metadata and metadata[key] is not None:
                return metadata[key]
            if key in first_row_metadata and first_row_metadata[key] is not None:
                return first_row_metadata[key]
        return None

    resolved = dict(metadata)
    if isinstance(first_row_metadata, dict):
        resolved.update(first_row_metadata)

    resolved["dataset_name_or_path"] = pick(
        "dataset_name_or_path", "dataset_name_or_path"
    )
    resolved["source_language"] = pick("src", "source_language")
    resolved["target_language"] = pick("tgt", "target_language")
    resolved["model_name"] = pick("model_name", "model_name")
    resolved["prompt_type"] = pick("prompt_type", "prompt_type")
    resolved["number_of_shots"] = pick("number_of_shots", "number_of_shots")
    resolved["decoding_temperature"] = pick(
        "decoding_temperature", "decoding_temperature"
    )

    if (
        resolved.get("language_pair") is None
        and resolved.get("source_language") is not None
        and resolved.get("target_language") is not None
    ):
        resolved["language_pair"] = (
            f"{resolved['source_language']}-{resolved['target_language']}"
        )

    return resolved


def hydrate_run_rows(rows, resolved_metadata):
    hydrated_rows = []
    needs_dataset_lookup = any(
        row.get("source_sentence") is None or row.get("reference_translation") is None
        for row in rows
    )

    dataset_src = None
    dataset_tgt = None
    if needs_dataset_lookup:
        from comptra.data.dataset import get_datasets

        dataset_name = resolved_metadata.get("dataset_name_or_path")
        src = resolved_metadata.get("source_language")
        tgt = resolved_metadata.get("target_language")
        if dataset_name is None or src is None or tgt is None:
            raise ValueError(
                "Missing dataset metadata. Provide --dataset_name_or_path, --src and --tgt "
                "when working from older evaluation outputs."
            )
        dataset_src = get_datasets(dataset_name, src)
        dataset_tgt = get_datasets(dataset_name, tgt)

    for idx, row in enumerate(rows):
        sentence_index = row.get("sentence_index", idx)
        dataset_index = row.get("dataset_index")
        if dataset_index is None and needs_dataset_lookup:
            dataset_index = idx

        source_sentence = row.get("source_sentence") or row.get("sentence")
        reference_translation = row.get("reference_translation")

        if dataset_src is not None and (source_sentence is None or reference_translation is None):
            source_sentence = dataset_src["devtest"][dataset_index]["sentence"]
            reference_translation = dataset_tgt["devtest"][dataset_index]["sentence"]

        record_metadata = dict(resolved_metadata)
        if isinstance(row.get("metadata"), dict):
            record_metadata.update(row["metadata"])

        hydrated_rows.append(
            {
                **row,
                "sentence_index": sentence_index,
                "dataset_index": dataset_index,
                "source_sentence": source_sentence,
                "reference_translation": reference_translation,
                "model_translation": row.get("model_translation") or row.get("translation"),
                "reasoning_trace": row.get("reasoning_trace"),
                "example_id": row.get("example_id")
                or (
                    f"{record_metadata.get('dataset_name_or_path', 'unknown')}:"
                    f"{record_metadata.get('source_language', 'unknown')}:"
                    f"{record_metadata.get('target_language', 'unknown')}:0:{sentence_index}"
                ),
                "metadata": record_metadata,
            }
        )

    return hydrated_rows
