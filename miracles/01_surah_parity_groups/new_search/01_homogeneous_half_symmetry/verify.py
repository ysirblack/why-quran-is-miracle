#!/usr/bin/env python3
"""
Homogeneous / Half Symmetry (28/29/29/28)
=========================================
Source: Simetrik Kitap: Kur'an, pages 74-76

Pattern:
- Homogeneous: Position and verse count have same parity (both odd or both even)
- Heterogeneous: Different parity
- First half: Surahs 1-57
- Second half: Surahs 58-114

Result: 28 / 29 / 29 / 28 mirror symmetry
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

    homo_first = []
    homo_second = []
    hetero_first = []
    hetero_second = []

    for surah in range(1, 115):
        vc = verse_counts[surah]
        pos_odd = surah % 2 == 1
        verse_odd = vc % 2 == 1
        homogeneous = (pos_odd == verse_odd)
        first_half = surah <= 57

        if homogeneous and first_half:
            homo_first.append((surah, vc))
        elif homogeneous and not first_half:
            homo_second.append((surah, vc))
        elif not homogeneous and first_half:
            hetero_first.append((surah, vc))
        else:
            hetero_second.append((surah, vc))

    print("=" * 60)
    print("HOMOGENEOUS / HALF SYMMETRY (28/29/29/28)")
    print("=" * 60)
    print()
    print(f"Homogeneous + First half (1-57):    {len(homo_first):2d}")
    print(f"Homogeneous + Second half (58-114): {len(homo_second):2d}")
    print(f"Heterogeneous + First half:         {len(hetero_first):2d}")
    print(f"Heterogeneous + Second half:        {len(hetero_second):2d}")
    print()
    print("SYMMETRY:")
    print(f"  [{len(homo_first)}] - [{len(homo_second)}] - [{len(hetero_first)}] - [{len(hetero_second)}]")
    print(f"   28  -  29  -  29  -  28  (Mirror symmetry)")
    print()
    print(f"Total homogeneous:   {len(homo_first) + len(homo_second)}")
    print(f"Total heterogeneous: {len(hetero_first) + len(hetero_second)}")
    print()

    # Verify
    expected = [28, 29, 29, 28]
    actual = [len(homo_first), len(homo_second), len(hetero_first), len(hetero_second)]

    if actual == expected:
        print("✓ VERIFIED: 28/29/29/28 symmetry exists")
    else:
        print(f"✗ ERROR: Expected {expected}, found {actual}")

    return {
        'homo_first': homo_first,
        'homo_second': homo_second,
        'hetero_first': hetero_first,
        'hetero_second': hetero_second
    }

if __name__ == "__main__":
    verify()
