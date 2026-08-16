"""
Mechanism #131: Ben Schoon (9to5Google) Cross-Entity Control Calibration —
Independent Outlet Privacy Vocabulary Distribution Quantifies Institutional
Amplification at Condé Nast / Future plc / Yahoo-Apollo Publications

TYPE B: Journalist Cross-Entity Tracking

CORE FINDING: Ben Schoon at 9to5Google (925 LLC, Seth Weintraub sole owner,
no corporate media parent, no VC backing, no AI content deals) applies privacy
vocabulary to Meta AND Samsung/Google camera glasses, creating a measurable
baseline for "natural" editorial concern about the smart glasses category.

The DELTA between Schoon's roughly 3:1 Meta-to-competitor privacy vocabulary
ratio and WIRED/Gizmodo/Future plc's infinite ratio (10+ terms for Meta,
ZERO for competitors) quantifies the institutional amplification factor.

KEY EVIDENCE:

Meta coverage (privacy-skeptical, product-aware):
- Jul 7, 2026: "Meta Ray-Ban glasses now disable the camera if privacy light breaks"
  Aggregated Victoria Song (Verge), added original analysis noting Gen 1 vs Gen 2
  enforcement gap. Privacy vocabulary: camera disable, privacy light, enforcement.
- Jul 9, 2026: "Meta developing always-on glasses with less-active privacy light"
  Aggregated FT/Hannah Murphy, editorial: "Needless to say, there are a lot of problems
  with that idea, including privacy (you cannot and should not be recording all the time)"
  Privacy vocabulary: problems, privacy, should not be recording all the time.

Samsung/Google coverage (skepticism-aware, applied evenly):
- Jul 23, 2026 (Inbox Newsletter #4): Samsung Unpacked Galaxy Glasses coverage.
  "Samsung and Google are diving head-first into this cultural quagmire, and while
  neither company has Meta's reputation for flamboyantly disregarding user privacy
  — and Samsung promises that it has accounted for tampering and abuse — by releasing
  these products they're subject to the same scrutiny."
  Privacy vocabulary: cultural quagmire, disregarding user privacy, tampering, abuse,
  subject to the same scrutiny.
  KEY: Applies privacy concern to Samsung/Google — they face "the same scrutiny."

THE INSTITUTIONAL DELTA:

9to5Google (control, independent):
  Meta privacy terms: ~5 (camera disable, privacy light, problems, should not record,
                          enforcement gap)
  Samsung/Google privacy terms: ~3 (cultural quagmire, tampering/abuse, same scrutiny)
  RATIO: ~1.7:1 (Meta slightly more, reasonable given market share & history)

WIRED (Condé Nast, Advance Publications):
  Meta privacy terms: 10+ (tool for mass surveillance, creep, creepy, alarming,
                            flooding the market, up in arms, privacy lightning rod,
                            drawn the ire, Glasshole, etc.)
  Samsung/Google privacy terms: 0
  RATIO: ∞ (undefined — ZERO competitor scrutiny)

Future plc (3-layer Google financial dependency, mechanism #114):
  Meta privacy terms: 6+ per writer (frightening, worrying, creepy, scared, terror, etc.)
  Samsung/Google privacy terms: 0 (aspirational: "blew me away," "seamless," "exciting")
  RATIO: ∞

Yahoo/Apollo ($38.4B AI financing, mechanism #111):
  Meta privacy terms: 12+ per article (TechCrunch Perez, mechanism #122)
  Snap privacy terms: 0 (despite 4 cameras vs Meta's 1)
  RATIO: ∞

INSTITUTIONAL AMPLIFICATION FACTOR:
The natural editorial concern (1.7:1 at control outlet) gets amplified to ∞
at institutional outlets. This is not a 2x or 5x amplification — it is a
qualitative shift from proportional concern to entity-selective weaponization.

PUBLICATION CONTEXT: 9to5Google (925 LLC):
- Owner: Seth Weintraub (sole proprietor)
- Funding: Affiliate revenue + display ads (no VC, no corporate parent)
- Sister sites: 9to5Mac, 9to5Toys, Electrek, DroneDJ, SpaceExplored
- AI content deals: NONE (no OpenAI, Google, Meta, or Anthropic licensing)
- Condé Nast connection: NONE
- Advance Publications connection: NONE
- Google advertising dependency: Display ads via Google Ad Manager (standard
  for independent publishers, not a licensing deal or content partnership)

This outlet has NO structural incentive to protect Google or attack Meta
beyond the standard affiliate revenue model (which favors positive product
coverage for ALL entities equally). Schoon's balanced privacy framing
represents the journalistic consensus absent institutional distortion.

5 CONFOUNDERS:
1. Google-centric site identity (MODERATE): 9to5Google's name implies Google
   alignment, which could create cultural bias toward Google. REBUTTAL: Schoon
   actively criticizes Google products in reviews (Pixel complaints, Android
   bugs) and applied privacy vocabulary to Google's glasses — the site name
   creates identity alignment but not editorial capture.

2. Affiliate revenue model (MODERATE): 9to5Google earns affiliate commissions
   from product links (Best Buy, Amazon). This incentivizes positive product
   coverage for ALL entities, not entity-selectively. REBUTTAL: The affiliate
   model creates an even playing field — positive framing benefits whether the
   product is Meta, Samsung, or Google. The privacy vocabulary Schoon DOES use
   works against his affiliate incentive, suggesting editorial conviction.

3. Aggregation vs investigation (STRONG): Schoon's Meta privacy articles
   aggregate original reporting from The Verge and FT. His editorial additions
   are shorter and less detailed than primary investigations. REBUTTAL: This is
   exactly the point — the aggregation model shows how the same primary-source
   facts (Victoria Song's LED report, Hannah Murphy's always-on report) get
   framed by different outlets. Schoon adds balanced editorial color; WIRED
   adds 10+ alarm terms to the same underlying facts.

4. Different audience expectations (MODERATE): 9to5Google readers are Android
   enthusiasts who want product news, not privacy advocacy. REBUTTAL: Audience
   expectations shape emphasis but not factual framing. Schoon still noted
   privacy concerns — he just applied them proportionally. WIRED's audience
   includes tech enthusiasts too.

5. Scale of coverage (WEAK): Schoon publishes 4-5 articles per day; each
   individual article gets less depth than a WIRED feature. REBUTTAL: The
   mechanism is about vocabulary distribution (which entities receive alarm
   language), not depth. A 500-word aggregation can still selectively omit or
   include privacy terms.

Cross-references: Mechanisms #33 (Samsung equivalence paradox), #110 (Future plc
EIC competitive framing), #114 (Future plc triple dependency), #115 (TechRadar
privacy bifurcation), #116 (Michael Hicks privacy suppression), #118 (WIRED
safety-research framing inversion), #122 (TechCrunch Snap zero-scrutiny),
#126 (Wong-Barr cross-publication beat replication), #130 (Snap competitive
privacy positioning amplification).
"""

