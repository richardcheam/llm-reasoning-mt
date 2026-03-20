# Few-Shot FLORES Note

This note is for a lightweight few-shot MT setup with small Gemma instruction models on a 64-example FLORES slice.

## Goal

Run few-shot translation with:

- `google/gemma-3-270m-it`
- `google/gemma-3-1b-it`

using:

- FLORES
- 64 examples
- local Hugging Face inference (`--inference_api hf`)

## Why This Setup

- It is small enough to test the pipeline quickly.
- It avoids `vllm`, which is not practical on this local Mac-style setup.
- It matches the repo's few-shot evaluation path in [evaluation.py](/Users/macbookpro/Desktop/M2MIASD/S6/algo-speech/llm-reasoning-mt/evaluation.py).

## One-Command Run

```bash
./scripts/eval_fewshot_flores_small_gemma.sh
```

If a repo-local `.env` exists, the script loads it automatically before starting. This is useful for `HF_TOKEN` / `HUGGINGFACE_HUB_TOKEN` when model access requires authentication.

Defaults in the script:

- `SRC=English`
- `TGT=French`
- `K=5`
- `MAX_SAMPLES=64`
- models:
  - `google/gemma-3-270m-it`
  - `google/gemma-3-1b-it`

If the exact few-shot count from the other setup was not 5, change `K`.

## Common Variants

Change language pair:

```bash
SRC=English TGT=German ./scripts/eval_fewshot_flores_small_gemma.sh
```

Change shot count:

```bash
K=4 ./scripts/eval_fewshot_flores_small_gemma.sh
```

Run only the 1B model:

```bash
./scripts/eval_fewshot_flores_small_gemma.sh google/gemma-3-1b-it
```

## Debug The 270M Model

If the 270M model returns empty translations, run the dedicated debug script on the GPU machine:

```bash
./scripts/debug_gemma_270m_fewshot.sh
```

Defaults in debug mode:

- `MAX_SAMPLES=1`
- `VERBOSE=1`
- `DEBUG_RAW_OUTPUTS=1`
- `MAX_NEW_TOKENS=128`

This saves the prompt, raw candidate generations, and cleaned candidate generations into `translate_0.jsonl` so you can see whether the emptiness comes from the model itself or from post-processing.

## Output Location

Runs are written under:

```text
runs/fewshot_flores_64/
```

Each run directory contains the evaluation outputs, including `translate_0.jsonl` and `run_metadata.json`.

## Metrics Follow-Up

After a run completes, export sentence-level metrics with:

```bash
python analysis/export_sentence_metrics.py --run_dir RUN_DIR --metrics bleu
```

Then build a Phase 2-ready dataset:

```bash
python analysis/build_phase2_dataset.py --run_dir RUN_DIR
```

## Notes

- The local HF path was patched to work on CPU / MPS / CUDA instead of assuming CUDA only.
- `google/gemma-3-270m-it` was added to the local model/chat-template handling.
- This script uses `template_key=14`, `retriever_type=bm25s`, and a direct few-shot translation path:
  - `method_translate=vanilla`
  - `steps=0`
  - `number_of_subproblems=0`
  - `number_of_refining_steps=0`

## If You Want Exact Reproduction

The remaining knobs to verify against the other person's setup are:

1. source language
2. target language
3. number of shots `K`
4. whether they used `bm25s` or `Random` retrieval
5. whether they reported corpus-level or sentence-level metrics
