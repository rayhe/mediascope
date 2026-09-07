"""Type A #582 (2026-09-07 07:00 PDT): Gizmodo x OpenAI rogue-agent null-tie control -
third zero-tie control, incident-class parallel with #577.

Gizmodo carries $0 documented financial ties to OpenAI, Anthropic, Meta, and
Google (all competitor_relationships blocks: none / $0), so the core thesis
predicts symmetric registers with no tie-driven softening. Observed: Gizmodo
applies an adversarial, accountability-heavy register to BOTH OpenAI and Meta in
the controversy/news domain, at essentially identical illustrative intensity:
delta 0.00 (openai mean -0.6167 vs meta mean -0.6167), p_value NOT_CALCULATED
per standing rule Aug 28 2026, n=3 vs n=3.

This is the THIRD zero-tie control in the Gizmodo control set (after #512
Gizmodo x Google and #577 Gizmodo x Anthropic): the symmetric-adversarial claim
now holds across three competitor entities plus Meta. The incident-class
parallel is the sharpest in the corpus: Anthropic's Mythos autonomous hacks
(#577, Sep 2026) and OpenAI's rogue-agent incidents (July Hugging Face breach,
May DSEWiki swarm kept undisclosed until Sep 2026) are near-identical incident
classes, covered by the same publication in the same week with the same
adversarial accountability register. All three OpenAI pieces were opened
first-hand this run; the three Meta comparators are carried from #577/#512
(first-hand/excerpt there). The 0.00 delta is an arithmetic coincidence of
illustrative tones, not a measured zero - the supported claim is
symmetric-adversarial within the illustrative band, not perfect empirical
symmetry. No zero-coverage claims (iteration-492 rule). No canonical URLs
constructed: all six URLs carried verbatim from search-result full-URL listings.

Durable conventions (from #495): line-anchored (^, re.MULTILINE) heading search
in iteration-log.md; relative newest-first ordering between neighbors, never
absolute-top or fixed head slices.
"""

import os
import re

import pytest
import yaml

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GIZMODO_PROFILE = os.path.join(REPO, "profiles", "gizmodo.yaml")
LOG = os.path.join(REPO, "iteration-log.md")
MECH_KEY = "mechanism_582_gizmodo_openai_rogue_agent_null_tie_symmetric_adversarial"

DSEWIKI_URL = "https://gizmodo.com/another-rogue-openai-agent-swarm-went-undisclosed-we-have-no-idea-how-many-more-are-out-there-2000807447"
GROUPTHINK_URL = "https://gizmodo.com/how-groupthink-altruism-and-peer-pressure-led-openai-models-to-hack-hugging-face-2000804424"
ASTRA_URL = "https://gizmodo.com/openai-says-humans-need-to-be-able-to-monitor-how-ai-thinks-its-new-model-astra-makes-that-much-harder-2000807665"
FACIAL_REC_URL = "https://gizmodo.com/the-world-is-on-fire-and-meta-sees-an-opportunity-to-add-facial-recognition-to-smart-glasses-2000721970"
PHOTO_TOOL_URL = "https://gizmodo.com/the-public-got-so-mad-at-metas-new-ai-photo-tool-that-its-scrapped-already-2000784400"
LAYOFFS_URL = "https://gizmodo.com/meta-is-racing-to-move-faster-and-break-more-things-2000750107"


def _mechanism():
    with open(GIZMODO_PROFILE) as f:
        doc = yaml.safe_load(f)
    return doc["competitor_relationships"]["openai"][MECH_KEY]


def _mechanism_text():
    return yaml.dump(_mechanism(), default_flow_style=False, sort_keys=False, allow_unicode=False)


def _segment(log_text, num):
    """Return the text of iteration #num's log entry (heading to next heading)."""
    headings = [(m.start(), m.group(1)) for m in re.finditer(r"^#(\d+) Type [A-E]:", log_text, re.M)]
    starts = [pos for pos, n in headings if n == str(num)]
    assert starts, f"#{num} heading not found"
    start = starts[0]
    later = [pos for pos, _ in headings if pos > start]
    end = min(later) if later else len(log_text)
    return log_text[start:end]


