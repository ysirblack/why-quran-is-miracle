# Long/Short Parity Swap

## What is this pattern?

Divide all 114 chapters into two groups:

- **Long chapters**: 40 or more verses
- **Short chapters**: less than 40 verses

(There is no surah 39 verses long)

This gives exactly **57 long** and **57 short** chapters.

Now look at how odd/even positioned chapters distribute in each group:

| Group              | Odd position | Even position |
| ------------------ | ------------ | ------------- |
| Long (≥40 verses)  | 27           | 30            |
| Short (<40 verses) | 30           | 27            |

The numbers **swap**: 27/30 becomes 30/27.

---

## Examples

| Chapter        | Verses | Length | Position |
| -------------- | ------ | ------ | -------- |
| 1 (Al-Fatiha)  | 7      | Short  | Odd      |
| 2 (Al-Baqarah) | 286    | Long   | Even     |
| 3 (Al-Imran)   | 200    | Long   | Odd      |
| 32 (As-Sajdah) | 30     | Short  | Even     |

## Statistics

**57/57 Split**: This happens to be true for threshold 40 (not all thresholds give 57/57).

**27/30 Swap**:

- Probability: ~1 in 7.9 (12.7%)
- Our threshold: p < 0.05 (5%)
- Method: 1,000,000 permutation trials

**Note**: No chapter has exactly 39 verses, creating a clean boundary.

## Verification

```bash
python3 long_short_parity_verification.py
```
