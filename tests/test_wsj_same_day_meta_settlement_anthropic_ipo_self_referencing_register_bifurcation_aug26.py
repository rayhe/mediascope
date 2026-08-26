"""
WSJ Same-Day Coverage Register Bifurcation: Meta $18B Settlement vs Anthropic $30T TAM Pre-IPO
Mechanism #326

FINDING: On August 25-26, 2026, the Wall Street Journal published two articles within 24 hours
that demonstrate a self-reinforcing editorial architecture:

1. META SETTLEMENT (Aug 26, Meghan Bobrowsky): "Meta Reaches $18 Billion Settlement With 48
   States Over Child-Safety Claims" — WSJ self-references its own Facebook Files series as
   having precipitated the litigation: "The settlement comes a few years after The Wall Street
   Journal reported on the company's own internal research showing its products were harming
   users in an award-winning series called The Facebook Files."

2. ANTHROPIC IPO (Aug 25, Corrie Driebusch): "Anthropic Expected to Tell Investors It Sees
   Over $30 Trillion in Potential Revenue" — aspirational investment framing. $30T TAM
   (12.5x all S&P 1500 tech revenue) presented with minimal scrutiny. The one skeptical
   quote (Damodaran) is attributed to SpaceX's SMALLER figure, not Anthropic's bigger one.

NOVEL CONTRIBUTIONS:
A) SELF-REFERENCING ACCOUNTABILITY LOOP: WSJ is both investigator and narrator of Meta's
   downfall. Facebook Files → litigation catalyst → settlement → WSJ covers settlement by
   citing its own journalism as the trigger. Creates institutional incentive to maintain
   adversarial Meta posture (franchise validation).

B) DUAL-ROLE FINANCIAL ARCHITECTURE: News Corp profits from BOTH directions simultaneously:
   - Meta accountability: Facebook Files franchise → subscriber engagement → awards
   - Anthropic IPO: $1.5B Bartz settlement recovery depends on Anthropic solvency/IPO
   These are not competing interests — they're complementary. Harder Meta coverage and
   softer Anthropic coverage BOTH serve News Corp's financial position.

C) SETTLEMENT-ADJACENT TAM CREDULITY: WSJ presents Anthropic's $30T TAM — a figure exceeding
   US GDP — with one lightly offset skeptical quote. By contrast, Meta's $130-145B capex
   (backed by $60.8B quarterly revenue and positive FCF) received intensive scrutiny across
   multiple WSJ articles. The ratio of scrutiny to projection magnitude is inverted.

D) NON-DISCLOSURE IN SELF-REFERENCING COVERAGE: WSJ's settlement article doesn't disclose
   News Corp's $50M/yr content licensing deal with Meta. WSJ's Anthropic IPO articles don't
   disclose News Corp's $1.5B settlement interest. Neither article carries financial
   relationship disclosure.

SOURCES:
- WSJ: https://www.wsj.com/tech/meta-reaches-18-billion-settlement-with-48-states-over-child-safety-claims-cf725a2b
- WSJ: https://www.wsj.com/tech/ai/anthropic-expected-to-tell-investors-it-sees-over-30-trillion-in-potential-revenue-a611efea
- WSJ: https://www.wsj.com/tech/ai/anthropic-tries-to-shore-up-investor-confidence-ahead-of-blockbuster-ipo-0ff736ad
- WSJ CEO Brief: https://www.wsj.com/cio-journal/anthropic-contemplates-the-ultimate-total-addressable-market-4cc2deed
"""

import unittest
import yaml
import os


def load_competitor_research():
    """Load competitor coverage research YAML."""
    path = os.path.join(os.path.dirname(__file__), '..', 'profiles', 'competitor-coverage-research.yaml')
    with open(path) as f:
        return yaml.safe_load(f)


def load_news_corp_profile():
    """Load News Corp publication profile."""
    path = os.path.join(os.path.dirname(__file__), '..', 'profiles', 'news-corp.yaml')
    with open(path) as f:
        return yaml.safe_load(f)


