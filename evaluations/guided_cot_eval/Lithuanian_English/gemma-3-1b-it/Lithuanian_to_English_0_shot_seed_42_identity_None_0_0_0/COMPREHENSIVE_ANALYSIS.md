# Phase 2 Comprehensive Analysis

**Total Examples Analyzed**: 64

---

## 1. Difficulty Distribution

Distribution of translation difficulty scores (1=easiest, 5=hardest):

| Difficulty Score | Count | Percentage |
|-----------------|-------|------------|
| 1 | 1 | 1.6% |
| 2 | 13 | 21.0% |
| 3 | 42 | 67.7% |
| 4 | 5 | 8.1% |
| 5 | 1 | 1.6% |

## 2. Linguistic Phenomena Frequencies

Frequency of linguistic phenomena across 62 examples:

| Phenomenon | Count | Percentage |
|------------|-------|------------|
| long_distance_dependency | 56 | 90.3% |
| named_entities | 47 | 75.8% |
| complex_syntax | 37 | 59.7% |

## 3. Primary Trace Type Distribution

Distribution of reasoning trace types (n=62):

| Trace Type | Count | Percentage |
|------------|-------|------------|
| NONE | 25 | 40.3% |
| CORRECT_LINGUISTIC_ANALYSIS | 13 | 21.0% |
| TRANSLATION_ATTEMPT | 12 | 19.4% |
| neutral | 7 | 11.3% |
| correct_linguistic_analysis | 3 | 4.8% |
| REASONING | 1 | 1.6% |
| REPETITION | 1 | 1.6% |

## 4. Trace Usefulness Distribution

Distribution of trace usefulness ratings:

| Usefulness Level | Count | Percentage |
|------------------|-------|------------|
| high | 15 | 24.2% |
| medium | 29 | 46.8% |
| neutral | 18 | 29.0% |

## 5. Trace-Translation Overlap Distribution

Distribution of overlap between reasoning traces and translations:

| Overlap Level | Count | Percentage |
|---------------|-------|------------|
| none | 9 | 100.0% |

## 6. Cross-Tabulations

### 6.1 Difficulty × Trace Type

| Difficulty | CORRECT_LINGUISTIC_ANALYSIS | NONE | REASONING | REPETITION | TRANSLATION_ATTEMPT | correct_linguistic_analysis | neutral |
|---|---|---|---|---|---|---|---|
| 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |
| 2 | 1 | 6 | 0 | 0 | 0 | 2 | 4 |
| 3 | 10 | 18 | 1 | 1 | 8 | 1 | 3 |
| 4 | 1 | 0 | 0 | 0 | 4 | 0 | 0 |
| 5 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |

### 6.2 Trace Type × Usefulness

| Trace Type | high | medium | neutral |
|---|---|---|---|
| CORRECT_LINGUISTIC_ANALYSIS | 10 | 3 | 0 |
| NONE | 0 | 11 | 14 |
| REASONING | 1 | 0 | 0 |
| REPETITION | 0 | 0 | 1 |
| TRANSLATION_ATTEMPT | 3 | 9 | 0 |
| correct_linguistic_analysis | 1 | 2 | 0 |
| neutral | 0 | 4 | 3 |

## 7. Translation Quality Correlations

### MetricX-24 Metric

**Average MetricX-24 by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| high | 9.98 |
| medium | 9.26 |
| neutral | 9.34 |

**Average MetricX-24 by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| TRANSLATION_ATTEMPT | 10.29 |
| CORRECT_LINGUISTIC_ANALYSIS | 9.73 |
| NONE | 9.68 |
| neutral | 8.39 |
| correct_linguistic_analysis | 8.39 |
| REASONING | 7.28 |
| REPETITION | 3.45 |

**Average MetricX-24 by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| none | 11.07 |

---

### COMET Metric

**Average COMET by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| high | 0.75 |
| medium | 0.73 |
| neutral | 0.76 |

**Average COMET by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| REPETITION | 0.85 |
| REASONING | 0.83 |
| correct_linguistic_analysis | 0.76 |
| neutral | 0.75 |
| CORRECT_LINGUISTIC_ANALYSIS | 0.75 |
| NONE | 0.74 |
| TRANSLATION_ATTEMPT | 0.72 |

**Average COMET by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| none | 0.70 |

---

### BLEU Metric

**Average BLEU by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| high | 14.44 |
| medium | 11.63 |
| neutral | 14.93 |

**Average BLEU by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| REPETITION | 18.06 |
| neutral | 17.55 |
| REASONING | 16.47 |
| CORRECT_LINGUISTIC_ANALYSIS | 14.69 |
| NONE | 12.46 |
| TRANSLATION_ATTEMPT | 11.13 |
| correct_linguistic_analysis | 9.76 |

**Average BLEU by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| none | 8.69 |

---

### chrF++ Metric

**Average chrF++ by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| high | 36.56 |
| medium | 34.98 |
| neutral | 38.00 |

**Average chrF++ by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| REPETITION | 46.21 |
| neutral | 38.73 |
| CORRECT_LINGUISTIC_ANALYSIS | 38.60 |
| NONE | 36.26 |
| REASONING | 34.78 |
| TRANSLATION_ATTEMPT | 33.00 |
| correct_linguistic_analysis | 30.08 |

**Average chrF++ by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| none | 29.58 |

---

## 8. Key Insights

- **Best performing trace type**: REPETITION (BLEU: 18.06)
- **Worst performing trace type**: correct_linguistic_analysis (BLEU: 9.76)
- **Performance gap**: 85.0% improvement from worst to best

- **Most common trace type**: NONE (25 examples, 40.3%)
- **Average difficulty score**: 2.87/5.0

---

*Analysis generated from evaluations/guided_cot_eval/Lithuanian_English/gemma-3-1b-it/Lithuanian_to_English_0_shot_seed_42_identity_None_0_0_0/phase2_annotations.jsonl*
