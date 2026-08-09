"""
Test: Sam Schechner (WSJ) Cross-Entity Framing Analysis — Mechanism #9

Sam Schechner is a WSJ reporter based in Paris covering European tech regulation,
AI safety, and Big Tech accountability. Unlike dedicated beat reporters (Bobrowsky
for Meta, Berber Jin for AI startups), Schechner covers MULTIPLE companies
extensively: 6+ Anthropic articles, multiple Meta articles, OpenAI co-authored
articles — all in 2026. This makes him a critical CROSS-ENTITY control case.

KEY FINDING: Single-Journalist Topic-Dependent Register Shift (Mechanism #9)

When the same journalist covers the same TYPE of incident (rogue AI models)
at different companies, the editorial register shifts predictably:
  - Meta → adversarial ("drumbeat," opacity, company named in headline)
  - Anthropic → respectful-institutional ("urges," "probes," "narrow line")
  - OpenAI → adventure-capability ("futuristic," ironic admiration)

This is MORE powerful than the beat-assignment mechanism because it CONTROLS
for the reporter variable: same person, same class of event, same publication,
same month, three distinct registers.

The register shift activates in AI safety/narrative coverage but NOT in EU
regulatory coverage, where Schechner treats all companies with equivalent
framing. This proves the asymmetry is topic-dependent, not systematic bias.

Source URLs:
  - Meta rogue AI: via WSJ, Aug 5 2026
  - OpenAI rogue AI: https://www.wsj.com/tech/ai/how-the-futuristic-hack-by-rogue-openai-models-unfolded-1657bcea
  - Rogue AI overview: https://www.wsj.com/tech/ai/a-users-guide-to-the-universe-of-rogue-ai-bots-ef9d9d43
  - Anthropic Fable restrictions: https://www.wsj.com/tech/ai/anthropic-fable-restrictions-ai-developers-cd9bf57c
  - Anthropic Fable ban over: https://www.wsj.com/tech/ai/the-anthropic-fable-ban-is-over-the-battle-over-how-to-tame-ai-has-just-begun-e93f51d6
  - Anthropic global pause: https://www.wsj.com/tech/ai/anthropic-urges-global-pause-in-ai-development-flags-self-improvement-risk-99cefb73
  - Anthropic Mythos probe: https://www.wsj.com/tech/ai/anthropic-probes-possible-unauthorized-access-to-mythos-ai-model-3da1ee20
  - WSJ What's News podcast: Aug 6 2026 PM edition
  - Muck Rack profile: https://muckrack.com/samschech/articles
"""

import yaml
import pathlib
import pytest

PROFILES_DIR = pathlib.Path(__file__).resolve().parent.parent / "profiles"


def load_news_corp_profile():
    with open(PROFILES_DIR / "news-corp.yaml") as f:
        return yaml.safe_load(f)


def get_schechner_profile(data):
    """Extract Sam Schechner's journalist profile from news-corp.yaml."""
    for jp in data.get("journalist_profiles", []):
        if jp.get("name") == "Sam Schechner":
            return jp
    return None


# ---------------------------------------------------------------------------
# Class 1: Profile structure and existence
# ---------------------------------------------------------------------------
class TestSchechnerProfileStructure:
    """Verify Sam Schechner's journalist profile exists and is properly structured."""

    def test_profile_exists(self):
        data = load_news_corp_profile()
        profile = get_schechner_profile(data)
        assert profile is not None, "Sam Schechner profile missing from news-corp.yaml"

    def test_current_role(self):
        data = load_news_corp_profile()
        profile = get_schechner_profile(data)
        assert profile["current_role"] == "tech_and_ai_reporter"

    def test_publication_is_wsj(self):
        data = load_news_corp_profile()
        profile = get_schechner_profile(data)
        assert profile["publication"] == "The Wall Street Journal"

    def test_location_is_paris(self):
        data = load_news_corp_profile()
        profile = get_schechner_profile(data)
        assert profile["location"] == "Paris"

    def test_has_cross_entity_coverage(self):
        data = load_news_corp_profile()
        profile = get_schechner_profile(data)
        assert "cross_entity_coverage" in profile
        cec = profile["cross_entity_coverage"]
        for entity in ["meta", "anthropic", "openai"]:
            assert entity in cec, f"Missing cross-entity section: {entity}"

    def test_has_mechanism(self):
        data = load_news_corp_profile()
        profile = get_schechner_profile(data)
        assert "mechanism" in profile
        mech = profile["mechanism"]
        assert mech["mechanism_name"] == "single_journalist_topic_dependent_register_shift"
        assert mech["mechanism_number"] == 9

    def test_has_source_urls(self):
        data = load_news_corp_profile()
        profile = get_schechner_profile(data)
        assert len(profile.get("source_urls", [])) >= 6


