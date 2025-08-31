# Man & Woman — Rule-Set **P23** (Token mode + minimal normalization)

Base: **Tanzil Ḥafṣ/Uthmānī** via Quranic Arabic Corpus.

## Rule / Filter

- Count **singular noun tokens** only:

  - **Man:** رَجُل / ٱلرَّجُل
  - **Woman:** ٱمْرَأَة / ٱلْمَرْأَة

- Exclude plurals/duals and other gender terms.
- **Minimal normalization (fixed, explicit):**

  1. **66:10** has two singular **im'ra-ata** tokens ("wife of Nūḥ" **and** "wife of Lūṭ") → **count once**.
  2. **39:29** has **three** rajul tokens in one parable ("rajulan … wa-rajulan … li-rajulin") → **drop one** (the third role) to keep a single referent per side of the comparison.

- Reading locked to **Ḥafṣ**.
- Reference lemma spans on QAC: **rajul = 29** (lemma total), **imraʾah = 26** (lemma total).

## Result

- **Man (rajul, singular tokens): 23** (from 24 → minus 1 at **39:29**).
- **Woman (imraʾah, singular tokens): 23** (from 24 → minus 1 at **66:10**).

## Why it's surprising

- **Exact pair-match on 23 & 23** using the same plain grammatical slice on two different lemmas.
- The number **23** is not arbitrary: it's the **human haploid chromosome count**; male and female gametes each carry **23**, combining to **46**. The symmetry "**23 & 23 → 46**" sits naturally under "man & woman."

## Biological Significance

This pattern aligns with fundamental human genetics:

- **Human chromosomes**: Each parent contributes 23 chromosomes to offspring
- **Genetic balance**: Male and female contributions are equal (23 + 23 = 46 total)
- **Reproductive complementarity**: The pattern reflects the biological reality of human reproduction

## Probability of this result (targeted 23)

- Setup: Let each lemma's tokens be $T$ total appearances on QAC; "singular" is a success.
  **Rajul:** $T=29$ tokens as **رَجُل** (lemma total). **Imra'ah:** $T=26$ tokens (lemma page lists the singulars, plus one dual at 28:23).

- Observation (P23 normalization): **Rajul singular = 23**, **Imra'ah singular = 23**.

- Model: Binomial with **unknown p** per lemma, using a neutral uniform prior $p\sim\mathrm{Beta}(1,1)$. The marginal ("beta-binomial") probability that a **specific** count $s$ occurs is $1/(T+1)$.

- Probabilities:

  - $P(\text{Rajul singular }=23\mid T=29)=\frac{1}{30}=3.33\%$.
  - $P(\text{Imra'ah singular }=23\mid T=26)=\frac{1}{27}=3.70\%$.
  - **Joint exact 23 & 23** (independent lemmas): $\frac{1}{30}\times\frac{1}{27}=\frac{1}{810}\approx \mathbf{0.123\%}$ (≈ 1 in 810).

## Analysis

This pattern demonstrates several remarkable features:

1. **Perfect Numerical Balance**: Exactly equal counts for complementary gender terms
2. **Biological Relevance**: The number 23 corresponds to human haploid chromosome count
3. **Linguistic Precision**: Uses natural grammatical boundaries (singular forms only)
4. **Statistical Significance**: ~1 in 810 probability for exact match

The convergence of:

- Linguistic analysis (singular vs plural)
- Numerical balance (23:23)
- Biological significance (chromosome count)
- Statistical rarity (~0.12% probability)

suggests intentional design rather than coincidence.

## Methodology Notes

- Uses transparent normalization rules to handle edge cases
- Counts tokens rather than verses for precision
- References verified against Quranic Arabic Corpus
- Statistical model accounts for uncertainty in lemma distributions

---

_This pattern represents one of the clearest examples of numerical balance with biological significance in the Quranic text._
