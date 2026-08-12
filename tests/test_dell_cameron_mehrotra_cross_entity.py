"""
Cross-entity coverage analysis: Dell Cameron & Dhruv Mehrotra (WIRED investigative team)

Mechanism #66: Investigative Resource Allocation as Entity-Targeting —
WIRED's Cameron-Mehrotra Privacy Investigation Asymmetry

KEY FINDING: Dell Cameron and Dhruv Mehrotra are WIRED's investigative
privacy/surveillance reporters. In 2026, they published a multi-part
investigative series on Meta's NameTag facial recognition code embedded in
the Meta AI app (Jun 4, Jun 8, and follow-ups on Rank One Computing).
The series demonstrated genuine investigative skill: code analysis,
independent expert reproduction, timeline reconstruction showing Meta had
deployed 3 AI models (face detection, cropping, biometric encoding) to
users' phones before publicly claiming the feature "doesn't exist."

The asymmetry: Cameron and Mehrotra have ZERO equivalent investigations
into Apple, Google, or Samsung privacy practices in the wearables space,
despite Apple Vision Pro having 12 outward-facing cameras (vs Meta's 1),
Google Android XR glasses having cameras, Samsung Galaxy Glasses having
cameras, and Snap Spectacles having 4 cameras.

This is not a criticism of the NameTag investigation itself — it was
legitimate and important journalism. The asymmetry is in the EDITORIAL
ALLOCATION of investigative resources. WIRED's editorial leadership
assigns Cameron/Mehrotra to investigate Meta's single-camera glasses
while the 12-camera Apple Vision Pro, the Apple PCC-to-Google Cloud
privacy architecture shift, Google's AI data collection through Android
XR, and Samsung/Google's identical camera hardware receive NO
investigative treatment from WIRED's privacy desk.

MECHANISM: The lane assignment operates at the editorial level, not the
journalist level. Cameron and Mehrotra report what they're assigned.
The asymmetry is structural — WIRED's editorial leadership (Katie Drummond)
channels investigative privacy resources toward Meta and consumer review
resources toward Apple/Google. This produces publication-level framing
asymmetry that is invisible in any single article.

FINANCIAL CONTEXT: Condé Nast (WIRED's parent) has AI licensing deals with
OpenAI (Aug 2024), Amazon (Jul 2025), Perplexity (2025), Microsoft (Dec 2025),
and is in Apple News Plus negotiations. Meta has NO financial relationship
with Condé Nast. The investigative resources track exactly with the financial
incentive structure: investigate the company that pays nothing, don't
investigate the companies that pay.

CONFOUNDING FACTORS:
1. Meta has a worse privacy track record historically (Facebook Cambridge
   Analytica, FTC $5B settlement). Reasonable editorial judgment could
   justify more scrutiny.
2. Apple's Vision Pro shipped 2024 and was recalled/discontinued 2025 —
   smaller installed base than Meta's 7M+ glasses.
3. Meta's NameTag was genuinely newsworthy — face recognition on glasses
   worn in public is a real privacy concern.
4. Apple, Samsung, and Google haven't shipped their smart glasses yet
   (as of Aug 2026), so there's less deployed code to investigate.
5. Cameron/Mehrotra may have pitched Meta stories themselves — editors
   approve but don't necessarily assign every story.

TESTABLE PREDICTIONS:
1. When Apple ships camera glasses (projected late 2027), WIRED will NOT
   assign Cameron/Mehrotra to investigate Apple's privacy practices —
   coverage will go to Lauren Goode (consumer review) or a news desk
   reporter (neutral framing).
2. When Samsung/Google ship camera glasses (fall 2026), WIRED's investigative
   desk will not produce equivalent "dormant surveillance infrastructure"
   coverage — despite identical hardware.
3. If Apple ships glasses without a camera, WIRED will frame this as
   "privacy leadership" rather than "feature deficiency" — positive framing
   for the competitor's limitation.
4. Cameron/Mehrotra will continue producing Meta privacy investigations
   through 2027 without equivalent investigations of Apple, Google, or
   Samsung privacy practices.

Sources:
  - WIRED: Cameron/Mehrotra "Meta Smart Glasses Had Hidden Facial Recognition Code"
    (Jun 4, 2026) — via Slashdot, Gizmodo, Digital Trends, Pixel Envy secondary coverage
    https://yro.slashdot.org/story/26/06/08/1945252/meta-deletes-face-recognition-system-from-its-smart-glasses-app
  - WIRED: Cameron/Mehrotra follow-up: Meta removes NameTag code (Jun 8, 2026)
    https://gizmodo.com/meta-removes-face-recognition-system-from-its-smart-glasses-is-mad-about-it-2000768975
  - WIRED: Cameron/Mehrotra: Rank One Computing military/police facial recognition supplier
    https://www.digitaltrends.com/wearables/meta-is-testing-smart-glass-facial-recognition-tech-thats-also-used-by-police-and-military-report/
  - Pixel Envy attribution: "Dhruv Mehrotra and Dell Cameron, Wired"
    https://pxlnv.com/linklog/meta-ai-facial-recognition-code/
  - WIRED profile cross_entity_wearables_framing: Apple Vision Pro 12 cameras, zero
    surveillance framing (Lauren Goode "I Cried Inside the Apple Vision Pro")
  - WIRED profile editorial_lane_assignment_mechanism: structural analysis
  - Press Freedom Tracker: Cameron subpoenaed in Meta lawsuit (2024)
    https://pressfreedomtracker.us/all-incidents/wired-reporter-subpoenaed-in-adult-entertainers-lawsuit-against-meta/

Created: 2026-08-12
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
# 1. MECHANISM #66 EXISTS IN COMPETITOR-COVERAGE-RESEARCH
# ===================================================================


class TestMechanism66InYAML:
    """Verify mechanism #66 is properly documented in competitor-coverage-research.yaml."""

    @pytest.fixture(scope="class")
    def research(self):
        return load_yaml("competitor-coverage-research.yaml")

    @pytest.fixture(scope="class")
    def cpf(self, research):
        return research.get("cross_publication_findings", {})

    def test_mechanism_66_exists(self, cpf):
        found = any(
            v.get("mechanism_id") == 66
            for v in cpf.values()
            if isinstance(v, dict)
        )
        assert found, "Mechanism #66 must exist in cross_publication_findings"

    def test_mechanism_66_key_name(self, cpf):
        assert "cameron_mehrotra_investigative_resource_allocation" in cpf, \
            "Key must be cameron_mehrotra_investigative_resource_allocation"

    def test_mechanism_name(self, cpf):
        entry = cpf["cameron_mehrotra_investigative_resource_allocation"]
        assert entry["mechanism"] == "investigative_resource_allocation_entity_targeting"

    def test_mechanism_id_is_66(self, cpf):
        entry = cpf["cameron_mehrotra_investigative_resource_allocation"]
        assert entry["mechanism_id"] == 66

    def test_journalists_listed(self, cpf):
        entry = cpf["cameron_mehrotra_investigative_resource_allocation"]
        journalists = entry.get("journalists", [])
        names = [j["name"] for j in journalists]
        assert "Dell Cameron" in names
        assert "Dhruv Mehrotra" in names

    def test_publication_wired(self, cpf):
        entry = cpf["cameron_mehrotra_investigative_resource_allocation"]
        assert entry["publication"] == "WIRED"


