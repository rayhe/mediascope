"""
Mechanism #266: Anthropic Pre-IPO Roadshow Publisher Narrative Monopoly

Type C: Financial Incentive Mapping
Date: 2026-08-24 03:00 PT
Iteration: #270

CORE FINDING: During Anthropic's SEC quiet period (June 1 confidential S-1
through public filing), the company cannot publicly discuss specific financials,
and its lead underwriters (Goldman Sachs, Morgan Stanley, JPMorgan) cannot
publish equity research. This creates a structural gap where tech/financial
PUBLICATIONS become the SOLE public narrative shapers for a $2T IPO valuation
story — and those publications have compound financial incentives to frame the
narrative positively.

KEY TIMELINE:
- Jun 1, 2026: Anthropic files confidential S-1 (quiet period begins)
- Jun 18, 2026: WSJ reports GS/MS forming "distinct teams" for OpenAI/Anthropic
- Mid-Aug 2026: Pre-IPO investor meetings begin (CFO Krishna Rao leading)
- Aug 13, 2026: FT reports 6 investors expect $2T (narrative is investor-leak-driven)
- Aug 18, 2026: Reuters reports $10B+ credit facility, banks jockeying for IPO roles
- Sep/Oct 2026: Targeted public listing

DURING THIS WINDOW:
1. Anthropic CFO meetings focus on "AI models, not financials" (CryptoBriefing Aug 13)
2. GS/MS equity research divisions CANNOT publish research (quiet period restriction)
3. SpaceX IPO bankers EXCLUDED from OpenAI/Anthropic paperwork (WSJ Jun 18)
4. ONLY publications + investor leaks shape the $2T valuation narrative

PUBLICATIONS SHAPING THE NARRATIVE + THEIR FINANCIAL INTERESTS:
- Financial Times: OpenAI content deal + Google Showcase deal → reporting $2T valuation
  based on 6 investor leaks validates OpenAI's parallel IPO valuation
- WSJ/News Corp: $250M/5yr OpenAI content deal → reporting dual-IPO bank dynamics
  positively serves News Corp's AI deal partner's ecosystem
- Bloomberg: Microsoft content deal → Microsoft owns 49% of OpenAI → Anthropic
  IPO success validates sector-wide AI valuations
- CNBC: Comcast parent has NBC Universal Google ad dependency → covering Anthropic
  positively serves Google (14% Anthropic investor)

FINANCIAL CHAIN — HOW POSITIVE ANTHROPIC IPO COVERAGE SERVES PUBLICATIONS:
1. Higher Anthropic IPO valuation → larger Google paper gains ($280B at $2T)
2. Google is #1 or #2 advertiser for most publications → Google financial health
   matters for publisher ad revenue
3. Higher Anthropic IPO → validates OpenAI IPO valuation (same sector, same banks)
4. OpenAI IPO success → validates publisher content deals with OpenAI
5. Anthropic zero-publisher-deal model SHOULD concern publishers (it proves deals
   are unnecessary), but short-term advertiser gains override long-term deal leverage

CREDIT FACILITY COMPOUND (Reuters Aug 18, 2026):
- Pre-IPO credit facility exceeding $10B target
- Banks committing ~$1.25B each in REVOLVING CREDIT — hoping to secure IPO co-manager slots
- This expands the number of financial institutions with skin in Anthropic's IPO success
- "Banks jockeying for larger commitments hoping to secure IPO roles"
- Source: https://www.reuters.com/legal/transactional/anthropics-pre-ipo-credit-facility-set-exceed-10-billion-bloomberg-news-reports-2026-08-18/

CONTRAST WITH META:
- Meta is publicly traded — executives discuss financials freely on earnings calls
- Meta coverage is NOT monopolized by publications during any quiet period
- Analysts at GS/MS freely publish Meta research (no quiet period applies)
- Meta has NO IPO bank fee incentive → no bank-level protection from criticism
- Meta has NO credit facility creating bank constituency → no bank-level advocacy

CONTRAST WITH OPENAI:
- OpenAI also filed confidential S-1 (Jun 8) and is in quiet period
- BUT OpenAI pushed IPO to 2027 → narrative urgency is lower
- Anthropic is the ACTIVE IPO candidate → publication narrative shaping is more
  immediately consequential
- Same GS/MS teams cannot work on both → further concentrating the publications'
  narrative monopoly

LEGITIMATE FACTORS:
- SEC quiet period restrictions are legal requirements, not publisher strategy
- CFO meetings with select investors are standard IPO process
- FT/WSJ/Bloomberg are the publications that SHOULD cover IPOs (it's their beat)
- Investor leaks are the primary source for pre-IPO valuation estimates — this
  is normal financial journalism practice
- Publications covering Anthropic favorably may reflect genuine assessment of
  strong fundamentals ($65B ARR, 14x YoY revenue growth)
- Google and Amazon's Anthropic investments are public knowledge — no hidden
  conflict to disclose

SOURCES:
- CryptoBriefing (Aug 13, 2026): https://cryptobriefing.com/anthropic-ipo-meetings-ai-models-not-financials/
- TradingView/dpa-AFX (Aug 13, 2026): https://www.tradingview.com/news/dpa_afx:0a1c26cd40287:0-anthropic-holds-early-investor-meetings-ahead-of-potential-ipo/
- Investopedia (Aug 14, 2026): https://www.investopedia.com/anthropic-could-go-public-soon-some-investors-are-eyeing-a-valuation-that-would-top-spacex-spcx-12058975
- WSJ (Jun 18, 2026): https://www.wsj.com/finance/banking/the-ipo-onslaught-is-forcing-bankers-to-pick-teams-50fab052
- Reuters (Aug 18, 2026): https://www.reuters.com/legal/transactional/anthropics-pre-ipo-credit-facility-set-exceed-10-billion-bloomberg-news-reports-2026-08-18/
- PYMNTS (Jul 15, 2026): https://www.pymnts.com/news/investment-tracker/ipo/2026/anthropic-begin-investor-meetings-potential-october-ipo/
- PYMNTS (Jun 3, 2026): https://www.pymnts.com/news/investment-tracker/ipo/2026/morgan-stanley-and-goldman-sachs-land-anthropic-ipo/
- TheStreet (Jul 15, 2026): https://www.thestreet.com/technology/anthropic-ipo-prospectus-registration-filing-changes-ai-investing
- eFincancialCareers (Jun 18, 2026): https://www.efinancialcareers.com/news/goldman-sachs-morgan-stanley-openai-anthropic
- GS/MS fee data from SpaceX IPO: WSJ Jun 18 ("$100 million apiece for SpaceX")

CROSS-REFERENCES: #21, #25, #257
"""
import unittest
import yaml
import os


PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


def load_competitor_entities():
    path = os.path.join(PROFILES_DIR, 'competitor-entities.yaml')
    with open(path) as f:
        return yaml.safe_load(f)


def load_competitor_research():
    path = os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml')
    with open(path) as f:
        return yaml.safe_load(f)


def find_mechanism(mechanism_id):
    """Find a mechanism by ID across all sections of competitor-coverage-research.yaml."""
    data = load_competitor_research()
    # Mechanisms are stored as named entries under 'publications' (or other top-level keys)
    # Each entry can have a 'mechanism_id' field
    for section_key, section_val in data.items():
        if isinstance(section_val, dict):
            for entry_key, entry_val in section_val.items():
                if isinstance(entry_val, dict) and entry_val.get('mechanism_id') == mechanism_id:
                    return entry_val
    return None


def load_publication_profile(name):
    path = os.path.join(PROFILES_DIR, f'{name}.yaml')
    with open(path) as f:
        return yaml.safe_load(f)


# =============================================================================
# Class 1: Quiet Period Timeline Verification
# =============================================================================
class TestQuietPeriodTimeline(unittest.TestCase):
    """Verify the quiet period timeline is documented in competitor-entities."""

    def setUp(self):
        entities = load_competitor_entities()
        self.anthropic = entities['entities']['anthropic']
        self.ipo = self.anthropic['ipo_filing']

    def test_s1_filing_date_is_june_1(self):
        """Confidential S-1 filed June 1, 2026 — quiet period start."""
        self.assertEqual(self.ipo['confidential_s1_date'], '2026-06-01')

    def test_target_listing_is_october_2026(self):
        """IPO target is as early as October 2026."""
        self.assertIn('October', self.ipo['target_listing'])

    def test_ipo_banks_include_gs_ms_jpm(self):
        """Goldman Sachs, Morgan Stanley, JPMorgan are all lead underwriters."""
        banks = self.ipo['ipo_banks_reported']
        self.assertIn('Goldman Sachs', banks)
        self.assertIn('Morgan Stanley', banks)
        self.assertIn('JPMorgan Chase', banks)

    def test_pre_ipo_credit_facility_exceeds_10b(self):
        """Pre-IPO credit facility exceeds $10B target (Reuters Aug 18)."""
        self.assertIn('pre_ipo_credit_facility_b', self.ipo)
        self.assertGreaterEqual(self.ipo['pre_ipo_credit_facility_b'], 10)

    def test_revenue_run_rate_at_filing(self):
        """Revenue run rate was $47B at filing time (May 2026)."""
        self.assertEqual(self.ipo['revenue_run_rate_at_filing_b'], 47)


