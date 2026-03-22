# Phase 2 Comprehensive Analysis

**Total Examples Analyzed**: 64

---

## 1. Difficulty Distribution

Distribution of translation difficulty scores (1=easiest, 5=hardest):

| Difficulty Score | Count | Percentage |
|-----------------|-------|------------|
| 2 | 5 | 8.2% |
| 3 | 50 | 82.0% |
| 4 | 6 | 9.8% |

## 2. Linguistic Phenomena Frequencies

Frequency of linguistic phenomena across 61 examples:

| Phenomenon | Count | Percentage |
|------------|-------|------------|
| long_distance_dependency | 59 | 96.7% |
| complex_syntax | 53 | 86.9% |
| named_entities | 41 | 67.2% |
| ambiguity | 7 | 11.5% |
| idiom | 7 | 11.5% |
| figurative_language | 7 | 11.5% |

## 3. Primary Trace Type Distribution

Distribution of reasoning trace types (n=61):

| Trace Type | Count | Percentage |
|------------|-------|------------|
| CORRECT_LINGUISTIC_ANALYSIS | 19 | 31.1% |
| TRANSLATION_ATTEMPT | 16 | 26.2% |
| neutral | 11 | 18.0% |
| NONE | 8 | 13.1% |
| correct_linguistic_analysis | 6 | 9.8% |
| REPETITION | 1 | 1.6% |

## 4. Trace Usefulness Distribution

Distribution of trace usefulness ratings:

| Usefulness Level | Count | Percentage |
|------------------|-------|------------|
| 2 | 5 | 8.2% |
| 3 | 1 | 1.6% |
| Medium | 2 | 3.3% |
| Neutral | 2 | 3.3% |
| high | 9 | 14.8% |
| medium | 37 | 60.7% |
| neutral | 5 | 8.2% |

## 5. Trace-Translation Overlap Distribution

Distribution of overlap between reasoning traces and translations:

| Overlap Level | Count | Percentage |
|---------------|-------|------------|
| 0 | 5 | 27.8% |
| low | 1 | 5.6% |
| none | 12 | 66.7% |

## 6. Cross-Tabulations

### 6.1 Difficulty × Trace Type

| Difficulty | CORRECT_LINGUISTIC_ANALYSIS | NONE | REPETITION | TRANSLATION_ATTEMPT | correct_linguistic_analysis | neutral |
|---|---|---|---|---|---|---|
| 2 | 0 | 2 | 0 | 0 | 0 | 3 |
| 3 | 17 | 6 | 1 | 13 | 5 | 8 |
| 4 | 2 | 0 | 0 | 3 | 1 | 0 |

### 6.2 Trace Type × Usefulness

| Trace Type | 2 | 3 | Medium | Neutral | high | medium | neutral |
|---|---|---|---|---|---|---|---|
| CORRECT_LINGUISTIC_ANALYSIS | 0 | 0 | 0 | 0 | 7 | 12 | 0 |
| NONE | 3 | 1 | 0 | 2 | 0 | 1 | 1 |
| REPETITION | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| TRANSLATION_ATTEMPT | 0 | 0 | 2 | 0 | 1 | 13 | 0 |
| correct_linguistic_analysis | 1 | 0 | 0 | 0 | 1 | 4 | 0 |
| neutral | 1 | 0 | 0 | 0 | 0 | 7 | 3 |

## 7. Translation Quality Correlations

### chrF++ Metric

**Average chrF++ by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 2 | 31.41 |
| 3 | 23.61 |
| Medium | 15.45 |
| Neutral | 38.54 |
| high | 20.48 |
| medium | 23.37 |
| neutral | 27.90 |

**Average chrF++ by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| NONE | 33.00 |
| correct_linguistic_analysis | 28.65 |
| CORRECT_LINGUISTIC_ANALYSIS | 24.49 |
| neutral | 21.51 |
| REPETITION | 20.52 |
| TRANSLATION_ATTEMPT | 19.92 |

**Average chrF++ by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| 0 | 28.96 |
| low | 13.75 |
| none | 23.40 |

---

### BLEU Metric

**Average BLEU by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 2 | 12.22 |
| 3 | 7.31 |
| Medium | 1.25 |
| Neutral | 16.89 |
| high | 4.76 |
| medium | 5.42 |
| neutral | 7.92 |

**Average BLEU by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| NONE | 13.54 |
| correct_linguistic_analysis | 5.85 |
| TRANSLATION_ATTEMPT | 5.57 |
| CORRECT_LINGUISTIC_ANALYSIS | 5.50 |
| neutral | 4.44 |
| REPETITION | 1.76 |

**Average BLEU by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| 0 | 11.26 |
| low | 1.17 |
| none | 5.59 |

---

### MetricX-24 Metric

**Average MetricX-24 by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 2 | 10.46 |
| 3 | 15.56 |
| Medium | 17.88 |
| Neutral | 12.91 |
| high | 13.11 |
| medium | 12.83 |
| neutral | 9.65 |

**Average MetricX-24 by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| correct_linguistic_analysis | 14.43 |
| TRANSLATION_ATTEMPT | 14.09 |
| neutral | 12.39 |
| CORRECT_LINGUISTIC_ANALYSIS | 12.26 |
| NONE | 10.08 |
| REPETITION | 8.19 |

**Average MetricX-24 by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| 0 | 10.98 |
| low | 16.25 |
| none | 12.80 |

---

### COMET Metric

**Average COMET by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 2 | 0.67 |
| 3 | 0.55 |
| Medium | 0.38 |
| Neutral | 0.67 |
| high | 0.60 |
| medium | 0.63 |
| neutral | 0.68 |

**Average COMET by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| REPETITION | 0.74 |
| NONE | 0.72 |
| neutral | 0.65 |
| CORRECT_LINGUISTIC_ANALYSIS | 0.61 |
| correct_linguistic_analysis | 0.61 |
| TRANSLATION_ATTEMPT | 0.58 |

**Average COMET by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| 0 | 0.67 |
| low | 0.63 |
| none | 0.58 |

---

## 8. Key Insights

- **Best performing trace type**: NONE (BLEU: 13.54)
- **Worst performing trace type**: REPETITION (BLEU: 1.76)
- **Performance gap**: 670.3% improvement from worst to best

- **Most common trace type**: CORRECT_LINGUISTIC_ANALYSIS (19 examples, 31.1%)
- **Average difficulty score**: 3.02/5.0

---

*Analysis generated from evaluations/guided_cot_eval/Turkish_Finnish/gemma-3-1b-it/Turkish_to_Finnish_0_shot_seed_42_identity_None_0_0_0/phase2_annotations.jsonl*
