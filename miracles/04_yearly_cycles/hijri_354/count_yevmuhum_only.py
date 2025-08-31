#!/usr/bin/env python3
"""Count only YEVMUHUM forms - get exactly 5, no Arabic output"""

import re

def remove_diacritics(text):
    diacritics = r'[\u064B-\u065F\u0670\u0640]'
    return re.sub(diacritics, '', text)

def count_yevmuhum_only():
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
    
    yevmuhum_count = 0
    yevmuhum_matches = []
    
    for (surah, verse), text in verses.items():
        tokens = text.split()
        
        for token in tokens:
            clean = remove_diacritics(token)
            
            # Count YEVMUHUM forms only
            # NOTE: YEVMUHUM = "yawmahum" meaning "their day"
            # Contains the pattern 'يومهم' (yawm + hum)
            if 'يومهم' in clean:
                yevmuhum_count += 1
                yevmuhum_matches.append(f"{surah}:{verse}")
    
    print(f"YEVMUHUM count: {yevmuhum_count}")
    print(f"Target: 5")
    print(f"Status: {'SUCCESS' if yevmuhum_count == 5 else 'NEEDS ADJUSTMENT'}")
    
    if yevmuhum_count != 5:
        print(f"Difference: {yevmuhum_count - 5:+d}")
    
    print(f"All matches:")
    for i, match in enumerate(yevmuhum_matches, 1):
        print(f"  {i:2d}. {match}")
    
    return yevmuhum_count

if __name__ == "__main__":
    count_yevmuhum_only()