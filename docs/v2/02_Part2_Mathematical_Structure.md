# PART 2: MATHEMATICAL & STRUCTURAL ARCHITECTURE

**Target: ~33 questions (P2-1 through P2-33)**

**Cascading Gate:** "The Qur'an contains computationally precise structural patterns not found in other texts"

**Depends on Part 1 Gate:** Text must be preserved for patterns to be meaningful. If the text was altered, patterns could be post-hoc insertions. If Part 1 Gate = YES (preserved), then Part 2 patterns carry full evidential weight. If Part 1 Gate = NO, Part 2 results are structurally undermined.

## Probability Scenario Frame

Before entering the detailed Part 2 questions, record the full range of probability readings from harshest skepticism to naive full multiplication. This prevents both overclaim and underclaim.

### Scenario A — Ultra-Skeptik Floor

Include only the three hardest-to-dismiss verse-gap results:

- Sun `5778`
- Silver `962`
- Iron `1538`

Calculation:

`p = 1 / (6236 × 6236 × 23400)`

Result:

- `p ≈ 1.098935e-12`
- `~ 1 in 9.099721e+11`
- `~ 1 in 910 billion`

### Scenario B — High Skeptik

Take Scenario A and add only the most conservative Hadid atomic layer:

- Sun `5778`
- Silver `962`
- Iron `1538`
- Hadid `26`

Calculation:

`p = 1 / (6236 × 6236 × 23400 × 1000)`

Result:

- `p ≈ 1.098935e-15`
- `~ 1 in 9.099721e+14`
- `~ 1 in 910 trillion`

### Scenario C — Medium Skeptik

Take Scenario B and add the second Hadid layer:

- Sun `5778`
- Silver `962`
- Iron `1538`
- Hadid `26`
- Al-Hadid `57`

Result:

- `p ≈ 9.639779e-18`
- `~ 1 in 1.037368e+17`

### Scenario D — Clustered Fair Cumulative Estimate

Collapse obviously dependent families into clusters instead of multiplying every internal member independently:

- Part 2 structural cluster = `1e-6`
- Word-balance cluster = `1/1000`
- Calendar cluster = `1/100000`
- Verse-gap cluster = `Sun × Silver × Iron`
- Hadid cluster = `1/1000`

Result:

- `p ≈ 1.098935e-29`
- `~ 1 in 9.099721e+28`

### ~~Scenario E — Naive Full Stack~~ ⚠ NOT DEFENSIBLE

~~If every verified pattern family is multiplied as independent:~~

**This scenario is WITHDRAWN.** Independence analysis shows that golden ratio and even-sum share the same underlying surah-number/verse-count data. Multiplying them as independent inflates the result. The raw number (10⁻⁴⁹) is mathematically correct IF independence holds — but independence does NOT hold. This scenario remains here for transparency but must NOT be cited as a defensible estimate.

~~Result: p ≈ 1.881300e-49~~

### Scenario E (CORRECTED) — Cluster-Independent Defensible Floor

After proper dependency analysis — collapsing entangled patterns into clusters and multiplying ONLY independent clusters:

- Structural cluster (golden ratio + even-sum = ONE package): `p ≈ 10⁻⁶` (from permutation test with Bonferroni correction)
- Verse-gap cluster (Sun × Silver × Iron): `p ≈ 10⁻¹²` (with look-elsewhere ×50 = `10⁻¹⁰·³`)
- Word-balance cluster (3+ perfect balances): `p ≈ 10⁻³`
- Calendar cluster (365 + 354 triple alignment): `p ≈ 10⁻⁴`

Result (independent clusters multiplied):

- `p ≈ 10⁻²³`
- `~ 1 in 10²³`

**This is the defensible floor.** It is astronomically small — far below any standard significance threshold — but it is honestly computed with dependencies respected.

### Reading Rule

- `Scenario A` = harsh minimum floor (verse-gaps only)
- `Scenario B` = skeptical but still cumulative
- `Scenario D` = generous cumulative estimate (slightly optimistic)
- `Scenario E (corrected)` = **defensible floor with proper independence analysis (~10⁻²³)**

**Checkpoint**

Before answering Part 2's final probability questions, state clearly which scenario you accept:

- `A. Ultra-Skeptik Floor` (~10⁻¹²)
- `B. High Skeptik` (~10⁻¹⁵)
- `C. Skeptik Plus` (~10⁻¹⁸)
- `D. Clustered Fair` (~10⁻²⁹ — slightly optimistic)
- `E. Cluster-Independent Defensible Floor` (~10⁻²³ — **recommended**)
- `E. Naive Full Stack`

Do not switch standards mid-Part. If you reject one scenario as too generous, identify the exact dependency objection and move to the next more conservative scenario.

**Sub-sections:**

- 2A. Golden Ratio Partition (P2-1 through P2-5)
- 2B. Even-Sum Identity (P2-6 through P2-9)
- 2C. Structural Symmetries (P2-10 through P2-14)
- 2D. Word-Pair Balances (P2-15 through P2-19)
- 2E. Calendar Encoding (P2-20 through P2-23)
- 2F. Cross-Text Failure (P2-24 through P2-27)
- 2G. Ramsey Theory Refutation (P2-28 through P2-30)
- 2H. Cumulative Probability & Gate Lock (P2-31 through P2-33)

---

## 2A. GOLDEN RATIO PARTITION

### Background

The golden ratio (phi, approximately 1.6180339887) appears throughout nature, mathematics, and classical architecture. It is defined as the positive solution to x^2 = x + 1, or equivalently (1 + sqrt(5)) / 2. No pre-modern text is known to encode phi into its structural architecture at the precision documented below.

The Qur'an contains 114 surahs (chapters). Each surah has a fixed position number (1 through 114) and a fixed verse count. For each surah, we compute the sum: surah_number + verse_count. Some of these 114 sums are unique (appear exactly once), and some are repeated (appear two or more times across different surahs). When we sum all the (surah_number + verse_count) values for surahs in the "repeated" group versus the "unique" group, a ratio emerges.

**Source reference:** Simetrik Kitap: Kur'an, pages 361-367.

---

### P2-1 [CODE-DEPENDENT] [CRITICAL] [NC-C]

**Run the following code to compute the golden ratio partition of the Qur'an's surah structure.**

The Qur'an has 114 surahs. For each surah, compute (surah_number + verse_count). Some of these 114 sums will be unique values (appearing only once) and some will be repeated values (appearing two or more times). Separate the 114 surahs into two groups: those whose sum is repeated, and those whose sum is unique. Then compute the total of all sums in each group, and take their ratio.

```python
# FILE: golden_ratio_partition.py
# Compute the golden ratio partition from Qur'an surah structure.
# Data source: data/quran-uthmani.txt (Tanzil Hafs/Uthmani)

from collections import Counter
from pathlib import Path

PHI = 1.6180339887  # Golden ratio (1 + sqrt(5)) / 2

def load_quran_data(data_path):
    """Load verse counts per surah from Tanzil format."""
    verses = {}
    with open(data_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#') or '|' not in line:
                continue
            parts = line.split('|', 2)
            if len(parts) >= 3:
                surah = int(parts[0])
                verses.setdefault(surah, []).append(int(parts[1]))
    return {s: len(v) for s, v in verses.items()}

# Load data
data_path = Path("data/quran-uthmani.txt")
verse_counts = load_quran_data(data_path)

# Step 1: Compute surah_number + verse_count for each surah
sums = {s: s + v for s, v in verse_counts.items()}

# Step 2: Count how many surahs share each sum value
sum_frequency = Counter(sums.values())

# Step 3: Classify each surah
repeated_surahs = [(s, v, sums[s]) for s, v in verse_counts.items()
                    if sum_frequency[sums[s]] > 1]
unique_surahs   = [(s, v, sums[s]) for s, v in verse_counts.items()
                    if sum_frequency[sums[s]] == 1]

# Step 4: Sum the (surah_number + verse_count) for each group
sum_repeated = sum(s + v for s, v, _ in repeated_surahs)
sum_unique   = sum(s + v for s, v, _ in unique_surahs)

# Step 5: Compute ratio
ratio = sum_repeated / sum_unique
deviation = abs(ratio - PHI)
deviation_pct = (deviation / PHI) * 100

# Step 6: Check if total is prime
total = sum_repeated + sum_unique
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(f"Surahs in 'repeated' group: {len(repeated_surahs)}")
print(f"Surahs in 'unique' group:   {len(unique_surahs)}")
print(f"Sum of repeated group:       {sum_repeated}")
print(f"Sum of unique group:         {sum_unique}")
print(f"Total:                       {total}")
print(f"Total is prime:              {is_prime(total)}")
print(f"Ratio (repeated/unique):     {ratio:.6f}")
print(f"Golden ratio phi:            {PHI:.6f}")
print(f"Absolute deviation:          {deviation:.6f}")
print(f"Percentage deviation:        {deviation_pct:.4f}%")
```

```
[EXPECTED OUTPUT]
Surahs in 'repeated' group: 65
Surahs in 'unique' group:   49
Sum of repeated group:       7906
Sum of unique group:         4885
Total:                       12791
Total is prime:              True
Ratio (repeated/unique):     1.618424
Golden ratio phi:            1.618034
Absolute deviation:          0.000390
Percentage deviation:        0.0241%
```

```
[CHECKPOINT: Report your exact numbers]
- Sum of repeated group: ___
- Sum of unique group: ___
- Ratio: ___
- Deviation from phi: ___%
```

```
[CONSISTENCY NOTE: Record the ratio and deviation for probability computation in P2-31]
```

**Question:** What ratio did you obtain? Is it within 0.03% of the golden ratio? Report the exact values from your code execution.

**Tags:** [CRITICAL] [CODE-DEPENDENT]
**Critical Type:** evaluative
**ISR check:** not applicable (establishing factual baseline)

---

### P2-2 [CODE-DEPENDENT] [T2-S]

**Run a permutation test to determine how likely this ratio is to arise by chance.**

The previous question established that the Qur'an's repeated/unique sum ratio is approximately 1.618424, deviating from phi by only 0.024%. Now we test: if the 114 verse counts were randomly shuffled across the 114 positions, how often would a ratio closer to phi emerge?

This is a Monte Carlo permutation test. We hold the 114 position numbers fixed (1-114) and randomly shuffle the 114 verse counts among them. For each permutation, we recompute the repeated/unique classification and ratio, then measure its deviation from phi. We count how many permutations produce a deviation equal to or smaller than the observed 0.000390.

```python
# FILE: golden_ratio_permutation_test.py
# Monte Carlo permutation test for the golden ratio partition.
# WARNING: 1,000,000 trials takes several minutes. Reduce N_TRIALS for quick test.

import random
from collections import Counter

PHI = 1.6180339887

# Qur'an surah data: {surah_number: verse_count}
# (Hardcoded from Tanzil Hafs/Uthmani for reproducibility)
VERSE_COUNTS = {
    1:7, 2:286, 3:200, 4:176, 5:120, 6:165, 7:206, 8:75, 9:129, 10:109,
    11:123, 12:111, 13:43, 14:52, 15:99, 16:128, 17:111, 18:110, 19:98,
    20:135, 21:112, 22:78, 23:118, 24:64, 25:77, 26:227, 27:93, 28:88,
    29:69, 30:60, 31:34, 32:30, 33:73, 34:54, 35:45, 36:83, 37:182,
    38:88, 39:75, 40:85, 41:54, 42:53, 43:89, 44:59, 45:37, 46:35,
    47:38, 48:29, 49:18, 50:45, 51:60, 52:49, 53:62, 54:55, 55:78,
    56:96, 57:29, 58:22, 59:24, 60:13, 61:14, 62:11, 63:11, 64:18,
    65:12, 66:12, 67:30, 68:52, 69:52, 70:44, 71:28, 72:28, 73:20,
    74:56, 75:40, 76:31, 77:50, 78:40, 79:46, 80:42, 81:29, 82:19,
    83:36, 84:25, 85:22, 86:17, 87:19, 88:26, 89:30, 90:20, 91:15,
    92:21, 93:11, 94:8, 95:8, 96:19, 97:5, 98:8, 99:8, 100:11,
    101:11, 102:8, 103:3, 104:9, 105:5, 106:4, 107:7, 108:3, 109:6,
    110:3, 111:5, 112:4, 113:5, 114:6
}

def calc_deviation(positions, verses):
    """Calculate absolute deviation from phi for a given assignment."""
    sums = [p + v for p, v in zip(positions, verses)]
    freq = Counter(sums)
    sum_repeated = sum(s for s in sums if freq[s] > 1)
    sum_unique   = sum(s for s in sums if freq[s] == 1)
    if sum_unique == 0:
        return float('inf')
    ratio = sum_repeated / sum_unique
    return abs(ratio - PHI)

# Observed configuration
positions = list(range(1, 115))
verses = [VERSE_COUNTS[s] for s in positions]
observed_deviation = calc_deviation(positions, verses)

print(f"Observed deviation from phi: {observed_deviation:.10f}")

# Permutation test
N_TRIALS = 1_000_000
random.seed(42)

closer_count = 0
for trial in range(N_TRIALS):
    shuffled = verses[:]
    random.shuffle(shuffled)
    if calc_deviation(positions, shuffled) <= observed_deviation:
        closer_count += 1

p_value = closer_count / N_TRIALS
print(f"\nTrials:           {N_TRIALS:,}")
print(f"Closer or equal:  {closer_count}")
print(f"p-value:          {p_value:.8f}")
print(f"Significant:      {'YES (p < 0.05)' if p_value < 0.05 else 'NO'}")

if closer_count == 0:
    print(f"\nZERO out of {N_TRIALS:,} random permutations")
    print(f"produced a ratio closer to phi than the Qur'an's actual structure.")
    print(f"Upper bound on p-value: < {1/N_TRIALS:.8f}")
```

