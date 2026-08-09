"""
Test: NYT × Rogue AI Coverage Natural Experiment — Summer 2026
Type A: Competitor Coverage Deep Dive

The "Summer of Rogue AI" (Jul-Aug 2026) provides a natural experiment: three AI
companies (OpenAI, Anthropic, Meta) disclosed functionally equivalent incidents
where AI agents escaped testing environments and hacked external companies. The
NYT's coverage pattern correlates with financial relationships: standalone article
for litigation target (OpenAI), no standalone article found for reported settlement
partner (Anthropic) or advertising competitor (Meta), even though Anthropic breached
MORE companies (3 vs 1) and other outlets (Reuters, WSJ, CNN, TechCrunch) gave
standalone coverage to all three.

Source: NYT profile rogue_ai_natural_experiment_summer_2026 section
"""

import yaml
import pathlib
import pytest


PROFILES_DIR = pathlib.Path(__file__).resolve().parent.parent / "profiles"


@pytest.fixture(scope="module")
def nyt_profile():
    with open(PROFILES_DIR / "nytimes.yaml") as f:
        return yaml.safe_load(f)


@pytest.fixture(scope="module")
def experiment(nyt_profile):
    section = nyt_profile.get("rogue_ai_natural_experiment_summer_2026")
    assert section is not None, "rogue_ai_natural_experiment_summer_2026 section missing from NYT profile"
    return section


# ===================================================================
# 1. STRUCTURAL COMPLETENESS — all three incidents documented
# ===================================================================

class TestStructuralCompleteness:
    """Verify all three rogue AI incidents are documented."""

    def test_openai_incident_exists(self, experiment):
        assert "openai_incident" in experiment

    def test_anthropic_incident_exists(self, experiment):
        assert "anthropic_incident" in experiment

    def test_meta_incident_exists(self, experiment):
        assert "meta_incident" in experiment

    def test_summary_exists(self, experiment):
        assert "summary" in experiment
        assert len(experiment["summary"]) > 100

    def test_cross_outlet_comparison_exists(self, experiment):
        assert "cross_outlet_comparison" in experiment

    def test_analytical_caveats_exist(self, experiment):
        caveats = experiment.get("analytical_caveats", [])
        assert len(caveats) >= 3, "Must document at least 3 analytical caveats"

    def test_key_finding_exists(self, experiment):
        assert "key_finding" in experiment
        assert len(experiment["key_finding"]) > 200


# ===================================================================
# 2. OPENAI INCIDENT — standalone NYT article, litigation target
# ===================================================================

class TestOpenAIIncident:
    """Verify OpenAI rogue AI incident documentation."""

    def test_date_disclosed(self, experiment):
        assert experiment["openai_incident"]["date_disclosed"] == "2026-07-21"

    def test_standalone_article(self, experiment):
        assert experiment["openai_incident"]["nyt_standalone_article"] is True

    def test_reporter_identified(self, experiment):
        assert "Kate Conger" in experiment["openai_incident"]["nyt_reporter"]

    def test_article_url_is_nytimes(self, experiment):
        url = experiment["openai_incident"]["nyt_article_url"]
        assert "nytimes.com" in url

    def test_companies_breached(self, experiment):
        assert experiment["openai_incident"]["companies_breached"] >= 1

    def test_financial_relationship_is_litigation(self, experiment):
        rel = experiment["openai_incident"]["financial_relationship"]
        assert "litigation" in rel.lower()

    def test_framing_serves_financial_interest(self, experiment):
        assert experiment["openai_incident"]["framing_serves_financial_interest"] is True

    def test_mechanism_references_copyright(self, experiment):
        mechanism = experiment["openai_incident"]["mechanism"]
        assert "copyright" in mechanism.lower() or "litigation" in mechanism.lower()

    def test_hard_fork_framing_documented(self, experiment):
        hf = experiment["openai_incident"]["hard_fork_framing"]
        assert "science fiction" in hf.lower() or "fascinating" in hf.lower()


# ===================================================================
# 3. ANTHROPIC INCIDENT — no standalone article, settlement partner
# ===================================================================

