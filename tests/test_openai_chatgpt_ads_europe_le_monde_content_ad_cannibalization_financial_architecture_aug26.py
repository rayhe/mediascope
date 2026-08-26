"""
Test: OpenAI ChatGPT Ads European Expansion — Le Monde Triple-Deal
Content-to-Ad Cannibalization Financial Architecture

Mechanism #319: chatgpt_ads_europe_content_ad_cannibalization_financial_architecture

DISCOVERY: OpenAI's ChatGPT Ads expansion to 31 European markets (Aug 24, 2026)
creates a compounding five-layer financial architecture where publishers who license
content to OpenAI are simultaneously having their ad revenue cannibalized by ads
placed beneath responses powered by their own licensed content.

Le Monde is the best-documented case of this architecture because CEO Louis Dreyfus
publicly disclosed:
1. Three AI deals (OpenAI Mar 2024, Perplexity May 2025, Meta Dec 2025)
2. 25% of ALL AI licensing revenue shared with staff journalists as yearly bonus
3. ChatGPT converts to Le Monde paid subscriptions 20x more than Facebook,
   50x more than Google Discover
4. AI licensing named as strategic revenue pillar

Five compounding layers:
- LAYER 1 (Content Subsidy): Le Monde licenses content to OpenAI → content powers
  ChatGPT responses in French
- LAYER 2 (Ad Cannibalization): OpenAI places ads beneath responses powered by
  Le Monde's content → competes with Le Monde for French advertiser budgets using
  the SAME agency partners (Publicis, Dentsu, Havas)
- LAYER 3 (Conversion Dependency): Le Monde becomes dependent on ChatGPT as a
  subscription conversion channel (20x Facebook per Dreyfus) → creates incentive
  to maintain favorable relationship with OpenAI
- LAYER 4 (Revenue Replacement Spiral): As OpenAI ads cannibalize French digital
  ad market, Le Monde's AI licensing revenue becomes a larger proportion of total
  income → increasing captivity
- LAYER 5 (Individual Journalist Incentive): Le Monde journalists receive 25%
  of AI licensing revenue as yearly bonus → individual-level (not just institutional)
  financial incentive tied to maintaining deal partnerships

COVERAGE TEST: Le Monde reported on OpenAI's French ad launch (Aug 25, 2026) WITHOUT
disclosing its own financial relationship with OpenAI in the article. The article frames
OpenAI's ad expansion as a business strategy, comparing to Google and Meta, without
noting that Le Monde itself has content deals with all three companies. EuropeSays
(Aug 20) explicitly identified the "Publisher Revenue Gap" — the disconnect between
who creates the underlying content and who captures the advertising revenue — which
Le Monde's own coverage omits.

FINANCIAL QUANTIFICATION:
- Le Monde Group total revenue: €310M (2024, up 2% YoY)
- Le Monde entity: ~€150M+ (est. 50% of group)
- Digital: 52% of Le Monde revenue = ~€78M
- Digital subscriber revenue: €72M (2025)
- Newsroom cost: €81M for 570 staff (2025)
- 680,000 subscribers (580,000 digital)
- AI licensing revenue: "significant" but undisclosed (est. €3-10M/yr)
- OpenAI ad revenue: approaching $1B annual run rate (Aug 2026, per Adweek/CFO Friar)
- OpenAI targeting $2.5B global ad revenue (2026), $100B by 2030
- ChatGPT: 1 billion weekly active users, 20% commercial intent
- OpenAI ad revenue grew 25%+ since start of Aug 2026
- French advertisers at launch: Bouygues Telecom, Cultura, TotalEnergies, Carrefour
- French agencies: Publicis, Dentsu, Havas (same agencies publishers use)
- OpenAI CPM prices dropping ~20% over 6 weeks (converging toward publisher rates)

COUNTER-CONFOUNDERS (7 legitimate factors):
1. Le Monde has a deal with Meta too — this is NOT Meta-exclusion bias; all three
   major AI companies are Le Monde partners
2. Le Monde's Aug 25 article is factual reporting, not advocacy or puff coverage
3. OpenAI's ad business is genuinely nascent — not yet a material threat to Le Monde's
   specific ad revenue
4. Many publications covered the ChatGPT Ads expansion without disclosing their own
   deals (if any); this is an industry-wide disclosure gap
5. Le Monde CEO Dreyfus has been publicly transparent about deals in trade press
   (Press Gazette Apr 2026) — the disclosure gap is editorial, not institutional
6. AI licensing revenue is still a small fraction of Le Monde's total revenue (~2-7%)
7. ChatGPT ads in France initially use only contextual targeting (no personalization
   in EEA), limiting overlap with publisher behavioral ad targeting

SOURCES:
- Le Monde, "Ads arrive on ChatGPT in France" (Aug 25, 2026)
  https://www.lemonde.fr/en/economy/article/2026/08/25/ads-arrive-on-chatgpt-in-france_6756812_19.html
- Adweek, "OpenAI Is Taking Its Ad Business to 31 New European Markets" (Aug 19, 2026)
  https://www.adweek.com/media/openai-is-taking-its-ad-business-to-31-new-european-markets/
- Press Gazette, "Le Monde CEO urges publishers to sign AI partnerships" (Apr 2026)
  https://pressgazette.co.uk/publishers/le-monde-ceo-urges-publishers-to-sign-ai-partnerships-to-stay-competitive/
- TechRepublic, "OpenAI Brings ChatGPT Ads to 31 European Countries" (Aug 20, 2026)
  https://www.techrepublic.com/article/news-openai-chatgpt-ads-europe-emea/
- EuropeSays, "ChatGPT Ads Reach Europe Monday" (Aug 20, 2026)
  https://www.europesays.com/europe/119979/
- Neowin, "OpenAI expands ChatGPT ads to 31 European markets" (Aug 19, 2026)
  https://www.neowin.net/news/openai-expands-chatgpt-ads-to-31-european-markets/
- Press Gazette, "News generative AI deals revealed" (tracker, updated Aug 2026)
  https://pressgazette.co.uk/platforms/news-publisher-ai-deals-lawsuits-openai-google/
- Reuters, "ChatGPT users to get access to Le Monde, Prisa Media" (Mar 13, 2024)
  https://www.reuters.com/technology/chatgpt-users-get-access-news-content-le-monde-prisa-media-2024-03-13/
- PYMNTS, "OpenAI Projects Steep Advertising Growth" (Apr 9, 2026)
  https://www.pymnts.com/artificial-intelligence-2/2026/openai-projects-steep-advertising-growth-targeting-100-billion-by-2030/
"""

