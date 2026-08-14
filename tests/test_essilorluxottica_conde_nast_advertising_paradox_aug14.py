"""
Mechanism #103: EssilorLuxottica-Condé Nast Cross-Subsidiary Advertising Paradox
— Parent-Level Advertising Revenue vs. WIRED Editorial Adversarialism

Finding: EssilorLuxottica spends ~€1.8-2B/yr on advertising and marketing
(H1 2023: €828M on €12.85B revenue = 6.4%), with Ray-Ban and Oakley as its
top-performing brands. A significant portion flows to fashion/lifestyle
publications including Condé Nast titles (Vogue, GQ, Vanity Fair, Architectural
Digest). Oakley maintained a DIRECT "global brand alliance" with WIRED
(co-created and sponsored content in print + WIRED.com, ~2014). Yet WIRED
produces the most consistently adversarial coverage of Meta Ray-Ban and
Oakley Meta smart glasses in the dataset — the SAME products driving
EssilorLuxottica's fastest-growing revenue segment (AI glasses nearly
doubled in Q2 2026, 7M+ units sold FY2025).

The paradox: EssilorLuxottica's advertising revenue flows to the PARENT
company (Condé Nast / Advance Publications) that also owns WIRED. The
adversarial framing targets "Meta" not "Ray-Ban" or "Oakley" — suggesting
the brand trigger overrides the advertising financial relationship.

Samsung contrast (Mechanism #76): Samsung's $9.7B global ad spend creates
COMPOUND positive coverage for Samsung glasses. EssilorLuxottica's ~€2B
ad spend does NOT create softer coverage for glasses carrying the "Meta"
brand name. This isolates "Meta" as the editorial trigger, not the product
category or the manufacturing partner.

Sources:
1. EssilorLuxottica H1 2023 Interim Financial Report — €828M advertising
   and marketing expenses on €12.85B revenue
   https://media.essilorluxottica.com/cms/caas/v1/media/126326/data/09f544d4a1697159768363056e0677a1/2023-h1-essilorluxottica-en-interim-financial-report.pdf
2. EssilorLuxottica Q4/FY2025 Results — €28.49B revenue, 7M+ AI glasses
   sold, AI glasses as key growth driver
   https://live.euronext.com/en/products/equities/company-news/2026-02-11-essilorluxottica-q4fy-2025-results-revenue-growing-184-q4
3. EssilorLuxottica Q2/H1 2026 Results — AI glasses nearly doubled in
   revenue in Q2 2026, H1 revenue €14.82B
   https://www.globenewswire.com/news-release/2026/07/28/3334563/0/en/essilorluxottica-q2-h1-2026-results-solid-revenue-trajectory-at-9-7-in-h1-with-q2-at-8-7-increasing-profitability-with-adj-operating-profit-15.html
4. Oakley-WIRED global brand alliance — co-created and sponsored content,
   brand advertising in international print editions and across WIRED.com
   https://sgbonline.com/oakleys-says-new-marketing-campaign-will-emphasize-disruptive-design/
5. Adrienne So, WIRED — Oakley Meta Vanguard review with "(which are
   garbage)" parenthetical (Oct 21, 2025), Mechanism #102
6. EssilorLuxottica Q1 2026 — revenues +10.8%, Ray-Ban and Oakley top
   performers boosted by AI glasses
   https://www.reuters.com/business/essilorluxottica-first-quarter-revenues-rise-108-boosted-by-ai-glasses-2026-04-22/
7. Condé Nast-Microsoft AI Content Marketplace pilot (Feb 2026) — Condé
   Nast US text-based editorial content licensed for Microsoft Copilot
   https://www.WebWire.com/ViewPressRel.asp?aId=350303
8. Condé Nast-OpenAI content licensing deal (Aug 2024) — multi-year
   agreement covering WIRED, Vogue, GQ, Vanity Fair, etc.
   https://siliconangle.com/2024/08/20/openai-agrees-content-licensing-deal-conde-nast-feed-searchgpt-chatgpt/

Confounding factors:
1. STRONG: WIRED editorial wall — standard journalistic practice separating
   advertising from editorial decisions. EssilorLuxottica ad spend in
   Vogue/GQ doesn't mean WIRED editorial is aware of or influenced by
   the parent-level revenue.
2. STRONG: Meta's genuine Cambridge Analytica/FB Papers history creates
   legitimate editorial skepticism independent of any financial relationship.
3. MODERATE: Oakley-WIRED brand alliance was ~2014 era; may not be active
   in 2025-2026. Historical relationship, not necessarily current.
4. MODERATE: Fashion ad budgets (Vogue, GQ) flow through different
   departments and ad sales teams than tech editorial at WIRED.
5. WEAK: Different reader demographics between Vogue/GQ (fashion) and
   WIRED (tech) mean different ad sales teams and client relationships.
6. WEAK: EssilorLuxottica doesn't explicitly condition ad spend on
   editorial coverage — standard practice for luxury advertisers.

Testable predictions:
1. WIRED will avoid mentioning EssilorLuxottica's financial success with
   AI glasses in product reviews, keeping the "Meta privacy" framing
   separate from the "Ray-Ban/Oakley commercial success" story.
2. Condé Nast fashion titles (Vogue, GQ) will cover Ray-Ban Meta glasses
   MORE favorably than WIRED covers the same product — isolating the
   tech editorial vs. fashion editorial framing difference within the
   SAME parent company.
3. If Samsung's Galaxy Glasses launch with Oakley-style branding (avoiding
   "Google" in the product name), Samsung will receive softer WIRED
   coverage than Meta Ray-Ban — confirming brand-trigger over product-
   category framing.
4. EssilorLuxottica earnings calls will increasingly emphasize AI glasses
   revenue without generating sympathetic WIRED coverage for the product
   category that funds Condé Nast's parent ad revenue.
"""

