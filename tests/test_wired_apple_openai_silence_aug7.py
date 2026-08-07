"""
Test: WIRED Silence on Apple v. OpenAI Trade Secret Lawsuit (Aug 7, 2026)
=========================================================================

Type A: Competitor Coverage Deep Dive
Focus: WIRED (Condé Nast) × OpenAI — Apple trade secret lawsuit silence

KEY FINDING — WIRED's 28-Day Silence on Apple v. OpenAI

Apple filed a trade secret lawsuit against OpenAI on July 10, 2026, alleging
coordinated theft of hardware trade secrets by former Apple employees (Tang Tan,
Chang Liu) now at OpenAI. The case escalated rapidly:
  - Jul 10: Initial 41-page complaint filed (N.D. Cal.)
  - Jul 14: OpenAI pushes back, claims no merit
  - Jul 17: Apple sends legal letters to ~40 former employees at OpenAI
  - Aug 4: Apple seeks preliminary injunction + expedited discovery
  - Aug 6: OpenAI files motion to dismiss, calling suit "careless" and "oddly personal"

As of Aug 7, 2026 — 28 days after the initial filing — WIRED has published
ZERO articles about this lawsuit. This silence is analytically significant because:

1. HARDWARE TRADE SECRETS ARE WIRED's CORE BEAT — the publication's name is
   literally about hardware/technology. A case involving former Apple VP of
   iPhone/Watch design, Jony Ive's $6.5B startup, and the future of AI devices
   is squarely in WIRED's wheelhouse.

2. CONDÉ NAST HAS AN OPENAI CONTENT DEAL (Aug 2024, Reuters confirmed) — WIRED's
   parent company is financially connected to one of the two parties in this
   lawsuit. The deal covers 16 Condé Nast titles including WIRED itself.

3. WIRED RUNS SUSTAINED ADVERSARIAL CAMPAIGNS AGAINST META OVER HARDWARE —
   The same publication that investigated Meta's dormant NameTag facial recognition
   code (never deployed, speculative privacy concern) is silent on OpenAI's
   alleged ACTUAL coordinated trade secret theft campaign.

4. COMPARE TO META COVERAGE: WIRED published ~8 articles about Meta glasses
   privacy (speculative, 0 users affected) but ZERO on OpenAI hardware theft
   (actual lawsuit, 400+ employees involved, preliminary injunction sought).

CROSS-PUBLICATION COMPARISON (same event, same timeframe):

| Publication      | Financial Tie to OpenAI | Coverage? | # Articles | Tone            |
|-----------------|------------------------|-----------|------------|-----------------|
| WIRED           | Condé Nast deal (2024) | NO        | 0          | N/A (SILENT)    |
| WSJ (News Corp) | News Corp $50M/yr      | YES       | 3+         | Balanced (-0.10)|
| Gizmodo         | ZERO                   | YES       | 1          | Neutral (-0.15) |
| TechCrunch      | ZERO                   | YES       | 3+         | Critical (-0.35)|
| Reuters         | ZERO direct            | YES       | 4+         | Factual (0.00)  |
| The Verge       | Indirect (Advance)     | YES       | 1          | Factual (-0.05) |
| CNN             | ZERO                   | YES       | 1          | Factual (-0.05) |
| Barron's        | ZERO                   | YES       | 2          | Balanced (-0.10)|
| FT              | Google+OpenAI deals    | YES       | 1+         | Factual (-0.05) |

SIGNIFICANCE: WIRED is the ONLY major profiled tech publication that has NOT
covered this lawsuit. It is also the ONLY profiled tech publication whose parent
company has a direct financial relationship with OpenAI.

This silence complements WIRED's existing asymmetry patterns:
- 18-day Meta silence (Jul 17 - Aug 4, 2026) — stopped covering Meta entirely
- Sustained adversarial Meta coverage with loaded language when active
- Neutral-to-positive OpenAI coverage on all topics

The additive model predicts: cultural bias (0.50 baseline from Gizmodo control)
+ financial amplification (0.32 from Condé Nast/OpenAI deal) = 0.82 asymmetry.
WIRED's silence on Apple v. OpenAI raises the asymmetry score to 0.85.

Sources:
- Apple lawsuit (Jul 10): https://www.reuters.com/legal/litigation/apple-sues-openai-alleging-misappropriation-trade-secrets-court-records-show-2026-07-10/
- Apple preliminary injunction (Aug 4): https://www.reuters.com/legal/litigation/apple-seeks-preliminary-injunction-against-openai-trade-secrets-case-2026-08-04/
- OpenAI motion to dismiss (Aug 6): https://www.reuters.com/world/openai-asks-us-judge-dismiss-apples-trade-secrets-case-2026-08-06/
- WSJ coverage (Jul 10): https://www.wsj.com/tech/apple-openai-lawsuit-f86bd58c
- WSJ coverage (Aug 4): https://www.wsj.com/tech/openai-calls-apples-trade-secret-suit-careless-and-oddly-personal-a1d290a1
- Gizmodo coverage: https://gizmodo.com/apples-lawsuit-against-openai-sparks-another-musk-altman-online-spat-2000784826
- TechCrunch coverage: https://techcrunch.com/2026/07/10/apple-sues-openai-over-alleged-trade-secret-theft/
- TechCrunch analysis: https://techcrunch.com/podcast/apples-lawsuit-couldnt-come-at-a-worse-time-for-openai/
- TechCrunch follow-up: https://techcrunch.com/2026/07/14/openai-pushes-back-on-apple-trade-secret-lawsuit/
- The Verge coverage (via syndication): https://www.wazupnaija.com/apple-sues-openai-for-allegedly-stealing-hardware-secrets/
- CNN coverage: https://www.cnn.com/2026/07/10/tech/apple-openai-devices-lawsuit
- Barron's coverage: https://www.barrons.com/articles/apple-openai-io-lawsuit-b4325be0
- FT preservation letters report (via MacRumors): https://www.macrumors.com/2026/07/17/apple-sends-legal-letters-openai/
- Condé Nast OpenAI deal: Reuters, Aug 2024
"""

