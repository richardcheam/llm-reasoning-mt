# Phase 2 Comprehensive Analysis

**Total Examples Analyzed**: 64

---

## 1. Difficulty Distribution

Distribution of translation difficulty scores (1=easiest, 5=hardest):

| Difficulty Score | Count | Percentage |
|-----------------|-------|------------|
| 1 | 4 | 6.3% |
| 2 | 20 | 31.7% |
| 3 | 35 | 55.6% |
| 4 | 3 | 4.8% |
| 5 | 1 | 1.6% |

## 2. Linguistic Phenomena Frequencies

Frequency of linguistic phenomena across 63 examples:

| Phenomenon | Count | Percentage |
|------------|-------|------------|
| long_distance_dependency | 54 | 85.7% |
| complex_syntax | 36 | 57.1% |
| named_entities | 35 | 55.6% |

## 3. Primary Trace Type Distribution

Distribution of reasoning trace types (n=63):

| Trace Type | Count | Percentage |
|------------|-------|------------|
| TRANSLATION_ATTEMPT | 28 | 44.4% |
| neutral | 20 | 31.7% |
| NONE | 9 | 14.3% |
| VACUOUS_FILLER | 3 | 4.8% |
| CORRECT_LINGUISTIC_ANALYSIS | 3 | 4.8% |

## 4. Trace Usefulness Distribution

Distribution of trace usefulness ratings:

| Usefulness Level | Count | Percentage |
|------------------|-------|------------|
| Medium | 1 | 1.6% |
| high | 3 | 4.8% |
| medium | 31 | 49.2% |
| neutral | 28 | 44.4% |

## 5. Trace-Translation Overlap Distribution

Distribution of overlap between reasoning traces and translations:

| Overlap Level | Count | Percentage |
|---------------|-------|------------|
| none | 4 | 100.0% |

## 6. Cross-Tabulations

### 6.1 Difficulty × Trace Type

| Difficulty | CORRECT_LINGUISTIC_ANALYSIS | NONE | TRANSLATION_ATTEMPT | VACUOUS_FILLER | neutral |
|---|---|---|---|---|---|
| 1 | 0 | 1 | 0 | 0 | 3 |
| 2 | 1 | 2 | 0 | 1 | 16 |
| 3 | 1 | 6 | 25 | 2 | 1 |
| 4 | 0 | 0 | 3 | 0 | 0 |
| 5 | 1 | 0 | 0 | 0 | 0 |

### 6.2 Trace Type × Usefulness

| Trace Type | Medium | high | medium | neutral |
|---|---|---|---|---|
| CORRECT_LINGUISTIC_ANALYSIS | 0 | 2 | 0 | 1 |
| NONE | 0 | 0 | 2 | 7 |
| TRANSLATION_ATTEMPT | 1 | 1 | 25 | 1 |
| VACUOUS_FILLER | 0 | 0 | 0 | 3 |
| neutral | 0 | 0 | 4 | 16 |

## 7. Translation Quality Correlations

### COMET Metric

**Average COMET by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| Medium | 0.73 |
| high | 0.48 |
| medium | 0.75 |
| neutral | 0.73 |

**Average COMET by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| neutral | 0.82 |
| TRANSLATION_ATTEMPT | 0.74 |
| CORRECT_LINGUISTIC_ANALYSIS | 0.66 |
| NONE | 0.65 |
| VACUOUS_FILLER | 0.40 |

**Average COMET by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| none | 0.90 |

---

### BLEU Metric

**Average BLEU by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| Medium | 8.97 |
| high | 3.70 |
| medium | 10.70 |
| neutral | 13.75 |

**Average BLEU by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| neutral | 16.24 |
| NONE | 13.49 |
| TRANSLATION_ATTEMPT | 9.36 |
| CORRECT_LINGUISTIC_ANALYSIS | 6.45 |
| VACUOUS_FILLER | 3.02 |

**Average BLEU by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| none | 8.86 |

---

### chrF++ Metric

**Average chrF++ by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| Medium | 29.82 |
| high | 20.03 |
| medium | 34.94 |
| neutral | 35.39 |

**Average chrF++ by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| neutral | 39.76 |
| NONE | 33.92 |
| TRANSLATION_ATTEMPT | 33.11 |
| CORRECT_LINGUISTIC_ANALYSIS | 30.21 |
| VACUOUS_FILLER | 15.31 |

**Average chrF++ by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| none | 35.29 |

---

### MetricX-24 Metric

**Average MetricX-24 by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| Medium | 6.25 |
| high | 14.48 |
| medium | 9.30 |
| neutral | 9.03 |

**Average MetricX-24 by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| CORRECT_LINGUISTIC_ANALYSIS | 13.48 |
| VACUOUS_FILLER | 11.69 |
| NONE | 10.30 |
| TRANSLATION_ATTEMPT | 9.77 |
| neutral | 7.46 |

**Average MetricX-24 by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| none | 5.98 |

---

## 8. Key Insights

- **Best performing trace type**: neutral (BLEU: 16.24)
- **Worst performing trace type**: VACUOUS_FILLER (BLEU: 3.02)
- **Performance gap**: 437.1% improvement from worst to best

- **Most common trace type**: TRANSLATION_ATTEMPT (28 examples, 44.4%)
- **Average difficulty score**: 2.63/5.0

---

*Analysis generated from evaluations/comprehensive_cot_eval/English_Finnish/gemma-3-1b-it/English_to_Finnish_0_shot_seed_42_identity_None_0_0_0/phase2_annotations.jsonl*
