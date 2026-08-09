"""
Tests for Brian Barrett (WIRED Executive Editor, News) cross-entity coverage analysis.

Barrett co-hosts the Uncanny Valley podcast and, as Executive Editor, shapes editorial
direction and headline framing for WIRED's news desk. His Uncanny Valley episode headlines
reveal a systematic "Crisis/Makeover Headline Paradox": Meta receives existential crisis
language while competitors receive positive transformation or neutral strategic framing,
even when covering the SAME underlying dynamics (AI investment, workforce restructuring).

The May 21, 2026 headline is the cleanest data point: "Meta Is in Crisis, Google Search's
Makeover, and AI Gets Booed by Graduates" — where the SAME editor applies "crisis" to Meta
and "makeover" to Google in a single headline.

Mechanism #14: Crisis/Makeover Headline Paradox (editorial direction asymmetry)
"""

import yaml
import pathlib
import pytest

PROFILES_DIR = pathlib.Path(__file__).resolve().parent.parent / "profiles"


@pytest.fixture(scope="module")
def wired_profile():
    with open(PROFILES_DIR / "wired.yaml") as f:
        return yaml.safe_load(f)


def _get_barrett(profile):
    """Find Barrett's key_journalists entry with cross_entity analysis."""
    for j in profile.get("key_journalists", []):
        if j.get("name") == "Brian Barrett" and "cross_entity_coverage_analysis" in j:
            return j
    pytest.fail("Brian Barrett cross_entity_coverage_analysis not found in wired.yaml")


# ── Role & Structural Position ─────────────────────────────────────────


class TestBarrettRole:
    """Verify Barrett's editorial position is documented."""

    def test_executive_editor_title(self, wired_profile):
        barrett = _get_barrett(wired_profile)
        patterns = barrett.get("known_patterns", "")
        assert "Executive Editor" in patterns

    def test_uncanny_valley_cohost(self, wired_profile):
        barrett = _get_barrett(wired_profile)
        patterns = barrett.get("known_patterns", "")
        assert "Uncanny Valley" in patterns

    def test_structural_significance_documented(self, wired_profile):
        barrett = _get_barrett(wired_profile)
        cea = barrett["cross_entity_coverage_analysis"]
        sig = cea.get("structural_significance", "")
        assert "editorial direction" in sig.lower()

    def test_shapes_newsroom_direction(self, wired_profile):
        barrett = _get_barrett(wired_profile)
        patterns = barrett.get("known_patterns", "")
        assert "shapes editorial direction" in patterns or "editorial direction" in patterns


# ── Meta Headline Framing ───────────────────────────────────────────────


class TestMetaHeadlines:
    """Barrett's Meta headlines consistently use crisis/failure language."""

    def test_meta_headlines_exist(self, wired_profile):
        barrett = _get_barrett(wired_profile)
        meta_h = barrett["cross_entity_coverage_analysis"]["meta_headlines_2026"]
        assert len(meta_h["examples"]) >= 4

    def test_meta_crisis_headline(self, wired_profile):
        barrett = _get_barrett(wired_profile)
        meta_h = barrett["cross_entity_coverage_analysis"]["meta_headlines_2026"]
        headlines = [e["headline"] for e in meta_h["examples"]]
        assert any("Crisis" in h for h in headlines)

    def test_meta_revolting_headline(self, wired_profile):
        barrett = _get_barrett(wired_profile)
        meta_h = barrett["cross_entity_coverage_analysis"]["meta_headlines_2026"]
        headlines = [e["headline"] for e in meta_h["examples"]]
        assert any("Revolting" in h for h in headlines)

    def test_meta_hacked_headline(self, wired_profile):
        barrett = _get_barrett(wired_profile)
        meta_h = barrett["cross_entity_coverage_analysis"]["meta_headlines_2026"]
        headlines = [e["headline"] for e in meta_h["examples"]]
        assert any("Hacked" in h for h in headlines)

    def test_meta_leaks_headline(self, wired_profile):
        barrett = _get_barrett(wired_profile)
        meta_h = barrett["cross_entity_coverage_analysis"]["meta_headlines_2026"]
        headlines = [e["headline"] for e in meta_h["examples"]]
        assert any("Leaks" in h for h in headlines)

    def test_meta_pattern_is_crisis(self, wired_profile):
        barrett = _get_barrett(wired_profile)
        meta_h = barrett["cross_entity_coverage_analysis"]["meta_headlines_2026"]
        pattern = meta_h.get("pattern", "")
        assert "crisis" in pattern.lower() or "failure" in pattern.lower()

    def test_all_meta_headlines_negative(self, wired_profile):
        barrett = _get_barrett(wired_profile)
        cea = barrett["cross_entity_coverage_analysis"]
        qs = cea["quantitative_summary"]
        assert qs["meta_positive_language_count"] == 0
        assert qs["meta_crisis_language_count"] >= 4


