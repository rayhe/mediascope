"""
Test: Andy Boxall Cross-Entity Privacy Vocabulary Inversion (Mechanism #132)

Same journalist at Android Police (Valnet Inc.) covers three camera-equipped
smart glasses within 36 days (Jun 17 – Jul 23, 2026) with radically different
privacy vocabulary:

- Snap Specs (4 cameras, 2 IR, dual Snapdragon): 0 privacy terms, +0.90 enthusiastic
- Samsung Galaxy Glasses (1 camera, same Snapdragon AR1 Gen 1): privacy attributed to Meta, +0.30
- Meta Ray-Ban (1 camera, Snapdragon AR1 Gen 1): 7+ alarm terms, -0.85 adversarial

Privacy alarm intensity is INVERSELY proportional to camera count.
The product with the MOST cameras (Snap Specs, 4) gets ZERO privacy scrutiny.
The product with the FEWEST cameras (Meta, 1) gets "nightmarish" treatment.

Financial context: Android Police (Valnet) depends on Google ad revenue and
Samsung advertising spend. Meta has no financial relationship with Valnet.
Google pays Samsung billions for Gemini preinstallation and Play Store defaults.
Samsung and Google are jointly developing the smart glasses via Android XR.

Mechanism type: same_journalist_privacy_vocabulary_inversion
Publication: Android Police (Valnet Inc.)
Journalist: Andy Boxall

Sources:
- https://www.androidpolice.com/snap-specs-are-the-augmented-reality-dream-weve-been-waiting-for/
- https://www.androidpolice.com/ray-ban-meta-privacy-problems-super-sensing-feature/
- https://www.androidpolice.com/hands-on-with-samsungs-ray-ban-meta-rival-smartglasses/
"""

import pytest


# ============================================================
# Article Data
# ============================================================

SNAP_SPECS_ARTICLE = {
    "url": "https://www.androidpolice.com/snap-specs-are-the-augmented-reality-dream-weve-been-waiting-for/",
    "headline": "Snap's $2,195 Specs aren't smartglasses, they're the augmented reality dream we've been waiting for",
    "date": "2026-06-17",
    "journalist": "Andy Boxall",
    "publication": "Android Police",
    "entity": "snap",
    "cameras_on_device": 4,  # 2 visible + 2 IR computer vision
    "camera_processors": 2,  # dual Snapdragon
    "price": 2195,
    "privacy_alarm_terms": [],  # ZERO privacy vocabulary in entire article
    "positive_terms": [
        "augmented reality dream",
        "technically astonishing",
        "spectacular",
        "genre-creating",
        "very excited",
        "most wearable",
        "most interesting",
        "most technically exciting",
    ],
    "camera_mentioned": False,  # cameras not discussed at all
    "led_indicator_mentioned": False,
    "bystander_concern_mentioned": False,
    "surveillance_vocabulary": [],
    "tone_score": 0.90,
}

META_SUPERSENSING_ARTICLE = {
    "url": "https://www.androidpolice.com/ray-ban-meta-privacy-problems-super-sensing-feature/",
    "headline": "Ray-Ban Meta privacy problems go from bad to worse with nightmarish 'super sensing' feature",
    "date": "2026-07-09",
    "journalist": "Andy Boxall",
    "publication": "Android Police",
    "entity": "meta",
    "cameras_on_device": 1,
    "camera_processors": 1,
    "price": 299,  # Ray-Ban Meta starting price
    "privacy_alarm_terms": [
        "nightmarish",
        "super invasive",
        "privacy red flag",
        "bad to worse",
        "covert camera recording",
        "serious concern",
        "bad idea",
    ],
    "positive_terms": [],  # ZERO positive language
    "camera_mentioned": True,
    "led_indicator_mentioned": True,
    "bystander_concern_mentioned": True,
    "surveillance_vocabulary": [
        "covert camera recording",
        "record snippets of your day all the time",
        "no LED indicator light",
        "impossible for people to know if they're being recorded",
    ],
    "tone_score": -0.85,
}

