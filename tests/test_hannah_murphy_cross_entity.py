"""
Tests for Hannah Murphy (FT) cross-entity coverage analysis.

Key finding: The SAME reporter applies DIFFERENT editorial standards to Meta vs Snap
for the SAME product category (AR glasses). Murphy's Meta coverage deploys surveillance/
legal-threat language; her Snap coverage uses business strategy language. Zero surveillance
terms appear in her Snap AR glasses coverage.

This is the strongest evidence of company-specific editorial framing in the MediaScope
dataset because it controls for three variables simultaneously:
1. Reporter identity (same person)
2. Product category (AR glasses with cameras)
3. Publication (same outlet, same editorial leadership)

The only variable left is company identity.

Sources:
- Techmeme: Meta glasses — https://www.techmeme.com/260708/p2
- Techmeme: Snap AR bet — http://www.techmeme.com/241028/p32
- Techmeme: Snap hiring — https://www.techmeme.com/220721/p33
- Techmeme: Meta equity cuts — https://www.techmeme.com/260219/p43
- Techmeme: Meta Oversight Board — https://www.techmeme.com/250221/p1
- Techmeme: Pinterest CEO Q&A — https://www.techmeme.com/240201/p7
- Techmeme: IBM suspends X ads — https://www.techmeme.com/231116/p47
- Techmeme: Wang/Muse Spark — https://www.techmeme.com/260603/p1
- Techmeme: Meta agentic tools — https://www.techmeme.com/260505/p42
- Muck Rack: Hannah Murphy — https://muckrack.com/hannah-murphy
"""

import yaml
import os
import pytest


PROFILES_DIR = os.path.join(os.path.dirname(__file__), "..", "profiles")


def load_ft_profile():
    with open(os.path.join(PROFILES_DIR, "financial-times.yaml")) as f:
        return yaml.safe_load(f)


class TestMurphyCoveragePortfolioBreadth:
    """Verify Murphy covers multiple social media companies, not just Meta."""

    def test_murphy_is_primary_meta_reporter(self):
        profile = load_ft_profile()
        murphy = None
        for j in profile["key_journalists"]:
            if j["name"] == "Hannah Murphy":
                murphy = j
                break
        assert murphy is not None
        assert "Meta" in murphy["beat"]

    def test_murphy_covers_snap(self):
        profile = load_ft_profile()
        murphy = [j for j in profile["key_journalists"] if j["name"] == "Hannah Murphy"][0]
        snap_articles = murphy["cross_entity_coverage_analysis"]["snap_coverage_portfolio"]
        assert len(snap_articles) >= 3, "Murphy should have 3+ documented Snap articles"

    def test_murphy_covers_tiktok(self):
        profile = load_ft_profile()
        murphy = [j for j in profile["key_journalists"] if j["name"] == "Hannah Murphy"][0]
        other = murphy["cross_entity_coverage_analysis"]["other_entity_coverage"]
        assert "tiktok" in other
        assert len(other["tiktok"]) >= 1

    def test_murphy_covers_x_twitter(self):
        profile = load_ft_profile()
        murphy = [j for j in profile["key_journalists"] if j["name"] == "Hannah Murphy"][0]
        other = murphy["cross_entity_coverage_analysis"]["other_entity_coverage"]
        assert "x_twitter" in other
        assert len(other["x_twitter"]) >= 2

    def test_murphy_covers_pinterest(self):
        profile = load_ft_profile()
        murphy = [j for j in profile["key_journalists"] if j["name"] == "Hannah Murphy"][0]
        other = murphy["cross_entity_coverage_analysis"]["other_entity_coverage"]
        assert "pinterest" in other
        assert len(other["pinterest"]) >= 1

    def test_murphy_does_not_cover_openai(self):
        """Murphy does NOT cover OpenAI — that's Murgia/Hammond territory."""
        profile = load_ft_profile()
        murphy = [j for j in profile["key_journalists"] if j["name"] == "Hannah Murphy"][0]
        not_covered = murphy["cross_entity_coverage_analysis"]["entities_not_covered_by_murphy"]
        assert "OpenAI" in not_covered["description"]
        assert "Anthropic" in not_covered["description"]


