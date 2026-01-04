# Even-Sum Surahs

## What is this pattern?

For each chapter, add its **position number** + **verse count**.

- Chapter 1 has 7 verses → 1 + 7 = 8 (even)
- Chapter 3 has 200 verses → 3 + 200 = 203 (odd)

This divides all 114 chapters into two groups:

- **57 chapters** where (position + verses) is **even**
- **57 chapters** where (position + verses) is **odd**

---

## The Pattern

When you sum up all the (position + verse) values for the **even-sum group**:

$$\sum_{\text{even-sum chapters}} (\text{position} + \text{verses}) = 6{,}236$$

This equals the **total number of verses in the entire Quran**.

---

## Worked Example

| Chapter    | Position | Verses | Position + Verses | Group  |
| ---------- | -------- | ------ | ----------------- | ------ |
| Al-Fatiha  | 1        | 7      | 8                 | Even ✓ |
| Al-Baqarah | 2        | 286    | 288               | Even ✓ |
| Al-Imran   | 3        | 200    | 203               | Odd    |
| An-Nisa    | 4        | 176    | 180               | Even ✓ |
| Al-Ma'idah | 5        | 120    | 125               | Odd    |

For the even-sum chapters, we add their (position + verses) values:

- Al-Fatiha: 8
- Al-Baqarah: 288
- An-Nisa: 180
- ... (all 57 chapters)

**Total: 6,236** = Total verses in the Quran

---

## Summary Table

| Group             | Chapter Count | Sum of (Position + Verses)     |
| ----------------- | ------------- | ------------------------------ |
| Even-sum chapters | 57            | **6,236** ← Total Quran verses |
| Odd-sum chapters  | 57            | 6,555                          |
| **All chapters**  | **114**       | **12,791**                     |

---

## Why is 57/57 split guaranteed?

The split is always 57/57 because:

- Positions 1-114 contain 57 odd and 57 even numbers
- (odd + odd) = even, (even + even) = even
- (odd + even) = odd, (even + odd) = odd

Since verse counts have a fixed parity distribution, the 57/57 split is arithmetic, not the interesting part.

**The interesting part**: The sum equaling exactly 6,236.

---

## Statistics

| Metric      | Value                           |
| ----------- | ------------------------------- |
| Probability | ~1 in 885 (0.11%)               |
| p-value     | 0.00113                         |
| Threshold   | p < 0.05 (5%)                   |
| **Result**  | **Statistically significant** ✓ |

Method: 1,000,000 permutation trials

---

## Verification

```bash
python3 even_sum_verification.py
```

Expected output:

```
Even-sum chapters: 57
Sum of (position + verses) for even group: 6236
Total Quran verses: 6236
Match: True
```
