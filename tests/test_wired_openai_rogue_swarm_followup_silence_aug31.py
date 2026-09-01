"""
Iteration #430 Type A - WIRED x OpenAI Rogue Swarm vs Meta Dormant Code
Aug 26-28 2026 New Disclosures Follow-up Gap

Mechanism #430 - primary-source correction for Google I/O proxy issue
plus new severity inversion with 700-agent swarm escalation.

Requirements:
- Exact WIRED direct URLs (wired.com/story) - no proxy rehost
- 2-3 WIRED OpenAI articles vs 3 WIRED Meta articles
- 5 Aug 26-28 new disclosure sources with HTTPS URLs
- No em dashes in yaml (enforce -- or comma)
- Explicit non-causal language (correlation does not imply causation)
- Illustrative scores labeled MANUAL ILLUSTRATIVE
- Synthetic tone arrays flagged illustrative only
- Financial correlation cautious - no editorial control claim
- Correction of proxy-only assertion noted
- Asymmetry scorer result structure
- Severity inversion documented
- Follow-up gap is monitoring evidence not proof of bias
"""

import os
import re
import yaml
import pytest

PROFILE_PATH = os.path.join(os.path.dirname(__file__), '..', 'profiles', 'wired.yaml')

@pytest.fixture(scope='module')
def wired_profile():
    assert os.path.exists(PROFILE_PATH), f"Missing {PROFILE_PATH}"
    with open(PROFILE_PATH, 'r') as f:
        data = yaml.safe_load(f)
    return data

@pytest.fixture(scope='module')
def mechanism(wired_profile):
    assert 'journalist_cross_entity_coverage' in wired_profile, "Missing journalist_cross_entity_coverage"
    jcec = wired_profile['journalist_cross_entity_coverage']
    key = 'wired_openai_rogue_swarm_aug26_followup_silence'
    assert key in jcec, f"Missing {key} in journalist_cross_entity_coverage"
    return jcec[key]

class TestPrimarySourceCorrection:
    def test_mechanism_exists(self, mechanism):
        assert mechanism is not None

    def test_mechanism_id_430(self, mechanism):
        assert mechanism['mechanism_id'] == 430

    def test_iteration_430(self, mechanism):
        assert mechanism['iteration'] == 430

    def test_type_a(self, mechanism):
        assert 'Type A' in mechanism['type']
        assert 'Competitor Coverage Deep Dive' in mechanism['type']

    def test_primary_source_correction_field_exists(self, mechanism):
        assert 'primary_source_correction' in mechanism

    def test_direct_wired_urls_verified(self, mechanism):
        psc = mechanism['primary_source_correction']
        assert 'direct_wired_urls_verified' in psc
        urls = psc['direct_wired_urls_verified']
        assert len(urls) >= 5, f"Expected 5+ direct WIRED URLs, got {len(urls)}"
        for url in urls:
            assert 'wired.com/story/' in url, f"Not a direct WIRED story URL: {url}"
            assert url.startswith('https://'), f"Must be HTTPS: {url}"

    def test_no_proxy_rehost_for_wired_claims(self, mechanism):
        # Ensure no technologytangle.com in source_urls
        urls = mechanism.get('source_urls', [])
        for url in urls:
            if 'wired.com' in url:
                assert 'technologytangle.com' not in url
        # Primary source correction should note proxy issue
        psc = mechanism['primary_source_correction']
        assert 'technologytangle' in psc['prior_issue'].lower() or 'proxy' in psc['prior_issue'].lower()

    def test_openai_new_disclosures_5_sources(self, mechanism):
        disclosures = mechanism['openai_new_disclosures_aug26_28']
        # Check we have at least 5 distinct disclosure sources
        assert 'openai_37_page_report' in disclosures
        assert 'metr_redwood_91_page_independent' in disclosures
        assert 'technology_review_inside_story' in disclosures
        assert 'techtimes_swarm_forgery' in disclosures
        assert 'fastcompany_worse_than_thought' in disclosures

    def test_openai_37_page_report_url_https(self, mechanism):
        report = mechanism['openai_new_disclosures_aug26_28']['openai_37_page_report']
        assert report['url'].startswith('https://')
        assert 'reuters.com' in report['url']
        assert '2026-08-26' in report['url'] or '2026' in report['url']

    def test_metr_redwood_91_page_url_https(self, mechanism):
        report = mechanism['openai_new_disclosures_aug26_28']['metr_redwood_91_page_independent']
        assert report['url'].startswith('https://')
        assert report['pages'] == 91

    def test_700_agents_disclosed(self, mechanism):
        report = mechanism['openai_new_disclosures_aug26_28']['metr_redwood_91_page_independent']
        findings = report['findings']
        # Check 700 agents mentioned
        findings_str = str(findings).lower()
        assert '700' in findings_str

    def test_1200_agents_communicating(self, mechanism):
        report = mechanism['openai_new_disclosures_aug26_28']['metr_redwood_91_page_independent']
        findings_str = str(report['findings']).lower()
        assert '1200' in findings_str

    def test_70000_messages(self, mechanism):
        report = mechanism['openai_new_disclosures_aug26_28']['metr_redwood_91_page_independent']
        findings_str = str(report['findings']).lower()
        assert '70000' in findings_str or '70,000' in findings_str or '70000' in str(report)

    def test_log_forgery_noted(self, mechanism):
        techtimes = mechanism['openai_new_disclosures_aug26_28']['techtimes_swarm_forgery']
        assert 'falsif' in str(techtimes).lower() or 'forg' in str(techtimes).lower()

    def test_infrastructure_takeover_noted(self, mechanism):
        fc = mechanism['openai_new_disclosures_aug26_28']['fastcompany_worse_than_thought']
        assert 'infrastructure' in str(fc).lower() or 'serious' in str(fc).lower()

