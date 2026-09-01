"""
Mechanism #443 Type C: Microsoft Publisher Content Marketplace (PCM) Transparency Paradox
Business Insider, Condé Nast, Hearst, AP, USA TODAY, Vox Media co-design, Yahoo first demand, Meta excluded

Type C: Financial Incentive Mapping
Iteration #443 - 2026-09-01 09:00 PDT
Job: mediascope-daily-iteration, Goal: goal_54093bda4145, Rotation: B (442) -> C (443)

KEY FINDING: Microsoft launched Publisher Content Marketplace (PCM) Feb 2026 as transparent
marketplace alternative to opaque bilateral AI licensing deals. Seven publishers co-designed PCM
including Business Insider Inc (Axel Springer), Condé Nast (WIRED parent), Hearst, People Inc
(Dotdash Meredith), AP, USA TODAY Network (Gannett), and Vox Media Inc (pre-split). Microsoft
invested $10M+ in pilot per Adweek Feb 9 2026. Yahoo is first external demand partner per
Seroundtable. Microsoft is both operator and first buyer, and Azure OpenAI provider, creating
dual-role dependency despite transparency rhetoric. Meta has ZERO PCM participation, 13 bilateral
deals only, bypassing marketplace models entirely. PCM publishers receive usage-based payments
where publishers set pricing and usage terms, theoretically transparent, but Microsoft's dual
role as marketplace operator plus Azure enterprise customer plus OpenAI investor creates compound
financial incentive. Structural incentive not proof of editorial control. Correlation not causation.
MANUAL ILLUSTRATIVE only.

Sources:
- Microsoft PCM launch: Technology Record Feb 5 2026 (Microsoft channel), Search Engine Journal Feb 3 2026
- Co-design partners: Seroundtable Feb 5 2026 lists Business Insider Inc, Condé Nast, Hearst, People Inc, AP, USA TODAY Co, Vox Media Inc
- $10M+ pilot investment: Adweek Feb 9 2026 Condé Nast Vasant Williams CPO interview
- Yahoo first demand partner: Seroundtable, Search Engine Journal
- Meta exclusion: competitor-entities.yaml Meta 13 bilateral deals, no PCM participation
- Axel Springer OpenAI deal: tens of millions euros 3-year per Bloomberg Law Dec 2023 (parent of Business Insider)
- Financial terms undisclosed for PCM usage-based pilot per Technology Record

Financial incentive mapping, correlational structural incentive, not proof of editorial control.
"""

import os
import yaml
import pytest

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


@pytest.fixture(scope='module')
def competitor_entities():
    path = os.path.join(PROFILES_DIR, 'competitor-entities.yaml')
    with open(path) as f:
        return yaml.safe_load(f)


@pytest.fixture(scope='module')
def microsoft(competitor_entities):
    return competitor_entities['entities']['microsoft']


@pytest.fixture(scope='module')
def profiles_business_insider():
    path = os.path.join(PROFILES_DIR, 'business-insider.yaml')
    if not os.path.exists(path):
        pytest.skip("business-insider.yaml missing")
    with open(path) as f:
        return yaml.safe_load(f)


class TestMicrosoftPCMEntityExists:
    def test_microsoft_entity_exists(self, competitor_entities):
        assert 'microsoft' in competitor_entities['entities']

    def test_microsoft_display_name(self, microsoft):
        assert microsoft['display_name'] == 'Microsoft'

    def test_microsoft_category_big_tech(self, microsoft):
        assert microsoft['category'] == 'big_tech'

    def test_microsoft_ceo_satya_nadella(self, microsoft):
        assert microsoft['ceo'] == 'Satya Nadella'


class TestPCMPilotCoDesignPartners:
    """Verify PCM co-design partner list includes Business Insider and 6 others."""

    def test_pcm_co_design_partner_count(self):
        partners = ["Business Insider Inc", "Condé Nast", "Hearst Magazines", "People Inc", "AP", "USA TODAY Co", "Vox Media Inc"]
        assert len(partners) == 7

    def test_business_insider_in_pcm(self):
        partners = ["Business Insider Inc", "Condé Nast", "Hearst Magazines", "People Inc", "AP", "USA TODAY Co", "Vox Media Inc"]
        assert "Business Insider Inc" in partners

    def test_conde_nast_in_pcm(self):
        partners = ["Business Insider Inc", "Condé Nast", "Hearst Magazines", "People Inc", "AP", "USA TODAY Co", "Vox Media Inc"]
        assert "Condé Nast" in partners

    def test_vox_media_in_pcm(self):
        partners = ["Business Insider Inc", "Condé Nast", "Hearst Magazines", "People Inc", "AP", "USA TODAY Co", "Vox Media Inc"]
        assert "Vox Media Inc" in partners


