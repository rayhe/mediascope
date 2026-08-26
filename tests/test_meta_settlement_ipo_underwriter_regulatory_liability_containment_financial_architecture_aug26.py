"""
Meta $17B Settlement — IPO Underwriter-Publisher Regulatory Liability Containment Financial Architecture
Mechanism #328

FINDING: Meta's $17-18B child safety settlement with 47 states (Aug 26, 2026) — the largest single-
company multistate settlement in US history — establishes state AG enforcement precedent for tech
platform child safety liability. The SAME state attorneys general (led by CA AG Rob Bonta) who
extracted $17B from Meta sent a 44-AG letter to OpenAI, Anthropic, Google, Apple, and 8 other AI
companies (Aug 2025) explicitly warning: "If you knowingly harm kids, you will answer for it."

OpenAI faces COMPARABLE litigation: the Adam Raine wrongful death lawsuit alleges ChatGPT-4o
advised a 16-year-old on suicide methods over months, leading to his death (Apr 2025). OpenAI
disclosed that 1.2 million ChatGPT users discuss suicide weekly. Character.AI/Google already
settled a comparable teen suicide case (Garcia). The FTC launched a formal inquiry into AI chatbot
companion risks targeting OpenAI, Meta, Alphabet, Character.AI, Snap, and xAI (Sep 2025).

IPO UNDERWRITER FINANCIAL ARCHITECTURE:
Goldman Sachs, Morgan Stanley, and JPMorgan Chase are lead underwriters for BOTH OpenAI ($852B)
and Anthropic ($965B→$2T) IPOs targeting late 2026/2027. If the $17B Meta settlement precedent
is priced as regulatory risk for AI chatbot companies, it could materially impact IPO valuations.
Combined underwriting fee exposure on deals of this magnitude: $500M-$2B+.

COVERAGE TEST (Aug 26, 2026 settlement day):
Publications with financial ties to AI labs covered Meta settlement adversarially WITHOUT drawing
the parallel to comparable AI chatbot child safety liability:
- CNN (WBD): Clare Duffy, 94 lines, ZERO mentions of OpenAI/Anthropic/ChatGPT/Claude or
  comparable AI lab child safety risks
- Bloomberg Tax: Meta payment structure focus, no AI lab comparison
- AP wire: Distributed to dozens of outlets, no AI lab comparison
- Reuters: Settlement details, no AI lab comparison

The omission is notable because:
1. The 44-AG letter named BOTH Meta and OpenAI/Anthropic for the same child safety concerns
2. OpenAI's Adam Raine case involves DIRECT causation (chatbot advised suicide methods) vs
   Meta's INDIRECT causation (addictive design features)
3. Anthropic's October 2026 IPO S-1 will need to disclose material litigation risks — the
   $17B precedent is directly relevant to prospective investors

CONFOUNDERS:
- STRONG: Genre — settlement coverage naturally focuses on the settling party
- STRONG: Breaking news — tight deadlines limit comparative analysis
- MODERATE: Legal specificity — social media addictive design ≠ AI chatbot interactions
  (different legal theories, different harm mechanisms)
- MODERATE: Scale — Meta has 3B+ users; ChatGPT has ~800M weekly users
- WEAK: Severity proportionality — ChatGPT direct suicide instruction may be MORE severe
  than Meta's indirect addictive design, suggesting UNDER-coverage if anything
- COUNTER-CONFOUNDING: Publications DID include comparative context about TikTok and YouTube
  (Meta's conditional 30% clause), proving genre does not preclude cross-entity comparison.
  The comparison to OTHER social media platforms was included; the comparison to AI chatbot
  platforms (facing the same AG warnings) was not.

SOURCES:
- CNN Meta settlement: https://www.cnn.com/2026/08/26/tech/meta-states-settle-trial-children
- Reuters settlement details: https://www.reuters.com/legal/government/what-meta-agreed-us-teen-safety-settlement-2026-08-26/
- AP via Barchart: https://www.barchart.com/story/news/4105091/meta-reaches-17-billion-settlement-with-states-in-landmark-trial-over-teen-social-media-addiction
- Bloomberg Tax: https://news.bloombergtax.com/artificial-intelligence/meta-states-agree-to-settle-teen-social-media-harm-case
- 44 AG letter to AI companies (Aug 2025): https://oag.ca.gov/news/press-releases/attorney-general-bonta-warns-ai-companies-if-you-harm-children-you-will-be-held
- FTC AI chatbot inquiry (Sep 2025): https://techcrunch.com/2025/09/11/ftc-launches-inquiry-into-ai-chatbot-companions-from-meta-openai-and-others/
- OpenAI Adam Raine lawsuit: https://gizmodo.com/openai-suicide-safety-issues-adam-raine-2000649307
- OpenAI 1.2M weekly suicide discussions: https://decrypt.co/353927/google-character-ai-settle-us-lawsuit-teens-suicide
- Anthropic IPO banks (Goldman, Morgan Stanley, JPMorgan): https://www.pymnts.com/news/investment-tracker/ipo/2026/morgan-stanley-and-goldman-sachs-land-anthropic-ipo/
- OpenAI IPO banks (Goldman, Morgan Stanley): https://www.wsj.com/finance/banking/the-ipo-onslaught-is-forcing-bankers-to-pick-teams-50fab052
- WSJ: Both banks forming "distinct teams" for competing IPOs: https://www.wsj.com/finance/banking/the-ipo-onslaught-is-forcing-bankers-to-pick-teams-50fab052
"""

