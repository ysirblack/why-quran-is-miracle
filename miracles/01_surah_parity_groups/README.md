# Surah Parity Groups: Numerical Pattern Analysis

This folder contains computational analysis of five numerical patterns discovered in the Quran's 114-chapter structure. All patterns are based on the canonical Tanzil Ḥafṣ/Uthmānī text and are computationally verified using rigorous statistical methods.

## The Five Numerical Patterns

### 1. Core 2×2 Parity Grouping (27/30/30/27)

**Pattern**: Chapters classified by order parity and verse-count parity reveal 27/30/30/27 distribution.

**Key Feature**: 57 odd chapters + 57 even chapters (guaranteed by sequential numbering 1-114).

**Probability**: ~1 in 6.7 (14.9%) - Based on 1,000,000 permutation trials

- Note: 57/57 split is guaranteed by the structure, not a random outcome

### 2. Even-Sum Chapters (6,236/6,555 Dual Accounting)

**Pattern**: Chapters where (chapter # + verse count) is even total exactly 6,236 (total Quran verses), while odd-sum chapters total 6,555 (sum of chapter numbers 1-114).

**Key Feature**: 57/57 split is guaranteed (arithmetic identity); the specific totals are the testable pattern.

**Probability**: ~1 in 833 (0.12%) - Based on 1,000,000 permutation trials

- Note: The 6,236 total matching total verses is the statistically interesting aspect

### 3. Long/Short Parity Swap (27/30 ↔ 30/27)

**Pattern**: 57 long chapters (≥40 verses) show 27 odd-order + 30 even-order, while 57 short chapters show 30 odd-order + 27 even-order.

**Key Feature**: No chapters have exactly 39 verses; threshold 40 is one of only 2 (of 284) that gives both 57/57 split and swap pattern.

**Probability**: ~1 in 7.9 (12.7%) for swap pattern - Based on 1,000,000 permutation trials

- Note: 57/57 split at threshold=40 is guaranteed by the actual data
- Threshold significance: ~1 in 142 (only 2 of 284 thresholds work)

### 4. Six-Block Symphony (19-Chapter Harmony)

**Pattern**: 114 chapters divided into 6 blocks of 19, analyzed through multiple classification systems (parity grids, homogeneity, prime classification) all produce specific alternating patterns.

**Key Feature**: 8 different pattern sequences must all match simultaneously across the 6 blocks.

**Probability**: ~1 in 29,412 (0.0034%) - Based on 1,000,000 permutation trials

- Note: This is the most statistically significant individual pattern
- 6 of the 8 patterns are interdependent (derived from same 2×2 parity grid)

### 5. Verse-Number Mirror (23/25 ↔ 25/23)

**Pattern**: 48 chapters where verses > chapter number, classified by two different methods (result parity vs order parity) both yield 23/25 distributions in mirror symmetry.

**Key Feature**: Two classification methods produce swapped counts.

**Probability**: ~1 in 439 (0.23%) - Based on 1,000,000 permutation trials

- Breakdown: Getting 48 filtered (~1 in 7.5), then swap pattern (~1 in 10.8), then exact 23/25 (~1 in 5.4)

## Pattern Summary

These five patterns exist in the Quran's 114-chapter structure and have been verified computationally. Individual probabilities range from common (~1 in 7) to rare (~1 in 29,412).

## Combined Probability Analysis

**Honest Assessment** (1,000,000 trials):

**Individual Pattern Probabilities:**

- Core 2×2 Grid: ~1 in 6.7 (14.9%)
- Even-Sum Total: ~1 in 833 (0.12%)
- Long/Short Swap: ~1 in 7.9 (12.7%)
- Six-Block Symphony: ~1 in 29,412 (0.0034%) ⭐ Most significant
- Verse-Number Mirror: ~1 in 439 (0.23%)

**Combined Result (all 5 patterns together):**

- **Observed**: < 1 in 1,000,000 (0 matches in 1,000,000 trials)
- **Theoretical** (if perfectly independent): ~1 in 595 billion

**Key Notes:**

- Corrected bugs from original calculator (149→114 surahs, fixed six-block logic)
- Removed guaranteed outcomes (57/57 splits) from probability calculations
- Only tested truly independent patterns
- Six-Block pattern is the bottleneck (rarest individual pattern)

See `COMBINED_ANALYSIS_SUMMARY.md` for detailed methodology and bug fixes.

## Pattern Structure

The five patterns analyze different aspects of the 114-chapter structure:

1. **Core 2×2 Grid**: Parity classification of chapters and verse counts
2. **Even-Sum**: Arithmetic properties of chapter numbers and verse counts
3. **Long/Short**: Magnitude-based classification (≥40 vs <40 verses)
4. **Six-Block**: Block-based patterns across 6 groups of 19 chapters
5. **Verse-Number Mirror**: Filtered subset (verses > number) classification

## Verification and Reproducibility

Each pattern includes:

- **Verification Script**: Python code to verify the pattern exists (`*_verification.py`)
- **Probability Analysis**: Honest statistical assessment (`honest_probability_analysis.py`)
- **Documentation**: Clear methodology in `README.md` and `main.md`
- **Data Source**: Tanzil Ḥafṣ/Uthmānī text (canonical Quran corpus)

All patterns are reproducible using the provided scripts and can be verified independently.

## Methodology and Key Findings

**Data Source:**

- Tanzil Ḥafṣ/Uthmānī text (canonical digital Quran corpus)
- Verse counts verified against standard references
- Basmalah counted only in Al-Fatiha (chapter 1)

**Statistical Method:**

- Permutation testing with 1,000,000 trials
- Preserves actual verse count distribution
- Randomly reassigns verse counts to chapter positions
- Tests what patterns would occur by chance

**Classification Rules:**

- Parity: Standard odd/even (chapter numbers 1-114)
- Length: ≥40 vs <40 verses threshold
- Prime: Standard mathematical definition (1 treated as prime per pattern convention)
- Even-Sum: Arithmetic sum of chapter number + verse count

**Key Findings:**

- All 5 patterns exist in the actual Quran structure
- Individual probabilities range from ~1 in 7 to ~1 in 29,412
- Combined probability: < 1 in 1,000,000 (observed) to ~1 in 595 billion (theoretical)
- Some claimed probabilities were inflated due to bugs (now corrected)
- Several "57/57 splits" are guaranteed by arithmetic, not random

**Files:**

- `AUDIT.md` - Complete audit methodology and log
- `COMBINED_ANALYSIS_SUMMARY.md` - Detailed combined analysis
- `honest_combined_probability_calculator.py` - Corrected probability calculator
- Individual pattern folders contain verification and analysis scripts

---

This research represents a computational analysis of numerical patterns in the Quran's structure, with honest probability assessments and transparent methodology.