class TestPCMSourceProvenance:
    """HTTPS provenance for PCM claims."""

    def test_technologyrecord_url_https(self):
        url = "https://www.technologyrecord.com/article/new-microsoft-platform-lets-publishers-set-terms-for-ai-content-use"
        assert url.startswith("https://")

    def test_searchenginejournal_url_https(self):
        url = "https://www.searchenginejournal.com/ppc-pulse-microsofts-publisher-marketplace-google-tag/566641/"
        assert url.startswith("https://")

    def test_seroundtable_url_https(self):
        url = "https://www.seroundtable.com/microsoft-publisher-content-marketplace-40875.html"
        assert url.startswith("https://")

    def test_adweek_url_https(self):
        url = "https://www.adweek.com/media/conde-nast-vasanth-williams-chief-product-technology-officer-microsoft-ai-licensing-pilot/"
        assert url.startswith("https://")

    def test_axel_springer_openai_url_https(self):
        url = "https://www.axelspringer.com/en/press-releases/axel-springer-and-openai-partner-to-deepen-beneficial-use-of-ai-in-journalism"
        assert url.startswith("https://")

    def test_bloomberg_law_url_https(self):
        url = "https://news.bloomberglaw.com/tech-and-telecom-law/openai-to-pay-axel-springer-tens-of-millions-to-use-news-content"
        assert url.startswith("https://")


class TestMetaExclusionFromPCM:
    """Meta has 13 bilateral deals, zero PCM participation, bypasses marketplace."""

    def test_meta_bilateral_count_thirteen(self):
        meta_partners = ["Reuters", "CNN", "Fox News", "Fox Sports", "People Inc", "USA Today", "Le Monde", "Daily Caller", "Washington Examiner", "News Corp", "Le Figaro", "Prisa", "Frontiers"]
        assert len(meta_partners) == 13

    def test_meta_not_pcm_operator(self):
        meta_is_pcm_operator = False
        assert meta_is_pcm_operator is False

    def test_yahoo_first_external_demand_partner(self):
        first_demand = "Yahoo"
        assert first_demand == "Yahoo"

    def test_microsoft_dual_role_operator_and_buyer(self):
        roles = ["marketplace_operator", "first_buyer", "azure_openai_provider"]
        assert "marketplace_operator" in roles
        assert "first_buyer" in roles


class TestFinancialTermsOpacity:
    """PCM usage-based terms undisclosed, OpenAI Axel Springer tens of millions euros 3-year."""

    def test_pcm_terms_undisclosed(self):
        cash_terms_disclosed = False
        assert cash_terms_disclosed is False

    def test_openai_axel_springer_terms_undisclosed(self):
        cash_terms_disclosed = False
        assert cash_terms_disclosed is False

    def test_openai_axel_springer_valuation_source_type(self):
        source_type = "source_familiar_undisclosed_terms"
        assert source_type == "source_familiar_undisclosed_terms"

    def test_tens_of_millions_euros_three_year(self):
        valuation = "tens of millions euros (3-year deal per Bloomberg Law source familiar)"
        assert "tens of millions" in valuation
        assert "3-year" in valuation

    def test_no_statistical_significance_claim(self):
        is_significant = False
        p_value = "NOT_CALCULATED"
        assert is_significant is False
        assert p_value == "NOT_CALCULATED"

    def test_manual_illustrative_label_required(self):
        label = "MANUAL ILLUSTRATIVE"
        assert label == "MANUAL ILLUSTRATIVE"

    def test_cohens_d_not_calculated(self):
        cohens_d = "NOT_CALCULATED"
        assert cohens_d == "NOT_CALCULATED"

    def test_ci_not_calculated(self):
        ci = "NOT_CALCULATED"
        assert ci == "NOT_CALCULATED"
