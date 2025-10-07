#!/usr/bin/env python3
"""
Honest Probability Analysis for Verse > Number Pattern

Claims: 48 surahs where verses > number show 23/25 swap pattern
between two classification methods.

Test if this is statistically significant.
"""

from pathlib import Path
from typing import Dict, List
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

def analyze_pattern(verse_counts: Dict[int, int]) -> Dict:
    """Analyze the verse > number pattern"""
    # Filter: verses > number
    filtered = [(num, count) for num, count in verse_counts.items() 
                if count > num]
    
    # Classification 1: by (verses - number) parity
    result_odd = sum(1 for num, count in filtered if (count - num) % 2 == 1)
    result_even = sum(1 for num, count in filtered if (count - num) % 2 == 0)
    
    # Classification 2: by surah number parity
    order_odd = sum(1 for num, count in filtered if num % 2 == 1)
    order_even = sum(1 for num, count in filtered if num % 2 == 0)
    
    return {
        'filtered_count': len(filtered),
        'result_odd': result_odd,
        'result_even': result_even,
        'order_odd': order_odd,
        'order_even': order_even,
        'swap_pattern': (result_odd == order_even and result_even == order_odd)
    }

def understand_pattern():
    """First understand the pattern and independence"""
    print("=" * 70)
    print("UNDERSTANDING THE VERSE > NUMBER PATTERN")
    print("=" * 70)
    print()
    
    verse_counts = load_verse_counts()
    result = analyze_pattern(verse_counts)
    
    print("OBSERVED PATTERN:")
    print("-" * 70)
    print(f"Filtered (verses > number):  {result['filtered_count']}")
    print()
    print(f"Classification 1 - Result Parity:")
    print(f"  (verses - number) is odd:  {result['result_odd']}")
    print(f"  (verses - number) is even: {result['result_even']}")
    print()
    print(f"Classification 2 - Order Parity:")
    print(f"  Surah number is odd:       {result['order_odd']}")
    print(f"  Surah number is even:      {result['order_even']}")
    print()
    print(f"Swap pattern exists: {result['swap_pattern']}")
    print()
    
    # Check independence
    print("KEY INSIGHT: Independence Check")
    print("-" * 70)
    print()
    print("Question 1: How many surahs have verses > number?")
    print(f"  Answer: {result['filtered_count']} surahs")
    print("  This is FIXED by the data, not a random variable")
    print()
    print("Question 2: Of these 48, how many are odd-numbered?")
    print(f"  Answer: {result['order_odd']} odd, {result['order_even']} even")
    print("  This is FIXED (which surahs pass the filter)")
    print()
    print("Question 3: Of these 48, is (verses - number) parity independent?")
    print("  Let's think: if verses and number have same parity,")
    print("  then (verses - number) is EVEN.")
    print("  If they have different parity, (verses - number) is ODD.")
    print()
    print("  So result_parity depends on whether verse_parity == order_parity!")
    print()
    print("Question 4: Are these two classifications independent?")
    print("  Classification 1: Tests (verses - number) parity")
    print("  Classification 2: Tests surah number parity")
    print()
    print("  Since verse counts can be permuted independently,")
    print("  these classifications COULD be independent.")
    print()
    
    return verse_counts, result

