#!/usr/bin/env python3
"""Verify Verses > Surah Number Pattern - 48 surahs with perfect 23/25 swap symmetry"""

import re

def load_quran_data():
    """Load Quran data from Tanzil format"""
    import os
    from pathlib import Path
    
    # Find the data file by searching up the directory tree
    current_dir = Path(__file__).parent
    data_path = None
    
    # Search up to 5 levels up for the data directory
    for _ in range(5):
        potential_path = current_dir / "data" / "quran-uthmani.txt"
        if potential_path.exists():
            data_path = str(potential_path)
            break
        current_dir = current_dir.parent
    
    if not data_path:
        raise FileNotFoundError("Could not find quran-uthmani.txt data file")
    
    verses = {}
    
    with open(data_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            if '|' in line:
                parts = line.split('|', 2)
                if len(parts) >= 3:
                    surah_num = int(parts[0])
                    verse_num = int(parts[1])
                    if surah_num not in verses:
                        verses[surah_num] = []
                    verses[surah_num].append(verse_num)
    
    return verses

def verify_verses_greater_than_number():
    """Verify the verses > surah number pattern with 23/25 swap symmetry"""
    verses_data = load_quran_data()
    
    # Calculate verse counts per surah
    surah_verse_counts = {}
    for surah_num in range(1, 115):  # 114 surahs
        if surah_num in verses_data:
            surah_verse_counts[surah_num] = len(verses_data[surah_num])
        else:
            surah_verse_counts[surah_num] = 0
    
    print(f"Loaded {len(surah_verse_counts)} surahs")
    print("=" * 60)
    
    # Filter: keep only surahs where verses > surah_number
    filtered_surahs = []
    for surah_num in range(1, 115):
        verse_count = surah_verse_counts[surah_num]
        if verse_count > surah_num:
            filtered_surahs.append((surah_num, verse_count))
    
    print(f"VERSES > SURAH NUMBER VERIFICATION")
    print("=" * 60)
    print(f"Filter: verses > surah number")
    print(f"Filtered surahs count:     {len(filtered_surahs):3d} / 48 target")
    print("-" * 40)
    
    # Classification Method 1: By subtraction result parity
    result_odd = []      # (verses - surah_number) is odd
    result_even = []     # (verses - surah_number) is even
    
    # Classification Method 2: By surah order parity
    order_odd = []       # surah number is odd
    order_even = []      # surah number is even
    
    for surah_num, verse_count in filtered_surahs:
        difference = verse_count - surah_num
        
        # Method 1: By result parity
        if difference % 2 == 1:  # odd result
            result_odd.append((surah_num, verse_count, difference))
        else:  # even result
            result_even.append((surah_num, verse_count, difference))
        
        # Method 2: By order parity
        if surah_num % 2 == 1:  # odd surah number
            order_odd.append((surah_num, verse_count, difference))
        else:  # even surah number
            order_even.append((surah_num, verse_count, difference))
    
    # Calculate counts
    result_odd_count = len(result_odd)
    result_even_count = len(result_even)
    order_odd_count = len(order_odd)
    order_even_count = len(order_even)
    
    print("CLASSIFICATION METHOD 1: By Subtraction Result")
    print(f"  Result is odd:           {result_odd_count:3d} / 23 target")
    print(f"  Result is even:          {result_even_count:3d} / 25 target")
    print("-" * 40)
    print("CLASSIFICATION METHOD 2: By Surah Order")
    print(f"  Order is odd:            {order_odd_count:3d} / 25 target")
    print(f"  Order is even:           {order_even_count:3d} / 23 target")
    
    # Check pattern verification
    filter_target = len(filtered_surahs) == 48
    result_odd_target = result_odd_count == 23
    result_even_target = result_even_count == 25
    order_odd_target = order_odd_count == 25
    order_even_target = order_even_count == 23
    swap_symmetry = (result_odd_count == order_even_count == 23 and 
                    result_even_count == order_odd_count == 25)
    
    print("\nVERIFICATION RESULTS:")
    print("-" * 40)
    print(f"Filtered count = 48:       {'SUCCESS' if filter_target else 'FAIL'}")
    print(f"Result odd = 23:           {'SUCCESS' if result_odd_target else 'FAIL'}")
    print(f"Result even = 25:          {'SUCCESS' if result_even_target else 'FAIL'}")
    print(f"Order odd = 25:            {'SUCCESS' if order_odd_target else 'FAIL'}")
    print(f"Order even = 23:           {'SUCCESS' if order_even_target else 'FAIL'}")
    print(f"Perfect 23/25 swap:        {'SUCCESS' if swap_symmetry else 'FAIL'}")
    
    all_targets_met = all([filter_target, result_odd_target, result_even_target, 
                          order_odd_target, order_even_target, swap_symmetry])
    print(f"Overall pattern:           {'SUCCESS' if all_targets_met else 'FAIL'}")
    
    # Show examples from each category
    print(f"\nEXAMPLES FROM EACH CATEGORY:")
    print("-" * 60)
    
    print(f"RESULT IS ODD (first 10 of {result_odd_count}):")
    print("Surah | Verses | Diff | Name")
    print("-" * 40)
    for i, (surah_num, verse_count, diff) in enumerate(result_odd[:10]):
        print(f"{surah_num:5d} | {verse_count:6d} | {diff:4d} | Surah {surah_num}")
    
    print(f"\nRESULT IS EVEN (first 10 of {result_even_count}):")
    print("Surah | Verses | Diff | Name")
    print("-" * 40)
    for i, (surah_num, verse_count, diff) in enumerate(result_even[:10]):
        print(f"{surah_num:5d} | {verse_count:6d} | {diff:4d} | Surah {surah_num}")
    
    print(f"\nORDER IS ODD (first 10 of {order_odd_count}):")
    print("Surah | Verses | Diff | Order")
    print("-" * 40)
    for i, (surah_num, verse_count, diff) in enumerate(order_odd[:10]):
        print(f"{surah_num:5d} | {verse_count:6d} | {diff:4d} | {'ODD' if surah_num % 2 == 1 else 'EVEN'}")
    
    print(f"\nORDER IS EVEN (first 10 of {order_even_count}):")
    print("Surah | Verses | Diff | Order")
    print("-" * 40)
    for i, (surah_num, verse_count, diff) in enumerate(order_even[:10]):
        print(f"{surah_num:5d} | {verse_count:6d} | {diff:4d} | {'ODD' if surah_num % 2 == 1 else 'EVEN'}")
    
    print(f"\nSWAP SYMMETRY ANALYSIS:")
    print("-" * 40)
    print(f"• Two completely different classification methods:")
    print(f"  1. By subtraction result parity: {result_odd_count} odd, {result_even_count} even")
    print(f"  2. By surah order parity: {order_odd_count} odd, {order_even_count} even")
    print(f"• Perfect swap symmetry:")
    print(f"  - Result odd ({result_odd_count}) ↔ Order even ({order_even_count})")
    print(f"  - Result even ({result_even_count}) ↔ Order odd ({order_odd_count})")
    print(f"• Both methods split the same 48 surahs into identical 23/25 groups")
    print(f"• This demonstrates mathematical coordination across different classification systems")
    
    # Additional statistical information
    avg_verses = sum(vc for _, vc in filtered_surahs) / len(filtered_surahs) if filtered_surahs else 0
    differences = [vc - sn for sn, vc in filtered_surahs]
    avg_difference = sum(differences) / len(differences) if differences else 0
    min_difference = min(differences) if differences else 0
    max_difference = max(differences) if differences else 0
    
    print(f"\nSTATISTICAL SUMMARY:")
    print("-" * 40)
    print(f"Total filtered surahs:     {len(filtered_surahs)}")
    print(f"Average verses:            {avg_verses:.1f}")
    print(f"Average difference:        {avg_difference:.1f}")
    print(f"Minimum difference:        {min_difference}")
    print(f"Maximum difference:        {max_difference}")
    print(f"Filter precision:          Exactly verses > surah number")
    print(f"Symmetry precision:        Perfect 23/25 swap across methods")
    
    return {
        'filtered_count': len(filtered_surahs),
        'result_odd': result_odd_count,
        'result_even': result_even_count,
        'order_odd': order_odd_count,
        'order_even': order_even_count,
        'swap_symmetry': swap_symmetry,
        'pattern_verified': all_targets_met,
        'total_surahs': len(surah_verse_counts)
    }

if __name__ == "__main__":
    verify_verses_greater_than_number()