import os
import pytest
import yaml


PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


def load_yaml(filename):
    filepath = os.path.join(PROFILES_DIR, filename)
    with open(filepath, 'r') as f:
        return yaml.safe_load(f)


class TestEssilorLuxotticaFinancialData:
    """Verify EssilorLuxottica advertising and revenue data."""

    def test_essilorluxottica_advertising_spend_h1_2023(self):
        """EssilorLuxottica spent €828M on advertising/marketing in H1 2023."""
        data = load_yaml('competitor-entities.yaml')
        el = data.get('essilorluxottica', {})
        ad_spend = el.get('essilorluxottica_advertising_paradox', {})
        assert ad_spend.get('h1_2023_advertising_marketing_eur_m') == 828

    def test_essilorluxottica_h1_2023_revenue(self):
        """H1 2023 revenue was €12,851M."""
        data = load_yaml('competitor-entities.yaml')
        el = data.get('essilorluxottica', {})
        ad_spend = el.get('essilorluxottica_advertising_paradox', {})
        assert ad_spend.get('h1_2023_revenue_eur_m') == 12851

    def test_advertising_as_percent_of_revenue(self):
        """Advertising/marketing was ~6.4% of revenue in H1 2023."""
        data = load_yaml('competitor-entities.yaml')
        el = data.get('essilorluxottica', {})
        ad_spend = el.get('essilorluxottica_advertising_paradox', {})
        pct = ad_spend.get('advertising_pct_of_revenue')
        assert pct is not None
        assert 6.0 <= pct <= 7.0

    def test_fy2025_revenue(self):
        """FY2025 revenue was €28,491M."""
        data = load_yaml('competitor-entities.yaml')
        el = data.get('essilorluxottica', {})
        ad_spend = el.get('essilorluxottica_advertising_paradox', {})
        assert ad_spend.get('fy2025_revenue_eur_m') == 28491

    def test_estimated_fy2025_advertising(self):
        """Estimated FY2025 advertising/marketing at ~€1.8B+."""
        data = load_yaml('competitor-entities.yaml')
        el = data.get('essilorluxottica', {})
        ad_spend = el.get('essilorluxottica_advertising_paradox', {})
        est = ad_spend.get('estimated_fy2025_advertising_eur_m')
        assert est is not None
        assert est >= 1800

    def test_ai_glasses_fy2025_units(self):
        """7M+ AI glasses sold in FY2025."""
        data = load_yaml('competitor-entities.yaml')
        el = data.get('essilorluxottica', {})
        ad_spend = el.get('essilorluxottica_advertising_paradox', {})
        assert ad_spend.get('ai_glasses_fy2025_units_m') >= 7

    def test_h1_2026_revenue(self):
        """H1 2026 revenue was €14,818M."""
        data = load_yaml('competitor-entities.yaml')
        el = data.get('essilorluxottica', {})
        ad_spend = el.get('essilorluxottica_advertising_paradox', {})
        assert ad_spend.get('h1_2026_revenue_eur_m') == 14818

    def test_q2_2026_ai_glasses_growth(self):
        """AI glasses nearly doubled in revenue in Q2 2026."""
        data = load_yaml('competitor-entities.yaml')
        el = data.get('essilorluxottica', {})
        ad_spend = el.get('essilorluxottica_advertising_paradox', {})
        desc = ad_spend.get('q2_2026_ai_glasses_growth', '')
        assert 'nearly doubl' in desc.lower() or 'almost doubl' in desc.lower()


