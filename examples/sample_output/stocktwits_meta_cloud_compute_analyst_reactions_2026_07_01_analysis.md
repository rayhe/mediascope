# MediaScope Type A: Stocktwits Meta Cloud Compute Analyst Reactions

**Date:** 2026-07-02  
**Source:** Stocktwits  
**Article:** "Analysts See Meta's Reported Cloud Plans as Potential Positive"  
**Published:** 2026-07-01 ~10:34 PM EDT  
**Coverage type:** Financial/analyst aggregation (investor-facing platform)  
**Note:** Stocktwits is NOT one of the 5 tracked publications (Wired, NYT, Guardian, Atlantic, MIT Tech Review). This analysis tests toolkit accuracy on investor-oriented financial journalism — a genre where framing devices operate differently than editorial/advocacy content.

---

## Article Context

Bloomberg reported July 1 that Meta is exploring selling excess AI compute capacity as a cloud business, competing with AWS/Azure/Google Cloud. Stocktwits aggregated Wall Street analyst reactions:

- **BMO Capital (Brian Pitz):** Revenue/operating income tailwind
- **Mizuho:** Not near-term, "margin of safety to medium-term EPS"  
- **Jefferies:** "Strategic" to AI ambitions, mirrors AWS playbook
- **Bloomberg:** Original reporting attribution

The article is bullish-consensus: 4 named analyst sources all frame the development positively. No bearish counterpoint included.

---

## Toolkit vs Manual Analysis

### 1. Entity Detection

| Entity | Toolkit | Manual | Match? |
|--------|---------|--------|--------|
| Meta | 21 | ~20 | ✅ Within margin |
| Media/Publications | 3 | 3 (Bloomberg ×3) | ✅ |
| Amazon | 3 | 3 (AWS playbook refs) | ✅ |
| Microsoft | 2 | 2 (Azure refs) | ✅ |
| Google | 1 | 1 | ✅ |
| CoreWeave | 1 | 1 | ✅ |
| Nebius | 1 | 1 | ✅ (new cluster added this iteration) |

**Assessment:** Entity detection accurate. Nebius cluster added to recognize the AI infrastructure player mentioned alongside CoreWeave.

### 2. Topic Classification

| Topic | Toolkit | Manual Assessment |
|-------|---------|-------------------|
| financial_results | 0.480 | Reasonable — EPS, revenue, ROIC language |
| corporate_strategy | 0.443 | Good — cloud pivot, AWS playbook framing |
| ai_development | 0.181 | Low but present — AI compute, capex |

**Gap:** No `cloud_infrastructure` or `investor_sentiment` bucket. Article is primarily about cloud strategy and analyst reactions. Current buckets approximate but don't precisely capture the financial journalism genre. Possible future work: add `investor_sentiment` topic bucket.

### 3. Sentiment

| Dimension | Toolkit | Manual Estimate | Match? |
|-----------|---------|-----------------|--------|
| overall_tone | 0.657 | +0.4 to +0.5 | ⚠️ Slightly high |
| emotional_language_intensity | 0.077 | ~0.05 | ✅ Low (clinical, financial) |
| source_authority_framing | 1.000 | High | ✅ All named analysts/firms |
| agency_attribution | 0.000 | 0.0 | ✅ No negative agency |
| headline_body_alignment | 0.802 | ~0.8 | ✅ Headline matches body |
| anonymous_source_ratio | 0.000 | 0.0 | ✅ All sources named |
| speculative_language_ratio | 0.480 | ~0.4 | ✅ Forward-looking analyst language |
| comparative_framing | 0.000 | 0.0 | ✅ No asymmetric comparisons |

**Assessment:** Tone ~0.15 high (toolkit reads the bullish consensus at face value, which is fair for a financial aggregation piece). Speculative language ratio is appropriately elevated — analyst notes are inherently forward-looking ("would be," "could generate," "appears to mirror").

### 4. Framing Devices

**Before fixes (this iteration):**

| Device | Evidence | Verdict |
|--------|----------|---------|
| `assumed_consensus` | "Analysts See" (headline) | ✅ TRUE POSITIVE |
| `ironic_quotation` | "a margin of safety to medium-term EPS," | ❌ FALSE POSITIVE |
| `ironic_quotation` | "strategic" | ❌ FALSE POSITIVE |
| `ironic_quotation` | an additional short phrase | ❌ FALSE POSITIVE |
| `self_referential_investigation` | "Bloomberg reported" | ❌ FALSE POSITIVE |

**After fixes:**

| Device | Evidence | Verdict |
|--------|----------|---------|
| `assumed_consensus` | "Analysts See" (headline) | ✅ TRUE POSITIVE |

**Assessment:** 4 false positives → 0 false positives. Only the legitimate `assumed_consensus` survives. The "Analysts See" headline pattern is genuinely an assumed-consensus construction (presupposes analyst agreement rather than reporting individual views), so this is a correct detection.

### 5. Source Extraction

