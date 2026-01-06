#!/usr/bin/env python3
"""
Arithmetic Mean Patterns
========================
Source: Simetrik Kitap: Kur'an, pages 289-303

Mean verse count = 6236 / 114 ≈ 54.70

Key patterns:
- 41/73: Above/below average (BOTH PRIME!)
- 48/48: Position matches + parity homo/hetero
- 9/9: Position NOT matches + parity homo/hetero

Position matches = (first half AND above average) OR (second half AND below average)
"""

from pathlib import Path

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
    print("ARITHMETIC MEAN PATTERNS")
    print("=" * 60)
    print()

    total_verses = sum(vc.values())
    mean = total_verses / 114
    print(f"Total verses: {total_verses}")
    print(f"Mean: {mean:.2f}")
    print()

    # Pattern 1: 41/73
    above = [(s, v) for s, v in vc.items() if v > mean]
    below = [(s, v) for s, v in vc.items() if v < mean]
    print(f"Above average: {len(above)}")
    print(f"Below average: {len(below)}")
    if len(above) == 41 and len(below) == 73:
        print("✓ VERIFIED: 41/73")
        print(f"★ BOTH ARE PRIME: {is_prime(41)} / {is_prime(73)}")
    print()

    # Position matches
    matching = [(s, v) for s, v in vc.items() if (s <= 57 and v > mean) or (s > 57 and v < mean)]
    not_matching = [(s, v) for s, v in vc.items() if not ((s <= 57 and v > mean) or (s > 57 and v < mean))]

    print(f"Position matches: {len(matching)}")
    print(f"Position NOT matches: {len(not_matching)}")
    print()

    # Pattern 2: 48/48
    matching_homo = len([x for x in matching if x[0] % 2 == x[1] % 2])
    matching_hetero = len([x for x in matching if x[0] % 2 != x[1] % 2])
    print(f"Matching + parity homo:   {matching_homo}")
    print(f"Matching + parity hetero: {matching_hetero}")
    if matching_homo == 48 and matching_hetero == 48:
        print("✓ VERIFIED: 48/48")
    print()

    # Pattern 3: 9/9
    not_matching_homo = len([x for x in not_matching if x[0] % 2 == x[1] % 2])
    not_matching_hetero = len([x for x in not_matching if x[0] % 2 != x[1] % 2])
    print(f"NOT matching + parity homo:   {not_matching_homo}")
    print(f"NOT matching + parity hetero: {not_matching_hetero}")
    if not_matching_homo == 9 and not_matching_hetero == 9:
        print("✓ VERIFIED: 9/9")

    return {
        'above': len(above),
        'below': len(below),
        'matching': len(matching),
        'not_matching': len(not_matching)
    }

if __name__ == "__main__":
    verify()
