"""
Test: Apple-Google $1B/yr Gemini Deal — Publisher Content Laundering Chain
Type C: Financial Incentive Mapping
Date: 2026-08-07

KEY FINDING:

Apple's $1B/yr deal with Google (announced Jan 12, 2026; Bloomberg reported
Nov 5, 2025) creates a financial pipeline where publisher content reaches
Apple's 2B+ devices WITHOUT direct publisher compensation:

  Publisher Content → Google Gemini Training → Apple $1B License → Siri → Users

Apple negotiated directly with publishers (Dec 2023: $50M offers to Condé
Nast, NBC News, IAC) but no confirmed publisher content deal was signed.
Instead, Apple bypassed publisher licensing by paying Google for a pre-trained
model — effectively laundering publisher content through Google's training
pipeline.

This contrasts with direct publisher licensing by:
  - Meta: $50M/yr to News Corp (direct)
  - OpenAI: Direct deals with NYT, People Inc., Condé Nast, etc.
  - Amazon: Direct deals with NYT ($20-25M), Condé Nast, Hearst

The publisher content laundering chain means:
1. Google trains Gemini on publisher content (Hachette/Cengage lawsuit confirms)
2. Apple pays Google $1B/yr for Gemini model access
3. Apple runs Gemini on Private Cloud Compute for Siri (2B+ devices)
4. Publishers receive $0 from Apple for content flowing through this chain
5. Apple avoids the legal/PR cost of scraping AND the financial cost of licensing

Sources:
- Bloomberg (Nov 5, 2025): https://www.macrumors.com/2025/11/05/apple-google-new-siri-payment/
- Reuters (Jan 12, 2026): https://www.reuters.com/business/google-apple-enter-into-multi-year-ai-deal-gemini-models-2026-01-12/
- CNN (Jan 12, 2026): https://www.cnn.com/2026/01/12/tech/apple-google-gemini-siri
- Motley Fool (Jun 26, 2026): https://www.fool.com/investing/2026/06/26/apple-paying-google-billion-year-for-ai-winner/
- Apple publisher negotiations (Dec 2023): https://www.reuters.com/technology/apple-explores-ai-deals-with-news-publishers-new-york-times-2023-12-22/
- Google copyright lawsuit (Jul 2026): https://www.hachettebookgroup.com/hachette-book-group-news/publishers-and-authors-file-class-action-lawsuit-against-google-for-willful-copyright-infringement-to-develop-gemini-ai-models/
"""

import yaml
import os
import pytest

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


def load_competitor_entities():
    path = os.path.join(PROFILES_DIR, 'competitor-entities.yaml')
    with open(path) as f:
        return yaml.safe_load(f)


def load_competitor_research():
    path = os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml')
    with open(path) as f:
        return yaml.safe_load(f)


def load_publication_profile(name):
    path = os.path.join(PROFILES_DIR, f'{name}.yaml')
    with open(path) as f:
        return yaml.safe_load(f)