# ===================================================================
# 2. CAMERON/MEHROTRA META INVESTIGATIONS DOCUMENTED
# ===================================================================


class TestCameronMehrotraMetaInvestigations:
    """Verify the Meta investigations are properly documented."""

    @pytest.fixture(scope="class")
    def entry(self):
        research = load_yaml("competitor-coverage-research.yaml")
        cpf = research.get("cross_publication_findings", {})
        return cpf["cameron_mehrotra_investigative_resource_allocation"]

    def test_has_meta_investigations(self, entry):
        assert "meta_investigations" in entry
        assert len(entry["meta_investigations"]) >= 3

    def test_nametag_discovery_documented(self, entry):
        titles = [inv.get("title", "") for inv in entry["meta_investigations"]]
        nametag = any("nametag" in t.lower() or "facial recognition" in t.lower()
                      for t in titles)
        assert nametag, "NameTag facial recognition investigation must be documented"

    def test_nametag_date_june_2026(self, entry):
        for inv in entry["meta_investigations"]:
            if "nametag" in inv.get("title", "").lower() or \
               "facial recognition" in inv.get("title", "").lower():
                assert inv["date"].startswith("2026-06"), \
                    "NameTag investigation was June 2026"
                break

    def test_code_removal_followup(self, entry):
        titles = [inv.get("title", "") for inv in entry["meta_investigations"]]
        removal = any("remov" in t.lower() or "delet" in t.lower()
                      for t in titles)
        assert removal, "Code removal follow-up must be documented"

    def test_rank_one_computing_investigation(self, entry):
        titles = [inv.get("title", "") for inv in entry["meta_investigations"]]
        rank_one = any("rank one" in t.lower() or "military" in t.lower()
                       for t in titles)
        assert rank_one, "Rank One Computing investigation must be documented"

    def test_all_investigations_have_framing(self, entry):
        for inv in entry["meta_investigations"]:
            assert "framing" in inv, f"Investigation '{inv.get('title')}' must have framing"

    def test_all_investigations_have_source_urls(self, entry):
        for inv in entry["meta_investigations"]:
            assert "source_urls" in inv or "source_url" in inv, \
                f"Investigation '{inv.get('title')}' must have source URL(s)"

    def test_meta_investigations_adversarial_tone(self, entry):
        """All Meta investigations should have negative/adversarial tone scores."""
        for inv in entry["meta_investigations"]:
            tone = inv.get("tone", 0)
            assert tone < 0, \
                f"Meta investigation '{inv.get('title')}' should have negative tone, got {tone}"


