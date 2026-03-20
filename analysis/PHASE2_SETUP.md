# Phase 2 Setup Notes

## What changed

I added a small Phase 2 scaffold so we can move from "final MT outputs + aggregate metrics"
to "sentence-level rows with traces, metadata, and sentence-level scores".

Files added:

- `analysis/phase2_utils.py`
- `analysis/export_sentence_metrics.py`
- `analysis/build_phase2_dataset.py`
- `analysis/PHASE2_SETUP.md`

Files updated:

- `comptra/sampler.py`
- `evaluation.py`

## Evaluation outputs are now richer

New evaluation runs still write `translate_0.jsonl`, but each row now keeps:

- `source_sentence`
- `reference_translation` for final outputs at `step == 0`
- `translation`
- `model_translation`
- `reasoning_trace` when `method_translate == cot`
- `sentence_index`
- `dataset_index`
- `step`
- `example_id`
- `metadata`

The old `translation` key is still present so the existing metric scripts stay compatible.

`evaluation.py` also now writes `run_metadata.json` in the run directory.

## Important limitation

Trace-faithfulness analysis is cleanest when:

- `--method_translate cot`
- `--steps 0`
- `--number_of_refining_steps 0`
- `--refine_after_merge 0`

If refinement is turned on, the saved trace still corresponds to the pre-refinement CoT output,
while the final translation may have changed afterward.

## Existing runs vs new runs

New runs:

- use the enriched `translate_0.jsonl`
- include `run_metadata.json`

Older runs:

- often only contain `sentence` and `translation`
- do not include traces
- can still be upgraded for Phase 2 dataset building if line order matches the first `N`
  examples of the evaluation split

For older runs, pass:

- `--dataset_name_or_path`
- `--src`
- `--tgt`

to the scripts below so they can reconstruct source/reference pairs from the benchmark.

## Recommended workflow

## Dependencies

The Phase 2 scripts assume the same research environment as the rest of the repo.

- `analysis/build_phase2_dataset.py` only needs standard Python plus the dataset-loading stack
  if it has to reconstruct older runs.
- `analysis/export_sentence_metrics.py` needs:
  - `sacrebleu` for BLEU
  - `comet` for COMET
  - `numpy`, `torch`, `transformers`, and `datasets` for MetricX

If one of these is missing, the script now raises an explicit error message telling you
which package family is required.

### 1. Generate fresh CoT evaluation outputs

Example:

```bash
python evaluation.py \
  --model_name_or_path YOUR_MODEL \
  --tokenizer_name_or_path YOUR_TOKENIZER \
  --src English \
  --tgt Xhosa \
  --dataset_name_or_path flores \
  --method_translate cot \
  --selection_method greedy \
  --k 0 \
  --steps 0 \
  --temperature 0.0 \
  --top_p 1.0 \
  --num_beams 1 \
  --num_return_sequences 1 \
  --output_dir YOUR_OUTPUT_DIR
```

### 2. Export sentence-level metrics

BLEU only:

```bash
python analysis/export_sentence_metrics.py \
  --run_dir YOUR_RUN_DIR \
  --metrics bleu
```

BLEU + COMET:

```bash
python analysis/export_sentence_metrics.py \
  --run_dir YOUR_RUN_DIR \
  --metrics bleu comet
```

BLEU + COMET + MetricX:

```bash
python analysis/export_sentence_metrics.py \
  --run_dir YOUR_RUN_DIR \
  --metrics bleu comet metricx
```

For older runs without metadata:

```bash
python analysis/export_sentence_metrics.py \
  --run_dir YOUR_RUN_DIR \
  --dataset_name_or_path flores \
  --src English \
  --tgt Xhosa \
  --metrics bleu comet
```

### 3. Build the Phase 2 dataset

```bash
python analysis/build_phase2_dataset.py \
  --run_dir YOUR_RUN_DIR
```

This writes `phase2_dataset.jsonl` with:

- `source_sentence`
- `reference_translation`
- `model_translation`
- `reasoning_trace`
- `metadata`

and `metadata["evaluation_scores"]` if `sentence_metrics.jsonl` is available.

## What this enables next

With `phase2_dataset.jsonl`, you can now:

1. run sentence difficulty tagging on `source_sentence` only
2. annotate a subset for linguistic phenomena
3. classify traces into:
   - `CORRECT_LINGUISTIC_ANALYSIS`
   - `HALLUCINATED_RULE`
   - `VACUOUS_FILLER`
   - `TRANSLATION_ATTEMPT`
   - `REPETITION`
4. correlate:
   - trace type
   - trace length
   - trace/translation overlap
   - sentence difficulty
   - sentence-level quality

## Suggested next manual step

Start with one small CoT run:

- one language pair
- one model
- one prompt type
- 100 to 300 examples

Then:

1. export sentence-level metrics
2. build the Phase 2 dataset
3. manually inspect 30 to 50 rows
4. freeze your annotation codebook before scaling up