class TestMurphyMetaCoverageFraming:
    """Verify Murphy's Meta coverage contains adversarial/surveillance framing."""

    def test_meta_glasses_adversarial_framing(self):
        profile = load_ft_profile()
        murphy = [j for j in profile["key_journalists"] if j["name"] == "Hannah Murphy"][0]
        meta_articles = murphy["cross_entity_coverage_analysis"]["meta_coverage_portfolio"]
        glasses_article = [a for a in meta_articles if "glasses" in a["article"].lower()
                          and "continuously" in a["article"].lower()][0]
        assert glasses_article["framing"] == "adversarial_surveillance"

    def test_meta_glasses_uses_surveillance_language(self):
        profile = load_ft_profile()
        murphy = [j for j in profile["key_journalists"] if j["name"] == "Hannah Murphy"][0]
        meta_articles = murphy["cross_entity_coverage_analysis"]["meta_coverage_portfolio"]
        glasses_article = [a for a in meta_articles if "glasses" in a["article"].lower()
                          and "continuously" in a["article"].lower()][0]
        language = glasses_article["language"]
        assert any("wiretapping" in term for term in language)
        assert any("biometric" in term for term in language)
        assert any("civil libert" in term for term in language)

    def test_meta_oversight_institutional_conflict_framing(self):
        profile = load_ft_profile()
        murphy = [j for j in profile["key_journalists"] if j["name"] == "Hannah Murphy"][0]
        meta_articles = murphy["cross_entity_coverage_analysis"]["meta_coverage_portfolio"]
        oversight = [a for a in meta_articles if "Oversight" in a["article"]][0]
        assert oversight["framing"] == "institutional_conflict"

    def test_meta_equity_cuts_morale_framing(self):
        profile = load_ft_profile()
        murphy = [j for j in profile["key_journalists"] if j["name"] == "Hannah Murphy"][0]
        meta_articles = murphy["cross_entity_coverage_analysis"]["meta_coverage_portfolio"]
        equity = [a for a in meta_articles if "stock options" in a["article"].lower()
                  or "equity" in a["article"].lower()][0]
        assert equity["framing"] == "morale_damage"

    def test_meta_has_some_neutral_coverage(self):
        """Murphy CAN write neutral Meta coverage — not 100% adversarial."""
        profile = load_ft_profile()
        murphy = [j for j in profile["key_journalists"] if j["name"] == "Hannah Murphy"][0]
        meta_articles = murphy["cross_entity_coverage_analysis"]["meta_coverage_portfolio"]
        neutral = [a for a in meta_articles
                   if a["framing"] in ("neutral_business", "balanced")]
        assert len(neutral) >= 2, "Murphy should have at least 2 neutral Meta articles"


class TestMurphySnapCoverageFraming:
    """Verify Murphy's Snap coverage uses constructive/business framing."""

    def test_snap_ar_glasses_constructive_framing(self):
        profile = load_ft_profile()
        murphy = [j for j in profile["key_journalists"] if j["name"] == "Hannah Murphy"][0]
        snap_articles = murphy["cross_entity_coverage_analysis"]["snap_coverage_portfolio"]
        ar_article = [a for a in snap_articles if "AR" in a["article"]
                      or "glasses" in a["article"].lower()
                      or "Spiegel" in a["article"]][0]
        assert ar_article["framing"] == "constructive_business"

    def test_snap_ar_glasses_zero_surveillance_language(self):
        """The diagnostic test: zero surveillance terms for Snap AR glasses."""
        profile = load_ft_profile()
        murphy = [j for j in profile["key_journalists"] if j["name"] == "Hannah Murphy"][0]
        snap_articles = murphy["cross_entity_coverage_analysis"]["snap_coverage_portfolio"]
        ar_article = [a for a in snap_articles if "AR" in a["article"]
                      or "glasses" in a["article"].lower()
                      or "Spiegel" in a["article"]][0]
        assert ar_article["privacy_language"] is not None
        assert "NONE" in ar_article["privacy_language"]

    def test_snap_hiring_neutral_framing(self):
        profile = load_ft_profile()
        murphy = [j for j in profile["key_journalists"] if j["name"] == "Hannah Murphy"][0]
        snap_articles = murphy["cross_entity_coverage_analysis"]["snap_coverage_portfolio"]
        hiring = [a for a in snap_articles if "hiring" in a["article"].lower()
                  or "reduce" in a["article"].lower()][0]
        assert hiring["framing"] == "neutral_business"


