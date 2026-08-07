"""
Tests for Will Douglas Heaven (MIT Technology Review) cross-entity coverage analysis.

Validates that WDH's coverage — as MIT TR's executive editor for AI with a PhD in
Computer Science — demonstrates systematic framing asymmetry across company coverage:
OpenAI receives exclusive insider access and constructive framing, Google DeepMind
receives demo enthusiasm and capability celebration, while Meta receives external
failure narration and mortality language for comparable technical events.

Key findings:
1. SOURCE ACCESS ASYMMETRY: Exclusive interview with OpenAI chief scientist Pachocki,
   private demo access to Google DeepMind's Mariner, ZERO documented exclusive Meta
   access. LeCun Paris meeting was group event covered by Heikkilä, not WDH.
2. FAILURE FRAMING DOUBLE STANDARD: Meta's Galactica retraction = "survived only three
   days" (mortality language). Google's Mariner getting stuck = "remarkable moment"
   (intelligence celebration). OpenAI's agent breach = scholarly "specification gaming"
   normalization. Same phenomenon (technical hiccup), opposite frames.
3. BREAKTHROUGH ATTRIBUTION: Anthropic's mechanistic interpretability on "10 Breakthrough
   Technologies" list, despite Meta's open-weight Llama enabling MORE external
   interpretability research. Proprietary introspection credited over open transparency.
4. FINANCIAL CORRELATION: MIT has bilateral programs with Google, Apple CSAIL membership,
   possible OpenAI content relationship — zero documented Meta institutional ties.
   Coverage warmth aligns with institutional relationship depth.
"""

import yaml
import pytest
import os

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


@pytest.fixture
def mit_tr():
    with open(os.path.join(PROFILES_DIR, 'mit-tech-review.yaml')) as f:
        return yaml.safe_load(f)


def _get_wdh(mit_tr):
    """Extract WDH cross-entity coverage data."""
    return mit_tr.get('journalist_cross_entity_coverage', {}).get('will_douglas_heaven', {})


# ===================================================================
# I. PROFILE STRUCTURE
# ===================================================================
class TestProfileStructure:
    """WDH profile has required cross-entity coverage fields."""

    def test_wdh_exists(self, mit_tr):
        wdh = _get_wdh(mit_tr)
        assert wdh, "WDH cross-entity coverage section missing from MIT TR profile"

    def test_has_role(self, mit_tr):
        wdh = _get_wdh(mit_tr)
        assert 'role' in wdh
        assert 'Executive Editor' in wdh['role']

    def test_has_editorial_authority(self, mit_tr):
        wdh = _get_wdh(mit_tr)
        assert 'editorial_authority' in wdh
        assert 'PhD' in wdh['editorial_authority']

    def test_has_all_four_entities(self, mit_tr):
        wdh = _get_wdh(mit_tr)
        for entity in ['openai', 'meta', 'google', 'anthropic']:
            assert entity in wdh, f"Missing entity coverage: {entity}"

    def test_each_entity_has_articles(self, mit_tr):
        wdh = _get_wdh(mit_tr)
        for entity in ['openai', 'meta', 'google', 'anthropic']:
            assert 'articles' in wdh[entity], f"{entity} missing articles list"
            assert len(wdh[entity]['articles']) > 0, f"{entity} has empty articles list"

    def test_each_entity_has_aggregate_tone(self, mit_tr):
        wdh = _get_wdh(mit_tr)
        for entity in ['openai', 'meta', 'google', 'anthropic']:
            assert 'aggregate_tone' in wdh[entity], f"{entity} missing aggregate_tone"

    def test_has_asymmetry_score(self, mit_tr):
        wdh = _get_wdh(mit_tr)
        assert 'cross_entity_asymmetry_score' in wdh
        score = wdh['cross_entity_asymmetry_score']
        assert 0 < score < 1, f"Asymmetry score {score} out of range"

    def test_has_source_access_asymmetry(self, mit_tr):
        wdh = _get_wdh(mit_tr)
        assert 'source_access_asymmetry' in wdh

    def test_has_failure_framing_asymmetry(self, mit_tr):
        wdh = _get_wdh(mit_tr)
        assert 'failure_framing_asymmetry' in wdh

    def test_has_financial_correlation(self, mit_tr):
        wdh = _get_wdh(mit_tr)
        assert 'financial_correlation' in wdh

    def test_date_analyzed(self, mit_tr):
        wdh = _get_wdh(mit_tr)
        assert wdh.get('date_analyzed') == '2026-08-07'


