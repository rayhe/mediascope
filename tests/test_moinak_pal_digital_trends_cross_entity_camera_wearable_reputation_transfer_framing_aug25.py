"""
Test Moinak Pal (Digital Trends) Cross-Entity Camera Wearable
Reputation Transfer Framing — Mechanism #301

Type B: Journalist Cross-Entity Tracking

Moinak Pal covers smart glasses for Digital Trends across Meta, Apple,
Samsung, and Google. The cross-entity vocabulary pattern shows Apple's
identical recording indicator LED framed as the *solution* to Meta's
*problem*, creating a hero/villain dyad from identical hardware.

Key natural experiment: Meta and Apple both use/will use LED recording
indicators on camera-equipped glasses. Meta's existing implementation
is framed as inadequate ("creepy reputation"), Apple's planned version
is framed as innovative ("solve trust through design").

Articles analyzed:
- "Apple smart glasses might avoid the creepy reputation of Meta Ray-Bans
  with a light trick" (Apr 12, 2026)
- "If you own Meta smart glasses then you may be banned from courts soon"
  (~Aug 21, 2026)
- "Meta is building face recognition into your glasses, and civil rights
  groups are not happy about it" (Apr 14, 2026)
- "Meta's latest surveillance plans are so dystopian that I am out of
  words" (Apr 22, 2026)
- Samsung Intelligent Eyewear launch coverage (Jul 22, 2026) — zero
  privacy vocabulary

Mechanism #301 in profiles/competitor-coverage-research.yaml
"""

import os
import yaml
import pytest


PROFILES_DIR = os.path.join(
    os.path.dirname(__file__), '..', 'profiles'
)


@pytest.fixture
def competitor_research():
    path = os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml')
    with open(path) as f:
        return yaml.safe_load(f)


@pytest.fixture
def publications():
    result = {}
    for fname in os.listdir(PROFILES_DIR):
        if fname.endswith('.yaml') and fname not in (
            '_template.yaml', 'competitor-entities.yaml',
            'competitor-coverage-research.yaml',
            'advocacy-coalitions.yaml',
            'instagram-accounts.yaml',
        ):
            path = os.path.join(PROFILES_DIR, fname)
            with open(path) as f:
                result[fname] = yaml.safe_load(f)
    return result


class TestMechanismStructure:
    """Verify mechanism #301 exists with required fields."""

    def test_mechanism_exists(self, competitor_research):
        mechs = competitor_research.get('publications', {})
        found = False
        for key, val in mechs.items():
            if isinstance(val, dict) and val.get('mechanism_id') == 301:
                found = True
                break
        assert found, "Mechanism #301 not found"

    def test_mechanism_has_journalist(self, competitor_research):
        mechs = competitor_research.get('publications', {})
        for key, val in mechs.items():
            if isinstance(val, dict) and val.get('mechanism_id') == 301:
                desc = str(val.get('description', '')).lower()
                assert 'moinak pal' in desc

    def test_mechanism_has_publication(self, competitor_research):
        mechs = competitor_research.get('publications', {})
        for key, val in mechs.items():
            if isinstance(val, dict) and val.get('mechanism_id') == 301:
                desc = str(val.get('description', '')).lower()
                assert 'digital trends' in desc

    def test_mechanism_has_sources(self, competitor_research):
        mechs = competitor_research.get('publications', {})
        for key, val in mechs.items():
            if isinstance(val, dict) and val.get('mechanism_id') == 301:
                sources = val.get('sources', [])
                assert len(sources) >= 3

    def test_mechanism_has_confounders(self, competitor_research):
        mechs = competitor_research.get('publications', {})
        for key, val in mechs.items():
            if isinstance(val, dict) and val.get('mechanism_id') == 301:
                confounders = val.get('confounders', [])
                assert len(confounders) >= 2

    def test_mechanism_has_cross_references(self, competitor_research):
        mechs = competitor_research.get('publications', {})
        for key, val in mechs.items():
            if isinstance(val, dict) and val.get('mechanism_id') == 301:
                xrefs = val.get('cross_references', [])
                assert len(xrefs) >= 1

    def test_mechanism_has_test_file(self, competitor_research):
        mechs = competitor_research.get('publications', {})
        for key, val in mechs.items():
            if isinstance(val, dict) and val.get('mechanism_id') == 301:
                tf = val.get('test_file', '')
                assert 'moinak_pal' in tf


class TestReputationTransferFraming:
    """Verify the core finding: identical features framed oppositely."""

    def test_meta_creepy_vocabulary_present(self, competitor_research):
        """Meta coverage uses alarm vocabulary."""
        mechs = competitor_research.get('publications', {})
        for key, val in mechs.items():
            if isinstance(val, dict) and val.get('mechanism_id') == 301:
                desc = str(val.get('description', '')).lower()
                assert 'creepy' in desc

    def test_apple_hero_vocabulary_present(self, competitor_research):
        """Apple coverage uses aspirational vocabulary."""
        mechs = competitor_research.get('publications', {})
        for key, val in mechs.items():
            if isinstance(val, dict) and val.get('mechanism_id') == 301:
                desc = str(val.get('description', '')).lower()
                assert any(term in desc for term in [
                    'solve trust', 'avoid', 'hero', 'solution'
                ])

    def test_samsung_zero_privacy_vocabulary(self, competitor_research):
        """Samsung camera glasses receive zero privacy scrutiny."""
        mechs = competitor_research.get('publications', {})
        for key, val in mechs.items():
            if isinstance(val, dict) and val.get('mechanism_id') == 301:
                desc = str(val.get('description', '')).lower()
                assert 'samsung' in desc
                assert 'zero' in desc or 'no privacy' in desc

    def test_led_natural_experiment_documented(self, competitor_research):
        """LED recording indicator natural experiment is documented."""
        mechs = competitor_research.get('publications', {})
        for key, val in mechs.items():
            if isinstance(val, dict) and val.get('mechanism_id') == 301:
                desc = str(val.get('description', '')).lower()
                assert 'led' in desc or 'recording indicator' in desc or 'light' in desc


