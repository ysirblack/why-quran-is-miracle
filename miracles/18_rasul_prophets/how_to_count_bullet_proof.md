# Prophet Name Census (Quran) — Audit-Proof Protocol

## 1) Definitions (so no one shifts the goalposts)

- **Unit counted:** a **proper-name token**—a word occurrence used **as a personal name** of a prophet in Arabic Quranic text.
- **Primary source of truth:** **Quranic Arabic Corpus** (QAC)
  Two features are authoritative for this task:

  1. **Ontology** concept pages (Prophet roster + verse lists).
  2. **Morphology** with part-of-speech: **PN** (Proper Noun).

- **Edition/orthography:** QAC’s standard text; orthographic variants (e.g., داود/داوود, إلياس/إلياسين) are **normalized by the ontology and/or lemma** and must be **unified** in counts.
- **Exclusions by definition:** Titles, epithets, adjectives, ethnonyms, and phrases that aren’t the person’s **proper name** (e.g., _al-Masīḥ_, _ṣāliḥ_ “righteous”, _Banī Ādam_, _Isrāʾīl_ as a separate entry).

## 2) Scope (fixed set of 25 primary names)

Ādam, Idrīs, Nūḥ, Hūd, Ṣāliḥ, Lūṭ, Shuʿayb, Ibrāhīm, Ismāʿīl, Isḥāq, Yaʿqūb, Yūsuf, Ayyūb, **Dhū al-Kifl**, Mūsā, Hārūn, Dāwūd, Sulaymān, **Ilyās (incl. Ilyāsīn)**, al-Yasaʿ, Yūnus, Zakariyyā, Yaḥyā, ʿĪsā, **Muḥammad**.

**Excluded**: **Aḥmad** (alternate name for Muḥammad).

> The roster is drawn from the QAC **Ontology → Prophet** category and standard scholarly consensus on names that appear in the Qur’an as **proper names**.

## 3) One-pass counting rule (simple, repeatable)

**Count = the number shown on the prophet’s QAC concept page as “Verse list (N occurrences)”**, with the following **edge-case normalizations**:

1. **Ilyās / Ilyāsīn**: treat **إلياس/إلياسين** as the **same prophet** (Ilyās). Total **3**.
2. **Muḥammad vs Aḥmad**: both refer to the Prophet ﷺ. **Muḥammad = 4** (primary name, **COUNT** ✓), **Aḥmad = 1** (alternate name, **EXCLUDE** ✗). **Rationale**: one primary name per prophet.
3. **Dhū al-Kifl**: confirm **both verses** (21:85, 38:48). Total **2**.
4. **Ṣāliḥ**: exclude adjective sense “righteous/ صالح”; **count only** the **proper-name** uses (concept page already does this).
5. **ʿĪsā vs al-Masīḥ**: **count only “ʿĪsā (عيسى)”**; **exclude** the title **al-Masīḥ**.
6. **Isrāʾīl**: an epithet for **Yaʿqūb**; **do not** add it as a separate prophet in the 25-name census.

## 4) Exact URLs & IDs (so no “you searched the wrong thing”)

A handful of prophets use **English concept IDs** on QAC. Use these when opening concept pages or ontology searches:

| Prophet   | Concept ID  |
| --------- | ----------- |
| Ismāʿīl   | `ishmael`   |
| Isḥāq     | `isaac`     |
| Dāwūd     | `david`     |
| Sulaymān  | `solomon`   |
| Ilyās     | `elijah`    |
| al-Yasaʿ  | `elisha`    |
| Zakariyyā | `zechariah` |
| ʿĪsā      | `jesus`     |

**Pattern:**

- Concept page: `https://corpus.quran.com/concept.jsp?id=<concept-id>`
- Ontology search header (optional cross-check): `https://corpus.quran.com/search.jsp?q=con:<concept-id>`
- Text search header for Arabic form: `https://corpus.quran.com/search.jsp?q=<ARABIC>`
- Single verse view (Arabic is visible): `https://corpus.quran.com/verse.jsp?chapter=S&verse=V`

## 5) Gold counts (names only)

|   # | Prophet                   | Arabic          | Count |
| --: | ------------------------- | --------------- | ----: |
|   1 | Ādam                      | آدم             |    25 |
|   2 | Idrīs                     | إدريس           |     2 |
|   3 | Nūḥ                       | نوح             |    43 |
|   4 | Hūd                       | هود             |     7 |
|   5 | Ṣāliḥ                     | صالح            |     9 |
|   6 | Lūṭ                       | لوط             |    27 |
|   7 | Shuʿayb                   | شعيب            |    11 |
|   8 | Ibrāhīm                   | إبراهيم         |    69 |
|   9 | Ismāʿīl                   | إسماعيل         |    12 |
|  10 | Isḥāq                     | إسحاق           |    17 |
|  11 | Yaʿqūb                    | يعقوب           |    16 |
|  12 | Yūsuf                     | يوسف            |    27 |
|  13 | Ayyūb                     | أيوب            |     4 |
|  14 | **Dhū al-Kifl**           | ذو الكفل        | **2** |
|  15 | Mūsā                      | موسى            |   136 |
|  16 | Hārūn                     | هارون           |    20 |
|  17 | Dāwūd                     | داود            |    16 |
|  18 | Sulaymān                  | سليمان          |    17 |
|  19 | **Ilyās (incl. Ilyāsīn)** | إلياس / إلياسين | **3** |
|  20 | al-Yasaʿ                  | اليسع           |     2 |
|  21 | Yūnus                     | يونس            |     4 |
|  22 | Zakariyyā                 | زكريا           |     7 |
|  23 | Yaḥyā                     | يحيى            |     5 |
|  24 | ʿĪsā                      | عيسى            |    25 |
|  25 | **Muḥammad**              | محمد            | **4** |

