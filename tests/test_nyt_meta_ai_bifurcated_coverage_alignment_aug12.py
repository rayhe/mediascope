"""
Mechanism #69: NYT Meta AI Coverage Bifurcation — Open-Source Philosophy (Positive)
vs Execution Performance (Adversarial), Aligned with Litigation Interests

KEY FINDING: The NYT — the only publication in the MediaScope dataset simultaneously
suing a tech company (OpenAI) while covering that company's products — produces a
BIFURCATED coverage pattern for Meta's AI that correlates with litigation interests:

(1) Meta's OPEN-SOURCE AI PHILOSOPHY receives POSITIVE framing:
    - "How A.I. Made Mark Zuckerberg Popular Again" (May 2024, Cade Metz/Mike Isaac)
    - "Zuckaissance," "champion," "genuinely good for the open-source community"
    - Article includes NYT lawsuit disclosure — editorial aware of conflict
    - SERVES LITIGATION: Open-source undermines OpenAI's closed model, which is
      the company the NYT is suing

(2) Meta's AI EXECUTION AND PERFORMANCE receives ADVERSARIAL framing:
    - "Avocado" model delay (Mar 2026): "trailing," "failed to match," "scrambles"
    - "Zuckerberg Again Overhauls Meta's AI Efforts" (Aug 2025): "tensions surfaced,"
      "personnel churn," "disappointing performance tests," "Behemoth abandoned"
    - Llama 4 "met with poor reception" — repeated across multiple articles
    - NEUTRAL TO LITIGATION: Meta's model quality has no bearing on OpenAI case

(3) Meta's SOCIAL PLATFORM receives ADVERSARIAL framing:
    - Children's safety trials ($1B+ verdicts), layoffs, Muse Image backlash
    - Covered by Mike Isaac, Sheera Frenkel (adversarial beat reporters)
    - NEUTRAL TO LITIGATION: Social platform issues unrelated to AI copyright

STRUCTURAL INSIGHT:
The NYT is the ONLY publication with a NEGATIVE financial relationship (lawsuit)
with a tech company. The coverage bifurcation test: if the NYT covers Meta's
open-source AI positively BECAUSE it undermines OpenAI (their litigation target),
this creates a LITIGATION-ALIGNED coverage pattern that parallels deal-aligned
patterns at other publications.

ASYMMETRIC FIREWALL HYPOTHESIS:
- Corporate litigation → Editorial: Firewall WORKS one-way. Despite suing OpenAI,
  NYT covers OpenAI products aspirationally (Metz: GPT-5.6 Sol "most powerful")
- Financial deals → Editorial: Firewall FAILS. At WIRED, Conde Nast's OpenAI deal
  correlates with softer coverage. At FT, OpenAI deal correlates with aspirational
  Anthropic framing.
- IMPLICATION: Editorial independence protects companies from ADVERSARIAL corporate
  relationships but does NOT protect against FAVORABLE corporate relationships
  (deals). The wall is one-directional.

CONFOUNDING FACTORS:
1. STRONG: Positive open-source coverage may reflect genuine editorial stance, not
   litigation strategy. The NYT editorial board may simply believe open-source is good.
2. MODERATE: Avocado/Behemoth delays ARE legitimately newsworthy negative events —
   adversarial framing may be warranted by facts.
3. MODERATE: Different reporters cover different topics — Metz covers AI industry broadly,
   Isaac covers Meta specifically. Topic assignment, not litigation strategy, may
   drive the bifurcation.
4. WEAK: The open-source article includes the lawsuit disclosure, suggesting editorial
   awareness of the conflict — but disclosure ≠ bias correction.
5. MODERATE: Other publications also cover Meta open-source more positively than Meta
   execution failures — this may be a universal pattern, not NYT-specific.
6. STRONG: Meta's open-source pivot was genuinely popular with developers — positive
   coverage reflects real sentiment, not manufactured narrative.
7. WEAK: The NYT-OpenAI lawsuit is handled by the legal department, and editorial
   decisions are made independently — no evidence of coordination.

TESTABLE PREDICTIONS:
1. If the NYT settles with OpenAI, positive Meta open-source coverage should DECREASE
   (no longer serves litigation narrative). If it persists, editorial stance explanation
   strengthened.
2. If Meta closes its next frontier model (moves away from open-source), NYT coverage
   of Meta AI should become uniformly adversarial — removing the one positive angle.
3. If another publication SUES OpenAI (e.g., CNN), that publication should develop
   similar bifurcated Meta AI coverage (positive on open-source, adversarial on execution).
4. NYT should cover OpenAI's open-source moves (if any) LESS positively than Meta's —
   because OpenAI doing open-source doesn't serve the "OpenAI is a copyright thief"
   narrative.

CROSS-REFERENCES:
- Mechanism #23: NYT Anthropic Triple-Chain Incentive (financial alignment)
- Mechanism #51: WIRED Copyright Piracy Framing Parity (Meta vs Anthropic piracy framing)
- Mechanism #57: Seetharaman Frame-Lock (professional identity overrides institutions)
- Mechanism #37: Open-Weight Policy Coverage Selection Asymmetry (coverage selection)

Sources:
- NYT "How A.I. Made Mark Zuckerberg Popular Again" (May 29, 2024):
  https://web.archive.org/web/20240529/https://www.nytimes.com/2024/05/29/technology/mark-zuckerberg-meta-ai-open-source.html
- NYT "Zuckerberg Again Overhauls Meta's A.I. Efforts" (Aug 19, 2025):
  https://web.archive.org/web/20250823090419/https://www.nytimes.com/2025/08/19/technology/mark-zuckerberg-meta-ai.html
- NYT "Meta Avocado Delay" reporting (Mar 12, 2026):
  https://www.pymnts.com/news/artificial-intelligence/2026/meta-avocado-delay-puts-135-billion-dollar-ai-bet-under-scrutiny/
- Reuters "Meta plans RL cuts, NYT reports" (Jan 12, 2026):
  https://www.reuters.com/business/meta-plans-cut-around-10-employees-reality-labs-division-nyt-reports-2026-01-12/
- Reuters "US presses Meta on AI reviews, NYT reports" (Jun 23, 2026):
  https://www.reuters.com/world/us/us-presses-meta-agree-ai-reviews-security-concerns-rise-nyt-reports-2026-06-23/
- Muck Rack Cade Metz portfolio: https://muckrack.com/cademetz/articles
- TechCrunch "NYT says OpenAI hid evidence" (Jul 9, 2026):
  https://techcrunch.com/2026/07/09/new-york-times-says-openai-hid-evidence-in-chatgpt-copyright-trial/
- Reuters "NYT sanctions motion" (Jul 9, 2026):
  https://www.reuters.com/legal/litigation/new-york-times-led-group-asks-court-sanction-openai-us-copyright-dispute-2026-07-09/
- Engadget "Is Zuckerberg flip-flopping on open source?" (Jul 2026):
  https://www.engadget.com/ai/is-mark-zuckerberg-flip-flopping-on-open-source-ai-231310567.html
"""

