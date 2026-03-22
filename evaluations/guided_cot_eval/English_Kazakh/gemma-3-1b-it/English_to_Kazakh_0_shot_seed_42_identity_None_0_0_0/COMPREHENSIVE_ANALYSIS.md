# Phase 2 Comprehensive Analysis

**Total Examples Analyzed**: 64

---

## 1. Difficulty Distribution

Distribution of translation difficulty scores (1=easiest, 5=hardest):

| Difficulty Score | Count | Percentage |
|-----------------|-------|------------|
| 1 | 1 | 1.6% |
| 2 | 1 | 1.6% |
| 3 | 50 | 82.0% |
| 4 | 8 | 13.1% |
| 5 | 1 | 1.6% |

## 2. Linguistic Phenomena Frequencies

Frequency of linguistic phenomena across 61 examples:

| Phenomenon | Count | Percentage |
|------------|-------|------------|
| long_distance_dependency | 60 | 98.4% |
| complex_syntax | 52 | 85.2% |
| named_entities | 39 | 63.9% |
| ambiguity | 3 | 4.9% |
| idiom | 3 | 4.9% |
| figurative_language | 3 | 4.9% |

## 3. Primary Trace Type Distribution

Distribution of reasoning trace types (n=61):

| Trace Type | Count | Percentage |
|------------|-------|------------|
| CORRECT_LINGUISTIC_ANALYSIS | 44 | 72.1% |
| TRANSLATION_ATTEMPT | 10 | 16.4% |
| NONE | 6 | 9.8% |
| neutral | 1 | 1.6% |

## 4. Trace Usefulness Distribution

Distribution of trace usefulness ratings:

| Usefulness Level | Count | Percentage |
|------------------|-------|------------|
| 2 | 3 | 4.9% |
| High | 1 | 1.6% |
| Medium | 4 | 6.6% |
| high | 15 | 24.6% |
| medium | 33 | 54.1% |
| neutral | 5 | 8.2% |

## 5. Trace-Translation Overlap Distribution

Distribution of overlap between reasoning traces and translations:

| Overlap Level | Count | Percentage |
|---------------|-------|------------|
| low | 1 | 2.8% |
| none | 35 | 97.2% |

## 6. Cross-Tabulations

### 6.1 Difficulty × Trace Type

| Difficulty | CORRECT_LINGUISTIC_ANALYSIS | NONE | TRANSLATION_ATTEMPT | neutral |
|---|---|---|---|---|
| 1 | 1 | 0 | 0 | 0 |
| 2 | 0 | 1 | 0 | 0 |
| 3 | 36 | 5 | 8 | 1 |
| 4 | 6 | 0 | 2 | 0 |
| 5 | 1 | 0 | 0 | 0 |

### 6.2 Trace Type × Usefulness

| Trace Type | 2 | High | Medium | high | medium | neutral |
|---|---|---|---|---|---|---|
| CORRECT_LINGUISTIC_ANALYSIS | 2 | 1 | 2 | 15 | 24 | 0 |
| NONE | 0 | 0 | 0 | 0 | 1 | 5 |
| TRANSLATION_ATTEMPT | 0 | 0 | 2 | 0 | 8 | 0 |
| neutral | 1 | 0 | 0 | 0 | 0 | 0 |

## 7. Translation Quality Correlations

### MetricX-24 Metric

**Average MetricX-24 by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 2 | 8.45 |
| High | 6.50 |
| Medium | 13.38 |
| high | 8.78 |
| medium | 7.47 |
| neutral | 8.00 |

**Average MetricX-24 by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| TRANSLATION_ATTEMPT | 10.68 |
| neutral | 7.91 |
| CORRECT_LINGUISTIC_ANALYSIS | 7.85 |
| NONE | 7.23 |

**Average MetricX-24 by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| low | 17.12 |
| none | 8.32 |

---

### chrF++ Metric

**Average chrF++ by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 2 | 13.84 |
| High | 11.80 |
| Medium | 10.55 |
| high | 15.29 |
| medium | 14.47 |
| neutral | 15.44 |

**Average chrF++ by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| CORRECT_LINGUISTIC_ANALYSIS | 15.36 |
| NONE | 15.11 |
| TRANSLATION_ATTEMPT | 10.45 |
| neutral | 8.66 |

**Average chrF++ by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| low | 0.83 |
| none | 13.85 |

---

### BLEU Metric

**Average BLEU by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 2 | 4.44 |
| High | 2.04 |
| Medium | 2.12 |
| high | 3.61 |
| medium | 4.27 |
| neutral | 4.20 |

**Average BLEU by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| CORRECT_LINGUISTIC_ANALYSIS | 4.42 |
| NONE | 3.70 |
| TRANSLATION_ATTEMPT | 2.13 |
| neutral | 1.92 |

**Average BLEU by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| low | 0.87 |
| none | 3.90 |

---

### COMET Metric

**Average COMET by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 2 | 0.62 |
| High | 0.64 |
| Medium | 0.48 |
| high | 0.62 |
| medium | 0.68 |
| neutral | 0.70 |

**Average COMET by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| NONE | 0.70 |
| CORRECT_LINGUISTIC_ANALYSIS | 0.67 |
| neutral | 0.59 |
| TRANSLATION_ATTEMPT | 0.56 |

**Average COMET by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| low | 0.26 |
| none | 0.66 |

---

## 8. Key Insights

- **Best performing trace type**: CORRECT_LINGUISTIC_ANALYSIS (BLEU: 4.42)
- **Worst performing trace type**: neutral (BLEU: 1.92)
- **Performance gap**: 129.9% improvement from worst to best

- **Most common trace type**: CORRECT_LINGUISTIC_ANALYSIS (44 examples, 72.1%)
- **Average difficulty score**: 3.11/5.0

---

*Analysis generated from evaluations/guided_cot_eval/English_Kazakh/gemma-3-1b-it/English_to_Kazakh_0_shot_seed_42_identity_None_0_0_0/phase2_annotations.jsonl*
