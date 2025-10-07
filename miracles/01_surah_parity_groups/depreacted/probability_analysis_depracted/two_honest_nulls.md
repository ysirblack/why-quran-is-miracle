# Two Honest Nulls

A fair probability framing for Section 19 results using two complementary null models.

## Null A — Permutation (book‑preserving)

- Fix the 114 observed verse counts (multiset) and the labels 1..114
- Randomize by uniformly permuting the counts over the labels
- Preserves the Qur’an’s verse histogram and total; breaks structure among labels

Use cases:

- Fair “book‑like” baseline honoring the actual distribution
- Good for assessing label‑structure claims

## Null B — Generative i.i.d. (full‑blind)

- Treat each sūrah’s verse count as an independent draw from a simple prior
- Baselines: Uniform[1..286] and a wider Uniform[1..600]
- Does not use the internal histogram; tests against a simple outside view

Use cases:

- Full‑blind plausibility check without book histogram
- Sensitivity testing across different prior supports

## Communication notes

- Present both nulls to avoid cherry‑picking
- Report joint probabilities with attention to dependencies
- Keep formulas and reproduced numbers available for auditing

---

See also: Clean Probability Bundle, Fair Book‑like Null.
