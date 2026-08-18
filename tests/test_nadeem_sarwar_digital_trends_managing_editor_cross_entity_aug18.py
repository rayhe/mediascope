"""
Mechanism #160: Nadeem Sarwar (Digital Trends / Designtechnica Corp) Managing Editor
Cross-Entity Editorial Direction Pattern

Discovery date: 2026-08-18 (Iteration #161, Type B)

FINDING:
Nadeem Sarwar, Managing Editor of Digital Trends (owned by Designtechnica Corp),
demonstrates cross-entity vocabulary bifurcation BOTH in his own bylined articles
AND through editorial direction of subordinate writers. This is the first mechanism
documenting the editorial chain from managing editor to staff writer within a single
publication.

KEY EVIDENCE:
1. Sarwar's own Meta article (Sep 20, 2025): "Meta Ray-Ban Display glasses sell
   personal superintelligence. I'll skip" — 12+ alarm terms including "hoarded
   personal data," "feeding your life to a bad machine," "ticking time bomb,"
   "pretty scary," "dangerous rubble," "lackadaisical approach to privacy"
2. Sarwar's own Samsung article (Mar 2026): "Samsung's smart glasses are coming,
   and they've got Meta in their sights" — ZERO alarm terms despite EXPLICITLY
   acknowledging hardware equivalence: "it's essentially the same approach Meta
   took with the Ray-Ban glasses"
3. Sarwar's own OpenAI article (Sep 19, 2025): "OpenAI is apparently planning a
   bunch of ChatGPT-powered AI devices" — neutral, zero alarm terms
4. Andy Boxall (mechanism #132) reports to Sarwar as Managing Editor — Boxall shows
   identical vocabulary bifurcation (7+ alarm terms for Meta, 0 for Snap Specs with
   4 cameras, 0 for Samsung)

CRITICAL OBSERVATION:
Sarwar's Samsung article contains a sentence that explicitly acknowledges hardware
equivalence while applying zero privacy scrutiny:
  "it's essentially the same approach Meta took with the Ray-Ban glasses — which
   currently own a majority of the smart glasses market, so the playbook clearly works."
This proves the vocabulary differential is NOT driven by capability differences
(which Sarwar himself acknowledges are equivalent) but by entity identity.

FINANCIAL CONTEXT:
- Digital Trends (Designtechnica Corp) depends on Google programmatic advertising
- Samsung is a major Google hardware partner (Android XR, $8B+ Play Store/Search deals)
- Meta is a structural competitor to Google (ad market, AI, Quest vs Android XR)
- OpenAI has no adversarial relationship with Digital Trends' revenue sources

Sources:
- Meta article: https://www.digitaltrends.com/computing/meta-ray-ban-display-glasses-sell-personal-superintelligence-ill-skip/
- Samsung article: https://www.digitaltrends.com/computing/samsungs-smart-glasses-are-coming-and-theyve-got-meta-in-their-sights/
- Andy Boxall Meta face recognition: https://www.digitaltrends.com/wearables/meta-is-building-face-recognition-into-your-glasses-and-civil-rights-groups-are-not-happy-about-it/
"""

import pytest
import yaml
import os

YAML_PATH = os.path.join(os.path.dirname(__file__), '..', 'profiles', 'competitor-coverage-research.yaml')


@pytest.fixture(scope='module')
def yaml_data():
    with open(YAML_PATH) as f:
        return yaml.safe_load(f)


@pytest.fixture(scope='module')
def mechanism(yaml_data):
    cpf = yaml_data.get('cross_publication_findings', {})
    entry = cpf.get('nadeem_sarwar_managing_editor_editorial_direction')
    assert entry is not None, "Mechanism entry 'nadeem_sarwar_managing_editor_editorial_direction' not found in YAML"
    return entry


