#!/usr/bin/env python3
"""
Statistical Testing for All Patterns
=====================================
Runs permutation tests for all 18 patterns in new_search folder.
Calculates p-values to determine statistical significance.
"""

import random
from pathlib import Path
from collections import Counter
import math

# Number of permutation trials
N_TRIALS = 100_000

def load_quran_data():
    """Load Quran data from file"""
    current_dir = Path(__file__).parent
    for _ in range(6):
        potential_path = current_dir / "data" / "quran-uthmani.txt"
        if potential_path.exists():
            data_path = potential_path
            break
        current_dir = current_dir.parent
    else:
        raise FileNotFoundError("data/quran-uthmani.txt not found")

    verses = {}
    with data_path.open('r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#') or '|' not in line:
                continue
            parts = line.split('|', 2)
            if len(parts) >= 3:
                surah = int(parts[0])
                verses.setdefault(surah, []).append(int(parts[1]))
    return {s: len(v) for s, v in verses.items()}

def is_prime_book(n):
    """Book considers 1 as prime"""
    if n == 1:
        return True
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_divisors(n):
    divs = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divs.append(i)
            if i != n // i:
                divs.append(n // i)
    return sorted(divs)

def proper_divisor_sum(n):
    if n <= 1:
        return 0
    return sum(d for d in get_divisors(n) if d < n)

def prime_factor_sum(n):
    if n == 1:
        return 1
    total = 0
    temp = n
    d = 2
    while d * d <= temp:
        while temp % d == 0:
            total += d
            temp //= d
        d += 1
    if temp > 1:
        total += temp
    return total

def count_primes_in_divisors(n):
    divisors = get_divisors(n)
    return sum(1 for d in divisors if is_prime_book(d))

# ============================================================
# PATTERN TEST FUNCTIONS
# ============================================================

def test_01_homogeneous_half_symmetry(positions, verses):
    """Test for 28/29/29/28 mirror symmetry"""
    homo_first = 0
    homo_second = 0
    hetero_first = 0
    hetero_second = 0

    for i, (p, v) in enumerate(zip(positions, verses)):
        same_parity = (p % 2) == (v % 2)
        first_half = p <= 57

        if same_parity and first_half:
            homo_first += 1
        elif same_parity and not first_half:
            homo_second += 1
        elif not same_parity and first_half:
            hetero_first += 1
        else:
            hetero_second += 1

    # Measure: how close to mirror symmetry (28/29/29/28)?
    # Perfect symmetry: homo_first == hetero_second AND homo_second == hetero_first
    diff = abs(homo_first - hetero_second) + abs(homo_second - hetero_first)
    return diff

def test_02_verses_less_than_position(positions, verses):
    """Test for 34/32/32/34 symmetry"""
    diff_odd = 0
    diff_even = 0
    pos_odd = 0
    pos_even = 0

    for p, v in zip(positions, verses):
        if v < p:
            diff = v - p
            if diff % 2 != 0:
                diff_odd += 1
            else:
                diff_even += 1
            if p % 2 != 0:
                pos_odd += 1
            else:
                pos_even += 1

    # Mirror symmetry score
    score = abs(diff_odd - pos_even) + abs(diff_even - pos_odd)
    return score

def test_05_div_2_not_3(positions, verses):
    """Test for 33/33/24/24 symmetry"""
    def has_prop(n):
        return n % 2 == 0 and n % 3 != 0

    homo_first = homo_second = hetero_first = hetero_second = 0

    for p, v in zip(positions, verses):
        same = has_prop(p) == has_prop(v)
        first_half = p <= 57

        if same and first_half:
            homo_first += 1
        elif same:
            homo_second += 1
        elif first_half:
            hetero_first += 1
        else:
            hetero_second += 1

    # Perfect symmetry: homo_first == homo_second AND hetero_first == hetero_second
    score = abs(homo_first - homo_second) + abs(hetero_first - hetero_second)
    return score

def test_06_div_3_not_2(positions, verses):
    """Test for 42/42/15/15 symmetry"""
    def has_prop(n):
        return n % 3 == 0 and n % 2 != 0

    homo_first = homo_second = hetero_first = hetero_second = 0

    for p, v in zip(positions, verses):
        same = has_prop(p) == has_prop(v)
        first_half = p <= 57

        if same and first_half:
            homo_first += 1
        elif same:
            homo_second += 1
        elif first_half:
            hetero_first += 1
        else:
            hetero_second += 1

    score = abs(homo_first - homo_second) + abs(hetero_first - hetero_second)
    return score

def test_07_prime_factor_sum(positions, verses):
    """Test for 71/71 and 43/43 symmetry"""
    pfs_verse_odd = sum(1 for v in verses if prime_factor_sum(v) % 2 != 0)
    pfs_pos_odd = sum(1 for p in positions if prime_factor_sum(p) % 2 != 0)
    pfs_verse_even = sum(1 for v in verses if prime_factor_sum(v) % 2 == 0)
    pfs_pos_even = sum(1 for p in positions if prime_factor_sum(p) % 2 == 0)

    score = abs(pfs_verse_odd - pfs_pos_odd) + abs(pfs_verse_even - pfs_pos_even)
    return score

def test_09_abundant(positions, verses):
    """Test for 14/14 and 43/43 symmetry"""
    def is_abundant(n):
        return proper_divisor_sum(n) > n

    ab_odd = sum(1 for p, v in zip(positions, verses) if is_abundant(v) and p % 2 != 0)
    ab_even = sum(1 for p, v in zip(positions, verses) if is_abundant(v) and p % 2 == 0)
    not_ab_odd = sum(1 for p, v in zip(positions, verses) if not is_abundant(v) and p % 2 != 0)
    not_ab_even = sum(1 for p, v in zip(positions, verses) if not is_abundant(v) and p % 2 == 0)

    score = abs(ab_odd - ab_even) + abs(not_ab_odd - not_ab_even)
    return score

def test_10_deficient(positions, verses):
    """Test for 41/41 and 16/16 symmetry"""
    def is_deficient(n):
        if n == 1:
            return True
        return proper_divisor_sum(n) < n

    def_odd = sum(1 for p, v in zip(positions, verses) if is_deficient(v) and p % 2 != 0)
    def_even = sum(1 for p, v in zip(positions, verses) if is_deficient(v) and p % 2 == 0)
    not_def_odd = sum(1 for p, v in zip(positions, verses) if not is_deficient(v) and p % 2 != 0)
    not_def_even = sum(1 for p, v in zip(positions, verses) if not is_deficient(v) and p % 2 == 0)

    score = abs(def_odd - def_even) + abs(not_def_odd - not_def_even)
    return score

def test_12_long_short(positions, verses):
    """Test for 57/57 split and 27/30/30/27 symmetry"""
    long_count = sum(1 for v in verses if v > 39)
    short_count = sum(1 for v in verses if v < 39)

    long_odd = sum(1 for p, v in zip(positions, verses) if v > 39 and p % 2 != 0)
    long_even = sum(1 for p, v in zip(positions, verses) if v > 39 and p % 2 == 0)
    short_odd = sum(1 for p, v in zip(positions, verses) if v < 39 and p % 2 != 0)
    short_even = sum(1 for p, v in zip(positions, verses) if v < 39 and p % 2 == 0)

    # 57/57 + mirror symmetry
    score = abs(long_count - short_count) + abs(long_odd - short_even) + abs(long_even - short_odd)
    return score

def test_14_divisor_count_2(positions, verses):
    """Test for 33/33/24/24 symmetry"""
    def has_2_divisors(n):
        return len(get_divisors(n)) == 2

    homo_first = homo_second = hetero_first = hetero_second = 0

    for p, v in zip(positions, verses):
        same = has_2_divisors(p) == has_2_divisors(v)
        first_half = p <= 57

        if same and first_half:
            homo_first += 1
        elif same:
            homo_second += 1
        elif first_half:
            hetero_first += 1
        else:
            hetero_second += 1

    score = abs(homo_first - homo_second) + abs(hetero_first - hetero_second)
    return score

def test_16_golden_ratio(positions, verses):
    """Test for golden ratio approximation"""
    PHI = 1.6180339887

    sums = [p + v for p, v in zip(positions, verses)]
    sum_counts = Counter(sums)

    sum_repeated = sum(s for s in sums if sum_counts[s] > 1)
    sum_unique = sum(s for s in sums if sum_counts[s] == 1)

    if sum_unique == 0:
        return float('inf')

    ratio = sum_repeated / sum_unique
    return abs(ratio - PHI)

def test_17_two_prime_divisors(positions, verses):
    """Test for 24/24/33/33 symmetry"""
    def has_two_primes(n):
        return count_primes_in_divisors(n) == 2

    homo_first = homo_second = hetero_first = hetero_second = 0

    for p, v in zip(positions, verses):
        same = has_two_primes(p) == has_two_primes(v)
        first_half = p <= 57

        if same and first_half:
            homo_first += 1
        elif same:
            homo_second += 1
        elif first_half:
            hetero_first += 1
        else:
            hetero_second += 1

    score = abs(homo_first - homo_second) + abs(hetero_first - hetero_second)
    return score

def test_18_three_prime_divisors(positions, verses):
    """Test for 25/25/32/32 symmetry"""
    def has_three_primes(n):
        return count_primes_in_divisors(n) == 3

    homo_first = homo_second = hetero_first = hetero_second = 0

    for p, v in zip(positions, verses):
        same = has_three_primes(p) == has_three_primes(v)
        first_half = p <= 57

        if same and first_half:
            homo_first += 1
        elif same:
            homo_second += 1
        elif first_half:
            hetero_first += 1
        else:
            hetero_second += 1

    score = abs(homo_first - homo_second) + abs(hetero_first - hetero_second)
    return score

# ============================================================
# MAIN RUNNER
# ============================================================

def run_permutation_test(test_func, positions, verses, n_trials=N_TRIALS):
    """Run permutation test and return p-value"""
    # Calculate observed statistic
    observed = test_func(positions, verses)

    # Run permutations
    count_as_good_or_better = 0
    verse_list = list(verses)

    for _ in range(n_trials):
        shuffled = verse_list.copy()
        random.shuffle(shuffled)
        stat = test_func(positions, shuffled)
        if stat <= observed:  # Lower score = better symmetry
            count_as_good_or_better += 1

    p_value = count_as_good_or_better / n_trials
    return observed, p_value

def main():
    print("=" * 70)
    print("STATISTICAL TESTING FOR ALL PATTERNS")
    print(f"Permutation trials: {N_TRIALS:,}")
    print("=" * 70)
    print()

    # Load data
    vc = load_quran_data()
    positions = list(range(1, 115))
    verses = [vc[s] for s in positions]

    # Define tests
    tests = [
        ("01 Homogeneous Half Symmetry (28/29/29/28)", test_01_homogeneous_half_symmetry),
        ("02 Verses < Position (34/32/32/34)", test_02_verses_less_than_position),
        ("05 Divisible by 2 not 3 (33/33/24/24)", test_05_div_2_not_3),
        ("06 Divisible by 3 not 2 (42/42/15/15)", test_06_div_3_not_2),
        ("07 Prime Factor Sum (71/71, 43/43)", test_07_prime_factor_sum),
        ("09 Abundant Numbers (14/14, 43/43)", test_09_abundant),
        ("10 Deficient Numbers (41/41, 16/16)", test_10_deficient),
        ("12 Long/Short Surahs (57/57, 27/30/30/27)", test_12_long_short),
        ("14 Divisor Count = 2 (33/33/24/24)", test_14_divisor_count_2),
        ("16 Golden Ratio (φ ≈ 1.618)", test_16_golden_ratio),
        ("17 Two Prime Divisors (24/24/33/33)", test_17_two_prime_divisors),
        ("18 Three Prime Divisors (25/25/32/32)", test_18_three_prime_divisors),
    ]

    results = []

    for name, test_func in tests:
        print(f"Testing: {name}...", end=" ", flush=True)
        observed, p_value = run_permutation_test(test_func, positions, verses)

        if p_value < 0.01:
            status = "★★★ HIGHLY SIGNIFICANT"
        elif p_value < 0.05:
            status = "★★ SIGNIFICANT"
        elif p_value < 0.10:
            status = "★ MARGINAL"
        else:
            status = "NOT SIGNIFICANT"

        print(f"p = {p_value:.4f} ({status})")
        results.append((name, observed, p_value, status))

    print()
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print()
    print(f"{'Pattern':<50} {'p-value':<12} {'Status'}")
    print("-" * 70)

    for name, observed, p_value, status in results:
        print(f"{name:<50} {p_value:<12.4f} {status}")

    print()
    significant = sum(1 for _, _, p, _ in results if p < 0.05)
    print(f"Significant patterns (p < 0.05): {significant} / {len(results)}")

    return results

if __name__ == "__main__":
    random.seed(42)  # For reproducibility
    main()
