#!/usr/bin/env python3
"""
Primality Meta-Pattern
======================
Source: Simetrik Kitap: Kur'an, pages 118-134

Discovery:
Every breakdown of 4 numbers follows the SAME primality pattern:
NOT PRIME, PRIME, PRIME, NOT PRIME

This applies to all 4 groups:
1. (8, 59, 23, 24)   - Prime category counts
2. (44, 23, 13, 34)  - Prime × Parity combinations
3. (15, 29, 11, 12)  - Prime homogeneous 4-way breakdown
4. (12, 1, 19, 15)   - Prime heterogeneous 4-way breakdown

Note: This book considers 1 as a prime number.
"""

from pathlib import Path

def is_prime_standard(n):
    """Standard primality check (1 is NOT prime)"""
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

def is_prime_book(n):
    """Book's primality check (1 IS prime)"""
    if n == 1:
        return True
    return is_prime_standard(n)

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

    # Calculate all categories
    both_prime = 0
    both_not_prime = 0
    pos_prime_only = 0
    verse_prime_only = 0

    prime_homo_parity_homo = 0
    prime_homo_parity_hetero = 0
    prime_hetero_parity_homo = 0
    prime_hetero_parity_hetero = 0

    ph_odd_odd = 0
    ph_even_even = 0
    ph_odd_even = 0
    ph_even_odd = 0

    phe_odd_odd = 0
    phe_even_even = 0
    phe_odd_even = 0
    phe_even_odd = 0

    for surah in range(1, 115):
        vc = verse_counts[surah]
        pos_is_prime = is_prime_book(surah)
        verse_is_prime = is_prime_book(vc)
        pos_is_odd = surah % 2 == 1
        verse_is_odd = vc % 2 == 1

        # Group 1: Prime category counts
        if pos_is_prime and verse_is_prime:
            both_prime += 1
        elif not pos_is_prime and not verse_is_prime:
            both_not_prime += 1
        elif pos_is_prime and not verse_is_prime:
            pos_prime_only += 1
        else:
            verse_prime_only += 1

        # Prime and parity homogeneity
        is_prime_homo = (pos_is_prime == verse_is_prime)
        is_parity_homo = (pos_is_odd == verse_is_odd)

        # Group 2: Prime × Parity combinations
        if is_prime_homo and is_parity_homo:
            prime_homo_parity_homo += 1
        elif is_prime_homo and not is_parity_homo:
            prime_homo_parity_hetero += 1
        elif not is_prime_homo and is_parity_homo:
            prime_hetero_parity_homo += 1
        else:
            prime_hetero_parity_hetero += 1

        # Group 3: Prime homogeneous 4-way
        if is_prime_homo:
            if pos_is_odd and verse_is_odd:
                ph_odd_odd += 1
            elif not pos_is_odd and not verse_is_odd:
                ph_even_even += 1
            elif pos_is_odd and not verse_is_odd:
                ph_odd_even += 1
            else:
                ph_even_odd += 1

        # Group 4: Prime heterogeneous 4-way
        if not is_prime_homo:
            if pos_is_odd and verse_is_odd:
                phe_odd_odd += 1
            elif not pos_is_odd and not verse_is_odd:
                phe_even_even += 1
            elif pos_is_odd and not verse_is_odd:
                phe_odd_even += 1
            else:
                phe_even_odd += 1

    # Define the 4 groups
    groups = [
        ("Prime category counts", (both_prime, both_not_prime, pos_prime_only, verse_prime_only)),
        ("Prime × Parity combinations", (prime_homo_parity_homo, prime_homo_parity_hetero, prime_hetero_parity_homo, prime_hetero_parity_hetero)),
        ("Prime homo 4-way", (ph_odd_odd, ph_even_even, ph_odd_even, ph_even_odd)),
        ("Prime hetero 4-way", (phe_odd_odd, phe_even_even, phe_odd_even, phe_even_odd)),
    ]

    expected_groups = [
        (8, 59, 23, 24),
        (44, 23, 13, 34),
        (15, 29, 11, 12),
        (12, 1, 19, 15),
    ]

    expected_pattern = [False, True, True, False]  # NOT, PRIME, PRIME, NOT

    print("=" * 70)
    print("PRIMALITY META-PATTERN")
    print("=" * 70)
    print()
    print("Every group of 4 follows: NOT PRIME, PRIME, PRIME, NOT PRIME")
    print("(Note: 1 is considered PRIME per the book)")
    print()

    all_verified = True
    for i, ((name, actual), expected) in enumerate(zip(groups, expected_groups)):
        # Use book's definition: 1 is prime
        primality = [is_prime_book(n) for n in actual]
        pattern_ok = primality == expected_pattern
        values_ok = actual == expected

        print(f"Group {i+1}: {name}")
        print(f"  Values:    {actual}")
        print(f"  Expected:  {expected}")
        print(f"  Primality: {['PRIME' if p else 'NOT' for p in primality]}")

        if values_ok and pattern_ok:
            print(f"  ✓ Values match AND pattern is NOT-PRIME-PRIME-NOT")
        else:
            if not values_ok:
                print(f"  ✗ Values don't match!")
            if not pattern_ok:
                print(f"  ✗ Pattern doesn't match!")
            all_verified = False
        print()

    print("=" * 70)
    if all_verified:
        print("✓ ALL 4 GROUPS VERIFIED")
        print("✓ META-PATTERN CONFIRMED: NOT, PRIME, PRIME, NOT")
    else:
        print("✗ VERIFICATION FAILED")
    print("=" * 70)

    return {
        'groups': groups,
        'all_verified': all_verified
    }

if __name__ == "__main__":
    verify()
