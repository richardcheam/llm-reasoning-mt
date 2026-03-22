# Phase 2 Comprehensive Analysis

**Total Examples Analyzed**: 64

---

## 1. Difficulty Distribution

Distribution of translation difficulty scores (1=easiest, 5=hardest):

| Difficulty Score | Count | Percentage |
|-----------------|-------|------------|
| 2 | 5 | 7.8% |
| 3 | 52 | 81.2% |
| 4 | 6 | 9.4% |
| 5 | 1 | 1.6% |

## 2. Linguistic Phenomena Frequencies

Frequency of linguistic phenomena across 64 examples:

| Phenomenon | Count | Percentage |
|------------|-------|------------|
| long_distance_dependency | 64 | 100.0% |
| complex_syntax | 51 | 79.7% |
| named_entities | 43 | 67.2% |
| ambiguity | 2 | 3.1% |
| idiom | 2 | 3.1% |
| figurative_language | 2 | 3.1% |

## 3. Primary Trace Type Distribution

Distribution of reasoning trace types (n=64):

| Trace Type | Count | Percentage |
|------------|-------|------------|
| TRANSLATION_ATTEMPT | 35 | 54.7% |
| CORRECT_LINGUISTIC_ANALYSIS | 18 | 28.1% |
| NONE | 5 | 7.8% |
| neutral | 4 | 6.2% |
| correct_linguistic_analysis | 2 | 3.1% |

## 4. Trace Usefulness Distribution

Distribution of trace usefulness ratings:

| Usefulness Level | Count | Percentage |
|------------------|-------|------------|
| 1 | 1 | 1.6% |
| 3 | 1 | 1.6% |
| High | 1 | 1.6% |
| Medium | 3 | 4.7% |
| high | 7 | 10.9% |
| medium | 46 | 71.9% |
| neutral | 5 | 7.8% |

## 5. Trace-Translation Overlap Distribution

Distribution of overlap between reasoning traces and translations:

| Overlap Level | Count | Percentage |
|---------------|-------|------------|
| 0 | 1 | 5.9% |
| none | 16 | 94.1% |

## 6. Cross-Tabulations

### 6.1 Difficulty × Trace Type

| Difficulty | CORRECT_LINGUISTIC_ANALYSIS | NONE | TRANSLATION_ATTEMPT | correct_linguistic_analysis | neutral |
|---|---|---|---|---|---|
| 2 | 0 | 2 | 0 | 0 | 3 |
| 3 | 16 | 3 | 31 | 1 | 1 |
| 4 | 1 | 0 | 4 | 1 | 0 |
| 5 | 1 | 0 | 0 | 0 | 0 |

### 6.2 Trace Type × Usefulness

| Trace Type | 1 | 3 | High | Medium | high | medium | neutral |
|---|---|---|---|---|---|---|---|
| CORRECT_LINGUISTIC_ANALYSIS | 0 | 0 | 1 | 1 | 4 | 12 | 0 |
| NONE | 1 | 0 | 0 | 0 | 0 | 2 | 2 |
| TRANSLATION_ATTEMPT | 0 | 1 | 0 | 2 | 2 | 29 | 1 |
| correct_linguistic_analysis | 0 | 0 | 0 | 0 | 1 | 1 | 0 |
| neutral | 0 | 0 | 0 | 0 | 0 | 2 | 2 |

## 7. Translation Quality Correlations

### COMET Metric

**Average COMET by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 1 | 0.76 |
| 3 | 0.75 |
| High | 0.79 |
| Medium | 0.85 |
| high | 0.72 |
| medium | 0.72 |
| neutral | 0.81 |

**Average COMET by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| correct_linguistic_analysis | 0.79 |
| neutral | 0.79 |
| CORRECT_LINGUISTIC_ANALYSIS | 0.74 |
| TRANSLATION_ATTEMPT | 0.73 |
| NONE | 0.69 |

**Average COMET by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| 0 | 0.76 |
| none | 0.70 |

---

### MetricX-24 Metric

**Average MetricX-24 by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 1 | 11.56 |
| 3 | 7.69 |
| High | 11.88 |
| Medium | 4.73 |
| high | 9.74 |
| medium | 9.99 |
| neutral | 9.37 |

**Average MetricX-24 by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| NONE | 12.49 |
| TRANSLATION_ATTEMPT | 9.89 |
| CORRECT_LINGUISTIC_ANALYSIS | 9.18 |
| correct_linguistic_analysis | 8.52 |
| neutral | 7.31 |

**Average MetricX-24 by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| 0 | 11.56 |
| none | 10.86 |

---

### chrF++ Metric

**Average chrF++ by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 1 | 27.13 |
| 3 | 42.48 |
| High | 42.08 |
| Medium | 34.83 |
| high | 37.71 |
| medium | 34.28 |
| neutral | 40.13 |

**Average chrF++ by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| CORRECT_LINGUISTIC_ANALYSIS | 38.72 |
| neutral | 35.23 |
| TRANSLATION_ATTEMPT | 34.57 |
| NONE | 33.02 |
| correct_linguistic_analysis | 22.38 |

**Average chrF++ by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| 0 | 27.13 |
| none | 30.45 |

---

### BLEU Metric

**Average BLEU by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 1 | 3.13 |
| 3 | 25.31 |
| High | 13.96 |
| Medium | 9.72 |
| high | 11.71 |
| medium | 10.92 |
| neutral | 21.29 |

**Average BLEU by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| neutral | 18.46 |
| CORRECT_LINGUISTIC_ANALYSIS | 15.30 |
| TRANSLATION_ATTEMPT | 10.41 |
| NONE | 8.93 |
| correct_linguistic_analysis | 2.01 |

**Average BLEU by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| 0 | 3.13 |
| none | 8.04 |

---

## 8. Key Insights

- **Best performing trace type**: neutral (BLEU: 18.46)
- **Worst performing trace type**: correct_linguistic_analysis (BLEU: 2.01)
- **Performance gap**: 817.1% improvement from worst to best

- **Most common trace type**: TRANSLATION_ATTEMPT (35 examples, 54.7%)
- **Average difficulty score**: 3.05/5.0

---

*Analysis generated from evaluations/guided_cot_eval/English_Finnish/gemma-3-1b-it/English_to_Finnish_0_shot_seed_42_identity_None_0_0_0/phase2_annotations.jsonl*
