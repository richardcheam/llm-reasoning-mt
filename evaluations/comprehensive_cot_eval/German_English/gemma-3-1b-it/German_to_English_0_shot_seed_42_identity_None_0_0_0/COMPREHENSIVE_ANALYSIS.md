# Phase 2 Comprehensive Analysis

**Total Examples Analyzed**: 64

---

## 1. Difficulty Distribution

Distribution of translation difficulty scores (1=easiest, 5=hardest):

| Difficulty Score | Count | Percentage |
|-----------------|-------|------------|
| 1 | 3 | 4.8% |
| 2 | 34 | 54.0% |
| 3 | 23 | 36.5% |
| 4 | 3 | 4.8% |

## 2. Linguistic Phenomena Frequencies

Frequency of linguistic phenomena across 63 examples:

| Phenomenon | Count | Percentage |
|------------|-------|------------|
| named_entities | 48 | 76.2% |
| long_distance_dependency | 47 | 74.6% |
| complex_syntax | 14 | 22.2% |

## 3. Primary Trace Type Distribution

Distribution of reasoning trace types (n=63):

| Trace Type | Count | Percentage |
|------------|-------|------------|
| neutral | 26 | 41.3% |
| TRANSLATION_ATTEMPT | 19 | 30.2% |
| NONE | 12 | 19.0% |
| CORRECT_LINGUISTIC_ANALYSIS | 4 | 6.3% |
| null | 2 | 3.2% |

## 4. Trace Usefulness Distribution

Distribution of trace usefulness ratings:

| Usefulness Level | Count | Percentage |
|------------------|-------|------------|
| high | 9 | 14.3% |
| medium | 15 | 23.8% |
| neutral | 39 | 61.9% |

## 5. Trace-Translation Overlap Distribution

Distribution of overlap between reasoning traces and translations:

| Overlap Level | Count | Percentage |
|---------------|-------|------------|
| none | 2 | 100.0% |

## 6. Cross-Tabulations

### 6.1 Difficulty × Trace Type

| Difficulty | CORRECT_LINGUISTIC_ANALYSIS | NONE | TRANSLATION_ATTEMPT | neutral | null |
|---|---|---|---|---|---|
| 1 | 0 | 1 | 0 | 0 | 2 |
| 2 | 1 | 7 | 1 | 25 | 0 |
| 3 | 3 | 4 | 15 | 1 | 0 |
| 4 | 0 | 0 | 3 | 0 | 0 |

### 6.2 Trace Type × Usefulness

| Trace Type | high | medium | neutral |
|---|---|---|---|
| CORRECT_LINGUISTIC_ANALYSIS | 4 | 0 | 0 |
| NONE | 1 | 0 | 11 |
| TRANSLATION_ATTEMPT | 4 | 15 | 0 |
| neutral | 0 | 0 | 26 |
| null | 0 | 0 | 2 |

## 7. Translation Quality Correlations

### BLEU Metric

**Average BLEU by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| high | 27.75 |
| medium | 22.46 |
| neutral | 26.62 |

**Average BLEU by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| CORRECT_LINGUISTIC_ANALYSIS | 41.73 |
| neutral | 27.96 |
| NONE | 23.15 |
| TRANSLATION_ATTEMPT | 21.65 |
| null | 20.90 |

**Average BLEU by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| none | 25.94 |

---

### COMET Metric

**Average COMET by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| high | 0.85 |
| medium | 0.84 |
| neutral | 0.85 |

**Average COMET by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| CORRECT_LINGUISTIC_ANALYSIS | 0.87 |
| neutral | 0.86 |
| NONE | 0.84 |
| TRANSLATION_ATTEMPT | 0.83 |
| null | 0.82 |

**Average COMET by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| none | 0.81 |

---

### MetricX-24 Metric

**Average MetricX-24 by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| high | 4.12 |
| medium | 4.98 |
| neutral | 3.96 |

**Average MetricX-24 by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| TRANSLATION_ATTEMPT | 5.06 |
| NONE | 4.24 |
| neutral | 3.82 |
| CORRECT_LINGUISTIC_ANALYSIS | 3.41 |
| null | 3.12 |

**Average MetricX-24 by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| none | 3.60 |

---

### chrF++ Metric

**Average chrF++ by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| high | 54.96 |
| medium | 48.77 |
| neutral | 50.90 |

**Average chrF++ by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| CORRECT_LINGUISTIC_ANALYSIS | 65.27 |
| null | 54.44 |
| neutral | 52.36 |
| TRANSLATION_ATTEMPT | 47.95 |
| NONE | 47.41 |

**Average chrF++ by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| none | 55.21 |

---

## 8. Key Insights

- **Best performing trace type**: CORRECT_LINGUISTIC_ANALYSIS (BLEU: 41.73)
- **Worst performing trace type**: null (BLEU: 20.90)
- **Performance gap**: 99.6% improvement from worst to best

- **Most common trace type**: neutral (26 examples, 41.3%)
- **Average difficulty score**: 2.41/5.0

---

*Analysis generated from evaluations/comprehensive_cot_eval/German_English/gemma-3-1b-it/German_to_English_0_shot_seed_42_identity_None_0_0_0/phase2_annotations.jsonl*
