#!/usr/bin/env python3
"""
Mean vs Long/Short Comparison
=============================
Source: Simetrik Kitap: Kur'an, page 327

Compares two different categorization methods:
1. Mean method: above/below average (54.70)
2. Long/Short method: above/below 39

REMARKABLE: Both methods produce IDENTICAL symmetry patterns!
- 96/96: Position matches for both
- 18/18: Position NOT matches for both
- 48/48: Matching + parity homo/hetero for both
- 9/9: NOT matching + parity homo/hetero for both
"""

from pathlib import Path

BOUNDARY = 39

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
    mean = sum(vc.values()) / 114

    print("=" * 60)
    print("MEAN vs LONG/SHORT COMPARISON")
    print("=" * 60)
    print(f"Mean: {mean:.2f}, Boundary: {BOUNDARY}")
    print()

    # Position matching for mean method
    mean_matching = [(s, v) for s, v in vc.items() if (s <= 57 and v > mean) or (s > 57 and v < mean)]
    mean_not_matching = [(s, v) for s, v in vc.items() if v != mean and not ((s <= 57 and v > mean) or (s > 57 and v < mean))]

    # Position matching for long/short method
    ls_matching = [(s, v) for s, v in vc.items() if (s <= 57 and v > BOUNDARY) or (s > 57 and v < BOUNDARY)]
    ls_not_matching = [(s, v) for s, v in vc.items() if v != BOUNDARY and not ((s <= 57 and v > BOUNDARY) or (s > 57 and v < BOUNDARY))]

    # Pattern 1: 96/96
    print(f"Mean method - position matches: {len(mean_matching)}")
    print(f"Long/Short method - position matches: {len(ls_matching)}")
    if len(mean_matching) == 96 and len(ls_matching) == 96:
        print("✓ VERIFIED: 96/96")
    print()

    # Pattern 2: 18/18
    print(f"Mean method - position NOT matches: {len(mean_not_matching)}")
    print(f"Long/Short method - position NOT matches: {len(ls_not_matching)}")
    if len(mean_not_matching) == 18 and len(ls_not_matching) == 18:
        print("✓ VERIFIED: 18/18")
    print()

    # Parity breakdowns
    mean_match_homo = len([x for x in mean_matching if x[0] % 2 == x[1] % 2])
    mean_match_hetero = len([x for x in mean_matching if x[0] % 2 != x[1] % 2])
    ls_match_homo = len([x for x in ls_matching if x[0] % 2 == x[1] % 2])
    ls_match_hetero = len([x for x in ls_matching if x[0] % 2 != x[1] % 2])

    # Pattern 3 & 4: 48/48
    print(f"Mean: matching parity: {mean_match_homo}/{mean_match_hetero}")
    if mean_match_homo == 48 and mean_match_hetero == 48:
        print("✓ VERIFIED: 48/48 (mean)")
    print(f"Long/Short: matching parity: {ls_match_homo}/{ls_match_hetero}")
    if ls_match_homo == 48 and ls_match_hetero == 48:
        print("✓ VERIFIED: 48/48 (L/S)")
    print()

    mean_not_match_homo = len([x for x in mean_not_matching if x[0] % 2 == x[1] % 2])
    mean_not_match_hetero = len([x for x in mean_not_matching if x[0] % 2 != x[1] % 2])
    ls_not_match_homo = len([x for x in ls_not_matching if x[0] % 2 == x[1] % 2])
    ls_not_match_hetero = len([x for x in ls_not_matching if x[0] % 2 != x[1] % 2])

    # Pattern 5 & 6: 9/9
    print(f"Mean: NOT matching parity: {mean_not_match_homo}/{mean_not_match_hetero}")
    if mean_not_match_homo == 9 and mean_not_match_hetero == 9:
        print("✓ VERIFIED: 9/9 (mean)")
    print(f"Long/Short: NOT matching parity: {ls_not_match_homo}/{ls_not_match_hetero}")
    if ls_not_match_homo == 9 and ls_not_match_hetero == 9:
        print("✓ VERIFIED: 9/9 (L/S)")

    return {
        'mean_matching': len(mean_matching),
        'ls_matching': len(ls_matching),
        'mean_not_matching': len(mean_not_matching),
        'ls_not_matching': len(ls_not_matching)
    }

if __name__ == "__main__":
    verify()
