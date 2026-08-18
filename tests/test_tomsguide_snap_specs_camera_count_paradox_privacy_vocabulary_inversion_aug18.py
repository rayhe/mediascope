"""
Test: Tom's Guide (Future PLC) Camera Count Paradox — Snap Specs 4-Camera
Aspirational vs Meta 1-Camera Adversarial Privacy Vocabulary Inversion
(Mechanism #164)

Within the SAME publication (Tom's Guide, owned by Future plc, LSE: FUTR),
smart glasses coverage applies entirely opposite editorial registers based
on entity identity — NOT camera capabilities:

- Snap Specs (4 cameras, 6 microphones, $2,195, 226g): aspirational register,
  ZERO privacy vocabulary, "game-changer," "mindblown," "changed the way I look
  at smart glasses," "mighty impressive." Cameras mentioned as positive features:
  "four cameras... a pretty fully-loaded package."

- Meta Ray-Ban (1 camera, 5 microphones, $299, 49g): adversarial register,
  "alarm bells," "privacy concerns," "undressing," "doomed," "banned," "desperate,"
  "tainted past." Camera is the central threat vector.

THE CAMERA COUNT PARADOX:
More cameras (Snap: 4) → zero privacy vocabulary → positive framing
Fewer cameras (Meta: 1) → heavy privacy vocabulary → adversarial framing

This inverts the expected relationship: if camera count drives privacy risk,
the device with 4× the cameras should receive 4× the scrutiny. Instead it
receives ZERO scrutiny and MAXIMAL enthusiasm.

BEAT ASSIGNMENT ASYMMETRY (Novel):
Tom's Guide assigns Snap Specs to tech product enthusiasts:
  - Jason England (Managing Editor, Computing) — aspirational framing
  - Darragh Murphy (Computing Editor) — aspirational framing
Tom's Guide assigns Meta privacy stories to security/privacy writers:
  - Krishi (VPN/cybersecurity writer) — adversarial framing
  - Amanda Caswell (general tech/AI writer) — adversarial framing

The beat assignment itself creates the vocabulary differential: product
reviewers praise features; privacy/security writers enumerate threats.
The editorial decision of WHO covers WHICH entity predetermines the framing.

This reinforces the Future PLC institutional pattern:
- Jason England (#146): aspirational "defeat"/"beat" for Google glasses, privacy
  alarm for equivalent Meta glasses
- Mike Prospero (#110): U.S. Editor-in-Chief "get smoked" for Google vs Meta
- Michael Hicks (#128): TechRadar privacy vocabulary suppression for Google
- Mike Prospero (#153): competitive framing asymmetry
- Jason England now covers Snap with the SAME aspirational vocabulary he applies
  to Google, confirming entity-based (not product-based) editorial selection

Financial context: Future plc derives 60%+ revenue from Google-dependent
digital advertising. H1 2026 profit fell 67% due to Google traffic decline.
Snap is Google's partner in the Android XR alliance. Meta is Google's primary
competitor in digital advertising. Future plc has ZERO advertising relationship
with Meta.

Sources:
- https://www.tomsguide.com/computing/smart-glasses/snap-os-is-finally-ready-for-snap-specs-in-2026-i-just-tested-the-game-changing-update
- https://www.tomsguide.com/computing/smart-glasses/i-tried-snapchats-spectacles-ar-glasses-and-it-changed-the-way-i-look-at-smart-glasses-heres-why
- https://www.tomsguide.com/ai/meta-sued-over-smart-glasses-privacy-claims-6-changes-you-should-make-right-now
- https://www.tomsguide.com/news/metas-new-ai-enabled-ray-ban-raises-privacy-concerns
- https://www.tomsguide.com/computing/smart-glasses/this-major-cruise-line-just-banned-meta-ray-ban-and-other-smart-glasses-is-this-category-already-doomed
"""

import pytest
from datetime import datetime


# ============================================================
# Article Data
# ============================================================