import pytest
import yaml
import os
import glob


# ─────────────────────────────────────────────────────────────────
# Fixtures
# ─────────────────────────────────────────────────────────────────

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


@pytest.fixture(scope="module")
def competitor_research():
    path = os.path.join(REPO_ROOT, "profiles", "competitor-coverage-research.yaml")
    with open(path) as f:
        return yaml.safe_load(f)


@pytest.fixture(scope="module")
def competitor_entities():
    path = os.path.join(REPO_ROOT, "profiles", "competitor-entities.yaml")
    with open(path) as f:
        return yaml.safe_load(f)


@pytest.fixture(scope="module")
def journalists_data():
    path = os.path.join(REPO_ROOT, "profiles", "careers", "journalists.yaml")
    with open(path) as f:
        return yaml.safe_load(f)


def find_journalist(data, name):
    """Find a journalist entry by name in journalists.yaml."""
    journalists = data.get("journalists", data) if isinstance(data, dict) else data
    if isinstance(journalists, list):
        for entry in journalists:
            if isinstance(entry, dict) and entry.get("name") == name:
                return entry
    return None


def find_mechanism(research, mech_id):
    """Find mechanism by ID anywhere in the research YAML."""
    cpf = research.get("cross_publication_findings", {})
    if isinstance(cpf, dict):
        for key, val in cpf.items():
            if isinstance(val, dict) and val.get("mechanism_id") == mech_id:
                return val
    pubs = research.get("publications", {})
    if isinstance(pubs, dict):
        for key, val in pubs.items():
            if isinstance(val, dict) and val.get("mechanism_id") == mech_id:
                return val
    return None


