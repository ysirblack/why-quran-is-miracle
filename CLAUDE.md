# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a research project analyzing numerical patterns and mathematical relationships in the Quran. The repository contains systematic verification tools and comprehensive documentation of 19+ distinct numerical patterns, including calendar alignments, word count balances, and scientific constants.

## Project Structure

- `/miracles/` - Main research directory with 19+ categorized numerical patterns
- `/data/` - Contains `quran-uthmani.txt` (Tanzil Ḥafṣ/Uthmānī text standard)  
- `/misc/` - Additional documentation and supporting materials
- Root level contains main documentation (`README.md`, `new_research.md`)

## Development Commands

### Running Python Scripts

Use `python3` instead of `python` (Python 3.9.6 available):

```bash
# Run specific verification scripts
python3 miracles/07_adam_jesus/adam_jesus_verification.py
python3 miracles/demo_verification.py

# Run the main verification toolkit
python3 miracles/quran_miracle_verifier.py --all
python3 miracles/quran_miracle_verifier.py --pattern man_woman

# Run tests
python3 miracles/test_miracle_verifier.py
```

### Installation

Dependencies are minimal (uses Python standard library):

```bash
# Install optional dependencies if needed
pip3 install -r miracles/requirements.txt
```

## Core Architecture

### Main Components

1. **QuranTextProcessor** - Handles text loading, normalization, and Unicode processing from Tanzil format
2. **ArabicWordCounter** - Performs morphological analysis and Arabic text tokenization with diacritics handling
3. **MiraclePatternVerifier** - Contains verification methods for all documented numerical patterns
4. **MiracleVerifierCLI** - Command-line interface with export capabilities

### Text Processing Pipeline

- **Source**: Tanzil Ḥafṣ/Uthmānī text (`data/quran-uthmani.txt`)
- **Normalization**: Unicode NFC, tatweel removal, diacritic handling
- **Counting**: Token-based with Arabic morphological awareness
- **Filtering**: Root-based analysis with semantic precision

### Pattern Categories

- **Calendar Patterns**: 365 days, 12 months, lunar/solar cycles
- **Biological Patterns**: 23:23 chromosome alignment (Man:Woman)
- **Balance Patterns**: Life:Death (145:145), Angels:Devils (88:88)
- **Scientific Constants**: Verse gap alignments with physical properties
- **Geographic Patterns**: Land:Sea ratios matching Earth's surface

## Key Files

- `miracles/quran_miracle_verifier.py` - Main verification toolkit
- `miracles/demo_verification.py` - Simple demonstration without Unicode issues
- `miracles/test_miracle_verifier.py` - Test suite for validation
- Individual pattern scripts in numbered miracle directories
- `data/quran-uthmani.txt` - Primary Quran text data (1.3MB)

## Research Methodology

- **Text Standard**: Tanzil Ḥafṣ/Uthmānī with consistent Unicode handling
- **Counting Rules**: Morphological root-based analysis with documented exclusions
- **Statistical Analysis**: Probability calculations for pattern significance
- **Reproducibility**: Transparent methodology with clear filtering criteria
- **Verification**: Multiple cross-references and independent validation methods
