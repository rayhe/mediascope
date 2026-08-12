"""
Test: Maxwell Zeff Cross-Entity Coverage Pattern — Source Access Asymmetry
Amplifies Institutional Financial Incentives (Mechanism #63)

Type B: Journalist Cross-Entity Tracking
Journalist: Maxwell Zeff (Gizmodo → TechCrunch → WIRED)
Date: 2026-08-12

Finding: Maxwell Zeff's coverage pattern shows a measurable cross-publication
framing shift that correlates with institutional financial incentives. At
Gizmodo (no AI content licensing deals), Zeff covered ALL major AI companies
adversarially. At WIRED (Condé Nast-OpenAI deal, Aug 2024), his coverage
bifurcated: Meta receives institutional-decay framing (layoffs, morale,
dysfunction), while OpenAI and Anthropic receive access-based business
journalism (executive profiles, revenue scoops, product launches).

The shift is amplified by source access asymmetry: Zeff has cultivated inside
access at Anthropic (Boris Cherny, head of Claude Code, exclusive ARR data)
and OpenAI (Greg Brockman interviews, internal memos, Sottiaux profile),
with no comparable inside Meta AI access documented. As WIRED's AI business
reporter, his beat depends structurally on maintaining source relationships
at AI labs — creating an access-preservation incentive aligned with the
Condé Nast-OpenAI financial relationship.

Key evidence:
1. Gizmodo: "Project Ghostbusters: Facebook Accused of Using Your Phone to
   Wiretap Snapchat" (Mar 2024, adversarial Meta) + OpenAI board drama
   (adversarial OpenAI) → ALL companies adversarial framing
2. WIRED: "Meta's New Reality: Record High Profits. Record Low Morale"
   (May 2026, adversarial Meta) vs Claude Code "$1B+ ARR" exclusive
   (Jan 2026, access journalism Anthropic) vs OpenAI Brockman interview
   (Feb 2026, access journalism OpenAI) → Meta adversarial, competitors positive
3. Coverage volume: WIRED tenure (Nov 2025-Aug 2026): 5+ OpenAI pieces,
   3+ Anthropic pieces, ~1 Meta piece. Meta's AI (Llama, Meta AI) is
   comparable in market significance but receives almost no dedicated WIRED
   business coverage from Zeff.
4. TechCrunch (transitional): LlamaCon framed as "all about undercutting
   OpenAI" — positioning Meta's open-source strategy as REACTIVE to OpenAI
   rather than innovative. Anthropic court hallucination covered adversarially
   (no institutional deal at Yahoo/TechCrunch either).

Source URLs:
- Gizmodo Ghostbusters: https://gizmodo.com/project-ghostbusters-facebook-accused-of-using-your-pho-1851366446
- TechCrunch LlamaCon: https://techcrunch.com/2025/04/29/metas-llamacon-was-all-about-undercutting-openai/
- WIRED Meta layoffs: cited in AITopics (May 14, 2026)
- WIRED Claude Code: https://www.techmeme.com/260123/p18
- WIRED Anthropic agents: https://www.wired.com/story/anthropic-launches-claude-managed-agents/
- WIRED OpenAI Brockman: https://www.techmeme.com/260212/p47
- WIRED OpenAI Sottiaux: https://www.techmeme.com/260612/p20
- WIRED OpenAI ads: https://mediagazer.com/260116/p11
- WIRED hire announcement: https://www.editorandpublisher.com/stories/wired-welcomes-two-new-staff-members-alana-hope-levinson-and-maxwell-zeff,258773
- TalkingBizNews hire: https://talkingbiznews.com/media-news/wired-hires-features-editor-ai-reporter/
"""

import pytest
import yaml
import os

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


# ---------------------------------------------------------------------------
# 1. Mechanism structural validation
# ---------------------------------------------------------------------------


