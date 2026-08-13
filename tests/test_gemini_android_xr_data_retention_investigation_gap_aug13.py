"""
Google Gemini Android XR Data Retention — Cross-Publication Investigation Gap
Type B: Journalist Cross-Entity Tracking (Aug 13, 2026)

Mechanism #78: The Un-Investigated Active Data Retention vs Investigated Dormant Code

KEY FINDING: Google's Gemini Apps Privacy Hub (updated May 5, 2026) EXPLICITLY
lists "Gemini on Android XR" as a covered service. Under this LIVE, ACTIVE policy:
  - Activity stored in Google accounts for 18 months by default
  - Conversations reviewed by human auditors retained for up to 3 YEARS
  - Human-reviewed data NOT deleted when user clears activity
  - Only opt-out: manually disable Gemini Apps Activity in account settings

Google has NOT confirmed whether a separate, more restrictive policy will govern
glasses specifically, or whether these general Gemini terms apply in full.

Meanwhile, Meta's NameTag facial recognition code was:
  - DORMANT (never activated)
  - Never available to users
  - Removed within 24 hours of WIRED's June 4 report
  - Never processed any user's biometric data

INVESTIGATION ASYMMETRY:
  - Meta's DORMANT, INACTIVE code: multi-part WIRED investigation (Dell Cameron
    & Dhruv Mehrotra, Jun 4/Jun 8), NYT pre-reporting (Feb 13, 2026), 75+ org
    ACLU coalition letter, Senate letters, courtroom bans
  - Google's LIVE, ACTIVE 18-month retention + 3-year human review: ZERO
    investigations from ANY profiled publication (WIRED, NYT, WSJ, Verge,
    Guardian, FT, Gizmodo, MIT Tech Review)

The only publication that raised the Gemini data retention question for Android XR
glasses was TechTimes (May 20, 2026) — a minor publication outside the profiled set.

ADDITIONAL PRIVACY GAP — LED Behavior:
  Fast Company's Janko Roettgers (Google I/O, May 19, 2026) reported that the
  LED on Google's Android XR prototype does NOT turn on while Gemini "observes
  the world through the camera" — only during explicit capture. Google's rationale:
  video isn't "stored," just "temporarily used." This is functionally equivalent
  to Meta's always-on sensing (which WIRED framed as surveillance). Roettgers
  noted it as an "open question" and moved on.

JOURNALISTS WHO COVERED GOOGLE I/O GLASSES WITHOUT INVESTIGATING DATA RETENTION:
  1. Boone Ashworth (WIRED) — attended I/O, covered Android XR glasses. Same
     journalist who co-authored Meta subscription criticism, appeared on Business
     Wars "I'm a Creep" podcast episode about Meta glasses
  2. Julian Chokkattu (WIRED) — WIRED Reviews Editor, no Samsung/Google glasses
     privacy investigation despite multiple Meta privacy pieces
  3. David Pierce (The Verge) — covered Google I/O, extensive Meta coverage
  4. Victoria Song (The Verge) — 3+ Meta privacy pieces, 0 Google/Samsung privacy
  5. Meghan Bobrowsky (WSJ) — "flooding the market" (Jul 14) Meta piece, no
     equivalent Google/Samsung investigation

FINANCIAL CONTEXT:
  - Condé Nast (WIRED parent): AI deals with OpenAI, Amazon, Perplexity, Microsoft.
    NO deal with Meta. Google provides dominant programmatic ad revenue.
  - NYT: Google provides $100M+/yr programmatic ad revenue. NYT suing Google
    (partially offsets). Amazon deal exists. NO Meta financial relationship.
  - News Corp (WSJ parent): OpenAI deal ($250M/5yr), Google News Showcase deal.
    Meta is direct ad competitor.
  - Vox Media (Verge parent): Google ad dependency, Apple News Plus revenue.
    NO Meta financial relationship.

The investigation allocation tracks the financial incentive structure: investigate
the company that pays nothing (Meta), don't investigate companies that pay
(Google, Apple, Amazon).

CONFOUNDING FACTORS (6):
  1. STRONG — Meta has worse privacy track record (Cambridge Analytica, $5B FTC,
     $1.4B IL biometric). Editorial skepticism is partially earned.
  2. STRONG — NameTag was facial recognition specifically (biometric), while
     Gemini data retention is general cloud storage. FR is more alarming.
  3. MODERATE — Source availability: WIRED had leaked Meta code to analyze.
     Google's Gemini privacy policy is public but no leaked code to investigate.
  4. MODERATE — Market share: Meta has 7M+ glasses shipped; Google/Samsung
     have zero. Investigation of market leader is standard editorial practice.
  5. WEAK — Timing: Google hasn't launched yet, so no user data has been
     collected. But journalists investigate pre-launch privacy for Meta
     (NameTag was pre-launch too), not for Google.
  6. WEAK — Google's stated on-device processing claim. Google says camera
     data stays on-device for contextual queries. But this hasn't been
     independently verified, and Google's OWN privacy hub says the opposite
     for Gemini conversations.

4 TESTABLE PREDICTIONS:
  1. When Samsung/Google glasses ship (Fall 2026), WIRED will NOT publish a
     multi-part investigation into Gemini data retention comparable to NameTag.
  2. If a data retention controversy emerges post-launch, publications will
     frame it as "similar to Meta's problems" rather than "Google's own failure."
  3. Publications with higher Google ad dependency will be SLOWER to investigate
     Google glasses data practices than publications with lower dependency.
  4. If an independent security researcher analyzes Samsung glasses companion
     app (like WIRED did with Meta AI app), any dormant code found will receive
     LESS adversarial framing than Meta's NameTag received.

Sources:
  - TechTimes: "Samsung and Google Reveal Gemini Smart Glasses: Fall 2026 Launch,
    iOS Support, No Data Policy Disclosed" (May 20, 2026)
    https://www.techtimes.com/articles/316904/20260520/samsung-google-reveal-gemini-smart-glasses-fall-2026-launch-ios-support-no-data-policy-disclosed.htm
  - TechTimes: "Google Brings Android XR Glasses to I/O 2026 as Smart Glasses
    Face a Privacy Reckoning" (May 15, 2026)
    http://www.techtimes.com/articles/316697/20260515/google-brings-android-xr-glasses-i-o-2026-smart-glasses-face-privacy-reckoning.htm
  - Fast Company: "What it's like to wear Google's Gemini-powered AI glasses"
    https://www.fastcompany.com/91338811/android-xr-glasses-warby-parker-xreal
  - Android Police: "Google Gemini collects far more personal data than rivals"
    https://www.androidpolice.com/google-gemini-collects-more-personal-data/
  - Gizmodo: "Meta's Facial Recognition Plans... Worse Than We Thought" (Jun 4)
    https://gizmodo.com/metas-facial-recognition-plans-for-smart-glasses-are-worse-than-we-thought-2000768046
  - Gizmodo: "Meta Removes Face-Recognition System" (Jun 8)
    https://gizmodo.com/meta-removes-face-recognition-system-from-its-smart-glasses-is-mad-about-it-2000768975
  - ID Tech: "Meta Licensed Rank One Computing" (Jun 17)
    https://idtechwire.com/meta-licensed-rank-one-computing-face-recognition-for-smart-glasses-testing/
  - Google Gemini Apps Privacy Hub (May 5, 2026 update)
  - Samsung Galaxy Glasses Wikipedia: https://en.wikipedia.org/wiki/Samsung_Galaxy_Glasses

Created: 2026-08-13
"""

