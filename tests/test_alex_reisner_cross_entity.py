"""
Alex Reisner (The Atlantic, staff writer / AI Watchdog) cross-entity coverage analysis.

Mechanism #16: Training Data Investigative Target Gradient

Alex Reisner is The Atlantic's sole AI training data investigator and "AI Watchdog"
project lead. His work is genuinely valuable investigative journalism exposing real
corporate wrongdoing. However, when the same practice (using pirated content libraries
for AI training) implicates BOTH Meta AND OpenAI, the investigative depth, headline
framing, and dramatic narrative are asymmetrically weighted toward Meta.

Critical financial context: The Atlantic signed a multiyear content licensing deal
with OpenAI (May 29, 2024). Reisner's employer is financially entangled with one
of the two primary companies he investigates for training data piracy.

Date analyzed: 2026-08-09
"""

import unittest
import yaml
import os


def load_profile():
    path = os.path.join(os.path.dirname(__file__), '..', 'profiles', 'atlantic.yaml')
    with open(path) as f:
        return yaml.safe_load(f)


class TestAlexReisnerBasicProfile(unittest.TestCase):
    """Verify Alex Reisner's profile entry in atlantic.yaml."""

    def test_journalist_exists(self):
        profile = load_profile()
        names = [j['name'] for j in profile['key_journalists']]
        self.assertIn('Alex Reisner', names)

    def test_beat_is_training_data(self):
        profile = load_profile()
        reisner = [j for j in profile['key_journalists'] if j['name'] == 'Alex Reisner'][0]
        self.assertIn('training data', reisner['beat'].lower())

    def test_has_cross_entity_coverage_analysis(self):
        profile = load_profile()
        reisner = [j for j in profile['key_journalists'] if j['name'] == 'Alex Reisner'][0]
        self.assertIn('cross_entity_coverage_analysis', reisner)

    def test_mechanism_number(self):
        profile = load_profile()
        reisner = [j for j in profile['key_journalists'] if j['name'] == 'Alex Reisner'][0]
        self.assertEqual(reisner['cross_entity_coverage_analysis']['mechanism_number'], 16)

    def test_mechanism_name(self):
        profile = load_profile()
        reisner = [j for j in profile['key_journalists'] if j['name'] == 'Alex Reisner'][0]
        self.assertIn('training_data_investigative_target_gradient',
                      reisner['cross_entity_coverage_analysis']['mechanism_name'])

    def test_date_analyzed(self):
        profile = load_profile()
        reisner = [j for j in profile['key_journalists'] if j['name'] == 'Alex Reisner'][0]
        self.assertEqual(reisner['cross_entity_coverage_analysis']['date_analyzed'], '2026-08-09')


class TestBooks3Investigation(unittest.TestCase):
    """Books3 (Aug 2023): 190K pirated books. Meta foregrounded, OpenAI absent from headlines."""

    def test_books3_entry_exists(self):
        profile = load_profile()
        reisner = [j for j in profile['key_journalists'] if j['name'] == 'Alex Reisner'][0]
        cea = reisner['cross_entity_coverage_analysis']
        self.assertIn('books3_investigation', cea)

    def test_books3_date(self):
        profile = load_profile()
        reisner = [j for j in profile['key_journalists'] if j['name'] == 'Alex Reisner'][0]
        self.assertEqual(reisner['cross_entity_coverage_analysis']['books3_investigation']['date'], '2023-08')

    def test_books3_book_count(self):
        profile = load_profile()
        reisner = [j for j in profile['key_journalists'] if j['name'] == 'Alex Reisner'][0]
        inv = reisner['cross_entity_coverage_analysis']['books3_investigation']
        self.assertGreaterEqual(inv['pirated_book_count'], 170000)

    def test_meta_in_headline(self):
        profile = load_profile()
        reisner = [j for j in profile['key_journalists'] if j['name'] == 'Alex Reisner'][0]
        inv = reisner['cross_entity_coverage_analysis']['books3_investigation']
        self.assertTrue(inv['meta_in_headline'])

    def test_openai_absent_from_headline(self):
        profile = load_profile()
        reisner = [j for j in profile['key_journalists'] if j['name'] == 'Alex Reisner'][0]
        inv = reisner['cross_entity_coverage_analysis']['books3_investigation']
        self.assertFalse(inv['openai_in_headline'])

    def test_searchable_database_built(self):
        profile = load_profile()
        reisner = [j for j in profile['key_journalists'] if j['name'] == 'Alex Reisner'][0]
        inv = reisner['cross_entity_coverage_analysis']['books3_investigation']
        self.assertTrue(inv['searchable_database_built'])

    def test_meta_framing_register(self):
        profile = load_profile()
        reisner = [j for j in profile['key_journalists'] if j['name'] == 'Alex Reisner'][0]
        inv = reisner['cross_entity_coverage_analysis']['books3_investigation']
        self.assertEqual(inv['meta_framing_register'], 'investigative_expose')