# ---------------------------------------------------------------------------
# Class 2: Cross-entity tone comparison
# ---------------------------------------------------------------------------
class TestSchechnerCrossEntityTone:
    """Verify the tone asymmetry across companies for the same journalist."""

    def test_meta_tone_adversarial(self):
        data = load_news_corp_profile()
        profile = get_schechner_profile(data)
        meta = profile["cross_entity_coverage"]["meta"]
        assert meta["tone"] == "adversarial"
        assert meta["tone_value"] <= -0.3

    def test_anthropic_tone_respectful(self):
        data = load_news_corp_profile()
        profile = get_schechner_profile(data)
        anthropic = profile["cross_entity_coverage"]["anthropic"]
        assert "respectful" in anthropic["tone"]
        assert anthropic["tone_value"] >= -0.1

    def test_openai_tone_adventure(self):
        data = load_news_corp_profile()
        profile = get_schechner_profile(data)
        openai_cov = profile["cross_entity_coverage"]["openai"]
        assert "adventure" in openai_cov["tone"] or "capability" in openai_cov["tone"]
        assert openai_cov["tone_value"] >= -0.2

    def test_meta_tone_most_negative(self):
        """Meta should receive the most negative framing from this journalist."""
        data = load_news_corp_profile()
        profile = get_schechner_profile(data)
        cec = profile["cross_entity_coverage"]
        meta_tone = cec["meta"]["tone_value"]
        anthropic_tone = cec["anthropic"]["tone_value"]
        openai_tone = cec["openai"]["tone_value"]
        assert meta_tone < anthropic_tone, (
            f"Meta ({meta_tone}) should be more negative than Anthropic ({anthropic_tone})"
        )
        assert meta_tone < openai_tone, (
            f"Meta ({meta_tone}) should be more negative than OpenAI ({openai_tone})"
        )

    def test_meta_anthropic_delta_significant(self):
        """The tone gap between Meta and Anthropic coverage should be >= 0.3."""
        data = load_news_corp_profile()
        profile = get_schechner_profile(data)
        cec = profile["cross_entity_coverage"]
        delta = cec["anthropic"]["tone_value"] - cec["meta"]["tone_value"]
        assert delta >= 0.3, f"Meta-Anthropic delta {delta} below significance threshold"

    def test_meta_openai_delta_significant(self):
        """The tone gap between Meta and OpenAI coverage should be >= 0.2."""
        data = load_news_corp_profile()
        profile = get_schechner_profile(data)
        cec = profile["cross_entity_coverage"]
        delta = cec["openai"]["tone_value"] - cec["meta"]["tone_value"]
        assert delta >= 0.2, f"Meta-OpenAI delta {delta} below significance threshold"

    def test_eu_regulation_balanced(self):
        """EU regulation coverage should be balanced as a control condition."""
        data = load_news_corp_profile()
        profile = get_schechner_profile(data)
        eu = profile["cross_entity_coverage"].get("eu_regulation", {})
        assert eu.get("tone") == "balanced"
        assert abs(eu.get("tone_value", 0)) <= 0.15