def get_mechanism(data, mechanism_id):
    """Find mechanism by ID in research data."""
    mechanisms = data.get('mechanisms', data.get('coverage_analysis', {}).get('mechanisms', []))
    if isinstance(mechanisms, list):
        for m in mechanisms:
            if m.get('mechanism_id') == mechanism_id:
                return m
    # Also check nested structures
    for key, val in data.items():
        if isinstance(val, dict):
            for subkey, subval in val.items():
                if isinstance(subval, list):
                    for item in subval:
                        if isinstance(item, dict) and item.get('mechanism_id') == mechanism_id:
                            return item
                elif isinstance(subval, dict) and subval.get('mechanism_id') == mechanism_id:
                    return subval
    return None


class TestSameDayRegisterBifurcation(unittest.TestCase):
    """Test the same-day editorial register split between Meta settlement and Anthropic IPO."""

    def test_meta_settlement_article_exists(self):
        """WSJ Meta settlement article (Aug 26, 2026) is documented."""
        data = load_competitor_research()
        mech = get_mechanism(data, 326)
        self.assertIsNotNone(mech, "Mechanism #326 must exist")
        articles = mech.get('articles', [])
        meta_settlement = [a for a in articles if 'settlement' in a.get('title', '').lower()
                          and a.get('entity') == 'Meta']
        self.assertTrue(len(meta_settlement) > 0, "Must document Meta settlement article")
        self.assertIn('2026-08-26', meta_settlement[0].get('date', ''))

    def test_anthropic_tam_article_exists(self):
        """WSJ Anthropic $30T TAM article (Aug 25, 2026) is documented."""
        data = load_competitor_research()
        mech = get_mechanism(data, 326)
        self.assertIsNotNone(mech)
        articles = mech.get('articles', [])
        anthro_tam = [a for a in articles if 'trillion' in a.get('title', '').lower()
                     and a.get('entity') == 'Anthropic']
        self.assertTrue(len(anthro_tam) > 0, "Must document Anthropic TAM article")

    def test_temporal_adjacency_within_24_hours(self):
        """Articles are within 24-hour window for same-day natural experiment validity."""
        data = load_competitor_research()
        mech = get_mechanism(data, 326)
        self.assertIsNotNone(mech)
        date_range = mech.get('date_range', '')
        self.assertIn('2026-08-25', date_range)
        self.assertIn('2026-08-26', date_range)

    def test_different_reporters_same_desk(self):
        """Different reporters but same editorial desk — institutional voice, not individual."""
        data = load_competitor_research()
        mech = get_mechanism(data, 326)
        self.assertIsNotNone(mech)
        articles = mech.get('articles', [])
        reporters = set()
        for a in articles:
            r = a.get('reporter', '')
            if r:
                reporters.add(r)
        self.assertTrue(len(reporters) >= 2,
                       "Must have at least 2 different reporters to demonstrate institutional voice")