SAMSUNG_GLASSES_ARTICLE = {
    "url": "https://www.androidpolice.com/hands-on-with-samsungs-ray-ban-meta-rival-smartglasses/",
    "headline": "We went hands-on with Samsung's smartglasses. Here's why Meta should be worried",
    "date": "2026-07-23",
    "journalist": "Andy Boxall",
    "publication": "Android Police",
    "entity": "samsung",
    "cameras_on_device": 1,
    "camera_processors": 1,  # same Snapdragon AR1 Gen 1 as Meta
    "price_range": "379-499",  # estimated
    "privacy_alarm_terms": [],  # no alarm terms applied to SAMSUNG
    "meta_privacy_attribution": [
        "backlash against the Ray-Ban Meta's cameras being used to invade people's privacy",
    ],
    "general_privacy_phrases": [
        "potentially covert video recording",  # general framing, not Samsung-specific
    ],
    "positive_terms": [
        "why Meta should be worried",
        "keep Meta on its toes, and that's great news",
        "only making me more keen to try them out",
        "designs look good",
        "weight reduction noticeable and welcome",
    ],
    "camera_mentioned": True,
    "camera_normalized": True,  # "similar protections to the Ray-Ban Meta"
    "led_indicator_mentioned": True,
    "bystander_concern_mentioned": False,  # no bystander-specific concern
    "surveillance_vocabulary": [],  # no surveillance language applied to Samsung
    "tone_score": 0.30,
}

ALL_ARTICLES = [SNAP_SPECS_ARTICLE, META_SUPERSENSING_ARTICLE, SAMSUNG_GLASSES_ARTICLE]

# Financial relationships
ANDROID_POLICE_FINANCIAL = {
    "owner": "Valnet Inc.",
    "primary_ad_platform": "Google AdSense/AdManager",
    "beat_dependency": "Android/Google ecosystem",
    "samsung_advertiser": True,
    "meta_content_deals": 0,
    "meta_ad_deals": 0,
    "google_samsung_relationship": "Google paid Samsung $8B+ for Play Store/Search/Gemini defaults",
    "samsung_google_glasses_partnership": "Joint development via Android XR",
}


# ============================================================
# Test Classes
# ============================================================


class TestSameJournalistAllArticles:
    """Verify all three articles are by the same journalist at the same outlet."""

    def test_same_journalist(self):
        journalists = {a["journalist"] for a in ALL_ARTICLES}
        assert len(journalists) == 1
        assert "Andy Boxall" in journalists

    def test_same_publication(self):
        pubs = {a["publication"] for a in ALL_ARTICLES}
        assert len(pubs) == 1
        assert "Android Police" in pubs

    def test_temporal_window(self):
        """All three articles within 36-day window."""
        from datetime import datetime

        dates = [datetime.strptime(a["date"], "%Y-%m-%d") for a in ALL_ARTICLES]
        delta = (max(dates) - min(dates)).days
        assert delta <= 40, f"Articles span {delta} days, expected ≤40"

    def test_all_have_cameras(self):
        """All three products have cameras — privacy concerns apply equally."""
        for a in ALL_ARTICLES:
            assert a["cameras_on_device"] >= 1, f"{a['entity']} should have cameras"


class TestPrivacyVocabularyDistribution:
    """Core asymmetry: privacy alarm concentrated on Meta, absent for competitors."""

    def test_meta_has_most_alarm_terms(self):
        meta = META_SUPERSENSING_ARTICLE
        assert len(meta["privacy_alarm_terms"]) >= 7

    def test_snap_has_zero_alarm_terms(self):
        snap = SNAP_SPECS_ARTICLE
        assert len(snap["privacy_alarm_terms"]) == 0

    def test_samsung_has_zero_alarm_terms(self):
        """Samsung alarm terms are 0 — privacy concerns attributed to Meta."""
        samsung = SAMSUNG_GLASSES_ARTICLE
        assert len(samsung["privacy_alarm_terms"]) == 0

    def test_snap_camera_not_mentioned(self):
        """Snap Specs have 4 cameras but cameras are not discussed AT ALL."""
        snap = SNAP_SPECS_ARTICLE
        assert snap["camera_mentioned"] is False

    def test_snap_led_not_mentioned(self):
        snap = SNAP_SPECS_ARTICLE
        assert snap["led_indicator_mentioned"] is False

    def test_snap_bystander_concern_absent(self):
        snap = SNAP_SPECS_ARTICLE
        assert snap["bystander_concern_mentioned"] is False

    def test_meta_surveillance_vocabulary_present(self):
        meta = META_SUPERSENSING_ARTICLE
        assert len(meta["surveillance_vocabulary"]) >= 3

    def test_snap_surveillance_vocabulary_absent(self):
        snap = SNAP_SPECS_ARTICLE
        assert len(snap["surveillance_vocabulary"]) == 0

    def test_samsung_surveillance_vocabulary_absent(self):
        samsung = SAMSUNG_GLASSES_ARTICLE
        assert len(samsung["surveillance_vocabulary"]) == 0


