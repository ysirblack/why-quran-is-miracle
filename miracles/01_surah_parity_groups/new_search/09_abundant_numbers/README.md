# Abundant Numbers Patterns

**Source:** Simetrik Kitap: Kur'an, pages 245-260

---

## Definition

**Abundant (Zengin) Number:** A number where sum of proper divisors > n

Examples:
- 12: 1+2+3+4+6 = 16 > 12
- 18: 1+2+3+6+9 = 21 > 18

---

## Pattern 1: Verse Abundant + Position Parity (14/14)

| Position Parity | Count |
|-----------------|-------|
| Odd | 14 |
| Even | 14 |

---

## Pattern 2: Verse NOT Abundant + Position Parity (43/43)

| Position Parity | Count |
|-----------------|-------|
| Odd | 43 |
| Even | 43 |

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
| Verse abundant + parity | 14 / 14 | Perfect symmetry |
| Verse NOT abundant + parity | 43 / 43 | Perfect symmetry |
| Homo / Hetero | 71 / 43 | **Both PRIME** |

---

## Verification

```bash
python3 verify.py
```

---

## Statistics

**Status:** Not yet tested

p-value to be calculated
