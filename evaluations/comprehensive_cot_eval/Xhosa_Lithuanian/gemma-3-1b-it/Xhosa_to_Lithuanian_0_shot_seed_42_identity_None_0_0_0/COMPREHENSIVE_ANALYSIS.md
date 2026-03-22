# Phase 2 Comprehensive Analysis

**Total Examples Analyzed**: 64

---

## 1. Difficulty Distribution

Distribution of translation difficulty scores (1=easiest, 5=hardest):

| Difficulty Score | Count | Percentage |
|-----------------|-------|------------|
| 1 | 1 | 1.8% |
| 2 | 3 | 5.5% |
| 3 | 33 | 60.0% |
| 4 | 14 | 25.5% |
| 5 | 4 | 7.3% |

## 2. Linguistic Phenomena Frequencies

Frequency of linguistic phenomena across 55 examples:

| Phenomenon | Count | Percentage |
|------------|-------|------------|
| long_distance_dependency | 52 | 94.5% |
| complex_syntax | 44 | 80.0% |
| named_entities | 42 | 76.4% |
| figurative_language | 4 | 7.3% |
| ambiguity | 3 | 5.5% |
| idiom | 3 | 5.5% |

## 3. Primary Trace Type Distribution

Distribution of reasoning trace types (n=55):

| Trace Type | Count | Percentage |
|------------|-------|------------|
| CORRECT_LINGUISTIC_ANALYSIS | 30 | 54.5% |
| TRANSLATION_ATTEMPT | 18 | 32.7% |
| NONE | 3 | 5.5% |
| correct_linguistic_analysis | 2 | 3.6% |
| neutral | 1 | 1.8% |
| REPETITION | 1 | 1.8% |

## 4. Trace Usefulness Distribution

Distribution of trace usefulness ratings:

| Usefulness Level | Count | Percentage |
|------------------|-------|------------|
| 3 | 1 | 1.8% |
| High | 1 | 1.8% |
| Medium | 8 | 14.5% |
| high | 11 | 20.0% |
| medium | 31 | 56.4% |
| neutral | 3 | 5.5% |

## 5. Trace-Translation Overlap Distribution

Distribution of overlap between reasoning traces and translations:

| Overlap Level | Count | Percentage |
|---------------|-------|------------|
| 0 | 1 | 3.4% |
| low | 3 | 10.3% |
| none | 25 | 86.2% |

## 6. Cross-Tabulations

### 6.1 Difficulty × Trace Type

| Difficulty | CORRECT_LINGUISTIC_ANALYSIS | NONE | REPETITION | TRANSLATION_ATTEMPT | correct_linguistic_analysis | neutral |
|---|---|---|---|---|---|---|
| 1 | 1 | 0 | 0 | 0 | 0 | 0 |
| 2 | 1 | 1 | 0 | 0 | 0 | 1 |
| 3 | 20 | 2 | 0 | 10 | 1 | 0 |
| 4 | 4 | 0 | 1 | 8 | 1 | 0 |
| 5 | 4 | 0 | 0 | 0 | 0 | 0 |

### 6.2 Trace Type × Usefulness

| Trace Type | 3 | High | Medium | high | medium | neutral |
|---|---|---|---|---|---|---|
| CORRECT_LINGUISTIC_ANALYSIS | 1 | 1 | 4 | 10 | 14 | 0 |
| NONE | 0 | 0 | 0 | 0 | 1 | 2 |
| REPETITION | 0 | 0 | 0 | 0 | 1 | 0 |
| TRANSLATION_ATTEMPT | 0 | 0 | 4 | 1 | 13 | 0 |
| correct_linguistic_analysis | 0 | 0 | 0 | 0 | 2 | 0 |
| neutral | 0 | 0 | 0 | 0 | 0 | 1 |

## 7. Translation Quality Correlations

### BLEU Metric

**Average BLEU by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 3 | 1.15 |
| High | 0.00 |
| Medium | 1.48 |
| high | 2.24 |
| medium | 1.86 |
| neutral | 7.64 |

**Average BLEU by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| NONE | 6.98 |
| neutral | 2.65 |
| CORRECT_LINGUISTIC_ANALYSIS | 2.44 |
| REPETITION | 1.33 |
| TRANSLATION_ATTEMPT | 1.04 |
| correct_linguistic_analysis | 0.69 |

**Average BLEU by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| 0 | 1.15 |
| low | 1.29 |
| none | 1.36 |

---

### COMET Metric

**Average COMET by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 3 | 0.36 |
| High | 0.24 |
| Medium | 0.33 |
| high | 0.33 |
| medium | 0.33 |
| neutral | 0.43 |

**Average COMET by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| NONE | 0.40 |
| neutral | 0.37 |
| REPETITION | 0.34 |
| CORRECT_LINGUISTIC_ANALYSIS | 0.34 |
| correct_linguistic_analysis | 0.32 |
| TRANSLATION_ATTEMPT | 0.32 |

**Average COMET by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| 0 | 0.36 |
| low | 0.29 |
| none | 0.33 |

---

### chrF++ Metric

**Average chrF++ by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 3 | 12.53 |
| High | 7.58 |
| Medium | 12.21 |
| high | 13.08 |
| medium | 12.50 |
| neutral | 17.53 |

**Average chrF++ by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| NONE | 18.13 |
| REPETITION | 16.25 |
| CORRECT_LINGUISTIC_ANALYSIS | 12.81 |
| correct_linguistic_analysis | 12.44 |
| TRANSLATION_ATTEMPT | 11.76 |
| neutral | 10.57 |

**Average chrF++ by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| 0 | 12.53 |
| low | 12.53 |
| none | 12.29 |

---

### MetricX-24 Metric

**Average MetricX-24 by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 3 | 17.62 |
| High | 15.12 |
| Medium | 17.48 |
| high | 17.91 |
| medium | 17.05 |
| neutral | 17.12 |

**Average MetricX-24 by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| neutral | 18.62 |
| correct_linguistic_analysis | 18.00 |
| TRANSLATION_ATTEMPT | 17.37 |
| REPETITION | 17.25 |
| CORRECT_LINGUISTIC_ANALYSIS | 17.20 |
| NONE | 16.33 |

**Average MetricX-24 by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| 0 | 17.62 |
| low | 17.00 |
| none | 17.34 |

---

## 8. Key Insights

- **Best performing trace type**: NONE (BLEU: 6.98)
- **Worst performing trace type**: correct_linguistic_analysis (BLEU: 0.69)
- **Performance gap**: 908.2% improvement from worst to best

- **Most common trace type**: CORRECT_LINGUISTIC_ANALYSIS (30 examples, 54.5%)
- **Average difficulty score**: 3.31/5.0

---

*Analysis generated from evaluations/comprehensive_cot_eval/Xhosa_Lithuanian/gemma-3-1b-it/Xhosa_to_Lithuanian_0_shot_seed_42_identity_None_0_0_0/phase2_annotations.jsonl*
