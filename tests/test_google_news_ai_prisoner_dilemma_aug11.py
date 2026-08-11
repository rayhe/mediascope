"""
Tests for Mechanism #50: Google News AI Prisoner's Dilemma — CMA Regulatory Arbitrage

Finding: Google's News AI pilot has enrolled 200+ publications globally (confirmed
Aug 4, 2026 by Press Gazette), converting the Showcase dependency relationship into
AI training rights extraction at scale. Industry insiders characterize the dynamics
as a "prisoner's dilemma." The UK CMA's world-first opt-out ruling is effectively
neutralized by Google's financial leverage.

Source: https://pressgazette.co.uk/news/google-ai-deals-uk-publishers/
Date: August 4, 2026
"""

import yaml
import os
import pytest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_yaml(filename):
    path = os.path.join(REPO_ROOT, "profiles", filename)
    with open(path, "r") as f:
        return yaml.safe_load(f)


# ──────────────────────────────────────────────────────────────────────
# Class 1: Core Mechanism Definition
# ──────────────────────────────────────────────────────────────────────

class TestMechanismDefinition:
    """Verify mechanism #50 is properly defined in competitor-coverage-research.yaml."""

    @pytest.fixture(autouse=True)
    def setup(self):
        self.research = load_yaml("competitor-coverage-research.yaml")
        self.cpf = self.research.get("cross_publication_findings", {})
        self.entry = self.cpf.get("google_news_ai_prisoner_dilemma_regulatory_arbitrage", {})

    def test_mechanism_exists(self):
        assert "google_news_ai_prisoner_dilemma_regulatory_arbitrage" in self.cpf

    def test_mechanism_id_is_50(self):
        assert self.entry.get("mechanism_id") == 50

    def test_mechanism_has_finding_summary(self):
        summary = self.entry.get("finding_summary", "")
        assert len(summary) > 100, "Finding summary should be substantive"

    def test_mechanism_type_is_financial(self):
        assert self.entry.get("finding_type") == "financial_incentive_mapping"

    def test_entities_include_google_and_meta(self):
        entities = self.entry.get("entities", [])
        assert "Google" in entities
        assert "Meta" in entities

    def test_date_added(self):
        date_val = self.entry.get("date_added")
        assert str(date_val) == "2026-08-11"

    def test_has_source_urls(self):
        urls = self.entry.get("source_urls", [])
        assert len(urls) >= 3, "Need at least 3 source URLs"

    def test_press_gazette_source_included(self):
        urls = self.entry.get("source_urls", [])
        assert any("pressgazette" in u for u in urls), \
            "Press Gazette (primary source) must be cited"


# ──────────────────────────────────────────────────────────────────────
# Class 2: Prisoner's Dilemma Game Theory Validation
# ──────────────────────────────────────────────────────────────────────

class TestPrisonersDilemmaLogic:
    """Verify the prisoner's dilemma characterization is documented with evidence."""

    @pytest.fixture(autouse=True)
    def setup(self):
        self.research = load_yaml("competitor-coverage-research.yaml")
        self.cpf = self.research.get("cross_publication_findings", {})
        self.entry = self.cpf.get("google_news_ai_prisoner_dilemma_regulatory_arbitrage", {})
        self.summary = self.entry.get("finding_summary", "")

    def test_prisoner_dilemma_mentioned(self):
        assert "prisoner" in self.summary.lower(), \
            "Finding must reference prisoner's dilemma game theory"

    def test_competitor_pressure_documented(self):
        assert "competitor" in self.summary.lower(), \
            "Finding must document competitor pressure dynamics"

    def test_industry_source_attribution(self):
        # The characterization comes from industry insiders, not our analysis
        assert "industry" in self.summary.lower() or "insider" in self.summary.lower() or \
            "source" in self.summary.lower(), \
            "Prisoner's dilemma framing must be attributed to industry sources"

    def test_no_upside_to_opting_out(self):
        """The core game theory: individual publishers cannot rationally refuse."""
        assert "opt out" in self.summary.lower() or "refusing" in self.summary.lower() or \
            "rationally" in self.summary.lower(), \
            "Must document that opting out is individually irrational"


