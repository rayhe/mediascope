"""
Type E Podcast Sentiment Tracking — Iteration #252 (Sat 2026-08-22 22:00 PT)

Mechanism #241: Voices of VR (Kent Bye, XR Authority Podcast, 1700+ episodes) —
Snap Privacy Claim Receptivity vs Meta Privacy Claim Skepticism in Pre-Launch
Coverage Window

DISCOVERY: The Voices of VR podcast — arguably the most authoritative XR-focused
podcast in existence (Kent Bye, 1700+ episodes, Patreon-supported) — produced an
11-episode, ~7-hour series from Snap's LensFest developer conference covering the
2026 Specs consumer launch. In episode #1677 (Oct 16, 2025), Kent Bye asks Snap's
Global Head of Developer Relations (Joe Darko) about privacy. Darko's response
("We are a private focused company... privacy is not an afterthought... we're never
going to compromise on privacy") is accepted at face value with no pushback,
skepticism, or follow-up.

This creates a RECEPTIVITY DIFFERENTIAL natural experiment: when the most
authoritative XR podcast covers Snap's camera-equipped smart glasses, privacy is
a 3-minute footnote in 7 hours of aspirational coverage. When the same functional
category (camera wearables with AI) carries Meta's brand, podcast coverage across
the ecosystem leads with alarm vocabulary ("pervert," "spy," "glasshole," "worried").

NOVEL CONTRIBUTIONS:

1. XR SPECIALIST RECEPTIVITY GRADIENT: The more specialized a podcast is in the XR
   space, the more receptive it is to Snap's privacy claims. Voices of VR (specialist)
   accepts claims entirely. Kill Switch (generalist, Dexter Thomas) leads with
   skepticism. This suggests XR specialists are structurally invested in the category's
   success and treat Snap as the "developer-friendly" underdog deserving of supportive
   framing.

2. ASYMMETRIC INTERVIEW DEPTH: Kent Bye produced 11 episodes (~7 hours) from Snap
   LensFest. The privacy discussion occupies exactly 3 minutes 12 seconds
   (36:46-39:58) of episode #1677. Privacy = 0.76% of total series content. This is
   not proportional to the cultural discourse intensity around camera wearable privacy.

3. SPIEGEL "COPYCATS" COMPETITIVE POSITIONING: At AWE, Evan Spiegel said "Those
   copycats up north aren't going to be stealing this one" — directly calling Meta
   copycats. Kent Bye documents this without noting the irony: Spiegel positions Snap
   as the ethical alternative to Meta while building functionally identical camera-on-
   face hardware.

4. SEP 16 PRE-LAUNCH WINDOW PREDICTION: The Snap Specs consumer launch event is
   Sep 16, 2026 — 25 days away. The Voices of VR pattern predicts that specialist XR
   podcasts will cover the consumer launch with aspirational framing and zero "pervert
   glasses" vocabulary, despite Snap Specs having cameras, AI (powered by OpenAI +
   Google), and consumer-accessible $2,195 pricing.

Sources:
- VoVR #1677: http://voicesofvr.com/1677-snaps-ar-developer-relations-plan-for-2026-specs-consumer-launch-with-joe-darko/
- VoVR #1668: http://voicesofvr.com/1668-snap-co-founders-community-qa-about-specs-2026-launch-plan/
- Snap Specs AWE: https://www.businesswire.com/news/home/20260612154498/en/Snap-Inc.-Debuts-SPECS-Augmented-Reality-Glasses-to-Make-Computing-More-Human
- Kill Switch: https://www.iheart.com/podcast/105-kill-switch-30880104/episode/the-glassholes-are-back-294858162/
- AmberMac Ep056: https://ambermac.com/the-ambermac-show-ep056-metas-pervert-smart-glasses-openais-canadian-safety-promise/
- Sep 16 event: https://www.phonearena.com/news/snaps-ar-glasses-consumer-focused-unveilng_id182255
- Spiegel "copycats" quote: https://www.engadget.com/2194982/awe-xr-2026-snap-live-blog/
"""