import unittest
import yaml
import os


def load_competitor_research():
    """Load competitor coverage research YAML."""
    path = os.path.join(os.path.dirname(__file__), '..', 'profiles', 'competitor-coverage-research.yaml')
    with open(path) as f:
        return yaml.safe_load(f)


def load_competitor_entities():
    """Load competitor entities YAML."""
    path = os.path.join(os.path.dirname(__file__), '..', 'profiles', 'competitor-entities.yaml')
    with open(path) as f:
        return yaml.safe_load(f)


def get_mechanism(data, mechanism_id):
    """Find mechanism by ID in research data."""
    mechanisms = data.get('mechanisms', data.get('coverage_analysis', {}).get('mechanisms', []))
    if isinstance(mechanisms, list):
        for m in mechanisms:
            if m.get('mechanism_id') == mechanism_id:
                return m
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


# =============================================================================
# TEST CLASS 1: Settlement Regulatory Precedent Documentation
# =============================================================================
class TestSettlementRegulatoryPrecedent(unittest.TestCase):
    """Verify mechanism #328 documents the Meta settlement as regulatory precedent."""

    def test_mechanism_exists(self):
        """Mechanism #328 must exist in competitor research YAML."""
        data = load_competitor_research()
        mech = get_mechanism(data, 328)
        self.assertIsNotNone(mech, "Mechanism #328 must exist in competitor-coverage-research.yaml")

    def test_settlement_amount_documented(self):
        """Settlement amount ($17-18B) documented."""
        data = load_competitor_research()
        mech = get_mechanism(data, 328)
        self.assertIsNotNone(mech)
        desc = str(mech)
        self.assertTrue('17' in desc or '18' in desc,
                       "Must document $17-18B settlement amount")

    def test_state_count_documented(self):
        """Number of participating states documented."""
        data = load_competitor_research()
        mech = get_mechanism(data, 328)
        self.assertIsNotNone(mech)
        desc = str(mech)
        # Check for state counts: 47 states, or 29 states in original suit, or 52 entities total
        self.assertTrue('47' in desc or '48' in desc or '29' in desc or '52' in desc,
                       "Must document number of participating states/entities")

    def test_largest_settlement_precedent(self):
        """Documents this as the largest single-company multistate settlement in history."""
        data = load_competitor_research()
        mech = get_mechanism(data, 328)
        self.assertIsNotNone(mech)
        desc = str(mech).lower()
        self.assertTrue('largest' in desc or 'record' in desc or 'historic' in desc,
                       "Must document precedent-setting scale")

    def test_conditional_payment_structure(self):
        """Documents the 70/30 conditional structure (30% contingent on rival settlements)."""
        data = load_competitor_research()
        mech = get_mechanism(data, 328)
        self.assertIsNotNone(mech)
        ss = mech.get('settlement_structure', {})
        # guaranteed_pct may be at settlement_structure level or nested
        guaranteed = ss.get('guaranteed_pct', 0) or ss.get('conditional_payment', {}).get('guaranteed_pct', 0)
        self.assertTrue(guaranteed >= 70,
                       "Must document 70% guaranteed payment")
        conditional_targets = ss.get('conditional_payment', {}).get('contingent_on', [])
        self.assertTrue(any('TikTok' in str(t) for t in conditional_targets),
                       "Contingent targets must include TikTok")
        self.assertTrue(any('YouTube' in str(t) for t in conditional_targets),
                       "Contingent targets must include YouTube")

    def test_conditional_excludes_ai_chatbot_companies(self):
        """Conditional 30% targets social media rivals (TikTok, YouTube) not AI labs."""
        data = load_competitor_research()
        mech = get_mechanism(data, 328)
        self.assertIsNotNone(mech)
        conditional = mech.get('settlement_structure', {}).get('conditional_payment', {})
        targets = conditional.get('contingent_on', [])
        targets_str = str(targets).lower()
        self.assertNotIn('openai', targets_str,
                        "Conditional targets do NOT include OpenAI")
        self.assertNotIn('anthropic', targets_str,
                        "Conditional targets do NOT include Anthropic")


