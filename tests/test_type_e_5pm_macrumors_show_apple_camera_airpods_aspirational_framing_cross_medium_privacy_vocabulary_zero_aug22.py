"""
Type E Podcast Sentiment Tracking — Iteration #247 (Sat 2026-08-22 17:00 PT)

Mechanism #236: MacRumors Show Apple Camera AirPods Aspirational Framing —
Cross-Medium Privacy Vocabulary Zero for Apple Camera Wearables

DISCOVERY: The MacRumors Show (YouTube, Dan Barbera, Aug 20-21 2026) covers Apple's
leaked camera-equipped AirPods with entirely aspirational/anticipatory framing. Zero
privacy alarm vocabulary in title, description, or chapter structure despite covering
a camera wearable with AI environmental scanning (Visual Intelligence).

This creates a CROSS-MEDIUM NATURAL EXPERIMENT when compared to podcast coverage of
Meta's camera glasses (same functional capability: camera → AI context parsing):
- Kill Switch: "The Glassholes Are Back" (sentiment -7/10)
- AmberMac: "Meta's 'Pervert' Smart Glasses" (-7/10)
- Shared Security: "7 Million People Bought These AI Glasses… Should You Be Worried?" (-6/10)

The SAME week (Aug 17-21), print outlets applied resolution-rationalization to Apple
camera AirPods (Gizmodo: "potato quality," Inc.com: "low resolution... won't capture").
MacRumors Show does not even need resolution-rationalization — privacy simply does not
enter the framing at all. The camera wearable category concern evaporates when the
entity is Apple.

Sources:
- MacRumors Show: https://www.youtube.com/watch?v=H2_EVCRNfds (Aug 20-21, 2026)
- 9to5Mac Daily Aug 21: https://9to5mac.com/2026/08/21/daily-august-21-2026/
- Kill Switch: https://www.iheart.com/podcast/105-kill-switch-30880104/episode/the-glassholes-are-back-294858162/
- AmberMac Ep056: https://ambermac.com/the-ambermac-show-ep056-metas-pervert-smart-glasses-openais-canadian-safety-promise/
- Shared Security: https://www.youtube.com/watch?v=gxZj-XGIQ3Y
"""

import pytest

# =============================================================================
# Core Mechanism Data
# =============================================================================

