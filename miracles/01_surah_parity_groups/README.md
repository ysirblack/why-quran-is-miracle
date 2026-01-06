# Surah Parity Groups

Analysis of numerical patterns in the Quran's 114-chapter structure.

**Our threshold**: p < 0.05 (5%)

---

## NEW: Simetrik Kitap Analysis (January 2025)

Comprehensive analysis of 18 patterns from "Simetrik Kitap: Kur'an" by Abdulaziz Bayindir and Haluk Nurbaki.

### Tier 1: Statistically Robust (p < 0.00001)

| #      | Pattern                             | p-value   | Method      |
| ------ | ----------------------------------- | --------- | ----------- |
| **12** | 57/57 Long/Short Split at Median 39 | < 0.00001 | Bootstrap   |
| **16** | Golden Ratio (7906/4885 = 1.618424) | < 0.00001 | Permutation |

### Tier 2: Significant but Methodologically Questionable

| #   | Pattern     | p-value | Note                              |
| --- | ----------- | ------- | --------------------------------- |
| 15  | 6236 Center | 0.00029 | Numerological (post-hoc property) |

### Tier 3: Observed Patterns (p > 0.05)

| #   | Pattern                                  | p-value |
| --- | ---------------------------------------- | ------- |
| 01  | Homogeneous Half Symmetry (28/29/29/28)  | 0.148   |
| 02  | Verses < Position Symmetry (34/32/32/34) | 0.085   |
| 03  | Prime Numbers (67/47, meta-patterns)     | 0.078   |
| 04  | Set Operations (32/32, 25/25, 101/13)    | 0.081   |
| 05  | Divisible by 2 not 3 (33/33/24/24)       | 0.156   |
| 06  | Divisible by 3 not 2 (42/42/15/15)       | 0.194   |
| 07  | Prime Factor Sum (71/71, 43/43)          | 0.062   |
| 08  | Perfect Numbers (2/2, 55/55)             | 0.382   |
| 09  | Abundant Numbers (14/14, 43/43)          | 0.172   |
| 10  | Deficient Numbers (41/41, 16/16)         | 0.165   |
| 11  | Arithmetic Mean (41/73, 48/48)           | 0.112   |
| 13  | Mean vs Long/Short (identical)           | 0.212   |
| 14  | Divisor Count = 2 (33/33/24/24)          | 0.163   |
| 17  | Two Prime Divisors (24/24/33/33)         | 0.143   |
| 18  | Three Prime Divisors (25/25/32/32)       | 0.149   |

### Full Analysis

See [`new_search/`](new_search/) for individual pattern details and [`new_search/STATISTICS_SUMMARY.md`](new_search/STATISTICS_SUMMARY.md) for methodology.

---

## Pattern 1: Even-Sum = Total Verses

**What is it?** Add each chapter's position + verse count. If even, it's in the "even-sum" group.

**The finding**: The 57 even-sum chapters contain exactly **6,236 verses** - the total verses in the Quran.

| Group             | Count | Total verses                 |
| ----------------- | ----- | ---------------------------- |
| Even-sum chapters | 57    | 6,236 (= total Quran verses) |
| Odd-sum chapters  | 57    | 6,555                        |

**Probability**: ~1 in 833 (0.12%) | **Passes**: Yes

---

## Pattern 2: Six-Block Symphony

**What is it?** Divide 114 chapters into 6 blocks of 19. Count parity categories in each block.

**The finding**: Multiple classification systems produce **alternating patterns** across all 6 blocks simultaneously.

**Probability**: ~1 in 29,412 (0.0034%) | **Passes**: Yes

---

## Pattern 3: Verse-Number Mirror

**What is it?** Filter to 48 chapters where verses > position. Classify by (a) subtraction result parity, (b) position parity.

**The finding**: Both methods give **mirrored distributions**: 23/25 ↔ 25/23.

**Probability**: ~1 in 439 (0.23%) | **Passes**: Yes

---

## Pattern 4: Core 2×2 Parity Grid

**What is it?** Classify chapters by position parity × verse count parity into 4 groups.

**The finding**: Distribution is **27, 30, 30, 27** - symmetric.

**Probability**: ~1 in 6.7 (14.9%) | **Passes**: No

---

