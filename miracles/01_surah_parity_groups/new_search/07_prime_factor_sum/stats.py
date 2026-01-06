#!/usr/bin/env python3
"""
Statistical test for pattern 07: PFS 71/71, 43/43

NOTE: Permutation doesn't change PFS counts of the verse set.
Using bootstrap with random verse distributions.
"""
import random
from pathlib import Path

N_TRIALS = 100_000

def load_quran_data():
    current_dir = Path(__file__).parent
    for _ in range(6):
        potential_path = current_dir / "data" / "quran-uthmani.txt"
        if potential_path.exists():
            break
        current_dir = current_dir.parent
    verses = {}
    with potential_path.open('r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#') or '|' not in line:
                continue
            parts = line.split('|', 2)
            if len(parts) >= 3:
                surah = int(parts[0])
                verses.setdefault(surah, []).append(int(parts[1]))
    return {s: len(v) for s, v in verses.items()}

def prime_factor_sum(n):
    if n == 1: return 1
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

# Pre-compute position PFS
POS_PFS_ODD = sum(1 for p in range(1, 115) if prime_factor_sum(p) % 2 == 1)  # 71
POS_PFS_EVEN = 114 - POS_PFS_ODD  # 43

def calc_score(verses):
    """Score: how close verse PFS odd/even matches position PFS odd/even"""
    v_odd = sum(1 for v in verses if prime_factor_sum(v) % 2 == 1)
    v_even = 114 - v_odd
    return abs(v_odd - POS_PFS_ODD) + abs(v_even - POS_PFS_EVEN)

def main():
    vc = load_quran_data()
    verses = [vc[s] for s in range(1, 115)]

    v_odd = sum(1 for v in verses if prime_factor_sum(v) % 2 == 1)
    v_even = 114 - v_odd

    print("ACTUAL VALUES:")
    print(f"  Position a₀ odd:  {POS_PFS_ODD}")
    print(f"  Position a₀ even: {POS_PFS_EVEN}")
    print(f"  Verse a₀ odd:     {v_odd}")
    print(f"  Verse a₀ even:    {v_even}")

    observed = calc_score(verses)
    print(f"\nObserved score: {observed} (0 = perfect match)")

    print("\nBootstrap test: generating random verse count distributions...")
    count = 0
    for i in range(N_TRIALS):
        random_verses = [random.randint(3, 286) for _ in range(114)]
        if calc_score(random_verses) <= observed:
            count += 1
        if (i+1) % 20000 == 0:
            print(f"  {i+1:,} trials done...")

    p = count / N_TRIALS
    print(f"\np-value: {p:.6f}")
    print(f"Significant (p<0.05): {'YES' if p < 0.05 else 'NO'}")

if __name__ == "__main__":
    random.seed(42)
    main()
