#!/usr/bin/env python3
"""
Set Operations Patterns
=======================
Source: Simetrik Kitap: Kur'an, pages 139-163

Multiple symmetric patterns found through set operations on:
- Position numbers (1-114)
- Verse count values (unique)
- Odd/even subsets
- Intersections, differences, membership

Key symmetries:
- 32/32: Odd ∩ Odd, Even ∩ Even
- 25/25: Odd - Odd, Even - Even
- 101/13: Verse in positions, NOT in positions (BOTH PRIME!)
- 25/25: Verse in pos + odd pos + Homo/Hetero
- 3/3: Verse NOT in pos + even pos + Homo/Hetero
- 10/10: Pos NOT in VC + odd/even + Hetero
- 15/15: Pos NOT in VC + odd/even + Homo
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

    # Basic sets
    positions = set(range(1, 115))  # {1, 2, ..., 114}
    verse_counts = set(vc.values())  # unique verse count values

    # Odd/even subsets
    odd_positions = {p for p in positions if p % 2 == 1}
    even_positions = {p for p in positions if p % 2 == 0}
    odd_verse_counts = {v for v in verse_counts if v % 2 == 1}
    even_verse_counts = {v for v in verse_counts if v % 2 == 0}

    print("=" * 70)
    print("SET OPERATIONS PATTERNS")
    print("=" * 70)
    print()

    # Pattern 1: Intersections (32/32)
    odd_int = len(odd_positions & odd_verse_counts)
    even_int = len(even_positions & even_verse_counts)
    print("PATTERN 1: Intersections")
    print(f"  Odd positions ∩ Odd verse counts:   {odd_int}")
    print(f"  Even positions ∩ Even verse counts: {even_int}")
    if odd_int == 32 and even_int == 32:
        print("  ✓ VERIFIED: 32/32 symmetry")
    print()

    # Pattern 2: Differences (25/25)
    odd_diff = len(odd_positions - odd_verse_counts)
    even_diff = len(even_positions - even_verse_counts)
    print("PATTERN 2: Set Differences")
    print(f"  Odd positions - Odd verse counts:   {odd_diff}")
    print(f"  Even positions - Even verse counts: {even_diff}")
    if odd_diff == 25 and even_diff == 25:
        print("  ✓ VERIFIED: 25/25 symmetry")
    print()

    # Pattern 3: Verse in positions (101/13) - BOTH PRIME!
    verse_in_pos = [(s, v) for s, v in vc.items() if v in positions]
    verse_not_in_pos = [(s, v) for s, v in vc.items() if v not in positions]
    vip_count = len(verse_in_pos)
    vnip_count = len(verse_not_in_pos)
    print("PATTERN 3: Verse Count in Position Numbers")
    print(f"  Verse count IN positions (1-114):     {vip_count}")
    print(f"  Verse count NOT in positions (>114):  {vnip_count}")
    if vip_count == 101 and vnip_count == 13:
        print(f"  ✓ VERIFIED: 101/13")
        print(f"  ★ BOTH ARE PRIME: {is_prime(101)} / {is_prime(13)}")
    print()

    # Pattern 4: Verse in pos + Position parity + Homo/Hetero (25/25)
    vip_odd = [(s, v) for s, v in verse_in_pos if s % 2 == 1]
    vip_odd_homo = len([(s, v) for s, v in vip_odd if s % 2 == v % 2])
    vip_odd_hetero = len([(s, v) for s, v in vip_odd if s % 2 != v % 2])
    print("PATTERN 4: Verse in Pos + Position Odd + Parity")
    print(f"  Verse in pos + Pos odd + Homo:   {vip_odd_homo}")
    print(f"  Verse in pos + Pos odd + Hetero: {vip_odd_hetero}")
    if vip_odd_homo == 25 and vip_odd_hetero == 25:
        print("  ✓ VERIFIED: 25/25 symmetry")
    print()

    # Pattern 5: Verse NOT in pos + Position even + Homo/Hetero (3/3)
    vnip_even = [(s, v) for s, v in verse_not_in_pos if s % 2 == 0]
    vnip_even_homo = len([(s, v) for s, v in vnip_even if s % 2 == v % 2])
    vnip_even_hetero = len([(s, v) for s, v in vnip_even if s % 2 != v % 2])
    print("PATTERN 5: Verse NOT in Pos + Position Even + Parity")
    print(f"  Verse NOT in pos + Pos even + Homo:   {vnip_even_homo}")
    print(f"  Verse NOT in pos + Pos even + Hetero: {vnip_even_hetero}")
    if vnip_even_homo == 3 and vnip_even_hetero == 3:
        print("  ✓ VERIFIED: 3/3 symmetry")
    print()

    # Pattern 6: Position NOT in verse counts + Hetero (10/10)
    pos_not_in_vc = [(s, v) for s, v in vc.items() if s not in verse_counts]
    pnvc_odd = [(s, v) for s, v in pos_not_in_vc if s % 2 == 1]
    pnvc_even = [(s, v) for s, v in pos_not_in_vc if s % 2 == 0]
    pnvc_odd_hetero = len([(s, v) for s, v in pnvc_odd if s % 2 != v % 2])
    pnvc_even_hetero = len([(s, v) for s, v in pnvc_even if s % 2 != v % 2])
    print("PATTERN 6: Position NOT in VC + Hetero")
    print(f"  Pos NOT in VC + Pos odd + Hetero:  {pnvc_odd_hetero}")
    print(f"  Pos NOT in VC + Pos even + Hetero: {pnvc_even_hetero}")
    if pnvc_odd_hetero == 10 and pnvc_even_hetero == 10:
        print("  ✓ VERIFIED: 10/10 symmetry")
    print()

    # Pattern 7: Position NOT in verse counts + Homo (15/15)
    pnvc_odd_homo = len([(s, v) for s, v in pnvc_odd if s % 2 == v % 2])
    pnvc_even_homo = len([(s, v) for s, v in pnvc_even if s % 2 == v % 2])
    print("PATTERN 7: Position NOT in VC + Homo")
    print(f"  Pos NOT in VC + Pos odd + Homo:  {pnvc_odd_homo}")
    print(f"  Pos NOT in VC + Pos even + Homo: {pnvc_even_homo}")
    if pnvc_odd_homo == 15 and pnvc_even_homo == 15:
        print("  ✓ VERIFIED: 15/15 symmetry")
    print()

    print("=" * 70)
    print("SUMMARY OF SYMMETRIES")
    print("=" * 70)
    print()
    print("  32 / 32  (Intersections)")
    print("  25 / 25  (Differences)")
    print("  101 / 13 (Verse in/not in pos) ★ BOTH PRIME")
    print("  25 / 25  (Verse in pos + odd + parity)")
    print("  3 / 3    (Verse NOT in pos + even + parity)")
    print("  10 / 10  (Pos NOT in VC + hetero)")
    print("  15 / 15  (Pos NOT in VC + homo)")
    print()

    return {
        'intersections': (odd_int, even_int),
        'differences': (odd_diff, even_diff),
        'verse_in_pos': (vip_count, vnip_count),
        'vip_parity': (vip_odd_homo, vip_odd_hetero),
        'vnip_even_parity': (vnip_even_homo, vnip_even_hetero),
        'pnvc_hetero': (pnvc_odd_hetero, pnvc_even_hetero),
        'pnvc_homo': (pnvc_odd_homo, pnvc_even_homo),
    }

if __name__ == "__main__":
    verify()
