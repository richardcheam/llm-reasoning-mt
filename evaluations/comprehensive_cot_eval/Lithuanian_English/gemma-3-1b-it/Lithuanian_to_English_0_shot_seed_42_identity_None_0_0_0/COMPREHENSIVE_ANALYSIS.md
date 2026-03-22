# Phase 2 Comprehensive Analysis

**Total Examples Analyzed**: 64

---

## 1. Difficulty Distribution

Distribution of translation difficulty scores (1=easiest, 5=hardest):

| Difficulty Score | Count | Percentage |
|-----------------|-------|------------|
| 1 | 3 | 4.8% |
| 2 | 18 | 28.6% |
| 3 | 37 | 58.7% |
| 4 | 3 | 4.8% |
| 5 | 2 | 3.2% |

## 2. Linguistic Phenomena Frequencies

Frequency of linguistic phenomena across 63 examples:

| Phenomenon | Count | Percentage |
|------------|-------|------------|
| named_entities | 50 | 79.4% |
| long_distance_dependency | 43 | 68.3% |
| complex_syntax | 22 | 34.9% |
| idiom | 1 | 1.6% |

## 3. Primary Trace Type Distribution

Distribution of reasoning trace types (n=63):

| Trace Type | Count | Percentage |
|------------|-------|------------|
| neutral | 20 | 31.7% |
| NONE | 16 | 25.4% |
| TRANSLATION_ATTEMPT | 14 | 22.2% |
| CORRECT_LINGUISTIC_ANALYSIS | 13 | 20.6% |

## 4. Trace Usefulness Distribution

Distribution of trace usefulness ratings:

| Usefulness Level | Count | Percentage |
|------------------|-------|------------|
| Medium | 1 | 1.6% |
| helpful | 1 | 1.6% |
| high | 11 | 17.5% |
| medium | 21 | 33.3% |
| neutral | 29 | 46.0% |

## 5. Trace-Translation Overlap Distribution

Distribution of overlap between reasoning traces and translations:

| Overlap Level | Count | Percentage |
|---------------|-------|------------|
| none | 4 | 100.0% |

## 6. Cross-Tabulations

### 6.1 Difficulty × Trace Type

| Difficulty | CORRECT_LINGUISTIC_ANALYSIS | NONE | TRANSLATION_ATTEMPT | neutral |
|---|---|---|---|---|
| 1 | 1 | 2 | 0 | 0 |
| 2 | 2 | 1 | 0 | 15 |
| 3 | 9 | 12 | 11 | 5 |
| 4 | 0 | 0 | 3 | 0 |
| 5 | 1 | 1 | 0 | 0 |

### 6.2 Trace Type × Usefulness

| Trace Type | Medium | helpful | high | medium | neutral |
|---|---|---|---|---|---|
| CORRECT_LINGUISTIC_ANALYSIS | 0 | 0 | 8 | 5 | 0 |
| NONE | 1 | 1 | 1 | 3 | 10 |
| TRANSLATION_ATTEMPT | 0 | 0 | 2 | 11 | 1 |
| neutral | 0 | 0 | 0 | 2 | 18 |

## 7. Translation Quality Correlations

### MetricX-24 Metric

**Average MetricX-24 by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| Medium | 2.45 |
| helpful | 6.22 |
| high | 10.64 |
| medium | 9.72 |
| neutral | 7.36 |

**Average MetricX-24 by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| TRANSLATION_ATTEMPT | 10.31 |
| CORRECT_LINGUISTIC_ANALYSIS | 9.80 |
| NONE | 8.41 |
| neutral | 6.85 |

**Average MetricX-24 by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| none | 8.62 |

---

### COMET Metric

**Average COMET by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| Medium | 0.83 |
| helpful | 0.76 |
| high | 0.71 |
| medium | 0.70 |
| neutral | 0.79 |

**Average COMET by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| neutral | 0.79 |
| NONE | 0.74 |
| CORRECT_LINGUISTIC_ANALYSIS | 0.71 |
| TRANSLATION_ATTEMPT | 0.71 |

**Average COMET by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| none | 0.71 |

---

### chrF++ Metric

**Average chrF++ by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| Medium | 33.85 |
| helpful | 26.45 |
| high | 33.13 |
| medium | 33.21 |
| neutral | 41.28 |

**Average chrF++ by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| neutral | 42.08 |
| NONE | 35.78 |
| CORRECT_LINGUISTIC_ANALYSIS | 35.17 |
| TRANSLATION_ATTEMPT | 31.99 |

**Average chrF++ by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| none | 32.78 |

---

### BLEU Metric

**Average BLEU by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| Medium | 10.47 |
| helpful | 6.02 |
| high | 11.58 |
| medium | 8.75 |
| neutral | 17.79 |

**Average BLEU by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| neutral | 20.29 |
| CORRECT_LINGUISTIC_ANALYSIS | 12.21 |
| NONE | 9.85 |
| TRANSLATION_ATTEMPT | 8.67 |

**Average BLEU by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| none | 8.45 |

---

## 8. Key Insights

- **Best performing trace type**: neutral (BLEU: 20.29)
- **Worst performing trace type**: TRANSLATION_ATTEMPT (BLEU: 8.67)
- **Performance gap**: 134.0% improvement from worst to best

- **Most common trace type**: neutral (20 examples, 31.7%)
- **Average difficulty score**: 2.73/5.0

---

*Analysis generated from evaluations/comprehensive_cot_eval/Lithuanian_English/gemma-3-1b-it/Lithuanian_to_English_0_shot_seed_42_identity_None_0_0_0/phase2_annotations.jsonl*
