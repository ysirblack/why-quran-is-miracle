#!/usr/bin/env python3
"""
Divisor Count = 2 (Prime Numbers) Patterns
==========================================
Source: Simetrik Kitap: Kur'an, pages 337-347

Numbers with exactly 2 divisors are prime numbers.
(1 has only 1 divisor, so it's not included)

Key pattern: 33/33/24/24
- Homo first/second: 33/33 (equal split)
- Hetero first/second: 24/24 (equal split)
"""

from pathlib import Path

def divisor_count(n):
    """Count number of divisors"""
    if n < 1:
        return 0
    count = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            count += 1
            if i != n // i:
                count += 1
    return count

def has_2_divisors(n):
    """True if n has exactly 2 divisors (prime numbers)"""
    return divisor_count(n) == 2

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
    print("DIVISOR COUNT = 2 (PRIME) PATTERNS")
    print("=" * 60)
    print()

    # Homogeneous: both have 2 divisors OR both don't
    homo = [(s, v) for s, v in vc.items() if has_2_divisors(s) == has_2_divisors(v)]
    hetero = [(s, v) for s, v in vc.items() if has_2_divisors(s) != has_2_divisors(v)]

    print(f"Homogeneous: {len(homo)}")
    print(f"Heterogeneous: {len(hetero)}")
    print()

    # Split by half
    homo_first = len([x for x in homo if x[0] <= 57])
    homo_second = len([x for x in homo if x[0] > 57])
    hetero_first = len([x for x in hetero if x[0] <= 57])
    hetero_second = len([x for x in hetero if x[0] > 57])

    print(f"Homo - first half:  {homo_first}")
    print(f"Homo - second half: {homo_second}")
    print(f"Hetero - first half:  {hetero_first}")
    print(f"Hetero - second half: {hetero_second}")
    print()

    if homo_first == 33 and homo_second == 33:
        print("✓ VERIFIED: Homo 33/33 (equal split)")
    if hetero_first == 24 and hetero_second == 24:
        print("✓ VERIFIED: Hetero 24/24 (equal split)")

    return {
        'homo': len(homo),
        'hetero': len(hetero),
        'homo_first': homo_first,
        'homo_second': homo_second,
        'hetero_first': hetero_first,
        'hetero_second': hetero_second
    }

if __name__ == "__main__":
    verify()