# =============================================================================
# TEST CLASS 2: Same-AG Cross-Entity Warning Documentation
# =============================================================================
class TestSameAGCrossEntityWarning(unittest.TestCase):
    """Verify the same AGs warned both Meta and AI labs about child safety."""

    def test_44_ag_letter_documented(self):
        """Documents the 44-AG letter to AI companies (Aug 2025)."""
        data = load_competitor_research()
        mech = get_mechanism(data, 328)
        self.assertIsNotNone(mech)
        ag_letter = mech.get('same_ag_cross_entity_warning', {})
        self.assertIsNotNone(ag_letter.get('date'),
                            "Must document AG letter date")

    def test_ag_letter_targeted_openai(self):
        """AG letter explicitly named OpenAI."""
        data = load_competitor_research()
        mech = get_mechanism(data, 328)
        self.assertIsNotNone(mech)
        ag_letter = mech.get('same_ag_cross_entity_warning', {})
        recipients = ag_letter.get('recipients', [])
        self.assertTrue(any('OpenAI' in str(r) for r in recipients),
                       "AG letter must list OpenAI as recipient")

    def test_ag_letter_targeted_anthropic(self):
        """AG letter explicitly named Anthropic."""
        data = load_competitor_research()
        mech = get_mechanism(data, 328)
        self.assertIsNotNone(mech)
        ag_letter = mech.get('same_ag_cross_entity_warning', {})
        recipients = ag_letter.get('recipients', [])
        self.assertTrue(any('Anthropic' in str(r) for r in recipients),
                       "AG letter must list Anthropic as recipient")

    def test_same_lead_ag_rob_bonta(self):
        """CA AG Rob Bonta led both the Meta settlement and the AI company warning letter."""
        data = load_competitor_research()
        mech = get_mechanism(data, 328)
        self.assertIsNotNone(mech)
        ag_letter = mech.get('same_ag_cross_entity_warning', {})
        self.assertIn('Bonta', ag_letter.get('lead_ag', ''),
                     "CA AG Bonta must be documented as leading both actions")

    def test_letter_quote_accountability_language(self):
        """Documents the explicit accountability language from AG letter."""
        data = load_competitor_research()
        mech = get_mechanism(data, 328)
        self.assertIsNotNone(mech)
        ag_letter = mech.get('same_ag_cross_entity_warning', {})
        quote = ag_letter.get('key_quote', '')
        self.assertTrue('accountable' in quote.lower() or 'answer for it' in quote.lower(),
                       "Must include accountability language from AG letter")


