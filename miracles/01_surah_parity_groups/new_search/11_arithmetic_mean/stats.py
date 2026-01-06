#!/usr/bin/env python3
"""
Statistical test for pattern 11: Arithmetic Mean 41/73 both prime

NOTE: Permutation doesn't change above/below average counts.
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

def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

def calc_score(verses):
    """Score: 0 if both above/below counts are prime, else higher"""
    mean = sum(verses) / len(verses)
    above = sum(1 for v in verses if v > mean)
    below = sum(1 for v in verses if v < mean)
    score = 0
    if not is_prime(above): score += 1
    if not is_prime(below): score += 1
    return score

def main():
    vc = load_quran_data()
    verses = [vc[s] for s in range(1, 115)]

    mean = sum(verses) / len(verses)
    above = sum(1 for v in verses if v > mean)
    below = sum(1 for v in verses if v < mean)

    print("ACTUAL VALUES:")
    print(f"  Mean: {mean:.2f}")
    print(f"  Above average: {above} (prime: {is_prime(above)})")
    print(f"  Below average: {below} (prime: {is_prime(below)})")

    observed = calc_score(verses)
    print(f"\nObserved score: {observed} (0 = both prime)")

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
