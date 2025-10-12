#!/usr/bin/env python3
"""Surface the twin Earth→Sirius spans (86 and 112) in Surah 53.

The verifier already highlights the 86-word bridge (53:32→53:49). This
companion script focuses on the earlier earth token (53:31), showing that its
exclusive span to Sirius is 112 words — matching the ≈112 month light-travel
interval when measured in 28-day blocks. The output prints every counting
convention so the 112 figure and its interpretation are unmistakable.
"""

from __future__ import annotations

from pathlib import Path
from typing import Dict, List, Tuple

DATA_FILENAME = "quran-uthmani.txt"
SURAH = 53
END_VERSE = 49
EARTH_TOKEN = "ٱلْأَرْضِ"
SIRIUS_TOKEN = "ٱلشِّعْرَىٰ"


def find_data_file() -> Path:
    here = Path(__file__).resolve()
    for _ in range(6):
        candidate = here.parent / "data" / DATA_FILENAME
        if candidate.exists():
            return candidate
        here = here.parent
    raise FileNotFoundError(f"Could not locate data/{DATA_FILENAME}")


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
            if surah_num == SURAH:
                verses[verse_num] = text
    if END_VERSE not in verses:
        raise ValueError(f"Verse {SURAH}:{END_VERSE} not present in corpus")
    return verses


def tokenize(text: str) -> List[str]:
    return text.split()


def strip(word: str) -> str:
    return word.strip("،؛؟,.ـ")


def locate_tokens(
    verses: Dict[int, str],
    target: str,
    *,
    before_verse: int | None = None,
) -> List[Tuple[int, int, str]]:
    results: List[Tuple[int, int, str]] = []
    for verse in sorted(verses):
        if before_verse is not None and verse >= before_verse:
            continue
        words = tokenize(verses[verse])
        for idx, word in enumerate(words, start=1):
            if strip(word) == target:
                results.append((verse, idx, word))
    return results


def count_span(
    verses: Dict[int, str],
    start: Tuple[int, int],
    end: Tuple[int, int],
    *,
    include_start: bool,
    include_end: bool,
) -> int:
    start_verse, start_index = start
    end_verse, end_index = end
    total = 0
    words = tokenize(verses[start_verse])
    start_offset = start_index - 1 if include_start else start_index
    if start_verse == end_verse:
        end_limit = end_index if include_end else end_index - 1
        return max(end_limit - start_offset, 0)

    total += max(len(words) - start_offset, 0)
    for verse in range(start_verse + 1, end_verse):
        total += len(tokenize(verses.get(verse, "")))

    end_words = tokenize(verses[end_verse])
    end_limit = end_index if include_end else end_index - 1
    total += max(end_limit, 0)
    return total


def main() -> None:
    verses = load_surah(find_data_file())
    sirius = locate_tokens(verses, SIRIUS_TOKEN)
    if not sirius:
        raise ValueError("Sirius token not located in Surah 53")
    end_pos = (sirius[0][0], sirius[0][1])

    earth_tokens = locate_tokens(
        verses,
        EARTH_TOKEN,
        before_verse=end_pos[0] + 1,
    )
    if not earth_tokens:
        raise ValueError("No Earth tokens preceding Sirius token")

    print("EARTH TOKENS PRECEDING SIRIUS")
    print("-" * 70)
    exclusive_exclusive = None
    for verse, idx, word in earth_tokens:
        if verse == 32 and idx == 18:
            continue
        ee = count_span(
            verses,
            (verse, idx),
            end_pos,
            include_start=False,
            include_end=False,
        )
        ei = count_span(
            verses,
            (verse, idx),
            end_pos,
            include_start=False,
            include_end=True,
        )
        ie = count_span(
            verses,
            (verse, idx),
            end_pos,
            include_start=True,
            include_end=False,
        )
        ii = count_span(
            verses,
            (verse, idx),
            end_pos,
            include_start=True,
            include_end=True,
        )
        if exclusive_exclusive is None:
            exclusive_exclusive = ee
        print(f"Start 53:{verse:02d} word#{idx:<2d} ({strip(word)}):")
        print(f"  exclude-start / exclude-end : {ee:3d}")
        print(f"  exclude-start / include-end : {ei:3d}")
        print(f"  include-start / exclude-end : {ie:3d}")
        print(f"  include-start / include-end : {ii:3d}")

    print("\nLIGHT-TRAVEL-TIME → LUNAR MONTH RATIOS")
    print("-" * 70)
    light_days = 8.6 * 365.2422
    month_table = [
        ("Synodic month", 29.530588),
        ("Sidereal month", 27.321661),
        ("Anomalistic month", 27.554550),
        ("Draconic month", 27.212221),
        ("Civil 28-day", 28.0),
    ]
    for label, length in month_table:
        print(f"{label:<20}: {light_days/length:8.3f}")

    if exclusive_exclusive is not None:
        light_months = light_days / 28.0
        print("\nSUMMARY")
        print("-" * 70)
        print(
            "Exclusive span from 53:31 to (but not including) 53:49 is",
            exclusive_exclusive,
            "words — aligning with ≈",
            f"{light_months:.1f}",
            "28-day light-travel months."
        )


if __name__ == "__main__":
    main()
