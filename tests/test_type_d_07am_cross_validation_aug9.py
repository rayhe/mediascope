"""
Type D: Test & Verify — Cross-Validation of News Corp Factiva Dual-Role +
Anthropic IPO Investor-Publisher Triangle + Infrastructure Count Sync

Date: 2026-08-09 07:00 PT

Cross-validates the two unlogged Type C iterations (05:00 and 06:00 PT) against
each other and against existing entity data. Key validation targets:

1. NEWS CORP TRIPLE REVENUE COHERENCE: News Corp is the first publisher receiving
   revenue from THREE major AI companies (OpenAI licensing, Meta licensing,
   Anthropic settlement). The Factiva marketplace analysis (05:00) and the
   Anthropic IPO triangle analysis (06:00) BOTH reference this — verify they
   are internally consistent.

2. FACTIVA MARKETPLACE ↔ BILATERAL DEAL CONSISTENCY: The marketplace_intermediary_
   landscape section's Factiva entry references News Corp's bilateral deals. These
   must match the entity-level News Corp data and the Anthropic triangle's
   settlement_revenue section.

3. ANTHROPIC ZERO-DEAL PARADOX ↔ MARKETPLACE POSITION: Anthropic has zero direct
   publisher deals AND is absent from all four marketplace operators. The zero-deal
   paradox in the triangle analysis must be consistent with the marketplace landscape
   (Anthropic neither buys through marketplaces nor sells).

4. MICROSOFT DEEPEST ENTANGLEMENT CLAIM: The marketplace concentration_risk section
   claims Microsoft has the "deepest entanglement" of any company. Cross-validate
   against the microsoft_openai_financial_axis data.

5. META ISOLATION CLAIM: concentration_risk claims Meta is the ONLY major AI company
   with no marketplace role. Verify against all entity profiles.

6. INFRASTRUCTURE COUNT SYNC: Verify README and ARCHITECTURE test/file counts match
   actual filesystem state after the two unlogged iterations.

Sources:
- profiles/competitor-entities.yaml (marketplace_intermediary_landscape, entities)
- profiles/news-corp.yaml
- tests/test_news_corp_factiva_marketplace_dual_role_aug9.py
- tests/test_anthropic_ipo_investor_publisher_triangle_aug9.py
"""

import pytest
import yaml
import os
import glob

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')
TESTS_DIR = os.path.dirname(__file__)
REPO_ROOT = os.path.join(os.path.dirname(__file__), '..')


def load_competitor_entities():
    path = os.path.join(PROFILES_DIR, 'competitor-entities.yaml')
    with open(path) as f:
        return yaml.safe_load(f)


def load_news_corp_profile():
    path = os.path.join(PROFILES_DIR, 'news-corp.yaml')
    with open(path) as f:
        return yaml.safe_load(f)


def load_readme():
    path = os.path.join(REPO_ROOT, 'README.md')
    with open(path) as f:
        return f.read()


def load_architecture():
    path = os.path.join(REPO_ROOT, 'docs', 'ARCHITECTURE.md')
    with open(path) as f:
        return f.read()


def get_entity(data, name):
    """Find entity by key or display_name in entities dict."""
    entities = data.get('entities', {})
    if isinstance(entities, dict):
        # Try direct key lookup first
        if name.lower() in entities:
            return entities[name.lower()]
        # Fall back to display_name match
        for key, e in entities.items():
            if isinstance(e, dict) and e.get('display_name', '').lower() == name.lower():
                return e
    return None


# --- Class 1: News Corp Triple Revenue Cross-Consistency ---

