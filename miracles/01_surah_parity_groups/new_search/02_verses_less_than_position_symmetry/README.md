# Verses Less Than Position Symmetry (34/32/32/34)

**Source:** Simetrik Kitap: Kur'an, page 91

---

## Filter

**Surahs where verse count < position number**

Total: 66 surahs

---

## Pattern

Two independent classifications of the same 66 surahs:

### By Difference Parity

| Difference (verses - position) | Count |
|-------------------------------|-------|
| Odd                           | 34    |
| Even                          | 32    |

### By Position Parity

| Position | Count |
|----------|-------|
| Odd      | 32    |
| Even     | 34    |

---

## Symmetry

**34 / 32 / 32 / 34** (Mirror symmetry)

```text
Diff odd:   34  ←→  32  :Diff even
Pos odd:    32  ←→  34  :Pos even
```

The numbers mirror each other: 34-32 and 32-34

---

## Verification

```bash
python3 verify.py
```

---

## Statistics

- **Method:** Permutation test (100,000 trials)
- **p-value:** 0.085
- **Significant (p<0.05):** No

The observed 34/32/32/34 symmetry occurs with reasonable frequency in random arrangements of the same data.
