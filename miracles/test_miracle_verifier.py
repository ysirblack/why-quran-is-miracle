#!/usr/bin/env python3
"""
Test Suite for Quran Miracle Verifier

This test suite validates the verification toolkit against known results
and ensures the pattern matching algorithms work correctly.

Run with: python test_miracle_verifier.py
"""

import unittest
from unittest.mock import patch, MagicMock
import sys
import os

# Add the current directory to the path to import our module
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from quran_miracle_verifier import (
    QuranTextProcessor, 
    ArabicWordCounter, 
    MiraclePatternVerifier,
    MiracleVerifierCLI
)

class TestQuranTextProcessor(unittest.TestCase):
    """Test the Quran text loading and processing functionality"""
    
    def setUp(self):
        self.processor = QuranTextProcessor()
    
    def test_normalize_arabic(self):
        """Test Arabic text normalization"""
        # Test tatweel removal
        text_with_tatweel = "اللــــــه"
        expected = "الله"
        result = self.processor.normalize_arabic(text_with_tatweel)
        self.assertEqual(result, expected)
        
        # Test whitespace trimming
        text_with_spaces = "  بسم الله الرحمن الرحيم  "
        expected = "بسم الله الرحمن الرحيم"
        result = self.processor.normalize_arabic(text_with_spaces)
        self.assertEqual(result, expected)
    
    def test_tokenize(self):
        """Test Arabic text tokenization"""
        text = "بسم الله الرحمن الرحيم"
        tokens = self.processor.tokenize(text)
        self.assertEqual(len(tokens), 4)
        self.assertIn("بسم", tokens)
        self.assertIn("الله", tokens)
        self.assertIn("الرحمن", tokens)
        self.assertIn("الرحيم", tokens)
    
    def test_verse_retrieval(self):
        """Test verse retrieval functionality"""
        # Test existing verse
        verse = self.processor.get_verse(1, 1)
        self.assertIsNotNone(verse)
        self.assertIn("الله", verse)
        
        # Test non-existing verse
        verse = self.processor.get_verse(999, 999)
        self.assertIsNone(verse)

class TestArabicWordCounter(unittest.TestCase):
    """Test the Arabic word counting functionality"""
    
    def setUp(self):
        self.processor = QuranTextProcessor()
        # Create test data with known words
        self.processor.verses = {
            (1, 1): "الحي الميت",  # life and death
            (1, 2): "رجل امرأة",   # man and woman  
            (1, 3): "الحياة الموت", # life and death
            (2, 1): "يوم شهر",     # day and month
            (2, 2): "البر البحر",   # land and sea
            (3, 1): "ملك شيطان",   # angel and devil
        }
        self.counter = ArabicWordCounter(self.processor)
    
    def test_count_by_pattern_exact(self):
        """Test exact pattern matching"""
        # Count exact occurrences of "الحي"
        results = self.counter.count_by_pattern("الحي", exact_match=True)
        # Should find it in verse 1:1
        self.assertGreater(sum(results.values()), 0)
    
    def test_count_by_pattern_partial(self):
        """Test partial pattern matching"""
        # Count partial matches containing "حي"
        results = self.counter.count_by_pattern("حي", exact_match=False)
        # Should find "الحي" and "الحياة"
        self.assertGreater(sum(results.values()), 1)
    
    def test_count_with_exclusions(self):
        """Test counting with inclusion and exclusion patterns"""
        include_patterns = ["رجل", "امرأة"]
        exclude_patterns = []
        
        count = self.counter.count_with_exclusions(include_patterns, exclude_patterns)
        self.assertGreater(count, 0)

class TestMiraclePatternVerifier(unittest.TestCase):
    """Test the miracle pattern verification functionality"""
    
    def setUp(self):
        # Create a processor with controlled test data
        self.processor = QuranTextProcessor()
        
        # Create test verses that should produce known counts
        # This is simplified test data - real data would have proper Arabic
        test_verses = {}
        
        # Generate 23 instances each of man/woman for testing
        for i in range(23):
            test_verses[(i+1, 1)] = "رجل"  # man
            test_verses[(i+1, 2)] = "امرأة"  # woman
        
        # Generate some life/death instances (simplified)
        for i in range(10):
            test_verses[(i+50, 1)] = "الحياة"  # life
            test_verses[(i+50, 2)] = "الموت"   # death
        
        self.processor.verses = test_verses
        self.counter = ArabicWordCounter(self.processor)
        self.verifier = MiraclePatternVerifier(self.counter)
    
    def test_man_woman_verification_structure(self):
        """Test the man/woman verification returns proper structure"""
        result = self.verifier.verify_man_woman_23_23()
        
        # Check all required fields are present
        required_fields = [
            'man_count', 'woman_count', 'matches_23_23', 
            'difference', 'ratio', 'biological_significance'
        ]
        
        for field in required_fields:
            self.assertIn(field, result)
        
        # Check data types
        self.assertIsInstance(result['man_count'], int)
        self.assertIsInstance(result['woman_count'], int)
        self.assertIsInstance(result['matches_23_23'], bool)
        self.assertIsInstance(result['difference'], int)
    
    def test_life_death_verification_structure(self):
        """Test the life/death verification returns proper structure"""
        result = self.verifier.verify_life_death_145_145()
        
        required_fields = [
            'life_count', 'death_count', 'matches_145_145',
            'difference', 'ratio', 'quranic_reference'
        ]
        
        for field in required_fields:
            self.assertIn(field, result)
    
    def test_calendar_verification_structure(self):
        """Test the calendar verification returns proper structure"""
        result = self.verifier.verify_days_months_365_30_12()
        
        required_fields = [
            'day_singular_count', 'days_plural_count', 'month_singular_count',
            'matches_365_30_12', 'solar_year_match', 'lunar_month_match',
            'calendar_months_match', 'joint_probability'
        ]
        
        for field in required_fields:
            self.assertIn(field, result)
    
    def test_run_all_verifications(self):
        """Test running all verifications together"""
        results = self.verifier.run_all_verifications()
        
        # Check that all expected patterns are included
        expected_patterns = [
            'man_woman_23_23', 'life_death_145_145', 'days_months_365_30_12',
            'land_sea_ratio', 'angels_devils_88_88', 'belief_disbelief_25_25',
            'hot_cold_4_4', 'rasul_prophets_513_513'
        ]
        
        for pattern in expected_patterns:
            self.assertIn(pattern, results)
        
        # Check that each result is a dictionary
        for pattern, result in results.items():
            self.assertIsInstance(result, dict)
            self.assertGreater(len(result), 0)

