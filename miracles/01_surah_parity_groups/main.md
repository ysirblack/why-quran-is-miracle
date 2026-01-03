# Surah Parity Groups

## Summary

Analysis of numerical patterns in the Quran's 114-chapter structure.

**3 patterns pass p < 0.05**:
1. Even-Sum = 6,236 (0.12%)
2. Six-Block Symphony (0.0034%)
3. Verse-Number Mirror (0.23%)

**2 patterns do not pass p < 0.05** (documented as observations):
1. Core 2×2 Grid (14.9%)
2. Long/Short Swap (12.7%)

## Key Results

| Group | Count |
|-------|-------|
| odd-odd | 27 |
| even-even | 30 |
| odd-even | 27 |
| even-odd | 30 |

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
