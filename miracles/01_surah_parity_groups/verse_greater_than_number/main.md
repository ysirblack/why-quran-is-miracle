# Surahs where **verses > sūrah number** — clear grouping & symmetry

**Filter first:** keep only sūrahs whose **number of verses is greater than their order number** (this yields **48** sūrahs total).

## Four groups (plain-English rules)

1. **Result is odd** — **23** sūrahs

   > Take the number of verses and **subtract** the sūrah's order.
   > If the **result is odd**, it goes here.

2. **Result is even** — **25** sūrahs

   > Same subtraction, but the **result is even**.

3. **Order is odd** — **25** sūrahs

   > From those 48, keep the ones whose **sūrah order is odd** (1st, 3rd, 5th, …).

4. **Order is even** — **23** sūrahs

   > From those 48, keep the ones whose **sūrah order is even** (2nd, 4th, 6th, …).

## The symmetry

- The two ways of slicing give **matching totals** in a neat swap:

  - "**result is odd**" (**23**) ↔ "**order is even**" (**23**)
  - "**result is even**" (**25**) ↔ "**order is odd**" (**25**)

- Either way you look at it, you split the same 48 sūrahs into **23 + 25**. Clean and easy to explain.

---

## Statistical Analysis

**Permutation Test (1,000,000 trials):**

**Pattern Components:**

1. **48 surahs filtered** (verses > number)

   - Probability: ~1 in 7.5 (13.3%)

2. **Swap pattern exists** (given 48 filtered)

   - Probability: ~1 in 10.8 (9.2%)

3. **Exact 23/25 split** (given swap)
   - Probability: ~1 in 5.4 (18.6%)

**Overall Result:**

- **All together: ~1 in 439 (0.23%)**
- **Test**: 1,000,000 trials, 2,276 matches

**Key Points:**

- Order parity split (25 odd, 23 even) is fixed by which surahs pass filter
- Randomness is in verse count assignments
- Classifications are independent under permutation

**Independence**: This pattern tests a filtered subset with different classification, independent from previous analyses.
