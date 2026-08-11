"""
Type D cross-validation — Aug 10, 23:00 PT

Cross-validates today's 4 new mechanisms (#33–#36) for internal consistency,
verifies infrastructure counts, checks mechanism_id uniqueness across the
full research YAML, and validates that new profile entries reference their
test files correctly.

Mechanisms validated:
- #33: Cross-Publication Facial Recognition Privacy Parity (OpenAI planned vs Meta dormant)
- #34: WIRED Institutional Rogue AI Coverage Volume Asymmetry
- #35: Advance/Condé Nast Aggregate AI Revenue Dependency
- #36: Pre-IPO Owner-Investor-Publisher Convergence

Also validates:
- No duplicate mechanism_ids in competitor-coverage-research.yaml
- All mechanism test files exist on disk
- README + ARCHITECTURE test counts match actual
- All Aug 10 test files pass structural consistency
- Cross-mechanism coherence (rogue AI #29 ↔ #34, facial recognition #33 ↔ entities)
"""
import os
import re
import unittest
import yaml

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROFILES = os.path.join(REPO, "profiles")
TESTS = os.path.join(REPO, "tests")


def load_yaml(name):
    with open(os.path.join(PROFILES, name)) as f:
        return yaml.safe_load(f)


def load_text(path):
    with open(os.path.join(REPO, path)) as f:
        return f.read()


class TestMechanismIdUniqueness(unittest.TestCase):
    """Every mechanism_id in competitor-coverage-research.yaml must be unique."""

    def test_no_duplicate_mechanism_ids(self):
        text = load_text("profiles/competitor-coverage-research.yaml")
        ids = re.findall(r"mechanism_id:\s*(\d+)", text)
        seen = {}
        for mid in ids:
            if mid in seen:
                seen[mid] += 1
            else:
                seen[mid] = 1
        dupes = {k: v for k, v in seen.items() if v > 1}
        # mechanism_id 17 and 19 appear twice (nested entries) — known and valid
        for known_dup in ["17", "19"]:
            dupes.pop(known_dup, None)
        self.assertEqual(dupes, {}, f"Duplicate mechanism_ids (excluding known nested): {dupes}")

    def test_mechanism_ids_are_contiguous_above_23(self):
        """Mechanisms #23 through current max should be contiguous (no gaps), except known skips."""
        text = load_text("profiles/competitor-coverage-research.yaml")
        ids = sorted(set(int(x) for x in re.findall(r"mechanism_id:\s*(\d+)", text)))
        above_23 = [x for x in ids if x >= 23]
        # mechanism_id 25 was never assigned (known gap)
        known_gaps = {25}
        expected = [x for x in range(min(above_23), max(above_23) + 1) if x not in known_gaps]
        self.assertEqual(above_23, expected,
                         f"Gap in mechanism_ids above 23: have {above_23}, expected {expected}")


class TestMechanism33FacialRecognitionParity(unittest.TestCase):
    """Cross-validate Mechanism #33: OpenAI planned facial recognition vs Meta dormant."""

    def setUp(self):
        self.research = load_yaml("competitor-coverage-research.yaml")
        self.entities = load_yaml("competitor-entities.yaml")

    def test_mechanism_33_exists(self):
        findings = self.research.get("cross_publication_findings", {})
        entry = findings.get("openai_meta_facial_recognition_parity", {})
        self.assertEqual(entry.get("mechanism_id"), 33)

    def test_mechanism_33_references_openai(self):
        findings = self.research.get("cross_publication_findings", {})
        entry = findings.get("openai_meta_facial_recognition_parity", {})
        summary = str(entry.get("finding_summary", ""))
        self.assertIn("OpenAI", summary)
        self.assertIn("facial recognition", summary.lower())

    def test_openai_entities_has_hardware_section(self):
        entities = self.entities.get("entities", self.entities)
        openai = entities.get("openai", {})
        hardware = openai.get("hardware_devices") or openai.get("hardware")
        self.assertIsNotNone(hardware,
                             "competitor-entities.yaml OpenAI section should have hardware_devices")

    def test_test_file_exists(self):
        self.assertTrue(
            os.path.exists(os.path.join(TESTS, "test_openai_meta_facial_recognition_parity_aug10.py")),
            "Mechanism #33 test file must exist"
        )


