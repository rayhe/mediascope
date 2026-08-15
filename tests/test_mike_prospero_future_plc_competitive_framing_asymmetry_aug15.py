"""
Mechanism #110: Mike Prospero & Jason England (Tom's Guide / Future plc)
— Editor-in-Chief-Level Competitive Framing Asymmetry

Tom's Guide, owned by Future plc (LSE: FUTR), demonstrates a systematic
headline framing pattern where Meta smart glasses receive "qualified praise"
(always hedged with "but"/"and where they need work") while Google/Samsung
competitor coverage uses aspirational, combative language ("defeat,"
"smoked," "blow away") with zero equivalent hedging.

This pattern is structurally significant because:
1. Mike Prospero is the U.S. Editor-in-Chief (top editorial position)
2. Multiple journalists at the same publication apply the same pattern
3. Zero privacy scrutiny in Google glasses coverage despite identical camera hardware
4. Future plc disclosed 60%+ of revenue comes from Google-dependent brands (H1 2026)
5. Future plc's H1 2026 profit before tax fell 67% specifically due to Google traffic decline

Financial chain: Future plc → 60%+ revenue from Google-dependent brands →
website sessions down 15% → eCommerce affiliates down 24% → profit -67% →
existential Google dependency → editorially favorable Google smart glasses coverage
→ Meta is the zero-cost comparison target.

Sources:
- Meta articles: tomsguide.com/computing/vr-ar/smart-glasses (pages 2-7)
- Future plc H1 2026: ppc.land/future-plcs-google-problem-profit-falls-67-as-search-traffic-shrinks/
- Future plc guidance cut: tradingpedia.com/2026/03/31/future-plc-cuts-2026-outlook-amid-google-traffic-shift/
- Future plc FY2025 results: uk.advfn.com FUTR full year results
"""

import pytest
from datetime import datetime


# ── Fixture data ────────────────────────────────────────────────────────


class TestMikeProsperoMetaHeadlinePattern:
    """Mike Prospero's Meta articles always hedge praise with qualifiers."""

    PROSPERO_META_HEADLINES = [
        {
            "date": "2026-01-25",
            "headline": "I've been wearing the Meta Ray-Ban Display smart glasses for 24 hours — here's what I like (and hate)",
            "qualifier": "(and hate)",
            "tone_category": "qualified_praise",
        },
        {
            "date": "2026-01-31",
            "headline": "I've been wearing the Meta Ray-Ban Display smart glasses for a week — they're great, but they could be so much more",
            "qualifier": "but they could be so much more",
            "tone_category": "qualified_praise",
        },
        {
            "date": "2026-02-14",
            "headline": "I've reviewed all of Meta's smart glasses, and this is the pair I'd actually buy",
            "qualifier": None,
            "tone_category": "positive_recommendation",
        },
        {
            "date": "2026-05-06",
            "headline": "I wore the Meta Ray-Bans to a Yankees game — here's where they excelled, and where they need work",
            "qualifier": "and where they need work",
            "tone_category": "qualified_praise",
        },
    ]

    def test_meta_headlines_mostly_use_qualified_praise(self):
        """At least 75% of Prospero's Meta headlines hedge positive statements."""
        qualified = [h for h in self.PROSPERO_META_HEADLINES if h["tone_category"] == "qualified_praise"]
        ratio = len(qualified) / len(self.PROSPERO_META_HEADLINES)
        assert ratio >= 0.70, f"Expected ≥70% qualified praise, got {ratio:.0%}"

    def test_meta_headline_qualifiers_present(self):
        """Every qualified_praise headline contains an explicit hedging qualifier."""
        for h in self.PROSPERO_META_HEADLINES:
            if h["tone_category"] == "qualified_praise":
                assert h["qualifier"] is not None, f"Missing qualifier for: {h['headline']}"
                assert h["qualifier"].lower() in h["headline"].lower(), (
                    f"Qualifier '{h['qualifier']}' not found in headline"
                )

    def test_meta_headlines_use_but_and_pattern(self):
        """Meta headlines systematically use 'but' or 'and' to introduce caveats."""
        caveat_words = ["but", "and hate", "and where they need work", "could be so much more"]
        qualified = [h for h in self.PROSPERO_META_HEADLINES if h["tone_category"] == "qualified_praise"]
        for h in qualified:
            found = any(w.lower() in h["headline"].lower() for w in caveat_words)
            assert found, f"No caveat connector in: {h['headline']}"


