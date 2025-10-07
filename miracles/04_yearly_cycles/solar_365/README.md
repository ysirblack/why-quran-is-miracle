# Solar-Year Pattern – 365 Days & 12 Months

This folder documents the solar-year alignment discovered in the Qur’anic vocabulary of
“day” and “month.” Two straightforward linguistic filters reproduce the familiar calendar
constants:

| Pattern | Rule Summary | Count |
| ------- | ------------ | ----- |
| **Days (singular)** | `يوم` simple forms + `ٱليوم` definite forms + `يوماً` tanwīn | **365** |
| **Months (singular)** | Singular `شهر` / `ٱلشهر` only (no plurals or duals) | **12** |

## Day (365) Breakdown

- **274** simple forms (`يوم` with at most one attached letter after removing diacritics)
- **75** definite forms (`ٱليوم`, `الْيوم`, etc.)
- **16** tanwīn forms (`يوماً`)

These counts are reproduced by `day_365_verifier.py`, which mirrors the Hijri analysis by
allowing only one prefix or suffix modification on the base word.

## Month (12) Count

- Every singular mention of “month” (`شهر`, `ٱلشهر`) is included.
- Dual forms (`شهرين`) and plurals (`شهور`, `أشهر`) are excluded.
- Verified by `days_month_verified.py`, which prints the twelve verse references for easy
  inspection.

## Reading the Outputs

- Run `python miracles/04_yearly_cycles/solar_365/day_365_verifier.py` to see the 365-day
  totals alongside representative verse lists.
- Run `python miracles/04_yearly_cycles/solar_365/days_month_verified.py` to confirm the
  twelve singular-month references.

These scripts rely solely on the canonical Tanzil Ḥafṣ/Uthmānī text (`data/quran-uthmani.txt`)
and transparent token rules, making the solar-year pattern reproducible for any reader or
researcher.
