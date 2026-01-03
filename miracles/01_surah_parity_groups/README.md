# Surah Parity Groups

Analysis of numerical patterns in the Quran's 114-chapter structure.

**Our threshold**: p < 0.05 (5%)

---

## Pattern 1: Even-Sum = Total Verses

**What is it?** Add each chapter's position + verse count. If even, it's in the "even-sum" group.

**The finding**: The 57 even-sum chapters contain exactly **6,236 verses** - the total verses in the Quran.

| Group | Count | Total verses |
|-------|-------|--------------|
| Even-sum chapters | 57 | 6,236 (= total Quran verses) |
| Odd-sum chapters | 57 | 6,555 |

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

## Methodology

- **Data**: Tanzil Ḥafṣ/Uthmānī text
- **Basmalah**: Counted only in Al-Fatiha
- **Statistical Method**: Permutation testing (1,000,000 trials)

## Script Verification

All scripts load real data and compute dynamically. No hardcoded outputs.

## Files

| Folder | Pattern |
|--------|---------|
| `even_sum_surahs/` | Pattern 1 |
| `new_data_slices/` | Pattern 2 |
| `verse_greater_than_number/` | Pattern 3 |
| `core_2x2_parity_grouping/` | Pattern 4 |
| `long_short_parity/` | Pattern 5 |