# ===================================================================
# 3. COMPETITOR INVESTIGATION ABSENCE DOCUMENTED
# ===================================================================


class TestCompetitorInvestigationAbsence:
    """Verify that the absence of competitor investigations is documented."""

    @pytest.fixture(scope="class")
    def entry(self):
        research = load_yaml("competitor-coverage-research.yaml")
        cpf = research.get("cross_publication_findings", {})
        return cpf["cameron_mehrotra_investigative_resource_allocation"]

    def test_has_competitor_investigation_absence(self, entry):
        assert "competitor_investigation_absence" in entry

    def test_apple_absence_documented(self, entry):
        absence = entry["competitor_investigation_absence"]
        apple = [a for a in absence if a.get("entity") == "Apple"]
        assert len(apple) >= 1, "Apple investigation absence must be documented"

    def test_google_absence_documented(self, entry):
        absence = entry["competitor_investigation_absence"]
        google = [a for a in absence if a.get("entity") == "Google"]
        assert len(google) >= 1, "Google investigation absence must be documented"

    def test_samsung_absence_documented(self, entry):
        absence = entry["competitor_investigation_absence"]
        samsung = [a for a in absence if a.get("entity") == "Samsung"]
        assert len(samsung) >= 1, "Samsung investigation absence must be documented"

    def test_snap_absence_documented(self, entry):
        absence = entry["competitor_investigation_absence"]
        snap = [a for a in absence if a.get("entity") == "Snap"]
        assert len(snap) >= 1, "Snap investigation absence must be documented"

    def test_apple_vision_pro_camera_count(self, entry):
        """Apple Vision Pro has 12 cameras — more than Meta's 1."""
        absence = entry["competitor_investigation_absence"]
        apple = [a for a in absence if a.get("entity") == "Apple"][0]
        assert apple.get("camera_count", 0) >= 12

    def test_absence_entries_have_privacy_relevance(self, entry):
        absence = entry["competitor_investigation_absence"]
        for a in absence:
            assert "privacy_relevant_capability" in a, \
                f"Absence for {a.get('entity')} must document privacy-relevant capability"


