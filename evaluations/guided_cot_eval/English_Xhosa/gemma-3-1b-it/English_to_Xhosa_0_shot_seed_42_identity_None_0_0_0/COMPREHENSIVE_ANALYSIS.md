# Phase 2 Comprehensive Analysis

**Total Examples Analyzed**: 64

---

## 1. Difficulty Distribution

Distribution of translation difficulty scores (1=easiest, 5=hardest):

| Difficulty Score | Count | Percentage |
|-----------------|-------|------------|
| 2 | 1 | 2.4% |
| 3 | 33 | 78.6% |
| 4 | 6 | 14.3% |
| 5 | 2 | 4.8% |

## 2. Linguistic Phenomena Frequencies

Frequency of linguistic phenomena across 42 examples:

| Phenomenon | Count | Percentage |
|------------|-------|------------|
| long_distance_dependency | 42 | 100.0% |
| complex_syntax | 34 | 81.0% |
| named_entities | 18 | 42.9% |
| ambiguity | 2 | 4.8% |
| idiom | 2 | 4.8% |
| figurative_language | 2 | 4.8% |

## 3. Primary Trace Type Distribution

Distribution of reasoning trace types (n=42):

| Trace Type | Count | Percentage |
|------------|-------|------------|
| TRANSLATION_ATTEMPT | 34 | 81.0% |
| CORRECT_LINGUISTIC_ANALYSIS | 3 | 7.1% |
| NONE | 3 | 7.1% |
| REPETITION | 1 | 2.4% |
| correct_linguistic_analysis | 1 | 2.4% |

## 4. Trace Usefulness Distribution

Distribution of trace usefulness ratings:

| Usefulness Level | Count | Percentage |
|------------------|-------|------------|
| 2 | 1 | 2.4% |
| High | 2 | 4.8% |
| Medium | 2 | 4.8% |
| high | 1 | 2.4% |
| medium | 35 | 83.3% |
| neutral | 1 | 2.4% |

## 5. Trace-Translation Overlap Distribution

Distribution of overlap between reasoning traces and translations:

| Overlap Level | Count | Percentage |
|---------------|-------|------------|
| 0 | 1 | 2.6% |
| low | 1 | 2.6% |
| none | 36 | 94.7% |

## 6. Cross-Tabulations

### 6.1 Difficulty × Trace Type

| Difficulty | CORRECT_LINGUISTIC_ANALYSIS | NONE | REPETITION | TRANSLATION_ATTEMPT | correct_linguistic_analysis |
|---|---|---|---|---|---|
| 2 | 0 | 1 | 0 | 0 | 0 |
| 3 | 3 | 2 | 1 | 26 | 1 |
| 4 | 0 | 0 | 0 | 6 | 0 |
| 5 | 0 | 0 | 0 | 2 | 0 |

### 6.2 Trace Type × Usefulness

| Trace Type | 2 | High | Medium | high | medium | neutral |
|---|---|---|---|---|---|---|
| CORRECT_LINGUISTIC_ANALYSIS | 0 | 0 | 0 | 0 | 3 | 0 |
| NONE | 1 | 0 | 0 | 0 | 1 | 1 |
| REPETITION | 0 | 0 | 0 | 0 | 1 | 0 |
| TRANSLATION_ATTEMPT | 0 | 2 | 2 | 1 | 29 | 0 |
| correct_linguistic_analysis | 0 | 0 | 0 | 0 | 1 | 0 |

## 7. Translation Quality Correlations

### chrF++ Metric

**Average chrF++ by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 2 | 11.44 |
| High | 7.75 |
| Medium | 13.34 |
| high | 13.96 |
| medium | 13.32 |
| neutral | 16.55 |

**Average chrF++ by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| CORRECT_LINGUISTIC_ANALYSIS | 22.54 |
| correct_linguistic_analysis | 18.61 |
| NONE | 14.60 |
| TRANSLATION_ATTEMPT | 12.03 |
| REPETITION | 11.19 |

**Average chrF++ by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| 0 | 11.44 |
| low | 6.22 |
| none | 13.25 |

---

### MetricX-24 Metric

**Average MetricX-24 by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 2 | 14.19 |
| High | 16.53 |
| Medium | 15.50 |
| high | 17.50 |
| medium | 14.84 |
| neutral | 13.94 |

**Average MetricX-24 by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| REPETITION | 17.38 |
| TRANSLATION_ATTEMPT | 15.91 |
| NONE | 12.23 |
| correct_linguistic_analysis | 9.50 |
| CORRECT_LINGUISTIC_ANALYSIS | 8.16 |

**Average MetricX-24 by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| 0 | 14.19 |
| low | 15.56 |
| none | 15.05 |

---

### BLEU Metric

**Average BLEU by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 2 | 1.29 |
| High | 0.96 |
| Medium | 2.28 |
| high | 1.82 |
| medium | 2.49 |
| neutral | 13.50 |

**Average BLEU by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| NONE | 6.19 |
| correct_linguistic_analysis | 4.51 |
| CORRECT_LINGUISTIC_ANALYSIS | 3.65 |
| REPETITION | 2.72 |
| TRANSLATION_ATTEMPT | 2.16 |

**Average BLEU by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| 0 | 1.29 |
| low | 0.55 |
| none | 2.44 |

---

### COMET Metric

**Average COMET by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 2 | 0.45 |
| High | 0.38 |
| Medium | 0.36 |
| high | 0.46 |
| medium | 0.40 |
| neutral | 0.60 |

**Average COMET by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| correct_linguistic_analysis | 0.53 |
| NONE | 0.51 |
| REPETITION | 0.45 |
| CORRECT_LINGUISTIC_ANALYSIS | 0.45 |
| TRANSLATION_ATTEMPT | 0.39 |

**Average COMET by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| 0 | 0.45 |
| low | 0.34 |
| none | 0.40 |

---

## 8. Key Insights

- **Best performing trace type**: NONE (BLEU: 6.19)
- **Worst performing trace type**: TRANSLATION_ATTEMPT (BLEU: 2.16)
- **Performance gap**: 186.1% improvement from worst to best

- **Most common trace type**: TRANSLATION_ATTEMPT (34 examples, 81.0%)
- **Average difficulty score**: 3.21/5.0

---

*Analysis generated from evaluations/guided_cot_eval/English_Xhosa/gemma-3-1b-it/English_to_Xhosa_0_shot_seed_42_identity_None_0_0_0/phase2_annotations.jsonl*
