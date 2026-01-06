# Divisible by 3 but NOT by 2 - Homogeneity Pattern

**Source:** Simetrik Kitap: Kur'an, pages 179-189

---

## Definition

**Property:** A number n has this property if:

- n is divisible by 3 (n % 3 == 0)
- n is NOT divisible by 2 (n % 2 != 0)

**Homogeneous:** Both position and verse count have the property, OR both don't

**Heterogeneous:** One has the property, the other doesn't

---

## Pattern

| Category      | First Half (1-57) | Second Half (58-114) |
| ------------- | ----------------- | -------------------- |
| Homogeneous   | 42                | 42                   |
| Heterogeneous | 15                | 15                   |

---

## Symmetry

- **Homo: 42/42** (equal split between halves)
- **Hetero: 15/15** (equal split between halves)

Total: 84 homogeneous, 30 heterogeneous

---

## Verification

```bash
python3 verify.py
```

---

## Statistics

- **Method:** Permutation test (100,000 trials)
- **p-value:** 0.194
- **Significant (p<0.05):** No

The observed 42/42/15/15 symmetry occurs with reasonable frequency in random arrangements of the same data.
