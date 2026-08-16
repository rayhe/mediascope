"""
WSJ Anthropic-Meta Military-Consumer Severity Inversion — Type A Competitor Deep Dive (Aug 15, 2026)

Mechanism #125: Military-Consumer Severity Inversion — Publication Applies
MORE Alarm Language to Consumer Camera Product Than to AI Used in Actual Bombing Raid

KEY FINDING: WSJ applies more alarm language (10+ terms) to Meta's consumer camera
glasses (zero deaths, unshipped features) than to Anthropic's Claude AI being used
in the U.S. military's operation to capture former Venezuelan President Maduro,
which "included bombing several sites in Caracas" (actual violence, actual deaths).

This is a SEVERITY INVERSION: editorial alarm intensity scales INVERSELY with
actual harm. Meta's theoretical consumer privacy risks generate "flooding,"
"up in arms," "lightning rod," "ire," and "ban" language, while AI involvement
in a bombing raid generates "safety-focused," "grappling," and "concerns."

FINANCIAL CONTEXT: News Corp has roughly balanced AI licensing revenue:
  - OpenAI: $50M/yr ($250M/5yr)
  - Meta: up to $50M/yr (3-year deal)
  - Anthropic: expected share of $1.5B copyright settlement
So the severity inversion is NOT financially predicted by the deal-driven model.
It is an EDITORIAL CALIBRATION FAILURE: the same publication's alarm vocabulary
is not correlated with actual harm magnitude.

This extends mechanism #49 (Bobrowsky beat-assignment entity-targeting) and the
existing severity_framing_inversion (rogue AI OpenAI vs Meta) by adding a
MILITARY-CONSUMER dimension where the harm gap is measured in human lives vs zero.

Sources:
  - WSJ: Bobrowsky "Meta Is Flooding the Market With Smartglasses" (Jul 14, 2026)
    https://www.wsj.com/tech/ai/meta-is-flooding-the-market-with-smartglasses-privacy-advocates-are-up-in-arms-8fb71539
  - WSJ: "Pentagon Used Anthropic's Claude in Maduro Venezuela Raid" (Feb 14, 2026)
    https://www.wsj.com/politics/national-security/pentagon-used-anthropics-claude-in-maduro-venezuela-raid-583aff17
  - WSJ: "Google Clears Pentagon to Use AI Tools" (Apr 28, 2026) — contains News Corp
    disclosure of OpenAI and Google financial relationships
    https://www.wsj.com/tech/ai/google-clears-pentagon-to-use-ai-tools-in-classified-settings-d8162cda
  - Reuters: "US used Anthropic's Claude during the Venezuela raid" (Feb 14, 2026)
    https://www.reuters.com/world/americas/us-used-anthropics-claude-during-the-venezuela-raid-wsj-reports-2026-02-13/

Created: 2026-08-15
"""

import yaml
import os
import pytest
from pathlib import Path

PROFILES_DIR = Path(__file__).parent.parent / "profiles"


def load_yaml(filename):
    """Load a YAML profile file."""
    path = PROFILES_DIR / filename
    with open(path, 'r') as f:
        return yaml.safe_load(f)


class TestMechanismPresence:
    """Verify mechanism #125 exists in competitor-coverage-research.yaml."""

    def test_mechanism_125_exists(self):
        data = load_yaml('competitor-coverage-research.yaml')
        # Check cross_publication_findings for the mechanism
        cpf = data.get('cross_publication_findings', {})
        assert 'wsj_anthropic_meta_military_consumer_severity_inversion' in cpf, \
            "Must have wsj_anthropic_meta_military_consumer_severity_inversion in cross_publication_findings"

    def test_mechanism_125_has_correct_id(self):
        data = load_yaml('competitor-coverage-research.yaml')
        cpf = data['cross_publication_findings']
        entry = cpf['wsj_anthropic_meta_military_consumer_severity_inversion']
        assert entry.get('mechanism_id') == 125, \
            "Mechanism must have ID 125"

    def test_mechanism_has_publication(self):
        data = load_yaml('competitor-coverage-research.yaml')
        cpf = data['cross_publication_findings']
        entry = cpf['wsj_anthropic_meta_military_consumer_severity_inversion']
        assert 'Wall Street Journal' in str(entry.get('publication', '')), \
            "Must identify WSJ as the publication"

    def test_mechanism_has_finding_type(self):
        data = load_yaml('competitor-coverage-research.yaml')
        cpf = data['cross_publication_findings']
        entry = cpf['wsj_anthropic_meta_military_consumer_severity_inversion']
        assert 'severity_inversion' in str(entry.get('finding_type', '')).lower() or \
               'severity' in str(entry.get('finding_type', '')).lower(), \
            "Finding type must reference severity inversion"