# ===================================================================
# II. AGGREGATE TONE PATTERNS
# ===================================================================
class TestAggregateTone:
    """WDH's aggregate tone varies systematically by entity."""

    def test_openai_tone_is_constructive(self, mit_tr):
        wdh = _get_wdh(mit_tr)
        tone = wdh['openai']['aggregate_tone']
        assert 'insider' in tone.lower() or 'constructive' in tone.lower(), \
            f"OpenAI tone '{tone}' should indicate insider access or constructive framing"

    def test_meta_tone_is_adversarial(self, mit_tr):
        wdh = _get_wdh(mit_tr)
        tone = wdh['meta']['aggregate_tone']
        assert 'failure' in tone.lower() or 'external' in tone.lower(), \
            f"Meta tone '{tone}' should indicate external/failure framing"

    def test_google_tone_is_enthusiastic(self, mit_tr):
        wdh = _get_wdh(mit_tr)
        tone = wdh['google']['aggregate_tone']
        assert 'enthusiasm' in tone.lower() or 'demo' in tone.lower(), \
            f"Google tone '{tone}' should indicate demo enthusiasm"

    def test_anthropic_tone_is_analytical(self, mit_tr):
        wdh = _get_wdh(mit_tr)
        tone = wdh['anthropic']['aggregate_tone']
        assert 'analytical' in tone.lower() or 'respectful' in tone.lower(), \
            f"Anthropic tone '{tone}' should indicate respectful/analytical framing"

    def test_meta_is_most_adversarial_tone(self, mit_tr):
        wdh = _get_wdh(mit_tr)
        meta_tone = wdh['meta']['aggregate_tone'].lower()
        for entity in ['openai', 'google', 'anthropic']:
            entity_tone = wdh[entity]['aggregate_tone'].lower()
            assert 'failure' not in entity_tone or 'external' not in entity_tone, \
                f"{entity} should not share Meta's adversarial tone category"


# ===================================================================
# III. SOURCE ACCESS HIERARCHY
# ===================================================================
class TestSourceAccess:
    """WDH's source access follows a clear hierarchy favoring OpenAI."""

    def test_openai_has_exclusive(self, mit_tr):
        wdh = _get_wdh(mit_tr)
        access = wdh['source_access_asymmetry']
        assert 'exclusive' in access.get('openai_access', '').lower()

    def test_openai_exclusive_mentions_pachocki(self, mit_tr):
        wdh = _get_wdh(mit_tr)
        access = wdh['source_access_asymmetry']
        assert 'Pachocki' in access.get('openai_access', ''), \
            "OpenAI exclusive should reference chief scientist Pachocki"

    def test_google_has_private_demo(self, mit_tr):
        wdh = _get_wdh(mit_tr)
        access = wdh['source_access_asymmetry']
        assert 'preview' in access.get('google_access', '').lower() or \
               'private' in access.get('google_access', '').lower()

    def test_meta_has_no_exclusive(self, mit_tr):
        wdh = _get_wdh(mit_tr)
        access = wdh['source_access_asymmetry']
        meta_access = access.get('meta_access', '').lower()
        assert 'no' in meta_access or 'zero' in meta_access or 'not' in meta_access, \
            "Meta access should document absence of exclusive access"

    def test_source_hierarchy_documented(self, mit_tr):
        wdh = _get_wdh(mit_tr)
        access = wdh['source_access_asymmetry']
        desc = access.get('description', '')
        assert 'hierarchy' in desc.lower() or 'OpenAI' in desc, \
            "Source access should document the access hierarchy"


