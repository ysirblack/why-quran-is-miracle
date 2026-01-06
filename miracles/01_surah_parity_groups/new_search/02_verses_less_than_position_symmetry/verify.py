#!/usr/bin/env python3
"""
Verses Less Than Position Symmetry (34/32/32/34)
=================================================
Source: Simetrik Kitap: Kur'an, page 91

Pattern:
- Filter: Surahs where verse count < position number (66 surahs)
- Split by: Difference parity AND Position parity

Result: 34 / 32 / 32 / 34 mirror symmetry
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

def verify():
    verse_counts = load_quran_data()

    # Filter: verses < position
    less_than = [(s, verse_counts[s]) for s in range(1, 115) if verse_counts[s] < s]

    # By difference parity (verses - position)
    diff_odd = [(s, vc) for s, vc in less_than if (vc - s) % 2 != 0]
    diff_even = [(s, vc) for s, vc in less_than if (vc - s) % 2 == 0]

    # By position parity
    pos_odd = [(s, vc) for s, vc in less_than if s % 2 == 1]
    pos_even = [(s, vc) for s, vc in less_than if s % 2 == 0]

    print("=" * 60)
    print("VERSES < POSITION SYMMETRY (34/32/32/34)")
    print("=" * 60)
    print()
    print(f"Total surahs (verses < position): {len(less_than)}")
    print()
    print("By DIFFERENCE parity (verses - position):")
    print(f"  Difference is ODD:  {len(diff_odd)}")
    print(f"  Difference is EVEN: {len(diff_even)}")
    print()
    print("By POSITION parity:")
    print(f"  Position is ODD:  {len(pos_odd)}")
    print(f"  Position is EVEN: {len(pos_even)}")
    print()
    print("SYMMETRY:")
    print(f"  [{len(diff_odd)}] - [{len(diff_even)}] - [{len(pos_odd)}] - [{len(pos_even)}]")
    print(f"   34  -  32  -  32  -  34  (Mirror symmetry)")
    print()

    # Verify
    expected = [34, 32, 32, 34]
    actual = [len(diff_odd), len(diff_even), len(pos_odd), len(pos_even)]

    if actual == expected:
        print("✓ VERIFIED: 34/32/32/34 symmetry exists")
    else:
        print(f"✗ ERROR: Expected {expected}, found {actual}")

    return {
        'diff_odd': diff_odd,
        'diff_even': diff_even,
        'pos_odd': pos_odd,
        'pos_even': pos_even
    }

if __name__ == "__main__":
    verify()
