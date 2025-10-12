import importlib.util
import sys
from pathlib import Path

import pytest


MODULE_PATH = (
    Path(__file__).resolve().parents[2]
    / "miracles"
    / "05_land_vs_sea"
    / "land_sea_simple_verification.py"
)

EXPECTED_SEA_REFS = {
    (2, 50),
    (2, 164),
    (5, 96),
    (6, 59),
    (6, 63),
    (6, 97),
    (7, 138),
    (7, 163),
    (10, 22),
    (10, 90),
    (14, 32),
    (16, 14),
    (17, 66),
    (17, 67),
    (17, 70),
    (18, 61),
    (18, 63),
    (18, 79),
    (18, 109),
    (20, 77),
    (22, 65),
    (26, 63),
    (27, 63),
    (30, 41),
    (31, 27),
    (31, 31),
    (42, 32),
    (44, 24),
    (45, 12),
    (52, 6),
    (55, 24),
}

EXPECTED_LAND_REFS = {
    (5, 96),
    (6, 59),
    (6, 63),
    (6, 97),
    (10, 22),
    (17, 67),
    (17, 68),
    (17, 70),
    (27, 63),
    (29, 65),
    (30, 41),
    (31, 32),
}


@pytest.fixture(scope="module")
def land_sea_module():
    spec = importlib.util.spec_from_file_location(
        "land_sea_simple_verification_tests", MODULE_PATH
    )
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def verification_result(land_sea_module):
    return land_sea_module.verify_land_sea(show_details=False)


def test_primary_counts_and_percentages(verification_result):
    sea_count, land_count = verification_result.primary_counts()
    assert sea_count == 32
    assert land_count == 12

    sea_pct, land_pct = verification_result.primary_percentages()
    assert sea_pct == pytest.approx(72.7272727, rel=1e-6)
    assert land_pct == pytest.approx(27.2727272, rel=1e-6)

    assert len(verification_result.dry_land_tokens) == 1
    enhanced_sea, enhanced_land = verification_result.enhanced_counts()
    assert enhanced_sea == 32
    assert enhanced_land == 13


def test_sea_token_references(verification_result):
    sea_refs = {(match.surah, match.verse) for match in verification_result.sea_tokens}
    assert sea_refs == EXPECTED_SEA_REFS

    # Two occurrences of 18:109 should be present as separate tokens.
    count_18109 = sum(
        1 for match in verification_result.sea_tokens if (match.surah, match.verse) == (18, 109)
    )
    assert count_18109 == 2


def test_land_token_references(verification_result):
    land_refs = {(match.surah, match.verse) for match in verification_result.land_tokens}
    assert land_refs == EXPECTED_LAND_REFS


def test_semantic_exclusions_documented(verification_result):
    exclusions = {
        (excluded.match.surah, excluded.match.verse): excluded.reason
        for excluded in verification_result.excluded_land_tokens
    }
    assert (52, 28) in exclusions
    assert exclusions[(52, 28)] == "divine name"
    assert (2, 177) in exclusions
    assert exclusions[(2, 177)] == "moral sense (ٱلْبِرّ)"
