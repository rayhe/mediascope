"""
MIT Technology Review × Anthropic — Pre-IPO Product Validation Asymmetry (Aug 9, 2026)

Tests for Mechanism #15: Pre-IPO Product Validation Amplifier.

MIT TR's Anthropic coverage in Jun-Jul 2026 uses fascinated/validating framing for
products and research, while contemporaneous Meta coverage uses security-failure/
warfare/dismissive framing for equivalent activities. The asymmetry is maximum (1.0
headline valence gap) and aligns with MIT's indirect financial interests through the
Google/Amazon → Anthropic endowment chain.

Key finding: MIT TR uses Anthropic as the standard-bearer for AI competence, against
which Meta's failures are measured. In the same article ("The Meta hack"), Anthropic's
Mythos is positioned as "too good at hacking to be released" (competence benchmark)
while Meta is "practically mindless" (incompetence benchmark).

Source: MIT Technology Review (technologyreview.com), Jun-Jul 2026
Analysis date: 2026-08-09
"""

import yaml
import os
import pytest

PROFILE_PATH = os.path.join(os.path.dirname(__file__), '..', 'profiles', 'mit-tech-review.yaml')


@pytest.fixture(scope='module')
def profile():
    with open(PROFILE_PATH) as f:
        return yaml.safe_load(f)


@pytest.fixture(scope='module')
def paradox(profile):
    return profile['competitor_relationships']['anthropic']['pre_ipo_product_validation_paradox']


@pytest.fixture(scope='module')
def anthropic_rel(profile):
    return profile['competitor_relationships']['anthropic']


class TestFinancialTieUpdate:
    """Verify the Anthropic financial tie has been updated from 'none' to indirect."""

    def test_financial_tie_is_indirect_endowment(self, anthropic_rel):
        assert anthropic_rel['financial_tie'] == 'indirect_endowment'

    def test_estimated_value_mentions_endowment(self, anthropic_rel):
        val = anthropic_rel['estimated_value'].lower()
        assert 'endowment' in val
        assert '$0 direct' in anthropic_rel['estimated_value']

    def test_direction_links_anthropic_to_mit(self, anthropic_rel):
        assert 'anthropic' in anthropic_rel['direction'].lower()
        assert 'endowment' in anthropic_rel['direction'].lower()

    def test_description_mentions_google_amazon(self, anthropic_rel):
        desc = anthropic_rel['description'].lower()
        assert 'google' in desc
        assert 'amazon' in desc

    def test_description_mentions_ipo(self, anthropic_rel):
        desc = anthropic_rel['description'].lower()
        assert 'ipo' in desc

    def test_coverage_prediction_shifted(self, anthropic_rel):
        assert anthropic_rel['coverage_prediction'] == 'softer_than_expected'


class TestMechanismIdentification:
    """Verify mechanism #15 is properly documented."""

    def test_mechanism_id(self, paradox):
        assert paradox['mechanism_id'] == 15

    def test_mechanism_name(self, paradox):
        assert 'Pre-IPO' in paradox['mechanism_name']
        assert 'Validation' in paradox['mechanism_name']

    def test_analysis_date(self, paradox):
        assert paradox['date_analyzed'] == '2026-08-09'


class TestAnthropicArticles:
    """Verify all 4 Anthropic pre-IPO articles are documented with correct framing."""

    def test_anthropic_article_count(self, paradox):
        assert len(paradox['anthropic_articles']) == 4

    def test_jspace_article_register(self, paradox):
        jspace = [a for a in paradox['anthropic_articles']
                  if 'hidden space' in a['title'].lower()][0]
        assert 'wonder' in jspace['register'] or 'fascination' in jspace['register']

    def test_jspace_article_url(self, paradox):
        jspace = [a for a in paradox['anthropic_articles']
                  if 'hidden space' in a['title'].lower()][0]
        assert 'technologyreview.com' in jspace['url']
        assert '2026' in jspace['url']

    def test_claude_science_register(self, paradox):
        cs = [a for a in paradox['anthropic_articles']
              if 'claude science' in a['title'].lower()][0]
        assert 'validation' in cs['register'] or 'product' in cs['register']

    def test_claude_science_deepmind_mantle(self, paradox):
        cs = [a for a in paradox['anthropic_articles']
              if 'claude science' in a['title'].lower()][0]
        assert 'mantle' in cs['key_framing'].lower() or 'DeepMind' in cs['key_framing']

    def test_code_with_claude_register(self, paradox):
        cwc = [a for a in paradox['anthropic_articles']
               if 'code with claude' in a['title'].lower()][0]
        assert 'future' in cwc['register']

    def test_breakthrough_technologies_register(self, paradox):
        bt = [a for a in paradox['anthropic_articles']
              if 'breakthrough' in a['title'].lower()][0]
        assert 'endorsement' in bt['register']