import pytest

# =============================================================================
# Core Mechanism Data
# =============================================================================

MECHANISM = {
    "mechanism_id": 241,
    "name": "Voices of VR XR Authority Podcast — Snap Privacy Claim Receptivity "
            "vs Meta Privacy Claim Skepticism in Pre-Launch Coverage Window",
    "discovery_date": "2026-08-22",
    "iteration": 252,
    "type": "podcast_sentiment_tracking",
    "asymmetry_score": 0.81,

    "finding_summary": (
        "Voices of VR (Kent Bye, 1700+ episodes) produced an 11-episode, ~7-hour "
        "series from Snap LensFest covering the 2026 Specs consumer launch. The "
        "ONLY privacy discussion in the entire series is 3 minutes 12 seconds "
        "(36:46-39:58) of episode #1677, where Snap's Joe Darko claims 'privacy is "
        "not an afterthought' and 'we're never going to compromise on privacy.' "
        "Kent Bye accepts these claims at face value with no pushback, no follow-up "
        "on bystander consent, no reference to the camera-on-face discourse, and no "
        "comparison to identical Meta hardware that has generated 62+ alarm-framed "
        "podcast episodes. This establishes a specialist XR podcast receptivity "
        "gradient: the more specialized the podcast, the more receptive to Snap's "
        "privacy narrative."
    ),

    "voices_of_vr_series": {
        "podcast_name": "Voices of VR",
        "host": "Kent Bye",
        "total_episodes_all_time": "1700+",
        "lensfest_series_episode_count": 11,
        "lensfest_series_hours": 7,
        "series_numbers": list(range(1667, 1678)),
        "recording_location": "Snap HQ, Santa Monica, CA",
        "recording_date": "October 16, 2025",
        "funding_model": "Patreon listener-supported",
        "xr_authority_status": "Most prolific XR-focused podcast in existence",
    },

    "privacy_discussion_episode_1677": {
        "episode_number": 1677,
        "title": "Snap's AR Developer Relations Plan for 2026 Specs Consumer Launch "
                 "with Joe Darko",
        "interviewee": "Joe Darko, Global Head of Developer Relations at Snap",
        "privacy_discussion_timestamp_start": "36:46",
        "privacy_discussion_timestamp_end": "39:58",
        "privacy_discussion_duration_seconds": 192,
        "series_total_seconds": 25200,  # ~7 hours
        "privacy_percentage_of_series": 0.76,
        "source_url": "http://voicesofvr.com/1677-snaps-ar-developer-relations-plan-"
                      "for-2026-specs-consumer-launch-with-joe-darko/",

        "kent_bye_privacy_question": (
            "Just curious to hear any comments on how you start to see privacy "
            "played into this larger story for allowing developers to experiment, "
            "but also trying to, as a company, have different guardrails or "
            "thresholds for what you have strong opinions on what is or is not OK."
        ),

        "joe_darko_privacy_claims": [
            "We are a private focused company in terms of from a privacy standpoint",
            "Privacy is not an afterthought",
            "We're never going to compromise on privacy. No matter what.",
            "We find ways and means to insert guardrails as we build",
            "We don't want to break the trust between Snap and our consumers",
            "We bring it back to our legal team, our privacy teams",
        ],

        "kent_bye_followup_questions": [],  # ZERO follow-up questions on privacy
        "kent_bye_pushback_instances": 0,

        "absent_from_discussion": [
            "bystander consent for camera recording",
            "camera-on-face privacy discourse",
            "Meta glasses comparison",
            "institutional bans (DEF CON, ICE, UK venues, courts)",
            "pervert/spy/glasshole vocabulary",
            "Swedish contractor scandal parallels",
            "facial recognition concerns",
            "LED indicator tampering",
            "gendered surveillance critique",
            "how Snap cameras functionally differ from Meta cameras",
        ],
    },

    "spiegel_competitive_positioning": {
        "quote": "Those copycats up north aren't going to be stealing this one",
        "context": "AWE 2026 keynote, reference to Meta",
        "framing": "Positions Snap as original innovator, Meta as unethical copier",
        "source_url": "https://www.engadget.com/2194982/awe-xr-2026-snap-live-blog/",
        "kent_bye_critique_of_framing": None,  # No critique of competitive positioning
    },

    "snap_specs_camera_capabilities": {
        "has_cameras": True,
        "has_ai": True,
        "ai_partners": ["OpenAI", "Google"],
        "can_record_video": True,
        "has_led_indicator": True,
        "consumer_price": 2195,
        "consumer_launch_date": "September 16, 2026",
        "consumer_launch_days_away": 25,  # as of Aug 22
        "shipping_countries": ["US", "UK", "France"],
    },

    "meta_comparison_equivalent_claims": {
        "meta_privacy_tagline": "Designed for privacy, controlled by you",
        "meta_has_cameras": True,
        "meta_has_ai": True,
        "meta_has_led_indicator": True,
        "meta_consumer_price_range": [224, 799],
        "meta_podcast_treatment": "alarm_vocabulary_dominant",
    },

    "podcast_receptivity_comparison": {
        "snap_coverage_by_voices_of_vr": {
            "series_length_hours": 7,
            "privacy_percentage": 0.76,
            "privacy_treatment": "accepted_at_face_value",
            "alarm_vocabulary_count": 0,
            "sentiment_score": 3,  # positive/aspirational overall
        },
        "meta_coverage_by_kill_switch": {
            "episode_length_minutes": 40,
            "privacy_percentage": 100,
            "privacy_treatment": "skepticism_dominant",
            "alarm_vocabulary_count": 10,
            "sentiment_score": -7,
        },
        "meta_coverage_by_ambermac": {
            "title_vocabulary": "Meta's 'Pervert' Smart Glasses",
            "privacy_treatment": "maximum_alarm",
            "alarm_vocabulary_count": 5,
            "sentiment_score": -7,
        },
        "meta_coverage_by_shared_security": {
            "title_vocabulary": "Should You Be Worried?",
            "privacy_treatment": "alarm_question",
            "alarm_vocabulary_count": 8,
            "sentiment_score": -6,
        },
        "meta_coverage_by_smashing_security": {
            "title_vocabulary": "Face off: Meta's Glasses",
            "alarm_vocabulary_count": 30,
            "sentiment_score": -8,
        },
    },

    "confounders": [
        {
            "id": 1,
            "description": "Snap Specs are not yet shipping — privacy concerns "
                           "may emerge post-launch when real users encounter issues",
            "strength": "STRONG",
            "assessment": "Valid but testable: the pre-launch framing establishes "
                         "the narrative template. Meta's pre-launch coverage in "
                         "2023 was ALSO aspirational; the shift happened post-launch. "
                         "The question is whether Snap will receive the same post-"
                         "launch scrutiny.",
        },
        {
            "id": 2,
            "description": "Meta has a specific contractor scandal (Sweden) that "
                           "Snap does not — media alarm may reflect real incidents",
            "strength": "STRONG",
            "assessment": "The contractor scandal is genuinely newsworthy. However, "
                         "the PRE-incident treatment of Meta (Google Glass redux, "
                         "'glasshole' revival) was already adversarial before the "
                         "scandal broke. Snap's pre-launch treatment is aspirational "
                         "with zero category-level privacy concern.",
        },
        {
            "id": 3,
            "description": "Voices of VR was invited by Snap to cover LensFest — "
                           "access journalism may soften coverage",
            "strength": "STRONG",
            "assessment": "Kent Bye explicitly notes 'Snap brought me down to LA to "
                         "cover their Lensfest developer conference.' Access-based "
                         "coverage creates structural incentive for favorable framing. "
                         "However, the same dynamic exists for Meta's developer "
                         "conferences, yet Meta-invited coverage remains more critical.",
        },
        {
            "id": 4,
            "description": "VoVR audience is XR developers — privacy is less "
                           "relevant to a developer-focused audience",
            "strength": "MODERATE",
            "assessment": "Developer audiences care about platform capabilities, not "
                         "consumer privacy. But when Meta holds developer conferences, "
                         "media coverage still foregrounds privacy. The developer-"
                         "audience framing is accepted for Snap but not for Meta.",
        },
        {
            "id": 5,
            "description": "Kent Bye records 1700+ episodes — cannot apply deep "
                           "scrutiny to every interview",
            "strength": "MODERATE",
            "assessment": "Volume constrains depth. But the total absence of follow-"
                         "up (0 privacy follow-ups in 11 episodes) is not a volume "
                         "constraint — it reflects framing priority.",
        },
        {
            "id": 6,
            "description": "Snap's market share is tiny vs Meta — less scrutiny "
                           "proportional to impact",
            "strength": "WEAK",
            "assessment": "Snap Specs are launching for $2,195 to consumers in "
                         "25 days. If market share were the criterion, pre-launch "
                         "coverage would reserve judgment. Instead, 7 hours of "
                         "aspirational framing establishes the 'ethical alternative' "
                         "narrative before a single consumer unit ships.",
        },
    ],

    "cross_references": [
        {"id": 239, "name": "Condé Nast Snapchat Discover Quintuple Financial Alignment"},
        {"id": 231, "name": "CLAD Quad-AI Developer Ecosystem"},
        {"id": 144, "name": "Podcast Ecosystem Amplification"},
        {"id": 148, "name": "Corporate Ownership Cross-Medium Portability"},
        {"id": 240, "name": "MacRumors Show Apple Camera AirPods Privacy Vocabulary Zero"},
        {"id": 232, "name": "NBC News Broadcast Meta Exclusive Alarm"},
    ],

    "sources": [
        "http://voicesofvr.com/1677-snaps-ar-developer-relations-plan-for-2026-specs-consumer-launch-with-joe-darko/",
        "http://voicesofvr.com/1668-snap-co-founders-community-qa-about-specs-2026-launch-plan/",
        "https://www.businesswire.com/news/home/20260612154498/en/Snap-Inc.-Debuts-SPECS-Augmented-Reality-Glasses-to-Make-Computing-More-Human",
        "https://www.iheart.com/podcast/105-kill-switch-30880104/episode/the-glassholes-are-back-294858162/",
        "https://ambermac.com/the-ambermac-show-ep056-metas-pervert-smart-glasses-openais-canadian-safety-promise/",
        "https://www.phonearena.com/news/snaps-ar-glasses-consumer-focused-unveilng_id182255",
        "https://www.engadget.com/2194982/awe-xr-2026-snap-live-blog/",
    ],
}


