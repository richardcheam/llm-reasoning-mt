# Phase 2 Comprehensive Analysis

**Total Examples Analyzed**: 64

---

## 1. Difficulty Distribution

Distribution of translation difficulty scores (1=easiest, 5=hardest):

| Difficulty Score | Count | Percentage |
|-----------------|-------|------------|
| 1 | 1 | 1.6% |
| 2 | 5 | 8.1% |
| 3 | 47 | 75.8% |
| 4 | 6 | 9.7% |
| 5 | 3 | 4.8% |

## 2. Linguistic Phenomena Frequencies

Frequency of linguistic phenomena across 62 examples:

| Phenomenon | Count | Percentage |
|------------|-------|------------|
| long_distance_dependency | 61 | 98.4% |
| complex_syntax | 48 | 77.4% |
| named_entities | 42 | 67.7% |
| ambiguity | 7 | 11.3% |
| idiom | 7 | 11.3% |
| figurative_language | 7 | 11.3% |

## 3. Primary Trace Type Distribution

Distribution of reasoning trace types (n=62):

| Trace Type | Count | Percentage |
|------------|-------|------------|
| CORRECT_LINGUISTIC_ANALYSIS | 44 | 71.0% |
| TRANSLATION_ATTEMPT | 8 | 12.9% |
| correct_linguistic_analysis | 4 | 6.5% |
| neutral | 4 | 6.5% |
| NONE | 1 | 1.6% |
| REASONING | 1 | 1.6% |

## 4. Trace Usefulness Distribution

Distribution of trace usefulness ratings:

| Usefulness Level | Count | Percentage |
|------------------|-------|------------|
| 2 | 3 | 4.8% |
| 3 | 3 | 4.8% |
| High | 2 | 3.2% |
| Medium | 2 | 3.2% |
| Medium (the translation is accurate but could be refined for a more natural flow) | 1 | 1.6% |
| high | 12 | 19.4% |
| medium | 34 | 54.8% |
| neutral | 5 | 8.1% |

## 5. Trace-Translation Overlap Distribution

Distribution of overlap between reasoning traces and translations:

| Overlap Level | Count | Percentage |
|---------------|-------|------------|
| 0 | 3 | 13.0% |
| none | 20 | 87.0% |

## 6. Cross-Tabulations

### 6.1 Difficulty × Trace Type

| Difficulty | CORRECT_LINGUISTIC_ANALYSIS | NONE | REASONING | TRANSLATION_ATTEMPT | correct_linguistic_analysis | neutral |
|---|---|---|---|---|---|---|
| 1 | 1 | 0 | 0 | 0 | 0 | 0 |
| 2 | 1 | 0 | 0 | 1 | 0 | 3 |
| 3 | 34 | 1 | 1 | 6 | 4 | 1 |
| 4 | 5 | 0 | 0 | 1 | 0 | 0 |
| 5 | 3 | 0 | 0 | 0 | 0 | 0 |

### 6.2 Trace Type × Usefulness

| Trace Type | 2 | 3 | High | Medium | Medium (the translation is accurate but could be refined for a more natural flow) | high | medium | neutral |
|---|---|---|---|---|---|---|---|---|
| CORRECT_LINGUISTIC_ANALYSIS | 2 | 3 | 2 | 2 | 1 | 12 | 21 | 1 |
| NONE | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 |
| REASONING | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 |
| TRANSLATION_ATTEMPT | 0 | 0 | 0 | 0 | 0 | 0 | 7 | 1 |
| correct_linguistic_analysis | 1 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| neutral | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 3 |

## 7. Translation Quality Correlations

### chrF++ Metric

**Average chrF++ by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 2 | 15.42 |
| 3 | 21.95 |
| High | 7.88 |
| Medium | 20.49 |
| Medium (the translation is accurate but could be refined for a more natural flow) | 19.12 |
| high | 18.95 |
| medium | 19.75 |
| neutral | 16.11 |

**Average chrF++ by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| REASONING | 38.83 |
| correct_linguistic_analysis | 20.59 |
| TRANSLATION_ATTEMPT | 20.13 |
| CORRECT_LINGUISTIC_ANALYSIS | 18.48 |
| neutral | 15.01 |
| NONE | 11.90 |

**Average chrF++ by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| 0 | 15.42 |
| none | 19.49 |

---

### BLEU Metric

**Average BLEU by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 2 | 0.93 |
| 3 | 3.65 |
| High | 0.70 |
| Medium | 2.37 |
| Medium (the translation is accurate but could be refined for a more natural flow) | 0.99 |
| high | 2.59 |
| medium | 4.96 |
| neutral | 2.69 |

**Average BLEU by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| REASONING | 15.71 |
| correct_linguistic_analysis | 3.93 |
| neutral | 3.65 |
| CORRECT_LINGUISTIC_ANALYSIS | 3.60 |
| NONE | 3.43 |
| TRANSLATION_ATTEMPT | 3.25 |

**Average BLEU by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| 0 | 0.93 |
| none | 4.48 |

---

### MetricX-24 Metric

**Average MetricX-24 by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 2 | 14.15 |
| 3 | 18.62 |
| High | 15.16 |
| Medium | 17.00 |
| Medium (the translation is accurate but could be refined for a more natural flow) | 15.19 |
| high | 17.77 |
| medium | 15.90 |
| neutral | 16.30 |

**Average MetricX-24 by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| TRANSLATION_ATTEMPT | 16.73 |
| CORRECT_LINGUISTIC_ANALYSIS | 16.59 |
| NONE | 15.81 |
| correct_linguistic_analysis | 15.77 |
| neutral | 14.30 |
| REASONING | 13.62 |

**Average MetricX-24 by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| 0 | 14.15 |
| none | 15.97 |

---

### COMET Metric

**Average COMET by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 2 | 0.51 |
| 3 | 0.38 |
| High | 0.41 |
| Medium | 0.48 |
| Medium (the translation is accurate but could be refined for a more natural flow) | 0.48 |
| high | 0.44 |
| medium | 0.53 |
| neutral | 0.52 |

**Average COMET by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| REASONING | 0.75 |
| neutral | 0.60 |
| NONE | 0.56 |
| CORRECT_LINGUISTIC_ANALYSIS | 0.48 |
| correct_linguistic_analysis | 0.47 |
| TRANSLATION_ATTEMPT | 0.47 |

**Average COMET by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| 0 | 0.51 |
| none | 0.51 |

---

## 8. Key Insights

- **Best performing trace type**: REASONING (BLEU: 15.71)
- **Worst performing trace type**: TRANSLATION_ATTEMPT (BLEU: 3.25)
- **Performance gap**: 384.1% improvement from worst to best

- **Most common trace type**: CORRECT_LINGUISTIC_ANALYSIS (44 examples, 71.0%)
- **Average difficulty score**: 3.08/5.0

---

*Analysis generated from evaluations/guided_cot_eval/Turkish_Lithuanian/gemma-3-1b-it/Turkish_to_Lithuanian_0_shot_seed_42_identity_None_0_0_0/phase2_annotations.jsonl*