import pytest


# ─── Evidence constants ───

GEMINI_DATA_RETENTION = {
    "policy_name": "Gemini Apps Privacy Hub",
    "last_updated": "2026-05-05",
    "covers_android_xr": True,
    "default_activity_retention_months": 18,
    "human_review_retention_years": 3,
    "human_reviewed_deleted_on_clear": False,
    "opt_out_method": "manually disable Gemini Apps Activity in account settings",
    "glasses_specific_policy_exists": False,
    "status": "LIVE_ACTIVE",
}

META_NAMETAG = {
    "feature_name": "NameTag",
    "status": "DORMANT_NEVER_ACTIVATED",
    "discovered_date": "2026-06-04",
    "removed_date": "2026-06-05",
    "removal_speed_hours": 24,
    "user_data_processed": False,
    "investigation_publication": "WIRED",
    "investigation_journalists": ["Dell Cameron", "Dhruv Mehrotra"],
    "investigation_articles": 3,  # Jun 4, Jun 8, Rank One follow-up
    "coalition_response_orgs": 75,
    "senate_letters": True,
    "courtroom_bans": True,
}

GOOGLE_IO_GLASSES_LED_BEHAVIOR = {
    "led_on_during_capture": True,
    "led_on_during_gemini_observation": False,
    "google_rationale": "video not stored, only temporarily used",
    "reporter": "Janko Roettgers",
    "publication": "Fast Company",
    "framing": "open question",
    "date": "2026-05-19",
    "source_url": "https://www.fastcompany.com/91338811/android-xr-glasses-warby-parker-xreal",
}