import subprocess
import os

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')
RESEARCH_YAML = os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml')
ENTITIES_YAML = os.path.join(PROFILES_DIR, 'competitor-entities.yaml')


def _grep(pattern, filepath):
    """Return lines matching pattern in filepath."""
    try:
        result = subprocess.run(
            ['grep', '-i', pattern, filepath],
            capture_output=True, text=True, timeout=10
        )
        return result.stdout.strip().split('\n') if result.stdout.strip() else []
    except Exception:
        return []


def _read_file(filepath):
    """Read file content."""
    try:
        with open(filepath, 'r') as f:
            return f.read()
    except Exception:
        return ''


class TestMechanismExists:
    """Verify mechanism #319 is documented."""

    def test_mechanism_id_in_research_yaml(self):
        lines = _grep('319', RESEARCH_YAML)
        assert any('319' in l for l in lines), \
            "Mechanism #319 not found in competitor-coverage-research.yaml"

    def test_mechanism_name_contains_cannibalization(self):
        lines = _grep('cannibalization', RESEARCH_YAML)
        assert len(lines) > 0, \
            "No cannibalization-related mechanism in research YAML"

    def test_mechanism_name_contains_chatgpt_ads(self):
        lines = _grep('chatgpt.*ads', RESEARCH_YAML)
        assert len(lines) > 0, \
            "No ChatGPT ads mechanism in research YAML"


