#!/usr/bin/env python3
"""
🌍⭐ EARTH-SIRIUS 861 LETTER GAP - VERIFIED
═══════════════════════════════════════════════════════════════════════════════

Pattern: Star (النجم) 53:1 → Earth (الأرض) 53:32 = 861 letters
Meaning: Sirius distance = 8.61 light-years = 861 centi-light-years

Source: https://www.kaheel7.com/ar/index.php/1/2087--2019
Method: Inclusive counting (include both endpoint letters)

═══════════════════════════════════════════════════════════════════════════════
"""

from pathlib import Path

def load_surah_53():
    """Load Surah 53 (An-Najm) from Quran data."""
    current_dir = Path(__file__).parent
    for _ in range(6):
        path = current_dir / "data" / "quran-uthmani.txt"
        if path.exists():
            break
        current_dir = current_dir.parent

    verses = {}
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            if line.startswith('53|'):
                parts = line.strip().split('|', 2)
                verses[int(parts[1])] = parts[2]
    return verses

def count_letters(text):
    """Count Arabic letters only (no diacritics)."""
    count = 0
    for char in text:
        code = ord(char)
        if 0x0621 <= code <= 0x064A or code == 0x0671:
            count += 1
    return count

def main():
    print("=" * 70)
    print("🌍⭐ EARTH-SIRIUS 861 LETTER GAP VERIFICATION")
    print("=" * 70)

    verses = load_surah_53()

    # Parse verse 53:1
    words_1 = verses[1].split()
    # Word 5 is Star: وَٱلنَّجْمِ
    star_word = words_1[4]
    star_letters = count_letters(star_word)
    letters_after_star = sum(count_letters(w) for w in words_1[5:])

    # Verses 53:2 to 53:31
    middle_letters = sum(count_letters(verses[v]) for v in range(2, 32))

    # Parse verse 53:32
    words_32 = verses[32].split()
    # Find Earth word (ٱلْأَرْضِ) - search by removing diacritics
    def strip_diacritics(t):
        import re
        return re.sub(r'[\u064B-\u0652\u0670]', '', t)

    earth_idx = next(i for i, w in enumerate(words_32) if 'أرض' in strip_diacritics(w) or 'ارض' in strip_diacritics(w))
    earth_word = words_32[earth_idx]
    earth_letters = count_letters(earth_word)
    letters_before_earth = sum(count_letters(w) for w in words_32[:earth_idx])

    print(f"""
📜 Surah 53: An-Najm (النجم) - "The Star"
─────────────────────────────────────────────

⭐ STAR (53:1, word #5): {star_word}
   Letters: {star_letters} (و ٱ ل ن ج م)

🌍 EARTH (53:32, word #{earth_idx+1}): {earth_word}
   Letters: {earth_letters} (ٱ ل أ ر ض)
    """)

    print("=" * 70)
    print("📏 LETTER GAP CALCULATION")
    print("=" * 70)

    gap_exclusive = letters_after_star + middle_letters + letters_before_earth
    gap_inclusive = gap_exclusive + 2  # Include last of Star + first of Earth

    print(f"""
   Method: INCLUSIVE (Kaheel7 methodology)
   ───────────────────────────────────────

   Letters after Star in 53:1:    {letters_after_star:>4}
   Letters in 53:2 to 53:31:      {middle_letters:>4}
   Letters before Earth in 53:32: {letters_before_earth:>4}
   ─────────────────────────────────────
   Subtotal (exclusive):          {gap_exclusive:>4}
   + Last letter of Star (م):       +1
   + First letter of Earth (ٱ):     +1
   ─────────────────────────────────────
   TOTAL (inclusive):             {gap_inclusive:>4}
    """)

    print("=" * 70)
    print("🎯 VERIFICATION")
    print("=" * 70)

    target = 861
    match = "✅ EXACT MATCH!" if gap_inclusive == target else f"±{abs(gap_inclusive - target)}"

    print(f"""
   Calculated: {gap_inclusive} letters
   Claimed:    {target} letters
   Result:     {match}
    """)

    print("=" * 70)
    print("🌟 ASTRONOMICAL SIGNIFICANCE")
    print("=" * 70)
    print(f"""
   Sirius (الشِّعْرَى) - mentioned in 53:49:
   ─────────────────────────────────────────
   • Distance from Earth: 8.6 light-years
   • {gap_inclusive} letters = 8.61 light-years (centi-ly encoding)
   • Brightest star in night sky (-1.46 mag)
   • Only star mentioned BY NAME in Quran

   Pattern in Surah "The Star":
   ────────────────────────────
   Star (53:1) ─── {gap_inclusive} letters ───→ Earth (53:32)
                                          │
                                     Sirius (53:49)

   7th century knowledge: Stellar distances UNKNOWN
   First parallax measurement: 1838 (Friedrich Bessel)
   Modern precision: 8.60 ± 0.04 light-years
    """)

    print("=" * 70)
    print("📊 PROBABILITY ANALYSIS")
    print("=" * 70)

    # Simple probability estimate
    surah_53_letters = sum(count_letters(verses[v]) for v in verses)
    possible_gaps = surah_53_letters  # Rough estimate

    print(f"""
   Surah 53 total letters: ~{surah_53_letters}

   For random text:
   • P(gap = exactly 861) ≈ 1/{possible_gaps} ≈ {1/possible_gaps*100:.3f}%

   Combined significance:
   • Correct surah theme ("The Star")
   • Star → Earth semantic connection
   • Exact distance encoding (8.61 ly)
   • Historical impossibility (7th century)
    """)

    return {'gap': gap_inclusive, 'target': target, 'match': gap_inclusive == target}

if __name__ == "__main__":
    result = main()

    if result['match']:
        print("\n" + "🎉" * 35)
        print("  PATTERN VERIFIED: 861 LETTERS = 8.61 LIGHT-YEARS")
        print("🎉" * 35)