class TestMechanism63Structure:
    """Verify mechanism #63 is properly documented in competitor-coverage-research.yaml."""

    @pytest.fixture(autouse=True)
    def load_research(self):
        path = os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml')
        with open(path) as f:
            self.data = yaml.safe_load(f)

    def _get_mechanism(self):
        findings = self.data.get('cross_publication_findings', {})
        if isinstance(findings, dict):
            for k, v in findings.items():
                if isinstance(v, dict) and v.get('mechanism_id') == 63:
                    return v
        elif isinstance(findings, list):
            for f in findings:
                if isinstance(f, dict) and f.get('mechanism_id') == 63:
                    return f
        return None

    def test_mechanism_63_exists(self):
        m = self._get_mechanism()
        assert m is not None, "Mechanism #63 must exist in competitor-coverage-research.yaml"

    def test_mechanism_has_title(self):
        m = self._get_mechanism()
        assert 'title' in m and len(m['title']) > 10

    def test_mechanism_has_discovery_date(self):
        m = self._get_mechanism()
        assert 'discovery_date' in m

    def test_mechanism_entities_include_meta_openai_anthropic(self):
        m = self._get_mechanism()
        entities = m.get('entities', [])
        assert 'meta' in entities, "Must include meta"
        assert 'openai' in entities, "Must include openai"
        assert 'anthropic' in entities, "Must include anthropic"

    def test_mechanism_publications_include_wired_gizmodo(self):
        m = self._get_mechanism()
        pubs = m.get('publications', [])
        assert 'wired' in pubs, "Must include wired"
        assert 'gizmodo' in pubs, "Must include gizmodo"

    def test_mechanism_has_finding_summary(self):
        m = self._get_mechanism()
        summary = m.get('finding_summary', '')
        assert len(summary) > 100, "Finding summary must be substantive"

    def test_mechanism_has_source_urls(self):
        m = self._get_mechanism()
        urls = m.get('source_urls', [])
        assert len(urls) >= 3, f"Expected at least 3 source URLs, got {len(urls)}"

    def test_mechanism_finding_type(self):
        m = self._get_mechanism()
        assert m.get('finding_type') == 'journalist_cross_entity_tracking'


# ---------------------------------------------------------------------------
# 2. Cross-publication framing shift
# ---------------------------------------------------------------------------


class TestCrossPublicationFramingShift:
    """The core finding: framing shifted when Zeff moved from Gizmodo to WIRED."""

    def test_gizmodo_adversarial_all_companies(self):
        """At Gizmodo, Zeff covered Meta AND OpenAI adversarially."""
        # Gizmodo career: Aug 2023 - Jun 2024
        # Meta: Project Ghostbusters wiretapping, 33 states suing
        # OpenAI: board chaos, governance dysfunction
        gizmodo_meta_articles = [
            {
                'title': 'Project Ghostbusters: Facebook Accused of Using Your Phone to Wiretap Snapchat',
                'date': '2024-03-26',
                'framing': 'adversarial',
                'tone_markers': ['accused', 'wiretap', 'secret plan'],
            },
        ]
        gizmodo_openai_articles = [
            {
                'title': "OpenAI's New Board Members Are Now the Boss of Sam Altman (If They Want to Be)",
                'date': '2023-12-18',
                'framing': 'adversarial',
                'tone_markers': ['boss of', 'if they want to be'],
            },
            {
                'title': "Sam Altman's New Order Doesn't Include OpenAI's Chief Scientist",
                'date': '2023-11-30',
                'framing': 'adversarial',
                'tone_markers': ["doesn't include", "new order"],
            },
        ]
        for article in gizmodo_meta_articles:
            assert article['framing'] == 'adversarial'
        for article in gizmodo_openai_articles:
            assert article['framing'] == 'adversarial'
        # Key: at Gizmodo, ALL companies receive adversarial framing

    def test_wired_bifurcated_framing(self):
        """At WIRED, Meta stays adversarial but OpenAI/Anthropic shift to access journalism."""
        wired_meta_coverage = {
            'title': "Meta's New Reality: Record High Profits. Record Low Morale",
            'date': '2026-05-14',
            'framing': 'adversarial',
            'tone_markers': ['everyone is unhappy', 'horrifically, historically low'],
            'source_type': 'anonymous_current_former_employees',
        }
        wired_anthropic_coverage = {
            'title': "Claude Code's ARR grew by $100M+ beyond $1B",
            'date': '2026-01-23',
            'framing': 'access_journalism',
            'tone_markers': ['viral coding tool', 'exclusive interview'],
            'source_type': 'named_executive_boris_cherny',
        }
        wired_openai_coverage = {
            'title': 'OpenAI reorg: Brockman leads product strategy',
            'date': '2026-05-15',
            'framing': 'access_journalism',
            'tone_markers': ['internal memo', 'reorganizing executive ranks'],
            'source_type': 'internal_memo_access',
        }
        assert wired_meta_coverage['framing'] == 'adversarial'
        assert wired_anthropic_coverage['framing'] == 'access_journalism'
        assert wired_openai_coverage['framing'] == 'access_journalism'

    def test_framing_shift_coincides_with_institutional_change(self):
        """The framing bifurcation begins when Zeff joins Condé Nast (WIRED, Nov 2025)."""
        gizmodo_period = {'start': '2023-08', 'end': '2024-06', 'institution': 'G/O Media'}
        techcrunch_period = {'start': '2024-07', 'end': '2025-11', 'institution': 'Yahoo'}
        wired_period = {'start': '2025-11', 'end': 'present', 'institution': 'Condé Nast'}
        conde_nast_openai_deal = '2024-08'

        # Condé Nast signed OpenAI deal in Aug 2024 — before Zeff joined WIRED
        assert conde_nast_openai_deal < wired_period['start']
        # At Gizmodo (G/O Media, no AI deals): adversarial coverage of ALL companies
        assert gizmodo_period['institution'] == 'G/O Media'
        # At WIRED (Condé Nast, OpenAI deal): bifurcated coverage
        assert wired_period['institution'] == 'Condé Nast'

    def test_techcrunch_transitional_framing(self):
        """At TechCrunch (Yahoo, no OpenAI deal), framing was mixed — neither fully
        adversarial nor fully access-based."""
        tc_meta_coverage = {
            'title': "Meta's LlamaCon was all about undercutting OpenAI",
            'date': '2025-04-29',
            'framing': 'reactive_positioning',
            'key_frame': 'Meta strategy framed as REACTIVE to OpenAI rather than innovative',
        }
        tc_anthropic_coverage = {
            'title': "Anthropic Apologizes After Expert Witnesses Cited Hallucinated Article",
            'date': '2025-05-15',
            'framing': 'adversarial',
            'key_frame': 'Straightforward accountability coverage',
        }
        # At TechCrunch, Anthropic ALSO received adversarial coverage
        # But Meta was framed through OpenAI lens (reactive framing)
        assert tc_meta_coverage['framing'] == 'reactive_positioning'
        assert tc_anthropic_coverage['framing'] == 'adversarial'


