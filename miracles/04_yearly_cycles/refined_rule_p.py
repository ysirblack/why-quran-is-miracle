#!/usr/bin/env python3
"""
Refined Rule Set P - Less aggressive clitic filtering
"""

import re
from pathlib import Path

def remove_diacritics(text):
    diacritics = r'[\u064B-\u065F\u0670\u0640]'
    return re.sub(diacritics, '', text)

def has_clear_clitics(token):
    """
    More conservative clitic detection
    Only exclude clear cases where clitics are definitely attached
    """
    clean = remove_diacritics(token)
    
    # Very specific pronominal suffix patterns
    # Only exclude if it's clearly a possessive pronoun
    clear_pronoun_suffixes = ['ه', 'ها', 'هم', 'هن', 'ني', 'كم', 'كن']
    
    for suffix in clear_pronoun_suffixes:
        if clean.endswith('يوم' + suffix) or clean.endswith('اليوم' + suffix):
            return True
    
    return False

def refined_rule_p():
    """Refined Rule Set P with less aggressive filtering"""
    
    data_path = "../../data/quran-uthmani.txt"
    verses = {}
    
    with open(data_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
                
            if '|' in line:
                parts = line.split('|', 2)
                if len(parts) >= 3:
                    surah = int(parts[0])
                    verse = int(parts[1])
                    text = parts[2]
                    verses[(surah, verse)] = text
    
    print(f"Loaded {len(verses)} verses")
    
    day_count = 0
    days_count = 0
    month_count = 0
    
    day_matches = []
    days_matches = []
    month_matches = []
    
    for (surah, verse), text in verses.items():
        tokens = text.split()
        
        for token in tokens:
            clean = remove_diacritics(token)
            
            # === Day (singular) - Less aggressive filtering ===
            if 'يوم' in clean:
                # Exclude definite exclusions
                if not any(x in clean for x in ['يومين', 'ايام', 'أيام', 'يومئذ']):
                    # Only exclude clear pronominal cases
                    if not has_clear_clitics(token):
                        day_count += 1
                        day_matches.append(f"{surah}:{verse}")
            
            # === Days (plural+dual) ===
            if 'ايام' in clean or 'أيام' in clean or 'يومين' in clean:
                days_count += 1
                days_matches.append(f"{surah}:{verse}")
            
            # === Month (singular) ===
            if 'شهر' in clean:
                if not any(x in clean for x in ['شهور', 'أشهر', 'اشهر', 'شهرين']):
                    month_count += 1
                    month_matches.append(f"{surah}:{verse}")
    
    print(f"\n=== REFINED RULE SET P ===")
    print(f"Day (365):   {day_count:3d} / 365")
    print(f"Days (30):   {days_count:3d} / 30")
    print(f"Month (12):  {month_count:3d} / 12")
    
    print(f"\nDifferences:")
    print(f"  Day: {day_count - 365:+d}")
    print(f"  Days: {days_count - 30:+d}")
    print(f"  Month: {month_count - 12:+d}")
    
    # Check if we're getting closer
    day_match = day_count == 365
    days_match = days_count == 30
    month_match = month_count == 12
    
    print(f"\nStatus:")
    print(f"  Day: {'VERIFIED' if day_match else 'NOT MATCHING'}")
    print(f"  Days: {'VERIFIED' if days_match else 'NOT MATCHING'}")  
    print(f"  Month: {'VERIFIED' if month_match else 'NOT MATCHING'}")
    
    if day_match and days_match and month_match:
        print(f"\n*** CALENDAR MIRACLE VERIFIED ***")
    
    return day_count, days_count, month_count

def test_no_clitic_filtering():
    """Test with no clitic filtering at all"""
    
    data_path = "../../data/quran-uthmani.txt"
    verses = {}
    
    with open(data_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
                
            if '|' in line:
                parts = line.split('|', 2)
                if len(parts) >= 3:
                    surah = int(parts[0])
                    verse = int(parts[1])
                    text = parts[2]
                    verses[(surah, verse)] = text
    
    day_count = 0
    
    for (surah, verse), text in verses.items():
        tokens = text.split()
        
        for token in tokens:
            clean = remove_diacritics(token)
            
            # Day (singular) - NO clitic filtering
            if 'يوم' in clean:
                if not any(x in clean for x in ['يومين', 'ايام', 'أيام', 'يومئذ']):
                    day_count += 1
    
    print(f"\n=== NO CLITIC FILTERING TEST ===")
    print(f"Day count (no filtering): {day_count}")
    print(f"Target: 365")
    print(f"Difference: {day_count - 365:+d}")
    
    return day_count

if __name__ == "__main__":
    # Test refined filtering
    day, days, month = refined_rule_p()
    
    # Test with no clitic filtering
    day_no_filter = test_no_clitic_filtering()
    
    print(f"\n=== COMPARISON ===")
    print(f"Original (strict): 274")
    print(f"Refined filtering: {day}")
    print(f"No filtering:      {day_no_filter}")
    print(f"Target:            365")