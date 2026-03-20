# Richard Cheam [RC] Phase 2 Annotation Methodology

**Project**: LLM Reasoning for Machine Translation  
**Date**: 2026-03-20  
**Codebook Version**: v1.0  
**Methodology**: Codebook-guided LLM-assisted annotation with manual audit

---

## Overview

This document describes the reproducible annotation methodology for Phase 2 trace analysis of the llm-reasoning-mt project. The methodology follows contamination-safe and reproducibility-first principles as specified in the project handoff documentation.

---

## Research Question

Why does reasoning or chain-of-thought (CoT) help for mathematics and coding, but not reliably for machine translation?

## RC Responsibilities

### Phase 1: Dataset Tagging
1. Tag the dataset for sentence difficulty (source-only)
2. Score each sentence by translation difficulty (1-5 scale)
3. Annotate a subset for linguistic phenomena:
   - Ambiguity
   - Idioms
   - Complex syntax
   - Named entities
   - Figurative language
   - Long-distance dependencies

### Phase 2: Trace Analysis
1. Categorize reasoning traces into types:
   - Correct linguistic analysis
   - Hallucinated rules
   - Vacuous filler
   - Actual translation attempts
   - Repetition
2. Measure overlap between traces and final translations
3. Analyze trace length vs. translation quality
4. Cross-tabulate with:
   - Model
   - Language pair
   - Prompt type
   - Number of shots

---

## Annotation Pipeline

### Step 1: Data Preparation

**Input**: Evaluation outputs from MT models with reasoning traces

**Process**:
```bash
# Export sentence-level metrics
python analysis/export_sentence_metrics.py \
    --run_dir <RUN_DIR> \
    --metrics bleu comet metricx

# Build Phase 2 dataset
python analysis/build_phase2_dataset.py \
    --run_dir <RUN_DIR>
```

**Output**: `phase2_dataset.jsonl` containing:
- `example_id`: Unique identifier
- `source_sentence`: Source text
- `reference_translation`: Human reference
- `model_translation`: Model output
- `reasoning_trace`: CoT trace (if present)
- `metadata`: Run configuration and evaluation scores

### Step 2: Pilot Annotation (50-100 examples)

**Purpose**: Refine codebook and establish consistency

**Process**:
```bash
# Manual pilot annotation
python analysis/annotate_dataset.py \
    --input_file phase2_dataset.jsonl \
    --output_file pilot_annotated.jsonl \
    --manual_mode \
    --sample_size 50 \
    --annotator_id RC
```

**Activities**:
1. Manually annotate 50-100 diverse examples
2. Identify edge cases and ambiguities
3. Refine codebook definitions if needed
4. Document any changes (increment codebook version)
5. Achieve inter-annotator agreement >0.7 (if multiple annotators)

### Step 3: LLM-Assisted Annotation Setup

**Model Selection**:
- Use open-source HuggingFace model with version control
- Recommended: `google/gemma-2-9b-it` or `meta-llama/Llama-3.1-8B-Instruct`
- Record exact model revision/commit hash

**Annotation Settings** (for reproducibility):
- Temperature: 0.0 (deterministic)
- Seed: Fixed (e.g., 42)
- Max tokens: 512
- Prompt template: `analysis/annotation_prompt_v1.txt`
- Codebook version: `v1.0`

**Process**:
```bash
# LLM-assisted annotation
python analysis/annotate_dataset.py \
    --input_file phase2_dataset.jsonl \
    --output_file full_annotated.jsonl \
    --annotation_model google/gemma-2-9b-it \
    --model_revision <SPECIFIC_COMMIT_HASH> \
    --prompt_template analysis/annotation_prompt_v1.txt \
    --codebook_version v1.0 \
    --temperature 0.0 \
    --seed 42 \
    --batch_size 8 \
    --save_raw_outputs \
    --annotator_id RC
```

