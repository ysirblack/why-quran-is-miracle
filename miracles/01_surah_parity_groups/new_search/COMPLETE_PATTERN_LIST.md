# Complete Pattern List: 230 Patterns from "Simetrik Kitap: Kur'an"

## Summary

| Category            | Count   | p-value             | Action             |
| ------------------- | ------- | ------------------- | ------------------ |
| CAT-1 (Very Strong) | 1       | p < 0.01%           | ✅ Script + README |
| CAT-2 (Strong)      | ~4      | p < 1%              | ✅ Script + README |
| CAT-3 (Moderate)    | ~25     | p < 5%              | ⚠️ Test first      |
| CAT-4 (Weak)        | ~70     | p > 5%              | 📝 Document only   |
| CAT-5 (Very Weak)   | ~130    | Guaranteed/Expected | ❌ Skip            |
| **TOTAL**           | **230** |                     |                    |

---

## SECTION 1: BASIC PARITY (15 patterns)

| #   | Pattern (Turkish)                           | English                     | Category | Reason               |
| --- | ------------------------------------------- | --------------------------- | -------- | -------------------- |
| 1   | Âyet sayısı tek olan sûreler kümesi         | Odd verse count surahs      | CAT-5    | FIXED: 54            |
| 2   | Âyet sayısı çift olan sûreler kümesi        | Even verse count surahs     | CAT-5    | FIXED: 60            |
| 3   | Âyet sayısı tek + sıra numarası tek         | Odd-verse + Odd-position    | CAT-5    | EXPECTED: 27         |
| 4   | Âyet sayısı tek + sıra numarası çift        | Odd-verse + Even-position   | CAT-5    | EXPECTED: 27         |
| 5   | Âyet sayısı çift + sıra numarası tek        | Even-verse + Odd-position   | CAT-5    | EXPECTED: 30         |
| 6   | Âyet sayısı çift + sıra numarası çift       | Even-verse + Even-position  | CAT-5    | EXPECTED: 30         |
| 7   | Âyet sayısı ve sıra numarası türdeş olan    | Parity homogeneous          | CAT-5    | GUARANTEED: 57       |
| 8   | Sıra numarası ve âyet sayısı türdeş olan    | Same as above               | CAT-5    | DUPLICATE            |
| 9   | Sıra numarası ve âyet sayısı türdeş olmayan | Parity heterogeneous        | CAT-5    | GUARANTEED: 57       |
| 10  | Türdeş + ilk yarı                           | Homogeneous + first half    | CAT-5    | ARBITRARY            |
| 11  | Türdeş + ikinci yarı                        | Homogeneous + second half   | CAT-5    | ARBITRARY            |
| 12  | Türdeş olmayan + ilk yarı                   | Heterogeneous + first half  | CAT-5    | ARBITRARY            |
| 13  | Türdeş olmayan + ikinci yarı                | Heterogeneous + second half | CAT-5    | ARBITRARY            |
| 14  | Sıra + âyet toplamı tek                     | Odd sum                     | CAT-5    | = Heterogeneous = 57 |
| 15  | Sıra + âyet toplamı çift                    | Even sum                    | CAT-5    | = Homogeneous = 57   |

**Section 1 Summary: 15 patterns, ALL CAT-5 (skip)**

---

## SECTION 2: VERSES > POSITION (5 patterns)

| #   | Pattern                    | English            | Category | Reason                    |
| --- | -------------------------- | ------------------ | -------- | ------------------------- |
| 16  | Âyet > sıra olan sûreler   | Verses > Position  | CAT-5    | FIXED: 48                 |
| 17  | Farkı tek olanlar          | Difference is odd  | CAT-3    | Need test                 |
| 18  | Farkı çift olanlar         | Difference is even | CAT-3    | Need test                 |
| 19  | Sıra numarası tek olanlar  | Position is odd    | CAT-5    | FIXED once filter applied |
| 20  | Sıra numarası çift olanlar | Position is even   | CAT-5    | FIXED once filter applied |

**Section 2: 2 testable (CAT-3), 3 skip (CAT-5)**

---

## SECTION 3: VERSES < POSITION (5 patterns)