# ── Competitor Headline Framing ─────────────────────────────────────────


class TestCompetitorHeadlines:
    """Barrett's competitor headlines use transformation/neutral/victim language."""

    def test_competitor_headlines_exist(self, wired_profile):
        barrett = _get_barrett(wired_profile)
        comp_h = barrett["cross_entity_coverage_analysis"]["competitor_headlines_2026"]
        assert len(comp_h["examples"]) >= 5

    def test_google_makeover_headline(self, wired_profile):
        barrett = _get_barrett(wired_profile)
        comp_h = barrett["cross_entity_coverage_analysis"]["competitor_headlines_2026"]
        headlines = [e["headline"] for e in comp_h["examples"]]
        assert any("Google" in h and "Makeover" in h for h in headlines)

    def test_apple_makeover_headline(self, wired_profile):
        barrett = _get_barrett(wired_profile)
        comp_h = barrett["cross_entity_coverage_analysis"]["competitor_headlines_2026"]
        headlines = [e["headline"] for e in comp_h["examples"]]
        assert any("Siri" in h and "Makeover" in h for h in headlines)

    def test_anthropic_victim_framing(self, wired_profile):
        barrett = _get_barrett(wired_profile)
        comp_h = barrett["cross_entity_coverage_analysis"]["competitor_headlines_2026"]
        headlines = [e["headline"] for e in comp_h["examples"]]
        assert any("Steal From Anthropic" in h for h in headlines)

    def test_anthropic_quality_endorsement(self, wired_profile):
        barrett = _get_barrett(wired_profile)
        comp_h = barrett["cross_entity_coverage_analysis"]["competitor_headlines_2026"]
        headlines = [e["headline"] for e in comp_h["examples"]]
        assert any("Best AI" in h for h in headlines)

    def test_apple_legal_agency(self, wired_profile):
        barrett = _get_barrett(wired_profile)
        comp_h = barrett["cross_entity_coverage_analysis"]["competitor_headlines_2026"]
        headlines = [e["headline"] for e in comp_h["examples"]]
        assert any("Apple Sued" in h for h in headlines)

    def test_no_competitor_crisis_language(self, wired_profile):
        barrett = _get_barrett(wired_profile)
        cea = barrett["cross_entity_coverage_analysis"]
        qs = cea["quantitative_summary"]
        assert qs["competitor_crisis_language_count"] == 0

    def test_all_competitor_headlines_neutral_or_positive(self, wired_profile):
        barrett = _get_barrett(wired_profile)
        cea = barrett["cross_entity_coverage_analysis"]
        qs = cea["quantitative_summary"]
        assert qs["competitor_positive_or_neutral_language_count"] >= 5


# ── The May 21 Paradox ──────────────────────────────────────────────────


class TestCrisisMakeoverParadox:
    """The May 21, 2026 headline is the cleanest natural experiment:
    same editor, same headline, same underlying dynamics (AI pivot),
    different framing for Meta vs Google."""

    def test_crisis_and_makeover_same_date(self, wired_profile):
        barrett = _get_barrett(wired_profile)
        cea = barrett["cross_entity_coverage_analysis"]
        meta_dates = {e["date"] for e in cea["meta_headlines_2026"]["examples"]}
        comp_dates = {e["date"] for e in cea["competitor_headlines_2026"]["examples"]}
        # Both should have entries on 2026-05-21
        assert "2026-05-21" in meta_dates
        assert "2026-05-21" in comp_dates

    def test_meta_crisis_google_makeover_same_headline(self, wired_profile):
        barrett = _get_barrett(wired_profile)
        cea = barrett["cross_entity_coverage_analysis"]
        # Find the May 21 Meta headline
        meta_may21 = [e for e in cea["meta_headlines_2026"]["examples"]
                      if e["date"] == "2026-05-21"]
        assert len(meta_may21) == 1
        assert "Crisis" in meta_may21[0]["headline"]
        assert "Makeover" in meta_may21[0]["headline"]  # Google part is in same headline

    def test_crisis_language_register(self, wired_profile):
        barrett = _get_barrett(wired_profile)
        cea = barrett["cross_entity_coverage_analysis"]
        meta_may21 = [e for e in cea["meta_headlines_2026"]["examples"]
                      if e["date"] == "2026-05-21"][0]
        assert "crisis" in meta_may21["language_register"].lower()

    def test_makeover_language_register(self, wired_profile):
        barrett = _get_barrett(wired_profile)
        cea = barrett["cross_entity_coverage_analysis"]
        comp_may21 = [e for e in cea["competitor_headlines_2026"]["examples"]
                      if e["date"] == "2026-05-21"][0]
        assert "makeover" in comp_may21["language_register"].lower()

    def test_mechanism_named(self, wired_profile):
        barrett = _get_barrett(wired_profile)
        cea = barrett["cross_entity_coverage_analysis"]
        assert "crisis_makeover_headline_paradox" in cea.get("mechanism_name", "")

    def test_mechanism_number(self, wired_profile):
        barrett = _get_barrett(wired_profile)
        cea = barrett["cross_entity_coverage_analysis"]
        assert cea.get("mechanism_number") == 14