class TestOakleyWiredHistoricalAlliance:
    """Verify Oakley's direct advertising partnership with WIRED."""

    def test_oakley_wired_brand_alliance_exists(self):
        """Oakley maintained a global brand alliance with WIRED."""
        data = load_yaml('competitor-entities.yaml')
        el = data.get('essilorluxottica', {})
        paradox = el.get('essilorluxottica_advertising_paradox', {})
        alliance = paradox.get('oakley_wired_direct_alliance', {})
        assert alliance.get('relationship_type') == 'global_brand_alliance'

    def test_oakley_wired_alliance_included_sponsored_content(self):
        """Alliance included co-created and sponsored multi-media content."""
        data = load_yaml('competitor-entities.yaml')
        el = data.get('essilorluxottica', {})
        paradox = el.get('essilorluxottica_advertising_paradox', {})
        alliance = paradox.get('oakley_wired_direct_alliance', {})
        desc = alliance.get('scope', '')
        assert 'co-created' in desc.lower() or 'sponsored' in desc.lower()

    def test_oakley_wired_alliance_included_print_and_digital(self):
        """Alliance spanned international print editions and WIRED.com."""
        data = load_yaml('competitor-entities.yaml')
        el = data.get('essilorluxottica', {})
        paradox = el.get('essilorluxottica_advertising_paradox', {})
        alliance = paradox.get('oakley_wired_direct_alliance', {})
        scope = alliance.get('scope', '')
        assert 'print' in scope.lower() or 'wired.com' in scope.lower()

    def test_oakley_wired_alliance_theme_was_disruption(self):
        """Alliance theme was disruption in design/technology/manufacturing."""
        data = load_yaml('competitor-entities.yaml')
        el = data.get('essilorluxottica', {})
        paradox = el.get('essilorluxottica_advertising_paradox', {})
        alliance = paradox.get('oakley_wired_direct_alliance', {})
        theme = alliance.get('theme', '')
        assert 'disruption' in theme.lower()

    def test_oakley_wired_alliance_source(self):
        """Alliance has a verifiable source URL."""
        data = load_yaml('competitor-entities.yaml')
        el = data.get('essilorluxottica', {})
        paradox = el.get('essilorluxottica_advertising_paradox', {})
        alliance = paradox.get('oakley_wired_direct_alliance', {})
        source = alliance.get('source_url', '')
        assert 'sgbonline.com' in source or 'adweek.com' in source


