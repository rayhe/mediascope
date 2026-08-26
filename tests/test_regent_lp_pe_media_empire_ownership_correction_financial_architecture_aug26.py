"""
Test: Regent LP — PE Media Empire Ownership Correction & Financial Architecture

Mechanism #315: Regent LP Private Equity Media Consolidation and TechCrunch
Ownership Correction

DISCOVERY: MediaScope attributed TechCrunch's 2026 editorial patterns to
Yahoo/Apollo financial incentives (mechanisms #104, #142). TechCrunch was
SOLD by Yahoo to Regent LP in March 2025 — all 2026 TechCrunch articles
analyzed in MediaScope were published under Regent ownership, not Apollo.

Regent LP (Beverly Hills, CA, founded 2013, Michael Reinstein) consolidated
a major tech media empire through back-to-back March 2025 acquisitions:
1. Foundry (from Blackstone/IDG) — Macworld, PCWorld, InfoWorld,
   Computerworld, CIO, TechAdvisor, TechHive, CSO, NetworkWorld
2. TechCrunch (from Yahoo/Apollo) — deal announced Mar 21, 2025

The resulting architecture creates three-layer financial incentives:
- Foundry publications are Apple-ecosystem revenue dependent (affiliate
  commissions, Apple-adjacent advertising)
- TechCrunch's startup/VC coverage is core product, now under same PE
  roof as Apple-dependent publications
- Regent invested in Lovable ($400M Series C, $13.3B valuation, Aug 12, 2026)
  — an AI company TechCrunch covers, creating a documentable conflict

DISCLOSURE ASYMMETRY (verified Aug 12, 2026 Lovable coverage):
- TechCrunch: explicit footnote — "One of Lovable's new Series C investors
  is Regent, the investment firm that also owns TechCrunch." (FULL)
- Computerworld (Foundry): "Regent is the parent company of Foundry" —
  omitted TechCrunch co-ownership. (PARTIAL)
- Military Times (Sightline/Regent): published Regent's press release
  with zero conflict disclosure. (NONE)

Sources:
- https://techcrunch.com/2025/03/21/techcrunch-has-personal-news/
- https://siliconcanals.com/regent-acquires-techcrunch/
- https://www.thewrap.com/yahoo-sells-techcrunch-regent/
- https://techcrunch.com/2026/08/12/lovable-confirms-new-13-3b-valuation-raises-another-400m/
- https://www.computerworld.com/article/4208770/lovable-bolsters-its-ai-software-creation-capacity-touts-400m-funding-round.html
- https://www.militarytimes.com/press-release/2026/08/12/regent-invests-in-lovables-400-million-series-c/
- https://www.sahmcapital.com/news/content/scoop-blackstones-idg-nears-deal-to-sell-foundry-to-regent-axios-2025-01-24
- https://en.wikipedia.org/wiki/Regent_LP
"""

import unittest
import yaml
import os

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


def load_yaml(filename):
    filepath = os.path.join(PROFILES_DIR, filename)
    with open(filepath, 'r') as f:
        return yaml.safe_load(f)


class TestRegentLPEntityExists(unittest.TestCase):
    """Verify Regent LP is properly documented as a media conglomerate entity."""

    @classmethod
    def setUpClass(cls):
        cls.entities = load_yaml('competitor-entities.yaml')
        # Navigate to the regent_lp entry
        cls.regent = None
        if 'entities' in cls.entities:
            cls.regent = cls.entities['entities'].get('regent_lp')
        elif 'media_conglomerates' in cls.entities:
            cls.regent = cls.entities['media_conglomerates'].get('regent_lp')
        else:
            # Try finding it at any depth
            for key, val in cls.entities.items():
                if isinstance(val, dict):
                    if 'regent_lp' in val:
                        cls.regent = val['regent_lp']
                        break
                    for k2, v2 in val.items():
                        if isinstance(v2, dict) and 'regent_lp' in v2:
                            cls.regent = v2['regent_lp']
                            break

    def test_regent_lp_entity_exists(self):
        """Regent LP should exist as a documented entity."""
        self.assertIsNotNone(self.regent, "regent_lp entity missing from competitor-entities.yaml")

    def test_regent_display_name(self):
        """Display name should identify Regent LP and Michael Reinstein."""
        self.assertIn('Regent', self.regent.get('display_name', ''))

    def test_regent_category_is_pe_media(self):
        """Category should reflect PE media conglomerate status."""
        category = self.regent.get('category', '')
        self.assertIn('media', category.lower())

    def test_regent_founded_2013(self):
        """Regent LP was founded in 2013."""
        self.assertEqual(self.regent.get('founded'), 2013)

    def test_regent_headquarters_beverly_hills(self):
        """Regent LP is headquartered in Beverly Hills, California."""
        hq = self.regent.get('headquarters', '')
        self.assertIn('Beverly Hills', hq)


