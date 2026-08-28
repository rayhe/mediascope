"""
CNN/WBD Settlement-Week AG Uthmeier Cross-Entity Contextualization Gap

Type A: Competitor Coverage Deep Dive
Publication: CNN (Warner Bros. Discovery)
Competitor: OpenAI
Mechanism: #347 — CNN Settlement-Week AG Cross-Entity Contextualization Gap

CORE FINDING:
CNN's settlement coverage (Clare Duffy, Aug 26-27, 2026) quotes Florida AG James
Uthmeier as the lone holdout AG who refused to join the Meta settlement, calling
payouts "peanuts compared to the profound harms Meta's profit-driven addictive
features inflicted on kids." CNN NEVER cross-references that Uthmeier is ALSO:
- The first AG to sue OpenAI over child safety (CNN's own Jun 1, 2026 article)
- The AG who launched the first-ever criminal investigation into OpenAI (Apr 2026)
- An AG who uses IDENTICAL rhetoric for OpenAI: "chosen profit over public safety"

CNN's own Aug 24 article (OpenAI subpoena by Alabama AG) mentions Uthmeier's
OpenAI lawsuit, proving institutional awareness just 2 days before the settlement.

This is a natural experiment: Same AG, same child safety topic domain, identical
rhetoric structure, different entities, different editorial contextualization.

Sources:
- CNN Aug 27: https://www.cnn.com/2026/08/27/tech/meta-settlement-impact-on-teens-business
- CNN Aug 26: https://www.cnn.com/2026/08/26/tech/meta-states-settle-trial-children
- CNN Jun 1: https://www.cnn.com/2026/06/01/business/florida-sues-chatgpt-openai-sam-altman
- CNN Aug 24: https://www.cnn.com/2026/08/24/tech/openai-subpoena-hugging-face-attorney-general-alabama
- CNN May 5: https://www.cnn.com/2026/05/05/tech/ai-youth-safety-independent-testing-lab
"""

import pytest
import yaml
import os

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROFILES_DIR = os.path.join(REPO_ROOT, "profiles")


def load_yaml(filename):
    path = os.path.join(PROFILES_DIR, filename)
    with open(path, "r") as f:
        return yaml.safe_load(f)


def find_mechanism(data, mechanism_id):
    """Search all top-level sections for a mechanism by ID."""
    for top_key in data:
        section = data[top_key]
        if isinstance(section, dict):
            for k, v in section.items():
                if isinstance(v, dict) and v.get("mechanism_id") == mechanism_id:
                    return v
    return None


def get_m347():
    data = load_yaml("competitor-coverage-research.yaml")
    m = find_mechanism(data, 347)
    assert m is not None, "Mechanism #347 not found"
    return m


class TestMechanismExistence:
    """Verify mechanism #347 exists in competitor-coverage-research.yaml."""

    def test_mechanism_347_exists(self):
        m = get_m347()
        assert m is not None

    def test_mechanism_347_has_title(self):
        m = get_m347()
        assert "title" in m or "finding" in m, "Missing title or finding"

    def test_mechanism_347_has_type(self):
        m = get_m347()
        assert m.get("type") is not None, "Missing type"

    def test_mechanism_347_has_asymmetry_score(self):
        m = get_m347()
        score = m.get("asymmetry_score")
        assert score is not None, "Missing asymmetry_score"
        assert 0.0 <= score <= 1.0, f"Score {score} out of range"

    def test_mechanism_347_has_test_file(self):
        m = get_m347()
        tf = m.get("test_file", "")
        assert "cnn_wbd" in tf or "uthmeier" in tf, f"test_file should reference CNN/Uthmeier: {tf}"