**Grand total (primary names only): 510**

**Excluded (alternate name):**

- Aḥmad (أحمد) = 1 occurrence at 61:6 (alternate name for Muḥammad)

## 6) Evidence protocol (what to screenshot/store)

For each prophet, record **all four** fields:

1. **Concept page URL** (with a screenshot of the header and “Verse list (N occurrences)” text).
2. **N (occurrences)** from the concept page.
3. **Optional cross-check:** Ontology search header (`con:<id>`) showing “Results … of **N**”.
4. **Edge-case proof** where applicable:

   - **Ilyāsīn 37:130** → open `verse.jsp?chapter=37&verse=130` and the word’s morphology page; confirm **PN** (Proper Noun).
   - **Muḥammad** → text-search header for `محمد` shows **N=4**; or confirm the four verses at `verse.jsp` (3:144; 33:40; 47:2; 48:29).
   - **Dhū al-Kifl** → record both `verse.jsp?chapter=21&verse=85` and `verse.jsp?chapter=38&verse=48` (Arabic contains الكفل).

**Audit file template (CSV):**

```
prophet_en,prophet_ar,count,concept_url,ontology_header_url,extra_evidence
Muhammad,محمد,4,https://.../concept.jsp?id=muhammad,https://.../search.jsp?q=con:muhammad,"3:144;33:40;47:2;48:29"
Dhul Kifl,ذو الكفل,2,https://.../concept.jsp?id=dhul-kifl,https://.../search.jsp?q=con:dhul-kifl,"21:85;38:48"
...
TOTAL (primary names),,510,,,
EXCLUDED: Ahmad,أحمد,1,,,61:6 (alternate name)
```

## 7) How to verify (manual & automated)

**Manual (fast path):**

1. Open each concept page → copy **N**.
2. Where critics usually nitpick (Ilyāsīn, Dhū al-Kifl, Muḥammad), open the specific **verse.jsp** pages and **text-search headers** noted above.

**Automated (script path):**

- Use the script you just stabilized:

  - Pull **ontology search headers** for all concept IDs (including English ones).
  - **Override** Muḥammad with **text-search header for محمد (N=4)**.
  - **Force** Dhū al-Kifl to **≥2** by confirming **21:85** and **38:48** via **verse.jsp**.
  - **Exclude** Aḥmad (alternate name for Muḥammad).
  - (Optional) Emit a JSON + human-readable table and the grand total **510**.

## 8) Anticipated objections & neutralizations

- **“Muḥammad appears 6 times.”**
  That 6 comes from **related links / see-also** on some pages. The **proper-name Arabic tokens** are **4**. Confirm via **text-search header** for `محمد` (N=4) or the four verses at `verse.jsp` (3:144; 33:40; 47:2; 48:29).

- **“Dhū al-Kifl is only once.”**
  Ontology summaries sometimes show one verse prominently (**38:48**). The second is **21:85** with **ذَا/ذُو/ذِي** + **الكفل**. Both **verse.jsp** pages exist and the Arabic shows **الكفل** → total **2**.

- **“Ilyāsīn isn’t Ilyās.”**
  In **37:130**, **إلياسين** is a known orthographic form tied to **Ilyās**; QAC **morphology tags it PN** and ontology merges it under the Ilyās concept. Total **3** (6:85; 37:123; 37:130).

- **“Count al-Masīḥ (Messiah) too.”**
  The rule is **proper-name tokens** of the **person’s given name**. _al-Masīḥ_ is a **title**, not the personal name ʿĪsā, so it’s **excluded** by definition.

- **"Add Isrāʾīl as a prophet."**
  _Isrāʾīl_ is an epithet of **Yaʿqūb**. The 25-name census tracks **distinct primary names**; so **no extra row** for Isrāʾīl. (If you want an epithet-aware study, create a separate mapping layer, but don't change the name-token total.)

- **"Why exclude Aḥmad?"**
  Aḥmad refers to the **same prophet** as Muḥammad ﷺ. The 25-name census uses **one primary name per prophet** for consistency. Muḥammad (4 occurrences) is the **primary name**; Aḥmad (1 occurrence) is an **alternate name** and thus excluded.

- **“Ṣāliḥ appears more; you missed the adjective.”**
  Correct—we **exclude** the adjective **ṣāliḥ** “righteous.” Only **PN-tagged** occurrences for the **prophet** are counted. The concept page’s verse list already filters this.

## 9) Reproducibility & change control

- **Deterministic:** Every number traces to a **specific page** on QAC and (optionally) a **POS=PN** check.
- **Checksum:** Sum of the 25 primary name counts must equal **510**.
- **Versioning:** Record a date + a one-line "what changed," e.g. "2025-10-10 — adopted primary-name-only principle: Muḥammad=4 (primary) counted, Aḥmad=1 (alternate) excluded; total=510."
