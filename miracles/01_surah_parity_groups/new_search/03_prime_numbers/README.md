# Prime Numbers Patterns

**Source:** Simetrik Kitap: Kur'an, pages 105-134

---

# Pattern 1: Prime Totals

**Source:** Page 108

---

## The Numbers

| Value      | Description                    | Prime?  |
| ---------- | ------------------------------ | ------- |
| 6555       | Sum of positions (1+2+...+114) | No      |
| 6236       | Sum of verses                  | No      |
| **12791**  | Sum of (positions + verses)    | **YES** |
| **209029** | Sum of (position × verses)     | **YES** |

---

## Pattern

Neither the sum of positions nor the sum of verses is prime individually.

But:

1. **12791** = 6555 + 6236 = Σ(position + verses) → **PRIME**
2. **209029** = Σ(position × verses) → **PRIME**

Both combined totals are prime numbers.

---

## Calculation

```text
Sum of products = 1×7 + 2×286 + 3×200 + 4×176 + ... + 114×6
               = 7 + 572 + 600 + 704 + ... + 684
               = 209029
```

---

## Verification

```bash
python3 verify.py
```

---

## Statistics

- **Method:** Permutation test (100,000 trials)
- **p-value:** 0.078
- **Significant (p<0.05):** No

---

## Notes

- 6555 = 3 × 5 × 19 × 23 (not prime)
- 6236 = 4 × 1559 (not prime)
- 12791 is prime
- 209029 is prime

---

# Pattern 2: Prime Homogeneity (67/47)

**Source:** Pages 112-115

---

## Definition

**Homogeneous (Türdeş):** Both position AND verse count are prime, or both are NOT prime

**Heterogeneous (Türdeş Olmayan):** One is prime, the other is not

**Note:** This book considers 1 as a prime number.

---

## Pattern

| Category              | Count  |
| --------------------- | ------ |
| Both prime            | 8      |
| Both NOT prime        | 59     |
| **Total Homogeneous** | **67** |

| Category                | Count  |
| ----------------------- | ------ |
| Position prime only     | 23     |
| Verse prime only        | 24     |
| **Total Heterogeneous** | **47** |

**Result:** 67 / 47

---

## Both Prime Surahs (8 total)

| Surah | Verses |
| ----- | ------ |
| 1     | 7      |
| 13    | 43     |
| 43    | 89     |
| 97    | 5      |
| 101   | 11     |
| 103   | 3      |
| 107   | 7      |
| 113   | 5      |

---

## Verification

```bash
python3 prime_homogeneity.py
```

---

## Statistics

- **Method:** Permutation test (100,000 trials)
- **p-value:** 0.078
- **Significant (p<0.05):** No

---

# Pattern 3: Prime × Parity Combinations

**Source:** Pages 112-115

---

## Main Categories (4 combinations)

| Prime Status  | Parity Status | Count   |
| ------------- | ------------- | ------- |
| Homogeneous   | Homogeneous   | 44      |
| Homogeneous   | Heterogeneous | 23      |
| Heterogeneous | Homogeneous   | 13      |
| Heterogeneous | Heterogeneous | 34      |
| **Total**     |               | **114** |

---

## Prime Homogeneous (67) - 4-way breakdown

| Position  | Verse | Count  |
| --------- | ----- | ------ |
| Odd       | Odd   | 15     |
| Even      | Even  | 29     |
| Odd       | Even  | 11     |
| Even      | Odd   | 12     |
| **Total** |       | **67** |

---

## Prime Heterogeneous (47) - 4-way breakdown

| Position  | Verse | Count  |
| --------- | ----- | ------ |
| Odd       | Odd   | 12     |
| Even      | Even  | 1      |
| Odd       | Even  | 19     |
| Even      | Odd   | 15     |
| **Total** |       | **47** |

---

## Verification

```bash
python3 prime_parity_combinations.py
```

---

## Statistics

- **Method:** Permutation test (100,000 trials)
- **p-value:** 0.078
- **Significant (p<0.05):** No

---

# Pattern 4: Primality Meta-Pattern

**Source:** Pages 118-134

---

## Discovery

Every breakdown of 4 numbers follows the SAME primality pattern:

**NOT PRIME → PRIME → PRIME → NOT PRIME**

(Note: 1 is considered prime per the book)

---

## The 4 Groups

| Group | Description                 | Values         | Primality              |
| ----- | --------------------------- | -------------- | ---------------------- |
| 1     | Prime category counts       | 8, 59, 23, 24  | NOT, PRIME, PRIME, NOT |
| 2     | Prime × Parity combinations | 44, 23, 13, 34 | NOT, PRIME, PRIME, NOT |
| 3     | Prime homo 4-way            | 15, 29, 11, 12 | NOT, PRIME, PRIME, NOT |
| 4     | Prime hetero 4-way          | 12, 1, 19, 15  | NOT, PRIME, PRIME, NOT |

---

## Group 1: Prime Category Counts (pages 118-120)

| Category                          | Count | Prime? |
| --------------------------------- | ----- | ------ |
| Both position AND verse prime     | 8     | NOT    |
| Both position AND verse NOT prime | 59    | PRIME  |
| Position prime, verse NOT prime   | 23    | PRIME  |
| Position NOT prime, verse prime   | 24    | NOT    |

---

## Group 2: Prime × Parity Combinations (pages 124-126)

| Prime  | Parity | Count | Prime? |
| ------ | ------ | ----- | ------ |
| Homo   | Homo   | 44    | NOT    |
| Homo   | Hetero | 23    | PRIME  |
| Hetero | Homo   | 13    | PRIME  |
| Hetero | Hetero | 34    | NOT    |

---

## Group 3: Prime Homogeneous 4-way (pages 130-131)

| Position | Verse | Count | Prime? |
| -------- | ----- | ----- | ------ |
| Odd      | Odd   | 15    | NOT    |
| Even     | Even  | 29    | PRIME  |
| Odd      | Even  | 11    | PRIME  |
| Even     | Odd   | 12    | NOT    |

---

## Group 4: Prime Heterogeneous 4-way (pages 132-134)

| Position | Verse | Count | Prime?                   |
| -------- | ----- | ----- | ------------------------ |
| Odd      | Odd   | 12    | NOT                      |
| Even     | Even  | 1     | PRIME (book: 1 is prime) |
| Odd      | Even  | 19    | PRIME                    |
| Even     | Odd   | 15    | NOT                      |

---

## Verification

```bash
python3 primality_meta_pattern.py
```

---

## Statistics

- **Method:** Permutation test (100,000 trials)
- **p-value:** 0.078
- **Significant (p<0.05):** No