class TestRegentAcquisitionHistory(unittest.TestCase):
    """Verify Regent's media acquisition timeline is documented."""

    @classmethod
    def setUpClass(cls):
        cls.entities = load_yaml('competitor-entities.yaml')
        cls.regent = None
        for key, val in cls.entities.items():
            if isinstance(val, dict):
                if 'regent_lp' in val:
                    cls.regent = val['regent_lp']
                    break
                for k2, v2 in val.items():
                    if isinstance(v2, dict) and 'regent_lp' in v2:
                        cls.regent = v2['regent_lp']
                        break
        cls.acquisitions = cls.regent.get('acquisition_history', []) if cls.regent else []

    def test_sightline_acquisition_2016(self):
        """Sightline Media Group acquired from Tegna in 2016."""
        sightline = [a for a in self.acquisitions if 'Sightline' in a.get('entity', '')]
        self.assertTrue(len(sightline) >= 1, "Sightline Media Group acquisition not documented")
        self.assertEqual(sightline[0].get('year'), 2016)

    def test_cheddar_acquisition_2023(self):
        """CheddarTV acquired from Altice USA in 2023."""
        cheddar = [a for a in self.acquisitions if 'Cheddar' in a.get('entity', '')]
        self.assertTrue(len(cheddar) >= 1, "CheddarTV acquisition not documented")
        self.assertEqual(cheddar[0].get('year'), 2023)

    def test_foundry_acquisition_march_2025(self):
        """Foundry (IDG Communications) acquired from Blackstone in March 2025."""
        foundry = [a for a in self.acquisitions if 'Foundry' in a.get('entity', '')]
        self.assertTrue(len(foundry) >= 1, "Foundry acquisition not documented")
        self.assertEqual(foundry[0].get('year'), 2025)
        self.assertEqual(foundry[0].get('month'), 'March')

    def test_foundry_includes_macworld_pcworld(self):
        """Foundry acquisition should include Macworld and PCWorld."""
        foundry = [a for a in self.acquisitions if 'Foundry' in a.get('entity', '')]
        self.assertTrue(len(foundry) >= 1)
        pubs = foundry[0].get('publications', [])
        self.assertIn('Macworld', pubs)
        self.assertIn('PCWorld', pubs)

    def test_techcrunch_acquisition_march_2025(self):
        """TechCrunch acquired from Yahoo/Apollo in March 2025."""
        tc = [a for a in self.acquisitions if 'TechCrunch' in a.get('entity', '')]
        self.assertTrue(len(tc) >= 1, "TechCrunch acquisition not documented")
        self.assertEqual(tc[0].get('year'), 2025)
        self.assertIn('Yahoo', tc[0].get('source', ''))

    def test_yahoo_retained_interest(self):
        """Yahoo retained a small interest in TechCrunch after sale."""
        tc = [a for a in self.acquisitions if 'TechCrunch' in a.get('entity', '')]
        self.assertTrue(len(tc) >= 1)
        note = tc[0].get('note', '')
        self.assertTrue('small interest' in note.lower() or 'retained' in note.lower(),
                        "Yahoo's retained interest should be documented")


class TestTechCrunchOwnershipCorrection(unittest.TestCase):
    """Verify that TechCrunch ownership has been corrected from Yahoo/Apollo to Regent."""

    @classmethod
    def setUpClass(cls):
        cls.entities = load_yaml('competitor-entities.yaml')
        cls.yahoo = None
        for key, val in cls.entities.items():
            if isinstance(val, dict):
                if 'yahoo_apollo' in val:
                    cls.yahoo = val['yahoo_apollo']
                    break
                for k2, v2 in val.items():
                    if isinstance(v2, dict) and 'yahoo_apollo' in v2:
                        cls.yahoo = v2['yahoo_apollo']
                        break

    def test_techcrunch_not_in_yahoo_aliases(self):
        """TechCrunch should NOT be listed as a Yahoo/Apollo alias (sold Mar 2025)."""
        aliases = self.yahoo.get('aliases', [])
        self.assertNotIn('TechCrunch', aliases,
                         "TechCrunch was sold to Regent LP in March 2025, "
                         "should not be a Yahoo/Apollo alias")

    def test_techcrunch_not_in_yahoo_regex(self):
        """TechCrunch should NOT appear in Yahoo/Apollo regex pattern."""
        regex = self.yahoo.get('regex', '')
        self.assertNotIn('TechCrunch', regex,
                         "TechCrunch should be removed from Yahoo/Apollo regex")

    def test_ownership_correction_documented(self):
        """Yahoo/Apollo entry should document the TechCrunch ownership correction."""
        correction = self.yahoo.get('ownership_correction_aug26', {})
        self.assertIsNotNone(correction, "Ownership correction should be documented")
        self.assertEqual(correction.get('techcrunch_sold_to'), 'Regent LP')

    def test_correction_identifies_affected_mechanisms(self):
        """Correction should identify mechanisms #104 and #142 as affected."""
        correction = self.yahoo.get('ownership_correction_aug26', {})
        affected = correction.get('affected_mechanisms', [])
        self.assertIn(104, affected)
        self.assertIn(142, affected)

    def test_engadget_still_yahoo(self):
        """Engadget should STILL be listed under Yahoo/Apollo."""
        aliases = self.yahoo.get('aliases', [])
        self.assertIn('Engadget', aliases,
                      "Engadget was NOT sold — should remain under Yahoo/Apollo")