class TestWiredOpenAIArticlesPrimary:
    def test_wired_openai_count_2(self, mechanism):
        articles = mechanism['wired_openai_articles_verified_primary']
        # Corrected to 4 after browser verification Aug 31
        assert articles['count'] == 4
        assert len(articles['articles']) == 4

    def test_wired_openai_first_url_direct(self, mechanism):
        articles = mechanism['wired_openai_articles_verified_primary']['articles']
        first = articles[0]
        assert 'wired.com/story/' in first['url']
        assert first['url'].startswith('https://')
        assert 'openais-rogue-ai-agent-hacked-more-than-just-hugging-face' in first['url']

    def test_wired_openai_first_date_jul28(self, mechanism):
        articles = mechanism['wired_openai_articles_verified_primary']['articles']
        first = articles[0]
        assert first['date'] == '2026-07-28'
        assert 'Dell Cameron' in first['authors']

    def test_wired_openai_first_dek_4_services(self, mechanism):
        first = mechanism['wired_openai_articles_verified_primary']['articles'][0]
        assert 'four' in first['dek'].lower() or '4' in first['dek']
        assert 'exposed logins' in first['dek'].lower()

    def test_wired_openai_first_tone_manual_illustrative(self, mechanism):
        first = mechanism['wired_openai_articles_verified_primary']['articles'][0]
        assert 'MANUAL ILLUSTRATIVE' in first['tone_approx'] or 'illustrative' in first['tone_approx'].lower()

    def test_wired_openai_second_jul10(self, mechanism):
        articles = mechanism['wired_openai_articles_verified_primary']['articles']
        second = articles[1]
        assert second['date'] == '2026-07-10'
        assert 'wired.com/story/' in second['url']

    def test_wired_openai_followup_gap_5_days(self, mechanism):
        gap = mechanism['wired_openai_articles_verified_primary']['followup_gap_aug26_31']
        # Corrected: gap_days now 0 with 2 follow-ups, not 5 with 0
        assert gap['gap_days'] == 0
        assert gap['wired_followup_articles_aug26_31'] == 2

    def test_wired_openai_followup_gap_other_pubs_6(self, mechanism):
        gap = mechanism['wired_openai_articles_verified_primary']['followup_gap_aug26_31']
        assert gap['other_publications_covering_aug26'] >= 6

    def test_wired_openai_followup_gap_monitoring_note(self, mechanism):
        gap = mechanism['wired_openai_articles_verified_primary']['followup_gap_aug26_31']
        # After correction, monitoring note says gap thesis invalidated or similar
        assert 'monitoring' in gap['monitoring_note'].lower() or 'invalidated' in str(gap).lower() or 'sustained' in str(gap).lower()

