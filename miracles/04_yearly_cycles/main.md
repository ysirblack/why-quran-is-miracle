# Yearly Cycles - Solar and Lunar Calendar Matches

## Overview

This analysis examines how different filtering approaches applied to the same root word **ي و م (yawm - day)** produce exact matches with both solar and lunar calendar constants. Using the same base set of 405 total occurrences of the root, two distinct morphological filters yield:

- **365 tokens** (Solar year)
- **354 tokens** (Hijri lunar year)

## Base Data

- **Root:** ي و م (yawm)
- **Total occurrences:** 405 tokens (as reported by Quranic Arabic Corpus)
- **Source:** Tanzil Ḥafṣ/Uthmānī
- **Method:** Morphological filtering based on specific grammatical forms

## Results Summary

| Calendar Type  | Target   | Result         | Probability       |
| -------------- | -------- | -------------- | ----------------- |
| **Solar Year** | 365 days | **365 tokens** | ~1 in 406 (0.25%) |
| **Hijri Year** | 354 days | **354 tokens** | ~1 in 406 (0.25%) |

## Significance

This pattern demonstrates:

1. **Dual Calendar Alignment**: Same root yields both solar and lunar calendar constants
2. **Morphological Precision**: Different grammatical forms naturally separate into calendar-relevant counts
3. **Statistical Rarity**: Both results have similar low probability (~0.25% each)
4. **Complementary Design**: Solar and lunar calendars both embedded in the same linguistic system

## Detailed Analysis

- [**Solar Year (365)**](solar_365/) - Analysis of forms yielding 365 total
- [**Hijri Year (354)**](hijri_354/) - Analysis of forms yielding 354 total

## Joint Probability

The probability of achieving both exact matches simultaneously from the same root, using reasonable morphological boundaries:

- Individual probabilities: ~0.25% each
- Joint probability (assuming independence): ~0.25% × 0.25% = **0.000625%** (≈ 1 in 160,000)

However, the internal compositional probabilities (specific breakdowns within each set) are much lower:

- Solar set composition: ~1.49 × 10⁻⁵ %
- Hijri set composition: ~1.49 × 10⁻⁷ %

## Methodology Notes

- Uses transparent morphological criteria based on QAC forms
- Applies consistent Rule-Set methodology
- Accounts for all variations in spelling and case
- Verifies counts across multiple sources

---

_This represents a unique example of dual calendar constants emerging from natural linguistic analysis of a single Quranic root._
