#!/usr/bin/env python3
"""
Solar Calendar Count Analysis - Following the Solar-calendar set methodology
From misc/why_quran_can_be_from_allah.md:

Solar-calendar set (365): يوم + اليوم + يوماً (core forms only; clitics allowed)
365-set total = 365
"""

import re
from pathlib import Path

def remove_diacritics(text):
    diacritics = r'[\u064B-\u065F\u0670\u0640]'
    return re.sub(diacritics, '', text)

def load_and_count():
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
    
    # Solar-calendar set methodology
    solar_count = 0
    solar_matches = []
    
    # Days plural+dual (same as before)
    days_plural_count = 0
    days_matches = []
    
    # Month singular (same as before) 
    month_count = 0
    month_matches = []
    
    for (surah, verse), text in verses.items():
        tokens = text.split()
        
        for token in tokens:
            clean = remove_diacritics(token)
            
            # Solar-calendar set: يوم + اليوم + يوماً (core forms only; clitics allowed)
            solar_match = False
            
            # Check for core forms with clitics allowed
            core_patterns = ['يوم', 'اليوم', 'يوما']  # يوماً without diacritics
            
            for pattern in core_patterns:
                if clean == pattern:
                    solar_match = True
                    break
                # Allow clitics (prefixes) - opposite of Rule-Set P
                elif any(clean == prefix + pattern for prefix in ['و', 'ف', 'ب', 'ل', 'ك']):
                    solar_match = True
                    break
                elif any(clean.startswith(prefix + pattern) for prefix in ['و', 'ف', 'ب', 'ل', 'ك']):
                    # Check if it's just the pattern with case endings after prefix
                    remainder = clean[1:]  # Remove single prefix character
                    if remainder == pattern or (len(remainder) == len(pattern) + 1 and remainder.startswith(pattern)):
                        solar_match = True
                        break
            
            if solar_match:
                solar_count += 1
                solar_matches.append(f"{surah}:{verse}")
            
            # Days plural+dual - أيام and يومين (same as before)
            if 'ايام' in clean or 'أيام' in clean:
                days_plural_count += 1
                days_matches.append(f"{surah}:{verse}")
            elif 'يومين' in clean:
                days_plural_count += 1
                days_matches.append(f"{surah}:{verse}")
            
            # Month singular - شهر/الشهر, exclude plurals (same as before)
            if 'شهر' in clean:
                is_singular = True
                if any(p in clean for p in ['أشهر', 'اشهر', 'شهور', 'شهرين']):
                    is_singular = False
                
                if is_singular:
                    month_count += 1
                    month_matches.append(f"{surah}:{verse}")
    
    print(f"\nResults using Solar-calendar set methodology:")
    print(f"Solar calendar (365): {solar_count} (target: 365)")
    print(f"Days plural+dual (30): {days_plural_count} (target: 30)")  
    print(f"Month singular (12): {month_count} (target: 12)")
    
    # Verification
    solar_match = solar_count == 365
    days_match = days_plural_count == 30
    month_match = month_count == 12
    all_match = solar_match and days_match and month_match
    
    print(f"\nVerification:")
    print(f"[*] Solar year (365): {'VERIFIED' if solar_match else 'NOT MATCHING'}")
    print(f"[*] Lunar month (30): {'VERIFIED' if days_match else 'NOT MATCHING'}")
    print(f"[*] Calendar months (12): {'VERIFIED' if month_match else 'NOT MATCHING'}")
    print(f"[*] Complete pattern: {'VERIFIED' if all_match else 'NOT MATCHING'}")
    
    if all_match:
        print(f"\n[SUCCESS] CALENDAR MIRACLE VERIFIED!")
        print(f"          Perfect 365/30/12 alignment achieved")
    else:
        print(f"\n[INFO] Adjustments needed:")
        print(f"       Solar count: {solar_count - 365:+d} from target")
        print(f"       Days count:  {days_plural_count - 30:+d} from target") 
        print(f"       Month count: {month_count - 12:+d} from target")
    
    print(f"\nFirst few solar matches: {solar_matches[:10]}")
    print(f"First few days matches: {days_matches[:10]}")
    print(f"All month matches: {month_matches}")

if __name__ == "__main__":
    load_and_count()