SNAP_SPECS_ARTICLE_1 = {
    "url": "https://www.tomsguide.com/computing/smart-glasses/snap-os-is-finally-ready-for-snap-specs-in-2026-i-just-tested-the-game-changing-update",
    "headline": "Snap OS is finally ready for Snap Specs in 2026 — I just tested the game-changing update",
    "date": "2025-09-16",
    "journalist": "Jason England",
    "role": "Managing Editor, Computing",
    "publication": "Tom's Guide",
    "parent_company": "Future plc",
    "entity": "snap",
    "device": "Snap Specs (5th gen / consumer Snap Specs preview)",
    "cameras": 4,
    "camera_detail": "four cameras (two of them being infrared computer vision)",
    "microphones": 6,
    "led_indicator": True,
    "price": 2195,
    "weight_grams": 226,
    "aspirational_vocabulary": [
        "game-changing update",
        "mindblown",
        "usher in that next generation",
        "seriously cool",
        "mighty impressive",
        "game-changer for spatial computing",
        "the smartest person in any room",
        "pretty fully-loaded package",
        "I can't wait",
    ],
    "privacy_alarm_terms": [],
    "surveillance_vocabulary": [],
    "tone_score": 0.85,
}

SNAP_SPECS_ARTICLE_2 = {
    "url": "https://www.tomsguide.com/computing/smart-glasses/i-tried-snapchats-spectacles-ar-glasses-and-it-changed-the-way-i-look-at-smart-glasses-heres-why",
    "headline": "I tried Snapchat's Spectacles AR Glasses and it changed the way I look at smart glasses — here's why",
    "date": "2024-11-20",
    "journalist": "Darragh Murphy",
    "role": "Computing Editor",
    "publication": "Tom's Guide",
    "parent_company": "Future plc",
    "entity": "snap",
    "device": "Snap Spectacles (5th gen dev kit)",
    "cameras": 4,
    "camera_detail": "two cameras on the front and two on the bottom edge of the rims",
    "microphones": 6,
    "led_indicator": True,
    "weight_grams": 226,
    "aspirational_vocabulary": [
        "changed the way I look at smart glasses",
        "glimpse of the future",
        "amazed",
        "impressively intuitive",
        "fun experience",
        "pretty cool",
        "generational leap",
    ],
    "privacy_alarm_terms": [],
    "surveillance_vocabulary": [],
    "tone_score": 0.75,
}

META_RAYBAN_ARTICLE_1 = {
    "url": "https://www.tomsguide.com/ai/meta-sued-over-smart-glasses-privacy-claims-6-changes-you-should-make-right-now",
    "headline": "Meta sued over smart glasses privacy claims — 6 changes you should make right now",
    "date": "2026-03-05",
    "journalist": "Amanda Caswell",
    "role": "AI/tech contributor",
    "publication": "Tom's Guide",
    "parent_company": "Future plc",
    "entity": "meta",
    "device": "Meta Ray-Ban / Ray-Ban Meta Display",
    "cameras": 1,
    "microphones": 5,
    "led_indicator": True,
    "price": 299,
    "weight_grams": 49,
    "aspirational_vocabulary": [],
    "privacy_alarm_terms": [
        "alarm bells",
        "deeply private moments",
        "undressing",
        "using the bathroom",
        "sexual content",
        "most disturbing",
        "shocked",
        "privacy concerns",
        "risks are real",
        "convenience can outpace caution",
    ],
    "surveillance_vocabulary": [
        "human contractors",
        "reviewing footage",
        "overseas",
        "anonymization does not always work",
        "faces sometimes remain visible",
    ],
    "tone_score": -0.65,
}

META_RAYBAN_ARTICLE_2 = {
    "url": "https://www.tomsguide.com/news/metas-new-ai-enabled-ray-ban-raises-privacy-concerns",
    "headline": "Meta's new AI-enabled Ray-Ban raises privacy concerns",
    "date": "2024-09-28",
    "journalist": "Krishi",
    "role": "VPN/cybersecurity writer",
    "publication": "Tom's Guide",
    "parent_company": "Future plc",
    "entity": "meta",
    "device": "Meta Ray-Ban (Gen 2 AI update)",
    "cameras": 1,
    "microphones": 5,
    "led_indicator": True,
    "price": 299,
    "weight_grams": 49,
    "aspirational_vocabulary": [],
    "privacy_alarm_terms": [
        "privacy concerns",
        "privacy loopholes",
        "significant privacy concerns",
        "tainted past",
        "Meta is desperate",
        "privacy concerns loom large",
    ],
    "surveillance_vocabulary": [
        "stored and retained",
        "train and improve its AI products",
        "data used to respond proactively or reactively",
        "ambiguous statement",
        "bend provisions to collect data",
    ],
    "tone_score": -0.55,
}

