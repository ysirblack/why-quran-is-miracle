#!/usr/bin/env python3
"""
Prime × Parity Combinations
===========================
Source: Simetrik Kitap: Kur'an, pages 112-115

Pattern:
- Combines prime homogeneity with parity homogeneity
- Creates 4 main categories and 4×4 sub-breakdowns

Note: This book considers 1 as a prime number.
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

    # Classify each surah
    prime_homo = []      # Both prime or both not prime
    prime_hetero = []    # One prime, one not
    parity_homo = []     # Both odd or both even
    parity_hetero = []   # One odd, one even

    # Combined categories
    prime_homo_parity_homo = []
    prime_homo_parity_hetero = []
    prime_hetero_parity_homo = []
    prime_hetero_parity_hetero = []

    # Detailed 4×4 breakdowns for prime homo
    ph_pos_odd_ver_odd = []
    ph_pos_even_ver_even = []
    ph_pos_odd_ver_even = []
    ph_pos_even_ver_odd = []

    # Detailed 4×4 breakdowns for prime hetero
    phe_pos_odd_ver_odd = []
    phe_pos_even_ver_even = []
    phe_pos_odd_ver_even = []
    phe_pos_even_ver_odd = []

    for surah in range(1, 115):
        vc = verse_counts[surah]
        pos_is_prime = is_prime(surah)
        verse_is_prime = is_prime(vc)
        pos_is_odd = surah % 2 == 1
        verse_is_odd = vc % 2 == 1

        # Prime homogeneity
        is_prime_homo = (pos_is_prime == verse_is_prime)
        if is_prime_homo:
            prime_homo.append((surah, vc))
        else:
            prime_hetero.append((surah, vc))

        # Parity homogeneity
        is_parity_homo = (pos_is_odd == verse_is_odd)
        if is_parity_homo:
            parity_homo.append((surah, vc))
        else:
            parity_hetero.append((surah, vc))

        # Combined categories
        if is_prime_homo and is_parity_homo:
            prime_homo_parity_homo.append((surah, vc))
        elif is_prime_homo and not is_parity_homo:
            prime_homo_parity_hetero.append((surah, vc))
        elif not is_prime_homo and is_parity_homo:
            prime_hetero_parity_homo.append((surah, vc))
        else:
            prime_hetero_parity_hetero.append((surah, vc))

        # 4×4 breakdown for prime homogeneous
        if is_prime_homo:
            if pos_is_odd and verse_is_odd:
                ph_pos_odd_ver_odd.append((surah, vc))
            elif not pos_is_odd and not verse_is_odd:
                ph_pos_even_ver_even.append((surah, vc))
            elif pos_is_odd and not verse_is_odd:
                ph_pos_odd_ver_even.append((surah, vc))
            else:
                ph_pos_even_ver_odd.append((surah, vc))

        # 4×4 breakdown for prime heterogeneous
        if not is_prime_homo:
            if pos_is_odd and verse_is_odd:
                phe_pos_odd_ver_odd.append((surah, vc))
            elif not pos_is_odd and not verse_is_odd:
                phe_pos_even_ver_even.append((surah, vc))
            elif pos_is_odd and not verse_is_odd:
                phe_pos_odd_ver_even.append((surah, vc))
            else:
                phe_pos_even_ver_odd.append((surah, vc))

    print("=" * 60)
    print("PRIME × PARITY COMBINATIONS")
    print("=" * 60)
    print()
    print("MAIN CATEGORIES (4 combinations):")
    print(f"  Prime homo + Parity homo:     {len(prime_homo_parity_homo)}")
    print(f"  Prime homo + Parity hetero:   {len(prime_homo_parity_hetero)}")
    print(f"  Prime hetero + Parity homo:   {len(prime_hetero_parity_homo)}")
    print(f"  Prime hetero + Parity hetero: {len(prime_hetero_parity_hetero)}")
    print()
    print(f"  Total: {len(prime_homo_parity_homo) + len(prime_homo_parity_hetero) + len(prime_hetero_parity_homo) + len(prime_hetero_parity_hetero)}")
    print()

    print("PRIME HOMOGENEOUS (67) - 4-way breakdown:")
    print(f"  Position odd, verse odd:   {len(ph_pos_odd_ver_odd)}")
    print(f"  Position even, verse even: {len(ph_pos_even_ver_even)}")
    print(f"  Position odd, verse even:  {len(ph_pos_odd_ver_even)}")
    print(f"  Position even, verse odd:  {len(ph_pos_even_ver_odd)}")
    print(f"  Total: {len(ph_pos_odd_ver_odd) + len(ph_pos_even_ver_even) + len(ph_pos_odd_ver_even) + len(ph_pos_even_ver_odd)}")
    print()

    print("PRIME HETEROGENEOUS (47) - 4-way breakdown:")
    print(f"  Position odd, verse odd:   {len(phe_pos_odd_ver_odd)}")
    print(f"  Position even, verse even: {len(phe_pos_even_ver_even)}")
    print(f"  Position odd, verse even:  {len(phe_pos_odd_ver_even)}")
    print(f"  Position even, verse odd:  {len(phe_pos_even_ver_odd)}")
    print(f"  Total: {len(phe_pos_odd_ver_odd) + len(phe_pos_even_ver_even) + len(phe_pos_odd_ver_even) + len(phe_pos_even_ver_odd)}")
    print()

    # Verify totals
    if len(prime_homo) == 67 and len(prime_hetero) == 47:
        print("✓ VERIFIED: Prime homogeneity 67/47")
    else:
        print(f"✗ ERROR: Expected 67/47, got {len(prime_homo)}/{len(prime_hetero)}")

    return {
        'prime_homo_parity_homo': prime_homo_parity_homo,
        'prime_homo_parity_hetero': prime_homo_parity_hetero,
        'prime_hetero_parity_homo': prime_hetero_parity_homo,
        'prime_hetero_parity_hetero': prime_hetero_parity_hetero,
        'ph_breakdown': {
            'odd_odd': ph_pos_odd_ver_odd,
            'even_even': ph_pos_even_ver_even,
            'odd_even': ph_pos_odd_ver_even,
            'even_odd': ph_pos_even_ver_odd
        },
        'phe_breakdown': {
            'odd_odd': phe_pos_odd_ver_odd,
            'even_even': phe_pos_even_ver_even,
            'odd_even': phe_pos_odd_ver_even,
            'even_odd': phe_pos_even_ver_odd
        }
    }

if __name__ == "__main__":
    verify()