class TestAppleGoogleGeminiDeal:
    """Verify the Apple-Google Gemini deal is documented with correct terms."""

    def test_apple_entity_exists(self):
        data = load_competitor_entities()
        assert 'apple' in data['entities']

    def test_apple_google_gemini_deal_exists(self):
        data = load_competitor_entities()
        apple = data['entities']['apple']
        assert 'apple_google_gemini_deal' in apple, \
            "Apple entity must document the $1B/yr Google Gemini deal"

    def test_gemini_deal_annual_value(self):
        data = load_competitor_entities()
        deal = data['entities']['apple']['apple_google_gemini_deal']
        assert deal.get('annual_value_b') == 1.0 or deal.get('annual_value_est_b') == 1.0, \
            "Deal value should be approximately $1B/yr"

    def test_gemini_deal_announcement_date(self):
        data = load_competitor_entities()
        deal = data['entities']['apple']['apple_google_gemini_deal']
        assert '2026-01' in str(deal.get('announcement_date', '')), \
            "Deal announced January 12, 2026"

    def test_gemini_deal_bloomberg_report_date(self):
        data = load_competitor_entities()
        deal = data['entities']['apple']['apple_google_gemini_deal']
        assert '2025-11' in str(deal.get('bloomberg_report_date', '')), \
            "Bloomberg first reported November 5, 2025"

    def test_gemini_deal_model_parameters(self):
        data = load_competitor_entities()
        deal = data['entities']['apple']['apple_google_gemini_deal']
        assert '1.2' in str(deal.get('model_parameters', '')), \
            "Custom Gemini model has 1.2 trillion parameters"

    def test_gemini_deal_has_source_urls(self):
        data = load_competitor_entities()
        deal = data['entities']['apple']['apple_google_gemini_deal']
        urls = deal.get('source_urls', [])
        assert len(urls) >= 2, "At least 2 source URLs (Bloomberg/Reuters)"

    def test_gemini_runs_on_apple_servers(self):
        data = load_competitor_entities()
        deal = data['entities']['apple']['apple_google_gemini_deal']
        combined = str(deal.get('detail', '')) + ' ' + str(deal.get('overview', ''))
        assert 'private cloud compute' in combined.lower() or 'pcc' in combined.lower(), \
            "Should note Gemini runs on Apple's Private Cloud Compute"

    def test_gemini_deal_context_vs_search_deal(self):
        """The $1B/yr Gemini deal is dwarfed by Google's $20B/yr search deal."""
        data = load_competitor_entities()
        deal = data['entities']['apple']['apple_google_gemini_deal']
        overview = str(deal.get('detail', '') or deal.get('overview', ''))
        assert '20' in overview or 'search' in overview.lower(), \
            "Should contextualize against the $20B/yr Google search deal"


class TestPublisherContentLaunderingChain:
    """Verify the publisher content laundering chain analysis."""

    def test_laundering_chain_documented(self):
        data = load_competitor_entities()
        apple = data['entities']['apple']
        assert 'publisher_content_chain' in apple or \
               'publisher_content_laundering' in apple or \
               'publisher_content_bypass' in apple, \
            "Must document how Apple bypasses publisher licensing via Google"

    def test_chain_identifies_zero_publisher_deals(self):
        data = load_competitor_entities()
        apple = data['entities']['apple']
        # Check in the content chain section or the main entity
        chain_key = None
        for key in ['publisher_content_chain', 'publisher_content_laundering', 'publisher_content_bypass']:
            if key in apple:
                chain_key = key
                break
        assert chain_key is not None
        chain = apple[chain_key]
        chain_str = str(chain).lower()
        assert 'zero' in chain_str or '0' in chain_str or 'no deal' in chain_str or 'no publisher' in chain_str, \
            "Must note Apple has zero confirmed publisher content deals"

    def test_chain_references_dec_2023_negotiations(self):
        data = load_competitor_entities()
        apple = data['entities']['apple']
        chain_key = None
        for key in ['publisher_content_chain', 'publisher_content_laundering', 'publisher_content_bypass']:
            if key in apple:
                chain_key = key
                break
        assert chain_key is not None
        chain_str = str(apple[chain_key]).lower()
        assert '2023' in chain_str or 'condé nast' in chain_str.replace('conde', 'condé') or \
               'conde nast' in chain_str, \
            "Must reference the Dec 2023 publisher negotiations (Condé Nast, NBC News, IAC)"

    def test_chain_references_google_training_lawsuit(self):
        data = load_competitor_entities()
        apple = data['entities']['apple']
        chain_key = None
        for key in ['publisher_content_chain', 'publisher_content_laundering', 'publisher_content_bypass']:
            if key in apple:
                chain_key = key
                break
        assert chain_key is not None
        chain_str = str(apple[chain_key]).lower()
        assert 'hachette' in chain_str or 'cengage' in chain_str or \
               'copyright' in chain_str or 'lawsuit' in chain_str, \
            "Must reference the Google copyright lawsuit confirming content was used in training"