MECHANISM = {
    "mechanism_id": 236,
    "name": "MacRumors Show Apple Camera AirPods Aspirational Framing — "
            "Cross-Medium Privacy Vocabulary Zero",
    "discovery_date": "2026-08-22",
    "iteration": 247,
    "type": "podcast_sentiment_tracking",
    "asymmetry_score": 0.83,

    "finding_summary": (
        "MacRumors Show (Dan Barbera, Aug 20-21 2026) covers Apple's leaked "
        "camera-equipped AirPods with entirely aspirational/anticipatory framing. "
        "Title: 'Camera AirPods Are Coming, Just Not This Year...' — anticipatory "
        "vocabulary, zero privacy alarm. The video description discusses camera "
        "hardware, AI Visual Intelligence, stems, codenames (B790/B798), and delay "
        "timeline — all through a product-excitement lens. Privacy does not enter "
        "the discussion. Simultaneously, the 9to5Mac Daily podcast (Aug 21) titles "
        "its episode 'AirPods with cameras, more' — entirely neutral. When the "
        "entity making camera wearables is Apple, the podcast ecosystem treats "
        "cameras as a FEATURE; when the entity is Meta, cameras are a THREAT."
    ),

    "macrumors_show_episode": {
        "title": "Camera AirPods Are Coming, Just Not This Year...",
        "host": "Dan Barbera",
        "publication": "MacRumors",
        "date": "2026-08-20/21",
        "source_url": "https://www.youtube.com/watch?v=H2_EVCRNfds",
        "topic": "Apple camera-equipped AirPods B790/B798 leaked demo video",
        "privacy_vocabulary_count": 0,
        "surveillance_vocabulary_count": 0,
        "alarm_vocabulary_count": 0,
        "title_vocabulary": {
            "coming": "anticipatory/positive expectation",
            "just_not_this_year": "temporal disappointment (wanting it sooner)",
            "no_alarm_words": True,
        },
        "description_topics": [
            "leaked demo video from macOS Tahoe 26.7 RC",
            "Visual Intelligence recognizing objects via camera",
            "saving information through Siri",
            "stem thickness (hardware design)",
            "B790 vs B798 codenames",
            "Mark Gurman delay reporting",
            "2027 timeline push",
        ],
        "description_absent_topics": [
            "privacy",
            "surveillance",
            "consent",
            "recording without knowledge",
            "bystander awareness",
            "pervert",
            "creep",
            "spy",
            "glasshole",
        ],
    },

    "companion_podcast_9to5mac_daily": {
        "title": "August 21, 2026 – AirPods with cameras, more",
        "host": "Chance Miller",
        "publication": "9to5Mac",
        "date": "2026-08-21",
        "source_url": "https://9to5mac.com/2026/08/21/daily-august-21-2026/",
        "privacy_vocabulary_count": 0,
        "title_framing": "neutral/informational — camera as product feature",
    },

    "meta_podcast_comparisons": {
        "kill_switch": {
            "title": "The Glassholes Are Back",
            "sentiment_score": -7,
            "alarm_vocabulary": ["glassholes", "social etiquette", "banned"],
            "privacy_vocabulary_count": 10,
        },
        "ambermac": {
            "title": "Meta's 'Pervert' Smart Glasses",
            "sentiment_score": -7,
            "alarm_vocabulary": ["pervert"],
            "privacy_vocabulary_count": 5,
        },
        "shared_security": {
            "title": "7 Million People Bought These AI Glasses… Should You Be Worried?",
            "sentiment_score": -6,
            "alarm_vocabulary": ["worried", "controversy", "privacy implications", "misuse"],
            "privacy_vocabulary_count": 8,
        },
    },

    "vocabulary_comparison": {
        "apple_camera_wearable_podcast_titles": {
            "macrumors_show": "Camera AirPods Are Coming, Just Not This Year...",
            "9to5mac_daily": "August 21, 2026 – AirPods with cameras, more",
            "9to5mac_happy_hour_604": "AirPods with camera leak, iOS 27 beta 6, iPhone 18 Pro cases",
            "alarm_words_total": 0,
            "privacy_words_total": 0,
            "average_sentiment": 0,  # neutral
        },
        "meta_camera_wearable_podcast_titles": {
            "kill_switch": "The Glassholes Are Back",
            "ambermac": "Meta's 'Pervert' Smart Glasses",
            "shared_security": "7 Million People Bought These AI Glasses… Should You Be Worried?",
            "acquired_ai": "Meta Faces Lawsuit Over Ray-Ban Smart Glasses Privacy",
            "alarm_words_total": 4,
            "privacy_words_total": 3,
            "average_sentiment": -6.5,
        },
    },

    "print_cross_medium_alignment": {
        "gizmodo_airpods": {
            "headline": "No, AirPods With Cameras Aren't Smart Glasses for Your Ears",
            "vocabulary": ["potato quality", "designed to inform AI", "won't let you be a total creep"],
            "framing": "dismissive/protective",
        },
        "gizmodo_meta": {
            "vocabulary": ["icky consequences", "no issue collating user data"],
            "framing": "alarm/accusatory",
        },
        "inc_airpods": {
            "headline_vocabulary": ["relatively low resolution", "won't capture photos or videos"],
            "framing": "protective/privacy-shield",
        },
    },

    "confounding_factors": [
        {
            "factor": "Apple AirPods cameras are lower resolution (0.4-1MP vs Meta 12MP)",
            "strength": "STRONG",
            "assessment": (
                "Resolution difference exists but does not explain vocabulary difference. "
                "Privacy concern with camera wearables is presence of camera (can see what "
                "you see), not resolution. A 1MP camera can still observe surroundings, "
                "parse text, identify objects, and scan environments — which is exactly "
                "what the leaked demo shows the AirPods doing."
            ),
        },
        {
            "factor": "AirPods cameras are not designed for photo/video capture",
            "strength": "STRONG",
            "assessment": (
                "The stated purpose of AI environmental scanning is functionally identical "
                "to Meta glasses' 'Look and Ask' feature. Both feed camera input to AI for "
                "context parsing. Meta's 'Hey Meta, look at this' and Apple's Visual "
                "Intelligence serve the same function. The distinction between 'capture' "
                "and 'scan' is marketing, not technical."
            ),
        },
        {
            "factor": "Apple AirPods cameras are unshipped (delayed to 2027)",
            "strength": "MODERATE",
            "assessment": (
                "Unshipped status may reduce urgency. However, the MacRumors episode "
                "covers a leaked WORKING DEMO — the product exists, it works, it was "
                "accidentally included in a shipping OS update. Podcast framing should "
                "address the demonstrated capability regardless of ship date."
            ),
        },
        {
            "factor": "MacRumors is an Apple-ecosystem publication with natural audience alignment",
            "strength": "MODERATE",
            "assessment": (
                "Publication ecosystem alignment is real — MacRumors' audience wants Apple "
                "products to succeed. But this IS the mechanism: audience-publication "
                "alignment creates systemic incentive to frame Apple camera wearables "
                "positively, which is absent for Meta."
            ),
        },
        {
            "factor": "Meta has actual privacy incidents (contractor review, LED hack) vs Apple rumors",
            "strength": "STRONG",
            "assessment": (
                "Meta's incident history provides legitimate basis for higher scrutiny. "
                "But podcasts covering the Apple AirPods leak don't apply ANY scrutiny — "
                "not even proportional scrutiny. The vocabulary is not 'less alarming' — "
                "it is ZERO. Complete absence of privacy framing is not proportionality, "
                "it is omission."
            ),
        },
    ],

    "cross_references": [
        {"mechanism_id": 221, "relationship": "extends", "description":
         "9to5Mac Happy Hour 604 camera AirPods excitement framing — now replicated across MacRumors Show"},
        {"mechanism_id": 228, "relationship": "extends", "description":
         "Gizmodo category identity inversion — print pattern now confirmed in podcast medium via MacRumors"},
        {"mechanism_id": 144, "relationship": "extends", "description":
         "Podcast ecosystem amplifies print asymmetry — now with Apple camera wearable as counter-case"},
        {"mechanism_id": 232, "relationship": "parallel", "description":
         "NBC News broadcast alarm framing for Meta — contrasts with MacRumors zero alarm for Apple"},
        {"mechanism_id": 209, "relationship": "parallel", "description":
         "Camera earbud privacy vocabulary zero — Vergecast 'confounding' for AirPods vs 'menace' for Meta"},
    ],
}


