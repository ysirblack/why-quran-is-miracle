#!/usr/bin/env python3
"""
Life vs Death - 105:105 Perfect Balance Verification

Methodology: Count NOUNS ONLY (concepts, not actions)
- Life root (ح-ي-ي): Noun forms meaning life/living/alive
- Death root (م-و-ت): Noun forms meaning death/dead/dying

Source: Quranic Arabic Corpus (corpus.quran.com)
Run: python3 miracles/10_life_death/life_death_verification.py
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
    # Remove harakat and other marks
    diacritics = r'[\u064B-\u0652\u0670\u06DF\u06E2\u06E5\u06E6\u0653]'
    return re.sub(diacritics, '', text)


def count_life_nouns(tokens):
    """
    Count LIFE nouns from root ح-ي-ي (Ha-Ya-Ya)

    Target counts from QAC:
    - حَىّ (hayy - alive/living): 24
    - حَيَوٰة (hayat - life): 76
    - حَيَوَان (hayawan - creature): 1
    - مَحْيَا (mahya - living): 2
    - مُحْىِ (muhyi - giver of life): 2
    TOTAL: 105

    Exclude:
    - All verbs
    - حَيَّة (snake): 1
    - تَحِيَّة (greeting): 6
    - ٱسْتِحْيَآء (shyness): 1
    """
    results = {
        'hayy': [],      # حَىّ (alive/living) - target 24
        'hayat': [],     # حَيَوٰة (life) - target 76
        'hayawan': [],   # حَيَوَان (creature) - target 1
        'mahya': [],     # مَحْيَا (living) - target 2
        'muhyi': [],     # مُحْىِ (giver of life) - target 2
        'excluded': []   # Excluded forms
    }

    for surah, verse, token in tokens:
        original = normalize_arabic(token)
        clean = remove_diacritics(original)

        # ============================================
        # EXCLUSIONS - Must check first
        # ============================================

        # Exclude verbs (Form I, II, IV, X)
        # Form IV verbs: أَحْيَا, فَأَحْيَا, أَحْيَاهَا, etc.
        # Be careful NOT to exclude the noun أَحْيَآء (living ones)
        if 'أَحْيَا' in original or 'أَحْيَٰ' in original:  # Verb with alif/superscript alif
            continue
        if 'فَأَحْيَا' in original or 'فَأَحْيَٰ' in original:
            continue
        # Form IV imperfect: يُحْيِى, نُحْيِى, تُحْيِى
        if 'يُحْىِ' in original or 'يُحْيِ' in original:
            continue
        if 'نُحْىِ' in original or 'تُحْىِ' in original:
            continue
        if 'يُحْيِيكُمْ' in original or 'فَأَحْيَٰكُمْ' in original:
            continue

        # Form X verbs: يَسْتَحْىِ, تَسْتَحْىِ, وَيَسْتَحْيُونَ
        if 'يَسْتَحْ' in original or 'تَسْتَحْ' in original or 'وَيَسْتَحْ' in original:
            continue

        # Form I verb: يَحْيَا, يَحْيَىٰ (but NOT حَيًّا which is noun)
        if 'يَحْيَا' in original or 'يَحْيَىٰ' in original:
            continue

        # Form II verb: حَيُّوا (greet)
        if 'حَيُّوا' in original:
            continue

        # Exclude: حَيَّة (snake) - 20:20
        if 'حَيَّة' in original:
            results['excluded'].append({
                'surah': surah, 'verse': verse, 'token': token, 'reason': 'snake'
            })
            continue

        # Exclude: تَحِيَّة (greeting) - verbal noun
        if 'تَحِيَّة' in original or 'تَحِيَّت' in original:
            results['excluded'].append({
                'surah': surah, 'verse': verse, 'token': token, 'reason': 'greeting'
            })
            continue

        # Exclude: ٱسْتِحْيَآء (shyness) - 28:25
        if 'ٱسْتِحْيَآء' in original:
            results['excluded'].append({
                'surah': surah, 'verse': verse, 'token': token, 'reason': 'shyness'
            })
            continue

        # ============================================
        # NOUN FORMS TO COUNT
        # ============================================

        # 1. حَيَوٰة / ٱلْحَيَوٰة (life) - target 76
        # Patterns: حَيَوٰة, ٱلْحَيَوٰة, لِلْحَيَوٰة, بِٱلْحَيَوٰة, وَٱلْحَيَوٰة
        if 'حَيَوٰة' in original:
            results['hayat'].append({
                'surah': surah, 'verse': verse, 'token': token
            })
            continue
        # Also check: حَيَات forms (different Unicode - uses regular alif)
        # حَيَاتُنَا (our life), حَيَاتِكُمُ (your life), لِحَيَاتِى (for my life)
        if 'حَيَات' in original or 'حَيَاتُ' in original or 'حَيَاتِ' in original:
            results['hayat'].append({
                'surah': surah, 'verse': verse, 'token': token
            })
            continue

        # 2. حَىّ / ٱلْحَىّ (alive/living) - target 24
        # Key: Uses ى (U+0649) not ي (U+064A), with shadda
        # Definite forms: ٱلْحَىُّ (nom), ٱلْحَىِّ (gen), ٱلْحَىَّ (acc)
        if 'ٱلْحَىُّ' in original or 'ٱلْحَىِّ' in original or 'ٱلْحَىَّ' in original:
            results['hayy'].append({
                'surah': surah, 'verse': verse, 'token': token
            })
            continue
        # With preposition: لِلْحَىِّ
        if 'لِلْحَىِّ' in original:
            results['hayy'].append({
                'surah': surah, 'verse': verse, 'token': token
            })
            continue
        # Indefinite forms: حَىٌّ (nom), حَىٍّ (gen), حَيًّا (acc with yaa)
        if 'حَىٌّ' in original or 'حَىٍّ' in original:
            results['hayy'].append({
                'surah': surah, 'verse': verse, 'token': token
            })
            continue
        # حَيًّا - indefinite accusative (uses regular yaa ي)
        if 'حَيًّا' in original:
            results['hayy'].append({
                'surah': surah, 'verse': verse, 'token': token
            })
            continue
        # Plural forms: أَحْيَآء with various endings
        # أَحْيَآءٌ (nom), أَحْيَآءٍ (gen), أَحْيَآءً (acc), ٱلْأَحْيَآءُ (def)
        if 'أَحْيَآء' in original or 'ٱلْأَحْيَآء' in original:
            results['hayy'].append({
                'surah': surah, 'verse': verse, 'token': token
            })
            continue
        # Also check patterns with regular yaa (some may use ي)
        if 'ٱلْحَيُّ' in original or 'ٱلْحَيِّ' in original or 'ٱلْحَيَّ' in original:
            results['hayy'].append({
                'surah': surah, 'verse': verse, 'token': token
            })
            continue

        # 3. حَيَوَان (creature/animal) - target 1 (only 29:64)
        if 'ٱلْحَيَوَانُ' in original or 'حَيَوَان' in original:
            results['hayawan'].append({
                'surah': surah, 'verse': verse, 'token': token
            })
            continue

        # 4. مَحْيَا (living/life) - target 2 (6:162, 45:21)
        if 'مَحْيَا' in original or 'مَّحْيَا' in original:
            results['mahya'].append({
                'surah': surah, 'verse': verse, 'token': token
            })
            continue

        # 5. مُحْىِ (giver of life) - active participle - target 2 (30:50, 41:39)
        # Pattern: لَمُحْىِ, مُحْىِ (but not يُحْىِ which is verb)
        if 'لَمُحْىِ' in original:
            results['muhyi'].append({
                'surah': surah, 'verse': verse, 'token': token
            })
            continue
        # Check for standalone مُحْىِ that's not a verb
        if 'مُحْىِ' in original and 'يُحْىِ' not in original and 'نُحْىِ' not in original and 'تُحْىِ' not in original:
            # Make sure it's the noun form
            if original.startswith('مُحْىِ') or 'ۦ' not in original:  # Not the verb ending
                results['muhyi'].append({
                    'surah': surah, 'verse': verse, 'token': token
                })
                continue

    return results


def count_death_nouns(tokens):
    """
    Count DEATH nouns from root م-و-ت (Meem-Waw-Ta)

    Target counts from QAC:
    - مَوْت (mawt - death): 50
    - مَيِّت (mayyit - dead person): 38
    - مَيْتَة (maytat - carrion): 6
    - مَيْت (mayt - dead): 5
    - مَمَات (mamat - death/dying): 3
    - مَوْتَة (mawtat - death): 3
    TOTAL: 105

    Exclude:
    - All verbs (مَاتَ, أَمَاتَ, يُمِيتُ, يَمُوتُ, etc.)
    """
    results = {
        'mawt': [],     # مَوْت (death) - target 50
        'mayyit': [],   # مَيِّت (dead person) - target 38
        'maytat': [],   # مَيْتَة (carrion) - target 6
        'mayt': [],     # مَيْت (dead) - target 5
        'mamat': [],    # مَمَات (death/dying) - target 3
        'mawtat': [],   # مَوْتَة (death) - target 3
        'excluded': []  # Excluded verbs
    }

    for surah, verse, token in tokens:
        original = normalize_arabic(token)
        clean = remove_diacritics(original)

        # ============================================
        # EXCLUSIONS - Verbs
        # ============================================

        # Form I verbs: مَاتَ, يَمُوتُ, تَمُوتُ, نَمُوتُ, مَاتُوا, مُتْ
        # Be careful NOT to exclude مَمَات nouns which contain مَاتُ substring
        if 'مَاتَ' in original and 'مَمَات' not in original:
            continue
        if 'مَاتُو' in original:  # مَاتُوا (they died) - more specific than مَاتُ
            continue
        if 'يَمُوتُ' in original or 'تَمُوتُ' in original or 'نَمُوتُ' in original:
            continue
        if 'يَمُوت' in original or 'تَمُوت' in original or 'نَمُوت' in original:
            continue
        if 'مُتْ' in original and 'مُتِّع' not in original:  # مُتْ is imperative "die!"
            continue
        if 'فَمُتْ' in original or 'وَمُتْ' in original:
            continue

        # Form IV verbs: أَمَاتَ, يُمِيتُ, نُمِيتُ, تُمِيتُ
        if 'أَمَاتَ' in original or 'فَأَمَاتَ' in original:
            continue
        if 'يُمِيتُ' in original or 'نُمِيتُ' in original or 'تُمِيتُ' in original:
            continue
        if 'يُمِيت' in original or 'نُمِيت' in original or 'تُمِيت' in original:
            continue

        # Form IV active participle as verb usage: مُمِيت
        if 'مُمِيت' in original:
            continue

        # ============================================
        # NOUN FORMS TO COUNT
        # ============================================

        # EXCLUDE: رَمَيْتَ (you threw) - different root ر-م-ي
        if 'رَمَيْت' in original:
            continue

        # 1. مَوْتَة (death - feminine) - target 3 (37:59, 44:35, 44:56)
        # Forms: مَوْتَتَنَا, مَوْتَتُنَا, ٱلْمَوْتَةَ
        if 'مَوْتَة' in original or 'مَوْتَت' in original:
            results['mawtat'].append({
                'surah': surah, 'verse': verse, 'token': token
            })
            continue

        # 2. مَمَات (death/dying) - target 3 (6:162, 17:75, 45:21)
        # Forms: وَمَمَاتِى, ٱلْمَمَاتِ, وَمَمَاتُهُمْ
        if 'مَمَات' in original or 'ٱلْمَمَات' in original:
            results['mamat'].append({
                'surah': surah, 'verse': verse, 'token': token
            })
            continue

        # 3. مَيْتَة (carrion/dead animal) - target 6
        # Forms: ٱلْمَيْتَةَ, ٱلْمَيْتَةُ, مَيْتَةً, مَّيْتَةً
        if 'مَيْتَة' in original or 'ٱلْمَيْتَة' in original or 'مَّيْتَة' in original:
            results['maytat'].append({
                'surah': surah, 'verse': verse, 'token': token
            })
            continue

        # 4. مَيِّت (dead person) - with shadda - target 38
        # Patterns: مَيِّت, ٱلْمَيِّت, مَّيِّت, لَمَيِّتُونَ, بِمَيِّت
        if 'مَيِّت' in original or 'مَّيِّت' in original or 'لَمَيِّت' in original or 'بِمَيِّت' in original:
            results['mayyit'].append({
                'surah': surah, 'verse': verse, 'token': token
            })
            continue
        # Plural forms: أَمْوَٰت, مَوْتَىٰ (dead ones)
        if 'أَمْوَٰت' in original or 'وَأَمْوَٰت' in original:
            results['mayyit'].append({
                'surah': surah, 'verse': verse, 'token': token
            })
            continue
        if 'مَوْتَىٰ' in original or 'ٱلْمَوْتَىٰ' in original:
            results['mayyit'].append({
                'surah': surah, 'verse': verse, 'token': token
            })
            continue
        # Definite plural: ٱلْأَمْوَٰتُ
        if 'ٱلْأَمْوَٰت' in original:
            results['mayyit'].append({
                'surah': surah, 'verse': verse, 'token': token
            })
            continue

        # 5. مَيْت (dead - without shadda) - target 5
        # Forms: مَيْتًا, مَّيْتًا (accusative indefinite)
        # QAC verses: 6:122, 25:49, 43:11, 49:12, 50:11
        if 'مَيْتً' in original or 'مَّيْتً' in original:
            results['mayt'].append({
                'surah': surah, 'verse': verse, 'token': token
            })
            continue

        # 6. مَوْت (death - main word) - target 50
        # Patterns: ٱلْمَوْتَ, ٱلْمَوْتِ, ٱلْمَوْتُ, مَوْتِهِ, مَوْتًا
        if 'ٱلْمَوْتَ' in original or 'ٱلْمَوْتِ' in original or 'ٱلْمَوْتُ' in original:
            results['mawt'].append({
                'surah': surah, 'verse': verse, 'token': token
            })
            continue
        if 'ٱلْمَوْت' in original:  # Catch remaining definite forms
            results['mawt'].append({
                'surah': surah, 'verse': verse, 'token': token
            })
            continue
        # Indefinite with case endings
        if 'مَوْتًا' in original:
            results['mawt'].append({
                'surah': surah, 'verse': verse, 'token': token
            })
            continue
        # Possessive forms
        if 'مَوْتِهِ' in original or 'مَوْتِهِمْ' in original or 'مَوْتِكُم' in original:
            results['mawt'].append({
                'surah': surah, 'verse': verse, 'token': token
            })
            continue
        # With prepositions: بِمَوْت, فَمَوْت
        if 'بِمَوْت' in original or 'فَمَوْت' in original:
            results['mawt'].append({
                'surah': surah, 'verse': verse, 'token': token
            })
            continue
        # Construct form: مَوْتِ
        if 'مَوْتِ' in original and 'ٱلْمَوْت' not in original:
            # Avoid already counted patterns
            if 'مَوْتِهِ' not in original and 'مَوْتِهِمْ' not in original:
                results['mawt'].append({
                    'surah': surah, 'verse': verse, 'token': token
                })
                continue

    return results


def main():
    print("=" * 70)
    print("LIFE vs DEATH - 105:105 Balance Verification")
    print("=" * 70)
    print()

    print("Loading Quran text...")
    verses, tokens = load_quran()
    print(f"Loaded {len(verses)} verses, {len(tokens)} tokens")
    print()

    print("Methodology: Count NOUNS ONLY (excluding verbs)")
    print("Source: Quranic Arabic Corpus (corpus.quran.com)")
    print()

    # Count Life nouns
    print("-" * 70)
    print("LIFE ROOT (ح-ي-ي) - Noun Forms")
    print("-" * 70)

    life = count_life_nouns(tokens)

    life_counts = {
        'حَىّ (alive/living)': len(life['hayy']),
        'حَيَوٰة (life)': len(life['hayat']),
        'حَيَوَان (creature)': len(life['hayawan']),
        'مَحْيَا (living)': len(life['mahya']),
        'مُحْىِ (giver of life)': len(life['muhyi']),
    }

    qac_life = {
        'حَىّ (alive/living)': 24,
        'حَيَوٰة (life)': 76,
        'حَيَوَان (creature)': 1,
        'مَحْيَا (living)': 2,
        'مُحْىِ (giver of life)': 2,
    }

    for form, count in life_counts.items():
        qac = qac_life.get(form, '?')
        status = "✓" if count == qac else f"(QAC: {qac})"
        print(f"  {form:<25} {count:>3} {status}")

    life_total = sum(life_counts.values())
    print("  " + "-" * 40)
    print(f"  {'TOTAL:':<25} {life_total:>3} (target: 105)")
    print()

    # Show exclusions
    if life['excluded']:
        print(f"  Excluded forms: {len(life['excluded'])}")
        for ex in life['excluded']:
            print(f"    {ex['surah']}:{ex['verse']} - {ex['token']} ({ex['reason']})")
    print()

    # Count Death nouns
    print("-" * 70)
    print("DEATH ROOT (م-و-ت) - Noun Forms")
    print("-" * 70)

    death = count_death_nouns(tokens)

    death_counts = {
        'مَوْت (death)': len(death['mawt']),
        'مَيِّت (dead person)': len(death['mayyit']),
        'مَيْتَة (carrion)': len(death['maytat']),
        'مَيْت (dead)': len(death['mayt']),
        'مَمَات (death/dying)': len(death['mamat']),
        'مَوْتَة (death)': len(death['mawtat']),
    }

    qac_death = {
        'مَوْت (death)': 50,
        'مَيِّت (dead person)': 38,
        'مَيْتَة (carrion)': 6,
        'مَيْت (dead)': 5,
        'مَمَات (death/dying)': 3,
        'مَوْتَة (death)': 3,
    }

    for form, count in death_counts.items():
        qac = qac_death.get(form, '?')
        status = "✓" if count == qac else f"(QAC: {qac})"
        print(f"  {form:<25} {count:>3} {status}")

    death_total = sum(death_counts.values())
    print("  " + "-" * 40)
    print(f"  {'TOTAL:':<25} {death_total:>3} (target: 105)")
    print()

    # Final result
    print("=" * 70)
    print("FINAL RESULT")
    print("=" * 70)
    print()
    print(f"  Life nouns:   {life_total:>3}")
    print(f"  Death nouns:  {death_total:>3}")
    print(f"  QAC Target:   105:105")
    print()

    # Check if matches
    if life_total == 105 and death_total == 105:
        print("  ✓ PERFECT 105:105 BALANCE VERIFIED!")
        print()
        print("  Both script counts match QAC exactly.")
    elif life_total == death_total:
        print(f"  ✓ BALANCED: {life_total}:{death_total}")
        print()
        print("  Note: Counts differ from QAC targets.")
    else:
        print(f"  Pattern found: {life_total}:{death_total}")
        print()
        print("  Debugging info below:")

    # Debug: Show sample matches
    print()
    print("-" * 70)
    print("SAMPLE MATCHES")
    print("-" * 70)

    print("\nLife - حَىّ (first 5):")
    for m in life['hayy'][:5]:
        print(f"  {m['surah']}:{m['verse']} {m['token']}")

    print(f"\nLife - حَيَوٰة (first 10 of {len(life['hayat'])}):")
    for m in life['hayat'][:10]:
        print(f"  {m['surah']}:{m['verse']} {m['token']}")

    print(f"\nDeath - مَوْت (first 10 of {len(death['mawt'])}):")
    for m in death['mawt'][:10]:
        print(f"  {m['surah']}:{m['verse']} {m['token']}")

    print(f"\nDeath - مَيِّت (first 10 of {len(death['mayyit'])}):")
    for m in death['mayyit'][:10]:
        print(f"  {m['surah']}:{m['verse']} {m['token']}")

    print()
    print("-" * 70)
    print("QAC VERIFICATION LINKS")
    print("-" * 70)
    print("Life root: https://corpus.quran.com/qurandictionary.jsp?q=Hyy")
    print("Death root: https://corpus.quran.com/qurandictionary.jsp?q=mwt")

    return life_total == death_total


if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
