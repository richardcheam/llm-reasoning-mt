# Phase 2 Comprehensive Analysis

**Total Examples Analyzed**: 64

---

## 1. Difficulty Distribution

Distribution of translation difficulty scores (1=easiest, 5=hardest):

| Difficulty Score | Count | Percentage |
|-----------------|-------|------------|
| 1 | 5 | 7.9% |
| 2 | 22 | 34.9% |
| 3 | 29 | 46.0% |
| 4 | 1 | 1.6% |
| 5 | 6 | 9.5% |

## 2. Linguistic Phenomena Frequencies

Frequency of linguistic phenomena across 63 examples:

| Phenomenon | Count | Percentage |
|------------|-------|------------|
| long_distance_dependency | 56 | 88.9% |
| named_entities | 52 | 82.5% |
| complex_syntax | 37 | 58.7% |
| ambiguity | 1 | 1.6% |
| idiom | 1 | 1.6% |
| figurative_language | 1 | 1.6% |

## 3. Primary Trace Type Distribution

Distribution of reasoning trace types (n=63):

| Trace Type | Count | Percentage |
|------------|-------|------------|
| TRANSLATION_ATTEMPT | 20 | 31.7% |
| NONE | 19 | 30.2% |
| neutral | 17 | 27.0% |
| CORRECT_LINGUISTIC_ANALYSIS | 4 | 6.3% |
| null | 2 | 3.2% |
| correct_linguistic_analysis | 1 | 1.6% |

## 4. Trace Usefulness Distribution

Distribution of trace usefulness ratings:

| Usefulness Level | Count | Percentage |
|------------------|-------|------------|
| 1 | 1 | 1.6% |
| HIGH | 1 | 1.6% |
| Medium | 2 | 3.2% |
| high | 6 | 9.5% |
| medium | 26 | 41.3% |
| neutral | 27 | 42.9% |

## 5. Trace-Translation Overlap Distribution

Distribution of overlap between reasoning traces and translations:

| Overlap Level | Count | Percentage |
|---------------|-------|------------|
| 0 | 1 | 7.7% |
| low | 1 | 7.7% |
| none | 11 | 84.6% |

## 6. Cross-Tabulations

### 6.1 Difficulty × Trace Type

| Difficulty | CORRECT_LINGUISTIC_ANALYSIS | NONE | TRANSLATION_ATTEMPT | correct_linguistic_analysis | neutral | null |
|---|---|---|---|---|---|---|
| 1 | 0 | 1 | 0 | 0 | 2 | 2 |
| 2 | 0 | 4 | 3 | 0 | 15 | 0 |
| 3 | 3 | 10 | 15 | 1 | 0 | 0 |
| 4 | 0 | 0 | 1 | 0 | 0 | 0 |
| 5 | 1 | 4 | 1 | 0 | 0 | 0 |

### 6.2 Trace Type × Usefulness

| Trace Type | 1 | HIGH | Medium | high | medium | neutral |
|---|---|---|---|---|---|---|
| CORRECT_LINGUISTIC_ANALYSIS | 0 | 0 | 0 | 2 | 2 | 0 |
| NONE | 1 | 1 | 1 | 2 | 4 | 10 |
| TRANSLATION_ATTEMPT | 0 | 0 | 1 | 1 | 17 | 1 |
| correct_linguistic_analysis | 0 | 0 | 0 | 0 | 1 | 0 |
| neutral | 0 | 0 | 0 | 1 | 2 | 14 |
| null | 0 | 0 | 0 | 0 | 0 | 2 |

## 7. Translation Quality Correlations

### COMET Metric

**Average COMET by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 1 | 0.82 |
| HIGH | 0.80 |
| Medium | 0.85 |
| high | 0.83 |
| medium | 0.74 |
| neutral | 0.76 |

**Average COMET by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| correct_linguistic_analysis | 0.84 |
| CORRECT_LINGUISTIC_ANALYSIS | 0.84 |
| neutral | 0.79 |
| null | 0.79 |
| NONE | 0.76 |
| TRANSLATION_ATTEMPT | 0.72 |

**Average COMET by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| 0 | 0.82 |
| low | 0.81 |
| none | 0.79 |

---

### chrF++ Metric

**Average chrF++ by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 1 | 38.03 |
| HIGH | 32.76 |
| Medium | 37.70 |
| high | 44.65 |
| medium | 39.13 |
| neutral | 40.97 |

**Average chrF++ by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| CORRECT_LINGUISTIC_ANALYSIS | 47.21 |
| TRANSLATION_ATTEMPT | 42.11 |
| neutral | 42.01 |
| correct_linguistic_analysis | 41.57 |
| null | 37.88 |
| NONE | 35.53 |

**Average chrF++ by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| 0 | 38.03 |
| low | 51.14 |
| none | 46.60 |

---

### MetricX-24 Metric

**Average MetricX-24 by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 1 | 2.48 |
| HIGH | 3.33 |
| Medium | 1.15 |
| high | 1.91 |
| medium | 4.52 |
| neutral | 3.85 |

**Average MetricX-24 by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| NONE | 5.00 |
| TRANSLATION_ATTEMPT | 4.33 |
| neutral | 2.80 |
| null | 2.04 |
| CORRECT_LINGUISTIC_ANALYSIS | 1.57 |
| correct_linguistic_analysis | 1.43 |

**Average MetricX-24 by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| 0 | 2.48 |
| low | 2.86 |
| none | 2.93 |

---

### BLEU Metric

**Average BLEU by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 1 | 18.95 |
| HIGH | 8.01 |
| Medium | 20.51 |
| high | 20.45 |
| medium | 15.67 |
| neutral | 19.74 |

**Average BLEU by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| neutral | 21.47 |
| CORRECT_LINGUISTIC_ANALYSIS | 19.55 |
| TRANSLATION_ATTEMPT | 17.76 |
| NONE | 15.62 |
| null | 12.08 |
| correct_linguistic_analysis | 11.76 |

**Average BLEU by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| 0 | 18.95 |
| low | 19.08 |
| none | 20.61 |

---

## 8. Key Insights

- **Best performing trace type**: neutral (BLEU: 21.47)
- **Worst performing trace type**: correct_linguistic_analysis (BLEU: 11.76)
- **Performance gap**: 82.6% improvement from worst to best

- **Most common trace type**: TRANSLATION_ATTEMPT (20 examples, 31.7%)
- **Average difficulty score**: 2.70/5.0

---

*Analysis generated from evaluations/comprehensive_cot_eval/French_German/gemma-3-1b-it/French_to_German_0_shot_seed_42_identity_None_0_0_0/phase2_annotations.jsonl*
