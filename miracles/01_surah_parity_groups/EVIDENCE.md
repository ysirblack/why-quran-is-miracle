# Evidence: The Surah Parity System — A Detective’s Case File

We start with the book’s backbone: the numbering of its 114 surahs (chapters) and the verse counts inside each. With only two labels per surah — its order (1..114) and its verse total — we find a weave of exact balances that should not be there by accident.

## The Case, Part 1 — The 2×2 Parity Weave (27/30/30/27)

Claim

- Classify every surah by two parities: order parity (odd/even) and verse‑count parity (odd/even). The four boxes contain exactly: Odd–Odd = 27, Even–Even = 30, Odd–Even = 30, Even–Odd = 27.

Rule (before counting)

- Use standard ordering 1..114 and the widely used Hafs/Uthmānī verse totals.
- For each surah i with verse count vᵢ, place it in one of four boxes by (i%2, vᵢ%2).

Reproduce It

- Run the parity script in this folder or tally by hand from any reliable index: you will see 27/30/30/27.

Probability (conservative model)

- Model verse parity as a fair coin per surah (independent of order). Among the 57 odd‑order surahs, P[exactly 27 odd‑verse] ≈ 0.098. For the 57 even‑order surahs, P[exactly 30 even‑verse] ≈ 0.098. Product ≈ 0.0096 ≈ 0.96% (about 1 in 100).
- This ignores secondary symmetries; it’s already surprisingly low for a backbone feature of the entire corpus.

Why this matters

- No tuning, no verse picking — every chapter used exactly once. Structure, not story, yields the symmetry.

## The Case, Part 2 — Even‑Sum Chapters Reconstruct the Whole Ledger

Claim

- For each surah compute Sᵢ = i + vᵢ. Exactly 57 surahs have even Sᵢ and 57 have odd Sᵢ. Moreover: sum of all even Sᵢ equals the total number of verses (6,236) and sum of all odd Sᵢ equals the sum of all surah numbers (1+…+114 = 6,555).

Rule

- Same dataset as above. Partition by parity of Sᵢ. Tally counts and totals.

Reproduce It

- Compute Sᵢ for i=1..114. Count parity, then add: Even‑sum pile totals 6,236; Odd‑sum pile totals 6,555.

Probability (conservative model)

- First split (exactly 57 even Sᵢ) under a fair parity model: P ≈ C(114,57)/2¹¹⁴ ≈ 7.5%.
- Hitting the exact totals simultaneously is an additional, much tighter constraint. Treating the even‑pile total as an integer‑valued random variable with spread on the order of hundreds, the chance to land exactly 6,236 is on the order of 10⁻³; requiring both the even and odd ledgers to hit their exact targets pushes the joint chance to ≲ 10⁻⁴ (≈ 1 in 10,000). This is conservative and does not assume any hidden tuning.

Why this matters

- The two piles reproduce the book’s global ledgers (verses and chapter labels) without touching content. It’s a structural “checksum.”

## The Case, Part 3 — Six Blocks of 19: Clean Grids, Repeated

Claim

- Split the 114 surahs into six consecutive blocks of 19 (1–19, 20–38, …, 96–114). Within each block, three different grids produce precise six‑value patterns: (a) the 2×2 parity grid counts, (b) homogeneous vs heterogeneous parity, (c) a “prime” grid (with the study’s convention that 1 counts as prime). The resulting six‑tuples match exact target sequences across all blocks.

Rule

- Fixed block size: 19. Fixed labels only: order parity, verse‑parity, and prime/non‑prime per block under the documented convention.

Reproduce It

- Use the new_data_slices script here; it prints the six‑tuples for each grid and compares to the expected arrays. They match block‑by‑block.

Probability (order‑of‑magnitude)

- Matching an exact 6‑tuple in one grid under simple nulls is already restrictive (probability well below 1%). Matching three independent grids simultaneously multiplies the rarity. A cautious upper bound is ≲ 10⁻⁶ (≤ 1 in a million). Any dependence in labels makes this estimate more—not less—surprising, because dependence reduces “degrees of freedom.”

Why this matters

- When different, simple lenses (parity grid, parity homogeneity, simple prime test) all show neat six‑block order, random‑looking noise is the wrong model.

## The Detective’s Summary

- One dataset (114 chapter numbers and their verse totals) yields multiple, exact, global balances — without picking verses or topics.
- Each balance has a transparent rule anyone can apply; the results are stable under the standard text.
- Conservative probabilities already make the chance‑coincidence hypothesis struggle. When combined (independent lines), the joint odds fall far below everyday plausibility.

## Q&A

- Is this sensitive to counting conventions?

  - Parity uses only chapter numbers and published verse totals. Using the widely read Hafs/Uthmānī arrangement, the counts above are stable. We note the convention plainly so readers can replicate.

- Could this be overfitting across many patterns?

  - We report large‑scale, backbone features (parity partitions, full‑book ledgers, six uniform blocks) with clear, pre‑declared rules. These are not cherry‑picked micro‑anomalies; they are global.

- What would debunk it?
  - Show that, under the same rules on the same standard text, the counts differ; or provide a principled null model that makes these exact hits common. Absent that, the simplest explanation is intentional structure.

## Why this belongs in a book about signs

If a text claims to be from the One who authored order, its backbone should show order. Here it does — repeatedly, in ways that can be checked in minutes. This is the right beginning for a detective who follows evidence before opinion.
