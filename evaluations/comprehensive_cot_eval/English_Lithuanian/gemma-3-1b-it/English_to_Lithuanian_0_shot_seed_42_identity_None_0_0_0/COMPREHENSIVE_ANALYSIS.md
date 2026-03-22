# Phase 2 Comprehensive Analysis

**Total Examples Analyzed**: 64

---

## 1. Difficulty Distribution

Distribution of translation difficulty scores (1=easiest, 5=hardest):

| Difficulty Score | Count | Percentage |
|-----------------|-------|------------|
| 1 | 2 | 3.2% |
| 2 | 12 | 19.0% |
| 3 | 42 | 66.7% |
| 4 | 6 | 9.5% |
| 5 | 1 | 1.6% |

## 2. Linguistic Phenomena Frequencies

Frequency of linguistic phenomena across 63 examples:

| Phenomenon | Count | Percentage |
|------------|-------|------------|
| long_distance_dependency | 59 | 93.7% |
| complex_syntax | 49 | 77.8% |
| named_entities | 36 | 57.1% |

## 3. Primary Trace Type Distribution

Distribution of reasoning trace types (n=63):

| Trace Type | Count | Percentage |
|------------|-------|------------|
| NONE | 20 | 31.7% |
| TRANSLATION_ATTEMPT | 13 | 20.6% |
| neutral | 11 | 17.5% |
| CORRECT_LINGUISTIC_ANALYSIS | 8 | 12.7% |
| correct_linguistic_analysis | 8 | 12.7% |
| REPETITION | 1 | 1.6% |
| null | 1 | 1.6% |
| VACUOUS_FILLER | 1 | 1.6% |

## 4. Trace Usefulness Distribution

Distribution of trace usefulness ratings:

| Usefulness Level | Count | Percentage |
|------------------|-------|------------|
| Medium | 3 | 4.8% |
| high | 3 | 4.8% |
| medium | 27 | 42.9% |
| neutral | 30 | 47.6% |

## 5. Trace-Translation Overlap Distribution

Distribution of overlap between reasoning traces and translations:

| Overlap Level | Count | Percentage |
|---------------|-------|------------|
| low | 3 | 13.0% |
| none | 20 | 87.0% |

## 6. Cross-Tabulations

### 6.1 Difficulty × Trace Type

| Difficulty | CORRECT_LINGUISTIC_ANALYSIS | NONE | REPETITION | TRANSLATION_ATTEMPT | VACUOUS_FILLER | correct_linguistic_analysis | neutral | null |
|---|---|---|---|---|---|---|---|---|
| 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 |
| 2 | 0 | 4 | 0 | 0 | 1 | 0 | 7 | 0 |
| 3 | 6 | 16 | 1 | 10 | 0 | 6 | 3 | 0 |
| 4 | 1 | 0 | 0 | 3 | 0 | 2 | 0 | 0 |
| 5 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

### 6.2 Trace Type × Usefulness

| Trace Type | Medium | high | medium | neutral |
|---|---|---|---|---|
| CORRECT_LINGUISTIC_ANALYSIS | 0 | 1 | 7 | 0 |
| NONE | 0 | 0 | 0 | 20 |
| REPETITION | 0 | 0 | 1 | 0 |
| TRANSLATION_ATTEMPT | 3 | 0 | 10 | 0 |
| VACUOUS_FILLER | 0 | 0 | 0 | 1 |
| correct_linguistic_analysis | 0 | 1 | 7 | 0 |
| neutral | 0 | 1 | 2 | 8 |
| null | 0 | 0 | 0 | 1 |

## 7. Translation Quality Correlations

### MetricX-24 Metric

**Average MetricX-24 by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| Medium | 18.62 |
| high | 7.45 |
| medium | 15.77 |
| neutral | 15.33 |

**Average MetricX-24 by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| TRANSLATION_ATTEMPT | 17.18 |
| null | 16.75 |
| CORRECT_LINGUISTIC_ANALYSIS | 15.54 |
| NONE | 15.26 |
| REPETITION | 14.50 |
| correct_linguistic_analysis | 14.48 |
| neutral | 13.72 |
| VACUOUS_FILLER | 13.19 |

**Average MetricX-24 by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| low | 18.08 |
| none | 15.84 |

---

### COMET Metric

**Average COMET by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| Medium | 0.39 |
| high | 0.66 |
| medium | 0.47 |
| neutral | 0.50 |

**Average COMET by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| REPETITION | 0.66 |
| VACUOUS_FILLER | 0.62 |
| neutral | 0.53 |
| NONE | 0.50 |
| correct_linguistic_analysis | 0.49 |
| TRANSLATION_ATTEMPT | 0.45 |
| CORRECT_LINGUISTIC_ANALYSIS | 0.45 |
| null | 0.37 |

**Average COMET by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| low | 0.42 |
| none | 0.46 |

---

### chrF++ Metric

**Average chrF++ by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| Medium | 22.31 |
| high | 24.91 |
| medium | 23.44 |
| neutral | 26.26 |

**Average chrF++ by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| REPETITION | 32.75 |
| neutral | 31.09 |
| NONE | 24.62 |
| null | 23.38 |
| TRANSLATION_ATTEMPT | 23.18 |
| CORRECT_LINGUISTIC_ANALYSIS | 22.21 |
| correct_linguistic_analysis | 21.89 |
| VACUOUS_FILLER | 17.67 |

**Average chrF++ by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| low | 27.35 |
| none | 20.19 |

---

### BLEU Metric

**Average BLEU by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| Medium | 2.32 |
| high | 6.71 |
| medium | 5.01 |
| neutral | 7.29 |

**Average BLEU by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| REPETITION | 19.93 |
| neutral | 11.37 |
| NONE | 5.28 |
| CORRECT_LINGUISTIC_ANALYSIS | 4.87 |
| TRANSLATION_ATTEMPT | 4.63 |
| correct_linguistic_analysis | 3.46 |
| null | 2.50 |
| VACUOUS_FILLER | 1.35 |

**Average BLEU by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| low | 2.70 |
| none | 3.54 |

---

## 8. Key Insights

- **Best performing trace type**: REPETITION (BLEU: 19.93)
- **Worst performing trace type**: VACUOUS_FILLER (BLEU: 1.35)
- **Performance gap**: 1371.3% improvement from worst to best

- **Most common trace type**: NONE (20 examples, 31.7%)
- **Average difficulty score**: 2.87/5.0

---

*Analysis generated from evaluations/comprehensive_cot_eval/English_Lithuanian/gemma-3-1b-it/English_to_Lithuanian_0_shot_seed_42_identity_None_0_0_0/phase2_annotations.jsonl*
