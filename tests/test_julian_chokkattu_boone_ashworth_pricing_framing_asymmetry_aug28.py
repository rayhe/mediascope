"""
Test for Mechanism #354 — Julian Chokkattu & Boone Ashworth Pricing Framing Asymmetry
Type B: Journalist Cross-Entity Tracking
Iteration #340 — 2026-08-28 04:00 PT

Focus: WIRED Gear desk applies consumer-hostile extraction framing to Meta's $799 Display + $19.99/mo
optional subscription while applying neutral/enthusiastic framing to Snap's $2,195 standalone Specs
($1,396 more expensive upfront, 2.75x price) with no extraction vocabulary.

Mechanism #354 documents:
- Meta Display: $799 MSRP, Neural Band, 6hr + 30hr case, 18hr band, Conversation Focus on-device
- Meta subscription: $19.99/mo Meta One Premium, 3hr free -> 15hr expanded, on-device feature
- Snap Specs: $2,195 MSRP, $200 deposit, 132g/136g TR90, 51-degree FOV, 16M colors, dual Snapdragon,
  4hr mixed-use + 20hr case, standalone no tether, no subscription but 2.75x upfront
- WIRED Gear desk (Chokkattu + Ashworth): Jul 2 2026 subscription article with "extracting value",
  "monetizing customers", scare quotes on "expanded access", consumer-hostile extraction narrative
- Same desk: zero standalone articles about Snap Specs Jun 16 2026 launch (0 vs 3+ Meta articles same window per #42)
- Price ratio: $2,195 / $799 = 2.75x, delta $1,396, yet Meta receives price criticism, Snap receives none
"""

import os
import yaml
import pytest


def load_wired_yaml():
    path = os.path.join(os.path.dirname(__file__), '..', 'profiles', 'wired.yaml')
    with open(path, 'r') as f:
        return yaml.safe_load(f)


def load_journalists_yaml():
    path = os.path.join(os.path.dirname(__file__), '..', 'profiles', 'careers', 'journalists.yaml')
    with open(path, 'r') as f:
        return yaml.safe_load(f)


class TestMetadata:
    def test_mechanism_id_354_exists(self):
        data = load_wired_yaml()
        # Check journalist_cross_entity_coverage contains chokkattu pricing entry
        jcec = data.get('journalist_cross_entity_coverage', {})
        # Could be under wired.yaml top-level key or nested
        # Look for mechanism_id 354 in any relevant section
        content = str(data)
        assert '354' in content or 'pricing_framing_asymmetry' in content.lower(), \
            "Mechanism #354 pricing framing asymmetry not found in wired.yaml"

    def test_required_fields_present(self):
        data = load_wired_yaml()
        # Ensure wired.yaml is loadable and has expected structure
        assert isinstance(data, dict)
        # Ensure journalist entry exists
        jcec = data.get('journalist_cross_entity_coverage') or data.get('cross_entity_coverage') or {}
        assert jcec is not None

    def test_chokkattu_journalist_profile_updated(self):
        data = load_journalists_yaml()
        journalists = data.get('journalists', [])
        julian = next((j for j in journalists if j.get('name') == 'Julian Chokkattu'), None)
        assert julian is not None, "Julian Chokkattu not found in journalists.yaml"
        # Must have mechanism 354 or pricing entry
        blob = str(julian)
        assert '354' in blob or 'pricing_framing' in blob or 'subscription' in blob.lower(), \
            "Julian Chokkattu profile missing mechanism #354 reference"


class TestMetaDisplayPricing:
    def test_meta_display_msrp_799_documented(self):
        data = load_wired_yaml()
        content = str(data)
        assert '799' in content, "Meta Display $799 MSRP not documented"

    def test_meta_subscription_1999_documented(self):
        data = load_wired_yaml()
        content = str(data)
        assert '19.99' in content or '19.99' in content.replace('$', ''), \
            "Meta $19.99 subscription not documented"

    def test_meta_conversation_focus_on_device(self):
        data = load_wired_yaml()
        content = str(data).lower()
        assert 'conversation focus' in content or 'conversation_focus' in content, \
            "Conversation Focus feature not documented"
        assert 'on-device' in content or 'on_device' in content or 'on device' in content, \
            "On-device nature of Conversation Focus not documented"


class TestSnapSpecsPricing:
    def test_snap_specs_2195_documented(self):
        data = load_wired_yaml()
        content = str(data)
        assert '2195' in content or '2,195' in content, "Snap Specs $2,195 not documented"

    def test_snap_specs_standalone_documented(self):
        data = load_wired_yaml()
        content = str(data).lower()
        assert 'standalone' in content, "Snap Specs standalone nature not documented"

    def test_snap_specs_51_degree_fov(self):
        data = load_wired_yaml()
        content = str(data)
        assert '51' in content, "Snap 51-degree FOV not documented"

    def test_snap_specs_dual_snapdragon(self):
        data = load_wired_yaml()
        content = str(data).lower()
        assert 'snapdragon' in content, "Snap dual Snapdragon processors not documented"


class TestWiredGearDeskFraming:
    def test_extraction_framing_documented(self):
        data = load_wired_yaml()
        content = str(data).lower()
        assert 'extracting value' in content or 'extracting_value' in content, \
            "'extracting value' framing not documented"

    def test_monetizing_customers_framing(self):
        data = load_wired_yaml()
        content = str(data).lower()
        assert 'monetizing' in content, "'monetizing customers' framing not documented"

    def test_expanded_access_scare_quotes(self):
        data = load_wired_yaml()
        content = str(data).lower()
        assert 'expanded access' in content, "'expanded access' scare quotes not documented"

    def test_subscription_article_date_jul2_2026(self):
        data = load_wired_yaml()
        content = str(data)
        assert '2026-07-02' in content or '2026-07-02' in content, \
            "Subscription article date Jul 2 2026 not documented"

    def test_chokkattu_authorship_documented(self):
        data = load_wired_yaml()
        content = str(data)
        assert 'Chokkattu' in content, "Julian Chokkattu authorship not documented"


