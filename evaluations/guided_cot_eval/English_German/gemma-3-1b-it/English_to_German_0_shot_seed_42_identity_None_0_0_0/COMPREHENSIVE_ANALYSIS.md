# Phase 2 Comprehensive Analysis

**Total Examples Analyzed**: 64

---

## 1. Difficulty Distribution

Distribution of translation difficulty scores (1=easiest, 5=hardest):

| Difficulty Score | Count | Percentage |
|-----------------|-------|------------|
| 2 | 2 | 3.4% |
| 3 | 53 | 89.8% |
| 4 | 4 | 6.8% |

## 2. Linguistic Phenomena Frequencies

Frequency of linguistic phenomena across 59 examples:

| Phenomenon | Count | Percentage |
|------------|-------|------------|
| long_distance_dependency | 59 | 100.0% |
| complex_syntax | 52 | 88.1% |
| named_entities | 43 | 72.9% |
| ambiguity | 3 | 5.1% |
| idiom | 3 | 5.1% |
| figurative_language | 3 | 5.1% |

## 3. Primary Trace Type Distribution

Distribution of reasoning trace types (n=59):

| Trace Type | Count | Percentage |
|------------|-------|------------|
| TRANSLATION_ATTEMPT | 37 | 62.7% |
| NONE | 9 | 15.3% |
| CORRECT_LINGUISTIC_ANALYSIS | 7 | 11.9% |
| neutral | 6 | 10.2% |

## 4. Trace Usefulness Distribution

Distribution of trace usefulness ratings:

| Usefulness Level | Count | Percentage |
|------------------|-------|------------|
| 1 | 2 | 3.4% |
| 3 | 1 | 1.7% |
| high | 3 | 5.1% |
| medium | 49 | 83.1% |
| neutral | 4 | 6.8% |

## 5. Trace-Translation Overlap Distribution

Distribution of overlap between reasoning traces and translations:

| Overlap Level | Count | Percentage |
|---------------|-------|------------|
| 0 | 3 | 6.7% |
| none | 42 | 93.3% |

## 6. Cross-Tabulations

### 6.1 Difficulty × Trace Type

| Difficulty | CORRECT_LINGUISTIC_ANALYSIS | NONE | TRANSLATION_ATTEMPT | neutral |
|---|---|---|---|---|
| 2 | 0 | 0 | 0 | 2 |
| 3 | 6 | 9 | 34 | 4 |
| 4 | 1 | 0 | 3 | 0 |

### 6.2 Trace Type × Usefulness

| Trace Type | 1 | 3 | high | medium | neutral |
|---|---|---|---|---|---|
| CORRECT_LINGUISTIC_ANALYSIS | 0 | 0 | 2 | 5 | 0 |
| NONE | 2 | 1 | 0 | 4 | 2 |
| TRANSLATION_ATTEMPT | 0 | 0 | 1 | 35 | 1 |
| neutral | 0 | 0 | 0 | 5 | 1 |

## 7. Translation Quality Correlations

### chrF++ Metric

**Average chrF++ by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 1 | 50.20 |
| 3 | 50.90 |
| high | 47.00 |
| medium | 43.87 |
| neutral | 51.09 |

**Average chrF++ by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| CORRECT_LINGUISTIC_ANALYSIS | 49.73 |
| NONE | 48.76 |
| neutral | 44.33 |
| TRANSLATION_ATTEMPT | 43.07 |

**Average chrF++ by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| 0 | 50.43 |
| none | 43.48 |

---

### MetricX-24 Metric

**Average MetricX-24 by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 1 | 1.87 |
| 3 | 2.94 |
| high | 2.47 |
| medium | 3.15 |
| neutral | 2.22 |

**Average MetricX-24 by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| neutral | 4.36 |
| TRANSLATION_ATTEMPT | 3.21 |
| NONE | 2.16 |
| CORRECT_LINGUISTIC_ANALYSIS | 1.85 |

**Average MetricX-24 by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| 0 | 2.23 |
| none | 3.26 |

---

### BLEU Metric

**Average BLEU by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 1 | 21.01 |
| 3 | 21.31 |
| high | 21.52 |
| medium | 21.29 |
| neutral | 28.95 |

**Average BLEU by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| NONE | 27.12 |
| CORRECT_LINGUISTIC_ANALYSIS | 26.26 |
| neutral | 21.45 |
| TRANSLATION_ATTEMPT | 19.74 |

**Average BLEU by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| 0 | 21.11 |
| none | 20.39 |

---

### COMET Metric

**Average COMET by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 1 | 0.78 |
| 3 | 0.71 |
| high | 0.78 |
| medium | 0.80 |
| neutral | 0.82 |

**Average COMET by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| CORRECT_LINGUISTIC_ANALYSIS | 0.83 |
| NONE | 0.80 |
| TRANSLATION_ATTEMPT | 0.80 |
| neutral | 0.76 |

**Average COMET by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| 0 | 0.75 |
| none | 0.79 |

---

## 8. Key Insights

- **Best performing trace type**: NONE (BLEU: 27.12)
- **Worst performing trace type**: TRANSLATION_ATTEMPT (BLEU: 19.74)
- **Performance gap**: 37.4% improvement from worst to best

- **Most common trace type**: TRANSLATION_ATTEMPT (37 examples, 62.7%)
- **Average difficulty score**: 3.03/5.0

---

*Analysis generated from evaluations/guided_cot_eval/English_German/gemma-3-1b-it/English_to_German_0_shot_seed_42_identity_None_0_0_0/phase2_annotations.jsonl*
