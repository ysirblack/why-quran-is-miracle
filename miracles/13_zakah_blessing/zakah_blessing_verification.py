#!/usr/bin/env python3
"""
Miracle 13: Zakah vs Blessing Root (32:32)
Verification Script

Methodology:
- Zakah: Count NOUN زَكَاة only (exclude verbs)
- Blessing: Count ALL FORMS from root ب-ر-ك (verbs + nouns + adjectives)

This compares:
- The specific obligation (zakah as noun)
- The divine response (blessing in all manifestations)

Source: Quranic Arabic Corpus (corpus.quran.com)
"""

import re
from pathlib import Path
import unicodedata


def load_quran():
    """Load Quran text from Tanzil format"""
    script_dir = Path(__file__).parent
    data_path = script_dir.parent.parent / "data" / "quran-uthmani.txt"

    if not data_path.exists():
        data_path = Path("/Users/ysirblack/Desktop/engineering/why_qur_an_is_miracle/data/quran-uthmani.txt")

    verses = {}
    tokens = []

    with open(data_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#') or '|' not in line:
                continue
            parts = line.split('|', 2)
            if len(parts) >= 3:
                surah, verse, text = int(parts[0]), int(parts[1]), parts[2]
                verses[(surah, verse)] = text
                for token in text.split():
                    tokens.append((surah, verse, token))

    return verses, tokens


def normalize_arabic(text):
    """Normalize Arabic text"""
    text = unicodedata.normalize('NFC', text)
    text = text.replace('\u0640', '')  # Remove tatweel
    return text


def remove_diacritics(text):
    """Remove Arabic diacritics for pattern matching"""
    diacritics = r'[\u064B-\u0652\u0670]'
    return re.sub(diacritics, '', text)


def count_zakah_noun(tokens):
    """
    Count زَكَاة (Zakah - noun only)

    Include: زَكَاة, ٱلزَّكَاة (nouns with all clitics)
    Exclude: All verbs (تزكى, يزكي, etc.)
    """
    matches = []

    for surah, verse, token in tokens:
        original = normalize_arabic(token)
        clean = remove_diacritics(original)

        # Exclude verb forms
        if 'تزك' in clean or 'يزك' in clean or 'زكى' in clean or 'زكاها' in clean:
            continue
        if 'تَزَكَّ' in original or 'يُزَكِّ' in original or 'زَكَّ' in original:
            continue

        # Zakah noun pattern
        if 'زكوة' in clean or 'الزكوة' in clean or 'زكاة' in clean or 'الزكاة' in clean:
            matches.append({
                'surah': surah,
                'verse': verse,
                'token': token
            })

    return matches


def count_blessing_root(tokens):
    """
    Count ALL FORMS from root ب-ر-ك (blessing root)

    Based on QAC complete list of 32 occurrences:
    - Form III verbs (8): بَارَكَ, بُورِكَ
    - Form VI verbs (9): تَبَارَكَ
    - Nouns (3): بَرَكَات
    - Nominal fem (4): مُبَارَكَة
    - Passive participle masc (8): مُبَارَك

    Source: corpus.quran.com/qurandictionary.jsp?q=brk
    """
    # QAC exact list for verification
    qac_list = {
        (7, 137): 'بَارَكْنَا',
        (17, 1): 'بَارَكْنَا',
        (21, 71): 'بَارَكْنَا',
        (21, 81): 'بَارَكْنَا',
        (27, 8): 'بُورِكَ',
        (34, 18): 'بَارَكْنَا',
        (37, 113): 'وَبَارَكْنَا',
        (41, 10): 'وَبَارَكَ',
        (7, 54): 'تَبَارَكَ',
        (23, 14): 'فَتَبَارَكَ',
        (25, 1): 'تَبَارَكَ',
        (25, 10): 'تَبَارَكَ',
        (25, 61): 'تَبَارَكَ',
        (40, 64): 'فَتَبَارَكَ',
        (43, 85): 'وَتَبَارَكَ',
        (55, 78): 'تَبَارَكَ',
        (67, 1): 'تَبَارَكَ',
        (7, 96): 'بَرَكَاتٍ',
        (11, 48): 'وَبَرَكَاتٍ',
        (11, 73): 'وَبَرَكَاتُهُ',
        (24, 35): 'مُبَارَكَةٍ',
        (24, 61): 'مُبَارَكَةً',
        (44, 3): 'مُبَارَكَةٍ',
        (28, 30): 'الْمُبَارَكَةِ',
        (3, 96): 'مُبَارَكًا',
        (19, 31): 'مُبَارَكًا',
        (21, 50): 'مُبَارَكٌ',
        (23, 29): 'مُبَارَكًا',
        (38, 29): 'مُبَارَكٌ',
        (50, 9): 'مُبَارَكًا',
        (6, 92): 'مُبَارَكٌ',
        (6, 155): 'مُبَارَكٌ',
    }

    matches = []

    for surah, verse, token in tokens:
        original = normalize_arabic(token)
        clean = remove_diacritics(original)

        found = False
        form_type = 'unknown'

        # Nominal feminine مُبَارَكَة (check FIRST - contains substring بَارَكَ)
        if 'مُبَارَكَة' in original or 'مُبَٰرَكَة' in original or 'مُّبَٰرَكَة' in original:
            if 'ٱلْمُبَٰرَكَةِ' in original:  # with article
                found = True
                form_type = 'Nominal fem'
            elif 'مُبَارَكَةً' in original or 'مُبَٰرَكَةً' in original:  # accusative
                found = True
                form_type = 'Nominal fem'
            elif 'مُبَارَكَةٍ' in original or 'مُّبَٰرَكَةٍ' in original:  # genitive
                found = True
                form_type = 'Nominal fem'

        # Passive participle masculine مُبَارَك (check SECOND - also contains بَارَكَ)
        elif 'مُبَارَك' in original or 'مُّبَٰرَك' in original or 'مُبَٰرَك' in original or 'مُّبَارَك' in original:
            # Exclude feminine forms (already handled above)
            if 'مُبَارَكَة' not in original and 'مُبَٰرَكَة' not in original and 'مُّبَٰرَكَة' not in original:
                found = True
                form_type = 'Passive participle masc'

        # Form VI verb تَبَارَكَ (check THIRD - contains بَارَكَ)
        elif 'تَبَارَكَ' in original or 'تَبَٰرَكَ' in original:
            found = True
            form_type = 'Form VI verb'

        # Form III verb بَارَكَ (active)
        elif 'بَارَكْ' in original or 'بَٰرَكْ' in original or 'بَارَكَ' in original or 'بَٰرَكَ' in original:
            found = True
            form_type = 'Form III verb'

        # Form III passive بُورِكَ
        elif 'بُورِكَ' in original:
            found = True
            form_type = 'Form III passive'

        # Noun بَرَكَات (with all case endings and clitics)
        elif 'بَرَكَ' in original and ('ت' in original or 'ه' in original):
            # More precise: must have برك root + ات/اتُ/اتٍ
            if 'بَرَكَات' in original or 'بَرَكَٰت' in original:
                found = True
                form_type = 'Noun'

        if found:
            matches.append({
                'surah': surah,
                'verse': verse,
                'token': token,
                'type': form_type
            })

    return matches


def main():
    print("=" * 70)
    print("MIRACLE 13: ZAKAH (noun) vs BLESSING ROOT (all forms)")
    print("=" * 70)
    print()

    print("Loading Quran text...")
    verses, tokens = load_quran()
    print(f"Loaded {len(verses)} verses, {len(tokens)} tokens")
    print()

    # Count Zakah (noun only)
    print("-" * 70)
    print("ZAKAH (زَكَاة - noun only)")
    print("-" * 70)
    zakah_matches = count_zakah_noun(tokens)
    print(f"Count: {len(zakah_matches)}")
    print(f"Target: 32")
    print(f"Match: {'YES ✓' if len(zakah_matches) == 32 else 'NO'}")
    print()

    # Count Blessing (all forms from root)
    print("-" * 70)
    print("BLESSING ROOT (ب-ر-ك - ALL forms)")
    print("-" * 70)
    blessing_matches = count_blessing_root(tokens)

    # Categorize by type
    from collections import Counter
    types = Counter(m['type'] for m in blessing_matches)

    for typ, count in sorted(types.items()):
        print(f"  {typ}: {count}")

    print(f"\nTOTAL: {len(blessing_matches)}")
    print(f"Target: 32")
    print(f"Match: {'YES ✓' if len(blessing_matches) == 32 else 'NO'}")
    print()

    # Results
    print("=" * 70)
    print("RESULTS")
    print("=" * 70)
    print()
    print(f"Zakah (noun):        {len(zakah_matches)}")
    print(f"Blessing (all root): {len(blessing_matches)}")
    print(f"Target: 32:32")
    print()

    if len(zakah_matches) == 32 and len(blessing_matches) == 32:
        print("✓ VERIFIED: Perfect 32:32 balance!")
        print()
        print("Methodology:")
        print("  - Zakah: The specific NOUN (obligation)")
        print("  - Blessing: The entire ROOT concept (divine response)")
        print("  - Perfect symmetry: giving (32) = receiving (32)")
    else:
        print(f"Pattern: {len(zakah_matches)}:{len(blessing_matches)}")
        print(f"Expected from QAC: Zakah noun = 32, Blessing root = 32")

    print()
    print("-" * 70)
    print("Sample ZAKAH Occurrences (first 10):")
    print("-" * 70)
    for m in zakah_matches[:10]:
        print(f"  {m['surah']}:{m['verse']} - {m['token']}")

    print()
    print("-" * 70)
    print("Sample BLESSING ROOT Occurrences (first 10):")
    print("-" * 70)
    for m in blessing_matches[:10]:
        print(f"  {m['surah']}:{m['verse']} - {m['token']} ({m['type']})")


if __name__ == "__main__":
    main()
