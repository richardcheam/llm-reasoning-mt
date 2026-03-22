# Phase 2 Comprehensive Analysis

**Total Examples Analyzed**: 64

---

## 1. Difficulty Distribution

Distribution of translation difficulty scores (1=easiest, 5=hardest):

| Difficulty Score | Count | Percentage |
|-----------------|-------|------------|
| 2 | 1 | 1.7% |
| 3 | 48 | 80.0% |
| 4 | 11 | 18.3% |

## 2. Linguistic Phenomena Frequencies

Frequency of linguistic phenomena across 60 examples:

| Phenomenon | Count | Percentage |
|------------|-------|------------|
| long_distance_dependency | 59 | 98.3% |
| complex_syntax | 51 | 85.0% |
| named_entities | 40 | 66.7% |
| ambiguity | 6 | 10.0% |
| idiom | 6 | 10.0% |
| figurative_language | 6 | 10.0% |

## 3. Primary Trace Type Distribution

Distribution of reasoning trace types (n=60):

| Trace Type | Count | Percentage |
|------------|-------|------------|
| CORRECT_LINGUISTIC_ANALYSIS | 29 | 48.3% |
| TRANSLATION_ATTEMPT | 23 | 38.3% |
| correct_linguistic_analysis | 3 | 5.0% |
| neutral | 3 | 5.0% |
| NONE | 2 | 3.3% |

## 4. Trace Usefulness Distribution

Distribution of trace usefulness ratings:

| Usefulness Level | Count | Percentage |
|------------------|-------|------------|
| 2 | 2 | 3.3% |
| 3 | 2 | 3.3% |
| High | 1 | 1.7% |
| Medium | 4 | 6.7% |
| Medium (the translation is understandable but could be improved) | 1 | 1.7% |
| high | 7 | 11.7% |
| medium | 42 | 70.0% |
| neutral | 1 | 1.7% |

## 5. Trace-Translation Overlap Distribution

Distribution of overlap between reasoning traces and translations:

| Overlap Level | Count | Percentage |
|---------------|-------|------------|
| 0 | 3 | 7.0% |
| low | 4 | 9.3% |
| none | 36 | 83.7% |

## 6. Cross-Tabulations

### 6.1 Difficulty × Trace Type

| Difficulty | CORRECT_LINGUISTIC_ANALYSIS | NONE | TRANSLATION_ATTEMPT | correct_linguistic_analysis | neutral |
|---|---|---|---|---|---|
| 2 | 0 | 0 | 0 | 0 | 1 |
| 3 | 24 | 2 | 17 | 3 | 2 |
| 4 | 5 | 0 | 6 | 0 | 0 |

### 6.2 Trace Type × Usefulness

| Trace Type | 2 | 3 | High | Medium | Medium (the translation is understandable but could be improved) | high | medium | neutral |
|---|---|---|---|---|---|---|---|---|
| CORRECT_LINGUISTIC_ANALYSIS | 1 | 1 | 0 | 1 | 0 | 6 | 20 | 0 |
| NONE | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| TRANSLATION_ATTEMPT | 0 | 0 | 1 | 3 | 1 | 1 | 17 | 0 |
| correct_linguistic_analysis | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| neutral | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 1 |

## 7. Translation Quality Correlations

### COMET Metric

**Average COMET by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 2 | 0.54 |
| 3 | 0.38 |
| High | 0.39 |
| Medium | 0.42 |
| Medium (the translation is understandable but could be improved) | 0.43 |
| high | 0.48 |
| medium | 0.44 |
| neutral | 0.49 |

**Average COMET by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| NONE | 0.50 |
| neutral | 0.50 |
| correct_linguistic_analysis | 0.47 |
| CORRECT_LINGUISTIC_ANALYSIS | 0.46 |
| TRANSLATION_ATTEMPT | 0.41 |

**Average COMET by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| 0 | 0.50 |
| low | 0.40 |
| none | 0.43 |

---

### chrF++ Metric

**Average chrF++ by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 2 | 28.91 |
| 3 | 19.45 |
| High | 28.74 |
| Medium | 20.27 |
| Medium (the translation is understandable but could be improved) | 20.65 |
| high | 28.01 |
| medium | 24.25 |
| neutral | 26.17 |

**Average chrF++ by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| neutral | 34.41 |
| NONE | 27.58 |
| CORRECT_LINGUISTIC_ANALYSIS | 24.71 |
| TRANSLATION_ATTEMPT | 23.54 |
| correct_linguistic_analysis | 17.11 |

**Average chrF++ by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| 0 | 29.67 |
| low | 24.50 |
| none | 22.99 |

---

### MetricX-24 Metric

**Average MetricX-24 by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 2 | 12.03 |
| 3 | 16.25 |
| High | 17.75 |
| Medium | 17.02 |
| Medium (the translation is understandable but could be improved) | 16.88 |
| high | 15.41 |
| medium | 16.54 |
| neutral | 14.69 |

**Average MetricX-24 by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| correct_linguistic_analysis | 17.71 |
| TRANSLATION_ATTEMPT | 17.23 |
| neutral | 15.94 |
| CORRECT_LINGUISTIC_ANALYSIS | 15.66 |
| NONE | 12.50 |

**Average MetricX-24 by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| 0 | 13.35 |
| low | 17.31 |
| none | 16.86 |

---

### BLEU Metric

**Average BLEU by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 2 | 7.26 |
| 3 | 2.13 |
| High | 2.24 |
| Medium | 2.49 |
| Medium (the translation is understandable but could be improved) | 2.22 |
| high | 5.38 |
| medium | 5.64 |
| neutral | 3.14 |

**Average BLEU by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| neutral | 19.60 |
| NONE | 5.86 |
| TRANSLATION_ATTEMPT | 4.91 |
| CORRECT_LINGUISTIC_ANALYSIS | 4.29 |
| correct_linguistic_analysis | 1.08 |

**Average BLEU by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| 0 | 6.26 |
| low | 5.34 |
| none | 4.02 |

---

## 8. Key Insights

- **Best performing trace type**: neutral (BLEU: 19.60)
- **Worst performing trace type**: correct_linguistic_analysis (BLEU: 1.08)
- **Performance gap**: 1719.8% improvement from worst to best

- **Most common trace type**: CORRECT_LINGUISTIC_ANALYSIS (29 examples, 48.3%)
- **Average difficulty score**: 3.17/5.0

---

*Analysis generated from evaluations/guided_cot_eval/English_Lithuanian/gemma-3-1b-it/English_to_Lithuanian_0_shot_seed_42_identity_None_0_0_0/phase2_annotations.jsonl*
