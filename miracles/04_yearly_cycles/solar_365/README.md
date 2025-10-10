# Solar-Year Pattern – 365 Days & 12 Months

This folder documents the solar-year alignment discovered in the Qur’anic vocabulary of
“day” and “month.” Two straightforward linguistic filters reproduce the familiar calendar
constants:

| Pattern               | Rule Summary                                                 | Count   |
| --------------------- | ------------------------------------------------------------ | ------- |
| **Days (singular)**   | `يوم` simple forms + `ٱليوم` definite forms + `يوماً` tanwīn | **365** |
| **Months (singular)** | Singular `شهر` / `ٱلشهر` only (no plurals or duals)          | **12**  |

## Day (365) Breakdown

- **274** simple forms (`يوم` with at most one attached letter after removing diacritics)
- **75** definite forms (`ٱليوم`, `الْيوم`, etc.)
- **16** tanwīn forms (`يوماً`)

These counts are reproduced by `day_365_verifier.py`, which mirrors the Hijri analysis by
allowing only one prefix or suffix modification on the base word.

## Month (12) Count

- Every singular mention of "month" (`شهر`, `ٱلشهر`) is included.
- Dual forms (`شهرين`) and plurals (`شهور`, `أشهر`) are excluded.
- Verified by `days_month_verified.py`, which prints the twelve verse references for easy
  inspection.

## Statistical Significance

### Bootstrap Resampling Analysis (Recommended)

The `bootstrap_probability_analysis.py` script in the parent folder tests whether these exact totals could occur by chance while preserving linguistic structure. Based on 100,000 trials:

| Pattern                             | Bootstrap Probability | Interpretation            |
| ----------------------------------- | --------------------- | ------------------------- |
| Solar 365 alone                     | ~4.3% (~1 in 23)      | Moderately common         |
| Solar 365 AND Hijri 354             | ~0.15% (~1 in 667)    | Notable                   |
| All three patterns (365 + 354 + 29) | ~0.04% (~1 in 2,500)  | Statistically significant |

The bootstrap method:

1. Resamples the 478 actual "day" tokens with replacement
2. Recategorizes them using the same grammatical rules
3. Checks if we get exactly 365 for solar, 354 for Hijri, and 29 for lunar
4. Repeats 100,000 times to estimate probability

This approach preserves the realistic distribution of grammatical forms (definite, possessive, plural, etc.) rather than assuming all token arrangements are equally likely.

### Combinatorial Analysis (Baseline Reference)

For comparison, `combined_probability_analysis.py` uses a uniform subset model (every subset of tokens equally likely):

- P(Solar 365) ≈ 1 in 1.285 × 10⁹⁴
- This is mathematically correct but linguistically unrealistic

**Recommendation**: Use the bootstrap probabilities when discussing statistical significance, as they better reflect how language actually works.

## Reading the Outputs

- Run `python miracles/04_yearly_cycles/solar_365/day_365_verifier.py` to see the 365-day
  totals alongside representative verse lists.
- Run `python miracles/04_yearly_cycles/solar_365/days_month_verified.py` to confirm the
  twelve singular-month references.

These scripts rely solely on the canonical Tanzil Ḥafṣ/Uthmānī text (`data/quran-uthmani.txt`)
and transparent token rules, making the solar-year pattern reproducible for any reader or
researcher.
