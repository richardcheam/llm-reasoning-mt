# Phase 2 Comprehensive Analysis

**Total Examples Analyzed**: 64

---

## 1. Difficulty Distribution

Distribution of translation difficulty scores (1=easiest, 5=hardest):

| Difficulty Score | Count | Percentage |
|-----------------|-------|------------|
| 1 | 1 | 1.6% |
| 2 | 19 | 30.6% |
| 3 | 38 | 61.3% |
| 4 | 3 | 4.8% |
| 5 | 1 | 1.6% |

## 2. Linguistic Phenomena Frequencies

Frequency of linguistic phenomena across 62 examples:

| Phenomenon | Count | Percentage |
|------------|-------|------------|
| long_distance_dependency | 58 | 93.5% |
| named_entities | 54 | 87.1% |
| complex_syntax | 34 | 54.8% |

## 3. Primary Trace Type Distribution

Distribution of reasoning trace types (n=62):

| Trace Type | Count | Percentage |
|------------|-------|------------|
| NONE | 22 | 35.5% |
| TRANSLATION_ATTEMPT | 22 | 35.5% |
| neutral | 12 | 19.4% |
| CORRECT_LINGUISTIC_ANALYSIS | 4 | 6.5% |
| correct_linguistic_analysis | 1 | 1.6% |
| null | 1 | 1.6% |

## 4. Trace Usefulness Distribution

Distribution of trace usefulness ratings:

| Usefulness Level | Count | Percentage |
|------------------|-------|------------|
| high | 12 | 19.4% |
| medium | 32 | 51.6% |
| neutral | 18 | 29.0% |

## 5. Trace-Translation Overlap Distribution

Distribution of overlap between reasoning traces and translations:

| Overlap Level | Count | Percentage |
|---------------|-------|------------|
| low | 1 | 25.0% |
| none | 3 | 75.0% |

## 6. Cross-Tabulations

### 6.1 Difficulty × Trace Type

| Difficulty | CORRECT_LINGUISTIC_ANALYSIS | NONE | TRANSLATION_ATTEMPT | correct_linguistic_analysis | neutral | null |
|---|---|---|---|---|---|---|
| 1 | 0 | 0 | 0 | 0 | 0 | 1 |
| 2 | 0 | 8 | 2 | 0 | 9 | 0 |
| 3 | 4 | 12 | 18 | 1 | 3 | 0 |
| 4 | 0 | 2 | 1 | 0 | 0 | 0 |
| 5 | 0 | 0 | 1 | 0 | 0 | 0 |

### 6.2 Trace Type × Usefulness

| Trace Type | high | medium | neutral |
|---|---|---|---|
| CORRECT_LINGUISTIC_ANALYSIS | 4 | 0 | 0 |
| NONE | 1 | 11 | 10 |
| TRANSLATION_ATTEMPT | 5 | 17 | 0 |
| correct_linguistic_analysis | 1 | 0 | 0 |
| neutral | 1 | 4 | 7 |
| null | 0 | 0 | 1 |

## 7. Translation Quality Correlations

### chrF++ Metric

**Average chrF++ by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| high | 55.70 |
| medium | 55.25 |
| neutral | 45.78 |

**Average chrF++ by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| CORRECT_LINGUISTIC_ANALYSIS | 63.48 |
| neutral | 54.80 |
| TRANSLATION_ATTEMPT | 51.53 |
| NONE | 51.06 |
| null | 49.86 |
| correct_linguistic_analysis | 41.86 |

**Average chrF++ by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| low | 75.06 |
| none | 48.10 |

---

### COMET Metric

**Average COMET by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| high | 0.85 |
| medium | 0.86 |
| neutral | 0.82 |

**Average COMET by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| CORRECT_LINGUISTIC_ANALYSIS | 0.89 |
| null | 0.88 |
| neutral | 0.85 |
| correct_linguistic_analysis | 0.85 |
| TRANSLATION_ATTEMPT | 0.85 |
| NONE | 0.84 |

**Average COMET by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| low | 0.93 |
| none | 0.85 |

---

### BLEU Metric

**Average BLEU by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| high | 30.50 |
| medium | 31.54 |
| neutral | 22.01 |

**Average BLEU by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| CORRECT_LINGUISTIC_ANALYSIS | 38.87 |
| neutral | 31.48 |
| NONE | 28.13 |
| TRANSLATION_ATTEMPT | 26.60 |
| correct_linguistic_analysis | 18.61 |
| null | 15.64 |

**Average BLEU by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| low | 60.51 |
| none | 25.27 |

---

### MetricX-24 Metric

**Average MetricX-24 by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| high | 3.89 |
| medium | 3.96 |
| neutral | 5.26 |

**Average MetricX-24 by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| null | 8.62 |
| TRANSLATION_ATTEMPT | 4.59 |
| NONE | 4.40 |
| correct_linguistic_analysis | 4.06 |
| neutral | 4.05 |
| CORRECT_LINGUISTIC_ANALYSIS | 2.23 |

**Average MetricX-24 by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| low | 1.62 |
| none | 6.17 |

---

## 8. Key Insights

- **Best performing trace type**: CORRECT_LINGUISTIC_ANALYSIS (BLEU: 38.87)
- **Worst performing trace type**: null (BLEU: 15.64)
- **Performance gap**: 148.5% improvement from worst to best

- **Most common trace type**: NONE (22 examples, 35.5%)
- **Average difficulty score**: 2.74/5.0

---

*Analysis generated from evaluations/guided_cot_eval/French_English/gemma-3-1b-it/French_to_English_0_shot_seed_42_identity_None_0_0_0/phase2_annotations.jsonl*
