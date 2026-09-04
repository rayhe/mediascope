"""Type A #512 (2026-09-04 06:00 PDT): Gizmodo x Google null-tie control -
symmetric adversarial register toward deal-absent entities.

Gizmodo carries $0 documented financial ties to Google, Meta, OpenAI, and
Anthropic (all competitor_relationships blocks: none / $0), so the core
thesis predicts symmetric registers with no tie-driven softening. Observed:
Gizmodo applies an adversarial, sarcastic register to BOTH Google and Meta in
the controversy/privacy domain, with a negligible +0.10 tone lean toward
Google that is not significant (p_value 0.396, n=2 vs n=2).

This is the control case the thesis needs: it bounds the claim so that
softening at deal publications (FT-OpenAI, Verge-OpenAI product domain #425)
cannot be dismissed as generic big-tech house style - Gizmodo's house style
is equal-opportunity adversarial and it shows here, symmetric. The claim is
explicitly domain-bounded: the profile's own tone-history block records a
POSITIVE Gizmodo register toward Google XR hardware (Project Aura, May 2026),
so the symmetric-adversarial claim covers controversy/privacy coverage only.

Statistical discipline: MANUAL ILLUSTRATIVE tones at article level, n=2 vs n=2.
Live scorer reproduced this run: delta 0.10, p_value 0.396, cohens_d 1.265,
is_significant False. No significance claimed or claimable.
correlation_not_causation. Three of four articles opened first-hand this run;
the Meta photo-tool piece is excerpt-bounded second-hand (marked in-mechanism).
No zero-coverage claims (iteration-492 rule). No canonical URLs constructed:
all four URLs carried verbatim from search-result full-URL listings.

Durable conventions (from #495): line-anchored (^, re.MULTILINE) heading search
in iteration-log.md; relative newest-first ordering between neighbors, never
absolute-top or fixed head slices.
"""

import os
import re
from datetime import datetime

import pytest
import yaml

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GIZMODO_PROFILE = os.path.join(REPO, "profiles", "gizmodo.yaml")
LOG = os.path.join(REPO, "iteration-log.md")
MECH_KEY = "mechanism_512_gizmodo_google_null_tie_symmetric_adversarial"

APPEAL_URL = "https://gizmodo.com/not-so-fast-google-that-lenient-monopoly-ruling-from-last-year-is-being-appealed-2000717092"
SETTLEMENTS_URL = "https://gizmodo.com/its-a-big-week-for-google-privacy-violation-settlements-2000715678"
FACIAL_REC_URL = "https://gizmodo.com/the-world-is-on-fire-and-meta-sees-an-opportunity-to-add-facial-recognition-to-smart-glasses-2000721970"
PHOTO_TOOL_URL = "https://gizmodo.com/the-public-got-so-mad-at-metas-new-ai-photo-tool-that-its-scrapped-already-2000784400"


def _mechanism():
    with open(GIZMODO_PROFILE) as f:
        doc = yaml.safe_load(f)
    return doc["competitor_relationships"]["google"][MECH_KEY]


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


class TestMechanism512Structure:
    def test_yaml_parses(self):
        with open(GIZMODO_PROFILE) as f:
            yaml.safe_load(f)

    def test_mechanism_key_exists_under_google(self):
        with open(GIZMODO_PROFILE) as f:
            doc = yaml.safe_load(f)
        assert MECH_KEY in doc["competitor_relationships"]["google"]

    def test_identity_fields(self):
        m = _mechanism()
        assert m["mechanism_id"] == 512
        assert m["iteration"] == 512
        assert m["iteration_type"] == "A"
        assert m["iteration_time"] == "2026-09-04 06:00 PDT"
        assert m["scheduled_job_id"] == "mediascope-daily-iteration"
        assert m["goal_id"] == "goal_54093bda4145"

    def test_publication_and_pair(self):
        m = _mechanism()
        assert "Gizmodo" in m["publication_focus"]
        assert "Keleops" in m["publication_focus"]
        assert m["type"].startswith("Type A")

    def test_null_tie_framing(self):
        finding = _mechanism()["finding"]
        assert "null-tie control" in finding.lower() or "null-tie" in finding.lower()
        assert "symmetric" in finding.lower()

    def test_four_articles(self):
        assert len(_mechanism()["articles"]) == 4

    def test_distinct_from_block_present(self):
        assert len(_mechanism()["distinct_from"]) >= 3

    def test_mechanism_is_nested_dict(self):
        assert isinstance(_mechanism(), dict)
        assert _mechanism()["mechanism_id"] == 512