# =============================================================================
# TEST CLASS 3: Comparable AI Lab Litigation Risk
# =============================================================================
class TestComparableAILabLitigationRisk(unittest.TestCase):
    """Verify documentation of comparable AI lab child safety litigation."""

    def test_openai_adam_raine_case_documented(self):
        """OpenAI Adam Raine wrongful death case documented."""
        data = load_competitor_research()
        mech = get_mechanism(data, 328)
        self.assertIsNotNone(mech)
        ai_lab_risk = mech.get('comparable_ai_lab_litigation', {})
        openai_cases = ai_lab_risk.get('openai', {}).get('cases', [])
        raine = [c for c in openai_cases if 'Raine' in str(c)]
        self.assertTrue(len(raine) > 0, "Must document Adam Raine case")

    def test_openai_suicide_discussion_scale(self):
        """OpenAI disclosed 1.2M weekly users discuss suicide on ChatGPT."""
        data = load_competitor_research()
        mech = get_mechanism(data, 328)
        self.assertIsNotNone(mech)
        ai_lab_risk = mech.get('comparable_ai_lab_litigation', {})
        openai_data = ai_lab_risk.get('openai', {})
        suicide_weekly = openai_data.get('weekly_suicide_discussions', 0)
        self.assertGreaterEqual(suicide_weekly, 1200000,
                               "Must document 1.2M+ weekly suicide discussions")

    def test_chatgpt_direct_causation_vs_meta_indirect(self):
        """Documents the direct vs indirect causation contrast."""
        data = load_competitor_research()
        mech = get_mechanism(data, 328)
        self.assertIsNotNone(mech)
        ai_lab_risk = mech.get('comparable_ai_lab_litigation', {})
        causation = ai_lab_risk.get('causation_comparison', {})
        meta_type = causation.get('meta', '')
        openai_type = causation.get('openai', '')
        self.assertIn('indirect', meta_type.lower(),
                     "Meta causation is indirect (addictive design)")
        self.assertIn('direct', openai_type.lower(),
                     "OpenAI causation is direct (chatbot advised suicide methods)")

    def test_character_ai_google_settlement_documented(self):
        """Character.AI/Google teen suicide settlement is documented as precedent."""
        data = load_competitor_research()
        mech = get_mechanism(data, 328)
        self.assertIsNotNone(mech)
        ai_lab_risk = mech.get('comparable_ai_lab_litigation', {})
        char_ai = ai_lab_risk.get('character_ai', {})
        self.assertTrue(char_ai.get('settled', False),
                       "Character.AI/Google settlement must be documented")

    def test_ftc_inquiry_scope_documented(self):
        """FTC AI chatbot companion inquiry (Sep 2025) scope is documented."""
        data = load_competitor_research()
        mech = get_mechanism(data, 328)
        self.assertIsNotNone(mech)
        ai_lab_risk = mech.get('comparable_ai_lab_litigation', {})
        ftc = ai_lab_risk.get('ftc_inquiry', {})
        targets = ftc.get('targets', [])
        self.assertTrue(len(targets) >= 5,
                       "FTC inquiry targeted 7 companies")
        self.assertTrue(any('OpenAI' in str(t) for t in targets),
                       "FTC inquiry must target OpenAI")


