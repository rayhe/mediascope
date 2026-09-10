"""Type A #647: WIRED x Anthropic Coxon-resignation register vs Meta Muse
trust-deficit register (mechanism 622).

Anthropic arm (existential-seriousness / virtue register, Sep 9 2026, n=1):
 "The AI Researcher Who Just Quit Anthropic Says It's 'Crunch Time for
 Humanity'" (WIRED) - Jacob Coxon interview: "At OpenAI, many have not
 deeply internalized the civilizational stakes. At Anthropic, the stakes
 are well-understood, but they are locked in a race to get there first";
 Evan Hubinger on-record: "we do not yet have a plan to solve alignment
 for superintelligence and are not clearly on track to." Anthropic is the
 lab where humanity's fate is decided; contrasted FAVORABLY against
 OpenAI. +0.25 MANUAL ILLUSTRATIVE.

Meta arm (trust-deficit skepticism register, Sep 8 2026, n=1):
 "Muse, Meta's New Personal AI Agent, Needs You to Trust It" (WIRED,
 Lily Hay Newman + Maxwell Zeff) - the headline makes trust the lede
 obstacle for Meta's biggest consumer AI launch; WIRED reports Meta
 acknowledges Muse Secure VM is "not technically inaccessible to Meta."
 -0.30 MANUAL ILLUSTRATIVE.

Scorer MANUAL ILLUSTRATIVE: illustrative delta (Anthropic minus Meta)
+0.55. n=1 per arm: degenerate statistical contract per the #638/#643
convention (p=1.0, d=0.0); engine NOT run, no divergence pin.

Financial context: Condé Nast multiyear OpenAI licensing deal (Aug 2024),
$0 direct Anthropic tie, $0 Meta tie; mechanism-312 dual-incentive
hypothesis is second-order and inferential. Correlate only.

STRONG confounders: Coxon's resignation was a genuine news event with
congressional alarm (76M X views); Meta's trust deficit is heavily
news-driven (Reuters led the same launch with internal safety concerns).
NOT a falsification-family member (WIRED-Anthropic direct prediction is
neutral; no named gradient contradicted).

Rotation: Type A follows Type E (#646) per A,B,C,D,E. Rotation guard fails
by design pre-anchor; anchor patched in the followup per the #565
convention.
"""

import glob
import os
import re
import subprocess
import sys

import pytest
import yaml

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TEST_BASENAME = os.path.basename(__file__)
PROFILE_PATH = os.path.join(REPO_ROOT, "profiles", "wired.yaml")
LOG_PATH = os.path.join(REPO_ROOT, "iteration-log.md")

MECH_KEY = (
    "mechanism_622_wired_anthropic_coxon_resignation_register_vs_meta_"
    "muse_trust_register_sep10"
)

WIRED_MUSE_URL = (
    "https://www.wired.com/story/"
    "meta-releases-muse-a-personal-ai-agent-with-privacy-built-into-it/"
)
ANTHROPIC_MIRROR_URL = (
    "https://www.15minutenews.com/article/2026/09/09/282659429/"
    "the-ai-researcher-who-just-quit-anthropic-says-its-crunch-time-for-humanity/"
)
QUOTE_SOURCE_URL = (
    "https://aiweekly.co/alerts/anthropic-researcher-coxon-quits-calls-ai-race-endgame"
)

TARGET_SCORES = [0.25]
PEER_SCORES = [-0.30]
TARGET_AVG = 0.25
PEER_AVG = -0.30
EXPECTED_DELTA = 0.55


def _run_git(*args):
    return subprocess.run(
        ["git", "-C", REPO_ROOT, *args],
        capture_output=True,
        text=True,
    )


def _profile():
    with open(PROFILE_PATH) as f:
        return yaml.safe_load(f)


def _entity():
    return _profile()["competitor_relationships"]["anthropic"]


def _mechanism():
    return _entity()[MECH_KEY]


def _read(path):
    with open(os.path.join(REPO_ROOT, path)) as fh:
        return fh.read()


