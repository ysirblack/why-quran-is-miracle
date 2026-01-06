# Long and Short Surahs Patterns

**Source:** Simetrik Kitap: Kur'an, pages 305-324

---

## Definition

**Boundary:** 39 verses

- **Long surah:** >39 verses
- **Short surah:** <39 verses

**Note:** No surah has exactly 39 verses - this creates a perfect natural boundary!

---

## Pattern 1: Long/Short Split (57/57)

| Category     | Count |
| ------------ | ----- |
| Long surahs  | 57    |
| Short surahs | 57    |

**Exact half of 114!**

---

## Pattern 2: Position Parity (27/30/30/27)

| Category | Odd Position | Even Position |
| -------- | ------------ | ------------- |
| Long     | 27           | 30            |
| Short    | 30           | 27            |

**Mirror symmetry: 27-30 / 30-27**

---

## Pattern 3: Position Matches + Parity (48/48)

Position matches = (first half AND long) OR (second half AND short)

| Parity Status | Count |
| ------------- | ----- |
| Homogeneous   | 48    |
| Heterogeneous | 48    |

---

## Pattern 4: Position NOT Matches + Parity (9/9)

| Parity Status | Count |
| ------------- | ----- |
| Homogeneous   | 9     |
| Heterogeneous | 9     |

---

## Summary

| Pattern               | Values      | Notes            |
| --------------------- | ----------- | ---------------- |
| Long / Short          | 57 / 57     | Exact half       |
| Long/Short + parity   | 27/30/30/27 | Mirror symmetry  |
| Matching + parity     | 48 / 48     | Perfect symmetry |
| NOT matching + parity | 9 / 9       | Perfect symmetry |

---

## Verification

```bash
python3 verify.py
```

---

## Statistics

**Status:** Not yet tested

p-value to be calculated