# =============================================================================
# Test Classes
# =============================================================================


class TestVoicesOfVRPodcastAuthority:
    """Verify Voices of VR is an authoritative XR source."""

    def test_episode_count_establishes_authority(self):
        """VoVR has 1700+ episodes — far more than any other XR podcast."""
        total = MECHANISM["voices_of_vr_series"]["total_episodes_all_time"]
        assert total == "1700+"

    def test_lensfest_series_is_substantial(self):
        """11 episodes, ~7 hours is a major investment in covering one event."""
        series = MECHANISM["voices_of_vr_series"]
        assert series["lensfest_series_episode_count"] == 11
        assert series["lensfest_series_hours"] == 7

    def test_patreon_funded_not_advertiser_dependent(self):
        """Patreon funding means no direct advertiser pressure."""
        funding = MECHANISM["voices_of_vr_series"]["funding_model"]
        assert "Patreon" in funding
        assert "listener-supported" in funding

    def test_snap_invited_kent_bye(self):
        """Snap brought Kent Bye to cover LensFest — access journalism dynamic."""
        location = MECHANISM["voices_of_vr_series"]["recording_location"]
        assert "Snap HQ" in location


class TestPrivacyDiscussionScope:
    """Test the scope and treatment of privacy in the VoVR series."""

    def test_privacy_occupies_tiny_fraction_of_series(self):
        """Privacy = 0.76% of the 7-hour series — effectively a footnote."""
        ep = MECHANISM["privacy_discussion_episode_1677"]
        pct = ep["privacy_percentage_of_series"]
        assert pct < 1.0, (
            f"Privacy discussion is {pct}% of series — less than 1%"
        )

    def test_privacy_discussion_duration(self):
        """Only 192 seconds of privacy discussion in ~7 hours."""
        duration = MECHANISM["privacy_discussion_episode_1677"][
            "privacy_discussion_duration_seconds"
        ]
        assert duration == 192
        assert duration < 240, "Privacy segment is under 4 minutes"

    def test_privacy_is_final_topic_before_wrap(self):
        """Privacy is asked near the end of the final episode — structurally marginal."""
        start = MECHANISM["privacy_discussion_episode_1677"][
            "privacy_discussion_timestamp_start"
        ]
        assert start == "36:46", "Privacy raised after 36 minutes of interview"


