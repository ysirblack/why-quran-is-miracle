#!/usr/bin/env python3
"""
Calendar Pattern Verifier - Days/Months Rule-Set P
Verifies the 365/30/12 calendar alignment miracle in the Quran

Based on research from new_research.md:
- Day (singular): count only bare يوم / ٱليوم tokens; exclude يومئذ; exclude clitic prefixes و/ف/ب/ل/ك and any pronominal suffixes
- Days (plural+dual): include أيام (any case/attachments) and يومين (dual)  
- Month (singular): include only شهر / ٱلشهر (singular); exclude plurals/dual
- Count tokens, not once-per-verse

Expected results:
- Day (singular) = 365
- Days (plural+dual) = 30 → أيام = 27, يومين = 3
- Month (singular) = 12
"""

import re
import argparse
from pathlib import Path
from typing import Dict, List, Tuple, Union
import unicodedata

class QuranTextLoader:
    """Loads Quran text from Uthmani format"""
    
    def __init__(self, data_path: str = None):
        self.verses = {}
        self.data_path = data_path or self._find_data_file()
        self.load_quran()
    
    def _find_data_file(self) -> str:
        """Find the Quran data file"""
        possible_paths = [
            "../../data/quran-uthmani.txt",
            "../data/quran-uthmani.txt", 
            "data/quran-uthmani.txt"
        ]
        
        for path in possible_paths:
            if Path(path).exists():
                return path
                
        raise FileNotFoundError("Could not find quran-uthmani.txt data file")
    
    def load_quran(self):
        """Load Quran text from file"""
        print(f"Loading Quran from: {self.data_path}")
        
        with open(self.data_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                    
                if '|' in line:
                    parts = line.split('|', 2)
                    if len(parts) >= 3:
                        surah = int(parts[0])
                        verse = int(parts[1])
                        text = parts[2]
                        self.verses[(surah, verse)] = text
        
        print(f"Loaded {len(self.verses)} verses")
    
    def get_verses(self) -> Dict[Tuple[int, int], str]:
        """Get all verses"""
        return self.verses

class ArabicTextProcessor:
    """Processes Arabic text according to Rule-Set P methodology"""
    
    @staticmethod
    def remove_diacritics(text: str) -> str:
        """Remove Arabic diacritics for pattern matching"""
        diacritics = r'[\u064B-\u065F\u0670\u0640]'
        return re.sub(diacritics, '', text)
    
    @staticmethod
    def tokenize(text: str) -> List[str]:
        """Split text into tokens"""
        return text.split()
    
    @staticmethod
    def has_clitic_prefix(token: str) -> bool:
        """Check if token has clitic prefixes و/ف/ب/ل/ك that should be excluded per Rule-Set P"""
        clean_token = ArabicTextProcessor.remove_diacritics(token)
        
        # Check for clitic prefixes that should exclude the word
        clitic_prefixes = ['و', 'ف', 'ب', 'ل', 'ك']
        
        for prefix in clitic_prefixes:
            if clean_token.startswith(prefix):
                remainder = clean_token[len(prefix):]
                # Check if remainder matches our target words
                target_patterns = ['يوم', 'اليوم', 'شهر', 'الشهر', 'ايام', 'يومين']
                if any(remainder == pattern or remainder.startswith(pattern) for pattern in target_patterns):
                    return True
        return False
    
    @staticmethod
    def has_pronominal_suffix(token: str) -> bool:
        """Check if token has pronominal suffixes that should be excluded per Rule-Set P"""
        clean_token = ArabicTextProcessor.remove_diacritics(token)
        
        # Common pronominal suffixes
        suffixes = ['ه', 'ها', 'هم', 'هن', 'ني', 'ك', 'كم', 'كن', 'ي']
        
        for suffix in suffixes:
            if clean_token.endswith(suffix):
                # Check if removing suffix gives us a target word
                base = clean_token[:-len(suffix)]
                target_patterns = ['يوم', 'اليوم', 'شهر', 'الشهر']
                if base in target_patterns:
                    return True
        return False

class CalendarPatternVerifier:
    """Verifies the Days/Months calendar pattern using Rule-Set P methodology"""
    
    def __init__(self, data_path: str = None):
        self.loader = QuranTextLoader(data_path)
        self.verses = self.loader.get_verses()
        self.processor = ArabicTextProcessor()
    
    def count_pattern(self, target_patterns: List[str], exclude_patterns: List[str] = None) -> Tuple[int, List[str]]:
        """Count occurrences of patterns according to Rule-Set P"""
        exclude_patterns = exclude_patterns or []
        matches = []
        
        for (surah, verse), text in self.verses.items():
            tokens = self.processor.tokenize(text)
            
            for token in tokens:
                clean_token = self.processor.remove_diacritics(token)
                
                # Check if token matches any target pattern
                pattern_match = False
                for pattern in target_patterns:
                    clean_pattern = self.processor.remove_diacritics(pattern)
                    
                    if self._is_valid_match(clean_token, clean_pattern, token):
                        pattern_match = True
                        break
                
                # Check exclusions
                if pattern_match:
                    excluded = False
                    for exclude_pattern in exclude_patterns:
                        clean_exclude = self.processor.remove_diacritics(exclude_pattern)
                        if clean_exclude in clean_token:
                            excluded = True
                            break
                    
                    if not excluded:
                        matches.append(f"{surah}:{verse} - {token}")
        
        return len(matches), matches
    
    def _is_valid_match(self, clean_token: str, clean_pattern: str, original_token: str) -> bool:
        """Check if token is a valid match according to Rule-Set P (bare words only)"""
        # Exclude tokens with clitic prefixes
        if self.processor.has_clitic_prefix(original_token):
            return False
        
        # Exclude tokens with pronominal suffixes
        if self.processor.has_pronominal_suffix(original_token):
            return False
        
        # Check for exact match
        if clean_token == clean_pattern:
            return True
        
        # Allow case endings (common in Arabic)
        if clean_token.startswith(clean_pattern):
            suffix = clean_token[len(clean_pattern):]
            # Allow single character case endings
            if len(suffix) == 1 and suffix in ['ا', 'ة', 'ه', 'ي', 'و', 'ن']:
                return True
        
        return False
    
    def verify_days_months_calendar(self) -> Dict[str, Union[int, List[str], bool]]:
        """Verify the complete Days/Months calendar pattern"""
        print("=" * 60)
        print("CALENDAR PATTERN VERIFICATION (Rule-Set P)")
        print("=" * 60)
        
        # Day (singular) patterns
        day_patterns = ["يوم", "ٱليوم"]
        day_exclude = ["يومئذ"]
        
        print(f"\n1) Counting Day (singular) patterns")
        day_count, day_matches = self.count_pattern(day_patterns, day_exclude)
        print(f"   Found: {day_count} matches")
        print(f"   First few references: {[m.split(' - ')[0] for m in day_matches[:5]]}")
        
        # Days (plural+dual) patterns  
        days_patterns = ["أيام", "يومين"]
        
        print(f"\n2) Counting Days (plural+dual) patterns")
        days_count, days_matches = self.count_pattern(days_patterns)
        print(f"   Found: {days_count} matches")
        print(f"   First few references: {[m.split(' - ')[0] for m in days_matches[:5]]}")
        
        # Month (singular) patterns
        month_patterns = ["شهر", "ٱلشهر"] 
        month_exclude = ["أشهر", "شهور", "شهرين"]
        
        print(f"\n3) Counting Month (singular) patterns")
        month_count, month_matches = self.count_pattern(month_patterns, month_exclude)
        print(f"   Found: {month_count} matches")
        print(f"   First few references: {[m.split(' - ')[0] for m in month_matches[:5]]}")
        
        # Results analysis
        print(f"\n" + "=" * 60)
        print("RESULTS")
        print("=" * 60)
        print(f"Day (singular):     {day_count:3d} (target: 365)")
        print(f"Days (plural+dual): {days_count:3d} (target: 30)")
        print(f"Month (singular):   {month_count:3d} (target: 12)")
        
        # Verification
        day_match = day_count == 365
        days_match = days_count == 30
        month_match = month_count == 12
        all_match = day_match and days_match and month_match
        
        print(f"\nVerification:")
        print(f"[*] Solar year (365 days):     {'VERIFIED' if day_match else 'NOT MATCHING'}")
        print(f"[*] Lunar month (30 days):     {'VERIFIED' if days_match else 'NOT MATCHING'}")
        print(f"[*] Calendar months (12):      {'VERIFIED' if month_match else 'NOT MATCHING'}")
        print(f"[*] Complete pattern:          {'VERIFIED' if all_match else 'NOT MATCHING'}")
        
        if all_match:
            print(f"\n[SUCCESS] MIRACLE VERIFIED: Perfect calendar alignment!")
            print(f"          Joint probability ≈ 1 in 131,400 (0.00076%)")
        else:
            print(f"\n[INFO] Pattern not fully verified. Differences:")
            print(f"       Day singular: {day_count - 365:+d} from target")
            print(f"       Days plural:  {days_count - 30:+d} from target") 
            print(f"       Month single: {month_count - 12:+d} from target")
        
        return {
            "day_singular_count": day_count,
            "day_singular_matches": day_matches,
            "days_plural_count": days_count, 
            "days_plural_matches": days_matches,
            "month_singular_count": month_count,
            "month_singular_matches": month_matches,
            "solar_year_match": day_match,
            "lunar_month_match": days_match,
            "calendar_months_match": month_match,
            "complete_pattern_verified": all_match
        }

def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description="Verify the Days/Months calendar pattern in the Quran",
        epilog="Example: python calendar_verifier.py --data ../../data/quran-uthmani.txt"
    )
    
    parser.add_argument('--data', type=str, help='Path to Quran data file')
    parser.add_argument('--verbose', action='store_true', help='Show detailed matches')
    
    args = parser.parse_args()
    
    try:
        verifier = CalendarPatternVerifier(args.data)
        results = verifier.verify_days_months_calendar()
        
        if args.verbose:
            print(f"\n" + "=" * 60)
            print("DETAILED MATCHES")
            print("=" * 60)
            
            print(f"\nDay (singular) matches:")
            for match in results["day_singular_matches"][:20]:  # Show first 20
                print(f"  {match}")
            
            print(f"\nDays (plural+dual) matches:")
            for match in results["days_plural_matches"]:
                print(f"  {match}")
                
            print(f"\nMonth (singular) matches:")
            for match in results["month_singular_matches"]:
                print(f"  {match}")
                
    except Exception as e:
        print(f"Error: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    main()