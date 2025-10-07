#!/usr/bin/env python3
"""
Count YEVMEIZIN (that day) forms.

Linguistic category: All forms of يومئذ (yawma'idhin - "that day")
- Counts every occurrence regardless of prefixes or grammatical role
- Simple, consistent rule: if it contains يومئذ, count it
"""

import re

def remove_diacritics(text):
    diacritics = r'[\u064B-\u065F\u0670\u0640]'
    return re.sub(diacritics, '', text)

def count_yevmeizin_only():
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
    
    yevmeizin_count = 0
    yevmeizin_matches = []
    
    for (surah, verse), text in verses.items():
        tokens = text.split()
        
        for token in tokens:
            clean = remove_diacritics(token)
            
            # Count ALL YEVMEIZIN forms
            # YEVMEIZIN = yawma'idhin (يومئذ) meaning "that day" or "on that day"
            # No filtering - count every occurrence
            if 'يومئذ' in clean:
                yevmeizin_count += 1
                yevmeizin_matches.append(f"{surah}:{verse}")
    
    print(f"YEVMEIZIN (all forms) count: {yevmeizin_count}")
    print(f"Linguistic rule: All forms of yawma'idhin (that day)")
    print(f"No filtering - counts base forms, prefixed forms, all grammatical variants")
    
    return yevmeizin_count

if __name__ == "__main__":
    count_yevmeizin_only()