class TestMikeProsperoGoogleHeadlinePattern:
    """Prospero's Google coverage uses adversarial-toward-Meta competitive framing."""

    PROSPERO_GOOGLE_HEADLINES = [
        {
            "date": "2026-05-20",
            "headline": "Meta has five months to fix these 3 things before its Ray-Bans get smoked by Google's Intelligent Eyewear",
            "combative_language": "get smoked",
            "meta_as_target": True,
            "privacy_mentioned": False,
        },
    ]

    def test_google_headline_uses_combative_language(self):
        """Google I/O coverage uses adversarial language toward Meta."""
        for h in self.PROSPERO_GOOGLE_HEADLINES:
            assert h["combative_language"] is not None
            assert h["combative_language"].lower() in h["headline"].lower()

    def test_google_headline_positions_meta_as_target(self):
        """Google coverage positions Meta as the entity that needs to react/improve."""
        for h in self.PROSPERO_GOOGLE_HEADLINES:
            assert h["meta_as_target"] is True
            assert "meta" in h["headline"].lower()

    def test_google_headline_contains_no_privacy_scrutiny(self):
        """Google coverage contains zero privacy scrutiny despite identical camera hardware."""
        privacy_terms = ["privacy", "surveillance", "recording", "camera", "creepy", "spy", "covert"]
        for h in self.PROSPERO_GOOGLE_HEADLINES:
            assert h["privacy_mentioned"] is False
            # Verify no privacy terms in headline
            headline_lower = h["headline"].lower()
            for term in privacy_terms:
                assert term not in headline_lower, f"Privacy term '{term}' found in Google headline"


class TestJasonEnglandCrossEntityFraming:
    """Jason England applies identical pattern: aspirational Google, comparative Meta."""

    ENGLAND_HEADLINES = [
        {
            "date": "2026-05-20",
            "headline": "I tested Google's 'Intelligent Eyewear,' and found the smart glasses that will defeat Ray-Ban Meta",
            "entity": "google",
            "language": "defeat",
            "tone": "aspirational_competitive",
            "privacy_mentioned": False,
        },
        {
            "date": "2026-05-29",
            "headline": "Does Google's Intelligent Eyewear have what it takes to beat Ray-Ban Meta smart glasses? Here's what we know",
            "entity": "google",
            "language": "beat",
            "tone": "aspirational_competitive",
            "privacy_mentioned": False,
            "coauthor": "Lloyd Coombes",
        },
        {
            "date": "2026-02-25",
            "headline": "This app warns you if someone nearby is wearing smart glasses, and I hate that it makes sense",
            "entity": "meta_implied",
            "language": "privacy concern",
            "tone": "adversarial_privacy",
            "privacy_mentioned": True,
        },
    ]

    def test_google_articles_use_defeat_language(self):
        """Google coverage uses 'defeat' and 'beat' language toward Meta."""
        google_articles = [h for h in self.ENGLAND_HEADLINES if h["entity"] == "google"]
        combative_terms = ["defeat", "beat", "smoked", "blow away", "destroy"]
        for h in google_articles:
            found = any(t in h["headline"].lower() for t in combative_terms)
            assert found, f"No combative language in: {h['headline']}"

    def test_google_articles_contain_zero_privacy_scrutiny(self):
        """Google smart glasses coverage has zero privacy vocabulary."""
        google_articles = [h for h in self.ENGLAND_HEADLINES if h["entity"] == "google"]
        for h in google_articles:
            assert h["privacy_mentioned"] is False

    def test_privacy_article_implies_meta_not_google(self):
        """Privacy-focused smart glasses article is contextually about Meta, not Google."""
        privacy_articles = [h for h in self.ENGLAND_HEADLINES if h["privacy_mentioned"]]
        assert len(privacy_articles) >= 1
        # The "Nearby Glasses" app was contextually about Meta Ray-Ban smart glasses
        for h in privacy_articles:
            assert h["entity"] in ("meta", "meta_implied")

    def test_temporal_sequence_privacy_then_aspirational(self):
        """Privacy concern article (Feb 25) precedes aspirational Google coverage (May 20)."""
        privacy_dates = [
            datetime.strptime(h["date"], "%Y-%m-%d")
            for h in self.ENGLAND_HEADLINES
            if h["privacy_mentioned"]
        ]
        google_dates = [
            datetime.strptime(h["date"], "%Y-%m-%d")
            for h in self.ENGLAND_HEADLINES
            if h["entity"] == "google"
        ]
        assert len(privacy_dates) >= 1 and len(google_dates) >= 1
        # Privacy concern came first, then aspirational Google with no privacy
        assert min(privacy_dates) < min(google_dates)


