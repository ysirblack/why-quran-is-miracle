# Six-Block Symphony

## What is this pattern?

Divide the 114 chapters into **6 blocks of 19 chapters** each:

| Block | Chapters |
| ----- | -------- |
| 1     | 1-19     |
| 2     | 20-38    |
| 3     | 39-57    |
| 4     | 58-76    |
| 5     | 77-95    |
| 6     | 96-114   |

Within each block, count how many chapters fall into each parity category (odd position + odd verses, etc.).

**The finding**: Multiple classification systems produce **alternating patterns** across all 6 blocks.

Example - Odd-Odd counts per block: **[6, 5, 4, 1, 4, 7]** → parities alternate E-O-E-O-E-O

---

## The Patterns

### 2×2 Parity Grid (per block)

| Category  | Block 1 | Block 2 | Block 3 | Block 4 | Block 5 | Block 6 | Parity Pattern |
| --------- | ------- | ------- | ------- | ------- | ------- | ------- | -------------- |
| Odd-Odd   | 6       | 5       | 4       | 1       | 4       | 7       | E-O-E-O-E-O    |
| Even-Odd  | 4       | 3       | 8       | 3       | 4       | 5       | E-O-E-O-E-O    |
| Odd-Even  | 4       | 4       | 6       | 8       | 6       | 2       | all even       |
| Even-Even | 5       | 7       | 1       | 7       | 5       | 5       | all odd        |

### Homogeneous vs Heterogeneous

| Category         | Block 1 | Block 2 | Block 3 | Block 4 | Block 5 | Block 6 | Parity Pattern |
| ---------------- | ------- | ------- | ------- | ------- | ------- | ------- | -------------- |
| Same parity      | 11      | 12      | 5       | 8       | 9       | 12      | O-E-O-E-O-E    |
| Different parity | 8       | 7       | 14      | 11      | 10      | 7       | E-O-E-O-E-O    |

## Statistics

**All patterns simultaneously**:

- Probability: ~1 in 29,412 (0.0034%)
- Our threshold: p < 0.05 (5%)
- Method: 1,000,000 permutation trials
- **Passes threshold**: Yes (most significant pattern in this folder)

**Note**: 6 of 8 patterns derive from the same 2×2 grid, so they're not fully independent.

## Verification

```bash
python3 new_data_slices_verification.py
```

---

## PS: Detailed Explanation

**Step 1: What is a "parity category"?**

Each chapter has two properties:

- Position parity: Is the chapter number odd or even?
- Verse parity: Is the verse count odd or even?

This creates 4 categories:

- **Odd-Odd**: Chapter 1 (position 1=odd, 7 verses=odd)
- **Even-Even**: Chapter 2 (position 2=even, 286 verses=even)
- **Odd-Even**: Chapter 3 (position 3=odd, 200 verses=even)
- **Even-Odd**: Chapter 6 (position 6=even, 165 verses=odd)

**Step 2: What do we count in each block?**

Take Block 1 (chapters 1-19). Count how many chapters fall into each category:

- Odd-Odd: 6 chapters
- Even-Odd: 4 chapters
- Odd-Even: 4 chapters
- Even-Even: 5 chapters

Do this for all 6 blocks.

**Step 3: What is the "alternating pattern"?**

Look at the Odd-Odd counts across all blocks: **[6, 5, 4, 1, 4, 7]**

Now check each number's parity:

- 6 = Even (E)
- 5 = Odd (O)
- 4 = Even (E)
- 1 = Odd (O)
- 4 = Even (E)
- 7 = Odd (O)

Pattern: **E-O-E-O-E-O** — it alternates perfectly!

**Step 4: Why is this notable?**

Multiple different count sequences (Odd-Odd, Even-Odd, Homogeneous, etc.) ALL show this alternating behavior simultaneously. The probability of this happening by chance is ~1 in 29,412.

**Simple analogy**: Imagine rolling dice 6 times and getting alternating odd/even results. That's ~1 in 64. Now imagine doing this with 7 different dice sequences simultaneously — that's much rarer.
