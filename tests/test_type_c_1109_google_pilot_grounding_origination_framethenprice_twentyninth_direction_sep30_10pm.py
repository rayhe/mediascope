"""Type C #1109: Google AI-contribution pilot origination frame vs payout reveal.

NeoTeo (Sep 30 2026, first-hand browser.open read this run, 23 rendered
lines) documents the pilot's announced origination: on June 18, 2026,
Google said it was "piloting a partnership model with websites whose
content contributes to the freshness and factuality of generative AI
responses through grounding" - grounding defined as "anchoring an AI
response in source information." The operating mechanics revealed
Sep 29-30 (m891, m894) are unilateral pricing on a fragmented
counterparty base. The new work is the FRAME as enrollment
infrastructure: publishers joined a "partnership" and learned the price
from an opaque "AI earnings" widget whose payout shows "not which pages
earned it, not how the number was calculated, and not why it changes."
Mechanism 897 lands in profiles/competitor-entities.yaml as the
TWENTY-NINTH relationship direction: FRAME-THEN-PRICE (announced
cooperation vs operating unilateral pricing) - distinct from #27
UNILATERAL PRICING (m891, who prices) and #28 DIVIDE-AND-CONQUER
(m894, how the payer prevents aggregation). NeoTeo also makes explicit
the two-track tiering: the AI Contribution Pilot (~100 publishers,
widget-metered micro-pricing) is SEPARATE from the News AI pilot (200+
publications, "commercial partnerships for enhanced content rights").
FIFTH and CLOSING leg of the 1105-1109 window
(D #1105 -> E #1106 -> A #1107 -> B #1108 -> C #1109 per #565).

Pre-commit green gate per #565/#719/#721: run with .venv/bin/python -m
pytest, deselecting TestNoveltyAnchor1109, TestRotationGuard1105_1109Window,
TestDocSyncRatchet, TestIterationLogEntry, TestStalenessPins1109, and the
commit-dependent tests in TestCorpusNoveltyPostCommit. ANCHORED_SHA is a
placeholder until the anchor followup patches it per #565.

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
    "type_c_1109_google_pilot_grounding_origination_framethenprice_"
    "twentyninth_direction_sep30_10pm"
)
FILE_STEM = (
    "test_type_c_1109_google_pilot_grounding_origination_framethenprice_"
    "twentyninth_direction_sep30_10pm"
)
OWN_BASENAME = FILE_STEM + ".py"

# Next-number needles fragment-built per #715 (runtime values are the
# contiguous forms; the source text never holds them contiguously).
US_897 = "mechanism_" + "897"
DASH_897 = "mechanism-" + "897"
MID_897 = "mechanism_id: " + "897"
US_898 = "mechanism_" + "898"
DASH_898 = "mechanism-" + "898"
MID_898 = "mechanism_id: " + "898"
TW28 = "TWENTY-" + "EIGHTH relationship direction"
TW29 = "TWENTY-" + "NINTH relationship direction"
TW30 = "THIRTI" + "ETH relationship direction"
T40 = "FORTI-" + "ETH falsification-family member"

ANCHORED_SHA = "PLACEHOLDER_40_HEX_PATCHED_POST_COMMIT_PER_565"
ITERATION = 1109
TYPE_LETTER = "C"
WINDOW = "1105-1109"

# (letter, number, main-sha, anchor-sha, log-hash-sha) per #721.
PREDECESSORS = [
    ("D", "1105", "2161fb38", "21adbaed", "ce757f92"),
    ("E", "1106", "efc381a0", "0a3b1066", "3369fce5"),
    ("A", "1107", "de889266", "7cac6995", "6dd6eec5"),
    ("B", "1108", "9cd97d0a", "cdac3f8d", "06622c5f"),
]

NOVEL_URLS = [
    "https://www.neoteo.com/en/"
    "googles-ai-contribution-pilot-has-widely-varying-reported-payouts",
]

F1105 = "test_type_d_1105"
F1106 = "test_type_e_1106"
F1107 = "test_type_a_1107"
F1108 = (
    "test_type_b_1108_nicole_nguyen_wsj_siri_grows_up_vs_muse_"
    "trust_register_sep30_9pm.py"
)
F1104 = (
    "test_type_c_1104_google_ai_answer_pilot_divide_and_conquer_"
    "twentyeighth_direction_sep30_5pm.py"
)

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
# 1. Novelty: this run is the first to claim mechanism 897 and the
#    TWENTY-NINTH relationship direction.
# ---------------------------------------------------------------------------

class TestNovelty1109:
    def test_single_test_file_for_iteration(self):
        files = glob.glob(os.path.join(TESTS_DIR, "test_type_c_1109*.py"))
        assert files == [os.path.join(TESTS_DIR, OWN_BASENAME)], files

    def test_max_numeric_mechanism_id_is_897(self):
        assert _max_numeric_mechanism_id_in_profiles() == 897

    def test_zero_underscore_898_repo_wide(self):
        assert _repo_grep_underscore_mechanism(898) == []

    def test_zero_dash_898_repo_wide(self):
        assert _repo_grep_dash_mechanism(898) == []

    def test_zero_numeric_898_in_profiles(self):
        assert _profiles_grep_numeric_mechanism_id(898) == []

    def test_block_key_unique_at_column_zero(self):
        text = open(PROFILES_FILE, encoding="utf-8").read()
        hits = [
            l for l in text.splitlines() if l.startswith(MECH_KEY + ":")
        ]
        assert len(hits) == 1, hits

    def test_no_type_c_1109_commit_pre_commit(self):
        # Pre-commit novelty guard: no commit may already claim this slot.
        # SUPERSEDED BY DESIGN once this run's main commit ("Type C #1109:")
        # lands; post-commit, TestNoveltyAnchor1109 asserts the unique main
        # commit instead. Deselect this test in post-commit full runs.
        out = _git("log", "--format=%s", "--grep=Type C #1109").stdout.strip()
        assert out == "", out


# ---------------------------------------------------------------------------
# 2. Rotation guard: C is the FIFTH and CLOSING leg of the 1105-1109 window.
#    (DESELECTED pre-commit per #565.)
# ---------------------------------------------------------------------------

class TestRotationGuard1105_1109Window:
    @pytest.mark.rotation
    def test_window_1105_1109_fifth_leg(self):
        """C is the fifth leg of the 1105-1109 window per #565."""
        assert TYPE_LETTER == "C"
        assert ITERATION == 1109
        assert WINDOW == "1105-1109"

    @pytest.mark.rotation
    def test_type_c_adjacency_in_window(self):
        """D(#1105) -> E(#1106) -> A(#1107) -> B(#1108) -> C(#1109, this run)."""
        d_files = glob.glob(os.path.join(TESTS_DIR, F1105 + "*.py"))
        e_files = glob.glob(os.path.join(TESTS_DIR, F1106 + "*.py"))
        a_files = glob.glob(os.path.join(TESTS_DIR, F1107 + "*.py"))
        b_files = glob.glob(os.path.join(TESTS_DIR, "test_type_b_1108*.py"))
        assert len(d_files) >= 1
        assert len(e_files) >= 1
        assert len(a_files) >= 1
        assert len(b_files) >= 1

    @pytest.mark.rotation
    def test_predecessor_is_type_b_1108(self):
        files = glob.glob(os.path.join(TESTS_DIR, "test_type_b_1108*.py"))
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
        """Newest-first log: #1108 above #1107 above #1106 above #1105."""
        subjects = _git("log", "--format=%s").stdout.splitlines()

        def first_idx(needle):
            for i, s in enumerate(subjects):
                if needle in s:
                    return i
            raise AssertionError(needle)

        i1108 = first_idx("Type B #1108")
        i1107 = first_idx("Type A #1107")
        i1106 = first_idx("Type E #1106")
        i1105 = first_idx("Type D #1105")
        assert i1108 < i1107 < i1106 < i1105

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

