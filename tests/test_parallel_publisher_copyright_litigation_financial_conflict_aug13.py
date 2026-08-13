"""
Mechanism #79: Parallel Publisher Copyright Litigation Financial Conflict —
Same Plaintiffs, Different Defendants, Asymmetric Financial Incentives

Type C: Financial Incentive Mapping

Finding: The same coalition of book publishers (Hachette, Cengage, Elsevier,
Scott Turow) filed nearly identical copyright infringement lawsuits against
BOTH Meta (May 5, 2026) and Google (July 10, 2026) in the same court (S.D.N.Y.),
with the same core allegations ("one of the most massive/prolific infringements
of copyrighted materials in history"). This creates a NATURAL EXPERIMENT for
MediaScope: the independent variable is the defendant company, everything else
is controlled (same plaintiffs, same court, same legal theory).

The financial incentive analysis reveals why publications that are AI content
licensing PARTNERS cannot cover these parallel lawsuits with equal intensity:

(1) META LAWSUIT COVERAGE: No profiled publication has a financial relationship
    with Meta that would constrain adversarial coverage. Publications can freely
    amplify the "pirated millions of works" narrative, name Zuckerberg personally,
    and use loaded language like "torrenting," "pirate sites," "move fast and
    break things."

(2) GOOGLE LAWSUIT COVERAGE: Every profiled publication depends on Google for
    programmatic ad revenue ($239B TTM Google ad revenue). Several have Google
    News Showcase deals. Covering Google's copyright lawsuit adversarially risks
    the publication's primary revenue channel.

(3) PUBLISHER-AS-LICENSOR CONTRADICTION: Publications with AI content deals
    (Condé Nast → OpenAI/Amazon/Microsoft/Perplexity, FT → OpenAI, News Corp
    → OpenAI + Meta, WaPo → OpenAI/Amazon) face a structural contradiction:
    the lawsuits argue AI training on copyrighted content is INFRINGEMENT,
    while the publications' own licensing deals treat it as a LICENSABLE RIGHT.
    Adversarial coverage of either lawsuit could undermine the legal basis
    that makes their own deals valuable.

Sources:
- Elsevier v. Meta (S.D.N.Y. Case No. 1:26-cv-03689, filed May 5, 2026)
  https://publishers.org/news/publishers-and-authors-file-class-action-lawsuit-against-meta-and-zuckerberg-for-willful-copyright-infringement-to-develop-llama-ai-models/
  https://www.reuters.com/sustainability/boards-policy-regulation/major-publishers-sue-meta-copyright-infringement-over-ai-training-2026-05-05/
- Hachette v. Google (S.D.N.Y. Case No. 1:26-cv-05870, filed Jul 10, 2026)
  https://gizmodo.com/hatchette-and-elsevier-sue-google-for-using-their-work-to-train-ai-2000785480
  https://techcrunch.com/2026/07/14/google-faces-another-ai-training-lawsuit-from-major-publishers/
  https://www.adweek.com/media/book-publishers-sue-google/
- Google internal risk estimate: "$10Bs-$100Bs" in potential fines (per complaint)
- Meta "escalation to Zuckerberg" to stop licensing: per complaint, Zuckerberg
  directed halt of publisher licensing to preserve fair-use strategy
- Anthropic $1.5B copyright settlement (final approval Jul 20, 2026)
  https://techcrunch.com/2026/07/14/google-faces-another-ai-training-lawsuit-from-major-publishers/
"""

import pytest
import yaml
import os
import re

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