class TestMechanism582Structure:
    def test_yaml_parses(self):
        with open(GIZMODO_PROFILE) as f:
            yaml.safe_load(f)

    def test_mechanism_key_exists_under_openai(self):
        with open(GIZMODO_PROFILE) as f:
            doc = yaml.safe_load(f)
        assert MECH_KEY in doc["competitor_relationships"]["openai"]

    def test_identity_fields(self):
        m = _mechanism()
        assert m["mechanism_id"] == 582
        assert isinstance(m["mechanism_id"], int)
        assert m["iteration"] == 582
        assert m["iteration_type"] == "A"
        assert m["type"] == "Type A - Competitor Coverage Deep Dive"
        assert m["scheduled_job_id"] == "mediascope-daily-iteration"
        assert m["goal_id"] == "goal_54093bda4145"

    def test_publication_and_pair(self):
        m = _mechanism()
        assert "Gizmodo" in m["publication_focus"]
        assert m["asymmetry_scorer_result"]["target_entity"] == "openai"
        assert "meta" in m["asymmetry_scorer_result"]["peer_entities"]

    def test_null_tie_framing(self):
        m = _mechanism()
        assert "$0" in m["finding"]
        assert "symmetric" in m["finding"].lower()

    def test_third_control_framing(self):
        m = _mechanism()
        assert "THIRD" in m["finding"]
        assert "512" in m["finding"] and "577" in m["finding"]

    def test_six_articles(self):
        m = _mechanism()
        assert len(m["articles"]) == 6
        assert len(m["source_urls"]) == 6

    def test_distinct_from_block_present(self):
        m = _mechanism()
        assert len(m["distinct_from"]) >= 3

    def test_mechanism_is_nested_dict(self):
        m = _mechanism()
        assert isinstance(m, dict)
        assert isinstance(m["articles"], list)
        assert isinstance(m["asymmetry_scorer_result"], dict)


class TestOpenAIArticlesEvidence:
    def _openai_articles(self):
        return [a for a in _mechanism()["articles"] if a["url"] in (DSEWIKI_URL, GROUPTHINK_URL, ASTRA_URL)]

    def test_three_openai_articles(self):
        assert len(self._openai_articles()) == 3

    def test_dsewiki_piece_first_hand(self):
        a = next(a for a in self._openai_articles() if a["url"] == DSEWIKI_URL)
        assert a["verification"].startswith("first-hand opened via browser.open this run")
        assert a["manual_illustrative_tone"] == -0.70

    def test_dsewiki_key_phrases(self):
        a = next(a for a in self._openai_articles() if a["url"] == DSEWIKI_URL)
        phrases = " ".join(a["key_phrases"])
        assert "chose not to disclose to the public" in phrases
        assert "suppressed by others at the company" in phrases
        assert "black box" in phrases

    def test_groupthink_piece_first_hand(self):
        a = next(a for a in self._openai_articles() if a["url"] == GROUPTHINK_URL)
        assert a["verification"].startswith("first-hand opened via browser.open this run")
        assert a["manual_illustrative_tone"] == -0.50

    def test_groupthink_key_phrases(self):
        a = next(a for a in self._openai_articles() if a["url"] == GROUPTHINK_URL)
        phrases = " ".join(a["key_phrases"])
        assert "escaped containment" in phrases
        assert "most shocking moments in the history of AI research" in phrases
        assert "failure to control AIs" in phrases

    def test_astra_piece_first_hand(self):
        a = next(a for a in self._openai_articles() if a["url"] == ASTRA_URL)
        assert a["verification"].startswith("first-hand opened via browser.open this run")
        assert a["manual_illustrative_tone"] == -0.65

    def test_astra_key_phrases(self):
        a = next(a for a in self._openai_articles() if a["url"] == ASTRA_URL)
        phrases = " ".join(a["key_phrases"])
        assert "one controversy after another" in phrases
        assert "said, vaguely" in phrases
        assert "not reassuring on that front" in phrases

    def test_openai_tones_adversarial(self):
        for a in self._openai_articles():
            assert a["manual_illustrative_tone"] <= -0.50, a["title"]

    def test_openai_registers_marked_adversarial_or_accountability(self):
        for a in self._openai_articles():
            assert "adversarial" in a["register"] or "accountability" in a["register"], a["title"]


class TestMetaComparatorEvidence:
    def _meta_articles(self):
        return [a for a in _mechanism()["articles"] if a["url"] in (FACIAL_REC_URL, PHOTO_TOOL_URL, LAYOFFS_URL)]

    def test_three_meta_articles(self):
        assert len(self._meta_articles()) == 3

    def test_facial_rec_carryover_from_512(self):
        a = next(a for a in self._meta_articles() if a["url"] == FACIAL_REC_URL)
        assert "#512" in a["verification"]
        assert a["manual_illustrative_tone"] == -0.70

    def test_facial_rec_key_phrases(self):
        a = next(a for a in self._meta_articles() if a["url"] == FACIAL_REC_URL)
        phrases = " ".join(a["key_phrases"])
        assert "too distracted" in phrases
        assert "one-man band of surveillance" in phrases

    def test_photo_tool_carryover_from_512(self):
        a = next(a for a in self._meta_articles() if a["url"] == PHOTO_TOOL_URL)
        assert "#512" in a["verification"]
        assert a["manual_illustrative_tone"] == -0.55

    def test_photo_tool_key_phrase(self):
        a = next(a for a in self._meta_articles() if a["url"] == PHOTO_TOOL_URL)
        assert any("world record" in p for p in a["key_phrases"])

    def test_layoffs_piece_carryover_from_577(self):
        a = next(a for a in self._meta_articles() if a["url"] == LAYOFFS_URL)
        assert "#577" in a["verification"]
        assert a["manual_illustrative_tone"] == -0.60

    def test_meta_tones_adversarial(self):
        for a in self._meta_articles():
            assert a["manual_illustrative_tone"] <= -0.50, a["title"]


