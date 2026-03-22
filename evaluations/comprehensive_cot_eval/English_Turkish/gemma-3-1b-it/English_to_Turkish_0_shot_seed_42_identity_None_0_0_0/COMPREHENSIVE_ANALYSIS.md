# Phase 2 Comprehensive Analysis

**Total Examples Analyzed**: 64

---

## 1. Difficulty Distribution

Distribution of translation difficulty scores (1=easiest, 5=hardest):

| Difficulty Score | Count | Percentage |
|-----------------|-------|------------|
| 1 | 2 | 3.1% |
| 2 | 23 | 35.9% |
| 3 | 31 | 48.4% |
| 4 | 4 | 6.2% |
| 5 | 4 | 6.2% |

## 2. Linguistic Phenomena Frequencies

Frequency of linguistic phenomena across 64 examples:

| Phenomenon | Count | Percentage |
|------------|-------|------------|
| long_distance_dependency | 57 | 89.1% |
| named_entities | 40 | 62.5% |
| complex_syntax | 39 | 60.9% |

## 3. Primary Trace Type Distribution

Distribution of reasoning trace types (n=64):

| Trace Type | Count | Percentage |
|------------|-------|------------|
| neutral | 24 | 37.5% |
| TRANSLATION_ATTEMPT | 23 | 35.9% |
| NONE | 13 | 20.3% |
| CORRECT_LINGUISTIC_ANALYSIS | 2 | 3.1% |
| REPETITION | 1 | 1.6% |
| correct_linguistic_analysis | 1 | 1.6% |

## 4. Trace Usefulness Distribution

Distribution of trace usefulness ratings:

| Usefulness Level | Count | Percentage |
|------------------|-------|------------|
| 4 | 1 | 1.6% |
| Easy | 1 | 1.6% |
| High | 1 | 1.6% |
| Medium | 3 | 4.7% |
| high | 3 | 4.7% |
| medium | 24 | 37.5% |
| neutral | 31 | 48.4% |

## 5. Trace-Translation Overlap Distribution

Distribution of overlap between reasoning traces and translations:

| Overlap Level | Count | Percentage |
|---------------|-------|------------|
| none | 8 | 100.0% |

## 6. Cross-Tabulations

### 6.1 Difficulty × Trace Type

| Difficulty | CORRECT_LINGUISTIC_ANALYSIS | NONE | REPETITION | TRANSLATION_ATTEMPT | correct_linguistic_analysis | neutral |
|---|---|---|---|---|---|---|
| 1 | 0 | 1 | 0 | 0 | 0 | 1 |
| 2 | 0 | 3 | 0 | 1 | 1 | 18 |
| 3 | 2 | 8 | 0 | 16 | 0 | 5 |
| 4 | 0 | 0 | 0 | 4 | 0 | 0 |
| 5 | 0 | 1 | 1 | 2 | 0 | 0 |

### 6.2 Trace Type × Usefulness

| Trace Type | 4 | Easy | High | Medium | high | medium | neutral |
|---|---|---|---|---|---|---|---|
| CORRECT_LINGUISTIC_ANALYSIS | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| NONE | 0 | 1 | 1 | 0 | 2 | 2 | 7 |
| REPETITION | 0 | 0 | 0 | 1 | 0 | 0 | 0 |
| TRANSLATION_ATTEMPT | 1 | 0 | 0 | 1 | 1 | 16 | 4 |
| correct_linguistic_analysis | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| neutral | 0 | 0 | 0 | 0 | 0 | 5 | 19 |

## 7. Translation Quality Correlations

### chrF++ Metric

**Average chrF++ by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 4 | 53.97 |
| Easy | 42.46 |
| High | 35.37 |
| Medium | 24.72 |
| high | 26.83 |
| medium | 32.29 |
| neutral | 36.62 |

**Average chrF++ by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| CORRECT_LINGUISTIC_ANALYSIS | 46.28 |
| REPETITION | 36.38 |
| correct_linguistic_analysis | 35.84 |
| neutral | 34.99 |
| NONE | 33.43 |
| TRANSLATION_ATTEMPT | 32.93 |

**Average chrF++ by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| none | 26.69 |

---

### MetricX-24 Metric

**Average MetricX-24 by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 4 | 1.18 |
| Easy | 5.41 |
| High | 1.64 |
| Medium | 12.77 |
| high | 7.17 |
| medium | 8.91 |
| neutral | 8.07 |

**Average MetricX-24 by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| REPETITION | 14.94 |
| correct_linguistic_analysis | 14.31 |
| CORRECT_LINGUISTIC_ANALYSIS | 10.12 |
| TRANSLATION_ATTEMPT | 9.01 |
| neutral | 7.98 |
| NONE | 6.43 |

**Average MetricX-24 by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| none | 10.01 |

---

### COMET Metric

**Average COMET by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 4 | 0.92 |
| Easy | 0.90 |
| High | 0.91 |
| Medium | 0.53 |
| high | 0.83 |
| medium | 0.71 |
| neutral | 0.73 |

**Average COMET by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| CORRECT_LINGUISTIC_ANALYSIS | 0.78 |
| NONE | 0.76 |
| neutral | 0.73 |
| TRANSLATION_ATTEMPT | 0.71 |
| correct_linguistic_analysis | 0.61 |
| REPETITION | 0.53 |

**Average COMET by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| none | 0.69 |

---

### BLEU Metric

**Average BLEU by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 4 | 28.45 |
| Easy | 13.56 |
| High | 9.54 |
| Medium | 5.80 |
| high | 6.13 |
| medium | 13.67 |
| neutral | 16.18 |

**Average BLEU by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| neutral | 17.73 |
| CORRECT_LINGUISTIC_ANALYSIS | 16.23 |
| TRANSLATION_ATTEMPT | 12.60 |
| correct_linguistic_analysis | 11.55 |
| NONE | 11.32 |
| REPETITION | 10.61 |

**Average BLEU by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| none | 7.66 |

---

## 8. Key Insights

- **Best performing trace type**: neutral (BLEU: 17.73)
- **Worst performing trace type**: REPETITION (BLEU: 10.61)
- **Performance gap**: 67.1% improvement from worst to best

- **Most common trace type**: neutral (24 examples, 37.5%)
- **Average difficulty score**: 2.77/5.0

---

*Analysis generated from evaluations/comprehensive_cot_eval/English_Turkish/gemma-3-1b-it/English_to_Turkish_0_shot_seed_42_identity_None_0_0_0/phase2_annotations.jsonl*
