# LLM Execution Instructions for RC Phase 2 Work

**Purpose**: Complete instructions for an LLM agent to execute Richard Cheam's Phase 2 annotation work from start to finish.

**Context**: This is the llm-reasoning-mt repository. All infrastructure is ready, but no evaluation runs have been completed yet. You need to generate CoT evaluation outputs, then annotate and analyze them.

---

## Prerequisites Verification

Before starting, verify:
- [ ] Linux machine with Python 3.8+ installed
- [ ] Repository cloned to local machine
- [ ] Internet connection available (for model downloads)
- [ ] At least 10GB free disk space
- [ ] Ideally: GPU available (but CPU works too, just slower)

---

## TASK 1: Environment Setup

### Step 1.1: Check Python

```bash
python --version
# or
python3 --version
```

Expected: Python 3.8 or higher

### Step 1.2: Run Environment Setup

Use the existing setup script:

```bash
bash scripts/setup_uv.sh
```

Or manually create environment:

```bash
# Create virtual environment
python3 -m venv .venv

# Activate environment
source .venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install dependencies
pip install -r requirements-phase2.txt

# Install spaCy model
python -m spacy download en_core_web_sm
```

**Expected duration**: 10-20 minutes

**Success check**: All packages install without errors

### Step 1.3: Activate Environment

Every time you open a new terminal:
```bash
source .venv/bin/activate
```

You should see `(.venv)` in your prompt.

### Step 1.4: Test Environment

```bash
python analysis/test_environment.py
```

**Expected output**: All checks should pass with ✓

**If any checks fail**: 
- Read the error messages
- Install missing packages manually
- Re-run the test

---

## TASK 2: Generate CoT Evaluation Data

**Goal**: Run evaluation with CoT to produce reasoning traces for annotation

### Step 2.1: Choose Evaluation Configuration

For RC's pilot work, start with a small, manageable evaluation:

**Recommended configuration**:
- Model: `google/gemma-2-2b-it` (small, fast)
- Language pair: English → French (well-supported)
- Dataset: FLORES dev split
- Samples: 100 examples
- Method: CoT (chain-of-thought)

**Why these choices**:
- Small model = faster inference on CPU
- French = well-supported, easier to verify
- 100 samples = enough for meaningful pilot analysis
- Dev split = safe from contamination

### Step 2.2: Run CoT Evaluation

Create and run this command:

```bash
python evaluation.py \
    --model_name_or_path google/gemma-2-2b-it \
    --tokenizer_name_or_path google/gemma-2-2b-it \
    --src English \
    --tgt French \
    --dataset_name_or_path flores \
    --method_translate cot \
    --template_key 14 \
    --selection_method greedy \
    --k 0 \
    --steps 0 \
    --number_of_subproblems 0 \
    --number_of_refining_steps 0 \
    --num_beams 1 \
    --num_return_sequences 1 \
    --temperature 0.0 \
    --top_p 1.0 \
    --max_new_tokens 2048 \
    --output_dir evaluations/pilot_cot_eng_fra \
    --max_samples 100 \
    --inference_api hf \
    --seed 42 \
    --verbose
```

**Expected duration**: 
- CPU: 30-90 minutes
- GPU: 5-15 minutes

**Success indicators**:
- Progress bar showing completion
- Files created in `evaluations/pilot_cot_eng_fra/`
- `translate_0.jsonl` exists
- `run_metadata.json` exists

### Step 2.3: Verify Evaluation Outputs

```bash
python -c "from analysis.phase2_utils import load_jsonl; d=load_jsonl('evaluations/pilot_cot_eng_fra/translate_0.jsonl'); print(f'Loaded {len(d)} examples'); print('Keys:', list(d[0].keys())); print('Has reasoning_trace:', 'reasoning_trace' in d[0]); print('Sample trace length:', len(str(d[0].get('reasoning_trace', ''))))"
```

**Expected output**:
- Loaded 100 examples (or close to it)
- Keys include: source_sentence, reference_translation, model_translation, reasoning_trace
- Has reasoning_trace: True
- Sample trace length: > 100 characters

**If reasoning_trace is missing or empty**:
- Check the `--method_translate cot` flag was set
- Check model outputs aren't being truncated
- Try with `--max_new_tokens 4096`

---

## TASK 3: Prepare Phase 2 Dataset

### Step 3.1: Export Sentence-Level Metrics

