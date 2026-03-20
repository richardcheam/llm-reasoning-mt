#!/usr/bin/env bash

set -euo pipefail

SCRIPT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
ROOT_DIR=$(cd "$SCRIPT_DIR/.." && pwd)
UV_CACHE_DIR="${UV_CACHE_DIR:-$ROOT_DIR/.uv-cache}"
VENV_DIR="${VENV_DIR:-$ROOT_DIR/.venv}"
TOPXGEN_DIR="${TOPXGEN_DIR:-$ROOT_DIR/../topxgen}"

WITH_GRAKEL=0
WITH_SONAR=0
WITH_VLLM=0
SKIP_SPACY_MODEL=0
SKIP_SMOKE_TESTS=0

SPACY_MODEL_WHEEL="https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.8.0/en_core_web_sm-3.8.0-py3-none-any.whl"

usage() {
  cat <<EOF
Usage: ./scripts/setup_uv.sh [options]

Create or refresh the local uv-based environment for llm-reasoning-mt.

Options:
  --with-grakel       Install the optional grakel dependency used by graph retrieval.
  --with-sonar        Install the optional sonar-space dependency used by SONAR retrieval.
  --with-vllm         Install vllm (recommended only on Linux/CUDA machines).
  --skip-spacy-model  Skip installation of en_core_web_sm.
  --skip-smoke-tests  Skip the final import checks.
  --help              Show this message.

Environment variables:
  UV_CACHE_DIR        Cache directory for uv. Default: $ROOT_DIR/.uv-cache
  VENV_DIR            Virtual environment path. Default: $ROOT_DIR/.venv
  TOPXGEN_DIR         Path to a sibling topxgen clone. Default: $ROOT_DIR/../topxgen
EOF
}

log() {
  printf '[setup_uv] %s\n' "$*"
}

die() {
  printf '[setup_uv] ERROR: %s\n' "$*" >&2
  exit 1
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --with-grakel)
      WITH_GRAKEL=1
      ;;
    --with-sonar)
      WITH_SONAR=1
      ;;
    --with-vllm)
      WITH_VLLM=1
      ;;
    --skip-spacy-model)
      SKIP_SPACY_MODEL=1
      ;;
    --skip-smoke-tests)
      SKIP_SMOKE_TESTS=1
      ;;
    --help|-h)
      usage
      exit 0
      ;;
    *)
      die "Unknown option: $1"
      ;;
  esac
  shift
done

ensure_uv() {
  if command -v uv >/dev/null 2>&1; then
    UV_BIN=$(command -v uv)
  elif [[ -x "$ROOT_DIR/.tools/uv/uv" ]]; then
    UV_BIN="$ROOT_DIR/.tools/uv/uv"
  else
    if ! command -v curl >/dev/null 2>&1; then
      die "uv is not installed and curl is unavailable to bootstrap it."
    fi
    local installer="${TMPDIR:-/tmp}/uv_install.sh"
    mkdir -p "$ROOT_DIR/.tools"
    log "Installing a local uv binary into $ROOT_DIR/.tools/uv"
    curl -LsSf https://astral.sh/uv/install.sh -o "$installer"
    env UV_INSTALL_DIR="$ROOT_DIR/.tools/uv" sh "$installer"
    UV_BIN="$ROOT_DIR/.tools/uv/uv"
  fi
  export UV_BIN
  log "Using uv at $UV_BIN"
}

ensure_cache_and_venv() {
  mkdir -p "$UV_CACHE_DIR"
  if [[ ! -d "$VENV_DIR" ]]; then
    log "Creating virtual environment at $VENV_DIR"
    env UV_CACHE_DIR="$UV_CACHE_DIR" "$UV_BIN" venv "$VENV_DIR"
  else
    log "Virtual environment already exists at $VENV_DIR"
  fi
}

install_base_requirements() {
  log "Installing base requirements from requirements-phase2.txt"
  env UV_CACHE_DIR="$UV_CACHE_DIR" \
    "$UV_BIN" pip install --python "$VENV_DIR/bin/python" -r "$ROOT_DIR/requirements-phase2.txt"
}

install_spacy_model() {
  if (( SKIP_SPACY_MODEL )); then
    log "Skipping spaCy model installation"
    return
  fi

  if "$VENV_DIR/bin/python" -c "import en_core_web_sm" >/dev/null 2>&1; then
    log "spaCy model en_core_web_sm is already installed"
    return
  fi

  log "Installing spaCy model en_core_web_sm"
  env UV_CACHE_DIR="$UV_CACHE_DIR" \
    "$UV_BIN" pip install --python "$VENV_DIR/bin/python" pip "$SPACY_MODEL_WHEEL"
}

install_optional_package() {
  local package_name="$1"
  log "Installing optional package: $package_name"
  env UV_CACHE_DIR="$UV_CACHE_DIR" \
    "$UV_BIN" pip install --python "$VENV_DIR/bin/python" "$package_name"
}

install_optional_dependencies() {
  if (( WITH_GRAKEL )); then
    install_optional_package "grakel"
  fi

  if (( WITH_SONAR )); then
    install_optional_package "sonar-space"
  fi

  if (( WITH_VLLM )); then
    if [[ "$(uname -s)" != "Linux" ]]; then
      log "Skipping vllm because this host is not Linux. Install it on a Linux/CUDA machine."
    else
      install_optional_package "vllm"
    fi
  fi
}

describe_topxgen() {
  if [[ -d "$TOPXGEN_DIR" ]]; then
    log "Detected sibling topxgen clone at $TOPXGEN_DIR"
    if [[ -f "$TOPXGEN_DIR/requirements.txt" ]]; then
      log "topxgen upstream extras include packages such as vllm, grakel, sonar-space, and rouge-score"
    fi
  else
    log "No sibling topxgen clone detected at $TOPXGEN_DIR"
  fi
}

run_smoke_tests() {
  if (( SKIP_SMOKE_TESTS )); then
    log "Skipping smoke tests"
    return
  fi

  log "Running smoke tests"
  "$VENV_DIR/bin/python" -c "import spacy; nlp = spacy.load('en_core_web_sm'); print('spacy_ok', nlp.meta.get('name'), nlp.meta.get('version'))"
  "$VENV_DIR/bin/python" -c "import train; print('train_import_ok')"
  "$VENV_DIR/bin/python" -c "import evaluation; print('evaluation_import_ok')"
  "$VENV_DIR/bin/python" -c "import paraphrase; print('paraphrase_import_ok')"
  "$VENV_DIR/bin/python" -c "import analysis.build_phase2_dataset as phase2; print('phase2_import_ok')"
}

print_next_steps() {
  cat <<EOF

[setup_uv] Setup complete.
[setup_uv] Activate the environment with:
  source "$VENV_DIR/bin/activate"

[setup_uv] Common checks:
  python evaluation.py --help
  python paraphrase.py --help
  python train.py --help
EOF
}

ensure_uv
describe_topxgen
ensure_cache_and_venv
install_base_requirements
install_spacy_model
install_optional_dependencies
run_smoke_tests
print_next_steps
