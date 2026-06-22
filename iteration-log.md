# MediaScope Iteration Log

Tracks every improvement cycle run on the toolkit.

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
