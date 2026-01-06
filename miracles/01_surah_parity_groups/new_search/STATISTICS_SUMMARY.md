# Statistical Summary of 18 Patterns

**Analysis Date:** January 2025

---

## Overview

This document summarizes statistical testing of 18 numerical patterns found in the Quran's structure, based on "Simetrik Kitap: Kur'an" by Abdulaziz Bayindir and Haluk Nurbaki.

**Methodology:**

- 100,000 trials per pattern
- Permutation tests for arrangement-dependent patterns
- Bootstrap tests for property-dependent patterns
- Bonferroni correction for multiple testing: α = 0.05/18 = 0.00278

---

## Tier Classification

### Tier 1: Statistically Robust (2 patterns)

| #      | Pattern                | p-value   | Method      | Notes                                      |
| ------ | ---------------------- | --------- | ----------- | ------------------------------------------ |
| **12** | Long/Short 57/57 Split | < 0.00001 | Bootstrap   | Median boundary (39), no surah at boundary |
| **16** | Golden Ratio           | < 0.00001 | Permutation | Deviation only 0.00039 from φ              |

### Tier 2: Significant But Methodologically Questionable (1 pattern)

| #   | Pattern     | p-value | Method      | Issues                                      |
| --- | ----------- | ------- | ----------- | ------------------------------------------- |
| 15  | 6236 Center | 0.00029 | Monte Carlo | Post-hoc property definition, numerological |

### Tier 3: Not Significant (15 patterns)

| #   | Pattern                    | p-value | Method      |
| --- | -------------------------- | ------- | ----------- |
| 01  | Homogeneous Half Symmetry  | 0.148   | Permutation |
| 02  | Verses < Position Symmetry | 0.085   | Permutation |
| 03  | Prime Numbers              | 0.078   | Permutation |
| 04  | Set Operations             | 0.081   | Bootstrap   |
| 05  | Divisible by 2 not 3       | 0.156   | Permutation |
| 06  | Divisible by 3 not 2       | 0.194   | Permutation |
| 07  | Prime Factor Sum           | 0.062   | Bootstrap   |
| 08  | Perfect Numbers            | 0.382   | Permutation |
| 09  | Abundant Numbers           | 0.172   | Permutation |
| 10  | Deficient Numbers          | 0.165   | Permutation |
| 11  | Arithmetic Mean            | 0.112   | Bootstrap   |
| 13  | Mean vs Long/Short         | 0.212   | Permutation |
| 14  | Divisor Count = 2          | 0.163   | Permutation |
| 17  | Two Prime Divisors         | 0.143   | Permutation |
| 18  | Three Prime Divisors       | 0.149   | Permutation |

---

## Method Explanation

### Permutation Test

- Shuffles the actual Quran verse counts among surah positions
- Measures: "Given this exact data, how unusual is the observed arrangement?"
- Used when the pattern depends on which verse count is assigned to which position

### Bootstrap Test

- Generates random verse count distributions (uniform 3-286)
- Measures: "How unusual is this data compared to random data?"
- Used when the pattern depends on aggregate properties (e.g., count of odd values)

### Monte Carlo Simulation

- Generates random values in a specified range
- Measures: "What's the probability of hitting a specific value?"

---

## Key Findings

### 1. Golden Ratio (Pattern 16) - Most Robust

The ratio of repeated-sum verse totals to unique-sum verse totals:

- **7906 / 4885 = 1.618424**
- **Golden Ratio φ = 1.618034**
- **Deviation: 0.00039**

This is the strongest finding. The permutation test correctly shuffles actual data.

### 2. 57/57 Split at Median (Pattern 12) - Robust

- 57 surahs have > 39 verses (long)
- 57 surahs have < 39 verses (short)
- **No surah has exactly 39 verses** (the median)
- Perfect 57/57 split at a natural mathematical boundary

This is robust because:

1. The boundary 39 is the median (not post-hoc selected)
2. The absence of 39-verse surahs is a structural property

### 3. Patterns 01-11, 13-14, 17-18 - Not Significant

These patterns, while visually striking, occur with reasonable frequency (6-38%) in random arrangements. This doesn't make them meaningless - it simply means we cannot statistically distinguish them from chance.

---

## Conclusion

**Out of 18 patterns:**

- **2 robust:** Golden Ratio and 57/57 split pass rigorous statistical testing
- **1 questionable:** 6236 center (numerological interpretation)
- **15 not significant:** Interesting as observations, not statistically distinguishable from chance

This is intellectually honest. Not everything needs to be statistically miraculous. The Golden Ratio and 57/57 split findings alone are genuinely remarkable.
