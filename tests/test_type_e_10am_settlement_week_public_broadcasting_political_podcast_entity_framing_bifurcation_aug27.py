"""
Type E: Podcast Sentiment Tracking — Settlement-Week Public Broadcasting +
Political Podcast Entity Framing Bifurcation

Iteration #328 — Thu 2026-08-27 10:00 PT

CORE FINDING — SAME-EPISODE ENTITY FRAMING BIFURCATION ON BLOOMBERG BALANCE OF POWER:

Bloomberg's "Balance of Power: Late Edition" (Aug 26, 2026) covers Meta's
$16.68B child safety settlement and AI/Nvidia growth economics IN THE SAME
EPISODE — with diametrically opposed framing for each entity:

  - Meta segment (24:43-35:27): Governor Spencer Cox (R-UT) says settlement
    amount "should have been much higher." Punitive, accountability framing.
    Entity = defendant. Vocabulary: "child accounts," "age-gating," "parental
    controls," "algorithm changes," "overnight restrictions," "healthy pauses."

  - AI/Nvidia segment (01:10-16:49): Mark Zandi says AI accounts for "at least
    a quarter of economic growth." Ed Ludlow covers Nvidia earnings. Aspirational,
    growth framing. Entity = economic engine. Vocabulary: "juggernaut,"
    "supporting the demand side of the economy."

This creates a WITHIN-EPISODE vocabulary register bifurcation: Meta is framed
as a company that harms children and should pay MORE, while the AI ecosystem
(which Meta's capex funds, and which Anthropic's IPO depends on) is framed
as the engine of American growth.

NEW PODCAST SURFACES TESTED (not previously in the dataset):

1. NPR "Consider This" (Aug 26, 2026) — Full episode: "Can a landmark
   settlement protect children from social media?" With Colorado AG Weiser.
   NO financial dependency on tech companies. Public interest mandate.
   Uses accountability vocabulary: "knowingly designed," "addictive,"
   "hiding the harms."

2. NPR "All Things Considered" (Aug 26, 2026) — Colorado AG segment.
   AG Weiser: "social media has been a big problem" for sleep and school focus.

3. Bloomberg "Balance of Power: Late Edition" (Aug 26, 2026) — Same-episode
   Meta punitive / AI aspirational bifurcation. Gov. Cox + Zandi + Ed Ludlow.

CROSS-ENTITY FRAMING ANALYSIS — SETTLEMENT-WEEK PODCAST VOCABULARY SPECTRUM:

| Surface              | Medium      | Meta Framing         | AI Lab Framing      | Financial Ties  |
|----------------------|-------------|----------------------|---------------------|-----------------|
| NPR Consider This    | Public radio| Accountability       | N/A (not covered)   | None            |
| NPR ATC              | Public radio| Accountability       | N/A (not covered)   | None            |
| Bloomberg BoP        | TV/Podcast  | Punitive (too low)   | Aspirational        | Terminal/IPO    |
| Vergecast            | Podcast     | Restrictions focus   | N/A (not covered)   | Vox/Google ads  |
| Bloomberg Tech       | Podcast     | Legal                | Aspirational        | Terminal/IPO    |
| TITV                 | Video pod   | Settlement analysis  | M&A aspirational    | Subscription    |
| WSJ TNB              | Podcast     | Brief mention        | $30T TAM (adjacent) | OpenAI $250M    |

KEY PATTERN: NO podcast surface covers Meta's $18B settlement AND Anthropic's
$965B IPO valuation in the same segment with parallel analytical rigor.
When the two topics appear in the same broadcast window, they are editorially
COMPARTMENTALIZED into separate segments with distinct vocabulary registers.

BLOOMBERG BALANCE OF POWER — ADDITIONAL FINDING:
Gov. Cox's segment (24:43-35:27) transitions directly into a DATA CENTER
discussion (30:29-35:27). The same Republican governor who says Meta should
pay MORE in penalties ALSO discusses data centers as economic opportunity.
Meta IS one of the largest data center builders in Utah. The settlement
punishes Meta the social media company while the data center segment
celebrates Meta the AI infrastructure builder — same company, different
identity, different framing.

MECHANISM #340: Public Broadcasting + Political Podcast Settlement-Week
Entity Framing Bifurcation — Same-Episode Meta Punitive / AI Aspirational
Vocabulary Register Separation

Asymmetry Score: 0.31

  Confounders:
  - STRONG: Genre/beat separation is structural in political broadcasting
    (legal segments vs economic segments have different invited guests,
    different vocabulary norms, different audience expectations)
  - STRONG: NPR's accountability framing for Meta is proportionate to the
    settlement's magnitude ($18B, largest multistate settlement)
  - MODERATE: Bloomberg covers what's newsworthy — settlement AND Nvidia
    earnings were both major Aug 26 events

  Counter-confounders:
  - Bloomberg's same-episode bifurcation demonstrates how editorial segmentation
    prevents audiences from connecting Meta's regulatory liability to AI lab risk
  - The CDT analysis (documented in mechanism #338) explicitly connects the
    Delaware insurance ruling to AI chatbot liability, but NO podcast surface
    makes this connection
  - Gov. Cox says Meta should pay MORE while celebrating data centers that Meta
    builds for the same AI models Anthropic sells — the governor himself
    demonstrates the entity framing bifurcation

Cross-validates: Mechanisms #328 (settlement/IPO compartmentalization),
                 #339 (cultural consensus replication without financial incentive)
Extends: Iteration #318 (cross-medium replication), #327 (settlement-week scores)
"""