class TestSelfReferencingAccountabilityLoop(unittest.TestCase):
    """Test WSJ self-referencing its own Facebook Files in settlement coverage."""

    def test_self_referencing_documented(self):
        """Mechanism documents WSJ self-referencing Facebook Files in settlement article."""
        data = load_competitor_research()
        mech = get_mechanism(data, 326)
        self.assertIsNotNone(mech)
        self_ref = mech.get('self_referencing_loop', {})
        self.assertTrue(self_ref.get('facebook_files_self_citation', False),
                       "Must document Facebook Files self-citation")

    def test_narrative_circularity_chain(self):
        """Documents the investigation → litigation → settlement → self-validation chain."""
        data = load_competitor_research()
        mech = get_mechanism(data, 326)
        self.assertIsNotNone(mech)
        self_ref = mech.get('self_referencing_loop', {})
        chain = self_ref.get('chain', [])
        required_stages = ['investigation', 'litigation', 'settlement', 'self_validation']
        for stage in required_stages:
            found = any(stage in str(c).lower() for c in chain)
            self.assertTrue(found, f"Chain must include {stage} stage")

    def test_award_mention_in_self_reference(self):
        """WSJ describes Facebook Files as 'award-winning' in settlement coverage."""
        data = load_competitor_research()
        mech = get_mechanism(data, 326)
        self.assertIsNotNone(mech)
        self_ref = mech.get('self_referencing_loop', {})
        self.assertTrue(self_ref.get('award_winning_descriptor', False),
                       "WSJ uses 'award-winning' descriptor for its own series")

    def test_institutional_incentive_to_maintain_adversarial_posture(self):
        """Self-referencing creates institutional incentive to maintain adversarial Meta posture."""
        data = load_competitor_research()
        mech = get_mechanism(data, 326)
        self.assertIsNotNone(mech)
        self_ref = mech.get('self_referencing_loop', {})
        incentive = self_ref.get('institutional_incentive', '')
        self.assertIn('franchise', incentive.lower(),
                     "Must document franchise validation incentive")


class TestDualRoleFinancialArchitecture(unittest.TestCase):
    """Test News Corp's complementary financial interests in both directions."""

    def test_meta_licensing_deal_documented(self):
        """News Corp-Meta content licensing deal ($50M/yr) documented."""
        data = load_competitor_research()
        mech = get_mechanism(data, 326)
        self.assertIsNotNone(mech)
        fin = mech.get('financial_architecture', {})
        meta_deal = fin.get('meta_deal', {})
        self.assertGreater(meta_deal.get('annual_value_m', 0), 0)

    def test_anthropic_settlement_interest_documented(self):
        """News Corp $1.5B Anthropic settlement recovery interest documented."""
        data = load_competitor_research()
        mech = get_mechanism(data, 326)
        self.assertIsNotNone(mech)
        fin = mech.get('financial_architecture', {})
        anthro = fin.get('anthropic_settlement', {})
        self.assertGreaterEqual(anthro.get('total_value_b', 0), 1.5)

    def test_complementary_not_competing(self):
        """Both directions serve News Corp's financial position simultaneously."""
        data = load_competitor_research()
        mech = get_mechanism(data, 326)
        self.assertIsNotNone(mech)
        fin = mech.get('financial_architecture', {})
        self.assertTrue(fin.get('complementary_incentives', False),
                       "Must document that harder-Meta + softer-Anthropic are complementary, not competing")

    def test_facebook_files_franchise_value(self):
        """Facebook Files franchise value (awards, subscribers, institutional reputation) documented."""
        data = load_competitor_research()
        mech = get_mechanism(data, 326)
        self.assertIsNotNone(mech)
        fin = mech.get('financial_architecture', {})
        franchise = fin.get('facebook_files_franchise', {})
        self.assertTrue(len(franchise) > 0,
                       "Must document Facebook Files franchise value components")

    def test_ipo_settlement_recovery_chain(self):
        """Anthropic IPO success → settlement recovery → News Corp revenue chain documented."""
        data = load_competitor_research()
        mech = get_mechanism(data, 326)
        self.assertIsNotNone(mech)
        fin = mech.get('financial_architecture', {})
        anthro = fin.get('anthropic_settlement', {})
        self.assertTrue(anthro.get('ipo_dependent', False),
                       "Settlement recovery depends on IPO success")


