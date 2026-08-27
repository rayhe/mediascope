"""
Type D Cross-Validation: Mechanisms #333–#338 (Aug 27, 2026, 07:00 PT)
======================================================================

Cross-validates the 6 mechanisms added during the Aug 27 iteration sprint
(05:00–06:00 PT rounds). These form the "settlement-week cluster" —
documenting coverage patterns around Meta's $18B child safety settlement
(Aug 26) and the simultaneous Anthropic $30T TAM / $2T IPO narrative
(Aug 25–26).

Mechanisms under test:
  #333 — Investor-Podcast-Publisher Financial Architecture Convergence
  #334 — Bloomberg LP Upstream Narrative Originator (Meta settlement vs Anthropic IPO)
  #335 — Jonathan Vanian (CNBC) Government Action Vocabulary Register Inversion
  #336 — TechCrunch/Yahoo OpenAI ChatGPT Ads Europe Coverage Selection Silence
  #337 — Meghan Bobrowsky (WSJ) Settlement-Week Vocabulary Bifurcation
  #338 — Insurance Denial Precedent — Asymmetric Financial Materiality Architecture

Additionally validates:
  - Settlement-week temporal clustering (all within 48h of Aug 26 settlement)
  - Cross-mechanism consistency (shared entities, shared confounders)
  - Financial architecture coherence across mechanisms
  - Dependency chain: textblob + vaderSentiment must be importable
"""

import unittest
from pathlib import Path
import yaml
import importlib

PROFILES_DIR = Path(__file__).resolve().parent.parent / "profiles"
TESTS_DIR = Path(__file__).resolve().parent


def _load_research():
    with open(PROFILES_DIR / "competitor-coverage-research.yaml") as f:
        return yaml.safe_load(f)


def _find_mechanism(data, mechanism_id):
    """Recursively search all sections for a mechanism by ID."""
    # Check publications
    for key, val in data.get("publications", {}).items():
        if isinstance(val, dict) and val.get("mechanism_id") == mechanism_id:
            return key, val, "publications"
    # Check cross_publication_findings
    for key, val in data.get("cross_publication_findings", {}).items():
        if isinstance(val, dict):
            if val.get("mechanism_id") == mechanism_id:
                return key, val, "cross_publication_findings"
            # Check nested dicts
            for subkey, subval in val.items():
                if isinstance(subval, dict) and subval.get("mechanism_id") == mechanism_id:
                    return f"{key}.{subkey}", subval, "cross_publication_findings"
    # Check journalist_profiles
    for key, val in data.get("journalist_profiles", {}).items():
        if isinstance(val, dict):
            for subkey, subval in val.items():
                if isinstance(subval, dict) and subval.get("mechanism_id") == mechanism_id:
                    return f"{key}.{subkey}", subval, "journalist_profiles"
            entries = val.get("cross_entity_examples", [])
            if isinstance(entries, list):
                for entry in entries:
                    if isinstance(entry, dict) and entry.get("mechanism_id") == mechanism_id:
                        return f"{key}.cross_entity", entry, "journalist_profiles"
    # Check podcast section
    for key, val in data.get("podcast_sentiment", {}).items():
        if isinstance(val, dict) and val.get("mechanism_id") == mechanism_id:
            return key, val, "podcast_sentiment"
    return None, None, None


def _deep_search_mechanism(data, mechanism_id, path=""):
    """Deep recursive search."""
    if isinstance(data, dict):
        if data.get("mechanism_id") == mechanism_id:
            return path, data
        for k, v in data.items():
            result = _deep_search_mechanism(v, mechanism_id, f"{path}.{k}")
            if result[1] is not None:
                return result
    elif isinstance(data, list):
        for i, item in enumerate(data):
            result = _deep_search_mechanism(item, mechanism_id, f"{path}[{i}]")
            if result[1] is not None:
                return result
    return path, None


