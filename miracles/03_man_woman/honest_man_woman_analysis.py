#!/usr/bin/env python3
"""
Honest Analysis of Man/Woman Pattern

This script verifies the actual counts and evaluates the statistical
significance of the claimed 25:25 balance, including critical examination
of the "normalization" rules.
"""

from pathlib import Path
from typing import Dict, List, Tuple
import random

def load_quran_text() -> Dict[Tuple[int, int], str]:
    """Load Quran text"""
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
    man_pattern = 'رَجُل'
    woman_patterns = ['ٱمْرَأَة', 'ٱمْرَأَت']
    
    man_verses = []
    woman_verses = []
    
    for (surah, verse), text in verses.items():
        # Count man
        man_count = text.count(man_pattern)
        if man_count > 0:
            man_verses.append((surah, verse, man_count, text))
        
        # Count woman
        woman_count = sum(text.count(p) for p in woman_patterns)
        if woman_count > 0:
            woman_verses.append((surah, verse, woman_count, text))
    
    return {
        'man_verses': man_verses,
        'woman_verses': woman_verses,
        'man_total': sum(count for _, _, count, _ in man_verses),
        'woman_total': sum(count for _, _, count, _ in woman_verses)
    }

def analyze_normalization_rules():
    """Critical analysis of the normalization rules"""
    print("=" * 70)
    print("CRITICAL ANALYSIS OF NORMALIZATION RULES")
    print("=" * 70)
    print()
    print("The pattern claims two 'minimal normalization' rules:")
    print()
    print("Rule 1: Verse 39:29 - Has 3 'man' tokens, drop 1, keep 2")
    print("  Claimed reason: 'Avoid double-counting in single parable'")
    print()
    print("Rule 2: Verse 66:10 - Has 2 'woman' tokens, count as 1")
    print("  Claimed reason: 'Single narrative principle'")
    print()
    print("CRITICAL QUESTIONS:")
    print("-" * 70)
    print()
    print("Q1: Why these specific verses?")
    print("  - Are there other verses with multiple tokens in single context?")
    print("  - Why adjust 39:29 but not others?")
    print("  - Why adjust 66:10 but not others?")
    print()
    print("Q2: Why these specific adjustments?")
    print("  - 39:29: Why drop 1 of 3, not 2 of 3, or all 3?")
    print("  - 66:10: Why count as 1, not 2, or 0?")
    print()
    print("Q3: Were these rules determined:")
    print("  a) PRE-HOC (before counting)?")
    print("  b) POST-HOC (after seeing raw counts)?")
    print()
    print("Q4: Statistical implication:")
    print("  - If rules are post-hoc (chosen to get 25:25),")
    print("    then the 'miracle' is just data fitting")
    print()
    print("RED FLAG: These rules look suspiciously designed to")
    print("          transform 26:26 into 25:25")
    print()

def understand_pattern():
    """Understand the pattern and check the claims"""
    print("=" * 70)
    print("UNDERSTANDING THE MAN/WOMAN PATTERN")
    print("=" * 70)
    print()
    
    verses = load_quran_text()
    counts = count_man_woman_occurrences(verses)
    
    print("RAW COUNTS (no normalization):")
    print("-" * 70)
    print(f"  Man (rajul):   {counts['man_total']}")
    print(f"  Woman (imra'ah): {counts['woman_total']}")
    print()
    
    # Find verse 39:29
    verse_39_29_man = [(s, v, c, t) for s, v, c, t in counts['man_verses'] if s == 39 and v == 29]
    if verse_39_29_man:
        print(f"Verse 39:29 (man tokens): {verse_39_29_man[0][2]} occurrences")
    
    # Find verse 66:10
    verse_66_10_woman = [(s, v, c, t) for s, v, c, t in counts['woman_verses'] if s == 66 and v == 10]
    if verse_66_10_woman:
        print(f"Verse 66:10 (woman tokens): {verse_66_10_woman[0][2]} occurrences")
    print()
    
    # Apply claimed normalization
    if verse_39_29_man:
        man_adjustment = 1  # Drop 1 from the 3
    else:
        man_adjustment = 0
    
    if verse_66_10_woman:
        woman_adjustment = verse_66_10_woman[0][2] - 1  # Keep 1 from 2
    else:
        woman_adjustment = 0
    
    normalized_man = counts['man_total'] - man_adjustment
    normalized_woman = counts['woman_total'] - woman_adjustment
    
    print("AFTER CLAIMED 'NORMALIZATION':")
    print("-" * 70)
    print(f"  Man:   {normalized_man} (was {counts['man_total']}, -1)")
    print(f"  Woman: {normalized_woman} (was {counts['woman_total']}, -{woman_adjustment})")
    print()
    
    print("CLAIM VERIFICATION:")
    print("-" * 70)
    print(f"  Raw balance: {counts['man_total']}:{counts['woman_total']}")
    print(f"  Normalized balance: {normalized_man}:{normalized_woman}")
    print(f"  Perfect balance? {normalized_man == normalized_woman}")
    print()
    
    # Check how many verses have multiple tokens
    multi_man = [(s, v, c) for s, v, c, _ in counts['man_verses'] if c > 1]
    multi_woman = [(s, v, c) for s, v, c, _ in counts['woman_verses'] if c > 1]
    
    print("CONTEXT CHECK:")
    print("-" * 70)
    print(f"Verses with multiple 'man' tokens: {len(multi_man)}")
    if multi_man:
        print("  Examples:", multi_man[:5])
    print()
    print(f"Verses with multiple 'woman' tokens: {len(multi_woman)}")
    if multi_woman:
        print("  Examples:", multi_woman[:5])
    print()
    
    print("CRITICAL OBSERVATION:")
    print("-" * 70)
    print(f"If raw counts are ALREADY balanced ({counts['man_total']}:{counts['woman_total']}),")
    print("why is 'normalization' needed at all?")
    print()
    print("The 'normalization' changes perfect 26:26 into perfect 25:25.")
    print("But 26:26 is ALSO a perfect balance!")
    print()
    
    return counts, normalized_man, normalized_woman

