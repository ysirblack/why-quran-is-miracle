#!/usr/bin/env python3
"""Explore word-span counts around the Earth→Sirius alignment in Surah 53.

This utility complements ``earth_sirius_verification.py`` by showing how the
86-word total compares with other possible starting points.  It enumerates every
word boundary prior to the Sirius token (53:49 word #4), reports the resulting
span length, and highlights the two ``ٱلْأَرْضِ`` occurrences.  It also prints a
simple baseline probability (uniform 60–120 range → 1/61 ≈ 1.6%) so readers can
see exactly what “1 in ~61” means in code rather than prose.
"""

from __future__ import annotations

from collections import Counter
from pathlib import Path
from typing import Dict, List, Tuple


DATA_FILENAME = "quran-uthmani.txt"
START_TOKEN = "ٱلْأَرْضِ"
END_TOKEN = "ٱلشِّعْرَىٰ"
SURAH_NUMBER = 53
END_VERSE = 49


def find_data_file() -> Path:
    here = Path(__file__).resolve()
    for _ in range(6):
        candidate = here.parent / "data" / DATA_FILENAME
        if candidate.exists():
            return candidate
        here = here.parent
    raise FileNotFoundError(f"Could not locate data/{DATA_FILENAME}")


def tokenize(text: str) -> List[str]:
    return text.split()


def strip_punct(token: str) -> str:
    return token.strip("،؛؟,.ـ")


def load_surah(path: Path) -> Dict[int, str]:
    verses: Dict[int, str] = {}
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split("|", 2)
            if len(parts) < 3:
                continue
            surah_num, verse_num, text = int(parts[0]), int(parts[1]), parts[2]
            if surah_num == SURAH_NUMBER:
                verses[verse_num] = text
    if END_VERSE not in verses:
        raise ValueError(f"Verse {SURAH_NUMBER}:{END_VERSE} missing from corpus")
    return verses


def locate_tokens(
    verses: Dict[int, str],
    target: str,
) -> List[Tuple[int, int, str]]:
    results: List[Tuple[int, int, str]] = []
    for verse in sorted(verses):
        words = tokenize(verses[verse])
        for idx, word in enumerate(words, start=1):
            if strip_punct(word) == target:
                results.append((verse, idx, word))
    return results


def span_length(
    verses: Dict[int, str],
    start_verse: int,
    start_index: int,
    end_verse: int,
    end_index: int,
) -> int:
    if (start_verse, start_index) == (end_verse, end_index):
        return 1
    total = 0
    words = tokenize(verses[start_verse])
    if start_verse == end_verse:
        return max(end_index - start_index, 0)
    total += len(words) - start_index
    for verse in range(start_verse + 1, end_verse):
        total += len(tokenize(verses.get(verse, "")))
    total += end_index
    return total


def main() -> None:
    data_path = find_data_file()
    verses = load_surah(data_path)

    all_boundaries: List[Tuple[int, int]] = []
    for verse in range(1, END_VERSE + 1):
        words = tokenize(verses.get(verse, ""))
        for idx in range(1, len(words) + 1):
            if verse == END_VERSE and idx >= 4:
                break
            all_boundaries.append((verse, idx))

    end_positions = locate_tokens(verses, END_TOKEN)
    if not end_positions:
        raise ValueError(f"End token {END_TOKEN} not found in Surah {SURAH_NUMBER}")
    end_verse, end_word_index, end_word = end_positions[0]

    lengths = []
    earth_lengths = []
    earth_positions = locate_tokens(verses, START_TOKEN)
    for verse, idx in all_boundaries:
        length = span_length(verses, verse, idx, end_verse, end_word_index)
        lengths.append(length)
        if any(v == verse and i == idx for v, i, _ in earth_positions):
            earth_lengths.append((verse, idx, length))

    length_counter = Counter(lengths)
    min_len, max_len = min(lengths), max(lengths)
    observed_baseline = 1 / (max_len - min_len + 1)
    reference_min, reference_max = 60, 120
    reference_range = reference_max - reference_min + 1
    reference_prob = 1 / reference_range

    print("EARTH → SIRIUS SPAN DISTRIBUTION (SURAH 53)")
    print("-" * 70)
    print(f"Total starting boundaries checked: {len(all_boundaries)}")
    print(f"Span lengths observed: {len(length_counter)} (range {min_len}–{max_len})")
    print(
        f"Uniform probability across observed range: {observed_baseline:.5f}"
        f" (≈ {observed_baseline*100:.2f}%)"
    )
    print(
        f"Reference uniform probability for 60–120 range: {reference_prob:.4f}"
        f" (≈ {reference_prob*100:.2f}%)"
    )
    print("\nEARTH TOKEN SPANS:")
    for verse, idx, length in earth_lengths:
        highlight = "<-- nearest Earth token" if verse == 32 else ""
        print(f"  Start 53:{verse:02d} word#{idx:<2d} → length {length:3d} {highlight}")

    target = 86
    print("\nSUMMARY FOR LENGTH 86:")
    print(f"  Occurrences among all boundaries: {length_counter[target]} (out of {len(all_boundaries)})")
    print(f"  Position(s) yielding 86: {[b for b in all_boundaries if span_length(verses, b[0], b[1], end_verse, end_word_index)==target]}")

    print("\nSELECTED NEARBY LENGTHS:")
    for candidate in range(target - 3, target + 4):
        print(
            f"  {candidate:3d}: count={length_counter.get(candidate, 0):3d}"
        )


if __name__ == "__main__":
    main()
