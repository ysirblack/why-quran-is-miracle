#!/usr/bin/env python3
"""Statistical test for pattern 13: Mean vs Long/Short identical results"""
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

def calc_score(positions, verses):
    mean = sum(verses) / len(verses)
    
    # Mean method matches
    mean_match = sum(1 for p, v in zip(positions, verses) 
                     if (p <= 57 and v > mean) or (p > 57 and v < mean))
    
    # Long/Short method matches
    ls_match = sum(1 for p, v in zip(positions, verses)
                   if (p <= 57 and v > 39) or (p > 57 and v < 39))
    
    # Score: difference between two methods (should be 0 for identical)
    return abs(mean_match - ls_match)

def main():
    vc = load_quran_data()
    positions = list(range(1, 115))
    verses = [vc[s] for s in positions]
    
    observed = calc_score(positions, verses)
    print(f"Observed: {observed} (0 = identical)")
    
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