class TestCondeNastCrossSubsidiaryParadox:
    """Verify the cross-subsidiary advertising paradox structure."""

    def test_conde_nast_owns_both_wired_and_fashion_titles(self):
        """Condé Nast owns WIRED AND Vogue/GQ/VF — same parent, different editorial."""
        data = load_yaml('wired.yaml')
        chain = data.get('ownership_chain', [])
        parent_names = [entry.get('name', '').lower() for entry in chain if isinstance(entry, dict)]
        assert any('condé nast' in n or 'conde nast' in n for n in parent_names) or \
               any('advance' in n for n in parent_names)

    def test_essilorluxottica_advertises_in_fashion_titles(self):
        """EssilorLuxottica/Ray-Ban advertises in Condé Nast fashion publications."""
        data = load_yaml('competitor-entities.yaml')
        el = data.get('essilorluxottica', {})
        paradox = el.get('essilorluxottica_advertising_paradox', {})
        fashion = paradox.get('conde_nast_fashion_advertising', {})
        titles = fashion.get('publications', [])
        assert any('vogue' in t.lower() for t in titles)
        assert any('gq' in t.lower() for t in titles)

    def test_paradox_documented_in_research(self):
        """Mechanism #103 is documented in competitor-coverage-research.yaml."""
        data = load_yaml('competitor-coverage-research.yaml')
        research = data.get('cross_publication_findings', [])
        if isinstance(research, list):
            found = any(
                isinstance(m, dict) and m.get('mechanism_id') == 103
                for m in research
            )
        else:
            found = False
        # Also check nested structures
        if not found:
            found = _find_mechanism_103(data)
        assert found, "Mechanism #103 not found in research file"

    def test_paradox_identifies_brand_trigger(self):
        """Paradox identifies 'Meta' as the editorial trigger, not the product."""
        data = load_yaml('competitor-entities.yaml')
        el = data.get('essilorluxottica', {})
        paradox = el.get('essilorluxottica_advertising_paradox', {})
        finding = paradox.get('finding', '')
        assert 'meta' in finding.lower()
        assert 'brand' in finding.lower() or 'trigger' in finding.lower() or 'name' in finding.lower()


class TestSamsungContrastComparison:
    """Compare EssilorLuxottica ad spend effect vs Samsung ad spend effect."""

    def test_samsung_ad_spend_larger_than_essilorluxottica(self):
        """Samsung's $9.7B global ad spend exceeds EL's ~€2B."""
        data = load_yaml('competitor-entities.yaml')
        el = data.get('essilorluxottica', {})
        paradox = el.get('essilorluxottica_advertising_paradox', {})
        comparison = paradox.get('samsung_contrast', {})
        samsung_ad = comparison.get('samsung_global_ad_spend_usd_b', 0)
        el_ad = comparison.get('essilorluxottica_estimated_ad_spend_eur_b', 0)
        assert samsung_ad > el_ad

    def test_samsung_creates_softer_coverage(self):
        """Samsung's ad spend creates softer glasses coverage (documented in #76)."""
        data = load_yaml('competitor-entities.yaml')
        el = data.get('essilorluxottica', {})
        paradox = el.get('essilorluxottica_advertising_paradox', {})
        comparison = paradox.get('samsung_contrast', {})
        assert comparison.get('samsung_coverage_effect') == 'softer'

    def test_essilorluxottica_does_not_create_softer_coverage(self):
        """EL's ad spend does NOT create softer Meta glasses coverage."""
        data = load_yaml('competitor-entities.yaml')
        el = data.get('essilorluxottica', {})
        paradox = el.get('essilorluxottica_advertising_paradox', {})
        comparison = paradox.get('samsung_contrast', {})
        assert comparison.get('essilorluxottica_coverage_effect') == 'no_effect'

    def test_difference_attributed_to_brand_name(self):
        """The difference is attributed to 'Meta' in the product name."""
        data = load_yaml('competitor-entities.yaml')
        el = data.get('essilorluxottica', {})
        paradox = el.get('essilorluxottica_advertising_paradox', {})
        comparison = paradox.get('samsung_contrast', {})
        explanation = comparison.get('explanation', '')
        assert 'meta' in explanation.lower()
        assert 'brand' in explanation.lower() or 'name' in explanation.lower()


class TestCondeNastAIDealContext:
    """Verify Condé Nast AI deal context — 5 deals, 0 Meta."""

    def test_conde_nast_has_openai_deal(self):
        """Condé Nast has OpenAI content licensing deal (Aug 2024)."""
        data = load_yaml('competitor-entities.yaml')
        el = data.get('essilorluxottica', {})
        paradox = el.get('essilorluxottica_advertising_paradox', {})
        context = paradox.get('conde_nast_ai_deal_context', {})
        deals = context.get('deals', [])
        assert any('openai' in d.lower() for d in deals)

    def test_conde_nast_has_microsoft_deal(self):
        """Condé Nast joined Microsoft AI Content Marketplace (Feb 2026)."""
        data = load_yaml('competitor-entities.yaml')
        el = data.get('essilorluxottica', {})
        paradox = el.get('essilorluxottica_advertising_paradox', {})
        context = paradox.get('conde_nast_ai_deal_context', {})
        deals = context.get('deals', [])
        assert any('microsoft' in d.lower() for d in deals)

    def test_conde_nast_has_no_meta_deal(self):
        """Condé Nast has NO Meta AI content deal."""
        data = load_yaml('competitor-entities.yaml')
        el = data.get('essilorluxottica', {})
        paradox = el.get('essilorluxottica_advertising_paradox', {})
        context = paradox.get('conde_nast_ai_deal_context', {})
        assert context.get('meta_deal') is False or context.get('meta_deal') == 'none'

    def test_financial_exclusion_amplifies_paradox(self):
        """Meta's absence from Condé Nast AI deals amplifies the paradox."""
        data = load_yaml('competitor-entities.yaml')
        el = data.get('essilorluxottica', {})
        paradox = el.get('essilorluxottica_advertising_paradox', {})
        context = paradox.get('conde_nast_ai_deal_context', {})
        finding = context.get('implication', '')
        assert 'exclusion' in finding.lower() or 'absence' in finding.lower() or 'paradox' in finding.lower() or 'amplif' in finding.lower()


