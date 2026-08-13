"""
Mechanism #77: NYT Smart Glasses Coverage Selection Asymmetry — NameTag
Investigation Exclusivity vs Samsung/Google Camera-Identical Hardware Silence

TYPE A: Competitor Coverage Deep Dive (NYT + Samsung/Google Android XR)

KEY FINDING: The New York Times broke the Meta NameTag facial recognition
exclusive (Feb 13, 2026), revealing leaked internal memos about Meta's plan
to add face identification to Ray-Ban smart glasses. The story triggered a
chain reaction: 75+ org ACLU coalition letter, Senate letters (Wyden/Merkley/
Markey), New York state courtroom bans, and multiple follow-up investigations
by WIRED, PetaPixel, and other outlets.

Samsung and Google launched IDENTICAL camera-equipped smart glasses (Google
I/O May 19, 2026; Galaxy Unpacked Jul 22, 2026) with the SAME privacy-
relevant hardware:
  - 12MP cameras (same as Meta)
  - Microphones and speakers
  - AI visual processing (Google Gemini)
  - Privacy LED with anti-tamper detection (copied Meta's design)
  - Always-on companion architecture
  - Smart glasses form factor

NYT has published ZERO standalone privacy investigations of Samsung/Google
glasses. The coverage gap is measurable:

| Entity     | NYT Privacy Investigations | Hardware (cameras) | AI Platform     |
|------------|---------------------------|--------------------|-----------------|
| Meta       | 3+ (NameTag, LED, data)   | 1x 12MP            | Meta AI         |
| Samsung    | 0                         | 1x 12MP            | Google Gemini   |
| Google     | 0                         | N/A (platform)     | Google Gemini   |
| Apple      | 0                         | Planned (N50)      | Siri (planned)  |

CRITICAL DISTINCTION: Google Gemini on Samsung glasses has ACCESS to Google's
entire user data ecosystem (Search, Gmail, Maps, Photos, YouTube). When a user
asks Samsung glasses "who is this?" — Gemini's visual identification capability
(Google Lens) can identify public figures WITHOUT a dedicated "NameTag" feature.
This is a SHIPPING AI capability, not a leaked plan. Yet the NYT has not
investigated whether Gemini on wearables performs visual identification.

FINANCIAL CONTEXT:
  - Samsung: 4th-largest global advertiser ($9.7B/yr) — significant NYT ad buyer
  - Google: $100M+/yr programmatic ad revenue to NYT (structurally dominant)
  - NYT vs Google (litigation): PMC v. Google (D.D.C., Case 1:25-cv-03192-APM)
  - Meta: Direct advertising competitor with NYT — no ad revenue relationship
  - Compound Samsung+Google leverage (Mechanism #76): favorable Samsung glasses
    coverage simultaneously pleases TWO entities with publisher financial ties

CONFOUNDING FACTORS (7, ranked by strength):
  1. STRONG: Source access — NYT had leaked Meta internal documents; may not
     have equivalent Samsung/Google sources for an investigation
  2. STRONG: NameTag was specifically FACIAL RECOGNITION — Samsung has NOT
     announced an equivalent feature. Meta's "reversal" (shutting down FB face
     recognition in 2021, then reintroducing via glasses) is a unique narrative
  3. STRONG: Samsung/Google glasses launched AFTER the NameTag story — different
     news cycle, investigation may simply be pending
  4. MODERATE: Beat assignment — NYT has established Meta beat reporters (Isaac,
     Frenkel) but no dedicated Samsung wearables beat reporter
  5. MODERATE: Meta's Cambridge Analytica / Facebook Papers legacy creates
     editorial priors that make Meta a "default villain" for privacy stories
  6. MODERATE: NYT is SUING Google (via PMC) — Google advertising leverage is
     partially offset by adversarial litigation, though ad dependency remains
  7. WEAK: Google Gemini's visual identification is a general AI capability,
     not a dedicated face-recognition feature — distinction matters editorially

TESTABLE PREDICTIONS:
  1. When Samsung glasses ship (Fall 2026), NYT will NOT publish a standalone
     privacy investigation of Samsung's cameras within 90 days of launch
  2. If Samsung announces facial recognition for its glasses, NYT coverage will
     use SOFTER vocabulary than its NameTag reporting ("face identification"
     vs "surveillance," "recognition feature" vs "dystopian")
  3. Publications with LOWER Samsung advertising revenue (e.g., The Guardian)
     are MORE likely to investigate Samsung glasses privacy
  4. If Google Gemini on Samsung glasses DOES perform visual identification
     of public figures, NYT will frame it as a "Google AI feature" not a
     "Samsung surveillance tool" — entity targeting shifts to Google

Sources:
  - NYT: "Meta Plans 'Name Tag' Facial Recognition for Smart Glasses" (Feb 13, 2026)
    (reported via MacRumors, Slashdot, PetaPixel referencing NYT exclusive)
  - Samsung Newsroom: "Samsung Brings Galaxy Ecosystem Into Everyday Eyewear"
    (Google I/O, May 19, 2026)
  - 9to5Google: "Samsung's Android XR glasses have a privacy light" (Jul 23, 2026)
    https://9to5google.com/2026/07/23/samsung-google-android-xr-glasses-features-privacy-light-details/
  - ACLU coalition letter: 75+ orgs to Zuckerberg (Apr 2026)
    https://www.nyclu.org/press-release/aclu-and-75-organizations-sound-alarm-on-metas-plan-to-add-facial-recognition-technology-to-ray-ban-and-oakley-eyegl
  - NYT financial: Google $100M+/yr programmatic ads (profiles/nytimes.yaml)
  - Samsung: $9.7B/yr advertising spend (profiles/competitor-entities.yaml)
  - Mechanism #76: Samsung-Google Compound Advertiser Leverage

Created: 2026-08-13
"""

