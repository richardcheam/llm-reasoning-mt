# Phase 2 Comprehensive Analysis

**Total Examples Analyzed**: 64

---

## 1. Difficulty Distribution

Distribution of translation difficulty scores (1=easiest, 5=hardest):

| Difficulty Score | Count | Percentage |
|-----------------|-------|------------|
| 1 | 2 | 3.1% |
| 2 | 8 | 12.5% |
| 3 | 44 | 68.8% |
| 4 | 8 | 12.5% |
| 5 | 2 | 3.1% |

## 2. Linguistic Phenomena Frequencies

Frequency of linguistic phenomena across 64 examples:

| Phenomenon | Count | Percentage |
|------------|-------|------------|
| long_distance_dependency | 59 | 92.2% |
| named_entities | 41 | 64.1% |
| complex_syntax | 37 | 57.8% |
| idiom | 1 | 1.6% |

## 3. Primary Trace Type Distribution

Distribution of reasoning trace types (n=64):

| Trace Type | Count | Percentage |
|------------|-------|------------|
| TRANSLATION_ATTEMPT | 28 | 43.8% |
| CORRECT_LINGUISTIC_ANALYSIS | 16 | 25.0% |
| NONE | 12 | 18.8% |
| neutral | 4 | 6.2% |
| null | 1 | 1.6% |
| correction | 1 | 1.6% |
| REASONING | 1 | 1.6% |
| REPETITION | 1 | 1.6% |

## 4. Trace Usefulness Distribution

Distribution of trace usefulness ratings:

| Usefulness Level | Count | Percentage |
|------------------|-------|------------|
| High | 1 | 1.6% |
| Medium | 4 | 6.2% |
| high | 5 | 7.8% |
| medium | 37 | 57.8% |
| neutral | 17 | 26.6% |

## 5. Trace-Translation Overlap Distribution

Distribution of overlap between reasoning traces and translations:

| Overlap Level | Count | Percentage |
|---------------|-------|------------|
| none | 24 | 100.0% |

## 6. Cross-Tabulations

### 6.1 Difficulty × Trace Type

| Difficulty | CORRECT_LINGUISTIC_ANALYSIS | NONE | REASONING | REPETITION | TRANSLATION_ATTEMPT | correction | neutral | null |
|---|---|---|---|---|---|---|---|---|
| 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| 2 | 2 | 2 | 0 | 0 | 2 | 0 | 2 | 0 |
| 3 | 10 | 9 | 1 | 1 | 20 | 1 | 2 | 0 |
| 4 | 1 | 1 | 0 | 0 | 6 | 0 | 0 | 0 |
| 5 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

### 6.2 Trace Type × Usefulness

| Trace Type | High | Medium | high | medium | neutral |
|---|---|---|---|---|---|
| CORRECT_LINGUISTIC_ANALYSIS | 1 | 1 | 3 | 10 | 1 |
| NONE | 0 | 1 | 0 | 2 | 9 |
| REASONING | 0 | 0 | 0 | 1 | 0 |
| REPETITION | 0 | 0 | 0 | 0 | 1 |
| TRANSLATION_ATTEMPT | 0 | 2 | 2 | 22 | 2 |
| correction | 0 | 0 | 0 | 1 | 0 |
| neutral | 0 | 0 | 0 | 1 | 3 |
| null | 0 | 0 | 0 | 0 | 1 |

## 7. Translation Quality Correlations

### BLEU Metric

**Average BLEU by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| High | 5.24 |
| Medium | 1.91 |
| high | 1.39 |
| medium | 2.39 |
| neutral | 3.40 |

**Average BLEU by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| correction | 7.73 |
| neutral | 3.11 |
| TRANSLATION_ATTEMPT | 2.90 |
| CORRECT_LINGUISTIC_ANALYSIS | 2.59 |
| NONE | 1.78 |
| REASONING | 0.88 |
| null | 0.82 |
| REPETITION | 0.19 |

**Average BLEU by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| none | 1.39 |

---

### COMET Metric

**Average COMET by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| High | 0.30 |
| Medium | 0.35 |
| high | 0.34 |
| medium | 0.39 |
| neutral | 0.41 |

**Average COMET by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| correction | 0.72 |
| NONE | 0.40 |
| TRANSLATION_ATTEMPT | 0.38 |
| REASONING | 0.38 |
| CORRECT_LINGUISTIC_ANALYSIS | 0.37 |
| neutral | 0.36 |
| null | 0.35 |
| REPETITION | 0.30 |

**Average COMET by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| none | 0.36 |

---

### chrF++ Metric

**Average chrF++ by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| High | 18.11 |
| Medium | 12.04 |
| high | 11.91 |
| medium | 12.84 |
| neutral | 12.19 |

**Average chrF++ by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| correction | 14.97 |
| TRANSLATION_ATTEMPT | 13.35 |
| CORRECT_LINGUISTIC_ANALYSIS | 13.01 |
| NONE | 11.83 |
| neutral | 10.68 |
| REPETITION | 10.21 |
| null | 9.24 |
| REASONING | 7.20 |

**Average chrF++ by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| none | 11.55 |

---

### MetricX-24 Metric

**Average MetricX-24 by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| High | 17.25 |
| Medium | 15.27 |
| high | 16.05 |
| medium | 15.62 |
| neutral | 14.89 |

**Average MetricX-24 by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| REASONING | 17.12 |
| null | 16.00 |
| neutral | 15.97 |
| REPETITION | 15.75 |
| CORRECT_LINGUISTIC_ANALYSIS | 15.62 |
| TRANSLATION_ATTEMPT | 15.47 |
| correction | 15.06 |
| NONE | 14.88 |

**Average MetricX-24 by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| none | 15.33 |

---

## 8. Key Insights

- **Best performing trace type**: correction (BLEU: 7.73)
- **Worst performing trace type**: REPETITION (BLEU: 0.19)
- **Performance gap**: 3924.5% improvement from worst to best

- **Most common trace type**: TRANSLATION_ATTEMPT (28 examples, 43.8%)
- **Average difficulty score**: 3.00/5.0

---

*Analysis generated from evaluations/comprehensive_cot_eval/Lithuanian_Xhosa/gemma-3-1b-it/Lithuanian_to_Xhosa_0_shot_seed_42_identity_None_0_0_0/phase2_annotations.jsonl*