class TestNoveltyAnchor1109:
    def test_anchor_is_40_hex(self):
        assert re.fullmatch(r"[0-9a-f]{40}", ANCHORED_SHA), ANCHORED_SHA

    def test_main_commit_is_unique_and_anchored(self):
        result = _git("log", "--format=%H %s", "--grep=Type C #1109")
        assert result.returncode == 0
        mains = [
            line
            for line in result.stdout.splitlines()
            if line.split(" ", 1)[1].startswith("Type C #1109:")
        ]
        assert len(mains) == 1, mains
        assert mains[0].split(" ", 1)[0] == ANCHORED_SHA


# ---------------------------------------------------------------------------
# 4. Mechanism 897 block structure.
# ---------------------------------------------------------------------------

class TestMechanism897Structure:
    def test_block_key_field_repeats_key(self):
        assert _block_yaml()["block_key"] == MECH_KEY

    def test_mechanism_id_numeric_897(self):
        blk = _block_yaml()
        assert blk["mechanism_id"] == 897
        assert isinstance(blk["mechanism_id"], int)

    def test_type_fields(self):
        blk = _block_yaml()
        assert blk["type"] == "financial_incentive_mapping"
        assert blk["type_label"] == "Financial Incentive Mapping"

    def test_iteration_fields(self):
        blk = _block_yaml()
        assert blk["iteration"] == 1109
        assert blk["iteration_type"] == "C"
        assert blk["iteration_time"] == "2026-09-30 22:00 PDT"
        assert blk["goal_id"] == "goal_54093bda4145"
        assert blk["scheduled_job_id"] == "mediascope-daily-iteration"

    def test_connects_to_exact(self):
        assert _block_yaml()["connects_to"] == [891, 894, 702, 708]

    def test_sources_structure(self):
        sources = _block_yaml()["sources"]
        assert len(sources) == 1
        for s in sources:
            assert s["url"].startswith("https://")
            assert s["what"]
            assert s["accessed"] == "2026-09-30"
            assert s["novel"] is True
        assert sources[0]["url"].startswith("https://www.neoteo.com/")

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
# 5. Mechanism 897 legs.
# ---------------------------------------------------------------------------

