"""
Mechanism #54: FT Capital-Raise Framing Asymmetry — Anthropic (Aspiration) vs Meta (Desperation)

Natural experiment: The Financial Times broke exclusive stories on BOTH Anthropic and Meta
raising massive capital in H1 2026. The framing divergence is stark:

Anthropic raises (FT as primary source):
  - Jan 27: $20B raise at $350B valuation — "six times the interest originally expected"
  - Apr 14: Investor comparison piece — Anthropic as "relative bargain," demand "insatiable"
  - May 7-8: $50B at ~$900B valuation — "inbound investment offers," "investors ready to throw
    any dollar amount"
  - May 15: $30B closed at $900B — "strong investor demand," "came together in weeks"
  Language: confidence, momentum, validation, growth trajectory

Meta raise (FT as primary source):
  - Jun 5: Equity raise exploration — "exploring 'creative' ways to raise cash," "seeks new
    sources of capital," "premature to conclude Meta had settled on a financing strategy"
  Language: uncertainty, desperation, financial stress
  Market impact: Meta stock dropped 6.6% on the FT report

Financial context: FT has a confirmed OpenAI content licensing deal (announced Apr 29, 2024
by FT's own AI Editor Madhumita Murgia). Anthropic is a content licensor to publishers.
Meta ended Facebook News payments in 2022 and pays publishers $0.

The asymmetry is NOT "FT protects OpenAI" (FT was neutral-to-negative about OpenAI in the
Apr 14 piece where investors had "second thoughts"). The asymmetry is: FT frames the
AI lab ecosystem (which pays for content) aspirationally, while framing Meta (which doesn't)
as financially stressed — even when both are doing fundamentally the same thing: raising
tens of billions of dollars for AI infrastructure.

Sources:
- Reuters: https://www.reuters.com/technology/meta-weighs-big-equity-raising-finance-ai-infrastructure-ft-reports-2026-06-05/
- Reuters: https://www.reuters.com/world/asia-pacific/sequoia-join-gic-coatue-anthropic-investment-ft-reports-2026-01-18/
- TechCrunch: https://techcrunch.com/2026/04/14/anthropics-rise-is-giving-some-openai-investors-second-thoughts/
- TechCrunch: https://techcrunch.com/2026/04/30/anthropic-potential-900b-valuation-round-could-happen-within-two-weeks/
- Morningstar: https://www.morningstar.com/news/dow-jones/202606056054/meta-platforms-slips-on-report-of-plans-for-multibillion-dollar-offering-to-fund-ai-buildout
- PYMNTS: https://www.pymnts.com/artificial-intelligence-2/2026/anthropic-close-to-finalizing-fundraising-deal-at-350-billion-valuation/
- Intellectia: (FT $50B/$900B source)
"""

import pytest
import yaml
import os
import glob


# ─────────────────────────────────────────────────────────────────────
#  Helpers
# ─────────────────────────────────────────────────────────────────────

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


def _load_yaml(filename):
    path = os.path.join(PROFILES_DIR, filename)
    with open(path) as f:
        return yaml.safe_load(f)


def _load_competitor_coverage():
    return _load_yaml('competitor-coverage-research.yaml')


def _load_ft_profile():
    return _load_yaml('financial-times.yaml')


def _load_competitor_entities():
    return _load_yaml('competitor-entities.yaml')


# ─────────────────────────────────────────────────────────────────────
#  1. Mechanism exists and is correctly located
# ─────────────────────────────────────────────────────────────────────

