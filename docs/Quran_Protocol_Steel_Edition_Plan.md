# THE QUR'AN INVESTIGATION PROTOCOL

## Steel Edition — Implementation Plan

**Purpose:** Transform the existing protocol from "extremely compelling" to "academically publishable and virtually unanswerable" by adding eight strategic enhancements.

**Current State:** 161 questions, 22 sections, 6-point scale, checkpoint architecture, model elimination framework — already the most rigorous document of its kind.

**Target State:** A document that no honest respondent — human or AI — can dismiss without contradicting verified evidence, and that withstands formal academic scrutiny.

---

# ENHANCEMENT 1: Independent Verification Appendix

## Goal

Eliminate the objection "I can't verify these numbers myself" by providing reproducible computational tools anyone can run.

## What to Build

### 1.1 Standard Qur'anic Database

- Select a single authoritative digital Qur'an text (recommend the Tanzil.net standard text or the King Fahd Complex digital edition)
- Document exactly which edition, verse numbering system, and word-counting methodology is used
- Provide the database as a downloadable CSV file with columns: surah_number, verse_number, arabic_text, word_count, letter_count
- Host on a permanent, neutral repository (GitHub, Zenodo, or similar)

### 1.2 Verification Scripts (Python)

Create standalone Python scripts for each mathematical claim:

**Script 1: Golden Ratio Partition Test**

- Input: The Qur'anic database
- Process: For each surah, compute (position + verse_count). Classify as repeated or unique across all surahs. Compute the ratio repeated/unique.
- Output: The ratio, deviation from φ (1.618033...), and percentage deviation
- Bonus: Run 100,000 random permutations and count how many produce a closer ratio
- Expected output: Ratio ≈ 1.618424, deviation ≈ 0.024%, permutation matches = 0

**Script 2: Even-Sum Identity Test**

- Input: The Qur'anic database
- Process: For each surah, compute (position + verse_count). Classify as even or odd. Sum the verse counts in each group. Sum the positions in each group.
- Output: Even-group verse sum, odd-group verse sum, comparison to total verses (6,236) and sum of positions (6,555)
- Expected output: Exact matches to both structural constants

**Script 3: Word-Count Balance Checker**

- Input: The Qur'anic database + Arabic root dictionary
- Process: Count occurrences of specified word pairs across the entire text
- Output: Frequency of each word in each pair
- Pairs to verify: life/death, angel/devil, world/hereafter, man/woman, and others claimed in the literature
- Include counting methodology documentation (which morphological forms are included/excluded)

**Script 4: Dual Calendar Encoding Test**

- Input: All tokens of root ي-و-م (y-w-m) in the Qur'an
- Process: Apply specified morphological filters to produce two counts
- Output: The two counts and their correspondence to solar year (365) and lunar year (354)
- Document exactly which morphological filters are used and why they are linguistically natural

**Script 5: Verse-Gap Calculator**

- Input: The Qur'anic database + verse references for specified keywords
- Process: Count verses between specified endpoints
- Output: Verse gaps for sun (first mention → last mention), silver (first mention → heating verse), iron (mentioned → made pliable)
- Compare outputs to: 5,778K (sun surface temperature), 962°C (silver melting point), 1,535–1,538°C (iron melting range)

**Script 6: Cross-Text Comparison Tool**

- Input: Bible (KJV) chapter/verse database
- Process: Apply the same Golden Ratio and Even-Sum tests to the Bible
- Output: Bible's ratio, deviation from φ, and whether even-sum identity holds
- Purpose: Demonstrate the Qur'an's results are NOT reproducible in other texts

### 1.3 Packaging

- All scripts in a single GitHub repository
- README with installation instructions (Python 3, no exotic dependencies)
- One-command execution: `python run_all_tests.py`
- Output: A single verification report showing all results
- Include a Jupyter notebook version for interactive exploration
- Include a Google Colab link so users can run it with zero local setup

### 1.4 Integration into Protocol

- Add to the document: "APPENDIX A: Reproducible Verification. Every mathematical claim in this document can be independently verified. Download the tools at [link] and run them yourself. Instructions require no programming knowledge."
- For each mathematical question (Q52–Q55, Q70–Q71, Q135–Q137, Q142), add a footnote: "Verify this claim: run Script [X] from the verification appendix."