```bash
python analysis/export_sentence_metrics.py \
    --run_dir evaluations/pilot_cot_eng_fra \
    --metrics bleu
```

**Note**: Starting with BLEU only (fast). COMET can be added later.

**Expected duration**: < 1 minute

**Success check**: `evaluations/pilot_cot_eng_fra/sentence_metrics.jsonl` created

### Step 3.2: Build Phase 2 Dataset

```bash
python analysis/build_phase2_dataset.py \
    --run_dir evaluations/pilot_cot_eng_fra
```

**Expected duration**: < 1 minute

**Success check**: `evaluations/pilot_cot_eng_fra/phase2_dataset.jsonl` created

### Step 3.3: Verify Phase 2 Dataset

```bash
python -c "from analysis.phase2_utils import load_jsonl; d=load_jsonl('evaluations/pilot_cot_eng_fra/phase2_dataset.jsonl'); print(f'Phase 2 dataset: {len(d)} examples'); print('Keys:', list(d[0].keys())); print('Has metadata:', 'metadata' in d[0]); print('Has eval scores:', 'evaluation_scores' in d[0].get('metadata', {}))"
```

**Expected output**:
- Phase 2 dataset: ~100 examples
- Keys include: example_id, source_sentence, reference_translation, model_translation, reasoning_trace, metadata
- Has metadata: True
- Has eval scores: True

---

## TASK 4: Pilot Manual Annotation

**Goal**: Manually annotate 20-30 examples to understand the codebook

### Step 4.1: Read the Codebook

**CRITICAL**: Before annotating, read:
- `analysis/annotation_codebook_v1.md` (complete annotation schema)
- `analysis/RC_QUICKSTART.md` (quick reference)

**Key concepts to understand**:
1. **Difficulty scoring (1-5)** - Based ONLY on source sentence
2. **Linguistic phenomena** - 6 binary tags
3. **Trace types** - 5 categories (CORRECT_LINGUISTIC_ANALYSIS, HALLUCINATED_RULE, etc.)
4. **Usefulness** - helpful/neutral/harmful
5. **Overlap** - none/low/medium/high

### Step 4.2: Run Manual Annotation

```bash
python analysis/annotate_dataset.py \
    --input_file evaluations/pilot_cot_eng_fra/phase2_dataset.jsonl \
    --output_file pilot_manual_20.jsonl \
    --manual_mode \
    --sample_size 20 \
    --annotator_id RC \
    --seed 42
```

**What happens**:
- Script shows each example interactively
- You provide annotations via keyboard input
- Progress is saved incrementally

**Expected duration**: 1-2 hours for 20 examples

**Tips for manual annotation**:
- Read ONLY the source sentence for difficulty scoring
- Take notes on edge cases
- Be consistent with your judgments
- If unsure, note it in annotator_notes

### Step 4.3: Review Pilot Annotations

```bash
python -c "from analysis.phase2_utils import load_jsonl; d=load_jsonl('pilot_manual_20.jsonl'); print(f'Annotated {len(d)} examples'); import json; print('Sample:', json.dumps(d[0], indent=2)[:500])"
```

Check for:
- All examples have annotations
- Difficulty scores make sense
- Trace types are distributed (not all the same)

---

## TASK 5: LLM-Assisted Full Annotation

**Goal**: Use LLM to annotate remaining examples with quality control

### Step 5.1: Run LLM Annotation

```bash
python analysis/annotate_dataset.py \
    --input_file evaluations/pilot_cot_eng_fra/phase2_dataset.jsonl \
    --output_file llm_annotations_full.jsonl \
    --annotation_model google/gemma-2-9b-it \
    --temperature 0.0 \
    --seed 42 \
    --batch_size 4 \
    --max_new_tokens 512 \
    --save_raw_outputs \
    --annotator_id RC_LLM \
    --inference_api hf
```

**Expected duration**: 
- CPU: 2-4 hours for 100 examples
- GPU: 20-40 minutes

**Success checks**:
- `llm_annotations_full.jsonl` created
- `llm_annotations_full_raw.jsonl` created (raw outputs)
- `llm_annotations_full_metadata.json` created (provenance)

### Step 5.2: Check Parse Success Rate

```bash
python -c "from analysis.phase2_utils import load_jsonl; d=load_jsonl('llm_annotations_full.jsonl'); errors = sum(1 for x in d if x.get('parse_error')); print(f'Total: {len(d)}, Parse errors: {errors}, Success rate: {100*(len(d)-errors)/len(d):.1f}%')"
```

