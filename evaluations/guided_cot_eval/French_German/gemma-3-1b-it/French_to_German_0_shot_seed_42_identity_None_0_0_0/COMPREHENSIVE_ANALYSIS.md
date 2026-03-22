# Phase 2 Comprehensive Analysis

**Total Examples Analyzed**: 64

---

## 1. Difficulty Distribution

Distribution of translation difficulty scores (1=easiest, 5=hardest):

| Difficulty Score | Count | Percentage |
|-----------------|-------|------------|
| 2 | 8 | 12.9% |
| 3 | 49 | 79.0% |
| 4 | 5 | 8.1% |

## 2. Linguistic Phenomena Frequencies

Frequency of linguistic phenomena across 62 examples:

| Phenomenon | Count | Percentage |
|------------|-------|------------|
| long_distance_dependency | 61 | 98.4% |
| complex_syntax | 49 | 79.0% |
| named_entities | 49 | 79.0% |
| ambiguity | 1 | 1.6% |
| idiom | 1 | 1.6% |
| figurative_language | 1 | 1.6% |

## 3. Primary Trace Type Distribution

Distribution of reasoning trace types (n=62):

| Trace Type | Count | Percentage |
|------------|-------|------------|
| TRANSLATION_ATTEMPT | 38 | 61.3% |
| NONE | 9 | 14.5% |
| CORRECT_LINGUISTIC_ANALYSIS | 7 | 11.3% |
| neutral | 5 | 8.1% |
| correct_linguistic_analysis | 3 | 4.8% |

## 4. Trace Usefulness Distribution

Distribution of trace usefulness ratings:

| Usefulness Level | Count | Percentage |
|------------------|-------|------------|
| 2 | 1 | 1.6% |
| Medium | 4 | 6.5% |
| high | 7 | 11.3% |
| medium | 41 | 66.1% |
| neutral | 9 | 14.5% |

## 5. Trace-Translation Overlap Distribution

Distribution of overlap between reasoning traces and translations:

| Overlap Level | Count | Percentage |
|---------------|-------|------------|
| 0 | 1 | 3.4% |
| low | 1 | 3.4% |
| none | 27 | 93.1% |

## 6. Cross-Tabulations

### 6.1 Difficulty × Trace Type

| Difficulty | CORRECT_LINGUISTIC_ANALYSIS | NONE | TRANSLATION_ATTEMPT | correct_linguistic_analysis | neutral |
|---|---|---|---|---|---|
| 2 | 1 | 2 | 0 | 1 | 4 |
| 3 | 6 | 7 | 33 | 2 | 1 |
| 4 | 0 | 0 | 5 | 0 | 0 |

### 6.2 Trace Type × Usefulness

| Trace Type | 2 | Medium | high | medium | neutral |
|---|---|---|---|---|---|
| CORRECT_LINGUISTIC_ANALYSIS | 0 | 0 | 3 | 3 | 1 |
| NONE | 1 | 0 | 0 | 3 | 5 |
| TRANSLATION_ATTEMPT | 0 | 4 | 2 | 32 | 0 |
| correct_linguistic_analysis | 0 | 0 | 1 | 1 | 1 |
| neutral | 0 | 0 | 1 | 2 | 2 |

## 7. Translation Quality Correlations

### BLEU Metric

**Average BLEU by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 2 | 27.27 |
| Medium | 26.88 |
| high | 23.75 |
| medium | 16.60 |
| neutral | 19.71 |

**Average BLEU by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| correct_linguistic_analysis | 38.12 |
| CORRECT_LINGUISTIC_ANALYSIS | 19.52 |
| NONE | 18.63 |
| TRANSLATION_ATTEMPT | 17.30 |
| neutral | 16.56 |

**Average BLEU by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| 0 | 27.27 |
| low | 11.32 |
| none | 17.60 |

---

### MetricX-24 Metric

**Average MetricX-24 by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 2 | 4.56 |
| Medium | 1.52 |
| high | 3.21 |
| medium | 4.02 |
| neutral | 4.46 |

**Average MetricX-24 by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| CORRECT_LINGUISTIC_ANALYSIS | 4.42 |
| NONE | 4.05 |
| neutral | 4.05 |
| TRANSLATION_ATTEMPT | 3.84 |
| correct_linguistic_analysis | 1.51 |

**Average MetricX-24 by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| 0 | 4.56 |
| low | 1.00 |
| none | 4.19 |

---

### chrF++ Metric

**Average chrF++ by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 2 | 49.15 |
| Medium | 49.31 |
| high | 43.83 |
| medium | 39.03 |
| neutral | 41.09 |

**Average chrF++ by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| correct_linguistic_analysis | 54.43 |
| CORRECT_LINGUISTIC_ANALYSIS | 42.41 |
| NONE | 41.98 |
| TRANSLATION_ATTEMPT | 39.74 |
| neutral | 35.00 |

**Average chrF++ by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| 0 | 49.15 |
| low | 32.42 |
| none | 40.67 |

---

### COMET Metric

**Average COMET by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 2 | 0.55 |
| Medium | 0.87 |
| high | 0.80 |
| medium | 0.73 |
| neutral | 0.77 |

**Average COMET by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| correct_linguistic_analysis | 0.85 |
| neutral | 0.80 |
| NONE | 0.75 |
| TRANSLATION_ATTEMPT | 0.74 |
| CORRECT_LINGUISTIC_ANALYSIS | 0.72 |

**Average COMET by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| 0 | 0.55 |
| low | 0.86 |
| none | 0.71 |

---

## 8. Key Insights

- **Best performing trace type**: correct_linguistic_analysis (BLEU: 38.12)
- **Worst performing trace type**: neutral (BLEU: 16.56)
- **Performance gap**: 130.1% improvement from worst to best

- **Most common trace type**: TRANSLATION_ATTEMPT (38 examples, 61.3%)
- **Average difficulty score**: 2.95/5.0

---

*Analysis generated from evaluations/guided_cot_eval/French_German/gemma-3-1b-it/French_to_German_0_shot_seed_42_identity_None_0_0_0/phase2_annotations.jsonl*
