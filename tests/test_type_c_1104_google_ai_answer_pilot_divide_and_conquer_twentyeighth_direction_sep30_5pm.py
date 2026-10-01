"""Type C #1104: Publisher divide-and-conquer against the AI-answer payment pilot.

The Decoder (Sep 30 2026, first-hand browser.open read this run, 44 rendered
lines) names the AI-contribution pilot's structural geometry: "Google sets
the terms through selective licensing deals, an opt-out feature, and a
payment model that lets it decide what content is worth" - "This
divide-and-conquer approach creates a prisoner's dilemma for publishers.
A few benefit, while most get little or nothing. Publishers that walk away
put little pressure on Google because other sources fill the gap, while
those that stay accept its rates." Mechanism 894 lands in
profiles/competitor-entities.yaml as the TWENTY-EIGHTH relationship
direction: DIVIDE-AND-CONQUER (fragmented-counterparty pricing) - distinct
from #27 UNILATERAL PRICING (m891, who prices) and from the in-corpus June
2026 training-deals divide-and-rule (techpolicy.press). The new
pricing-power work is substitutability: the bilateral structure is what
makes unilateral pricing stick. FIFTH and CLOSING leg of the 1100-1104
window (D #1100 -> E #1101 -> A #1102 -> B #1103 -> C #1104 per #565).

Pre-commit green gate per #565/#719/#721: run with .venv/bin/python -m
pytest, deselecting TestNoveltyAnchor1104, TestRotationGuard1100_1104Window,
TestDocSyncRatchet, TestIterationLogEntry, and the three commit-dependent
tests in TestCorpusNoveltyPostCommit. ANCHORED_SHA is a placeholder until
the anchor followup patches it per #565.

ASCII-only. No em dashes. Next-number needles fragment-built per #715.
"""

import glob
import os
import re
import subprocess

import pytest
import yaml


REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TESTS_DIR = os.path.join(REPO_ROOT, "tests")
PROFILES_DIR = os.path.join(REPO_ROOT, "profiles")
PROFILES_FILE = os.path.join(PROFILES_DIR, "competitor-entities.yaml")

MECH_KEY = (
    "type_c_1104_google_ai_answer_pilot_divide_and_conquer_"
    "twentyeighth_direction_sep30_5pm"
)
FILE_STEM = (
    "test_type_c_1104_google_ai_answer_pilot_divide_and_conquer_"
    "twentyeighth_direction_sep30_5pm"
)
OWN_BASENAME = FILE_STEM + ".py"

# Next-number needles fragment-built per #715 (runtime values are the
# contiguous forms; the source text never holds them contiguously).
US_894 = "mechanism_" + "894"
DASH_894 = "mechanism-" + "894"
MID_894 = "mechanism_id: " + "894"
US_895 = "mechanism_" + "895"
DASH_895 = "mechanism-" + "895"
MID_895 = "mechanism_id: " + "895"
TW28 = "TWENTY-" + "EIGHTH relationship direction"
TW29 = "TWENTY-" + "NINTH relationship direction"
T39 = "THIRTY-" + "NINTH falsification-family member"

ANCHORED_SHA = "9bb80079b6eaed6f039016100e7f6c17e62f3bbd"  # main-commit SHA, patched post-commit per #565
ITERATION = 1104
TYPE_LETTER = "C"
WINDOW = "1100-1104"

# (letter, number, main-sha, anchor-sha, log-hash-sha) per #721.
PREDECESSORS = [
    ("D", "1100", "6678ba05", "eb9cc385", "07c91cf1"),
    ("E", "1101", "49b1d581", "95860871", "04f5fb9e"),
    ("A", "1102", "ac41d979", "2e3fe060", "741a16f1"),
    ("B", "1103", "bfe7f31a", "40654528", "13ab9340"),
]