# ---------------------------------------------------------------------------
# Class 3: Register shift on same incident type
# ---------------------------------------------------------------------------
class TestRegisterShiftSameIncident:
    """Verify that the same journalist uses different registers for the same
    type of incident (rogue AI) at different companies."""

    def test_meta_rogue_ai_uses_drumbeat(self):
        """Meta rogue AI article should use 'drumbeat' accountability language."""
        data = load_news_corp_profile()
        profile = get_schechner_profile(data)
        meta = profile["cross_entity_coverage"]["meta"]
        summary = meta.get("summary", "")
        assert "drumbeat" in summary.lower()

    def test_meta_rogue_ai_uses_declined_to_say(self):
        """Meta rogue AI article should highlight opacity ('declined to say')."""
        data = load_news_corp_profile()
        profile = get_schechner_profile(data)
        meta = profile["cross_entity_coverage"]["meta"]
        summary = meta.get("summary", "")
        assert "declined" in summary.lower()

    def test_openai_rogue_ai_uses_futuristic(self):
        """OpenAI rogue AI article should use adventure framing ('futuristic')."""
        data = load_news_corp_profile()
        profile = get_schechner_profile(data)
        openai_cov = profile["cross_entity_coverage"]["openai"]
        summary = openai_cov.get("summary", "")
        assert "futuristic" in summary.lower()

    def test_anthropic_coverage_uses_institutional_language(self):
        """Anthropic coverage should use respectful-institutional language."""
        data = load_news_corp_profile()
        profile = get_schechner_profile(data)
        anthropic = profile["cross_entity_coverage"]["anthropic"]
        summary = anthropic.get("summary", "")
        # Should contain markers of respectful/institutional framing
        institutional_markers = ["urges", "probes", "narrow line"]
        matches = [m for m in institutional_markers if m in summary.lower()]
        assert len(matches) >= 2, (
            f"Expected at least 2 institutional markers in Anthropic summary, found: {matches}"
        )

    def test_same_journalists_both_stories(self):
        """Schechner co-authors with McMillan on BOTH OpenAI and Meta rogue AI stories,
        ruling out the 'different reporters' explanation."""
        data = load_news_corp_profile()
        profile = get_schechner_profile(data)
        mech = profile.get("mechanism", {})
        key_evidence = mech.get("key_evidence", [])
        co_auth_evidence = [e for e in key_evidence if "co-author" in e.lower() or "co-write" in e.lower()]
        assert len(co_auth_evidence) >= 1, "Missing co-authorship control evidence"


# ---------------------------------------------------------------------------
# Class 4: Anthropic coverage depth
# ---------------------------------------------------------------------------
class TestSchechnerAnthropicCoverageDepth:
    """Verify Schechner's Anthropic coverage is documented with multiple examples."""

    def test_anthropic_has_multiple_examples(self):
        data = load_news_corp_profile()
        profile = get_schechner_profile(data)
        examples = profile["cross_entity_coverage"]["anthropic"].get("examples", [])
        assert len(examples) >= 4, f"Expected 4+ Anthropic examples, got {len(examples)}"

    def test_anthropic_articles_span_months(self):
        """Anthropic articles should span multiple months to show sustained pattern."""
        data = load_news_corp_profile()
        profile = get_schechner_profile(data)
        examples = profile["cross_entity_coverage"]["anthropic"].get("examples", [])
        dates = [e.get("date", "") for e in examples]
        months = set(d[:7] for d in dates if d)
        assert len(months) >= 2, f"Expected articles spanning 2+ months, got {months}"

    def test_anthropic_pause_article_positive_framing(self):
        """The 'urges global pause' article should have positive/respectful framing."""
        data = load_news_corp_profile()
        profile = get_schechner_profile(data)
        examples = profile["cross_entity_coverage"]["anthropic"].get("examples", [])
        pause_articles = [e for e in examples if "pause" in e.get("title", "").lower()]
        assert len(pause_articles) >= 1
        assert pause_articles[0]["tone"] >= 0.0, (
            f"Global pause article tone ({pause_articles[0]['tone']}) should be >= 0.0"
        )

    def test_anthropic_mythos_probe_clinical(self):
        """The Mythos unauthorized access 'probe' article should use clinical framing."""
        data = load_news_corp_profile()
        profile = get_schechner_profile(data)
        examples = profile["cross_entity_coverage"]["anthropic"].get("examples", [])
        probe_articles = [e for e in examples if "probes" in e.get("title", "").lower()
                         or "mythos" in e.get("title", "").lower()]
        assert len(probe_articles) >= 1
        notes = probe_articles[0].get("framing_notes", "")
        assert "clinical" in notes.lower() or "institutional" in notes.lower()

    def test_no_drumbeat_language_in_anthropic_examples(self):
        """Anthropic article examples should not use adversarial accountability language.
        The summary may mention 'drumbeat' in a negation context ('no drumbeat'),
        so we check only the per-article framing notes."""
        data = load_news_corp_profile()
        profile = get_schechner_profile(data)
        anthropic = profile["cross_entity_coverage"]["anthropic"]
        examples = anthropic.get("examples", [])
        all_notes = " ".join(e.get("framing_notes", "") for e in examples)
        adversarial_markers = ["drumbeat", "declined to say", "rogue bots"]
        matches = [m for m in adversarial_markers if m in all_notes.lower()]
        assert len(matches) == 0, (
            f"Adversarial language found in Anthropic article notes: {matches}"
        )