class TestMechanism54Exists:
    """Verify mechanism #54 is present in cross_publication_findings."""

    def test_mechanism_in_cpf(self):
        data = _load_competitor_coverage()
        cpf = data.get('cross_publication_findings', {})
        found = any(
            v.get('mechanism_id') == 54
            for v in cpf.values()
            if isinstance(v, dict)
        )
        assert found, "Mechanism #54 not found in cross_publication_findings"

    def test_mechanism_key_name(self):
        data = _load_competitor_coverage()
        cpf = data.get('cross_publication_findings', {})
        assert 'ft_anthropic_meta_capital_raise_framing_asymmetry' in cpf, \
            "Expected key 'ft_anthropic_meta_capital_raise_framing_asymmetry' in cpf"

    def test_has_date_added(self):
        data = _load_competitor_coverage()
        cpf = data.get('cross_publication_findings', {})
        entry = cpf.get('ft_anthropic_meta_capital_raise_framing_asymmetry', {})
        assert entry.get('date_added'), "Missing date_added"

    def test_has_discovery_date(self):
        data = _load_competitor_coverage()
        cpf = data.get('cross_publication_findings', {})
        entry = cpf.get('ft_anthropic_meta_capital_raise_framing_asymmetry', {})
        assert entry.get('discovery_date'), "Missing discovery_date"

    def test_finding_type_is_competitor_coverage(self):
        data = _load_competitor_coverage()
        cpf = data.get('cross_publication_findings', {})
        entry = cpf.get('ft_anthropic_meta_capital_raise_framing_asymmetry', {})
        assert entry.get('finding_type') == 'competitor_coverage_deep_dive'

    def test_rotation_type_is_a(self):
        data = _load_competitor_coverage()
        cpf = data.get('cross_publication_findings', {})
        entry = cpf.get('ft_anthropic_meta_capital_raise_framing_asymmetry', {})
        assert entry.get('rotation_type') == 'A'


# ─────────────────────────────────────────────────────────────────────
#  2. Anthropic capital-raise framing language
# ─────────────────────────────────────────────────────────────────────

class TestAnthropicFramingLanguage:
    """FT's Anthropic fundraising coverage uses aspiration/confidence framing."""

    def test_anthropic_raises_documented(self):
        data = _load_competitor_coverage()
        cpf = data.get('cross_publication_findings', {})
        entry = cpf.get('ft_anthropic_meta_capital_raise_framing_asymmetry', {})
        raises = entry.get('anthropic_capital_events', [])
        assert len(raises) >= 3, f"Expected >=3 Anthropic events, got {len(raises)}"

    def test_anthropic_jan_raise_amount(self):
        data = _load_competitor_coverage()
        cpf = data.get('cross_publication_findings', {})
        entry = cpf.get('ft_anthropic_meta_capital_raise_framing_asymmetry', {})
        raises = entry.get('anthropic_capital_events', [])
        jan_raises = [r for r in raises if '2026-01' in str(r.get('date', ''))]
        assert len(jan_raises) >= 1, "Missing January 2026 Anthropic raise"
        assert any('20' in str(r.get('amount_billions', '')) or r.get('amount_billions', 0) == 20
                   for r in jan_raises), "January raise should be $20B"

    def test_anthropic_may_valuation(self):
        data = _load_competitor_coverage()
        cpf = data.get('cross_publication_findings', {})
        entry = cpf.get('ft_anthropic_meta_capital_raise_framing_asymmetry', {})
        raises = entry.get('anthropic_capital_events', [])
        may_raises = [r for r in raises if '2026-05' in str(r.get('date', ''))]
        assert len(may_raises) >= 1, "Missing May 2026 Anthropic raise"
        assert any(r.get('valuation_billions', 0) >= 900 for r in may_raises), \
            "May raise should reflect $900B+ valuation"

    def test_aspiration_language_documented(self):
        data = _load_competitor_coverage()
        cpf = data.get('cross_publication_findings', {})
        entry = cpf.get('ft_anthropic_meta_capital_raise_framing_asymmetry', {})
        lang = entry.get('anthropic_framing_language', [])
        assert len(lang) >= 3, f"Expected >=3 aspiration language examples, got {len(lang)}"

    def test_no_desperation_language_for_anthropic(self):
        """Anthropic framing should NOT include desperation/stress vocabulary."""
        data = _load_competitor_coverage()
        cpf = data.get('cross_publication_findings', {})
        entry = cpf.get('ft_anthropic_meta_capital_raise_framing_asymmetry', {})
        lang = entry.get('anthropic_framing_language', [])
        desperation_words = ['creative ways', 'new sources', 'premature', 'speculation']
        for phrase in lang:
            phrase_lower = phrase.lower() if isinstance(phrase, str) else ''
            for word in desperation_words:
                assert word not in phrase_lower, \
                    f"Desperation language '{word}' found in Anthropic framing: {phrase}"


# ─────────────────────────────────────────────────────────────────────
#  3. Meta capital-raise framing language
# ─────────────────────────────────────────────────────────────────────

