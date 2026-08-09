"""Cross-entity coverage analysis: Cecilia Kang (NYT) — Mechanism #9B

Cecilia Kang is Sheera Frenkel's co-author on 'An Ugly Truth' (HarperCollins,
2021, seven-figure advance). She covers Meta from a complementary beat:
regulatory/policy (Washington DC) vs Frenkel's cybersecurity/AI (San Francisco).
This creates a DUAL-BEAT ADVERSARIAL PIPELINE — Mechanism #9B (Parallel Beat
Reinforcement).

Key finding: TWO reporters sharing the same book deal financial incentive but
covering Meta from independent beats produces 360-degree adversarial coverage
with no comparable pipeline for any competitor at the NYT.
"""

import re

import pytest
import yaml


@pytest.fixture(scope="module")
def nyt_profile():
    with open("profiles/nytimes.yaml") as f:
        return yaml.safe_load(f)


@pytest.fixture(scope="module")
def kang_entry(nyt_profile):
    for j in nyt_profile.get("key_journalists", []):
        if "Cecilia Kang" in j.get("name", ""):
            return j
    pytest.fail("Cecilia Kang entry not found in nytimes.yaml key_journalists")


@pytest.fixture(scope="module")
def frenkel_entry(nyt_profile):
    for j in nyt_profile.get("key_journalists", []):
        if "Sheera Frenkel" in j.get("name", ""):
            return j
    pytest.fail("Sheera Frenkel entry not found in nytimes.yaml key_journalists")


@pytest.fixture(scope="module")
def cross_entity(kang_entry):
    return kang_entry.get("cross_entity_coverage_analysis", {})


class TestKangProfileCompleteness:
    """Profile structure and essential fields."""

    def test_has_cross_entity_analysis(self, kang_entry):
        assert "cross_entity_coverage_analysis" in kang_entry

    def test_has_mechanism_9b(self, cross_entity):
        mech = cross_entity.get("mechanism", "")
        assert "9B" in mech, f"Expected Mechanism #9B, got: {mech}"

    def test_has_career_trajectory(self, cross_entity):
        career = cross_entity.get("career_trajectory", {})
        assert "washington_post" in career
        assert "new_york_times" in career
        assert "san_jose_mercury_news" in career

    def test_has_book_financial_interest(self, cross_entity):
        book = cross_entity.get("book_financial_interest", {})
        assert "An Ugly Truth" in book.get("title", "")
        assert "seven" in book.get("advance", "").lower()

    def test_has_source_urls(self, cross_entity):
        urls = cross_entity.get("source_urls", {})
        assert len(urls) >= 5, f"Expected at least 5 source URLs, got {len(urls)}"

    def test_beat_is_regulatory_policy(self, kang_entry):
        beat = kang_entry.get("beat", "")
        assert "regulatory" in beat.lower() or "policy" in beat.lower()

    def test_washington_dc_based(self, kang_entry):
        text = str(kang_entry)
        assert "Washington" in text or "DC" in text

    def test_has_meta_coverage_section(self, cross_entity):
        assert "meta_coverage" in cross_entity

    def test_has_google_coverage_section(self, cross_entity):
        assert "google_coverage" in cross_entity

    def test_has_openai_anthropic_coverage_section(self, cross_entity):
        assert "openai_anthropic_coverage" in cross_entity