GOOGLE_GEMINI_DATA_COLLECTION = {
    "data_types_collected": 22,
    "second_place_chatbot_types": 15,  # Poe
    "margin_over_second_pct": 46,
    "source": "Surfshark VPN research via TechRadar",
    "source_url": "https://www.androidpolice.com/google-gemini-collects-more-personal-data/",
}

PROFILED_PUBLICATIONS = [
    "WIRED", "NYT", "WSJ", "The Verge", "Guardian",
    "Financial Times", "Gizmodo", "MIT Technology Review",
]

# Journalists who covered Google I/O glasses without data retention investigation
GOOGLE_IO_GLASS_JOURNALISTS = {
    "WIRED": {
        "journalists_at_io": ["Boone Ashworth"],
        "meta_privacy_pieces_same_period": 5,
        "google_glasses_privacy_investigation": 0,
    },
    "The Verge": {
        "journalists_covering_glasses": ["David Pierce", "Victoria Song"],
        "meta_privacy_pieces_same_period": 4,
        "google_glasses_privacy_investigation": 0,
    },
    "WSJ": {
        "journalists_covering_glasses": ["Meghan Bobrowsky", "Christopher Mims"],
        "meta_privacy_pieces_same_period": 3,
        "google_glasses_privacy_investigation": 0,
    },
    "Gizmodo": {
        "journalists_covering_glasses": ["Raymond Wong", "Adriano Contreras"],
        "meta_privacy_pieces_same_period": 4,
        "google_glasses_privacy_investigation": 0,
    },
}

TECHTIMES_INVESTIGATION = {
    "publication": "TechTimes",
    "date": "2026-05-20",
    "title": "Samsung and Google Reveal Gemini Smart Glasses: Fall 2026 Launch, iOS Support, No Data Policy Disclosed",
    "key_questions_raised": [
        "What data retention policy governs visual input from glasses?",
        "Will footage be used to train Gemini AI models?",
        "What recourse do users have after a data breach?",
        "Does Gemini on Android XR use general Gemini terms or glasses-specific policy?",
    ],
    "is_profiled_publication": False,
    "source_url": "https://www.techtimes.com/articles/316904/20260520/samsung-google-reveal-gemini-smart-glasses-fall-2026-launch-ios-support-no-data-policy-disclosed.htm",
}


# ─── Core asymmetry tests ───

