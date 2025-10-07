#!/usr/bin/env python3
"""Complete Hijri 354 lunar calendar pattern verification using imported functions"""

from count_yevm_only import count_yevm_only
from count_yevmeizin_only import count_yevmeizin_only  
from count_yevmuhum_only import count_yevmuhum_only
from count_yevmekum_only import count_yevmekum_only

def verify_hijri_354_complete():
    print("HIJRI 354 LUNAR CALENDAR PATTERN VERIFICATION")
    print("=" * 60)
    
    # Get individual counts using proven working functions
    yevm_count = count_yevm_only()
    print()
    yevmeizin_count = count_yevmeizin_only()
    print()
    yevmuhum_count = count_yevmuhum_only()
    print()
    yevmekum_count = count_yevmekum_only()
    
    print("\n" + "=" * 60)
    print("FINAL HIJRI 354 SUMMARY")
    print("=" * 60)
    print(f"1. YEVM (simple day forms):   {yevm_count:3d}")
    print(f"2. YEVMEIZIN (that day):      {yevmeizin_count:3d}") 
    print(f"3. YEVMUHUM (their day):      {yevmuhum_count:3d}")
    print(f"4. YEVMEKUM (your day):       {yevmekum_count:3d}")
    print("-" * 40)
    
    total_count = yevm_count + yevmeizin_count + yevmuhum_count + yevmekum_count
    print(f"TOTAL HIJRI PATTERN:          {total_count:3d}")
    
    # Status check
    all_correct = (yevm_count == 274 and yevmeizin_count == 70 and 
                   yevmuhum_count == 5 and yevmekum_count == 5)
    
    print(f"STATUS: {'HIJRI 354 VERIFIED' if all_correct and total_count == 354 else 'Count: ' + str(total_count)}")
    
    return {
        'yevm': yevm_count,
        'yevmeizin': yevmeizin_count, 
        'yevmuhum': yevmuhum_count,
        'yevmekum': yevmekum_count,
        'total': total_count
    }

if __name__ == "__main__":
    verify_hijri_354_complete()