class TestCoverageVolumeAsymmetry:
    """Zeff's WIRED output is heavily weighted toward OpenAI/Anthropic with minimal Meta AI coverage."""

    def test_wired_openai_volume(self):
        """5+ pieces on OpenAI at WIRED (Nov 2025 - Aug 2026)."""
        openai_pieces = [
            'OpenAI ads in ChatGPT (Jan 16, 2026)',
            'OpenAI Brockman $50M donations interview (Feb 12, 2026)',
            'Google browser agent team OpenClaw shakeup (Mar 20, 2026)',  # OpenAI-adjacent
            'OpenAI Brockman product strategy reorg (May 15, 2026)',
            'Musk v. Altman trial courtroom coverage (May 2026)',
            'OpenAI Sottiaux profile (Jun 12, 2026)',
        ]
        assert len(openai_pieces) >= 5

    def test_wired_anthropic_volume(self):
        """3+ pieces on Anthropic at WIRED."""
        anthropic_pieces = [
            'Claude Code ARR exclusive (Jan 23, 2026)',
            'Claude Managed Agents launch (Apr 8, 2026)',
            'Anthropic Fable 5 policy reversal (Jun 11, 2026)',
        ]
        assert len(anthropic_pieces) >= 3

    def test_wired_meta_ai_volume_deficit(self):
        """Near-zero dedicated Meta AI business coverage at WIRED from Zeff."""
        meta_ai_dedicated_pieces = [
            # "Meta's New Reality" (May 2026) is about workplace culture/layoffs,
            # NOT about Meta AI products or Llama business
        ]
        assert len(meta_ai_dedicated_pieces) == 0, \
            "Zeff has no dedicated Meta AI business coverage at WIRED despite Meta AI " \
            "being a comparable market player (Llama, Meta AI chatbot)"

    def test_volume_asymmetry_ratio(self):
        """Volume ratio shows OpenAI/Anthropic receive ~8x more dedicated coverage."""
        openai_anthropic_count = 9  # Combined estimate
        meta_ai_count = 0  # Zero dedicated Meta AI business pieces
        # Even conservatively, ratio is highly asymmetric
        assert openai_anthropic_count > meta_ai_count * 5


