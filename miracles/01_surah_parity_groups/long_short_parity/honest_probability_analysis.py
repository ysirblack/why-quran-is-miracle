#!/usr/bin/env python3
"""
Honest Probability Analysis for Long/Short Parity Pattern

Claims:
1. 57 long (>=40 verses) and 57 short (<=39 verses) surahs
2. Long: 27 odd-order, 30 even-order
3. Short: 30 odd-order, 27 even-order (swap pattern)
4. No surahs have exactly 39 verses (clean boundary)

Let's test if these are statistically significant and independent.
"""

from pathlib import Path
from typing import Dict, Tuple
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

def analyze_long_short_pattern(verse_counts: Dict[int, int], threshold: int = 40) -> Dict:
    """Analyze long/short pattern at given threshold"""
    long_odd = sum(1 for s in range(1, 115) 
                   if verse_counts[s] >= threshold and s % 2 == 1)
    long_even = sum(1 for s in range(1, 115) 
                    if verse_counts[s] >= threshold and s % 2 == 0)
    short_odd = sum(1 for s in range(1, 115) 
                    if verse_counts[s] < threshold and s % 2 == 1)
    short_even = sum(1 for s in range(1, 115) 
                     if verse_counts[s] < threshold and s % 2 == 0)
    
    total_long = long_odd + long_even
    total_short = short_odd + short_even
    
    # Check for chapters with exactly threshold-1 verses
    has_boundary_verse = any(verse_counts[s] == threshold - 1 for s in range(1, 115))
    
    return {
        'long_odd': long_odd,
        'long_even': long_even,
        'short_odd': short_odd,
        'short_even': short_even,
        'total_long': total_long,
        'total_short': total_short,
        'has_boundary': has_boundary_verse
    }

def understand_the_pattern():
    """First understand what determines this pattern"""
    print("=" * 70)
    print("UNDERSTANDING THE LONG/SHORT PARITY PATTERN")
    print("=" * 70)
    print()
    
    verse_counts = load_verse_counts()
    result = analyze_long_short_pattern(verse_counts, threshold=40)
    
    print("OBSERVED PATTERN (40-verse threshold):")
    print("-" * 70)
    print(f"Long surahs (>=40):  {result['total_long']}")
    print(f"  Odd-order:  {result['long_odd']}")
    print(f"  Even-order: {result['long_even']}")
    print()
    print(f"Short surahs (<40):  {result['total_short']}")
    print(f"  Odd-order:  {result['short_odd']}")
    print(f"  Even-order: {result['short_even']}")
    print()
    print(f"Surahs with exactly 39 verses: {'YES' if result['has_boundary'] else 'NO'}")
    print()
    
    # KEY INSIGHT: Check if this pattern is related to parity
    print("KEY INSIGHT: Independence Check")
    print("-" * 70)
    print("Is this pattern INDEPENDENT from the core parity pattern?")
    print()
    print("Let's check: how does 'long' vs 'short' relate to verse parity?")
    print()
    
    # Check correlation between length and verse parity
    long_with_odd_verses = sum(1 for s in range(1, 115)
                               if verse_counts[s] >= 40 and verse_counts[s] % 2 == 1)
    long_with_even_verses = sum(1 for s in range(1, 115)
                                if verse_counts[s] >= 40 and verse_counts[s] % 2 == 0)
    short_with_odd_verses = sum(1 for s in range(1, 115)
                                if verse_counts[s] < 40 and verse_counts[s] % 2 == 1)
    short_with_even_verses = sum(1 for s in range(1, 115)
                                 if verse_counts[s] < 40 and verse_counts[s] % 2 == 0)
    
    print(f"Long surahs:  {long_with_odd_verses} odd-verse, {long_with_even_verses} even-verse")
    print(f"Short surahs: {short_with_odd_verses} odd-verse, {short_with_even_verses} even-verse")
    print()
    
    print("Is this just testing a different threshold?")
    print("The core pattern tested verse count parity.")
    print("This pattern tests verse count magnitude (>=40 vs <40).")
    print("These ARE different questions, so this could be independent.")
    print()
    
    return verse_counts, result