class TestSettlementWeekMechanismExistence(unittest.TestCase):
    """All 6 mechanisms from the Aug 27 settlement-week sprint exist."""

    @classmethod
    def setUpClass(cls):
        cls.data = _load_research()

    def _get_mechanism(self, mid):
        """Try standard lookup, fallback to deep search."""
        key, val, section = _find_mechanism(self.data, mid)
        if val is None:
            path, val = _deep_search_mechanism(self.data, mid)
            key = path
        self.assertIsNotNone(val, f"Mechanism #{mid} not found anywhere in research data")
        return key, val

    def test_mechanism_333_exists(self):
        key, val = self._get_mechanism(333)
        # Should be podcast/cross-surface convergence
        desc = str(val).lower()
        self.assertTrue(
            any(term in desc for term in ["podcast", "investor", "convergence"]),
            f"#333 should relate to podcast/investor convergence, got key={key}"
        )

    def test_mechanism_334_exists(self):
        key, val = self._get_mechanism(334)
        desc = str(val).lower()
        self.assertTrue(
            any(term in desc for term in ["bloomberg", "narrative", "originator"]),
            f"#334 should relate to Bloomberg narrative, got key={key}"
        )

    def test_mechanism_335_exists(self):
        key, val = self._get_mechanism(335)
        desc = str(val).lower()
        self.assertTrue(
            any(term in desc for term in ["vanian", "cnbc", "government"]),
            f"#335 should relate to Vanian/CNBC, got key={key}"
        )

    def test_mechanism_336_exists(self):
        key, val = self._get_mechanism(336)
        desc = str(val).lower()
        self.assertTrue(
            any(term in desc for term in ["techcrunch", "openai", "chatgpt", "ads", "europe"]),
            f"#336 should relate to TechCrunch/OpenAI coverage selection, got key={key}"
        )

    def test_mechanism_337_exists(self):
        key, val = self._get_mechanism(337)
        desc = str(val).lower()
        self.assertTrue(
            any(term in desc for term in ["bobrowsky", "wsj", "settlement"]),
            f"#337 should relate to Bobrowsky/WSJ, got key={key}"
        )

    def test_mechanism_338_exists(self):
        key, val = self._get_mechanism(338)
        desc = str(val).lower()
        self.assertTrue(
            any(term in desc for term in ["insurance", "denial", "financial materiality"]),
            f"#338 should relate to insurance denial, got key={key}"
        )

    def test_sequential_ids_333_to_338(self):
        """All IDs from 333–338 exist."""
        found = set()
        for mid in range(333, 339):
            key, val, section = _find_mechanism(self.data, mid)
            if val is None:
                _, val = _deep_search_mechanism(self.data, mid)
            if val is not None:
                found.add(mid)
        missing = set(range(333, 339)) - found
        self.assertEqual(missing, set(),
                        f"Missing mechanisms: {missing}")


class TestSettlementWeekConfounderQuality(unittest.TestCase):
    """Each settlement-week mechanism documents confounders with strength ratings."""

    @classmethod
    def setUpClass(cls):
        cls.data = _load_research()

    def _get_mechanism(self, mid):
        key, val, section = _find_mechanism(self.data, mid)
        if val is None:
            _, val = _deep_search_mechanism(self.data, mid)
        return val

    def _extract_confounders(self, mechanism):
        """Extract confounders from various possible field names."""
        if mechanism is None:
            return []
        for field in ["confounders", "confounding_factors", "confounder_analysis"]:
            c = mechanism.get(field, [])
            if c:
                return c if isinstance(c, list) else [c]
        return []

    def test_333_has_confounders(self):
        m = self._get_mechanism(333)
        if m is None:
            self.skipTest("Mechanism #333 not found")
        confounders = self._extract_confounders(m)
        self.assertGreater(len(confounders), 0, "#333 has no confounders")

    def test_338_has_strong_confounders(self):
        m = self._get_mechanism(338)
        if m is None:
            self.skipTest("Mechanism #338 not found")
        confounders = self._extract_confounders(m)
        self.assertGreater(len(confounders), 0, "#338 has no confounders")
        # Insurance denial should have strong confounders given legal specificity
        has_strong = False
        for c in confounders:
            if isinstance(c, dict):
                strength = str(c.get("strength", "")).upper()
                if strength == "STRONG":
                    has_strong = True
                    break
            elif isinstance(c, str) and "STRONG" in c.upper():
                has_strong = True
                break
        self.assertTrue(has_strong,
                       "#338 (insurance denial) should have at least one STRONG confounder")

    def test_337_has_beat_assignment_confounder(self):
        """WSJ settlement-week bifurcation should note beat assignment as confounder."""
        m = self._get_mechanism(337)
        if m is None:
            self.skipTest("Mechanism #337 not found")
        confounders = self._extract_confounders(m)
        all_text = " ".join(str(c) for c in confounders).lower()
        self.assertTrue(
            any(term in all_text for term in ["beat", "assignment", "desk", "genre"]),
            "#337 should document beat assignment as confounder"
        )


class TestSettlementWeekCrossReferences(unittest.TestCase):
    """Settlement-week mechanisms should cross-reference each other."""

    @classmethod
    def setUpClass(cls):
        cls.data = _load_research()

    def _get_mechanism(self, mid):
        key, val, section = _find_mechanism(self.data, mid)
        if val is None:
            _, val = _deep_search_mechanism(self.data, mid)
        return val

    def _get_cross_refs(self, mechanism):
        """Extract cross-referenced mechanism IDs."""
        if mechanism is None:
            return set()
        refs = set()
        for field in ["cross_references", "cross_validates", "extends", "complements"]:
            cr = mechanism.get(field, [])
            if isinstance(cr, list):
                for item in cr:
                    if isinstance(item, dict):
                        mid = item.get("mechanism_id")
                        if mid is not None:
                            refs.add(int(mid))
                    elif isinstance(item, (int, float)):
                        refs.add(int(item))
        return refs

    def test_338_references_settlement_mechanisms(self):
        """Insurance denial (#338) should reference at least one settlement mechanism."""
        m = self._get_mechanism(338)
        if m is None:
            self.skipTest("Mechanism #338 not found")
        refs = self._get_cross_refs(m)
        settlement_refs = refs & set(range(326, 339))
        self.assertGreater(len(settlement_refs), 0,
                          "#338 should cross-reference other settlement-week mechanisms")