**Outputs**:
- `full_annotated.jsonl`: Parsed annotations
- `full_annotated_raw.jsonl`: Raw model outputs
- `full_annotated_metadata.json`: Annotation provenance

### Step 4: Quality Control

**Manual Audit**:
- Sample 10-20% of LLM annotations for manual review
- Focus on:
  - Parse errors
  - Edge cases
  - High-difficulty examples
  - Inconsistent labels

**Consistency Checks**:
```bash
# Generate consistency report
python analysis/audit_annotations.py \
    --annotated_file full_annotated.jsonl \
    --audit_sample_size 100 \
    --output_report audit_report.md
```

**Correction Process**:
- If audit reveals systematic errors, refine prompt or switch models
- Re-annotate problematic subset
- Document all changes

### Step 5: Descriptive Analysis

**Generate analysis tables**:
```bash
# Analyze trace patterns
python analysis/analyze_traces.py \
    --annotated_file full_annotated.jsonl \
    --output_dir analysis_results/
```

**Key Analyses**:

1. **Trace Type Distribution**
   - Frequency of each trace type by model
   - Frequency by prompt type
   - Frequency by language pair

2. **Trace Usefulness vs. Quality**
   - Correlation: trace usefulness ↔ translation quality (BLEU/COMET)
   - Do helpful traces lead to better translations?

3. **Trace Length vs. Quality**
   - Correlation: trace length ↔ translation quality
   - Are longer traces better?

4. **Difficulty vs. Trace Behavior**
   - Do difficult sentences get better traces?
   - Are vacuous traces more common for easy sentences?

5. **Linguistic Phenomena vs. Trace Types**
   - Which phenomena trigger correct linguistic analysis?
   - Which lead to hallucinated rules?

6. **Overlap vs. Quality**
   - Does high trace-translation overlap predict quality?

---

## Contamination Safety Protocol

**Critical Rules**:

1. **Difficulty Tagging is Source-Only**
   - Do NOT use reference translation
   - Do NOT use model translation
   - Do NOT use reasoning trace
   - Only analyze source sentence complexity

2. **Test Set Protection**
   - Do NOT generate reasoning traces on held-out test sets (e.g., FLORES devtest)
   - Only annotate evaluation outputs from designated analysis splits

3. **Consistency Requirements**
   - Use fixed prompt template across all batches
   - Use fixed model and settings across all batches
   - Do NOT modify codebook mid-annotation (version updates only)

---

## Reproducibility Protocol

### Minimum Artifacts

1. **Codebook**
   - File: `analysis/annotation_codebook_v1.md`
   - Versioned and frozen

2. **Prompt Template**
   - File: `analysis/annotation_prompt_v1.txt`
   - Fixed template with placeholders

3. **Annotation Script**
   - File: `analysis/annotate_dataset.py`
   - Deterministic, reproducible pipeline

4. **Metadata**
   - Model name and revision
   - Prompt version
   - Codebook version
   - Date, seed, temperature
   - All hyperparameters

5. **Raw Outputs**
   - Saved before parsing
   - Allows re-parsing if needed

6. **Audit Log**
   - Manual corrections
   - Edge case decisions
   - Codebook refinements

### Replication Instructions

To replicate RC annotations:

```bash
# Clone repository
git clone <repo-url>
cd llm-reasoning-mt

# Install dependencies
pip install -r requirements-phase2.txt

# Download annotation model
# (HuggingFace will cache automatically)

# Run annotation with exact settings
python analysis/annotate_dataset.py \
    --input_file <PATH_TO_PHASE2_DATASET> \
    --output_file annotated_output.jsonl \
    --annotation_model google/gemma-2-9b-it \
    --model_revision <EXACT_COMMIT_HASH> \
    --prompt_template analysis/annotation_prompt_v1.txt \
    --codebook_version v1.0 \
    --temperature 0.0 \
    --seed 42 \
    --max_new_tokens 512 \
    --batch_size 8 \
    --save_raw_outputs
```