class TestRegentLovableAIInvestment(unittest.TestCase):
    """Verify Regent's AI investment in Lovable is documented."""

    @classmethod
    def setUpClass(cls):
        cls.entities = load_yaml('competitor-entities.yaml')
        cls.regent = None
        for key, val in cls.entities.items():
            if isinstance(val, dict):
                if 'regent_lp' in val:
                    cls.regent = val['regent_lp']
                    break
                for k2, v2 in val.items():
                    if isinstance(v2, dict) and 'regent_lp' in v2:
                        cls.regent = v2['regent_lp']
                        break
        cls.ai = cls.regent.get('ai_investments', {}) if cls.regent else {}
        cls.lovable = cls.ai.get('lovable', {})

    def test_lovable_investment_exists(self):
        """Regent's Lovable investment should be documented."""
        self.assertTrue(len(self.lovable) > 0, "Lovable investment entry missing")

    def test_lovable_date_august_2026(self):
        """Lovable investment was August 12, 2026."""
        self.assertEqual(self.lovable.get('date'), '2026-08-12')

    def test_lovable_series_c(self):
        """Investment was in Series C round."""
        self.assertEqual(self.lovable.get('round'), 'Series C')

    def test_lovable_round_size_400m(self):
        """Round size was $400 million."""
        self.assertEqual(self.lovable.get('round_size_m'), 400)

    def test_lovable_valuation_13_3b(self):
        """Lovable valuation was $13.3 billion."""
        self.assertAlmostEqual(self.lovable.get('valuation_b'), 13.3, places=1)


class TestDisclosureAsymmetry(unittest.TestCase):
    """
    Verify the disclosure asymmetry across Regent-owned publications covering
    Regent's own Lovable investment on the same day (Aug 12, 2026).
    """

    @classmethod
    def setUpClass(cls):
        cls.entities = load_yaml('competitor-entities.yaml')
        cls.regent = None
        for key, val in cls.entities.items():
            if isinstance(val, dict):
                if 'regent_lp' in val:
                    cls.regent = val['regent_lp']
                    break
                for k2, v2 in val.items():
                    if isinstance(v2, dict) and 'regent_lp' in v2:
                        cls.regent = v2['regent_lp']
                        break
        cls.lovable_sources = []
        if cls.regent:
            ai = cls.regent.get('ai_investments', {})
            lovable = ai.get('lovable', {})
            cls.lovable_sources = lovable.get('sources', [])

    def test_techcrunch_full_disclosure(self):
        """TechCrunch disclosed Regent ownership in Lovable coverage with explicit footnote."""
        tc_sources = [s for s in self.lovable_sources
                      if 'techcrunch.com' in s.get('url', '')]
        self.assertTrue(len(tc_sources) >= 1,
                        "TechCrunch Lovable coverage source missing")
        note = tc_sources[0].get('note', '')
        self.assertTrue('disclosed' in note.lower() or 'footnote' in note.lower(),
                        "TechCrunch's disclosure should be documented")

    def test_computerworld_partial_disclosure(self):
        """Computerworld disclosed Regent as Foundry parent but NOT TechCrunch co-ownership."""
        cw_sources = [s for s in self.lovable_sources
                      if 'computerworld.com' in s.get('url', '')]
        self.assertTrue(len(cw_sources) >= 1,
                        "Computerworld Lovable coverage source missing")
        note = cw_sources[0].get('note', '')
        self.assertTrue('partial' in note.lower() or 'omit' in note.lower()
                        or 'not mention' in note.lower(),
                        "Computerworld's partial disclosure should be documented")

    def test_military_times_no_disclosure(self):
        """Military Times published Regent press release with zero conflict disclosure."""
        mt_sources = [s for s in self.lovable_sources
                      if 'militarytimes.com' in s.get('url', '')]
        self.assertTrue(len(mt_sources) >= 1,
                        "Military Times Lovable press release source missing")
        note = mt_sources[0].get('note', '')
        self.assertTrue('absent' in note.lower() or 'zero' in note.lower()
                        or 'no' in note.lower(),
                        "Military Times lack of disclosure should be documented")

    def test_three_publications_three_disclosure_levels(self):
        """Three Regent-owned publications should show three different disclosure levels."""
        tc = [s for s in self.lovable_sources if 'techcrunch.com' in s.get('url', '')]
        cw = [s for s in self.lovable_sources if 'computerworld.com' in s.get('url', '')]
        mt = [s for s in self.lovable_sources if 'militarytimes.com' in s.get('url', '')]
        self.assertTrue(len(tc) >= 1 and len(cw) >= 1 and len(mt) >= 1,
                        "All three Regent publication sources should be documented")