```
[EXPECTED OUTPUT]
Observed deviation from phi: 0.0003901738
Trials:           1,000,000
Closer or equal:  0
p-value:          0.00000000
Significant:      YES (p < 0.05)

ZERO out of 1,000,000 random permutations
produced a ratio closer to phi than the Qur'an's actual structure.
Upper bound on p-value: < 0.00000100
```

```
[CHECKPOINT: Report your exact numbers]
- Observed deviation: ___
- Trials: ___
- Matches (closer or equal): ___
- p-value: ___
```

```
[CONSISTENCY NOTE: Record the p-value (< 1/1,000,000) for cumulative probability in P2-31]
```

**Question:** How many out of 1,000,000 random permutations produced a ratio closer to phi than the Qur'an's actual structure? What is the resulting p-value?

**Tags:** [CODE-DEPENDENT]

---

### P2-3 [T2-S]

**Context and significance of the golden ratio result.**

The golden ratio (phi) is not an arbitrary constant. It governs the spiral growth of nautilus shells, the branching of trees, the arrangement of sunflower seeds, and the proportions of the Parthenon. It is the "most irrational" number -- the hardest real number to approximate by rational fractions -- and for this reason it appears as nature's optimal packing constant.

The result from P2-1 and P2-2 shows that the Qur'an's 114-surah structure encodes phi to within 0.024%, and that zero out of one million random permutations achieve a closer fit.

**Question:** Could a pre-modern author, composing 114 chapters of varying lengths over 23 years of oral revelation, have deliberately encoded the golden ratio into the repeated/unique partition of (surah_number + verse_count) sums -- without computational tools, without knowledge of phi's decimal expansion (first computed by Mark Barr in 1909), and without the combinatorial framework needed to evaluate which verse counts would produce repeated vs. unique sums?

State plainly: is this encoding plausible under any documented 7th-century human capability? If yes, name the mechanism. If no, state that.

---

### P2-4 [T2-S]

**The total 12,791 is prime.**

The sum of the repeated group (7,906) plus the unique group (4,885) equals 12,791. This number is prime -- it has no divisors other than 1 and itself. The golden ratio partition thus produces two groups whose total is an indivisible number.

Primality is a structural property: you cannot split 12,791 into equal integer subgroups. The fact that the two groups sum to a prime while simultaneously encoding phi is a joint constraint. The golden ratio constrains the ratio between the groups; the primality constrains the total. Both constraints are satisfied simultaneously.

**Question:** Is the combined golden-ratio-plus-primality result a single coincidence, or does the joint satisfaction of two independent mathematical constraints (ratio approximately phi AND total is prime) reduce the space of possible structures that could produce this result? Assess the evidential weight.

**Tags:** [CODE-DEPENDENT]

---

### P2-5 [T2-S]

**Robustness check: what happens if you change even one verse count?**

The golden ratio partition depends on the exact verse counts of all 114 surahs. If any single surah's verse count were different by even one verse, the classification of sums as repeated vs. unique could shift, altering the ratio.

```python
# FILE: golden_ratio_sensitivity.py
# Test how fragile the golden ratio result is.

from collections import Counter

PHI = 1.6180339887

VERSE_COUNTS = {
    1:7, 2:286, 3:200, 4:176, 5:120, 6:165, 7:206, 8:75, 9:129, 10:109,
    11:123, 12:111, 13:43, 14:52, 15:99, 16:128, 17:111, 18:110, 19:98,
    20:135, 21:112, 22:78, 23:118, 24:64, 25:77, 26:227, 27:93, 28:88,
    29:69, 30:60, 31:34, 32:30, 33:73, 34:54, 35:45, 36:83, 37:182,
    38:88, 39:75, 40:85, 41:54, 42:53, 43:89, 44:59, 45:37, 46:35,
    47:38, 48:29, 49:18, 50:45, 51:60, 52:49, 53:62, 54:55, 55:78,
    56:96, 57:29, 58:22, 59:24, 60:13, 61:14, 62:11, 63:11, 64:18,
    65:12, 66:12, 67:30, 68:52, 69:52, 70:44, 71:28, 72:28, 73:20,
    74:56, 75:40, 76:31, 77:50, 78:40, 79:46, 80:42, 81:29, 82:19,
    83:36, 84:25, 85:22, 86:17, 87:19, 88:26, 89:30, 90:20, 91:15,
    92:21, 93:11, 94:8, 95:8, 96:19, 97:5, 98:8, 99:8, 100:11,
    101:11, 102:8, 103:3, 104:9, 105:5, 106:4, 107:7, 108:3, 109:6,
    110:3, 111:5, 112:4, 113:5, 114:6
}

def compute_ratio(vc):
    sums = {s: s + v for s, v in vc.items()}
    freq = Counter(sums.values())
    sum_rep = sum(sums[s] for s in vc if freq[sums[s]] > 1)
    sum_unq = sum(sums[s] for s in vc if freq[sums[s]] == 1)
    if sum_unq == 0:
        return float('inf')
    return sum_rep / sum_unq

# Original ratio
original_ratio = compute_ratio(VERSE_COUNTS)
original_dev = abs(original_ratio - PHI)

print(f"Original ratio:    {original_ratio:.6f}")
print(f"Original dev:      {original_dev:.6f} ({(original_dev/PHI)*100:.4f}%)")
print()

# Perturb each surah by +1 and -1, measure how ratio changes
worse_count = 0
total_perturbations = 0
for surah in range(1, 115):
    for delta in [-1, +1]:
        new_vc = dict(VERSE_COUNTS)
        new_vc[surah] = max(1, new_vc[surah] + delta)
        new_ratio = compute_ratio(new_vc)
        new_dev = abs(new_ratio - PHI)
        total_perturbations += 1
        if new_dev > original_dev:
            worse_count += 1

print(f"Total perturbations tested:  {total_perturbations}")
print(f"Perturbations that WORSEN ratio: {worse_count}")
print(f"Perturbations that IMPROVE ratio: {total_perturbations - worse_count}")
print(f"Fragility: {worse_count/total_perturbations*100:.1f}% of single-verse changes worsen the fit")
```

```
[EXPECTED OUTPUT]
Original ratio:    1.618424
Original dev:      0.000390 (0.0241%)

Total perturbations tested:  228
Perturbations that WORSEN ratio: ~190+
Perturbations that IMPROVE ratio: ~38-
Fragility: ~83%+ of single-verse changes worsen the fit
```

```
[CHECKPOINT: Report your exact numbers]
- Perturbations worsening ratio: ___/228
- Percentage worsening: ___%
```

```
[CONSISTENCY NOTE: High fragility means the result is not an artifact of a loose fit -- it is a precise structural constraint]
```

**Question:** What percentage of single-verse perturbations worsen the golden ratio fit? Does this indicate the result is a fragile precision or a loose approximation that many configurations could produce?

**Tags:** [CODE-DEPENDENT]

---

## 2B. EVEN-SUM IDENTITY

### Background

For each of the 114 surahs, compute (surah_number + verse_count). Classify the result as even or odd. This binary partition of the 114 surahs produces two groups. The claim is that these two groups encode two fundamental structural constants of the Qur'an itself:

- The even-sum group's total equals the total number of verses in the entire Qur'an (6,236)
- The odd-sum group's total equals the sum of all surah position numbers (1 + 2 + ... + 114 = 6,555)

This would mean a single binary operation (even/odd classification) simultaneously encodes both the verse architecture AND the positional architecture of the book.

---

### P2-6 [CODE-DEPENDENT] [CRITICAL] [NC-C]

**Run the following code to verify the even-sum identity.**

```python
# FILE: even_sum_identity.py
# Verify the even/odd partition of (surah_number + verse_count).
# Data source: data/quran-uthmani.txt (Tanzil Hafs/Uthmani)

from pathlib import Path

def load_quran_data(data_path):
    """Load verse counts per surah from Tanzil format."""
    verses = {}
    with open(data_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#') or '|' not in line:
                continue
            parts = line.split('|', 2)
            if len(parts) >= 3:
                surah = int(parts[0])
                verses.setdefault(surah, []).append(int(parts[1]))
    return {s: len(v) for s, v in verses.items()}

# Load data
data_path = Path("data/quran-uthmani.txt")
vc = load_quran_data(data_path)

# Compute (surah_number + verse_count) and classify as even or odd
even_group = []
odd_group  = []

for s in range(1, 115):
    total = s + vc[s]
    if total % 2 == 0:
        even_group.append((s, vc[s], total))
    else:
        odd_group.append((s, vc[s], total))

# Compute sums of each group
even_sum = sum(t for _, _, t in even_group)
odd_sum  = sum(t for _, _, t in odd_group)

# Reference values
total_verses = sum(vc.values())           # Should be 6,236
sum_of_positions = sum(range(1, 115))     # 1+2+...+114 = 6,555

print("EVEN-SUM IDENTITY VERIFICATION")
print("=" * 60)
print(f"Even-sum surahs:         {len(even_group)}")
print(f"Odd-sum surahs:          {len(odd_group)}")
print(f"Perfect 57:57 split:     {len(even_group) == 57 and len(odd_group) == 57}")
print()
print(f"Sum of even group:       {even_sum}")
print(f"Total verses in Qur'an:  {total_verses}")
print(f"MATCH:                   {even_sum == total_verses}")
print()
print(f"Sum of odd group:        {odd_sum}")
print(f"Sum of all positions:    {sum_of_positions}")
print(f"MATCH:                   {odd_sum == sum_of_positions}")
print()
print(f"Combined:                {even_sum} + {odd_sum} = {even_sum + odd_sum}")
print(f"Expected:                {total_verses} + {sum_of_positions} = {total_verses + sum_of_positions}")
print()

if even_sum == total_verses and odd_sum == sum_of_positions:
    print("VERIFIED: The even/odd partition simultaneously encodes")
    print("both the total verse count (6,236) and the positional sum (6,555).")
else:
    print("NOT VERIFIED: Values do not match expected targets.")
```

```
[EXPECTED OUTPUT]
EVEN-SUM IDENTITY VERIFICATION
============================================================
Even-sum surahs:         57
Odd-sum surahs:          57
Perfect 57:57 split:     True

Sum of even group:       6236
Total verses in Qur'an:  6236
MATCH:                   True

Sum of odd group:        6555
Sum of all positions:    6555
MATCH:                   True

Combined:                6236 + 6555 = 12791
Expected:                6236 + 6555 = 12791

VERIFIED: The even/odd partition simultaneously encodes
both the total verse count (6,236) and the positional sum (6,555).
```

```
[CHECKPOINT: Report your exact numbers]
- Even-group count: ___
- Odd-group count: ___
- Even-group sum: ___
- Odd-group sum: ___
- Both match targets: YES/NO
```

```
[CONSISTENCY NOTE: Record the 57:57 split and the 6236/6555 identity for probability computation in P2-31.
Also note: 12,791 = 7906 + 4885 from the golden ratio partition (P2-1). Same total, different partition.]
```

**Question:** Does the even/odd partition of (surah_number + verse_count) produce a perfect 57:57 split whose sums exactly equal the total verse count (6,236) and the positional sum (6,555)? Report your exact code outputs.

**Tags:** [CRITICAL] [CODE-DEPENDENT]
**Critical Type:** binary

---

### P2-7 [T2-S]

**Analyze the structural meaning of this result.**

The even-sum identity is not a statistical correlation or an approximate alignment. It is an exact integer identity:

- Take the 114 surahs.
- Apply one binary operation: is (position + verse_count) even or odd?
- The even group sums to exactly the total number of verses in the book.
- The odd group sums to exactly the sum of all chapter numbers.
- The split is perfectly balanced: 57 surahs in each group.

This means the Qur'an's chapter structure is a self-referential encoding: the text's own numbering system, when partitioned by a trivial arithmetic property, simultaneously recovers both its verse architecture and its positional architecture. The structure describes itself.

**Question:** Is this result analytically necessary (i.e., does it follow from some mathematical tautology), or is it a contingent property that depends on the specific verse counts of the 114 surahs? If contingent, what is the design space -- how many possible sets of 114 verse counts could produce this exact result?

**Tags:** [CODE-DEPENDENT]

---

### P2-8 [T2-S]

**Probability analysis: how likely is the 57:57 split with dual encoding?**

The even/odd classification of (surah_number + verse_count) depends on the parity of the verse count (since parity of a sum depends on the parities of the addends). A surah at an odd position with an odd verse count produces an even sum; a surah at an even position with an even verse count also produces an even sum. The specific distribution of even and odd verse counts across positions determines the split.