class TestWIREDAdversarialArticles:
    """Verify WIRED's adversarial coverage of EssilorLuxottica's AI glasses products."""

    def test_adrienne_so_oakley_vanguard_review_adversarial(self):
        """Adrienne So's Oakley Meta Vanguard review used adversarial language."""
        data = load_yaml('competitor-entities.yaml')
        el = data.get('essilorluxottica', {})
        paradox = el.get('essilorluxottica_advertising_paradox', {})
        articles = paradox.get('wired_adversarial_examples', [])
        oakley_review = [a for a in articles if 'vanguard' in a.get('product', '').lower() or 'oakley' in a.get('product', '').lower()]
        assert len(oakley_review) >= 1
        assert oakley_review[0].get('tone', 0) < 0

    def test_wired_coverage_targets_meta_not_rayban(self):
        """WIRED adversarial framing targets 'Meta' not 'Ray-Ban'/'Oakley'."""
        data = load_yaml('competitor-entities.yaml')
        el = data.get('essilorluxottica', {})
        paradox = el.get('essilorluxottica_advertising_paradox', {})
        framing = paradox.get('framing_target', '')
        assert 'meta' in framing.lower()

    def test_irony_oakley_disruption_theme(self):
        """WIRED's Oakley brand alliance promoted 'disruption' — now WIRED attacks
        Oakley's most disruptive product (Oakley Meta Vanguard)."""
        data = load_yaml('competitor-entities.yaml')
        el = data.get('essilorluxottica', {})
        paradox = el.get('essilorluxottica_advertising_paradox', {})
        irony = paradox.get('oakley_wired_direct_alliance', {}).get('irony_note', '')
        assert 'disrupt' in irony.lower() or 'vanguard' in irony.lower()


class TestConfoundingFactors:
    """Verify confounding factors are documented."""

    def test_has_at_least_5_confounding_factors(self):
        """Mechanism #103 has at least 5 confounding factors."""
        data = load_yaml('competitor-entities.yaml')
        el = data.get('essilorluxottica', {})
        paradox = el.get('essilorluxottica_advertising_paradox', {})
        factors = paradox.get('confounding_factors', [])
        assert len(factors) >= 5

    def test_has_strong_confounding_factors(self):
        """At least 2 confounding factors rated STRONG."""
        data = load_yaml('competitor-entities.yaml')
        el = data.get('essilorluxottica', {})
        paradox = el.get('essilorluxottica_advertising_paradox', {})
        factors = paradox.get('confounding_factors', [])
        strong = [f for f in factors if f.get('strength', '').upper() == 'STRONG']
        assert len(strong) >= 2

    def test_editorial_wall_is_strong_confound(self):
        """WIRED editorial wall between advertising and editorial is documented."""
        data = load_yaml('competitor-entities.yaml')
        el = data.get('essilorluxottica', {})
        paradox = el.get('essilorluxottica_advertising_paradox', {})
        factors = paradox.get('confounding_factors', [])
        wall_factors = [f for f in factors if 'editorial wall' in f.get('description', '').lower() or 'editorial independ' in f.get('description', '').lower()]
        assert len(wall_factors) >= 1
        assert wall_factors[0].get('strength', '').upper() == 'STRONG'