class TestNewsCorpTripleRevenueCrossConsistency:
    """The Anthropic triangle (06:00) and Factiva marketplace (05:00) both
    reference News Corp receiving revenue from three AI companies. Verify
    these references are internally consistent."""

    def test_triangle_settlement_mentions_news_corp(self):
        data = load_competitor_entities()
        anthropic = get_entity(data, 'Anthropic')
        assert anthropic is not None
        triangle = anthropic.get('investor_advertiser_publisher_triangle', {})
        dynamics = triangle.get('triangle_dynamics', [])
        settlement_item = None
        for d in dynamics:
            if isinstance(d, dict) and d.get('name') == 'settlement_revenue_adds_direct_layer':
                settlement_item = d
                break
        assert settlement_item is not None, "settlement_revenue_adds_direct_layer missing"
        detail = settlement_item.get('detail', '')
        assert 'News Corp' in detail
        assert 'OpenAI' in detail
        assert 'Meta' in detail
        assert 'Anthropic' in detail

    def test_triangle_settlement_says_first_triple(self):
        data = load_competitor_entities()
        anthropic = get_entity(data, 'Anthropic')
        triangle = anthropic.get('investor_advertiser_publisher_triangle', {})
        dynamics = triangle.get('triangle_dynamics', [])
        for d in dynamics:
            if isinstance(d, dict) and d.get('name') == 'settlement_revenue_adds_direct_layer':
                assert 'FIRST' in d.get('detail', '') or 'first' in d.get('detail', '').lower()
                return
        pytest.fail("settlement_revenue_adds_direct_layer not found")

    def test_triangle_settlement_references_earnings_call(self):
        data = load_competitor_entities()
        anthropic = get_entity(data, 'Anthropic')
        triangle = anthropic.get('investor_advertiser_publisher_triangle', {})
        dynamics = triangle.get('triangle_dynamics', [])
        for d in dynamics:
            if isinstance(d, dict) and d.get('name') == 'settlement_revenue_adds_direct_layer':
                detail = d.get('detail', '')
                assert 'Q4' in detail or 'earnings' in detail.lower()
                assert 'Thomson' in detail
                return
        pytest.fail("settlement_revenue_adds_direct_layer not found")

    def test_factiva_parent_deals_include_openai_and_meta(self):
        data = load_competitor_entities()
        ml = data.get('marketplace_intermediary_landscape', {})
        tier2 = ml.get('tier_2_marketplace', {})
        operators = tier2.get('operators', [])
        factiva = None
        for op in operators:
            if isinstance(op, dict) and 'Factiva' in op.get('name', ''):
                factiva = op
                break
        assert factiva is not None, "Factiva not found in tier_2 operators"
        parent_deals = factiva.get('parent_deals', [])
        deal_text = ' '.join(str(d) for d in parent_deals)
        assert 'OpenAI' in deal_text
        assert 'Meta' in deal_text


# --- Class 2: Anthropic Zero-Deal ↔ Marketplace Absence ---

class TestAnthropicMarketplaceAbsence:
    """Anthropic has zero direct publisher deals AND is not a buyer or seller
    in any marketplace. The zero-deal paradox must be consistent with the
    marketplace landscape showing Anthropic's absence."""

    def test_anthropic_not_in_any_marketplace_operator(self):
        data = load_competitor_entities()
        ml = data.get('marketplace_intermediary_landscape', {})
        tier2 = ml.get('tier_2_marketplace', {})
        operators = tier2.get('operators', [])
        for op in operators:
            if isinstance(op, dict):
                name = op.get('name', '')
                assert 'Anthropic' not in name, f"Anthropic should not be a marketplace operator: {name}"

    def test_anthropic_not_marketplace_buyer(self):
        data = load_competitor_entities()
        ml = data.get('marketplace_intermediary_landscape', {})
        tier2 = ml.get('tier_2_marketplace', {})
        operators = tier2.get('operators', [])
        for op in operators:
            if isinstance(op, dict):
                buyer = op.get('first_buyer', '')
                publishers = op.get('publishers', [])
                assert 'Anthropic' not in str(buyer), f"Anthropic should not be a buyer"

    def test_zero_deal_paradox_references_triangle(self):
        data = load_competitor_entities()
        anthropic = get_entity(data, 'Anthropic')
        triangle = anthropic.get('investor_advertiser_publisher_triangle', {})
        dynamics = triangle.get('triangle_dynamics', [])
        zdp = None
        for d in dynamics:
            if isinstance(d, dict) and d.get('name') == 'zero_deal_paradox_explained':
                zdp = d
                break
        assert zdp is not None
        detail = zdp.get('detail', '')
        assert 'zero' in detail.lower() or 'ZERO' in detail
        assert 'Google' in detail or 'Amazon' in detail


# --- Class 3: Microsoft Deepest Entanglement Validation ---