class TestArticleEvidence:
    """Verify both articles are documented with source URLs."""

    def test_meta_glasses_article_documented(self):
        data = load_yaml('competitor-coverage-research.yaml')
        cpf = data['cross_publication_findings']
        entry = cpf['wsj_anthropic_meta_military_consumer_severity_inversion']
        articles = entry.get('articles', [])
        meta_titles = [a.get('title', '') for a in articles]
        assert any('flooding' in t.lower() or 'smartglasses' in t.lower() or 'glasses' in t.lower()
                    for t in meta_titles), \
            "Must document the Meta smartglasses article"

    def test_anthropic_pentagon_article_documented(self):
        data = load_yaml('competitor-coverage-research.yaml')
        cpf = data['cross_publication_findings']
        entry = cpf['wsj_anthropic_meta_military_consumer_severity_inversion']
        articles = entry.get('articles', [])
        titles = [a.get('title', '') for a in articles]
        assert any('pentagon' in t.lower() or 'maduro' in t.lower() or 'venezuela' in t.lower()
                    for t in titles), \
            "Must document the Anthropic/Pentagon article"

    def test_meta_article_has_source_url(self):
        data = load_yaml('competitor-coverage-research.yaml')
        cpf = data['cross_publication_findings']
        entry = cpf['wsj_anthropic_meta_military_consumer_severity_inversion']
        articles = entry.get('articles', [])
        meta_article = next(
            (a for a in articles if 'flooding' in a.get('title', '').lower()
             or 'smartglasses' in a.get('title', '').lower()), None
        )
        assert meta_article is not None, "Meta article must be present"
        assert 'wsj.com' in meta_article.get('source_url', ''), \
            "Meta article must have WSJ source URL"

    def test_anthropic_article_has_source_url(self):
        data = load_yaml('competitor-coverage-research.yaml')
        cpf = data['cross_publication_findings']
        entry = cpf['wsj_anthropic_meta_military_consumer_severity_inversion']
        articles = entry.get('articles', [])
        anthro_article = next(
            (a for a in articles if 'pentagon' in a.get('title', '').lower()
             or 'maduro' in a.get('title', '').lower()), None
        )
        assert anthro_article is not None, "Anthropic/Pentagon article must be present"
        assert 'wsj.com' in anthro_article.get('source_url', ''), \
            "Anthropic article must have WSJ source URL"


