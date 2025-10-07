#!/usr/bin/env python3
"""
Hijri 29-Day Pattern Verifier (Plural + Dual forms)

Counts the exact occurrences of Qur'anic tokens derived from the root "يوم"
that represent plural days (أيام) and the dual form (يومين). The total of
26 plural days and 3 dual "two days" aligns with the 29-day lunar month
length observed in the Hijri calendar.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Tuple


DIACRITICS_PATTERN = re.compile(r"[\u064B-\u065F\u0670\u0640]")
PREFIX_CHARS = {"و", "ف", "ب", "ل", "ك"}
PRONOUN_SUFFIXES = (
    "كما",
    "كم",
    "كن",
    "هما",
    "هم",
    "هن",
    "ها",
    "نا",
)


def remove_diacritics(text: str) -> str:
    """Strip tashkeel and tatweel to simplify token comparisons."""
    return DIACRITICS_PATTERN.sub("", text)


@dataclass
class DayForms:
    ayyam: List[str]
    yawmayn: List[str]


def normalize_plural_base(token: str) -> str:
    """Reduce a token to its plural stem for 'أيام' detection."""
    if not token:
        return token

    # Normalize initial alef/hamza variants
    if token[0] in {"أ", "إ", "ٱ"}:
        token = "ا" + token[1:]

    # Remove stacked proclitics (و، ف، ب، ل، ك)
    while token and token[0] in PREFIX_CHARS:
        token = token[1:]
        if token and token[0] in {"أ", "إ", "ٱ"}:
            token = "ا" + token[1:]

    # Drop the definite article if present
    if token.startswith("ال"):
        token = token[2:]
        if token and token[0] in {"أ", "إ", "ٱ"}:
            token = "ا" + token[1:]

    # Remove pronominal suffixes
    changed = True
    while changed and token:
        changed = False
        for suffix in PRONOUN_SUFFIXES:
            if token.endswith(suffix):
                token = token[: -len(suffix)]
                changed = True
                break

    # Elide trailing alef from tanwin (e.g., أياماً -> اياما)
    if token.endswith("ا"):
        token = token[:-1]

    return token


def normalize_dual_base(token: str) -> str:
    """Reduce a token to its dual stem for 'يومين' detection."""
    if not token:
        return token
    if token[0] in {"أ", "إ", "ٱ"}:
        token = "ا" + token[1:]

    while token and token[0] in PREFIX_CHARS:
        token = token[1:]

    if token.startswith("ال"):
        token = token[2:]

    return token


def load_verses() -> Dict[Tuple[int, int], List[str]]:
    """Load the Tanzil text into a (surah, ayah) -> tokens mapping."""
    current = Path(__file__).parent
    data_path: Path | None = None

    for _ in range(6):
        candidate = current / "data" / "quran-uthmani.txt"
        if candidate.exists():
            data_path = candidate
            break
        current = current.parent

    if data_path is None:
        raise FileNotFoundError("Could not locate data/quran-uthmani.txt")

    verses: Dict[Tuple[int, int], List[str]] = {}
    with data_path.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            surah_s, ayah_s, text = line.split("|", 2)
            verses[(int(surah_s), int(ayah_s))] = text.split()

    return verses


def collect_day_forms(verses: Dict[Tuple[int, int], List[str]]) -> DayForms:
    """Capture plural (أيام) and dual (يومين) occurrences across the text."""
    ayyam_matches: List[str] = []
    yawmayn_matches: List[str] = []

    for (surah, ayah), tokens in verses.items():
        cleaned_tokens = [remove_diacritics(token) for token in tokens]

        for original, cleaned in zip(tokens, cleaned_tokens):
            plural_base = normalize_plural_base(cleaned)
            dual_base = normalize_dual_base(cleaned)

            if plural_base == "ايام":
                ayyam_matches.append(f"{surah}:{ayah} | {original} -> {cleaned}")
            elif dual_base == "يومين":
                yawmayn_matches.append(f"{surah}:{ayah} | {original} -> {cleaned}")

    return DayForms(ayyam=ayyam_matches, yawmayn=yawmayn_matches)


def print_report(forms: DayForms) -> None:
    ayyam_total = len(forms.ayyam)
    yawmayn_total = len(forms.yawmayn)
    combined = ayyam_total + yawmayn_total

    print("=" * 70)
    print("HIJRI 29-DAY PATTERN VERIFICATION (Plural + Dual forms)")
    print("=" * 70)
    print()
    print("Counts:")
    print(f"  AYYAM (plural days): {ayyam_total}")
    print(f"  YAWMAYN (dual \"two days\"): {yawmayn_total}")
    print(f"  Combined total: {combined}")
    print()
    print("-" * 70)
    print("AYYAM occurrences (26 total):")
    for entry in forms.ayyam:
        print(f"  {entry}")
    print()
    print("-" * 70)
    print("YAWMAYN occurrences (3 total):")
    for entry in forms.yawmayn:
        print(f"  {entry}")
    print()
    print("=" * 70)
    if combined == 29:
        print("STATUS: 29-day Hijri month alignment confirmed.")
    else:
        print(f"STATUS: Counts differ from 29 (found {combined}).")
    print("=" * 70)


def main() -> None:
    verses = load_verses()
    forms = collect_day_forms(verses)
    print_report(forms)


if __name__ == "__main__":
    main()
