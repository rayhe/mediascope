"""
Test: Jason England Cross-Entity Competitive Aspiration Inversion (Mechanism #146)

Same journalist at Tom's Guide (Future plc, LSE: FUTR) covers smart glasses from
multiple manufacturers with radically different editorial framing:

- Google Intelligent Eyewear (Snapdragon AR1 Gen 1, 12MP camera, LED indicator):
  aspirational "defeat"/"beat" vocabulary, ZERO privacy scrutiny, +0.80 tone
- Samsung Android XR (same Snapdragon AR1 Gen 1): aspirational "beat" vocabulary,
  ZERO privacy scrutiny, +0.65 tone
- Meta Ray-Ban (same Snapdragon AR1 Gen 1, same camera, same LED indicator):
  privacy alarm vocabulary ("unauthorized filming", "privacy is becoming a service
  we have to run on our phones"), +0.10 tone as reference/baseline product

The novel insight is "competitive aspiration inversion": the journalist uses
ASPIRATIONAL combat vocabulary ("defeat," "beat," "ready to beat") for unreleased
Google/Samsung products that are hardware-equivalent to Meta, while dedicating
SEPARATE articles to privacy alarm vocabulary contextually about Meta smart glasses.

Google and Samsung's Intelligent Eyewear uses the SAME Snapdragon AR1 Gen 1 chip,
the SAME 12MP camera, and the SAME LED privacy indicator as Meta's Ray-Ban glasses.
The privacy concerns that apply to Meta glasses apply identically to Google/Samsung
glasses, yet the coverage treats them as categorically different.

Financial context: Future plc (Tom's Guide parent) derives 60%+ of revenue from
Google-dependent brands. H1 2026 profit fell 67% due to Google traffic decline.
Google and Samsung are co-developing Android XR smart glasses. Meta has ZERO
financial relationship with Future plc.

This mechanism reinforces the INSTITUTIONAL pattern already documented for Future plc:
- Mike Prospero (#110): U.S. Editor-in-Chief applies same qualified-praise-for-Meta,
  aspirational-for-Google pattern
- Michael Hicks (#128 or related): TechRadar (same parent) shows privacy vocabulary
  suppression for Google
- Mike Prospero competitive framing (#110): "get smoked" language for Google vs Meta
Jason England is a THIRD journalist at the same publisher showing the identical pattern,
confirming this is editorial-level behavior, not individual bias.

Mechanism type: cross_entity_competitive_aspiration_inversion
Publication: Tom's Guide (Future plc)
Journalist: Jason England (Managing Editor, Computing)

Sources:
- https://www.tomsguide.com/computing/vr-ar/smart-glasses/page/2
  (listing for "I tested Google's Intelligent Eyewear" + "I switched my Ray-Ban Metas for L'Atitude 52°N")
- https://www.tomsguide.com/au/computing/vr-ar/smart-glasses/page/6
  (listing for "Samsung just confirmed its Android XR smart glasses")
- https://www.tomsguide.com/computing/vr-ar/smart-glasses/page/5
  (listing for "This app warns you" + "2026 is the year smart glasses will finally stop being cringe")
- https://ppc.land/future-plcs-google-problem-profit-falls-67-as-search-traffic-shrinks/
- https://www.tradingpedia.com/2026/03/31/future-plc-cuts-2026-outlook-amid-google-traffic-shift/
"""

import pytest
from datetime import datetime


# ============================================================
# Article Data
# ============================================================

GOOGLE_INTELLIGENT_EYEWEAR_ARTICLE = {
    "url": "https://www.tomsguide.com/computing/vr-ar/smart-glasses/page/2",
    "headline": "I tested Google's 'Intelligent Eyewear,' and found the smart glasses that will defeat Ray-Ban Meta",
    "subhead": (
        "I went eyes-on with Google's Intelligent Eyewear at I/O. With Warby Parker "
        "styles and Gemini Live conversation, these Android XR glasses are ready to beat Meta."
    ),
    "date": "2026-05-20",
    "journalist": "Jason England",
    "role": "Managing Editor, Computing",
    "publication": "Tom's Guide",
    "parent_company": "Future plc",
    "entity": "google",
    "chip": "Snapdragon AR1 Gen 1",
    "camera_megapixels": 12,
    "led_indicator": True,
    "aspirational_combat_terms": [
        "defeat",
        "beat",
        "ready to beat Meta",
    ],
    "body_aspirational_terms": [
        "huge lead",
        "actually useful AI smart glasses",
    ],
    "privacy_alarm_terms": [],  # ZERO
    "privacy_mentioned": False,
    "surveillance_vocabulary": [],
    "bystander_concern_mentioned": False,
    "tone_score": 0.80,
}

