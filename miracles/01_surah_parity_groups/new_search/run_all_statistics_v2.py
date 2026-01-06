#!/usr/bin/env python3
"""
Statistical Testing for All Patterns - Version 2
=================================================
Improved tests with better metrics and all patterns included.
"""

import random
from pathlib import Path
from collections import Counter
import math

N_TRIALS = 100_000

def load_quran_data():
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
    if n == 1:
        return True
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_prime_standard(n):
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

PHI = 1.6180339887

# ============================================================
# IMPROVED TEST FUNCTIONS
# ============================================================

def test_01_symmetry(positions, verses):
    """28/29/29/28 mirror symmetry - measure deviation from perfect mirror"""
    homo_first = homo_second = hetero_first = hetero_second = 0
    for p, v in zip(positions, verses):
        same = (p % 2) == (v % 2)
        first = p <= 57
        if same and first: homo_first += 1
        elif same: homo_second += 1
        elif first: hetero_first += 1
        else: hetero_second += 1
    # Perfect mirror: a/b/b/a pattern
    return abs(homo_first - hetero_second) + abs(homo_second - hetero_first)

def test_02_symmetry(positions, verses):
    """34/32/32/34 mirror symmetry"""
    diff_odd = diff_even = pos_odd = pos_even = 0
    for p, v in zip(positions, verses):
        if v < p:
            diff = v - p
            if diff % 2 != 0: diff_odd += 1
            else: diff_even += 1
            if p % 2 != 0: pos_odd += 1
            else: pos_even += 1
    return abs(diff_odd - pos_even) + abs(diff_even - pos_odd)

def test_03_prime_totals(positions, verses):
    """12791 and 209029 both prime"""
    total_sum = sum(p + v for p, v in zip(positions, verses))
    product_sum = sum(p * v for p, v in zip(positions, verses))
    # Score: 0 if both prime, 1 if one prime, 2 if neither
    score = 0
    if not is_prime_standard(total_sum): score += 1
    if not is_prime_standard(product_sum): score += 1
    return score

def test_04_set_ops_32_32(positions, verses):
    """Odd∩Odd = 32, Even∩Even = 32"""
    odd_odd = sum(1 for p, v in zip(positions, verses) if p % 2 == 1 and v % 2 == 1)
    even_even = sum(1 for p, v in zip(positions, verses) if p % 2 == 0 and v % 2 == 0)
    return abs(odd_odd - even_even)

def test_04_set_ops_101_13(positions, verses):
    """101 in range, 13 out of range - both prime"""
    in_range = sum(1 for v in verses if 1 <= v <= 114)
    out_range = sum(1 for v in verses if v > 114)
    # Check if both counts are prime
    score = abs(in_range - 101) + abs(out_range - 13)
    if is_prime_standard(in_range) and is_prime_standard(out_range):
        score = 0  # Perfect
    return score

def test_05_equal_split(positions, verses):
    """33/33/24/24 equal halves"""
    def has_prop(n): return n % 2 == 0 and n % 3 != 0
    homo_first = homo_second = hetero_first = hetero_second = 0
    for p, v in zip(positions, verses):
        same = has_prop(p) == has_prop(v)
        first = p <= 57
        if same and first: homo_first += 1
        elif same: homo_second += 1
        elif first: hetero_first += 1
        else: hetero_second += 1
    return abs(homo_first - homo_second) + abs(hetero_first - hetero_second)

def test_06_equal_split(positions, verses):
    """42/42/15/15 equal halves"""
    def has_prop(n): return n % 3 == 0 and n % 2 != 0
    homo_first = homo_second = hetero_first = hetero_second = 0
    for p, v in zip(positions, verses):
        same = has_prop(p) == has_prop(v)
        first = p <= 57
        if same and first: homo_first += 1
        elif same: homo_second += 1
        elif first: hetero_first += 1
        else: hetero_second += 1
    return abs(homo_first - homo_second) + abs(hetero_first - hetero_second)

def test_07_pfs_symmetry(positions, verses):
    """71/71 and 43/43 - verse pfs parity matches position pfs parity counts"""
    v_odd = sum(1 for v in verses if prime_factor_sum(v) % 2 == 1)
    v_even = 114 - v_odd
    # Compare to position pfs (fixed: 71 odd, 43 even)
    return abs(v_odd - 71) + abs(v_even - 43)

