#!/usr/bin/env python3
"""
Honest Probability Analysis for Core 2x2 Parity Pattern

This script calculates the probability of the 27/30/30/27 pattern
using proper statistical methods that can withstand academic scrutiny.

Key principles:
1. Use appropriate probability distribution (hypergeometric)
2. Calculate expected values BEFORE comparing to observed
3. Account for constraints (114 surahs total, 57 odd/57 even fixed)
4. Provide honest interpretation
"""

from pathlib import Path
from math import comb
from typing import Dict, Tuple

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

def analyze_parity_pattern() -> Dict:
    """Analyze the actual parity pattern in the Quran"""
    verse_counts = load_verse_counts()
    
    # Count the four groups
    odd_odd = sum(1 for s in range(1, 115) 
                  if s % 2 == 1 and verse_counts[s] % 2 == 1)
    even_even = sum(1 for s in range(1, 115) 
                    if s % 2 == 0 and verse_counts[s] % 2 == 0)
    odd_even = sum(1 for s in range(1, 115) 
                   if s % 2 == 1 and verse_counts[s] % 2 == 0)
    even_odd = sum(1 for s in range(1, 115) 
                   if s % 2 == 0 and verse_counts[s] % 2 == 1)
    
    # Total odd and even verse counts
    total_odd_verses = odd_odd + even_odd
    total_even_verses = even_even + odd_even
    
    return {
        'odd_odd': odd_odd,
        'even_even': even_even,
        'odd_even': odd_even,
        'even_odd': even_odd,
        'total_odd_verses': total_odd_verses,
        'total_even_verses': total_even_verses
    }

def calculate_hypergeometric_probability(K: int, N: int, n: int, k: int) -> float:
    """
    Calculate hypergeometric probability P(X = k)
    
    Parameters:
    K: Number of success states in population
    N: Total population size
    n: Number of draws (sample size)
    k: Number of observed successes in sample
    
    Returns:
    Probability of getting exactly k successes
    """
    try:
        return (comb(K, k) * comb(N - K, n - k)) / comb(N, n)
    except (ValueError, ZeroDivisionError):
        return 0.0

def statistical_analysis() -> Dict:
    """
    Perform honest statistical analysis of the parity pattern.
    
    This uses the hypergeometric distribution, which is the correct
    model when sampling without replacement from a finite population.
    """
    pattern = analyze_parity_pattern()
    
    # Fixed constraints
    N = 114  # Total surahs
    n_odd_numbered = 57  # Odd-numbered positions (1, 3, 5, ...)
    n_even_numbered = 57  # Even-numbered positions (2, 4, 6, ...)
    K_odd_verses = pattern['total_odd_verses']  # Surahs with odd verse counts
    K_even_verses = pattern['total_even_verses']  # Surahs with even verse counts
    
    # Expected values under random distribution
    expected_odd_odd = K_odd_verses * (n_odd_numbered / N)
    expected_even_odd = K_odd_verses * (n_even_numbered / N)
    expected_odd_even = K_even_verses * (n_odd_numbered / N)
    expected_even_even = K_even_verses * (n_even_numbered / N)
    
    # Observed values
    obs_odd_odd = pattern['odd_odd']
    obs_even_odd = pattern['even_odd']
    
    # Calculate probability of observing exactly this value
    prob_odd_odd = calculate_hypergeometric_probability(
        K=K_odd_verses, N=N, n=n_odd_numbered, k=obs_odd_odd
    )
    
    # Calculate probability of deviating this much or more from expected
    # This gives a two-tailed p-value
    deviation = abs(obs_odd_odd - expected_odd_odd)
    p_value = 0.0
    for k in range(0, K_odd_verses + 1):
        if abs(k - expected_odd_odd) >= deviation:
            p_value += calculate_hypergeometric_probability(
                K=K_odd_verses, N=N, n=n_odd_numbered, k=k
            )
    
    return {
        'observed': {
            'odd_odd': obs_odd_odd,
            'even_even': pattern['even_even'],
            'odd_even': pattern['odd_even'],
            'even_odd': obs_even_odd
        },
        'expected': {
            'odd_odd': expected_odd_odd,
            'even_even': expected_even_even,
            'odd_even': expected_odd_even,
            'even_odd': expected_even_odd
        },
        'deviations': {
            'odd_odd': obs_odd_odd - expected_odd_odd,
            'even_even': pattern['even_even'] - expected_even_even,
            'odd_even': pattern['odd_even'] - expected_odd_even,
            'even_odd': obs_even_odd - expected_even_odd
        },
        'probability_exact': prob_odd_odd,
        'p_value_two_tailed': p_value,
        'one_in': 1 / prob_odd_odd if prob_odd_odd > 0 else float('inf')
    }