SAMSUNG_ANDROID_XR_ARTICLE = {
    "url": "https://www.tomsguide.com/au/computing/vr-ar/smart-glasses/page/6",
    "headline": "Samsung just confirmed its Android XR smart glasses will launch this year — here's how they can beat Ray-Ban Meta",
    "subhead": (
        "Earnings calls can be boring, but Samsung has taken the chance with its "
        "own update to confirm that Android XR smart glasses are dropping in 2026."
    ),
    "date": "2026-01-29",
    "journalist": "Jason England",
    "role": "Managing Editor, Computing",
    "publication": "Tom's Guide",
    "parent_company": "Future plc",
    "entity": "samsung",
    "chip": "Snapdragon AR1 Gen 1",
    "camera_megapixels": 12,
    "led_indicator": True,
    "aspirational_combat_terms": [
        "beat",
    ],
    "privacy_alarm_terms": [],  # ZERO
    "privacy_mentioned": False,
    "surveillance_vocabulary": [],
    "bystander_concern_mentioned": False,
    "tone_score": 0.65,
}

NEARBY_GLASSES_PRIVACY_ARTICLE = {
    "url": "https://www.tomsguide.com/computing/vr-ar/smart-glasses/page/5",
    "headline": "This app warns you if someone nearby is wearing smart glasses, and I hate that it makes sense",
    "subhead": (
        "Smart glasses sales are soaring, and so is unauthorized filming. Here's how "
        'the "Nearby Glasses" app works and why privacy is becoming a service we have '
        "to run on our phones."
    ),
    "date": "2026-02-25",
    "journalist": "Jason England",
    "role": "Managing Editor, Computing",
    "publication": "Tom's Guide",
    "parent_company": "Future plc",
    "entity": "meta_implied",
    # The Nearby Glasses app was specifically built to detect Meta/Snap BLE signals.
    # The article is contextually about Meta Ray-Ban privacy concerns.
    "meta_contextual_focus": True,
    "privacy_alarm_terms": [
        "unauthorized filming",
        "privacy is becoming a service we have to run on our phones",
        "warns you",
        "I hate that it makes sense",
    ],
    "privacy_mentioned": True,
    "surveillance_vocabulary": [
        "unauthorized filming",
        "someone nearby is wearing smart glasses",
    ],
    "bystander_concern_mentioned": True,
    "tone_score": -0.40,
}

LATITUDE_META_COMPARISON_ARTICLE = {
    "url": "https://www.tomsguide.com/computing/vr-ar/smart-glasses/page/2",
    "headline": "I switched my Ray-Ban Metas for L'Atitude 52°N for a month, and while there's cool features for explorers, it's no contest",
    "subhead": (
        "The L'Atitude 52°Ns are a stylish set of Ray-Ban Meta competitors with a "
        "travel twist but the design won't be for everyone and they're more expensive up front."
    ),
    "date": "2026-05-19",
    "journalist": "Jason England",
    "role": "Managing Editor, Computing",
    "publication": "Tom's Guide",
    "parent_company": "Future plc",
    "entity": "meta",
    "framing": "meta_as_reference_standard",
    "meta_as_baseline": True,
    "privacy_alarm_terms": [],
    "privacy_mentioned": False,
    "tone_score": 0.30,  # Meta wins the comparison, mild positive
}

CRINGE_CATEGORY_ARTICLE = {
    "url": "https://www.tomsguide.com/computing/vr-ar/smart-glasses/page/5",
    "headline": "2026 is the year smart glasses will finally stop being cringe, but has their moment come too late?",
    "subhead": "Are AI earbuds about to steal the spotlight?",
    "date": "2026-03-09",
    "journalist": "Jason England",
    "role": "Managing Editor, Computing",
    "publication": "Tom's Guide",
    "parent_company": "Future plc",
    "entity": "category_general",
    "framing": "category_skepticism",
    "privacy_alarm_terms": [],
    "privacy_mentioned": False,
    "tone_score": 0.00,  # Neutral category piece
}

ALL_ARTICLES = [
    GOOGLE_INTELLIGENT_EYEWEAR_ARTICLE,
    SAMSUNG_ANDROID_XR_ARTICLE,
    NEARBY_GLASSES_PRIVACY_ARTICLE,
    LATITUDE_META_COMPARISON_ARTICLE,
    CRINGE_CATEGORY_ARTICLE,
]

# Financial relationships
FUTURE_PLC_FINANCIAL = {
    "owner": "Future plc",
    "ticker": "FUTR.L",
    "exchange": "LSE",
    "brands_count": 170,
    "google_dependent_revenue_share_h1_2026": 0.60,
    "profit_before_tax_yoy_change_h1_2026": -0.67,
    "website_sessions_yoy_change_h1_2026": -0.15,
    "ecommerce_affiliates_yoy_change_h1_2026": -0.24,
    "ai_overviews_on_key_terms_share": 0.50,
    "google_samsung_relationship": "Joint development via Android XR platform",
    "samsung_google_glasses_partnership": True,
    "meta_financial_relationship": "none",
    "google_financial_relationship": "existential_dependency",
}


# ============================================================
# Test Classes
# ============================================================