def test_08_perfect_symmetry(positions, verses):
    """2/2 and 55/55 perfect number symmetry"""
    def is_perfect(n): return proper_divisor_sum(n) == n
    perf_odd = sum(1 for p, v in zip(positions, verses) if is_perfect(v) and p % 2 == 1)
    perf_even = sum(1 for p, v in zip(positions, verses) if is_perfect(v) and p % 2 == 0)
    not_perf_odd = sum(1 for p, v in zip(positions, verses) if not is_perfect(v) and p % 2 == 1)
    not_perf_even = sum(1 for p, v in zip(positions, verses) if not is_perfect(v) and p % 2 == 0)
    return abs(perf_odd - perf_even) + abs(not_perf_odd - not_perf_even)

def test_09_abundant_symmetry(positions, verses):
    """14/14 and 43/43 abundant symmetry"""
    def is_abundant(n): return proper_divisor_sum(n) > n
    ab_odd = sum(1 for p, v in zip(positions, verses) if is_abundant(v) and p % 2 == 1)
    ab_even = sum(1 for p, v in zip(positions, verses) if is_abundant(v) and p % 2 == 0)
    not_ab_odd = sum(1 for p, v in zip(positions, verses) if not is_abundant(v) and p % 2 == 1)
    not_ab_even = sum(1 for p, v in zip(positions, verses) if not is_abundant(v) and p % 2 == 0)
    return abs(ab_odd - ab_even) + abs(not_ab_odd - not_ab_even)

def test_10_deficient_symmetry(positions, verses):
    """41/41 and 16/16 deficient symmetry"""
    def is_deficient(n):
        if n == 1: return True
        return proper_divisor_sum(n) < n
    def_odd = sum(1 for p, v in zip(positions, verses) if is_deficient(v) and p % 2 == 1)
    def_even = sum(1 for p, v in zip(positions, verses) if is_deficient(v) and p % 2 == 0)
    not_def_odd = sum(1 for p, v in zip(positions, verses) if not is_deficient(v) and p % 2 == 1)
    not_def_even = sum(1 for p, v in zip(positions, verses) if not is_deficient(v) and p % 2 == 0)
    return abs(def_odd - def_even) + abs(not_def_odd - not_def_even)

def test_11_mean_prime(positions, verses):
    """41/73 both prime - above/below mean"""
    mean = sum(verses) / len(verses)
    above = sum(1 for v in verses if v > mean)
    below = sum(1 for v in verses if v < mean)
    # Both should be prime
    score = 0
    if not is_prime_standard(above): score += 1
    if not is_prime_standard(below): score += 1
    return score

def test_12_long_short_split(positions, verses):
    """57/57 perfect split at boundary 39"""
    long_count = sum(1 for v in verses if v > 39)
    short_count = sum(1 for v in verses if v < 39)
    return abs(long_count - 57) + abs(short_count - 57)

def test_12_long_short_mirror(positions, verses):
    """27/30/30/27 mirror symmetry"""
    long_odd = sum(1 for p, v in zip(positions, verses) if v > 39 and p % 2 == 1)
    long_even = sum(1 for p, v in zip(positions, verses) if v > 39 and p % 2 == 0)
    short_odd = sum(1 for p, v in zip(positions, verses) if v < 39 and p % 2 == 1)
    short_even = sum(1 for p, v in zip(positions, verses) if v < 39 and p % 2 == 0)
    # Mirror: long_odd = short_even, long_even = short_odd
    return abs(long_odd - short_even) + abs(long_even - short_odd)

def test_14_divisor2_equal(positions, verses):
    """33/33/24/24 equal halves"""
    def has_2_div(n): return len(get_divisors(n)) == 2
    homo_first = homo_second = hetero_first = hetero_second = 0
    for p, v in zip(positions, verses):
        same = has_2_div(p) == has_2_div(v)
        first = p <= 57
        if same and first: homo_first += 1
        elif same: homo_second += 1
        elif first: hetero_first += 1
        else: hetero_second += 1
    return abs(homo_first - homo_second) + abs(hetero_first - hetero_second)

def test_16_golden_ratio(positions, verses):
    """Golden ratio approximation"""
    sums = [p + v for p, v in zip(positions, verses)]
    sum_counts = Counter(sums)
    sum_repeated = sum(s for s in sums if sum_counts[s] > 1)
    sum_unique = sum(s for s in sums if sum_counts[s] == 1)
    if sum_unique == 0: return float('inf')
    ratio = sum_repeated / sum_unique
    return abs(ratio - PHI)

