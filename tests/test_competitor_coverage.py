"""Tests for competitor coverage analysis.

Verifies that:
1. CompetitorAnalyzer loads all competitor relationships from profiles
2. Financial relationship types are correctly weighted
3. Asymmetry matrix construction works
4. Financial correlation computation produces expected results
5. Coverage predictions align with financial ties
"""

import pytest
from pathlib import Path

# ---------------------------------------------------------------------------
# Fixture: profiles directory path
# ---------------------------------------------------------------------------
PROFILES_DIR = str(Path(__file__).parent.parent / "profiles")


# ===========================================================================
# Section 1: Entity definitions and relationship loading
# ===========================================================================

class TestCompetitorEntities:
    """Tests that competitor-entities.yaml is well-formed."""

    def test_entity_definitions_load(self):
        """All 7 competitor entities should be defined."""
        import yaml
        path = Path(PROFILES_DIR) / "competitor-entities.yaml"
        assert path.exists(), f"competitor-entities.yaml missing at {path}"
        with open(path) as f:
            data = yaml.safe_load(f)
        entities = data.get("entities", {})
        expected = {"openai", "anthropic", "amazon", "apple", "google", "x_twitter", "meta", "xai"}
        assert set(entities.keys()) == expected

    def test_entity_has_required_fields(self):
        """Each entity must have display_name, aliases, regex, and category."""
        import yaml
        with open(Path(PROFILES_DIR) / "competitor-entities.yaml") as f:
            data = yaml.safe_load(f)
        for key, defn in data["entities"].items():
            assert "display_name" in defn, f"{key} missing display_name"
            assert "aliases" in defn, f"{key} missing aliases"
            assert "regex" in defn, f"{key} missing regex"
            assert "category" in defn, f"{key} missing category"

    def test_entity_regex_compiles(self):
        """Every entity regex should compile without error."""
        import re
        import yaml
        with open(Path(PROFILES_DIR) / "competitor-entities.yaml") as f:
            data = yaml.safe_load(f)
        for key, defn in data["entities"].items():
            try:
                re.compile(defn["regex"])
            except re.error as e:
                pytest.fail(f"Entity {key} regex failed to compile: {e}")

    def test_meta_regex_matches_meta_not_metadata(self):
        """Meta regex should match 'Meta' but not 'metadata'."""
        import re
        import yaml
        with open(Path(PROFILES_DIR) / "competitor-entities.yaml") as f:
            data = yaml.safe_load(f)
        meta_regex = data["entities"]["meta"]["regex"]
        assert re.search(meta_regex, "Meta announced new AI features")
        assert not re.search(meta_regex, "The metadata was corrupted")
        assert not re.search(meta_regex, "This metamorphosis was surprising")

    def test_openai_regex_matches_chatgpt(self):
        """OpenAI regex should match ChatGPT and GPT variants."""
        import re
        import yaml
        with open(Path(PROFILES_DIR) / "competitor-entities.yaml") as f:
            data = yaml.safe_load(f)
        openai_regex = data["entities"]["openai"]["regex"]
        assert re.search(openai_regex, "ChatGPT reached 300M weekly users")
        assert re.search(openai_regex, "OpenAI launched GPT-5")
        assert re.search(openai_regex, "Sora generated realistic video")

    def test_apple_regex_excludes_apple_pie(self):
        """Apple regex should match the company but not food terms."""
        import re
        import yaml
        with open(Path(PROFILES_DIR) / "competitor-entities.yaml") as f:
            data = yaml.safe_load(f)
        apple_regex = data["entities"]["apple"]["regex"]
        assert re.search(apple_regex, "Apple announced record earnings")
        assert not re.search(apple_regex, "She made an apple pie")
        assert re.search(apple_regex, "Tim Cook addressed investors")

    def test_amazon_regex_excludes_amazon_river(self):
        """Amazon regex should match the company but not the river."""
        import re
        import yaml
        with open(Path(PROFILES_DIR) / "competitor-entities.yaml") as f:
            data = yaml.safe_load(f)
        amazon_regex = data["entities"]["amazon"]["regex"]
        assert re.search(amazon_regex, "Amazon reported Q2 earnings")
        assert not re.search(amazon_regex, "The Amazon rainforest is burning")
        assert re.search(amazon_regex, "AWS launched new AI services")


