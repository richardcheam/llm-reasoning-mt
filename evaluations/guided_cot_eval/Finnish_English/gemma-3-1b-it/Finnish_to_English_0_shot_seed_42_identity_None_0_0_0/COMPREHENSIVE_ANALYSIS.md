# Phase 2 Comprehensive Analysis

**Total Examples Analyzed**: 64

---

## 1. Difficulty Distribution

Distribution of translation difficulty scores (1=easiest, 5=hardest):

| Difficulty Score | Count | Percentage |
|-----------------|-------|------------|
| 2 | 17 | 27.0% |
| 3 | 43 | 68.3% |
| 4 | 3 | 4.8% |

## 2. Linguistic Phenomena Frequencies

Frequency of linguistic phenomena across 63 examples:

| Phenomenon | Count | Percentage |
|------------|-------|------------|
| long_distance_dependency | 60 | 95.2% |
| named_entities | 52 | 82.5% |
| complex_syntax | 40 | 63.5% |

## 3. Primary Trace Type Distribution

Distribution of reasoning trace types (n=63):

| Trace Type | Count | Percentage |
|------------|-------|------------|
| TRANSLATION_ATTEMPT | 44 | 69.8% |
| NONE | 12 | 19.0% |
| neutral | 4 | 6.3% |
| CORRECT_LINGUISTIC_ANALYSIS | 2 | 3.2% |
| REASONING | 1 | 1.6% |

## 4. Trace Usefulness Distribution

Distribution of trace usefulness ratings:

| Usefulness Level | Count | Percentage |
|------------------|-------|------------|
| high | 12 | 19.0% |
| medium | 46 | 73.0% |
| neutral | 5 | 7.9% |

## 5. Trace-Translation Overlap Distribution

Distribution of overlap between reasoning traces and translations:

| Overlap Level | Count | Percentage |
|---------------|-------|------------|
| none | 13 | 100.0% |

## 6. Cross-Tabulations

### 6.1 Difficulty × Trace Type

| Difficulty | CORRECT_LINGUISTIC_ANALYSIS | NONE | REASONING | TRANSLATION_ATTEMPT | neutral |
|---|---|---|---|---|---|
| 2 | 1 | 7 | 0 | 5 | 4 |
| 3 | 1 | 4 | 1 | 37 | 0 |
| 4 | 0 | 1 | 0 | 2 | 0 |

### 6.2 Trace Type × Usefulness

| Trace Type | high | medium | neutral |
|---|---|---|---|
| CORRECT_LINGUISTIC_ANALYSIS | 2 | 0 | 0 |
| NONE | 1 | 8 | 3 |
| REASONING | 0 | 1 | 0 |
| TRANSLATION_ATTEMPT | 8 | 35 | 1 |
| neutral | 1 | 2 | 1 |

## 7. Translation Quality Correlations

### BLEU Metric

**Average BLEU by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| high | 16.38 |
| medium | 15.19 |
| neutral | 13.53 |

**Average BLEU by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| TRANSLATION_ATTEMPT | 16.31 |
| neutral | 15.18 |
| NONE | 13.30 |
| CORRECT_LINGUISTIC_ANALYSIS | 9.96 |
| REASONING | 5.12 |

**Average BLEU by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| none | 12.26 |

---

### COMET Metric

**Average COMET by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| high | 0.84 |
| medium | 0.81 |
| neutral | 0.73 |

**Average COMET by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| TRANSLATION_ATTEMPT | 0.82 |
| NONE | 0.82 |
| CORRECT_LINGUISTIC_ANALYSIS | 0.75 |
| neutral | 0.71 |
| REASONING | 0.65 |

**Average COMET by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| none | 0.80 |

---

### MetricX-24 Metric

**Average MetricX-24 by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| high | 4.91 |
| medium | 6.76 |
| neutral | 9.12 |

**Average MetricX-24 by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| REASONING | 10.88 |
| neutral | 9.36 |
| NONE | 7.12 |
| CORRECT_LINGUISTIC_ANALYSIS | 6.98 |
| TRANSLATION_ATTEMPT | 6.08 |

**Average MetricX-24 by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| none | 7.12 |

---

### chrF++ Metric

**Average chrF++ by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| high | 41.58 |
| medium | 39.40 |
| neutral | 30.14 |

**Average chrF++ by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| TRANSLATION_ATTEMPT | 41.14 |
| NONE | 37.41 |
| CORRECT_LINGUISTIC_ANALYSIS | 36.42 |
| REASONING | 26.68 |
| neutral | 25.86 |

**Average chrF++ by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| none | 38.37 |

---

## 8. Key Insights

- **Best performing trace type**: TRANSLATION_ATTEMPT (BLEU: 16.31)
- **Worst performing trace type**: REASONING (BLEU: 5.12)
- **Performance gap**: 218.4% improvement from worst to best

- **Most common trace type**: TRANSLATION_ATTEMPT (44 examples, 69.8%)
- **Average difficulty score**: 2.78/5.0

---

*Analysis generated from evaluations/guided_cot_eval/Finnish_English/gemma-3-1b-it/Finnish_to_English_0_shot_seed_42_identity_None_0_0_0/phase2_annotations.jsonl*
