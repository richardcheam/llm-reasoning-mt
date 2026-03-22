# Phase 2 Comprehensive Analysis

**Total Examples Analyzed**: 64

---

## 1. Difficulty Distribution

Distribution of translation difficulty scores (1=easiest, 5=hardest):

| Difficulty Score | Count | Percentage |
|-----------------|-------|------------|
| 1 | 3 | 4.7% |
| 2 | 33 | 51.6% |
| 3 | 23 | 35.9% |
| 4 | 4 | 6.2% |
| 5 | 1 | 1.6% |

## 2. Linguistic Phenomena Frequencies

Frequency of linguistic phenomena across 64 examples:

| Phenomenon | Count | Percentage |
|------------|-------|------------|
| named_entities | 52 | 81.2% |
| long_distance_dependency | 48 | 75.0% |
| complex_syntax | 19 | 29.7% |
| ambiguity | 1 | 1.6% |
| idiom | 1 | 1.6% |
| figurative_language | 1 | 1.6% |

## 3. Primary Trace Type Distribution

Distribution of reasoning trace types (n=64):

| Trace Type | Count | Percentage |
|------------|-------|------------|
| neutral | 24 | 37.5% |
| NONE | 19 | 29.7% |
| TRANSLATION_ATTEMPT | 11 | 17.2% |
| CORRECT_LINGUISTIC_ANALYSIS | 6 | 9.4% |
| correct_linguistic_analysis | 2 | 3.1% |
| VACUOUS_FILLER | 1 | 1.6% |
| REASONING | 1 | 1.6% |

## 4. Trace Usefulness Distribution

Distribution of trace usefulness ratings:

| Usefulness Level | Count | Percentage |
|------------------|-------|------------|
| 1 | 1 | 1.6% |
| HIGH | 1 | 1.6% |
| Neutral | 1 | 1.6% |
| high | 16 | 25.0% |
| medium | 16 | 25.0% |
| neutral | 29 | 45.3% |

## 5. Trace-Translation Overlap Distribution

Distribution of overlap between reasoning traces and translations:

| Overlap Level | Count | Percentage |
|---------------|-------|------------|
| none | 1 | 100.0% |

## 6. Cross-Tabulations

### 6.1 Difficulty × Trace Type

| Difficulty | CORRECT_LINGUISTIC_ANALYSIS | NONE | REASONING | TRANSLATION_ATTEMPT | VACUOUS_FILLER | correct_linguistic_analysis | neutral |
|---|---|---|---|---|---|---|---|
| 1 | 1 | 2 | 0 | 0 | 0 | 0 | 0 |
| 2 | 4 | 7 | 0 | 0 | 1 | 1 | 20 |
| 3 | 1 | 8 | 0 | 9 | 0 | 1 | 4 |
| 4 | 0 | 2 | 1 | 1 | 0 | 0 | 0 |
| 5 | 0 | 0 | 0 | 1 | 0 | 0 | 0 |

### 6.2 Trace Type × Usefulness

| Trace Type | 1 | HIGH | Neutral | high | medium | neutral |
|---|---|---|---|---|---|---|
| CORRECT_LINGUISTIC_ANALYSIS | 0 | 0 | 0 | 6 | 0 | 0 |
| NONE | 0 | 1 | 1 | 3 | 5 | 9 |
| REASONING | 0 | 0 | 0 | 1 | 0 | 0 |
| TRANSLATION_ATTEMPT | 0 | 0 | 0 | 3 | 8 | 0 |
| VACUOUS_FILLER | 0 | 0 | 0 | 0 | 0 | 1 |
| correct_linguistic_analysis | 0 | 0 | 0 | 2 | 0 | 0 |
| neutral | 1 | 0 | 0 | 1 | 3 | 19 |

## 7. Translation Quality Correlations

### chrF++ Metric

**Average chrF++ by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 1 | 20.78 |
| HIGH | 24.72 |
| Neutral | 56.45 |
| high | 46.74 |
| medium | 37.36 |
| neutral | 43.38 |

**Average chrF++ by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| VACUOUS_FILLER | 57.71 |
| CORRECT_LINGUISTIC_ANALYSIS | 56.68 |
| correct_linguistic_analysis | 47.29 |
| neutral | 42.77 |
| REASONING | 41.88 |
| NONE | 39.83 |
| TRANSLATION_ATTEMPT | 35.27 |

**Average chrF++ by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| none | 20.78 |

---

### MetricX-24 Metric

**Average MetricX-24 by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 1 | 7.78 |
| HIGH | 12.38 |
| Neutral | 1.63 |
| high | 6.33 |
| medium | 6.43 |
| neutral | 5.43 |

**Average MetricX-24 by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| VACUOUS_FILLER | 10.31 |
| REASONING | 9.44 |
| TRANSLATION_ATTEMPT | 7.43 |
| CORRECT_LINGUISTIC_ANALYSIS | 6.09 |
| neutral | 5.63 |
| NONE | 5.46 |
| correct_linguistic_analysis | 3.23 |

**Average MetricX-24 by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| none | 7.78 |

---

### BLEU Metric

**Average BLEU by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 1 | 2.46 |
| HIGH | 11.68 |
| Neutral | 33.80 |
| high | 22.01 |
| medium | 13.08 |
| neutral | 20.94 |

**Average BLEU by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| CORRECT_LINGUISTIC_ANALYSIS | 34.97 |
| correct_linguistic_analysis | 21.79 |
| neutral | 21.78 |
| REASONING | 19.82 |
| NONE | 15.80 |
| TRANSLATION_ATTEMPT | 10.04 |
| VACUOUS_FILLER | 9.85 |

**Average BLEU by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| none | 2.46 |

---

### COMET Metric

**Average COMET by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| 1 | 0.79 |
| HIGH | 0.76 |
| Neutral | 0.88 |
| high | 0.85 |
| medium | 0.81 |
| neutral | 0.83 |

**Average COMET by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| CORRECT_LINGUISTIC_ANALYSIS | 0.87 |
| VACUOUS_FILLER | 0.87 |
| correct_linguistic_analysis | 0.87 |
| neutral | 0.84 |
| NONE | 0.83 |
| TRANSLATION_ATTEMPT | 0.81 |
| REASONING | 0.70 |

**Average COMET by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| none | 0.79 |

---

## 8. Key Insights

- **Best performing trace type**: CORRECT_LINGUISTIC_ANALYSIS (BLEU: 34.97)
- **Worst performing trace type**: VACUOUS_FILLER (BLEU: 9.85)
- **Performance gap**: 255.1% improvement from worst to best

- **Most common trace type**: neutral (24 examples, 37.5%)
- **Average difficulty score**: 2.48/5.0

---

*Analysis generated from evaluations/comprehensive_cot_eval/Turkish_English/gemma-3-1b-it/Turkish_to_English_0_shot_seed_42_identity_None_0_0_0/phase2_annotations.jsonl*