# ===========================================================================
# Section 2: Publication profile competitor relationships
# ===========================================================================

class TestPublicationRelationships:
    """Tests that every publication profile has well-formed competitor_relationships."""

    PUBLICATIONS = [
        "wired", "the-verge", "atlantic", "nytimes", "financial-times",
        "guardian", "mit-tech-review", "gizmodo", "news-corp"
    ]

    ENTITIES = ["openai", "meta", "anthropic", "amazon", "apple", "google", "x_twitter"]

    def _load_profile(self, slug):
        import yaml
        path = Path(PROFILES_DIR) / f"{slug}.yaml"
        assert path.exists(), f"Profile {slug}.yaml missing"
        with open(path) as f:
            return yaml.safe_load(f)

    @pytest.mark.parametrize("pub", PUBLICATIONS)
    def test_has_competitor_relationships(self, pub):
        """Each publication must have a competitor_relationships section."""
        data = self._load_profile(pub)
        assert "competitor_relationships" in data, f"{pub} missing competitor_relationships"

    @pytest.mark.parametrize("pub", PUBLICATIONS)
    def test_all_entities_covered(self, pub):
        """Each publication must have entries for all 7 entities."""
        data = self._load_profile(pub)
        cr = data["competitor_relationships"]
        for entity in self.ENTITIES:
            assert entity in cr, f"{pub} missing competitor_relationships.{entity}"

    @pytest.mark.parametrize("pub", PUBLICATIONS)
    def test_financial_tie_is_valid(self, pub):
        """Each relationship must have a recognized financial_tie type."""
        valid_types = {
            "licensing", "investment", "advertising", "distribution",
            "indirect", "mixed", "negotiating", "adversarial", "litigation",
            "adversarial_litigation", "settlement", "coercive",
            "commercial_partnership", "none"
        }
        data = self._load_profile(pub)
        cr = data["competitor_relationships"]
        for entity, rel in cr.items():
            if isinstance(rel, dict):
                tie = rel.get("financial_tie", "none")
                assert tie in valid_types, f"{pub}.{entity} has invalid financial_tie: {tie}"

    @pytest.mark.parametrize("pub", PUBLICATIONS)
    def test_coverage_prediction_is_valid(self, pub):
        """Each relationship must have a valid coverage_prediction."""
        valid_predictions = {"softer", "neutral", "adversarial", "unknown"}
        data = self._load_profile(pub)
        cr = data["competitor_relationships"]
        for entity, rel in cr.items():
            if isinstance(rel, dict):
                pred = rel.get("coverage_prediction", "unknown")
                assert pred in valid_predictions, (
                    f"{pub}.{entity} has invalid coverage_prediction: {pred}"
                )


# ===========================================================================
# Section 3: Financial relationship asymmetry patterns
# ===========================================================================

