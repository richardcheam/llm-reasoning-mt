# Phase 2 Comprehensive Analysis

**Total Examples Analyzed**: 64

---

## 1. Difficulty Distribution

Distribution of translation difficulty scores (1=easiest, 5=hardest):

| Difficulty Score | Count | Percentage |
|-----------------|-------|------------|
| 2 | 4 | 6.3% |
| 3 | 53 | 84.1% |
| 4 | 6 | 9.5% |

## 2. Linguistic Phenomena Frequencies

Frequency of linguistic phenomena across 63 examples:

| Phenomenon | Count | Percentage |
|------------|-------|------------|
| long_distance_dependency | 63 | 100.0% |
| complex_syntax | 49 | 77.8% |
| named_entities | 38 | 60.3% |
| ambiguity | 1 | 1.6% |
| idiom | 1 | 1.6% |
| figurative_language | 1 | 1.6% |

## 3. Primary Trace Type Distribution

Distribution of reasoning trace types (n=63):

| Trace Type | Count | Percentage |
|------------|-------|------------|
| TRANSLATION_ATTEMPT | 22 | 34.9% |
| NONE | 15 | 23.8% |
| CORRECT_LINGUISTIC_ANALYSIS | 15 | 23.8% |
| neutral | 8 | 12.7% |
| REPETITION | 2 | 3.2% |
| correct_linguistic_analysis | 1 | 1.6% |

## 4. Trace Usefulness Distribution

Distribution of trace usefulness ratings:

| Usefulness Level | Count | Percentage |
|------------------|-------|------------|
| 1 | 1 | 1.6% |
| High | 2 | 3.2% |
| Medium | 2 | 3.2% |
| high | 4 | 6.3% |
| medium | 45 | 71.4% |
| neutral | 9 | 14.3% |

## 5. Trace-Translation Overlap Distribution

Distribution of overlap between reasoning traces and translations:

| Overlap Level | Count | Percentage |
|---------------|-------|------------|
| 0 | 1 | 8.3% |
| none | 11 | 91.7% |

## 6. Cross-Tabulations

### 6.1 Difficulty × Trace Type

| Difficulty | CORRECT_LINGUISTIC_ANALYSIS | NONE | REPETITION | TRANSLATION_ATTEMPT | correct_linguistic_analysis | neutral |
|---|---|---|---|---|---|---|
| 2 | 0 | 0 | 0 | 0 | 0 | 4 |
| 3 | 13 | 14 | 2 | 19 | 1 | 4 |
| 4 | 2 | 1 | 0 | 3 | 0 | 0 |

### 6.2 Trace Type × Usefulness

| Trace Type | 1 | High | Medium | high | medium | neutral |
|---|---|---|---|---|---|---|
| CORRECT_LINGUISTIC_ANALYSIS | 0 | 1 | 0 | 3 | 11 | 0 |
| NONE | 1 | 0 | 0 | 0 | 9 | 5 |
| REPETITION | 0 | 0 | 0 | 0 | 1 | 1 |
| TRANSLATION_ATTEMPT | 0 | 1 | 2 | 1 | 18 | 0 |
| correct_linguistic_analysis | 0 | 0 | 0 | 0 | 1 | 0 |
| neutral | 0 | 0 | 0 | 0 | 5 | 3 |

## 7. Translation Quality Correlations

### MetricX-24 Metric

**Average MetricX-24 by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 1 | 10.19 |
| High | 9.05 |
| Medium | 11.03 |
| high | 10.98 |
| medium | 8.77 |
| neutral | 7.79 |

**Average MetricX-24 by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| REPETITION | 10.52 |
| TRANSLATION_ATTEMPT | 10.17 |
| CORRECT_LINGUISTIC_ANALYSIS | 9.49 |
| NONE | 7.40 |
| neutral | 7.19 |
| correct_linguistic_analysis | 3.61 |

**Average MetricX-24 by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| 0 | 10.19 |
| none | 10.19 |

---

### chrF++ Metric

**Average chrF++ by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 1 | 30.97 |
| High | 37.63 |
| Medium | 30.51 |
| high | 24.77 |
| medium | 36.29 |
| neutral | 33.50 |

**Average chrF++ by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| correct_linguistic_analysis | 50.87 |
| NONE | 42.78 |
| REPETITION | 35.55 |
| CORRECT_LINGUISTIC_ANALYSIS | 33.92 |
| TRANSLATION_ATTEMPT | 31.51 |
| neutral | 29.36 |

**Average chrF++ by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| 0 | 30.97 |
| none | 24.01 |

---

### COMET Metric

**Average COMET by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 1 | 0.82 |
| High | 0.79 |
| Medium | 0.61 |
| high | 0.66 |
| medium | 0.75 |
| neutral | 0.73 |

**Average COMET by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| correct_linguistic_analysis | 0.91 |
| NONE | 0.81 |
| neutral | 0.78 |
| CORRECT_LINGUISTIC_ANALYSIS | 0.76 |
| TRANSLATION_ATTEMPT | 0.67 |
| REPETITION | 0.66 |

**Average COMET by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| 0 | 0.82 |
| none | 0.63 |

---

### BLEU Metric

**Average BLEU by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 1 | 6.67 |
| High | 9.31 |
| Medium | 11.67 |
| high | 6.08 |
| medium | 17.00 |
| neutral | 13.03 |

**Average BLEU by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| correct_linguistic_analysis | 29.92 |
| NONE | 22.18 |
| REPETITION | 15.07 |
| TRANSLATION_ATTEMPT | 13.20 |
| CORRECT_LINGUISTIC_ANALYSIS | 13.01 |
| neutral | 9.60 |

**Average BLEU by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| 0 | 6.67 |
| none | 4.87 |

---

## 8. Key Insights

- **Best performing trace type**: correct_linguistic_analysis (BLEU: 29.92)
- **Worst performing trace type**: neutral (BLEU: 9.60)
- **Performance gap**: 211.6% improvement from worst to best

- **Most common trace type**: TRANSLATION_ATTEMPT (22 examples, 34.9%)
- **Average difficulty score**: 3.03/5.0

---

*Analysis generated from evaluations/guided_cot_eval/English_Turkish/gemma-3-1b-it/English_to_Turkish_0_shot_seed_42_identity_None_0_0_0/phase2_annotations.jsonl*