class TestAppleVsMetaPublisherDealContrast:
    """Compare Apple's content bypass with Meta's direct licensing."""

    def test_meta_has_direct_publisher_deals(self):
        """Meta's publisher deal info is documented in Apple's content bypass comparison."""
        data = load_competitor_entities()
        apple = data['entities']['apple']
        chain_key = None
        for key in ['publisher_content_chain', 'publisher_content_laundering', 'publisher_content_bypass']:
            if key in apple:
                chain_key = key
                break
        assert chain_key is not None
        chain_str = str(apple[chain_key]).lower()
        assert 'meta' in chain_str and ('50m' in chain_str or 'news corp' in chain_str), \
            "Apple content bypass section should reference Meta's $50M/yr News Corp deal for contrast"

    def test_apple_has_no_confirmed_publisher_deals(self):
        data = load_competitor_entities()
        apple = data['entities']['apple']
        # Apple should have documentation of negotiations but no confirmed deals
        chain_key = None
        for key in ['publisher_content_chain', 'publisher_content_laundering', 'publisher_content_bypass']:
            if key in apple:
                chain_key = key
                break
        chain_str = str(apple.get(chain_key, '')).lower()
        overview = str(apple.get('publisher_content_bypass', {}).get('overview', '')).lower()
        combined = chain_str + ' ' + overview
        assert 'zero' in combined or 'no deal' in combined or 'no confirmed' in combined, \
            "Apple entity should indicate negotiations but no confirmed deals"

    def test_openai_has_multiple_publisher_deals(self):
        """OpenAI's publisher deals are documented in Apple's content bypass comparison."""
        data = load_competitor_entities()
        apple = data['entities']['apple']
        chain_key = None
        for key in ['publisher_content_chain', 'publisher_content_laundering', 'publisher_content_bypass']:
            if key in apple:
                chain_key = key
                break
        assert chain_key is not None
        chain_str = str(apple[chain_key]).lower()
        assert 'openai' in chain_str, \
            "Apple content bypass should reference OpenAI's direct publisher deals for contrast"

    def test_amazon_has_direct_publisher_deals(self):
        data = load_competitor_entities()
        amazon = data['entities']['amazon']
        amazon_str = str(amazon).lower()
        assert 'nyt' in amazon_str or 'new york times' in amazon_str or \
               'condé nast' in amazon_str or 'conde nast' in amazon_str or \
               'hearst' in amazon_str, \
            "Amazon entity should list direct publisher deals"


class TestAppleGeminiDealCondeNastImplications:
    """Test implications for Condé Nast (WIRED's parent)."""

    def test_conde_nast_was_in_apple_negotiations(self):
        """Condé Nast was explicitly approached by Apple in Dec 2023."""
        data = load_competitor_entities()
        apple = data['entities']['apple']
        apple_str = str(apple).lower()
        assert 'condé nast' in apple_str.replace('conde', 'condé') or \
               'conde nast' in apple_str, \
            "Apple entity must note Condé Nast was in Dec 2023 negotiations"

    def test_conde_nast_has_openai_deal(self):
        """Condé Nast has an active OpenAI licensing deal (Aug 2024)."""
        data = load_competitor_research()
        wired = data['publications']['wired']
        wired_str = str(wired).lower()
        assert 'openai' in wired_str, \
            "WIRED profile must reference the Condé Nast-OpenAI deal"

    def test_conde_nast_has_amazon_deal(self):
        """Condé Nast has an Amazon Rufus licensing deal (Jul 2025)."""
        data = load_competitor_research()
        wired = data['publications']['wired']
        wired_str = str(wired).lower()
        assert 'amazon' in wired_str or 'rufus' in wired_str, \
            "WIRED profile must reference the Condé Nast-Amazon deal"

    def test_conde_nast_has_microsoft_deal(self):
        """Condé Nast has a Microsoft PCM deal (Feb 2026)."""
        data = load_competitor_research()
        wired = data['publications']['wired']
        wired_str = str(wired).lower()
        assert 'microsoft' in wired_str or 'pcm' in wired_str, \
            "WIRED profile must reference the Condé Nast-Microsoft deal"

    def test_conde_nast_zero_meta_deal(self):
        """Condé Nast has NO Meta content licensing deal."""
        data = load_competitor_research()
        wired = data['publications']['wired']
        meta_tone = wired.get('meta_coverage_tone', '')
        assert meta_tone == 'adversarial', \
            "WIRED's Meta coverage is adversarial — no financial relationship"