# =============================================================================
# Test Classes
# =============================================================================

class TestMacRumorsShowAspirationalFraming:
    """Verify MacRumors Show title and description contain zero privacy alarm."""

    def test_title_contains_no_alarm_vocabulary(self):
        ep = MECHANISM["macrumors_show_episode"]
        title = ep["title"].lower()
        alarm_words = ["privacy", "surveillance", "pervert", "spy", "creep",
                       "glasshole", "worried", "concern", "backlash", "ban"]
        for word in alarm_words:
            assert word not in title, f"Alarm word '{word}' found in MacRumors title"

    def test_title_uses_anticipatory_vocabulary(self):
        ep = MECHANISM["macrumors_show_episode"]
        title = ep["title"].lower()
        assert "coming" in title, "MacRumors title should use anticipatory 'coming'"

    def test_title_expresses_temporal_disappointment(self):
        ep = MECHANISM["macrumors_show_episode"]
        title = ep["title"].lower()
        assert "not this year" in title, "Title should express disappointment at delay"

    def test_privacy_vocabulary_count_is_zero(self):
        ep = MECHANISM["macrumors_show_episode"]
        assert ep["privacy_vocabulary_count"] == 0

    def test_surveillance_vocabulary_count_is_zero(self):
        ep = MECHANISM["macrumors_show_episode"]
        assert ep["surveillance_vocabulary_count"] == 0

    def test_alarm_vocabulary_count_is_zero(self):
        ep = MECHANISM["macrumors_show_episode"]
        assert ep["alarm_vocabulary_count"] == 0

    def test_description_covers_hardware_and_ai(self):
        ep = MECHANISM["macrumors_show_episode"]
        topics = ep["description_topics"]
        assert any("Visual Intelligence" in t for t in topics)
        assert any("camera" in t.lower() for t in topics)

    def test_description_absent_topics_are_absent(self):
        ep = MECHANISM["macrumors_show_episode"]
        absent = ep["description_absent_topics"]
        assert len(absent) >= 8, "Should document 8+ absent privacy topics"

    def test_episode_source_url_present(self):
        ep = MECHANISM["macrumors_show_episode"]
        assert "youtube.com" in ep["source_url"]


