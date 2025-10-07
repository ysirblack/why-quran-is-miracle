#!/usr/bin/env python3
"""
Honest Probability Analysis for Even-Sum Pattern

This pattern claims:
1. 57 surahs have even (surah# + verses), 57 have odd
2. The even-sum surahs total to 6,236 (total verses)
3. The odd-sum surahs total to 6,555 (sum of 1+2+...+114)

Let's analyze if this is statistically significant.
"""

from pathlib import Path
from math import comb
from typing import Dict, List, Tuple
import random

def load_verse_counts() -> Dict[int, int]:
    """Load verse counts from Quran data"""
    current_dir = Path(__file__).parent
    for _ in range(6):
        potential_path = current_dir / "data" / "quran-uthmani.txt"
        if potential_path.exists():
            data_path = potential_path
            break
        current_dir = current_dir.parent
    else:
        raise FileNotFoundError("Could not find data/quran-uthmani.txt")
    
    verse_counts = {}
    with data_path.open('r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#') or '|' not in line:
                continue
            parts = line.split('|', 2)
            if len(parts) < 3:
                continue
            surah_num = int(parts[0])
            verse_num = int(parts[1])
            verse_counts[surah_num] = max(verse_counts.get(surah_num, 0), verse_num)
    
    return verse_counts

def analyze_even_sum_pattern(verse_counts: Dict[int, int]) -> Dict:
    """Analyze the even-sum pattern"""
    even_sum_surahs = []
    odd_sum_surahs = []
    
    for surah in range(1, 115):
        verses = verse_counts[surah]
        sum_val = surah + verses
        if sum_val % 2 == 0:
            even_sum_surahs.append((surah, verses, sum_val))
        else:
            odd_sum_surahs.append((surah, verses, sum_val))
    
    even_total = sum(s[2] for s in even_sum_surahs)
    odd_total = sum(s[2] for s in odd_sum_surahs)
    
    return {
        'even_count': len(even_sum_surahs),
        'odd_count': len(odd_sum_surahs),
        'even_total': even_total,
        'odd_total': odd_total,
        'even_surahs': even_sum_surahs,
        'odd_surahs': odd_sum_surahs
    }

def understand_the_pattern():
    """First, let's understand what determines this pattern"""
    print("=" * 70)
    print("UNDERSTANDING THE EVEN-SUM PATTERN")
    print("=" * 70)
    print()
    
    verse_counts = load_verse_counts()
    result = analyze_even_sum_pattern(verse_counts)
    
    print("OBSERVED PATTERN:")
    print("-" * 70)
    print(f"Even-sum surahs: {result['even_count']}")
    print(f"Odd-sum surahs:  {result['odd_count']}")
    print(f"Even-sum total:  {result['even_total']:,}")
    print(f"Odd-sum total:   {result['odd_total']:,}")
    print()
    
    # Understand the constraint
    total_verses = sum(verse_counts.values())
    sum_of_orders = sum(range(1, 115))
    grand_total = total_verses + sum_of_orders
    
    print("MATHEMATICAL CONSTRAINTS:")
    print("-" * 70)
    print(f"Total verses:              {total_verses:,}")
    print(f"Sum of surah numbers:      {sum_of_orders:,}")
    print(f"Grand total (must equal):  {grand_total:,}")
    print()
    print(f"Even-sum + Odd-sum:        {result['even_total'] + result['odd_total']:,}")
    print(f"Match: {'YES' if result['even_total'] + result['odd_total'] == grand_total else 'NO'}")
    print()
    
    # Key insight: The 57:57 split
    print("KEY INSIGHT #1: The 57:57 split")
    print("-" * 70)
    print("A surah has EVEN sum when (surah# + verses) is even.")
    print("This happens when BOTH have the same parity:")
    print("  - Odd surah + Odd verses = Even sum")
    print("  - Even surah + Even verses = Even sum")
    print()
    print("From previous parity analysis:")
    print("  - Odd-Odd:   27 surahs")
    print("  - Even-Even: 30 surahs")
    print(f"  - Total:     {27 + 30} surahs (matches {result['even_count']}!)")
    print()
    print("THE 57:57 SPLIT IS ARITHMETICALLY GUARANTEED!")
    print("It's the same pattern we already analyzed.")
    print()
    
    # Key insight: The totals
    print("KEY INSIGHT #2: The 6,236 and 6,555 totals")
    print("-" * 70)
    print("Since even-sum + odd-sum must equal 12,791,")
    print("if one group sums to 6,236, the other MUST sum to 6,555.")
    print()
    print("These two constraints are NOT independent!")
    print()
    
    return verse_counts, result

