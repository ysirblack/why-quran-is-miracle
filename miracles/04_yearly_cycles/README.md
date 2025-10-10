# Yearly Cycles Miracle – Solar & Hijri Alignment

The Qur’an’s use of the root **يوم (yawm / “day”)** maps perfectly onto both the solar year
and the Hijri lunar year. The patterns below are fully reproducible from the canonical
Tanzil Ḥafṣ/Uthmānī text and can be shown to any audience in minutes.

## Four Calendar Signatures

| Calendar constant         | Qur’anic rule                                                                      | Count   | Quick verifier                     |
| ------------------------- | ---------------------------------------------------------------------------------- | ------- | ---------------------------------- |
| **365 solar days**        | Simple `يوم` (≤ 5 chars) + definite `اليوم` + tanwīn `يوماً`                       | **365** | `solar_365/day_365_verifier.py`    |
| **12 calendar months**    | Singular `شهر` / `ٱلشهر` (dual/plural excluded)                                    | **12**  | `solar_365/days_month_verified.py` |
| **354 Hijri days**        | Simple `يوم` + `يومئذ` (“that day”) + `يومهم` (“their day”) + `يومكم` (“your day”) | **354** | `hijri_354/hijri_354_combined.py`  |
| **29 Hijri month length** | Plural `أيام` + dual `يومين`                                                       | **29**  | `hijri_354/days_29_verifier.py`    |

Each script prints the total and example verses. No manual tweaking—just computed counts
from the full 6,236 verses.

## How Rare Is This?

We provide two statistical approaches:

### 1. Combinatorial Analysis (Uniform Subset Model)

`combined_probability_analysis.py` assumes every subset of the 478 `يوم` tokens is equally likely:

| Pattern                   | Probability  | Approximate odds     |
| ------------------------- | ------------ | -------------------- |
| Solar 365-day composition | `7.780e-95`  | ≈ 1 in 1.285 × 10⁹⁴  |
| Hijri 354-day composition | `2.348e-101` | ≈ 1 in 4.259 × 10¹⁰⁰ |
| Lunar 29 (plural + dual)  | `2.371e-46`  | ≈ 1 in 4.218 × 10⁴⁵  |
| Calendar months 12        | `7.938e-06`  | ≈ 1 in 1.260 × 10⁵   |

> **Note:** This model is mathematically correct but linguistically unrealistic. It treats all
> token selections as equally probable, which doesn't reflect how language works.

### 2. Bootstrap Resampling (Linguistically Realistic)

`bootstrap_probability_analysis.py` preserves linguistic structure by resampling actual tokens
and recategorizing them using grammatical rules. Based on 100,000 trials:

| Pattern                        | Bootstrap Probability | Approximate odds |
| ------------------------------ | --------------------- | ---------------- |
| Solar 365 alone                | ~4.3%                 | ~1 in 23         |
| Hijri 354 alone                | ~4.2%                 | ~1 in 24         |
| Lunar 29 alone                 | ~7.7%                 | ~1 in 13         |
| **Solar 365 AND Hijri 354**    | **~0.15%**            | **~1 in 667**    |
| **All three (365 + 354 + 29)** | **~0.04%**            | **~1 in 2,500**  |

> **Note:** This approach is more realistic because it:
>
> - Preserves the distribution of grammatical forms (definite, possessive, plural, etc.)
> - Tests whether the exact calendar totals could occur by chance
> - Doesn't assume all subsets are equally likely

The bootstrap analysis shows that while individual patterns are moderately common, the **simultaneous occurrence** of all three calendar alignments (solar year, lunar year, and lunar month) is statistically notable at approximately **1 in 2,500**.

## Sharing the Miracle

- `main.md` – one-page story of the solar and Hijri matches with direct links.
- `bootstrap_probability_analysis.py` – **recommended** realistic probability model (run with 100k trials).
- `combined_probability_analysis.py` – combinatorial baseline (mathematically correct but unrealistic).
- `solar_365/` & `hijri_354/` – verse lists, screenshots, and detailed notes ready to share.

With these resources you can walk anyone through the counts, the rule sets, and the
honest probabilities—showing how the Qur'an contains a notable pattern of calendar alignments.

## Quick Q&A

**Q1. How do I verify the 365-day count myself?**  
Run `python miracles/04_yearly_cycles/solar_365/day_365_verifier.py` to see the total and sample verses.

**Q2. Does the 365 rule include plural or possessive forms?**  
No—only simple `يوم`, definite `اليوم`, and tanwīn `يوماً`, each with light clitic attachment (≤ 5 characters after removing diacritics).

**Q3. Is the month count also automated?**  
Yes. `solar_365/days_month_verified.py` finds exactly 12 singular mentions of `شهر` / `ٱلشهر`; plurals and duals are excluded.

**Q4. What about the Hijri 354-day tally?**  
`hijri_354/hijri_354_combined.py` adds four categories—simple `يوم`, “that day” (`يومئذ`), “their day” (`يومهم`), and “your day” (`يومكم`)—for a total of 354.

**Q5. How is the 29-day Hijri month length counted?**  
`hijri_354/days_29_verifier.py` lists every plural `أيام` (26 occurrences) and dual `يومين` (3 occurrences) for a combined 29.

**Q6. What are the two probability models?**  
We provide two approaches:

1. `combined_probability_analysis.py` - Combinatorial model (mathematically correct but linguistically unrealistic)
2. `bootstrap_probability_analysis.py` - Bootstrap resampling (preserves linguistic structure, more realistic)

**Q7. Which probability should I quote?**  
Use the **bootstrap probabilities** (~1 in 2,500 for all three patterns) when sharing with others. The combinatorial model (10^245) is too unrealistic because it assumes all token arrangements are equally likely.

**Q8. How does bootstrap resampling work?**  
It resamples the 478 actual tokens with replacement, preserving their grammatical distribution, then recategorizes them and checks if we get the exact calendar totals. This tests whether the pattern is coincidental while respecting how Arabic grammar works.

**Q9. Can I see the verse references for each category?**  
All verifiers print sample verses; for complete lists, read the scripts or redirect their output to a file.

**Q10. Is any manual tweaking required to hit the totals?**  
No. The scripts operate on the full Tanzil dataset, applying fixed linguistic rules. Anyone can rerun them and get the same totals.