class TestFinancialIncentiveArchitecture(unittest.TestCase):
    """Verify the three-layer financial incentive architecture is documented."""

    @classmethod
    def setUpClass(cls):
        cls.entities = load_yaml('competitor-entities.yaml')
        cls.regent = None
        for key, val in cls.entities.items():
            if isinstance(val, dict):
                if 'regent_lp' in val:
                    cls.regent = val['regent_lp']
                    break
                for k2, v2 in val.items():
                    if isinstance(v2, dict) and 'regent_lp' in v2:
                        cls.regent = v2['regent_lp']
                        break
        cls.architecture = cls.regent.get('financial_incentive_architecture', {}) if cls.regent else {}

    def test_cross_publication_alignment_documented(self):
        """Cross-publication alignment should be documented."""
        cpa = self.architecture.get('cross_publication_alignment', {})
        self.assertTrue(len(cpa) > 0, "Cross-publication alignment not documented")

    def test_apple_ecosystem_dependency_mentioned(self):
        """Apple-ecosystem revenue dependency should be identified."""
        cpa = self.architecture.get('cross_publication_alignment', {})
        desc = cpa.get('description', '')
        self.assertTrue('apple' in desc.lower(),
                        "Apple-ecosystem dependency should be documented")

    def test_ai_investment_conflict_mentioned(self):
        """AI investment conflict (Lovable) should be documented."""
        cpa = self.architecture.get('cross_publication_alignment', {})
        desc = cpa.get('description', '')
        self.assertTrue('lovable' in desc.lower() or 'ai investment' in desc.lower(),
                        "AI investment conflict should be documented")

    def test_disclosure_asymmetry_section_exists(self):
        """Disclosure asymmetry section should exist."""
        da = self.architecture.get('disclosure_asymmetry', {})
        self.assertTrue(len(da) > 0, "Disclosure asymmetry not documented")

    def test_techcrunch_ownership_correction_section(self):
        """TechCrunch ownership correction section should exist."""
        toc = self.architecture.get('techcrunch_ownership_correction', {})
        self.assertTrue(len(toc) > 0, "TechCrunch ownership correction not documented")

    def test_correction_lists_stale_and_correct_chains(self):
        """Correction should show both stale and correct ownership chains."""
        toc = self.architecture.get('techcrunch_ownership_correction', {})
        stale = toc.get('stale_ownership_chain', '')
        correct = toc.get('correct_ownership_chain', '')
        self.assertIn('Yahoo', stale)
        self.assertIn('Apollo', stale)
        self.assertIn('Regent', correct)


class TestRegentSources(unittest.TestCase):
    """Verify source documentation for Regent LP entity."""

    @classmethod
    def setUpClass(cls):
        cls.entities = load_yaml('competitor-entities.yaml')
        cls.regent = None
        for key, val in cls.entities.items():
            if isinstance(val, dict):
                if 'regent_lp' in val:
                    cls.regent = val['regent_lp']
                    break
                for k2, v2 in val.items():
                    if isinstance(v2, dict) and 'regent_lp' in v2:
                        cls.regent = v2['regent_lp']
                        break
        cls.sources = cls.regent.get('sources', []) if cls.regent else []

    def test_minimum_6_sources(self):
        """At least 6 sources should be cited."""
        self.assertGreaterEqual(len(self.sources), 6)

    def test_wikipedia_source(self):
        """Wikipedia source should be included."""
        wiki = [s for s in self.sources if 'wikipedia.org' in s.get('url', '')]
        self.assertTrue(len(wiki) >= 1)

    def test_techcrunch_announcement_source(self):
        """TechCrunch's own acquisition announcement should be cited."""
        tc = [s for s in self.sources if 'techcrunch.com/2025' in s.get('url', '')]
        self.assertTrue(len(tc) >= 1)

    def test_axios_scoop_source(self):
        """Axios scoop on Foundry sale should be cited."""
        axios = [s for s in self.sources
                 if 'foundry' in s.get('note', '').lower()
                 and ('axios' in s.get('note', '').lower()
                      or 'axios' in s.get('url', '').lower()
                      or 'sahmcapital' in s.get('url', '').lower())]
        self.assertTrue(len(axios) >= 1, "Axios scoop source missing")


if __name__ == '__main__':
    unittest.main()
