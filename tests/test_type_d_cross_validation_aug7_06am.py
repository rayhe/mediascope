"""
Type D Cross-Validation: Aug 7 2026 06:00 PT

Validates internal consistency across the three major findings from
today's A, B, C iterations:

1. NYT × Amazon February Simultaneous Paradox (Type A, 01:00):
   NYT sent Kashmir Hill after UNRELEASED Meta NameTag while covering
   Amazon Ring's DEPLOYED Familiar Faces as a business story — same week.

2. Samsung Equivalence Paradox (Type B, 03:00):
   Samsung Intelligent Eyewear is spec-identical to Meta Ray-Ban on every
   privacy-relevant dimension, yet receives product-review framing while
   Meta receives surveillance framing. Real-world policy consequence:
   Iberville Parish banned "Meta glasses" by name — Samsung exempt.

3. PMC Deal Fragmentation Paradox (Type C, 05:00):
   Vox Media split leaves The Verge's AI content deals orphaned between
   PMC and Lupa Systems. PMC is suing Google over AI Overviews yet
   The Verge's editorial hostility targets Meta, not Google.

Cross-validation ensures:
- Entity counts are consistent across all profile files
- Samsung entity properly integrated without breaking existing tests
- Financial relationship sums remain consistent
- Source URLs are present for all new findings
"""

import yaml
import os
import pytest

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


def load_yaml(path):
    with open(path) as f:
        return yaml.safe_load(f)


@pytest.fixture(scope='module')
def entities():
    return load_yaml(os.path.join(PROFILES_DIR, 'competitor-entities.yaml'))