# ──────────────────────────────────────────────────────────────────────
# Class 3: Scale Confirmation — 200+ Publications
# ──────────────────────────────────────────────────────────────────────

class TestScaleConfirmation:
    """Verify Google News AI pilot scale data is accurately documented."""

    @pytest.fixture(autouse=True)
    def setup(self):
        self.entities = load_yaml("competitor-entities.yaml")
        self.google = self.entities.get("entities", {}).get("google", {})
        self.coercive = self.google.get("showcase_coercive_cycle", {})
        self.stage4 = self.coercive.get("stage_4_scale_confirmation_aug2026", {})

    def test_stage_4_exists(self):
        assert self.stage4, "Stage 4 (scale confirmation) must exist in Google entity"

    def test_news_ai_pilot_count(self):
        count = self.stage4.get("news_ai_pilot_global_count")
        assert count is not None, "News AI pilot count must be documented"
        assert "200" in str(count), "200+ publications confirmed by Google spokesperson"

    def test_showcase_count(self):
        count = self.stage4.get("showcase_global_count")
        assert count == 2800, "2,800 Showcase publications confirmed by Google"

    def test_showcase_countries(self):
        countries = self.stage4.get("showcase_countries")
        assert countries == 33, "33 countries confirmed by Google spokesperson"

    def test_date_confirmed(self):
        assert self.stage4.get("date_confirmed") == "2026-08-04"

    def test_source_is_press_gazette(self):
        assert self.stage4.get("source") == "Press Gazette"


# ──────────────────────────────────────────────────────────────────────
# Class 4: UK Market Dominance Data
# ──────────────────────────────────────────────────────────────────────

class TestUKMarketDominance:
    """Verify UK-specific market data showing Google's dominance."""

    @pytest.fixture(autouse=True)
    def setup(self):
        self.entities = load_yaml("competitor-entities.yaml")
        self.google = self.entities.get("entities", {}).get("google", {})
        self.coercive = self.google.get("showcase_coercive_cycle", {})
        self.stage4 = self.coercive.get("stage_4_scale_confirmation_aug2026", {})
        self.uk = self.stage4.get("uk_market_dominance", {})

    def test_google_uk_page_views(self):
        views = self.uk.get("google_uk_page_views_apr_2026_b")
        assert views == 36, "36 billion UK page views in April 2026"

    def test_google_uk_page_views_growth(self):
        growth = self.uk.get("google_uk_page_views_yoy_pct")
        assert growth == 31, "31% YoY growth in UK page views"

    def test_google_vs_publishers_comparison(self):
        comp = self.uk.get("google_uk_page_views_vs_next", "")
        assert "24" in str(comp), "More than next 24 publishers combined"

    def test_google_uk_adspend(self):
        adspend = self.uk.get("google_uk_adspend_2025_b_gbp")
        assert adspend == 21.5, "£21.5B Google UK ad spend"

    def test_newsbrands_adspend_declining(self):
        ns_pct = self.uk.get("newsbrands_magazines_adspend_yoy_pct")
        assert ns_pct < 0, "Newsbrands ad spend must be declining"

    def test_adspend_ratio(self):
        """Google's UK ad spend is ~20x publisher ad spend."""
        google = self.uk.get("google_uk_adspend_2025_b_gbp", 0)
        pubs = self.uk.get("newsbrands_magazines_adspend_b_gbp", 1)
        ratio = google / pubs
        assert ratio >= 15, f"Google/publisher ad spend ratio is {ratio:.1f}x, expected 15x+"


# ──────────────────────────────────────────────────────────────────────
# Class 5: UK Deal Terms
# ──────────────────────────────────────────────────────────────────────

