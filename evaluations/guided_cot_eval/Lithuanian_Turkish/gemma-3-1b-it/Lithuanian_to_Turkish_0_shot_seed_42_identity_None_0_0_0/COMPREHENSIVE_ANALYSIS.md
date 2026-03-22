# Phase 2 Comprehensive Analysis

**Total Examples Analyzed**: 64

---

## 1. Difficulty Distribution

Distribution of translation difficulty scores (1=easiest, 5=hardest):

| Difficulty Score | Count | Percentage |
|-----------------|-------|------------|
| 2 | 2 | 3.2% |
| 3 | 55 | 88.7% |
| 4 | 5 | 8.1% |

## 2. Linguistic Phenomena Frequencies

Frequency of linguistic phenomena across 62 examples:

| Phenomenon | Count | Percentage |
|------------|-------|------------|
| long_distance_dependency | 60 | 96.8% |
| complex_syntax | 44 | 71.0% |
| named_entities | 40 | 64.5% |
| ambiguity | 2 | 3.2% |
| idiom | 2 | 3.2% |
| figurative_language | 2 | 3.2% |

## 3. Primary Trace Type Distribution

Distribution of reasoning trace types (n=62):

| Trace Type | Count | Percentage |
|------------|-------|------------|
| CORRECT_LINGUISTIC_ANALYSIS | 38 | 61.3% |
| NONE | 11 | 17.7% |
| TRANSLATION_ATTEMPT | 7 | 11.3% |
| neutral | 3 | 4.8% |
| correct_linguistic_analysis | 3 | 4.8% |

## 4. Trace Usefulness Distribution

Distribution of trace usefulness ratings:

| Usefulness Level | Count | Percentage |
|------------------|-------|------------|
| 1 | 2 | 3.2% |
| High | 2 | 3.2% |
| Medium | 1 | 1.6% |
| Neutral | 1 | 1.6% |
| high | 8 | 12.9% |
| medium | 42 | 67.7% |
| neutral | 6 | 9.7% |

## 5. Trace-Translation Overlap Distribution

Distribution of overlap between reasoning traces and translations:

| Overlap Level | Count | Percentage |
|---------------|-------|------------|
| 0 | 2 | 8.7% |
| none | 21 | 91.3% |

## 6. Cross-Tabulations

### 6.1 Difficulty × Trace Type

| Difficulty | CORRECT_LINGUISTIC_ANALYSIS | NONE | TRANSLATION_ATTEMPT | correct_linguistic_analysis | neutral |
|---|---|---|---|---|---|
| 2 | 0 | 1 | 0 | 0 | 1 |
| 3 | 35 | 10 | 5 | 3 | 2 |
| 4 | 3 | 0 | 2 | 0 | 0 |

### 6.2 Trace Type × Usefulness

| Trace Type | 1 | High | Medium | Neutral | high | medium | neutral |
|---|---|---|---|---|---|---|---|
| CORRECT_LINGUISTIC_ANALYSIS | 0 | 2 | 1 | 0 | 8 | 27 | 0 |
| NONE | 2 | 0 | 0 | 1 | 0 | 4 | 4 |
| TRANSLATION_ATTEMPT | 0 | 0 | 0 | 0 | 0 | 7 | 0 |
| correct_linguistic_analysis | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| neutral | 0 | 0 | 0 | 0 | 0 | 1 | 2 |

## 7. Translation Quality Correlations

### COMET Metric

**Average COMET by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 1 | 0.61 |
| High | 0.51 |
| Medium | 0.74 |
| Neutral | 0.75 |
| high | 0.57 |
| medium | 0.52 |
| neutral | 0.60 |

**Average COMET by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| neutral | 0.74 |
| NONE | 0.55 |
| CORRECT_LINGUISTIC_ANALYSIS | 0.55 |
| correct_linguistic_analysis | 0.52 |
| TRANSLATION_ATTEMPT | 0.46 |

**Average COMET by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| 0 | 0.61 |
| none | 0.50 |

---

### chrF++ Metric

**Average chrF++ by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 1 | 21.24 |
| High | 29.97 |
| Medium | 23.98 |
| Neutral | 26.67 |
| high | 18.80 |
| medium | 20.23 |
| neutral | 21.95 |

**Average chrF++ by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| neutral | 29.69 |
| correct_linguistic_analysis | 26.91 |
| CORRECT_LINGUISTIC_ANALYSIS | 20.85 |
| NONE | 19.57 |
| TRANSLATION_ATTEMPT | 15.37 |

**Average chrF++ by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| 0 | 21.24 |
| none | 20.89 |

---

### MetricX-24 Metric

**Average MetricX-24 by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 1 | 14.81 |
| High | 13.06 |
| Medium | 15.25 |
| Neutral | 11.06 |
| high | 14.04 |
| medium | 14.49 |
| neutral | 12.20 |

**Average MetricX-24 by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| TRANSLATION_ATTEMPT | 15.40 |
| NONE | 14.72 |
| correct_linguistic_analysis | 14.19 |
| CORRECT_LINGUISTIC_ANALYSIS | 14.09 |
| neutral | 9.52 |

**Average MetricX-24 by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| 0 | 14.81 |
| none | 14.86 |

---

### BLEU Metric

**Average BLEU by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 1 | 6.06 |
| High | 2.95 |
| Medium | 3.23 |
| Neutral | 5.82 |
| high | 2.79 |
| medium | 4.67 |
| neutral | 6.64 |

**Average BLEU by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| neutral | 11.51 |
| NONE | 5.48 |
| TRANSLATION_ATTEMPT | 4.74 |
| correct_linguistic_analysis | 4.22 |
| CORRECT_LINGUISTIC_ANALYSIS | 3.81 |

**Average BLEU by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| 0 | 6.06 |
| none | 4.35 |

---

## 8. Key Insights

- **Best performing trace type**: neutral (BLEU: 11.51)
- **Worst performing trace type**: CORRECT_LINGUISTIC_ANALYSIS (BLEU: 3.81)
- **Performance gap**: 202.2% improvement from worst to best

- **Most common trace type**: CORRECT_LINGUISTIC_ANALYSIS (38 examples, 61.3%)
- **Average difficulty score**: 3.05/5.0

---

*Analysis generated from evaluations/guided_cot_eval/Lithuanian_Turkish/gemma-3-1b-it/Lithuanian_to_Turkish_0_shot_seed_42_identity_None_0_0_0/phase2_annotations.jsonl*
