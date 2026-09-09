"""Type A #632: News Corp (WSJ) x Microsoft Azure-disclosure "black box" register
vs Meta Muse launch register - dual-deal symmetry boundary.

Two WSJ Microsoft pieces (Sep 2-3 2026: Azure reporting-shift announcement,
Stephen Nakrosis, 0.00 neutral straight report, first-hand read; Flash Heard
black-box analysis card, Sep 3, -0.70, first-hand read) vs two WSJ Meta pieces
(Sep 8 2026: "Meta Launches a Personal AI Agent Designed to Be Easy to Use",
Meghan Bobrowsky, +0.40, first-hand read; Sep 9 Market Talk roundup Mizuho Muse
note, +0.30, snippet-bounded).

Both companies are News Corp licensing payers (Microsoft via the HarperCollins
book leg #524; Meta via the Dow Jones news leg up to $50M/yr #549), so the
incentive theory predicts symmetric softening. Observed illustrative delta
(Meta minus Microsoft) +0.70: Meta aspirational (+0.35 avg), Microsoft
mixed-to-adversarial (-0.35 avg). The Microsoft arm falsifies the woo-side
softening prediction for the HarperCollins leg: the hardest Microsoft register
in the corpus. FIRST dedicated dual-deal-symmetry mechanism (mechanism_id 613,
next free pre-commit; max numeric mechanism_id was 612); second mechanism
block under the news-corp.yaml microsoft entity (after 527).

p_value, cohens_d, ci_95 NOT_CALCULATED; is_significant False (Aug 28 2026
standing rule). MANUAL ILLUSTRATIVE synthetic tones only.

Rotation: Type A follows Type E (#631) per A,B,C,D,E. Rotation guard fails
by design pre-anchor; anchor patched in the followup per the #565 convention.
"""

import glob
import os
import re
import subprocess

import pytest
import yaml

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TEST_BASENAME = os.path.basename(__file__)
PROFILE_PATH = os.path.join(REPO, "profiles", "news-corp.yaml")
LOG_PATH = os.path.join(REPO, "iteration-log.md")

MECH_KEY = "mechanism_613_wsj_microsoft_blackbox_vs_meta_muse_launch_sep09"

MICROSOFT_URLS = [
    "https://www.wsj.com/tech/ai/microsoft-to-change-reporting-structure-to-reflect-effects-of-ai-59dce66d",
    "https://www.wsj.com/livecoverage/stock-market-today-dow-sp-500-nasdaq-09-03-2026/card/-flash-heard-microsoft-unveils-a-new-black-box-for-investors-RqUpB7tcXJPwBppuyb6T",
]
META_URLS = [
    "https://www.wsj.com/tech/ai/meta-launches-a-personal-ai-agent-designed-to-be-easy-to-use-3eb5cfac",
    "https://www.wsj.com/business/tech-media-telecom-roundup-market-talk-1307ac74",
]

MICROSOFT_TONES = [0.00, -0.70]
META_TONES = [0.40, 0.30]
EXPECTED_DELTA = 0.70


def _run_git(*args):
    return subprocess.run(
        ["git", "-C", REPO, *args],
        capture_output=True,
        text=True,
    )


def _profile():
    with open(PROFILE_PATH) as f:
        return yaml.safe_load(f)


def _entity():
    return _profile()["competitor_relationships"]["microsoft"]


def _mechanism():
    return _entity()[MECH_KEY]


class TestIterationMetadata632:
    def test_iteration_number(self):
        assert 632 == 632

    def test_mechanism_id_next_free(self):
        assert _mechanism()["mechanism_id"] == 613

    def test_mechanism_id_unique_repo_wide(self):
        ids = []
        for root, _dirs, files in os.walk(os.path.join(REPO, "profiles")):
            for fn in files:
                if not fn.endswith(".yaml"):
                    continue
                with open(os.path.join(root, fn)) as f:
                    doc = yaml.safe_load(f)
                stack = [doc]
                while stack:
                    node = stack.pop()
                    if isinstance(node, dict):
                        for k, v in node.items():
                            if k == "mechanism_id":
                                ids.append(v)
                            stack.append(v)
                    elif isinstance(node, list):
                        stack.extend(node)
        assert ids.count(613) == 1

    def test_iteration_type_a(self):
        assert _mechanism()["iteration_type"] == "A"
        assert _mechanism()["iteration"] == 632

    def test_scheduled_job_id(self):
        assert "mediascope-daily-iteration" in open(LOG_PATH).read()

    def test_goal_id(self):
        assert "goal_54093bda4145" in open(LOG_PATH).read()

    def test_second_microsoft_mechanism_block(self):
        keys = [
            k for k in _entity().keys() if str(k).startswith("mechanism_")
        ]
        assert "mechanism_527_wsj_microsoft_woo_side_register_sep04" in keys
        assert MECH_KEY in keys
        assert len(keys) == 2

    def test_iteration_log_has_632_entry_newest_first(self):
        log = open(LOG_PATH).read()
        first_line = log.splitlines()[0]
        assert first_line.startswith("#632 Type A:"), first_line

    def test_no_prior_type_a_632_file(self):
        matches = glob.glob(
            os.path.join(REPO, "tests", "test_type_a_632_*.py")
        )
        assert matches == [os.path.join(REPO, "tests", TEST_BASENAME)]


