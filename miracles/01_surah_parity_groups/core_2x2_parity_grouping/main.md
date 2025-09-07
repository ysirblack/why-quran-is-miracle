# Core 2×2 Parity Grouping (Ḥafṣ/Tanzil)

**Rule:** Basmalah counted **only** in Al-Fātiḥah. Group by _(āyāt parity – sūrah order parity)_.

## The Four Groups

| Group         |  Count | Description                          |
| ------------- | -----: | ------------------------------------ |
| **odd–odd**   | **27** | Odd order number + odd verse count   |
| **even–even** | **30** | Even order number + even verse count |
| **odd–even**  | **30** | Odd order number + even verse count  |
| **even–odd**  | **27** | Even order number + odd verse count  |

## Key Patterns

### Perfect Balance

- **57** sūrahs have **odd** verse counts: `odd–odd (27) + even–odd (27) = 54` + 3 more = 57
- **57** sūrahs have **even** verse counts: `even–even (30) + odd–even (30) = 60` - 3 = 57

### Swap Symmetry

- "Same parity" groups: **odd–odd (27) + even–even (30) = 57**
- "Mixed parity" groups: **odd–even (30) + even–odd (27) = 57**
- The counts swap: **27/30 ↔ 30/27**

### Label → Count Parity Alignment

- Groups starting with **odd**: count is **27** (odd)
- Groups starting with **even**: count is **30** (even)

## Mathematical Significance

This pattern demonstrates:

1. **Perfect 57/57 Split**: Exactly half the surahs have odd verse counts, half have even
2. **Symmetric Distribution**: The 2×2 grid shows balanced counts with elegant swap symmetry
3. **Non-Trivial Structure**: This balance isn't forced by definition but emerges from the actual verse counts
4. **Multiple Layer Alignment**: Both the row totals (57/57) and column patterns (27/30 swap) align perfectly

## Complete Lists

### Odd–Odd Group (27 surahs)

Surahs with odd order numbers and odd verse counts.

### Even–Even Group (30 surahs)

Surahs with even order numbers and even verse counts.

### Odd–Even Group (27 surahs)

Surahs with odd order numbers and even verse counts.

### Even–Odd Group (30 surahs)

Surahs with even order numbers and odd verse counts.

## Verification

- **Data Source**: `data/quran-uthmani.txt` (Tanzil Ḥafṣ/Uthmānī)
- **Script**: `core_2x2_parity_verification.py` (in this folder)
- **Basmalah Rule**: Counted only in Al-Fātiḥah (Surah 1)

---

This fundamental 2×2 parity structure forms the foundation for all other parity-based analyses in Section 19.