| #   | Pattern                    | English            | Category | Reason             |
| --- | -------------------------- | ------------------ | -------- | ------------------ |
| 21  | Âyet < sıra olan sûreler   | Verses < Position  | CAT-5    | COMPLEMENT: 66     |
| 22  | Farkı tek olanlar          | Difference is odd  | CAT-4    | Complement pattern |
| 23  | Farkı çift olanlar         | Difference is even | CAT-4    | Complement pattern |
| 24  | Sıra numarası tek olanlar  | Position is odd    | CAT-5    | FIXED              |
| 25  | Sıra numarası çift olanlar | Position is even   | CAT-5    | FIXED              |

**Section 3: 2 weak (CAT-4), 3 skip (CAT-5)**

---

## SECTION 4: PRIME NUMBERS (22 patterns)

| #   | Pattern                                     | English                          | Category | Reason                        |
| --- | ------------------------------------------- | -------------------------------- | -------- | ----------------------------- |
| 26  | Sıra × âyet çarpımı                         | Position × Verses product        | CAT-4    | Untested                      |
| 27  | Asal türdeş ve türdeş olmayan               | Prime homogeneous overview       | CAT-3    | Need test                     |
| 28  | Asal türdeş olan sûreler                    | Both prime or both not-prime     | CAT-3    | Need test                     |
| 29  | Asal türdeş olmayan sûreler                 | One prime, one not               | CAT-4    | Complement of above           |
| 30  | Her ikisi de asal                           | Both prime                       | CAT-5    | Fixed: 7 surahs               |
| 31  | Her ikisi de asal değil                     | Neither prime                    | CAT-5    | Fixed: 59 surahs              |
| 32  | Sıra asal, âyet asal değil                  | Position prime, verses not       | CAT-5    | Fixed: 23 surahs              |
| 33  | Sıra asal değil, âyet asal                  | Position not prime, verses prime | CAT-5    | Fixed: 25 surahs              |
| 34  | Asal türdeş + parity türdeş                 | Prime-homo + parity-homo         | CAT-4    | Cross-classification          |
| 35  | Asal türdeş + parity türdeş olmayan         | Prime-homo + parity-hetero       | CAT-4    | Cross-classification          |
| 36  | Asal türdeş olmayan + parity türdeş         | Prime-hetero + parity-homo       | CAT-4    | Cross-classification          |
| 37  | Asal türdeş olmayan + parity türdeş olmayan | Prime-hetero + parity-hetero     | CAT-4    | Cross-classification          |
| 38  | Asal türdeş + sıra tek + âyet tek           | Prime-homo + odd-odd             | CAT-5    | Sub-subset                    |
| 39  | Asal türdeş + sıra çift + âyet çift         | Prime-homo + even-even           | CAT-5    | Sub-subset                    |
| 40  | Asal türdeş + sıra tek + âyet çift          | Prime-homo + odd-even            | CAT-5    | Sub-subset                    |
| 41  | Asal türdeş + sıra çift + âyet tek          | Prime-homo + even-odd            | CAT-5    | Sub-subset                    |
| 42  | Asal türdeş olmayan + sıra tek + âyet tek   | Prime-hetero + odd-odd           | CAT-5    | Sub-subset                    |
| 43  | Asal türdeş olmayan + sıra çift + âyet çift | Prime-hetero + even-even         | CAT-5    | Sub-subset                    |
| 44  | Asal türdeş olmayan + sıra tek + âyet çift  | Prime-hetero + odd-even          | CAT-5    | Sub-subset                    |
| 45  | Asal türdeş olmayan + sıra çift + âyet tek  | Prime-hetero + even-odd          | CAT-5    | Sub-subset                    |

**Section 4: 6 testable (CAT-3), rest weak/skip (CAT-4/5)**

---

## SECTION 5: SET OPERATIONS (23 patterns)

