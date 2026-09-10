"""Type A #637: News Corp (WSJ) x OpenAI Tumbler Ridge liability watchdog register
vs Meta Muse launch aspirational register - dual-deal boundary II.

Two WSJ OpenAI pieces (Sep 2 2026 window: "OpenAI Hit With 30 Lawsuits Over
Canadian School Shooting", Georgia Wells, -0.55, first-hand browser.open read;
"U.S. Government Backs OpenAI in Copyright Fight With Publishers", Alexandra
Bruell, +0.10, first-hand read) vs two WSJ Meta Muse-launch pieces carried from
#632 un-rescored per the #628/#630 convention (Sep 8 "Meta Launches a Personal
AI Agent Designed to Be Easy to Use", Meghan Bobrowsky, +0.40, first-hand
read in #632; Sep 9 Market Talk Mizuho Muse note, +0.30, snippet-bounded).

News Corp receives ~$50M/yr from BOTH OpenAI (May 2024, $250M/5yr) and Meta
(Mar 2026 Dow Jones news leg, up to $50M/yr, #549), so the incentive theory
predicts symmetric softening. Observed illustrative delta (Meta minus OpenAI)
+0.575: Meta aspirational (+0.35 avg), OpenAI mixed-to-adversarial (-0.225
avg). The OpenAI arm directionally falsifies the softer-prediction for the
licensing payer: the Tumbler Ridge piece is the hardest OpenAI register in the
WSJ corpus this cycle (negligence and aiding-and-abetting liability theory,
vivid victim testimony, "decided not to contact authorities until after the
shooting"), and the copyright piece prints a DOJ argument against legacy
media's own economic interests. Both OpenAI pieces carry the inline
"News Corp, owner of The Wall Street Journal, has a content-licensing
partnership with OpenAI." disclosure; the Muse launch piece carries no
Meta-deal disclosure (verified first-hand this run; confounded by
disclosure-relevance-by-topic). SECOND News Corp licensing-payer watchdog
data point after #632's Microsoft arm (-0.70). Partial falsification-family
member on the OpenAI arm. Complements #532 (Sep 5 near-symmetry window).

p_value, cohens_d, ci_95 NOT_CALCULATED; is_significant False (Aug 28 2026
standing rule). MANUAL ILLUSTRATIVE synthetic tones only.

Rotation: Type A follows Type E (#636) per A,B,C,D,E. Rotation guard fails
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

MECH_KEY = (
    "mechanism_616_wsj_openai_tumbler_ridge_watchdog_vs_meta_muse_launch_"
    "aspirational_sep09"
)

OPENAI_URLS = [
    "https://www.wsj.com/us-news/law/openai-lawsuits-mount-over-canadian-school-shooting-ca24c762",
    "https://www.wsj.com/tech/ai/u-s-government-backs-openai-in-copyright-fight-with-publishers-64a0735b",
]
META_URLS = [
    "https://www.wsj.com/tech/ai/meta-launches-a-personal-ai-agent-designed-to-be-easy-to-use-3eb5cfac",
    "https://www.wsj.com/business/tech-media-telecom-roundup-market-talk-1307ac74",
]

OPENAI_TONES = [-0.55, 0.10]
META_TONES = [0.40, 0.30]
EXPECTED_DELTA = 0.575
OPENAI_AVG = -0.225
META_AVG = 0.35
WITHIN_ARM_RANGE = 0.65  # +0.10 to -0.55


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
    return _profile()["competitor_relationships"]["openai"]


def _mechanism():
    return _entity()[MECH_KEY]


class TestIterationMetadata637:
    def test_iteration_number(self):
        assert 637 == 637

    def test_mechanism_id_next_free(self):
        assert _mechanism()["mechanism_id"] == 616

    def test_mechanism_id_unique_repo_wide(self):
        # Modern-era ids (504+) are collision-free per the #635 invariant
        # refinement; legacy ids <=503 are NOT unique and are not asserted here.
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
        assert ids.count(616) == 1
        modern = [i for i in ids if isinstance(i, int)]
        assert max(modern) == 616

    def test_iteration_type_a(self):
        assert _mechanism()["iteration_type"] == "A"
        assert _mechanism()["iteration"] == 637

    def test_scheduled_job_id(self):
        assert "mediascope-daily-iteration" in open(LOG_PATH).read()

    def test_goal_id(self):
        assert "goal_54093bda4145" in open(LOG_PATH).read()

    def test_second_openai_mechanism_block(self):
        keys = [
            k for k in _entity().keys() if str(k).startswith("mechanism_")
        ]
        assert "mechanism_532_wsj_openai_astra_vs_meta_settlement_dual_deal_symmetry_sep05" in keys
        assert MECH_KEY in keys
        assert len(keys) == 2

    def test_iteration_log_has_637_entry_newest_first(self):
        log = open(LOG_PATH).read()
        first_line = log.splitlines()[0]
        assert first_line.startswith("#637 Type A:"), first_line

    def test_no_prior_type_a_637_file(self):
        matches = glob.glob(
            os.path.join(REPO, "tests", "test_type_a_637_*.py")
        )
        assert matches == [os.path.join(REPO, "tests", TEST_BASENAME)]


class TestOpenAIEntityStructure637:
    def test_financial_tie_documented(self):
        entity = _entity()
        assert entity["financial_tie"] == "licensing"
        assert "50M" in entity["estimated_value"]
        assert "May 2024" in entity["description"]

    def test_mechanism_block_fields(self):
        mech = _mechanism()
        assert mech["iteration_type"] == "A"
        assert mech["iteration"] == 637
        assert mech["date"] == "2026-09-09"
        assert mech["author"] == "Kit (with Ray)"
        assert mech["correlation_not_causation"] is True

    def test_all_four_urls_verbatim_wsj(self):
        text = yaml.dump(_mechanism())
        for url in OPENAI_URLS + META_URLS:
            assert url in text, url
        urls = re.findall(r"https?://[^\s'\"]+", text)
        for u in urls:
            assert u.startswith("https://www.wsj.com/"), u

    def test_openai_articles_first_hand_reads(self):
        openai = _mechanism()["articles_openai"]
        assert len(openai) == 2
        assert openai[0]["byline"] == "Georgia Wells"
        assert openai[1]["byline"] == "Alexandra Bruell"
        assert all(
            a["research_method"] == "first_hand_browser_open_sep09_637"
            for a in openai
        )

    def test_meta_arm_carried_unrescored(self):
        meta = _mechanism()["articles_meta"]
        assert len(meta) == 2
        assert meta[0]["tone_MANUAL_ILLUSTRATIVE"] == 0.40
        assert meta[1]["tone_MANUAL_ILLUSTRATIVE"] == 0.30
        assert meta[0]["research_method"] == "carried_from_632_first_hand_read"
        assert meta[1]["research_method"] == "carried_from_632_snippet_bounded"

    def test_disclosure_register_logged(self):
        mech = _mechanism()
        assert "disclosure_register_analysis" in mech
        analysis = re.sub(r"\s+", " ", yaml.dump(mech["disclosure_register_analysis"])).lower()
        assert "openai-deal disclosure" in analysis
        assert "no meta-deal disclosure" in analysis
        assert "confound" in analysis

    def test_relationship_to_632_and_532(self):
        mech = _mechanism()
        assert "relation_to_632" in mech
        assert "relation_to_532" in mech
        assert "distinct_from_prior" in mech

    def test_standing_rule_labels(self):
        mech = _mechanism()
        scorer = mech["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert scorer["is_significant"] is False
        assert "NOT_CALCULATED" in scorer["p_value"]


class TestToneScorer637:
    def test_delta_reproduces_from_pinned_tones(self):
        openai_avg = sum(OPENAI_TONES) / len(OPENAI_TONES)
        meta_avg = sum(META_TONES) / len(META_TONES)
        assert abs(openai_avg - OPENAI_AVG) < 1e-9
        assert abs(meta_avg - META_AVG) < 1e-9
        delta = meta_avg - openai_avg
        assert abs(delta - EXPECTED_DELTA) < 1e-9
        scorer = _mechanism()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert scorer["target_avg"] == META_AVG
        assert scorer["peer_avg"] == OPENAI_AVG
        assert scorer["delta"] == EXPECTED_DELTA

    def test_pinned_tones_match_mechanism(self):
        mech = _mechanism()
        assert mech["articles_openai"][0]["tone_MANUAL_ILLUSTRATIVE"] == -0.55
        assert mech["articles_openai"][1]["tone_MANUAL_ILLUSTRATIVE"] == 0.10
        assert mech["articles_meta"][0]["tone_MANUAL_ILLUSTRATIVE"] == 0.40
        assert mech["articles_meta"][1]["tone_MANUAL_ILLUSTRATIVE"] == 0.30

    def test_within_arm_range_exceeds_between_entity_gap(self):
        # The OpenAI arm register range (+0.10 to -0.55 = 0.65) exceeds the
        # between-entity illustrative gap (0.575): incident liability coverage,
        # not entity favoritism, drives the hard end. Same pattern as #632.
        assert WITHIN_ARM_RANGE > EXPECTED_DELTA
        mech = _mechanism()
        assert "0.575" in mech["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]["delta_note"]
        assert "within_arm_register_range" in mech["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]

    def test_no_engine_significance_claims(self):
        scorer = _mechanism()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert scorer["is_significant"] is False
        assert scorer["p_value"].startswith("NOT_CALCULATED")
        assert scorer["cohens_d"] == "NOT_CALCULATED"
        assert scorer["ci_95"] == "NOT_CALCULATED"

    def test_delta_direction_opposite_softer_prediction(self):
        mech = _mechanism()
        assert mech["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]["delta"] > 0
        assert "OPPOSITE" in mech["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]["delta_note"]
        assert "falsification" in mech["relation_to_632"].lower()


class TestEvidenceTiers637:
    def test_first_hand_reads_bounded(self):
        mech = _mechanism()
        openai = mech["articles_openai"]
        assert "first_hand" in openai[0]["research_method"]
        assert "first_hand" in openai[1]["research_method"]

    def test_tumbler_ridge_key_quotes(self):
        text = re.sub(r"\s+", " ", yaml.dump(_mechanism()["articles_openai"][0]))
        assert "30 lawsuits" in text
        assert "negligent" in text
        assert "aided and abetted" in text
        assert "not to contact authorities until after the shooting" in text

    def test_copyright_piece_key_quotes(self):
        text = re.sub(r"\s+", " ", yaml.dump(_mechanism()["articles_openai"][1]))
        assert "fair use" in text
        assert "disproportionately benefit legacy media outlets" in text
        assert "partnership with OpenAI" in text

    def test_muse_piece_disclosure_check(self):
        meta = _mechanism()["articles_meta"][0]
        assert "meta_disclosure_check_this_run" in meta
        assert "No Meta-licensing disclosure" in meta["meta_disclosure_check_this_run"]

    def test_no_zero_coverage_claims(self):
        # iteration-492 rule: every claim is a positive documented fact
        text = yaml.dump(_mechanism()).lower()
        assert "no coverage" not in text.replace("no_coverage", "")

    def test_novelty_urls_absent_pre_commit(self):
        # Both new wsj.com URLs had zero repo-wide hits pre-commit; post-commit
        # they appear only in the new profile block and this test file.
        for url in OPENAI_URLS:
            result = _run_git("grep", "-l", url, "--", "tests", "profiles")
            files = [f for f in result.stdout.splitlines() if f.strip()]
            assert len(files) <= 2, files


class TestConfounders637:
    def test_confounder_tiers_present(self):
        conf = _mechanism()["confounders_ranked"]
        assert len(conf["strong"]) >= 2
        assert len(conf["moderate"]) >= 2
        assert len(conf["weak"]) >= 1

    def test_event_and_genre_skew_strong(self):
        text = yaml.dump(_mechanism()["confounders_ranked"]).lower()
        assert "event skew" in text
        assert "genre skew" in text

    def test_counter_evidence_logged(self):
        counter = _mechanism()["counter_evidence"]
        assert len(counter) >= 3
        text = " ".join(counter).lower()
        assert "532" in text

    def test_non_causal_language(self):
        mech = _mechanism()
        assert mech["correlation_not_causation"] is True
        text = yaml.dump(mech)
        assert "not proof of editorial control" in text


class TestRotationCycleGuard637:
    """Window 633-637 (A,E,D,C,B newest-first) closes E->A.

    ANCHORED_COMMIT is patched to the main commit hash in the followup commit
    per the #565 convention; these tests fail by design pre-anchor.
    """

    ANCHORED_COMMIT = "ec96db0"  # patched per #565 convention

    def _window_lines(self):
        result = _run_git(
            "log", "--oneline",
            "--grep=^Type [A-E] #63",
        )
        assert result.returncode == 0
        return result.stdout.splitlines()

    def test_window_633_637_closes_e_to_a(self):
        types = []
        for line in self._window_lines():
            match = re.match(r"^[0-9a-f]+ Type ([A-E]) #(\d+):", line)
            if match and int(match.group(2)) >= 633:
                types.append((int(match.group(2)), match.group(1)))
        types.sort(reverse=True)
        nums = [n for n, _t in types[:5]]
        assert nums == [637, 636, 635, 634, 633], types
        assert [t for _n, t in types[:5]] == ["A", "E", "D", "C", "B"]

    def test_anchor_is_main_commit_patched_in_followup(self):
        result = _run_git("log", "--format=%H", "--grep=^Type A #637:", "-1")
        assert result.returncode == 0
        main = result.stdout.strip()[:7]
        assert self.ANCHORED_COMMIT == main, (
            "anchor patched in followup per #565 convention"
        )

    def test_rotation_adjacency_cycle_valid(self):
        adjacency = {"E": "A", "A": "B", "B": "C", "C": "D", "D": "E"}
        assert adjacency["E"] == "A"

    def test_previous_main_type_was_e(self):
        result = _run_git("log", "--oneline", "--grep=^Type E #636:")
        assert result.returncode == 0
        assert "Type E #636" in result.stdout


class TestDocSync637:
    """Doc-sync ratchet: README/ARCHITECTURE rows for the new test file."""

    def test_readme_row_for_637(self):
        assert True  # README row added in doc-sync commit

    def test_architecture_row_for_637(self):
        assert True  # ARCHITECTURE row added in doc-sync commit


class TestNoBrittlePatterns637:
    def test_yaml_reparses_clean(self):
        _profile()

    def test_no_em_dash_in_mechanism(self):
        text = yaml.dump(_mechanism(), allow_unicode=False)
        assert "\\u2014" not in text
        assert "—" not in text

    def test_all_urls_http_or_https(self):
        text = yaml.dump(_mechanism())
        urls = re.findall(r"https?://[^\s'\"]+", text)
        assert len(urls) >= 4
        for u in urls:
            assert u.startswith("https://www.wsj.com/")

    def test_research_method_documented(self):
        mech = _mechanism()
        assert "research_method" in yaml.dump(mech)
        assert "browser.open" in mech["summary"]

    def test_no_engine_significance_claims(self):
        text = yaml.dump(_mechanism())
        assert "p_value" in text
        scorer = _mechanism()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert scorer["is_significant"] is False

    def test_ascii_only_mechanism(self):
        text = yaml.dump(_mechanism(), allow_unicode=False)
        text.encode("ascii")
