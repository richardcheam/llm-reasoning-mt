# Phase 2 Comprehensive Analysis

**Total Examples Analyzed**: 64

---

## 1. Difficulty Distribution

Distribution of translation difficulty scores (1=easiest, 5=hardest):

| Difficulty Score | Count | Percentage |
|-----------------|-------|------------|
| 2 | 5 | 8.1% |
| 3 | 52 | 83.9% |
| 4 | 4 | 6.5% |
| 5 | 1 | 1.6% |

## 2. Linguistic Phenomena Frequencies

Frequency of linguistic phenomena across 62 examples:

| Phenomenon | Count | Percentage |
|------------|-------|------------|
| long_distance_dependency | 60 | 96.8% |
| complex_syntax | 48 | 77.4% |
| named_entities | 44 | 71.0% |
| ambiguity | 5 | 8.1% |
| idiom | 5 | 8.1% |
| figurative_language | 5 | 8.1% |

## 3. Primary Trace Type Distribution

Distribution of reasoning trace types (n=62):

| Trace Type | Count | Percentage |
|------------|-------|------------|
| TRANSLATION_ATTEMPT | 35 | 56.5% |
| NONE | 13 | 21.0% |
| CORRECT_LINGUISTIC_ANALYSIS | 12 | 19.4% |
| neutral | 2 | 3.2% |

## 4. Trace Usefulness Distribution

Distribution of trace usefulness ratings:

| Usefulness Level | Count | Percentage |
|------------------|-------|------------|
| 1 | 2 | 3.2% |
| 2 | 2 | 3.2% |
| 3 | 1 | 1.6% |
| Medium | 1 | 1.6% |
| high | 3 | 4.8% |
| medium | 46 | 74.2% |
| neutral | 7 | 11.3% |

## 5. Trace-Translation Overlap Distribution

Distribution of overlap between reasoning traces and translations:

| Overlap Level | Count | Percentage |
|---------------|-------|------------|
| 0 | 4 | 33.3% |
| none | 8 | 66.7% |

## 6. Cross-Tabulations

### 6.1 Difficulty × Trace Type

| Difficulty | CORRECT_LINGUISTIC_ANALYSIS | NONE | TRANSLATION_ATTEMPT | neutral |
|---|---|---|---|---|
| 2 | 0 | 3 | 2 | 0 |
| 3 | 11 | 10 | 29 | 2 |
| 4 | 0 | 0 | 4 | 0 |
| 5 | 1 | 0 | 0 | 0 |

### 6.2 Trace Type × Usefulness

| Trace Type | 1 | 2 | 3 | Medium | high | medium | neutral |
|---|---|---|---|---|---|---|---|
| CORRECT_LINGUISTIC_ANALYSIS | 0 | 1 | 0 | 0 | 1 | 10 | 0 |
| NONE | 2 | 1 | 1 | 0 | 0 | 3 | 6 |
| TRANSLATION_ATTEMPT | 0 | 0 | 0 | 1 | 2 | 31 | 1 |
| neutral | 0 | 0 | 0 | 0 | 0 | 2 | 0 |

## 7. Translation Quality Correlations

### chrF++ Metric

**Average chrF++ by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 1 | 30.43 |
| 2 | 20.38 |
| 3 | 40.74 |
| Medium | 24.06 |
| high | 16.26 |
| medium | 24.83 |
| neutral | 37.01 |

**Average chrF++ by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| neutral | 34.06 |
| NONE | 33.17 |
| TRANSLATION_ATTEMPT | 24.37 |
| CORRECT_LINGUISTIC_ANALYSIS | 22.04 |

**Average chrF++ by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| 0 | 32.58 |
| none | 24.38 |

---

### COMET Metric

**Average COMET by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 1 | 0.56 |
| 2 | 0.48 |
| 3 | 0.71 |
| Medium | 0.46 |
| high | 0.61 |
| medium | 0.61 |
| neutral | 0.71 |

**Average COMET by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| neutral | 0.76 |
| NONE | 0.68 |
| TRANSLATION_ATTEMPT | 0.60 |
| CORRECT_LINGUISTIC_ANALYSIS | 0.55 |

**Average COMET by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| 0 | 0.60 |
| none | 0.56 |

---

### MetricX-24 Metric

**Average MetricX-24 by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 1 | 13.75 |
| 2 | 13.59 |
| 3 | 8.06 |
| Medium | 16.38 |
| high | 14.02 |
| medium | 12.90 |
| neutral | 10.38 |

**Average MetricX-24 by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| CORRECT_LINGUISTIC_ANALYSIS | 13.81 |
| TRANSLATION_ATTEMPT | 13.44 |
| NONE | 10.40 |
| neutral | 7.90 |

**Average MetricX-24 by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| 0 | 11.89 |
| none | 13.90 |

---

### BLEU Metric

**Average BLEU by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 1 | 8.77 |
| 2 | 1.32 |
| 3 | 19.56 |
| Medium | 2.68 |
| high | 3.32 |
| medium | 6.40 |
| neutral | 21.55 |

**Average BLEU by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| neutral | 16.90 |
| NONE | 15.82 |
| TRANSLATION_ATTEMPT | 5.81 |
| CORRECT_LINGUISTIC_ANALYSIS | 4.57 |

**Average BLEU by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| 0 | 9.80 |
| none | 5.08 |

---

## 8. Key Insights

- **Best performing trace type**: neutral (BLEU: 16.90)
- **Worst performing trace type**: CORRECT_LINGUISTIC_ANALYSIS (BLEU: 4.57)
- **Performance gap**: 270.0% improvement from worst to best

- **Most common trace type**: TRANSLATION_ATTEMPT (35 examples, 56.5%)
- **Average difficulty score**: 3.02/5.0

---

*Analysis generated from evaluations/guided_cot_eval/Finnish_Turkish/gemma-3-1b-it/Finnish_to_Turkish_0_shot_seed_42_identity_None_0_0_0/phase2_annotations.jsonl*