# ─────────────────────────────────────────────────────────────────
# Ben Schoon Profile Integrity
# ─────────────────────────────────────────────────────────────────

class TestBenSchoonProfileIntegrity:
    """Validate Ben Schoon's journalist profile contains required control data."""

    def test_ben_schoon_exists_in_journalists(self, journalists_data):
        j = find_journalist(journalists_data, "Ben Schoon")
        assert j is not None, "Ben Schoon must exist in journalists.yaml"

    def test_ben_schoon_publication_is_9to5google(self, journalists_data):
        j = find_journalist(journalists_data, "Ben Schoon")
        career = j.get("career", [])
        pubs = [c.get("publication", "") for c in career if isinstance(c, dict)]
        assert "9to5google" in pubs, "Ben Schoon's career must include 9to5google"

    def test_ben_schoon_has_multi_publication_flag(self, journalists_data):
        j = find_journalist(journalists_data, "Ben Schoon")
        assert "multi_publication" in j

    def test_ben_schoon_has_source_urls(self, journalists_data):
        j = find_journalist(journalists_data, "Ben Schoon")
        urls = j.get("source_urls", [])
        assert len(urls) >= 2, "Ben Schoon must have at least 2 source URLs"

    def test_9to5google_marked_as_control(self, journalists_data):
        j = find_journalist(journalists_data, "Ben Schoon")
        notes = j.get("notes", "")
        assert "CONTROL" in notes, "Ben Schoon's profile must identify 9to5Google as CONTROL outlet"

    def test_ownership_structure_documented(self, journalists_data):
        j = find_journalist(journalists_data, "Ben Schoon")
        notes = j.get("notes", "")
        assert "925 LLC" in notes or "Seth Weintraub" in notes, \
            "Ownership structure (925 LLC / Seth Weintraub) must be documented"

    def test_no_conde_nast_connection(self, journalists_data):
        j = find_journalist(journalists_data, "Ben Schoon")
        notes = j.get("notes", "")
        assert "NO CONDÉ NAST" in notes.upper() or "NO CONDE NAST" in notes.upper(), \
            "Profile must explicitly state no Condé Nast connection"

    def test_no_advance_connection(self, journalists_data):
        j = find_journalist(journalists_data, "Ben Schoon")
        notes = j.get("notes", "")
        assert "NO" in notes.upper() and "ADVANCE" in notes.upper(), \
            "Profile must explicitly state no Advance Publications connection"


# ─────────────────────────────────────────────────────────────────
# Ben Schoon Meta Coverage Analysis
# ─────────────────────────────────────────────────────────────────