# ===================================================================
# 4. LANE ASSIGNMENT MECHANISM
# ===================================================================


class TestLaneAssignmentMechanism:
    """Verify the editorial lane assignment analysis."""

    @pytest.fixture(scope="class")
    def entry(self):
        research = load_yaml("competitor-coverage-research.yaml")
        cpf = research.get("cross_publication_findings", {})
        return cpf["cameron_mehrotra_investigative_resource_allocation"]

    def test_has_lane_assignment_analysis(self, entry):
        assert "lane_assignment_analysis" in entry

    def test_consumer_review_lane_identified(self, entry):
        lane = entry["lane_assignment_analysis"]
        assert "consumer_review_reporters" in lane
        reporters = lane["consumer_review_reporters"]
        names = [r.get("name", "") for r in reporters]
        assert "Lauren Goode" in names, \
            "Lauren Goode must be identified as consumer review reporter"

    def test_investigative_lane_identified(self, entry):
        lane = entry["lane_assignment_analysis"]
        assert "investigative_reporters" in lane
        reporters = lane["investigative_reporters"]
        names = [r.get("name", "") for r in reporters]
        assert "Dell Cameron" in names
        assert "Dhruv Mehrotra" in names

    def test_lane_determines_framing(self, entry):
        lane = entry["lane_assignment_analysis"]
        assert "structural_effect" in lane
        effect = lane["structural_effect"]
        assert "assignment" in effect.lower() or "editorial" in effect.lower(), \
            "Structural effect should explain how assignment determines framing"

    def test_editorial_leadership_named(self, entry):
        lane = entry["lane_assignment_analysis"]
        assert "editor_in_chief" in lane
        assert "Drummond" in lane["editor_in_chief"] or \
               "Katie" in lane["editor_in_chief"]


# ===================================================================
# 5. FINANCIAL ALIGNMENT
# ===================================================================


class TestFinancialAlignment:
    """Verify financial incentive correlation is documented."""

    @pytest.fixture(scope="class")
    def entry(self):
        research = load_yaml("competitor-coverage-research.yaml")
        cpf = research.get("cross_publication_findings", {})
        return cpf["cameron_mehrotra_investigative_resource_allocation"]

    def test_has_financial_context(self, entry):
        assert "financial_context" in entry

    def test_meta_zero_deal(self, entry):
        fc = entry["financial_context"]
        meta_deal = fc.get("meta_conde_nast_deal", "")
        assert "none" in meta_deal.lower() or "zero" in meta_deal.lower() or \
               "$0" in meta_deal, \
            "Must document that Meta has no Condé Nast deal"

    def test_conde_nast_ai_deals_listed(self, entry):
        fc = entry["financial_context"]
        deals = fc.get("conde_nast_ai_deals", [])
        deal_partners = [d.get("partner", "") for d in deals]
        assert any("OpenAI" in p for p in deal_partners), "OpenAI deal must be listed"
        assert any("Amazon" in p or "Rufus" in p for p in deal_partners), \
            "Amazon deal must be listed"

    def test_apple_news_plus_negotiations(self, entry):
        fc = entry["financial_context"]
        apple = fc.get("apple_relationship", "")
        assert "news" in apple.lower() or "negotiat" in apple.lower() or \
               "licensing" in apple.lower(), \
            "Apple News Plus licensing negotiations must be documented"


# ===================================================================
# 6. CONFOUNDING FACTORS (INTELLECTUAL HONESTY)
# ===================================================================