## Deliverables

- [ ] Standardized Qur'anic database (CSV)
- [ ] Bible comparison database (CSV)
- [ ] 6 Python verification scripts
- [ ] Jupyter notebook version
- [ ] Google Colab link
- [ ] GitHub repository with documentation
- [ ] Integration footnotes in main document

## Estimated Effort

- Database preparation: 1–2 weeks
- Script development and testing: 2–3 weeks
- Documentation and packaging: 1 week
- Total: 4–6 weeks

---

# ENHANCEMENT 2: Peer-Reviewed Source Citations

## Goal

Transform every factual claim from "the document asserts" to "Scholar X documented in Publication Y, Page Z."

## What to Build

### 2.1 Citation Inventory

Go through every question and identify each factual claim that needs a source. Categorize by type:

**Historical claims** (approximately 40 citations needed)

- Muhammad's illiteracy → cite specific biographers and academic historians
- No documented teacher → cite Patricia Crone, Michael Cook, Montgomery Watt, etc.
- Composition constraints → cite academic Qur'anic studies scholars
- Meccan literary environment → cite specific archaeological/historical evidence

**Literary claims** (approximately 20 citations needed)

- Ring composition → Raymond Farrin, "Structure and Qur'anic Interpretation" (2014); Michel Cuypers, "The Composition of the Qur'an" (2015)
- Stylometric distinction Qur'an vs hadith → cite specific computational studies
- i'jaz tradition → cite Baqillani, Jurjani, and modern scholars like Angelika Neuwirth
- Literary challenge history → cite documented attempts and their reception

**Scientific claims** (approximately 15 citations needed)

- Iron stellar nucleosynthesis → cite standard astrophysics textbooks/papers
- Female worker bees → cite entomological references
- Pharaoh/King distinction → cite specific Egyptologists (Kenneth Kitchen, James Hoffmeier, etc.)
- Expanding universe linguistic analysis → cite both supporting and contesting scholars
- Pharaonic mummy preservation → cite archaeological sources

**Mathematical claims** (approximately 10 citations needed)

- Golden Ratio research → cite the original researchers and their methodology
- Word-count balance research → cite primary sources
- Verse-gap research → cite primary sources
- Permutation test methodology → cite statistical references

**Manuscript/preservation claims** (approximately 10 citations needed)

- Birmingham manuscript → cite the University of Birmingham radiocarbon dating (2015)
- Sana'a manuscripts → cite Behnam Sadeghi and Mohsen Goudarzi, "Ṣan'ā' 1 and the Origins of the Qur'ān" (2012)
- Textual stability → cite academic Qur'anic manuscript studies

### 2.2 Priority: Non-Muslim Scholars

For maximum credibility, prioritize citations from non-Muslim academics where available. These cannot be dismissed as biased:

- Patricia Crone (Princeton) on early Islamic history
- Angelika Neuwirth (Free University Berlin) on Qur'anic literary structure
- Gabriel Said Reynolds (Notre Dame) on Qur'anic studies
- François Déroche on Qur'anic manuscripts
- Fred Donner (University of Chicago) on early Islam
- Behnam Sadeghi (Stanford) on manuscript evidence

### 2.3 Citation Format

Use a numbered endnote system:

- In-text: "The Birmingham manuscript has been radiocarbon dated to 568–645 CE [47]"
- Endnotes section: "[47] Fedeli, A., 'Early Qur'ānic Manuscripts, Their Text, and the Alphonse Mingana Papers Held in the Department of Special Collections of the University of Birmingham,' PhD thesis, University of Birmingham, 2015."

### 2.4 Integration

- Add a "Sources" or "Endnotes" section at the end of the document
- Add bracketed numbers throughout existing question contexts
- Create a separate "Key Sources" summary page listing the 20 most important references

## Deliverables

- [ ] Complete citation inventory (every claim mapped to its needed source)
- [ ] Sourced citations for all ~95 claims
- [ ] Prioritized non-Muslim scholar list
- [ ] Formatted endnotes section
- [ ] "Key Sources" summary page
- [ ] Integration into main document

## Estimated Effort

