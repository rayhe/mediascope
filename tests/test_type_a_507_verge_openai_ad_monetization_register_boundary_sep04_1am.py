"""Type A #507 (2026-09-04 01:00 PDT): The Verge x OpenAI ad-monetization register
boundary condition.

Second Verge x OpenAI Type A, but a distinct analytical unit from iteration 425
(Aug 31, product/AI-model aspiration-vs-deficit): this one works the
AD-MONETIZATION CONTROVERSY domain. The Vox Media x OpenAI strategic partnership
(May 29 2024, #494) predicts softer OpenAI coverage; observed is an adversarial
register applied to BOTH the deal partner (Mar 2026 ChatGPT uninstalls-spike piece)
and Meta (Apr 2026 Manus undisclosed-ads investigation). The soft register sits in
the Decoder access-interview genre (Nick Turley, Aug 2025), i.e. genre/access
drives register, not entity identity. Joins the falsification family; explicitly
bounded against #425 (incentive pattern holds in the product domain, fails here).

Statistical discipline: MANUAL ILLUSTRATIVE tones at article level, n=2 vs n=2.
Live scorer reproduced this run: delta -0.15, p_value 0.816, cohens_d -0.265,
is_significant False. No significance claimed or claimable. correlation_not_causation.
theverge.com policy-blocked: Manus piece opened first-hand via full-text mirror;
the other three items rest on search excerpts marked second-hand in-mechanism
(mirror-first rule, #492 precedent). No zero-coverage claims. No canonical URLs
constructed: the uninstalls URL is carried verbatim from repo mechanism #48; the
Manus canonical URL never surfaced and was NOT invented.

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
VERGE_PROFILE = os.path.join(REPO, "profiles", "the-verge.yaml")
LOG = os.path.join(REPO, "iteration-log.md")
MECH_KEY = "mechanism_507_verge_openai_ad_monetization_register_boundary_condition"

UNINSTALLS_URL = "https://www.theverge.com/news/653614/chatgpt-uninstalls-spike-openai-ads-pentagon"
MANUS_MIRROR = "https://dailyguardian.ca/meta-is-running-get-rich-quick-ads-for-its-ai-tools/"
DEAL_SOURCE = "https://venturebeat.com/ai/openai-partners-with-the-atlantic-and-the-verge-publisher-vox-media"


def _mechanism():
    with open(VERGE_PROFILE) as f:
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


class TestMechanism507Structure:
    def test_yaml_parses(self):
        with open(VERGE_PROFILE) as f:
            yaml.safe_load(f)

    def test_mechanism_key_exists(self):
        assert MECH_KEY in yaml.safe_load(open(VERGE_PROFILE))["competitor_relationships"]["openai"]

    def test_identity_fields(self):
        m = _mechanism()
        assert m["mechanism_id"] == 507
        assert m["iteration"] == 507
        assert m["iteration_type"] == "A"
        assert m["iteration_time"] == "2026-09-04 01:00 PDT"
        assert m["scheduled_job_id"] == "mediascope-daily-iteration"
        assert m["goal_id"] == "goal_54093bda4145"

    def test_publication_and_pair(self):
        m = _mechanism()
        assert m["publication_focus"] == "The Verge (Vox Media / PMC)"
        assert m["type"].startswith("Type A")

    def test_boundary_condition_framing(self):
        finding = _mechanism()["finding"]
        assert "boundary" in finding.lower()
        assert "genre" in finding.lower()

    def test_deal_partnership_cited(self):
        finding = _mechanism()["finding"]
        assert "May 29 2024" in finding
        assert "#494" in finding

    def test_distinct_from_block_present(self):
        m = _mechanism()
        assert len(m["distinct_from"]) >= 3
        assert any("425" in d for d in m["distinct_from"])


class TestOpenAIArticlesEvidence:
    def test_four_articles_listed(self):
        assert len(_mechanism()["articles"]) == 4

    def test_turley_interview_soft_register(self):
        arts = _mechanism()["articles"]
        turley = arts[0]
        assert "Turley" in turley["title"]
        assert "Decoder" in turley["format"]
        assert turley["manual_illustrative_tone"] == 0.25
        assert "thoughtful and tasteful" in turley["key_phrases"]

    def test_turley_interview_marked_second_hand(self):
        arts = _mechanism()["articles"]
        assert arts[0]["verification"] == "second-hand via search excerpts"
        assert arts[0]["url"] is None

    def test_uninstalls_url_verbatim_from_repo_48(self):
        arts = _mechanism()["articles"]
        assert arts[1]["url"] == UNINSTALLS_URL
        assert "#48" in arts[1]["url_note"]

    def test_uninstalls_adversarial_facts_recorded(self):
        arts = _mechanism()["articles"]
        phrases = " ".join(arts[1]["key_phrases"])
        assert "295%" in phrases
        assert "2.5M" in phrases
        assert arts[1]["manual_illustrative_tone"] == -0.55

    def test_uninstalls_register_adversarial(self):
        arts = _mechanism()["articles"]
        assert "adversarial" in arts[1]["register"]


class TestMetaComparatorEvidence:
    def test_manus_mirror_opened_first_hand(self):
        arts = _mechanism()["articles"]
        assert arts[2]["mirror_opened_first_hand"] == MANUS_MIRROR

    def test_manus_canonical_url_not_constructed(self):
        arts = _mechanism()["articles"]
        assert arts[2]["url"] is None
        assert "NOT invented" in arts[2]["url_note"] or "NOT constructed" in arts[2]["url_note"]

    def test_manus_date_bounded(self):
        arts = _mechanism()["articles"]
        assert "circa" in str(arts[2]["date"])
        assert "unverified" in arts[2]["date_note"]

    def test_manus_adversarial_phrases_recorded(self):
        arts = _mechanism()["articles"]
        phrases = " ".join(arts[2]["key_phrases"])
        assert "probably break the law" in phrases
        assert "did not respond to multiple requests for comment" in phrases
        assert arts[2]["manual_illustrative_tone"] == -0.70

    def test_ai_info_label_excerpt_bounded(self):
        arts = _mechanism()["articles"]
        assert "excerpt-bounded" in arts[3]["url_note"]
        assert arts[3]["verification"] == "second-hand excerpt only"
        assert arts[3]["manual_illustrative_tone"] == 0.10


class TestScorerReproduction:
    def _run(self):
        from mediascope.score.asymmetry import calculate_asymmetry
        return calculate_asymmetry(
            target_scores=[-0.70, 0.10],
            peer_scores=[0.25, -0.55],
            target_entity="meta",
            peer_entities=["openai"],
            publication_slug="the-verge",
            period_start=datetime(2025, 8, 1),
            period_end=datetime(2026, 9, 4),
        )

    def test_delta_matches_profile(self):
        r = self._run()
        assert r.asymmetry_score == pytest.approx(_mechanism()["asymmetry_scorer_result"]["asymmetry_score"])

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


class TestSourceHygiene:
    def test_all_source_urls_https(self):
        for u in _mechanism()["source_urls"]:
            assert u.startswith("https://"), u

    def test_deal_source_present(self):
        assert DEAL_SOURCE in _mechanism()["source_urls"]

    def test_manus_mirror_in_sources(self):
        assert MANUS_MIRROR in _mechanism()["source_urls"]

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

    def test_genre_confounder_present(self):
        confs = _mechanism()["confounders"]
        assert any("Genre confound" in c for c in confs)

    def test_425_domain_tension_present(self):
        confs = _mechanism()["confounders"]
        assert any("#425" in c for c in confs)

    def test_counter_evidence_nonempty(self):
        ce = _mechanism()["counter_evidence"]
        assert len(ce) >= 3
        assert any("Turley" in c for c in ce)

    def test_correlation_not_causation(self):
        m = _mechanism()
        assert "not causation" in m["finding"]
        assert "not causation" in m["asymmetry_scorer_result"]["methodology"]

    def test_research_method_notes_policy_block(self):
        assert "policy-blocked" in _mechanism()["research_method"]

    def test_no_zero_coverage_claims(self):
        assert "no zero-coverage claims" in _mechanism()["research_method"]


class TestNoveltyVs425And48:
    def test_no_prior_type_a_verge_openai_ads_file(self):
        names = os.listdir(os.path.join(REPO, "tests"))
        hits = [n for n in names
                if n.startswith("test_type_a") and "verge" in n and "openai" in n and "ad" in n]
        assert hits == [os.path.basename(__file__)]

    def test_mechanism_key_unique_in_profile(self):
        doc = yaml.safe_load(open(VERGE_PROFILE))
        keys = list(doc["competitor_relationships"]["openai"].keys())
        assert keys.count(MECH_KEY) == 1

    def test_zero_article_overlap_with_425_noted(self):
        distinct = _mechanism()["distinct_from"]
        assert any("zero article overlap" in d for d in distinct)


class TestIterationLog:
    def test_507_heading_exists_line_anchored(self):
        log = open(LOG).read()
        assert re.search(r"^#507 Type A:", log, re.M)

    def test_507_segment_names_boundary_condition(self):
        seg = _segment(open(LOG).read(), 507)
        assert "boundary" in seg.lower()

    def test_relative_newest_first_507_before_506(self):
        log = open(LOG).read()
        headings = [(m.start(), m.group(1)) for m in re.finditer(r"^#(\d+) Type [A-E]:", log, re.M)]
        pos = {n: p for p, n in headings}
        assert pos["507"] < pos["506"]

    def test_rotation_line_present_in_segment(self):
        seg = _segment(open(LOG).read(), 507)
        assert "506 E -> 507 A" in seg

    def test_scorer_values_in_segment(self):
        seg = _segment(open(LOG).read(), 507)
        assert "-0.15" in seg and "p_value 0.816" in seg

    def test_novelty_block_present_in_segment(self):
        seg = _segment(open(LOG).read(), 507)
        assert "Novelty Verification" in seg