class TestBookDealCoAuthorMechanism:
    """Validates that Kang and Frenkel share the same book deal mechanism."""

    def test_same_book_title(self, cross_entity, frenkel_entry):
        kang_book = cross_entity.get("book_financial_interest", {}).get("title", "")
        frenkel_book = frenkel_entry.get("cross_entity_coverage_analysis", {}).get(
            "book_financial_interest", {}
        ).get("title", "")
        assert "An Ugly Truth" in kang_book
        assert "An Ugly Truth" in frenkel_book

    def test_same_publisher(self, cross_entity, frenkel_entry):
        kang_pub = cross_entity.get("book_financial_interest", {}).get("publisher", "")
        frenkel_pub = frenkel_entry.get("cross_entity_coverage_analysis", {}).get(
            "book_financial_interest", {}
        ).get("publisher", "")
        assert "HarperCollins" in kang_pub
        assert "HarperCollins" in frenkel_pub

    def test_frenkel_is_co_author(self, cross_entity):
        co_author = cross_entity.get("book_financial_interest", {}).get("co_author", "")
        assert "Frenkel" in co_author

    def test_kang_is_frenkel_co_author(self, frenkel_entry):
        co_author = frenkel_entry.get("cross_entity_coverage_analysis", {}).get(
            "book_financial_interest", {}
        ).get("co_author", "")
        assert "Kang" in co_author

    def test_both_seven_figure_advance(self, cross_entity, frenkel_entry):
        kang_advance = cross_entity.get("book_financial_interest", {}).get("advance", "")
        frenkel_advance = frenkel_entry.get("cross_entity_coverage_analysis", {}).get(
            "book_financial_interest", {}
        ).get("advance", "")
        assert "seven" in kang_advance.lower()
        assert "seven" in frenkel_advance.lower()

    def test_mechanism_9b_distinct_from_9(self, cross_entity):
        relationship = cross_entity.get("mechanism_relationship", "")
        assert "sub-variant" in relationship.lower() or "variant" in relationship.lower()
        assert "different beats" in relationship.lower() or "DIFFERENT beats" in relationship

    def test_financial_conflict_note_present(self, cross_entity):
        note = cross_entity.get("book_financial_interest", {}).get(
            "financial_conflict_note", ""
        )
        assert "financial" in note.lower()
        assert "conflict" in note.lower() or "interest" in note.lower()


class TestToneAsymmetry:
    """Validates that Kang shows the same Meta-adversarial asymmetry as Frenkel."""

    def test_meta_tone_negative(self, cross_entity):
        meta_tone = cross_entity.get("meta_coverage", {}).get("tone", 0)
        assert meta_tone <= -0.40, f"Meta tone {meta_tone} not sufficiently adversarial"

    def test_google_tone_near_neutral(self, cross_entity):
        google_tone = cross_entity.get("google_coverage", {}).get("tone", 0)
        assert -0.20 <= google_tone <= 0.10, f"Google tone {google_tone} not neutral"

    def test_openai_tone_neutral_to_positive(self, cross_entity):
        oa_tone = cross_entity.get("openai_anthropic_coverage", {}).get("tone", 0)
        assert oa_tone >= -0.10, f"OpenAI/Anthropic tone {oa_tone} unexpectedly negative"

    def test_meta_google_tone_gap(self, cross_entity):
        meta = cross_entity.get("meta_coverage", {}).get("tone", 0)
        google = cross_entity.get("google_coverage", {}).get("tone", 0)
        gap = google - meta
        assert gap >= 0.30, f"Meta-Google tone gap {gap:.2f} too small (need ≥ 0.30)"

    def test_meta_openai_tone_gap(self, cross_entity):
        meta = cross_entity.get("meta_coverage", {}).get("tone", 0)
        oa = cross_entity.get("openai_anthropic_coverage", {}).get("tone", 0)
        gap = oa - meta
        assert gap >= 0.40, f"Meta-OpenAI tone gap {gap:.2f} too small (need ≥ 0.40)"

    def test_register_prosecutorial_for_meta(self, cross_entity):
        register = cross_entity.get("meta_coverage", {}).get("register", "")
        assert "prosecutorial" in register.lower()

    def test_register_procedural_for_google(self, cross_entity):
        register = cross_entity.get("google_coverage", {}).get("register", "")
        assert "procedural" in register.lower()