class TestVocabularyRegisterAnalysis(unittest.TestCase):
    """Test vocabulary differences between Meta and Anthropic coverage."""

    def test_meta_accountability_vocabulary(self):
        """Meta settlement article uses accountability/punitive vocabulary."""
        data = load_competitor_research()
        mech = get_mechanism(data, 326)
        self.assertIsNotNone(mech)
        meta_vocab = mech.get('meta_vocabulary', [])
        accountability_terms = [v for v in meta_vocab if any(t in v.lower() for t in
            ['settlement', 'harm', 'addict', 'liability', 'accountability',
             'knowingly', 'ushering', 'massive', 'went after'])]
        self.assertGreater(len(accountability_terms), 3,
                          f"Must have 4+ accountability terms, found: {accountability_terms}")

    def test_anthropic_aspirational_vocabulary(self):
        """Anthropic TAM article uses aspirational/investment vocabulary."""
        data = load_competitor_research()
        mech = get_mechanism(data, 326)
        self.assertIsNotNone(mech)
        anthro_vocab = mech.get('anthropic_vocabulary', [])
        aspirational_terms = [v for v in anthro_vocab if any(t in v.lower() for t in
            ['trillion', 'potential', 'blockbuster', 'robust', 'doubled',
             'top', 'cutting-edge', 'front-runner'])]
        self.assertGreater(len(aspirational_terms), 3,
                          f"Must have 4+ aspirational terms, found: {aspirational_terms}")

    def test_tone_delta(self):
        """Tone delta between Meta and Anthropic coverage is significant."""
        data = load_competitor_research()
        mech = get_mechanism(data, 326)
        self.assertIsNotNone(mech)
        delta = mech.get('tone_delta', 0)
        self.assertGreater(abs(delta), 0.5,
                          "Tone delta must exceed 0.5 for statistical significance")


class TestScrutinyMagnitudeInversion(unittest.TestCase):
    """Test that scrutiny is inversely proportional to claim magnitude."""

    def test_tam_exceeds_us_gdp(self):
        """Anthropic $30T TAM exceeds US GDP (~$29T), documented."""
        data = load_competitor_research()
        mech = get_mechanism(data, 326)
        self.assertIsNotNone(mech)
        scrutiny = mech.get('scrutiny_magnitude_analysis', {})
        self.assertTrue(scrutiny.get('tam_exceeds_us_gdp', False))

    def test_tam_vs_sp1500_tech_revenue_ratio(self):
        """$30T TAM is 12.5x all S&P 1500 tech company revenue, documented."""
        data = load_competitor_research()
        mech = get_mechanism(data, 326)
        self.assertIsNotNone(mech)
        scrutiny = mech.get('scrutiny_magnitude_analysis', {})
        ratio = scrutiny.get('tam_to_sp1500_tech_revenue_multiple', 0)
        self.assertGreater(ratio, 10, "TAM/S&P 1500 tech revenue multiple must exceed 10x")

    def test_skeptical_quote_misdirection(self):
        """Damodaran skepticism quote is about SpaceX's smaller figure, not Anthropic's bigger one."""
        data = load_competitor_research()
        mech = get_mechanism(data, 326)
        self.assertIsNotNone(mech)
        scrutiny = mech.get('scrutiny_magnitude_analysis', {})
        self.assertTrue(scrutiny.get('skepticism_misdirected_to_smaller_figure', False),
                       "Skeptical quote targets SpaceX $28.5T, not Anthropic $30T+")

    def test_meta_capex_scrutiny_comparison(self):
        """Meta's smaller, revenue-backed capex receives MORE scrutiny than Anthropic's TAM."""
        data = load_competitor_research()
        mech = get_mechanism(data, 326)
        self.assertIsNotNone(mech)
        scrutiny = mech.get('scrutiny_magnitude_analysis', {})
        meta = scrutiny.get('meta_capex', {})
        self.assertIn('intensive', meta.get('scrutiny_level', '').lower())

    def test_inversion_ratio_documented(self):
        """Scrutiny-to-magnitude ratio inversion is explicitly documented."""
        data = load_competitor_research()
        mech = get_mechanism(data, 326)
        self.assertIsNotNone(mech)
        scrutiny = mech.get('scrutiny_magnitude_analysis', {})
        self.assertTrue(scrutiny.get('inversion_documented', False),
                       "Must explicitly document that larger claim gets less scrutiny")


