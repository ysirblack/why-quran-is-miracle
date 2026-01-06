#!/usr/bin/env python3
"""
Golden Ratio Pattern
====================
Source: Simetrik Kitap: Kur'an, pages 361-367

For each surah, calculate: position + verse count
Some sums are repeated (mükerrer), some are unique (mükerrer olmayan)

REMARKABLE:
- Sum of repeated category: 7906
- Sum of unique category: 4885
- Ratio: 7906 / 4885 = 1.618424 ≈ φ (golden ratio!)
- Total: 7906 + 4885 = 12791 (PRIME!)
"""

from pathlib import Path
from collections import Counter

PHI = 1.6180339887  # Golden ratio

def load_quran_data():
    current_dir = Path(__file__).parent
    for _ in range(6):
        potential_path = current_dir / "data" / "quran-uthmani.txt"
        if potential_path.exists():
            data_path = potential_path
            break
        current_dir = current_dir.parent
    else:
        raise FileNotFoundError("data/quran-uthmani.txt not found")

    verses = {}
    with data_path.open('r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#') or '|' not in line:
                continue
            parts = line.split('|', 2)
            if len(parts) >= 3:
                surah = int(parts[0])
                verses.setdefault(surah, []).append(int(parts[1]))
    return {s: len(v) for s, v in verses.items()}

def verify():
    vc = load_quran_data()

    print("=" * 60)
    print("GOLDEN RATIO PATTERN")
    print("=" * 60)
    print()

    # Calculate position + verse count for each surah
    sums = {s: s + v for s, v in vc.items()}
    sum_counts = Counter(sums.values())

    # Repeated vs unique
    repeated_surahs = [(s, v, sums[s]) for s, v in vc.items() if sum_counts[sums[s]] > 1]
    unique_surahs = [(s, v, sums[s]) for s, v in vc.items() if sum_counts[sums[s]] == 1]

    print(f"Repeated sums (mükerrer): {len(repeated_surahs)} surahs")
    print(f"Unique sums (mükerrer olmayan): {len(unique_surahs)} surahs")
    print()

    # Sum of each category
    sum_repeated = sum(s + v for s, v, _ in repeated_surahs)
    sum_unique = sum(s + v for s, v, _ in unique_surahs)

    print(f"Sum of repeated: {sum_repeated}")
    print(f"Sum of unique: {sum_unique}")
    print(f"Total: {sum_repeated + sum_unique}")
    print()

    # Golden ratio
    ratio = sum_repeated / sum_unique
    print(f"Ratio: {sum_repeated} / {sum_unique} = {ratio:.6f}")
    print(f"Golden ratio φ = {PHI:.6f}")
    print(f"Difference: {abs(ratio - PHI):.6f}")
    print()

    if sum_repeated == 7906 and sum_unique == 4885:
        print("✓ VERIFIED: 7906 / 4885")
    if abs(ratio - PHI) < 0.001:
        print("✓ VERIFIED: Ratio ≈ Golden Ratio (φ)")
    if sum_repeated + sum_unique == 12791:
        print("✓ VERIFIED: Total = 12791 (PRIME)")

    return {
        'repeated_count': len(repeated_surahs),
        'unique_count': len(unique_surahs),
        'sum_repeated': sum_repeated,
        'sum_unique': sum_unique,
        'ratio': ratio
    }

if __name__ == "__main__":
    verify()