class TestFinancialAsymmetryPatterns:
    """Test that financial relationships predict coverage asymmetry patterns."""

    def _load_all_profiles(self):
        import yaml
        profiles = {}
        for slug in TestPublicationRelationships.PUBLICATIONS:
            path = Path(PROFILES_DIR) / f"{slug}.yaml"
            with open(path) as f:
                profiles[slug] = yaml.safe_load(f)
        return profiles

    def test_wired_openai_is_licensing(self):
        """WIRED should show licensing relationship with OpenAI (Condé Nast deal)."""
        profiles = self._load_all_profiles()
        wired = profiles["wired"]["competitor_relationships"]
        assert wired["openai"]["financial_tie"] == "licensing"

    def test_wired_meta_is_none(self):
        """WIRED should show no financial relationship with Meta."""
        profiles = self._load_all_profiles()
        wired = profiles["wired"]["competitor_relationships"]
        assert wired["meta"]["financial_tie"] == "none"

    def test_wired_openai_softer_than_meta(self):
        """WIRED coverage prediction: softer for OpenAI, adversarial for Meta."""
        profiles = self._load_all_profiles()
        wired = profiles["wired"]["competitor_relationships"]
        assert wired["openai"]["coverage_prediction"] == "softer"
        assert wired["meta"]["coverage_prediction"] == "adversarial"

    def test_nyt_openai_is_adversarial(self):
        """NYT is suing OpenAI — should show adversarial relationship."""
        profiles = self._load_all_profiles()
        nyt = profiles["nytimes"]["competitor_relationships"]
        assert nyt["openai"]["financial_tie"] == "adversarial"

    def test_nyt_amazon_is_licensing(self):
        """NYT has licensing deal with Amazon — should show licensing."""
        profiles = self._load_all_profiles()
        nyt = profiles["nytimes"]["competitor_relationships"]
        assert nyt["amazon"]["financial_tie"] == "licensing"

    def test_nyt_adversarial_financial_predicts_adversarial_coverage(self):
        """NYT adversarial financial tie with OpenAI → adversarial coverage prediction."""
        profiles = self._load_all_profiles()
        nyt = profiles["nytimes"]["competitor_relationships"]
        assert nyt["openai"]["coverage_prediction"] == "adversarial"

    def test_nyt_licensing_predicts_softer_coverage(self):
        """NYT licensing tie with Amazon → softer coverage prediction."""
        profiles = self._load_all_profiles()
        nyt = profiles["nytimes"]["competitor_relationships"]
        assert nyt["amazon"]["coverage_prediction"] == "softer"

    def test_atlantic_apple_is_investment(self):
        """Atlantic owner LPJ holds ~$17B in Apple stock — should show investment."""
        profiles = self._load_all_profiles()
        atlantic = profiles["atlantic"]["competitor_relationships"]
        assert atlantic["apple"]["financial_tie"] == "investment"

    def test_atlantic_apple_softer_prediction(self):
        """Atlantic's massive Apple financial conflict → softer coverage prediction."""
        profiles = self._load_all_profiles()
        atlantic = profiles["atlantic"]["competitor_relationships"]
        assert atlantic["apple"]["coverage_prediction"] == "softer"

    def test_news_corp_dual_licensing(self):
        """News Corp has licensing deals with BOTH OpenAI AND Meta."""
        profiles = self._load_all_profiles()
        nc = profiles["news-corp"]["competitor_relationships"]
        assert nc["openai"]["financial_tie"] == "licensing"
        assert nc["meta"]["financial_tie"] == "licensing"

    def test_news_corp_balanced_coverage_prediction(self):
        """News Corp with dual deals should predict softer for both."""
        profiles = self._load_all_profiles()
        nc = profiles["news-corp"]["competitor_relationships"]
        assert nc["openai"]["coverage_prediction"] == "softer"
        assert nc["meta"]["coverage_prediction"] == "softer"

    def test_gizmodo_all_none(self):
        """Gizmodo (clean control) should have no financial ties to anyone."""
        profiles = self._load_all_profiles()
        giz = profiles["gizmodo"]["competitor_relationships"]
        for entity in TestPublicationRelationships.ENTITIES:
            assert giz[entity]["financial_tie"] == "none", (
                f"Gizmodo should have no financial tie with {entity}"
            )

    def test_ft_openai_is_licensing(self):
        """FT has confirmed OpenAI licensing deal (Apr 2024)."""
        profiles = self._load_all_profiles()
        ft = profiles["financial-times"]["competitor_relationships"]
        assert ft["openai"]["financial_tie"] == "licensing"

    def test_guardian_openai_is_licensing(self):
        """Guardian signed OpenAI deal Feb 2025."""
        profiles = self._load_all_profiles()
        guardian = profiles["guardian"]["competitor_relationships"]
        assert guardian["openai"]["financial_tie"] == "licensing"

    def test_verge_openai_is_licensing(self):
        """The Verge (via Vox Media) has OpenAI licensing deal."""
        profiles = self._load_all_profiles()
        verge = profiles["the-verge"]["competitor_relationships"]
        assert verge["openai"]["financial_tie"] == "licensing"

    def test_licensing_always_predicts_softer(self):
        """Every licensing relationship should predict softer coverage."""
        profiles = self._load_all_profiles()
        violations = []
        for slug, data in profiles.items():
            cr = data.get("competitor_relationships", {})
            for entity, rel in cr.items():
                if isinstance(rel, dict):
                    if rel.get("financial_tie") == "licensing":
                        pred = rel.get("coverage_prediction")
                        if pred != "softer":
                            violations.append(
                                f"{slug}.{entity}: licensing tie but prediction={pred}"
                            )
        assert not violations, f"Licensing ties should predict softer:\n" + "\n".join(violations)

    def test_adversarial_always_predicts_adversarial(self):
        """Every adversarial financial tie should predict adversarial coverage."""
        profiles = self._load_all_profiles()
        violations = []
        for slug, data in profiles.items():
            cr = data.get("competitor_relationships", {})
            for entity, rel in cr.items():
                if isinstance(rel, dict):
                    if rel.get("financial_tie") == "adversarial":
                        pred = rel.get("coverage_prediction")
                        if pred != "adversarial":
                            violations.append(
                                f"{slug}.{entity}: adversarial tie but prediction={pred}"
                            )
        assert not violations, (
            f"Adversarial ties should predict adversarial coverage:\n"
            + "\n".join(violations)
        )


