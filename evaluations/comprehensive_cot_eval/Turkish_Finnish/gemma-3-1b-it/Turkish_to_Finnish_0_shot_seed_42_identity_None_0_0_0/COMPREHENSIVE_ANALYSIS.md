# Phase 2 Comprehensive Analysis

**Total Examples Analyzed**: 64

---

## 1. Difficulty Distribution

Distribution of translation difficulty scores (1=easiest, 5=hardest):

| Difficulty Score | Count | Percentage |
|-----------------|-------|------------|
| 1 | 4 | 6.2% |
| 2 | 17 | 26.6% |
| 3 | 35 | 54.7% |
| 4 | 2 | 3.1% |
| 5 | 6 | 9.4% |

## 2. Linguistic Phenomena Frequencies

Frequency of linguistic phenomena across 64 examples:

| Phenomenon | Count | Percentage |
|------------|-------|------------|
| long_distance_dependency | 56 | 87.5% |
| named_entities | 51 | 79.7% |
| complex_syntax | 36 | 56.2% |
| ambiguity | 2 | 3.1% |
| idiom | 2 | 3.1% |
| figurative_language | 2 | 3.1% |

## 3. Primary Trace Type Distribution

Distribution of reasoning trace types (n=64):

| Trace Type | Count | Percentage |
|------------|-------|------------|
| NONE | 22 | 34.4% |
| TRANSLATION_ATTEMPT | 16 | 25.0% |
| neutral | 13 | 20.3% |
| CORRECT_LINGUISTIC_ANALYSIS | 9 | 14.1% |
| correct_linguistic_analysis | 4 | 6.2% |

## 4. Trace Usefulness Distribution

Distribution of trace usefulness ratings:

| Usefulness Level | Count | Percentage |
|------------------|-------|------------|
| 1 | 1 | 1.6% |
| 2 | 1 | 1.6% |
| High | 3 | 4.7% |
| Medium. The tracing of the distance traveled is relevant to understanding the context of the announcement. | 1 | 1.6% |
| Neutral | 1 | 1.6% |
| helpful | 2 | 3.1% |
| high | 10 | 15.6% |
| medium | 28 | 43.8% |
| neutral | 17 | 26.6% |

## 5. Trace-Translation Overlap Distribution

Distribution of overlap between reasoning traces and translations:

| Overlap Level | Count | Percentage |
|---------------|-------|------------|
| 0 | 2 | 33.3% |
| none | 4 | 66.7% |

## 6. Cross-Tabulations

### 6.1 Difficulty × Trace Type

| Difficulty | CORRECT_LINGUISTIC_ANALYSIS | NONE | TRANSLATION_ATTEMPT | correct_linguistic_analysis | neutral |
|---|---|---|---|---|---|
| 1 | 0 | 2 | 0 | 0 | 2 |
| 2 | 0 | 8 | 1 | 0 | 8 |
| 3 | 6 | 11 | 12 | 3 | 3 |
| 4 | 0 | 0 | 2 | 0 | 0 |
| 5 | 3 | 1 | 1 | 1 | 0 |

### 6.2 Trace Type × Usefulness

| Trace Type | 1 | 2 | High | Medium. The tracing of the distance traveled is relevant to understanding the context of the announcement. | Neutral | helpful | high | medium | neutral |
|---|---|---|---|---|---|---|---|---|---|
| CORRECT_LINGUISTIC_ANALYSIS | 0 | 0 | 2 | 0 | 0 | 0 | 3 | 3 | 1 |
| NONE | 1 | 1 | 1 | 1 | 1 | 2 | 3 | 3 | 9 |
| TRANSLATION_ATTEMPT | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 15 | 0 |
| correct_linguistic_analysis | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 3 | 0 |
| neutral | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 4 | 7 |

## 7. Translation Quality Correlations

### chrF++ Metric

**Average chrF++ by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 1 | 32.10 |
| 2 | 23.74 |
| High | 28.75 |
| Medium. The tracing of the distance traveled is relevant to understanding the context of the announcement. | 36.55 |
| Neutral | 36.75 |
| helpful | 34.10 |
| high | 22.70 |
| medium | 20.10 |
| neutral | 21.24 |

**Average chrF++ by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| NONE | 28.24 |
| CORRECT_LINGUISTIC_ANALYSIS | 24.27 |
| TRANSLATION_ATTEMPT | 20.15 |
| correct_linguistic_analysis | 17.02 |
| neutral | 15.72 |

**Average chrF++ by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| 0 | 27.92 |
| none | 19.06 |

---

### BLEU Metric

**Average BLEU by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 1 | 4.23 |
| 2 | 3.18 |
| High | 4.39 |
| Medium. The tracing of the distance traveled is relevant to understanding the context of the announcement. | 13.83 |
| Neutral | 9.59 |
| helpful | 12.61 |
| high | 5.58 |
| medium | 4.91 |
| neutral | 7.18 |

**Average BLEU by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| NONE | 8.05 |
| correct_linguistic_analysis | 6.02 |
| TRANSLATION_ATTEMPT | 5.29 |
| CORRECT_LINGUISTIC_ANALYSIS | 4.88 |
| neutral | 4.21 |

**Average BLEU by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| 0 | 3.70 |
| none | 2.08 |

---

### COMET Metric

**Average COMET by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 1 | 0.86 |
| 2 | 0.48 |
| High | 0.54 |
| Medium. The tracing of the distance traveled is relevant to understanding the context of the announcement. | 0.57 |
| Neutral | 0.68 |
| helpful | 0.77 |
| high | 0.63 |
| medium | 0.61 |
| neutral | 0.61 |

**Average COMET by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| NONE | 0.66 |
| correct_linguistic_analysis | 0.65 |
| TRANSLATION_ATTEMPT | 0.61 |
| neutral | 0.58 |
| CORRECT_LINGUISTIC_ANALYSIS | 0.57 |

**Average COMET by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| 0 | 0.67 |
| none | 0.60 |

---

### MetricX-24 Metric

**Average MetricX-24 by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 1 | 7.34 |
| 2 | 11.06 |
| High | 11.88 |
| Medium. The tracing of the distance traveled is relevant to understanding the context of the announcement. | 11.06 |
| Neutral | 10.44 |
| helpful | 7.73 |
| high | 11.84 |
| medium | 13.54 |
| neutral | 12.07 |

**Average MetricX-24 by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| correct_linguistic_analysis | 13.75 |
| neutral | 13.50 |
| TRANSLATION_ATTEMPT | 13.16 |
| CORRECT_LINGUISTIC_ANALYSIS | 13.16 |
| NONE | 10.64 |

**Average MetricX-24 by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| 0 | 9.20 |
| none | 13.33 |

---

## 8. Key Insights

- **Best performing trace type**: NONE (BLEU: 8.05)
- **Worst performing trace type**: neutral (BLEU: 4.21)
- **Performance gap**: 91.2% improvement from worst to best

- **Most common trace type**: NONE (22 examples, 34.4%)
- **Average difficulty score**: 2.83/5.0

---

*Analysis generated from evaluations/comprehensive_cot_eval/Turkish_Finnish/gemma-3-1b-it/Turkish_to_Finnish_0_shot_seed_42_identity_None_0_0_0/phase2_annotations.jsonl*