class TestIterationMetadata647:
    def test_iteration_number(self):
        assert 647 == 647

    def test_type_a(self):
        assert _mechanism()["iteration_type"] == "A"

    def test_mechanism_id_next_free(self):
        assert _mechanism()["mechanism_id"] == 622

    def test_mechanism_id_unique_repo_wide(self):
        # Modern-era ids (504+) are collision-free; legacy ids <=503 are NOT
        # unique and are not asserted here.
        ids = []
        for root, _dirs, files in os.walk(os.path.join(REPO_ROOT, "profiles")):
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
        assert ids.count(622) == 1
        # Known pre-existing exception: id 597 is double-registered in
        # profiles/competitor-entities.yaml (pinned by #604 tests).
        modern = [i for i in ids if isinstance(i, int) and i >= 504]
        non597 = [i for i in modern if i != 597]
        assert len(non597) == len(set(non597))
        assert modern.count(597) == 2

    def test_goal_and_job_ids(self):
        m = _mechanism()
        assert m["goal_id"] == "goal_54093bda4145"
        assert m["scheduled_job_id"] == "mediascope-daily-iteration"

    def test_pair_names_wired_anthropic_vs_meta(self):
        assert "WIRED x Anthropic" in _mechanism()["pair"]
        assert "Meta" in _mechanism()["pair"]


class TestWiredAnthropicEntityStructure647:
    def test_anthropic_entity_exists(self):
        assert "anthropic" in _profile()["competitor_relationships"]

    def test_mechanism_key_present(self):
        assert MECH_KEY in _entity()

    def test_one_anthropic_article(self):
        arts = _mechanism()["anthropic_articles"]
        assert len(arts) == 1
        assert "Crunch Time for Humanity" in arts[0]["title"]

    def test_one_meta_article(self):
        arts = _mechanism()["meta_articles"]
        assert len(arts) == 1
        assert "Needs You to Trust It" in arts[0]["title"]

    def test_meta_authors(self):
        art = _mechanism()["meta_articles"][0]
        assert "Lily Hay Newman" in art["journalist"]
        assert "Maxwell Zeff" in art["journalist"]

    def test_urls_verbatim(self):
        text = yaml.dump(_mechanism())
        assert WIRED_MUSE_URL in text
        assert ANTHROPIC_MIRROR_URL in text
        assert QUOTE_SOURCE_URL in text

    def test_no_invented_wired_coxon_url(self):
        # The WIRED Coxon interview URL was never captured (wired.com is
        # policy-blocked); per the no-canonical-URL rule no URL was invented.
        # The only wired.com/story URL in the block must be the Muse one,
        # which third-party mirrors cite verbatim.
        text = yaml.dump(_mechanism())
        wired_story_urls = re.findall(
            r"https://www\.wired\.com/story/[a-z0-9\-/]+", text
        )
        assert wired_story_urls == [WIRED_MUSE_URL], wired_story_urls

    def test_register_fields_present(self):
        for a in _mechanism()["anthropic_articles"] + _mechanism()["meta_articles"]:
            assert "register" in a
            assert "manual_illustrative_tone" in a
            assert "source_note" in a

    def test_coxon_quote_present(self):
        art = _mechanism()["anthropic_articles"][0]
        assert "stakes are well-understood" in art["key_framing"]
        assert "not clearly on track" in art["key_framing"]


class TestToneScorer647:
    def test_scorer_block_methodology_manual(self):
        s = _mechanism()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert "MANUAL ILLUSTRATIVE" in s["methodology"]
        assert "DO NOT claim empirical significance" in s["methodology"]

    def test_target_scores_match_anthropic_tones(self):
        s = _mechanism()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert s["target_scores_MANUAL_ILLUSTRATIVE"] == TARGET_SCORES
        assert s["target_avg"] == TARGET_AVG

    def test_peer_scores_match_meta_tones(self):
        s = _mechanism()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert s["peer_scores_MANUAL_ILLUSTRATIVE"] == PEER_SCORES
        assert s["peer_avg"] == PEER_AVG

    def test_delta_arithmetic_exact(self):
        s = _mechanism()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert s["delta_manual_illustrative"] == EXPECTED_DELTA
        assert s["delta_manual_illustrative"] == round(TARGET_AVG - PEER_AVG, 4)

    def test_degenerate_contract_no_divergence_pin(self):
        # n=1 per arm: degenerate statistical contract per the #638/#643
        # convention (p=1.0, d=0.0). Engine NOT run; divergence pins require
        # engine significance, which cannot occur on n=1 arms.
        s = _mechanism()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        eng = s["engine_degenerate"]
        assert "p=1.0" in eng
        assert "d=0.0" in eng
        assert "no divergence pin" in eng

    def test_finding_layer_refuses(self):
        s = _mechanism()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        finding = s["finding_layer"]
        assert "NOT_CALCULATED" in finding
        assert "is_significant False" in finding

    def test_positive_delta_means_anthropic_softer(self):
        # Positive delta: target (Anthropic) mean > peer (Meta) mean.
        assert EXPECTED_DELTA > 0
        assert TARGET_AVG > PEER_AVG

    def test_convention_stated(self):
        s = _mechanism()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert "target-minus-peer" in s["convention"]
        assert "target = Anthropic arm" in s["convention"]


