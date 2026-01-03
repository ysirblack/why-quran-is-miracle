# Core 2×2 Parity Grid

## What is this pattern?

Every Quran chapter has two properties:

- Its **position** (1st, 2nd, 3rd...) - which is either odd or even
- Its **verse count** - which is either odd or even

When you sort all 114 chapters into 4 groups based on these two properties, you get:

| Position | Verse Count | Count |
| -------- | ----------- | ----- |
| Odd      | Odd         | 27    |
| Even     | Even        | 30    |
| Odd      | Even        | 30    |
| Even     | Odd         | 27    |

The distribution is symmetric: **27, 30, 30, 27**.

---

## Examples

| Chapter        | Position | Verses     | Group     |
| -------------- | -------- | ---------- | --------- |
| 1 (Al-Fatiha)  | 1 (odd)  | 7 (odd)    | Odd-Odd   |
| 2 (Al-Baqarah) | 2 (even) | 286 (even) | Even-Even |
| 3 (Al-Imran)   | 3 (odd)  | 200 (even) | Odd-Even  |
| 6 (Al-An'am)   | 6 (even) | 165 (odd)  | Even-Odd  |

## Statistics

- **Probability**: ~1 in 6.7 (14.9%)
- **Our threshold**: p < 0.05 (5%)
- **Method**: 1,000,000 permutation trials

## Verification

```bash
python3 core_2x2_parity_verification.py
```