def permutation_test(verse_counts: Dict[int, int], num_trials: int = 1000000):
    """Test by permuting verse counts"""
    print("=" * 70)
    print("PERMUTATION TEST")
    print("=" * 70)
    print()
    
    print(f"Running {num_trials:,} permutation trials...")
    print("Shuffling verse counts among the 114 surahs...")
    print()
    
    actual_result = analyze_pattern(verse_counts)
    
    # Count different types of matches
    match_filtered_count = 0
    match_swap_pattern = 0
    match_exact_23_25 = 0
    match_all = 0
    
    verse_list = list(verse_counts.values())
    
    for trial in range(num_trials):
        shuffled = random.sample(verse_list, len(verse_list))
        temp_counts = {i+1: shuffled[i] for i in range(114)}
        temp_result = analyze_pattern(temp_counts)
        
        # How many get 48 filtered?
        if temp_result['filtered_count'] == actual_result['filtered_count']:
            match_filtered_count += 1
            
            # Of those with 48 filtered, how many get swap pattern?
            if temp_result['swap_pattern']:
                match_swap_pattern += 1
                
                # Of those with swap, how many get exact 23/25?
                if (temp_result['result_odd'] == 23 and 
                    temp_result['result_even'] == 25):
                    match_exact_23_25 += 1
        
        # How many match everything?
        if (temp_result['filtered_count'] == actual_result['filtered_count'] and
            temp_result['result_odd'] == actual_result['result_odd'] and
            temp_result['result_even'] == actual_result['result_even'] and
            temp_result['order_odd'] == actual_result['order_odd'] and
            temp_result['order_even'] == actual_result['order_even']):
            match_all += 1
    
    print("Results:")
    print("-" * 70)
    
    prob_filtered = match_filtered_count / num_trials
    print(f"Step 1: Get exactly 48 filtered")
    print(f"  Matches: {match_filtered_count:,} / {num_trials:,}")
    print(f"  Probability: ~1 in {1/prob_filtered if prob_filtered > 0 else float('inf'):.1f} ({prob_filtered*100:.2f}%)")
    print()
    
    if match_filtered_count > 0:
        prob_swap_given_48 = match_swap_pattern / match_filtered_count
        print(f"Step 2: Given 48 filtered, get swap pattern")
        print(f"  Matches: {match_swap_pattern:,} / {match_filtered_count:,}")
        print(f"  Probability: ~1 in {1/prob_swap_given_48 if prob_swap_given_48 > 0 else float('inf'):.1f} ({prob_swap_given_48*100:.2f}%)")
        print()
        
        if match_swap_pattern > 0:
            prob_23_25_given_swap = match_exact_23_25 / match_swap_pattern
            print(f"Step 3: Given swap, get exactly 23/25")
            print(f"  Matches: {match_exact_23_25:,} / {match_swap_pattern:,}")
            print(f"  Probability: ~1 in {1/prob_23_25_given_swap if prob_23_25_given_swap > 0 else float('inf'):.1f} ({prob_23_25_given_swap*100:.2f}%)")
            print()
    
    prob_all = match_all / num_trials
    print(f"Overall: All conditions simultaneously")
    print(f"  Matches: {match_all:,} / {num_trials:,}")
    if prob_all > 0:
        print(f"  Probability: ~1 in {1/prob_all:.1f} ({prob_all*100:.4f}%)")
    else:
        print(f"  Probability: < 1 in {num_trials:,}")
    print()
    
    return {
        'match_filtered_count': match_filtered_count,
        'match_swap_pattern': match_swap_pattern,
        'match_exact_23_25': match_exact_23_25,
        'match_all': match_all,
        'trials': num_trials,
        'prob_all': prob_all
    }

def main():
    """Run comprehensive analysis"""
    # Understand the pattern
    verse_counts, actual = understand_pattern()
    
    # Run permutation test
    print()
    stats = permutation_test(verse_counts, num_trials=1000000)
    
    print()
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print()
    print("Pattern components:")
    print("  1. Exactly 48 surahs have verses > number")
    print("  2. Two classification methods both give 23/25 split")
    print("  3. The 23 and 25 swap between methods")
    print()
    
    if stats['prob_all'] > 0:
        print(f"Overall probability: ~1 in {1/stats['prob_all']:.1f}")
    else:
        print(f"Overall probability: < 1 in {stats['trials']:,}")
    print()
    print("The probability depends heavily on:")
    print("  - How common it is to get exactly 48 filtered")
    print("  - Given 48, how likely is the swap pattern")
    print()
    print("Note: The 'order parity' split is FIXED once we know")
    print("which 48 surahs pass the filter. The randomness is in")
    print("which verse counts get assigned to which surah positions.")

if __name__ == "__main__":
    main()

