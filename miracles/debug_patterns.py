#!/usr/bin/env python3
import re

def remove_diacritics(text):
    """Remove Arabic diacritics"""
    diacritics = r'[\u064B-\u065F\u0670\u0640]'
    return re.sub(diacritics, '', text)

def test_patterns():
    # Test with some sample verses from the data
    test_verses = [
        "مَٰلِكِ يَوْمِ ٱلدِّينِ",  # Should contain يوم
        "وَبِٱلْيَوْمِ ٱلْـَٔاخِرِ",  # Should contain اليوم
        "وَٱذْكُرُوا۟ أَيَّامَ ٱللَّهِ",  # Should contain أيام
        "فِى يَوْمَيْنِ"  # Should contain يومين
    ]
    
    patterns = ["يوم", "ٱليوم", "أيام", "يومين"]
    
    for verse in test_verses:
        print(f"Original verse: {verse}")
        clean_verse = remove_diacritics(verse)
        print(f"Clean verse: {clean_verse}")
        
        tokens = verse.split()
        for token in tokens:
            clean_token = remove_diacritics(token)
            print(f"  Token: {token} -> Clean: {clean_token}")
            
            for pattern in patterns:
                if pattern in clean_token or clean_token == pattern:
                    print(f"    MATCH: {pattern}")
        print()

if __name__ == "__main__":
    test_patterns()