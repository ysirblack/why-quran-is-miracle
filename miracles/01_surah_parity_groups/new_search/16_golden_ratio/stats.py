#!/usr/bin/env python3
"""Statistical test for pattern 16: Golden Ratio 7906/4885 ≈ φ

Optimized with multiprocessing (all CPU cores). No external dependencies.
"""
import random
from pathlib import Path
from collections import Counter
from multiprocessing import Pool, cpu_count

N_TRIALS = 100_000_000  # 100M trials — statistically robust, finishes in minutes
PHI = 1.6180339887

def load_quran_data():
    current_dir = Path(__file__).parent
    for _ in range(6):
        potential_path = current_dir / "data" / "quran-uthmani.txt"
        if potential_path.exists():
            break
        current_dir = current_dir.parent
    verses = {}
    with potential_path.open('r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#') or '|' not in line:
                continue
            parts = line.split('|', 2)
            if len(parts) >= 3:
                surah = int(parts[0])
                verses.setdefault(surah, []).append(int(parts[1]))
    return {s: len(v) for s, v in verses.items()}

def calc_score(positions, verses):
    sums = [p + v for p, v in zip(positions, verses)]
    sum_counts = Counter(sums)
    sum_repeated = sum(s for s in sums if sum_counts[s] > 1)
    sum_unique = sum(s for s in sums if sum_counts[s] == 1)
    if sum_unique == 0:
        return float('inf')
    ratio = sum_repeated / sum_unique
    return abs(ratio - PHI)

# Precomputed as module-level for workers (set in main, read by workers)
_positions = None
_verses = None
_observed = None

def _init_worker(positions, verses, observed):
    global _positions, _verses, _observed
    _positions = positions
    _verses = verses
    _observed = observed

def worker(args):
    """Worker function: run n_trials shuffles and count hits."""
    n_trials, seed = args
    rng = random.Random(seed)
    count = 0
    verses = list(_verses)
    positions = _positions
    for _ in range(n_trials):
        rng.shuffle(verses)
        if calc_score(positions, verses) <= _observed:
            count += 1
    return count

def main():
    vc = load_quran_data()
    positions = list(range(1, 115))
    verses = [vc[s] for s in positions]

    observed = calc_score(positions, verses)
    print(f"Observed deviation from φ: {observed:.10f}")

    n_cores = cpu_count()
    print(f"Using {n_cores} CPU cores, {N_TRIALS:,} total trials")

    # Split trials across cores
    trials_per_core = N_TRIALS // n_cores
    remainder = N_TRIALS % n_cores
    tasks = []
    for i in range(n_cores):
        n = trials_per_core + (1 if i < remainder else 0)
        tasks.append((n, 42 + i))

    with Pool(n_cores, initializer=_init_worker,
              initargs=(positions, verses, observed)) as pool:
        results = pool.map(worker, tasks)

    total_count = sum(results)
    p = total_count / N_TRIALS
    print(f"\nTrials: {N_TRIALS:,}")
    print(f"Matches: {total_count:,}")
    print(f"p-value: {p:.8f}")
    print(f"Significant (p<0.05): {'YES' if p < 0.05 else 'NO'}")

if __name__ == "__main__":
    main()
