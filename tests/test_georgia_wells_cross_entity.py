"""
Cross-entity analysis: Georgia Wells (WSJ) — Dual-Beat AI Governance Reporter

Type B iteration — Journalist Cross-Entity Tracking (Aug 10, 2026 15:00 PT)

Georgia Wells covers BOTH OpenAI governance/regulation AND Meta business AI
at the Wall Street Journal. Unlike beat-siloed reporters (Bobrowsky→Meta,
Berber Jin→AI startups), Wells operates across entity boundaries, making her
a strong control case for whether financial relationships predict individual
reporter behavior.

KEY FINDING: Editorial Independence Under Financial Conflict

Wells co-authored adversarial coverage of OpenAI (state AG investigation,
Jun 13) DESPITE News Corp's $250M+ content licensing deal with OpenAI.
She also co-authored the dramatic "Rogue AI Hacks Herald New Era of Cyber
Chaos" article (Aug 2) — the biggest rogue AI story of 2026 — which
included News Corp's best-in-class financial disclosure.

Her Meta coverage ("Zuckerberg Wants Meta's New AI Agents to Run Your
Whole Business," Jun 3) uses business-expansion framing without adversarial
escalation. The difference in editorial register between her Meta and OpenAI
coverage is primarily explained by story TYPE (business expansion vs
regulatory enforcement), not by the financial relationship.

IMPLICATION: The WSJ's disclosure practice (consistently noting News Corp
licensing deals) correlates with more balanced cross-entity coverage.
This CONTRASTS with publications that lack disclosure (WIRED, Guardian)
and show stronger financial-relationship-predicted asymmetry.

Source URLs:
  - OpenAI AG investigation: https://www.wsj.com/tech/openai-investigated-by-coalition-of-state-attorneys-general-088a3928
  - Rogue AI Hacks: https://www.wsj.com/tech/ai/openai-anthropic-rogue-ai-models-20b6bb3c
  - Meta business AI agents: https://www.wsj.com/tech/mark-zuckerberg-wants-metas-new-ai-agents-to-run-your-whole-business-6e2100e2
  - AI virus: https://www.wsj.com/tech/ai/the-latest-scary-sounding-ai-milestone-a-brand-new-virus-6080b1db
"""

import yaml
import pathlib
import pytest

PROFILES_DIR = pathlib.Path(__file__).resolve().parent.parent / "profiles"


def load_news_corp_profile():
    with open(PROFILES_DIR / "news-corp.yaml") as f:
        return yaml.safe_load(f)


def get_wells_profile(data):
    """Extract Georgia Wells's journalist profile from news-corp.yaml."""
    for jp in data.get("journalist_profiles", []):
        if jp.get("name") == "Georgia Wells":
            return jp
    return None


# ---------------------------------------------------------------------------
# Class 1: Profile structure and existence
# ---------------------------------------------------------------------------
class TestWellsProfileStructure:
    """Verify Georgia Wells's journalist profile exists and is properly structured."""

    def test_profile_exists(self):
        data = load_news_corp_profile()
        profile = get_wells_profile(data)
        assert profile is not None, "Georgia Wells profile missing from news-corp.yaml"

    def test_current_role(self):
        data = load_news_corp_profile()
        profile = get_wells_profile(data)
        assert profile["current_role"] == "ai_governance_reporter"

    def test_publication_is_wsj(self):
        data = load_news_corp_profile()
        profile = get_wells_profile(data)
        assert profile["publication"] == "The Wall Street Journal"

    def test_has_cross_entity_analysis(self):
        data = load_news_corp_profile()
        profile = get_wells_profile(data)
        assert "cross_entity_coverage_analysis" in profile, (
            "Georgia Wells needs cross_entity_coverage_analysis section"
        )

    def test_has_mechanism_id(self):
        data = load_news_corp_profile()
        profile = get_wells_profile(data)
        analysis = profile.get("cross_entity_coverage_analysis", {})
        assert analysis.get("mechanism_id") == 30