# =============================================================================
# Class 2: Pre-IPO Roadshow Meeting Structure
# =============================================================================
class TestPreIPORoadshowMeetings(unittest.TestCase):
    """Verify pre-IPO meeting structure is documented."""

    def setUp(self):
        entities = load_competitor_entities()
        self.anthropic = entities['entities']['anthropic']
        self.ipo = self.anthropic['ipo_filing']

    def test_pre_ipo_meetings_documented(self):
        """Pre-IPO investor meetings are documented."""
        self.assertIn('pre_ipo_investor_meetings', self.ipo)

    def test_meetings_led_by_cfo(self):
        """CFO Krishna Rao is leading the meetings."""
        meetings = self.ipo['pre_ipo_investor_meetings']
        self.assertIn('Krishna Rao', meetings.get('led_by', ''))

    def test_meetings_focus_on_models_not_financials(self):
        """Meetings focus on AI models, not financials — creating narrative gap."""
        meetings = self.ipo['pre_ipo_investor_meetings']
        focus = meetings.get('focus', '')
        self.assertIn('model', focus.lower())

    def test_meetings_started_mid_august(self):
        """Meetings began mid-August 2026."""
        meetings = self.ipo['pre_ipo_investor_meetings']
        self.assertIn('mid-August', meetings.get('start_date', ''))

    def test_valuation_not_discussed_in_meetings(self):
        """Company has NOT discussed specific valuation in meetings."""
        meetings = self.ipo['pre_ipo_investor_meetings']
        self.assertTrue(meetings.get('valuation_discussed') is False
                        or 'not discussed' in meetings.get('valuation_note', '').lower())


# =============================================================================
# Class 3: Publisher Narrative Monopoly Structure
# =============================================================================
class TestPublisherNarrativeMonopoly(unittest.TestCase):
    """Verify the mechanism documenting publisher narrative monopoly during quiet period."""

    def setUp(self):
        self.mechanism = find_mechanism(266)

    def test_mechanism_266_exists(self):
        """Mechanism #266 exists in competitor-coverage-research.yaml."""
        self.assertIsNotNone(self.mechanism, "Mechanism #266 not found")

    def test_mechanism_type_is_financial_incentive_mapping(self):
        """Mechanism is categorized as financial incentive mapping."""
        self.assertIn('financial', self.mechanism.get('type', '').lower())

    def test_mechanism_documents_quiet_period(self):
        """Mechanism references SEC quiet period."""
        finding = self.mechanism.get('finding', '')
        self.assertIn('quiet period', finding.lower())

    def test_mechanism_documents_narrative_monopoly(self):
        """Mechanism documents publications as sole narrative shapers."""
        finding = self.mechanism.get('finding', '')
        self.assertTrue(
            'narrative' in finding.lower() and
            ('monopoly' in finding.lower() or 'sole' in finding.lower() or 'only' in finding.lower())
        )

    def test_mechanism_has_source_urls(self):
        """Mechanism has source URLs for verification."""
        sources = self.mechanism.get('source_urls', [])
        self.assertGreaterEqual(len(sources), 5)

    def test_mechanism_cross_references_21_25_257(self):
        """Mechanism cross-references #21, #25, #257."""
        xrefs = self.mechanism.get('cross_references', [])
        xref_ids = [x.get('mechanism_id', x) if isinstance(x, dict) else x for x in xrefs]
        for mid in [21, 25, 257]:
            self.assertIn(mid, xref_ids, f"Missing cross-reference to #{mid}")


# =============================================================================
# Class 4: Bank Fee Revenue Incentive Chain
# =============================================================================
class TestBankFeeRevenueIncentive(unittest.TestCase):
    """Verify SpaceX fee data and dual-IPO fee incentive documentation."""

    def setUp(self):
        self.mechanism = find_mechanism(266)

    def test_spacex_fee_data_documented(self):
        """SpaceX IPO fee data documented — $100M each for GS/MS."""
        finding = self.mechanism.get('finding', '')
        fee_data = self.mechanism.get('bank_fee_data', {})
        self.assertTrue(
            '$100' in finding or
            fee_data.get('spacex_gs_fee_m', 0) >= 100 or
            fee_data.get('spacex_ms_fee_m', 0) >= 100,
            "SpaceX fee data ($100M each for GS/MS) not documented"
        )

    def test_dual_ipo_fee_potential_documented(self):
        """Dual AI IPO fee potential is documented (aggregate for GS/MS)."""
        finding = self.mechanism.get('finding', '')
        fee_data = self.mechanism.get('bank_fee_data', {})
        self.assertTrue(
            'fee' in finding.lower() or
            len(fee_data) > 0,
            "Bank fee incentive data not documented"
        )

    def test_credit_facility_bank_jockeying(self):
        """Credit facility banks jockeying for IPO roles is documented."""
        finding = self.mechanism.get('finding', '')
        self.assertIn('credit facility', finding.lower())


