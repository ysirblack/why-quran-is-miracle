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

| Calendar Type  | Target   | Result         |
| -------------- | -------- | -------------- |
| **Solar Year** | 365 days | **365 tokens** |
| **Hijri Year** | 354 days | **354 tokens** |

## Significance

This pattern demonstrates:

1. **Dual Calendar Alignment**: Same root yields both solar and lunar calendar constants
2. **Morphological Precision**: Different grammatical forms naturally separate into calendar-relevant counts
3. **Statistical Rarity**: A probability helper explores how unlikely these counts are
   under simple random subset models
4. **Complementary Design**: Solar and lunar calendars both embedded in the same linguistic system

## Detailed Analysis

- [**Solar Year (365)**](solar_365/) - Analysis of forms yielding 365 total
- [**Hijri Year (354)**](hijri_354/) - Analysis of forms yielding 354 total

## Probability Exploration

An optional probability helper (`combined_probability_analysis.py`) estimates how unlikely
the key counts would be under simple random subset models:

- Solar 365-day composition (Rule Set P)
- Hijri 354-day composition (component rule set)
- Lunar month 29 (plural + dual forms)
- Calendar months 12 (singular `شهر`)

All figures depend entirely on the chosen null model, so the script prints both the
assumptions and the resulting probabilities for transparency.

## Methodology Notes

- Uses transparent morphological criteria based on QAC forms
- Applies consistent Rule-Set methodology
- Accounts for all variations in spelling and case
- Verifies counts across multiple sources

---

_This represents a unique example of dual calendar constants emerging from natural linguistic analysis of a single Quranic root._
