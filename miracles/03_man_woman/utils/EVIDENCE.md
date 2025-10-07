# Evidence: Man & Woman — 26:26 Perfect Balance

Counting singular references to "man" (rajul) and "woman" (imra'ah) throughout the Quran reveals a perfect numerical balance.

## What Exactly Is the Claim?

- **Man (rajul)**: 26 occurrences
- **Woman (imra'ah)**: 26 occurrences
- **Perfect 26:26 balance**
- Text standard: Tanzil Ḥafṣ/Uthmānī edition

## The Counting Method

- Count all singular tokens of 'رَجُل' (rajul) for man
- Count all singular tokens of 'ٱمْرَأَة/ٱمْرَأَت' (imra'ah) for woman
- Exclude plural/dual forms
- No adjustments or normalizations applied
- All occurrences counted as they appear in the text

## Reproduce It Yourself

1. Use Tanzil Ḥafṣ/Uthmānī text
2. Search for 'رَجُل' (rajul) - singular man
3. Search for 'ٱمْرَأَة' and 'ٱمْرَأَت' (imra'ah) - singular woman
4. Count all occurrences
5. Result: 26:26 perfect balance

## Statistical Analysis

**Probability**: ~1 in 9.1 (11.01%)

Using binomial distribution:

- Total tokens: 52 (26 + 26)
- Probability of exactly 26:26 split: P = C(52,26) × 0.5^52
- Result: 0.1101 or about 11%

**Interpretation**:

- Like flipping 52 coins and getting exactly 26 heads, 26 tails
- Moderately interesting, not extremely rare
- Similar to other balanced distributions in natural language

## Q&A

**Q: Is this adjusted or normalized?**  
A: No. These are raw counts from the text. Every occurrence is counted as it appears.

**Q: What about verses with multiple tokens?**  
A: All tokens are counted. For example:

- Verse 2:282 has 2 'man' tokens - both counted
- Verse 66:10 has 2 'woman' tokens - both counted

**Q: What's the probability?**  
A: ~1 in 9 (11%), based on binomial distribution. This is moderately interesting but not extraordinarily rare.

**Q: Is this related to human chromosomes (23)?**  
A: The count is 26, not 23. There is no demonstrated connection to chromosome numbers.

## Verification

- **Script**: `man_woman_honest_verification.py`
- **Data**: `data/quran-uthmani.txt`
- **Method**: Direct counting, no adjustments
- **Reproducible**: Yes, by anyone with the same data source

---

This pattern demonstrates balanced gender representation in the Quran's singular terminology for man and woman.