class TestMetaFramingLanguage:
    """FT's Meta equity raise coverage uses desperation/uncertainty framing."""

    def test_meta_raise_documented(self):
        data = _load_competitor_coverage()
        cpf = data.get('cross_publication_findings', {})
        entry = cpf.get('ft_anthropic_meta_capital_raise_framing_asymmetry', {})
        meta_event = entry.get('meta_capital_event', {})
        assert meta_event, "Missing meta_capital_event"

    def test_meta_raise_date(self):
        data = _load_competitor_coverage()
        cpf = data.get('cross_publication_findings', {})
        entry = cpf.get('ft_anthropic_meta_capital_raise_framing_asymmetry', {})
        meta_event = entry.get('meta_capital_event', {})
        assert '2026-06' in str(meta_event.get('date', '')), "Meta raise should be June 2026"

    def test_meta_stock_impact(self):
        """FT's Meta report caused 6.6% stock drop — market interpreted it negatively."""
        data = _load_competitor_coverage()
        cpf = data.get('cross_publication_findings', {})
        entry = cpf.get('ft_anthropic_meta_capital_raise_framing_asymmetry', {})
        meta_event = entry.get('meta_capital_event', {})
        impact = meta_event.get('stock_impact_percent', 0)
        assert abs(impact) >= 5, f"Expected >=5% stock impact, got {impact}"

    def test_desperation_language_documented(self):
        data = _load_competitor_coverage()
        cpf = data.get('cross_publication_findings', {})
        entry = cpf.get('ft_anthropic_meta_capital_raise_framing_asymmetry', {})
        lang = entry.get('meta_framing_language', [])
        assert len(lang) >= 3, f"Expected >=3 desperation language examples, got {len(lang)}"

    def test_creative_ways_phrase(self):
        """The 'exploring creative ways to raise cash' phrase implies desperation."""
        data = _load_competitor_coverage()
        cpf = data.get('cross_publication_findings', {})
        entry = cpf.get('ft_anthropic_meta_capital_raise_framing_asymmetry', {})
        lang = entry.get('meta_framing_language', [])
        combined = ' '.join(str(l).lower() for l in lang)
        assert 'creative' in combined, "Missing 'creative ways' desperation language"


# ─────────────────────────────────────────────────────────────────────
#  4. Structural comparison — same activity, different framing
# ─────────────────────────────────────────────────────────────────────

class TestStructuralComparison:
    """Both companies were doing the same thing: raising billions for AI."""

    def test_both_raising_billions(self):
        data = _load_competitor_coverage()
        cpf = data.get('cross_publication_findings', {})
        entry = cpf.get('ft_anthropic_meta_capital_raise_framing_asymmetry', {})
        summary = entry.get('finding_summary', '')
        assert 'tens of billions' in summary.lower() or 'billion' in summary.lower()

    def test_same_purpose_ai_infrastructure(self):
        data = _load_competitor_coverage()
        cpf = data.get('cross_publication_findings', {})
        entry = cpf.get('ft_anthropic_meta_capital_raise_framing_asymmetry', {})
        summary = entry.get('finding_summary', '')
        assert 'ai' in summary.lower(), "Should mention AI as the purpose for both raises"

    def test_temporal_proximity(self):
        """Both events within ~5 months of each other (Jan-Jun 2026)."""
        data = _load_competitor_coverage()
        cpf = data.get('cross_publication_findings', {})
        entry = cpf.get('ft_anthropic_meta_capital_raise_framing_asymmetry', {})
        assert entry.get('temporal_window_months', 0) <= 6, \
            "Events should be within 6-month window"

    def test_ft_was_primary_source_for_both(self):
        """FT broke both stories — this is not about different source access."""
        data = _load_competitor_coverage()
        cpf = data.get('cross_publication_findings', {})
        entry = cpf.get('ft_anthropic_meta_capital_raise_framing_asymmetry', {})
        assert entry.get('ft_primary_source_both'), \
            "FT should be marked as primary source for both stories"

    def test_framing_delta_documented(self):
        """The framing delta should be quantified or described."""
        data = _load_competitor_coverage()
        cpf = data.get('cross_publication_findings', {})
        entry = cpf.get('ft_anthropic_meta_capital_raise_framing_asymmetry', {})
        delta = entry.get('framing_delta', {})
        assert delta.get('anthropic_tone', '') in ['aspirational', 'positive', 'confident']
        assert delta.get('meta_tone', '') in ['desperation', 'uncertain', 'negative', 'stressed']