# =============================================================================
# Class 5: Publication Financial Interests During Quiet Period
# =============================================================================
class TestPublicationFinancialInterests(unittest.TestCase):
    """Verify that key publications shaping the IPO narrative have documented
    financial interests tied to Anthropic's IPO success."""

    def setUp(self):
        self.mechanism = find_mechanism(266)

    def test_ft_openai_deal_plus_narrative_role(self):
        """FT has OpenAI content deal AND is primary $2T narrative source."""
        narrative_pubs = self.mechanism.get('narrative_shaping_publications', {})
        ft = narrative_pubs.get('financial_times', {})
        self.assertTrue(
            ft.get('has_openai_deal', False) or
            'OpenAI' in ft.get('financial_interest', ''),
            "FT's OpenAI deal + narrative role not documented"
        )

    def test_wsj_newscorp_openai_deal(self):
        """WSJ/News Corp has $250M/5yr OpenAI deal AND reports dual-IPO dynamics."""
        narrative_pubs = self.mechanism.get('narrative_shaping_publications', {})
        wsj = narrative_pubs.get('wsj', narrative_pubs.get('wall_street_journal', {}))
        self.assertTrue(
            wsj.get('parent_openai_deal', False) or
            'News Corp' in wsj.get('financial_interest', '') or
            '$250M' in wsj.get('financial_interest', ''),
            "WSJ/News Corp OpenAI deal not documented"
        )

    def test_meta_has_no_quiet_period_protection(self):
        """Meta has no equivalent quiet period or bank research restriction."""
        finding = self.mechanism.get('finding', '')
        meta_contrast = self.mechanism.get('meta_contrast', '')
        self.assertTrue(
            'Meta' in finding or
            len(meta_contrast) > 0,
            "Meta contrast (no quiet period protection) not documented"
        )

    def test_publication_count_at_least_three(self):
        """At least 3 publications documented as narrative shapers."""
        narrative_pubs = self.mechanism.get('narrative_shaping_publications', {})
        self.assertGreaterEqual(len(narrative_pubs), 3)


# =============================================================================
# Class 6: Asymmetry Score and Confounders
# =============================================================================
class TestAsymmetryScoreAndConfounders(unittest.TestCase):
    """Verify asymmetry scoring and confounder documentation."""

    def setUp(self):
        self.mechanism = find_mechanism(266)

    def test_asymmetry_score_present(self):
        """Mechanism has an asymmetry score."""
        self.assertIn('asymmetry_score', self.mechanism)

    def test_asymmetry_score_in_valid_range(self):
        """Asymmetry score is between 0 and 1."""
        score = self.mechanism['asymmetry_score']
        self.assertGreaterEqual(score, 0.0)
        self.assertLessEqual(score, 1.0)

    def test_confounders_documented(self):
        """At least 3 confounders documented."""
        confounders = self.mechanism.get('confounders', [])
        self.assertGreaterEqual(len(confounders), 3)

    def test_strong_confounder_present(self):
        """At least one STRONG confounder is present."""
        confounders = self.mechanism.get('confounders', [])
        strong = [c for c in confounders
                  if c.get('strength', c.get('type', '')).upper() == 'STRONG']
        self.assertGreaterEqual(len(strong), 1)


