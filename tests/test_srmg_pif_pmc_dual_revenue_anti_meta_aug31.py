"""
Mechanism #422 Type C: PIF SRMG PMC Dual Revenue Anti-Meta

Type C: Financial Incentive Mapping

DISCOVERY: PIF sold all Meta shares Q2 2025 (667,996 class A ~$380M+) while retaining $200M+ stake in PMC via SRMG chain PIF->SNB->NCB Capital->Al Ahli Capital Fund 13->SRMG->PMC->The Verge. SRMG Media Solutions (SMS) advertising partnership May 2025 creates SECOND financial relationship beyond equity: Saudi government/private sector advertising (tourism, government departments, investment sectors, mega projects - Vision 2030 priorities) routed through PMC 40+ brands (Variety, Rolling Stone, Billboard, Hollywood Reporter, WWD, 412M monthly users, 150M social followers, 6B video views, formats video/banners/audience layering, co-create custom content pending editorial approval). SRMG financial deterioration Jul 15 2026 (52-week low SAR 68.00 down 12% from SAR 77.00, range 68-199, 1-year -46.94%, market cap SAR 5.50B ~$1.47B down from $1.65B, EV SAR 6.06B, revenue TTM SAR 2.79B -9.92% YoY, FY2025 SAR 2.67B -18.09% YoY, net income TTM -SAR 364.14M, EPS -SAR 4.55, ROE -18.66%, ROA -3.35%, ROIC -9.81%, debt/EBITDA 8.90, interest coverage -2.31, employees 700 down from 2000 65% reduction, Q1 2026 partial recovery net profit SAR 33.07M +6.88% YoY vs Q1 2025 SAR 30.94M revenue SAR 769.63M +18.26% YoY vs SAR 650.76M EPS SAR 0.41 up from 0.39 sequential Q4 2025 loss SAR 357.04M FY2025 full-year net loss SAR 366.28M vs profit SAR 201.69M FY2024) creates distressed-investor pressure to monetize equity via commercial partnership.

PIF Q2 2025 13F: sold all Meta (667,996), Shopify 1.25M, PayPal 1.76M, Alibaba 1.61M ADS, Nu Holdings 6.83M, FedEx 498,164, total US equity $23.8B down from $25.5B end Q1, holdings $43.6B March to $36.5B June, AUM $1.15T, shifted to semiconductors Arm +400M shares ASML Analog Devices healthcare UnitedHealth Eli Lilly Merck Apple new position Lucid massive increase. Significance: PIF aligned AGAINST Meta (divested) and WITH Apple/Arm/chip ecosystem, through SRMG PIF has $200M+ stake in PMC (The Verge parent), The Verge ultimate beneficial ownership includes sovereign investor that actively sold Meta stock while retaining media investment creating structural financial alignment against most-covered company.

NOVELTY vs existing SRMG distress coverage (6a6abad Jul 15 2026 was distress alone): this mechanism adds dual revenue dependency (equity + advertising) plus PIF divestment as structural anti-Meta signal plus governance (Prince Badr, Ahmed Al-Khatib, Jomana Al-Rashid) plus Q2 2026 recovery context. No prior Type C covered advertising partnership May 2025 as primary mechanism.

CONFOUNDERS: editorial independence STRONG, market dominance STRONG, access journalism MODERATE, beat specialization MODERATE, Vision 2030 alignment WEAK, distressed pressure easing WEAK (Q2 profit +77.7% YoY).

Source URLs:
- Reuters PIF sold stakes https://www.reuters.com/world/middle-east/saudi-wealth-fund-sold-its-stakes-meta-shopify-paypal-q2-2025-08-14/
- AInvest https://www.ainvest.com/news/saudi-wealth-fund-sells-tech-holdings-exits-meta-alibaba-2508-0/
- BroadcastProMe SMS-PMC https://www.broadcastprome.com/news/srmg-media-solutions-and-penske-media-to-elevate-mena-advertisers-on-global-stage/
- SAHM Capital https://www.sahmcapital.com/news/content/pressr-srmg-media-solutions-partners-with-penske-media-corporation-to-expand-global-reach-for-mena-brands-and-advertisers-2025-04-17
- Gulf Business $200M https://gulfbusiness.com/en/2018/media/saudis-pif-acquires-stake-us-media-business-200m/
- TheWrap https://www.thewrap.com/jay-penske-saudi-stake-media-company-200-million-khashoggi-murder/
- Saudi Exchange https://www.saudiexchange.sa/wps/portal/saudiexchange/newsandreports/issuer-news/issuer-announcements/issuer-announcements-details/?anId=87205&anCat=1&cs=4210&locale=en
"""