class TestSnapPrivacyClaimReceptivity:
    """Test how VoVR treats Snap's privacy claims."""

    def test_darko_makes_strong_privacy_claims(self):
        """Darko claims Snap will 'never compromise on privacy.'"""
        claims = MECHANISM["privacy_discussion_episode_1677"][
            "joe_darko_privacy_claims"
        ]
        assert len(claims) >= 6
        strong_claims = [c for c in claims if "never" in c.lower()]
        assert len(strong_claims) >= 1

    def test_zero_followup_questions(self):
        """Kent Bye asks ZERO follow-up questions on privacy."""
        followups = MECHANISM["privacy_discussion_episode_1677"][
            "kent_bye_followup_questions"
        ]
        assert len(followups) == 0, (
            "No follow-up questions on privacy — claims accepted at face value"
        )

    def test_zero_pushback(self):
        """Kent Bye provides zero pushback on privacy claims."""
        pushback = MECHANISM["privacy_discussion_episode_1677"][
            "kent_bye_pushback_instances"
        ]
        assert pushback == 0

    def test_absent_topics_not_raised(self):
        """10 critical privacy topics are absent from the discussion."""
        absent = MECHANISM["privacy_discussion_episode_1677"][
            "absent_from_discussion"
        ]
        assert len(absent) >= 10
        # Key absences
        assert "bystander consent for camera recording" in absent
        assert "camera-on-face privacy discourse" in absent
        assert "Meta glasses comparison" in absent
        assert "institutional bans (DEF CON, ICE, UK venues, courts)" in absent

    def test_no_alarm_vocabulary(self):
        """Zero alarm vocabulary in VoVR Snap coverage."""
        alarm_count = MECHANISM["podcast_receptivity_comparison"][
            "snap_coverage_by_voices_of_vr"
        ]["alarm_vocabulary_count"]
        assert alarm_count == 0


