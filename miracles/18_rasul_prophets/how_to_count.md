# Scope & Principles

- **Scope (26 names):** Ādam, Idrīs, Nūḥ, Hūd, Ṣāliḥ, Lūṭ, Shuʿayb, Ibrāhīm, Ismāʿīl, Isḥāq, Yaʿqūb, Yūsuf, Ayyūb, Dhū al-Kifl, Mūsā, Hārūn, Dāwūd, Sulaymān, Ilyās, al-Yasaʿ, Yūnus, Zakariyyā, Yaḥyā, ʿĪsā, Muḥammad, Aḥmad.
- **Counting rule:** count **only proper-name tokens** (i.e., the word is used as a person’s name in that verse). Do **not** count common adjectives/titles or other senses.
- **Primary source:** Quranic Arabic Corpus (morphology + ontology). It exposes proper-noun tags and concept pages, which let you separate name-uses from generic word-uses. ([Quranic Arabic Corpus][1])

# One-Minute Quickstart (Manual)

1. Open the **Quranic Arabic Corpus → Ontology → Prophet** list (contains the named figures we need). ([Quranic Arabic Corpus][2])
2. Click a prophet (e.g., _Nūḥ_) to open their **concept page**. Use the **“Verse list (N occurrences)”** number there as the **proper-name count**. (This list already excludes non-name uses.) ([Quranic Arabic Corpus][3])
3. Repeat for all 26 names.
4. Apply the **edge-case rules** below (e.g., normalize _Ilyās/Il Yāsīn_, exclude _al-Masīḥ_ as a title, etc.). Where a concept page is incomplete or ambiguous, confirm with a **lemma + POS search** that filters to proper nouns (examples below).

# Disambiguation & Normalization Rules (Critical)

These keep the counts **name-only** and consistent across editions.

1. **Ṣāliḥ (صالح)**

   - Two senses exist: **the name** (Prophet Ṣāliḥ) vs **the adjective** “righteous/ صالح”. Count **only** when tagged/treated as the **proper name** on the concept/verse pages. (The concept’s verse list gives the name-use total.)

2. **Ilyās (إلياس) / Ilyāsīn (إلياسين)**

   - Qur’an has a morphological variant in **37:130**. Normalize **both** to _Ilyās_ and count them together. You can verify 3 proper-name tokens via a lemma+POS search (see the sample query below). ([Quranic Arabic Corpus][4])

3. **Isrāʾīl (إسرائيل)**

   - An epithet for **Yaʿqūb**; do **not** add as a separate prophet. If you’re doing person-centric analysis you may map _Isrāʾīl_ tokens to **Yaʿqūb**; for a **name-token** census, keep _Isrāʾīl_ **excluded** from the 26-name list.

4. **ʿĪsā (Jesus) vs _al-Masīḥ_ (the Messiah)**

   - **Count only “ʿĪsā”** as the personal name. **Exclude** the title _al-Masīḥ_ from name counts.

5. **Muḥammad vs Aḥmad**

   - **Both are proper names** of the Prophet ﷺ (Aḥmad occurs once at 61:6). Count them separately as **distinct name tokens**.

6. **Dhū al-Kifl (ذو الكفل)**

   - Occurs twice (21:85; 38:48). Morphologically appears with **dhū/ḏū** + **al-kifl**. Confirm on the concept page and the two verses if needed. ([Quranic Arabic Corpus][5])

7. **Orthography variants**

   - Accept all standard spellings: e.g., **Dāwūd** appears as داود (sometimes داوود), **Hārūn** as هارون, etc. Ontology + lemma search will unify them.

# How to Verify with POS-Filtered Search (When Needed)

If a concept page looks incomplete or you want to double-check, run a **lemma + POS** query that restricts to **proper nouns** (POS = `pn`). Example for **Ilyās**:

- Search: **lemma = إلياس / إلياسين, POS = proper noun**
  The site’s search returns **3** results and shows each verse: 6:85, 37:123, 37:130. ([Quranic Arabic Corpus][6])

