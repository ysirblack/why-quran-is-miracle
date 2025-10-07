# Solar-Year Notes – Honest State of the Day/Month Counts

## What Still Holds

- **365 singular days**: Verified via `day_365_verifier.py`, using the same “≤ 5 characters”
  YEVM rule adopted in the Hijri scripts.
- **12 singular months**: Verified via `days_month_verified.py`, counting only `شهر` /
  `ٱلشهر` tokens and excluding plurals/dual.

These totals remain unchanged and reproducible.

## About the Former “30-Day” Claim

- Verse **2:8** (`وَبِٱلْيَوْمِ ٱلْـَٔاخِرِ`) contains a distinctive “Last Day” spelling,
  but two dozen other verses deploy the same phrase with different clitic attachment.
- Earlier scripts counted only that single occurrence to close the gap to 30, which is not
  a defensible linguistic rule.
- Plural/dual experiments now live in the Hijri materials; this folder no longer asserts a
  30-day result by default.

If you choose to define a new inclusion rule (e.g., “count every instance of اليوم الآخر”),
state it explicitly and cite the resulting count. The helper `days_token_inventory.py`
prints all qualifying verses (26 adjacent occurrences plus one non-adjacent example at 5:5).

## Scripts in This Folder

- `day_365_verifier.py` – confirms 274/75/16 breakdown and total of 365.
- `days_month_verified.py` – legacy runner that still applies the optional “Last Day”
  increment. Review the comment block before relying on its 30-day output.
- `days_token_inventory.py` – token frequency table for every form containing “يوم,” plus
  explicit lists of “اليوم الآخر” occurrences (26 adjacent, 1 non-adjacent).

## Recommended Next Steps

1. Document any additional theological rule (if desired) in code and prose.
2. Keep the 365/12 verification scripts as part of the solar package; they remain accurate
   and aligned with the Hijri methodology.