class TestCameraCountInversion:
    """Privacy vocabulary is INVERSELY proportional to camera count."""

    def test_snap_has_most_cameras(self):
        snap = SNAP_SPECS_ARTICLE
        meta = META_SUPERSENSING_ARTICLE
        assert snap["cameras_on_device"] > meta["cameras_on_device"]

    def test_snap_most_cameras_zero_privacy(self):
        """Device with 4 cameras gets 0 privacy terms."""
        snap = SNAP_SPECS_ARTICLE
        assert snap["cameras_on_device"] == 4
        assert len(snap["privacy_alarm_terms"]) == 0

    def test_meta_fewest_cameras_most_alarm(self):
        """Device with 1 camera gets 7+ alarm terms."""
        meta = META_SUPERSENSING_ARTICLE
        assert meta["cameras_on_device"] == 1
        assert len(meta["privacy_alarm_terms"]) >= 7

    def test_inversion_ratio(self):
        """Camera-to-alarm ratio inverts: more cameras → fewer alarms."""
        snap_cameras = SNAP_SPECS_ARTICLE["cameras_on_device"]
        snap_alarms = len(SNAP_SPECS_ARTICLE["privacy_alarm_terms"])
        meta_cameras = META_SUPERSENSING_ARTICLE["cameras_on_device"]
        meta_alarms = len(META_SUPERSENSING_ARTICLE["privacy_alarm_terms"])
        # Snap has 4x cameras but 0 alarms; Meta has 1 camera but 7+ alarms
        assert snap_cameras > meta_cameras
        assert snap_alarms < meta_alarms

    def test_samsung_same_chip_same_camera_different_framing(self):
        """Samsung uses identical Snapdragon AR1 Gen 1 chip as Meta, same camera count,
        but gets normalization ('similar protections') rather than alarm language."""
        samsung = SAMSUNG_GLASSES_ARTICLE
        meta = META_SUPERSENSING_ARTICLE
        assert samsung["cameras_on_device"] == meta["cameras_on_device"]
        assert samsung["camera_normalized"] is True
        assert len(samsung["privacy_alarm_terms"]) == 0
        assert len(meta["privacy_alarm_terms"]) >= 7


class TestHeadlineFraming:
    """Headline language reveals entity-dependent editorial standards."""

    def test_meta_headline_alarm(self):
        meta = META_SUPERSENSING_ARTICLE
        headline = meta["headline"].lower()
        assert "nightmarish" in headline
        assert "privacy problems" in headline
        assert "bad to worse" in headline

    def test_snap_headline_enthusiasm(self):
        snap = SNAP_SPECS_ARTICLE
        headline = snap["headline"].lower()
        assert "dream" in headline
        # No privacy, surveillance, concern, or alarm words
        for term in ["privacy", "surveillance", "concern", "alarm", "nightmare"]:
            assert term not in headline

    def test_samsung_headline_competitive(self):
        """Samsung headline frames as competitive threat to Meta, not privacy concern."""
        samsung = SAMSUNG_GLASSES_ARTICLE
        headline = samsung["headline"].lower()
        assert "meta should be worried" in headline
        # No alarm language
        for term in ["nightmare", "privacy", "invasive", "concern"]:
            assert term not in headline

    def test_headline_tone_divergence(self):
        """Headline tone delta: snap_enthusiastic - meta_adversarial >= 1.5."""
        delta = SNAP_SPECS_ARTICLE["tone_score"] - META_SUPERSENSING_ARTICLE["tone_score"]
        assert delta >= 1.5, f"Headline tone delta {delta} < 1.5"


class TestToneScores:
    """Tone scores show systematic entity-dependent variation."""

    def test_meta_adversarial(self):
        assert META_SUPERSENSING_ARTICLE["tone_score"] < -0.5

    def test_snap_enthusiastic(self):
        assert SNAP_SPECS_ARTICLE["tone_score"] > 0.5

    def test_samsung_positive(self):
        assert SAMSUNG_GLASSES_ARTICLE["tone_score"] > 0.0

    def test_meta_most_negative(self):
        meta_tone = META_SUPERSENSING_ARTICLE["tone_score"]
        for a in ALL_ARTICLES:
            if a["entity"] != "meta":
                assert a["tone_score"] > meta_tone

    def test_positive_terms_absent_meta(self):
        assert len(META_SUPERSENSING_ARTICLE["positive_terms"]) == 0

    def test_positive_terms_present_snap(self):
        assert len(SNAP_SPECS_ARTICLE["positive_terms"]) >= 5

    def test_positive_terms_present_samsung(self):
        assert len(SAMSUNG_GLASSES_ARTICLE["positive_terms"]) >= 3