# =============================================================================
# TEST CLASS 4: IPO Underwriter Financial Architecture
# =============================================================================
class TestIPOUnderwriterFinancialArchitecture(unittest.TestCase):
    """Verify IPO underwriter financial incentive mapping."""

    def test_shared_underwriters_documented(self):
        """Goldman Sachs, Morgan Stanley, JPMorgan underwrite BOTH OpenAI and Anthropic IPOs."""
        data = load_competitor_research()
        mech = get_mechanism(data, 328)
        self.assertIsNotNone(mech)
        underwriters = mech.get('ipo_underwriter_architecture', {})
        shared = underwriters.get('shared_banks', [])
        self.assertIn('Goldman Sachs', shared)
        self.assertIn('Morgan Stanley', shared)

    def test_openai_ipo_valuation(self):
        """OpenAI IPO valuation ($852B) documented."""
        data = load_competitor_research()
        mech = get_mechanism(data, 328)
        self.assertIsNotNone(mech)
        underwriters = mech.get('ipo_underwriter_architecture', {})
        openai_val = underwriters.get('openai_valuation_b', 0)
        self.assertGreaterEqual(openai_val, 852,
                               "OpenAI valuation must be >= $852B")

    def test_anthropic_ipo_valuation(self):
        """Anthropic IPO valuation ($965B, targeting $2T) documented."""
        data = load_competitor_research()
        mech = get_mechanism(data, 328)
        self.assertIsNotNone(mech)
        underwriters = mech.get('ipo_underwriter_architecture', {})
        anthro_val = underwriters.get('anthropic_valuation_b', 0)
        self.assertGreaterEqual(anthro_val, 965,
                               "Anthropic valuation must be >= $965B")

    def test_underwriting_fee_exposure(self):
        """Combined underwriting fee exposure documented."""
        data = load_competitor_research()
        mech = get_mechanism(data, 328)
        self.assertIsNotNone(mech)
        underwriters = mech.get('ipo_underwriter_architecture', {})
        fees = underwriters.get('estimated_combined_fees', '')
        self.assertTrue('500' in str(fees) or 'billion' in str(fees).lower() or 'B' in str(fees),
                       "Must document substantial underwriting fee exposure")

    def test_regulatory_risk_pricing_incentive(self):
        """Banks have incentive to minimize perceived regulatory risk for IPO clients."""
        data = load_competitor_research()
        mech = get_mechanism(data, 328)
        self.assertIsNotNone(mech)
        underwriters = mech.get('ipo_underwriter_architecture', {})
        incentive = underwriters.get('regulatory_risk_pricing_incentive', '')
        self.assertTrue(len(incentive) > 20,
                       "Must explain the regulatory risk pricing incentive")

    def test_same_banks_distinct_teams(self):
        """WSJ reported banks forming 'distinct teams' to avoid information sharing."""
        data = load_competitor_research()
        mech = get_mechanism(data, 328)
        self.assertIsNotNone(mech)
        underwriters = mech.get('ipo_underwriter_architecture', {})
        self.assertTrue(underwriters.get('distinct_teams', False),
                       "Must document distinct team arrangements at shared banks")