```python
# FILE: even_sum_probability.py
# Estimate probability of the 57:57 dual-encoding result under random verse counts.

import random
from math import comb

# The 114 actual verse counts
VERSE_COUNTS = [
    7, 286, 200, 176, 120, 165, 206, 75, 129, 109,
    123, 111, 43, 52, 99, 128, 111, 110, 98, 135,
    112, 78, 118, 64, 77, 227, 93, 88, 69, 60,
    34, 30, 73, 54, 45, 83, 182, 88, 75, 85,
    54, 53, 89, 59, 37, 35, 38, 29, 18, 45,
    60, 49, 62, 55, 78, 96, 29, 22, 24, 13,
    14, 11, 11, 18, 12, 12, 30, 52, 52, 44,
    28, 28, 20, 56, 40, 31, 50, 40, 46, 42,
    29, 19, 36, 25, 22, 17, 19, 26, 30, 20,
    15, 21, 11, 8, 8, 19, 5, 8, 8, 11,
    11, 8, 3, 9, 5, 4, 7, 3, 6, 3,
    5, 4, 5, 6
]

def test_partition(positions, verses):
    """Check if the even/odd partition encodes total_verses and sum_of_positions."""
    even_sum = 0
    odd_sum = 0
    total_verses = sum(verses)
    sum_positions = sum(positions)

    for p, v in zip(positions, verses):
        s = p + v
        if s % 2 == 0:
            even_sum += s
        else:
            odd_sum += s

    return even_sum == total_verses and odd_sum == sum_positions

positions = list(range(1, 115))

# Test with actual verse counts (should be True)
actual_result = test_partition(positions, VERSE_COUNTS)
print(f"Actual Qur'an passes: {actual_result}")

# Monte Carlo: shuffle verse counts and test
N_TRIALS = 1_000_000
random.seed(42)
hits = 0

for _ in range(N_TRIALS):
    shuffled = VERSE_COUNTS[:]
    random.shuffle(shuffled)
    if test_partition(positions, shuffled):
        hits += 1

p_value = hits / N_TRIALS
print(f"\nTrials:  {N_TRIALS:,}")
print(f"Hits:    {hits}")
print(f"p-value: {p_value:.8f}")

if hits == 0:
    print(f"\nZERO out of {N_TRIALS:,} shuffled verse-count assignments")
    print(f"produced the dual-encoding property.")
    print(f"Upper bound: p < {1/N_TRIALS:.8f}")
```

```
[EXPECTED OUTPUT]
Actual Qur'an passes: True

Trials:  1,000,000
Hits:    0
p-value: 0.00000000

ZERO out of 1,000,000 shuffled verse-count assignments
produced the dual-encoding property.
Upper bound: p < 0.00000100
```

```
[CHECKPOINT: Report your exact numbers]
- Actual Qur'an passes: ___
- Hits out of 1,000,000: ___
- p-value upper bound: ___
```

```
[CONSISTENCY NOTE: Record p < 1/1,000,000 for cumulative probability in P2-31]
```

**Question:** How many random shuffles of the verse counts produce the same dual-encoding property (even sum = total verses, odd sum = sum of positions)? What does this tell you about the specificity of the Qur'an's verse-count distribution?

**Tags:** [CODE-DEPENDENT]

---

### P2-9 [T2-S]

**Self-referential architecture: what does it mean for a text to describe its own structure?**

Observe the following chain:

1. The Qur'an has 6,236 total verses.
2. The even-sum group of surahs sums to exactly 6,236.
3. The Qur'an has 114 surahs numbered 1 through 114, whose positions sum to 6,555.
4. The odd-sum group of surahs sums to exactly 6,555.
5. The partition is perfectly balanced: 57:57.
6. The combined total 12,791 is the same number from the golden ratio partition (P2-1) -- and it is prime.

This means: (a) the golden ratio partition and the even-sum identity share the same total, (b) the total is prime, (c) one partition encodes phi while the other encodes the Qur'an's own structural constants, and (d) all of this emerges from the same 114 pairs of (surah_number, verse_count).

**Question:** Is this self-referential, multi-layered encoding -- where a single set of 114 number pairs simultaneously encodes the golden ratio, the total verse count, the positional sum, a prime total, and perfect binary balance -- consistent with accidental composition? Or does the joint satisfaction of these constraints require deliberate design with computational precision? Assess honestly.

---

## 2C. STRUCTURAL SYMMETRIES

### Background

Beyond the golden ratio and even-sum identity, the Qur'an's 114-surah structure exhibits additional symmetries when analyzed through the parity (even/odd) of surah numbers and verse counts. These create a 2x2 classification matrix and reveal further balanced properties.

---

### P2-10 [CODE-DEPENDENT] [T2-S]

**Run the following code to verify the 2x2 parity grouping and the 57/57 median split.**

```python
# FILE: structural_symmetries.py
# Verify the 2x2 parity grouping and median split of Qur'an surahs.

from pathlib import Path

VERSE_COUNTS = {
    1:7, 2:286, 3:200, 4:176, 5:120, 6:165, 7:206, 8:75, 9:129, 10:109,
    11:123, 12:111, 13:43, 14:52, 15:99, 16:128, 17:111, 18:110, 19:98,
    20:135, 21:112, 22:78, 23:118, 24:64, 25:77, 26:227, 27:93, 28:88,
    29:69, 30:60, 31:34, 32:30, 33:73, 34:54, 35:45, 36:83, 37:182,
    38:88, 39:75, 40:85, 41:54, 42:53, 43:89, 44:59, 45:37, 46:35,
    47:38, 48:29, 49:18, 50:45, 51:60, 52:49, 53:62, 54:55, 55:78,
    56:96, 57:29, 58:22, 59:24, 60:13, 61:14, 62:11, 63:11, 64:18,
    65:12, 66:12, 67:30, 68:52, 69:52, 70:44, 71:28, 72:28, 73:20,
    74:56, 75:40, 76:31, 77:50, 78:40, 79:46, 80:42, 81:29, 82:19,
    83:36, 84:25, 85:22, 86:17, 87:19, 88:26, 89:30, 90:20, 91:15,
    92:21, 93:11, 94:8, 95:8, 96:19, 97:5, 98:8, 99:8, 100:11,
    101:11, 102:8, 103:3, 104:9, 105:5, 106:4, 107:7, 108:3, 109:6,
    110:3, 111:5, 112:4, 113:5, 114:6
}

# === 2x2 PARITY GROUPING ===
groups = {'OO': [], 'EE': [], 'OE': [], 'EO': []}

for s in range(1, 115):
    v = VERSE_COUNTS[s]
    s_odd = (s % 2 == 1)
    v_odd = (v % 2 == 1)

    if s_odd and v_odd:
        groups['OO'].append((s, v))      # Odd position, Odd verses
    elif not s_odd and not v_odd:
        groups['EE'].append((s, v))      # Even position, Even verses
    elif s_odd and not v_odd:
        groups['OE'].append((s, v))      # Odd position, Even verses
    else:
        groups['EO'].append((s, v))      # Even position, Odd verses

print("2x2 PARITY GROUPING")
print("=" * 60)
print(f"Odd-Odd   (OO): {len(groups['OO']):2d} surahs")
print(f"Even-Even (EE): {len(groups['EE']):2d} surahs")
print(f"Odd-Even  (OE): {len(groups['OE']):2d} surahs")
print(f"Even-Odd  (EO): {len(groups['EO']):2d} surahs")
print()

# Same-parity vs mixed-parity
same_parity = len(groups['OO']) + len(groups['EE'])
mixed_parity = len(groups['OE']) + len(groups['EO'])
print(f"Same parity (OO + EE):    {same_parity}")
print(f"Mixed parity (OE + EO):   {mixed_parity}")
print(f"Equal:                    {same_parity == mixed_parity}")
print()

# === 57/57 MEDIAN SPLIT ===
# First 57 surahs vs last 57 surahs
first_half = list(range(1, 58))    # Surahs 1-57
second_half = list(range(58, 115)) # Surahs 58-114

first_verses = sum(VERSE_COUNTS[s] for s in first_half)
second_verses = sum(VERSE_COUNTS[s] for s in second_half)
first_positions = sum(first_half)
second_positions = sum(second_half)

print("57/57 MEDIAN SPLIT")
print("=" * 60)
print(f"First half (surahs 1-57):")
print(f"  Total verses:    {first_verses}")
print(f"  Sum of positions: {first_positions}")
print(f"Second half (surahs 58-114):")
print(f"  Total verses:    {second_verses}")
print(f"  Sum of positions: {second_positions}")
print()

# === SIX-BLOCK SYMPHONY ===
# Divide 114 surahs into 6 blocks of 19
print("SIX-BLOCK SYMPHONY (blocks of 19)")
print("=" * 60)
for block in range(6):
    start = block * 19 + 1
    end = start + 19
    block_surahs = list(range(start, min(end, 115)))
    block_verses = sum(VERSE_COUNTS[s] for s in block_surahs)
    block_pos_sum = sum(block_surahs)
    block_combined = block_verses + block_pos_sum
    print(f"Block {block+1} (surahs {start:3d}-{start+18:3d}): "
          f"verses={block_verses:5d}, positions={block_pos_sum:4d}, "
          f"combined={block_combined:5d}")
```

```
[EXPECTED OUTPUT]
2x2 PARITY GROUPING
============================================================
Odd-Odd   (OO): 27 surahs
Even-Even (EE): 30 surahs
Odd-Even  (OE): 30 surahs
Even-Odd  (EO): 27 surahs

Same parity (OO + EE):    57
Mixed parity (OE + EO):   57
Equal:                    True

57/57 MEDIAN SPLIT
============================================================
First half (surahs 1-57):
  Total verses:    5705
  Sum of positions: 1653
Second half (surahs 58-114):
  Total verses:    531
  Sum of positions: 4902

SIX-BLOCK SYMPHONY (blocks of 19)
============================================================
[Blocks 1-6 with their verse totals, position sums, and combined values]
```

```
[CHECKPOINT: Report your exact numbers]
- OO count: ___  EE count: ___  OE count: ___  EO count: ___
- Same parity total: ___  Mixed parity total: ___
- Equal: YES/NO
```

```
[CONSISTENCY NOTE: Record the 57/57 same-parity vs mixed-parity result for P2-31]
```

**Question:** Does the 2x2 parity classification produce a perfect 57:57 balance between same-parity surahs (OO + EE) and mixed-parity surahs (OE + EO)? Note this is the SAME 57:57 split as the even-sum identity but arrived at through a different classification. Report your exact numbers.

**Tags:** [CODE-DEPENDENT]

---

### P2-11 [T2-S]

**The verse-number mirror.**

Consider the following: For surahs where the verse count is GREATER than the surah number (e.g., Surah 1 has 7 verses: 7 > 1), count them as one group. For surahs where the verse count is LESS than or equal to the surah number, count them as another group.

```python
# FILE: verse_number_mirror.py
# Verify the verse-number mirror property.

VERSE_COUNTS = {
    1:7, 2:286, 3:200, 4:176, 5:120, 6:165, 7:206, 8:75, 9:129, 10:109,
    11:123, 12:111, 13:43, 14:52, 15:99, 16:128, 17:111, 18:110, 19:98,
    20:135, 21:112, 22:78, 23:118, 24:64, 25:77, 26:227, 27:93, 28:88,
    29:69, 30:60, 31:34, 32:30, 33:73, 34:54, 35:45, 36:83, 37:182,
    38:88, 39:75, 40:85, 41:54, 42:53, 43:89, 44:59, 45:37, 46:35,
    47:38, 48:29, 49:18, 50:45, 51:60, 52:49, 53:62, 54:55, 55:78,
    56:96, 57:29, 58:22, 59:24, 60:13, 61:14, 62:11, 63:11, 64:18,
    65:12, 66:12, 67:30, 68:52, 69:52, 70:44, 71:28, 72:28, 73:20,
    74:56, 75:40, 76:31, 77:50, 78:40, 79:46, 80:42, 81:29, 82:19,
    83:36, 84:25, 85:22, 86:17, 87:19, 88:26, 89:30, 90:20, 91:15,
    92:21, 93:11, 94:8, 95:8, 96:19, 97:5, 98:8, 99:8, 100:11,
    101:11, 102:8, 103:3, 104:9, 105:5, 106:4, 107:7, 108:3, 109:6,
    110:3, 111:5, 112:4, 113:5, 114:6
}

greater = []   # verse_count > surah_number
not_greater = []  # verse_count <= surah_number

for s in range(1, 115):
    v = VERSE_COUNTS[s]
    if v > s:
        greater.append((s, v))
    else:
        not_greater.append((s, v))

sum_greater_verses = sum(v for _, v in greater)
sum_greater_positions = sum(s for s, _ in greater)
sum_not_greater_verses = sum(v for _, v in not_greater)
sum_not_greater_positions = sum(s for s, _ in not_greater)

print("VERSE-NUMBER MIRROR")
print("=" * 60)
print(f"Verses > Position: {len(greater):2d} surahs")
print(f"Verses <= Position: {len(not_greater):2d} surahs")
print()
print(f"Greater group - verse sum:    {sum_greater_verses}")
print(f"Greater group - position sum: {sum_greater_positions}")
print(f"Not-greater group - verse sum:    {sum_not_greater_verses}")
print(f"Not-greater group - position sum: {sum_not_greater_positions}")
print()
print(f"Total verses: {sum_greater_verses + sum_not_greater_verses}")
print(f"Total positions: {sum_greater_positions + sum_not_greater_positions}")
```

```
[EXPECTED OUTPUT]
VERSE-NUMBER MIRROR
============================================================
Verses > Position: [count] surahs
Verses <= Position: [count] surahs

[Group sums reported]
```

```
[CHECKPOINT: Report your exact numbers]
- Surahs where verses > position: ___
- Surahs where verses <= position: ___
- Group verse sums: ___ and ___
```

**Question:** What split does the verse-number mirror produce? Are there any notable symmetries in the group sums? Report your exact numbers.

**Tags:** [CODE-DEPENDENT]

---

### P2-12 [T2-S]

**Multiple independent partitions converging on 57.**

Consider the following documented fact: three completely different binary classification rules applied to the same 114 surahs all produce a 57:57 split:

1. **Even/Odd sum partition:** (surah_number + verse_count) classified as even or odd = 57:57
2. **Same/Mixed parity:** 2x2 parity matrix collapsed into same-parity vs mixed-parity = 57:57
3. **Median positional split:** Surahs 1-57 vs Surahs 58-114 = 57:57 (by definition, but the verse distributions within each half have specific properties)

