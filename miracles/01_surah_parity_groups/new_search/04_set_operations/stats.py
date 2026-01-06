#!/usr/bin/env python3
"""
Statistical test for pattern 04: Set Operations 32/32, 25/25, 101/13

NOTE: Permutation test is NOT appropriate for this pattern because
shuffling verse counts among positions does not change the SET of
unique verse count values.

Instead, we use a bootstrap approach: generate random verse count
distributions and see how often perfect symmetry occurs.
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
    """Calculate symmetry score for set operations"""
    positions = set(range(1, 115))
    verse_count_set = set(verses)

    odd_pos = {p for p in positions if p % 2 == 1}
    even_pos = {p for p in positions if p % 2 == 0}
    odd_vc = {v for v in verse_count_set if v % 2 == 1}
    even_vc = {v for v in verse_count_set if v % 2 == 0}

    odd_int = len(odd_pos & odd_vc)
    even_int = len(even_pos & even_vc)
    odd_diff = len(odd_pos - odd_vc)
    even_diff = len(even_pos - even_vc)

    return abs(odd_int - even_int) + abs(odd_diff - even_diff)

def main():
    vc = load_quran_data()
    verses = [vc[s] for s in range(1, 115)]

    print("ACTUAL VALUES:")
    position_set = set(range(1, 115))
    verse_count_set = set(verses)
    odd_pos = {p for p in position_set if p % 2 == 1}
    even_pos = {p for p in position_set if p % 2 == 0}
    odd_vc = {v for v in verse_count_set if v % 2 == 1}
    even_vc = {v for v in verse_count_set if v % 2 == 0}

    print(f"  Unique verse counts: {len(verse_count_set)}")
    print(f"  Odd positions ∩ Odd VC: {len(odd_pos & odd_vc)} (expect 32)")
    print(f"  Even positions ∩ Even VC: {len(even_pos & even_vc)} (expect 32)")
    print(f"  Odd positions - Odd VC: {len(odd_pos - odd_vc)} (expect 25)")
    print(f"  Even positions - Even VC: {len(even_pos - even_vc)} (expect 25)")

    observed = calc_score(verses)
    print(f"\nObserved score: {observed} (0 = perfect symmetry)")

    # Bootstrap: generate random verse counts from same distribution
    print("\nBootstrap test: generating random verse count distributions...")
    min_v, max_v = min(verses), max(verses)

    count = 0
    for i in range(N_TRIALS):
        # Generate 114 random verse counts from similar range
        random_verses = [random.randint(3, 286) for _ in range(114)]
        if calc_score(random_verses) <= observed:
            count += 1
        if (i+1) % 20000 == 0:
            print(f"  {i+1:,} trials done...")

    p = count / N_TRIALS
    print(f"\np-value: {p:.6f}")
    print(f"Significant (p<0.05): {'YES' if p < 0.05 else 'NO'}")
    print("\nNote: Bootstrap test using uniform(3, 286) distribution")

if __name__ == "__main__":
    random.seed(42)
    main()