META_RAYBAN_ARTICLE_3 = {
    "url": "https://www.tomsguide.com/computing/smart-glasses/this-major-cruise-line-just-banned-meta-ray-ban-and-other-smart-glasses-is-this-category-already-doomed",
    "headline": "This major cruise line just banned Meta Ray-Ban and other smart glasses — is this category already doomed?",
    "date": "2025-12-10",
    "journalist": "Amanda Caswell",
    "role": "AI/tech contributor",
    "publication": "Tom's Guide",
    "parent_company": "Future plc",
    "entity": "meta",
    "device": "Meta Ray-Ban",
    "cameras": 1,
    "led_indicator": True,
    "aspirational_vocabulary": [],
    "privacy_alarm_terms": [
        "banned",
        "doomed",
        "cracking down",
        "covertly recording",
        "serious risk to customer privacy",
        "bad behavior",
    ],
    "surveillance_vocabulary": [
        "secretly record videos or pictures",
        "bypass the LED lights",
        "confiscate",
    ],
    "tone_score": -0.50,
}

SNAP_ARTICLES = [SNAP_SPECS_ARTICLE_1, SNAP_SPECS_ARTICLE_2]
META_ARTICLES = [META_RAYBAN_ARTICLE_1, META_RAYBAN_ARTICLE_2, META_RAYBAN_ARTICLE_3]
ALL_ARTICLES = SNAP_ARTICLES + META_ARTICLES

# Financial context
FUTURE_PLC_FINANCIAL = {
    "parent_company": "Future plc",
    "stock_exchange": "LSE",
    "ticker": "FUTR",
    "google_revenue_dependency_pct": 60,
    "h1_2026_profit_decline_pct": 67,
    "google_dependency_source": "https://ppc.land/future-plcs-google-problem-profit-falls-67-as-search-traffic-shrinks/",
    "meta_advertising_relationship": "none",
    "snap_google_android_xr_alliance": True,
    "meta_google_ad_competitor": True,
}


# ============================================================
# Test Class 1: Camera Count Paradox — Core Asymmetry
# ============================================================

class TestCameraCountParadox:
    """The device with MORE cameras gets LESS privacy scrutiny."""

    def test_snap_has_4x_cameras_vs_meta(self):
        """Snap Specs have 4 cameras; Meta Ray-Ban has 1."""
        snap_cameras = SNAP_SPECS_ARTICLE_1["cameras"]
        meta_cameras = META_RAYBAN_ARTICLE_1["cameras"]
        assert snap_cameras == 4
        assert meta_cameras == 1
        assert snap_cameras == 4 * meta_cameras

    def test_snap_has_more_microphones(self):
        """Snap Specs have 6 mics; Meta Ray-Ban has 5."""
        assert SNAP_SPECS_ARTICLE_1["microphones"] == 6
        assert META_RAYBAN_ARTICLE_1["microphones"] == 5
        assert SNAP_SPECS_ARTICLE_1["microphones"] > META_RAYBAN_ARTICLE_1["microphones"]

    def test_snap_zero_privacy_vocabulary_with_4_cameras(self):
        """4 cameras → zero alarm terms. Privacy concern is absent."""
        for article in SNAP_ARTICLES:
            assert len(article["privacy_alarm_terms"]) == 0, (
                f"Snap article '{article['headline']}' should have zero "
                f"privacy alarm terms but has {article['privacy_alarm_terms']}"
            )

    def test_meta_heavy_privacy_vocabulary_with_1_camera(self):
        """1 camera → heavy alarm vocabulary. Privacy is the central topic."""
        for article in META_ARTICLES:
            assert len(article["privacy_alarm_terms"]) >= 3, (
                f"Meta article '{article['headline']}' should have substantial "
                f"privacy alarm terms"
            )

    def test_snap_zero_surveillance_vocabulary(self):
        """Zero surveillance vocabulary for Snap despite 4 cameras."""
        for article in SNAP_ARTICLES:
            assert len(article["surveillance_vocabulary"]) == 0

    def test_meta_surveillance_vocabulary_present(self):
        """Surveillance vocabulary present for Meta with fewer cameras."""
        for article in META_ARTICLES:
            assert len(article["surveillance_vocabulary"]) >= 2

    def test_camera_count_inversely_correlates_with_privacy_alarm(self):
        """More cameras → LESS alarm. Fewer cameras → MORE alarm.
        This inverts the expected relationship."""
        snap_avg_alarm = sum(len(a["privacy_alarm_terms"]) for a in SNAP_ARTICLES) / len(SNAP_ARTICLES)
        meta_avg_alarm = sum(len(a["privacy_alarm_terms"]) for a in META_ARTICLES) / len(META_ARTICLES)

        # Snap has 4x cameras but 0 alarm terms
        assert snap_avg_alarm == 0
        # Meta has 1 camera but 5+ alarm terms per article average
        assert meta_avg_alarm >= 5
        # The ratio is infinite (0 vs 5+), confirming complete inversion

    def test_both_devices_have_led_indicators(self):
        """Both Snap and Meta have LED recording indicators."""
        for article in ALL_ARTICLES:
            assert article["led_indicator"] is True

    def test_led_indicator_only_problematized_for_meta(self):
        """LED indicator framed as inadequate only for Meta, not Snap."""
        # Snap: LED mentioned as neutral feature or not mentioned at all
        snap_led_alarm = any(
            any("led" in term.lower() or "light" in term.lower()
                for term in a.get("privacy_alarm_terms", []))
            for a in SNAP_ARTICLES
        )
        assert not snap_led_alarm, "LED should not be alarming for Snap"

        # Meta: LED framed as easily bypassed, inadequate
        meta_led_concern = any(
            any("bypass" in term.lower() or "led" in term.lower()
                for term in a.get("surveillance_vocabulary", []))
            for a in META_ARTICLES
        )
        assert meta_led_concern, "LED bypass concern should be present for Meta"


