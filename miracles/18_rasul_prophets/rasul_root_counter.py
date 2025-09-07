#!/usr/bin/env python3
"""Rasūl Root (ر-س-ل) Counter - Target: 513 total"""

import re
from pathlib import Path

def remove_diacritics(text):
    """Remove Arabic diacritics for cleaner pattern matching"""
    diacritics = r'[\u064B-\u065F\u0670\u0640]'
    return re.sub(diacritics, '', text)

def count_rasul_root():
    """Count all forms derived from the ر-س-ل root"""
    
    # Find the data file by searching up the directory tree
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
    
    # Load all verses
    all_verses = {}
    
    with open(data_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            if '|' in line:
                parts = line.split('|', 2)
                if len(parts) >= 3:
                    surah_num, verse_num, text = int(parts[0]), int(parts[1]), parts[2]
                    all_verses[(surah_num, verse_num)] = text
    
    print("=" * 80)
    print("RASŪL ROOT (ر-س-ل) COMPREHENSIVE COUNTER")
    print("=" * 80)
    print(f"Target: All morphological forms from root ر-س-ل = 513 tokens")
    print(f"Text standard: Tanzil Ḥafṣ/Uthmānī")
    print("-" * 60)
    
    # Root ر-س-ل patterns - comprehensive approach
    # Need to capture ALL forms from the trilateral root ر-س-ل
    
    total_count = 0
    all_matches = []
    
    # Pattern categories for analysis
    categories = {
        'messenger_nouns': 0,      # رسول، رسل variants
        'send_verbs': 0,           # أرسل and inflections  
        'message_nouns': 0,        # رسالة، رسالات
        'participles': 0,          # مرسل، مرسلة، مرسلات variants
        'other_forms': 0           # Any other ر-س-ل derived forms
    }
    
    print(f"Scanning for all ر-س-ل root derivatives...")
    print("-" * 60)
    
    for (surah, verse), text in all_verses.items():
        tokens = text.split()
        
        for token in tokens:
            clean_token = remove_diacritics(token)
            
            # Check if token contains ر-س-ل patterns
            # This is comprehensive - any token with the root sequence
            if ('رسل' in clean_token or 'رسول' in clean_token or 
                'ارسل' in clean_token or 'أرسل' in clean_token or
                'رسال' in clean_token or 'مرسل' in clean_token):
                
                total_count += 1
                
                # Categorize for analysis
                if 'رسول' in clean_token or 'رسل' in clean_token:
                    categories['messenger_nouns'] += 1
                    category = 'messenger'
                elif 'ارسل' in clean_token or 'أرسل' in clean_token:
                    categories['send_verbs'] += 1
                    category = 'send_verb'
                elif 'رسال' in clean_token:
                    categories['message_nouns'] += 1
                    category = 'message'
                elif 'مرسل' in clean_token:
                    categories['participles'] += 1
                    category = 'participle'
                else:
                    categories['other_forms'] += 1
                    category = 'other'
                
                # Store for analysis (limit output)
                if len(all_matches) < 30:
                    all_matches.append(f"{surah}:{verse} - {clean_token} ({category})")
    
    print(f"MORPHOLOGICAL BREAKDOWN:")
    print(f"• Messenger nouns (رسول/رسل): {categories['messenger_nouns']}")
    print(f"• Send verbs (أرسل variants): {categories['send_verbs']}")
    print(f"• Message nouns (رسالة/رسالات): {categories['message_nouns']}")
    print(f"• Participles (مرسل variants): {categories['participles']}")
    print(f"• Other ر-س-ل forms: {categories['other_forms']}")
    
    print(f"\nSAMPLE MATCHES (first 25 of {total_count}):")
    for i, match in enumerate(all_matches[:25], 1):
        print(f"  {i:2d}. {match}")
    
    if len(all_matches) > 25:
        print(f"  ... and {total_count - 25} more ر-س-ل tokens")
    
    print(f"\nTOTAL ر-س-ل ROOT COUNT: {total_count}")
    print(f"TARGET: 513")
    print(f"DIFFERENCE: {total_count - 513:+d}")
    
    # Assessment
    precision = abs(total_count - 513)
    if precision == 0:
        status = "✅ PERFECT MATCH!"
    elif precision <= 5:
        status = f"✅ EXCELLENT (±{precision})"
    elif precision <= 15:
        status = f"🔶 GOOD (±{precision})"
    else:
        status = f"⚪ NEEDS REFINEMENT (±{precision})"
    
    print(f"\nVERIFICATION STATUS: {status}")
    
    print(f"\nMETHODOLOGY NOTES:")
    print("-" * 60)
    print(f"• Root-based search: All tokens containing ر-س-ل sequences")
    print(f"• Morphological coverage: Verbs, nouns, participles included")
    print(f"• Comprehensive approach: Surface form pattern matching")
    print(f"• Target accuracy: Documented 513 total from all derivations")
    
    if precision > 15:
        print(f"\nREFINEMENT NEEDED:")
        print(f"• Current count ({total_count}) differs significantly from target (513)")
        print(f"• May need more specific morphological rules")
        print(f"• Consider Arabic linguistic expertise for exact root analysis")
    
    return {
        'total_count': total_count,
        'target': 513,
        'precision': precision,
        'categories': categories,
        'matches_sample': all_matches[:10]
    }

if __name__ == "__main__":
    count_rasul_root()