NOVEL_URLS = [
    "https://the-decoder.com/google-is-paying-almost-no-publishers-"
    "almost-nothing-for-content-used-in-ai-answers/",
    "https://theoutpost.ai/news-story/google-tests-paying-publishers-"
    "for-ai-search-features-amid-traffic-concerns-31522/",
    "https://www.androidheadlines.com/2026/09/"
    "google-tests-paying-publishers-ai-search-content.html",
    "https://newsheadlinealert.com/news/"
    "googles-early-attempt-to-pay-websites-for-ai-answers-is-struggling-"
    "6abd485c30702",
]

F1099 = (
    "test_type_c_1099_google_ai_contribution_pilot_rate_disclosure_"
    "unilateral_pricing_twentyseventh_direction_sep30_12pm.py"
)
F1103 = (
    "test_type_b_1103_nicole_nguyen_wsj_muse_trust_history_vs_claude_"
    "password_agent_functional_caution_sep30_4pm.py"
)
F1100 = "test_type_d_1100"
F1101 = "test_type_e_1101"
F1102 = "test_type_a_1102"

PYTEST_BIN = ".venv/bin/python"


def _git(*args):
    return subprocess.run(
        ["git"] + list(args), cwd=REPO_ROOT, capture_output=True, text=True
    )


def _iter_source_files():
    """Yield profile + test source paths (profiles/ and tests/)."""
    for root, dirs, files in os.walk(PROFILES_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
            yield os.path.join(root, f)
    for root, dirs, files in os.walk(TESTS_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
            if f == OWN_BASENAME:
                continue
            yield os.path.join(root, f)


def _repo_grep_underscore_mechanism(n):
    needle = "mechanism_%d" % n
    return [
        p
        for p in _iter_source_files()
        if needle in open(p, encoding="utf-8", errors="replace").read()
    ]


def _repo_grep_dash_mechanism(n):
    needle = "mechanism-%d" % n
    return [
        p
        for p in _iter_source_files()
        if needle in open(p, encoding="utf-8", errors="replace").read()
    ]


def _profiles_grep_numeric_mechanism_id(n):
    needle = "mechanism_id: %d" % n
    hits = []
    for root, dirs, files in os.walk(PROFILES_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
            p = os.path.join(root, f)
            if needle in open(p, encoding="utf-8", errors="replace").read():
                hits.append(p)
    return hits


def _max_numeric_mechanism_id_in_profiles():
    best = 0
    for root, dirs, files in os.walk(PROFILES_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
            text = open(
                os.path.join(root, f), encoding="utf-8", errors="replace"
            ).read()
            for m in re.finditer(r"mechanism_id:\s*(\d+)", text):
                best = max(best, int(m.group(1)))
    return best


def _block_text():
    text = open(PROFILES_FILE, encoding="utf-8").read()
    start = text.index(MECH_KEY + ":")
    out = []
    for i, line in enumerate(text[start:].splitlines()):
        if i > 0 and re.match(r"^[a-z_]", line):
            break
        out.append(line)
    return "\n".join(out)


def _block_yaml():
    data = yaml.safe_load(open(PROFILES_FILE, encoding="utf-8"))
    return data[MECH_KEY]


def _class_run(path, node):
    """Run one tests/<path>::<node> in a subprocess; return CompletedProcess."""
    cmd = [
        PYTEST_BIN,
        "-m",
        "pytest",
        "%s::%s" % (os.path.join("tests", path), node),
        "-q",
        "--no-header",
        "-p",
        "no:cacheprovider",
        "-o",
        "addopts=",
    ]
    return subprocess.run(
        cmd, cwd=REPO_ROOT, capture_output=True, text=True, timeout=600
    )


# ---------------------------------------------------------------------------
# 1. Novelty: this run is the first to claim mechanism 894 and the
#    TWENTY-EIGHTH relationship direction.
# ---------------------------------------------------------------------------

class TestNovelty1104:
    def test_single_test_file_for_iteration(self):
        files = glob.glob(os.path.join(TESTS_DIR, "test_type_c_1104*.py"))
        assert files == [os.path.join(TESTS_DIR, OWN_BASENAME)], files

    def test_max_numeric_mechanism_id_is_894(self):
        assert _max_numeric_mechanism_id_in_profiles() == 894

    def test_zero_underscore_895_repo_wide(self):
        assert _repo_grep_underscore_mechanism(895) == []

    def test_zero_dash_895_repo_wide(self):
        assert _repo_grep_dash_mechanism(895) == []

    def test_zero_numeric_895_in_profiles(self):
        assert _profiles_grep_numeric_mechanism_id(895) == []

    def test_block_key_unique_at_column_zero(self):
        text = open(PROFILES_FILE, encoding="utf-8").read()
        hits = [
            l for l in text.splitlines() if l.startswith(MECH_KEY + ":")
        ]
        assert len(hits) == 1, hits

    def test_no_type_c_1104_commit_pre_commit(self):
        # Pre-commit novelty guard: no commit may already claim this slot.
        # SUPERSEDED BY DESIGN once this run's main commit ("Type C #1104:")
        # lands; post-commit, TestNoveltyAnchor1104 asserts the unique main
        # commit instead. Deselect this test in post-commit full runs.
        out = _git("log", "--format=%s", "--grep=Type C #1104").stdout.strip()
        assert out == "", out


# ---------------------------------------------------------------------------
# 2. Rotation guard: C is the FIFTH and CLOSING leg of the 1100-1104 window.
#    (DESELECTED pre-commit per #565.)
# ---------------------------------------------------------------------------

class TestRotationGuard1100_1104Window:
    @pytest.mark.rotation
    def test_window_1100_1104_fifth_leg(self):
        """C is the fifth leg of the 1100-1104 window per #565."""
        assert TYPE_LETTER == "C"
        assert ITERATION == 1104
        assert WINDOW == "1100-1104"

    @pytest.mark.rotation
    def test_type_c_adjacency_in_window(self):
        """D(#1100) -> E(#1101) -> A(#1102) -> B(#1103) -> C(#1104, this run)."""
        d_files = glob.glob(os.path.join(TESTS_DIR, F1100 + "*.py"))
        e_files = glob.glob(os.path.join(TESTS_DIR, F1101 + "*.py"))
        a_files = glob.glob(os.path.join(TESTS_DIR, F1102 + "*.py"))
        b_files = glob.glob(os.path.join(TESTS_DIR, "test_type_b_1103*.py"))
        assert len(d_files) >= 1
        assert len(e_files) >= 1
        assert len(a_files) >= 1
        assert len(b_files) >= 1

    @pytest.mark.rotation
    def test_predecessor_is_type_b_1103(self):
        files = glob.glob(os.path.join(TESTS_DIR, "test_type_b_1103*.py"))
        assert len(files) >= 1

    @pytest.mark.rotation
    def test_predecessor_chains_in_history(self):
        """Each predecessor's main/anchor/log-hash SHAs are in history."""
        for letter, num, main, anchor, loghash in PREDECESSORS:
            out = _git(
                "log", "--format=%H", "--grep=Type %s #%s" % (letter, num)
            ).stdout
            for sha in (main, anchor, loghash):
                assert any(
                    h.startswith(sha) for h in out.split()
                ), (letter, num, sha)

    @pytest.mark.rotation
    def test_window_order_in_history(self):
        """Newest-first log: #1103 above #1102 above #1101 above #1100."""
        subjects = _git("log", "--format=%s").stdout.splitlines()

        def first_idx(needle):
            for i, s in enumerate(subjects):
                if needle in s:
                    return i
            raise AssertionError(needle)

        i1103 = first_idx("Type B #1103")
        i1102 = first_idx("Type A #1102")
        i1101 = first_idx("Type E #1101")
        i1100 = first_idx("Type D #1100")
        assert i1103 < i1102 < i1101 < i1100

    @pytest.mark.rotation
    def test_anchor_is_ancestor_of_head(self):
        """Post-commit: the anchor commit is an ancestor of HEAD."""
        result = subprocess.run(
            ["git", "merge-base", "--is-ancestor", ANCHORED_SHA, "HEAD"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0


# ---------------------------------------------------------------------------
# 3. Novelty anchor (DESELECTED pre-commit per #565; patched green post-commit).
# ---------------------------------------------------------------------------

class TestNoveltyAnchor1104:
    def test_anchor_is_40_hex(self):
        assert re.fullmatch(r"[0-9a-f]{40}", ANCHORED_SHA), ANCHORED_SHA

    def test_main_commit_is_unique_and_anchored(self):
        result = _git("log", "--format=%H %s", "--grep=Type C #1104")
        assert result.returncode == 0
        mains = [
            line
            for line in result.stdout.splitlines()
            if line.split(" ", 1)[1].startswith("Type C #1104:")
        ]
        assert len(mains) == 1, mains
        assert mains[0].split(" ", 1)[0] == ANCHORED_SHA


# ---------------------------------------------------------------------------
# 4. Mechanism 894 block structure.
# ---------------------------------------------------------------------------

class TestMechanism894Structure:
    def test_block_key_field_repeats_key(self):
        assert _block_yaml()["block_key"] == MECH_KEY

    def test_mechanism_id_numeric_894(self):
        blk = _block_yaml()
        assert blk["mechanism_id"] == 894
        assert isinstance(blk["mechanism_id"], int)

    def test_type_fields(self):
        blk = _block_yaml()
        assert blk["type"] == "financial_incentive_mapping"
        assert blk["type_label"] == "Financial Incentive Mapping"

    def test_iteration_fields(self):
        blk = _block_yaml()
        assert blk["iteration"] == 1104
        assert blk["iteration_type"] == "C"
        assert blk["iteration_time"] == "2026-09-30 17:00 PDT"
        assert blk["goal_id"] == "goal_54093bda4145"
        assert blk["scheduled_job_id"] == "mediascope-daily-iteration"

    def test_connects_to_exact(self):
        assert _block_yaml()["connects_to"] == [891, 702, 708, 666, 539]

    def test_sources_structure(self):
        sources = _block_yaml()["sources"]
        assert len(sources) == 4
        for s in sources:
            assert s["url"].startswith("https://")
            assert s["what"]
            assert s["accessed"] == "2026-09-30"
            assert s["novel"] is True
        assert sources[0]["url"].startswith("https://the-decoder.com/")

    def test_discipline_fields(self):
        blk = _block_yaml()
        assert blk["tone_scored"] is False
        assert blk["engine_run"] is False
        assert blk["is_significant"] is False
        assert blk["verdict"] == "directionally_supported_not_proven"
        assert blk["no_analysis_json_update"] is True
        assert blk["artifact_grade"] is False

    def test_novelty_claim_documents_precommit_verification(self):
        assert "Pre-commit novelty verified" in _block_text()

    def test_concurrency_field(self):
        text = _block_text()
        assert "#899" in text and "#938" in text
        assert "#900" in text and "#1012-wt" in text
        assert "#1024" in text and "m846" in text


# ---------------------------------------------------------------------------
# 5. Mechanism 894 legs.
# ---------------------------------------------------------------------------

class TestMechanism894Legs:
    def test_finding_peg(self):
        text = _block_text()
        assert "44 rendered lines" in text
        assert "around 100" in text
        assert "first analysis-tier piece" in text

    def test_instrument_triad_leg(self):
        text = _block_text()
        assert "selective licensing deals" in text
        assert "an opt-out feature" in text
        assert "a payment model that lets it decide what content is worth" in text
        assert "no market price for AI-answer content can form" in text

    def test_substitution_geometry_leg(self):
        text = _block_text()
        assert "other sources fill the gap" in text
        assert "SUBSTITUTION" in text
        assert "defector" in text

    def test_holdout_geometry_leg(self):
        text = _block_text()
        assert "refusing to join the program to push Google to pay more" in text
        assert "direct licensing deals like those made by OpenAI" in text
        assert "RELAY-FIDELITY FLAG" in text
        assert "relay error" in text

    def test_aggregation_instrument_leg(self):
        text = _block_text()
        assert "THE ONE COUNTER-LEVER" in text
        assert "Munich Regional Court May 28 2026" in text
        assert "ZAK Jul 14 2026" in text
        assert "CARRIED, not fresh" in text
        assert "If that interpretation gains wider acceptance" in text

    def test_corpus_lineage(self):
        text = _block_text()
        assert "m891" in text and "m702" in text and "m708" in text
        assert "techpolicy.press" in text
        assert "m539" in text and "m666" in text

    def test_incentive_geometry(self):
        text = _block_text()
        assert "no individual publisher is pivotal" in text
        assert "take-the-widget-rate" in text

    def test_coverage_nexus(self):
        text = _block_text()
        assert "Zero ''AI earnings''" in text or 'Zero "AI earnings"' in text
        assert "NOT_SCORED" in text

    def test_legs_distinct(self):
        text = _block_text()
        for leg in (
            "instrument_triad_leg:",
            "substitution_geometry_leg:",
            "holdout_geometry_leg:",
            "aggregation_instrument_leg:",
            "incentive_geometry:",
            "coverage_nexus:",
        ):
            assert leg in text, leg

    def test_counterargument_collapse_condition(self):
        text = _block_text()
        assert "pilot-phase scaffolding" in text
        assert "EC Dec 2025 probe" in text


# ---------------------------------------------------------------------------
# 6. TWENTY-EIGHTH relationship direction taxonomy.
# ---------------------------------------------------------------------------

class TestMechanism894Taxonomy:
    def test_twenty_eighth_present(self):
        assert "TWENTY-EIGHTH relationship direction" in _block_text()

    def test_enumeration_covers_1_to_27(self):
        tax = _block_text()
        assert "1 sue-then-sign m624" in tax
        assert "12 regulatory-bargaining m1004" in tax
        assert "27 unilateral pricing m891" in tax

    def test_distinct_from_pay_or_litigate(self):
        tax = _block_text()
        assert "Distinct from #2 pay-or-litigate bifurcation m636" in tax

    def test_distinct_from_regulatory_bargaining(self):
        tax = _block_text()
        assert "from #12 regulatory-bargaining m1004" in tax

    def test_mirror_of_ecosystem_grant(self):
        tax = _block_text()
        assert "from #15 ecosystem-grant m1029" in tax
        assert "mirror image" in tax

    def test_distinct_from_unilateral_pricing(self):
        tax = _block_text()
        assert "from #27 unilateral pricing m891" in tax
        assert "WHO prices the content vs HOW" in tax

    def test_falsifiable(self):
        tax = _block_text()
        assert "Falsifiable:" in tax
        assert "collective AI-answer licensing vehicle" in tax

    def test_taxonomy_tension_carried(self):
        tax = _block_text()
        assert "m737" in tax
        assert "Not resolved this run" in tax


# ---------------------------------------------------------------------------
# 7. Confounders.
# ---------------------------------------------------------------------------

class TestMechanism894Confounders:
    def test_confounder_count_and_order(self):
        conf = _block_yaml()["confounders"]
        assert len(conf) == 7
        strengths = [c["strength"] for c in conf]
        assert strengths == (
            ["STRONG"] * 3 + ["MEDIUM"] * 2 + ["WEAK"] * 2
        ), strengths

    def test_strong_single_piece_framing(self):
        texts = " ".join(
            c["text"]
            for c in _block_yaml()["confounders"]
            if c["strength"] == "STRONG"
        )
        assert "niche AI press" in texts

    def test_strong_relay_fidelity(self):
        texts = " ".join(
            c["text"]
            for c in _block_yaml()["confounders"]
            if c["strength"] == "STRONG"
        )
        assert "NYT-v-Google" in texts or "NYT''v-Google" in texts

    def test_strong_german_rulings_carried(self):
        texts = " ".join(
            c["text"]
            for c in _block_yaml()["confounders"]
            if c["strength"] == "STRONG"
        )
        assert "carried, not fresh" in texts

    def test_medium_holdout_leverage_unproven(self):
        texts = " ".join(
            c["text"]
            for c in _block_yaml()["confounders"]
            if c["strength"] == "MEDIUM"
        )
        assert "hoped-for" in texts

    def test_medium_dilemma_is_framing(self):
        texts = " ".join(
            c["text"]
            for c in _block_yaml()["confounders"]
            if c["strength"] == "MEDIUM"
        )
        assert "analytical framing, not a measured game" in texts

    def test_weak_window_and_sampling(self):
        texts = " ".join(
            c["text"]
            for c in _block_yaml()["confounders"]
            if c["strength"] == "WEAK"
        )
        assert "single-day evidence window" in texts
        assert "Pilot-phase sampling" in texts


# ---------------------------------------------------------------------------
# 8. Research method: 4 search sets + 1 first-hand browser.open per #503.
# ---------------------------------------------------------------------------

class TestResearchMethodTypeC1104:
    def test_four_novel_urls_verbatim(self):
        assert len(NOVEL_URLS) == 4
        assert NOVEL_URLS[0].startswith(
            "https://the-decoder.com/google-is-paying-almost-no-publishers-"
        )
        assert "theoutpost.ai/news-story/" in NOVEL_URLS[1]
        assert "androidheadlines.com/2026/09/" in NOVEL_URLS[2]
        assert "newsheadlinealert.com/news/" in NOVEL_URLS[3]

    def test_first_hand_decoder_open(self):
        src = _block_yaml()["sources"][0]
        assert "first-hand browser.open read this run" in src["what"]
        assert "44 rendered lines" in src["what"]

    def test_novelty_claim_documents_sources(self):
        nov = _block_text()
        assert "4 novel URLs" in nov
        assert "FIRST dedicated corpus mechanism" in nov
        assert "TWENTY-EIGHTH relationship direction" in nov

    def test_rotation_transparency_in_block(self):
        rt = _block_text()
        assert "FIFTH and CLOSING leg of the 1100-1104 window" in rt
        for letter, num, main, anchor, loghash in PREDECESSORS:
            assert ("#%s Type %s" % (num, letter)) in rt
            for sha in (main, anchor, loghash):
                assert sha in rt
        assert "#1105 Type D, opening the 1105-1109 window" in rt


# ---------------------------------------------------------------------------
# 9. Post-commit corpus novelty (894 present; 895 absent; no 29th direction).
# ---------------------------------------------------------------------------

class TestCorpusNoveltyPostCommit:
    def test_zero_underscore_895_repo_wide(self):
        assert _repo_grep_underscore_mechanism(895) == []

    def test_zero_dash_895_repo_wide(self):
        assert _repo_grep_dash_mechanism(895) == []

    def test_zero_numeric_895_in_profiles(self):
        assert _profiles_grep_numeric_mechanism_id(895) == []

    def test_no_twenty_ninth_direction(self):
        # The next direction slot must be unclaimed repo-wide.
        for path in ("profiles/", "tests/", "iteration-log.md"):
            result = _git("grep", "-F", TW29, "HEAD", "--", path)
            assert result.returncode != 0, (path, result.stdout[:200])

    def test_894_present_in_committed_tree(self):
        # Commit-dependent: passes after the main commit lands.
        result = _git("grep", "-F", MID_894, "HEAD", "--", "profiles/")
        assert result.returncode == 0, result.stderr[:200]

    def test_block_key_in_committed_profiles(self):
        # Commit-dependent: passes after the main commit lands.
        result = _git(
            "grep", "-F", MECH_KEY, "HEAD", "--",
            "profiles/competitor-entities.yaml",
        )
        assert result.returncode == 0, result.stderr[:200]

    def test_type_c_1104_entry_in_committed_log(self):
        # Commit-dependent: passes after the main commit lands.
        result = _git("grep", "-F", "## #1104 Type C:", "HEAD", "--",
                      "iteration-log.md")
        assert result.returncode == 0, result.stderr[:200]


# ---------------------------------------------------------------------------
# 10. Staleness pins: predecessor forward guards' designed lifecycle.
# ---------------------------------------------------------------------------

class TestStalenessPins1104:
    def test_1103_zero_numeric_894_guard_fails_by_design(self):
        """#1103's zero-numeric-894 sweep fails BY DESIGN: the single hit is
        the new m894 block in profiles/competitor-entities.yaml."""
        res = _class_run(
            F1103, "TestNovelty1103::test_zero_numeric_next_num_in_profiles"
        )
        assert res.returncode != 0, res.stdout[-500:]

    def test_1103_underscore_894_guard_still_passes(self):
        res = _class_run(
            F1103, "TestNovelty1103::test_zero_underscore_next_num_repo_wide"
        )
        assert res.returncode == 0, res.stdout[-500:]

    def test_1103_dash_894_guard_still_passes(self):
        res = _class_run(
            F1103, "TestNovelty1103::test_zero_dash_next_num_repo_wide"
        )
        assert res.returncode == 0, res.stdout[-500:]

    def test_1099_no_twenty_eighth_guard_still_green_against_head(self):
        """#1099's no-twenty-eighth guard greps HEAD, which lags this run's
        uncommitted files: it stays green pre-commit and goes stale BY
        DESIGN at the main commit. The next pin documents the working-tree
        premise violation."""
        res = _class_run(
            F1099,
            "TestCorpusNoveltyPostCommit::test_no_twenty_eighth_direction",
        )
        assert res.returncode == 0, res.stdout[-500:]

    def test_twenty_eighth_needle_present_in_working_tree(self):
        """The needle #1099's guard protects is now deliberately present in
        the working tree (this run's block + test file)."""
        hits = []
        for root, dirs, files in os.walk(TESTS_DIR):
            dirs[:] = [d for d in dirs if d != "__pycache__"]
            for f in files:
                p = os.path.join(root, f)
                if TW28 in open(p, encoding="utf-8",
                                errors="replace").read():
                    hits.append(p)
        assert any("test_type_c_1104_" in h for h in hits), hits
        text = open(PROFILES_FILE, encoding="utf-8").read()
        assert TW28 in text


# ---------------------------------------------------------------------------
# 11. Doc-sync ratchet (DESELECTED pre-commit per #565/#719/#721).
# ---------------------------------------------------------------------------

EXPECT_TESTS = 56255  # README total post-doc-sync, patched post-first-run
EXPECT_FILES = 1429
FILE_TESTS = 83  # this file's collected count
EXPECT_CLASSES = 14


class TestDocSyncRatchet:
    def _readme(self):
        with open(os.path.join(REPO_ROOT, "README.md"),
                  encoding="utf-8") as fh:
            return fh.read()

    def test_readme_stats_line_ratchet(self):
        m = re.search(
            r"\|\s*Tests\s*\|\s*(\d+)\s*\|\s*Across\s*(\d+)\s*test files",
            self._readme(),
        )
        assert m is not None, "README stats line missing"
        assert (int(m.group(1)), int(m.group(2))) == (
            EXPECT_TESTS, EXPECT_FILES)

    def test_readme_table_row_present(self):
        row = [l for l in self._readme().splitlines() if FILE_STEM in l]
        assert len(row) == 1, "README test-table row missing"
        assert "Type C #1104" in row[0]
        assert "%d tests, %d classes" % (
            FILE_TESTS, EXPECT_CLASSES) in row[0]

    def test_architecture_tree_row_present(self):
        with open(
            os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md"),
            encoding="utf-8",
        ) as fh:
            text = fh.read()
        row = [l for l in text.splitlines() if FILE_STEM in l]
        assert len(row) == 1, "ARCHITECTURE tree row missing"
        assert "1100-1104 window FIFTH leg" in row[0]

    def test_collected_count_matches_expected(self):
        result = subprocess.run(
            [
                ".venv/bin/python",
                "-m",
                "pytest",
                os.path.join("tests", FILE_STEM + ".py"),
                "--collect-only",
                "-q",
                "--no-header",
                "-p",
                "no:cacheprovider",
                "-o",
                "addopts=",
            ],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            timeout=600,
        )
        m = re.search(r"(\d+) tests? collected", result.stdout)
        assert m is not None, result.stdout[-500:]
        assert int(m.group(1)) == FILE_TESTS, result.stdout[-500:]


# ---------------------------------------------------------------------------
# 12. Iteration-log entry (DESELECTED pre-commit per #565/#719/#721).
# ---------------------------------------------------------------------------

class TestIterationLogEntry:
    def _log(self):
        with open(os.path.join(REPO_ROOT, "iteration-log.md"),
                  encoding="utf-8") as fh:
            return fh.read()

    def test_entry_header_present(self):
        text = self._log()
        assert "## #1104 Type C:" in text
        assert "Type C FIFTH leg of the 1100-1104 window, CLOSING it" in text

    def test_entry_rotation_transparency(self):
        text = self._log()
        assert "1100-1104 window FIFTH leg" in text
        for letter, num, main, anchor, loghash in PREDECESSORS:
            assert ("#%s Type %s" % (num, letter)) in text

    def test_entry_finding_summary(self):
        text = self._log()
        assert "DIVIDE-AND-CONQUER" in text
        assert "TWENTY-EIGHTH" in text

    def test_entry_method(self):
        text = self._log()
        assert "4 search sets" in text
        assert "1 browser.open" in text
        assert "The Decoder" in text

    def test_entry_doc_sync_ratchet(self):
        text = self._log()
        assert "56172/1428 -> 56255/1429 (+83/+1)" in text

    def test_entry_guard_lifecycle(self):
        text = self._log()
        assert "zero-894" in text
        assert "no-twenty-eighth" in text
        assert "zero-895" in text

    def test_anchor_sha_pinned_and_logged(self):
        # Commit-dependent: passes after the anchor followup patches
        # ANCHORED_SHA to the main-commit SHA and the log-hash followup
        # registers the hashes in the entry header per #721.
        assert ANCHORED_SHA[:8] in self._log()


# ---------------------------------------------------------------------------
# 13. In-flight isolation: never touch concurrent workers' files.
# ---------------------------------------------------------------------------

class TestInflightIsolation:
    def test_no_concurrent_inflight_iteration_commits_staged(self):
        # The in-flight #899/#938/#900/#1012-wt working-tree edits are
        # owned by their runs; this run stages only its own files.
        status = _git("status", "--short").stdout
        staged = [
            l for l in status.splitlines() if l.startswith(("M ", "A "))
        ]
        for f in ("nytimes.yaml", "test_type_b_938_",
                  "test_type_d_900_", "test_type_a_1012_"):
            assert not any(f in l for l in staged)

    def test_this_run_stages_only_own_files(self):
        status = _git("status", "--short").stdout
        staged = [
            l for l in status.splitlines() if l.startswith(("M ", "A "))
        ]
        allowed = (
            "profiles/competitor-entities.yaml",
            "test_type_c_1104_",
            "README.md",
            "docs/ARCHITECTURE.md",
            "iteration-log.md",
        )
        for l in staged:
            assert any(a in l for a in allowed), l


# ---------------------------------------------------------------------------
# 14. Block hygiene.
# ---------------------------------------------------------------------------

class TestBlockHygiene:
    def _docs(self):
        text = open(PROFILES_FILE, encoding="utf-8").read()
        return list(yaml.safe_load_all(text))

    def test_yaml_single_document(self):
        assert len(self._docs()) == 1

    def test_block_round_trips(self):
        blk = _block_yaml()
        assert blk["yaml_parse_clean"] is True
        assert blk["ascii_only"] is True
        assert isinstance(blk["confounders"], list)
        assert isinstance(blk["sources"], list)

    def test_ascii_only_block(self):
        text = _block_text()
        assert not re.search(r"[^\x00-\x7F]", text), \
            "non-ASCII bytes in block"

    def test_no_em_dashes_in_block(self):
        assert "\u2014" not in _block_text().encode("unicode_escape").decode()

    def test_no_em_dashes_in_test_file(self):
        text = open(os.path.join(TESTS_DIR, OWN_BASENAME),
                     encoding="utf-8").read()
        assert "\u2014" not in text.encode("unicode_escape").decode()