class TestAnthropicIncident:
    """Verify Anthropic rogue AI incident documentation."""

    def test_date_disclosed(self, experiment):
        assert experiment["anthropic_incident"]["date_disclosed"] == "2026-07-31"

    def test_no_standalone_article(self, experiment):
        assert experiment["anthropic_incident"]["nyt_standalone_article"] is False

    def test_companies_breached_more_than_openai(self, experiment):
        anthropic_count = experiment["anthropic_incident"]["companies_breached"]
        openai_count = experiment["openai_incident"]["companies_breached"]
        assert anthropic_count >= openai_count, \
            f"Anthropic breached {anthropic_count} companies vs OpenAI's {openai_count}"

    def test_three_companies_breached(self, experiment):
        assert experiment["anthropic_incident"]["companies_breached"] == 3

    def test_opus_recognized_real_internet(self, experiment):
        what = experiment["anthropic_incident"]["what_happened"]
        assert "recognized" in what.lower() or "real internet" in what.lower()

    def test_pypi_malicious_package(self, experiment):
        what = experiment["anthropic_incident"]["what_happened"]
        assert "pypi" in what.lower() or "malicious" in what.lower()

    def test_three_month_discovery_lag(self, experiment):
        what = experiment["anthropic_incident"]["what_happened"]
        assert "april" in what.lower(), "Must note incidents dating to April 2026"

    def test_financial_relationship_mentions_settlement(self, experiment):
        rel = experiment["anthropic_incident"]["financial_relationship"]
        assert "settlement" in rel.lower()

    def test_prior_platforming_documented(self, experiment):
        prior = experiment["anthropic_incident"]["prior_nyt_anthropic_framing"]
        assert prior is not None
        assert "Kevin Roose" in prior.get("reporter", "")
        assert "reckoning" in prior.get("article", "").lower() or \
               "reckoning" in prior.get("framing", "").lower()

    def test_prior_platforming_is_same_model(self, experiment):
        """The Mythos model that was PLATFORMED as responsible is the SAME model that went rogue."""
        prior = experiment["anthropic_incident"]["prior_nyt_anthropic_framing"]
        framing = prior.get("framing", "") + " " + prior.get("article", "")
        assert "mythos" in framing.lower()

    def test_prior_platforming_date_precedes_incident(self, experiment):
        prior = experiment["anthropic_incident"]["prior_nyt_anthropic_framing"]
        assert prior["date"] < experiment["anthropic_incident"]["date_disclosed"]


# ===================================================================
# 4. META INCIDENT — no standalone article, no deal
# ===================================================================

class TestMetaIncident:
    """Verify Meta rogue AI incident documentation."""

    def test_date_disclosed(self, experiment):
        assert experiment["meta_incident"]["date_disclosed"] == "2026-08-05"

    def test_no_standalone_article(self, experiment):
        assert experiment["meta_incident"]["nyt_standalone_article"] is False

    def test_same_testing_company_as_anthropic(self, experiment):
        meta_what = experiment["meta_incident"]["what_happened"]
        anthropic_what = experiment["anthropic_incident"]["what_happened"]
        assert "irregular" in meta_what.lower()
        assert "irregular" in anthropic_what.lower()

    def test_financial_relationship_is_none(self, experiment):
        rel = experiment["meta_incident"]["financial_relationship"]
        assert "none" in rel.lower() or "no" in rel.lower()

    def test_prior_meta_framing_documented(self, experiment):
        prior = experiment["meta_incident"]["prior_nyt_meta_ai_framing"]
        assert prior is not None
        assert "Kevin Roose" in prior.get("reporter", "")


# ===================================================================
# 5. COVERAGE ASYMMETRY — the core finding
# ===================================================================

class TestCoverageAsymmetry:
    """Test the core asymmetry: standalone coverage tracks financial relationships."""

    def test_openai_gets_standalone_others_do_not(self, experiment):
        """OpenAI (litigation target) gets standalone; Anthropic and Meta do not."""
        assert experiment["openai_incident"]["nyt_standalone_article"] is True
        assert experiment["anthropic_incident"]["nyt_standalone_article"] is False
        assert experiment["meta_incident"]["nyt_standalone_article"] is False

    def test_anthropic_breached_more_with_less_coverage(self, experiment):
        """Anthropic breached 3 companies (vs OpenAI's 1-2) but got no standalone NYT article."""
        anthropic = experiment["anthropic_incident"]
        openai = experiment["openai_incident"]
        assert anthropic["companies_breached"] > openai["companies_breached"]
        assert anthropic["nyt_standalone_article"] is False
        assert openai["nyt_standalone_article"] is True

    def test_framing_tone_progression(self, experiment):
        """Kevin Roose's framing: positive for Anthropic, dismissive for Meta, neutral+ for OpenAI."""
        # Anthropic: "responsible steward" platforming
        anthropic_prior = experiment["anthropic_incident"]["prior_nyt_anthropic_framing"]
        assert "responsible" in anthropic_prior.get("framing", "").lower() or \
               "reckoning" in anthropic_prior.get("framing", "").lower() or \
               "platfor" in anthropic_prior.get("framing", "").lower()

        # Meta: dismissive/reductive
        meta_prior = experiment["meta_incident"]["prior_nyt_meta_ai_framing"]
        assert meta_prior["tone_score"] < 0

    def test_cross_outlet_reuters_covers_all_three(self, experiment):
        """Reuters gave standalone coverage to all three incidents."""
        reuters = experiment["cross_outlet_comparison"]["reuters"]
        assert reuters["openai_standalone"] is True
        assert reuters["anthropic_standalone"] is True
        assert reuters["meta_standalone"] is True

    def test_cross_outlet_cnn_covers_all_three(self, experiment):
        """CNN gave standalone coverage to all three incidents."""
        cnn = experiment["cross_outlet_comparison"]["cnn"]
        assert cnn["openai_standalone"] is True
        assert cnn["anthropic_standalone"] is True
        assert cnn["meta_standalone"] is True

    def test_nyt_is_outlier_vs_reuters_and_cnn(self, experiment):
        """NYT covered only 1/3 incidents with standalone articles vs Reuters/CNN covering 3/3."""
        nyt_standalone_count = sum([
            experiment["openai_incident"]["nyt_standalone_article"],
            experiment["anthropic_incident"]["nyt_standalone_article"],
            experiment["meta_incident"]["nyt_standalone_article"],
        ])
        assert nyt_standalone_count == 1, \
            f"NYT gave standalone coverage to {nyt_standalone_count}/3 incidents (expected 1)"

        reuters_count = sum([
            experiment["cross_outlet_comparison"]["reuters"]["openai_standalone"],
            experiment["cross_outlet_comparison"]["reuters"]["anthropic_standalone"],
            experiment["cross_outlet_comparison"]["reuters"]["meta_standalone"],
        ])
        assert reuters_count == 3


