"""
Test Mechanism #104: TechCrunch (Yahoo/Apollo) Privacy-Improvement-As-Indictment Framing
+ Private Equity AI Infrastructure Financing Chain

Type A: Competitor Coverage Deep Dive (Aug 14, 2026 16:00 PT — Iteration #107)

KEY FINDING: TechCrunch (owned by Yahoo, majority-owned by Apollo Global Management
since Sep 2021) published "Meta wants its AI glasses to seem less creepy. Its AI
strategy says otherwise" on Jul 8, 2026 — the SAME DAY Meta shipped its v26 LED
anti-tamper privacy update. The article reframes the privacy improvement as evidence
of ongoing privacy failure, invoking Cambridge Analytica (2018, 8 years prior),
human reviewer controversy, Instagram AI training opt-out, and NameTag dormant code.

Samsung Galaxy Glasses launched Jul 22, 2026 with IDENTICAL privacy-relevant hardware
(same Snapdragon AR1 Gen 1 chip, camera, LED indicator) and Google Gemini cloud
AI processing. No published data retention policy. No dedicated TechCrunch adversarial
privacy investigation of Samsung's glasses exists.

Apollo Global Management (TechCrunch's parent's parent) co-financed the $35B AI XPV
Platform (announced Jun 9, 2026) for Anthropic and OpenAI compute expansion. Apollo
also separately financing $3.4B for xAI chip leasing (Feb 2026). This $38B+ total
represents the largest documented financial relationship between a publication's
ownership chain and Meta's AI competitors in the dataset.

CONFOUNDING: Yahoo CEO Jim Lanzone is vocally anti-AI-scraping. Yahoo editorial may
operate independently of Apollo investment decisions. Causation NOT established.
This is the first private equity ownership chain in the dataset.

Sources:
  - https://techcrunch.com/2026/07/08/meta-wants-its-ai-glasses-to-seem-less-creepy-its-ai-strategy-says-otherwise/
  - https://www.wsj.com/tech/ai/broadcom-apollo-blackstone-launch-35-billion-ai-infrastructure-platform-8fc8f65e
  - https://www.reuters.com/business/apollo-xai-near-34-billion-deal-fund-ai-chips-information-reports-2026-02-09/
  - https://www.fool.com/investing/2026/06/17/apollo-and-blackstone-just-closed-a-35-billion-pri/
  - https://gizmodo.com/samsung-let-me-touch-its-warby-parker-x-gentle-monster-smart-glasses-but-not-wear-them-2000788835
"""

import yaml
import os
import pytest

RESEARCH_PATH = os.path.join(
    os.path.dirname(__file__), '..', 'profiles', 'competitor-coverage-research.yaml'
)


@pytest.fixture(scope='module')
def research_data():
    with open(RESEARCH_PATH) as f:
        return yaml.safe_load(f)


@pytest.fixture(scope='module')
def mechanism_104(research_data):
    cpf = research_data.get('cross_publication_findings', {})
    section = cpf.get('techcrunch_yahoo_apollo_privacy_indictment_framing')
    assert section is not None, (
        "Missing techcrunch_yahoo_apollo_privacy_indictment_framing in "
        "competitor-coverage-research.yaml cross_publication_findings"
    )
    return section


# ── Class 1: TechCrunch Ownership Chain ─────────────────────────────


class TestTechCrunchOwnershipChain:
    """Verify Yahoo → Apollo ownership chain is documented."""

    def test_publication_is_techcrunch(self, mechanism_104):
        pub = mechanism_104.get('publication', '')
        assert 'TechCrunch' in pub

    def test_yahoo_ownership(self, mechanism_104):
        chain = mechanism_104.get('ownership_chain', {})
        assert chain.get('immediate_parent') == 'Yahoo Inc.'

    def test_apollo_majority_owner(self, mechanism_104):
        chain = mechanism_104.get('ownership_chain', {})
        ultimate = chain.get('ultimate_owner', '')
        assert 'Apollo' in ultimate

    def test_acquisition_date(self, mechanism_104):
        chain = mechanism_104.get('ownership_chain', {})
        assert chain.get('acquisition_date') == '2021-09'

    def test_acquisition_price(self, mechanism_104):
        chain = mechanism_104.get('ownership_chain', {})
        assert chain.get('acquisition_price_usd_billions') == 5

    def test_ownership_archetype(self, mechanism_104):
        archetype = mechanism_104.get('ownership_archetype', '')
        assert 'private equity' in archetype.lower()


# ── Class 2: Apollo AI Financing Relationships ─────────────────────