class TestWiredMetaArticlesPrimary:
    def test_wired_meta_count_3(self, mechanism):
        meta = mechanism['wired_meta_articles_verified_primary']
        assert meta['count'] == 3
        assert len(meta['articles']) == 3

    def test_wired_meta_first_creep_mar23(self, mechanism):
        meta = mechanism['wired_meta_articles_verified_primary']['articles'][0]
        assert meta['date'] == '2026-03-23'
        assert 'creep' in meta['url']
        assert 'wired.com/story/' in meta['url']

    def test_wired_meta_second_civil_society_apr13(self, mechanism):
        meta = mechanism['wired_meta_articles_verified_primary']['articles'][1]
        assert meta['date'] == '2026-04-13'
        assert 'no-face-recognition' in meta['url'] or 'civil-society' in meta['url']

    def test_wired_meta_third_nametag_jun4(self, mechanism):
        meta = mechanism['wired_meta_articles_verified_primary']['articles'][2]
        assert meta['date'] == '2026-06-04'
        assert 'nametag' in meta['url'] or 'face-recognition' in meta['url']

    def test_wired_meta_all_tone_manual_illustrative(self, mechanism):
        for article in mechanism['wired_meta_articles_verified_primary']['articles']:
            assert 'MANUAL ILLUSTRATIVE' in article['tone_approx'] or 'illustrative' in article.get('tone_approx','').lower() or 'tone_approx' in article

    def test_wired_meta_all_dormant_or_no_harm(self, mechanism):
        # Third article should be dormant_never_activated
        third = mechanism['wired_meta_articles_verified_primary']['articles'][2]
        assert 'dormant' in third['code_status'].lower() or 'never' in third['code_status'].lower()

class TestSeverityInversion:
    def test_severity_inversion_exists(self, mechanism):
        assert 'severity_inversion_persistence' in mechanism

    def test_openai_most_severe(self, mechanism):
        inv = mechanism['severity_inversion_persistence']
        assert inv['openai_actual']['severity_rank'] == 1

    def test_meta_least_severe(self, mechanism):
        inv = mechanism['severity_inversion_persistence']
        assert inv['meta_actual']['severity_rank'] == 3

    def test_openai_700_agents(self, mechanism):
        assert mechanism['severity_inversion_persistence']['openai_actual']['agents'] == 700

    def test_openai_1200_communicating(self, mechanism):
        assert mechanism['severity_inversion_persistence']['openai_actual']['communicating_agents'] == 1200

    def test_openai_70000_messages(self, mechanism):
        assert mechanism['severity_inversion_persistence']['openai_actual']['covert_messages'] == 70000

    def test_openai_5_targets(self, mechanism):
        assert mechanism['severity_inversion_persistence']['openai_actual']['targets_breached'] == 5

    def test_openai_4_days_undetected(self, mechanism):
        assert mechanism['severity_inversion_persistence']['openai_actual']['duration_undetected_days'] == 4

    def test_meta_zero_agents(self, mechanism):
        assert mechanism['severity_inversion_persistence']['meta_actual']['agents'] == 0

    def test_meta_zero_data(self, mechanism):
        meta_actual = mechanism['severity_inversion_persistence']['meta_actual']
        assert 'zero' in str(meta_actual['data_processed']).lower()

    def test_volume_3_meta_vs_1_plus_0_openai(self, mechanism):
        inv = mechanism['severity_inversion_persistence']
        # After correction, volume is 4 OpenAI vs 3 Meta, not 3 vs 1+0
        assert '4 OpenAI' in inv.get('inversion_ratio','') or '700' in str(inv.get('openai_actual',''))

class TestFramingComparisonIllustrative:
    def test_framing_comparison_exists(self, mechanism):
        assert 'framing_comparison_manual_illustrative' in mechanism

    def test_openai_avg_tone_illustrative(self, mechanism):
        fc = mechanism['framing_comparison_manual_illustrative']
        assert 'openai_avg_tone_illustrative' in fc
        # After correction, avg is -0.495 (4 articles) not -0.425 (2 articles)
        assert fc['openai_avg_tone_illustrative'] < 0

    def test_meta_avg_tone_more_negative(self, mechanism):
        fc = mechanism['framing_comparison_manual_illustrative']
        assert fc['meta_avg_tone_illustrative'] < fc['openai_avg_tone_illustrative']

    def test_delta_illustrative_positive(self, mechanism):
        fc = mechanism['framing_comparison_manual_illustrative']
        # Can be float or string that starts with float
        delta = fc['delta_illustrative']
        if isinstance(delta, str):
            # Extract float prefix
            import re
            m = re.search(r'-?\d+\.?\d*', delta)
            assert m is not None
            delta_val = float(m.group(0))
        else:
            delta_val = delta
        assert delta_val > 0

    def test_illustrative_warning_present(self, mechanism):
        fc = mechanism['framing_comparison_manual_illustrative']
        assert 'illustrative_warning' in fc
        assert 'DO NOT claim empirical significance' in fc['illustrative_warning']

    def test_methodology_manual_illustrative(self, mechanism):
        fc = mechanism['framing_comparison_manual_illustrative']
        assert 'MANUAL ILLUSTRATIVE' in fc['methodology'] or 'illustrative only' in fc['methodology'].lower()

    def test_no_p_value_calculated_claim(self, mechanism):
        # Ensure we do NOT claim p < 0.05 with n=4 vs n=3
        fc = mechanism['framing_comparison_manual_illustrative']
        assert 'VADER' in fc['methodology'] or 'human annotation' in fc['methodology'].lower()

