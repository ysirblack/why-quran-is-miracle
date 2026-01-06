# Arithmetic Mean Patterns

**Source:** Simetrik Kitap: Kur'an, pages 289-303

---

## Definition

**Mean verse count** = 6236 / 114 ≈ 54.70

**Position matches (örtüşen):**
- First half (1-57) AND above average, OR
- Second half (58-114) AND below average

---

## Pattern 1: Above/Below Average (41/73)

| Category | Count | Prime? |
|----------|-------|--------|
| Above average | 41 | **YES** |
| Below average | 73 | **YES** |

**Both counts are prime numbers!**

---

## Pattern 2: Position Matches + Parity (48/48)

| Parity Status | Count |
|---------------|-------|
| Homogeneous | 48 |
| Heterogeneous | 48 |

---

## Pattern 3: Position NOT Matches + Parity (9/9)

| Parity Status | Count |
|---------------|-------|
| Homogeneous | 9 |
| Heterogeneous | 9 |

---

## Summary

| Pattern | Values | Notes |
|---------|--------|-------|
| Above / Below average | 41 / 73 | **Both PRIME** |
| Matching + parity | 48 / 48 | Perfect symmetry |
| NOT matching + parity | 9 / 9 | Perfect symmetry |

---

## Verification

```bash
python3 verify.py
```

---

## Statistics

- **Method:** Bootstrap test (100,000 trials, uniform 3-286)
- **p-value:** 0.112
- **Significant (p<0.05):** No

Note: Bootstrap used because above/below average counts don't change with permutation of the same values.
