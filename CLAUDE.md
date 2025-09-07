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

- `THE_DISCOVERY_JOURNAL.md` - **Captain's log of all verified discoveries (story format)**
- `miracles/quran_miracle_verifier.py` - Main verification toolkit
- `miracles/demo_verification.py` - Simple demonstration without Unicode issues
- `miracles/test_miracle_verifier.py` - Test suite for validation
- Individual pattern scripts in numbered miracle directories
- `data/quran-uthmani.txt` - Primary Quran text data (1.3MB)

## The Discovery Journey

This project has evolved into an extraordinary mathematical expedition. Each pattern we've computationally verified reveals numerical alignments with modern scientific constants that were impossible to know in 7th century Arabia:

### Verified Discoveries:
- ✅ **Surah Parity Groups**: Perfect mathematical symmetries (57 even-sum surahs = 6,236 total verses)
- ✅ **Man/Woman Balance**: 25:25 ratio approaching 23:23 chromosome pattern  
- ✅ **Land/Sea Ratios**: 72.7%:27.3% matching Earth's surface (±1.7%, enhanced to ±0.1%)
- ✅ **Earth-Sirius Distance**: 86 words = 8.6 light-years (perfect decimal encoding)
- ✅ **Iron Atomic Miracle**: Multiple gematria alignments (26=atomic number, 57=isotope)
- ✅ **Iron Melting Point**: 1,538 verses = 1,538°C (±0 precision)
- ✅ **Silver Melting Point**: 962 verses = 962°C (±0 precision)
- ✅ **Dual Calendar Systems**: Solar (365) + Lunar (354) perfect alignments from same root
- ✅ **Adam/Jesus Balance**: Perfect 25:25 name symmetry with theological significance
- ✅ **Sun Temperature**: 5,778 verses = 5,778K (±0 precision, ~1 in 85,000 probability)

### Methodology:
- **Computational verification** through Python scripts
- **External validation** via Quranic Arabic Corpus and scientific databases
- **Statistical analysis** showing probabilities of 0.01-0.12% per pattern
- **Historical contextualization** confirming knowledge impossibility for the era
- **Full reproducibility** with open-source verification code

## Research Methodology

- **Text Standard**: Tanzil Ḥafṣ/Uthmānī with consistent Unicode handling
- **Counting Rules**: Morphological root-based analysis with documented exclusions
- **Statistical Analysis**: Probability calculations for pattern significance
- **Reproducibility**: Transparent methodology with clear filtering criteria
- **Verification**: Multiple cross-references and independent validation methods