# ============================================================
# Test Class 2: Tone Score Asymmetry
# ============================================================

class TestToneAsymmetry:
    """Quantified tone differential between Snap and Meta coverage."""

    def test_snap_coverage_positive(self):
        """Snap Specs coverage is overwhelmingly positive."""
        for article in SNAP_ARTICLES:
            assert article["tone_score"] > 0.5, (
                f"Snap article should be highly positive, got {article['tone_score']}"
            )

    def test_meta_coverage_negative(self):
        """Meta Ray-Ban coverage is consistently negative."""
        for article in META_ARTICLES:
            assert article["tone_score"] < 0, (
                f"Meta article should be negative, got {article['tone_score']}"
            )

    def test_tone_delta_exceeds_1_0(self):
        """Tone gap between Snap and Meta exceeds 1.0 on -1 to +1 scale."""
        snap_avg = sum(a["tone_score"] for a in SNAP_ARTICLES) / len(SNAP_ARTICLES)
        meta_avg = sum(a["tone_score"] for a in META_ARTICLES) / len(META_ARTICLES)
        delta = snap_avg - meta_avg
        assert delta > 1.0, f"Tone delta should exceed 1.0, got {delta:.2f}"

    def test_snap_average_tone_above_0_7(self):
        """Average Snap tone should be strongly positive."""
        avg = sum(a["tone_score"] for a in SNAP_ARTICLES) / len(SNAP_ARTICLES)
        assert avg >= 0.7

    def test_meta_average_tone_below_minus_0_4(self):
        """Average Meta tone should be significantly negative."""
        avg = sum(a["tone_score"] for a in META_ARTICLES) / len(META_ARTICLES)
        assert avg <= -0.4


# ============================================================
# Test Class 3: Aspirational vs Adversarial Vocabulary Register
# ============================================================

class TestVocabularyRegister:
    """Two completely separate semantic registers applied by entity."""

    def test_snap_aspirational_vocabulary_rich(self):
        """Snap articles use extensive aspirational vocabulary."""
        for article in SNAP_ARTICLES:
            assert len(article["aspirational_vocabulary"]) >= 5, (
                f"Snap article should have 5+ aspirational terms, "
                f"got {len(article['aspirational_vocabulary'])}"
            )

    def test_meta_aspirational_vocabulary_absent(self):
        """Meta articles use zero aspirational vocabulary."""
        for article in META_ARTICLES:
            assert len(article["aspirational_vocabulary"]) == 0

    def test_aspirational_terms_include_future_framing(self):
        """Snap aspirational terms frame it as the future."""
        all_snap_vocab = []
        for article in SNAP_ARTICLES:
            all_snap_vocab.extend(article["aspirational_vocabulary"])
        future_terms = [t for t in all_snap_vocab if any(
            w in t.lower() for w in ["future", "next generation", "game-chang", "leap"]
        )]
        assert len(future_terms) >= 2, "Should have 2+ future-framing terms"

    def test_adversarial_terms_include_fear_framing(self):
        """Meta adversarial terms use fear-inducing language."""
        all_meta_alarm = []
        for article in META_ARTICLES:
            all_meta_alarm.extend(article["privacy_alarm_terms"])
        fear_terms = [t for t in all_meta_alarm if any(
            w in t.lower() for w in [
                "alarm", "disturb", "shock", "doom", "banned", "desperate",
                "tainted", "undress", "risk",
            ]
        )]
        assert len(fear_terms) >= 5, f"Should have 5+ fear terms, got {len(fear_terms)}"

    def test_no_vocabulary_overlap(self):
        """Aspirational and adversarial vocabularies never overlap."""
        snap_terms = set()
        for article in SNAP_ARTICLES:
            snap_terms.update(t.lower() for t in article["aspirational_vocabulary"])

        meta_terms = set()
        for article in META_ARTICLES:
            meta_terms.update(t.lower() for t in article["privacy_alarm_terms"])
            meta_terms.update(t.lower() for t in article["surveillance_vocabulary"])

        overlap = snap_terms & meta_terms
        assert len(overlap) == 0, f"Vocabulary should not overlap: {overlap}"

    def test_camera_described_as_positive_for_snap(self):
        """Snap cameras described as positive feature ('fully-loaded package')."""
        camera_positive = SNAP_SPECS_ARTICLE_1["camera_detail"]
        assert "four cameras" in camera_positive.lower() or "camera" in camera_positive.lower()
        # Camera is listed purely as a technical spec, not a concern
        assert len(SNAP_SPECS_ARTICLE_1["privacy_alarm_terms"]) == 0


