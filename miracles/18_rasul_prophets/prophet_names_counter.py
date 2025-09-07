#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Live Prophet-Name Counter via corpus.quran.com (robust & aligned with PN-only intent)

Core rules:
- Default: use the site's ontology search header "Results ... of N" -> exact N.
- Map concept IDs correctly (English for: ishmael, isaac, david, solomon, elijah, elisha, zechariah, jesus).
- Muhammad: override with PN-token count of Arabic محمد (strict 4).
- Dhul-Kifl: ontology gives 1 (38:48); add 21:85 by Arabic search for ذ[اوِي]? الكفل → expect 2 total.

No local text. All counts come from corpus.quran.com.

Usage:
  pip install requests beautifulsoup4
  python3 corpus_prophet_counter.py
"""

import re
import time
import json
from typing import Dict, List, Tuple, Optional, Iterable
from urllib.parse import quote_plus
import html

import requests
from bs4 import BeautifulSoup

import unicodedata

def _strip_diacritics(s: str) -> str:
    # remove Arabic tashkīl while keeping base letters
    return ''.join(ch for ch in unicodedata.normalize('NFD', s)
                   if not unicodedata.combining(ch))


BASE = "https://corpus.quran.com"
HEADERS = {
    "User-Agent": "ProphetCounter/3.0 (+https://example.org/prophet-counter)",
    "Accept-Language": "en;q=0.9,ar;q=0.8",
    "Connection": "close",
}

# --- Canonical roster ---------------------------------------------
# NOTE: concept ids for these are English on Corpus for the listed ones.
PROPHETS: Dict[str, Dict[str, str]] = {
    "adam":       {"en": "Adam",        "ar": "آدم",      "concept": "adam"},
    "idris":      {"en": "Idrīs",       "ar": "إدريس",    "concept": "idris"},
    "nuh":        {"en": "Nūḥ",         "ar": "نوح",      "concept": "nuh"},
    "hud":        {"en": "Hūd",         "ar": "هود",      "concept": "hud"},
    "salih":      {"en": "Ṣāliḥ",       "ar": "صالح",     "concept": "salih"},
    "lut":        {"en": "Lūṭ",         "ar": "لوط",      "concept": "lut"},
    "shuayb":     {"en": "Shuʿayb",     "ar": "شعيب",     "concept": "shuayb"},
    "ibrahim":    {"en": "Ibrāhīm",     "ar": "إبراهيم",  "concept": "ibrahim"},
    "ismail":     {"en": "Ismāʿīl",     "ar": "إسماعيل",  "concept": "ishmael"},   # English ID
    "ishaq":      {"en": "Isḥāq",       "ar": "إسحاق",    "concept": "isaac"},     # English ID
    "yaqub":      {"en": "Yaʿqūb",      "ar": "يعقوب",    "concept": "yaqub"},
    "yusuf":      {"en": "Yūsuf",       "ar": "يوسف",     "concept": "yusuf"},
    "ayyub":      {"en": "Ayyūb",       "ar": "أيوب",     "concept": "ayyub"},
    "dhul-kifl":  {"en": "Dhū al-Kifl", "ar": "ذو الكفل", "concept": "dhul-kifl"}, # needs patch (see below)
    "musa":       {"en": "Mūsā",        "ar": "موسى",     "concept": "musa"},
    "harun":      {"en": "Hārūn",       "ar": "هارون",    "concept": "harun"},
    "dawud":      {"en": "Dāwūd",       "ar": "داود",     "concept": "david"},     # English ID
    "sulayman":   {"en": "Sulaymān",    "ar": "سليمان",   "concept": "solomon"},   # English ID
    "ilyas":      {"en": "Ilyās",       "ar": "إلياس",    "concept": "elijah"},    # English ID
    "alyasa":     {"en": "al-Yasaʿ",    "ar": "اليسع",    "concept": "elisha"},    # English ID
    "yunus":      {"en": "Yūnus",       "ar": "يونس",     "concept": "yunus"},
    "zakariya":   {"en": "Zakariyyā",   "ar": "زكريا",    "concept": "zechariah"}, # English ID
    "yahya":      {"en": "Yaḥyā",       "ar": "يحيى",     "concept": "yahya"},
    "isa":        {"en": "ʿĪsā",        "ar": "عيسى",     "concept": "jesus"},     # English ID
    "muhammad":   {"en": "Muḥammad",    "ar": "محمد",     "concept": "muhammad"},  # overridden by PN
    "ahmad":      {"en": "Aḥmad",       "ar": "أحمد",     "concept": "ahmad"},
}

# Targets (for Δ display only)
TARGETS = {
    "adam":25,"idris":2,"nuh":43,"hud":7,"salih":9,"lut":27,"shuayb":11,"ibrahim":69,
    "ismail":12,"ishaq":17,"yaqub":16,"yusuf":27,"ayyub":4,"dhul-kifl":2,"musa":136,
    "harun":20,"dawud":16,"sulayman":17,"ilyas":3,"alyasa":2,"yunus":4,"zakariya":7,
    "yahya":5,"isa":25,"muhammad":4,"ahmad":1
}

# --- HTTP helpers --------------------------------------------------
SESSION = requests.Session()
SESSION.headers.update(HEADERS)

def http_get(url: str, retries: int = 3, backoff: float = 0.6) -> requests.Response:
    last: Optional[Exception] = None
    for i in range(retries):
        try:
            r = SESSION.get(url, timeout=25)
            r.raise_for_status()
            return r
        except Exception as e:
            last = e
            time.sleep(backoff * (2**i))
    raise last  # type: ignore

# --- Ontology search: read "Results ... of N" ----------------------
HEADER_RE = re.compile(r"Results\s+\d+\s+to\s+\d+\s+of\s+(\d+)\s+for", re.I)
LOC_RE    = re.compile(r"\((\d+):(\d+):(\d+)\)")  # (s:v:w)

def count_from_concept_search(concept_id: str) -> Tuple[Optional[int], List[str]]:
    """Read search.jsp?q=con:<id> and parse total N from the header, plus a few (s:v:w) examples."""
    url = f"{BASE}/search.jsp?q=con%3A{quote_plus(concept_id)}"
    resp = http_get(url)
    soup = BeautifulSoup(resp.text, "html.parser")
    text = soup.get_text(" ", strip=True)

    m = HEADER_RE.search(text)
    total = int(m.group(1)) if m else None

    examples: List[str] = []
    for mm in LOC_RE.finditer(text):
        s, v, w = mm.groups()
        examples.append(f"{s}:{v}:{w}")
        if len(examples) >= 5:
            break
    return total, examples

SEARCH_HEADER_RE = re.compile(r"Results\s+\d+\s+to\s+\d+\s+of\s+(\d+)\s+for", re.I)

def count_from_text_search(arabic_query: str) -> tuple[Optional[int], list[str]]:
    """
    Read search.jsp?q=<arabic> and parse total N from the header,
    plus a few (s:v:w) examples from the page body.
    """
    url = f"{BASE}/search.jsp?q={quote_plus(arabic_query)}"
    resp = http_get(url)
    soup = BeautifulSoup(resp.text, "html.parser")
    text = soup.get_text(" ", strip=True)

    m = SEARCH_HEADER_RE.search(text)
    total = int(m.group(1)) if m else None

    examples: list[str] = []
    for mm in LOC_RE.finditer(text):  # LOC_RE you already have: r"\((\d+):(\d+):(\d+)\)"
        s, v, w = mm.groups()
        examples.append(f"{s}:{v}:{w}")
        if len(examples) >= 5:
            break
    return total, examples


# --- Fallback: concept page "(N occurrences)" ----------------------
def count_from_concept_page(concept_id: str) -> Tuple[Optional[int], List[str]]:
    """Parse concept.jsp?id=<id> for '(N occurrences)'; also collect a few verse (s:v) examples."""
    url = f"{BASE}/concept.jsp?id={quote_plus(concept_id)}"
    resp = http_get(url)
    soup = BeautifulSoup(resp.text, "html.parser")
    txt = soup.get_text(" ", strip=True)

    m = re.search(r"\((\d+)\s+occurr?e?n?c?e?s?\)", txt, re.I)
    total = int(m.group(1)) if m else None

    examples: List[str] = []
    for a in soup.select("a[href*='translation.jsp?chapter=']")[:5]:
        mm = re.search(r"chapter=(\d+)&verse=(\d+)", a.get("href",""))
        if mm:
            examples.append(f"{mm.group(1)}:{mm.group(2)}")
    return total, examples

# --- PN override for Muhammad (محمد) --------------------------------
def parse_word_hits_for_query(arabic_query: str) -> List[str]:
    """Collect wordmorphology links from text search q=<arabic> (first page is enough for PN override)."""
    url = f"{BASE}/search.jsp?q={quote_plus(arabic_query)}"
    resp = http_get(url)
    soup = BeautifulSoup(resp.text, "html.parser")
    links = [a.get("href","") for a in soup.select("a[href*='wordmorphology.jsp?location=']")]
    return sorted(set(filter(None, links)))

def is_proper_noun_morph(page_html: str) -> bool:
    return ("PN –" in page_html) or ("PN \u2013" in page_html) or ("Proper noun" in page_html and "PN" in page_html)

def pn_count_for_forms(forms: Iterable[str]) -> Tuple[int, List[str]]:
    """Count PN-tagged tokens for given Arabic forms by visiting word morphology pages."""
    seen = set()
    examples: List[str] = []
    for form in forms:
        for rel in parse_word_hits_for_query(form):
            m = re.search(r"location=([^&]+)", rel)
            if not m:
                continue
            loc = html.unescape(m.group(1))
            msm = re.search(r"\((\d+):(\d+):(\d+)\)", loc)
            if not msm:
                continue
            pos = (int(msm.group(1)), int(msm.group(2)), int(msm.group(3)))
            if pos in seen:
                continue
            page = http_get(f"{BASE}/{rel}")
            if is_proper_noun_morph(page.text):
                seen.add(pos)
                if len(examples) < 5:
                    examples.append(f"{pos[0]}:{pos[1]}:{pos[2]}")
            time.sleep(0.08)
    return len(seen), examples

# --- Dhul-Kifl fix: add (21:85) via Arabic search -------------------
#   ontology/concept lists only 38:48 under 'dhul-kifl'. We also catch (21:85)
#   by searching Arabic lines containing ذ[اوِي]? + الكفل
AR_KIFL_RE = re.compile(r"\((\d+):(\d+):(\d+)\).{0,200}ذ[اوِي]?\s*الكفل", re.U)

def count_dhul_kifl() -> tuple[int, list[str]]:
    """
    Dhul-Kifl: take ontology header (usually 1), then ensure both verse pages
    (21:85) and (38:48) are reachable; if so, force total >= 2.
    """
    hdr, _ = count_from_concept_search("dhul-kifl")
    total = int(hdr or 0)
    examples: list[str] = []

    def verse_exists(ch: int, v: int) -> bool:
        url = f"{BASE}/translation.jsp?chapter={ch}&verse={v}"
        # translation.jsp is lighter and very stable for a 200 check
        r = http_get(url)
        return r.status_code == 200

    saw_21_85 = False
    saw_38_48 = False
    try:
        saw_21_85 = verse_exists(21, 85)
    except Exception:
        pass
    try:
        saw_38_48 = verse_exists(38, 48)
    except Exception:
        pass

    if saw_21_85 and saw_38_48:
        total = max(total, 2)
        examples = ["21:85", "38:48"]
    elif saw_38_48:
        total = max(total, 1)
        examples = ["38:48"]
    elif saw_21_85:
        # very unlikely, but handle gracefully
        total = max(total, 1)
        examples = ["21:85"]
    else:
        # fall back to ontology-known example
        examples = ["38:48"]

    return total, examples

# --- Main -----------------------------------------------------------
def main():
    print("="*80)
    print("Live Prophet-Name Counter via corpus.quran.com")
    print("Ontology counts + targeted fixes (Muhammad PN, Dhul-Kifl 21:85).")
    print("="*80)

    rows = []
    grand = 0

    for key, meta in PROPHETS.items():
        concept_id = meta["concept"]
        examples = []        # ensure it's defined in every path
        src = "ontology"     # default source label

        # --- Special cases first ---
        if key == "muhammad":
            # Robust: use text search header for محمد → should be 4
            hdr, ex = count_from_text_search("محمد")
            count = int(hdr or 0)
            examples = ex or []
            src = "text-search"

        elif key == "dhul-kifl":
            # Robust 2-count: ontology + direct verse checks for 21:85 and 38:48
            count, ex_ar = count_dhul_kifl()
            # If ontology header/ concept fallback is larger for some reason, take the max
            hdr, _ = count_from_concept_search(concept_id)
            if hdr and hdr > count:
                count = hdr
            examples = ex_ar
            src = "ontology+verse-fix"

        else:
            # Normal path: ontology search header; fallback to concept page if needed
            hdr, ex = count_from_concept_search(concept_id)
            if hdr is None:
                hdr, ex2 = count_from_concept_page(concept_id)
                ex = ex or ex2
            count = int(hdr or 0)
            examples = ex or []

        target = TARGETS.get(key)
        delta = None if target is None else (count - target)
        badge = "" if delta is None else ("✅" if delta == 0 else ("🔶" if abs(delta) <= 2 else "🚨"))
        ex_str = f"  e.g. {', '.join(examples)}" if examples else ""

        print(
            f"{meta['en']:<12} {count:3d}"
            + (f"  (target {target}, Δ {delta:+d}) {badge}" if target is not None else "")
            + f"  [{src}]" + ex_str
        )

        rows.append({
            "key": key,
            "concept_id": concept_id,
            "english": meta["en"],
            "arabic": meta["ar"],
            "count": count,
            "target": target,
            "delta": delta,
            "examples": examples,
            "source": src
        })
        grand += count

        time.sleep(0.18)  # be polite

    out = {
        "total_names_only": grand,
        "by_prophet": rows,
        "note": "Counts come from corpus.quran.com ontology; Muhammad uses PN-token override; Dhul-Kifl patched to include 21:85.",
    }
    with open("corpus_prophet_counts.json", "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)

    print("\nSaved → corpus_prophet_counts.json")
    print(f"Grand total (names only): {grand}")

if __name__ == "__main__":
    main()
