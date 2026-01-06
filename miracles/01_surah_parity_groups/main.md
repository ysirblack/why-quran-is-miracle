# Surah Parity Groups

## Summary

Analysis of numerical patterns in the Quran's 114-chapter structure.

---

## NEW: Simetrik Kitap Analysis (January 2025)

18 patterns from "Simetrik Kitap: Kur'an" by Abdulaziz Bayindir and Haluk Nurbaki.

### Tier 1: Statistically Robust (p < 0.00001)

| #      | Pattern                             | p-value   | Method      |
| ------ | ----------------------------------- | --------- | ----------- |
| **12** | 57/57 Long/Short Split at Median 39 | < 0.00001 | Bootstrap   |
| **16** | Golden Ratio (7906/4885 = 1.618424) | < 0.00001 | Permutation |

### Tier 2: Significant but Methodologically Questionable

| #   | Pattern                                                   | p-value | Method      | Note          |
| --- | --------------------------------------------------------- | ------- | ----------- | ------------- |
| 15  | 6236 Center (total verses at center of 6236-like numbers) | 0.00029 | Monte Carlo | Numerological |

### Tier 3: Observed Patterns (p > 0.05)

| #   | Pattern                                  | p-value | Method      |
| --- | ---------------------------------------- | ------- | ----------- |
| 01  | Homogeneous Half Symmetry (28/29/29/28)  | 0.148   | Permutation |
| 02  | Verses < Position Symmetry (34/32/32/34) | 0.085   | Permutation |
| 03  | Prime Numbers (67/47, meta-patterns)     | 0.078   | Permutation |
| 04  | Set Operations (32/32, 25/25, 101/13)    | 0.081   | Bootstrap   |
| 05  | Divisible by 2 not 3 (33/33/24/24)       | 0.156   | Permutation |
| 06  | Divisible by 3 not 2 (42/42/15/15)       | 0.194   | Permutation |
| 07  | Prime Factor Sum (71/71, 43/43)          | 0.062   | Bootstrap   |
| 08  | Perfect Numbers (2/2, 55/55, 54/54)      | 0.382   | Permutation |
| 09  | Abundant Numbers (14/14, 43/43, 71/43)   | 0.172   | Permutation |
| 10  | Deficient Numbers (41/41, 16/16, 71/43)  | 0.165   | Permutation |
| 11  | Arithmetic Mean (41/73, 48/48, 9/9)      | 0.112   | Bootstrap   |
| 13  | Mean vs Long/Short (identical results)   | 0.212   | Permutation |
| 14  | Divisor Count = 2 (33/33/24/24)          | 0.163   | Permutation |
| 17  | Two Prime Divisors (24/24/33/33)         | 0.143   | Permutation |
| 18  | Three Prime Divisors (25/25/32/32)       | 0.149   | Permutation |

See [`new_search/`](new_search/) for individual pattern details and [`new_search/STATISTICS_SUMMARY.md`](new_search/STATISTICS_SUMMARY.md) for methodology.

---

## Original Analysis

**3 patterns pass p < 0.05**:

1. Even-Sum = 6,236 (0.12%)
2. Six-Block Symphony (0.0034%)
3. Verse-Number Mirror (0.23%)

**2 patterns do not pass p < 0.05** (documented as observations):

1. Core 2×2 Grid (14.9%)
2. Long/Short Swap (12.7%)

## Key Results

| Group     | Count |
| --------- | ----- |
| odd-odd   | 27    |
| even-even | 30    |
| odd-even  | 27    |
| even-odd  | 30    |

- 57 surahs have odd verse counts
- 57 surahs have even verse counts
- The 57/57 split is arithmetically guaranteed, not a random outcome

## Sub-Analyses

- [Core 2×2 Parity Grouping](core_2x2_parity_grouping/) - Observation (p = 14.9%)
- [Even Sum Surahs](even_sum_surahs/) - Significant (p = 0.12%)
- [Long/Short Parity](long_short_parity/) - Observation (p = 12.7%)
- [Six-Block Symphony](new_data_slices/) - Significant (p = 0.0034%)
- [Verse-Number Mirror](verse_greater_than_number/) - Significant (p = 0.23%)

## Methodology

- Data: Tanzil Ḥafṣ/Uthmānī text
- Basmalah counted only in Al-Fatiha
- Statistical method: Permutation testing (1,000,000 trials)
- Significance threshold: p < 0.05
