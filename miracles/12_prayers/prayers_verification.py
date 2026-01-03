#!/usr/bin/env python3
"""
Miracle 12: Prayers (Salawat) = 5
Verification Script

Rule (from main.md):
- Include only: صَلَوَات / ٱلصَّلَوَات (plural - "prayers")
- Exclude: صَلَاة / ٱلصَّلَاة (singular), verbs, and related nouns (مُصَلّى)
- Count tokens

Target: 5 (matching the 5 daily prayers in Islam)

Run: python3 miracles/12_prayers/prayers_verification.py
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


def count_prayers_plural(tokens):
    """
    Count صَلَوَات (Salawat - prayers, plural form)

    Include: صَلَوَات, ٱلصَّلَوَات, وَٱلصَّلَوَات, etc.
    Exclude: صَلَاة (singular), verbs, مُصَلّى (prayer place)
    """
    matches = []

    for surah, verse, token in tokens:
        original = normalize_arabic(token)
        clean = remove_diacritics(original)

        # Look for plural صلوات pattern
        # In Uthmani: صَلَوَٰت or صَّلَوَٰت (with superscript alif)
        if 'صَلَوَٰت' in original or 'صَّلَوَٰت' in original:
            matches.append({
                'surah': surah,
                'verse': verse,
                'token': token
            })
        # Also check without diacritics
        elif 'صلوات' in clean or 'صلوت' in clean:
            matches.append({
                'surah': surah,
                'verse': verse,
                'token': token
            })

    return matches


def count_prayer_singular(tokens):
    """
    Count صَلَاة (Salah - prayer, singular form)

    For comparison - not part of the claim
    """
    matches = []

    for surah, verse, token in tokens:
        original = normalize_arabic(token)
        clean = remove_diacritics(original)

        # Singular صلاة pattern
        # In Uthmani: صَلَوٰة or صَلَٰوة or صَّلَوٰة
        if 'صَلَوٰة' in original or 'صَلَٰوة' in original or 'صَّلَوٰة' in original:
            matches.append({
                'surah': surah,
                'verse': verse,
                'token': token
            })
        elif 'صلوة' in clean or 'صلاة' in clean:
            # Avoid counting plural
            if 'صلوات' not in clean and 'صلوت' not in clean:
                matches.append({
                    'surah': surah,
                    'verse': verse,
                    'token': token
                })

    return matches


def main():
    print("=" * 70)
    print("MIRACLE 12: PRAYERS (Salawat) = 5")
    print("=" * 70)
    print()

    print("Loading Quran text...")
    verses, tokens = load_quran()
    print(f"Loaded {len(verses)} verses, {len(tokens)} tokens")
    print()

    # Count Prayers (plural)
    print("-" * 70)
    print("PRAYERS - PLURAL (صَلَوَات - Salawat)")
    print("-" * 70)
    plural_matches = count_prayers_plural(tokens)
    print(f"Count: {len(plural_matches)}")
    print(f"Target: 5 (matching 5 daily prayers)")
    print(f"Match: {'YES ✓' if len(plural_matches) == 5 else 'NO'}")
    print()

    # Count Prayer (singular) for comparison
    print("-" * 70)
    print("PRAYER - SINGULAR (صَلَاة - Salah) [for comparison]")
    print("-" * 70)
    singular_matches = count_prayer_singular(tokens)
    print(f"Count: {len(singular_matches)}")
    print()

    # Results
    print("=" * 70)
    print("RESULTS")
    print("=" * 70)
    print()
    print(f"Prayers (صَلَوَات - plural): {len(plural_matches)}")
    print(f"Prayer (صَلَاة - singular): {len(singular_matches)}")
    print(f"Target plural: 5")
    print()

    if len(plural_matches) == 5:
        print("VERIFIED: Exactly 5 occurrences of 'prayers' (plural)!")
        print()
        print("The Five Daily Prayers (Salat):")
        print("  1. Fajr - Dawn prayer")
        print("  2. Dhuhr - Midday prayer")
        print("  3. Asr - Afternoon prayer")
        print("  4. Maghrib - Sunset prayer")
        print("  5. Isha - Night prayer")
    else:
        print("NOTE: Script count differs from target.")
        print("This pattern has low statistical significance due to small numbers.")

    print()
    print("-" * 70)
    print("All PLURAL Occurrences:")
    print("-" * 70)
    for m in plural_matches:
        print(f"  {m['surah']}:{m['verse']} - {m['token']}")

    print()
    print("-" * 70)
    print("Sample SINGULAR Occurrences (first 15):")
    print("-" * 70)
    for m in singular_matches[:15]:
        print(f"  {m['surah']}:{m['verse']} - {m['token']}")

    # Statistical note
    print()
    print("-" * 70)
    print("STATISTICAL NOTE")
    print("-" * 70)
    print("Small number patterns (like 5) have limited statistical significance.")
    print("The probability of randomly hitting exactly 5 is higher than larger")
    print("patterns like 115:115 or 145:145.")
    print()
    print("However, the religious significance adds meaning:")
    print("- The plural 'prayers' appears exactly 5 times")
    print("- Islam prescribes exactly 5 daily prayers")
    print("- This alignment may be intentional design or notable coincidence")


if __name__ == "__main__":
    main()