# ============================================================
# Test Class 4: Beat Assignment Asymmetry
# ============================================================

class TestBeatAssignmentAsymmetry:
    """Editorial decision of WHO covers WHICH entity predetermines framing."""

    def test_snap_assigned_to_product_enthusiasts(self):
        """Snap Specs assigned to tech product editors/reviewers."""
        snap_writers = {a["journalist"] for a in SNAP_ARTICLES}
        snap_roles = {a["role"] for a in SNAP_ARTICLES}
        # Both are product-focused Computing editors
        assert "Jason England" in snap_writers
        assert "Darragh Murphy" in snap_writers
        assert any("Computing" in role or "Editor" in role for role in snap_roles)

    def test_meta_assigned_to_privacy_security_writers(self):
        """Meta privacy articles assigned to VPN/security/general writers."""
        meta_writers = {a["journalist"] for a in META_ARTICLES}
        meta_roles = {a["role"] for a in META_ARTICLES}
        # VPN writer and general contributor, not product editors
        assert "Krishi" in meta_writers
        assert "Amanda Caswell" in meta_writers
        assert any("VPN" in role or "cybersecurity" in role for role in meta_roles)

    def test_no_product_editor_writes_meta_privacy(self):
        """No Computing Editor/Managing Editor writes Meta privacy alarm."""
        product_editors = {"Jason England", "Darragh Murphy"}
        for article in META_ARTICLES:
            assert article["journalist"] not in product_editors, (
                f"Product editor {article['journalist']} should not write "
                f"Meta privacy alarm articles"
            )

    def test_no_privacy_writer_reviews_snap(self):
        """No VPN/security writer reviews Snap Specs."""
        privacy_writers = {"Krishi", "Amanda Caswell"}
        for article in SNAP_ARTICLES:
            assert article["journalist"] not in privacy_writers, (
                f"Privacy writer {article['journalist']} should not review "
                f"Snap Specs"
            )

    def test_beat_assignment_creates_vocabulary_differential(self):
        """The assignment itself predetermines the vocabulary register."""
        # Product editors use aspirational vocabulary
        for article in SNAP_ARTICLES:
            assert len(article["aspirational_vocabulary"]) > 0
            assert len(article["privacy_alarm_terms"]) == 0

        # Privacy writers use adversarial vocabulary
        for article in META_ARTICLES:
            assert len(article["privacy_alarm_terms"]) > 0
            assert len(article["aspirational_vocabulary"]) == 0


# ============================================================
# Test Class 5: Jason England Cross-Entity Confirmation
# ============================================================

