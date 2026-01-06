# 6236 Pattern

**Source:** Simetrik Kitap: Kur'an, pages 351-354

---

## Definition

**6236** = Total verse count in the Quran

**6236-like property:** A 4-digit number ABCD where:

- A = D (first digit = last digit)
- A = B × C (first digit = product of middle digits)

For 6236: **6 = 6** and **6 = 2 × 3** ✓

---

## The 23 Numbers

| #      | Number   | Pattern        |
| ------ | -------- | -------------- |
| 1      | 1111     | 1=1, 1=1×1     |
| 2      | 2122     | 2=2, 2=1×2     |
| 3      | 2212     | 2=2, 2=2×1     |
| 4      | 3133     | 3=3, 3=1×3     |
| 5      | 3313     | 3=3, 3=3×1     |
| 6      | 4144     | 4=4, 4=1×4     |
| 7      | 4224     | 4=4, 4=2×2     |
| 8      | 4414     | 4=4, 4=4×1     |
| 9      | 5155     | 5=5, 5=1×5     |
| 10     | 5515     | 5=5, 5=5×1     |
| 11     | 6166     | 6=6, 6=1×6     |
| **12** | **6236** | **6=6, 6=2×3** |
| 13     | 6326     | 6=6, 6=3×2     |
| 14     | 6616     | 6=6, 6=6×1     |
| 15     | 7177     | 7=7, 7=1×7     |
| 16     | 7717     | 7=7, 7=7×1     |
| 17     | 8188     | 8=8, 8=1×8     |
| 18     | 8248     | 8=8, 8=2×4     |
| 19     | 8428     | 8=8, 8=4×2     |
| 20     | 8818     | 8=8, 8=8×1     |
| 21     | 9199     | 9=9, 9=1×9     |
| 22     | 9339     | 9=9, 9=3×3     |
| 23     | 9919     | 9=9, 9=9×1     |

---

## Remarkable Properties

### Count = 23

- **23 is PRIME!**
- 23 = middle digits of 6236 (2 and 3)
- 23 = years of Quran revelation to Prophet Muhammad (pbuh)

### Position = Center

- 6236 is at position **12** (exact center of 23)
- 11 numbers above
- 11 numbers below

### Digit Sum Ratio

| Position   | Digit Sum |
| ---------- | --------- |
| Above 6236 | 127       |
| Below 6236 | 254       |

**254 = 2 × 127** (exactly double!)

### Odd/Even Symmetry

| Type | Above | Below |
| ---- | ----- | ----- |
| Odd  | 5     | 5     |
| Even | 6     | 6     |

---

## Verification

```bash
python3 verify.py
```

---

## Statistics

- **Method:** Monte Carlo simulation (100,000 trials, range 4000-8000)
- **p-value:** 0.00029 (for hitting exact value 6236)
- **Significant (p<0.05):** Yes
- **Passes Bonferroni correction (p<0.00278):** Yes

### Methodological Note:
This is a mathematical curiosity about the number 6236. The "6236-like property" was defined after observing the total. The test asks: "What's the probability that a random verse total in the range 4000-8000 would be 6236?" This is significant but should be interpreted carefully as numerological rather than structural.