# ---------------------------------------------------------------------------
# Class 2: Dual-beat coverage scope
# ---------------------------------------------------------------------------
class TestDualBeatScope:
    """Verify Wells's coverage spans multiple AI entities."""

    def test_covers_openai(self):
        data = load_news_corp_profile()
        profile = get_wells_profile(data)
        analysis = profile["cross_entity_coverage_analysis"]
        assert "openai_coverage" in analysis

    def test_covers_meta(self):
        data = load_news_corp_profile()
        profile = get_wells_profile(data)
        analysis = profile["cross_entity_coverage_analysis"]
        assert "meta_coverage" in analysis

    def test_openai_article_count_ge_2(self):
        data = load_news_corp_profile()
        profile = get_wells_profile(data)
        analysis = profile["cross_entity_coverage_analysis"]
        articles = analysis["openai_coverage"].get("articles", [])
        assert len(articles) >= 2, (
            f"Expected at least 2 OpenAI articles, found {len(articles)}"
        )

    def test_meta_article_count_ge_1(self):
        data = load_news_corp_profile()
        profile = get_wells_profile(data)
        analysis = profile["cross_entity_coverage_analysis"]
        articles = analysis["meta_coverage"].get("articles", [])
        assert len(articles) >= 1, (
            f"Expected at least 1 Meta article, found {len(articles)}"
        )


# ---------------------------------------------------------------------------
# Class 3: OpenAI adversarial coverage despite financial relationship
# ---------------------------------------------------------------------------
class TestOpenAIAdversarialCoverage:
    """Verify Wells wrote adversarial OpenAI coverage despite News Corp deal."""

    def test_ag_investigation_article_exists(self):
        data = load_news_corp_profile()
        profile = get_wells_profile(data)
        articles = profile["cross_entity_coverage_analysis"]["openai_coverage"]["articles"]
        ag_articles = [a for a in articles if "attorney" in a.get("title", "").lower()
                       or "ag" in a.get("topic", "").lower()
                       or "investigated" in a.get("title", "").lower()]
        assert len(ag_articles) >= 1, (
            "Missing OpenAI AG investigation article in Wells's coverage"
        )

    def test_ag_article_tone_is_adversarial(self):
        data = load_news_corp_profile()
        profile = get_wells_profile(data)
        articles = profile["cross_entity_coverage_analysis"]["openai_coverage"]["articles"]
        ag_articles = [a for a in articles if "investigated" in a.get("title", "").lower()]
        assert len(ag_articles) >= 1
        tone = ag_articles[0].get("tone_category", "")
        assert tone in ("adversarial", "regulatory_enforcement"), (
            f"AG investigation tone should be adversarial or regulatory, got: {tone}"
        )

    def test_rogue_ai_article_exists(self):
        data = load_news_corp_profile()
        profile = get_wells_profile(data)
        articles = profile["cross_entity_coverage_analysis"]["openai_coverage"]["articles"]
        rogue = [a for a in articles if "rogue" in a.get("title", "").lower()
                 or "cyber chaos" in a.get("title", "").lower()]
        assert len(rogue) >= 1, (
            "Missing rogue AI article in Wells's OpenAI coverage"
        )

    def test_rogue_ai_article_has_disclosure(self):
        data = load_news_corp_profile()
        profile = get_wells_profile(data)
        articles = profile["cross_entity_coverage_analysis"]["openai_coverage"]["articles"]
        rogue = [a for a in articles if "rogue" in a.get("title", "").lower()
                 or "cyber chaos" in a.get("title", "").lower()]
        assert len(rogue) >= 1
        assert rogue[0].get("includes_news_corp_disclosure") is True, (
            "Rogue AI article should include News Corp-OpenAI disclosure"
        )

    def test_editorial_independence_finding(self):
        """Wells covers OpenAI adversarially despite News Corp's $250M+ deal."""
        data = load_news_corp_profile()
        profile = get_wells_profile(data)
        analysis = profile["cross_entity_coverage_analysis"]
        finding = analysis.get("key_finding", "")
        assert "independence" in finding.lower() or "despite" in finding.lower(), (
            "Key finding should document editorial independence from financial conflict"
        )


# ---------------------------------------------------------------------------
# Class 4: Meta coverage register
# ---------------------------------------------------------------------------
class TestMetaCoverageRegister:
    """Verify Wells's Meta coverage uses business-expansion register."""

    def test_meta_business_article_exists(self):
        data = load_news_corp_profile()
        profile = get_wells_profile(data)
        articles = profile["cross_entity_coverage_analysis"]["meta_coverage"]["articles"]
        business = [a for a in articles if "business" in a.get("title", "").lower()
                    or "agent" in a.get("title", "").lower()]
        assert len(business) >= 1

    def test_meta_tone_is_neutral(self):
        data = load_news_corp_profile()
        profile = get_wells_profile(data)
        meta_cov = profile["cross_entity_coverage_analysis"]["meta_coverage"]
        tone = meta_cov.get("average_tone_category", "")
        assert tone in ("neutral", "balanced", "business_reporting"), (
            f"Meta coverage tone should be neutral/balanced, got: {tone}"
        )

    def test_meta_no_adversarial_escalation(self):
        """Wells's Meta coverage should not use adversarial escalation language."""
        data = load_news_corp_profile()
        profile = get_wells_profile(data)
        meta_cov = profile["cross_entity_coverage_analysis"]["meta_coverage"]
        assert meta_cov.get("adversarial_escalation") is False