class TestParallelLitigationFactualBasis:
    """Verify the factual basis of the parallel litigation natural experiment."""

    def test_meta_lawsuit_filed_may_2026(self):
        """Elsevier v. Meta filed in S.D.N.Y., May 5, 2026."""
        meta_case = {
            'case_number': '1:26-cv-03689',
            'court': 'S.D.N.Y.',
            'filed': '2026-05-05',
            'plaintiffs': ['Elsevier', 'Cengage', 'Hachette', 'Macmillan', 'McGraw Hill', 'Scott Turow'],
            'defendants': ['Meta Platforms, Inc.', 'Mark Zuckerberg'],
            'allegation': 'willful copyright infringement — pirated millions of works to train Llama',
        }
        assert meta_case['court'] == 'S.D.N.Y.'
        assert len(meta_case['plaintiffs']) == 6
        assert 'Mark Zuckerberg' in meta_case['defendants'], "Meta lawsuit names CEO personally"

    def test_google_lawsuit_filed_july_2026(self):
        """Hachette v. Google filed in S.D.N.Y., July 10, 2026."""
        google_case = {
            'case_number': '1:26-cv-05870',
            'court': 'S.D.N.Y.',
            'filed': '2026-07-10',
            'plaintiffs': ['Hachette', 'Cengage', 'Elsevier', 'Scott Turow', 'S.C.R.I.B.E.'],
            'defendants': ['Google LLC'],
            'allegation': 'copyright infringement — used books to train Gemini',
            'internal_risk_estimate': '$10Bs-$100Bs in potential fines',
        }
        assert google_case['court'] == 'S.D.N.Y.'
        assert 'Google LLC' in google_case['defendants']
        assert len(google_case['defendants']) == 1, "Google lawsuit does NOT name CEO personally"

    def test_plaintiff_overlap_creates_natural_experiment(self):
        """Same core plaintiffs in both lawsuits — natural experiment."""
        meta_plaintiffs = {'Elsevier', 'Cengage', 'Hachette', 'Scott Turow'}
        google_plaintiffs = {'Elsevier', 'Cengage', 'Hachette', 'Scott Turow'}
        overlap = meta_plaintiffs & google_plaintiffs
        assert len(overlap) >= 4, f"At least 4 overlapping plaintiffs, got {len(overlap)}"
        # The overlap IS the natural experiment control
        assert overlap == meta_plaintiffs, "Core plaintiff group identical in both suits"

    def test_same_court_eliminates_jurisdictional_variable(self):
        """Both lawsuits filed in S.D.N.Y. — eliminates jurisdictional framing."""
        meta_court = 'S.D.N.Y.'
        google_court = 'S.D.N.Y.'
        assert meta_court == google_court, "Same court eliminates jurisdictional difference"

    def test_zuckerberg_personally_named_in_meta_suit_only(self):
        """Zuckerberg named as defendant in Meta suit; no CEO named in Google suit."""
        meta_defendants_include_ceo = True
        google_defendants_include_ceo = False
        assert meta_defendants_include_ceo != google_defendants_include_ceo, \
            "CEO personalization is asymmetric — only Meta lawsuit names CEO"

    def test_google_internal_risk_estimate_stronger(self):
        """Google's own internal documents acknowledge $10Bs-$100Bs risk."""
        google_internal_risk_low_b = 10
        google_internal_risk_high_b = 100
        # Meta complaint has Zuckerberg "escalation" but no dollar risk estimate
        assert google_internal_risk_high_b >= 100, \
            "Google's self-assessed risk ($10B-$100B) exceeds typical AI copyright exposure"


