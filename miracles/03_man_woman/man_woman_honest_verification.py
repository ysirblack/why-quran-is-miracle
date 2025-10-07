#!/usr/bin/env python3
"""
Honest Man & Woman Count Verification

This script counts singular forms of "man" (rajul) and "woman" (imra'ah)
in the Quran without arbitrary adjustments.

Counts all occurrences as they appear in the text.
"""

from pathlib import Path
from typing import Dict, List, Tuple
from math import comb

def load_quran_text() -> Dict[Tuple[int, int], str]:
    """Load Quran text from Tanzil format"""
    current_dir = Path(__file__).parent
    for _ in range(6):
        potential_path = current_dir / "data" / "quran-uthmani.txt"
        if potential_path.exists():
            data_path = potential_path
            break
        current_dir = current_dir.parent
    else:
        raise FileNotFoundError("Could not find data/quran-uthmani.txt")
    
    verses = {}
    with data_path.open('r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#') or '|' not in line:
                continue
            parts = line.split('|', 2)
            if len(parts) < 3:
                continue
            surah, verse, text = int(parts[0]), int(parts[1]), parts[2]
            verses[(surah, verse)] = text
    
    return verses

def count_man_woman_occurrences(verses: Dict[Tuple[int, int], str]) -> Dict:
    """Count man and woman occurrences"""
    # Patterns to search for
    man_pattern = 'رَجُل'  # rajul (man)
    woman_patterns = ['ٱمْرَأَة', 'ٱمْرَأَت']  # imra'ah (woman)
    
    man_occurrences = []
    woman_occurrences = []
    
    for (surah, verse), text in sorted(verses.items()):
        # Count man occurrences
        man_count = text.count(man_pattern)
        if man_count > 0:
            man_occurrences.append({
                'surah': surah,
                'verse': verse,
                'count': man_count,
                'text': text
            })
        
        # Count woman occurrences
        woman_count = sum(text.count(p) for p in woman_patterns)
        if woman_count > 0:
            woman_occurrences.append({
                'surah': surah,
                'verse': verse,
                'count': woman_count,
                'text': text
            })
    
    man_total = sum(occ['count'] for occ in man_occurrences)
    woman_total = sum(occ['count'] for occ in woman_occurrences)
    
    return {
        'man_occurrences': man_occurrences,
        'woman_occurrences': woman_occurrences,
        'man_total': man_total,
        'woman_total': woman_total
    }

def calculate_probability(man_count: int, woman_count: int) -> Dict:
    """Calculate probability of getting equal counts"""
    total = man_count + woman_count
    
    if man_count != woman_count:
        # Not balanced
        return {
            'balanced': False,
            'probability': None,
            'one_in': None
        }
    
    # Probability of getting exactly n:n split from 2n tokens
    # Using binomial: C(2n, n) * 0.5^(2n)
    prob = comb(total, man_count) * (0.5 ** total)
    
    return {
        'balanced': True,
        'probability': prob,
        'one_in': 1 / prob if prob > 0 else float('inf')
    }

def main():
    """Run honest verification"""
    print("=" * 70)
    print("HONEST MAN & WOMAN COUNT VERIFICATION")
    print("=" * 70)
    print()
    print("Counting singular forms:")
    print("  Man: rajul (singular masculine)")
    print("  Woman: imra'ah (singular feminine)")
    print()
    print("Data source: Tanzil Hafs/Uthmani")
    print("Method: Count all occurrences as they appear (no adjustments)")
    print()
    
    # Load and count
    verses = load_quran_text()
    counts = count_man_woman_occurrences(verses)
    
    print("=" * 70)
    print("RESULTS")
    print("=" * 70)
    print()
    print(f"Total Man (rajul) occurrences:   {counts['man_total']}")
    print(f"Total Woman (imra'ah) occurrences: {counts['woman_total']}")
    print()
    print(f"Found in {len(counts['man_occurrences'])} verses (man)")
    print(f"Found in {len(counts['woman_occurrences'])} verses (woman)")
    print()
    
    # Check balance
    balanced = counts['man_total'] == counts['woman_total']
    print(f"Perfect balance: {balanced}")
    print()
    
    # Calculate probability
    prob_result = calculate_probability(counts['man_total'], counts['woman_total'])
    
    print("=" * 70)
    print("STATISTICAL ANALYSIS")
    print("=" * 70)
    print()
    
    if prob_result['balanced']:
        print(f"The counts are perfectly balanced: {counts['man_total']}:{counts['woman_total']}")
        print()
        print(f"Probability of this balance:")
        print(f"  P = {prob_result['probability']:.4f}")
        print(f"    = ~1 in {prob_result['one_in']:.1f}")
        print(f"    = ~{prob_result['probability']*100:.2f}%")
        print()
        print("Interpretation:")
        print(f"  Getting a {counts['man_total']}:{counts['woman_total']} split is like")
        print(f"  flipping {counts['man_total'] + counts['woman_total']} coins and getting exactly")
        print(f"  {counts['man_total']} heads and {counts['woman_total']} tails.")
        print()
        print("  This is moderately interesting but not extremely rare.")
    else:
        print(f"The counts are NOT balanced: {counts['man_total']}:{counts['woman_total']}")
        print(f"Difference: {abs(counts['man_total'] - counts['woman_total'])}")
    
    print()
    print("=" * 70)
    print("VERSES WITH MULTIPLE OCCURRENCES")
    print("=" * 70)
    print()
    
    # Show verses with multiple man occurrences
    multi_man = [occ for occ in counts['man_occurrences'] if occ['count'] > 1]
    print(f"Verses with multiple 'man' tokens: {len(multi_man)}")
    for occ in multi_man:
        print(f"  {occ['surah']}:{occ['verse']} - {occ['count']} occurrences")
    print()
    
    # Show verses with multiple woman occurrences
    multi_woman = [occ for occ in counts['woman_occurrences'] if occ['count'] > 1]
    print(f"Verses with multiple 'woman' tokens: {len(multi_woman)}")
    for occ in multi_woman:
        print(f"  {occ['surah']}:{occ['verse']} - {occ['count']} occurrences")
    print()
    
    print("=" * 70)
    print("FIRST 10 MAN OCCURRENCES")
    print("=" * 70)
    for i, occ in enumerate(counts['man_occurrences'][:10], 1):
        print(f"{i:2d}. Surah {occ['surah']:3d}, Verse {occ['verse']:3d} ({occ['count']} times)")
    print()
    
    print("=" * 70)
    print("FIRST 10 WOMAN OCCURRENCES")
    print("=" * 70)
    for i, occ in enumerate(counts['woman_occurrences'][:10], 1):
        print(f"{i:2d}. Surah {occ['surah']:3d}, Verse {occ['verse']:3d} ({occ['count']} times)")
    print()
    
    print("=" * 70)
    print("HONEST CONCLUSION")
    print("=" * 70)
    print()
    if balanced:
        print(f"The Quran contains {counts['man_total']} occurrences of 'man' (rajul)")
        print(f"and {counts['woman_total']} occurrences of 'woman' (imra'ah) in singular form.")
        print()
        print(f"This perfect balance has a probability of ~1 in {prob_result['one_in']:.1f}")
        print(f"or about {prob_result['probability']*100:.2f}%.")
        print()
        print("This is a moderately interesting balance, though not extremely rare.")
    else:
        print(f"The counts are {counts['man_total']} man : {counts['woman_total']} woman")
        print("(not perfectly balanced)")
    print()
    print("All counts verified. No adjustments applied.")
    
    return counts

if __name__ == "__main__":
    main()