class TestSettlementWeekEntities(unittest.TestCase):
    """Settlement-week mechanisms should consistently reference Meta and competitors."""

    @classmethod
    def setUpClass(cls):
        cls.data = _load_research()

    def _get_mechanism(self, mid):
        key, val, section = _find_mechanism(self.data, mid)
        if val is None:
            _, val = _deep_search_mechanism(self.data, mid)
        return val

    def test_338_meta_as_primary_entity(self):
        m = self._get_mechanism(338)
        if m is None:
            self.skipTest("Mechanism #338 not found")
        entities = m.get("entities", {})
        all_text = str(entities).lower()
        self.assertIn("meta", all_text,
                     "#338 should have Meta as an entity")

    def test_338_has_comparator_entities(self):
        m = self._get_mechanism(338)
        if m is None:
            self.skipTest("Mechanism #338 not found")
        entities = m.get("entities", {})
        comparators = entities.get("comparators", [])
        all_text = str(entities).lower()
        self.assertTrue(
            any(term in all_text for term in ["anthropic", "openai"]),
            "#338 should compare Meta with AI labs"
        )


class TestAsymmetryScoreConsistency(unittest.TestCase):
    """Asymmetry scores in settlement-week mechanisms should be in valid range."""

    @classmethod
    def setUpClass(cls):
        cls.data = _load_research()

    def _get_mechanism(self, mid):
        key, val, section = _find_mechanism(self.data, mid)
        if val is None:
            _, val = _deep_search_mechanism(self.data, mid)
        return val

    def _get_score(self, mechanism):
        if mechanism is None:
            return None
        for field in ["adjusted_score", "asymmetry_score", "raw_score"]:
            score = mechanism.get(field)
            if score is not None:
                return float(score)
        return None

    def test_338_score_in_range(self):
        m = self._get_mechanism(338)
        if m is None:
            self.skipTest("Mechanism #338 not found")
        score = self._get_score(m)
        if score is None:
            self.skipTest("#338 has no asymmetry score")
        self.assertGreaterEqual(score, 0.0, "Score must be >= 0")
        self.assertLessEqual(score, 1.0, "Score must be <= 1")

    def test_337_score_modest_given_confounders(self):
        """WSJ bifurcation has strong structural confounders — score should be < 0.5."""
        m = self._get_mechanism(337)
        if m is None:
            self.skipTest("Mechanism #337 not found")
        score = self._get_score(m)
        if score is None:
            self.skipTest("#337 has no asymmetry score")
        self.assertLess(score, 0.5,
                       "#337 has strong beat-assignment confounders; adjusted score should be modest")


class TestDependencyChain(unittest.TestCase):
    """Core NLP dependencies must be importable after pip install."""

    def test_textblob_importable(self):
        try:
            importlib.import_module("textblob")
        except ImportError:
            self.fail("textblob is not importable — run: pip install textblob")

    def test_vader_importable(self):
        try:
            importlib.import_module("vaderSentiment.vaderSentiment")
        except ImportError:
            self.fail("vaderSentiment is not importable — run: pip install vaderSentiment")

    def test_yaml_importable(self):
        try:
            importlib.import_module("yaml")
        except ImportError:
            self.fail("PyYAML is not importable — run: pip install pyyaml")

    def test_mediascope_sentiment_importable(self):
        """The composite sentiment module should import without errors."""
        try:
            from mediascope.analyze.sentiment import analyze_composite
        except ImportError as e:
            self.fail(f"mediascope.analyze.sentiment import failed: {e}")


class TestSettlementWeekNaturalExperiment(unittest.TestCase):
    """
    The Meta $18B settlement (Aug 26) and Anthropic $30T TAM/$2T IPO pitch
    (Aug 25-26) create a natural experiment: how do publications cover two
    major tech stories in the same 48-hour window?

    Cross-validates mechanisms #326–#338 which document this experiment.
    """

    @classmethod
    def setUpClass(cls):
        cls.data = _load_research()

    def test_settlement_cluster_size(self):
        """At least 6 mechanisms should reference the Aug 26 settlement or IPO."""
        settlement_mechanisms = set()
        for mid in range(326, 339):
            _, val = _deep_search_mechanism(self.data, mid)
            if val is not None:
                all_text = str(val).lower()
                if any(term in all_text for term in [
                    "settlement", "18b", "18 billion",
                    "anthropic", "ipo", "30 trillion", "2 trillion"
                ]):
                    settlement_mechanisms.add(mid)
        self.assertGreaterEqual(len(settlement_mechanisms), 6,
                               f"Expected >= 6 settlement-week mechanisms, found {len(settlement_mechanisms)}: {settlement_mechanisms}")

    def test_multi_publication_coverage(self):
        """Settlement-week mechanisms should span at least 3 publications."""
        publications = set()
        for mid in range(326, 339):
            _, val = _deep_search_mechanism(self.data, mid)
            if val is not None:
                pub = val.get("publication", "")
                if pub:
                    publications.add(pub.lower())
        self.assertGreaterEqual(len(publications), 3,
                               f"Settlement-week should span 3+ publications, found: {publications}")


if __name__ == "__main__":
    unittest.main()