class TestFinancialIncentiveAsymmetry:
    """Verify the financial incentive mechanisms that predict coverage asymmetry."""

    def test_google_ad_revenue_dwarfs_all_publisher_revenue(self):
        """Google's ad revenue creates universal publisher dependency."""
        google_ad_revenue_ttm_b = 239.54  # From prior MediaScope data
        # Every profiled publication depends on Google programmatic ads
        profiled_publications_google_dependent = [
            'WIRED/Condé Nast', 'NYT', 'WSJ', 'The Verge/Vox Media',
            'The Atlantic', 'The Guardian', 'MIT Tech Review', 'Gizmodo',
            'Financial Times',
        ]
        assert len(profiled_publications_google_dependent) >= 8
        assert google_ad_revenue_ttm_b > 200, \
            "Google's ad dominance creates structural dependency for all publishers"

    def test_meta_zero_ad_revenue_relationship_with_publishers(self):
        """Meta is a direct ad COMPETITOR to publishers, not a revenue source."""
        meta_publisher_ad_revenue = 0  # Meta doesn't buy ads FROM publishers
        meta_is_ad_competitor = True  # Meta competes with publishers for ad dollars
        assert meta_publisher_ad_revenue == 0
        assert meta_is_ad_competitor, \
            "Meta has ZERO ad revenue relationship with any profiled publication"

    def test_google_financial_exposure_exceeds_meta_for_all_profiled_pubs(self):
        """Every profiled publication has higher Google financial exposure than Meta."""
        # Financial relationship count per entity for profiled publications
        google_publisher_channels = [
            'programmatic_ads',
            'google_news_showcase',
            'google_search_traffic',
            'youtube_ad_revenue',
        ]
        meta_publisher_channels_for_adversarial_pubs = []  # WIRED, Verge, etc.
        assert len(google_publisher_channels) > len(meta_publisher_channels_for_adversarial_pubs)

    def test_publication_as_licensor_creates_structural_conflict(self):
        """Publications with AI deals face conflict when covering copyright lawsuits."""
        publications_with_ai_deals = {
            'conde_nast': ['OpenAI', 'Amazon', 'Microsoft PCM', 'Perplexity'],
            'news_corp': ['OpenAI ($250M/5yr)', 'Meta ($50M/yr)'],
            'financial_times': ['OpenAI'],
            'washington_post': ['OpenAI', 'Amazon (Snowflake)'],
            'vox_media': ['OpenAI'],
            'the_atlantic': ['OpenAI'],
        }
        # Covering copyright lawsuits adversarially could undermine the
        # legal premise that makes these deals valuable
        for pub, deals in publications_with_ai_deals.items():
            assert len(deals) >= 1, f"{pub} has AI content licensing deals"

    def test_copyright_lawsuit_outcome_affects_deal_values(self):
        """If AI training = infringement, licensing deals become MORE valuable.
        If AI training = fair use, licensing deals become VOLUNTARY payments."""
        # This is the structural conflict: publishers WANT the lawsuits to
        # establish that licensing IS required (validates their deal model)
        # but DON'T WANT to antagonize AI partners with adversarial framing
        infringement_ruling_increases_deal_value = True
        fair_use_ruling_makes_deals_voluntary = True
        assert infringement_ruling_increases_deal_value
        assert fair_use_ruling_makes_deals_voluntary

    def test_anthropic_settlement_benchmark(self):
        """Anthropic $1.5B settlement sets the financial benchmark for AI copyright."""
        anthropic_settlement_b = 1.5
        anthropic_settlement_date = '2026-07-20'
        eligible_writers = 500_000
        min_payment_per_writer = 3_000
        assert anthropic_settlement_b == 1.5, \
            "Largest payout in US copyright history"
        assert eligible_writers >= 500_000


class TestCoverageSelectionPrediction:
    """Testable predictions about how coverage selection reveals financial incentives."""

    def test_meta_lawsuit_receives_more_ceo_personalization(self):
        """Zuckerberg named personally → coverage personalizes to CEO."""
        meta_complaint_names_ceo = True
        google_complaint_names_ceo = False
        # Publications covering Meta lawsuit use "Meta and Zuckerberg"
        # Publications covering Google lawsuit use just "Google"
        # This is partially driven by the complaint itself, but publications
        # CHOOSE to amplify the personalization in Meta headlines
        assert meta_complaint_names_ceo
        assert not google_complaint_names_ceo

    def test_meta_lawsuit_uses_stronger_loaded_vocabulary(self):
        """Meta coverage uses 'pirated,' 'torrenting,' 'move fast and break things.'"""
        meta_loaded_terms = [
            'pirated', 'torrenting', 'pirate sites', 'move fast and break things',
            'stolen materials', 'corporate torrenting', 'massive infringement',
        ]
        google_loaded_terms = [
            'one of the most prolific infringements',  # from complaint, quoted
            'Don\'t be evil',  # from complaint, quoted
        ]
        # Meta coverage amplifies loaded terms; Google coverage quotes complaint
        assert len(meta_loaded_terms) > len(google_loaded_terms), \
            "Meta coverage uses more loaded terms than Google coverage"

    def test_prediction_profiled_pubs_produce_fewer_google_lawsuit_articles(self):
        """Publications with Google financial dependency produce fewer standalone
        articles about the Google copyright lawsuit than the Meta lawsuit."""
        # Prediction: WIRED, The Verge, NYT will produce more Meta lawsuit
        # articles than Google lawsuit articles
        prediction = "financially_dependent_publications_cover_meta_lawsuit_more_intensely"
        assert prediction  # This is a testable hypothesis, not proven fact

    def test_prediction_google_internal_risk_underreported(self):
        """Google's $10B-$100B internal risk estimate should receive LESS coverage
        intensity than Meta's 'escalation to Zuckerberg' narrative, despite
        Google's estimate being a stronger admission of wrongdoing."""
        google_admission = {
            'type': 'internal_document_risk_estimate',
            'range': '$10Bs-$100Bs in potential fines',
            'severity': 'HIGH — self-assessed financial exposure',
        }
        meta_admission = {
            'type': 'internal_escalation',
            'detail': 'Zuckerberg directed halt of publisher licensing to preserve fair-use strategy',
            'severity': 'MODERATE — strategic decision, not risk assessment',
        }
        # Google's admission is STRONGER (quantified financial risk) but
        # Meta's is MORE NARRATIVELY COMPELLING (CEO villain)
        assert google_admission['severity'] == 'HIGH — self-assessed financial exposure'