class TestNonDisclosureAsymmetry(unittest.TestCase):
    """Test non-disclosure of financial relationships in both articles."""

    def test_meta_article_no_licensing_disclosure(self):
        """Meta settlement article doesn't disclose News Corp-Meta licensing deal."""
        data = load_competitor_research()
        mech = get_mechanism(data, 326)
        self.assertIsNotNone(mech)
        disclosure = mech.get('non_disclosure_analysis', {})
        self.assertFalse(disclosure.get('meta_article_discloses_licensing', False))

    def test_anthropic_article_no_settlement_disclosure(self):
        """Anthropic IPO article doesn't disclose News Corp settlement interest."""
        data = load_competitor_research()
        mech = get_mechanism(data, 326)
        self.assertIsNotNone(mech)
        disclosure = mech.get('non_disclosure_analysis', {})
        self.assertFalse(disclosure.get('anthropic_article_discloses_settlement_interest', False))

    def test_bidirectional_non_disclosure(self):
        """Non-disclosure is bidirectional — neither direction carries conflict notice."""
        data = load_competitor_research()
        mech = get_mechanism(data, 326)
        self.assertIsNotNone(mech)
        disclosure = mech.get('non_disclosure_analysis', {})
        self.assertTrue(disclosure.get('bidirectional_non_disclosure', False))


class TestSettlementAmountComparison(unittest.TestCase):
    """Test comparative framing of Meta $18B settlement vs Anthropic $1.5B copyright settlement."""

    def test_meta_settlement_amount(self):
        """Meta child safety settlement amount ($18B) documented."""
        data = load_competitor_research()
        mech = get_mechanism(data, 326)
        self.assertIsNotNone(mech)
        settlements = mech.get('settlement_comparison', {})
        self.assertGreaterEqual(settlements.get('meta_child_safety_b', 0), 16)

    def test_anthropic_copyright_settlement_amount(self):
        """Anthropic copyright settlement amount ($1.5B) documented."""
        data = load_competitor_research()
        mech = get_mechanism(data, 326)
        self.assertIsNotNone(mech)
        settlements = mech.get('settlement_comparison', {})
        self.assertGreaterEqual(settlements.get('anthropic_copyright_b', 0), 1.5)

    def test_settlement_coverage_volume_asymmetry(self):
        """Meta $18B settlement gets more WSJ articles than Anthropic $1.5B settlement."""
        data = load_competitor_research()
        mech = get_mechanism(data, 326)
        self.assertIsNotNone(mech)
        settlements = mech.get('settlement_comparison', {})
        meta_articles = settlements.get('meta_wsj_articles', 0)
        anthro_articles = settlements.get('anthropic_wsj_articles', 0)
        self.assertGreater(meta_articles, anthro_articles,
                          "Meta settlement gets more WSJ coverage volume")

    def test_piracy_vocabulary_comparison(self):
        """Anthropic copyright case (pirated books) gets softer vocabulary than Meta child safety."""
        data = load_competitor_research()
        mech = get_mechanism(data, 326)
        self.assertIsNotNone(mech)
        settlements = mech.get('settlement_comparison', {})
        self.assertTrue(settlements.get('piracy_vocabulary_differential', False))