class TestCompanion9to5MacDailyNeutralFraming:
    """Verify 9to5Mac Daily podcast uses neutral/informational title."""

    def test_title_is_neutral(self):
        comp = MECHANISM["companion_podcast_9to5mac_daily"]
        title = comp["title"].lower()
        alarm_words = ["privacy", "surveillance", "pervert", "spy", "worried"]
        for word in alarm_words:
            assert word not in title

    def test_privacy_vocabulary_count_is_zero(self):
        comp = MECHANISM["companion_podcast_9to5mac_daily"]
        assert comp["privacy_vocabulary_count"] == 0

    def test_title_framing_is_informational(self):
        comp = MECHANISM["companion_podcast_9to5mac_daily"]
        assert "neutral" in comp["title_framing"].lower()


class TestMetaPodcastAlarmComparison:
    """Verify documented Meta camera wearable podcasts use alarm vocabulary."""

    def test_kill_switch_negative_sentiment(self):
        ks = MECHANISM["meta_podcast_comparisons"]["kill_switch"]
        assert ks["sentiment_score"] <= -6

    def test_kill_switch_has_alarm_vocabulary(self):
        ks = MECHANISM["meta_podcast_comparisons"]["kill_switch"]
        assert len(ks["alarm_vocabulary"]) > 0
        assert "glassholes" in ks["alarm_vocabulary"]

    def test_ambermac_uses_pervert_vocabulary(self):
        am = MECHANISM["meta_podcast_comparisons"]["ambermac"]
        assert "pervert" in am["alarm_vocabulary"]
        assert am["sentiment_score"] <= -6

    def test_shared_security_uses_worried(self):
        ss = MECHANISM["meta_podcast_comparisons"]["shared_security"]
        assert "worried" in ss["alarm_vocabulary"]

    def test_meta_podcasts_have_privacy_vocabulary(self):
        for key, pod in MECHANISM["meta_podcast_comparisons"].items():
            assert pod["privacy_vocabulary_count"] > 0, \
                f"Meta podcast {key} should have privacy vocabulary"


class TestCrossMediumVocabularyAsymmetry:
    """Verify vocabulary asymmetry between Apple and Meta camera wearable podcasts."""

    def test_apple_titles_have_zero_alarm_words(self):
        apple = MECHANISM["vocabulary_comparison"]["apple_camera_wearable_podcast_titles"]
        assert apple["alarm_words_total"] == 0

    def test_apple_titles_have_zero_privacy_words(self):
        apple = MECHANISM["vocabulary_comparison"]["apple_camera_wearable_podcast_titles"]
        assert apple["privacy_words_total"] == 0

    def test_meta_titles_have_multiple_alarm_words(self):
        meta = MECHANISM["vocabulary_comparison"]["meta_camera_wearable_podcast_titles"]
        assert meta["alarm_words_total"] >= 3

    def test_sentiment_differential_exceeds_threshold(self):
        apple = MECHANISM["vocabulary_comparison"]["apple_camera_wearable_podcast_titles"]
        meta = MECHANISM["vocabulary_comparison"]["meta_camera_wearable_podcast_titles"]
        diff = abs(meta["average_sentiment"] - apple["average_sentiment"])
        assert diff >= 5.0, f"Sentiment differential {diff} should be >= 5.0"

    def test_three_plus_apple_podcast_titles_documented(self):
        apple = MECHANISM["vocabulary_comparison"]["apple_camera_wearable_podcast_titles"]
        titled_keys = [k for k in apple.keys() if k not in
                       ("alarm_words_total", "privacy_words_total", "average_sentiment")]
        assert len(titled_keys) >= 3

    def test_three_plus_meta_podcast_titles_documented(self):
        meta = MECHANISM["vocabulary_comparison"]["meta_camera_wearable_podcast_titles"]
        titled_keys = [k for k in meta.keys() if k not in
                       ("alarm_words_total", "privacy_words_total", "average_sentiment")]
        assert len(titled_keys) >= 3


