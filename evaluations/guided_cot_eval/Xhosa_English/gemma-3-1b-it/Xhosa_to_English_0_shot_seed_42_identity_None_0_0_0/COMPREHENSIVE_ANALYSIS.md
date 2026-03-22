# Phase 2 Comprehensive Analysis

**Total Examples Analyzed**: 64

---

## 1. Difficulty Distribution

Distribution of translation difficulty scores (1=easiest, 5=hardest):

| Difficulty Score | Count | Percentage |
|-----------------|-------|------------|
| 2 | 2 | 3.1% |
| 3 | 47 | 73.4% |
| 4 | 13 | 20.3% |
| 5 | 2 | 3.1% |

## 2. Linguistic Phenomena Frequencies

Frequency of linguistic phenomena across 64 examples:

| Phenomenon | Count | Percentage |
|------------|-------|------------|
| long_distance_dependency | 64 | 100.0% |
| complex_syntax | 54 | 84.4% |
| named_entities | 50 | 78.1% |
| ambiguity | 2 | 3.1% |
| idiom | 2 | 3.1% |
| figurative_language | 2 | 3.1% |

## 3. Primary Trace Type Distribution

Distribution of reasoning trace types (n=64):

| Trace Type | Count | Percentage |
|------------|-------|------------|
| TRANSLATION_ATTEMPT | 52 | 81.2% |
| NONE | 5 | 7.8% |
| CORRECT_LINGUISTIC_ANALYSIS | 4 | 6.2% |
| neutral | 3 | 4.7% |

## 4. Trace Usefulness Distribution

Distribution of trace usefulness ratings:

| Usefulness Level | Count | Percentage |
|------------------|-------|------------|
| 1 | 1 | 1.6% |
| 2 | 1 | 1.6% |
| High | 1 | 1.6% |
| Medium | 9 | 14.1% |
| high | 3 | 4.7% |
| medium | 47 | 73.4% |
| neutral | 2 | 3.1% |

## 5. Trace-Translation Overlap Distribution

Distribution of overlap between reasoning traces and translations:

| Overlap Level | Count | Percentage |
|---------------|-------|------------|
| 0 | 2 | 4.9% |
| low | 1 | 2.4% |
| none | 38 | 92.7% |

## 6. Cross-Tabulations

### 6.1 Difficulty × Trace Type

| Difficulty | CORRECT_LINGUISTIC_ANALYSIS | NONE | TRANSLATION_ATTEMPT | neutral |
|---|---|---|---|---|
| 2 | 0 | 0 | 0 | 2 |
| 3 | 3 | 5 | 38 | 1 |
| 4 | 0 | 0 | 13 | 0 |
| 5 | 1 | 0 | 1 | 0 |

### 6.2 Trace Type × Usefulness

| Trace Type | 1 | 2 | High | Medium | high | medium | neutral |
|---|---|---|---|---|---|---|---|
| CORRECT_LINGUISTIC_ANALYSIS | 0 | 0 | 1 | 0 | 1 | 2 | 0 |
| NONE | 1 | 1 | 0 | 0 | 0 | 2 | 1 |
| TRANSLATION_ATTEMPT | 0 | 0 | 0 | 9 | 2 | 41 | 0 |
| neutral | 0 | 0 | 0 | 0 | 0 | 2 | 1 |

## 7. Translation Quality Correlations

### BLEU Metric

**Average BLEU by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 1 | 0.98 |
| 2 | 3.53 |
| High | 0.82 |
| Medium | 9.05 |
| high | 11.60 |
| medium | 5.09 |
| neutral | 4.29 |

**Average BLEU by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| CORRECT_LINGUISTIC_ANALYSIS | 11.23 |
| TRANSLATION_ATTEMPT | 5.58 |
| NONE | 5.03 |
| neutral | 3.09 |

**Average BLEU by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| 0 | 2.26 |
| low | 27.19 |
| none | 4.12 |

---

### chrF++ Metric

**Average chrF++ by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 1 | 11.14 |
| 2 | 25.63 |
| High | 6.05 |
| Medium | 24.21 |
| high | 23.04 |
| medium | 20.95 |
| neutral | 18.49 |

**Average chrF++ by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| NONE | 24.73 |
| CORRECT_LINGUISTIC_ANALYSIS | 21.63 |
| TRANSLATION_ATTEMPT | 20.90 |
| neutral | 18.06 |

**Average chrF++ by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| 0 | 18.39 |
| low | 39.16 |
| none | 19.24 |

---

### MetricX-24 Metric

**Average MetricX-24 by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 1 | 17.50 |
| 2 | 16.38 |
| High | 17.00 |
| Medium | 16.06 |
| high | 16.10 |
| medium | 15.43 |
| neutral | 15.88 |

**Average MetricX-24 by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| NONE | 16.50 |
| CORRECT_LINGUISTIC_ANALYSIS | 16.25 |
| TRANSLATION_ATTEMPT | 15.52 |
| neutral | 15.44 |

**Average MetricX-24 by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| 0 | 16.94 |
| low | 15.69 |
| none | 15.65 |

---

### COMET Metric

**Average COMET by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 1 | 0.37 |
| 2 | 0.46 |
| High | 0.41 |
| Medium | 0.48 |
| high | 0.46 |
| medium | 0.50 |
| neutral | 0.48 |

**Average COMET by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| neutral | 0.50 |
| TRANSLATION_ATTEMPT | 0.49 |
| CORRECT_LINGUISTIC_ANALYSIS | 0.48 |
| NONE | 0.45 |

**Average COMET by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| 0 | 0.41 |
| low | 0.51 |
| none | 0.48 |

---

## 8. Key Insights

- **Best performing trace type**: CORRECT_LINGUISTIC_ANALYSIS (BLEU: 11.23)
- **Worst performing trace type**: neutral (BLEU: 3.09)
- **Performance gap**: 263.8% improvement from worst to best

- **Most common trace type**: TRANSLATION_ATTEMPT (52 examples, 81.2%)
- **Average difficulty score**: 3.23/5.0

---

*Analysis generated from evaluations/guided_cot_eval/Xhosa_English/gemma-3-1b-it/Xhosa_to_English_0_shot_seed_42_identity_None_0_0_0/phase2_annotations.jsonl*