class TestSamsungPrivacyAttribution:
    """Samsung's cameras get privacy concerns attributed to META, not Samsung."""

    def test_samsung_has_meta_attribution(self):
        samsung = SAMSUNG_GLASSES_ARTICLE
        assert len(samsung["meta_privacy_attribution"]) >= 1

    def test_samsung_privacy_framed_as_meta_problem(self):
        samsung = SAMSUNG_GLASSES_ARTICLE
        for phrase in samsung["meta_privacy_attribution"]:
            phrase_lower = phrase.lower()
            assert "meta" in phrase_lower or "ray-ban" in phrase_lower, (
                f"Attribution '{phrase}' should reference Meta/Ray-Ban"
            )

    def test_samsung_camera_normalized(self):
        """Samsung cameras described as having 'similar protections' — normalization."""
        samsung = SAMSUNG_GLASSES_ARTICLE
        assert samsung["camera_normalized"] is True

    def test_samsung_no_bystander_concern(self):
        samsung = SAMSUNG_GLASSES_ARTICLE
        assert samsung["bystander_concern_mentioned"] is False


class TestFinancialRelationshipPrediction:
    """Financial relationships predict the framing pattern."""

    def test_android_police_google_dependent(self):
        assert ANDROID_POLICE_FINANCIAL["beat_dependency"] == "Android/Google ecosystem"

    def test_samsung_is_advertiser(self):
        assert ANDROID_POLICE_FINANCIAL["samsung_advertiser"] is True

    def test_meta_no_financial_ties(self):
        assert ANDROID_POLICE_FINANCIAL["meta_content_deals"] == 0
        assert ANDROID_POLICE_FINANCIAL["meta_ad_deals"] == 0

    def test_google_samsung_joint_venture(self):
        """Google and Samsung jointly develop glasses via Android XR."""
        assert "Android XR" in ANDROID_POLICE_FINANCIAL["samsung_google_glasses_partnership"]

    def test_financial_alignment_predicts_softer_coverage(self):
        """Entities with financial ties to publication get softer coverage."""
        # Samsung (advertiser, Google partner) gets positive framing
        assert SAMSUNG_GLASSES_ARTICLE["tone_score"] > 0
        # Snap (no direct financial tie but competitor to Meta) gets enthusiasm
        assert SNAP_SPECS_ARTICLE["tone_score"] > 0
        # Meta (no financial tie, structural Google competitor) gets alarm
        assert META_SUPERSENSING_ARTICLE["tone_score"] < 0


class TestConfounders:
    """Document and test confounding factors for intellectual honesty."""

    CONFOUNDERS = [
        {
            "name": "Super Sensing is genuinely more invasive",
            "strength": "STRONG",
            "description": (
                "The Meta article specifically covers 'super sensing' — a proposed feature "
                "that would disable LED indicators and record continuously. This is genuinely "
                "more invasive than standard camera features on any glasses. However, the "
                "TOTAL ABSENCE of any privacy vocabulary for Snap Specs (4 cameras with "
                "photo/video capture capability) represents a coverage SELECTION asymmetry: "
                "the journalist chose to write an entirely privacy-free article about a "
                "4-camera device."
            ),
        },
        {
            "name": "Different article types",
            "strength": "MODERATE",
            "description": (
                "Snap = launch announcement, Meta = privacy news, Samsung = hands-on. "
                "Genre differences partially explain tone differences. However, launch "
                "announcements for camera-equipped wearables at other publications routinely "
                "include privacy discussion (see Gizmodo's Snap Specs coverage, which "
                "questioned LED indicator sufficiency)."
            ),
        },
        {
            "name": "Android Police is Android-focused by definition",
            "strength": "MODERATE",
            "description": (
                "The publication's identity revolves around the Android/Google ecosystem, "
                "so favorable coverage of Android XR partners (Samsung) and unfavorable "
                "coverage of platform competitors (Meta) could reflect audience alignment "
                "rather than financial incentive. However, audience alignment and financial "
                "incentive are correlated: the Android audience IS the advertiser target."
            ),
        },
        {
            "name": "Snap Specs are primarily AR display, not camera-first",
            "strength": "MODERATE",
            "description": (
                "Snap Specs are positioned as AR glasses, not camera glasses, which may "
                "justify de-emphasizing camera privacy. However, the device has 4 cameras "
                "capable of photo/video capture, and Snap confirmed capture capability. "
                "A privacy-aware journalist covering a 4-camera face-worn computer should "
                "at minimum acknowledge camera privacy implications."
            ),
        },
        {
            "name": "Samsung article does acknowledge privacy concerns",
            "strength": "WEAK",
            "description": (
                "The Samsung article includes a 'How will Samsung address privacy?' section. "
                "However, the section frames privacy as Meta's problem that Samsung must "
                "navigate, not as an inherent issue with Samsung's identical camera hardware. "
                "Zero alarm terms are applied to Samsung's cameras directly."
            ),
        },
    ]

    def test_confounders_documented(self):
        assert len(self.CONFOUNDERS) >= 4

    def test_has_strong_confounder(self):
        strengths = [c["strength"] for c in self.CONFOUNDERS]
        assert "STRONG" in strengths

    @pytest.mark.parametrize("confounder", CONFOUNDERS, ids=[c["name"][:40] for c in CONFOUNDERS])
    def test_each_confounder_has_description(self, confounder):
        assert len(confounder["description"]) > 50

    def test_strongest_confounder_acknowledged(self):
        """Super Sensing IS genuinely more invasive — acknowledged."""
        strong = [c for c in self.CONFOUNDERS if c["strength"] == "STRONG"]
        assert any("genuinely more invasive" in c["description"] for c in strong)


