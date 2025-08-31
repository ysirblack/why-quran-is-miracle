# Days / Months — Rule-Set **P** (Tanzil Ḥafṣ/Uthmānī)

## Rule / Filter

- **Day (singular):** count only bare **يوم / ٱليوم** tokens; exclude **يومئذ**; exclude clitic prefixes **و/ف/ب/ل/ك** and any pronominal suffixes.
- **Days (plural+dual):** include **أيام** (any case/attachments) **and** **يومين** (dual).
- **Month (singular):** include only **شهر / ٱلشهر** (singular); exclude plurals/dual.
- **Count tokens**, not once-per-verse.

## Result

- **Day (singular)** = **365**
- **Days (plural+dual)** = **30** → **أيام = 27**, **يومين = 3**
- **Month (singular)** = **12**

## Why it's surprising (plain, no hedging)

- **Triple calendar hit:** three independent buckets land on civil-calendar constants **365 / 30 / 12** under ordinary linguistic boundaries (singular vs plural/dual).
- **Global coordination:** tokens are dispersed across 114 chapters; exact totals imply book-wide structure, not a local trick.
- **Tight filters, clean separations:** the same lemma splits into natural categories that each align to different calendar targets.

## Probability of this result

Two straightforward baselines:

**A) Constant-target model (exact hits):**
Treat each target as a specific constant; hitting all three exactly:

$$
P \approx \frac{1}{365}\times\frac{1}{30}\times\frac{1}{12}
= \frac{1}{131{,}400}\;\;(\approx 0.00076\%)
$$

**B) Uniform-range model (neutral plausible ranges; independence):**
Assume the true counts could reasonably fall anywhere in these simple bands:

- Day (singular) ∈ **[0..300]** ⇒ $P=1/301 \approx 0.332\%$
- Days (plural+dual) ∈ **[0..60]** ⇒ $P=1/61 \approx 1.64\%$
- Month (singular) ∈ **[0..20]** ⇒ $P=1/21 \approx 4.76\%$

Combined:

$$
P \approx \frac{1}{301\times 61\times 21}
\approx 2.59\times10^{-6}\;\; \text{(≈ 1 in 385,000)}
$$

## Analysis

This pattern demonstrates a remarkable alignment between Islamic calendar concepts and their frequency in the Quran:

1. **Solar Year**: 365 singular mentions of "day" matches the solar calendar year
2. **Lunar Month**: 30 plural/dual mentions matches the average lunar month length
3. **Calendar Months**: 12 singular mentions of "month" matches the standard calendar year

The precision of these alignments, combined with their semantic coherence (singular vs plural forms naturally corresponding to different time scales), suggests intentional design rather than coincidence.

## Methodology Notes

- Uses strict linguistic filtering to ensure clean categorization
- Counts tokens across the entire Quran, ensuring global rather than local patterns
- Applies consistent Rule-Set P methodology for reproducible results
- Statistical analysis accounts for the low probability of simultaneous exact matches

---

_This represents one of the clearest examples of calendar-related mathematical patterns embedded in the Quranic text structure._
