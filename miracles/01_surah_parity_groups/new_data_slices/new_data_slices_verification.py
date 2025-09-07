#!/usr/bin/env python3
"""Verify six 19-surah block data slices: 2x2 parity grid and prime slices.

Basmalah counted only in Al-Fatihah.
Data source: data/quran-uthmani.txt (Tanzil Uthmani)
"""
from pathlib import Path
from math import isqrt


def load_quran_data():
    """Load Quran data from Tanzil format (quran-uthmani.txt).

    Returns a dict: {surah_number: [verse_numbers...]}
    """
    current_dir = Path(__file__).parent
    data_path = None

    # Search up to 6 levels up for the data directory
    for _ in range(6):
        potential_path = current_dir / "data" / "quran-uthmani.txt"
        if potential_path.exists():
            data_path = potential_path
            break
        current_dir = current_dir.parent

    if not data_path:
        raise FileNotFoundError("Could not find data/quran-uthmani.txt")

    verses = {}
    with data_path.open('r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            if '|' not in line:
                continue
            parts = line.split('|', 2)
            if len(parts) < 3:
                continue
            surah_num = int(parts[0])
            verse_num = int(parts[1])
            verses.setdefault(surah_num, []).append(verse_num)

    return verses


def is_prime_custom(n: int) -> bool:
    """Prime test treating 1 as prime per document convention.

    - 1 is treated as prime
    - 0 is not prime
    - Standard primality for n >= 2
    """
    if n == 1:
        return True
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    limit = isqrt(n)
    i = 3
    while i <= limit:
        if n % i == 0:
            return False
        i += 2
    return True


def compute_block_index(surah_number: int) -> int:
    """Return index 0..5 for six 19-surah blocks across 1..114"""
    return (surah_number - 1) // 19


def verify_new_data_slices():
    verses_data = load_quran_data()

    # Verse counts per surah
    verse_count_by_surah = {s: len(verses_data.get(s, [])) for s in range(1, 115)}

    # Initialize counts for six blocks
    odd_odd = [0] * 6
    even_odd = [0] * 6
    odd_even = [0] * 6
    even_even = [0] * 6

    homogeneous = [0] * 6
    heterogeneous = [0] * 6

    prime_homogeneous = [0] * 6
    prime_heterogeneous = [0] * 6

    # Populate
    for surah in range(1, 115):
        count = verse_count_by_surah[surah]
        block = compute_block_index(surah)

        order_is_odd = (surah % 2 == 1)
        ayat_is_odd = (count % 2 == 1)

        # 2x2 parity grid
        if order_is_odd and ayat_is_odd:
            odd_odd[block] += 1
        elif (not order_is_odd) and ayat_is_odd:
            even_odd[block] += 1
        elif order_is_odd and (not ayat_is_odd):
            odd_even[block] += 1
        else:
            even_even[block] += 1

        # Homogeneous vs heterogeneous (by parity)
        if order_is_odd == ayat_is_odd:
            homogeneous[block] += 1
            # Parity-equal paths land here (odd-odd or even-even)
        else:
            heterogeneous[block] += 1

        # Prime slices (treat 1 as prime)
        order_is_prime = is_prime_custom(surah)
        ayat_is_prime = is_prime_custom(count)
        if order_is_prime == ayat_is_prime:
            prime_homogeneous[block] += 1
        else:
            prime_heterogeneous[block] += 1

    def parity_pattern(values):
        return '-'.join('O' if v % 2 == 1 else 'E' for v in values)

    # Expected arrays from the research doc
    expected = {
        'odd_odd': [6, 5, 4, 1, 4, 7],
        'even_odd': [4, 3, 8, 3, 4, 5],
        'odd_even': [4, 4, 6, 8, 6, 2],
        'even_even': [5, 7, 1, 7, 5, 5],
        'homogeneous': [11, 12, 5, 8, 9, 12],
        'heterogeneous': [8, 7, 14, 11, 10, 7],
        'prime_homogeneous': [11, 12, 11, 10, 11, 12],
        'prime_heterogeneous': [8, 7, 8, 9, 8, 7],
    }

    actual = {
        'odd_odd': odd_odd,
        'even_odd': even_odd,
        'odd_even': odd_even,
        'even_even': even_even,
        'homogeneous': homogeneous,
        'heterogeneous': heterogeneous,
        'prime_homogeneous': prime_homogeneous,
        'prime_heterogeneous': prime_heterogeneous,
    }

    print("SIX 19-SURAH BLOCKS — COUNTS")
    print("=" * 60)
    for key in ['odd_odd', 'even_odd', 'odd_even', 'even_even']:
        print(f"{key.replace('_', '-').upper():>18}: {actual[key]}  | parity {parity_pattern(actual[key])}")
    print("-" * 60)
    for key in ['homogeneous', 'heterogeneous']:
        print(f"{key.replace('_', ' ').title():>18}: {actual[key]}  | parity {parity_pattern(actual[key])}")
    print("-" * 60)
    for key in ['prime_homogeneous', 'prime_heterogeneous']:
        print(f"{key.replace('_', ' ').title():>18}: {actual[key]}")

    print("\nVERIFICATION")
    print("-" * 60)
    all_match = True
    for key in expected:
        match = (actual[key] == expected[key])
        print(f"{key:>18}: {'SUCCESS' if match else 'MISMATCH'}  (expected {expected[key]}, got {actual[key]})")
        if not match:
            all_match = False

    print("-" * 60)
    print(f"Overall: {'SUCCESS' if all_match else 'CHECK DIFFERENCES'}")

    return {
        'success': all_match,
        **actual,
    }


if __name__ == "__main__":
    verify_new_data_slices()