class TestHeadlineEntitySelection:
    """Verify headline patterns target Meta specifically."""

    def test_court_ban_entity_specificity(self, competitor_research):
        """UK court ban applies to all camera glasses but headline names Meta."""
        mechs = competitor_research.get('publications', {})
        for key, val in mechs.items():
            if isinstance(val, dict) and val.get('mechanism_id') == 301:
                sources = [str(s) for s in val.get('sources', [])]
                court_sources = [s for s in sources if 'court' in s.lower() or 'ban' in s.lower()]
                assert len(court_sources) >= 1

    def test_apple_headline_positions_as_solution(self, competitor_research):
        """Apple headline frames the same feature as Meta's fix."""
        mechs = competitor_research.get('publications', {})
        for key, val in mechs.items():
            if isinstance(val, dict) and val.get('mechanism_id') == 301:
                sources = [str(s) for s in val.get('sources', [])]
                apple_sources = [s for s in sources if 'apple' in s.lower() and 'creepy' in s.lower()]
                assert len(apple_sources) >= 1

    def test_meta_headlines_use_alarm_framing(self, competitor_research):
        """Meta headlines carry alarm/negative vocabulary."""
        mechs = competitor_research.get('publications', {})
        for key, val in mechs.items():
            if isinstance(val, dict) and val.get('mechanism_id') == 301:
                sources = [str(s) for s in val.get('sources', [])]
                alarm_meta = [s for s in sources if any(
                    term in s.lower() for term in ['dystopian', 'surveillance', 'stalker', 'creepy', 'banned']
                )]
                assert len(alarm_meta) >= 2


class TestVocabularyInventory:
    """Cross-entity vocabulary counts."""

    def test_meta_alarm_term_count(self, competitor_research):
        """Meta receives multiple distinct alarm terms."""
        mechs = competitor_research.get('publications', {})
        for key, val in mechs.items():
            if isinstance(val, dict) and val.get('mechanism_id') == 301:
                desc = str(val.get('description', ''))
                meta_terms = ['creepy', 'dystopian', 'surveillance', 'banned',
                              'stalker', 'covert', 'deceptive', 'misused']
                found = sum(1 for t in meta_terms if t.lower() in desc.lower())
                assert found >= 4, f"Only {found} Meta alarm terms found"

    def test_apple_aspirational_term_count(self, competitor_research):
        """Apple receives aspirational/solution vocabulary."""
        mechs = competitor_research.get('publications', {})
        for key, val in mechs.items():
            if isinstance(val, dict) and val.get('mechanism_id') == 301:
                desc = str(val.get('description', ''))
                apple_terms = ['solve', 'trust', 'design', 'refining',
                               'innovative', 'approach', 'avoid']
                found = sum(1 for t in apple_terms if t.lower() in desc.lower())
                assert found >= 3, f"Only {found} Apple aspirational terms found"

    def test_samsung_vocabulary_is_neutral(self, competitor_research):
        """Samsung coverage vocabulary is product-neutral."""
        mechs = competitor_research.get('publications', {})
        for key, val in mechs.items():
            if isinstance(val, dict) and val.get('mechanism_id') == 301:
                desc = str(val.get('description', ''))
                samsung_terms = ['intelligent eyewear', 'ai glasses race',
                                 'translation', 'navigation']
                found = sum(1 for t in samsung_terms if t.lower() in desc.lower())
                assert found >= 1


class TestConfounders:
    """Verify confounders are documented honestly."""

    def test_meta_market_leader_confounder(self, competitor_research):
        """Documents that Meta is the market leader (more scrutiny expected)."""
        mechs = competitor_research.get('publications', {})
        for key, val in mechs.items():
            if isinstance(val, dict) and val.get('mechanism_id') == 301:
                confounders = val.get('confounders', [])
                confounder_text = ' '.join(str(c) for c in confounders).lower()
                assert 'market' in confounder_text or 'leader' in confounder_text

    def test_apple_not_yet_shipped_confounder(self, competitor_research):
        """Documents that Apple glasses haven't shipped yet."""
        mechs = competitor_research.get('publications', {})
        for key, val in mechs.items():
            if isinstance(val, dict) and val.get('mechanism_id') == 301:
                confounders = val.get('confounders', [])
                confounder_text = ' '.join(str(c) for c in confounders).lower()
                assert any(term in confounder_text for term in [
                    'not yet', 'unreleased', 'pre-launch', 'shipped', 'available'
                ])


class TestCrossReferences:
    """Verify cross-references to related mechanisms."""

    def test_references_digital_trends_editorial_level(self, competitor_research):
        """Should reference the existing DT editorial-level analysis."""
        mechs = competitor_research.get('publications', {})
        for key, val in mechs.items():
            if isinstance(val, dict) and val.get('mechanism_id') == 301:
                xrefs = val.get('cross_references', [])
                xref_ids = [x.get('mechanism_id') for x in xrefs if isinstance(x, dict)]
                # Should reference at least one existing mechanism
                assert len(xref_ids) >= 1