| #     | Pattern                                     | English                         | Category | Reason           |
| ----- | ------------------------------------------- | ------------------------------- | -------- | ---------------- |
| 46    | Sıra numaraları kümesi                      | Set of position numbers         | CAT-5    | Definition only  |
| 47    | Âyet sayıları kümesi                        | Set of verse counts             | CAT-5    | Definition only  |
| 48    | Tek sıra numaraları kümesi                  | Odd positions set               | CAT-5    | Definition       |
| 49    | Tek âyet sayıları kümesi                    | Odd verse counts set            | CAT-5    | Definition       |
| 50    | Tek sıra ∩ tek âyet                         | Odd positions ∩ Odd verses      | CAT-4    | Set intersection |
| 51    | Çift sıra numaraları kümesi                 | Even positions set              | CAT-5    | Definition       |
| 52    | Çift âyet sayıları kümesi                   | Even verse counts set           | CAT-5    | Definition       |
| 53    | Çift sıra ∩ çift âyet                       | Even positions ∩ Even verses    | CAT-4    | Set intersection |
| 54    | Tek sıra — tek âyet                         | Odd positions − Odd verses      | CAT-4    | Set difference   |
| 55    | Çift sıra — çift âyet                       | Even positions − Even verses    | CAT-4    | Set difference   |
| 56    | Âyet sayıları sıra numaralarında bulunan    | Verse count exists in positions | CAT-3    | Novel            |
| 57    | Âyet sayıları sıra numaralarında bulunmayan | Verse count not in positions    | CAT-4    | Complement       |
| 58-67 | Various cross-classifications               | Combinations                    | CAT-4/5  | Sub-subsets      |

**Section 5: ~2 testable (CAT-3), rest weak/skip**

---

## SECTION 6: DIVISIBLE BY 2 NOT 3 (7 patterns)

| #     | Pattern                             | English               | Category | Reason                   |
| ----- | ----------------------------------- | --------------------- | -------- | ------------------------ |
| 68    | İkiye bölünen üçe bölünmeyen türdeş | Div2-not3 homogeneous | CAT-4    | Arbitrary classification |
| 69-73 | First/second half combinations      | Sub-patterns          | CAT-5    | Arbitrary                |

**Section 6: 1 weak (CAT-4), 6 skip (CAT-5)**

---

## SECTION 7: DIVISIBLE BY 3 NOT 2 (7 patterns)

| #     | Pattern                             | English               | Category | Reason                   |
| ----- | ----------------------------------- | --------------------- | -------- | ------------------------ |
| 74    | Üçe bölünen ikiye bölünmeyen türdeş | Div3-not2 homogeneous | CAT-4    | Arbitrary classification |
| 75-79 | First/second half combinations      | Sub-patterns          | CAT-5    | Arbitrary                |

**Section 7: 1 weak (CAT-4), 6 skip (CAT-5)**

---

## SECTION 8: PRIME FACTOR SUM (17 patterns)

| #     | Pattern                        | English                         | Category | Reason     |
| ----- | ------------------------------ | ------------------------------- | -------- | ---------- |
| 80    | Sıra Asal Çarpanlar Toplamları | Sum of prime factors (position) | CAT-3    | Novel      |
| 81    | Âyet Asal Çarpanlar Toplamları | Sum of prime factors (verses)   | CAT-3    | Novel      |
| 82    | a₀(âyet) tek                   | Prime factor sum is odd         | CAT-3    | Novel      |
| 83    | a₀(sıra) tek                   | Prime factor sum is odd         | CAT-3    | Novel      |
| 84    | a₀(âyet) çift                  | Prime factor sum is even        | CAT-4    | Complement |
| 85    | a₀(sıra) çift                  | Prime factor sum is even        | CAT-4    | Complement |
| 86    | a₀(âyet) asal                  | Prime factor sum is prime       | CAT-3    | Novel      |
| 87-95 | First/second half combinations | Sub-patterns                    | CAT-4/5  | Arbitrary  |

**Section 8: 5 testable (CAT-3), rest weak/skip**

---

## SECTION 9: PERFECT NUMBERS (13 patterns)

