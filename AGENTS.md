# Repository Guidelines

## Project Structure & Module Organization

- `miracles/` — Source analyses and verification scripts grouped by topic (e.g., `04_yearly_cycles/solar_365/day_365_verifier.py`). Each topic typically includes `main.md` (explanation) and one or more `.py` scripts.
- `data/` — Canonical text sources (e.g., `quran-uthmani.txt`). Do not modify; treat as read-only input.
- `misc/` — Long-form write-ups and generated artifacts.
- Root docs — `README.md`, `THE_DISCOVERY_JOURNAL.md`, and assessment files provide context and methodology.

## Build, Test, and Development Commands

- Environment (optional extras): `python -m venv .venv && source .venv/bin/activate && pip install -r miracles/requirements.txt`
- Run a verifier (example): `python miracles/04_yearly_cycles/solar_365/day_365_verifier.py`
- More examples:
  - `python miracles/04_yearly_cycles/hijri_354/hijri_354_combined.py`
  - `python miracles/20_carbon_creation/carbon_creation_verification.py`
- Formatting (optional): `black miracles`  — format Python code.
- Type check (optional): `mypy miracles`  — basic static checks.

## Coding Style & Naming Conventions

- Python 3.9+; prefer standard library. Use clear, pure functions and deterministic I/O.
- Indentation: 4 spaces; line length ~100 chars; include type hints where helpful.
- Filenames: `snake_case.py`; topic folders prefixed with two-digit index (e.g., `06_verse_gap_alignments`).
- Keep data constants and regex at top of modules; document assumptions in module docstrings.

## Testing Guidelines

- No formal suite exists yet. When adding code, include `pytest` tests under `tests/` mirroring paths (e.g., `tests/04_yearly_cycles/test_solar_365.py`).
- Name tests `test_*.py`; focus on tokenization, counting, and edge cases (Unicode normalization, exclusions).
- Run with: `pytest -q`; aim for coverage of new logic; avoid network in tests.

## Commit & Pull Request Guidelines

- Commits: short, imperative subject (e.g., “add hijri day count”). Prefixes like `feat:`, `fix:`, or `chore:` are welcome but not required.
- PRs: include a concise description, reproducible steps (commands run), input data references, and sample outputs. Attach screenshots or logs for verifiers when useful.
- Do not rewrite `data/quran-uthmani.txt`; additions should be new scripts or docs under an appropriate topic folder.

## Security & Configuration Tips

- Prefer offline operation using `data/` sources. If a script supports online fetching, make it optional and disabled by default.
- Large media or generated outputs should go in `misc/` or be linked externally rather than committed to source folders.

