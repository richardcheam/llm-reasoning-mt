#!/usr/bin/env bash

set -euo pipefail

SCRIPT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
ROOT_DIR=$(cd "$SCRIPT_DIR/.." && pwd)

SRC="${SRC:-English}"
TGT="${TGT:-French}"
K="${K:-5}"
MAX_SAMPLES="${MAX_SAMPLES:-1}"
REQUEST_BATCH_SIZE="${REQUEST_BATCH_SIZE:-1}"
MAX_NEW_TOKENS="${MAX_NEW_TOKENS:-128}"
SEED="${SEED:-122}"

if [[ "${1:-}" == "--help" || "${1:-}" == "-h" ]]; then
  cat <<EOF
Usage: ./scripts/debug_gemma_270m_fewshot.sh

Run a 1-example debug evaluation for google/gemma-3-270m-it with:
  DEBUG_RAW_OUTPUTS=1
  VERBOSE=1
  MAX_SAMPLES=1

Override via environment variables:
  SRC, TGT, K, MAX_SAMPLES, REQUEST_BATCH_SIZE, MAX_NEW_TOKENS, SEED
EOF
  exit 0
fi

DEBUG_RAW_OUTPUTS=1 \
VERBOSE=1 \
SRC="$SRC" \
TGT="$TGT" \
K="$K" \
MAX_SAMPLES="$MAX_SAMPLES" \
REQUEST_BATCH_SIZE="$REQUEST_BATCH_SIZE" \
MAX_NEW_TOKENS="$MAX_NEW_TOKENS" \
SEED="$SEED" \
"$ROOT_DIR/scripts/eval_fewshot_flores_small_gemma.sh" google/gemma-3-270m-it