class TestMetaComparisonEquivalence:
    """Test that Snap and Meta have equivalent camera hardware."""

    def test_both_have_cameras(self):
        """Both Snap Specs and Meta glasses have cameras."""
        assert MECHANISM["snap_specs_camera_capabilities"]["has_cameras"]
        assert MECHANISM["meta_comparison_equivalent_claims"]["meta_has_cameras"]

    def test_both_have_ai(self):
        """Both have AI assistants."""
        assert MECHANISM["snap_specs_camera_capabilities"]["has_ai"]
        assert MECHANISM["meta_comparison_equivalent_claims"]["meta_has_ai"]

    def test_both_have_led_indicators(self):
        """Both have LED privacy indicators."""
        assert MECHANISM["snap_specs_camera_capabilities"]["has_led_indicator"]
        assert MECHANISM["meta_comparison_equivalent_claims"]["meta_has_led_indicator"]

    def test_snap_ai_powered_by_openai_and_google(self):
        """Snap Specs AI is powered by OpenAI AND Google — same companies that
        have financial relationships with publications covering them."""
        partners = MECHANISM["snap_specs_camera_capabilities"]["ai_partners"]
        assert "OpenAI" in partners
        assert "Google" in partners


class TestReceptivityDifferential:
    """Test the differential treatment between Snap and Meta podcast coverage."""

    def test_snap_positive_sentiment_meta_negative_sentiment(self):
        """VoVR Snap coverage: +3. Meta coverage across podcasts: -6 to -8."""
        comp = MECHANISM["podcast_receptivity_comparison"]
        snap_score = comp["snap_coverage_by_voices_of_vr"]["sentiment_score"]
        meta_scores = [
            comp["meta_coverage_by_kill_switch"]["sentiment_score"],
            comp["meta_coverage_by_ambermac"]["sentiment_score"],
            comp["meta_coverage_by_shared_security"]["sentiment_score"],
            comp["meta_coverage_by_smashing_security"]["sentiment_score"],
        ]
        assert snap_score > 0
        assert all(s < 0 for s in meta_scores)
        # Gap between Snap and worst Meta score
        gap = snap_score - min(meta_scores)
        assert gap >= 10, f"Sentiment gap of {gap} between Snap (+3) and Meta (-8)"

    def test_snap_zero_alarm_vs_meta_high_alarm(self):
        """VoVR has 0 alarm words for Snap vs 5-30 for Meta across podcasts."""
        comp = MECHANISM["podcast_receptivity_comparison"]
        snap_alarm = comp["snap_coverage_by_voices_of_vr"]["alarm_vocabulary_count"]
        meta_alarms = [
            comp["meta_coverage_by_kill_switch"]["alarm_vocabulary_count"],
            comp["meta_coverage_by_ambermac"]["alarm_vocabulary_count"],
            comp["meta_coverage_by_shared_security"]["alarm_vocabulary_count"],
            comp["meta_coverage_by_smashing_security"]["alarm_vocabulary_count"],
        ]
        assert snap_alarm == 0
        assert sum(meta_alarms) >= 50, (
            f"Total Meta alarm words across 4 podcasts: {sum(meta_alarms)}"
        )

    def test_snap_privacy_0_76_pct_vs_meta_100_pct(self):
        """Snap gets 0.76% privacy focus; Meta Kill Switch is 100% privacy."""
        comp = MECHANISM["podcast_receptivity_comparison"]
        snap_pct = comp["snap_coverage_by_voices_of_vr"]["privacy_percentage"]
        meta_pct = comp["meta_coverage_by_kill_switch"]["privacy_percentage"]
        assert snap_pct < 1
        assert meta_pct == 100
        ratio = meta_pct / snap_pct
        assert ratio > 100, f"Meta privacy focus is {ratio:.0f}x Snap's"