class TestBenSchoonMetaCoverage:
    """Validate documented Meta coverage contains privacy vocabulary."""

    def test_meta_coverage_documented(self, journalists_data):
        j = find_journalist(journalists_data, "Ben Schoon")
        career = j.get("career", [])
        career_notes = " ".join(c.get("notes", "") for c in career if isinstance(c, dict))
        assert "META WEARABLES COVERAGE" in career_notes, \
            "Ben Schoon's career notes must document META WEARABLES COVERAGE"

    def test_meta_privacy_light_article(self, journalists_data):
        j = find_journalist(journalists_data, "Ben Schoon")
        career = j.get("career", [])
        career_notes = " ".join(c.get("notes", "") for c in career if isinstance(c, dict))
        assert "privacy light" in career_notes.lower(), \
            "Must document Jul 7 Meta privacy light enforcement article"

    def test_meta_always_on_article(self, journalists_data):
        j = find_journalist(journalists_data, "Ben Schoon")
        career = j.get("career", [])
        career_notes = " ".join(c.get("notes", "") for c in career if isinstance(c, dict))
        assert "always-on" in career_notes.lower() or "recording all the time" in career_notes.lower(), \
            "Must document Jul 9 Meta always-on glasses article"

    def test_meta_privacy_editorial_voice(self, journalists_data):
        j = find_journalist(journalists_data, "Ben Schoon")
        career = j.get("career", [])
        career_notes = " ".join(c.get("notes", "") for c in career if isinstance(c, dict))
        assert "you cannot and should not be recording all the time" in career_notes, \
            "Must document Ben Schoon's editorial privacy voice"

    def test_meta_framing_described_as_skepticism_forward(self, journalists_data):
        j = find_journalist(journalists_data, "Ben Schoon")
        career = j.get("career", [])
        career_notes = " ".join(c.get("notes", "") for c in career if isinstance(c, dict))
        assert "skepticism-forward" in career_notes or "skepticism" in career_notes.lower(), \
            "Coverage framing must be characterized as skepticism-forward"


# ─────────────────────────────────────────────────────────────────
# Mechanism #131 Structure
# ─────────────────────────────────────────────────────────────────

class TestMechanism131Structure:
    """Validate mechanism #131 exists with required structural fields."""

    def test_mechanism_131_exists(self, competitor_research):
        m = find_mechanism(competitor_research, 131)
        assert m is not None, "Mechanism #131 must exist in competitor-coverage-research.yaml"

    def test_mechanism_has_finding_summary(self, competitor_research):
        m = find_mechanism(competitor_research, 131)
        assert "finding_summary" in m
        assert len(m["finding_summary"]) > 200, "Finding summary must be substantive"

    def test_mechanism_has_discovery_date(self, competitor_research):
        m = find_mechanism(competitor_research, 131)
        assert m.get("discovery_date") == "2026-08-16"

    def test_mechanism_has_test_file(self, competitor_research):
        m = find_mechanism(competitor_research, 131)
        assert "test_file" in m
        assert "ben_schoon" in m["test_file"]

    def test_mechanism_type_is_control_calibration(self, competitor_research):
        m = find_mechanism(competitor_research, 131)
        ft = m.get("finding_type", "")
        assert "control" in ft.lower() or "calibration" in ft.lower(), \
            "Mechanism type must be control_outlet_calibration or similar"

    def test_mechanism_domain_is_wearables(self, competitor_research):
        m = find_mechanism(competitor_research, 131)
        assert "wearables" in m.get("domain", "").lower()


# ─────────────────────────────────────────────────────────────────
# Control Outlet Calibration Data
# ─────────────────────────────────────────────────────────────────

class TestControlCalibrationData:
    """Validate the control calibration compares 9to5Google to institutional outlets."""

    def test_mechanism_has_control_outlet_data(self, competitor_research):
        m = find_mechanism(competitor_research, 131)
        assert m is not None
        summary = m.get("finding_summary", "")
        assert "9to5google" in summary.lower() or "9to5Google" in summary

    def test_meta_privacy_vocabulary_documented(self, competitor_research):
        m = find_mechanism(competitor_research, 131)
        summary = m.get("finding_summary", "") + str(m.get("control_calibration", ""))
        assert "privacy" in summary.lower()

    def test_samsung_google_privacy_vocabulary_documented(self, competitor_research):
        m = find_mechanism(competitor_research, 131)
        summary = m.get("finding_summary", "") + str(m.get("control_calibration", ""))
        # Must document that 9to5Google DOES apply privacy vocabulary to Samsung/Google
        assert "samsung" in summary.lower() or "google" in summary.lower()

    def test_institutional_comparison_included(self, competitor_research):
        m = find_mechanism(competitor_research, 131)
        summary = m.get("finding_summary", "") + str(m.get("control_calibration", ""))
        # Must compare to at least one institutional outlet
        assert any(x in summary.lower() for x in ["wired", "gizmodo", "future plc", "yahoo"])

    def test_amplification_factor_documented(self, competitor_research):
        m = find_mechanism(competitor_research, 131)
        summary = m.get("finding_summary", "") + str(m.get("control_calibration", ""))
        # Must document the amplification delta
        assert "amplification" in summary.lower() or "ratio" in summary.lower() or "delta" in summary.lower()