| #       | Pattern                       | English                    | Category  | Reason                   |
| ------- | ----------------------------- | -------------------------- | --------- | ------------------------ |
| 96      | Âyet sayısı mükemmel          | Perfect number verse count | CAT-2     | Very rare: only 6, 28    |
| 97      | Mükemmel + sıra tek           | Perfect + odd position     | CAT-3     | Sub-pattern              |
| 98      | Mükemmel + sıra çift          | Perfect + even position    | CAT-3     | Sub-pattern              |
| 99      | Mükemmel olmayan              | Not perfect                | CAT-5     | Almost all (complement)  |
| 100-101 | Not perfect + position parity | Sub-patterns               | CAT-5     | Skip                     |
| 102     | Mükemmel türdeş               | Perfect homogeneous        | CAT-2     | Need test                |
| 103-107 | Cross-classifications         | Sub-patterns               | CAT-4     | Sub-subsets              |

**Section 9: 2 strong (CAT-2), 2 moderate (CAT-3), rest skip**

---

## SECTION 10: ABUNDANT NUMBERS (8 patterns)

| #       | Pattern            | English              | Category | Reason                |
| ------- | ------------------ | -------------------- | -------- | --------------------- |
| 108     | Âyet sayısı zengin | Abundant verse count | CAT-4    | ~25% of numbers       |
| 109-115 | Sub-patterns       | Combinations         | CAT-4/5  | Common classification |

**Section 10: All CAT-4/5 (abundant numbers are common)**

---

## SECTION 11: DEFICIENT NUMBERS (9 patterns)

| #       | Pattern         | English               | Category | Reason          |
| ------- | --------------- | --------------------- | -------- | --------------- |
| 116     | Âyet sayısı kıt | Deficient verse count | CAT-4    | ~75% of numbers |
| 117-123 | Sub-patterns    | Combinations          | CAT-4/5  | Very common     |

**Section 11: All CAT-4/5 (deficient numbers are very common)**

---

## SECTION 12: ARITHMETIC MEAN (12 patterns)

| #       | Pattern               | English       | Category | Reason              |
| ------- | --------------------- | ------------- | -------- | ------------------- |
| 124     | Ortalamanın üstünde   | Above average | CAT-4    | Arbitrary threshold |
| 125     | Ortalamanın altında   | Below average | CAT-4    | Arbitrary threshold |
| 126-131 | Cross-classifications | Sub-patterns  | CAT-4/5  | Arbitrary           |

**Section 12: All CAT-4/5**

---

## SECTION 13: LONG/SHORT SURAHS (19 patterns)

| #       | Pattern            | English      | Category | Reason             |
| ------- | ------------------ | ------------ | -------- | ------------------ |
| 132     | Uzun sûreler (≥40) | Long surahs  | CAT-4    | p ≈ 13%            |
| 133     | Kısa sûreler (<40) | Short surahs | CAT-4    | Complement         |
| 134-147 | Sub-patterns       | Combinations | CAT-4/5  | Post-hoc threshold |

**Section 13: All CAT-4/5**

---

## SECTION 14: DIVISOR COUNT = 2 (9 patterns)

| #       | Pattern          | English                     | Category | Reason      |
| ------- | ---------------- | --------------------------- | -------- | ----------- |
| 148     | Bölen sayısı = 2 | Exactly 2 divisors (primes) | CAT-3    | Novel       |
| 149-155 | Sub-patterns     | Combinations                | CAT-4/5  | Sub-subsets |

**Section 14: 1 moderate (CAT-3), rest weak**

---

## SECTION 15: 6236 ANALYSIS (3 patterns)

| #   | Pattern      | English          | Category | Reason            |
| --- | ------------ | ---------------- | -------- | ----------------- |
| 156 | 6236 section | 6236 properties  | CAT-3    | Specific to Quran |
| 157 | 6236 benzeri | Similar to 6236  | CAT-3    | Need details      |
| 158 | 6236 konumu  | Position of 6236 | CAT-3    | Need details      |

**Section 15: All CAT-3 (need to see specific claims)**

---

## SECTION 16: GOLDEN RATIO (5 patterns)

| #   | Pattern                     | English           | Category | Reason        |
| --- | --------------------------- | ----------------- | -------- | ------------- |
| 159 | Altın Oran                  | Golden ratio      | CAT-3    | Popular claim |
| 160 | Sıra + âyet toplamı dizisi  | Sum sequence      | CAT-4    | Need details  |
| 161 | Toplamları mükerrer         | Repeated sums     | CAT-4    | Need details  |
| 162 | Toplamları mükerrer olmayan | Non-repeated sums | CAT-4    | Complement    |