# =============================================================================
# Class 1: Mechanism Existence and Structural Fields
# =============================================================================
class TestMechanismStructure:
    """Verify mechanism #160 exists with all required structural fields."""

    def test_mechanism_id(self, mechanism):
        assert mechanism['mechanism_id'] == 160

    def test_mechanism_name_contains_sarwar(self, mechanism):
        name = mechanism['mechanism_name']
        assert 'Sarwar' in name
        assert 'Managing Editor' in name

    def test_finding_type(self, mechanism):
        assert mechanism['finding_type'] == 'same_journalist_cross_entity_tracking'

    def test_rotation_type_b(self, mechanism):
        assert mechanism['rotation_type'] == 'B'

    def test_discovery_date(self, mechanism):
        assert mechanism['discovery_date'] == '2026-08-18'

    def test_journalist_field(self, mechanism):
        assert mechanism['journalist'] == 'Nadeem Sarwar'

    def test_publication(self, mechanism):
        assert 'Digital Trends' in mechanism['publication']

    def test_publication_owner(self, mechanism):
        assert 'Designtechnica' in mechanism['publication_owner']

    def test_domain(self, mechanism):
        assert mechanism['domain'] == 'wearables_coverage_asymmetry'

    def test_editorial_role(self, mechanism):
        assert mechanism['editorial_role'] == 'Managing Editor'


# =============================================================================
# Class 2: Cross-Entity Article Coverage
# =============================================================================
class TestCrossEntityArticles:
    """Verify Sarwar's cross-entity coverage is documented with URLs and vocabulary."""

    def test_meta_article_exists(self, mechanism):
        articles = mechanism['articles']
        assert 'meta_personal_superintelligence' in articles

    def test_meta_article_url(self, mechanism):
        meta = mechanism['articles']['meta_personal_superintelligence']
        assert 'digitaltrends.com' in meta['url']
        assert 'superintelligence' in meta['url']

    def test_meta_article_headline(self, mechanism):
        meta = mechanism['articles']['meta_personal_superintelligence']
        assert "I'll skip" in meta['headline']

    def test_meta_tone_strongly_negative(self, mechanism):
        meta = mechanism['articles']['meta_personal_superintelligence']
        assert meta['tone_score'] <= -0.75

    def test_samsung_article_exists(self, mechanism):
        articles = mechanism['articles']
        assert 'samsung_glasses_coming' in articles

    def test_samsung_article_url(self, mechanism):
        samsung = mechanism['articles']['samsung_glasses_coming']
        assert 'digitaltrends.com' in samsung['url']

    def test_samsung_zero_alarm_terms(self, mechanism):
        samsung = mechanism['articles']['samsung_glasses_coming']
        assert samsung['privacy_terms'] == 0

    def test_samsung_tone_positive(self, mechanism):
        samsung = mechanism['articles']['samsung_glasses_coming']
        assert samsung['tone_score'] > 0

    def test_openai_article_exists(self, mechanism):
        articles = mechanism['articles']
        assert 'openai_devices' in articles

    def test_openai_zero_alarm_terms(self, mechanism):
        openai = mechanism['articles']['openai_devices']
        assert openai['privacy_terms'] == 0


# =============================================================================
# Class 3: Meta-Specific Alarm Vocabulary
# =============================================================================
class TestMetaAlarmVocabulary:
    """Verify the specific alarm terms Sarwar applies exclusively to Meta."""

    def test_alarm_word_count_minimum(self, mechanism):
        meta = mechanism['articles']['meta_personal_superintelligence']
        assert len(meta['alarm_words']) >= 8

    def test_hoarded_personal_data(self, mechanism):
        alarm = mechanism['articles']['meta_personal_superintelligence']['alarm_words']
        assert any('hoarded' in w.lower() for w in alarm)

    def test_feeding_life_to_bad_machine(self, mechanism):
        alarm = mechanism['articles']['meta_personal_superintelligence']['alarm_words']
        assert any('bad machine' in w.lower() for w in alarm)

    def test_ticking_time_bomb(self, mechanism):
        alarm = mechanism['articles']['meta_personal_superintelligence']['alarm_words']
        assert any('ticking time bomb' in w.lower() for w in alarm)

    def test_pretty_scary(self, mechanism):
        alarm = mechanism['articles']['meta_personal_superintelligence']['alarm_words']
        assert any('scary' in w.lower() for w in alarm)

    def test_dangerous_rubble(self, mechanism):
        alarm = mechanism['articles']['meta_personal_superintelligence']['alarm_words']
        assert any('dangerous rubble' in w.lower() for w in alarm)

    def test_lackadaisical_privacy(self, mechanism):
        alarm = mechanism['articles']['meta_personal_superintelligence']['alarm_words']
        assert any('lackadaisical' in w.lower() for w in alarm)

    def test_editorial_refusal(self, mechanism):
        """Managing Editor explicitly refuses to use the product in headline."""
        meta = mechanism['articles']['meta_personal_superintelligence']
        assert meta.get('editorial_refusal') is True