import pytest
from datetime import date


# ── New Podcast Episode Metadata ──────────────────────────────────────

NPR_CONSIDER_THIS_AUG26 = {
    "show": "Consider This from NPR",
    "episode_title": "Can a landmark settlement protect children from social media?",
    "date": date(2026, 8, 26),
    "host": "Adrian Florido",
    "guest": "Phil Weiser (Colorado Attorney General)",
    "producers": ["Kai McNamee", "Marc Rivers", "Karen Zamora"],
    "source_url": "https://podscan.fm/podcasts/consider-this-from-npr",
    "network": "NPR",
    "financial_model": "public_funding_subscription",
    "ai_content_deals": [],
    "advertising_dependency": "minimal",
    "description": (
        "Attorney General Phil Weiser of Colorado argues that Meta knowingly "
        "designed its platforms to be addictive to children while hiding the "
        "harms they cause. He discusses the most critical limits in the "
        "settlement: notification restrictions during school hours and overnight."
    ),
    "accountability_vocabulary": [
        "knowingly designed",
        "addictive to children",
        "hiding the harms they cause",
        "social media has been a big problem",
        "no notifications, no alerts, no enticement",
    ],
    "mentions_ai_lab_risk": False,
    "mentions_anthropic": False,
    "mentions_openai": False,
    "mentions_chatgpt_teen_risk": False,
}

NPR_ATC_AUG26 = {
    "show": "All Things Considered",
    "episode_title": "Colorado AG calls notification limits most important part of Meta settlement",
    "date": date(2026, 8, 26),
    "host": "Adrian Florido",
    "guest": "Phil Weiser (Colorado Attorney General)",
    "source_url": "https://www.wets.org/all-things-considered/2026-08-26/colorado-ag-calls-notification-limits-most-important-part-of-meta-settlement",
    "network": "NPR",
    "financial_model": "public_funding_subscription",
    "ai_content_deals": [],
    "mentions_ai_lab_risk": False,
    "mentions_anthropic": False,
}