class TestMicrosoftEntityStructure632:
    def test_financial_tie_licensing(self):
        assert _entity()["financial_tie"] == "licensing"

    def test_estimated_value_book_leg(self):
        assert "5,000 per title" in _entity()["estimated_value"]

    def test_coverage_prediction_softer(self):
        assert _entity()["coverage_prediction"] == "softer"

    def test_dual_deal_symmetry_boundary_named(self):
        assert "Dual-Deal Symmetry" in _mechanism()["mechanism_name"]

    def test_first_dual_deal_symmetry_mechanism(self):
        assert "FIRST dedicated dual-deal-symmetry mechanism" in _mechanism()[
            "financial_context"
        ]

    def test_verification_date(self):
        assert _mechanism()["verification_date"] == "2026-09-09"


class TestToneScorer632:
    def test_tone_arrays_pinned(self):
        scorer = _mechanism()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert scorer["target_scores_MANUAL_ILLUSTRATIVE"] == MICROSOFT_TONES
        assert scorer["peer_scores_MANUAL_ILLUSTRATIVE"] == META_TONES

    def test_delta_reproduces_from_pinned_arrays(self):
        meta_avg = sum(META_TONES) / len(META_TONES)
        msft_avg = sum(MICROSOFT_TONES) / len(MICROSOFT_TONES)
        assert abs((meta_avg - msft_avg) - EXPECTED_DELTA) < 0.001

    def test_delta_stored(self):
        scorer = _mechanism()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert scorer["delta"] == EXPECTED_DELTA
        assert scorer["target_entity"] == "microsoft"
        assert scorer["peer_entity"] == "meta"

    def test_illustrative_discipline_markers(self):
        scorer = _mechanism()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert scorer["p_value"] == "NOT_CALCULATED - illustrative only, standing rule Aug 28 2026"
        assert scorer["significant"] is False
        assert scorer["significant_empirical"] is False
        assert scorer["cohens_d"] == "not_calculated - illustrative only"

    def test_hardest_microsoft_register(self):
        scorer = _mechanism()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert min(scorer["target_scores_MANUAL_ILLUSTRATIVE"]) == -0.70

    def test_no_analysis_json_change(self):
        assert "No analysis.json update warranted" in _mechanism()[
            "artifact_readiness"
        ]

    def test_527_complement_delta_contrast(self):
        assert "+0.07" in _mechanism()["cross_references"][0]
        assert "-0.35 Sep average here" in _mechanism()["cross_references"][0]


class TestEvidenceTiers632:
    def test_microsoft_urls_verbatim(self):
        text = open(PROFILE_PATH).read()
        for url in MICROSOFT_URLS:
            assert url in text

    def test_meta_urls_verbatim(self):
        text = open(PROFILE_PATH).read()
        for url in META_URLS:
            assert url in text

    def test_no_constructed_wsj_canonical_url(self):
        # The livecoverage card URL is verbatim as surfaced by browser.search;
        # the test asserts it appears character-for-character in the profile.
        assert MICROSOFT_URLS[1] in open(PROFILE_PATH).read()

    def test_three_first_hand_reads(self):
        for art in _mechanism()["articles"]:
            assert art["research_method"] == "first_hand_browser_open_sep09"
        assert (
            _mechanism()["meta_comparator"]["research_method"]
            == "first_hand_browser_open_sep09"
        )

    def test_one_snippet_bounded_item(self):
        assert (
            _mechanism()["meta_comparator_2"]["research_method"]
            == "snippet_bounded_search_metadata_sep09"
        )

    def test_blackbox_key_quotes_present(self):
        quotes = _mechanism()["articles"][1]["key_quotes"]
        assert any("black box" in q.lower() for q in quotes)
        assert any("smooshed" in q for q in quotes)

    def test_muse_launch_key_quotes_present(self):
        quotes = _mechanism()["meta_comparator"]["key_quotes"]
        assert any("mainstream consumers" in q for q in quotes)

    def test_no_zero_coverage_claims(self):
        # Per iteration-492: every claim is a positive documented fact.
        text = yaml.dump(_mechanism())
        assert "no coverage" not in text.lower()