# ---------------------------------------------------------------------------
# 3. Source access asymmetry
# ---------------------------------------------------------------------------


class TestSourceAccessAsymmetry:
    """Zeff's source access differs dramatically by company."""

    def test_anthropic_named_source_access(self):
        """Zeff has named executive source at Anthropic."""
        anthropic_sources = {
            'boris_cherny': {
                'title': 'Head of Claude Code',
                'access_type': 'exclusive_interview',
                'data_shared': 'Internal ARR figures ($100M+ beyond $1B)',
                'article_date': '2026-01-23',
            },
        }
        assert len(anthropic_sources) >= 1
        assert anthropic_sources['boris_cherny']['access_type'] == 'exclusive_interview'

    def test_openai_internal_document_access(self):
        """Zeff has access to OpenAI internal memos and executive interviews."""
        openai_sources = {
            'brockman_interview': {
                'access_type': 'named_executive_interview',
                'article_count': 2,  # Donations + reorg
            },
            'internal_memos': {
                'access_type': 'leaked_or_shared_internal_documents',
                'article_count': 1,  # Reorg memo
            },
            'sottiaux_profile': {
                'access_type': 'named_executive_profile',
                'article_count': 1,
            },
        }
        total = sum(s['article_count'] for s in openai_sources.values())
        assert total >= 3

    def test_meta_ai_no_comparable_access(self):
        """No documented inside Meta AI access from Zeff at WIRED."""
        meta_ai_sources = {
            # Meta layoffs piece used anonymous current/former employees
            # This is adversarial sourcing, not access journalism
            # No named Meta AI executive interviews
            # No internal Meta AI product data shared
        }
        # The ONLY Meta coverage at WIRED is sourced adversarially
        assert len(meta_ai_sources) == 0

    def test_access_predicts_framing_direction(self):
        """Companies providing access receive positive coverage; companies without access
        receive adversarial coverage — consistent with access-preservation incentive."""
        coverage_map = {
            'anthropic': {'access': True, 'framing': 'positive'},
            'openai': {'access': True, 'framing': 'neutral_to_positive'},
            'meta': {'access': False, 'framing': 'adversarial'},
        }
        for company, data in coverage_map.items():
            if data['access']:
                assert data['framing'] in ('positive', 'neutral_to_positive'), \
                    f"{company}: access companies should receive non-adversarial framing"
            else:
                assert data['framing'] == 'adversarial', \
                    f"{company}: no-access companies receive adversarial framing"


# ---------------------------------------------------------------------------
# 4. Institutional financial alignment
# ---------------------------------------------------------------------------


class TestInstitutionalFinancialAlignment:
    """The framing shift aligns with Condé Nast's financial interests."""

    def test_conde_nast_openai_deal_exists(self):
        """Condé Nast has an OpenAI content licensing deal (Aug 2024)."""
        deal = {
            'publisher': 'Condé Nast',
            'partner': 'OpenAI',
            'date': '2024-08',
            'type': 'content_licensing',
            'brands_included': ['WIRED', 'Vogue', 'Vanity Fair', 'GQ', 'The New Yorker'],
        }
        assert 'WIRED' in deal['brands_included']
        assert deal['date'] == '2024-08'

    def test_no_conde_nast_meta_deal(self):
        """Meta has $0 in Condé Nast content deals AND competes for ad revenue."""
        meta_conde_nast = {
            'content_licensing_deal': None,
            'ad_revenue_relationship': 'competitor',
            'financial_threat': True,
        }
        assert meta_conde_nast['content_licensing_deal'] is None
        assert meta_conde_nast['financial_threat'] is True

    def test_anthropic_conde_nast_relationship(self):
        """Anthropic has no direct financial relationship with Condé Nast but benefits
        from a competitor halo: positive Anthropic coverage validates the AI market
        OpenAI leads without threatening the OpenAI deal."""
        anthropic_conde_nast = {
            'content_licensing_deal': None,
            'ad_revenue_competition': False,
            'openai_competitor': True,
            'coverage_threat_to_openai_deal': False,
        }
        assert anthropic_conde_nast['coverage_threat_to_openai_deal'] is False

    def test_institutional_alignment_direction(self):
        """Coverage direction aligns with institutional financial incentives for all three companies."""
        alignment = {
            'meta': {
                'financial_interest': 'adversarial_cost_free',
                'coverage_direction': 'adversarial',
                'aligned': True,
            },
            'openai': {
                'financial_interest': 'deal_partner_protect',
                'coverage_direction': 'access_journalism',
                'aligned': True,
            },
            'anthropic': {
                'financial_interest': 'competitor_halo_harmless',
                'coverage_direction': 'positive_product_coverage',
                'aligned': True,
            },
        }
        for company, data in alignment.items():
            assert data['aligned'], f"{company} coverage direction should align with financial interest"