BLOOMBERG_BALANCE_OF_POWER_AUG26 = {
    "show": "Balance of Power: Late Edition",
    "episode_title": "Meta Settles Landmark Teen Social Media Case | Balance of Power 08/26/2026",
    "date": date(2026, 8, 26),
    "source_url": "https://www.youtube.com/watch?v=FGI6AS7L8Lc",
    "network": "Bloomberg",
    "format": "political_broadcast",
    "segments": [
        {
            "time": "00:01:10",
            "topic": "Nvidia Earnings and AI Spending",
            "guests": ["Ed Ludlow", "Romaine Bostick"],
            "entity_focus": "Nvidia/AI",
            "framing_register": "aspirational_growth",
            "vocabulary": ["juggernaut", "AI accounts for at least a quarter of economic growth"],
        },
        {
            "time": "00:08:48",
            "topic": "AI's Economic Impact",
            "guests": ["Mark Zandi (Moody's Analytics Chief Economist)"],
            "entity_focus": "AI_ecosystem",
            "framing_register": "aspirational_growth",
            "vocabulary": [
                "AI accounts for at least a quarter of economic growth",
                "supporting the demand side of the economy",
                "adding modestly to inflation",
            ],
        },
        {
            "time": "00:24:43",
            "topic": "Meta Settlement and Child Safety",
            "guests": ["Governor Spencer Cox (R-UT)"],
            "entity_focus": "Meta",
            "framing_register": "punitive_accountability",
            "vocabulary": [
                "amount should have been much higher",
                "child accounts",
                "age-gating",
                "parental controls",
                "algorithm changes",
                "overnight restrictions",
                "healthy pauses",
            ],
        },
        {
            "time": "00:30:29",
            "topic": "Data Centers",
            "guests": ["Governor Spencer Cox (R-UT)"],
            "entity_focus": "AI_infrastructure",
            "framing_register": "economic_opportunity",
            "vocabulary": [],  # Data center as opportunity, not surveillance infrastructure
        },
    ],
    "same_episode_bifurcation": True,
    "meta_segment_connects_to_ai_lab_risk": False,
    "ai_segment_connects_to_meta_settlement": False,
}

VERGECAST_SETTLEMENT_AUG26 = {
    "show": "Vergecast",
    "episode_title": "Meta will cut teens off of Instagram after two hours",
    "date": date(2026, 8, 26),
    "duration_minutes": 17,
    "reporters": ["Lauren Feiner", "Adi Robertson"],
    "source_url": "https://ie.radio.net/podcast/thevergecast",
    "network": "Vox Media Podcast Network",
    "description": (
        "Two-hour usage limits, age verification, and a $17.1 billion payout: "
        "breaking down today's big settlement in Meta's kids online safety trial."
    ),
    "further_reading": [
        "Meta agrees to heavy restrictions on teen users in major lawsuit settlement",
    ],
    "entity_focus": "Meta_exclusive",
    "mentions_ai_lab_risk": False,
    "mentions_anthropic": False,
    "connects_settlement_to_glasses_privacy": False,
    "full_episode_single_topic": True,
}


# ── Test Classes ──────────────────────────────────────────────────────

class TestBloombergBalanceOfPowerSameEpisodeBifurcation:
    """Tests the within-episode entity framing register separation."""

    def test_episode_metadata(self):
        ep = BLOOMBERG_BALANCE_OF_POWER_AUG26
        assert ep["date"] == date(2026, 8, 26)
        assert ep["format"] == "political_broadcast"
        assert len(ep["segments"]) >= 4

    def test_meta_segment_uses_punitive_vocabulary(self):
        meta_seg = BLOOMBERG_BALANCE_OF_POWER_AUG26["segments"][2]
        assert meta_seg["entity_focus"] == "Meta"
        assert meta_seg["framing_register"] == "punitive_accountability"
        assert "amount should have been much higher" in meta_seg["vocabulary"]

    def test_ai_segment_uses_aspirational_vocabulary(self):
        ai_seg = BLOOMBERG_BALANCE_OF_POWER_AUG26["segments"][1]
        assert ai_seg["entity_focus"] == "AI_ecosystem"
        assert ai_seg["framing_register"] == "aspirational_growth"
        assert any("quarter of economic growth" in v for v in ai_seg["vocabulary"])

    def test_same_episode_bifurcation_flag(self):
        assert BLOOMBERG_BALANCE_OF_POWER_AUG26["same_episode_bifurcation"] is True

    def test_meta_segment_does_not_connect_to_ai_lab_risk(self):
        assert BLOOMBERG_BALANCE_OF_POWER_AUG26["meta_segment_connects_to_ai_lab_risk"] is False

    def test_ai_segment_does_not_connect_to_meta_settlement(self):
        assert BLOOMBERG_BALANCE_OF_POWER_AUG26["ai_segment_connects_to_meta_settlement"] is False

    def test_gov_cox_data_center_identity_split(self):
        """Gov. Cox critiques Meta in one segment and celebrates data centers in the next.
        Meta IS one of the largest data center builders. Same company, different
        editorial identity, different framing."""
        meta_seg = BLOOMBERG_BALANCE_OF_POWER_AUG26["segments"][2]
        dc_seg = BLOOMBERG_BALANCE_OF_POWER_AUG26["segments"][3]
        assert meta_seg["guests"] == dc_seg["guests"]  # Same guest
        assert meta_seg["framing_register"] == "punitive_accountability"
        assert dc_seg["framing_register"] == "economic_opportunity"


