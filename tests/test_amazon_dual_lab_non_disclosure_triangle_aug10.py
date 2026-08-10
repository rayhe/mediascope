"""
Type C: Amazon-Bezos $63B Dual-Lab Non-Disclosure Triangle — Mechanism #25

Amazon is the single largest investor in BOTH OpenAI ($50B, Feb 2026)
AND Anthropic ($13B+, cumulative through Apr 2026), totaling $63B across
the two AI labs that have both filed confidential S-1s for IPO. Jeff
Bezos personally owns the Washington Post, which has its own "strategic
content-sharing" agreement with OpenAI (content licensing deal). WaPo
editorial pages systematically omit disclosure of Bezos's AI financial
interests (documented by Washingtonian, Jun 23 2026, Paul Farhi —
former WaPo reporter, 35 years).

PROFILE DATA CORRECTION: competitor-entities.yaml previously stated
"Amazon invests in Anthropic only" (under Microsoft's
dual_ai_lab_investment_paradox). This was factually wrong after Amazon's
$50B OpenAI investment in Feb 2026. Amazon is now the LARGEST dual-lab
investor ($63B total), surpassing Microsoft ($13B OpenAI + $5B Anthropic
= $18B) by 3.5x.

KEY FINANCIAL CHAINS:
1. Amazon → $50B OpenAI investment (Feb 2026, Series F)
2. Amazon → $13B+ Anthropic investment ($8B initial + $5B Apr 2026)
3. OpenAI → $138B multiyear investment into AWS infrastructure
4. WaPo ← OpenAI content licensing deal ("strategic content-sharing")
5. Jeff Bezos owns WaPo (purchased 2013, $250M)
6. Anthropic → $53.4B paper gain for Amazon Q2 2026
7. Both OpenAI (Jun 8) and Anthropic (Jun 1) filed confidential S-1s

NON-DISCLOSURE EVIDENCE (Washingtonian, Jun 23 2026):
- Zero WaPo editorial/opinion columns opposing data center construction
  over 6 months, despite Bezos/Amazon financial interest
- WaPo-OpenAI content deal not disclosed in columns specifically about
  ChatGPT
- Amazon-OpenAI $138B AWS infrastructure deal never referenced in
  supportive commentary
- "Simple mention" of Bezos ownership ("Amazon founder Jeff Bezos owns
  the Post") only appears intermittently, near article bottoms
- SPJ ethics committee chair Dan Axelrod quoted: "Media credibility
  hinges on the audience's assumption that journalists are, first and
  foremost, serving the public"
- WaPo news side (as distinct from opinion) is "rigorous and consistent"
  in disclosing — the gap is editorial/opinion

CONTRAST WITH META:
Meta has ZERO investment in any AI lab's IPO. Meta has ZERO newspaper
ownership. Meta's only publisher financial relationship is voluntary
content licensing ($50M/yr News Corp + 12 others). Yet Meta receives
the most sustained adversarial coverage from publications whose owner
(Bezos/Amazon) has $63B invested in Meta's competitors.

DUAL-IPO EXPOSURE (Jun 2026):
- OpenAI S-1: Filed Jun 8, 2026 (confidential). Underwriters: GS, MS,
  JPMorgan. Target valuation: ~$1T. Amazon: $50B invested.
- Anthropic S-1: Filed Jun 1, 2026 (confidential). Underwriters: GS, MS.
  Target valuation: ~$965B+. Amazon: $13B invested.
- If both IPOs succeed at target valuations, Amazon's $63B stake could
  appreciate to $100B+.
- If IPOs fail or are delayed, Amazon's unrealized gains ($53.4B Q2 2026
  from Anthropic alone) are at risk.

LEGITIMATE FACTORS:
- WaPo news side is editorially independent and does disclose Bezos
  ownership — the non-disclosure is concentrated in opinion/editorial
- Bezos has maintained a public stance of editorial independence since
  2013 purchase
- Amazon's investment decisions are made by corporate leadership, not
  by Bezos personally (he is executive chairman, not CEO)
- WaPo's adversarial Meta coverage predates the OpenAI investment by
  many years
- Amazon's OpenAI investment has a commercial rationale (AWS revenue,
  Trainium compute) separate from any coverage influence
- Large institutional investors routinely invest in competing companies
  without coverage implications

Sources:
- Washingtonian (Jun 23, 2026): https://washingtonian.com/2026/06/23/the-washington-post-loves-data-centers-a-lot-more-than-disclosing-jeff-bezos-financial-interest-in-promoting-them/
- Engadget (Feb 2026): https://www.engadget.com/ai/openai-secures-another-110-billion-in-funding-from-amazon-nvidia-and-softbank-171006356.html
- The Times (Mar 2026): https://www.thetimes.com/business/companies-markets/article/openai-chatgpt-valuation-record-funding-round-9g5gfwt2b
- CoinDesk (Apr 1, 2026): https://www.coindesk.com/tech/2026/04/01/openai-raises-a-record-usd122-billion-at-as-revenue-crosses-usd2-billion-per-month
- eWeek (Jun 2026): https://www.eweek.com/news/openai-confidential-ipo-filing-sec/
- PYMNTS (Jun 2026): https://www.pymnts.com/artificial-intelligence-2/2026/openai-confidential-ipo-filing-joins-race-for-largest-public-listing-ever/
- TechTimes (Jun 2026): https://www.techtimes.com/articles/319145/20260626/openai-ipo-delay-sends-softbank-down-38-billion-altman-refuses-any-cut-1-trillion-target.htm
- MarketWatch Q2 earnings: https://www.marketwatch.com/livecoverage/amazon-earnings-stock-results-guidance-q2/card/amazon-posts-a-big-gain-on-its-anthropic-investment-H0PZCbIeYiLLhY0mUTS3

Created: 2026-08-10 08:00 PT
"""