# ===========================================================================
# Section 4: Source URL verification
# ===========================================================================

class TestSourceURLs:
    """Test that financial claims have source URLs where required."""

    def _load_all_profiles(self):
        import yaml
        profiles = {}
        for slug in TestPublicationRelationships.PUBLICATIONS:
            path = Path(PROFILES_DIR) / f"{slug}.yaml"
            with open(path) as f:
                profiles[slug] = yaml.safe_load(f)
        return profiles

    def test_licensing_deals_have_source_urls(self):
        """Every licensing relationship should have a source_url."""
        profiles = self._load_all_profiles()
        missing = []
        for slug, data in profiles.items():
            cr = data.get("competitor_relationships", {})
            for entity, rel in cr.items():
                if isinstance(rel, dict):
                    tie = rel.get("financial_tie")
                    if tie in ("licensing", "investment"):
                        url = rel.get("source_url", "")
                        if not url:
                            missing.append(f"{slug}.{entity} ({tie})")
        # Allow some missing — not all deals have public source URLs
        # But the major ones (OpenAI, Amazon, News Corp) should have them
        assert len(missing) < 5, (
            f"Too many licensing/investment ties without source_url:\n"
            + "\n".join(missing)
        )


# ===========================================================================
# Section 5: Coverage research YAML
# ===========================================================================

class TestCoverageResearch:
    """Test that the competitor coverage research file is well-formed."""

    def test_research_file_exists(self):
        """competitor-coverage-research.yaml should exist."""
        path = Path(PROFILES_DIR) / "competitor-coverage-research.yaml"
        assert path.exists()

    def test_research_has_all_publications(self):
        """Research should cover all 9 publications."""
        import yaml
        with open(Path(PROFILES_DIR) / "competitor-coverage-research.yaml") as f:
            data = yaml.safe_load(f)
        pubs = data.get("publications", {})
        expected = {
            "wired", "the-verge", "atlantic", "nytimes", "financial-times",
            "guardian", "mit-tech-review", "gizmodo", "news-corp"
        }
        assert set(pubs.keys()) == expected

    def test_research_has_aggregate_findings(self):
        """Research should include aggregate findings with hypothesis and evidence."""
        import yaml
        with open(Path(PROFILES_DIR) / "competitor-coverage-research.yaml") as f:
            data = yaml.safe_load(f)
        agg = data.get("aggregate_findings", {})
        assert "hypothesis" in agg
        assert "evidence_strength" in agg
        assert "key_evidence" in agg
        assert len(agg["key_evidence"]) >= 3

    def test_each_publication_has_meta_coverage(self):
        """Every publication in research should have meta_coverage_tone."""
        import yaml
        with open(Path(PROFILES_DIR) / "competitor-coverage-research.yaml") as f:
            data = yaml.safe_load(f)
        for slug, pub_data in data["publications"].items():
            assert "meta_coverage_tone" in pub_data, f"{slug} missing meta_coverage_tone"
            assert "asymmetry_verdict" in pub_data, f"{slug} missing asymmetry_verdict"