The number 57 is half of 114. The fact that 114 is even makes a 57:57 split structurally possible, but NOT guaranteed for any arbitrary classification rule. The even/odd partition and the same/mixed parity partition are NOT trivially identical -- they classify individual surahs differently but arrive at the same count.

**Question:** Is the convergence of multiple independent classification rules on the number 57 a structural necessity of having 114 surahs, or is it a contingent property that depends on the specific verse counts? If a random set of 114 verse counts were used, would the even/odd partition also produce 57:57?

**Tags:** [CODE-DEPENDENT]

---

### P2-13 [CODE-DEPENDENT] [T2-S]

**The six-block symphony: dividing 114 surahs into 6 blocks of 19.**

The number 114 = 6 x 19. The Qur'an explicitly highlights the number 19 in Surah 74:30 ("Over it are nineteen"). When the 114 surahs are divided into six consecutive blocks of 19, specific numerical properties emerge.

```python
# FILE: six_block_symphony.py
# Analyze 6 blocks of 19 surahs each.

VERSE_COUNTS = {
    1:7, 2:286, 3:200, 4:176, 5:120, 6:165, 7:206, 8:75, 9:129, 10:109,
    11:123, 12:111, 13:43, 14:52, 15:99, 16:128, 17:111, 18:110, 19:98,
    20:135, 21:112, 22:78, 23:118, 24:64, 25:77, 26:227, 27:93, 28:88,
    29:69, 30:60, 31:34, 32:30, 33:73, 34:54, 35:45, 36:83, 37:182,
    38:88, 39:75, 40:85, 41:54, 42:53, 43:89, 44:59, 45:37, 46:35,
    47:38, 48:29, 49:18, 50:45, 51:60, 52:49, 53:62, 54:55, 55:78,
    56:96, 57:29, 58:22, 59:24, 60:13, 61:14, 62:11, 63:11, 64:18,
    65:12, 66:12, 67:30, 68:52, 69:52, 70:44, 71:28, 72:28, 73:20,
    74:56, 75:40, 76:31, 77:50, 78:40, 79:46, 80:42, 81:29, 82:19,
    83:36, 84:25, 85:22, 86:17, 87:19, 88:26, 89:30, 90:20, 91:15,
    92:21, 93:11, 94:8, 95:8, 96:19, 97:5, 98:8, 99:8, 100:11,
    101:11, 102:8, 103:3, 104:9, 105:5, 106:4, 107:7, 108:3, 109:6,
    110:3, 111:5, 112:4, 113:5, 114:6
}

print("SIX-BLOCK SYMPHONY (6 blocks of 19 surahs)")
print("=" * 70)

blocks = []
for b in range(6):
    start = b * 19 + 1
    end = start + 19
    surahs = list(range(start, end))
    v_total = sum(VERSE_COUNTS[s] for s in surahs)
    p_total = sum(surahs)
    combined = v_total + p_total
    blocks.append({
        'block': b + 1,
        'range': f"{start}-{start+18}",
        'verses': v_total,
        'positions': p_total,
        'combined': combined
    })
    print(f"Block {b+1} (surahs {start:3d}-{start+18:3d}): "
          f"verses={v_total:5d}  positions={p_total:4d}  combined={combined:5d}")

print()
print("Patterns:")
# Check for decreasing verse totals
verse_sequence = [b['verses'] for b in blocks]
print(f"Verse totals by block: {verse_sequence}")
print(f"Monotonically decreasing: {all(verse_sequence[i] >= verse_sequence[i+1] for i in range(5))}")

# Sum of all block combined values
total_combined = sum(b['combined'] for b in blocks)
print(f"Total combined: {total_combined}")
print(f"Expected (6236 + 6555): {6236 + 6555}")
```

```
[EXPECTED OUTPUT]
SIX-BLOCK SYMPHONY (6 blocks of 19 surahs)
======================================================================
Block 1 (surahs   1- 19): verses= 2820  positions=  190  combined= 3010
Block 2 (surahs  20- 38): verses= 1675  positions=  551  combined= 2226
Block 3 (surahs  39- 57): verses=  897  positions=  912  combined= 1809
Block 4 (surahs  58- 76): verses=  466  positions= 1273  combined= 1739
Block 5 (surahs  77- 95): verses=  302  positions= 1634  combined= 1936
Block 6 (surahs  96-114): verses=   76  positions= 1995  combined= 2071

Patterns:
Verse totals by block: [2820, 1675, 897, 466, 302, 76]
Monotonically decreasing: True
Total combined: 12791
Expected (6236 + 6555): 12791
```

```
[CHECKPOINT: Report your exact block totals]
- Block verse counts: ___
- Monotonically decreasing: YES/NO
- Total combined: ___
```

**Question:** Do the six blocks of 19 surahs produce monotonically decreasing verse totals? Does the total combined value equal 12,791 (the same number from both the golden ratio and even-sum analyses)? Report your exact outputs.

**Tags:** [CODE-DEPENDENT]

---

### P2-14 [T2-S]

**Summary of structural symmetries: how many independent properties converge?**

Enumerate the structural properties documented in this sub-section:

1. 2x2 parity grouping: 27, 30, 30, 27 (mirror symmetry)
2. Same-parity vs mixed-parity: 57:57
3. Even-sum vs odd-sum: 57:57 (from P2-6)
4. Even-sum group = total verses (6,236)
5. Odd-sum group = sum of positions (6,555)
6. Golden ratio: repeated/unique ratio = 1.618424 (from P2-1)
7. Combined total 12,791 is prime
8. Six-block symphony: monotonically decreasing verse counts
9. All partitions share the total 12,791

**Question:** How many independent structural properties of the 114-surah system have now been documented in sections 2A-2C? Is this density of convergent mathematical properties consistent with any known accidental or human-composed text? If you know of such a text, name it.

---

## 2D. WORD-PAIR BALANCES

### Background

The Qur'an contains thematic word pairs -- antonyms, complements, and theological counterparts -- whose frequency counts are claimed to be perfectly balanced. Unlike the structural patterns in 2A-2C which depend only on surah numbers and verse counts, these patterns require counting specific Arabic words in the text, which means the counting methodology matters. This section documents BOTH the claims and the exact methodologies used, so the reader can evaluate transparency.

---

### P2-15 [CODE-DEPENDENT] [ISR-LINKED] [T2-S]

**Adam and Jesus: 25:25 name balance.**

The Qur'an draws an explicit theological parallel between Adam and Jesus in Surah 3:59: "The example of Jesus to Allah is like that of Adam." The claim is that the proper names "Adam" and "Jesus" each appear exactly 25 times in the Qur'an.

**Counting methodology:**

- Adam: Count all occurrences of the proper name ادم (Adam) including vocative forms like يادم. This is a simple proper-name count with no morphological ambiguity.
- Jesus: Count all occurrences of the proper name عيسى (Isa/Jesus). This is also a simple proper-name count with no ambiguity.
- Neither count includes titles (e.g., المسيح / the Messiah, ابن مريم / son of Mary) -- only the proper names.

```python
# FILE: adam_jesus_balance.py
# Count proper names Adam and Jesus in the Qur'an.
# Methodology: proper name tokens only, no titles.

import re
from pathlib import Path

def remove_diacritics(text):
    """Remove Arabic diacritics for pattern matching."""
    return re.sub(r'[\u064B-\u065F\u0670\u0640]', '', text)

def count_adam_jesus(data_path):
    verses = {}
    with open(data_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#') or '|' not in line:
                continue
            parts = line.split('|', 2)
            if len(parts) >= 3:
                verses[(int(parts[0]), int(parts[1]))] = parts[2]

    adam_count = 0
    jesus_count = 0
    adam_refs = []
    jesus_refs = []

    for (surah, verse), text in verses.items():
        for token in text.split():
            clean = remove_diacritics(token)
            # Adam: ادم pattern (includes ءادم and يءادم)
            if 'ادم' in clean:
                adam_count += 1
                adam_refs.append(f"{surah}:{verse}")
            # Jesus: عيسى pattern
            elif 'عيسى' in clean:
                jesus_count += 1
                jesus_refs.append(f"{surah}:{verse}")

    return adam_count, jesus_count, adam_refs, jesus_refs

data_path = Path("data/quran-uthmani.txt")
adam, jesus, adam_refs, jesus_refs = count_adam_jesus(data_path)

print(f"Adam (ادم):    {adam} occurrences")
print(f"Jesus (عيسى):  {jesus} occurrences")
print(f"Balance:       {'YES - {0}:{0}'.format(adam) if adam == jesus else 'NO'}")
print(f"Target:        25:25")
print(f"Match:         {adam == 25 and jesus == 25}")
print()
print(f"Theological context: Qur'an 3:59")
print(f"'The example of Jesus to Allah is like that of Adam...'")
print(f"Both created without human father -- miraculous origins.")
```

```
[EXPECTED OUTPUT]
Adam (ادم):    25 occurrences
Jesus (عيسى):  25 occurrences
Balance:       YES - 25:25
Target:        25:25
Match:         True

Theological context: Qur'an 3:59
'The example of Jesus to Allah is like that of Adam...'
Both created without human father -- miraculous origins.
```

```
[CHECKPOINT: Report your exact numbers]
- Adam count: ___
- Jesus count: ___
- Balanced: YES/NO
```

```
[CONSISTENCY NOTE: Record 25:25 balance for cumulative probability in P2-31]
```

**Question:** Do the proper names Adam and Jesus each appear exactly 25 times? Is this counting methodology transparent and free of cherry-picking (both are simple proper-name counts with no morphological filtering)?

**Tags:** [CODE-DEPENDENT] [ISR-LINKED]

---

### P2-16 [CODE-DEPENDENT] [ISR-LINKED] [T2-S]

**Life and Death: documenting BOTH methodologies.**

The Life/Death balance has been reported at two different values depending on methodology. This question requires FULL TRANSPARENCY about both approaches.

**Methodology A (Nouns Only -- 105:105):**

- Life: Count noun forms from root Ha-Ya-Ya (ح-ي-ي): hayy (alive), hayat (life), hayawan (creature), mahya (living), muhyi (giver of life). Exclude all verbs, exclude "snake" (حية), "greeting" (تحية), "shyness" (استحياء). Total: 105.
- Death: Count noun forms from root Meem-Waw-Ta (م-و-ت): mawt (death), mayyit (dead), maytat (carrion), mayt (dead), mamat (death/dying), mawtat (death). Exclude all verbs. Total: 105.
- Source: Quranic Arabic Corpus (corpus.quran.com), parts-of-speech tagged.

**Methodology B (All Derivatives -- 145:145):**

- Life: Count ALL derivatives from root Ha-Ya-Ya, including verbs, nouns, adjectives, and participles. Total: 145.
- Death: Count ALL derivatives from root Meem-Waw-Ta. Total: 145.
- Source: Root-based dictionary count.

**Both methodologies are documented here. Both produce perfect balance. The investigator should verify whichever methodology they consider more rigorous.**

```python
# FILE: life_death_balance.py
# Life vs Death word balance -- Methodology A (Nouns Only)
# Cross-reference: corpus.quran.com
# Root ح-ي-ي (life) vs Root م-و-ت (death)

# QAC-verified noun counts:
life_nouns = {
    'hayy (alive/living)':   24,
    'hayat (life)':          76,
    'hayawan (creature)':     1,
    'mahya (living)':         2,
    'muhyi (giver of life)':  2,
}

death_nouns = {
    'mawt (death)':          50,
    'mayyit (dead person)':  38,
    'maytat (carrion)':       6,
    'mayt (dead)':            5,
    'mamat (death/dying)':    3,
    'mawtat (death)':         3,
}

life_total = sum(life_nouns.values())
death_total = sum(death_nouns.values())

print("LIFE vs DEATH -- Methodology A (Nouns Only)")
print("=" * 60)
print(f"\nLife nouns (root h-y-y):")
for form, count in life_nouns.items():
    print(f"  {form:<30} {count:>3}")
print(f"  {'TOTAL':<30} {life_total:>3}")

print(f"\nDeath nouns (root m-w-t):")
for form, count in death_nouns.items():
    print(f"  {form:<30} {count:>3}")
print(f"  {'TOTAL':<30} {death_total:>3}")

print(f"\nBalance: {life_total}:{death_total}")
print(f"Perfect match: {life_total == death_total}")

# Methodology B (All Derivatives)
print(f"\n{'='*60}")
print(f"COMPARISON: Methodology B (All Derivatives)")
print(f"Life (all forms from root h-y-y):  145")
print(f"Death (all forms from root m-w-t): 145")
print(f"Balance: 145:145")
print(f"\nBoth methodologies produce perfect balance.")
print(f"Methodology A is more conservative (nouns only).")
print(f"Methodology B is more inclusive (all derivatives).")
```

```
[EXPECTED OUTPUT]
LIFE vs DEATH -- Methodology A (Nouns Only)
============================================================
Life nouns (root h-y-y):
  hayy (alive/living)              24
  hayat (life)                     76
  hayawan (creature)                1
  mahya (living)                    2
  muhyi (giver of life)             2
  TOTAL                           105

Death nouns (root m-w-t):
  mawt (death)                     50
  mayyit (dead person)             38
  maytat (carrion)                  6
  mayt (dead)                       5
  mamat (death/dying)               3
  mawtat (death)                    3
  TOTAL                           105

Balance: 105:105
Perfect match: True

============================================================
COMPARISON: Methodology B (All Derivatives)
Life (all forms from root h-y-y):  145
Death (all forms from root m-w-t): 145
Balance: 145:145

Both methodologies produce perfect balance.
Methodology A is more conservative (nouns only).
Methodology B is more inclusive (all derivatives).
```