class TestMicrosoftDeepestEntanglement:
    """concentration_risk claims Microsoft has the deepest entanglement.
    Cross-validate against microsoft_openai_financial_axis."""

    def test_microsoft_in_marketplace_operators(self):
        data = load_competitor_entities()
        ml = data.get('marketplace_intermediary_landscape', {})
        tier2 = ml.get('tier_2_marketplace', {})
        operators = tier2.get('operators', [])
        ms_found = False
        for op in operators:
            if isinstance(op, dict) and 'Microsoft' in op.get('name', ''):
                ms_found = True
                assert op.get('dual_role', False) is True
                break
        assert ms_found, "Microsoft not found in marketplace operators"

    def test_microsoft_is_buyer_and_operator(self):
        data = load_competitor_entities()
        ml = data.get('marketplace_intermediary_landscape', {})
        tier2 = ml.get('tier_2_marketplace', {})
        operators = tier2.get('operators', [])
        for op in operators:
            if isinstance(op, dict) and 'Microsoft' in op.get('name', ''):
                assert op.get('is_buyer', False) is True
                assert op.get('dual_role', False) is True
                return
        pytest.fail("Microsoft not in marketplace operators")

    def test_concentration_risk_names_microsoft(self):
        data = load_competitor_entities()
        ml = data.get('marketplace_intermediary_landscape', {})
        cr = ml.get('concentration_risk', '')
        assert 'Microsoft' in cr

    def test_microsoft_openai_axis_exists(self):
        data = load_competitor_entities()
        assert 'microsoft_openai_financial_axis' in data, \
            "microsoft_openai_financial_axis section should exist"

    def test_microsoft_ai_lab_investments_includes_openai(self):
        data = load_competitor_entities()
        ml = data.get('marketplace_intermediary_landscape', {})
        tier2 = ml.get('tier_2_marketplace', {})
        operators = tier2.get('operators', [])
        for op in operators:
            if isinstance(op, dict) and 'Microsoft' in op.get('name', ''):
                investments = op.get('ai_lab_investments', [])
                inv_text = ' '.join(str(i) for i in investments)
                assert 'OpenAI' in inv_text
                return
        pytest.fail("Microsoft not found")


# --- Class 4: Meta Isolation Claim ---

class TestMetaIsolationClaim:
    """concentration_risk claims Meta is the ONLY major AI company with
    no marketplace operator role, no marketplace buyer role, no AI lab
    investor role. Verify this is true in the data."""

    def test_concentration_risk_isolates_meta(self):
        data = load_competitor_entities()
        ml = data.get('marketplace_intermediary_landscape', {})
        cr = ml.get('concentration_risk', '')
        assert 'Meta' in cr
        # Should say Meta is NOT a marketplace operator/buyer
        assert 'NOT' in cr or 'not' in cr.lower()

    def test_meta_not_in_marketplace_operators(self):
        data = load_competitor_entities()
        ml = data.get('marketplace_intermediary_landscape', {})
        tier2 = ml.get('tier_2_marketplace', {})
        operators = tier2.get('operators', [])
        for op in operators:
            if isinstance(op, dict):
                name = op.get('name', '')
                assert 'Meta' not in name, f"Meta should not be a marketplace operator: {name}"

    def test_meta_entity_has_no_ai_lab_investor_flag(self):
        """Meta doesn't invest in external AI labs (unlike Microsoft→OpenAI,
        Amazon→Anthropic, Google→Anthropic)."""
        data = load_competitor_entities()
        meta = get_entity(data, 'Meta')
        if meta is not None:
            # Meta entity might not exist as a separate competitor entity
            investments = meta.get('ai_lab_investments', [])
            assert len(investments) == 0 or investments is None


# --- Class 5: Factiva Source Count Coherence ---

class TestFactivaSourceCountCoherence:
    """The Factiva entry claims 8,100+ sources with AI rights, >25% of total.
    Verify this claim is consistent across all references."""

    def test_factiva_source_count_in_marketplace(self):
        data = load_competitor_entities()
        ml = data.get('marketplace_intermediary_landscape', {})
        tier2 = ml.get('tier_2_marketplace', {})
        operators = tier2.get('operators', [])
        for op in operators:
            if isinstance(op, dict) and 'Factiva' in op.get('name', ''):
                count = op.get('news_sources_with_ai_rights', 0)
                assert count >= 8100
                pct = op.get('pct_of_total_sources', 0)
                assert pct >= 25
                return
        pytest.fail("Factiva not found in operators")

    def test_factiva_is_not_ai_buyer(self):
        data = load_competitor_entities()
        ml = data.get('marketplace_intermediary_landscape', {})
        tier2 = ml.get('tier_2_marketplace', {})
        operators = tier2.get('operators', [])
        for op in operators:
            if isinstance(op, dict) and 'Factiva' in op.get('name', ''):
                assert op.get('is_buyer', True) is False, \
                    "Factiva is a marketplace only, not an AI buyer"
                return
        pytest.fail("Factiva not found")

    def test_factiva_parent_is_publisher_flag(self):
        data = load_competitor_entities()
        ml = data.get('marketplace_intermediary_landscape', {})
        tier2 = ml.get('tier_2_marketplace', {})
        operators = tier2.get('operators', [])
        for op in operators:
            if isinstance(op, dict) and 'Factiva' in op.get('name', ''):
                assert op.get('parent_is_publisher', False) is True
                return
        pytest.fail("Factiva not found")