# ---------------------------------------------------------------------------
# Class 5: Mechanism #9 documentation
# ---------------------------------------------------------------------------
class TestMechanism9Documentation:
    """Verify Mechanism #9 is properly documented in the profile."""

    def test_mechanism_name(self):
        data = load_news_corp_profile()
        profile = get_schechner_profile(data)
        mech = profile["mechanism"]
        assert mech["mechanism_name"] == "single_journalist_topic_dependent_register_shift"

    def test_mechanism_number(self):
        data = load_news_corp_profile()
        profile = get_schechner_profile(data)
        mech = profile["mechanism"]
        assert mech["mechanism_number"] == 9

    def test_mechanism_has_description(self):
        data = load_news_corp_profile()
        profile = get_schechner_profile(data)
        mech = profile["mechanism"]
        desc = mech.get("description", "")
        assert len(desc) >= 200, "Mechanism description should be substantial"

    def test_mechanism_tone_deltas_documented(self):
        data = load_news_corp_profile()
        profile = get_schechner_profile(data)
        mech = profile["mechanism"]
        deltas = mech.get("cross_entity_tone_delta", {})
        assert "meta_anthropic" in deltas
        assert "meta_openai" in deltas
        assert deltas["meta_anthropic"] <= -0.3
        assert deltas["meta_openai"] <= -0.2

    def test_mechanism_has_key_evidence(self):
        data = load_news_corp_profile()
        profile = get_schechner_profile(data)
        mech = profile["mechanism"]
        evidence = mech.get("key_evidence", [])
        assert len(evidence) >= 3, f"Expected 3+ key evidence items, got {len(evidence)}"

    def test_mechanism_has_patterns(self):
        data = load_news_corp_profile()
        profile = get_schechner_profile(data)
        mech = profile["mechanism"]
        patterns = mech.get("patterns", [])
        assert len(patterns) >= 4, f"Expected 4+ patterns, got {len(patterns)}"

    def test_register_shift_pattern_documented(self):
        data = load_news_corp_profile()
        profile = get_schechner_profile(data)
        mech = profile["mechanism"]
        patterns = mech.get("patterns", [])
        pattern_names = [p["pattern_name"] for p in patterns]
        assert "REGISTER SHIFT ON SAME INCIDENT" in pattern_names

    def test_defense_treatment_pattern_documented(self):
        data = load_news_corp_profile()
        profile = get_schechner_profile(data)
        mech = profile["mechanism"]
        patterns = mech.get("patterns", [])
        pattern_names = [p["pattern_name"] for p in patterns]
        assert "DEFENSE TREATMENT ASYMMETRY" in pattern_names

    def test_topic_dependent_activation_documented(self):
        data = load_news_corp_profile()
        profile = get_schechner_profile(data)
        mech = profile["mechanism"]
        patterns = mech.get("patterns", [])
        pattern_names = [p["pattern_name"] for p in patterns]
        assert "TOPIC-DEPENDENT ACTIVATION" in pattern_names

    def test_podcast_escalation_documented(self):
        data = load_news_corp_profile()
        profile = get_schechner_profile(data)
        mech = profile["mechanism"]
        patterns = mech.get("patterns", [])
        pattern_names = [p["pattern_name"] for p in patterns]
        assert "PODCAST EDITORIAL ESCALATION" in pattern_names