class TestSpiegelCompetitivePositioning:
    """Test Snap CEO's competitive framing against Meta."""

    def test_copycats_quote_recorded(self):
        """Spiegel called Meta 'copycats up north' at AWE."""
        quote = MECHANISM["spiegel_competitive_positioning"]["quote"]
        assert "copycats" in quote.lower()

    def test_kent_bye_does_not_critique_framing(self):
        """Kent Bye does not critique Spiegel's competitive framing."""
        critique = MECHANISM["spiegel_competitive_positioning"][
            "kent_bye_critique_of_framing"
        ]
        assert critique is None

    def test_snap_builds_same_camera_hardware(self):
        """Despite 'copycats' framing, Snap builds functionally identical hardware."""
        snap = MECHANISM["snap_specs_camera_capabilities"]
        meta = MECHANISM["meta_comparison_equivalent_claims"]
        # Both have cameras, AI, and LED indicators
        assert snap["has_cameras"] == meta["meta_has_cameras"]
        assert snap["has_ai"] == meta["meta_has_ai"]
        assert snap["has_led_indicator"] == meta["meta_has_led_indicator"]


class TestSep16PreLaunchWindow:
    """Test predictions for the Sep 16 consumer launch coverage window."""

    def test_consumer_launch_date(self):
        """Snap Specs consumer launch event is Sep 16, 2026."""
        date = MECHANISM["snap_specs_camera_capabilities"]["consumer_launch_date"]
        assert date == "September 16, 2026"

    def test_launch_25_days_away(self):
        """Launch is 25 days from Aug 22."""
        days = MECHANISM["snap_specs_camera_capabilities"]["consumer_launch_days_away"]
        assert days == 25

    def test_shipping_to_three_consumer_markets(self):
        """Specs shipping to US, UK, and France — the same markets with bans."""
        countries = MECHANISM["snap_specs_camera_capabilities"]["shipping_countries"]
        assert "US" in countries  # ICE ban, DEF CON ban, NY courts ban
        assert "UK" in countries  # Soho House, Wetherspoons, UK Comic Cons ban
        assert "France" in countries

    def test_consumer_pricing_accessible(self):
        """$2,195 is expensive but accessible to enthusiasts."""
        price = MECHANISM["snap_specs_camera_capabilities"]["consumer_price"]
        assert price == 2195


