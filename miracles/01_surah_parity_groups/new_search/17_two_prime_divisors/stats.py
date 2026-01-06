#!/usr/bin/env python3
"""Statistical test for pattern 17: Two Prime Divisors 24/24/33/33"""
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

def is_prime_book(n):
    if n == 1: return True
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

def get_divisors(n):
    divs = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divs.append(i)
            if i != n // i:
                divs.append(n // i)
    return divs

def count_primes_in_divisors(n):
    return sum(1 for d in get_divisors(n) if is_prime_book(d))

def has_two_primes(n):
    return count_primes_in_divisors(n) == 2

def calc_score(positions, verses):
    homo_first = homo_second = hetero_first = hetero_second = 0
    for p, v in zip(positions, verses):
        same = has_two_primes(p) == has_two_primes(v)
        first = p <= 57
        if same and first: homo_first += 1
        elif same: homo_second += 1
        elif first: hetero_first += 1
        else: hetero_second += 1
    return abs(homo_first - homo_second) + abs(hetero_first - hetero_second)

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