class TestUKDealTerms:
    """Verify the reported UK deal structure."""

    @pytest.fixture(autouse=True)
    def setup(self):
        self.entities = load_yaml("competitor-entities.yaml")
        self.google = self.entities.get("entities", {}).get("google", {})
        self.coercive = self.google.get("showcase_coercive_cycle", {})
        self.stage4 = self.coercive.get("stage_4_scale_confirmation_aug2026", {})
        self.terms = self.stage4.get("uk_deal_terms", {})

    def test_duration(self):
        assert self.terms.get("duration_years") == 2

    def test_exit_clause(self):
        assert self.terms.get("exit_clause_days") == 90

    def test_nda_clauses(self):
        assert self.terms.get("nda_clauses") is True

    def test_no_sue_clauses(self):
        assert self.terms.get("no_sue_clauses") is True

    def test_guardian_revenue_documented(self):
        rev = self.terms.get("guardian_annual_revenue", "")
        assert "million" in rev.lower() or "single figure" in rev.lower()

    def test_ft_revenue_documented(self):
        rev = self.terms.get("ft_annual_revenue", "")
        assert "million" in rev.lower() or "single figure" in rev.lower()


# ──────────────────────────────────────────────────────────────────────
# Class 6: CMA Regulatory Arbitrage
# ──────────────────────────────────────────────────────────────────────

class TestCMARegulationArbitrage:
    """Verify the CMA ruling undermining is documented."""

    @pytest.fixture(autouse=True)
    def setup(self):
        self.entities = load_yaml("competitor-entities.yaml")
        self.google = self.entities.get("entities", {}).get("google", {})
        self.coercive = self.google.get("showcase_coercive_cycle", {})
        self.stage4 = self.coercive.get("stage_4_scale_confirmation_aug2026", {})
        self.cma = self.stage4.get("cma_regulatory_arbitrage", {})

    def test_cma_section_exists(self):
        assert self.cma, "CMA regulatory arbitrage section must exist"

    def test_cma_ruling_date(self):
        assert self.cma.get("cma_ruling_date") == "2026-06-03"

    def test_ruling_undermined_flag(self):
        assert self.cma.get("ruling_undermined") is True

    def test_detail_explains_mechanism(self):
        detail = self.cma.get("detail", "")
        assert len(detail) > 100, "CMA detail must explain the arbitrage mechanism"
        assert "prisoner" in detail.lower() or "opt" in detail.lower(), \
            "Detail must reference opt-out dynamics or prisoner's dilemma"


# ──────────────────────────────────────────────────────────────────────
# Class 7: Industry Characterization Quotes
# ──────────────────────────────────────────────────────────────────────

class TestIndustryCharacterization:
    """Verify industry source quotes are properly documented."""

    @pytest.fixture(autouse=True)
    def setup(self):
        self.entities = load_yaml("competitor-entities.yaml")
        self.google = self.entities.get("entities", {}).get("google", {})
        self.coercive = self.google.get("showcase_coercive_cycle", {})
        self.stage4 = self.coercive.get("stage_4_scale_confirmation_aug2026", {})
        self.chars = self.stage4.get("industry_characterization", {})

    def test_prisoner_dilemma_quote(self):
        pd = self.chars.get("prisoner_dilemma", "")
        assert "no upside" in pd.lower() or "saying no" in pd.lower(), \
            "Prisoner's dilemma quote must include 'no upside to saying no'"

    def test_no_sue_deals_quote(self):
        nsd = self.chars.get("no_sue_deals", "")
        assert "renting peace" in nsd.lower(), \
            "No-sue deals quote must include 'renting peace'"

    def test_divide_and_rule_characterization(self):
        dar = self.chars.get("divide_and_rule", "")
        assert "divide" in dar.lower(), \
            "Divide and rule characterization must be documented"

    def test_chinnappa_quote(self):
        c = self.chars.get("chinnappa_long_term", "")
        assert "short term" in c.lower() or "long term" in c.lower(), \
            "Chinnappa quote must contrast short-term vs long-term"


# ──────────────────────────────────────────────────────────────────────
# Class 8: Meta Coercion Comparison
# ──────────────────────────────────────────────────────────────────────