class TestApplePublisherNegotiationTimeline:
    """Verify the timeline of Apple's failed publisher negotiations."""

    def test_negotiations_started_dec_2023(self):
        data = load_competitor_entities()
        apple = data['entities']['apple']
        chain_key = None
        for key in ['publisher_content_chain', 'publisher_content_laundering', 'publisher_content_bypass']:
            if key in apple:
                chain_key = key
                break
        assert chain_key is not None
        chain_str = str(apple[chain_key])
        assert '2023' in chain_str, "Must reference Dec 2023 start of negotiations"

    def test_offered_fifty_million(self):
        """Apple offered $50M for multi-year publisher content deals."""
        data = load_competitor_entities()
        apple = data['entities']['apple']
        chain_key = None
        for key in ['publisher_content_chain', 'publisher_content_laundering', 'publisher_content_bypass']:
            if key in apple:
                chain_key = key
                break
        assert chain_key is not None
        chain_str = str(apple[chain_key])
        assert '50' in chain_str, "Must note the $50M offer amount"

    def test_publishers_were_lukewarm(self):
        """Some publishers were lukewarm on Apple's offer."""
        data = load_competitor_entities()
        apple = data['entities']['apple']
        chain_key = None
        for key in ['publisher_content_chain', 'publisher_content_laundering', 'publisher_content_bypass']:
            if key in apple:
                chain_key = key
                break
        assert chain_key is not None
        chain_str = str(apple[chain_key]).lower()
        assert 'lukewarm' in chain_str or 'declined' in chain_str or \
               'stalled' in chain_str or 'no confirmed' in chain_str or \
               'not signed' in chain_str, \
            "Must note publishers were unenthusiastic or deals didn't close"

    def test_negotiations_preceded_gemini_deal(self):
        """Publisher negotiations (Dec 2023) predated Gemini deal (Jan 2026) by 2 years."""
        data = load_competitor_entities()
        apple = data['entities']['apple']
        chain_key = None
        for key in ['publisher_content_chain', 'publisher_content_laundering', 'publisher_content_bypass']:
            if key in apple:
                chain_key = key
                break
        assert chain_key is not None
        chain_str = str(apple[chain_key]).lower()
        # Should note the timeline gap
        assert ('2023' in chain_str and '2026' in chain_str) or \
               'year' in chain_str or 'preceded' in chain_str, \
            "Must note the 2-year gap between publisher negotiations and Gemini deal"


class TestGoogleTrainingContentEvidence:
    """Verify evidence that Google trained Gemini on publisher content."""

    def test_google_entity_has_copyright_lawsuit(self):
        data = load_competitor_entities()
        google = data['entities']['google']
        assert 'publisher_litigation_jul2026' in google, \
            "Google entity must document the Jul 2026 copyright lawsuit"

    def test_hachette_cengage_elsevier_plaintiffs(self):
        data = load_competitor_entities()
        lawsuit = data['entities']['google']['publisher_litigation_jul2026']
        plaintiffs = lawsuit.get('plaintiffs', [])
        plaintiff_str = ' '.join(str(p) for p in plaintiffs).lower()
        assert 'hachette' in plaintiff_str, "Hachette must be listed as plaintiff"
        assert 'cengage' in plaintiff_str, "Cengage must be listed as plaintiff"
        assert 'elsevier' in plaintiff_str, "Elsevier must be listed as plaintiff"

    def test_lawsuit_alleges_millions_of_works(self):
        data = load_competitor_entities()
        lawsuit = data['entities']['google']['publisher_litigation_jul2026']
        detail = str(lawsuit.get('detail', '')).lower()
        assert 'million' in detail, \
            "Lawsuit alleges Google copied millions of books/articles"

    def test_google_internal_fine_estimate(self):
        """Google internally flagged $10Bs-$100Bs in potential fines."""
        data = load_competitor_entities()
        lawsuit = data['entities']['google']['publisher_litigation_jul2026']
        detail = str(lawsuit.get('detail', '')).lower()
        assert 'fine' in detail or 'billion' in detail, \
            "Must note Google's internal fine estimate"