class TestLibGenInvestigation(unittest.TestCase):
    """LibGen (Mar 2025): 7.5M books, both Meta and OpenAI implicated. Dramatic narrative 90% Meta."""

    def test_libgen_entry_exists(self):
        profile = load_profile()
        reisner = [j for j in profile['key_journalists'] if j['name'] == 'Alex Reisner'][0]
        cea = reisner['cross_entity_coverage_analysis']
        self.assertIn('libgen_investigation', cea)

    def test_libgen_date(self):
        profile = load_profile()
        reisner = [j for j in profile['key_journalists'] if j['name'] == 'Alex Reisner'][0]
        self.assertEqual(reisner['cross_entity_coverage_analysis']['libgen_investigation']['date'], '2025-03')

    def test_libgen_book_count(self):
        profile = load_profile()
        reisner = [j for j in profile['key_journalists'] if j['name'] == 'Alex Reisner'][0]
        inv = reisner['cross_entity_coverage_analysis']['libgen_investigation']
        self.assertGreaterEqual(inv['pirated_book_count'], 7500000)

    def test_both_companies_used_libgen(self):
        profile = load_profile()
        reisner = [j for j in profile['key_journalists'] if j['name'] == 'Alex Reisner'][0]
        inv = reisner['cross_entity_coverage_analysis']['libgen_investigation']
        self.assertIn('Meta', inv['companies_using_libgen'])
        self.assertIn('OpenAI', inv['companies_using_libgen'])

    def test_headline_foregrounds_meta(self):
        profile = load_profile()
        reisner = [j for j in profile['key_journalists'] if j['name'] == 'Alex Reisner'][0]
        inv = reisner['cross_entity_coverage_analysis']['libgen_investigation']
        self.assertIn('Meta', inv['subhead'])

    def test_meta_narrative_allocation(self):
        """~90% of dramatic narrative devoted to Meta."""
        profile = load_profile()
        reisner = [j for j in profile['key_journalists'] if j['name'] == 'Alex Reisner'][0]
        inv = reisner['cross_entity_coverage_analysis']['libgen_investigation']
        self.assertGreaterEqual(inv['meta_narrative_share_pct'], 85)

    def test_meta_dramatic_evidence(self):
        """Meta evidence includes internal emails, MZ escalation, corporate laptop concerns."""
        profile = load_profile()
        reisner = [j for j in profile['key_journalists'] if j['name'] == 'Alex Reisner'][0]
        inv = reisner['cross_entity_coverage_analysis']['libgen_investigation']
        meta_evidence = inv['meta_evidence_types']
        self.assertIn('internal_emails', meta_evidence)
        self.assertIn('mz_escalation', meta_evidence)
        self.assertIn('corporate_laptop_torrenting', meta_evidence)
        self.assertIn('legal_risk_assessment', meta_evidence)

    def test_openai_denial_accepted(self):
        """OpenAI gets one spokesperson denial quote, accepted at face value."""
        profile = load_profile()
        reisner = [j for j in profile['key_journalists'] if j['name'] == 'Alex Reisner'][0]
        inv = reisner['cross_entity_coverage_analysis']['libgen_investigation']
        self.assertEqual(inv['openai_evidence_type'], 'spokesperson_denial')

    def test_openai_denial_not_investigated(self):
        """No follow-up investigation into OpenAI's denial claims."""
        profile = load_profile()
        reisner = [j for j in profile['key_journalists'] if j['name'] == 'Alex Reisner'][0]
        inv = reisner['cross_entity_coverage_analysis']['libgen_investigation']
        self.assertFalse(inv['openai_denial_investigated'])

    def test_openai_former_employees_claim(self):
        """OpenAI claimed LibGen used by 'former employees' in 2021 — not independently verified."""
        profile = load_profile()
        reisner = [j for j in profile['key_journalists'] if j['name'] == 'Alex Reisner'][0]
        inv = reisner['cross_entity_coverage_analysis']['libgen_investigation']
        self.assertIn('former_employees', inv['openai_deflection_language'])