class TestMetaCoercionComparison:
    """Verify the Google vs Meta coercion asymmetry is documented."""

    @pytest.fixture(autouse=True)
    def setup(self):
        self.entities = load_yaml("competitor-entities.yaml")
        self.google = self.entities.get("entities", {}).get("google", {})
        self.coercive = self.google.get("showcase_coercive_cycle", {})

    def test_google_coercion_count(self):
        count = self.coercive.get("google_coercion_count", 0)
        assert count >= 5, f"Google has {count} coercive mechanisms, expected 5+"

    def test_meta_coercion_count_zero(self):
        count = self.coercive.get("meta_coercion_count", -1)
        assert count == 0, "Meta must have ZERO coercive mechanisms"

    def test_meta_contrast_documented(self):
        contrast = self.coercive.get("meta_contrast", "")
        assert len(contrast) > 100, "Meta contrast must be documented"
        assert "voluntary" in contrast.lower() or "ZERO" in contrast, \
            "Must specify Meta deals are voluntary with zero coercion"

    def test_coverage_paradox_documented(self):
        paradox = self.coercive.get("coverage_paradox", "")
        assert len(paradox) > 100, "Coverage paradox must be documented"
        assert "safe target" in paradox.lower() or "adversarial" in paradox.lower()


# ──────────────────────────────────────────────────────────────────────
# Class 9: Confounding Factors
# ──────────────────────────────────────────────────────────────────────

class TestConfoundingFactors:
    """Verify confounding factors are documented with rebuttals."""

    @pytest.fixture(autouse=True)
    def setup(self):
        self.research = load_yaml("competitor-coverage-research.yaml")
        self.cpf = self.research.get("cross_publication_findings", {})
        self.entry = self.cpf.get("google_news_ai_prisoner_dilemma_regulatory_arbitrage", {})
        self.factors = self.entry.get("confounding_factors", [])

    def test_has_confounding_factors(self):
        assert len(self.factors) >= 4, "Need at least 4 confounding factors"

    def test_each_factor_has_rebuttal(self):
        for i, factor in enumerate(self.factors):
            assert "factor" in factor, f"Factor {i} missing 'factor' field"
            assert "rebuttal" in factor, f"Factor {i} missing 'rebuttal' field"
            assert len(factor["rebuttal"]) > 50, f"Factor {i} rebuttal too short"

    def test_genuine_product_value_addressed(self):
        factors_text = " ".join(f.get("factor", "") for f in self.factors)
        assert "benefit" in factors_text.lower() or "product" in factors_text.lower(), \
            "Must address whether deals have genuine product value for publishers"

    def test_meta_controversy_alternative_addressed(self):
        factors_text = " ".join(f.get("factor", "") for f in self.factors)
        assert "meta" in factors_text.lower(), \
            "Must address alternative that Meta generates more controversies"


# ──────────────────────────────────────────────────────────────────────
# Class 10: Testable Predictions
# ──────────────────────────────────────────────────────────────────────

class TestTestablePredictions:
    """Verify mechanism includes falsifiable predictions."""

    @pytest.fixture(autouse=True)
    def setup(self):
        self.research = load_yaml("competitor-coverage-research.yaml")
        self.cpf = self.research.get("cross_publication_findings", {})
        self.entry = self.cpf.get("google_news_ai_prisoner_dilemma_regulatory_arbitrage", {})
        self.prediction = self.entry.get("testable_prediction", "")

    def test_has_testable_prediction(self):
        assert len(self.prediction) > 100, "Must have substantive testable prediction"

    def test_prediction_includes_timeline(self):
        assert "2027" in self.prediction or "month" in self.prediction.lower(), \
            "Prediction must include a timeline for verification"

    def test_prediction_is_falsifiable(self):
        assert "fail" in self.prediction.lower() or "revision" in self.prediction.lower(), \
            "Prediction must state what would falsify the mechanism"

    def test_prediction_addresses_enrollment_growth(self):
        assert "500" in self.prediction or "enrollment" in self.prediction.lower() or \
            "pilot" in self.prediction.lower(), \
            "Prediction must address expected enrollment trajectory"

    def test_prediction_addresses_publisher_withdrawal(self):
        assert "withdraw" in self.prediction.lower() or "zero" in self.prediction.lower(), \
            "Prediction must address whether publishers will withdraw"
