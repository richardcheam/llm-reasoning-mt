# Phase 2 Comprehensive Analysis

**Total Examples Analyzed**: 64

---

## 1. Difficulty Distribution

Distribution of translation difficulty scores (1=easiest, 5=hardest):

| Difficulty Score | Count | Percentage |
|-----------------|-------|------------|
| 2 | 5 | 8.8% |
| 3 | 46 | 80.7% |
| 4 | 4 | 7.0% |
| 5 | 2 | 3.5% |

## 2. Linguistic Phenomena Frequencies

Frequency of linguistic phenomena across 57 examples:

| Phenomenon | Count | Percentage |
|------------|-------|------------|
| long_distance_dependency | 55 | 96.5% |
| complex_syntax | 45 | 78.9% |
| named_entities | 35 | 61.4% |

## 3. Primary Trace Type Distribution

Distribution of reasoning trace types (n=57):

| Trace Type | Count | Percentage |
|------------|-------|------------|
| TRANSLATION_ATTEMPT | 25 | 43.9% |
| CORRECT_LINGUISTIC_ANALYSIS | 22 | 38.6% |
| NONE | 5 | 8.8% |
| neutral | 3 | 5.3% |
| correct_linguistic_analysis | 2 | 3.5% |

## 4. Trace Usefulness Distribution

Distribution of trace usefulness ratings:

| Usefulness Level | Count | Percentage |
|------------------|-------|------------|
| Medium | 2 | 3.5% |
| high | 5 | 8.8% |
| medium | 42 | 73.7% |
| neutral | 8 | 14.0% |

## 5. Trace-Translation Overlap Distribution

Distribution of overlap between reasoning traces and translations:

| Overlap Level | Count | Percentage |
|---------------|-------|------------|
| none | 38 | 100.0% |

## 6. Cross-Tabulations

### 6.1 Difficulty × Trace Type

| Difficulty | CORRECT_LINGUISTIC_ANALYSIS | NONE | TRANSLATION_ATTEMPT | correct_linguistic_analysis | neutral |
|---|---|---|---|---|---|
| 2 | 0 | 3 | 0 | 0 | 2 |
| 3 | 18 | 2 | 23 | 2 | 1 |
| 4 | 2 | 0 | 2 | 0 | 0 |
| 5 | 2 | 0 | 0 | 0 | 0 |

### 6.2 Trace Type × Usefulness

| Trace Type | Medium | high | medium | neutral |
|---|---|---|---|---|
| CORRECT_LINGUISTIC_ANALYSIS | 0 | 5 | 17 | 0 |
| NONE | 0 | 0 | 0 | 5 |
| TRANSLATION_ATTEMPT | 2 | 0 | 22 | 1 |
| correct_linguistic_analysis | 0 | 0 | 2 | 0 |
| neutral | 0 | 0 | 1 | 2 |

## 7. Translation Quality Correlations

### COMET Metric

**Average COMET by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| Medium | 0.42 |
| high | 0.43 |
| medium | 0.40 |
| neutral | 0.46 |

**Average COMET by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| NONE | 0.50 |
| correct_linguistic_analysis | 0.48 |
| neutral | 0.42 |
| CORRECT_LINGUISTIC_ANALYSIS | 0.41 |
| TRANSLATION_ATTEMPT | 0.39 |

**Average COMET by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| none | 0.40 |

---

### MetricX-24 Metric

**Average MetricX-24 by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| Medium | 16.44 |
| high | 17.68 |
| medium | 16.09 |
| neutral | 16.84 |

**Average MetricX-24 by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| correct_linguistic_analysis | 18.56 |
| NONE | 16.44 |
| TRANSLATION_ATTEMPT | 16.33 |
| neutral | 16.21 |
| CORRECT_LINGUISTIC_ANALYSIS | 16.16 |

**Average MetricX-24 by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| none | 16.29 |

---

### chrF++ Metric

**Average chrF++ by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| Medium | 4.66 |
| high | 9.70 |
| medium | 9.16 |
| neutral | 8.40 |

**Average chrF++ by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| CORRECT_LINGUISTIC_ANALYSIS | 9.34 |
| TRANSLATION_ATTEMPT | 9.06 |
| neutral | 8.85 |
| NONE | 7.85 |
| correct_linguistic_analysis | 5.95 |

**Average chrF++ by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| none | 8.79 |

---

### BLEU Metric

**Average BLEU by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| Medium | 1.12 |
| high | 1.55 |
| medium | 1.89 |
| neutral | 3.51 |

**Average BLEU by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| NONE | 4.89 |
| CORRECT_LINGUISTIC_ANALYSIS | 2.22 |
| TRANSLATION_ATTEMPT | 1.55 |
| neutral | 1.21 |
| correct_linguistic_analysis | 0.71 |

**Average BLEU by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| none | 1.65 |

---

## 8. Key Insights

- **Best performing trace type**: NONE (BLEU: 4.89)
- **Worst performing trace type**: correct_linguistic_analysis (BLEU: 0.71)
- **Performance gap**: 589.5% improvement from worst to best

- **Most common trace type**: TRANSLATION_ATTEMPT (25 examples, 43.9%)
- **Average difficulty score**: 3.05/5.0

---

*Analysis generated from evaluations/comprehensive_cot_eval/Xhosa_Kazakh/gemma-3-1b-it/Xhosa_to_Kazakh_0_shot_seed_42_identity_None_0_0_0/phase2_annotations.jsonl*