import yaml
import pathlib
import re

PROFILES = pathlib.Path(__file__).resolve().parent.parent / "profiles"


def _load_yaml(name: str) -> dict:
    with open(PROFILES / name, encoding="utf-8") as f:
        return yaml.safe_load(f)


def _get_mechanism():
    data = _load_yaml("competitor-coverage-research.yaml")
    cpf = data.get("cross_publication_findings", {})
    for key, val in cpf.items():
        if isinstance(val, dict) and val.get("mechanism_id") == 69:
            return val
    return None


# ===================================================================
# 1. Mechanism exists and has required fields
# ===================================================================

class TestMechanism69Exists:
    """Mechanism #69 is in cross_publication_findings with required fields."""

    @classmethod
    def setup_class(cls):
        cls.mech = _get_mechanism()

    def test_mechanism_exists(self):
        assert self.mech is not None, "Mechanism #69 should exist in cross_publication_findings"

    def test_has_mechanism_id(self):
        assert self.mech.get("mechanism_id") == 69

    def test_has_name(self):
        name = self.mech.get("name", "")
        assert len(name) > 20, f"Name should be descriptive, got: {name}"

    def test_has_finding_summary(self):
        summary = self.mech.get("finding_summary", "")
        assert len(summary) > 200, f"Finding summary should be substantive, got {len(summary)} chars"

    def test_has_discovery_date(self):
        assert self.mech.get("discovery_date") is not None

    def test_has_date_added(self):
        assert self.mech.get("date_added") is not None

    def test_has_publication(self):
        assert self.mech.get("publication") == "nytimes"

    def test_has_source_urls(self):
        urls = self.mech.get("source_urls", [])
        assert len(urls) >= 5, f"Should have at least 5 source URLs, got {len(urls)}"

    def test_has_test_file(self):
        tf = self.mech.get("test_file", "")
        assert "aug12" in tf.lower(), f"Test file should reference aug12, got: {tf}"


# ===================================================================
# 2. Bifurcation structure documented
# ===================================================================