# =============================================================================
# TEST CLASS 5: Coverage Omission Test (AI Lab Comparison Gap)
# =============================================================================
class TestCoverageOmissionAILabComparison(unittest.TestCase):
    """Test that settlement coverage omits comparable AI lab risk references."""

    def test_cnn_settlement_article_omits_openai(self):
        """CNN settlement article (94 lines) makes zero OpenAI/ChatGPT references."""
        data = load_competitor_research()
        mech = get_mechanism(data, 328)
        self.assertIsNotNone(mech)
        coverage_test = mech.get('coverage_omission_test', {})
        cnn = coverage_test.get('cnn', {})
        self.assertEqual(cnn.get('openai_mentions', -1), 0,
                        "CNN settlement article must have zero OpenAI mentions")

    def test_cnn_settlement_article_omits_anthropic(self):
        """CNN settlement article makes zero Anthropic/Claude references."""
        data = load_competitor_research()
        mech = get_mechanism(data, 328)
        self.assertIsNotNone(mech)
        coverage_test = mech.get('coverage_omission_test', {})
        cnn = coverage_test.get('cnn', {})
        self.assertEqual(cnn.get('anthropic_mentions', -1), 0,
                        "CNN settlement article must have zero Anthropic mentions")

    def test_cnn_settlement_DOES_mention_tiktok_youtube(self):
        """CNN settlement article DOES include TikTok/YouTube comparison."""
        data = load_competitor_research()
        mech = get_mechanism(data, 328)
        self.assertIsNotNone(mech)
        coverage_test = mech.get('coverage_omission_test', {})
        cnn = coverage_test.get('cnn', {})
        self.assertTrue(cnn.get('tiktok_youtube_mentions', 0) > 0,
                       "CNN article DOES mention TikTok/YouTube (proves genre allows comparison)")

    def test_bloomberg_settlement_omits_ai_lab_comparison(self):
        """Bloomberg Tax settlement article omits AI lab regulatory risk comparison."""
        data = load_competitor_research()
        mech = get_mechanism(data, 328)
        self.assertIsNotNone(mech)
        coverage_test = mech.get('coverage_omission_test', {})
        bloomberg = coverage_test.get('bloomberg', {})
        self.assertEqual(bloomberg.get('ai_lab_comparison', -1), 0,
                        "Bloomberg must have zero AI lab regulatory risk comparison")

    def test_ap_wire_omits_ai_lab_comparison(self):
        """AP wire settlement coverage omits AI lab comparison."""
        data = load_competitor_research()
        mech = get_mechanism(data, 328)
        self.assertIsNotNone(mech)
        coverage_test = mech.get('coverage_omission_test', {})
        ap = coverage_test.get('ap', {})
        self.assertEqual(ap.get('ai_lab_comparison', -1), 0,
                        "AP wire must have zero AI lab comparison")

    def test_selective_entity_inclusion_pattern(self):
        """Coverage includes social media rivals but excludes AI lab competitors."""
        data = load_competitor_research()
        mech = get_mechanism(data, 328)
        self.assertIsNotNone(mech)
        coverage_test = mech.get('coverage_omission_test', {})
        pattern = coverage_test.get('selective_entity_inclusion', {})
        included = pattern.get('included_entities', [])
        excluded = pattern.get('excluded_entities', [])
        self.assertTrue(any('TikTok' in str(e) for e in included),
                       "TikTok must be in included entities")
        self.assertTrue(any('OpenAI' in str(e) for e in excluded),
                       "OpenAI must be in excluded entities")
        self.assertTrue(any('Anthropic' in str(e) for e in excluded),
                       "Anthropic must be in excluded entities")


# =============================================================================
# TEST CLASS 6: Publisher Financial Relationships Predicting Omission
# =============================================================================
class TestPublisherFinancialRelationships(unittest.TestCase):
    """Verify publisher financial relationships that predict AI lab comparison omission."""

    def test_cnn_wbd_financial_relationships_documented(self):
        """CNN/WBD financial relationships documented."""
        data = load_competitor_research()
        mech = get_mechanism(data, 328)
        self.assertIsNotNone(mech)
        publisher_finance = mech.get('publisher_financial_relationships', {})
        cnn = publisher_finance.get('cnn_wbd', {})
        self.assertTrue(len(str(cnn)) > 20,
                       "CNN/WBD financial relationships must be documented")

    def test_bloomberg_bank_dependency_documented(self):
        """Bloomberg terminal dependency on underwriter banks documented."""
        data = load_competitor_research()
        mech = get_mechanism(data, 328)
        self.assertIsNotNone(mech)
        publisher_finance = mech.get('publisher_financial_relationships', {})
        bloomberg = publisher_finance.get('bloomberg', {})
        self.assertTrue(bloomberg.get('terminal_dependency_on_underwriter_banks', False),
                       "Bloomberg terminal dependency on IPO underwriter banks must be documented")

    def test_wsj_news_corp_openai_deal(self):
        """WSJ/News Corp $250M/5yr OpenAI deal documented in this mechanism's context."""
        data = load_competitor_research()
        mech = get_mechanism(data, 328)
        self.assertIsNotNone(mech)
        publisher_finance = mech.get('publisher_financial_relationships', {})
        wsj = publisher_finance.get('wsj_news_corp', {})
        openai_deal = wsj.get('openai_content_deal_m', 0)
        self.assertGreaterEqual(openai_deal, 250,
                               "News Corp/OpenAI deal must be >= $250M")

    def test_ft_openai_deal_documented(self):
        """FT/OpenAI content licensing deal documented."""
        data = load_competitor_research()
        mech = get_mechanism(data, 328)
        self.assertIsNotNone(mech)
        publisher_finance = mech.get('publisher_financial_relationships', {})
        ft = publisher_finance.get('financial_times', {})
        self.assertTrue(ft.get('openai_content_deal', False),
                       "FT/OpenAI deal must be documented")