class TestAlarmLanguageAsymmetry:
    """Verify the alarm language differential is documented."""

    def test_meta_alarm_terms_counted(self):
        data = load_yaml('competitor-coverage-research.yaml')
        cpf = data['cross_publication_findings']
        entry = cpf['wsj_anthropic_meta_military_consumer_severity_inversion']
        meta_alarm = entry.get('meta_alarm_vocabulary', {})
        terms = meta_alarm.get('terms', [])
        assert len(terms) >= 8, \
            f"Must document 8+ Meta alarm terms, found {len(terms)}"

    def test_meta_alarm_includes_key_phrases(self):
        data = load_yaml('competitor-coverage-research.yaml')
        cpf = data['cross_publication_findings']
        entry = cpf['wsj_anthropic_meta_military_consumer_severity_inversion']
        meta_alarm = entry.get('meta_alarm_vocabulary', {})
        terms_lower = [t.lower() for t in meta_alarm.get('terms', [])]
        key_phrases = ['flooding', 'up in arms', 'lightning rod']
        found = sum(1 for kp in key_phrases if any(kp in t for t in terms_lower))
        assert found >= 2, \
            f"Must include at least 2 of {key_phrases}, found {found}"

    def test_anthropic_sympathetic_terms_counted(self):
        data = load_yaml('competitor-coverage-research.yaml')
        cpf = data['cross_publication_findings']
        entry = cpf['wsj_anthropic_meta_military_consumer_severity_inversion']
        anthro = entry.get('anthropic_sympathetic_vocabulary', {})
        terms = anthro.get('terms', [])
        assert len(terms) >= 3, \
            f"Must document 3+ Anthropic sympathetic terms, found {len(terms)}"

    def test_alarm_ratio_documented(self):
        data = load_yaml('competitor-coverage-research.yaml')
        cpf = data['cross_publication_findings']
        entry = cpf['wsj_anthropic_meta_military_consumer_severity_inversion']
        meta_count = len(entry.get('meta_alarm_vocabulary', {}).get('terms', []))
        anthro_count = len(entry.get('anthropic_sympathetic_vocabulary', {}).get('terms', []))
        # Meta alarm terms should outnumber Anthropic alarm terms
        assert meta_count > anthro_count, \
            f"Meta alarm terms ({meta_count}) must exceed Anthropic ({anthro_count})"


class TestSeverityInversion:
    """Verify the severity inversion is quantified."""

    def test_harm_comparison_documented(self):
        data = load_yaml('competitor-coverage-research.yaml')
        cpf = data['cross_publication_findings']
        entry = cpf['wsj_anthropic_meta_military_consumer_severity_inversion']
        inversion = entry.get('severity_inversion', {})
        assert 'meta_actual_harm' in inversion, "Must document Meta's actual harm level"
        assert 'anthropic_actual_harm' in inversion, "Must document Anthropic's actual harm level"

    def test_meta_harm_is_zero(self):
        data = load_yaml('competitor-coverage-research.yaml')
        cpf = data['cross_publication_findings']
        entry = cpf['wsj_anthropic_meta_military_consumer_severity_inversion']
        inversion = entry.get('severity_inversion', {})
        meta_harm = str(inversion.get('meta_actual_harm', '')).lower()
        assert 'zero' in meta_harm or 'none' in meta_harm or '0' in meta_harm, \
            "Meta's actual harm must be documented as zero/none"

    def test_anthropic_harm_is_violence(self):
        data = load_yaml('competitor-coverage-research.yaml')
        cpf = data['cross_publication_findings']
        entry = cpf['wsj_anthropic_meta_military_consumer_severity_inversion']
        inversion = entry.get('severity_inversion', {})
        anthro_harm = str(inversion.get('anthropic_actual_harm', '')).lower()
        assert any(word in anthro_harm for word in ['bombing', 'military', 'violence', 'raid', 'combat']), \
            "Anthropic's actual harm must reference bombing/military/violence"

    def test_inversion_direction_documented(self):
        data = load_yaml('competitor-coverage-research.yaml')
        cpf = data['cross_publication_findings']
        entry = cpf['wsj_anthropic_meta_military_consumer_severity_inversion']
        inversion = entry.get('severity_inversion', {})
        direction = str(inversion.get('direction', '')).lower()
        assert 'inverse' in direction or 'invert' in direction or 'negative' in direction, \
            "Must document that alarm language is inversely correlated with harm"

    def test_meta_features_unshipped(self):
        data = load_yaml('competitor-coverage-research.yaml')
        cpf = data['cross_publication_findings']
        entry = cpf['wsj_anthropic_meta_military_consumer_severity_inversion']
        inversion = entry.get('severity_inversion', {})
        meta_features = str(inversion.get('meta_feature_status', '')).lower()
        assert any(word in meta_features for word in ['unshipped', 'development', 'patent', 'not shipped', 'exploring']), \
            "Must note that alarmed-about Meta features are unshipped/in development"