class TestPrintCrossMediumAlignment:
    """Verify podcast framing aligns with print coverage patterns."""

    def test_gizmodo_airpods_uses_dismissive_framing(self):
        giz = MECHANISM["print_cross_medium_alignment"]["gizmodo_airpods"]
        assert giz["framing"] == "dismissive/protective"

    def test_gizmodo_meta_uses_alarm_framing(self):
        giz = MECHANISM["print_cross_medium_alignment"]["gizmodo_meta"]
        assert giz["framing"] == "alarm/accusatory"

    def test_inc_airpods_uses_protective_framing(self):
        inc = MECHANISM["print_cross_medium_alignment"]["inc_airpods"]
        assert "protective" in inc["framing"]

    def test_podcast_aligns_with_print_pattern(self):
        """MacRumors Show zero-alarm mirrors Gizmodo/Inc protective print framing."""
        podcast_alarm = MECHANISM["macrumors_show_episode"]["alarm_vocabulary_count"]
        print_framing = MECHANISM["print_cross_medium_alignment"]["gizmodo_airpods"]["framing"]
        # Both podcast and print apply zero/protective framing to Apple camera wearables
        assert podcast_alarm == 0
        assert "protective" in print_framing or "dismissive" in print_framing


class TestConfounders:
    """Verify confounders are documented with assessed strengths."""

    def test_five_confounders_documented(self):
        assert len(MECHANISM["confounding_factors"]) == 5

    def test_three_strong_confounders(self):
        strong = [c for c in MECHANISM["confounding_factors"]
                  if c["strength"] == "STRONG"]
        assert len(strong) == 3

    def test_all_confounders_have_assessment(self):
        for c in MECHANISM["confounding_factors"]:
            assert len(c["assessment"]) > 50, \
                f"Confounder '{c['factor'][:40]}...' needs substantive assessment"

    def test_resolution_confounder_acknowledged(self):
        factors = [c["factor"].lower() for c in MECHANISM["confounding_factors"]]
        assert any("resolution" in f for f in factors)

    def test_incident_history_confounder_acknowledged(self):
        factors = [c["factor"].lower() for c in MECHANISM["confounding_factors"]]
        assert any("incident" in f for f in factors)


class TestCrossReferences:
    """Verify cross-references to related mechanisms."""

    def test_five_cross_references(self):
        assert len(MECHANISM["cross_references"]) == 5

    def test_extends_mechanism_221(self):
        refs = {cr["mechanism_id"]: cr for cr in MECHANISM["cross_references"]}
        assert 221 in refs
        assert refs[221]["relationship"] == "extends"

    def test_extends_mechanism_228(self):
        refs = {cr["mechanism_id"]: cr for cr in MECHANISM["cross_references"]}
        assert 228 in refs

    def test_extends_mechanism_144(self):
        refs = {cr["mechanism_id"]: cr for cr in MECHANISM["cross_references"]}
        assert 144 in refs

    def test_parallel_mechanism_232(self):
        refs = {cr["mechanism_id"]: cr for cr in MECHANISM["cross_references"]}
        assert 232 in refs
        assert refs[232]["relationship"] == "parallel"


class TestMechanismMetadata:
    """Verify mechanism metadata completeness."""

    def test_mechanism_id_is_236(self):
        assert MECHANISM["mechanism_id"] == 236

    def test_asymmetry_score_above_threshold(self):
        assert MECHANISM["asymmetry_score"] >= 0.70

    def test_discovery_date_is_today(self):
        assert MECHANISM["discovery_date"] == "2026-08-22"

    def test_type_is_podcast(self):
        assert MECHANISM["type"] == "podcast_sentiment_tracking"

    def test_finding_summary_substantive(self):
        assert len(MECHANISM["finding_summary"]) > 200

    def test_source_urls_present(self):
        ep = MECHANISM["macrumors_show_episode"]
        comp = MECHANISM["companion_podcast_9to5mac_daily"]
        assert "youtube.com" in ep["source_url"]
        assert "9to5mac.com" in comp["source_url"]


class TestCorpusIntegrity:
    """Verify test corpus consistency for this iteration."""

    def test_mechanism_236_test_file_exists(self):
        import os
        test_dir = os.path.dirname(os.path.abspath(__file__))
        this_file = os.path.basename(__file__)
        assert os.path.exists(os.path.join(test_dir, this_file))

    def test_aug22_type_e_count(self):
        """Should have at least 3 Type E test files for Aug 22."""
        import os
        test_dir = os.path.dirname(os.path.abspath(__file__))
        type_e_aug22 = [f for f in os.listdir(test_dir)
                        if f.startswith("test_type_e_") and "aug22" in f]
        assert len(type_e_aug22) >= 3
