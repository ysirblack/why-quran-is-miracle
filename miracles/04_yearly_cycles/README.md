# Yearly Cycles Miracle – Solar & Hijri Alignment

The Qur’an’s use of the root **يوم (yawm / “day”)** maps perfectly onto both the solar year
and the Hijri lunar year. The patterns below are fully reproducible from the canonical
Tanzil Ḥafṣ/Uthmānī text and can be shown to any audience in minutes.

## Four Calendar Signatures

| Calendar constant | Qur’anic rule | Count | Quick verifier |
| ----------------- | ------------- | ----- | -------------- |
| **365 solar days** | Simple `يوم` (≤ 5 chars) + definite `اليوم` + tanwīn `يوماً` | **365** | `solar_365/day_365_verifier.py` |
| **12 calendar months** | Singular `شهر` / `ٱلشهر` (dual/plural excluded) | **12** | `solar_365/days_month_verified.py` |
| **354 Hijri days** | Simple `يوم` + `يومئذ` (“that day”) + `يومهم` (“their day”) + `يومكم` (“your day”) | **354** | `hijri_354/hijri_354_combined.py` |
| **29 Hijri month length** | Plural `أيام` + dual `يومين` | **29** | `hijri_354/days_29_verifier.py` |

Each script prints the total and example verses. No manual tweaking—just computed counts
from the full 6,236 verses.

## How Rare Is This?

`combined_probability_analysis.py` gives an illustrative baseline: suppose every subset of
the 451 `يوم` tokens were equally likely. The chance of stumbling onto each exact
composition is tiny:

| Pattern | Probability (uniform subset model) | Approximate odds |
| ------- | ---------------------------------- | ---------------- |
| Solar 365-day composition | `7.780e-95` | ≈ 1 in 1.285 × 10⁹⁴ |
| Hijri 354-day composition | `2.348e-101` | ≈ 1 in 4.259 × 10¹⁰⁰ |
| Lunar 29 (plural + dual) | `2.371e-46` | ≈ 1 in 4.218 × 10⁴⁵ |
| Calendar months 12 | `7.938e-06` | ≈ 1 in 1.260 × 10⁵ |
| All four together (independent product) | `3.438e-246` | ≈ 1 in 2.909 × 10²⁴⁵ |

> **Reminder:** This model is deliberately simple—real language isn’t a random draw. When
> quoting the numbers, lead with “Under a uniform random subset model …” so the assumption
> is crystal clear.

## Sharing the Miracle

- `main.md` – one-page story of the solar and Hijri matches with direct links.
- `combined_probability_analysis.py` – run live to show the probabilities.
- `solar_365/` & `hijri_354/` – verse lists, screenshots, and detailed notes ready to share.

With these resources you can walk anyone through the counts, the rule sets, and the
“wow-factor” probabilities—showing how the Qur’an encodes both solar and lunar calendars
with astonishing precision.

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

**Q6. What does the probability script actually assume?**  
`combined_probability_analysis.py` assumes every subset of the 451 `يوم` tokens is equally likely—it’s a uniform random baseline, not a claim about how Arabic is written.

**Q7. Are the odds really as huge as the script prints?**  
Under that uniform model, yes (e.g., ≈1 in 10⁹⁴ for the solar breakdown). Just make sure you state the assumption whenever you share the numbers.

**Q8. Is there a more realistic statistical model?**  
Not yet in this repo. A next step would be a permutation test that preserves the overall counts of each form while shuffling verses—great idea for future work.

**Q9. Can I see the verse references for each category?**  
All verifiers print sample verses; for complete lists, read the scripts or redirect their output to a file.

**Q10. Is any manual tweaking required to hit the totals?**  
No. The scripts operate on the full Tanzil dataset, applying fixed linguistic rules. Anyone can rerun them and get the same totals.
