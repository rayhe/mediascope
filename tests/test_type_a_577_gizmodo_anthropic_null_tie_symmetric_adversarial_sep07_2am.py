"""Type A #577 (2026-09-07 02:00 PDT): Gizmodo x Anthropic null-tie control -
symmetric adversarial register toward a second deal-absent entity.

Gizmodo carries $0 documented financial ties to Anthropic, Meta, OpenAI, and
Google (all competitor_relationships blocks: none / $0), so the core thesis
predicts symmetric registers with no tie-driven softening. Observed: Gizmodo
applies an adversarial, sarcastic register to BOTH Anthropic and Meta in the
controversy/news domain, with a +0.12 tone lean toward Anthropic that is not
significant (p_value NOT_CALCULATED per standing rule Aug 28 2026, n=3 vs n=3).

This is the SECOND zero-tie control in the Gizmodo control pair (after #512
Gizmodo x Google): the symmetric-adversarial claim now holds across two
competitor entities. It bounds the thesis claim so that softening at deal
publications (FT-OpenAI, Verge-OpenAI product domain #425) cannot be
dismissed as generic big-tech house style - Gizmodo's house style is
equal-opportunity adversarial and it shows here, symmetric. The claim is
explicitly domain-bounded: Gizmodo's business-domain Anthropic items
(Project Glasswing launch, TeraWulf 20-year lease) run neutral-business, so
the symmetric-adversarial claim covers controversy/news coverage only.

Statistical discipline: MANUAL ILLUSTRATIVE tones at article level, n=3 vs n=3.
Mean-delta arithmetic reproduced this run: delta 0.12, p_value
NOT_CALCULATED, cohens_d NOT_CALCULATED, ci NOT_CALCULATED, is_significant
False. No significance claimed or claimable. correlation_not_causation. Two
of three Anthropic articles opened first-hand this run; the autonomous-hacks
piece and the Meta layoffs comparator are excerpt-bounded second-hand (marked
in-mechanism). Meta facial-recognition and photo-tool pieces were
first-hand/excerpt in #512 with URLs re-verified verbatim this run. No
zero-coverage claims (iteration-492 rule). No canonical URLs constructed: all
six URLs carried verbatim from search-result full-URL listings.

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
MECH_KEY = "mechanism_577_gizmodo_anthropic_null_tie_symmetric_adversarial"

HACKS_URL = "https://gizmodo.com/?p=2000805796"
SETTLEMENT_URL = "https://gizmodo.com/anthropic-agrees-to-1-5-billion-settlement-for-downloading-pirated-books-to-train-ai-2000654666"
MYTHOS_URL = "https://gizmodo.com/anthropic-releases-a-safer-version-of-its-too-dangerous-mythos-ai-2000769492"
FACIAL_REC_URL = "https://gizmodo.com/the-world-is-on-fire-and-meta-sees-an-opportunity-to-add-facial-recognition-to-smart-glasses-2000721970"
PHOTO_TOOL_URL = "https://gizmodo.com/the-public-got-so-mad-at-metas-new-ai-photo-tool-that-its-scrapped-already-2000784400"
LAYOFFS_URL = "https://gizmodo.com/meta-is-racing-to-move-faster-and-break-more-things-2000750107"


def _mechanism():
    with open(GIZMODO_PROFILE) as f:
        doc = yaml.safe_load(f)
    return doc["competitor_relationships"]["anthropic"][MECH_KEY]


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


class TestMechanism577Structure:
    def test_yaml_parses(self):
        with open(GIZMODO_PROFILE) as f:
            yaml.safe_load(f)

    def test_mechanism_key_exists_under_anthropic(self):
        with open(GIZMODO_PROFILE) as f:
            doc = yaml.safe_load(f)
        assert MECH_KEY in doc["competitor_relationships"]["anthropic"]

    def test_identity_fields(self):
        m = _mechanism()
        assert m["mechanism_id"] == 577
        assert isinstance(m["mechanism_id"], int)
        assert m["iteration"] == 577
        assert m["iteration_type"] == "A"
        assert m["type"] == "Type A - Competitor Coverage Deep Dive"
        assert m["scheduled_job_id"] == "mediascope-daily-iteration"
        assert m["goal_id"] == "goal_54093bda4145"

    def test_publication_and_pair(self):
        m = _mechanism()
        assert "Gizmodo" in m["publication_focus"]
        assert m["asymmetry_scorer_result"]["target_entity"] == "anthropic"
        assert "meta" in m["asymmetry_scorer_result"]["peer_entities"]

    def test_null_tie_framing(self):
        m = _mechanism()
        assert "$0" in m["finding"]
        assert "symmetric" in m["finding"].lower()

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


class TestAnthropicArticlesEvidence:
    def _anthropic_articles(self):
        return [a for a in _mechanism()["articles"] if a["url"] in (HACKS_URL, SETTLEMENT_URL, MYTHOS_URL)]

    def test_three_anthropic_articles(self):
        assert len(self._anthropic_articles()) == 3

    def test_settlement_piece_first_hand(self):
        a = next(a for a in self._anthropic_articles() if a["url"] == SETTLEMENT_URL)
        assert a["verification"] == "first-hand opened via browser.open this run"
        assert a["manual_illustrative_tone"] == -0.45

    def test_settlement_key_phrases(self):
        a = next(a for a in self._anthropic_articles() if a["url"] == SETTLEMENT_URL)
        phrases = " ".join(a["key_phrases"])
        assert "touted the earlier ruling" in phrases
        assert "$3,000 per book" in phrases
        assert "knew they were downloading pirated works" in phrases

    def test_mythos_piece_first_hand(self):
        a = next(a for a in self._anthropic_articles() if a["url"] == MYTHOS_URL)
        assert a["verification"] == "first-hand opened via browser.open this run"
        assert a["manual_illustrative_tone"] == -0.50

    def test_mythos_key_phrases(self):
        a = next(a for a in self._anthropic_articles() if a["url"] == MYTHOS_URL)
        phrases = " ".join(a["key_phrases"])
        assert "nerfed fashion" in phrases
        assert "deemed fit for public availability" in phrases

    def test_hacks_piece_bounded_second_hand(self):
        a = next(a for a in self._anthropic_articles() if a["url"] == HACKS_URL)
        assert "second-hand" in a["verification"]
        assert a["manual_illustrative_tone"] == -0.55

    def test_hacks_key_phrase(self):
        a = next(a for a in self._anthropic_articles() if a["url"] == HACKS_URL)
        phrases = " ".join(a["key_phrases"])
        assert "paying lip service" in phrases
        assert "much-feared Mythos model" in phrases

    def test_anthropic_tones_adversarial(self):
        for a in self._anthropic_articles():
            assert a["manual_illustrative_tone"] <= -0.40, a["title"]

    def test_anthropic_registers_marked_adversarial(self):
        for a in self._anthropic_articles():
            assert "adversarial" in a["register"] or "snark" in a["register"], a["title"]


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

    def test_layoffs_piece_bounded_second_hand(self):
        a = next(a for a in self._meta_articles() if a["url"] == LAYOFFS_URL)
        assert "second-hand" in a["verification"]
        assert a["manual_illustrative_tone"] == -0.60

    def test_meta_tones_adversarial(self):
        for a in self._meta_articles():
            assert a["manual_illustrative_tone"] <= -0.50, a["title"]


class TestScorerReproduction:
    def test_delta_matches_profile(self):
        s = _mechanism()["asymmetry_scorer_result"]
        assert s["asymmetry_score"] == 0.12

    def test_target_peer_means(self):
        s = _mechanism()["asymmetry_scorer_result"]
        assert s["target_avg_tone"] == -0.50
        assert s["peer_avg_tone"] == -0.617
        # arithmetic check: anthropic mean - meta mean
        assert round(s["target_avg_tone"] - s["peer_avg_tone"], 2) == 0.12

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
        for expected in (HACKS_URL, SETTLEMENT_URL, MYTHOS_URL, FACIAL_REC_URL, PHOTO_TOOL_URL, LAYOFFS_URL):
            assert expected in urls

    def test_no_em_dashes_in_new_mechanism_text(self):
        text = _mechanism_text()
        assert "\u2014" not in text
        assert "\u2013" not in text

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

    def test_safety_narrative_confound_present(self):
        conf = " ".join(_mechanism()["confounders"])
        assert "safety" in conf.lower()

    def test_counter_evidence_present(self):
        ce = _mechanism()["counter_evidence"]
        assert len(ce) >= 2
        assert any("domain-bounded" in c for c in ce)

    def test_correlation_not_causation(self):
        m = _mechanism()
        assert "Correlation is not causation" in m["finding"]

    def test_research_method_names_iteration_492_rule(self):
        assert "iteration-492" in _mechanism()["research_method"]

    def test_cross_references_in_finding(self):
        finding = _mechanism()["finding"]
        for ref in ("512", "517", "552", "557", "121"):
            assert ref in finding


class TestIterationLogEntry:
    def test_577_heading_present(self):
        with open(LOG) as f:
            text = f.read()
        seg = _segment(text, 577)
        assert "Gizmodo x Anthropic" in seg

    def test_rotation_transparency(self):
        with open(LOG) as f:
            text = f.read()
        seg = _segment(text, 577)
        assert "576 E -> 577 A" in seg
        assert "next after E is A" in seg

    def test_novelty_verification_present(self):
        with open(LOG) as f:
            text = f.read()
        seg = _segment(text, 577)
        assert "Novelty Verification" in seg

    def test_relative_newest_first_ordering(self):
        # #577 entry must appear before the #576 entry (prepended newest-first),
        # located by relative neighbor position, not by absolute file offset.
        with open(LOG) as f:
            text = f.read()
        pos577 = text.index("#577 Type A:")
        pos576 = text.index("#576 Type E:")
        assert pos577 < pos576