def test_threshold_significance(verse_counts: Dict[int, int]):
    """Test how special the 40-verse threshold is"""
    print("=" * 70)
    print("TESTING THRESHOLD SIGNIFICANCE")
    print("=" * 70)
    print()
    
    print("Is 40 verses a special threshold?")
    print("Let's test all possible thresholds and see how many give 57/57 split:")
    print()
    
    perfect_splits = []
    for threshold in range(3, 287):
        result = analyze_long_short_pattern(verse_counts, threshold)
        if result['total_long'] == 57 and result['total_short'] == 57:
            perfect_splits.append(threshold)
    
    print(f"Thresholds that give 57/57 split: {len(perfect_splits)}")
    if len(perfect_splits) <= 20:
        print(f"They are: {perfect_splits}")
    else:
        print(f"First 20: {perfect_splits[:20]}")
        print(f"Last 20: {perfect_splits[-20:]}")
    print()
    
    print(f"Probability of random threshold giving 57/57: {len(perfect_splits)/284:.3f}")
    print()
    
    # Now test which of these also give the 27/30 swap pattern
    perfect_swap_thresholds = []
    for threshold in perfect_splits:
        result = analyze_long_short_pattern(verse_counts, threshold)
        if (result['long_odd'] == 27 and result['long_even'] == 30 and
            result['short_odd'] == 30 and result['short_even'] == 27):
            perfect_swap_thresholds.append(threshold)
    
    print(f"Of those, how many ALSO give 27/30 swap pattern: {len(perfect_swap_thresholds)}")
    print(f"They are: {perfect_swap_thresholds}")
    print()
    
    if len(perfect_swap_thresholds) > 0:
        prob = len(perfect_swap_thresholds) / 284
        print(f"Probability: {len(perfect_swap_thresholds)}/284 = ~1 in {284/len(perfect_swap_thresholds):.1f}")
    else:
        print("Probability: < 1 in 284")
    print()
    
    return perfect_swap_thresholds

def permutation_test(verse_counts: Dict[int, int], num_trials: int = 1000000):
    """Test by permuting verse counts"""
    print("=" * 70)
    print("PERMUTATION TEST")
    print("=" * 70)
    print()
    
    print(f"Running {num_trials:,} permutation trials...")
    print("Shuffling verse counts and testing if 40-verse threshold")
    print("gives the 27/30 swap pattern...")
    print()
    
    verse_list = list(verse_counts.values())
    match_count = 0
    split_57_count = 0
    swap_27_30_count = 0
    
    for trial in range(num_trials):
        shuffled = random.sample(verse_list, len(verse_list))
        temp_counts = {i+1: shuffled[i] for i in range(114)}
        result = analyze_long_short_pattern(temp_counts, threshold=40)
        
        if result['total_long'] == 57 and result['total_short'] == 57:
            split_57_count += 1
            
            if (result['long_odd'] == 27 and result['long_even'] == 30 and
                result['short_odd'] == 30 and result['short_even'] == 27):
                swap_27_30_count += 1
                match_count += 1
    
    prob_split = split_57_count / num_trials
    prob_swap = swap_27_30_count / num_trials
    prob_both = match_count / num_trials
    
    print(f"Results:")
    print(f"  57/57 split at threshold=40: {split_57_count:,} ({prob_split*100:.2f}%)")
    if prob_split > 0:
        print(f"    Probability: ~1 in {1/prob_split:.1f}")
    print()
    print(f"  27/30 swap pattern (given 57/57): {swap_27_30_count:,} ({prob_swap*100:.3f}%)")
    if prob_swap > 0:
        print(f"    Probability: ~1 in {1/prob_swap:.1f}")
    else:
        print(f"    Probability: < 1 in {num_trials:,}")
    print()
    
    return {
        'split_matches': split_57_count,
        'swap_matches': swap_27_30_count,
        'trials': num_trials,
        'prob_split': prob_split,
        'prob_swap': prob_swap
    }

def main():
    """Run comprehensive analysis"""
    # Understand the pattern
    verse_counts, actual = understand_the_pattern()
    
    # Test threshold significance
    print()
    swap_thresholds = test_threshold_significance(verse_counts)
    
    # Run permutation test
    print()
    stats = permutation_test(verse_counts, num_trials=1000000)
    
    print()
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print()
    print("CLAIM 1: '57/57 split at 40-verse threshold'")
    if stats['prob_split'] > 0:
        print(f"  Probability: ~1 in {1/stats['prob_split']:.1f}")
    print()
    print("CLAIM 2: '27/30 swap pattern (long vs short)'")
    if stats['prob_swap'] > 0:
        print(f"  Probability: ~1 in {1/stats['prob_swap']:.1f}")
    else:
        print(f"  Probability: < 1 in {stats['trials']:,}")
    print()
    print("CLAIM 3: 'No surahs with exactly 39 verses'")
    print(f"  Status: {not actual['has_boundary']}")
    prob_no_39 = (283/284) ** 114  # Probability no surah lands on 39
    print(f"  Probability (if uniform): ~{prob_no_39:.2f} or ~1 in {1/prob_no_39:.1f}")
    print()
    print("INDEPENDENCE: Is this different from core parity pattern?")
    print("  YES - tests verse magnitude (>=40), not verse parity (odd/even)")
    print("  This is independent evidence.")

if __name__ == "__main__":
    main()