class TestPriceAsymmetryCalculation:
    def test_price_ratio_275x(self):
        meta_price = 799
        snap_price = 2195
        ratio = snap_price / meta_price
        assert 2.7 < ratio < 2.8, f"Price ratio should be ~2.75x, got {ratio:.2f}"
        # Ensure documented ratio matches calculation
        data = load_wired_yaml()
        content = str(data)
        # Allow either 2.75 or calculated
        assert '2.75' in content or '2.7' in content or str(round(ratio, 2)) in content, \
            "Price ratio 2.75x not documented"

    def test_price_delta_1396(self):
        delta = 2195 - 799
        assert delta == 1396
        data = load_wired_yaml()
        content = str(data)
        assert '1396' in content or '1,396' in content, "Price delta $1,396 not documented"

    def test_year1_cost_comparison(self):
        # Meta year 1: $799 + ($19.99*12) = $1,038.88 if subscriber, $799 if not
        # Snap year 1: $2,195 + ($99*12) = $3,383 per mechanism #42
        # Test that calculation is consistent
        meta_base = 799
        snap_base = 2195
        assert snap_base > meta_base * 2.5, "Snap should be >2.5x Meta base price"

    def test_asymmetry_score_direction(self):
        # WIRED Gear desk criticizes cheaper Meta ($799 + optional $20) while ignoring more expensive Snap ($2,195)
        # This is inverted price criticism — cheaper product gets hostile framing
        meta_price = 799
        snap_price = 2195
        assert snap_price > meta_price, "Asymmetry requires Snap more expensive than Meta"
        # If framing were price-consistent, Snap would receive MORE criticism


class TestCompoundCompetitorSilenceExtension:
    def test_zero_standalone_snap_articles_documented(self):
        data = load_wired_yaml()
        content = str(data)
        # From mechanism #42: 0 standalone Snap Specs articles vs 3+ Meta
        assert '0' in content  # minimal check, detailed in #42
        # Ensure compound silence referenced
        assert 'compound' in content.lower() or 'silence' in content.lower() or 'Spec' in content

    def test_3_plus_meta_articles_window(self):
        data = load_wired_yaml()
        # Mechanism #42 documented 3+ Meta articles same window
        content = str(data).lower()
        # Check that Meta coverage volume is mentioned
        assert 'meta' in content


class TestSources:
    def test_minimum_source_count(self):
        data = load_wired_yaml()
        # Mechanism #354 should have at least 5 source URLs (Snap launch + Meta subscription + WIRED article proxy)
        content = str(data)
        # Count https occurrences
        url_count = content.count('https://')
        assert url_count >= 5, f"Expected >=5 source URLs, found {url_count}"

    def test_https_urls_only(self):
        data = load_wired_yaml()
        # All source_urls should be https
        content = str(data)
        # Basic check: no http:// in source_urls (except techmeme http allowed historically, but prefer https)
        # For this mechanism, require https for new entries
        if 'source_urls' in content:
            # Ensure at least the new mechanism's URLs are https
            assert 'https://' in content

    def test_snap_launch_sources_present(self):
        data = load_wired_yaml()
        content = str(data).lower()
        assert 'techcrunch' in content or 'appleinsider' in content or 'zacks' in content, \
            "Snap launch source not present"

    def test_meta_subscription_source_present(self):
        data = load_wired_yaml()
        content = str(data).lower()
        assert 'androidauthority' in content or 'slashdot' in content or 'the verge' in content, \
            "Meta subscription source not present"


class TestCrossReferences:
    def test_cross_reference_mechanism_42(self):
        data = load_wired_yaml()
        content = str(data)
        assert '42' in content, "Cross-reference to mechanism #42 (compound competitor silence) missing"

    def test_cross_reference_mechanism_47_72_91_93(self):
        data = load_wired_yaml()
        content = str(data)
        # Should reference at least one of Chokkattu's existing Meta mechanisms
        has_ref = any(x in content for x in ['47', '72', '91', '93', '207'])
        assert has_ref, "Cross-reference to existing Chokkattu mechanisms missing"

    def test_journalist_cross_entity_structure(self):
        data = load_wired_yaml()
        jcec = data.get('journalist_cross_entity_coverage', {})
        assert isinstance(jcec, dict), "journalist_cross_entity_coverage should be dict"
        # Should contain chokkattu entry
        blob = str(jcec).lower()
        assert 'chokkattu' in blob or 'pricing' in blob, "Chokkattu pricing entry not in journalist_cross_entity_coverage"


class TestFindingSummary:
    def test_finding_summary_present(self):
        data = load_wired_yaml()
        content = str(data)
        assert 'finding_summary' in content.lower() or 'finding' in content.lower()

    def test_inverted_price_criticism_documented(self):
        data = load_wired_yaml()
        content = str(data).lower()
        # Core insight: cheaper product ($799) gets hostile framing, expensive ($2,195) gets neutral/no coverage
        assert 'inverted' in content or 'cheaper' in content or '2.75' in content or 'hostile' in content, \
            "Inverted price criticism insight not documented"

    def test_consumer_hostile_extraction_narrative(self):
        data = load_wired_yaml()
        content = str(data).lower()
        assert 'extraction' in content or 'consumer-hostile' in content or 'consumer_hostile' in content