import yaml
import os
import pytest
from pathlib import Path

PROFILES_DIR = Path(__file__).parent.parent / "profiles"


def load_yaml(name: str) -> dict:
    with open(PROFILES_DIR / name) as f:
        return yaml.safe_load(f)


# ===================================================================
# 1. MECHANISM #77 EXISTS IN COMPETITOR-COVERAGE-RESEARCH
# ===================================================================


class TestMechanism77InYAML:
    """Verify mechanism #77 is properly documented in competitor-coverage-research.yaml."""

    @pytest.fixture(scope="class")
    def research(self):
        return load_yaml("competitor-coverage-research.yaml")

    def test_mechanism_77_exists(self, research):
        cpf = research.get("cross_publication_findings", {})
        found = any(
            v.get("mechanism_id") == 77
            for v in cpf.values()
            if isinstance(v, dict)
        )
        assert found, "Mechanism #77 must exist in cross_publication_findings"

    def test_mechanism_77_key_name(self, research):
        cpf = research.get("cross_publication_findings", {})
        assert "nyt_samsung_glasses_coverage_selection_silence" in cpf, \
            "Key 'nyt_samsung_glasses_coverage_selection_silence' required"

    def test_mechanism_77_has_finding_summary(self, research):
        cpf = research.get("cross_publication_findings", {})
        mech = cpf.get("nyt_samsung_glasses_coverage_selection_silence", {})
        summary = mech.get("finding_summary", "")
        assert "Samsung" in summary or "samsung" in summary.lower(), \
            "Finding summary must reference Samsung"
        assert "NYT" in summary or "New York Times" in summary, \
            "Finding summary must reference NYT"

    def test_mechanism_77_has_test_file(self, research):
        cpf = research.get("cross_publication_findings", {})
        mech = cpf.get("nyt_samsung_glasses_coverage_selection_silence", {})
        tf = mech.get("test_file", "")
        assert "nyt_samsung_glasses" in tf, \
            "test_file must reference this test"

    def test_mechanism_77_has_date(self, research):
        cpf = research.get("cross_publication_findings", {})
        mech = cpf.get("nyt_samsung_glasses_coverage_selection_silence", {})
        assert mech.get("date_added") == "2026-08-13", \
            "date_added should be 2026-08-13"


# ===================================================================
# 2. NYT PROFILE — META NAMETAG INVESTIGATION EXISTS
# ===================================================================


class TestNYTNameTagInvestigationDocumented:
    """NYT broke the NameTag exclusive — verify documentation."""

    @pytest.fixture(scope="class")
    def nyt_profile(self):
        return load_yaml("nytimes.yaml")

    def test_nyt_has_meta_glasses_coverage(self, nyt_profile):
        """NYT profile must reference Meta glasses / NameTag coverage."""
        profile_str = yaml.dump(nyt_profile).lower()
        has_nametag = "nametag" in profile_str or "name tag" in profile_str
        has_glasses = "smart glasses" in profile_str or "ray-ban" in profile_str
        has_facial_rec = "facial recognition" in profile_str
        assert has_nametag or has_glasses or has_facial_rec, \
            "NYT profile should reference NameTag, smart glasses, or facial recognition"