class TestTestablePredictions:
    """Verify testable predictions are documented."""

    def test_has_at_least_4_testable_predictions(self):
        """Mechanism #103 has at least 4 testable predictions."""
        data = load_yaml('competitor-entities.yaml')
        el = data.get('essilorluxottica', {})
        paradox = el.get('essilorluxottica_advertising_paradox', {})
        predictions = paradox.get('testable_predictions', [])
        assert len(predictions) >= 4

    def test_prediction_vogue_gq_vs_wired_framing(self):
        """Prediction: Vogue/GQ cover Ray-Ban Meta more favorably than WIRED."""
        data = load_yaml('competitor-entities.yaml')
        el = data.get('essilorluxottica', {})
        paradox = el.get('essilorluxottica_advertising_paradox', {})
        predictions = paradox.get('testable_predictions', [])
        fashion_pred = [p for p in predictions if 'vogue' in p.get('description', '').lower() or 'gq' in p.get('description', '').lower() or 'fashion' in p.get('description', '').lower()]
        assert len(fashion_pred) >= 1

    def test_prediction_samsung_brand_name_test(self):
        """Prediction: Samsung glasses avoiding 'Google' in name get softer WIRED coverage."""
        data = load_yaml('competitor-entities.yaml')
        el = data.get('essilorluxottica', {})
        paradox = el.get('essilorluxottica_advertising_paradox', {})
        predictions = paradox.get('testable_predictions', [])
        samsung_pred = [p for p in predictions if 'samsung' in p.get('description', '').lower() or 'brand' in p.get('description', '').lower()]
        assert len(samsung_pred) >= 1


class TestSourceURLQuality:
    """Verify all sources use HTTPS and are properly documented."""

    def test_all_source_urls_https(self):
        """All source URLs in the mechanism use HTTPS."""
        data = load_yaml('competitor-entities.yaml')
        el = data.get('essilorluxottica', {})
        paradox = el.get('essilorluxottica_advertising_paradox', {})
        sources = paradox.get('source_urls', [])
        for url in sources:
            assert url.startswith('https://'), f"Non-HTTPS URL: {url}"

    def test_has_at_least_6_source_urls(self):
        """At least 6 source URLs documented."""
        data = load_yaml('competitor-entities.yaml')
        el = data.get('essilorluxottica', {})
        paradox = el.get('essilorluxottica_advertising_paradox', {})
        sources = paradox.get('source_urls', [])
        assert len(sources) >= 6


class TestMechanismCrossReferences:
    """Verify cross-references to related mechanisms."""

    def test_references_samsung_compound_leverage_76(self):
        """References Samsung-Google Compound Advertiser Leverage (#76)."""
        data = load_yaml('competitor-entities.yaml')
        el = data.get('essilorluxottica', {})
        paradox = el.get('essilorluxottica_advertising_paradox', {})
        xrefs = paradox.get('cross_references', [])
        ref_76 = [x for x in xrefs if x.get('mechanism_id') == 76]
        assert len(ref_76) >= 1

    def test_references_adrienne_so_privacy_vocabulary_102(self):
        """References Adrienne So Wearables Privacy Vocabulary (#102)."""
        data = load_yaml('competitor-entities.yaml')
        el = data.get('essilorluxottica', {})
        paradox = el.get('essilorluxottica_advertising_paradox', {})
        xrefs = paradox.get('cross_references', [])
        ref_102 = [x for x in xrefs if x.get('mechanism_id') == 102]
        assert len(ref_102) >= 1

    def test_references_conde_nast_ai_deal_portfolio_78(self):
        """References Condé Nast AI Deal Portfolio Dependency Index (#78)."""
        data = load_yaml('competitor-entities.yaml')
        el = data.get('essilorluxottica', {})
        paradox = el.get('essilorluxottica_advertising_paradox', {})
        xrefs = paradox.get('cross_references', [])
        ref_78 = [x for x in xrefs if x.get('mechanism_id') == 78]
        assert len(ref_78) >= 1


def _find_mechanism_103(data):
    """Recursively search for mechanism_id: 103 in the data structure."""
    if isinstance(data, dict):
        for k, v in data.items():
            if k == 'mechanism_id' and v == 103:
                return True
            if _find_mechanism_103(v):
                return True
    elif isinstance(data, list):
        for item in data:
            if _find_mechanism_103(item):
                return True
    return False