class TestRegisterAnalysis647:
    def test_anthropic_register_is_seriousness_family(self):
        arts = _mechanism()["anthropic_articles"]
        assert arts[0]["register"] == "existential_seriousness_virtue"

    def test_meta_register_is_trust_deficit_family(self):
        arts = _mechanism()["meta_articles"]
        assert arts[0]["register"] == "trust_deficit_skepticism"

    def test_temporal_matching(self):
        # The pair is temporally matched: Sep 8 (Meta) and Sep 9 (Anthropic),
        # 24 hours apart - the tightest temporal match on the WIRED-Anthropic
        # strand.
        anthropic_date = _mechanism()["anthropic_articles"][0]["date"]
        meta_date = _mechanism()["meta_articles"][0]["date"]
        assert anthropic_date == "2026-09-09"
        assert meta_date == "2026-09-08"

    def test_finding_names_prediction_adjacent_not_proven(self):
        finding = _mechanism()["finding"]
        assert "prediction-adjacent" in finding
        assert "Correlation only" in finding

    def test_finding_names_strong_confounders(self):
        finding = _mechanism()["finding"]
        assert "STRONG confounders dominate" in finding


class TestFinancialContext647:
    def test_predictor_second_order(self):
        fc = _mechanism()["financial_context"]
        assert fc["predictor"] == "second_order_normalization"
        assert fc["prediction"] == "softer_than_expected"

    def test_chain_cites_conde_nast_openai(self):
        fc = _mechanism()["financial_context"]
        assert "Condé Nast" in fc["chain"]
        assert "OpenAI" in fc["chain"]
        assert "$0 direct Anthropic tie" in fc["chain"]

    def test_status_correlate_only(self):
        fc = _mechanism()["financial_context"]
        assert "correlate only" in fc["status"]
        assert "not proof of editorial influence" in fc["status"]


class TestConfounders647:
    def test_two_strong_confounders(self):
        strong = _mechanism()["confounders_ranked"]["strong"]
        assert len(strong) == 2

    def test_news_value_confounder_leads(self):
        strong = _mechanism()["confounders_ranked"]["strong"]
        assert "genuine event" in strong[0]
        assert "76M" in strong[0]

    def test_meta_trust_deficit_confounder(self):
        strong = _mechanism()["confounders_ranked"]["strong"]
        assert "earned trust deficit" in strong[1]
        assert "$18B" in strong[1]

    def test_three_moderate_confounders(self):
        moderate = _mechanism()["confounders_ranked"]["moderate"]
        assert len(moderate) == 3

    def test_genre_skew_confounder(self):
        moderate = _mechanism()["confounders_ranked"]["moderate"]
        assert any("Genre skew" in c for c in moderate)

    def test_not_puff_coverage_confounder(self):
        moderate = _mechanism()["confounders_ranked"]["moderate"]
        assert any("not puff coverage" in c for c in moderate)

    def test_two_weak_confounders(self):
        weak = _mechanism()["confounders_ranked"]["weak"]
        assert len(weak) == 2

    def test_counterevidence_three_items(self):
        ce = _mechanism()["counterevidence"]
        assert len(ce) == 3

    def test_counterevidence_adversarial_capacity(self):
        ce = _mechanism()["counterevidence"]
        assert any("Jul 31 2026" in c for c in ce)


class TestNovelty647:
    def test_zero_test_files_pre_commit(self):
        assert glob.glob(
            os.path.join(REPO_ROOT, "tests", "test_type_a_647*")
        ) == [os.path.join(REPO_ROOT, "tests", TEST_BASENAME)]

    def test_exactly_one_main_commit_647(self):
        # Pre-main-commit this asserted zero matches; post-main-commit it
        # pins exactly one main commit for #647 (followup/doc-sync commits
        # use different subjects and are not counted).
        result = _run_git("log", "--oneline", "-E", "--grep=^Type A #647:")
        lines = [
            line
            for line in result.stdout.splitlines()
            if re.match(r"^[0-9a-f]+ Type A #647:", line)
        ]
        assert len(lines) == 1, result.stdout

    def test_distinct_from_mechanism_312(self):
        finding = _mechanism()["finding"]
        assert "mechanisms 118" in finding
        assert "312 (data-retention coverage-selection silence)" in finding

    def test_sibling_of_642(self):
        xrefs = _mechanism()["cross_references"]
        assert any("#642" in x for x in xrefs)

    def test_not_falsification_member(self):
        finding = _mechanism()["finding"]
        assert "Not a falsification-family member" in finding

    def test_no_647_mechanism_collision(self):
        # No other mechanism in profiles/ is keyed for iteration 647.
        text = _read("profiles/wired.yaml")
        assert text.count("iteration: 647") == 1