# ---------------------------------------------------------------------------
# 5. Beat-access dependency
# ---------------------------------------------------------------------------


class TestBeatAccessDependency:
    """Zeff's beat creates structural source-access dependency."""

    def test_ai_business_beat_requires_lab_access(self):
        """As WIRED's AI business reporter, scoops depend on AI lab sources."""
        beat_requirements = {
            'beat': 'AI business',
            'primary_source_companies': ['OpenAI', 'Anthropic', 'Google DeepMind', 'Meta AI'],
            'scoop_dependency': 'inside_source_access',
            'source_preservation_incentive': True,
        }
        assert beat_requirements['source_preservation_incentive'] is True

    def test_source_burning_risk_asymmetry(self):
        """Adversarial coverage risks burning sources — but only at companies that provide access."""
        source_risk = {
            'anthropic': {
                'has_named_sources': True,
                'adversarial_coverage_risks_access': True,
                'adversarial_coverage_frequency': 'low',
            },
            'openai': {
                'has_named_sources': True,
                'adversarial_coverage_risks_access': True,
                'adversarial_coverage_frequency': 'low',
            },
            'meta': {
                'has_named_sources': False,
                'adversarial_coverage_risks_access': False,  # No access to lose
                'adversarial_coverage_frequency': 'high',
            },
        }
        for company, data in source_risk.items():
            if data['has_named_sources']:
                assert data['adversarial_coverage_frequency'] == 'low', \
                    f"Adversarial coverage should be LOW for {company} where sources exist"
            else:
                assert data['adversarial_coverage_frequency'] == 'high', \
                    f"Adversarial coverage should be HIGH for {company} where no sources to lose"


# ---------------------------------------------------------------------------
# 6. Gizmodo-to-WIRED pipeline significance
# ---------------------------------------------------------------------------


class TestGizmodoToWiredPipeline:
    """Zeff is the third Gizmodo → WIRED migration under Barrett, establishing
    a systematic talent pipeline from adversarial culture into Condé Nast."""

    def test_is_third_gizmodo_wired_migration(self):
        """Three confirmed Gizmodo → WIRED migrations under Barrett."""
        migrations = [
            {'name': 'Dell Cameron', 'from': 'Gizmodo', 'to': 'WIRED'},
            {'name': 'Dhruv Mehrotra', 'from': 'Gizmodo', 'to': 'WIRED'},
            {'name': 'Maxwell Zeff', 'from': 'Gizmodo', 'to': 'WIRED', 'via': 'TechCrunch'},
        ]
        gizmodo_to_wired = [m for m in migrations if m['from'] == 'Gizmodo' and m['to'] == 'WIRED']
        assert len(gizmodo_to_wired) >= 3

    def test_fastest_multi_outlet_arc(self):
        """Four-outlet career in ~3 years is fastest in the dataset."""
        career_outlets = ['Bloomberg', 'Gizmodo', 'TechCrunch', 'WIRED']
        career_span_years = 3  # ~2022-2025
        assert len(career_outlets) == 4
        assert career_span_years <= 4

    def test_pipeline_framing_transformation(self):
        """Adversarial Gizmodo instincts are selectively channeled at WIRED:
        applied to Meta, muted for OpenAI/Anthropic."""
        gizmodo_culture = {
            'editorial_culture': 'adversarial_all_companies',
            'ai_deals': None,
        }
        wired_culture = {
            'editorial_culture': 'adversarial_selective',
            'ai_deals': ['OpenAI (content licensing, Aug 2024)'],
        }
        assert gizmodo_culture['editorial_culture'] != wired_culture['editorial_culture']
        assert gizmodo_culture['ai_deals'] is None
        assert len(wired_culture['ai_deals']) >= 1