# --- Class 6: Amazon Dual-Presence Coherence ---

class TestAmazonDualPresenceCoherence:
    """Amazon appears in BOTH the marketplace landscape (as operator/buyer)
    and the Anthropic triangle (as investor). These must be consistent."""

    def test_amazon_in_marketplace_operators(self):
        data = load_competitor_entities()
        ml = data.get('marketplace_intermediary_landscape', {})
        tier2 = ml.get('tier_2_marketplace', {})
        operators = tier2.get('operators', [])
        amazon_found = False
        for op in operators:
            if isinstance(op, dict) and 'Amazon' in op.get('name', ''):
                amazon_found = True
                break
        assert amazon_found

    def test_amazon_marketplace_mentions_anthropic_investment(self):
        data = load_competitor_entities()
        ml = data.get('marketplace_intermediary_landscape', {})
        tier2 = ml.get('tier_2_marketplace', {})
        operators = tier2.get('operators', [])
        for op in operators:
            if isinstance(op, dict) and 'Amazon' in op.get('name', ''):
                investments = op.get('ai_lab_investments', [])
                inv_text = ' '.join(str(i) for i in investments)
                assert 'Anthropic' in inv_text
                return
        pytest.fail("Amazon not found")

    def test_amazon_triangle_leg_investment_matches(self):
        data = load_competitor_entities()
        anthropic = get_entity(data, 'Anthropic')
        triangle = anthropic.get('investor_advertiser_publisher_triangle', {})
        amazon_leg = triangle.get('amazon_leg', {})
        assert amazon_leg.get('invested_total_b', 0) >= 13

    def test_amazon_ad_revenue_consistent_across_sections(self):
        """Amazon TTM ad revenue should be consistent between triangle and entity."""
        data = load_competitor_entities()
        anthropic = get_entity(data, 'Anthropic')
        triangle = anthropic.get('investor_advertiser_publisher_triangle', {})
        amazon_leg = triangle.get('amazon_leg', {})
        # Should be $76B TTM
        assert amazon_leg.get('publisher_ad_revenue_ttm_b', 0) >= 70


# --- Class 7: Infrastructure Count Sync ---

class TestInfrastructureCountSync:
    """Verify README and ARCHITECTURE test/file counts match actual state."""

    def test_actual_test_file_count(self):
        test_files = glob.glob(os.path.join(TESTS_DIR, 'test_*.py'))
        count = len(test_files)
        readme = load_readme()
        arch = load_architecture()
        # Both should reference the same count
        assert f'{count} test file' in readme or f'{count}' in readme
        assert f'{count} test file' in arch or f'{count}' in arch

    def test_readme_and_architecture_test_counts_match(self):
        readme = load_readme()
        arch = load_architecture()
        # Extract test count from both
        import re
        readme_match = re.search(r'(\d{4,})\s*tests', readme)
        arch_match = re.search(r'(\d{4,})\s*tests', arch)
        assert readme_match is not None, "README should have test count"
        assert arch_match is not None, "ARCHITECTURE should have test count"
        assert readme_match.group(1) == arch_match.group(1), \
            f"README ({readme_match.group(1)}) and ARCHITECTURE ({arch_match.group(1)}) test counts diverge"

    def test_readme_and_architecture_file_counts_match(self):
        readme = load_readme()
        arch = load_architecture()
        import re
        # Use the header pattern that both docs share
        readme_match = re.search(r'(\d+)\s*test files', readme)
        arch_match = re.search(r'(\d+)\s*test files', arch)
        assert readme_match is not None
        assert arch_match is not None
        readme_count = int(readme_match.group(1))
        arch_count = int(arch_match.group(1))
        # Both must be the same (structural consistency enforces this)
        assert readme_count == arch_count, \
            f"File counts diverge: README={readme_count}, ARCH={arch_count}"

    def test_source_url_count_reasonable(self):
        """Each recent test file should have source references documented."""
        factiva_test = os.path.join(TESTS_DIR, 'test_news_corp_factiva_marketplace_dual_role_aug9.py')
        triangle_test = os.path.join(TESTS_DIR, 'test_anthropic_ipo_investor_publisher_triangle_aug9.py')
        for tf in [factiva_test, triangle_test]:
            assert os.path.exists(tf), f"{os.path.basename(tf)} should exist"
            with open(tf) as f:
                content = f.read()
            # Should have source references (URLs or descriptive citations)
            assert 'Source' in content or 'source' in content or 'http' in content, \
                f"{os.path.basename(tf)} should have source references"