# ── Quantitative Summary ────────────────────────────────────────────────


class TestQuantitativeSummary:
    """Verify the statistical summary of headline valence."""

    def test_perfect_valence_gap(self, wired_profile):
        barrett = _get_barrett(wired_profile)
        qs = barrett["cross_entity_coverage_analysis"]["quantitative_summary"]
        assert qs["headline_valence_gap"] == 1.0

    def test_four_meta_headlines(self, wired_profile):
        barrett = _get_barrett(wired_profile)
        qs = barrett["cross_entity_coverage_analysis"]["quantitative_summary"]
        assert qs["meta_headlines_analyzed"] == 4

    def test_six_competitor_headlines(self, wired_profile):
        barrett = _get_barrett(wired_profile)
        qs = barrett["cross_entity_coverage_analysis"]["quantitative_summary"]
        assert qs["competitor_headlines_analyzed"] == 6


# ── Podcast Transcript Evidence ─────────────────────────────────────────


class TestPodcastTranscriptEvidence:
    """Barrett's podcast commentary reveals how crisis framing is constructed."""

    def test_spyware_language(self, wired_profile):
        barrett = _get_barrett(wired_profile)
        cea = barrett["cross_entity_coverage_analysis"]
        quotes = cea["podcast_transcript_evidence"]["key_quotes"]
        spyware_quotes = [q for q in quotes if "spyware" in q.get("quote", "").lower()]
        assert len(spyware_quotes) >= 1

    def test_spyware_speaker_is_barrett(self, wired_profile):
        barrett = _get_barrett(wired_profile)
        cea = barrett["cross_entity_coverage_analysis"]
        quotes = cea["podcast_transcript_evidence"]["key_quotes"]
        spyware_quotes = [q for q in quotes if "spyware" in q.get("quote", "").lower()]
        assert spyware_quotes[0]["speaker"] == "Brian Barrett"

    def test_meltdown_language(self, wired_profile):
        barrett = _get_barrett(wired_profile)
        cea = barrett["cross_entity_coverage_analysis"]
        quotes = cea["podcast_transcript_evidence"]["key_quotes"]
        meltdown_quotes = [q for q in quotes if "meltdown" in q.get("quote", "").lower()]
        assert len(meltdown_quotes) >= 1

    def test_episode_identified(self, wired_profile):
        barrett = _get_barrett(wired_profile)
        cea = barrett["cross_entity_coverage_analysis"]
        episode = cea["podcast_transcript_evidence"]["episode"]
        assert "May 21, 2026" in episode


# ── Financial Incentive Connection ──────────────────────────────────────


class TestFinancialIncentiveConnection:
    """Barrett's framing aligns with Condé Nast's financial relationships."""

    def test_conde_nast_openai_deal_referenced(self, wired_profile):
        barrett = _get_barrett(wired_profile)
        cea = barrett["cross_entity_coverage_analysis"]
        fin = cea.get("financial_incentive_connection", "")
        assert "Condé Nast" in fin
        assert "OpenAI" in fin

    def test_meta_no_content_deal(self, wired_profile):
        barrett = _get_barrett(wired_profile)
        cea = barrett["cross_entity_coverage_analysis"]
        fin = cea.get("financial_incentive_connection", "")
        assert "no content licensing deal" in fin.lower() or "overestimate the value" in fin

    def test_asymmetry_direction_documented(self, wired_profile):
        barrett = _get_barrett(wired_profile)
        cea = barrett["cross_entity_coverage_analysis"]
        fin = cea.get("financial_incentive_connection", "")
        assert "aligns with financial interests" in fin.lower() or "financial" in fin.lower()

    def test_test_file_path(self, wired_profile):
        barrett = _get_barrett(wired_profile)
        cea = barrett["cross_entity_coverage_analysis"]
        assert cea.get("test_file") == "tests/test_brian_barrett_cross_entity.py"