class TestBifurcationStructure:
    """The mechanism documents the three-way coverage bifurcation."""

    @classmethod
    def setup_class(cls):
        cls.mech = _get_mechanism()

    def test_references_open_source_positive(self):
        summary = self.mech.get("finding_summary", "")
        assert "open" in summary.lower() and ("positive" in summary.lower() or "aspirational" in summary.lower()), \
            "Should reference positive open-source coverage"

    def test_references_execution_adversarial(self):
        summary = self.mech.get("finding_summary", "")
        assert "adversarial" in summary.lower() or "negative" in summary.lower(), \
            "Should reference adversarial execution coverage"

    def test_references_litigation(self):
        summary = self.mech.get("finding_summary", "")
        assert "litigation" in summary.lower() or "lawsuit" in summary.lower() or "suing" in summary.lower(), \
            "Should reference NYT-OpenAI litigation"

    def test_references_bifurcation_or_dual(self):
        summary = self.mech.get("finding_summary", "")
        assert any(term in summary.lower() for term in ["bifurcate", "dual", "split", "two track", "two-track"]), \
            "Should reference the bifurcated/dual-track coverage pattern"


# ===================================================================
# 3. Confounding factors properly documented
# ===================================================================

class TestConfoundingFactors:
    """Mechanism #69 has properly structured confounding factors."""

    @classmethod
    def setup_class(cls):
        cls.mech = _get_mechanism()

    def test_has_confounding_factors(self):
        cf = self.mech.get("confounding_factors", [])
        assert len(cf) >= 5, f"Should have at least 5 confounding factors, got {len(cf)}"

    def test_factors_have_descriptions(self):
        cf = self.mech.get("confounding_factors", [])
        for factor in cf:
            if isinstance(factor, dict):
                desc = factor.get("description", "")
                assert len(desc) > 20, f"Confounding factor description too short: {desc}"
            elif isinstance(factor, str):
                assert len(factor) > 20, f"Confounding factor too short: {factor}"

    def test_has_strong_factor(self):
        """At least one confounding factor should be rated STRONG."""
        cf = self.mech.get("confounding_factors", [])
        has_strong = False
        for factor in cf:
            if isinstance(factor, dict):
                strength = factor.get("strength", "")
                if "STRONG" in str(strength).upper():
                    has_strong = True
            elif isinstance(factor, str) and "STRONG" in factor.upper():
                has_strong = True
        assert has_strong, "Should have at least one STRONG confounding factor"


# ===================================================================
# 4. Testable predictions
# ===================================================================

class TestTestablePredictions:
    """Mechanism #69 has falsifiable predictions."""

    @classmethod
    def setup_class(cls):
        cls.mech = _get_mechanism()

    def test_has_predictions(self):
        predictions = self.mech.get("testable_predictions", [])
        assert len(predictions) >= 3, f"Should have at least 3 predictions, got {len(predictions)}"

    def test_predictions_are_substantive(self):
        predictions = self.mech.get("testable_predictions", [])
        for pred in predictions:
            text = pred if isinstance(pred, str) else pred.get("prediction", "")
            assert len(text) > 30, f"Prediction too short: {text}"


# ===================================================================
# 5. Cross-references valid
# ===================================================================

class TestCrossReferences:
    """Mechanism #69 cross-references related mechanisms."""

    @classmethod
    def setup_class(cls):
        cls.mech = _get_mechanism()

    def test_has_cross_references(self):
        xrefs = self.mech.get("cross_references", [])
        assert len(xrefs) >= 3, f"Should have at least 3 cross-references, got {len(xrefs)}"

    def test_references_nyt_anthropic(self):
        """Should cross-reference #23 (NYT Anthropic triple-chain)."""
        xrefs = self.mech.get("cross_references", [])
        has_23 = any(
            (isinstance(x, dict) and x.get("mechanism_id") == 23)
            or (isinstance(x, str) and "23" in x)
            for x in xrefs
        )
        assert has_23, "Should cross-reference mechanism #23 (NYT Anthropic)"

    def test_references_copyright_piracy(self):
        """Should cross-reference #51 (WIRED copyright piracy framing)."""
        xrefs = self.mech.get("cross_references", [])
        has_51 = any(
            (isinstance(x, dict) and x.get("mechanism_id") == 51)
            or (isinstance(x, str) and "51" in x)
            for x in xrefs
        )
        assert has_51, "Should cross-reference mechanism #51 (copyright piracy)"

    def test_references_open_weight(self):
        """Should cross-reference #37 (open-weight policy coverage)."""
        xrefs = self.mech.get("cross_references", [])
        has_37 = any(
            (isinstance(x, dict) and x.get("mechanism_id") == 37)
            or (isinstance(x, str) and "37" in x)
            for x in xrefs
        )
        assert has_37, "Should cross-reference mechanism #37 (open-weight policy)"


# ===================================================================
# 6. Evidence articles documented
# ===================================================================