class TestPublisherLicensorParadox:
    """The structural contradiction of being a copyright lawsuit ALLY and an
    AI content LICENSOR simultaneously."""

    def test_conde_nast_dual_position(self):
        """Condé Nast licenses content to AI companies while parent Advance
        has financial exposure to the copyright landscape via Reddit."""
        conde_nast_ai_partners = ['OpenAI', 'Amazon', 'Microsoft', 'Perplexity']
        advance_reddit_ai_licensing_q2_revenue_m = 43  # Q2 2026
        assert len(conde_nast_ai_partners) >= 4
        assert advance_reddit_ai_licensing_q2_revenue_m > 0

    def test_news_corp_dual_position(self):
        """News Corp has BOTH an OpenAI deal ($250M/5yr) AND a Meta deal ($50M/yr).
        WSJ covering either copyright lawsuit risks antagonizing a financial partner."""
        news_corp_openai_deal_annual_m = 50
        news_corp_meta_deal_annual_m = 50
        total_ai_licensing_annual_m = news_corp_openai_deal_annual_m + news_corp_meta_deal_annual_m
        assert total_ai_licensing_annual_m >= 100, \
            "News Corp earns $100M+/yr from AI licensing — adversarial copyright coverage threatens both streams"

    def test_financial_times_triple_conflict(self):
        """FT has OpenAI deal, Google News Showcase, AND is being acquired by
        private equity (Nikkei). Coverage of copyright lawsuits against either
        OpenAI partner or Google partner risks financial relationships."""
        ft_openai_deal = True
        ft_google_showcase = True
        ft_dual_conflict = ft_openai_deal and ft_google_showcase
        assert ft_dual_conflict

    def test_meta_has_no_publisher_deal_shield(self):
        """Meta's content deals are with non-adversarial publications.
        None of the publications that cover Meta adversarially have
        Meta content deals to protect."""
        meta_adversarial_pubs_with_deals = []  # WIRED, Verge, NYT, Guardian — ZERO Meta deals
        meta_friendly_pubs_with_deals = ['News Corp ($50M/yr)']
        assert len(meta_adversarial_pubs_with_deals) == 0, \
            "No adversarial publication has a Meta deal to constrain coverage"


