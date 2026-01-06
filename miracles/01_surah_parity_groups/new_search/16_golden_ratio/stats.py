#!/usr/bin/env python3
"""Statistical test for pattern 16: Golden Ratio 7906/4885 ≈ φ"""
import random
from pathlib import Path
from collections import Counter

N_TRIALS = 100_000
PHI = 1.6180339887

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

def calc_score(positions, verses):
    sums = [p + v for p, v in zip(positions, verses)]
    sum_counts = Counter(sums)
    sum_repeated = sum(s for s in sums if sum_counts[s] > 1)
    sum_unique = sum(s for s in sums if sum_counts[s] == 1)
    if sum_unique == 0:
        return float('inf')
    ratio = sum_repeated / sum_unique
    return abs(ratio - PHI)

def main():
    vc = load_quran_data()
    positions = list(range(1, 115))
    verses = [vc[s] for s in positions]
    
    observed = calc_score(positions, verses)
    print(f"Observed deviation from φ: {observed:.6f}")
    
    count = 0
    for i in range(N_TRIALS):
        shuffled = verses.copy()
        random.shuffle(shuffled)
        if calc_score(positions, shuffled) <= observed:
            count += 1
        if (i+1) % 10000 == 0:
            print(f"  {i+1:,} trials done...")
    
    p = count / N_TRIALS
    print(f"\np-value: {p:.6f}")
    print(f"Significant (p<0.05): {'YES' if p < 0.05 else 'NO'}")

if __name__ == "__main__":
    random.seed(42)
    main()