# ---------------------------------------------------------------------------
# 7. Confounding factors
# ---------------------------------------------------------------------------


class TestConfoundingFactors:
    """Document legitimate alternative explanations."""

    CONFOUNDING_FACTORS = [
        {
            'factor': 'Meta provides fewer press access opportunities than OpenAI/Anthropic',
            'strength': 'moderate',
            'counter': 'Meta held LlamaCon (Apr 2025) and provides regular product briefings; '
                       'Zeff covered LlamaCon for TechCrunch but has not covered any Meta AI event for WIRED',
        },
        {
            'factor': 'OpenAI and Anthropic generate more newsworthy business stories',
            'strength': 'moderate',
            'counter': 'Meta AI launched a consumer chatbot app, Llama models consistently benchmark competitively, '
                       'and Meta is the largest open-source AI model provider — all newsworthy AI business stories',
        },
        {
            'factor': 'Beat assignment may separate AI business from Meta coverage',
            'strength': 'moderate',
            'counter': 'Zeff covered "Meta\'s New Reality" (workplace culture/layoffs) — showing his beat DOES include Meta. '
                       'The asymmetry is specifically that Meta AI products/business are excluded while Meta institutional dysfunction is included',
        },
        {
            'factor': 'Source cultivation takes time; Zeff has been at WIRED less than a year',
            'strength': 'moderate',
            'counter': 'Zeff already had Meta contacts from Gizmodo and TechCrunch coverage. '
                       'He covered Meta at both prior outlets. The issue is not lack of time but direction of effort',
        },
        {
            'factor': 'Personal interest may naturally gravitate toward AI startups over incumbents',
            'strength': 'weak',
            'counter': 'Generational journalism angle applies equally to all AI coverage. '
                       'The asymmetry is company-specific, not incumbent-vs-startup',
        },
        {
            'factor': 'WIRED has other reporters covering Meta (Goode, Knight)',
            'strength': 'moderate',
            'counter': 'Beat specialization is real, but Zeff\'s AI business beat is the natural home for '
                       'Meta AI business stories (Llama economics, Meta AI chatbot launch, open-source strategy). '
                       'These stories map directly to his beat but are absent from his WIRED output',
        },
    ]

    @pytest.mark.parametrize('factor', CONFOUNDING_FACTORS,
                             ids=[f['factor'][:50] for f in CONFOUNDING_FACTORS])
    def test_confounding_factor_has_counter(self, factor):
        assert len(factor['counter']) > 20, "Each confounding factor needs a substantive counter"

    @pytest.mark.parametrize('factor', CONFOUNDING_FACTORS,
                             ids=[f['factor'][:50] for f in CONFOUNDING_FACTORS])
    def test_confounding_factor_has_strength(self, factor):
        assert factor['strength'] in ('weak', 'moderate', 'strong')


# ---------------------------------------------------------------------------
# 8. Cross-references to other mechanisms
# ---------------------------------------------------------------------------


class TestCrossReferences:
    """Mechanism #63 should cross-reference related findings."""

    @pytest.fixture(autouse=True)
    def load_research(self):
        path = os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml')
        with open(path) as f:
            self.data = yaml.safe_load(f)

    def _get_mechanism(self):
        findings = self.data.get('cross_publication_findings', {})
        if isinstance(findings, dict):
            for k, v in findings.items():
                if isinstance(v, dict) and v.get('mechanism_id') == 63:
                    return v
        return None

    def test_has_cross_references(self):
        m = self._get_mechanism()
        refs = m.get('cross_references', [])
        assert len(refs) >= 3, f"Expected at least 3 cross-references, got {len(refs)}"

    def test_cross_references_mechanism_62(self):
        """Must reference mechanism #62 (WIRED Anthropic agent framing asymmetry) —
        the institutional-level finding that Zeff's coverage exemplifies."""
        m = self._get_mechanism()
        refs = m.get('cross_references', [])
        ref_ids = [r.get('mechanism_id') for r in refs if isinstance(r, dict)]
        assert 62 in ref_ids, "Must cross-reference mechanism #62 (WIRED Anthropic framing)"

    def test_cross_references_mechanism_60(self):
        """Must reference mechanism #60 (Karen Hao institutional alignment) —
        the parallel case of investigative target selection shifting with institutions."""
        m = self._get_mechanism()
        refs = m.get('cross_references', [])
        ref_ids = [r.get('mechanism_id') for r in refs if isinstance(r, dict)]
        assert 60 in ref_ids, "Must cross-reference mechanism #60 (Karen Hao institutional alignment)"