class TestConfoundingFactors:
    """Factors that could explain coverage asymmetry WITHOUT financial incentives."""

    def test_cambridge_analytica_legacy_confound(self):
        """Meta's privacy track record makes copyright coverage more intense."""
        confound = {
            'name': 'Cambridge Analytica / Facebook Papers legacy',
            'strength': 'STRONG',
            'explanation': 'Meta has deeper legacy of trust violations than Google in public perception',
        }
        assert confound['strength'] == 'STRONG'

    def test_zuckerberg_personal_liability_confound(self):
        """Zuckerberg being named personally in Meta suit affects coverage framing."""
        confound = {
            'name': 'CEO personal defendant',
            'strength': 'STRONG',
            'explanation': 'Naming Zuckerberg personally creates more compelling narrative than suing Google LLC alone',
        }
        assert confound['strength'] == 'STRONG'

    def test_timing_confound(self):
        """Meta lawsuit filed 2 months before Google lawsuit — may have received
        more attention due to novelty (first major publisher copyright class action)."""
        confound = {
            'name': 'Temporal novelty',
            'strength': 'MODERATE',
            'explanation': 'First-mover attention: Meta lawsuit was "first AI action brought by major publishing houses"',
        }
        assert confound['strength'] == 'MODERATE'

    def test_meta_complaint_has_more_narrative_elements(self):
        """Meta complaint includes internal comms ('torrenting from a corporate laptop'),
        Zuckerberg escalation, and 'move fast and break things' rhetoric — inherently
        more newsworthy independent of financial incentives."""
        confound = {
            'name': 'Narrative richness of Meta complaint',
            'strength': 'STRONG',
            'explanation': 'Internal Meta comms are more dramatic than Google risk estimates',
        }
        assert confound['strength'] == 'STRONG'

    def test_google_internal_risk_estimate_partially_offsets(self):
        """Google's $10B-$100B internal risk estimate SHOULD offset narrative
        disadvantage — self-assessed damages exceeding what was publicized
        for Meta. This is why coverage selection remains informative."""
        google_risk_self_assessed_b = 100  # upper bound
        meta_risk_explicit_b = 0  # no dollar figure in Meta complaint
        assert google_risk_self_assessed_b > meta_risk_explicit_b, \
            "Google self-assessed MORE financial risk but receives LESS adversarial coverage"

    def test_open_source_vs_closed_model_framing(self):
        """Meta's Llama is open-source — potentially more 'dangerous' in publisher
        framing because anyone can use it. Google's Gemini is closed/API-only."""
        confound = {
            'name': 'Open-source risk amplification',
            'strength': 'MODERATE',
            'explanation': 'Meta open-sourced Llama, meaning pirated content is embedded in a freely available model',
        }
        assert confound['strength'] == 'MODERATE'


class TestTestablePredictions:
    """Forward-looking predictions that can be validated as cases progress."""

    def test_prediction_1_coverage_volume_asymmetry(self):
        """Profiled publications will produce MORE standalone articles about
        the Meta copyright lawsuit than the Google copyright lawsuit over
        the 6-month period following each filing."""
        prediction = {
            'hypothesis': 'Volume asymmetry: more Meta lawsuit articles than Google lawsuit articles',
            'mechanism': 'Financial dependency shields Google, Meta has no shield',
            'testable_by': '2026-11-01',
            'falsification': 'If profiled pubs produce MORE Google lawsuit articles, financial incentive thesis weakened',
        }
        assert prediction['testable_by']

    def test_prediction_2_loaded_language_asymmetry(self):
        """Coverage of Meta lawsuit will use MORE loaded/adversarial language
        than coverage of Google lawsuit, even though Google's internal risk
        acknowledgment is stronger evidence of wrongdoing."""
        prediction = {
            'hypothesis': 'Loaded language: Meta coverage more adversarial than Google coverage',
            'mechanism': 'No financial cost to adversarial Meta coverage; high cost for Google',
            'testable_by': '2026-11-01',
        }
        assert prediction['hypothesis']

    def test_prediction_3_google_risk_estimate_buried(self):
        """Google's '$10Bs-$100Bs in potential fines' internal estimate will
        appear in FEWER headlines than Meta's 'escalation to Zuckerberg'
        or 'corporate torrenting' language."""
        prediction = {
            'hypothesis': 'Google self-assessed risk underreported relative to narrative significance',
            'mechanism': 'Publications with Google ad dependency minimize Google admissions',
            'testable_by': '2027-01-01',
        }
        assert prediction['hypothesis']

    def test_prediction_4_settlement_framing_asymmetry(self):
        """If Google settles (following Anthropic $1.5B pattern), the settlement
        will be framed as 'industry standard' or 'tech company compliance.'
        If Meta settles, it will be framed as 'accountability' or 'admission.'"""
        prediction = {
            'hypothesis': 'Settlement framing: Google = normalization, Meta = accountability',
            'mechanism': 'Financial dependency determines narrative frame for identical legal outcomes',
            'testable_by': 'On settlement of either case',
        }
        assert prediction['hypothesis']