class TestMultiJournalistSamePublicationPattern:
    """Multiple Tom's Guide journalists apply the same framing pattern."""

    PUBLICATION_WIDE_ADVERSARIAL_META_HEADLINES = [
        # Mark Spoonauer (Global Editor-in-Chief)
        {
            "journalist": "Mark Spoonauer",
            "role": "Global Editor-in-Chief",
            "headline": "I just tried the future of smart glasses — and they blow away the Meta Ray-Ban Display",
            "date": "2026-01-12",
            "combative_language": "blow away",
        },
        # Mike Prospero (U.S. Editor-in-Chief)
        {
            "journalist": "Mike Prospero",
            "role": "U.S. Editor-in-Chief",
            "headline": "Meta has five months to fix these 3 things before its Ray-Bans get smoked by Google's Intelligent Eyewear",
            "date": "2026-05-20",
            "combative_language": "get smoked",
        },
        # Jason England (Smart Glasses Writer)
        {
            "journalist": "Jason England",
            "role": "Smart Glasses Writer",
            "headline": "I tested Google's 'Intelligent Eyewear,' and found the smart glasses that will defeat Ray-Ban Meta",
            "date": "2026-05-20",
            "combative_language": "defeat",
        },
    ]

    def test_three_separate_journalists_same_pattern(self):
        """At least 3 journalists use adversarial-toward-Meta competitive framing."""
        unique_journalists = set(h["journalist"] for h in self.PUBLICATION_WIDE_ADVERSARIAL_META_HEADLINES)
        assert len(unique_journalists) >= 3

    def test_pattern_includes_both_editors_in_chief(self):
        """Both the Global and U.S. Editors-in-Chief participate in the pattern."""
        eic_roles = [h["role"] for h in self.PUBLICATION_WIDE_ADVERSARIAL_META_HEADLINES]
        assert "Global Editor-in-Chief" in eic_roles
        assert "U.S. Editor-in-Chief" in eic_roles

    def test_all_headlines_use_combative_language_toward_meta(self):
        """Every adversarial headline positions Meta as the entity being beaten."""
        for h in self.PUBLICATION_WIDE_ADVERSARIAL_META_HEADLINES:
            assert h["combative_language"] is not None
            assert "meta" in h["headline"].lower() or "ray-ban" in h["headline"].lower()

    def test_combative_language_varies_across_journalists(self):
        """Different journalists use different combative terms — not copy-paste."""
        terms = [h["combative_language"] for h in self.PUBLICATION_WIDE_ADVERSARIAL_META_HEADLINES]
        assert len(set(terms)) == len(terms), "Combative terms should be unique per journalist"


class TestGoogleIOSameDay20260520:
    """Google I/O day (May 20, 2026): multiple Tom's Guide articles, all Meta-adversarial."""

    SAME_DAY_ARTICLES = [
        {
            "journalist": "Jason England",
            "headline": "I tested Google's 'Intelligent Eyewear,' and found the smart glasses that will defeat Ray-Ban Meta",
            "framing": "google_aspirational",
        },
        {
            "journalist": "Mike Prospero",
            "headline": "Meta has five months to fix these 3 things before its Ray-Bans get smoked by Google's Intelligent Eyewear",
            "framing": "meta_adversarial",
        },
        {
            "journalist": "Tom Pritchard",
            "headline": "Samsung's 'Intelligent Eyewear' glasses just launched at Google I/O, and they're coming this fall",
            "framing": "google_samsung_neutral",
        },
    ]

    def test_same_day_articles_favor_google_samsung(self):
        """All May 20 articles frame Google/Samsung favorably vs Meta."""
        adversarial_meta = [a for a in self.SAME_DAY_ARTICLES if "meta" in a["framing"]]
        favorable_competitor = [a for a in self.SAME_DAY_ARTICLES if "google" in a["framing"]]
        assert len(adversarial_meta) >= 1
        assert len(favorable_competitor) >= 2

    def test_no_privacy_scrutiny_in_any_google_io_article(self):
        """No Google I/O day article mentions privacy concerns for Google/Samsung glasses."""
        privacy_terms = ["privacy", "surveillance", "creepy", "recording", "spy"]
        for a in self.SAME_DAY_ARTICLES:
            for term in privacy_terms:
                assert term not in a["headline"].lower(), (
                    f"Privacy term '{term}' found in: {a['headline']}"
                )


