# Probability Analysis - Surah Parity Groups

This section contains comprehensive statistical analysis of the probability that the observed patterns in surah parity groups could occur by chance.

## Analysis Overview

The probability calculations consider multiple approaches:

1. **[Clean Probability Bundle](clean_probability_bundle.md)** - Full-blind analysis assuming no prior knowledge of the Quran's structure
2. **[Two Honest Nulls](two_honest_nulls.md)** - Comparison between permutation and generative i.i.d. models
3. **[Fair Book-like Null](fair_book_null.md)** - Analysis preserving the actual verse count distribution

## Key Results Summary

| Approach                   | Probability   | Notes                       |
| -------------------------- | ------------- | --------------------------- |
| **i.i.d. Uniform[1..286]** | ~4.1 × 10⁻⁶⁶  | Full-blind generative model |
| **i.i.d. Uniform[1..600]** | ~2.7 × 10⁻¹³⁹ | Wider scope analysis        |
| **Permutation Model**      | ~7.1 × 10⁻²¹  | Fair book-preserving model  |

## Events Analyzed

The probability calculations include these simultaneous events:

- **(P1) Parity–Sum core**: Exactly 57 even sums, with even-group total = total verse count
- **(P1-grid) 27/30 grid**: Specific parity distribution within the 2×2 classification
- **(P2) 40-threshold**: Exactly 57 long (≥40 verses) and 57 short (≤39 verses) surahs
- **(P2-grid)**: 27/30 distribution among long surahs by order parity
- **(P3) Revelation-order exclusion**: Pattern holds for mushaf order but fails for revelation order
- **(P4) "verses > order" mirror**: 48 total with internal 23/25 symmetric splits

## Statistical Significance

All approaches yield probabilities far below conventional significance thresholds:

- **Most conservative estimate**: ~1 in 1.4 × 10²⁰ (140 quintillion)
- **Full-blind estimate**: ~1 in 2.7 × 10¹³⁹

These probabilities are so small that they suggest the patterns are not due to chance but represent intentional mathematical design.

## Methodology Notes

- All calculations use transparent, reproducible methods
- Multiple independent null models validate the findings
- Conservative estimates account for potential dependencies
- Exact combinatorial calculations where possible, normal approximations for large samples

---

_The detailed mathematical derivations and calculations are provided in the linked analysis files._