import os
import yaml
import pytest

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')

def load_verge():
    with open(os.path.join(PROFILES_DIR, 'the-verge.yaml'), 'r') as f:
        return yaml.safe_load(f)

def load_competitor_entities():
    with open(os.path.join(PROFILES_DIR, 'competitor-entities.yaml'), 'r') as f:
        return yaml.safe_load(f)

def verge_text():
    with open(os.path.join(PROFILES_DIR, 'the-verge.yaml'), 'r') as f:
        return f.read()

class TestPIFMetaDivestment:
    def test_verge_yaml_contains_pif_chain(self):
        txt = verge_text()
        assert 'PIF' in txt and 'SNB' in txt and 'NCB Capital' in txt and 'Al Ahli' in txt and 'SRMG' in txt and 'PMC' in txt

    def test_verge_yaml_pif_sold_meta_667996(self):
        txt = verge_text()
        assert '667,996' in txt or '667996' in txt
        assert 'sold all Meta' in txt or 'sold all Meta shares' in txt or 'sold all Meta shares' in txt.lower() or 'PIF sold all Meta' in txt

    def test_verge_yaml_pif_total_exposure_23_8(self):
        txt = verge_text()
        assert ('23.8' in txt)  # 25.5 verified via competitor-entities.yaml

    def test_reuters_source_url_present(self):
        txt = verge_text()
        # profile may not have Reuters URL directly but competitor-entities should; check both
        entities = load_competitor_entities()
        e = entities['entities']['srmg_pif_pmc_dual_revenue_anti_meta_mechanism_422']
        urls = []
        urls.extend(e.get('pif_tech_portfolio_dynamics_q2_2025_13f', {}).get('source_urls', []))
        urls.extend(e.get('investment_2018', {}).get('source_urls', []))
        urls.extend(e.get('advertising_partnership_may_2025', {}).get('source_urls', []))
        assert any('reuters.com/world/middle-east/saudi-wealth-fund-sold-its-stakes-meta' in u for u in urls)

class TestSRMGAdvertisingPartnership:
    def test_verge_yaml_contains_srmg_media_solutions(self):
        txt = verge_text()
        assert 'SRMG Media Solutions' in txt or 'SMS' in txt

    def test_verge_yaml_advertising_40_brands_412m(self):
        txt = verge_text()
        assert '40' in txt and '412' in txt

    def test_advertising_partnership_source_url(self):
        entities = load_competitor_entities()
        e = entities['entities']['srmg_pif_pmc_dual_revenue_anti_meta_mechanism_422']
        urls = e['advertising_partnership_may_2025']['source_urls']
        assert any('broadcastprome.com' in u for u in urls)
        assert any('sahmcapital.com' in u for u in urls)

    def test_dual_revenue_dependency_documented(self):
        entities = load_competitor_entities()
        e = entities['entities']['srmg_pif_pmc_dual_revenue_anti_meta_mechanism_422']
        assert 'dual_revenue_dependency' in e['advertising_partnership_may_2025']
        dep = e['advertising_partnership_may_2025']['dual_revenue_dependency']
        assert 'a_equity' in dep and 'b_advertising' in dep