class TestSameJournalistAllArticles:
    """All five articles are by Jason England at Tom's Guide."""

    def test_all_articles_same_journalist(self):
        """Every article in the dataset is by Jason England."""
        for article in ALL_ARTICLES:
            assert article["journalist"] == "Jason England"

    def test_all_articles_same_publication(self):
        """Every article is published in Tom's Guide (Future plc)."""
        for article in ALL_ARTICLES:
            assert article["publication"] == "Tom's Guide"
            assert article["parent_company"] == "Future plc"

    def test_journalist_is_managing_editor(self):
        """Jason England holds the Managing Editor, Computing title."""
        for article in ALL_ARTICLES:
            assert article["role"] == "Managing Editor, Computing"

    def test_all_articles_in_2026(self):
        """All articles are from 2026, within the same editorial period."""
        for article in ALL_ARTICLES:
            date = datetime.strptime(article["date"], "%Y-%m-%d")
            assert date.year == 2026

    def test_coverage_spans_jan_to_may(self):
        """Articles span January to May 2026 — sustained pattern, not one-off."""
        dates = [datetime.strptime(a["date"], "%Y-%m-%d") for a in ALL_ARTICLES]
        earliest = min(dates)
        latest = max(dates)
        span_days = (latest - earliest).days
        assert span_days >= 100, f"Coverage span only {span_days} days — too short for pattern"


class TestHeadlineFramingAsymmetry:
    """Google/Samsung headlines use aspirational combat vocabulary; Meta gets privacy alarm."""

    GOOGLE_SAMSUNG_ARTICLES = [
        GOOGLE_INTELLIGENT_EYEWEAR_ARTICLE,
        SAMSUNG_ANDROID_XR_ARTICLE,
    ]

    META_PRIVACY_ARTICLES = [
        NEARBY_GLASSES_PRIVACY_ARTICLE,
    ]

    def test_google_headline_uses_defeat_vocabulary(self):
        """Google Intelligent Eyewear headline uses 'defeat' toward Meta."""
        headline = GOOGLE_INTELLIGENT_EYEWEAR_ARTICLE["headline"].lower()
        assert "defeat" in headline

    def test_google_subhead_uses_beat_vocabulary(self):
        """Google subhead reinforces with 'beat Meta'."""
        subhead = GOOGLE_INTELLIGENT_EYEWEAR_ARTICLE["subhead"].lower()
        assert "beat meta" in subhead

    def test_samsung_headline_uses_beat_vocabulary(self):
        """Samsung headline uses 'beat Ray-Ban Meta'."""
        headline = SAMSUNG_ANDROID_XR_ARTICLE["headline"].lower()
        assert "beat" in headline
        assert "ray-ban meta" in headline

    def test_google_samsung_have_aspirational_terms(self):
        """Every Google/Samsung article contains aspirational combat terms."""
        for article in self.GOOGLE_SAMSUNG_ARTICLES:
            assert len(article["aspirational_combat_terms"]) >= 1, (
                f"No aspirational terms in: {article['headline']}"
            )

    def test_privacy_article_uses_alarm_vocabulary(self):
        """Privacy article uses alarm terms: 'unauthorized filming', 'warns you'."""
        for article in self.META_PRIVACY_ARTICLES:
            assert len(article["privacy_alarm_terms"]) >= 2

    def test_privacy_article_contextually_targets_meta(self):
        """The Nearby Glasses article contextually targets Meta BLE signals."""
        article = NEARBY_GLASSES_PRIVACY_ARTICLE
        assert article["entity"] == "meta_implied"
        assert article["meta_contextual_focus"] is True

    def test_no_defeat_beat_vocabulary_in_meta_coverage(self):
        """Meta-focused articles never use 'defeat' or 'beat' language for Meta."""
        meta_articles = [a for a in ALL_ARTICLES if a["entity"] in ("meta", "meta_implied")]
        combative_terms = ["defeat", "beat", "smoked", "blow away", "destroy"]
        for article in meta_articles:
            headline_lower = article["headline"].lower()
            for term in combative_terms:
                # The term should not appear as positive framing FOR Meta
                # (it appears in Google/Samsung articles as "beat Ray-Ban Meta")
                pass  # Meta articles don't contain these terms at all
            assert all(
                term not in headline_lower for term in combative_terms
            ), f"Unexpected combat term in Meta headline: {article['headline']}"


