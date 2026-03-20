# Project Work Guideline

## Task Map

| If you want to… | Start here |
|---|---|
| Understand project goals and expected pipeline | [README.md](/Users/macbookpro/Desktop/M2MIASD/S6/algo-speech/llm-reasoning-mt/README.md) |
| Generate synthetic reasoning datasets (MAPS/SBYS/TEaR/Refine/CoT/CompTra) | [paraphrase.py](/Users/macbookpro/Desktop/M2MIASD/S6/algo-speech/llm-reasoning-mt/paraphrase.py), [scripts/paraphrase.sh](/Users/macbookpro/Desktop/M2MIASD/S6/algo-speech/llm-reasoning-mt/scripts/paraphrase.sh) |
| Convert generated JSONL to train-ready `source/target` format | [train_datasets.py](/Users/macbookpro/Desktop/M2MIASD/S6/algo-speech/llm-reasoning-mt/train_datasets.py) |
| Run SFT training | [train.py](/Users/macbookpro/Desktop/M2MIASD/S6/algo-speech/llm-reasoning-mt/train.py), [scripts/train.sh](/Users/macbookpro/Desktop/M2MIASD/S6/algo-speech/llm-reasoning-mt/scripts/train.sh) |
| Run GRPO/RL training | [train.py](/Users/macbookpro/Desktop/M2MIASD/S6/algo-speech/llm-reasoning-mt/train.py), [scripts/grpo.sh](/Users/macbookpro/Desktop/M2MIASD/S6/algo-speech/llm-reasoning-mt/scripts/grpo.sh), [configs/deepspeed_zero3_multi.yaml](/Users/macbookpro/Desktop/M2MIASD/S6/algo-speech/llm-reasoning-mt/configs/deepspeed_zero3_multi.yaml) |
| Evaluate translations (divide/translate/merge/refine) | [evaluation.py](/Users/macbookpro/Desktop/M2MIASD/S6/algo-speech/llm-reasoning-mt/evaluation.py), [scripts/eval.sh](/Users/macbookpro/Desktop/M2MIASD/S6/algo-speech/llm-reasoning-mt/scripts/eval.sh) |
| Change prompting templates | [comptra/prompts/templates.py](/Users/macbookpro/Desktop/M2MIASD/S6/algo-speech/llm-reasoning-mt/comptra/prompts/templates.py), plus prompt files in `comptra/prompts/` |
| Change model backend behavior (vLLM/OpenAI/HF/Anthropic/Cohere) | [comptra/sampler.py](/Users/macbookpro/Desktop/M2MIASD/S6/algo-speech/llm-reasoning-mt/comptra/sampler.py), [comptra/apply_chat_template.py](/Users/macbookpro/Desktop/M2MIASD/S6/algo-speech/llm-reasoning-mt/comptra/apply_chat_template.py), [comptra/models.py](/Users/macbookpro/Desktop/M2MIASD/S6/algo-speech/llm-reasoning-mt/comptra/models.py) |
| Change retrieval for ICL demos (bm25s/SONAR/etc.) | [comptra/retriever.py](/Users/macbookpro/Desktop/M2MIASD/S6/algo-speech/llm-reasoning-mt/comptra/retriever.py) |
| Change language codes / supported langs | [comptra/languages.py](/Users/macbookpro/Desktop/M2MIASD/S6/algo-speech/llm-reasoning-mt/comptra/languages.py) |
| Change benchmark dataset loading (FLORES/NTREX/TICO/WMT24) | [comptra/data/dataset.py](/Users/macbookpro/Desktop/M2MIASD/S6/algo-speech/llm-reasoning-mt/comptra/data/dataset.py) |
| Run metric scoring utilities (MetricX etc.) | [comptra/evaluate/test.py](/Users/macbookpro/Desktop/M2MIASD/S6/algo-speech/llm-reasoning-mt/comptra/evaluate/test.py), [scripts/test.sh](/Users/macbookpro/Desktop/M2MIASD/S6/algo-speech/llm-reasoning-mt/scripts/test.sh) |

## Practical Workflow

1. Read [README.md](/Users/macbookpro/Desktop/M2MIASD/S6/algo-speech/llm-reasoning-mt/README.md) and pick one path: `data generation`, `training`, or `evaluation`.
2. Use the matching script in `scripts/` as your baseline run command.
3. If behavior is wrong, debug in the matching Python entry file first (`paraphrase.py`, `train.py`, `evaluation.py`).
4. If logic depends on strategy/template/backend, then move to `comptra/prompts/`, `comptra/sampler.py`, or `train_datasets.py`.
5. Keep outputs under a clean experiment folder structure (`data/`, checkpoints, generations) before editing core code.

## Where To Edit For A New Strategy

- Add prompts in `comptra/prompts/`.
- Add generation path in [paraphrase.py](/Users/macbookpro/Desktop/M2MIASD/S6/algo-speech/llm-reasoning-mt/paraphrase.py).
- Add dataset builder in [train_datasets.py](/Users/macbookpro/Desktop/M2MIASD/S6/algo-speech/llm-reasoning-mt/train_datasets.py).
- Register in [train.py](/Users/macbookpro/Desktop/M2MIASD/S6/algo-speech/llm-reasoning-mt/train.py) dataset switch.
- Update [README.md](/Users/macbookpro/Desktop/M2MIASD/S6/algo-speech/llm-reasoning-mt/README.md) and relevant `scripts/*.sh`.
