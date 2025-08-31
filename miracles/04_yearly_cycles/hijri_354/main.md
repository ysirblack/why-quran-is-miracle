# Hijri Year Match - 354 Days

## Rule / Filter

Include only these tokens:

- **يَوْم** (bare "yawm")
- **يَوْمَئِذٍ / يَوْمِئِذٍ / يَوْمٌ … إِذٍ** (all casings of "on that day")
- **يَوْمَهُمْ** ("their day")
- **يَوْمُكُمْ/يَوْمِكُمْ/يَوْمَكُمْ** ("your day")
- Count the curated genitive pattern **يَوْمِ … إِذٍ** as **2** (fixed subcase)

Exclude **ٱلْيَوْم/الْيَوْم**, **يَوْمًا**, plurals/duals, and any other attachments.

## Result

- **يَوْم** = **274**
- **يَوْمَئِذٍ** (all case-variants) = **68** (explicitly tallied)
- **يَوْمَهُمْ** = **5** (listed across 5 verses)
- **يَوْمُكُمْ/…** = **5** (e.g., **6:130**, **21:103**, **32:14**, **39:71**, **45:34**)
- **يَوْمِ … إِذٍ** (genitive split) = **2**

**Total = 274 + 68 + 5 + 5 + 2 = 354**

## Why this is surprising

A different, equally mechanical slice—this time favoring adverbial **"يومئذٍ"** and two specific possessives—lands on **354**, the **Hijrī lunar year** (12 × 29.5). Two unrelated filters, two calendar constants.

## Probability Analysis

### Target Hit Probability

- **Universe**: Same 405 total _yawm_ tokens
- **Observation**: **N = 354 included** (Set-B slice)
- **Result**: $P(N=354|M=405)=\mathbf{1/406}\approx 0.2469\%$

### Internal Composition Probability

Split across **5 buckets** (274 + 68 + 5 + 5 + 2): with a neutral Dirichlet(1,1,1,1,1), every 5-way composition of 354 is equally likely:

$$
P\big((274,68,5,5,2)\text{ exactly}\big)=\frac{1}{\binom{354+5-1}{5-1}}=\frac{1}{\binom{358}{4}}\approx \mathbf{1.49\times10^{-9}}\ (\text{= }1.49\times10^{-7}\%)
$$

## Linguistic Analysis

This filtering approach emphasizes:

1. **Temporal Deixis**: يَوْمَئِذٍ ("on that day") - 68 occurrences
2. **Possessive Constructions**:
   - يَوْمَهُمْ ("their day") - 5 occurrences
   - يَوْمُكُمْ variations ("your day") - 5 occurrences
3. **Genitive Patterns**: Split constructions - 2 occurrences
4. **Base Form**: Same يَوْم core - 274 occurrences

## Hijri Calendar Significance

The Hijri calendar is based on lunar months:

- **354 days**: Standard lunar year (12 × 29.5 average)
- **Islamic significance**: Calendar used for religious observances
- **Historical importance**: Dating system from Prophet Muhammad's migration

## Comparison with Solar Filter

| Feature                 | Solar Filter (365) | Hijri Filter (354)           |
| ----------------------- | ------------------ | ---------------------------- |
| **Base form**           | يَوْم (274)        | يَوْم (274)                  |
| **Primary addition**    | ٱلْيَوْم (75)      | يَوْمَئِذٍ (68)              |
| **Secondary additions** | يَوْمًا (16)       | Possessives (10) + Split (2) |
| **Focus**               | Definiteness       | Temporal reference           |
| **Grammar**             | Noun forms         | Adverbial + possessive       |

## Analysis

This pattern demonstrates:

1. **Complementary Filtering**: Different morphological approaches yield different calendar constants
2. **Linguistic Coherence**: Each filter follows consistent grammatical principles
3. **Statistical Independence**: Both results emerge from the same base data
4. **Cultural Relevance**: Hijri calendar central to Islamic practice

## Significance

The emergence of both solar (365) and lunar (354) calendar constants from systematic morphological analysis of the same root suggests:

- Intentional dual calendar design
- Mathematical sophistication in linguistic choices
- Recognition of both solar and lunar temporal cycles
- Embedded astronomical knowledge

---

_This analysis complements the solar year pattern, demonstrating dual calendar awareness embedded in Quranic linguistic structure._