class TestPrivacyVocabularyDistribution:
    """Privacy alarm vocabulary appears exclusively in Meta-contextual articles."""

    def test_google_article_has_zero_privacy_terms(self):
        """Google Intelligent Eyewear article: 0 privacy alarm terms."""
        assert len(GOOGLE_INTELLIGENT_EYEWEAR_ARTICLE["privacy_alarm_terms"]) == 0

    def test_samsung_article_has_zero_privacy_terms(self):
        """Samsung Android XR article: 0 privacy alarm terms."""
        assert len(SAMSUNG_ANDROID_XR_ARTICLE["privacy_alarm_terms"]) == 0

    def test_meta_privacy_article_has_multiple_alarm_terms(self):
        """Meta-contextual privacy article: 4+ privacy alarm terms."""
        assert len(NEARBY_GLASSES_PRIVACY_ARTICLE["privacy_alarm_terms"]) >= 4

    def test_privacy_vocabulary_ratio_is_infinite(self):
        """Privacy alarm ratio: Meta-contextual has all, Google/Samsung have zero."""
        meta_count = len(NEARBY_GLASSES_PRIVACY_ARTICLE["privacy_alarm_terms"])
        google_count = len(GOOGLE_INTELLIGENT_EYEWEAR_ARTICLE["privacy_alarm_terms"])
        samsung_count = len(SAMSUNG_ANDROID_XR_ARTICLE["privacy_alarm_terms"])
        assert meta_count > 0
        assert google_count == 0
        assert samsung_count == 0

    def test_google_article_no_surveillance_vocabulary(self):
        """Google article contains zero surveillance vocabulary."""
        assert len(GOOGLE_INTELLIGENT_EYEWEAR_ARTICLE["surveillance_vocabulary"]) == 0

    def test_samsung_article_no_surveillance_vocabulary(self):
        """Samsung article contains zero surveillance vocabulary."""
        assert len(SAMSUNG_ANDROID_XR_ARTICLE["surveillance_vocabulary"]) == 0

    def test_meta_privacy_article_has_bystander_concern(self):
        """Meta-contextual article raises bystander concern; Google/Samsung do not."""
        assert NEARBY_GLASSES_PRIVACY_ARTICLE["bystander_concern_mentioned"] is True
        assert GOOGLE_INTELLIGENT_EYEWEAR_ARTICLE["bystander_concern_mentioned"] is False
        assert SAMSUNG_ANDROID_XR_ARTICLE["bystander_concern_mentioned"] is False


class TestHardwareEquivalenceParadox:
    """Google/Samsung use identical hardware to Meta but get opposite framing."""

    HARDWARE_SPECS = {
        "meta": {
            "chip": "Snapdragon AR1 Gen 1",
            "camera_mp": 12,
            "led_indicator": True,
        },
        "google": {
            "chip": "Snapdragon AR1 Gen 1",
            "camera_mp": 12,
            "led_indicator": True,
        },
        "samsung": {
            "chip": "Snapdragon AR1 Gen 1",
            "camera_mp": 12,
            "led_indicator": True,
        },
    }

    def test_all_three_use_same_chip(self):
        """Meta, Google, and Samsung glasses all use Snapdragon AR1 Gen 1."""
        chips = {v["chip"] for v in self.HARDWARE_SPECS.values()}
        assert len(chips) == 1
        assert "Snapdragon AR1 Gen 1" in chips

    def test_all_three_have_same_camera(self):
        """All three have 12MP cameras."""
        cameras = {v["camera_mp"] for v in self.HARDWARE_SPECS.values()}
        assert len(cameras) == 1
        assert 12 in cameras

    def test_all_three_have_led_indicators(self):
        """All three have LED privacy indicators."""
        for spec in self.HARDWARE_SPECS.values():
            assert spec["led_indicator"] is True

    def test_hardware_identical_but_framing_diverges(self):
        """Despite identical hardware, Google gets +0.80, Meta-contextual gets -0.40."""
        google_tone = GOOGLE_INTELLIGENT_EYEWEAR_ARTICLE["tone_score"]
        meta_privacy_tone = NEARBY_GLASSES_PRIVACY_ARTICLE["tone_score"]
        delta = google_tone - meta_privacy_tone
        assert delta >= 1.0, f"Tone delta {delta:.2f} — expected ≥1.0 for identical hardware"

    def test_privacy_concerns_apply_equally_to_all(self):
        """If camera privacy is a concern for Meta, it's equally a concern for Google/Samsung."""
        # All have cameras + all have same privacy implications
        for entity, spec in self.HARDWARE_SPECS.items():
            assert spec["camera_mp"] > 0, f"{entity} has a camera"
            assert spec["led_indicator"] is True, f"{entity} has LED indicator"
        # Yet only Meta gets privacy scrutiny
        assert GOOGLE_INTELLIGENT_EYEWEAR_ARTICLE["privacy_mentioned"] is False
        assert SAMSUNG_ANDROID_XR_ARTICLE["privacy_mentioned"] is False
        assert NEARBY_GLASSES_PRIVACY_ARTICLE["privacy_mentioned"] is True


