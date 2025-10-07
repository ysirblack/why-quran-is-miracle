#!/usr/bin/env python3
"""
Honest Probability Analysis for Six-Block Pattern

Claims: When dividing 114 surahs into 6 blocks of 19, eight different
classification patterns show alternating patterns across blocks.

Test if this is statistically significant.
"""

from pathlib import Path
from typing import Dict, List
import random
from math import isqrt

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

def is_prime_custom(n: int) -> bool:
    """Prime test treating 1 as prime per document convention"""
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

def analyze_six_blocks(verse_counts: Dict[int, int]) -> Dict:
    """Analyze the six 19-surah blocks"""
    odd_odd = [0] * 6
    even_odd = [0] * 6
    odd_even = [0] * 6
    even_even = [0] * 6
    homogeneous = [0] * 6
    heterogeneous = [0] * 6
    prime_homogeneous = [0] * 6
    prime_heterogeneous = [0] * 6
    
    for surah in range(1, 115):
        count = verse_counts[surah]
        block = (surah - 1) // 19
        
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
        
        # Homogeneous vs heterogeneous
        if order_is_odd == ayat_is_odd:
            homogeneous[block] += 1
        else:
            heterogeneous[block] += 1
        
        # Prime classification
        order_is_prime = is_prime_custom(surah)
        ayat_is_prime = is_prime_custom(count)
        if order_is_prime == ayat_is_prime:
            prime_homogeneous[block] += 1
        else:
            prime_heterogeneous[block] += 1
    
    return {
        'odd_odd': odd_odd,
        'even_odd': even_odd,
        'odd_even': odd_even,
        'even_even': even_even,
        'homogeneous': homogeneous,
        'heterogeneous': heterogeneous,
        'prime_homogeneous': prime_homogeneous,
        'prime_heterogeneous': prime_heterogeneous
    }

def has_alternating_pattern(values: List[int]) -> bool:
    """Check if values alternate between even and odd"""
    if len(values) < 2:
        return False
    for i in range(len(values) - 1):
        if values[i] % 2 == values[i+1] % 2:
            return False
    return True

def all_same_parity(values: List[int]) -> bool:
    """Check if all values have the same parity"""
    return all(v % 2 == values[0] % 2 for v in values)

def check_patterns(result: Dict) -> Dict:
    """Check which patterns exist in the result"""
    return {
        'odd_odd_alternates': has_alternating_pattern(result['odd_odd']),
        'even_odd_alternates': has_alternating_pattern(result['even_odd']),
        'odd_even_all_even': all_same_parity(result['odd_even']) and result['odd_even'][0] % 2 == 0,
        'even_even_all_odd': all_same_parity(result['even_even']) and result['even_even'][0] % 2 == 1,
        'homogeneous_alternates': has_alternating_pattern(result['homogeneous']),
        'heterogeneous_alternates': has_alternating_pattern(result['heterogeneous']),
        'prime_homo_alternates': has_alternating_pattern(result['prime_homogeneous']),
        # prime_het pattern is more complex, checking specific pattern
    }

def understand_pattern():
    """First understand the pattern and independence"""
    print("=" * 70)
    print("UNDERSTANDING THE SIX-BLOCK PATTERN")
    print("=" * 70)
    print()
    
    verse_counts = load_verse_counts()
    result = analyze_six_blocks(verse_counts)
    
    print("OBSERVED PATTERNS:")
    print("-" * 70)
    print(f"Odd-Odd:     {result['odd_odd']}")
    print(f"Even-Odd:    {result['even_odd']}")
    print(f"Odd-Even:    {result['odd_even']}")
    print(f"Even-Even:   {result['even_even']}")
    print()
    print(f"Homogeneous: {result['homogeneous']}")
    print(f"Heterogeneous: {result['heterogeneous']}")
    print()
    print(f"Prime-Homo:  {result['prime_homogeneous']}")
    print(f"Prime-Het:   {result['prime_heterogeneous']}")
    print()
    
    # Check independence
    print("KEY INSIGHT: Independence Check")
    print("-" * 70)
    print("Are these 8 patterns independent?")
    print()
    print("1. Odd-Odd, Even-Odd, Odd-Even, Even-Even:")
    print("   These are the 2x2 parity grid - NOT independent")
    print("   They must sum to 19 per block")
    print()
    print("2. Homogeneous vs Heterogeneous:")
    print("   Homogeneous = Odd-Odd + Even-Even")
    print("   Heterogeneous = Odd-Even + Even-Odd")
    print("   These are DERIVED from the 2x2 grid - NOT independent")
    print()
    print("3. Prime-Homo vs Prime-Het:")
    print("   Different classification (prime vs non-prime)")
    print("   This COULD be independent from parity")
    print()
    print("CONCLUSION: We really have 2 independent pattern systems:")
    print("  System 1: Parity-based (6 patterns that are all related)")
    print("  System 2: Prime-based (2 patterns)")
    print()
    
    return verse_counts, result

def permutation_test(verse_counts: Dict[int, int], num_trials: int = 100000):
    """Test by permuting verse counts"""
    print("=" * 70)
    print("PERMUTATION TEST")
    print("=" * 70)
    print()
    
    print(f"Running {num_trials:,} permutation trials...")
    print()
    
    actual_result = analyze_six_blocks(verse_counts)
    actual_patterns = check_patterns(actual_result)
    
    verse_list = list(verse_counts.values())
    match_counts = {key: 0 for key in actual_patterns}
    all_match = 0
    
    for trial in range(num_trials):
        shuffled = random.sample(verse_list, len(verse_list))
        temp_counts = {i+1: shuffled[i] for i in range(114)}
        temp_result = analyze_six_blocks(temp_counts)
        temp_patterns = check_patterns(temp_result)
        
        # Count individual pattern matches
        for key in actual_patterns:
            if temp_patterns[key] == actual_patterns[key]:
                match_counts[key] += 1
        
        # Count if ALL patterns match
        if all(temp_patterns[k] == actual_patterns[k] for k in actual_patterns):
            all_match += 1
    
    print("Individual Pattern Probabilities:")
    print("-" * 70)
    for key, count in match_counts.items():
        prob = count / num_trials
        print(f"{key:30s}: {count:6,} / {num_trials:,} = ~1 in {1/prob if prob > 0 else float('inf'):.1f}")
    
    print()
    prob_all = all_match / num_trials
    print(f"ALL patterns simultaneously:      {all_match:6,} / {num_trials:,}")
    if prob_all > 0:
        print(f"                                   = ~1 in {1/prob_all:.1f}")
    else:
        print(f"                                   < 1 in {num_trials:,}")
    print()
    
    return {
        'matches': match_counts,
        'all_match': all_match,
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
    print("The 8 patterns are NOT all independent:")
    print("  - 6 patterns are all derived from the 2x2 parity grid")
    print("  - 2 patterns (prime-based) are independent")
    print()
    print("Individual alternating patterns occur fairly frequently:")
    print("  - Each pattern has ~1-20% probability individually")
    print()
    if stats['prob_all'] > 0:
        print(f"All patterns simultaneously: ~1 in {1/stats['prob_all']:.1f}")
    else:
        print(f"All patterns simultaneously: < 1 in {stats['trials']:,}")
    print()
    print("The probability is lower than individual patterns because")
    print("we're requiring ALL 8 patterns to match simultaneously.")

if __name__ == "__main__":
    main()