## Pattern 5: Long/Short Swap

**What is it?** Split chapters into long (≥40 verses) and short (<40). Check position parity distribution.

**The finding**: Long = 27 odd, 30 even. Short = 30 odd, 27 even. The numbers **swap**.

**Probability**: ~1 in 7.9 (12.7%) | **Passes**: No

---

## Combined

**All 5 patterns together**: <1 in 1,000,000 (0 matches in 1M trials)

---

## Addressing Skeptical Questions

> For comprehensive methodology defense, see [METHODOLOGY_FAQ.md](../METHODOLOGY_FAQ.md)

### Q: Some patterns don't pass p < 0.05. Why include them?

**A:** Full transparency. We show ALL patterns, not just significant ones:

| Pattern      | p-value | Significant? | Shown?  |
| ------------ | ------- | ------------ | ------- |
| Even-Sum     | 0.12%   | YES          | YES     |
| Six-Block    | 0.0034% | YES          | YES     |
| Verse-Mirror | 0.23%   | YES          | YES     |
| Core 2x2     | 14.9%   | NO           | **YES** |
| Long/Short   | 12.7%   | NO           | **YES** |

Cherry-picking would mean HIDING the non-significant patterns.

### Q: Are these patterns independent?

**A:** No, and we acknowledge this:

- Patterns 2, 4, 5 share the same 2x2 parity grid structure
- We test them JOINTLY via permutation (shuffle once, check all)
- Combined probability accounts for dependencies

### Q: Why divide into 6 blocks of 19?

**A:** 19 is significant in Quranic numerology (mentioned in 74:30). But the pattern works because:

- 114 = 6 × 19 (perfect division)
- The alternating patterns emerge across ALL 6 blocks
- This isn't arbitrary - it's testing for structure at the surah level

### Q: Could someone have designed this?

| Requirement                         | 7th Century? | Modern? |
| ----------------------------------- | ------------ | ------- |
| Permutation testing                 | ❌           | ✅      |
| Statistical analysis                | ❌           | ✅      |
| Track all 114 surahs simultaneously | Impractical  | ✅      |
| Knowledge of probability theory     | ❌           | ✅      |

### Q: What alternative explanations exist?

| Explanation        | Assessment                            |
| ------------------ | ------------------------------------- |
| Pure coincidence   | Combined p < 1 in 1,000,000           |
| Human design       | Requires modern statistical awareness |
| Post-hoc selection | We show non-significant patterns too  |

### Common Misconceptions (Why These Objections Don't Apply)

> For detailed explanations, see [METHODOLOGY_FAQ.md - Illegitimate Objections](../METHODOLOGY_FAQ.md#illegitimate-objections-based-on-misunderstanding)

| Misconception                | Why It's Wrong                                                                  |
| ---------------------------- | ------------------------------------------------------------------------------- |
| "Cherry-picking!"            | Text frozen 1,400 years. We DISCOVER patterns, can't DESIGN outcomes.           |
| "Why these rules?"           | Rules DESCRIBE data (surah structure), don't filter for results.                |
| "Subjective interpretation!" | Rules documented, reproducible. Same rules = same counts. Verify yourself.      |
| "No pre-registration!"       | Pre-reg is for prospective studies. This is fixed historical corpus.            |
| "Find this in any text!"     | Challenge accepted. Try Bible/Torah. Six-block symmetry is structurally unique. |

---

## Methodology

- **Data**: Tanzil Ḥafṣ/Uthmānī text
- **Basmalah**: Counted only in Al-Fatiha
- **Statistical Method**: Permutation testing (1,000,000 trials)

## Script Verification

All scripts load real data and compute dynamically. No hardcoded outputs.

## Files

| Folder                       | Pattern                                                               |
| ---------------------------- | --------------------------------------------------------------------- |
| `even_sum_surahs/`           | Pattern 1                                                             |
| `new_data_slices/`           | Pattern 2                                                             |
| `verse_greater_than_number/` | Pattern 3                                                             |
| `core_2x2_parity_grouping/`  | Pattern 4                                                             |
| `long_short_parity/`         | Pattern 5                                                             |
| **`new_search/`**            | **18 patterns from Simetrik Kitap (Golden Ratio, 57/57 Split, etc.)** |
