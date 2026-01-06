#!/usr/bin/env python3
"""
6236 Pattern
============
Source: Simetrik Kitap: Kur'an, pages 351-354

6236 = Total verse count in the Quran

Property: 4-digit number ABCD where:
- A = D (first = last)
- A = B × C (first = product of middle digits)

For 6236: 6 = 6, and 6 = 2 × 3 ✓

Remarkable findings:
- 23 such numbers exist (23 is PRIME!)
- 23 = middle digits of 6236 (2, 3)
- 23 = years of Quran revelation
- 6236 is at exact CENTER (position 12)
- 11 numbers above, 11 below (symmetry!)
- Digit sum above: 127, below: 254 (exactly 2×!)
- 5 odd above, 5 odd below
- 6 even above, 6 even below
"""

def is_6236_like(n):
    """Check if n has the 6236-like property"""
    if n < 1000 or n > 9999:
        return False
    s = str(n)
    A, B, C, D = int(s[0]), int(s[1]), int(s[2]), int(s[3])
    return A == D and A == B * C

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

def digit_sum(n):
    return sum(int(d) for d in str(n))

def verify():
    # Find all 6236-like numbers
    like_numbers = [n for n in range(1000, 10000) if is_6236_like(n)]

    print("=" * 60)
    print("6236 PATTERN")
    print("=" * 60)
    print()

    # Count check
    print(f"6236-like numbers found: {len(like_numbers)}")
    if len(like_numbers) == 23:
        print("✓ VERIFIED: 23 numbers")
        print(f"  ★ 23 is PRIME: {is_prime(23)}")
        print(f"  ★ 23 = middle digits of 6236 (2, 3)")
        print(f"  ★ 23 = years of Quran revelation")
    print()

    # List all numbers
    print("All 6236-like numbers:")
    for i, n in enumerate(like_numbers):
        s = str(n)
        marker = " ← 6236 (CENTER)" if n == 6236 else ""
        print(f"  {i+1:2d}. {n} ({s[0]}×{s[1]}×{s[2]}={s[3]}){marker}")
    print()

    # Position and symmetry
    pos_6236 = like_numbers.index(6236)
    above = like_numbers[:pos_6236]
    below = like_numbers[pos_6236+1:]

    print(f"Position of 6236: {pos_6236 + 1} (center of 23)")
    print(f"Numbers above: {len(above)}")
    print(f"Numbers below: {len(below)}")
    if len(above) == 11 and len(below) == 11:
        print("✓ VERIFIED: 11/11 symmetry")
    print()

    # Digit sums
    sum_above = sum(digit_sum(n) for n in above)
    sum_below = sum(digit_sum(n) for n in below)
    print(f"Digit sum above: {sum_above}")
    print(f"Digit sum below: {sum_below}")
    if sum_below == 2 * sum_above:
        print(f"✓ VERIFIED: {sum_below} = 2 × {sum_above}")
    print()

    # Odd/even
    odd_above = len([n for n in above if n % 2 == 1])
    even_above = len([n for n in above if n % 2 == 0])
    odd_below = len([n for n in below if n % 2 == 1])
    even_below = len([n for n in below if n % 2 == 0])

    print(f"Odd: {odd_above} above, {odd_below} below")
    print(f"Even: {even_above} above, {even_below} below")
    if odd_above == 5 and odd_below == 5:
        print("✓ VERIFIED: 5/5 odd symmetry")
    if even_above == 6 and even_below == 6:
        print("✓ VERIFIED: 6/6 even symmetry")

    return {
        'count': len(like_numbers),
        'position': pos_6236 + 1,
        'sum_above': sum_above,
        'sum_below': sum_below
    }

if __name__ == "__main__":
    verify()
