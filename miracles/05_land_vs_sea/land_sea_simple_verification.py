#!/usr/bin/env python3
"""Verify the land vs sea token ratio directly from the Tanzil corpus.

This replaces the earlier hard-coded lists with a deterministic tokenizer that
scans ``data/quran-uthmani.txt``. The filters implement the documented rules:

* Sea tokens: definite singular ``ٱلْبَحْرُ/ٱلْبَحْرَ/ٱلْبَحْرِ`` only.
* Land tokens: definite singular ``ٱلْبَرُّ/ٱلْبَرَّ/ٱلْبَرِّ`` used in the
  geographic sense (fatha on ب, shadda+kasra on ر). Moral forms ``ٱلْبِرّ`` and
  the divine name in 52:28 are excluded.
* Optional dry-land token: ``يَبَسًا`` in 20:77.

For transparency the script prints every matched token (surah:ayah, surface
form, full verse text). The expectation is to see 32 sea tokens across
31 verses, 12 land tokens, and the optional dry-land token.
"""

from __future__ import annotations

import re
import platform
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple


# Arabic diacritics present in the Uthmani script (Ḥafṣ).
ARABIC_DIACRITICS: Sequence[str] = tuple(
    chr(code)
    for code in list(range(0x0610, 0x061A + 1))
    + list(range(0x064B, 0x065F + 1))
    + list(range(0x06D6, 0x06ED + 1))
)

# Characters that behave as proclitics (وَ، فَ، بِـ, كَـ, لِـ, سَـ ...).
PREFIXES: Sequence[str] = ("و", "ف", "ب", "ك", "ل", "س")

# Regex to split verses into tokens while preserving Arabic letters/diacritics.
TOKEN_SPLIT_RE = re.compile(r"[\s\u060C\u061B\u061F،؛؟,:;.!?()\[\]{}]+")

# Base (diacritic-free) forms we expect to keep.
SEA_BASE_FORM = "ٱلبحر"
LAND_BASE_FORM = "ٱلبر"
DRY_LAND_BASE_FORM = "يبسا"

# Semantic exclusion: 52:28 uses ٱلْبَرُّ as a divine name, not geography.
SEMANTIC_LAND_EXCLUSIONS = {(52, 28)}

EARTH_TOTAL_SURFACE_KM2 = 510.1e6
# NASA/NOAA consensus figures: oceans/seas ≈361.3M km² (71.2%), land ≈148.9M km² (28.8%)
EARTH_WATER_PERCENTAGE = 71.2
EARTH_LAND_PERCENTAGE = 28.8

# Windows consoles (especially when logging) often choke on Arabic glyphs.
SUPPRESS_ARABIC_OUTPUT = platform.system().lower() == "windows"
ARABIC_PLACEHOLDER = "[Arabic suppressed on Windows]"


@dataclass(frozen=True)
class TokenMatch:
    """Concrete occurrence of a token classified as sea/land/dry-land."""

    surah: int
    verse: int
    surface: str  # surface form from the corpus
    core: str  # surface form after stripping proclitics

    @property
    def ref(self) -> str:
        return f"{self.surah}:{self.verse}"


@dataclass(frozen=True)
class ExcludedToken:
    """Token that was filtered out, along with the exclusion reason."""

    match: TokenMatch
    reason: str


@dataclass
class VerificationResult:
    """Container for classification results."""

    sea_tokens: List[TokenMatch]
    land_tokens: List[TokenMatch]
    excluded_land_tokens: List[ExcludedToken]
    dry_land_tokens: List[TokenMatch]

    def primary_counts(self) -> Tuple[int, int]:
        return len(self.sea_tokens), len(self.land_tokens)

    def enhanced_counts(self) -> Tuple[int, int]:
        sea_count, land_count = self.primary_counts()
        return sea_count, land_count + len(self.dry_land_tokens)

    def primary_percentages(self) -> Tuple[float, float]:
        return compute_percentages(*self.primary_counts())

    def enhanced_percentages(self) -> Tuple[float, float]:
        sea_count, land_count = self.enhanced_counts()
        return compute_percentages(sea_count, land_count)


def compute_percentages(sea_count: int, land_count: int) -> Tuple[float, float]:
    total = sea_count + land_count
    if total == 0:
        return 0.0, 0.0
    sea_pct = (sea_count / total) * 100.0
    land_pct = (land_count / total) * 100.0
    return sea_pct, land_pct


def find_data_file(start: Optional[Path] = None) -> Path:
    """Search upwards from *start* for ``data/quran-uthmani.txt``."""

    current = (start or Path(__file__).resolve()).parent
    for _ in range(6):
        candidate = current / "data" / "quran-uthmani.txt"
        if candidate.exists():
            return candidate
        current = current.parent
    raise FileNotFoundError("Could not locate data/quran-uthmani.txt")