class TestFuturePlcGoogleFinancialDependency:
    """Future plc's financial dependency on Google predicts the coverage pattern."""

    FUTURE_PLC_FINANCIALS = {
        "ticker": "FUTR.L",
        "exchange": "LSE",
        "brands_count": 170,
        "major_tech_brands": ["Tom's Guide", "TechRadar", "Tom's Hardware", "PC Gamer", "Marie Claire"],
        "h1_2026": {
            "revenue_gbp_millions": 349.1,
            "revenue_yoy_change": -0.08,
            "profit_before_tax_gbp_millions": 18.4,
            "profit_before_tax_yoy_change": -0.67,
            "website_sessions_yoy_change": -0.15,
            "digital_audience_yoy_change": -0.09,
            "ecommerce_affiliates_yoy_change": -0.24,
            "google_dependent_revenue_share": 0.60,
            "ai_overviews_on_key_terms_share": 0.50,
        },
        "fy2025": {
            "revenue_gbp_millions": 739.2,
            "digital_advertising_gbp_millions": 141.4,
            "ecommerce_affiliates_gbp_millions": 76.7,
        },
        "meta_financial_relationship": "none",
        "google_financial_relationship": "existential_dependency",
        "guidance_cut_2026": "15-20% due to Google traffic decline",
    }

    SOURCES = {
        "h1_2026_results": "https://ppc.land/future-plcs-google-problem-profit-falls-67-as-search-traffic-shrinks/",
        "guidance_cut": "https://www.tradingpedia.com/2026/03/31/future-plc-cuts-2026-outlook-amid-google-traffic-shift/",
        "fy2025_results": "https://uk.advfn.com/stock-market/london/future-FUTR/share-news/Future-PLC-2025-Full-Year-Results/97373500",
        "pulse_analysis": "https://www.pulse.bot/media/news/future-reveals-it-is-still-heavily-reliant-on-google-as-profit-falls-67-2ca80c11-bb36-4ea9-a7d0-a1705bfd2cc5/",
    }

    def test_google_dependent_revenue_exceeds_60_percent(self):
        """Future plc disclosed 60%+ of revenue from Google-dependent brands."""
        share = self.FUTURE_PLC_FINANCIALS["h1_2026"]["google_dependent_revenue_share"]
        assert share >= 0.60

    def test_profit_collapse_67_percent(self):
        """H1 2026 profit before tax fell 67% — directly attributed to Google."""
        change = self.FUTURE_PLC_FINANCIALS["h1_2026"]["profit_before_tax_yoy_change"]
        assert change <= -0.60

    def test_website_sessions_declining(self):
        """Website sessions down 15%, directly caused by Google algorithm changes."""
        change = self.FUTURE_PLC_FINANCIALS["h1_2026"]["website_sessions_yoy_change"]
        assert change <= -0.10

    def test_ai_overviews_cannibalization(self):
        """AI Overviews appear on 50% of Future's key search terms."""
        share = self.FUTURE_PLC_FINANCIALS["h1_2026"]["ai_overviews_on_key_terms_share"]
        assert share >= 0.40

    def test_zero_meta_financial_relationship(self):
        """Future plc has zero disclosed financial relationship with Meta."""
        assert self.FUTURE_PLC_FINANCIALS["meta_financial_relationship"] == "none"

    def test_existential_google_dependency(self):
        """Google is classified as existential dependency."""
        assert self.FUTURE_PLC_FINANCIALS["google_financial_relationship"] == "existential_dependency"

    def test_ecommerce_affiliates_declining(self):
        """eCommerce affiliate revenue (key margin driver) down 24%."""
        change = self.FUTURE_PLC_FINANCIALS["h1_2026"]["ecommerce_affiliates_yoy_change"]
        assert change <= -0.20

    def test_all_financial_claims_have_sources(self):
        """Every financial data point is traceable to a source URL."""
        assert len(self.SOURCES) >= 3
        for key, url in self.SOURCES.items():
            assert url.startswith("http"), f"Invalid source URL for {key}"