class TestSRMGFinancialDeterioration:
    def test_verge_yaml_52_week_low_68(self):
        txt = verge_text()
        assert '68.00' in txt or 'SAR 68' in txt

    def test_verge_yaml_workforce_700_65_pct(self):
        txt = verge_text()
        assert '700' in txt and '65%' in txt or '65' in txt

    def test_competitor_entities_financials(self):
        entities = load_competitor_entities()
        e = entities['entities']['srmg_pif_pmc_dual_revenue_anti_meta_mechanism_422']
        fin = e['financial_deterioration_jul15_2026']
        assert fin['share_price_SAR'] == 68.00
        assert fin['workforce_reduction_pct'] == 65
        assert fin['interest_coverage'] == -2.31
        assert fin['debt_to_ebitda'] == 8.90
        assert fin['q1_2026_partial_recovery']['net_profit_SAR_M'] == 33.07
        assert fin['q1_2026_partial_recovery']['revenue_SAR_M'] == 769.63

    def test_q2_2026_recovery_still_exists(self):
        entities = load_competitor_entities()
        # original srmg_q2_2026_results may exist elsewhere
        txt = open(os.path.join(PROFILES_DIR, 'competitor-entities.yaml')).read()
        assert '653.2' in txt or '71.2' in txt

class TestGovernance:
    def test_prince_badr_and_tourism_minister(self):
        entities = load_competitor_entities()
        e = entities['entities']['srmg_pif_pmc_dual_revenue_anti_meta_mechanism_422']
        gov = e['governance']
        assert 'prince_badr_bin_abdullah' in gov or 'prince_badr' in gov or 'Prince Badr' in str(gov.values()) or 'Prince Badr' in str(gov)
        assert 'ahmed_bin_aqeel_al_khatib' in gov or 'ahmed_bin_aqeel' in str(list(gov.keys()))

    def test_ceo_jomana_first_female(self):
        entities = load_competitor_entities()
        e = entities['entities']['srmg_pif_pmc_dual_revenue_anti_meta_mechanism_422']
        assert 'jomana' in str(e['governance']).lower()
        assert 'first female' in str(e['governance']).lower() or 'First female' in str(e['governance'])

class TestInvestment2018:
    def test_200m_plus_25m_jv(self):
        entities = load_competitor_entities()
        e = entities['entities']['srmg_pif_pmc_dual_revenue_anti_meta_mechanism_422']
        inv = e['investment_2018']
        assert '$200M' in inv['amount'] or '200M' in inv['amount']
        assert '700M' in inv['valuation']

    def test_source_urls_gulf_business_thewrap(self):
        entities = load_competitor_entities()
        e = entities['entities']['srmg_pif_pmc_dual_revenue_anti_meta_mechanism_422']
        urls = e['investment_2018']['source_urls']
        assert any('gulfbusiness.com' in u for u in urls)
        assert any('thewrap.com' in u for u in urls)

class TestConfoundersAndMethodology:
    def test_confounders_documented(self):
        entities = load_competitor_entities()
        e = entities['entities']['srmg_pif_pmc_dual_revenue_anti_meta_mechanism_422']
        assert len(e['confounders']) >= 5
        levels = [c['level'] for c in e['confounders']]
        assert 'STRONG' in levels and 'MODERATE' in levels and 'WEAK' in levels

    def test_methodology_not_calculated(self):
        entities = load_competitor_entities()
        e = entities['entities']['srmg_pif_pmc_dual_revenue_anti_meta_mechanism_422']
        assert (e.get('p_value') == 'not_calculated' or e.get('methodology', {}).get('p_value') == 'not_calculated')
        assert (e.get('cohens_d') == 'not_calculated' or e.get('methodology', {}).get('cohens_d') == 'not_calculated')
        assert (e.get('significant') is False or e.get('methodology', {}).get('significant') is False)
        assert (e.get('significant_empirical') is False or e.get('methodology', {}).get('significant_empirical') is False)

    def test_no_em_dash_in_detail(self):
        txt = open(os.path.join(PROFILES_DIR, 'competitor-entities.yaml')).read()
        # our mechanism should not contain em dash character
        e_section = txt.split('srmg_pif_pmc_dual_revenue_anti_meta_mechanism_422')[1][:5000]
        assert '—' not in e_section

