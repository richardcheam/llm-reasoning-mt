# Phase 2 Comprehensive Analysis

**Total Examples Analyzed**: 64

---

## 1. Difficulty Distribution

Distribution of translation difficulty scores (1=easiest, 5=hardest):

| Difficulty Score | Count | Percentage |
|-----------------|-------|------------|
| 3 | 45 | 90.0% |
| 4 | 4 | 8.0% |
| 5 | 1 | 2.0% |

## 2. Linguistic Phenomena Frequencies

Frequency of linguistic phenomena across 50 examples:

| Phenomenon | Count | Percentage |
|------------|-------|------------|
| long_distance_dependency | 50 | 100.0% |
| complex_syntax | 46 | 92.0% |
| named_entities | 31 | 62.0% |
| ambiguity | 2 | 4.0% |
| idiom | 2 | 4.0% |
| figurative_language | 2 | 4.0% |

## 3. Primary Trace Type Distribution

Distribution of reasoning trace types (n=50):

| Trace Type | Count | Percentage |
|------------|-------|------------|
| TRANSLATION_ATTEMPT | 42 | 84.0% |
| NONE | 4 | 8.0% |
| CORRECT_LINGUISTIC_ANALYSIS | 3 | 6.0% |
| correct_linguistic_analysis | 1 | 2.0% |

## 4. Trace Usefulness Distribution

Distribution of trace usefulness ratings:

| Usefulness Level | Count | Percentage |
|------------------|-------|------------|
| 3 | 1 | 2.0% |
| Medium | 6 | 12.0% |
| high | 1 | 2.0% |
| medium | 40 | 80.0% |
| neutral | 2 | 4.0% |

## 5. Trace-Translation Overlap Distribution

Distribution of overlap between reasoning traces and translations:

| Overlap Level | Count | Percentage |
|---------------|-------|------------|
| 0 | 1 | 2.6% |
| none | 37 | 97.4% |

## 6. Cross-Tabulations

### 6.1 Difficulty × Trace Type

| Difficulty | CORRECT_LINGUISTIC_ANALYSIS | NONE | TRANSLATION_ATTEMPT | correct_linguistic_analysis |
|---|---|---|---|---|
| 3 | 2 | 4 | 38 | 1 |
| 4 | 0 | 0 | 4 | 0 |
| 5 | 1 | 0 | 0 | 0 |

### 6.2 Trace Type × Usefulness

| Trace Type | 3 | Medium | high | medium | neutral |
|---|---|---|---|---|---|
| CORRECT_LINGUISTIC_ANALYSIS | 0 | 2 | 1 | 0 | 0 |
| NONE | 1 | 0 | 0 | 1 | 2 |
| TRANSLATION_ATTEMPT | 0 | 4 | 0 | 38 | 0 |
| correct_linguistic_analysis | 0 | 0 | 0 | 1 | 0 |

## 7. Translation Quality Correlations

### chrF++ Metric

**Average chrF++ by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 3 | 9.67 |
| Medium | 5.96 |
| high | 12.87 |
| medium | 9.66 |
| neutral | 8.13 |

**Average chrF++ by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| TRANSLATION_ATTEMPT | 9.45 |
| NONE | 8.22 |
| correct_linguistic_analysis | 8.15 |
| CORRECT_LINGUISTIC_ANALYSIS | 7.64 |

**Average chrF++ by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| 0 | 9.67 |
| none | 9.00 |

---

### MetricX-24 Metric

**Average MetricX-24 by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 3 | 16.62 |
| Medium | 16.36 |
| high | 18.88 |
| medium | 16.67 |
| neutral | 15.69 |

**Average MetricX-24 by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| TRANSLATION_ATTEMPT | 16.83 |
| CORRECT_LINGUISTIC_ANALYSIS | 16.10 |
| correct_linguistic_analysis | 15.94 |
| NONE | 15.20 |

**Average MetricX-24 by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| 0 | 16.62 |
| none | 16.64 |

---

### COMET Metric

**Average COMET by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 3 | 0.46 |
| Medium | 0.32 |
| high | 0.43 |
| medium | 0.37 |
| neutral | 0.48 |

**Average COMET by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| NONE | 0.43 |
| correct_linguistic_analysis | 0.41 |
| CORRECT_LINGUISTIC_ANALYSIS | 0.38 |
| TRANSLATION_ATTEMPT | 0.36 |

**Average COMET by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| 0 | 0.46 |
| none | 0.36 |

---

### BLEU Metric

**Average BLEU by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 3 | 1.36 |
| Medium | 1.35 |
| high | 6.05 |
| medium | 2.76 |
| neutral | 2.60 |

**Average BLEU by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| NONE | 3.01 |
| CORRECT_LINGUISTIC_ANALYSIS | 2.67 |
| TRANSLATION_ATTEMPT | 2.61 |
| correct_linguistic_analysis | 1.59 |

**Average BLEU by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| 0 | 1.36 |
| none | 2.53 |

---

## 8. Key Insights

- **Best performing trace type**: NONE (BLEU: 3.01)
- **Worst performing trace type**: correct_linguistic_analysis (BLEU: 1.59)
- **Performance gap**: 89.1% improvement from worst to best

- **Most common trace type**: TRANSLATION_ATTEMPT (42 examples, 84.0%)
- **Average difficulty score**: 3.12/5.0

---

*Analysis generated from evaluations/guided_cot_eval/Xhosa_Kazakh/gemma-3-1b-it/Xhosa_to_Kazakh_0_shot_seed_42_identity_None_0_0_0/phase2_annotations.jsonl*
