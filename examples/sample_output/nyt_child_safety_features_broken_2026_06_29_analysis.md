# Analysis: NYT Child Safety Features Study Coverage (Jun 29, 2026)

## Article Metadata
- **Publication:** The New York Times
- **Date:** June 29, 2026
- **Headline (reconstructed):** "Child Safety Features on Major Social Media Platforms Found Broken, Buried, or Missing in University Study"
- **Primary source:** "Broken, Buried, or Missing" study by Lexie Matsumoto, Arturo Béjar, Abdulraheem Arar, Damon McCoy, Laura Edelson (NYU & Northeastern University / Cybersafety Research Center)
- **Note:** Article reconstructed from Engadget, CNN, and cross-references — NYT direct text is paywalled and blocked by browser policy. Same reconstruction pattern used for prior NYT Arena article analysis.

---

## Toolkit Output Summary

### Sentiment
| Metric | Score | Assessment |
|--------|-------|------------|
| overall_tone | -0.0525 | Near-neutral; VADER reads factual investigative prose correctly here |
| raw_tone | -0.0525 | No framing correction needed (correction fires only on positive-raw with adversarial signals) |
| emotional_language_intensity | 0.3051 | Moderate — driven by quoted self-harm content ("razor blade skin," "eating disorder") rather than editorial language |
| source_authority_framing | 0.76 | High — mostly named institutional sources |
| agency_attribution | -0.3333 | Slightly negative; dampened from -1.0 due to sparse-data fix (total hits < 3) |
| speculative_language_ratio | 0.2119 | Moderate — may overcount conditional phrasing in research methodology language |
| headline_body_alignment | 0.135 | Low alignment score — toolkit issue; headline and body are well-aligned in practice |
| anonymous_source_ratio | 0.20 | 1 anonymous source (unnamed Meta spokesperson) out of 5 total |

### Entities (27 unique, 52 mentions)
| Cluster | Entities |
|---------|----------|
| Meta | Meta, Instagram, Facebook |
| Google | YouTube, Alphabet, Google |
| Snap | Snapchat, Snap |
| TikTok | TikTok |
| Media/Publications | NYT, The New York Times, Reuters, Bloomberg |
| Academic/Research | New York University, Northeastern University |
| Research Centers | Cybersafety Research Center |
| US Congress | Congress, Senate, House of Representatives |
| Child Safety Researchers | Lexie Matsumoto, Arturo Béjar, Abdulraheem Arar, Damon McCoy, Laura Edelson |
| EU Regulatory | European Commission |
| Legal/Judicial | Digital Services Act |
| Australia | Australia |

**Remaining gaps:** KIDS Act / KOSA legislation not detected (entity cluster exists now but article may not mention them by acronym). Senate Judiciary Committee mentioned but may not have been matched as distinct from "Senate."

### Topics
| Topic | Confidence | Matched Keywords |
|-------|-----------|-----------------|
| child_safety | 0.609 | child safety, minor, minors, parental controls, teen, teenager, teens, youth safety |
| antitrust_regulation | 0.120 | Digital Services Act, European Commission |
| litigation | 0.058 | verdict |

**Assessment:** child_safety correctly dominant. antitrust_regulation is a stretch — the DSA probe is regulatory enforcement, not antitrust. Missing: a "platform_accountability" or "content_moderation" topic bucket would better capture this article's theme.

### Framing Devices (21 total, 5 types)
| Device Type | Count | Assessment |
|-------------|-------|------------|
| ironic_quotation | 12 | Mostly correct — quoted study categories and self-harm content. Some are direct quotes rather than ironic use |
| taxonomy_framing | 5 | **NEW** — correctly detecting "broken, buried, or missing" taxonomy. Major improvement |
| emotional_appeal | 2 | "alarming" and "mental health" — appropriate detection |
| loaded_language | 1 | "exploitation" — correct |
| self_referential_investigation | 1 | "Reuters reported" — false positive; this is wire attribution, not self-referential investigation |

**Key gap:** "crash-testing" analogy not detected. The analogy_metaphor patterns look for "like crash-testing" but the actual text may use it differently (e.g., "Researchers crash-tested features" or "The report crash-tested 86 features"). Need to check exact phrasing and potentially broaden the pattern.

### Sources (5 detected)
| Source | Type | Attribution |
|--------|------|------------|
| Bloomberg News | named | "reported" |
| "A Meta spokesperson said" | anonymous | "said" — unnamed spokesperson counts as anonymous |
| Instagram | organizational | "said" |
| Reuters | organizational | "reported" |
| Meta | organizational | "said" |

**Improvements from this iteration:**
- Pattern 6b case-sensitivity fix: [Aa]n? now matches "A Meta spokesperson said"
- _KNOWN_ORGS expanded: Instagram, Snapchat, Snap, TikTok, YouTube, Reuters, Bloomberg
- Direct organizational attribution pattern: "[Org] said" without requiring "in a statement"