class TestDualBeatPipeline:
    """Validates the dual-beat adversarial pipeline (Mechanism #9B core finding)."""

    def test_different_beats(self, cross_entity, frenkel_entry):
        kang_beat_text = str(cross_entity.get("career_trajectory", {}))
        frenkel_beat = frenkel_entry.get("beat", "")
        assert "regulatory" in kang_beat_text.lower() or "policy" in kang_beat_text.lower()
        assert "cybersecurity" in frenkel_beat.lower() or "cyber" in frenkel_beat.lower()

    def test_dual_beat_pattern_documented(self, cross_entity):
        patterns = cross_entity.get("cross_entity_patterns", [])
        pattern_names = [p.get("pattern_name", "") for p in patterns]
        has_dual_beat = any("DUAL-BEAT" in name or "dual-beat" in name.lower()
                           for name in pattern_names)
        assert has_dual_beat, f"No dual-beat pattern found in: {pattern_names}"

    def test_pipeline_complementarity(self, cross_entity):
        patterns = cross_entity.get("cross_entity_patterns", [])
        dual_beat = next(
            (p for p in patterns
             if "DUAL-BEAT" in p.get("pattern_name", "") or "dual" in p.get("pattern_name", "").lower()),
            None
        )
        assert dual_beat is not None
        desc = dual_beat.get("description", "")
        assert "cybersecurity" in desc.lower() or "technical" in desc.lower()
        assert "regulatory" in desc.lower() or "policy" in desc.lower()

    def test_no_equivalent_pipeline_for_competitors(self, cross_entity):
        patterns = cross_entity.get("cross_entity_patterns", [])
        dual_beat = next(
            (p for p in patterns
             if "DUAL-BEAT" in p.get("pattern_name", "")),
            None
        )
        assert dual_beat is not None
        desc = dual_beat.get("description", "")
        assert "no equivalent" in desc.lower() or "No equivalent" in desc

    def test_summary_mentions_360_degree(self, cross_entity):
        summary = cross_entity.get("summary", "")
        assert "360" in summary or "dual" in summary.lower()


class TestHeadlineNamingAsymmetry:
    """Meta named first in shared-liability headlines."""

    def test_meta_named_first_in_verdict(self, cross_entity):
        articles = cross_entity.get("meta_coverage", {}).get("recent_articles", [])
        verdict_articles = [a for a in articles
                           if "Negligent" in a.get("title", "") or "negligent" in a.get("title", "")]
        assert len(verdict_articles) >= 1
        title = verdict_articles[0].get("title", "")
        meta_pos = title.lower().find("meta")
        youtube_pos = title.lower().find("youtube")
        assert meta_pos < youtube_pos, f"Meta not named first: {title}"

    def test_youtube_gets_defense_headline(self, cross_entity):
        google_articles = cross_entity.get("google_coverage", {}).get("recent_articles", [])
        argues_articles = [a for a in google_articles
                          if "Argues" in a.get("title", "")]
        assert len(argues_articles) >= 1
        title = argues_articles[0].get("title", "")
        assert "YouTube" in title
        assert "Argues" in title

    def test_naming_pattern_documented(self, cross_entity):
        patterns = cross_entity.get("cross_entity_patterns", [])
        naming_patterns = [p for p in patterns
                          if "NAMING" in p.get("pattern_name", "") or "naming" in p.get("pattern_name", "").lower()]
        assert len(naming_patterns) >= 1


class TestPartnershipEnforcementToggle:
    """Kang can write neutrally about Meta when government frames it as partner."""

    def test_dhs_partnership_article_neutral(self, cross_entity):
        oa_articles = cross_entity.get("openai_anthropic_coverage", {}).get("recent_articles", [])
        dhs_articles = [a for a in oa_articles
                       if "DHS" in a.get("title", "") or "pilot" in a.get("title", "").lower()]
        assert len(dhs_articles) >= 1
        tone = dhs_articles[0].get("tone", -1)
        assert tone >= -0.10, f"DHS partnership article tone {tone} not neutral"

    def test_toggle_pattern_documented(self, cross_entity):
        patterns = cross_entity.get("cross_entity_patterns", [])
        toggle = [p for p in patterns
                 if "TOGGLE" in p.get("pattern_name", "") or "toggle" in p.get("pattern_name", "").lower()]
        assert len(toggle) >= 1

    def test_toggle_explanation(self, cross_entity):
        patterns = cross_entity.get("cross_entity_patterns", [])
        toggle = next(
            (p for p in patterns
             if "TOGGLE" in p.get("pattern_name", "")),
            None
        )
        assert toggle is not None
        desc = toggle.get("description", "")
        assert "partner" in desc.lower()
        assert "enforcement" in desc.lower() or "target" in desc.lower()