# ===================================================================
# IV. FAILURE FRAMING DOUBLE STANDARD
# ===================================================================
class TestFailureFraming:
    """Identical technical events receive opposite framing by company."""

    def test_meta_galactica_mortality_language(self, mit_tr):
        wdh = _get_wdh(mit_tr)
        framing = wdh['failure_framing_asymmetry']
        meta_framing = framing.get('meta_galactica', '')
        assert 'survived' in meta_framing.lower(), \
            "Meta Galactica framing should reference 'survived' mortality language"

    def test_google_mariner_celebration_language(self, mit_tr):
        wdh = _get_wdh(mit_tr)
        framing = wdh['failure_framing_asymmetry']
        google_framing = framing.get('google_mariner', '')
        assert 'remarkable' in google_framing.lower(), \
            "Google Mariner framing should reference 'remarkable' celebration language"

    def test_openai_scholarly_normalization(self, mit_tr):
        wdh = _get_wdh(mit_tr)
        framing = wdh['failure_framing_asymmetry']
        openai_framing = framing.get('openai_reward_hacking', '')
        assert 'specification gaming' in openai_framing.lower() or \
               'scholarly' in openai_framing.lower() or \
               'normalized' in openai_framing.lower(), \
            "OpenAI reward hacking should show scholarly normalization framing"

    def test_framing_delta_significant(self, mit_tr):
        wdh = _get_wdh(mit_tr)
        framing = wdh['failure_framing_asymmetry']
        delta = framing.get('framing_delta', 0)
        assert delta >= 0.5, f"Failure framing delta {delta} should be >= 0.5 (significant)"

    def test_galactica_vs_mariner_is_double_standard(self, mit_tr):
        """The same phenomenon — a technical product encountering difficulty — receives
        opposite editorial treatment. Galactica (voluntary retraction) → death language.
        Mariner (getting stuck during demo) → intelligence celebration."""
        wdh = _get_wdh(mit_tr)
        framing = wdh['failure_framing_asymmetry']
        meta = framing.get('meta_galactica', '').lower()
        google = framing.get('google_mariner', '').lower()
        # Meta gets negative framing language
        assert any(w in meta for w in ['survived', 'death', 'failure', 'mortality']), \
            "Meta Galactica should have negative framing vocabulary"
        # Google gets positive framing language
        assert any(w in google for w in ['remarkable', 'celebration', 'intelligence', 'breakthrough']), \
            "Google Mariner should have positive framing vocabulary"


# ===================================================================
# V. ARTICLE-LEVEL FRAMING VALIDATION
# ===================================================================
class TestArticleFraming:
    """Individual articles carry the correct framing analysis."""

    def test_openai_exclusive_interview_exists(self, mit_tr):
        wdh = _get_wdh(mit_tr)
        articles = wdh['openai']['articles']
        interview_types = [a for a in articles if a.get('article_type') == 'exclusive_interview']
        assert len(interview_types) > 0, "OpenAI should have at least one exclusive interview"

    def test_meta_has_product_failure_article(self, mit_tr):
        wdh = _get_wdh(mit_tr)
        articles = wdh['meta']['articles']
        failure_types = [a for a in articles if a.get('article_type') == 'product_failure']
        assert len(failure_types) > 0, "Meta should have at least one product_failure article"

    def test_all_articles_have_source_urls(self, mit_tr):
        wdh = _get_wdh(mit_tr)
        for entity in ['openai', 'meta', 'google', 'anthropic']:
            for article in wdh[entity]['articles']:
                assert article.get('source_url'), \
                    f"{entity} article '{article.get('title', 'unknown')}' missing source_url"

    def test_all_articles_have_framing_notes(self, mit_tr):
        wdh = _get_wdh(mit_tr)
        for entity in ['openai', 'meta', 'google', 'anthropic']:
            for article in wdh[entity]['articles']:
                assert article.get('framing_notes'), \
                    f"{entity} article '{article.get('title', 'unknown')}' missing framing_notes"

    def test_openai_articles_count(self, mit_tr):
        wdh = _get_wdh(mit_tr)
        assert wdh['openai']['article_count'] >= 4, "OpenAI should have 4+ articles documented"

    def test_meta_articles_count(self, mit_tr):
        wdh = _get_wdh(mit_tr)
        assert wdh['meta']['article_count'] >= 2, "Meta should have 2+ articles documented"


