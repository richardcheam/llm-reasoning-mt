# Phase 2 Comprehensive Analysis

**Total Examples Analyzed**: 64

---

## 1. Difficulty Distribution

Distribution of translation difficulty scores (1=easiest, 5=hardest):

| Difficulty Score | Count | Percentage |
|-----------------|-------|------------|
| 3 | 38 | 74.5% |
| 4 | 12 | 23.5% |
| 5 | 1 | 2.0% |

## 2. Linguistic Phenomena Frequencies

Frequency of linguistic phenomena across 51 examples:

| Phenomenon | Count | Percentage |
|------------|-------|------------|
| long_distance_dependency | 51 | 100.0% |
| complex_syntax | 41 | 80.4% |
| named_entities | 29 | 56.9% |
| ambiguity | 1 | 2.0% |
| idiom | 1 | 2.0% |
| figurative_language | 1 | 2.0% |

## 3. Primary Trace Type Distribution

Distribution of reasoning trace types (n=51):

| Trace Type | Count | Percentage |
|------------|-------|------------|
| TRANSLATION_ATTEMPT | 30 | 58.8% |
| CORRECT_LINGUISTIC_ANALYSIS | 12 | 23.5% |
| NONE | 5 | 9.8% |
| REVISION_OF_TRANSLATION | 1 | 2.0% |
| neutral | 1 | 2.0% |
| REPETITION | 1 | 2.0% |
| correct_linguistic_analysis | 1 | 2.0% |

## 4. Trace Usefulness Distribution

Distribution of trace usefulness ratings:

| Usefulness Level | Count | Percentage |
|------------------|-------|------------|
| 2 | 1 | 2.0% |
| High | 2 | 3.9% |
| Medium | 6 | 11.8% |
| high | 4 | 7.8% |
| medium | 36 | 70.6% |
| neutral | 2 | 3.9% |

## 5. Trace-Translation Overlap Distribution

Distribution of overlap between reasoning traces and translations:

| Overlap Level | Count | Percentage |
|---------------|-------|------------|
| 0 | 1 | 2.9% |
| low | 2 | 5.7% |
| none | 32 | 91.4% |

## 6. Cross-Tabulations

### 6.1 Difficulty × Trace Type

| Difficulty | CORRECT_LINGUISTIC_ANALYSIS | NONE | REPETITION | REVISION_OF_TRANSLATION | TRANSLATION_ATTEMPT | correct_linguistic_analysis | neutral |
|---|---|---|---|---|---|---|---|
| 3 | 9 | 5 | 1 | 0 | 21 | 1 | 1 |
| 4 | 2 | 0 | 0 | 1 | 9 | 0 | 0 |
| 5 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |

### 6.2 Trace Type × Usefulness

| Trace Type | 2 | High | Medium | high | medium | neutral |
|---|---|---|---|---|---|---|
| CORRECT_LINGUISTIC_ANALYSIS | 0 | 1 | 1 | 3 | 7 | 0 |
| NONE | 1 | 0 | 0 | 0 | 2 | 2 |
| REPETITION | 0 | 0 | 0 | 0 | 1 | 0 |
| REVISION_OF_TRANSLATION | 0 | 0 | 1 | 0 | 0 | 0 |
| TRANSLATION_ATTEMPT | 0 | 1 | 4 | 1 | 24 | 0 |
| correct_linguistic_analysis | 0 | 0 | 0 | 0 | 1 | 0 |
| neutral | 0 | 0 | 0 | 0 | 1 | 0 |

## 7. Translation Quality Correlations

### chrF++ Metric

**Average chrF++ by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 2 | 8.55 |
| High | 12.01 |
| Medium | 11.24 |
| high | 12.50 |
| medium | 14.09 |
| neutral | 12.95 |

**Average chrF++ by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| NONE | 16.15 |
| correct_linguistic_analysis | 15.84 |
| REVISION_OF_TRANSLATION | 14.85 |
| CORRECT_LINGUISTIC_ANALYSIS | 14.02 |
| TRANSLATION_ATTEMPT | 12.80 |
| REPETITION | 10.25 |
| neutral | 9.43 |

**Average chrF++ by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| 0 | 8.55 |
| low | 11.68 |
| none | 13.18 |

---

### COMET Metric

**Average COMET by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 2 | 0.26 |
| High | 0.38 |
| Medium | 0.39 |
| high | 0.32 |
| medium | 0.38 |
| neutral | 0.44 |

**Average COMET by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| NONE | 0.43 |
| REPETITION | 0.42 |
| correct_linguistic_analysis | 0.41 |
| CORRECT_LINGUISTIC_ANALYSIS | 0.40 |
| neutral | 0.39 |
| REVISION_OF_TRANSLATION | 0.38 |
| TRANSLATION_ATTEMPT | 0.36 |

**Average COMET by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| 0 | 0.26 |
| low | 0.35 |
| none | 0.37 |

---

### BLEU Metric

**Average BLEU by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 2 | 1.58 |
| High | 1.07 |
| Medium | 2.21 |
| high | 1.16 |
| medium | 3.48 |
| neutral | 3.59 |

**Average BLEU by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| NONE | 7.40 |
| correct_linguistic_analysis | 2.83 |
| TRANSLATION_ATTEMPT | 2.71 |
| CORRECT_LINGUISTIC_ANALYSIS | 2.40 |
| neutral | 1.65 |
| REVISION_OF_TRANSLATION | 1.49 |
| REPETITION | 1.20 |

**Average BLEU by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| 0 | 1.58 |
| low | 1.48 |
| none | 2.44 |

---

### MetricX-24 Metric

**Average MetricX-24 by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 2 | 18.25 |
| High | 15.75 |
| Medium | 15.26 |
| high | 14.98 |
| medium | 15.01 |
| neutral | 15.38 |

**Average MetricX-24 by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| REVISION_OF_TRANSLATION | 16.50 |
| NONE | 15.51 |
| TRANSLATION_ATTEMPT | 15.25 |
| CORRECT_LINGUISTIC_ANALYSIS | 14.97 |
| neutral | 14.88 |
| REPETITION | 13.50 |
| correct_linguistic_analysis | 12.69 |

**Average MetricX-24 by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| 0 | 18.25 |
| low | 16.16 |
| none | 14.80 |

---

## 8. Key Insights

- **Best performing trace type**: NONE (BLEU: 7.40)
- **Worst performing trace type**: REPETITION (BLEU: 1.20)
- **Performance gap**: 516.8% improvement from worst to best

- **Most common trace type**: TRANSLATION_ATTEMPT (30 examples, 58.8%)
- **Average difficulty score**: 3.27/5.0

---

*Analysis generated from evaluations/guided_cot_eval/Lithuanian_Xhosa/gemma-3-1b-it/Lithuanian_to_Xhosa_0_shot_seed_42_identity_None_0_0_0/phase2_annotations.jsonl*