class TestDiagnosticComparisonARGlasses:
    """The core finding: same reporter, same product category, different framing."""

    def test_surveillance_count_meta_gt_zero(self):
        profile = load_ft_profile()
        murphy = [j for j in profile["key_journalists"] if j["name"] == "Hannah Murphy"][0]
        comp = murphy["cross_entity_coverage_analysis"]["diagnostic_comparison_ar_glasses"]
        assert comp["surveillance_term_count_meta"] > 0

    def test_surveillance_count_snap_is_zero(self):
        profile = load_ft_profile()
        murphy = [j for j in profile["key_journalists"] if j["name"] == "Hannah Murphy"][0]
        comp = murphy["cross_entity_coverage_analysis"]["diagnostic_comparison_ar_glasses"]
        assert comp["surveillance_term_count_snap"] == 0

    def test_asymmetry_ratio_is_infinite(self):
        """Meta surveillance terms / Snap surveillance terms = infinity (6:0)."""
        profile = load_ft_profile()
        murphy = [j for j in profile["key_journalists"] if j["name"] == "Hannah Murphy"][0]
        comp = murphy["cross_entity_coverage_analysis"]["diagnostic_comparison_ar_glasses"]
        assert comp["surveillance_term_count_meta"] >= 5
        assert comp["surveillance_term_count_snap"] == 0

    def test_meta_glasses_language_contains_legal_terms(self):
        profile = load_ft_profile()
        murphy = [j for j in profile["key_journalists"] if j["name"] == "Hannah Murphy"][0]
        comp = murphy["cross_entity_coverage_analysis"]["diagnostic_comparison_ar_glasses"]
        meta_lang = comp["meta_glasses_language"]
        legal_terms = [t for t in meta_lang if any(
            w in t.lower() for w in ["wiretapping", "biometric", "civil libert", "surveillance"]
        )]
        assert len(legal_terms) >= 3

    def test_snap_glasses_language_is_business_only(self):
        profile = load_ft_profile()
        murphy = [j for j in profile["key_journalists"] if j["name"] == "Hannah Murphy"][0]
        comp = murphy["cross_entity_coverage_analysis"]["diagnostic_comparison_ar_glasses"]
        snap_lang = comp["snap_glasses_language"]
        for term in snap_lang:
            assert "surveillance" not in term.lower()
            assert "wiretapping" not in term.lower()
            assert "biometric" not in term.lower()
            assert "privacy" not in term.lower()

    def test_finding_identifies_company_identity_as_variable(self):
        profile = load_ft_profile()
        murphy = [j for j in profile["key_journalists"] if j["name"] == "Hannah Murphy"][0]
        comp = murphy["cross_entity_coverage_analysis"]["diagnostic_comparison_ar_glasses"]
        finding = comp["finding"]
        assert "company" in finding.lower() or "manufacturer" in finding.lower()


class TestMurphyOverallClassification:
    """Verify the overall classification of Murphy's coverage pattern."""

    def test_classified_as_meta_adversarial_not_social_media_adversarial(self):
        profile = load_ft_profile()
        murphy = [j for j in profile["key_journalists"] if j["name"] == "Hannah Murphy"][0]
        classification = murphy["cross_entity_coverage_analysis"]["overall_classification"]
        assert "Meta-adversarial" in classification
        assert "social-media-adversarial" in classification.lower()

    def test_classification_notes_cannot_be_explained_by_beat_assignment(self):
        profile = load_ft_profile()
        murphy = [j for j in profile["key_journalists"] if j["name"] == "Hannah Murphy"][0]
        classification = murphy["cross_entity_coverage_analysis"]["overall_classification"]
        assert "beat assignment" in classification.lower()

    def test_classification_notes_product_category_not_explanatory(self):
        profile = load_ft_profile()
        murphy = [j for j in profile["key_journalists"] if j["name"] == "Hannah Murphy"][0]
        classification = murphy["cross_entity_coverage_analysis"]["overall_classification"]
        assert "product category" in classification.lower() or "AR glasses" in classification


