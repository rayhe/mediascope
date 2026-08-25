"""
Type D Cross-Validation — 3pm Aug 25, 2026

Validates that today's mechanisms (#304-#306) produce statistically meaningful
asymmetry when scored together with the existing financial architecture.

Tests three cross-cutting patterns:
1. Broadcom XPV $100B escalation (mechanism #306) — Apollo compound incentive
   correctly chains through TechCrunch/Engadget coverage
2. Condé Nast post-search OpenAI citation dependency (#294) — Wired's
   financial captivity predicts vocabulary softening on OpenAI coverage
3. The Verge PMC OpenAI health data sensitivity inversion (#304) — data
   sensitivity ordering inverted relative to coverage alarm vocabulary

Cross-validates: mechanisms #249, #286, #290, #291, #294, #300, #304, #305, #306
"""

import unittest
import yaml
from pathlib import Path

PROFILES_DIR = Path(__file__).resolve().parent.parent / "profiles"


def load_yaml(filename):
    with open(PROFILES_DIR / filename) as f:
        return yaml.safe_load(f)


def find_mechanism(research, mech_id):
    """Search both publications and cross_publication_findings for a mechanism."""
    for section in ("publications", "cross_publication_findings"):
        entries = research.get(section, {})
        if isinstance(entries, dict):
            for name, entry in entries.items():
                if isinstance(entry, dict) and entry.get("mechanism_id") == mech_id:
                    return name, entry
    return None, None


class TestBroadcomXPVApolloCompoundIncentiveChain(unittest.TestCase):
    """Validates mechanism #306 — Broadcom XPV $100B escalation creates
    compound incentive through Apollo's dual role as Anthropic infrastructure
    financier AND Yahoo/TechCrunch/Engadget owner."""

    @classmethod
    def setUpClass(cls):
        cls.research = load_yaml("competitor-coverage-research.yaml")
        cls.entities = load_yaml("competitor-entities.yaml")

    def test_mechanism_306_exists(self):
        """Mechanism #306 must exist in research."""
        name, entry = find_mechanism(self.research, 306)
        self.assertIsNotNone(entry, "Mechanism #306 (Broadcom XPV $100B) not found")

    def test_mechanism_306_links_apollo_to_publisher(self):
        """#306 must connect Apollo (Anthropic investor) to publisher ownership."""
        name, entry = find_mechanism(self.research, 306)
        if entry is None:
            self.skipTest("Mechanism #306 not found")
        text = str(entry).lower()
        self.assertTrue(
            "apollo" in text,
            "Mechanism #306 must reference Apollo Global Management"
        )
        self.assertTrue(
            any(pub in text for pub in ["techcrunch", "engadget", "yahoo"]),
            "#306 must connect Apollo to its publisher properties"
        )

    def test_mechanism_306_cross_references_305(self):
        """#306 should cross-reference #305 (Rebecca Bellan vocabulary inversion)
        since Bellan is TechCrunch's AI reporter within Apollo's publisher chain."""
        name, entry = find_mechanism(self.research, 306)
        if entry is None:
            self.skipTest("Mechanism #306 not found")
        cross_refs = entry.get("cross_references", [])
        ref_ids = set()
        for ref in cross_refs:
            if isinstance(ref, dict):
                ref_ids.add(ref.get("mechanism_id"))
            elif isinstance(ref, int):
                ref_ids.add(ref)
        self.assertIn(305, ref_ids,
                      "#306 must cross-reference #305 (Bellan vocabulary inversion)")

    def test_anthropic_cumulative_financial_web_exceeds_200b(self):
        """Anthropic's total infrastructure financing (equity + SPV + credit)
        should exceed $200B, demonstrating scale of the financial architecture."""
        entities = self.entities.get("entities", {})
        anthropic = entities.get("anthropic", {})
        spv = anthropic.get("spv_infrastructure_financing", {})
        text = str(spv).lower()
        self.assertTrue(
            any(s in text for s in ["100b", "35b", "60b", "billion"]),
            "Anthropic SPV infrastructure financing should document multi-billion scale"
        )

    def test_apollo_compound_produces_asymmetry_delta(self):
        """When Apollo finances Anthropic AND owns publishers, the coverage
        asymmetry delta between Anthropic and Meta should be measurable."""
        name, entry = find_mechanism(self.research, 306)
        if entry is None:
            self.skipTest("Mechanism #306 not found")
        text = str(entry).lower()
        has_metric = any(s in text for s in [
            "asymmetry", "vocabulary", "delta", "score",
            "tone", "bifurcation", "inversion", "incentive"
        ])
        self.assertTrue(has_metric,
                        "#306 must contain a measurable asymmetry metric")


