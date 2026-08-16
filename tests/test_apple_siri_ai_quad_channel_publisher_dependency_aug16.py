"""
Test: Apple Siri AI Content Licensing — Quad-Channel Publisher Financial
Architecture Pre-N50 (Mechanism #136)

Apple is building FOUR simultaneous publisher financial dependency channels:
1. Apple News+ (50% of $12.99/mo, engagement-weighted, 400+ publishers, 125M MAU)
2. Apple Advertising ($7.3B+ record quarter, embedded in $30.7B Services)
3. App Store Commission (15-30% of publisher app subscriptions, News Partner: 15%)
4. Siri AI Content Licensing (NEW: nine-figure budget, variable pay-per-use, multiyear)

This is the most comprehensive publisher financial dependency of any tech company,
and all four channels converge BEFORE Apple's N50 smart glasses launch (WWDC Jun 2027).
Meta has ZERO content channels with publishers and competes for advertising revenue.

Sources:
- https://www.wsj.com/business/media/apple-in-talks-to-pay-publishers-to-improve-ai-powered-siri-0641f64b
- https://www.macstories.net/news/apple-reports-q3-2026-earnings/
- https://www.macobserver.com/news/apple-q3-2026-earnings-results-revenue-hits-109-4-billion-up-16-eps-jumps-29/
- https://www.adweek.com/media/conde-nast-events-revenue-2026/
- https://ppa.co.uk/guest-blog-8-facts-publishers-should-know-about-apple-news-plus
"""

import yaml
import os
import pytest


PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


def load_yaml(filename):
    path = os.path.join(PROFILES_DIR, filename)
    with open(path, 'r') as f:
        return yaml.safe_load(f)


class TestAppleSiriAIDealFacts:
    """Verify core facts about Apple's Siri AI content licensing negotiations."""

    def test_siri_ai_deal_exists_in_entity_profile(self):
        entities = load_yaml('competitor-entities.yaml')
        apple = entities['entities']['apple']
        assert 'siri_ai_content_licensing' in apple, \
            "Apple entity must document Siri AI content licensing negotiations"

    def test_siri_ai_budget_nine_figures(self):
        entities = load_yaml('competitor-entities.yaml')
        siri = entities['entities']['apple']['siri_ai_content_licensing']
        budget = siri.get('proposed_budget', '')
        assert 'nine-figure' in budget.lower() or '100' in budget, \
            "Budget must be documented as nine-figure ($100M+)"

    def test_siri_ai_variable_compensation_model(self):
        entities = load_yaml('competitor-entities.yaml')
        siri = entities['entities']['apple']['siri_ai_content_licensing']
        model = siri.get('compensation_model', '')
        assert 'variable' in model.lower() or 'pay' in model.lower(), \
            "Compensation model must be documented as variable/pay-per-use"

    def test_siri_ai_multiyear_term(self):
        entities = load_yaml('competitor-entities.yaml')
        siri = entities['entities']['apple']['siri_ai_content_licensing']
        term = siri.get('deal_term', '')
        assert 'multiyear' in term.lower() or 'multi-year' in term.lower(), \
            "Deal term must be documented as multiyear"

    def test_siri_ai_source_url(self):
        entities = load_yaml('competitor-entities.yaml')
        siri = entities['entities']['apple']['siri_ai_content_licensing']
        urls = siri.get('source_urls', [])
        wsj_found = any('wsj.com' in u for u in urls)
        assert wsj_found, "WSJ Aug 13, 2026 article must be cited as source"

    def test_siri_ai_pre_n50_timing(self):
        """Deals negotiated before N50 launch creates pre-launch incentive."""
        entities = load_yaml('competitor-entities.yaml')
        siri = entities['entities']['apple']['siri_ai_content_licensing']
        n50_ref = siri.get('n50_timing_relevance', '')
        assert 'n50' in n50_ref.lower() or 'glasses' in n50_ref.lower(), \
            "Must document that Siri AI deals precede N50 smart glasses launch"