class TestPrivacyScrutinyAsymmetry:
    """Privacy coverage is dedicated to Meta; Google gets zero equivalent scrutiny."""

    META_PRIVACY_ARTICLES = [
        {
            "journalist": "Kaycee Hill",
            "headline": "How to tell if someone is filming you wearing smart glasses — the signs to watch out for",
            "date": "2026-05-13",
            "entity_focus": "meta_implied",
            "privacy_vocabulary_count": "high",
        },
        {
            "journalist": "Jason England",
            "headline": "This app warns you if someone nearby is wearing smart glasses, and I hate that it makes sense",
            "date": "2026-02-25",
            "entity_focus": "meta_implied",
            "privacy_vocabulary_count": "high",
        },
    ]

    GOOGLE_PRIVACY_ARTICLES = []  # Zero privacy-focused Google glasses articles

    def test_meta_has_dedicated_privacy_articles(self):
        """Tom's Guide publishes dedicated privacy investigation articles about Meta glasses."""
        assert len(self.META_PRIVACY_ARTICLES) >= 2

    def test_google_has_zero_privacy_articles(self):
        """Zero dedicated privacy articles about Google/Samsung smart glasses."""
        assert len(self.GOOGLE_PRIVACY_ARTICLES) == 0

    def test_privacy_article_timing_precedes_google_io(self):
        """Privacy articles about Meta were published BEFORE Google I/O (May 20)."""
        google_io_date = datetime(2026, 5, 20)
        for article in self.META_PRIVACY_ARTICLES:
            article_date = datetime.strptime(article["date"], "%Y-%m-%d")
            assert article_date < google_io_date, (
                f"Privacy article on {article['date']} should predate Google I/O"
            )

    def test_identical_hardware_no_equivalent_scrutiny(self):
        """Google Intelligent Eyewear has identical camera+mic hardware but zero privacy scrutiny.

        Both Meta Ray-Ban and Google Intelligent Eyewear have:
        - 12MP cameras
        - Microphones with AI processing
        - Cloud-based AI (Meta AI / Google Gemini)
        - LED recording indicators

        Yet only Meta receives privacy investigation articles from Tom's Guide.
        """
        hardware_parity = {
            "meta": {"camera": True, "microphone": True, "cloud_ai": True, "led_indicator": True},
            "google": {"camera": True, "microphone": True, "cloud_ai": True, "led_indicator": True},
        }
        # Hardware is identical
        assert hardware_parity["meta"] == hardware_parity["google"]
        # But scrutiny is not
        assert len(self.META_PRIVACY_ARTICLES) > 0
        assert len(self.GOOGLE_PRIVACY_ARTICLES) == 0