def test_17_two_prime_div(positions, verses):
    """24/24/33/33 equal halves"""
    def has_two(n): return count_primes_in_divisors(n) == 2
    homo_first = homo_second = hetero_first = hetero_second = 0
    for p, v in zip(positions, verses):
        same = has_two(p) == has_two(v)
        first = p <= 57
        if same and first: homo_first += 1
        elif same: homo_second += 1
        elif first: hetero_first += 1
        else: hetero_second += 1
    return abs(homo_first - homo_second) + abs(hetero_first - hetero_second)

def test_18_three_prime_div(positions, verses):
    """25/25/32/32 equal halves"""
    def has_three(n): return count_primes_in_divisors(n) == 3
    homo_first = homo_second = hetero_first = hetero_second = 0
    for p, v in zip(positions, verses):
        same = has_three(p) == has_three(v)
        first = p <= 57
        if same and first: homo_first += 1
        elif same: homo_second += 1
        elif first: hetero_first += 1
        else: hetero_second += 1
    return abs(homo_first - homo_second) + abs(hetero_first - hetero_second)

def run_test(test_func, positions, verses, n_trials=N_TRIALS):
    observed = test_func(positions, verses)
    count = 0
    verse_list = list(verses)
    for _ in range(n_trials):
        shuffled = verse_list.copy()
        random.shuffle(shuffled)
        stat = test_func(positions, shuffled)
        if stat <= observed:
            count += 1
    return observed, count / n_trials

def main():
    print("=" * 75)
    print("STATISTICAL TESTING - VERSION 2")
    print(f"Permutation trials: {N_TRIALS:,}")
    print("=" * 75)
    print()

    vc = load_quran_data()
    positions = list(range(1, 115))
    verses = [vc[s] for s in positions]

    tests = [
        ("01 Mirror Symmetry (28/29/29/28)", test_01_symmetry),
        ("02 Mirror Symmetry (34/32/32/34)", test_02_symmetry),
        ("03 Prime Totals (12791, 209029)", test_03_prime_totals),
        ("04 Intersections (32/32)", test_04_set_ops_32_32),
        ("04 In/Out Range (101/13 prime)", test_04_set_ops_101_13),
        ("05 Equal Split (33/33/24/24)", test_05_equal_split),
        ("06 Equal Split (42/42/15/15)", test_06_equal_split),
        ("07 PFS Match (71/71, 43/43)", test_07_pfs_symmetry),
        ("08 Perfect Symmetry (2/2, 55/55)", test_08_perfect_symmetry),
        ("09 Abundant Symmetry (14/14, 43/43)", test_09_abundant_symmetry),
        ("10 Deficient Symmetry (41/41, 16/16)", test_10_deficient_symmetry),
        ("11 Mean Split Prime (41/73)", test_11_mean_prime),
        ("12 Long/Short Split (57/57)", test_12_long_short_split),
        ("12 Long/Short Mirror (27/30/30/27)", test_12_long_short_mirror),
        ("14 Divisor=2 Equal (33/33/24/24)", test_14_divisor2_equal),
        ("16 Golden Ratio (φ)", test_16_golden_ratio),
        ("17 Two Prime Div (24/24/33/33)", test_17_two_prime_div),
        ("18 Three Prime Div (25/25/32/32)", test_18_three_prime_div),
    ]

    results = []
    for name, test_func in tests:
        print(f"Testing: {name}...", end=" ", flush=True)
        observed, p_value = run_test(test_func, positions, verses)

        if p_value < 0.001:
            status = "★★★ p<0.001"
        elif p_value < 0.01:
            status = "★★ p<0.01"
        elif p_value < 0.05:
            status = "★ p<0.05"
        else:
            status = f"p={p_value:.3f}"

        print(status)
        results.append((name, observed, p_value, status))

    print()
    print("=" * 75)
    print("FINAL SUMMARY")
    print("=" * 75)
    print()

    sig_001 = sum(1 for _, _, p, _ in results if p < 0.001)
    sig_01 = sum(1 for _, _, p, _ in results if 0.001 <= p < 0.01)
    sig_05 = sum(1 for _, _, p, _ in results if 0.01 <= p < 0.05)
    not_sig = sum(1 for _, _, p, _ in results if p >= 0.05)

    print(f"★★★ Highly significant (p < 0.001): {sig_001}")
    print(f"★★  Very significant (p < 0.01):    {sig_01}")
    print(f"★   Significant (p < 0.05):         {sig_05}")
    print(f"    Not significant (p ≥ 0.05):     {not_sig}")
    print()

    print("Significant patterns:")
    for name, obs, p, status in results:
        if p < 0.05:
            print(f"  {name}: p = {p:.6f}")

    return results

if __name__ == "__main__":
    random.seed(42)
    main()