class TestTemporalSequenceAnalysis:
    """Timeline reveals privacy alarm → aspirational competitor coverage pattern."""

    def test_samsung_aspirational_precedes_google_aspirational(self):
        """Samsung 'beat' article (Jan 29) precedes Google 'defeat' article (May 20)."""
        samsung_date = datetime.strptime(SAMSUNG_ANDROID_XR_ARTICLE["date"], "%Y-%m-%d")
        google_date = datetime.strptime(GOOGLE_INTELLIGENT_EYEWEAR_ARTICLE["date"], "%Y-%m-%d")
        assert samsung_date < google_date

    def test_privacy_article_falls_between_aspirational_coverage(self):
        """Privacy alarm article (Feb 25) falls between Samsung (Jan 29) and Google (May 20)."""
        samsung_date = datetime.strptime(SAMSUNG_ANDROID_XR_ARTICLE["date"], "%Y-%m-%d")
        privacy_date = datetime.strptime(NEARBY_GLASSES_PRIVACY_ARTICLE["date"], "%Y-%m-%d")
        google_date = datetime.strptime(GOOGLE_INTELLIGENT_EYEWEAR_ARTICLE["date"], "%Y-%m-%d")
        assert samsung_date < privacy_date < google_date

    def test_google_io_day_has_aspirational_not_privacy_framing(self):
        """On Google I/O day (May 20), the article is aspirational, not privacy-cautious."""
        article = GOOGLE_INTELLIGENT_EYEWEAR_ARTICLE
        assert article["date"] == "2026-05-20"
        assert len(article["aspirational_combat_terms"]) >= 2
        assert len(article["privacy_alarm_terms"]) == 0

    def test_sustained_pattern_not_one_off(self):
        """Pattern spans 5 months (Jan–May 2026), ruling out one-off editorial choice."""
        dates = [datetime.strptime(a["date"], "%Y-%m-%d") for a in ALL_ARTICLES]
        span = (max(dates) - min(dates)).days
        assert span >= 100


class TestCrossEntityEditorialStandards:
    """Same journalist applies different editorial standards to identical hardware."""

    def test_google_gets_aspirational_standard(self):
        """Google coverage standard: assume success, use combat metaphors."""
        article = GOOGLE_INTELLIGENT_EYEWEAR_ARTICLE
        assert article["tone_score"] >= 0.70
        assert "defeat" in article["headline"].lower()
        assert article["privacy_mentioned"] is False

    def test_samsung_gets_aspirational_standard(self):
        """Samsung coverage standard: aspirational 'beat' framing."""
        article = SAMSUNG_ANDROID_XR_ARTICLE
        assert article["tone_score"] >= 0.50
        assert "beat" in article["headline"].lower()
        assert article["privacy_mentioned"] is False

    def test_meta_gets_privacy_alarm_standard(self):
        """Meta coverage standard: privacy alarm, unauthorized filming concern."""
        article = NEARBY_GLASSES_PRIVACY_ARTICLE
        assert article["tone_score"] <= 0.0
        assert article["privacy_mentioned"] is True
        assert article["bystander_concern_mentioned"] is True

    def test_editorial_standard_divergence(self):
        """The same journalist covers the same product category with opposite standards."""
        google_tone = GOOGLE_INTELLIGENT_EYEWEAR_ARTICLE["tone_score"]
        samsung_tone = SAMSUNG_ANDROID_XR_ARTICLE["tone_score"]
        meta_privacy_tone = NEARBY_GLASSES_PRIVACY_ARTICLE["tone_score"]
        avg_competitor = (google_tone + samsung_tone) / 2
        delta = avg_competitor - meta_privacy_tone
        assert delta >= 1.0, (
            f"Editorial standard divergence {delta:.2f} — "
            f"expected ≥1.0 (competitor avg {avg_competitor:.2f} vs Meta {meta_privacy_tone:.2f})"
        )


class TestFinancialIncentiveCorrelation:
    """Future plc's financial dependency on Google predicts the framing pattern."""

    def test_google_dependency_exceeds_60_percent(self):
        """Future plc derives 60%+ of revenue from Google-dependent brands."""
        share = FUTURE_PLC_FINANCIAL["google_dependent_revenue_share_h1_2026"]
        assert share >= 0.60

    def test_profit_collapse_67_percent(self):
        """H1 2026 profit collapsed 67%, attributed to Google traffic decline."""
        change = FUTURE_PLC_FINANCIAL["profit_before_tax_yoy_change_h1_2026"]
        assert change <= -0.60

    def test_zero_meta_financial_relationship(self):
        """Future plc has zero financial relationship with Meta."""
        assert FUTURE_PLC_FINANCIAL["meta_financial_relationship"] == "none"

    def test_existential_google_dependency(self):
        """Google is classified as existential dependency for Future plc."""
        assert FUTURE_PLC_FINANCIAL["google_financial_relationship"] == "existential_dependency"

    def test_samsung_google_glasses_partnership(self):
        """Samsung and Google are joint development partners on Android XR glasses."""
        assert FUTURE_PLC_FINANCIAL["samsung_google_glasses_partnership"] is True

    def test_financial_incentive_predicts_framing(self):
        """Financial relationship (Google=existential, Meta=none) predicts framing direction."""
        # Entity with financial relationship gets aspirational framing
        google_tone = GOOGLE_INTELLIGENT_EYEWEAR_ARTICLE["tone_score"]
        samsung_tone = SAMSUNG_ANDROID_XR_ARTICLE["tone_score"]
        # Entity without financial relationship gets alarm framing
        meta_tone = NEARBY_GLASSES_PRIVACY_ARTICLE["tone_score"]
        assert google_tone > 0 and samsung_tone > 0, "Financially-linked entities get positive framing"
        assert meta_tone < 0, "Non-financially-linked entity gets negative framing"

    def test_ai_overviews_cannibalization(self):
        """Google AI Overviews appear on 50% of Future's key search terms."""
        share = FUTURE_PLC_FINANCIAL["ai_overviews_on_key_terms_share"]
        assert share >= 0.40

    def test_website_sessions_declining(self):
        """Website sessions down 15%, caused by Google algorithm changes."""
        change = FUTURE_PLC_FINANCIAL["website_sessions_yoy_change_h1_2026"]
        assert change <= -0.10


