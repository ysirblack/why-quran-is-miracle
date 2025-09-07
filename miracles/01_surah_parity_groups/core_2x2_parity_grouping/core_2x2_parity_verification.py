#!/usr/bin/env python3
"""Verify Core 2×2 Parity Grouping - odd-odd, even-even, odd-even, even-odd counts"""

import re
from pathlib import Path

def load_quran_data():
    """Load Quran data from Tanzil format"""
    current_dir = Path(__file__).parent
    
    # Search up to 6 levels up for the data directory
    for _ in range(6):
        potential_path = current_dir / "data" / "quran-uthmani.txt"
        if potential_path.exists():
            data_path = potential_path
            break
        current_dir = current_dir.parent
    
    if not data_path:
        raise FileNotFoundError("Could not find data/quran-uthmani.txt")
    
    verses = {}
    with data_path.open('r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            if '|' not in line:
                continue
            parts = line.split('|', 2)
            if len(parts) < 3:
                continue
            surah_num = int(parts[0])
            verse_num = int(parts[1])
            verses.setdefault(surah_num, []).append(verse_num)
    
    return verses

def verify_core_2x2_parity():
    """Verify the core 2×2 parity grouping"""
    verses_data = load_quran_data()
    
    # Calculate verse counts per surah
    verse_count_by_surah = {s: len(verses_data.get(s, [])) for s in range(1, 115)}
    
    # Initialize counters for the four groups
    odd_odd = []
    even_even = []
    odd_even = []
    even_odd = []
    
    # Classify each surah
    for surah_num in range(1, 115):
        verse_count = verse_count_by_surah[surah_num]
        
        order_is_odd = (surah_num % 2 == 1)
        ayat_is_odd = (verse_count % 2 == 1)
        
        if order_is_odd and ayat_is_odd:
            odd_odd.append((surah_num, verse_count))
        elif (not order_is_odd) and (not ayat_is_odd):
            even_even.append((surah_num, verse_count))
        elif order_is_odd and (not ayat_is_odd):
            odd_even.append((surah_num, verse_count))
        else:  # even order, odd ayat
            even_odd.append((surah_num, verse_count))
    
    # Expected counts from the research
    expected_counts = {
        'odd_odd': 27,
        'even_even': 30,
        'odd_even': 30,
        'even_odd': 27
    }
    
    actual_counts = {
        'odd_odd': len(odd_odd),
        'even_even': len(even_even),
        'odd_even': len(odd_even),
        'even_odd': len(even_odd)
    }
    
    print("CORE 2×2 PARITY GROUPING VERIFICATION")
    print("=" * 60)
    print(f"Odd–Odd:     {actual_counts['odd_odd']:2d} / {expected_counts['odd_odd']:2d} (odd order + odd verses)")
    print(f"Even–Even:   {actual_counts['even_even']:2d} / {expected_counts['even_even']:2d} (even order + even verses)")
    print(f"Odd–Even:    {actual_counts['odd_even']:2d} / {expected_counts['odd_even']:2d} (odd order + even verses)")
    print(f"Even–Odd:    {actual_counts['even_odd']:2d} / {expected_counts['even_odd']:2d} (even order + odd verses)")
    
    print("\nVERIFICATION RESULTS:")
    print("-" * 40)
    all_correct = True
    for group, expected in expected_counts.items():
        actual = actual_counts[group]
        status = "✓" if actual == expected else "✗"
        print(f"{group.replace('_', '–').title():>12}: {status} {actual:2d} / {expected:2d}")
        if actual != expected:
            all_correct = False
    
    print(f"\nOverall: {'SUCCESS' if all_correct else 'FAIL'}")
    
    # Check the key patterns
    odd_verse_total = actual_counts['odd_odd'] + actual_counts['even_odd']
    even_verse_total = actual_counts['even_even'] + actual_counts['odd_even']
    same_parity_total = actual_counts['odd_odd'] + actual_counts['even_even']
    mixed_parity_total = actual_counts['odd_even'] + actual_counts['even_odd']
    
    print(f"\nKEY PATTERNS:")
    print("-" * 40)
    print(f"Odd verse count surahs:  {odd_verse_total:2d}")
    print(f"Even verse count surahs: {even_verse_total:2d}")
    print(f"Same parity groups:      {same_parity_total:2d}")
    print(f"Mixed parity groups:     {mixed_parity_total:2d}")
    
    # Show some examples from each group
    print(f"\nEXAMPLES FROM EACH GROUP:")
    print("-" * 40)
    
    groups = [
        ("Odd–Odd", odd_odd[:5]),
        ("Even–Even", even_even[:5]),
        ("Odd–Even", odd_even[:5]),
        ("Even–Odd", even_odd[:5])
    ]
    
    for group_name, examples in groups:
        print(f"\n{group_name}:")
        for surah_num, verse_count in examples:
            print(f"  {surah_num:3d}: {verse_count:3d} verses")
        if len(examples) < len(eval(group_name.lower().replace('–', '_'))):
            remaining = len(eval(group_name.lower().replace('–', '_'))) - len(examples)
            print(f"  ... and {remaining} more")
    
    return {
        'success': all_correct,
        'counts': actual_counts,
        'groups': {
            'odd_odd': odd_odd,
            'even_even': even_even,
            'odd_even': odd_even,
            'even_odd': even_odd
        }
    }

if __name__ == "__main__":
    verify_core_2x2_parity()