import yaml
import os
import pytest

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')
ENTITIES_PROFILE = os.path.join(PROFILES_DIR, 'competitor-entities.yaml')


def load_yaml(path):
    with open(path) as f:
        return yaml.safe_load(f)


@pytest.fixture(scope='module')
def entities():
    return load_yaml(ENTITIES_PROFILE)


@pytest.fixture(scope='module')
def amazon(entities):
    return entities['entities']['amazon']


@pytest.fixture(scope='module')
def microsoft(entities):
    return entities['entities']['microsoft']


# ===================================================================
# TEST CLASS 1: Amazon OpenAI Investment Data Correction
# ===================================================================
class TestAmazonOpenAIInvestment:
    """Validates the OpenAI $50B investment is documented in Amazon entity."""

    def test_openai_investment_layer_exists(self, amazon):
        layers = amazon['sextuple_publisher_leverage']['layers']
        layer_names = {l['name'] for l in layers}
        assert 'openai_investment' in layer_names

    def test_openai_investment_amount(self, amazon):
        layers = amazon['sextuple_publisher_leverage']['layers']
        openai_layer = next(l for l in layers if l['name'] == 'openai_investment')
        assert openai_layer['openai_invested_b'] == 50

    def test_openai_investment_round(self, amazon):
        layers = amazon['sextuple_publisher_leverage']['layers']
        openai_layer = next(l for l in layers if l['name'] == 'openai_investment')
        assert '122' in openai_layer['detail'] or 'Series F' in openai_layer['detail']

    def test_dual_lab_total_exceeds_60b(self, amazon):
        layers = amazon['sextuple_publisher_leverage']['layers']
        anthropic_layer = next(l for l in layers if l['name'] == 'anthropic_investment')
        openai_layer = next(l for l in layers if l['name'] == 'openai_investment')
        total = anthropic_layer['anthropic_total_invested_b'] + openai_layer['openai_invested_b']
        assert total >= 63

    def test_layer_count_is_seven(self, amazon):
        layers = amazon['sextuple_publisher_leverage']['layers']
        assert len(layers) == 7