def load_verses(data_path: Path) -> Dict[Tuple[int, int], str]:
    """Load the Tanzil corpus into a (surah, ayah) -> text mapping."""

    verses: Dict[Tuple[int, int], str] = {}
    with data_path.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split("|", 2)
            if len(parts) < 3:
                continue
            surah, ayah, text = int(parts[0]), int(parts[1]), parts[2]
            verses[(surah, ayah)] = text
    return verses


def iter_tokens(verse_text: str) -> Iterable[str]:
    """Yield whitespace/punctuation-delimited tokens from *verse_text*."""

    for token in TOKEN_SPLIT_RE.split(verse_text):
        if token:
            yield token


def strip_prefixes(token: str) -> str:
    """Remove proclitics (و, ف, ب, ك, ل, س) and their vowels from *token*."""

    index = 0
    length = len(token)
    # peel multiple prefixes (e.g., فَوَٱلْبَحْرِ)
    while index < length and token[index] in PREFIXES:
        index += 1
        while index < length and token[index] in ARABIC_DIACRITICS:
            index += 1
    # drop any diacritics immediately before the core word
    while index < length and token[index] in ARABIC_DIACRITICS:
        index += 1
    return token[index:]


def strip_diacritics(token: str) -> str:
    """Return *token* with Arabic diacritics removed."""

    return "".join(ch for ch in token if ch not in ARABIC_DIACRITICS)


def first_diacritic(token: str, start: int) -> Optional[str]:
    """Return the first diacritic in *token[start:]* (if any)."""

    for ch in token[start:]:
        if ch in ARABIC_DIACRITICS:
            return ch
        if not ch:
            break
    return None


def is_definite_singular_sea(core: str) -> bool:
    """True if *core* is one of the definite singular sea forms."""

    if not core.startswith("ٱل"):
        return False
    base = strip_diacritics(core)
    return base == SEA_BASE_FORM


def classify_land_form(core: str) -> Optional[str]:
    """Return ``None`` if *core* is the geographic land form, else a reason."""

    if not core.startswith("ٱل"):
        return "missing definite article"
    base = strip_diacritics(core)
    if base != LAND_BASE_FORM:
        return "different base form"
    try:
        ba_index = core.index("ب")
    except ValueError:
        return "missing ب"
    vowel_after_ba = first_diacritic(core, ba_index + 1)
    if vowel_after_ba != "\u064e":  # fatha
        return "moral sense (ٱلْبِرّ)"
    try:
        ra_index = core.index("ر", ba_index)
    except ValueError:
        return "missing ر"
    remainder = core[ra_index + 1 :]
    has_shadda = "\u0651" in remainder
    has_kasra = "\u0650" in remainder
    if not has_shadda or not has_kasra:
        return "non-geographic inflection"
    return None


def collect_matches(verses: Dict[Tuple[int, int], str]) -> VerificationResult:
    """Scan *verses* and classify land/sea tokens."""

    sea_tokens: List[TokenMatch] = []
    land_tokens: List[TokenMatch] = []
    excluded_land: List[ExcludedToken] = []
    dry_land_tokens: List[TokenMatch] = []

    for (surah, ayah), text in verses.items():
        for token in iter_tokens(text):
            core = strip_prefixes(token)
            if not core:
                continue
            base = strip_diacritics(core)
            if is_definite_singular_sea(core):
                sea_tokens.append(TokenMatch(surah, ayah, token, core))
            land_reason = classify_land_form(core)
            if land_reason is None:
                match = TokenMatch(surah, ayah, token, core)
                if (surah, ayah) in SEMANTIC_LAND_EXCLUSIONS:
                    excluded_land.append(ExcludedToken(match, "divine name"))
                else:
                    land_tokens.append(match)
            elif base == LAND_BASE_FORM:
                match = TokenMatch(surah, ayah, token, core)
                excluded_land.append(ExcludedToken(match, land_reason))
            if base == DRY_LAND_BASE_FORM:
                dry_land_tokens.append(TokenMatch(surah, ayah, token, core))

    # Sort for stable presentation.
    sea_tokens.sort(key=lambda m: (m.surah, m.verse, m.surface))
    land_tokens.sort(key=lambda m: (m.surah, m.verse, m.surface))
    excluded_land.sort(key=lambda m: (m.match.surah, m.match.verse, m.match.surface))
    dry_land_tokens.sort(key=lambda m: (m.surah, m.verse, m.surface))

    return VerificationResult(sea_tokens, land_tokens, excluded_land, dry_land_tokens)