class TestFinancialContext:
    """Verify financial relationships are documented as control."""

    def test_news_corp_openai_deal_noted(self):
        data = load_yaml('competitor-coverage-research.yaml')
        cpf = data['cross_publication_findings']
        entry = cpf['wsj_anthropic_meta_military_consumer_severity_inversion']
        financial = entry.get('financial_context', {})
        openai = str(financial.get('openai_deal', '')).lower()
        assert '$50m' in openai or '$250m' in openai or '50m' in openai, \
            "Must document News Corp-OpenAI $50M/yr deal"

    def test_news_corp_meta_deal_noted(self):
        data = load_yaml('competitor-coverage-research.yaml')
        cpf = data['cross_publication_findings']
        entry = cpf['wsj_anthropic_meta_military_consumer_severity_inversion']
        financial = entry.get('financial_context', {})
        meta_deal = str(financial.get('meta_deal', '')).lower()
        assert '$50m' in meta_deal or '50m' in meta_deal, \
            "Must document News Corp-Meta $50M/yr deal"

    def test_anthropic_settlement_noted(self):
        data = load_yaml('competitor-coverage-research.yaml')
        cpf = data['cross_publication_findings']
        entry = cpf['wsj_anthropic_meta_military_consumer_severity_inversion']
        financial = entry.get('financial_context', {})
        anthro = str(financial.get('anthropic_relationship', '')).lower()
        assert 'settlement' in anthro or '$1.5b' in anthro or '1.5b' in anthro, \
            "Must document News Corp-Anthropic settlement relationship"

    def test_balanced_deals_as_control(self):
        data = load_yaml('competitor-coverage-research.yaml')
        cpf = data['cross_publication_findings']
        entry = cpf['wsj_anthropic_meta_military_consumer_severity_inversion']
        financial = entry.get('financial_context', {})
        interpretation = str(financial.get('interpretation', '')).lower()
        assert 'balanced' in interpretation or 'control' in interpretation or \
               'not financially' in interpretation, \
            "Must note that balanced deals mean inversion is NOT financially predicted"


class TestConfounders:
    """Verify confounders are documented."""

    def test_confounders_present(self):
        data = load_yaml('competitor-coverage-research.yaml')
        cpf = data['cross_publication_findings']
        entry = cpf['wsj_anthropic_meta_military_consumer_severity_inversion']
        confounders = entry.get('confounders', [])
        assert len(confounders) >= 3, \
            f"Must document at least 3 confounders, found {len(confounders)}"

    def test_confounders_include_genre_difference(self):
        data = load_yaml('competitor-coverage-research.yaml')
        cpf = data['cross_publication_findings']
        entry = cpf['wsj_anthropic_meta_military_consumer_severity_inversion']
        confounders = entry.get('confounders', [])
        confounder_text = ' '.join([str(c) for c in confounders]).lower()
        assert 'genre' in confounder_text or 'section' in confounder_text or \
               'beat' in confounder_text or 'national security' in confounder_text, \
            "Must consider article genre/section as a confounder"

    def test_confounders_include_reporter_difference(self):
        data = load_yaml('competitor-coverage-research.yaml')
        cpf = data['cross_publication_findings']
        entry = cpf['wsj_anthropic_meta_military_consumer_severity_inversion']
        confounders = entry.get('confounders', [])
        confounder_text = ' '.join([str(c) for c in confounders]).lower()
        assert 'reporter' in confounder_text or 'journalist' in confounder_text or \
               'author' in confounder_text or 'bobrowsky' in confounder_text, \
            "Must consider different reporters as a confounder"


class TestCrossReferences:
    """Verify cross-references to related mechanisms."""

    def test_references_mechanism_49(self):
        data = load_yaml('competitor-coverage-research.yaml')
        cpf = data['cross_publication_findings']
        entry = cpf['wsj_anthropic_meta_military_consumer_severity_inversion']
        cross_refs = entry.get('cross_references', [])
        ref_ids = [cr.get('mechanism_id', 0) for cr in cross_refs]
        assert 49 in ref_ids, \
            "Must cross-reference mechanism #49 (Bobrowsky beat-assignment entity-targeting)"

    def test_references_rogue_ai_severity_inversion(self):
        data = load_yaml('competitor-coverage-research.yaml')
        cpf = data['cross_publication_findings']
        entry = cpf['wsj_anthropic_meta_military_consumer_severity_inversion']
        cross_refs = entry.get('cross_references', [])
        ref_text = ' '.join([str(cr) for cr in cross_refs]).lower()
        assert 'rogue' in ref_text or 'severity' in ref_text, \
            "Must cross-reference existing WSJ severity_framing_inversion"

    def test_has_discovery_date(self):
        data = load_yaml('competitor-coverage-research.yaml')
        cpf = data['cross_publication_findings']
        entry = cpf['wsj_anthropic_meta_military_consumer_severity_inversion']
        assert entry.get('discovery_date', '').startswith('2026-08-15'), \
            "Discovery date must be 2026-08-15"


