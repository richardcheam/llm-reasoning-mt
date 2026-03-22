# Phase 2 Comprehensive Analysis

**Total Examples Analyzed**: 64

---

## 1. Difficulty Distribution

Distribution of translation difficulty scores (1=easiest, 5=hardest):

| Difficulty Score | Count | Percentage |
|-----------------|-------|------------|
| 3 | 44 | 91.7% |
| 4 | 4 | 8.3% |

## 2. Linguistic Phenomena Frequencies

Frequency of linguistic phenomena across 48 examples:

| Phenomenon | Count | Percentage |
|------------|-------|------------|
| long_distance_dependency | 48 | 100.0% |
| complex_syntax | 39 | 81.2% |
| named_entities | 25 | 52.1% |
| ambiguity | 1 | 2.1% |
| idiom | 1 | 2.1% |
| figurative_language | 1 | 2.1% |

## 3. Primary Trace Type Distribution

Distribution of reasoning trace types (n=48):

| Trace Type | Count | Percentage |
|------------|-------|------------|
| TRANSLATION_ATTEMPT | 39 | 81.2% |
| NONE | 4 | 8.3% |
| CORRECT_LINGUISTIC_ANALYSIS | 3 | 6.2% |
| neutral | 2 | 4.2% |

## 4. Trace Usefulness Distribution

Distribution of trace usefulness ratings:

| Usefulness Level | Count | Percentage |
|------------------|-------|------------|
| 1 | 1 | 2.1% |
| Medium | 2 | 4.2% |
| high | 3 | 6.2% |
| medium | 41 | 85.4% |
| neutral | 1 | 2.1% |

## 5. Trace-Translation Overlap Distribution

Distribution of overlap between reasoning traces and translations:

| Overlap Level | Count | Percentage |
|---------------|-------|------------|
| 0 | 1 | 2.9% |
| low | 1 | 2.9% |
| none | 33 | 94.3% |

## 6. Cross-Tabulations

### 6.1 Difficulty × Trace Type

| Difficulty | CORRECT_LINGUISTIC_ANALYSIS | NONE | TRANSLATION_ATTEMPT | neutral |
|---|---|---|---|---|
| 3 | 3 | 4 | 35 | 2 |
| 4 | 0 | 0 | 4 | 0 |

### 6.2 Trace Type × Usefulness

| Trace Type | 1 | Medium | high | medium | neutral |
|---|---|---|---|---|---|
| CORRECT_LINGUISTIC_ANALYSIS | 0 | 0 | 0 | 3 | 0 |
| NONE | 1 | 0 | 0 | 2 | 1 |
| TRANSLATION_ATTEMPT | 0 | 2 | 3 | 34 | 0 |
| neutral | 0 | 0 | 0 | 2 | 0 |

## 7. Translation Quality Correlations

### MetricX-24 Metric

**Average MetricX-24 by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 1 | 15.88 |
| Medium | 15.12 |
| high | 17.19 |
| medium | 14.74 |
| neutral | 15.69 |

**Average MetricX-24 by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| NONE | 15.86 |
| TRANSLATION_ATTEMPT | 15.05 |
| neutral | 13.97 |
| CORRECT_LINGUISTIC_ANALYSIS | 13.12 |

**Average MetricX-24 by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| 0 | 15.88 |
| low | 16.88 |
| none | 14.65 |

---

### BLEU Metric

**Average BLEU by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 1 | 0.18 |
| Medium | 1.61 |
| high | 0.82 |
| medium | 2.34 |
| neutral | 1.81 |

**Average BLEU by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| neutral | 3.73 |
| TRANSLATION_ATTEMPT | 2.24 |
| NONE | 1.33 |
| CORRECT_LINGUISTIC_ANALYSIS | 1.12 |

**Average BLEU by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| 0 | 0.18 |
| low | 2.41 |
| none | 2.03 |

---

### chrF++ Metric

**Average chrF++ by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 1 | 0.70 |
| Medium | 4.48 |
| high | 4.65 |
| medium | 11.49 |
| neutral | 9.83 |

**Average chrF++ by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| CORRECT_LINGUISTIC_ANALYSIS | 11.60 |
| TRANSLATION_ATTEMPT | 10.84 |
| neutral | 8.85 |
| NONE | 7.33 |

**Average chrF++ by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| 0 | 0.70 |
| low | 1.83 |
| none | 11.44 |

---

### COMET Metric

**Average COMET by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 1 | 0.25 |
| Medium | 0.44 |
| high | 0.40 |
| medium | 0.41 |
| neutral | 0.40 |

**Average COMET by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| neutral | 0.49 |
| TRANSLATION_ATTEMPT | 0.41 |
| CORRECT_LINGUISTIC_ANALYSIS | 0.40 |
| NONE | 0.37 |

**Average COMET by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| 0 | 0.25 |
| low | 0.49 |
| none | 0.40 |

---

## 8. Key Insights

- **Best performing trace type**: neutral (BLEU: 3.73)
- **Worst performing trace type**: CORRECT_LINGUISTIC_ANALYSIS (BLEU: 1.12)
- **Performance gap**: 233.6% improvement from worst to best

- **Most common trace type**: TRANSLATION_ATTEMPT (39 examples, 81.2%)
- **Average difficulty score**: 3.08/5.0

---

*Analysis generated from evaluations/guided_cot_eval/Kazakh_Xhosa/gemma-3-1b-it/Kazakh_to_Xhosa_0_shot_seed_42_identity_None_0_0_0/phase2_annotations.jsonl*
