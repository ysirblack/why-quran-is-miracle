# Divisor Count = 2 (Prime Numbers) Patterns

**Source:** Simetrik Kitap: Kur'an, pages 337-347

---

## Definition

**Divisor count = 2:** Numbers with exactly 2 divisors (prime numbers)

Examples:
- 2 has divisors {1, 2} → count = 2 ✓
- 7 has divisors {1, 7} → count = 2 ✓
- 1 has divisors {1} → count = 1 ✗
- 6 has divisors {1, 2, 3, 6} → count = 4 ✗

---

## Total Counts

| Category | Count |
|----------|-------|
| Homogeneous | 66 |
| Heterogeneous | 48 |

---

## Pattern: Split by Half (33/33/24/24)

| Category | First Half (1-57) | Second Half (58-114) |
|----------|-------------------|----------------------|
| Homogeneous | 33 | 33 |
| Heterogeneous | 24 | 24 |

Both categories split equally between halves!

---

## Summary

| Pattern | Values | Notes |
|---------|--------|-------|
| Homo first/second | 33 / 33 | Equal split |
| Hetero first/second | 24 / 24 | Equal split |

---

## Verification

```bash
python3 verify.py
```

---

## Statistics

**Status:** Not yet tested

p-value to be calculated