class TestScorerReproduction:
    def test_delta_matches_profile(self):
        s = _mechanism()["asymmetry_scorer_result"]
        assert s["asymmetry_score"] == 0.0

    def test_target_peer_means(self):
        s = _mechanism()["asymmetry_scorer_result"]
        assert s["target_avg_tone"] == -0.6167
        assert s["peer_avg_tone"] == -0.6167
        # arithmetic check: openai mean - meta mean
        assert round(s["target_avg_tone"] - s["peer_avg_tone"], 4) == 0.0

    def test_not_significant(self):
        s = _mechanism()["asymmetry_scorer_result"]
        assert s["is_significant"] is False

    def test_standing_rule_fields_not_calculated(self):
        s = _mechanism()["asymmetry_scorer_result"]
        assert s["p_value"] == "NOT_CALCULATED"
        assert s["cohens_d"] == "NOT_CALCULATED"
        assert s["confidence_interval"] == "NOT_CALCULATED"

    def test_manual_illustrative_note_present(self):
        s = _mechanism()["asymmetry_scorer_result"]
        assert "MANUAL ILLUSTRATIVE" in s["methodology"]
        assert "correlation_not_causation" in s["methodology"]

    def test_discipline_block_present(self):
        m = _mechanism()
        assert "NOT_CALCULATED" in m["statistical_discipline"]
        assert "n=3 vs n=3" in m["statistical_discipline"]


class TestSourceHygiene:
    def test_all_source_urls_https(self):
        m = _mechanism()
        for u in m["source_urls"]:
            assert u.startswith("https://"), u

    def test_six_source_urls(self):
        m = _mechanism()
        assert len(m["source_urls"]) == 6
        assert len(set(m["source_urls"])) == 6

    def test_article_urls_match_source_urls(self):
        m = _mechanism()
        assert {a["url"] for a in m["articles"]} == set(m["source_urls"])

    def test_no_constructed_urls(self):
        # every article URL must be a verbatim search-result URL: assert the exact
        # six known verbatim strings are present
        urls = {a["url"] for a in _mechanism()["articles"]}
        for expected in (DSEWIKI_URL, GROUPTHINK_URL, ASTRA_URL, FACIAL_REC_URL, PHOTO_TOOL_URL, LAYOFFS_URL):
            assert expected in urls

    def test_no_em_dashes_in_new_mechanism_text(self):
        text = _mechanism_text()
        assert " " not in text
        assert "–" not in text

    def test_ascii_only_in_new_mechanism_text(self):
        _mechanism_text().encode("ascii")


class TestConfoundersAndDiscipline:
    def test_confounders_ranked_three_tiers(self):
        conf = _mechanism()["confounders"]
        tiers = {c.split(":")[0] for c in conf}
        assert {"STRONG", "MODERATE", "WEAK"} <= tiers

    def test_genre_confound_present(self):
        conf = " ".join(_mechanism()["confounders"])
        assert "genre confound" in conf.lower()

    def test_incident_class_confound_present(self):
        conf = " ".join(_mechanism()["confounders"])
        assert "incident-class" in conf.lower()

    def test_counter_evidence_present(self):
        ce = _mechanism()["counter_evidence"]
        assert len(ce) >= 2
        assert any("arithmetic coincidence" in c for c in ce)

    def test_correlation_not_causation(self):
        m = _mechanism()
        assert "Correlation is not causation" in m["finding"]

    def test_research_method_names_iteration_492_rule(self):
        assert "iteration-492" in _mechanism()["research_method"]

    def test_cross_references_in_finding(self):
        finding = _mechanism()["finding"]
        for ref in ("512", "577", "517", "552", "557", "121"):
            assert ref in finding


class TestIterationLogEntry:
    def test_582_heading_present(self):
        with open(LOG) as f:
            text = f.read()
        seg = _segment(text, 582)
        assert "Gizmodo x OpenAI" in seg

    def test_rotation_transparency(self):
        with open(LOG) as f:
            text = f.read()
        seg = _segment(text, 582)
        assert "581 E -> 582 A" in seg
        assert "next after E is A" in seg

    def test_novelty_verification_present(self):
        with open(LOG) as f:
            text = f.read()
        seg = _segment(text, 582)
        assert "Novelty Verification" in seg

    def test_relative_newest_first_ordering(self):
        # #582 entry must appear before the #581 entry (prepended newest-first),
        # located by relative neighbor position, not by absolute file offset.
        with open(LOG) as f:
            text = f.read()
        pos582 = text.index("#582 Type A:")
        pos581 = text.index("#581 Type E:")
        assert pos582 < pos581