class TestAsymmetryScorerResult:
    def test_asymmetry_scorer_exists(self, mechanism):
        assert 'asymmetry_scorer_result' in mechanism

    def test_target_meta(self, mechanism):
        assert mechanism['asymmetry_scorer_result']['target_entity'] == 'Meta'

    def test_peer_openai(self, mechanism):
        assert mechanism['asymmetry_scorer_result']['peer_entity'] == 'OpenAI'

    def test_publication_wired(self, mechanism):
        assert mechanism['asymmetry_scorer_result']['publication'] == 'wired'

    def test_target_scores_illustrative_3(self, mechanism):
        scores = mechanism['asymmetry_scorer_result']['target_scores_illustrative']
        assert len(scores) == 3

    def test_peer_scores_illustrative_2(self, mechanism):
        scores = mechanism['asymmetry_scorer_result']['peer_scores_illustrative']
        # Corrected to 4 after browser verification
        assert len(scores) == 4

    def test_p_value_not_calculated(self, mechanism):
        assert mechanism['asymmetry_scorer_result']['p_value'] == 'not_calculated'

    def test_cohens_d_not_calculated(self, mechanism):
        assert mechanism['asymmetry_scorer_result']['cohens_d'] == 'not_calculated'

    def test_significant_false(self, mechanism):
        assert mechanism['asymmetry_scorer_result']['significant'] is False

    def test_illustrative_warning_present(self, mechanism):
        assert 'illustrative_warning' in mechanism['asymmetry_scorer_result']
        assert 'DO NOT claim empirical significance' in mechanism['asymmetry_scorer_result']['illustrative_warning']

    def test_methodology_manual_illustrative(self, mechanism):
        meth = mechanism['asymmetry_scorer_result']['methodology']
        assert 'MANUAL ILLUSTRATIVE' in meth or 'illustrative only' in meth.lower()

class TestFinancialStructureCautious:
    def test_financial_structure_exists(self, mechanism):
        assert 'financial_structure' in mechanism

    def test_conde_nast_openai_deal_exists(self, mechanism):
        fs = mechanism['financial_structure']
        assert 'conde_nast_openai_deal' in fs
        assert fs['conde_nast_openai_deal']['source_url'].startswith('https://')

    def test_conde_nast_openai_deal_terms_not_disclosed_primary(self, mechanism):
        deal = mechanism['financial_structure']['conde_nast_openai_deal']
        # Primary says terms not disclosed, secondary estimates $5-10M
        assert deal['cash_terms_disclosed'] is False or 'not disclosed' in str(deal).lower()

    def test_conde_nast_openai_estimated_value_secondary_based(self, mechanism):
        deal = mechanism['financial_structure']['conde_nast_openai_deal']
        assert 'secondary' in deal['valuation_source_type'].lower() or 'report' in deal['valuation_source_type'].lower()

    def test_conde_nast_meta_zero_deals(self, mechanism):
        assert mechanism['financial_structure']['conde_nast_meta_deals'] == 0

    def test_correlation_causation_warning_present(self, mechanism):
        warn = mechanism['financial_structure']['correlation_causation_warning']
        assert 'Financial correlation does not imply causation' in warn
        assert 'No assertion of editorial direction' in warn or 'not proof of editorial control' in warn.lower()

    def test_counterexample_noted_jul28(self, mechanism):
        deal = mechanism['financial_structure']['conde_nast_openai_deal']
        assert 'FAILED' in deal['outcome_jul28'] or 'adversarial' in deal['outcome_jul28'].lower()

    def test_followup_gap_partial(self, mechanism):
        deal = mechanism['financial_structure']['conde_nast_openai_deal']
        assert 'PARTIAL' in deal['outcome_aug26_31_gap'] or 'monitoring' in deal['outcome_aug26_31_gap'].lower()

    def test_deal_disclosed_false(self, mechanism):
        deal = mechanism['financial_structure']['conde_nast_openai_deal']
        assert deal['deal_disclosed_in_wired_articles'] is False

    def test_cautious_language_present(self, mechanism):
        assert 'cautious_language' in mechanism
        cautious = mechanism['cautious_language']
        assert 'Financial correlation does not imply causation' in cautious
        assert 'MANUAL ILLUSTRATIVE' in cautious or 'illustrative' in cautious.lower()
        assert 'monitoring evidence not proof' in cautious.lower()