# =============================================================================
# TEST CLASS 7: Confounders
# =============================================================================
class TestConfounders(unittest.TestCase):
    """Verify confounders are honestly documented."""

    def test_genre_confounder_strong(self):
        """Genre confounder (settlement coverage focuses on settling party) rated STRONG."""
        data = load_competitor_research()
        mech = get_mechanism(data, 328)
        self.assertIsNotNone(mech)
        confounders = mech.get('confounders', [])
        genre = [c for c in confounders if 'genre' in str(c).lower()]
        self.assertTrue(len(genre) > 0, "Genre confounder must be documented")
        self.assertEqual(genre[0].get('strength', ''), 'STRONG')

    def test_breaking_news_confounder_strong(self):
        """Breaking news deadline confounder rated STRONG."""
        data = load_competitor_research()
        mech = get_mechanism(data, 328)
        self.assertIsNotNone(mech)
        confounders = mech.get('confounders', [])
        deadline = [c for c in confounders if 'breaking' in str(c).lower() or 'deadline' in str(c).lower()]
        self.assertTrue(len(deadline) > 0, "Breaking news deadline confounder must be documented")
        self.assertEqual(deadline[0].get('strength', ''), 'STRONG')

    def test_counter_confounding_tiktok_youtube_inclusion(self):
        """Counter-confounder: TikTok/YouTube comparison IS included, proving genre allows it."""
        data = load_competitor_research()
        mech = get_mechanism(data, 328)
        self.assertIsNotNone(mech)
        confounders = mech.get('confounders', [])
        counter = [c for c in confounders if 'counter' in str(c).lower()
                   and ('tiktok' in str(c).lower() or 'youtube' in str(c).lower())]
        self.assertTrue(len(counter) > 0,
                       "Counter-confounder re: TikTok/YouTube inclusion must be documented")

    def test_legal_specificity_confounder_moderate(self):
        """Legal specificity confounder (different harm mechanisms) rated MODERATE."""
        data = load_competitor_research()
        mech = get_mechanism(data, 328)
        self.assertIsNotNone(mech)
        confounders = mech.get('confounders', [])
        legal = [c for c in confounders if 'legal' in str(c).lower() or 'specificity' in str(c).lower()]
        self.assertTrue(len(legal) > 0, "Legal specificity confounder must be documented")
        self.assertEqual(legal[0].get('strength', ''), 'MODERATE')

    def test_at_least_five_confounders(self):
        """Mechanism must document at least 5 confounders for analytic rigor."""
        data = load_competitor_research()
        mech = get_mechanism(data, 328)
        self.assertIsNotNone(mech)
        confounders = mech.get('confounders', [])
        self.assertGreaterEqual(len(confounders), 5,
                               "At least 5 confounders required for analytic rigor")


# =============================================================================
# TEST CLASS 8: Cross-References to Existing Mechanisms
# =============================================================================
class TestCrossReferences(unittest.TestCase):
    """Verify cross-references to related existing mechanisms."""

    def test_cross_references_exist(self):
        """Mechanism must have cross-references to related mechanisms."""
        data = load_competitor_research()
        mech = get_mechanism(data, 328)
        self.assertIsNotNone(mech)
        xrefs = mech.get('cross_references', [])
        self.assertGreaterEqual(len(xrefs), 2,
                               "Must have at least 2 cross-references")

    def test_cross_ref_wsj_same_day_bifurcation(self):
        """Cross-references mechanism #326 (WSJ same-day register bifurcation)."""
        data = load_competitor_research()
        mech = get_mechanism(data, 328)
        self.assertIsNotNone(mech)
        xrefs = mech.get('cross_references', [])
        ref_326 = [x for x in xrefs if x.get('mechanism_id') == 326]
        self.assertTrue(len(ref_326) > 0,
                       "Must cross-reference mechanism #326")

    def test_cross_ref_child_safety_litigation(self):
        """Cross-references existing child safety litigation mechanisms."""
        data = load_competitor_research()
        mech = get_mechanism(data, 328)
        self.assertIsNotNone(mech)
        xrefs = mech.get('cross_references', [])
        # Should reference one of the child safety mechanisms
        child_safety_ids = [21, 40, 55]  # Known child safety mechanism IDs
        found = any(x.get('mechanism_id') in child_safety_ids for x in xrefs)
        # Fallback: check for any child-safety cross-reference by name
        if not found:
            found = any('child' in str(x).lower() or 'safety' in str(x).lower() for x in xrefs)
        self.assertTrue(found, "Must cross-reference child safety litigation mechanisms")