**Acceptable**: Parse success rate > 80%

**If < 80%**:
- Check raw outputs to see what LLM generated
- May need to adjust prompt or try different model
- Can manually fix parse errors

### Step 5.3: Manual Audit Sample

Randomly audit 10-20 examples to verify LLM quality:

```bash
python -c "from analysis.phase2_utils import load_jsonl; import random; random.seed(42); d=load_jsonl('llm_annotations_full.jsonl'); sample = random.sample(d, 10); import json; [print(f'\n=== Example {i} ===\n', json.dumps(ex, indent=2)[:300]) for i, ex in enumerate(sample)]"
```

**Manual review checklist**:
- [ ] Difficulty scores seem reasonable
- [ ] Linguistic phenomena tags are accurate
- [ ] Trace type classifications make sense
- [ ] Usefulness judgments are plausible

**If quality is poor**:
- Consider re-annotating with better prompt
- Or increase manual annotation instead

---

## TASK 6: Generate Analysis Tables

**Goal**: Produce descriptive statistics and correlations

### Step 6.1: Run Analysis

```bash
python analysis/analyze_traces.py \
    --annotated_file llm_annotations_full.jsonl \
    --phase2_file evaluations/pilot_cot_eng_fra/phase2_dataset.jsonl \
    --output_dir results_pilot/
```

**Expected duration**: < 1 minute

**Output files created**:
- `results_pilot/SUMMARY.md` - High-level statistics
- `results_pilot/difficulty_distribution.md`
- `results_pilot/phenomena_frequencies.md`
- `results_pilot/trace_type_distribution.md`
- `results_pilot/usefulness_distribution.md`
- `results_pilot/overlap_distribution.md`
- `results_pilot/crosstab_*.md` - Cross-tabulations
- `results_pilot/quality_correlations.md`

### Step 6.2: Review Results

Open `results_pilot/SUMMARY.md` and check:
- Difficulty distribution is reasonable (not all 1s or all 5s)
- Trace types are distributed (multiple categories present)
- Usefulness categories are represented
- Quality correlations make sense

### Step 6.3: Generate Report Summary

Create a summary document:

```bash
cat results_pilot/SUMMARY.md
```

**Key findings to extract**:
1. Most common trace type
2. Average difficulty score
3. Correlation between trace usefulness and BLEU score
4. Most common linguistic phenomena
5. Trace-translation overlap patterns

---

## TASK 7: Deliverables Package

**Goal**: Organize all outputs for RC's final deliverables

### Step 7.1: Create Deliverables Directory

```bash
mkdir -p deliverables_rc_phase2
```

### Step 7.2: Copy Key Files

```bash
cp analysis/annotation_codebook_v1.md deliverables_rc_phase2/
cp analysis/annotation_prompt_v1.txt deliverables_rc_phase2/
cp pilot_manual_20.jsonl deliverables_rc_phase2/
cp llm_annotations_full.jsonl deliverables_rc_phase2/
cp llm_annotations_full_metadata.json deliverables_rc_phase2/
cp -r results_pilot deliverables_rc_phase2/analysis_results/
```

### Step 7.3: Create Executive Summary

Create `deliverables_rc_phase2/EXECUTIVE_SUMMARY.md`:

```markdown
# RC Phase 2 Analysis - Executive Summary

**Date**: [DATE]
**Annotator**: Richard Cheam [RC]
**Dataset**: FLORES English→French, CoT traces
**Sample Size**: [N] examples

## Annotation Methodology

- Codebook version: v1.0
- Manual pilot: 20 examples
- LLM-assisted: [N-20] examples (model: google/gemma-2-9b-it)
- Manual audit: 10 examples
- Parse success rate: [X]%

## Key Findings

1. **Difficulty Distribution**
   - Average difficulty: [X.X]
   - Most common: Score [N] ([X]%)

2. **Trace Type Distribution**
   - Most common: [TYPE] ([X]%)
   - Least common: [TYPE] ([X]%)

3. **Trace Usefulness**
   - Helpful: [X]%
   - Neutral: [X]%
   - Harmful: [X]%

4. **Quality Correlation**
   - Helpful traces → Avg BLEU: [X.XX]
   - Neutral traces → Avg BLEU: [X.XX]
   - Harmful traces → Avg BLEU: [X.XX]

5. **Linguistic Phenomena**
   - Most common: [PHENOMENON] ([X]%)
   - ...

## Conclusion

[Summary of whether CoT traces appear helpful for MT, based on the data]

## Reproducibility

All annotations reproducible with:
- Model: google/gemma-2-9b-it (revision: [HASH])
- Temperature: 0.0
- Seed: 42
- Codebook: v1.0
- Prompt: annotation_prompt_v1.txt
```