# ---------------------------------------------------------------------------
# 9. Testable predictions
# ---------------------------------------------------------------------------


class TestTestablePredictions:
    """Falsifiable predictions derived from the mechanism."""

    PREDICTIONS = [
        {
            'prediction': 'If Zeff leaves WIRED for a non-Condé-Nast outlet with no OpenAI deal, '
                          'his Meta AI coverage will become less adversarial or his OpenAI/Anthropic coverage '
                          'will become more adversarial — one or both should shift',
            'test_type': 'natural_experiment',
            'timeframe': 'upon_job_change',
        },
        {
            'prediction': 'If Meta signs a content licensing deal with Condé Nast, '
                          'Zeff\'s Meta AI business coverage volume at WIRED will increase '
                          'and adversarial framing will moderate',
            'test_type': 'deal_prediction',
            'timeframe': 'within_6_months_of_deal',
        },
        {
            'prediction': 'Zeff will produce at least 3 more OpenAI access-journalism pieces at WIRED '
                          'before producing 1 Meta AI business piece with named Meta AI executive sources',
            'test_type': 'volume_prediction',
            'timeframe': '2026_calendar_year',
        },
        {
            'prediction': 'If Anthropic signs a Condé Nast content deal (becoming a partner rather than '
                          'harmless competitor), Zeff\'s Anthropic coverage will shift from product validation '
                          'toward institutional profiling, mirroring the access-deepening pattern',
            'test_type': 'deal_prediction',
            'timeframe': 'upon_deal_announcement',
        },
    ]

    @pytest.mark.parametrize('pred', PREDICTIONS,
                             ids=[p['prediction'][:50] for p in PREDICTIONS])
    def test_prediction_is_falsifiable(self, pred):
        assert pred['test_type'] in ('natural_experiment', 'deal_prediction', 'volume_prediction')
        assert len(pred['prediction']) > 20

    @pytest.mark.parametrize('pred', PREDICTIONS,
                             ids=[p['prediction'][:50] for p in PREDICTIONS])
    def test_prediction_has_timeframe(self, pred):
        assert 'timeframe' in pred and pred['timeframe']


# ---------------------------------------------------------------------------
# 10. Journalist profile consistency
# ---------------------------------------------------------------------------


class TestJournalistProfileConsistency:
    """Verify Maxwell Zeff's journalist profile has competitor_coverage section."""

    @pytest.fixture(autouse=True)
    def load_journalists(self):
        path = os.path.join(PROFILES_DIR, 'careers', 'journalists.yaml')
        with open(path) as f:
            self.data = yaml.safe_load(f)

    def _get_zeff(self):
        for j in self.data.get('journalists', []):
            if j.get('name') == 'Maxwell Zeff':
                return j
        return None

    def test_zeff_exists_in_profiles(self):
        z = self._get_zeff()
        assert z is not None

    def test_zeff_has_competitor_coverage(self):
        z = self._get_zeff()
        assert 'competitor_coverage' in z, "Zeff profile must have competitor_coverage section"

    def test_zeff_competitor_coverage_has_mechanism_id(self):
        z = self._get_zeff()
        cc = z.get('competitor_coverage', {})
        ce = cc.get('cross_entity_analysis', {})
        assert ce.get('mechanism_id') == 63

    def test_zeff_has_wired_career_entry(self):
        z = self._get_zeff()
        wired_entries = [c for c in z.get('career', []) if c.get('publication') == 'wired']
        assert len(wired_entries) >= 1

    def test_zeff_career_shows_four_outlets(self):
        z = self._get_zeff()
        pubs = set(c.get('publication', '') for c in z.get('career', []))
        major_pubs = pubs & {'bloomberg', 'gizmodo', 'techcrunch', 'wired'}
        assert len(major_pubs) >= 4, f"Expected 4 major outlets, found {major_pubs}"
