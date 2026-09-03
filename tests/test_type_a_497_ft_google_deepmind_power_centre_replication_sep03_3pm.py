"""Type A #497 (2026-09-03 15:00 PDT): FT x Google DeepMind leadership-transition register.

Same-treatment cross-publication replication of mechanism #487 (Guardian x Google,
same Aug 5 2026 Hassabis event): the FT's insider power-anatomy register
('AI power centre has moved to Sergey Brin's desk', a dozen FT sources) vs its
adversarial legal register for Meta's $16.68bn teen-safety settlement
('blockbuster legal battle') within a 3-week window. First Type A empirical tone
test of the #437 dual-AI-payer portfolio prediction (FT takes AI money from both
OpenAI and Google, $0 from Meta).

Statistical discipline: MANUAL ILLUSTRATIVE tones at headline/lede-excerpt level,
n=1 per side. Live scorer reproduced this run: delta -0.55, p_value 1.0,
cohens_d 0.0, is_significant False. No significance claimed or claimable.
correlation_not_causation. ft.com paywalled: only positively verified
headline/lede excerpts are asserted (mirror-first rule, #492 precedent); the
Google canonical URL never surfaced and is NOT invented.

Durable conventions (from #495): line-anchored (^, re.MULTILINE) heading search in
iteration-log.md; relative newest-first ordering between neighbors, never
absolute-top or fixed head slices.
"""

import os
import re
from datetime import datetime

import pytest
import yaml

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FT_PROFILE = os.path.join(REPO, "profiles", "financial-times.yaml")
LOG = os.path.join(REPO, "iteration-log.md")
MECH_KEY = "mechanism_497_ft_google_deepmind_power_centre_vs_meta_blockbuster_legal_register"
FT_META_URL = "https://www.ft.com/content/21dcbd96-ee57-445c-a9ba-0938c49b91c0"


def _mechanism():
    with open(FT_PROFILE) as f:
        doc = yaml.safe_load(f)
    return doc["competitor_relationships"]["google"][MECH_KEY]


def _segment(log_text, num):
    """Return the text of iteration #num's log entry (heading to next heading)."""
    headings = [(m.start(), m.group(1)) for m in re.finditer(r"^#(\d+) Type [A-E]:", log_text, re.M)]
    starts = [pos for pos, n in headings if n == str(num)]
    assert starts, f"#{num} heading not found"
    start = starts[0]
    later = [pos for pos, _ in headings if pos > start]
    end = min(later) if later else len(log_text)
    return log_text[start:end]


class TestMechanism497Structure:
    def test_yaml_parses(self):
        with open(FT_PROFILE) as f:
            yaml.safe_load(f)

    def test_mechanism_key_exists(self):
        with open(FT_PROFILE) as f:
            doc = yaml.safe_load(f)
        assert MECH_KEY in doc["competitor_relationships"]["google"]

    def test_identity_fields(self):
        m = _mechanism()
        assert m["mechanism_id"] == 497
        assert m["iteration"] == 497
        assert m["iteration_type"] == "A"
        assert m["iteration_time"] == "2026-09-03 15:00 PDT"
        assert m["scheduled_job_id"] == "mediascope-daily-iteration"
        assert m["goal_id"] == "goal_54093bda4145"

    def test_publication_and_pair(self):
        m = _mechanism()
        assert m["publication_focus"] == "Financial Times"
        assert m["entity_pair"] == "Google vs Meta"
        assert "replication of #487" in m["type"]

    def test_status_is_baseline_not_confirmation(self):
        m = _mechanism()
        assert "BASELINE" in m["status"]
        assert "does not confirm" in m["status"]


class TestGoogleArticleEvidence:
    def test_single_scored_google_article(self):
        m = _mechanism()
        assert len(m["google_articles"]) == 1

    def test_headline_and_date(self):
        art = _mechanism()["google_articles"][0]
        assert "power centre has moved to Sergey Brin" in art["title"]
        assert art["date"] == "2026-08-08"

    def test_no_invented_canonical_url(self):
        art = _mechanism()["google_articles"][0]
        assert art["url"] == "NO_CANONICAL_URL - ft.com canonical URL never surfaced in search; not invented per URL-verbatim rule"
        assert "ft.com" not in art["url"].replace("ft.com canonical", "")

    def test_byline_not_guessed(self):
        art = _mechanism()["google_articles"][0]
        assert art["journalist"].startswith("UNVERIFIED")

    def test_verified_lede_excerpt(self):
        art = _mechanism()["google_articles"][0]
        assert "most important desk" in art["lede"]
        assert "That arrangement ended this week" in art["lede"]

    def test_dozen_source_attribution_recorded(self):
        art = _mechanism()["google_articles"][0]
        assert "dozen people familiar with the company" in art["sourcing_markers"]

    def test_body_negatives_marked_unverified(self):
        art = _mechanism()["google_articles"][0]
        assert art["negative_facts_status"].startswith("UNVERIFIED")

    def test_illustrative_tone_labeled(self):
        art = _mechanism()["google_articles"][0]
        assert art["illustrative_tone"] == -0.10
        assert "excerpt only" in art["illustrative_tone_basis"]


