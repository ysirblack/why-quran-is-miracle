#!/usr/bin/env python3
"""
Perfect Numbers Patterns
========================
Source: Simetrik Kitap: Kur'an, pages 225-241

Perfect number: n where sum of proper divisors equals n
Examples: 6 = 1+2+3, 28 = 1+2+4+7+14

Only 4 surahs have perfect verse counts:
- Surah 71: 28 verses
- Surah 72: 28 verses
- Surah 109: 6 verses
- Surah 114: 6 verses

Key patterns:
- 2/2: Verse perfect + position odd/even
- 55/55: Verse NOT perfect + position odd/even
- 54/54: Homo + parity homo/hetero
- 3/3: Hetero + parity homo/hetero
"""

from pathlib import Path

def is_perfect(n):
    """Check if n is a perfect number"""
    if n < 2:
        return False
    divisor_sum = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisor_sum += i
            if i != n // i:
                divisor_sum += n // i
    return divisor_sum == n

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
    print("PERFECT NUMBERS PATTERNS")
    print("=" * 60)
    print()

    # Find surahs with perfect verse counts
    verse_perfect = [(s, v) for s, v in vc.items() if is_perfect(v)]
    verse_not_perfect = [(s, v) for s, v in vc.items() if not is_perfect(v)]

    print(f"Surahs with perfect verse count: {len(verse_perfect)}")
    for s, v in verse_perfect:
        print(f"  Surah {s}: {v} verses")
    print()

    # Pattern 1: 2/2
    verse_perf_odd = len([(s, v) for s, v in verse_perfect if s % 2 == 1])
    verse_perf_even = len([(s, v) for s, v in verse_perfect if s % 2 == 0])
    print(f"Verse perfect + pos odd:  {verse_perf_odd}")
    print(f"Verse perfect + pos even: {verse_perf_even}")
    if verse_perf_odd == 2 and verse_perf_even == 2:
        print("✓ VERIFIED: 2/2")
    print()

    # Pattern 2: 55/55
    verse_not_perf_odd = len([(s, v) for s, v in verse_not_perfect if s % 2 == 1])
    verse_not_perf_even = len([(s, v) for s, v in verse_not_perfect if s % 2 == 0])
    print(f"Verse NOT perfect + pos odd:  {verse_not_perf_odd}")
    print(f"Verse NOT perfect + pos even: {verse_not_perf_even}")
    if verse_not_perf_odd == 55 and verse_not_perf_even == 55:
        print("✓ VERIFIED: 55/55")
    print()

    # Homogeneity
    homo = [(s, v) for s, v in vc.items() if is_perfect(s) == is_perfect(v)]
    hetero = [(s, v) for s, v in vc.items() if is_perfect(s) != is_perfect(v)]

    print(f"Homogeneous (perfect): {len(homo)}")
    print(f"Heterogeneous: {len(hetero)}")
    print()

    # Pattern 3: 54/54
    homo_parity_homo = len([(s, v) for s, v in homo if s % 2 == v % 2])
    homo_parity_hetero = len([(s, v) for s, v in homo if s % 2 != v % 2])
    print(f"Homo + parity homo:   {homo_parity_homo}")
    print(f"Homo + parity hetero: {homo_parity_hetero}")
    if homo_parity_homo == 54 and homo_parity_hetero == 54:
        print("✓ VERIFIED: 54/54")
    print()

    # Pattern 4: 3/3
    hetero_parity_homo = len([(s, v) for s, v in hetero if s % 2 == v % 2])
    hetero_parity_hetero = len([(s, v) for s, v in hetero if s % 2 != v % 2])
    print(f"Hetero + parity homo:   {hetero_parity_homo}")
    print(f"Hetero + parity hetero: {hetero_parity_hetero}")
    if hetero_parity_homo == 3 and hetero_parity_hetero == 3:
        print("✓ VERIFIED: 3/3")

    return {
        'verse_perfect': verse_perfect,
        'homo': len(homo),
        'hetero': len(hetero)
    }

if __name__ == "__main__":
    verify()
