# Phase 2 Comprehensive Analysis

**Total Examples Analyzed**: 64

---

## 1. Difficulty Distribution

Distribution of translation difficulty scores (1=easiest, 5=hardest):

| Difficulty Score | Count | Percentage |
|-----------------|-------|------------|
| 1 | 1 | 1.6% |
| 2 | 18 | 28.1% |
| 3 | 41 | 64.1% |
| 4 | 3 | 4.7% |
| 5 | 1 | 1.6% |

## 2. Linguistic Phenomena Frequencies

Frequency of linguistic phenomena across 64 examples:

| Phenomenon | Count | Percentage |
|------------|-------|------------|
| long_distance_dependency | 60 | 93.8% |
| named_entities | 53 | 82.8% |
| complex_syntax | 34 | 53.1% |

## 3. Primary Trace Type Distribution

Distribution of reasoning trace types (n=64):

| Trace Type | Count | Percentage |
|------------|-------|------------|
| TRANSLATION_ATTEMPT | 35 | 54.7% |
| NONE | 18 | 28.1% |
| neutral | 5 | 7.8% |
| CORRECT_LINGUISTIC_ANALYSIS | 4 | 6.2% |
| null | 1 | 1.6% |
| REPETITION | 1 | 1.6% |

## 4. Trace Usefulness Distribution

Distribution of trace usefulness ratings:

| Usefulness Level | Count | Percentage |
|------------------|-------|------------|
| high | 13 | 20.3% |
| medium | 35 | 54.7% |
| neutral | 16 | 25.0% |

## 5. Trace-Translation Overlap Distribution

Distribution of overlap between reasoning traces and translations:

| Overlap Level | Count | Percentage |
|---------------|-------|------------|
| low | 1 | 9.1% |
| none | 10 | 90.9% |

## 6. Cross-Tabulations

### 6.1 Difficulty × Trace Type

| Difficulty | CORRECT_LINGUISTIC_ANALYSIS | NONE | REPETITION | TRANSLATION_ATTEMPT | neutral | null |
|---|---|---|---|---|---|---|
| 1 | 0 | 0 | 0 | 0 | 0 | 1 |
| 2 | 0 | 10 | 0 | 3 | 5 | 0 |
| 3 | 4 | 8 | 1 | 28 | 0 | 0 |
| 4 | 0 | 0 | 0 | 3 | 0 | 0 |
| 5 | 0 | 0 | 0 | 1 | 0 | 0 |

### 6.2 Trace Type × Usefulness

| Trace Type | high | medium | neutral |
|---|---|---|---|
| CORRECT_LINGUISTIC_ANALYSIS | 3 | 1 | 0 |
| NONE | 0 | 7 | 11 |
| REPETITION | 0 | 1 | 0 |
| TRANSLATION_ATTEMPT | 10 | 25 | 0 |
| neutral | 0 | 1 | 4 |
| null | 0 | 0 | 1 |

## 7. Translation Quality Correlations

### MetricX-24 Metric

**Average MetricX-24 by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| high | 4.45 |
| medium | 5.20 |
| neutral | 3.34 |

**Average MetricX-24 by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| CORRECT_LINGUISTIC_ANALYSIS | 6.89 |
| neutral | 5.53 |
| TRANSLATION_ATTEMPT | 4.94 |
| null | 3.42 |
| NONE | 3.25 |
| REPETITION | 3.22 |

**Average MetricX-24 by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| low | 4.16 |
| none | 6.99 |

---

### COMET Metric

**Average COMET by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| high | 0.84 |
| medium | 0.83 |
| neutral | 0.86 |

**Average COMET by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| REPETITION | 0.89 |
| NONE | 0.87 |
| neutral | 0.84 |
| CORRECT_LINGUISTIC_ANALYSIS | 0.83 |
| null | 0.82 |
| TRANSLATION_ATTEMPT | 0.82 |

**Average COMET by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| low | 0.88 |
| none | 0.76 |

---

### BLEU Metric

**Average BLEU by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| high | 27.01 |
| medium | 25.07 |
| neutral | 27.11 |

**Average BLEU by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| REPETITION | 57.36 |
| neutral | 29.32 |
| NONE | 28.52 |
| TRANSLATION_ATTEMPT | 24.17 |
| CORRECT_LINGUISTIC_ANALYSIS | 21.86 |
| null | 11.77 |

**Average BLEU by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| low | 4.55 |
| none | 21.51 |

---

### chrF++ Metric

**Average chrF++ by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| high | 52.73 |
| medium | 49.58 |
| neutral | 50.99 |

**Average chrF++ by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| REPETITION | 74.47 |
| NONE | 53.36 |
| TRANSLATION_ATTEMPT | 49.56 |
| neutral | 47.85 |
| CORRECT_LINGUISTIC_ANALYSIS | 46.97 |
| null | 39.94 |

**Average chrF++ by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| low | 36.78 |
| none | 46.24 |

---

## 8. Key Insights

- **Best performing trace type**: REPETITION (BLEU: 57.36)
- **Worst performing trace type**: null (BLEU: 11.77)
- **Performance gap**: 387.5% improvement from worst to best

- **Most common trace type**: TRANSLATION_ATTEMPT (35 examples, 54.7%)
- **Average difficulty score**: 2.77/5.0

---

*Analysis generated from evaluations/guided_cot_eval/German_English/gemma-3-1b-it/German_to_English_0_shot_seed_42_identity_None_0_0_0/phase2_annotations.jsonl*
