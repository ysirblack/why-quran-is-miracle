# Two Prime Divisors Pattern

**Source:** Simetrik Kitap: Kur'an

---

## Definition

**Two Prime Divisors:** A number n has exactly 2 prime numbers in its divisor set.

**Note:** This book considers 1 as prime.

Examples:
- 2 has divisors {1, 2}, primes in set = {1, 2} = 2 primes ✓
- 4 has divisors {1, 2, 4}, primes in set = {1, 2} = 2 primes ✓
- 6 has divisors {1, 2, 3, 6}, primes in set = {1, 2, 3} = 3 primes ✗
- 9 has divisors {1, 3, 9}, primes in set = {1, 3} = 2 primes ✓

---

## The Pattern

| Category | First Half (1-57) | Second Half (58-114) |
|----------|-------------------|----------------------|
| Homogeneous | 24 | 24 |
| Heterogeneous | 33 | 33 |

---

## Symmetry

- **Homogeneous:** Equal split 24/24
- **Heterogeneous:** Equal split 33/33
- Both categories perfectly balanced between halves!

---

## Verification

```bash
python3 verify.py
```

---

## Statistics

- **Method:** Permutation test (100,000 trials)
- **p-value:** 0.143
- **Significant (p<0.05):** No

The observed 24/24/33/33 symmetry occurs with reasonable frequency in random arrangements.