class TestMetaArticleEvidence:
    def test_single_scored_meta_article(self):
        m = _mechanism()
        assert len(m["meta_articles"]) == 1

    def test_canonical_url_verbatim(self):
        art = _mechanism()["meta_articles"][0]
        assert art["url"] == FT_META_URL

    def test_date_and_adversarial_lede(self):
        art = _mechanism()["meta_articles"][0]
        assert art["date"] == "2026-08-26"
        assert "blockbuster legal battle" in art["lede"]
        assert "$16.68bn" in art["lede"]

    def test_headline_marked_unverified(self):
        art = _mechanism()["meta_articles"][0]
        assert "unverified" in art["title"].lower()

    def test_illustrative_tone_labeled(self):
        art = _mechanism()["meta_articles"][0]
        assert art["illustrative_tone"] == -0.65


class TestScorerReproduction:
    def _run(self):
        from mediascope.score.asymmetry import calculate_asymmetry
        return calculate_asymmetry(
            target_scores=[-0.65],
            peer_scores=[-0.10],
            target_entity="Meta",
            peer_entities=["Google"],
            publication_slug="financial-times",
            period_start=datetime(2026, 8, 5),
            period_end=datetime(2026, 8, 26),
        )

    def test_delta_matches_profile(self):
        r = self._run()
        assert r.asymmetry_score == pytest.approx(_mechanism()["scorer_manual_illustrative"]["asymmetry_delta"])

    def test_not_significant(self):
        r = self._run()
        assert r.is_significant is False
        assert _mechanism()["scorer_manual_illustrative"]["is_significant"] is False

    def test_p_value_degenerate(self):
        r = self._run()
        assert r.p_value == 1.0
        assert r.cohens_d == 0.0

    def test_manual_illustrative_note_present(self):
        note = _mechanism()["scorer_manual_illustrative"]["note"]
        assert "MANUAL ILLUSTRATIVE" in note
        assert "n=1 per side" in note


class TestSourceHygiene:
    def test_all_source_urls_https(self):
        for u in _mechanism()["source_urls"]:
            assert u.startswith("https://"), u

    def test_no_invented_ft_google_url_in_sources(self):
        urls = _mechanism()["source_urls"]
        assert not any("ft.com" in u and "deepmind" in u.lower() for u in urls)
        assert FT_META_URL in urls

    def test_no_em_dashes_in_new_mechanism_text(self):
        raw = open(FT_PROFILE).read()
        seg = raw[raw.index(MECH_KEY):raw.index(MECH_KEY) + 12000]
        assert "\u2014" not in seg

    def test_ascii_only_in_new_mechanism_text(self):
        raw = open(FT_PROFILE).read()
        seg = raw[raw.index(MECH_KEY):raw.index(MECH_KEY) + 12000]
        assert all(ord(c) < 128 for c in seg)


class TestConfoundersAndDiscipline:
    def test_confounders_ranked_three_tiers(self):
        rc = _mechanism()["ranked_confounders"]
        assert set(rc.keys()) == {"strong", "moderate", "weak"}

    def test_event_structure_confounder_present(self):
        strong = " ".join(_mechanism()["ranked_confounders"]["strong"])
        assert "Event-structure" in strong

    def test_counter_evidence_nonempty(self):
        ce = _mechanism()["counter_evidence"]
        assert len(ce) >= 3
        assert any("Brin" in c or "power" in c for c in ce)

    def test_correlation_not_causation(self):
        m = _mechanism()
        assert "correlation_not_causation" in m["statistical_discipline"]
        assert "is_significant false" in m["statistical_discipline"]


class TestCrossReferences:
    def test_references_487_replication(self):
        text = " ".join(_mechanism()["cross_references"])
        assert "#487" in text

    def test_references_437_dual_payer(self):
        text = " ".join(_mechanism()["cross_references"])
        assert "#437" in text

    def test_distinct_from_aug5_glasses_test(self):
        m = _mechanism()
        assert "test_ft_google_coverage_asymmetry.py" in m["distinct_from_prior"]
        assert "glasses" in m["distinct_from_prior"]


class TestIterationLog:
    def test_497_heading_exists_line_anchored(self):
        log = open(LOG).read()
        assert re.search(r"^#497 Type A:", log, re.M)

    def test_497_segment_names_power_centre(self):
        seg = _segment(open(LOG).read(), 497)
        assert "power centre" in seg

    def test_relative_newest_first_497_before_496(self):
        log = open(LOG).read()
        headings = [(m.start(), m.group(1)) for m in re.finditer(r"^#(\d+) Type [A-E]:", log, re.M)]
        pos = {n: p for p, n in headings}
        assert pos["497"] < pos["496"]

    def test_rotation_line_present_in_segment(self):
        seg = _segment(open(LOG).read(), 497)
        assert "496 E -> 497 A" in seg


class TestNovelty:
    def test_no_prior_type_a_ft_google_leadership_file(self):
        names = os.listdir(os.path.join(REPO, "tests"))
        hits = [n for n in names if n.startswith("test_type_a") and "ft" in n and "google" in n
                and any(k in n for k in ("leadership", "deepmind", "power_centre", "brin", "hassabis"))]
        assert hits == [os.path.basename(__file__)]

    def test_aug5_glasses_file_still_exists_and_distinct(self):
        path = os.path.join(REPO, "tests", "test_ft_google_coverage_asymmetry.py")
        assert os.path.exists(path)