class TestAnthropicUsagePolicy:
    """Verify the usage policy contradiction is documented."""

    def test_usage_policy_prohibition_documented(self):
        data = load_yaml('competitor-coverage-research.yaml')
        cpf = data['cross_publication_findings']
        entry = cpf['wsj_anthropic_meta_military_consumer_severity_inversion']
        policy = entry.get('anthropic_usage_policy_contradiction', {})
        prohibitions = str(policy.get('stated_prohibitions', '')).lower()
        assert 'violence' in prohibitions or 'weapons' in prohibitions or \
               'surveillance' in prohibitions, \
            "Must document Anthropic's stated prohibitions (violence, weapons, surveillance)"

    def test_actual_use_documented(self):
        data = load_yaml('competitor-coverage-research.yaml')
        cpf = data['cross_publication_findings']
        entry = cpf['wsj_anthropic_meta_military_consumer_severity_inversion']
        policy = entry.get('anthropic_usage_policy_contradiction', {})
        actual_use = str(policy.get('actual_use', '')).lower()
        assert 'bombing' in actual_use or 'military' in actual_use or \
               'raid' in actual_use or 'capture' in actual_use, \
            "Must document actual use in bombing raid"

    def test_contradiction_framing_noted(self):
        data = load_yaml('competitor-coverage-research.yaml')
        cpf = data['cross_publication_findings']
        entry = cpf['wsj_anthropic_meta_military_consumer_severity_inversion']
        policy = entry.get('anthropic_usage_policy_contradiction', {})
        wsj_framing = str(policy.get('wsj_framing_of_contradiction', '')).lower()
        assert 'sympathetic' in wsj_framing or 'principled' in wsj_framing or \
               'safety' in wsj_framing or 'grappling' in wsj_framing, \
            "Must document WSJ's sympathetic framing of Anthropic's contradiction"


class TestNewsCorpProfileUpdated:
    """Verify news-corp.yaml has the military-consumer severity inversion."""

    def test_news_corp_has_anthropic_pentagon_coverage(self):
        data = load_yaml('news-corp.yaml')
        cr = data.get('competitor_relationships', {})
        anthro = cr.get('anthropic', {})
        coverage_examples = anthro.get('coverage_examples', [])
        titles = [e.get('title', '') for e in coverage_examples]
        assert any('pentagon' in t.lower() or 'maduro' in t.lower() or 'venezuela' in t.lower()
                    for t in titles), \
            "news-corp.yaml must document Anthropic Pentagon/Maduro coverage"

    def test_anthropic_pentagon_has_tone_score(self):
        data = load_yaml('news-corp.yaml')
        cr = data.get('competitor_relationships', {})
        anthro = cr.get('anthropic', {})
        coverage_examples = anthro.get('coverage_examples', [])
        pentagon_article = next(
            (e for e in coverage_examples
             if 'pentagon' in e.get('title', '').lower() or 'maduro' in e.get('title', '').lower()),
            None
        )
        assert pentagon_article is not None, "Pentagon article must be in examples"
        assert 'tone' in pentagon_article, "Pentagon article must have tone score"

    def test_anthropic_relationship_type(self):
        data = load_yaml('news-corp.yaml')
        cr = data.get('competitor_relationships', {})
        anthro = cr.get('anthropic', {})
        assert anthro.get('financial_tie') in ['settlement', 'settlement_revenue', 'litigation_settlement'], \
            "Anthropic relationship must be settlement-based"