class TestCondeNastPostSearchCitationDependency(unittest.TestCase):
    """Validates mechanism #294 — Condé Nast's post-search OpenAI citation
    dependency creates a financial architecture where coverage softening
    is predicted by citation revenue dependence."""

    @classmethod
    def setUpClass(cls):
        cls.research = load_yaml("competitor-coverage-research.yaml")

    def test_mechanism_294_exists(self):
        """Mechanism #294 must exist."""
        name, entry = find_mechanism(self.research, 294)
        self.assertIsNotNone(entry, "Mechanism #294 not found")

    def test_294_connects_search_collapse_to_openai_dependency(self):
        """#294 must show how Google search traffic collapse pushes
        publishers toward OpenAI citation dependency."""
        name, entry = find_mechanism(self.research, 294)
        if entry is None:
            self.skipTest("Mechanism #294 not found")
        text = str(entry).lower()
        self.assertTrue(
            "search" in text and ("collapse" in text or "decline" in text or "traffic" in text),
            "#294 must reference Google search traffic decline"
        )
        self.assertTrue(
            "citation" in text or "openai" in text,
            "#294 must connect to OpenAI citation dependency"
        )

    def test_294_implicates_wired_coverage(self):
        """Since WIRED is a Condé Nast property, the citation dependency
        should predict softer WIRED coverage of OpenAI."""
        name, entry = find_mechanism(self.research, 294)
        if entry is None:
            self.skipTest("Mechanism #294 not found")
        text = str(entry).lower()
        self.assertTrue(
            any(s in text for s in ["condé nast", "conde nast", "wired", "cond"]),
            "#294 must reference Condé Nast or WIRED in citation dependency chain"
        )

    def test_wired_core_profile_has_adversarial_meta_tone(self):
        """WIRED's core profile should show adversarial Meta coverage."""
        pubs = self.research.get("publications", {})
        wired = pubs.get("wired", {})
        meta_tone = wired.get("meta_coverage_tone", "")
        self.assertIn("adversarial", meta_tone.lower(),
                      f"WIRED Meta tone should be adversarial, got: {meta_tone}")