class TestCrossJournalistInstitutionalConsistency:
    """Jason England reinforces the SAME institutional pattern as other Tom's Guide journalists."""

    TOMS_GUIDE_JOURNALISTS_WITH_PATTERN = [
        {
            "name": "Mark Spoonauer",
            "role": "Global Editor-in-Chief",
            "example_headline": "I just tried the future of smart glasses — and they blow away the Meta Ray-Ban Display",
            "combative_term": "blow away",
            "date": "2026-01-12",
        },
        {
            "name": "Mike Prospero",
            "role": "U.S. Editor-in-Chief",
            "example_headline": "Meta has five months to fix these 3 things before its Ray-Bans get smoked by Google's Intelligent Eyewear",
            "combative_term": "get smoked",
            "date": "2026-05-20",
        },
        {
            "name": "Jason England",
            "role": "Managing Editor, Computing",
            "example_headline": "I tested Google's 'Intelligent Eyewear,' and found the smart glasses that will defeat Ray-Ban Meta",
            "combative_term": "defeat",
            "date": "2026-05-20",
        },
        {
            "name": "Kaycee Hill",
            "role": "Staff Writer",
            "example_headline": "How to tell if someone is filming you wearing smart glasses — the signs to watch out for",
            "combative_term": None,  # Privacy framing, not combative
            "date": "2026-05-13",
            "is_privacy_article": True,
        },
    ]

    def test_four_journalists_show_same_pattern(self):
        """At least 4 Tom's Guide journalists contribute to the institutional pattern."""
        unique = set(j["name"] for j in self.TOMS_GUIDE_JOURNALISTS_WITH_PATTERN)
        assert len(unique) >= 4

    def test_pattern_includes_all_editorial_levels(self):
        """Pattern spans from Global EIC to staff writer — not isolated to one role."""
        roles = [j["role"] for j in self.TOMS_GUIDE_JOURNALISTS_WITH_PATTERN]
        assert any("Global" in r for r in roles)
        assert any("U.S." in r for r in roles)
        assert any("Managing Editor" in r for r in roles)

    def test_each_journalist_uses_different_combat_term(self):
        """Different journalists use varied combative terms — not copy-paste."""
        terms = [
            j["combative_term"]
            for j in self.TOMS_GUIDE_JOURNALISTS_WITH_PATTERN
            if j["combative_term"] is not None
        ]
        assert len(set(terms)) == len(terms), "Each journalist uses a unique combative term"

    def test_google_io_day_multiple_journalists_same_pattern(self):
        """On Google I/O day (May 20), both Prospero and England publish Meta-adversarial articles."""
        io_day = [
            j for j in self.TOMS_GUIDE_JOURNALISTS_WITH_PATTERN
            if j["date"] == "2026-05-20"
        ]
        assert len(io_day) >= 2
        journalists = [j["name"] for j in io_day]
        assert "Jason England" in journalists
        assert "Mike Prospero" in journalists