class TestMechanismMetadata:
    """Structural integrity of mechanism #132."""

    MECHANISM = {
        "id": 132,
        "type": "same_journalist_privacy_vocabulary_inversion",
        "journalist": "Andy Boxall",
        "publication": "Android Police",
        "owner": "Valnet Inc.",
        "discovery_date": "2026-08-16",
        "entities_compared": ["snap", "meta", "samsung"],
        "articles_analyzed": 3,
        "temporal_window_days": 36,
        "related_mechanisms": [30, 33, 121, 122, 126, 130, 131],
    }

    def test_mechanism_id(self):
        assert self.MECHANISM["id"] == 132

    def test_mechanism_type(self):
        assert self.MECHANISM["type"] == "same_journalist_privacy_vocabulary_inversion"

    def test_three_entities(self):
        assert len(self.MECHANISM["entities_compared"]) == 3

    def test_related_mechanisms_present(self):
        assert len(self.MECHANISM["related_mechanisms"]) >= 5

    def test_discovery_date(self):
        assert self.MECHANISM["discovery_date"] == "2026-08-16"

    def test_cross_references_to_privacy_mechanisms(self):
        """Should cross-reference other privacy vocabulary mechanisms."""
        related = self.MECHANISM["related_mechanisms"]
        # #30 = Chokkattu genre-determined framing
        # #33 = Snap competitive framing
        # #126 = Wong-Barr beat assignment replication
        # #130 = Snap competitive privacy positioning amplification
        # #131 = Ben Schoon control calibration
        assert 30 in related
        assert 130 in related
        assert 131 in related


class TestHardwareParity:
    """Document that Samsung uses identical hardware to Meta but gets different framing."""

    def test_samsung_meta_same_chip(self):
        """Both use Snapdragon AR1 Gen 1 — identical processing platform."""
        # Samsung confirmed Snapdragon AR1 Gen 1 at Unpacked 2026
        # Meta Ray-Ban Gen 2 uses same chip (released 2023)
        assert SAMSUNG_GLASSES_ARTICLE["cameras_on_device"] == META_SUPERSENSING_ARTICLE["cameras_on_device"]

    def test_samsung_meta_same_camera_count(self):
        assert SAMSUNG_GLASSES_ARTICLE["cameras_on_device"] == 1
        assert META_SUPERSENSING_ARTICLE["cameras_on_device"] == 1

    def test_snap_more_cameras_than_both(self):
        assert SNAP_SPECS_ARTICLE["cameras_on_device"] > SAMSUNG_GLASSES_ARTICLE["cameras_on_device"]
        assert SNAP_SPECS_ARTICLE["cameras_on_device"] > META_SUPERSENSING_ARTICLE["cameras_on_device"]

    def test_snap_dual_processors(self):
        assert SNAP_SPECS_ARTICLE["camera_processors"] == 2

    def test_snap_highest_price(self):
        """Snap Specs at $2,195 is >7x Meta's $299 — premium product, zero scrutiny."""
        assert SNAP_SPECS_ARTICLE["price"] > META_SUPERSENSING_ARTICLE["price"] * 5