# ===================================================================
# TEST CLASS 2: Microsoft Dual-Investor Claim Correction
# ===================================================================
class TestMicrosoftDualInvestorCorrected:
    """Validates that Microsoft's profile no longer claims it is the ONLY
    company investing in both OpenAI and Anthropic."""

    def test_dual_paradox_acknowledges_amazon(self, microsoft):
        paradox = microsoft['septuple_publisher_leverage']['dual_ai_lab_investment_paradox']
        # Must mention Amazon's dual investment
        assert 'Amazon' in paradox
        # Opening sentence must not claim Microsoft is the only dual investor
        first_sentence = paradox.split('.')[0]
        assert 'ONLY' not in first_sentence

    def test_dual_paradox_notes_amazon_larger(self, microsoft):
        paradox = microsoft['septuple_publisher_leverage']['dual_ai_lab_investment_paradox']
        # Must acknowledge Amazon's larger scale
        assert '50' in paradox or 'larger' in paradox.lower() or 'largest' in paradox.lower()


# ===================================================================
# TEST CLASS 3: WaPo-OpenAI Content Licensing Deal
# ===================================================================
class TestWaPoOpenAIContentDeal:
    """Validates the WaPo-OpenAI strategic content-sharing agreement
    is documented in the Amazon entity profile."""

    def test_wapo_openai_deal_documented(self, amazon):
        layers = amazon['sextuple_publisher_leverage']['layers']
        wapo_layer = next(l for l in layers if l['name'] == 'bezos_wapo_ownership')
        detail = wapo_layer['detail']
        assert 'OpenAI' in detail
        assert 'content' in detail.lower()

    def test_wapo_openai_deal_type(self, amazon):
        layers = amazon['sextuple_publisher_leverage']['layers']
        wapo_layer = next(l for l in layers if l['name'] == 'bezos_wapo_ownership')
        # Must reference strategic content-sharing or licensing
        detail = wapo_layer['detail']
        assert 'strategic' in detail.lower() or 'licensing' in detail.lower() or 'content-sharing' in detail.lower()


# ===================================================================
# TEST CLASS 4: OpenAI AWS Infrastructure Deal
# ===================================================================
class TestOpenAIAWSInfrastructureDeal:
    """Validates the OpenAI $138B AWS infrastructure deal is documented."""

    def test_aws_openai_deal_exists(self, amazon):
        layers = amazon['sextuple_publisher_leverage']['layers']
        aws_layer = next(l for l in layers if l['name'] == 'aws_cloud_hosting')
        detail = aws_layer['detail']
        assert 'OpenAI' in detail

    def test_aws_openai_deal_scale(self, amazon):
        layers = amazon['sextuple_publisher_leverage']['layers']
        aws_layer = next(l for l in layers if l['name'] == 'aws_cloud_hosting')
        detail = aws_layer['detail']
        # Must mention the $138B or 'exclusive third-party cloud' deal
        assert '138' in detail or 'exclusive' in detail.lower() or 'Frontier' in detail


# ===================================================================
# TEST CLASS 5: Non-Disclosure Evidence
# ===================================================================
class TestNonDisclosureEvidence:
    """Validates the Washingtonian-sourced non-disclosure evidence
    is documented in Mechanism #25."""

    def test_mechanism_25_exists(self, amazon):
        assert 'mechanism_25_dual_lab_non_disclosure_triangle' in amazon

    def test_mechanism_25_has_id(self, amazon):
        m = amazon['mechanism_25_dual_lab_non_disclosure_triangle']
        assert m['mechanism_id'] == 25

    def test_washingtonian_source(self, amazon):
        m = amazon['mechanism_25_dual_lab_non_disclosure_triangle']
        sources = str(m.get('source_urls', ''))
        assert 'washingtonian' in sources.lower()

    def test_non_disclosure_patterns_documented(self, amazon):
        m = amazon['mechanism_25_dual_lab_non_disclosure_triangle']
        nd = m['non_disclosure_patterns']
        assert len(nd) >= 3

    def test_editorial_vs_news_distinction(self, amazon):
        m = amazon['mechanism_25_dual_lab_non_disclosure_triangle']
        finding = str(m)
        # Must note that WaPo news side IS rigorous — gap is editorial
        assert 'news' in finding.lower() and 'editorial' in finding.lower() or \
               'opinion' in finding.lower()


