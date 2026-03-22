# Phase 2 Comprehensive Analysis

**Total Examples Analyzed**: 64

---

## 1. Difficulty Distribution

Distribution of translation difficulty scores (1=easiest, 5=hardest):

| Difficulty Score | Count | Percentage |
|-----------------|-------|------------|
| 2 | 1 | 1.9% |
| 3 | 43 | 79.6% |
| 4 | 6 | 11.1% |
| 5 | 4 | 7.4% |

## 2. Linguistic Phenomena Frequencies

Frequency of linguistic phenomena across 54 examples:

| Phenomenon | Count | Percentage |
|------------|-------|------------|
| long_distance_dependency | 54 | 100.0% |
| complex_syntax | 50 | 92.6% |
| named_entities | 41 | 75.9% |
| ambiguity | 3 | 5.6% |
| idiom | 2 | 3.7% |
| figurative_language | 2 | 3.7% |

## 3. Primary Trace Type Distribution

Distribution of reasoning trace types (n=54):

| Trace Type | Count | Percentage |
|------------|-------|------------|
| TRANSLATION_ATTEMPT | 37 | 68.5% |
| CORRECT_LINGUISTIC_ANALYSIS | 13 | 24.1% |
| RE 촉각 | 1 | 1.9% |
| REPETITION | 1 | 1.9% |
| correct_linguistic_analysis | 1 | 1.9% |
| NONE | 1 | 1.9% |

## 4. Trace Usefulness Distribution

Distribution of trace usefulness ratings:

| Usefulness Level | Count | Percentage |
|------------------|-------|------------|
| 3 | 1 | 1.9% |
| High | 2 | 3.7% |
| Medium | 9 | 16.7% |
| high | 6 | 11.1% |
| medium | 34 | 63.0% |
| neutral | 2 | 3.7% |

## 5. Trace-Translation Overlap Distribution

Distribution of overlap between reasoning traces and translations:

| Overlap Level | Count | Percentage |
|---------------|-------|------------|
| low | 2 | 5.0% |
| none | 38 | 95.0% |

## 6. Cross-Tabulations

### 6.1 Difficulty × Trace Type

| Difficulty | CORRECT_LINGUISTIC_ANALYSIS | NONE | RE 촉각 | REPETITION | TRANSLATION_ATTEMPT | correct_linguistic_analysis |
|---|---|---|---|---|---|---|
| 2 | 0 | 0 | 0 | 0 | 1 | 0 |
| 3 | 10 | 1 | 0 | 0 | 31 | 1 |
| 4 | 1 | 0 | 0 | 0 | 5 | 0 |
| 5 | 2 | 0 | 1 | 1 | 0 | 0 |

### 6.2 Trace Type × Usefulness

| Trace Type | 3 | High | Medium | high | medium | neutral |
|---|---|---|---|---|---|---|
| CORRECT_LINGUISTIC_ANALYSIS | 1 | 1 | 1 | 4 | 6 | 0 |
| NONE | 0 | 0 | 0 | 0 | 0 | 1 |
| RE 촉각 | 0 | 1 | 0 | 0 | 0 | 0 |
| REPETITION | 0 | 0 | 0 | 1 | 0 | 0 |
| TRANSLATION_ATTEMPT | 0 | 0 | 8 | 1 | 27 | 1 |
| correct_linguistic_analysis | 0 | 0 | 0 | 0 | 1 | 0 |

## 7. Translation Quality Correlations

### chrF++ Metric

**Average chrF++ by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 3 | 6.78 |
| High | 11.94 |
| Medium | 11.01 |
| high | 8.99 |
| medium | 12.54 |
| neutral | 18.84 |

**Average chrF++ by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| NONE | 18.46 |
| CORRECT_LINGUISTIC_ANALYSIS | 12.28 |
| TRANSLATION_ATTEMPT | 12.03 |
| REPETITION | 10.53 |
| RE 촉각 | 7.38 |
| correct_linguistic_analysis | 6.77 |

**Average chrF++ by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| low | 15.06 |
| none | 12.00 |

---

### MetricX-24 Metric

**Average MetricX-24 by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 3 | 17.50 |
| High | 18.06 |
| Medium | 18.15 |
| high | 18.00 |
| medium | 17.48 |
| neutral | 15.53 |

**Average MetricX-24 by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| REPETITION | 19.00 |
| correct_linguistic_analysis | 18.25 |
| CORRECT_LINGUISTIC_ANALYSIS | 17.62 |
| TRANSLATION_ATTEMPT | 17.60 |
| RE 촉각 | 17.38 |
| NONE | 15.38 |

**Average MetricX-24 by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| low | 17.12 |
| none | 17.44 |

---

### COMET Metric

**Average COMET by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 3 | 0.32 |
| High | 0.30 |
| Medium | 0.34 |
| high | 0.33 |
| medium | 0.34 |
| neutral | 0.33 |

**Average COMET by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| REPETITION | 0.41 |
| CORRECT_LINGUISTIC_ANALYSIS | 0.34 |
| TRANSLATION_ATTEMPT | 0.34 |
| RE 촉각 | 0.33 |
| NONE | 0.32 |
| correct_linguistic_analysis | 0.31 |

**Average COMET by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| low | 0.37 |
| none | 0.34 |

---

### BLEU Metric

**Average BLEU by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 3 | 0.33 |
| High | 2.31 |
| Medium | 1.71 |
| high | 1.49 |
| medium | 2.60 |
| neutral | 1.86 |

**Average BLEU by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| TRANSLATION_ATTEMPT | 2.53 |
| CORRECT_LINGUISTIC_ANALYSIS | 1.75 |
| correct_linguistic_analysis | 1.61 |
| REPETITION | 1.51 |
| NONE | 1.00 |
| RE 촉각 | 0.79 |

**Average BLEU by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| low | 1.68 |
| none | 2.43 |

---

## 8. Key Insights

- **Best performing trace type**: TRANSLATION_ATTEMPT (BLEU: 2.53)
- **Worst performing trace type**: RE 촉각 (BLEU: 0.79)
- **Performance gap**: 222.5% improvement from worst to best

- **Most common trace type**: TRANSLATION_ATTEMPT (37 examples, 68.5%)
- **Average difficulty score**: 3.24/5.0

---

*Analysis generated from evaluations/guided_cot_eval/Xhosa_Lithuanian/gemma-3-1b-it/Xhosa_to_Lithuanian_0_shot_seed_42_identity_None_0_0_0/phase2_annotations.jsonl*
