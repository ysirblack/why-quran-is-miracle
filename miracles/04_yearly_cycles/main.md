# Yearly Cycles: Solar & Hijri Calendar Alignment

## Summary

The Qur'an contains 478 tokens with the root **يوم (yawm / "day")**. Different morphological filters yield both solar and lunar calendar constants from the SAME token pool:

| Pattern | Count | Verified |
|---------|-------|----------|
| Solar year | 274 + 75 + 16 = **365** | YES |
| Hijri year | 274 + 70 + 5 + 5 = **354** | YES |
| Calendar months | **12** | YES |
| Hijri month | 26 + 3 = **29** | YES |

## Token Breakdown

```
All 478 tokens:
├── simple (يوم):        274  ← SHARED by solar & hijri
├── definite (اليوم):     75  ← Solar only
├── tanwīn (يوماً):       16  ← Solar only
├── "that day" (يومئذ):   70  ← Hijri only
├── "their day" (يومهم):   5  ← Hijri only
├── "your day" (يومكم):    5  ← Hijri only
├── plural (أيام):        26  ← Lunar month
├── dual (يومين):          3  ← Lunar month
└── excluded:              4
```

## Statistics

**Combined probability (bootstrap)**: ~1 in 2,500 to 7,000

**Our threshold**: p < 0.05 (5%)

**Passes threshold**: YES

## Verification

```bash
python3 miracles/04_yearly_cycles/solar_365/day_365_verifier.py
python3 miracles/04_yearly_cycles/hijri_354/hijri_354_combined.py
python3 miracles/04_yearly_cycles/bootstrap_probability_analysis.py
```

**Data source**: Tanzil Ḥafṣ/Uthmānī

**Cross-verified with**: Quranic Arabic Corpus
