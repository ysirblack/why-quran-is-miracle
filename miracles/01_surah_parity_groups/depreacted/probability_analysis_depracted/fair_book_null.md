# Fair Book-like Null (Permutation)

A book-preserving baseline for Section 19 probabilities that honors the Qur’an’s verse histogram.

## Model

- Fix the multiset of the 114 observed verse counts
- Fix the label set {1..114}
- Randomize by uniform permutation of counts over labels
- Basmalah counted only in Al‑Fātiḥah (as in the data)

This breaks any structure between specific counts and labels while keeping the book‑level totals and histogram intact.

## What we test

- Parity–Sum core (57 even sums; even total = 6,236)
- 27/30 grid across order×āyāt parity
- 40‑threshold 57/57 split and its 27/30 long‑grid
- “Verses > order” mirror (48 total; 23/25 swap)

## Typical result scale

- Joint probability on the order of ~7.1 × 10⁻²¹ (from the paper’s reproduction) under conservative multiplication with dependency checks.

## Why include this null

- Keeps the actual distribution of verse lengths
- Tests whether observed structure needs more than the histogram to arise
- Complements full‑blind generative models

---

See also: Clean Probability Bundle, Two Honest Nulls.