# ===================================================================
# VI. FINANCIAL RELATIONSHIP CORRELATION
# ===================================================================
class TestFinancialCorrelation:
    """Financial relationships predict coverage tone direction."""

    def test_mit_google_relationship_exists(self, mit_tr):
        wdh = _get_wdh(mit_tr)
        fin = wdh['financial_correlation']
        assert fin.get('mit_google_program') is True

    def test_mit_apple_csail_exists(self, mit_tr):
        wdh = _get_wdh(mit_tr)
        fin = wdh['financial_correlation']
        assert fin.get('mit_apple_csail') is True

    def test_meta_has_zero_relationship(self, mit_tr):
        wdh = _get_wdh(mit_tr)
        fin = wdh['financial_correlation']
        meta_rel = fin.get('mit_meta_relationship', '').lower()
        assert 'no' in meta_rel or 'zero' in meta_rel, \
            "Meta relationship field should document absence of MIT ties"

    def test_financial_predicts_tone_documented(self, mit_tr):
        wdh = _get_wdh(mit_tr)
        fin = wdh['financial_correlation']
        predicts = fin.get('financial_predicts_tone', '')
        assert len(predicts) > 50, "Financial-predicts-tone analysis should be substantive"

    def test_google_financial_relationship_matches_warm_coverage(self, mit_tr):
        """Google has MIT bilateral program AND receives 'remarkable' demo framing."""
        wdh = _get_wdh(mit_tr)
        assert wdh['financial_correlation']['mit_google_program'] is True
        assert 'enthusiasm' in wdh['google']['aggregate_tone'].lower() or \
               'demo' in wdh['google']['aggregate_tone'].lower()

    def test_meta_zero_relationship_matches_adversarial_coverage(self, mit_tr):
        """Meta has zero MIT ties AND receives failure/external framing."""
        wdh = _get_wdh(mit_tr)
        meta_rel = wdh['financial_correlation']['mit_meta_relationship'].lower()
        assert 'zero' in meta_rel or 'no' in meta_rel
        assert 'failure' in wdh['meta']['aggregate_tone'].lower() or \
               'external' in wdh['meta']['aggregate_tone'].lower()


# ===================================================================
# VII. CROSS-ENTITY ASYMMETRY SCORE
# ===================================================================
class TestAsymmetryScore:
    """Overall asymmetry score is calibrated correctly."""

    def test_score_moderate_high(self, mit_tr):
        wdh = _get_wdh(mit_tr)
        score = wdh['cross_entity_asymmetry_score']
        assert 0.4 <= score <= 0.8, \
            f"WDH asymmetry score {score} should be moderate-high (0.4-0.8)"

    def test_score_lower_than_schiffer(self, mit_tr):
        """WDH should have lower asymmetry than WIRED's Schiffer (0.82)
        because WDH maintains a more scholarly baseline."""
        wdh = _get_wdh(mit_tr)
        score = wdh['cross_entity_asymmetry_score']
        assert score < 0.82, \
            f"WDH score {score} should be lower than Schiffer's 0.82"

    def test_asymmetry_notes_mention_scholarly(self, mit_tr):
        wdh = _get_wdh(mit_tr)
        notes = wdh.get('asymmetry_notes', '')
        assert 'scholar' in notes.lower(), \
            "Asymmetry notes should acknowledge WDH's scholarly baseline"


# ===================================================================
# VIII. HEIKKILÄ MIGRATION
# ===================================================================
class TestHeikkilaMigration:
    """Heikkilä MIT TR → FT migration is documented."""

    def test_migration_exists(self, mit_tr):
        cross = mit_tr.get('journalist_cross_entity_coverage', {})
        assert 'heikkila_migration' in cross, "Heikkilä migration section missing"

    def test_migration_from_mit_tr(self, mit_tr):
        migration = mit_tr['journalist_cross_entity_coverage']['heikkila_migration']
        assert migration['from_publication'] == 'MIT Technology Review'

    def test_migration_to_ft(self, mit_tr):
        migration = mit_tr['journalist_cross_entity_coverage']['heikkila_migration']
        assert migration['to_publication'] == 'Financial Times'

    def test_migration_has_significance(self, mit_tr):
        migration = mit_tr['journalist_cross_entity_coverage']['heikkila_migration']
        sig = migration.get('significance', '')
        assert 'natural experiment' in sig.lower() or 'high-value' in sig.lower(), \
            "Migration significance should note its analytical value"

    def test_migration_has_source_url(self, mit_tr):
        migration = mit_tr['journalist_cross_entity_coverage']['heikkila_migration']
        assert migration.get('source_url'), "Migration should cite evidence"

    def test_migration_bridges_both_institutions(self, mit_tr):
        migration = mit_tr['journalist_cross_entity_coverage']['heikkila_migration']
        sig = migration.get('significance', '')
        assert 'bridge' in sig.lower() or 'both institutions' in sig.lower(), \
            "Migration should note Heikkilä bridges FT and MIT TR via State of AI collab"