class TestEvidenceArticles:
    """Specific articles cited as evidence."""

    @classmethod
    def setup_class(cls):
        cls.mech = _get_mechanism()

    def test_positive_open_source_evidence(self):
        """Should cite the 'Zuckaissance' article as positive evidence."""
        summary = self.mech.get("finding_summary", "")
        source_urls = self.mech.get("source_urls", [])
        combined = summary + " ".join(str(u) for u in source_urls)
        assert any(term in combined.lower() for term in ["popular again", "zuckaissance", "open source"]), \
            "Should cite positive open-source coverage evidence"

    def test_adversarial_execution_evidence(self):
        """Should cite Avocado delay or Behemoth abandonment as adversarial evidence."""
        summary = self.mech.get("finding_summary", "")
        assert any(term in summary.lower() for term in ["avocado", "behemoth", "trailing", "delay"]), \
            "Should cite adversarial execution coverage evidence"

    def test_litigation_evidence(self):
        """Should cite the NYT-OpenAI lawsuit details."""
        summary = self.mech.get("finding_summary", "")
        assert any(term in summary.lower() for term in ["copyright", "sanction", "evidence"]), \
            "Should cite NYT-OpenAI litigation details"


# ===================================================================
# 7. Asymmetric firewall hypothesis
# ===================================================================

class TestAsymmetricFirewall:
    """The mechanism documents the one-way editorial firewall finding."""

    @classmethod
    def setup_class(cls):
        cls.mech = _get_mechanism()

    def test_firewall_hypothesis_documented(self):
        summary = self.mech.get("finding_summary", "")
        assert "firewall" in summary.lower() or "asymmetric" in summary.lower(), \
            "Should document the asymmetric firewall hypothesis"

    def test_contrasts_with_deal_publications(self):
        """Should contrast NYT (litigation) with deal publications (WIRED, FT)."""
        summary = self.mech.get("finding_summary", "")
        assert any(pub in summary for pub in ["WIRED", "FT", "Cond"]), \
            "Should contrast with deal-based publications"


# ===================================================================
# 8. NYT profile integration
# ===================================================================

class TestNYTProfileIntegration:
    """NYT profile should reference the bifurcated coverage mechanism."""

    @classmethod
    def setup_class(cls):
        cls.profile = _load_yaml("nytimes.yaml")

    def test_meta_ai_bifurcation_referenced(self):
        """NYT profile should have a reference to the meta AI bifurcation finding."""
        profile_str = str(self.profile)
        assert any(term in profile_str.lower() for term in [
            "bifurcate", "mechanism_69", "mechanism #69",
            "meta_ai_bifurcated", "_ref", "litigation_aligned"
        ]), "NYT profile should reference the bifurcated coverage mechanism"


# ===================================================================
# 9. Entity integration
# ===================================================================

class TestEntityIntegration:
    """OpenAI entity should reference NYT litigation alignment."""

    @classmethod
    def setup_class(cls):
        cls.entities = _load_yaml("competitor-entities.yaml")

    def test_openai_nyt_litigation_documented(self):
        """OpenAI entity should reference the NYT litigation."""
        openai = self.entities.get("entities", {}).get("openai", {})
        openai_str = str(openai)
        assert "NYT" in openai_str or "New York Times" in openai_str or "nytimes" in openai_str, \
            "OpenAI entity should reference NYT litigation"


# ===================================================================
# 10. Structural consistency with dataset
# ===================================================================

class TestStructuralConsistency:
    """Mechanism #69 integrates correctly with the broader dataset."""

    @classmethod
    def setup_class(cls):
        cls.research = _load_yaml("competitor-coverage-research.yaml")
        cls.cpf = cls.research.get("cross_publication_findings", {})

    def test_mechanism_69_in_cpf_not_publications(self):
        """#69 should be in cross_publication_findings, NOT publications."""
        pubs = self.research.get("publications", {})
        pubs_str = str(pubs)
        assert "mechanism_id: 69" not in pubs_str, \
            "Mechanism #69 should NOT be in publications section"

    def test_no_duplicate_mechanism_ids(self):
        """No duplicate mechanism IDs in cross_publication_findings."""
        ids = []
        for k, v in self.cpf.items():
            if isinstance(v, dict) and v.get("mechanism_id"):
                ids.append(v["mechanism_id"])
        assert len(ids) == len(set(ids)), f"Duplicate mechanism IDs found: {[x for x in ids if ids.count(x) > 1]}"

    def test_mechanism_69_is_max_or_near(self):
        """#69 should be the current max or near-max mechanism ID."""
        max_id = 0
        for k, v in self.cpf.items():
            if isinstance(v, dict):
                mid = v.get("mechanism_id", 0)
                if mid > max_id:
                    max_id = mid
        assert max_id >= 69, f"Max mechanism ID should be >= 69, got {max_id}"

    def test_mechanism_count_reasonable(self):
        """Should have 50+ mechanisms in cross_publication_findings."""
        count = sum(1 for k, v in self.cpf.items() if isinstance(v, dict) and v.get("mechanism_id"))
        assert count >= 50, f"Should have 50+ mechanisms, got {count}"
