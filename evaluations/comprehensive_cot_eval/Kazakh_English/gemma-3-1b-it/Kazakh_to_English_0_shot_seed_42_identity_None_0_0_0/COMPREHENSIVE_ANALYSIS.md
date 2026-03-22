# Phase 2 Comprehensive Analysis

**Total Examples Analyzed**: 64

---

## 1. Difficulty Distribution

Distribution of translation difficulty scores (1=easiest, 5=hardest):

| Difficulty Score | Count | Percentage |
|-----------------|-------|------------|
| 1 | 6 | 9.4% |
| 2 | 6 | 9.4% |
| 3 | 43 | 67.2% |
| 4 | 6 | 9.4% |
| 5 | 3 | 4.7% |

## 2. Linguistic Phenomena Frequencies

Frequency of linguistic phenomena across 64 examples:

| Phenomenon | Count | Percentage |
|------------|-------|------------|
| long_distance_dependency | 55 | 85.9% |
| named_entities | 49 | 76.6% |
| complex_syntax | 25 | 39.1% |
| ambiguity | 1 | 1.6% |

## 3. Primary Trace Type Distribution

Distribution of reasoning trace types (n=64):

| Trace Type | Count | Percentage |
|------------|-------|------------|
| CORRECT_LINGUISTIC_ANALYSIS | 26 | 40.6% |
| NONE | 18 | 28.1% |
| TRANSLATION_ATTEMPT | 14 | 21.9% |
| neutral | 3 | 4.7% |
| REASONING | 2 | 3.1% |
| correct_linguistic_analysis | 1 | 1.6% |

## 4. Trace Usefulness Distribution

Distribution of trace usefulness ratings:

| Usefulness Level | Count | Percentage |
|------------------|-------|------------|
| High | 1 | 1.6% |
| Medium | 1 | 1.6% |
| helpful | 1 | 1.6% |
| high | 30 | 46.9% |
| medium | 19 | 29.7% |
| neutral | 12 | 18.8% |

## 5. Trace-Translation Overlap Distribution

Distribution of overlap between reasoning traces and translations:

| Overlap Level | Count | Percentage |
|---------------|-------|------------|
| none | 4 | 100.0% |

## 6. Cross-Tabulations

### 6.1 Difficulty × Trace Type

| Difficulty | CORRECT_LINGUISTIC_ANALYSIS | NONE | REASONING | TRANSLATION_ATTEMPT | correct_linguistic_analysis | neutral |
|---|---|---|---|---|---|---|
| 1 | 6 | 0 | 0 | 0 | 0 | 0 |
| 2 | 3 | 0 | 0 | 0 | 1 | 2 |
| 3 | 15 | 17 | 2 | 8 | 0 | 1 |
| 4 | 0 | 1 | 0 | 5 | 0 | 0 |
| 5 | 2 | 0 | 0 | 1 | 0 | 0 |

### 6.2 Trace Type × Usefulness

| Trace Type | High | Medium | helpful | high | medium | neutral |
|---|---|---|---|---|---|---|
| CORRECT_LINGUISTIC_ANALYSIS | 1 | 1 | 0 | 21 | 2 | 1 |
| NONE | 0 | 0 | 0 | 0 | 9 | 9 |
| REASONING | 0 | 0 | 0 | 2 | 0 | 0 |
| TRANSLATION_ATTEMPT | 0 | 0 | 0 | 7 | 7 | 0 |
| correct_linguistic_analysis | 0 | 0 | 1 | 0 | 0 | 0 |
| neutral | 0 | 0 | 0 | 0 | 1 | 2 |

## 7. Translation Quality Correlations

### COMET Metric

**Average COMET by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| High | 0.50 |
| Medium | 0.66 |
| helpful | 0.65 |
| high | 0.72 |
| medium | 0.71 |
| neutral | 0.67 |

**Average COMET by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| REASONING | 0.80 |
| neutral | 0.74 |
| NONE | 0.71 |
| TRANSLATION_ATTEMPT | 0.70 |
| CORRECT_LINGUISTIC_ANALYSIS | 0.69 |
| correct_linguistic_analysis | 0.65 |

**Average COMET by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| none | 0.71 |

---

### chrF++ Metric

**Average chrF++ by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| High | 12.68 |
| Medium | 24.85 |
| helpful | 35.11 |
| high | 32.58 |
| medium | 28.78 |
| neutral | 24.50 |

**Average chrF++ by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| REASONING | 41.17 |
| correct_linguistic_analysis | 35.11 |
| TRANSLATION_ATTEMPT | 30.19 |
| CORRECT_LINGUISTIC_ANALYSIS | 30.06 |
| neutral | 27.91 |
| NONE | 26.97 |

**Average chrF++ by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| none | 30.57 |

---

### BLEU Metric

**Average BLEU by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| High | 3.83 |
| Medium | 4.16 |
| helpful | 10.26 |
| high | 11.78 |
| medium | 6.57 |
| neutral | 7.16 |

**Average BLEU by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| REASONING | 20.80 |
| neutral | 11.87 |
| CORRECT_LINGUISTIC_ANALYSIS | 11.21 |
| correct_linguistic_analysis | 10.26 |
| NONE | 6.43 |
| TRANSLATION_ATTEMPT | 6.29 |

**Average BLEU by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| none | 8.67 |

---

### MetricX-24 Metric

**Average MetricX-24 by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| High | 16.00 |
| Medium | 15.06 |
| helpful | 12.69 |
| high | 10.78 |
| medium | 10.55 |
| neutral | 12.95 |

**Average MetricX-24 by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| correct_linguistic_analysis | 12.69 |
| NONE | 12.10 |
| CORRECT_LINGUISTIC_ANALYSIS | 11.53 |
| neutral | 11.00 |
| TRANSLATION_ATTEMPT | 10.30 |
| REASONING | 7.69 |

**Average MetricX-24 by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| none | 9.45 |

---

## 8. Key Insights

- **Best performing trace type**: REASONING (BLEU: 20.80)
- **Worst performing trace type**: TRANSLATION_ATTEMPT (BLEU: 6.29)
- **Performance gap**: 230.8% improvement from worst to best

- **Most common trace type**: CORRECT_LINGUISTIC_ANALYSIS (26 examples, 40.6%)
- **Average difficulty score**: 2.91/5.0

---

*Analysis generated from evaluations/comprehensive_cot_eval/Kazakh_English/gemma-3-1b-it/Kazakh_to_English_0_shot_seed_42_identity_None_0_0_0/phase2_annotations.jsonl*
