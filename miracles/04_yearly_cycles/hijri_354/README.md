# The Hijri 354 Pattern: Lunar Calendar Alignment

A computational analysis of specific forms of the Arabic word "day" (يوم) in the Quran reveals exactly 354 occurrences matching the Islamic lunar year (354 days).

## How the Pattern Works

**Step 1: Identify Four Linguistic Categories**

1. **YEVM** (يوم): Simple forms - base + single modification (length ≤ 5 characters)
2. **YEVMEIZIN** (يومئذ): "That day" - all forms of yawma'idhin
3. **YEVMUHUM** (يومهم): "Their day" - all possessive forms
4. **YEVMEKUM** (يومكم): "Your day" - all possessive forms

**Step 2: Count Each Category Systematically**

- Apply consistent linguistic rules for each category
- Count all occurrences across the entire text
- No filtering within categories (count all forms)

**Step 3: Sum the Categories**

Simple forms + That day + Their day + Your day = 354

## Verified Counts

| Category      | Count   | Linguistic Rule                                       | Example Verses       |
| ------------- | ------- | ----------------------------------------------------- | -------------------- |
| **YEVM**      | 274     | Simple forms (base + single modification, length ≤ 5) | 1:4, 2:8, 3:9        |
| **YEVMEIZIN** | 70      | All forms of يومئذ (yawma'idhin - "that day")         | 3:167, 4:42, 6:16    |
| **YEVMUHUM**  | 5       | All forms of يومهم (yawmahum - "their day")           | 7:51, 43:83, 51:60   |
| **YEVMEKUM**  | 5       | All forms of يومكم (yawmukum - "your day")            | 6:130, 21:103, 32:14 |
| **TOTAL**     | **354** | **Islamic lunar year**                                | -                    |

## Hijri Month Length (29 days)

In addition to the 354-day year match, the plural and dual day forms alone align with the
short Hijri month length (29 days). The helper script below strips diacritics, normalises
prefix/suffix attachments, and lists every verse contributing to the total:

```bash
python miracles/04_yearly_cycles/hijri_354/days_29_verifier.py
```

**Results:**

- ✅ `أيام` (plural days): 26 occurrences
- ✅ `يومين` (dual “two days”): 3 occurrences
- ✅ Combined total: 29 (matches the 29-day lunar month)

This count uses purely grammatical criteria—no additional categories—which makes it a
useful baseline when comparing to alternative rule sets in the solar analysis.

## The Mathematical Alignment

**Perfect 354 Total**: Exactly matches the Islamic lunar year (approximately 12 × 29.5 days)

**Linguistic Coherence**: Each category follows clear grammatical principles:

- **YEVM**: Distinguishes simple forms (base + one element) from compound forms (base + multiple elements)
  - Included: يوم (yawm), ويوم (wa-yawm), فيوم (fa-yawm)
  - Excluded: كيومكم (ka-yawmukum), وبيومهم (wa-bi-yawmihim)
- **YEVMEIZIN**: All forms of the specific compound يومئذ (yawma'idhin)

  - No filtering by prefix or grammatical role
  - Simple rule: if it contains يومئذ, count it

- **YEVMUHUM & YEVMEKUM**: All possessive forms
  - Simple pattern matching
  - No exclusions

**Dual Calendar Recognition**: Complements the solar year (365) pattern, demonstrating awareness of both solar and lunar cycles.

## Statistical Significance

### Bootstrap Resampling Analysis (Recommended)

The `bootstrap_probability_analysis.py` script in the parent folder tests whether these exact totals could occur by chance while preserving linguistic structure. Based on 100,000 trials:

| Pattern                             | Bootstrap Probability | Interpretation            |
| ----------------------------------- | --------------------- | ------------------------- |
| Hijri 354 alone                     | ~4.2% (~1 in 24)      | Moderately common         |
| Solar 365 AND Hijri 354             | ~0.15% (~1 in 667)    | Notable                   |
| All three patterns (365 + 354 + 29) | ~0.04% (~1 in 2,500)  | Statistically significant |

The bootstrap method:

1. Resamples the 478 actual "day" tokens with replacement
2. Recategorizes them using the same grammatical rules
3. Checks if we get exactly 354 for Hijri, 365 for solar, and 29 for lunar
4. Repeats 100,000 times to estimate probability

This approach preserves the realistic distribution of grammatical forms (definite, possessive, plural, etc.) rather than assuming all token arrangements are equally likely.

### Combinatorial Analysis (Baseline Reference)

For comparison, `combined_probability_analysis.py` uses a uniform subset model (every subset of tokens equally likely):

- P(Hijri 354) ≈ 1 in 4.259 × 10¹⁰⁰
- This is mathematically correct but linguistically unrealistic

**Recommendation**: Use the bootstrap probabilities when discussing statistical significance, as they better reflect how language actually works.

## Verification

All counts are computationally verified and reproducible:

```bash
python miracles/04_yearly_cycles/hijri_354/hijri_354_combined.py
```

**Results:**

- ✅ YEVM: 274
- ✅ YEVMEIZIN: 70
- ✅ YEVMUHUM: 5
- ✅ YEVMEKUM: 5
- ✅ **TOTAL: 354**

## Data Source

- **Text**: Tanzil Ḥafṣ/Uthmānī (canonical digital Quran corpus)
- **Verses**: 6,236 total
- **Method**: Diacritics removed, token-by-token pattern matching

## Linguistic Justification

### YEVM (length ≤ 5)

The length filter distinguishes:

- **Simple forms**: Base + single modification
  - يوم (3 chars) - base "day"
  - ويوم (4 chars) - "and day"
  - يومها (5 chars) - "her day"
- **Compound forms**: Base + multiple modifications
  - كيومكم (6 chars) - "like your day" (preposition + base + possessive)
  - وبيومهم (7 chars) - "and with their day" (conjunction + preposition + base + possessive)

This mirrors standard Arabic morphology where stacked modifications increase complexity.

### YEVMEIZIN (all forms)

All forms of يومئذ (yawma'idhin - "that day"):

- Base forms (length 5): 60
- Prefixed forms (length 6): 10
  - wa-prefixed: 1
  - fa-prefixed: 4
  - Other: 5

No filtering - counts all grammatical variants of this specific temporal expression.

### Possessives (all forms)

YEVMUHUM (يومهم): 5 occurrences  
YEVMEKUM (يومكم): 5 occurrences

Simple pattern matching - counts all possessive constructions.

## Reproducibility

All scripts are available for independent verification:

- `count_yevm_only.py` - YEVM simple forms
- `count_yevmeizin_only.py` - YEVMEIZIN all forms
- `count_yevmuhum_only.py` - YEVMUHUM possessives
- `count_yevmekum_only.py` - YEVMEKUM possessives
- `hijri_354_combined.py` - Combined verification

Each script uses clear, documented linguistic rules applied systematically to the entire text.
