# Homogeneous / Half Symmetry (28/29/29/28)

**Source:** Simetrik Kitap: Kur'an, pages 74-76

---

## Definitions

**Homogeneous (Türdeş):** Position and verse count have the same parity

- Both odd (e.g., Surah 1, 7 verses → odd-odd)
- Both even (e.g., Surah 2, 286 verses → even-even)

**Heterogeneous (Türdeş Olmayan):** Different parity

- Position odd, verses even
- Position even, verses odd

**First Half:** Surahs 1-57
**Second Half:** Surahs 58-114

---

## Pattern

| Group         | First Half (1-57) | Second Half (58-114) |
| ------------- | ----------------- | -------------------- |
| Homogeneous   | 28                | 29                   |
| Heterogeneous | 29                | 28                   |

**Symmetry:** 28 / 29 / 29 / 28 (Mirror symmetry)

```text
Homogeneous:     28  ←→  29
Heterogeneous:   29  ←→  28
                 ↑       ↑
               First   Second
               Half    Half
```

---

## Totals

- Total homogeneous: 28 + 29 = **57**
- Total heterogeneous: 29 + 28 = **57**
- Total surahs: 114

---

## Verification

```bash
python3 verify.py
```

---

## Statistics

- **Method:** Permutation test (100,000 trials)
- **p-value:** 0.148
- **Significant (p<0.05):** No

The observed 28/29/29/28 symmetry occurs with reasonable frequency in random arrangements of the same data.

---

## Notes

- 57/57 split is guaranteed (homogeneous + heterogeneous = 114)
- The actual pattern: 28/29/29/28 mirror symmetry in first/second half distribution