Fill in the [PLACEHOLDERS] with actual values from your results.

---

## TASK 8: Quality Checks

Before finalizing, verify:

### Contamination Safety
- [ ] Difficulty annotations used source-only (verified in manual pilot)
- [ ] No test set contamination (used dev split)
- [ ] Consistent annotation settings across all examples

### Reproducibility
- [ ] Annotation metadata saved (`llm_annotations_full_metadata.json`)
- [ ] Model revision recorded
- [ ] Raw outputs saved
- [ ] Codebook version documented
- [ ] All settings logged

### Completeness
- [ ] Manual pilot completed (20+ examples)
- [ ] LLM annotation completed (80+ examples)
- [ ] Manual audit completed (10+ examples)
- [ ] Analysis tables generated
- [ ] Summary report written
- [ ] Deliverables packaged

---

## Expected Timeline

**Total time**: 1-2 days (depending on CPU vs GPU)

- Environment setup: 30 minutes
- CoT evaluation: 30-90 minutes (CPU) or 5-15 minutes (GPU)
- Phase 2 dataset prep: 5 minutes
- Manual pilot (20 examples): 1-2 hours
- LLM annotation (80 examples): 2-4 hours (CPU) or 20-40 minutes (GPU)
- Manual audit: 30 minutes
- Analysis generation: 5 minutes
- Report writing: 1-2 hours
- Total: ~6-10 hours active work

---

## Troubleshooting Guide

### "Out of memory" during evaluation
```bash
# Reduce batch size (add to evaluation.py command)
--request_batch_size 1
```

### "CUDA out of memory" during LLM annotation
```bash
# Use CPU instead
--device cpu --batch_size 1
```

### "Parse errors" in LLM annotation
- Check `llm_annotations_full_raw.jsonl` to see what LLM generated
- LLM might not be following JSON format
- Try different model or adjust prompt

### Evaluation is too slow
- Reduce `--max_samples` to 50 or even 20 for testing
- Use smaller model (google/gemma-2-2b-it)
- Consider running on GPU machine

### Model download fails
- Check internet connection
- Check HuggingFace is accessible
- May need HF_TOKEN for some models

---

## Success Criteria

You have successfully completed RC's Phase 2 work when:

1. ✅ Phase 2 dataset created with 50-100 annotated examples
2. ✅ Annotations include difficulty, phenomena, trace types, usefulness
3. ✅ Manual pilot completed to validate codebook
4. ✅ LLM-assisted annotation with >80% parse success
5. ✅ Manual audit confirms annotation quality
6. ✅ Analysis tables generated showing distributions and correlations
7. ✅ Deliverables packaged with reproducibility metadata
8. ✅ Executive summary written with key findings

---

## Final Checklist for LLM Executor

Before marking this complete, ensure:

- [ ] `evaluations/pilot_cot_eng_fra/translate_0.jsonl` exists with reasoning traces
- [ ] `evaluations/pilot_cot_eng_fra/phase2_dataset.jsonl` exists
- [ ] `pilot_manual_20.jsonl` exists with manual annotations
- [ ] `llm_annotations_full.jsonl` exists with LLM annotations
- [ ] `llm_annotations_full_metadata.json` documents reproducibility
- [ ] `results_pilot/SUMMARY.md` exists with analysis
- [ ] `deliverables_rc_phase2/` folder contains all key files
- [ ] Executive summary written with actual findings
- [ ] All quality checks passed

---

## Handoff to RC

Once complete, provide RC with:

1. **Deliverables folder**: `deliverables_rc_phase2/`
2. **Executive summary**: Key findings in 1-2 pages
3. **Instructions for replication**: Point to metadata files
4. **Next steps**: Suggestions for expanding to more language pairs or larger samples

---

**End of LLM Execution Instructions**

Good luck! Follow each task in order, verify success at each step, and document any issues or deviations.
