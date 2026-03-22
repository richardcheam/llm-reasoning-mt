# Phase 2 Comprehensive Analysis

**Total Examples Analyzed**: 64

---

## 1. Difficulty Distribution

Distribution of translation difficulty scores (1=easiest, 5=hardest):

| Difficulty Score | Count | Percentage |
|-----------------|-------|------------|
| 1 | 2 | 3.4% |
| 2 | 5 | 8.5% |
| 3 | 49 | 83.1% |
| 4 | 2 | 3.4% |
| 5 | 1 | 1.7% |

## 2. Linguistic Phenomena Frequencies

Frequency of linguistic phenomena across 59 examples:

| Phenomenon | Count | Percentage |
|------------|-------|------------|
| long_distance_dependency | 57 | 96.6% |
| named_entities | 48 | 81.4% |
| complex_syntax | 48 | 81.4% |
| idiom | 2 | 3.4% |
| ambiguity | 1 | 1.7% |
| figurative_language | 1 | 1.7% |

## 3. Primary Trace Type Distribution

Distribution of reasoning trace types (n=59):

| Trace Type | Count | Percentage |
|------------|-------|------------|
| TRANSLATION_ATTEMPT | 42 | 71.2% |
| neutral | 7 | 11.9% |
| NONE | 5 | 8.5% |
| CORRECT_LINGUISTIC_ANALYSIS | 3 | 5.1% |
| HALLUCINATED_RULE | 1 | 1.7% |
| Translation Attempt | 1 | 1.7% |

## 4. Trace Usefulness Distribution

Distribution of trace usefulness ratings:

| Usefulness Level | Count | Percentage |
|------------------|-------|------------|
| 3 | 1 | 1.7% |
| High | 1 | 1.7% |
| Medium | 4 | 6.8% |
| high | 4 | 6.8% |
| medium | 44 | 74.6% |
| neutral | 5 | 8.5% |

## 5. Trace-Translation Overlap Distribution

Distribution of overlap between reasoning traces and translations:

| Overlap Level | Count | Percentage |
|---------------|-------|------------|
| 0 | 1 | 2.5% |
| low | 3 | 7.5% |
| none | 36 | 90.0% |

## 6. Cross-Tabulations

### 6.1 Difficulty × Trace Type

| Difficulty | CORRECT_LINGUISTIC_ANALYSIS | HALLUCINATED_RULE | NONE | TRANSLATION_ATTEMPT | Translation Attempt | neutral |
|---|---|---|---|---|---|---|
| 1 | 0 | 0 | 0 | 0 | 0 | 2 |
| 2 | 0 | 0 | 1 | 1 | 0 | 3 |
| 3 | 3 | 1 | 4 | 38 | 1 | 2 |
| 4 | 0 | 0 | 0 | 2 | 0 | 0 |
| 5 | 0 | 0 | 0 | 1 | 0 | 0 |

### 6.2 Trace Type × Usefulness

| Trace Type | 3 | High | Medium | high | medium | neutral |
|---|---|---|---|---|---|---|
| CORRECT_LINGUISTIC_ANALYSIS | 0 | 0 | 0 | 2 | 1 | 0 |
| HALLUCINATED_RULE | 0 | 0 | 1 | 0 | 0 | 0 |
| NONE | 1 | 0 | 0 | 0 | 2 | 2 |
| TRANSLATION_ATTEMPT | 0 | 1 | 2 | 2 | 36 | 1 |
| Translation Attempt | 0 | 0 | 1 | 0 | 0 | 0 |
| neutral | 0 | 0 | 0 | 0 | 5 | 2 |

## 7. Translation Quality Correlations

### COMET Metric

**Average COMET by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 3 | 0.88 |
| High | 0.73 |
| Medium | 0.66 |
| high | 0.84 |
| medium | 0.76 |
| neutral | 0.76 |

**Average COMET by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| neutral | 0.82 |
| NONE | 0.80 |
| CORRECT_LINGUISTIC_ANALYSIS | 0.79 |
| HALLUCINATED_RULE | 0.75 |
| TRANSLATION_ATTEMPT | 0.75 |
| Translation Attempt | 0.50 |

**Average COMET by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| 0 | 0.88 |
| low | 0.61 |
| none | 0.74 |

---

### chrF++ Metric

**Average chrF++ by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 3 | 60.28 |
| High | 47.72 |
| Medium | 40.90 |
| high | 47.30 |
| medium | 44.33 |
| neutral | 41.84 |

**Average chrF++ by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| neutral | 52.10 |
| CORRECT_LINGUISTIC_ANALYSIS | 49.03 |
| Translation Attempt | 45.54 |
| TRANSLATION_ATTEMPT | 43.19 |
| NONE | 43.11 |
| HALLUCINATED_RULE | 33.78 |

**Average chrF++ by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| 0 | 60.28 |
| low | 44.47 |
| none | 43.53 |

---

### BLEU Metric

**Average BLEU by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 3 | 36.32 |
| High | 23.11 |
| Medium | 15.54 |
| high | 21.06 |
| medium | 22.21 |
| neutral | 17.47 |

**Average BLEU by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| neutral | 35.93 |
| CORRECT_LINGUISTIC_ANALYSIS | 26.50 |
| NONE | 22.95 |
| TRANSLATION_ATTEMPT | 18.93 |
| HALLUCINATED_RULE | 14.74 |
| Translation Attempt | 14.67 |

**Average BLEU by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| 0 | 36.32 |
| low | 17.04 |
| none | 20.47 |

---

### MetricX-24 Metric

**Average MetricX-24 by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 3 | 2.22 |
| High | 7.81 |
| Medium | 8.00 |
| high | 1.89 |
| medium | 5.80 |
| neutral | 6.43 |

**Average MetricX-24 by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| Translation Attempt | 12.06 |
| TRANSLATION_ATTEMPT | 6.14 |
| NONE | 5.18 |
| CORRECT_LINGUISTIC_ANALYSIS | 3.79 |
| neutral | 3.78 |
| HALLUCINATED_RULE | 3.33 |

**Average MetricX-24 by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| 0 | 2.22 |
| low | 6.68 |
| none | 6.42 |

---

## 8. Key Insights

- **Best performing trace type**: neutral (BLEU: 35.93)
- **Worst performing trace type**: Translation Attempt (BLEU: 14.67)
- **Performance gap**: 145.0% improvement from worst to best

- **Most common trace type**: TRANSLATION_ATTEMPT (42 examples, 71.2%)
- **Average difficulty score**: 2.92/5.0

---

*Analysis generated from evaluations/guided_cot_eval/German_French/gemma-3-1b-it/German_to_French_0_shot_seed_42_identity_None_0_0_0/phase2_annotations.jsonl*