# ---------------------------------------------------------------------------
# Class 5: Cross-entity comparison
# ---------------------------------------------------------------------------
class TestCrossEntityComparison:
    """Verify the cross-entity comparison documents register differences."""

    def test_register_difference_explained_by_story_type(self):
        """Any editorial register difference should be attributed to story type,
        not financial relationship."""
        data = load_news_corp_profile()
        profile = get_wells_profile(data)
        analysis = profile["cross_entity_coverage_analysis"]
        explanation = analysis.get("register_difference_explanation", "")
        assert "story type" in explanation.lower() or "topic" in explanation.lower(), (
            "Register differences should be explained by story type/topic"
        )

    def test_financial_relationship_not_predictive(self):
        data = load_news_corp_profile()
        profile = get_wells_profile(data)
        analysis = profile["cross_entity_coverage_analysis"]
        assert analysis.get("financial_relationship_predictive") is False, (
            "For Wells, financial relationship should NOT predict coverage direction"
        )

    def test_disclosure_practice_correlation(self):
        """WSJ's disclosure practice should be noted as correlating with balanced coverage."""
        data = load_news_corp_profile()
        profile = get_wells_profile(data)
        analysis = profile["cross_entity_coverage_analysis"]
        disclosure_note = analysis.get("disclosure_correlation", "")
        assert len(disclosure_note) > 50, (
            "Should document correlation between WSJ disclosure and balanced coverage"
        )


# ---------------------------------------------------------------------------
# Class 6: Assignment pattern
# ---------------------------------------------------------------------------
class TestAssignmentPattern:
    """Document the reporter assignment pattern for rogue AI coverage."""

    def test_rogue_ai_team_size_documented(self):
        """The OpenAI/Anthropic rogue AI article had 3 reporters; Meta had 1."""
        data = load_news_corp_profile()
        profile = get_wells_profile(data)
        analysis = profile["cross_entity_coverage_analysis"]
        pattern = analysis.get("assignment_pattern", {})
        assert pattern.get("openai_rogue_ai_reporters") == 3
        assert pattern.get("meta_rogue_ai_reporters") == 1

    def test_assignment_difference_legitimate(self):
        """The assignment difference has legitimate editorial explanation."""
        data = load_news_corp_profile()
        profile = get_wells_profile(data)
        analysis = profile["cross_entity_coverage_analysis"]
        pattern = analysis.get("assignment_pattern", {})
        factors = pattern.get("legitimate_factors", [])
        assert len(factors) >= 2, (
            "Should document at least 2 legitimate factors for assignment difference"
        )

    def test_wells_not_on_meta_rogue_ai(self):
        """Wells was on OpenAI rogue AI article but NOT Meta rogue AI article."""
        data = load_news_corp_profile()
        profile = get_wells_profile(data)
        analysis = profile["cross_entity_coverage_analysis"]
        pattern = analysis.get("assignment_pattern", {})
        assert pattern.get("wells_on_openai_rogue_ai") is True
        assert pattern.get("wells_on_meta_rogue_ai") is False


# ---------------------------------------------------------------------------
# Class 7: Structural consistency with existing profiles
# ---------------------------------------------------------------------------
class TestStructuralConsistency:
    """Verify Wells's profile follows the same structure as other WSJ profiles."""

    def test_has_source_urls(self):
        data = load_news_corp_profile()
        profile = get_wells_profile(data)
        analysis = profile["cross_entity_coverage_analysis"]
        urls = analysis.get("source_urls", [])
        assert len(urls) >= 3, f"Expected at least 3 source URLs, found {len(urls)}"

    def test_has_legitimate_factors(self):
        data = load_news_corp_profile()
        profile = get_wells_profile(data)
        analysis = profile["cross_entity_coverage_analysis"]
        factors = analysis.get("legitimate_factors", [])
        assert len(factors) >= 4, (
            f"Expected at least 4 legitimate factors, found {len(factors)}"
        )

    def test_has_test_file_reference(self):
        data = load_news_corp_profile()
        profile = get_wells_profile(data)
        analysis = profile["cross_entity_coverage_analysis"]
        assert analysis.get("test_file") == "tests/test_georgia_wells_cross_entity.py"

    def test_has_test_count(self):
        data = load_news_corp_profile()
        profile = get_wells_profile(data)
        analysis = profile["cross_entity_coverage_analysis"]
        assert analysis.get("test_count") >= 28
