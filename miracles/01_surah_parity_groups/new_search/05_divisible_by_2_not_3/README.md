# Divisible by 2 but NOT by 3 - Homogeneity Pattern

**Source:** Simetrik Kitap: Kur'an, pages 167-176

---

## Definition

**Property:** A number n has this property if:

- n is divisible by 2 (n % 2 == 0)
- n is NOT divisible by 3 (n % 3 != 0)

**Homogeneous:** Both position and verse count have the property, OR both don't

**Heterogeneous:** One has the property, the other doesn't

---

## Pattern

| Category      | First Half (1-57) | Second Half (58-114) |
| ------------- | ----------------- | -------------------- |
| Homogeneous   | 33                | 33                   |
| Heterogeneous | 24                | 24                   |

---

## Symmetry

- **Homo: 33/33** (equal split between halves)
- **Hetero: 24/24** (equal split between halves)

Total: 66 homogeneous, 48 heterogeneous

---

## Verification

```bash
python3 verify.py
```

---

## Statistics

- **Method:** Permutation test (100,000 trials)
- **p-value:** 0.156
- **Significant (p<0.05):** No

The observed 33/33/24/24 symmetry occurs with reasonable frequency in random arrangements of the same data.
