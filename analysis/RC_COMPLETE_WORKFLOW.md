# Complete RC Phase 2 Workflow

**Critical**: You need evaluation outputs with reasoning traces BEFORE you can annotate them.

## Overview

The existing data in [`data/`](../data/) is **training data** (synthetic reasoning datasets for fine-tuning), **NOT evaluation outputs** suitable for annotation.

For Phase 2 annotation, you need:
1. **Evaluation outputs** from running CoT models on test sets
2. With reasoning traces included
3. With sentence-level quality metrics

## Complete Step-by-Step Workflow

### Phase A: Generate Evaluation Data (If Not Available)

#### Option 1: Check for Existing Evaluation Runs

Look for existing evaluation run directories:
```cmd
dir /s /b runs\* 2>nul
dir /s /b evaluations\* 2>nul
dir /s /b outputs\* 2>nul
```

Evaluation runs typically contain:
- `translate_0.jsonl` (model outputs)
- `run_metadata.json` (configuration)
- Possibly `results.json` (aggregate metrics)

#### Option 2: Run New Evaluation with CoT

If no suitable evaluation runs exist, you need to generate them. Here's how:

**Important**: This requires a GPU or significant compute time on CPU.

```cmd
REM Activate environment
.venv\Scripts\activate.bat

REM Example: Evaluate a CoT model on FLORES
python evaluation.py ^
    --model_name_or_path path/to/your/cot-finetuned-model ^
    --tokenizer_name_or_path path/to/tokenizer ^
    --src English ^
    --tgt Xhosa ^
    --dataset_name_or_path flores ^
    --method_translate cot ^
    --template_key 14 ^
    --k 0 ^
    --steps 0 ^
    --num_beams 1 ^
    --temperature 0.0 ^
    --max_new_tokens 2048 ^
    --output_dir evaluations/gemma-3-4b-xhosa-cot-flores ^
    --max_samples 100 ^
    --inference_api hf
```

**Key parameters for Phase 2**:
- `--method_translate cot` - This generates reasoning traces!
- `--steps 0` - Direct CoT, no decomposition
- `--max_samples 100` - Start small for pilot
- `--output_dir` - Where outputs will be saved

**Note**: Running evaluation can take 1-30 minutes depending on:
- Model size
- Number of samples
- CPU vs GPU
- Trace length

### Phase B: Prepare Phase 2 Dataset

Once you have evaluation outputs:

#### Step 1: Export Sentence-Level Metrics

```cmd
python analysis\export_sentence_metrics.py ^
    --run_dir evaluations\gemma-3-4b-xhosa-cot-flores ^
    --metrics bleu comet
```

This creates `sentence_metrics.jsonl` with BLEU and COMET scores per example.

**Note**: 
- BLEU is fast (< 1 minute)
- COMET requires downloading a model (~1GB) and takes longer
- MetricX is optional but very slow

#### Step 2: Build Phase 2 Dataset

```cmd
python analysis\build_phase2_dataset.py ^
    --run_dir evaluations\gemma-3-4b-xhosa-cot-flores
```

This creates `phase2_dataset.jsonl` with:
- Source sentences
- Reference translations
- Model translations
- Reasoning traces
- Metadata
- Evaluation scores (from step 1)

**This is the file you'll annotate!**

### Phase C: Annotation

Now you can proceed with annotation:

#### Step 3: Pilot Manual Annotation

```cmd
python analysis\annotate_dataset.py ^
    --input_file evaluations\gemma-3-4b-xhosa-cot-flores\phase2_dataset.jsonl ^
    --output_file pilot_manual.jsonl ^
    --manual_mode ^
    --sample_size 50 ^
    --annotator_id RC
```

#### Step 4: Full LLM-Assisted Annotation

```cmd
python analysis\annotate_dataset.py ^
    --input_file evaluations\gemma-3-4b-xhosa-cot-flores\phase2_dataset.jsonl ^
    --output_file llm_annotations.jsonl ^
    --annotation_model google/gemma-2-9b-it ^
    --temperature 0.0 ^
    --seed 42 ^
    --save_raw_outputs ^
    --annotator_id RC
```

### Phase D: Analysis

#### Step 5: Generate Analysis Tables

```cmd
python analysis\analyze_traces.py ^
    --annotated_file llm_annotations.jsonl ^
    --phase2_file evaluations\gemma-3-4b-xhosa-cot-flores\phase2_dataset.jsonl ^
    --output_dir results\
```

---

## Quick Decision Tree

### Do you have existing evaluation runs with CoT traces?

