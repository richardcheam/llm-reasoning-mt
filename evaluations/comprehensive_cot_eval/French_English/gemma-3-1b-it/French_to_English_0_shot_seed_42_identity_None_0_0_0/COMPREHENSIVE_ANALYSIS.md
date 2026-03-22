# Phase 2 Comprehensive Analysis

**Total Examples Analyzed**: 64

---

## 1. Difficulty Distribution

Distribution of translation difficulty scores (1=easiest, 5=hardest):

| Difficulty Score | Count | Percentage |
|-----------------|-------|------------|
| 1 | 1 | 1.6% |
| 2 | 29 | 45.3% |
| 3 | 28 | 43.8% |
| 4 | 3 | 4.7% |
| 5 | 3 | 4.7% |

## 2. Linguistic Phenomena Frequencies

Frequency of linguistic phenomena across 64 examples:

| Phenomenon | Count | Percentage |
|------------|-------|------------|
| named_entities | 49 | 76.6% |
| long_distance_dependency | 47 | 73.4% |
| complex_syntax | 17 | 26.6% |

## 3. Primary Trace Type Distribution

Distribution of reasoning trace types (n=64):

| Trace Type | Count | Percentage |
|------------|-------|------------|
| neutral | 24 | 37.5% |
| NONE | 23 | 35.9% |
| TRANSLATION_ATTEMPT | 11 | 17.2% |
| CORRECT_LINGUISTIC_ANALYSIS | 6 | 9.4% |

## 4. Trace Usefulness Distribution

Distribution of trace usefulness ratings:

| Usefulness Level | Count | Percentage |
|------------------|-------|------------|
| 5 - Very Helpful | 1 | 1.6% |
| helpful | 1 | 1.6% |
| high | 8 | 12.5% |
| medium | 18 | 28.1% |
| neutral | 36 | 56.2% |

## 5. Trace-Translation Overlap Distribution

Distribution of overlap between reasoning traces and translations:

| Overlap Level | Count | Percentage |
|---------------|-------|------------|
| none | 1 | 100.0% |

## 6. Cross-Tabulations

### 6.1 Difficulty × Trace Type

| Difficulty | CORRECT_LINGUISTIC_ANALYSIS | NONE | TRANSLATION_ATTEMPT | neutral |
|---|---|---|---|---|
| 1 | 0 | 1 | 0 | 0 |
| 2 | 0 | 6 | 0 | 23 |
| 3 | 5 | 14 | 8 | 1 |
| 4 | 0 | 1 | 2 | 0 |
| 5 | 1 | 1 | 1 | 0 |

### 6.2 Trace Type × Usefulness

| Trace Type | 5 - Very Helpful | helpful | high | medium | neutral |
|---|---|---|---|---|---|
| CORRECT_LINGUISTIC_ANALYSIS | 1 | 0 | 5 | 0 | 0 |
| NONE | 0 | 1 | 1 | 7 | 14 |
| TRANSLATION_ATTEMPT | 0 | 0 | 1 | 10 | 0 |
| neutral | 0 | 0 | 1 | 1 | 22 |

## 7. Translation Quality Correlations

### BLEU Metric

**Average BLEU by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 5 - Very Helpful | 39.46 |
| helpful | 5.06 |
| high | 27.61 |
| medium | 20.94 |
| neutral | 31.10 |

**Average BLEU by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| neutral | 31.51 |
| CORRECT_LINGUISTIC_ANALYSIS | 29.25 |
| NONE | 26.92 |
| TRANSLATION_ATTEMPT | 19.18 |

**Average BLEU by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| none | 20.36 |

---

### chrF++ Metric

**Average chrF++ by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 5 - Very Helpful | 55.11 |
| helpful | 25.40 |
| high | 52.75 |
| medium | 48.31 |
| neutral | 54.17 |

**Average chrF++ by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| neutral | 54.22 |
| CORRECT_LINGUISTIC_ANALYSIS | 51.85 |
| NONE | 51.76 |
| TRANSLATION_ATTEMPT | 47.21 |

**Average chrF++ by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| none | 49.32 |

---

### COMET Metric

**Average COMET by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 5 - Very Helpful | 0.89 |
| helpful | 0.78 |
| high | 0.84 |
| medium | 0.85 |
| neutral | 0.86 |

**Average COMET by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| neutral | 0.86 |
| TRANSLATION_ATTEMPT | 0.86 |
| NONE | 0.85 |
| CORRECT_LINGUISTIC_ANALYSIS | 0.81 |

**Average COMET by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| none | 0.85 |

---

### MetricX-24 Metric

**Average MetricX-24 by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 5 - Very Helpful | 3.16 |
| helpful | 8.25 |
| high | 4.59 |
| medium | 3.58 |
| neutral | 3.92 |

**Average MetricX-24 by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| CORRECT_LINGUISTIC_ANALYSIS | 4.72 |
| neutral | 4.07 |
| TRANSLATION_ATTEMPT | 3.82 |
| NONE | 3.73 |

**Average MetricX-24 by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| none | 2.61 |

---

## 8. Key Insights

- **Best performing trace type**: neutral (BLEU: 31.51)
- **Worst performing trace type**: TRANSLATION_ATTEMPT (BLEU: 19.18)
- **Performance gap**: 64.3% improvement from worst to best

- **Most common trace type**: neutral (24 examples, 37.5%)
- **Average difficulty score**: 2.66/5.0

---

*Analysis generated from evaluations/comprehensive_cot_eval/French_English/gemma-3-1b-it/French_to_English_0_shot_seed_42_identity_None_0_0_0/phase2_annotations.jsonl*