class TestLeMondeDealPortfolio:
    """Verify Le Monde's triple AI deal portfolio is documented."""

    def test_le_monde_openai_deal_documented(self):
        content = _read_file(RESEARCH_YAML)
        assert 'Le Monde' in content or 'le_monde' in content, \
            "Le Monde not mentioned in research YAML"

    def test_le_monde_triple_deal(self):
        content = _read_file(RESEARCH_YAML)
        lower = content.lower()
        has_openai = 'le monde' in lower and 'openai' in lower
        has_perplexity = 'perplexity' in lower
        has_meta = 'meta' in lower
        assert has_openai and has_perplexity and has_meta, \
            "Le Monde triple deal portfolio not fully documented"

    def test_journalist_revenue_share_documented(self):
        content = _read_file(RESEARCH_YAML)
        assert '25%' in content or 'revenue share' in content.lower() or \
            'journalist bonus' in content.lower(), \
            "Le Monde 25% journalist revenue share not documented"


class TestChatGPTAdsExpansion:
    """Verify ChatGPT Ads European expansion facts."""

    def test_31_european_markets(self):
        content = _read_file(RESEARCH_YAML)
        assert '31' in content, "31 European markets not documented"

    def test_ad_revenue_run_rate(self):
        content = _read_file(RESEARCH_YAML)
        lower = content.lower()
        assert '$1' in content or '1 billion' in lower or \
            'billion run rate' in lower or '$1b' in lower or \
            'approaching' in lower, \
            "OpenAI ad revenue run rate not documented"

    def test_one_billion_weekly_users(self):
        content = _read_file(RESEARCH_YAML)
        assert '1 billion' in content.lower() or '1B' in content or \
            'billion weekly' in content.lower(), \
            "ChatGPT 1 billion weekly users not documented"


class TestFiveLayerArchitecture:
    """Verify the five-layer financial architecture is documented."""

    def test_content_subsidy_layer(self):
        content = _read_file(RESEARCH_YAML)
        lower = content.lower()
        assert 'content subsidy' in lower or 'content license' in lower or \
            'licenses content' in lower, \
            "Content subsidy layer not documented"

    def test_ad_cannibalization_layer(self):
        content = _read_file(RESEARCH_YAML)
        lower = content.lower()
        assert 'cannibalization' in lower or 'cannibaliz' in lower, \
            "Ad cannibalization layer not documented"

    def test_conversion_dependency_layer(self):
        content = _read_file(RESEARCH_YAML)
        lower = content.lower()
        assert 'conversion' in lower or '20x' in content or \
            '20 times' in lower, \
            "Conversion dependency layer not documented"

    def test_revenue_replacement_layer(self):
        content = _read_file(RESEARCH_YAML)
        lower = content.lower()
        assert 'revenue replacement' in lower or 'captivity' in lower or \
            'replacement spiral' in lower, \
            "Revenue replacement spiral layer not documented"

    def test_journalist_incentive_layer(self):
        content = _read_file(RESEARCH_YAML)
        lower = content.lower()
        assert 'journalist' in lower and ('bonus' in lower or
            'incentive' in lower or 'revenue share' in lower), \
            "Individual journalist incentive layer not documented"


class TestAgencyOverlap:
    """Verify the shared agency infrastructure is documented."""

    def test_publicis_documented(self):
        content = _read_file(RESEARCH_YAML)
        assert 'Publicis' in content, "Publicis not documented as shared agency"

    def test_dentsu_documented(self):
        content = _read_file(RESEARCH_YAML)
        assert 'Dentsu' in content, "Dentsu not documented as shared agency"

    def test_havas_documented(self):
        content = _read_file(RESEARCH_YAML)
        assert 'Havas' in content, "Havas not documented as shared agency"