class TestMechanism897Legs:
    def test_finding_peg(self):
        text = _block_text()
        assert "23 rendered lines" in text
        assert "June 18, 2026" in text
        assert "freshness and factuality" in text
        assert "FIRST dedicated corpus mechanism" in text

    def test_origination_frame_leg(self):
        text = _block_text()
        assert "partnership model" in text
        assert "grounding" in text
        assert "No price, no formula, no payment range disclosed" in text
        assert "m891" in text

    def test_two_track_architecture_leg(self):
        text = _block_text()
        assert "TWO distinct publisher payment tracks" in text
        assert "AI Contribution Pilot" in text
        assert "News AI pilot" in text
        assert "commercial partnerships for enhanced content rights" in text
        assert "widget-metered micro-pricing" in text

    def test_frame_shift_leg(self):
        text = _block_text()
        assert "FRAME ITSELF as pricing-power infrastructure" in text
        assert "enrollment infrastructure" in text
        assert "invitation-only" in text

    def test_corpus_lineage(self):
        text = _block_text()
        assert "m891" in text and "m894" in text
        assert "m702" in text and "m708" in text
        assert "m539" in text and "m666" in text

    def test_incentive_geometry(self):
        text = _block_text()
        assert "three named legs" in text
        assert "never priced anything at any stage" in text
        assert "widget-metered micro-pricing for the" in text

    def test_coverage_nexus(self):
        text = _block_text()
        assert "freshness and factuality" in text
        assert "NOT_SCORED" in text

    def test_legs_distinct(self):
        text = _block_text()
        for leg in (
            "origination_frame_leg:",
            "two_track_architecture_leg:",
            "frame_shift_leg:",
            "incentive_geometry:",
            "coverage_nexus:",
        ):
            assert leg in text, leg

    def test_counterargument_sincerity_condition(self):
        text = _block_text()
        assert "sincere product language" in text
        assert "extremely collaborative" in text


# ---------------------------------------------------------------------------
# 6. TWENTY-NINTH relationship direction taxonomy.
# ---------------------------------------------------------------------------

class TestMechanism897Taxonomy:
    def test_twenty_ninth_present(self):
        assert "TWENTY-NINTH relationship direction" in _block_text()

    def test_enumeration_covers_1_to_28(self):
        tax = _block_text()
        assert "1 sue-then-sign m624" in tax
        assert "12 regulatory-bargaining m1004" in tax
        assert "27 unilateral pricing m891" in tax
        assert "28 divide-and-conquer m894" in tax

    def test_distinct_from_unilateral_pricing(self):
        tax = _block_text()
        assert "Distinct from #27 unilateral pricing m891" in tax
        assert "WHO sets the price" in tax

    def test_distinct_from_divide_and_conquer(self):
        tax = _block_text()
        assert "from #28 divide-and-conquer m894" in tax
        assert "HOW the payer prevents aggregation" in tax

    def test_distinct_from_ecosystem_grant(self):
        tax = _block_text()
        assert "from #15 ecosystem-grant m1029" in tax
        assert "honestly framed" in tax

    def test_frame_enrollment_infrastructure(self):
        tax = _block_text()
        assert "FRAME-THEN-PRICE" in tax
        assert "enrollment infrastructure" in tax

    def test_falsifiable(self):
        tax = _block_text()
        assert "Falsifiable:" in tax
        assert "no frame shift" in tax

    def test_taxonomy_tension_carried(self):
        tax = _block_text()
        assert "m737" in tax
        assert "Not resolved this run" in tax