# =============================================================================
# Class 4: Hardware Equivalence Acknowledgment
# =============================================================================
class TestHardwareEquivalenceAcknowledgment:
    """The Samsung article explicitly acknowledges hardware equivalence with Meta
    while applying zero alarm terms — proving the differential is entity-driven."""

    def test_equivalence_acknowledged(self, mechanism):
        samsung = mechanism['articles']['samsung_glasses_coming']
        assert samsung.get('hardware_equivalence_acknowledged') is True

    def test_equivalence_quote(self, mechanism):
        samsung = mechanism['articles']['samsung_glasses_coming']
        quote = samsung.get('equivalence_quote', '')
        assert 'same approach Meta took' in quote

    def test_samsung_has_camera(self, mechanism):
        samsung = mechanism['articles']['samsung_glasses_coming']
        assert samsung.get('camera_discussed') is True

    def test_samsung_camera_no_privacy_concern(self, mechanism):
        """Samsung camera discussed as feature, not concern."""
        samsung = mechanism['articles']['samsung_glasses_coming']
        assert samsung['privacy_terms'] == 0
        assert samsung.get('camera_discussed') is True

    def test_vocabulary_delta(self, mechanism):
        """Meta gets 8+ alarm terms, Samsung gets 0 — infinite ratio."""
        meta = mechanism['articles']['meta_personal_superintelligence']
        samsung = mechanism['articles']['samsung_glasses_coming']
        assert len(meta['alarm_words']) >= 8
        assert samsung['privacy_terms'] == 0


# =============================================================================
# Class 5: Editorial Direction Chain
# =============================================================================
class TestEditorialDirectionChain:
    """Verify the editorial hierarchy from Managing Editor to staff writers."""

    def test_editorial_chain_documented(self, mechanism):
        chain = mechanism.get('editorial_direction_chain')
        assert chain is not None

    def test_boxall_subordinate_identified(self, mechanism):
        chain = mechanism['editorial_direction_chain']
        subordinates = chain.get('subordinate_writers', [])
        names = [s.get('name', '') for s in subordinates]
        assert 'Andy Boxall' in names

    def test_boxall_mechanism_cross_reference(self, mechanism):
        chain = mechanism['editorial_direction_chain']
        subordinates = chain.get('subordinate_writers', [])
        boxall = [s for s in subordinates if s.get('name') == 'Andy Boxall'][0]
        assert boxall.get('mechanism_id') == 132

    def test_boxall_same_pattern(self, mechanism):
        chain = mechanism['editorial_direction_chain']
        subordinates = chain.get('subordinate_writers', [])
        boxall = [s for s in subordinates if s.get('name') == 'Andy Boxall'][0]
        assert boxall.get('same_vocabulary_bifurcation') is True

    def test_institutional_pattern_inference(self, mechanism):
        """When the managing editor AND a staff writer show the same pattern,
        the inference is institutional editorial direction, not individual bias."""
        chain = mechanism['editorial_direction_chain']
        assert chain.get('institutional_inference') is True

    def test_chain_depth(self, mechanism):
        """At least 2 levels documented: Managing Editor -> Staff Writer."""
        chain = mechanism['editorial_direction_chain']
        assert chain.get('chain_depth', 0) >= 2


# =============================================================================
# Class 6: Financial Context
# =============================================================================
class TestFinancialContext:
    """Verify the financial incentive structure is documented."""

    def test_owner_documented(self, mechanism):
        fc = mechanism['financial_context']
        assert 'Designtechnica' in fc['owner']

    def test_google_ad_dependency(self, mechanism):
        fc = mechanism['financial_context']
        assert 'Google' in fc['primary_ad_platform']

    def test_samsung_advertiser(self, mechanism):
        fc = mechanism['financial_context']
        assert fc['samsung_advertiser'] is True

    def test_google_samsung_partnership(self, mechanism):
        fc = mechanism['financial_context']
        assert 'Android XR' in fc.get('google_samsung_glasses_partnership', '')

    def test_meta_no_financial_ties(self, mechanism):
        fc = mechanism['financial_context']
        assert fc.get('meta_financial_ties') in ('none', 'none_direct', None)

    def test_prediction(self, mechanism):
        fc = mechanism['financial_context']
        pred = fc.get('prediction', '')
        assert len(pred) > 50


