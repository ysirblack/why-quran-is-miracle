#!/usr/bin/env python3
"""
Combined probability exploration for the Yearly Cycles project.

This script computes simple combinatorial probabilities for the solar (365-day), Hijri
(354-day), lunar month (29-day plural+dual forms), and calendar month (12 mentions of
شهر) patterns under a transparent – but highly simplified – null model:

    • Start with all 405 Quranic tokens containing the root "يوم".
    • Pick a subset uniformly at random.
    • Ask for the probability that the chosen subset matches the pattern exactly.

Because the actual filters select *all* tokens in their category (and exclude the rest),
only one subset of the appropriate size is “successful”. We therefore compute:

    P(solar pattern) = 1 / C(405, 365)
    P(hijri pattern) = 1 / C(405, 354)
    P(lunar 29-day pattern) = 1 / C(405, 29)
    P(months 12 pattern) = 1 / C(total_شهر_tokens, 12)

For convenience we also report the (independent) product of these probabilities and the
approximate “1 in X” figures using base‑10 logarithms.

⚠️  Important: This null model treats every subset of a given size as equally likely. Real
    linguistic processes are obviously not uniform random draws, so the numbers below are
    best viewed as illustrative lower bounds rather than definitive statistical claims.
"""

from __future__ import annotations

import math
from pathlib import Path

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
from typing import Dict, List, Tuple

# --- Basic helpers ---------------------------------------------------------

def remove_diacritics(text: str) -> str:
    """Strip Arabic tashkeel and tatweel characters for simple pattern checks."""
    return "".join(
        ch for ch in text
        if not ("\u064B" <= ch <= "\u065F" or ch == "\u0670" or ch == "\u0640")
    )


def load_day_tokens() -> List[str]:
    """
    Return a list of all tokens containing the substring 'يوم' from the Tanzil text.
    """
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

    tokens: List[str] = []
    with data_path.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            _, _, text = line.split("|", 2)
            for token in text.split():
                clean = remove_diacritics(token)
                if "يوم" in clean:
                    tokens.append(clean)
    return tokens


def categorise_tokens(tokens: List[str]) -> Dict[str, List[str]]:
    """
    Split tokens into the categories used by the solar and Hijri filters.
    """
    categories = {
        "solar_simple": [],
        "solar_definite": [],
        "solar_tanwin": [],
        "day_plural": [],
        "day_dual": [],
        "hijri_that_day": [],
        "hijri_their_day": [],
        "hijri_your_day": [],
        "excluded": [],
    }

    for token in tokens:
        normalized = (
            token.replace("أ", "ا")
            .replace("إ", "ا")
            .replace("ٱ", "ا")
            .replace("آ", "ا")
        )

        if token == "يوما":
            categories["solar_tanwin"].append(token)
        elif "يومين" in normalized:
            categories["day_dual"].append(token)
        elif "ايام" in normalized:
            categories["day_plural"].append(token)
        elif any(al in token for al in ("اليوم", "الْيوم", "ٱلْيوم", "ٱليوم")):
            categories["solar_definite"].append(token)
        elif token == "يوم" or (
            len(token) <= 5
            and not any(ex in token for ex in ("يومهم", "يومكم", "يومئذ"))
            and "يوم" in token
        ):
            categories["solar_simple"].append(token)
        elif "يومئذ" in token:
            categories["hijri_that_day"].append(token)
        elif "يومهم" in token:
            categories["hijri_their_day"].append(token)
        elif "يومكم" in token:
            categories["hijri_your_day"].append(token)
        else:
            categories["excluded"].append(token)

    return categories


def load_month_tokens() -> List[str]:
    """Return all tokens containing the substring 'شهر'."""
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

    tokens: List[str] = []
    with data_path.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            _, _, text = line.split("|", 2)
            for token in text.split():
                clean = remove_diacritics(token)
                if "شهر" in clean:
                    tokens.append(clean)
    return tokens


def load_plural_dual_tokens() -> Dict[str, List[str]]:
    """Return plural (أيام) and dual (يومين) forms of the day root."""
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

    categories = {"plural": [], "dual": []}

    def normalize_plural_base(token: str) -> str:
        if not token:
            return token
        if token[0] in {"أ", "إ", "ٱ"}:
            token = "ا" + token[1:]
        while token and token[0] in PREFIX_CHARS:
            token = token[1:]
            if token and token[0] in {"أ", "إ", "ٱ"}:
                token = "ا" + token[1:]
        if token.startswith("ال"):
            token = token[2:]
            if token and token[0] in {"أ", "إ", "ٱ"}:
                token = "ا" + token[1:]
        changed = True
        while changed and token:
            changed = False
            for suffix in PRONOUN_SUFFIXES:
                if token.endswith(suffix):
                    token = token[: -len(suffix)]
                    changed = True
                    break
        if token.endswith("ا"):
            token = token[:-1]
        return token

    def normalize_dual_base(token: str) -> str:
        if not token:
            return token
        if token[0] in {"أ", "إ", "ٱ"}:
            token = "ا" + token[1:]
        while token and token[0] in PREFIX_CHARS:
            token = token[1:]
        if token.startswith("ال"):
            token = token[2:]
        return token

    with data_path.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            _, _, text = line.split("|", 2)
            for token in text.split():
                cleaned = remove_diacritics(token)
                plural_base = normalize_plural_base(cleaned)
                dual_base = normalize_dual_base(cleaned)
                if plural_base == "ايام":
                    categories["plural"].append(cleaned)
                elif dual_base == "يومين":
                    categories["dual"].append(cleaned)

    return categories