class TestMusicInvestigation(unittest.TestCase):
    """Music (Jun 2026): 21M songs. Targets Suno — company-neutral, NOT anti-Meta."""

    def test_music_entry_exists(self):
        profile = load_profile()
        reisner = [j for j in profile['key_journalists'] if j['name'] == 'Alex Reisner'][0]
        cea = reisner['cross_entity_coverage_analysis']
        self.assertIn('music_investigation', cea)

    def test_music_target_is_suno(self):
        profile = load_profile()
        reisner = [j for j in profile['key_journalists'] if j['name'] == 'Alex Reisner'][0]
        inv = reisner['cross_entity_coverage_analysis']['music_investigation']
        self.assertEqual(inv['primary_target'], 'Suno')

    def test_music_is_company_neutral(self):
        """When the investigation doesn't involve Meta vs OpenAI, framing is neutral."""
        profile = load_profile()
        reisner = [j for j in profile['key_journalists'] if j['name'] == 'Alex Reisner'][0]
        inv = reisner['cross_entity_coverage_analysis']['music_investigation']
        self.assertEqual(inv['framing_neutrality'], 'company_neutral')

    def test_music_track_count(self):
        profile = load_profile()
        reisner = [j for j in profile['key_journalists'] if j['name'] == 'Alex Reisner'][0]
        inv = reisner['cross_entity_coverage_analysis']['music_investigation']
        self.assertGreaterEqual(inv['track_count'], 12000000)


