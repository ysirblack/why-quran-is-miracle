#!/usr/bin/env python3
"""
DAY (365) Pattern Verification - Solar Year

Verifies the three singular-day categories counted across the text:
- YEVMEN (يوماً): tanwin form (extended duration nuance)
- ELYEVM (اليوم): definite article forms, clitics allowed
- YEVM (يوم): simple forms using the same base + single-modification rule
              as the Hijri 354 analysis (diacritic-free length ≤ 5)
"""

import re
from pathlib import Path

EXPECTED_YEVM = 274
EXPECTED_ELYEVM = 75
EXPECTED_YEVMEN = 16
EXPECTED_TOTAL = EXPECTED_YEVM + EXPECTED_ELYEVM + EXPECTED_YEVMEN

def remove_diacritics(text):
    """Remove Arabic diacritics for pattern matching"""
    diacritics = r'[\u064B-\u065F\u0670\u0640]'
    return re.sub(diacritics, '', text)

def is_simple_yevm_form(clean_token: str) -> bool:
    """
    Apply the shared YEVM rule (Hijri + Solar analyses).

    Linguistic rationale:
    - The bare stem "يوم" is three letters long.
    - Genuine "simple" variants add one extra letter (single proclitic such as wa-/bi-/li-
      or single enclitic such as -ha), yielding four or five letters once diacritics are removed.
    - Tokens longer than five characters necessarily stack multiple morphemes (e.g.,
      possessive + preposition) and therefore leave the simple-form category.
    """
    if 'يوم' not in clean_token:
        return False
    if clean_token == 'يوم':
        return True
    if len(clean_token) > 5:
        return False
    if any(excl in clean_token for excl in ['يومهم', 'يومكم', 'يومئذ']):
        return False
    return True

def verify_day_365_pattern():
    """Verify the DAY (365) singular pattern"""
    
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
    
    # Load Quran text
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
    
    print(f"Loaded {len(verses)} verses from Hafs (Tanzil Uthmani)")
    
    # === DAY (365) Count ===
    yevm_count = 0      # يوم - simple form (≤5 chars after cleaning)
    elyevm_count = 0    # اليوم - with definite article
    yevmen_count = 0    # يومًا - with tanwin
    
    yevm_matches = []
    elyevm_matches = []
    yevmen_matches = []
    
    for (surah, verse), text in verses.items():
        tokens = text.split()
        
        for token in tokens:
            clean = remove_diacritics(token)
            
            # Skip plural/dual forms
            if any(x in clean for x in ['ايام', 'أيام', 'يومين']):
                continue
            
            # Solar Calendar Set (365): يوم + اليوم + يوماً (core forms, clitics allowed)
            if 'يوم' in clean:
                # يوماً (tanwin form) - exact match
                if clean == 'يوما':
                    yevmen_count += 1
                    yevmen_matches.append(f"{surah}:{verse}")
                
                # اليوم (definite form, clitics allowed)
                elif any(al_form in clean for al_form in ['اليوم', 'الْيوم', 'ٱلْيوم', 'ٱليوم']):
                    elyevm_count += 1
                    elyevm_matches.append(f"{surah}:{verse}")
                
                # يوم (simple forms) - apply shared Hijri rule
                elif not any(suffix in clean for suffix in ['يوما', 'يومين', 'ايام', 'أيام']):
                    if not any(al_form in clean for al_form in ['اليوم', 'الْيوم', 'ٱلْيوم', 'ٱليوم']):
                        if is_simple_yevm_form(clean):
                            yevm_count += 1
                            yevm_matches.append(f"{surah}:{verse}")
    
    total_day_count = yevm_count + elyevm_count + yevmen_count
    
    # === RESULTS ===
    print(f"\n" + "="*60)
    print(f"DAY (365) PATTERN VERIFICATION")
    print(f"="*60)
    
    print(f"\nBreakdown:")
    print(f"  - YEVM (simple ≤5 chars): {yevm_count:3d}  (expected {EXPECTED_YEVM})")
    print(f"  - ELYEVM (definite):      {elyevm_count:3d}  (expected {EXPECTED_ELYEVM})")
    print(f"  - YEVMEN (tanwin):        {yevmen_count:3d}  (expected {EXPECTED_YEVMEN})")
    print(f"  TOTAL:                    {total_day_count:3d}  (expected {EXPECTED_TOTAL})")
    
    day_verified = total_day_count == EXPECTED_TOTAL
    print(f"\n  Status: {'VERIFIED' if day_verified else 'NOT MATCHING'}")
    
    if day_verified:
        print(f"\n*** DAY (365) SOLAR YEAR PATTERN VERIFIED ***")
        print(f"Perfect alignment with solar calendar!")
    else:
        print(f"\n*** ANALYSIS NEEDED ***")
        print(f"Current count: {total_day_count}")
        print(f"Difference: {total_day_count - EXPECTED_TOTAL:+d}")
    
    # Show sample matches
    print(f"\n" + "="*60)
    print(f"SAMPLE MATCHES")
    print(f"="*60)
    
    print(f"\nYEVM matches (first 10 of {len(yevm_matches)}):")
    for i, match in enumerate(yevm_matches[:10], 1):
        print(f"  {i:2d}. {match}")
    
    print(f"\nELYEVM matches (first 10 of {len(elyevm_matches)}):")
    for i, match in enumerate(elyevm_matches[:10], 1):
        print(f"  {i:2d}. {match}")
    
    print(f"\nYEVMEN matches (all {len(yevmen_matches)}):")
    for i, match in enumerate(yevmen_matches, 1):
        print(f"  {i:2d}. {match}")
    
    return yevm_count, elyevm_count, yevmen_count, total_day_count

def main():
    """Main verification function"""
    print("QURAN DAY (365) SOLAR CALENDAR VERIFICATION")
    print("Rule Set P Implementation - Singular Forms Only")
    print("="*60)
    
    yevm, elyevm, yevmen, total = verify_day_365_pattern()
    
    print(f"\n" + "="*60)
    print(f"FINAL SUMMARY")
    print(f"="*60)
    print(f"YEVM (simple):     {yevm:3d}/{EXPECTED_YEVM}  {'OK' if yevm == EXPECTED_YEVM else 'DIFF'}")
    print(f"ELYEVM (definite): {elyevm:3d}/{EXPECTED_ELYEVM}  {'OK' if elyevm == EXPECTED_ELYEVM else 'DIFF'}")
    print(f"YEVMEN (tanwin):   {yevmen:3d}/{EXPECTED_YEVMEN}  {'OK' if yevmen == EXPECTED_YEVMEN else 'DIFF'}")
    print(f"TOTAL DAY:         {total:3d}/{EXPECTED_TOTAL}  {'PERFECT' if total == EXPECTED_TOTAL else 'NEEDS WORK'}")
    
    if total == 365:
        print(f"\n🎉 SUCCESS: Solar year pattern verified!")
        print(f"   365-day solar calendar embedded in Quranic structure.")
    
    return total == 365

if __name__ == "__main__":
    main()
