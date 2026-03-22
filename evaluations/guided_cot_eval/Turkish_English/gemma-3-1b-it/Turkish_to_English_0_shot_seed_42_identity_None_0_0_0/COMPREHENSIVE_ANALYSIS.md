# Phase 2 Comprehensive Analysis

**Total Examples Analyzed**: 64

---

## 1. Difficulty Distribution

Distribution of translation difficulty scores (1=easiest, 5=hardest):

| Difficulty Score | Count | Percentage |
|-----------------|-------|------------|
| 2 | 15 | 23.8% |
| 3 | 48 | 76.2% |

## 2. Linguistic Phenomena Frequencies

Frequency of linguistic phenomena across 63 examples:

| Phenomenon | Count | Percentage |
|------------|-------|------------|
| long_distance_dependency | 59 | 93.7% |
| named_entities | 54 | 85.7% |
| complex_syntax | 43 | 68.3% |
| ambiguity | 1 | 1.6% |
| idiom | 1 | 1.6% |
| figurative_language | 1 | 1.6% |

## 3. Primary Trace Type Distribution

Distribution of reasoning trace types (n=63):

| Trace Type | Count | Percentage |
|------------|-------|------------|
| NONE | 25 | 39.7% |
| TRANSLATION_ATTEMPT | 18 | 28.6% |
| neutral | 10 | 15.9% |
| CORRECT_LINGUISTIC_ANALYSIS | 8 | 12.7% |
| correct_linguistic_analysis | 2 | 3.2% |

## 4. Trace Usefulness Distribution

Distribution of trace usefulness ratings:

| Usefulness Level | Count | Percentage |
|------------------|-------|------------|
| 1 | 1 | 1.6% |
| high | 11 | 17.5% |
| medium | 35 | 55.6% |
| neutral | 16 | 25.4% |

## 5. Trace-Translation Overlap Distribution

Distribution of overlap between reasoning traces and translations:

| Overlap Level | Count | Percentage |
|---------------|-------|------------|
| none | 3 | 75.0% |
| null | 1 | 25.0% |

## 6. Cross-Tabulations

### 6.1 Difficulty × Trace Type

| Difficulty | CORRECT_LINGUISTIC_ANALYSIS | NONE | TRANSLATION_ATTEMPT | correct_linguistic_analysis | neutral |
|---|---|---|---|---|---|
| 2 | 1 | 5 | 0 | 1 | 8 |
| 3 | 7 | 20 | 18 | 1 | 2 |

### 6.2 Trace Type × Usefulness

| Trace Type | 1 | high | medium | neutral |
|---|---|---|---|---|
| CORRECT_LINGUISTIC_ANALYSIS | 0 | 8 | 0 | 0 |
| NONE | 1 | 0 | 15 | 9 |
| TRANSLATION_ATTEMPT | 0 | 2 | 16 | 0 |
| correct_linguistic_analysis | 0 | 1 | 1 | 0 |
| neutral | 0 | 0 | 3 | 7 |

## 7. Translation Quality Correlations

### chrF++ Metric

**Average chrF++ by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 1 | 41.72 |
| high | 34.93 |
| medium | 40.88 |
| neutral | 48.07 |

**Average chrF++ by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| neutral | 45.65 |
| NONE | 43.04 |
| TRANSLATION_ATTEMPT | 41.88 |
| CORRECT_LINGUISTIC_ANALYSIS | 34.92 |
| correct_linguistic_analysis | 30.10 |

**Average chrF++ by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| none | 39.76 |
| null | 41.72 |

---

### COMET Metric

**Average COMET by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 1 | 0.77 |
| high | 0.74 |
| medium | 0.82 |
| neutral | 0.87 |

**Average COMET by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| neutral | 0.87 |
| NONE | 0.85 |
| TRANSLATION_ATTEMPT | 0.79 |
| correct_linguistic_analysis | 0.76 |
| CORRECT_LINGUISTIC_ANALYSIS | 0.73 |

**Average COMET by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| none | 0.76 |
| null | 0.77 |

---

### MetricX-24 Metric

**Average MetricX-24 by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 1 | 8.88 |
| high | 7.92 |
| medium | 5.71 |
| neutral | 4.22 |

**Average MetricX-24 by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| correct_linguistic_analysis | 7.73 |
| CORRECT_LINGUISTIC_ANALYSIS | 7.70 |
| TRANSLATION_ATTEMPT | 6.56 |
| NONE | 5.45 |
| neutral | 3.18 |

**Average MetricX-24 by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| none | 9.19 |
| null | 8.88 |

---

### BLEU Metric

**Average BLEU by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 1 | 21.71 |
| high | 10.72 |
| medium | 19.64 |
| neutral | 25.79 |

**Average BLEU by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| neutral | 24.73 |
| NONE | 21.29 |
| TRANSLATION_ATTEMPT | 19.84 |
| CORRECT_LINGUISTIC_ANALYSIS | 11.28 |
| correct_linguistic_analysis | 6.37 |

**Average BLEU by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| none | 13.27 |
| null | 21.71 |

---

## 8. Key Insights

- **Best performing trace type**: neutral (BLEU: 24.73)
- **Worst performing trace type**: correct_linguistic_analysis (BLEU: 6.37)
- **Performance gap**: 288.0% improvement from worst to best

- **Most common trace type**: NONE (25 examples, 39.7%)
- **Average difficulty score**: 2.76/5.0

---

*Analysis generated from evaluations/guided_cot_eval/Turkish_English/gemma-3-1b-it/Turkish_to_English_0_shot_seed_42_identity_None_0_0_0/phase2_annotations.jsonl*
