#!/usr/bin/env python3
"""
Statistical test for pattern 12: Long/Short 57/57, Mirror 27/30/30/27

NOTE: Permutation doesn't change long/short counts (same values).
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

def calc_score(verses):
    """Score: deviation from 57/57 split"""
    long_count = sum(1 for v in verses if v > 39)
    short_count = sum(1 for v in verses if v < 39)
    # Perfect 57/57 = score 0
    return abs(long_count - 57) + abs(short_count - 57)

def main():
    vc = load_quran_data()
    verses = [vc[s] for s in range(1, 115)]

    long_count = sum(1 for v in verses if v > 39)
    short_count = sum(1 for v in verses if v < 39)
    equal_count = sum(1 for v in verses if v == 39)

    print("ACTUAL VALUES:")
    print(f"  Long (>39):  {long_count}")
    print(f"  Short (<39): {short_count}")
    print(f"  Equal (=39): {equal_count}")

    observed = calc_score(verses)
    print(f"\nObserved score: {observed} (0 = perfect 57/57)")

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
