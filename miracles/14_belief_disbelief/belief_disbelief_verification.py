#!/usr/bin/env python3
"""
Miracle 14: Belief vs Disbelief - Three Exact Ratios (5:3, 9:8, 5:4)
Verification Script

Verifies THREE exact mathematical ratios between belief and disbelief concepts:
1. Security (أَمْن): 5 vs Disbelief-alt (كُفُور): 3 = 5:3 ratio
2. Faith (إِيمَٰن): 45 vs Disbelief forms (كُفْر+كُفُور): 40 = 9:8 ratio
3. Faith+Security: 50 vs Disbelief forms: 40 = 5:4 ratio

All three ratios show belief/security forms EXCEED disbelief forms!

Source: Quranic Arabic Corpus (corpus.quran.com)
Run: python3 miracles/14_belief_disbelief/belief_disbelief_verification.py
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


def count_faith(tokens):
    """
    Count إِيمَٰن (Iman - faith/belief masdar)

    Include: إِيمَٰن, ٱلإِيمَٰن (masdar forms)
    Exclude: آمنوا (verbs), مؤمنون/مؤمنين (agents), مؤمن (adjective)

    QAC: 45 occurrences
    """
    matches = []

    for surah, verse, token in tokens:
        original = normalize_arabic(token)
        clean = remove_diacritics(original)

        # Exclude verb forms: آمن, آمنوا, آمنت, يؤمن, تؤمنون, etc.
        if 'آمن' in clean or 'يؤمن' in clean or 'تؤمن' in clean or 'نؤمن' in clean:
            continue
        if 'ءَامَن' in original or 'يُؤْمِن' in original or 'تُؤْمِن' in original:
            continue

        # Exclude agent nouns: مؤمن, مؤمنون, مؤمنين, مؤمنات
        if 'مؤمن' in clean or 'مؤمنو' in clean:
            continue
        if 'مُؤْمِن' in original or 'مُّؤْمِن' in original:
            continue

        # Look for ايمان / إيمان masdar
        # In Uthmani: ٱلإِيمَٰنُ / إِيمَٰن
        if 'ٱلْإِيمَٰن' in original or 'إِيمَٰن' in original:
            matches.append({
                'surah': surah,
                'verse': verse,
                'token': token
            })
        elif 'بِٱلْإِيمَٰن' in original or 'لِلْإِيمَٰن' in original:
            matches.append({
                'surah': surah,
                'verse': verse,
                'token': token
            })
        # Check without diacritics
        elif 'ايمان' in clean or 'الايمان' in clean or 'للايمان' in clean or 'بالايمان' in clean:
            matches.append({
                'surah': surah,
                'verse': verse,
                'token': token
            })

    return matches


def count_security(tokens):
    """
    Count أَمْن (Amn - security/safety noun)

    From root أ-م-ن (same as faith/belief)
    Specific noun meaning security/safety/peace

    QAC: 5 occurrences
    """
    matches = []

    for surah, verse, token in tokens:
        original = normalize_arabic(token)
        clean = remove_diacritics(original)

        # Exclude verbs and participles
        if 'آمن' in clean or 'مؤمن' in clean or 'ءامن' in clean:
            continue

        # Look for أَمْن noun (security)
        # In Uthmani: أَمْن, ٱلْأَمْن, بِأَمْن
        if 'أَمْن' in original:
            matches.append({
                'surah': surah,
                'verse': verse,
                'token': token
            })

    return matches


def count_disbelief_primary(tokens):
    """
    Count كُفْر (Kufr - disbelief masdar)

    Include ONLY: كُفْر masdar with diacritics كُفْر (damma-sukun pattern)
    Exclude: كَفَرَ verbs (fatha pattern), كافر agents, كُفْران different noun

    QAC: 37 occurrences
    """
    matches = []

    for surah, verse, token in tokens:
        original = normalize_arabic(token)
        clean = remove_diacritics(original)

        # CRITICAL: Exclude verbs كَفَرَ (fatha pattern)
        if 'كَفَرَ' in original or 'كَفَرُ' in original or 'كَفَرْ' in original:
            continue
        if 'يَكْفُر' in original or 'تَكْفُر' in original or 'نَكْفُر' in original:
            continue
        # Form II verb كَفَّرَ (to expiate/forgive)
        if 'كَفَّرَ' in original or 'كُفِّرَ' in original:
            continue

        # Exclude agent nouns: كافر, كافرون, كافرين, كفار
        if 'كافر' in clean or 'كفار' in clean:
            continue
        if 'كَٰفِر' in original or 'كُفَّار' in original:
            continue

        # Exclude كُفْران (different noun)
        if 'كُفْرَان' in original:
            continue

        # Exclude كُفُور (alternate noun - counted separately)
        if 'كُفُور' in original or 'كَفُور' in original:
            continue

        # ONLY match masdar كُفْر (noun with damma-sukun)
        if 'كُفْر' in original:
            matches.append({
                'surah': surah,
                'verse': verse,
                'token': token
            })

    return matches


def count_disbelief_alt(tokens):
    """
    Count كُفُور (Kufur - disbelief/ingratitude alternate noun)

    Different noun form from كُفْر, emphasizes ingratitude aspect

    CRITICAL: Must be كُفُور (damma-damma pattern), NOT كَفُور (fatha-damma = ungrateful adjective)
    - كَفُور (kafūr - ungrateful adjective): 12 occurrences (EXCLUDE)
    - كُفُور (kufūr - disbelief noun): 3 occurrences (INCLUDE)

    QAC: 3 occurrences
    """
    matches = []

    for surah, verse, token in tokens:
        original = normalize_arabic(token)
        clean = remove_diacritics(original)

        # Exclude كَفُور (ungrateful adjective - fatha on first letter)
        if 'كَفُور' in original:
            continue

        # ONLY match كُفُور (disbelief noun - damma on first letter)
        if 'كُفُور' in original:
            # Make sure it's not an agent noun or verb
            if 'كافر' not in clean and 'كفار' not in clean:
                matches.append({
                    'surah': surah,
                    'verse': verse,
                    'token': token
                })

    return matches


def main():
    print("=" * 80)
    print("MIRACLE 14: BELIEF vs DISBELIEF - THREE EXACT RATIOS")
    print("=" * 80)
    print()

    print("Loading Quran text...")
    verses, tokens = load_quran()
    print(f"Loaded {len(verses)} verses, {len(tokens)} tokens")
    print()

    # Count all forms
    print("Counting forms...")
    faith = count_faith(tokens)
    security = count_security(tokens)
    disbelief_primary = count_disbelief_primary(tokens)
    disbelief_alt = count_disbelief_alt(tokens)

    print()
    print("=" * 80)
    print("PATTERN 1: Security vs Disbelief-Ingratitude (5:3)")
    print("=" * 80)
    print()
    print(f"Security (أَمْن):              {len(security)} (target: 5)")
    print(f"Disbelief-alt (كُفُور):        {len(disbelief_alt)} (target: 3)")
    print(f"Ratio:                         {len(security)}:{len(disbelief_alt)}")
    print()

    if len(security) == 5 and len(disbelief_alt) == 3:
        print("✓ VERIFIED: Exact 5:3 ratio!")
        print(f"  Multiplier: {len(security)/len(disbelief_alt):.3f}x (security exceeds disbelief)")
    else:
        print(f"✗ FAILED: Expected 5:3, got {len(security)}:{len(disbelief_alt)}")

    print()
    print("=" * 80)
    print("PATTERN 2: Faith vs Disbelief Forms (9:8)")
    print("=" * 80)
    print()
    print(f"Faith masdar (إِيمَٰن):         {len(faith)} (target: 45)")
    print(f"Disbelief forms (كُفْر+كُفُور): {len(disbelief_primary)}+{len(disbelief_alt)}={len(disbelief_primary)+len(disbelief_alt)} (target: 40)")
    print(f"Ratio:                         {len(faith)}:{len(disbelief_primary)+len(disbelief_alt)}")
    print()

    if len(faith) == 45 and (len(disbelief_primary) + len(disbelief_alt)) == 40:
        print("✓ VERIFIED: Exact 9:8 ratio!")
        print(f"  Multiplier: {len(faith)/(len(disbelief_primary)+len(disbelief_alt)):.3f}x (faith exceeds disbelief)")
    else:
        print(f"✗ FAILED: Expected 45:40, got {len(faith)}:{len(disbelief_primary)+len(disbelief_alt)}")

    print()
    print("=" * 80)
    print("PATTERN 3: Faith+Security vs Disbelief (5:4)")
    print("=" * 80)
    print()
    print(f"Faith+Security (إِيمَٰن+أَمْن): {len(faith)}+{len(security)}={len(faith)+len(security)} (target: 50)")
    print(f"Disbelief forms (كُفْر+كُفُور): {len(disbelief_primary)}+{len(disbelief_alt)}={len(disbelief_primary)+len(disbelief_alt)} (target: 40)")
    print(f"Ratio:                         {len(faith)+len(security)}:{len(disbelief_primary)+len(disbelief_alt)}")
    print()

    if (len(faith) + len(security)) == 50 and (len(disbelief_primary) + len(disbelief_alt)) == 40:
        print("✓ VERIFIED: Exact 5:4 ratio!")
        print(f"  Multiplier: {(len(faith)+len(security))/(len(disbelief_primary)+len(disbelief_alt)):.3f}x (faith+security exceeds disbelief)")
    else:
        print(f"✗ FAILED: Expected 50:40, got {len(faith)+len(security)}:{len(disbelief_primary)+len(disbelief_alt)}")

    print()
    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print()

    pattern1_ok = (len(security) == 5 and len(disbelief_alt) == 3)
    pattern2_ok = (len(faith) == 45 and (len(disbelief_primary) + len(disbelief_alt)) == 40)
    pattern3_ok = ((len(faith) + len(security)) == 50 and (len(disbelief_primary) + len(disbelief_alt)) == 40)

    if pattern1_ok and pattern2_ok and pattern3_ok:
        print("✓ ALL THREE EXACT RATIOS VERIFIED!")
        print()
        print("  Pattern 1 (5:3): Security 5 vs Disbelief-alt 3")
        print("  Pattern 2 (9:8): Faith 45 vs Disbelief forms 40")
        print("  Pattern 3 (5:4): Faith+Security 50 vs Disbelief 40")
        print()
        print("All three ratios show belief/security forms > disbelief forms!")
        print("This reflects the Quranic teaching of divine mercy favoring faith.")
    else:
        print("✗ VERIFICATION FAILED")
        print()
        print(f"  Pattern 1 (5:3): {'✓' if pattern1_ok else '✗'}")
        print(f"  Pattern 2 (9:8): {'✓' if pattern2_ok else '✗'}")
        print(f"  Pattern 3 (5:4): {'✓' if pattern3_ok else '✗'}")


if __name__ == "__main__":
    main()