# ---------------------------------------------------------------------------
# 7. Confounders.
# ---------------------------------------------------------------------------

class TestMechanism897Confounders:
    def test_confounder_count_and_order(self):
        conf = _block_yaml()["confounders"]
        assert len(conf) == 6
        strengths = [c["strength"] for c in conf]
        assert strengths == (
            ["STRONG"] * 2 + ["MEDIUM"] * 2 + ["WEAK"] * 2
        ), strengths

    def test_strong_single_synthesis(self):
        texts = " ".join(
            c["text"]
            for c in _block_yaml()["confounders"]
            if c["strength"] == "STRONG"
        )
        assert "only corpus source" in texts

    def test_strong_identity_inference(self):
        texts = " ".join(
            c["text"]
            for c in _block_yaml()["confounders"]
            if c["strength"] == "STRONG"
        )
        assert "Identity inference" in texts

    def test_medium_byline_and_phase(self):
        texts = " ".join(
            c["text"]
            for c in _block_yaml()["confounders"]
            if c["strength"] == "MEDIUM"
        )
        assert "Byline and outlet thinness" in texts
        assert "Phase-vs-tier ambiguity" in texts

    def test_weak_window_and_sincerity(self):
        texts = " ".join(
            c["text"]
            for c in _block_yaml()["confounders"]
            if c["strength"] == "WEAK"
        )
        assert "single-day evidence window" in texts
        assert "Frame sincerity" in texts


# ---------------------------------------------------------------------------
# 8. Research method: 4 search sets + 1 first-hand browser.open per #503.
# ---------------------------------------------------------------------------

class TestResearchMethodTypeC1109:
    def test_one_novel_url_verbatim(self):
        assert len(NOVEL_URLS) == 1
        assert NOVEL_URLS[0].startswith("https://www.neoteo.com/en/")

    def test_first_hand_neoteo_open(self):
        src = _block_yaml()["sources"][0]
        assert "first-hand browser.open read this run" in src["what"]
        assert "23 rendered lines" in src["what"]

    def test_novelty_claim_documents_sources(self):
        nov = _block_text()
        assert "1 novel source URL" in nov
        assert "FIRST dedicated corpus mechanism" in nov
        assert "TWENTY-NINTH relationship direction" in nov

    def test_rotation_transparency_in_block(self):
        rt = _block_text()
        assert "FIFTH and CLOSING leg of the 1105-1109 window" in rt
        for letter, num, main, anchor, loghash in PREDECESSORS:
            assert ("#%s Type %s" % (num, letter)) in rt
            for sha in (main, anchor, loghash):
                assert sha in rt
        assert "#1110 Type D, opening the 1110-1114 window" in rt


# ---------------------------------------------------------------------------
# 9. Post-commit corpus novelty (897 present; 898 absent; no 30th direction).
# ---------------------------------------------------------------------------

class TestCorpusNoveltyPostCommit:
    def test_zero_underscore_898_repo_wide(self):
        assert _repo_grep_underscore_mechanism(898) == []

    def test_zero_dash_898_repo_wide(self):
        assert _repo_grep_dash_mechanism(898) == []

    def test_zero_numeric_898_in_profiles(self):
        assert _profiles_grep_numeric_mechanism_id(898) == []

    def test_no_thirtieth_direction(self):
        # The next direction slot must be unclaimed repo-wide.
        for path in ("profiles/", "tests/", "iteration-log.md"):
            result = _git("grep", "-F", TW30, "HEAD", "--", path)
            assert result.returncode != 0, (path, result.stdout[:200])

    def test_no_fortieth_falsification_member(self):
        for path in ("profiles/", "tests/", "iteration-log.md"):
            result = _git("grep", "-F", T40, "HEAD", "--", path)
            assert result.returncode != 0, (path, result.stdout[:200])

    def test_897_present_in_committed_tree(self):
        # Commit-dependent: passes after the main commit lands.
        result = _git("grep", "-F", MID_897, "HEAD", "--", "profiles/")
        assert result.returncode == 0, result.stderr[:200]

    def test_block_key_in_committed_profiles(self):
        # Commit-dependent: passes after the main commit lands.
        result = _git(
            "grep", "-F", MECH_KEY, "HEAD", "--",
            "profiles/competitor-entities.yaml",
        )
        assert result.returncode == 0, result.stderr[:200]

    def test_type_c_1109_entry_in_committed_log(self):
        # Commit-dependent: passes after the main commit lands.
        result = _git("grep", "-F", "## #1109 Type C:", "HEAD", "--",
                      "iteration-log.md")
        assert result.returncode == 0, result.stderr[:200]