class TestGoogleArticlesEvidence:
    def _google_articles(self):
        arts = _mechanism()["articles"]
        return [a for a in arts if "Google" in a["title"]]

    def test_two_google_articles(self):
        assert len(self._google_articles()) == 2

    def test_appeal_piece_first_hand(self):
        a = next(a for a in self._google_articles() if "Appealed" in a["title"])
        assert a["url"] == APPEAL_URL
        assert a["verification"] == "first-hand opened via browser.open this run"
        assert a["manual_illustrative_tone"] == -0.55

    def test_appeal_key_phrases(self):
        a = next(a for a in self._google_articles() if "Appealed" in a["title"])
        joined = " ".join(a["key_phrases"])
        assert "god-kings" in joined
        assert "payola" in joined
        assert "best case scenario" in joined

    def test_settlements_piece_first_hand(self):
        a = next(a for a in self._google_articles() if "Settlements" in a["title"])
        assert a["url"] == SETTLEMENTS_URL
        assert a["verification"] == "first-hand opened via browser.open this run"
        assert a["manual_illustrative_tone"] == -0.50

    def test_settlements_figures(self):
        a = next(a for a in self._google_articles() if "Settlements" in a["title"])
        joined = " ".join(a["key_phrases"])
        assert "$135M" in joined
        assert "$68M" in joined
        assert "admit no wrongdoing" in joined

    def test_google_tones_adversarial(self):
        for a in self._google_articles():
            assert a["manual_illustrative_tone"] <= -0.40

    def test_google_registers_marked_adversarial(self):
        for a in self._google_articles():
            assert "adversarial" in a["register"]


class TestMetaComparatorEvidence:
    def _meta_articles(self):
        arts = _mechanism()["articles"]
        return [a for a in arts if "Meta" in a["title"]]

    def test_two_meta_articles(self):
        assert len(self._meta_articles()) == 2

    def test_facial_rec_piece_first_hand(self):
        a = next(a for a in self._meta_articles() if "Facial Recognition" in a["title"])
        assert a["url"] == FACIAL_REC_URL
        assert a["verification"] == "first-hand opened via browser.open this run"
        assert a["manual_illustrative_tone"] == -0.70

    def test_facial_rec_key_phrases(self):
        a = next(a for a in self._meta_articles() if "Facial Recognition" in a["title"])
        joined = " ".join(a["key_phrases"])
        assert "not hyperbole" in joined
        assert "one-man band of surveillance" in joined

    def test_photo_tool_piece_bounded_second_hand(self):
        a = next(a for a in self._meta_articles() if "Photo Tool" in a["title"])
        assert a["url"] == PHOTO_TOOL_URL
        assert "second-hand" in a["verification"]
        assert a["manual_illustrative_tone"] == -0.55

    def test_photo_tool_key_phrase(self):
        a = next(a for a in self._meta_articles() if "Photo Tool" in a["title"])
        joined = " ".join(a["key_phrases"])
        assert "world record" in joined
        assert "utter miscalculation" in joined

    def test_meta_tones_adversarial(self):
        for a in self._meta_articles():
            assert a["manual_illustrative_tone"] <= -0.40


class TestScorerReproduction:
    def _run(self):
        from mediascope.score.asymmetry import calculate_asymmetry
        return calculate_asymmetry(
            target_scores=[-0.55, -0.50],
            peer_scores=[-0.55, -0.70],
            target_entity="google",
            peer_entities=["meta"],
            publication_slug="gizmodo",
            period_start=datetime(2026, 2, 1),
            period_end=datetime(2026, 9, 4),
        )

    def test_delta_matches_profile(self):
        r = self._run()
        assert r.asymmetry_score == pytest.approx(_mechanism()["asymmetry_scorer_result"]["asymmetry_score"])

    def test_target_peer_means(self):
        r = self._run()
        res = _mechanism()["asymmetry_scorer_result"]
        assert r.target_avg_tone == pytest.approx(res["target_avg_tone"])
        assert r.peer_avg_tone == pytest.approx(res["peer_avg_tone"])

    def test_not_significant(self):
        r = self._run()
        assert r.is_significant is False
        assert _mechanism()["asymmetry_scorer_result"]["is_significant"] is False

    def test_p_value_matches(self):
        r = self._run()
        assert r.p_value == pytest.approx(_mechanism()["asymmetry_scorer_result"]["p_value"], abs=0.01)

    def test_cohens_d_matches(self):
        r = self._run()
        assert r.cohens_d == pytest.approx(_mechanism()["asymmetry_scorer_result"]["cohens_d"], abs=0.01)

    def test_manual_illustrative_note_present(self):
        method = _mechanism()["asymmetry_scorer_result"]["methodology"]
        assert "MANUAL ILLUSTRATIVE" in method
        assert "n=2 vs n=2" in method

    def test_ci_recorded(self):
        ci = _mechanism()["asymmetry_scorer_result"]["confidence_interval"]
        assert len(ci) == 2
        assert ci[0] <= ci[1]


