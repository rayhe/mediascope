# MediaScope Iteration Log

Tracks every improvement cycle run on the toolkit.

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
