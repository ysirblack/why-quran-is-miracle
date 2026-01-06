# Perfect Numbers Patterns

**Source:** Simetrik Kitap: Kur'an, pages 225-241

---

## Definition

**Perfect Number:** A number where the sum of proper divisors equals itself

Examples:
- 6 = 1 + 2 + 3
- 28 = 1 + 2 + 4 + 7 + 14

---

## Surahs with Perfect Verse Counts

Only 4 surahs have perfect number verse counts:

| Surah | Verses | Perfect Number |
|-------|--------|----------------|
| 71 | 28 | 28 |
| 72 | 28 | 28 |
| 109 | 6 | 6 |
| 114 | 6 | 6 |

---

## Pattern 1: Verse Perfect + Position Parity (2/2)

| Position Parity | Count |
|-----------------|-------|
| Odd | 2 |
| Even | 2 |

---

## Pattern 2: Verse NOT Perfect + Position Parity (55/55)

| Position Parity | Count |
|-----------------|-------|
| Odd | 55 |
| Even | 55 |

---

## Pattern 3: Homo + Parity (54/54)

Homogeneous (both perfect or both not perfect): 108 surahs

| Parity Status | Count |
|---------------|-------|
| Homogeneous | 54 |
| Heterogeneous | 54 |

---

## Pattern 4: Hetero + Parity (3/3)

Heterogeneous (one perfect, one not): 6 surahs

| Parity Status | Count |
|---------------|-------|
| Homogeneous | 3 |
| Heterogeneous | 3 |

---

## Summary

| Pattern | Values |
|---------|--------|
| Verse perfect + parity | 2 / 2 |
| Verse NOT perfect + parity | 55 / 55 |
| Homo + parity | 54 / 54 |
| Hetero + parity | 3 / 3 |

---

## Verification

```bash
python3 verify.py
```

---

## Statistics

- **Method:** Permutation test (100,000 trials)
- **p-value:** 0.382
- **Significant (p<0.05):** No

The observed symmetries occur with reasonable frequency in random arrangements.
