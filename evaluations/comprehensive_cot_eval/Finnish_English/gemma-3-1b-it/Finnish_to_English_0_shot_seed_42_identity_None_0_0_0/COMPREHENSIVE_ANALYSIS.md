# Phase 2 Comprehensive Analysis

**Total Examples Analyzed**: 64

---

## 1. Difficulty Distribution

Distribution of translation difficulty scores (1=easiest, 5=hardest):

| Difficulty Score | Count | Percentage |
|-----------------|-------|------------|
| 1 | 1 | 1.6% |
| 2 | 33 | 51.6% |
| 3 | 26 | 40.6% |
| 4 | 1 | 1.6% |
| 5 | 3 | 4.7% |

## 2. Linguistic Phenomena Frequencies

Frequency of linguistic phenomena across 64 examples:

| Phenomenon | Count | Percentage |
|------------|-------|------------|
| long_distance_dependency | 48 | 75.0% |
| named_entities | 45 | 70.3% |
| complex_syntax | 14 | 21.9% |
| ambiguity | 1 | 1.6% |

## 3. Primary Trace Type Distribution

Distribution of reasoning trace types (n=64):

| Trace Type | Count | Percentage |
|------------|-------|------------|
| neutral | 21 | 32.8% |
| TRANSLATION_ATTEMPT | 20 | 31.2% |
| NONE | 15 | 23.4% |
| CORRECT_LINGUISTIC_ANALYSIS | 8 | 12.5% |

## 4. Trace Usefulness Distribution

Distribution of trace usefulness ratings:

| Usefulness Level | Count | Percentage |
|------------------|-------|------------|
| helpful | 2 | 3.1% |
| high | 11 | 17.2% |
| medium | 16 | 25.0% |
| neutral | 35 | 54.7% |

## 5. Trace-Translation Overlap Distribution

Distribution of overlap between reasoning traces and translations:

| Overlap Level | Count | Percentage |
|---------------|-------|------------|
| none | 4 | 100.0% |

## 6. Cross-Tabulations

### 6.1 Difficulty × Trace Type

| Difficulty | CORRECT_LINGUISTIC_ANALYSIS | NONE | TRANSLATION_ATTEMPT | neutral |
|---|---|---|---|---|
| 1 | 0 | 1 | 0 | 0 |
| 2 | 3 | 6 | 3 | 21 |
| 3 | 5 | 7 | 14 | 0 |
| 4 | 0 | 0 | 1 | 0 |
| 5 | 0 | 1 | 2 | 0 |

### 6.2 Trace Type × Usefulness

| Trace Type | helpful | high | medium | neutral |
|---|---|---|---|---|
| CORRECT_LINGUISTIC_ANALYSIS | 1 | 7 | 0 | 0 |
| NONE | 1 | 1 | 2 | 11 |
| TRANSLATION_ATTEMPT | 0 | 3 | 14 | 3 |
| neutral | 0 | 0 | 0 | 21 |

## 7. Translation Quality Correlations

### COMET Metric

**Average COMET by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| helpful | 0.77 |
| high | 0.82 |
| medium | 0.84 |
| neutral | 0.82 |

**Average COMET by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| TRANSLATION_ATTEMPT | 0.84 |
| NONE | 0.84 |
| neutral | 0.82 |
| CORRECT_LINGUISTIC_ANALYSIS | 0.77 |

**Average COMET by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| none | 0.80 |

---

### MetricX-24 Metric

**Average MetricX-24 by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| helpful | 7.64 |
| high | 6.08 |
| medium | 5.49 |
| neutral | 5.52 |

**Average MetricX-24 by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| CORRECT_LINGUISTIC_ANALYSIS | 7.17 |
| neutral | 6.15 |
| TRANSLATION_ATTEMPT | 5.23 |
| NONE | 4.82 |

**Average MetricX-24 by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| none | 7.73 |

---

### BLEU Metric

**Average BLEU by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| helpful | 5.65 |
| high | 19.16 |
| medium | 15.87 |
| neutral | 17.69 |

**Average BLEU by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| NONE | 23.36 |
| TRANSLATION_ATTEMPT | 16.30 |
| CORRECT_LINGUISTIC_ANALYSIS | 15.45 |
| neutral | 14.05 |

**Average BLEU by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| none | 7.86 |

---

### chrF++ Metric

**Average chrF++ by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| helpful | 32.33 |
| high | 40.33 |
| medium | 39.94 |
| neutral | 41.34 |

**Average chrF++ by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| NONE | 44.50 |
| TRANSLATION_ATTEMPT | 39.81 |
| neutral | 39.55 |
| CORRECT_LINGUISTIC_ANALYSIS | 37.47 |

**Average chrF++ by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| none | 34.78 |

---

## 8. Key Insights

- **Best performing trace type**: NONE (BLEU: 23.36)
- **Worst performing trace type**: neutral (BLEU: 14.05)
- **Performance gap**: 66.2% improvement from worst to best

- **Most common trace type**: neutral (21 examples, 32.8%)
- **Average difficulty score**: 2.56/5.0

---

*Analysis generated from evaluations/comprehensive_cot_eval/Finnish_English/gemma-3-1b-it/Finnish_to_English_0_shot_seed_42_identity_None_0_0_0/phase2_annotations.jsonl*
