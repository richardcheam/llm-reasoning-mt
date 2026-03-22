# Comprehensive Linguistic Analysis: Generic CoT vs Guided CoT

**Analysis Date**: 2026-03-22

**Language Pairs Analyzed**: 24/24

**Model**: google/gemma-3-1b-it

**Evaluation Setup**: Each language pair evaluated on 64 translation examples with Phase 2 linguistic annotation

---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [Aggregate Statistics](#2-aggregate-statistics-across-all-language-pairs)
3. [Language Pair Detailed Comparisons](#3-language-pair-detailed-comparisons)
4. [CoT Paradox Analysis](#4-cot-paradox-analysis)
5. [Linguistic Expert Interpretation Guide](#5-linguistic-expert-interpretation-guide)

---

## 1. Executive Summary

### Key Findings

1. **Empty Trace Reduction**: Guided CoT reduces empty traces (NONE) by **7.9 percentage points** (Generic: 23.2%, Guided: 15.3%)

2. **Translation Attempt Increase**: Guided CoT increases translation attempts by **13.8pp** (Generic: 31.6%, Guided: 45.4%)

3. **Linguistic Analysis Increase**: Guided CoT increases correct linguistic analysis by **4.5pp** (Generic: 16.3%, Guided: 20.8%)

4. **Translation Quality Impact**:
   - **BLEU**: Generic=11.23, Guided=12.49 (+1.26, +11.3%)
   - **chrF++**: Generic=28.53, Guided=30.39 (+1.87, +6.5%)
   - **COMET**: Generic=0.62, Guided=0.65 (+0.03, +4.2%)
   - **MetricX-24**: Generic=10.61, Guided=10.13 (-0.48, -4.5%)

---

## 2. Aggregate Statistics Across All Language Pairs

### 2.1 Trace Distribution Summary

| Metric | Generic CoT | Guided CoT | Difference |
|--------|-------------|------------|------------|
| Total Examples | 1536 | 1536 | 0 |
| Empty Traces (NONE) | 357 (23.2%) | 235 (15.3%) | -122 (-7.9pp) |
| Translation Attempts | 486 (31.6%) | 698 (45.4%) | +212 (13.8pp) |
| Linguistic Analysis | 251 (16.3%) | 320 (20.8%) | +69 (4.5pp) |
| Neutral/Generic | 324 (21.1%) | 110 (7.2%) | -214 (-13.9pp) |

## 3. Language Pair Detailed Comparisons

### 3.1 English → Finnish

**Examples**: 64 | **Avg Difficulty**: Generic=2.63, Guided=3.05

**Linguistic Phenomena Frequency**:

| Phenomenon | Generic | Guided |
|------------|---------|--------|
| ambiguity | 0.0% | 3.1% |
| complex_syntax | 57.1% | 79.7% |
| figurative_language | 0.0% | 3.1% |
| idiom | 0.0% | 3.1% |
| long_distance_dependency | 85.7% | 100.0% |
| named_entities | 55.6% | 67.2% |

**Trace Type Distribution**:

| Trace Type | Generic Count | Generic % | Guided Count | Guided % | Δ Count | Δ % |
|------------|---------------|-----------|--------------|----------|---------|-----|
| CORRECT_LINGUISTIC_ANALYSIS | 3 | 4.8% | 18 | 28.1% | +15 | +23.3pp |
| NONE | 9 | 14.3% | 5 | 7.8% | -4 | -6.5pp |
| TRANSLATION_ATTEMPT | 28 | 44.4% | 35 | 54.7% | +7 | +10.3pp |
| VACUOUS_FILLER | 3 | 4.8% | 0 | 0.0% | -3 | -4.8pp |
| correct_linguistic_analysis | 0 | 0.0% | 2 | 3.1% | +2 | +3.1pp |
| neutral | 20 | 31.7% | 4 | 6.2% | -16 | -25.5pp |

**Trace Usefulness Distribution**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| 1 | 0.0% | 1.6% | +1.6pp |
| 3 | 0.0% | 1.6% | +1.6pp |
| High | 0.0% | 1.6% | +1.6pp |
| Medium | 1.6% | 4.7% | +3.1pp |
| high | 4.8% | 10.9% | +6.1pp |
| medium | 49.2% | 71.9% | +22.7pp |
| neutral | 44.4% | 7.8% | -36.6pp |

**Translation Quality by Metric**:

<details>
<summary><b>BLEU</b> (click to expand)</summary>

**Overall Average**: Generic=9.712, Guided=11.022 (Δ +1.310)

**By Trace Type**:

| Trace Type | Generic | Guided | Δ |
|------------|---------|--------|---|
| CORRECT_LINGUISTIC_ANALYSIS | 6.450 | 15.300 | +8.850 |
| NONE | 13.490 | 8.930 | -4.560 |
| TRANSLATION_ATTEMPT | 9.360 | 10.410 | +1.050 |
| VACUOUS_FILLER | 3.020 | 0.000 | -3.020 |
| correct_linguistic_analysis | 0.000 | 2.010 | +2.010 |
| neutral | 16.240 | 18.460 | +2.220 |

**By Trace Usefulness**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| 1 | 0.000 | 3.130 | +3.130 |
| 3 | 0.000 | 25.310 | +25.310 |
| High | 0.000 | 13.960 | +13.960 |
| Medium | 8.970 | 9.720 | +0.750 |
| high | 3.700 | 11.710 | +8.010 |
| medium | 10.700 | 10.920 | +0.220 |
| neutral | 13.750 | 21.290 | +7.540 |

**Performance Range**:
- Generic: Best=neutral (16.240), Worst=VACUOUS_FILLER (3.020), Gap=13.220
- Guided: Best=neutral (18.460), Worst=correct_linguistic_analysis (2.010), Gap=16.450

</details>

<details>
<summary><b>chrF++</b> (click to expand)</summary>

**Overall Average**: Generic=30.462, Guided=32.784 (Δ +2.322)

**By Trace Type**:

| Trace Type | Generic | Guided | Δ |
|------------|---------|--------|---|
| CORRECT_LINGUISTIC_ANALYSIS | 30.210 | 38.720 | +8.510 |
| NONE | 33.920 | 33.020 | -0.900 |
| TRANSLATION_ATTEMPT | 33.110 | 34.570 | +1.460 |
| VACUOUS_FILLER | 15.310 | 0.000 | -15.310 |
| correct_linguistic_analysis | 0.000 | 22.380 | +22.380 |
| neutral | 39.760 | 35.230 | -4.530 |

**By Trace Usefulness**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| 1 | 0.000 | 27.130 | +27.130 |
| 3 | 0.000 | 42.480 | +42.480 |
| High | 0.000 | 42.080 | +42.080 |
| Medium | 29.820 | 34.830 | +5.010 |
| high | 20.030 | 37.710 | +17.680 |
| medium | 34.940 | 34.280 | -0.660 |
| neutral | 35.390 | 40.130 | +4.740 |

**Performance Range**:
- Generic: Best=neutral (39.760), Worst=VACUOUS_FILLER (15.310), Gap=24.450
- Guided: Best=CORRECT_LINGUISTIC_ANALYSIS (38.720), Worst=correct_linguistic_analysis (22.380), Gap=16.340

</details>

<details>
<summary><b>COMET</b> (click to expand)</summary>

**Overall Average**: Generic=0.654, Guided=0.748 (Δ +0.094)

**By Trace Type**:

| Trace Type | Generic | Guided | Δ |
|------------|---------|--------|---|
| CORRECT_LINGUISTIC_ANALYSIS | 0.660 | 0.740 | +0.080 |
| NONE | 0.650 | 0.690 | +0.040 |
| TRANSLATION_ATTEMPT | 0.740 | 0.730 | -0.010 |
| VACUOUS_FILLER | 0.400 | 0.000 | -0.400 |
| correct_linguistic_analysis | 0.000 | 0.790 | +0.790 |
| neutral | 0.820 | 0.790 | -0.030 |

**By Trace Usefulness**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| 1 | 0.000 | 0.760 | +0.760 |
| 3 | 0.000 | 0.750 | +0.750 |
| High | 0.000 | 0.790 | +0.790 |
| Medium | 0.730 | 0.850 | +0.120 |
| high | 0.480 | 0.720 | +0.240 |
| medium | 0.750 | 0.720 | -0.030 |
| neutral | 0.730 | 0.810 | +0.080 |

**Performance Range**:
- Generic: Best=neutral (0.820), Worst=VACUOUS_FILLER (0.400), Gap=0.420
- Guided: Best=correct_linguistic_analysis (0.790), Worst=NONE (0.690), Gap=0.100

</details>

<details>
<summary><b>MetricX-24</b> (click to expand)</summary>

**Overall Average**: Generic=10.540, Guided=9.478 (Δ -1.062)

**By Trace Type**:

| Trace Type | Generic | Guided | Δ |
|------------|---------|--------|---|
| CORRECT_LINGUISTIC_ANALYSIS | 13.480 | 9.180 | -4.300 |
| NONE | 10.300 | 12.490 | +2.190 |
| TRANSLATION_ATTEMPT | 9.770 | 9.890 | +0.120 |
| VACUOUS_FILLER | 11.690 | 0.000 | -11.690 |
| correct_linguistic_analysis | 0.000 | 8.520 | +8.520 |
| neutral | 7.460 | 7.310 | -0.150 |

**By Trace Usefulness**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| 1 | 0.000 | 11.560 | +11.560 |
| 3 | 0.000 | 7.690 | +7.690 |
| High | 0.000 | 11.880 | +11.880 |
| Medium | 6.250 | 4.730 | -1.520 |
| high | 14.480 | 9.740 | -4.740 |
| medium | 9.300 | 9.990 | +0.690 |
| neutral | 9.030 | 9.370 | +0.340 |

**Performance Range**:
- Generic: Best=CORRECT_LINGUISTIC_ANALYSIS (13.480), Worst=neutral (7.460), Gap=6.020
- Guided: Best=NONE (12.490), Worst=neutral (7.310), Gap=5.180

</details>

---

### 3.2 English → French

**Examples**: 64 | **Avg Difficulty**: Generic=2.72, Guided=2.91

**Linguistic Phenomena Frequency**:

| Phenomenon | Generic | Guided |
|------------|---------|--------|
| complex_syntax | 59.4% | 82.8% |
| figurative_language | 0.0% | 1.7% |
| long_distance_dependency | 87.5% | 100.0% |
| named_entities | 62.5% | 69.0% |

**Trace Type Distribution**:

| Trace Type | Generic Count | Generic % | Guided Count | Guided % | Δ Count | Δ % |
|------------|---------------|-----------|--------------|----------|---------|-----|
| CORRECT_LINGUISTIC_ANALYSIS | 1 | 1.6% | 9 | 15.5% | +8 | +13.9pp |
| NONE | 25 | 39.1% | 10 | 17.2% | -15 | -21.9pp |
| REPETITION | 1 | 1.6% | 0 | 0.0% | -1 | -1.6pp |
| TRANSLATION_ATTEMPT | 20 | 31.2% | 27 | 46.6% | +7 | +15.4pp |
| VACUOUS_FILLER | 0 | 0.0% | 1 | 1.7% | +1 | +1.7pp |
| correct_linguistic_analysis | 4 | 6.2% | 3 | 5.2% | -1 | -1.0pp |
| neutral | 13 | 20.3% | 8 | 13.8% | -5 | -6.5pp |

**Trace Usefulness Distribution**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| Neutral | 1.6% | 0.0% | -1.6pp |
| helpful | 1.6% | 0.0% | -1.6pp |
| high | 3.1% | 5.2% | +2.1pp |
| medium | 37.5% | 75.9% | +38.4pp |
| neutral | 56.2% | 19.0% | -37.2pp |

**Translation Quality by Metric**:

<details>
<summary><b>BLEU</b> (click to expand)</summary>

**Overall Average**: Generic=30.367, Guided=31.797 (Δ +1.430)

**By Trace Type**:

| Trace Type | Generic | Guided | Δ |
|------------|---------|--------|---|
| CORRECT_LINGUISTIC_ANALYSIS | 7.770 | 32.340 | +24.570 |
| NONE | 36.070 | 42.500 | +6.430 |
| REPETITION | 55.410 | 0.000 | -55.410 |
| TRANSLATION_ATTEMPT | 28.560 | 28.100 | -0.460 |
| VACUOUS_FILLER | 0.000 | 16.150 | +16.150 |
| correct_linguistic_analysis | 31.680 | 40.570 | +8.890 |
| neutral | 22.710 | 31.120 | +8.410 |

**By Trace Usefulness**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| Neutral | 21.870 | 0.000 | -21.870 |
| helpful | 40.310 | 0.000 | -40.310 |
| high | 29.050 | 42.130 | +13.080 |
| medium | 28.230 | 32.200 | +3.970 |
| neutral | 32.230 | 28.920 | -3.310 |

**Performance Range**:
- Generic: Best=REPETITION (55.410), Worst=CORRECT_LINGUISTIC_ANALYSIS (7.770), Gap=47.640
- Guided: Best=NONE (42.500), Worst=VACUOUS_FILLER (16.150), Gap=26.350

</details>

<details>
<summary><b>chrF++</b> (click to expand)</summary>

**Overall Average**: Generic=52.103, Guided=53.782 (Δ +1.678)

**By Trace Type**:

| Trace Type | Generic | Guided | Δ |
|------------|---------|--------|---|
| CORRECT_LINGUISTIC_ANALYSIS | 30.100 | 56.250 | +26.150 |
| NONE | 56.040 | 60.180 | +4.140 |
| REPETITION | 80.120 | 0.000 | -80.120 |
| TRANSLATION_ATTEMPT | 49.530 | 49.300 | -0.230 |
| VACUOUS_FILLER | 0.000 | 44.180 | +44.180 |
| correct_linguistic_analysis | 53.350 | 57.400 | +4.050 |
| neutral | 43.480 | 55.380 | +11.900 |

**By Trace Usefulness**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| Neutral | 47.860 | 0.000 | -47.860 |
| helpful | 59.090 | 0.000 | -59.090 |
| high | 45.570 | 68.620 | +23.050 |
| medium | 50.060 | 52.750 | +2.690 |
| neutral | 52.240 | 51.960 | -0.280 |

**Performance Range**:
- Generic: Best=REPETITION (80.120), Worst=CORRECT_LINGUISTIC_ANALYSIS (30.100), Gap=50.020
- Guided: Best=NONE (60.180), Worst=VACUOUS_FILLER (44.180), Gap=16.000

</details>

<details>
<summary><b>COMET</b> (click to expand)</summary>

**Overall Average**: Generic=0.818, Guided=0.837 (Δ +0.018)

**By Trace Type**:

| Trace Type | Generic | Guided | Δ |
|------------|---------|--------|---|
| CORRECT_LINGUISTIC_ANALYSIS | 0.720 | 0.840 | +0.120 |
| NONE | 0.850 | 0.870 | +0.020 |
| REPETITION | 0.910 | 0.000 | -0.910 |
| TRANSLATION_ATTEMPT | 0.790 | 0.770 | -0.020 |
| VACUOUS_FILLER | 0.000 | 0.780 | +0.780 |
| correct_linguistic_analysis | 0.820 | 0.900 | +0.080 |
| neutral | 0.820 | 0.860 | +0.040 |

**By Trace Usefulness**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| Neutral | 0.790 | 0.000 | -0.790 |
| helpful | 0.940 | 0.000 | -0.940 |
| high | 0.850 | 0.890 | +0.040 |
| medium | 0.800 | 0.800 | 0.000 |
| neutral | 0.840 | 0.870 | +0.030 |

**Performance Range**:
- Generic: Best=REPETITION (0.910), Worst=CORRECT_LINGUISTIC_ANALYSIS (0.720), Gap=0.190
- Guided: Best=correct_linguistic_analysis (0.900), Worst=TRANSLATION_ATTEMPT (0.770), Gap=0.130

</details>

<details>
<summary><b>MetricX-24</b> (click to expand)</summary>

**Overall Average**: Generic=3.763, Guided=3.833 (Δ +0.070)

**By Trace Type**:

| Trace Type | Generic | Guided | Δ |
|------------|---------|--------|---|
| CORRECT_LINGUISTIC_ANALYSIS | 7.030 | 3.060 | -3.970 |
| NONE | 3.050 | 2.530 | -0.520 |
| REPETITION | 1.700 | 0.000 | -1.700 |
| TRANSLATION_ATTEMPT | 4.200 | 4.750 | +0.550 |
| VACUOUS_FILLER | 0.000 | 7.160 | +7.160 |
| correct_linguistic_analysis | 3.660 | 1.850 | -1.810 |
| neutral | 2.940 | 3.650 | +0.710 |

**By Trace Usefulness**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| Neutral | 3.690 | 0.000 | -3.690 |
| helpful | 1.230 | 0.000 | -1.230 |
| high | 4.010 | 2.150 | -1.860 |
| medium | 3.980 | 4.060 | +0.080 |
| neutral | 3.150 | 3.430 | +0.280 |

**Performance Range**:
- Generic: Best=CORRECT_LINGUISTIC_ANALYSIS (7.030), Worst=REPETITION (1.700), Gap=5.330
- Guided: Best=VACUOUS_FILLER (7.160), Worst=correct_linguistic_analysis (1.850), Gap=5.310

</details>

---

### 3.3 English → German

**Examples**: 64 | **Avg Difficulty**: Generic=2.62, Guided=3.03

**Linguistic Phenomena Frequency**:

| Phenomenon | Generic | Guided |
|------------|---------|--------|
| ambiguity | 0.0% | 5.1% |
| complex_syntax | 59.4% | 88.1% |
| figurative_language | 0.0% | 5.1% |
| idiom | 0.0% | 5.1% |
| long_distance_dependency | 84.4% | 100.0% |
| named_entities | 53.1% | 72.9% |

**Trace Type Distribution**:

| Trace Type | Generic Count | Generic % | Guided Count | Guided % | Δ Count | Δ % |
|------------|---------------|-----------|--------------|----------|---------|-----|
| CORRECT_LINGUISTIC_ANALYSIS | 4 | 6.2% | 7 | 11.9% | +3 | +5.7pp |
| NONE | 18 | 28.1% | 9 | 15.3% | -9 | -12.8pp |
| TRANSLATION_ATTEMPT | 20 | 31.2% | 37 | 62.7% | +17 | +31.5pp |
| VACUOUS_FILLER | 1 | 1.6% | 0 | 0.0% | -1 | -1.6pp |
| correct_linguistic_analysis | 1 | 1.6% | 0 | 0.0% | -1 | -1.6pp |
| neutral | 17 | 26.6% | 6 | 10.2% | -11 | -16.4pp |
| null | 3 | 4.7% | 0 | 0.0% | -3 | -4.7pp |

**Trace Usefulness Distribution**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| 1 | 0.0% | 3.4% | +3.4pp |
| 3 | 0.0% | 1.7% | +1.7pp |
| Easy | 1.6% | 0.0% | -1.6pp |
| high | 6.2% | 5.1% | -1.1pp |
| medium | 40.6% | 83.1% | +42.5pp |
| neutral | 51.6% | 6.8% | -44.8pp |

**Translation Quality by Metric**:

<details>
<summary><b>BLEU</b> (click to expand)</summary>

**Overall Average**: Generic=21.720, Guided=23.642 (Δ +1.922)

**By Trace Type**:

| Trace Type | Generic | Guided | Δ |
|------------|---------|--------|---|
| CORRECT_LINGUISTIC_ANALYSIS | 19.910 | 26.260 | +6.350 |
| NONE | 23.910 | 27.120 | +3.210 |
| TRANSLATION_ATTEMPT | 15.650 | 19.740 | +4.090 |
| VACUOUS_FILLER | 2.330 | 0.000 | -2.330 |
| correct_linguistic_analysis | 60.600 | 0.000 | -60.600 |
| neutral | 23.560 | 21.450 | -2.110 |
| null | 6.080 | 0.000 | -6.080 |

**By Trace Usefulness**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| 1 | 0.000 | 21.010 | +21.010 |
| 3 | 0.000 | 21.310 | +21.310 |
| Easy | 29.050 | 0.000 | -29.050 |
| high | 18.120 | 21.520 | +3.400 |
| medium | 18.490 | 21.290 | +2.800 |
| neutral | 21.890 | 28.950 | +7.060 |

**Performance Range**:
- Generic: Best=correct_linguistic_analysis (60.600), Worst=VACUOUS_FILLER (2.330), Gap=58.270
- Guided: Best=NONE (27.120), Worst=TRANSLATION_ATTEMPT (19.740), Gap=7.380

</details>

<details>
<summary><b>chrF++</b> (click to expand)</summary>

**Overall Average**: Generic=44.510, Guided=46.472 (Δ +1.962)

**By Trace Type**:

| Trace Type | Generic | Guided | Δ |
|------------|---------|--------|---|
| CORRECT_LINGUISTIC_ANALYSIS | 46.520 | 49.730 | +3.210 |
| NONE | 42.440 | 48.760 | +6.320 |
| TRANSLATION_ATTEMPT | 40.650 | 43.070 | +2.420 |
| VACUOUS_FILLER | 31.760 | 0.000 | -31.760 |
| correct_linguistic_analysis | 73.180 | 0.000 | -73.180 |
| neutral | 49.470 | 44.330 | -5.140 |
| null | 27.550 | 0.000 | -27.550 |

**By Trace Usefulness**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| 1 | 0.000 | 50.200 | +50.200 |
| 3 | 0.000 | 50.900 | +50.900 |
| Easy | 50.100 | 0.000 | -50.100 |
| high | 45.510 | 47.000 | +1.490 |
| medium | 43.100 | 43.870 | +0.770 |
| neutral | 43.600 | 51.090 | +7.490 |

**Performance Range**:
- Generic: Best=correct_linguistic_analysis (73.180), Worst=null (27.550), Gap=45.630
- Guided: Best=CORRECT_LINGUISTIC_ANALYSIS (49.730), Worst=TRANSLATION_ATTEMPT (43.070), Gap=6.660

</details>

<details>
<summary><b>COMET</b> (click to expand)</summary>

**Overall Average**: Generic=0.786, Guided=0.797 (Δ +0.012)

**By Trace Type**:

| Trace Type | Generic | Guided | Δ |
|------------|---------|--------|---|
| CORRECT_LINGUISTIC_ANALYSIS | 0.810 | 0.830 | +0.020 |
| NONE | 0.870 | 0.800 | -0.070 |
| TRANSLATION_ATTEMPT | 0.770 | 0.800 | +0.030 |
| VACUOUS_FILLER | 0.760 | 0.000 | -0.760 |
| correct_linguistic_analysis | 0.930 | 0.000 | -0.930 |
| neutral | 0.800 | 0.760 | -0.040 |
| null | 0.560 | 0.000 | -0.560 |

**By Trace Usefulness**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| 1 | 0.000 | 0.780 | +0.780 |
| 3 | 0.000 | 0.710 | +0.710 |
| Easy | 0.860 | 0.000 | -0.860 |
| high | 0.820 | 0.780 | -0.040 |
| medium | 0.790 | 0.800 | +0.010 |
| neutral | 0.800 | 0.820 | +0.020 |

**Performance Range**:
- Generic: Best=correct_linguistic_analysis (0.930), Worst=null (0.560), Gap=0.370
- Guided: Best=CORRECT_LINGUISTIC_ANALYSIS (0.830), Worst=neutral (0.760), Gap=0.070

</details>

<details>
<summary><b>MetricX-24</b> (click to expand)</summary>

**Overall Average**: Generic=3.479, Guided=2.895 (Δ -0.584)

**By Trace Type**:

| Trace Type | Generic | Guided | Δ |
|------------|---------|--------|---|
| CORRECT_LINGUISTIC_ANALYSIS | 4.480 | 1.850 | -2.630 |
| NONE | 2.060 | 2.160 | +0.100 |
| TRANSLATION_ATTEMPT | 4.040 | 3.210 | -0.830 |
| VACUOUS_FILLER | 2.720 | 0.000 | -2.720 |
| correct_linguistic_analysis | 1.230 | 0.000 | -1.230 |
| neutral | 2.650 | 4.360 | +1.710 |
| null | 7.170 | 0.000 | -7.170 |

**By Trace Usefulness**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| 1 | 0.000 | 1.870 | +1.870 |
| 3 | 0.000 | 2.940 | +2.940 |
| Easy | 1.590 | 0.000 | -1.590 |
| high | 4.370 | 2.470 | -1.900 |
| medium | 3.660 | 3.150 | -0.510 |
| neutral | 2.790 | 2.220 | -0.570 |

**Performance Range**:
- Generic: Best=null (7.170), Worst=correct_linguistic_analysis (1.230), Gap=5.940
- Guided: Best=neutral (4.360), Worst=CORRECT_LINGUISTIC_ANALYSIS (1.850), Gap=2.510

</details>

---

### 3.4 English → Kazakh

**Examples**: 64 | **Avg Difficulty**: Generic=2.84, Guided=3.11

**Linguistic Phenomena Frequency**:

| Phenomenon | Generic | Guided |
|------------|---------|--------|
| ambiguity | 0.0% | 4.9% |
| complex_syntax | 75.0% | 85.2% |
| figurative_language | 0.0% | 4.9% |
| idiom | 0.0% | 4.9% |
| long_distance_dependency | 92.2% | 98.4% |
| named_entities | 65.6% | 63.9% |

**Trace Type Distribution**:

| Trace Type | Generic Count | Generic % | Guided Count | Guided % | Δ Count | Δ % |
|------------|---------------|-----------|--------------|----------|---------|-----|
| CORRECT_LINGUISTIC_ANALYSIS | 11 | 17.2% | 44 | 72.1% | +33 | +54.9pp |
| NONE | 23 | 35.9% | 6 | 9.8% | -17 | -26.1pp |
| REPETITION | 1 | 1.6% | 0 | 0.0% | -1 | -1.6pp |
| TRANSLATION_ATTEMPT | 14 | 21.9% | 10 | 16.4% | -4 | -5.5pp |
| VACUOUS_FILLER | 1 | 1.6% | 0 | 0.0% | -1 | -1.6pp |
| correct_linguistic_analysis | 3 | 4.7% | 0 | 0.0% | -3 | -4.7pp |
| neutral | 11 | 17.2% | 1 | 1.6% | -10 | -15.6pp |

**Trace Usefulness Distribution**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| 2 | 0.0% | 4.9% | +4.9pp |
| High | 1.6% | 1.6% | 0.0pp |
| Medium | 0.0% | 6.6% | +6.6pp |
| high | 6.2% | 24.6% | +18.4pp |
| medium | 48.4% | 54.1% | +5.7pp |
| neutral | 43.8% | 8.2% | -35.6pp |

**Translation Quality by Metric**:

<details>
<summary><b>BLEU</b> (click to expand)</summary>

**Overall Average**: Generic=3.204, Guided=3.042 (Δ -0.162)

**By Trace Type**:

| Trace Type | Generic | Guided | Δ |
|------------|---------|--------|---|
| CORRECT_LINGUISTIC_ANALYSIS | 3.130 | 4.420 | +1.290 |
| NONE | 4.710 | 3.700 | -1.010 |
| REPETITION | 0.000 | 0.000 | 0.000 |
| TRANSLATION_ATTEMPT | 2.580 | 2.130 | -0.450 |
| VACUOUS_FILLER | 6.240 | 0.000 | -6.240 |
| correct_linguistic_analysis | 1.390 | 0.000 | -1.390 |
| neutral | 4.380 | 1.920 | -2.460 |

**By Trace Usefulness**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| 2 | 0.000 | 4.440 | +4.440 |
| High | 4.650 | 2.040 | -2.610 |
| Medium | 0.000 | 2.120 | +2.120 |
| high | 5.920 | 3.610 | -2.310 |
| medium | 3.110 | 4.270 | +1.160 |
| neutral | 4.030 | 4.200 | +0.170 |

**Performance Range**:
- Generic: Best=VACUOUS_FILLER (6.240), Worst=REPETITION (0.000), Gap=6.240
- Guided: Best=CORRECT_LINGUISTIC_ANALYSIS (4.420), Worst=neutral (1.920), Gap=2.500

</details>

<details>
<summary><b>chrF++</b> (click to expand)</summary>

**Overall Average**: Generic=13.136, Guided=12.395 (Δ -0.741)

**By Trace Type**:

| Trace Type | Generic | Guided | Δ |
|------------|---------|--------|---|
| CORRECT_LINGUISTIC_ANALYSIS | 14.420 | 15.360 | +0.940 |
| NONE | 14.150 | 15.110 | +0.960 |
| REPETITION | 2.250 | 0.000 | -2.250 |
| TRANSLATION_ATTEMPT | 10.860 | 10.450 | -0.410 |
| VACUOUS_FILLER | 21.380 | 0.000 | -21.380 |
| correct_linguistic_analysis | 13.710 | 0.000 | -13.710 |
| neutral | 15.180 | 8.660 | -6.520 |

**By Trace Usefulness**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| 2 | 0.000 | 13.840 | +13.840 |
| High | 15.540 | 11.800 | -3.740 |
| Medium | 0.000 | 10.550 | +10.550 |
| high | 14.670 | 15.290 | +0.620 |
| medium | 12.870 | 14.470 | +1.600 |
| neutral | 14.090 | 15.440 | +1.350 |

**Performance Range**:
- Generic: Best=VACUOUS_FILLER (21.380), Worst=REPETITION (2.250), Gap=19.130
- Guided: Best=CORRECT_LINGUISTIC_ANALYSIS (15.360), Worst=neutral (8.660), Gap=6.700

</details>

<details>
<summary><b>COMET</b> (click to expand)</summary>

**Overall Average**: Generic=0.606, Guided=0.630 (Δ +0.024)

**By Trace Type**:

| Trace Type | Generic | Guided | Δ |
|------------|---------|--------|---|
| CORRECT_LINGUISTIC_ANALYSIS | 0.650 | 0.670 | +0.020 |
| NONE | 0.700 | 0.700 | 0.000 |
| REPETITION | 0.480 | 0.000 | -0.480 |
| TRANSLATION_ATTEMPT | 0.570 | 0.560 | -0.010 |
| VACUOUS_FILLER | 0.650 | 0.000 | -0.650 |
| correct_linguistic_analysis | 0.520 | 0.000 | -0.520 |
| neutral | 0.670 | 0.590 | -0.080 |

**By Trace Usefulness**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| 2 | 0.000 | 0.620 | +0.620 |
| High | 0.820 | 0.640 | -0.180 |
| Medium | 0.000 | 0.480 | +0.480 |
| high | 0.750 | 0.620 | -0.130 |
| medium | 0.600 | 0.680 | +0.080 |
| neutral | 0.680 | 0.700 | +0.020 |

**Performance Range**:
- Generic: Best=NONE (0.700), Worst=REPETITION (0.480), Gap=0.220
- Guided: Best=NONE (0.700), Worst=TRANSLATION_ATTEMPT (0.560), Gap=0.140

</details>

<details>
<summary><b>MetricX-24</b> (click to expand)</summary>

**Overall Average**: Generic=9.126, Guided=8.418 (Δ -0.708)

**By Trace Type**:

| Trace Type | Generic | Guided | Δ |
|------------|---------|--------|---|
| CORRECT_LINGUISTIC_ANALYSIS | 7.070 | 7.850 | +0.780 |
| NONE | 6.100 | 7.230 | +1.130 |
| REPETITION | 15.060 | 0.000 | -15.060 |
| TRANSLATION_ATTEMPT | 8.720 | 10.680 | +1.960 |
| VACUOUS_FILLER | 8.000 | 0.000 | -8.000 |
| correct_linguistic_analysis | 10.740 | 0.000 | -10.740 |
| neutral | 8.190 | 7.910 | -0.280 |

**By Trace Usefulness**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| 2 | 0.000 | 8.450 | +8.450 |
| High | 1.840 | 6.500 | +4.660 |
| Medium | 0.000 | 13.380 | +13.380 |
| high | 6.300 | 8.780 | +2.480 |
| medium | 8.600 | 7.470 | -1.130 |
| neutral | 6.850 | 8.000 | +1.150 |

**Performance Range**:
- Generic: Best=REPETITION (15.060), Worst=NONE (6.100), Gap=8.960
- Guided: Best=TRANSLATION_ATTEMPT (10.680), Worst=NONE (7.230), Gap=3.450

</details>

---

### 3.5 English → Lithuanian

**Examples**: 64 | **Avg Difficulty**: Generic=2.87, Guided=3.17

**Linguistic Phenomena Frequency**:

| Phenomenon | Generic | Guided |
|------------|---------|--------|
| ambiguity | 0.0% | 10.0% |
| complex_syntax | 77.8% | 85.0% |
| figurative_language | 0.0% | 10.0% |
| idiom | 0.0% | 10.0% |
| long_distance_dependency | 93.7% | 98.3% |
| named_entities | 57.1% | 66.7% |

**Trace Type Distribution**:

| Trace Type | Generic Count | Generic % | Guided Count | Guided % | Δ Count | Δ % |
|------------|---------------|-----------|--------------|----------|---------|-----|
| CORRECT_LINGUISTIC_ANALYSIS | 8 | 12.7% | 29 | 48.3% | +21 | +35.6pp |
| NONE | 20 | 31.7% | 2 | 3.3% | -18 | -28.4pp |
| REPETITION | 1 | 1.6% | 0 | 0.0% | -1 | -1.6pp |
| TRANSLATION_ATTEMPT | 13 | 20.6% | 23 | 38.3% | +10 | +17.7pp |
| VACUOUS_FILLER | 1 | 1.6% | 0 | 0.0% | -1 | -1.6pp |
| correct_linguistic_analysis | 8 | 12.7% | 3 | 5.0% | -5 | -7.7pp |
| neutral | 11 | 17.5% | 3 | 5.0% | -8 | -12.5pp |
| null | 1 | 1.6% | 0 | 0.0% | -1 | -1.6pp |

**Trace Usefulness Distribution**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| 2 | 0.0% | 3.3% | +3.3pp |
| 3 | 0.0% | 3.3% | +3.3pp |
| High | 0.0% | 1.7% | +1.7pp |
| Medium | 4.8% | 6.7% | +1.9pp |
| Medium (the translation is understandable but could be improved) | 0.0% | 1.7% | +1.7pp |
| high | 4.8% | 11.7% | +6.9pp |
| medium | 42.9% | 70.0% | +27.1pp |
| neutral | 47.6% | 1.7% | -45.9pp |

**Translation Quality by Metric**:

<details>
<summary><b>BLEU</b> (click to expand)</summary>

**Overall Average**: Generic=6.674, Guided=7.148 (Δ +0.474)

**By Trace Type**:

| Trace Type | Generic | Guided | Δ |
|------------|---------|--------|---|
| CORRECT_LINGUISTIC_ANALYSIS | 4.870 | 4.290 | -0.580 |
| NONE | 5.280 | 5.860 | +0.580 |
| REPETITION | 19.930 | 0.000 | -19.930 |
| TRANSLATION_ATTEMPT | 4.630 | 4.910 | +0.280 |
| VACUOUS_FILLER | 1.350 | 0.000 | -1.350 |
| correct_linguistic_analysis | 3.460 | 1.080 | -2.380 |
| neutral | 11.370 | 19.600 | +8.230 |
| null | 2.500 | 0.000 | -2.500 |

**By Trace Usefulness**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| 2 | 0.000 | 7.260 | +7.260 |
| 3 | 0.000 | 2.130 | +2.130 |
| High | 0.000 | 2.240 | +2.240 |
| Medium | 2.320 | 2.490 | +0.170 |
| Medium (the translation is understandable but could be improved) | 0.000 | 2.220 | +2.220 |
| high | 6.710 | 5.380 | -1.330 |
| medium | 5.010 | 5.640 | +0.630 |
| neutral | 7.290 | 3.140 | -4.150 |

**Performance Range**:
- Generic: Best=REPETITION (19.930), Worst=VACUOUS_FILLER (1.350), Gap=18.580
- Guided: Best=neutral (19.600), Worst=correct_linguistic_analysis (1.080), Gap=18.520

</details>

<details>
<summary><b>chrF++</b> (click to expand)</summary>

**Overall Average**: Generic=24.599, Guided=25.470 (Δ +0.871)

**By Trace Type**:

| Trace Type | Generic | Guided | Δ |
|------------|---------|--------|---|
| CORRECT_LINGUISTIC_ANALYSIS | 22.210 | 24.710 | +2.500 |
| NONE | 24.620 | 27.580 | +2.960 |
| REPETITION | 32.750 | 0.000 | -32.750 |
| TRANSLATION_ATTEMPT | 23.180 | 23.540 | +0.360 |
| VACUOUS_FILLER | 17.670 | 0.000 | -17.670 |
| correct_linguistic_analysis | 21.890 | 17.110 | -4.780 |
| neutral | 31.090 | 34.410 | +3.320 |
| null | 23.380 | 0.000 | -23.380 |

**By Trace Usefulness**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| 2 | 0.000 | 28.910 | +28.910 |
| 3 | 0.000 | 19.450 | +19.450 |
| High | 0.000 | 28.740 | +28.740 |
| Medium | 22.310 | 20.270 | -2.040 |
| Medium (the translation is understandable but could be improved) | 0.000 | 20.650 | +20.650 |
| high | 24.910 | 28.010 | +3.100 |
| medium | 23.440 | 24.250 | +0.810 |
| neutral | 26.260 | 26.170 | -0.090 |

**Performance Range**:
- Generic: Best=REPETITION (32.750), Worst=VACUOUS_FILLER (17.670), Gap=15.080
- Guided: Best=neutral (34.410), Worst=correct_linguistic_analysis (17.110), Gap=17.300

</details>

<details>
<summary><b>COMET</b> (click to expand)</summary>

**Overall Average**: Generic=0.509, Guided=0.468 (Δ -0.041)

**By Trace Type**:

| Trace Type | Generic | Guided | Δ |
|------------|---------|--------|---|
| CORRECT_LINGUISTIC_ANALYSIS | 0.450 | 0.460 | +0.010 |
| NONE | 0.500 | 0.500 | 0.000 |
| REPETITION | 0.660 | 0.000 | -0.660 |
| TRANSLATION_ATTEMPT | 0.450 | 0.410 | -0.040 |
| VACUOUS_FILLER | 0.620 | 0.000 | -0.620 |
| correct_linguistic_analysis | 0.490 | 0.470 | -0.020 |
| neutral | 0.530 | 0.500 | -0.030 |
| null | 0.370 | 0.000 | -0.370 |

**By Trace Usefulness**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| 2 | 0.000 | 0.540 | +0.540 |
| 3 | 0.000 | 0.380 | +0.380 |
| High | 0.000 | 0.390 | +0.390 |
| Medium | 0.390 | 0.420 | +0.030 |
| Medium (the translation is understandable but could be improved) | 0.000 | 0.430 | +0.430 |
| high | 0.660 | 0.480 | -0.180 |
| medium | 0.470 | 0.440 | -0.030 |
| neutral | 0.500 | 0.490 | -0.010 |

**Performance Range**:
- Generic: Best=REPETITION (0.660), Worst=null (0.370), Gap=0.290
- Guided: Best=NONE (0.500), Worst=TRANSLATION_ATTEMPT (0.410), Gap=0.090

</details>

<details>
<summary><b>MetricX-24</b> (click to expand)</summary>

**Overall Average**: Generic=15.078, Guided=15.808 (Δ +0.731)

**By Trace Type**:

| Trace Type | Generic | Guided | Δ |
|------------|---------|--------|---|
| CORRECT_LINGUISTIC_ANALYSIS | 15.540 | 15.660 | +0.120 |
| NONE | 15.260 | 12.500 | -2.760 |
| REPETITION | 14.500 | 0.000 | -14.500 |
| TRANSLATION_ATTEMPT | 17.180 | 17.230 | +0.050 |
| VACUOUS_FILLER | 13.190 | 0.000 | -13.190 |
| correct_linguistic_analysis | 14.480 | 17.710 | +3.230 |
| neutral | 13.720 | 15.940 | +2.220 |
| null | 16.750 | 0.000 | -16.750 |

**By Trace Usefulness**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| 2 | 0.000 | 12.030 | +12.030 |
| 3 | 0.000 | 16.250 | +16.250 |
| High | 0.000 | 17.750 | +17.750 |
| Medium | 18.620 | 17.020 | -1.600 |
| Medium (the translation is understandable but could be improved) | 0.000 | 16.880 | +16.880 |
| high | 7.450 | 15.410 | +7.960 |
| medium | 15.770 | 16.540 | +0.770 |
| neutral | 15.330 | 14.690 | -0.640 |

**Performance Range**:
- Generic: Best=TRANSLATION_ATTEMPT (17.180), Worst=VACUOUS_FILLER (13.190), Gap=3.990
- Guided: Best=correct_linguistic_analysis (17.710), Worst=NONE (12.500), Gap=5.210

</details>

---

### 3.6 English → Turkish

**Examples**: 64 | **Avg Difficulty**: Generic=2.77, Guided=3.03

**Linguistic Phenomena Frequency**:

| Phenomenon | Generic | Guided |
|------------|---------|--------|
| ambiguity | 0.0% | 1.6% |
| complex_syntax | 60.9% | 77.8% |
| figurative_language | 0.0% | 1.6% |
| idiom | 0.0% | 1.6% |
| long_distance_dependency | 89.1% | 100.0% |
| named_entities | 62.5% | 60.3% |

**Trace Type Distribution**:

| Trace Type | Generic Count | Generic % | Guided Count | Guided % | Δ Count | Δ % |
|------------|---------------|-----------|--------------|----------|---------|-----|
| CORRECT_LINGUISTIC_ANALYSIS | 2 | 3.1% | 15 | 23.8% | +13 | +20.7pp |
| NONE | 13 | 20.3% | 15 | 23.8% | +2 | +3.5pp |
| REPETITION | 1 | 1.6% | 2 | 3.2% | +1 | +1.6pp |
| TRANSLATION_ATTEMPT | 23 | 35.9% | 22 | 34.9% | -1 | -1.0pp |
| correct_linguistic_analysis | 1 | 1.6% | 1 | 1.6% | 0 | 0.0pp |
| neutral | 24 | 37.5% | 8 | 12.7% | -16 | -24.8pp |

**Trace Usefulness Distribution**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| 1 | 0.0% | 1.6% | +1.6pp |
| 4 | 1.6% | 0.0% | -1.6pp |
| Easy | 1.6% | 0.0% | -1.6pp |
| High | 1.6% | 3.2% | +1.6pp |
| Medium | 4.7% | 3.2% | -1.5pp |
| high | 4.7% | 6.3% | +1.6pp |
| medium | 37.5% | 71.4% | +33.9pp |
| neutral | 48.4% | 14.3% | -34.1pp |

**Translation Quality by Metric**:

<details>
<summary><b>BLEU</b> (click to expand)</summary>

**Overall Average**: Generic=13.340, Guided=17.163 (Δ +3.823)

**By Trace Type**:

| Trace Type | Generic | Guided | Δ |
|------------|---------|--------|---|
| CORRECT_LINGUISTIC_ANALYSIS | 16.230 | 13.010 | -3.220 |
| NONE | 11.320 | 22.180 | +10.860 |
| REPETITION | 10.610 | 15.070 | +4.460 |
| TRANSLATION_ATTEMPT | 12.600 | 13.200 | +0.600 |
| correct_linguistic_analysis | 11.550 | 29.920 | +18.370 |
| neutral | 17.730 | 9.600 | -8.130 |

**By Trace Usefulness**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| 1 | 0.000 | 6.670 | +6.670 |
| 4 | 28.450 | 0.000 | -28.450 |
| Easy | 13.560 | 0.000 | -13.560 |
| High | 9.540 | 9.310 | -0.230 |
| Medium | 5.800 | 11.670 | +5.870 |
| high | 6.130 | 6.080 | -0.050 |
| medium | 13.670 | 17.000 | +3.330 |
| neutral | 16.180 | 13.030 | -3.150 |

**Performance Range**:
- Generic: Best=neutral (17.730), Worst=REPETITION (10.610), Gap=7.120
- Guided: Best=correct_linguistic_analysis (29.920), Worst=neutral (9.600), Gap=20.320

</details>

<details>
<summary><b>chrF++</b> (click to expand)</summary>

**Overall Average**: Generic=36.642, Guided=37.332 (Δ +0.690)

**By Trace Type**:

| Trace Type | Generic | Guided | Δ |
|------------|---------|--------|---|
| CORRECT_LINGUISTIC_ANALYSIS | 46.280 | 33.920 | -12.360 |
| NONE | 33.430 | 42.780 | +9.350 |
| REPETITION | 36.380 | 35.550 | -0.830 |
| TRANSLATION_ATTEMPT | 32.930 | 31.510 | -1.420 |
| correct_linguistic_analysis | 35.840 | 50.870 | +15.030 |
| neutral | 34.990 | 29.360 | -5.630 |

**By Trace Usefulness**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| 1 | 0.000 | 30.970 | +30.970 |
| 4 | 53.970 | 0.000 | -53.970 |
| Easy | 42.460 | 0.000 | -42.460 |
| High | 35.370 | 37.630 | +2.260 |
| Medium | 24.720 | 30.510 | +5.790 |
| high | 26.830 | 24.770 | -2.060 |
| medium | 32.290 | 36.290 | +4.000 |
| neutral | 36.620 | 33.500 | -3.120 |

**Performance Range**:
- Generic: Best=CORRECT_LINGUISTIC_ANALYSIS (46.280), Worst=TRANSLATION_ATTEMPT (32.930), Gap=13.350
- Guided: Best=correct_linguistic_analysis (50.870), Worst=neutral (29.360), Gap=21.510

</details>

<details>
<summary><b>COMET</b> (click to expand)</summary>

**Overall Average**: Generic=0.687, Guided=0.765 (Δ +0.078)

**By Trace Type**:

| Trace Type | Generic | Guided | Δ |
|------------|---------|--------|---|
| CORRECT_LINGUISTIC_ANALYSIS | 0.780 | 0.760 | -0.020 |
| NONE | 0.760 | 0.810 | +0.050 |
| REPETITION | 0.530 | 0.660 | +0.130 |
| TRANSLATION_ATTEMPT | 0.710 | 0.670 | -0.040 |
| correct_linguistic_analysis | 0.610 | 0.910 | +0.300 |
| neutral | 0.730 | 0.780 | +0.050 |

**By Trace Usefulness**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| 1 | 0.000 | 0.820 | +0.820 |
| 4 | 0.920 | 0.000 | -0.920 |
| Easy | 0.900 | 0.000 | -0.900 |
| High | 0.910 | 0.790 | -0.120 |
| Medium | 0.530 | 0.610 | +0.080 |
| high | 0.830 | 0.660 | -0.170 |
| medium | 0.710 | 0.750 | +0.040 |
| neutral | 0.730 | 0.730 | 0.000 |

**Performance Range**:
- Generic: Best=CORRECT_LINGUISTIC_ANALYSIS (0.780), Worst=REPETITION (0.530), Gap=0.250
- Guided: Best=correct_linguistic_analysis (0.910), Worst=REPETITION (0.660), Gap=0.250

</details>

<details>
<summary><b>MetricX-24</b> (click to expand)</summary>

**Overall Average**: Generic=10.465, Guided=8.063 (Δ -2.402)

**By Trace Type**:

| Trace Type | Generic | Guided | Δ |
|------------|---------|--------|---|
| CORRECT_LINGUISTIC_ANALYSIS | 10.120 | 9.490 | -0.630 |
| NONE | 6.430 | 7.400 | +0.970 |
| REPETITION | 14.940 | 10.520 | -4.420 |
| TRANSLATION_ATTEMPT | 9.010 | 10.170 | +1.160 |
| correct_linguistic_analysis | 14.310 | 3.610 | -10.700 |
| neutral | 7.980 | 7.190 | -0.790 |

**By Trace Usefulness**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| 1 | 0.000 | 10.190 | +10.190 |
| 4 | 1.180 | 0.000 | -1.180 |
| Easy | 5.410 | 0.000 | -5.410 |
| High | 1.640 | 9.050 | +7.410 |
| Medium | 12.770 | 11.030 | -1.740 |
| high | 7.170 | 10.980 | +3.810 |
| medium | 8.910 | 8.770 | -0.140 |
| neutral | 8.070 | 7.790 | -0.280 |

**Performance Range**:
- Generic: Best=REPETITION (14.940), Worst=NONE (6.430), Gap=8.510
- Guided: Best=REPETITION (10.520), Worst=correct_linguistic_analysis (3.610), Gap=6.910

</details>

---

### 3.7 English → Xhosa

**Examples**: 64 | **Avg Difficulty**: Generic=2.92, Guided=3.21

**Linguistic Phenomena Frequency**:

| Phenomenon | Generic | Guided |
|------------|---------|--------|
| ambiguity | 0.0% | 4.8% |
| complex_syntax | 59.6% | 81.0% |
| figurative_language | 0.0% | 4.8% |
| idiom | 0.0% | 4.8% |
| long_distance_dependency | 98.1% | 100.0% |
| named_entities | 51.9% | 42.9% |

**Trace Type Distribution**:

| Trace Type | Generic Count | Generic % | Guided Count | Guided % | Δ Count | Δ % |
|------------|---------------|-----------|--------------|----------|---------|-----|
| CORRECT_LINGUISTIC_ANALYSIS | 4 | 7.7% | 3 | 7.1% | -1 | -0.6pp |
| NONE | 7 | 13.5% | 3 | 7.1% | -4 | -6.4pp |
| REPETITION | 0 | 0.0% | 1 | 2.4% | +1 | +2.4pp |
| TRANSLATION_ATTEMPT | 35 | 67.3% | 34 | 81.0% | -1 | +13.7pp |
| correct_linguistic_analysis | 1 | 1.9% | 1 | 2.4% | 0 | +0.5pp |
| neutral | 5 | 9.6% | 0 | 0.0% | -5 | -9.6pp |

**Trace Usefulness Distribution**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| 2 | 0.0% | 2.4% | +2.4pp |
| High | 0.0% | 4.8% | +4.8pp |
| Medium | 1.9% | 4.8% | +2.9pp |
| high | 0.0% | 2.4% | +2.4pp |
| medium | 73.1% | 83.3% | +10.2pp |
| neutral | 25.0% | 2.4% | -22.6pp |

**Translation Quality by Metric**:

<details>
<summary><b>BLEU</b> (click to expand)</summary>

**Overall Average**: Generic=2.566, Guided=3.846 (Δ +1.280)

**By Trace Type**:

| Trace Type | Generic | Guided | Δ |
|------------|---------|--------|---|
| CORRECT_LINGUISTIC_ANALYSIS | 3.130 | 3.650 | +0.520 |
| NONE | 2.210 | 6.190 | +3.980 |
| REPETITION | 0.000 | 2.720 | +2.720 |
| TRANSLATION_ATTEMPT | 2.850 | 2.160 | -0.690 |
| correct_linguistic_analysis | 0.430 | 4.510 | +4.080 |
| neutral | 4.210 | 0.000 | -4.210 |

**By Trace Usefulness**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| 2 | 0.000 | 1.290 | +1.290 |
| High | 0.000 | 0.960 | +0.960 |
| Medium | 0.850 | 2.280 | +1.430 |
| high | 0.000 | 1.820 | +1.820 |
| medium | 3.200 | 2.490 | -0.710 |
| neutral | 2.070 | 13.500 | +11.430 |

**Performance Range**:
- Generic: Best=neutral (4.210), Worst=correct_linguistic_analysis (0.430), Gap=3.780
- Guided: Best=NONE (6.190), Worst=TRANSLATION_ATTEMPT (2.160), Gap=4.030

</details>

<details>
<summary><b>chrF++</b> (click to expand)</summary>

**Overall Average**: Generic=13.574, Guided=15.794 (Δ +2.220)

**By Trace Type**:

| Trace Type | Generic | Guided | Δ |
|------------|---------|--------|---|
| CORRECT_LINGUISTIC_ANALYSIS | 16.930 | 22.540 | +5.610 |
| NONE | 13.500 | 14.600 | +1.100 |
| REPETITION | 0.000 | 11.190 | +11.190 |
| TRANSLATION_ATTEMPT | 14.650 | 12.030 | -2.620 |
| correct_linguistic_analysis | 7.060 | 18.610 | +11.550 |
| neutral | 15.730 | 0.000 | -15.730 |

**By Trace Usefulness**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| 2 | 0.000 | 11.440 | +11.440 |
| High | 0.000 | 7.750 | +7.750 |
| Medium | 8.280 | 13.340 | +5.060 |
| high | 0.000 | 13.960 | +13.960 |
| medium | 15.520 | 13.320 | -2.200 |
| neutral | 12.530 | 16.550 | +4.020 |

**Performance Range**:
- Generic: Best=CORRECT_LINGUISTIC_ANALYSIS (16.930), Worst=correct_linguistic_analysis (7.060), Gap=9.870
- Guided: Best=CORRECT_LINGUISTIC_ANALYSIS (22.540), Worst=REPETITION (11.190), Gap=11.350

</details>

<details>
<summary><b>COMET</b> (click to expand)</summary>

**Overall Average**: Generic=0.390, Guided=0.466 (Δ +0.076)

**By Trace Type**:

| Trace Type | Generic | Guided | Δ |
|------------|---------|--------|---|
| CORRECT_LINGUISTIC_ANALYSIS | 0.370 | 0.450 | +0.080 |
| NONE | 0.440 | 0.510 | +0.070 |
| REPETITION | 0.000 | 0.450 | +0.450 |
| TRANSLATION_ATTEMPT | 0.400 | 0.390 | -0.010 |
| correct_linguistic_analysis | 0.340 | 0.530 | +0.190 |
| neutral | 0.400 | 0.000 | -0.400 |

**By Trace Usefulness**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| 2 | 0.000 | 0.450 | +0.450 |
| High | 0.000 | 0.380 | +0.380 |
| Medium | 0.370 | 0.360 | -0.010 |
| high | 0.000 | 0.460 | +0.460 |
| medium | 0.390 | 0.400 | +0.010 |
| neutral | 0.420 | 0.600 | +0.180 |

**Performance Range**:
- Generic: Best=NONE (0.440), Worst=correct_linguistic_analysis (0.340), Gap=0.100
- Guided: Best=correct_linguistic_analysis (0.530), Worst=TRANSLATION_ATTEMPT (0.390), Gap=0.140

</details>

<details>
<summary><b>MetricX-24</b> (click to expand)</summary>

**Overall Average**: Generic=15.288, Guided=12.636 (Δ -2.652)

**By Trace Type**:

| Trace Type | Generic | Guided | Δ |
|------------|---------|--------|---|
| CORRECT_LINGUISTIC_ANALYSIS | 14.450 | 8.160 | -6.290 |
| NONE | 15.010 | 12.230 | -2.780 |
| REPETITION | 0.000 | 17.380 | +17.380 |
| TRANSLATION_ATTEMPT | 15.000 | 15.910 | +0.910 |
| correct_linguistic_analysis | 16.380 | 9.500 | -6.880 |
| neutral | 15.600 | 0.000 | -15.600 |

**By Trace Usefulness**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| 2 | 0.000 | 14.190 | +14.190 |
| High | 0.000 | 16.530 | +16.530 |
| Medium | 15.500 | 15.500 | 0.000 |
| high | 0.000 | 17.500 | +17.500 |
| medium | 14.920 | 14.840 | -0.080 |
| neutral | 15.350 | 13.940 | -1.410 |

**Performance Range**:
- Generic: Best=correct_linguistic_analysis (16.380), Worst=CORRECT_LINGUISTIC_ANALYSIS (14.450), Gap=1.930
- Guided: Best=REPETITION (17.380), Worst=CORRECT_LINGUISTIC_ANALYSIS (8.160), Gap=9.220

</details>

---

### 3.8 Finnish → English

**Examples**: 64 | **Avg Difficulty**: Generic=2.56, Guided=2.78

**Linguistic Phenomena Frequency**:

| Phenomenon | Generic | Guided |
|------------|---------|--------|
| ambiguity | 1.6% | 0.0% |
| complex_syntax | 21.9% | 63.5% |
| long_distance_dependency | 75.0% | 95.2% |
| named_entities | 70.3% | 82.5% |

**Trace Type Distribution**:

| Trace Type | Generic Count | Generic % | Guided Count | Guided % | Δ Count | Δ % |
|------------|---------------|-----------|--------------|----------|---------|-----|
| CORRECT_LINGUISTIC_ANALYSIS | 8 | 12.5% | 2 | 3.2% | -6 | -9.3pp |
| NONE | 15 | 23.4% | 12 | 19.0% | -3 | -4.4pp |
| REASONING | 0 | 0.0% | 1 | 1.6% | +1 | +1.6pp |
| TRANSLATION_ATTEMPT | 20 | 31.2% | 44 | 69.8% | +24 | +38.6pp |
| neutral | 21 | 32.8% | 4 | 6.3% | -17 | -26.5pp |

**Trace Usefulness Distribution**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| helpful | 3.1% | 0.0% | -3.1pp |
| high | 17.2% | 19.0% | +1.8pp |
| medium | 25.0% | 73.0% | +48.0pp |
| neutral | 54.7% | 7.9% | -46.8pp |

**Translation Quality by Metric**:

<details>
<summary><b>BLEU</b> (click to expand)</summary>

**Overall Average**: Generic=17.290, Guided=11.974 (Δ -5.316)

**By Trace Type**:

| Trace Type | Generic | Guided | Δ |
|------------|---------|--------|---|
| CORRECT_LINGUISTIC_ANALYSIS | 15.450 | 9.960 | -5.490 |
| NONE | 23.360 | 13.300 | -10.060 |
| REASONING | 0.000 | 5.120 | +5.120 |
| TRANSLATION_ATTEMPT | 16.300 | 16.310 | +0.010 |
| neutral | 14.050 | 15.180 | +1.130 |

**By Trace Usefulness**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| helpful | 5.650 | 0.000 | -5.650 |
| high | 19.160 | 16.380 | -2.780 |
| medium | 15.870 | 15.190 | -0.680 |
| neutral | 17.690 | 13.530 | -4.160 |

**Performance Range**:
- Generic: Best=NONE (23.360), Worst=neutral (14.050), Gap=9.310
- Guided: Best=TRANSLATION_ATTEMPT (16.310), Worst=REASONING (5.120), Gap=11.190

</details>

<details>
<summary><b>chrF++</b> (click to expand)</summary>

**Overall Average**: Generic=40.332, Guided=33.502 (Δ -6.831)

**By Trace Type**:

| Trace Type | Generic | Guided | Δ |
|------------|---------|--------|---|
| CORRECT_LINGUISTIC_ANALYSIS | 37.470 | 36.420 | -1.050 |
| NONE | 44.500 | 37.410 | -7.090 |
| REASONING | 0.000 | 26.680 | +26.680 |
| TRANSLATION_ATTEMPT | 39.810 | 41.140 | +1.330 |
| neutral | 39.550 | 25.860 | -13.690 |

**By Trace Usefulness**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| helpful | 32.330 | 0.000 | -32.330 |
| high | 40.330 | 41.580 | +1.250 |
| medium | 39.940 | 39.400 | -0.540 |
| neutral | 41.340 | 30.140 | -11.200 |

**Performance Range**:
- Generic: Best=NONE (44.500), Worst=CORRECT_LINGUISTIC_ANALYSIS (37.470), Gap=7.030
- Guided: Best=TRANSLATION_ATTEMPT (41.140), Worst=neutral (25.860), Gap=15.280

</details>

<details>
<summary><b>COMET</b> (click to expand)</summary>

**Overall Average**: Generic=0.818, Guided=0.750 (Δ -0.068)

**By Trace Type**:

| Trace Type | Generic | Guided | Δ |
|------------|---------|--------|---|
| CORRECT_LINGUISTIC_ANALYSIS | 0.770 | 0.750 | -0.020 |
| NONE | 0.840 | 0.820 | -0.020 |
| REASONING | 0.000 | 0.650 | +0.650 |
| TRANSLATION_ATTEMPT | 0.840 | 0.820 | -0.020 |
| neutral | 0.820 | 0.710 | -0.110 |

**By Trace Usefulness**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| helpful | 0.770 | 0.000 | -0.770 |
| high | 0.820 | 0.840 | +0.020 |
| medium | 0.840 | 0.810 | -0.030 |
| neutral | 0.820 | 0.730 | -0.090 |

**Performance Range**:
- Generic: Best=TRANSLATION_ATTEMPT (0.840), Worst=CORRECT_LINGUISTIC_ANALYSIS (0.770), Gap=0.070
- Guided: Best=TRANSLATION_ATTEMPT (0.820), Worst=REASONING (0.650), Gap=0.170

</details>

<details>
<summary><b>MetricX-24</b> (click to expand)</summary>

**Overall Average**: Generic=5.843, Guided=8.084 (Δ +2.241)

**By Trace Type**:

| Trace Type | Generic | Guided | Δ |
|------------|---------|--------|---|
| CORRECT_LINGUISTIC_ANALYSIS | 7.170 | 6.980 | -0.190 |
| NONE | 4.820 | 7.120 | +2.300 |
| REASONING | 0.000 | 10.880 | +10.880 |
| TRANSLATION_ATTEMPT | 5.230 | 6.080 | +0.850 |
| neutral | 6.150 | 9.360 | +3.210 |

**By Trace Usefulness**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| helpful | 7.640 | 0.000 | -7.640 |
| high | 6.080 | 4.910 | -1.170 |
| medium | 5.490 | 6.760 | +1.270 |
| neutral | 5.520 | 9.120 | +3.600 |

**Performance Range**:
- Generic: Best=CORRECT_LINGUISTIC_ANALYSIS (7.170), Worst=NONE (4.820), Gap=2.350
- Guided: Best=REASONING (10.880), Worst=TRANSLATION_ATTEMPT (6.080), Gap=4.800

</details>

---

### 3.9 Finnish → Turkish

**Examples**: 64 | **Avg Difficulty**: Generic=2.66, Guided=3.02

**Linguistic Phenomena Frequency**:

| Phenomenon | Generic | Guided |
|------------|---------|--------|
| ambiguity | 0.0% | 8.1% |
| complex_syntax | 60.9% | 77.4% |
| figurative_language | 0.0% | 8.1% |
| idiom | 0.0% | 8.1% |
| long_distance_dependency | 85.9% | 96.8% |
| named_entities | 78.1% | 71.0% |

**Trace Type Distribution**:

| Trace Type | Generic Count | Generic % | Guided Count | Guided % | Δ Count | Δ % |
|------------|---------------|-----------|--------------|----------|---------|-----|
| CORRECT_LINGUISTIC_ANALYSIS | 5 | 7.8% | 12 | 19.4% | +7 | +11.6pp |
| NONE | 12 | 18.8% | 13 | 21.0% | +1 | +2.2pp |
| REVISION_NEEDED | 1 | 1.6% | 0 | 0.0% | -1 | -1.6pp |
| TRANSLATION_ATTEMPT | 30 | 46.9% | 35 | 56.5% | +5 | +9.6pp |
| correction | 1 | 1.6% | 0 | 0.0% | -1 | -1.6pp |
| neutral | 14 | 21.9% | 2 | 3.2% | -12 | -18.7pp |
| translation_attempt | 1 | 1.6% | 0 | 0.0% | -1 | -1.6pp |

**Trace Usefulness Distribution**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| 1 | 0.0% | 3.2% | +3.2pp |
| 2 | 0.0% | 3.2% | +3.2pp |
| 3 | 0.0% | 1.6% | +1.6pp |
| High | 4.7% | 0.0% | -4.7pp |
| Medium | 1.6% | 1.6% | 0.0pp |
| helpful | 1.6% | 0.0% | -1.6pp |
| high | 3.1% | 4.8% | +1.7pp |
| medium | 50.0% | 74.2% | +24.2pp |
| neutral | 39.1% | 11.3% | -27.8pp |

**Translation Quality by Metric**:

<details>
<summary><b>BLEU</b> (click to expand)</summary>

**Overall Average**: Generic=4.990, Guided=10.775 (Δ +5.785)

**By Trace Type**:

| Trace Type | Generic | Guided | Δ |
|------------|---------|--------|---|
| CORRECT_LINGUISTIC_ANALYSIS | 7.390 | 4.570 | -2.820 |
| NONE | 9.780 | 15.820 | +6.040 |
| REVISION_NEEDED | 1.240 | 0.000 | -1.240 |
| TRANSLATION_ATTEMPT | 4.970 | 5.810 | +0.840 |
| correction | 4.270 | 0.000 | -4.270 |
| neutral | 4.100 | 16.900 | +12.800 |
| translation_attempt | 3.180 | 0.000 | -3.180 |

**By Trace Usefulness**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| 1 | 0.000 | 8.770 | +8.770 |
| 2 | 0.000 | 1.320 | +1.320 |
| 3 | 0.000 | 19.560 | +19.560 |
| High | 11.860 | 0.000 | -11.860 |
| Medium | 17.630 | 2.680 | -14.950 |
| helpful | 2.860 | 0.000 | -2.860 |
| high | 17.280 | 3.320 | -13.960 |
| medium | 4.540 | 6.400 | +1.860 |
| neutral | 5.340 | 21.550 | +16.210 |

**Performance Range**:
- Generic: Best=NONE (9.780), Worst=REVISION_NEEDED (1.240), Gap=8.540
- Guided: Best=neutral (16.900), Worst=CORRECT_LINGUISTIC_ANALYSIS (4.570), Gap=12.330

</details>

<details>
<summary><b>chrF++</b> (click to expand)</summary>

**Overall Average**: Generic=19.447, Guided=28.410 (Δ +8.963)

**By Trace Type**:

| Trace Type | Generic | Guided | Δ |
|------------|---------|--------|---|
| CORRECT_LINGUISTIC_ANALYSIS | 22.230 | 22.040 | -0.190 |
| NONE | 24.090 | 33.170 | +9.080 |
| REVISION_NEEDED | 13.900 | 0.000 | -13.900 |
| TRANSLATION_ATTEMPT | 19.140 | 24.370 | +5.230 |
| correction | 27.500 | 0.000 | -27.500 |
| neutral | 16.110 | 34.060 | +17.950 |
| translation_attempt | 13.160 | 0.000 | -13.160 |

**By Trace Usefulness**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| 1 | 0.000 | 30.430 | +30.430 |
| 2 | 0.000 | 20.380 | +20.380 |
| 3 | 0.000 | 40.740 | +40.740 |
| High | 31.470 | 0.000 | -31.470 |
| Medium | 38.880 | 24.060 | -14.820 |
| helpful | 24.240 | 0.000 | -24.240 |
| high | 18.530 | 16.260 | -2.270 |
| medium | 19.670 | 24.830 | +5.160 |
| neutral | 17.230 | 37.010 | +19.780 |

**Performance Range**:
- Generic: Best=correction (27.500), Worst=translation_attempt (13.160), Gap=14.340
- Guided: Best=neutral (34.060), Worst=CORRECT_LINGUISTIC_ANALYSIS (22.040), Gap=12.020

</details>

<details>
<summary><b>COMET</b> (click to expand)</summary>

**Overall Average**: Generic=0.553, Guided=0.647 (Δ +0.095)

**By Trace Type**:

| Trace Type | Generic | Guided | Δ |
|------------|---------|--------|---|
| CORRECT_LINGUISTIC_ANALYSIS | 0.610 | 0.550 | -0.060 |
| NONE | 0.640 | 0.680 | +0.040 |
| REVISION_NEEDED | 0.410 | 0.000 | -0.410 |
| TRANSLATION_ATTEMPT | 0.600 | 0.600 | 0.000 |
| correction | 0.580 | 0.000 | -0.580 |
| neutral | 0.570 | 0.760 | +0.190 |
| translation_attempt | 0.460 | 0.000 | -0.460 |

**By Trace Usefulness**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| 1 | 0.000 | 0.560 | +0.560 |
| 2 | 0.000 | 0.480 | +0.480 |
| 3 | 0.000 | 0.710 | +0.710 |
| High | 0.660 | 0.000 | -0.660 |
| Medium | 0.760 | 0.460 | -0.300 |
| helpful | 0.660 | 0.000 | -0.660 |
| high | 0.680 | 0.610 | -0.070 |
| medium | 0.600 | 0.610 | +0.010 |
| neutral | 0.570 | 0.710 | +0.140 |

**Performance Range**:
- Generic: Best=NONE (0.640), Worst=REVISION_NEEDED (0.410), Gap=0.230
- Guided: Best=neutral (0.760), Worst=CORRECT_LINGUISTIC_ANALYSIS (0.550), Gap=0.210

</details>

<details>
<summary><b>MetricX-24</b> (click to expand)</summary>

**Overall Average**: Generic=14.306, Guided=11.387 (Δ -2.918)

**By Trace Type**:

| Trace Type | Generic | Guided | Δ |
|------------|---------|--------|---|
| CORRECT_LINGUISTIC_ANALYSIS | 12.760 | 13.810 | +1.050 |
| NONE | 10.850 | 10.400 | -0.450 |
| REVISION_NEEDED | 17.250 | 0.000 | -17.250 |
| TRANSLATION_ATTEMPT | 12.550 | 13.440 | +0.890 |
| correction | 17.000 | 0.000 | -17.000 |
| neutral | 12.850 | 7.900 | -4.950 |
| translation_attempt | 16.880 | 0.000 | -16.880 |

**By Trace Usefulness**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| 1 | 0.000 | 13.750 | +13.750 |
| 2 | 0.000 | 13.590 | +13.590 |
| 3 | 0.000 | 8.060 | +8.060 |
| High | 11.140 | 0.000 | -11.140 |
| Medium | 9.500 | 16.380 | +6.880 |
| helpful | 10.810 | 0.000 | -10.810 |
| high | 10.340 | 14.020 | +3.680 |
| medium | 12.700 | 12.900 | +0.200 |
| neutral | 12.830 | 10.380 | -2.450 |

**Performance Range**:
- Generic: Best=REVISION_NEEDED (17.250), Worst=NONE (10.850), Gap=6.400
- Guided: Best=CORRECT_LINGUISTIC_ANALYSIS (13.810), Worst=neutral (7.900), Gap=5.910

</details>

---

### 3.10 French → English

**Examples**: 64 | **Avg Difficulty**: Generic=2.66, Guided=2.74

**Linguistic Phenomena Frequency**:

| Phenomenon | Generic | Guided |
|------------|---------|--------|
| complex_syntax | 26.6% | 54.8% |
| long_distance_dependency | 73.4% | 93.5% |
| named_entities | 76.6% | 87.1% |

**Trace Type Distribution**:

| Trace Type | Generic Count | Generic % | Guided Count | Guided % | Δ Count | Δ % |
|------------|---------------|-----------|--------------|----------|---------|-----|
| CORRECT_LINGUISTIC_ANALYSIS | 6 | 9.4% | 4 | 6.5% | -2 | -2.9pp |
| NONE | 23 | 35.9% | 22 | 35.5% | -1 | -0.4pp |
| TRANSLATION_ATTEMPT | 11 | 17.2% | 22 | 35.5% | +11 | +18.3pp |
| correct_linguistic_analysis | 0 | 0.0% | 1 | 1.6% | +1 | +1.6pp |
| neutral | 24 | 37.5% | 12 | 19.4% | -12 | -18.1pp |
| null | 0 | 0.0% | 1 | 1.6% | +1 | +1.6pp |

**Trace Usefulness Distribution**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| 5 - Very Helpful | 1.6% | 0.0% | -1.6pp |
| helpful | 1.6% | 0.0% | -1.6pp |
| high | 12.5% | 19.4% | +6.9pp |
| medium | 28.1% | 51.6% | +23.5pp |
| neutral | 56.2% | 29.0% | -27.2pp |

**Translation Quality by Metric**:

<details>
<summary><b>BLEU</b> (click to expand)</summary>

**Overall Average**: Generic=26.715, Guided=26.555 (Δ -0.160)

**By Trace Type**:

| Trace Type | Generic | Guided | Δ |
|------------|---------|--------|---|
| CORRECT_LINGUISTIC_ANALYSIS | 29.250 | 38.870 | +9.620 |
| NONE | 26.920 | 28.130 | +1.210 |
| TRANSLATION_ATTEMPT | 19.180 | 26.600 | +7.420 |
| correct_linguistic_analysis | 0.000 | 18.610 | +18.610 |
| neutral | 31.510 | 31.480 | -0.030 |
| null | 0.000 | 15.640 | +15.640 |

**By Trace Usefulness**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| 5 - Very Helpful | 39.460 | 0.000 | -39.460 |
| helpful | 5.060 | 0.000 | -5.060 |
| high | 27.610 | 30.500 | +2.890 |
| medium | 20.940 | 31.540 | +10.600 |
| neutral | 31.100 | 22.010 | -9.090 |

**Performance Range**:
- Generic: Best=neutral (31.510), Worst=TRANSLATION_ATTEMPT (19.180), Gap=12.330
- Guided: Best=CORRECT_LINGUISTIC_ANALYSIS (38.870), Worst=null (15.640), Gap=23.230

</details>

<details>
<summary><b>chrF++</b> (click to expand)</summary>

**Overall Average**: Generic=51.260, Guided=52.098 (Δ +0.838)

**By Trace Type**:

| Trace Type | Generic | Guided | Δ |
|------------|---------|--------|---|
| CORRECT_LINGUISTIC_ANALYSIS | 51.850 | 63.480 | +11.630 |
| NONE | 51.760 | 51.060 | -0.700 |
| TRANSLATION_ATTEMPT | 47.210 | 51.530 | +4.320 |
| correct_linguistic_analysis | 0.000 | 41.860 | +41.860 |
| neutral | 54.220 | 54.800 | +0.580 |
| null | 0.000 | 49.860 | +49.860 |

**By Trace Usefulness**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| 5 - Very Helpful | 55.110 | 0.000 | -55.110 |
| helpful | 25.400 | 0.000 | -25.400 |
| high | 52.750 | 55.700 | +2.950 |
| medium | 48.310 | 55.250 | +6.940 |
| neutral | 54.170 | 45.780 | -8.390 |

**Performance Range**:
- Generic: Best=neutral (54.220), Worst=TRANSLATION_ATTEMPT (47.210), Gap=7.010
- Guided: Best=CORRECT_LINGUISTIC_ANALYSIS (63.480), Worst=correct_linguistic_analysis (41.860), Gap=21.620

</details>

<details>
<summary><b>COMET</b> (click to expand)</summary>

**Overall Average**: Generic=0.845, Guided=0.860 (Δ +0.015)

**By Trace Type**:

| Trace Type | Generic | Guided | Δ |
|------------|---------|--------|---|
| CORRECT_LINGUISTIC_ANALYSIS | 0.810 | 0.890 | +0.080 |
| NONE | 0.850 | 0.840 | -0.010 |
| TRANSLATION_ATTEMPT | 0.860 | 0.850 | -0.010 |
| correct_linguistic_analysis | 0.000 | 0.850 | +0.850 |
| neutral | 0.860 | 0.850 | -0.010 |
| null | 0.000 | 0.880 | +0.880 |

**By Trace Usefulness**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| 5 - Very Helpful | 0.890 | 0.000 | -0.890 |
| helpful | 0.780 | 0.000 | -0.780 |
| high | 0.840 | 0.850 | +0.010 |
| medium | 0.850 | 0.860 | +0.010 |
| neutral | 0.860 | 0.820 | -0.040 |

**Performance Range**:
- Generic: Best=neutral (0.860), Worst=CORRECT_LINGUISTIC_ANALYSIS (0.810), Gap=0.050
- Guided: Best=CORRECT_LINGUISTIC_ANALYSIS (0.890), Worst=NONE (0.840), Gap=0.050

</details>

<details>
<summary><b>MetricX-24</b> (click to expand)</summary>

**Overall Average**: Generic=4.085, Guided=4.658 (Δ +0.573)

**By Trace Type**:

| Trace Type | Generic | Guided | Δ |
|------------|---------|--------|---|
| CORRECT_LINGUISTIC_ANALYSIS | 4.720 | 2.230 | -2.490 |
| NONE | 3.730 | 4.400 | +0.670 |
| TRANSLATION_ATTEMPT | 3.820 | 4.590 | +0.770 |
| correct_linguistic_analysis | 0.000 | 4.060 | +4.060 |
| neutral | 4.070 | 4.050 | -0.020 |
| null | 0.000 | 8.620 | +8.620 |

**By Trace Usefulness**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| 5 - Very Helpful | 3.160 | 0.000 | -3.160 |
| helpful | 8.250 | 0.000 | -8.250 |
| high | 4.590 | 3.890 | -0.700 |
| medium | 3.580 | 3.960 | +0.380 |
| neutral | 3.920 | 5.260 | +1.340 |

**Performance Range**:
- Generic: Best=CORRECT_LINGUISTIC_ANALYSIS (4.720), Worst=NONE (3.730), Gap=0.990
- Guided: Best=null (8.620), Worst=CORRECT_LINGUISTIC_ANALYSIS (2.230), Gap=6.390

</details>

---

### 3.11 French → German

**Examples**: 64 | **Avg Difficulty**: Generic=2.70, Guided=2.95

**Linguistic Phenomena Frequency**:

| Phenomenon | Generic | Guided |
|------------|---------|--------|
| ambiguity | 1.6% | 1.6% |
| complex_syntax | 58.7% | 79.0% |
| figurative_language | 1.6% | 1.6% |
| idiom | 1.6% | 1.6% |
| long_distance_dependency | 88.9% | 98.4% |
| named_entities | 82.5% | 79.0% |

**Trace Type Distribution**:

| Trace Type | Generic Count | Generic % | Guided Count | Guided % | Δ Count | Δ % |
|------------|---------------|-----------|--------------|----------|---------|-----|
| CORRECT_LINGUISTIC_ANALYSIS | 4 | 6.3% | 7 | 11.3% | +3 | +5.0pp |
| NONE | 19 | 30.2% | 9 | 14.5% | -10 | -15.7pp |
| TRANSLATION_ATTEMPT | 20 | 31.7% | 38 | 61.3% | +18 | +29.6pp |
| correct_linguistic_analysis | 1 | 1.6% | 3 | 4.8% | +2 | +3.2pp |
| neutral | 17 | 27.0% | 5 | 8.1% | -12 | -18.9pp |
| null | 2 | 3.2% | 0 | 0.0% | -2 | -3.2pp |

**Trace Usefulness Distribution**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| 1 | 1.6% | 0.0% | -1.6pp |
| 2 | 0.0% | 1.6% | +1.6pp |
| HIGH | 1.6% | 0.0% | -1.6pp |
| Medium | 3.2% | 6.5% | +3.3pp |
| high | 9.5% | 11.3% | +1.8pp |
| medium | 41.3% | 66.1% | +24.8pp |
| neutral | 42.9% | 14.5% | -28.4pp |

**Translation Quality by Metric**:

<details>
<summary><b>BLEU</b> (click to expand)</summary>

**Overall Average**: Generic=16.373, Guided=22.026 (Δ +5.653)

**By Trace Type**:

| Trace Type | Generic | Guided | Δ |
|------------|---------|--------|---|
| CORRECT_LINGUISTIC_ANALYSIS | 19.550 | 19.520 | -0.030 |
| NONE | 15.620 | 18.630 | +3.010 |
| TRANSLATION_ATTEMPT | 17.760 | 17.300 | -0.460 |
| correct_linguistic_analysis | 11.760 | 38.120 | +26.360 |
| neutral | 21.470 | 16.560 | -4.910 |
| null | 12.080 | 0.000 | -12.080 |

**By Trace Usefulness**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| 1 | 18.950 | 0.000 | -18.950 |
| 2 | 0.000 | 27.270 | +27.270 |
| HIGH | 8.010 | 0.000 | -8.010 |
| Medium | 20.510 | 26.880 | +6.370 |
| high | 20.450 | 23.750 | +3.300 |
| medium | 15.670 | 16.600 | +0.930 |
| neutral | 19.740 | 19.710 | -0.030 |

**Performance Range**:
- Generic: Best=neutral (21.470), Worst=correct_linguistic_analysis (11.760), Gap=9.710
- Guided: Best=correct_linguistic_analysis (38.120), Worst=neutral (16.560), Gap=21.560

</details>

<details>
<summary><b>chrF++</b> (click to expand)</summary>

**Overall Average**: Generic=41.052, Guided=42.712 (Δ +1.660)

**By Trace Type**:

| Trace Type | Generic | Guided | Δ |
|------------|---------|--------|---|
| CORRECT_LINGUISTIC_ANALYSIS | 47.210 | 42.410 | -4.800 |
| NONE | 35.530 | 41.980 | +6.450 |
| TRANSLATION_ATTEMPT | 42.110 | 39.740 | -2.370 |
| correct_linguistic_analysis | 41.570 | 54.430 | +12.860 |
| neutral | 42.010 | 35.000 | -7.010 |
| null | 37.880 | 0.000 | -37.880 |

**By Trace Usefulness**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| 1 | 38.030 | 0.000 | -38.030 |
| 2 | 0.000 | 49.150 | +49.150 |
| HIGH | 32.760 | 0.000 | -32.760 |
| Medium | 37.700 | 49.310 | +11.610 |
| high | 44.650 | 43.830 | -0.820 |
| medium | 39.130 | 39.030 | -0.100 |
| neutral | 40.970 | 41.090 | +0.120 |

**Performance Range**:
- Generic: Best=CORRECT_LINGUISTIC_ANALYSIS (47.210), Worst=NONE (35.530), Gap=11.680
- Guided: Best=correct_linguistic_analysis (54.430), Worst=neutral (35.000), Gap=19.430

</details>

<details>
<summary><b>COMET</b> (click to expand)</summary>

**Overall Average**: Generic=0.790, Guided=0.772 (Δ -0.018)

**By Trace Type**:

| Trace Type | Generic | Guided | Δ |
|------------|---------|--------|---|
| CORRECT_LINGUISTIC_ANALYSIS | 0.840 | 0.720 | -0.120 |
| NONE | 0.760 | 0.750 | -0.010 |
| TRANSLATION_ATTEMPT | 0.720 | 0.740 | +0.020 |
| correct_linguistic_analysis | 0.840 | 0.850 | +0.010 |
| neutral | 0.790 | 0.800 | +0.010 |
| null | 0.790 | 0.000 | -0.790 |

**By Trace Usefulness**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| 1 | 0.820 | 0.000 | -0.820 |
| 2 | 0.000 | 0.550 | +0.550 |
| HIGH | 0.800 | 0.000 | -0.800 |
| Medium | 0.850 | 0.870 | +0.020 |
| high | 0.830 | 0.800 | -0.030 |
| medium | 0.740 | 0.730 | -0.010 |
| neutral | 0.760 | 0.770 | +0.010 |

**Performance Range**:
- Generic: Best=correct_linguistic_analysis (0.840), Worst=TRANSLATION_ATTEMPT (0.720), Gap=0.120
- Guided: Best=correct_linguistic_analysis (0.850), Worst=CORRECT_LINGUISTIC_ANALYSIS (0.720), Gap=0.130

</details>

<details>
<summary><b>MetricX-24</b> (click to expand)</summary>

**Overall Average**: Generic=2.862, Guided=3.574 (Δ +0.712)

**By Trace Type**:

| Trace Type | Generic | Guided | Δ |
|------------|---------|--------|---|
| CORRECT_LINGUISTIC_ANALYSIS | 1.570 | 4.420 | +2.850 |
| NONE | 5.000 | 4.050 | -0.950 |
| TRANSLATION_ATTEMPT | 4.330 | 3.840 | -0.490 |
| correct_linguistic_analysis | 1.430 | 1.510 | +0.080 |
| neutral | 2.800 | 4.050 | +1.250 |
| null | 2.040 | 0.000 | -2.040 |

**By Trace Usefulness**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| 1 | 2.480 | 0.000 | -2.480 |
| 2 | 0.000 | 4.560 | +4.560 |
| HIGH | 3.330 | 0.000 | -3.330 |
| Medium | 1.150 | 1.520 | +0.370 |
| high | 1.910 | 3.210 | +1.300 |
| medium | 4.520 | 4.020 | -0.500 |
| neutral | 3.850 | 4.460 | +0.610 |

**Performance Range**:
- Generic: Best=NONE (5.000), Worst=correct_linguistic_analysis (1.430), Gap=3.570
- Guided: Best=CORRECT_LINGUISTIC_ANALYSIS (4.420), Worst=correct_linguistic_analysis (1.510), Gap=2.910

</details>

---

### 3.12 German → English

**Examples**: 64 | **Avg Difficulty**: Generic=2.41, Guided=2.77

**Linguistic Phenomena Frequency**:

| Phenomenon | Generic | Guided |
|------------|---------|--------|
| complex_syntax | 22.2% | 53.1% |
| long_distance_dependency | 74.6% | 93.8% |
| named_entities | 76.2% | 82.8% |

**Trace Type Distribution**:

| Trace Type | Generic Count | Generic % | Guided Count | Guided % | Δ Count | Δ % |
|------------|---------------|-----------|--------------|----------|---------|-----|
| CORRECT_LINGUISTIC_ANALYSIS | 4 | 6.3% | 4 | 6.2% | 0 | -0.1pp |
| NONE | 12 | 19.0% | 18 | 28.1% | +6 | +9.1pp |
| REPETITION | 0 | 0.0% | 1 | 1.6% | +1 | +1.6pp |
| TRANSLATION_ATTEMPT | 19 | 30.2% | 35 | 54.7% | +16 | +24.5pp |
| neutral | 26 | 41.3% | 5 | 7.8% | -21 | -33.5pp |
| null | 2 | 3.2% | 1 | 1.6% | -1 | -1.6pp |

**Trace Usefulness Distribution**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| high | 14.3% | 20.3% | +6.0pp |
| medium | 23.8% | 54.7% | +30.9pp |
| neutral | 61.9% | 25.0% | -36.9pp |

**Translation Quality by Metric**:

<details>
<summary><b>BLEU</b> (click to expand)</summary>

**Overall Average**: Generic=27.078, Guided=28.833 (Δ +1.755)

**By Trace Type**:

| Trace Type | Generic | Guided | Δ |
|------------|---------|--------|---|
| CORRECT_LINGUISTIC_ANALYSIS | 41.730 | 21.860 | -19.870 |
| NONE | 23.150 | 28.520 | +5.370 |
| REPETITION | 0.000 | 57.360 | +57.360 |
| TRANSLATION_ATTEMPT | 21.650 | 24.170 | +2.520 |
| neutral | 27.960 | 29.320 | +1.360 |
| null | 20.900 | 11.770 | -9.130 |

**By Trace Usefulness**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| high | 27.750 | 27.010 | -0.740 |
| medium | 22.460 | 25.070 | +2.610 |
| neutral | 26.620 | 27.110 | +0.490 |

**Performance Range**:
- Generic: Best=CORRECT_LINGUISTIC_ANALYSIS (41.730), Worst=null (20.900), Gap=20.830
- Guided: Best=REPETITION (57.360), Worst=null (11.770), Gap=45.590

</details>

<details>
<summary><b>chrF++</b> (click to expand)</summary>

**Overall Average**: Generic=53.486, Guided=52.025 (Δ -1.461)

**By Trace Type**:

| Trace Type | Generic | Guided | Δ |
|------------|---------|--------|---|
| CORRECT_LINGUISTIC_ANALYSIS | 65.270 | 46.970 | -18.300 |
| NONE | 47.410 | 53.360 | +5.950 |
| REPETITION | 0.000 | 74.470 | +74.470 |
| TRANSLATION_ATTEMPT | 47.950 | 49.560 | +1.610 |
| neutral | 52.360 | 47.850 | -4.510 |
| null | 54.440 | 39.940 | -14.500 |

**By Trace Usefulness**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| high | 54.960 | 52.730 | -2.230 |
| medium | 48.770 | 49.580 | +0.810 |
| neutral | 50.900 | 50.990 | +0.090 |

**Performance Range**:
- Generic: Best=CORRECT_LINGUISTIC_ANALYSIS (65.270), Worst=NONE (47.410), Gap=17.860
- Guided: Best=REPETITION (74.470), Worst=null (39.940), Gap=34.530

</details>

<details>
<summary><b>COMET</b> (click to expand)</summary>

**Overall Average**: Generic=0.844, Guided=0.845 (Δ +0.001)

**By Trace Type**:

| Trace Type | Generic | Guided | Δ |
|------------|---------|--------|---|
| CORRECT_LINGUISTIC_ANALYSIS | 0.870 | 0.830 | -0.040 |
| NONE | 0.840 | 0.870 | +0.030 |
| REPETITION | 0.000 | 0.890 | +0.890 |
| TRANSLATION_ATTEMPT | 0.830 | 0.820 | -0.010 |
| neutral | 0.860 | 0.840 | -0.020 |
| null | 0.820 | 0.820 | 0.000 |

**By Trace Usefulness**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| high | 0.850 | 0.840 | -0.010 |
| medium | 0.840 | 0.830 | -0.010 |
| neutral | 0.850 | 0.860 | +0.010 |

**Performance Range**:
- Generic: Best=CORRECT_LINGUISTIC_ANALYSIS (0.870), Worst=null (0.820), Gap=0.050
- Guided: Best=REPETITION (0.890), Worst=null (0.820), Gap=0.070

</details>

<details>
<summary><b>MetricX-24</b> (click to expand)</summary>

**Overall Average**: Generic=3.930, Guided=4.542 (Δ +0.612)

**By Trace Type**:

| Trace Type | Generic | Guided | Δ |
|------------|---------|--------|---|
| CORRECT_LINGUISTIC_ANALYSIS | 3.410 | 6.890 | +3.480 |
| NONE | 4.240 | 3.250 | -0.990 |
| REPETITION | 0.000 | 3.220 | +3.220 |
| TRANSLATION_ATTEMPT | 5.060 | 4.940 | -0.120 |
| neutral | 3.820 | 5.530 | +1.710 |
| null | 3.120 | 3.420 | +0.300 |

**By Trace Usefulness**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| high | 4.120 | 4.450 | +0.330 |
| medium | 4.980 | 5.200 | +0.220 |
| neutral | 3.960 | 3.340 | -0.620 |

**Performance Range**:
- Generic: Best=TRANSLATION_ATTEMPT (5.060), Worst=null (3.120), Gap=1.940
- Guided: Best=CORRECT_LINGUISTIC_ANALYSIS (6.890), Worst=REPETITION (3.220), Gap=3.670

</details>

---

### 3.13 German → French

**Examples**: 64 | **Avg Difficulty**: Generic=2.50, Guided=2.92

**Linguistic Phenomena Frequency**:

| Phenomenon | Generic | Guided |
|------------|---------|--------|
| ambiguity | 0.0% | 1.7% |
| complex_syntax | 56.2% | 81.4% |
| figurative_language | 0.0% | 1.7% |
| idiom | 0.0% | 3.4% |
| long_distance_dependency | 82.8% | 96.6% |
| named_entities | 73.4% | 81.4% |

**Trace Type Distribution**:

| Trace Type | Generic Count | Generic % | Guided Count | Guided % | Δ Count | Δ % |
|------------|---------------|-----------|--------------|----------|---------|-----|
| CORRECT_LINGUISTIC_ANALYSIS | 2 | 3.1% | 3 | 5.1% | +1 | +2.0pp |
| HALLUCINATED_RULE | 0 | 0.0% | 1 | 1.7% | +1 | +1.7pp |
| NONE | 18 | 28.1% | 5 | 8.5% | -13 | -19.6pp |
| TRANSLATION_ATTEMPT | 23 | 35.9% | 42 | 71.2% | +19 | +35.3pp |
| Translation Attempt | 0 | 0.0% | 1 | 1.7% | +1 | +1.7pp |
| neutral | 16 | 25.0% | 7 | 11.9% | -9 | -13.1pp |
| null | 4 | 6.2% | 0 | 0.0% | -4 | -6.2pp |
| translation_attempt | 1 | 1.6% | 0 | 0.0% | -1 | -1.6pp |

**Trace Usefulness Distribution**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| 3 | 0.0% | 1.7% | +1.7pp |
| High | 0.0% | 1.7% | +1.7pp |
| Medium | 0.0% | 6.8% | +6.8pp |
| high | 9.4% | 6.8% | -2.6pp |
| medium | 40.6% | 74.6% | +34.0pp |
| neutral | 50.0% | 8.5% | -41.5pp |

**Translation Quality by Metric**:

<details>
<summary><b>BLEU</b> (click to expand)</summary>

**Overall Average**: Generic=24.128, Guided=22.287 (Δ -1.842)

**By Trace Type**:

| Trace Type | Generic | Guided | Δ |
|------------|---------|--------|---|
| CORRECT_LINGUISTIC_ANALYSIS | 32.130 | 26.500 | -5.630 |
| HALLUCINATED_RULE | 0.000 | 14.740 | +14.740 |
| NONE | 24.290 | 22.950 | -1.340 |
| TRANSLATION_ATTEMPT | 19.260 | 18.930 | -0.330 |
| Translation Attempt | 0.000 | 14.670 | +14.670 |
| neutral | 26.750 | 35.930 | +9.180 |
| null | 24.010 | 0.000 | -24.010 |
| translation_attempt | 18.330 | 0.000 | -18.330 |

**By Trace Usefulness**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| 3 | 0.000 | 36.320 | +36.320 |
| High | 0.000 | 23.110 | +23.110 |
| Medium | 0.000 | 15.540 | +15.540 |
| high | 19.340 | 21.060 | +1.720 |
| medium | 20.600 | 22.210 | +1.610 |
| neutral | 26.100 | 17.470 | -8.630 |

**Performance Range**:
- Generic: Best=CORRECT_LINGUISTIC_ANALYSIS (32.130), Worst=translation_attempt (18.330), Gap=13.800
- Guided: Best=neutral (35.930), Worst=Translation Attempt (14.670), Gap=21.260

</details>

<details>
<summary><b>chrF++</b> (click to expand)</summary>

**Overall Average**: Generic=44.847, Guided=44.458 (Δ -0.388)

**By Trace Type**:

| Trace Type | Generic | Guided | Δ |
|------------|---------|--------|---|
| CORRECT_LINGUISTIC_ANALYSIS | 53.330 | 49.030 | -4.300 |
| HALLUCINATED_RULE | 0.000 | 33.780 | +33.780 |
| NONE | 42.800 | 43.110 | +0.310 |
| TRANSLATION_ATTEMPT | 43.530 | 43.190 | -0.340 |
| Translation Attempt | 0.000 | 45.540 | +45.540 |
| neutral | 43.240 | 52.100 | +8.860 |
| null | 51.950 | 0.000 | -51.950 |
| translation_attempt | 34.230 | 0.000 | -34.230 |

**By Trace Usefulness**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| 3 | 0.000 | 60.280 | +60.280 |
| High | 0.000 | 47.720 | +47.720 |
| Medium | 0.000 | 40.900 | +40.900 |
| high | 42.150 | 47.300 | +5.150 |
| medium | 43.600 | 44.330 | +0.730 |
| neutral | 44.550 | 41.840 | -2.710 |

**Performance Range**:
- Generic: Best=CORRECT_LINGUISTIC_ANALYSIS (53.330), Worst=translation_attempt (34.230), Gap=19.100
- Guided: Best=neutral (52.100), Worst=HALLUCINATED_RULE (33.780), Gap=18.320

</details>

<details>
<summary><b>COMET</b> (click to expand)</summary>

**Overall Average**: Generic=0.775, Guided=0.735 (Δ -0.040)

**By Trace Type**:

| Trace Type | Generic | Guided | Δ |
|------------|---------|--------|---|
| CORRECT_LINGUISTIC_ANALYSIS | 0.840 | 0.790 | -0.050 |
| HALLUCINATED_RULE | 0.000 | 0.750 | +0.750 |
| NONE | 0.770 | 0.800 | +0.030 |
| TRANSLATION_ATTEMPT | 0.740 | 0.750 | +0.010 |
| Translation Attempt | 0.000 | 0.500 | +0.500 |
| neutral | 0.790 | 0.820 | +0.030 |
| null | 0.790 | 0.000 | -0.790 |
| translation_attempt | 0.720 | 0.000 | -0.720 |

**By Trace Usefulness**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| 3 | 0.000 | 0.880 | +0.880 |
| High | 0.000 | 0.730 | +0.730 |
| Medium | 0.000 | 0.660 | +0.660 |
| high | 0.740 | 0.840 | +0.100 |
| medium | 0.780 | 0.760 | -0.020 |
| neutral | 0.760 | 0.760 | 0.000 |

**Performance Range**:
- Generic: Best=CORRECT_LINGUISTIC_ANALYSIS (0.840), Worst=translation_attempt (0.720), Gap=0.120
- Guided: Best=neutral (0.820), Worst=Translation Attempt (0.500), Gap=0.320

</details>

<details>
<summary><b>MetricX-24</b> (click to expand)</summary>

**Overall Average**: Generic=4.502, Guided=5.713 (Δ +1.212)

**By Trace Type**:

| Trace Type | Generic | Guided | Δ |
|------------|---------|--------|---|
| CORRECT_LINGUISTIC_ANALYSIS | 2.680 | 3.790 | +1.110 |
| HALLUCINATED_RULE | 0.000 | 3.330 | +3.330 |
| NONE | 6.170 | 5.180 | -0.990 |
| TRANSLATION_ATTEMPT | 5.380 | 6.140 | +0.760 |
| Translation Attempt | 0.000 | 12.060 | +12.060 |
| neutral | 4.650 | 3.780 | -0.870 |
| null | 4.490 | 0.000 | -4.490 |
| translation_attempt | 3.640 | 0.000 | -3.640 |

**By Trace Usefulness**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| 3 | 0.000 | 2.220 | +2.220 |
| High | 0.000 | 7.810 | +7.810 |
| Medium | 0.000 | 8.000 | +8.000 |
| high | 5.400 | 1.890 | -3.510 |
| medium | 4.480 | 5.800 | +1.320 |
| neutral | 5.850 | 6.430 | +0.580 |

**Performance Range**:
- Generic: Best=NONE (6.170), Worst=CORRECT_LINGUISTIC_ANALYSIS (2.680), Gap=3.490
- Guided: Best=Translation Attempt (12.060), Worst=HALLUCINATED_RULE (3.330), Gap=8.730

</details>

---

### 3.14 Kazakh → English

**Examples**: 64 | **Avg Difficulty**: Generic=2.91, Guided=3.10

**Linguistic Phenomena Frequency**:

| Phenomenon | Generic | Guided |
|------------|---------|--------|
| ambiguity | 1.6% | 1.6% |
| complex_syntax | 39.1% | 71.4% |
| figurative_language | 0.0% | 1.6% |
| idiom | 0.0% | 1.6% |
| long_distance_dependency | 85.9% | 95.2% |
| named_entities | 76.6% | 77.8% |

**Trace Type Distribution**:

| Trace Type | Generic Count | Generic % | Guided Count | Guided % | Δ Count | Δ % |
|------------|---------------|-----------|--------------|----------|---------|-----|
| CORRECT_LINGUISTIC_ANALYSIS | 26 | 40.6% | 6 | 9.5% | -20 | -31.1pp |
| NONE | 18 | 28.1% | 17 | 27.0% | -1 | -1.1pp |
| REASONING | 2 | 3.1% | 0 | 0.0% | -2 | -3.1pp |
| REPETITION | 0 | 0.0% | 2 | 3.2% | +2 | +3.2pp |
| TRANSLATION_ATTEMPT | 14 | 21.9% | 33 | 52.4% | +19 | +30.5pp |
| correct_linguistic_analysis | 1 | 1.6% | 1 | 1.6% | 0 | 0.0pp |
| neutral | 3 | 4.7% | 4 | 6.3% | +1 | +1.6pp |

**Trace Usefulness Distribution**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| 3 | 0.0% | 1.6% | +1.6pp |
| Easy | 0.0% | 1.6% | +1.6pp |
| High | 1.6% | 0.0% | -1.6pp |
| Medium | 1.6% | 3.2% | +1.6pp |
| helpful | 1.6% | 0.0% | -1.6pp |
| high | 46.9% | 19.0% | -27.9pp |
| medium | 29.7% | 63.5% | +33.8pp |
| neutral | 18.8% | 11.1% | -7.7pp |

**Translation Quality by Metric**:

<details>
<summary><b>BLEU</b> (click to expand)</summary>

**Overall Average**: Generic=11.143, Guided=6.808 (Δ -4.335)

**By Trace Type**:

| Trace Type | Generic | Guided | Δ |
|------------|---------|--------|---|
| CORRECT_LINGUISTIC_ANALYSIS | 11.210 | 2.870 | -8.340 |
| NONE | 6.430 | 9.840 | +3.410 |
| REASONING | 20.800 | 0.000 | -20.800 |
| REPETITION | 0.000 | 11.320 | +11.320 |
| TRANSLATION_ATTEMPT | 6.290 | 9.200 | +2.910 |
| correct_linguistic_analysis | 10.260 | 1.730 | -8.530 |
| neutral | 11.870 | 5.890 | -5.980 |

**By Trace Usefulness**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| 3 | 0.000 | 1.090 | +1.090 |
| Easy | 0.000 | 8.590 | +8.590 |
| High | 3.830 | 0.000 | -3.830 |
| Medium | 4.160 | 3.090 | -1.070 |
| helpful | 10.260 | 0.000 | -10.260 |
| high | 11.780 | 4.960 | -6.820 |
| medium | 6.570 | 9.390 | +2.820 |
| neutral | 7.160 | 12.160 | +5.000 |

**Performance Range**:
- Generic: Best=REASONING (20.800), Worst=TRANSLATION_ATTEMPT (6.290), Gap=14.510
- Guided: Best=REPETITION (11.320), Worst=correct_linguistic_analysis (1.730), Gap=9.590

</details>

<details>
<summary><b>chrF++</b> (click to expand)</summary>

**Overall Average**: Generic=31.902, Guided=27.422 (Δ -4.480)

**By Trace Type**:

| Trace Type | Generic | Guided | Δ |
|------------|---------|--------|---|
| CORRECT_LINGUISTIC_ANALYSIS | 30.060 | 19.640 | -10.420 |
| NONE | 26.970 | 34.060 | +7.090 |
| REASONING | 41.170 | 0.000 | -41.170 |
| REPETITION | 0.000 | 32.560 | +32.560 |
| TRANSLATION_ATTEMPT | 30.190 | 29.060 | -1.130 |
| correct_linguistic_analysis | 35.110 | 26.700 | -8.410 |
| neutral | 27.910 | 22.510 | -5.400 |

**By Trace Usefulness**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| 3 | 0.000 | 25.720 | +25.720 |
| Easy | 0.000 | 34.610 | +34.610 |
| High | 12.680 | 0.000 | -12.680 |
| Medium | 24.850 | 19.180 | -5.670 |
| helpful | 35.110 | 0.000 | -35.110 |
| high | 32.580 | 23.830 | -8.750 |
| medium | 28.780 | 30.260 | +1.480 |
| neutral | 24.500 | 34.640 | +10.140 |

**Performance Range**:
- Generic: Best=REASONING (41.170), Worst=NONE (26.970), Gap=14.200
- Guided: Best=NONE (34.060), Worst=CORRECT_LINGUISTIC_ANALYSIS (19.640), Gap=14.420

</details>

<details>
<summary><b>COMET</b> (click to expand)</summary>

**Overall Average**: Generic=0.715, Guided=0.707 (Δ -0.008)

**By Trace Type**:

| Trace Type | Generic | Guided | Δ |
|------------|---------|--------|---|
| CORRECT_LINGUISTIC_ANALYSIS | 0.690 | 0.640 | -0.050 |
| NONE | 0.710 | 0.730 | +0.020 |
| REASONING | 0.800 | 0.000 | -0.800 |
| REPETITION | 0.000 | 0.720 | +0.720 |
| TRANSLATION_ATTEMPT | 0.700 | 0.700 | 0.000 |
| correct_linguistic_analysis | 0.650 | 0.770 | +0.120 |
| neutral | 0.740 | 0.680 | -0.060 |

**By Trace Usefulness**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| 3 | 0.000 | 0.650 | +0.650 |
| Easy | 0.000 | 0.790 | +0.790 |
| High | 0.500 | 0.000 | -0.500 |
| Medium | 0.660 | 0.560 | -0.100 |
| helpful | 0.650 | 0.000 | -0.650 |
| high | 0.720 | 0.680 | -0.040 |
| medium | 0.710 | 0.710 | 0.000 |
| neutral | 0.670 | 0.720 | +0.050 |

**Performance Range**:
- Generic: Best=REASONING (0.800), Worst=correct_linguistic_analysis (0.650), Gap=0.150
- Guided: Best=correct_linguistic_analysis (0.770), Worst=CORRECT_LINGUISTIC_ANALYSIS (0.640), Gap=0.130

</details>

<details>
<summary><b>MetricX-24</b> (click to expand)</summary>

**Overall Average**: Generic=10.885, Guided=12.058 (Δ +1.173)

**By Trace Type**:

| Trace Type | Generic | Guided | Δ |
|------------|---------|--------|---|
| CORRECT_LINGUISTIC_ANALYSIS | 11.530 | 13.410 | +1.880 |
| NONE | 12.100 | 10.510 | -1.590 |
| REASONING | 7.690 | 0.000 | -7.690 |
| REPETITION | 0.000 | 10.340 | +10.340 |
| TRANSLATION_ATTEMPT | 10.300 | 11.300 | +1.000 |
| correct_linguistic_analysis | 12.690 | 13.560 | +0.870 |
| neutral | 11.000 | 13.230 | +2.230 |

**By Trace Usefulness**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| 3 | 0.000 | 13.380 | +13.380 |
| Easy | 0.000 | 14.940 | +14.940 |
| High | 16.000 | 0.000 | -16.000 |
| Medium | 15.060 | 15.810 | +0.750 |
| helpful | 12.690 | 0.000 | -12.690 |
| high | 10.780 | 12.770 | +1.990 |
| medium | 10.550 | 10.790 | +0.240 |
| neutral | 12.950 | 10.650 | -2.300 |

**Performance Range**:
- Generic: Best=correct_linguistic_analysis (12.690), Worst=REASONING (7.690), Gap=5.000
- Guided: Best=correct_linguistic_analysis (13.560), Worst=REPETITION (10.340), Gap=3.220

</details>

---

### 3.15 Kazakh → Xhosa

**Examples**: 64 | **Avg Difficulty**: Generic=3.12, Guided=3.08

**Linguistic Phenomena Frequency**:

| Phenomenon | Generic | Guided |
|------------|---------|--------|
| ambiguity | 0.0% | 2.1% |
| complex_syntax | 66.1% | 81.2% |
| figurative_language | 0.0% | 2.1% |
| idiom | 0.0% | 2.1% |
| long_distance_dependency | 98.2% | 100.0% |
| named_entities | 71.4% | 52.1% |

**Trace Type Distribution**:

| Trace Type | Generic Count | Generic % | Guided Count | Guided % | Δ Count | Δ % |
|------------|---------------|-----------|--------------|----------|---------|-----|
| CORRECT_LINGUISTIC_ANALYSIS | 18 | 32.1% | 3 | 6.2% | -15 | -25.9pp |
| NONE | 7 | 12.5% | 4 | 8.3% | -3 | -4.2pp |
| REPETITION | 1 | 1.8% | 0 | 0.0% | -1 | -1.8pp |
| TRANSLATION_ATTEMPT | 28 | 50.0% | 39 | 81.2% | +11 | +31.2pp |
| correct_linguistic_analysis | 2 | 3.6% | 0 | 0.0% | -2 | -3.6pp |
| neutral | 0 | 0.0% | 2 | 4.2% | +2 | +4.2pp |

**Trace Usefulness Distribution**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| 1 | 0.0% | 2.1% | +2.1pp |
| Medium | 5.4% | 4.2% | -1.2pp |
| high | 7.1% | 6.2% | -0.9pp |
| medium | 76.8% | 85.4% | +8.6pp |
| neutral | 10.7% | 2.1% | -8.6pp |

**Translation Quality by Metric**:

<details>
<summary><b>BLEU</b> (click to expand)</summary>

**Overall Average**: Generic=1.656, Guided=2.105 (Δ +0.449)

**By Trace Type**:

| Trace Type | Generic | Guided | Δ |
|------------|---------|--------|---|
| CORRECT_LINGUISTIC_ANALYSIS | 0.910 | 1.120 | +0.210 |
| NONE | 2.880 | 1.330 | -1.550 |
| REPETITION | 0.940 | 0.000 | -0.940 |
| TRANSLATION_ATTEMPT | 2.650 | 2.240 | -0.410 |
| correct_linguistic_analysis | 0.900 | 0.000 | -0.900 |
| neutral | 0.000 | 3.730 | +3.730 |

**By Trace Usefulness**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| 1 | 0.000 | 0.180 | +0.180 |
| Medium | 0.930 | 1.610 | +0.680 |
| high | 0.970 | 0.820 | -0.150 |
| medium | 2.050 | 2.340 | +0.290 |
| neutral | 3.100 | 1.810 | -1.290 |

**Performance Range**:
- Generic: Best=NONE (2.880), Worst=correct_linguistic_analysis (0.900), Gap=1.980
- Guided: Best=neutral (3.730), Worst=CORRECT_LINGUISTIC_ANALYSIS (1.120), Gap=2.610

</details>

<details>
<summary><b>chrF++</b> (click to expand)</summary>

**Overall Average**: Generic=8.568, Guided=9.655 (Δ +1.087)

**By Trace Type**:

| Trace Type | Generic | Guided | Δ |
|------------|---------|--------|---|
| CORRECT_LINGUISTIC_ANALYSIS | 4.010 | 11.600 | +7.590 |
| NONE | 8.940 | 7.330 | -1.610 |
| REPETITION | 15.600 | 0.000 | -15.600 |
| TRANSLATION_ATTEMPT | 9.040 | 10.840 | +1.800 |
| correct_linguistic_analysis | 5.250 | 0.000 | -5.250 |
| neutral | 0.000 | 8.850 | +8.850 |

**By Trace Usefulness**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| 1 | 0.000 | 0.700 | +0.700 |
| Medium | 4.600 | 4.480 | -0.120 |
| high | 5.770 | 4.650 | -1.120 |
| medium | 7.570 | 11.490 | +3.920 |
| neutral | 8.610 | 9.830 | +1.220 |

**Performance Range**:
- Generic: Best=REPETITION (15.600), Worst=CORRECT_LINGUISTIC_ANALYSIS (4.010), Gap=11.590
- Guided: Best=CORRECT_LINGUISTIC_ANALYSIS (11.600), Worst=NONE (7.330), Gap=4.270

</details>

<details>
<summary><b>COMET</b> (click to expand)</summary>

**Overall Average**: Generic=0.388, Guided=0.417 (Δ +0.029)

**By Trace Type**:

| Trace Type | Generic | Guided | Δ |
|------------|---------|--------|---|
| CORRECT_LINGUISTIC_ANALYSIS | 0.330 | 0.400 | +0.070 |
| NONE | 0.430 | 0.370 | -0.060 |
| REPETITION | 0.390 | 0.000 | -0.390 |
| TRANSLATION_ATTEMPT | 0.380 | 0.410 | +0.030 |
| correct_linguistic_analysis | 0.410 | 0.000 | -0.410 |
| neutral | 0.000 | 0.490 | +0.490 |

**By Trace Usefulness**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| 1 | 0.000 | 0.250 | +0.250 |
| Medium | 0.350 | 0.440 | +0.090 |
| high | 0.310 | 0.400 | +0.090 |
| medium | 0.370 | 0.410 | +0.040 |
| neutral | 0.460 | 0.400 | -0.060 |

**Performance Range**:
- Generic: Best=NONE (0.430), Worst=CORRECT_LINGUISTIC_ANALYSIS (0.330), Gap=0.100
- Guided: Best=neutral (0.490), Worst=NONE (0.370), Gap=0.120

</details>

<details>
<summary><b>MetricX-24</b> (click to expand)</summary>

**Overall Average**: Generic=14.612, Guided=14.500 (Δ -0.112)

**By Trace Type**:

| Trace Type | Generic | Guided | Δ |
|------------|---------|--------|---|
| CORRECT_LINGUISTIC_ANALYSIS | 16.590 | 13.120 | -3.470 |
| NONE | 13.430 | 15.860 | +2.430 |
| REPETITION | 13.120 | 0.000 | -13.120 |
| TRANSLATION_ATTEMPT | 15.480 | 15.050 | -0.430 |
| correct_linguistic_analysis | 14.440 | 0.000 | -14.440 |
| neutral | 0.000 | 13.970 | +13.970 |

**By Trace Usefulness**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| 1 | 0.000 | 15.880 | +15.880 |
| Medium | 17.040 | 15.120 | -1.920 |
| high | 17.200 | 17.190 | -0.010 |
| medium | 15.560 | 14.740 | -0.820 |
| neutral | 13.140 | 15.690 | +2.550 |

**Performance Range**:
- Generic: Best=CORRECT_LINGUISTIC_ANALYSIS (16.590), Worst=REPETITION (13.120), Gap=3.470
- Guided: Best=NONE (15.860), Worst=CORRECT_LINGUISTIC_ANALYSIS (13.120), Gap=2.740

</details>

---

### 3.16 Lithuanian → English

**Examples**: 64 | **Avg Difficulty**: Generic=2.73, Guided=2.87

**Linguistic Phenomena Frequency**:

| Phenomenon | Generic | Guided |
|------------|---------|--------|
| complex_syntax | 34.9% | 59.7% |
| idiom | 1.6% | 0.0% |
| long_distance_dependency | 68.3% | 90.3% |
| named_entities | 79.4% | 75.8% |

**Trace Type Distribution**:

| Trace Type | Generic Count | Generic % | Guided Count | Guided % | Δ Count | Δ % |
|------------|---------------|-----------|--------------|----------|---------|-----|
| CORRECT_LINGUISTIC_ANALYSIS | 13 | 20.6% | 13 | 21.0% | 0 | +0.4pp |
| NONE | 16 | 25.4% | 25 | 40.3% | +9 | +14.9pp |
| REASONING | 0 | 0.0% | 1 | 1.6% | +1 | +1.6pp |
| REPETITION | 0 | 0.0% | 1 | 1.6% | +1 | +1.6pp |
| TRANSLATION_ATTEMPT | 14 | 22.2% | 12 | 19.4% | -2 | -2.8pp |
| correct_linguistic_analysis | 0 | 0.0% | 3 | 4.8% | +3 | +4.8pp |
| neutral | 20 | 31.7% | 7 | 11.3% | -13 | -20.4pp |

**Trace Usefulness Distribution**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| Medium | 1.6% | 0.0% | -1.6pp |
| helpful | 1.6% | 0.0% | -1.6pp |
| high | 17.5% | 24.2% | +6.7pp |
| medium | 33.3% | 46.8% | +13.5pp |
| neutral | 46.0% | 29.0% | -17.0pp |

**Translation Quality by Metric**:

<details>
<summary><b>BLEU</b> (click to expand)</summary>

**Overall Average**: Generic=12.755, Guided=14.303 (Δ +1.548)

**By Trace Type**:

| Trace Type | Generic | Guided | Δ |
|------------|---------|--------|---|
| CORRECT_LINGUISTIC_ANALYSIS | 12.210 | 14.690 | +2.480 |
| NONE | 9.850 | 12.460 | +2.610 |
| REASONING | 0.000 | 16.470 | +16.470 |
| REPETITION | 0.000 | 18.060 | +18.060 |
| TRANSLATION_ATTEMPT | 8.670 | 11.130 | +2.460 |
| correct_linguistic_analysis | 0.000 | 9.760 | +9.760 |
| neutral | 20.290 | 17.550 | -2.740 |

**By Trace Usefulness**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| Medium | 10.470 | 0.000 | -10.470 |
| helpful | 6.020 | 0.000 | -6.020 |
| high | 11.580 | 14.440 | +2.860 |
| medium | 8.750 | 11.630 | +2.880 |
| neutral | 17.790 | 14.930 | -2.860 |

**Performance Range**:
- Generic: Best=neutral (20.290), Worst=TRANSLATION_ATTEMPT (8.670), Gap=11.620
- Guided: Best=REPETITION (18.060), Worst=correct_linguistic_analysis (9.760), Gap=8.300

</details>

<details>
<summary><b>chrF++</b> (click to expand)</summary>

**Overall Average**: Generic=36.255, Guided=36.809 (Δ +0.554)

**By Trace Type**:

| Trace Type | Generic | Guided | Δ |
|------------|---------|--------|---|
| CORRECT_LINGUISTIC_ANALYSIS | 35.170 | 38.600 | +3.430 |
| NONE | 35.780 | 36.260 | +0.480 |
| REASONING | 0.000 | 34.780 | +34.780 |
| REPETITION | 0.000 | 46.210 | +46.210 |
| TRANSLATION_ATTEMPT | 31.990 | 33.000 | +1.010 |
| correct_linguistic_analysis | 0.000 | 30.080 | +30.080 |
| neutral | 42.080 | 38.730 | -3.350 |

**By Trace Usefulness**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| Medium | 33.850 | 0.000 | -33.850 |
| helpful | 26.450 | 0.000 | -26.450 |
| high | 33.130 | 36.560 | +3.430 |
| medium | 33.210 | 34.980 | +1.770 |
| neutral | 41.280 | 38.000 | -3.280 |

**Performance Range**:
- Generic: Best=neutral (42.080), Worst=TRANSLATION_ATTEMPT (31.990), Gap=10.090
- Guided: Best=REPETITION (46.210), Worst=correct_linguistic_analysis (30.080), Gap=16.130

</details>

<details>
<summary><b>COMET</b> (click to expand)</summary>

**Overall Average**: Generic=0.738, Guided=0.771 (Δ +0.034)

**By Trace Type**:

| Trace Type | Generic | Guided | Δ |
|------------|---------|--------|---|
| CORRECT_LINGUISTIC_ANALYSIS | 0.710 | 0.750 | +0.040 |
| NONE | 0.740 | 0.740 | 0.000 |
| REASONING | 0.000 | 0.830 | +0.830 |
| REPETITION | 0.000 | 0.850 | +0.850 |
| TRANSLATION_ATTEMPT | 0.710 | 0.720 | +0.010 |
| correct_linguistic_analysis | 0.000 | 0.760 | +0.760 |
| neutral | 0.790 | 0.750 | -0.040 |

**By Trace Usefulness**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| Medium | 0.830 | 0.000 | -0.830 |
| helpful | 0.760 | 0.000 | -0.760 |
| high | 0.710 | 0.750 | +0.040 |
| medium | 0.700 | 0.730 | +0.030 |
| neutral | 0.790 | 0.760 | -0.030 |

**Performance Range**:
- Generic: Best=neutral (0.790), Worst=CORRECT_LINGUISTIC_ANALYSIS (0.710), Gap=0.080
- Guided: Best=REPETITION (0.850), Worst=TRANSLATION_ATTEMPT (0.720), Gap=0.130

</details>

<details>
<summary><b>MetricX-24</b> (click to expand)</summary>

**Overall Average**: Generic=8.843, Guided=8.173 (Δ -0.670)

**By Trace Type**:

| Trace Type | Generic | Guided | Δ |
|------------|---------|--------|---|
| CORRECT_LINGUISTIC_ANALYSIS | 9.800 | 9.730 | -0.070 |
| NONE | 8.410 | 9.680 | +1.270 |
| REASONING | 0.000 | 7.280 | +7.280 |
| REPETITION | 0.000 | 3.450 | +3.450 |
| TRANSLATION_ATTEMPT | 10.310 | 10.290 | -0.020 |
| correct_linguistic_analysis | 0.000 | 8.390 | +8.390 |
| neutral | 6.850 | 8.390 | +1.540 |

**By Trace Usefulness**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| Medium | 2.450 | 0.000 | -2.450 |
| helpful | 6.220 | 0.000 | -6.220 |
| high | 10.640 | 9.980 | -0.660 |
| medium | 9.720 | 9.260 | -0.460 |
| neutral | 7.360 | 9.340 | +1.980 |

**Performance Range**:
- Generic: Best=TRANSLATION_ATTEMPT (10.310), Worst=neutral (6.850), Gap=3.460
- Guided: Best=TRANSLATION_ATTEMPT (10.290), Worst=REPETITION (3.450), Gap=6.840

</details>

---

### 3.17 Lithuanian → Turkish

**Examples**: 64 | **Avg Difficulty**: Generic=2.90, Guided=3.05

**Linguistic Phenomena Frequency**:

| Phenomenon | Generic | Guided |
|------------|---------|--------|
| ambiguity | 0.0% | 3.2% |
| complex_syntax | 52.4% | 71.0% |
| figurative_language | 0.0% | 3.2% |
| idiom | 0.0% | 3.2% |
| long_distance_dependency | 85.7% | 96.8% |
| named_entities | 65.1% | 64.5% |

**Trace Type Distribution**:

| Trace Type | Generic Count | Generic % | Guided Count | Guided % | Δ Count | Δ % |
|------------|---------------|-----------|--------------|----------|---------|-----|
| CORRECT_LINGUISTIC_ANALYSIS | 14 | 22.2% | 38 | 61.3% | +24 | +39.1pp |
| HALLUCINATED_RULE | 1 | 1.6% | 0 | 0.0% | -1 | -1.6pp |
| NONE | 10 | 15.9% | 11 | 17.7% | +1 | +1.8pp |
| TRANSLATION_ATTEMPT | 17 | 27.0% | 7 | 11.3% | -10 | -15.7pp |
| correct_linguistic_analysis | 3 | 4.8% | 3 | 4.8% | 0 | 0.0pp |
| neutral | 18 | 28.6% | 3 | 4.8% | -15 | -23.8pp |

**Trace Usefulness Distribution**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| 1 | 0.0% | 3.2% | +3.2pp |
| High | 1.6% | 3.2% | +1.6pp |
| Medium | 0.0% | 1.6% | +1.6pp |
| Neutral | 0.0% | 1.6% | +1.6pp |
| high | 9.5% | 12.9% | +3.4pp |
| medium | 42.9% | 67.7% | +24.8pp |
| neutral | 46.0% | 9.7% | -36.3pp |

**Translation Quality by Metric**:

<details>
<summary><b>BLEU</b> (click to expand)</summary>

**Overall Average**: Generic=4.078, Guided=5.952 (Δ +1.874)

**By Trace Type**:

| Trace Type | Generic | Guided | Δ |
|------------|---------|--------|---|
| CORRECT_LINGUISTIC_ANALYSIS | 3.910 | 3.810 | -0.100 |
| HALLUCINATED_RULE | 9.470 | 0.000 | -9.470 |
| NONE | 2.030 | 5.480 | +3.450 |
| TRANSLATION_ATTEMPT | 2.680 | 4.740 | +2.060 |
| correct_linguistic_analysis | 0.000 | 4.220 | +4.220 |
| neutral | 6.380 | 11.510 | +5.130 |

**By Trace Usefulness**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| 1 | 0.000 | 6.060 | +6.060 |
| High | 0.000 | 2.950 | +2.950 |
| Medium | 0.000 | 3.230 | +3.230 |
| Neutral | 0.000 | 5.820 | +5.820 |
| high | 2.460 | 2.790 | +0.330 |
| medium | 2.970 | 4.670 | +1.700 |
| neutral | 5.170 | 6.640 | +1.470 |

**Performance Range**:
- Generic: Best=HALLUCINATED_RULE (9.470), Worst=correct_linguistic_analysis (0.000), Gap=9.470
- Guided: Best=neutral (11.510), Worst=CORRECT_LINGUISTIC_ANALYSIS (3.810), Gap=7.700

</details>

<details>
<summary><b>chrF++</b> (click to expand)</summary>

**Overall Average**: Generic=14.377, Guided=22.478 (Δ +8.101)

**By Trace Type**:

| Trace Type | Generic | Guided | Δ |
|------------|---------|--------|---|
| CORRECT_LINGUISTIC_ANALYSIS | 14.950 | 20.850 | +5.900 |
| HALLUCINATED_RULE | 32.810 | 0.000 | -32.810 |
| NONE | 9.940 | 19.570 | +9.630 |
| TRANSLATION_ATTEMPT | 9.200 | 15.370 | +6.170 |
| correct_linguistic_analysis | 0.670 | 26.910 | +26.240 |
| neutral | 18.690 | 29.690 | +11.000 |

**By Trace Usefulness**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| 1 | 0.000 | 21.240 | +21.240 |
| High | 3.530 | 29.970 | +26.440 |
| Medium | 0.000 | 23.980 | +23.980 |
| Neutral | 0.000 | 26.670 | +26.670 |
| high | 10.300 | 18.800 | +8.500 |
| medium | 10.660 | 20.230 | +9.570 |
| neutral | 16.660 | 21.950 | +5.290 |

**Performance Range**:
- Generic: Best=HALLUCINATED_RULE (32.810), Worst=correct_linguistic_analysis (0.670), Gap=32.140
- Guided: Best=neutral (29.690), Worst=TRANSLATION_ATTEMPT (15.370), Gap=14.320

</details>

<details>
<summary><b>COMET</b> (click to expand)</summary>

**Overall Average**: Generic=0.455, Guided=0.564 (Δ +0.109)

**By Trace Type**:

| Trace Type | Generic | Guided | Δ |
|------------|---------|--------|---|
| CORRECT_LINGUISTIC_ANALYSIS | 0.480 | 0.550 | +0.070 |
| HALLUCINATED_RULE | 0.610 | 0.000 | -0.610 |
| NONE | 0.410 | 0.550 | +0.140 |
| TRANSLATION_ATTEMPT | 0.410 | 0.460 | +0.050 |
| correct_linguistic_analysis | 0.270 | 0.520 | +0.250 |
| neutral | 0.550 | 0.740 | +0.190 |

**By Trace Usefulness**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| 1 | 0.000 | 0.610 | +0.610 |
| High | 0.280 | 0.510 | +0.230 |
| Medium | 0.000 | 0.740 | +0.740 |
| Neutral | 0.000 | 0.750 | +0.750 |
| high | 0.420 | 0.570 | +0.150 |
| medium | 0.420 | 0.520 | +0.100 |
| neutral | 0.520 | 0.600 | +0.080 |

**Performance Range**:
- Generic: Best=HALLUCINATED_RULE (0.610), Worst=correct_linguistic_analysis (0.270), Gap=0.340
- Guided: Best=neutral (0.740), Worst=TRANSLATION_ATTEMPT (0.460), Gap=0.280

</details>

<details>
<summary><b>MetricX-24</b> (click to expand)</summary>

**Overall Average**: Generic=14.895, Guided=13.584 (Δ -1.311)

**By Trace Type**:

| Trace Type | Generic | Guided | Δ |
|------------|---------|--------|---|
| CORRECT_LINGUISTIC_ANALYSIS | 14.960 | 14.090 | -0.870 |
| HALLUCINATED_RULE | 16.380 | 0.000 | -16.380 |
| NONE | 14.040 | 14.720 | +0.680 |
| TRANSLATION_ATTEMPT | 15.540 | 15.400 | -0.140 |
| correct_linguistic_analysis | 14.580 | 14.190 | -0.390 |
| neutral | 13.870 | 9.520 | -4.350 |

**By Trace Usefulness**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| 1 | 0.000 | 14.810 | +14.810 |
| High | 14.940 | 13.060 | -1.880 |
| Medium | 0.000 | 15.250 | +15.250 |
| Neutral | 0.000 | 11.060 | +11.060 |
| high | 15.360 | 14.040 | -1.320 |
| medium | 15.320 | 14.490 | -0.830 |
| neutral | 13.900 | 12.200 | -1.700 |

**Performance Range**:
- Generic: Best=HALLUCINATED_RULE (16.380), Worst=neutral (13.870), Gap=2.510
- Guided: Best=TRANSLATION_ATTEMPT (15.400), Worst=neutral (9.520), Gap=5.880

</details>

---

### 3.18 Lithuanian → Xhosa

**Examples**: 64 | **Avg Difficulty**: Generic=3.00, Guided=3.27

**Linguistic Phenomena Frequency**:

| Phenomenon | Generic | Guided |
|------------|---------|--------|
| ambiguity | 0.0% | 2.0% |
| complex_syntax | 57.8% | 80.4% |
| figurative_language | 0.0% | 2.0% |
| idiom | 1.6% | 2.0% |
| long_distance_dependency | 92.2% | 100.0% |
| named_entities | 64.1% | 56.9% |

**Trace Type Distribution**:

| Trace Type | Generic Count | Generic % | Guided Count | Guided % | Δ Count | Δ % |
|------------|---------------|-----------|--------------|----------|---------|-----|
| CORRECT_LINGUISTIC_ANALYSIS | 16 | 25.0% | 12 | 23.5% | -4 | -1.5pp |
| NONE | 12 | 18.8% | 5 | 9.8% | -7 | -9.0pp |
| REASONING | 1 | 1.6% | 0 | 0.0% | -1 | -1.6pp |
| REPETITION | 1 | 1.6% | 1 | 2.0% | 0 | +0.4pp |
| REVISION_OF_TRANSLATION | 0 | 0.0% | 1 | 2.0% | +1 | +2.0pp |
| TRANSLATION_ATTEMPT | 28 | 43.8% | 30 | 58.8% | +2 | +15.0pp |
| correct_linguistic_analysis | 0 | 0.0% | 1 | 2.0% | +1 | +2.0pp |
| correction | 1 | 1.6% | 0 | 0.0% | -1 | -1.6pp |
| neutral | 4 | 6.2% | 1 | 2.0% | -3 | -4.2pp |
| null | 1 | 1.6% | 0 | 0.0% | -1 | -1.6pp |

**Trace Usefulness Distribution**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| 2 | 0.0% | 2.0% | +2.0pp |
| High | 1.6% | 3.9% | +2.3pp |
| Medium | 6.2% | 11.8% | +5.6pp |
| high | 7.8% | 7.8% | 0.0pp |
| medium | 57.8% | 70.6% | +12.8pp |
| neutral | 26.6% | 3.9% | -22.7pp |

**Translation Quality by Metric**:

<details>
<summary><b>BLEU</b> (click to expand)</summary>

**Overall Average**: Generic=2.500, Guided=2.811 (Δ +0.311)

**By Trace Type**:

| Trace Type | Generic | Guided | Δ |
|------------|---------|--------|---|
| CORRECT_LINGUISTIC_ANALYSIS | 2.590 | 2.400 | -0.190 |
| NONE | 1.780 | 7.400 | +5.620 |
| REASONING | 0.880 | 0.000 | -0.880 |
| REPETITION | 0.190 | 1.200 | +1.010 |
| REVISION_OF_TRANSLATION | 0.000 | 1.490 | +1.490 |
| TRANSLATION_ATTEMPT | 2.900 | 2.710 | -0.190 |
| correct_linguistic_analysis | 0.000 | 2.830 | +2.830 |
| correction | 7.730 | 0.000 | -7.730 |
| neutral | 3.110 | 1.650 | -1.460 |
| null | 0.820 | 0.000 | -0.820 |

**By Trace Usefulness**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| 2 | 0.000 | 1.580 | +1.580 |
| High | 5.240 | 1.070 | -4.170 |
| Medium | 1.910 | 2.210 | +0.300 |
| high | 1.390 | 1.160 | -0.230 |
| medium | 2.390 | 3.480 | +1.090 |
| neutral | 3.400 | 3.590 | +0.190 |

**Performance Range**:
- Generic: Best=correction (7.730), Worst=REPETITION (0.190), Gap=7.540
- Guided: Best=NONE (7.400), Worst=REPETITION (1.200), Gap=6.200

</details>

<details>
<summary><b>chrF++</b> (click to expand)</summary>

**Overall Average**: Generic=11.311, Guided=13.334 (Δ +2.023)

**By Trace Type**:

| Trace Type | Generic | Guided | Δ |
|------------|---------|--------|---|
| CORRECT_LINGUISTIC_ANALYSIS | 13.010 | 14.020 | +1.010 |
| NONE | 11.830 | 16.150 | +4.320 |
| REASONING | 7.200 | 0.000 | -7.200 |
| REPETITION | 10.210 | 10.250 | +0.040 |
| REVISION_OF_TRANSLATION | 0.000 | 14.850 | +14.850 |
| TRANSLATION_ATTEMPT | 13.350 | 12.800 | -0.550 |
| correct_linguistic_analysis | 0.000 | 15.840 | +15.840 |
| correction | 14.970 | 0.000 | -14.970 |
| neutral | 10.680 | 9.430 | -1.250 |
| null | 9.240 | 0.000 | -9.240 |

**By Trace Usefulness**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| 2 | 0.000 | 8.550 | +8.550 |
| High | 18.110 | 12.010 | -6.100 |
| Medium | 12.040 | 11.240 | -0.800 |
| high | 11.910 | 12.500 | +0.590 |
| medium | 12.840 | 14.090 | +1.250 |
| neutral | 12.190 | 12.950 | +0.760 |

**Performance Range**:
- Generic: Best=correction (14.970), Worst=REASONING (7.200), Gap=7.770
- Guided: Best=NONE (16.150), Worst=neutral (9.430), Gap=6.720

</details>

<details>
<summary><b>COMET</b> (click to expand)</summary>

**Overall Average**: Generic=0.407, Guided=0.399 (Δ -0.009)

**By Trace Type**:

| Trace Type | Generic | Guided | Δ |
|------------|---------|--------|---|
| CORRECT_LINGUISTIC_ANALYSIS | 0.370 | 0.400 | +0.030 |
| NONE | 0.400 | 0.430 | +0.030 |
| REASONING | 0.380 | 0.000 | -0.380 |
| REPETITION | 0.300 | 0.420 | +0.120 |
| REVISION_OF_TRANSLATION | 0.000 | 0.380 | +0.380 |
| TRANSLATION_ATTEMPT | 0.380 | 0.360 | -0.020 |
| correct_linguistic_analysis | 0.000 | 0.410 | +0.410 |
| correction | 0.720 | 0.000 | -0.720 |
| neutral | 0.360 | 0.390 | +0.030 |
| null | 0.350 | 0.000 | -0.350 |

**By Trace Usefulness**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| 2 | 0.000 | 0.260 | +0.260 |
| High | 0.300 | 0.380 | +0.080 |
| Medium | 0.350 | 0.390 | +0.040 |
| high | 0.340 | 0.320 | -0.020 |
| medium | 0.390 | 0.380 | -0.010 |
| neutral | 0.410 | 0.440 | +0.030 |

**Performance Range**:
- Generic: Best=correction (0.720), Worst=REPETITION (0.300), Gap=0.420
- Guided: Best=NONE (0.430), Worst=TRANSLATION_ATTEMPT (0.360), Gap=0.070

</details>

<details>
<summary><b>MetricX-24</b> (click to expand)</summary>

**Overall Average**: Generic=15.734, Guided=14.757 (Δ -0.977)

**By Trace Type**:

| Trace Type | Generic | Guided | Δ |
|------------|---------|--------|---|
| CORRECT_LINGUISTIC_ANALYSIS | 15.620 | 14.970 | -0.650 |
| NONE | 14.880 | 15.510 | +0.630 |
| REASONING | 17.120 | 0.000 | -17.120 |
| REPETITION | 15.750 | 13.500 | -2.250 |
| REVISION_OF_TRANSLATION | 0.000 | 16.500 | +16.500 |
| TRANSLATION_ATTEMPT | 15.470 | 15.250 | -0.220 |
| correct_linguistic_analysis | 0.000 | 12.690 | +12.690 |
| correction | 15.060 | 0.000 | -15.060 |
| neutral | 15.970 | 14.880 | -1.090 |
| null | 16.000 | 0.000 | -16.000 |

**By Trace Usefulness**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| 2 | 0.000 | 18.250 | +18.250 |
| High | 17.250 | 15.750 | -1.500 |
| Medium | 15.270 | 15.260 | -0.010 |
| high | 16.050 | 14.980 | -1.070 |
| medium | 15.620 | 15.010 | -0.610 |
| neutral | 14.890 | 15.380 | +0.490 |

**Performance Range**:
- Generic: Best=REASONING (17.120), Worst=NONE (14.880), Gap=2.240
- Guided: Best=REVISION_OF_TRANSLATION (16.500), Worst=correct_linguistic_analysis (12.690), Gap=3.810

</details>

---

### 3.19 Turkish → English

**Examples**: 64 | **Avg Difficulty**: Generic=2.48, Guided=2.76

**Linguistic Phenomena Frequency**:

| Phenomenon | Generic | Guided |
|------------|---------|--------|
| ambiguity | 1.6% | 1.6% |
| complex_syntax | 29.7% | 68.3% |
| figurative_language | 1.6% | 1.6% |
| idiom | 1.6% | 1.6% |
| long_distance_dependency | 75.0% | 93.7% |
| named_entities | 81.2% | 85.7% |

**Trace Type Distribution**:

| Trace Type | Generic Count | Generic % | Guided Count | Guided % | Δ Count | Δ % |
|------------|---------------|-----------|--------------|----------|---------|-----|
| CORRECT_LINGUISTIC_ANALYSIS | 6 | 9.4% | 8 | 12.7% | +2 | +3.3pp |
| NONE | 19 | 29.7% | 25 | 39.7% | +6 | +10.0pp |
| REASONING | 1 | 1.6% | 0 | 0.0% | -1 | -1.6pp |
| TRANSLATION_ATTEMPT | 11 | 17.2% | 18 | 28.6% | +7 | +11.4pp |
| VACUOUS_FILLER | 1 | 1.6% | 0 | 0.0% | -1 | -1.6pp |
| correct_linguistic_analysis | 2 | 3.1% | 2 | 3.2% | 0 | +0.1pp |
| neutral | 24 | 37.5% | 10 | 15.9% | -14 | -21.6pp |

**Trace Usefulness Distribution**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| 1 | 1.6% | 1.6% | 0.0pp |
| HIGH | 1.6% | 0.0% | -1.6pp |
| Neutral | 1.6% | 0.0% | -1.6pp |
| high | 25.0% | 17.5% | -7.5pp |
| medium | 25.0% | 55.6% | +30.6pp |
| neutral | 45.3% | 25.4% | -19.9pp |

**Translation Quality by Metric**:

<details>
<summary><b>BLEU</b> (click to expand)</summary>

**Overall Average**: Generic=19.150, Guided=16.702 (Δ -2.448)

**By Trace Type**:

| Trace Type | Generic | Guided | Δ |
|------------|---------|--------|---|
| CORRECT_LINGUISTIC_ANALYSIS | 34.970 | 11.280 | -23.690 |
| NONE | 15.800 | 21.290 | +5.490 |
| REASONING | 19.820 | 0.000 | -19.820 |
| TRANSLATION_ATTEMPT | 10.040 | 19.840 | +9.800 |
| VACUOUS_FILLER | 9.850 | 0.000 | -9.850 |
| correct_linguistic_analysis | 21.790 | 6.370 | -15.420 |
| neutral | 21.780 | 24.730 | +2.950 |

**By Trace Usefulness**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| 1 | 2.460 | 21.710 | +19.250 |
| HIGH | 11.680 | 0.000 | -11.680 |
| Neutral | 33.800 | 0.000 | -33.800 |
| high | 22.010 | 10.720 | -11.290 |
| medium | 13.080 | 19.640 | +6.560 |
| neutral | 20.940 | 25.790 | +4.850 |

**Performance Range**:
- Generic: Best=CORRECT_LINGUISTIC_ANALYSIS (34.970), Worst=VACUOUS_FILLER (9.850), Gap=25.120
- Guided: Best=neutral (24.730), Worst=correct_linguistic_analysis (6.370), Gap=18.360

</details>

<details>
<summary><b>chrF++</b> (click to expand)</summary>

**Overall Average**: Generic=45.919, Guided=39.118 (Δ -6.801)

**By Trace Type**:

| Trace Type | Generic | Guided | Δ |
|------------|---------|--------|---|
| CORRECT_LINGUISTIC_ANALYSIS | 56.680 | 34.920 | -21.760 |
| NONE | 39.830 | 43.040 | +3.210 |
| REASONING | 41.880 | 0.000 | -41.880 |
| TRANSLATION_ATTEMPT | 35.270 | 41.880 | +6.610 |
| VACUOUS_FILLER | 57.710 | 0.000 | -57.710 |
| correct_linguistic_analysis | 47.290 | 30.100 | -17.190 |
| neutral | 42.770 | 45.650 | +2.880 |

**By Trace Usefulness**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| 1 | 20.780 | 41.720 | +20.940 |
| HIGH | 24.720 | 0.000 | -24.720 |
| Neutral | 56.450 | 0.000 | -56.450 |
| high | 46.740 | 34.930 | -11.810 |
| medium | 37.360 | 40.880 | +3.520 |
| neutral | 43.380 | 48.070 | +4.690 |

**Performance Range**:
- Generic: Best=VACUOUS_FILLER (57.710), Worst=TRANSLATION_ATTEMPT (35.270), Gap=22.440
- Guided: Best=neutral (45.650), Worst=correct_linguistic_analysis (30.100), Gap=15.550

</details>

<details>
<summary><b>COMET</b> (click to expand)</summary>

**Overall Average**: Generic=0.827, Guided=0.800 (Δ -0.027)

**By Trace Type**:

| Trace Type | Generic | Guided | Δ |
|------------|---------|--------|---|
| CORRECT_LINGUISTIC_ANALYSIS | 0.870 | 0.730 | -0.140 |
| NONE | 0.830 | 0.850 | +0.020 |
| REASONING | 0.700 | 0.000 | -0.700 |
| TRANSLATION_ATTEMPT | 0.810 | 0.790 | -0.020 |
| VACUOUS_FILLER | 0.870 | 0.000 | -0.870 |
| correct_linguistic_analysis | 0.870 | 0.760 | -0.110 |
| neutral | 0.840 | 0.870 | +0.030 |

**By Trace Usefulness**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| 1 | 0.790 | 0.770 | -0.020 |
| HIGH | 0.760 | 0.000 | -0.760 |
| Neutral | 0.880 | 0.000 | -0.880 |
| high | 0.850 | 0.740 | -0.110 |
| medium | 0.810 | 0.820 | +0.010 |
| neutral | 0.830 | 0.870 | +0.040 |

**Performance Range**:
- Generic: Best=CORRECT_LINGUISTIC_ANALYSIS (0.870), Worst=REASONING (0.700), Gap=0.170
- Guided: Best=neutral (0.870), Worst=CORRECT_LINGUISTIC_ANALYSIS (0.730), Gap=0.140

</details>

<details>
<summary><b>MetricX-24</b> (click to expand)</summary>

**Overall Average**: Generic=6.799, Guided=6.124 (Δ -0.675)

**By Trace Type**:

| Trace Type | Generic | Guided | Δ |
|------------|---------|--------|---|
| CORRECT_LINGUISTIC_ANALYSIS | 6.090 | 7.700 | +1.610 |
| NONE | 5.460 | 5.450 | -0.010 |
| REASONING | 9.440 | 0.000 | -9.440 |
| TRANSLATION_ATTEMPT | 7.430 | 6.560 | -0.870 |
| VACUOUS_FILLER | 10.310 | 0.000 | -10.310 |
| correct_linguistic_analysis | 3.230 | 7.730 | +4.500 |
| neutral | 5.630 | 3.180 | -2.450 |

**By Trace Usefulness**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| 1 | 7.780 | 8.880 | +1.100 |
| HIGH | 12.380 | 0.000 | -12.380 |
| Neutral | 1.630 | 0.000 | -1.630 |
| high | 6.330 | 7.920 | +1.590 |
| medium | 6.430 | 5.710 | -0.720 |
| neutral | 5.430 | 4.220 | -1.210 |

**Performance Range**:
- Generic: Best=VACUOUS_FILLER (10.310), Worst=correct_linguistic_analysis (3.230), Gap=7.080
- Guided: Best=correct_linguistic_analysis (7.730), Worst=neutral (3.180), Gap=4.550

</details>

---

### 3.20 Turkish → Finnish

**Examples**: 64 | **Avg Difficulty**: Generic=2.83, Guided=3.02

**Linguistic Phenomena Frequency**:

| Phenomenon | Generic | Guided |
|------------|---------|--------|
| ambiguity | 3.1% | 11.5% |
| complex_syntax | 56.2% | 86.9% |
| figurative_language | 3.1% | 11.5% |
| idiom | 3.1% | 11.5% |
| long_distance_dependency | 87.5% | 96.7% |
| named_entities | 79.7% | 67.2% |

**Trace Type Distribution**:

| Trace Type | Generic Count | Generic % | Guided Count | Guided % | Δ Count | Δ % |
|------------|---------------|-----------|--------------|----------|---------|-----|
| CORRECT_LINGUISTIC_ANALYSIS | 9 | 14.1% | 19 | 31.1% | +10 | +17.0pp |
| NONE | 22 | 34.4% | 8 | 13.1% | -14 | -21.3pp |
| REPETITION | 0 | 0.0% | 1 | 1.6% | +1 | +1.6pp |
| TRANSLATION_ATTEMPT | 16 | 25.0% | 16 | 26.2% | 0 | +1.2pp |
| correct_linguistic_analysis | 4 | 6.2% | 6 | 9.8% | +2 | +3.6pp |
| neutral | 13 | 20.3% | 11 | 18.0% | -2 | -2.3pp |

**Trace Usefulness Distribution**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| 1 | 1.6% | 0.0% | -1.6pp |
| 2 | 1.6% | 8.2% | +6.6pp |
| 3 | 0.0% | 1.6% | +1.6pp |
| High | 4.7% | 0.0% | -4.7pp |
| Medium | 0.0% | 3.3% | +3.3pp |
| Medium. The tracing of the distance traveled is relevant to understanding the context of the announcement. | 1.6% | 0.0% | -1.6pp |
| Neutral | 1.6% | 3.3% | +1.7pp |
| helpful | 3.1% | 0.0% | -3.1pp |
| high | 15.6% | 14.8% | -0.8pp |
| medium | 43.8% | 60.7% | +16.9pp |
| neutral | 26.6% | 8.2% | -18.4pp |

**Translation Quality by Metric**:

<details>
<summary><b>BLEU</b> (click to expand)</summary>

**Overall Average**: Generic=5.690, Guided=6.110 (Δ +0.420)

**By Trace Type**:

| Trace Type | Generic | Guided | Δ |
|------------|---------|--------|---|
| CORRECT_LINGUISTIC_ANALYSIS | 4.880 | 5.500 | +0.620 |
| NONE | 8.050 | 13.540 | +5.490 |
| REPETITION | 0.000 | 1.760 | +1.760 |
| TRANSLATION_ATTEMPT | 5.290 | 5.570 | +0.280 |
| correct_linguistic_analysis | 6.020 | 5.850 | -0.170 |
| neutral | 4.210 | 4.440 | +0.230 |

**By Trace Usefulness**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| 1 | 4.230 | 0.000 | -4.230 |
| 2 | 3.180 | 12.220 | +9.040 |
| 3 | 0.000 | 7.310 | +7.310 |
| High | 4.390 | 0.000 | -4.390 |
| Medium | 0.000 | 1.250 | +1.250 |
| Medium. The tracing of the distance traveled is relevant to understanding the context of the announcement. | 13.830 | 0.000 | -13.830 |
| Neutral | 9.590 | 16.890 | +7.300 |
| helpful | 12.610 | 0.000 | -12.610 |
| high | 5.580 | 4.760 | -0.820 |
| medium | 4.910 | 5.420 | +0.510 |
| neutral | 7.180 | 7.920 | +0.740 |

**Performance Range**:
- Generic: Best=NONE (8.050), Worst=neutral (4.210), Gap=3.840
- Guided: Best=NONE (13.540), Worst=REPETITION (1.760), Gap=11.780

</details>

<details>
<summary><b>chrF++</b> (click to expand)</summary>

**Overall Average**: Generic=21.080, Guided=24.682 (Δ +3.602)

**By Trace Type**:

| Trace Type | Generic | Guided | Δ |
|------------|---------|--------|---|
| CORRECT_LINGUISTIC_ANALYSIS | 24.270 | 24.490 | +0.220 |
| NONE | 28.240 | 33.000 | +4.760 |
| REPETITION | 0.000 | 20.520 | +20.520 |
| TRANSLATION_ATTEMPT | 20.150 | 19.920 | -0.230 |
| correct_linguistic_analysis | 17.020 | 28.650 | +11.630 |
| neutral | 15.720 | 21.510 | +5.790 |

**By Trace Usefulness**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| 1 | 32.100 | 0.000 | -32.100 |
| 2 | 23.740 | 31.410 | +7.670 |
| 3 | 0.000 | 23.610 | +23.610 |
| High | 28.750 | 0.000 | -28.750 |
| Medium | 0.000 | 15.450 | +15.450 |
| Medium. The tracing of the distance traveled is relevant to understanding the context of the announcement. | 36.550 | 0.000 | -36.550 |
| Neutral | 36.750 | 38.540 | +1.790 |
| helpful | 34.100 | 0.000 | -34.100 |
| high | 22.700 | 20.480 | -2.220 |
| medium | 20.100 | 23.370 | +3.270 |
| neutral | 21.240 | 27.900 | +6.660 |

**Performance Range**:
- Generic: Best=NONE (28.240), Worst=neutral (15.720), Gap=12.520
- Guided: Best=NONE (33.000), Worst=TRANSLATION_ATTEMPT (19.920), Gap=13.080

</details>

<details>
<summary><b>COMET</b> (click to expand)</summary>

**Overall Average**: Generic=0.614, Guided=0.652 (Δ +0.038)

**By Trace Type**:

| Trace Type | Generic | Guided | Δ |
|------------|---------|--------|---|
| CORRECT_LINGUISTIC_ANALYSIS | 0.570 | 0.610 | +0.040 |
| NONE | 0.660 | 0.720 | +0.060 |
| REPETITION | 0.000 | 0.740 | +0.740 |
| TRANSLATION_ATTEMPT | 0.610 | 0.580 | -0.030 |
| correct_linguistic_analysis | 0.650 | 0.610 | -0.040 |
| neutral | 0.580 | 0.650 | +0.070 |

**By Trace Usefulness**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| 1 | 0.860 | 0.000 | -0.860 |
| 2 | 0.480 | 0.670 | +0.190 |
| 3 | 0.000 | 0.550 | +0.550 |
| High | 0.540 | 0.000 | -0.540 |
| Medium | 0.000 | 0.380 | +0.380 |
| Medium. The tracing of the distance traveled is relevant to understanding the context of the announcement. | 0.570 | 0.000 | -0.570 |
| Neutral | 0.680 | 0.670 | -0.010 |
| helpful | 0.770 | 0.000 | -0.770 |
| high | 0.630 | 0.600 | -0.030 |
| medium | 0.610 | 0.630 | +0.020 |
| neutral | 0.610 | 0.680 | +0.070 |

**Performance Range**:
- Generic: Best=NONE (0.660), Worst=CORRECT_LINGUISTIC_ANALYSIS (0.570), Gap=0.090
- Guided: Best=REPETITION (0.740), Worst=TRANSLATION_ATTEMPT (0.580), Gap=0.160

</details>

<details>
<summary><b>MetricX-24</b> (click to expand)</summary>

**Overall Average**: Generic=12.842, Guided=11.907 (Δ -0.935)

**By Trace Type**:

| Trace Type | Generic | Guided | Δ |
|------------|---------|--------|---|
| CORRECT_LINGUISTIC_ANALYSIS | 13.160 | 12.260 | -0.900 |
| NONE | 10.640 | 10.080 | -0.560 |
| REPETITION | 0.000 | 8.190 | +8.190 |
| TRANSLATION_ATTEMPT | 13.160 | 14.090 | +0.930 |
| correct_linguistic_analysis | 13.750 | 14.430 | +0.680 |
| neutral | 13.500 | 12.390 | -1.110 |

**By Trace Usefulness**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| 1 | 7.340 | 0.000 | -7.340 |
| 2 | 11.060 | 10.460 | -0.600 |
| 3 | 0.000 | 15.560 | +15.560 |
| High | 11.880 | 0.000 | -11.880 |
| Medium | 0.000 | 17.880 | +17.880 |
| Medium. The tracing of the distance traveled is relevant to understanding the context of the announcement. | 11.060 | 0.000 | -11.060 |
| Neutral | 10.440 | 12.910 | +2.470 |
| helpful | 7.730 | 0.000 | -7.730 |
| high | 11.840 | 13.110 | +1.270 |
| medium | 13.540 | 12.830 | -0.710 |
| neutral | 12.070 | 9.650 | -2.420 |

**Performance Range**:
- Generic: Best=correct_linguistic_analysis (13.750), Worst=NONE (10.640), Gap=3.110
- Guided: Best=correct_linguistic_analysis (14.430), Worst=REPETITION (8.190), Gap=6.240

</details>

---

### 3.21 Turkish → Lithuanian

**Examples**: 64 | **Avg Difficulty**: Generic=2.70, Guided=3.08

**Linguistic Phenomena Frequency**:

| Phenomenon | Generic | Guided |
|------------|---------|--------|
| ambiguity | 3.1% | 11.3% |
| complex_syntax | 59.4% | 77.4% |
| figurative_language | 1.6% | 11.3% |
| idiom | 1.6% | 11.3% |
| long_distance_dependency | 87.5% | 98.4% |
| named_entities | 71.9% | 67.7% |

**Trace Type Distribution**:

| Trace Type | Generic Count | Generic % | Guided Count | Guided % | Δ Count | Δ % |
|------------|---------------|-----------|--------------|----------|---------|-----|
| CORRECT_LINGUISTIC_ANALYSIS | 19 | 29.7% | 44 | 71.0% | +25 | +41.3pp |
| NONE | 19 | 29.7% | 1 | 1.6% | -18 | -28.1pp |
| REASONING | 0 | 0.0% | 1 | 1.6% | +1 | +1.6pp |
| TRANSLATION_ATTEMPT | 10 | 15.6% | 8 | 12.9% | -2 | -2.7pp |
| correct_linguistic_analysis | 2 | 3.1% | 4 | 6.5% | +2 | +3.4pp |
| neutral | 14 | 21.9% | 4 | 6.5% | -10 | -15.4pp |

**Trace Usefulness Distribution**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| 2 | 0.0% | 4.8% | +4.8pp |
| 3 | 1.6% | 4.8% | +3.2pp |
| High | 1.6% | 3.2% | +1.6pp |
| Medium | 0.0% | 3.2% | +3.2pp |
| Medium (the translation is accurate but could be refined for a more natural flow) | 0.0% | 1.6% | +1.6pp |
| helpful | 1.6% | 0.0% | -1.6pp |
| high | 10.9% | 19.4% | +8.5pp |
| medium | 39.1% | 54.8% | +15.7pp |
| neutral | 45.3% | 8.1% | -37.2pp |

**Translation Quality by Metric**:

<details>
<summary><b>BLEU</b> (click to expand)</summary>

**Overall Average**: Generic=3.392, Guided=5.595 (Δ +2.203)

**By Trace Type**:

| Trace Type | Generic | Guided | Δ |
|------------|---------|--------|---|
| CORRECT_LINGUISTIC_ANALYSIS | 3.250 | 3.600 | +0.350 |
| NONE | 3.380 | 3.430 | +0.050 |
| REASONING | 0.000 | 15.710 | +15.710 |
| TRANSLATION_ATTEMPT | 2.340 | 3.250 | +0.910 |
| correct_linguistic_analysis | 1.500 | 3.930 | +2.430 |
| neutral | 6.490 | 3.650 | -2.840 |

**By Trace Usefulness**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| 2 | 0.000 | 0.930 | +0.930 |
| 3 | 2.780 | 3.650 | +0.870 |
| High | 0.990 | 0.700 | -0.290 |
| Medium | 0.000 | 2.370 | +2.370 |
| Medium (the translation is accurate but could be refined for a more natural flow) | 0.000 | 0.990 | +0.990 |
| helpful | 2.290 | 0.000 | -2.290 |
| high | 2.090 | 2.590 | +0.500 |
| medium | 2.950 | 4.960 | +2.010 |
| neutral | 5.130 | 2.690 | -2.440 |

**Performance Range**:
- Generic: Best=neutral (6.490), Worst=correct_linguistic_analysis (1.500), Gap=4.990
- Guided: Best=REASONING (15.710), Worst=TRANSLATION_ATTEMPT (3.250), Gap=12.460

</details>

<details>
<summary><b>chrF++</b> (click to expand)</summary>

**Overall Average**: Generic=16.364, Guided=20.823 (Δ +4.459)

**By Trace Type**:

| Trace Type | Generic | Guided | Δ |
|------------|---------|--------|---|
| CORRECT_LINGUISTIC_ANALYSIS | 15.330 | 18.480 | +3.150 |
| NONE | 16.650 | 11.900 | -4.750 |
| REASONING | 0.000 | 38.830 | +38.830 |
| TRANSLATION_ATTEMPT | 16.520 | 20.130 | +3.610 |
| correct_linguistic_analysis | 13.360 | 20.590 | +7.230 |
| neutral | 19.960 | 15.010 | -4.950 |

**By Trace Usefulness**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| 2 | 0.000 | 15.420 | +15.420 |
| 3 | 26.640 | 21.950 | -4.690 |
| High | 13.060 | 7.880 | -5.180 |
| Medium | 0.000 | 20.490 | +20.490 |
| Medium (the translation is accurate but could be refined for a more natural flow) | 0.000 | 19.120 | +19.120 |
| helpful | 9.500 | 0.000 | -9.500 |
| high | 14.540 | 18.950 | +4.410 |
| medium | 16.480 | 19.750 | +3.270 |
| neutral | 17.790 | 16.110 | -1.680 |

**Performance Range**:
- Generic: Best=neutral (19.960), Worst=correct_linguistic_analysis (13.360), Gap=6.600
- Guided: Best=REASONING (38.830), Worst=NONE (11.900), Gap=26.930

</details>

<details>
<summary><b>COMET</b> (click to expand)</summary>

**Overall Average**: Generic=0.574, Guided=0.555 (Δ -0.019)

**By Trace Type**:

| Trace Type | Generic | Guided | Δ |
|------------|---------|--------|---|
| CORRECT_LINGUISTIC_ANALYSIS | 0.480 | 0.480 | 0.000 |
| NONE | 0.580 | 0.560 | -0.020 |
| REASONING | 0.000 | 0.750 | +0.750 |
| TRANSLATION_ATTEMPT | 0.580 | 0.470 | -0.110 |
| correct_linguistic_analysis | 0.610 | 0.470 | -0.140 |
| neutral | 0.620 | 0.600 | -0.020 |

**By Trace Usefulness**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| 2 | 0.000 | 0.510 | +0.510 |
| 3 | 0.390 | 0.380 | -0.010 |
| High | 0.440 | 0.410 | -0.030 |
| Medium | 0.000 | 0.480 | +0.480 |
| Medium (the translation is accurate but could be refined for a more natural flow) | 0.000 | 0.480 | +0.480 |
| helpful | 0.670 | 0.000 | -0.670 |
| high | 0.460 | 0.440 | -0.020 |
| medium | 0.560 | 0.530 | -0.030 |
| neutral | 0.590 | 0.520 | -0.070 |

**Performance Range**:
- Generic: Best=neutral (0.620), Worst=CORRECT_LINGUISTIC_ANALYSIS (0.480), Gap=0.140
- Guided: Best=REASONING (0.750), Worst=correct_linguistic_analysis (0.470), Gap=0.280

</details>

<details>
<summary><b>MetricX-24</b> (click to expand)</summary>

**Overall Average**: Generic=14.316, Guided=15.470 (Δ +1.154)

**By Trace Type**:

| Trace Type | Generic | Guided | Δ |
|------------|---------|--------|---|
| CORRECT_LINGUISTIC_ANALYSIS | 15.890 | 16.590 | +0.700 |
| NONE | 14.160 | 15.810 | +1.650 |
| REASONING | 0.000 | 13.620 | +13.620 |
| TRANSLATION_ATTEMPT | 14.740 | 16.730 | +1.990 |
| correct_linguistic_analysis | 13.060 | 15.770 | +2.710 |
| neutral | 13.730 | 14.300 | +0.570 |

**By Trace Usefulness**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| 2 | 0.000 | 14.150 | +14.150 |
| 3 | 17.880 | 18.620 | +0.740 |
| High | 15.380 | 15.160 | -0.220 |
| Medium | 0.000 | 17.000 | +17.000 |
| Medium (the translation is accurate but could be refined for a more natural flow) | 0.000 | 15.190 | +15.190 |
| helpful | 12.750 | 0.000 | -12.750 |
| high | 15.940 | 17.770 | +1.830 |
| medium | 15.430 | 15.900 | +0.470 |
| neutral | 13.570 | 16.300 | +2.730 |

**Performance Range**:
- Generic: Best=CORRECT_LINGUISTIC_ANALYSIS (15.890), Worst=correct_linguistic_analysis (13.060), Gap=2.830
- Guided: Best=TRANSLATION_ATTEMPT (16.730), Worst=REASONING (13.620), Gap=3.110

</details>

---

### 3.22 Xhosa → English

**Examples**: 64 | **Avg Difficulty**: Generic=2.89, Guided=3.23

**Linguistic Phenomena Frequency**:

| Phenomenon | Generic | Guided |
|------------|---------|--------|
| ambiguity | 0.0% | 3.1% |
| complex_syntax | 63.5% | 84.4% |
| figurative_language | 0.0% | 3.1% |
| idiom | 1.6% | 3.1% |
| long_distance_dependency | 93.7% | 100.0% |
| named_entities | 73.0% | 78.1% |

**Trace Type Distribution**:

| Trace Type | Generic Count | Generic % | Guided Count | Guided % | Δ Count | Δ % |
|------------|---------------|-----------|--------------|----------|---------|-----|
| CORRECT_LINGUISTIC_ANALYSIS | 16 | 25.4% | 4 | 6.2% | -12 | -19.2pp |
| NONE | 12 | 19.0% | 5 | 7.8% | -7 | -11.2pp |
| REPETITION | 1 | 1.6% | 0 | 0.0% | -1 | -1.6pp |
| TRANSLATION_ATTEMPT | 29 | 46.0% | 52 | 81.2% | +23 | +35.2pp |
| neutral | 5 | 7.9% | 3 | 4.7% | -2 | -3.2pp |

**Trace Usefulness Distribution**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| 1 | 0.0% | 1.6% | +1.6pp |
| 2 | 0.0% | 1.6% | +1.6pp |
| High | 1.6% | 1.6% | 0.0pp |
| Medium | 3.2% | 14.1% | +10.9pp |
| high | 20.6% | 4.7% | -15.9pp |
| medium | 49.2% | 73.4% | +24.2pp |
| neutral | 25.4% | 3.1% | -22.3pp |

**Translation Quality by Metric**:

<details>
<summary><b>BLEU</b> (click to expand)</summary>

**Overall Average**: Generic=6.534, Guided=6.232 (Δ -0.302)

**By Trace Type**:

| Trace Type | Generic | Guided | Δ |
|------------|---------|--------|---|
| CORRECT_LINGUISTIC_ANALYSIS | 5.040 | 11.230 | +6.190 |
| NONE | 7.390 | 5.030 | -2.360 |
| REPETITION | 10.860 | 0.000 | -10.860 |
| TRANSLATION_ATTEMPT | 5.800 | 5.580 | -0.220 |
| neutral | 3.580 | 3.090 | -0.490 |

**By Trace Usefulness**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| 1 | 0.000 | 0.980 | +0.980 |
| 2 | 0.000 | 3.530 | +3.530 |
| High | 9.700 | 0.820 | -8.880 |
| Medium | 1.570 | 9.050 | +7.480 |
| high | 5.650 | 11.600 | +5.950 |
| medium | 5.620 | 5.090 | -0.530 |
| neutral | 6.610 | 4.290 | -2.320 |

**Performance Range**:
- Generic: Best=REPETITION (10.860), Worst=neutral (3.580), Gap=7.280
- Guided: Best=CORRECT_LINGUISTIC_ANALYSIS (11.230), Worst=neutral (3.090), Gap=8.140

</details>

<details>
<summary><b>chrF++</b> (click to expand)</summary>

**Overall Average**: Generic=22.148, Guided=21.330 (Δ -0.818)

**By Trace Type**:

| Trace Type | Generic | Guided | Δ |
|------------|---------|--------|---|
| CORRECT_LINGUISTIC_ANALYSIS | 19.240 | 21.630 | +2.390 |
| NONE | 22.110 | 24.730 | +2.620 |
| REPETITION | 28.480 | 0.000 | -28.480 |
| TRANSLATION_ATTEMPT | 22.610 | 20.900 | -1.710 |
| neutral | 18.300 | 18.060 | -0.240 |

**By Trace Usefulness**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| 1 | 0.000 | 11.140 | +11.140 |
| 2 | 0.000 | 25.630 | +25.630 |
| High | 25.390 | 6.050 | -19.340 |
| Medium | 15.060 | 24.210 | +9.150 |
| high | 19.360 | 23.040 | +3.680 |
| medium | 22.830 | 20.950 | -1.880 |
| neutral | 20.860 | 18.490 | -2.370 |

**Performance Range**:
- Generic: Best=REPETITION (28.480), Worst=neutral (18.300), Gap=10.180
- Guided: Best=NONE (24.730), Worst=neutral (18.060), Gap=6.670

</details>

<details>
<summary><b>COMET</b> (click to expand)</summary>

**Overall Average**: Generic=0.490, Guided=0.480 (Δ -0.010)

**By Trace Type**:

| Trace Type | Generic | Guided | Δ |
|------------|---------|--------|---|
| CORRECT_LINGUISTIC_ANALYSIS | 0.490 | 0.480 | -0.010 |
| NONE | 0.540 | 0.450 | -0.090 |
| REPETITION | 0.450 | 0.000 | -0.450 |
| TRANSLATION_ATTEMPT | 0.510 | 0.490 | -0.020 |
| neutral | 0.460 | 0.500 | +0.040 |

**By Trace Usefulness**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| 1 | 0.000 | 0.370 | +0.370 |
| 2 | 0.000 | 0.460 | +0.460 |
| High | 0.540 | 0.410 | -0.130 |
| Medium | 0.390 | 0.480 | +0.090 |
| high | 0.490 | 0.460 | -0.030 |
| medium | 0.510 | 0.500 | -0.010 |
| neutral | 0.520 | 0.480 | -0.040 |

**Performance Range**:
- Generic: Best=NONE (0.540), Worst=REPETITION (0.450), Gap=0.090
- Guided: Best=neutral (0.500), Worst=NONE (0.450), Gap=0.050

</details>

<details>
<summary><b>MetricX-24</b> (click to expand)</summary>

**Overall Average**: Generic=15.218, Guided=15.928 (Δ +0.710)

**By Trace Type**:

| Trace Type | Generic | Guided | Δ |
|------------|---------|--------|---|
| CORRECT_LINGUISTIC_ANALYSIS | 15.460 | 16.250 | +0.790 |
| NONE | 13.840 | 16.500 | +2.660 |
| REPETITION | 16.250 | 0.000 | -16.250 |
| TRANSLATION_ATTEMPT | 15.040 | 15.520 | +0.480 |
| neutral | 15.500 | 15.440 | -0.060 |

**By Trace Usefulness**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| 1 | 0.000 | 17.500 | +17.500 |
| 2 | 0.000 | 16.380 | +16.380 |
| High | 14.940 | 17.000 | +2.060 |
| Medium | 16.880 | 16.060 | -0.820 |
| high | 15.770 | 16.100 | +0.330 |
| medium | 14.970 | 15.430 | +0.460 |
| neutral | 14.120 | 15.880 | +1.760 |

**Performance Range**:
- Generic: Best=REPETITION (16.250), Worst=NONE (13.840), Gap=2.410
- Guided: Best=NONE (16.500), Worst=neutral (15.440), Gap=1.060

</details>

---

### 3.23 Xhosa → Kazakh

**Examples**: 64 | **Avg Difficulty**: Generic=3.05, Guided=3.12

**Linguistic Phenomena Frequency**:

| Phenomenon | Generic | Guided |
|------------|---------|--------|
| ambiguity | 0.0% | 4.0% |
| complex_syntax | 78.9% | 92.0% |
| figurative_language | 0.0% | 4.0% |
| idiom | 0.0% | 4.0% |
| long_distance_dependency | 96.5% | 100.0% |
| named_entities | 61.4% | 62.0% |

**Trace Type Distribution**:

| Trace Type | Generic Count | Generic % | Guided Count | Guided % | Δ Count | Δ % |
|------------|---------------|-----------|--------------|----------|---------|-----|
| CORRECT_LINGUISTIC_ANALYSIS | 22 | 38.6% | 3 | 6.0% | -19 | -32.6pp |
| NONE | 5 | 8.8% | 4 | 8.0% | -1 | -0.8pp |
| TRANSLATION_ATTEMPT | 25 | 43.9% | 42 | 84.0% | +17 | +40.1pp |
| correct_linguistic_analysis | 2 | 3.5% | 1 | 2.0% | -1 | -1.5pp |
| neutral | 3 | 5.3% | 0 | 0.0% | -3 | -5.3pp |

**Trace Usefulness Distribution**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| 3 | 0.0% | 2.0% | +2.0pp |
| Medium | 3.5% | 12.0% | +8.5pp |
| high | 8.8% | 2.0% | -6.8pp |
| medium | 73.7% | 80.0% | +6.3pp |
| neutral | 14.0% | 4.0% | -10.0pp |

**Translation Quality by Metric**:

<details>
<summary><b>BLEU</b> (click to expand)</summary>

**Overall Average**: Generic=2.116, Guided=2.470 (Δ +0.354)

**By Trace Type**:

| Trace Type | Generic | Guided | Δ |
|------------|---------|--------|---|
| CORRECT_LINGUISTIC_ANALYSIS | 2.220 | 2.670 | +0.450 |
| NONE | 4.890 | 3.010 | -1.880 |
| TRANSLATION_ATTEMPT | 1.550 | 2.610 | +1.060 |
| correct_linguistic_analysis | 0.710 | 1.590 | +0.880 |
| neutral | 1.210 | 0.000 | -1.210 |

**By Trace Usefulness**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| 3 | 0.000 | 1.360 | +1.360 |
| Medium | 1.120 | 1.350 | +0.230 |
| high | 1.550 | 6.050 | +4.500 |
| medium | 1.890 | 2.760 | +0.870 |
| neutral | 3.510 | 2.600 | -0.910 |

**Performance Range**:
- Generic: Best=NONE (4.890), Worst=correct_linguistic_analysis (0.710), Gap=4.180
- Guided: Best=NONE (3.010), Worst=correct_linguistic_analysis (1.590), Gap=1.420

</details>

<details>
<summary><b>chrF++</b> (click to expand)</summary>

**Overall Average**: Generic=8.210, Guided=8.365 (Δ +0.155)

**By Trace Type**:

| Trace Type | Generic | Guided | Δ |
|------------|---------|--------|---|
| CORRECT_LINGUISTIC_ANALYSIS | 9.340 | 7.640 | -1.700 |
| NONE | 7.850 | 8.220 | +0.370 |
| TRANSLATION_ATTEMPT | 9.060 | 9.450 | +0.390 |
| correct_linguistic_analysis | 5.950 | 8.150 | +2.200 |
| neutral | 8.850 | 0.000 | -8.850 |

**By Trace Usefulness**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| 3 | 0.000 | 9.670 | +9.670 |
| Medium | 4.660 | 5.960 | +1.300 |
| high | 9.700 | 12.870 | +3.170 |
| medium | 9.160 | 9.660 | +0.500 |
| neutral | 8.400 | 8.130 | -0.270 |

**Performance Range**:
- Generic: Best=CORRECT_LINGUISTIC_ANALYSIS (9.340), Worst=correct_linguistic_analysis (5.950), Gap=3.390
- Guided: Best=TRANSLATION_ATTEMPT (9.450), Worst=CORRECT_LINGUISTIC_ANALYSIS (7.640), Gap=1.810

</details>

<details>
<summary><b>COMET</b> (click to expand)</summary>

**Overall Average**: Generic=0.440, Guided=0.395 (Δ -0.045)

**By Trace Type**:

| Trace Type | Generic | Guided | Δ |
|------------|---------|--------|---|
| CORRECT_LINGUISTIC_ANALYSIS | 0.410 | 0.380 | -0.030 |
| NONE | 0.500 | 0.430 | -0.070 |
| TRANSLATION_ATTEMPT | 0.390 | 0.360 | -0.030 |
| correct_linguistic_analysis | 0.480 | 0.410 | -0.070 |
| neutral | 0.420 | 0.000 | -0.420 |

**By Trace Usefulness**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| 3 | 0.000 | 0.460 | +0.460 |
| Medium | 0.420 | 0.320 | -0.100 |
| high | 0.430 | 0.430 | 0.000 |
| medium | 0.400 | 0.370 | -0.030 |
| neutral | 0.460 | 0.480 | +0.020 |

**Performance Range**:
- Generic: Best=NONE (0.500), Worst=TRANSLATION_ATTEMPT (0.390), Gap=0.110
- Guided: Best=NONE (0.430), Worst=TRANSLATION_ATTEMPT (0.360), Gap=0.070

</details>

<details>
<summary><b>MetricX-24</b> (click to expand)</summary>

**Overall Average**: Generic=16.740, Guided=16.017 (Δ -0.723)

**By Trace Type**:

| Trace Type | Generic | Guided | Δ |
|------------|---------|--------|---|
| CORRECT_LINGUISTIC_ANALYSIS | 16.160 | 16.100 | -0.060 |
| NONE | 16.440 | 15.200 | -1.240 |
| TRANSLATION_ATTEMPT | 16.330 | 16.830 | +0.500 |
| correct_linguistic_analysis | 18.560 | 15.940 | -2.620 |
| neutral | 16.210 | 0.000 | -16.210 |

**By Trace Usefulness**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| 3 | 0.000 | 16.620 | +16.620 |
| Medium | 16.440 | 16.360 | -0.080 |
| high | 17.680 | 18.880 | +1.200 |
| medium | 16.090 | 16.670 | +0.580 |
| neutral | 16.840 | 15.690 | -1.150 |

**Performance Range**:
- Generic: Best=correct_linguistic_analysis (18.560), Worst=CORRECT_LINGUISTIC_ANALYSIS (16.160), Gap=2.400
- Guided: Best=TRANSLATION_ATTEMPT (16.830), Worst=NONE (15.200), Gap=1.630

</details>

---

### 3.24 Xhosa → Lithuanian

**Examples**: 64 | **Avg Difficulty**: Generic=3.31, Guided=3.24

**Linguistic Phenomena Frequency**:

| Phenomenon | Generic | Guided |
|------------|---------|--------|
| ambiguity | 5.5% | 5.6% |
| complex_syntax | 80.0% | 92.6% |
| figurative_language | 7.3% | 3.7% |
| idiom | 5.5% | 3.7% |
| long_distance_dependency | 94.5% | 100.0% |
| named_entities | 76.4% | 75.9% |

**Trace Type Distribution**:

| Trace Type | Generic Count | Generic % | Guided Count | Guided % | Δ Count | Δ % |
|------------|---------------|-----------|--------------|----------|---------|-----|
| CORRECT_LINGUISTIC_ANALYSIS | 30 | 54.5% | 13 | 24.1% | -17 | -30.4pp |
| NONE | 3 | 5.5% | 1 | 1.9% | -2 | -3.6pp |
| RE 촉각 | 0 | 0.0% | 1 | 1.9% | +1 | +1.9pp |
| REPETITION | 1 | 1.8% | 1 | 1.9% | 0 | +0.1pp |
| TRANSLATION_ATTEMPT | 18 | 32.7% | 37 | 68.5% | +19 | +35.8pp |
| correct_linguistic_analysis | 2 | 3.6% | 1 | 1.9% | -1 | -1.7pp |
| neutral | 1 | 1.8% | 0 | 0.0% | -1 | -1.8pp |

**Trace Usefulness Distribution**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| 3 | 1.8% | 1.9% | +0.1pp |
| High | 1.8% | 3.7% | +1.9pp |
| Medium | 14.5% | 16.7% | +2.2pp |
| high | 20.0% | 11.1% | -8.9pp |
| medium | 56.4% | 63.0% | +6.6pp |
| neutral | 5.5% | 3.7% | -1.8pp |

**Translation Quality by Metric**:

<details>
<summary><b>BLEU</b> (click to expand)</summary>

**Overall Average**: Generic=2.522, Guided=1.532 (Δ -0.990)

**By Trace Type**:

| Trace Type | Generic | Guided | Δ |
|------------|---------|--------|---|
| CORRECT_LINGUISTIC_ANALYSIS | 2.440 | 1.750 | -0.690 |
| NONE | 6.980 | 1.000 | -5.980 |
| RE 촉각 | 0.000 | 0.790 | +0.790 |
| REPETITION | 1.330 | 1.510 | +0.180 |
| TRANSLATION_ATTEMPT | 1.040 | 2.530 | +1.490 |
| correct_linguistic_analysis | 0.690 | 1.610 | +0.920 |
| neutral | 2.650 | 0.000 | -2.650 |

**By Trace Usefulness**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| 3 | 1.150 | 0.330 | -0.820 |
| High | 0.000 | 2.310 | +2.310 |
| Medium | 1.480 | 1.710 | +0.230 |
| high | 2.240 | 1.490 | -0.750 |
| medium | 1.860 | 2.600 | +0.740 |
| neutral | 7.640 | 1.860 | -5.780 |

**Performance Range**:
- Generic: Best=NONE (6.980), Worst=correct_linguistic_analysis (0.690), Gap=6.290
- Guided: Best=TRANSLATION_ATTEMPT (2.530), Worst=RE 촉각 (0.790), Gap=1.740

</details>

<details>
<summary><b>chrF++</b> (click to expand)</summary>

**Overall Average**: Generic=13.660, Guided=11.242 (Δ -2.418)

**By Trace Type**:

| Trace Type | Generic | Guided | Δ |
|------------|---------|--------|---|
| CORRECT_LINGUISTIC_ANALYSIS | 12.810 | 12.280 | -0.530 |
| NONE | 18.130 | 18.460 | +0.330 |
| RE 촉각 | 0.000 | 7.380 | +7.380 |
| REPETITION | 16.250 | 10.530 | -5.720 |
| TRANSLATION_ATTEMPT | 11.760 | 12.030 | +0.270 |
| correct_linguistic_analysis | 12.440 | 6.770 | -5.670 |
| neutral | 10.570 | 0.000 | -10.570 |

**By Trace Usefulness**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| 3 | 12.530 | 6.780 | -5.750 |
| High | 7.580 | 11.940 | +4.360 |
| Medium | 12.210 | 11.010 | -1.200 |
| high | 13.080 | 8.990 | -4.090 |
| medium | 12.500 | 12.540 | +0.040 |
| neutral | 17.530 | 18.840 | +1.310 |

**Performance Range**:
- Generic: Best=NONE (18.130), Worst=neutral (10.570), Gap=7.560
- Guided: Best=NONE (18.460), Worst=correct_linguistic_analysis (6.770), Gap=11.690

</details>

<details>
<summary><b>COMET</b> (click to expand)</summary>

**Overall Average**: Generic=0.348, Guided=0.342 (Δ -0.007)

**By Trace Type**:

| Trace Type | Generic | Guided | Δ |
|------------|---------|--------|---|
| CORRECT_LINGUISTIC_ANALYSIS | 0.340 | 0.340 | 0.000 |
| NONE | 0.400 | 0.320 | -0.080 |
| RE 촉각 | 0.000 | 0.330 | +0.330 |
| REPETITION | 0.340 | 0.410 | +0.070 |
| TRANSLATION_ATTEMPT | 0.320 | 0.340 | +0.020 |
| correct_linguistic_analysis | 0.320 | 0.310 | -0.010 |
| neutral | 0.370 | 0.000 | -0.370 |

**By Trace Usefulness**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| 3 | 0.360 | 0.320 | -0.040 |
| High | 0.240 | 0.300 | +0.060 |
| Medium | 0.330 | 0.340 | +0.010 |
| high | 0.330 | 0.330 | 0.000 |
| medium | 0.330 | 0.340 | +0.010 |
| neutral | 0.430 | 0.330 | -0.100 |

**Performance Range**:
- Generic: Best=NONE (0.400), Worst=correct_linguistic_analysis (0.320), Gap=0.080
- Guided: Best=REPETITION (0.410), Worst=correct_linguistic_analysis (0.310), Gap=0.100

</details>

<details>
<summary><b>MetricX-24</b> (click to expand)</summary>

**Overall Average**: Generic=17.462, Guided=17.538 (Δ +0.077)

**By Trace Type**:

| Trace Type | Generic | Guided | Δ |
|------------|---------|--------|---|
| CORRECT_LINGUISTIC_ANALYSIS | 17.200 | 17.620 | +0.420 |
| NONE | 16.330 | 15.380 | -0.950 |
| RE 촉각 | 0.000 | 17.380 | +17.380 |
| REPETITION | 17.250 | 19.000 | +1.750 |
| TRANSLATION_ATTEMPT | 17.370 | 17.600 | +0.230 |
| correct_linguistic_analysis | 18.000 | 18.250 | +0.250 |
| neutral | 18.620 | 0.000 | -18.620 |

**By Trace Usefulness**:

| Usefulness | Generic | Guided | Δ |
|------------|---------|--------|---|
| 3 | 17.620 | 17.500 | -0.120 |
| High | 15.120 | 18.060 | +2.940 |
| Medium | 17.480 | 18.150 | +0.670 |
| high | 17.910 | 18.000 | +0.090 |
| medium | 17.050 | 17.480 | +0.430 |
| neutral | 17.120 | 15.530 | -1.590 |

**Performance Range**:
- Generic: Best=neutral (18.620), Worst=NONE (16.330), Gap=2.290
- Guided: Best=REPETITION (19.000), Worst=NONE (15.380), Gap=3.620

</details>

---

## 4. CoT Paradox Analysis

**The CoT Paradox**: Instances where empty traces (NONE/neutral) perform better than linguistic analysis traces.

### BLEU Paradox Cases

**Found 40 instances where empty traces outperform linguistic analysis**

| Language Pair | CoT Variant | Empty Score | Linguistic Score | Gap |
|---------------|-------------|-------------|------------------|-----|
| English→French | Generic | 36.070 | 7.770 | 28.300 |
| English→Lithuanian | Guided | 19.600 | 4.290 | 15.310 |
| Turkish→English | Guided | 24.730 | 11.280 | 13.450 |
| Finnish→Turkish | Guided | 16.900 | 4.570 | 12.330 |
| English→French | Guided | 42.500 | 32.340 | 10.160 |
| English→Finnish | Generic | 16.240 | 6.450 | 9.790 |
| German→French | Guided | 35.930 | 26.500 | 9.430 |
| English→Turkish | Guided | 22.180 | 13.010 | 9.170 |
| Lithuanian→English | Generic | 20.290 | 12.210 | 8.080 |
| Turkish→Finnish | Guided | 13.540 | 5.500 | 8.040 |

### chrF++ Paradox Cases

**Found 31 instances where empty traces outperform linguistic analysis**

| Language Pair | CoT Variant | Empty Score | Linguistic Score | Gap |
|---------------|-------------|-------------|------------------|-----|
| English→French | Generic | 56.040 | 30.100 | 25.940 |
| Kazakh→English | Guided | 34.060 | 19.640 | 14.420 |
| Finnish→Turkish | Guided | 34.060 | 22.040 | 12.020 |
| Turkish→English | Guided | 45.650 | 34.920 | 10.730 |
| English→Lithuanian | Guided | 34.410 | 24.710 | 9.700 |
| English→Finnish | Generic | 39.760 | 30.210 | 9.550 |
| English→Lithuanian | Generic | 31.090 | 22.210 | 8.880 |
| English→Turkish | Guided | 42.780 | 33.920 | 8.860 |
| Lithuanian→Turkish | Guided | 29.690 | 20.850 | 8.840 |
| Turkish→Finnish | Guided | 33.000 | 24.490 | 8.510 |

### COMET Paradox Cases

**Found 39 instances where empty traces outperform linguistic analysis**

| Language Pair | CoT Variant | Empty Score | Linguistic Score | Gap |
|---------------|-------------|-------------|------------------|-----|
| Finnish→Turkish | Guided | 0.760 | 0.550 | 0.210 |
| Lithuanian→Turkish | Guided | 0.740 | 0.550 | 0.190 |
| English→Finnish | Generic | 0.820 | 0.660 | 0.160 |
| Turkish→English | Guided | 0.870 | 0.730 | 0.140 |
| Turkish→Lithuanian | Generic | 0.620 | 0.480 | 0.140 |
| English→French | Generic | 0.850 | 0.720 | 0.130 |
| Turkish→Lithuanian | Guided | 0.600 | 0.480 | 0.120 |
| Turkish→Finnish | Guided | 0.720 | 0.610 | 0.110 |
| Kazakh→Xhosa | Generic | 0.430 | 0.330 | 0.100 |
| Turkish→Finnish | Generic | 0.660 | 0.570 | 0.090 |

### MetricX-24 Paradox Cases

**Found 26 instances where empty traces outperform linguistic analysis**

| Language Pair | CoT Variant | Empty Score | Linguistic Score | Gap |
|---------------|-------------|-------------|------------------|-----|
| English→Xhosa | Guided | 12.230 | 8.160 | 4.070 |
| German→French | Generic | 6.170 | 2.680 | 3.490 |
| French→German | Generic | 5.000 | 1.570 | 3.430 |
| English→Finnish | Guided | 12.490 | 9.180 | 3.310 |
| Kazakh→Xhosa | Guided | 15.860 | 13.120 | 2.740 |
| English→German | Guided | 4.360 | 1.850 | 2.510 |
| Finnish→English | Guided | 9.360 | 6.980 | 2.380 |
| French→English | Guided | 4.400 | 2.230 | 2.170 |
| Xhosa→Lithuanian | Generic | 18.620 | 17.200 | 1.420 |
| German→French | Guided | 5.180 | 3.790 | 1.390 |

## 5. Linguistic Expert Interpretation Guide

### 5.1 Experimental Setup

**Evaluation Framework**:
- **24 language pairs** covering diverse typological characteristics
- **64 examples per language pair** (1,536 per CoT variant, 3,072 total)
- **Model**: google/gemma-3-1b-it (1B parameter LLM)
- **Two CoT variants**:
  - **Generic CoT**: Standard "think step by step" prompting
  - **Guided CoT**: Linguistic phenomenon-specific prompting with structured analysis

**Evaluation Metrics**:
- **BLEU** (with effective_order=True): N-gram overlap, sentence-level
- **chrF++**: Character n-gram F-score
- **COMET**: Neural learned metric (wmt22-comet-da)
- **MetricX-24**: Google's MT5-based learned metric

**Phase 2 Annotation Categories**:
- **Trace Types**: NONE, TRANSLATION_ATTEMPT, CORRECT_LINGUISTIC_ANALYSIS, HALLUCINATED_RULE, etc.
- **Usefulness**: high, medium, neutral (how helpful the reasoning trace was)
- **Difficulty**: 1-5 scale (translation complexity)
- **Linguistic Phenomena**: named_entities, complex_syntax, long_distance_dependency

### 5.2 Key Questions for Analysis

1. **Does guided prompting increase reasoning quality?**
   - Compare CORRECT_LINGUISTIC_ANALYSIS rates between variants
   - Examine trace usefulness distributions

2. **Does the CoT Paradox persist across metrics?**
   - Check if empty traces (NONE/neutral) outperform linguistic analysis
   - Identify language pairs where the paradox is strongest

3. **Are there language-specific patterns?**
   - Compare morphologically rich vs. isolating languages
   - Examine directions (e.g., English→X vs. X→English)

4. **What linguistic phenomena benefit most from guided CoT?**
   - Cross-reference phenomena frequencies with quality improvements
   - Identify where explicit linguistic prompting helps vs. hurts

### 5.3 Statistical Notes

- **Sample size**: 64 examples per language pair provides moderate statistical power
- **Percentage point (pp) differences**: Direct subtraction of percentages (e.g., 45% - 30% = 15pp)
- **Metric score ranges**: BLEU (0-100), chrF++ (0-100), COMET (-inf to 1.0), MetricX-24 (0-25)
- **Suggested significance threshold**: >5pp difference or >10% relative change

---

*Analysis generated from COMPREHENSIVE_ANALYSIS.md files in both evaluation directories*
*Total pairs analyzed: 24/24*
*Total examples: 3072 (1536 Generic + 1536 Guided)*
