"""
Type D Cross-Validation — Aug 19 10:00 AM PT
Iteration #181: Structural integrity fixes from test suite run

Validates:
1. Mechanism #180 correctly placed in cross_publication_findings (not publications)
2. Mechanism #178 has top-level asymmetry_score
3. Guardian-Samsung financial_tie uses valid type ('indirect' not 'indirect_via_google')
4. Nvidia entity present in competitor-entities.yaml
5. YAML structural integrity after section relocation
6. No mechanism entries remain in publications section
7. Score distribution for recent mechanisms (170+) is reasonable
"""

import os
import unittest

import yaml

PROFILES_DIR = os.path.join(os.path.dirname(__file__), "..", "profiles")


def _load_yaml(name):
    path = os.path.join(PROFILES_DIR, name)
    with open(path) as f:
        return yaml.safe_load(f)


class TestMechanism180Placement(unittest.TestCase):
    """Mechanism #180 must be in cross_publication_findings, not publications."""

    @classmethod
    def setUpClass(cls):
        cls.ccr = _load_yaml("competitor-coverage-research.yaml")

    def test_mechanism_180_in_cpf(self):
        cpf = self.ccr.get("cross_publication_findings", {})
        found = any(
            isinstance(v, dict) and v.get("mechanism_id") == 180
            for v in cpf.values()
        )
        assert found, "Mechanism #180 not found in cross_publication_findings"

    def test_mechanism_180_not_in_publications(self):
        pubs = self.ccr.get("publications", {})
        for pub_key, pub_val in pubs.items():
            if isinstance(pub_val, dict):
                for key in pub_val:
                    assert "samsung_reddit_advance" not in str(key), (
                        f"Mechanism #180 still in publications/{pub_key}/{key}"
                    )

    def test_mechanism_180_has_score(self):
        cpf = self.ccr.get("cross_publication_findings", {})
        for key, val in cpf.items():
            if isinstance(val, dict) and val.get("mechanism_id") == 180:
                score = val.get("asymmetry_score")
                assert score is not None, "#180 missing asymmetry_score"
                assert 0.5 <= score <= 1.0, f"#180 score {score} out of range"
                break

    def test_mechanism_180_has_required_fields(self):
        cpf = self.ccr.get("cross_publication_findings", {})
        entry = cpf.get("samsung_reddit_advance_advertising_feedback_loop", {})
        assert entry.get("mechanism_id") == 180
        assert entry.get("type") == "financial_incentive_triple_channel"
        assert entry.get("entities") == ["Samsung", "Meta"]
        assert entry.get("publication_parent") == "Advance Publications"
        assert entry.get("test_file") is not None
        assert entry.get("source_urls") is not None
        assert len(entry.get("source_urls", [])) >= 2


class TestMechanism178TopLevelScore(unittest.TestCase):
    """Mechanism #178 must have a top-level asymmetry_score in CPF."""

    @classmethod
    def setUpClass(cls):
        cls.ccr = _load_yaml("competitor-coverage-research.yaml")

    def test_mechanism_178_has_top_level_score(self):
        cpf = self.ccr.get("cross_publication_findings", {})
        for key, val in cpf.items():
            if isinstance(val, dict) and val.get("mechanism_id") == 178:
                score = val.get("asymmetry_score")
                assert score is not None, (
                    "#178 missing top-level asymmetry_score (may be nested under significance)"
                )
                assert score == 0.91, f"#178 score should be 0.91, got {score}"
                break
        else:
            self.fail("#178 not found in cross_publication_findings")