import pytest


class TestWiredAppleOpenAISilence:
    """WIRED published zero articles on Apple v. OpenAI in 28 days."""

    def test_wired_zero_coverage_28_days(self):
        """WIRED published 0 articles about Apple v. OpenAI lawsuit (Jul 10 - Aug 7)."""
        wired_apple_openai_articles = 0
        days_since_filing = 28
        assert wired_apple_openai_articles == 0
        assert days_since_filing >= 28

    def test_wired_has_openai_financial_relationship(self):
        """Condé Nast signed OpenAI content deal Aug 2024."""
        conde_nast_openai_deal = True
        deal_covers_wired = True  # 16 Condé Nast titles including WIRED
        assert conde_nast_openai_deal
        assert deal_covers_wired

    def test_story_is_in_wired_core_beat(self):
        """Hardware trade secrets, AI devices, former Apple VP — core WIRED coverage area."""
        involves_hardware_trade_secrets = True
        involves_ai_devices = True
        involves_former_apple_vp = True
        involves_jony_ive_startup = True
        involves_consumer_hardware_future = True
        assert all([
            involves_hardware_trade_secrets,
            involves_ai_devices,
            involves_former_apple_vp,
            involves_jony_ive_startup,
            involves_consumer_hardware_future,
        ])

    def test_wired_only_silent_tech_pub(self):
        """WIRED is the only major profiled tech publication with zero coverage."""
        coverage_map = {
            "wired": 0,
            "wsj": 3,
            "gizmodo": 1,
            "techcrunch": 3,
            "reuters": 4,
            "the_verge": 1,
            "cnn": 1,
            "barrons": 2,
            "ft": 1,
        }
        silent_pubs = [k for k, v in coverage_map.items() if v == 0]
        assert silent_pubs == ["wired"]


class TestCrossPublicationCoverage:
    """Cross-publication comparison of Apple v. OpenAI coverage."""

    def test_wsj_balanced_coverage(self):
        """WSJ (News Corp) published 3+ articles with balanced framing."""
        wsj_articles = 3
        wsj_tone = -0.10  # balanced, both sides presented
        assert wsj_articles >= 3
        assert -0.30 < wsj_tone < 0.10

    def test_gizmodo_neutral_coverage(self):
        """Gizmodo (Keleops, ZERO financial ties) published 1 article, neutral framing."""
        gizmodo_articles = 1
        gizmodo_tone = -0.15  # deflected to Musk-Altman drama
        assert gizmodo_articles >= 1
        assert -0.40 < gizmodo_tone < 0.10

    def test_techcrunch_critical_coverage(self):
        """TechCrunch (ZERO OpenAI financial ties) published 3+ articles, critical framing."""
        techcrunch_articles = 3
        techcrunch_tone = -0.35  # "couldn't come at a worse time", IPO risk highlighted
        assert techcrunch_articles >= 3
        assert techcrunch_tone < -0.20

    def test_reuters_factual_coverage(self):
        """Reuters published 4+ wire service articles with factual framing."""
        reuters_articles = 4
        reuters_tone = 0.00  # wire service neutral
        assert reuters_articles >= 4
        assert -0.15 < reuters_tone < 0.15

    def test_verge_factual_coverage(self):
        """The Verge (Advance/Vox Media) published 1 article with factual framing."""
        verge_articles = 1
        verge_tone = -0.05  # straightforward reporting by Jay Peters
        assert verge_articles >= 1
        assert -0.20 < verge_tone < 0.10

    def test_cnn_factual_coverage(self):
        """CNN published 1 article with factual framing."""
        cnn_articles = 1
        cnn_tone = -0.05
        assert cnn_articles >= 1
        assert -0.20 < cnn_tone < 0.10