| Source | Verb | Affiliation | Manual Check |
|--------|------|-------------|--------------|
| Brian Pitz | said | (empty) | ⚠️ Should be "BMO Capital" |
| Analysts | said | "Meta's record capital expenditure" | ❌ Garbage extraction |
| Mizuho | said | (empty) | ✅ Org is own affiliation |
| Jefferies | said | (empty) | ✅ Org is own affiliation |
| Bloomberg | reported | Bloomberg | ✅ |

**Authority grade:** 0.950 — correctly high (all named, institutional sources).

**Open bug:** The `[Org] analyst [Name] [verb]` pattern (e.g., "BMO Capital analyst Brian Pitz said") isn't matched. The generic "Analysts" source extracts garbage affiliation from the following noun phrase. This is a sources.py pattern gap, not fixed this iteration.

---

## Fixes Applied This Iteration

### Fix 1: Firm-level attribution filter for ironic_quotation (framing.py)

**Problem:** `ironic_quotation` detector only checked for personal-pronoun attribution ("he said", "she said") in lookback/lookahead. In financial journalism, quotes are attributed to firms ("Jefferies said", "Mizuho said", "BMO Capital said").

**Changes:**
1. **Short quotes (≤3 words):** Added `_ORG_ATTR_PAT` regex to lookahead — matches `[word]+ said/noted/added` after the quote. Expanded lookahead window from 50 → 80 chars (50 was clipping "Jefferies said" at 51 chars).
2. **Short quotes lookback:** Added org-level attribution patterns (`" said it "`, `" said the "`, `" said that "`, `" added that "`, etc.) to `_ATTRIBUTION_SHORT`.
3. **Longer quotes (>3 words):** Added 200-char wide lookback for org-level attribution patterns (`_ORG_QUOTE`). Added 60-char lookahead for post-quote attribution (`_LONG_POST_ATTR`).

**Impact:** Eliminates false positives on analyst-attributed quotes while preserving genuine scare quotes (editorial "safe" and "responsible" still fire correctly).

### Fix 2: Wire service cross-citation filter for self_referential_investigation (framing.py)

**Problem:** `self_referential_investigation` flagged "Bloomberg reported" even without `source_publication` set. But "Bloomberg reported" is ALWAYS a cross-citation — Bloomberg articles don't say "Bloomberg reported"; they just report.

**Change:** Added pre-filter that suppresses `self_referential_investigation` for well-known wire services (Bloomberg, Reuters, AP, FT, WSJ) even when `source_publication` is not provided. Reflexive patterns ("our investigation") are always preserved.

### Fix 3: Nebius entity cluster (entities.py)

Added Nebius/Nebius Group to AI infrastructure entity clusters (alongside CoreWeave, Palantir).

### Tests Added

`test_analyst_quote_attribution.py` — 13 new tests across 4 test classes:
- `TestShortAnalystQuotePostAttribution` (4 tests): firm-level post-attribution for short quotes
- `TestLongerAnalystQuoteAttribution` (3 tests): firm-level pre/post-attribution for longer quotes  
- `TestWireCrossCitation` (4 tests): wire service cross-citation filtering, including positive case (Bloomberg self-referential when source IS Bloomberg)
- `TestGenuineScarequotesPreserved` (2 tests): editorial scare quotes still detected

**Suite:** 1205 passed, 2 xfailed, 0 failures (up from 1192+2).

---

## Design Observations

1. **Financial journalism is a distinct genre for framing analysis.** Analyst-aggregation articles use quoted phrases differently than editorial/advocacy pieces. Quotes are direct speech from institutional sources, not editorial commentary. The toolkit's framing devices were calibrated for editorial coverage (Wired, Guardian, etc.) where quotes-in-quotes often ARE scare quotes. This iteration adds genre awareness.

2. **Attribution distance varies by genre.** In editorial writing, attribution is usually adjacent to the quote ("he said"). In financial journalism, attribution can be 100+ characters before the quote ("Mizuho said it does not believe ... sees it 'more as planning...'"). The wider lookback (200 chars for longer quotes) handles this without increasing false negatives in editorial analysis.

3. **Cross-citation is never self-referential.** The prior code only filtered cross-citations when `source_publication` was explicitly set. But wire services are structurally incapable of being self-referential in this pattern — adding a hardcoded set of known wire services eliminates an entire class of false positives without needing the caller to specify the source.

4. **Source affiliation extraction remains the weakest dimension.** The `[Org] analyst [Name] [verb]` pattern gap has persisted across multiple article types. This should be the next sources.py improvement.

---

## Remaining Open Items

- **Source affiliation pattern:** `[Org] analyst [Name] [verb]` not matched. "BMO Capital analyst Brian Pitz said" → affiliation should be "BMO Capital". Not fixed this iteration.
- **Topic bucket gap:** No `cloud_infrastructure` or `investor_sentiment` topic. Current approximations (financial_results + corporate_strategy) are adequate but imprecise.
- **Overall tone calibration:** 0.657 vs manual ~0.45. Toolkit reads bullish consensus at face value. Consider adding a "consensus discount" for one-sided source coverage (all positive, no bearish counterpoint).
