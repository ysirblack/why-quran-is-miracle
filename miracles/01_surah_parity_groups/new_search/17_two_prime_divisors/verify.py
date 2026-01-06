#!/usr/bin/env python3
"""
Two Prime Divisors Pattern
===========================
Source: Simetrik Kitap: Kur'an

Numbers with exactly 2 prime divisors in their divisor set.
Note: This book considers 1 as prime.

Examples:
- 2 has divisors {1, 2}, primes = {1, 2} = 2 primes ✓
- 4 has divisors {1, 2, 4}, primes = {1, 2} = 2 primes ✓
- 6 has divisors {1, 2, 3, 6}, primes = {1, 2, 3} = 3 primes ✗

Pattern: 24/33/24/33 (homo_first/hetero_first/homo_second/hetero_second)
"""

from pathlib import Path

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

def count_primes_in_divisors(n):
    """Count how many primes (including 1) are in the divisor set"""
    divisors = get_divisors(n)
    return sum(1 for d in divisors if is_prime_book(d))

def has_two_prime_divisors(n):
    """Check if n has exactly 2 primes in its divisor set"""
    return count_primes_in_divisors(n) == 2

def verify():
    vc = load_quran_data()

    print("=" * 60)
    print("TWO PRIME DIVISORS PATTERN")
    print("(Numbers with exactly 2 primes in divisor set, 1 as prime)")
    print("=" * 60)
    print()

    homo = []
    hetero = []

    for s, v in vc.items():
        s_has = has_two_prime_divisors(s)
        v_has = has_two_prime_divisors(v)

        if s_has == v_has:
            homo.append((s, v))
        else:
            hetero.append((s, v))

    print(f"Homogeneous (both have or both don't have): {len(homo)}")
    print(f"Heterogeneous (one has, one doesn't): {len(hetero)}")
    print()

    # Split by halves
    homo_first = [x for x in homo if x[0] <= 57]
    homo_second = [x for x in homo if x[0] > 57]
    hetero_first = [x for x in hetero if x[0] <= 57]
    hetero_second = [x for x in hetero if x[0] > 57]

    print("Split by halves:")
    print(f"  Homogeneous - first half (1-57):  {len(homo_first)}")
    print(f"  Homogeneous - second half (58-114): {len(homo_second)}")
    print(f"  Heterogeneous - first half (1-57):  {len(hetero_first)}")
    print(f"  Heterogeneous - second half (58-114): {len(hetero_second)}")
    print()

    # Verification
    if len(homo_first) == 24 and len(homo_second) == 24:
        print("✓ VERIFIED: Homogeneous 24/24 symmetry")
    if len(hetero_first) == 33 and len(hetero_second) == 33:
        print("✓ VERIFIED: Heterogeneous 33/33 symmetry")
    if is_prime_book(33):
        print("  ★ 33 is NOT prime (33 = 3 × 11)")
    if is_prime_book(24):
        print("  ★ 24 is NOT prime (24 = 2³ × 3)")

    return {
        'homo': len(homo),
        'hetero': len(hetero),
        'homo_first': len(homo_first),
        'homo_second': len(homo_second),
        'hetero_first': len(hetero_first),
        'hetero_second': len(hetero_second)
    }

if __name__ == "__main__":
    verify()