class TestQuadChannelArchitecture:
    """Verify the four-channel publisher financial dependency structure."""

    def test_four_channels_documented(self):
        entities = load_yaml('competitor-entities.yaml')
        apple = entities['entities']['apple']
        quad = apple.get('quad_channel_publisher_dependency', {})
        channels = quad.get('channels', [])
        assert len(channels) >= 4, \
            f"Must document at least 4 publisher financial channels, found {len(channels)}"

    def test_channel_1_news_plus(self):
        entities = load_yaml('competitor-entities.yaml')
        quad = entities['entities']['apple']['quad_channel_publisher_dependency']
        channels = quad['channels']
        news_plus = [c for c in channels if 'news' in c.get('name', '').lower()
                     and 'plus' in c.get('name', '').lower()]
        assert len(news_plus) >= 1, "Channel 1: Apple News+ must be documented"

    def test_channel_2_advertising(self):
        entities = load_yaml('competitor-entities.yaml')
        quad = entities['entities']['apple']['quad_channel_publisher_dependency']
        channels = quad['channels']
        ads = [c for c in channels if 'advertis' in c.get('name', '').lower()]
        assert len(ads) >= 1, "Channel 2: Apple Advertising must be documented"

    def test_channel_3_app_store(self):
        entities = load_yaml('competitor-entities.yaml')
        quad = entities['entities']['apple']['quad_channel_publisher_dependency']
        channels = quad['channels']
        store = [c for c in channels if 'app store' in c.get('name', '').lower()
                 or 'commission' in c.get('name', '').lower()]
        assert len(store) >= 1, "Channel 3: App Store commission must be documented"

    def test_channel_4_siri_ai_licensing(self):
        entities = load_yaml('competitor-entities.yaml')
        quad = entities['entities']['apple']['quad_channel_publisher_dependency']
        channels = quad['channels']
        siri = [c for c in channels if 'siri' in c.get('name', '').lower()]
        assert len(siri) >= 1, "Channel 4: Siri AI licensing must be documented"

    def test_meta_zero_channels(self):
        entities = load_yaml('competitor-entities.yaml')
        quad = entities['entities']['apple']['quad_channel_publisher_dependency']
        meta = quad.get('meta_contrast', {})
        count = meta.get('publisher_financial_channels', -1)
        assert count == 0, "Meta must be documented as having 0 publisher financial channels"


class TestAppleQ3FY2026Financials:
    """Verify Apple Q3 FY2026 earnings data accuracy."""

    def test_q3_revenue(self):
        entities = load_yaml('competitor-entities.yaml')
        siri = entities['entities']['apple']['siri_ai_content_licensing']
        q3 = siri.get('apple_q3_fy2026', {})
        rev = q3.get('revenue_b', 0)
        assert 109 <= rev <= 110, f"Q3 revenue must be ~$109.4B, got {rev}"

    def test_q3_services_revenue(self):
        entities = load_yaml('competitor-entities.yaml')
        siri = entities['entities']['apple']['siri_ai_content_licensing']
        q3 = siri.get('apple_q3_fy2026', {})
        svc = q3.get('services_revenue_b', 0)
        assert 30 <= svc <= 31, f"Q3 Services must be ~$30.7B, got {svc}"

    def test_q3_services_gross_margin(self):
        entities = load_yaml('competitor-entities.yaml')
        siri = entities['entities']['apple']['siri_ai_content_licensing']
        q3 = siri.get('apple_q3_fy2026', {})
        margin = q3.get('services_gross_margin_pct', 0)
        assert 75 <= margin <= 76, f"Services margin must be ~75.6%, got {margin}"

    def test_q3_paid_subscriptions(self):
        entities = load_yaml('competitor-entities.yaml')
        siri = entities['entities']['apple']['siri_ai_content_licensing']
        q3 = siri.get('apple_q3_fy2026', {})
        subs = q3.get('paid_subscriptions_b', 0)
        assert subs >= 1.5, f"Must be >=1.5B paid subscriptions, got {subs}"

    def test_q3_wearables_revenue(self):
        entities = load_yaml('competitor-entities.yaml')
        siri = entities['entities']['apple']['siri_ai_content_licensing']
        q3 = siri.get('apple_q3_fy2026', {})
        wear = q3.get('wearables_home_accessories_b', 0)
        assert 7.5 <= wear <= 8.5, f"Wearables must be ~$7.9B, got {wear}"