class TestConfoundingFactors:
    """Confounding factors must be documented for intellectual honesty."""

    @pytest.fixture(scope="class")
    def entry(self):
        research = load_yaml("competitor-coverage-research.yaml")
        cpf = research.get("cross_publication_findings", {})
        return cpf["cameron_mehrotra_investigative_resource_allocation"]

    def test_has_confounding_factors(self, entry):
        assert "confounding_factors" in entry
        assert len(entry["confounding_factors"]) >= 4

    def test_meta_privacy_history_acknowledged(self, entry):
        factors = entry["confounding_factors"]
        history = any("track record" in f.get("factor", "").lower() or
                      "cambridge" in f.get("factor", "").lower() or
                      "history" in f.get("factor", "").lower()
                      for f in factors)
        assert history, "Meta's worse privacy history must be acknowledged"

    def test_competitor_product_maturity_acknowledged(self, entry):
        factors = entry["confounding_factors"]
        maturity = any("ship" in f.get("factor", "").lower() or
                       "launch" in f.get("factor", "").lower() or
                       "deployed" in f.get("factor", "").lower() or
                       "installed" in f.get("factor", "").lower()
                       for f in factors)
        assert maturity, "Competitor products not yet shipping must be acknowledged"

    def test_nametag_newsworthiness_acknowledged(self, entry):
        factors = entry["confounding_factors"]
        newsworthy = any("newsworthy" in f.get("factor", "").lower() or
                         "legitimate" in f.get("factor", "").lower() or
                         "genuine" in f.get("factor", "").lower()
                         for f in factors)
        assert newsworthy, "NameTag investigation's legitimate newsworthiness must be acknowledged"

    def test_confounding_factors_have_strength(self, entry):
        factors = entry["confounding_factors"]
        for f in factors:
            assert "strength" in f, f"Factor '{f.get('factor', '')}' must have strength rating"


# ===================================================================
# 7. CROSS-REFERENCES
# ===================================================================


class TestCrossReferences:
    """Verify cross-references to related mechanisms."""

    @pytest.fixture(scope="class")
    def entry(self):
        research = load_yaml("competitor-coverage-research.yaml")
        cpf = research.get("cross_publication_findings", {})
        return cpf["cameron_mehrotra_investigative_resource_allocation"]

    def test_has_cross_references(self, entry):
        assert "cross_references" in entry
        assert len(entry["cross_references"]) >= 2

    def test_references_chokkattu_ashworth(self, entry):
        """Should cross-reference the Chokkattu/Ashworth gear desk asymmetry."""
        refs = entry["cross_references"]
        ref_ids = [r.get("mechanism_id") for r in refs if isinstance(r, dict)]
        ref_strs = [str(r) for r in refs if not isinstance(r, dict)]
        chokkattu = any(rid in [14, 44, 49] for rid in ref_ids) or \
                    any("chokkattu" in s.lower() or "ashworth" in s.lower()
                        for s in ref_strs)
        assert chokkattu, "Must cross-reference Chokkattu/Ashworth mechanisms"

    def test_references_gurman_access_dependency(self, entry):
        """Should cross-reference Gurman's access dependency mechanism."""
        refs = entry["cross_references"]
        ref_ids = [r.get("mechanism_id") for r in refs if isinstance(r, dict)]
        ref_strs = [str(r) for r in refs if not isinstance(r, dict)]
        gurman = 11 in ref_ids or \
                 any("gurman" in s.lower() or "access dependency" in s.lower()
                     for s in ref_strs)
        assert gurman, "Must cross-reference Gurman access dependency (#11)"


# ===================================================================
# 8. TESTABLE PREDICTIONS
# ===================================================================