class TestRotationCycleGuard647:
    # Deselected pre-commit per the #565 followup convention; anchor patched
    # in the followup once the #647 main-commit SHA is known.
    ANCHORED_SHA = "PATCH_ME_IN_FOLLOWUP"

    @staticmethod
    def _mains():
        out = subprocess.run(
            ["git", "log", "--format=%s"],
            cwd=str(REPO_ROOT),
            capture_output=True,
            text=True,
            check=True,
        ).stdout.splitlines()
        return [s for s in out if re.match(r"^Type [A-E] #\d+:", s)]

    def test_window_643_647_closes_e_to_a(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m, "unparseable rotation subject: %r" % (s,)
            observed.append((m.group(1), m.group(2)))
        assert observed == [
            ("A", "647"),
            ("E", "646"),
            ("D", "645"),
            ("C", "644"),
            ("B", "643"),
        ], "rotation window 643-647 wrong: %r" % (observed,)

    def test_rotation_adjacency_cycle_valid(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m
            observed.append(m.group(1))
        assert observed == ["A", "E", "D", "C", "B"]
        order = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
        for a, b in zip(observed, observed[1:]):
            assert (order[a] - order[b]) % 5 == 1, (
                "rotation broken: %s -> %s is not a valid cycle edge" % (a, b)
            )

    def test_anchor_is_main_commit_patched_in_followup(self):
        result = _run_git("log", "--format=%H %s")
        assert result.returncode == 0
        mains = [
            line for line in result.stdout.splitlines() if "Type A #647:" in line
        ]
        main = mains[0].split()[0] if mains else ""
        assert self.ANCHORED_SHA == main, (
            "anchor patched in followup per #565 convention"
        )


class TestDocSync647:
    # Fails pre-commit by design per the #565 followup convention; the README
    # stats table refresh, narrative line, and ARCHITECTURE row land in the
    # doc-sync commit.
    def _readme_stats(self):
        path = os.path.join(REPO_ROOT, "README.md")
        with open(path) as fh:
            text = fh.read()
        m = re.search(r"\| Tests \| (\d+) \| Across (\d+) test files \|", text)
        assert m, "README stats table row not found"
        return int(m.group(1)), int(m.group(2))

    def _actual_counts(self):
        # Authoritative pytest-based count (same method as the --check gate;
        # the regex estimate undercounts parametrize expansions).
        out = subprocess.run(
            [sys.executable, "scripts/count_stats.py", "--pytest"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            timeout=400,
        )
        m = re.search(r"Total tests\s+(\d+)", out.stdout)
        assert m
        total = int(m.group(1))
        files = len(glob.glob(os.path.join(REPO_ROOT, "tests", "test_*.py")))
        return total, files

    def test_readme_stats_table_fresh(self):
        assert self._readme_stats() == self._actual_counts()

    def test_readme_narrative_line_fresh(self):
        path = os.path.join(REPO_ROOT, "README.md")
        with open(path) as fh:
            text = fh.read()
        m = re.search(r"has \*\*(\d+) tests\*\* across (\d+) test files", text)
        assert m, "README narrative test-count line not found"
        total, files = self._actual_counts()
        assert (int(m.group(1)), int(m.group(2))) == (total, files)

    def test_architecture_row_present(self):
        text = _read("docs/ARCHITECTURE.md")
        assert "test_type_a_647" in text


class TestNoBrittlePatterns647:
    def test_yaml_reparses_clean(self):
        _profile()

    def test_no_em_dash_in_mechanism(self):
        text = yaml.dump(_mechanism(), allow_unicode=False)
        assert "\\u2014" not in text
        assert "—" not in text

    def test_all_urls_http_or_https(self):
        text = yaml.dump(_mechanism())
        urls = re.findall(r"https?://[^\s'\"]+", text)
        assert len(urls) >= 3
        for u in urls:
            assert u.startswith("https://"), u

    def test_research_method_documented(self):
        mech = _mechanism()
        assert "research_method" in yaml.dump(mech)
        assert "browser.search" in mech["research_method"]

    def test_no_engine_significance_claims(self):
        text = yaml.dump(_mechanism())
        assert "NOT_CALCULATED" in text
        assert "is_significant False" in text

    def test_manual_illustrative_labeled(self):
        text = yaml.dump(_mechanism())
        assert "MANUAL ILLUSTRATIVE" in text