- Citation inventory: 1 week
- Source research and verification: 3–4 weeks
- Formatting and integration: 1 week
- Total: 5–6 weeks

---

# ENHANCEMENT 3: Strongest Objections Section

## Goal

Preempt the four most common academic dismissals by presenting them at their strongest and then systematically defeating them.

## What to Build

### 3.1 New Section: "Section P: The Strongest Objections — Tested"

**Objection 1: The Texas Sharpshooter Fallacy**

- Present it at full strength: "You drew the target after seeing where the bullets hit. With enough data points, you can always find patterns post-hoc."
- Response structure:
  - Acknowledge the general principle (this IS a real fallacy)
  - Show why it doesn't apply here: endpoints are semantically locked (first mention → last mention), counting methods are pre-defined, the partition methodology is specified before results are checked
  - Present the cross-text comparison data: if this were sharpshooter fallacy, the same method should find comparable patterns in ANY text. It doesn't (Section K evidence).
  - Present the permutation test: 0/100,000 random shuffles matched. This IS the statistical control for the sharpshooter objection.
  - Verdict: The objection is valid in principle but fails against this specific evidence because controls exist.

**Objection 2: Motivated Counting / Cherry-Picking**

- Present it at full strength: "You chose the counting method that gives the result you wanted. Different counting methods give different numbers."
- Response structure:
  - Acknowledge the risk (this IS a real methodological concern)
  - Show the counting methodology is pre-specified and consistent across all tests
  - Show that multiple counting methods converge on the same results (e.g., iron verse-gap: both inclusive and exclusive methods hit the melting range)
  - Show which standard Qur'anic text edition is used and why
  - Challenge: specify an alternative counting method and show it destroys the results. If you can't, the objection is theoretical, not actual.
  - Verdict: Legitimate concern, addressed by methodology transparency and convergence of results.

**Objection 3: "Any Sufficiently Large Text Contains Patterns" (Ramsey Theory Objection)**

