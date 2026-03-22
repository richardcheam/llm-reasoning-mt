# Phase 2 Comprehensive Analysis

**Total Examples Analyzed**: 64

---

## 1. Difficulty Distribution

Distribution of translation difficulty scores (1=easiest, 5=hardest):

| Difficulty Score | Count | Percentage |
|-----------------|-------|------------|
| 2 | 7 | 12.1% |
| 3 | 49 | 84.5% |
| 4 | 2 | 3.4% |

## 2. Linguistic Phenomena Frequencies

Frequency of linguistic phenomena across 58 examples:

| Phenomenon | Count | Percentage |
|------------|-------|------------|
| long_distance_dependency | 58 | 100.0% |
| complex_syntax | 48 | 82.8% |
| named_entities | 40 | 69.0% |
| figurative_language | 1 | 1.7% |

## 3. Primary Trace Type Distribution

Distribution of reasoning trace types (n=58):

| Trace Type | Count | Percentage |
|------------|-------|------------|
| TRANSLATION_ATTEMPT | 27 | 46.6% |
| NONE | 10 | 17.2% |
| CORRECT_LINGUISTIC_ANALYSIS | 9 | 15.5% |
| neutral | 8 | 13.8% |
| correct_linguistic_analysis | 3 | 5.2% |
| VACUOUS_FILLER | 1 | 1.7% |

## 4. Trace Usefulness Distribution

Distribution of trace usefulness ratings:

| Usefulness Level | Count | Percentage |
|------------------|-------|------------|
| high | 3 | 5.2% |
| medium | 44 | 75.9% |
| neutral | 11 | 19.0% |

## 5. Trace-Translation Overlap Distribution

Distribution of overlap between reasoning traces and translations:

| Overlap Level | Count | Percentage |
|---------------|-------|------------|
| low | 1 | 2.9% |
| none | 33 | 97.1% |

## 6. Cross-Tabulations

### 6.1 Difficulty × Trace Type

| Difficulty | CORRECT_LINGUISTIC_ANALYSIS | NONE | TRANSLATION_ATTEMPT | VACUOUS_FILLER | correct_linguistic_analysis | neutral |
|---|---|---|---|---|---|---|
| 2 | 0 | 0 | 0 | 1 | 1 | 5 |
| 3 | 9 | 10 | 25 | 0 | 2 | 3 |
| 4 | 0 | 0 | 2 | 0 | 0 | 0 |

### 6.2 Trace Type × Usefulness

| Trace Type | high | medium | neutral |
|---|---|---|---|
| CORRECT_LINGUISTIC_ANALYSIS | 3 | 6 | 0 |
| NONE | 0 | 6 | 4 |
| TRANSLATION_ATTEMPT | 0 | 27 | 0 |
| VACUOUS_FILLER | 0 | 0 | 1 |
| correct_linguistic_analysis | 0 | 2 | 1 |
| neutral | 0 | 3 | 5 |

## 7. Translation Quality Correlations

### COMET Metric

**Average COMET by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| high | 0.89 |
| medium | 0.80 |
| neutral | 0.87 |

**Average COMET by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| correct_linguistic_analysis | 0.90 |
| NONE | 0.87 |
| neutral | 0.86 |
| CORRECT_LINGUISTIC_ANALYSIS | 0.84 |
| VACUOUS_FILLER | 0.78 |
| TRANSLATION_ATTEMPT | 0.77 |

**Average COMET by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| low | 0.71 |
| none | 0.77 |

---

### MetricX-24 Metric

**Average MetricX-24 by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| high | 2.15 |
| medium | 4.06 |
| neutral | 3.43 |

**Average MetricX-24 by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| VACUOUS_FILLER | 7.16 |
| TRANSLATION_ATTEMPT | 4.75 |
| neutral | 3.65 |
| CORRECT_LINGUISTIC_ANALYSIS | 3.06 |
| NONE | 2.53 |
| correct_linguistic_analysis | 1.85 |

**Average MetricX-24 by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| low | 4.44 |
| none | 4.69 |

---

### BLEU Metric

**Average BLEU by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| high | 42.13 |
| medium | 32.20 |
| neutral | 28.92 |

**Average BLEU by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| NONE | 42.50 |
| correct_linguistic_analysis | 40.57 |
| CORRECT_LINGUISTIC_ANALYSIS | 32.34 |
| neutral | 31.12 |
| TRANSLATION_ATTEMPT | 28.10 |
| VACUOUS_FILLER | 16.15 |

**Average BLEU by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| low | 19.34 |
| none | 25.29 |

---

### chrF++ Metric

**Average chrF++ by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| high | 68.62 |
| medium | 52.75 |
| neutral | 51.96 |

**Average chrF++ by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| NONE | 60.18 |
| correct_linguistic_analysis | 57.40 |
| CORRECT_LINGUISTIC_ANALYSIS | 56.25 |
| neutral | 55.38 |
| TRANSLATION_ATTEMPT | 49.30 |
| VACUOUS_FILLER | 44.18 |

**Average chrF++ by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| low | 43.88 |
| none | 47.98 |

---

## 8. Key Insights

- **Best performing trace type**: NONE (BLEU: 42.50)
- **Worst performing trace type**: VACUOUS_FILLER (BLEU: 16.15)
- **Performance gap**: 163.2% improvement from worst to best

- **Most common trace type**: TRANSLATION_ATTEMPT (27 examples, 46.6%)
- **Average difficulty score**: 2.91/5.0

---

*Analysis generated from evaluations/guided_cot_eval/English_French/gemma-3-1b-it/English_to_French_0_shot_seed_42_identity_None_0_0_0/phase2_annotations.jsonl*