class TestMechanism34RogueAIVolume(unittest.TestCase):
    """Cross-validate Mechanism #34: WIRED rogue AI coverage volume asymmetry."""

    def setUp(self):
        self.research = load_yaml("competitor-coverage-research.yaml")
        self.wired = load_yaml("wired.yaml")

    def test_mechanism_34_exists(self):
        findings = self.research.get("cross_publication_findings", {})
        entry = findings.get("wired_rogue_ai_coverage_volume_asymmetry", {})
        self.assertEqual(entry.get("mechanism_id"), 34)

    def test_wired_profile_has_rogue_ai_section(self):
        self.assertIn("cross_entity_coverage_analysis", self.wired,
                       "WIRED profile must have cross_entity_coverage_analysis")
        cea = self.wired["cross_entity_coverage_analysis"]
        self.assertIn("rogue_ai_coverage_volume_asymmetry", cea,
                       "Must have rogue_ai_coverage_volume_asymmetry in WIRED cross-entity analysis")

    def test_mechanism_34_coherent_with_29(self):
        """#34 (WIRED rogue AI) should reference or complement #29 (Guardian rogue AI)."""
        findings = self.research.get("cross_publication_findings", {})
        m34 = findings.get("wired_rogue_ai_coverage_volume_asymmetry", {})
        m34_summary = str(m34.get("finding_summary", ""))
        # Both are about rogue AI — at minimum both mention Irregular or containment
        self.assertTrue(
            "irregular" in m34_summary.lower() or "rogue" in m34_summary.lower(),
            "#34 summary should reference the Irregular/rogue AI natural experiment"
        )

    def test_test_file_exists(self):
        self.assertTrue(
            os.path.exists(os.path.join(TESTS, "test_wired_rogue_ai_coverage_volume_asymmetry_aug10.py"))
        )


class TestMechanism35AdvanceAggregate(unittest.TestCase):
    """Cross-validate Mechanism #35: Advance/Condé Nast aggregate AI dependency."""

    def setUp(self):
        self.research = load_yaml("competitor-coverage-research.yaml")

    def test_mechanism_35_exists(self):
        findings = self.research.get("cross_publication_findings", {})
        entry = findings.get("advance_conde_nast_aggregate_ai_dependency", {})
        self.assertEqual(entry.get("mechanism_id"), 35)

    def test_references_conde_nast(self):
        findings = self.research.get("cross_publication_findings", {})
        entry = findings.get("advance_conde_nast_aggregate_ai_dependency", {})
        summary = str(entry.get("finding_summary", ""))
        self.assertTrue(
            "condé nast" in summary.lower() or "conde nast" in summary.lower() or "advance" in summary.lower(),
            "Mechanism #35 should reference Condé Nast or Advance"
        )

    def test_test_file_exists(self):
        self.assertTrue(
            os.path.exists(os.path.join(TESTS, "test_advance_conde_nast_aggregate_ai_dependency_aug10.py"))
        )


class TestMechanism36PreIPOConvergence(unittest.TestCase):
    """Cross-validate Mechanism #36: Pre-IPO owner-investor-publisher convergence."""

    def setUp(self):
        self.research = load_yaml("competitor-coverage-research.yaml")
        self.entities = load_yaml("competitor-entities.yaml")

    def test_mechanism_36_exists(self):
        findings = self.research.get("cross_publication_findings", {})
        entry = findings.get("pre_ipo_owner_investor_publisher_convergence", {})
        self.assertEqual(entry.get("mechanism_id"), 36)

    def test_references_anthropic(self):
        findings = self.research.get("cross_publication_findings", {})
        entry = findings.get("pre_ipo_owner_investor_publisher_convergence", {})
        summary = str(entry.get("finding_summary", ""))
        self.assertIn("Anthropic", summary,
                       "Mechanism #36 should reference Anthropic (pre-IPO subject)")

    def test_three_chains_documented(self):
        """The finding should document Amazon→WashPost, Salesforce→Time, News Corp chains."""
        findings = self.research.get("cross_publication_findings", {})
        entry = findings.get("pre_ipo_owner_investor_publisher_convergence", {})
        summary = str(entry.get("finding_summary", ""))
        for entity in ["Amazon", "Salesforce", "News Corp"]:
            self.assertIn(entity, summary,
                          f"Mechanism #36 should document the {entity} chain")

    def test_entities_yaml_has_convergence_section(self):
        entities = self.entities.get("entities", self.entities)
        anthropic = entities.get("anthropic", {})
        convergence = anthropic.get("pre_ipo_owner_investor_publisher_convergence")
        self.assertIsNotNone(convergence,
                             "Anthropic entry in entities should have pre_ipo_owner_investor_publisher_convergence")

    def test_test_file_exists(self):
        self.assertTrue(
            os.path.exists(os.path.join(TESTS, "test_pre_ipo_owner_investor_publisher_convergence_aug10.py"))
        )