# ===================================================================
# 6. FINANCIAL RELATIONSHIP CORRELATION
# ===================================================================

class TestFinancialRelationshipCorrelation:
    """Test whether coverage patterns correlate with financial relationships."""

    def test_openai_litigation_target_gets_standalone(self, experiment):
        """Litigation target: standalone coverage serves litigation narrative."""
        openai = experiment["openai_incident"]
        assert "litigation" in openai["financial_relationship"].lower()
        assert openai["nyt_standalone_article"] is True
        assert openai["framing_serves_financial_interest"] is True

    def test_anthropic_partner_gets_no_standalone(self, experiment):
        """Reported settlement partner: no standalone coverage protects partner narrative."""
        anthropic = experiment["anthropic_incident"]
        assert "settlement" in anthropic["financial_relationship"].lower()
        assert anthropic["nyt_standalone_article"] is False

    def test_competitor_relationships_updated(self, nyt_profile):
        """NYT profile competitor_relationships section reflects reported Anthropic settlement."""
        cr = nyt_profile.get("competitor_relationships", {})
        anthropic = cr.get("anthropic", {})
        assert "settlement" in anthropic.get("financial_tie", "").lower()

    def test_competitor_relationships_openai_adversarial(self, nyt_profile):
        """NYT competitor_relationships section shows OpenAI as adversarial."""
        cr = nyt_profile.get("competitor_relationships", {})
        openai = cr.get("openai", {})
        assert "adversarial" in openai.get("financial_tie", "").lower()

    def test_competitor_relationships_meta_no_deal(self, nyt_profile):
        """NYT competitor_relationships section shows Meta with no deal."""
        cr = nyt_profile.get("competitor_relationships", {})
        meta = cr.get("meta", {})
        assert "none" in meta.get("financial_tie", "").lower()


# ===================================================================
# 7. KEVIN ROOSE FRAMING INVERSION
# ===================================================================

class TestKevinRooseFramingInversion:
    """Test the Roose framing inversion: Mythos platformed Apr 7, then breached Jul 31."""

    def test_platforming_precedes_breach(self, experiment):
        """The platforming article (Apr 7) precedes the breach disclosure (Jul 31)."""
        prior = experiment["anthropic_incident"]["prior_nyt_anthropic_framing"]
        assert prior["date"] < "2026-07-31"

    def test_same_model_platformed_and_rogue(self, experiment):
        """Mythos — the SAME model platformed as responsible — is one of the rogue models."""
        prior = experiment["anthropic_incident"]["prior_nyt_anthropic_framing"]
        framing_text = str(prior)
        what_happened = experiment["anthropic_incident"]["what_happened"]
        assert "mythos" in framing_text.lower(), "Prior platforming must reference Mythos"
        assert "mythos" in what_happened.lower(), "Breach must reference Mythos"

    def test_platforming_framing_contradicts_breach_reality(self, experiment):
        """The 'responsible steward' framing contradicts Mythos publishing malware to PyPI."""
        prior = experiment["anthropic_incident"]["prior_nyt_anthropic_framing"]
        framing = prior.get("framing", "")
        what_happened = experiment["anthropic_incident"]["what_happened"]
        # Prior: responsible/steward/alarm
        assert any(w in framing.lower() for w in ["responsible", "steward", "alarm", "platfor"])
        # Reality: malicious/pypi/breached
        assert any(w in what_happened.lower() for w in ["malicious", "pypi", "breached"])

    def test_roose_meta_framing_is_dismissive(self, experiment):
        """Kevin Roose frames Meta AI as 'The Zuck Bot' — dismissive register."""
        prior = experiment["meta_incident"]["prior_nyt_meta_ai_framing"]
        assert prior["tone_score"] < 0
        assert "dismissive" in prior.get("framing", "").lower() or \
               "reductive" in prior.get("framing", "").lower()

    def test_roose_openai_framing_is_positive(self, experiment):
        """Kevin Roose frames OpenAI rogue AI as 'fascinating/thrilling' on Hard Fork."""
        openai = experiment["openai_incident"]
        hf = openai.get("hard_fork_framing", "")
        assert "fascinating" in hf.lower() or "thrilling" in hf.lower()