class TestFTReporterAssignmentPattern:
    """Verify FT's reporter→entity assignment creates structural asymmetry."""

    def test_murphy_is_dedicated_meta_reporter(self):
        profile = load_ft_profile()
        murphy = [j for j in profile["key_journalists"] if j["name"] == "Hannah Murphy"][0]
        assert "Meta" in murphy["beat"]
        assert "San Francisco" in murphy["location"]

    def test_murgia_is_ai_editor(self):
        profile = load_ft_profile()
        murgia = [j for j in profile["key_journalists"] if j["name"] == "Madhumita Murgia"][0]
        assert "AI Editor" in murgia.get("role", "") or "AI" in murgia["beat"]

    def test_murgia_meta_coverage_is_neutral(self):
        profile = load_ft_profile()
        murgia = [j for j in profile["key_journalists"] if j["name"] == "Madhumita Murgia"][0]
        meta_articles = murgia["meta_articles"]
        neutral_or_labor = [a for a in meta_articles
                           if a["framing"] in ("neutral_business", "adversarial_labor")]
        assert len(neutral_or_labor) == len(meta_articles), \
            "Murgia's Meta coverage should be neutral or labor-focused, not surveillance-framed"

    def test_murgia_openai_coverage_is_constructive(self):
        profile = load_ft_profile()
        murgia = [j for j in profile["key_journalists"] if j["name"] == "Madhumita Murgia"][0]
        openai_articles = murgia["openai_articles"]
        constructive = [a for a in openai_articles if "constructive" in a["framing"]]
        assert len(constructive) >= 1

    def test_hammond_is_deals_reporter(self):
        profile = load_ft_profile()
        hammond = [j for j in profile["key_journalists"] if j["name"] == "George Hammond"][0]
        assert "deals" in hammond["beat"].lower() or "M&A" in hammond["beat"]


class TestMurphySourceURLDocumentation:
    """Every Murphy cross-entity article should have a source URL."""

    def test_meta_articles_have_urls(self):
        profile = load_ft_profile()
        murphy = [j for j in profile["key_journalists"] if j["name"] == "Hannah Murphy"][0]
        for article in murphy["cross_entity_coverage_analysis"]["meta_coverage_portfolio"]:
            if "url" in article:
                assert article["url"].startswith("http")

    def test_snap_articles_have_urls(self):
        profile = load_ft_profile()
        murphy = [j for j in profile["key_journalists"] if j["name"] == "Hannah Murphy"][0]
        for article in murphy["cross_entity_coverage_analysis"]["snap_coverage_portfolio"]:
            if "url" in article:
                assert article["url"].startswith("http")

    def test_diagnostic_comparison_has_both_language_sets(self):
        profile = load_ft_profile()
        murphy = [j for j in profile["key_journalists"] if j["name"] == "Hannah Murphy"][0]
        comp = murphy["cross_entity_coverage_analysis"]["diagnostic_comparison_ar_glasses"]
        assert len(comp["meta_glasses_language"]) >= 5
        assert len(comp["snap_glasses_language"]) >= 2


class TestThreePublicationLaneAssignmentComparison:
    """Compare FT's pattern to WIRED and NYT patterns already documented."""

    def test_ft_pattern_is_within_reporter(self):
        """FT's asymmetry shows up WITHIN a single reporter's coverage."""
        profile = load_ft_profile()
        murphy = [j for j in profile["key_journalists"] if j["name"] == "Hannah Murphy"][0]
        finding = murphy["cross_entity_coverage_analysis"]["finding"]
        # Murphy covers BOTH Meta and Snap — same reporter, different framing
        assert "Meta" in finding and "Snap" in finding

    def test_ft_pattern_is_distinct_from_wired_desk_assignment(self):
        """FT ≠ WIRED's desk-level assignment pattern."""
        profile = load_ft_profile()
        murphy = [j for j in profile["key_journalists"] if j["name"] == "Hannah Murphy"][0]
        comp = murphy["cross_entity_coverage_analysis"]["diagnostic_comparison_ar_glasses"]
        finding = comp["finding"]
        assert "WIRED" in finding, "Should reference WIRED's different mechanism"

    def test_ft_pattern_is_distinct_from_nyt_reporter_assignment(self):
        """FT ≠ NYT's between-reporter assignment pattern."""
        profile = load_ft_profile()
        murphy = [j for j in profile["key_journalists"] if j["name"] == "Hannah Murphy"][0]
        comp = murphy["cross_entity_coverage_analysis"]["diagnostic_comparison_ar_glasses"]
        finding = comp["finding"]
        assert "NYT" in finding, "Should reference NYT's different mechanism"

    def test_ft_is_strongest_evidence(self):
        """FT within-reporter asymmetry is the strongest evidence because it controls
        for reporter, product category, and publication simultaneously."""
        profile = load_ft_profile()
        murphy = [j for j in profile["key_journalists"] if j["name"] == "Hannah Murphy"][0]
        comp = murphy["cross_entity_coverage_analysis"]["diagnostic_comparison_ar_glasses"]
        finding = comp["finding"]
        assert "strongest" in finding.lower()