For any prophet, use:

- Open **Search → “Search for words”** and set **POS = pn** (proper noun), plus a suitable **lemma** (or use the concept page’s verse list first, then confirm specific verses from there).

# Standard Operating Procedure (SOP)

1. **Prepare the roster (26 names)** from the Ontology → Prophet list. Confirm exclusions: Luqmān, Dhū l-Qarnayn, ʿUzayr, Ṭālūt, etc. are **not** counted as prophets here (per the ontology categories). ([Quranic Arabic Corpus][2])
2. **For each name**, open the **concept page** and record the **“Verse list (N occurrences)”** as the **proper-name count**.
3. **Apply normalization**:

   - Merge **Ilyās + Ilyāsīn** under _Ilyās_ (step 2 total should already reflect this; if not, confirm via POS search). ([Quranic Arabic Corpus][4])
   - Keep **Muḥammad** and **Aḥmad** as **separate rows**.
   - **Exclude** non-name senses: _ṣāliḥ_ = righteous (adjective), _al-Masīḥ_ = title.
   - Do **not** add _Isrāʾīl_ as a new prophet.

4. **Record results** in a table with columns: `index | English | Arabic | count | evidence` (paste the concept page title or note “concept verse list”).
5. **Sum the counts** for the **grand total** (should equal **511** with the corpus settings described).
6. **Spot-check edge verses**:

   - **Dhū al-Kifl**: verify **21:85** and **38:48** pages. ([Quranic Arabic Corpus][7])
   - **Ilyāsīn** form at **37:130**: confirm it’s tagged as a **proper noun**. ([Quranic Arabic Corpus][8])

# Example: Full Walkthrough for One Name

**Prophet:** Yūnus (يونس)
**Step A:** Ontology → Prophet → _Yunus_ concept page → read “Verse list (N occurrences)” → **4**.
**Step B (optional cross-check):** Search by lemma `يونس` with **POS = pn** and confirm the same four verses are listed.
**Write-down:** `Yūnus | يونس | 4 | concept verse list`

# Quality-Assurance Checklist

- ✅ **Proper-name only:** Every count comes from a concept **verse list** or a **POS=pn** filtered search.
- ✅ **Variants normalized:** _Ilyās/Ilyāsīn_ merged; spelling variants (داود/داوود) unified by lemma. ([Quranic Arabic Corpus][4])
- ✅ **Titles excluded:** _al-Masīḥ_ not counted; _Isrāʾīl_ handled as Jacob’s epithet if needed, but not added as a separate name. ([Quranic Arabic Corpus][2])
- ✅ **Edge cases checked:** _Dhū al-Kifl_ verified at **21:85** and **38:48**. ([Quranic Arabic Corpus][7])
- ✅ **Grand total match:** Sum equals **511**.

# Why this is Reproducible

- It uses **explicit morphological tags** (proper noun = PN) and/or the **Ontology’s verse lists**, both of which are deterministic on the site. ([Quranic Arabic Corpus][1])
- Every exception is captured by small, auditable rules (titles vs names, adjectives vs names, variant spellings normalized by lemma).

# Optional: Minimal Data Schema (if you log results)

```text
prophet_en, prophet_ar, count, evidence
Adam, آدم, 25, "concept verse list"
…
Muhammad, محمد, 4, "concept verse list"
Ahmad, أحمد, 1, "concept verse list"
TOTAL,,511,
```

# Troubleshooting Deltas

- **Your total ≠ 511?**

  - Re-check **Ṣāliḥ** entries (adjective vs name).
  - Ensure **Ilyāsīn (37:130)** is **included** with Ilyās. ([Quranic Arabic Corpus][4])
  - Make sure you **excluded titles** (e.g., _al-Masīḥ_) and **didn’t add Isrāʾīl** as a new prophet. ([Quranic Arabic Corpus][2])
  - If a concept page looks off, **confirm with POS=pn search**.

