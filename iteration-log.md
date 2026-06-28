# MediaScope Iteration Log

Tracks every improvement cycle run on the toolkit.

---

## 2026-06-27 19:00 PT — Hour Type D: Toolkit Quality & Documentation — Doc/Code Sync Audit

**Focus:** Systematic audit and fix of documentation drift across all doc files, CLI, README, and structural consistency tests.
**Rationale:** New features (confession_framing framing device, government_oversight topic bucket) were added to code and tests but not propagated to all documentation surfaces. The structural consistency test had a stale CLI assertion that masked the framing count drift.

### 1. Documentation Drift Identified and Fixed

Six drift instances found across 4 documentation files + CLI + test:

| File | Issue | Before | After |
|---|---|---|---|
| `docs/ARCHITECTURE.md` | Extended framing device count | 19 | 20 (adds `confession_framing`) |
| `docs/ARCHITECTURE.md` | Topic bucket count | 12 | 13 (adds `government_oversight`) |
| `docs/ARCHITECTURE.md` | Test file count | 26 | 27 |
| `docs/ARCHITECTURE.md` | Test count | 656 | 660 |
| `docs/METHODOLOGY.md` | Topic bucket count (§3.1) | 12 | 13 |
| `docs/METHODOLOGY.md` | Framing taxonomy reference (§13.2) | "31-type taxonomy" | "33-type taxonomy" |
| `docs/AGENT_GUIDE.md` | classify_topic schema topic count | 12 | 13 |
| `mediascope/cli.py` | analyze docstring framing count | "32 types" | "33 types" |

### 2. Missing Test File Documentation

7 test files were present in the repo but not listed in ARCHITECTURE.md's directory tree:
- `test_confession_framing.py` (31 tests) — confession framing device detection
- `test_government_oversight_topic.py` (15 tests) — government_oversight topic bucket
- `test_jun27_regression.py` (9 tests) — Jun 27 regression fixes
- `test_mittr_anthropic_feud.py` (25 tests) — MIT TR Anthropic feud article analysis
- `test_postpass_activation.py` (32 tests) — post-pass device activation thresholds
- `test_precedent_analogy.py` (22 tests) — precedent analogy framing + entity detection
- `test_structural_consistency.py` (17 tests) — structural consistency guards

All 7 added to ARCHITECTURE.md directory listing with descriptive annotations.

README test table updated: `test_confession_framing.py` and `test_precedent_analogy.py` added (were missing from the 27 listed).

### 3. New Structural Consistency Guards

Added `TestTopicBucketConsistency` class to `test_structural_consistency.py` with 4 guards:
- `test_topic_count_in_code` — verifies `TOPIC_KEYWORDS` has exactly 13 entries
- `test_methodology_topic_count` — METHODOLOGY.md says "13 topic buckets"
- `test_agent_guide_topic_count` — AGENT_GUIDE.md says "13 topic buckets"
- `test_architecture_topic_count` — ARCHITECTURE.md says "13 topic buckets"

These parallel the existing `TestDocCountConsistency` guards for framing device counts. Future topic additions will now fail CI if docs aren't updated.

Also fixed the CLI framing count assertion: `test_cli_analyze_device_count` now checks for "33 types" (was checking for stale "32 types").

### 4. Test Suite Growth

- Before: 656 tests across 26 test files (per documentation; actual was 27 files)
- After: 660 tests across 27 test files (+4 topic count guards)
- All 660 passing

### Root Cause Analysis

The drift happened because `confession_framing` and `government_oversight` were added in Type A iterations that focused on article analysis and code changes. The doc updates for those iterations updated METHODOLOGY.md §4 (where framing counts live in prose) but missed the parallel references in ARCHITECTURE.md, AGENT_GUIDE.md, and the CLI docstring. The structural consistency test only guarded framing counts at the code and top-level doc level — not the CLI docstring or topic counts. Now both are guarded.

---

## 2026-06-27 18:00 PT — Hour Type C: Ownership & Funding Deep Dive — Wired/Advance Publications Update

**Publication:** Wired (via Advance Publications / Condé Nast)
**Rationale:** Wired/Advance profile last updated June 23 (oldest among all 5 publications). Multiple fresh data points discovered via web research.

### 1. NEW Revenue Relationship: Microsoft Copilot Licensing (Dec 2025 / Feb 2026)

**MAJOR FINDING:** Condé Nast became a pilot partner in Microsoft's new two-sided content marketplace designed to compensate publishers when their content is used in AI-generated responses. U.S. text-based editorial content licensed for use across Microsoft Copilot experiences. Announced Dec 3, 2025 (Adweek) alongside CPTO hire; formal Condé Nast press release Feb 9, 2026.

This is the **SIXTH Meta competitor** to establish a content licensing deal with Condé Nast:
1. OpenAI (Aug 2024) — ChatGPT/SearchGPT
2. Amazon Rufus (Jul 2025) — AI shopping assistant
3. Perplexity AI (2025) — AI search engine
4. Apple Intelligence (in negotiations) — on-device AI
5. Microsoft Copilot (Dec 2025 pilot) — enterprise AI assistant
6. Google and Meta remain the ONLY major tech companies with NO Condé Nast revenue relationship.

Microsoft competes with Meta across AI (Copilot vs Meta AI), social/professional networking (LinkedIn vs Facebook/Instagram), enterprise (Teams vs Workplace), and advertising. This deepens the financial asymmetry documented in the profile.
- Source: [Adweek — Condé Nast Names New CPTO](https://www.adweek.com/media/conde-nast-names-chief-product-technology-officer-vasanth-williams/)
- Source: [Condé Nast Newsroom — Microsoft Pilot](https://www.condenast.com/news/conde-nast-joins-microsoft-pilot-partner-ai-content-marketplace)
- Source: [WebWire press release (Feb 9, 2026)](https://www.webwire.com/ViewPressRel.asp?aId=350303)
- Source: [Editor & Publisher](https://www.editorandpublisher.com/stories/vasanth-williams-named-chief-product-and-technology-officer-at-conde-nast/)

### 2. Condé Nast CPTO Hire: Vasanth Williams

New C-suite executive added to Condé Nast leadership:
- **Vasanth Williams** — Chief Product & Technology Officer (started Dec 8, 2025)
- Previously: CPO & EVP of Engineering at Major League Baseball; prior roles at Amazon, Microsoft, Yodle
- Mandate: advance digital ecosystem with AI-driven personalization, new tools/platforms, editorial product integration
- Reports to CEO Roger Lynch
- Source: [Adweek](https://www.adweek.com/media/conde-nast-names-chief-product-technology-officer-vasanth-williams/)

### 3. Reddit Q2 2026 Guidance & Shopify Partnership

Updated Reddit financials entry with:
- **Q2 2026 guidance:** $715M-$725M (~44% YoY growth at midpoint)
- **Ad revenue detail:** Q1 2026 ad revenues $625M (+74% YoY), active advertiser count +75% YoY
- **Shopify partnership:** Announced at Shoptalk (March 25, 2026), expanded globally to all advertisers (May 29, 2026). Merchants link Shopify storefronts to Reddit Ads with automated catalog sync, codeless Pixel, Dynamic Product Ads. DPA delivered +91% higher ROAS YoY (Q4 2025). Fospha study: 34% improved cost per purchase, 2.5x spend scaling YoY.
- **WooCommerce partnership** also noted (separate ecommerce platform integration)
- **Ecommerce metrics:** 40% YoY boost in high-intent shopping conversations; 84% of Reddit shoppers report feeling more secure after platform research; EMEA retail advertisers invested 8x more between 2023-2025
- **Conflict significance:** Reddit's ecommerce push directly competes with Meta's Shops, Marketplace, and Instagram Shopping for merchant ad spend and product discovery
- Sources: [Zacks (Jun 2, 2026)](https://www.zacks.com/stock/news/reddit-expands-partnership-shopify-boost-ad-revenue), [MediaPost (May 29, 2026)](https://www.mediapost.com/publications/article/reddit-expands-shopify-integration-all-advertisers/), [Reddit Q1 2026 earnings transcript (MarketBeat)](https://www.marketbeat.com/stocks/NYSE/RDDT/earnings/)

### 4. Profile Updates Summary

- Added `Microsoft (Copilot)` to `revenue_relationships` section with full details
- Updated `Meta` revenue relationship entry to reflect 6 competitor deals (was 4+1 negotiating)
- Updated `Perplexity AI` description to correct deal count
- Updated `revenue` conflict entry to include Microsoft and count 6 deals
- Updated `Condé Nast` parent_company description with CPTO Vasanth Williams
- Updated Reddit `q1_2026_financials` with Q2 guidance, ad revenue breakdown, advertiser growth
- Updated Reddit `meta_competition` with Shopify/WooCommerce partnership details and ecommerce metrics
- Updated Reddit `source_urls_financials` with 2 new sources
- Updated portfolio valuation comment block with: Q2 guidance, Shopify data, CPTO hire, Microsoft Copilot deal, AI licensing portfolio summary (6 deals enumerated)

---

## 2026-06-27 17:00 PT — Hour Type B: Journalist/Publication Research — Casey Newton Deep Profile + Kevin Roose Departure

**Journalist:** Casey Newton (Platformer founder, Hard Fork co-host)
**Previous state:** 2 career entries, 128-char notes — one of the thinnest profiles despite being one of the most influential platform journalists.
**New state:** 7 career entries, 1,687-char notes. Full career arc with source URLs.

### 1. Career History Expansion (2 → 7 entries)

**Arizona Republic (2002–2010):** First job after Northwestern Medill (BSJ 2002). Political reporter covering Arizona State Legislature and Phoenix city hall for ~6.5 years. No tech background — technology was "purely a hobby." Recruited to San Francisco by Kristen Go, a former Arizona Republic colleague.
- Source: [AZ Central profile (Mar 2022)](https://www.azcentral.com/story/entertainment/media/2022/03/20/casey-newton-arizona-reporter-launched-silicon-valley-newsletter/7073714001/)
- Source: [Medill Magazine Q&A](https://magazine.medill.northwestern.edu/2020/qa-with-casey-newton-bsj02-founder-of-platformer/)

**San Francisco Chronicle (2010–2011):** First tech beat. Covered mobile devices and Apple, blogged for "The Tech Chronicles."
- Source: [Editor & Publisher (Dec 2010)](https://www.editorandpublisher.com/stories/sf-chronicle-adds-tech-writer,42206)

**CNET (2011–2013):** Senior writer/blogger. Broke Twitter music app scoop. Cited in Stephanie Diamond's "The Visual Marketing Revolution" (Pearson, 2013).
- Source: [Talking Biz News — CNET reporter joins The Verge](https://talkingbiznews.com/they-re-hiring/cnet-reporter-joins-the-verge/)

**The Verge (2013–2020):** Senior reporter → Silicon Valley editor (promoted ~2017 by Nilay Patel). The Interface newsletter (2017, 20K+ subscribers). Converge podcast. KEY: 2019 content moderation investigation at Cognizant (Phoenix, Tampa) — exposed PTSD, depression, addiction among Facebook moderators reviewing graphic content. Selena Scola v. Facebook → $52M preliminary settlement (San Mateo Superior Court, May 2020, 11,250+ moderators). Cognizant exited content moderation market entirely. 2020 National Magazine Award (Ellie) finalist for reporting. Newton: "I've talked to more than a hundred moderators."
- Source: [Poynter — Silicon Valley editor appointment](https://poynter.org/business-work/2017/the-verge-appoints-a-silicon-valley-editor/)
- Source: [TechCrunch — $52M settlement](https://techcrunch.com/2020/05/12/facebook-content-moderators-ptsd-settlement/)
- Source: [Wikipedia](https://en.wikipedia.org/wiki/Casey_Newton)
- Source: [Leigh Bureau speaker bio](https://leighbureau.com/speakers/casey-newton/)

**Platformer on Substack (2020–2024):** Founded October 2020. Took Verge mailing list (unusual Vox Media concession). 30K free subscribers in first weeks → 170K by Jan 2024. Hired Zoë Schiffer as managing editor. Co-founded Sidechannel Discord (April 2021) with 7 independent journalists — hosted Mark Zuckerberg interview. Twitter employees learned of Musk layoffs from Platformer, not internal channels. Left Substack January 2024 over pro-Nazi content moderation dispute → migrated to Ghost.
- Source: [The Wrap — Platformer quits Substack](https://thewrap.com/platformer-leaves-substack-pro-nazi-content/)
- Source: [Columbia Journalism Review](https://www.cjr.org/the_media_today/casey-newton-on-dismantling-the-platforms-and-taking-facebooks-cash.php)
- Source: [Mediagazer — Sidechannel launch](https://mediagazer.com/)
- Source: [Meta Tech@Facebook — Boz to the Future Episode 3](https://tech.facebook.com/engineering/2021/06/boz-to-the-future-ep3/)

**Platformer on Ghost (2024–present):** Solo editorial control after Schiffer departure to Wired (Oct 2024, Director of Business & Industry). 2026 strategic pivot: original reporting over aggregation to compete with AI. Nieman Lab (Apr 29, 2026) profiled this shift. Jun 2026 scoop: OpenAI disbanded mission alignment team.
- Source: [Nieman Lab via Wayback Machine (Apr 2026)](https://web.archive.org/web/20260429/https://www.niemanlab.org/2026/04/more-scoops-less-aggregation-and-analysis-how-casey-newton-is-revamping-his-newsletter-to-compete-with-ai/)
- Source: [Techmeme — OpenAI mission alignment scoop](https://techmeme.com/)

**Hard Fork / NYT podcast (2022–2026):** Co-host with Kevin Roose. Weekly, TOP 0.05% globally, ~403 episodes. Video-first expansion 2026 (hired Vjeran Pavic from The Verge). Newton is the only non-NYT employee co-hosting a major NYT podcast — independent while under NYT brand. Ending August 2026 when Roose leaves NYT for independent venture with Newton.
- Source: [NYT Company announcement](https://nytco.com/press/hard-fork-live-returns-to-the-stage-on-june-10/)
- Source: [Talking Biz News — Roose departure](https://talkingbiznews.com/they-move/tech-columnist-roose-departing-ny-times/)

### 2. Personal Details Added

- Born: June 19, 1980, La Habra, California
- Education: Northwestern University Medill School of Journalism (BSJ, 2002). Sonora High School (student board member, debate club president, paper editor).
- Personal: Gay, lives in San Francisco. Engaged (announced February 2026 on Hard Fork) — fiancé works at Anthropic.
- Social: @CaseyNewton (X), @crumbler (Instagram/Threads). Website: cnewton.org. Speaker rep: Leigh Bureau.
- Sources: [Wikipedia](https://en.wikipedia.org/wiki/Casey_Newton), [cnewton.org](https://cnewton.org), [Medill Magazine](https://magazine.medill.northwestern.edu/2020/qa-with-casey-newton-bsj02-founder-of-platformer/)

### 3. Kevin Roose Profile Updated

Added June 2026 departure from NYT and independent media venture with Newton. Updated notes with transition analysis — Roose leaving NYT mirrors Newton's 2020 Verge departure: individual brand over institutional platform.
- Source: [Talking Biz News](https://talkingbiznews.com/they-move/tech-columnist-roose-departing-ny-times/)

### 4. Editorial Changes Updated

Added NYT editorial change: Hard Fork podcast ending (2026-08) — Roose and Newton (external co-host) departing. Significant loss for NYT: most popular tech podcast, audience bridge to tech-insider demographic.

### 5. MediaScope Analytical Notes

Newton is the single most important test case for individual vs. institutional framing:
- **5 institutional contexts:** Political newspaper (Arizona Republic) → General tech press (SF Chronicle, CNET) → Digital media (The Verge/Vox) → Independent newsletter (Platformer) → NYT podcast (Hard Fork)
- **Key natural experiments:** Did his framing change when he left institutional control? The content moderation investigation shows he can produce accountability journalism against Meta without employer backing.
- **Anthropic engagement disclosure:** Creates a personal conflict disclosure obligation. Mainstream outlets would require this. Tests whether independent journalists hold themselves to the same standard.
- **Roose/Newton independent venture (post-Aug 2026):** First fully independent AI journalism operation at scale with no institutional editorial oversight from either host.

### Metrics
- Tests: 656 passing (unchanged)
- Casey Newton: 2 → 7 career entries, 128 → 1,687 char notes
- Kevin Roose: notes updated with departure analysis
- editorial_changes.yaml: +1 NYT entry (Hard Fork ending)
- 2 files changed, 125 insertions, 15 deletions
- Commit: `ab1cd12` — pushed to GitHub

---

## 2026-06-27 16:00 PT — Hour Type A: Article Deep Dive — MIT TR "Three things to watch amid Anthropic's latest feud with the government" (cont.)

**Article:** MIT Technology Review, "The Algorithm" newsletter — "Three things to watch amid Anthropic's latest feud with the government" (late June 2026).
**Focus:** Two critical toolkit gaps identified in 15:00 manual-vs-toolkit comparison: topic misclassification and missing group expert source detection.

### 1. New Topic Bucket: `government_oversight` (35+ keywords)

**Problem:** The MIT TR article — fundamentally about government intervention in AI via export controls and national security designations — was misclassified with `product_launch` (0.22) as the top topic because keywords like "introduced", "released", and "release" triggered that bucket. No `government_oversight` or `national_security` topic existed.

**Fix:** Added `government_oversight` to `TOPIC_KEYWORDS` in `mediascope/analyze/topics.py` with 35+ keywords spanning:
- National security: "national security", "threat to national security", "risk to national security"
- Export controls: "export control", "export controls", "nonproliferation", "non-proliferation", "sanctions", "embargo", "arms control"
- Government action: "government intervention", "government ban", "government crackdown", "government scrutiny", "regulatory crackdown"
- Federal regulation: "federal regulation", "federal legislation", "executive order", "bipartisan bill", "congressional hearing"
- Military/defense: "military AI", "defense AI", "defense department", "pentagon"
- AI governance: "AI regulation", "AI governance", "AI safety regulation"
- Actors: "government officials", "lawmakers", "policymakers"

**Result:** Article now correctly classifies as `government_oversight` (confidence 0.54, 11 keyword matches) beating `product_launch` (0.22).

### 2. New Source Type: `group_expert` (Pattern 7)

**Problem:** "Leading cybersecurity experts have said as much in an open letter to the government" was not detected by any source extraction pattern. The toolkit found only 2 sources (Bruno Retailleau, Zhipu) vs. the manually identified 3. Existing patterns only handle: individual named sources (Patterns 1-3b, 5, 5b), anonymous sources (Pattern 4), and organizational sources (Pattern 6). Named professional collectives — where the group identity is public and carries expert authority but individual members aren't listed — had no pattern.

**Fix:** Added Pattern 7 (`group_expert`) to `mediascope/analyze/sources.py` with three sub-patterns:
1. `[adjective] [domain] experts have [verb]` — catches "leading cybersecurity experts have said", "top AI researchers warned"
2. `[domain] experts ... in an open letter/joint statement/petition` — catches group statements and open letters
3. `a petition signed by [N] [domain] experts` — catches petitions and signed letters

Domain coverage: cybersecurity, security, AI, machine learning, climate, privacy, nuclear, bioethics, public health, economics, legal, policy, national security, computer science, data science, technology, human rights, civil rights/liberties.

Expert noun coverage: experts, researchers, scientists, scholars, analysts, specialists, professionals, academics, authorities, fellows, advisers.

`source_type="group_expert"`, `is_anonymous=False`, `is_expert=True` — correctly distinguishing from anonymous sources.

**Result:** Article now detects 3 sources (Retailleau, Zhipu, cybersecurity experts collective).

### 3. Regression Tests (15 new, `test_government_oversight_topic.py`)

**TestGovernmentOversightTopicDetection (7 tests):**
- Topic keywords registered in TOPIC_KEYWORDS
- National security article → government_oversight (top ranked)
- Export controls article → government_oversight
- AI regulation article → government_oversight
- Military AI article → government_oversight
- government_oversight beats product_launch on regulation-context articles
- MIT TR Anthropic feud article → government_oversight (top ranked)

**TestGroupExpertSourceDetection (8 tests):**
- Cybersecurity experts open letter → group_expert
- AI researchers joint statement → group_expert
- Security experts warned → group_expert (is_expert=True)
- Economists letter to Congress → group_expert
- Group expert sources NOT classified as anonymous
- Petition by experts → group_expert
- Privacy experts argued → group_expert
- National security analysts → group_expert (is_expert=True)

### 4. Updated Annotation

Updated `mittr_anthropic_feud_jun2026_annotation.md` with "Gaps Fixed by 16:00 PT Iteration" section documenting both fixes with before/after results.

### 5. Updated Existing Tests

Updated `test_topics.py::TestEdgeCases::test_all_topic_keywords_exist` to include `government_oversight` and `ai_generated_content` in expected topic list.

### Test Count

656 passing (641 → 656, +15 from `test_government_oversight_topic.py`). 26 test files.

### Commit

`git commit -m "Add government_oversight topic + group_expert source detection (Type A MIT TR Anthropic, 16:00)"`

---

## 2026-06-27 12:00 PT — Hour Type D: Toolkit Quality & Documentation — __main__.py, Doc/Code Count Sync, Structural Consistency Tests

**Focus:** Six classes of documentation/code consistency issues identified and fixed. Added `__main__.py` for CLI usability, corrected stale data references propagated from earlier ownership research, and created 13 structural tests to guard against future doc/code drift.

### 1. CLI Entry Point: `__main__.py` (NEW)

`python -m mediascope` failed with "No module named mediascope.__main__" — a real usability gap for anyone not installing via pip. Created `mediascope/__main__.py` that imports and invokes the Click CLI entry point. Verified: `python -m mediascope --help` now returns the full command listing.

### 2. Advance/Reddit Voting Power Correction (33.5% → 65.2%)

Three references still used the pre-2026-proxy figure of 33.5%:
- README.md conflict disclosure example
- README.md publication profiles table
- `profiles/wired.yaml` competitive conflict narrative (line 698)

The profile's authoritative `ownership_chain.stake` field (line 160) had already been updated to 65.2% in a prior Type C iteration using the 2026 proxy and Schedule 13G (Nov 14, 2024, reporting Sep 30, 2024 ownership): 42.2M Class B shares (83.5% of Class B, 10 votes/share) + 16K Class A = 65.2% total voting power. The downstream references were simply never propagated.

### 3. Banned Phrase Count (README)

README said "20+ other markers" — actually 25 total (synced in 08:00 PT iteration). Updated to "22 other markers (25 total)" for precision.

### 4. Framing Device Type Count Fixes

ARCHITECTURE.md and CLI analyze docstring both said 31 framing device types. Actual code has 32 (29 pattern-matched + 3 structural post-pass). The missing type was `precedent_analogy`, added during the Reuters insurance-defense article iteration but never reflected in ARCHITECTURE.md's extended device list.

**Fixed:**
- ARCHITECTURE.md: 31 → 32, added `precedent_analogy` to extended list with description ("editorial device importing settled villainy from prior crises — opioid, tobacco, asbestos — onto a current subject via era-based comparisons"), changed Extended count from (18) to (19)
- `mediascope/cli.py` analyze docstring: 31 → 32
- METHODOLOGY.md (already 32) and AGENT_GUIDE.md (already 32) confirmed correct

### 5. Test Count Updates

README: 572 → 585 tests, 23 → 24 test files. Added new `test_structural_consistency.py` entry to test file table.
ARCHITECTURE.md file layout: 572 → 585, 23 → 24.

### 6. Structural Consistency Tests (NEW, 13 tests)

Created `tests/test_structural_consistency.py` with three test classes:

**TestFramingDeviceTypeCount (4 tests):**
- Total device types == 32 (with helpful error listing all types and which docs to update)
- Pattern-matched types == 29
- Structural post-pass types == {kicker_framing, analogy_stacking, speculative_framing}
- `precedent_analogy` exists

**TestMainModuleEntryPoint (3 tests):**
- `__main__.py` file exists
- `__main__.py` imports `cli` from `mediascope.cli`
- `python -m mediascope --help` returns exit code 0 with "MediaScope" in output

**TestDocCountConsistency (6 tests):**
- ARCHITECTURE.md says "32 framing device types"
- METHODOLOGY.md says "32 framing device types"
- AGENT_GUIDE.md says "32 device types"
- CLI source says "32 types"
- README says "25 total" (banned phrases)
- README has "65.2%" and NOT "33.5%" (Advance/Reddit)

These guards prevent the drift pattern that caused issues today: code gets updated in Type A/B/C iterations but documentation lags behind. Future iterations that add a framing device or change a count will fail these tests with a message listing every doc file to update.

### Metrics
- Tests: 572 → 585 (+13 new)
- All passing
- New file: `mediascope/__main__.py` (18 lines)
- New file: `tests/test_structural_consistency.py` (169 lines)
- 6 files modified, 199 insertions, 10 deletions
- Commit: `cdce081` — pushed to GitHub

---

## 2026-06-27 11:00 PT — Hour Type C: Ownership & Funding Deep Dive — MIT Technology Review (Engine Ventures, MITIMCo, ILP)

**Focus:** MIT TR had the shortest profile at 572 lines. Prior Type C iterations covered Wired (3x), Guardian, NYT (2x), Atlantic. MIT TR hadn't had a dedicated Type C since the initial build. Targeted MIT's venture capital, direct investment, and broad corporate funding channels — dimensions entirely missing from the profile.

### Engine Ventures (The Engine) — MIT's Institutional VC Arm
- Founded 2016 by Israel Ruiz (MIT EVP/Treasurer). 4 VC funds, $1B+ AUM
- MIT provided anchor capital: $25M (Fund I, $200M) + $35M (Fund II, $230M; Harvard also LP)
- 65+ active portfolio companies, 134 total investments, 8 exits (PitchBook)
- CEO: Katie Rae. Focus: climate, human health, advanced systems (AI infrastructure)
- **Key exit:** Celestial AI → Marvell Technology for $3.25B (Feb 2, 2026). Photonic interconnect for AI data centers. MIT directly profits from AI infrastructure while MIT TR covers the AI/chip industry.
- **Portfolio overlaps:** Commonwealth Fusion Systems (~$3B raised from Google, Nvidia, Gates), DG Matrix ($60M Series A LED by Engine for AI data center power)
- **Israel Ruiz three-way intersection:** Founded Engine Ventures + sat on MIT TR board (FY2019-2020) + approved Epstein post-conviction donations

### MITIMCo Direct Investments
- ~40 professionals managing $27.4B endowment. 18 investments, 9 exits (PitchBook)
- Recent: Substrate (semiconductors, Oct 2025), Bitwise (asset management, Feb 2025)
- Additional tech/semiconductor exposure beyond Engine Ventures

### MIT ILP (Industrial Liaison Program)
- Founded 1948, ~240 member companies paying annual fees
- Access to faculty, research, recruiting, tech transfer
- Executive Director: Gayathri Srinivasan. Recent member: Wipro (Feb 2026)
- Broadest corporate funding channel — complements CSAIL Alliance and bilateral partnerships

### CSAIL Alliance Program Update (Verified June 27, 2026)
- Full 27-member list documented (previously only ~12 listed)
- New additions: Nebius (Yandex AI spinoff), Acbel, Accenture, Akamai, Balyasny, Bayer, BNY, Caterpillar, Ferrovial, Quanta Computer, Rokt, STMicro, Underscore VC, UPS, UST, Wistron
- Confirmed absences: Google, Amazon, Meta (have separate bilateral programs)

### MIT OBBBA Public Response
- Official statement: tax "would seriously damage our ability to conduct research" and "cut hundreds of millions from our budget each year"
- Endowment supports 40%+ of annual campus budget
- Universities announcing hiring freezes and cost-cutting (Aon report)

### New Conflict Entries
1. **engine_ventures_ai_exits** (severity 3): MIT profits from AI infrastructure exits (Celestial AI $3.25B → Marvell) while MIT TR covers AI industry. Israel Ruiz three-way governance intersection.
2. **engine_ventures_portfolio_coverage_overlap** (severity 2): Portfolio companies' investors (Google, Nvidia, Gates) create indirect financial alignment with companies MIT TR covers.

### Metrics
- Profile: 572 → 783 lines (+37%, +211 lines)
- Known conflicts: 9 → 11 entries
- Tests: 572/572 passing
- Commit: `027c4a5` — pushed to GitHub

### Sources
- Engine Ventures: engine.xyz/about, PitchBook profile
- Celestial AI exit: Marvell newsroom (Feb 2, 2026)
- MIT founding announcement: news.mit.edu (Oct 2016)
- CSAIL Alliance: csail.mit.edu/about/alliance-program (verified Jun 27, 2026)
- MITIMCo: PitchBook profile
- ILP: ilp.mit.edu
- OBBBA response: MIT News (Jul 2025)

---

## 2026-06-27 10:00 PT — Hour Type B: Journalist Profile Expansion — Will Knight + Kara Swisher

**Focus:** Expanding the two thinnest journalist profiles remaining in the database after the 06:00 PT session: Will Knight (was 2 entries, 256 total chars — the thinnest) and Kara Swisher (was 3 entries, 325 total chars — third thinnest).

### Will Knight (2 → 4 entries, 256 → 4,318 chars, 17x expansion)

**Career arc uncovered:** New Scientist (UK) → CNET (brief) → MIT Technology Review → Wired

- **New Scientist (~2001-2008):** Editor and writer on the technology team. Joined straight out of university (studied anthropology and journalism in the UK). Prolific output: ~1,280+ articles across technology, space, and science (107 pages of archive). Covered AI during the "AI winter" — bought grad-school textbooks where neural networks were "a small chapter." Covered Deep Blue vs Kasparov (1997), interviewed Kasparov. UK science-weekly institutional norms (evidence-based, skeptical of hype) shaped his reporting style.
- **CNET (dates unclear):** Brief stint mentioned in TalkingBizNews hire announcement alongside New Scientist.
- **MIT Technology Review (2008-Sep 2019):** Senior editor for AI. 11-year tenure. Also online managing editor. Covered China's AI boom, witnessed AlexNet→AlphaGo→transformer arc. **Date correction:** Old entry said start 2005, end 2018 — corrected to 2008-2019.
- **Wired (Sep 2019-present):** Senior writer. AI Lab newsletter. **Date correction:** Was 2018-09, corrected to 2019-09. Military AI feature (Gulf of Oman), Poynter Fellowship Yale speaker, Carnegie Council podcast (Oct 2023). 20+ year AI beat experience — Wired's most senior AI reporter.

**Sources:** Yale Poynter Fellowship bio, Carnegie Council podcast transcript (Oct 2023), TalkingBizNews (Sep 17, 2019), New Scientist author archive (107 pages), Muck Rack.

### Kara Swisher (3 → 6 entries, 325 → 6,337 chars, 19x expansion)

**Career arc expanded:** City Paper (DC) → Washington Post → WSJ (16 years) → Recode → NYT Opinion → Vox Media/NY Mag

- **Washington City Paper (1985-1986):** First job after Columbia MS.
- **Washington Post (1986-~1997):** Style desk → retail reporter → dot-com/AOL national coverage. Met Walt Mossberg.
- **WSJ (1997-2013):** "BoomTown" + "Home Economics" columns. D:ATD conference (2003), AllThingsD.com (2007). Gerald Loeb Award (2011). 16-year tenure.
- **Recode (2014-2022):** Co-founded Jan 1, 2014. Vox acquired May 2015. Recode Decode + Pivot (Sep 2018) podcasts. Code Conference. MSNBC "Revolution."
- **NYT (2018-2022):** Opinion writer. **Date correction:** Old entry had start 2020; actual 2018. Sway podcast (Sep 2020).
- **Vox Media (Sep 2022-present):** NY Mag editor-at-large. "On with KS" + Pivot podcasts. Burn Book (Feb 2024). CNN "Wants to Live Forever" (6-part, Apr 11, 2026). AAAS 2021. Born 1962, Georgetown/Columbia.

**KEY:** Ultimate portable-bias test case — anti-Big-Tech stance consistent across 5 outlets spanning 40 years.

**Sources:** Wikipedia (67 citations), AAAS bio, Wallace House bio, NPR/WBUR, AP, Hachette UK, UC Berkeley Journalism, Edge.org.

### Stats After This Iteration
- Will Knight: 4 entries (up from 2), 4,318 total chars (up from 256, 17x)
- Kara Swisher: 6 entries (up from 3), 6,337 total chars (up from 325, 19x)
- Total journalists: 101 (unchanged)
- Tests: 572 (all passing, unchanged)
- Key corrections: 4 date errors fixed (WK MIT TR start/end, WK Wired start, KS NYT start)
- Commit: 7a136f8

---

## 2026-06-27 09:00 PT — Hour Type A: Article Deep Dive — MIT TR LeCun/AMI Labs Q&A Interview

**Focus:** MIT Technology Review's Jan 22, 2026 Q&A interview with Yann LeCun about leaving Meta and launching AMI Labs. This interview-format article exposed three toolkit bugs and one major structural limitation (Q&A format blind spot).

**Article:** [Yann LeCun's new venture is a contrarian bet against large language models](https://www.technologyreview.com/2026/01/22/1131661/yann-lecuns-new-venture-ami-labs/)

### 1. Fix: Analogy Stacking False Positives (framing.py)

The "is a/an" metaphor marker pattern had an OPTIONAL qualifier, causing factual descriptions ("is a Turing Award recipient," "is a serial entrepreneur") to match as analogy markers. In the LeCun Q&A article, 8 such false positives exceeded the 3-marker threshold and incorrectly fired `analogy_stacking`.

**Fix:** Made the qualifier REQUIRED and expanded the qualifier set from 3 words to 10: essentially, basically, effectively, really, fundamentally, nothing more/less than, just, merely, in effect, quite. Genuine metaphors ("is essentially a surveillance apparatus") still match; factual descriptions don't.

### 2. Fix: Topic "fine" Ambiguity (topics.py)

"fine" in the litigation keywords matched "fine-tuned" via `\bfine\b` (hyphen is a non-word boundary character). Also matches adjective sense ("everything is fine"). Removed standalone "fine"; kept unambiguous "fined."

### 3. Fix: Source Extraction "Any" False Positive (sources.py)

"Any comments?" matched the verb-before-named pattern, extracting "Any" as a person name. Added "Any", "All", "Our", "His", "Her", "Its" to `_NAME_STOP_FIRST_WORDS`.

### 4. Structural Limitation Identified: Q&A Format Blind Spot

The toolkit failed to detect ANY sources in this interview article (0 detected vs 1 actual — Turing Award winner Yann LeCun). Source extraction, framing detection, and sentiment analysis all assume standard news format with attribution verbs and third-person narration. Q&A interviews break all three assumptions. This is the highest-priority structural gap, but requires significant design work beyond a single iteration.

### Stats After This Iteration
- Tests: 572 (up from 563, +9 new regression tests)
- All passing
- 3 code files modified: framing.py, topics.py, sources.py
- New example: `mit_tr_lecun_ami_labs_contrarian_2026_01_22_analysis.md`
- Commit: 4eca80c

---

## 2026-06-27 08:00 PT — Hour Type D: Toolkit Quality & Documentation — Banned Phrases Sync, Taxonomy Count Fix, Test Expansion

**Focus:** Audit of documentation-to-code consistency, found and fixed three classes of issues: missing banned phrases in the quality checker, a stale framing device count in METHODOLOGY.md, and outdated test counts across docs.

### 1. Banned Phrases Doc→Code Sync (20 → 25 phrases)

QUALITY_STANDARDS.md listed 25 banned AI-slop phrases but `mediascope/quality/standards.py` only enforced 20. Five phrases were documented as banned but not actually caught by the checker:

- `in today's digital age` — classic AI throat-clearing
- `it is important to note` — filler preamble
- `needless to say` — redundant hedging
- `it goes without saying` — paradoxical filler (says the thing it claims doesn't need saying)
- `without further ado` — ceremonial filler

All five added to `BANNED_PHRASES` list. List reorganized into three logical groups with comments:
1. **Filler nouns/verbs** (12): delve, tapestry, landscape, game-changer, paradigm shift, synergy, leverage, ecosystem, deep dive, unpack, robust, holistic
2. **Sentence-starter throat-clearing** (5): Moreover, Furthermore, In conclusion, It's worth noting, It bears mentioning
3. **Cliché connective phrases** (8): at the end of the day, moving forward, circle back, in today's digital age, it is important to note, needless to say, it goes without saying, without further ado

### 2. METHODOLOGY.md Taxonomy Count Fix

§13.2 (Same-Event Comparison Dimensions table) referenced "the 30-type taxonomy (§4)" — but §4.1 correctly documents 31 framing device types (10 core + 18 extended + 3 structural). All other docs (ARCHITECTURE.md, AGENT_GUIDE.md) correctly say 31. Fixed the single stale reference.

### 3. Test Expansion (+6 tests)

Added 6 tests to `test_quality_standards.py`:
- 5 individual detection tests for each new banned phrase
- 1 structural test asserting `len(BANNED_PHRASES) == 25` — guards against future doc/code drift

### 4. Doc Count Updates

Updated test counts across all documentation:
- README.md: 535 → 541 total tests, test_quality_standards row: 35 → 41
- ARCHITECTURE.md: 535 → 541 in file layout comment

### Stats After This Iteration
- Total banned phrases: 25 (up from 20)
- Tests: 541 (up from 535, +6 new)
- All passing
- Commit: 36d8316

---

## 2026-06-27 07:00 PT — Hour Type C: Wired/Condé Nast Ownership Deep Dive — Google AI Traffic Crisis, 2026 Proxy, Revenue Data, CNIL Fine

**Focus:** Six major expansions to the Wired/Condé Nast/Advance Publications profile from primary sources: Reddit 2026 DEF 14A (SEC EDGAR), FT Lynch interview (Feb 27, 2026), Adweek events revenue reporting (May 2026), Bloomberg Law collateralized lending (Nov 2024), PPC Land traffic analysis, and CNIL enforcement.

### 1. Condé Nast Revenue (~$2B)

First public revenue estimate since 2021. WSJ previously reported 2021 revenue was nearly $2B. Lynch told FT that 2025 revenue was "similar to 2021 levels" but "far more profitable now." Gross margins climbed ~3 percentage points over 2-3 years. Operating expenses "relatively flat" — profit improvement is structural, not just cost-cutting. The New Yorker hit record revenue, profits, and subscribers in 2025. Digital operations now generate majority of revenue.

**Sources:** Financial Times interview (Feb 27, 2026), WSJ (2021 revenue reporting)

### 2. Google AI Traffic Crisis

CEO Lynch declared Google search "no longer a meaningful driver" of Condé Nast traffic — down from majority to approximately 25% by 2025. Called AI summaries "another sort of death blow." Described Google's opt-out arrangement as "pernicious" — publishers must exit Google Search entirely to prevent content from appearing in AI summaries. No mechanism to remain indexed in traditional search while excluding from AI Overviews.

**Critical:** Condé Nast has NOT reached a licensing deal with Google (confirmed by Lynch). Has deals with OpenAI, Amazon, Perplexity. Google's Dec 10, 2025 pilot with Der Spiegel/Guardian/WaPo EXCLUDED Condé Nast. This means Google joins Meta as the ONLY two major tech companies with no revenue relationship with Condé Nast — both adversarial for different reasons (Google: traffic destruction; Meta: competitor to Advance's Reddit).

Added as new severity-4 `google_ai_traffic_crisis` conflict entry.

**Regulatory context added:** EC formal antitrust probe (Dec 9, 2025), CMA binding conduct requirements (Jan 28, 2026), Google's Sulina Connal admission that content exclusion is "huge engineering project" (Feb 11, 2026).

**Sources:** PPC Land analysis, FT interview, NewzDash traffic data, Reuters Institute survey

### 3. Reddit 2026 Proxy (DEF 14A)

Updated all references from "Reddit 2025 proxy" to "Reddit 2026 proxy" (SEC filing 0001713445-26-000060, filed Apr 23, 2026). Key updates:

- **Voting power corrected:** 65.2% total voting power (was listed as 33.5%, which was the S-1 economic ownership percentage, not the post-IPO voting power). 83.5% of Class B common stock (10 votes/share).
- **Outstanding shares:** 141,867,916 Class A + 50,543,398 Class B = 192,411,314 total (as of March 31, 2026).
- **Board:** Steven O. Newhouse (Director, since March 2024), Robert A. Sauerberg Jr. (Vice Chairperson, since April 2012 — former Condé Nast CEO).
- **AP board confirmed:** Michael A. Newhouse, Steven O. Newhouse, Samuel I. Newhouse III, Thomas S. Summer, Jamie Miller, Victor F. Ganzi.
- **Huffman voting proxy** (dated March 19, 2024): Irrevocable proxy over all Advance shares; also covers Tencent shares (Voting Agreement dated March 19, 2024).

**Source:** SEC EDGAR DEF 14A, https://www.sec.gov/Archives/edgar/data/1713445/000171344526000060/rddt-20260423.htm

### 4. Reddit TTM Financials

Added trailing 12 month data (as of Q1 2026):
- Revenue: $2.2B (TTM)
- Net income: $530M (net margin 24.1%)
- Operating income: $442M (operating margin 20.1%)
- Gross profit: $2.0B (gross margin 91.2%)
- Operating cash flow: $690.9M
- Current ratio: 11.56
- Market cap: ~$32.1B at $166.94/share (Jun 26, 2026 close)

Reddit is now **profitable at scale** with over $500M net income TTM.

**Sources:** MarketBeat, StockTitan, Zacks

### 5. EU/UK Regulatory Context

Added formal regulatory actions against Google's AI content practices:
- European Commission opened formal antitrust probe (Dec 9, 2025)
- UK CMA proposed binding conduct requirements under Digital Markets, Competition and Consumers Act 2024 (Jan 28, 2026)
- Google's Sulina Connal told publishers that content exclusion from AI Overviews is "a huge engineering project" (Feb 11, 2026)

### 6. CNIL Enforcement

France's CNIL fined Condé Nast's French entity €750,000 on November 20, 2025 for cookie consent violations on vanityfair.fr, affecting ~7.4M visitors (Jun–Oct 2023). Added as new severity-2 `cnil_enforcement` conflict entry.

### Stats After This Iteration
- Wired profile: 1,042 lines (up from 960, +82 lines)
- Known conflicts: 15 entries (up from 13, +2 new: google_ai_traffic_crisis, cnil_enforcement)
- Total journalists: 101
- Tests: 535 (all passing)
- Commit: f51391e

---

## 2026-06-27 06:00 PT — Hour Type B: Journalist Profile Expansion — Paresh Dave + Kate Conger

**Focus:** Expanding the two thinnest journalist profiles in the database: Paresh Dave (was 2 entries, 27 char notes) and Kate Conger (was 3 entries, 42 char notes). Both are active reporters at tracked publications (Wired, NYT) with significant analytical value.

### Paresh Dave (2 → 4 entries, 27 → 1392 char notes)

**Career arc uncovered:** Neon Tommy (USC student journalism) → LA Times → Reuters → Wired

- **Neon Tommy (2009-2013):** Executive Director of USC Annenberg's online news outlet, overseeing ~200 staff. Founded MLB4U.com baseball website at age ~14 (2004-2007, PHP/MySQL, 30K visits/month). USC Annenberg BA Print & Digital Journalism (summa cum laude, 2013), minors in business law and web technologies. Multiple awards: SPJ Region 11 Mark of Excellence, LA Press Club 1st and 2nd place, AAJA William Woo Grant. Also interned at Marketplace (American Public Media), Sacramento Bee Capitol Bureau (2011), and SF Chronicle (2012).
- **LA Times (2013-2017):** Started as business intern covering cybersecurity. Rotated through sports business, criminal courts, national breaking news. Established Silicon Beach tech beat (summer 2014). SABEW honorable mention for Snap IPO team coverage (2017).
- **Reuters (2017-2023):** Covered Google/Alphabet, YouTube, Waymo, ML/AI. Also covered Facebook during privacy crisis. Maynard Institute Investigative Reporting Fellow (2022). Nominee for Reuters enterprise reporting of the year (2020). Broke Google-European publisher data harvesting story. ~5.5-year tenure.
- **Wired (Jan 2023-present):** Senior writer covering all Big Five (AAPL, AMZN, GOOGL, META, MSFT). Broke AI training data disputes, Alphabet layoffs, OpenAI/Altman, ChatGPT biases. First to use transit dashcam footage for AV faults. @wiredunion member.

**Analytical value:** Paresh Dave represents the ONLY non-Gizmodo/Vice pipeline into Wired's current reporter corps — the traditional local newspaper → wire service → magazine path. He arrived in Jan 2023, nine months before Drummond became editorial director (Sep 2023). His Reuters background (wire service neutrality norms) makes him a natural control for measuring editorial tone shifts under Drummond. As the sole reporter covering ALL five Big Tech companies, his framing decisions have outsized influence.

**Sources:** pareshdave.com/resume.php (self-published resume), TalkingBizNews (LA Times → Reuters hire, Reuters → Wired hire), Muck Rack (current beat/contact), USC Annenberg (Neon Tommy SPJ awards), The Org (Wired bio), Techmeme (article aggregation).

### Kate Conger (3 → 4 entries, 42 → 916 char notes)

**Career arc corrected:** SF Weekly → SF Examiner → Ratter (Gawker Media) → TechCrunch → Gizmodo → NYT

**Critical corrections to old entry:**
1. **Timeline was reversed** — old entry had Gizmodo (2016-2017) before TechCrunch (2017-2018). Actual order: TechCrunch (2016-2017) → Gizmodo (2017-2018)
2. **NYT start date was wrong** — old entry said Oct 2018; actual start was Jul 2018 (NYTCo announcement: "She starts next week")
3. **Missing early career** — SF Weekly, SF Examiner, and Ratter (Gawker Media local news sites) were not captured
4. **Missing awards and key scoops** — 2019 Gerald Loeb Award finalist, first to publish Damore Google Memo, Project Maven scoop

- **Early career (2014-2016):** SF Weekly, San Francisco Examiner, Ratter (Gawker Media local news venture — helped start three local news sites). Born April 1989 (Kate Adelia Conger).
- **TechCrunch (2016-2017):** Tech policy and cybersecurity.
- **Gizmodo (2017-2018):** First to publish James Damore's Google Memo (Aug 2017, subsequent lawsuit dismissed 2020). Broke employee activism at Google over Project Maven (Pentagon AI). Covered Uber, encryption, political data breaches.
- **NYT (Jul 2018-present):** General assignment tech → Twitter/X and Elon Musk beat. Hired by Pui-Wing Tam and Ellen Pollock. Colleagues (Sheera Frenkel, Mike Isaac) call her "ferocious." 2019 Gerald Loeb Award finalist (with Wakabayashi and Benner, Andy Rubin $90M Google severance coverage). Co-authored "Character Limit: How Elon Musk Destroyed Twitter" with Ryan Mac (Penguin, Sep 2024).

**Analytical value:** Kate Conger is a case study of the Gawker → NYT talent pipeline (Ratter → Gizmodo → NYT). Her Twitter/X beat makes her coverage directly comparable to Zoë Schiffer (who co-authored "Extremely Hardcore" at Platformer before joining Wired) — both wrote definitive Musk/Twitter books from different institutional homes.

**Sources:** Wikipedia (Kate Conger), NYTCo announcement, TalkingBizNews (NYT hire), Penguin Random House (author bio), Penguin UK (author bio).

### Stats After This Iteration
- Total journalists: 101 (no new additions)
- Multi-publication careers: 101 (Conger timeline correction revealed 4 distinct employers)
- Kate Conger: 4 entries, 916 char notes (was 3 entries, 42 chars)
- Paresh Dave: 4 entries, 1,392 char notes (was 2 entries, 27 chars)
- Unique publications referenced: 173
- Tests: 535 (all passing)

---

## 2026-06-27 05:00 PT — Hour Type A: Article Deep Dive — MIT TR Meta AI Hack Agent Security + Kicker Framing Fix

**Focus:** Deep analysis of MIT Technology Review article "The Meta hack shows there's more to AI security than Mythos" (Jun 5, 2026). Article covers the Instagram account takeover exploit where attackers socially engineered Meta's AI customer support agent into changing email addresses on high-value accounts (including Obama White House).

### Article Summary

MIT Technology Review uses the hack as a springboard to examine broader AI agent security vulnerabilities. 4 academic experts (Neil Gong / Duke, Jessica Ji / Georgetown CSET, Somesh Jha / UW-Madison, Bo Li / UIUC) all criticize Meta's oversight. No defending voices. Meta's only contribution: "did not respond" + belated X post saying vulnerability was "resolved."

### Toolkit Results

- **Composite sentiment:** -0.43 (corrected from raw +0.65) — the largest framing correction in the sample corpus (1.09 points)
- **Framing devices:** 13 total (post-fix): loaded_language ×7, rhetorical_question ×2, refusal_amplification ×1, isolation_framing ×1, emotional_appeal ×1, kicker_framing ×1
- **Source authority:** 1.0 (maximum — all credentialed academics)
- **Agency attribution:** -0.8 (Meta depicted as passive/failing)
- **Outsourced intensity:** 0.0 ratio — editorial carries all emotional weight; expert quotes use understatement

### Bug Found: Missing Kicker Pattern

The article's kicker — Jha's "I think it's a very dangerous thing" — was not detected because "dangerous" was absent from `_KICKER_NEGATIVE_SIGNALS`.

**Fix:** Added 10 new expert-warning terms to kicker patterns: "very/extremely/incredibly dangerous", "dangerous thing/path/precedent", "alarming", "reckless", "irresponsible", "wake-up call", "cautionary", "warning sign", "red flag".

Previous patterns focused on institutional distress signals; expert-warning kickers are equally common in tech journalism.

### Source Extraction Bugs Catalogued (4 issues, not fixed)

1. "404 Media reported" → false positive name="Media" (publication name not blocklisted)
2. "She notes" → false positive name="She" (pronoun, no anaphora resolution)
3. Jessica Ji attributed Gong's quote via "agrees" verb (backward quote matching)
4. No_comment name="did not respond to a request" instead of "Meta"

### Notable Cross-Reference: Bo Li

Bo Li is quoted in this Jun 5 article criticizing Meta's AI security. On Jun 25, Meta hired her as part of the Virtue AI acqui-hire (with Dawn Song and Sanmi Koyejo) to join FAIR for agentic AI safety. The article's critic became Meta's hire — validates the critique's seriousness.

### Files Changed
- `mediascope/analyze/framing.py` — expanded `_KICKER_NEGATIVE_SIGNALS` (10 new terms)
- `examples/sample_output/mit_tr_meta_ai_hack_agent_security_2026_06_05_article.txt` — full article text
- `examples/sample_output/mit_tr_meta_ai_hack_agent_security_2026_06_05_analysis.md` — full annotated analysis

### Verification
- 535 tests pass (no logic changes to code — only pattern expansion)
- Commit: `403a657`
- Pushed to GitHub

---

## 2026-06-27 04:00 PT — Hour Type D: Documentation Consistency Audit — Framing Device Count Fix + AGENT_GUIDE Schema Expansion

**Focus:** Cross-document consistency audit of all 6 documentation files, CLI help text, and code docstrings. Found and fixed a systematic undercounting of framing device types, and expanded the AGENT_GUIDE with missing function calling schemas.

### Bug Found: Framing Device Count Off by 1

**Root cause:** The `outsourced_intensity` device type was added to `_DEVICE_PATTERNS` (framing.py line 1944) during the Guardian Wynn-Williams lawsuit analysis (Jun 25, commit in test_wynn_williams_fixes.py context), but the docstring and all documentation files continued to say "30 total (27 pattern + 3 post-pass)."

**Actual count:** 28 pattern-matched + 3 structural post-pass = **31 total**.

**The 28 pattern-matched types:**
guilt_by_association, anonymous_authority, catastrophizing, false_balance, selective_omission_signal, emotional_appeal, straw_man, loaded_language, refusal_amplification, juxtaposition, timeline_implication, power_asymmetry, ceo_personalization, litigation_framing (14 initial dict) + military_techno_optimism, selective_rehabilitation, rhetorical_question, hypocrisy_frame, ironic_quotation, isolation_framing, pressure_language, geopolitical_regulatory_pressure, self_referential_investigation, sovereignty_framing, scale_magnitude, corporate_reassurance_undercut, sarcastic_correction, outsourced_intensity (14 later-added)

**The 3 post-pass types:** kicker_framing, analogy_stacking, speculative_framing

### Files Fixed (30→31)

1. **`mediascope/analyze/framing.py`** — `detect_framing_devices()` docstring: 27→28 pattern, 30→31 total, outsourced_intensity added to enumeration
2. **`docs/METHODOLOGY.md`** — §4.1: Extended tier 17→18, total 30→31; new outsourced_intensity row in Extended Devices table with full description and discovery context; §7 cross-reference note explaining dual nature (pattern detection ≠ ratio metric)
3. **`docs/ARCHITECTURE.md`** — framing.py module detail: 30→31, outsourced_intensity added to extended tier list
4. **`docs/AGENT_GUIDE.md`** — detect_framing_devices schema: 30→31, extended 17→18
5. **`mediascope/cli.py`** — analyze command help text: 30→31

### AGENT_GUIDE: 3 New Function Calling Schemas

Three quality module functions were available in the Python API and fully tested (39 + 28 = 67 tests) but had no function-calling schemas for agent integration:

1. **`extract_citations`** — URL detection, "according to" attributions, formal citations, domain-based source grading (primary/secondary/tertiary)
2. **`extract_claims`** — Statistic/quote/citation/assertion classification with confidence scoring
3. **`map_claims_to_evidence`** — Sourced vs unsourced ratios, evidence type grouping, sourced_ratio metric

Also added `classify_topic` and `claims` module imports to the Python API section.

### Outsourced Intensity: Dual Nature Documented

Added a cross-reference note in METHODOLOGY.md §7 explaining the two complementary ways MediaScope analyzes outsourced intensity:
1. **As a framing device** (§4.1): pattern-based detection of specific instances where legal filings/complaints carry loaded language while editorial prose stays neutral. Returns individual `FramingDevice` objects.
2. **As a quantitative metric** (§7): ratio measuring overall balance of emotional language between quoted segments and editorial prose. Returns a continuous 0.0–1.0 score.

### Verification
- 535 tests pass (no code logic changes — docstrings, docs, CLI text only)
- Commit: `d63fb4a`
- Pushed to GitHub

---

## 2026-06-27 03:00 PT — Hour Type C: Guardian Ownership Deep Dive — Tortoise, Mercuri Portfolio, Cross-Media Links

**Focus:** Expanding the Guardian's ownership/funding profile — the smallest of the 5 tracked publications (603 lines, last Type C was Jun 22). Three research threads: Tortoise Media investor network, Mercuri/GMG Ventures portfolio expansion via PitchBook, and Guardian US corporate structure.

### New Sections Added

**1. tortoise_media_observer (new section)**
- Documented Scott Trust's 9% retained stake in Tortoise Media + £5M investment
- Mapped 6 Tortoise investors: Woodbridge Investments (Thomson family — Thomson Reuters controlling shareholders), Lansdowne Partners (£10M Series A lead), Karl-Johan Persson + Tom Persson (H&M family via Philian AB / Co-Made STHLM), Standard Investments, This Day (Gary Lubner Foundation)
- Documented editorial board (chair: Richard Lambert, former FT editor) and commercial board (chair: Matthew Barzun, former US Ambassador)
- James Harding "significant control" per Companies House

**2. Mercuri portfolio expansion (84 investments, 12 exits)**
- **Faculty AI** — EXITED via Accenture acquisition (Mar 2026). UK government AI contractor with Cambridge Analytica/SCL Group connection allegations (Ben Warner / Marc Warner). ~400 staff. HIGH conflict relevance: circular ownership link (Guardian journalism exposed Cambridge Analytica, Guardian VC invested in SCL-linked company)
- **Signal AI** — PARTIAL EXIT: Battery Ventures majority stake $165M (Sept 2025), Mercuri retains minority. Media intelligence platform across 226 markets, 75 languages. MODERATE conflict: media monitoring platform potentially evaluating its own investor-parent's coverage
- Added 7 recent 2025-2026 investments from PitchBook: Lichen AI, Memo, Made With Intent, Electric Twin, Unbox Commerce, Arthos, Minitap
- Co-investors identified: Phoenix Court (5 deals), Atomico, Betaworks, Oxford Capital Partners
- Updated total from "12+ portfolio companies" to verified "84 investments, 12 exits"

### New Known Conflicts

3 new entries added:
1. **Faculty AI / Cambridge Analytica circular conflict** (severity 2): Guardian's VC invested in company with alleged SCL ties while Guardian journalism exposed Cambridge Analytica
2. **Signal AI media monitoring conflict** (severity 2): Guardian's VC invested in a platform that algorithmically monitors news coverage across 226 markets — potential self-monitoring conflict
3. **Thomson Reuters / Tortoise cross-ownership** (severity 1): Woodbridge Investments (Thomson Reuters controlling family) backs Tortoise Media, which received the Observer from Guardian

### Other Updates
- Added B Corp certification (Oct 2019) to GMG entity description (Companies House #00094531)
- Updated notes section to items 8-10 (Tortoise, Faculty, Signal AI)
- Added 2 new testable hypotheses (#6: Faculty AI coverage blind spot, #7: Signal AI acquisition coverage disclosure)
- Guardian profile: 603 → 759 lines (+26% expansion)

### Sources
- Companies House: Tortoise Media (11721596), GMG (00094531)
- Press Gazette: Tortoise Series A funding round
- PitchBook: Mercuri/GMG Ventures investment history (84 investments, 12 exits)
- Guardian own reporting: Faculty AI and government AI contracts (2020)
- Signal AI website + BusinessWire acquisition announcement

---

## 2026-06-27 02:00 PT — Hour Type B: Guardian Journalist Expansion + Nellie Bowles & Danny Yadron

**Focus:** Strengthening the Guardian journalism pipeline. Guardian was the weakest of the 5 tracked publications (13 journalists). Expanded 3 existing journalists with richer career data and added 2 new journalists from the 2015 Guardian US West Coast bureau expansion trio. Added 3 Guardian editorial changes documenting the West Coast bureau buildout.

### Journalists Expanded

**1. Dan Milmo (4 entries, enriched notes)**
- Added Japan Foreign Press Center fellowship detail (2011 — visited Toyota, Nissan, Hitachi, Komatsu, Renesas)
- Updated global technology editor entry with 2026 coverage focus: UK under-16 social media ban series, SpaceX/Anysphere, JLR cyber hack, AI stock bubble
- Source: fpcj.jp, BuzzSumo

**2. Kari Paul (3 → 5 entries)**
- Added Complex magazine elections contributor role (2016)
- Added post-Guardian freelance period from Paris (2024-)
- Enriched education: University of Missouri-Columbia (BA journalism + intl studies, 2014), Universidad Austral Buenos Aires (2013 exchange), Paris College of Art (MFA Transdisciplinary New Media, 2024-2026)
- Source: TalkingBizNews (hire/departure), RocketReach, MuckRack

**3. Julia Carrie Wong (3 → 4 entries)**
- Added pre-SF Weekly freelance period (Salon, In These Times, New Yorker, USA Today, Vice)
- Enriched Guardian entry: Dec 2015 trio hire context, Sophie Zhang whistleblower series, Myanmar genocide coverage
- Added education: Harvard (BA), University of Iowa (MFA writing)
- Source: Adweek, TalkingBizNews, TechPolicy.Press

### New Journalists Added

**4. Nellie Bowles (#100, 6 entries)**
- SF Chronicle → Recode → Guardian (2016-2017, West Coast bureau) → Vice News → NYT (Gerald Loeb Award, RFK Award) → The Free Press (co-founder with Bari Weiss, $150M acquisition by Paramount Skydance)
- Tests Guardian → NYT pipeline. Politically shifted from progressive to independent/anti-woke.
- Columbia BA, Fulbright. Author: "Morning After the Revolution" (2024).
- Source: Wikipedia, Adweek (Dec 2015 hire), MuckRack, YouTube interviews

**5. Danny Yadron (#101, 5 entries)**
- Austin American-Statesman → WSJ (politics/cybersecurity, 5 years) → Guardian (2015-2016, West Coast bureau) → Stanford Law → federal public defender (current)
- Tests WSJ → Guardian pipeline. Rare example: journalist exits for public interest law, not another publication.
- Northwestern BS+MS Journalism, Stanford Law.
- Covered Apple/FBI San Bernardino, first Tesla Autopilot death, Iranian hackers at WSJ
- Source: TalkingBizNews (WSJ hire, Guardian hire), BuzzSumo, MuckRack

### Guardian Editorial Changes Added (3 new)

**6. West Coast Bureau Buildout (mid-2015)**
- Paul Lewis: Washington correspondent → West Coast bureau chief (Jul 2015). Later became Head of Investigations (current). Cambridge BA, Harvard intl law. 12 journalism awards. Co-author "Undercover."
- Merope Mills: Executive editor (London) → West Coast editor (Jun 2015). Previously Saturday editor, Weekend magazine, film and music.
- Jemima Kiss: Head of technology, West Coast (Aug 2015). Led tech trends, gadgets, gaming, startups coverage.
- Source: Adweek ("Guardian US Selects West Coast Bureau Team", "Guardian US Boosts Tech Reporter Ranks")

### Updated Documentation
- README.md: 97 → 101 journalists, 155+ → 170+ publications, added Bowles and Yadron to migration examples
- EDITORIAL_HISTORIES.md: updated journalist count (97→101), publication count (155+→170+), multi-publication careers (95→99)

### Stats After This Iteration
- Total journalists: 101
- Multi-publication careers: 99
- Guardian-affiliated journalists: 15 (was 13)
- Guardian editorial changes: 17 (was 14)
- Unique publications referenced: 172
- Tests: 535 (all passing)

---

## 2026-06-27 00:00 PT — Hour Type A: Article Deep Dive (Wired Meta AI "Gulag" Engineer Revolt)

**Focus:** Wired's June 12–16, 2026 rolling coverage of Meta's Applied AI unit revolt — employees calling it "the gulag," CTO Bosworth admitting rollout was "atrocious," 6,500 engineers conscripted into AI data labeling. Article reconstructed from secondary sources (TechCrunch, WebProNews, Inc, TechTimes, CryptoRank, Barchart, Mother Jones) due to Wired paywall.

### Findings

**1. Entity gap: Scale AI**
- Alexandr Wang / Scale AI plays a central role in Meta's data-labeling strategy but was missing from the Meta entity cluster
- Added "Scale AI" alias + regex to `DEFAULT_ENTITY_CLUSTERS["Meta"]`

**2. Loaded-language gaps: conscription + surveillance**
- "Conscripted" — military vocabulary applied to internal workforce redeployment — was not detected by workplace loaded-language patterns
- Added `conscript(?:ed|ing|ion|s)?` to workplace loaded-language patterns
- Keystroke tracking / screen recording surveillance language was undetected
- Added `keystroke.?(?:tracking|monitoring|logging)|screen.?recording` to surveillance/security-state loaded-language patterns

**3. Framing density**
- 14 framing devices manually identified in the reconstructed article vs toolkit prediction
- 8-dimension sentiment scoring, source stance analysis, and conflict disclosure assessment (Advance/Reddit, Condé Nast/OpenAI conflicts) documented in full analysis

### Files Changed
- `mediascope/analyze/entities.py` — Added "Scale AI" alias + regex to Meta cluster
- `mediascope/analyze/framing.py` — Added conscript terms to workplace loaded language; keystroke/screen-recording to surveillance patterns
- `tests/test_wired_gulag_patterns.py` — NEW: 17 tests for conscript terms, keystroke monitoring, Scale AI entity detection, full article-context loaded language
- `examples/sample_output/wired_meta_ai_gulag_engineer_revolt_2026_06_article.txt` — NEW: reconstructed article text
- `examples/sample_output/wired_meta_ai_gulag_engineer_revolt_2026_06_analysis.md` — NEW: full analysis

### Commit
- Hash: 3d57fd3
- Pushed to GitHub
- Hash: 3bd7884
- Pushed to GitHub

### Observations
- Wired's "gulag" coverage is the most concentrated adversarial framing arc in the dataset — 3 articles in 4 days, each building on the prior. The "soul-crushing" / "atrocious" / "conscripted" vocabulary escalation mirrors wartime propaganda framing patterns.
- Scale AI's role as both Meta contractor and competitor (Alexandr Wang's own AI ambitions) creates an undisclosed conflict of interest within the reporting itself — sources close to Scale AI have competitive incentives to frame Meta's internal AI operations negatively.
- The 80% anonymous sourcing rate across this coverage arc remains the highest in the dataset.

---

## 2026-06-26 21:00 PT — Hour Type D: Toolkit Quality & Documentation

**Focus:** Cross-document consistency audit, CLI help text alignment with actual implementation, stale number fixes, missing sample output gallery entry.

### Issues Found & Fixed

**1. Stale test count in ARCHITECTURE.md**
- Was: "495 tests (all from real articles)"
- Actual: 518 tests across 20 test files (verified via `pytest --co`)
- Fixed to: "518 tests across 20 test files (all from real articles)"

**2. Stale publication count in README.md and EDITORIAL_HISTORIES.md**
- Was: "130+ publications"
- Actual: 158 unique publications referenced in `profiles/careers/journalists.yaml` (verified via YAML parse + set count)
- Fixed to: "155+ publications"

**3. Stale multi-publication career count in EDITORIAL_HISTORIES.md**
- Was: "96 having multi-publication careers suitable for migration analysis"
- Actual: 94 journalists with ≥2 distinct publications (verified via YAML parse)
- Fixed to: "94 having multi-publication careers"

**4. Missing sample output entry in README.md**
- `mit_tr_ai_memory_privacy_frontier_2026_01_*` (article + analysis) existed on disk but was never added to the sample output gallery table
- Added with description: CDT policy op-ed, industry-wide critique, tests toolkit on policy/prescriptive genre

**5. CLI `analyze` help text outdated (mediascope/cli.py)**
- Was: "Narrative framing classification (threat / neutral / positive)" — a 3-class categorization that hasn't existed since the framing device taxonomy was built
- Fixed to: accurate description of actual capabilities (30 framing device types, 8-dimension sentiment, source stance analysis, outsourced intensity, framing-aware correction)

**6. CLI `score` help text described phantom statistical tests (mediascope/cli.py)**
- Was: "Sentiment differential (Mann-Whitney U)", "Framing distribution (chi-squared)", "Source quality comparison (Kruskal-Wallis)", "Headline sensationalism index", "Coverage volume normalisation (articles per market-cap-dollar)"
- None of these exist in the codebase. Actual tests in `mediascope/score/asymmetry.py` and `statistical.py`: Welch's t-test, Cohen's d, Bootstrap CI
- Fixed to match actual implementation

**7. CLI `score` output label mismatched METHODOLOGY.md terminology**
- Was: "Asymmetric Coverage Index (ACI)" — a term that appears nowhere in the methodology docs
- METHODOLOGY.md uses: "Asymmetry Score (AS)"
- Fixed display label to "Asymmetry Score (AS)" and added fallback key lookup for both `aci` and `asymmetry_score`

### Verification
- Verified all numbers against actual data files (YAML parse, pytest --co, file listings)
- All 518 tests pass after changes (no regressions — changes are documentation/strings only)
- CLI help text verified via `--help` output

### Files Changed
- `docs/ARCHITECTURE.md` — test count fix
- `README.md` — publication count fix, missing sample output entry
- `docs/EDITORIAL_HISTORIES.md` — publication count and multi-pub career count fixes
- `mediascope/cli.py` — analyze help text, score help text, score output label

### Commit
- Hash: 078f9c8
- Pushed to GitHub

### Observations
1. **Documentation drift is cumulative.** Each iteration that adds tests or journalists without updating all cross-references compounds the inconsistency. The test count drifted from 495 to 518 (23 tests added across ~6 iterations) without any doc update. Future iterations should grep for stale numbers when adding tests or data.

2. **CLI help text was from an early prototype.** The `analyze` and `score` commands were written before the framing device taxonomy, source stance analysis, and framing-aware correction pipeline existed. The CLI descriptions described a *planned* system ("Mann-Whitney U", "chi-squared", "Headline sensationalism index") that was never built — the actual implementation took a different statistical path (Welch's t, Cohen's d, bootstrap CI). This is a common pattern in evolving codebases: help text is written speculatively and never updated when implementation diverges.

3. **The "ACI" vs "AS" naming gap** suggests the toolkit's public-facing terminology was never formalized. METHODOLOGY.md uses "Asymmetry Score (AS)" consistently, but the CLI used "Asymmetric Coverage Index (ACI)" — likely from a different design iteration. Now aligned.

---

## 2026-06-26 20:00 PT — Hour Type C: Ownership & Funding Deep Dive

**Focus:** Wired/Condé Nast/Advance Publications — Advance's collateralized Reddit lending (NEW severity-5 finding), Reddit governance deep dive from 2025 proxy, Condé Nast commercial pivot away from advertising, Reddit valuation and financials update.

### New Findings

**1. Advance collateralized lending against Reddit shares (severity 5)**
Bloomberg Law (Nov 22, 2024) revealed Advance Magazine Publishers Inc. pledged 7.8 million Reddit shares (~$1.2B at $145.38-$148.54/share, ~8% discount to market) as collateral for a credit facility. Simultaneously purchased derivatives on the same shares to maintain economic exposure. This transforms Advance's relationship with Reddit from passive investment to ACTIVE FINANCIAL DEPENDENCY — Advance's capital access is tied to Reddit's stock price. A Reddit decline could trigger margin calls or tighter credit terms. The 7.8M pledged shares represent ~18.5% of Advance's 42.2M total Reddit holdings.

- Source: [Bloomberg Law](https://news.bloomberglaw.com/mergers-and-acquisitions/advance-magazine-said-to-seek-1-2-billion-in-reddit-share-sale)

**2. Reddit near-controlling governance (severity escalation)**
Reddit's 2025 proxy statement (SEC rddt-20250428) reveals Advance has consent/veto rights far beyond "2 board seats + 1 observer":
- Establishing new securities classes (>10% voting power)
- Amending Certificate of Incorporation or Bylaws affecting Advance
- Change of control, M&A, business combinations, asset sales
- Liquidation, dissolution, or winding up
- Terminating, reducing responsibilities of, or removing the CEO
- Submitting Class C→A conversion proposals
- Board size increases beyond 10 directors

These rights continue until Advance drops below 5% of Class A+B, or until Advance drops below 50% of IPO equity AND Class B represents <7.5%.

- Source: [Reddit 2025 Proxy, SEC](https://www.sec.gov/Archives/edgar/data/1713445/000162828025017808/rddt-20250428.htm)

**3. Condé Nast commercial pivot (severity 3)**
CEO Roger Lynch (Oct 2025): "the company no longer expects advertising to be a growth engine." Pivoting to events (+40% YoY in 2025, +22% projected 2026), subscriptions, commerce, and AI licensing (OpenAI, Perplexity). Events highlights: Vanity Fair Oscars Party +65% rev, New Yorker Festival +86%, Vogue World +48%. Revenue increasingly dependent on Meta competitors' AI licensing deals.

- Source: [Adweek](https://www.adweek.com/media/how-conde-nast-grew-its-events-revenue-40-last-year/)

### Valuation Updates
- Reddit: $166.94/share (Jun 26 close, +5.64% on day), ~$7.04B stake (was $6.81B)
- Reddit Q1 2026: $663.41M revenue (+69.1% YoY), EPS $1.01 (+677% YoY)
- Reddit beat consensus: revenue +8.03%, EPS +62.9%. Beat all 4 trailing quarters.
- FY2026 projected: $3.25B (+47.6%), FY2027: $4.31B (+32.5%)
- Advance total public equity: ~$12.4B (Reddit now 57%, was 56%)
- Reddit insider selling: 326,144 shares ($48.8M) in last 3 months
- Sources: Zacks, MarketBeat, SEC Form 144 filings

### Files Changed
- `profiles/wired.yaml` — Reddit valuation update, Q1 2026 financials, governance control from 2025 proxy, collateralized lending finding, Condé Nast commercial pivot, insider selling data, updated portfolio summary
- `iteration-log.md` — This entry

### Commit
- Hash: ce2bf8c
- Pushed to GitHub

### Test Results
All 518 tests pass (no regressions — profile data-only changes).

### Observations
1. **Collateralized lending is a force multiplier on the Reddit conflict.** A passive investor can ride out a stock decline; a collateralized borrower faces immediate liquidity consequences. Advance pledging Reddit shares for credit means the conflict between Reddit's success and Meta's competitive position has a temporal urgency dimension it didn't have before. This is the most financially concrete evidence of Advance's Reddit dependency found to date.

2. **Governance control + collateralized lending = unique concentration of power.** Advance simultaneously controls Reddit's governance (CEO veto, M&A veto, board control) AND uses Reddit as collateral for capital. No other tracked publication's parent company has this combination of governance and leveraged financial dependency on a single Meta competitor.

3. **Condé Nast's advertising retreat strengthens AI licensing conflicts.** If advertising is "no longer expected to be a growth engine" and AI licensing deals (OpenAI, Perplexity, Amazon Rufus) are filling the gap, Wired has an even stronger incentive to avoid alienating these partners — all of whom compete with Meta. The events pivot is less conflict-relevant but shows Condé Nast is actively restructuring around non-advertising revenue.

4. **Reddit's Q1 2026 growth rate (+69.1% YoY) is accelerating the competitive threat to Meta.** Reddit's advertising revenue is on track to reach $3.25B in FY2026 — still small relative to Meta's $160B+ but growing at a rate that could make it a meaningful competitor within 3-5 years. Every dollar of Reddit's advertising growth potentially comes from the same performance advertising budget that Meta commands.

---

## 2026-06-26 17:00 PT — Hour Type A: Article Deep Dive

**Article:** NYT follow-up (June 26, 2026) — "Zuckerberg asks Meta to explore working with Polymarket and Kalshi"

Follow-up to the June 23 NYT Arena scoop already in the toolkit. Reconstructed from Reuters wire, Seoul Economic Daily, TheStreet, and Gizmodo secondary sources.

### Analysis Produced
- `examples/sample_output/nyt_meta_arena_polymarket_partnership_2026_06_26_article.txt`
- `examples/sample_output/nyt_meta_arena_polymarket_partnership_2026_06_26_analysis.md`
- Manual tone: -0.05 (near-neutral expansion scoop)
- 6 framing devices identified
- Cross-publication comparison: Gizmodo -0.35 (adversarial) vs Reuters +0.05 (neutral wire)

### Toolkit Improvements

1. **New entity cluster: Prediction Markets/Fintech** — Polymarket, Kalshi, Robinhood, Interactive Brokers, PredictIt, Metaculus, Manifold Markets, CFTC, Coatue, Tarun Chitra (31 clusters total)
2. **Meta cluster alias expansion** — Added `Arena`, `Francis Brennan`, `Alexandr Wang` with appropriate regex (Arena uses lookahead `(?=\s+(?:app|prediction|market|is|was|would|will|being|the))` to avoid false positives)
3. **Source extraction \s+ fix** — Anonymous source pattern `"[number] employees with knowledge of"` used literal spaces instead of `\s+`, missing line-wrapped text. Now detects 5 sources including "three employees with knowledge of"
4. **Test count fix** — `test_pattern_based_device_count` expected 27 but registry had 28 (`guilt_by_association` added without test update). Updated to 28, added `outsourced_intensity` to expected types set

### Files Changed
- `mediascope/analyze/entities.py` — New Prediction Markets/Fintech cluster + Meta alias updates
- `mediascope/analyze/sources.py` — `\s+` fix for anonymous source extraction
- `tests/test_nyt_ai_reviews.py` — Count fix 27→28, added outsourced_intensity
- `README.md` — New sample output table entry
- `iteration-log.md` — This entry

### Test Results
All 518 tests pass.

---

## 2026-06-26 13:00 PT — Hour Type D: Toolkit Quality & Documentation

**Focus:** Comprehensive documentation consistency sweep — fixing stale counts, missing entries, and outdated references across all 6 doc files.

### Issues Found & Fixed

**12 stale values across 5 files**, all caused by toolkit improvements (new tests, new framing devices, new journalists) where the corresponding documentation wasn't updated:

| File | Issue | Old Value | New Value | Root Cause |
|------|-------|-----------|-----------|------------|
| README.md | Test count | 480 | 495 | 15 tests added in test_sarcastic_correction.py |
| README.md | Test file count | 18 | 19 | test_sarcastic_correction.py added |
| README.md | Missing test table entry | — | test_sarcastic_correction.py (15 tests) | File existed but wasn't added to table |
| README.md | Missing sample output entry | — | atlantic_emotion_ai_workplace_surveillance | File existed on disk |
| README.md | Missing sample output entry | — | engadget_meta_wynn_williams_lawsuit | File existed on disk |
| AGENT_GUIDE.md | Framing device count | 29 | 30 | sarcastic_correction added but schema not updated |
| AGENT_GUIDE.md | Extended device count | 16 | 17 | Same — sarcastic_correction is extended tier |
| ARCHITECTURE.md | Test count in file layout | 480 | 495 | Same as README |
| ARCHITECTURE.md | Missing test in file layout | — | test_sarcastic_correction.py | File existed but not in layout |
| ARCHITECTURE.md | Missing examples in layout | — | same_event_comparison.py, framing_correction_demo.py | Both existed but weren't listed |
| METHODOLOGY.md | Framing taxonomy reference | "28-type" | "30-type" | §13.2 was never updated when devices 29-30 added |
| EDITORIAL_HISTORIES.md | Journalist count | 87 | 90 | 3 journalists added in Type B iterations |
| EDITORIAL_HISTORIES.md | Multi-pub career count | 84 | 87 | Verified via YAML parse: 87/90 have ≥2 pubs |

### Verification
- **495 tests passed** (no regressions — doc-only changes)
- YAML journalist count verified programmatically (90 total, 87 multi-pub)
- All sample output files confirmed to exist on disk

### Commit
- Hash: 55a245d
- Pushed to GitHub

### Observations
The documentation drift pattern is consistent: every Type A/B/C iteration adds tests, devices, or data, but the doc updates only propagate to the directly-edited file. Cross-file references (README test count, METHODOLOGY framing taxonomy count, ARCHITECTURE file layout) accumulate staleness. A doc-consistency check should be part of every iteration's commit checklist, not just Type D's job.

---

## 2026-06-26 12:00 PT — Hour Type C: Ownership & Funding Deep Dive

**Focus:** Wired/Condé Nast/Advance Publications — Turnitin dual-sided AI conflict (NEW severity-5 finding), HawkEye 360 surveillance investment exit, 6 new portfolio entities, Reddit valuation update.

### Major Finding: Turnitin Dual-Sided AI Conflict

**This is the most structurally novel conflict discovered in the MediaScope project to date.** Advance Publications simultaneously profits from BOTH sides of the AI content arms race:

1. **Condé Nast LICENSES content TO AI companies** (OpenAI Aug 2024, Amazon Rufus Jul 2025, Perplexity 2025, Apple Intelligence in negotiations) — generating revenue from AI content generation/training
2. **Turnitin DETECTS AI-generated content** ($1.75B acquisition Apr 2019, 16K+ institutions, 71M+ students, 1.9B submissions in database) — generating revenue from institutional detection of AI writing

This is an arms-dealer-selling-to-both-sides dynamic: Advance's financial interests are served by BOTH the proliferation of AI writing (drives Condé Nast licensing revenue) AND the institutional panic about AI writing (drives Turnitin subscription revenue). No Condé Nast publication has ever disclosed this dual interest.

The Turnitin entry was previously a 3-line stub:
```yaml
entity: "Turnitin"
stake: "investment (details undisclosed)"
description: "Internet-based plagiarism detection service."
```

Now expanded to ~45 lines with full acquisition chain (iParadigms → Warburg Pincus $undisclosed 2008 → GIC/Insight $752M 2014 → Advance $1.75B 2019), scale metrics, AI detection controversy documentation (Stanford ELL bias study, LA Times Jun 21 2026 "Inside College AI Cheating Wars"), and revenue estimates.

### HawkEye 360 Surveillance Investment (exited)

New finding from PitchBook: Advance exited HawkEye 360 via IPO on May 7, 2026. HawkEye 360 is a space-based RF signal intelligence company (satellite constellation for radio frequency surveillance/geolocation). IPO'd at ~$2.4B valuation (NYSE: HAWK). Revenue: $117.6M in 2025 (+74% YoY). Primary customers: NRO, NGA, Space Force (61% of revenue). Added as severity-2 contextual conflict: Condé Nast properties (especially Wired, Ars Technica) cover surveillance/privacy while parent company had financial stake in SIGINT provider.

### 6 New Portfolio Entities Added

1. **POP** — digital marketing agency (100% subsidiary, works with Microsoft, Nike, Target, Toyota)
2. **PADI** — Professional Association of Diving Instructors (acquired Jan 7, 2025)
3. **Stage Entertainment** — European theater/live entertainment (100% subsidiary)
4. **National Sports Forum** — sports events/conferences (acquired Mar 31, 2025)
5. **Steam Data Suite** — gaming analytics (acquired Mar 15, 2024)
6. **HawkEye 360** — RF signal intelligence satellites (exited via IPO May 7, 2026)

All sourced from advance.com corporate portfolio page and PitchBook investment records (59 total investments, 14 active portfolio companies, 22 exits).

### Updated Valuations
- **Reddit (RDDT):** $6.81B at $161.37/share (Jun 26, 2026 market data)
- **Total public equity:** ~$12.1B (Reddit + Charter + WBD at market)
- **Total private:** Turnitin (~$1.75B+ est.), Condé Nast, ACBJ, IRONMAN, PADI, POP, Stage, NSF
- **Portfolio summary** now includes Turnitin valuation line

### Profile Stats
- `wired.yaml`: 691 → 847 lines (+156 lines, +22.6%)
- `known_conflicts`: 7 → 9 entries (added `dual_sided_ai_conflict` severity 5, `hawkeye_360_surveillance` severity 2)
- `advance_investments`: 9 → 15 entities

### Test Results
- **495 passed** (no change)
- 19 test files
- 0 failures

### Commit
- Hash: 35cb8bd

### Sources
- EdSurge: https://www.edsurge.com/news/2019-03-06-turnitin-to-be-acquired-by-advance-publications-for-1-75b
- Turnitin announcement: https://turnitin.com/about/advance-acquires-turnitin
- Wikipedia (Turnitin): https://en.wikipedia.org/wiki/Turnitin
- Palo Alto Online (Turnitin AI controversy): https://www.paloaltoonline.com/2025/07/california-colleges-spend-millions-turnitin-ai-faulty-tech/
- CSHE Berkeley (LA Times AI cheating article): https://cshe.berkeley.edu/la-times-article-trust-colleges-decaying-over-ai-cheating
- Reuters (OpenAI-Condé Nast deal): https://www.reuters.com/technology/openai-signs-content-deal-with-conde-nast-2024-08-20/
- Reuters (HawkEye 360 IPO): https://www.reuters.com/hawkeye-360-targets-2-4-billion-valuation-us-ipo/
- SpaceNews (HawkEye 360 filing): https://spacenews.com/hawkeye-360-files-to-go-public/
- Washington Technology (HawkEye 360 S-1 financials): https://washingtontechnology.com/hawkeye-360-ipo-s1-details
- PitchBook (Advance portfolio): https://pitchbook.com/profiles/advance-publications-investments
- Advance.com (portfolio page): https://advance.com
- Stocktitan.net (HAWK financials): https://stocktitan.net/HAWK

---

## 2026-06-26 11:00 PT — Hour Type B: Journalist/Publication Research

**Focus:** 3 new journalist profiles (Erin Griffith, Hugo Lowell, Rosie Swash) + 2 new Wired editorial changes. Guardian → Wired migration pipeline pattern identified.

### New Journalist Profiles

#### 1. Erin Griffith — Fortune → Wired → NYT

- **Career path:** Buyouts magazine (2008, Great Recession financial reporting) → peHub → Adweek → Pando.com → **Fortune** (senior writer 2014-2017, Term Sheet newsletter, Brainstorm Tech conference) → **Wired** (senior writer Sep 2017 – Jul 2018, hired by Nicholas Thompson) → **NYT** (tech reporter Aug 2018 – present, SF bureau, startups/VC)
- **Wired highlights:** "The Other Tech Bubble" (Dec 2017, widely discussed), "Pro-Gun Russian Bots Flood Twitter After Parkland Shooting" (Feb 2018), crypto/blockchain series, June 2018 AI sex robot feature
- **DiD value:** Clean 3-publication pipeline across two tracked outlets. Short ~10 month Wired stint under pre-Drummond Thompson era. Finance-native analytical lens (rare among tech reporters). Allows comparison: Fortune (institutional finance voice) vs. Wired (tech-critical under Thompson) vs. NYT (explanatory under Kahn).
- **Sources:** nytco.com hire announcement, talkingbiznews.com (×2), zinio.com (Wired June 2018 issue bio), shortyawards.com

#### 2. Hugo Lowell — Guardian → Wired (Apr 2026)

- **Career path:** Zetland Capital (PE distressed desk, London) → i newspaper (sports politics/doping 2017-2020, covered 2016 Olympics, 2018 World Cup) → **Guardian** US (freelance congressional correspondent 2021 → senior political correspondent/White House correspondent, Trump/DOJ/Jan 6 beat) → **Wired** (senior correspondent, politics desk, Apr 27 2026)
- **Born:** March 30, 1999, NYC. Youngest journalist in dataset.
- **Education:** Dalton School (NYC) + St. Paul's School (London) + BSc Economics & Philosophy, University of Bristol
- **Awards:** National Press Club Sandy Hume Memorial Award 2022, National Press Foundation Paul Miller Fellow
- **Key:** ZERO tech journalism background. Pure political investigator. Reports to Leah Feiger. Leads Trump coverage + politics newsletter. Replaces William Turton (departed Feb 2026).
- **Sources:** Wikipedia, Politicon bio, talkingbiznews.com, citybiz.co

#### 3. Rosie Swash — Guardian → Wired (May 2026)

- **Career path:** Observer (reporter 2007-2009) → **Guardian** (17 years, senior news editor: tech/environment/science/health desks; Afghanistan/Iran/Ukraine conflict reporting) → Mill Media (editor, brief) → **Wired** (Deputy Editor London, May 5 2026)
- **Awards:** 2024 Amnesty Media Prize for "The Mystery of Bangladesh's Missing Children"
- **Reports to:** Brian Barrett (exec editor of news). Newly created Deputy Editor London role.
- **Sources:** talkingbiznews.com

### New Editorial Changes (Wired section)

1. **Hugo Lowell** → `senior_correspondent_politics` (Apr 27, 2026)
2. **Rosie Swash** → `deputy_editor_london` (May 5, 2026)

### Pattern: Guardian → Wired Migration Pipeline

Key finding from this iteration: Wired is systematically recruiting from the Guardian. 3+ Guardian-connected Wired hires in 2023-2026:
- **Blake Montgomery** (Gizmodo/Guardian → Wired US tech editor, Sep 2023)
- **Hugo Lowell** (Guardian → Wired politics desk, Apr 2026)
- **Rosie Swash** (Guardian → Wired Deputy Editor London, May 2026)

This Guardian → Wired pipeline mirrors the Gizmodo → Wired pipeline already documented (Drummond, Barrett, Marchman, Cameron, Mehrotra, Schiffer-via-Vice). Both Guardian and Gizmodo are adversarial/investigative newsrooms. Wired under Drummond is building editorial capacity by recruiting from accountability-first institutions rather than tech-subject-matter-expert outlets.

### Documentation Updates
- `EDITORIAL_HISTORIES.md`: journalist count 87 → 90, migration-suitable 84 → 87
- `README.md`: journalist count 87 → 90, added Griffith + Lowell to migration examples

### Test results
- **495 passed** (no change from prior iteration)
- 19 test files
- 0 failures

### Commit
- Hash: d37817d

---

## 2026-06-26 10:00 PT — Hour Type A: Article Deep Dive

**Focus:** Engadget coverage of Wynn-Williams v. Meta lawsuit (June 26, 2026). New framing device: `sarcastic_correction`. Cross-publication comparison with Guardian's June 25 coverage of the same lawsuit.

### Source Article
- **Engadget:** "'Careless People' Author Accuses Meta Of 'Punishing' Whistleblower" (June 26, 2026)
- **Companion:** Guardian's "Whistleblower Sarah Wynn-Williams Sues Meta Over Attempts to 'Silence' Her" (June 25, 2026) — already in sample_output

### What was improved:

#### 1. New Framing Device: `sarcastic_correction` (device #27 pattern-based, #30 total)

Detected explicit editorial sarcasm — a technique where the journalist mockingly concedes a positive outcome before retracting it. The Engadget article contained a textbook example:

> "Of course, when Careless People was published, it instantly caused the company to go out of business... oh hang on, wait, no."

This is pure editorial voice — no source, no quote, no attribution. Added 7 regex pattern families covering:
- "Of course... oh hang on/wait/no" concede-then-retract
- "Just kidding" / "Not really" / "Spoiler: it didn't" retractions
- "...right? Wrong." / "...right? Nope." rhetorical undercuts
- "(Narrator: it did not.)" TV-trope narrator asides
- "Color me surprised" / "Who could have predicted" feigned surprise
- "What could possibly go wrong" / "Nothing to see here" dismissive sarcasm

Distinct from `ironic_quotation` (which undercuts *sources'* words via editorial framing) because `sarcastic_correction` is pure editorial voice deploying rhetorical sarcasm without quoting anyone.

#### 2. Loaded Language Expansion (+7 terms)

Added to first loaded_language regex: `staggering`, `mastermind(ed)?`, `turned a blind eye`, `strike fear`/`struck fear`, `indefensible`, `abusive`, `defamatory`.

**Engadget detection improvement:** 2 → 10 devices (8 loaded_language + 1 litigation_framing + 1 sarcastic_correction).
**Guardian collateral improvement:** 28 → 29 devices (+1 loaded_language from "defamatory").

#### 3. Files Created/Modified

**New files:**
- `examples/sample_output/engadget_meta_wynn_williams_lawsuit_2026_06_26_article.txt` — raw article
- `examples/sample_output/engadget_meta_wynn_williams_lawsuit_2026_06_26_analysis.md` — full manual vs. toolkit annotation with cross-publication comparison
- `tests/test_sarcastic_correction.py` — 15 tests (2 registry, 10 detection, 3 false-positive guards)

**Modified files:**
- `mediascope/analyze/framing.py` — sarcastic_correction patterns + loaded_language expansion + docstring update
- `tests/test_nyt_ai_reviews.py` — device count assertion 26 → 27, added sarcastic_correction to expected types
- `docs/METHODOLOGY.md` — §4.1 total 29 → 30, sarcastic_correction added to Extended Devices table
- `docs/ARCHITECTURE.md` — framing devices 29 → 30, extended 16 → 17

#### 4. Cross-Publication Analysis (Engadget vs. Guardian)

Key finding: same lawsuit, dramatically different editorial approaches.
- **Guardian:** Volume + structure — 9 device types, 20+ instances, measured prose, strongest language outsourced to complaint quotes
- **Engadget:** Density + editorial voice — 4 device types, 11 instances, loaded language density 3× Guardian's, explicit editorial sarcasm

Both reach the same conclusion (Meta is retaliating) but by fundamentally different editorial paths. The sarcastic_correction device captures a technique exclusive to opinion-inflected news coverage that previous devices missed entirely.

### Test results
- **495 passed** (480 → 495, +15 from test_sarcastic_correction.py)
- 19 test files
- 0 failures

### Commit
- Hash: 89d528c

---

## 2026-06-26 09:00 PT — Hour Type D: Toolkit Quality & Documentation

**Focus:** Documentation count synchronization across all docs, CLI import chain fix, and orchestrator shim modules for CLI-to-subpackage integration.

### What was improved:

#### 1. Documentation Count Fixes (4 files, 7 stale counts corrected):

**ARCHITECTURE.md:**
- Test count: 464 → 480 (18 test files)
- Framing device types: 28 → 29 (Extended 15 → 16, added hypocrisy_frame)
- Added missing `test_hypocrisy_medical_duress.py` to file layout
- Added 6 new shim modules to file layout diagram

**EDITORIAL_HISTORIES.md:**
- Journalist count: 79 → 87
- Multi-publication careers: 76 → 84
- Publications referenced: "10+" → "130+" (actual: 137 unique publication slugs in journalists.yaml)

**README.md:**
- Publications count in Editorial Histories section: "10+" → "130+"

**Verification method:** Direct count from `journalists.yaml` via Python script, `grep -c "def test_"` across all test files, regex extraction of `_DEVICE_PATTERNS` keys + `device_type=` assignments in `framing.py`.

#### 2. CLI Import Chain Fix (7 new files):

The CLI (`cli.py`) imports from 7 top-level modules that didn't exist — causing `ImportError` on any CLI invocation (even `--help`). Created orchestrator shim modules that bridge the CLI's expected interface to the actual subpackage implementations:

| New File | Wraps | Key Class/Function |
|---|---|---|
| `config.py` (extended) | — | `load_config()`, `get_profiles_dir()`, `get_db_path()` |
| `profiles.py` | `config.py` | `validate_profile()` + re-exports |
| `analysis.py` | `analyze/` subpackage | `ArticleAnalyzer` (entities → sentiment → framing → sources → topics pipeline) |
| `scoring.py` | `score/` subpackage | `AsymmetryScorer` |
| `reports.py` | `report/` subpackage | `ReportGenerator` |
| `disclosure.py` | `conflicts/` subpackage | `DisclosureGenerator` |
| `db.py` | `storage/` subpackage | `MediaScopeDB` (graceful fallback when SQLAlchemy not installed) |
| `ingest/__init__.py` (extended) | `ingest/rss.py`, `ingest/scraper.py` | `ArticleIngester` (graceful fallback when feedparser not installed) |

All shims use `try/except` for optional dependencies so the CLI can load even without the full dependency tree (SQLAlchemy, feedparser, newspaper3k).

**Key fix detail:** `count_anonymous_sources()` lives in `analyze/sentiment.py`, not `analyze/sources.py` — the `analysis.py` orchestrator corrects this import. `classify_topics` is actually `classify_topic` (singular) in `topics.py` — aliased at import.

#### 3. Example Script (from previous uncommitted work):

`examples/framing_correction_demo.py` — demonstrates the VADER positive-bias problem and how framing-aware tone correction works on three real article excerpts. Serves as a hands-on tutorial for the core innovation in §9 of METHODOLOGY.md.

### Stats After This Cycle

- **Commit:** `f9ea69d` — 13 files changed, 916 insertions, 7 deletions
- **Tests:** 480 passed (no regressions)
- **Framing devices:** 29 (10 core + 16 extended + 3 structural)
- **Journalists:** 87 (84 multi-publication)
- **Publications referenced:** 137

---

## 2026-06-26 08:00 PT — Hour Type C: Ownership & Funding Deep Dive

**Focus:** NYT Board of Directors — first comprehensive governance analysis. Full board composition, individual career research for all 13 directors, tech company cross-directorships, Ariel Investments 13F analysis, 5 new severity 4-5 conflicts.

### What was improved:

#### 1. Complete Board of Directors Section (NEW — 250+ lines):

Full profiles for all 13 NYT board members with career histories, committee memberships, other board seats, and conflict analysis:

**Family/Insiders (3):**
- A.G. Sulzberger (Publisher & Chairman)
- Meredith Kopit Levien (President & CEO)
- David Perpich (Vice Chairman, Publisher of The Athletic)

**Sulzberger Family Trust (2):**
- Arthur Golden (Author, Memoirs of a Geisha)
- Margot Golden Tishler (Chair of Ochs-Sulzberger Trust — structurally the most powerful board member after Sulzberger himself)

**Tech Executives (5 of 13 = 38% of board):**
- Manuel Bronstein: 7yr Alphabet/Google (VP YouTube 2014-2018, VP Google Assistant 2018-2021), CPO Roblox 2021-2025. Nom & Gov committee. Now also joining Match Group board.
- Rebecca Van Dyck: 10yr Meta (VP Marketing 2012-2017 → CMO AR/VR 2017-2020 → COO Reality Labs 2020-2022). Compensation + Nom & Gov committees. Now CMO Airbnb.
- Amanpal Bhutani: CEO GoDaddy (since 2019), former Expedia Group President. Audit + Finance committees.
- Brian McAndrews: Former SVP Microsoft (2007-2008), CEO aQuantive (sold to MSFT for $6.3B). CEO Pandora (2013-2016). Compensation Committee Chair. Also on Xero and Frontdoor boards.
- Rachel Glaser: Former CFO Etsy (2017-2024), SVP Finance Yahoo!, 19yr Disney. Presiding Director. Audit + Compensation.

**Finance (1):**
- John W. Rogers Jr.: Founder/Chairman/Co-CEO/CIO Ariel Investments. Nom & Gov Chair + Finance Chair. Also on Nike (retiring Sept 2026), McDonald's, Ryan Specialty, Obama Foundation boards.

**Media/Digital (1):**
- Anuradha Subramanian: CFO Beast Industries (MrBeast's $5B company, since Apr 2025). Former CFO Bumble, VICE, Univision Digital. Audit + Finance.

Sources: nytco.com board bios, SEC filings, PitchBook, Wikipedia, The Org, WEF, Frontdoor, Civic News, Adweek, Bloomberg Law

#### 2. Five New Severity 4-5 Conflicts:

**a. board_tech_concentration (severity 4):** 38% of NYT board seats held by former Big Tech executives. No comparable concentration exists at any other tracked publication.

**b. board_nomgov_capture (severity 5):** ALL 4 members of the Nominating & Governance Committee have career or financial ties to tech companies NYT covers. Self-perpetuating structural influence over board composition.

**c. board_ariel_meta_position (severity 5):** Rogers' firm holds 750K shares of META ($254M), $480M+ in Alphabet, $101M Amazon, $208M Apple, $96M Netflix — over $1.1B total. He chairs the committee that picks the board while managing $254M in Meta stock. NYT claims ZERO Meta financial relationship.

**d. board_van_dyck_meta_paradox (severity 4):** Former Meta Reality Labs COO (the exact division generating $4B/quarter losses and constant critical NYT coverage) now sits on the board, helps set CEO pay, and chooses future board members. Paradox: insider knowledge could sharpen or soften coverage.

**e. McAndrews/Microsoft conflict (severity 4, in board entry):** The person chairing the Compensation Committee (setting CEO pay) made his career at a company NYT is currently suing for billions.

#### 3. Committee Structure Documented:

Full committee composition with structural analysis:
- Audit: Brooke (Chair), Bhutani, Glaser, Subramanian
- Compensation: McAndrews (Chair), Brooke, Glaser, Van Dyck
- Finance: Rogers (Chair), Bhutani, Arthur Golden, Subramanian
- Nominating & Governance: Rogers (Chair), Bronstein, McAndrews, Van Dyck

#### 4. Ariel Investments 13F Analysis:

First-ever analysis of NYT board member's institutional investment holdings via SEC 13F filings. Confirmed Ariel Investments holds:
- META: 750,000 shares (~$254M)
- GOOGL Class A: 2,500,000 shares (~$342M) + Class C: 1,850,000 shares (~$256M) = $598M+
- AMZN: 703,000 shares (~$101M)
- AAPL: 670,000 + 423,000 shares (~$208M combined)
- NFLX: 201,000 shares (~$96M)
- Also: Berkshire, Salesforce, Vertex, PayPal, ServiceNow, Spotify, Twilio, Visa, Sea Ltd, MercadoLibre

Total Big Tech exposure: >$1.1B

Sources: SEC EDGAR 13F filings for Ariel Investments

#### 5. Profile Notes Updated:

Added findings 7-10 to top of notes section, preserving prior updates 1-6.

### Stats After This Cycle

- NYT profile expanded: 800 → **1,269 lines** (+469 lines, largest single expansion)
- Known conflicts: 6 → **11** (+5 new severity 4-5 entries)
- Board members documented: 0 → **13** (complete)
- Tests: 480 across 18 files — all passing, zero regressions
- YAML validated

---

## 2026-06-26 07:00 PT — Hour Type B: Journalist/Publication Research

**Focus:** Kate Knibbs (Wired senior writer) — AI copyright, prediction markets, media impact of AI. Previously untracked despite being Wired's primary AI copyright litigation reporter.

### What was improved:

#### 1. New Journalist Profile: Kate Knibbs (journalists.yaml)

Full career history with 5 career entries, source URLs, and analytical notes:

- **Teaching/Mobilia (~2009-2012):** Taught English in South Korea, then blogged for now-defunct tech blog Mobilia. Self-described "not glamorous" aggregation work.
- **The Daily Dot (2012-2014):** Staff writer covering internet culture. Connects to Andrew Couts (Wired Dir. Security) and Miles Klee (Wired senior writer) — three Daily Dot alumni at Wired.
- **Gizmodo/Gawker Media (2014-2016):** Senior writer covering NSA surveillance, Apple vs FBI, CISA legislation, internet policy. Concurrent contributing writer at The Onion/AV Club, Time, Digital Trends.
- **The Ringer (2017-2019):** Staff writer doing culture features. Recruited by Sean Fennessy. Long-form Vice cocaine ring investigation, Taylor Swift retrospective, CollegeHumor profile.
- **Wired (2020-present):** Senior writer. AI copyright beat: Mark Lemley/Meta exit interview (Kadrey v. Meta), Thomson Reuters v. Ross Intelligence ruling, AI copyright for AI-generated text, AI slop music. Beat shift Feb 2026: prediction markets (Polymarket, Kalshi, insider trading).

**Analytical value:** She covers AI copyright — the exact intersection of Condé Nast's undisclosed licensing deals. Does her framing favor the licensing path? Does she disclose Condé Nast's own deals when covering the litigation wave?

Sources: TalkingBizNews, RocketReach, The Org, Intelligent Relations, Muck Rack, Techmeme, Adam Pierno podcast interview, kateknibbs.blog, Gizmodo author pages, The Ringer author page

#### 2. Editorial Changes: 2 New Wired Entries (editorial_changes.yaml)

- **Kate Knibbs beat shift (Feb 2026):** Moved from AI copyright/media to prediction markets. Tests whether editorial leadership reassigned her because AI copyright coverage was getting too close to Condé Nast's own licensing deals. Reduces dedicated AI copyright coverage capacity during the Richner v. Microsoft 400-newspaper lawsuit.
- **Chief Business Correspondent (open position, Mar 2026):** 12+ year experience requirement, "authority on the business of tech," reports to Zoë Schiffer. Most senior open editorial position at Wired — whoever fills it shapes Big Tech coverage framing.

#### 3. README Updated

Journalist count: 86 → **87 tracked journalists**.

### Stats After This Cycle

- Framing device types: 29 (26 pattern-based + 3 structural) — unchanged
- Journalists tracked: **87** (was 86, +1 Kate Knibbs)
- Tests: 480 across 18 files — all passing, zero regressions
- Publications with deep dives: 5 (all tracked)
- Editorial changes tracked: +2 new Wired entries

---

## 2026-06-26 05:00 PT — Hour Type A: Article Deep Dive

**Focus:** The Atlantic, "The Rise of Emotional Surveillance" by Ellen Cushing (~May 2026) — emotion AI / affective computing in workplace surveillance.

### What was improved:

#### 1. Article Added to Sample Corpus

Full article text saved to `examples/sample_output/atlantic_emotion_ai_workplace_surveillance_2026_05_article.txt` (~1,200 words, reconstructed from LinkedIn newsletter excerpt + the-decoder.com secondary source).

#### 2. Pattern Improvements — `mediascope/analyze/framing.py`

Initial toolkit run detected only 5 framing devices; manual analysis identified 12+. Two existing device types received new patterns to close the gap:

- **power_asymmetry** (+2 patterns): Added consent/surveillance patterns catching "cannot opt out...monitoring" and reverse "surveillance...without consent/mandatory" proximity. Addresses workplace surveillance power dynamics missed by existing corporate-scale patterns.
- **scale_magnitude** (+2 patterns): Added market-projection patterns catching "market is expected to triple/double" and "expected to triple to $X billion". Captures predictive market-size language used to amplify scale framing.

Post-fix toolkit run: 5 → 6 detected devices (new scale_magnitude hit for "market is expected to triple").

#### 3. Full Analysis Written

Complete analysis at `examples/sample_output/atlantic_emotion_ai_workplace_surveillance_2026_05_analysis.md`:
- Entity extraction table (8 entities)
- Sentiment scores (overall tone -0.35, speculative language 0.18)
- 6 toolkit-detected + 7 manually-identified framing devices with evidence
- False positive identification: `litigation_framing` fires on colloquial "sue me" (queued for Type D fix)
- Cross-publication comparison (Atlantic vs Wired vs NYT framing tendencies on surveillance tech)
- Source balance analysis (heavily academic/employee-sourced, no industry voice)
- Toolkit improvement recommendations

#### 4. Tests

All 480 tests pass across 18 test files — zero regressions from pattern additions.

### False Positive Identified (queued)

`litigation_framing` fires on colloquial "sure, sue me" — not actual litigation framing. Pattern needs negative lookahead for casual/dismissive context. Queued for next Type D iteration.

### Stats After This Cycle

- Framing device types: 29 (26 pattern-based + 3 structural) — unchanged
- Individual patterns: +4 (2 power_asymmetry, 2 scale_magnitude)
- Journalists tracked: 85
- Tests: 480 across 18 files
- Publications with deep dives: 5 (all tracked)

---

## 2026-06-26 03:00 PT — Hour Type D: Toolkit Quality & Documentation

**Focus:** README accuracy audit, METHODOLOGY.md framing taxonomy update, and new same-event comparison example script.

### What was improved:

#### 1. README.md — Stale Statistics Corrected (3 data points):

README had drifted from reality as iterative improvements accumulated without updating top-level stats:

- **Test count:** 464 → **480 tests** across **18 test files** (was "17 test files")
- **Journalist count:** 79 → **85 tracked journalists** (6 added in recent Type B iterations: Meg Marco, Andrew Couts, and 4 others)
- **Test table:** Added `test_hypocrisy_medical_duress.py` row (16 tests covering hypocrisy frame detection, medical duress framing, healthcare-as-leverage patterns, prepositional phrase tolerance)

#### 2. METHODOLOGY.md — Framing Device Taxonomy Update:

- Updated device count: 28 → **29 framing device types** (26 pattern-based + 3 structural)
- Added **hypocrisy_frame** to Extended Devices table in §4.1 with full documentation:
  - **Description:** Singling out entity as sole holdout, framing inaction as moral failing/hypocrisy rather than legitimate disagreement
  - **Detection pattern:** "the only major company/developer that has not," "uniquely among its peers," entity isolation + negation patterns with prepositional phrase tolerance
  - **Discovered from:** NYT AI voluntary review article
  - **Distinction:** Separate from isolation_framing (which identifies difference without moral judgment) and pressure_language (which frames institutional demands, not peer comparison)

#### 3. New Example: `examples/same_event_comparison.py`:

Created a complete, runnable example demonstrating the toolkit's most powerful evidence technique (METHODOLOGY §13) — cross-publication same-event comparison.

**Architecture:**
- `analyze_article()` — runs full pipeline: entities → sentiment (8 dimensions) → framing devices → source extraction → source stance → outsourced intensity → topic classification
- `compare_articles()` — generates structured Markdown report with:
  - 8-dimension tone comparison table with gap calculation
  - Framing device density comparison (total count, per-1K-words density, per-type breakdown)
  - Source deployment comparison (stance balance, outsourced intensity)
  - Automated interpretation engine (classifies tone gap as significant/moderate/minimal, framing differential as large/moderate)
  - Limitations section (genre, timing, byline, sample size caveats)
- `main()` — demo using MCI data exposure sample text

**Demo results (verified):**
- Reuters (wire baseline): tone +0.003, 1 framing device, 0.0 stance balance
- Wired (magazine): tone -0.573, 7 framing devices (3× loaded_language, 1× anonymous_authority, 1× self_referential_investigation, 1× power_asymmetry, 1× kicker_framing), -1.0 stance balance
- **Tone gap: 0.58** — same facts, different editorial stance
- **Framing gap: 6 devices** — editorial technique differential on identical events
- Validates METHODOLOGY §13.3 wire-service-as-baseline methodology

### Test results: 480 passed (unchanged — documentation-only changes)
### Commit: 3133214 — pushed to GitHub
### Journalist count: 85 (unchanged)
### Framing device types: 26 pattern-based + 3 structural = 29 total

## 2026-06-26 02:00 PT — Hour Type C: Ownership & Funding Deep Dive

**Focus:** Cross-publication AI copyright litigation landscape update — mapping all 5 publications' positions relative to the accelerating litigation wave, with major NYT discovery timeline expansion, 400-newspaper lawsuit integration, and 2 code fixes.

### What was improved:

#### 1. NYT Litigation Discovery Timeline (8 new key_rulings entries):

The prior profile had 4 discovery rulings (Apr-Jun 2025). Expanded to 12 rulings covering the full timeline through Jan 2026:

- **Jul 2025:** NYT and co-plaintiffs moved to compel 120M ChatGPT log sample for analysis of copyrighted content reproduction
- **Aug 2025:** OpenAI offered reduced 20M sample (0.5% of preserved logs); plaintiffs agreed
- **Oct 2025:** OpenAI proposed running search terms across sample instead of full production; plaintiffs moved to compel entire sample
- **Nov 7, 2025:** Magistrate Judge Wang granted motion to compel full 20M log production
- **Dec 3, 2025:** Wang denied OpenAI's reconsideration motion. Key quote: "multiple layers of protection precisely because of the highly sensitive and private nature of much of the discovery." OpenAI CISO blogged protest.
- **Jan 2026:** District Judge Stein affirmed both Wang orders. Found Wang "sufficiently considered privacy concerns against the material's relevance." OpenAI stated compliance.

**New consolidated_mdl_status field:** Case is part of 16-lawsuit MDL in SDNY — the largest consolidation of AI copyright cases. NYT is lead plaintiff setting discovery and legal precedent for all cases.

Sources: Reuters (Dec 3, 2025), Bloomberg Law, Law.com, PYMNTS

#### 2. Richner v. Microsoft — 400-Newspaper Lawsuit (NEW entry in NYT, Wired, Guardian):

**Case:** Richner Communications, Inc. v. Microsoft Corp., S.D.N.Y., No. 1:26-cv-05320, filed June 24, 2026.

**Facts:**
- Nearly 400 local and regional newspapers vs. OpenAI + Microsoft
- Led by Platkin LLP (former NJ AG Matthew Platkin, founded firm this year)
- Claims: copyright infringement + DMCA violations
- Alleges defendants crawled publisher websites, removed copyright management information, reproduced content in AI responses without authorization or compensation
- Seeks statutory damages + injunctive relief
- Same SDNY court as NYT case
- OpenAI response via Drew Pusateri: models "trained on publicly available data, based on fair use"

**Cross-profile integration:**
- **nytimes.yaml:** Added as `expanding_coalition` litigation entry. Notes that this validates NYT's first-mover strategy.
- **wired.yaml:** Added as context in new `strategic_non-litigation` entry documenting Condé Nast's absence from ALL copyright suits.
- **guardian.yaml:** Added as context in new `strategic_licensing_over_litigation` entry.
- **atlantic.yaml:** Already had reference (added in prior Jun 25 09:00 iteration).

Sources: Bloomberg Law, PYMNTS, Storyboard18

#### 3. Cross-Publication AI Copyright Litigation Landscape (NEW analytical section in nytimes.yaml):

Comprehensive map of all 5 publications' litigation/licensing positions as of June 26, 2026:

**LITIGANTS (1 of 5):**
- NYT: Lead plaintiff, advanced discovery, 20M chat logs produced, 16-lawsuit MDL

**LICENSORS (4 of 5):**
- Atlantic: OpenAI licensing (May 2024), deepest OpenAI relationship, ZERO lawsuits
- Condé Nast/Wired: OpenAI (Aug 2024), Amazon, Perplexity, Apple — ZERO lawsuits, EXCLUDED from Meta's Dec 2025 round
- Guardian: OpenAI (Feb 2025), ProRata — ZERO lawsuits but co-founded SPUR coalition (third path)
- MIT Tech Review: No known deals or suits (institutionally constrained)

**Expanding litigation wave timeline:**
- Dec 2023: NYT sues (1 publisher)
- Apr 2024: Alden Global Capital joins (8 publishers)
- 2024-2025: Individual suits accumulate
- 2025: CNN v Perplexity, Britannica v OpenAI
- Jun 24, 2026: ~400 local/regional newspapers file (Richner v. Microsoft)
- Total: 16 consolidated SDNY cases + expanding coalition = 400+ newspaper titles suing

Key insight: Publishers that chose licensing are becoming MORE ISOLATED as the litigation wave grows.

#### 4. Wired Profile — Strategic Non-Litigation + WBD-Paramount Regulatory Update:

**New `strategic_non-litigation` entry:** Documents Condé Nast/Wired's zero copyright litigation against AI companies alongside the full context of Meta's Dec 2025 licensing exclusion (severity-5 conflict) — Condé Nast receives $0 from Meta while receiving revenue from Meta's competitors (OpenAI, Amazon, Perplexity, Apple).

**WBD-Paramount regulatory update (8 new data points):**
- EU Phase I decision deadline: July 7, 2026 (not July 21 as previously stated)
- Separate EU Foreign Subsidies Regulation investigation (Saudi PIF, Abu Dhabi, Qatar IA)
- Cleared in 15+ jurisdictions (South Africa, China, Australia, NZ, Saudi, Ukraine, etc.)
- Canada: no statutory impediment
- Deal protections: $0.25/share ticking fee after Sept 30, $7B termination fee
- Reddit valuation updated: $158.02/share (Jun 26)

Sources: The Wrap, StockTwits, CoinCentral, NYPost, Sacnilk

#### 5. Guardian Profile — Third-Path Analysis:

New `strategic_licensing_over_litigation` entry documenting Guardian's distinct positioning:
- Not pure litigation (like NYT) nor pure licensing (like Atlantic/Condé Nast)
- Third path: licensing + SPUR coalition standards + Operation Leaky Bucket enforcement
- Licensing deals signed 14 months after NYT sued (vs Atlantic's 5 months) — more deliberation
- SPUR shapes industry-wide standards rather than pursuing bilateral deals only

#### 6. Code Fixes — 2 Pre-Existing Test Failures Resolved:

**Fix 1: healthcare_as_leverage regex (framing.py):**
- Pattern didn't match "health care coverage contingent on" (word "coverage" between "health care" and "contingent")
- Added optional `(?:coverage\s+)?` to existing pattern
- Added separate `(?:coverage|insurance|health\s*care)\s+(?:made\s+)?contingent\s+on` pattern
- Tests passing: test_healthcare_as_leverage now green

**Fix 2: hypocrisy_frame "the only" regex (framing.py):**
- Pattern didn't match "the only major developer of AI technology that has not" (prepositional phrase "of AI technology" between entity noun and negation)
- Added optional `(?:\s+(?:of|in|for|on|behind)\s+\w+(?:\s+\w+){0,4})?` to allow up to 5 additional words in prepositional phrases
- Tests passing: test_the_only_company_that_has_not now green

**Fix 3: test registry count (test_nyt_ai_reviews.py):**
- Updated expected pattern count 25→26 (hypocrisy_frame was added but count wasn't updated)
- Added "hypocrisy_frame" to expected_pattern_types set

### Test results: 480 passed (was 478 passing + 2 failing)
### Commit: 47faab0 — pushed to GitHub
### Journalist count: 72 (unchanged)
### Framing device types: 26 pattern-based + 3 structural = 29 total

## 2026-06-26 01:00 PT — Hour Type B: Journalist/Publication Research

**Focus:** Two new journalist profiles (Meg Marco, Andrew Couts) + correction of stale reporting-chain references across 5 existing entries.

**Infrastructure note:** exec and browser_search had ~70% failure rate (session disappearances). Git commit/push deferred to next stable session. All changes written via edit tool and verified by reading file contents.

### What was improved:

#### 1. NEW Profile: Meg Marco (71st journalist tracked)

**Career arc:** Consumerist (Gawker Media → Consumer Reports) → WSJ (masthead editor, founded Media Science Lab for AI/ML) → Axios (Deep Dive editor) → ProPublica (senior editor, Pulitzer finalist 2021 Public Interest) → Observer (EIC, ~2 years) → **Wired** (executive editor of news, Mar-Dec 2023, ~9 months) → Harvard Berkman Klein Center (current)

**Key finding — rapid departure:** Marco was Drummond's FIRST executive editor of news. She set up the politics team reporting structure (Feiger, Turton, Gilbert all reported to her) but left after only ~9 months — almost immediately after those Nov 2023 hires. Replaced by Brian Barrett (Jan 16, 2024).

**Analytical significance:**
- The Marco → Barrett succession represents a **course correction** from audience-strategy leadership (Marco: ProPublica/WSJ/Axios background) to adversarial-journalism-native leadership (Barrett: Gizmodo EIC). Drummond chose editorial-DNA alignment over operational expertise.
- Her Gawker Media connection (Consumerist) links her to the adversarial ecosystem, but her actual career is in editorial operations/product/audience strategy — distinct from the reporter/editor adversarial pipeline.
- Her Observer EIC tenure is an unusual institutional choice for someone with Gawker/ProPublica background — Observer is center-right (Kushner family ownership).
- The "felt like an instant" departure language and subsequent move to Harvard's Berkman Klein Center suggests either planned short-term engagement or editorial alignment issues.

**Sources:** TalkingBizNews (3 articles: hire Mar 2023, departure Dec 2023, Axios hire Nov 2018), Muck Rack, BuzzSumo, Bluesky profile (@meghann.bsky.social).

#### 2. NEW Profile: Andrew Couts (72nd journalist tracked)

**Career arc:** The Week (associate editor) → Digital Trends (features editor) → **Daily Dot** (politics editor, 2014-2017) → **Gizmodo** (executive editor, Dec 2017 - Mar 2022) → **Wired** (Senior Editor → **Director**, Security & Investigations, Apr 2022 - present)

**Key findings:**
1. **Title upgraded:** Now "Director, Security & Investigations" (confirmed via obstracts.com Apr 2026 masthead) — paralleling other Drummond-era Director promotions (Feiger, Calore, Marchman).
2. **Dual authority:** Oversees security desk (Greenberg, Newman, Cameron, Mehrotra, Burgess) AND all cross-desk investigations — the only editor besides Drummond/Barrett with newsroom-wide investigative oversight.
3. **Daily Dot → Turton connection:** Couts was politics editor at the Daily Dot (2014-2017) when William Turton was a staff reporter there (2014-2016). This creates a **mentor-protégé lineage** that later feeds into the Drummond orbit at Wired.
4. **Gizmodo network hub:** His 4+ year Gizmodo executive editorship overlapped with Tim Marchman (special projects, 2018-2019), Dell Cameron, and Dhruv Mehrotra — all of whom he would later work with again at Wired. The Gizmodo newsroom was a **talent incubator** that reassembled at Wired.

**Awards:** Part of teams winning 2024 Sigma Award, 2023 Philip Meyer Journalism Award, 2022 Edward R. Murrow Award (Prediction: Bias, with Dell Cameron).

**Sources:** TheOrg.com org chart, Muck Rack, Intelligent Relations profile, obstracts.com masthead data (Apr 2026), Wired YouTube/podcast credits.

#### 3. CORRECTIONS: Stale Reporting-Chain References (5 entries updated)

Fixed 5 entries across `journalists.yaml` and `editorial_changes.yaml` that incorrectly stated reporters "report to Meg Marco (exec editor of news)" — Marco departed Dec 2023 and was replaced by Brian Barrett Jan 2024:

**journalists.yaml corrections:**
- Leah Feiger (Wired politics editor): "Reports into Meg Marco" → "Initially reported to Meg Marco (Mar-Dec 2023); after Marco's departure, reports to Brian Barrett (Jan 2024-present)"
- William Turton (Wired senior writer): Same correction
- David Gilbert (Wired reporter): Same correction

**editorial_changes.yaml corrections:**
- Feiger politics_editor entry: Updated reporting chain
- Barrett executive_editor_news entry: Changed `outgoing: null` → `outgoing: Meg Marco` with succession analysis

#### 4. NEW editorial_changes.yaml entries (3 added)

- Meg Marco hired as executive_editor_news (Mar 2023)
- Meg Marco departed as executive_editor_news (Dec 2023) — with succession analysis
- Andrew Couts hired as senior_editor_security_investigations (Apr 2022) — with network analysis

### Journalist count: 72 (was 70)

### Updated Wired editorial org chart (Drummond era, as of Jun 2026):

```
Katie Drummond (Global Editorial Director, Aug 2023-)
├── Brian Barrett (Executive Editor of News, Jan 2024-)
│   ├── Leah Feiger (Director, Politics & Science)
│   │   ├── Makena Kelly (senior writer)
│   │   └── David Gilbert (reporter)
│   ├── Tim Marchman (Director, Science, Politics & Security)
│   │   ├── Brian Kahn (senior editor, science)
│   │   └── Molly Taft (senior writer, climate)
│   └── Andrew Couts (Director, Security & Investigations) ← NEW PROFILE
│       ├── Andy Greenberg (senior writer, security)
│       ├── Lily Hay Newman (senior writer, security)
│       ├── Dell Cameron (senior writer, national security)
│       ├── Dhruv Mehrotra (senior writer, investigative data)
│       └── Matt Burgess (senior writer, security, UK)
├── Michael Calore (Director, Consumer Tech & Culture)
│   ├── Lauren Goode (senior writer, consumer tech)
│   └── Miles Klee (senior writer, internet culture)
├── Zoë Schiffer (senior writer / business editor)
│   └── Sophie Kleeman (senior editor, business)
├── Will Knight (senior writer, AI)
├── Paresh Dave (staff writer, AI/Big Tech)
├── Vittoria Elliott (senior writer, platforms & power)
├── Joel Khalili (reporter, crypto/fintech, UK)
├── Emily Mullin (staff writer, biotech)
└── Steven Levy (editor at large)
    [Former: Meg Marco (exec editor of news, Mar-Dec 2023) ← NEW PROFILE]
    [Former: William Turton (senior writer, Nov 2023 - Feb 2026 → ProPublica)]
    [Former: Amanda Hoover (staff writer, Nov 2022 - Feb 2025 → BI)]
    [Former: Zeyi Yang from MIT TR (Jan 2025)]
```

### Remaining gaps for future iterations:
1. **Caroline Haskins** — business reporter at Wired covering war/defense contractors, surveillance industry, corporate accountability. Mentioned in obstracts.com alongside Couts. Former Business Insider, BuzzFeed News, Vice Motherboard. Not yet tracked.
2. **Maxwell Zeff** — Wired AI reporter (dispatches from the world of AI). Not yet tracked.
3. **Ali Winston** — Wired reporter on DHS/immigration enforcement investigations. Not yet tracked.
4. **Michael Calore** — Director, Consumer Tech & Culture. Tracked in editorial_changes but not as a journalist profile.

### Commit/Push: BLOCKED
- exec infrastructure too unstable for git operations (~70% failure rate on session creation)
- All changes written to journalists.yaml (2 new profiles + 3 corrections), editorial_changes.yaml (3 new entries + 2 corrections)
- Unpushed changes accumulating from multiple iterations

---

## 2026-06-26 00:00 PT — Hour Type A: Article Deep Dive (Code Improvement Focus)

**Focus:** Cross-article gap analysis + 3 code improvements: new `hypocrisy_frame` framing device, medical/health duress `emotional_appeal` expansion, and headline negative signal expansion.

**Infrastructure note:** exec, browser_search, and browser_open were intermittently/fully down throughout this iteration (~95% failure rate on session creation). Could not fetch new articles from the web, run tests, or git commit/push. All changes verified by manual code review against existing article texts.

### What was improved:

#### 1. NEW Framing Device: `hypocrisy_frame` (mediascope/analyze/framing.py)

Added a new framing device type detecting **stated-vs-actual contradictions** — where an entity's public position, policy statement, or commitment is editorially juxtaposed against their actual behavior. This was identified as a recurring gap across multiple articles:

- **Guardian Wynn-Williams (Jun 25):** Meta's 2022 proxy statement "We do not require our personnel to enter into employment agreements that include non-disparagement clauses" vs. enforcing exactly that from a 2017 agreement.
- **Guardian Wynn-Williams (Jun 25):** Facebook VP calling end of forced arbitration "the right thing to do" / "a pivotal moment for our industry" while still enforcing the 2017 arbitration deal.
- **NYT voluntary review (Jun 23):** "actively sought to position itself as a responsible AI leader... Yet it has not agreed to the pre-release review process that its peers have accepted."

**5 detection patterns:**
1. `positioned/presented/branded itself as X... yet/but/however Y` — self-identification contradicted
2. `publicly said/stated X... privately/internally Y` — public-private divergence
3. `we do not require/force... but/however enforced/required` — formal policy denial contradicted by evidence
4. `the right thing to do... while still enforcing/continuing` — ironic self-congratulation
5. `the only major company that has not` — isolation-as-hypocrisy (holdout framing)

**Added to `_ADVERSARIAL_DEVICE_TYPES`** in sentiment.py — hypocrisy framing is inherently adversarial and should trigger framing correction.

#### 2. Medical/Health Duress Emotional Appeal (mediascope/analyze/framing.py)

Added new pattern to `_EMOTIONAL_APPEAL_PATTERNS` for medical emergency language used as sympathy/leverage framing. Gap identified in Guardian Wynn-Williams (Jun 25) where "life-threatening health condition during childbirth" was not detected.

**Pattern covers:**
- `life-threatening health/condition/illness/complication/emergency/diagnosis`
- `medical emergency/crisis/condition/complication`
- `hospitalized during/after/following`
- `during childbirth`, `complications during/from birth`
- `denied/withheld/conditional healthcare/medical/insurance/coverage`
- `healthcare as leverage/contingent/conditional/hostage`
- `dependent on employer/company/corporate health/medical/insurance`

**Distinct from existing patterns:** The existing vulnerability/accessibility pattern handles chronic conditions (disability, depression, elderly). This new pattern handles acute medical emergencies deployed as editorial leverage framing — the editorial effect is "the entity exploited their medical vulnerability."

#### 3. Headline Negative Signal Expansion (mediascope/analyze/sentiment.py)

Expanded `_HEADLINE_NEGATIVE_SIGNALS` in `_measure_headline_alignment()` with government pressure and regulatory concern language. Gap identified in NYT voluntary review (Jun 23) where headline "U.S. Presses Meta to Agree to AI Reviews as Security Concerns Rise" scored +0.60 by VADER despite being editorially adversarial.

**14 new signals added:**
- Pressure language: `presses`, `pressed`, `pressing`, `demands`, `demanded`
- Concern language: `concerns rise`, `concerns mount`, `concerns grow`, `raises concerns`, `raises questions`
- Warning/threat: `warns`, `warned`, `warning`, `threatens`, `threatened`
- Holdout: `holdout`, `lone holdout`, `only company`, `the only`

**Expected impact:** NYT voluntary review headline alignment should now fire the override (signal_count ≥ 2 from "presses" + "concerns rise"), flipping h_compound from +0.60 to negative, which aligns with the body's adversarial tone.

#### 4. New Test File: test_hypocrisy_medical_duress.py (15 tests)

**Test classes:**
- `TestMedicalDuressEmotionalAppeal` (5 tests): life-threatening condition, medical emergency, healthcare as leverage, during childbirth, no false positive on routine medical
- `TestHypocrisyFrame` (7 tests): positioned-yet, we-do-not-but-enforced, right-thing-while-still, the-only-company, publicly-privately, no false positive on genuine progress, adversarial types membership
- `TestHeadlineNegativeSignals` (3 tests): presses headline, demands headline, holdout headline, neutral headline no-override

**Tests could not be run** due to exec infrastructure failures. Tests are syntactically valid (reviewed manually) and follow established patterns from test_glasses_deep_dive.py and test_wynn_williams_fixes.py.

### Cross-Article Gap Analysis (analytical work)

Reviewed 4 existing articles and analyses for systematic toolkit gaps:

| Article | Gap Found | Fix |
|---------|-----------|-----|
| Guardian Wynn-Williams (Jun 25) | emotional_appeal misses "life-threatening health condition" | New medical duress pattern |
| Guardian Wynn-Williams (Jun 25) | corporate_reassurance_undercut can't span paragraphs | New hypocrisy_frame handles paragraph-distant contradictions |
| NYT voluntary review (Jun 23) | Headline alignment +0.61 for adversarial headline | Expanded headline negative signals |
| NYT voluntary review (Jun 23) | Hypocrisy frame undetected ("positioned as responsible... Yet") | New hypocrisy_frame device |

### Remaining gaps for future iterations:
1. **Vulnerability contextualization** — "particularly vulnerable to misuse" and "cannot be recalled or controlled" in NYT voluntary review. These are negative contextual framing but don't match any existing device. Would need a new "vulnerability_positioning" device type.
2. **Corrected tone overshoot** — NYT voluntary review corrected to -0.57 vs manual -0.20. Correction formula heavily weights agency, overshooting on measured adversarial pieces.
3. **Cross-paragraph corporate_reassurance_undercut** — Guardian Wynn-Williams has the reassurance ("We do not require...") and the contradiction several paragraphs apart. Current corporate_reassurance_undercut requires ~200 char proximity. The new hypocrisy_frame partially addresses this with longer match windows (150-200 chars) but won't catch multi-paragraph gaps.

### Commit/Push: BLOCKED
- All 3 code files changed + 1 new test file created
- Git commit and GitHub push deferred to next iteration due to exec infrastructure failures
- **Unpushed changes:** framing.py (~40 lines added), sentiment.py (~15 lines added), test_hypocrisy_medical_duress.py (new, ~260 lines)
- Previous unpushed commits: `e9c1075` (Type D), `3ed1d26` (Type C)

---

## 2026-06-25 23:00 PT — Hour Type D: Toolkit Quality & Documentation

**Focus:** Comprehensive documentation updates — new methodology section, test/gallery sync, cross-doc consistency.

### What was improved:

#### 1. METHODOLOGY.md: New §13 Cross-Publication Same-Event Comparison

Added a complete new methodology section (§13) documenting the cross-publication same-event comparison technique that had emerged organically through multiple sample analyses but was never formally documented:

- **Wire-service baseline methodology:** Using Reuters/AP as the "control" — their near-zero framing device count establishes the factual baseline, and the gap between wire-service tone and magazine tone isolates the editorial framing contribution.
- **Comparison dimensions table:** 8 systematic dimensions for same-event comparison (word count, tone score, framing device count/types, source roster, stance balance, outsourced intensity, structural choices).
- **3 validated examples with data:**
  - MCI data exposure (Jun 22): Wired −0.60 vs Reuters −0.10 = −0.50 gap, 7 vs 1 framing devices
  - Meta glasses launch (Jun 23): Wired −0.15 vs Gizmodo +0.10 = −0.25 gap, 10 vs 0 framing devices
  - Arena prediction markets (Jun 23): Reuters +0.05 vs Engadget −0.70 = −0.75 gap
- **Analytical value:** Argues same-event comparisons are more persuasive than aggregate asymmetry scores because they control for event severity (the most important confound).
- **Publication-specific framing fingerprints:** Documents Wired's characteristic patterns (self-referential investigation, kicker framing, surveillance-consumer juxtaposition).
- **Limitations:** Selection bias in article pairs, genre differences, timing effects, byline variation.
- Renumbered former §13 (Causal Identification via Journalist Migration) → §14 with all 7 subsections updated.

#### 2. README.md: Test Table and Sample Output Gallery Updates

**Test count fix:** 446 → **464 tests** across **17 test files** (was 16).

Two missing test files added to table:
- `test_glasses_deep_dive.py` (17 tests): Kicker framing, product-name stop-filter, emotional_appeal false-positive exclusion, loaded language expansion
- `test_wynn_williams_fixes.py` (18 tests): Source extraction false positives (day names, book titles), litigation framing expansion, power_asymmetry per-violation fines

**8 missing sample output gallery entries added:**
- `atlantic_tool_crushes_creativity_2025_10_*`: Charlie Warzel's AI slop cultural critique
- `atlantic_ai_not_conscious_2026_06_*`: Ted Chiang ~4,200-word essay on AI consciousness (50 Anthropic mentions, entity detection gaps for Amanda Askell, AlphaFold, IBM/Deep Blue)
- `guardian_uk_tech_crackdown_us_intervention_2026_06_09_*`: Sovereignty framing discovery — led to new device types
- `guardian_meta_wynn_williams_lawsuit_2026_06_25_*`: Litigation framing expansion (0→10 detections), corporate_reassurance_undercut
- `gizmodo_vs_wired_glasses_launch_2026_06_23_*`: Same-event cross-pub comparison — 10 vs 0 framing devices on same Bosworth press event
- `reuters_meta_dalton_smith_departure_2026_06_17_*`: Wire-service baseline — natural experiment against Wired's coverage of same restructuring

#### 3. ARCHITECTURE.md: Test Count and File Layout

Updated stale test count from 429 → **464 tests** (17 files). Added `test_glasses_deep_dive.py` and `test_wynn_williams_fixes.py` to the file layout with descriptions.

### Commit:
- `e9c1075` — "docs: Type D — cross-pub comparison methodology, test/gallery updates"
- **Push pending** — exec session infrastructure was unstable during this run; commit saved locally, push will complete on next stable session.

### Unpushed commits:
- `e9c1075` (this iteration) + `3ed1d26` (Type C iteration from 22:00)

---

## 2026-06-25 22:00 PT — Hour Type C: Ownership & Funding Deep Dive

**Focus:** Wired/Condé Nast/Advance Publications — 6 major expansions: WBD-Paramount acquisition timeline, Meta Dec 2025 AI licensing exclusion (new severity-5 conflict), Perplexity as new revenue partner, events revenue commercial pivot data, updated portfolio valuations, and new portfolio_concentration conflict.

### What was improved:

#### 1. WBD-Paramount Skydance Acquisition (MAJOR portfolio realization event):

Complete timeline of the WBD bidding war:
- **Nov 13, 2025:** WBD Board initiates Strategic Review
- **Dec 4, 2025:** WBD signs merger agreement with Netflix ($23.25 cash + ~$4.50 Netflix stock = ~$27.75/share). WBD would separate Streaming & Studios from Global Networks (SpinCo); Netflix acquires Streaming & Studios side.
- **Dec 2025:** Paramount Skydance launches unsolicited all-cash tender offer at $30/share for 100% of WBD (including Global Networks). WBD Board unanimously recommends shareholders REJECT in favor of Netflix.
- **Feb 27, 2026:** Netflix declines to raise its bid and withdraws. WBD Board deems Paramount offer "superior."
- **Jun 2026 (early):** DOJ approves Paramount-WBD acquisition
- **Jun 24, 2026:** Paramount submits EU antitrust remedy — divesting Universal Pictures film distribution JV. EU Commission review extended to Jul 21.
- **Jun 25, 2026:** NY and CA AGs may sue to block merger. Larry Ellison/CNN overhaul controversy (WSJ).

**Impact on Advance:** If Paramount closes at $30/share, Advance realizes ~$2.94B from remaining ~98M shares + $1.1B already realized (Jun 2024 sale) = ~$4.04B total from WBD. Largest single liquidity event since Reddit IPO. Changes capital allocation landscape.

Sources: StockTitan/SEC filings, Sacnilk (Feb 27), NYPost (Jun 25), StockTwits/Reuters (Jun 24)

#### 2. Meta December 2025 AI Licensing Deals — Condé Nast EXCLUDED (NEW severity-5 conflict):

CRITICAL finding: On Dec 5, 2025, Meta entered the AI content licensing market by signing multi-year deals with 7 publishers to incorporate their content into Llama LLM and Meta AI chatbot:
- CNN, Fox News, Fox Sports, Le Monde Group, People Inc., The Daily Caller, The Washington Examiner, USA Today, USA Today Network

**Condé Nast was not among them.** This is not a passive absence — it's an active exclusion from a round that included Condé Nast's direct competitors. By Q1 2026, these deals were producing "meaningful" and "notable" revenue for publishers (per USA Today Co. and People Inc. Q1 2026 earnings, Digiday May 2026).

**Conflict analysis:** Condé Nast now receives AI licensing revenue from OpenAI, Amazon, Perplexity, and Apple (negotiating) — all Meta competitors — while receiving $0 from Meta despite Meta actively paying Condé Nast's publisher competitors. This creates a financial incentive to frame Meta negatively (no revenue stake in Meta's success) while framing Meta's competitors positively (revenue relationships with all of them).

**Added as new `meta_licensing_exclusion` known_conflict entry, severity 5.**

Sources: Reuters (Dec 5, 2025), Digiday (Dec 5, 2025 + May 2026 Q1 publisher report)

#### 3. Perplexity AI — NEW revenue relationship:

CEO Roger Lynch cited Perplexity alongside OpenAI as an AI licensing partner in Oct 2025 strategic pivot statement: "it plans to lean on events, subscriptions, commerce, and licensing deals with AI players including OpenAI and Perplexity" (Adweek, May 2026). Added as new entry in revenue_relationships. Perplexity is a 5th Meta competitor in Condé Nast's licensing portfolio.

Source: Adweek (May 2026)

#### 4. Events Revenue Commercial Pivot Data:

Major new financial data from Adweek (May 2026) CRO interview:
- Events revenue grew **40%** in 2025, projecting **+22%** in 2026
- Vanity Fair Oscars Party: **+65%** YoY revenue growth
- The New Yorker Festival: **+86%** YoY revenue growth
- Vogue World: **+48%** YoY revenue growth (heading to Milan for 5th edition)
- CEO Lynch (Oct 2025): advertising "no longer expected to be a growth engine"
- **$600M** in product sales in 2024 via editorial affiliate content
- **28 billion** video views in 2024
- CRO Herbst-Brady career arc: Yahoo → Snap → Viacom → Condé Nast (joined Aug 2024)
- Thread Podcast quote: "AI didn't kill premium media — it made it more valuable"

Added as `commercial_pivot` field in Condé Nast consolidated entry.

Sources: Adweek (May 2026), Thread Podcast (2026)

#### 5. Portfolio Valuation Updates (Jun 25, 2026):

| Holding | Price (Jun 25) | Value | Change vs Jun 23 |
|---|---|---|---|
| Reddit (RDDT) | $157.82 | ~$6.66B | Down from $7.0B (-4.9%) |
| Charter (CHTR) | $129.65 | ~$2.67B | Down from $2.7B (-1.6%) |
| WBD | $26.98 market / $30 tender | ~$2.65B / ~$2.94B | Up from $2.6B (+0.4%) |
| **Total public equity** | | **~$12.0B** | **Down from ~$12.3B** |

CHTR deterioration: -67.49% 1yr, -82.03% 5yr. Consensus "Reduce" (6 sell, 9 hold, 5 buy). Q1 2026 EPS missed by $0.84.

Reddit Q1 2026 data: EPS $1.01 (beat by $0.39), revenue $663.41M (+69.1% YoY). Targeting 1B users. Needham reaffirmed Buy with $300 target.

#### 6. Portfolio Concentration Conflict (NEW severity-5 entry):

Reddit now represents **~56%** of Advance's public equity ($6.66B of ~$12.0B), up from ~40% at time of IPO. As Charter collapses and WBD approaches exit via Paramount tender, Reddit's portfolio dominance intensifies. If Paramount closes and WBD cash is redeployed while Charter continues declining, Reddit could represent 65-70%+ of Advance's public portfolio.

**Analytical significance:** The Newhouse family's wealth is increasingly tied to a single asset that directly competes with Meta. This CONCENTRATION makes the conflict-of-interest between Reddit and Wired's Meta coverage more acute with each passing quarter. No Condé Nast property has ever disclosed this growing portfolio concentration.

### Commit: `3ed1d26` — 1 file changed, 149 insertions, 24 deletions
### Tests: 464/464 passing
### Pushed to GitHub

---

## 2026-06-25 21:00 PT — Hour Type B: Journalist/Publication Research

**Focus:** 4 new journalists added (83 total, up from 79), 1 new editorial change. All 4 have multi-publication careers critical for DiD (difference-in-differences) migration analysis. One is a rare journalist→government→journalist arc.

### New journalists added:

#### 1. Gilad Edelman — Washington Monthly → Wired → FTC → Atlantic
- **Career:** Columbia BA (2005-2009) → Yale JD (2012-2015) → Washington Monthly (editor/exec editor, Sep 2016 - Nov 2019) → Wired (politics writer, Nov 2019 - Sep 2022) → FTC (comms strategist under Lina Khan, Sep 2022 - Apr 2023) → Atlantic (senior editor, Apr 2023 - present)
- **Significance:** Rarest career arc in the dataset: journalist → government regulator → journalist. Yale JD gives legal/regulatory lens unique among tracked journalists. At Wired covered Section 230, content moderation, disinformation. FTC stint under Lina Khan gives insider regulatory perspective. Now covers economics/political economy with tech antitrust focus at Atlantic.
- **DiD value:** HIGH — crossed from Condé Nast (Wired) to Emerson Collective (Atlantic) with a government stint in between. Does his framing shift with institutional change?
- **Recent articles:** "Will Google Ever Have to Pay for Its Sins?" (Jan 2026), "Guilt by Association With Epstein" (Feb 2026), "The Rise of Libertarian Authoritarianism" (Jan 2026)
- **Sources:** BuzzSumo journalist profile, TheOrg, TalkingBizNews, JournalistHunt, Orchid/Priv8 Podcast
- **Source URLs:**
  - https://talkingbiznews.com/they-re-hiring/the-atlantic-hires-edelman-as-a-senior-editor-for-economics-coverage/
  - https://theorg.com/org/the-atlantic/people/gilad-edelman
  - https://buzzsumo.com/journalist/gilad-edelman-148776732/
  - https://journalisthunt.com/journalists/gilad-edelman

#### 2. Amanda Hoover — NJ Advance Media → Morning Brew → Wired → Business Insider
- **Career:** Northeastern BA journalism → Boston Globe (breaking news) → Christian Science Monitor (rapid response) → NJ Advance Media/Star-Ledger (state govt reporter, ~2019-2021) → Morning Brew (tech reporter, Nov 2021 - Oct 2022) → Wired (staff writer, Nov 2022 - Feb 2025) → Business Insider (senior correspondent, Mar 2025 - present)
- **Significance:** Promoted within Wired by Katie Drummond (Aug 2024). Covered Facebook Marketplace scams, TikTok Shop, AI workplace impact, Airbnb, layoff culture. Appeared on Wired Gadget Lab and Uncanny Valley podcasts.
- **DiD value:** HIGH — entered and exited Condé Nast ecosystem. Does her tech coverage tone differ now at BI vs Wired?
- **Sources:** TalkingBizNews (3 articles: Morning Brew hire, Wired hire, BI hire), Wired editorial promotions announcement, sxyngh.com Wired author page, Techmeme
- **Source URLs:**
  - https://talkingbiznews.com/they-re-hiring/wired-hires-morning-brews-hoover/
  - https://talkingbiznews.com/they-re-hiring/business-insider-hires-hoover-to-cover-tech/
  - https://talkingbiznews.com/they-re-hiring/morning-brew-hires-hoover-as-tech-reporter/

#### 3. Adam Satariano — Bloomberg → NYT (London)
- **Career:** UC Santa Cruz → Congressional Quarterly (Washington, ~2005-2007) → Bloomberg (11 years, ~2007-2018: SF→London transition 2016) → NYT (tech correspondent London, Mar 2018 - present)
- **Significance:** EU tech regulation beat — covers DMA, DSA enforcement against Meta, TikTok, Google. His coverage directly shapes perception of whether EU enforcement is justified oversight or anti-American protectionism. Recent: EU preliminary findings on TikTok "addictive design" (Jun 2026). Longtime Bloomberg-to-NYT migration (11 years → NYT).
- **DiD value:** MEDIUM — single clean migration (Bloomberg → NYT), less institutional contrast than Edelman but critical for EU regulatory framing analysis.
- **Sources:** TalkingBizNews NYT hire announcement, Techmeme (TikTok DSA coverage), nytco.com
- **Source URLs:**
  - https://talkingbiznews.com/they-re-hiring/ny-times-hires-bloombergs-satariano-to-cover-tech-in-europe/
  - https://techmeme.com/search (TikTok DSA coverage)

#### 4. Sapna Maheshwari — Bloomberg → BuzzFeed → NYT
- **Career:** UNC-Chapel Hill (business journalism) → Bloomberg News (reporter, ~2011-2013) → BuzzFeed (reporter, 2013-2016) → NYT (Aug 2016 - present: advertising → retail → TikTok/emerging media)
- **Significance:** Award-winning investigative reporter (SABEW Best in Business, Front Page Award). 3.6M views on BuzzFeed's most-read investigative feature ever. Now NYT's TikTok/emerging media reporter — direct Meta competitor coverage. Her retail/advertising background gives deep platform business model understanding.
- **DiD value:** MEDIUM-HIGH — covers TikTok (Meta competitor) at NYT. Natural experiment: does she apply same critical scrutiny to TikTok as NYT applies to Meta?
- **Sources:** Wikipedia, nytco.com press release, TalkingBizNews (3 articles: BuzzFeed→NYT hire, retail beat move, TikTok beat move), me.sh profile
- **Source URLs:**
  - https://en.wikipedia.org/wiki/Sapna_Maheshwari
  - https://nytco.com/press/a-new-role-for-sapna-maheshwari/
  - https://talkingbiznews.com/they-re-hiring/buzzfeeds-maheshwari-to-join-ny-times-biz-desk/

### Editorial changes added:

1. **Atlantic: Gilad Edelman hired as senior editor, economics** (Apr 2023) — first journalist in dataset with government regulator (FTC) experience. Adds legal/regulatory authority to Atlantic's tech coverage.

### Updated statistics:
- **Journalists:** 79 → 83
- **Multi-publication:** 77 → 80 (80/83 = 96.4%)
- **Tests:** 464 passing (unchanged)

### Analytical notes:

**Key insight — NYT TikTok coverage gap:** Sapna Maheshwari is NYT's dedicated TikTok reporter. Adding her enables a critical comparison: how does NYT frame TikTok (a Meta competitor whose product directly competes with Instagram Reels) versus how NYT frames Meta? If NYT applies consistently critical scrutiny to both platforms, that's evidence of principled reporting. If TikTok gets softer treatment despite similar children's safety concerns, that reveals platform-level bias in the newsroom.

**Key insight — Edelman's unique career arc:** No other journalist in the dataset has moved from journalism → government regulation → journalism. His FTC tenure under Lina Khan (who brought the most aggressive Big Tech enforcement cases in decades) means he has insider knowledge of how regulators actually build cases. This makes his Atlantic coverage of Google antitrust and tech policy uniquely authoritative — and uniquely testable for institutional bias, since he wrote about the same topics from inside Condé Nast just 2 years earlier.

## 2026-06-25 16:00 PT — Hour Type A: Article Deep Dive

**Article:** "Whistleblower Sarah Wynn-Williams sues Meta over attempts to 'silence' her"
**Publication:** The Guardian
**Date:** June 25, 2026
**Sequel to:** Guardian Hay Festival coverage (June 1, 2026)

### Article summary:
Wynn-Williams filed a 57-page complaint in US District Court (N.D. Cal.) challenging the arbitration gag order Meta obtained in March 2025 after publication of her memoir "Careless People." Claims: arbitration agreement signed under duress ($300K expense reimbursement and healthcare as leverage), "coercive surveillance" (Meta rep traveled to Hay Festival to build sanctions case), First Amendment violation. Seeking: void severance agreement, lift arbitration order, compensatory damages. Meta had sought $50K per violation including each book sale.

### Manual vs toolkit comparison — 6 bugs found and fixed:

#### Source extraction (2 bugs):
1. **"Thursday" extracted as source** — "on Thursday argues" matched `[A-Z][a-z]+ (verb)` pattern. Fixed: added all day names (Mon-Sun) and month names (Jan-Dec) to `_NAME_STOP_FIRST_WORDS`.
2. **"Careless People" extracted as source** — book title + "alleges" verb. Fixed: added book/media title false positives to `_NAME_STOP_NAMES`.

#### Framing detection (2 bugs):
3. **litigation_framing: 0 detections on an article ABOUT a lawsuit** — pattern only knew "lawsuit", "legal action", "court challenge", "injunction", "class action". "Complaint", "suit", "arbitration" were all missing. Fixed: added complaint/suit/counter-suit/arbitration/petition to filing vocabulary. Added "is suing/sued/sues [entity]" pattern. Added "arbitration/severance + ruling/order/agreement/clause/hearing" pattern. Result: 0 → 10 detections.
4. **power_asymmetry missed "$50K per violation"** — pattern required `each\s+(?:violation|breach)` but article said "each purported violation". Fixed: changed to `each\s+(?:\w+\s+)?(?:violation|breach|instance)` to allow one adjective. Result: 0 → 1 detection.

#### Entity detection (2 bugs):
5. **Joel Kaplan and Sheryl Sandberg not in Meta cluster** — both are senior Meta executives central to whistleblower coverage. Fixed: added to aliases + regex, along with Nick Clegg and Dina Powell McCormick.
6. **SEC and DOJ not in any cluster** — Wynn-Williams filed with both but neither was tracked. Fixed: added to US Government cluster.

### Tests: 464 passing (446 → 464, +18 new in `test_wynn_williams_fixes.py`)
### Commit: `5c5c21f` — 6 files changed, 339 insertions, 6 deletions
### Pushed to GitHub

---

## 2026-06-25 14:00 PT — Hour Type D: Toolkit Quality & Documentation

**Focus:** Comprehensive documentation sync across 4 files (ARCHITECTURE.md, README.md, METHODOLOGY.md, EDITORIAL_HISTORIES.md) — all had stale numbers from weeks of rapid iteration. ARCHITECTURE.md was the most outdated, still showing numbers from ~15 iterations ago.

### What was improved:

#### 1. ARCHITECTURE.md — most stale, 7 corrections:

| Item | Before | After | Verification |
|---|---|---|---|
| Framing device count | 22 | 28 | `len(_DEVICE_PATTERNS) + 3 = 25 + 3 = 28` |
| Core device tier | 12 | 10 | Audit against METHODOLOGY.md taxonomy |
| Extended device tier | 7 | 15 | Audit against METHODOLOGY.md taxonomy |
| Topic bucket count | 10 | 12 | `len(TOPIC_KEYWORDS) = 12` |
| Test count | 236 | 429 | `pytest --tb=no -q` |
| Test file count | 8 | 15 | `ls tests/test_*.py \| wc -l` |
| Test file list | 8 entries (unsorted) | 15 entries (alphabetically sorted with descriptions) | Per-file pytest counts |

**Tier reclassification rationale:** straw_man, refusal_amplification, juxtaposition, timeline_implication were listed as Core but are extended devices by definition (added from real-article analysis, not fundamental pattern types). ceo_personalization and litigation_framing are Core (fundamental editorial techniques).

**Missing test files added:** test_atlantic_analysis.py (31), test_citations.py (39), test_claims.py (28), test_loaded_language_uproar.py (13), test_quality_standards.py (35), test_scale_magnitude.py (16), test_topics.py (28)

#### 2. README.md — test table modernization:

- Test count: 398 → 429
- Test file count: 14 → 15
- Added per-file test counts to table column (previously not shown)
- Added 3 new test file rows: test_atlantic_analysis.py, test_loaded_language_uproar.py, test_scale_magnitude.py
- Topic reference: 11 → 12

#### 3. METHODOLOGY.md — topic classification expansion:

- Topic bucket count: 10 → 12
- Added `ai_generated_content` with verified keywords from implementation: slop, AI slop, synthetic content, AI-generated, deepfake, AI art, model collapse, engagement bait, hallucination
- Added `workplace_culture` with verified keywords from implementation: morale, burnout, attrition, retention, toxic culture, internal revolt, soul-crushing, return to office, disgruntled
- Added analytical note explaining topic design: `ai_generated_content` vs `ai_development` (output vs creation), `workplace_culture` vs `layoffs` (culture vs formal actions) vs `executive_behavior` (culture vs leadership)

#### 4. EDITORIAL_HISTORIES.md — journalist count sync:

- Journalist count: 51 → 70 (verified via `grep "^  - name:" journalists.yaml | wc -l`)
- Multi-publication count: 48 → 66 (verified via Python analysis of career events: 66 of 70 journalists have career events at ≥2 distinct publications)

### Cross-verification method:

Every updated number was verified against the actual implementation:
- Framing devices: `python3 -c "from mediascope.analyze.framing import _DEVICE_PATTERNS; print(len(_DEVICE_PATTERNS))"`
- Topics: `python3 -c "from mediascope.analyze.topics import TOPIC_KEYWORDS; print(len(TOPIC_KEYWORDS))"`
- Tests: `python3 -m pytest tests/ --tb=no -q` → 429 passed
- Journalists: `grep "^  - name:" profiles/careers/journalists.yaml | wc -l` → 70
- Multi-pub: Python script checking `len(set(pubs)) >= 2` per journalist → 66

### Commit: `1367171` — 4 files changed, 40 insertions, 26 deletions
### Tests: 429/429 passing

---

## 2026-06-25 13:00 PT — Hour Type C: Ownership & Funding Deep Dive

**Focus:** MIT Technology Review — OBBBA endowment tax (now signed law, not proposed), federally-subsidized royalty income provision, MIT endowment portfolio VC/PE exposure, new Honeywell corporate partnership. Six major profile expansions.

### What was improved:

1. **OBBBA endowment tax — corrected from "proposed" to ENACTED LAW (signed July 4, 2025):**
   - The profile previously said "Big Beautiful Bill Act proposes endowment tax increase" — this is now LAW
   - Tiered structure: 1.4% ($500K-$750K/student), 4% ($750K-$2M), 8% (>$2M/student)
   - MIT classification: $27.4B endowment / 11,816 students = ~$2,318,340/student → **8% tier** (highest)
   - ~5.7x increase from prior 1.4% flat rate
   - Effective for taxable years beginning after Dec 31, 2025 (MIT's FY starts July 1, 2026)
   - Student threshold raised from 500 to 3,000 (MIT at 11,816, well above)
   - MIT is one of 15 institutions subject to new rates (5 at 8% or 4%, 5 at 1.4%)
   - Congressional estimate: $761M total additional revenue over 10 years across all affected schools
   - In 2023, all 56 previously affected schools paid $381M combined at the old 1.4% rate
   - Sources: Faegre Drinker (Jul 2025), Foley & Lardner, Wikipedia, Broadridge/Peterson, Tax Policy Center

2. **"Federally-Subsidized Royalty Income" provision — NEW SECTION:**
   - The OBBBA includes royalties from any patent/copyright/IP in the endowment tax base IF:
     (a) IP resulted from student/faculty work at the institution, AND
     (b) any federal funds were used in research/development/creation
   - This DIRECTLY taxes the output of MIT's massive federally funded research enterprise
   - MIT's $762M total research expenditures generate patents developed with NSF, DOD, NIH, DARPA funding
   - Creates a novel FEEDBACK LOOP: same corporate partnerships (Google, IBM, Amazon) that create editorial conflicts for MIT TR also generate taxable royalty income for MIT
   - Sources: Faegre Drinker detailed analysis, OBBBA text (amended IRC §4968)

3. **"Related organizations" provision:**
   - OBBBA includes assets and NII of entities controlled by the institution in the endowment tax calculation
   - Technology Review Inc. ($6.5M total assets) is a MIT-controlled nonprofit
   - Its assets are likely counted toward MIT's endowment-per-student calculation
   - Source: Faegre Drinker analysis

4. **Executive compensation excise tax expansion (IRC §4960):**
   - OBBBA broadens "covered employee" definition: now ANY employee/former employee paid >$1M in any year (previously only top 5)
   - MIT administrators on MIT TR board already near/above threshold: David Schmittlein ($1.05M, MIT Sloan Dean), Cynthia Barnhart ($987K, MIT Provost)
   - Could affect future board composition and compensation structures
   - Source: Foley & Lardner

5. **MIT endowment portfolio composition — NEW DATA:**
   - 30-40% allocation to private investments (PE + VC) per MPI/Institutional Investor analysis
   - MIT has one of the HIGHEST VC exposures among elite endowments (alongside Brown, Dartmouth, Princeton)
   - High VC exposure = direct financial interest in tech startups covered by MIT TR
   - Glen Shor (MIT EVP/Treasurer, $883K, MIT TR board Director) manages these investments
   - MPI analysis: "MIT is very well diversified" but VC retrenchment drove negative returns in FY2023
   - Sources: Institutional Investor, PitchBook

6. **MIT-Honeywell partnership (June 24, 2026) — NEW ENTRY:**
   - MIT Center for Sustainability Science and Strategy collaboration with Honeywell
   - Joint report "Accelerating Energy Expansion" published June 24, 2026
   - Models AI-enabled cost reductions: $225B in oil-based fuels, $80B in LNG by 2050
   - Added as 9th corporate partnership and 9th revenue relationship
   - Extends MIT corporate ties beyond pure tech into industrial technology
   - Source: PR Newswire (Jun 24, 2026)

### New known_conflict entry:
- **obbba_royalty_tax_feedback_loop** (severity 3): The OBBBA's royalty income provision creates a feedback loop — the same corporate partnerships that create editorial conflicts also generate taxable royalty income, and the ~5.7x tax increase may make MIT MORE dependent on corporate research funding and event sponsorship, potentially DEEPENING existing conflicts

### MIT enrollment data added (2025-2026):
- 11,816 total students (4,561 UG + 7,255 grad)
- 3,475 international (529 UG + 2,946 grad)
- 8,341 domestic (70.6%)
- Source: MIT Registrar (registrar.mit.edu)

### Key analytical insight:
The OBBBA endowment tax creates a structural INTENSIFICATION of MIT TR's existing editorial conflicts. The ~5.7x tax increase pressures MIT's institutional budget, which may increase dependence on (a) corporate research funding, (b) event sponsorship revenue (flows through MIT TR), and (c) endowment returns (30-40% VC/PE, including investments in companies MIT TR covers). The "Federally-Subsidized Royalty Income" provision is the first federal tax mechanism that directly links university-corporate research partnerships to tax liability — making the editorial conflict and the financial conflict the SAME thing.

### Anti-avoidance provisions:
Treasury directed to promulgate regulations to "prevent avoidance of such tax through the restructuring of endowment funds or other arrangements" — meaning MIT cannot restructure to escape the 8% tier.

### Commit: `bee1b08` — 1 file changed, 119 insertions, 4 deletions
### Tests: 429/429 passing

---

## 2026-06-25 12:00 PT — Hour Type B: Journalist/Publication Research (Guardian US)

**Focus:** Guardian US desk expansion — new journalist Jeremy Barr (WaPo → Guardian), Betsy Reed EIC entry, editorial_changes.yaml updates. 70 journalists now tracked.

### New Journalist: Jeremy Barr (70th tracked)

**Career timeline (7 positions, 4 publications before Guardian):**

| Period | Publication | Role | Beat |
|---|---|---|---|
| 2012-01 → 2013-06 | Pew Research Center | Researcher | Research |
| 2013-07 → 2014-06 | Poynter.org | Contributor (freelance) | Media criticism, journalism |
| 2014-07 → 2015-10 | Politico Media | Associate editor | Media |
| 2015-11 → 2017-05 | AdAge | Digital media reporter | Advertising trends |
| 2017-06 → 2020-06 | Hollywood Reporter | Senior media & politics writer | Media, politics, Trump admin |
| 2020-06 → 2025-09 | Washington Post | Media reporter | Media industry, regulation, lawsuits |
| 2025-10 → present | Guardian US | Media & power reporter | Media, politics, corporate influence |

**Education:** Emory University BA (political science + sociology), University of Maryland MA (journalism). Native of Rockville, MD. Participated in WaPo's young journalist development program as a teenager. Taught English in Hungary pre-journalism.

**Why this journalist matters for MediaScope:**
- His beat at Guardian US DIRECTLY overlaps with MediaScope's mission — he covers media ownership, regulation, lawsuits, and how powerful institutions shape information flows
- Covered Smartmatic v. Fox News at WaPo — exactly the type of media-ownership-shapes-coverage story we analyze
- First-ever US media reporter at Guardian — structural expansion beyond tech into media criticism
- Reports to Dominic Rushe (US business editor); coordinates with UK media editor Michael Savage
- Central analytical question: does he cover the Guardian's own OpenAI/Google licensing deals with the same scrutiny he'd apply to rival publications?
- POLITICO connection: contemporaneous with Johana Bhuiyan at Politico NY (2013-2015) — two journalists who overlapped at the same publication now both at Guardian US

**Sources:**
- Editor & Publisher hiring announcement (Oct 2025)
- Talking Biz News (WaPo hire 2020, THR hire 2017, AdAge move 2015)
- Poynter (career beat, contributor archive 2013-2014)
- AdAge author bio page
- Muck Rack verified profile

### New Editorial Changes Entry: Betsy Reed as Guardian US EIC

**Career arc:** The Nation (exec editor 2006-2014) → The Intercept (EIC 2015-2022) → Guardian US (EIC Sep 2022-)

**Key facts:**
- Succeeded John Mulholland as Guardian US editor-in-chief
- Under her leadership: 50+ journalists added, 60% growth in supporting readers
- New coverage areas: investigations, US soccer, wellness
- Launched "The Whole Picture" US marketing campaign (fall 2025) — positioning Guardian independence against US press decline
- Harvard BA 1990 (history and literature). Edited Scahill's 'Blackwater' and 'Dirty Wars'
- CUNY Newmark J-School 2025 commencement speaker
- Most adversarial institutional origin of any EIC in dataset (The Intercept was built on Snowden disclosures)

**Sources:** Wikipedia, CUNY J-School announcement (Oct 2025), CJR interview (Nov 2025), LittleSis, Agorapp

### Other Discoveries

1. **Kari Paul departure date confirmed:** Left Guardian August 2024 for Paris College of Art MFA (Transdisciplinary New Media, 2024-2026). RocketReach profile confirms. Entry already correctly shows end date 2024-06.

2. **Johana Bhuiyan entry verified:** All dates confirmed accurate. Senior Tech Reporter and Editor since Aug 2021. Education: Lehigh University BA Journalism. Continues to publish actively (Apple/ICE tracking apps story, border patrol DNA collection, 2025-2026).

### Commit: `c9fb5ba` — 3 files changed, 77 insertions, 1 deletion
### Tests: 429/429 passing

---

## 2026-06-25 10:00 PT — Hour Type A: Article Deep Dive (Atlantic)

**Focus:** "A Tool That Crushes Creativity" by Charlie Warzel (The Atlantic, Oct 2025) — opinion essay on AI slop as cultural phenomenon. Full 5-module analysis with manual comparison, gap identification, and systematic fixes.

### Key Metrics Improvement

| Dimension | Before | After |
|---|---|---|
| Entity clusters | 8 | 11 (+3: VC/Tech Investors, Spotify, Policy Research) |
| Entity mentions | 30 | 38 (+8) |
| Source detection | 2 | 7 (+5 named sources) |
| Framing devices | 23 | 27 (+4) |
| Emotional intensity | 0.22 | 0.95 (correctly high for adversarial essay) |
| Primary topic | ai_development (0.21) | ai_generated_content (0.79) — NEW bucket |
| Tests | 398 | 429 (+31) |

### Fixes Applied (16 total)

**entities.py:**
- Added J.D. Vance to Political Figures (regex handles "J. D.", "J.D.", "JD")
- Created VC/Tech Investors cluster (Marc Andreessen, a16z, Sequoia, Benchmark, etc.)
- Created Spotify cluster (Spotify, Daniel Ek)
- Added Graphite + Pew Research Center to Policy Research cluster

**sources.py:**
- Added 12 neutral attribution verbs: mused/muses, quipped/quips, reflected/reflects, pondered/ponders, dubbed/dubs, coined/coins, pleaded/pleads, implored/implores, beseeched
- New Pattern 3b: "[Name] has/have/had [verb]" for auxiliary + main verb (caught "Angelos Arnis has dubbed")
- Pattern 5: Added optional adverb (`\w+ly`) before verb in appositives (caught "convincingly argued")

**framing.py:**
- Straight-quote ironic quotation patterns (article uses `"` not `""`/"`)
- "nightmarish" added to catastrophizing patterns
- "cultural dead end", "model collapse", "ecological harm" added to catastrophizing
- CEO personalization broadened: `[CEO]'s [plan/vision/strategy/obsession/agenda/initiative/push]`

**sentiment.py:**
- Added 18 AI-criticism/cultural-criticism emotional terms (narcotic, stupefying, soulless, nihilism, meaninglessness, disorientation, recursive, corrosive, sinister, pervasive, polluted, degrade, slop, unsatisfying, contextless, never-ending, frictionlessness)

**topics.py:**
- NEW topic bucket `ai_generated_content` (28 keywords: slop, synthetic content, AI-generated, model collapse, ultra-processed, engagement bait, etc.)

### Known Limitations Documented

1. **Ironic quotation at paragraph distance:** 200-char window misses essay-style editorial undercuts that operate across paragraph boundaries. Needs coreference-aware paragraph-level detector.
2. **Stance misclassification in opinion essays:** Source quoted "supportively" by text content can be deployed ironically by editorial context. Needs ironic deployment detection.
3. **X (single-letter platform):** Not detected as entity; regex can't disambiguate "X" the platform from "X" the letter without context.
4. **Scale/magnitude for content production:** "5,000 shows" not in current scale patterns (focused on fines/losses).

### Outputs
- `examples/sample_output/atlantic_tool_crushes_creativity_2025_10_analysis.md` — Full analysis
- `tests/test_atlantic_analysis.py` — 31 regression tests

---

## 2026-06-25 09:00 PT — Hour Type D: Toolkit Quality & Documentation

**Focus:** Test coverage expansion — 4 previously-untested core modules now have comprehensive regression tests. Test count: 268 → 398 (+130 tests, 48.5% increase).

### What was improved:

#### 1. `test_quality_standards.py` (35 tests) — NEW
Tests for `mediascope/quality/standards.py`, the quality enforcement layer that checks MediaScope's own output for AI slop, structural quality, and analytical rigor.

- **Banned phrase detection (9 tests):** Case-insensitive matching for lowercase phrases (`delve`, `tapestry`, `landscape`), case-sensitive for capitalized phrases (`Moreover,`, `Furthermore,`). Multiple phrase detection, deduction scoring (-5 per occurrence), error severity classification, line number reporting.
- **Em dash enforcement (4 tests):** Under-limit no-issue, over-limit warning, -3 per excess scoring, count tracking.
- **Counterargument detection (6 tests):** Detects `however`, `critics argue`, `on the other hand`, `opposing view`. Missing counterargument costs -10 points.
- **Limitations detection (4 tests):** Detects `limitation`, `caveat`, `this analysis does not`. Missing costs -8 points.
- **Methodology detection (4 tests):** Detects `methodology`, `we analyzed`, `statistical`. Missing costs -5 points (info severity, not warning).
- **Scoring & pass/fail (6 tests):** Perfect text → 100, empty text → 77 (missing all three signals), pass threshold at 60 + no errors, single banned phrase (error) causes fail regardless of score, score clamped to 0-100, multiple violations compound.
- **Report structure (2 tests):** All `QualityReport` fields populated with correct types, all `QualityIssue` entries have required fields.

#### 2. `test_citations.py` (35 tests) — NEW
Tests for `mediascope/quality/citations.py`, the citation extraction and source grading layer.

- **Source grading (19 tests):** 7 primary domains tested (sec.gov, ftc.gov, arxiv.org, pubmed, courtlistener, doi.org + subdomain inheritance), 6 secondary domains (reuters, nytimes, wsj, bbc, guardian, bloomberg), 4 tertiary domains (wordpress, substack, twitter, medium), plus Wikipedia as tertiary.
- **Domain extraction (5 tests):** `www.` stripping, subdomain preservation, no-scheme handling, empty string, complex URLs with query params.
- **Citation extraction (11 tests):** URL extraction with trailing punctuation stripping, grade assignment from URLs, "according to" attribution patterns, "as reported by" patterns, formal bracketed citations `[1]`, parenthetical citations `(Author 2024)`, URL deduplication, empty text, no-citation text, combined multi-type extraction, trailing punctuation stripping.
- **Citation report (5 tests):** Empty list, type counts, primary ratio, domain breakdown, verified count.

#### 3. `test_topics.py` (28 tests) — NEW
Tests for `mediascope/analyze/topics.py`, the topic classification engine that assigns articles to standardized topic buckets for confound control (METHODOLOGY.md §3).

- **Topic bucket detection (13 tests):** Every standardized bucket tested with representative text: layoffs (2 patterns), ai_development (2), privacy_data, antitrust_regulation, child_safety, content_moderation, financial_results, product_launch, executive_behavior, litigation, workplace_culture.
- **Confidence scoring (3 tests):** More keywords → higher confidence, confidence in [0, 1], matched_keywords populated.
- **Top-N filtering (4 tests):** Default top-3, custom top-N, top-1, descending sort verified.
- **Custom topics (2 tests):** Custom topic detected, custom + standard coexist in results.
- **Edge cases (4 tests):** Empty text → [], no matches → [], short text still works, all 11 keyword sets exist and are non-empty.
- **Multi-topic articles (2 tests):** layoffs + financial_results co-detected, privacy_data + litigation co-detected.

#### 4. `test_claims.py` (32 tests) — NEW
Tests for `mediascope/quality/claims.py`, the claim extraction and evidence mapping engine.

- **Statistic detection (4 tests):** Percentages (33%), dollar amounts ($4.03 billion, $5 million), multipliers (3x).
- **Quote detection (2 tests):** Straight quotes, curly quotes (U+201C/U+201D).
- **Citation signals (3 tests):** `according to`, `as reported by`, `study by`.
- **Assertion detection (3 tests):** Superlatives ("most adversarial"), proves/demonstrates, "has never".
- **Source attribution (3 tests):** URLs as sources, "according to" as sources, bare assertions correctly unsourced.
- **Claim mapping (4 tests):** sourced/unsourced partition, by_type grouping, sourced_ratio in [0, 1], empty list → zeroes.
- **Unsupported claims ratio (4 tests):** All sourced → 0.0, all unsourced → 1.0, mixed → 0.5, empty → 0.0.
- **Confidence scoring (2 tests):** Statistics get higher confidence (≥0.5), all scores in [0, 1].
- **Edge cases (3 tests):** Empty text → [], short sentences skipped, narrative text → no claims.

### Coverage gap analysis:

Before this iteration, 8 of 17 Python modules in `mediascope/` had test files. After:

| Module | Lines | Tests Before | Tests After |
|--------|-------|-------------|-------------|
| `analyze/entities.py` | — | ✅ | ✅ |
| `analyze/framing.py` | — | ✅ (in sentiment) | ✅ |
| `analyze/sentiment.py` | — | ✅ | ✅ |
| `analyze/sources.py` | — | ✅ (source_stance) | ✅ |
| `analyze/topics.py` | 221 | ❌ | ✅ 28 tests |
| `quality/standards.py` | 207 | ❌ | ✅ 35 tests |
| `quality/citations.py` | 252 | ❌ | ✅ 35 tests |
| `quality/claims.py` | 267 | ❌ | ✅ 32 tests |
| `score/asymmetry.py` | — | ✅ | ✅ |
| `careers/*` | — | ✅ | ✅ |
| `conflicts/*` | 876 | ❌ | ❌ (next D target) |
| `ingest/*` | — | ❌ | ❌ |
| `report/*` | — | ❌ | ❌ |

Still untested: `conflicts/` (ownership, disclosure, litigation, revenue — 876 lines), `ingest/`, `report/`, `storage/`. The `conflicts/` module is the next priority for a Type D iteration.

### Test results:
- **398/398 passing** (268 existing + 130 new, all green)

### README updates:
- Test count: 268 → 398
- Test table expanded with 4 new entries
- Test run examples expanded with quality and topic-specific commands

### Files:
- `tests/test_quality_standards.py` — NEW (35 tests)
- `tests/test_citations.py` — NEW (35 tests)
- `tests/test_topics.py` — NEW (28 tests)
- `tests/test_claims.py` — NEW (32 tests)
- `README.md` — test count and table updated

---

## 2026-06-25 09:00 PT — Hour Type C: Ownership & Funding Deep Dive

**Focus:** The Atlantic — first dedicated Type C iteration for this publication. Six major expansions: new EC investments (X-Energy, Xcimer, LoveFrom chain), civic governance entanglements (Partnership for San Francisco), litigation landscape (strategic non-litigation + union bargaining), new revenue relationships (NewsGuard AI, CivicScience, Atlantic Labs), and cross-publication OpenAI licensing map.

### What was improved:

1. **New Emerson Collective investments (3 additions + 1 chain deepening):**
   - **X-Energy** — $700M Series C (Feb 2025). EC co-invested with AMAZON. Nuclear SMR startup. Creates financial alignment with Meta's cloud/advertising/device competitor. Source: TechCrunch.
   - **Xcimer** — $100M round. Fusion laser energy. Other investors: Hedosophia, Breakthrough Energy Ventures, Lowercarbon Capital. Source: TechCrunch.
   - **California Forever** — LPJ investor in planned city, 66,000 acres in Solano County. Source: Wikipedia (cited).
   - **LoveFrom/io Products chain deepened:** EC didn't just invest in io Products — LPJ backed Jony Ive's LoveFrom BEFORE it birthed io Products. Ive: "If it wasn't for Laurene, there wouldn't be LoveFrom." LPJ hosted Ive/Altman prototype reveal at EC Demo Day. Full chain: EC backed LoveFrom (2019) → LoveFrom birthed io Products → OpenAI acquired io Products ($6.5B, 2025). LPJ is an ENABLER, not merely an investor. Sources: 9to5Mac (2 articles).
   - **MSE divestiture documented:** LPJ divested 20% stake in Monumental Sports (Dec 2025).

2. **Civic governance entanglements (new section):**
   - **Partnership for San Francisco** (March 2025): 26-member civic coalition led by Katherine August-deWilde.
   - Co-chairs: LPJ + Ruth Porat (Alphabet/Google President & CIO)
   - Members include: Sam Altman (OpenAI CEO), Jony Ive (LoveFrom)
   - Quarterly meetings creating DIRECT PERSONAL GOVERNANCE LINKS between Atlantic's owner and:
     (a) Meta's #1 advertising competitor (Google/Alphabet)
     (b) Atlantic's content licensing partner + investment exit company (OpenAI)
     (c) The designer whose company Atlantic's owner funded → became OpenAI's $6.5B acquisition
   - No other publication owner in the dataset has this density of civic governance links
   - Sources: FA Magazine, Bloomberg, Mace Magazine

3. **Litigation connections (0 → 2 entries):**
   - **Strategic non-litigation:** Atlantic has ZERO lawsuits against AI companies. Chose licensing (May 2024) over litigation — 5 months after NYT sued (Dec 2023). Conspicuously absent from 400-newspaper OpenAI/Microsoft suit (June 2026, SDNY). Alex Reisner's Books3 investigation exposed Meta/LLaMA training data but Atlantic didn't sue. Revenue alignment with AI companies rather than fellow publishers.
   - **Union bargaining dispute:** Atlantic Union (NewsGuild of NY) demanded OpenAI deal transparency. ~60 journalists signed letter. Thompson/OpenAI refused full disclosure. Bargaining for AI contract protections ongoing.
   - Sources: Bloomberg Law, The Wrap, NYGuild, TechCrunch

4. **New revenue relationships (3 entries):**
   - **NewsGuard AI** (June 2026): Launch co-marketing partner. Revenue-share model. CRITICAL TENSION — NewsGuard positions itself AGAINST LLMs that "shoplift journalism" while Atlantic licenses content TO one of those LLMs. Thompson promotes both without acknowledging contradiction.
   - **CivicScience** (Sep 2025): Advertising partnership for real-time consumer insights and targeting. Shows Atlantic building ad-tech capabilities alongside subscription revenue.
   - **Atlantic Labs**: Expanded from mention to full revenue_relationship entry. Atlantic's product team has "privileged access" to OpenAI tech — deeper than standard licensing. Co-developing news features in ChatGPT.
   - Sources: CNN, NewsGuard, Editor & Publisher, Morningstar/PR Newswire, OpenAI blog, Maginative

5. **Known conflicts expanded (8 → 11):**
   - NEW: Civic governance (severity 3) — Partnership for SF links to Porat/Altman/Ive
   - NEW: Co-investment alignment (severity 2) — EC + Amazon co-investing in X-Energy
   - NEW: AI partnership tension (severity 1) — simultaneous OpenAI deal + anti-LLM NewsGuard partnership

6. **Cross-publication OpenAI licensing map (new analytical section):**
   - 4 of 5 tracked publications have financial relationships with OpenAI
   - Atlantic: Licensing + product + equity exit (deepest)
   - Condé Nast/Wired: Licensing (Aug 2024)
   - Guardian: Licensing (Feb 2025)
   - NYT: Lawsuit (only litigant)
   - MIT TR: No documented relationship
   - 3 of 5 chose revenue over enforcement

### Key analytical discoveries:

1. **LPJ's civic governance links create an unprecedented concentration of AI industry power around a media owner.** She co-chairs a quarterly-meeting civic organization with Google's president, sits at the same table as OpenAI's CEO, and already has the deepest financial relationship with OpenAI of any publication in the dataset. No disclosure of these relationships has been observed in Atlantic coverage.

2. **The Atlantic's "dual AI monetization" strategy is unique in the dataset.** No other tracked publication simultaneously licenses content to OpenAI AND co-markets a product positioned against ChatGPT's approach. Thompson's messaging is strategically contradictory — promoting both revenue streams without acknowledging the tension. This suggests sophisticated hedging: maximizing revenue regardless of which side of the AI-vs-journalism debate prevails.

3. **EC's X-Energy co-investment with Amazon adds a FIFTH Meta competitor to the financial alignment list.** The Atlantic's owner now has financial connections to: Apple ($16B+ stock), OpenAI (licensing + equity exit), Mistral AI (open-source LLM competitor), Google/Alphabet (civic governance), and Amazon (X-Energy co-investment). Five of the six largest Meta competitors have financial links to Atlantic's owner.

4. **The LoveFrom chain deepens the io Products conflict beyond equity.** LPJ is not merely an investor — she backed the design firm in 2019, personally facilitated the Ive-Altman relationship, and hosted their product reveal at EC's own Demo Day. The chain (EC funds LoveFrom → LoveFrom creates io Products → OpenAI acquires io Products) shows LPJ's involvement at every stage of what became OpenAI's $6.5B acquisition.

5. **Strategic non-litigation reveals incentive alignment.** Atlantic chose revenue over enforcement at the exact moment its peers were filing suits. The 400-newspaper OpenAI/Microsoft suit (June 2026) makes Atlantic's absence more conspicuous. This is consistent with the compound OpenAI relationship — Atlantic benefits when OpenAI succeeds.

### New analytical questions added:
6. Google/Alphabet coverage bias (via Porat civic link)?
7. Amazon coverage bias (via X-Energy co-investment)?
8. NewsGuard vs OpenAI messaging consistency?
9. Cross-publication OpenAI licensing effect on coverage?

### Stats:
- Atlantic profile: 511 → 761 lines (+250 lines, 49% expansion)
- Known conflicts: 8 → 11 (+3)
- Litigation connections: 0 → 2
- Revenue relationships: 2 → 5 (+3: NewsGuard AI, CivicScience, Atlantic Labs)
- Investment entities: 13 → 17 (+4: X-Energy, Xcimer, LoveFrom expanded, California Forever)
- Civic connections section: NEW (Partnership for SF, SF Art Institute)
- Cross-publication OpenAI map: NEW analytical section in notes
- Source URLs cited: 18 across all new entries
- Tests: 268/268 passing
- YAML validity: confirmed

---

## 2026-06-25 08:00 PT — Hour Type B: Journalist/Publication Research

**Focus:** MIT Technology Review staff expansion — 8 new journalists tracked (7 new entries + 1 major update), total journalists 59 → 67. Previously MIT TR had only 3 tracked staff (Honan, Heikkilä, Knight); now 10 current/former staff with full career histories.

### Key Discovery: Melissa Heikkilä departed MIT TR for Financial Times

**Major correction:** Heikkilä was listed as MIT TR's "current beat holder" for AI, but she departed in January 2025 for the Financial Times as AI correspondent. Her full career chain was incomplete — now expanded:
- Helsingin Sanomat (Finland's largest daily, ~2016-2018)
- The Economist (assistant news editor, ~2019-2020) — **previously unknown**
- POLITICO Europe (AI correspondent, ~2020-2022)
- MIT Technology Review (senior AI reporter, May 2022 – Jan 2025)
- Financial Times (AI correspondent, started Jan 27, 2025)

Notable irony: MIT TR + FT formed "The State of AI" editorial partnership (Oct 2025), where Heikkilä was paired with her former MIT TR colleague Eileen Guo on "The End of Privacy" edition.

### New journalists added (7):

1. **James O'Donnell** — Senior AI Reporter (Heikkilä's replacement)
   - Villanova BA (Econ/PoliSci) → Fulbright to Finland → Brookings → EIG → Princeton MPA → FRONTLINE PBS Tow Fellow → MIT TR
   - 2026 ASME National Magazine Award finalist (AI energy investigation with Casey Crownhart)
   - Policy/institutional power lens vs. Heikkilä's EU regulatory frame — measurable editorial shift
   - Sources: technologyreview.com/author/james-odonnell/, jrc.princeton.edu, pbs.org/wgbh/frontline

2. **Will Douglas Heaven** — Senior AI Editor
   - PhD CS Imperial College London → New Scientist chief tech editor → BBC Future Now founding editor → MIT TR (~2020)
   - Only MIT TR senior editor with a CS PhD — genuine technical depth
   - Shapes entire AI editorial direction, 219+ articles
   - Based in London — one of MIT TR's UK-based staff
   - Sources: technologyreview.com/author/will-douglas-heaven/, theorg.com, sciencefriday.com

3. **Eileen Guo** — Senior Reporter, Features & Investigations
   - Tufts BA → co-founded Impassion Afghanistan + Paiwandgah (Kabul, 2.5 years) → MIT Press Innovations → freelance (NYT, WaPo, NatGeo, Wired) → MIT TR (~2021)
   - Ida B. Wells Fellow (Type Investigations). Work sparked EU antitrust investigation (Amazon/iRobot), contract suspensions, US AI bias standards
   - MIT TR's primary accountability journalist — most explicitly critical editorial stance
   - Sources: eileenguo.com, muckrack.com/eileen-guo, talkingbiznews.com, ire.org

4. **Casey Crownhart** — Senior Climate & Energy Reporter
   - MIT BS ChemE + Literature → materials science startup → NYU SHERP MA → freelance → MIT TR (~2022)
   - 300+ articles. Writes The Spark climate newsletter. Science Friday regular contributor
   - ASME finalist with O'Donnell for AI energy investigation — cross-beat collaboration
   - Sources: technologyreview.com/author/casey-crownhart/, popsci.com, talkingbiznews.com

5. **Amy Nordrum** — Executive Editor of Operations
   - Ohio Univ BA → NYU SHERP MA → IEEE Spectrum news manager → MIT TR (Jul 2020) → NYU Stern MBA
   - Oversees franchise lists (10 Breakthrough Technologies, Innovators Under 35)
   - Not a reporter but shapes editorial ops and standards
   - Sources: amynordrum.com, technologyreview.com/author/amy-nordrum/, theorg.com

6. **Tate Ryan-Mosley** — Senior Tech Policy Reporter
   - Kellogg Institute fellow (conflict/post-war development, 2012) → tech strategy consultant → MIT TR researcher → MIT TR reporter (~2019/2020)
   - 113+ articles. The Technocrat newsletter. In Machines We Trust podcast
   - Covers tech policy, democracy, elections, facial recognition regulation
   - Sources: event.technologyreview.com/emtech-next/speakers, itgo.me (author page), muckrack.com

7. **Caiwei Chen** — China Reporter
   - Columbia MA → Rest of World → MIT TR (~2024)
   - 5+ years covering Chinese internet/tech. Part of Chaoyang Trap newsletter
   - Sources: talkingbiznews.com

8. **Jessica Hamzelou** — Senior Health/Biomedicine/Biotech Reporter
   - UCL BSc → Imperial College London MSc → 12+ years at New Scientist → MIT TR (~2021)
   - Second New Scientist → MIT TR pipeline (after Will Douglas Heaven)
   - Sources: talkingbiznews.com

### Analytical insights discovered:

1. **MIT TR is a net exporter of journalism talent:**
   - MIT TR → Wired: Will Knight (2018), Zeyi Yang (~2025), Emily Mullin (MIT TR → Knight SJF → Wired)
   - MIT TR → Atlantic: Karen Hao (2022)
   - MIT TR → Financial Times: Melissa Heikkilä (Jan 2025)
   - 5+ departures to other tracked/major publications in ~7 years

2. **New Scientist → MIT TR is an underappreciated British pipeline:**
   - Will Douglas Heaven (chief tech editor → senior AI editor)
   - Jessica Hamzelou (biomed reporter → senior reporter)
   - Both British, both Imperial College London connections (PhD, MSc)

3. **NYU SHERP is institutional pipeline to MIT TR:**
   - Amy Nordrum (MA → MIT TR)
   - Casey Crownhart (MA → MIT TR)
   - Same graduate program feeding both editorial and reporting staff

4. **O'Donnell replacing Heikkilä = editorial frame shift:**
   - Heikkilä: Finnish → EU regulatory beat (POLITICO Europe → MIT TR) → covered AI through European regulatory lens
   - O'Donnell: American → policy research (Brookings/Princeton) → FRONTLINE → covers AI through institutional power dynamics
   - Measurable difference in framing should appear in post-Jan-2025 MIT TR AI coverage

5. **Heikkilä's presence at FT may have catalyzed MIT TR + FT partnership:**
   - She departed Jan 2025, partnership announced Oct 2025
   - She was paired with former colleague Eileen Guo — pre-existing relationship

### Editorial changes updated:
- Added Heikkilä departure + O'Donnell replacement entry
- Added Caiwei Chen hire entry
- Connected to Zeyi Yang departure timeline

### Stats:
- journalists.yaml: +287 lines (8 new entries, 1 major update)
- editorial_changes.yaml: +14 lines (2 new entries)
- README.md: journalist count 59 → 67, added Heikkilä migration to examples
- Tests: 268 (all passing, no new tests — changes are career data additions)
- Commit: `0dab417`
- Pushed to GitHub: ✅

---

## 2026-06-25 06:00 PT — Hour Type A: Article Deep Dive

**Focus:** Entity detection coverage expansion — 3 new entity clusters and expanded aliases for 2 existing clusters, validated against Wired's "Meta's Very Own Smart Glasses Go on Sale Today for $299" (Julian Chokkattu, June 23, 2026).

### What was improved:

1. **Meta cluster expanded (+4 aliases):**
   - Alex Himel / Himel (Meta VP)
   - Ankit Brahmbhatt / Brahmbhatt (Sr. Dir. PM, quoted in glasses article)
   - Will Cathcart / Cathcart (WhatsApp head)
   - Muse Spark (Meta's first closed AI model)
   - Also removed "Horizon Worlds" and "Meta Horizon" from Meta cluster to avoid shadowing VR/Metaverse cluster

2. **EssilorLuxottica cluster expanded (+2 aliases):**
   - Francesco Milleri / Milleri (CEO)
   - LensCrafters (retail subsidiary)

3. **New "Smart Glasses Competitors" cluster (6 aliases):**
   - Gentle Monster, XREAL, Even Realities, Halo, Solos, Brilliant Labs
   - Explicit regex to avoid false positives (e.g., "frame" ≠ Brilliant Labs "Frame" product)

4. **New "Celebrity/Influencer" cluster (2 aliases):**
   - Kylie Jenner, Jenner (with possessive support: `Jenner's`)
   - Previously unclustered — Kylie Jenner had 3+ mentions in glasses article as Starfire designer

5. **New "Indian Fintech" cluster (4 aliases):**
   - CRED, Kunal Shah, PhonePe, UPI
   - Case-sensitive regex for CRED and UPI to avoid false positives

### Validation — Wired glasses article re-analysis:

| Metric | Before | After |
|---|---|---|
| Entity clusters detected | 5 | 7 |
| Total entity mentions | 64 | 71 |
| New detections | — | Kylie Jenner ×1, Jenner ×2, LensCrafters ×1, Gentle Monster ×1, Muse Spark ×1, Ankit Brahmbhatt ×1 |

Previously, "Kylie Jenner" was flagged as a known limitation ("personal names without organization context aren't clustered"). Now resolved with the Celebrity/Influencer cluster. Analysis file updated to reflect 7-cluster entity distribution.

### Total entity clusters: 25 → 28

### Stats:
- Files modified: `mediascope/analyze/entities.py`, `examples/sample_output/wired_meta_glasses_launch_self_branded_2026_06_23_analysis.md`
- Tests: 268 (all passing, no new tests this iteration — changes are additive aliases, covered by existing cluster-format tests)
- Lines changed: +29/-1 in entities.py

---

## 2026-06-25 01:00 PT — Hour Type D: Toolkit Quality & Documentation

**Focus:** Documentation-code synchronization — METHODOLOGY.md framing device taxonomy was 4 types behind the codebase (22 documented vs 26 implemented), README had stale journalist count (51 vs 56), and no automated guard against future drift.

### What was improved:

1. **METHODOLOGY.md §4.1 — Framing device taxonomy synchronized (22 → 26 types):**
   - Core devices expanded from 8 → 10:
     - **CEO Personalization** added: possessive/led constructions attributing corporate actions to the CEO personally ("Zuckerberg's Meta," "Musk-led Tesla"). 2 regex patterns. Makes institutional decisions feel like personal edicts, amplifying negative framing.
     - **Litigation Framing** added: positioning entities as adversarially using courts ("seeking/filing legal challenge," "legal battle against," "took X to court"). 3 regex patterns. Frames litigation as aggression rather than legitimate dispute resolution.
   - Extended devices expanded from 11 → 13:
     - **Geopolitical Regulatory Pressure** added: framing international regulatory tensions as geopolitical confrontation. 5 regex patterns covering embassy/diplomatic submissions, sovereignty/defiance rhetoric, trade-tension language, transatlantic framing. Discovered from Guardian UK tech crackdown article.
     - **Sovereignty Framing** added: deploying national/patriotic identity language to delegitimize foreign positions ("British families," "our children," "national interest" near tech entities). 5 regex patterns. Discovered from Guardian UK tech crackdown article. Distinct from loaded_language — strategic national identity deployment vs emotional vocabulary.
   - Structural (post-pass) unchanged at 3: kicker_framing, analogy_stacking, speculative_framing
   - Updated tier count text: "core devices (10 pattern-matched types)" and "not captured by the core devices"

2. **README.md — Stale numbers corrected:**
   - Journalist count: 51 → 56 (added Turton, Gilbert, Yang in recent Type B iterations, plus prior additions)
   - Added Zeyi Yang to named migration examples
   - Test count: 236 → 239

3. **New registry tests (3 tests in TestFramingDeviceRegistry class):**
   - `test_pattern_based_device_count`: asserts exactly 23 pattern-based types in `_DEVICE_PATTERNS`
   - `test_all_expected_types_registered`: enumerates all 23 expected types (10 core + 13 extended) and asserts each exists in the registry — catches both missing and undocumented types
   - `test_structural_types_in_detect_function`: verifies all 3 structural types (kicker_framing, analogy_stacking, speculative_framing) appear in `detect_framing_devices()` source
   - These tests will **automatically catch future doc-code drift** — adding a framing type without updating docs (or vice versa) will fail the test suite

### Key insight:

**Documentation drift is a real problem in rapidly-iterated research toolkits.** The 4 missing types were added across 3 separate iteration cycles (Jun 22-24), each with proper code and code-level comments, but nobody updated METHODOLOGY.md. The registry tests solve this structurally — the test suite now enforces documentation-code synchronization. This is especially important for MediaScope because the methodology documentation IS the academic credibility: a tool that claims to detect 22 framing types but actually implements 26 looks sloppy if anyone audits it.

### Stats:
- METHODOLOGY.md: 4 new device type entries, count updated 22→26
- README.md: journalist count 51→56, test count 236→239
- Tests: 236 → 239 (+3 registry tests)
- All 239 tests passing
- Commit: `5ebd1de`
- Pushed to GitHub: ✅

---

## 2026-06-25 00:00 PT — Hour Type C: Ownership & Funding Deep Dive

**Focus:** The Guardian — six major gaps filled: STEL PE/VC fund managers identified, FY2025/26 financial data added, Apple News relationship documented, Cadwalladr v Banks litigation fully recorded, Guardian US operations expanded, and known_conflicts updated with 3 new entries (including a novel "counter-conflict" concept).

### What was improved:

1. **STEL PE/VC portfolio managers — first comprehensive identification (stel_private_investments section):**
   - STEL has £352M committed across 28 managers, with £276M NAV
   - **Hg Capital** identified as LARGEST PE commitment (Genesis 11, Mercury 5, Saturn strategies). Hg is the largest European software investor, $110B AUM, portfolio of ~60 B2B software companies worth $195B aggregate enterprise value. Self-described "AI leader in private equity." Creates diffuse exposure to the AI/enterprise tech ecosystem.
   - **Verdane** — Northern European sustainable growth buyouts (energy transition, sustainable consumption)
   - **G2VP** — US growth-stage VC at intersection of sustainability × technology
   - **Bridges Fund Management** — UK needs-driven real estate (care homes, affordable housing)
   - **Frazier Life Sciences** — US biotech/therapeutics VC (added FY2024/25)
   - **SV Health Investors (SV8 Biotech Fund)** — biotech VC (Dec 2025, per PEI database)
   - **Ninety One** — Emerging Market Transition Debt (EMTD) credit strategy
   - Unnamed female founders fund (healthcare, education, environmental tech)
   - Also documented advisors: Cardano (SAA + public markets), Cambridge Associates (private investments), Redington (environmental sustainability)
   - Sources: STEL 2024/25 Performance Report, STEL 2021/22 Report, PEI database (14 fund commitments, 3 visible without subscription)

2. **FY2025/26 financial data — Guardian US now $81.4M:**
   - Digital reader revenue reached £125M in year to March 2026 (up 17% YoY from £107M)
   - US revenue: $81.4M (up 25% YoY), strongest result in 15-year US history
   - US reader revenue up 32%, ad sales up 9%
   - US team doubled to 200+ employees (150 editorial) in 3 years
   - 80%+ of income from outside UK (Katharine Viner at WAN-IFRA Congress, Jun 2026)
   - Corrected FY2024/25: US + Canada revenue was £55.5M (+23%), not "£50M+"
   - Washington Post endorsement controversy (Oct 2024) drove sustained US reader surge
   - New US video podcast "Stateside" launched May 2026
   - Payment channels expanded: Feast recipe app, main app, Guardian Weekly, print
   - Sources: Tomorrow's Publisher, A Media Operator, WAN-IFRA

3. **Apple News relationship — DROPPED in 2017:**
   - Guardian dropped Apple News AND Facebook Instant Articles in April 2017
   - Chose direct reader relationships over platform distribution
   - Statement: "Our primary objective is to bring audiences to the trusted environment of the Guardian"
   - ZERO Apple platform revenue, ZERO Facebook platform revenue
   - Unlike Condé Nast (Wired), which is in Apple Intelligence negotiations (~$50M+)
   - Added as revenue_relationship entry with "none (dropped)" type
   - Source: AppleInsider (Apr 2017)

4. **Cadwalladr v Banks litigation — full timeline documented (litigation_connections):**
   - Banks sued Cadwalladr INDIVIDUALLY (not Guardian/TED) over 2019 TED Talk about Russian connections
   - High Court (Jun 2022): Cadwalladr won — public interest defense upheld by Steyn J
   - Court of Appeal (Feb 2023): Banks partly won — TED Talk liability after Apr 2020
   - Settlement (Apr 2023): £35,000 damages via consent order
   - Costs order (May 2023): 60% Banks' High Court costs + repay + 1/3 appeal = ~£560,000+
   - Supreme Court refused permission to appeal on costs
   - Cadwalladr crowdfunded >£1.1M for defense; had £275,000 insurance
   - Classified as SLAPP by NUJ, Anti-SLAPP Coalition, RSF, ARTICLE 19, PEN International
   - Guardian signed Anti-SLAPP Coalition statement — institutional backing despite not being a party
   - Sources: judiciary.uk (2 rulings), PEN International, NUJ, openDemocracy, Chambers and Partners

5. **Cambridge Analytica catalytic journalism — documented:**
   - Guardian (Cadwalladr) + NYT co-broke scandal (2018), triggering $5.8B+ in enforcement actions
   - $5B FTC fine, $725M class action, $100M SEC, $31.85M Australia, DC AG lawsuit (revived Jul 2025)
   - Delaware Chancery meta-oversight trial (2026, Zuckerberg testimony)
   - Guardian's institutional identity partly defined by exposing Facebook/Meta data practices
   - Sources: Reuters, 9to5Mac

6. **Known conflicts expanded (3 new entries, total now 9):**
   - NEW: STEL PE/VC portfolio (severity 1) — Hg Capital as largest PE holding, diffuse tech ecosystem exposure
   - NEW: Apple News/Facebook drop (severity -1) — first "counter-conflict" entry. Guardian's proactive platform independence partially offsets other conflicts.
   - NEW: (Counter-conflict concept introduced — negative severity indicates structural independence factor)
   - Notes section fully rewritten with updated reality assessment:
     - Added 2 new testable hypotheses (Cambridge Analytica institutional identity, Washington Post controversy effect)
     - Added counter-conflicts section documenting 4 structural independence factors
     - Updated cross-publication comparison with latest data (Wired $7B Reddit stake, Atlantic OpenAI/io Products $6.5B exit, NYT Carlos Slim 25.1%)

### Key analytical insights:

1. **The Guardian's structural independence is MORE robust than previously documented:** Dropping Apple News in 2017 was forward-looking — the Guardian voluntarily gave up platform revenue before it became a conflict issue. No other tracked publication has done this. Combined with the reader-funded model (£125M and growing), the Guardian has the least platform dependency of any publication in the dataset.

2. **Hg Capital is an interesting but diffuse conflict:** As the largest European software investor ($110B AUM, ~60 portfolio companies), Hg is the only STEL PE holding with meaningful tech ecosystem exposure. But it's B2B enterprise software — not social media, not consumer tech, not direct Meta competition. The conflict is sector-level, not company-specific. This is consistent with the "partial control" reclassification.

3. **The Cadwalladr litigation reveals institutional editorial alignment:** Banks targeted Cadwalladr individually rather than the Guardian as an organization, but the Guardian signed the Anti-SLAPP Coalition statement supporting her defense. This shows the Guardian's corporate leadership (not just editorial) backing the adversarial journalism that defines its Meta coverage identity. The £35,000 damages + ~£560,000 costs represent a significant personal cost for investigative journalism about powerful figures connected to Facebook.

4. **US growth is transforming the Guardian's conflict profile:** At $81.4M (and growing 25%+/yr), the US business is approaching the threshold where its financial interests meaningfully affect editorial decisions. The Washington Post endorsement controversy accelerated this — the Guardian is now actively positioning itself as the alternative to captured US media. This reader-funded growth REDUCES tech-company leverage (no advertiser dependency) but INCREASES the editorial incentive to frame US tech companies critically (because that's what US readers are paying for).

5. **Novel "counter-conflict" concept introduced:** Previous analysis only tracked conflicts (things that bias coverage). But the Guardian's structural choices — dropping platforms, reader-funding, non-profit ownership — actively work AGAINST bias. Modeling these as negative-severity conflicts creates a more complete picture of a publication's overall incentive landscape.

### Stats:
- Guardian profile: 386 → 586+ lines (expanded by ~200 lines)
- Known conflicts: 6 → 9 (+3, including 1 counter-conflict)
- Litigation connections: 0 → 2
- Revenue relationships: 3 → 4 (+Apple News dropped entry)
- Named STEL PE/VC managers: 0 → 7+
- New financial data years: FY2025/26 added
- Source URLs cited: 22 across all new entries
- Tests: 236/236 passing
- YAML validity: confirmed

**Focus:** Wired's Drummond-era politics team (William Turton, David Gilbert) and a cross-publication migration (Zeyi Yang, MIT TR → Wired). These three journalists were referenced in existing editorial_changes notes but lacked their own career entries — a significant gap since Turton and Gilbert are core members of Drummond's editorial transformation, and Yang represents the third MIT TR → Wired migration in the dataset.

### What was improved:

1. **William Turton — new journalist entry (journalists.yaml):**
   - Prodigy who started at 14, broke Lizard Squad at 17, skipped college
   - Career: Daily Dot (Jun 2014) → Gizmodo (Apr 2016) → The Outline (May 2017, hired by Drummond) → Vice News Tonight (Oct 2017) → Bloomberg (Jul 2019) → Wired (Nov 6, 2023) → ProPublica (Feb 2026)
   - DRUMMOND ORBIT: Followed Drummond through Gizmodo → The Outline → Wired — three newsrooms, deepest network in dataset
   - Left Wired for ProPublica Feb 2026 — FIRST departure from Drummond's politics team
   - FBI/DOJ beat departure signals tech-politics hybrid model fragmenting
   - Sources: Poynter (2 articles), TalkingBizNews (3 articles), ProPublica press release, SevenLetter, MediaPost, RocketReach

2. **David Gilbert — new journalist entry (journalists.yaml):**
   - Career: TrustedReviews (news editor) → IBTimes (EU/UK tech editor, ~4 yrs) → Vice (Sep 2016 – Sep 2023, 7 yrs) → Wired (Oct 2023)
   - First of three Drummond politics team hires
   - Ireland-based — covers US extremism remotely (Coffee w/ Journalist podcast confirmed)
   - Beat: disinformation, online extremism, far-right movements, QAnon, mass shootings
   - Education: UCC BA (American Literature, American Cinema, Silent Cinema, Old English, Beowulf, Greek & Roman Civilisation)
   - Sources: TalkingBizNews (2 articles), RocketReach, Eventible speaker profile, Prowly, BuzzSumo, Coffee w/ Journalist podcast

3. **Zeyi Yang — new journalist entry (journalists.yaml):**
   - Career: Rest of World (Jun 2020) → Protocol (Jan 2021) → MIT Tech Review (Apr 2022) → Wired (~Jan 2025)
   - CROSS-PUBLICATION MIGRATION: MIT TR → Wired — third such migration after Will Knight (2018) and Gideon Lichfield (2020)
   - Created China Report newsletter at MIT TR, 144 posts
   - 2024 ASME NEXT Award winner
   - Only tracked journalist who reads primary Chinese-language sources
   - Education: Peking University (BA), Columbia (MA Journalism + International Affairs)
   - Yale Poynter Fellow (Mar 2026 talk: "How to Cover 'The Chinese Century'")
   - Co-founded LGBTQ Mandarin podcast 无所不JI
   - Sources: Yale Law School event page, Poynter Fellowship page, TalkingBizNews (2 articles), NüVoices podcast, Muck Rack, MIT TR author page

4. **Editorial changes (editorial_changes.yaml):**
   - Wired: +2 entries (5 → 7): Turton departure (Feb 2026), Yang hire (Jan 2025)
   - MIT Tech Review: +1 entry (7 → 8): Yang departure (Jan 2025)

### Key analytical discoveries:

**The Drummond Personnel Pipeline is deeper than previously documented:**
- Turton followed Drummond through THREE newsrooms (Gizmodo 2016 overlap → The Outline 2017 direct hire → Wired 2023 politics team)
- This is more interconnected than the Feiger-Drummond Vice connection (1 overlap period)
- The Gizmodo→Outline→Vice→Wired pathway created a core personnel cluster carrying adversarial editorial DNA across 4+ newsrooms over 7 years

**Turton's departure fractures the politics team:**
- First departure from the Nov 2023 trio (Feiger, Turton, Gilbert)
- His move to ProPublica's FBI/DOJ beat signals pure federal law enforcement separated from Wired's tech-politics hybrid
- Remaining team (Feiger, Gilbert) now weighted toward disinformation/political campaigns, losing Turton's cybersecurity + campaigns intersection
- Wired posted a job listing for "senior correspondent to cover politics" ($115K-$200K, DC-based, 7+ years experience) — likely his replacement

**MIT TR → Wired is a one-directional talent pipeline:**
- Will Knight (2018), Gideon Lichfield (2020), Zeyi Yang (~2025) — all moved MIT TR → Wired
- Zero reverse migrations (Wired → MIT TR) documented
- Pattern: MIT's research-adjacent credentialing → Condé Nast's larger platform
- Yang's departure leaves MIT TR without a dedicated China tech correspondent during peak US-China tech competition

### Stats:
- Total journalists: 53 → 56 (+3)
- Cross-publication migrants: 10 → 11 (+Zeyi Yang)
- Wired editorial changes: 5 → 7 (+2)
- MIT TR editorial changes: 7 → 8 (+1)
- Source URLs cited: 21 across all new entries
- Tests: 236/236 passing
- YAML validity: confirmed (both files)
- Commit: `fabbd12`
- Pushed to GitHub: ✅

---

## 2026-06-24 22:00 PT — Hour Type A: Article Deep Dive

**Focus:** Guardian article "Crackdown on tech platforms will go ahead despite US intervention, says No 10" (Dan Milmo & Jessica Elgot, 2026-06-09). Previously had article text but no analysis. Deep dive revealed a novel framing device pattern — sovereignty_framing — warranting new toolkit detection capability.

### What was improved:

1. **Full article analysis (134 lines):**
   - 8-dimension manual sentiment scoring vs toolkit expectations
   - 9 framing devices identified manually (4 not in toolkit vocabulary)
   - Entity distribution: UK Govt 48%, US Govt 32%, Tech/Meta 20%
   - Source imbalance: 6 pro-regulation voices, 0 tech company voices
   - Conflict of interest assessment: Guardian's OpenAI licensing deal relevant but undisclosed (AI chatbot restrictions part of UK consultation)
   - Comparison with how peer publications would frame the same story
   - 3 toolkit improvement recommendations

2. **NEW framing device type — sovereignty_framing (framing.py):**
   - 5 regex patterns detecting national/patriotic identity language in tech regulation contexts
   - Pattern 1: National adjective + people/families/interest ("British families", "our children", "American innovation")
   - Pattern 2-3: "national interest/security" near tech entities (bidirectional)
   - Pattern 4: "act in the [nation's] interest"
   - Pattern 5: "will not deter/stop [nation]"
   - Fires 5× on Guardian article (all true positives): "British young people", "British parents", "British families", "act in the UK's national interest", "will not deter the UK"
   - Also fires on NYT AI reviews article (true positive: "national security" near Meta)
   - Distinct from loaded_language — sovereignty framing is a strategic rhetorical technique that deploys national identity to delegitimize foreign corporate/government positions

3. **Anonymous source detection improvements (sentiment.py):**
   - Added UK-style passive institutional attribution: "it is understood that", "it is believed that", "it is thought that", "it has emerged that" — standard Guardian/UK press Lobby sourcing construction
   - Added "one/a senior [party]? [title]" pattern for unnamed political/industry figures described by seniority + role (e.g., "one senior Republican congressman")

4. **Test update (test_nyt_ai_reviews.py):**
   - `test_total_device_types` updated from 3 → 4 expected device types to include sovereignty_framing (true positive match)

### Why this article:
The Guardian UK tech crackdown article was one of 4 articles with text but no analysis in the sample_output directory. As a co-byline from Guardian's global tech editor Dan Milmo, it reveals core Guardian editorial DNA: sovereignty framing, source imbalance, CEO personalization, and kicker positioning — all patterns that generalize across the Guardian's tech coverage.

### Analytical insights:
- **Sovereignty framing is the Guardian's primary rhetorical tool** for UK tech regulation coverage. By framing regulation as patriotic duty ("British families"), the article transforms corporate regulation into national defense, making any opposition (US government, Meta) appear anti-British.
- **100% source imbalance** is not accidental. The article is ABOUT regulating tech platforms, yet no tech platform spokesperson is quoted. This "refusal by absence" is subtler than "declined to comment" and is not currently detected by the toolkit.
- **Meta as kicker:** Meta appears only in the final paragraph, introduced solely as a legal challenger. The reader's last impression is Meta-as-litigant, regardless of the article's actual topic (UK-US diplomatic tension). Combined with CEO personalization ("Mark Zuckerberg's Meta"), this isolates Meta from the generic "tech platforms" discussed earlier.

### Stats:
- Analysis file: 134 lines, 15,271 bytes
- framing.py: +64 lines (sovereignty_framing patterns)
- sentiment.py: +21 lines (UK anonymous source patterns)
- test_nyt_ai_reviews.py: +3/-1 lines (updated assertion)
- Tests: 236/236 passing
- Total device types: 22 → 23 (+sovereignty_framing)
- Commit: `ebcf8e3`
- Pushed to GitHub: ✅

---

## 2026-06-24 18:00 PT — Hour Type D: Toolkit Quality & Documentation

**Focus:** Comprehensive overhaul of ADDING_PUBLICATIONS.md (weakest doc file, 68 → 678 lines), plus README Testing section and ARCHITECTURE test annotations.

### What was improved:

1. **ADDING_PUBLICATIONS.md — complete rewrite (10x expansion):**
   - **Complete reference for ALL 12 profile sections** (was documenting only 5):
     - `known_conflicts`: severity scale (1-5), conflict types, evidence requirements, real examples from Wired profile
     - `editorial_leadership`: field descriptions, why ITS analysis needs stance documentation
     - `key_journalists`: what to document, who to prioritize
     - `bias_ratings`: Ad Fontes (0-64 reliability, -42/+42 bias), AllSides (5-point), MBFC scales documented
     - `ai_crawl_policy`: what crawler permissions imply about licensing deals
     - `litigation_connections`: types (funder/plaintiff/connected_party), PACER/UK CAT sources
     - `internal_ai_tools`: "hypocrisy index" analytical value, NYT as example
     - `editorial_stance`: how to document positions with evidence
   - **New section: Adding Career Data** — complete documentation of:
     - `journalists.yaml` format: career event fields (8 fields documented with types/requirements), publication slugs for tracked publications, how non-tracked publications work
     - Priority order for who to add: cross-publication migrants > multi-outlet > beat leads > recent hires
     - `editorial_changes.yaml` format: leadership change fields, why notes matter for ITS
   - **Research workflow:** step-by-step (5 steps, ~6 hours), specific sources for each section
   - **Expanded validation:** YAML validity check commands, 10-item completeness checklist, 8 quality standards for repo contributions
   - **Revenue relationships:** compound relationship documentation (NYT Amazon example), documenting absence of relationships as analytically significant
   - **FAQ:** 5 questions covering paywalled pubs, opaque ownership, complex corporate structures, false-positive entity detection, departed journalists
   - **Examples:** minimal profile (Fox News, 3-entity chain) + reference to wired.yaml as complete profile

2. **README.md — Testing section + gallery update:**
   - New "Testing" section: 236 tests across 8 test files, table describing each file's coverage
   - Test execution commands (pytest -v, -k keyword, specific file)
   - Regression test requirement noted for all analysis improvements
   - Bosworth reorg article added to Sample Output Gallery (was missing — `wired_meta_bosworth_atrocious_reorg_2026_06_16_*`)

3. **ARCHITECTURE.md — test file annotations:**
   - File Layout tree updated: 8 test files annotated with analytical coverage areas
   - Explicit test count (236) added to tests directory entry

### Why ADDING_PUBLICATIONS.md:
This was the weakest documentation file — the actual Wired profile uses 12 different YAML sections, but the guide only documented 5. Anyone trying to add a new publication would have to reverse-engineer the existing profiles to figure out `known_conflicts`, `editorial_leadership`, career data formats, etc. The guide is now comprehensive enough that a contributor (human or AI agent) can build a complete profile from scratch without examining existing profiles.

### Stats:
- ADDING_PUBLICATIONS.md: 68 → 678 lines (+897%)
- README.md: +29 lines (Testing section + gallery entry)
- ARCHITECTURE.md: +9 lines (test annotations)
- Tests: 236/236 passing (no code changes)
- Commit: `5aab6be`
- Pushed to GitHub: ✅

---

## 2026-06-24 17:00 PT — Hour Type C: Ownership & Funding Deep Dive

**Focus:** NYT — three major gaps in the ownership/funding profile. Carlos Slim's 25.1% Class A shareholding (entirely missing), compound Amazon dependency via Wirecutter affiliate revenue ($70-125M+/yr, previously documented at only $20-25M/yr AI deal), and Amazon's March 2026 affiliate commission cuts (up to 50%, directly impacting NYT revenue).

### What was improved:

1. **Carlos Slim / Control Empresarial de Capitales — new ownership_chain entry:**
   - SEC Schedule 13G/A filed February 9, 2026 (signed by Marco Antonio Slim Domit as Attorney-in-Fact)
   - Control Empresarial de Capitales S.A. de C.V. owns 29,123,098 Class A Common Shares
   - = 25.1% of 115,847,488 outstanding Class A shares (per Form 10-Q filed Oct 30, 2025)
   - LARGEST INDIVIDUAL SHAREHOLDER of any tracked publication
   - Value: ~$2.07B at $71.22/share (Jun 24, 2026)
   - Slim Family: Carlos Slim Helú, Carlos/Marco Antonio/Patrick Slim Domit, 3 daughters — beneficiaries of Mexican trust owning all voting equity of Control Empresarial
   - History: $250M emergency loan at 14.05% interest (Jan 2009) during NYT near-bankruptcy, converted to equity, sold ~1.5M shares in 2017-18, position grew from ~17% to 25.1% partly via NYT share buybacks reducing denominator
   - Files as 13G (passive) — no board seats, no known editorial influence
   - Carlos Slim: net worth ~$99.1B (Bloomberg Jul 2025, 18th globally), core fortune from Telmex/América Móvil telecom monopoly
   - Sources: SEC EDGAR (0001140361-26-004396), Wikipedia
   - Added as new known_conflict entry (severity 2)

2. **Compound Amazon dependency ($70-125M+/yr) — new wirecutter_affiliate_revenue section + amazon_affiliate_commission_cuts_2026 section:**
   - FY2025 "Affiliate, licensing and other revenues" = $308.1M (10.9% of total $2,824.9M revenue)
   - Quarterly breakdown: Q1 ~$69.9M, Q2 $70.5M, Q3 ~$67.5M, Q4 $100.2M (holiday spike)
   - Amazon AI licensing deal ($20-25M/yr, started May 2025) contributed ~$13-17M in FY2025 (partial year)
   - Remaining $291-295M is primarily Wirecutter affiliate + other licensing
   - Wirecutter acquired for $30M (2016), made $20M+ in 2018 alone (Ahrefs)
   - CJR reported NY Mag's Strategist got 80%+ of affiliate revenue from Amazon — Wirecutter likely similar
   - Combined Amazon exposure: $70-125M+/yr = LARGEST tech company dependency in 5-publication set
   - Sources: NYT FY2025 10-K (SEC EDGAR), Ahrefs case study, CJR, Digiday, Poynter

3. **Amazon affiliate commission cuts (March 2026) — new section:**
   - Amazon restructured Associates program starting March 9, 2026 (U.S.)
   - Premium rates (up to 10%) reset to 4-5%
   - Milestone-based incentive tiers eliminated for most publishers
   - Year-over-year performance bonuses gutted
   - Reporting tools degraded
   - NEVER publicly announced — publishers learned from account manager conversations
   - One deal-site publisher revised 2026 Amazon revenue forecast down 50%
   - 7 publishers/partners confirmed to Adweek
   - Source: Adweek (Mark Stenberg, ~May 17 2026)
   - Creates a dynamic where Amazon is simultaneously squeezing (affiliate cuts) and subsidizing (AI licensing) NYT

4. **Revenue relationship upgraded — Amazon:**
   - Changed from `relationship_type: "ai_licensing"` to `"ai_licensing + affiliate_revenue (COMPOUND)"`
   - Changed from `estimated_value: "$20-25M/year"` to `"$70-125M+/year (combined)"`
   - Added 4 source URLs including SEC filing and Adweek
   - Documented the timing dynamic: AI licensing signed May 2025, affiliate cuts March 2026

5. **New conflict entries:**
   - `compound_amazon_dependency` (severity 5) — Karen Weise covers Amazon while it pays NYT $70-125M+/yr. Most direct testable revenue/coverage conflict in dataset
   - `major_shareholder_concentration` (severity 2) — Slim Family's 25.1% Class A stake, governance observation
   - `no_meta_counterweight` updated to reference $70-125M+ compound figure

6. **YAML parse fix:**
   - Fixed pre-existing YAML validity error in `internal_ai_tools` section (mixed list/mapping under same key)
   - Changed to `tools:` sub-key for the list entries
   - YAML now parses cleanly

### New analytical questions:
1. Does Amazon coverage soften under the compound $70-125M+/yr dependency? Compare Karen Weise's pre-May-2025 vs post-May-2025 Amazon coverage tone
2. Does the March 2026 affiliate commission cut change coverage posture? (Paradox: Amazon cutting NYT's income could embitter OR make NYT more deferential to protect AI deal)
3. Does Q1 2026 reporting show Wirecutter revenue decline from affiliate cuts?
4. How does Slim's 25.1% interact with Sulzberger dual-class control?

### Stats:
- NYT ownership chain: 3 → 4 entities (+33%)
- NYT known conflicts: 4 → 6 (+50%)
- YAML validity: FIXED (pre-existing parse error corrected)
- Tests: 236/236 passing (no code changes, profile-only update)
- Commit: `1817131`
- Pushed to GitHub: ✅

---

## 2026-06-24 16:00 PT — Hour Type B: Journalist/Publication Research

**Focus:** The Guardian — expanded from 8 to 10 tracked journalists and 9 to 12 editorial changes. Guardian had the biggest coverage gap: only 3 active tech journalists tracked (Dan Milmo, Johana Bhuiyan, Blake Montgomery) despite being one of the most analytically important publications for the Meta coverage bias project. Four journalists had departed since 2024 (Alex Hern → Economist, Kari Paul → art school, Samantha Oltman → Bloomberg, Hibaq Farah → NYT).

### What was improved:

1. **Dara Kerr — new journalist entry (journalists.yaml):**
   - Guardian US tech reporter (Dec 2024–present)
   - Career: freelance → CNET/CBS Interactive (Sep 2014–Jan 2021) → The Markup (Jan 2021–Jan 2023) → NPR (Jan 2023–Nov 2024) → Guardian (Dec 2024–)
   - Education: NYU BA, Columbia SIPA (International Relations), UC Berkeley Graduate School of Journalism
   - Beat: tech labor, gig economy, surveillance, Big Tech accountability
   - Based in Bay Area. Originally from Colorado, lived in Latin America
   - Replaces Kari Paul's West Coast tech reporter role
   - Analytical value: Career arc shows consistent move toward public-interest, accountability-focused journalism models — each employer operates further from advertising-revenue dependency (CNET → nonprofit Markup → public media NPR → reader-funded Guardian). The Markup's data-driven investigative methodology is the analytical template she brings
   - Sources: TalkingBizNews (4 articles: CNET departure, Markup hire, Markup departure, NPR hire, NPR departure, Guardian hire), DIARY directory (Jan 6 2025 announcement), AeroLeads profile

2. **Robert Booth — new journalist entry (journalists.yaml):**
   - Guardian UK Technology Editor (replaced Alex Hern, ~Oct 2024)
   - NOT a cross-publication migration — 24-year Guardian veteran, internal beat change
   - Previous beat: housing, homelessness, social affairs (20+ years)
   - Known for: Grenfell Tower fire coverage (7-year inquiry, 72 deaths, corporate dishonesty exposé with Emine Sinmaz), FOI-intensive investigative methodology, Orwell Foundation panelist
   - Analytical value: Guardian deliberately chose investigative rigor over tech-domain expertise. His Grenfell template (systemic corporate failure → government negligence → vulnerable population harm) maps directly onto tech accountability narratives. Tests whether an investigative/social affairs frame produces different tech coverage than tech-native reporters
   - Sources: Orwell Foundation profile, Muck Rack (confirms current UK Technology Editor title), TalkingBizNews (Hern departure notice), WhatDoTheyKnow (FOI to Cabinet Office re: Grenfell companies, Sep 2024), Guardian Grenfell coverage

3. **Caspar Llewellyn Smith — new editorial change entry (editorial_changes.yaml):**
   - Guardian Chief AI Officer (~Jan 2024)
   - 20+ year Guardian veteran: Daily Telegraph → Observer Music Monthly (2003) → Head of Culture → editor of theguardian.com → Director of Digital Strategy → executive committee (2015) → Chief Product Officer (~5 years) → CAIO
   - Among first major UK newspapers to appoint a dedicated CAIO
   - 4 focus areas: (1) external AI licensing agreements (making sure Guardian gets paid), (2) internal AI tool deployment, (3) strategic thinking about AI/journalism future, (4) org-wide AI training
   - Set up Guardian AI Council (senior editors + technologists)
   - Participated in Globe and Mail Foundation "Editing Democracy" panel (2026)
   - Analytical value: CAIO role creates institutional AI strategy at executive level — separate from editorial coverage of AI. Dual positioning (covering AI critically while commercially licensing content to OpenAI) is the central tension in Guardian's AI posture
   - Sources: The Org (title/career), The Media Stack interview (role details, 4 focus areas), BusinessWire (panel appearance)

4. **Robert Booth — UK Technology Editor editorial change (editorial_changes.yaml):**
   - Hern (11 years, tech-specialist) → Booth (24 years, zero tech journalism experience)
   - Signal: Guardian values investigative methodology over subject-matter expertise

5. **Dara Kerr — US Technology Reporter editorial change (editorial_changes.yaml):**
   - Paul (departed mid-2024) → Kerr (Dec 2024), West Coast/Bay Area role continuity

### Guardian tech desk current active roster:
- **UK:** Dan Milmo (global tech editor), Robert Booth (UK tech editor)
- **US:** Blake Montgomery (US tech editor, NY), Johana Bhuiyan (senior reporter, surveillance/accountability), Dara Kerr (reporter, Bay Area)
- **Leadership:** Caspar Llewellyn Smith (Chief AI Officer), Katharine Viner (EIC)
- **Departed 2024:** Alex Hern (→ Economist), Kari Paul (→ art school), Samantha Oltman (→ Bloomberg, after only 4 months), Hibaq Farah (→ NYT Opinion)

### Editorial turnover analysis:
The Guardian's tech desk experienced ~50% personnel turnover in 2024 alone (4 departures from ~8 active tech journalists). The replacements reveal a clear editorial strategy:
- **UK:** Replaced a tech-native specialist (Hern) with an investigative generalist (Booth) — prioritizing accountability methodology over domain expertise
- **US:** Replaced a departing reporter (Paul) with a labor/accountability specialist (Kerr) — deepening the accountability-journalism pipeline that Johana Bhuiyan already represents
- **Structural:** Created a CAIO role to manage the commercial/editorial AI tension, rather than leaving it to editorial leaders

### Files modified:
- `profiles/careers/journalists.yaml` — 2 new journalist entries (Dara Kerr, Robert Booth)
- `profiles/careers/editorial_changes.yaml` — 3 new entries (Llewellyn Smith CAIO, Booth UK tech editor, Kerr US tech reporter)

### Stats:
- Guardian journalists tracked: 8 → 10 (+25%)
- Guardian editorial changes: 9 → 12 (+33%)
- Total journalists: 51 → 53
- Tests: 236/236 passing (no code changes)
- Commit: `cc9da1e`
- Pushed to GitHub: ✅

---

## 2026-06-24 15:00 PT — Hour Type A: Article Deep Dive

**Focus:** NYT — "U.S. Presses Meta to Agree to A.I. Reviews" (June 23, 2026). Manual analysis vs toolkit comparison, with 3 pattern fixes (2 anonymous source patterns, 1 juxtaposition false positive) and 20 new tests.

### What was improved:

1. **New anonymous source pattern: numbered government officials**
   - Problem: "two government officials said" (paragraph 8) was not detected by any anonymous source pattern in either `sentiment.py` or `framing.py`
   - Root cause: patterns covered "people familiar with," "sources close to," "a person with knowledge of" — but NOT numbered institutional officials as anonymous sources
   - Pattern added to both files: `N government/administration/intelligence/defense/senior/federal/White House/Commerce officials/aides/advisers said/told/confirmed`
   - Impact: anonymous_authority framing devices 3 → 5 in this article; anonymous source detection 6 → 8
   - This pattern type is extremely common in NYT/WaPo government-pressure reporting

2. **New anonymous source pattern: person-involved proximity**
   - Problem: "one person involved in the process said" (paragraph 10) was missed
   - Root cause: existing patterns required "knowledge of" but not "involved in" / "close to" / "inside" / "privy to" — different semantic category (proximity vs knowledge)
   - Pattern added to both files: `one/a person involved in|close to|inside|with the|within the|privy to|briefed on|engaged in` + context nouns (process, matter, talks, discussions, negotiations, deliberations, effort, planning)
   - Impact: catches a common attribution construction in regulatory and diplomatic reporting

3. **Juxtaposition false positive fix: "government" + "public" in policy context**
   - Problem: "government up to 30 days to evaluate A.I. models before their release to the public" triggered military/consumer juxtaposition
   - Root cause: "government" was in the military/enforcement term list, and "public" was in the consumer/civilian term list. Both are too generic — in policy reporting "government" means "federal regulator" (not military apparatus), and "public" means "general populace" (not consumer market)
   - Fix: removed "government" from military/enforcement terms and "public" from consumer/civilian terms in both forward and reverse juxtaposition patterns
   - Verified: legitimate military+consumer and Pentagon+civilian juxtapositions still fire correctly
   - Impact: false positive juxtaposition 1 → 0 in this article

### Manual tone assessment: -0.15 (mildly adversarial)

The article positions Meta as a laggard/holdout using:
- **Isolation framing** ("the only major U.S. developer") — centerpiece device
- **Pressure language** ("pressing," 2x "confidential request") — government as active authority
- **Dense anonymous sourcing** (5 distinct anonymous groups, 3 named sources)
- **Implicit threat via Anthropic section** — even cooperators face consequences ("less than 90 minutes")
- Diplomatic language ("advancing," "leadership," "secure") masks adversarial structure

### Toolkit tone: +0.9856 (VADER)

VADER is wildly wrong (+0.9856 vs manual -0.15). Root cause: diplomatic/policy language scans positive. "Advancing U.S. leadership on robust and secure frontier A.I." reads as strongly positive to VADER but is a corporate damage-control quote. This is a known VADER failure mode for institutional reporting — the sentiment correction system should catch it via isolation_framing + pressure_language adversarial device counts.

### Entity detection notes:
- Anthropic: 7 mentions (most mentioned entity — the cautionary example dominates)
- Meta: 6 mentions (primary subject but fewer mentions than Anthropic)
- Trump: 3 mentions (detected correctly)
- Government entities not in cluster system: CAISI, White House, Commerce Department (partially caught via custom), Biden administration
- Model names not tracked: Muse Spark, Fable 5

### Files modified:
- `mediascope/analyze/framing.py` — 2 new anonymous_authority patterns, juxtaposition fix
- `mediascope/analyze/sentiment.py` — 2 new anonymous source patterns
- `tests/test_nyt_ai_reviews.py` — NEW: 20 tests across 5 classes
- `examples/sample_output/nyt_meta_ai_voluntary_review_2026_06_23_analysis.md` — updated with iteration 2 findings

### Stats:
- Framing devices: 8 → 9 (was 8 with false positive; now 9 without it: +2 anonymous_authority, -1 juxtaposition FP)
- Manual tone: -0.15 (mildly adversarial)
- Toolkit raw VADER: +0.9856 (wrong direction — known VADER limitation)
- Anonymous source detection: 6 → 8 (+2 new patterns)
- Tests: 216 → 236 (+20)
- Commit: `835750e`
- Pushed to GitHub: ✅

---

## 2026-06-24 14:00 PT — Hour Type D: Toolkit Quality & Documentation

**Focus:** Documentation reconciliation — audited all 6 docs + README against actual codebase and fixed systematic drift in framing device counts, journalist counts, and editorial leadership coverage.

### What was improved:

1. **Framing device count reconciliation (20 → 22):**
   - Audited actual `_DEVICE_PATTERNS` dict (19 pattern-based types) + 3 structural post-pass detectors = 22 total
   - Two devices were in code but missing from all documentation:
     - `self_referential_investigation` (pattern-based, 5 patterns): publication citing its own prior reporting as evidence within adversarial coverage, creating a closed feedback loop
     - `speculative_framing` (structural post-pass, 5+ threshold): cumulative conditional language converting possibility into implied inevitability
   - Updated METHODOLOGY.md: Added both devices to their respective tables (Extended Devices + Structural Devices)
   - Updated ARCHITECTURE.md: Changed "20 framing device types" → 22, Extended tier 6→7, Structural tier 2→3

2. **Journalist count reconciliation (17 → 51):**
   - Audited `journalists.yaml`: 51 journalists tracked, 48 with multi-publication careers suitable for migration analysis
   - Updated EDITORIAL_HISTORIES.md from "17 journalists" to "51 journalists" in both Starter Data section and Academic Novelty section
   - README.md already had the correct count (51) from a prior update

3. **Migration table expansion (7 → 16 entries):**
   - Added 9 high-value migration events to EDITORIAL_HISTORIES.md:
     - Mike Isaac: 5-outlet career (Wired→AllThingsD→Forbes→Recode→NYT) — rich decomposition
     - Kashmir Hill: 5-outlet privacy/surveillance career — portable stance test
     - Katie Drummond: 7-outlet career ending as Wired editorial director — highest migration count in dataset
     - Jessica Hamzelou: 13-year New Scientist tenure → MIT TR — deepest institutional encoding test
     - Paresh Dave: Reuters → Wired — wire service objectivity vs editorial culture
     - Johana Bhuiyan: 5-outlet cross-national career — stance portability across national contexts
     - Hibaq Farah: NYT → Guardian — reverse Atlantic crossing
     - Kaitlyn Tiffany: Vox → The Verge → Atlantic — digital-native to legacy adaptation
     - Dell Cameron: 4-outlet investigative security reporter — consistent adversarial posture test

4. **Editorial leadership changes table expansion (5 → 15 entries):**
   - Added 10 entries from the rich `editorial_changes.yaml` data:
     - Wired: Leah Feiger (first-ever politics editor, Nov 2023), Gideon Lichfield (double natural experiment with MIT TR)
     - NYT: Joseph Kahn (exec editor, sued OpenAI), Pui-Wing Tam (tech team architect — recruited Isaac, Frenkel, Hill, Weise, Grant, Mickle), Zach Seward (first AI editorial director)
     - Atlantic: Nicholas Thompson (ex-Wired EIC → Atlantic CEO — direct editorial culture bridge)
     - MIT TR: Gideon Lichfield (investigative shift), Will Douglas Heaven (AI editorial direction)
     - Guardian: OpenAI licensing deal (destroys pure control-case status), Samantha Oltman (4-month tenure departure — editorial resilience test)

### Files modified:
- `docs/METHODOLOGY.md` — 2 new framing device entries
- `docs/ARCHITECTURE.md` — updated counts and tier descriptions
- `docs/EDITORIAL_HISTORIES.md` — journalist count, migration table, leadership table

### Stats:
- Tests: 216/216 passing (no code changes)
- Commit: `3e698df`
- Documentation discrepancies resolved: 4 (framing count ×2, journalist count ×2)

## 2026-06-24 13:00 PT — Hour Type C: Ownership & Funding Deep Dive

**Focus:** MIT Technology Review — selected because its profile had the biggest ownership/funding gap among the 5 tracked publications. Deep research into MIT endowment, CSAIL corporate affiliates, IBM lab expansion, SenseTime sanctions update, iFlyTek partnership, and Project NANDA anti-AI-hype findings.

### What was improved:

1. **MIT endowment corrected and expanded:**
   - Fixed: $27.4B figure is FY2025 (ending June 30, 2025), not FY2024 as previously stated
   - Added: FY2025 investment return 14.8% (vs 8.9% FY2024, -2.9% FY2023)
   - Added: 10-year annualized return 10.7%, $1.57B operating distribution (~5% spending rate)
   - Added: 5th largest US university endowment, largest YoY increase among top-25 (11.4%)
   - Added: Big Beautiful Bill Act endowment tax threat (1.4% → up to 8% starting FY2027)

2. **MIT-IBM Watson AI Lab → MIT-IBM Computing Research Lab:**
   - Renamed to reflect expanded scope (AI + algorithms + quantum computing)
   - Updated stats: 210+ projects, 150+ MIT faculty, 200+ IBM researchers, 1,500+ peer-reviewed articles, 500+ students/postdocs
   - Updated co-directors: Aude Oliva (MIT CSAIL) and David Cox (IBM Research VP)

3. **CSAIL Alliance Program — new corporate affiliates section:**
   - Documented current members: Apple, Microsoft, Qualcomm, Samsung Ventures, Dell EMC, Red Hat, Lenovo, Northrop Grumman, Raytheon Technologies, Mercedes-Benz, Jane Street, Khosla Ventures
   - Apple as CSAIL affiliate is a new previously-undocumented conflict — MIT's parent institution has a direct paid corporate relationship with Apple
   - Added as new known_conflict entry (severity 2)

4. **iFlyTek CSAIL collaboration — new partnership entry:**
   - 5-year collaboration between iFlyTek ("China's Siri") and MIT CSAIL
   - Second Chinese AI company with formal MIT research partnership (alongside SenseTime)
   - Deepens the pattern of MIT ties to Chinese AI/surveillance ecosystem

5. **SenseTime status — comprehensive update:**
   - MIT kept donation but put additional uses "on hold," paused new proposals/fellowships
   - MIT media relations now denies current collaboration (present tense statement)
   - SenseTime added to DoD "Chinese Military Companies" list (2024 NDAA revision)
   - SenseTime pivoted to LLMs, joined China's "Model-Chip Ecosystem Innovation Alliance" alongside Huawei (2025 WAIC)

6. **Project NANDA / "The GenAI Divide" — new institutional research conflict:**
   - MIT researchers found ~95% of organizations saw no measurable financial return from generative AI despite $30-40B enterprise spending
   - Creates tension: MIT's own research says AI underdelivers, but MIT depends on AI industry funding
   - Added as new known_conflict entry (severity 2)

7. **Revenue relationships updated:**
   - Apple: upgraded from "unspecified" to documented CSAIL Alliance membership with source URL
   - IBM: expanded with lab rename, updated stats (210+ projects, 1,500+ papers), new co-directors

### New conflict entries added:
- `csail_corporate_affiliates` (severity 2) — Apple, Microsoft, Qualcomm, Samsung as paying CSAIL members
- `genai_divide_institutional_conflict` (severity 2) — MIT's own anti-AI-hype research vs AI industry funding dependency

### Stats:
- MIT TR known conflicts: 6 → 8 (+33%)
- MIT corporate partnerships documented: 6 → 9 (+50%)
- Source URLs added: 4 new
- Tests: 216/216 passing

---

## 2026-06-24 12:00 PT — Hour Type B: Journalist/Publication Research

**Focus:** MIT Technology Review — massive expansion from 5 to 13 tracked journalists. MIT TR had the thinnest coverage of all 5 publications (only Heikkilä, Knight, Honan, Lichfield, Hao tracked; Knight and Hao migrated away). Identified 8 new journalists via FT partnership press release, staff page, TalkingBizNews, EmTech bios, and fellowship profiles.

### What was improved:

1. **8 new MIT Tech Review journalists added to `journalists.yaml`:**
   - **Will Douglas Heaven** — Senior AI Editor. PhD Computer Science (Imperial). New Scientist → BBC Future Now (founding editor) → MIT TR (Jan 2020). 219+ articles. London-based. Shapes entire AI editorial direction.
   - **James O'Donnell** — Senior AI Reporter. FRONTLINE PBS → MIT TR. Focus: AI in high-stakes domains (police, military, judiciary). National Magazine Award finalist 2026 ('Power Hungry'). 127+ articles.
   - **Casey Crownhart** — Senior Climate Reporter. BS ChemE + Literature (MIT), MA SHERP (NYU). Materials science researcher → freelance → MIT TR (~2022). NatMag Award finalist 2026. 300+ articles (most prolific climate reporter on staff).
   - **Eileen Guo** — Senior Reporter, Features & Investigations. Co-founded Afghanistan's first digital media agency. Ida B. Wells Fellow. IWMF Fellow. Speaks Mandarin, Spanish, limited Persian. Based in LA.
   - **Grace Huckins** — AI Reporter. PhD Neuroscience + Philosophy (Stanford), Rhodes Scholar, Nine Dots Prize 2024/25 ($100K + Cambridge UP book deal), National Academies Schmidt Award 2024. Stanford lecturer. Based in SF.
   - **Rhiannon Williams** — News Reporter. Telegraph → i newspaper → MIT TR (~2022). Writes The Download daily newsletter (941+ posts — most prolific writer on staff). Created AI Hype Index. London-based.
   - **Jessica Hamzelou** — Senior Reporter, Biomedicine. ~13-year New Scientist veteran. Knight Science Journalism Fellow at MIT. KEY MIGRATION: New Scientist → MIT TR. BSc UCL, MSc Imperial. London-based.
   - **Amy Nordrum** — Executive Editor, Operations. IEEE Spectrum → MIT TR (Jul 2020). Controls 10 Breakthrough Technologies, Innovators Under 35, 15 Climate Tech Companies to Watch. BA Ohio, MA SHERP NYU, MBA NYU Stern.

2. **4 new editorial_changes.yaml entries:**
   - Amy Nordrum exec editor appointment (Jul 2020)
   - Will Douglas Heaven AI editor appointment (Jan 2020)
   - MIT TR × FT strategic editorial partnership (Oct 2025)
   - National Magazine Award finalist for Power Hungry investigation (Mar 2026)

3. **Key analytical insights discovered:**
   - **UK-heavy editorial team:** Heaven, Williams, Hamzelou all London-based — unusual for US-headquartered publication, creates transatlantic editorial culture blend
   - **FT partnership creates formal cross-publication coordination** — MIT TR reporters now pair with FT correspondents, blending institutional voices
   - **STEM-to-journalism pipeline:** Crownhart (chemical engineering), Huckins (neuroscience PhD), Heaven (CS PhD) — MIT TR has more PhD-holding reporters than any other tracked publication
   - **Hamzelou's 13-year New Scientist tenure** is a natural experiment for DiD regression: does her reporting tone change between New Scientist and MIT TR?
   - **Rhiannon Williams (941+ posts)** is the most prolific writer across ALL 5 tracked publications — her daily newsletter choices shape reader perceptions more than any feature writer

### Stats:
- MIT TR journalists tracked: 5 → 13 (+160%)
- Total tracked journalists: 43 → 51 (+19%)
- New cross-publication migrations: 1 (Hamzelou: New Scientist → MIT TR)
- Editorial changes added: 4
- Sources cited: 20+ unique URLs
- Files changed: 3 (journalists.yaml +201 lines, editorial_changes.yaml +26 lines, README.md +1/-1)
- Tests: 216 passed (YAML-only changes)
- Commit: `cc18c34`
- Pushed to GitHub: ✅

---

## 2026-06-24 11:00 PT — Hour Type A: Article Deep Dive

**Focus:** Wired — "Meta CTO Andrew Bosworth Admits the Company's AI Reorg Was 'Atrocious'" (~2026-06-16). Manual analysis vs toolkit comparison, with framing pattern fix and 6 new tests.

### What was improved:

1. **Committed prior unstaged work (`ae58a7e`):**
   - self_referential_investigation framing device (21st type)
   - Anchor correction path (Path C) for product reviews with embedded adversarial devices
   - 15 new tests for anchor correction logic

2. **Self-referential investigation — 2 new passive-voice patterns:**
   - Pattern 4 (passive investigative): `VERB by PUBLICATION` — catches "reporting by WIRED," "investigation by The New York Times," "analysis by The Guardian"
   - Pattern 5 (document access): `ACCESS_VERB by PUBLICATION` — catches "seen by WIRED," "obtained by The Guardian," "reviewed by MIT Technology Review," "leaked to WSJ"
   - **Impact:** Bosworth article went from 0 → 3 self_referential_investigation detections, correctly identifying: "seen by WIRED" (×2), "reporting by WIRED" (×1)
   - These passive/document-access constructions are extremely common in Wired and NYT reporting — the existing 3 active-voice patterns missed them entirely

3. **Manual tone assessment: -0.30 vs toolkit -0.66:**
   - Raw VADER: +0.62 — inflated by Bosworth's aspirational management-speak ("personalized attention," "better explaining," "fun and enjoyable," "invest responsibly")
   - These are "damage control" hedges — they read positive to lexicon-based sentiment but function as admission-of-failure language
   - Correction overcorrects from +0.62 → -0.66 (should be ~-0.30)
   - Root cause documented: no "management-speak / damage-control language" detection to moderate correction magnitude

4. **Source analysis gaps documented:**
   - Lede "a top executive told" classified as anonymous — but IS Bosworth, named in the very next sentence. Needs paragraph-level coreference.
   - Anonymous employee who called work "a gulag" — the article's most adversarial source — completely missed by source extractor. Needs attributive construction patterns: `one to describe it as "X"`, `workers described`.
   - Stance balance shows 1.0 (fully supportive) when manual assessment is ~0.0 (balanced). The "gulag" employee is adversarial; Bosworth is self-critical, not supportive.

5. **Framing gaps documented:**
   - "Zuckerberg loyalist" loaded characterization not detected (primes reader to see Bosworth as aligned, not independent)
   - Ironic juxtaposition in kicker (mass layoffs → fix with snacks) not distinguished from generic kicker_framing
   - Selective quotation: choosing "a gulag" as the employee quote over presumably many less inflammatory options

6. **6 new tests in `test_sentiment.py`:**
   - `TestSelfReferentialInvestigationPassive` class: reporting_by_publication, investigation_by_nyt, seen_by_publication, obtained_by_guardian, reviewed_by_mit_tech_review, bosworth_article_full
   - All pass. Full suite: **216 passed**

### Stats:
- Framing device types: 20 → 22 (self_referential_investigation patterns 3 → 5)
- Manual tone: -0.30 (moderately negative)
- Toolkit tone: -0.66 (overcorrected; direction correct, magnitude too aggressive)
- Source analysis: 2 false positives, 1 missed adversarial anonymous source
- Tests: 210 → 216 (+6)
- Commits: `ae58a7e` (prior unstaged work), `2563cd1` (article deep dive + pattern fix)
- Pushed to GitHub: ✅

---

## 2026-06-24 05:00 PT — Hour Type D: Toolkit Quality & Documentation

**Focus:** Massive documentation gap — METHODOLOGY.md documented only 8 of 20 framing device types. Added active-negative agency and tone correction pipeline documentation. Updated README sample gallery and journalist count.

### What was improved:

1. **METHODOLOGY.md §4.1 — Framing Device Taxonomy (8 → 20):**
   - METHODOLOGY.md had not been updated since the original 8 core devices were written
   - Code has evolved through 11+ real-article iterations, adding 12 new device types
   - Reorganized into three tiers: Core (12 pattern-matched), Extended (6 from real articles), Structural (2 post-pass)
   - Extended devices documented with the source article that motivated each addition
   - New types: straw_man, refusal_amplification, juxtaposition, timeline_implication, military_techno_optimism, selective_rehabilitation, rhetorical_question, ironic_quotation, isolation_framing, pressure_language, kicker_framing, analogy_stacking

2. **METHODOLOGY.md §5.2 — Anonymous Source Scoring:**
   - Documented counted anonymous source patterns ("two employees said," "three people familiar")
   - Documented no-comment signal exclusion (source_type="no_comment" filtered from counts)
   - Both discovered through NYT Meta Arena and voluntary review article analyses

3. **METHODOLOGY.md §8-9 — New sections:**
   - §8: Active-Negative Agency Detection — verb categories (surveillance/extraction, workforce harm, coercion), impact on tone correction
   - §9: Framing-Aware Tone Correction — VADER positive-bias problem, correction activation conditions (3+ adversarial devices, agency ≤ -0.3, positive raw VADER), headline framing override, security context adjustment
   - These were the toolkit's most impactful analytical improvements with zero methodology documentation

4. **METHODOLOGY.md — Section renumbering:**
   - Renumbered §§8-11 → §§10-13 to accommodate new sections. 13 sections total now.

5. **ARCHITECTURE.md — framing.py section:**
   - Updated from "Eight framing device types" to "20 framing device types" with tier breakdown
   - Added kicker_framing and analogy_stacking post-pass descriptions

6. **ARCHITECTURE.md — sources.py section:**
   - Added counted anonymous source detection documentation
   - Added no-comment signal tagging documentation

7. **README.md — Sample Output Gallery:**
   - Added 8 missing sample analyses: atlantic_meta_ai_slop_vibes, mit_tr_llms_mass_surveillance, mit_tr_meta_ai_security_hack, wired_meta_dark_mood, wired_meta_horizon_worlds_comedy_club, wired_meta_mci_data_exposure, wired_meta_nametag_removal, wired_meta_rayban_creep
   - Gallery now lists all 19 annotated analyses

8. **README.md — Journalist count:**
   - Updated from 17 to 43 tracked journalists

### Stats:
- Files changed: 3 (METHODOLOGY.md, ARCHITECTURE.md, README.md)
- Lines: +117, -16
- New METHODOLOGY.md sections: 2 (§8 Active-Negative Agency, §9 Framing-Aware Tone Correction)
- Framing devices documented: 8 → 20 (+150%)
- Sample analyses documented in README: 11 → 19 (+73%)
- Tests: 202 passing (documentation-only, no code changes)
- Commit: `fa09204`

---

## 2026-06-24 04:00 PT — Hour Type C: Ownership & Funding Deep Dive

**Focus:** The Atlantic / Emerson Collective — expanded ownership chain, investment portfolio, corporate structure, and financial conflicts. Committed as `a887d94`.

### What was improved:

1. **MAJOR FINDING — io Products / OpenAI exit (severity 5):**
   - Emerson Collective was a founding backer of io Products (Jony Ive's AI hardware startup), which OpenAI acquired for $6.5 BILLION in 2025 — OpenAI's largest acquisition ever
   - Other backers: Thrive Capital, SV Angel, Sutter Hill Ventures. ~55 employees. $5B equity + $1.5B from prior 23% stake
   - This creates a COMPOUND financial relationship: EC receives licensing revenue from OpenAI (since May 2024) AND realized a capital gain from OpenAI via the io exit
   - No other tracked publication has an owner that both licenses content to AND has an equity exit through the same AI company
   - Also creates Apple tension: LPJ holds $16B+ Apple stock, but io Products was designed to compete with Apple
   - Sources: PitchBook, TechCrunch, The Information, Bloomberg, thehindubusinessline.com

2. **Emerson Collective LLC structure documented:**
   - EC is an LLC (not a 501(c)(3) nonprofit) — deliberate legal choice for flexibility
   - The LLC is owned by the Emerson Collective Foundation (a 501(c)(3))
   - Foundation operates Waverley Street Foundation as philanthropic arm (~$2.74B assets, May 2026)
   - LLC-inside-foundation structure shields for-profit investments from public 990 disclosure
   - Inside Philanthropy named LPJ "Least Transparent Mega-Giver" of 2019
   - Sources: InfluenceWatch, Devex, ProPublica Nonprofit Explorer

3. **Expanded investment portfolio (8 new entries):**
   - io Products (Jony Ive, acquired by OpenAI $6.5B)
   - Commonwealth Fusion Systems (2021, fusion)
   - Boom Supersonic (2019, aerospace)
   - Gimlet Media (2017, exited via Spotify ~$230M)
   - Midi Health (2024, $60M Series B lead)
   - Teal Health (2025, $10M seed, cancer screening device)
   - Amplify (2015, edtech)
   - Axios updated: exited 2022 when sold to Cox Enterprises for $525M
   - Sources: Wikipedia (Emerson Collective article), PitchBook

4. **Reed Jobs / Yosemite spinoff:**
   - Cancer-focused VC spun out of EC in Aug 2023
   - Fund I: $263M. Fund II: target $350M, raised $200M+
   - ~20 portfolio companies (Tune Therapeutics, Chai Discovery)
   - LPs: MIT, Memorial Sloan Kettering, Amgen, John Doerr
   - CROSS-PUBLICATION LINK: MIT is both a Yosemite LP and parent of MIT Technology Review
   - Sources: TechCrunch, Forbes India, Milken Institute bio, DealBook

5. **Waverley Street Foundation grants:**
   - $2.74B in assets (May 2026)
   - Major grants: Climate Imperative Foundation ($36M x2, $18M x4), Conservation International ($21M), Thousand Currents ($20M), European Climate Foundation ($10M x2)
   - Source: InfluenceWatch, Instrumentl

6. **Atlantic business metrics updated:**
   - 1.4M+ subscribers (Feb 2026, up from 1M+ mid-2024)
   - Revenue over $100M, profitable since March 2024
   - 15% subscriber growth YoY, 70%+ retention rate
   - 3 tiers: Digital $79.99, Print+Digital $89.99, Premium $120
   - Chief Growth Officer: Megha Garibaldi
   - Sources: Press Gazette podcast, WAN-IFRA, pugpig.com, Editor & Publisher

7. **Apple stock price updated:** AAPL at $294.30/share (Jun 24, 2026), market cap ~$4.37T

8. **New conflict types added:**
   - `investment_exit` (severity 5): io Products/OpenAI compound relationship
   - `transparency` (severity 3): LLC structure opacity problem
   - `cross_publication_link` (severity 1): Yosemite/MIT LP relationship

### Stats:
- Profile expanded by 275 lines (16 removed, 275 added)
- New investment entries: 8
- New conflict types: 3
- Severity-5 conflict discovered: io Products / OpenAI exit
- Date corrections: 0
- Tests: 202 passing, YAML validated
- Sources cited: 15+ unique URLs
- Commit: `a887d94`

---

## 2026-06-24 03:00 PT — Hour Type B: Journalist Career Research

**Focus:** Expand career histories for 5 journalists across 3 publications (Wired, Atlantic, Guardian). Committed prior unstaged work (Alex Hern + Dan Milmo expansions), then deep-researched Steven Levy, Adrienne LaFrance, and Ian Bogost.

### What was improved:

1. **Committed prior unstaged work (Alex Hern + Dan Milmo):**
   - Alex Hern: Expanded from 2 entries to 6 (Left Foot Forward → New Statesman → Guardian reporter → features writer → senior correspondent → Economist AI Writer). KEY MIGRATION: Guardian → Economist (Oct 2024), 11-year Guardian veteran. Won Technology Journalist of the Year 2020. Founded TechScape newsletter.
   - Dan Milmo: Expanded from 2 entries to 4 (Guardian trainee → transport correspondent → deputy business editor → global technology editor). Unusual transport-to-tech beat change.
   - Sources: speakout.uk, theguardian.com/profile, xriskobservatory.org, various LinkedIn/press profiles
   - Commit: `a7f53f3`

2. **Steven Levy (Wired) — expanded from 2 to 7 entries:**
   - Full career arc: freelance (Rolling Stone, Esquire, 1975–1983) → Newsweek senior editor (1984–2008, 24 years) → Wired senior staff writer (2008–2014) → founded Backchannel on Medium (2014) → Condé Nast acquired Backchannel (Jun 2016) → Backchannel editor at Wired (2016–2017) → editor at large (2017–present)
   - Critical insight: Levy has been at Wired since its 1993 founding (as contributing writer), making him the longest-tenured writer. His 50-year career arc from Rolling Stone counterculture to Condé Nast editor at large is unique.
   - Sources: ubiquity.acm.org, edge.org/memberbio, computerhistory.org, digiday.com, mnacritique.mergersindia.com, wired.com/author

3. **Adrienne LaFrance (Atlantic) — expanded from 2 to 10 entries:**
   - Full pre-Atlantic career: WBUR (Boston NPR) → Hawaii Public Radio → Honolulu Weekly managing editor → Honolulu Civil Beat (ran DC bureau for Omidyar's nonprofit) → Nieman Journalism Lab (Harvard) → Digital First Media / Project Thunderdome
   - Atlantic career expanded: staff writer (2014) → editor of TheAtlantic.com (2017) → executive editor (May 2019, first woman in 162-year history)
   - **DATE CORRECTION:** Promotion to executive editor was May 2019, not "2021-01" as previously listed. Confirmed via FIPP, Wikipedia, and multiple sources.
   - Key work: "The Prophecies of Q" (Jun 2020 cover), "Facebook Is a Doomsday Machine" (Dec 2020)
   - Sources: chqdaily.com, fipp.com, niemanlab.org, theatlantic.com/author, en.wikipedia.org

4. **Ian Bogost (Atlantic) — expanded from 1 to 6 entries:**
   - Pre-journalism career: software engineer at US Interactive (1997) → CTO at Media Revolution / Hans Zimmer's media group → founded Persuasive Games LLC (2003)
   - Academic career: Georgia Tech Ivan Allen College Distinguished Chair (2004–2021) → WashU Barbara and David Thomas Distinguished Professor (2021–present, directs Film & Media Studies)
   - **DATE CORRECTION:** Atlantic contributing editor since 2013, not 2017 as previously listed. Confirmed via bogost.com and Atlantic author page.
   - Rare pipeline: tech industry → academia (PhD Comparative Literature, not CS) → journalism. Humanities lens on technology is distinctive among tech writers.
   - 11 books including Racing the Beam (2009), Alien Phenomenology (2012)
   - Sources: bogost.com, engineering.washu.edu, edge.org/memberbio, theatlantic.com/author

### Stats:
- Journalist entries expanded: 5 (Hern 2→6, Milmo 2→4, Levy 2→7, LaFrance 2→10, Bogost 1→6)
- Total new career entries added: 27
- Date corrections: 2 (LaFrance exec editor 2021→2019, Bogost Atlantic start 2017→2013)
- Tests: 202 passing
- Sources cited: 20+ unique URLs across all expansions

---

## 2026-06-23 17:00 PT — Hour Type D: Documentation + Source Extractor Improvements

**Focus:** Fix incorrect import paths in docs, add missing function calling schemas, update examples to demonstrate newer features, analyze the NYT Arena article (missing analysis), and fix a critical source extraction blind spot discovered during analysis.

### What was improved:

1. **Fixed incorrect import path in AGENT_GUIDE.md:**
   - `measure_outsourced_intensity` was listed as importing from `mediascope.analyze.sources` but actually lives in `mediascope.analyze.sentiment`
   - `detect_power_asymmetry` was listed as a standalone function but is actually a framing device type detected by `detect_framing_devices` in `mediascope.analyze.framing`
   - Any agent following the AGENT_GUIDE would have gotten ImportError on these

2. **Added missing function calling schemas to AGENT_GUIDE.md:**
   - `analyze_source_stance`: JSON schema with article_text, target_entity parameters
   - `measure_outsourced_intensity`: JSON schema with article_text parameter and note about correct module location
   - These features were documented in README and METHODOLOGY but had no agent-callable schemas

3. **Updated examples/quick_start.py:**
   - Added source stance analysis (adversarial/supportive/neutral counts, stance_balance)
   - Added outsourced intensity demonstration (outsourced_ratio, editorial vs quoted intensity)
   - Previously only showed sentiment and entities — newer features were undocumented in examples

4. **Updated examples/full_pipeline.py:**
   - Fixed imports: added `analyze_source_stance` from sources, `measure_outsourced_intensity` from sentiment
   - Added stance and outsourced_intensity to per-article analysis dict
   - Added Source Stance Summary output section: avg stance balance, total adversarial/supportive counts, avg outsourced intensity across target-entity articles

5. **Created NYT Arena prediction markets analysis (new article):**
   - File: `examples/sample_output/nyt_meta_prediction_markets_arena_2026_06_23_analysis.md`
   - Article reconstructed from 5 secondary sources (Reuters, NY Post, IBD, Engadget, CNN)
   - Manual tone assessment: -0.10 (near-neutral business scoop)
   - **KEY FINDING:** Toolkit was completely blind to counted-anonymous source patterns — "two employees with knowledge of the matter" and "one person familiar with the plans" were not detected, causing 100% anonymous sourcing to read as 0%
   - Cross-publication comparison of same event, same day: Engadget (-0.70) vs Reuters (+0.05) — quantifies how editorial culture drives coverage asymmetry independent of financial conflicts

6. **Source extractor improvements (mediascope/analyze/sources.py):**
   - Added "X employees/people with knowledge of" pattern — catches "two employees with knowledge of the matter" and similar constructions common in NYT/WSJ product-leak scoops
   - Added singular "one person/employee familiar with" pattern — catches "one person familiar with the plans" and similar
   - Added no-comment detection: "did not immediately respond to a request for comment," "declined to comment," and variants — meaningful editorial signal that the entity chose not to provide its side

7. **6 new tests (tests/test_source_stance.py):**
   - `TestCountedAnonymousSources` class: employees_with_knowledge, one_person_familiar, three_people_said, no_comment_detection, nyt_arena_full_article (integration), declined_to_comment_variant
   - All 6 pass. Full suite: **179 passed** (up from 173)

8. **Updated README.md:** Added NYT Arena article to Sample Output Gallery

### Commit: `1509e6a`
### Pushed to GitHub: ✅

## 2026-06-23 16:00 PT — Hour Type C: Wired/Condé Nast/Advance Publications Ownership & Funding Deep Dive

**Focus:** Comprehensive ownership chain, investment portfolio, financial data, and conflict-of-interest analysis for Wired's parent companies. This is the most critical publication in the 5-pub set for Ray's research, yet its profile had the thinnest ownership data. Now massively expanded.

### What was improved:

1. **MAJOR FINDING — Donald Newhouse died May 26, 2026 (aged 96, lymphoma):**
   - Last surviving second-generation Newhouse
   - Forbes net worth at death: $15.4B
   - Third generation now fully in control for the first time
   - Steven O. Newhouse (chairman/co-president) is the key figure: sits on Advance board, Reddit board (as Advance Designee)
   - Advance Publications board identified from Reddit proxy: Michael A. Newhouse, Steven O. Newhouse, Samuel I. Newhouse III, Thomas S. Summer, Victor F. Ganzi
   - Michael Andrew Newhouse on AP (Associated Press) board since 2017
   - Family office: 35 adult households, 100+ family members
   - CIO: Bei Saville (from Northern Trust Asset Management OCIO division)
   - Source: Wikipedia (with NYT obituary citation), Institutional Investor

2. **Advance Publications full investment portfolio with current valuations:**
   - **Reddit (RDDT):** 42.2M shares Class B + 16K Class A = 33.5% voting power. ~$7.0B at $165.63/share. 2 board seats (Steven O. Newhouse, Robert A. Sauerberg) + 1 observer. Board expansion veto >10 members. Huffman holds irrevocable proxy on Advance shares. Original $10M investment (5,800%+ return). Sources: SEC Exhibit 2 (Voting Agreement), Reddit proxy, TheWrap, Bloomberg
   - **Charter Communications (CHTR):** ~20.6M shares, 12.3% of Class A. ~$2.7B at $131.75/share. Complex multi-entity structure (A/N, NBCo, API, NFH, Advance Long-Term Trust). A/N grants 6% vote proxy to Liberty Broadband. From Bright House Networks merger (2016). Sources: SEC Schedule 13D/A (Oct 2023)
   - **Warner Bros. Discovery (WBD):** ~98M shares remaining (~4%), ~$2.6B at $26.88/share. Originally 198.18M shares (~8.1%). Newhouse resigned from WBD board Mar 2024. Sold 100M shares Jun 2024 at $10.97 for $1.1B (now worth $2.7B — $1.6B opportunity cost). Sources: SEC Schedule 13D/A (Apr 2024), Bethel Clarion
   - **Other holdings:** ACBJ (43 local business papers, 500+ journalists), Leaders Group (Sports Business Journal, Newzoo), IRONMAN Group (acquired 2020), Turnitin, Brightspot CMS, regional newspapers (~12 titles)
   - **Total public equity: ~$12.3B+** (before private holdings)

3. **Revenue relationships — all three AI deals fully sourced:**
   - **OpenAI:** Multi-year, announced Aug 20, 2024. ChatGPT + SearchGPT. Lynch memo to staff quoted. Sources: Condé Nast press release, SiliconAngle, Adweek, TheWrap, Decrypt
   - **Amazon Rufus:** Multi-year, announced Jul 10, 2025. Shopping assistant content licensing. Commerce angle. Sources: Digiday (original), Engadget, Glossy, The Decoder, AdExchanger
   - **Apple Intelligence:** Negotiations reported 2024-2025, ~$50M+ archive access. No formal announcement yet.
   - **Meta: $0.** NO revenue relationship. The only major tech company not paying. This is the most important data point.

4. **Condé Nast financial data and restructuring timeline (8 events, 2024-2026):**
   - UK subsidiary: £244.8M turnover FY2023, £8.3M pre-tax profit (collapsed from £23.3M). Source: Companies House via Business Live
   - Lynch memo (Apr 2026): Profitable in 2025 with revenue growth continuing into Q1 2026
   - 7 marquee brands = 85% of revenue (FT, Feb 2026): Vogue, GQ, New Yorker, Wired, VF, AD, CN Traveler
   - Restructuring: Pitchfork→GQ (2024), 270 layoffs (Nov 2024), C-suite cuts (Jan 2025, 14+ execs), Wintour steps down as EIC (2025), Teen Vogue→Vogue (2025), Them sold (Feb 2026), Self shut down (Apr 2026), Wired Italy ending, Glamour Germany/Spain/Mexico closing, 16 unionized layoffs (Apr 2026)
   - CRO Elizabeth Herbst-Brady (joined Aug 2024) driving cost restructuring

5. **Known conflicts expanded from 3 to 5 entries:**
   - Investment (Reddit): Upgraded with $7B valuation, board seat details, voting agreement
   - Investment (WBD): NEW — ~$2.6B remaining, streaming/content competition with Meta
   - Revenue: Upgraded with all three AI deal details and the $0 Meta relationship
   - Competitive: Upgraded with Reddit FY2025 revenue data
   - Succession risk: NEW — Donald Newhouse death, third generation transition, 100+ family members

### Key analytical insights:

1. **The $7B Reddit conflict is larger than previously documented:** At $165.63/share, Advance's Reddit stake is worth ~$7.0B — triple the $2B IPO gain originally noted. This is by far the largest single asset in Advance's portfolio. Every negative Meta story potentially benefits Reddit's competitive position and therefore this $7B stake.

2. **The "revenue asymmetry" is now fully sourced:** Condé Nast has multi-year deals with OpenAI (Aug 2024), Amazon (Jul 2025), and Apple (in negotiations). All are Meta competitors. Meta pays $0. The structural incentive is clear: companies paying Condé Nast get partnerships; Meta gets adversarial coverage from a publication whose parent's $7B investment benefits from Meta's struggles.

3. **Donald Newhouse's death creates succession uncertainty:** The last second-generation patriarch died May 26, 2026. Steven O. Newhouse (third gen) now leads, but the family office spans 100+ people across 35 households. Estate settlements, tax events, or strategic realignment could alter Advance's media and investment posture.

4. **Advance's total public equity portfolio (~$12.3B+) creates multiple potential conflicts:** It's not just Reddit. WBD ($2.6B) competes with Meta in streaming. Charter ($2.7B) is in the content distribution chain. These cross-holdings create a web of incentives that standard editorial conflict disclosures don't capture.

5. **The Wired Italy closure coincides with profit pressure:** Condé Nast's UK profits fell 64% (£23.3M→£8.3M) on flat revenue. The parent is "profitable" but under visible cost pressure, making the AI licensing deals (OpenAI, Amazon) increasingly important revenue diversification — and making the absence of a Meta deal more consequential.

### Commit: (pending push)
### Sources: SEC EDGAR (Schedule 13D filings for Charter, WBD, Reddit), Reddit DEF 14A proxy (2025), Wikipedia, Companies House (UK), TheWrap, Adweek, Digiday, Engadget, SiliconAngle, Business Live (City AM), Institutional Investor, Bloomberg Billionaires Index, FT (paywalled, referenced via TheWrap), Status.news, Fashionista, MediaPost, SPMG Media

## 2026-06-23 15:00 PT — Hour Type B: NYT Tech Desk Deep Dive — 8 Journalist Career Histories

**Focus:** Comprehensive career research on the New York Times tech desk — the LARGEST gap remaining in the journalist tracking database. 6 key reporters listed in the NYT profile had zero career histories; Mike Isaac's entry was minimal (2 positions). This iteration fills the entire NYT tech desk.

### What was improved:

1. **Mike Isaac — EXPANDED (2 entries → 5 career entries):**
   - Added Forbes contributor (2009-2010): music journalism roots (Paste Magazine, Performer Magazine)
   - Added Wired staff writer (2010-2012): mobile/Google beat, editor was Brian X. Chen (now NYT). KEY: First position in Condé Nast/Advance Publications orbit
   - Split AllThingsD (2012-2013, hired by Kara Swisher/Walt Mossberg) and Re/code (2014) as separate entries
   - Massively expanded NYT entry (2014-present): Gerald Loeb Award details, Super Pumped (W.W. Norton 2019, NYT/WSJ bestseller), Showtime series (2022, JGL, cameo), MSNBC contract, 2018 Facebook team Loeb Award, covered Meta metaverse/AI race/Musk Twitter/OpenAI crisis. 12+ year tenure — longest-serving current NYT tech reporter
   - Education: UC Berkeley 2010, English Literature. From Fort Worth, TX

2. **Sheera Frenkel — NEW (5 career entries):**
   - McClatchy foreign correspondent (2005-2009): Middle East, Arab Spring, Iran nuclear, Syria. Hebrew fluent, conversational Arabic
   - NPR correspondent (2009-2012): continued Middle East coverage
   - Times of London (2012-2015): final foreign correspondent role
   - BuzzFeed News (2015-2017): originated cybersecurity beat, profiled Fancy Bear, ISIS internet use, Myanmar. CAREER PIVOT: foreign correspondent → cybersecurity
   - NYT (2017-present): hired by Ellen Pollock and Pui-Wing Tam alongside Nicole Perlroth. 2018 "Delay, Deny and Deflect" Facebook exposé (6 months, 50+ interviews). Awards: Pulitzer finalist 2019, George Polk, Gerald Loeb, Mirror Award 2022. Co-wrote "An Ugly Truth" (2021) — NYT/international bestseller. Education: Boston University
   - Analytical insight: foreign correspondent framing toolkit (covert actors, hidden motivations, institutional deception) maps directly onto Big Tech coverage

3. **Kashmir Hill — NEW (5 career entries):**
   - Above the Law blogger (2008-2009): first journalism role, legal news
   - Forbes writer/editor (2010-2014): 4-year tenure, started "Not-So Private Parts" blog (pioneered privacy reporting genre), Bitcoin week experiment (viral), Google Plus pressure story (Google hired PIs). SABEW innovation award
   - Fusion editor (2014-2017): editor of "Real Future" tech vertical. Overlap period with Kevin Roose (VP/co-EP of Real Future TV)
   - Gizmodo investigative reporter (2017-2019): Special Projects Desk. "Goodbye Big Five" experiment (cut off all 5 major tech companies). Experimental journalism
   - NYT enterprise reporter (2019-present): Clearview AI investigation (Jan 2020) changed facial recognition policy nationwide. "Your Face Belongs to Us" (Random House 2023) — FT Best Books 2023 Technology, Royal Society Trivedi Science Book Prize shortlist 2024. Mar 2024: exposed GM/Honda/Kia/Hyundai sharing driver data with LexisNexis — GM ended practice in 11 days. Born March 5, 1981. Partner: Trevor Timm (FPF co-founder). Education: Duke BA, NYU MA Magazine Journalism

4. **Kevin Roose — NEW (4 career entries):**
   - NYT finance reporter (2011-2012): first NYT stint, ~1 year covering Wall Street. Straight from Brown University
   - New York Magazine lead business writer (2012-2014): Daily Intel blog, Silicon Valley coverage. Published "Young Money" (2014, NYT bestseller)
   - Fusion senior editor/VP (2014-2017): VP overseeing editorial projects and strategy. Co-executive producer of "Real Future" TV. NOTE: Kashmir Hill also at Fusion during this period
   - NYT columnist (2017-present): second stint. "The Shift" column. Created "Rabbit Hole" podcast (2020, internet radicalization). Co-hosts "Hard Fork" with Casey Newton. Feb 2023: viral Bing/Sydney conversation. "Futureproof" (2021). Writing "The AGI Chronicles" (coming 2026). Forbes 30 Under 30. 2018 Gerald Loeb team award. Lives in Oakland, CA

5. **Karen Weise — NEW (3 career entries):**
   - ProPublica intern (2009): early career. Previously public radio (SoCal), briefly management consultant
   - Bloomberg Businessweek/News (2010-2018): long tenure. Started in NYC (policy, consumer finance, housing), moved to Seattle for tech. Won SABEW for 2015 Dan Price/Gravity Payments exposé. Ellen Pollock was top editor at Businessweek when the story ran
   - NYT Seattle tech correspondent (2018-present): covers Amazon, Microsoft, richest people. CONFLICT ANGLE: covers Amazon, which pays NYT $20-25M/yr in AI licensing since May 2025. Testable hypothesis: does Amazon coverage tone shift post-deal? Education: Yale, UC Berkeley J-School

6. **Tripp Mickle — NEW (2 career entries):**
   - Wall Street Journal (2014-2022): 8 years covering Apple, Google. Previously sportswriter. Broke Jony Ive departure, Tim Cook/Trump relationship
   - NYT Apple reporter (2022-present): hired with Nico Grant. "After Steve" (William Morrow, May 2022) — 200+ interviews, thesis: Apple lost its soul under Cook. WSJ → NYT migration for Apple beat

7. **Nico Grant — NEW, DEPARTED (2 career entries):**
   - Bloomberg (2019-2022): enterprise tech → Google beat (early 2021). Broke discrimination/harassment in Google ethical AI group, mental health toll stories. Born in Trinidad, raised in NYC. Hunter College, CUNY MS
   - NYT (2022-2025): Google/Alphabet. DEPARTED: "Working there was a dream come true, but now, it's time to chase other dreams outside of journalism." Creates gap on NYT Google/AI beat

8. **Eli Tan — NEW (1 entry):**
   - NYT (2026-present): promoted from fellowship to Meta beat reporter. Second dedicated Meta reporter alongside Mike Isaac. Editor: Jim Kerstetter. Covered data centers, AI dating, AI and pastors during fellowship. "A knack for telling stories that make us understand technology's impact on regular people"

### NYT Profile updates (nytimes.yaml):
- key_journalists expanded: 8 → 11 entries with full career context, books, awards, known patterns
- Added notable_departures section: Nico Grant (left journalism 2025), Nicole Perlroth (to CISA 2021)
- Added CONFLICT NOTE on Karen Weise covering Amazon (NYT's $20-25M/yr licensing partner)

### Editorial changes (editorial_changes.yaml) — 4 new NYT entries:
- Pui-Wing Tam: technology editor (2015) — built the entire NYT tech team
- Zach Seward: editorial director of AI initiatives (2024) — first role of its kind
- Eli Tan: Meta reporter hire (2026) — second dedicated Meta reporter
- Nico Grant: Google reporter departure (2025) — gap on Google beat

### Key analytical discoveries:

1. **The Pui-Wing Tam pipeline:** Nearly every major NYT tech reporter was hired by Tam (joined 2015 from Bloomberg). She is the single most important architect of NYT's tech coverage posture — her hiring choices determine whose editorial DNA enters the newsroom. Previously at WSJ where HP hired PIs to surveil her phone records.

2. **The Fusion connection:** Kevin Roose AND Kashmir Hill both worked at Fusion during 2014-2017. Roose was VP/co-EP of Real Future (TV); Hill was editor of Real Future (web). This shared institutional experience at a young, experimental outlet may create editorial affinity at NYT.

3. **The 'Ugly Truth' / 'Super Pumped' parallel:** NYT's two primary Meta-adjacent reporters (Frenkel and Isaac) both wrote adversarial bestsellers about their beat companies. Book-writing creates a financial incentive to maintain adversarial framing — their expertise is marketable precisely because they are adversarial.

4. **The foreign correspondent → tech pipeline:** Frenkel's decade in the Middle East gave her a framing toolkit (hidden actors, institutional deception, covert operations) that maps directly onto tech coverage. Compare: Drummond's adversarial journalism at Wired, but with war-correspondent credibility.

5. **Karen Weise's Amazon conflict:** She covers Amazon, which pays NYT $20-25M/yr in AI licensing since May 2025. Most direct testable revenue/coverage conflict on the NYT tech desk.

### Commit: `b9ec6c0`
### Tests: 173/173 passing
### Files modified: 3 core (journalists.yaml +239 lines, nytimes.yaml +53/-27 lines, editorial_changes.yaml +24 lines)
### Sources: nytco.com (×7 staff announcements), Poynter (×2), Talking Biz News (×8), AllThingsD (×2), Adweek, Editor & Publisher, HarperCollins, Penguin Random House, kevinroose.com, Princeton ISC, FedSoc, USENIX, Jewish Journal, NPR, University of Colorado, University of Michigan, Goodreads, MacRumors, BuzzSumo

## 2026-06-22 21:00 PT — Hour Type D: Toolkit Quality & Documentation Overhaul

**Focus:** Systematic audit of all 6 documentation files against the actual codebase. Found 5 issues across 4 files — stale content, missing modules, broken numbering, and absent CLI documentation for the careers subsystem.

### What was improved:

1. **ARCHITECTURE.md — Complete rewrite (+251 lines):**
   - **careers/ module documented:** All 5 files (models.py, tracker.py, migrations.py, editorial_leadership.py, influence.py) with detailed descriptions of data models, algorithms, and API
   - **sources.py analysis layer expanded:** Source stance analysis, outsourced intensity detection, and power asymmetry framing now documented with module-level detail
   - **New: Sentiment Correction Pipeline diagram:** Shows the multi-layer flow from raw VADER/TextBlob scores → framing device detection → active-negative agency check → framing-aware tone correction → corrected composite score. Documents the specific failure mode this solves (VADER positive-bias on measured editorial prose)
   - **New: Editorial Histories Pipeline diagram:** Career Tracker → Migration Detection → Source-Side DiD / Portable Bias / Dest-Side DiD → Bias Decomposition / Leadership ITS
   - **New: Analyze Layer Module Detail section:** Every module in `mediascope/analyze/` documented with features including active-negative agency detection, security context adjustment, appositive source extraction, source stop-word filtering, workplace coercion language, investment-near-layoffs juxtaposition
   - **New: Careers Layer Module Detail section:** All 5 careers modules documented with algorithms (DiD + Huber-White robust SEs, ITS segmented regression, two-way ANOVA decomposition, portable bias scoring)
   - **New: Complete File Layout tree:** Actual filesystem structure reflecting all modules, profiles (including careers/), docs, examples, and tests
   - **New: Extension Points:** Custom framing devices and custom source stance terms sections
   - **Configuration section expanded:** Added career data YAML paths (journalists.yaml, editorial_changes.yaml)
   - **Storage tables updated:** Added framing_results, source_analyses tables; noted raw+corrected sentiment scores

2. **METHODOLOGY.md — Section numbering fix (9 edits):**
   - §8 "Quality Control" subsections were numbered 6.1/6.2 → corrected to 8.1/8.2
   - §11 "Causal Identification Through Journalist Migration Analysis" subsections were numbered 9.1-9.7 → corrected to 11.1-11.7
   - Root cause: sections were added incrementally across multiple iterations without renumbering. §§6-7 (Source Stance Analysis, Outsourced Intensity) were inserted before what was originally §6 Quality Control, pushing it to §8 without updating its internal numbering

3. **README.md — Two updates:**
   - **Guardian reclassification:** Publication profiles table updated from "Control case" / "Pure editorial bias, no financial conflicts" → "Partial control" / "OpenAI + ProRata licensing deals, but no equity in specific competitors. Closest to baseline in the 5-pub set (pre-Feb 2025 coverage cleaner)." This aligns the README with the Type C iteration that discovered the OpenAI licensing deal and reclassified the Guardian
   - **Sample output gallery:** Added MIT TR Anduril article entry (Tone: -0.10 manual/+0.64 toolkit, VADER positive-bias failure mode, 0 anonymous sources, Microsoft IVAS $22B comparison frame). The article + analysis pair existed on disk since the earlier analysis but was not listed in the gallery

4. **AGENT_GUIDE.md — Careers CLI documentation (+240 lines):**
   - **6 new CLI command docs:** `mediascope careers list`, `show`, `migrations`, `leadership`, `diff`, `analyze` — each with syntax, input/output descriptions, and usage examples including option flags
   - **4 new function calling schemas:** `careers_diff` (journalist_name, window_days, target_entity), `careers_analyze` (journalist_name), `careers_list`, `careers_migrations` (from_pub, to_pub) — JSON schemas matching the existing OpenAI/Anthropic format used for analyze_publication and generate_disclosure
   - **Python API imports expanded:** Added `analyze_source_stance`, `measure_outsourced_intensity`, `detect_power_asymmetry` from sources.py; added `CareerTracker`, `MigrationAnalyzer`, `LeadershipAnalyzer`, `InfluenceScorer` from careers/
   - **2 new JSON output format examples:** Source stance output (stance_balance, outsourced_intensity, power_asymmetry) and DiD analysis output (did_estimate, p-value, portable_bias_estimate)
   - **Agent prompts updated:** General-purpose prompt expanded with 4 careers workflow steps; research agent prompt updated to mention framing correction, source stance analysis, and DiD caveats

### Also committed (from prior Type C iteration that failed to push):
- Guardian profile expansion: Scott Trust board (14 members), STEL board (7), FY2024-25/2023-24 financials, OpenAI/ProRata deals, GMG Ventures/Mercuri, SPUR coalition, 4 ownership changes, 5 editorial changes entries

### Tests: 134/134 passing

### Commits:
- `3e8a03d` — Type C: Guardian ownership deep dive (previously uncommitted)
- `dc2078e` — Type D: Documentation overhaul (this iteration)

---

## 2026-06-22 20:00 PT — Hour Type C: Guardian Ownership & Funding Deep Dive

**Focus:** Complete structural mapping of The Guardian's ownership chain, governance boards, financial data, AI licensing deals, venture capital arm, and industry coalition memberships. Critical reappraisal of Guardian's role as "control case" in the MediaScope framework.

### What was improved:

1. **Guardian profile (`profiles/guardian.yaml`) — massive expansion (+249 lines, near-complete rewrite):**
   - **Ownership chain overhauled:** 4 entities → 5 (added Scott Trust Endowment Ltd as distinct entity). Each entry rewritten with precise operational descriptions. GNM (operating company) distinguished from GMG (parent company).
   - **Scott Trust board fully mapped (14 members):** First complete board listing with roles, backgrounds, and source URLs. Key discovery: **Vivian Schiller** — former Twitter Global Chair of News (Meta competitor), NPR CEO, NYTimes.com GM, now Aspen Institute + Thomson Reuters Foundation board. Significant tech-media connections.
   - **Scott Trust Endowment board fully mapped (7 members):** Tracy Corrigan (chair), Jonathan Evans (CIO), and 5 directors. Source: STEL 2024-25 performance report.
   - **STEL financials:** £1,245.6M value (March 2025), 10-year return 6.3% (below 8.2% target), diversified across PE/VC (£276M NAV, £352M committed across 28 managers), public equity, emerging markets, hedge funds, credit, gold, bonds. Source: official STEL report.
   - **FY2024-25 financials added:** £275M record revenue (+6.7%), digital reader revenue £100M+ (20%+ growth), 1.3M recurring digital supporters, operating loss below £25M. Source: Tomorrow's Publisher.
   - **FY2023-24 financials added:** £257.8M revenue (-2.5%), digital reader revenue £88.2M (+8%), advertising £62.2M (-13%), operating loss £33.9M. Source: The Media Leader/InPublishing.
   - **OpenAI licensing deal documented:** Strategic partnership Feb 19, 2025. Guardian archive + real-time journalism in ChatGPT. Also rolling out ChatGPT Enterprise internally. Source: Editor & Publisher.
   - **ProRata licensing deal documented:** Revenue share model (50% of revenue to publishers). Source: INMA webinar with Robert Hahn.
   - **Google advertising relationship expanded:** Programmatic revenue up 25%+, Guardian seeing "less demand through Google's pipes," integrated with The Trade Desk OpenPath. Source: AdExchanger.
   - **GMG Ventures / Mercuri VC arm fully documented:** Fund 1: £42M (Scott Trust sole LP, 1.5x TVPI), Fund 2: £50M (British Business Bank cornerstone). B Corp certified. Focus: AI-enabled media-tech startups. Source: British Business Bank press release.
   - **SPUR coalition membership:** Founding member (Feb 2026) alongside BBC, FT, Sky News, Telegraph. 36 total members. "Operation Leaky Bucket" internal compliance. Source: journalism.co.uk.
   - **Anna Bateson added as CEO** to editorial leadership. Keith Underwood (CFO/COO) documented with OpenAI deal quotes.
   - **OpenAI added as target entity** with coverage asymmetry hypothesis (does coverage soften post-deal?).
   - **4 ownership change events documented:** Scott Trust 2008 conversion, STEL separation, Observer sale, OpenAI partnership.

2. **Editorial changes (`profiles/careers/editorial_changes.yaml`) — 5 new Guardian entries:**
   - Anna Bateson CEO appointment
   - OpenAI licensing deal (2025-02-19) — marked as "CRITICAL BUSINESS EVENT"
   - SPUR coalition founding (2026-02)
   - Dr Jonathan Paine Scott Trust board appointment (2024-11) — Rothschild TMT specialist
   - Jane Martinson Scott Trust board appointment (2025-07)

3. **Tests: 134/134 passing**

### Key analytical discovery:

**The Guardian is no longer a clean control case.** The previous assumption — non-profit trust with $0 AI deals and no corporate parent with tech/AI interests — was WRONG on a critical dimension. The OpenAI licensing deal (Feb 2025) creates a direct commercial relationship with Meta's #1 AI competitor. Combined with the ProRata deal, Mercuri VC fund investing in AI media-tech startups, and SPUR coalition membership creating structural opposition to non-licensing AI companies (including Meta), the Guardian has real financial incentives that could influence coverage.

However, the Guardian's conflicts DIFFER IN KIND from the other four publications:
- **Wired/Condé Nast:** Advance Publications owns 33.5% of Reddit (direct Meta competitor equity)
- **Atlantic:** Emerson Collective holds $16B Apple stock + Mistral AI investment (concentrated competitor equity)
- **NYT:** Amazon AI deal ($20-25M/yr) + actively suing OpenAI/Microsoft (litigation-driven conflict)
- **MIT TR:** Parent MIT receives $174M/yr from industry including Meta itself (research dependency)
- **Guardian:** Licensing deals with AI companies, but NO equity ownership in specific competitors. £1.2B endowment diversified across 28+ PE/VC managers, not concentrated.

**RECLASSIFICATION:** Guardian moved from "clean control case" to "partial control." Still the closest thing to a baseline in the 5-publication set, but with documented caveats. Pre-Feb 2025 Guardian coverage is cleaner than post-deal coverage for analytical purposes.

**Three testable hypotheses generated:**
1. Did Guardian coverage of OpenAI change after Feb 2025 deal?
2. Does Guardian cover Meta differently from its licensing partners vs non-partners?
3. Did SPUR coalition formation (Feb 2026) shift editorial framing of AI companies?

### Sources:
- Scott Trust Endowment 2024/25 performance report: `uploads.guim.co.uk/2025/09/11/Scott_Trust_Endowment_performance_report_24_25_(1).pdf`
- Editor & Publisher (editorandpublisher.com) — OpenAI deal, Jane Martinson board appointment
- INMA (inma.org) — Robert Hahn webinar: OpenAI + ProRata + pipeline deals
- InPublishing (inpublishing.co.uk) — Dr Jonathan Paine board appointment, Scott Trust board list (Nov 2024)
- journalism.co.uk — SPUR coalition founding announcement
- televisual.com — SPUR coalition expansion
- Tomorrow's Publisher (tomorrowspublisher.today) — FY2024-25 results
- The Media Leader (uk.themedialeader.com) — FY2023-24 results with advertising revenue breakdown
- British Business Bank press release — GMG Ventures / Mercuri Fund 2
- Global Venturing — Mercuri Fund 2 details
- AdExchanger — Guardian programmatic revenue, Google relationship
- Reuters Institute / Thomson Reuters Foundation — Vivian Schiller biography
- UKSIF — Scott Trust Endowment ESG/investment description
- Wikipedia — Guardian history, Scott Trust structure, conversion timeline

---

## 2026-06-22 19:00 PT — Hour Type B: Journalist/Publication Research — Katie Drummond + Leah Feiger Career Profiles

**Focus:** Deep career research on the two most analytically important figures in Wired's post-2023 editorial transformation: Katie Drummond (Global Editorial Director) and Leah Feiger (first-ever politics editor, now Director of Politics & Science). Drummond was already flagged in `editorial_changes.yaml` as "the most important leadership change" but had NO entry in `journalists.yaml`. Feiger was entirely untracked despite being the person who built Wired's politics desk from scratch.

### What was improved:

1. **Katie Drummond — Complete career history added to `journalists.yaml` (8 career entries):**
   - Wired intern (2009–2012): national security blog, military research during Iraq/Afghanistan. First career job.
   - The Verge (2013-04 – 2014-11): Hired to run new science section. Promoted to assistant managing editor. Part of Josh Topolsky orbit.
   - Bloomberg Businessweek (2014-11 – 2015-10): Deputy editor. Followed Josh Topolsky (third time).
   - Gizmodo (2015-11 – 2017-04): EIC/executive managing editor. ~17 months. First top-editor role.
   - The Outline (2017-04 – 2018-03): First executive editor. Topolsky's startup. ~11 months.
   - Medium (2018-04 – 2019-02): Deputy editor. ~11 months.
   - Vice Media (2019-03 – 2023-08): SVP of Global News & Entertainment. Her longest pre-Wired stint (4.5 years). Led global expansion of Vice News across Latin America, Europe, Asia. Oversaw all Vice digital brands. Teams won Emmys, OJAs, SOPA Awards, Peabody. Left day after Fortress bankruptcy acquisition.
   - Wired (2023-08 – present): Global Editorial Director. Announced Aug 10, started Aug 28. Replaced Gideon Lichfield. Reports to Anna Wintour.
   - Key metadata: Born 1985/1986, Calgary, Alberta. Queen's University BA in Philosophy (2008). Married, one daughter, Brooklyn. Freedom of the Press Foundation board (2024).

2. **Leah Feiger — Complete career history added to `journalists.yaml` (3 career entries):**
   - Freelance (2016-01 – 2020-09): Atlantic (editorial fellow), NYT, WaPo/The Lily, The Forward, Fodor's, OZY, Atlas Obscura, Bitch Media, Culture Trip, Segal Family Foundation. Education: Dartmouth BA (African Studies + Gender Studies), UCT MS (Gender Studies), Columbia MS (Journalism).
   - Vice News (2020-09 – 2023-11): Senior features editor → managing editor. Led politics and gender coverage. Vice News Reports podcast credits. Direct overlap with Drummond at Vice (Drummond was SVP Mar 2019 – Aug 2023).
   - Wired (2023-11 – present): First day Nov 13, 2023. First-ever politics editor. Part of 3-reporter, 2-editor politics team (with William Turton, David Gilbert). Reports to Meg Marco. Promoted to Director of Politics & Science by 2025-2026. Hosts WIRED Politics Lab podcast. 252+ articles.

3. **`editorial_changes.yaml` — Wired section massively expanded:**
   - Drummond entry rewritten: full career context (Gizmodo EIC → Vice SVP → Wired GED), editorial philosophy quote, DOGE metrics (62,500 subs in 2 weeks), Sidney Hillman Prize, Story Zero ethos, FPF board, Anna Wintour reporting line.
   - New entry: Leah Feiger politics editor hire (2023-11). Documents creation of first-ever Wired politics team (3 reporters + 2 editors). Names full team: Feiger, William Turton (Bloomberg), David Gilbert.

4. **`profiles/wired.yaml` — editorial_leadership section overhauled:**
   - Drummond entry expanded with start_date, full editorial stance documentation, key metrics
   - Added Leah Feiger (Director of Politics & Science) with editorial stance
   - Added Brian Barrett (Executive Editor, News)
   - Added Zoë Schiffer (Director of Business & Industry)
   - Added Meg Marco (Executive Editor of News — Feiger's boss)
   - key_journalists section expanded: added Leah Feiger, William Turton, David Gilbert entries; updated existing entries with podcast/title details

5. **Key analytical insights documented in journalist notes:**

   **The Drummond→Feiger Vice pipeline:** Drummond was Vice SVP (Mar 2019 – Aug 2023). Feiger was Vice features editor (Sep 2020 – Nov 2023). They overlapped for 3 years. When Drummond took the Wired job in Aug 2023, she recruited Feiger from Vice within 3 months (Nov 2023 first day). This is a direct personnel pipeline from Vice's adversarial editorial culture into Wired's newsroom.

   **The Josh Topolsky orbit:** Drummond followed Josh Topolsky across THREE publications: The Verge → Bloomberg (2014) → The Outline (2017). This is a unique pattern in the dataset — no other tracked journalist shows this kind of serial affiliation with a single editorial mentor.

   **Career-arc bias signal:** Drummond's entire career progression — Gizmodo (tech-adversarial by founding DNA) → Vice (explicitly adversarial brand identity) → Wired (now explicitly adversarial under her leadership) — represents a consistent selection effect: she has chosen, and been chosen by, publications with confrontational editorial postures. Her stated philosophy confirms this: "If you do wrong, I want to find out, and then I want the world to know."

   **Institutional transformation quantified:** Under Drummond + Feiger, Wired achieved: (1) first-ever politics team (Nov 2023), (2) first-ever politics issue (2025), (3) 62,500 new US subs in 2 weeks from DOGE coverage (Feb 2025), (4) Sidney Hillman Prize, (5) CBS Mornings, Pivot podcast, Business Insider profiles, (6) Uncanny Valley podcast franchise + KQED radio, (7) first dedicated Musk beat reporter, (8) political billboard campaigns in Brooklyn/DC/LA/Austin/SF. This is not a gradual editorial drift — it's a deliberate structural pivot executed by two leaders with adversarial-journalism backgrounds.

### Sources:
- Wikipedia: Katie Drummond (en.wikipedia.org/wiki/Katie_Drummond)
- Depth Perception by Long Lead: "If you do wrong, I want the world to know" (depthperceptionbyll.substack.com/p/katie-drummond-journalist-interview-wired)
- The Wrap: "Katie Drummond Named Wired Top Editor After Exit From Vice" (thewrap.com, Aug 2023)
- The Org: Katie Drummond profile (theorg.com/org/wired/org-chart/katie-drummond)
- Freedom of the Press Foundation: Board announcement (freedom.press, 2024)
- ONA23: Katie Drummond bio (ona23.journalists.org)
- MMA Global: Katie Drummond bio (mmaglobal.com)
- PPA: Condé Nast appointment (ppa.co.uk, Aug 2023)
- Condé Nast: Official announcement (condenast.com, Aug 2023)
- AP/Boston Globe: "Not known for political coverage, Wired takes a leading role" by David Bauder (Feb 26, 2025)
- Business Insider/Talking Biz News: "How DOGE and Trump helped Wired add 62K subs in two weeks" by Peter Kafka
- Talking Biz News: "Wired is launching a political coverage team" (Nov 2023)
- Talking Biz News: "Vice hires Feiger as senior features editor" (Sep 2020)
- Talking Biz News: "Wired magazine wins Hillman Prize" (2025)
- Mediatrends.it: Leah Feiger interview at Wired Italy Big Interview, Bocconi University Milan (Jun 2025)
- Muck Rack: Leah Feiger profile
- JournalistHunt: Leah Feiger profile
- Nieman Lab: "Wired is teaming up with KQED" (2026)
- Talking Biz News: "Wired seeks a staff editor" job listing (2026) — confirms "director, science, politics, and security" title
- Adweek: "As Wired Journalists Become Influencers, Subscriptions Surge" (2025)
- Adweek: "Wired Sees Commercial Gains and Editorial Traction" (2025)
- Variety: "Vice Names Katie Drummond Senior VP of Digital" (Mar 2019)
- Vox/Recode: "The Outline has hired Gizmodo Media's Katie Drummond" by Peter Kafka (Apr 2017)
- Observer: "It's Always Some Gawker Season Somewhere" (Nov 2015) — Gizmodo hire
- Talking Biz News: "Businessweek hires Drummond from The Verge" (Nov 2014)
- Knight Science Journalism @ MIT: "The Verge launches new science vertical with Wired's Drummond" (Apr 2013)
- NYT: "Wired's New Editor Doesn't Care if the Tech Bros Are Mad" by Katie Robertson (Mar 2026) — cited via Wikipedia ref
- Pivot podcast transcript: Drummond guest, DOGE coverage discussion (Feb 2025)

### Commit: `d4b5f49`
### Tests: 134/134 passing
### Files modified: 4 (profiles/careers/journalists.yaml, profiles/careers/editorial_changes.yaml, profiles/wired.yaml, iteration-log.md)

## 2026-06-22 11:00 PT — Hour Type D: Toolkit Quality — Source Stance, Outsourced Intensity, Power Asymmetry

**Focus:** Implement three critical analytical features identified as gaps across multiple prior iteration cycles (Type A: Guardian Hay Festival, Wired NameTag, Wired Applied AI Revolt). These were the most-cited open issues in the codebase.

### What was improved:

1. **Source Stance Analysis (`sources.py: analyze_source_stance()`):**
   - New function that classifies each extracted source as adversarial, supportive, or neutral
   - Uses quote content analysis: scans source quotes for negative stance terms (harmful, reckless, censorship, exploitation, etc.) and positive stance terms (innovative, beneficial, safe, transparent, etc.)
   - Weights adversarial attribution verbs (warned, blasted, fumed, accused, threatened, etc.)
   - Produces `stance_balance` metric: -1.0 (all adversarial) to +1.0 (all supportive)
   - Returns named lists of adversarial/supportive sources for auditing
   - Solves the repeatedly-identified gap where `source_authority` scored 1.0 (all named = high quality) even when 100% of sources were deployed to attack the subject

2. **Outsourced Intensity Detection (`sentiment.py: measure_outsourced_intensity()`):**
   - New function that splits article text into quoted segments and editorial prose
   - Measures emotional language density in each segment independently
   - Computes `outsourced_ratio`: 0.0 (balanced) to 1.0 (all emotional language in quotes)
   - Handles both smart (curly) quotes and straight quotes
   - Returns word counts for quoted vs editorial segments
   - Solves the "outsourced intensity not detectable" gap first identified in the Guardian Hay Festival analysis

3. **Power Asymmetry Framing Device (`framing.py: power_asymmetry`):**
   - New framing device type with 6 pattern families:
     - Financial magnitude near individual ($1.5T corporation vs. whistleblower)
     - Legal army / deep pockets / unlimited resources language
     - David vs Goliath explicit framing
     - Cannot-afford-legal-fight patterns
     - Fine-per-violation-could-bankrupt patterns
     - Reverse direction (individual near corporate financial scale)
   - Added to `_ADVERSARIAL_DEVICE_TYPES` set so it contributes to framing correction
   - False-positive guard: doesn't fire on routine earnings reports with dollar figures
   - Solves the "power asymmetry not a recognized device type" gap

4. **22 new tests (`tests/test_source_stance.py`):**
   - TestAnalyzeSourceStance: 7 tests (adversarial, supportive, mixed, empty, neutral, loaded verb shift, source name lists)
   - TestOutsourcedIntensity: 6 tests (high outsourcing, no outsourcing, empty, balanced, smart quotes, word counts)
   - TestPowerAsymmetryFraming: 6 tests (financial asymmetry, legal army, David vs Goliath, cannot afford, no false positive, fine per violation)
   - TestIntegrationWhistleblowerArticle: 3 end-to-end tests (realistic whistleblower article scenario triggering all three features)
   - Total test suite: 106/106 passing (84 existing + 22 new)

5. **METHODOLOGY.md expanded with 2 new sections:**
   - §6 Source Stance Analysis: scoring formula, interpretation table, interaction-with-authority matrix (High authority + Adversarial stance = sophisticated editorial bias)
   - §7 Outsourced Intensity Detection: detection method, outsourced_ratio interpretation table, combined signal analysis
   - Power Asymmetry added to §4.1 framing device taxonomy table
   - Section numbering updated (§9 Limitations, §10 References, §11 Causal Identification)

6. **README.md updated:**
   - Items 10-12 added to "What It Does" list: outsourced intensity, source stance, power asymmetry framing

### Key analytical insight documented:

The most sophisticated form of editorial bias combines three signals:
- **High source authority** (all named, credentialed sources)
- **Adversarial source stance** (all sources deployed against subject)
- **High outsourced intensity** (emotional language in quotes, not editorial prose)

This combination reads as professional journalism — measured prose, named sources, direct quotes — while the entire frame is adversarial. No single metric detects it; only the combination reveals the pattern.

### Commit: `6f77768`
### Tests: 106/106 passing
### Files modified: 7 (sources.py, sentiment.py, framing.py, METHODOLOGY.md, README.md, test_sentiment.py, test_source_stance.py [new])

## 2026-06-22 09:00 PT — Hour Type C: MIT Technology Review Ownership & Funding Deep Dive

**Focus:** Comprehensive ownership, governance, and institutional funding deep dive on MIT Technology Review — the publication with the thinnest existing profile and the most structurally complex conflict of interest among all 5 tracked publications.

### What was improved:

1. **Complete corporate structure documented from IRS 990 filings:**
   - Technology Review Inc., 501(c)(3) nonprofit, EIN 95-4893200
   - Revenue: $22.3M (FY2024 ending June 2024), $22.3M expenses, $6.5M total assets
   - Revenue model: ~33% from events (CEO stated Digiday 2020), plus subscriptions, advertising/brand partnerships, custom content
   - CEO/Publisher Elizabeth Bramson-Boudreau: $420K + $71K benefits (FY2024)
   - EIC Mat Honan: $292K + $74K benefits (FY2024)
   - Filing flags: "Provided first-class or charter travel" + "Reported conflict of interest transactions" in FY2024

2. **MIT-controlled board of directors fully mapped:**
   - 4 of 8 members are MIT administrators compensated $333K-$1.05M by MIT
   - Cynthia Barnhart (Co-Chair, MIT Provost, $987K from MIT) — oversees academic partnerships with Google, Amazon, etc.
   - David Schmittlein (Director, MIT Sloan Dean, $1.05M) — leads corporate education programs
   - Glen Shor (Director, MIT EVP/Treasurer, $883K) — manages MIT's finances
   - Whitney Espich (Director, $333K from MIT)
   - 4 external members: Alan Spoon (Co-Chair), Josh Macht, Lara Boro, Peter Caruso (Clerk)
   - **No structural editorial independence mechanism** (no Scott Trust, no dual-class shares)

3. **Former board members with Epstein connections documented:**
   - Joichi Ito (Director FY2018-2020) — resigned over Epstein funding scandal, was on TR board WHILE soliciting Epstein donations
   - Israel Ruiz (Director FY2019-2020) — one of three MIT VPs who approved Epstein's post-conviction donations
   - Martin Schmidt (Chair through FY2022) — MIT Provost tasked with investigating Epstein donations

4. **MIT institutional research funding quantified:**
   - $762M total research expenditures (FY2020), $174M (23%) from industry
   - MIT-IBM Watson AI Lab: $240M/10yr ($90M to MIT directly), established 2017
   - MIT Schwarzman College of Computing: $1.1B total, $350M from Stephen Schwarzman/Blackstone (2018), houses MIT-Google and MIT-Amazon programs
   - MIT-Google Program for Computing Innovation: Up to $130K/project, must show "relevance to Google"
   - MIT-Amazon Science Hub: Formal bilateral research hub
   - MIT-SenseTime Alliance (2018): Chinese AI company, funded 27 research projects, LATER sanctioned by US (Entity List Oct 2019, CMIC list Dec 2021)
   - Eric & Wendy Schmidt personal gift to MIT Intelligence Quest
   - Meta: Funds MIT research through FAIR collaborations (reverse conflict — MIT parent RECEIVES Meta money)

5. **robots.txt analysis (verified Jun 22, 2026):**
   - Blocks 25+ named AI bots — one of the most aggressive blockers in the tracking set
   - Full list: GPTBot, ChatGPT-User, OAI-SearchBot, ClaudeBot, Claude-Web, anthropic-ai, Google-Extended, Google-CloudVertexBot, Meta-ExternalAgent, Meta-ExternalFetcher, FacebookBot, Amazonbot, Applebot-Extended, PerplexityBot, CCBot, cohere-ai, Bytespider, DuckAssistBot, Diffbot, YouBot, and more
   - No known AI licensing deals
   - Blocks EVERY major AI company's bot — including those that fund MIT research

6. **Mat Honan career history expanded:**
   - Wired senior writer/columnist → BuzzFeed News executive editor (SF bureau chief, led to Pulitzer 2021) → MIT TR EIC (Aug 17, 2021)
   - Three-institution chain creates editorial culture bridge analysis opportunity

7. **Gideon Lichfield career history added (new):**
   - Quartz founding editor → MIT TR EIC (2017-2020) → Wired EIC (2020-2023)
   - HIGHEST-VALUE MIGRATION IN DATASET: same person leading two tracked publications sequentially
   - Enables direct DiD regression to decompose individual from institutional editorial effects

8. **Jason Pontin → Bramson-Boudreau CEO transition documented:**
   - Pontin was President/Publisher/CEO ($515K on FY2018 990)
   - Bramson-Boudreau took over ~Oct 2017 from Atlantic Media/Economist Group background
   - Drove digital-first strategy and event revenue expansion

9. **Editorial changes updated:**
   - Added Pontin → Bramson-Boudreau publisher/CEO transition (2017-10)
   - Updated Lichfield hire date and details
   - Updated Honan hire with correct Aug 2021 start date and compensation from 990

10. **Analytical framework significantly advanced:**
    - Identified MIT TR as MOST STRUCTURALLY CONFLICTED publication despite appearing least so
    - Conflict type is COOPERATIVE (parent receives money FROM covered companies) vs COMPETITIVE (Wired's parent owns Meta's competitor)
    - No structural editorial independence mechanism — board controlled by MIT administrators whose primary jobs require maintaining corporate funding relationships
    - Key testable hypothesis: Does MIT TR coverage of companies that fund MIT differ from coverage of companies that don't?

### Key discovery:
- **MIT Technology Review's conflicts are the inverse of Wired's.** Wired/Condé Nast has COMPETITIVE conflicts (Advance owns Reddit, a Meta competitor; has AI deals with OpenAI, Amazon, Apple — all Meta competitors). MIT TR has COOPERATIVE conflicts (MIT RECEIVES money FROM Google, Amazon, IBM, Microsoft, Apple, Meta — all companies MIT TR covers). This means the expected bias direction is opposite: Wired has incentive to cover Meta negatively, while MIT TR has incentive (structurally, not editorially) to SOFTEN coverage of its parent's funders. The toolkit should be able to detect this through sentiment asymmetry analysis comparing coverage of MIT funders vs non-funders.

### Sources:
- ProPublica Nonprofit Explorer: Technology Review Inc. Form 990 filings FY2018-2024
- MIT Facts: Research Expenditures FY2020
- MIT Schwarzman College of Computing: Industry Programs page
- MIT News: IBM Watson AI Lab announcement (Sep 2017), Schwarzman College announcement (Oct 2018), SenseTime Alliance announcement (Feb 2018), Eric Schmidt gift (May 2018), Epstein fact-finding release (Jan 2020)
- MIT Technology Review: Ito resignation coverage, Epstein report coverage, Honan hire announcement
- Digiday: Bramson-Boudreau interview on event revenue (Apr 2020)
- Talking Biz News: Honan hire announcement
- Mission.org: Bramson-Boudreau interview on editorial independence
- technologyreview.com/robots.txt: Direct verification (Jun 22, 2026)
- Wikipedia: MIT Schwarzman College of Computing
- Blackstone.com: Schwarzman biography

## 2026-06-22 07:00 PT — Hour Type A: Article Deep Dive (Guardian Meta/Hay Festival Whistleblower)

**Focus:** Guardian article on Meta silencing Facebook whistleblower Sarah Wynn-Williams at Hay Festival (Jun 1, 2026) — first non-Wired example.

### What was improved:

1. **New annotated example: Guardian Meta Whistleblower Hay Festival (Jun 1, 2026):**
   - Reconstructed from 7+ secondary sources (ExecReview, Infralog, The Times, PPC Land, AOB News, Global Arbitration Review, LinkedIn Journalism Today)
   - Full 8-dimension manual sentiment analysis: overall tone -0.45, emotional intensity 0.55
   - 8 framing devices manually identified (loaded_language, emotional_appeal, power_asymmetry, timeline_implication, source_deployment, outsourced_intensity, refusal_by_absence, scene_setting)
   - Source analysis: 100% anti-Meta named sources, 0% pro-Meta or neutral sources, no Meta spokesperson quote
   - Conflict disclosure assessment: Guardian is the CONTROL CASE — no financial conflicts (Scott Trust non-profit structure), but structural competitive conflict exists. Cadwalladr's personal adversarial history with Meta undisclosed.
   - First Guardian article in sample corpus — diversifies beyond Wired

2. **Emotional language vocabulary expanded (+16 terms):**
   - Legal/censorship/power-abuse terms: censorship, silenced, silencing, gagged, gag order, muzzled, hostage, hostage situation, despotic, tyranny, tyrannical, oppressive, oppression, trolling, intimidate, intimidation, bankrupt, bankruptcy, sanctioned, sanctions motion, punitive, chilling, chilling effect, suppress, suppression, retaliation, retaliatory, stifle, stifled
   - These terms were completely absent from the emotional vocabulary, causing 0.0 emotional intensity on a clearly emotionally charged article

3. **Passive framing vocabulary expanded (+13 patterns):**
   - Legal silencing patterns: "forced to sit in silence", "unable to speak", "unable even to nod", "forced into silence", "sat in silence", "sit in silence", "threatened with bankruptcy", "threatened her", "on the eve of publication", "fines of", "formally sanctioned", "legal order", "legal restrictions", "mounting legal restrictions", "legal action", "emergency legal order", "emergency arbitration", "arbitration order", "sanctions motion"

4. **Framing detection improvements (framing.py):**
   - **Fixed catastrophizing false positive**: "end of" pattern now requires abstract/institutional objects (democracy, freedom, privacy, journalism, era, civilization) rather than matching any "end of" (was triggering on "end of the event")
   - **New loaded_language patterns**: Legal censorship language (censorship, silenced, gagged, hostage situation, despotic, trolling, suppression, retaliation, chilling effect) — catches editorial language framing legal action as speech suppression
   - **New loaded_language patterns**: Corporate-as-state framing (sovereign affect, assert their power, nation states, kings/emperors, bankruptcy, formally sanctioned, sanctions motion) — catches language comparing corporate power to government authority
   - **New emotional_appeal patterns**: Sympathy-eliciting personal impact (moved to tears, standing ovation, act of solidarity, unable to speak/nod, threatened with bankruptcy) — catches emotional scenes designed to generate reader sympathy
   - **New timeline_implication pattern**: "on the eve of" preemptive action constructions (on the eve of, on the verge of, just before, shortly before, the night before) followed by event nouns — classic editorial timing device suggesting suppression

5. **Entity detection expanded (+1 cluster):**
   - New "Whistleblowers/Critics" cluster: Sarah Wynn-Williams, Frances Haugen, Sophie Zhang, Christopher Wylie, Carole Cadwalladr, Tim Wu
   - Critical for articles about corporate accountability where source identity determines framing

6. **README updated**: Sample Output Gallery now includes the Guardian example with key findings.

### Key findings from manual-vs-toolkit gap analysis:

**Toolkit improvements:**
- Emotional intensity: 0.0 → 1.0 (was completely blind to legal/censorship emotional vocabulary)
- Framing devices: 1 false positive → 20 real detections (15 loaded_language, 4 emotional_appeal, 1 timeline_implication)
- Entity detection: Meta-only → Meta (19) + Whistleblowers/Critics (16)

**Remaining critical gaps:**
1. **Source authority metric** scores 1.0 (all named) when the real issue is 100% adversarial source deployment — all 7 quotes are anti-Meta, with Meta getting only 1 passive paraphrase. The metric measures named/anonymous ratio, not whose authority is being invoked against whom.
2. **Headline-body alignment** shows -1.0 (contradictory) when headline and body are perfectly aligned — VADER sign-conflict artifact when both are negative but at different magnitudes.
3. **Comparative framing** misses political/power comparisons (Wu comparing corporations to "despotic nation states") — vocabulary only catches business competitor language.
4. **Outsourced intensity** not detectable — journalistic technique of deploying emotional quotes from sources while maintaining measured editorial prose. The strongest language ("censorship", "despotic", "hostage", "asshole") all come from quotes, not the journalist.
5. **Power asymmetry framing** not a recognized device type — article's core frame is $1.5T corporation crushing individual through legal machinery ($50K/breach, bankruptcy threat).

### Commit: `94843f5`
### Sources: ExecReview, Infralog, The Times (×2), PPC Land, AOB News, Global Arbitration Review, LinkedIn Journalism Today

## 2026-06-22 06:00 PT — Hour Type A: Article Deep Dive (Wired NameTag Investigation)

**Focus:** Wired investigation into Meta embedding unreleased "NameTag" facial recognition system in Meta AI app for smart glasses (~June 5, 2026)

### What was improved:

1. **New annotated example: Wired Meta NameTag Facial Recognition (~Jun 5, 2026):**
   - Reconstructed from 6+ secondary sources (Engadget, Gizmodo, Android Authority, Digital Trends ×2, INCYBER NEWS)
   - Full 8-dimension manual sentiment analysis: overall tone -0.65, emotional intensity 0.55
   - 8+ framing devices manually identified (loaded_language, timeline_implication, refusal_amplification, juxtaposition, emotional_appeal, guilt_by_association)
   - Source analysis: 85% critical, 15% defensive (Meta spokesperson only)
   - Conflict disclosure assessment: Condé Nast/Advance Publications financial interests in Meta competitors undisclosed
   - Two new files: article reconstruction + comprehensive analysis with toolkit comparison

2. **Entity detection expanded with 2 new clusters:**
   - **Privacy/Civil Liberties Orgs:** EFF, ACLU, Access Now, Fight for the Future, EPIC — critical for privacy/surveillance coverage where advocacy orgs are key sources
   - **Media/Publications:** NYT, WaPo, Guardian, Reuters, AP, Bloomberg, FT, TechCrunch, The Verge, Ars Technica, The Information — tracks cross-publication citation patterns

3. **Whitespace handling fix in alias pattern builder (`entities.py`):**
   - `re.escape(alias)` now replaces escaped literal spaces with `\s+`
   - Fixes "The New York\nTimes" across line breaks not matching "The New York Times" alias
   - All multi-word entity aliases now tolerant of newlines, tabs, and multiple spaces

4. **Framing detection improvements (`framing.py`):**
   - Added "discreetly" to loaded_language secrecy patterns (was missing alongside quietly/secretly/covertly/surreptitiously)
   - Added "say-one-thing-do-another" timeline_implication pattern: catches editorial constructions where public statements contradict private actions
   - Added "contradictory/inconsistent/at odds with/undermines/belies" to timeline_implication vocabulary
   - Extended timeline removal pattern to include "investigation" as trigger word

5. **Sentiment analysis improvements (`sentiment.py`):**
   - Added "discreetly" to PASSIVE_FRAMING list
   - Added 13 privacy/surveillance emotional vocabulary terms to EMOTIONAL_LANGUAGE: surveillance, biometric surveillance, mass identification, faceprints/faceprint, vacuum up, weaponized, stalkers/stalking, abusers, covert filming, vile/vile behavior, invasive
   - Emotional intensity on NameTag article improved from 0.0 → 0.43

### Key findings from manual-vs-toolkit gap analysis:

**Critical gap identified — VADER positive-bias on investigative journalism:**
The toolkit scored overall_tone +0.61 on a clearly adversarial (-0.65 manual) article. VADER/TextBlob interpret factual prose as positive even when editorial framing (word choice, source deployment, timeline juxtaposition) is deeply negative. This is the toolkit's single biggest scoring failure and needs a framing-aware correction factor: when loaded_language + timeline_implication + agency_attribution all indicate adversarial framing, apply a negative adjustment to the VADER/TextBlob composite. Priority for next D iteration.

**Source balance gap:** Current source_authority_framing doesn't distinguish whether sources validate or undermine the subject. In this article, 100% of non-Meta sources are critical; Meta's spokesperson is positioned as defensive and immediately contradicted by code evidence. The toolkit scores source_authority as +1.0 (all named sources = high authority) when the real question is whose authority is being invoked against whom.

### Commit: `1991b5c`
### Sources: Gizmodo, Android Authority, Digital Trends (×2), INCYBER NEWS, Engadget, 9to5Google (search snippets)

## 2026-06-22 05:00 PT — Hour Type D: Toolkit Quality & Documentation

**Focus:** Fix all test failures, improve entity detection architecture, add real-world annotated example, improve documentation.

### What was improved:

1. **All 5 test failures resolved (73/73 pass):**
   - `test_large_effect`: `cohens_d()` returns signed value; test fixed to use `abs(d) > 0.8`
   - `test_custom_clusters`: `detect_entities()` only accepted list-format clusters but test/docs used dict format; overhauled to support both
   - `test_empty_mentions`: `get_primary_entity([])` returned `""`, fixed to return `None`
   - `test_each_cluster_has_aliases`: `DEFAULT_ENTITY_CLUSTERS` upgraded from plain list format to dict format with `aliases` key
   - `test_each_cluster_has_regex`: Updated test to treat `regex` as optional (clusters auto-generate patterns from aliases when `regex` absent)

2. **Entity detection architecture overhaul (`entities.py`):**
   - Added `_normalize_cluster()` function to handle both dict format (`{aliases: [...], regex: "..."}`) and list format (`["alias1", "alias2"]`)
   - `DEFAULT_ENTITY_CLUSTERS` now uses dict format with custom regex for Meta, Google, Apple, Amazon — includes negative lookahead for common false positives (Meta tag, Apple pie, Amazon rainforest, Google Sheets)
   - New aliases: Android (Google), AirPods/Apple Watch/John Ternus/macOS (Apple), Prime Video (Amazon), GPT-4o (OpenAI), Windows (Microsoft)
   - Added `ClusterEntry`/`ClusterDict` type aliases for type safety
   - `get_primary_entity()` return type changed from `str` to `str | None`

3. **New annotated example: Wired Meta Applied AI Revolt (2026-06-13):**
   - Reconstructed article text from 6+ secondary sources (NY Post, Memeburn, People Matters, Wired24 ZA, Digital Trends, Reuters)
   - Full 8-dimension manual sentiment analysis: overall tone -0.72, emotional intensity 0.78
   - 5/7 framing devices detected (anonymous authority, catastrophizing, selective omission, emotional appeal, loaded language)
   - Source analysis: 80% anonymous sources, 0% pro-Meta sources
   - Conflict disclosure: Advance Publications' 33.5% Reddit stake undisclosed
   - Counterarguments section: dissatisfaction is real, anonymous sourcing standard for internal reporting, etc.
   - Two new files: `*_article.txt` + `*_analysis.md` pair

4. **Framing detection improvements (`framing.py`):**
   - Added workplace-specific loaded language patterns: soul-crushing, drudgery, gulag, draftees, menial, dehumanizing, atrocious, brutal, sweatshop
   - These patterns surfaced from manual analysis of the Wired Applied AI article

5. **README.md improvements:**
   - Added Troubleshooting section: false positives, signed Cohen's d, dual cluster formats, import errors
   - Added Sample Output Gallery table describing all annotated example files

6. **ADDING_PUBLICATIONS.md improvements:**
   - Updated Target Entity Clusters section to document both dict format (recommended) and list format (shorthand)
   - Added guidance on when to use custom regex vs. auto-generation

### Commit: `c60c709`
### Sources: Wired (paywalled), NY Post, Memeburn, People Matters, Wired24 ZA, Digital Trends, Reuters

---

## 2026-06-22 02:00 PT — Hour Type C: NYT Ownership & Funding Deep Dive

**Focus:** Ownership & Funding Deep Dive — The New York Times Company

### What was improved:

1. **Comprehensive financial data added from SEC filings:**
   - FY2025: $2,824.9M total revenue (+9.2% YoY), $431.6M operating profit (+22.9%), $344.0M net income, $2.09 EPS
   - Q1 2026: $712.2M revenue (+12% YoY), $0.61 EPS (beat $0.49 consensus by 24.5%), digital ads $93.3M (+31.6%), 310K net new digital subs
   - 12.52M digital-only subscribers, 13.08M total (as of Q1 2026)
   - Market cap ~$11.83B, stock ~$73 (Jun 2026)

2. **Sulzberger family dual-class ownership structure documented:**
   - 1997 Trust holds 738,810 Class B shares + 1,400,000 Class A + ~4.3M indirect Class A
   - Class B holders elect ~70% of Board of Directors
   - 8 trustees, supermajority (6/8) required
   - Primary objective: "maintain the editorial independence and integrity of The New York Times"
   - Family aggregate: ~11% of total equity (but controls the company via Class B)
   - Source: SEC DEF 14A proxy statement

3. **Institutional shareholders section (new):**
   - 95.37% of Class A owned by institutional investors
   - Top 7 holders: Vanguard ($1.09B), T. Rowe Price ($727.45M), AQR Capital ($433.28M), Wellington ($361.81M), Berkshire Hathaway ($351.66M), State Street ($348.99M), Darsana Capital ($299.29M)
   - Notable: Berkshire Hathaway is actively buying NYT stock ($5.07M in 24mo)
   - T. Rowe Price is largest seller ($4.57M in 24mo)

4. **Amazon AI licensing deal ($20-25M/yr) fully documented:**
   - First AI content licensing deal for NYT, signed May 29, 2025
   - Multi-year agreement: Amazon gets news + Cooking + The Athletic content
   - Can train AI models AND use summaries/excerpts in products (Alexa, etc.)
   - Financial terms from Bloomberg: $20-25M/year (~1% of total 2024 revenue)
   - Key strategic signal: NYT chose Amazon over OpenAI/Microsoft (suing them)

5. **NYT v OpenAI lawsuit tracker completely rewritten:**
   - All key rulings dated and sourced: motion to dismiss denied (Apr 2025), preservation order (May 2025), preservation affirmed (Jun 2025)
   - Judge names: Sidney H. Stein (presiding), Ona T. Wang (magistrate)
   - Current status: discovery phase, no trial date, NYT searching preserved ChatGPT logs
   - Consolidated with Author Actions (Authors Guild, Alter, Basbanes cases)
   - Mondaq analysis cited for preservation order implications

6. **Meta relationship explicitly documented as $0:**
   - Meta signed AI deals with 7 publishers in Dec 2025; NYT not among them
   - Zero advertising, zero licensing — creates zero commercial counterweight to adversarial coverage
   - Key for asymmetry analysis: Amazon ($20-25M/yr) vs Meta ($0) coverage comparison

7. **Internal AI tools section (new):**
   - Echo (summarization), Stet (quality evaluation), Cheat Sheet (investigations)
   - Approved external tools: GitHub Copilot, Google Vertex AI, NotebookLM, Amazon AI, OpenAI API
   - Zach Seward documented as first editorial director of AI initiatives (hired Feb 2024)
   - Guidelines: AI cannot draft/revise articles, no AI images/videos in stories

8. **Apple relationship corrected:**
   - Apple News partnership ended June 2020 (was incorrectly listed as "partnership")
   - Apple Podcasts subscription program joined Oct 2025
   - Never joined Apple News+ ($10/mo tier)

9. **Amazon added as target entity:**
   - New target entity for coverage monitoring, flagged as licensing partner
   - Coverage asymmetry question: does Amazon coverage soften post-deal?

### Sources:
- SEC 10-K (FY2025) via TradingView
- Zacks.com Q1 2026 earnings analysis (May 7, 2026)
- MarketBeat institutional ownership data (Jun 2026)
- SEC DEF 14A proxy statement (sec.gov)
- Digiday "2025 timeline of AI deals between publishers and tech companies"
- Digiday "NYT's Amazon deal signals a new wave of publisher partnerships" (Jun 2, 2025)
- Livemint/Bloomberg: Amazon $20-25M/yr deal terms disclosure
- Mondaq: "From Copyright Case To AI Data Crisis" (Jul 2025) — comprehensive preservation order analysis
- TechCrunch: "NYT has greenlit AI tools for product and edit staff" (Feb 17, 2025)
- WAN-IFRA: Zach Seward interview on NYT AI toolkit
- IRE.org: "Inside The New York Times's A.I. toolkit"
- Digiday: "Inside The New York Times' AI newsroom strategy"
- TheStreet: "NYTimes Ends Partnership with Apple News" (Jun 29, 2020)
- 9to5Mac: Apple Podcasts + NYT subscription program
- CourtListener: NYT v. Microsoft/OpenAI docket (1:23-cv-11195)
- Global Legal Post: Judge denies OpenAI motion to dismiss (Apr 2025)

---

## 2026-06-22 01:00 PT — Hour Type B: Guardian Tech Desk Deep Dive

**Focus:** Journalist/Publication Research — Guardian technology desk expansion

### What was improved:
1. **6 new journalist career histories** added to `profiles/careers/journalists.yaml`:
   - **Johana Bhuiyan** — Senior tech reporter/editor, Guardian US (Aug 2021–present). Career: POLITICO NY → BuzzFeed News → Recode → LA Times → Guardian. Surveillance of marginalized communities specialist.
   - **Blake Montgomery** — US tech editor, Guardian (Sep 2023–present). Career: EdSurge → BuzzFeed News → Daily Beast → Gizmodo → Guardian. 
   - **Samantha Oltman** — Brief Reworked AI series editor (Feb–Jun 2026). Career: Wired → BuzzFeed News → Recode/Vox EIC → Good Luck Media → Guardian → Bloomberg. Left after only 4 months.
   - **Julia Carrie Wong** — Former Guardian tech reporter (2015–2021). Facebook whistleblower (Sophie Zhang) coverage. Left tech beat for other topics.
   - **Kari Paul** — Former Guardian West Coast tech reporter (2019–2024). Left for art school in Paris.
   - **Hibaq Farah** — Former Guardian UK tech reporter (~2023–2024). Led TikTok moderation investigation. Left for NYT Opinion.

2. **Guardian profile (`profiles/guardian.yaml`) corrections:**
   - **REMOVED** Kiran Stacey from key_journalists — he is the Guardian's UK *policy editor* covering British politics, NOT a tech reporter. Was incorrectly listed as "US tech policy."
   - **ADDED** Blake Montgomery, Johana Bhuiyan as current tech desk staff
   - **ADDED** full editorial history: 4 notable arrivals (Milmo, Bhuiyan, Montgomery, Oltman), 4 notable departures (Wong, Paul, Farah, Oltman)
   - **UPDATED** editorial notes with turnover analysis: significant churn 2021–2026, core stability from Hern (UK, since 2013) and Milmo (global, since 2021)

3. **Editorial changes (`profiles/careers/editorial_changes.yaml`):**
   - Added 3 Guardian leadership entries: Montgomery hire (2023), Oltman hire (2026-02), Oltman departure (2026-06)

### Key discovery:
- **Samantha Oltman's 4-month Guardian tenure** is analytically interesting. She brought Recode/Kara Swisher editorial DNA to the Guardian's "Reworked" AI series, then left for Bloomberg after only ~4 months. This creates a natural experiment: did Guardian AI/work coverage tone shift during her Feb–Jun 2026 tenure? Her Wired → Recode → Guardian path also adds to the Condé Nast editorial pipeline analysis.

### Sources:
- Talking Biz News (talkingbiznews.com) — primary source for all hire/departure announcements
- Muck Rack profiles (muckrack.com) — journalist verification and byline coverage
- The Org (theorg.com) — Bhuiyan career timeline
- Editor & Publisher (editorandpublisher.com) — Guardian Reworked launch, Farah→NYT move
- RocketReach (rocketreach.co) — Kari Paul career dates
- NYT Company blog (nytco.com) — Farah hire announcement

---

## 2026-06-22 08:00 PT — Hour Type B: Atlantic Tech Desk Deep Dive

**Focus:** Journalist/Publication Research — Atlantic technology desk expansion + conflict-of-interest mapping

### What was improved:

1. **6 new journalist career histories** added to `profiles/careers/journalists.yaml`:
   - **Matteo Wong** — Harvard Crimson → Atlantic assistant editor (Jun 2022) → staff writer (May 2024). Atlantic's primary AI voice. Covers chatbot harms, AI safety tensions, labor displacement.
   - **Alex Reisner** — Freelance programmer-journalist → Atlantic contributing writer (Aug 2023) → staff writer (Oct 2025). Broke Books3 story (190K pirated books in Meta/LLaMA training). Built AI Watchdog searchable database. YouTube AI training data investigation.
   - **Kaitlyn Tiffany** — The Verge → Vox/The Goods → Atlantic (Aug 2019). Internet culture/platforms specialist. Author of 'Everything I Need I Get From You' (2022).
   - **Ali Breland** — FCC tech reporter → Mother Jones → Atlantic (May 2024). Disinformation/extremism reporter. Nick Fuentes specialist. Livingston Award finalist.
   - **Ellen Cushing** — East Bay Express → SF Magazine → BuzzFeed News → Atlantic senior tech editor (May 2018) → food/culture staff writer (May 2024). KEY: Built the SF tech bureau that shaped Atlantic's entire tech desk.
   - **Nicholas Thompson** — Washington Monthly → New Yorker → Wired EIC (2017-2020) → Atlantic CEO (Dec 2020). CRITICAL MIGRATION: Creates direct Condé Nast → Atlantic editorial culture pipeline.

2. **Atlantic profile (`profiles/atlantic.yaml`) major overhaul:**
   - Key journalists: 5 → 8 (added Reisner, Tiffany, Breland)
   - Known conflicts: 2 → 5 (added Emerson Collective AI investments $1B+, OpenAI licensing deal, Thompson executive pipeline)
   - Revenue relationships: Added OpenAI licensing deal (May 2024)
   - Ownership chain: Added 5 Emerson Collective investments (Mistral, World Labs, Formation Bio, Zap Energy, Axios)
   - Editorial leadership: Added Thompson (CEO), LaFrance (corrected date), Lattman (vice chairman)
   - Fixed ai_crawl_policy: Was "No known AI licensing deals" — corrected
   - Added OpenAI as target entity
   - Notable arrivals: 3 → 8; added notable departures
   - LaFrance start date corrected from 2021-01 to 2019-05

3. **Editorial changes (`profiles/careers/editorial_changes.yaml`):**
   - Added 5 Atlantic entries: Goldberg (EIC), LaFrance (exec editor, corrected), Thompson (CEO), Cushing (tech editor), Lattman (vice chairman)

### Key discovery:
- **The Atlantic's layered conflicts are deeper than initially mapped.** Emerson Collective's $1B+ AI investments (especially Mistral, a direct Meta Llama competitor) combine with the OpenAI licensing deal, $16B Apple stock, and a CEO who wrote adversarial Facebook coverage at Wired to create multi-level financial incentives. The Atlantic's own union demanding transparency on the OpenAI deal — with EIC Goldberg backing the demand — is itself evidence of internal recognition of potential conflicts. This makes Atlantic potentially a more interesting analytical target than originally anticipated.

### Sources:
- Editor & Publisher (editorandpublisher.com) — all hire/promotion announcements
- Talking Biz News (talkingbiznews.com) — Tiffany, Wong, Reisner, Cushing hire announcements
- VentureBeat (venturebeat.com) — OpenAI-Atlantic deal, Mistral Series B
- The Wrap (thewrap.com) — OpenAI deal terms, union transparency demand
- Bloomberg Tax (news.bloombergtax.com) — deal confirmation
- CNBC/Fintrx via FutureFamilyOffice.net — Emerson Collective $1B+ AI investments
- Intellectia.ai — World Labs $1B round
- TechCrunch — Zap Energy $130M round
- SiliconAngle — Mistral $415M Series A
- NPR, Wikipedia — Emerson Collective Atlantic acquisition (2017)
- WEF, Infosys, WebSummit — Thompson career details
- Muck Rack — Wong, Cushing, Breland byline verification
- Cascade PBS, Authors Guild — Reisner Books3 investigation impact
- The Brief (thebrief.news) — Reisner YouTube AI training data investigation
- Agility PR Solutions — Cushing/Lorenz 2018 hires

---

## 2026-06-23 10:00 PT — Hour Type A (Article Deep Dive)

### Article: The Atlantic — "Inside the Dirty, Dystopian World of AI Data Centers"
- **Author:** Matteo Wong
- **Published:** March 13, 2026 (April 2026 issue)
- **URL:** https://www.theatlantic.com/technology/archive/2026/03/ai-data-center-energy-water-environmental-impact/681930/
- **Archived:** https://web.archive.org/web/2026/https://www.theatlantic.com/technology/archive/2026/03/ai-data-center-energy-water-environmental-impact/681930/
- **Length:** ~4,200 words

### Manual Analysis Summary
- **Overall tone:** -0.40 (moderately negative, sustained rather than inflammatory)
- **Per-entity tone:** Meta -0.55, Google -0.40, Microsoft -0.35, OpenAI/Stargate -0.50, X/Colossus -0.30, Amazon -0.25
- **Framing devices:** 12 total — 6 loaded_language, 3 scale_metaphor, 2 environmental_justice, 1 dystopian_imagery
- **Source analysis:** 0 anonymous sources; sources lean critical (environmental advocates, affected residents, academics) with minimal industry rebuttal
- **Conflict disclosure:** OpenAI licensing deal disclosed inline ("The Atlantic has a business relationship with OpenAI"). Emerson Collective ownership ($1B+ AI investments including Mistral, Apple $16B stake) NOT disclosed. Apple partnership on Siri/Gemini NOT disclosed despite Apple being a data center builder discussed in article.

### Code Changes
1. **Entity alias expansion (`mediascope/analyze/entities.py`):**
   - Added "Stargate" to OpenAI cluster — Stargate is the $500B OpenAI/SoftBank/Oracle data center joint venture prominently discussed in the article. Without this alias, mentions of "the Stargate Project" and "Stargate data centers" would miss the OpenAI attribution.
   - Added "Colossus", "Colossus II" to X/Twitter cluster — Colossus is xAI's Memphis data center (100K Nvidia GPUs), described in the article as consuming as much power as a medium-sized US city. Without these aliases, Colossus references would not roll up to the X/Twitter entity.

2. **README sample output gallery:** Added Atlantic article entry with tone score, framing device breakdown, source count, and conflict disclosure note.

### Toolkit Improvement Recommendations (documented in analysis, not implemented this hour)
- Priority 2: Per-entity tone scoring module (current toolkit computes document-level only)
- Priority 3: Environmental justice frame detector (water stress, emissions rebound, NEPA exemptions)
- Priority 4: Conflict disclosure completeness tracker (disclosed vs. undisclosed per entity)
- Priority 5: Scale metaphor extraction ("enough power to run X," "equivalent to Y homes")

### Test Results
- 143/143 passing (was 134 last checked; additional tests from prior iterations)

### Files
- `examples/sample_output/atlantic_ai_data_centers_dirty_dystopian_2026_03_article.txt`
- `examples/sample_output/atlantic_ai_data_centers_dirty_dystopian_2026_03_analysis.md`

---

## 2026-06-25 02:00 PT — Hour Type A (Article Deep Dive)

### Comparative Analysis: Gizmodo vs Wired — Meta Smart Glasses Launch (June 23, 2026)

**Approach:** Direct comparison of two articles covering the identical event (Meta's self-branded AI glasses launch, June 23, 2026) from publications with different editorial postures. This surfaces framing differences that single-article analysis cannot reveal.

- **Gizmodo** (James Pero): ~890 words, neutral-positive product review. **0 framing devices detected.** Clean consumer journalism with one honest business-question paragraph about Meta's privacy track record.
- **Wired** (Julian Chokkattu): ~1,200 words, neutral-leaning-negative. **10 framing devices detected:**
  - 4× loaded_language ("Comically," "nefarious," "discreetly," "face-recognition feature")
  - 2× self_referential_investigation (WIRED's own NameTag exposé, twice cited)
  - 1× catastrophizing ("disastrous" re: Snap launch)
  - 1× juxtaposition (consumer glasses + military surveillance tech)
  - 1× emotional_appeal (employee morale injected into product review)
  - 1× kicker_framing (unrelated workforce turmoil closing)

**Key finding:** 0.25 manual tone gap (+0.10 Gizmodo vs -0.15 Wired) driven entirely by editorial injection — privacy concern paragraphs (~12% of Wired article), self-referential investigation loop, and negative kicker. Both articles are factually accurate; the framing difference is in what is *included* and where it is *placed*.

**Toolkit validation:** Zero false positives on Gizmodo article is a critical calibration result. The toolkit correctly distinguished Gizmodo's honest analytical observation ("poor track record when it comes to privacy") from Wired's editorial framing.

### Code Changes

1. **New framing device: `scale_magnitude` (27th type)**
   - 7 regex pattern groups: calculated maximums, dollar-impact projections, scale analogies, country/city comparisons, cumulative loss totals, victim/case rosters, comparison amplifiers
   - Implements Priority 5 recommendation from prior Type A iteration (Atlantic data centers analysis)
   - Carefully scoped to avoid false positives on simple number mentions (e.g., "$299 price," "8 hours battery life," "3.5 billion users" without amplifier)
   - Pattern fixes: possessive pronouns before qualifiers ("their global annual sales"), adverb placement flexibility ("enough to roughly power"), optional country qualifiers ("U.S. homes")

2. **Registry and documentation updates:**
   - `tests/test_nyt_ai_reviews.py` registry test: 23→24 pattern-based types
   - `docs/METHODOLOGY.md`: 26→27 total types, added Scale/Magnitude Framing row to Extended Devices table

### Test Results
- **255/255 passing** (was 239; +16 new scale_magnitude tests)
- New test file: `tests/test_scale_magnitude.py` — 16 tests (3 calculated maximum, 2 scale analogy, 2 cumulative total, 3 victim roster, 2 comparison amplifier, 3 negative/false-positive checks, 1 integration)

### Files
- `examples/sample_output/gizmodo_vs_wired_glasses_launch_2026_06_23_analysis.md` (comparative analysis)
- `tests/test_scale_magnitude.py` (new test file)
- Modified: `mediascope/analyze/framing.py`, `docs/METHODOLOGY.md`, `tests/test_nyt_ai_reviews.py`

---

## 2026-06-25 03:00 PT — Hour Type A: Article Deep Dive

### Focus: Reuters × Emily Dalton Smith Departure (2026-06-17)

**Article:** "Meta head of product for 'AI for work' transformation is leaving company" — Reuters wire story reporting Emily Dalton Smith's departure from Meta, where she led the "AI for Work" initiative and Metamate internal AI assistant. First Reuters article analyzed in the toolkit; provides a natural comparison baseline against Wired's editorial coverage of the same Meta restructuring events.

### Manual Assessment
- Overall tone: -0.15 (mildly negative — facts are inherently negative but Reuters maintains flat emotional register)
- Key loaded language: "uproar" (employee characterization), "tantamount to helping design their own bot replacements" (employee-attributed framing)
- Framing comparison: Reuters tone gap from neutral (-0.15) is less than half of Wired's (-0.30 to -0.45) on the same events, confirming the publication DNA hypothesis

### Toolkit Gaps Found
1. **"Uproar"** and **"backlash"** were not in loaded_language patterns
2. **"Tantamount to"** (legitimacy-stripping equivalence construction) was missing
3. **"Helping design their own bot replacements"** variant of "training their own replacements" was missing
4. **Twitter-like false positive:** "Twitter-like microblogging app Threads" incorrectly triggered X/Twitter entity match — descriptive comparison, not entity reference
5. **Sentiment overcorrection:** Post-fix overall_tone -0.452 overcorrects from raw +0.275 (manual: -0.15). Framing correction magnitude needs severity weighting.
6. **Headline-body alignment:** 0.300 score on a genuinely well-aligned neutral article — metric calibrated for editorial articles, not neutral wire-service reporting
7. **Missing entities:** Emily Dalton Smith (7 mentions), Manus, Metamate, China/Chinese government — not in default clusters

### Code Changes

1. **Loaded language pattern expansion** (`mediascope/analyze/framing.py`):
   - Added `uproar|backlash` to employee revolt pattern
   - Added `tantamount\s+to` to employee revolt pattern
   - Added `(?:help(?:ing)?|design(?:ing)?)\s+(?:their|your|our|its)\s+(?:own\s+)?(?:bot\s+)?replacements?` variant

2. **Entity false positive fix** (`mediascope/analyze/entities.py`):
   - Changed alias pattern lookahead from `(?!\w)` to `(?![\w]|-(?:like|esque|style|inspired|adjacent)\b)`
   - Prevents entity matches in descriptive comparisons (Twitter-like, Uber-esque, Apple-style)

3. **New test file: `tests/test_loaded_language_uproar.py`** — 13 tests covering:
   - Uproar/backlash detection (3 tests)
   - Tantamount detection (2 tests)
   - Helping/designing replacements (2 tests)
   - Twitter-like false positive fix (4 tests)
   - Negative false positive checks (2 tests)

### Test Results
- **268/268 passing** (was 255; +13 new)

### Files
- `examples/sample_output/reuters_meta_dalton_smith_departure_2026_06_17_article.txt`
- `examples/sample_output/reuters_meta_dalton_smith_departure_2026_06_17_analysis.md`
- `tests/test_loaded_language_uproar.py` (new)
- Modified: `mediascope/analyze/framing.py`, `mediascope/analyze/entities.py`

---

## 2026-06-25 04:00 PT — Hour Type A: Article Deep Dive

**Focus:** Cross-publication framing comparison — Wired vs. Reuters on Meta MCI data exposure (2026-06-22)

### Improvements

1. **New framing device: `corporate_reassurance_undercut`** (`mediascope/analyze/framing.py`):
   - Detects when corporate PR reassurance language ("carefully designed with privacy safeguards," "no indication of improper access," "committed to / takes seriously") is immediately undercut by adversarial conjunctions and contradicting evidence
   - 5 regex patterns covering: careful-design + contradiction, privacy-safeguards + failure, no-indication + contradiction, committed-to + failure, not-primary-objective + contradiction
   - Validated on both Wired and Reuters MCI articles — fires on both with appropriate intensity differentiation (strong in Wired's adversarial context, mild in Reuters' neutral context)

2. **Updated `detect_framing_devices()` docstring** — now accurately lists all 25 pattern-matched types + 3 structural post-pass types (28 total). Previous docstring was stale at 23.

3. **Registry test updates** (`tests/test_nyt_ai_reviews.py`):
   - `test_pattern_based_device_count`: 24 → 25
   - `test_all_expected_types_registered`: added `corporate_reassurance_undercut` to expected set

4. **METHODOLOGY.md §4.1 updated** — framing device count 27 → 28; `corporate_reassurance_undercut` added to Extended Devices table with description, detection patterns, and provenance (Wired/Reuters MCI coverage).

5. **Cross-publication analysis written** — `wired_vs_reuters_mci_data_exposure_2026_06_22_cross_analysis.md`:
   - Structural comparison: headline framing ("Exposed" vs "Pause"), source architecture, employee voice selection, quantification strategy
   - Framing device density: Wired 7+ devices vs Reuters 1 device
   - Validates `corporate_reassurance_undercut` device on real cross-publication data
   - Establishes wire-service-as-baseline methodology for future comparisons
   - Documents Wired's "Model Compatibility Initiative" naming error (caught by Computerworld)

6. **README.md updated** — test count 239 → 268; new example entry for cross-analysis

### Test Results
- **268/268 passing** (unchanged count; 2 registry tests fixed to match new device)

### Stats
- Pattern-based framing devices: 24 → 25
- Total framing device types: 27 → 28 (25 pattern + 3 structural)
- Example analyses: +1 cross-publication comparison

### Files
- `examples/sample_output/wired_vs_reuters_mci_data_exposure_2026_06_22_cross_analysis.md` (new)
- Modified: `mediascope/analyze/framing.py`, `tests/test_nyt_ai_reviews.py`, `docs/METHODOLOGY.md`, `README.md`

---

## 2026-06-25 05:00 PT — Hour Type A: Article Deep Dive

### Focus: The Atlantic — "No, Artificial Intelligence Is Not Conscious" by Ted Chiang (~June 3, 2026)

### Article Profile
~4,200-word philosophical essay arguing LLMs aren't conscious. Critiques Anthropic's Claude "constitution" (84-page document governing Claude's behavior) as dishonest anthropomorphism. Uses extensive analogies (slot machines, RPG character sheets, Alpha Centauri thought experiment) and rhetorical questions to build argument. Author is a MacArthur Fellow and fiction writer known for "Story of Your Life" (basis for Arrival).

Source: The Atlantic, retrieved via Wayback Machine.

### Gaps Found & Fixed

#### 1. Entity detection (`mediascope/analyze/entities.py`):
- **Amanda Askell** added to Anthropic cluster (Anthropic's in-house philosopher, mentioned 4x)
- **AlphaFold** added to Google cluster + Google regex expanded to match compound product names
- **New Yorker** added to Media/Publications cluster
- **IBM cluster** created (IBM, Deep Blue, Watson, Red Hat) — not in this article but referenced in analysis
- **Sora 2** added to OpenAI cluster

#### 2. Loaded language expansion (`mediascope/analyze/framing.py`):
- Added `preying` / `preys on` / `prey on` to privacy-predation pattern (was missing despite `predatory` being present)
- Added `slavery` to workplace loaded terms (only `slave` existed — `\bslave\b` doesn't match "slavery")
- **New dismissive/trivializing pattern** (12 terms): `hype`, `make-believe`, `game of make-believe`, `play along`, `playing pretend`, `fantasy/fantasies/fantasize`, `indulge/indulging`, `abdicate responsibilities`, `charade`, `theatre/theater`, `parlor trick`, `hand-waving`, `smoke and mirrors`, `window dressing`, `lip service`, `fig leaf`

#### 3. Rhetorical question expansion:
Added 8 new patterns for philosophical/essay-form questions:
- "Should we (seriously/really) consider/believe/accept...?" — philosophical challenge
- "Has anything (fundamentally) changed/shifted...?" — dismissive rhetorical
- "How is this/that [adj], given that...?" — incredulous challenge
- "What are we to make of...?" — reflective/judgmental
- "So why are/is/do/does...?" — dismissive "So" opener
- "Is [entity] going to...?" — accountability challenge
- "Who is...?" — legalistic/categorical challenge

#### 4. Speculative framing expansion:
Added explicit hypothetical markers pattern:
- "for the sake of argument" / "purely for the sake of argument"
- "let's pretend/imagine/suppose/say/assume/hypothesize"
- "hypothetical scenario/situation/world/case"
- "thought experiment"
- "just for argument's sake"

### Results
| Metric | Before fixes | After fixes |
|--------|-------------|-------------|
| Entity mentions | ~53 | 58 (+5) |
| Entity clusters | 3 | 4 (+Media/Pubs) |
| Framing devices | 1 | 20 (+19) |
| Framing device types firing | 1 | 3 (+rhetorical_question, +analogy_stacking) |

### Key Insight
The toolkit was designed primarily for news-article framing (journalistic implications, editorial positioning). Long-form opinion essays by named authors use a different framing vocabulary — philosophical argument, rhetorical questions, and analogy stacking rather than anonymous sourcing and selective omission. This iteration bridges that gap, making the toolkit useful for analyzing essay-form AI criticism alongside standard news coverage.

### Test Results
- **268/268 passing** (all existing tests pass with new patterns)

### Files
- `mediascope/analyze/entities.py` — 5 entity cluster additions
- `mediascope/analyze/framing.py` — loaded_language +1 pattern (dismissive/trivializing), rhetorical_question +8 patterns, speculative_framing +1 pattern, predation/workplace term additions
- `examples/sample_output/atlantic_ai_not_conscious_2026_06_article.txt` — new article text
- `examples/sample_output/atlantic_ai_not_conscious_2026_06_analysis.md` — new analysis with pre/post comparison

---

## Iteration: 2026-06-25T07:00 PT — Type B: Journalist Research

### Focus
Added 3 new journalists to `profiles/careers/journalists.yaml`: Andy Greenberg (Wired security), Cecilia Kang (NYT tech policy), Emily Mullin (MIT TR → Wired biotech). Total journalist count: 56 → 59.

### What Was Improved

**Andy Greenberg** — Wired's longest-serving security/privacy journalist (~12 years, Forbes → Wired 2014). Author of 3 books (*This Machine Kills Secrets*, *Sandworm*, *Tracers in the Dark*). Two Gerald Loeb Awards. His Jeep hack article prompted 1.4M vehicle recall + Senate bill. Added to Investigative Journalists section. Analytical value: institutional control case for measuring Drummond-era editorial drift in security beat.

**Cecilia Kang** — NYT national technology correspondent (AP-Dow Jones → SJMN → WaPo → NYT 2014). Co-authored *An Ugly Truth* (2021) with tracked journalist Sheera Frenkel. Gerald Loeb + George Polk Awards, Pulitzer finalist. Added to NYT Tech Desk section. Analytical value: covers antitrust/regulation — her framing of DOJ v. Google and FTC v. Meta shapes reader understanding of whether Big Tech should be broken up. Cross-reference with Frenkel entry.

**Emily Mullin** — Third MIT TR → Wired migration (after Will Knight 2018, Zeyi Yang 2025). Career: MIT TR associate editor (biomedicine, ~2017-2019) → freelance → Pittsburgh Post-Gazette (COVID) → MIT Knight Science Journalism Fellow → Wired (Jan 2022). Added to Cross-Publication Migrations section. Analytical value: three MIT TR → Wired moves is statistically notable — this is the highest-frequency inter-publication pipeline in the corpus. Biotech beat may be insulated from editorial tone pressure (less politically charged than AI/surveillance), making her a control case for beat-specific editorial pressure.

### Source URLs
- Andy Greenberg: https://www.wired.com/author/andy-greenberg/, https://www.forbes.com/sites/andygreenberg/, https://en.wikipedia.org/wiki/Andy_Greenberg
- Cecilia Kang: https://www.nytimes.com/by/cecilia-kang, https://www.linkedin.com/in/cecilia-kang-b28711/, https://www.washingtonpost.com/people/cecilia-kang/
- Emily Mullin: https://www.wired.com/author/emily-mullin/, https://www.technologyreview.com/author/emily-mullin/, https://ksj.mit.edu/emily-mullin/, https://onezero.medium.com/@emilymullin

### Key Insight
The MIT Technology Review → Wired pipeline is now the single most-documented inter-publication migration channel in the corpus (3 journalists: Knight, Yang, Mullin), spanning AI, China tech, and biotech beats. This pattern suggests a systematic institutional relationship rather than coincidence — possibly Condé Nast recruiting from MIT TR's talent pool, or MIT TR's culture/compensation driving departures. Each migration covers a different beat, ruling out beat-specific pull factors and pointing to institutional-level dynamics.

### Test Results
- Tests run after changes (see below)

### Files
- `profiles/careers/journalists.yaml` — +3 journalists (Greenberg, Kang, Mullin), total 59
- `README.md` — journalist count updated 56 → 59


---

## Iteration: 2026-06-25T11:00 PT — Type B: Journalist Research

### Focus
Added 2 new journalists to `profiles/careers/journalists.yaml`: Matt Burgess (Wired UK security), Lily Hay Newman (Wired US security). New section: "WIRED SECURITY DESK — CURRENT STAFF." Total journalist count: 67 → 69.

### What Was Improved

**Matt Burgess** — Wired UK's primary security/privacy reporter, based in London. Career: UK press agencies/national newspapers → Progressive Digital Media Group (B2B) → Factor magazine (deputy editor) → Wired UK (staff writer → acting commissioning editor → senior editor → deputy digital editor → senior writer, ~2016–present). University of Sheffield journalism degree. Author of 3 books: *Freedom of Information* (Routledge, 2015), *Reed Hastings: Building Netflix* (W&N, 2020), *WIRED Guides: Artificial Intelligence* (Penguin Random House, 2021). Created FOI Directory (2012) — 10,000+ UK public authorities. Key coverage: GDPR enforcement failures, Clearview AI/GDPR, deepfake nudify ecosystem (1.4M+ Telegram accounts), UK Home Office web surveillance, submarine internet cables, passport-free travel/facial recognition. Also published in The Guardian, HuffPost, TechCrunch. Analytical value: longest-serving current security reporter at Wired UK with upward mobility within publication (rare); UK/EU regulatory lens enables cross-continental comparison with US-based security desk.

**Lily Hay Newman** — Wired US senior security/privacy writer, based in NYC. Career: Slate/Future Tense (technology reporter, ~2014–2017) → Wired (senior writer, ~2017–present). ~7+ year tenure makes her one of the security desk's longest-serving current staff alongside Andy Greenberg. Slate's Future Tense was a collaboration with New America Foundation and Arizona State University — think-tank-adjacent pipeline. Key coverage: Trickbot Russian cybercriminals, Okta/Lapsus$ hack, CISA/Jen Easterly interview, protest surveillance, airport security vulnerabilities, digital opsec for teens. Hosts/appears on Wired video series "Incognito Mode" and "The Big Interview." Works closely with Andrew Couts (Senior Editor, Security & Investigations). Fletcher School (Tufts) speaker. Analytical value: US-lens counterpart to Burgess — same desk, same beat, different regulatory contexts. Think-tank pipeline via Future Tense signals policy-first framing orientation.

### Source URLs
- Matt Burgess: https://www.wired.com/author/matt-burgess/, https://talkingbiznews.com/they-re-hiring/wired-uk-hires-burgess-as-staff-writer/, https://theorg.com/org/wired-uk/org-chart/matt-burgess, https://www.cision.co.uk/blog/media-briefing-matt-burgess-wired-uk/, https://muckrack.com/mattburgess
- Lily Hay Newman: https://www.wired.com/author/lily-hay-newman/, https://fletcher.tufts.edu/ (speaker panel reference)

### Key Insight
The new "Wired Security Desk" section now provides comprehensive desk-level staffing data: Andy Greenberg (~12 years, investigative), Dell Cameron (Gizmodo → Wired, surveillance), Dhruv Mehrotra (data/computational), Matt Burgess (Wired UK, EU lens), and Lily Hay Newman (US lens, think-tank pipeline). This enables desk-level editorial analysis — do all five writers exhibit similar adversarial-frame intensity toward Big Tech, or does it vary by beat sub-specialization (cybercrime vs. surveillance vs. GDPR vs. digital safety)? The Burgess/Newman pairing is particularly useful: same employer, same beat, different continents and regulatory contexts.

### Test Results
- 429 tests passing (all green)

### Files
- `profiles/careers/journalists.yaml` — +2 journalists (Burgess, Newman), new section, total 69
- `README.md` — journalist count updated 67 → 69


---

## Iteration: 2026-06-25T15:00 PT — Type A: Article Deep Dive

### Focus
Wired article: "Meta's Very Own Smart Glasses Go on Sale Today for $299" by Julian Chokkattu (Jun 23, 2026). Manual analysis vs toolkit prediction comparison. 4 bugs found and fixed, 17 new tests added.

### What Was Improved

**Bug 1 — Entity miss: Peter Bristol.** Meta's VP of Industrial Design, quoted 2x in the article, was not in `DEFAULT_ENTITY_CLUSTERS`. Added "Peter Bristol" and "Bristol" to Meta aliases and regex. Trade-off: "Bristol" (city) may false-positive in non-tech articles — accepted as consistent with existing single-name aliases.

**Bug 2 — Affiliation misattribution: Bosworth → "Snap's Specs".** The text "On Snap's Specs, Meta chief technology officer Andrew Bosworth says..." caused the possessive pattern to extract "Snap's Specs" instead of "Meta". Root cause: no pattern existed for non-possessive title constructions like "Meta chief technology officer [Name]". Fix: added Pattern 0b (non-possessive title → org affiliation), inserted before the over-broad possessive Pattern 2. Also added "executive" to the title word list to handle "chief executive" (regex backtracking fix).

**Bug 3 — False anonymous source: "Many people are still concerned".** Editorial narration misclassified as anonymous source. Root cause: catch-all anonymous pattern made the attribution verb optional (`?`), allowing "Many people" alone to match. Fix: made verb required. Existing specific patterns (e.g., "people familiar with the matter") are unaffected.

**Bug 4 — Source miss: single-name attribution.** "Bristol says" was invisible because all source patterns required "First Last" two-word names. Added Pattern 5b for single-name sources (`[A-Z][a-z]{2,} [verb]`) with aggressive false-positive filtering: stop words, organization names, and full-name dedup (skip "Bosworth" if "Andrew Bosworth" already captured).

### Source URLs
- Article text: `examples/sample_output/wired_meta_glasses_launch_self_branded_2026_06_23_article.txt`
- Deep dive: `examples/sample_output/wired_meta_glasses_launch_self_branded_2026_06_23_deep_dive.md`

### Key Insight
The affiliation extraction pipeline had a blind spot for the most common title construction in tech journalism: "[Company] [title] [Name] says..." — non-possessive, no preposition. This pattern is more frequent than possessive ("[Company]'s [title]") or prepositional ("at [Company]") forms in product launch and executive interview articles. The fix (Pattern 0b) addresses an entire class of misattributions, not just this one article.

### Test Results
- 446 tests passing (429 + 17 new, zero regressions)

### Files
- `mediascope/analyze/entities.py` — +Peter Bristol/Bristol in Meta cluster
- `mediascope/analyze/sources.py` — 4 source extraction fixes (affiliation, false anon, single-name, dedup)
- `tests/test_glasses_deep_dive.py` — 17 new tests
- `examples/sample_output/wired_meta_glasses_launch_self_branded_2026_06_23_deep_dive.md` — full annotated analysis

## 2026-06-25 17:00 PT — Hour Type B: Journalist/Publication Research

**Focus:** 3 new journalists added + 1 factual error fixed
**Commit:** `c05cae2`
**Journalists:** 70 → 73 total, 69 multi-publication (up from 66)

### New journalists added:

#### 1. Ryan Mac (Forbes → BuzzFeed News → NYT)
- **Why this matters:** Mac is arguably NYT's most important tech accountability reporter covering Meta, Zuckerberg, and Musk. He was the single biggest gap in the dataset — his co-author Kate Conger was tracked but he wasn't.
- **Career:** Stanford BA (2011) → Forbes staff writer (2011-2017, billionaires list → tech startups) → BuzzFeed News senior reporter (Jun 2017-Jun 2021, Facebook/Musk accountability) → NYT correspondent (Jul 2021-present, tech accountability)
- **Awards:** 2019 Mirror Award, 2020 George Polk Award (both for Facebook coverage at BuzzFeed), 2017 Gerald Loeb Award finalist (Thiel/Gawker)
- **Book:** Co-authored "Character Limit: How Elon Musk Destroyed Twitter" (Penguin Press, Sept 2024) with Kate Conger
- **Analytical value:** Same beat (tech billionaire accountability) across 3 institutional contexts — strongest controlled comparison in dataset. Forbes → BuzzFeed → NYT pipeline represents increasing-prestige trajectory amplifying same adversarial instinct. Paired with Kate Conger via shared book creates dual-pipeline natural experiment (Conger: Gizmodo → TechCrunch → NYT vs Mac: Forbes → BuzzFeed → NYT).
- **Sources:** Wikipedia (`en.wikipedia.org/wiki/Ryan_Mac`), nytco.com announcement (Jun 24, 2021), Poynter (May 16, 2017), Penguin Random House author bio, TalkingBizNews (May 2017, Jun 2021), Muck Rack, Web Summit speaker profile

#### 2. Nitasha Tiku (NYmag → NY Observer → Valleywag → Verge → BuzzFeed → Wired → WaPo)
- **Why this matters:** Tiku's Wired → WaPo migration is one of the most analytically valuable transitions in the dataset — she moved FROM a tracked publication (Wired, Condé Nast) to an untracked one (WaPo, Bezos-owned). Her 7-publication career spans nearly every major digital media era.
- **Career:** NYmag assistant editor (~2009-2011) → NY Observer senior editor/Betabeat (~2011-2013) → Valleywag/Gawker editor (~2013-2014) → The Verge West Coast senior editor (~2015) → BuzzFeed News senior writer (~2015-2017) → Wired senior writer (May 8, 2017-Aug 2019) → Washington Post tech culture reporter (Sep 16, 2019-Feb 2026)
- **At Wired:** Under Nicholas Thompson (tracked EIC). Hired same day as features editor Mark Robinson. Wrote cover story on Google turmoil during Trump administration.
- **Laid off:** WaPo Feb 2026 layoffs
- **Sources:** TalkingBizNews hiring announcements (May 2017 Wired hire, Sept 2019 WaPo hire, Feb 2026 layoff), TheOrg.com profile, Poynter (Verge hire ~2015), Longform Podcast #286 (Mar 2018), Podchaser, Data & Society

#### 3. Natasha Singer (Russian Vogue → The Forward → Outside → NYT)
- **Why this matters:** Longest-tenured NYT tech reporter (~17+ years). Non-traditional pipeline (international journalism/literary magazines → NYT tech) with orthogonal beat (education tech, student privacy, consumer data) compared to Meta/platform accountability reporters.
- **Career:** Russian Vogue founding editor (~1998-2001) → The Forward Moscow bureau chief (~2002-2004) → Outside Magazine correspondent (~2005-2007) → NYT reporter (~2008-present)
- **Awards:** 2019 George Polk Award (team, privacy coverage), 2019 Pulitzer finalist (National Reporting)
- **Fellowship:** Knight Science Journalism fellow at MIT (2021-22, alongside Karen Hao — also tracked)
- **Impact:** "You For Sale" series prompted congressional/federal investigations. Coverage led to California's Student Online Personal Information Protection Act of 2014.
- **Sources:** Cornell Milstein Program speaker bio, Clay.earth profile, Data & Society Research Institute page, Podchaser, TalkingBizNews (Knight fellowship), National Education Policy Center

### Bug fix: Kate Conger co-author error
- **Before:** Kate Conger's NYT career entry listed "Character Limit" co-author as "Mike Isaac"
- **After:** Corrected to "Ryan Mac" with note distinguishing Mike Isaac (wrote "Super Pumped" about Uber)
- **Impact:** This error would have corrupted any co-authorship network analysis. Mac and Conger are a rare paired-journalist case (same book, same reporting process, different career pipelines) — getting the link right is essential for the DiD methodology.

### Tests: 464 passing (unchanged — no new test code needed for career data additions)
### Pushed to GitHub

## 2026-06-25 18:00 PT — Hour Type B: Journalist/Publication Research

**Focus:** Data integrity fixes (6 duplicate entries), 2 new journalists (Vittoria Elliott, Makena Kelly), career expansion (Brian Barrett), and 4 new editorial leadership changes.

### Duplicate removal — 6 entries

Found 6 duplicate journalist entries in `journalists.yaml` caused by earlier batch additions:
- James O'Donnell (index 60, first at 49)
- Will Douglas Heaven (index 61, first at 48)
- Eileen Guo (index 62, first at 51)
- Casey Crownhart (index 63, first at 50)
- Amy Nordrum (index 64, first at 55)
- Jessica Hamzelou (index 67, first at 54)

All duplicates had identical data — removed second occurrences. Count: 73 → 67.

### New journalist: Vittoria Elliott (Wired)

**Career pipeline:** Tufts BA (International Relations & Psychology) → international development (Ghana, Kenya, India) → Columbia Journalism MS → freelance (Al Jazeera, ProPublica, The New Humanitarian, CBS, Washington Post) → Rest of World (staff writer, ~2021-2022) → Wired (platforms and power reporter, Jul 2022, now senior writer)

**Analytical value:** Non-traditional pipeline into Wired tech journalism via international development rather than the Silicon Valley insider path. Led Wired's AI Elections Project (2024). Her beat directly overlaps Meta coverage. Regular TV/radio (PBS NewsHour, BBC, NPR, Al Jazeera). Co-bylines with Matt Burgess on EU-Big Tech coverage (May 2026).

**Sources:** Talking Biz News hire announcement, vittoriaelliott.com, Concordia Summit bio, TED AI Show appearance.

### New journalist: Makena Kelly (Wired)

**Career pipeline:** Nebraska Wesleyan BA (Journalism, editor-in-chief of student paper) → Lincoln Journal Star (intern) → CQ Roll Call (Congress reporter, ~2017-2018) → The Verge (politics reporter, ~2019-2023) → Wired (senior writer, politics team, Nov 27, 2023)

**Analytical value:** Part of Drummond's Nov 2023 politics team build-out (alongside Leah Feiger, William Turton, David Gilbert). CQ Roll Call congressional press corps background gives DC framing lens unique among Wired writers. Writes Politics Lab newsletter. Broke CFPB 1,400-employee termination story (2025). Appeared on NPR at DNC 2024 covering political influencers.

**Sources:** Talking Biz News hire announcement (Nov 22, 2023), Podchaser bio, Westminster Town Hall Forum bio, NPR interview transcript (Aug 21, 2024), Techmeme aggregation.

### Career expansion: Brian Barrett (Wired)

**Before:** 1 career event (Wired, 2014-present, thin notes).
**After:** 4 career events with sources:
1. Yomiuri Shimbun — business reporter (~2008-2010)
2. Gizmodo — Editor-in-Chief (~2011-2013). Drummond later called this "The Barrett Era."
3. Wired (first stint) — News editor, ~8 years (2014-2022)
4. Wired (return) — Executive editor of news, rehired by Drummond, Jan 16, 2024

**Key insight:** Barrett's return is a structural signal — Drummond explicitly recruited him because of his Gizmodo adversarial editorial DNA. This creates a natural experiment for pre-Drummond vs Drummond-era editorial tone.

**Sources:** McNally Robinson book bio, ebook.de bio, Advertising Week NYC 2019 bio, Talking Biz News promotion announcement (~late 2023), eaglegeosystems Wired author page.

### Editorial changes added (4 new entries)

1. **Vittoria Elliott hire** (2022-07) — platforms and power reporter, from Rest of World
2. **Makena Kelly politics team hire** (2023-11-27) — senior writer from The Verge
3. **Brian Barrett executive editor return** (2024-01-16) — rehired by Drummond, US/UK news teams
4. **Michael Calore Director promotion** (2024-01) — Director of Consumer Tech & Culture, first of 3 new Director positions under Drummond

### Documentation updates

- journalist count: 70 → 69 (removed duplicates, added 2, net -1)
- multi-publication count: 66 → 68 (both new journalists have multi-pub careers)
- Updated EDITORIAL_HISTORIES.md and README.md counts

### Tests: 464 passing (unchanged — data-only changes)

---

## 2026-06-25 19:00 PT — Hour Type B: Journalist/Publication Research

**Focus:** 5 new journalists (NYT×4, Wired×1) + 4 Wired editorial changes + Wired UK structural contraction

### New journalists added (69 → 74):

| Journalist | Publication | Career Path | Career Events | Source URLs |
|---|---|---|---|---|
| David McCabe | NYT | HuffPost → The Hill → Axios → NYT (2019) | 4 | nytco.com, Benton Institute, Muck Rack |
| Tiffany Hsu | NYT | LA Times → NYT media (2017) → NYT misinfo (2022) | 3 | PEN America, nytco.com, Editor & Publisher |
| Stuart A. Thompson | NYT | WSJ (graphics dir) → NYT Opinion (2017) → NYT misinfo (2021) | 3 | nytco.com, Talking Biz News, Storybench |
| David Yaffe-Bellany | NYT | TX Tribune → NYT fellow → Bloomberg → NYT crypto (2022) | 4 | nytco.com, Talking Biz News, BuzzSumo |
| Joel Khalili | Wired | PR agency → ITProPortal → TechRadar → Wired (2022) | 4 | The Org, TechRadar, Intelligent Relations |

### Why these 5:

1. **McCabe** — NYT's primary tech antitrust/regulation reporter in Washington. Essential for Meta antitrust coverage analysis. Co-covers with Cecilia Kang (already tracked). The Google monopoly trial coverage, FTC AI chatbot inquiry, and Tim Cook/Pelosi lobbying stories are all in MediaScope's analysis scope.

2. **Hsu** — NYT's misinformation reporter covers AI-generated content, deepfakes, platform content moderation — ground zero for Meta coverage bias analysis. Won Mirror Award with Sheera Frenkel (already tracked). Her beat makes every Meta trust & safety story go through her lens.

3. **Thompson** — NYT's other misinformation reporter, unusual visual/data journalist background. WSJ Pulitzer winner turned beat reporter. Co-bylines with Hsu on Sora deepfake investigation. His visual forensic approach is distinct from traditional reporters — relevant for MediaScope's framing analysis.

4. **Yaffe-Bellany** — NYT crypto/fintech reporter. Covers Trump crypto deals ($2B UAE/World Liberty Financial). Intersects with Meta's Libra/Diem history. Texas Tribune → Bloomberg → NYT pipeline is a natural experiment for DiD analysis.

5. **Khalili** — Wired's London-based crypto/fintech reporter. PR agency background (Red Lorry Yellow Lorry) is unusual — insider knowledge of tech PR strategies. His European regulatory perspective on crypto intersects with Meta/Libra coverage.

### Editorial changes documented (Wired, 11 → 15):

1. **UK print edition pulled (2026):** 7 editorial staff left London end of 2025. Team rebuilt for audience development. Katie Drummond quote: "creating a sustainable and growing subscription business is the future of Wired." Digital subscribers doubled. Signals Condé Nast cost-cutting.

2. **Brian Kahn hired (May 4, 2026):** Senior editor, science desk. From Bloomberg climate team. Reports to Tim Marchman. SF office.

3. **Sophie Kleeman hired (May 11, 2026):** Senior editor, business desk. From Business Insider (deputy enterprise editor). Reports to Zoë Schiffer. Creates Drummond → Schiffer → Kleeman editorial hierarchy for enterprise tech/Big Tech coverage.

4. **Peter Guest departed (~Dec 2025):** Acting business editor UK → Coda Story. Part of broader UK contraction alongside 7 other staff departures.

### Analytical observations:

- **Wired UK contraction is significant:** 8 departures (Guest + 7 staff) + print cancellation means Wired's UK/European editorial capacity is sharply reduced. Matt Burgess and Joel Khalili remain but with less editorial infrastructure around them. This could affect Wired's European regulatory coverage quality.

- **Sophie Kleeman reporting to Zoë Schiffer** creates a notable editorial chain: Drummond (EIC, ex-Vice) → Schiffer (senior writer, ex-Verge/Platformer) → Kleeman (senior editor, ex-BI). All three came from adversarial tech media. The business desk's editorial DNA is now almost entirely critical-by-default.

- **NYT misinformation cluster:** Adding Hsu + Thompson completes the NYT misinformation team picture alongside Steven Lee Myers (not yet tracked). All three regularly co-byline. Their beat is inherently about platform accountability — every Meta content moderation decision becomes their story.

- **Multi-publication count:** 66 → 71 (all 5 new journalists have careers at 2+ distinct publications, strengthening DiD regression dataset).

### Stats after this iteration:
- Total journalists: 74
- Multi-publication journalists: 71
- Total career events: 18 new (total ~360+)
- Wired editorial changes: 15
- Tests: 464/464 passing

### Commit: `88f2459` — 2 files changed, 245 insertions
### Pushed to GitHub

---

## 2026-06-25 20:00 PT — Hour Type B: Journalist/Publication Research

**Focus:** 5 new Wired journalists added, expanding roster from 74 → 79. Three new editorial_changes entries. Major analytical finding: Gizmodo/G/O Media as dominant feeder network.

### New journalists added:

#### 1. Tim Marchman — Director, Science, Politics, and Security at Wired (2024–present)
- **Career:** sportswriter (Chicago baseball) → Deadspin EIC (Gawker Media, 2013–2014) → Gizmodo Media special projects editor (2018–2019) → Vice Media features director (2019–2024, through Vice bankruptcy) → Wired (2024–present)
- **Significance:** Recruited by Katie Drummond. Oversees politics desk (Leah Feiger), science desk, security. Led Wired's DOGE scoops that consistently beat NYT/WaPo despite no DC bureau. Philadelphia-based.
- **Gizmodo connection:** ✅ Special projects editor at Gizmodo (2018–2019), overlapping with Drummond's Gizmodo tenure (EIC 2015–2017)
- **Sources:** Bulletin of Atomic Scientists interview (Mar 2025), RocketReach profile, The Org, Talking Biz News, Podchaser
- **Source URLs:**
  - https://thebulletin.org/2025/03/staring-into-the-doge-abyss-with-wireds-tim-marchman/
  - https://rocketreach.co/tim-marchman-email_51918440
  - https://theorg.com/org/wired/org-chart/tim-marchman

#### 2. Sophie Kleeman — Senior editor, business desk at Wired (May 2026–present)
- **Career:** NYU BA journalism & anthropology → Mic (editorial fellow → staff writer, 2014–2015) → Gizmodo (staff writer → news editor, 2016–2018) → Business Insider (essays/features editor → senior investigations editor → deputy enterprise editor, 2018–2026) → Wired (May 2026)
- **Reports to:** Zoë Schiffer
- **Significance:** Enterprise investigative editing specialty — data centers, C-sections, Musk's Tesla empire at BI. Editorial hierarchy now: Drummond → Schiffer → Kleeman for Big Tech enterprise coverage.
- **Gizmodo connection:** ✅ Staff writer/news editor at Gizmodo (2016–2018)
- **Sources:** Talking Biz News, CityBiz, Muck Rack, me.sh, Gizmodo author pages
- **Source URLs:**
  - https://talkingbiznews.com/they-re-hiring/kleeman-joins-insiders-investigations-team-as-senior-editor/
  - https://talkingbiznews.com/media-news/wired-hires-editors-from-business-insider-bloomberg/
  - https://citybiz.co/article/wired-expands-editorial-team-with-hires-from-business-insider-and-bloomberg/

#### 3. Brian Kahn — Senior editor, science desk at Wired (May 2026–present)
- **Career:** Earther managing editor (2017–2021) → Protocol climate editor (2022–2023) → Bloomberg climate team editor (2023–2026) → Wired (May 2026)
- **Reports to:** Tim Marchman
- **Significance:** Climate/clean tech specialist who moved through advocacy-adjacent journalism (Earther) to institutional business journalism (Bloomberg) to Wired. Fourth Earther/Gizmodo connection at Wired alongside Taft, Marchman, Drummond.
- **Sources:** Talking Biz News, CityBiz
- **Source URLs:**
  - https://talkingbiznews.com/media-news/wired-hires-editors-from-business-insider-bloomberg/

#### 4. Molly Taft — Senior writer, science desk at Wired (Mar 2025–present)
- **Career:** Bowdoin BA → Columbia Journalism MS (Stabile investigative fellow) → Center for Public Integrity fellow (2020) → Gizmodo/Earther staff writer (2021–2023, won 2023 SEAL Environmental Award) → The New Republic contributing senior editor, climate (2023) → Drilled Media reporter/editor (2023–2025) → Wired (Mar 2025)
- **Reports to:** Tim Marchman. They/them.
- **Significance:** Climate beat. Drilled Media known for adversarial fossil fuel industry coverage — pipeline mirrors Drummond's recruitment of adversarial-journalism talent.
- **Gizmodo connection:** ✅ Earther/Gizmodo staff writer (2021–2023)
- **Sources:** The Org, Talking Biz News, Rainforest Journalism Fund, Muck Rack, BuzzSumo, Undark Magazine
- **Source URLs:**
  - https://talkingbiznews.com/media-news/wired-hires-taft-as-senior-writer/
  - https://theorg.com/org/wired/org-chart/molly-taft
  - https://rainforestjournalismfund.org/journalists/molly-taft

#### 5. Miles Klee — Senior writer, culture desk at Wired (Feb 2026–present)
- **Career:** Williams College BA English & Philosophy → financial trade pub copy editor → Daily Dot staff writer (2014–2016) → MEL Magazine senior staff writer (2017–2022) → Rolling Stone culture writer (2022–2026) → Wired (Feb 2026)
- **Reports to:** Michael Calore (Director, Consumer Tech & Culture)
- **Significance:** Non-traditional pipeline — no prior tech journalism. Covers internet culture, conspiracy theories, memes, digital subcultures. Author: "Ivyland," "True False," "Double Black Diamond." First major hire from outside traditional tech-journalism pipeline, signals Wired's editorial expansion beyond pure tech coverage.
- **Sources:** Editor & Publisher, Talking Biz News, DIARY directory, The Org, MEL Magazine, Rolling Stone
- **Source URLs:**
  - https://editorandpublisher.com/stories/wired-adds-senior-writer-to-the-culture-desk/
  - https://diarydirectory.com/stories/wired-usa-appoints-senior-writer/

### New editorial_changes entries (3):
- Tim Marchman: director_science_politics_security (2024-01)
- Molly Taft: senior_writer_climate (2025-03-24)
- Miles Klee: senior_writer_culture (2026-02-02)
- (Brian Kahn and Sophie Kleeman already had entries from prior iteration)

### Key analytical finding: Gizmodo/G/O Media as dominant feeder network

Of the 5 new journalists, 3 have Gizmodo in their career histories:
- Tim Marchman: Gizmodo special projects editor (2018–2019)
- Sophie Kleeman: Gizmodo staff writer → news editor (2016–2018)
- Molly Taft: Gizmodo/Earther staff writer (2021–2023)

Combined with Katie Drummond (Gizmodo EIC 2015–2017) and the broader G/O Media diaspora, Gizmodo is now the single largest feeder network into Wired's current editorial structure. This matters for the adversarial-journalism pipeline thesis: Gizmodo was known for confrontational tech coverage, and its alumni are now in editorial leadership (Drummond), desk director (Marchman), and reporting/editing (Kleeman, Taft) positions at Wired.

The full Gizmodo → Wired pipeline now includes at least:
1. Katie Drummond (Gizmodo EIC → Wired Global Editorial Director)
2. Tim Marchman (Gizmodo special projects → Wired Director, Science/Politics/Security)
3. Sophie Kleeman (Gizmodo news editor → Wired senior editor, business)
4. Molly Taft (Gizmodo/Earther staff → Wired senior writer, climate)
5. Brian Barrett (Gizmodo EIC → Wired executive editor, returned 2024)
Plus Brian Kahn's Earther connection (Earther was Gizmodo's climate vertical).

### Stats:
- Total journalists: 79 (was 74)
- Multi-publication: 76 of 79 (was 71 of 74)
- Tests: 464/464 passing
- Commit: `bf081ea` — 4 files changed, 261 insertions, 3 deletions
- Pushed to GitHub

---

## 2026-06-26 06:00 PT — Type B: Journalist Research

**Focus:** Will Oremus — WaPo → Atlantic migration

**New journalist added:**
- **Will Oremus** — 4-position career: Slate (senior writer, 2012-2020) → OneZero/Medium (senior writer, 2020-2021) → Washington Post (tech reporter, 2021-2026) → The Atlantic (tech reporter, 2026-present). BA Philosophy Stanford, MA Politics Columbia. Co-wrote WaPo "Tech 202" newsletter. Departed amid WaPo's Feb 2026 layoffs (~1/3 of staff). Covers online speech, AI, information economy at Atlantic.

**Editorial changes entry:**
- Atlantic: tech_reporter hire — Will Oremus (2026-04)

**Migration significance:**
- WaPo (Bezos-owned, unstable post-layoffs) → Atlantic (Emerson Collective-owned, profitable under CEO Nicholas Thompson — himself former Wired EIC)
- Thompson's presence at Atlantic creates a Condé Nast editorial culture bridge
- Tests: (1) Does Oremus's explanatory/analysis style shift toward Atlantic's longer-form essay voice? (2) Does coverage of Meta/AI carry different framing under Emerson Collective vs Bezos ownership?

**Other findings:**
- Wired actively hiring 5 roles: chief business correspondent, staff editor, senior writer (investigations), staff writer (business), senior writer (climate). No completed hires beyond those already tracked.

**Stats:**
- Total journalists: 86 (was 85)
- Tests: 480/480 passing
- Commit: `ebb8552` — 4 files changed, 83 insertions, 1 deletion
- Pushed to GitHub

---

## 2026-06-26 14:00 PT — Hour Type A: Article Deep Dive

**Focus:** MIT Technology Review op-ed "What AI 'remembers' about you is privacy's next frontier" (2026-01-28) by Miranda Bogen & Ruchika Joshi (CDT)

**Article analysis:**
- Saved: `examples/sample_output/mit_tr_ai_memory_privacy_frontier_2026_01_article.txt`
- Analysis: `examples/sample_output/mit_tr_ai_memory_privacy_frontier_2026_01_analysis.md`
- Framing: 6 devices detected (4 true positives, 2 known false positives documented)
- CDT affiliation: Center for Democracy & Technology — established digital rights org, not activist fringe

**Bug fix (HIGH SEVERITY): analogy_stacking and speculative_framing post-passes never called**
- `_detect_analogy_stacking()` and `_detect_speculative_framing()` were fully defined with patterns, thresholds, and deduplication logic, but `detect_framing_devices()` never called them
- Root cause: these were added as post-passes (like `kicker_framing`) but the calls were never wired into the main detection function
- Fix: added `devices.extend(_detect_analogy_stacking(text))` and `devices.extend(_detect_speculative_framing(text))` after kicker_framing post-pass, with re-sort
- Impact: 2 of 30 device types were completely non-functional before this fix

**Pattern improvements (4 edits to `mediascope/analyze/framing.py`):**
1. loaded_language: added "deceptive", "misleading", "disingenuous" adjectives
2. loaded_language: added `unprecedented [adj]? (breach|violation|exposure|threat|risk|danger|harm|crisis|failure)` pattern
3. speculative_framing: expanded verb list with influence, affect, impact, leak, seep, expose, enable, allow, determine, shape
4. speculative_framing: added optional intervening adverb (`(?:\w+\s+)?`) to "could [adv] verb" pattern for phrases like "could later influence"

**New test file:** `tests/test_postpass_activation.py` — 23 tests covering:
- analogy_stacking above/below threshold (6 tests)
- speculative_framing above/below threshold (4 tests)
- Expanded speculative verbs (leak, seep, expose, influence, etc.) (2 tests)
- loaded_language new patterns (deceptive, misleading, disingenuous, unprecedented+noun) (9 tests)
- Integration: both post-passes firing together (1 test)
- Key learning: analogy pattern tests need well-spaced markers (80+ chars apart) to avoid overlap deduplication from greedy `.{3,80}` regex tails

**Stats:**
- Total test files: 20 (was 19)
- Tests: 518/518 passing (was 495)
- Device types functional: 30/30 (was 28/30 — analogy_stacking + speculative_framing were dead code)


---

## 2026-06-26 14:00 PT — Hour Type A: Article Deep Dive

**Focus:** MIT Technology Review op-ed "What AI 'remembers' about you is privacy's next frontier" (2026-01-28) by Miranda Bogen & Ruchika Joshi (CDT)

**Article analysis:**
- Saved: `examples/sample_output/mit_tr_ai_memory_privacy_frontier_2026_01_article.txt`
- Analysis: `examples/sample_output/mit_tr_ai_memory_privacy_frontier_2026_01_analysis.md`
- Framing: 6 devices detected (4 true positives, 2 known false positives documented)
- CDT affiliation: Center for Democracy & Technology — established digital rights org, not activist fringe

**Bug fix (HIGH SEVERITY): analogy_stacking and speculative_framing post-passes never called**
- `_detect_analogy_stacking()` and `_detect_speculative_framing()` were fully defined with patterns, thresholds, and deduplication logic, but `detect_framing_devices()` never called them
- Root cause: these were added as post-passes (like `kicker_framing`) but the calls were never wired into the main detection function
- Fix: added `devices.extend(_detect_analogy_stacking(text))` and `devices.extend(_detect_speculative_framing(text))` after kicker_framing post-pass, with re-sort
- Impact: 2 of 30 device types were completely non-functional before this fix

**Pattern improvements (4 edits to `mediascope/analyze/framing.py`):**
1. loaded_language: added "deceptive", "misleading", "disingenuous" adjectives
2. loaded_language: added `unprecedented [adj]? (breach|violation|exposure|threat|risk|danger|harm|crisis|failure)` pattern
3. speculative_framing: expanded verb list with influence, affect, impact, leak, seep, expose, enable, allow, determine, shape
4. speculative_framing: added optional intervening adverb (`(?:\w+\s+)?`) to "could [adv] verb" pattern for phrases like "could later influence"

**New test file:** `tests/test_postpass_activation.py` — 23 tests covering:
- analogy_stacking above/below threshold (6 tests)
- speculative_framing above/below threshold (4 tests)
- Expanded speculative verbs (leak, seep, expose, influence, etc.) (2 tests)
- loaded_language new patterns (deceptive, misleading, disingenuous, unprecedented+noun) (9 tests)
- Integration: both post-passes firing together (1 test)
- Key learning: analogy pattern tests need well-spaced markers (80+ chars apart) to avoid overlap deduplication from greedy `.{3,80}` regex tails

**Stats:**
- Total test files: 20 (was 19)
- Tests: 518/518 passing (was 495)
- Device types functional: 30/30 (was 28/30 — analogy_stacking + speculative_framing were dead code)

## 2026-06-26 16:00 PT — Hour Type B: Journalist/Publication Research

**Focus:** Cade Metz career expansion + Jeff Horwitz addition

### Changes
1. **Cade Metz career expanded (2 → 4 entries):**
   - Added PC Magazine (1994–2007): researcher → writer → Senior Writer and Editor. ~13-year tenure. First job after Duke BA English 1994. Source: Duke English dept interview, CHM bio, champions-speakers
   - Added The Register (2007–2011): US Editor, San Francisco bureau chief. Moved to West Coast for this role. Adversarial Wikipedia coverage, appeared in "Truth in Numbers?" documentary. Source: CHM bio, theregister.com archives (last byline Sep 2011)
   - Fixed Wired start date: 2012-03 → 2011-10 (champions-speakers confirms "In 2011"; Register bylines end Sep 2011)
   - Enriched NYT entry with SF bureau, wife Taylor, two daughters, Genius Makers publication details, DiD analysis question
   - Enriched notes with father (IBM engineer, UPC barcode inventor), freelance work (Metro Magazine, Encarta, American Baby), playwright credits

2. **Jeff Horwitz added as journalist #91 (7 career entries):**
   - Washington City Paper → San Bernardino Sun → Legal Times → American Banker → AP → WSJ → Reuters
   - Led 2021 Facebook Files investigation (Frances Haugen whistleblower docs)
   - Won George Polk Award, Gerald Loeb Award (x2), 2026 Pulitzer Prize (with Engen Tham)
   - Author of "Broken Code" (2023); basis for Aaron Sorkin film "The Social Reckoning"
   - Rationale: most consequential single Meta investigator. Not at a tracked publication (WSJ/Reuters) but upstream source for derivative coverage across all 5 tracked outlets

### Sources
- https://english.duke.edu/news/cade-metz-duke-english-alum-technology-correspondent
- https://computerhistory.org/profile/cade-metz/
- https://champions-speakers.co.uk/speaker-agent/cade-metz
- theregister.com/Author/Cade-Metz (archive pages, articles through Sep 2011)
- https://www.reuters.com/media-center/reuters-enterprise-team-expands-with-hires-of-jeff-horwitz-and-gavin-finch/
- https://talkingbiznews.com/media-news/reuters-hires-wsjs-horwitz/
- https://www.pulitzer.org/winners/jeff-horwitz-and-engen-tham-reuters
- en.wikipedia.org/wiki/Jeff_Horwitz

### Test Results
516 passed, 2 failed (pre-existing: outsourced_intensity framing device count mismatch from prior iteration, unrelated to this change)

## 2026-06-26 19:00 PT — Hour Type B: Journalist/Publication Research

**Focus:** Expand Lauren Goode career (2→7 entries), add 2 new journalists (Morgan Meaker, Paris Martineau), add 2 Wired editorial changes.

### Journalists Updated

**Lauren Goode (expanded: 2 → 7 career entries)**
- Full career chain reconstructed: ESPN (production assistant, 2003-05) → A&E Networks (producer on Biography series, 2005-08) → Wall Street Journal (video producer, Digits show, 2008-11) → AllThingsD (senior tech reviewer under Mossberg/Swisher, 2011-13) → Recode (managing editor reviews, 2014-15) → The Verge (senior editor, Emmy Award winner, 2015-18) → Wired (senior writer, 2018-present)
- Key insight: entire career shaped inside the Mossberg/Swisher talent pipeline (AllThingsD → Recode → Verge). She followed them through every entity transition before breaking to Condé Nast.
- Sources: AllThingsD intro post (allthingsd.com/20110824/introducing-lauren-goode/), Talking Biz News hire announcement, Clark University profile (clarku.edu), Vox Media/Recode acquisition coverage (webpronews.com), CHM speaker profile

### Journalists Added

**Morgan Meaker (#96) — Telegraph → Wired → Bloomberg**
- Career: Telegraph reporter (2018-21) → Wired senior writer covering Europe (Nov 2021-Sep 2024) → Bloomberg Weekend senior writer (2025-present)
- City University London MA International Journalism. Forbes 30 Under 30 (European media). BSME 'best of best' + 'best specialist writer' (2023)
- ANALYTICAL VALUE: Her departure from Wired creates a gap in EU regulatory coverage (DSA, DMA, AI Act). No replacement announced as of Jun 2026. Wired → Bloomberg migration = Condé Nast → Bloomberg LP ownership transition.
- Sources: morgan-meaker.com, Talking Biz News hire (Nov 2021) and departure articles, Muck Rack, BuzzSumo, Veryan Studio interview

**Paris Martineau (#97) — Outline → Wired → Information → Consumer Reports**
- Career: NY Magazine/Select All (2017) → The Outline (staff writer, 2018) → Wired (business desk staff writer, Oct 2018-Jun 2020) → The Information (tech/investigative reporter, ~5 years, 2020-24) → Consumer Reports (senior investigative reporter, 2025-present)
- NYU BA Comparative Literature. Known for month-long investigative deep dives at The Information.
- ANALYTICAL VALUE: Pre-Drummond era Wired data point (Thompson era business desk). Crossed 3 distinct funding models: ad-funded (Wired), subscriber-funded (The Information), nonprofit (Consumer Reports) — natural experiment for how funding model shapes framing.
- Sources: Talking Biz News hire/departure announcements, BuzzSumo profile, Better Offline podcast appearance, Techmeme archives

### Editorial Changes Added
1. Morgan Meaker departure from Wired (2024-09) — senior_writer_europe position, no replacement
2. Paris Martineau departure from Wired (2020-06) — staff_writer_business position, joined The Information

### Files Changed
- `profiles/careers/journalists.yaml` — Expanded Goode (7 entries), added Meaker (3 entries), added Martineau (5 entries)
- `profiles/careers/editorial_changes.yaml` — 2 new Wired departures
- `README.md` — Journalist count 95→97, added Meaker and Martineau to migration examples
- `docs/EDITORIAL_HISTORIES.md` — Journalist count 95→97, multi-pub count 92→96

### Commit
- Hash: e2e95b3
- Pushed to GitHub

### Test Results
All 518 tests pass (no regressions — data-only changes).

### Observations
1. **Mossberg/Swisher pipeline:** Lauren Goode's expanded career reveals a talent pipeline from AllThingsD/Recode that fed reporters into both The Verge (Vox Media) and Wired (Condé Nast). Mike Isaac also came through this pipeline before landing at NYT. This cohort shares editorial DNA worth tracking across publications.
2. **Wired Europe coverage gap:** Morgan Meaker's departure (Sep 2024) with no replacement signals Wired deprioritizing dedicated EU tech regulation coverage. This matters for MediaScope because EU regulatory framing (DSA/DMA enforcement, AI Act) is a major vector for anti-Meta coverage.
3. **Funding model natural experiment:** Paris Martineau's 5-publication career spanning 3 distinct funding models (ad, subscription, nonprofit) is a rare natural experiment for DiD analysis of how funding structure shapes editorial framing, independent of individual journalist identity.

---

## Iteration: 2026-06-26 22:00 PT — Type A: Article Deep Dive

**Focus:** Reuters × Meta MCI Pause (2026-06-22) — article already stored, missing analysis file

### Article Analyzed
- **Source:** Reuters (wire service)
- **Title:** "Meta to pause internal mouse-tracking tech while examining data security issues"
- **Authors:** Katie Paul and Jaspreet Singh
- **Date:** 2026-06-22
- **URL:** https://www.reuters.com/legal/litigation/meta-pause-internal-mouse-tracking-tech-while-examining-data-security-issues-2026-06-22/

### Analysis Created
`reuters_meta_mci_pause_2026_06_22_analysis.md` — Full manual analysis with:
- Entity audit (toolkit vs. manual) — 2 clusters correctly detected, no significant gaps
- Framing device deep dive — 6→9 devices after fixes (50% improvement)
- Sentiment scoring root cause analysis — VADER wire-service inflation pattern confirmed
- Cross-publication comparison with Wired's parallel MCI coverage

### Code Improvements (3 changes to `mediascope/analyze/framing.py`)

**1. Surveillance loaded_language: workplace context extension**
- Extended surveillance pattern to match employee/workplace contexts (`employee|worker|staff|intern(?:al)?|workplace|computer`) in addition to consumer/commercial
- Previously: only fired on "tracking... consumer/app/device/glasses"
- Now: fires on "tracking/monitoring... employees' computers" (critical for MCI coverage)

**2. Data-negligence loaded_language pattern (NEW)**
- Added new pattern for technical-negligence indicators: `unencrypted|plaintext|plain.?text|without\s+encryption|not\s+encrypted|stored?\s+in\s+plain` near data/information context
- These terms carry strong editorial valence — naming the absence of encryption implies negligence
- Fires on: "unencrypted form" in MCI article

**3. Claim-vs-reality hypocrisy_frame pattern (NEW)**
- Added wire-service form of stated-vs-actual contradiction: "said/announced it will pause/stop/halt..." (with up to 4 intervening words for temporal phrases) + ".{10,1200}?" + "was still recording/running/..."
- Window of 1200 chars accommodates wire-service structure where contradiction spans 3-6 paragraphs of factual context
- Fires on: "said on Monday it will pause...The tool was still recording" (991 chars apart)

### Test Results
All 518 tests pass (no regressions).

### Key Findings
1. **VADER wire-service inflation confirmed as systematic:** raw_tone +0.498 on a data-exposure article. This is the same class of error as the Dalton Smith analysis (+0.275). Corporate PR language ("carefully designed", "privacy safeguards", "no indication") registers as positive in VADER's lexicon. Two-article pattern now documented.
2. **Wire-service loaded language is subtler than magazine style:** Reuters uses single words ("sensitive", "unencrypted") where Wired would use full sentences. The loaded_language patterns needed workplace surveillance and data-negligence sub-patterns to catch this.
3. **Structural contradiction without conjunction:** Wire services juxtapose claim and reality through paragraph sequencing rather than explicit "yet/but/however" conjunctions. The new claim-vs-reality pattern detects this at paragraph distances up to 1200 chars.
4. **The cross-analysis file already existed** (`wired_vs_reuters_mci_data_exposure_2026_06_22_cross_analysis.md`) — this standalone analysis completes the pair by providing detailed toolkit validation for the Reuters side.

### Commit
- Hash: 3f16877
- Pushed to GitHub
- Changes: `mediascope/analyze/framing.py` (3 pattern additions), `examples/sample_output/reuters_meta_mci_pause_2026_06_22_analysis.md` (new file)

---

## Iteration: 2026-06-27 00:00 PT — Type B: Journalist/Publication Research

**Focus:** Expand Eli Tan career (1→5 entries), update Mike Isaac profile, add NYT editorial changes

### Journalists Updated

**Eli Tan (expanded: 1 → 5 career entries)**
- Full career chain reconstructed: CoinDesk (news reporter, NFTs/gaming/metaverse, Oct 2021–Feb 2023) → Columbia University (MA Journalism, 2023–24) → Washington Post (business/Congress reporter, 2024) → NYT Fellow (technology, 2025) → NYT Staff (Meta beat reporter, 2026–present)
- Key insight: represents a new-generation pipeline into prestige tech journalism — crypto trade press → Columbia MA → WaPo → NYT, rather than the traditional Wired/Verge → NYT path
- His CoinDesk metaverse coverage (during boom/bust cycle) gives him firsthand experience with the hype dynamics Meta bet its corporate identity on
- Sources: NYTCo staff announcement (nytco.com), Bush School alumni profile (bush.edu), CoinDesk author page, Muck Rack profile, Talking Biz News, BuzzSumo journalist profile

**Mike Isaac (profile updated)**
- Notes and latest career entry updated to reflect Jan 2026 role expansion
- Shifted from dedicated Meta reporter (10+ years) to broader Silicon Valley correspondent with mentoring responsibilities
- Eli Tan took over day-to-day Meta beat; Isaac now also "keeps the Tech group on the pulse of news"

### Editorial Changes Added (NYT)
1. Eli Tan hired as `meta_beat_reporter` (new position, Jan 2026) — second dedicated Meta reporter alongside Isaac
2. Mike Isaac expanded to `silicon_valley_correspondent` (Jan 2026) — from Meta-specific to broader SV coverage with mentoring

### Analytical Observations
1. **NYT doubling Meta coverage capacity:** Having two dedicated reporters on a single company beat is unusual — comparable to having two dedicated Apple reporters. This signals institutional investment in Meta as a coverage priority, not just individual interest.
2. **New credentialing pipeline:** The CoinDesk → Columbia → WaPo → NYT path represents a different journalist production pipeline than the Mossberg/Swisher pipeline (AllThingsD → Recode → Verge → NYT) or the Condé Nast pipeline (Wired → NYT). Three distinct feeder systems now populate NYT's tech desk.
3. **DiD opportunity:** Tan's early Meta coverage can be compared against his CoinDesk baseline to measure institutional framing velocity — how quickly NYT's editorial culture shapes a new reporter's tone. His crypto/metaverse background may create a different baseline than reporters who came through policy or general tech beats.
4. **Zero thin profiles remaining:** Database now has no journalists with only 1 career entry — every tracked journalist has a multi-entry career chain for migration analysis.

### Files Changed
- `profiles/careers/journalists.yaml` — Eli Tan (1→5 entries), Mike Isaac (updated notes + career entry)
- `profiles/careers/editorial_changes.yaml` — 2 new NYT entries (Tan hire, Isaac expansion)
- `README.md` — Added Eli Tan to migration examples
- `docs/EDITORIAL_HISTORIES.md` — Multi-pub count 94→95

### Test Results
All 518 tests pass (no regressions — data-only changes).

### Commit
- Hash: 2a9212f
- Pushed to GitHub


## Iteration: 2026-06-27 08:00 PT — Type A: Article Deep Dive

**Focus:** Reuters "In Meta's social media litigation, who pays the lawyers?" (Jun 23, 2026) — insurance companies refusing to cover Meta's defense in 3,300+ child addiction lawsuits

### Article Summary
Alison Frankel's legal analysis column examines a parallel battle to Meta's social media addiction litigation: whether 20+ insurers led by The Hartford and Chubb must cover Meta's defense costs. Delaware Superior Court ruled they don't (deliberate conduct ≠ accident), now on appeal to Delaware Supreme Court. Article draws explicit opioid-era precedent analogy and quantifies Meta's legal exposure ($6M bellwether verdict, 3,300 CA state + 2,400 federal MDL lawsuits).

### Toolkit Gaps Found & Fixed

**A. New entity clusters (entities.py)**
1. **Insurance/Litigation Finance:** The Hartford, Chubb, ACE American, Flashlight Capital, Innsworth Capital, Burford Capital, Reed Smith, Calfee Halter, plus "litigation funder/funding" and "third-party funder/funding" generic patterns
2. **Legal/Judicial:** Delaware Superior/Supreme Court, Section 230, Communications Decency Act, Digital Services Act, DSA, MDL numbers, bellwether trial/verdict/case

**Impact:** Article had 14 undetected entity mentions (7 insurance + 7 legal) — now all correctly clustered.

**B. New framing device: `precedent_analogy` (framing.py)**
- Detects explicit comparison of current controversy to well-known historical case
- 5 regex patterns: era-based precedent, "much like / akin to" comparisons, "following the playbook from", "as was the case with", noun-subject echoes/mirrors/parallels
- Threshold: 1 (fires on single occurrence, unlike analogy_stacking's 3+)
- Rationale: Single strong precedent analogies import settled moral weight — the opioid comparison makes readers evaluate Meta through the lens of opioid villains without argument
- Source pattern: "echoes opioid-era coverage fights involving drugmakers and pharmacies"

**C. Expanded `scale_magnitude` patterns (framing.py)**
- "hundreds/tens/dozens of millions/billions" — vague large-scale amounts (previously undetected)
- "more than N [institutional entities]" — insurers, companies, corporations, firms, agencies, banks, investors, institutions, organizations (previously only caught victim/case rosters)

**D. Fixed analogy marker regex (framing.py)**
- "echoes" no longer requires "of" — `echoes? of` → `echoes?(?: of)?`
- Added "harks back to / mirrors / parallels / recalls / conjures" to marker patterns

**Detection improvement:** Before: 8 framing devices, 3 entity clusters. After: 12 framing devices, 5 entity clusters.

### Files Changed
- `mediascope/analyze/framing.py` — precedent_analogy device, scale_magnitude expansion, analogy marker fix
- `mediascope/analyze/entities.py` — Insurance/Litigation Finance and Legal/Judicial clusters
- `docs/METHODOLOGY.md` — 31→32 device types, precedent_analogy in Extended Devices table
- `docs/AGENT_GUIDE.md` — 31→32 device types, 18→19 extended devices
- `tests/test_nyt_ai_reviews.py` — 28→29 pattern count, precedent_analogy in expected set
- `tests/test_precedent_analogy.py` — 22 new tests (6 precedent_analogy, 5 insurance entities, 4 legal entities, 4 scale_magnitude expansions, 2 analogy marker fixes, 1 false-positive check)
- `examples/sample_output/reuters_meta_insurance_defense_2026_06_23_article.txt` — reconstructed article
- `examples/sample_output/reuters_meta_insurance_defense_2026_06_23_analysis.md` — full analysis

### Test Results
All 563 tests pass (541 existing + 22 new, no regressions).

### Commit

---

## 2026-06-27 13:00 PT — Type A: Article Deep Dive (Confession Framing)

### Focus
Added `confession_framing` as framing device type #33 (30th pattern-matched, 20th extended). Grounded in the Wired Bosworth "Admits" headline analysis and cross-publication attribution verb asymmetry.

### Problem
The toolkit detected loaded individual words ("atrocious," "gulag") but missed the editorial *structure* of framing statements as confessions via attribution verb choice. "Bosworth admits" ≠ "Bosworth said" — the verb choice imposes a confession frame before the reader encounters the content. This asymmetry (employees "describe" while executives "admit") was documented in §4.2 of METHODOLOGY.md but not actually detected.

### Implementation
8 regex pattern families in `mediascope/analyze/framing.py`:
1. **Core confession verbs:** `[Person/Title] admits/admitted/concedes/acknowledged that "..."`
2. **Headline-style:** Title-case `X Admits Y` for headline detection
3. **Amplified confession:** `was forced/compelled/pressured to admit/acknowledge/concede`
4. **Delayed confession:** `finally/eventually/reluctantly/grudgingly admitted/conceded`
5. **Informal:** `came/comes clean about/on`
6. **Informal:** `owned up to`
7. **Direct label:** `mea culpa`
8. **Meta-framing:** `in a rare/stunning/candid admission/acknowledgment/concession`

### Files Changed
- `mediascope/analyze/framing.py` — +95 lines: 8 pattern families, docstring 28→29→30 pattern-matched types
- `tests/test_confession_framing.py` — 31 new tests (15 positive, 6 negative, 5 Bosworth integration, 5 cross-publication)
- `tests/test_structural_consistency.py` — 29→30 pattern-matched, 32→33 total
- `tests/test_nyt_ai_reviews.py` — 29→30 pattern count, confession_framing in expected set
- `docs/METHODOLOGY.md` — 32→33 device types, 19→20 extended devices, new table entry

### Source Articles
- Wired "Meta CTO Andrew Bosworth Admits the Company's AI Reorg Was 'Atrocious'" (Jun 16, 2026)
- Wired Applied AI revolt (Jun 13, 2026) — attribution verb asymmetry documented
- Reuters Dalton/Smith departure (Jun 17, 2026) — comparison: "Reuters would never lead with 'admits'"
- Fast Company Meta reversal (Jun 25, 2026) — validation target

### Test Results
All 616 tests pass (585 existing + 31 new, no regressions).

### Commit
`d0cb040` → `3fea382`

---

## 2026-06-27 15:00 PT — Type A: Article Deep Dive (MIT TR Anthropic Feud)

### Focus
Deep dive on MIT Technology Review's "Three things to watch amid Anthropic's latest feud with the government" (The Algorithm newsletter, Jun 2026). Covers Anthropic Fable/Mythos models, US export controls, Amazon CEO Jassy flagging Fable as dangerous, and AI nonproliferation framing.

### Problem
Initial analysis detected only 2 framing devices. The article uses subtle framing through speculative questions, scare quotes, first-person hedges, and cross-domain analogies (nuclear/pharmaceutical nonproliferation applied to AI) — all patterns the toolkit underdetected.

### Implementation

**Entity improvements:**
- Added `Fable` as Anthropic cluster alias (entity mentioned prominently but unrecognized)
- New `Chinese AI` entity cluster: Zhipu, DeepSeek, Baidu, Qwen, Yi, 01.AI, SenseTime, iFlytek, Megvii, 4Paradigm, Moonshot AI, MiniMax, Zhipu AI

**Framing pattern expansions (5 categories):**
1. **rhetorical_question** — 3 new patterns: speculative questions ("is it possible...?", max 200 chars), cliffhanger questions ("What will X bring?"), capability-challenge questions ("Can X really...?")
2. **ironic_quotation** — 3 scare-quote patterns: lowercase words in quotes, smart-quote equivalent, "broadly labeled" attribution
3. **loaded_language** — 5 new terms: drastic(ally), superficial(ly), reckless(ly), egregious(ly), flagrant(ly)
4. **speculative_framing** — question-form "is it possible" threshold pattern; first-person hedges ("I wouldn't write it off", "Playing this forward")
5. **precedent_analogy** — cross-domain analogy pattern ("in the manner of" / "applying the concept of" + nuclear/pharmaceutical/military domain terms)

### Results
Article detection improved from 2 → 17 framing devices across 7 types. No new device *types* added (still 33 total), only expanded pattern coverage within existing types.

### Files Changed
- `mediascope/analyze/entities.py` — Fable alias + Chinese AI cluster
- `mediascope/analyze/framing.py` — 5 pattern category expansions
- `tests/test_mittr_anthropic_feud.py` — 25 new tests (all pass)
- `examples/sample_output/mittr_anthropic_feud_jun2026.txt` — article text
- `examples/sample_output/mittr_anthropic_feud_jun2026_annotation.md` — full annotation
- `README.md` — test count 585→641, new test file entry

### Test Results
All 641 tests pass (616 existing + 25 new, no regressions).

### Commit
`3fea382`

---