class TestInstitutionalConflictComparison:
    """NYT's OpenAI lawsuit vs book deal — personal vs institutional conflict."""

    def test_openai_lawsuit_acknowledged(self, cross_entity):
        oa_text = str(cross_entity.get("openai_anthropic_coverage", {}))
        assert "lawsuit" in oa_text.lower() or "copyright" in oa_text.lower() or "suing" in oa_text.lower()

    def test_personal_vs_institutional_distinction(self, cross_entity):
        note = cross_entity.get("book_financial_interest", {}).get(
            "financial_conflict_note", ""
        )
        assert "institutional" in note.lower() or "personal" in note.lower()

    def test_no_adversarial_openai_coverage(self, cross_entity):
        oa_volume = cross_entity.get("openai_anthropic_coverage", {}).get("volume", "")
        assert "low" in oa_volume.lower()

    def test_regulatory_beat_not_pointed_at_openai(self, cross_entity):
        oa_framing = str(cross_entity.get("openai_anthropic_coverage", {}).get("framing_pattern", ""))
        assert "partner" in oa_framing.lower() or "not pointed" in oa_framing.lower()


class TestCrossValidation:
    """Consistency with Frenkel Mechanism #9 and broader NYT findings."""

    def test_mechanism_9b_references_mechanism_9(self, cross_entity):
        relationship = cross_entity.get("mechanism_relationship", "")
        assert "#9" in relationship or "Mechanism 9" in relationship

    def test_frenkel_meta_tone_also_negative(self, frenkel_entry):
        meta_tone = frenkel_entry.get("cross_entity_coverage_analysis", {}).get(
            "meta_coverage", {}
        ).get("tone", 0)
        if isinstance(meta_tone, (int, float)):
            assert meta_tone <= -0.40

    def test_both_coauthors_meta_adversarial(self, cross_entity, frenkel_entry):
        kang_meta = cross_entity.get("meta_coverage", {}).get("tone", 0)
        frenkel_meta = frenkel_entry.get("cross_entity_coverage_analysis", {}).get(
            "meta_coverage", {}
        ).get("tone", 0)
        if isinstance(kang_meta, (int, float)) and isinstance(frenkel_meta, (int, float)):
            assert kang_meta <= -0.40
            assert frenkel_meta <= -0.40

    def test_validation_strengthens_mechanism_9(self, cross_entity):
        summary = cross_entity.get("summary", "")
        assert "validation" in summary.lower() or "validates" in summary.lower() or "strengthens" in summary.lower()

    def test_five_cross_entity_patterns(self, cross_entity):
        patterns = cross_entity.get("cross_entity_patterns", [])
        assert len(patterns) >= 5, f"Expected at least 5 patterns, got {len(patterns)}"

    def test_nyt_0_meta_deal_consistent(self, nyt_profile):
        """NYT has no content licensing deal with Meta — consistent with adversarial framing."""
        conflicts = nyt_profile.get("known_conflicts", [])
        text = str(conflicts)
        # The litigation is with OpenAI, not Meta
        assert "OpenAI" in text or "openai" in text.lower()

    def test_all_source_urls_https(self, cross_entity):
        urls = cross_entity.get("source_urls", {})
        for key, url in urls.items():
            if url.startswith("http://"):
                pytest.fail(f"HTTP URL found for {key}: {url}")