class TestAGUthmeierNaturalExperiment:
    """Core natural experiment: Same AG, same topic, different entities, different framing."""

    def test_uthmeier_meta_rhetoric_documented(self):
        """CNN Aug 27 quotes Uthmeier's Meta rhetoric."""
        m = get_m347()
        finding = str(m.get("finding", ""))
        assert "peanuts" in finding.lower() or "uthmeier" in finding.lower(), \
            "Should document Uthmeier's Meta settlement quote"

    def test_uthmeier_openai_rhetoric_documented(self):
        """CNN Jun 1 quotes Uthmeier's identical OpenAI rhetoric."""
        m = get_m347()
        finding = str(m.get("finding", ""))
        assert "openai" in finding.lower() or "profit over" in finding.lower(), \
            "Should document Uthmeier's OpenAI rhetoric parallel"

    def test_institutional_awareness_documented(self):
        """CNN Aug 24 article proves newsroom knows about Uthmeier's OpenAI enforcement."""
        m = get_m347()
        finding = str(m.get("finding", ""))
        evidence = str(m.get("evidence", ""))
        combined = finding + evidence
        assert "aug 24" in combined.lower() or "august 24" in combined.lower() or \
               "subpoena" in combined.lower() or "institutional" in combined.lower(), \
            "Should document CNN's institutional awareness via Aug 24 article"

    def test_same_ag_different_entity_framing(self):
        """The natural experiment: identical rhetoric, different contextualization."""
        m = get_m347()
        finding = str(m.get("finding", ""))
        assert "cross-reference" in finding.lower() or "contextualization" in finding.lower() or \
               "omit" in finding.lower() or "absent" in finding.lower(), \
            "Should document the cross-entity contextualization gap"


class TestCNNSettlementArticleVocabulary:
    """Verify the vocabulary register differential is documented."""

    def test_meta_accountability_vocabulary(self):
        """CNN settlement articles use full accountability vocabulary for Meta."""
        m = get_m347()
        finding = str(m.get("finding", ""))
        assert any(term in finding.lower() for term in
                   ["addictive", "harm", "settlement", "accountability"]), \
            "Should document Meta accountability vocabulary in CNN coverage"

    def test_openai_coverage_register_differential(self):
        """CNN OpenAI child safety coverage uses different register."""
        m = get_m347()
        finding = str(m.get("finding", ""))
        assert "florida" in finding.lower() or "child safety" in finding.lower(), \
            "Should document OpenAI child safety coverage context"


class TestCNNFinancialArchitecture:
    """Verify CNN/WBD financial incentive structure is connected."""

    def test_wbd_cnn_entity_exists(self):
        """CNN/WBD entity exists in competitor-entities.yaml."""
        data = load_yaml("competitor-entities.yaml")
        # Navigate to the correct top-level key
        entities = data.get("entities", data)
        found = False
        if isinstance(entities, dict):
            for key, val in entities.items():
                if isinstance(val, dict):
                    aliases = val.get("aliases", [])
                    name = val.get("display_name", "")
                    if "CNN" in str(aliases) or "CNN" in name or "cnn" in str(key):
                        found = True
                        break
        assert found, "WBD/CNN entity should exist in competitor-entities.yaml"

    def test_meta_content_deal_documented(self):
        """CNN's Meta content licensing deal (Dec 2025) is documented."""
        data = load_yaml("competitor-entities.yaml")
        content = yaml.dump(data)
        assert "meta" in content.lower() and "content" in content.lower() and \
               ("cnn" in content.lower() or "wbd" in content.lower()), \
            "CNN's Meta content deal should be documented"

    def test_mechanism_124_cross_reference(self):
        """Mechanism #347 should cross-reference mechanism #124 (quad financial architecture)."""
        m = get_m347()
        cross_refs = m.get("cross_references", m.get("cross_validates", []))
        finding = str(m.get("finding", ""))
        has_ref = False
        if isinstance(cross_refs, list):
            for ref in cross_refs:
                if isinstance(ref, dict) and ref.get("mechanism_id") == 124:
                    has_ref = True
                elif ref == 124:
                    has_ref = True
        if "124" in finding or "#124" in finding:
            has_ref = True
        assert has_ref, "Should cross-reference mechanism #124 (WBD quad financial architecture)"


class TestConfounderDocumentation:
    """Verify confounders are properly documented."""

    def test_has_confounders(self):
        m = get_m347()
        confounders = m.get("confounders", [])
        assert len(confounders) >= 2, f"Should have at least 2 confounders, got {len(confounders)}"

    def test_has_strong_confounders(self):
        m = get_m347()
        confounders = m.get("confounders", [])
        strong_count = sum(1 for c in confounders
                           if isinstance(c, dict) and c.get("severity", "").upper() == "STRONG")
        assert strong_count >= 2, f"Should have at least 2 STRONG confounders, got {strong_count}"

    def test_beat_assignment_confounder(self):
        """Beat assignment is a structural confounder."""
        m = get_m347()
        confounders = m.get("confounders", [])
        has_beat = any("beat" in str(c).lower() for c in confounders)
        assert has_beat, "Should document beat assignment as a confounder"

    def test_news_value_confounder(self):
        """News value proportionality is a confounder."""
        m = get_m347()
        confounders = m.get("confounders", [])
        has_news_value = any("news value" in str(c).lower() or "proportional" in str(c).lower()
                             for c in confounders)
        assert has_news_value, "Should document news value proportionality as a confounder"


