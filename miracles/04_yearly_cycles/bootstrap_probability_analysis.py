#!/usr/bin/env python3
"""
Bootstrap Probability Analysis for Yearly Cycles

This script uses bootstrap resampling to calculate the probability of the
yearly cycle patterns (365 solar, 354 hijri, 29 lunar) occurring by chance.

Unlike combinatorial probability (which assumes uniform random selection),
this approach:
1. Preserves the actual linguistic distribution of tokens
2. Resamples with replacement from the real Quran data
3. Tests how often resampled data produces the target totals

This is a more realistic null hypothesis that respects the linguistic
structure of the text while still testing for coincidence.
"""

from __future__ import annotations

import random
import re
from pathlib import Path
from typing import Dict, List, Tuple
from collections import Counter

# Arabic prefixes and suffixes
PREFIX_CHARS = {"و", "ف", "ب", "ل", "ك"}
PRONOUN_SUFFIXES = ("كما", "كم", "كن", "هما", "هم", "هن", "ها", "نا")


def remove_diacritics(text: str) -> str:
    """Strip Arabic tashkeel and tatweel characters."""
    return re.sub(r'[\u064B-\u065F\u0670\u0640]', '', text)


def normalize_alef(text: str) -> str:
    """Normalize all alef variants to plain alef."""
    return text.replace("أ", "ا").replace("إ", "ا").replace("ٱ", "ا").replace("آ", "ا")


