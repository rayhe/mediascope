"""Type A #587 (2026-09-07 12:00 PDT): Gizmodo x Apple null-tie control -
fourth zero-tie control, product-lane reputation-carve boundary.

Gizmodo carries $0 documented financial ties to Apple and Meta (all
competitor_relationships blocks in this profile: none / $0), so the core thesis
predicts symmetric registers with no tie-driven softening. Observed: Gizmodo
applies an adversarial, snark-heavy register to BOTH Apple and Meta in the
controversy/news domain at closely matched illustrative intensity: delta
+0.1334 (apple mean -0.4833 vs meta mean -0.6167), p_value NOT_CALCULATED per
standing rule Aug 28 2026, n=3 vs n=3.

This is the FOURTH zero-tie control in the Gizmodo control set (after #512
Gizmodo x Google, #577 Gizmodo x Anthropic, #582 Gizmodo x OpenAI): the
symmetric-adversarial claim now holds across four competitor entities plus
Meta - the widest control set in the corpus. All three Apple pieces were
opened first-hand this run; two are new-to-corpus, the third is in-corpus as
a wearables example first scored as an Apple-side target item here. The three
Meta comparators are carried from #512/#577/#582.

The product-lane boundary: the glasses-minefield piece (Apr 2026, Raymond
Wong) applies the privacy-minefield frame to Apple's entry BUT with a partial
reputation carve Apple does not extend to Meta ("built on its reputation for
*not* doing that [collecting user data]" vs "the entire company is built
around collecting data"). The carve tracks Apple's genuine hardware-sales
business model and privacy marketing, not a financial tie (none exists). The
control is correctly bounded: symmetric adversarial register in
controversy/news, not identical treatment in every lane. The trade-secrets
piece (2000795382) was deliberately NOT reused as an Apple-side item: it is
in-corpus as an OpenAI-side litigation item and entity-tone attribution
follows the target entity, not the URL. No zero-coverage claims
(iteration-492 rule). No canonical URLs constructed: all six URLs carried
verbatim from search-result full-URL listings or prior units.

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
MECH_KEY = "mechanism_587_gizmodo_apple_null_tie_fourth_control_product_lane_boundary"

PRIVACY_AI_URL = "https://gizmodo.com/apple-says-its-new-google-infused-ai-is-all-about-privacy-2000768997"
VISION_PRO_URL = "https://gizmodo.com/apples-vision-pro-will-stick-ai-siri-right-in-your-face-2000768744"
GLASSES_MINEFIELD_URL = "https://gizmodo.com/apples-smart-glasses-are-stepping-into-a-privacy-minefield-2000746809"
FACIAL_REC_URL = "https://gizmodo.com/the-world-is-on-fire-and-meta-sees-an-opportunity-to-add-facial-recognition-to-smart-glasses-2000721970"
PHOTO_TOOL_URL = "https://gizmodo.com/the-public-got-so-mad-at-metas-new-ai-photo-tool-that-its-scrapped-already-2000784400"
LAYOFFS_URL = "https://gizmodo.com/meta-is-racing-to-move-faster-and-break-more-things-2000750107"

APPLE_URLS = (PRIVACY_AI_URL, VISION_PRO_URL, GLASSES_MINEFIELD_URL)
META_URLS = (FACIAL_REC_URL, PHOTO_TOOL_URL, LAYOFFS_URL)


def _mechanism():
    with open(GIZMODO_PROFILE) as f:
        doc = yaml.safe_load(f)
    return doc["competitor_relationships"]["apple"][MECH_KEY]


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


class TestMechanism587Structure:
    def test_yaml_parses(self):
        with open(GIZMODO_PROFILE) as f:
            yaml.safe_load(f)

    def test_mechanism_key_exists_under_apple(self):
        with open(GIZMODO_PROFILE) as f:
            doc = yaml.safe_load(f)
        assert MECH_KEY in doc["competitor_relationships"]["apple"]

    def test_mechanism_id_and_iteration(self):
        m = _mechanism()
        assert m["mechanism_id"] == 587
        assert m["iteration"] == 587
        assert m["iteration_type"] == "A"
        assert m["iteration_time"] == "2026-09-07 12:00 PDT"

    def test_required_metadata_fields(self):
        m = _mechanism()
        assert m["scheduled_job_id"] == "mediascope-daily-iteration"
        assert m["goal_id"] == "goal_54093bda4145"
        assert "Gizmodo" in m["publication_focus"]
        assert m["type"] == "Type A - Competitor Coverage Deep Dive"

    def test_six_articles(self):
        assert len(_mechanism()["articles"]) == 6

    def test_apple_block_financial_tie_unchanged(self):
        with open(GIZMODO_PROFILE) as f:
            doc = yaml.safe_load(f)
        apple = doc["competitor_relationships"]["apple"]
        assert apple["financial_tie"] == "none"
        assert apple["estimated_value"] == "$0"


class TestAppleArticlesEvidence:
    def _apple_articles(self):
        return [a for a in _mechanism()["articles"] if a["url"] in APPLE_URLS]

    def test_three_apple_articles(self):
        assert len(self._apple_articles()) == 3

    def test_privacy_ai_piece_first_hand_new_to_corpus(self):
        a = next(a for a in self._apple_articles() if a["url"] == PRIVACY_AI_URL)
        assert a["verification"].startswith("first-hand this run")
        assert "NEW-TO-CORPUS" in a["verification"]
        assert a["manual_illustrative_tone"] == -0.50
        assert a["register"] == "skeptical_distancing"

    def test_privacy_ai_key_phrases(self):
        a = next(a for a in self._apple_articles() if a["url"] == PRIVACY_AI_URL)
        phrases = " ".join(a["key_phrases"])
        assert "technobabble for being able to access the web" in phrases
        assert "We are not like other AI companies" in phrases

    def test_vision_pro_piece_first_hand_new_to_corpus(self):
        a = next(a for a in self._apple_articles() if a["url"] == VISION_PRO_URL)
        assert a["verification"].startswith("first-hand this run")
        assert "NEW-TO-CORPUS" in a["verification"]
        assert a["manual_illustrative_tone"] == -0.55
        assert a["register"] == "dismissive_snark"

    def test_vision_pro_key_phrases(self):
        a = next(a for a in self._apple_articles() if a["url"] == VISION_PRO_URL)
        phrases = " ".join(a["key_phrases"])
        assert "small ounce of love" in phrases
        assert "inane queries" in phrases
        assert "Hello, Orb" in phrases

    def test_glasses_minefield_reputation_carve(self):
        a = next(a for a in self._apple_articles() if a["url"] == GLASSES_MINEFIELD_URL)
        assert a["verification"].startswith("first-hand this run")
        assert "first scored as an Apple-side target item in this unit" in a["verification"]
        assert a["manual_illustrative_tone"] == -0.40
        assert a["register"] == "adversarial_with_reputation_carve"

    def test_glasses_minefield_carve_phrases(self):
        a = next(a for a in self._apple_articles() if a["url"] == GLASSES_MINEFIELD_URL)
        phrases = " ".join(a["key_phrases"])
        assert "doubly messy" in phrases
        assert "reputation for *not* doing that" in phrases
        assert "entire company is built around collecting data" in phrases

    def test_apple_tones_adversarial_band(self):
        for a in self._apple_articles():
            assert -0.70 <= a["manual_illustrative_tone"] <= -0.40, a["title"]

    def test_apple_registers_adversarial(self):
        for a in self._apple_articles():
            assert "adversarial" in a["register"] or "snark" in a["register"] or "distancing" in a["register"], a["title"]


class TestMetaComparatorEvidence:
    def _meta_articles(self):
        return [a for a in _mechanism()["articles"] if a["url"] in META_URLS]

    def test_three_meta_articles(self):
        assert len(self._meta_articles()) == 3

    def test_facial_rec_carryover_from_512(self):
        a = next(a for a in self._meta_articles() if a["url"] == FACIAL_REC_URL)
        assert "#512" in a["verification"]
        assert a["manual_illustrative_tone"] == -0.70

    def test_photo_tool_carryover_from_512(self):
        a = next(a for a in self._meta_articles() if a["url"] == PHOTO_TOOL_URL)
        assert "#512" in a["verification"]
        assert a["manual_illustrative_tone"] == -0.55

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
        assert s["asymmetry_score"] == 0.1334

    def test_target_peer_means(self):
        s = _mechanism()["asymmetry_scorer_result"]
        assert s["target_entity"] == "apple"
        assert s["peer_entities"] == ["meta"]
        assert s["target_avg_tone"] == -0.4833
        assert s["peer_avg_tone"] == -0.6167
        # arithmetic check: apple mean - meta mean
        assert round(s["target_avg_tone"] - s["peer_avg_tone"], 4) == 0.1334

    def test_means_reproduce_from_article_tones(self):
        articles = _mechanism()["articles"]
        apple_tones = [a["manual_illustrative_tone"] for a in articles if a["url"] in APPLE_URLS]
        meta_tones = [a["manual_illustrative_tone"] for a in articles if a["url"] in META_URLS]
        assert round(sum(apple_tones) / 3, 4) == -0.4833
        assert round(sum(meta_tones) / 3, 4) == -0.6167

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
        assert "+0.1334" in m["statistical_discipline"]


class TestSourceHygiene:
    def test_all_source_urls_https(self):
        m = _mechanism()
        for u in m["source_urls"]:
            assert u.startswith("https://"), u

    def test_six_source_urls_unique(self):
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
        for expected in APPLE_URLS + META_URLS:
            assert expected in urls

    def test_trade_secrets_piece_not_double_counted(self):
        urls = {a["url"] for a in _mechanism()["articles"]}
        assert "https://gizmodo.com/openai-says-apples-real-problem-is-being-bad-at-ai-not-stolen-secrets-2000795382" not in urls

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
        assert "genre" in conf.lower()

    def test_product_lane_boundary_confound_present(self):
        conf = " ".join(_mechanism()["confounders"])
        assert "product-lane" in conf.lower()

    def test_business_model_confound_present(self):
        conf = " ".join(_mechanism()["confounders"])
        assert "business-model" in conf.lower()

    def test_counter_evidence_present(self):
        ce = _mechanism()["counter_evidence"]
        assert len(ce) >= 2
        assert any("illustrative-band" in c for c in ce)

    def test_correlation_not_causation(self):
        m = _mechanism()
        assert "Correlation is not causation" in m["finding"]

    def test_research_method_names_iteration_492_rule(self):
        assert "iteration-492" in _mechanism()["research_method"]

    def test_cross_references_in_finding(self):
        finding = _mechanism()["finding"]
        for ref in ("512", "577", "582", "121", "547"):
            assert ref in finding

    def test_distinct_from_names_fourth_control(self):
        df = " ".join(_mechanism()["distinct_from"])
        assert "FOURTH zero-tie control" in df


class TestIterationLogEntry:
    def test_587_heading_present(self):
        with open(LOG) as f:
            text = f.read()
        seg = _segment(text, 587)
        assert "Gizmodo x Apple" in seg

    def test_rotation_transparency(self):
        with open(LOG) as f:
            text = f.read()
        seg = _segment(text, 587)
        assert "586 E -> 587 A" in seg
        assert "next after E is A" in seg

    def test_novelty_verification_present(self):
        with open(LOG) as f:
            text = f.read()
        seg = _segment(text, 587)
        assert "Novelty Verification" in seg

    def test_relative_newest_first_ordering(self):
        # #587 entry must appear before the #586 entry (prepended newest-first),
        # located by relative neighbor position, not by absolute file offset.
        with open(LOG) as f:
            text = f.read()
        pos587 = text.index("#587 Type A:")
        pos586 = text.index("#586 Type E:")
        assert pos587 < pos586