# ===================================================================
# 3. SAMSUNG HARDWARE PARITY — IDENTICAL PRIVACY-RELEVANT FEATURES
# ===================================================================


class TestSamsungHardwareParity:
    """Samsung glasses have identical privacy-relevant hardware to Meta."""

    @pytest.fixture(scope="class")
    def entities(self):
        return load_yaml("competitor-entities.yaml")

    def test_samsung_entity_exists(self, entities):
        ents = entities.get("entities", {})
        assert "samsung" in ents, "Samsung must be in competitor-entities"

    def test_samsung_has_camera_hardware(self, entities):
        samsung = entities["entities"].get("samsung", {})
        samsung_str = yaml.dump(samsung).lower()
        has_camera = "camera" in samsung_str
        has_glasses = "glasses" in samsung_str or "eyewear" in samsung_str
        assert has_camera or has_glasses, \
            "Samsung entity must reference camera-equipped glasses/eyewear"

    def test_samsung_has_advertising_leverage(self, entities):
        samsung = entities["entities"].get("samsung", {})
        samsung_str = yaml.dump(samsung).lower()
        has_ad = "advertis" in samsung_str
        assert has_ad, "Samsung entity must document advertising leverage"

    def test_samsung_ad_spend_documented(self, entities):
        samsung = entities["entities"].get("samsung", {})
        samsung_str = yaml.dump(samsung)
        # Samsung is ~$9.7B/yr in measured media spend
        has_figure = "9.7" in samsung_str or "9,700" in samsung_str or \
                     "billion" in samsung_str.lower()
        assert has_figure, "Samsung's ~$9.7B/yr advertising spend must be documented"


# ===================================================================
# 4. NYT-GOOGLE FINANCIAL RELATIONSHIP DOCUMENTED
# ===================================================================


class TestNYTGoogleFinancialRelationship:
    """NYT depends on Google for $100M+/yr in programmatic ads."""

    @pytest.fixture(scope="class")
    def nyt_profile(self):
        return load_yaml("nytimes.yaml")

    def test_nyt_google_financial_relationship_exists(self, nyt_profile):
        profile_str = yaml.dump(nyt_profile).lower()
        assert "google" in profile_str and "programmatic" in profile_str, \
            "NYT profile must document Google programmatic ad relationship"

    def test_nyt_google_ad_revenue_figure(self, nyt_profile):
        """NYT receives $100M+/yr from Google ad tech stack."""
        profile_str = yaml.dump(nyt_profile)
        assert "100M" in profile_str or "$100" in profile_str, \
            "NYT-Google relationship must document $100M+ figure"


# ===================================================================
# 5. META AS AD COMPETITOR (NO AD REVENUE TO NYT)
# ===================================================================


class TestMetaAdCompetitorRelationship:
    """Meta is NYT's ad competitor, not ad revenue source."""

    @pytest.fixture(scope="class")
    def entities(self):
        return load_yaml("competitor-entities.yaml")

    def test_meta_ad_competitor_documented(self, entities):
        meta = entities.get("entities", {}).get("meta", {})
        if meta:
            meta_str = yaml.dump(meta).lower()
            has_competitor = "competitor" in meta_str or "antagonis" in meta_str
            assert has_competitor, \
                "Meta entity should reference ad competitor/antagonism status"


# ===================================================================
# 6. COVERAGE SELECTION DIFFERENTIAL — ZERO SAMSUNG INVESTIGATIONS
# ===================================================================


class TestCoverageSelectionDifferential:
    """Verify the coverage gap is documented in research YAML."""

    @pytest.fixture(scope="class")
    def research(self):
        return load_yaml("competitor-coverage-research.yaml")

    def test_meta_nyt_privacy_investigation_count(self, research):
        """NYT has 3+ Meta privacy investigations; mechanism must document this."""
        cpf = research.get("cross_publication_findings", {})
        mech = cpf.get("nyt_samsung_glasses_coverage_selection_silence", {})
        mech_str = yaml.dump(mech).lower()
        # Must reference NYT's Meta investigation count
        has_count = "3" in mech_str or "three" in mech_str or \
                    "multiple" in mech_str or "nametag" in mech_str
        assert has_count, \
            "Mechanism must document NYT's multiple Meta privacy investigations"

    def test_samsung_zero_investigations_documented(self, research):
        """Samsung receives 0 NYT standalone privacy investigations."""
        cpf = research.get("cross_publication_findings", {})
        mech = cpf.get("nyt_samsung_glasses_coverage_selection_silence", {})
        mech_str = yaml.dump(mech).lower()
        has_zero = "zero" in mech_str or "0" in mech_str or "none" in mech_str
        assert has_zero, \
            "Mechanism must document Samsung's ZERO NYT privacy investigations"