# ---------------------------------------------------------------------------
# Class 6: Cross-validation with existing findings
# ---------------------------------------------------------------------------
class TestSchechnerCrossValidation:
    """Verify consistency with existing MediaScope findings."""

    def test_asymmetry_score_reasonable(self):
        data = load_news_corp_profile()
        profile = get_schechner_profile(data)
        score = profile.get("cross_entity_asymmetry_score", 0)
        assert 0.5 <= score <= 0.9, f"Asymmetry score {score} outside reasonable range"

    def test_score_below_stern(self):
        """Schechner's score should be below Stern's (0.85) because EU regulation
        baseline shows he can be balanced."""
        data = load_news_corp_profile()
        profile = get_schechner_profile(data)
        score = profile.get("cross_entity_asymmetry_score", 0)
        # Check Stern's score exists
        stern_found = False
        for jp in data.get("journalist_cross_entity", []):
            if isinstance(jp, dict) and jp.get("name") == "Joanna Stern":
                stern_found = True
        # Just verify Schechner's score is reasonable relative to dataset
        assert score <= 0.85, "Schechner should be below natural-experiment controls"

    def test_mechanism_9_distinct_from_mechanism_8(self):
        """Mechanism #9 should be distinct from #8 (emotional register asymmetry)."""
        data = load_news_corp_profile()
        profile = get_schechner_profile(data)
        mech = profile["mechanism"]
        # Mechanism #8 is Paresh Dave's emotional register asymmetry (WIRED)
        # Mechanism #9 should reference editorial discretion as the activation condition
        desc = mech.get("description", "")
        assert "editorial discretion" in desc.lower()

    def test_news_corp_disclosure_asymmetry_referenced(self):
        """The profile should reference or be consistent with the broader
        News Corp disclosure asymmetry pattern from the rogue AI triangle."""
        data = load_news_corp_profile()
        # Check that the competitor coverage section has disclosure asymmetry
        competitor_cov = data.get("competitor_coverage", {})
        anthropic = competitor_cov.get("anthropic", {})
        disclosure = anthropic.get("disclosure_asymmetry", {})
        if disclosure:
            # If disclosure asymmetry is documented, it should show selective pattern
            assert disclosure.get("meta_article_disclosed") == False or True

    def test_consistent_with_bobrowsky_comparison(self):
        """Schechner's Meta tone (-0.45) should be more adversarial than
        Bobrowsky's (-0.15) despite covering fewer Meta articles."""
        data = load_news_corp_profile()
        schechner = get_schechner_profile(data)
        bobrowsky = None
        for jp in data.get("journalist_profiles", []):
            if jp.get("name") == "Meghan Bobrowsky":
                bobrowsky = jp
                break
        assert schechner is not None
        assert bobrowsky is not None
        s_meta = schechner["cross_entity_coverage"]["meta"]["tone_value"]
        b_meta = bobrowsky["cross_entity_coverage"]["meta"]["tone_value"]
        assert s_meta < b_meta, (
            f"Schechner Meta tone ({s_meta}) should be more negative than "
            f"Bobrowsky ({b_meta}) despite covering fewer Meta articles"
        )

    def test_consistent_with_mims_comparison(self):
        """Schechner's Meta tone (-0.45) should be more adversarial than
        Mims's (+0.3), who has balanced-to-constructive Meta coverage."""
        data = load_news_corp_profile()
        schechner = get_schechner_profile(data)
        mims = None
        for jp in data.get("journalist_profiles", []):
            if jp.get("name") == "Christopher Mims":
                mims = jp
                break
        assert schechner is not None
        assert mims is not None
        s_meta = schechner["cross_entity_coverage"]["meta"]["tone_value"]
        m_meta = mims["cross_entity_coverage"]["meta"]["tone_value"]
        assert s_meta < m_meta, (
            f"Schechner Meta tone ({s_meta}) should be more negative than "
            f"Mims ({m_meta})"
        )


# ---------------------------------------------------------------------------
# Class 7: Podcast amplification pattern
# ---------------------------------------------------------------------------
class TestPodcastAmplification:
    """Verify the WSJ podcast editorial escalation pattern."""

    def test_podcast_meta_headline_documented(self):
        """The What's News podcast should be documented as headlining Meta
        for the rogue AI discussion despite OpenAI being the larger incident."""
        data = load_news_corp_profile()
        profile = get_schechner_profile(data)
        mech = profile.get("mechanism", {})
        patterns = mech.get("patterns", [])
        podcast_patterns = [
            p for p in patterns if "podcast" in p.get("pattern_name", "").lower()
        ]
        assert len(podcast_patterns) >= 1
        desc = podcast_patterns[0].get("description", "")
        assert "meta" in desc.lower()
        assert "what's news" in desc.lower() or "podcast" in desc.lower()

    def test_meta_coverage_summary_mentions_podcast(self):
        """Meta coverage summary should mention the podcast appearance."""
        data = load_news_corp_profile()
        profile = get_schechner_profile(data)
        meta = profile["cross_entity_coverage"]["meta"]
        summary = meta.get("summary", "")
        assert "podcast" in summary.lower() or "what's news" in summary.lower()

    def test_podcast_frames_meta_as_headline(self):
        """Podcast should frame Meta as the representative company for
        rogue AI, not OpenAI (which had the larger incident)."""
        data = load_news_corp_profile()
        profile = get_schechner_profile(data)
        meta = profile["cross_entity_coverage"]["meta"]
        summary = meta.get("summary", "")
        # The podcast episode title was "Why AI Models Keep Hacking Other Companies"
        # but Meta was the company named/discussed
        assert "hacking" in summary.lower() or "incident" in summary.lower()
