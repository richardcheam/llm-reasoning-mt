# UV Environment Setup

This repo did not include a `requirements.txt` or `pyproject.toml`, so the local environment is currently based on [requirements-phase2.txt](/Users/macbookpro/Desktop/M2MIASD/S6/algo-speech/llm-reasoning-mt/requirements-phase2.txt).

## One-Command Setup

Use the setup script:

```bash
./scripts/setup_uv.sh
```

It will:

1. Bootstrap `uv` locally if needed.
2. Create `.venv/`.
3. Install the base dependencies from `requirements-phase2.txt`.
4. Install the spaCy English model.
5. Run import smoke tests for the main entry points.

Optional extras:

```bash
./scripts/setup_uv.sh --with-grakel
./scripts/setup_uv.sh --with-sonar
./scripts/setup_uv.sh --with-vllm
```

## What was done

1. Installed a local copy of `uv` in `.tools/uv/`.
2. Created a virtual environment in `.venv/`.
3. Installed the project dependencies from `requirements-phase2.txt`.
4. Installed the spaCy English model `en_core_web_sm`, which is required by multiple modules at import time.
5. Patched [comptra/sampler.py](/Users/macbookpro/Desktop/M2MIASD/S6/algo-speech/llm-reasoning-mt/comptra/sampler.py) so the repo can import without `vllm` being installed. `vllm` is still required if you explicitly run with `--inference_api vllm`.
6. Patched [comptra/utils.py](/Users/macbookpro/Desktop/M2MIASD/S6/algo-speech/llm-reasoning-mt/comptra/utils.py) and [comptra/prompts/decompose.py](/Users/macbookpro/Desktop/M2MIASD/S6/algo-speech/llm-reasoning-mt/comptra/prompts/decompose.py) so imports do not trigger network downloads for FastText, SacreBLEU, or NLTK resources.

## Reuse These Commands

Create the environment:

```bash
UV_CACHE_DIR="$PWD/.uv-cache" ./.tools/uv/uv venv .venv
```

Install dependencies:

```bash
UV_CACHE_DIR="$PWD/.uv-cache" ./.tools/uv/uv pip install --python .venv/bin/python -r requirements-phase2.txt
```

Install the spaCy English model:

```bash
UV_CACHE_DIR="$PWD/.uv-cache" ./.tools/uv/uv pip install --python .venv/bin/python pip https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.8.0/en_core_web_sm-3.8.0-py3-none-any.whl
```

Quick validation:

```bash
UV_CACHE_DIR="$PWD/.uv-cache" .venv/bin/python -c "import spacy; nlp = spacy.load('en_core_web_sm'); print(nlp.meta['name'], nlp.meta['version'])"
UV_CACHE_DIR="$PWD/.uv-cache" .venv/bin/python -c "import evaluation; print('evaluation import ok')"
```

## topxgen Clone

The setup script auto-detects a sibling clone at `../topxgen` if it exists. This is useful because `llm-reasoning-mt` reuses ideas and optional dependencies from that upstream repo, but the script does not blindly install all of `topxgen`'s requirements by default. In particular, GPU- or experiment-specific packages such as `vllm`, `sonar-space`, and `grakel` stay opt-in.

## What Works In This Environment

- Phase 2 analysis scripts in `analysis/`
- Evaluation and generation flows using `--inference_api hf`
- Evaluation and generation flows using hosted APIs (`openai`, `anthropic`, `cohere`) if credentials are provided
- Most training code paths, including the `trl`-based parts

## Still Optional / Not Installed

- `vllm`
  - Needed only for `--inference_api vllm`
  - Usually best installed separately on a Linux GPU machine
- `SONAR`
  - Only needed for SONAR-based retrieval experiments
- `grakel`
  - Only needed for graph-kernel retrieval experiments
- `flash-attn`
  - Needed only if you want `--use_flash_attn`
- `liger-kernel`
  - Needed only if you want `--use_liger_loss`

## Notes

- The local `uv` cache is stored in `.uv-cache/` because the default user cache path was not writable in this setup.
- SacreBLEU is now configured lazily and uses a repo-local `.sacrebleu/` cache when needed.
- If you want to keep the repo clean, consider adding `.venv/`, `.uv-cache/`, and `.tools/` to `.gitignore`.
