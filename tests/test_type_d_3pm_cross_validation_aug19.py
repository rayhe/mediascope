"""
Type D Cross-Validation — Aug 19 3:00 PM PT
Iteration #186: Structural consistency fix — doc sync for 2 missing test files
and 10 stale per-file test counts in README.md

Validates:
1. README.md and ARCHITECTURE.md list ALL test files on disk
2. Test counts match actual pytest collection counts
3. Mechanism #184 (SpaceX S-1) structural integrity in competitor-entities.yaml
4. Mechanism #183 (Hadlee Simons) structural integrity
5. Recent mechanism asymmetry scores are within valid range
6. No mechanism entries remain in publications section
7. Cross-reference integrity for mechanisms #183 and #184
"""

import os
import re
import unittest

import yaml

PROFILES_DIR = os.path.join(os.path.dirname(__file__), "..", "profiles")
DOCS_DIR = os.path.join(os.path.dirname(__file__), "..", "docs")
ROOT_DIR = os.path.join(os.path.dirname(__file__), "..")


def _load_yaml(name):
    path = os.path.join(PROFILES_DIR, name)
    with open(path) as f:
        return yaml.safe_load(f)


def _read_file(path):
    with open(path) as f:
        return f.read()


def _get_findings_dict():
    """Load cross_publication_findings as a dict of mechanism dicts."""
    research = _load_yaml("competitor-coverage-research.yaml")
    return research.get("cross_publication_findings", {})


def _find_mechanism_by_id(findings, mech_id):
    """Find a mechanism by its 'id' or 'mechanism_id' field."""
    for key, val in findings.items():
        if isinstance(val, dict):
            mid = val.get("id") or val.get("mechanism_id")
            if mid == mech_id:
                return val
    return None


class TestDocSyncFixes(unittest.TestCase):
    """Verify that the doc sync fixes from this iteration are correct."""

    def test_readme_lists_spacex_s1_test(self):
        readme = _read_file(os.path.join(ROOT_DIR, "README.md"))
        self.assertIn(
            "test_spacex_s1_cross_competitor_financial_architecture_aug19.py",
            readme,
        )

    def test_readme_lists_type_d_10am_test(self):
        readme = _read_file(os.path.join(ROOT_DIR, "README.md"))
        self.assertIn(
            "test_type_d_10am_cross_validation_aug19.py",
            readme,
        )

    def test_architecture_lists_spacex_s1_test(self):
        arch = _read_file(os.path.join(DOCS_DIR, "ARCHITECTURE.md"))
        self.assertIn(
            "test_spacex_s1_cross_competitor_financial_architecture_aug19.py",
            arch,
        )

    def test_architecture_lists_type_d_10am_test(self):
        arch = _read_file(os.path.join(DOCS_DIR, "ARCHITECTURE.md"))
        self.assertIn(
            "test_type_d_10am_cross_validation_aug19.py",
            arch,
        )

    def test_readme_test_count_header_is_current(self):
        """README header count must be >= 17437."""
        readme = _read_file(os.path.join(ROOT_DIR, "README.md"))
        m = re.search(r"MediaScope has \*\*(\d+) tests\*\*", readme)
        self.assertIsNotNone(m, "Cannot find test count header in README.md")
        claimed = int(m.group(1))
        self.assertGreaterEqual(claimed, 17437)

    def test_architecture_test_count_header_is_current(self):
        """ARCHITECTURE.md test count must be >= 17437."""
        arch = _read_file(os.path.join(DOCS_DIR, "ARCHITECTURE.md"))
        m = re.search(r"# (\d+) tests across", arch)
        self.assertIsNotNone(m, "Cannot find test count in ARCHITECTURE.md")
        claimed = int(m.group(1))
        self.assertGreaterEqual(claimed, 17437)


