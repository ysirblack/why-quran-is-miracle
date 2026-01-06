#!/usr/bin/env python3
"""
Statistical test for pattern 15: 6236 Pattern

The pattern: 6236 is a "6236-like" number (ABCD where A=D and A=B×C)
and it sits at the EXACT CENTER of all 23 such numbers.

Test: What's the probability that a random total verse count would:
1. Be a 6236-like number
2. Be at the center position
"""
import random

N_TRIALS = 100_000

def is_6236_like(n):
    if n < 1000 or n > 9999: return False
    s = str(n)
    A, B, C, D = int(s[0]), int(s[1]), int(s[2]), int(s[3])
    return A == D and A == B * C

# Find all 6236-like numbers
ALL_6236_LIKE = [n for n in range(1000, 10000) if is_6236_like(n)]
CENTER_INDEX = len(ALL_6236_LIKE) // 2  # 11 (0-indexed)

def main():
    print("6236 PATTERN ANALYSIS")
    print("=" * 50)
    print(f"\nAll 6236-like numbers: {len(ALL_6236_LIKE)}")
    print(f"Center index: {CENTER_INDEX} (1-indexed: {CENTER_INDEX + 1})")
    print(f"Number at center: {ALL_6236_LIKE[CENTER_INDEX]}")
    print(f"Actual Quran total: 6236")

    # Check if 6236 is at center
    if 6236 in ALL_6236_LIKE:
        idx = ALL_6236_LIKE.index(6236)
        print(f"6236 is at index: {idx} (1-indexed: {idx + 1})")
        is_center = (idx == CENTER_INDEX)
        print(f"Is at center: {is_center}")
    else:
        print("6236 is NOT a 6236-like number!")
        return

    # Statistical test: What's the probability that a random number
    # in the plausible range is 6236-like AND at center?
    print("\n" + "=" * 50)
    print("MONTE CARLO TEST")
    print("Range: 4000-8000 (plausible total verse counts)")
    print("=" * 50)

    count_is_like = 0
    count_is_center = 0

    for i in range(N_TRIALS):
        # Generate random total in plausible range
        total = random.randint(4000, 8000)

        if is_6236_like(total):
            count_is_like += 1
            idx = ALL_6236_LIKE.index(total)
            if idx == CENTER_INDEX:
                count_is_center += 1

        if (i+1) % 20000 == 0:
            print(f"  {i+1:,} trials done...")

    p_like = count_is_like / N_TRIALS
    p_center = count_is_center / N_TRIALS

    print(f"\nResults:")
    print(f"  Is 6236-like: {count_is_like}/{N_TRIALS} = {p_like:.6f}")
    print(f"  Is at center: {count_is_center}/{N_TRIALS} = {p_center:.6f}")

    print(f"\np-value (being 6236-like AND at center): {p_center:.6f}")
    print(f"Significant (p<0.05): {'YES' if p_center < 0.05 else 'NO'}")

    # Theoretical calculation
    print("\n" + "=" * 50)
    print("THEORETICAL ANALYSIS")
    print("=" * 50)
    like_in_range = [n for n in ALL_6236_LIKE if 4000 <= n <= 8000]
    print(f"6236-like numbers in range 4000-8000: {len(like_in_range)}")
    print(f"Numbers: {like_in_range}")
    theoretical_p = 1 / (8000 - 4000 + 1) if 6236 in like_in_range else 0
    print(f"Theoretical p (exact 6236): {theoretical_p:.6f} = 1/{8000-4000+1}")

if __name__ == "__main__":
    random.seed(42)
    main()