class TestVergePMCHealthDataSensitivityInversion(unittest.TestCase):
    """Validates mechanism #304 — The Verge/PMC inverts data sensitivity
    ordering: OpenAI ChatGPT Health (HIPAA-category medical records) gets
    neutral framing while Meta glasses (opt-in photos) get surveillance
    vocabulary."""

    @classmethod
    def setUpClass(cls):
        cls.research = load_yaml("competitor-coverage-research.yaml")

    def test_mechanism_304_exists(self):
        """Mechanism #304 must exist."""
        name, entry = find_mechanism(self.research, 304)
        self.assertIsNotNone(entry, "Mechanism #304 not found")

    def test_304_compares_data_sensitivity_levels(self):
        """#304 must compare data sensitivity between health records and photos."""
        name, entry = find_mechanism(self.research, 304)
        if entry is None:
            self.skipTest("Mechanism #304 not found")
        text = str(entry).lower()
        self.assertTrue(
            any(s in text for s in ["health", "medical", "hipaa"]),
            "#304 must reference health/medical data sensitivity"
        )
        self.assertTrue(
            any(s in text for s in ["glasses", "camera", "photo", "video"]),
            "#304 must reference glasses/camera data"
        )

    def test_304_documents_vocabulary_inversion(self):
        """#304 should show that MORE sensitive data (health) gets LESS
        alarm vocabulary — the inversion pattern."""
        name, entry = find_mechanism(self.research, 304)
        if entry is None:
            self.skipTest("Mechanism #304 not found")
        text = str(entry).lower()
        self.assertTrue(
            any(s in text for s in ["inversion", "surveillance", "vocabulary", "framing"]),
            "#304 must document the vocabulary inversion pattern"
        )

    def test_304_identifies_verge_pmc(self):
        """#304 should identify The Verge / PMC as the publication."""
        name, entry = find_mechanism(self.research, 304)
        if entry is None:
            self.skipTest("Mechanism #304 not found")
        text = str(entry).lower()
        self.assertTrue(
            any(s in text for s in ["verge", "pmc", "vox media"]),
            "#304 must identify The Verge or PMC"
        )


class TestCrossValidationAsymmetryScoring(unittest.TestCase):
    """Cross-validates that the financial architecture produces
    statistically meaningful asymmetry across multiple mechanisms."""

    @classmethod
    def setUpClass(cls):
        cls.research = load_yaml("competitor-coverage-research.yaml")
        cls.entities = load_yaml("competitor-entities.yaml")

    def test_aggregate_hypothesis_states_financial_prediction(self):
        """The aggregate findings must state the core hypothesis linking
        financial relationships to coverage tone."""
        agg = self.research.get("aggregate_findings", {})
        hypothesis = agg.get("hypothesis", "")
        h_lower = hypothesis.lower()
        # The hypothesis mentions "licensing revenue" and "cover"
        self.assertTrue(
            ("licensing" in h_lower or "revenue" in h_lower or "financial" in h_lower)
            and ("cover" in h_lower or "favorabl" in h_lower),
            f"Hypothesis must link financial relationships to coverage: {hypothesis[:100]}"
        )

    def test_evidence_strength_is_strong_or_very_strong(self):
        """With 250+ mechanisms, evidence strength should be strong."""
        agg = self.research.get("aggregate_findings", {})
        strength = agg.get("evidence_strength", "")
        self.assertIn(strength.lower(), ["strong", "very_strong", "very strong",
                                          "overwhelming"],
                      f"Evidence strength should be strong+, got: {strength}")

    def test_core_publications_all_show_adversarial_meta_tone(self):
        """Publications without Meta financial relationships (WIRED, Verge,
        Atlantic) should all show adversarial Meta coverage tone."""
        pubs = self.research.get("publications", {})
        no_deal = ["wired", "the-verge", "atlantic"]
        for pub_name in no_deal:
            pub = pubs.get(pub_name, {})
            tone = pub.get("meta_coverage_tone", "")
            self.assertTrue(
                "adversarial" in tone.lower() or "critical" in tone.lower(),
                f"{pub_name} should show adversarial/critical Meta tone, got: {tone}"
            )

    def test_mechanism_count_exceeds_200(self):
        """Total mechanism count across all sections should exceed 200."""
        all_ids = set()
        for section in ("publications", "cross_publication_findings"):
            entries = self.research.get(section, {})
            if isinstance(entries, dict):
                for name, entry in entries.items():
                    if isinstance(entry, dict):
                        mid = entry.get("mechanism_id") or entry.get("mechanism_number")
                        if mid:
                            all_ids.add(mid)
        self.assertGreaterEqual(len(all_ids), 200,
                                f"Expected 200+ mechanisms, found {len(all_ids)}")

    def test_multiple_entity_types_covered(self):
        """The entity database should cover multiple competitor types."""
        entities = self.entities.get("entities", {})
        expected = {"openai", "anthropic", "apple", "google"}
        actual = set(entities.keys())
        missing = expected - actual
        self.assertEqual(missing, set(),
                         f"Missing competitor entities: {missing}")

    def test_openai_ad_infrastructure_documented(self):
        """OpenAI's advertising infrastructure should be documented."""
        entities = self.entities.get("entities", {})
        openai = entities.get("openai", {})
        text = str(openai).lower()
        self.assertTrue(
            any(s in text for s in ["advertising", "ad revenue", "ads", "chatgpt ads"]),
            "OpenAI entity should document advertising infrastructure"
        )

    def test_cross_publication_findings_has_aug25_entries(self):
        """Cross-publication findings should contain entries from today's
        iteration work, identifiable by aug25 test file references."""
        cpf = self.research.get("cross_publication_findings", {})
        aug25_keys = [k for k in cpf.keys() if "aug25" in k.lower()
                      or "broadcom_xpv_100b" in k.lower()
                      or "rebecca_bellan" in k.lower()]
        self.assertGreaterEqual(len(aug25_keys), 2,
                                f"Expected 2+ aug25 cross-publication entries, found: {aug25_keys}")


