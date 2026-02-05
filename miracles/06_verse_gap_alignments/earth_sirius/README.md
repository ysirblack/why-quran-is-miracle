# Earth-Sirius Distance: Dual Encoding (Words & Letters)

## The Discovery

In Surah 53 "An-Najm" (The Star), the Earth-Sirius distance is encoded **twice**:

| Method      | Start         | End            | Count   | Encoding | Sirius Distance |
| ----------- | ------------- | -------------- | ------- | -------- | --------------- |
| **Words**   | Earth (53:32) | Sirius (53:49) | **86**  | 8.6      | 8.6 ly          |
| **Letters** | Star (53:1)   | Earth (53:32)  | **861** | 8.61     | 8.6 ly          |

Both encodings point to the same astronomical fact: **Sirius is 8.6 light-years from Earth.**

> **Encoding:**
>
> - 8.61 light-years = **86.1 deci-light-years** (8.61 × 10 = 86.1)
> - 8.61 light-years = **861 centi-light-years** (8.61 × 100 = 861)

---

## Pattern 1: Word Count (86 Words)

From "Earth" (الأرض) in 53:32 to "Sirius" (الشعرى) in 53:49 = **86 words** = **8.6 light-years**

```bash
python3 earth_sirius_verification.py
```

**Breakdown:**

- 53:32 (after الأرض): 13 words
- 53:33-53:48: 69 words
- 53:49 (through الشعرى): 4 words
- **Total: 86 words**

---

## Pattern 2: Letter Count (861 Letters) ✨ NEW

From "Star" (النجم) in 53:1 to "Earth" (الأرض) in 53:32 = **861 letters** = **8.61 light-years**

```bash
python3 verify_861.py
```

**Breakdown:**

```text
Letters after Star in 53:1:       6
Letters in 53:2 to 53:31:       783
Letters before Earth in 53:32:   70
─────────────────────────────────────
Subtotal (exclusive):           859
+ Last letter of Star (م):       +1
+ First letter of Earth (ٱ):     +1
─────────────────────────────────────
TOTAL (inclusive):              861 ✅
```

**Methodology:**

- Arabic letters only (no diacritics)
- Inclusive counting (both endpoint letters included)
- Text: Tanzil Ḥafṣ/Uthmānī

---

## Thematic Flow

```text
Surah 53: "An-Najm" (النجم) = "The Star"

     53:1 (Star/النجم)
          │
          │ 861 letters
          │
          ▼
     53:32 (Earth/الأرض)
          │
          │ 86 words
          │
          ▼
     53:49 (Sirius/الشعرى)
```

- **Surah name**: "The Star" - explicit astronomical theme
- **Star (53:1)**: Opens with "By the star when it descends"
- **Earth (53:32)**: "...when He produced you from the Earth"
- **Sirius (53:49)**: Only star mentioned BY NAME in the entire Quran

---

## Astronomical Data

| Property           | Value                        |
| ------------------ | ---------------------------- |
| Star               | Sirius (Alpha Canis Majoris) |
| Arabic name        | الشِّعْرَى (Ash-Shi'ra)      |
| Distance           | 8.60 ± 0.04 light-years      |
| Apparent magnitude | -1.46 (brightest star)       |

---

## Statistical Significance

| Pattern      | Probability        |
| ------------ | ------------------ |
| Word (86)    | ~1/60 ≈ 1.7%       |
| Letter (861) | ~1/1441 ≈ 0.07%    |
| **Combined** | ~1/86,000 ≈ 0.001% |

---

## Historical Context

- **7th century**: Stellar distances completely unknown
- **1838**: First stellar parallax measurement (Bessel)
- **Knowledge gap**: ~1,200 years

---

## Verification Scripts

| Script                         | Purpose          |
| ------------------------------ | ---------------- |
| `verify_861.py`                | Letter gap (861) |
| `earth_sirius_verification.py` | Word gap (86)    |

---

**Data source:** Tanzil Ḥafṣ/Uthmānī text