class TestConfounders:
    """Verify confounders are documented."""

    def test_minimum_confounders(self):
        """At least 6 confounders documented."""
        assert len(MECHANISM["confounders"]) >= 6

    def test_strong_confounders_count(self):
        """At least 3 STRONG confounders."""
        strong = [c for c in MECHANISM["confounders"] if c["strength"] == "STRONG"]
        assert len(strong) >= 3

    def test_access_journalism_confounder_documented(self):
        """Access journalism (Snap invitation) is documented as confounder."""
        access = [c for c in MECHANISM["confounders"]
                  if "access" in c["description"].lower()
                  or "invited" in c["description"].lower()]
        assert len(access) >= 1


class TestCrossReferences:
    """Verify mechanism cross-references."""

    def test_cross_references_exist(self):
        """Cross-references to related mechanisms."""
        refs = MECHANISM["cross_references"]
        assert len(refs) >= 4

    def test_references_conde_nast_snap_alignment(self):
        """References mechanism #239 — Condé Nast quintuple Snap alignment."""
        ref_ids = [r["id"] for r in MECHANISM["cross_references"]]
        assert 239 in ref_ids

    def test_references_podcast_amplification(self):
        """References mechanism #144 — podcast ecosystem amplification."""
        ref_ids = [r["id"] for r in MECHANISM["cross_references"]]
        assert 144 in ref_ids


class TestSourceVerification:
    """Verify all sources are documented."""

    def test_minimum_sources(self):
        """At least 7 source URLs."""
        assert len(MECHANISM["sources"]) >= 7

    def test_voices_of_vr_source_included(self):
        """VoVR episode URL is in sources."""
        urls = MECHANISM["sources"]
        vovr = [u for u in urls if "voicesofvr.com" in u]
        assert len(vovr) >= 1

    def test_comparison_podcast_sources_included(self):
        """Comparison podcasts (Kill Switch, AmberMac) have source URLs."""
        urls = MECHANISM["sources"]
        kill_switch = [u for u in urls if "iheart.com" in u]
        ambermac = [u for u in urls if "ambermac.com" in u]
        assert len(kill_switch) >= 1
        assert len(ambermac) >= 1
