# Phase 2 Comprehensive Analysis

**Total Examples Analyzed**: 64

---

## 1. Difficulty Distribution

Distribution of translation difficulty scores (1=easiest, 5=hardest):

| Difficulty Score | Count | Percentage |
|-----------------|-------|------------|
| 1 | 2 | 3.2% |
| 2 | 11 | 17.5% |
| 3 | 44 | 69.8% |
| 4 | 4 | 6.3% |
| 5 | 2 | 3.2% |

## 2. Linguistic Phenomena Frequencies

Frequency of linguistic phenomena across 63 examples:

| Phenomenon | Count | Percentage |
|------------|-------|------------|
| long_distance_dependency | 59 | 93.7% |
| named_entities | 46 | 73.0% |
| complex_syntax | 40 | 63.5% |
| idiom | 1 | 1.6% |

## 3. Primary Trace Type Distribution

Distribution of reasoning trace types (n=63):

| Trace Type | Count | Percentage |
|------------|-------|------------|
| TRANSLATION_ATTEMPT | 29 | 46.0% |
| CORRECT_LINGUISTIC_ANALYSIS | 16 | 25.4% |
| NONE | 12 | 19.0% |
| neutral | 5 | 7.9% |
| REPETITION | 1 | 1.6% |

## 4. Trace Usefulness Distribution

Distribution of trace usefulness ratings:

| Usefulness Level | Count | Percentage |
|------------------|-------|------------|
| High | 1 | 1.6% |
| Medium | 2 | 3.2% |
| high | 13 | 20.6% |
| medium | 31 | 49.2% |
| neutral | 16 | 25.4% |

## 5. Trace-Translation Overlap Distribution

Distribution of overlap between reasoning traces and translations:

| Overlap Level | Count | Percentage |
|---------------|-------|------------|
| none | 16 | 100.0% |

## 6. Cross-Tabulations

### 6.1 Difficulty × Trace Type

| Difficulty | CORRECT_LINGUISTIC_ANALYSIS | NONE | REPETITION | TRANSLATION_ATTEMPT | neutral |
|---|---|---|---|---|---|
| 1 | 2 | 0 | 0 | 0 | 0 |
| 2 | 4 | 2 | 0 | 0 | 5 |
| 3 | 9 | 10 | 1 | 24 | 0 |
| 4 | 0 | 0 | 0 | 4 | 0 |
| 5 | 1 | 0 | 0 | 1 | 0 |

### 6.2 Trace Type × Usefulness

| Trace Type | High | Medium | high | medium | neutral |
|---|---|---|---|---|---|
| CORRECT_LINGUISTIC_ANALYSIS | 0 | 0 | 13 | 3 | 0 |
| NONE | 0 | 0 | 0 | 1 | 11 |
| REPETITION | 0 | 0 | 0 | 0 | 1 |
| TRANSLATION_ATTEMPT | 1 | 2 | 0 | 26 | 0 |
| neutral | 0 | 0 | 0 | 1 | 4 |

## 7. Translation Quality Correlations

### BLEU Metric

**Average BLEU by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| High | 9.70 |
| Medium | 1.57 |
| high | 5.65 |
| medium | 5.62 |
| neutral | 6.61 |

**Average BLEU by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| REPETITION | 10.86 |
| NONE | 7.39 |
| TRANSLATION_ATTEMPT | 5.80 |
| CORRECT_LINGUISTIC_ANALYSIS | 5.04 |
| neutral | 3.58 |

**Average BLEU by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| none | 4.63 |

---

### chrF++ Metric

**Average chrF++ by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| High | 25.39 |
| Medium | 15.06 |
| high | 19.36 |
| medium | 22.83 |
| neutral | 20.86 |

**Average chrF++ by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| REPETITION | 28.48 |
| TRANSLATION_ATTEMPT | 22.61 |
| NONE | 22.11 |
| CORRECT_LINGUISTIC_ANALYSIS | 19.24 |
| neutral | 18.30 |

**Average chrF++ by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| none | 22.28 |

---

### MetricX-24 Metric

**Average MetricX-24 by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| High | 14.94 |
| Medium | 16.88 |
| high | 15.77 |
| medium | 14.97 |
| neutral | 14.12 |

**Average MetricX-24 by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| REPETITION | 16.25 |
| neutral | 15.50 |
| CORRECT_LINGUISTIC_ANALYSIS | 15.46 |
| TRANSLATION_ATTEMPT | 15.04 |
| NONE | 13.84 |

**Average MetricX-24 by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| none | 15.24 |

---

### COMET Metric

**Average COMET by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| High | 0.54 |
| Medium | 0.39 |
| high | 0.49 |
| medium | 0.51 |
| neutral | 0.52 |

**Average COMET by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| NONE | 0.54 |
| TRANSLATION_ATTEMPT | 0.51 |
| CORRECT_LINGUISTIC_ANALYSIS | 0.49 |
| neutral | 0.46 |
| REPETITION | 0.45 |

**Average COMET by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| none | 0.50 |

---

## 8. Key Insights

- **Best performing trace type**: REPETITION (BLEU: 10.86)
- **Worst performing trace type**: neutral (BLEU: 3.58)
- **Performance gap**: 203.1% improvement from worst to best

- **Most common trace type**: TRANSLATION_ATTEMPT (29 examples, 46.0%)
- **Average difficulty score**: 2.89/5.0

---

*Analysis generated from evaluations/comprehensive_cot_eval/Xhosa_English/gemma-3-1b-it/Xhosa_to_English_0_shot_seed_42_identity_None_0_0_0/phase2_annotations.jsonl*