**Remaining gaps:**
- Snap and TikTok spokespeople mentioned but not extracted (different attribution phrasing)
- Study authors cited as sources ("the study's authors noted") not detected — "noted" may be in verb list but "the study's authors" is a noun phrase, not a name pattern
- "The platforms said" — collective attribution not captured
- Quote extraction sometimes grabs wrong nearby text

---

## Manual Assessment vs Toolkit

### Tone
- **Manual:** Near-neutral investigative with strong implicit criticism via data presentation
- **Toolkit:** -0.0525 (near-neutral) ✓
- **Verdict:** Correct. The article presents data and lets findings speak; editorializing is minimal.

### Entity Coverage
- **Manual:** ~20+ entities expected
- **Toolkit:** 27 entities ✓ (up from 15 pre-fix)
- **Verdict:** Major improvement. New clusters (Academic/Research, US Congress, Child Safety Researchers, Research Centers, Australia) capture the full entity landscape.

### Source Balance
- **Manual:** 5+ sources (Meta spokesperson, study authors, platform spokespeople, wire services)
- **Toolkit:** 5 sources ✓ (up from 1 pre-fix)
- **Verdict:** Significant improvement. Still missing some secondary sources.

### Framing
- **Manual:** Key devices are (1) "crash-testing" analogy importing automotive safety regulation frame, (2) "broken/buried/missing" taxonomy implying completeness, (3) corporate accountability framing via juxtaposition with litigation
- **Toolkit:** Taxonomy correctly detected (NEW). "Crash-testing" analogy still missed. Corporate accountability framing partially captured via loaded_language.
- **Verdict:** taxonomy_framing is the highest-impact new detection. analogy_metaphor patterns need broadening.

### Agency
- **Manual:** Mixed — researchers are active agents (tested, found), platforms are mixed (built features but features failed), Congress is active (considering legislation)
- **Toolkit:** -0.3333 (slightly negative, dampened)
- **Verdict:** Improved from -1.0. Dampening correctly prevents extreme scores from sparse evidence. A richer agency vocabulary would improve accuracy.

---

## Toolkit Improvements Made This Iteration

### 1. Entity Clusters (entities.py)
**Added 7 new clusters:**
- `US Congress` — Congress, Senate, House, committee names
- `Academic/Research` — NYU, Northeastern, Stanford, MIT, Georgetown, etc.
- `Research Centers` — Cybersafety Research Center, CCDH, NCMEC, Thorn, etc.
- `Child Safety Legislation` — KIDS Act, COPPA, KOSA, EARN IT Act
- `Child Safety Researchers` — Béjar, Matsumoto, Edelson, McCoy, Arar
- `Australia` — Australia, Australian government, eSafety Commissioner

### 2. Source Extraction (sources.py)
- **Case-sensitivity fix:** `\ban?` → `\b[Aa]n?` in Pattern 6b (organizational spokesperson attribution)
- **Expanded `_KNOWN_ORGS`:** Added instagram, snapchat, snap, tiktok, youtube, bytedance, reddit, pinterest, discord, spotify, netflix, uber, lyft, airbnb, stripe, shopify, reuters, bloomberg
- **New direct org attribution pattern:** "[Org] said/reported" without requiring "in a statement" qualifier
- **Spokesperson in role-descriptor patterns:** Added spokesperson/spokeswoman/spokesman to anonymous role-descriptor + reverse patterns
- **Case-insensitive adjectives:** `[a-z]+` → `[A-Za-z]+` for optional org-name adjectives in role patterns

### 3. Framing Detection (framing.py)
- **New device: `analogy_metaphor`** — "like crash-testing", "akin to", "equivalent of", "tantamount to", "as if" constructions
- **New device: `taxonomy_framing`** — three-part taxonomies ("broken, buried, or missing"), "classified as", structured category language
- Updated METHODOLOGY.md with both new device descriptions
- Updated docstring counts (39→41 pattern-matched, 44→46 total)

### 4. Sentiment — Agency Attribution (sentiment.py)
- **Sparse-data dampening:** When total agency hits < 3, score is dampened by factor (total/3.0). Prevents extreme -1.0/+1.0 from single word matches while preserving direction.

### 5. Tests
- Updated framing device type counts in test_nyt_ai_reviews.py (39→41) and test_structural_consistency.py (39→41, 44→46)
- All 1002 tests pass

---

## Remaining Known Gaps

1. **"crash-testing" analogy detection:** analogy_metaphor patterns may not match all constructions of this analogy in the article text. Need to check exact phrasing.
2. **Study-as-source attribution:** "the study's authors noted" — noun-phrase sources not captured by person-name patterns
3. **Collective attribution:** "The platforms said" — no pattern for collective actor attribution
4. **self_referential_investigation false positive:** "Reuters reported" is wire attribution, not editorial self-reference
5. **headline_body_alignment (0.135):** Too low for a well-aligned article. Likely a VADER scoring issue with the headline containing both factual and evaluative terms.
6. **Topic coverage:** No "platform_accountability" or "content_moderation" topic bucket for this class of article.
7. **Source quote extraction:** Sometimes grabs wrong nearby text (e.g., quote from a different paragraph).