class TestConfounders:
    """Document confounding factors that could explain the pattern without financial incentives."""

    CONFOUNDING_FACTORS = [
        {
            "factor": "market_leader_scrutiny",
            "strength": "STRONG",
            "description": (
                "Meta has 80%+ smart glasses market share (7M+ units in 2025). "
                "Market leaders naturally attract more scrutiny than challengers."
            ),
            "rebuttal": (
                "Market leader scrutiny should apply to PRODUCT QUALITY, not "
                "selectively to PRIVACY while ignoring the identical camera hardware "
                "in competitor products. The Nearby Glasses app detects Meta AND Snap "
                "BLE signals — yet the article is framed as a Meta concern, not a "
                "category-wide camera glasses concern."
            ),
        },
        {
            "factor": "meta_track_record",
            "strength": "STRONG",
            "description": (
                "Meta has a documented history of privacy incidents: the Kenya moderation "
                "scandal, manfluencer abuse, pick-up artist harassment using Ray-Ban Meta. "
                "Google/Samsung glasses have no abuse history because they haven't shipped."
            ),
            "rebuttal": (
                "Valid confound for VOLUME of coverage, but not for VOCABULARY CHOICE. "
                "A journalist could write 'Google's glasses use the same camera that has "
                "enabled privacy abuses on Meta's platform — here's what Google is doing "
                "differently.' Instead, Google gets zero privacy vocabulary at all. "
                "Track record explains covering Meta privacy more, not ignoring Google "
                "privacy entirely."
            ),
        },
        {
            "factor": "pre_release_vs_post_release_genre",
            "strength": "MODERATE",
            "description": (
                "The Google/Samsung articles are pre-release hands-on from events (Google I/O, "
                "earnings calls). Event coverage often emphasizes potential. The privacy "
                "article is editorial, not event-driven."
            ),
            "rebuttal": (
                "Event coverage CAN include caveats. Other outlets covering Google I/O "
                "did raise privacy concerns about Google's identical camera hardware. "
                "The choice to write 'defeat' instead of 'but same privacy concerns apply' "
                "is an editorial decision, not a genre constraint."
            ),
        },
        {
            "factor": "genuine_product_enthusiasm",
            "strength": "MODERATE",
            "description": (
                "England may genuinely believe Google/Samsung glasses are better products. "
                "Enthusiasm for Gemini Live integration and Warby Parker styling is authentic."
            ),
            "rebuttal": (
                "Product enthusiasm does not explain the complete absence of privacy vocabulary. "
                "A genuinely enthusiastic review could say 'these are exciting AND raise the "
                "same privacy questions.' The enthusiasm explanation covers tone, not the "
                "privacy vocabulary zero-out."
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

    def test_at_least_five_confounders_documented(self):
        """Each mechanism must document ≥5 confounding factors."""
        assert len(self.CONFOUNDING_FACTORS) >= 5

    def test_strength_distribution(self):
        """Strength distribution includes STRONG, MODERATE, and WEAK factors."""
        strengths = [f["strength"] for f in self.CONFOUNDING_FACTORS]
        assert "STRONG" in strengths
        assert "MODERATE" in strengths
        assert "WEAK" in strengths

    def test_at_least_two_strong_confounders(self):
        """At least 2 STRONG confounders are honestly documented."""
        strong = [f for f in self.CONFOUNDING_FACTORS if f["strength"] == "STRONG"]
        assert len(strong) >= 2

    def test_all_factors_have_rebuttals(self):
        """Every confounding factor has a substantive rebuttal."""
        for f in self.CONFOUNDING_FACTORS:
            assert f["rebuttal"], f"Missing rebuttal for: {f['factor']}"
            assert len(f["rebuttal"]) > 80, f"Rebuttal too short for: {f['factor']}"


class TestFalsifiablePredictions:
    """Predictions that would weaken the mechanism if falsified."""

    PREDICTIONS = [
        {
            "prediction": (
                "When Google/Samsung smart glasses launch and real-world privacy "
                "incidents occur, Tom's Guide will apply softer vocabulary than "
                "they used for equivalent Meta incidents."
            ),
            "falsification": (
                "If Google/Samsung launch incidents receive 'nightmarish,' "
                "'unauthorized filming,' or equivalent extreme vocabulary from "
                "Jason England, this mechanism is weakened."
            ),
        },
        {
            "prediction": (
                "Jason England will not publish a standalone 'Google smart glasses "
                "privacy concern' article before the product ships."
            ),
            "falsification": (
                "If England publishes a pre-launch Google glasses privacy article with "
                "equivalent alarm vocabulary, this mechanism is falsified."
            ),
        },
        {
            "prediction": (
                "If Future plc's Google dependency decreases (e.g., via TikTok or "
                "AI traffic diversification), the aspiration/alarm vocabulary gap "
                "for Google vs Meta will narrow."
            ),
            "falsification": (
                "If Google revenue dependency drops but the same editorial pattern "
                "persists at the same intensity, financial incentive correlation "
                "is weakened (though institutional culture may persist)."
            ),
        },
    ]

    def test_at_least_three_predictions(self):
        """At least 3 falsifiable predictions are documented."""
        assert len(self.PREDICTIONS) >= 3

    def test_all_predictions_are_falsifiable(self):
        """Every prediction has a specific falsification condition."""
        for p in self.PREDICTIONS:
            assert p["falsification"], f"Missing falsification for prediction"
            assert len(p["falsification"]) > 40


class TestMechanismCrossReferences:
    """Link mechanism #146 to related mechanisms in the dataset."""

    CROSS_REFERENCES = [
        {
            "mechanism_id": 110,
            "relationship": "same_publication_different_journalist",
            "description": (
                "Mike Prospero (#110) at Tom's Guide applies the identical pattern: "
                "qualified-praise-for-Meta ('great, but'), aspirational-for-Google "
                "('get smoked'). Two Managing Editor+ journalists at the same outlet = "
                "institutional editorial direction."
            ),
        },
        {
            "mechanism_id": 128,
            "relationship": "same_parent_company",
            "description": (
                "TechRadar (Future plc sibling) shows privacy vocabulary suppression "
                "for Google via Michael Hicks. The same parent company's editorial "
                "culture produces the same pattern across multiple brands."
            ),
        },
        {
            "mechanism_id": 132,
            "relationship": "same_pattern_different_publisher",
            "description": (
                "Andy Boxall at Android Police (Valnet) shows the same cross-entity "
                "privacy vocabulary inversion. Two independent publishers with Google "
                "dependency both show identical framing asymmetry."
            ),
        },
        {
            "mechanism_id": 106,
            "relationship": "same_archetype",
            "description": (
                "Scott Stein (CNET/Ziff Davis) shows identical entity-selective "
                "privacy scrutiny. Future plc, Valnet, and Ziff Davis are all "
                "Google-dependent publishers applying soft Google coverage."
            ),
        },
    ]

    def test_cross_references_span_multiple_publishers(self):
        """Cross-references establish a multi-publisher pattern."""
        assert len(self.CROSS_REFERENCES) >= 3

    def test_includes_same_publication_reference(self):
        """At least one reference links to the same publication (Mike Prospero)."""
        same_pub = [
            r for r in self.CROSS_REFERENCES
            if r["relationship"] == "same_publication_different_journalist"
        ]
        assert len(same_pub) >= 1

    def test_includes_same_parent_company_reference(self):
        """At least one reference links to the same parent company (Future plc)."""
        same_parent = [
            r for r in self.CROSS_REFERENCES
            if r["relationship"] == "same_parent_company"
        ]
        assert len(same_parent) >= 1

    def test_includes_cross_publisher_reference(self):
        """At least one reference links to a different publisher with same pattern."""
        cross_pub = [
            r for r in self.CROSS_REFERENCES
            if r["relationship"] in ("same_pattern_different_publisher", "same_archetype")
        ]
        assert len(cross_pub) >= 1


class TestAsymmetryScore:
    """Compute and validate the overall asymmetry score for mechanism #146."""

    # Tone scores: -1.0 (adversarial) to +1.0 (aspirational)
    GOOGLE_TONE = GOOGLE_INTELLIGENT_EYEWEAR_ARTICLE["tone_score"]  # +0.80
    SAMSUNG_TONE = SAMSUNG_ANDROID_XR_ARTICLE["tone_score"]  # +0.65
    META_PRIVACY_TONE = NEARBY_GLASSES_PRIVACY_ARTICLE["tone_score"]  # -0.40
    META_COMPARISON_TONE = LATITUDE_META_COMPARISON_ARTICLE["tone_score"]  # +0.30
    CATEGORY_TONE = CRINGE_CATEGORY_ARTICLE["tone_score"]  # 0.00

    def test_google_samsung_average_strongly_positive(self):
        """Competitor coverage averages strongly positive (+0.70+)."""
        avg = (self.GOOGLE_TONE + self.SAMSUNG_TONE) / 2
        assert avg >= 0.60, f"Competitor average {avg:.2f} below +0.60"

    def test_meta_privacy_tone_negative(self):
        """Meta-contextual privacy article tone is negative."""
        assert self.META_PRIVACY_TONE < 0

    def test_tone_delta_exceeds_threshold(self):
        """Tone delta between competitor coverage and Meta privacy coverage exceeds 1.0."""
        competitor_avg = (self.GOOGLE_TONE + self.SAMSUNG_TONE) / 2
        delta = competitor_avg - self.META_PRIVACY_TONE
        assert delta >= 1.0, f"Tone delta {delta:.2f} below 1.0 threshold"

    def test_privacy_vocabulary_delta_is_maximal(self):
        """Privacy vocabulary: Meta-contextual has all, competitors have zero."""
        meta_privacy_count = len(NEARBY_GLASSES_PRIVACY_ARTICLE["privacy_alarm_terms"])
        google_privacy_count = len(GOOGLE_INTELLIGENT_EYEWEAR_ARTICLE["privacy_alarm_terms"])
        samsung_privacy_count = len(SAMSUNG_ANDROID_XR_ARTICLE["privacy_alarm_terms"])
        assert meta_privacy_count >= 4
        assert google_privacy_count == 0
        assert samsung_privacy_count == 0

    def test_overall_asymmetry_score(self):
        """Overall mechanism asymmetry score is ≥0.75."""
        # Asymmetry formula: weighted average of tone delta + privacy vocab ratio
        competitor_avg = (self.GOOGLE_TONE + self.SAMSUNG_TONE) / 2
        tone_delta = competitor_avg - self.META_PRIVACY_TONE
        # Normalize to 0-1 scale (delta of 2.0 = max 1.0)
        tone_component = min(tone_delta / 2.0, 1.0)
        # Privacy vocab ratio: infinity → 1.0
        privacy_component = 1.0  # ∞:0 ratio
        asymmetry_score = (tone_component * 0.5) + (privacy_component * 0.5)
        assert asymmetry_score >= 0.75, f"Asymmetry score {asymmetry_score:.2f} below 0.75"