def categorise_month_tokens(tokens: List[str]) -> Dict[str, List[str]]:
    """Split month tokens into singular vs excluded (dual/plural) forms."""
    categories = {"month_singular": [], "month_excluded": []}
    for token in tokens:
        if any(plural in token for plural in ("شهور", "أشهر", "اشهر", "شهرين")):
            categories["month_excluded"].append(token)
        else:
            categories["month_singular"].append(token)
    return categories


def log10_probability(prob: float) -> float:
    """Return log10(probability) handling the prob == 0 edge case."""
    if prob == 0:
        return float("-inf")
    return math.log10(prob)


def one_in(prob: float) -> float:
    """Return the reciprocal 'one in X' figure, guarding against zero."""
    if prob == 0:
        return float("inf")
    return 1.0 / prob


# --- Main analysis ---------------------------------------------------------

def main() -> None:
    tokens = load_day_tokens()
    categories = categorise_tokens(tokens)
    month_tokens = load_month_tokens()
    month_categories = categorise_month_tokens(month_tokens)
    plural_dual = load_plural_dual_tokens()

    total_tokens = len(tokens)
    solar_total = (
        len(categories["solar_simple"])
        + len(categories["solar_definite"])
        + len(categories["solar_tanwin"])
    )
    hijri_total = (
        len(categories["solar_simple"])
        + len(categories["hijri_that_day"])
        + len(categories["hijri_their_day"])
        + len(categories["hijri_your_day"])
    )
    lunar_29_total = len(plural_dual["plural"]) + len(plural_dual["dual"])

    solar_prob = 1 / math.comb(total_tokens, solar_total)
    hijri_prob = 1 / math.comb(total_tokens, hijri_total)
    if 0 < lunar_29_total < total_tokens:
        lunar_prob = 1 / math.comb(total_tokens, lunar_29_total)
    elif lunar_29_total == 0:
        lunar_prob = 0.0
    else:
        lunar_prob = 1.0
    combined_prob = solar_prob * hijri_prob  # independent draws assumption

    print("=" * 70)
    print("YEARLY CYCLES - PROBABILITY EXPLORATION")
    print("=" * 70)
    print(f"Total tokens containing 'yawm' root: {total_tokens}")
    print()
    print("Solar pattern counts (Rule Set P):")
    print(f"  Simple forms      : {len(categories['solar_simple'])}")
    print(f"  Definite forms    : {len(categories['solar_definite'])}")
    print(f"  Tanwin forms      : {len(categories['solar_tanwin'])}")
    print(f"  Total (solar set) : {solar_total}")
    plural_count = len(categories["day_plural"]) or len(plural_dual["plural"])
    dual_count = len(categories["day_dual"]) or len(plural_dual["dual"])
    print(f"  Plural forms      : {plural_count}")
    print(f"  Dual forms        : {dual_count}")
    print(f"  Total (plural+dual): {lunar_29_total}")
    print()
    print("Hijri pattern counts (Component-based rule):")
    print(f"  Simple forms      : {len(categories['solar_simple'])}")
    print(f"  'That Day' forms  : {len(categories['hijri_that_day'])}")
    print(f"  'Their day' forms : {len(categories['hijri_their_day'])}")
    print(f"  'Your day' forms  : {len(categories['hijri_your_day'])}")
    print(f"  Total (hijri set) : {hijri_total}")
    print()
    print("Month pattern counts:")
    print(f"  Singular forms    : {len(month_categories['month_singular'])}")
    print(f"  Other forms       : {len(month_categories['month_excluded'])}")
    print(f"  Total (month root): {len(month_tokens)}")
    print()
    print("Null model assumption:")
    print("  Uniform random subset of tokens with the same size as the observed pattern.")
    print("  Only one subset satisfies the exact category requirements.")
    print()
    print("Probability estimates under this model:")
    print(f"  Solar pattern probability : {solar_prob:.3e}  (log10 ~ {log10_probability(solar_prob):.2f})")
    print(f"  -> approximately 1 in {one_in(solar_prob):.3e}")
    print(f"  Hijri pattern probability : {hijri_prob:.3e}  (log10 ~ {log10_probability(hijri_prob):.2f})")
    print(f"  -> approximately 1 in {one_in(hijri_prob):.3e}")
    if lunar_prob not in (0.0, 1.0):
        print(f"  Lunar month (29) probability : {lunar_prob:.3e}  (log10 ~ {log10_probability(lunar_prob):.2f})")
        print(f"  -> approximately 1 in {one_in(lunar_prob):.3e}")
    else:
        print("  Lunar month (29) probability : not computed (all qualifying tokens are selected).")
        lunar_prob = 1.0
    total_month_tokens = len(month_tokens)
    month_singular = len(month_categories["month_singular"])
    month_prob = 1 / math.comb(total_month_tokens, month_singular)
    print(f"  Calendar months (12) probability : {month_prob:.3e}  (log10 ~ {log10_probability(month_prob):.2f})")
    print(f"  -> approximately 1 in {one_in(month_prob):.3e}")
    print(f"  Combined (independent)    : {combined_prob:.3e}  (log10 ~ {log10_probability(combined_prob):.2f})")
    print(f"  -> approximately 1 in {one_in(combined_prob):.3e}")
    combined_with_lunar = combined_prob * lunar_prob
    combined_all = combined_with_lunar * month_prob if month_prob else float("inf")
    print(f"  Combined (solar + hijri + lunar 29 + months 12): {combined_all:.3e} "
          f"(log10 ~ {log10_probability(combined_all):.2f})")
    print(f"  -> approximately 1 in {one_in(combined_all):.3e}")
    print()
    print("[!] Reminder: Real linguistic processes are not uniform random draws, so these")
    print("    probabilities should be interpreted as illustrative rather than definitive.")


if __name__ == "__main__":
    main()
