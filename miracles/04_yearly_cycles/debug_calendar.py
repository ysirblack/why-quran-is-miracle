#!/usr/bin/env python3
"""
Debug version to see exactly what words are being counted/excluded
"""

import re
from pathlib import Path

def remove_diacritics(text):
    diacritics = r'[\u064B-\u065F\u0670\u0640]'
    return re.sub(diacritics, '', text)

def load_quran():
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
    return verses

def analyze_day_words():
    """Analyze all words containing يوم to see what we should count"""
    verses = load_quran()
    yawm_words = []
    
    for (surah, verse), text in verses.items():
        tokens = text.split()
        for token in tokens:
            clean = remove_diacritics(token)
            if 'يوم' in clean:
                yawm_words.append({
                    'reference': f"{surah}:{verse}",
                    'original': token,
                    'clean': clean,
                    'should_count': None  # We'll determine this
                })
    
    print(f"\nFound {len(yawm_words)} words containing يوم")
    
    # Analyze each word according to Rule-Set P
    day_singular = 0
    days_plural = 0
    excluded = 0
    
    print("\nAnalyzing each word:")
    for i, word in enumerate(yawm_words):
        ref = word['reference']
        orig = word['original']
        clean = word['clean']
        
        # Rule-Set P analysis
        reason = ""
        category = ""
        
        # Check for يومئذ exclusion
        if 'يومئذ' in clean:
            category = "EXCLUDED"
            reason = "compound يومئذ"
            excluded += 1
        
        # Check for clitic prefixes و/ف/ب/ل/ك
        elif any(clean.startswith(p) for p in ['و', 'ف', 'ب', 'ل', 'ك']):
            # Check what remains after prefix
            for prefix in ['و', 'ف', 'ب', 'ل', 'ك']:
                if clean.startswith(prefix):
                    remainder = clean[len(prefix):]
                    if remainder in ['يوم', 'اليوم'] or remainder.startswith('يوم') or remainder.startswith('اليوم'):
                        category = "EXCLUDED"
                        reason = f"clitic prefix {prefix}"
                        excluded += 1
                        break
        
        # Check for pronominal suffixes
        elif any(clean.endswith(s) for s in ['ه', 'ها', 'هم', 'هن', 'ني', 'ك', 'كم', 'كن', 'ي']):
            category = "EXCLUDED" 
            reason = "pronominal suffix"
            excluded += 1
        
        # Check for plural forms
        elif 'ايام' in clean or 'أيام' in clean:
            category = "DAYS_PLURAL"
            reason = "أيام plural"
            days_plural += 1
        
        elif 'يومين' in clean:
            category = "DAYS_DUAL"
            reason = "يومين dual"
            days_plural += 1
        
        # Check for bare singular forms
        elif clean in ['يوم', 'اليوم'] or clean.endswith('يوم') or clean.endswith('اليوم'):
            # Allow case endings
            base_patterns = ['يوم', 'اليوم']
            for pattern in base_patterns:
                if clean == pattern:
                    category = "DAY_SINGULAR"
                    reason = f"bare {pattern}"
                    day_singular += 1
                    break
                elif clean.startswith(pattern) and len(clean) == len(pattern) + 1:
                    # Single character case ending
                    ending = clean[len(pattern):]
                    if ending in ['ا', 'ة', 'ه', 'ي', 'و', 'ن']:
                        category = "DAY_SINGULAR"
                        reason = f"bare {pattern} + case ending"
                        day_singular += 1
                        break
        
        if not category:
            category = "OTHER"
            reason = "other form"
        
        # Print first 50 for analysis
        if i < 50:
            print(f"  {ref:>8} | {orig:>15} | {clean:>10} | {category:>12} | {reason}")
    
    print(f"\nSUMMARY:")
    print(f"Day singular: {day_singular}")
    print(f"Days plural+dual: {days_plural}")
    print(f"Excluded: {excluded}")
    print(f"Total analyzed: {len(yawm_words)}")

def analyze_month_words():
    """Analyze all words containing شهر"""
    verses = load_quran()
    month_words = []
    
    for (surah, verse), text in verses.items():
        tokens = text.split()
        for token in tokens:
            clean = remove_diacritics(token)
            if 'شهر' in clean:
                month_words.append({
                    'reference': f"{surah}:{verse}",
                    'original': token,
                    'clean': clean
                })
    
    print(f"\nFound {len(month_words)} words containing شهر")
    
    month_singular = 0
    excluded = 0
    
    print("\nMonth words analysis:")
    for word in month_words:
        ref = word['reference']
        orig = word['original']
        clean = word['clean']
        
        # Check for plural exclusions
        if any(p in clean for p in ['أشهر', 'شهور', 'شهرين']):
            category = "EXCLUDED"
            reason = "plural/dual form"
            excluded += 1
        elif clean in ['شهر', 'الشهر'] or clean.endswith('شهر') or clean.endswith('الشهر'):
            category = "MONTH_SINGULAR"
            reason = "singular form"
            month_singular += 1
        else:
            category = "OTHER"
            reason = "other form"
        
        print(f"  {ref:>8} | {orig:>15} | {clean:>12} | {category:>12} | {reason}")
    
    print(f"\nMonth singular: {month_singular}")
    print(f"Excluded: {excluded}")

if __name__ == "__main__":
    print("=== DEBUG ANALYSIS OF CALENDAR WORDS ===")
    analyze_day_words()
    analyze_month_words()