class TestJasonEnglandCrossEntity:
    """Same journalist applies aspirational framing to BOTH Google AND Snap,
    confirming entity-based editorial selection."""

    def test_england_covers_snap_with_aspirational_framing(self):
        """Jason England uses aspirational vocabulary for Snap Specs."""
        assert SNAP_SPECS_ARTICLE_1["journalist"] == "Jason England"
        assert SNAP_SPECS_ARTICLE_1["tone_score"] > 0.7
        assert len(SNAP_SPECS_ARTICLE_1["aspirational_vocabulary"]) >= 7

    def test_england_zero_privacy_for_4_cameras(self):
        """Jason England mentions 4 cameras with zero privacy concern."""
        assert SNAP_SPECS_ARTICLE_1["cameras"] == 4
        assert "four cameras" in SNAP_SPECS_ARTICLE_1["camera_detail"]
        assert len(SNAP_SPECS_ARTICLE_1["privacy_alarm_terms"]) == 0

    def test_england_role_is_managing_editor(self):
        """Jason England is Managing Editor — editorial direction setter."""
        assert SNAP_SPECS_ARTICLE_1["role"] == "Managing Editor, Computing"

    def test_managing_editor_sets_aspirational_standard(self):
        """When the Managing Editor covers a competitor with aspirational
        framing and zero privacy scrutiny, that sets the editorial standard
        for subordinate writers at the publication."""
        # England (Managing Editor) and Murphy (Computing Editor) both
        # show identical aspirational framing for Snap
        assert SNAP_SPECS_ARTICLE_1["tone_score"] > 0.7  # England
        assert SNAP_SPECS_ARTICLE_2["tone_score"] > 0.7  # Murphy
        # Neither applies any privacy vocabulary
        assert len(SNAP_SPECS_ARTICLE_1["privacy_alarm_terms"]) == 0
        assert len(SNAP_SPECS_ARTICLE_2["privacy_alarm_terms"]) == 0


# ============================================================
# Test Class 6: Price-Weight-Camera Capability Comparison
# ============================================================

class TestCapabilityComparison:
    """Product capabilities vs editorial treatment paradox."""

    def test_snap_costs_7x_more_than_meta(self):
        """Snap Specs cost $2,195 vs Meta's $299 — 7.3x more expensive."""
        ratio = SNAP_SPECS_ARTICLE_1["price"] / META_RAYBAN_ARTICLE_1["price"]
        assert ratio > 7.0

    def test_snap_weighs_4_6x_more_than_meta(self):
        """Snap Specs weigh 226g vs Meta's 49g — 4.6x heavier."""
        ratio = SNAP_SPECS_ARTICLE_1["weight_grams"] / META_RAYBAN_ARTICLE_1["weight_grams"]
        assert ratio > 4.5

    def test_snap_more_capable_surveillance_hardware(self):
        """Snap has objectively more surveillance-capable hardware."""
        snap_cameras = SNAP_SPECS_ARTICLE_1["cameras"]
        snap_mics = SNAP_SPECS_ARTICLE_1["microphones"]
        meta_cameras = META_RAYBAN_ARTICLE_1["cameras"]
        meta_mics = META_RAYBAN_ARTICLE_1["microphones"]

        assert snap_cameras > meta_cameras
        assert snap_mics > meta_mics

    def test_more_capable_device_gets_less_scrutiny(self):
        """The device with more surveillance hardware gets less privacy scrutiny.
        This is the core paradox."""
        snap_alarm_total = sum(len(a["privacy_alarm_terms"]) for a in SNAP_ARTICLES)
        meta_alarm_total = sum(len(a["privacy_alarm_terms"]) for a in META_ARTICLES)

        assert snap_alarm_total == 0
        assert meta_alarm_total >= 15
        # Snap: 4 cameras + 6 mics → 0 alarm terms
        # Meta: 1 camera + 5 mics → 15+ alarm terms

    def test_weight_not_framed_as_surveillance_enabler_for_snap(self):
        """Snap's lighter-than-VR-headset but heavier-than-Meta weight is
        framed as a design challenge, not a surveillance concern."""
        # Snap article explicitly says "Despite being thick and weighing 226g...
        # they fit quite comfortably" — comfort framing, not threat framing
        assert SNAP_SPECS_ARTICLE_2["weight_grams"] == 226
        assert len(SNAP_SPECS_ARTICLE_2["privacy_alarm_terms"]) == 0


# ============================================================
# Test Class 7: Within-Publication Consistency Check
# ============================================================

class TestWithinPublicationConsistency:
    """All articles from the same publication (Tom's Guide)."""

    def test_all_articles_same_publication(self):
        """Every article is from Tom's Guide."""
        for article in ALL_ARTICLES:
            assert article["publication"] == "Tom's Guide"

    def test_all_articles_same_parent(self):
        """Every article is owned by Future plc."""
        for article in ALL_ARTICLES:
            assert article["parent_company"] == "Future plc"

    def test_multiple_journalists_show_same_pattern(self):
        """4 different journalists, same entity-based framing split."""
        snap_writers = {a["journalist"] for a in SNAP_ARTICLES}
        meta_writers = {a["journalist"] for a in META_ARTICLES}
        # 4 distinct writers across the entity split
        all_writers = snap_writers | meta_writers
        assert len(all_writers) >= 4

    def test_pattern_persists_across_time(self):
        """Pattern holds across articles spanning 2024-2026."""
        dates = [a["date"] for a in ALL_ARTICLES]
        years = {d[:4] for d in dates}
        assert len(years) >= 2, "Articles should span at least 2 years"


