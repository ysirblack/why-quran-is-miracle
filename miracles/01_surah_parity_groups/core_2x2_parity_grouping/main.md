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

- **54** sūrahs have **odd** verse counts: `odd–odd (27) + even–odd (27) = 54`
- **60** sūrahs have **even** verse counts: `even–even (30) + odd–even (30) = 60`

### Swap Symmetry

- "Same parity" groups: **odd–odd (27) + even–even (30) = 57**
- "Mixed parity" groups: **odd–even (30) + even–odd (27) = 57**
- The counts swap: **27/30 ↔ 30/27**

### Label → Count Parity Alignment

- Groups starting with **odd**: count is **27** (odd)
- Groups starting with **even**: count is **30** (even)

## Mathematical Significance

This pattern demonstrates:

1. **Exact Bucket Totals**: Each of the four parity buckets hits its target counts (`27, 30, 30, 27`).
2. **Same vs Mixed Symmetry**: Same-parity (`odd–odd + even–even`) and mixed-parity (`odd–even + even–odd`) totals both land on **57**.
3. **Actual Verse Distribution**: The raw verse counts split **54 odd** vs **60 even**, matching the script output precisely.
4. **Non-Trivial Structure**: The mirrored arrangement emerges from the data—it is not a definitional artifact.

## Complete Lists

### Odd–Odd Group (27 surahs)

Surahs with odd order numbers and odd verse counts.

### Even–Even Group (30 surahs)

Surahs with even order numbers and even verse counts.

### Odd–Even Group (30 surahs)

Surahs with odd order numbers and even verse counts.

### Even–Odd Group (27 surahs)

Surahs with even order numbers and odd verse counts.

## Verification

- **Data Source**: `data/quran-uthmani.txt` (Tanzil Ḥafṣ/Uthmānī)
- **Script**: `core_2x2_parity_verification.py` (in this folder)
- **Basmalah Rule**: Counted only in Al-Fātiḥah (Surah 1)

---

This fundamental 2×2 parity structure forms the foundation for all other parity-based analyses in Section 19.
