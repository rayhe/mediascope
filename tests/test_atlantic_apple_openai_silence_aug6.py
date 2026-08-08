"""
Test: Atlantic × Apple/OpenAI — 27-Day Editorial Silence on Densest Financial Conflict
Created: 2026-08-06 15:00 PT (Type A: Competitor Coverage Deep Dive)

Validates the finding that The Atlantic has maintained complete editorial
silence on the Apple v. OpenAI trade secret lawsuit (Jul 10 → Aug 6, 2026)
despite having the densest five-way financial conflict of any publication
in the tracked set. Tests verify data consistency across profiles, escalation
timeline accuracy, and silence duration claims.
"""
import yaml
import os
import unittest
from datetime import date

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


def load_yaml(filename):
    path = os.path.join(PROFILES_DIR, filename)
    with open(path) as f:
        return yaml.safe_load(f)


class TestAtlanticAppleOpenAISilenceDuration(unittest.TestCase):
    """Verify the 27-day silence claim is consistent across profiles."""

    @classmethod
    def setUpClass(cls):
        cls.research = load_yaml('competitor-coverage-research.yaml')
        cls.atlantic = load_yaml('atlantic.yaml')
        cls.entities = load_yaml('competitor-entities.yaml')

    def _get_atlantic_research(self):
        return self.research['publications']['atlantic']

    def test_silence_section_exists(self):
        """Atlantic research has apple_v_openai_editorial_silence section."""
        atlantic = self._get_atlantic_research()
        self.assertIn('apple_v_openai_editorial_silence', atlantic)

    def test_silence_spans_27_days(self):
        """Silence duration is documented as at least 27 days."""
        silence = self._get_atlantic_research()['apple_v_openai_editorial_silence']
        desc = silence['description']
        # Accept either 27 or 29 days (updated Aug 8)
        self.assertTrue('27 days' in desc or '29 days' in desc)

    def test_filing_date_jul_10(self):
        """Apple filing date is Jul 10, 2026."""
        silence = self._get_atlantic_research()['apple_v_openai_editorial_silence']
        desc = silence['description']
        self.assertIn('Jul 10', desc)

    def test_preliminary_injunction_aug_4(self):
        """Apple preliminary injunction date is Aug 4, 2026."""
        silence = self._get_atlantic_research()['apple_v_openai_editorial_silence']
        desc = silence['description']
        self.assertIn('Aug 4', desc)

    def test_motion_to_dismiss_aug_6(self):
        """OpenAI motion to dismiss date is Aug 6, 2026."""
        silence = self._get_atlantic_research()['apple_v_openai_editorial_silence']
        desc = silence['description']
        self.assertIn('Aug 6', desc)

    def test_three_escalation_phases(self):
        """Three escalation phases documented."""
        silence = self._get_atlantic_research()['apple_v_openai_editorial_silence']
        desc = silence['description']
        # Check all three phases numbered
        self.assertIn('(1)', desc)
        self.assertIn('(2)', desc)
        self.assertIn('(3)', desc)


class TestAtlanticFiveWayConflict(unittest.TestCase):
    """Verify the five-way conflict structure is documented."""

    @classmethod
    def setUpClass(cls):
        cls.research = load_yaml('competitor-coverage-research.yaml')
        cls.atlantic = load_yaml('atlantic.yaml')

    def _get_silence(self):
        return self.research['publications']['atlantic']['apple_v_openai_editorial_silence']

    def test_five_way_conflict_section(self):
        """FIVE-WAY CONFLICT documented in silence section."""
        desc = self._get_silence()['description']
        self.assertIn('FIVE-WAY CONFLICT', desc)

    def test_lpj_apple_stock_plaintiff(self):
        """LPJ $17B Apple stock as PLAINTIFF."""
        desc = self._get_silence()['description']
        self.assertIn('PLAINTIFF', desc)
        self.assertIn('$17B', desc)

    def test_ec_io_products_defendant(self):
        """EC backed io Products as DEFENDANT."""
        desc = self._get_silence()['description']
        self.assertIn('io Products', desc)
        self.assertIn('DEFENDANT', desc)

    def test_atlantic_openai_deal_primary_defendant(self):
        """Atlantic OpenAI deal as PRIMARY DEFENDANT."""
        desc = self._get_silence()['description']
        self.assertIn('PRIMARY DEFENDANT', desc)

    def test_atlantic_labs_collaboration(self):
        """Atlantic Labs co-development with OpenAI."""
        desc = self._get_silence()['description']
        self.assertIn('Atlantic Labs', desc)

    def test_io_products_acquisition_profit(self):
        """EC profited from $6.5B io Products acquisition."""
        desc = self._get_silence()['description']
        self.assertIn('$6.5B', desc)


