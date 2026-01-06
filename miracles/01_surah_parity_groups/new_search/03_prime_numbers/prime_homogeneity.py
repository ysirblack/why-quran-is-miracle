#!/usr/bin/env python3
"""
Prime Homogeneity Pattern (67/47)
==================================
Source: Simetrik Kitap: Kur'an, pages 112-115

Pattern:
- Türdeş (Homogeneous): Both position AND verse count are prime, or both are NOT prime
- Türdeş Olmayan (Heterogeneous): One is prime, the other is not

Note: This book considers 1 as a prime number.

Result: 67 homogeneous / 47 heterogeneous
"""

from pathlib import Path

def is_prime(n):
    """Check if n is prime (with 1 considered as prime per the book)"""
    if n == 1:
        return True  # Book considers 1 as prime
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
    verse_counts = load_quran_data()

    both_prime = []
    both_not_prime = []
    pos_prime_only = []
    verse_prime_only = []

    for surah in range(1, 115):
        vc = verse_counts[surah]
        pos_is_prime = is_prime(surah)
        verse_is_prime = is_prime(vc)

        if pos_is_prime and verse_is_prime:
            both_prime.append((surah, vc))
        elif not pos_is_prime and not verse_is_prime:
            both_not_prime.append((surah, vc))
        elif pos_is_prime and not verse_is_prime:
            pos_prime_only.append((surah, vc))
        else:
            verse_prime_only.append((surah, vc))

    turdes = len(both_prime) + len(both_not_prime)
    turdes_olmayan = len(pos_prime_only) + len(verse_prime_only)

    print("=" * 60)
    print("PRIME HOMOGENEITY PATTERN (67/47)")
    print("=" * 60)
    print()
    print("HOMOGENEOUS (Türdeş):")
    print(f"  Both prime:      {len(both_prime)}")
    print(f"  Both NOT prime:  {len(both_not_prime)}")
    print(f"  TOTAL:           {turdes}")
    print()
    print("HETEROGENEOUS (Türdeş Olmayan):")
    print(f"  Position prime only:  {len(pos_prime_only)}")
    print(f"  Verse prime only:     {len(verse_prime_only)}")
    print(f"  TOTAL:                {turdes_olmayan}")
    print()
    print(f"Grand total: {turdes} + {turdes_olmayan} = {turdes + turdes_olmayan}")
    print()

    # Verify
    if turdes == 67 and turdes_olmayan == 47:
        print("✓ VERIFIED: 67/47 pattern confirmed")
    else:
        print(f"✗ ERROR: Expected 67/47, got {turdes}/{turdes_olmayan}")

    print()
    print("Both prime surahs:")
    for s, vc in both_prime:
        print(f"  Surah {s:3d}: {vc:3d} verses")

    return {
        'both_prime': both_prime,
        'both_not_prime': both_not_prime,
        'pos_prime_only': pos_prime_only,
        'verse_prime_only': verse_prime_only,
        'turdes': turdes,
        'turdes_olmayan': turdes_olmayan
    }

if __name__ == "__main__":
    verify()
