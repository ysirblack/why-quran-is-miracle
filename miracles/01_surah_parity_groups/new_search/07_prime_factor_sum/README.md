# Prime Factor Sum (a₀) Patterns

**Source:** Simetrik Kitap: Kur'an, pages 191-221

---

## Definition

**a₀(n)** = Sum of prime factors with multiplicity

Examples:
- a₀(12) = 2 + 2 + 3 = 7 (since 12 = 2² × 3)
- a₀(18) = 2 + 3 + 3 = 8 (since 18 = 2 × 3²)
- a₀(1) = 1 (special case per book)

---

## Pattern 1: Odd/Odd (71/71)

| Category | Count | Prime? |
|----------|-------|--------|
| a₀(verse) odd | 71 | **YES** |
| a₀(position) odd | 71 | **YES** |

**Both counts are prime!**

---

## Pattern 2: Even/Even (43/43)

| Category | Count | Prime? |
|----------|-------|--------|
| a₀(verse) even | 43 | **YES** |
| a₀(position) even | 43 | **YES** |

**Both counts are prime!**

---

## Pattern 3: Prime/Not Prime (60/54)

| Category | Count |
|----------|-------|
| a₀(verse) prime | 60 |
| a₀(verse) NOT prime | 54 |

---

## Pattern 4: Cross-reference (27/27/33/33)

| Category | First Half | Second Half |
|----------|------------|-------------|
| a₀(verse) prime | 27 | 33 |
| Verse even | 27 | 33 |

Perfect alignment!

---

## Pattern 5: Cross-reference (30/30/24/24)

| Category | First Half | Second Half |
|----------|------------|-------------|
| a₀(verse) NOT prime | 30 | 24 |
| Verse odd | 30 | 24 |

Perfect alignment!

---

## Summary

| Pattern | Values | Notes |
|---------|--------|-------|
| a₀ odd | 71 / 71 | **Both PRIME** |
| a₀ even | 43 / 43 | **Both PRIME** |
| a₀ prime/not | 60 / 54 | |
| a₀ prime ↔ verse even | 27/27 / 33/33 | Cross-alignment |
| a₀ not prime ↔ verse odd | 30/30 / 24/24 | Cross-alignment |

---

## Verification

```bash
python3 verify.py
```

---

## Statistics

- **Method:** Bootstrap test (100,000 trials, uniform 3-286)
- **p-value:** 0.062
- **Significant (p<0.05):** No

Note: Bootstrap used because PFS parity counts don't change with permutation of the same values.
