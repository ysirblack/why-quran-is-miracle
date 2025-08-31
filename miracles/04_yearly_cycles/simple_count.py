#!/usr/bin/env python3
"""
Simple count analysis to verify Rule-Set P implementation
"""

import re
from pathlib import Path

def remove_diacritics(text):
    diacritics = r'[\u064B-\u065F\u0670\u0640]'
    return re.sub(diacritics, '', text)

def load_and_analyze():
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
    
    # Simple counting according to Rule-Set P
    day_singular_count = 0
    days_plural_count = 0
    month_singular_count = 0
    
    day_matches = []
    days_matches = []
    month_matches = []
    
    for (surah, verse), text in verses.items():
        tokens = text.split()
        
        for token in tokens:
            clean = remove_diacritics(token)
            
            # Rule 1: Day singular - bare يوم/اليوم, exclude يومئذ, exclude clitic prefixes
            if ('يوم' in clean) and ('يومئذ' not in clean):
                # Check if it's a bare form (not prefixed)
                is_bare = False
                
                # Check for exact matches and case endings
                if clean in ['يوم', 'اليوم']:
                    is_bare = True
                elif clean in ['يوما', 'اليوما', 'يومة', 'اليومة', 'يومي', 'اليومي', 'يومو', 'اليومو', 'يومن', 'اليومن']:
                    is_bare = True
                
                # Exclude clitic prefixes
                if any(clean.startswith(p + 'يوم') or clean.startswith(p + 'اليوم') for p in ['و', 'ف', 'ب', 'ل', 'ك']):
                    is_bare = False
                
                # Exclude pronominal suffixes (simple check)
                if any(clean.endswith(s) for s in ['ه', 'ها', 'هم', 'هن', 'ني', 'ك', 'كم', 'كن']):
                    is_bare = False
                
                if is_bare and 'ايام' not in clean and 'يومين' not in clean:
                    day_singular_count += 1
                    day_matches.append(f"{surah}:{verse}")
            
            # Rule 2: Days plural+dual - أيام and يومين
            if 'ايام' in clean or 'أيام' in clean:
                days_plural_count += 1
                days_matches.append(f"{surah}:{verse}")
            elif 'يومين' in clean:
                days_plural_count += 1
                days_matches.append(f"{surah}:{verse}")
            
            # Rule 3: Month singular - شهر/الشهر, exclude plurals
            if 'شهر' in clean:
                is_singular = True
                
                # Exclude plurals/dual
                if any(p in clean for p in ['أشهر', 'اشهر', 'شهور', 'شهرين']):
                    is_singular = False
                
                if is_singular:
                    month_singular_count += 1
                    month_matches.append(f"{surah}:{verse}")
    
    print(f"\nResults according to Rule-Set P:")
    print(f"Day (singular): {day_singular_count} (target: 365)")
    print(f"Days (plural+dual): {days_plural_count} (target: 30)")  
    print(f"Month (singular): {month_singular_count} (target: 12)")
    
    print(f"\nFirst few day singular matches: {day_matches[:10]}")
    print(f"First few days plural matches: {days_matches[:10]}")
    print(f"All month singular matches: {month_matches}")

if __name__ == "__main__":
    load_and_analyze()