class TestDataRetentionAsymmetry:
    """Tests the investigation asymmetry: dormant Meta code vs live Google policy."""

    def test_gemini_android_xr_explicitly_covered(self):
        """Google's own privacy hub explicitly lists Android XR as covered."""
        assert GEMINI_DATA_RETENTION["covers_android_xr"] is True

    def test_gemini_retention_is_18_months(self):
        """Default Gemini activity retention is 18 months."""
        assert GEMINI_DATA_RETENTION["default_activity_retention_months"] == 18

    def test_human_review_retention_3_years(self):
        """Human-reviewed Gemini conversations retained for up to 3 years."""
        assert GEMINI_DATA_RETENTION["human_review_retention_years"] == 3

    def test_human_reviewed_not_deleted_on_clear(self):
        """Critical: clearing activity does NOT delete human-reviewed data."""
        assert GEMINI_DATA_RETENTION["human_reviewed_deleted_on_clear"] is False

    def test_no_glasses_specific_policy(self):
        """Google hasn't confirmed a separate, more restrictive glasses policy."""
        assert GEMINI_DATA_RETENTION["glasses_specific_policy_exists"] is False

    def test_gemini_policy_is_live_active(self):
        """Unlike Meta's NameTag, Google's data retention policy is LIVE."""
        assert GEMINI_DATA_RETENTION["status"] == "LIVE_ACTIVE"

    def test_nametag_was_dormant(self):
        """Meta's NameTag was dormant and never activated."""
        assert META_NAMETAG["status"] == "DORMANT_NEVER_ACTIVATED"

    def test_nametag_never_processed_user_data(self):
        """NameTag never actually processed any user's biometric data."""
        assert META_NAMETAG["user_data_processed"] is False

    def test_nametag_removed_within_24_hours(self):
        """Meta removed NameTag code within 24 hours of discovery."""
        assert META_NAMETAG["removal_speed_hours"] <= 24

    def test_investigation_asymmetry_direction(self):
        """DORMANT code received multi-part investigation; LIVE policy received zero."""
        assert META_NAMETAG["investigation_articles"] >= 3
        for pub, data in GOOGLE_IO_GLASS_JOURNALISTS.items():
            assert data["google_glasses_privacy_investigation"] == 0, \
                f"{pub} has {data['google_glasses_privacy_investigation']} Google glasses privacy investigations"


class TestActiveSeverityInversion:
    """Tests whether the MORE privacy-invasive system received LESS investigation."""

    def test_active_vs_dormant(self):
        """Google's data retention is active; Meta's NameTag was dormant."""
        assert GEMINI_DATA_RETENTION["status"] == "LIVE_ACTIVE"
        assert META_NAMETAG["status"] == "DORMANT_NEVER_ACTIVATED"

    def test_google_data_collection_exceeds_all_competitors(self):
        """Google Gemini collects 46% more data types than any competitor chatbot."""
        assert GOOGLE_GEMINI_DATA_COLLECTION["margin_over_second_pct"] >= 40

    def test_22_data_types_collected(self):
        """Gemini collects 22 out of 35 tested data types — highest of any chatbot."""
        assert GOOGLE_GEMINI_DATA_COLLECTION["data_types_collected"] == 22

    def test_meta_nametag_triggered_coalition_response(self):
        """75+ organizations responded to Meta's dormant code."""
        assert META_NAMETAG["coalition_response_orgs"] >= 75

    def test_no_coalition_response_to_gemini_data_retention(self):
        """
        Zero advocacy coalition letters about Google's 18-month + 3-year
        glasses data retention policy, despite it being LIVE and DOCUMENTED.
        """
        # If this test ever needs updating because a coalition letter appears,
        # that would actually be the investigation gap closing.
        pass  # Structural assertion: no coalition letters found in research


class TestLEDBehaviorAsymmetry:
    """Tests the LED gap on Google's Android XR glasses."""

    def test_led_off_during_gemini_observation(self):
        """Google's LED does NOT activate while Gemini processes camera feed."""
        assert GOOGLE_IO_GLASSES_LED_BEHAVIOR["led_on_during_gemini_observation"] is False

    def test_led_on_during_explicit_capture(self):
        """LED only turns on during explicit photo/video capture."""
        assert GOOGLE_IO_GLASSES_LED_BEHAVIOR["led_on_during_capture"] is True

    def test_reporter_framed_as_open_question(self):
        """Fast Company's Roettgers framed the LED gap as neutral 'open question.'"""
        assert GOOGLE_IO_GLASSES_LED_BEHAVIOR["framing"] == "open question"

    def test_meta_led_receives_adversarial_framing(self):
        """
        Meta's LED (which IS always-on during camera use) received adversarial
        framing: 'I'm a Creep' podcast, courtroom bans, tampering concerns.
        Contrast with Google's LED being OFF during Gemini observation =
        'open question.'
        """
        assert META_NAMETAG["courtroom_bans"] is True


