# Verse-Number Mirror

## What is this pattern?

First, filter to chapters where **verse count > chapter position**.

Example: Chapter 1 has 7 verses. 7 > 1, so it qualifies.
Example: Chapter 50 has 45 verses. 45 < 50, so it doesn't qualify.

This filter gives exactly **48 chapters**.

Now classify these 48 chapters two different ways:

**Method 1**: Subtract (verses - position). Is the result odd or even?
**Method 2**: Is the chapter position odd or even?

| Method                | Odd | Even |
| --------------------- | --- | ---- |
| By subtraction result | 23  | 25   |
| By position           | 25  | 23   |

The numbers **mirror**: 23/25 becomes 25/23.

---

## Examples

| Chapter    | Position | Verses | Difference | Result | Position Parity |
| ---------- | -------- | ------ | ---------- | ------ | --------------- |
| Al-Fatiha  | 1        | 7      | 6          | Even   | Odd             |
| Al-Baqarah | 2        | 286    | 284        | Even   | Even            |
| Al-Imran   | 3        | 200    | 197        | Odd    | Odd             |
| Al-An'am   | 6        | 165    | 159        | Odd    | Even            |

## Statistics

- Probability: ~1 in 439 (0.23%)
- Our threshold: p < 0.05 (5%)
- Method: 1,000,000 permutation trials
- **Passes threshold**: Yes

## Verification

```bash
python3 verses_greater_verification.py
```
