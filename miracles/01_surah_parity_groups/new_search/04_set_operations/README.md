# Set Operations Patterns

**Source:** Simetrik Kitap: Kur'an, pages 139-163

---

## Overview

Multiple symmetric patterns found through set operations on position numbers and verse counts.

---

## Pattern 1: Intersections (32/32)

**Source:** Pages 141-142

| Operation                          | Result |
| ---------------------------------- | ------ |
| Odd positions ∩ Odd verse counts   | 32     |
| Even positions ∩ Even verse counts | 32     |

---

## Pattern 2: Set Differences (25/25)

**Source:** Pages 145-146

| Operation                          | Result |
| ---------------------------------- | ------ |
| Odd positions - Odd verse counts   | 25     |
| Even positions - Even verse counts | 25     |

---

## Pattern 3: Verse Count in Position Numbers (101/13)

**Source:** Pages 149-150

| Category                            | Count | Prime?  |
| ----------------------------------- | ----- | ------- |
| Verse count IN positions (1-114)    | 101   | **YES** |
| Verse count NOT in positions (>114) | 13    | **YES** |

**Both counts are prime numbers!**

---

## Pattern 4: Verse in Pos + Position Odd + Parity (25/25)

**Source:** Pages 154-155

| Condition                   | Homogeneous | Heterogeneous |
| --------------------------- | ----------- | ------------- |
| Verse in pos + Position odd | 25          | 25            |

---

## Pattern 5: Verse NOT in Pos + Position Even + Parity (3/3)

**Source:** Page 158

| Condition                        | Homogeneous | Heterogeneous |
| -------------------------------- | ----------- | ------------- |
| Verse NOT in pos + Position even | 3           | 3             |

---

## Pattern 6: Position NOT in VC + Hetero (10/10)

**Source:** Page 161

| Position Parity | Heterogeneous |
| --------------- | ------------- |
| Odd             | 10            |
| Even            | 10            |

---

## Pattern 7: Position NOT in VC + Homo (15/15)

**Source:** Page 163

| Position Parity | Homogeneous |
| --------------- | ----------- |
| Odd             | 15          |
| Even            | 15          |

---

## Summary

| Pattern                          | Values   | Notes            |
| -------------------------------- | -------- | ---------------- |
| Intersections                    | 32 / 32  | Perfect symmetry |
| Differences                      | 25 / 25  | Perfect symmetry |
| Verse in positions               | 101 / 13 | **Both PRIME**   |
| Verse in pos + odd + parity      | 25 / 25  | Perfect symmetry |
| Verse NOT in pos + even + parity | 3 / 3    | Perfect symmetry |
| Pos NOT in VC + hetero           | 10 / 10  | Perfect symmetry |
| Pos NOT in VC + homo             | 15 / 15  | Perfect symmetry |

---

## Verification

```bash
python3 verify.py
```

---

## Statistics

- **Method:** Bootstrap test (100,000 trials, uniform 3-286)
- **p-value:** 0.081
- **Significant (p<0.05):** No

Note: Bootstrap used because set operations on unique verse values don't change with permutation.
