# RC Quick Start Guide

**For**: Richard Cheam [RC]  
**Project**: LLM Reasoning for Machine Translation - Phase 2 Analysis  
**Date**: 2026-03-20

---

## What Has Been Prepared

Your Phase 2 annotation infrastructure is ready. Here's what's available:

### 📚 Documentation
- ✅ [`annotation_codebook_v1.md`](annotation_codebook_v1.md) - Complete annotation schema
- ✅ [`annotation_prompt_v1.txt`](annotation_prompt_v1.txt) - LLM prompt template
- ✅ [`RC_METHODOLOGY.md`](RC_METHODOLOGY.md) - Full methodology document
- ✅ [`README.md`](README.md) - Phase 2 infrastructure overview

### 🛠️ Scripts
- ✅ [`annotate_dataset.py`](annotate_dataset.py) - Annotation pipeline (manual + LLM)
- ✅ [`analyze_traces.py`](analyze_traces.py) - Statistical analysis generator
- ✅ Existing: [`build_phase2_dataset.py`](build_phase2_dataset.py), [`export_sentence_metrics.py`](export_sentence_metrics.py)

### 📋 Annotation Schema (Summary)
1. **Difficulty** (1-5, source-only)
2. **Linguistic Phenomena** (6 binary tags)
3. **Trace Type** (5 categories)
4. **Trace Usefulness** (helpful/neutral/harmful)
5. **Trace Overlap** (none/low/medium/high)

---

## Your First Steps

### Option A: Start with Manual Pilot (Recommended)

**Purpose**: Get familiar with the codebook and refine it

```bash
# 1. Check if you have a phase2 dataset already
# If not, create one from evaluation outputs:
python analysis/build_phase2_dataset.py \
    --run_dir path/to/evaluation/run

# 2. Run manual pilot annotation (interactive)
python analysis/annotate_dataset.py \
    --input_file path/to/phase2_dataset.jsonl \
    --output_file pilot_manual.jsonl \
    --manual_mode \
    --sample_size 50 \
    --annotator_id RC
```

**What happens**: The script will show you each example and prompt you for annotations interactively. This helps you:
- Understand the annotation categories
- Identify edge cases
- Refine the codebook if needed

**Time**: ~2-3 hours for 50 examples

### Option B: Jump to LLM-Assisted Annotation

**Purpose**: Annotate larger datasets quickly with quality control

```bash
# Annotate with LLM
python analysis/annotate_dataset.py \
    --input_file path/to/phase2_dataset.jsonl \
    --output_file llm_annotated.jsonl \
    --annotation_model google/gemma-2-9b-it \
    --temperature 0.0 \
    --seed 42 \
    --batch_size 8 \
    --save_raw_outputs \
    --annotator_id RC

# Generate analysis tables
python analysis/analyze_traces.py \
    --annotated_file llm_annotated.jsonl \
    --phase2_file path/to/phase2_dataset.jsonl \
    --output_dir results/
```

**Important**: Always audit 10-20% of LLM annotations manually!

---

## Recommended Workflow

### Week 1: Pilot Phase
```
Day 1-2: Manual annotation of 50-100 examples
Day 3: Review annotations, identify edge cases
Day 4: Refine codebook if needed (create v1.1)
Day 5: Re-annotate pilot with refined codebook
```

### Week 2: Full Annotation
```
Day 1: Set up LLM annotation pipeline
Day 2-3: Run LLM annotation on full dataset
Day 4-5: Manual audit of 10-20% sample
```

### Week 3: Analysis
```
Day 1-2: Generate descriptive statistics
Day 3-4: Create analysis tables and visualizations
Day 5: Write summary report
```

### Week 4: Deliverables
```
Day 1-2: Error analysis examples
Day 3: Reproducibility documentation
Day 4-5: Final report and presentations
```

---

## Critical Reminders

### ⚠️ Contamination Safety
- **NEVER** use reference translation for difficulty scoring
- **NEVER** use model translation for difficulty scoring
- **NEVER** use reasoning trace for difficulty scoring
- Difficulty is **SOURCE-ONLY**

### 🔒 Reproducibility
If using LLM annotation:
- ✅ Use fixed model with specific revision/commit hash
- ✅ Temperature = 0.0 (deterministic)
- ✅ Save raw outputs (`--save_raw_outputs`)
- ✅ Record all metadata
- ✅ Manual audit 10-20% of results

### 📊 Sampling Strategy
For full annotation, stratify by:
- Model (all models tested)
- Prompt type (direct, CoT templates, MAPS, etc.)
- Language pair
- Number of shots
- Quality (high and low BLEU)
- Trace length (short and long)

---

## Common Commands Reference