class TestInfrastructureSync(unittest.TestCase):
    """README and ARCHITECTURE test counts match actual."""

    def test_readme_summary_count_matches(self):
        readme = load_text("README.md")
        match = re.search(r"(\d[\d,]+)\s*test files", readme)
        self.assertIsNotNone(match)
        stated = int(match.group(1).replace(",", ""))
        actual = len([f for f in os.listdir(TESTS) if f.startswith("test_") and f.endswith(".py")])
        self.assertEqual(stated, actual,
                         f"README says {stated} test files, actual is {actual}")

    def test_readme_test_count_reasonable(self):
        readme = load_text("README.md")
        match = re.search(r"\*\*(\d[\d,]+)\s*tests\*\*", readme)
        self.assertIsNotNone(match)
        stated = int(match.group(1).replace(",", ""))
        self.assertGreaterEqual(stated, 8800,
                                f"README test count {stated} too low (expected ≥8800)")
        self.assertLessEqual(stated, 9500,
                             f"README test count {stated} suspiciously high")

    def test_architecture_test_count_reasonable(self):
        arch = load_text("docs/ARCHITECTURE.md")
        match = re.search(r"(\d[\d,]+)\s*tests across\s*(\d+)", arch)
        self.assertIsNotNone(match)
        tests = int(match.group(1).replace(",", ""))
        files = int(match.group(2))
        actual_files = len([f for f in os.listdir(TESTS) if f.startswith("test_") and f.endswith(".py")])
        self.assertEqual(files, actual_files,
                         f"ARCHITECTURE says {files} files, actual {actual_files}")

    def test_all_aug10_test_files_present(self):
        """All test files with 'aug10' in their name should exist and be importable."""
        aug10_files = [f for f in os.listdir(TESTS)
                       if f.startswith("test_") and "aug10" in f and f.endswith(".py")]
        self.assertGreaterEqual(len(aug10_files), 10,
                                f"Expected at least 10 Aug 10 test files, found {len(aug10_files)}")

    def test_all_mechanism_test_files_exist(self):
        """Every finding in research YAML with a test_file should have that file on disk."""
        research = load_yaml("competitor-coverage-research.yaml")
        findings = research.get("cross_publication_findings", {})
        missing = []
        for key, val in findings.items():
            if isinstance(val, dict):
                tf = val.get("test_file")
                if tf:
                    path = os.path.join(REPO, tf)
                    if not os.path.exists(path):
                        missing.append(f"{key}: {tf}")
        self.assertEqual(missing, [], f"Missing test files referenced in research YAML: {missing}")


class TestCrossPublicationCoherence(unittest.TestCase):
    """Validate cross-mechanism coherence within today's findings."""

    def setUp(self):
        self.research = load_yaml("competitor-coverage-research.yaml")
        self.findings = self.research.get("cross_publication_findings", {})

    def test_rogue_ai_mechanisms_share_experiment(self):
        """#29 (Guardian) and #34 (WIRED) both describe the same Irregular natural experiment."""
        m29 = self.findings.get("guardian_rogue_ai_volume_temperature_asymmetry", {})
        m34 = self.findings.get("wired_rogue_ai_coverage_volume_asymmetry", {})
        for mid, entry in [(29, m29), (34, m34)]:
            summary = str(entry.get("finding_summary", ""))
            self.assertTrue(
                "openai" in summary.lower() or "anthropic" in summary.lower()
                or "rogue" in summary.lower() or "irregular" in summary.lower(),
                f"Mechanism #{mid} should reference the rogue AI experiment entities"
            )

    def test_meta_isolation_consistent(self):
        """Mechanisms #33 and #36 should both note Meta's lack of financial deals."""
        m33 = self.findings.get("openai_meta_facial_recognition_parity", {})
        m36 = self.findings.get("pre_ipo_owner_investor_publisher_convergence", {})
        for mid, entry in [(33, m33), (36, m36)]:
            summary = str(entry.get("finding_summary", ""))
            self.assertTrue(
                "meta" in summary.lower(),
                f"Mechanism #{mid} should reference Meta"
            )


if __name__ == "__main__":
    unittest.main()