class TestGuardianSamsungFinancialTie(unittest.TestCase):
    """Guardian-Samsung financial_tie must use a valid relationship type."""

    @classmethod
    def setUpClass(cls):
        cls.guardian = _load_yaml("guardian.yaml")

    def test_samsung_tie_is_valid(self):
        cr = self.guardian.get("competitor_relationships", {})
        samsung = cr.get("samsung", {})
        tie = samsung.get("financial_tie")
        valid_types = {
            "negotiating", "licensing", "indirect", "mixed", "advertising",
            "indirect_endowment", "settlement_reported", "litigation",
            "settlement", "investment", "coercive", "adversarial",
            "advertising_dependency", "none", "adversarial_litigation",
            "commercial_partnership"
        }
        assert tie in valid_types, f"Guardian-Samsung financial_tie '{tie}' not in valid types"

    def test_samsung_prediction_is_valid(self):
        cr = self.guardian.get("competitor_relationships", {})
        samsung = cr.get("samsung", {})
        pred = samsung.get("coverage_prediction")
        valid_predictions = {
            "softer", "softer_than_expected", "neutral", "adversarial",
            "positive_if_deal_confirmed", "unknown", "neutral_to_absent"
        }
        assert pred in valid_predictions, (
            f"Guardian-Samsung coverage_prediction '{pred}' not in valid predictions"
        )


class TestNvidiaEntityPresent(unittest.TestCase):
    """Nvidia must be in competitor-entities.yaml."""

    @classmethod
    def setUpClass(cls):
        cls.entities = _load_yaml("competitor-entities.yaml")

    def test_nvidia_exists(self):
        entities = self.entities.get("entities", self.entities)
        assert "nvidia" in entities, "nvidia not found in competitor-entities.yaml"

    def test_nvidia_has_name(self):
        entities = self.entities.get("entities", self.entities)
        nvidia = entities.get("nvidia", {})
        assert nvidia.get("display_name") or nvidia.get("name"), "nvidia entity missing name field"


class TestNoMechanismsInPublications(unittest.TestCase):
    """No mechanism entries should exist in the publications section."""

    @classmethod
    def setUpClass(cls):
        cls.ccr = _load_yaml("competitor-coverage-research.yaml")

    def test_publications_clean(self):
        pubs = self.ccr.get("publications", {})
        mechanism_keys = []
        for pub_key, pub_val in pubs.items():
            if isinstance(pub_val, dict):
                for key, val in pub_val.items():
                    if isinstance(val, dict) and "mechanism_id" in val and "finding" in val:
                        mechanism_keys.append(f"{pub_key}/{key}")
        assert not mechanism_keys, (
            f"Mechanism entries found in publications section: {mechanism_keys}"
        )


class TestRecentMechanismScores(unittest.TestCase):
    """All mechanisms >= 170 in CPF must have valid asymmetry_score."""

    @classmethod
    def setUpClass(cls):
        cls.ccr = _load_yaml("competitor-coverage-research.yaml")

    def test_all_recent_scored(self):
        cpf = self.ccr.get("cross_publication_findings", {})
        issues = []
        for key, val in cpf.items():
            if isinstance(val, dict) and val.get("mechanism_id", 0) >= 170:
                score = val.get("asymmetry_score")
                mid = val["mechanism_id"]
                if score is None:
                    issues.append(f"#{mid} missing score")
                elif not (0.5 <= score <= 1.0):
                    issues.append(f"#{mid} score={score} out of [0.5, 1.0]")
        assert not issues, f"Score issues: {issues}"

    def test_cpf_count_at_least_150(self):
        cpf = self.ccr.get("cross_publication_findings", {})
        count = sum(
            1 for v in cpf.values()
            if isinstance(v, dict) and "mechanism_id" in v
        )
        assert count >= 150, f"Only {count} mechanisms in CPF, expected >= 150"

    def test_max_mechanism_id_at_least_180(self):
        cpf = self.ccr.get("cross_publication_findings", {})
        max_id = max(
            (v["mechanism_id"] for v in cpf.values()
             if isinstance(v, dict) and "mechanism_id" in v),
            default=0
        )
        assert max_id >= 180, f"Max mechanism ID is {max_id}, expected >= 180"


class TestYAMLStructuralIntegrity(unittest.TestCase):
    """The YAML file must parse without errors after structural edits."""

    def test_ccr_parses(self):
        data = _load_yaml("competitor-coverage-research.yaml")
        assert "cross_publication_findings" in data
        assert "publications" in data
        assert "methodology" in data

    def test_guardian_parses(self):
        data = _load_yaml("guardian.yaml")
        assert "competitor_relationships" in data

    def test_competitor_entities_parses(self):
        data = _load_yaml("competitor-entities.yaml")
        entities = data.get("entities", data)
        assert "nvidia" in entities


if __name__ == "__main__":
    unittest.main()