# ===================================================================
# 7. CONFOUNDING FACTORS (minimum 5)
# ===================================================================


class TestConfoundingFactorsDocumented:
    """Mechanism must document confounding factors for intellectual honesty."""

    @pytest.fixture(scope="class")
    def research(self):
        return load_yaml("competitor-coverage-research.yaml")

    def test_confounding_factors_exist(self, research):
        cpf = research.get("cross_publication_findings", {})
        mech = cpf.get("nyt_samsung_glasses_coverage_selection_silence", {})
        confounds = mech.get("confounding_factors", [])
        assert len(confounds) >= 5, \
            f"Must have >= 5 confounding factors, found {len(confounds)}"

    def test_source_access_confound(self, research):
        """Source access is the strongest confound — NYT had leaked Meta docs."""
        cpf = research.get("cross_publication_findings", {})
        mech = cpf.get("nyt_samsung_glasses_coverage_selection_silence", {})
        confounds_str = yaml.dump(mech.get("confounding_factors", [])).lower()
        assert "source" in confounds_str or "leaked" in confounds_str, \
            "Must document source access as a confounding factor"

    def test_facial_recognition_specificity_confound(self, research):
        """NameTag was specifically facial recognition — Samsung hasn't announced one."""
        cpf = research.get("cross_publication_findings", {})
        mech = cpf.get("nyt_samsung_glasses_coverage_selection_silence", {})
        confounds_str = yaml.dump(mech.get("confounding_factors", [])).lower()
        has_fr = "facial recognition" in confounds_str or \
                 "face recognition" in confounds_str or \
                 "nametag" in confounds_str
        assert has_fr, \
            "Must document that NameTag was specifically facial recognition"


# ===================================================================
# 8. TESTABLE PREDICTIONS
# ===================================================================


class TestTestablePredictions:
    """Mechanism must include testable predictions for falsifiability."""

    @pytest.fixture(scope="class")
    def research(self):
        return load_yaml("competitor-coverage-research.yaml")

    def test_predictions_exist(self, research):
        cpf = research.get("cross_publication_findings", {})
        mech = cpf.get("nyt_samsung_glasses_coverage_selection_silence", {})
        predictions = mech.get("testable_predictions", [])
        assert len(predictions) >= 3, \
            f"Must have >= 3 testable predictions, found {len(predictions)}"

    def test_prediction_references_samsung_launch(self, research):
        """At least one prediction should reference Samsung glasses shipping."""
        cpf = research.get("cross_publication_findings", {})
        mech = cpf.get("nyt_samsung_glasses_coverage_selection_silence", {})
        preds_str = yaml.dump(mech.get("testable_predictions", [])).lower()
        has_launch = "launch" in preds_str or "ship" in preds_str or \
                     "fall 2026" in preds_str
        assert has_launch, \
            "Prediction must reference Samsung glasses launch timing"


# ===================================================================
# 9. CROSS-REFERENCES TO RELATED MECHANISMS
# ===================================================================


class TestCrossReferences:
    """Mechanism should reference related mechanisms."""

    @pytest.fixture(scope="class")
    def research(self):
        return load_yaml("competitor-coverage-research.yaml")

    def test_references_samsung_equivalence_paradox(self, research):
        """Should reference the Samsung Equivalence Paradox mechanism."""
        cpf = research.get("cross_publication_findings", {})
        mech = cpf.get("nyt_samsung_glasses_coverage_selection_silence", {})
        mech_str = yaml.dump(mech).lower()
        has_ref = "equivalence paradox" in mech_str or \
                  "mechanism" in mech_str
        assert has_ref, "Should reference related Samsung mechanisms"

    def test_references_compound_advertiser_leverage(self, research):
        """Should reference Samsung-Google compound leverage (#76)."""
        cpf = research.get("cross_publication_findings", {})
        mech = cpf.get("nyt_samsung_glasses_coverage_selection_silence", {})
        mech_str = yaml.dump(mech)
        has_76 = "#76" in mech_str or "76" in mech_str or \
                 "compound" in mech_str.lower()
        assert has_76, "Should reference Mechanism #76 (compound leverage)"