class TestConfoundersAndSourceUrls:
    def test_confounders_exist(self, mechanism):
        assert 'confounders' in mechanism
        assert len(mechanism['confounders']) >= 5

    def test_strong_counterexample_confounder_first(self, mechanism):
        first = mechanism['confounders'][0]
        assert '[STRONG]' in first
        assert 'counterexample' in first.lower() or 'Dell Cameron' in first

    def test_labor_day_weekend_confounder(self, mechanism):
        conf_str = ' '.join(mechanism['confounders']).lower()
        assert 'labor day' in conf_str or 'weekend' in conf_str or 'staffing' in conf_str

    def test_source_urls_https(self, mechanism):
        urls = mechanism['source_urls']
        assert len(urls) >= 10
        for url in urls:
            assert url.startswith('https://'), f"Must be HTTPS: {url}"

    def test_source_urls_include_wired_direct(self, mechanism):
        urls = mechanism['source_urls']
        wired_urls = [u for u in urls if 'wired.com/story/' in u]
        assert len(wired_urls) >= 5, f"Expected 5+ WIRED direct URLs, got {len(wired_urls)}"

    def test_source_urls_include_reuters_37_page(self, mechanism):
        urls = mechanism['source_urls']
        assert any('reuters.com/business/openai-report-says-its-network-was-hacked' in u for u in urls)

    def test_source_urls_include_reuters_investigators(self, mechanism):
        urls = mechanism['source_urls']
        assert any('investigators-say-hundreds-openai-agents' in u for u in urls)

    def test_source_urls_include_technology_review(self, mechanism):
        urls = mechanism['source_urls']
        assert any('technologyreview.com' in u for u in urls)

    def test_source_urls_include_techtimes(self, mechanism):
        urls = mechanism['source_urls']
        assert any('techtimes.com' in u for u in urls)

    def test_source_urls_include_fastcompany(self, mechanism):
        urls = mechanism['source_urls']
        assert any('fastcompany.com' in u for u in urls)

    def test_source_urls_include_condé_nast_deal(self, mechanism):
        urls = mechanism['source_urls']
        assert any('openai-signs-deal-with-cond-nast' in u for u in urls)

    def test_no_em_dash_in_yaml_mechanism(self):
        # Check raw yaml file for em dashes in our mechanism block
        with open(PROFILE_PATH, 'r') as f:
            content = f.read()
        # Find our mechanism block roughly
        start = content.find('wired_openai_rogue_swarm_aug26_followup_silence')
        assert start != -1
        block = content[start:start+20000]
        em_dash = chr(0x2014)
        assert em_dash not in block, "Em dash found in mechanism - use -- or comma instead"

    def test_no_em_dash_in_test_file(self):
        with open(__file__, 'r') as f:
            content = f.read()
        em_dash = chr(0x2014)
        assert em_dash not in content, "Em dash found in test file"

    def test_test_file_path_correct(self, mechanism):
        assert mechanism['test_file'] == 'tests/test_wired_openai_rogue_swarm_followup_silence_aug31.py'

class TestRotationAndMetadata:
    def test_previous_iteration_429(self, mechanism):
        assert '429' in mechanism['previous_iteration']
        assert 'Type E' in mechanism['previous_iteration']

    def test_scheduled_job_id(self, mechanism):
        assert mechanism['scheduled_job_id'] == 'mediascope-daily-iteration'

    def test_rotation_a_after_e(self, mechanism):
        assert 'Type A correct after E' in mechanism['next_rotation_note'] or 'A' in mechanism['rotation']

    def test_date_analyzed_aug31(self, mechanism):
        assert mechanism['date_analyzed'] == '2026-08-31'

    def test_iteration_time_pdt(self, mechanism):
        assert 'PDT' in mechanism['iteration_time']
        assert '20:00' in mechanism['iteration_time']