# References (for auditors)

- Quranic Arabic Corpus — homepage and ontology docs. ([Quranic Arabic Corpus][1])
- Ontology → **Prophet** list (source roster + exclusions like _Messiah_, _Israel_). ([Quranic Arabic Corpus][2])
- Edge-case proofs: **Ilyāsīn 37:130** proper-noun tagging; **Dhū al-Kifl** verses 21:85 & 38:48. ([Quranic Arabic Corpus][8])

---

If you want, I can also package this into a tiny checklist PDF or a CSV template you can hand to anyone on your team so they can replicate the 511 without context.

[1]: https://corpus.quran.com/?utm_source=chatgpt.com "The Quranic Arabic Corpus - Word by Word Grammar, Syntax ..."
[2]: https://corpus.quran.com/concept.jsp?id=prophet&utm_source=chatgpt.com "Prophet - Ontology of Quranic Concepts from ..."
[3]: https://corpus.quran.com/concept.jsp?id=nuh&utm_source=chatgpt.com "Nuh - Ontology of Quranic Concepts from ..."
[4]: https://corpus.quran.com/translation.jsp?chapter=37&verse=130&utm_source=chatgpt.com "Verse (37:130) - English Translation"
[5]: https://corpus.quran.com/concept.jsp?id=dhul-kifl&utm_source=chatgpt.com "Dhul Kifl - Ontology of Quranic Concepts from ..."
[6]: https://corpus.quran.com/search.jsp?q=lem%3A%3CiloyaAs+pos%3Apn&utm_source=chatgpt.com "The Quranic Arabic Corpus - Quran Search"
[7]: https://corpus.quran.com/translation.jsp?chapter=21&verse=85&utm_source=chatgpt.com "Verse (21:85) - English Translation"
[8]: https://corpus.quran.com/wordmorphology.jsp?location=%2837%3A130%3A3%29&utm_source=chatgpt.com "Verse (37:130), Word 3 - Quranic Grammar"

Here’s the full, **proper-name only** count for each prophet, plus the grand total.

|   # | Prophet (EN)            | Arabic          | Count |
| --: | ----------------------- | --------------- | ----: |
|   1 | Adam                    | آدم             |    25 |
|   2 | Idrīs                   | إدريس           |     2 |
|   3 | Nūḥ                     | نوح             |    43 |
|   4 | Hūd                     | هود             |     7 |
|   5 | Ṣāliḥ                   | صالح            |     9 |
|   6 | Lūṭ                     | لوط             |    27 |
|   7 | Shuʿayb                 | شعيب            |    11 |
|   8 | Ibrāhīm                 | إبراهيم         |    69 |
|   9 | Ismāʿīl                 | إسماعيل         |    12 |
|  10 | Isḥāq                   | إسحاق           |    17 |
|  11 | Yaʿqūb                  | يعقوب           |    16 |
|  12 | Yūsuf                   | يوسف            |    27 |
|  13 | Ayyūb                   | أيوب            |     4 |
|  14 | Dhū al-Kifl             | ذو الكفل        |     2 |
|  15 | Mūsā                    | موسى            |   136 |
|  16 | Hārūn                   | هارون           |    20 |
|  17 | Dāwūd                   | داود            |    16 |
|  18 | Sulaymān                | سليمان          |    17 |
|  19 | Ilyās _(incl. Ilyāsīn)_ | إلياس / إلياسين |     3 |
|  20 | al-Yasaʿ                | اليسع           |     2 |
|  21 | Yūnus                   | يونس            |     4 |
|  22 | Zakariyyā               | زكريا           |     7 |
|  23 | Yaḥyā                   | يحيى            |     5 |
|  24 | ʿĪsā                    | عيسى            |    25 |
|  25 | Muḥammad                | محمد            |     4 |
|  26 | Aḥmad                   | أحمد            |     1 |

**Grand total (all prophet name tokens): 511**