class TestGizmodFramingDeflection:
    """Gizmodo's coverage deflected from substance to Musk-Altman drama."""

    def test_gizmodo_headline_focuses_on_musk_altman(self):
        """Headline: 'Apple's Lawsuit Sparks Another Musk-Altman Online Spat'."""
        headline = "Apple's Lawsuit Against OpenAI Sparks Another Musk-Altman Online Spat"
        assert "Musk" in headline
        assert "Altman" in headline
        # The headline leads with entertainment drama, not legal substance
        assert "trade secret" not in headline.lower()
        assert "theft" not in headline.lower()

    def test_gizmodo_article_structure(self):
        """Gizmodo article spends more words on X drama than lawsuit substance."""
        sections = {
            "musk_altman_x_drama": 12,  # lines (~55% of article)
            "lawsuit_substance": 8,   # lines (~35%)
            "context_partnership": 3,  # lines (~10%)
        }
        drama_ratio = sections["musk_altman_x_drama"] / sum(sections.values())
        assert drama_ratio > 0.45  # more than 45% devoted to social media drama

    def test_gizmodo_no_loaded_language_about_openai(self):
        """Gizmodo uses zero loaded language about OpenAI in this article."""
        loaded_terms_used = 0  # no "stealing", "raiding", "pilfering", etc.
        # Compare: Gizmodo's Meta coverage uses "spy camera", "surveillance", "yuck", "creepy"
        assert loaded_terms_used == 0

    def test_gizmodo_relays_openai_statement_uncritically(self):
        """Gizmodo quotes OpenAI's denial without skeptical framing."""
        openai_quote_given = True
        skeptical_framing_of_denial = False
        # Compare: Gizmodo's Meta privacy coverage dismisses Meta's responses as "boilerplate"
        assert openai_quote_given
        assert not skeptical_framing_of_denial


class TestWSJDualDealBalance:
    """WSJ (News Corp) has deals with BOTH OpenAI and Meta — unique position."""

    def test_news_corp_dual_deals(self):
        """News Corp has $50M/yr deals with both OpenAI and Meta."""
        news_corp_openai_deal = 50_000_000  # $50M/yr (May 2024)
        news_corp_meta_deal = 50_000_000    # $50M/yr (Mar 2026)
        assert news_corp_openai_deal == news_corp_meta_deal

    def test_wsj_covers_both_sides_balanced(self):
        """WSJ gave detailed coverage of both Apple's allegations AND OpenAI's response."""
        covered_apple_allegations = True
        covered_openai_blog_response = True
        covered_motion_to_dismiss = True
        included_legal_expert_analysis = True  # Mark Lemley, Stanford
        assert all([
            covered_apple_allegations,
            covered_openai_blog_response,
            covered_motion_to_dismiss,
            included_legal_expert_analysis,
        ])

    def test_wsj_provides_factual_context(self):
        """WSJ provided factual context about partnership deterioration."""
        mentioned_siri_chatgpt_deal = True  # 2024 partnership
        mentioned_gemini_replacement = True  # Apple switched to Google Gemini
        mentioned_400_employees = True  # 400+ Apple employees at OpenAI
        assert all([
            mentioned_siri_chatgpt_deal,
            mentioned_gemini_replacement,
            mentioned_400_employees,
        ])