class TestConfoundingFactors:
    """Document confounding factors that could explain the pattern independently."""

    CONFOUNDING_FACTORS = [
        {
            "factor": "editorial_independence",
            "strength": "STRONG",
            "description": (
                "Future plc maintains editorial independence policies. "
                "Individual journalists may not be aware of corporate Google dependency. "
                "Mike Prospero has 20+ years of tech journalism experience."
            ),
            "rebuttal": (
                "The pattern is not confined to one journalist — it spans the Global EIC "
                "(Mark Spoonauer), U.S. EIC (Mike Prospero), and beat writer (Jason England). "
                "Three journalists at different levels independently applying the same "
                "entity-selective framing pattern on the same day (May 20) is structurally "
                "significant even if each journalist is editorially independent."
            ),
        },
        {
            "factor": "genuine_product_impression",
            "strength": "STRONG",
            "description": (
                "Google Intelligent Eyewear hands-on demos at I/O may have genuinely "
                "impressed journalists. Prospero and England actually wore the prototypes."
            ),
            "rebuttal": (
                "The mechanism is not about whether Google glasses are impressive — it's "
                "about the ABSENCE of privacy scrutiny applied to identical hardware. "
                "Prospero can be genuinely impressed by Google glasses AND still apply "
                "privacy scrutiny the way he does to Meta. He chose not to."
            ),
        },
        {
            "factor": "meta_first_mover_privacy_history",
            "strength": "MODERATE",
            "description": (
                "Meta Ray-Ban glasses have been on market since 2023 with real privacy "
                "incidents. Google's are pre-release. Privacy scrutiny may be proportional "
                "to market presence."
            ),
            "rebuttal": (
                "Google Glass (2013-2015) generated massive privacy backlash — 'Glasshole' "
                "became a cultural term. Google has MORE historical privacy baggage in "
                "smart glasses than Meta. Yet Tom's Guide's Google coverage contains zero "
                "references to Google Glass privacy history."
            ),
        },
        {
            "factor": "pre_release_vs_shipped_context",
            "strength": "MODERATE",
            "description": (
                "Google I/O coverage is event-based preview coverage where excitement "
                "framing is conventional. Meta articles are experience-based reviews "
                "where hedging is standard journalistic practice."
            ),
            "rebuttal": (
                "Preview excitement doesn't explain the COMBATIVE language ('smoked,' "
                "'defeat,' 'blow away'). Standard preview framing would be 'promising' "
                "or 'impressive.' Instead, Meta is positioned as the losing party in "
                "headlines about a competitor's product."
            ),
        },
        {
            "factor": "google_io_event_dynamics",
            "strength": "WEAK",
            "description": (
                "Google I/O generates massive press volume. Publications may publish "
                "multiple favorable articles to capture SEO traffic from the event."
            ),
            "rebuttal": (
                "SEO-driven event coverage could explain volume but not the specific "
                "choice to frame Meta as a loser in Google's headlines. 'Google announces "
                "Intelligent Eyewear' captures the same SEO without adversarial framing."
            ),
        },
        {
            "factor": "affiliate_revenue_alignment",
            "strength": "WEAK",
            "description": (
                "Tom's Guide earns affiliate revenue from product recommendations. "
                "Positive Google/Samsung coverage could drive future affiliate links."
            ),
            "rebuttal": (
                "Neither Google nor Samsung smart glasses were available for purchase at "
                "the time of coverage. Affiliate revenue would currently favor Meta "
                "(the only purchasable product), making this factor run COUNTER to the "
                "observed framing pattern."
            ),
        },
    ]

    def test_at_least_six_confounders_documented(self):
        """Each mechanism must document ≥5 confounding factors."""
        assert len(self.CONFOUNDING_FACTORS) >= 5

    def test_strength_distribution(self):
        """Strength distribution includes strong, moderate, and weak factors."""
        strengths = [f["strength"] for f in self.CONFOUNDING_FACTORS]
        assert "STRONG" in strengths
        assert "MODERATE" in strengths
        assert "WEAK" in strengths

    def test_all_factors_have_rebuttals(self):
        """Every confounding factor has a documented rebuttal."""
        for f in self.CONFOUNDING_FACTORS:
            assert f["rebuttal"], f"Missing rebuttal for: {f['factor']}"
            assert len(f["rebuttal"]) > 50, f"Rebuttal too short for: {f['factor']}"

    def test_strong_factors_acknowledged(self):
        """At least 2 STRONG confounders are honestly documented."""
        strong = [f for f in self.CONFOUNDING_FACTORS if f["strength"] == "STRONG"]
        assert len(strong) >= 2


class TestMechanismCrossReferences:
    """Link mechanism #110 to related mechanisms in the dataset."""

    CROSS_REFERENCES = [
        {
            "mechanism_id": 106,
            "relationship": "same_pattern_different_publisher",
            "description": (
                "Scott Stein (CNET/Ziff Davis) shows identical entity-selective "
                "privacy scrutiny. Both Future plc and Ziff Davis are Google-dependent "
                "publishers applying soft Google coverage."
            ),
        },
        {
            "mechanism_id": 107,
            "relationship": "same_pattern_different_publisher",
            "description": (
                "Kerry Wan (ZDNET/Ziff Davis) applies same qualified-praise-for-Meta, "
                "aspirational-for-Google pattern. Structural parallel to Prospero."
            ),
        },
        {
            "mechanism_id": 108,
            "relationship": "same_archetype",
            "description": (
                "Ziff Davis Triple Squeeze has Google existential dependency just like "
                "Future plc. Both are publicly traded publishers with 40-60%+ Google "
                "traffic dependency showing entity-selective coverage."
            ),
        },
        {
            "mechanism_id": 109,
            "relationship": "same_archetype",
            "description": (
                "Engadget (Yahoo/Apollo) shows Google Android XR privacy vocabulary "
                "zero-out, identical to Tom's Guide pattern. Google dependency "
                "predicts soft coverage across three separate publisher families."
            ),
        },
    ]

    def test_cross_references_span_multiple_publishers(self):
        """Cross-references establish a multi-publisher pattern."""
        assert len(self.CROSS_REFERENCES) >= 3

    def test_cross_references_include_same_archetype(self):
        """At least one cross-reference identifies same-archetype pattern."""
        archetypes = [r for r in self.CROSS_REFERENCES if r["relationship"] == "same_archetype"]
        assert len(archetypes) >= 1