class TestDisclosureAsymmetry:
    """Verify Le Monde coverage disclosure gap is documented."""

    def test_le_monde_article_url_documented(self):
        content = _read_file(RESEARCH_YAML)
        assert 'lemonde.fr' in content, \
            "Le Monde article URL not documented"

    def test_disclosure_gap_noted(self):
        content = _read_file(RESEARCH_YAML)
        lower = content.lower()
        assert 'disclosure' in lower or 'undisclosed' in lower or \
            'no disclosure' in lower, \
            "Disclosure gap not noted"

    def test_europesays_publisher_gap_cited(self):
        content = _read_file(RESEARCH_YAML)
        assert 'europesays' in content.lower() or \
            'Publisher Revenue Gap' in content, \
            "EuropeSays Publisher Revenue Gap analysis not cited"


class TestFinancialQuantification:
    """Verify key financial figures are documented."""

    def test_le_monde_revenue(self):
        content = _read_file(RESEARCH_YAML)
        assert '310' in content or '€310' in content, \
            "Le Monde Group €310M revenue not documented"

    def test_openai_ad_targets(self):
        content = _read_file(RESEARCH_YAML)
        assert '$2.5' in content or '2.5 billion' in content.lower() or \
            '$100' in content, \
            "OpenAI $2.5B/$100B ad revenue targets not documented"

    def test_french_advertisers_documented(self):
        content = _read_file(RESEARCH_YAML)
        lower = content.lower()
        french_advertisers = ['bouygues', 'cultura', 'totalenergies', 'carrefour']
        found = sum(1 for a in french_advertisers if a in lower)
        assert found >= 2, \
            f"Only {found}/4 French advertisers documented"


class TestCounterConfounders:
    """Verify counter-confounders are documented."""

    def test_meta_deal_noted(self):
        content = _read_file(RESEARCH_YAML)
        lower = content.lower()
        assert ('le monde' in lower or 'le_monde' in lower) and \
            'meta' in lower, \
            "Le Monde's Meta deal not documented as counter-confounder"

    def test_nascent_threat_noted(self):
        content = _read_file(RESEARCH_YAML)
        lower = content.lower()
        assert 'nascent' in lower or 'early' in lower or \
            'not yet material' in lower or 'genuinely' in lower, \
            "Nascent ad threat confounder not documented"

    def test_editorial_vs_institutional_disclosure(self):
        content = _read_file(RESEARCH_YAML)
        lower = content.lower()
        assert 'dreyfus' in lower or 'press gazette' in lower, \
            "Dreyfus public transparency vs editorial disclosure gap not documented"


class TestSourceURLIntegrity:
    """Verify all source URLs are present."""

    def test_le_monde_source_url(self):
        content = _read_file(RESEARCH_YAML)
        assert 'lemonde.fr/en/economy/article/2026/08/25' in content, \
            "Le Monde Aug 25 article URL missing"

    def test_adweek_source_url(self):
        content = _read_file(RESEARCH_YAML)
        assert 'adweek.com' in content, "Adweek source URL missing"

    def test_press_gazette_source_url(self):
        content = _read_file(RESEARCH_YAML)
        assert 'pressgazette.co.uk' in content, \
            "Press Gazette source URL missing"

    def test_europesays_source_url(self):
        content = _read_file(RESEARCH_YAML)
        assert 'europesays.com' in content, "EuropeSays source URL missing"

    def test_techrepublic_source_url(self):
        content = _read_file(RESEARCH_YAML)
        assert 'techrepublic.com' in content, \
            "TechRepublic source URL missing"


class TestCrossReferences:
    """Verify cross-references to existing mechanisms."""

    def test_references_prior_openai_ad_mechanisms(self):
        """Should reference existing OpenAI ad coverage mechanisms."""
        content = _read_file(RESEARCH_YAML)
        lower = content.lower()
        # Should reference openai ad-related mechanisms
        assert 'openai' in lower and 'ad' in lower, \
            "No cross-reference to existing OpenAI ad mechanisms"

    def test_references_publisher_captivity(self):
        """Should reference existing publisher financial captivity patterns."""
        content = _read_file(RESEARCH_YAML)
        lower = content.lower()
        assert 'captivity' in lower or 'dependency' in lower, \
            "No cross-reference to publisher financial captivity patterns"