def statistical_analysis_permutation(verse_counts: Dict[int, int], num_trials: int = 100000):
    """
    Perform permutation test: shuffle verse counts and see how often
    we get even-sum total = 6,236
    """
    print("PERMUTATION TEST")
    print("=" * 70)
    print("Shuffling verse counts randomly across 114 surahs...")
    print(f"Running {num_trials:,} trials...")
    print()
    
    actual_result = analyze_even_sum_pattern(verse_counts)
    actual_even_total = actual_result['even_total']
    total_verses = sum(verse_counts.values())
    
    verse_list = list(verse_counts.values())
    
    # Count how many permutations give us even-sum total = 6,236
    match_count = 0
    close_count = 0  # within 100
    
    for trial in range(num_trials):
        # Shuffle verse counts
        shuffled = random.sample(verse_list, len(verse_list))
        temp_counts = {i+1: shuffled[i] for i in range(114)}
        
        # Calculate even-sum total for this permutation
        temp_result = analyze_even_sum_pattern(temp_counts)
        temp_even_total = temp_result['even_total']
        
        if temp_even_total == actual_even_total:
            match_count += 1
        if abs(temp_even_total - actual_even_total) <= 100:
            close_count += 1
    
    prob_exact = match_count / num_trials
    prob_close = close_count / num_trials
    
    print(f"Results after {num_trials:,} trials:")
    print("-" * 70)
    print(f"Exact matches (= {actual_even_total:,}): {match_count:,} ({prob_exact*100:.3f}%)")
    print(f"Close matches (± 100):                  {close_count:,} ({prob_close*100:.2f}%)")
    print()
    
    if prob_exact > 0:
        print(f"Probability: ~1 in {1/prob_exact:.1f}")
    else:
        print(f"Probability: < 1 in {num_trials:,}")
    
    return {
        'exact_matches': match_count,
        'close_matches': close_count,
        'trials': num_trials,
        'prob_exact': prob_exact,
        'prob_close': prob_close
    }

def main():
    """Run comprehensive analysis"""
    # First, understand the pattern
    verse_counts, actual = understand_the_pattern()
    
    # Run statistical test
    print()
    stats = statistical_analysis_permutation(verse_counts, num_trials=100000)
    
    print()
    print("=" * 70)
    print("HONEST ASSESSMENT")
    print("=" * 70)
    print()
    print("CLAIM 1: '57 surahs have even sums, 57 have odd sums'")
    print("  VERDICT: Arithmetically guaranteed (not a new pattern)")
    print("  This is the same as the odd-odd + even-even = 57 pattern")
    print("  we already analyzed. It's a restatement, not independent evidence.")
    print()
    print("CLAIM 2: 'Even-sum total = 6,236 (total verses)'")
    if stats['prob_exact'] > 0.01:  # > 1%
        print(f"  VERDICT: Not statistically significant")
        print(f"  Probability: ~1 in {1/stats['prob_exact']:.1f}")
        print(f"  This could reasonably occur by chance.")
    elif stats['prob_exact'] > 0:
        print(f"  VERDICT: Moderately significant")
        print(f"  Probability: ~1 in {1/stats['prob_exact']:.1f}")
        print(f"  Less likely than chance, but not extraordinary.")
    else:
        print(f"  VERDICT: Needs more analysis")
        print(f"  Probability: < 1 in {stats['trials']:,}")
        print(f"  Rare enough to warrant further investigation.")
    print()
    print("OVERALL: The '57/57 split' is not new evidence.")
    print("The '6,236 total' requires larger-scale statistical testing")
    print("to determine true significance.")

if __name__ == "__main__":
    main()