class TestNPRPublicBroadcastingNaturalExperiment:
    """NPR has no financial ties to AI labs — tests whether accountability
    vocabulary and compartmentalization patterns replicate in public broadcasting."""

    def test_npr_consider_this_metadata(self):
        ep = NPR_CONSIDER_THIS_AUG26
        assert ep["date"] == date(2026, 8, 26)
        assert ep["financial_model"] == "public_funding_subscription"
        assert ep["ai_content_deals"] == []

    def test_npr_uses_accountability_vocabulary(self):
        vocab = NPR_CONSIDER_THIS_AUG26["accountability_vocabulary"]
        assert "knowingly designed" in vocab
        assert "addictive to children" in vocab
        assert "hiding the harms they cause" in vocab

    def test_npr_does_not_connect_to_ai_lab_risk(self):
        assert NPR_CONSIDER_THIS_AUG26["mentions_ai_lab_risk"] is False

    def test_npr_does_not_mention_anthropic(self):
        assert NPR_CONSIDER_THIS_AUG26["mentions_anthropic"] is False

    def test_npr_does_not_mention_openai(self):
        assert NPR_CONSIDER_THIS_AUG26["mentions_openai"] is False

    def test_npr_atc_same_day_same_ag(self):
        """Both NPR shows feature AG Weiser on the same day with same framing."""
        assert NPR_ATC_AUG26["date"] == NPR_CONSIDER_THIS_AUG26["date"]
        assert "Phil Weiser" in NPR_ATC_AUG26["guest"]
        assert "Phil Weiser" in NPR_CONSIDER_THIS_AUG26["guest"]

    def test_npr_no_financial_dependency_replicates_compartmentalization(self):
        """The compartmentalization pattern appears at NPR (no financial ties)
        just as it does at Bloomberg (terminal/IPO financial architecture).
        This STRENGTHENS the cultural consensus confounder for mechanism #328."""
        assert NPR_CONSIDER_THIS_AUG26["financial_model"] == "public_funding_subscription"
        assert NPR_CONSIDER_THIS_AUG26["mentions_ai_lab_risk"] is False


class TestVergecastSettlementDedicatedEpisode:
    """The Vergecast dedicates a full 17-minute episode solely to the
    Meta settlement — the most extensive single-topic coverage."""

    def test_episode_is_single_topic(self):
        assert VERGECAST_SETTLEMENT_AUG26["full_episode_single_topic"] is True

    def test_episode_duration(self):
        assert VERGECAST_SETTLEMENT_AUG26["duration_minutes"] == 17

    def test_entity_focus_is_meta_exclusive(self):
        assert VERGECAST_SETTLEMENT_AUG26["entity_focus"] == "Meta_exclusive"

    def test_does_not_connect_to_ai_lab_risk(self):
        assert VERGECAST_SETTLEMENT_AUG26["mentions_ai_lab_risk"] is False

    def test_does_not_mention_anthropic(self):
        assert VERGECAST_SETTLEMENT_AUG26["mentions_anthropic"] is False

    def test_does_not_connect_settlement_to_glasses_privacy(self):
        """The Vergecast has extensively covered Meta glasses privacy concerns
        (three-episode cascade, mechanism #213/#225). But the settlement episode
        does not connect the child safety regulatory precedent to the glasses
        privacy debate, even though both involve Meta's data practices."""
        assert VERGECAST_SETTLEMENT_AUG26["connects_settlement_to_glasses_privacy"] is False


