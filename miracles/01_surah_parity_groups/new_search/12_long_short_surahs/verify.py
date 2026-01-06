#!/usr/bin/env python3
"""
Long and Short Surahs Patterns
==============================
Source: Simetrik Kitap: Kur'an, pages 305-324

Boundary: 39 verses (no surah has exactly 39 verses!)
- Long surah: >39 verses
- Short surah: <39 verses

Key patterns:
- 57/57: Long/Short (exact half!)
- 27/30/30/27: Long odd/even, Short odd/even (mirror symmetry)
- 48/48: Position matches + parity homo/hetero
- 9/9: Position NOT matches + parity homo/hetero
"""

from pathlib import Path

BOUNDARY = 39

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
    print("LONG AND SHORT SURAHS PATTERNS")
    print("=" * 60)
    print()

    # Check boundary
    has_39 = [s for s, v in vc.items() if v == BOUNDARY]
    print(f"Boundary: {BOUNDARY} verses")
    print(f"Surahs with exactly {BOUNDARY} verses: {len(has_39)} (none!)")
    print()

    # Long and Short
    long_surahs = [(s, v) for s, v in vc.items() if v > BOUNDARY]
    short_surahs = [(s, v) for s, v in vc.items() if v < BOUNDARY]

    print(f"Long surahs (>{BOUNDARY}): {len(long_surahs)}")
    print(f"Short surahs (<{BOUNDARY}): {len(short_surahs)}")
    if len(long_surahs) == 57 and len(short_surahs) == 57:
        print("✓ VERIFIED: 57/57 (exact half!)")
    print()

    # Pattern 1: 27/30/30/27
    long_odd = len([x for x in long_surahs if x[0] % 2 == 1])
    long_even = len([x for x in long_surahs if x[0] % 2 == 0])
    short_odd = len([x for x in short_surahs if x[0] % 2 == 1])
    short_even = len([x for x in short_surahs if x[0] % 2 == 0])

    print(f"Long + pos odd:   {long_odd}")
    print(f"Long + pos even:  {long_even}")
    print(f"Short + pos odd:  {short_odd}")
    print(f"Short + pos even: {short_even}")
    if [long_odd, long_even, short_odd, short_even] == [27, 30, 30, 27]:
        print("✓ VERIFIED: 27/30/30/27 (mirror symmetry!)")
    print()

    # Position matches
    matching = [(s, v) for s, v in vc.items() if (s <= 57 and v > BOUNDARY) or (s > 57 and v < BOUNDARY)]
    not_matching = [(s, v) for s, v in vc.items() if v != BOUNDARY and not ((s <= 57 and v > BOUNDARY) or (s > 57 and v < BOUNDARY))]

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
        'long': len(long_surahs),
        'short': len(short_surahs),
        'matching': len(matching),
        'not_matching': len(not_matching)
    }

if __name__ == "__main__":
    verify()