# ===================================================================
# IX. CROSS-REFERENCING WITH MIT TR PROFILE
# ===================================================================
class TestCrossReference:
    """WDH analysis is consistent with MIT TR profile's other sections."""

    def test_wdh_in_key_journalists(self, mit_tr):
        journalists = mit_tr.get('key_journalists', [])
        names = [j['name'] for j in journalists]
        assert 'Will Douglas Heaven' in names, \
            "WDH should appear in key_journalists list"

    def test_wdh_beat_matches(self, mit_tr):
        journalists = mit_tr.get('key_journalists', [])
        wdh_entry = next((j for j in journalists if j['name'] == 'Will Douglas Heaven'), None)
        assert wdh_entry is not None
        assert 'AI' in wdh_entry.get('beat', '')

    def test_heikkila_in_notable_departures(self, mit_tr):
        editorial = mit_tr.get('editorial_history', {})
        departures = editorial.get('notable_departures', [])
        names = [d.get('journalist', '') for d in departures]
        assert 'Melissa Heikkilä' in names, \
            "Heikkilä should appear in notable_departures"

    def test_heikkila_departure_matches_migration(self, mit_tr):
        editorial = mit_tr.get('editorial_history', {})
        departures = editorial.get('notable_departures', [])
        heikkila = next((d for d in departures if d.get('journalist') == 'Melissa Heikkilä'), None)
        assert heikkila is not None
        assert 'Financial Times' in heikkila.get('to', '')

    def test_mit_google_conflict_documented(self, mit_tr):
        """MIT-Google bilateral program should be in known_conflicts."""
        conflicts = mit_tr.get('known_conflicts', [])
        conflict_texts = ' '.join([c.get('description', '') for c in conflicts])
        assert 'Google' in conflict_texts or 'MIT-Google' in conflict_texts, \
            "MIT-Google relationship should be documented in known_conflicts"

    def test_apple_csail_documented(self, mit_tr):
        """Apple CSAIL membership should be in known_conflicts."""
        conflicts = mit_tr.get('known_conflicts', [])
        conflict_texts = ' '.join([c.get('description', '') for c in conflicts])
        assert 'Apple' in conflict_texts, \
            "Apple CSAIL membership should appear in known_conflicts"

    def test_editorial_partnership_ft_documented(self, mit_tr):
        """FT editorial partnership should be documented."""
        editorial = mit_tr.get('editorial_history', {})
        partnerships = editorial.get('editorial_partnerships', [])
        if partnerships:
            ft_partners = [p for p in partnerships if 'Financial Times' in p.get('partner', '')]
            assert len(ft_partners) > 0, "FT editorial partnership should be documented"


# ===================================================================
# X. COUNTER-ARGUMENT ACKNOWLEDGMENT
# ===================================================================
class TestCounterArguments:
    """Profile acknowledges legitimate counter-arguments."""

    def test_notes_scholarly_baseline(self, mit_tr):
        """WDH has genuine analytical capability — the asymmetry is in selective
        application, not absence of rigor."""
        wdh = _get_wdh(mit_tr)
        notes = wdh.get('asymmetry_notes', '')
        assert 'analytical' in notes.lower() or 'rigor' in notes.lower(), \
            "Notes should acknowledge WDH's genuine analytical capability"

    def test_anthropic_coverage_shows_critical_thinking(self, mit_tr):
        """Anthropic coverage demonstrates real balanced analysis, showing WDH
        CAN be balanced — strengthening the case that Meta imbalance is systematic."""
        wdh = _get_wdh(mit_tr)
        anthropic_tone = wdh['anthropic']['aggregate_tone']
        assert 'analytical' in anthropic_tone.lower() or 'respectful' in anthropic_tone.lower()

    def test_asymmetry_is_selective_not_total(self, mit_tr):
        """The finding is selective application of rigor, not absence of rigor."""
        wdh = _get_wdh(mit_tr)
        notes = wdh.get('asymmetry_notes', '')
        assert 'selectively applied' in notes.lower() or 'selective' in notes.lower(), \
            "Notes should characterize asymmetry as selective, not total"
