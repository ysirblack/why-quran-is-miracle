#!/usr/bin/env python3
"""
Simple demonstration of the Quran Miracle Verifier functionality
Avoids Unicode display issues while showing the core verification capabilities
"""

from quran_miracle_verifier import QuranTextProcessor, ArabicWordCounter, MiraclePatternVerifier

def main():
    print("=" * 60)
    print("QURAN MIRACLE VERIFIER - DEMO")
    print("=" * 60)
    
    try:
        # Initialize the system
        processor = QuranTextProcessor()
        counter = ArabicWordCounter(processor)
        verifier = MiraclePatternVerifier(counter)
        
        print(f"Loaded {len(processor.verses)} verses for analysis")
        print()
        
        # Run a few key verifications
        patterns_to_test = [
            ("Man:Woman 23:23", verifier.verify_man_woman_23_23),
            ("Life:Death 145:145", verifier.verify_life_death_145_145),
            ("Calendar 365:30:12", verifier.verify_days_months_365_30_12),
            ("Land:Sea Ratio", verifier.verify_land_sea_ratio),
        ]
        
        results = {}
        for pattern_name, verification_func in patterns_to_test:
            print(f"Testing {pattern_name}...")
            result = verification_func()
            results[pattern_name] = result
            
            # Display key results
            for key, value in result.items():
                if 'count' in key or 'matches_' in key:
                    print(f"  {key}: {value}")
            print()
        
        # Summary
        verified_patterns = []
        for pattern, data in results.items():
            for key, value in data.items():
                if key.startswith('matches_') and value:
                    verified_patterns.append(pattern)
                    break
        
        print("=" * 60)
        print("VERIFICATION SUMMARY")
        print("=" * 60)
        print(f"Patterns tested: {len(patterns_to_test)}")
        print(f"Patterns verified: {len(verified_patterns)}")
        print()
        
        if verified_patterns:
            print("Verified patterns:")
            for pattern in verified_patterns:
                print(f"  - {pattern}")
        
        print()
        print("Note: This demo uses sample data. For complete verification,")
        print("download full Quran text from https://tanzil.net/download/")
        
    except Exception as e:
        print(f"Demo error: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())