class TestApolloAIFinancingRelationships:
    """Verify Apollo's financial ties to Anthropic, OpenAI, and xAI."""

    def test_apollo_ai_xpv_platform_exists(self, mechanism_104):
        deals = mechanism_104.get('apollo_ai_financing', {})
        xpv = deals.get('ai_xpv_platform', {})
        assert xpv, "Missing ai_xpv_platform section"

    def test_xpv_platform_amount(self, mechanism_104):
        xpv = mechanism_104.get('apollo_ai_financing', {}).get('ai_xpv_platform', {})
        assert xpv.get('amount_usd_billions') == 35

    def test_xpv_anthropic_is_customer(self, mechanism_104):
        xpv = mechanism_104.get('apollo_ai_financing', {}).get('ai_xpv_platform', {})
        customers = xpv.get('customers', [])
        assert 'Anthropic' in customers

    def test_xpv_openai_is_customer(self, mechanism_104):
        xpv = mechanism_104.get('apollo_ai_financing', {}).get('ai_xpv_platform', {})
        customers = xpv.get('customers', [])
        assert 'OpenAI' in customers

    def test_xpv_date(self, mechanism_104):
        xpv = mechanism_104.get('apollo_ai_financing', {}).get('ai_xpv_platform', {})
        assert xpv.get('announced_date') == '2026-06-09'

    def test_xai_chip_deal(self, mechanism_104):
        deals = mechanism_104.get('apollo_ai_financing', {})
        xai = deals.get('xai_chip_lease', {})
        assert xai.get('amount_usd_billions') == 3.4

    def test_total_exceeds_38b(self, mechanism_104):
        deals = mechanism_104.get('apollo_ai_financing', {})
        total = deals.get('total_ai_financing_usd_billions', 0)
        assert total >= 38

    def test_dwarfs_content_licensing(self, mechanism_104):
        deals = mechanism_104.get('apollo_ai_financing', {})
        total = deals.get('total_ai_financing_usd_billions', 0)
        # News Corp OpenAI deal is ~$250M over 5 years = $50M/yr
        # Apollo total >= $38B = 760x larger
        assert total >= 38, "Apollo financing must dwarf content licensing deals"

    def test_has_xpv_source_url(self, mechanism_104):
        xpv = mechanism_104.get('apollo_ai_financing', {}).get('ai_xpv_platform', {})
        url = xpv.get('source_url', '')
        assert 'wsj.com' in url or 'fool.com' in url or 'reuters.com' in url

    def test_has_xai_source_url(self, mechanism_104):
        xai = mechanism_104.get('apollo_ai_financing', {}).get('xai_chip_lease', {})
        url = xai.get('source_url', '')
        assert 'reuters.com' in url


# ── Class 3: TechCrunch Meta Article Framing ───────────────────────


class TestTechCrunchMetaArticleFraming:
    """Verify the Jul 8, 2026 TechCrunch article's framing characteristics."""

    def test_article_url(self, mechanism_104):
        article = mechanism_104.get('meta_glasses_article', {})
        url = article.get('url', '')
        assert 'techcrunch.com' in url
        assert '2026/07/08' in url

    def test_title_contains_seem_less_creepy(self, mechanism_104):
        article = mechanism_104.get('meta_glasses_article', {})
        title = article.get('title', '')
        assert 'seem less creepy' in title.lower() or 'less creepy' in title.lower()

    def test_title_contains_says_otherwise(self, mechanism_104):
        article = mechanism_104.get('meta_glasses_article', {})
        title = article.get('title', '')
        assert 'says otherwise' in title.lower()

    def test_same_day_as_v26_update(self, mechanism_104):
        article = mechanism_104.get('meta_glasses_article', {})
        assert article.get('publication_date') == '2026-07-08'
        assert article.get('same_day_as_meta_v26_update') is True

    def test_invokes_cambridge_analytica(self, mechanism_104):
        article = mechanism_104.get('meta_glasses_article', {})
        rhetorical = article.get('rhetorical_devices', [])
        device_names = [d.get('device', '') for d in rhetorical]
        examples = [d.get('example', '') for d in rhetorical]
        all_text = ' '.join(device_names + examples).lower()
        assert 'cambridge' in all_text and 'analytica' in all_text, \
            "Article must invoke Cambridge Analytica as historical liability anchor"

    def test_uses_tainted_vocabulary(self, mechanism_104):
        article = mechanism_104.get('meta_glasses_article', {})
        rhetorical = article.get('rhetorical_devices', [])
        all_text = ' '.join(d.get('example', '') for d in rhetorical)
        assert 'tainted' in all_text.lower()

    def test_uses_plows_forward(self, mechanism_104):
        article = mechanism_104.get('meta_glasses_article', {})
        rhetorical = article.get('rhetorical_devices', [])
        all_text = ' '.join(d.get('example', '') for d in rhetorical)
        assert 'plows forward' in all_text.lower()

    def test_improvement_reframed_as_cynicism(self, mechanism_104):
        article = mechanism_104.get('meta_glasses_article', {})
        assert article.get('improvement_reframed_as_cynicism') is True

    def test_meta_tone_adversarial(self, mechanism_104):
        article = mechanism_104.get('meta_glasses_article', {})
        tone = article.get('meta_tone', 0)
        assert tone <= -0.40, f"Meta tone {tone} should be <= -0.40"

    def test_rhetorical_device_count(self, mechanism_104):
        article = mechanism_104.get('meta_glasses_article', {})
        rhetorical = article.get('rhetorical_devices', [])
        assert len(rhetorical) >= 4, \
            f"Need >= 4 rhetorical devices, got {len(rhetorical)}"