class TestFinancialConflict(unittest.TestCase):
    """The Atlantic has an OpenAI content licensing deal (May 2024). Reisner's employer is
    financially entangled with one of the two companies he investigates for piracy."""

    def test_atlantic_openai_deal_documented(self):
        profile = load_profile()
        reisner = [j for j in profile['key_journalists'] if j['name'] == 'Alex Reisner'][0]
        cea = reisner['cross_entity_coverage_analysis']
        self.assertIn('employer_financial_conflict', cea)

    def test_deal_date(self):
        profile = load_profile()
        reisner = [j for j in profile['key_journalists'] if j['name'] == 'Alex Reisner'][0]
        conflict = reisner['cross_entity_coverage_analysis']['employer_financial_conflict']
        self.assertEqual(conflict['deal_date'], '2024-05-29')

    def test_deal_partner_is_openai(self):
        profile = load_profile()
        reisner = [j for j in profile['key_journalists'] if j['name'] == 'Alex Reisner'][0]
        conflict = reisner['cross_entity_coverage_analysis']['employer_financial_conflict']
        self.assertEqual(conflict['partner'], 'OpenAI')

    def test_deal_type(self):
        profile = load_profile()
        reisner = [j for j in profile['key_journalists'] if j['name'] == 'Alex Reisner'][0]
        conflict = reisner['cross_entity_coverage_analysis']['employer_financial_conflict']
        self.assertIn('content_licensing', conflict['deal_type'])

    def test_deal_includes_training_data_access(self):
        """OpenAI gets access to The Atlantic's content archives for training."""
        profile = load_profile()
        reisner = [j for j in profile['key_journalists'] if j['name'] == 'Alex Reisner'][0]
        conflict = reisner['cross_entity_coverage_analysis']['employer_financial_conflict']
        self.assertTrue(conflict['openai_gets_training_data_access'])

    def test_atlantic_labs_collaboration(self):
        """OpenAI also collaborates on Atlantic Labs microsite."""
        profile = load_profile()
        reisner = [j for j in profile['key_journalists'] if j['name'] == 'Alex Reisner'][0]
        conflict = reisner['cross_entity_coverage_analysis']['employer_financial_conflict']
        self.assertTrue(conflict['product_collaboration'])

    def test_union_opposition_documented(self):
        """Atlantic union was 'deeply troubled' by the deal."""
        profile = load_profile()
        reisner = [j for j in profile['key_journalists'] if j['name'] == 'Alex Reisner'][0]
        conflict = reisner['cross_entity_coverage_analysis']['employer_financial_conflict']
        self.assertTrue(conflict['union_opposition'])

    def test_editor_backed_union(self):
        """Editor-in-chief Jeffrey Goldberg backed the union's concerns."""
        profile = load_profile()
        reisner = [j for j in profile['key_journalists'] if j['name'] == 'Alex Reisner'][0]
        conflict = reisner['cross_entity_coverage_analysis']['employer_financial_conflict']
        self.assertTrue(conflict['editor_backed_union_concerns'])


class TestTheWatchdogParadox(unittest.TestCase):
    """The central paradox: Atlantic's 'AI Watchdog' who investigates companies for pirating
    content to train AI works at a publication that LICENSED ITS OWN CONTENT to one of those
    same pirate companies."""

    def test_paradox_documented(self):
        profile = load_profile()
        reisner = [j for j in profile['key_journalists'] if j['name'] == 'Alex Reisner'][0]
        cea = reisner['cross_entity_coverage_analysis']
        self.assertIn('watchdog_paradox', cea)

    def test_paradox_description(self):
        profile = load_profile()
        reisner = [j for j in profile['key_journalists'] if j['name'] == 'Alex Reisner'][0]
        paradox = reisner['cross_entity_coverage_analysis']['watchdog_paradox']
        desc = paradox['description'].lower()
        self.assertIn('watchdog', desc)
        self.assertIn('openai', desc)

    def test_paradox_asymmetry_direction(self):
        """Asymmetry direction: softer on OpenAI (deal partner), harder on Meta (no deal)."""
        profile = load_profile()
        reisner = [j for j in profile['key_journalists'] if j['name'] == 'Alex Reisner'][0]
        paradox = reisner['cross_entity_coverage_analysis']['watchdog_paradox']
        self.assertEqual(paradox['softer_coverage_target'], 'OpenAI')
        self.assertEqual(paradox['harder_coverage_target'], 'Meta')

    def test_meta_has_no_atlantic_deal(self):
        """Meta has no content licensing deal with The Atlantic."""
        profile = load_profile()
        reisner = [j for j in profile['key_journalists'] if j['name'] == 'Alex Reisner'][0]
        paradox = reisner['cross_entity_coverage_analysis']['watchdog_paradox']
        self.assertFalse(paradox['meta_has_atlantic_deal'])