class TestCompetitorChannelComparison:
    """Verify comparative publisher financial channel counts across companies."""

    def test_apple_has_most_channels(self):
        entities = load_yaml('competitor-entities.yaml')
        quad = entities['entities']['apple']['quad_channel_publisher_dependency']
        comparison = quad.get('competitor_channel_comparison', {})
        apple_count = comparison.get('apple', 0)
        google_count = comparison.get('google', 0)
        openai_count = comparison.get('openai', 0)
        assert apple_count >= 4, f"Apple must have >=4 channels, got {apple_count}"
        assert apple_count > google_count, \
            f"Apple ({apple_count}) must exceed Google ({google_count})"
        assert apple_count > openai_count, \
            f"Apple ({apple_count}) must exceed OpenAI ({openai_count})"

    def test_meta_has_zero_channels(self):
        entities = load_yaml('competitor-entities.yaml')
        quad = entities['entities']['apple']['quad_channel_publisher_dependency']
        comparison = quad.get('competitor_channel_comparison', {})
        meta_count = comparison.get('meta', -1)
        assert meta_count == 0, f"Meta must have 0 publisher channels, got {meta_count}"

    def test_channel_delta_documented(self):
        """The gap between Apple (4) and Meta (0) must be documented."""
        entities = load_yaml('competitor-entities.yaml')
        quad = entities['entities']['apple']['quad_channel_publisher_dependency']
        delta = quad.get('apple_meta_channel_delta', 0)
        assert delta >= 4, f"Apple-Meta channel delta must be >=4, got {delta}"


class TestMechanism136Structure:
    """Verify mechanism #136 structural integrity in competitor-coverage-research.yaml."""

    def test_mechanism_exists(self):
        ccr = load_yaml('competitor-coverage-research.yaml')
        cpf = ccr.get('cross_publication_findings', {})
        found = False
        for key, val in cpf.items():
            if isinstance(val, dict) and val.get('mechanism_id') == 136:
                found = True
                break
        assert found, "Mechanism #136 must exist in cross_publication_findings"

    def test_mechanism_has_finding_summary(self):
        ccr = load_yaml('competitor-coverage-research.yaml')
        cpf = ccr.get('cross_publication_findings', {})
        for key, val in cpf.items():
            if isinstance(val, dict) and val.get('mechanism_id') == 136:
                assert 'finding_summary' in val, \
                    "Mechanism #136 must have finding_summary"
                assert len(val['finding_summary']) > 100, \
                    "finding_summary must be substantive (>100 chars)"
                return
        pytest.fail("Mechanism #136 not found")

    def test_mechanism_has_source_urls(self):
        ccr = load_yaml('competitor-coverage-research.yaml')
        cpf = ccr.get('cross_publication_findings', {})
        for key, val in cpf.items():
            if isinstance(val, dict) and val.get('mechanism_id') == 136:
                urls = val.get('source_urls', [])
                assert len(urls) >= 4, \
                    f"Mechanism #136 must have >=4 source URLs, found {len(urls)}"
                wsj = any('wsj.com' in u for u in urls)
                assert wsj, "Must cite WSJ article on Siri AI publisher deals"
                return
        pytest.fail("Mechanism #136 not found")

    def test_mechanism_has_confounders(self):
        ccr = load_yaml('competitor-coverage-research.yaml')
        cpf = ccr.get('cross_publication_findings', {})
        for key, val in cpf.items():
            if isinstance(val, dict) and val.get('mechanism_id') == 136:
                confounders = val.get('confounders', [])
                assert len(confounders) >= 5, \
                    f"Must have >=5 confounders, found {len(confounders)}"
                strong = [c for c in confounders
                          if c.get('strength', '').upper() == 'STRONG']
                assert len(strong) >= 2, \
                    f"Must have >=2 STRONG confounders, found {len(strong)}"
                return
        pytest.fail("Mechanism #136 not found")

    def test_mechanism_has_cross_references(self):
        ccr = load_yaml('competitor-coverage-research.yaml')
        cpf = ccr.get('cross_publication_findings', {})
        for key, val in cpf.items():
            if isinstance(val, dict) and val.get('mechanism_id') == 136:
                refs = val.get('cross_references', [])
                assert len(refs) >= 3, \
                    f"Must cross-reference >=3 other mechanisms, found {len(refs)}"
                ref_ids = [r.get('mechanism_id') for r in refs]
                assert 61 in ref_ids, "Must cross-reference #61 (News+ pre-N50 alignment)"
                return
        pytest.fail("Mechanism #136 not found")

    def test_mechanism_has_testable_predictions(self):
        ccr = load_yaml('competitor-coverage-research.yaml')
        cpf = ccr.get('cross_publication_findings', {})
        for key, val in cpf.items():
            if isinstance(val, dict) and val.get('mechanism_id') == 136:
                preds = val.get('testable_predictions', [])
                assert len(preds) >= 3, \
                    f"Must have >=3 testable predictions, found {len(preds)}"
                return
        pytest.fail("Mechanism #136 not found")