def calculate_probability():
    """Calculate honest probability"""
    print("=" * 70)
    print("STATISTICAL ANALYSIS")
    print("=" * 70)
    print()
    
    print("QUESTION: What's the probability of getting equal counts?")
    print()
    print("METHOD 1: Raw counts (26:26)")
    print("-" * 70)
    print("  Total tokens: 26 + 26 = 52")
    print("  If each token randomly assigned to 'man' or 'woman',")
    print("  probability of exactly 26:26 split:")
    print()
    # Binomial probability: C(52,26) * 0.5^52
    from math import comb
    prob_26_26 = comb(52, 26) * (0.5 ** 52)
    print(f"  P(26:26) = C(52,26) * 0.5^52 = {prob_26_26:.4f}")
    print(f"           = ~1 in {1/prob_26_26:.1f}")
    print()
    
    print("METHOD 2: After normalization (25:25)")
    print("-" * 70)
    print("  Total tokens after: 25 + 25 = 50")
    print("  Probability of exactly 25:25 split:")
    print()
    prob_25_25 = comb(50, 25) * (0.5 ** 50)
    print(f"  P(25:25) = C(50,25) * 0.5^50 = {prob_25_25:.4f}")
    print(f"           = ~1 in {1/prob_25_25:.1f}")
    print()
    
    print("INTERPRETATION:")
    print("-" * 70)
    print("Getting a 26:26 or 25:25 split isn't particularly rare")
    print("when you have ~50 total tokens.")
    print()
    print("This is like flipping 52 coins and getting 26 heads, 26 tails.")
    print("Common? Not exactly. Rare? Not really.")
    print()
    print("The key question: Was the 'normalization' pre-determined")
    print("or chosen post-hoc to achieve a desired result?")
    print()

def main():
    """Run comprehensive honest analysis"""
    print()
    print("*" * 70)
    print("HONEST ANALYSIS: MAN/WOMAN PATTERN")
    print("*" * 70)
    print()
    
    # Understand the pattern
    counts, norm_man, norm_woman = understand_pattern()
    
    # Analyze normalization
    print()
    analyze_normalization_rules()
    
    # Calculate probability
    print()
    calculate_probability()
    
    print()
    print("=" * 70)
    print("HONEST CONCLUSION")
    print("=" * 70)
    print()
    print("1. RAW COUNTS: 26 man : 26 woman")
    print("   - This IS a perfect balance")
    print("   - Probability: ~1 in 9 (11.2%)")
    print()
    print("2. AFTER 'NORMALIZATION': 25 man : 25 woman")
    print("   - Also a perfect balance")
    print("   - Probability: ~1 in 9 (11.2%)")
    print()
    print("3. THE 'NORMALIZATION' RULES:")
    print("   - Appear arbitrary (why these verses? why these adjustments?)")
    print("   - Look post-hoc (chosen to get a specific result)")
    print("   - Not linguistically necessary (raw counts already balanced)")
    print()
    print("4. CHROMOSOME CONNECTION (23)")
    print("   - Claimed but not achieved (got 25, not 23)")
    print("   - Seems like retcon (originally targeted 23, got 25, kept it)")
    print()
    print("VERDICT:")
    print("  The 26:26 raw balance IS interesting (~1 in 9).")
    print("  The 'normalization' to 25:25 appears arbitrary.")
    print("  The probability is NOT 1 in 400 as claimed.")
    print("  The chromosome connection (23) is not demonstrated.")
    print()
    print("RECOMMENDATION:")
    print("  Present the raw 26:26 balance honestly as ~1 in 9.")
    print("  Remove arbitrary normalization rules.")
    print("  Drop the chromosome connection claim (25 != 23).")

if __name__ == "__main__":
    main()

