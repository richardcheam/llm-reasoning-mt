# Phase 2 Comprehensive Analysis

**Total Examples Analyzed**: 64

---

## 1. Difficulty Distribution

Distribution of translation difficulty scores (1=easiest, 5=hardest):

| Difficulty Score | Count | Percentage |
|-----------------|-------|------------|
| 1 | 4 | 6.2% |
| 2 | 16 | 25.0% |
| 3 | 39 | 60.9% |
| 4 | 4 | 6.2% |
| 5 | 1 | 1.6% |

## 2. Linguistic Phenomena Frequencies

Frequency of linguistic phenomena across 64 examples:

| Phenomenon | Count | Percentage |
|------------|-------|------------|
| long_distance_dependency | 56 | 87.5% |
| named_entities | 40 | 62.5% |
| complex_syntax | 38 | 59.4% |

## 3. Primary Trace Type Distribution

Distribution of reasoning trace types (n=64):

| Trace Type | Count | Percentage |
|------------|-------|------------|
| NONE | 25 | 39.1% |
| TRANSLATION_ATTEMPT | 20 | 31.2% |
| neutral | 13 | 20.3% |
| correct_linguistic_analysis | 4 | 6.2% |
| REPETITION | 1 | 1.6% |
| CORRECT_LINGUISTIC_ANALYSIS | 1 | 1.6% |

## 4. Trace Usefulness Distribution

Distribution of trace usefulness ratings:

| Usefulness Level | Count | Percentage |
|------------------|-------|------------|
| Neutral | 1 | 1.6% |
| helpful | 1 | 1.6% |
| high | 2 | 3.1% |
| medium | 24 | 37.5% |
| neutral | 36 | 56.2% |

## 5. Trace-Translation Overlap Distribution

Distribution of overlap between reasoning traces and translations:

| Overlap Level | Count | Percentage |
|---------------|-------|------------|
| none | 15 | 100.0% |

## 6. Cross-Tabulations

### 6.1 Difficulty × Trace Type

| Difficulty | CORRECT_LINGUISTIC_ANALYSIS | NONE | REPETITION | TRANSLATION_ATTEMPT | correct_linguistic_analysis | neutral |
|---|---|---|---|---|---|---|
| 1 | 0 | 3 | 0 | 0 | 0 | 1 |
| 2 | 0 | 5 | 0 | 1 | 0 | 10 |
| 3 | 1 | 17 | 1 | 15 | 3 | 2 |
| 4 | 0 | 0 | 0 | 3 | 1 | 0 |
| 5 | 0 | 0 | 0 | 1 | 0 | 0 |

### 6.2 Trace Type × Usefulness

| Trace Type | Neutral | helpful | high | medium | neutral |
|---|---|---|---|---|---|
| CORRECT_LINGUISTIC_ANALYSIS | 0 | 0 | 0 | 1 | 0 |
| NONE | 1 | 1 | 0 | 1 | 22 |
| REPETITION | 0 | 0 | 0 | 0 | 1 |
| TRANSLATION_ATTEMPT | 0 | 0 | 1 | 18 | 1 |
| correct_linguistic_analysis | 0 | 0 | 1 | 3 | 0 |
| neutral | 0 | 0 | 0 | 1 | 12 |

## 7. Translation Quality Correlations

### COMET Metric

**Average COMET by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| Neutral | 0.79 |
| helpful | 0.94 |
| high | 0.85 |
| medium | 0.80 |
| neutral | 0.84 |

**Average COMET by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| REPETITION | 0.91 |
| NONE | 0.85 |
| correct_linguistic_analysis | 0.82 |
| neutral | 0.82 |
| TRANSLATION_ATTEMPT | 0.79 |
| CORRECT_LINGUISTIC_ANALYSIS | 0.72 |

**Average COMET by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| none | 0.81 |

---

### BLEU Metric

**Average BLEU by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| Neutral | 21.87 |
| helpful | 40.31 |
| high | 29.05 |
| medium | 28.23 |
| neutral | 32.23 |

**Average BLEU by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| REPETITION | 55.41 |
| NONE | 36.07 |
| correct_linguistic_analysis | 31.68 |
| TRANSLATION_ATTEMPT | 28.56 |
| neutral | 22.71 |
| CORRECT_LINGUISTIC_ANALYSIS | 7.77 |

**Average BLEU by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| none | 28.29 |

---

### chrF++ Metric

**Average chrF++ by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| Neutral | 47.86 |
| helpful | 59.09 |
| high | 45.57 |
| medium | 50.06 |
| neutral | 52.24 |

**Average chrF++ by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| REPETITION | 80.12 |
| NONE | 56.04 |
| correct_linguistic_analysis | 53.35 |
| TRANSLATION_ATTEMPT | 49.53 |
| neutral | 43.48 |
| CORRECT_LINGUISTIC_ANALYSIS | 30.10 |

**Average chrF++ by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| none | 49.78 |

---

### MetricX-24 Metric

**Average MetricX-24 by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| Neutral | 3.69 |
| helpful | 1.23 |
| high | 4.01 |
| medium | 3.98 |
| neutral | 3.15 |

**Average MetricX-24 by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| CORRECT_LINGUISTIC_ANALYSIS | 7.03 |
| TRANSLATION_ATTEMPT | 4.20 |
| correct_linguistic_analysis | 3.66 |
| NONE | 3.05 |
| neutral | 2.94 |
| REPETITION | 1.70 |

**Average MetricX-24 by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| none | 3.78 |

---

## 8. Key Insights

- **Best performing trace type**: REPETITION (BLEU: 55.41)
- **Worst performing trace type**: CORRECT_LINGUISTIC_ANALYSIS (BLEU: 7.77)
- **Performance gap**: 613.0% improvement from worst to best

- **Most common trace type**: NONE (25 examples, 39.1%)
- **Average difficulty score**: 2.72/5.0

---

*Analysis generated from evaluations/comprehensive_cot_eval/English_French/gemma-3-1b-it/English_to_French_0_shot_seed_42_identity_None_0_0_0/phase2_annotations.jsonl*