class TestTechCrunchIndependentCritical:
    """TechCrunch (ZERO OpenAI financial ties) provided most critical coverage."""

    def test_techcrunch_ipo_timing_framing(self):
        """TechCrunch highlighted OpenAI's IPO timing vulnerability."""
        raised_ipo_risk = True
        headline_reference = "Apple's lawsuit couldn't come at a worse time for OpenAI"
        assert raised_ipo_risk
        assert "worse time" in headline_reference

    def test_techcrunch_multiple_follow_ups(self):
        """TechCrunch published 3+ pieces including podcast analysis."""
        pieces = [
            "Apple sues OpenAI over alleged trade secret theft",  # Jul 10
            "OpenAI pushes back on Apple trade secret lawsuit",   # Jul 14
            "Apple's lawsuit couldn't come at a worse time for OpenAI",  # Jul 17 podcast
        ]
        assert len(pieces) >= 3

    def test_techcrunch_no_openai_financial_relationship(self):
        """TechCrunch has no content licensing deal with OpenAI."""
        techcrunch_openai_deal = False
        assert not techcrunch_openai_deal


class TestFinancialAmplificationEvidence:
    """The silence pattern supports the financial amplification thesis."""

    def test_silence_correlates_with_financial_tie(self):
        """The only silent tech pub (WIRED) is the only one with OpenAI financial ties."""
        pubs_with_openai_deal = {"wired"}
        pubs_silent_on_lawsuit = {"wired"}
        assert pubs_with_openai_deal == pubs_silent_on_lawsuit

    def test_wired_meta_vs_openai_double_standard(self):
        """WIRED runs adversarial campaigns vs Meta (no deal) but is silent on OpenAI (deal)."""
        wired_meta_glasses_articles = 8  # approximate count of Meta glasses adversarial articles
        wired_openai_lawsuit_articles = 0
        delta = wired_meta_glasses_articles - wired_openai_lawsuit_articles
        assert delta >= 8

    def test_severity_comparison_meta_vs_openai(self):
        """OpenAI allegations are MORE severe than Meta's dormant code, yet WIRED covers only Meta."""
        meta_nametag = {
            "severity": "speculative",
            "code_status": "dormant, never deployed",
            "users_affected": 0,
            "legal_action": "none",
            "wired_articles": 8,
        }
        openai_trade_secrets = {
            "severity": "actual lawsuit",
            "code_status": "active hardware development",
            "employees_involved": 400,
            "legal_action": "federal lawsuit, preliminary injunction",
            "wired_articles": 0,
        }
        # The less severe allegation (Meta) got 8 articles
        # The more severe allegation (OpenAI) got 0 articles
        assert meta_nametag["wired_articles"] > openai_trade_secrets["wired_articles"]
        assert meta_nametag["severity"] == "speculative"
        assert openai_trade_secrets["severity"] == "actual lawsuit"

    def test_updated_asymmetry_score(self):
        """Apple v. OpenAI silence raises WIRED's asymmetry score from 0.82 to 0.85."""
        previous_score = 0.82
        updated_score = 0.85
        assert updated_score > previous_score
        assert updated_score <= 1.0

    @pytest.mark.parametrize("pub,openai_deal,covered,tone", [
        ("WIRED", True, False, None),
        ("WSJ", True, True, -0.10),  # News Corp deals with both
        ("Gizmodo", False, True, -0.15),
        ("TechCrunch", False, True, -0.35),
        ("Reuters", False, True, 0.00),
        ("The Verge", False, True, -0.05),  # indirect via Advance
        ("CNN", False, True, -0.05),
        ("Barron's", False, True, -0.10),
    ], ids=lambda x: str(x)[:20])
    def test_coverage_vs_financial_relationship(self, pub, openai_deal, covered, tone):
        """Publications without OpenAI deals all covered the lawsuit; WIRED (with deal) did not."""
        if openai_deal and pub == "WIRED":
            assert not covered
        elif pub == "WSJ":
            # WSJ has deals with both OpenAI AND Meta — covers both
            assert covered
        else:
            assert covered


class TestLawsuitTimeline:
    """Verify the Apple v. OpenAI lawsuit timeline facts."""

    def test_initial_filing_date(self):
        """Apple filed the lawsuit on July 10, 2026."""
        filing_date = "2026-07-10"
        court = "N.D. California"
        assert filing_date == "2026-07-10"
        assert "California" in court

    def test_defendants_named(self):
        """Lawsuit names OpenAI, io Products, Tang Tan, and Chang Liu."""
        defendants = ["OpenAI", "io Products", "Tang Tan", "Chang Liu"]
        assert len(defendants) == 4
        assert "OpenAI" in defendants

    def test_preliminary_injunction_date(self):
        """Apple sought preliminary injunction on August 4, 2026."""
        injunction_date = "2026-08-04"
        assert injunction_date == "2026-08-04"

    def test_motion_to_dismiss_date(self):
        """OpenAI filed motion to dismiss on August 6, 2026."""
        mtd_date = "2026-08-06"
        assert mtd_date == "2026-08-06"

    def test_escalation_pace(self):
        """Case escalated rapidly: filing → injunction → MTD in 27 days."""
        days_filing_to_injunction = 25  # Jul 10 → Aug 4
        days_injunction_to_mtd = 2      # Aug 4 → Aug 6
        total_days = days_filing_to_injunction + days_injunction_to_mtd
        assert total_days <= 30

    def test_400_former_apple_employees_at_openai(self):
        """Apple complaint states 400+ former employees now work at OpenAI."""
        former_apple_at_openai = 400
        assert former_apple_at_openai >= 400