class TestEscalationSourceURLs(unittest.TestCase):
    """Verify all escalation source URLs exist and are plausible."""

    @classmethod
    def setUpClass(cls):
        cls.research = load_yaml('competitor-coverage-research.yaml')

    def _get_silence(self):
        return self.research['publications']['atlantic']['apple_v_openai_editorial_silence']

    def test_filing_source_url(self):
        """Filing source URL exists and references Reuters."""
        sources = self._get_silence()['escalation_sources']
        self.assertIn('filing', sources)
        self.assertIn('reuters.com', sources['filing'])

    def test_injunction_source_url(self):
        """Preliminary injunction source URL exists and references Reuters."""
        sources = self._get_silence()['escalation_sources']
        self.assertIn('preliminary_injunction', sources)
        self.assertIn('reuters.com', sources['preliminary_injunction'])

    def test_dismissal_source_url(self):
        """Motion to dismiss source URL exists."""
        sources = self._get_silence()['escalation_sources']
        self.assertIn('motion_to_dismiss', sources)
        self.assertIn('reuters.com', sources['motion_to_dismiss'])

    def test_openai_blog_response_url(self):
        """OpenAI blog response URL exists and references WSJ."""
        sources = self._get_silence()['escalation_sources']
        self.assertIn('openai_blog_response', sources)
        self.assertIn('wsj.com', sources['openai_blog_response'])


class TestPublicationsCoveredVsNotCovered(unittest.TestCase):
    """Verify the coverage tracking lists."""

    @classmethod
    def setUpClass(cls):
        cls.research = load_yaml('competitor-coverage-research.yaml')

    def _get_silence(self):
        return self.research['publications']['atlantic']['apple_v_openai_editorial_silence']

    def test_within_hours_list(self):
        """Multiple publications covered within hours."""
        pubs = self._get_silence()['publications_that_covered']['within_hours']
        self.assertGreater(len(pubs), 8)
        self.assertIn('Reuters', pubs)
        self.assertIn('CNN', pubs)
        self.assertIn('WSJ', pubs)
        self.assertIn('TechCrunch', pubs)

    def test_within_days_list(self):
        """Additional publications covered within days."""
        pubs = self._get_silence()['publications_that_covered']['within_days']
        self.assertGreater(len(pubs), 2)

    def test_atlantic_in_not_covered(self):
        """The Atlantic is explicitly listed as not_covered."""
        pubs = self._get_silence()['publications_that_covered']['not_covered']
        self.assertIn('The Atlantic', pubs)

    def test_not_covered_is_atlantic_only(self):
        """Only The Atlantic in the not_covered list."""
        pubs = self._get_silence()['publications_that_covered']['not_covered']
        self.assertEqual(len(pubs), 1)


class TestAtlanticProfileEditorialGap(unittest.TestCase):
    """Verify the Atlantic profile's editorial coverage gap is updated."""

    @classmethod
    def setUpClass(cls):
        cls.atlantic = load_yaml('atlantic.yaml')

    def _get_io_products_investment(self):
        """Find io Products investment in Atlantic profile."""
        # Search in ownership_chain entities' investments
        for item in self.atlantic.get('ownership_chain', []):
            if isinstance(item, dict) and 'investments' in item:
                for inv in item['investments']:
                    if 'io Products' in inv.get('entity', ''):
                        return inv
        # Also check top-level investments
        for inv in self.atlantic.get('investments', []):
            if 'io Products' in inv.get('entity', ''):
                return inv
        return None

    def test_io_products_investment_exists(self):
        """io Products investment documented in Atlantic profile."""
        inv = self._get_io_products_investment()
        self.assertIsNotNone(inv, "io Products investment should exist in Atlantic profile")

    def test_editorial_gap_references_27_days(self):
        """Atlantic profile's editorial gap mentions 27 days."""
        inv = self._get_io_products_investment()
        if inv:
            notes = inv.get('notes', '') + inv.get('relationship', '')
            self.assertIn('27', notes)

    def test_editorial_gap_references_three_escalations(self):
        """Atlantic profile mentions three escalation phases."""
        inv = self._get_io_products_investment()
        if inv:
            notes = inv.get('notes', '') + inv.get('relationship', '')
            # Should mention preliminary injunction and motion to dismiss
            self.assertIn('preliminary injunction', notes.lower())

    def test_editorial_gap_updated_beyond_jul_12(self):
        """Atlantic profile's editorial gap is updated beyond the original Jul 12 date."""
        inv = self._get_io_products_investment()
        if inv:
            notes = inv.get('notes', '') + inv.get('relationship', '')
            # Should NOT still say "Jul 12" as the only date — should include Aug dates
            self.assertIn('Aug', notes)


