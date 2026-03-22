# Phase 2 Comprehensive Analysis

**Total Examples Analyzed**: 64

---

## 1. Difficulty Distribution

Distribution of translation difficulty scores (1=easiest, 5=hardest):

| Difficulty Score | Count | Percentage |
|-----------------|-------|------------|
| 1 | 8 | 12.5% |
| 2 | 22 | 34.4% |
| 3 | 31 | 48.4% |
| 5 | 3 | 4.7% |

## 2. Linguistic Phenomena Frequencies

Frequency of linguistic phenomena across 64 examples:

| Phenomenon | Count | Percentage |
|------------|-------|------------|
| long_distance_dependency | 53 | 82.8% |
| named_entities | 47 | 73.4% |
| complex_syntax | 36 | 56.2% |

## 3. Primary Trace Type Distribution

Distribution of reasoning trace types (n=64):

| Trace Type | Count | Percentage |
|------------|-------|------------|
| TRANSLATION_ATTEMPT | 23 | 35.9% |
| NONE | 18 | 28.1% |
| neutral | 16 | 25.0% |
| null | 4 | 6.2% |
| CORRECT_LINGUISTIC_ANALYSIS | 2 | 3.1% |
| translation_attempt | 1 | 1.6% |

## 4. Trace Usefulness Distribution

Distribution of trace usefulness ratings:

| Usefulness Level | Count | Percentage |
|------------------|-------|------------|
| high | 6 | 9.4% |
| medium | 26 | 40.6% |
| neutral | 32 | 50.0% |

## 5. Trace-Translation Overlap Distribution

Distribution of overlap between reasoning traces and translations:

| Overlap Level | Count | Percentage |
|---------------|-------|------------|
| none | 13 | 100.0% |

## 6. Cross-Tabulations

### 6.1 Difficulty × Trace Type

| Difficulty | CORRECT_LINGUISTIC_ANALYSIS | NONE | TRANSLATION_ATTEMPT | neutral | null | translation_attempt |
|---|---|---|---|---|---|---|
| 1 | 0 | 0 | 0 | 4 | 4 | 0 |
| 2 | 0 | 9 | 2 | 11 | 0 | 0 |
| 3 | 2 | 8 | 19 | 1 | 0 | 1 |
| 5 | 0 | 1 | 2 | 0 | 0 | 0 |

### 6.2 Trace Type × Usefulness

| Trace Type | high | medium | neutral |
|---|---|---|---|
| CORRECT_LINGUISTIC_ANALYSIS | 1 | 1 | 0 |
| NONE | 1 | 3 | 14 |
| TRANSLATION_ATTEMPT | 4 | 18 | 1 |
| neutral | 0 | 3 | 13 |
| null | 0 | 0 | 4 |
| translation_attempt | 0 | 1 | 0 |

## 7. Translation Quality Correlations

### BLEU Metric

**Average BLEU by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| high | 19.34 |
| medium | 20.60 |
| neutral | 26.10 |

**Average BLEU by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| CORRECT_LINGUISTIC_ANALYSIS | 32.13 |
| neutral | 26.75 |
| NONE | 24.29 |
| null | 24.01 |
| TRANSLATION_ATTEMPT | 19.26 |
| translation_attempt | 18.33 |

**Average BLEU by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| none | 19.32 |

---

### COMET Metric

**Average COMET by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| high | 0.74 |
| medium | 0.78 |
| neutral | 0.76 |

**Average COMET by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| CORRECT_LINGUISTIC_ANALYSIS | 0.84 |
| null | 0.79 |
| neutral | 0.79 |
| NONE | 0.77 |
| TRANSLATION_ATTEMPT | 0.74 |
| translation_attempt | 0.72 |

**Average COMET by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| none | 0.76 |

---

### MetricX-24 Metric

**Average MetricX-24 by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| high | 5.40 |
| medium | 4.48 |
| neutral | 5.85 |

**Average MetricX-24 by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| NONE | 6.17 |
| TRANSLATION_ATTEMPT | 5.38 |
| neutral | 4.65 |
| null | 4.49 |
| translation_attempt | 3.64 |
| CORRECT_LINGUISTIC_ANALYSIS | 2.68 |

**Average MetricX-24 by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| none | 5.29 |

---

### chrF++ Metric

**Average chrF++ by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| high | 42.15 |
| medium | 43.60 |
| neutral | 44.55 |

**Average chrF++ by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| CORRECT_LINGUISTIC_ANALYSIS | 53.33 |
| null | 51.95 |
| TRANSLATION_ATTEMPT | 43.53 |
| neutral | 43.24 |
| NONE | 42.80 |
| translation_attempt | 34.23 |

**Average chrF++ by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| none | 43.24 |

---

## 8. Key Insights

- **Best performing trace type**: CORRECT_LINGUISTIC_ANALYSIS (BLEU: 32.13)
- **Worst performing trace type**: translation_attempt (BLEU: 18.33)
- **Performance gap**: 75.3% improvement from worst to best

- **Most common trace type**: TRANSLATION_ATTEMPT (23 examples, 35.9%)
- **Average difficulty score**: 2.50/5.0

---

*Analysis generated from evaluations/comprehensive_cot_eval/German_French/gemma-3-1b-it/German_to_French_0_shot_seed_42_identity_None_0_0_0/phase2_annotations.jsonl*
