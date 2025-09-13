# Appendix — Probabilities & Null Models (Planned Rigorous Estimates)

This appendix documents, for each evidence, the intended fair null model and how we will compute a rigorous p‑value (permutation/Monte Carlo), alongside the quick upper‑bound estimates already shown in the main dossier. The aim is transparency: define the game before rolling the dice.

Conventions

- Book‑preserving (permutation) null: keep the real verse‑length histogram or token inventory and randomize assignments consistent with the structure; recompute the statistic.
- Generative null: draw values from a simple distribution (e.g., Uniform ranges) to give an outside‑view bound; used for sensitivity only.
- Trials: target 1e5–1e6 per item for stable empirical p‑values with 95% confidence intervals.

## 1) Surah Parity System

- Quick: local binomial/grids + joint permutation: ~7.1 × 10⁻²¹ (see main text).
- Planned: reproduce the permutation bundle and publish code + seed for independent replication.

## 2) Solar 365 (singular day tokens)

- Quick: ≈ 1/1,400.
- Planned null: tokenize full corpus; preserve token counts per verse; randomly relabel day‑form categories under morphological constraints; ask P(total = 365 and bucket vector = 274/75/16). Report empirical p.

## 3) Hijri 354 (five day‑form categories)

- Quick: ≈ 1/1,700.
- Planned null: as above with five buckets, including the two agreed yevmiizin instances pre‑declared. Report empirical p.

## 4) Land vs Sea 71/29 (enhanced 32/45)

- Quick: ≈ 1/46.
- Planned null: treat reference set as fixed; test alternative principled sets (leave‑one‑out / add candidates) to bound p; also a hypergeometric exact hit on 32/45.

## 5) Man & Woman 25:25 (after normalization)

- Quick: ≈ 1/400 upper‑bound.
- Planned null: fix total M+W tokens; randomize allocation across verses with verse‑length stratification; adjust the two special verses; P(exact 25:25).

## 6) Adam & Jesus 25:25

- Quick: ≈ 1/1,600 upper‑bound.
- Planned null: as above for proper names only; P(exact 25:25) with stratification.

## 7) Sun 5778 (exclusive 2:258→91:1)

- Quick: ≈ 1/85,000.
- Planned null: permute verse order across 6,236 positions; count the exclusive gap between the fixed anchors; P(gap = 5,778).

## 8) Iron 1538 (inclusive 17:50→34:10)

- Quick: ≈ 1/8,300.
- Planned null: as above; P(gap = 1,538 inclusive).

## 9) Silver 962 (exclusive 3:14→9:35)

- Quick: ≈ 1/7,000.
- Planned null: as above; P(gap = 962 exclusive).

## 10) Earth→Sirius 86 words

- Quick: ≈ 1.6% (range‑based upper‑bound).
- Planned null: within Surah 53, randomize verse word boundaries or order under constraints; recompute token‑to‑token path; P(count = 86).

## 11) Sun–Sirius radius ratio (91/53)

- Quick: ≈ 0.59–0.90% by enumeration over all surah‑ratio pairs.
- Planned: publish the exact enumeration and band test against published measurements; sensitivity to alternative bands.

## 12) Surah 91 — 15 verses, uniform rhyme

- Quick: ≈ 0.022–0.070% (family‑frequency + verse count).
- Planned null: estimate -hā family frequency corpus‑wide; compute P(15 consecutive hits) × P(verse count = 15), cross‑check via bootstrap.

## 13) Rasul root total 513

- Quick: ≈ 1/300 (broad band bound).
- Planned null: keep token inventory; randomize root labels over surface tokens (diacritic‑stripped), preserving counts; P(total = 513) for ر‑س‑ل.

## 14) Carbon creation tracks (C=6, C‑12; bio spans)

- Quick: C‑12 track ~1e‑7 to 1e‑9; combined much lower.
- Planned null: permute verse order; recompute exact 12×k span hits for declared anchors; parallel tests for local 6‑spans and bio spans; product with Bonferroni correction.

## 15) Surah 57 iron signatures (26/57; verse 25/26)

- Quick: < 1/3,000 (combined conservative bound).
- Planned: enumerate Abjad possibilities under Arabic letters; P(حديد=26 and الحديد=57) × P(surah=57) × P(verse aligns), with sensitivity to local Basmalah counting.

## 16) Iron core 5,100th verse

- Quick: ≈ 1/6,236.
- Planned null: permute verse order; P(index 5,100 hit), also test thematic coherence co‑occurrence via keyword shuffles.

## 17) Moon landing 1389 AH

- Quick: ≈ 1/1,400 for exact year.
- Planned: uniform year mapping over 622–present; optional phase constraint to refine p.

## 18) Fertility Day 11 (1:1→2:222 singular days)

- Quick: ≈ 1/556.
- Planned null: tokenize, preserve verse lengths; random relabel singular/plural/dual under morphological constraints; P(count = 11).

## 19) Baltic 55°N, 19–20°E

- Quick: ≈ 1/64,800 (coarse grid).
- Planned: constrain to Baltic latitude/longitude band; P(exact 55 and 19–20) within the reduced space.

## 20) Camel 295 day‑tokens (6:144→81:4)

- Quick: ≈ 1/500.
- Planned null: as in calendars; P(exclusive span count ≈ 295) with specific exclusions.

## 21) “19” multi‑layer design (74:30 → Surah 82 → 82:19)

- Quick: ≲ 1/10,000.
- Planned: joint P(exact 19‑verse chapter) × P(unique “Allah” ending among ~6,236 verses), cross‑checked by corpus enumeration.

---

When ready, we will publish small, self‑contained Python scripts (deterministic seeds) and insert the empirical p‑values here, with confidence intervals and links to code. Until then, the quick bounds in the main dossier remain intentionally conservative.