# ─────────────────────────────────────────────────────────────────────
#  5. Financial relationship context
# ─────────────────────────────────────────────────────────────────────

class TestFinancialRelationshipContext:
    """FT's financial relationships predict the framing asymmetry."""

    def test_ft_openai_deal_documented(self):
        data = _load_competitor_coverage()
        cpf = data.get('cross_publication_findings', {})
        entry = cpf.get('ft_anthropic_meta_capital_raise_framing_asymmetry', {})
        fin = entry.get('financial_context', {})
        assert fin.get('ft_openai_deal'), "Should document FT-OpenAI deal"

    def test_anthropic_is_content_licensor(self):
        data = _load_competitor_coverage()
        cpf = data.get('cross_publication_findings', {})
        entry = cpf.get('ft_anthropic_meta_capital_raise_framing_asymmetry', {})
        fin = entry.get('financial_context', {})
        assert fin.get('anthropic_content_licensor'), \
            "Should note Anthropic is a content licensor to publishers"

    def test_meta_zero_publisher_payments(self):
        data = _load_competitor_coverage()
        cpf = data.get('cross_publication_findings', {})
        entry = cpf.get('ft_anthropic_meta_capital_raise_framing_asymmetry', {})
        fin = entry.get('financial_context', {})
        assert fin.get('meta_publisher_payments_post_2022') == 0 or \
               str(fin.get('meta_publisher_payments_post_2022', '')).lower() in ['0', 'zero', '$0']

    def test_ecosystem_alignment_not_company_specific(self):
        """Key insight: asymmetry is ecosystem-level, not company-level protection."""
        data = _load_competitor_coverage()
        cpf = data.get('cross_publication_findings', {})
        entry = cpf.get('ft_anthropic_meta_capital_raise_framing_asymmetry', {})
        insight = entry.get('structural_insight', '')
        assert 'ecosystem' in insight.lower(), \
            "Should document that the asymmetry is ecosystem-level"

    def test_ft_not_protecting_openai_specifically(self):
        """FT covered OpenAI negatively in Apr 14 piece — rules out pure OpenAI protection."""
        data = _load_competitor_coverage()
        cpf = data.get('cross_publication_findings', {})
        entry = cpf.get('ft_anthropic_meta_capital_raise_framing_asymmetry', {})
        assert entry.get('ft_openai_negative_coverage_documented'), \
            "Should document FT's negative OpenAI coverage as counterevidence"


# ─────────────────────────────────────────────────────────────────────
#  6. Confounding factors
# ─────────────────────────────────────────────────────────────────────

class TestConfoundingFactors:
    """At least 5 legitimate confounding factors with rebuttals."""

    def test_minimum_confounding_factors(self):
        data = _load_competitor_coverage()
        cpf = data.get('cross_publication_findings', {})
        entry = cpf.get('ft_anthropic_meta_capital_raise_framing_asymmetry', {})
        factors = entry.get('confounding_factors', [])
        assert len(factors) >= 5, f"Expected >=5 confounding factors, got {len(factors)}"

    def test_each_factor_has_rebuttal(self):
        data = _load_competitor_coverage()
        cpf = data.get('cross_publication_findings', {})
        entry = cpf.get('ft_anthropic_meta_capital_raise_framing_asymmetry', {})
        factors = entry.get('confounding_factors', [])
        for i, f in enumerate(factors):
            assert f.get('rebuttal'), f"Factor {i} missing rebuttal: {f.get('factor', '')}"

    @pytest.mark.parametrize("factor_keyword", [
        "private vs public",
        "dilution",
        "growth rate",
        "profitability",
        "track record",
    ])
    def test_key_confounds_addressed(self, factor_keyword):
        """Each major confound should be addressed somewhere in the factors list."""
        data = _load_competitor_coverage()
        cpf = data.get('cross_publication_findings', {})
        entry = cpf.get('ft_anthropic_meta_capital_raise_framing_asymmetry', {})
        factors = entry.get('confounding_factors', [])
        combined = ' '.join(
            str(f.get('factor', '')) + ' ' + str(f.get('rebuttal', ''))
            for f in factors
        ).lower()
        assert factor_keyword.lower() in combined, \
            f"Confounding factor '{factor_keyword}' not addressed"


# ─────────────────────────────────────────────────────────────────────
#  7. Testable predictions
# ─────────────────────────────────────────────────────────────────────