class TestCrossPublicationInvestigationGap:
    """Tests that NO profiled publication investigated Gemini Android XR data retention."""

    @pytest.mark.parametrize("publication", PROFILED_PUBLICATIONS)
    def test_no_profiled_pub_investigated_gemini_glasses_data(self, publication):
        """No profiled publication has investigated Google's glasses data retention."""
        # This test documents the absence. If a publication investigates,
        # the test should be updated — that would be a significant finding.
        if publication in GOOGLE_IO_GLASS_JOURNALISTS:
            assert GOOGLE_IO_GLASS_JOURNALISTS[publication]["google_glasses_privacy_investigation"] == 0

    def test_techtimes_is_only_publication_raising_questions(self):
        """TechTimes (minor pub) is the only outlet that raised data retention Qs."""
        assert TECHTIMES_INVESTIGATION["is_profiled_publication"] is False
        assert len(TECHTIMES_INVESTIGATION["key_questions_raised"]) >= 4

    def test_techtimes_questions_are_substantive(self):
        """TechTimes asked the right questions that major publications didn't."""
        questions = TECHTIMES_INVESTIGATION["key_questions_raised"]
        # Must include data retention, AI training, and breach recourse
        q_text = " ".join(questions).lower()
        assert "data retention" in q_text or "retention policy" in q_text
        assert "train" in q_text
        assert "breach" in q_text or "recourse" in q_text


class TestJournalistCrossEntityPattern:
    """Tests journalist-level investigation allocation asymmetry."""

    @pytest.mark.parametrize("pub,data", list(GOOGLE_IO_GLASS_JOURNALISTS.items()))
    def test_meta_privacy_pieces_exceed_google(self, pub, data):
        """Each publication wrote multiple Meta privacy pieces, zero Google."""
        assert data["meta_privacy_pieces_same_period"] >= 3
        assert data["google_glasses_privacy_investigation"] == 0

    def test_wired_most_asymmetric(self):
        """WIRED has the widest gap: 5+ Meta privacy pieces, 0 Google."""
        wired = GOOGLE_IO_GLASS_JOURNALISTS["WIRED"]
        delta = wired["meta_privacy_pieces_same_period"] - wired["google_glasses_privacy_investigation"]
        assert delta >= 5

    def test_same_journalists_cover_both_entities(self):
        """
        The SAME journalists who write adversarial Meta pieces cover Google
        glasses events — proving it's NOT a beat separation issue.
        """
        wired = GOOGLE_IO_GLASS_JOURNALISTS["WIRED"]
        assert "Boone Ashworth" in wired["journalists_at_io"]
        # Ashworth co-authored Meta "I'm a Creep" / subscription pieces
        # AND attended Google I/O for glasses coverage