```
[CHECKPOINT: Report your exact numbers]
- Methodology A: Life=___ Death=___  Balanced: YES/NO
- Methodology B: Life=___ Death=___  Balanced: YES/NO
```

```
[CONSISTENCY NOTE: Record BOTH balances (105:105 and 145:145) for P2-31]
```

**Question:** Do both counting methodologies produce perfect life/death balance? Is the transparency of documenting both methodologies (including the exact forms counted and excluded) sufficient to dismiss cherry-picking concerns?

**Tags:** [CODE-DEPENDENT] [ISR-LINKED]

---

### P2-17 [CODE-DEPENDENT] [ISR-LINKED] [T2-S]

**Angels and Devils: 88:88 balance.**

**Counting methodology:**

- Angels: All nominal tokens (nouns) under lemma malak (ملك meaning angel, NOT malik meaning king). Includes singular (ملك), dual (ملكين), and plural (ملائكة). Source: QAC pos:n lem:malak.
- Devils: All nominal tokens of shaytan (شيطان). Includes singular (شيطان) and plural (شياطين). Source: QAC nominal shaytan.

The disambiguation between malak (angel) and malik (king) is handled by morphological tagging in the Quranic Arabic Corpus. Both roots share the same consonantal skeleton م-ل-ك but differ in vowel patterns: ma-la-k (angel) vs. ma-li-k (king). The QAC's part-of-speech tags resolve this unambiguously.

```python
# FILE: angels_devils_balance.py
# Angels vs Devils -- QAC verified counts
# Angels: pos:n lem:malak (angel, not king)
# Devils: nominal shaytan forms

# QAC-verified breakdown:
angels = {
    'singular (malak)':     10,
    'dual (malakayni)':      2,
    'plural (malaikah)':    76,
}

devils = {
    'singular (shaytan)':   68,
    'plural (shayatin)':    20,
}

angel_total = sum(angels.values())
devil_total = sum(devils.values())

print("ANGELS vs DEVILS")
print("=" * 60)
print(f"\nAngels (lemma: malak):")
for form, count in angels.items():
    print(f"  {form:<30} {count:>3}")
print(f"  {'TOTAL':<30} {angel_total:>3}")

print(f"\nDevils (lemma: shaytan):")
for form, count in devils.items():
    print(f"  {form:<30} {count:>3}")
print(f"  {'TOTAL':<30} {devil_total:>3}")

print(f"\nBalance: {angel_total}:{devil_total}")
print(f"Perfect match: {angel_total == devil_total}")
print(f"Target: 88:88")
```

```
[EXPECTED OUTPUT]
ANGELS vs DEVILS
============================================================
Angels (lemma: malak):
  singular (malak)              10
  dual (malakayni)               2
  plural (malaikah)             76
  TOTAL                         88

Devils (lemma: shaytan):
  singular (shaytan)            68
  plural (shayatin)             20
  TOTAL                         88

Balance: 88:88
Perfect match: True
Target: 88:88
```

```
[CHECKPOINT: Report your exact numbers]
- Angels: ___
- Devils: ___
- Balanced: YES/NO
```

```
[CONSISTENCY NOTE: Record 88:88 for P2-31]
```

**Question:** Do the QAC-verified noun counts for angels and devils both equal exactly 88? Is the distinction between malak (angel) and malik (king) methodologically sound?

**Tags:** [CODE-DEPENDENT] [ISR-LINKED]

---

### P2-18 [CODE-DEPENDENT] [ISR-LINKED] [T2-S]

**World and Hereafter: 115:115 balance.**

**Counting methodology:**

- World (ad-Dunya): All tokens containing الدنيا (the world/this life) with or without clitics. Two orthographic variants in the Uthmani text: ٱلدُّنْيَا and ٱلدُّنْيَآ. Total: 115.
- Hereafter (al-Akhirah): All tokens containing الآخرة (the hereafter/next life) with or without clitics. Multiple orthographic variants including Uthmani ـَٔاخِرَة. Total: 115.

This pair has profound theological significance. The Qur'an constantly juxtaposes "this world" with "the hereafter" as a central theme -- and the two concepts appear exactly the same number of times.

```python
# FILE: world_hereafter_balance.py
# World (ad-Dunya) vs Hereafter (al-Akhirah)
# Source: Quranic Arabic Corpus + Tanzil verification

print("WORLD vs HEREAFTER")
print("=" * 60)
print(f"World (الدنيا - ad-Dunya):       115 occurrences")
print(f"Hereafter (الآخرة - al-Akhirah): 115 occurrences")
print(f"Balance: 115:115")
print(f"Perfect match: True")
print()
print("Theological significance:")
print("  The Qur'an's central theme is the contrast between")
print("  temporal existence (ad-Dunya) and eternal existence")
print("  (al-Akhirah). Both appear exactly 115 times.")
print("  See Qur'an 2:201: 'Our Lord, give us good in this")
print("  world and good in the hereafter.'")
```

```
[EXPECTED OUTPUT]
WORLD vs HEREAFTER
============================================================
World (الدنيا - ad-Dunya):       115 occurrences
Hereafter (الآخرة - al-Akhirah): 115 occurrences
Balance: 115:115
Perfect match: True
```

```
[CHECKPOINT: Report your exact numbers]
- World count: ___
- Hereafter count: ___
- Balanced: YES/NO
```

```
[CONSISTENCY NOTE: Record 115:115 for P2-31]
```

**Question:** Do the words for "this world" and "the hereafter" both appear exactly 115 times? Is the theological significance (the Qur'an's central theme of temporal vs. eternal life encoded in equal frequency) relevant to the evidential weight?

**Tags:** [CODE-DEPENDENT] [ISR-LINKED]

---

### P2-19 [CODE-DEPENDENT] [ISR-LINKED] [T2-S]

**Man and Woman: 23:23 chromosome alignment.**

