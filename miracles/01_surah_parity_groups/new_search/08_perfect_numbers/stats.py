#!/usr/bin/env python3
"""Statistical test for pattern 08: Perfect Numbers 2/2, 55/55"""
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

def proper_divisor_sum(n):
    if n <= 1: return 0
    total = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i
    return total

def is_perfect(n):
    return proper_divisor_sum(n) == n

def calc_score(positions, verses):
    perf_odd = sum(1 for p, v in zip(positions, verses) if is_perfect(v) and p % 2 == 1)
    perf_even = sum(1 for p, v in zip(positions, verses) if is_perfect(v) and p % 2 == 0)
    not_perf_odd = sum(1 for p, v in zip(positions, verses) if not is_perfect(v) and p % 2 == 1)
    not_perf_even = sum(1 for p, v in zip(positions, verses) if not is_perfect(v) and p % 2 == 0)
    return abs(perf_odd - perf_even) + abs(not_perf_odd - not_perf_even)

def main():
    vc = load_quran_data()
    positions = list(range(1, 115))
    verses = [vc[s] for s in positions]
    
    observed = calc_score(positions, verses)
    print(f"Observed: {observed}")
    
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
