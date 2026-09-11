"""Type A #667: Reuters x OpenAI Sep 4-10 2026 register vs Reuters x Meta
Muse-launch accountability register (mechanism 634, entities.openai).

FIRST dedicated Reuters x OpenAI Type A mechanism. All three OpenAI-arm
URLs are NEW to the corpus this run (repo-wide greps on URL fragments):
(1) Sep 8-9, Friar's Communacopia/Goldman conference appearance yields an
enterprise-growth narrative ("pushing its AI into specialized industries
and undercutting open-source rivals on cost"; enterprise revenue up 32%
June-to-July; Jalapeno chip "taped out" within nine months) +0.15 MANUAL
ILLUSTRATIVE, excerpt_bounded (search excerpts plus Sina English mirror
reprint; Reuters original byline unattested; reuters.com not opened
first-hand this run); (2) Sep 10, the ChatGPT for Financial Services
launch carries design-partner validation (Morgan Stanley, Evercore) and
an LSEG/PitchBook/Daloopa data stack +0.20 MANUAL ILLUSTRATIVE,
excerpt_bounded; (3) Sep 4, the Reuters Breakingviews opinion column on
the OpenAI agent breach is adversarial -0.25 MANUAL ILLUSTRATIVE
(opinion genre, byline unattested), used ONLY as within-publication
register-range context (Reuters' OpenAI range spans +0.20 to -0.25,
width 0.45), not a primary straight-news arm.

Meta arm carried from #664/m633 (in corpus): Reuters' Sep 8 Katie Paul
Muse-launch piece runs a hard accountability register ("despite internal
concerns that the technology mismanages its access to sensitive personal
data"; "RAISING THE STAKES FOR SAFETY") -0.45 MANUAL ILLUSTRATIVE.

Scorer MANUAL ILLUSTRATIVE: illustrative delta (OpenAI minus Meta) +0.625
(0.175 - (-0.45)). n=2 vs n=1 arms: degenerate statistical contract
(p=1.0, d=0.0); engine NOT run, no divergence pin. No empirical
significance claimed or computed.

Financial context: predictor payer_leg_incentive predicts softer coverage
from the paid counterparty. Reuters is PAID BY Meta under the Oct 25 2024
multiyear AI news licensing deal (mechanism 633, ACTIVE per the
#599/#609 convention; bounded absence per the iteration-492 rule), while
no Reuters x OpenAI AI licensing deal exists on record (bounded absence;
OpenAI's publisher deals are with FT, Conde Nast, Time, Axel Springer,
Le Monde, Prisa, all covered BY Reuters, not WITH Reuters). Status
CONTRADICTED on the pinned arms: the paid counterparty's Meta coverage
(-0.45) is harder than its OpenAI coverage (+0.175 avg). FOURTEENTH
falsification-family member (after #664 thirteenth; #632/#637 partial
members only). Launch-genre matched-pair nuance: FinServ (+0.20) and
Muse (-0.45) are both product launches, so genre alone does not explain
the gap; launch VALENCE (partner validation vs documented internal safety
concerns plus Shah's on-record admission) is the leading alternative.
Correlation only, not causation.

Rotation: Type A follows Type E (#666) per A,B,C,D,E. Rotation guard
fails by design pre-anchor; anchor patched in the followup per the #565
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
PROFILE_PATH = os.path.join(REPO_ROOT, "profiles", "competitor-entities.yaml")
LOG_PATH = os.path.join(REPO_ROOT, "iteration-log.md")

MECH_KEY = "mechanism_634_reuters_openai_sep_week_register_vs_reuters_meta_muse_register"

FRIAR_CHIP_URL = (
    "https://www.reuters.com/world/china/"
    "openai-offers-ai-chip-design-touts-cost-advantage-over-open-source-"
    "cfo-says-2026-09-09/"
)
FINSERV_URL = (
    "https://www.reuters.com/business/"
    "openai-launches-chatgpt-financial-services-industry-2026-09-10/"
)
BREAKINGVIEWS_URL = (
    "https://www.reuters.com/commentary/breakingviews/"
    "ai-agent-hack-tests-solvency-more-than-sentience-2026-09-04/"
)
REUTERS_MUSE_URL = (
    "https://www.reuters.com/business/"
    "meta-launches-ai-agent-that-can-access-other-apps-send-emails-"
    "make-payments-2026-09-08/"
)

TARGET_SCORES = [0.15, 0.20]
PEER_SCORES = [-0.45]
TARGET_AVG = 0.175
PEER_AVG = -0.45
EXPECTED_DELTA = 0.625


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
    return _profile()["entities"]["openai"]


def _mechanism():
    return _entity()[MECH_KEY]


def _read(path):
    with open(os.path.join(REPO_ROOT, path)) as fh:
        return fh.read()


class TestIterationMetadata667:
    def test_iteration_number(self):
        assert _mechanism()["iteration"] == 667

    def test_type_a(self):
        assert _mechanism()["iteration_type"] == "A"

    def test_mechanism_id_next_free(self):
        assert _mechanism()["mechanism_id"] == 634

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
        assert ids.count(634) == 1
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

    def test_pair_names_reuters_openai_meta(self):
        pair = _mechanism()["pair"]
        assert "Reuters" in pair
        assert "OpenAI" in pair
        assert "Meta" in pair

    def test_iteration_time_sep11_midnight(self):
        assert _mechanism()["iteration_time"] == "2026-09-11 00:00 PDT"

    def test_author_kit_with_ray(self):
        assert _mechanism()["author"] == "Kit (with Ray)"


class TestOpenAIEntityStructure667:
    def test_entity_display_name_openai(self):
        assert _entity()["display_name"] == "OpenAI"

    def test_mechanism_nested_under_openai(self):
        assert MECH_KEY in _entity()
        assert _mechanism()["mechanism_id"] == 634

    def test_sibling_mechanism_609_intact(self):
        sib = _entity()["mechanism_609_openai_india_attribution_deal_blitz"]
        assert sib["mechanism_id"] == 609


class TestToneScorer667:
    def test_target_scores(self):
        m = _mechanism()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert m["target_scores_MANUAL_ILLUSTRATIVE"] == TARGET_SCORES

    def test_peer_scores(self):
        m = _mechanism()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert m["peer_scores_MANUAL_ILLUSTRATIVE"] == PEER_SCORES

    def test_avgs(self):
        m = _mechanism()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert m["target_avg"] == pytest.approx(TARGET_AVG)
        assert m["peer_avg"] == pytest.approx(PEER_AVG)

    def test_delta_calc(self):
        m = _mechanism()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert m["delta_manual_illustrative"] == pytest.approx(EXPECTED_DELTA)
        assert m["target_avg"] - m["peer_avg"] == pytest.approx(EXPECTED_DELTA)
        assert m["delta_calc"] == "0.175 - (-0.45) = 0.625"

    def test_degenerate_contract_documented(self):
        m = _mechanism()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert "p=1.0, d=0.0" in m["engine_degenerate"]
        assert "NOT run" in m["engine_degenerate"]

    def test_finding_layer_refuses(self):
        m = _mechanism()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert "NOT_CALCULATED" in m["finding_layer"]
        assert "is_significant False" in m["finding_layer"]

    def test_manual_illustrative_label_present(self):
        m = _mechanism()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert "MANUAL ILLUSTRATIVE" in m["methodology"]
        assert "DO NOT claim empirical significance" in m["methodology"]

    def test_article_tones_match_scorer_arms(self):
        mech = _mechanism()
        openai_tones = [
            a["manual_illustrative_tone"] for a in mech["openai_articles"]
        ]
        # First two arms are the primary straight-news arms scored above;
        # the third is the Breakingviews register-range context arm.
        assert openai_tones[:2] == TARGET_SCORES
        assert openai_tones[2] == pytest.approx(-0.25)
        assert mech["meta_articles"][0]["manual_illustrative_tone"] == pytest.approx(
            PEER_AVG
        )


class TestRegisterAnalysis667:
    def test_friar_chip_url_verbatim(self):
        art = _mechanism()["openai_articles"][0]
        assert art["url"] == FRIAR_CHIP_URL

    def test_friar_register_enterprise_growth(self):
        art = _mechanism()["openai_articles"][0]
        assert art["register"] == "enterprise_growth_constructive"
        assert "32%" in art["key_framing"]
        assert "undercutting open-source rivals on cost" in art["key_framing"]
        assert "taped out" in art["key_framing"]

    def test_friar_byline_unattested(self):
        art = _mechanism()["openai_articles"][0]
        assert "unattested" in art["byline"]

    def test_finserv_url_verbatim(self):
        art = _mechanism()["openai_articles"][1]
        assert art["url"] == FINSERV_URL

    def test_finserv_register_product_launch_forward(self):
        art = _mechanism()["openai_articles"][1]
        assert art["register"] == "product_launch_forward"
        assert "Morgan Stanley and Evercore" in art["key_framing"]
        assert "LSEG, PitchBook and Daloopa" in art["key_framing"]
        assert "GPT-6 Astra" in art["key_framing"]

    def test_breakingviews_url_verbatim(self):
        art = _mechanism()["openai_articles"][2]
        assert art["url"] == BREAKINGVIEWS_URL

    def test_breakingviews_range_context_only(self):
        art = _mechanism()["openai_articles"][2]
        assert art["register"] == "watchdog_opinion_column"
        assert "register-range context" in art["role"]
        assert "NOT a primary straight-news arm" in art["role"]
        assert "lurid predictions" in art["key_framing"]

    def test_meta_arm_carried_from_664(self):
        art = _mechanism()["meta_articles"][0]
        assert art["url"] == REUTERS_MUSE_URL
        assert art["byline"] == "Katie Paul"
        assert art["register"] == "accountability_launch"
        assert "RAISING THE STAKES FOR SAFETY" in art["key_framing"]
        assert "mismanages its access to sensitive personal data" in art[
            "key_framing"
        ]

    def test_all_register_urls_https(self):
        text = yaml.dump(_mechanism())
        urls = re.findall(r"https?://[^\s'\"]+", text)
        assert len(urls) >= 4
        for u in urls:
            assert u.startswith("https://"), u

    def test_evidence_tier_excerpt_bounded(self):
        for art in _mechanism()["openai_articles"]:
            assert "excerpt-bounded" in art["source_note"]
        assert "reuters.com not opened first-hand" in (
            " ".join(
                a["source_note"] for a in _mechanism()["openai_articles"]
            )
        )


class TestFinancialContext667:
    def test_predictor_payer_leg_incentive(self):
        fc = _mechanism()["financial_context"]
        assert fc["predictor"] == "payer_leg_incentive"
        assert fc["prediction"] == "softer_than_expected"

    def test_chain_names_meta_reuters_deal(self):
        chain = _mechanism()["financial_context"]["chain"]
        assert "Oct 25 2024" in chain
        assert "Mechanism 633" in chain
        assert "ACTIVE" in chain
        assert "bounded absence" in chain

    def test_chain_reuters_openai_no_deal_bounded_absence(self):
        chain = _mechanism()["financial_context"]["chain"]
        assert "NO AI licensing deal on record" in chain
        assert "Conde Nast" in chain
        assert "Le Monde" in chain

    def test_status_contradicted_fourteenth(self):
        status = _mechanism()["financial_context"]["status"]
        assert "contradicted" in status
        assert "FOURTEENTH falsification-family member" in status
        assert "Correlational only" in status


class TestConfounders667:
    def _confounders(self):
        return _mechanism()["confounders_ranked"]

    def test_three_strong_confounders(self):
        assert len(self._confounders()["strong"]) == 3

    def test_news_peg_valence_skew_strong(self):
        strong = " ".join(self._confounders()["strong"])
        assert "News-peg valence skew" in strong
        assert "news-maker inheritance" in strong

    def test_launch_genre_matched_pair_strong(self):
        strong = " ".join(self._confounders()["strong"])
        assert "Launch-genre matched-pair nuance" in strong

    def test_wire_service_genre_strong(self):
        strong = " ".join(self._confounders()["strong"])
        assert "Wire-service genre" in strong
        assert "Trust Principles" in strong

    def test_four_moderate_confounders(self):
        assert len(self._confounders()["moderate"]) == 4

    def test_excerpt_bounded_moderate(self):
        moderate = " ".join(self._confounders()["moderate"])
        assert "Excerpt-bounded evidence tier" in moderate

    def test_breakingviews_opinion_genre_moderate(self):
        moderate = " ".join(self._confounders()["moderate"])
        assert "opinion column" in moderate
        assert "width 0.45" in moderate

    def test_payment_magnitude_moderate(self):
        moderate = " ".join(self._confounders()["moderate"])
        assert "Payment magnitude unknown" in moderate

    def test_two_weak_confounders(self):
        assert len(self._confounders()["weak"]) == 2

    def test_degenerate_weak(self):
        weak = " ".join(self._confounders()["weak"])
        assert "degenerate statistical contract" in weak

    def test_bounded_absence_weak(self):
        weak = " ".join(self._confounders()["weak"])
        assert "Bounded absence" in weak

    def test_counterevidence_four_items(self):
        ce = _mechanism()["counterevidence"]
        assert len(ce) == 4

    def test_counterevidence_breakingviews_adversarial(self):
        ce = " ".join(_mechanism()["counterevidence"])
        assert "lurid predictions" in ce
        assert "adversarial capacity toward OpenAI" in ce

    def test_counterevidence_reuters_self_report_neutral(self):
        ce = " ".join(_mechanism()["counterevidence"])
        assert "neutral facts-first" in ce

    def test_counterevidence_wsj_tumbler_ridge(self):
        ce = " ".join(_mechanism()["counterevidence"])
        assert "#637/m616" in ce
        assert "-0.55" in ce

    def test_counterevidence_shah_admission(self):
        ce = " ".join(_mechanism()["counterevidence"])
        assert "Shah" in ce
        assert "source-driven accountability" in ce


class TestNovelty667:
    def test_zero_test_files_pre_commit(self):
        assert glob.glob(
            os.path.join(REPO_ROOT, "tests", "test_type_a_667*")
        ) == [os.path.join(REPO_ROOT, "tests", TEST_BASENAME)]

    def test_type_a_667_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 followup convention; the main
        # commit exists exactly once post-commit and its SHA matches the
        # rotation-guard anchor patched in the followup. Novelty was
        # verified pre-commit by shell greps (zero test_type_a_667 files,
        # no Type A #667 in git log, zero mechanism_634 keys, the three
        # OpenAI-arm URL fragments new to corpus); this test pins that no
        # duplicate #667 main commit ever appears.
        out = subprocess.run(
            ["git", "log", "--format=%H %s"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=True,
        ).stdout.splitlines()
        mains = [l for l in out if re.match(r"^[0-9a-f]{40} Type A #667:", l)]
        assert len(mains) == 1, (
            "expected exactly one Type A #667 main commit, got: %r" % (mains,)
        )
        sha = mains[0].split(" ", 1)[0]
        anchor = TestRotationCycleGuard667.ANCHORED_SHA
        assert anchor != "PATCH_ME_IN_FOLLOWUP", "anchor not patched"
        assert sha == anchor, "main commit %s != guard anchor %s" % (sha, anchor)

    def test_distinct_from_ft_pair_625(self):
        xrefs = _mechanism()["cross_references"]
        assert any("mechanism 625" in x for x in xrefs)
        assert any("intentionally not duplicated" in x for x in xrefs)

    def test_fourteenth_falsification_family_member(self):
        finding = _mechanism()["finding"]
        assert "FOURTEENTH falsification-family member" in finding
        assert "after #664 thirteenth" in finding
        assert "#632/#637 partial" in finding

    def test_cross_refs_carry_arms(self):
        xrefs = _mechanism()["cross_references"]
        assert any("#664" in x for x in xrefs)
        assert any("#662" in x for x in xrefs)
        assert any("#637" in x for x in xrefs)

    def test_no_667_mechanism_collision(self):
        # No other mechanism in competitor-entities.yaml is keyed for
        # iteration 667.
        text = _read("profiles/competitor-entities.yaml")
        assert text.count("iteration: 667") == 1


class TestRotationCycleGuard667:
    # Deselected pre-commit per the #565 followup convention; anchor patched
    # in the followup once the #667 main-commit SHA is known.
    ANCHORED_SHA = "d0edb822affb5364fe207b6661d6b10d1b44d84b"

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

    def test_window_663_667_closes_e_to_a(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m, "unparseable rotation subject: %r" % (s,)
            observed.append((m.group(1), m.group(2)))
        assert observed == [
            ("A", "667"),
            ("E", "666"),
            ("D", "665"),
            ("C", "664"),
            ("B", "663"),
        ], "rotation window 663-667 wrong: %r" % (observed,)

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
            line for line in result.stdout.splitlines() if "Type A #667:" in line
        ]
        main = mains[0].split()[0] if mains else ""
        assert self.ANCHORED_SHA == main, (
            "anchor patched in followup per #565 convention"
        )


class TestDocSync667:
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
        assert "test_type_a_667" in text

    def test_iteration_log_entry_667(self):
        text = _read("iteration-log.md")
        assert "#667" in text


class TestNoBrittlePatterns667:
    def test_yaml_reparses_clean(self):
        _profile()
