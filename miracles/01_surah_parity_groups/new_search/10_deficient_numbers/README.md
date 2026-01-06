# Deficient Numbers Patterns

**Source:** Simetrik Kitap: Kur'an, pages 263-281

---

## Definition

**Deficient (Kıt) Number:** A number where sum of proper divisors < n

Examples:
- 8: 1+2+4 = 7 < 8
- 10: 1+2+5 = 8 < 10
- 1: 0 < 1 (considered deficient per book)

---

## Pattern 1: Verse Deficient + Position Parity (41/41)

| Position Parity | Count |
|-----------------|-------|
| Odd | 41 |
| Even | 41 |

---

## Pattern 2: Verse NOT Deficient + Position Parity (16/16)

| Position Parity | Count |
|-----------------|-------|
| Odd | 16 |
| Even | 16 |

---

## Pattern 3: Homogeneity (71/43)

| Category | Count | Prime? |
|----------|-------|--------|
| Homogeneous | 71 | **YES** |
| Heterogeneous | 43 | **YES** |

**Both counts are prime numbers!**

---

## Summary

| Pattern | Values | Notes |
|---------|--------|-------|
| Verse deficient + parity | 41 / 41 | Perfect symmetry |
| Verse NOT deficient + parity | 16 / 16 | Perfect symmetry |
| Homo / Hetero | 71 / 43 | **Both PRIME** |

---

## Verification

```bash
python3 verify.py
```

---

## Statistics

- **Method:** Permutation test (100,000 trials)
- **p-value:** 0.165
- **Significant (p<0.05):** No

The observed symmetries occur with reasonable frequency in random arrangements.