class TestSourceHygiene:
    def test_all_source_urls_https(self):
        for u in _mechanism()["source_urls"]:
            assert u.startswith("https://"), u

    def test_four_source_urls(self):
        srcs = _mechanism()["source_urls"]
        assert len(srcs) == 4
        assert APPEAL_URL in srcs
        assert SETTLEMENTS_URL in srcs
        assert FACIAL_REC_URL in srcs
        assert PHOTO_TOOL_URL in srcs

    def test_no_constructed_urls(self):
        assert "no canonical urls constructed" in _mechanism()["research_method"].lower() or \
               "No canonical URLs constructed" in _mechanism()["research_method"]

    def test_no_em_dashes_in_new_mechanism_text(self):
        assert "\u2014" not in _mechanism_text()
        assert "\u2013" not in _mechanism_text()

    def test_ascii_only_in_new_mechanism_text(self):
        text = _mechanism_text()
        assert all(ord(c) < 128 for c in text)


class TestConfoundersAndDiscipline:
    def test_confounders_ranked_three_tiers(self):
        confs = _mechanism()["confounders"]
        tiers = {c.split(":")[0] for c in confs}
        assert tiers == {"STRONG", "MODERATE", "WEAK"}

    def test_genre_confounder_present(self):
        confs = _mechanism()["confounders"]
        assert any("genre confound" in c.lower() for c in confs)

    def test_product_aura_counter_domain_noted(self):
        joined = " ".join(_mechanism()["confounders"] + _mechanism()["counter_evidence"])
        assert "Project Aura" in joined

    def test_counter_evidence_nonempty(self):
        ce = _mechanism()["counter_evidence"]
        assert len(ce) >= 2
        assert any("Project Aura" in c for c in ce)

    def test_correlation_not_causation(self):
        m = _mechanism()
        assert "not causation" in m["finding"]
        assert "not causation" in m["asymmetry_scorer_result"]["methodology"] or \
               "correlation_not_causation" in m["asymmetry_scorer_result"]["methodology"]

    def test_no_zero_coverage_claims(self):
        assert "no zero-coverage claims" in _mechanism()["research_method"]

    def test_cohens_d_small_sample_caveat(self):
        assert "small-sample artifact" in _mechanism()["statistical_discipline"]


class TestNoveltyVsPrior:
    def test_no_prior_gizmodo_google_type_a(self):
        # repo-wide: no other Type A mechanism works Gizmodo x Google
        with open(GIZMODO_PROFILE) as f:
            doc = yaml.safe_load(f)
        google = doc["competitor_relationships"]["google"]
        mech_keys = [k for k in google if k.startswith("mechanism_")]
        assert mech_keys == [MECH_KEY]

    def test_tone_history_block_acknowledged(self):
        joined = " ".join(_mechanism()["confounders"] + _mechanism()["counter_evidence"])
        assert "tone-history block" in joined

    def test_meta_only_repo_analyses_referenced(self):
        assert "gizmodo_meta_led_tamper_disable_2026_07_08" in _mechanism()["research_method"]
        assert "gizmodo_smart_glasses_hit_privacy_pile_up_2026_07_30" in _mechanism()["research_method"]

    def test_falsification_family_context(self):
        assert "#502" in _mechanism()["distinct_from"][3]
        assert "CONTROL" in _mechanism()["distinct_from"][3]

    def test_zero_article_overlap_asserted(self):
        assert "zero Google article overlap" in _mechanism()["distinct_from"][1]


class TestIterationLog:
    def test_512_entry_present(self):
        with open(LOG) as f:
            log_text = f.read()
        seg = _segment(log_text, 512)
        assert "Type A" in seg

    def test_512_entry_type_a_gizmodo_google(self):
        with open(LOG) as f:
            log_text = f.read()
        seg = _segment(log_text, 512)
        assert "Gizmodo" in seg
        assert "Google" in seg

    def test_512_scorer_numbers_in_log(self):
        with open(LOG) as f:
            log_text = f.read()
        seg = _segment(log_text, 512)
        assert "0.10" in seg
        assert "0.396" in seg

    def test_rotation_transparency_511_to_512(self):
        with open(LOG) as f:
            log_text = f.read()
        seg = _segment(log_text, 512)
        assert "511 E -> 512 A" in seg

    def test_512_newer_than_511(self):
        with open(LOG) as f:
            log_text = f.read()
        headings = [(m.start(), m.group(1)) for m in re.finditer(r"^#(\d+) Type [A-E]:", log_text, re.M)]
        pos512 = next(p for p, n in headings if n == "512")
        pos511 = next(p for p, n in headings if n == "511")
        assert pos512 < pos511, "newest-first ordering violated"