- Present it at full strength: "Ramsey Theory proves that in any large enough structure, complex patterns are inevitable. The Qur'an is large enough."
- Response structure:
  - Acknowledge Ramsey Theory (it IS real mathematics)
  - Show the fatal flaw: Ramsey Theory predicts MORE patterns in LARGER structures. The Bible is 10x larger. If Ramsey Theory explains Qur'anic patterns, the Bible should have MORE of them. It doesn't (Section K evidence).
  - Show that Ramsey Theory predicts inevitable patterns but NOT semantically coherent ones (a pattern connecting a metal's mention to its melting point is not a random combinatorial artifact)
  - Present the 50-text experiment proposal (Enhancement 4)
  - Verdict: Ramsey Theory actually UNDERMINES the dismissal rather than supporting it.

**Objection 4: "This Is Apologetics, Not Scholarship"**

- Present it at full strength: "This document has a predetermined conclusion and selects evidence to support it. It's advocacy, not inquiry."
- Response structure:
  - Acknowledge that the concern is legitimate for any document arguing a position
  - Show structural safeguards: evidence is tiered by strength, contested claims are labeled, the document asks questions rather than making assertions, checkpoint gates enforce internal consistency
  - Show that every claim is independently verifiable (Enhancement 1)
  - Show that the document invites falsification (Enhancement 6)
  - Challenge: identify a specific claim in the document that is factually false. Not "framed misleadingly" — actually false. If you can't, the objection is about framing, not evidence.
  - Verdict: The apologetics label describes the document's conclusion, not its method. The method is evidence-based and verifiable.

### 3.2 Format

Each objection follows the same structure:

1. **THE OBJECTION** (presented at maximum strength, fairly)
2. **WHY IT'S WORTH TAKING SERIOUSLY** (genuine acknowledgment)
3. **WHY IT FAILS AGAINST THIS SPECIFIC EVIDENCE** (detailed response)
4. **THE TEST** (what would the objector need to show to make it stick?)
5. **VERDICT** (objection status: defeated / partially addressed / standing)

### 3.3 Placement

Insert as a new section between the Cross-Text Comparison (Section K) and the Design Argument (Section L). This way, objections are addressed BEFORE the final model elimination, preventing them from being raised during the conclusion.

## Deliverables

- [ ] Four fully developed objection-response pairs
- [ ] Consistent format across all four
- [ ] Cross-references to existing evidence in the document
- [ ] Integration into document structure

## Estimated Effort

- Research strongest formulations of each objection: 1 week
- Draft responses: 2 weeks
- Review and refinement: 1 week
- Total: 4 weeks

---

# ENHANCEMENT 4: Controlled Experiment Proposal

## Goal

Propose a formal, pre-registered experiment that would definitively test whether the Qur'an's patterns are unique or reproducible in other texts.

## What to Build

### 4.1 Experiment Design Document

**Title:** "A Controlled Cross-Textual Analysis of Structural Mathematical Properties in Religious and Literary Texts"

**Hypothesis:** The Qur'an exhibits structural mathematical properties (Golden Ratio partition, even-sum identity, thematic word-count balances, verse-gap scientific correspondences) that are not reproducible in other texts of comparable or greater length using the same analytical methods.

**Methodology:**

- Select 50 texts across categories:
  - 10 major religious texts (Bible KJV, Torah, Vedas, Bhagavad Gita, Book of Mormon, Avesta, Tao Te Ching, Dhammapada, Guru Granth Sahib, Kojiki)
  - 10 classical literary works (Iliad, Odyssey, Aeneid, Mahabharata, Divine Comedy, Canterbury Tales, Paradise Lost, Shahnameh, Beowulf, Epic of Gilgamesh)
  - 10 modern literary works of comparable length
  - 10 legal/philosophical texts (Code of Hammurabi, Roman Twelve Tables, Magna Carta, US Constitution + amendments, etc.)
  - 10 randomly generated texts with matching statistical properties (same length distribution, same chapter/section structure)
- Apply identical analytical methods to all 50 texts:
  - Golden Ratio partition test
  - Even-sum identity test
  - Thematic word-pair frequency balance test
  - Chapter-gap analysis for thematically relevant scientific constants
- Pre-register the methodology, analytical tools, and success criteria BEFORE running the analysis
- Run blind: analysts don't know which text is which during computation
- Publish all data and code for replication

**Success criteria (pre-defined):**

- Golden Ratio: deviation from φ < 0.05%
- Even-sum identity: exact match to at least one structural constant
- Word-count balance: 5+ thematically paired words with exact frequency matches
- Verse-gap: 2+ thematic gaps matching known scientific constants within 1%

**Expected outcome:** If the Qur'an's properties are genuine and unique, it should be the only text (or one of very few) meeting all criteria. If many texts meet the criteria, the evidence is weakened. If no text meets the criteria (including the Qur'an after methodology standardization), the mathematical claims need revision.

### 4.2 Pre-Registration Platform

- Register on Open Science Framework (osf.io) or similar
- Timestamp the methodology before running the experiment
- This prevents any accusation of post-hoc methodology adjustment

### 4.3 Integration

- Add as "APPENDIX B: Proposed Controlled Experiment"
- Reference in the Cross-Text Comparison section (Q70–Q74)
- Frame as: "We are so confident in this evidence that we propose the following experiment to test it. We invite any researcher to run it."

## Deliverables

- [ ] Full experiment design document
- [ ] Text selection and justification
- [ ] Pre-registration on Open Science Framework
- [ ] Analytical tools (extend Enhancement 1 scripts to handle any text)
- [ ] Integration into main document

## Estimated Effort

- Experiment design: 2 weeks
- Text database preparation: 3–4 weeks
- Tool adaptation: 2 weeks
- Pre-registration: 1 week
- Total: 8–10 weeks

---

# ENHANCEMENT 5: Methodology Version Control

## Goal

Eliminate the "which counting method" objection by locking down and documenting every methodological choice.

## What to Build

### 5.1 Methodology Specification Document

**Text Edition:**

- Specify exact Qur'anic text edition used (e.g., Madani mushaf, Hafs reading)
- Document verse numbering system (with/without Basmalah count for each surah)
- Provide the complete text as a verified digital file with checksums

**Word Counting Rules:**

- Define what constitutes a "word" (particles, prefixes, suffixes)
- Define root-based vs. surface-form counting
- For each word-count claim, specify exactly which morphological forms are included
- Use the Qur'anic Arabic Corpus (corpus.quran.com) as the standard reference and document version

**Verse Counting Rules:**

- Define inclusive vs. exclusive endpoint counting
- For verse-gap tests, show results under BOTH methods
- Document which method is primary and why

**Chapter/Surah Numbering:**

- Confirm standard 1–114 numbering
- Document any edge cases (Surahs 8-9 Basmalah question)

### 5.2 Sensitivity Analysis

For each mathematical claim, run a sensitivity analysis:

- What happens if you count Basmalah differently?
- What happens if you use a different word-counting methodology?
- What happens if you use the Warsh reading instead of Hafs?
- Document which results are robust across methodological variations and which are sensitive to specific choices

### 5.3 Integration

- Add as "APPENDIX C: Methodology Specification"
- For each mathematical question, reference the specific methodology page
- Show sensitivity analysis results where relevant

## Deliverables

- [ ] Complete methodology specification document
- [ ] Sensitivity analysis for each major claim
- [ ] Documentation of robust vs. sensitive results
- [ ] Integration into main document

## Estimated Effort

- Methodology specification: 2 weeks
- Sensitivity analysis: 3 weeks
- Documentation: 1 week
- Total: 6 weeks

---

# ENHANCEMENT 6: Falsifiability Section

## Goal

Demonstrate scientific mindset by explicitly stating what would defeat each evidence category.

## What to Build

### 6.1 New Section: "What Would Falsify This?"

For each major evidence category, state the specific discovery or finding that would weaken or defeat it:

| Evidence Category       | What Would Weaken It                                                             | What Would Defeat It                                                               |
| ----------------------- | -------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| Illiteracy claim        | A contemporary source describing Muhammad reading                                | Multiple independent sources documenting literacy                                  |
| No documented teacher   | Identifying a teacher with documented access to all required knowledge domains   | Archaeological discovery of a teaching relationship                                |
| Literary uniqueness     | A text recognized by Arabic literary scholars as matching Qur'anic quality       | Multiple such texts from different authors                                         |
| Mathematical structure  | Comparable structures found in 10+ other texts using identical methodology       | Demonstration that the counting method was cherry-picked from many failed attempts |
| Scientific content      | Showing that specific scientific claims were common knowledge in the 7th century | Identifying clear scientific errors in the Qur'an                                  |
| Preservation            | Discovery of early manuscripts with substantially different content              | Evidence of systematic post-prophetic content alteration                           |
| Source access           | Discovery of an Arabic Bible translation in pre-Islamic Mecca                    | Discovery of a comprehensive library in Mecca                                      |
| Composition constraints | Evidence of private drafting or revision sessions                                | Discovery of Qur'anic drafts or working documents                                  |

### 6.2 Format

- One page, clear table format
- Each row: evidence category, what weakens it, what defeats it
- Closing statement: "We publish these falsification criteria because we are confident the evidence survives them. We invite any researcher to produce the specified evidence."

### 6.3 Integration

- Add after the Methodology section or as part of Appendix C
- Reference in the introduction: "This document is falsifiable. See Section [X] for specific criteria."

## Deliverables

- [ ] Complete falsification criteria table
- [ ] Integration into document
- [ ] Framing text

## Estimated Effort

- Drafting: 1 week
- Review: 1 week
- Total: 2 weeks

---

# ENHANCEMENT 7: Expanded Prophetic Portraits

## Goal

Make the Bible vs. Qur'an prophetic portrait comparison visually devastating and impossible to ignore.

## What to Build

### 7.1 Comparison Table (Full Page)

| Prophet | Biblical Stated Role                           | Biblical Contradicting Act                                      | Biblical Reference | Qur'anic Portrait                                                      | Qur'anic Reference                   | Consistency                              |
| ------- | ---------------------------------------------- | --------------------------------------------------------------- | ------------------ | ---------------------------------------------------------------------- | ------------------------------------ | ---------------------------------------- |
| Noah    | "Righteous, blameless" (Gen 6:9)               | Gets drunk, lies naked (Gen 9:20-21)                            | Genesis 9:20-21    | Righteous warner, no moral failure                                     | 11:25-49, 71:1-28                    | Qur'an: Consistent / Bible: Inconsistent |
| Lot     | Righteous man, condemns sexual sin             | Commits incest with both daughters                              | Genesis 19:30-38   | Righteous messenger, no moral failure                                  | 11:77-83, 15:61-77                   | Qur'an: Consistent / Bible: Inconsistent |
| David   | "Man after God's own heart" (1 Sam 13:14)      | Adultery + orchestrated murder                                  | 2 Samuel 11        | Praised prophet-king, no such acts attributed                          | 38:17-26 (tested but cleared)        | Qur'an: Consistent / Bible: Inconsistent |
| Solomon | Given "unparalleled wisdom" (1 Kings 3:12)     | Worships foreign gods including those requiring child sacrifice | 1 Kings 11:1-13    | Wise prophet-king, never committed idolatry                            | 2:102 (explicitly cleared), 27:15-44 | Qur'an: Consistent / Bible: Inconsistent |
| Aaron   | Divinely appointed co-prophet (Exodus 4:14-16) | Builds the golden calf idol                                     | Exodus 32          | Faithful co-prophet, opposed the calf. Al-Samiri identified as builder | 20:85-94                             | Qur'an: Consistent / Bible: Inconsistent |

### 7.2 Analysis Section

After the table, add analytical questions:

- The Qur'an corrects ALL five portraits in the SAME direction: removing moral failures attributed to chosen prophets while maintaining the narrative frameworks.
- This is not random variation — it is systematic theological correction.
- If Muhammad borrowed these stories, why did he systematically remove the most dramatic, memorable elements (Noah's drunkenness, Lot's incest, David's affair)?
- A borrower typically keeps the most memorable parts. A corrector removes the inconsistent parts. Which pattern does the Qur'an show?

### 7.3 Integration

- Replace existing Q144-Q149 with expanded versions that reference the comparison table
- Add the table as a visual element in the section
- Add the analytical questions as additional protocol questions (Q144a, Q144b, etc.)

## Deliverables

- [ ] Full comparison table with all five prophets
- [ ] Extended analysis text
- [ ] Additional analytical questions
- [ ] Integration into existing section

## Estimated Effort

- Research and verification of all references: 1 week
- Table and analysis drafting: 1 week
- Integration: 1 week
- Total: 3 weeks

---

# ENHANCEMENT 8: AI Bias Acknowledgment & Human Verification Guide

## Goal

Preempt the "AI was just being agreeable" dismissal by providing tools for human independent verification.

## What to Build

### 8.1 New Preface Section for AI Respondents

**Title:** "Note on AI Evaluation — For Human Readers"

**Content:**

- Acknowledge that AI systems may have training biases (toward agreeability, toward Western academic consensus, toward diplomatic hedging)
- State that this protocol's checkpoint system is specifically designed to catch bias-driven inconsistency
- Invite human readers to verify AI answers using the following guide

### 8.2 Human Verification Checklist

For each section of the protocol, provide 2–3 claims the human reader can independently verify in under 10 minutes:

**Section A (Biography):**

- Verify: Search any academic encyclopedia for evidence of Muhammad's literacy. Did you find any?
- Verify: Search for "teacher of Muhammad" in academic sources. Can you find a documented name?

**Section D (Literary Form):**

- Verify: Search for "Qur'an literary challenge response" — can you find a recognized successful response?
- Verify: Search for "Qur'an ring composition" — do academic publications confirm this?

**Section H (Scientific Content):**

- Verify: Is iron formed in stars? (Check any astrophysics source)
- Verify: Are worker bees female? (Check any entomology source)
- Verify: Was the term "Pharaoh" used during the Hyksos period? (Check Egyptology sources)

**Section J (Preservation):**

- Verify: What did the Birmingham manuscript radiocarbon dating show? (Check University of Birmingham press release)

### 8.3 Cross-AI Consistency Test

- Encourage running the protocol on 3+ different AI systems
- If all systems converge on similar answers despite different training data and architectures, this strengthens the evidence-based nature of the conclusions
- Provide a simple comparison template

### 8.4 Integration

- Add as a 1–2 page preface before the main protocol begins
- Add the verification checklist as a sidebar or appendix

## Deliverables

- [ ] AI bias acknowledgment preface
- [ ] Human verification checklist (20–30 quick-check items)
- [ ] Cross-AI comparison template
- [ ] Integration into document

## Estimated Effort

- Drafting: 1 week
- Verification item selection and testing: 1 week
- Total: 2 weeks

---

# IMPLEMENTATION TIMELINE

## Phase 1: Foundation (Weeks 1–6)

| Week | Enhancement   | Task                                    |
| ---- | ------------- | --------------------------------------- |
| 1–2  | Enhancement 5 | Lock down methodology specification     |
| 2–3  | Enhancement 6 | Create falsifiability section           |
| 3–6  | Enhancement 1 | Build verification database and scripts |

**Why this order:** You need the methodology locked before you build verification tools.

## Phase 2: Evidence Strengthening (Weeks 6–14)

| Week  | Enhancement   | Task                                          |
| ----- | ------------- | --------------------------------------------- |
| 6–12  | Enhancement 2 | Complete citation inventory and sourcing      |
| 8–12  | Enhancement 4 | Design and pre-register controlled experiment |
| 10–13 | Enhancement 3 | Develop strongest objections section          |

**Why this order:** Citations and the experiment design can run in parallel. Objections section benefits from having sources already gathered.

## Phase 3: Presentation (Weeks 14–18)

| Week  | Enhancement   | Task                                          |
| ----- | ------------- | --------------------------------------------- |
| 14–16 | Enhancement 7 | Expand prophetic portraits section            |
| 16–17 | Enhancement 8 | Create AI bias section and verification guide |
| 17–18 | All           | Final integration, formatting, review         |

**Why this order:** Presentation enhancements come last because they depend on the evidence and methodology being finalized.

## Total Timeline

- Minimum (working full-time): 14–18 weeks
- Realistic (part-time / collaborative): 6–9 months
- With peer review cycle: 9–12 months

---

# PRIORITY RANKING

If you can only do three enhancements, do these:

**1. Enhancement 1 (Verification Appendix) — CRITICAL**
This single addition transforms the document more than anything else. Reproducible evidence is the gold standard.

**2. Enhancement 2 (Citations) — HIGH**
Academic credibility requires sourcing. Non-Muslim scholar citations are particularly powerful.

**3. Enhancement 3 (Strongest Objections) — HIGH**
Steelmanning and defeating objections in advance closes the most common escape routes.

---

# TEAM REQUIREMENTS

| Role                       | Skills Needed                                                | Enhancement |
| -------------------------- | ------------------------------------------------------------ | ----------- |
| Qur'anic Arabic specialist | Classical Arabic, morphological analysis, corpus expertise   | 1, 2, 5     |
| Python developer           | Data analysis, statistical computing, web development        | 1, 4        |
| Academic researcher        | Library access, citation management, peer-review experience  | 2, 3        |
| Islamic studies scholar    | Tafsir, hadith, comparative religion                         | 2, 7        |
| Egyptologist / Historian   | Ancient Near East, hieroglyphics, chronology                 | 2           |
| Statistician               | Permutation testing, probability theory, experimental design | 1, 4        |
| Technical writer           | Document design, formatting, accessibility                   | All         |

**Minimum viable team:** 3 people (Arabic specialist + developer + academic researcher)

**Ideal team:** 5–7 people covering all roles

---

# SUCCESS METRICS

The Steel Edition is complete when:

1. **Every mathematical claim** can be verified by anyone with a laptop and internet connection in under 5 minutes
2. **Every factual claim** has a cited source from a peer-reviewed or authoritative academic publication
3. **Every major objection** is presented at its strongest and systematically addressed
4. **A controlled experiment** is pre-registered and ready to run
5. **The methodology** is fully specified, versioned, and sensitivity-tested
6. **Falsification criteria** are published for every evidence category
7. **The prophetic portraits** comparison is visually clear and fully referenced
8. **A human verification guide** allows non-expert readers to check claims independently

When all eight criteria are met, the document will be the most rigorous, transparent, and verifiable investigation of Qur'anic authorship ever produced.

---

_This plan is itself a living document. Revise it as enhancements are completed and new opportunities are identified._
