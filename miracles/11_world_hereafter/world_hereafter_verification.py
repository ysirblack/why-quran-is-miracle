#!/usr/bin/env python3
"""
Miracle 11: World vs Hereafter (115:115)
Verification Script

Rule (from main.md):
- World: الدنيا with or without clitics
- Hereafter: الآخرة AND orthographic الاخرة, with or without clitics

IMPORTANT: Both spellings of "hereafter" must be included:
- الآخرة (with hamza - standard)
- الاخرة (with plain alif - Quranic variant)

Run: python3 miracles/11_world_hereafter/world_hereafter_verification.py
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


def count_world(tokens):
    """
    Count الدنيا (ad-Dunya - the World)

    Include: All tokens of الدنيا with or without clitics
    Examples: الدنيا, بالدنيا, وللدنيا, للدنيا

    Two orthographic variants:
    - ٱلدُّنْيَا (110 occurrences - without maddah)
    - ٱلدُّنْيَآ (5 occurrences - with maddah)
    """
    matches = []

    for surah, verse, token in tokens:
        original = normalize_arabic(token)
        clean = remove_diacritics(original)

        # الدنيا pattern (with various prefixes)
        # Two Tanzil variants:
        # - ٱلدُّنْيَا (standard)
        # - ٱلدُّنْيَآ (with maddah)
        if 'ٱلدُّنْيَا' in original or 'ٱلدُّنْيَآ' in original:
            matches.append({
                'surah': surah,
                'verse': verse,
                'token': token
            })
        elif 'الدنيا' in clean or 'لدنيا' in clean:
            matches.append({
                'surah': surah,
                'verse': verse,
                'token': token
            })

    return matches


def count_hereafter(tokens):
    """
    Count الآخرة (al-Akhirah - the Hereafter)

    Include: All tokens with or without clitics
    - Both orthographies: الآخرة (with hamza) and الاخرة (plain alif)
    - With clitics: بالآخرة, للآخرة, والآخرة, etc.

    In Uthmani script: ٱلْـَٔاخِرَةِ (with tatweel and hamza above)
    """
    matches = []

    for surah, verse, token in tokens:
        original = normalize_arabic(token)
        clean = remove_diacritics(original)

        # Check for various forms of "the hereafter"
        # Uthmani uses: ٱلْـَٔاخِرَة (with tatweel ـ and hamza ٔ)
        # The key pattern is: ـَٔاخِرَة or ءَاخِرَة

        found = False

        # Check for the Uthmani pattern with ـَٔ (tatweel + hamza above)
        # This is the most common pattern in the Tanzil text
        if 'ـَٔاخِرَة' in original:
            found = True

        # Check for other possible patterns
        if not found:
            # Remove tatweel and check
            no_tatweel = original.replace('\u0640', '')
            # Check for ٔاخرة pattern (high hamza)
            if 'ٔاخِرَة' in no_tatweel or 'ٔاخرة' in no_tatweel:
                found = True
            # Check for ءاخرة (standalone hamza)
            elif 'ءَاخِرَة' in no_tatweel or 'ءاخرة' in no_tatweel:
                found = True

        # Also check clean (no diacritics) for broader match
        if not found:
            # Remove tatweel from clean too
            clean_no_tatweel = clean.replace('\u0640', '')
            # Look for اخرة pattern (definite "the hereafter")
            if 'لاخرة' in clean_no_tatweel:
                found = True

        if found:
            matches.append({
                'surah': surah,
                'verse': verse,
                'token': token
            })

    return matches


def main():
    print("=" * 70)
    print("MIRACLE 11: WORLD (ad-Dunya) vs HEREAFTER (al-Akhirah)")
    print("=" * 70)
    print()

    print("Loading Quran text...")
    verses, tokens = load_quran()
    print(f"Loaded {len(verses)} verses, {len(tokens)} tokens")
    print()

    # Count World
    print("-" * 70)
    print("WORLD (الدنيا - ad-Dunya)")
    print("-" * 70)
    world_matches = count_world(tokens)
    print(f"Count: {len(world_matches)}")
    print(f"Target: 115")
    print(f"Match: {'YES ✓' if len(world_matches) == 115 else 'NO'}")
    print()

    # Count Hereafter
    print("-" * 70)
    print("HEREAFTER (الآخرة - al-Akhirah)")
    print("-" * 70)
    hereafter_matches = count_hereafter(tokens)
    print(f"Count: {len(hereafter_matches)}")
    print(f"Target: 115")
    print(f"Match: {'YES ✓' if len(hereafter_matches) == 115 else 'NO'}")
    print()

    # Results
    print("=" * 70)
    print("RESULTS")
    print("=" * 70)
    print()
    print(f"World (الدنيا): {len(world_matches)}")
    print(f"Hereafter (الآخرة): {len(hereafter_matches)}")
    print(f"Target: 115:115")
    print()

    if len(world_matches) == 115 and len(hereafter_matches) == 115:
        print("VERIFIED: Perfect 115:115 balance!")
    else:
        print("NOTE: Script count differs from target.")
        print()
        print("The 115:115 balance requires including:")
        print("  - Both orthographic variants of الآخرة")
        print("  - All clitic prefixes (بـ، و، ل، etc.)")
        print()
        print("Key theme: Quranic duality of temporal vs eternal existence.")
        print("See Quran 2:201: 'Give us good in this world and good in the next'")

    print()
    print("-" * 70)
    print("Sample World Occurrences (first 15):")
    print("-" * 70)
    for m in world_matches[:15]:
        print(f"  {m['surah']}:{m['verse']} - {m['token']}")

    print()
    print("-" * 70)
    print("Sample Hereafter Occurrences (first 15):")
    print("-" * 70)
    for m in hereafter_matches[:15]:
        print(f"  {m['surah']}:{m['verse']} - {m['token']}")


if __name__ == "__main__":
    main()