def print_summary(result: VerificationResult, verses: Dict[Tuple[int, int], str]) -> None:
    """Print headline statistics and token listings."""

    sea_count, land_count = result.primary_counts()
    sea_pct, land_pct = result.primary_percentages()
    enhanced_sea_count, enhanced_land_count = result.enhanced_counts()
    enhanced_sea_pct, enhanced_land_pct = result.enhanced_percentages()

    water_diff = abs(sea_pct - EARTH_WATER_PERCENTAGE)
    land_diff = abs(land_pct - EARTH_LAND_PERCENTAGE)
    enhanced_water_diff = abs(enhanced_sea_pct - EARTH_WATER_PERCENTAGE)
    enhanced_land_diff = abs(enhanced_land_pct - EARTH_LAND_PERCENTAGE)
    water_area_mkm2 = EARTH_TOTAL_SURFACE_KM2 * (EARTH_WATER_PERCENTAGE / 100) / 1e6
    land_area_mkm2 = EARTH_TOTAL_SURFACE_KM2 * (EARTH_LAND_PERCENTAGE / 100) / 1e6

    print("=" * 70)
    print("LAND VS SEA — MORPHOLOGICAL VERIFICATION")
    print("=" * 70)
    print("Corpus: data/quran-uthmani.txt (Tanzil Ḥafṣ/Uthmānī)")
    print("Rules: definite singular ٱلْبَحْرُ / ٱلْبَرُّ tokens only")
    if SUPPRESS_ARABIC_OUTPUT:
        print("Note: Arabic text suppressed on Windows environment to avoid logging issues.")
    print(
        "Reference (Earth): "
        f"{EARTH_WATER_PERCENTAGE:.1f}% water (~{water_area_mkm2:.1f}M km²), "
        f"{EARTH_LAND_PERCENTAGE:.1f}% land (~{land_area_mkm2:.1f}M km²)"
    )
    print("-" * 70)
    print("PRIMARY ANALYSIS (geographical land only):")
    print(f"  Sea tokens:   {sea_count:2d} ({sea_pct:.2f}%)")
    print(f"  Land tokens:  {land_count:2d} ({land_pct:.2f}%)")
    print(f"  Ratio:        {sea_pct:.2f} : {land_pct:.2f}")
    print(f"  Δ vs Earth:   water ±{water_diff:.2f}%, land ±{land_diff:.2f}%")
    print("-" * 70)
    enhanced_land_only = enhanced_land_count - land_count
    print("ENHANCED ANALYSIS (includes يَبَسًا dry-land pathway):")
    print(f"  Sea tokens:   {enhanced_sea_count:2d} ({enhanced_sea_pct:.2f}%)")
    print(
        f"  Land tokens:  {enhanced_land_count:2d} ({enhanced_land_pct:.2f}%)"
        f"  [primary land + {enhanced_land_only}]"
    )
    print(
        f"  Δ vs Earth:   water ±{enhanced_water_diff:.2f}%, "
        f"land ±{enhanced_land_diff:.2f}%"
    )

    if result.excluded_land_tokens:
        print("-" * 70)
        print("Semantic exclusions (non-geographical ٱلْبَرّ forms):")
        for excluded in result.excluded_land_tokens:
            match = excluded.match
            verse_text = verses.get((match.surah, match.verse), "")
            verse_out = (
                ARABIC_PLACEHOLDER if SUPPRESS_ARABIC_OUTPUT else verse_text
            )
            surface_out = (
                ARABIC_PLACEHOLDER if SUPPRESS_ARABIC_OUTPUT else match.surface
            )
            print(
                f"  {match.ref:<7} {surface_out:<12}"
                f" [{excluded.reason}] {verse_out}"
            )

    print("-" * 70)
    print("Sea tokens (definite singular ٱلْبَحْر):")
    for match in result.sea_tokens:
        verse_text = verses.get((match.surah, match.verse), "")
        verse_out = (
            ARABIC_PLACEHOLDER if SUPPRESS_ARABIC_OUTPUT else verse_text
        )
        surface_out = (
            ARABIC_PLACEHOLDER if SUPPRESS_ARABIC_OUTPUT else match.surface
        )
        print(f"  {match.ref:<7} {surface_out:<12} {verse_out}")

    print("-" * 70)
    print("Land tokens (definite singular ٱلْبَرّ in geographic sense):")
    for match in result.land_tokens:
        verse_text = verses.get((match.surah, match.verse), "")
        verse_out = (
            ARABIC_PLACEHOLDER if SUPPRESS_ARABIC_OUTPUT else verse_text
        )
        surface_out = (
            ARABIC_PLACEHOLDER if SUPPRESS_ARABIC_OUTPUT else match.surface
        )
        print(f"  {match.ref:<7} {surface_out:<12} {verse_out}")

    if result.dry_land_tokens:
        print("-" * 70)
        print("Dry-land semantic equivalents (יَبَسًا):")
        for match in result.dry_land_tokens:
            verse_text = verses.get((match.surah, match.verse), "")
            verse_out = (
                ARABIC_PLACEHOLDER if SUPPRESS_ARABIC_OUTPUT else verse_text
            )
            surface_out = (
                ARABIC_PLACEHOLDER if SUPPRESS_ARABIC_OUTPUT else match.surface
            )
            print(f"  {match.ref:<7} {surface_out:<12} {verse_out}")


def verify_land_sea(show_details: bool = True) -> VerificationResult:
    """Run the verification and optionally print a human-readable summary."""

    data_file = find_data_file()
    verses = load_verses(data_file)
    result = collect_matches(verses)
    if show_details:
        print_summary(result, verses)
    return result


if __name__ == "__main__":
    verify_land_sea(show_details=True)