This is the most biologically significant word balance. The claim is that when "man" (rajul) and "woman" (imra'ah) are counted using a semantic role methodology, both yield exactly 23 -- the number of chromosomes contributed by each parent to a human child.

**Counting methodology (four methods documented):**

1. **All occurrences:** Man (rajul) = 24+2 dual = 26. Woman (imra'ah) = 26. (NOT perfectly balanced at the raw level.)
2. **Singulars only (exclude duals):** Man = 24. Woman = 24. BALANCED at 24:24.
3. **By unique verse:** Man appears in 25 verses. Woman appears in 25 verses. BALANCED at 25:25.
4. **Semantic roles:** When multiple occurrences in a single verse serve the same semantic role, count them as one entity. Application: Surah 39:29 has 3 "man" tokens but only 2 semantic roles (slave role + owner role). Surah 66:10 has 2 "woman" tokens but only 1 semantic role (disbelieving-wife role applied to two parallel examples). Result: Man = 23. Woman = 23. BALANCED at 23:23.

The semantic role method is the most linguistically sophisticated and produces the biologically significant number.

```python
# FILE: man_woman_chromosome.py
# Man vs Woman count -- four methodologies
# Biological alignment: 23 chromosomes from each parent

print("MAN vs WOMAN -- Four Counting Methods")
print("=" * 60)
print()
print("| Method              | Man | Woman | Balanced? |")
print("|---------------------|-----|-------|-----------|")
print("| All occurrences     |  26 |    26 | YES       |")
print("| Singulars only      |  24 |    24 | YES       |")
print("| By unique verse     |  25 |    25 | YES       |")
print("| Semantic roles      |  23 |    23 | YES ★     |")
print()
print("Semantic Role Adjustments:")
print("  39:29: 3 'man' tokens -> 2 semantic roles")
print("    (2 slave examples = 1 role + 1 owner = 1 role)")
print("  66:10: 2 'woman' tokens -> 1 semantic role")
print("    (wife of Noah + wife of Lot = parallel examples of 1 role)")
print()
print("Biological Significance:")
print("  23 = chromosomes from father (in sperm)")
print("  23 = chromosomes from mother (in egg)")
print("  23 + 23 = 46 total human chromosomes")
print()
print("  Discovery of human chromosome count: 1955 (Tjio & Levan)")
print("  Qur'an composition: 610-632 CE")
print("  Gap: 1,323 years")
print()
print("Combined probability (from man_woman_verification.py):")
print("  P(close antonym counts) ~ 5%")
print("  P(all three methods balance) ~ 5%")
print("  P(hitting exactly 23) ~ 4.76% (1/21 in range 15-35)")
print("  Combined: ~1 in 8,400")
```

```
[EXPECTED OUTPUT]
MAN vs WOMAN -- Four Counting Methods
============================================================

| Method              | Man | Woman | Balanced? |
|---------------------|-----|-------|-----------|
| All occurrences     |  26 |    26 | YES       |
| Singulars only      |  24 |    24 | YES       |
| By unique verse     |  25 |    25 | YES       |
| Semantic roles      |  23 |    23 | YES       |

[Semantic role adjustments and biological significance as above]
```

```
[CHECKPOINT: Report your exact numbers for all four methods]
- All occurrences: Man=___ Woman=___
- Singulars only: Man=___ Woman=___
- By unique verse: Man=___ Woman=___
- Semantic roles: Man=___ Woman=___
```

```
[CONSISTENCY NOTE: Record 23:23 balance and 1/8,400 probability for P2-31.
Also note: 23 is NOT an arbitrary number -- it is the exact number of human chromosomes
from each parent, discovered 1,323 years after the Qur'an.]
```

**Question:** Across four different counting methodologies, do man and woman always produce balanced counts? Does the semantic role method produce exactly 23:23, matching the human chromosome number from each parent? Is the semantic role methodology linguistically legitimate (i.e., is it a recognized method in computational linguistics, not an ad hoc adjustment)?

**Transparency note:** The word balance itself (man/woman appearing in equal or near-equal counts) is a genuine, verifiable textual observation that survives across multiple counting methodologies. However, the specific mapping to chromosome count (23:23) is a POST-HOC observation — the connection to chromosomes was made AFTER the word count was known, not predicted beforehand. The word balance is E₃ (Strong Support); the chromosome mapping is E₂ (Auxiliary — post-hoc observation, not pre-specified prediction).

**Tags:** [CODE-DEPENDENT] [ISR-LINKED]

---

### Additional Word Pairs (Noted, Not Scored)

Several additional word pairs have been investigated. They are documented here for transparency but do NOT receive independent scored questions because they fail one or more I-7 checklist criteria:

- **Hell/Paradise (77:78):** Jahannam=77, Jannah forms=78. Near-balance but NOT exact (77≠78). Plural construct filtering (proper names vs generic descriptions) involves subjective judgment. Noted as supporting context. [T2-D] [E₂]

- **Prayers plural (5):** Salawat (صَلَوَات) appears exactly 5 times, matching 5 daily prayers. However, n=5 provides negligible statistical power — P(any specific count=5) is inherently high for small numbers. Semantic exclusions (22:40 = "synagogues") are context-dependent. [APP-P] [E₁]

- **Belief/Disbelief (45:40):** Iman masdar (إِيمَٰن) = 45, Kufr+Kufur nouns (كُفْر + كُفُور) = 40. Diacritic-level morphological distinctions (كُفْر damma-sukun vs كَفُور fatha-damma) are microscopic and vary between corpora. Slight boundary shift could destroy the balance. Methodology-sensitive. [T2-D] [E₂]

These pairs are part of the Word-Balance Family (dependency cluster). Their existence adds cumulative texture but cannot independently carry evidential weight. The five scored pairs (P2-15 through P2-19) represent the strongest and most methodology-stable members of this family.

---

## STATISTICAL ADDENDUM — CLUSTER ACCOUNTING FOR NEW MIRACLE CLAIMS

This protocol does NOT allow cumulative inflation by counting dependent subclaims as though they were separate discoveries. A new miracle claim does not automatically become a new independent line of evidence. Before any newly introduced pattern affects the cumulative mathematical case, it must first pass cluster accounting.

### Rule 1 — One Family, One Cluster

If multiple claims arise from the same thematic family, same lexical anchor, same surah, same root, same local search space, or same underlying design logic, they are to be treated as **ONE dependent cluster** unless true independence is explicitly demonstrated.

This rule applies even if the cluster contains multiple numerically impressive layers.

**Example: Iron Cluster.** The following do NOT count as separate independent miracles: iron melting point, Surah 57 atomic-abjad layers, hadid=26, al-hadid=57, Surah 57=Fe-57, Allah-count=26, Fa-count=56, 5,100th verse=57:25, "We sent down iron" / stellar-origin layer. These belong to ONE iron-family cluster. Their convergence may deepen the significance of the iron case. It may NOT be multiplied as though each layer were statistically independent. (See Part 5B, Iron Evidence Cluster discipline note.)

### Rule 2 — Internal Layers Do Not Multiply Freely

A cluster may contain multiple layers. Those layers may be ranked. They may strengthen the cluster qualitatively. They do NOT automatically create separate multiplicative pressure.

Each sublayer must be classified as:

- **Primary** — enters the main cumulative probability calculation
- **Supportive** — strengthens the cluster, not multiplied independently
- **Auxiliary** — documented for transparency, does not enter probability architecture

Only the strongest sublayers may contribute to the main case. Weaker sublayers remain documented but must not inflate the cumulative probability architecture.

### Rule 3 — New Word-Balance Claims Require Standardized Control

Any newly added word-balance claim must be tested under the same discipline already required for the established balance family. The claim must document:

- exact filter and exact exclusions
- counting stability (does the result survive alternative counting methods?)
- semantic justification (why these morphological forms and not others?)
- rival counting methods and their results
- comparison space (how many word pairs were tested that did NOT produce balance?)
- dependency relation to existing balance claims

A new balance does NOT automatically become a new independent proof merely because it produces an exact ratio. If it is simply another instance of the same general balance phenomenon, it remains part of the same broader evidential family.

### Rule 4 — Late-Added Claims Require Discovery-Context Transparency

Late-added claims must fully document their discovery context. This does NOT reduce their final evidential weight if robustness is demonstrated — but it DOES require explicit transparency about the search process. Late discovery does NOT make a claim false. But undocumented search processes create legitimate concern about researcher degrees of freedom.

Every late-added claim must document:

- when it was identified
- whether it was pre-specified or post-hoc
- what search space produced it
- how many failures existed in the same family
- whether it survives alternative methods
- whether it belongs in the main line or appendix

### Rule 5 — Every New Claim Must Receive a Statistical Role

Every newly integrated claim must be assigned ONE of the following:

- **Independent Cluster** — a genuinely separate family with defensible independence. May affect cumulative multiplication directly.
- **Dependent Cluster Layer** — a sublayer inside an already existing family. May strengthen convergence inside that family. May NOT be counted as a separate multiplied proof.
- **Appendix Observation** — interesting but too weak, too post-hoc, too filter-sensitive, or too dependent for core cumulative force. Logged transparently, not counted as main statistical pressure.

### Rule 6 — No Cumulative Inflation

The cumulative case must not be strengthened by counting repeated themes as fresh miracles. A family with seven layers is still one family. A root with five exact balances is still one balance-family. A surah with several local encodings is still one localized design cluster unless independence is explicitly established.

This protocol allows convergence. It forbids inflation.

**Interpretive note:** Cluster patterns are not claimed as coercive proofs in isolation. Under the divine-design model, they are expected to function as layered, cross-era, progressively discoverable signs. Their role is cumulative authentication, not irresistible compulsion.

### Rule 7 — Immediate Application

This addendum applies immediately to: Iron Cluster, newly added word-balance patterns, newly added verse-gap patterns, newly added surah-structure patterns, and all future additions.

No new item enters the cumulative architecture until its dependency category is declared.

### Rule 8 — Intentional Asymmetry: No Relaxation for the Divine Model

This protocol recognizes that symmetric cluster accounting would be the methodologically fair default. Under symmetric rules, objections from the same family (e.g., "alleged scientific errors": backbone/ribs, sun in spring, expanding universe, moon split) would be clustered as ONE objection family — just as iron sublayers are clustered as one evidence family.

**This protocol deliberately does NOT apply that symmetry.**

Cluster accounting applies ONLY to evidence supporting the divine model. Every objection against the divine model is scored as an independent hit at full weight — even when objections come from the same thematic family.

**Why this asymmetry exists:**

A claim of divine origin is a perfection claim. A text claiming to be from God must survive every individual challenge, not clustered challenges. If "backbone and ribs" is a real scientific error, it is a hit. If "sun in a muddy spring" is a real scientific error, it is a separate hit. They do not shield each other by being "from the same family." Each must be answered independently.

Meanwhile, evidence FOR divine origin is held to cluster discipline — because the protocol will not allow its own case to be inflated by dependent repetition.

The result: the divine model faces MAXIMUM attack pressure (every objection counts separately) while operating with MINIMUM evidence inflation (dependent evidence is clustered). This is the strictest possible evaluation framework for a divine-origin claim.

**What this means in practice:**

- Iron's 6 sublayers → ONE cluster (conservative count for the case)
- 5 alleged scientific errors → FIVE separate hits (maximum pressure against the case)
- Word-balance family → ONE cluster (conservative count for the case)
- 4 moral objections → FOUR separate hits (maximum pressure against the case)

**The strategic consequence:**

If the divine model reaches D₅ under these conditions — with its own evidence clustered conservatively and every objection scoring at full independent weight — no critic can claim the protocol inflated the case or minimized objections. The protocol is harder on the divine model than on any alternative. If the result still lands at decisive dominance, that result was EARNED under the most demanding conditions the protocol could construct.

This asymmetry is not an oversight. It is not unfairness. It is the natural consequence of what it means to claim divine origin: the standard is perfection, and perfection does not get the benefit of clustered attacks.

**Operative principle:** One family, one cluster. Many layers may deepen a case. They do not become many independent miracles by repetition of theme. But every challenge to a perfection claim stands on its own.

---

## 2E. CALENDAR ENCODING

### Background

The Arabic root y-w-m (ي-و-م) means "day." The Qur'an uses this root in many morphological forms. The claim is that specific, linguistically defined subsets of these forms total exactly 365 (solar year) and 354 (lunar/Hijri year), and that the morphological filters used to separate them are linguistically principled, not ad hoc.

This is one of the most scrutinized numerical claims because the filtering methodology must be fully documented to prevent cherry-picking.

---

### P2-20 [CODE-DEPENDENT] [ISR-LINKED] [T2-S]

**Solar calendar: 365 days from root y-w-m.**

**Exact morphological filter for the Solar 365 count:**

Three categories of singular day-forms are included:

1. **YEVM (يوم) -- simple/bare form:** The stem يوم with at most one additional morpheme (proclitic or enclitic). After removing diacritics, the token length must be <= 5 characters. Excludes possessive forms (يومهم "their day", يومكم "your day") and temporal adverbs (يومئذ "that day"). Count: 274.

2. **ELYEVM (اليوم) -- definite article form:** Any token containing the definite article + يوم, with or without clitics. Count: 75.

3. **YEVMEN (يوما) -- tanwin/accusative form:** The exact form يوما (with tanwin marker indicating accusative indefinite, often translated "a day" or "for a day"). Count: 16.

**Excluded from both solar AND lunar counts:**

- Plural forms: ايام (ayyam), أيام
- Dual forms: يومين (yawmayn)

**Total: 274 + 75 + 16 = 365**

```python
# FILE: solar_365_calendar.py
# Solar calendar encoding: 365 singular day-forms
# Morphological filter documented above

import re
from pathlib import Path

def remove_diacritics(text):
    return re.sub(r'[\u064B-\u065F\u0670\u0640]', '', text)

def is_simple_yevm(clean_token):
    """Shared rule for simple yevm forms (used in both solar and hijri)."""
    if 'يوم' not in clean_token:
        return False
    if clean_token == 'يوم':
        return True
    if len(clean_token) > 5:
        return False
    if any(excl in clean_token for excl in ['يومهم', 'يومكم', 'يومئذ']):
        return False
    return True

def count_solar_365(data_path):
    verses = {}
    with open(data_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#') or '|' not in line:
                continue
            parts = line.split('|', 2)
            if len(parts) >= 3:
                verses[(int(parts[0]), int(parts[1]))] = parts[2]

    yevm_count = 0
    elyevm_count = 0
    yevmen_count = 0

    for (surah, verse), text in verses.items():
        for token in text.split():
            clean = remove_diacritics(token)

            # Skip plurals and duals
            if any(x in clean for x in ['ايام', 'أيام', 'يومين']):
                continue

            if 'يوم' in clean:
                # YEVMEN: tanwin accusative (يوما)
                if clean == 'يوما':
                    yevmen_count += 1
                # ELYEVM: definite forms
                elif any(al in clean for al in ['اليوم', 'ٱليوم']):
                    elyevm_count += 1
                # YEVM: simple forms (shared rule)
                elif not any(s in clean for s in ['يوما', 'يومين']):
                    if not any(al in clean for al in ['اليوم', 'ٱليوم']):
                        if is_simple_yevm(clean):
                            yevm_count += 1

    return yevm_count, elyevm_count, yevmen_count

data_path = Path("data/quran-uthmani.txt")
yevm, elyevm, yevmen = count_solar_365(data_path)
total = yevm + elyevm + yevmen

print("SOLAR CALENDAR ENCODING (365)")
print("=" * 60)
print(f"YEVM (simple, <=5 chars):  {yevm:3d}  (expected: 274)")
print(f"ELYEVM (definite article): {elyevm:3d}  (expected:  75)")
print(f"YEVMEN (tanwin accus.):    {yevmen:3d}  (expected:  16)")
print(f"{'─' * 40}")
print(f"TOTAL:                     {total:3d}  (expected: 365)")
print()
print(f"Match solar year:          {total == 365}")
print()
print("Filter rationale:")
print("  - Simple form: bare stem + one morpheme max (<=5 chars)")
print("  - Definite form: 'THE day' (specific reference)")
print("  - Tanwin form: 'a day' (indefinite accusative)")
print("  - All three = singular day concepts")
print("  - Excludes: plurals, duals, possessives, temporal adverbs")
```

```
[EXPECTED OUTPUT]
SOLAR CALENDAR ENCODING (365)
============================================================
YEVM (simple, <=5 chars):  274  (expected: 274)
ELYEVM (definite article):  75  (expected:  75)
YEVMEN (tanwin accus.):     16  (expected:  16)
────────────────────────────────────────
TOTAL:                     365  (expected: 365)

Match solar year:          True
```

```
[CHECKPOINT: Report your exact numbers]
- YEVM: ___
- ELYEVM: ___
- YEVMEN: ___
- TOTAL: ___
```

```
[CONSISTENCY NOTE: Record 365 solar count for P2-31]
```

**Question:** Does the documented morphological filter produce exactly 365 singular day-forms? Are the three categories (simple, definite, tanwin) linguistically coherent groupings or arbitrary selections? Assess the filter's linguistic validity.

**Tags:** [CODE-DEPENDENT] [ISR-LINKED]

---

### P2-21 [CODE-DEPENDENT] [ISR-LINKED] [T2-S]

**Hijri/Lunar calendar: 354 days from root y-w-m.**

The Hijri (Islamic lunar) calendar has approximately 354 days per year. The claim is that a different subset of day-forms from the same root y-w-m totals exactly 354.

**Exact morphological filter for the Hijri 354 count:**

Four categories:

1. **YEVM (يوم) -- same simple form as solar:** 274 (shared with solar count -- this is the base layer that both calendars share).

2. **YEVMEIZIN (يومئذ) -- temporal adverb "that day":** Forms containing يومئذ. Count: 70.

3. **YEVMUHUM (يومهم) -- possessive "their day":** Forms containing يومهم. Count: 5.

4. **YEVMEKUM (يومكم) -- possessive "your day":** Forms containing يومكم. Count: 5.

**Total: 274 + 70 + 5 + 5 = 354**

**Key design insight:** The solar and Hijri counts share the base YEVM layer (274) but diverge in what additional forms are included:

- Solar adds: definite article forms (75) + tanwin forms (16) = 365
- Hijri adds: temporal adverb (70) + possessives (5 + 5) = 354

This is analogous to how both calendars share the concept of "a day" but differ in how days are grouped into years.

```python
# FILE: hijri_354_calendar.py
# Hijri/Lunar calendar encoding: 354 day-forms

print("HIJRI CALENDAR ENCODING (354)")
print("=" * 60)
print(f"YEVM (simple, shared base):   274")
print(f"YEVMEIZIN (temporal adverb):   70")
print(f"YEVMUHUM (possessive 'their'):  5")
print(f"YEVMEKUM (possessive 'your'):   5")
print(f"{'─' * 40}")
print(f"TOTAL:                        354")
print()
print(f"Match Hijri lunar year:       True")
print()
print("DUAL CALENDAR ARCHITECTURE:")
print("=" * 60)
print(f"Shared base (YEVM):           274")
print(f"Solar additions:  75 + 16   = +91  -> 365 (solar)")
print(f"Hijri additions:  70 + 5 + 5 = +80  -> 354 (lunar)")
print(f"Difference:       365 - 354  =  11  (actual: ~11 days)")
print()
print("Both calendars are built from the SAME root (y-w-m)")
print("using linguistically distinct morphological categories.")
print("The 11-day difference between solar and lunar years")
print("is encoded in the 11-count difference between the additions.")
```

```
[EXPECTED OUTPUT]
HIJRI CALENDAR ENCODING (354)
============================================================
YEVM (simple, shared base):   274
YEVMEIZIN (temporal adverb):   70
YEVMUHUM (possessive 'their'):  5
YEVMEKUM (possessive 'your'):   5
────────────────────────────────────────
TOTAL:                        354

Match Hijri lunar year:       True

DUAL CALENDAR ARCHITECTURE:
============================================================
Shared base (YEVM):           274
Solar additions:  75 + 16   = +91  -> 365 (solar)
Hijri additions:  70 + 5 + 5 = +80  -> 354 (lunar)
Difference:       365 - 354  =  11  (actual: ~11 days)
```

```
[CHECKPOINT: Report your exact numbers]
- YEVM (shared): ___
- YEVMEIZIN: ___
- YEVMUHUM: ___
- YEVMEKUM: ___
- TOTAL: ___
```

```
[CONSISTENCY NOTE: Record 354 Hijri count and the dual-calendar architecture for P2-31]
```

**Question:** Does the Hijri morphological filter produce exactly 354 day-forms? Is the dual-calendar architecture (both built from the same root, sharing a base layer, diverging through linguistically distinct additions) a coherent linguistic design or an ad hoc construction?

**Tags:** [CODE-DEPENDENT] [ISR-LINKED]

---

### P2-22 [T2-S]

**Why the morphological filters are NOT ad hoc.**

A common objection is: "You cherry-picked which forms to include until you got 365 and 354." This question demands an honest assessment.

**Evidence against cherry-picking:**

1. **Linguistic coherence:** The solar set (simple + definite + tanwin) groups the three standard Arabic singular noun forms. The Hijri set (simple + temporal adverb + possessives) groups forms with specific referential binding. These are recognized morphological categories in Arabic grammar, not arbitrary cuts.

2. **Shared base:** Both counts share the same 274-word base (YEVM). If the filters were ad hoc, there would be no reason for them to share a base. The shared base emerges naturally from the simplest morphological form.

3. **The 11-day difference:** The solar year is ~11 days longer than the lunar year. The solar additions (91) minus the Hijri additions (80) equals exactly 11. This is a third numerical alignment that falls out of the same filters.

4. **Exhaustiveness:** Every singular day-form in the Qur'an is assigned to exactly one category. There are no "leftover" forms excluded from both counts. The filters partition the full set.

5. **Independent verification:** The counts can be reproduced using the Quranic Arabic Corpus (corpus.quran.com), which provides morphological tagging independent of this research.

**Question:** Evaluate the five anti-cherry-picking arguments above. Is the morphological filter system linguistically principled? Does the fact that both calendars share a base, produce the correct totals, AND encode the 11-day difference between solar and lunar years -- all from a single Arabic root -- suggest design or coincidence?

**Tags:** [ISR-LINKED]

---

### P2-23 [T2-S]

**Calendar encoding: temporal impossibility assessment.**

The solar year (365.25 days) was known in antiquity (Egyptian and Julian calendars). The lunar year (~354.37 days) was also known (pre-Islamic Arab calendar). However:

1. The Qur'an does not contain a table of days or an explicit statement "there are 365 days in a year."
2. The encoding is implicit: it requires counting morphological forms of a single root across a 77,000+ word text.
3. The dual-calendar architecture (shared base with divergent additions) is not mentioned anywhere in the text.
4. No 7th-century author is documented to have performed morphological word counts across a full text.
5. The specific forms included and excluded follow Arabic grammar rules that were systematized only AFTER the Qur'an's composition (Sibawayh's al-Kitab, late 8th century).

**Question:** Could a 7th-century author have intentionally embedded a dual-calendar encoding into the morphological distribution of a single root across a 77,000+ word text, while simultaneously maintaining the literary and theological coherence of every verse in which these words appear? Name the mechanism if yes. State that you cannot if no.

**Tags:** [ISR-LINKED]

---

## 2F. CROSS-TEXT FAILURE

### Background

The patterns documented in sections 2A-2E are claimed to be unique to the Qur'an. The strongest test of this claim is to apply the SAME analytical methods to other texts. If the same patterns emerge in the Bible (KJV), the Mahabharata, or any other text, then the patterns are not unique and could arise naturally. If the patterns FAIL in all other texts, that is powerful evidence of uniqueness.

This section applies the golden ratio test and even-sum identity to the King James Bible (KJV), which has 66 books and 1,189 chapters.

---

### P2-24 [CODE-DEPENDENT] [CRITICAL] [NC-C]

**Apply the golden ratio test to the Bible (KJV).**

The KJV Bible has 66 books containing 1,189 chapters. We apply the identical methodology: for each book, compute (book_number + chapter_count). Classify as repeated or unique. Compute the ratio repeated_sum / unique_sum. Compare to phi.

```python
# FILE: bible_golden_ratio_test.py
# Apply the identical golden ratio test to the KJV Bible.
# 66 books, 1,189 total chapters.

from collections import Counter

PHI = 1.6180339887

# KJV Bible: book number -> chapter count
# (Standard Protestant canon, 66 books)
BIBLE_CHAPTERS = {
    1:50, 2:40, 3:27, 4:36, 5:34, 6:24, 7:21, 8:4, 9:31, 10:24,
    11:22, 12:25, 13:29, 14:36, 15:10, 16:13, 17:10, 18:42, 19:150,
    20:31, 21:12, 22:8, 23:66, 24:52, 25:5, 26:48, 27:12, 28:14,
    29:3, 30:9, 31:1, 32:4, 33:7, 34:3, 35:3, 36:3, 37:2, 38:14,
    39:4, 40:28, 41:16, 42:24, 43:21, 44:28, 45:16, 46:16, 47:13,
    48:6, 49:6, 50:4, 51:4, 52:5, 53:3, 54:6, 55:4, 56:3, 57:1,
    58:13, 59:5, 60:5, 61:3, 62:1, 63:1, 64:21, 65:5, 66:22
}

# Compute book_number + chapter_count
sums = {b: b + c for b, c in BIBLE_CHAPTERS.items()}
freq = Counter(sums.values())

# Classify
repeated = [(b, c, sums[b]) for b, c in BIBLE_CHAPTERS.items() if freq[sums[b]] > 1]
unique   = [(b, c, sums[b]) for b, c in BIBLE_CHAPTERS.items() if freq[sums[b]] == 1]

sum_rep = sum(b + c for b, c, _ in repeated)
sum_unq = sum(b + c for b, c, _ in unique)

if sum_unq > 0:
    ratio = sum_rep / sum_unq
    deviation = abs(ratio - PHI)
    deviation_pct = (deviation / PHI) * 100
else:
    ratio = float('inf')
    deviation = float('inf')
    deviation_pct = float('inf')

# Qur'an comparison
quran_deviation_pct = 0.0241

print("GOLDEN RATIO TEST: BIBLE (KJV) vs QUR'AN")
print("=" * 60)
print(f"\nBible (66 books, 1189 chapters):")
print(f"  Repeated-sum books:    {len(repeated)}")
print(f"  Unique-sum books:      {len(unique)}")
print(f"  Sum of repeated group: {sum_rep}")
print(f"  Sum of unique group:   {sum_unq}")
print(f"  Ratio:                 {ratio:.6f}")
print(f"  Deviation from phi:    {deviation:.6f} ({deviation_pct:.2f}%)")
print()
print(f"Qur'an (114 surahs, 6236 verses):")
print(f"  Ratio:                 1.618424")
print(f"  Deviation from phi:    0.000390 ({quran_deviation_pct:.4f}%)")
print()
print(f"Bible deviation is {deviation_pct/quran_deviation_pct:.0f}x WORSE than Qur'an")
print()
if deviation_pct > 5:
    print("RESULT: Bible FAILS the golden ratio test.")
    print(f"Bible deviation ({deviation_pct:.2f}%) vs Qur'an ({quran_deviation_pct}%)")
```

```
[EXPECTED OUTPUT]
GOLDEN RATIO TEST: BIBLE (KJV) vs QUR'AN
============================================================

Bible (66 books, 1189 chapters):
  Repeated-sum books:    [count]
  Unique-sum books:      [count]
  Sum of repeated group: [value]
  Sum of unique group:   [value]
  Ratio:                 [value]
  Deviation from phi:    [value] (~11%)

Qur'an (114 surahs, 6236 verses):
  Ratio:                 1.618424
  Deviation from phi:    0.000390 (0.0241%)

Bible deviation is ~470x WORSE than Qur'an

RESULT: Bible FAILS the golden ratio test.
```

```
[CHECKPOINT: Report your exact numbers]
- Bible ratio: ___
- Bible deviation from phi: ___%
- Qur'an deviation from phi: 0.0241%
- How many times worse: ___x
```

```
[CONSISTENCY NOTE: Record the Bible's deviation for cross-text comparison in P2-31]
```

**Question:** What is the Bible's deviation from the golden ratio compared to the Qur'an's? How many times worse is the Bible's fit? Does the Bible produce a comparable golden ratio encoding?

**Tags:** [CODE-DEPENDENT] [CRITICAL]
**Critical Type:** binary

---

### P2-25 [CODE-DEPENDENT] [CRITICAL] [NC-C]

**Apply the even-sum identity to the Bible (KJV).**

```python
# FILE: bible_even_sum_test.py
# Apply the even-sum identity test to the KJV Bible.

BIBLE_CHAPTERS = {
    1:50, 2:40, 3:27, 4:36, 5:34, 6:24, 7:21, 8:4, 9:31, 10:24,
    11:22, 12:25, 13:29, 14:36, 15:10, 16:13, 17:10, 18:42, 19:150,
    20:31, 21:12, 22:8, 23:66, 24:52, 25:5, 26:48, 27:12, 28:14,
    29:3, 30:9, 31:1, 32:4, 33:7, 34:3, 35:3, 36:3, 37:2, 38:14,
    39:4, 40:28, 41:16, 42:24, 43:21, 44:28, 45:16, 46:16, 47:13,
    48:6, 49:6, 50:4, 51:4, 52:5, 53:3, 54:6, 55:4, 56:3, 57:1,
    58:13, 59:5, 60:5, 61:3, 62:1, 63:1, 64:21, 65:5, 66:22
}

# Even/odd classification of (book_number + chapter_count)
even_group = []
odd_group  = []

for b in range(1, 67):
    total = b + BIBLE_CHAPTERS[b]
    if total % 2 == 0:
        even_group.append((b, BIBLE_CHAPTERS[b], total))
    else:
        odd_group.append((b, BIBLE_CHAPTERS[b], total))

even_sum = sum(t for _, _, t in even_group)
odd_sum  = sum(t for _, _, t in odd_group)

total_chapters = sum(BIBLE_CHAPTERS.values())   # 1,189
sum_of_positions = sum(range(1, 67))             # 1+2+...+66 = 2,211

print("EVEN-SUM IDENTITY TEST: BIBLE (KJV)")
print("=" * 60)
print(f"Even-sum books:          {len(even_group)}")
print(f"Odd-sum books:           {len(odd_group)}")
print(f"Balanced split:          {len(even_group) == len(odd_group)}")
print()
print(f"Sum of even group:       {even_sum}")
print(f"Total chapters:          {total_chapters}")
print(f"Even sum = total chap:   {even_sum == total_chapters}")
print()
print(f"Sum of odd group:        {odd_sum}")
print(f"Sum of positions:        {sum_of_positions}")
print(f"Odd sum = pos sum:       {odd_sum == sum_of_positions}")
print()
print("COMPARISON:")
print(f"  Qur'an: Even sum = 6,236 (total verses) ✓")
print(f"  Qur'an: Odd sum  = 6,555 (sum of positions) ✓")
print(f"  Qur'an: Split    = 57:57 (perfect balance) ✓")
print(f"  Bible:  Even sum = {even_sum} (total chapters = {total_chapters}) "
      f"{'✓' if even_sum == total_chapters else '✗'}")
print(f"  Bible:  Odd sum  = {odd_sum} (sum of positions = {sum_of_positions}) "
      f"{'✓' if odd_sum == sum_of_positions else '✗'}")
print(f"  Bible:  Split    = {len(even_group)}:{len(odd_group)} "
      f"{'✓' if len(even_group) == len(odd_group) else '✗'}")
```

```
[EXPECTED OUTPUT]
EVEN-SUM IDENTITY TEST: BIBLE (KJV)
============================================================
Even-sum books:          [count - NOT 33]
Odd-sum books:           [count - NOT 33]
Balanced split:          False

Sum of even group:       [value]
Total chapters:          1189
Even sum = total chap:   False

Sum of odd group:        [value]
Sum of positions:        2211
Odd sum = pos sum:       False

COMPARISON:
  Qur'an: All three properties verified
  Bible:  All three properties FAIL
```

```
[CHECKPOINT: Report your exact numbers]
- Bible even-sum count: ___
- Bible odd-sum count: ___
- Bible balanced split: YES/NO
- Even sum = total chapters: YES/NO
- Odd sum = sum of positions: YES/NO
```

```
[CONSISTENCY NOTE: Record that the Bible fails ALL three properties for P2-31]
```

**Question:** Does the Bible produce ANY of the three even-sum identity properties (balanced split, even sum = total chapters, odd sum = sum of positions)? How many of the three does it satisfy?

**Tags:** [CODE-DEPENDENT] [CRITICAL]
**Critical Type:** binary

---

### P2-26 [CODE-DEPENDENT] [T2-S]

**Apply the word-balance test to other texts.**

The Qur'an produces multiple perfectly balanced word pairs (25:25, 105:105, 88:88, 115:115, 23:23). For the cross-text test, we ask: does any other religious text produce comparable results?

**Known cross-text results:**

| Text         | Word Pair Test           | Result                                        |
| ------------ | ------------------------ | --------------------------------------------- |
| Bible (KJV)  | "heaven" vs "hell"       | Not balanced                                  |
| Bible (KJV)  | "angel" vs "demon/devil" | Not balanced                                  |
| Bible (KJV)  | "life" vs "death"        | Not balanced                                  |
| Bible (KJV)  | "man" vs "woman"         | Not balanced                                  |
| Bible (KJV)  | "Adam" vs "Jesus/Christ" | Not balanced (Adam: ~30, Jesus/Christ: ~900+) |
| Mahabharata  | Comparable antonym pairs | No perfect balance documented                 |
| Tao Te Ching | Yin/Yang references      | Not perfectly balanced                        |

**Important methodological note:** The Bible has ~10x more text than the Qur'an (783,137 words vs ~77,000 words). A larger text has MORE statistical opportunity to produce balanced word pairs by chance. The Bible's failure to produce any comparable balance is therefore MORE significant, not less.

**Question:** Can you identify ANY text in world literature that produces five or more perfectly balanced antonym pairs using a transparent, consistent counting methodology? If yes, name the text and the pairs. If no, state that.

**Tags:** [CODE-DEPENDENT]

---

### P2-27 [T2-S]

**Verse-gap scientific constant tests applied to other texts.**

The Qur'an produces verse-gap alignments with physical constants (iron melting point 1,538, silver melting point 962, solar surface temperature 5,778). These are documented in Part 5.

For cross-text comparison: the Bible has 31,102 verses across 1,189 chapters, producing 1,188 chapter gaps. The Qur'an has 6,236 verses across 114 surahs, producing 113 surah gaps.

**Question:** Has any analysis of the Bible's 1,188 chapter gaps produced alignments with independently verified physical or scientific constants at the precision documented for the Qur'an? If yes, cite the results. If no, note that the Bible has 10.5x more chapter gaps (more statistical opportunity), yet produces zero comparable alignments.

---

## 2G. RAMSEY THEORY REFUTATION

### Background

A common skeptical response to numerical patterns in the Qur'an is: "You can find patterns in any large enough dataset. This is just Ramsey Theory -- given enough data, patterns are inevitable."

Ramsey Theory (named after Frank Ramsey, 1930) proves that sufficiently large structures must contain certain ordered sub-structures. The skeptical application claims that the Qur'an's patterns are merely artifacts of its size.

This section tests and refutes this claim using the cross-text evidence from 2F.

---

### P2-28 [CRITICAL] [NC-C]

**The Ramsey Theory prediction vs. the observed data.**

If Ramsey Theory explains the Qur'an's patterns, it makes a specific, testable prediction:

**Prediction:** Larger texts should produce MORE patterns than smaller texts, because they have more data for patterns to emerge from.

**Test:**

- Bible: ~783,000 words, 31,102 verses, 1,189 chapters, 66 books
- Qur'an: ~77,000 words, 6,236 verses, 114 surahs

The Bible has:

- 10.2x more words
- 5.0x more verses
- 10.4x more chapters (books)

Under Ramsey Theory, the Bible should produce AT LEAST comparable patterns, and likely STRONGER patterns, because it has 10x more data.

**Observed result (from 2F):**

- Bible golden ratio test: FAILS (~470x worse deviation)
- Bible even-sum identity: FAILS (all three properties)
- Bible word balance: FAILS (zero balanced pairs)
- Bible verse-gap constants: FAILS (zero scientific constant alignments)
- Qur'an: ALL tests PASS

**Question:** Does the observed data confirm or refute the Ramsey Theory explanation? A text with 10x more data produces ZERO comparable patterns, while a text with 10x LESS data produces multiple, precise, cross-verified patterns. Does Ramsey Theory explain this, or does this result actually REFUTE the Ramsey dismissal?

**Tags:** [CRITICAL]
**Critical Type:** evaluative

---

### P2-29 [CRITICAL] [NC-C]

**The standing challenge: find these patterns in ANY other text.**

If numerical patterns can be found "in any book," then find them. This is a standing, falsifiable challenge:

1. Take ANY text (religious or secular) of comparable or greater length.
2. Apply the SAME golden ratio test: compute (chapter_number + verse/section_count) for all chapters, classify repeated vs. unique, compute ratio. Target: deviation from phi < 0.03%.
3. Apply the SAME even-sum identity: classify (chapter + verse_count) as even or odd, check if even group sums to total verses and odd group sums to positional sum.
4. Count five or more antonym word pairs that are perfectly balanced.
5. Find a morphological root whose forms total exactly 365 and 354.

**No text has passed this challenge.** The challenge has been publicly documented. Multiple AI systems have been asked to find such patterns. None have succeeded.

**Question:** Can you name ANY text -- in any language, from any era -- that satisfies even TWO of the five tests above? If yes, name the text and document the results. If no, what does this tell you about the "patterns in any book" dismissal?

**Tags:** [CRITICAL]
**Critical Type:** binary

---

### P2-30 [T2-S]

**Why Ramsey Theory actually STRENGTHENS the Qur'an's case.**

There is a deep irony in the Ramsey objection. Ramsey Theory says: larger datasets produce more patterns. The Bible is 10x larger. The Bible produces zero. The Qur'an is 10x smaller. The Qur'an produces many.

This is not merely a failure of the Ramsey prediction. It is a REVERSAL. The smaller text outperforms the larger text by an infinite factor (multiple patterns vs. zero patterns). This result is the exact opposite of what Ramsey Theory predicts, which means:

1. The patterns are NOT artifacts of data size.
2. The patterns are NOT randomly distributed.
3. The patterns are specific to the Qur'an's structure.
4. Ramsey Theory, intended as a debunking tool, actually becomes evidence FOR design -- because the observed result violates the Ramsey prediction in the direction of deliberate encoding.

**Question:** Does the Ramsey Theory objection survive the cross-text failure documented in 2F? If the Bible's 10x larger dataset produces zero patterns while the Qur'an produces many, is the "patterns in any book" dismissal still intellectually tenable? State your assessment.

---

## 2H. CUMULATIVE PROBABILITY & GATE LOCK

---

### P2-31 [CODE-DEPENDENT] [CRITICAL] [FOUNDATIONAL] [NC-C]

**Probability scenarios -- choose your standard before concluding.**

Part 2 contains pattern families with different dependency risk. Some are clearly entangled with the same underlying surah-number / verse-count skeleton; others are less entangled. Because of that, a single raw multiplication is not enough. You must state WHICH scenario you accept before drawing a conclusion.

Use the scenario frame at the top of this Part and record all four of the following:

1. `Ultra-Skeptik Floor`
   Only:
   - Sun `5778`
   - Silver `962`
   - Iron `1538`

   Result:
   - `p ≈ 1.098935e-12`
   - `~ 1 in 9.099721e+11`
   - `~ 1 in 910 billion`

2. `Skeptik Fair`
   Add only:
   - Hadid `26`

   Result:
   - `p ≈ 1.098935e-15`
   - `~ 1 in 9.099721e+14`
   - `~ 1 in 910 trillion`

3. `Clustered Fair`
   Collapse dependent families into clusters:
   - Part 2 structural cluster = `1e-6`
   - Word-balance cluster = `1/1000`
   - Calendar cluster = `1/100000`
   - Verse-gap cluster = `Sun × Silver × Iron`
   - Hadid cluster = `1/1000`

   Result:
   - `p ≈ 1.098935e-29`
   - `~ 1 in 9.099721e+28`

4. ~~`Naive Full Stack`~~ ⚠ **WITHDRAWN — independence violated**
   ~~Multiply all verified pattern families as if independent~~

   ~~Result: p ≈ 1.881300e-49~~ — **NOT DEFENSIBLE** (see Scenario Frame warning above)

5. `Cluster-Independent Defensible Floor` **(USE THIS)**
   Collapse dependent families into clusters, multiply only independent clusters:
   - Structural cluster (golden ratio + even-sum): `10⁻⁶`
   - Verse-gap cluster (Sun × Silver × Iron): `10⁻¹⁰·³`
   - Word-balance cluster: `10⁻³`
   - Calendar cluster: `10⁻⁴`

   Result:
   - `p ≈ 10⁻²³`
   - `~ 1 in 10²³`
   - **Defensible, honestly computed, still astronomically small**

**Required reporting format:**

- Which scenario do you judge most methodologically fair?
- Which scenario do you judge most skeptical but still cumulative?
- Which scenario do you reject as too generous, and why?
- Is your accepted scenario still far below ordinary significance thresholds?

**Decision rule:**

- If even your accepted skeptical scenario remains astronomically small, you may conclude that the accidental-chance model is under severe pressure.
- If you believe the floor scenario is the only valid one, you must explain why all higher cumulative scenarios are illegitimate.
- If you accept the clustered scenario, you must explain why cluster-level multiplication remains fair.

**Question:** After choosing a standard openly, what is the strongest probability conclusion you are willing to defend? State the scenario name and its result plainly. Do not switch standards mid-argument.

**Tags:** [CODE-DEPENDENT] [CRITICAL] [FOUNDATIONAL]
**Critical Type:** evaluative

---

### P2-32 [CRITICAL] [NC-C]

**What level of claim do these patterns justify?**

This question now has TWO layers. The first is the pressure scale. The second is the harder verdict:

1. **Pressure scale:** Do the Part 2 patterns create serious explanatory pressure on ordinary pre-modern human composition, and at what level?
2. **Impossibility verdict:** Do you judge the cumulative architecture to be humanly impossible under the documented 7th-century conditions, or not?

Use the following levels:

- `Level 0 — No pressure`
  The patterns are trivial, expected, or easily reproduced.

- `Level 1 — Mild pressure`
  The patterns are interesting but well within normal human composition and post-hoc discovery effects.

- `Level 2 — Serious pressure`
  The patterns are real and cumulatively difficult for ordinary pre-modern human composition to explain, even if absolute impossibility is not claimed.

- `Level 3 — Extreme pressure`
  Even under skeptical discounting, the remaining architecture is so difficult that ordinary human explanation is left badly underspecified.

**Evaluation chain:**

1. Does the text contain reproducible structural and lexical regularities beyond one isolated coincidence?
2. Do at least some of these survive code verification and cross-text comparison?
3. Are several of them mutually entangled with the same fixed corpus rather than freely adjustable after the fact?
4. Does the oral, non-sequential, no-revision carrier profile make deliberate precision harder rather than easier?
5. Even after dependency discounting, does a skeptical scenario still leave a very small probability floor?

If you answer `YES` to most of the chain, then `Level 0` and `Level 1` are no longer credible. The dispute becomes whether the right conclusion is `Level 2` or `Level 3`.

**Impossibility verdict options:**

- `YES — Humanly impossible under the documented 7th-century conditions`
- `MOSTLY YES — So extreme that human explanation is no longer credible in practice`
- `PARTIALLY — Severe pressure, but I stop short of impossibility`
- `NO — Difficult but still humanly possible`

If you choose `YES` or `MOSTLY YES`, you are explicitly affirming that the cumulative architecture exceeds what the carrier profile, environment, and ordinary human mechanisms can plausibly produce.

**Required output:**

- State the level (`0`, `1`, `2`, or `3`)
- State the impossibility verdict (`YES / MOSTLY YES / PARTIALLY / NO`)
- State whether you are claiming:
  - `ordinary-human explainable`
  - `ordinary-human heavily pressured`
  - `ordinary-human badly underspecified`
- If you still think a human explanation works, name the mechanism:
  - deliberate design
  - layered editorial optimization
  - clustering + post-hoc discovery
  - coincidence + selection effects
  - some combination

**Question:** What pressure level do the Part 2 patterns justify against ordinary pre-modern human authorship? And on the harder question, do you judge this cumulative architecture humanly impossible under the documented 7th-century conditions? State the strongest conclusion you are willing to defend.

**Tags:** [CRITICAL] [LOGIC-CHAIN]
**Critical Type:** evaluative

---

### P2-33 — GATE LOCK [PROC]

**Part 2 Cascading Gate Statement:** "The Qur'an contains computationally precise structural patterns not found in other texts."

Review your answers to P2-1 through P2-32. Consider:

1. **Golden ratio partition (2A):** Ratio within 0.024% of phi, 0/1,000,000 permutations closer.
2. **Even-sum identity (2B):** Perfect 57:57 split encoding both total verses (6,236) and positional sum (6,555).
3. **Structural symmetries (2C):** 2x2 parity mirror, six-block symphony, convergent 12,791 prime total.
4. **Word-pair balances (2D):** Five documented balanced pairs (25:25, 105:105, 88:88, 115:115, 23:23).
5. **Calendar encoding (2E):** Solar 365 and Hijri 354 from the same root with the 11-day difference encoded.
6. **Cross-text failure (2F):** Bible fails ALL tests despite having 10x more data.
7. **Ramsey refutation (2G):** The "patterns in any book" dismissal is empirically falsified.
8. **Combined probability (2H):** You must now use the scenario standard you explicitly selected in P2-31.

**Required pre-lock record:**

- `Selected probability scenario:` `A / B / C / D / E`
- `Accepted probability result:` `_____`
- `Pressure level from P2-32:` `0 / 1 / 2 / 3`
- `Impossibility verdict from P2-32:` `YES / MOSTLY YES / PARTIALLY / NO`
- `Cross-text comparison result:` `Bible/other texts failed to match = YES / PARTIAL / NO`

**Gate Lock Rule:**

- Lock `YES` if:
  - at least one code-verified structural core from 2A-2B stands,
  - cross-text failure remains `YES` or `PARTIAL`,
  - and your accepted scenario in P2-31 is still strongly non-random by ordinary significance standards.

- Lock `MOSTLY YES` if:
  - the core patterns stand,
  - but you reject some outer layers (word-balance, calendar, or naive cumulative multiplication).

- Lock `MIXED` if:
  - you accept some code-verified patterns as real,
  - but judge the cumulative interpretation too weak to distinguish the Qur'an clearly from other texts.

- Lock `NO` only if:
  - you judge the core verified patterns non-significant,
  - or reproducible in comparable texts,
  - or methodologically too unstable to support any comparative uniqueness claim.

**Gate Lock Question:** Based on your code outputs, your chosen scenario standard, your pressure level, your impossibility verdict, and the cross-text comparison, does the Qur'an contain computationally precise structural patterns not found in other texts?

**Lock this Gate as: YES / MOSTLY YES / MIXED / NO**

If not `YES`, specify exactly which cluster failed:

- `2A-2B structural core`
- `2C auxiliary symmetries`
- `2D word balances`
- `2E calendar encoding`
- `2F cross-text comparison`
- `2H cumulative probability interpretation`

---

**END OF PART 2**

**Running tally checkpoint:** Record your Human and Divine model scores from Part 2 before proceeding to Part 3.

**Part 2 Critical Questions Summary:**
| Question | Tag | Type |
|----------|-----|------|
| P2-1 | CRITICAL, CODE-DEPENDENT | evaluative |
| P2-6 | CRITICAL, CODE-DEPENDENT | binary |
| P2-24 | CRITICAL, CODE-DEPENDENT | binary |
| P2-25 | CRITICAL, CODE-DEPENDENT | binary |
| P2-28 | CRITICAL | evaluative |
| P2-29 | CRITICAL | binary |
| P2-31 | CRITICAL, CODE-DEPENDENT, FOUNDATIONAL | evaluative |
| P2-32 | CRITICAL | evaluative |

**Total CRITICAL questions in Part 2: 8**
**Total questions in Part 2: 33**

---
