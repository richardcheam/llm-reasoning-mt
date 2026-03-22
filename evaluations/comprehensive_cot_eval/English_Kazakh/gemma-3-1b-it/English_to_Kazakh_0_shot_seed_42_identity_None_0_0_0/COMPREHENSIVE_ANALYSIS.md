# Phase 2 Comprehensive Analysis

**Total Examples Analyzed**: 64

---

## 1. Difficulty Distribution

Distribution of translation difficulty scores (1=easiest, 5=hardest):

| Difficulty Score | Count | Percentage |
|-----------------|-------|------------|
| 1 | 3 | 4.7% |
| 2 | 10 | 15.6% |
| 3 | 46 | 71.9% |
| 4 | 4 | 6.2% |
| 5 | 1 | 1.6% |

## 2. Linguistic Phenomena Frequencies

Frequency of linguistic phenomena across 64 examples:

| Phenomenon | Count | Percentage |
|------------|-------|------------|
| long_distance_dependency | 59 | 92.2% |
| complex_syntax | 48 | 75.0% |
| named_entities | 42 | 65.6% |

## 3. Primary Trace Type Distribution

Distribution of reasoning trace types (n=64):

| Trace Type | Count | Percentage |
|------------|-------|------------|
| NONE | 23 | 35.9% |
| TRANSLATION_ATTEMPT | 14 | 21.9% |
| neutral | 11 | 17.2% |
| CORRECT_LINGUISTIC_ANALYSIS | 11 | 17.2% |
| correct_linguistic_analysis | 3 | 4.7% |
| REPETITION | 1 | 1.6% |
| VACUOUS_FILLER | 1 | 1.6% |

## 4. Trace Usefulness Distribution

Distribution of trace usefulness ratings:

| Usefulness Level | Count | Percentage |
|------------------|-------|------------|
| High | 1 | 1.6% |
| high | 4 | 6.2% |
| medium | 31 | 48.4% |
| neutral | 28 | 43.8% |

## 5. Trace-Translation Overlap Distribution

Distribution of overlap between reasoning traces and translations:

| Overlap Level | Count | Percentage |
|---------------|-------|------------|
| low | 1 | 5.6% |
| none | 17 | 94.4% |

## 6. Cross-Tabulations

### 6.1 Difficulty × Trace Type

| Difficulty | CORRECT_LINGUISTIC_ANALYSIS | NONE | REPETITION | TRANSLATION_ATTEMPT | VACUOUS_FILLER | correct_linguistic_analysis | neutral |
|---|---|---|---|---|---|---|---|
| 1 | 0 | 1 | 0 | 0 | 0 | 0 | 2 |
| 2 | 0 | 2 | 0 | 0 | 1 | 0 | 7 |
| 3 | 10 | 20 | 1 | 10 | 0 | 3 | 2 |
| 4 | 1 | 0 | 0 | 3 | 0 | 0 | 0 |
| 5 | 0 | 0 | 0 | 1 | 0 | 0 | 0 |

### 6.2 Trace Type × Usefulness

| Trace Type | High | high | medium | neutral |
|---|---|---|---|---|
| CORRECT_LINGUISTIC_ANALYSIS | 0 | 2 | 8 | 1 |
| NONE | 0 | 1 | 4 | 18 |
| REPETITION | 0 | 0 | 1 | 0 |
| TRANSLATION_ATTEMPT | 1 | 1 | 12 | 0 |
| VACUOUS_FILLER | 0 | 0 | 0 | 1 |
| correct_linguistic_analysis | 0 | 0 | 3 | 0 |
| neutral | 0 | 0 | 3 | 8 |

## 7. Translation Quality Correlations

### BLEU Metric

**Average BLEU by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| High | 4.65 |
| high | 5.92 |
| medium | 3.11 |
| neutral | 4.03 |

**Average BLEU by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| VACUOUS_FILLER | 6.24 |
| NONE | 4.71 |
| neutral | 4.38 |
| CORRECT_LINGUISTIC_ANALYSIS | 3.13 |
| TRANSLATION_ATTEMPT | 2.58 |
| correct_linguistic_analysis | 1.39 |
| REPETITION | 0.00 |

**Average BLEU by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| low | 1.16 |
| none | 2.45 |

---

### COMET Metric

**Average COMET by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| High | 0.82 |
| high | 0.75 |
| medium | 0.60 |
| neutral | 0.68 |

**Average COMET by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| NONE | 0.70 |
| neutral | 0.67 |
| VACUOUS_FILLER | 0.65 |
| CORRECT_LINGUISTIC_ANALYSIS | 0.65 |
| TRANSLATION_ATTEMPT | 0.57 |
| correct_linguistic_analysis | 0.52 |
| REPETITION | 0.48 |

**Average COMET by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| low | 0.77 |
| none | 0.56 |

---

### MetricX-24 Metric

**Average MetricX-24 by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| High | 1.84 |
| high | 6.30 |
| medium | 8.60 |
| neutral | 6.85 |

**Average MetricX-24 by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| REPETITION | 15.06 |
| correct_linguistic_analysis | 10.74 |
| TRANSLATION_ATTEMPT | 8.72 |
| neutral | 8.19 |
| VACUOUS_FILLER | 8.00 |
| CORRECT_LINGUISTIC_ANALYSIS | 7.07 |
| NONE | 6.10 |

**Average MetricX-24 by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| low | 5.69 |
| none | 8.73 |

---

### chrF++ Metric

**Average chrF++ by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| High | 15.54 |
| high | 14.67 |
| medium | 12.87 |
| neutral | 14.09 |

**Average chrF++ by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| VACUOUS_FILLER | 21.38 |
| neutral | 15.18 |
| CORRECT_LINGUISTIC_ANALYSIS | 14.42 |
| NONE | 14.15 |
| correct_linguistic_analysis | 13.71 |
| TRANSLATION_ATTEMPT | 10.86 |
| REPETITION | 2.25 |

**Average chrF++ by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| low | 9.78 |
| none | 10.79 |

---

## 8. Key Insights

- **Best performing trace type**: VACUOUS_FILLER (BLEU: 6.24)
- **Worst performing trace type**: REPETITION (BLEU: 0.00)
- **Performance gap**: 4954471.4% improvement from worst to best

- **Most common trace type**: NONE (23 examples, 35.9%)
- **Average difficulty score**: 2.84/5.0

---

*Analysis generated from evaluations/comprehensive_cot_eval/English_Kazakh/gemma-3-1b-it/English_to_Kazakh_0_shot_seed_42_identity_None_0_0_0/phase2_annotations.jsonl*