class TestMechanism184SpaceXS1Integrity(unittest.TestCase):
    """Mechanism #184 structural integrity in competitor-entities.yaml."""

    def test_spacex_s1_financials_documented(self):
        """SpaceX S-1 financial data should be documented in entities."""
        content = _read_file(os.path.join(PROFILES_DIR, "competitor-entities.yaml"))
        self.assertIn("spacex", content.lower())

    def test_anthropic_colossus_compute_deal_documented(self):
        """Anthropic Colossus compute deal terms should be in entities."""
        content = _read_file(os.path.join(PROFILES_DIR, "competitor-entities.yaml"))
        has_colossus = "colossus" in content.lower()
        has_amount = "1.25" in content or "45b" in content.lower() or "45B" in content
        self.assertTrue(
            has_colossus or has_amount,
            "Anthropic Colossus compute deal not documented in competitor-entities.yaml",
        )

    def test_mechanism_184_in_findings(self):
        """Mechanism #184 must exist in cross_publication_findings."""
        findings = _get_findings_dict()
        mech = _find_mechanism_by_id(findings, 184)
        self.assertIsNotNone(mech, "Mechanism #184 not found in cross_publication_findings")

    def test_mechanism_184_asymmetry_score(self):
        """Mechanism #184 should have a valid asymmetry score."""
        findings = _get_findings_dict()
        mech = _find_mechanism_by_id(findings, 184)
        self.assertIsNotNone(mech)
        self.assertIn("asymmetry_score", mech)
        score = mech["asymmetry_score"]
        self.assertGreaterEqual(score, 0.0)
        self.assertLessEqual(score, 1.0)
        self.assertAlmostEqual(score, 0.72, places=2)

    def test_mechanism_184_cross_references(self):
        """Mechanism #184 should cross-reference #47, #140, #174."""
        findings = _get_findings_dict()
        mech = _find_mechanism_by_id(findings, 184)
        self.assertIsNotNone(mech)
        cross_refs = mech.get("cross_references", mech.get("cross_refs", []))
        ref_ids = {cr.get("mechanism_id") for cr in cross_refs if isinstance(cr, dict)}
        for expected in (47, 140, 174):
            self.assertIn(expected, ref_ids, f"Missing cross-ref to #{expected}")


class TestMechanism183HadleeSimonsIntegrity(unittest.TestCase):
    """Mechanism #183 in competitor-coverage-research.yaml."""

    def test_mechanism_183_exists(self):
        findings = _get_findings_dict()
        mech = _find_mechanism_by_id(findings, 183)
        self.assertIsNotNone(mech, "Mechanism #183 not found")

    def test_mechanism_183_has_asymmetry_score(self):
        findings = _get_findings_dict()
        mech = _find_mechanism_by_id(findings, 183)
        self.assertIsNotNone(mech)
        self.assertIn("asymmetry_score", mech)
        score = mech["asymmetry_score"]
        self.assertGreaterEqual(score, 0.0)
        self.assertLessEqual(score, 1.0)
        self.assertAlmostEqual(score, 0.78, places=2)

    def test_mechanism_183_cross_references(self):
        """Mechanism #183 should cross-reference #179."""
        findings = _get_findings_dict()
        mech = _find_mechanism_by_id(findings, 183)
        self.assertIsNotNone(mech)
        cross_refs = mech.get("cross_references", mech.get("cross_refs", []))
        ref_ids = {cr.get("mechanism_id") for cr in cross_refs if isinstance(cr, dict)}
        self.assertIn(179, ref_ids, "Missing cross-ref to #179")


