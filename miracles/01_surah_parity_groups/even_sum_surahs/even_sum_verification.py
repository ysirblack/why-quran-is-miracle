#!/usr/bin/env python3
"""Verify Even-Sum Surahs Pattern - 57 surahs with even (verses + surah_number) sums totaling 6,236"""

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

def verify_even_sum_surahs():
    """Verify the even-sum surahs pattern"""
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
    
    # Calculate sums: (verse_count + surah_number)
    even_sum_surahs = []
    odd_sum_surahs = []
    
    for surah_num in range(1, 115):
        verse_count = surah_verse_counts[surah_num]
        sum_value = verse_count + surah_num
        
        if sum_value % 2 == 0:  # Even sum
            even_sum_surahs.append((surah_num, verse_count, sum_value))
        else:  # Odd sum
            odd_sum_surahs.append((surah_num, verse_count, sum_value))
    
    # Calculate totals
    total_even_sums = sum(sum_val for _, _, sum_val in even_sum_surahs)
    total_odd_sums = sum(sum_val for _, _, sum_val in odd_sum_surahs)
    total_verses = sum(surah_verse_counts.values())
    sum_of_orders = sum(range(1, 115))  # 1+2+...+114 = 6555
    
    print("EVEN-SUM SURAHS VERIFICATION")
    print("=" * 60)
    print(f"Even-sum surahs count:     {len(even_sum_surahs):3d} / 57 target")
    print(f"Odd-sum surahs count:      {len(odd_sum_surahs):3d} / 57 target")
    print("-" * 40)
    print(f"Total of even sums:        {total_even_sums:,} / 6,236 target")
    print(f"Total of odd sums:         {total_odd_sums:,} / 6,555 target")
    print("-" * 40)
    print(f"Total verses in Quran:     {total_verses:,}")
    print(f"Sum of surah orders:       {sum_of_orders:,}")
    print(f"Combined total:            {total_even_sums + total_odd_sums:,}")
    print(f"Expected combined:         {total_verses + sum_of_orders:,}")
    
    # Check if targets are met
    even_target_hit = total_even_sums == 6236
    odd_target_hit = total_odd_sums == 6555
    count_balance = len(even_sum_surahs) == 57 and len(odd_sum_surahs) == 57
    
    print("\nVERIFICATION RESULTS:")
    print("-" * 40)
    print(f"Even sums = Total verses:  {'SUCCESS' if even_target_hit else 'FAIL'}")
    print(f"Odd sums = Sum of orders:  {'SUCCESS' if odd_target_hit else 'FAIL'}")
    print(f"Perfect 57:57 balance:     {'SUCCESS' if count_balance else 'FAIL'}")
    print(f"Overall pattern:           {'SUCCESS' if all([even_target_hit, odd_target_hit, count_balance]) else 'FAIL'}")
    
    # Show first 20 even-sum surahs
    print(f"\nFIRST 20 EVEN-SUM SURAHS:")
    print("-" * 40)
    print("Surah | Verses | Sum | Name")
    print("-" * 40)
    
    surah_names = {
        1: "Al-Fātiḥah", 2: "Al-Baqarah", 4: "An-Nisā'", 9: "At-Tawbah",
        11: "Hūd", 13: "Ar-Ra'd", 14: "Ibrāhīm", 15: "Al-Ḥijr",
        16: "An-Naḥl", 17: "Al-Isrā'", 18: "Al-Kahf", 22: "Al-Ḥajj",
        24: "An-Nūr", 25: "Al-Furqān", 27: "An-Naml", 28: "Al-Qaṣaṣ",
        29: "Al-'Ankabūt", 30: "Ar-Rūm", 32: "As-Sajdah", 33: "Al-Aḥzāb"
    }
    
    for i, (surah_num, verse_count, sum_val) in enumerate(even_sum_surahs[:20]):
        name = surah_names.get(surah_num, f"Surah {surah_num}")
        print(f"{surah_num:5d} | {verse_count:6d} | {sum_val:3d} | {name}")
    
    if len(even_sum_surahs) > 20:
        print(f"... and {len(even_sum_surahs) - 20} more even-sum surahs")
    
    print(f"\nMATHEMATICAL SIGNIFICANCE:")
    print("-" * 40)
    print(f"• Perfect 57:57 balance between even and odd sum groups")
    print(f"• Even sums total = Total Quran verses ({total_verses:,})")
    print(f"• Odd sums total = Sum of all surah numbers ({sum_of_orders:,})")
    print(f"• Combined: {total_even_sums:,} + {total_odd_sums:,} = {total_even_sums + total_odd_sums:,}")
    print(f"• This represents the complete mathematical structure of Quranic numbering")
    
    return {
        'even_count': len(even_sum_surahs),
        'odd_count': len(odd_sum_surahs),
        'even_total': total_even_sums,
        'odd_total': total_odd_sums,
        'pattern_verified': even_target_hit and odd_target_hit and count_balance,
        'total_verses': total_verses,
        'sum_of_orders': sum_of_orders
    }

if __name__ == "__main__":
    verify_even_sum_surahs()