# =============================================================================
# Class 7: Source URL Validation
# =============================================================================
class TestSourceURLValidity(unittest.TestCase):
    """Verify all source URLs are present and properly formatted."""

    def setUp(self):
        self.mechanism = find_mechanism(266)

    def test_cryptobriefing_source(self):
        """CryptoBriefing source URL present."""
        urls = self.mechanism.get('source_urls', [])
        self.assertTrue(any('cryptobriefing.com' in u for u in urls))

    def test_wsj_source(self):
        """WSJ source URL present."""
        urls = self.mechanism.get('source_urls', [])
        self.assertTrue(any('wsj.com' in u for u in urls))

    def test_reuters_credit_facility_source(self):
        """Reuters credit facility source URL present."""
        urls = self.mechanism.get('source_urls', [])
        self.assertTrue(any('reuters.com' in u for u in urls))

    def test_investopedia_source(self):
        """Investopedia source URL present."""
        urls = self.mechanism.get('source_urls', [])
        self.assertTrue(any('investopedia.com' in u for u in urls))

    def test_all_urls_start_with_https(self):
        """All source URLs use HTTPS."""
        urls = self.mechanism.get('source_urls', [])
        for url in urls:
            self.assertTrue(url.startswith('https://'), f"Non-HTTPS URL: {url}")


# =============================================================================
# Class 8: Dual-IPO Comparative Structure
# =============================================================================
class TestDualIPOComparativeStructure(unittest.TestCase):
    """Verify OpenAI-Anthropic dual IPO dynamics are documented."""

    def setUp(self):
        entities = load_competitor_entities()
        self.openai = entities['entities']['openai']
        self.anthropic = entities['entities']['anthropic']

    def test_both_have_same_lead_banks(self):
        """Both OpenAI and Anthropic have GS and MS as lead underwriters."""
        openai_banks = set(self.openai['ipo_filing'].get('ipo_banks_reported', []))
        anthropic_banks = set(self.anthropic['ipo_filing'].get('ipo_banks_reported', []))
        overlap = openai_banks & anthropic_banks
        self.assertIn('Goldman Sachs', overlap)
        self.assertIn('Morgan Stanley', overlap)

    def test_anthropic_valuation_exceeds_openai(self):
        """Anthropic's latest valuation ($965B) exceeds OpenAI's ($852B)."""
        openai_val = self.openai['ipo_filing']['valuation_at_filing_b']
        anthropic_val = self.anthropic['ipo_filing']['valuation_at_filing_b']
        self.assertGreater(anthropic_val, openai_val)

    def test_openai_delayed_to_2027(self):
        """OpenAI has signaled possible delay to 2027, making Anthropic the active IPO."""
        # Check revenue trajectory or target listing notes
        target = str(self.openai['ipo_filing'].get('target_listing', ''))
        ipo_race = str(self.openai['ipo_filing'].get('ipo_race_dynamics', ''))
        self.assertTrue(
            '2027' in target or '2027' in ipo_race,
            "OpenAI potential delay to 2027 not documented"
        )


# =============================================================================
# Class 9: Google/Amazon Investor Gain Publication Impact
# =============================================================================
class TestInvestorGainPublicationImpact(unittest.TestCase):
    """Verify that Google and Amazon's Anthropic investor gains and their impact
    on publication advertiser relationships are documented."""

    def setUp(self):
        entities = load_competitor_entities()
        self.anthropic = entities['entities']['anthropic']
        self.ipo = self.anthropic['ipo_filing']

    def test_google_stake_documented(self):
        """Google's ~14% Anthropic stake is documented."""
        investors = self.ipo.get('strategic_investors', [])
        google_entries = [i for i in investors if 'Google' in str(i) or 'Alphabet' in str(i)]
        self.assertGreaterEqual(len(google_entries), 1)

    def test_amazon_stake_documented(self):
        """Amazon's 15-20% Anthropic stake is documented."""
        investors = self.ipo.get('strategic_investors', [])
        amazon_entries = [i for i in investors if 'Amazon' in str(i)]
        self.assertGreaterEqual(len(amazon_entries), 1)

    def test_target_valuation_is_2t(self):
        """Target IPO valuation is $2T."""
        target = self.ipo.get('target_valuation_range_t', 0)
        self.assertGreaterEqual(target, 2.0)

    def test_google_gain_at_2t_documented(self):
        """Google's paper gain at $2T is documented (14% × $2T = ~$280B)."""
        investors = self.ipo.get('strategic_investors', [])
        google_str = str([i for i in investors if 'Google' in str(i) or 'Alphabet' in str(i)])
        self.assertIn('280', google_str, "Google $280B gain at $2T not documented")

    def test_amazon_gain_at_2t_documented(self):
        """Amazon's paper gain at $2T is documented (15-20% × $2T = $300-400B)."""
        investors = self.ipo.get('strategic_investors', [])
        amazon_str = str([i for i in investors if 'Amazon' in str(i)])
        self.assertTrue(
            '300' in amazon_str or '400' in amazon_str,
            "Amazon $300-400B gain at $2T not documented"
        )


if __name__ == '__main__':
    unittest.main()