def load_all_yawm_tokens() -> List[Tuple[str, str]]:
    """
    Load all tokens from the day root (يوم) from the Quran.
    This includes:
    - Tokens containing يوم (singular forms)
    - Tokens containing أيام/ايام (plural forms - different spelling!)
    
    Returns list of (original_token, cleaned_token) tuples.
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

    tokens: List[Tuple[str, str]] = []
    with data_path.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            _, _, text = line.split("|", 2)
            for token in text.split():
                clean = remove_diacritics(token)
                normalized = normalize_alef(clean)
                
                # Include tokens with يوم OR أيام (plural has different spelling)
                if "يوم" in clean or "ايام" in normalized:
                    tokens.append((token, clean))
    
    return tokens


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


def categorize_token(token: str) -> str:
    """
    Categorize a single token into grammatical categories.
    Returns the category name as a string.
    """
    normalized = normalize_alef(token)
    
    # Priority order matters - check most specific first
    
    # Special compounds (hijri pattern)
    if "يومئذ" in token:
        return "that_day"  # yawma'idhin
    if "يومهم" in token:
        return "their_day"  # yawmahum
    if "يومكم" in token:
        return "your_day"  # yawmukum
    
    # Plural and dual - use proper normalization
    plural_base = normalize_plural_base(token)
    dual_base = normalize_dual_base(token)
    
    if plural_base == "ايام":
        return "plural"
    if dual_base == "يومين":
        return "dual"
    
    # Tanwin (solar pattern)
    if token == "يوما":
        return "tanwin"
    
    # Definite (solar pattern)
    if any(al in token for al in ("اليوم", "الْيوم", "ٱلْيوم", "ٱليوم")):
        return "definite"
    
    # Simple forms (both solar and hijri)
    if token == "يوم" or (len(token) <= 5 and "يوم" in token):
        return "simple"
    
    # Everything else
    return "excluded"


def calculate_totals(token_categories: List[str]) -> Dict[str, int]:
    """Calculate solar, hijri, and lunar totals from categorized tokens."""
    counts = Counter(token_categories)
    
    solar_total = counts["simple"] + counts["definite"] + counts["tanwin"]
    hijri_total = counts["simple"] + counts["that_day"] + counts["their_day"] + counts["your_day"]
    lunar_total = counts["plural"] + counts["dual"]
    
    return {
        "solar": solar_total,
        "hijri": hijri_total,
        "lunar": lunar_total,
        "counts": counts
    }


def bootstrap_analysis(tokens: List[Tuple[str, str]], n_trials: int = 1_000_000) -> Dict:
    """
    Perform bootstrap resampling to test probability of patterns.
    
    Args:
        tokens: List of (original, cleaned) token tuples
        n_trials: Number of bootstrap samples to generate
    
    Returns:
        Dictionary with results including probabilities and hit counts
    """
    # Get actual observed values
    actual_categories = [categorize_token(clean) for _, clean in tokens]
    actual_totals = calculate_totals(actual_categories)
    
    print("=" * 70)
    print("BOOTSTRAP PROBABILITY ANALYSIS - YEARLY CYCLES")
    print("=" * 70)
    print()
    print("Methodology:")
    print("  1. Load all 451 tokens containing the 'yawm' root")
    print("  2. Resample 451 tokens with replacement (bootstrap)")
    print("  3. Recategorize using grammatical rules")
    print("  4. Calculate solar/hijri/lunar totals")
    print(f"  5. Repeat {n_trials:,} times")
    print("  6. Count how often we hit exact target values")
    print()
    print("This preserves linguistic distribution while testing for coincidence.")
    print()
    print("-" * 70)
    print("OBSERVED VALUES (Actual Quran):")
    print("-" * 70)
    print(f"  Total 'yawm' tokens: {len(tokens)}")
    print()
    print("  Category counts:")
    for category, count in sorted(actual_totals["counts"].items()):
        print(f"    {category:12s}: {count:3d}")
    print()
    print("  Pattern totals:")
    print(f"    Solar 365:  {actual_totals['solar']:3d} (simple + definite + tanwin)")
    print(f"    Hijri 354:  {actual_totals['hijri']:3d} (simple + that_day + their_day + your_day)")
    print(f"    Lunar 29:   {actual_totals['lunar']:3d} (plural + dual)")
    print()
    print("-" * 70)
    print(f"RUNNING BOOTSTRAP ANALYSIS ({n_trials:,} trials)...")
    print("-" * 70)
    
    # Bootstrap resampling
    solar_hits = 0
    hijri_hits = 0
    lunar_hits = 0
    both_solar_hijri = 0
    all_three = 0
    
    # Track distribution for analysis
    solar_distribution = []
    hijri_distribution = []
    lunar_distribution = []
    
    cleaned_tokens = [clean for _, clean in tokens]
    
    for trial in range(n_trials):
        # Progress reporting - adjust frequency based on trial count
        report_freq = max(1000, n_trials // 10)
        if (trial + 1) % report_freq == 0:
            print(f"  Progress: {trial + 1:,} / {n_trials:,} ({100*(trial+1)/n_trials:.1f}%)")
        
        # Resample with replacement
        resampled = random.choices(cleaned_tokens, k=len(tokens))
        
        # Categorize resampled tokens
        categories = [categorize_token(token) for token in resampled]
        
        # Calculate totals
        totals = calculate_totals(categories)
        
        solar_distribution.append(totals["solar"])
        hijri_distribution.append(totals["hijri"])
        lunar_distribution.append(totals["lunar"])
        
        # Check for exact hits
        solar_hit = (totals["solar"] == 365)
        hijri_hit = (totals["hijri"] == 354)
        lunar_hit = (totals["lunar"] == 29)
        
        if solar_hit:
            solar_hits += 1
        if hijri_hit:
            hijri_hits += 1
        if lunar_hit:
            lunar_hits += 1
        if solar_hit and hijri_hit:
            both_solar_hijri += 1
        if solar_hit and hijri_hit and lunar_hit:
            all_three += 1
    
    print()
    print("-" * 70)
    print("RESULTS:")
    print("-" * 70)
    print()
    
    # Calculate probabilities
    solar_prob = solar_hits / n_trials
    hijri_prob = hijri_hits / n_trials
    lunar_prob = lunar_hits / n_trials
    both_prob = both_solar_hijri / n_trials
    all_prob = all_three / n_trials
    
    # Print results
    print("Individual Pattern Probabilities:")
    print()
    print(f"  Solar 365:")
    print(f"    Hits: {solar_hits:,} / {n_trials:,}")
    print(f"    P(exactly 365) = {solar_prob:.6f}")
    if solar_prob > 0:
        print(f"    -> approximately 1 in {1/solar_prob:,.1f}")
    else:
        print(f"    -> approximately < 1 in {n_trials:,}")
    print()
    
    print(f"  Hijri 354:")
    print(f"    Hits: {hijri_hits:,} / {n_trials:,}")
    print(f"    P(exactly 354) = {hijri_prob:.6f}")
    if hijri_prob > 0:
        print(f"    -> approximately 1 in {1/hijri_prob:,.1f}")
    else:
        print(f"    -> approximately < 1 in {n_trials:,}")
    print()
    
    print(f"  Lunar 29:")
    print(f"    Hits: {lunar_hits:,} / {n_trials:,}")
    print(f"    P(exactly 29) = {lunar_prob:.6f}")
    if lunar_prob > 0:
        print(f"    -> approximately 1 in {1/lunar_prob:,.1f}")
    else:
        print(f"    -> approximately < 1 in {n_trials:,}")
    print()
    
    print("-" * 70)
    print("Combined Pattern Probabilities:")
    print("-" * 70)
    print()
    print(f"  Both Solar (365) AND Hijri (354):")
    print(f"    Hits: {both_solar_hijri:,} / {n_trials:,}")
    print(f"    P(both) = {both_prob:.6f}")
    if both_prob > 0:
        print(f"    -> approximately 1 in {1/both_prob:,.1f}")
    else:
        print(f"    -> approximately < 1 in {n_trials:,}")
    print()
    
    print(f"  All Three (Solar 365 + Hijri 354 + Lunar 29):")
    print(f"    Hits: {all_three:,} / {n_trials:,}")
    print(f"    P(all three) = {all_prob:.6f}")
    if all_prob > 0:
        print(f"    -> approximately 1 in {1/all_prob:,.1f}")
    else:
        print(f"    -> approximately < 1 in {n_trials:,}")
    print()
    
    # Distribution statistics
    print("-" * 70)
    print("Distribution Statistics (from bootstrap samples):")
    print("-" * 70)
    print()
    
    import statistics
    
    print(f"  Solar total:")
    print(f"    Mean: {statistics.mean(solar_distribution):.2f}")
    print(f"    Std Dev: {statistics.stdev(solar_distribution):.2f}")
    print(f"    Range: [{min(solar_distribution)}, {max(solar_distribution)}]")
    print()
    
    print(f"  Hijri total:")
    print(f"    Mean: {statistics.mean(hijri_distribution):.2f}")
    print(f"    Std Dev: {statistics.stdev(hijri_distribution):.2f}")
    print(f"    Range: [{min(hijri_distribution)}, {max(hijri_distribution)}]")
    print()
    
    print(f"  Lunar total:")
    print(f"    Mean: {statistics.mean(lunar_distribution):.2f}")
    print(f"    Std Dev: {statistics.stdev(lunar_distribution):.2f}")
    print(f"    Range: [{min(lunar_distribution)}, {max(lunar_distribution)}]")
    print()
    
    print("=" * 70)
    print("INTERPRETATION:")
    print("=" * 70)
    print()
    print("This bootstrap analysis preserves the linguistic structure of")
    print("the text while testing whether the exact totals (365, 354, 29)")
    print("could occur by chance through resampling.")
    print()
    print("The probability reflects how often grammatical categories,")
    print("when resampled, produce these exact calendar-significant numbers.")
    print()
    
    return {
        "n_trials": n_trials,
        "solar_hits": solar_hits,
        "hijri_hits": hijri_hits,
        "lunar_hits": lunar_hits,
        "both_hits": both_solar_hijri,
        "all_hits": all_three,
        "solar_prob": solar_prob,
        "hijri_prob": hijri_prob,
        "lunar_prob": lunar_prob,
        "both_prob": both_prob,
        "all_prob": all_prob,
        "solar_distribution": solar_distribution,
        "hijri_distribution": hijri_distribution,
        "lunar_distribution": lunar_distribution,
    }


def main():
    """Main entry point."""
    tokens = load_all_yawm_tokens()
    
    # Run bootstrap with 100k trials (balanced between speed and accuracy)
    results = bootstrap_analysis(tokens, n_trials=100_000)
    
    print()
    print("Analysis complete.")
    print()


if __name__ == "__main__":
    main()