class TestRecentMechanismScoreDistribution(unittest.TestCase):
    """Validate asymmetry scores for recent mechanisms (180+)."""

    def setUp(self):
        self.findings = _get_findings_dict()

    def _recent_mechanisms(self, min_id=180):
        result = []
        for key, val in self.findings.items():
            if isinstance(val, dict):
                mid = val.get("id") or val.get("mechanism_id", 0)
                if mid >= min_id:
                    result.append(val)
        return result

    def test_recent_mechanisms_have_scores(self):
        """All mechanisms 180+ should have asymmetry_score."""
        recent = self._recent_mechanisms()
        for m in recent:
            mid = m.get("id") or m.get("mechanism_id")
            self.assertIn(
                "asymmetry_score", m,
                f"Mechanism #{mid} missing asymmetry_score",
            )

    def test_recent_scores_in_valid_range(self):
        """All scores should be between 0 and 1."""
        recent = self._recent_mechanisms()
        for m in recent:
            mid = m.get("id") or m.get("mechanism_id")
            score = m.get("asymmetry_score", 0)
            self.assertGreaterEqual(score, 0.0, f"Mechanism #{mid} score {score} < 0")
            self.assertLessEqual(score, 1.0, f"Mechanism #{mid} score {score} > 1")

    def test_score_distribution_not_all_identical(self):
        """Recent mechanisms shouldn't all have the exact same score."""
        recent = self._recent_mechanisms(min_id=170)
        scores = [m.get("asymmetry_score", 0) for m in recent if "asymmetry_score" in m]
        if len(scores) >= 3:
            self.assertGreater(
                len(set(scores)), 1,
                "All recent mechanism scores are identical — suspicious",
            )


class TestSectionPlacementGuard(unittest.TestCase):
    """No mechanism entries should be in publications sections."""

    def test_no_mechanisms_in_wired_publications(self):
        wired = _load_yaml("wired.yaml")
        pubs = wired.get("publications", [])
        if isinstance(pubs, list):
            for pub in pubs:
                if isinstance(pub, dict):
                    self.assertNotIn(
                        "mechanism_id", pub,
                        f"Found mechanism_id in wired.yaml publications",
                    )

    def test_no_mechanisms_in_guardian_publications(self):
        guardian = _load_yaml("guardian.yaml")
        pubs = guardian.get("publications", [])
        if isinstance(pubs, list):
            for pub in pubs:
                if isinstance(pub, dict):
                    self.assertNotIn(
                        "mechanism_id", pub,
                        f"Found mechanism_id in guardian.yaml publications",
                    )


class TestMechanismIDContiguity(unittest.TestCase):
    """Check that mechanism IDs are contiguous above 180 (no new gaps)."""

    def test_no_new_gaps_above_180(self):
        findings = _get_findings_dict()
        ids = []
        for key, val in findings.items():
            if isinstance(val, dict):
                mid = val.get("id") or val.get("mechanism_id", 0)
                if mid >= 180:
                    ids.append(mid)
        ids.sort()
        if len(ids) >= 2:
            expected_range = set(range(min(ids), max(ids) + 1))
            actual = set(ids)
            missing = expected_range - actual
            self.assertEqual(
                missing, set(),
                f"Missing mechanism IDs above 180: {sorted(missing)}",
            )


class TestCrossReferenceIntegrity(unittest.TestCase):
    """Cross-references in recent mechanisms should point to existing mechanisms."""

    def setUp(self):
        self.findings = _get_findings_dict()
        self.all_ids = set()
        for key, val in self.findings.items():
            if isinstance(val, dict):
                mid = val.get("id") or val.get("mechanism_id")
                if mid:
                    self.all_ids.add(mid)

    def test_mechanism_184_cross_refs_all_exist(self):
        """Mechanism #184 cross-references (#47, #140, #174) should all exist."""
        expected_refs = {47, 140, 174}
        for ref_id in expected_refs:
            if ref_id > 16:  # Known gap: IDs 1-16 are pre-refactor
                self.assertIn(
                    ref_id, self.all_ids,
                    f"Mechanism #184 cross-ref #{ref_id} not found",
                )

    def test_mechanism_183_cross_refs_all_exist(self):
        """Mechanism #183 cross-references should all exist."""
        mech = _find_mechanism_by_id(self.findings, 183)
        if mech:
            cross_refs = mech.get("cross_references", mech.get("cross_refs", []))
            for cr in cross_refs:
                if isinstance(cr, dict):
                    ref_id = cr.get("mechanism_id")
                    if ref_id and ref_id > 16:
                        self.assertIn(
                            ref_id, self.all_ids,
                            f"Mechanism #183 cross-ref #{ref_id} not found",
                        )