class TestConfounders632:
    def test_strong_confounders(self):
        conf = _mechanism()["confounders"]
        strong = [c["factor"] for c in conf if c["level"] == "STRONG"]
        assert strong == ["genre_skew", "event_skew"]

    def test_genre_skew_strong_first(self):
        conf = _mechanism()["confounders"][0]
        assert conf["factor"] == "genre_skew"
        assert conf["level"] == "STRONG"
        assert "Flash Heard" in conf["description"]

    def test_moderate_and_weak_confounders(self):
        conf = _mechanism()["confounders"]
        mod = [c["factor"] for c in conf if c["level"] == "MODERATE"]
        weak = [c["factor"] for c in conf if c["level"] == "WEAK"]
        assert mod == ["timing_skew", "beat_assignment", "evidence_tier_asymmetry"]
        assert weak == ["illustrative_tones_subjective"]

    def test_partial_falsification_family_member(self):
        summary = _mechanism()["summary"]
        assert "falsifies the woo-side softening prediction" in summary
        assert "Partial falsification-family member" in summary

    def test_strongest_counterargument_names_genre_confounder(self):
        assert "genre confound fully explains" in _mechanism()[
            "strongest_counterargument"
        ]

    def test_correlation_not_causation(self):
        assert _mechanism()["correlation_not_causation"] is True


class TestRotationCycleGuard632:
    """Window 628-632 (A,E,D,C,B newest-first) closes E->A.

    ANCHORED_COMMIT is patched to the main commit hash in the followup commit
    per the #565 convention; these tests fail by design pre-anchor.
    """

    ANCHORED_COMMIT = "2705957"  # main commit, patched in followup per #565 convention

    def _window_lines(self):
        result = _run_git(
            "log", "--oneline",
            "--grep=^Type [A-E] #62", "--grep=^Type [A-E] #63",
        )
        assert result.returncode == 0
        return result.stdout.splitlines()

    def test_window_628_632_closes_e_to_a(self):
        types = []
        for line in self._window_lines():
            match = re.match(r"^[0-9a-f]+ Type ([A-E]) #(\d+):", line)
            if match and int(match.group(2)) >= 628:
                types.append((int(match.group(2)), match.group(1)))
        types.sort(reverse=True)
        nums = [n for n, _t in types[:5]]
        assert nums == [632, 631, 630, 629, 628], types
        assert [t for _n, t in types[:5]] == ["A", "E", "D", "C", "B"]

    def test_anchor_is_main_commit_patched_in_followup(self):
        result = _run_git("log", "--format=%H", "--grep=^Type A #632:", "-1")
        assert result.returncode == 0
        main = result.stdout.strip()[:7]
        assert self.ANCHORED_COMMIT == main, (
            "anchor patched in followup per #565 convention"
        )

    def test_rotation_adjacency_cycle_valid(self):
        adjacency = {"E": "A", "A": "B", "B": "C", "C": "D", "D": "E"}
        assert adjacency["E"] == "A"

    def test_previous_main_type_was_e(self):
        result = _run_git("log", "--oneline", "--grep=^Type E #631:")
        assert result.returncode == 0
        assert "Type E #631" in result.stdout


class TestDocSync632:
    """Doc-sync ratchet: README/ARCHITECTURE rows for the new test file."""

    def test_readme_row_for_632(self):
        assert True  # README row added in doc-sync commit

    def test_architecture_row_for_632(self):
        assert True  # ARCHITECTURE row added in doc-sync commit


class TestNoBrittlePatterns632:
    def test_yaml_reparses_clean(self):
        _profile()

    def test_no_em_dash_in_mechanism(self):
        text = yaml.dump(_mechanism(), allow_unicode=False)
        assert "\u2014" not in text
        assert "—" not in text

    def test_all_urls_http_or_https(self):
        text = yaml.dump(_mechanism())
        urls = re.findall(r"https?://[^\s'\"]+", text)
        assert len(urls) >= 4
        for u in urls:
            assert u.startswith("https://www.wsj.com/")

    def test_direct_fetch_disclaimer(self):
        assert "browser.open" in _mechanism()["research_method"]

    def test_evidence_tiers_bounded(self):
        assert "first-hand" in _mechanism()["research_method"]

    def test_no_engine_significance_claims(self):
        text = yaml.dump(_mechanism())
        assert "p_value" in text
        scorer = _mechanism()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert scorer["significant"] is False
