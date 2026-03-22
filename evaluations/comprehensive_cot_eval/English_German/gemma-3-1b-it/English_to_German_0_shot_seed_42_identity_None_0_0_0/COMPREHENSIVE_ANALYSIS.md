# Phase 2 Comprehensive Analysis

**Total Examples Analyzed**: 64

---

## 1. Difficulty Distribution

Distribution of translation difficulty scores (1=easiest, 5=hardest):

| Difficulty Score | Count | Percentage |
|-----------------|-------|------------|
| 1 | 5 | 7.8% |
| 2 | 21 | 32.8% |
| 3 | 33 | 51.6% |
| 4 | 3 | 4.7% |
| 5 | 2 | 3.1% |

## 2. Linguistic Phenomena Frequencies

Frequency of linguistic phenomena across 64 examples:

| Phenomenon | Count | Percentage |
|------------|-------|------------|
| long_distance_dependency | 54 | 84.4% |
| complex_syntax | 38 | 59.4% |
| named_entities | 34 | 53.1% |

## 3. Primary Trace Type Distribution

Distribution of reasoning trace types (n=64):

| Trace Type | Count | Percentage |
|------------|-------|------------|
| TRANSLATION_ATTEMPT | 20 | 31.2% |
| NONE | 18 | 28.1% |
| neutral | 17 | 26.6% |
| CORRECT_LINGUISTIC_ANALYSIS | 4 | 6.2% |
| null | 3 | 4.7% |
| VACUOUS_FILLER | 1 | 1.6% |
| correct_linguistic_analysis | 1 | 1.6% |

## 4. Trace Usefulness Distribution

Distribution of trace usefulness ratings:

| Usefulness Level | Count | Percentage |
|------------------|-------|------------|
| Easy | 1 | 1.6% |
| high | 4 | 6.2% |
| medium | 26 | 40.6% |
| neutral | 33 | 51.6% |

## 5. Trace-Translation Overlap Distribution

Distribution of overlap between reasoning traces and translations:

| Overlap Level | Count | Percentage |
|---------------|-------|------------|
| none | 20 | 100.0% |

## 6. Cross-Tabulations

### 6.1 Difficulty × Trace Type

| Difficulty | CORRECT_LINGUISTIC_ANALYSIS | NONE | TRANSLATION_ATTEMPT | VACUOUS_FILLER | correct_linguistic_analysis | neutral | null |
|---|---|---|---|---|---|---|---|
| 1 | 0 | 1 | 0 | 0 | 0 | 1 | 3 |
| 2 | 1 | 6 | 0 | 0 | 1 | 13 | 0 |
| 3 | 1 | 11 | 17 | 1 | 0 | 3 | 0 |
| 4 | 1 | 0 | 2 | 0 | 0 | 0 | 0 |
| 5 | 1 | 0 | 1 | 0 | 0 | 0 | 0 |

### 6.2 Trace Type × Usefulness

| Trace Type | Easy | high | medium | neutral |
|---|---|---|---|---|
| CORRECT_LINGUISTIC_ANALYSIS | 0 | 3 | 1 | 0 |
| NONE | 1 | 0 | 2 | 15 |
| TRANSLATION_ATTEMPT | 0 | 1 | 19 | 0 |
| VACUOUS_FILLER | 0 | 0 | 0 | 1 |
| correct_linguistic_analysis | 0 | 0 | 1 | 0 |
| neutral | 0 | 0 | 3 | 14 |
| null | 0 | 0 | 0 | 3 |

## 7. Translation Quality Correlations

### COMET Metric

**Average COMET by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| Easy | 0.86 |
| high | 0.82 |
| medium | 0.79 |
| neutral | 0.80 |

**Average COMET by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| correct_linguistic_analysis | 0.93 |
| NONE | 0.87 |
| CORRECT_LINGUISTIC_ANALYSIS | 0.81 |
| neutral | 0.80 |
| TRANSLATION_ATTEMPT | 0.77 |
| VACUOUS_FILLER | 0.76 |
| null | 0.56 |

**Average COMET by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| none | 0.78 |

---

### BLEU Metric

**Average BLEU by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| Easy | 29.05 |
| high | 18.12 |
| medium | 18.49 |
| neutral | 21.89 |

**Average BLEU by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| correct_linguistic_analysis | 60.60 |
| NONE | 23.91 |
| neutral | 23.56 |
| CORRECT_LINGUISTIC_ANALYSIS | 19.91 |
| TRANSLATION_ATTEMPT | 15.65 |
| null | 6.08 |
| VACUOUS_FILLER | 2.33 |

**Average BLEU by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| none | 17.00 |

---

### MetricX-24 Metric

**Average MetricX-24 by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| Easy | 1.59 |
| high | 4.37 |
| medium | 3.66 |
| neutral | 2.79 |

**Average MetricX-24 by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| null | 7.17 |
| CORRECT_LINGUISTIC_ANALYSIS | 4.48 |
| TRANSLATION_ATTEMPT | 4.04 |
| VACUOUS_FILLER | 2.72 |
| neutral | 2.65 |
| NONE | 2.06 |
| correct_linguistic_analysis | 1.23 |

**Average MetricX-24 by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| none | 3.22 |

---

### chrF++ Metric

**Average chrF++ by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| Easy | 50.10 |
| high | 45.51 |
| medium | 43.10 |
| neutral | 43.60 |

**Average chrF++ by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| correct_linguistic_analysis | 73.18 |
| neutral | 49.47 |
| CORRECT_LINGUISTIC_ANALYSIS | 46.52 |
| NONE | 42.44 |
| TRANSLATION_ATTEMPT | 40.65 |
| VACUOUS_FILLER | 31.76 |
| null | 27.55 |

**Average chrF++ by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| none | 42.23 |

---

## 8. Key Insights

- **Best performing trace type**: correct_linguistic_analysis (BLEU: 60.60)
- **Worst performing trace type**: VACUOUS_FILLER (BLEU: 2.33)
- **Performance gap**: 2501.7% improvement from worst to best

- **Most common trace type**: TRANSLATION_ATTEMPT (20 examples, 31.2%)
- **Average difficulty score**: 2.62/5.0

---

*Analysis generated from evaluations/comprehensive_cot_eval/English_German/gemma-3-1b-it/English_to_German_0_shot_seed_42_identity_None_0_0_0/phase2_annotations.jsonl*