### Build Phase 2 Dataset
```bash
# From evaluation run
python analysis/build_phase2_dataset.py --run_dir <RUN_DIR>

# With metrics
python analysis/export_sentence_metrics.py --run_dir <RUN_DIR> --metrics bleu comet
python analysis/build_phase2_dataset.py --run_dir <RUN_DIR>
```

### Manual Annotation
```bash
python analysis/annotate_dataset.py \
    --input_file phase2_dataset.jsonl \
    --output_file manual_annotations.jsonl \
    --manual_mode \
    --sample_size 100
```

### LLM Annotation (HuggingFace)
```bash
python analysis/annotate_dataset.py \
    --input_file phase2_dataset.jsonl \
    --output_file llm_annotations.jsonl \
    --annotation_model google/gemma-2-9b-it \
    --model_revision <COMMIT_HASH> \
    --inference_api hf \
    --temperature 0.0 \
    --seed 42 \
    --save_raw_outputs
```

### LLM Annotation (vLLM - faster for GPU)
```bash
python analysis/annotate_dataset.py \
    --input_file phase2_dataset.jsonl \
    --output_file llm_annotations.jsonl \
    --annotation_model google/gemma-2-9b-it \
    --inference_api vllm \
    --temperature 0.0 \
    --batch_size 32 \
    --save_raw_outputs
```

### Generate Analysis
```bash
python analysis/analyze_traces.py \
    --annotated_file annotations.jsonl \
    --phase2_file phase2_dataset.jsonl \
    --output_dir results/
```

---

## Troubleshooting

### "No such file or directory: phase2_dataset.jsonl"
You need to build the Phase 2 dataset first from evaluation runs:
```bash
python analysis/build_phase2_dataset.py --run_dir <PATH_TO_EVALUATION_RUN>
```

### "CUDA out of memory" during LLM annotation
Reduce batch size or use CPU:
```bash
--batch_size 1 --device cpu
```

### LLM annotation produces parse errors
Check the raw outputs to see what the model generated:
```bash
# Raw outputs are saved to <output_file>_raw.jsonl
# Review and adjust prompt template if needed
```

### Manual mode is too slow
Start with a smaller pilot (20-30 examples) to get familiar, then switch to LLM-assisted annotation with manual audit.

---

## Expected Deliverables

### Minimum
1. ✅ Annotation codebook
2. Pilot annotated dataset (50-100 examples)
3. Full annotated dataset (500-1000+ examples)
4. Annotation metadata (provenance)
5. Summary statistics tables

### Strong (Recommended)
6. Error analysis examples (10-20 per trace type)
7. Reproducibility report
8. Quality correlation analysis
9. Visualizations (charts, heatmaps)
10. Audit report

---

## File Outputs

After annotation, you'll have:

```
analysis/
├── phase2_dataset.jsonl          # Input data
├── pilot_manual.jsonl            # Pilot annotations
├── llm_annotations.jsonl         # Main annotations
├── llm_annotations_raw.jsonl     # Raw LLM outputs
├── llm_annotations_metadata.json # Provenance
└── results/
    ├── SUMMARY.md
    ├── difficulty_distribution.md
    ├── phenomena_frequencies.md
    ├── trace_type_distribution.md
    ├── usefulness_distribution.md
    ├── overlap_distribution.md
    ├── crosstab_*.md
    └── quality_correlations.md
```

---

## Need Help?

### Resources
- **Codebook**: [`annotation_codebook_v1.md`](annotation_codebook_v1.md) - Detailed definitions
- **Methodology**: [`RC_METHODOLOGY.md`](RC_METHODOLOGY.md) - Complete protocol
- **README**: [`README.md`](README.md) - Infrastructure overview
- **Handoff**: [`../RC_LLM_HANDOFF.txt`](../RC_LLM_HANDOFF.txt) - Original requirements

### Key Principles
1. **Contamination-safe**: Difficulty is source-only
2. **Reproducible**: Fixed models, prompts, settings, metadata
3. **Auditable**: Manual review of 10-20% of LLM annotations
4. **Documented**: Every decision, edge case, refinement
5. **Stratified**: Representative sampling across conditions

---

## Quick Sanity Checks

Before starting full annotation:
- [ ] Read the annotation codebook
- [ ] Try manual annotation on 5 examples
- [ ] Understand difficulty scoring (source-only!)
- [ ] Understand the 5 trace types
- [ ] Know the difference between idiom and figurative language
- [ ] Know when to mark a trace as "helpful" vs "neutral"

Before finalizing:
- [ ] Manual audit completed (10-20%)
- [ ] Annotation metadata saved
- [ ] Analysis tables generated
- [ ] Summary statistics make sense
- [ ] Reproducibility instructions documented

---

**Ready to start!**

Begin with Option A (manual pilot) if you want to get familiar with the schema, or Option B (LLM-assisted) if you're confident with the codebook and ready to scale.

**Good luck!**  
— Automated setup completed 2026-03-20