class TestMetaArticles:
    """Verify all 3 contemporaneous Meta articles are documented with correct framing."""

    def test_meta_article_count(self, paradox):
        assert len(paradox['meta_articles_same_period']) == 3

    def test_meta_hack_register(self, paradox):
        hack = [a for a in paradox['meta_articles_same_period']
                if 'hack' in a['title'].lower()][0]
        assert 'failure' in hack['register'] or 'incompetence' in hack['register']

    def test_meta_hack_practically_mindless(self, paradox):
        hack = [a for a in paradox['meta_articles_same_period']
                if 'hack' in a['title'].lower()][0]
        assert 'practically mindless' in hack['key_framing'].lower()

    def test_meta_hack_url(self, paradox):
        hack = [a for a in paradox['meta_articles_same_period']
                if 'hack' in a['title'].lower()][0]
        assert 'technologyreview.com' in hack['url']

    def test_warfare_article_register(self, paradox):
        warfare = [a for a in paradox['meta_articles_same_period']
                   if 'warfare' in a['title'].lower()][0]
        assert 'warfare' in warfare['register'] or 'military' in warfare['register']

    def test_warfare_weapons_system(self, paradox):
        warfare = [a for a in paradox['meta_articles_same_period']
                   if 'warfare' in a['title'].lower()][0]
        assert 'weapons system' in warfare['key_framing'].lower()

    def test_brain_typing_register(self, paradox):
        bt = [a for a in paradox['meta_articles_same_period']
              if 'brain typing' in a['title'].lower()][0]
        assert 'dismissive' in bt['register']

    def test_brain_typing_stuck_framing(self, paradox):
        bt = [a for a in paradox['meta_articles_same_period']
              if 'brain typing' in a['title'].lower()][0]
        assert 'stuck' in bt['key_framing'].lower()


class TestQuantitativeSummary:
    """Verify the headline valence gap and article counts."""

    def test_anthropic_article_count(self, paradox):
        assert paradox['quantitative_summary']['anthropic_article_count'] == 4

    def test_anthropic_positive_count(self, paradox):
        assert paradox['quantitative_summary']['anthropic_positive_register_count'] == 4

    def test_anthropic_negative_count(self, paradox):
        assert paradox['quantitative_summary']['anthropic_negative_register_count'] == 0

    def test_meta_article_count(self, paradox):
        assert paradox['quantitative_summary']['meta_article_count'] == 3

    def test_meta_positive_count(self, paradox):
        assert paradox['quantitative_summary']['meta_positive_register_count'] == 0

    def test_meta_negative_count(self, paradox):
        assert paradox['quantitative_summary']['meta_negative_register_count'] == 3

    def test_headline_valence_gap_maximum(self, paradox):
        assert paradox['quantitative_summary']['headline_valence_gap'] == 1.0

    def test_anthropic_as_meta_benchmark(self, paradox):
        benchmark = paradox['quantitative_summary']['anthropic_as_meta_benchmark'].lower()
        assert 'mythos' in benchmark
        assert 'standard-bearer' in benchmark or 'measuring stick' in benchmark


class TestFinancialIncentiveConnection:
    """Verify the endowment → IPO incentive chain is documented."""

    def test_pre_ipo_timing(self, paradox):
        fic = paradox['financial_incentive_connection'].lower()
        assert 'pre-ipo' in fic or 'october 2026' in fic

    def test_google_stake_value(self, paradox):
        fic = paradox['financial_incentive_connection']
        assert '$135B' in fic or '135B' in fic

    def test_amazon_stake_value(self, paradox):
        fic = paradox['financial_incentive_connection']
        assert '$200B' in fic or '200B' in fic

    def test_endowment_size(self, paradox):
        fic = paradox['financial_incentive_connection']
        assert '$27.4B' in fic or '27.4B' in fic

    def test_kornbluth_corporate_pivot(self, paradox):
        fic = paradox['financial_incentive_connection'].lower()
        assert 'kornbluth' in fic

    def test_obbba_pressure(self, paradox):
        fic = paradox['financial_incentive_connection'].lower()
        assert 'obbba' in fic or 'endowment tax' in fic


class TestCrossReferences:
    """Verify cross-references to other documented asymmetry patterns."""

    def test_cross_references_exist(self, paradox):
        assert len(paradox['cross_reference']) >= 3

    def test_barrett_paradox_referenced(self, paradox):
        refs = ' '.join(paradox['cross_reference']).lower()
        assert 'barrett' in refs

    def test_wong_paradox_referenced(self, paradox):
        refs = ' '.join(paradox['cross_reference']).lower()
        assert 'wong' in refs

    def test_wdh_profile_referenced(self, paradox):
        refs = ' '.join(paradox['cross_reference']).lower()
        assert 'wdh' in refs or 'journalist' in refs


class TestComparisonArticleAlignment:
    """Verify that Anthropic and Meta comparison notes reference each other."""

    def test_jspace_comparison_mentions_meta_hack(self, paradox):
        jspace = [a for a in paradox['anthropic_articles']
                  if 'hidden space' in a['title'].lower()][0]
        assert 'meta' in jspace['comparison_to_meta'].lower()

    def test_claude_science_comparison_mentions_muse_spark(self, paradox):
        cs = [a for a in paradox['anthropic_articles']
              if 'claude science' in a['title'].lower()][0]
        comp = cs['comparison_to_meta'].lower()
        assert 'muse spark' in comp or 'warfare' in comp

    def test_code_with_claude_comparison_mentions_llama(self, paradox):
        cwc = [a for a in paradox['anthropic_articles']
               if 'code with claude' in a['title'].lower()][0]
        comp = cwc['comparison_to_meta'].lower()
        assert 'llama' in comp or 'open-weight' in comp

    def test_meta_hack_comparison_mentions_anthropic(self, paradox):
        hack = [a for a in paradox['meta_articles_same_period']
                if 'hack' in a['title'].lower()][0]
        assert 'anthropic' in hack['key_framing'].lower() or 'mythos' in hack['key_framing'].lower()

    def test_meta_warfare_comparison_mentions_consumer(self, paradox):
        warfare = [a for a in paradox['meta_articles_same_period']
                   if 'warfare' in a['title'].lower()][0]
        framing = warfare['key_framing'].lower()
        assert 'consumer' in framing or 'weapons' in framing