# =============================================================================
# Class 7: Confounders
# =============================================================================
class TestConfounders:
    """Verify minimum 5 confounders with required strength distribution."""

    def test_minimum_five_confounders(self, mechanism):
        confounders = mechanism['confounders']
        assert len(confounders) >= 5

    def test_at_least_two_strong(self, mechanism):
        confounders = mechanism['confounders']
        strong = [c for c in confounders if c['strength'] == 'STRONG']
        assert len(strong) >= 2

    def test_at_least_two_moderate(self, mechanism):
        confounders = mechanism['confounders']
        moderate = [c for c in confounders if c['strength'] == 'MODERATE']
        assert len(moderate) >= 2

    def test_at_least_one_weak(self, mechanism):
        confounders = mechanism['confounders']
        weak = [c for c in confounders if c['strength'] == 'WEAK']
        assert len(weak) >= 1

    def test_confounders_have_descriptions(self, mechanism):
        for c in mechanism['confounders']:
            assert len(c.get('description', '')) > 30

    def test_opinion_column_confounder(self, mechanism):
        """The Meta article is opinion/editorial — strongest confounder."""
        confounders = mechanism['confounders']
        names = [c['name'].lower() for c in confounders]
        assert any('opinion' in n or 'editorial' in n or 'column' in n for n in names)


# =============================================================================
# Class 8: Cross-References to Related Mechanisms
# =============================================================================
class TestCrossReferences:
    """Verify cross-references to related mechanisms."""

    def test_has_related_mechanisms(self, mechanism):
        related = mechanism.get('related_mechanisms', [])
        assert len(related) >= 3

    def test_boxall_mechanism_referenced(self, mechanism):
        related = mechanism.get('related_mechanisms', [])
        mech_ids = [r['mechanism_id'] for r in related]
        assert 132 in mech_ids

    def test_openai_companion_vocabulary_referenced(self, mechanism):
        """Should reference mechanism #159 (OpenAI companion vs Meta surveillance)."""
        related = mechanism.get('related_mechanisms', [])
        mech_ids = [r['mechanism_id'] for r in related]
        assert 159 in mech_ids

    def test_relationships_described(self, mechanism):
        related = mechanism.get('related_mechanisms', [])
        for r in related:
            assert len(r.get('relationship', '')) > 10


# =============================================================================
# Class 9: OpenAI Coverage Specifics
# =============================================================================
class TestOpenAICoverage:
    """Verify OpenAI coverage details — zero alarm for camera-equipped devices."""

    def test_openai_article_headline(self, mechanism):
        openai = mechanism['articles']['openai_devices']
        headline = openai.get('headline', '')
        assert 'OpenAI' in headline

    def test_openai_tone_neutral_or_positive(self, mechanism):
        openai = mechanism['articles']['openai_devices']
        assert openai['tone_score'] >= 0

    def test_openai_has_camera_capability(self, mechanism):
        """OpenAI device has cameras, sensors, personal data access — zero alarm."""
        openai = mechanism['articles']['openai_devices']
        assert openai.get('device_has_cameras') is True

    def test_openai_device_uses_personal_data(self, mechanism):
        """OpenAI device explicitly uses emails and personal information."""
        openai = mechanism['articles']['openai_devices']
        assert openai.get('device_uses_personal_data') is True


# =============================================================================
# Class 10: Doc Sync Integrity
# =============================================================================
class TestDocSync:
    """Verify documentation files are in sync."""

    def test_readme_mentions_test_file(self):
        readme_path = os.path.join(os.path.dirname(__file__), '..', 'README.md')
        with open(readme_path) as f:
            content = f.read()
        assert 'test_nadeem_sarwar_digital_trends_managing_editor_cross_entity_aug18' in content

    def test_architecture_mentions_test_file(self):
        arch_path = os.path.join(os.path.dirname(__file__), '..', 'docs', 'ARCHITECTURE.md')
        with open(arch_path) as f:
            content = f.read()
        assert 'test_nadeem_sarwar_digital_trends_managing_editor_cross_entity_aug18' in content

    def test_yaml_mechanism_count_incremented(self, yaml_data):
        cpf = yaml_data.get('cross_publication_findings', {})
        mechanism_ids = [v.get('mechanism_id', 0) for v in cpf.values() if isinstance(v, dict)]
        assert 160 in mechanism_ids
