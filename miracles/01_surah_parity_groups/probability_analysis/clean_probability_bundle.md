# Clean Probability Bundle (full‑blind i.i.d.)

Goal: quantify the joint probability of the Section 19 parity signals under a full‑blind generative model that does not use the Qur’an’s internal verse histogram.

## Model

- i.i.d. counts: each sūrah’s āyāt is an independent draw
- Baselines used:
  - Uniform[1..286]
  - Wider‑scope sensitivity: Uniform[1..600]
- Labels 1..114 are fixed; only verse counts are random.

## Events bundled

- P1: Parity–Sum core (57 even sums; even‑group total = 6,236)
- P1‑grid: 27/30 parity grid across order×āyāt
- P2: 40‑threshold split → 57 long (≥40) and 57 short (≤39)
- P2‑grid: long (≥40) split 27/30 by order parity
- P3: Revelation‑order exclusion (muṣḥaf hits, revelation does not)
- P4: “verses > order” mirror (48 total; internal 23/25 swap)

## Results (back‑of‑envelope)

- Uniform[1..286] → ~4.1 × 10⁻⁶⁶
- Uniform[1..600] → ~2.7 × 10⁻¹³⁹

These reflect multiplicative aggregation with conservative handling to avoid double‑counting dependencies.

## Notes

- Independence and identical marginals are assumptions of this model
- Serves as a full‑blind outside view (no use of the actual verse histogram)
- Complements the book‑preserving permutation null.

---

See also: Two Honest Nulls, Fair Book‑like Null.