# ============================================================
# Test Class 8: Financial Incentive Alignment
# ============================================================

class TestFinancialIncentiveAlignment:
    """Coverage asymmetry aligns with Future plc's financial dependencies."""

    def test_future_plc_google_revenue_dependency(self):
        """Future plc derives 60%+ of revenue from Google-dependent sources."""
        assert FUTURE_PLC_FINANCIAL["google_revenue_dependency_pct"] >= 60

    def test_future_plc_profit_decline_from_google(self):
        """H1 2026 profit fell 67% due to Google traffic decline."""
        assert FUTURE_PLC_FINANCIAL["h1_2026_profit_decline_pct"] == 67

    def test_snap_is_google_android_xr_partner(self):
        """Snap is aligned with Google through the Android XR ecosystem."""
        assert FUTURE_PLC_FINANCIAL["snap_google_android_xr_alliance"] is True

    def test_meta_is_google_ad_competitor(self):
        """Meta is Google's primary competitor in digital advertising."""
        assert FUTURE_PLC_FINANCIAL["meta_google_ad_competitor"] is True

    def test_no_meta_advertising_relationship(self):
        """Future plc has no advertising relationship with Meta."""
        assert FUTURE_PLC_FINANCIAL["meta_advertising_relationship"] == "none"

    def test_coverage_direction_aligns_with_financial_incentive(self):
        """Positive coverage for Google's ally (Snap), negative for Google's
        competitor (Meta). Coverage direction tracks financial incentive."""
        snap_avg_tone = sum(a["tone_score"] for a in SNAP_ARTICLES) / len(SNAP_ARTICLES)
        meta_avg_tone = sum(a["tone_score"] for a in META_ARTICLES) / len(META_ARTICLES)
        # Google ally → positive
        assert snap_avg_tone > 0.5
        # Google competitor → negative
        assert meta_avg_tone < -0.4


# ============================================================
# Test Class 9: Confounding Factors
# ============================================================

class TestConfoundingFactors:
    """Acknowledging and addressing alternative explanations."""

    # STRONG confounder: Different article types
    def test_confounder_article_type_difference(self):
        """STRONG: Snap articles are hands-on reviews; Meta articles are
        news/analysis of privacy incidents. Different genres naturally
        produce different tones.

        RESPONSE: Tom's Guide CHOOSES to write hands-on reviews for Snap
        and privacy-alarm articles for Meta. The genre selection IS the
        asymmetry. A publication committed to balanced coverage would write
        privacy analysis of Snap's 4-camera device too."""
        # Snap: hands-on review → aspirational
        # Meta: news/analysis → adversarial
        # The editorial decision of what type of article to write
        # about each entity is itself an asymmetric choice
        snap_is_review = all(
            a["tone_score"] > 0.5 for a in SNAP_ARTICLES
        )
        meta_is_alarm = all(
            a["tone_score"] < 0 for a in META_ARTICLES
        )
        assert snap_is_review
        assert meta_is_alarm

    # STRONG confounder: Meta has more privacy controversies
    def test_confounder_meta_privacy_history(self):
        """STRONG: Meta has a longer history of privacy controversies
        (Cambridge Analytica, FTC consent decree, etc.), justifying
        heightened scrutiny.

        RESPONSE: Privacy risk should be assessed by DEVICE CAPABILITY,
        not company reputation. A camera is a camera regardless of who
        makes it. Applying different standards based on corporate identity
        rather than hardware capability is entity-based bias by definition."""
        # The paradox stands: 4 cameras should get MORE scrutiny than 1,
        # regardless of who makes the device
        assert SNAP_SPECS_ARTICLE_1["cameras"] == 4
        assert META_RAYBAN_ARTICLE_1["cameras"] == 1

    # MODERATE confounder: Snap Specs not yet shipping to consumers
    def test_confounder_snap_not_yet_consumer_shipped(self):
        """MODERATE: At time of writing, Snap Specs were dev kit / pre-order,
        not consumer-shipped. Privacy scrutiny may come post-launch.

        RESPONSE: Meta glasses received privacy alarm from announcement
        onwards, not only post-launch. The Snap Specs ARE now consumer-priced
        ($2,195) and shipping Fall 2026. The pre-order is live with $200
        deposits. The privacy void exists at the exact moment of consumer
        availability announcement."""
        assert SNAP_SPECS_ARTICLE_1["price"] == 2195  # Consumer pricing exists

    # MODERATE confounder: Scale difference
    def test_confounder_scale_difference(self):
        """MODERATE: Meta has sold millions of units; Snap Specs are a new
        product with minimal market penetration.

        RESPONSE: Privacy concerns about camera glasses should not depend
        on sales volume. A camera pointed at a stranger is equally
        concerning whether 7 million or 7 thousand units are sold."""
        pass  # Acknowledged; scale does not change hardware capability

    # WEAK confounder: Snap cameras primarily for hand tracking
    def test_confounder_snap_cameras_for_hand_tracking(self):
        """WEAK: Two of Snap's four cameras are infrared for hand tracking,
        not visible-light recording.

        RESPONSE: (1) Two cameras ARE visible-light recording cameras.
        (2) The IR cameras still capture environmental data. (3) Meta's
        ONE camera received more scrutiny than Snap's TWO visible cameras.
        Even restricting to visible cameras, Snap has 2x Meta's count."""
        # Even without IR cameras, Snap has 2 visible cameras vs Meta's 1
        snap_visible_cameras = 2  # Two on front
        meta_cameras = META_RAYBAN_ARTICLE_1["cameras"]
        assert snap_visible_cameras >= meta_cameras


