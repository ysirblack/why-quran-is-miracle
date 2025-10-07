# New Data Slices - Six 19-Surah Blocks (Hafs/Tanzil)

Rule: Basmalah counted only in Al-Fatihah. Group by surah order and ayat counts (Tanzil Hafs/Uthmani).

## Six fixed blocks of 19 surahs

- Blocks: [1-19], [20-38], [39-57], [58-76], [77-95], [96-114]
- Odd-order per block: [10, 9, 10, 9, 10, 9]
- Even-order per block: [9, 10, 9, 10, 9, 10]

These order-parity counts are fixed by construction (19 labels per block).

## 2x2 parity grid (order x ayat)

For each block, classify surahs by order parity and ayat parity, then count:

- ODD-ODD: [6, 5, 4, 1, 4, 7] -> parity pattern E-O-E-O-E-O
- EVEN-ODD: [4, 3, 8, 3, 4, 5] -> E-O-E-O-E-O
- ODD-EVEN: [4, 4, 6, 8, 6, 2] -> all even
- EVEN-EVEN: [5, 7, 1, 7, 5, 5] -> all odd

The count sequences show neat alternation across blocks.

## Homogeneous vs heterogeneous (by parity)

Aggregate the 2x2 grid by "same parity" vs "different parity":

- Homogeneous (order parity = ayat parity): [11, 12, 5, 8, 9, 12] -> O-E-O-E-O-E
- Heterogeneous (!=): [8, 7, 14, 11, 10, 7] -> E-O-E-O-E-O

These two sequences are implied by the 2x2 grid; they simply re-express it.

## Prime-homogeneous vs prime-heterogeneous (independent slice)

Use the document's convention where 1 is treated as "prime," and compare "prime/non-prime" of order vs ayat:

- Prime-homogeneous (same prime status): [11, 12, 11, 10, 11, 12] -> O-E-O-E-O-E
- Prime-heterogeneous (different): [8, 7, 8, 9, 8, 7]

This "prime" view is an independent slice that also yields tidy alternations.

## Reproduce / verify

- Data: data/quran-uthmani.txt (Tanzil Uthmani)
- Script: new_data_slices_verification.py (in this folder)
- Output includes the six 19-block arrays above and their parity patterns.

---

## Statistical Analysis

**Permutation Test (1,000,000 trials):**

**Pattern Independence:**

- 6 parity-based patterns are derived from the same 2×2 grid (NOT independent)
- 2 prime-based patterns provide independent classification

**Individual Patterns:**

- Each alternating pattern: ~1 in 16 to 1 in 64 individually
- Fairly common when tested separately

**All Patterns Together:**

- **Probability**: ~1 in 29,412 (0.0034%)
- **Test**: 1,000,000 trials, 34 matches
- Requires all patterns simultaneously

**Independence**: These block-based patterns are independent from individual surah parity patterns analyzed earlier.
