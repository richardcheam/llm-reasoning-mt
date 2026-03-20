#!/usr/bin/env bash

set -euo pipefail

SCRIPT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
ROOT_DIR=$(cd "$SCRIPT_DIR/.." && pwd)
PYTHON_BIN="${PYTHON_BIN:-$ROOT_DIR/.venv/bin/python}"

if [[ -f "$ROOT_DIR/.env" ]]; then
  set -a
  # shellcheck disable=SC1091
  source "$ROOT_DIR/.env"
  set +a
fi

SRC="${SRC:-English}"
TGT="${TGT:-French}"
K="${K:-5}"
MAX_SAMPLES="${MAX_SAMPLES:-64}"
REQUEST_BATCH_SIZE="${REQUEST_BATCH_SIZE:-1}"
MAX_NEW_TOKENS="${MAX_NEW_TOKENS:-192}"
SEED="${SEED:-122}"
TEMPLATE_KEY="${TEMPLATE_KEY:-14}"
RETRIEVER_TYPE="${RETRIEVER_TYPE:-bm25s}"
OUTPUT_BASE="${OUTPUT_BASE:-$ROOT_DIR/runs/fewshot_flores_64}"
DEBUG_RAW_OUTPUTS="${DEBUG_RAW_OUTPUTS:-0}"
VERBOSE="${VERBOSE:-0}"

usage() {
  cat <<EOF
Usage: ./scripts/eval_fewshot_flores_small_gemma.sh [MODEL ...]

Run few-shot MT on 64 FLORES examples with small Gemma instruction models.

Defaults:
  models: google/gemma-3-270m-it google/gemma-3-1b-it
  SRC=English
  TGT=French
  K=5
  MAX_SAMPLES=64
  REQUEST_BATCH_SIZE=1
  DEBUG_RAW_OUTPUTS=0
  VERBOSE=0

Examples:
  ./scripts/eval_fewshot_flores_small_gemma.sh
  SRC=English TGT=German K=4 ./scripts/eval_fewshot_flores_small_gemma.sh
  SRC=English TGT=French ./scripts/eval_fewshot_flores_small_gemma.sh google/gemma-3-1b-it
  DEBUG_RAW_OUTPUTS=1 VERBOSE=1 MAX_SAMPLES=1 ./scripts/eval_fewshot_flores_small_gemma.sh google/gemma-3-270m-it
EOF
}

slugify() {
  echo "$1" | tr '/:' '__'
}

if [[ "${1:-}" == "--help" || "${1:-}" == "-h" ]]; then
  usage
  exit 0
fi

MODELS=("$@")
if [[ ${#MODELS[@]} -eq 0 ]]; then
  MODELS=("google/gemma-3-270m-it" "google/gemma-3-1b-it")
fi

if [[ ! -x "$PYTHON_BIN" ]]; then
  echo "[fewshot_gemma] Python not found at $PYTHON_BIN" >&2
  echo "[fewshot_gemma] Run ./scripts/setup_uv.sh first or set PYTHON_BIN." >&2
  exit 1
fi

mkdir -p "$OUTPUT_BASE"

for MODEL in "${MODELS[@]}"; do
  MODEL_SLUG=$(slugify "$MODEL")
  RUN_DIR="$OUTPUT_BASE/${SRC}_to_${TGT}/${MODEL_SLUG}/k_${K}_seed_${SEED}"
  mkdir -p "$RUN_DIR"

  echo "[fewshot_gemma] Running $MODEL -> $RUN_DIR"
  CMD=(
    "$PYTHON_BIN" "$ROOT_DIR/evaluation.py"
    --model_name_or_path "$MODEL"
    --tokenizer_name_or_path "$MODEL"
    --src "$SRC"
    --tgt "$TGT"
    --dataset_name_or_path flores
    --inference_api hf
    --request_batch_size "$REQUEST_BATCH_SIZE"
    --max_samples "$MAX_SAMPLES"
    --num_return_sequences 1
    --num_beams 1
    --max_new_tokens "$MAX_NEW_TOKENS"
    --temperature 0.0
    --top_p 1.0
    --repetition_penalty 1.0
    --output_dir "$RUN_DIR"
    --k "$K"
    --seed "$SEED"
    --method_divide identity
    --merge_prompt vanilla
    --method_translate vanilla
    --selection_method greedy
    --steps 0
    --number_of_subproblems 0
    --number_of_refining_steps 0
    --template_key "$TEMPLATE_KEY"
    --retriever_type "$RETRIEVER_TYPE"
    --number_of_merge_demonstrations 0
  )

  if [[ "$DEBUG_RAW_OUTPUTS" == "1" ]]; then
    CMD+=(--debug_raw_outputs)
  fi

  if [[ "$VERBOSE" == "1" ]]; then
    CMD+=(--verbose)
  fi

  "${CMD[@]}"
done

echo "[fewshot_gemma] Runs complete."
