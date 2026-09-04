"""Type A #502 (2026-09-03 20:00 PDT): WIRED x Microsoft PCM adversarial boundary condition.

First WIRED x Microsoft Type A (zero prior wired+Microsoft test files, glob verified).
Tests the Cond Nast Microsoft Publisher Content Marketplace (Feb 2026) softer-coverage
prediction as a boundary condition: WIRED published an adversarial Microsoft emissions
investigation AFTER the deal, so the strong softening claim fails at the coverage-selection
level; a weaker within-article register-cushioning claim is documented against the Meta
comparator with heavy confounders.

Statistical discipline: MANUAL ILLUSTRATIVE tones at article level, n=2 vs n=1.
Live scorer reproduced this run: delta 0.90, p_value 1.0, cohens_d ~1.591,
is_significant False. No significance claimed or claimable. correlation_not_causation.
wired.com policy-blocked: the emissions piece was opened first-hand via its archive.org
mirror; the Scout and Meta pieces rest on mirror/search excerpts marked second-hand
in-mechanism (mirror-first rule, #492 precedent). No zero-coverage claims.

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
WIRED_PROFILE = os.path.join(REPO, "profiles", "wired.yaml")
LOG = os.path.join(REPO, "iteration-log.md")
MECH_KEY = "mechanism_502_wired_microsoft_pcm_adversarial_boundary_condition"

MS_EMISSIONS_URL = "https://www.wired.com/story/microsoft-25-percent-jump-in-carbon-emissions/"
MS_EMISSIONS_MIRROR = "https://web.archive.org/web/20260710232642/https://www.wired.com/story/microsoft-25-percent-jump-in-carbon-emissions/"
MS_SCOUT_URL = "https://www.wired.com/story/meet-microsoft-scout-your-ai-coworker-that-never-logs-off/"
META_CSAM_URL = "https://www.wired.com/story/meta-ran-ads-that-contained-ai-generated-child-sexual-abuse-imagery/"


def _mechanism():
    with open(WIRED_PROFILE) as f:
        doc = yaml.safe_load(f)
    return doc["competitor_relationships"]["microsoft"][MECH_KEY]


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


class TestMechanism502Structure:
    def test_yaml_parses(self):
        with open(WIRED_PROFILE) as f:
            yaml.safe_load(f)

    def test_mechanism_key_exists(self):
        assert MECH_KEY in yaml.safe_load(open(WIRED_PROFILE))["competitor_relationships"]["microsoft"]

    def test_identity_fields(self):
        m = _mechanism()
        assert m["mechanism_id"] == 502
        assert m["iteration"] == 502
        assert m["iteration_type"] == "A"
        assert m["iteration_time"] == "2026-09-03 20:00 PDT"
        assert m["scheduled_job_id"] == "mediascope-daily-iteration"
        assert m["goal_id"] == "goal_54093bda4145"

    def test_publication_and_pair(self):
        m = _mechanism()
        assert m["publication_focus"] == "WIRED (Conde Nast)"
        assert m["type"].startswith("Type A")

    def test_boundary_condition_framing(self):
        finding = _mechanism()["finding"]
        assert "boundary" in finding.lower()
        assert "does not buy immunity" in finding


class TestMicrosoftArticlesEvidence:
    def test_three_articles_listed(self):
        arts = _mechanism()["articles"]
        assert len(arts) == 3

    def test_emissions_canonical_url_verbatim(self):
        arts = _mechanism()["articles"]
        assert arts[0]["url"] == MS_EMISSIONS_URL

    def test_emissions_mirror_opened_first_hand(self):
        arts = _mechanism()["articles"]
        assert arts[0]["mirror_opened_first_hand"] == MS_EMISSIONS_MIRROR
        assert "Massive" in arts[0]["title"]
        assert arts[0]["manual_illustrative_tone"] == -0.35

    def test_emissions_adversarial_facts_recorded(self):
        finding = _mechanism()["finding"]
        assert "11.5M tons" in finding
        assert "Chevron" in finding

    def test_scout_url_verbatim_and_second_hand(self):
        arts = _mechanism()["articles"]
        assert arts[1]["url"] == MS_SCOUT_URL
        assert arts[1]["author"] == "Reece Rogers"
        assert any("second_hand" in k for k in arts[1])
        assert arts[1]["manual_illustrative_tone"] == 0.45

    def test_scout_privacy_vocabulary_claim_bounded(self):
        finding = _mechanism()["finding"]
        assert "excerpt-bounded" in finding

    def test_cushioning_devices_enumerated(self):
        finding = _mechanism()["finding"]
        for device in ("industry-diffusion", "executive voice share", "highly commendable",
                       "carbon negative by 2030", "zero watchdog"):
            assert device in finding, device


class TestMetaComparatorEvidence:
    def test_meta_url_verbatim(self):
        arts = _mechanism()["articles"]
        assert arts[2]["url"] == META_CSAM_URL

    def test_meta_byline_and_date(self):
        arts = _mechanism()["articles"]
        assert arts[2]["author"] == "Matt Burgess"
        assert arts[2]["date"] == "2026-08-06"

    def test_meta_excerpts_marked_second_hand(self):
        arts = _mechanism()["articles"]
        assert any("second_hand" in k for k in arts[2])
        assert any("engadget" in u for u in arts[2]["mirror_excerpts_second_hand"])

    def test_watchdog_frame_recorded(self):
        finding = _mechanism()["finding"]
        assert "reviewed, approved, and allowed to run by Meta" in finding
        assert "Tech Transparency Project" in finding

    def test_meta_tone_labeled(self):
        arts = _mechanism()["articles"]
        assert arts[2]["manual_illustrative_tone"] == -0.85


class TestScorerReproduction:
    def _run(self):
        from mediascope.score.asymmetry import calculate_asymmetry
        return calculate_asymmetry(
            target_scores=[-0.35, 0.45],
            peer_scores=[-0.85],
            target_entity="microsoft",
            peer_entities=["meta"],
            publication_slug="wired",
            period_start=datetime(2026, 6, 1),
            period_end=datetime(2026, 8, 31),
        )

    def test_delta_matches_profile(self):
        r = self._run()
        assert r.asymmetry_score == pytest.approx(_mechanism()["asymmetry_scorer_result"]["asymmetry_score"])

    def test_not_significant(self):
        r = self._run()
        assert r.is_significant is False
        assert _mechanism()["asymmetry_scorer_result"]["is_significant"] is False

    def test_p_value_degenerate(self):
        r = self._run()
        assert r.p_value == 1.0

    def test_cohens_d_matches(self):
        r = self._run()
        assert r.cohens_d == pytest.approx(_mechanism()["asymmetry_scorer_result"]["cohens_d"], abs=0.01)

    def test_manual_illustrative_note_present(self):
        method = _mechanism()["asymmetry_scorer_result"]["methodology"]
        assert "MANUAL ILLUSTRATIVE" in method
        assert "n=2 vs n=1" in method


class TestSourceHygiene:
    def test_all_source_urls_https(self):
        for u in _mechanism()["source_urls"]:
            assert u.startswith("https://"), u

    def test_canonical_wired_urls_not_constructed(self):
        srcs = _mechanism()["source_urls"]
        assert MS_EMISSIONS_MIRROR in srcs
        assert MS_SCOUT_URL in srcs
        assert META_CSAM_URL in srcs

    def test_no_em_dashes_in_new_mechanism_text(self):
        assert "\u2014" not in _mechanism_text()
        assert "\u2013" not in _mechanism_text()

    def test_ascii_only_in_new_mechanism_text(self):
        text = _mechanism_text()
        assert all(ord(c) < 128 for c in text)


class TestConfoundersAndDiscipline:
    def test_confounders_ranked_three_tiers(self):
        confs = _mechanism()["confounders"]
        tiers = {c.split("]")[0] for c in confs}
        assert tiers == {"[STRONG", "[MODERATE", "[WEAK"}

    def test_moral_gravity_confounder_present(self):
        confs = _mechanism()["confounders"]
        assert any("Moral-gravity" in c for c in confs)

    def test_counter_evidence_nonempty(self):
        ce = _mechanism()["counter_evidence"]
        assert len(ce) >= 3
        assert any("cuts against" in c for c in ce)

    def test_correlation_not_causation(self):
        m = _mechanism()
        assert "not causation" in m["finding"]
        assert "not causation" in m["asymmetry_scorer_result"]["methodology"]

    def test_research_method_notes_policy_block(self):
        assert "policy-blocked" in _mechanism()["research_method"]


class TestCrossReferences:
    def test_pcm_deal_context_present(self):
        doc = yaml.safe_load(open(WIRED_PROFILE))
        ms = doc["competitor_relationships"]["microsoft"]
        assert "Publisher Content Marketplace" in ms["description"]
        assert ms["coverage_prediction"] == "softer"

    def test_no_prior_wired_microsoft_type_a_file(self):
        names = os.listdir(os.path.join(REPO, "tests"))
        hits = [n for n in names if n.startswith("test_type_a") and "wired" in n and "microsoft" in n]
        assert hits == [os.path.basename(__file__)]

    def test_zero_prior_wired_microsoft_files_overall(self):
        names = os.listdir(os.path.join(REPO, "tests"))
        hits = [n for n in names if "wired" in n and "microsoft" in n]
        assert hits == [os.path.basename(__file__)]


class TestIterationLog:
    def test_502_heading_exists_line_anchored(self):
        log = open(LOG).read()
        assert re.search(r"^#502 Type A:", log, re.M)

    def test_502_segment_names_boundary_condition(self):
        seg = _segment(open(LOG).read(), 502)
        assert "boundary" in seg.lower()

    def test_relative_newest_first_502_before_501(self):
        log = open(LOG).read()
        headings = [(m.start(), m.group(1)) for m in re.finditer(r"^#(\d+) Type [A-E]:", log, re.M)]
        pos = {n: p for p, n in headings}
        assert pos["502"] < pos["501"]

    def test_rotation_line_present_in_segment(self):
        seg = _segment(open(LOG).read(), 502)
        assert "501 E -> 502 A" in seg

    def test_scorer_values_in_segment(self):
        seg = _segment(open(LOG).read(), 502)
        assert "0.90" in seg and "p_value 1.0" in seg
