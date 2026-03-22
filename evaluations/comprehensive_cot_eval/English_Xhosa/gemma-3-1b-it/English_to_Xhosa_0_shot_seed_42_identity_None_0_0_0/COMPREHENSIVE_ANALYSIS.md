# Phase 2 Comprehensive Analysis

**Total Examples Analyzed**: 64

---

## 1. Difficulty Distribution

Distribution of translation difficulty scores (1=easiest, 5=hardest):

| Difficulty Score | Count | Percentage |
|-----------------|-------|------------|
| 2 | 5 | 9.6% |
| 3 | 46 | 88.5% |
| 4 | 1 | 1.9% |

## 2. Linguistic Phenomena Frequencies

Frequency of linguistic phenomena across 52 examples:

| Phenomenon | Count | Percentage |
|------------|-------|------------|
| long_distance_dependency | 51 | 98.1% |
| complex_syntax | 31 | 59.6% |
| named_entities | 27 | 51.9% |

## 3. Primary Trace Type Distribution

Distribution of reasoning trace types (n=52):

| Trace Type | Count | Percentage |
|------------|-------|------------|
| TRANSLATION_ATTEMPT | 35 | 67.3% |
| NONE | 7 | 13.5% |
| neutral | 5 | 9.6% |
| CORRECT_LINGUISTIC_ANALYSIS | 4 | 7.7% |
| correct_linguistic_analysis | 1 | 1.9% |

## 4. Trace Usefulness Distribution

Distribution of trace usefulness ratings:

| Usefulness Level | Count | Percentage |
|------------------|-------|------------|
| Medium | 1 | 1.9% |
| medium | 38 | 73.1% |
| neutral | 13 | 25.0% |

## 5. Trace-Translation Overlap Distribution

Distribution of overlap between reasoning traces and translations:

| Overlap Level | Count | Percentage |
|---------------|-------|------------|
| none | 20 | 100.0% |

## 6. Cross-Tabulations

### 6.1 Difficulty × Trace Type

| Difficulty | CORRECT_LINGUISTIC_ANALYSIS | NONE | TRANSLATION_ATTEMPT | correct_linguistic_analysis | neutral |
|---|---|---|---|---|---|
| 2 | 1 | 1 | 0 | 0 | 3 |
| 3 | 3 | 6 | 34 | 1 | 2 |
| 4 | 0 | 0 | 1 | 0 | 0 |

### 6.2 Trace Type × Usefulness

| Trace Type | Medium | medium | neutral |
|---|---|---|---|
| CORRECT_LINGUISTIC_ANALYSIS | 0 | 3 | 1 |
| NONE | 0 | 1 | 6 |
| TRANSLATION_ATTEMPT | 1 | 30 | 4 |
| correct_linguistic_analysis | 0 | 1 | 0 |
| neutral | 0 | 3 | 2 |

## 7. Translation Quality Correlations

### MetricX-24 Metric

**Average MetricX-24 by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| Medium | 15.50 |
| medium | 14.92 |
| neutral | 15.35 |

**Average MetricX-24 by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| correct_linguistic_analysis | 16.38 |
| neutral | 15.60 |
| NONE | 15.01 |
| TRANSLATION_ATTEMPT | 15.00 |
| CORRECT_LINGUISTIC_ANALYSIS | 14.45 |

**Average MetricX-24 by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| none | 14.84 |

---

### COMET Metric

**Average COMET by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| Medium | 0.37 |
| medium | 0.39 |
| neutral | 0.42 |

**Average COMET by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| NONE | 0.44 |
| neutral | 0.40 |
| TRANSLATION_ATTEMPT | 0.40 |
| CORRECT_LINGUISTIC_ANALYSIS | 0.37 |
| correct_linguistic_analysis | 0.34 |

**Average COMET by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| none | 0.40 |

---

### chrF++ Metric

**Average chrF++ by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| Medium | 8.28 |
| medium | 15.52 |
| neutral | 12.53 |

**Average chrF++ by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| CORRECT_LINGUISTIC_ANALYSIS | 16.93 |
| neutral | 15.73 |
| TRANSLATION_ATTEMPT | 14.65 |
| NONE | 13.50 |
| correct_linguistic_analysis | 7.06 |

**Average chrF++ by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| none | 16.87 |

---

### BLEU Metric

**Average BLEU by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| Medium | 0.85 |
| medium | 3.20 |
| neutral | 2.07 |

**Average BLEU by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| neutral | 4.21 |
| CORRECT_LINGUISTIC_ANALYSIS | 3.13 |
| TRANSLATION_ATTEMPT | 2.85 |
| NONE | 2.21 |
| correct_linguistic_analysis | 0.43 |

**Average BLEU by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| none | 3.56 |

---

## 8. Key Insights

- **Best performing trace type**: neutral (BLEU: 4.21)
- **Worst performing trace type**: correct_linguistic_analysis (BLEU: 0.43)
- **Performance gap**: 870.7% improvement from worst to best

- **Most common trace type**: TRANSLATION_ATTEMPT (35 examples, 67.3%)
- **Average difficulty score**: 2.92/5.0

---

*Analysis generated from evaluations/comprehensive_cot_eval/English_Xhosa/gemma-3-1b-it/English_to_Xhosa_0_shot_seed_42_identity_None_0_0_0/phase2_annotations.jsonl*