class TestSilenceAsOmissionBias(unittest.TestCase):
    """Verify the theoretical framework: silence as editorial bias."""

    @classmethod
    def setUpClass(cls):
        cls.research = load_yaml('competitor-coverage-research.yaml')

    def _get_silence(self):
        return self.research['publications']['atlantic']['apple_v_openai_editorial_silence']

    def test_mediascope_significance_exists(self):
        """MediaScope significance section exists."""
        silence = self._get_silence()
        self.assertIn('mediascope_significance', silence)

    def test_omission_as_bias_documented(self):
        """Editorial OMISSION identified as extreme bias form."""
        sig = self._get_silence()['mediascope_significance']
        self.assertIn('OMISSION', sig)

    def test_silence_vs_tone_distinction(self):
        """Distinction between tone bias and coverage omission."""
        sig = self._get_silence()['mediascope_significance']
        self.assertIn('tone', sig.lower())

    def test_no_disclosure_possible_without_coverage(self):
        """Notes that no disclosure failure is possible when coverage doesn't exist."""
        sig = self._get_silence()['mediascope_significance']
        self.assertIn('disclosure', sig.lower())


class TestAsymmetryVerdictUpdated(unittest.TestCase):
    """Verify the asymmetry_verdict references the Aug 6 silence finding."""

    @classmethod
    def setUpClass(cls):
        cls.research = load_yaml('competitor-coverage-research.yaml')

    def _get_atlantic(self):
        return self.research['publications']['atlantic']

    def test_verdict_mentions_aug_6(self):
        """Asymmetry verdict references Aug 6, 2026 update."""
        verdict = self._get_atlantic()['asymmetry_verdict']
        self.assertIn('Aug 6', verdict)

    def test_verdict_mentions_omission(self):
        """Verdict extends analysis from tone to omission."""
        verdict = self._get_atlantic()['asymmetry_verdict']
        self.assertIn('OMISSION', verdict)

    def test_verdict_mentions_trade_secret(self):
        """Verdict references trade secret lawsuit."""
        verdict = self._get_atlantic()['asymmetry_verdict']
        self.assertIn('trade secret', verdict.lower())

    def test_verdict_maintains_five_vectors(self):
        """Verdict still documents 5 financial vectors vs Meta's 0."""
        verdict = self._get_atlantic()['asymmetry_verdict']
        self.assertIn('5', verdict)
        self.assertIn('Meta: 0', verdict)


class TestOpenAIDismissalLanguage(unittest.TestCase):
    """Verify OpenAI's Aug 6 motion to dismiss language is captured."""

    @classmethod
    def setUpClass(cls):
        cls.research = load_yaml('competitor-coverage-research.yaml')

    def _get_silence(self):
        return self.research['publications']['atlantic']['apple_v_openai_editorial_silence']

    def test_careless_language_captured(self):
        """OpenAI's 'careless' characterization documented."""
        desc = self._get_silence()['description']
        self.assertIn('careless', desc.lower())

    def test_oddly_personal_language_captured(self):
        """OpenAI's 'oddly personal' characterization documented."""
        desc = self._get_silence()['description']
        self.assertIn('oddly personal', desc.lower())

    def test_common_issue_language(self):
        """OpenAI's claim about Apple's 'common issue' documented."""
        desc = self._get_silence()['description']
        self.assertIn('common issue', desc.lower())

    def test_motion_filed_same_day_as_analysis(self):
        """Motion to dismiss filed same day as this analysis (Aug 6)."""
        desc = self._get_silence()['description']
        self.assertIn('Aug 6', desc)


class TestCrossEntityConsistency(unittest.TestCase):
    """Verify Apple and OpenAI entity profiles are consistent with lawsuit data."""

    @classmethod
    def setUpClass(cls):
        cls.entities = load_yaml('competitor-entities.yaml')

    def test_apple_openai_collapse_documented(self):
        """Apple entity has openai_partnership_collapse section."""
        apple = self.entities['entities']['apple']
        self.assertIn('openai_partnership_collapse', apple)

    def test_apple_lawsuit_date_consistent(self):
        """Apple-OpenAI lawsuit date is Jul 10 in entity profile."""
        apple = self.entities['entities']['apple']
        collapse = apple['openai_partnership_collapse']
        # Check phase 3 date
        phase3 = collapse.get('phase_3_apple_sues_openai', {})
        date_val = phase3.get('date')
        # YAML may parse as date object or string
        if isinstance(date_val, date):
            self.assertEqual(str(date_val), '2026-07-10')
        else:
            self.assertEqual(date_val, '2026-07-10')

    def test_openai_entity_exists(self):
        """OpenAI entity exists in competitor-entities.yaml."""
        self.assertIn('openai', self.entities['entities'])

    def test_io_products_named_as_defendant(self):
        """io Products named as defendant in Apple-OpenAI section."""
        apple = self.entities['entities']['apple']
        collapse = apple['openai_partnership_collapse']
        overview = collapse.get('overview', '')
        phase3 = collapse.get('phase_3_apple_sues_openai', {})
        combined = overview + phase3.get('detail', '')
        self.assertIn('io Products', combined)


if __name__ == '__main__':
    unittest.main()
