#!/usr/bin/env python3
"""
Count YEVMEKUM (your day) forms.

Linguistic category: All forms of يومكم (yawmakum - "your day")
- Counts every occurrence of the possessive form "your day"
"""

import re

def remove_diacritics(text):
    diacritics = r'[\u064B-\u065F\u0670\u0640]'
    return re.sub(diacritics, '', text)

def count_yevmekum_only():
    # Find the data file by searching up the directory tree
    from pathlib import Path
    current_dir = Path(__file__).parent
    data_path = None
    for _ in range(5):
        potential_path = current_dir / "data" / "quran-uthmani.txt"
        if potential_path.exists():
            data_path = str(potential_path)
            break
        current_dir = current_dir.parent
    if not data_path:
        raise FileNotFoundError("Could not find quran-uthmani.txt data file")
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
    
    yevmekum_count = 0
    yevmekum_matches = []
    
    for (surah, verse), text in verses.items():
        tokens = text.split()
        
        for token in tokens:
            clean = remove_diacritics(token)
            
            # Count YEVMEKUM forms only
            # NOTE: YEVMEKUM = "yawmakum" meaning "your day"
            # Contains the pattern 'يومكم' (yawm + kum)
            if 'يومكم' in clean:
                yevmekum_count += 1
                yevmekum_matches.append(f"{surah}:{verse}")
    
    print(f"YEVMEKUM (your day) count: {yevmekum_count}")
    print(f"Linguistic rule: All forms of yawmakum (your day)")
    
    return yevmekum_count

if __name__ == "__main__":
    count_yevmekum_only()