def main():
    """Run the honest statistical analysis and report results"""
    print("=" * 70)
    print("HONEST PROBABILITY ANALYSIS: Core 2×2 Parity Pattern")
    print("=" * 70)
    print()
    
    pattern = analyze_parity_pattern()
    stats = statistical_analysis()
    
    print("OBSERVED PATTERN:")
    print("-" * 70)
    print(f"Odd-Odd:    {pattern['odd_odd']:2d} surahs")
    print(f"Even-Even:  {pattern['even_even']:2d} surahs")
    print(f"Odd-Even:   {pattern['odd_even']:2d} surahs")
    print(f"Even-Odd:   {pattern['even_odd']:2d} surahs")
    print()
    print(f"Total with odd verses:  {pattern['total_odd_verses']:2d}")
    print(f"Total with even verses: {pattern['total_even_verses']:2d}")
    print()
    
    print("STATISTICAL ANALYSIS:")
    print("-" * 70)
    print("Using hypergeometric distribution (correct model for finite population)")
    print()
    print("Expected values under random distribution:")
    print(f"  Odd-Odd:    {stats['expected']['odd_odd']:.1f}")
    print(f"  Even-Even:  {stats['expected']['even_even']:.1f}")
    print(f"  Odd-Even:   {stats['expected']['odd_even']:.1f}")
    print(f"  Even-Odd:   {stats['expected']['even_odd']:.1f}")
    print()
    
    print("Deviations (Observed - Expected):")
    print(f"  Odd-Odd:    {stats['deviations']['odd_odd']:+.1f}")
    print(f"  Even-Even:  {stats['deviations']['even_even']:+.1f}")
    print(f"  Odd-Even:   {stats['deviations']['odd_even']:+.1f}")
    print(f"  Even-Odd:   {stats['deviations']['even_odd']:+.1f}")
    print()
    
    print("PROBABILITY CALCULATIONS:")
    print("-" * 70)
    print(f"P(exactly {stats['observed']['odd_odd']} odd-verse in odd-numbered) = {stats['probability_exact']:.6f}")
    print(f"That's approximately 1 in {stats['one_in']:.1f}")
    print()
    print(f"Two-tailed p-value: {stats['p_value_two_tailed']:.4f}")
    print(f"(Probability of deviation this large or larger from expected)")
    print()
    
    print("HONEST INTERPRETATION:")
    print("-" * 70)
    
    if stats['p_value_two_tailed'] > 0.05:
        print("Result: NOT statistically significant (p > 0.05)")
        print()
        print("The observed pattern is consistent with random chance.")
        print("The deviation from expected value is very small.")
        print()
        print("CONCLUSION: This pattern alone does not demonstrate")
        print("statistical significance or indicate design beyond chance.")
    else:
        print(f"Result: Statistically significant (p = {stats['p_value_two_tailed']:.4f})")
        print()
        print("The observed pattern deviates significantly from random expectation.")
        print()
        print("CONCLUSION: This pattern shows statistically significant")
        print("deviation from what random chance would predict.")
    
    print()
    print("=" * 70)
    print("METHODOLOGY NOTES:")
    print("=" * 70)
    print()
    print("1. Uses hypergeometric distribution (correct for finite population)")
    print("2. Calculates expected values BEFORE comparison")
    print("3. Reports two-tailed p-value (proper hypothesis testing)")
    print("4. Acknowledges constraints (114 surahs, 57 odd/57 even fixed)")
    print("5. Provides honest interpretation based on standard significance levels")
    print()
    print("This analysis can withstand academic scrutiny.")

if __name__ == "__main__":
    main()