class TestMiracleVerifierCLI(unittest.TestCase):
    """Test the command-line interface functionality"""
    
    def setUp(self):
        self.cli = MiracleVerifierCLI()
    
    def test_cli_initialization(self):
        """Test that CLI initializes properly"""
        self.assertIsNotNone(self.cli.processor)
        self.assertIsNotNone(self.cli.counter)
        self.assertIsNotNone(self.cli.verifier)
    
    def test_print_results_format(self):
        """Test that results printing doesn't crash"""
        # Create mock results
        mock_results = {
            'test_pattern': {
                'count': 10,
                'matches_test': True,
                'ratio': 1.0,
                'description': 'Test pattern'
            }
        }
        
        # This should not raise any exceptions
        try:
            self.cli.print_results(mock_results)
            success = True
        except Exception as e:
            success = False
            print(f"Print results failed: {e}")
        
        self.assertTrue(success, "Print results should not raise exceptions")

class TestIntegration(unittest.TestCase):
    """Integration tests for the complete system"""
    
    def test_full_pipeline(self):
        """Test the complete pipeline from text loading to verification"""
        try:
            # Initialize the complete system
            processor = QuranTextProcessor()
            counter = ArabicWordCounter(processor)
            verifier = MiraclePatternVerifier(counter)
            cli = MiracleVerifierCLI()
            
            # Run a single verification to test the pipeline
            result = verifier.verify_man_woman_23_23()
            
            # Should complete without errors and return a dictionary
            self.assertIsInstance(result, dict)
            self.assertGreater(len(result), 0)
            
        except Exception as e:
            self.fail(f"Full pipeline test failed with error: {e}")
    
    def test_data_loading_fallback(self):
        """Test that the system gracefully handles missing data files"""
        processor = QuranTextProcessor()
        
        # Should have some verses loaded (either real data or sample data)
        self.assertGreater(len(processor.verses), 0)
        
        # Should have the basic sample verses
        verse_1_1 = processor.get_verse(1, 1)
        self.assertIsNotNone(verse_1_1)

def run_performance_tests():
    """Run basic performance tests"""
    print("\n" + "="*60)
    print("PERFORMANCE TESTS")
    print("="*60)
    
    import time
    
    # Test text processing performance
    processor = QuranTextProcessor()
    start_time = time.time()
    
    # Process all loaded verses
    total_tokens = 0
    for verse_text in processor.verses.values():
        tokens = processor.tokenize(verse_text)
        total_tokens += len(tokens)
    
    processing_time = time.time() - start_time
    print(f"INFO: Processed {len(processor.verses)} verses ({total_tokens} tokens) in {processing_time:.3f}s")
    
    # Test verification performance
    counter = ArabicWordCounter(processor)
    verifier = MiraclePatternVerifier(counter)
    
    start_time = time.time()
    result = verifier.verify_man_woman_23_23()
    verification_time = time.time() - start_time
    
    print(f"INFO: Single pattern verification: {verification_time:.3f}s")
    
    # Test all verifications
    start_time = time.time()
    all_results = verifier.run_all_verifications()
    all_time = time.time() - start_time
    
    print(f"INFO: All 8 pattern verifications: {all_time:.3f}s")
    print(f"INFO: Average per pattern: {all_time/8:.3f}s")

def main():
    """Main test runner"""
    print("QURAN MIRACLE VERIFIER - TEST SUITE")
    print("="*60)
    
    # Run the unit tests
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add all test classes
    test_classes = [
        TestQuranTextProcessor,
        TestArabicWordCounter, 
        TestMiraclePatternVerifier,
        TestMiracleVerifierCLI,
        TestIntegration
    ]
    
    for test_class in test_classes:
        tests = loader.loadTestsFromTestCase(test_class)
        suite.addTests(tests)
    
    # Run the tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Run performance tests
    run_performance_tests()
    
    # Print summary
    print("\n" + "="*60)
    print("TEST SUMMARY")
    print("="*60)
    print(f"Tests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    
    if result.failures:
        print("\nFAILURES:")
        for test, failure in result.failures:
            print(f"- {test}: {failure}")
    
    if result.errors:
        print("\nERRORS:")  
        for test, error in result.errors:
            print(f"- {test}: {error}")
    
    # Return exit code
    if result.failures or result.errors:
        print("\nERROR: Some tests failed")
        return 1
    else:
        print("\nSUCCESS: All tests passed!")
        return 0

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)