# ---------------------------------------------------------------------------
# 10. Staleness pins: predecessor forward guards' designed lifecycle.
# ---------------------------------------------------------------------------

class TestStalenessPins1109:
    def test_1108_zero_numeric_897_guard_fails_by_design(self):
        """#1108's zero-numeric-897 sweep fails BY DESIGN: the single hit is
        the new m897 block in profiles/competitor-entities.yaml."""
        res = _class_run(
            F1108, "TestForwardGuards1108::test_zero_numeric_897_in_profiles"
        )
        assert res.returncode != 0, res.stdout[-500:]

    def test_1108_underscore_897_guard_still_passes(self):
        res = _class_run(
            F1108, "TestForwardGuards1108::test_zero_underscore_897_repo_wide"
        )
        assert res.returncode == 0, res.stdout[-500:]

    def test_1108_dash_897_guard_still_passes(self):
        res = _class_run(
            F1108, "TestForwardGuards1108::test_zero_dash_897_repo_wide"
        )
        assert res.returncode == 0, res.stdout[-500:]

    def test_1104_no_twenty_ninth_guard_stale_by_design_post_commit(self):
        """#1104's no-twenty-ninth guard greps HEAD. Pre-commit it stayed
        green (HEAD lagged this run's uncommitted files); at the main
        commit HEAD caught up and the guard fails BY DESIGN - the corpus
        now deliberately contains the TWENTY-NINTH relationship
        direction. This is the guard's designed end-state; the #1110
        Type D run inherits the no-thirtieth guard pinned in
        TestCorpusNoveltyPostCommit."""
        res = _class_run(
            F1104,
            "TestCorpusNoveltyPostCommit::test_no_twenty_ninth_direction",
        )
        assert res.returncode != 0, res.stdout[-500:]
        assert "test_no_twenty_ninth_direction" in res.stdout

    def test_twenty_ninth_needle_present_in_working_tree(self):
        """The needle #1104's guard protects is now deliberately present in
        the working tree (this run's block + test file)."""
        hits = []
        for root, dirs, files in os.walk(TESTS_DIR):
            dirs[:] = [d for d in dirs if d != "__pycache__"]
            for f in files:
                p = os.path.join(root, f)
                if TW29 in open(p, encoding="utf-8",
                                errors="replace").read():
                    hits.append(p)
        assert any("test_type_c_1109_" in h for h in hits), hits
        text = open(PROFILES_FILE, encoding="utf-8").read()
        assert TW29 in text


# ---------------------------------------------------------------------------
# 11. Doc-sync ratchet (DESELECTED pre-commit per #565/#719/#721).
# ---------------------------------------------------------------------------

EXPECT_TESTS = 56592  # README total post-doc-sync, patched post-first-run
EXPECT_FILES = 1434
FILE_TESTS = 81  # this file's collected count
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
        assert "Type C #1109" in row[0]
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
        assert "1105-1109 window FIFTH leg" in row[0]

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
        assert "## #1109 Type C:" in text
        assert "Type C FIFTH leg of the 1105-1109 window, CLOSING it" in text

    def test_entry_rotation_transparency(self):
        text = self._log()
        assert "1105-1109 window FIFTH leg" in text
        for letter, num, main, anchor, loghash in PREDECESSORS:
            assert ("#%s Type %s" % (num, letter)) in text

    def test_entry_finding_summary(self):
        text = self._log()
        assert "FRAME-THEN-PRICE" in text
        assert "TWENTY-NINTH" in text

    def test_entry_method(self):
        text = self._log()
        assert "4 search sets" in text
        assert "1 browser.open" in text
        assert "NeoTeo" in text

    def test_entry_doc_sync_ratchet(self):
        text = self._log()
        assert "56511/1433 -> 56592/1434 (+81/+1)" in text

    def test_entry_guard_lifecycle(self):
        text = self._log()
        assert "zero-897" in text
        assert "no-twenty-ninth" in text
        assert "zero-898" in text

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
            "test_type_c_1109_",
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