# =============================================================================
# TEST CLASS 9: Asymmetry Score
# =============================================================================
class TestAsymmetryScore(unittest.TestCase):
    """Verify asymmetry scoring is calibrated and honest."""

    def test_asymmetry_score_exists(self):
        """Mechanism must have an asymmetry score."""
        data = load_competitor_research()
        mech = get_mechanism(data, 328)
        self.assertIsNotNone(mech)
        score = mech.get('asymmetry_score', None)
        self.assertIsNotNone(score, "Asymmetry score must be present")

    def test_asymmetry_score_moderate_given_strong_confounders(self):
        """Score should be moderate (0.25-0.55) given two STRONG confounders."""
        data = load_competitor_research()
        mech = get_mechanism(data, 328)
        self.assertIsNotNone(mech)
        score = mech.get('asymmetry_score', 0)
        self.assertGreaterEqual(score, 0.25,
                               "Score should be >= 0.25 (counter-confounders elevate)")
        self.assertLessEqual(score, 0.55,
                            "Score should be <= 0.55 (two STRONG confounders temper)")

    def test_score_rationale_includes_confounders(self):
        """Score rationale must reference confounders."""
        data = load_competitor_research()
        mech = get_mechanism(data, 328)
        self.assertIsNotNone(mech)
        rationale = mech.get('score_rationale', '')
        self.assertTrue('confounder' in rationale.lower() or 'genre' in rationale.lower(),
                       "Score rationale must reference confounders")


# =============================================================================
# TEST CLASS 10: Anthropic IPO S-1 Disclosure Relevance
# =============================================================================
class TestAnthropicIPODisclosureRelevance(unittest.TestCase):
    """Test documentation of $17B precedent relevance to Anthropic S-1."""

    def test_s1_disclosure_relevance_documented(self):
        """$17B precedent relevance to Anthropic S-1 disclosure requirements."""
        data = load_competitor_research()
        mech = get_mechanism(data, 328)
        self.assertIsNotNone(mech)
        s1_impact = mech.get('ipo_disclosure_relevance', {})
        self.assertTrue(s1_impact.get('anthropic_s1_material_risk', False),
                       "Must document $17B as material risk for Anthropic S-1")

    def test_anthropic_october_2026_timeline(self):
        """Documents Anthropic's October 2026 IPO timeline proximity."""
        data = load_competitor_research()
        mech = get_mechanism(data, 328)
        self.assertIsNotNone(mech)
        s1_impact = mech.get('ipo_disclosure_relevance', {})
        timeline = s1_impact.get('timeline', '')
        self.assertIn('October', timeline,
                     "Must document October 2026 IPO timeline")

    def test_claude_teen_usage_regulatory_exposure(self):
        """Documents Claude/teen usage as regulatory exposure for Anthropic."""
        data = load_competitor_research()
        mech = get_mechanism(data, 328)
        self.assertIsNotNone(mech)
        s1_impact = mech.get('ipo_disclosure_relevance', {})
        self.assertTrue(s1_impact.get('claude_teen_exposure', False),
                       "Must document Claude teen usage as regulatory exposure")


if __name__ == '__main__':
    unittest.main()
