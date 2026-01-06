#!/usr/bin/env python3
"""
Prime Totals Pattern
====================
Source: Simetrik Kitap: Kur'an, page 108

Pattern:
- Sum of (position + verses) = 12791 → PRIME
- Sum of (position × verses) = 209029 → PRIME

Both key totals are prime numbers.
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
    verse_counts = load_quran_data()

    # Calculate sums
    sum_positions = sum(range(1, 115))  # 1+2+...+114 = 6555
    sum_verses = sum(verse_counts.values())  # 6236
    sum_total = sum_positions + sum_verses  # 12791
    sum_products = sum(s * verse_counts[s] for s in range(1, 115))  # 209029

    print("=" * 60)
    print("PRIME TOTALS PATTERN")
    print("=" * 60)
    print()
    print(f"Sum of positions (1-114):    {sum_positions}")
    print(f"  Is prime? {is_prime(sum_positions)}")
    print()
    print(f"Sum of verses:               {sum_verses}")
    print(f"  Is prime? {is_prime(sum_verses)}")
    print()
    print(f"Total (positions + verses):  {sum_total}")
    print(f"  Is prime? {is_prime(sum_total)} ✓")
    print()
    print(f"Sum of products (Σ pos×ver): {sum_products}")
    print(f"  Is prime? {is_prime(sum_products)} ✓")
    print()

    # Verify expected values
    all_correct = True

    if sum_total == 12791 and is_prime(sum_total):
        print("✓ VERIFIED: 12791 is prime")
    else:
        print(f"✗ ERROR: Expected 12791 prime, got {sum_total}")
        all_correct = False

    if sum_products == 209029 and is_prime(sum_products):
        print("✓ VERIFIED: 209029 is prime")
    else:
        print(f"✗ ERROR: Expected 209029 prime, got {sum_products}")
        all_correct = False

    return {
        'sum_positions': sum_positions,
        'sum_verses': sum_verses,
        'sum_total': sum_total,
        'sum_products': sum_products,
        'all_correct': all_correct
    }

if __name__ == "__main__":
    verify()