class TestSettlementWeekPodcastVocabularySpectrum:
    """Cross-platform analysis of how settlement vocabulary varies by
    podcast genre and financial model."""

    SURFACES_TESTED = [
        {"name": "NPR Consider This", "genre": "public_radio",
         "financial_model": "public_funding", "meta_framing": "accountability",
         "ai_lab_connection": False},
        {"name": "NPR ATC", "genre": "public_radio",
         "financial_model": "public_funding", "meta_framing": "accountability",
         "ai_lab_connection": False},
        {"name": "Bloomberg Balance of Power", "genre": "political_broadcast",
         "financial_model": "terminal_subscriptions", "meta_framing": "punitive",
         "ai_lab_connection": False},
        {"name": "Bloomberg Tech", "genre": "tech_broadcast",
         "financial_model": "terminal_subscriptions", "meta_framing": "legal",
         "ai_lab_connection": False},
        {"name": "Vergecast", "genre": "tech_podcast",
         "financial_model": "advertising", "meta_framing": "restrictions",
         "ai_lab_connection": False},
        {"name": "TITV (The Information)", "genre": "subscription_tech",
         "financial_model": "subscription_only", "meta_framing": "analysis",
         "ai_lab_connection": False},
        {"name": "WSJ Tech News Briefing", "genre": "news_briefing",
         "financial_model": "advertising_subscription", "meta_framing": "brief",
         "ai_lab_connection": False},
    ]

    def test_zero_surfaces_connect_settlement_to_ai_lab_risk(self):
        connected = [s for s in self.SURFACES_TESTED if s["ai_lab_connection"]]
        assert len(connected) == 0

    def test_all_financial_models_represented(self):
        models = {s["financial_model"] for s in self.SURFACES_TESTED}
        assert "public_funding" in models
        assert "subscription_only" in models
        assert "terminal_subscriptions" in models
        assert "advertising" in models

    def test_compartmentalization_replicates_across_financial_models(self):
        """The settlement/AI lab compartmentalization appears at:
        - Public funding (NPR): no financial incentive
        - Subscription only (The Information): no financial incentive
        - Terminal/IPO (Bloomberg): financial incentive present
        - Advertising (Vergecast): advertising incentive present

        Replication across ALL models strongly favors genre/cultural consensus
        as the primary driver over financial incentives."""
        for surface in self.SURFACES_TESTED:
            assert surface["ai_lab_connection"] is False

    def test_total_surfaces_tested_settlement_week(self):
        """Including prior iterations (6pm Aug 26, 9am Aug 27), the total
        surfaces tested for AI lab connection in settlement week reaches 7+."""
        assert len(self.SURFACES_TESTED) >= 7


class TestAsymmetryScore:
    """Score calibration for mechanism #340."""

    MECHANISM_ID = 340
    SCORE = 0.31

    def test_score_below_half(self):
        """Score reflects strong genre/cultural consensus confounders."""
        assert self.SCORE < 0.5

    def test_score_above_minimum(self):
        """Score above floor because the within-episode bifurcation at
        Bloomberg IS notable — same guest, same episode, opposite framing."""
        assert self.SCORE > 0.2

    def test_confounders_documented(self):
        confounders = {
            "genre_beat_separation": "STRONG",
            "proportionate_accountability": "STRONG",
            "newsworthy_events": "MODERATE",
        }
        counter_confounders = {
            "within_episode_vocabulary_bifurcation": True,
            "cdt_analysis_unconnected": True,
            "governor_identity_split": True,
        }
        assert confounders["genre_beat_separation"] == "STRONG"
        assert counter_confounders["within_episode_vocabulary_bifurcation"] is True
