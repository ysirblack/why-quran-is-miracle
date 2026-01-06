#!/usr/bin/env python3
"""
Deficient Numbers Patterns
==========================
Source: Simetrik Kitap: Kur'an, pages 263-281

Deficient (Kıt) number: sum of proper divisors < n
Examples: 8 (1+2+4=7<8), 10 (1+2+5=8<10)
Note: 1 is considered deficient (0 < 1)

Key patterns:
- 41/41: Verse deficient + position odd/even
- 16/16: Verse NOT deficient + position odd/even
- 71/43: Homogeneous / Heterogeneous (BOTH PRIME!)
"""

from pathlib import Path

def proper_divisor_sum(n):
    if n < 2:
        return 0
    total = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i
    return total

def is_deficient(n):
    """Deficient: sum of proper divisors < n. 1 is considered deficient."""
    if n == 1:
        return True
    if n < 1:
        return False
    return proper_divisor_sum(n) < n

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
    print("DEFICIENT NUMBERS PATTERNS")
    print("=" * 60)
    print()

    verse_def = [(s, v) for s, v in vc.items() if is_deficient(v)]
    verse_not_def = [(s, v) for s, v in vc.items() if not is_deficient(v)]

    print(f"Verse deficient: {len(verse_def)}")
    print(f"Verse NOT deficient: {len(verse_not_def)}")
    print()

    # Pattern 1: 41/41
    verse_def_odd = len([x for x in verse_def if x[0] % 2 == 1])
    verse_def_even = len([x for x in verse_def if x[0] % 2 == 0])
    print(f"Verse deficient + pos odd:  {verse_def_odd}")
    print(f"Verse deficient + pos even: {verse_def_even}")
    if verse_def_odd == 41 and verse_def_even == 41:
        print("✓ VERIFIED: 41/41")
    print()

    # Pattern 2: 16/16
    verse_not_def_odd = len([x for x in verse_not_def if x[0] % 2 == 1])
    verse_not_def_even = len([x for x in verse_not_def if x[0] % 2 == 0])
    print(f"Verse NOT deficient + pos odd:  {verse_not_def_odd}")
    print(f"Verse NOT deficient + pos even: {verse_not_def_even}")
    if verse_not_def_odd == 16 and verse_not_def_even == 16:
        print("✓ VERIFIED: 16/16")
    print()

    # Pattern 3: 71/43
    homo = [(s, v) for s, v in vc.items() if is_deficient(s) == is_deficient(v)]
    hetero = [(s, v) for s, v in vc.items() if is_deficient(s) != is_deficient(v)]
    print(f"Homogeneous: {len(homo)}")
    print(f"Heterogeneous: {len(hetero)}")
    if len(homo) == 71 and len(hetero) == 43:
        print("✓ VERIFIED: 71/43")
        print(f"★ BOTH ARE PRIME: {is_prime(71)} / {is_prime(43)}")

    return {
        'verse_deficient': len(verse_def),
        'homo': len(homo),
        'hetero': len(hetero)
    }

if __name__ == "__main__":
    verify()
