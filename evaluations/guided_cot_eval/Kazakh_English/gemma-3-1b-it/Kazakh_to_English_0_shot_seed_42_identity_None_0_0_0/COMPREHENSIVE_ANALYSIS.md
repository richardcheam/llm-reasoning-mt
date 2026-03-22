# Phase 2 Comprehensive Analysis

**Total Examples Analyzed**: 64

---

## 1. Difficulty Distribution

Distribution of translation difficulty scores (1=easiest, 5=hardest):

| Difficulty Score | Count | Percentage |
|-----------------|-------|------------|
| 2 | 7 | 11.1% |
| 3 | 43 | 68.3% |
| 4 | 13 | 20.6% |

## 2. Linguistic Phenomena Frequencies

Frequency of linguistic phenomena across 63 examples:

| Phenomenon | Count | Percentage |
|------------|-------|------------|
| long_distance_dependency | 60 | 95.2% |
| named_entities | 49 | 77.8% |
| complex_syntax | 45 | 71.4% |
| ambiguity | 1 | 1.6% |
| idiom | 1 | 1.6% |
| figurative_language | 1 | 1.6% |

## 3. Primary Trace Type Distribution

Distribution of reasoning trace types (n=63):

| Trace Type | Count | Percentage |
|------------|-------|------------|
| TRANSLATION_ATTEMPT | 33 | 52.4% |
| NONE | 17 | 27.0% |
| CORRECT_LINGUISTIC_ANALYSIS | 6 | 9.5% |
| neutral | 4 | 6.3% |
| REPETITION | 2 | 3.2% |
| correct_linguistic_analysis | 1 | 1.6% |

## 4. Trace Usefulness Distribution

Distribution of trace usefulness ratings:

| Usefulness Level | Count | Percentage |
|------------------|-------|------------|
| 3 | 1 | 1.6% |
| Easy | 1 | 1.6% |
| Medium | 2 | 3.2% |
| high | 12 | 19.0% |
| medium | 40 | 63.5% |
| neutral | 7 | 11.1% |

## 5. Trace-Translation Overlap Distribution

Distribution of overlap between reasoning traces and translations:

| Overlap Level | Count | Percentage |
|---------------|-------|------------|
| 0 | 1 | 4.3% |
| none | 22 | 95.7% |

## 6. Cross-Tabulations

### 6.1 Difficulty × Trace Type

| Difficulty | CORRECT_LINGUISTIC_ANALYSIS | NONE | REPETITION | TRANSLATION_ATTEMPT | correct_linguistic_analysis | neutral |
|---|---|---|---|---|---|---|
| 2 | 0 | 4 | 0 | 0 | 1 | 2 |
| 3 | 3 | 13 | 1 | 24 | 0 | 2 |
| 4 | 3 | 0 | 1 | 9 | 0 | 0 |

### 6.2 Trace Type × Usefulness

| Trace Type | 3 | Easy | Medium | high | medium | neutral |
|---|---|---|---|---|---|---|
| CORRECT_LINGUISTIC_ANALYSIS | 0 | 0 | 0 | 4 | 2 | 0 |
| NONE | 1 | 1 | 0 | 0 | 9 | 6 |
| REPETITION | 0 | 0 | 0 | 0 | 2 | 0 |
| TRANSLATION_ATTEMPT | 0 | 0 | 2 | 6 | 25 | 0 |
| correct_linguistic_analysis | 0 | 0 | 0 | 1 | 0 | 0 |
| neutral | 0 | 0 | 0 | 1 | 2 | 1 |

## 7. Translation Quality Correlations

### chrF++ Metric

**Average chrF++ by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 3 | 25.72 |
| Easy | 34.61 |
| Medium | 19.18 |
| high | 23.83 |
| medium | 30.26 |
| neutral | 34.64 |

**Average chrF++ by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| NONE | 34.06 |
| REPETITION | 32.56 |
| TRANSLATION_ATTEMPT | 29.06 |
| correct_linguistic_analysis | 26.70 |
| neutral | 22.51 |
| CORRECT_LINGUISTIC_ANALYSIS | 19.64 |

**Average chrF++ by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| 0 | 25.72 |
| none | 25.27 |

---

### COMET Metric

**Average COMET by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 3 | 0.65 |
| Easy | 0.79 |
| Medium | 0.56 |
| high | 0.68 |
| medium | 0.71 |
| neutral | 0.72 |

**Average COMET by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| correct_linguistic_analysis | 0.77 |
| NONE | 0.73 |
| REPETITION | 0.72 |
| TRANSLATION_ATTEMPT | 0.70 |
| neutral | 0.68 |
| CORRECT_LINGUISTIC_ANALYSIS | 0.64 |

**Average COMET by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| 0 | 0.65 |
| none | 0.67 |

---

### MetricX-24 Metric

**Average MetricX-24 by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 3 | 13.38 |
| Easy | 14.94 |
| Medium | 15.81 |
| high | 12.77 |
| medium | 10.79 |
| neutral | 10.65 |

**Average MetricX-24 by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| correct_linguistic_analysis | 13.56 |
| CORRECT_LINGUISTIC_ANALYSIS | 13.41 |
| neutral | 13.23 |
| TRANSLATION_ATTEMPT | 11.30 |
| NONE | 10.51 |
| REPETITION | 10.34 |

**Average MetricX-24 by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| 0 | 13.38 |
| none | 12.21 |

---

### BLEU Metric

**Average BLEU by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 3 | 1.09 |
| Easy | 8.59 |
| Medium | 3.09 |
| high | 4.96 |
| medium | 9.39 |
| neutral | 12.16 |

**Average BLEU by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| REPETITION | 11.32 |
| NONE | 9.84 |
| TRANSLATION_ATTEMPT | 9.20 |
| neutral | 5.89 |
| CORRECT_LINGUISTIC_ANALYSIS | 2.87 |
| correct_linguistic_analysis | 1.73 |

**Average BLEU by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| 0 | 1.09 |
| none | 7.04 |

---

## 8. Key Insights

- **Best performing trace type**: REPETITION (BLEU: 11.32)
- **Worst performing trace type**: correct_linguistic_analysis (BLEU: 1.73)
- **Performance gap**: 553.9% improvement from worst to best

- **Most common trace type**: TRANSLATION_ATTEMPT (33 examples, 52.4%)
- **Average difficulty score**: 3.10/5.0

---

*Analysis generated from evaluations/guided_cot_eval/Kazakh_English/gemma-3-1b-it/Kazakh_to_English_0_shot_seed_42_identity_None_0_0_0/phase2_annotations.jsonl*