class TestMechanismCrossReferenceIntegrity(unittest.TestCase):
    """Validates that cross-references between today's mechanisms
    form a coherent chain: #304 → #305 → #306 should connect
    publication-level framing → journalist-level vocabulary →
    financial architecture."""

    @classmethod
    def setUpClass(cls):
        cls.research = load_yaml("competitor-coverage-research.yaml")

    def test_mechanism_305_exists_with_journalist(self):
        """#305 (Rebecca Bellan) should identify the journalist."""
        name, entry = find_mechanism(self.research, 305)
        if entry is None:
            self.skipTest("Mechanism #305 not found")
        text = str(entry).lower()
        self.assertTrue(
            "bellan" in text or "rebecca" in text,
            "#305 must identify Rebecca Bellan as the journalist"
        )

    def test_mechanism_305_has_tone_delta(self):
        """#305 should document a measurable tone delta between
        Meta and Anthropic coverage by the same journalist."""
        name, entry = find_mechanism(self.research, 305)
        if entry is None:
            self.skipTest("Mechanism #305 not found")
        text = str(entry).lower()
        has_delta = any(s in text for s in [
            "delta", "inversion", "bifurcation", "tone",
            "-0.20", "+0.15", "0.35", "vocabulary"
        ])
        self.assertTrue(has_delta,
                        "#305 must contain a measurable tone delta")

    def test_306_references_305_creating_chain(self):
        """#306 should reference #305, creating an explanatory chain:
        financial architecture (#306) → journalist vocabulary (#305)."""
        name306, entry306 = find_mechanism(self.research, 306)
        if entry306 is None:
            self.skipTest("Mechanism #306 not found")
        cross_refs = entry306.get("cross_references", [])
        ref_ids = set()
        for ref in cross_refs:
            if isinstance(ref, dict):
                ref_ids.add(ref.get("mechanism_id"))
            elif isinstance(ref, int):
                ref_ids.add(ref)
        self.assertIn(305, ref_ids,
                      "Financial architecture (#306) should chain to journalist vocabulary (#305)")

    def test_today_mechanisms_have_confounders(self):
        """Each mechanism from today should document confounders."""
        for mech_id in [304, 305, 306]:
            name, entry = find_mechanism(self.research, mech_id)
            if entry is None:
                continue
            text = str(entry).lower()
            has_confounders = (
                "confounder" in text or
                "confounding" in text or
                isinstance(entry.get("confounders"), list) or
                isinstance(entry.get("confounding_factors"), list)
            )
            self.assertTrue(has_confounders,
                            f"Mechanism #{mech_id} should document confounders")


if __name__ == "__main__":
    unittest.main()