class TestTestablePredictions:
    """Verify testable predictions are documented."""

    @pytest.fixture(scope="class")
    def entry(self):
        research = load_yaml("competitor-coverage-research.yaml")
        cpf = research.get("cross_publication_findings", {})
        return cpf["cameron_mehrotra_investigative_resource_allocation"]

    def test_has_testable_predictions(self, entry):
        assert "testable_predictions" in entry
        assert len(entry["testable_predictions"]) >= 3

    def test_apple_glasses_prediction(self, entry):
        preds = entry["testable_predictions"]
        apple = any("apple" in p.get("prediction", "").lower() and
                     "glass" in p.get("prediction", "").lower()
                     for p in preds)
        assert apple, "Must predict coverage pattern when Apple ships glasses"

    def test_samsung_google_prediction(self, entry):
        preds = entry["testable_predictions"]
        samsung = any(("samsung" in p.get("prediction", "").lower() or
                       "google" in p.get("prediction", "").lower()) and
                      ("glass" in p.get("prediction", "").lower() or
                       "android xr" in p.get("prediction", "").lower())
                      for p in preds)
        assert samsung, "Must predict coverage pattern when Samsung/Google ships glasses"


# ===================================================================
# 9. WIRED PROFILE INTEGRATION
# ===================================================================


class TestWiredProfileIntegration:
    """Verify Dell Cameron and Dhruv Mehrotra are in WIRED's journalist section."""

    @pytest.fixture(scope="class")
    def wired_profile(self):
        return load_yaml("wired.yaml")

    def test_dell_cameron_in_wired_profile(self, wired_profile):
        """Dell Cameron must appear in WIRED's profile."""
        yaml_str = yaml.dump(wired_profile)
        assert "Dell Cameron" in yaml_str, "Dell Cameron must be in wired.yaml"

    def test_dhruv_mehrotra_in_wired_profile(self, wired_profile):
        """Dhruv Mehrotra must appear in WIRED's profile."""
        yaml_str = yaml.dump(wired_profile)
        assert "Dhruv Mehrotra" in yaml_str, "Dhruv Mehrotra must be in wired.yaml"

    def test_investigative_designation(self, wired_profile):
        """Cameron/Mehrotra should be identified as investigative reporters."""
        yaml_str = yaml.dump(wired_profile)
        assert "investigative" in yaml_str.lower(), \
            "WIRED profile must reference investigative reporting"


# ===================================================================
# 10. CAMERA COUNT PARADOX VALIDATION
# ===================================================================


class TestCameraCountParadox:
    """The camera count paradox: more cameras = less investigation."""

    @pytest.fixture(scope="class")
    def entry(self):
        research = load_yaml("competitor-coverage-research.yaml")
        cpf = research.get("cross_publication_findings", {})
        return cpf["cameron_mehrotra_investigative_resource_allocation"]

    def test_has_camera_count_comparison(self, entry):
        assert "camera_count_paradox" in entry

    def test_apple_more_cameras_than_meta(self, entry):
        paradox = entry["camera_count_paradox"]
        assert paradox.get("apple_vision_pro_cameras", 0) > \
               paradox.get("meta_rayban_cameras", 0), \
            "Apple Vision Pro must have more cameras than Meta Ray-Ban"

    def test_apple_cameras_documented(self, entry):
        paradox = entry["camera_count_paradox"]
        assert paradox.get("apple_vision_pro_cameras", 0) >= 12

    def test_meta_cameras_documented(self, entry):
        paradox = entry["camera_count_paradox"]
        assert paradox.get("meta_rayban_cameras", 0) == 1

    def test_snap_cameras_documented(self, entry):
        paradox = entry["camera_count_paradox"]
        assert paradox.get("snap_spectacles_cameras", 0) >= 4

    def test_paradox_conclusion(self, entry):
        paradox = entry["camera_count_paradox"]
        assert "conclusion" in paradox
        conclusion = paradox["conclusion"]
        assert "manufacturer" in conclusion.lower() or \
               "identity" in conclusion.lower() or \
               "entity" in conclusion.lower(), \
            "Conclusion must state that entity identity, not camera count, drives coverage"