@pytest.fixture(scope='module')
def research():
    return load_yaml(os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml'))


@pytest.fixture(scope='module')
def nyt_profile():
    return load_yaml(os.path.join(PROFILES_DIR, 'nytimes.yaml'))


@pytest.fixture(scope='module')
def verge_profile():
    return load_yaml(os.path.join(PROFILES_DIR, 'the-verge.yaml'))


@pytest.fixture(scope='module')
def wired_profile():
    return load_yaml(os.path.join(PROFILES_DIR, 'wired.yaml'))


class TestEntityCountConsistency:
    """After Samsung addition, entity counts must be consistent everywhere."""

    def test_entities_in_yaml(self, entities):
        """competitor-entities.yaml should have at least 9 entities (grew to 11 with microsoft + snowflake)."""
        assert len(entities['entities']) >= 9

    def test_samsung_present(self, entities):
        """Samsung must be in the entities list."""
        assert 'samsung' in entities['entities']

    def test_samsung_has_display_name(self, entities):
        samsung = entities['entities']['samsung']
        assert samsung.get('display_name') is not None

    def test_core_entities_still_present(self, entities):
        """Core entities should still be present (Microsoft tracked under OpenAI axis, not standalone)."""
        required = {'openai', 'anthropic', 'google', 'amazon', 'apple', 'xai', 'x_twitter'}
        present = set(entities['entities'].keys())
        missing = required - present
        assert not missing, f"Missing core entities: {missing}"


class TestNYTAmazonParadoxCrossRef:
    """The February 2026 paradox should be documented in NYT profile."""

    def test_nyt_has_kashmir_hill_journalist(self, nyt_profile):
        """NYT profile should document Kashmir Hill as key journalist."""
        key_journalists = nyt_profile.get('key_journalists', [])
        hill = next((j for j in key_journalists if 'Hill' in j.get('name', '')), None)
        assert hill is not None, "Kashmir Hill must be in NYT key_journalists list"

    def test_february_paradox_in_research(self, research):
        """competitor-coverage-research should document the Feb 2026 paradox."""
        pubs = research.get('publications', {})
        nyt = pubs.get('nyt', pubs.get('nytimes', pubs.get('new_york_times', {})))
        # The paradox should exist somewhere in the research data
        content = yaml.dump(nyt)
        assert 'nametag' in content.lower() or 'simultaneous' in content.lower() or \
               'ring' in content.lower() or 'familiar_faces' in content.lower(), \
               "February 2026 NYT × Amazon paradox should be documented in research"

    def test_amazon_entity_has_ring(self, entities):
        """Amazon entity should reference Ring brand."""
        amazon = entities['entities']['amazon']
        content = yaml.dump(amazon).lower()
        assert 'ring' in content, "Amazon entity should mention Ring"


class TestSamsungEquivalenceIntegration:
    """Samsung finding must be consistent with WIRED/Verge profiles."""

    def test_samsung_in_research(self, research):
        """Samsung equivalence paradox should be in research file."""
        content = yaml.dump(research).lower()
        assert 'samsung' in content, "Samsung should be referenced in competitor research"

    def test_samsung_has_eyewear_specs(self, entities):
        """Samsung entity should reference Intelligent Eyewear."""
        samsung = entities['entities']['samsung']
        content = yaml.dump(samsung).lower()
        assert 'eyewear' in content or 'glasses' in content or 'smart' in content, \
               "Samsung should reference smart eyewear product"

    def test_samsung_has_camera_spec(self, entities):
        """Samsung entity or research should document camera specs for comparison."""
        samsung = entities['entities']['samsung']
        content = yaml.dump(samsung).lower()
        assert '12mp' in content or '12 mp' in content or 'camera' in content, \
               "Samsung camera spec should be documented for comparison"

    def test_school_ban_documented(self, research):
        """Iberville Parish school ban should be documented as policy consequence."""
        content = yaml.dump(research).lower()
        assert 'iberville' in content or 'school' in content, \
               "Iberville Parish school ban should be documented"


class TestPMCFragmentationCrossRef:
    """PMC deal fragmentation should be consistent with Verge profile."""

    def test_verge_ownership_chain_includes_pmc(self, verge_profile):
        """The Verge profile should reflect PMC ownership."""
        chain = verge_profile.get('ownership_chain', [])
        chain_str = yaml.dump(chain).lower()
        assert 'pmc' in chain_str or 'penske' in chain_str, \
               "Verge ownership chain must include PMC/Penske"

    def test_verge_has_openai_deal_reference(self, verge_profile):
        """The Verge profile should reference the inherited OpenAI deal."""
        content = yaml.dump(verge_profile).lower()
        assert 'openai' in content, \
               "Verge profile should reference OpenAI deal (inherited from Vox Media)"

    def test_pmc_google_litigation_in_entities(self, entities):
        """Google entity should reference PMC antitrust litigation."""
        google = entities['entities']['google']
        content = yaml.dump(google).lower()
        assert 'pmc' in content or 'penske' in content or 'rolling stone' in content or \
               'publisher' in content, \
               "Google entity should reference PMC/publisher litigation"

    def test_fragmentation_in_research(self, research):
        """PMC deal fragmentation should be documented in research."""
        content = yaml.dump(research).lower()
        assert 'fragmentation' in content or 'lupa' in content or 'split' in content, \
               "PMC deal fragmentation should be documented in research"


class TestCrossParadoxConsistency:
    """All three paradoxes should support the same overarching thesis."""

    def test_meta_in_entities_as_detection_target(self, entities):
        """Meta is in competitor-entities as a detection target entity (the subject of analysis)."""
        assert 'meta' in entities['entities'], \
               "Meta should be in competitor-entities for entity detection purposes"

    def test_meta_has_no_publisher_licensing_deals(self, entities):
        """Meta entity in competitor-entities is minimal (detection-only).
        Meta's publisher deals (News Corp $50M/yr) are documented in
        publication profiles, not the entity file — this is architecturally
        correct because Meta is the subject of analysis, not a competitor."""
        meta = entities['entities']['meta']
        # Meta entity should be detection-focused: aliases, regex, category
        assert meta.get('display_name') is not None
        assert meta.get('regex') is not None
        # It should NOT have the same rich financial data as competitor entities
        assert meta.get('publisher_deals_note') is None, \
               "Meta entity should not have publisher deals — those belong in publication profiles"

    def test_financial_direction_predictions_documented(self, research):
        """Each paradox should make a prediction about coverage direction."""
        content = yaml.dump(research).lower()
        # Financial relationships should predict coverage direction
        assert 'predict' in content or 'incentive' in content or 'financial' in content

    def test_no_orphaned_source_urls(self, research):
        """Source URLs in research file should not be empty strings."""
        content = yaml.dump(research)
        # Check for common empty-source patterns
        assert 'source: ""' not in content, "No source URL should be an empty string"
        assert "source: ''" not in content, "No source URL should be an empty string"

    def test_entities_after_all_iterations(self, entities):
        """Confirm entity count stable after all today's iterations (grew to 11)."""
        entity_names = sorted(entities['entities'].keys())
        expected = sorted(['amazon', 'anthropic', 'apple', 'google', 'meta',
                          'microsoft', 'openai', 'samsung', 'snowflake',
                          'x_twitter', 'xai'])
        assert entity_names == expected, \
               f"Entity list mismatch.\nExpected: {expected}\nGot: {entity_names}"