**Section 16: 1 moderate (CAT-3), rest weak**

---

## SECTION 17: 2 PRIME DIVISORS (9 patterns)

| #       | Pattern        | English                  | Category | Reason               |
| ------- | -------------- | ------------------------ | -------- | -------------------- |
| 163     | İki asal bölen | Exactly 2 prime divisors | CAT-4    | Many numbers qualify |
| 164-169 | Sub-patterns   | Combinations             | CAT-4/5  | Sub-subsets          |

**Section 17: All CAT-4/5**

---

## SECTION 18: 3 PRIME DIVISORS (9 patterns)

| #       | Pattern       | English                  | Category | Reason               |
| ------- | ------------- | ------------------------ | -------- | -------------------- |
| 170     | Üç asal bölen | Exactly 3 prime divisors | CAT-4    | Many numbers qualify |
| 171-176 | Sub-patterns  | Combinations             | CAT-4/5  | Sub-subsets          |

**Section 18: All CAT-4/5**

---

## SECTION 19: 19-BLOCK PATTERNS (45 patterns)

| #       | Pattern                     | English                      | Category  | Reason           |
| ------- | --------------------------- | ---------------------------- | --------- | ---------------- |
| 177-182 | Tekler ve çiftler per block | Odd/even counts per 19-block | CAT-3     | Part of symphony |
| 183-188 | Odd-odd per block           | [6,5,4,1,4,7]                | **CAT-1** | Part of symphony |
| 189-194 | Even-odd per block          | [4,3,8,3,4,5]                | **CAT-1** | Part of symphony |
| 195-200 | Even-even per block         | [5,7,1,7,5,5]                | **CAT-1** | Part of symphony |
| 201-206 | Odd-even per block          | [4,4,6,8,6,2]                | **CAT-1** | Part of symphony |
| 207-212 | Homogeneous per block       | [11,12,5,8,9,12]             | **CAT-1** | Part of symphony |
| 213-218 | Heterogeneous per block     | [8,7,14,11,10,7]             | **CAT-1** | Part of symphony |

**Section 19: Combined as ONE CAT-1 pattern (Six-Block Symphony)**

---

## FINAL COUNT BY CATEGORY

| Category  | Patterns                 | % of Total |
| --------- | ------------------------ | ---------- |
| **CAT-1** | 1 (with 42 sub-patterns) | 0.4%       |
| **CAT-2** | 4                        | 1.7%       |
| **CAT-3** | 25                       | 10.9%      |
| **CAT-4** | 70                       | 30.4%      |
| **CAT-5** | 130                      | 56.5%      |
| **TOTAL** | **230**                  | **100%**   |

---

## SCRIPTS TO CREATE (Priority Order)

| Priority | Pattern                  | Category | Script Name                         |
| -------- | ------------------------ | -------- | ----------------------------------- |
| 1        | Six-Block Symphony       | CAT-1    | `six_block_symphony.py` ✅ EXISTS   |
| 2        | Perfect Numbers          | CAT-2    | `perfect_numbers.py`                |
| 3        | Prime Homogeneous        | CAT-3    | `prime_homogeneous.py`              |
| 4        | Prime Factor Sum         | CAT-3    | `prime_factor_sum.py`               |
| 5        | 6236 Properties          | CAT-3    | `number_6236.py`                    |
| 6        | Golden Ratio             | CAT-3    | `golden_ratio.py`                   |
| 7        | Verse Count in Positions | CAT-3    | `verse_in_positions.py`             |
| 8        | Verses > Position Mirror | CAT-3    | `verse_greater_mirror.py` ✅ EXISTS |

---

## PATTERNS TO SKIP (138 total)

All CAT-5 patterns are skipped because they are:

- FIXED by data (counts determined by text)
- GUARANTEED by arithmetic (57/57 splits)
- ARBITRARY divisions (first/second half)
- COMPLEMENTS (always 114 - X)
- DUPLICATES (same pattern, different wording)

---

_Total patterns: 230_
_Worth testing: ~30 (CAT-1 through CAT-3)_
_Skip: ~200 (CAT-4 and CAT-5)_