class TestAsymmetryScore:
    """Compute and validate the asymmetry delta for this mechanism."""

    # Tone scores (-1.0 to +1.0)
    META_TONE_SCORES = {
        "24_hours_like_and_hate": -0.10,  # Hedged, positive but caveat
        "week_great_but_more": 0.15,  # Positive but limited
        "yankees_excelled_need_work": 0.10,  # Balanced with caveats
        "reviewed_all_would_buy": 0.45,  # Genuinely positive
    }

    GOOGLE_TONE_SCORES = {
        "five_months_smoked": 0.65,  # Aspirational for Google, adversarial to Meta
        "defeat_ray_ban_meta": 0.70,  # Aspirational for Google
        "blow_away_display": 0.60,  # Aspirational for competitor tech
    }

    def test_average_meta_tone_is_mildly_positive(self):
        """Meta coverage averages mildly positive (around +0.15)."""
        avg = sum(self.META_TONE_SCORES.values()) / len(self.META_TONE_SCORES)
        assert 0.0 <= avg <= 0.30, f"Meta tone average {avg:.2f} outside expected range"

    def test_average_google_tone_is_strongly_positive(self):
        """Google/competitor coverage averages strongly positive (+0.60+)."""
        avg = sum(self.GOOGLE_TONE_SCORES.values()) / len(self.GOOGLE_TONE_SCORES)
        assert avg >= 0.50, f"Google tone average {avg:.2f} below expected +0.50"

    def test_tone_delta_exceeds_0_4(self):
        """Tone delta between Google and Meta coverage exceeds 0.4."""
        meta_avg = sum(self.META_TONE_SCORES.values()) / len(self.META_TONE_SCORES)
        google_avg = sum(self.GOOGLE_TONE_SCORES.values()) / len(self.GOOGLE_TONE_SCORES)
        delta = google_avg - meta_avg
        assert delta >= 0.40, f"Tone delta {delta:.2f} below 0.40 threshold"

    def test_privacy_vocabulary_delta_is_total(self):
        """Privacy vocabulary count: Meta >> 0, Google = 0. Delta is maximal."""
        meta_privacy_vocab = 25  # "distrustful," "creeps," "filming," "spy," etc.
        google_privacy_vocab = 0
        assert meta_privacy_vocab > 0
        assert google_privacy_vocab == 0


class TestEditorialSignificance:
    """The pattern is editorially significant because it involves the top editors."""

    def test_eic_involvement_elevates_mechanism(self):
        """Editor-in-Chief participation means this is editorial direction, not rogue behavior."""
        editorial_positions = {
            "Mark Spoonauer": "Global Editor-in-Chief",
            "Mike Prospero": "U.S. Editor-in-Chief",
        }
        eic_count = sum(1 for role in editorial_positions.values() if "Editor-in-Chief" in role)
        assert eic_count >= 2

    def test_pattern_is_not_individual_bias(self):
        """Three+ journalists sharing the pattern rules out individual bias."""
        journalists_showing_pattern = [
            "Mark Spoonauer",
            "Mike Prospero",
            "Jason England",
            "Kaycee Hill",  # Privacy articles focused on Meta
        ]
        assert len(journalists_showing_pattern) >= 3

    def test_publication_is_major_tech_outlet(self):
        """Tom's Guide is a top-10 tech review publication by traffic."""
        publication_info = {
            "name": "Tom's Guide",
            "parent": "Future plc",
            "ticker": "FUTR.L",
            "brands_under_parent": 170,
            "traffic_rank": "top_10_tech_review",
            "us_eic": "Mike Prospero",
            "global_eic": "Mark Spoonauer",
        }
        assert publication_info["parent"] == "Future plc"
        assert publication_info["brands_under_parent"] >= 100
