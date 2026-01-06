#!/usr/bin/env python3
"""
Prime Factor Sum (a₀) Patterns
==============================
Source: Simetrik Kitap: Kur'an, pages 191-221

a₀(n) = sum of prime factors with multiplicity
Example: a₀(12) = 2+2+3 = 7 (since 12 = 2² × 3)
Special case: a₀(1) = 1 (as per book)

Key patterns:
- 71/71 (both prime!): a₀(verse) odd / a₀(pos) odd
- 43/43 (both prime!): a₀(verse) even / a₀(pos) even
- 60/54: a₀(verse) prime / NOT prime
- 27/27/33/33: a₀(verse) prime first/second, verse even first/second
- 30/30/24/24: a₀(verse) NOT prime first/second, verse odd first/second
"""

from pathlib import Path

def prime_factor_sum(n):
    """Calculate a₀(n) = sum of prime factors with multiplicity. a₀(1) = 1"""
    if n == 1:
        return 1  # Book considers a₀(1) = 1
    if n <= 0:
        return 0
    total = 0
    d = 2
    temp = n
    while d * d <= temp:
        while temp % d == 0:
            total += d
            temp //= d
        d += 1
    if temp > 1:
        total += temp
    return total

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

    a0_verse_odd = []
    a0_pos_odd = []
    a0_verse_even = []
    a0_pos_even = []
    a0_verse_prime = []
    a0_verse_not_prime = []

    for surah in range(1, 115):
        v = vc[surah]
        a0_v = prime_factor_sum(v)
        a0_p = prime_factor_sum(surah)

        if a0_v % 2 == 1:
            a0_verse_odd.append((surah, v))
        else:
            a0_verse_even.append((surah, v))

        if a0_p % 2 == 1:
            a0_pos_odd.append((surah, v))
        else:
            a0_pos_even.append((surah, v))

        if is_prime(a0_v):
            a0_verse_prime.append((surah, v))
        else:
            a0_verse_not_prime.append((surah, v))

    print("=" * 60)
    print("PRIME FACTOR SUM (a₀) PATTERNS")
    print("=" * 60)
    print()

    # Pattern 1: 71/71
    print(f"a₀(verse) odd:  {len(a0_verse_odd)}")
    print(f"a₀(pos) odd:    {len(a0_pos_odd)}")
    if len(a0_verse_odd) == 71 and len(a0_pos_odd) == 71:
        print(f"✓ VERIFIED: 71/71 - BOTH ARE PRIME!")
    print()

    # Pattern 2: 43/43
    print(f"a₀(verse) even: {len(a0_verse_even)}")
    print(f"a₀(pos) even:   {len(a0_pos_even)}")
    if len(a0_verse_even) == 43 and len(a0_pos_even) == 43:
        print(f"✓ VERIFIED: 43/43 - BOTH ARE PRIME!")
    print()

    # Pattern 3: 60/54
    print(f"a₀(verse) prime:     {len(a0_verse_prime)}")
    print(f"a₀(verse) NOT prime: {len(a0_verse_not_prime)}")
    if len(a0_verse_prime) == 60 and len(a0_verse_not_prime) == 54:
        print("✓ VERIFIED: 60/54")
    print()

    # Pattern 4: 27/27/33/33
    a0v_prime_first = len([x for x in a0_verse_prime if x[0] <= 57])
    a0v_prime_second = len([x for x in a0_verse_prime if x[0] > 57])
    verse_even_first = len([x for x in vc.items() if x[1] % 2 == 0 and x[0] <= 57])
    verse_even_second = len([x for x in vc.items() if x[1] % 2 == 0 and x[0] > 57])

    print(f"a₀(verse) prime - first:  {a0v_prime_first}")
    print(f"Verse even - first:       {verse_even_first}")
    print(f"a₀(verse) prime - second: {a0v_prime_second}")
    print(f"Verse even - second:      {verse_even_second}")
    if (a0v_prime_first == 27 and verse_even_first == 27 and
        a0v_prime_second == 33 and verse_even_second == 33):
        print("✓ VERIFIED: 27/27/33/33")
    print()

    # Pattern 5: 30/30/24/24
    a0v_not_prime_first = len([x for x in a0_verse_not_prime if x[0] <= 57])
    a0v_not_prime_second = len([x for x in a0_verse_not_prime if x[0] > 57])
    verse_odd_first = len([x for x in vc.items() if x[1] % 2 == 1 and x[0] <= 57])
    verse_odd_second = len([x for x in vc.items() if x[1] % 2 == 1 and x[0] > 57])

    print(f"a₀(verse) NOT prime - first:  {a0v_not_prime_first}")
    print(f"Verse odd - first:            {verse_odd_first}")
    print(f"a₀(verse) NOT prime - second: {a0v_not_prime_second}")
    print(f"Verse odd - second:           {verse_odd_second}")
    if (a0v_not_prime_first == 30 and verse_odd_first == 30 and
        a0v_not_prime_second == 24 and verse_odd_second == 24):
        print("✓ VERIFIED: 30/30/24/24")

    return {
        'a0_verse_odd': len(a0_verse_odd),
        'a0_pos_odd': len(a0_pos_odd),
        'a0_verse_even': len(a0_verse_even),
        'a0_pos_even': len(a0_pos_even),
        'a0_verse_prime': len(a0_verse_prime),
        'a0_verse_not_prime': len(a0_verse_not_prime)
    }

if __name__ == "__main__":
    verify()
