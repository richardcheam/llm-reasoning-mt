# Phase 2 Comprehensive Analysis

**Total Examples Analyzed**: 64

---

## 1. Difficulty Distribution

Distribution of translation difficulty scores (1=easiest, 5=hardest):

| Difficulty Score | Count | Percentage |
|-----------------|-------|------------|
| 2 | 2 | 3.6% |
| 3 | 45 | 80.4% |
| 4 | 9 | 16.1% |

## 2. Linguistic Phenomena Frequencies

Frequency of linguistic phenomena across 56 examples:

| Phenomenon | Count | Percentage |
|------------|-------|------------|
| long_distance_dependency | 55 | 98.2% |
| named_entities | 40 | 71.4% |
| complex_syntax | 37 | 66.1% |

## 3. Primary Trace Type Distribution

Distribution of reasoning trace types (n=56):

| Trace Type | Count | Percentage |
|------------|-------|------------|
| TRANSLATION_ATTEMPT | 28 | 50.0% |
| CORRECT_LINGUISTIC_ANALYSIS | 18 | 32.1% |
| NONE | 7 | 12.5% |
| correct_linguistic_analysis | 2 | 3.6% |
| REPETITION | 1 | 1.8% |

## 4. Trace Usefulness Distribution

Distribution of trace usefulness ratings:

| Usefulness Level | Count | Percentage |
|------------------|-------|------------|
| Medium | 3 | 5.4% |
| high | 4 | 7.1% |
| medium | 43 | 76.8% |
| neutral | 6 | 10.7% |

## 5. Trace-Translation Overlap Distribution

Distribution of overlap between reasoning traces and translations:

| Overlap Level | Count | Percentage |
|---------------|-------|------------|
| none | 28 | 100.0% |

## 6. Cross-Tabulations

### 6.1 Difficulty × Trace Type

| Difficulty | CORRECT_LINGUISTIC_ANALYSIS | NONE | REPETITION | TRANSLATION_ATTEMPT | correct_linguistic_analysis |
|---|---|---|---|---|---|
| 2 | 1 | 1 | 0 | 0 | 0 |
| 3 | 14 | 6 | 1 | 23 | 1 |
| 4 | 3 | 0 | 0 | 5 | 1 |

### 6.2 Trace Type × Usefulness

| Trace Type | Medium | high | medium | neutral |
|---|---|---|---|---|
| CORRECT_LINGUISTIC_ANALYSIS | 1 | 4 | 12 | 1 |
| NONE | 0 | 0 | 2 | 5 |
| REPETITION | 0 | 0 | 1 | 0 |
| TRANSLATION_ATTEMPT | 2 | 0 | 26 | 0 |
| correct_linguistic_analysis | 0 | 0 | 2 | 0 |

## 7. Translation Quality Correlations

### MetricX-24 Metric

**Average MetricX-24 by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| Medium | 17.04 |
| high | 17.20 |
| medium | 15.56 |
| neutral | 13.14 |

**Average MetricX-24 by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| CORRECT_LINGUISTIC_ANALYSIS | 16.59 |
| TRANSLATION_ATTEMPT | 15.48 |
| correct_linguistic_analysis | 14.44 |
| NONE | 13.43 |
| REPETITION | 13.12 |

**Average MetricX-24 by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| none | 16.15 |

---

### BLEU Metric

**Average BLEU by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| Medium | 0.93 |
| high | 0.97 |
| medium | 2.05 |
| neutral | 3.10 |

**Average BLEU by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| NONE | 2.88 |
| TRANSLATION_ATTEMPT | 2.65 |
| REPETITION | 0.94 |
| CORRECT_LINGUISTIC_ANALYSIS | 0.91 |
| correct_linguistic_analysis | 0.90 |

**Average BLEU by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| none | 1.25 |

---

### COMET Metric

**Average COMET by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| Medium | 0.35 |
| high | 0.31 |
| medium | 0.37 |
| neutral | 0.46 |

**Average COMET by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| NONE | 0.43 |
| correct_linguistic_analysis | 0.41 |
| REPETITION | 0.39 |
| TRANSLATION_ATTEMPT | 0.38 |
| CORRECT_LINGUISTIC_ANALYSIS | 0.33 |

**Average COMET by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| none | 0.35 |

---

### chrF++ Metric

**Average chrF++ by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| Medium | 4.60 |
| high | 5.77 |
| medium | 7.57 |
| neutral | 8.61 |

**Average chrF++ by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| REPETITION | 15.60 |
| TRANSLATION_ATTEMPT | 9.04 |
| NONE | 8.94 |
| correct_linguistic_analysis | 5.25 |
| CORRECT_LINGUISTIC_ANALYSIS | 4.01 |

**Average chrF++ by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| none | 5.00 |

---

## 8. Key Insights

- **Best performing trace type**: NONE (BLEU: 2.88)
- **Worst performing trace type**: correct_linguistic_analysis (BLEU: 0.90)
- **Performance gap**: 221.2% improvement from worst to best

- **Most common trace type**: TRANSLATION_ATTEMPT (28 examples, 50.0%)
- **Average difficulty score**: 3.12/5.0

---

*Analysis generated from evaluations/comprehensive_cot_eval/Kazakh_Xhosa/gemma-3-1b-it/Kazakh_to_Xhosa_0_shot_seed_42_identity_None_0_0_0/phase2_annotations.jsonl*