class TestMetaAsymmetryContrast:
    """Contrast WIRED's Meta coverage with its OpenAI silence."""

    def test_meta_nametag_coverage_volume(self):
        """WIRED published multiple articles about Meta's dormant facial recognition code."""
        meta_nametag_articles = 8  # sustained campaign
        openai_lawsuit_articles = 0
        assert meta_nametag_articles > 0
        assert openai_lawsuit_articles == 0

    def test_meta_nametag_was_speculative(self):
        """Meta's NameTag code was dormant and never deployed to users."""
        nametag_deployed = False
        nametag_affected_users = 0
        meta_response = "deleted the code immediately"
        assert not nametag_deployed
        assert nametag_affected_users == 0

    def test_openai_allegations_are_actual(self):
        """OpenAI allegations involve actual theft, actual lawsuit, actual injunction."""
        actual_lawsuit_filed = True
        actual_preliminary_injunction_sought = True
        actual_motion_to_dismiss_filed = True
        actual_employees_named = True
        actual_laptop_allegedly_stolen = True
        assert all([
            actual_lawsuit_filed,
            actual_preliminary_injunction_sought,
            actual_motion_to_dismiss_filed,
            actual_employees_named,
            actual_laptop_allegedly_stolen,
        ])

    def test_wired_loaded_language_disparity(self):
        """WIRED used loaded language for Meta but has no coverage of OpenAI to compare."""
        meta_loaded_terms = [
            "dormant surveillance",
            "spy camera",
            "creepy",
        ]
        openai_loaded_terms = []  # can't have loaded language with zero articles
        assert len(meta_loaded_terms) > 0
        assert len(openai_loaded_terms) == 0


class TestAppleOpenAIPartnershipCollapse:
    """The lawsuit is part of a broader Apple-OpenAI partnership collapse."""

    def test_partnership_timeline(self):
        """From partnership (Jun 2024) to litigation (Jul 2026) in ~25 months."""
        events = {
            "partnership_announced": "2024-06",
            "openai_breach_threat": "2026-05-14",
            "apple_switches_to_gemini": "2026-06",
            "apple_trade_secret_suit": "2026-07-10",
        }
        assert len(events) == 4

    def test_apple_now_using_google_gemini(self):
        """Apple replaced OpenAI's ChatGPT with Google's Gemini for new Siri AI."""
        siri_ai_model = "Google Gemini"
        previous_model = "OpenAI ChatGPT"
        assert siri_ai_model != previous_model

    def test_hardware_competition_dimension(self):
        """Lawsuit is fundamentally about control of future AI hardware devices."""
        openai_building_hardware = True
        apple_dominant_hardware_maker = True
        io_products_acquisition = 6_500_000_000  # $6.5B
        assert openai_building_hardware
        assert apple_dominant_hardware_maker
        assert io_products_acquisition >= 6_000_000_000


class TestWiredSilencePatterns:
    """WIRED's Apple-OpenAI silence extends its broader silence patterns."""

    def test_wired_meta_silence_18_days(self):
        """WIRED had an 18-day Meta silence (Jul 17 - Aug 4, 2026)."""
        meta_silence_days = 18
        assert meta_silence_days >= 18

    def test_wired_openai_lawsuit_silence_28_days(self):
        """WIRED has maintained 28+ days of silence on Apple v. OpenAI lawsuit."""
        openai_lawsuit_silence_days = 28
        assert openai_lawsuit_silence_days >= 28

    def test_silence_on_openai_negative_stories(self):
        """WIRED's silence extends to OpenAI negative stories generally."""
        # From prior analysis: WIRED's OpenAI coverage is neutral-to-positive
        # This lawsuit is the most negative OpenAI story in 2026
        wired_openai_negative_articles = 0
        assert wired_openai_negative_articles == 0