# ── Class 4: Samsung Coverage Asymmetry ────────────────────────────


class TestSamsungCoverageAsymmetry:
    """Samsung Galaxy Glasses get no equivalent adversarial TechCrunch coverage."""

    def test_samsung_same_chip(self, mechanism_104):
        samsung = mechanism_104.get('samsung_comparison', {})
        assert 'AR1 Gen 1' in samsung.get('chip', '')

    def test_samsung_has_led(self, mechanism_104):
        samsung = mechanism_104.get('samsung_comparison', {})
        assert samsung.get('has_led_indicator') is True

    def test_samsung_no_published_data_policy(self, mechanism_104):
        samsung = mechanism_104.get('samsung_comparison', {})
        assert samsung.get('published_data_retention_policy') is False

    def test_samsung_zero_tc_adversarial_investigations(self, mechanism_104):
        samsung = mechanism_104.get('samsung_comparison', {})
        assert samsung.get('techcrunch_adversarial_privacy_articles') == 0

    def test_samsung_camera_resolution_undisclosed(self, mechanism_104):
        samsung = mechanism_104.get('samsung_comparison', {})
        assert samsung.get('camera_resolution_disclosed') is False

    def test_samsung_gemini_cloud_processing(self, mechanism_104):
        samsung = mechanism_104.get('samsung_comparison', {})
        assert samsung.get('cloud_ai_processing') == 'Google Gemini'


# ── Class 5: Confounding Factors ───────────────────────────────────


class TestConfoundingFactors:
    """Verify confounding factors are honestly documented."""

    def test_has_confounding_factors(self, mechanism_104):
        factors = mechanism_104.get('confounding_factors', [])
        assert len(factors) >= 4

    def test_yahoo_editorial_independence_noted(self, mechanism_104):
        factors = mechanism_104.get('confounding_factors', [])
        factor_text = ' '.join(f.get('factor', '') for f in factors)
        assert 'editorial independence' in factor_text.lower() or \
               'independent' in factor_text.lower()

    def test_yahoo_anti_ai_scraping_noted(self, mechanism_104):
        factors = mechanism_104.get('confounding_factors', [])
        factor_text = ' '.join(f.get('factor', '') for f in factors)
        assert 'anti-ai' in factor_text.lower() or \
               'rsl' in factor_text.lower() or \
               'scraping' in factor_text.lower()

    def test_causation_not_claimed(self, mechanism_104):
        summary = mechanism_104.get('finding_summary', '')
        assert 'causation not established' in summary.lower() or \
               'not established' in summary.lower()

    def test_has_strong_confounders(self, mechanism_104):
        factors = mechanism_104.get('confounding_factors', [])
        strong_count = sum(1 for f in factors if f.get('strength') == 'STRONG')
        assert strong_count >= 2, "Must have at least 2 STRONG confounders"


# ── Class 6: Cross-Reference Existing Mechanisms ───────────────────


class TestCrossReferenceExistingMechanisms:
    """Verify cross-references to related mechanisms."""

    def test_mechanism_id(self, mechanism_104):
        assert mechanism_104.get('mechanism_id') == 104

    def test_has_cross_references(self, mechanism_104):
        refs = mechanism_104.get('cross_references', [])
        assert len(refs) >= 3

    def test_references_samsung_framing_inversion_93(self, mechanism_104):
        refs = mechanism_104.get('cross_references', [])
        ref_ids = [r.get('mechanism_id', 0) for r in refs if isinstance(r, dict)]
        assert 93 in ref_ids, "Must cross-reference #93 (Samsung Privacy Feature Framing Inversion)"

    def test_references_wired_headline_gap_89(self, mechanism_104):
        refs = mechanism_104.get('cross_references', [])
        ref_ids = [r.get('mechanism_id', 0) for r in refs if isinstance(r, dict)]
        assert 89 in ref_ids, "Must cross-reference #89 (WIRED headline-substance gap)"

    def test_references_news_corp_100(self, mechanism_104):
        refs = mechanism_104.get('cross_references', [])
        ref_ids = [r.get('mechanism_id', 0) for r in refs if isinstance(r, dict)]
        assert 100 in ref_ids, "Must cross-reference #100 (News Corp triple revenue)"

    def test_has_source_urls(self, mechanism_104):
        urls = mechanism_104.get('source_urls', [])
        assert len(urls) >= 5, f"Need >= 5 source URLs, got {len(urls)}"

    def test_finding_summary_length(self, mechanism_104):
        summary = mechanism_104.get('finding_summary', '')
        assert len(summary) >= 200, f"Finding summary too short: {len(summary)} chars"

    def test_date_added(self, mechanism_104):
        assert mechanism_104.get('date_added') == '2026-08-14'

    def test_iteration(self, mechanism_104):
        assert mechanism_104.get('iteration') == 107