All settings are logged in `annotated_output_metadata.json`.

---

## Sampling Strategy

### Stratified Sampling for Full Annotation

To ensure representative coverage:

**Stratification Dimensions**:
1. **Model**: Include all models tested
2. **Prompt Type**: Direct, CoT (templates 1-6), MAPS, SBYS, etc.
3. **Language Pair**: Focus on main pairs (e.g., English-Xhosa)
4. **Number of Shots**: 0-shot, few-shot
5. **Quality**: Sample both high and low BLEU scores
6. **Trace Length**: Sample short and long traces

**Recommended Sample Sizes**:
- Pilot: 50-100 examples
- Full annotation: 500-1000 examples (or full dataset if <1000)
- Audit: 10-20% of LLM-annotated examples

---

## Expected Deliverables

### Minimum Deliverables

1. **Annotation Codebook** (`annotation_codebook_v1.md`)
2. **Pilot Annotated Dataset** (`pilot_annotated.jsonl`)
3. **Full Annotated Dataset** (`full_annotated.jsonl`)
4. **Annotation Metadata** (`full_annotated_metadata.json`)
5. **Audit Report** (`audit_report.md`)
6. **Summary Statistics**:
   - Trace type frequencies
   - Usefulness vs. quality table
   - Difficulty distribution
   - Linguistic phenomena frequencies

### Strong Deliverables (Recommended)

1. **Reproducibility Report**:
   - Exact replication instructions
   - Model provenance
   - All hyperparameters
   - Inter-annotator agreement (if applicable)

2. **Error Analysis Examples**:
   - 10-20 examples of each trace type
   - Annotated explanations
   - Comparison of helpful vs. harmful traces

3. **Analysis Tables**:
   - Trace type × prompt type
   - Trace type × model
   - Usefulness × quality bucket
   - Overlap × quality
   - Length × quality
   - Difficulty × trace behavior

4. **Visualizations**:
   - Distribution plots
   - Correlation heatmaps
   - Quality stratification charts

---

## Timeline Recommendation

1. **Week 1**: Pilot annotation (50-100 examples), codebook refinement
2. **Week 2**: LLM-assisted full annotation, quality control
3. **Week 3**: Manual audit, corrections, analysis
4. **Week 4**: Deliverables preparation, documentation

---

## Tools and Scripts

### Core Scripts

- `analysis/build_phase2_dataset.py`: Build analysis dataset
- `analysis/annotate_dataset.py`: Main annotation pipeline
- `analysis/audit_annotations.py`: Quality control audit (to be created)
- `analysis/analyze_traces.py`: Generate analysis tables (to be created)

### Utility Scripts

- `analysis/phase2_utils.py`: Data loading utilities
- `analysis/export_sentence_metrics.py`: Compute evaluation metrics

### Configuration Files

- `analysis/annotation_codebook_v1.md`: Annotation schema
- `analysis/annotation_prompt_v1.txt`: LLM prompt template
- `requirements-phase2.txt`: Python dependencies

---

## Notes

### Known Limitations

1. LLM-assisted annotation may have systematic biases
   - Mitigate with manual audit and inter-annotator checks

2. Trace analysis requires subjective judgment
   - Use codebook consistently
   - Document edge cases

3. Overlap measurement is qualitative
   - Consider developing automated lexical overlap metric

### Future Improvements

1. Develop automated inter-annotator agreement calculator
2. Create trace overlap metric (e.g., token-level F1)
3. Build visualization dashboard for trace analysis
4. Extend to more language pairs

---

## References

- Project handoff: `RC_LLM_HANDOFF.txt`
- Phase 2 setup: `analysis/PHASE2_SETUP.md`
- Main README: `README.md`
- Work guidelines: `WORK_GUIDELINE.md`

---

**Contact**: Richard Cheam [RC]  
**Last Updated**: 2026-03-20  
**Version**: 1.0