class TestSourceURLIntegrity:
    """Verify source URLs are documented."""

    def test_has_source_urls(self):
        m = get_m347()
        urls = m.get("source_urls", m.get("sources", []))
        assert len(urls) >= 4, f"Should have at least 4 source URLs, got {len(urls)}"

    def test_cnn_settlement_urls_present(self):
        m = get_m347()
        urls = str(m.get("source_urls", m.get("sources", [])))
        assert "cnn.com" in urls, "Should include CNN source URLs"

    def test_settlement_and_openai_urls_both_present(self):
        """Both settlement and OpenAI child safety source URLs present."""
        m = get_m347()
        urls = str(m.get("source_urls", m.get("sources", [])))
        assert "settlement" in urls.lower() or "meta-states" in urls.lower(), \
            "Should include settlement article URL"
        assert "openai" in urls.lower() or "florida" in urls.lower() or \
               "chatgpt" in urls.lower(), \
            "Should include OpenAI child safety article URL"


class TestAsymmetryScoreCalibration:
    """Verify asymmetry score is properly calibrated given confounder load."""

    def test_score_below_0_5_with_heavy_confounders(self):
        """Heavy confounder load should keep score below 0.5."""
        m = get_m347()
        score = m.get("asymmetry_score", 0)
        confounders = m.get("confounders", [])
        strong_count = sum(1 for c in confounders
                           if isinstance(c, dict) and c.get("severity", "").upper() == "STRONG")
        if strong_count >= 2:
            assert score < 0.5, \
                f"Score {score} should be below 0.5 with {strong_count} STRONG confounders"

    def test_score_above_0_15(self):
        """Natural experiment quality should keep score above noise floor."""
        m = get_m347()
        score = m.get("asymmetry_score", 0)
        assert score > 0.15, f"Score {score} should be above noise floor (0.15)"

    def test_score_consistent_with_settlement_cluster(self):
        """Score should be in range of other settlement-week mechanisms."""
        m = get_m347()
        score = m.get("asymmetry_score", 0)
        assert 0.15 <= score <= 0.65, \
            f"Score {score} outside settlement-week cluster range (0.15-0.65)"


class TestCNNAnalysisArticleFraming:
    """Test the Aug 27 analysis article's AI pivot framing."""

    def test_meta_ai_pivot_framing_documented(self):
        """CNN frames Meta's AI pivot as business recovery, not liability surface."""
        m = get_m347()
        finding = str(m.get("finding", ""))
        evidence = str(m.get("evidence", ""))
        combined = finding + evidence
        assert "fundamentals" in combined.lower() or "ai pivot" in combined.lower() or \
               "artificial intelligence" in combined.lower(), \
            "Should document CNN's Meta AI pivot framing in analysis article"

    def test_ai_safety_lab_aspirational_framing_documented(self):
        """CNN May 5 frames OpenAI/Anthropic as funders of safety research."""
        m = get_m347()
        finding = str(m.get("finding", ""))
        evidence = str(m.get("evidence", ""))
        combined = finding + evidence
        assert "safety lab" in combined.lower() or "common sense" in combined.lower() or \
               "aspirational" in combined.lower() or "funder" in combined.lower() or \
               "crash test" in combined.lower(), \
            "Should document OpenAI/Anthropic aspirational framing as safety research funders"


class TestSettlementWeekCoverageComparison:
    """Quantitative comparison of CNN coverage volume and depth across entities."""

    def test_meta_vs_openai_article_count_differential(self):
        """CNN published 2+ settlement articles vs 0 OpenAI child safety articles same week."""
        m = get_m347()
        finding = str(m.get("finding", ""))
        evidence = str(m.get("evidence", ""))
        combined = finding + evidence
        assert "two" in combined.lower() or "2" in combined or \
               "multiple" in combined.lower() or "articles" in combined.lower(), \
            "Should document Meta vs OpenAI article count differential"