class TestConfounderQuality:
    """Verify confounders have proper strength ratings and substance."""

    @pytest.fixture
    def confounders(self):
        ccr = load_yaml('competitor-coverage-research.yaml')
        cpf = ccr.get('cross_publication_findings', {})
        for key, val in cpf.items():
            if isinstance(val, dict) and val.get('mechanism_id') == 136:
                return val.get('confounders', [])
        pytest.fail("Mechanism #136 not found")

    def test_all_confounders_have_strength(self, confounders):
        for c in confounders:
            assert 'strength' in c, f"Confounder missing strength: {c.get('factor', '?')}"
            assert c['strength'].upper() in ('STRONG', 'MODERATE', 'WEAK'), \
                f"Invalid strength '{c['strength']}' for {c.get('factor', '?')}"

    def test_all_confounders_have_detail(self, confounders):
        for c in confounders:
            assert 'detail' in c, f"Confounder missing detail: {c.get('factor', '?')}"
            assert len(c['detail']) > 20, \
                f"Confounder detail too short for {c.get('factor', '?')}"

    def test_deals_not_yet_signed_confounder(self, confounders):
        """Critical confounder: deals are still in negotiation, not signed."""
        negotiation = [c for c in confounders
                       if 'negotiat' in c.get('factor', '').lower()
                       or 'not yet signed' in c.get('factor', '').lower()
                       or 'talks' in c.get('factor', '').lower()]
        assert len(negotiation) >= 1, \
            "Must document that Siri AI deals are not yet signed as a confounder"


class TestCrossReferenceIntegrity:
    """Verify bidirectional cross-references between #136 and older mechanisms."""

    def test_mechanism_61_backrefs_136(self):
        """Mechanism #61 (News+ pre-N50) should reference #136."""
        entities = load_yaml('competitor-entities.yaml')
        apple = entities['entities']['apple']
        alignment = apple.get('apple_news_glasses_prelaunch_alignment', {})
        refs = alignment.get('cross_references', [])
        ref_ids = [r.get('mechanism_id') for r in refs]
        assert 136 in ref_ids, \
            "Mechanism #61 must have backref to #136 (quad-channel expansion)"

    def test_mechanism_134_cross_referenced(self):
        """Mechanism #136 should reference #134 (remediation coverage silence)."""
        ccr = load_yaml('competitor-coverage-research.yaml')
        cpf = ccr.get('cross_publication_findings', {})
        for key, val in cpf.items():
            if isinstance(val, dict) and val.get('mechanism_id') == 136:
                refs = val.get('cross_references', [])
                ref_ids = [r.get('mechanism_id') for r in refs]
                assert 134 in ref_ids, \
                    "Must cross-reference #134 (WIRED remediation silence)"
                return
        pytest.fail("Mechanism #136 not found")


class TestQuadChannelMetaContrast:
    """Test the asymmetry between Apple's quad-channel and Meta's zero channels."""

    def test_meta_no_content_deals_documented(self):
        entities = load_yaml('competitor-entities.yaml')
        quad = entities['entities']['apple']['quad_channel_publisher_dependency']
        meta = quad.get('meta_contrast', {})
        assert 'content_deals' in meta, "Meta's zero content deals must be documented"
        assert meta['content_deals'] == 0, "Meta content deals must be 0"

    def test_meta_ad_competitor_status(self):
        entities = load_yaml('competitor-entities.yaml')
        quad = entities['entities']['apple']['quad_channel_publisher_dependency']
        meta = quad.get('meta_contrast', {})
        assert meta.get('is_publisher_ad_competitor', True), \
            "Meta must be flagged as a publisher advertising competitor"

    def test_asymmetry_implications(self):
        """The quad-vs-zero asymmetry creates coverage incentive differential."""
        entities = load_yaml('competitor-entities.yaml')
        quad = entities['entities']['apple']['quad_channel_publisher_dependency']
        impl = quad.get('coverage_incentive_implication', '')
        assert len(impl) > 50, "Coverage incentive implication must be substantive"
        assert 'meta' in impl.lower(), "Implication must reference Meta contrast"


class TestDocSync:
    """Verify README and ARCHITECTURE docs are updated."""

    def test_readme_test_count_current(self):
        readme_path = os.path.join(os.path.dirname(__file__), '..', 'README.md')
        with open(readme_path, 'r') as f:
            content = f.read()
        # Should reference current test file count
        assert 'test_apple_siri_ai_quad_channel_publisher_dependency_aug16' in content, \
            "README must list this test file"

    def test_architecture_test_count_current(self):
        arch_path = os.path.join(os.path.dirname(__file__), '..',
                                 'docs', 'ARCHITECTURE.md')
        with open(arch_path, 'r') as f:
            content = f.read()
        assert 'test_apple_siri_ai_quad_channel_publisher_dependency_aug16' in content, \
            "ARCHITECTURE.md must list this test file"