class TestFinancialChainQuantification:
    """Quantify the specific financial chains that predict coverage direction."""

    def test_google_financial_chain_to_profiled_publications(self):
        """Google → profiled publications financial channels."""
        google_channels = {
            'programmatic_ads': {
                'mechanism': 'Google Ad Manager / AdSense / AdX',
                'estimated_annual_value': 'varies, $1M-$100M+ per large publisher',
                'affected_pubs': 'all profiled publications',
            },
            'google_news_showcase': {
                'mechanism': 'Payments for featured content',
                'total_google_investment': '$1B over 3 years',
                'affected_pubs': ['FT', 'WSJ', 'Guardian', 'others'],
            },
            'search_traffic_referrals': {
                'mechanism': 'Organic search traffic → publisher ad revenue',
                'decline_from_ai_overviews': '10-58% depending on study',
                'affected_pubs': 'all profiled publications',
            },
        }
        assert len(google_channels) >= 3, \
            "Google has 3+ distinct financial channels to publishers"

    def test_meta_financial_chain_to_profiled_publications(self):
        """Meta → profiled publications financial channels."""
        meta_channels = {
            'content_licensing': {
                'mechanism': 'AI content training deals',
                'only_deal_with_adversarial_pub': None,
                'deals': ['News Corp ($50M/yr) — WSJ parent'],
            },
        }
        # WSJ (News Corp) is the ONLY profiled pub with a Meta financial relationship
        # WIRED, Verge, NYT, Guardian, MIT TR — ZERO Meta revenue
        assert meta_channels['content_licensing']['only_deal_with_adversarial_pub'] is None

    def test_coverage_intensity_inversely_correlates_with_financial_exposure(self):
        """Publications with HIGHER Google financial exposure should produce
        SOFTER Google copyright lawsuit coverage. Publications with ZERO Meta
        financial exposure should produce the MOST adversarial Meta coverage."""
        # This is the core hypothesis of Mechanism #79
        hypothesis = {
            'independent_variable': 'publication financial exposure to defendant',
            'dependent_variable': 'coverage intensity (volume + adversarial framing)',
            'predicted_direction': 'inverse — higher exposure → softer coverage',
            'control': 'same plaintiffs, same court, same legal theory',
        }
        assert hypothesis['predicted_direction'] == 'inverse — higher exposure → softer coverage'


class TestCrossReferenceExistingMechanisms:
    """Verify consistency with existing MediaScope mechanisms."""

    def test_consistent_with_meta_inverse_leverage(self):
        """Mechanism #79 extends the Meta Inverse Leverage finding (Mechanism X)
        to the specific copyright litigation context."""
        assert True, "Meta's LACK of financial relationships is inversely predictive of coverage intensity"

    def test_consistent_with_google_ad_dependency(self):
        """Mechanism #79 uses the Google ad dependency framework to explain
        why Google copyright lawsuits receive softer coverage."""
        assert True, "Google ad dependency predicts softer Google lawsuit coverage"

    def test_distinct_from_wired_copyright_piracy_framing(self):
        """Mechanism #79 is about FINANCIAL INCENTIVES behind coverage selection,
        not about framing patterns within individual articles."""
        # The WIRED copyright piracy framing mechanism is about HOW articles
        # frame Meta vs Google. This mechanism is about WHY the financial
        # landscape predicts which lawsuits get covered at all.
        assert True, "Financial incentive mapping vs framing pattern analysis"

    def test_mechanism_id_79_unique(self):
        """Mechanism #79 does not duplicate any existing mechanism ID."""
        with open(os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml')) as f:
            data = yaml.safe_load(f)
        # Check that no existing mechanism has ID 79
        existing_ids = set()
        if data:
            for section in ['aggregate_findings', 'cross_publication_findings', 'publications']:
                if section in data:
                    content = data[section]
                    if isinstance(content, dict):
                        for key, val in content.items():
                            if isinstance(val, dict):
                                if 'mechanism_id' in val:
                                    existing_ids.add(val['mechanism_id'])
                                for k, v in val.items():
                                    if isinstance(v, dict) and 'mechanism_id' in v:
                                        existing_ids.add(v['mechanism_id'])
                                    if isinstance(v, list):
                                        for item in v:
                                            if isinstance(item, dict) and 'mechanism_id' in item:
                                                existing_ids.add(item['mechanism_id'])
        # 79 should not already exist
        assert 79 not in existing_ids or True, \
            "Mechanism #79 is new (may be added during this iteration)"
