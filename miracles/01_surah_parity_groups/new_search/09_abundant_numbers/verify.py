#!/usr/bin/env python3
"""
Abundant Numbers Patterns
=========================
Source: Simetrik Kitap: Kur'an, pages 245-260

Abundant (Zengin) number: sum of proper divisors > n
Examples: 12 (1+2+3+4+6=16>12), 18 (1+2+3+6+9=21>18)

Key patterns:
- 14/14: Verse abundant + position odd/even
- 43/43: Verse NOT abundant + position odd/even
- 71/43: Homogeneous / Heterogeneous (BOTH PRIME!)
"""

from pathlib import Path

def is_abundant(n):
    """Check if n is abundant (sum of proper divisors > n)"""
    if n < 2:
        return False
    divisor_sum = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisor_sum += i
            if i != n // i:
                divisor_sum += n // i
    return divisor_sum > n

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

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

def verify():
    vc = load_quran_data()

    print("=" * 60)
    print("ABUNDANT NUMBERS PATTERNS")
    print("=" * 60)
    print()

    verse_abundant = [(s, v) for s, v in vc.items() if is_abundant(v)]
    verse_not_abundant = [(s, v) for s, v in vc.items() if not is_abundant(v)]

    print(f"Verse abundant: {len(verse_abundant)}")
    print(f"Verse NOT abundant: {len(verse_not_abundant)}")
    print()

    # Pattern 1: 14/14
    verse_ab_odd = len([x for x in verse_abundant if x[0] % 2 == 1])
    verse_ab_even = len([x for x in verse_abundant if x[0] % 2 == 0])
    print(f"Verse abundant + pos odd:  {verse_ab_odd}")
    print(f"Verse abundant + pos even: {verse_ab_even}")
    if verse_ab_odd == 14 and verse_ab_even == 14:
        print("✓ VERIFIED: 14/14")
    print()

    # Pattern 2: 43/43
    verse_not_ab_odd = len([x for x in verse_not_abundant if x[0] % 2 == 1])
    verse_not_ab_even = len([x for x in verse_not_abundant if x[0] % 2 == 0])
    print(f"Verse NOT abundant + pos odd:  {verse_not_ab_odd}")
    print(f"Verse NOT abundant + pos even: {verse_not_ab_even}")
    if verse_not_ab_odd == 43 and verse_not_ab_even == 43:
        print("✓ VERIFIED: 43/43")
    print()

    # Pattern 3: 71/43
    homo = [(s, v) for s, v in vc.items() if is_abundant(s) == is_abundant(v)]
    hetero = [(s, v) for s, v in vc.items() if is_abundant(s) != is_abundant(v)]
    print(f"Homogeneous: {len(homo)}")
    print(f"Heterogeneous: {len(hetero)}")
    if len(homo) == 71 and len(hetero) == 43:
        print("✓ VERIFIED: 71/43")
        print(f"★ BOTH ARE PRIME: {is_prime(71)} / {is_prime(43)}")

    return {
        'verse_abundant': len(verse_abundant),
        'homo': len(homo),
        'hetero': len(hetero)
    }

if __name__ == "__main__":
    verify()
