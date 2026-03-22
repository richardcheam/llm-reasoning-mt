# Phase 2 Comprehensive Analysis

**Total Examples Analyzed**: 64

---

## 1. Difficulty Distribution

Distribution of translation difficulty scores (1=easiest, 5=hardest):

| Difficulty Score | Count | Percentage |
|-----------------|-------|------------|
| 1 | 5 | 7.8% |
| 2 | 19 | 29.7% |
| 3 | 36 | 56.2% |
| 4 | 1 | 1.6% |
| 5 | 3 | 4.7% |

## 2. Linguistic Phenomena Frequencies

Frequency of linguistic phenomena across 64 examples:

| Phenomenon | Count | Percentage |
|------------|-------|------------|
| long_distance_dependency | 55 | 85.9% |
| named_entities | 50 | 78.1% |
| complex_syntax | 39 | 60.9% |

## 3. Primary Trace Type Distribution

Distribution of reasoning trace types (n=64):

| Trace Type | Count | Percentage |
|------------|-------|------------|
| TRANSLATION_ATTEMPT | 30 | 46.9% |
| neutral | 14 | 21.9% |
| NONE | 12 | 18.8% |
| CORRECT_LINGUISTIC_ANALYSIS | 5 | 7.8% |
| correction | 1 | 1.6% |
| translation_attempt | 1 | 1.6% |
| REVISION_NEEDED | 1 | 1.6% |

## 4. Trace Usefulness Distribution

Distribution of trace usefulness ratings:

| Usefulness Level | Count | Percentage |
|------------------|-------|------------|
| High | 3 | 4.7% |
| Medium | 1 | 1.6% |
| helpful | 1 | 1.6% |
| high | 2 | 3.1% |
| medium | 32 | 50.0% |
| neutral | 25 | 39.1% |

## 5. Trace-Translation Overlap Distribution

Distribution of overlap between reasoning traces and translations:

| Overlap Level | Count | Percentage |
|---------------|-------|------------|
| low | 1 | 14.3% |
| none | 6 | 85.7% |

## 6. Cross-Tabulations

### 6.1 Difficulty × Trace Type

| Difficulty | CORRECT_LINGUISTIC_ANALYSIS | NONE | REVISION_NEEDED | TRANSLATION_ATTEMPT | correction | neutral | translation_attempt |
|---|---|---|---|---|---|---|---|
| 1 | 0 | 2 | 0 | 0 | 0 | 3 | 0 |
| 2 | 0 | 6 | 0 | 5 | 0 | 7 | 1 |
| 3 | 2 | 4 | 1 | 24 | 1 | 4 | 0 |
| 4 | 0 | 0 | 0 | 1 | 0 | 0 | 0 |
| 5 | 3 | 0 | 0 | 0 | 0 | 0 | 0 |

### 6.2 Trace Type × Usefulness

| Trace Type | High | Medium | helpful | high | medium | neutral |
|---|---|---|---|---|---|---|
| CORRECT_LINGUISTIC_ANALYSIS | 3 | 0 | 0 | 1 | 1 | 0 |
| NONE | 0 | 0 | 1 | 0 | 1 | 10 |
| REVISION_NEEDED | 0 | 0 | 0 | 0 | 0 | 1 |
| TRANSLATION_ATTEMPT | 0 | 1 | 0 | 1 | 24 | 4 |
| correction | 0 | 0 | 0 | 0 | 1 | 0 |
| neutral | 0 | 0 | 0 | 0 | 5 | 9 |
| translation_attempt | 0 | 0 | 0 | 0 | 0 | 1 |

## 7. Translation Quality Correlations

### chrF++ Metric

**Average chrF++ by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| High | 31.47 |
| Medium | 38.88 |
| helpful | 24.24 |
| high | 18.53 |
| medium | 19.67 |
| neutral | 17.23 |

**Average chrF++ by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| correction | 27.50 |
| NONE | 24.09 |
| CORRECT_LINGUISTIC_ANALYSIS | 22.23 |
| TRANSLATION_ATTEMPT | 19.14 |
| neutral | 16.11 |
| REVISION_NEEDED | 13.90 |
| translation_attempt | 13.16 |

**Average chrF++ by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| low | 38.88 |
| none | 20.70 |

---

### COMET Metric

**Average COMET by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| High | 0.66 |
| Medium | 0.76 |
| helpful | 0.66 |
| high | 0.68 |
| medium | 0.60 |
| neutral | 0.57 |

**Average COMET by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| NONE | 0.64 |
| CORRECT_LINGUISTIC_ANALYSIS | 0.61 |
| TRANSLATION_ATTEMPT | 0.60 |
| correction | 0.58 |
| neutral | 0.57 |
| translation_attempt | 0.46 |
| REVISION_NEEDED | 0.41 |

**Average COMET by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| low | 0.76 |
| none | 0.51 |

---

### BLEU Metric

**Average BLEU by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| High | 11.86 |
| Medium | 17.63 |
| helpful | 2.86 |
| high | 17.28 |
| medium | 4.54 |
| neutral | 5.34 |

**Average BLEU by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| NONE | 9.78 |
| CORRECT_LINGUISTIC_ANALYSIS | 7.39 |
| TRANSLATION_ATTEMPT | 4.97 |
| correction | 4.27 |
| neutral | 4.10 |
| translation_attempt | 3.18 |
| REVISION_NEEDED | 1.24 |

**Average BLEU by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| low | 17.63 |
| none | 3.44 |

---

### MetricX-24 Metric

**Average MetricX-24 by Trace Usefulness**

| Usefulness Level | Average Score |
|------------------|---------------|
| High | 11.14 |
| Medium | 9.50 |
| helpful | 10.81 |
| high | 10.34 |
| medium | 12.70 |
| neutral | 12.83 |

**Average MetricX-24 by Trace Type**

| Trace Type | Average Score |
|------------|---------------|
| REVISION_NEEDED | 17.25 |
| correction | 17.00 |
| translation_attempt | 16.88 |
| neutral | 12.85 |
| CORRECT_LINGUISTIC_ANALYSIS | 12.76 |
| TRANSLATION_ATTEMPT | 12.55 |
| NONE | 10.85 |

**Average MetricX-24 by Trace-Translation Overlap**

| Overlap Level | Average Score |
|---------------|---------------|
| low | 9.50 |
| none | 14.25 |

---

## 8. Key Insights

- **Best performing trace type**: NONE (BLEU: 9.78)
- **Worst performing trace type**: REVISION_NEEDED (BLEU: 1.24)
- **Performance gap**: 687.7% improvement from worst to best

- **Most common trace type**: TRANSLATION_ATTEMPT (30 examples, 46.9%)
- **Average difficulty score**: 2.66/5.0

---

*Analysis generated from evaluations/comprehensive_cot_eval/Finnish_Turkish/gemma-3-1b-it/Finnish_to_Turkish_0_shot_seed_42_identity_None_0_0_0/phase2_annotations.jsonl*