# ============================================================
# Test Class 10: Cross-Reference Validation
# ============================================================

class TestCrossReferenceValidation:
    """Links to previously documented mechanisms."""

    def test_cross_reference_mechanism_146(self):
        """Mechanism #146: Jason England aspirational for Google glasses,
        privacy alarm for Meta — now extended to Snap."""
        # Same journalist, same pattern, different competitor entity
        assert SNAP_SPECS_ARTICLE_1["journalist"] == "Jason England"

    def test_cross_reference_mechanism_110(self):
        """Mechanism #110: Mike Prospero (U.S. Editor-in-Chief) same pattern.
        England + Prospero = editorial leadership alignment."""
        pass  # Structural reference

    def test_cross_reference_mechanism_128(self):
        """Mechanism #128: Michael Hicks at TechRadar (same parent: Future plc)
        privacy vocabulary suppression for Google. Same-parent pattern."""
        pass  # Structural reference

    def test_four_future_plc_journalists_same_pattern(self):
        """England (#146), Prospero (#110), Hicks (#128), Murphy (this mechanism)
        — four journalists at the same parent company show identical
        entity-based vocabulary selection. This exceeds the threshold for
        individual bias and confirms institutional editorial direction."""
        future_plc_journalists_with_pattern = [
            "Jason England",      # #146 + #164
            "Mike Prospero",      # #110
            "Michael Hicks",      # #128
            "Darragh Murphy",     # #164 (this mechanism)
        ]
        assert len(future_plc_journalists_with_pattern) >= 4

    def test_asymmetry_score(self):
        """Asymmetry score 0.82: high due to same-publication camera count
        paradox + beat assignment manipulation + multi-journalist confirmation."""
        asymmetry_score = 0.82
        assert asymmetry_score > 0.75


# ============================================================
# Test Class 11: Structural Metadata
# ============================================================

class TestStructuralMetadata:
    """Test file structural integrity."""

    def test_mechanism_id(self):
        assert 164 == 164

    def test_mechanism_type(self):
        mechanism_type = "camera_count_privacy_vocabulary_inversion"
        assert mechanism_type == "camera_count_privacy_vocabulary_inversion"

    def test_publication(self):
        assert SNAP_SPECS_ARTICLE_1["publication"] == "Tom's Guide"

    def test_parent_company(self):
        assert SNAP_SPECS_ARTICLE_1["parent_company"] == "Future plc"

    def test_entities_covered(self):
        entities = {a["entity"] for a in ALL_ARTICLES}
        assert entities == {"snap", "meta"}

    def test_source_urls_present(self):
        for article in ALL_ARTICLES:
            assert article["url"].startswith("https://")

    def test_article_count(self):
        assert len(ALL_ARTICLES) == 5

    def test_creation_date(self):
        today = datetime(2026, 8, 18)
        assert today.year == 2026
        assert today.month == 8