class TestFinancialChainArithmetic:
    """Verify the financial arithmetic of the content chain."""

    def test_apple_pays_google_1b(self):
        """Apple pays Google $1B/yr for Gemini."""
        data = load_competitor_entities()
        deal = data['entities']['apple']['apple_google_gemini_deal']
        val = deal.get('annual_value_b') or deal.get('annual_value_est_b')
        assert val == 1.0

    def test_google_pays_apple_20b_search(self):
        """Google pays Apple $20B/yr for default search — 20x the Gemini deal."""
        data = load_competitor_entities()
        deal = data['entities']['apple']['apple_google_gemini_deal']
        overview = str(deal.get('detail', '') or deal.get('overview', ''))
        assert '20' in overview, "Must note Google's $20B/yr search payment for context"

    def test_meta_pays_news_corp_50m(self):
        """Meta's $50M/yr News Corp deal is referenced in Apple's content chain comparison."""
        data = load_competitor_entities()
        apple = data['entities']['apple']
        chain_key = None
        for key in ['publisher_content_chain', 'publisher_content_laundering', 'publisher_content_bypass']:
            if key in apple:
                chain_key = key
                break
        assert chain_key is not None
        chain_str = str(apple[chain_key]).lower()
        assert 'meta' in chain_str and '50m' in chain_str, \
            "Content chain comparison must reference Meta's $50M/yr direct deal"

    def test_apple_pays_publishers_zero(self):
        """Apple pays publishers $0 despite content flowing through Gemini."""
        data = load_competitor_entities()
        apple = data['entities']['apple']
        chain_key = None
        for key in ['publisher_content_chain', 'publisher_content_laundering', 'publisher_content_bypass']:
            if key in apple:
                chain_key = key
                break
        assert chain_key is not None
        chain_str = str(apple[chain_key]).lower()
        assert '$0' in chain_str or 'zero' in chain_str or 'nothing' in chain_str, \
            "Must explicitly state publishers receive $0 from Apple"


class TestSourceCitations:
    """Verify all claims have proper source URLs."""

    def test_gemini_deal_sources(self):
        data = load_competitor_entities()
        deal = data['entities']['apple']['apple_google_gemini_deal']
        urls = deal.get('source_urls', [])
        assert any('reuters' in url or 'bloomberg' in url or 'macrumors' in url for url in urls), \
            "Must cite Bloomberg/Reuters/MacRumors for deal terms"

    def test_publisher_negotiations_source(self):
        data = load_competitor_entities()
        apple = data['entities']['apple']
        chain_key = None
        for key in ['publisher_content_chain', 'publisher_content_laundering', 'publisher_content_bypass']:
            if key in apple:
                chain_key = key
                break
        assert chain_key is not None
        chain = apple[chain_key]
        urls = chain.get('source_urls', [])
        assert len(urls) >= 1, "Publisher negotiations must have at least 1 source URL"

    def test_google_lawsuit_sources(self):
        data = load_competitor_entities()
        lawsuit = data['entities']['google']['publisher_litigation_jul2026']
        urls = lawsuit.get('source_urls', [])
        assert len(urls) >= 1, "Google lawsuit must have source URLs"


class TestCrossFileConsistency:
    """Verify cross-file consistency between entities and research profiles."""

    def test_wired_profile_matches_entities(self):
        """WIRED profile's deal descriptions should be consistent with entities."""
        research = load_competitor_research()
        entities = load_competitor_entities()
        wired = research['publications']['wired']
        # WIRED's openai_coverage_tone should exist
        assert 'openai_coverage_tone' in wired
        # OpenAI entity should exist
        assert 'openai' in entities['entities']

    def test_apple_entity_openai_collapse_still_present(self):
        """Existing Apple-OpenAI partnership collapse should not be overwritten."""
        data = load_competitor_entities()
        apple = data['entities']['apple']
        assert 'openai_partnership_collapse' in apple, \
            "Apple-OpenAI partnership collapse must remain documented"

    def test_apple_entity_has_both_google_and_openai_sections(self):
        """Apple entity should document BOTH the Gemini deal AND the OpenAI collapse."""
        data = load_competitor_entities()
        apple = data['entities']['apple']
        assert 'apple_google_gemini_deal' in apple, "Must have Gemini deal section"
        assert 'openai_partnership_collapse' in apple, "Must have OpenAI collapse section"

    def test_google_entity_has_network_revenue_data(self):
        """Google entity should have network revenue decline data."""
        data = load_competitor_entities()
        google = data['entities']['google']
        assert 'network_revenue_decline' in google or 'advertising_dependency_coercion' in google