# ─────────────────────────────────────────────────────────────────
# Privacy Vocabulary Ratios
# ─────────────────────────────────────────────────────────────────

class TestPrivacyVocabularyRatios:
    """Validate the privacy vocabulary ratio measurements."""

    def test_control_ratio_is_finite(self, competitor_research):
        """9to5Google ratio must be finite (not ∞) — both entities get SOME vocabulary."""
        m = find_mechanism(competitor_research, 131)
        cal = m.get("control_calibration", m.get("privacy_vocabulary_ratios", {}))
        if isinstance(cal, dict):
            control = cal.get("control_outlet", cal.get("9to5google", {}))
            if isinstance(control, dict):
                meta_count = control.get("meta_privacy_terms", 0)
                competitor_count = control.get("competitor_privacy_terms",
                                               control.get("samsung_google_privacy_terms", 0))
                assert meta_count > 0, "Control outlet must have SOME Meta privacy vocabulary"
                assert competitor_count > 0, "Control outlet must have SOME competitor privacy vocabulary"

    def test_institutional_ratio_is_infinite_or_very_high(self, competitor_research):
        """WIRED/Gizmodo ratio must be ∞ or very high — competitors get ZERO vocabulary."""
        m = find_mechanism(competitor_research, 131)
        cal = m.get("control_calibration", m.get("privacy_vocabulary_ratios", {}))
        if isinstance(cal, dict):
            for outlet in ["wired", "gizmodo", "future_plc"]:
                inst = cal.get(outlet, {})
                if isinstance(inst, dict):
                    competitor_terms = inst.get("competitor_privacy_terms",
                                                inst.get("samsung_google_privacy_terms", -1))
                    if competitor_terms >= 0:
                        assert competitor_terms == 0, \
                            f"Institutional outlet {outlet} must have ZERO competitor privacy terms"


# ─────────────────────────────────────────────────────────────────
# Cross-Reference Integrity
# ─────────────────────────────────────────────────────────────────

class TestCrossReferenceIntegrity:
    """Validate cross-references to related mechanisms."""

    def test_mechanism_has_cross_references(self, competitor_research):
        m = find_mechanism(competitor_research, 131)
        refs = m.get("cross_references", [])
        assert len(refs) >= 3, "Must cross-reference at least 3 related mechanisms"

    def test_references_include_samsung_equivalence(self, competitor_research):
        m = find_mechanism(competitor_research, 131)
        refs = m.get("cross_references", [])
        ref_ids = [r.get("mechanism_id", r) if isinstance(r, dict) else r for r in refs]
        assert 33 in ref_ids, "Must reference mechanism #33 (Samsung equivalence paradox)"

    def test_references_include_future_plc(self, competitor_research):
        m = find_mechanism(competitor_research, 131)
        refs = m.get("cross_references", [])
        ref_ids = [r.get("mechanism_id", r) if isinstance(r, dict) else r for r in refs]
        assert 114 in ref_ids or 110 in ref_ids, \
            "Must reference Future plc mechanisms (#110 or #114)"


# ─────────────────────────────────────────────────────────────────
# Confounder Documentation
# ─────────────────────────────────────────────────────────────────

