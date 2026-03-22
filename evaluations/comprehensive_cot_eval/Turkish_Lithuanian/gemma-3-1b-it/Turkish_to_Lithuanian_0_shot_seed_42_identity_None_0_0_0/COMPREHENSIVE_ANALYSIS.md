# Phase 2 Comprehensive Analysis

**Total Examples Analyzed**: 64

---

## 1. Difficulty Distribution

Distribution of translation difficulty scores (1=easiest, 5=hardest):

| Difficulty Score | Count | Percentage |
|-----------------|-------|------------|
| 1 | 4 | 6.2% |
| 2 | 19 | 29.7% |
| 3 | 37 | 57.8% |
| 5 | 4 | 6.2% |

## 2. Linguistic Phenomena Frequencies

Frequency of linguistic phenomena across 64 examples:

| Phenomenon | Count | Percentage |
|------------|-------|------------|
| long_distance_dependency | 56 | 87.5% |
| named_entities | 46 | 71.9% |
| complex_syntax | 38 | 59.4% |
| ambiguity | 2 | 3.1% |
| idiom | 1 | 1.6% |
| figurative_language | 1 | 1.6% |

## 3. Primary Trace Type Distribution

Distribution of reasoning trace types (n=64):

| Trace Type | Count | Percentage |
|------------|-------|------------|
| NONE | 19 | 29.7% |
| CORRECT_LINGUISTIC_ANALYSIS | 19 | 29.7% |
| neutral | 14 | 21.9% |
| TRANSLATION_ATTEMPT | 10 | 15.6% |
| correct_linguistic_analysis | 2 | 3.1% |

## 4. Trace Usefulness Distribution

Distribution of trace usefulness ratings:

| Usefulness Level | Count | Percentage |
|------------------|-------|------------|
| 3 | 1 | 1.6% |
| High | 1 | 1.6% |
| helpful | 1 | 1.6% |
| high | 7 | 10.9% |
| medium | 25 | 39.1% |
| neutral | 29 | 45.3% |

## 5. Trace-Translation Overlap Distribution

Distribution of overlap between reasoning traces and translations:

| Overlap Level | Count | Percentage |
|---------------|-------|------------|
| 0 | 1 | 8.3% |
| none | 11 | 91.7% |

## 6. Cross-Tabulations

### 6.1 Difficulty × Trace Type

| Difficulty | CORRECT_LINGUISTIC_ANALYSIS | NONE | TRANSLATION_ATTEMPT | correct_linguistic_analysis | neutral |
|---|---|---|---|---|---|
| 1 | 0 | 3 | 0 | 0 | 1 |
| 2 | 2 | 7 | 0 | 1 | 9 |
| 3 | 13 | 9 | 10 | 1 | 4 |
| 5 | 4 | 0 | 0 | 0 | 0 |

### 6.2 Trace Type × Usefulness

| Trace Type | 3 | High | helpful | high | medium | neutral |
|---|---|---|---|---|---|---|
| CORRECT_LINGUISTIC_ANALYSIS | 0 | 1 | 0 | 6 | 9 | 3 |
| NONE | 1 | 0 | 1 | 0 | 2 | 15 |
| TRANSLATION_ATTEMPT | 0 | 0 | 0 | 0 | 9 | 1 |
| correct_linguistic_analysis | 0 | 0 | 0 | 1 | 1 | 0 |
| neutral | 0 | 0 | 0 | 0 | 4 | 10 |

## 7. Translation Quality Correlations

### MetricX-24 Metric

**Average MetricX-24 by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 3 | 17.88 |
| High | 15.38 |
| helpful | 12.75 |
| high | 15.94 |
| medium | 15.43 |
| neutral | 13.57 |

**Average MetricX-24 by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| CORRECT_LINGUISTIC_ANALYSIS | 15.89 |
| TRANSLATION_ATTEMPT | 14.74 |
| NONE | 14.16 |
| neutral | 13.73 |
| correct_linguistic_analysis | 13.06 |

**Average MetricX-24 by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| 0 | 17.88 |
| none | 16.50 |

---

### COMET Metric

**Average COMET by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 3 | 0.39 |
| High | 0.44 |
| helpful | 0.67 |
| high | 0.46 |
| medium | 0.56 |
| neutral | 0.59 |

**Average COMET by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| neutral | 0.62 |
| correct_linguistic_analysis | 0.61 |
| NONE | 0.58 |
| TRANSLATION_ATTEMPT | 0.58 |
| CORRECT_LINGUISTIC_ANALYSIS | 0.48 |

**Average COMET by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| 0 | 0.39 |
| none | 0.51 |

---

### chrF++ Metric

**Average chrF++ by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 3 | 26.64 |
| High | 13.06 |
| helpful | 9.50 |
| high | 14.54 |
| medium | 16.48 |
| neutral | 17.79 |

**Average chrF++ by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| neutral | 19.96 |
| NONE | 16.65 |
| TRANSLATION_ATTEMPT | 16.52 |
| CORRECT_LINGUISTIC_ANALYSIS | 15.33 |
| correct_linguistic_analysis | 13.36 |

**Average chrF++ by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| 0 | 26.64 |
| none | 17.41 |

---

### BLEU Metric

**Average BLEU by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 3 | 2.78 |
| High | 0.99 |
| helpful | 2.29 |
| high | 2.09 |
| medium | 2.95 |
| neutral | 5.13 |

**Average BLEU by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| neutral | 6.49 |
| NONE | 3.38 |
| CORRECT_LINGUISTIC_ANALYSIS | 3.25 |
| TRANSLATION_ATTEMPT | 2.34 |
| correct_linguistic_analysis | 1.50 |

**Average BLEU by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| 0 | 2.78 |
| none | 1.94 |

---

## 8. Key Insights

- **Best performing trace type**: neutral (BLEU: 6.49)
- **Worst performing trace type**: correct_linguistic_analysis (BLEU: 1.50)
- **Performance gap**: 333.5% improvement from worst to best

- **Most common trace type**: NONE (19 examples, 29.7%)
- **Average difficulty score**: 2.70/5.0

---

*Analysis generated from evaluations/comprehensive_cot_eval/Turkish_Lithuanian/gemma-3-1b-it/Turkish_to_Lithuanian_0_shot_seed_42_identity_None_0_0_0/phase2_annotations.jsonl*