class TestTestablePredictions:
    """Mechanism must include falsifiable predictions."""

    def test_has_testable_prediction(self):
        data = _load_competitor_coverage()
        cpf = data.get('cross_publication_findings', {})
        entry = cpf.get('ft_anthropic_meta_capital_raise_framing_asymmetry', {})
        pred = entry.get('testable_prediction', '')
        assert len(pred) > 50, "Testable prediction too short or missing"

    def test_prediction_includes_falsification(self):
        data = _load_competitor_coverage()
        cpf = data.get('cross_publication_findings', {})
        entry = cpf.get('ft_anthropic_meta_capital_raise_framing_asymmetry', {})
        pred = entry.get('testable_prediction', '').lower()
        assert 'fail' in pred or 'revision' in pred or 'falsif' in pred or 'wrong' in pred, \
            "Prediction should include falsification criteria"


# ─────────────────────────────────────────────────────────────────────
#  8. Source URLs
# ─────────────────────────────────────────────────────────────────────

class TestSourceUrls:
    """Must include verifiable source URLs."""

    def test_has_source_urls(self):
        data = _load_competitor_coverage()
        cpf = data.get('cross_publication_findings', {})
        entry = cpf.get('ft_anthropic_meta_capital_raise_framing_asymmetry', {})
        urls = entry.get('source_urls', [])
        assert len(urls) >= 4, f"Expected >=4 source URLs, got {len(urls)}"

    def test_includes_reuters_meta_source(self):
        data = _load_competitor_coverage()
        cpf = data.get('cross_publication_findings', {})
        entry = cpf.get('ft_anthropic_meta_capital_raise_framing_asymmetry', {})
        urls = entry.get('source_urls', [])
        assert any('reuters.com' in u and 'meta' in u.lower() for u in urls), \
            "Should include Reuters source for Meta equity raise"

    def test_includes_anthropic_source(self):
        data = _load_competitor_coverage()
        cpf = data.get('cross_publication_findings', {})
        entry = cpf.get('ft_anthropic_meta_capital_raise_framing_asymmetry', {})
        urls = entry.get('source_urls', [])
        assert any('anthropic' in u.lower() for u in urls), \
            "Should include source URL for Anthropic coverage"


# ─────────────────────────────────────────────────────────────────────
#  9. Cross-reference with FT profile
# ─────────────────────────────────────────────────────────────────────

class TestFTProfileConsistency:
    """Mechanism should be cross-referenced in FT profile."""

    def test_ft_profile_references_mechanism(self):
        ft = _load_ft_profile()
        # Check for mechanism #54 reference anywhere in the profile
        ft_str = yaml.dump(ft)
        assert '54' in ft_str, "FT profile should reference mechanism #54"

    def test_ft_has_openai_deal_documented(self):
        ft = _load_ft_profile()
        ft_str = yaml.dump(ft).lower()
        assert 'openai' in ft_str and 'deal' in ft_str, \
            "FT profile should document OpenAI content deal"


# ─────────────────────────────────────────────────────────────────────
#  10. Test file metadata
# ─────────────────────────────────────────────────────────────────────

class TestMetadata:
    """Mechanism metadata matches test file."""

    def test_test_file_reference(self):
        data = _load_competitor_coverage()
        cpf = data.get('cross_publication_findings', {})
        entry = cpf.get('ft_anthropic_meta_capital_raise_framing_asymmetry', {})
        expected = 'tests/test_ft_anthropic_meta_capital_raise_framing_asymmetry_aug11.py'
        assert entry.get('test_file') == expected

    def test_test_count_matches(self):
        """Test count in YAML should match actual test count in this file."""
        import re
        data = _load_competitor_coverage()
        cpf = data.get('cross_publication_findings', {})
        entry = cpf.get('ft_anthropic_meta_capital_raise_framing_asymmetry', {})
        # Count tests in this file using same regex as structural consistency test
        test_file = os.path.join(os.path.dirname(__file__),
                                 'test_ft_anthropic_meta_capital_raise_framing_asymmetry_aug11.py')
        with open(test_file) as f:
            content = f.read()
        test_count = len(re.findall(r'^\s+def test_', content, re.MULTILINE))
        claimed = entry.get('test_count', 0)
        assert claimed == test_count, \
            f"YAML claims {claimed} tests but file has {test_count}"