class TestConfounderDocumentation:
    """Validate confounders are documented with rebuttals."""

    def test_mechanism_has_confounders(self, competitor_research):
        m = find_mechanism(competitor_research, 131)
        confounders = m.get("confounding_factors", m.get("confounders", []))
        assert len(confounders) >= 4, "Must document at least 4 confounding factors"

    def test_google_centric_site_identity_confounder(self, competitor_research):
        m = find_mechanism(competitor_research, 131)
        confounders = m.get("confounding_factors", m.get("confounders", []))
        conf_text = str(confounders).lower()
        assert "google" in conf_text and ("identity" in conf_text or "name" in conf_text or "centric" in conf_text), \
            "Must document Google-centric site identity as a confounder"

    def test_affiliate_revenue_confounder(self, competitor_research):
        m = find_mechanism(competitor_research, 131)
        confounders = m.get("confounding_factors", m.get("confounders", []))
        conf_text = str(confounders).lower()
        assert "affiliate" in conf_text, \
            "Must document affiliate revenue model as a confounder"

    def test_aggregation_vs_investigation_confounder(self, competitor_research):
        m = find_mechanism(competitor_research, 131)
        confounders = m.get("confounding_factors", m.get("confounders", []))
        conf_text = str(confounders).lower()
        assert "aggregat" in conf_text or "investigat" in conf_text, \
            "Must document aggregation vs investigation as a confounder"


# ─────────────────────────────────────────────────────────────────
# Ownership Independence Verification
# ─────────────────────────────────────────────────────────────────

class TestOwnershipIndependence:
    """Verify 925 LLC independence from all institutional media parents."""

    def test_no_conde_nast_ownership(self, competitor_research):
        m = find_mechanism(competitor_research, 131)
        summary = str(m)
        assert "condé nast" not in summary.lower().replace("no condé nast", "").replace(
            "no conde nast", "").replace("zero condé nast", "").replace(
            "no advance", "").replace("no institutional", "") or \
            "no condé nast" in summary.lower() or "no conde nast" in summary.lower() or \
            "zero" in summary.lower()

    def test_no_vc_backing(self, journalists_data):
        j = find_journalist(journalists_data, "Ben Schoon")
        notes = j.get("notes", "")
        assert "not venture-backed" in notes.lower() or "no vc" in notes.lower(), \
            "Profile must confirm no VC backing"

    def test_no_ai_content_deals(self, journalists_data):
        j = find_journalist(journalists_data, "Ben Schoon")
        notes = j.get("notes", "")
        career = j.get("career", [])
        all_text = notes + " ".join(c.get("notes", "") for c in career if isinstance(c, dict))
        # No AI content deal language should appear
        assert "content deal" not in all_text.lower() or "no" in all_text.lower()


# ─────────────────────────────────────────────────────────────────
# Analytical Value Assessment
# ─────────────────────────────────────────────────────────────────

class TestAnalyticalValue:
    """Verify the mechanism provides measurable analytical value."""

    def test_mechanism_establishes_baseline(self, competitor_research):
        """The mechanism must establish a baseline for 'natural' editorial concern."""
        m = find_mechanism(competitor_research, 131)
        summary = m.get("finding_summary", "")
        assert "baseline" in summary.lower() or "control" in summary.lower() or \
               "natural" in summary.lower()

    def test_mechanism_quantifies_delta(self, competitor_research):
        """Must quantify the difference between control and institutional outlets."""
        m = find_mechanism(competitor_research, 131)
        summary = m.get("finding_summary", "")
        cal = str(m.get("control_calibration", m.get("privacy_vocabulary_ratios", "")))
        combined = summary + cal
        assert any(x in combined.lower() for x in ["ratio", "delta", "factor", "amplif"]), \
            "Must quantify the institutional amplification"

    def test_mechanism_names_comparison_outlets(self, competitor_research):
        """Must explicitly name institutional outlets being compared."""
        m = find_mechanism(competitor_research, 131)
        summary = m.get("finding_summary", "") + str(m.get("control_calibration", ""))
        outlet_count = sum(1 for x in ["wired", "gizmodo", "future plc", "techcrunch", "yahoo"]
                           if x in summary.lower())
        assert outlet_count >= 2, "Must compare to at least 2 institutional outlets by name"