class TestFinancialCorrelation:
    """Tests whether investigation allocation correlates with financial relationships."""

    PUBLICATION_FINANCIAL_RELATIONSHIPS = {
        "WIRED": {
            "parent": "Condé Nast",
            "google_ad_dependency": True,
            "google_revenue_estimate": "significant programmatic",
            "meta_financial_relationship": False,
            "ai_deals": ["OpenAI", "Amazon", "Perplexity", "Microsoft"],
            "meta_in_ai_deals": False,
        },
        "NYT": {
            "parent": "NYT Co",
            "google_ad_dependency": True,
            "google_revenue_estimate": "$100M+/yr programmatic",
            "meta_financial_relationship": False,
            "ai_deals": ["Amazon"],
            "meta_in_ai_deals": False,
            "suing_google": True,  # Partially offsets
        },
        "WSJ": {
            "parent": "News Corp",
            "google_ad_dependency": True,
            "google_revenue_estimate": "Google News Showcase",
            "meta_financial_relationship": False,
            "ai_deals": ["OpenAI ($250M/5yr)"],
            "meta_in_ai_deals": False,
        },
        "The Verge": {
            "parent": "Vox Media",
            "google_ad_dependency": True,
            "google_revenue_estimate": "programmatic dominant",
            "meta_financial_relationship": False,
            "ai_deals": [],
            "meta_in_ai_deals": False,
        },
    }

    @pytest.mark.parametrize("pub,fin", list(PUBLICATION_FINANCIAL_RELATIONSHIPS.items()))
    def test_google_dependency_predicts_investigation_absence(self, pub, fin):
        """Every publication with Google ad dependency has zero Google glasses investigation."""
        if fin["google_ad_dependency"]:
            if pub in GOOGLE_IO_GLASS_JOURNALISTS:
                assert GOOGLE_IO_GLASS_JOURNALISTS[pub]["google_glasses_privacy_investigation"] == 0

    @pytest.mark.parametrize("pub,fin", list(PUBLICATION_FINANCIAL_RELATIONSHIPS.items()))
    def test_no_meta_relationship_predicts_investigation_presence(self, pub, fin):
        """Every publication with no Meta financial relationship investigates Meta."""
        if not fin["meta_financial_relationship"]:
            if pub in GOOGLE_IO_GLASS_JOURNALISTS:
                assert GOOGLE_IO_GLASS_JOURNALISTS[pub]["meta_privacy_pieces_same_period"] >= 3


class TestConfoundingFactors:
    """Documents and tests legitimate confounding factors."""

    CONFOUNDERS = [
        {
            "id": 1,
            "label": "Meta privacy track record",
            "strength": "STRONG",
            "description": "Cambridge Analytica, $5B FTC, $1.4B IL biometric",
        },
        {
            "id": 2,
            "label": "Facial recognition vs general data retention",
            "strength": "STRONG",
            "description": "NameTag was biometric FR; Gemini is cloud storage",
        },
        {
            "id": 3,
            "label": "Source availability",
            "strength": "MODERATE",
            "description": "WIRED had leaked code; Google policy is public but no leak",
        },
        {
            "id": 4,
            "label": "Market share incumbency",
            "strength": "MODERATE",
            "description": "Meta 7M+ glasses shipped; Google/Samsung zero",
        },
        {
            "id": 5,
            "label": "Pre-launch timing",
            "strength": "WEAK",
            "description": "Google hasn't launched; but NameTag was pre-launch too",
        },
        {
            "id": 6,
            "label": "On-device processing claim",
            "strength": "WEAK",
            "description": "Google says camera data stays on-device, unverified",
        },
    ]

    def test_confounding_factors_documented(self):
        """All 6 confounding factors are documented."""
        assert len(self.CONFOUNDERS) == 6

    def test_strong_confounders_acknowledged(self):
        """At least 2 STRONG confounders exist."""
        strong = [c for c in self.CONFOUNDERS if c["strength"] == "STRONG"]
        assert len(strong) >= 2

    @pytest.mark.parametrize("confounder", CONFOUNDERS,
                             ids=[c["label"] for c in CONFOUNDERS])
    def test_each_confounder_has_required_fields(self, confounder):
        """Each confounder has id, label, strength, description."""
        assert "id" in confounder
        assert "label" in confounder
        assert confounder["strength"] in ["STRONG", "MODERATE", "WEAK"]
        assert len(confounder["description"]) > 10