class TestConfounders(unittest.TestCase):
    """Test documented confounders for the mechanism."""

    def test_severity_confounder(self):
        """STRONG confounder: Meta child safety case IS more severe than Anthropic IPO news."""
        data = load_competitor_research()
        mech = get_mechanism(data, 326)
        self.assertIsNotNone(mech)
        confounders = mech.get('confounders', [])
        severity = [c for c in confounders if 'severe' in str(c).lower() or 'severity' in str(c).lower()]
        self.assertTrue(len(severity) > 0, "Must document severity confounder")
        if isinstance(severity[0], dict):
            self.assertIn('STRONG', severity[0].get('strength', ''))
        else:
            self.assertIn('STRONG', str(severity[0]))

    def test_event_type_confounder(self):
        """MODERATE confounder: Different event types (settlement vs IPO are different story genres)."""
        data = load_competitor_research()
        mech = get_mechanism(data, 326)
        self.assertIsNotNone(mech)
        confounders = mech.get('confounders', [])
        event_type = [c for c in confounders if 'event type' in str(c).lower() or 'genre' in str(c).lower()]
        self.assertTrue(len(event_type) > 0, "Must document event type/genre confounder")

    def test_counter_confounding_scrutiny_inversion(self):
        """COUNTER-CONFOUNDING: Larger Anthropic claims get LESS scrutiny than smaller Meta claims."""
        data = load_competitor_research()
        mech = get_mechanism(data, 326)
        self.assertIsNotNone(mech)
        confounders = mech.get('confounders', [])
        counter = [c for c in confounders if 'COUNTER' in str(c)]
        self.assertTrue(len(counter) > 0, "Must document counter-confounding evidence")

    def test_counter_confounding_non_disclosure(self):
        """COUNTER-CONFOUNDING: Neither article discloses News Corp financial relationships."""
        data = load_competitor_research()
        mech = get_mechanism(data, 326)
        self.assertIsNotNone(mech)
        confounders = mech.get('confounders', [])
        non_disc = [c for c in confounders if 'non-disclosure' in str(c).lower() or 'disclose' in str(c).lower()]
        self.assertTrue(len(non_disc) > 0, "Must document non-disclosure counter-confounder")


class TestAsymmetryScore(unittest.TestCase):
    """Test overall asymmetry scoring."""

    def test_asymmetry_score_tempered(self):
        """Asymmetry score is tempered by strong confounders (severity difference)."""
        data = load_competitor_research()
        mech = get_mechanism(data, 326)
        self.assertIsNotNone(mech)
        score = mech.get('asymmetry_score', 0)
        self.assertGreater(score, 0.4, "Score must exceed 0.4 (pattern exists)")
        self.assertLess(score, 0.85, "Score must be below 0.85 (strong confounders)")

    def test_mechanism_classification(self):
        """Mechanism classified as self-referencing financial architecture."""
        data = load_competitor_research()
        mech = get_mechanism(data, 326)
        self.assertIsNotNone(mech)
        mech_type = mech.get('type', '')
        self.assertIn('self_referencing', mech_type.lower())

    def test_cross_reference_to_mechanism_317(self):
        """Cross-references mechanism #317 (WSJ Anthropic pre-IPO aspirational narrative)."""
        data = load_competitor_research()
        mech = get_mechanism(data, 326)
        self.assertIsNotNone(mech)
        cross_refs = mech.get('cross_references', [])
        ref_317 = [r for r in cross_refs if r.get('mechanism_id') == 317]
        self.assertTrue(len(ref_317) > 0, "Must cross-reference mechanism #317")


class TestCEOBriefAmplification(unittest.TestCase):
    """Test WSJ CEO Brief newsletter amplification of Anthropic TAM narrative."""

    def test_ceo_brief_amplification_documented(self):
        """WSJ CEO Brief (Steven Rosenbush) amplifies $30T TAM narrative on Aug 26."""
        data = load_competitor_research()
        mech = get_mechanism(data, 326)
        self.assertIsNotNone(mech)
        amplification = mech.get('ceo_brief_amplification', {})
        self.assertTrue(len(amplification) > 0,
                       "Must document CEO Brief newsletter amplification")

    def test_newsletter_same_day_as_settlement(self):
        """CEO Brief amplification runs on same day as Meta settlement coverage."""
        data = load_competitor_research()
        mech = get_mechanism(data, 326)
        self.assertIsNotNone(mech)
        amplification = mech.get('ceo_brief_amplification', {})
        self.assertIn('2026-08-26', str(amplification.get('date', '')))


if __name__ == '__main__':
    unittest.main()