**YES** → Skip to Phase B (Prepare Phase 2 Dataset)
- Check if runs contain `translate_0.jsonl` with reasoning traces
- Verify with: `python -c "from analysis.phase2_utils import load_jsonl; data = load_jsonl('path/to/translate_0.jsonl'); print(data[0].keys())"`

**NO** → Start with Phase A (Generate Evaluation Data)
- Need to run evaluation with CoT models
- Requires GPU or patience (CPU evaluation is slow)

### Can you run evaluations on a GPU machine?

**YES** → Use existing scripts:
- [`scripts/eval_fewshot_flores_small_gemma.sh`](../scripts/eval_fewshot_flores_small_gemma.sh) (bash)
- Or adapt to Windows with the commands above

**NO (CPU only)** → Start with small samples:
- Use `--max_samples 10` for testing
- Use `--inference_api hf` (not vllm)
- Consider using smaller models (google/gemma-3-270m-it)
- Or work with existing evaluation data if available

---

## Recommended Pilot Setup

For a quick pilot to test the annotation pipeline:

### 1. Use Existing Data (If Available)

Check if there are evaluation runs in the repository:
```cmd
dir /s /b *.jsonl | findstr translate
```

### 2. Generate Small Evaluation (If Needed)

Run evaluation on just 20 examples to test the pipeline:
```cmd
python evaluation.py ^
    --model_name_or_path google/gemma-3-1b-it ^
    --tokenizer_name_or_path google/gemma-3-1b-it ^
    --src English ^
    --tgt French ^
    --dataset_name_or_path flores ^
    --method_translate cot ^
    --template_key 14 ^
    --k 0 ^
    --max_samples 20 ^
    --output_dir test_evaluation ^
    --inference_api hf
```

**Time estimate**: 5-15 minutes on CPU for 20 examples

### 3. Build Test Dataset

```cmd
python analysis\export_sentence_metrics.py ^
    --run_dir test_evaluation ^
    --metrics bleu

python analysis\build_phase2_dataset.py ^
    --run_dir test_evaluation
```

### 4. Test Manual Annotation

```cmd
python analysis\annotate_dataset.py ^
    --input_file test_evaluation\phase2_dataset.jsonl ^
    --output_file test_annotations.jsonl ^
    --manual_mode ^
    --sample_size 5
```

This lets you test the entire pipeline with just 5 examples!

---

## What Data Exists Already?

The [`data/`](../data/) directory contains:
- ✅ **Training datasets** with synthetic reasoning traces
- ❌ **NOT evaluation outputs** for annotation

For annotation, you need outputs from [`evaluation.py`](../evaluation.py:1), which:
- Runs a trained model on test data (FLORES, NTREX, etc.)
- Generates translations with reasoning traces
- Saves outputs in a structured format
- Allows computing quality metrics

---

## Contamination Warning

From [`RC_LLM_HANDOFF.txt`](../RC_LLM_HANDOFF.txt:56):

> **Do not generate reasoning traces on held-out test sets such as FLORES devtest if those sets are meant for evaluation**

For RC's annotation work:
- ✅ **OK**: Annotate evaluation outputs explicitly designated for analysis
- ✅ **OK**: Use FLORES dev split for annotation
- ❌ **NOT OK**: Generate new traces on final test sets meant for model selection
- ❌ **NOT OK**: Use traces that might contaminate future experiments

**Recommendation**: Use evaluation outputs from:
1. Development sets (FLORES dev, not devtest)
2. Outputs already generated for analysis purposes
3. Separate held-out analysis set (not used for model training or tuning)

---

## Summary

### If you have evaluation runs with CoT traces:
```
1. export_sentence_metrics.py
2. build_phase2_dataset.py
3. annotate_dataset.py
4. analyze_traces.py
```

### If you need to generate evaluation data first:
```
1. evaluation.py (with --method_translate cot)
2. export_sentence_metrics.py
3. build_phase2_dataset.py
4. annotate_dataset.py
5. analyze_traces.py
```

### For quick testing:
```
1. evaluation.py (20 samples, small model)
2. build_phase2_dataset.py
3. annotate_dataset.py (5 samples, manual mode)
```

---

## Next Action

**Check for existing evaluation data first**:
```cmd
REM Look for evaluation runs
dir /s /b translate_0.jsonl

REM If found, check content
python -c "from analysis.phase2_utils import load_jsonl; d=load_jsonl('path/to/translate_0.jsonl'); print('Keys:', d[0].keys()); print('Has trace:', 'reasoning_trace' in d[0])"
```

Then decide: use existing data or generate new evaluation outputs.
