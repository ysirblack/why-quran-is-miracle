#!/usr/bin/env python3
"""Verify Adam and Jesus proper name counts - both should be exactly 25"""

import re

def remove_diacritics(text):
    diacritics = r'[\u064B-\u065F\u0670\u0640]'
    return re.sub(diacritics, '', text)

def verify_adam_jesus():
    data_path = "../../data/quran-uthmani.txt"
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
    print("=" * 50)
    
    adam_count = 0
    jesus_count = 0
    adam_matches = []
    jesus_matches = []
    
    for (surah, verse), text in verses.items():
        tokens = text.split()
        
        for token in tokens:
            clean = remove_diacritics(token)
            
            # Count ADAM - proper name only
            # Multiple spellings: ءادم (hamza+alif+dal+meem) and ادم (alif+dal+meem)
            # Also appears as يءادم in vocative constructions
            if 'ادم' in clean:  # Will match both ءادم and يءادم patterns
                adam_count += 1
                adam_matches.append(f"{surah}:{verse}")
            
            # Count JESUS - proper name only  
            # Pattern: عيسى (Isa/Jesus) - exclude titles like المسيح, ابن مريم
            # QAC confirmed spelling: عِيسَىٰ (ain + ya + seen + alif)
            elif 'عيسى' in clean:
                jesus_count += 1
                jesus_matches.append(f"{surah}:{verse}")
    
    print("ADAM & JESUS PROPER NAME VERIFICATION")
    print("=" * 50)
    print(f"ADAM (proper name):    {adam_count:3d} / 25 target")
    print(f"JESUS (proper name):   {jesus_count:3d} / 25 target")
    print("-" * 30)
    print(f"BALANCE CHECK:         {'EQUAL' if adam_count == jesus_count else 'UNEQUAL'}")
    print(f"TARGET MATCH:          {'SUCCESS' if adam_count == 25 and jesus_count == 25 else 'NEEDS ADJUSTMENT'}")
    
    if adam_count != 25 or jesus_count != 25:
        print(f"\nDifferences:")
        if adam_count != 25: print(f"  ADAM: {adam_count - 25:+d}")
        if jesus_count != 25: print(f"  JESUS: {jesus_count - 25:+d}")
    
    print(f"\nADAM matches (first 10):")
    for i, match in enumerate(adam_matches[:10], 1):
        print(f"  {i:2d}. {match}")
    
    print(f"\nJESUS matches (first 10):")
    for i, match in enumerate(jesus_matches[:10], 1):
        print(f"  {i:2d}. {match}")
    
    print(f"\nTHEOLOGICAL NOTE:")
    print(f"Quran 3:59 explicitly pairs Adam and Jesus:")
    print(f"'The example of Jesus with Allah is like that of Adam...'")
    print(f"Both created without human fathers - miraculous origins")
    
    return {
        'adam': adam_count,
        'jesus': jesus_count,
        'balanced': adam_count == jesus_count,
        'target_hit': adam_count == 25 and jesus_count == 25
    }

if __name__ == "__main__":
    verify_adam_jesus()