# Phase 2 Comprehensive Analysis

**Total Examples Analyzed**: 64

---

## 1. Difficulty Distribution

Distribution of translation difficulty scores (1=easiest, 5=hardest):

| Difficulty Score | Count | Percentage |
|-----------------|-------|------------|
| 1 | 1 | 1.6% |
| 2 | 19 | 30.2% |
| 3 | 32 | 50.8% |
| 4 | 7 | 11.1% |
| 5 | 4 | 6.3% |

## 2. Linguistic Phenomena Frequencies

Frequency of linguistic phenomena across 63 examples:

| Phenomenon | Count | Percentage |
|------------|-------|------------|
| long_distance_dependency | 54 | 85.7% |
| named_entities | 41 | 65.1% |
| complex_syntax | 33 | 52.4% |

## 3. Primary Trace Type Distribution

Distribution of reasoning trace types (n=63):

| Trace Type | Count | Percentage |
|------------|-------|------------|
| neutral | 18 | 28.6% |
| TRANSLATION_ATTEMPT | 17 | 27.0% |
| CORRECT_LINGUISTIC_ANALYSIS | 14 | 22.2% |
| NONE | 10 | 15.9% |
| correct_linguistic_analysis | 3 | 4.8% |
| HALLUCINATED_RULE | 1 | 1.6% |

## 4. Trace Usefulness Distribution

Distribution of trace usefulness ratings:

| Usefulness Level | Count | Percentage |
|------------------|-------|------------|
| High | 1 | 1.6% |
| high | 6 | 9.5% |
| medium | 27 | 42.9% |
| neutral | 29 | 46.0% |

## 5. Trace-Translation Overlap Distribution

Distribution of overlap between reasoning traces and translations:

| Overlap Level | Count | Percentage |
|---------------|-------|------------|
| none | 14 | 100.0% |

## 6. Cross-Tabulations

### 6.1 Difficulty × Trace Type

| Difficulty | CORRECT_LINGUISTIC_ANALYSIS | HALLUCINATED_RULE | NONE | TRANSLATION_ATTEMPT | correct_linguistic_analysis | neutral |
|---|---|---|---|---|---|---|
| 1 | 0 | 0 | 0 | 0 | 0 | 1 |
| 2 | 2 | 0 | 2 | 0 | 0 | 15 |
| 3 | 9 | 1 | 7 | 11 | 2 | 2 |
| 4 | 1 | 0 | 1 | 5 | 0 | 0 |
| 5 | 2 | 0 | 0 | 1 | 1 | 0 |

### 6.2 Trace Type × Usefulness

| Trace Type | High | high | medium | neutral |
|---|---|---|---|---|
| CORRECT_LINGUISTIC_ANALYSIS | 1 | 3 | 8 | 2 |
| HALLUCINATED_RULE | 0 | 0 | 0 | 1 |
| NONE | 0 | 0 | 1 | 9 |
| TRANSLATION_ATTEMPT | 0 | 2 | 14 | 1 |
| correct_linguistic_analysis | 0 | 1 | 2 | 0 |
| neutral | 0 | 0 | 2 | 16 |

## 7. Translation Quality Correlations

### BLEU Metric

**Average BLEU by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| High | 0.00 |
| high | 2.46 |
| medium | 2.97 |
| neutral | 5.17 |

**Average BLEU by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| HALLUCINATED_RULE | 9.47 |
| neutral | 6.38 |
| CORRECT_LINGUISTIC_ANALYSIS | 3.91 |
| TRANSLATION_ATTEMPT | 2.68 |
| NONE | 2.03 |
| correct_linguistic_analysis | 0.00 |

**Average BLEU by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| none | 1.46 |

---

### chrF++ Metric

**Average chrF++ by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| High | 3.53 |
| high | 10.30 |
| medium | 10.66 |
| neutral | 16.66 |

**Average chrF++ by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| HALLUCINATED_RULE | 32.81 |
| neutral | 18.69 |
| CORRECT_LINGUISTIC_ANALYSIS | 14.95 |
| NONE | 9.94 |
| TRANSLATION_ATTEMPT | 9.20 |
| correct_linguistic_analysis | 0.67 |

**Average chrF++ by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| none | 8.77 |

---

### MetricX-24 Metric

**Average MetricX-24 by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| High | 14.94 |
| high | 15.36 |
| medium | 15.32 |
| neutral | 13.90 |

**Average MetricX-24 by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| HALLUCINATED_RULE | 16.38 |
| TRANSLATION_ATTEMPT | 15.54 |
| CORRECT_LINGUISTIC_ANALYSIS | 14.96 |
| correct_linguistic_analysis | 14.58 |
| NONE | 14.04 |
| neutral | 13.87 |

**Average MetricX-24 by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| none | 15.69 |

---

### COMET Metric

**Average COMET by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| High | 0.28 |
| high | 0.42 |
| medium | 0.42 |
| neutral | 0.52 |

**Average COMET by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| HALLUCINATED_RULE | 0.61 |
| neutral | 0.55 |
| CORRECT_LINGUISTIC_ANALYSIS | 0.48 |
| NONE | 0.41 |
| TRANSLATION_ATTEMPT | 0.41 |
| correct_linguistic_analysis | 0.27 |

**Average COMET by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| none | 0.40 |

---

## 8. Key Insights

- **Best performing trace type**: HALLUCINATED_RULE (BLEU: 9.47)
- **Worst performing trace type**: correct_linguistic_analysis (BLEU: 0.00)
- **Performance gap**: 9.47 BLEU points from worst to best

- **Most common trace type**: neutral (18 examples, 28.6%)
- **Average difficulty score**: 2.90/5.0

---

*Analysis generated from evaluations/comprehensive_cot_eval/Lithuanian_Turkish/gemma-3-1b-it/Lithuanian_to_Turkish_0_shot_seed_42_identity_None_0_0_0/phase2_annotations.jsonl*