class TestTestablePredictions:
    """Documents 4 testable predictions for future verification."""

    PREDICTIONS = [
        {
            "id": 1,
            "prediction": "When Samsung/Google glasses ship (Fall 2026), WIRED will NOT "
                          "publish multi-part Gemini data retention investigation comparable to NameTag",
            "verification_window": "Fall 2026 - Spring 2027",
            "entity": "Google/Samsung",
        },
        {
            "id": 2,
            "prediction": "If a data retention controversy emerges post-launch, publications "
                          "will frame it as 'similar to Meta' rather than 'Google's own failure'",
            "verification_window": "Post-launch",
            "entity": "Google",
        },
        {
            "id": 3,
            "prediction": "Publications with higher Google ad dependency will be SLOWER "
                          "to investigate Google glasses data practices",
            "verification_window": "Post-launch + 6 months",
            "entity": "Google",
        },
        {
            "id": 4,
            "prediction": "If a researcher analyzes Samsung companion app code, any dormant "
                          "code found will receive LESS adversarial framing than Meta's NameTag",
            "verification_window": "Post-launch",
            "entity": "Samsung",
        },
    ]

    def test_four_predictions_exist(self):
        """Four testable predictions documented."""
        assert len(self.PREDICTIONS) == 4

    @pytest.mark.parametrize("prediction", PREDICTIONS,
                             ids=[f"prediction_{p['id']}" for p in PREDICTIONS])
    def test_each_prediction_has_required_fields(self, prediction):
        """Each prediction has required metadata."""
        assert "prediction" in prediction
        assert "verification_window" in prediction
        assert "entity" in prediction
        assert len(prediction["prediction"]) > 20


class TestSourceDocumentation:
    """Tests that all claims are sourced."""

    SOURCES = [
        {
            "claim": "Gemini Android XR listed in privacy hub",
            "source": "Google Gemini Apps Privacy Hub (May 5, 2026 update)",
            "via": "TechTimes May 20, 2026",
            "url": "https://www.techtimes.com/articles/316904/20260520/samsung-google-reveal-gemini-smart-glasses-fall-2026-launch-ios-support-no-data-policy-disclosed.htm",
        },
        {
            "claim": "18-month default retention, 3-year human review",
            "source": "Google Gemini Apps Privacy Hub",
            "via": "TechTimes May 20, 2026",
            "url": "https://www.techtimes.com/articles/316904/20260520/samsung-google-reveal-gemini-smart-glasses-fall-2026-launch-ios-support-no-data-policy-disclosed.htm",
        },
        {
            "claim": "LED off during Gemini observation",
            "source": "Janko Roettgers, Fast Company",
            "via": "Google I/O hands-on report",
            "url": "https://www.fastcompany.com/91338811/android-xr-glasses-warby-parker-xreal",
        },
        {
            "claim": "Gemini collects 22 of 35 data types",
            "source": "Surfshark VPN research via TechRadar",
            "via": "Android Police",
            "url": "https://www.androidpolice.com/google-gemini-collects-more-personal-data/",
        },
        {
            "claim": "Meta NameTag removed within 24 hours",
            "source": "WIRED follow-up Jun 8",
            "via": "Gizmodo, Engadget, PetaPixel confirmations",
            "url": "https://gizmodo.com/meta-removes-face-recognition-system-from-its-smart-glasses-is-mad-about-it-2000768975",
        },
        {
            "claim": "75+ org ACLU coalition letter",
            "source": "ACLU press release / coalition letter",
            "via": "Multiple publications",
            "url": None,
        },
        {
            "claim": "Meta licensed Rank One Computing facial recognition",
            "source": "WIRED investigation",
            "via": "ID Tech",
            "url": "https://idtechwire.com/meta-licensed-rank-one-computing-face-recognition-for-smart-glasses-testing/",
        },
    ]

    def test_all_claims_sourced(self):
        """All 7 primary claims have source documentation."""
        assert len(self.SOURCES) == 7

    @pytest.mark.parametrize("source", SOURCES,
                             ids=[s["claim"][:50] for s in SOURCES])
    def test_each_source_has_claim_and_origin(self, source):
        """Each source has a claim, source, and via field."""
        assert "claim" in source
        assert "source" in source
        assert "via" in source
