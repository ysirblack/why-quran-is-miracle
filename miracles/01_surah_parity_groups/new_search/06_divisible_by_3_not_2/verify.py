#!/usr/bin/env python3
"""
Divisible by 3 but NOT by 2 - Homogeneity Pattern
==================================================
Source: Simetrik Kitap: Kur'an, pages 179-189

Pattern:
- Property: n % 3 == 0 AND n % 2 != 0
- Homogeneous: Both position and verse have the property, or both don't
- Split by first half (1-57) and second half (58-114)

Result: 42/42/15/15 symmetry
- Homo: 42/42 (equal split between halves)
- Hetero: 15/15 (equal split between halves)
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

def div_by_3_not_2(n):
    """Returns True if n is divisible by 3 but NOT by 2"""
    return n % 3 == 0 and n % 2 != 0

def verify():
    vc = load_quran_data()

    homo_first = []
    homo_second = []
    hetero_first = []
    hetero_second = []

    for surah in range(1, 115):
        v = vc[surah]
        pos_prop = div_by_3_not_2(surah)
        verse_prop = div_by_3_not_2(v)

        is_homo = (pos_prop == verse_prop)
        is_first_half = surah <= 57

        if is_homo and is_first_half:
            homo_first.append((surah, v))
        elif is_homo and not is_first_half:
            homo_second.append((surah, v))
        elif not is_homo and is_first_half:
            hetero_first.append((surah, v))
        else:
            hetero_second.append((surah, v))

    print("=" * 60)
    print("DIVISIBLE BY 3 BUT NOT BY 2 - HOMOGENEITY")
    print("=" * 60)
    print()
    print(f"Homogeneous - First half (1-57):    {len(homo_first)}")
    print(f"Homogeneous - Second half (58-114): {len(homo_second)}")
    print(f"Heterogeneous - First half:         {len(hetero_first)}")
    print(f"Heterogeneous - Second half:        {len(hetero_second)}")
    print()
    print(f"Total Homogeneous:   {len(homo_first) + len(homo_second)}")
    print(f"Total Heterogeneous: {len(hetero_first) + len(hetero_second)}")
    print()

    if len(homo_first) == 42 and len(homo_second) == 42:
        print("✓ VERIFIED: Homo 42/42 (equal split)")
    if len(hetero_first) == 15 and len(hetero_second) == 15:
        print("✓ VERIFIED: Hetero 15/15 (equal split)")

    return {
        'homo_first': homo_first,
        'homo_second': homo_second,
        'hetero_first': hetero_first,
        'hetero_second': hetero_second
    }

if __name__ == "__main__":
    verify()
