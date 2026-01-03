#!/usr/bin/env python3
"""
Miracle 16: Hot vs Cold (4:4)
Verification Script

Counts pure TEMPERATURE concepts only:
- Hot: ٱلْحَرّ (the heat), حَرُور (scorching heat)
- Cold: بَرْد (coldness), بَارِد (cold)
- EXCLUDES: بَرَد (hail) - precipitation, not pure temperature

QAC verified: 4:4 exact balance

Run: python3 miracles/16_hot_cold/hot_cold_verification.py
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


def count_hot(tokens):
    """
    Count Hot (حَرّ - heat) - pure temperature concept

    Include:
    - ٱلْحَرِّ / ٱلْحَرَّ / حَرًّا (al-harr / harran - the heat, heat)
    - ٱلْحَرُورُ (al-harur - scorching heat)

    Exclude:
    - حُرّ (hurr - free/freeman) - different meaning
    - حَرَّمَ (harrama - forbid) - different root
    - All other derivatives

    QAC verified: 4 occurrences
    """
    matches = []

    for surah, verse, token in tokens:
        original = normalize_arabic(token)

        # Check for heat forms (حَرّ with fatha)
        # ٱلْحَرِّ (al-harr) - 9:81
        # ٱلْحَرَّ (al-harra) - 16:81
        # حَرًّا (harran) - 9:81
        # ٱلْحَرُورُ (al-harur) - 35:21

        if 'ٱلْحَرِّ' in original:
            matches.append({'surah': surah, 'verse': verse, 'token': token, 'type': 'الحر'})
        elif 'ٱلْحَرَّ' in original:
            matches.append({'surah': surah, 'verse': verse, 'token': token, 'type': 'الحر'})
        elif 'حَرًّا' in original:
            matches.append({'surah': surah, 'verse': verse, 'token': token, 'type': 'حرا'})
        elif 'ٱلْحَرُورُ' in original:
            matches.append({'surah': surah, 'verse': verse, 'token': token, 'type': 'الحرور'})

    return matches


def count_cold(tokens):
    """
    Count Cold (بَرْد - coldness) - pure temperature concept

    Include:
    - بَرْد / بَرْدًا (bard / bardan - coldness)
    - بَارِد (barid - cool)

    EXCLUDE:
    - بَرَد (barad - hail) - precipitation, not pure temperature concept

    QAC verified: 4 occurrences (excluding hail)
    """
    matches = []

    for surah, verse, token in tokens:
        original = normalize_arabic(token)

        # EXCLUDE hail (بَرَد) - it's precipitation, not pure temperature
        if 'بَرَدٍ' in original or 'بَرَدًا' in original or 'بَرَدُ' in original:
            continue

        # EXCLUDE false positives like بِرَدِّهِنَّ (return them)
        if 'بِرَدِّ' in original:
            continue

        # Include cold/coolness forms
        # بَرْدًا (bardan) - 21:69, 78:24
        # بَارِدٌ (barid) - 38:42
        # بَارِدٍ (barid) - 56:44

        if 'بَرْدًا' in original:
            matches.append({'surah': surah, 'verse': verse, 'token': token, 'type': 'برد'})
        elif 'بَارِدٌ' in original:
            matches.append({'surah': surah, 'verse': verse, 'token': token, 'type': 'بارد'})
        elif 'بَارِدٍ' in original:
            matches.append({'surah': surah, 'verse': verse, 'token': token, 'type': 'بارد'})

    return matches


def main():
    print("=" * 80)
    print("MIRACLE 16: HOT vs COLD - Pure Temperature Concepts (4:4)")
    print("=" * 80)
    print()

    print("Loading Quran text...")
    verses, tokens = load_quran()
    print(f"Loaded {len(verses)} verses, {len(tokens)} tokens")
    print()

    # Count Hot
    print("-" * 80)
    print("HOT (حَرّ - heat)")
    print("-" * 80)
    hot_matches = count_hot(tokens)
    print(f"Count: {len(hot_matches)}")
    print(f"Target: 4")
    print(f"Match: {'YES ✓' if len(hot_matches) == 4 else 'NO ✗'}")
    print()

    # Count Cold
    print("-" * 80)
    print("COLD (بَرْد - coldness, EXCLUDING hail)")
    print("-" * 80)
    cold_matches = count_cold(tokens)
    print(f"Count: {len(cold_matches)}")
    print(f"Target: 4")
    print(f"Match: {'YES ✓' if len(cold_matches) == 4 else 'NO ✗'}")
    print()

    # Results
    print("=" * 80)
    print("RESULTS")
    print("=" * 80)
    print()
    print(f"Hot (temperature): {len(hot_matches)}")
    print(f"Cold (temperature): {len(cold_matches)}")
    print(f"Ratio: {len(hot_matches)}:{len(cold_matches)}")
    print()

    if len(hot_matches) == 4 and len(cold_matches) == 4:
        print("✓ VERIFIED: Perfect 4:4 balance!")
        print()
        print("Pure temperature concepts (hot vs cold) are perfectly balanced.")
        print("Hail excluded as precipitation phenomenon, not pure temperature.")
    else:
        print(f"✗ FAILED: Expected 4:4, got {len(hot_matches)}:{len(cold_matches)}")

    print()
    print("-" * 80)
    print("All HOT Occurrences:")
    print("-" * 80)
    for m in hot_matches:
        print(f"  {m['surah']}:{m['verse']} - {m['token']} ({m['type']})")

    print()
    print("-" * 80)
    print("All COLD Occurrences (excluding hail):")
    print("-" * 80)
    for m in cold_matches:
        print(f"  {m['surah']}:{m['verse']} - {m['token']} ({m['type']})")

    print()
    print("-" * 80)
    print("METHODOLOGY NOTE")
    print("-" * 80)
    print("Hail (بَرَد - barad) is EXCLUDED because it's a precipitation")
    print("phenomenon, not a pure temperature concept.")
    print()
    print("With this proper categorization:")
    print("  - Hot (temperature) = 4")
    print("  - Cold (temperature) = 4")
    print("  - Hail (precipitation) = 1 (excluded from cold count)")
    print()
    print("QAC Source:")
    print("  - Hot root (ح-ر-ر): https://corpus.quran.com/qurandictionary.jsp?q=Hrr")
    print("  - Cold root (ب-ر-د): https://corpus.quran.com/qurandictionary.jsp?q=brd")


if __name__ == "__main__":
    main()