# ===================================================================
# TEST CLASS 6: Dual-IPO Financial Exposure
# ===================================================================
class TestDualIPOExposure:
    """Validates the dual-IPO S-1 filing data is documented."""

    def test_openai_s1_filing_date(self, amazon):
        m = amazon['mechanism_25_dual_lab_non_disclosure_triangle']
        ipo = m['dual_ipo_exposure']
        assert ipo['openai_s1_filed'] == '2026-06-08'

    def test_anthropic_s1_filing_date(self, amazon):
        m = amazon['mechanism_25_dual_lab_non_disclosure_triangle']
        ipo = m['dual_ipo_exposure']
        assert ipo['anthropic_s1_filed'] == '2026-06-01'

    def test_combined_investment_total(self, amazon):
        m = amazon['mechanism_25_dual_lab_non_disclosure_triangle']
        ipo = m['dual_ipo_exposure']
        assert ipo['amazon_combined_investment_b'] >= 63

    def test_meta_ipo_stake_zero(self, amazon):
        m = amazon['mechanism_25_dual_lab_non_disclosure_triangle']
        ipo = m['dual_ipo_exposure']
        assert ipo['meta_ipo_financial_stake_b'] == 0


# ===================================================================
# TEST CLASS 7: Legitimate Factors
# ===================================================================
class TestLegitimatFactors:
    """Every mechanism must document non-trivial confounders."""

    def test_legitimate_factors_exist(self, amazon):
        m = amazon['mechanism_25_dual_lab_non_disclosure_triangle']
        assert 'legitimate_factors' in m
        assert len(m['legitimate_factors']) >= 4

    def test_editorial_independence_acknowledged(self, amazon):
        m = amazon['mechanism_25_dual_lab_non_disclosure_triangle']
        factors = str(m['legitimate_factors'])
        assert 'independence' in factors.lower() or 'news side' in factors.lower()

    def test_commercial_rationale_acknowledged(self, amazon):
        m = amazon['mechanism_25_dual_lab_non_disclosure_triangle']
        factors = str(m['legitimate_factors'])
        assert 'AWS' in factors or 'commercial' in factors.lower() or 'Trainium' in factors


# ===================================================================
# TEST CLASS 8: Meta Contrast
# ===================================================================
class TestMetaContrastDualLab:
    """Meta's zero-investment position in both IPOs."""

    def test_meta_zero_ai_lab_investment(self, amazon):
        m = amazon['mechanism_25_dual_lab_non_disclosure_triangle']
        contrast = m['meta_contrast']
        assert 'ZERO' in contrast or 'zero' in contrast or '0' in contrast

    def test_meta_no_newspaper_ownership(self, amazon):
        m = amazon['mechanism_25_dual_lab_non_disclosure_triangle']
        contrast = m['meta_contrast']
        assert 'newspaper' in contrast.lower() or 'ownership' in contrast.lower()

    def test_asymmetry_temporal_noted(self, amazon):
        m = amazon['mechanism_25_dual_lab_non_disclosure_triangle']
        contrast = m['meta_contrast']
        # Meta IPO was 2012, OpenAI/Anthropic IPOs are 2026+
        assert '2012' in contrast or 'past' in contrast.lower() or 'temporal' in contrast.lower()
