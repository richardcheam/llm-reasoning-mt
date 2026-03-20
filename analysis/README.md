# Phase 2 Analysis Infrastructure

This directory contains the complete annotation and analysis infrastructure for Richard Cheam's [RC] Phase 2 work on the llm-reasoning-mt project.

## Purpose

Annotate and analyze reasoning traces from machine translation models to understand why chain-of-thought reasoning helps for math/coding but not reliably for MT.

## Quick Start

### 1. Build Phase 2 Dataset

Start from evaluation outputs:

```bash
# Export sentence-level metrics
python analysis/export_sentence_metrics.py \
    --run_dir path/to/evaluation/run \
    --metrics bleu comet

# Build analysis-ready dataset
python analysis/build_phase2_dataset.py \
    --run_dir path/to/evaluation/run
```

This creates `phase2_dataset.jsonl` with source sentences, translations, traces, and metadata.

### 2. Pilot Annotation (Manual)

Annotate 50-100 examples manually to refine the codebook:

```bash
python analysis/annotate_dataset.py \
    --input_file path/to/phase2_dataset.jsonl \
    --output_file pilot_annotated.jsonl \
    --manual_mode \
    --sample_size 50 \
    --annotator_id RC
```

### 3. Full Annotation (LLM-Assisted)

Annotate the full dataset with reproducible LLM pipeline:

```bash
python analysis/annotate_dataset.py \
    --input_file path/to/phase2_dataset.jsonl \
    --output_file full_annotated.jsonl \
    --annotation_model google/gemma-2-9b-it \
    --model_revision <COMMIT_HASH> \
    --temperature 0.0 \
    --seed 42 \
    --save_raw_outputs \
    --annotator_id RC
```

### 4. Generate Analysis Tables

Produce descriptive statistics and correlations:

```bash
python analysis/analyze_traces.py \
    --annotated_file full_annotated.jsonl \
    --phase2_file path/to/phase2_dataset.jsonl \
    --output_dir analysis_results/
```

## Files

### Core Scripts

| File | Purpose |
|------|---------|
| [`build_phase2_dataset.py`](build_phase2_dataset.py) | Build analysis dataset from evaluation runs |
| [`export_sentence_metrics.py`](export_sentence_metrics.py) | Compute sentence-level BLEU/COMET/MetricX |
| [`annotate_dataset.py`](annotate_dataset.py) | Reproducible annotation pipeline |
| [`analyze_traces.py`](analyze_traces.py) | Generate summary statistics and tables |
| [`phase2_utils.py`](phase2_utils.py) | Shared utilities for data loading |

### Documentation

| File | Purpose |
|------|---------|
| [`PHASE2_SETUP.md`](PHASE2_SETUP.md) | Phase 2 infrastructure overview |
| [`RC_METHODOLOGY.md`](RC_METHODOLOGY.md) | Complete annotation methodology |
| [`annotation_codebook_v1.md`](annotation_codebook_v1.md) | Annotation schema and definitions |
| [`annotation_prompt_v1.txt`](annotation_prompt_v1.txt) | LLM annotation prompt template |

## Annotation Schema

### Sentence Difficulty (1-5 scale, source-only)
- 1 = Trivial
- 2 = Easy
- 3 = Moderate
- 4 = Difficult
- 5 = Very Difficult

### Linguistic Phenomena (binary)
- Ambiguity
- Idiom
- Complex syntax
- Named entities
- Figurative language
- Long-distance dependency

### Trace Type Classification
- **CORRECT_LINGUISTIC_ANALYSIS**: Accurate linguistic insights
- **HALLUCINATED_RULE**: Invented or incorrect rules
- **VACUOUS_FILLER**: Generic content with no information
- **TRANSLATION_ATTEMPT**: Actual translation drafts
- **REPETITION**: Repeated content without new information

### Trace Usefulness
- **helpful**: Improves translation quality
- **neutral**: No effect on quality
- **harmful**: Degrades translation quality

### Trace-Translation Overlap
- **none**: <5% overlap
- **low**: 5-25% overlap
- **medium**: 25-75% overlap
- **high**: >75% overlap

## Contamination Safety

**CRITICAL**: Difficulty scoring is **source-only**
- Do NOT use reference translation
- Do NOT use model translation  
- Do NOT use reasoning trace
- Only analyze source sentence complexity

## Reproducibility

All LLM-assisted annotations must record:
- Model name and revision (HuggingFace commit hash)
- Prompt template version
- Codebook version
- Temperature, seed, and all hyperparameters
- Date and annotator ID

See [`RC_METHODOLOGY.md`](RC_METHODOLOGY.md) for complete reproducibility protocol.

## Output Files

### Annotation Output
- `annotated_dataset.jsonl`: Parsed annotations
- `annotated_dataset_raw.jsonl`: Raw LLM outputs
- `annotated_dataset_metadata.json`: Annotation provenance

### Analysis Output
- `SUMMARY.md`: High-level statistics
- `difficulty_distribution.md`: Difficulty score frequencies
- `phenomena_frequencies.md`: Linguistic phenomena counts
- `trace_type_distribution.md`: Trace type frequencies
- `usefulness_distribution.md`: Usefulness categories
- `overlap_distribution.md`: Overlap categories
- `crosstab_*.md`: Cross-tabulation tables
- `quality_correlations.md`: Quality vs. trace characteristics

## Example Workflow

```bash
# Step 1: Prepare data
python analysis/build_phase2_dataset.py \
    --run_dir runs/gemma-3-4b-xhosa-cot/

# Step 2: Pilot annotation (manual)
python analysis/annotate_dataset.py \
    --input_file runs/gemma-3-4b-xhosa-cot/phase2_dataset.jsonl \
    --output_file pilot_annotations.jsonl \
    --manual_mode \
    --sample_size 50

# Step 3: Refine codebook based on pilot
# (Edit annotation_codebook_v1.md if needed, increment version)

# Step 4: Full LLM-assisted annotation
python analysis/annotate_dataset.py \
    --input_file runs/gemma-3-4b-xhosa-cot/phase2_dataset.jsonl \
    --output_file full_annotations.jsonl \
    --annotation_model google/gemma-2-9b-it \
    --temperature 0.0 \
    --seed 42 \
    --save_raw_outputs

# Step 5: Generate analysis
python analysis/analyze_traces.py \
    --annotated_file full_annotations.jsonl \
    --phase2_file runs/gemma-3-4b-xhosa-cot/phase2_dataset.jsonl \
    --output_dir results/
```

## Dependencies

Core dependencies:
- Python 3.8+
- `transformers` (for HuggingFace models)
- `torch` (for inference)
- `vllm` (optional, for faster batch inference)
- `sacrebleu` (for BLEU metrics)
- `comet` (for COMET metrics)
- `datasets` (for MetricX)

Install with:
```bash
pip install -r requirements-phase2.txt
```

## Deliverables

### Minimum
1. Annotation codebook (v1.0)
2. Pilot annotated dataset (50-100 examples)
3. Full annotated dataset
4. Annotation metadata
5. Summary statistics tables

### Recommended
1. Error analysis examples
2. Reproducibility report
3. Quality correlations
4. Visualizations
5. Audit report (10-20% manual review)

## References

- Main project: [`../README.md`](../README.md)
- Handoff document: [`../RC_LLM_HANDOFF.txt`](../RC_LLM_HANDOFF.txt)
- Work guidelines: [`../WORK_GUIDELINE.md`](../WORK_GUIDELINE.md)

## Contact

**Owner**: Richard Cheam [RC]  
**Version**: 1.0  
**Last Updated**: 2026-03-20