class TestLegitimateFactors(unittest.TestCase):
    """Acknowledge legitimate factors that partially explain the asymmetry."""

    def test_legitimate_factors_documented(self):
        profile = load_profile()
        reisner = [j for j in profile['key_journalists'] if j['name'] == 'Alex Reisner'][0]
        cea = reisner['cross_entity_coverage_analysis']
        self.assertIn('legitimate_factors', cea)

    def test_meta_has_more_court_evidence(self):
        """Meta has more dramatic court evidence (unsealed emails, MZ escalation)."""
        profile = load_profile()
        reisner = [j for j in profile['key_journalists'] if j['name'] == 'Alex Reisner'][0]
        factors = reisner['cross_entity_coverage_analysis']['legitimate_factors']
        factor_names = [f['factor'] for f in factors]
        self.assertIn('meta_court_evidence_volume', factor_names)

    def test_recency_factor(self):
        """Meta's LibGen use more recent (2023-2024) vs OpenAI's (claimed 2021)."""
        profile = load_profile()
        reisner = [j for j in profile['key_journalists'] if j['name'] == 'Alex Reisner'][0]
        factors = reisner['cross_entity_coverage_analysis']['legitimate_factors']
        factor_names = [f['factor'] for f in factors]
        self.assertIn('temporal_recency', factor_names)

    def test_reisner_covers_other_companies(self):
        """Reisner also covers Suno, The Pile (Nvidia, Apple, etc.) — not exclusively anti-Meta."""
        profile = load_profile()
        reisner = [j for j in profile['key_journalists'] if j['name'] == 'Alex Reisner'][0]
        factors = reisner['cross_entity_coverage_analysis']['legitimate_factors']
        factor_names = [f['factor'] for f in factors]
        self.assertIn('multi_company_coverage', factor_names)


class TestQuantitativeSummary(unittest.TestCase):
    """Quantitative summary of the cross-entity asymmetry."""

    def test_summary_exists(self):
        profile = load_profile()
        reisner = [j for j in profile['key_journalists'] if j['name'] == 'Alex Reisner'][0]
        cea = reisner['cross_entity_coverage_analysis']
        self.assertIn('quantitative_summary', cea)

    def test_meta_article_count(self):
        """Multiple articles primarily targeting Meta's training data practices."""
        profile = load_profile()
        reisner = [j for j in profile['key_journalists'] if j['name'] == 'Alex Reisner'][0]
        summary = reisner['cross_entity_coverage_analysis']['quantitative_summary']
        self.assertGreaterEqual(summary['meta_primary_target_articles'], 2)

    def test_openai_standalone_investigation_count(self):
        """Zero standalone investigations of OpenAI's training data practices."""
        profile = load_profile()
        reisner = [j for j in profile['key_journalists'] if j['name'] == 'Alex Reisner'][0]
        summary = reisner['cross_entity_coverage_analysis']['quantitative_summary']
        self.assertEqual(summary['openai_standalone_investigation_articles'], 0)

    def test_headline_asymmetry(self):
        """Meta appears in headlines; OpenAI does not."""
        profile = load_profile()
        reisner = [j for j in profile['key_journalists'] if j['name'] == 'Alex Reisner'][0]
        summary = reisner['cross_entity_coverage_analysis']['quantitative_summary']
        self.assertGreaterEqual(summary['meta_headline_appearances'], 2)
        self.assertEqual(summary['openai_headline_appearances'], 0)

    def test_searchable_database_targets(self):
        """Searchable databases built for Meta/Books3 and LibGen — framed around Meta."""
        profile = load_profile()
        reisner = [j for j in profile['key_journalists'] if j['name'] == 'Alex Reisner'][0]
        summary = reisner['cross_entity_coverage_analysis']['quantitative_summary']
        self.assertGreaterEqual(summary['searchable_databases_built'], 2)

    def test_overall_tone_delta(self):
        """Significant tone delta between Meta and OpenAI coverage."""
        profile = load_profile()
        reisner = [j for j in profile['key_journalists'] if j['name'] == 'Alex Reisner'][0]
        summary = reisner['cross_entity_coverage_analysis']['quantitative_summary']
        self.assertGreaterEqual(summary['meta_openai_tone_delta'], 0.5)


if __name__ == '__main__':
    unittest.main()
