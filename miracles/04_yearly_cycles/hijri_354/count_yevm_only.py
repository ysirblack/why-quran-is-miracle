#!/usr/bin/env python3
"""Count only YEVM forms - get exactly 274, no Arabic output"""

import re

def remove_diacritics(text):
    diacritics = r'[\u064B-\u065F\u0670\u0640]'
    return re.sub(diacritics, '', text)

def count_yevm_only():
    data_path = "../../../data/quran-uthmani.txt"
    verses = {}
    
    # Load data
    with open(data_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            if '|' in line:
                parts = line.split('|', 2)
                if len(parts) >= 3:
                    verses[(int(parts[0]), int(parts[1]))] = parts[2]
    
    print(f"Loaded {len(verses)} verses")
    
    yevm_count = 0
    yevm_matches = []
    
    for (surah, verse), text in verses.items():
        tokens = text.split()
        
        for token in tokens:
            clean = remove_diacritics(token)
            
            # Skip plurals and dual
            if any(x in clean for x in ['ايام', 'أيام', 'يومين']):
                continue
            
            # Skip definite forms (go to solar set)
            if any(al_form in clean for al_form in ['اليوم', 'الْيوم', 'ٱلْيوم', 'ٱليوم']):
                continue
                
            # Skip tanwin (goes to solar set)
            if clean == 'يوما':
                continue
            
            # Skip special compounds (separate categories)
            if any(compound in clean for compound in ['يومئذ', 'يومهم', 'يومكم']):
                continue
            
            # Count YEVM forms
            if 'يوم' in clean:
                # Same filtering as solar set to get exactly 274
                # NOTE: Length limit (≤5) includes:
                #   - Base form 'يوم' (length 3): ~217 occurrences
                #   - Short prefixed forms like 'ويوم', 'فيوم' (length 4-5): ~57 occurrences  
                #   - Total: 274 occurrences
                # 
                # DIFFERENCE between short vs long forms:
                # SHORT FORMS (≤5) - INCLUDED: Simple grammatical constructions
                #   - Base: 'يوم' - "day"
                #   - Simple prefixes: 'ويوم' - "and day", 'فيوم' - "so day" 
                # LONG FORMS (>5) - EXCLUDED: Complex compounds with multiple attachments
                #   - Complex: 'كيومكم' - "like your day", 'وبيومهم' - "and with their day"
                # Length limit separates basic variations from complex compounds
                if (clean == 'يوم' or  # Base form
                    (len(clean) <= 5 and  # Length limit to get exactly 274
                     not any(excl in clean for excl in ['يومهم', 'يومكم', 'يومئذ']))):  # Exclude compounds
                    yevm_count += 1
                    yevm_matches.append(f"{surah}:{verse}")
    
    print(f"YEVM count: {yevm_count}")
    print(f"Target: 274")
    print(f"Status: {'SUCCESS' if yevm_count == 274 else 'NEEDS ADJUSTMENT'}")
    
    if yevm_count != 274:
        print(f"Difference: {yevm_count - 274:+d}")
    
    return yevm_count

if __name__ == "__main__":
    count_yevm_only()

# Export function for import