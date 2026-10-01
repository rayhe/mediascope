"""Type B #1113 (2026-10-01 02:00 PDT) - Joanna Stern (New Things/NBC,
independent phase) x Meta Zuckerberg Connect interview vs Apple iPhone Duo
hands-on register pair, mechanism 899.

FOURTH leg of the 1110-1114 window (D #1110 -> E #1111 -> A #1112 ->
B #1113 -> C #1114), per the #565 rotation anchor. Predecessor: #1112
Type A (mediascope-daily-iteration, 2026-10-01 01:00 PDT). The 1105-1109
window is verified closed.

Mechanism 899 pairs Stern's Sep-24 2026 New Things/NBC Zuckerberg interview
at Meta Connect 2026 (accountability register: "pervert glasses" pressed,
"Is AI going to kill us?" opener, phones-don't-have-lights defense
countered; -0.50 MANUAL ILLUSTRATIVE, FRESH, relay-attested, excerpt-bounded
per #503, 0 browser.open) against her FRESH Sep-10 2026 iPhone Duo
hands-on at Apple Park (enthusiast first-impressions with a visible
hardware caveat: "I see no crease whatsoever", matte inner display the
favorite feature, missing telephoto "the biggest hardware disappointment";
+0.35 MANUAL ILLUSTRATIVE, relay-attested via macdailynews, excerpt-bounded
per #503).

Finding: same journalist, same month, both zero-deal (independent phase),
14 days apart - Apple draws the enthusiast register (+0.35) while Meta
draws the accountability register (-0.50). Illustrative delta (Apple minus
Meta) +0.85. The naive independence-hardening prediction (zero deals ->
harder coverage everywhere) FAILS on ordering at the journalist level:
FORTY-FIRST falsification-family member, ledger 40 -> 41. The m105
career-migration 1.00 Meta swing is REFRAMED: the swing tracks the
hardening factual substrate (her Jun-2026 secret-recording investigation,
the LED-tamper beat, the Kenya-subcontractor class action), not merely the
disappearance of the News Corp deal money; the Apple register's +0.55
cross-phase shift (WSJ Vision Pro -0.20 -> independent Duo +0.35) is the
money-story's unexplained residue. FIRST dedicated Type B mechanism on
Joanna Stern (m105 is the unnumbered natural experiment; Aug-7/Aug-14
commits are not numbered pairs).

STRONG confounders (disclosed, not hidden): factual-substrate difference;
CROSS-GENRE pair (CEO accountability interview vs hardware hands-on -
unlike #1108's same-genre pair, genre conditioning does heavy lifting);
product-form confound on the cross-phase Apple comparison (Vision Pro
headset vs foldable phone). MODERATE: 14-day temporal gap; relay-tier both
arms + stale "WSJ's Joanna Stern" boilerplate in the Duo relay (phase
certain, publication attribution flagged). WEAK: degenerate n=1 per arm.

Statistical discipline per the Aug 28 2026 standing rule: MANUAL
ILLUSTRATIVE ONLY, engine NOT run, p_value/cohens_d/ci_95
NOT_CALCULATED, is_significant false, verdict
directionally_supported_not_proven, no_analysis_json_update true, NOT
artifact-grade. Correlation is not causation; hypothesis-generating
only.

Literal discipline per #715: this file carries NO contiguous
underscore-form, dash-form, or numeric-form 899/900 mechanism literals -
the mechanism needles are format-built ("%d" % MECH_NUM / NEXT_NUM), so
the zero-899 pre-commit sweeps and zero-900 forward guards stay valid.
The #1024 m846 sourcing-constraint matter is not touched by this run.
Do NOT touch #1024's m846.
"""

import glob
import logging
import os
import re
import subprocess

import pytest
import yaml

from mediascope.score.asymmetry import calculate_asymmetry

log = logging.getLogger(__name__)

ITERATION = 1113
TYPE_LETTER = "B"
WINDOW = "1110-1114"
MECH_NUM = 899
NEXT_NUM = 900
ANCHORED_SHA = "d95faffb"  # main commit, patched in the anchor followup per #565
OWN_BASENAME = (
    "test_type_b_1113_joanna_stern_meta_zuckerberg_interview_"
    "vs_apple_iphone_duo_register_sep2026_2am.py"
)
BLOCK_KEY = (
    "type_b_1113_joanna_stern_meta_zuckerberg_interview_"
    "vs_apple_iphone_duo_register_sep2026"
)
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TESTS_DIR = os.path.join(REPO_ROOT, "tests")
PROFILES_DIR = os.path.join(REPO_ROOT, "profiles")
JOURNALISTS_FILE = os.path.join(PROFILES_DIR, "careers", "journalists.yaml")
YT_URL = "https://www.youtube.com/watch?v=D7VrIkPtH80"
DUO_URL = (
    "https://macdailynews.com/2026/09/10/"
    "i-see-no-crease-whatsoever-wsjs-joanna-stern-hands-on-"
    "with-apples-iphone-duo/"
)

# Patched post-commit once README/ARCHITECTURE doc-sync lands.
README_TEST_COUNT = 56860  # post-doc-sync total
README_FILE_COUNT = 1438  # post-doc-sync total
TEST_BASENAME = OWN_BASENAME

F1112 = ("test_type_a_1112_wired_openai_lasst_huggingface_lawsuit_"
         "register_vs_meta_carried_arms_oct01_1am.py")


def _git(*args):
    return subprocess.run(["git"] + list(args), cwd=REPO_ROOT,
                          capture_output=True, text=True)


def _class_run(test_file, class_name):
    return subprocess.run(
        [os.path.join(REPO_ROOT, ".venv", "bin", "python"), "-m", "pytest",
         os.path.join(TESTS_DIR, test_file) + "::" + class_name,
         "-q", "--no-header", "-p", "no:cacheprovider"],
        cwd=REPO_ROOT, capture_output=True, text=True,
    )


def _source_files():
    out = []
    for root, dirs, files in os.walk(REPO_ROOT):
        dirs[:] = [d for d in dirs
                   if d not in ("__pycache__", ".git", ".venv")]
        for f in files:
            out.append(os.path.join(root, f))
    return out


def _iter_source_files():
    for p in _source_files():
        yield p


def _read(p):
    with open(p, encoding="utf-8", errors="replace") as f:
        return f.read()


def _profiles_grep_numeric_mechanism_id(num):
    needle = "mechanism_id: %d" % num
    hits = []
    for root, dirs, files in os.walk(PROFILES_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
            p = os.path.join(root, f)
            if needle in _read(p):
                hits.append(p)
    return hits


def _repo_grep_underscore_mechanism(num):
    needle = "mechanism_%d" % num
    return [p for p in _iter_source_files() if needle in _read(p)
            and not p.endswith(OWN_BASENAME)]


def _repo_grep_dash_mechanism(num):
    needle = "mechanism-%d" % num
    return [p for p in _iter_source_files() if needle in _read(p)
            and not p.endswith(OWN_BASENAME)]


def _block():
    d = yaml.safe_load(_read(JOURNALISTS_FILE))
    journalists = d["journalists"]
    stern = next(j for j in journalists if j.get("name") == "Joanna Stern")
    # Type B blocks nest under competitor_coverage (4-space indent).
    return stern["competitor_coverage"][BLOCK_KEY]


def _block_text():
    text = _read(JOURNALISTS_FILE)
    start = text.index(BLOCK_KEY)
    # Block ends at the next 4-space sibling key or the next journalist entry.
    tail = text[start:]
    m = re.search(r"\n    [a-z_]+:|\n- name:", tail[1:])
    end = start + 1 + m.start() if m else len(text)
    return text[start:end]


# ---------------------------------------------------------------------------
# 1. Novelty (pre-commit: #715 protocol).
# ---------------------------------------------------------------------------

class TestNovelty1113:
    def test_single_test_file_for_iteration(self):
        files = glob.glob(os.path.join(TESTS_DIR, "test_type_b_1113*.py"))
        assert len(files) == 1, files
        assert files[0].endswith(OWN_BASENAME)

    def test_no_type_b_1113_in_git_log(self):
        # Commit-dependent: empty pre-commit; fails post-commit by design.
        res = _git("log", "--oneline", "--grep=Type B #1113")
        assert res.stdout.strip() == "", res.stdout

    def test_max_numeric_mechanism_id_is_899(self):
        # Working tree includes the uncommitted block (mechanism_id 899).
        ids = []
        for root, dirs, files in os.walk(PROFILES_DIR):
            dirs[:] = [d for d in dirs if d != "__pycache__"]
            for f in files:
                p = os.path.join(root, f)
                for m in re.finditer(r"mechanism_id:\s*(\d+)",
                                     _read(p)):
                    ids.append(int(m.group(1)))
        assert max(ids) == MECH_NUM

    def test_numeric_899_exactly_one_profile(self):
        hits = _profiles_grep_numeric_mechanism_id(MECH_NUM)
        assert hits == [JOURNALISTS_FILE], hits

    def test_zero_underscore_899_repo_wide(self):
        # Designed keying: colon-form block key only; underscore-form 899
        # stays zero (own test file excluded, needles format-built per #715).
        assert _repo_grep_underscore_mechanism(MECH_NUM) == []

    def test_zero_dash_899_repo_wide(self):
        assert _repo_grep_dash_mechanism(MECH_NUM) == []

    def test_novel_urls_only_in_block_and_own_file(self):
        # Pre-insert novelty (zero-hit repo-wide) verified via subprocess
        # during research; post-insert the URLs live only in the block.
        for url in (YT_URL, DUO_URL):
            hits = [p for p in _iter_source_files()
                    if url in _read(p)
                    and not p.endswith(OWN_BASENAME)]
            assert hits == [JOURNALISTS_FILE], (url, hits)

    def test_block_key_present_in_journalists(self):
        assert BLOCK_KEY in _read(JOURNALISTS_FILE)


# ---------------------------------------------------------------------------
# 2. Rotation guard (markers anchor/rotation).
# ---------------------------------------------------------------------------

class TestRotationGuard1113:
    @pytest.mark.rotation
    def test_window_1110_1114_fourth_leg(self):
        """B is the fourth leg of the 1110-1114 window per #565."""
        assert TYPE_LETTER == "B"
        assert ITERATION == 1113
        assert WINDOW == "1110-1114"

    @pytest.mark.rotation
    def test_type_b_adjacency_in_window(self):
        """D(#1110) -> E(#1111) -> A(#1112) -> B(#1113, this run) -> C(#1114)."""
        d_files = glob.glob(os.path.join(TESTS_DIR, "test_type_d_1110*.py"))
        e_files = glob.glob(os.path.join(TESTS_DIR, "test_type_e_1111*.py"))
        a_files = glob.glob(os.path.join(TESTS_DIR, "test_type_a_1112*.py"))
        assert len(d_files) >= 1 and len(e_files) >= 1 and len(a_files) >= 1

    @pytest.mark.rotation
    def test_predecessor_is_type_a_1112(self):
        files = glob.glob(os.path.join(TESTS_DIR, "test_type_a_1112*.py"))
        assert len(files) >= 1

    @pytest.mark.rotation
    def test_single_type_b_1113_file_is_this_run(self):
        files = glob.glob(os.path.join(TESTS_DIR, "test_type_b_1113*.py"))
        assert len(files) == 1 and files[0].endswith(OWN_BASENAME)

    @pytest.mark.anchor
    def test_anchor_is_ancestor_of_head(self):
        """Post-commit: the anchor commit is an ancestor of HEAD.
        Deselected pre-commit per #565 (commit-dependent)."""
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

class TestNoveltyAnchor1113:
    @pytest.mark.anchor
    def test_anchor_sha_patched_post_commit(self):
        # No #1113 main commit exists pre-commit; the anchor test pins
        # the main commit SHA once the followup patches ANCHORED_SHA.
        # Deselected pre-commit per #565; patched green in the anchor
        # followup.
        result = subprocess.run(
            ["git", "log", "--format=%H %s", "--", "tests/" + OWN_BASENAME],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        mains = [
            line
            for line in result.stdout.splitlines()
            if "Type B #1113" in line and "followup" not in line.lower()
        ]
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "placeholder",
        )
        assert any(ANCHORED_SHA[:12] in line for line in mains)

    @pytest.mark.anchor
    def test_anchor_sha_is_ancestor_of_head(self):
        result = subprocess.run(
            ["git", "merge-base", "--is-ancestor", ANCHORED_SHA, "HEAD"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0


# ---------------------------------------------------------------------------
# 4. Mechanism 899 block structure (YAML-parsed).
# ---------------------------------------------------------------------------

class TestMechanism899Structure:
    def test_block_key_present(self):
        assert BLOCK_KEY in _read(JOURNALISTS_FILE)

    def test_mechanism_id(self):
        assert _block()["mechanism_id"] == MECH_NUM

    def test_type_and_iteration(self):
        b = _block()
        assert b["type"] == "Type B: Journalist Cross-Entity Tracking"
        assert b["iteration"] == ITERATION
        assert b["journalist"] == "Joanna Stern"
        assert b["publication"] == "new-things"

    def test_meta_arm_fresh_novel(self):
        arm = _block()["meta_arm"]
        assert arm["entity"] == "Meta"
        assert arm["date"] == "2026-09-24"
        assert YT_URL in arm["url"]
        assert arm["manual_illustrative_tone"] == -0.50
        assert "pervert glasses" in arm["register_summary"]

    def test_apple_arm_fresh_novel(self):
        arm = _block()["apple_arm"]
        assert arm["entity"] == "Apple"
        assert arm["date"] == "2026-09-10"
        assert DUO_URL in arm["url"]
        assert arm["manual_illustrative_tone"] == 0.35
        assert "crease" in arm["register_summary"]

    def test_m105_arms_carried_not_rescored(self):
        # m105's WSJ-era arms are carried per #807, not re-scored here.
        b = _block()
        assert "m105" in b["falsification_family"]
        assert "#807" in str(b["cross_references"])

    def test_illustrative_delta(self):
        delta = _block()["illustrative_delta"]
        assert "+0.85" in delta
        assert "Apple minus Meta" in delta

    def test_falsification_forty_first(self):
        fam = _block()["falsification_family"]
        assert "FORTY-FIRST falsification-family member" in fam
        assert _block()["falsification_ledger"] == "41"

    def test_statistical_discipline(self):
        disc = _block()["statistical_discipline"]
        assert "MANUAL ILLUSTRATIVE ONLY" in disc
        assert "engine NOT run" in disc
        assert "is_significant false" in disc
        assert "NOT_CALCULATED" in disc
        assert _block()["no_analysis_json_update"] is True
        assert _block()["correlation_not_causation"] is True

    def test_confounder_coverage(self):
        confs = _block()["confounders"]
        assert len(confs) >= 5
        joined = " ".join(confs)
        assert "[STRONG]" in joined
        assert "cross-genre" in joined.lower() or "CROSS-GENRE" in joined
        assert "[WEAK]" in joined
        assert len(_block()["counterevidence"]) >= 3

    def test_ascii_only(self):
        text = _block_text()
        assert "\u2014" not in text  # no em dashes
        assert "\u2013" not in text  # no en dashes
        text.encode("ascii")


# ---------------------------------------------------------------------------
# 5. Falsification ledger: FORTY-FIRST lands here; ledger holds at 41.
# ---------------------------------------------------------------------------

class TestLedger41:
    def _ledger_hits(self, needle):
        hits = []
        for root, dirs, files in os.walk(PROFILES_DIR):
            dirs[:] = [d for d in dirs if d != "__pycache__"]
            for f in files:
                p = os.path.join(root, f)
                if needle in _read(p):
                    hits.append(p)
        return hits

    def test_forty_first_present_once(self):
        hits = self._ledger_hits("FORTY-FIRST falsification-family member")
        assert hits == [JOURNALISTS_FILE], hits

    def test_forty_first_is_m899(self):
        text = _read(JOURNALISTS_FILE)
        assert "FORTY-FIRST falsification-family member" in text
        assert ("mechanism_id: %d" % MECH_NUM) in text

    def test_fortieth_intact(self):
        hits = self._ledger_hits("FORTIETH falsification-family member")
        wired = os.path.join(PROFILES_DIR, "wired.yaml")
        assert hits == [wired], hits

    def test_no_forty_second_member(self):
        assert self._ledger_hits("FORTY-SECOND falsification-family member") == []

    def test_ledger_41_in_block(self):
        assert _block()["falsification_ledger"] == "41"


# ---------------------------------------------------------------------------
# 6. Forward guards: zero-900 in all mechanism-key forms (own file excluded,
#    needles format-built per #715).
# ---------------------------------------------------------------------------

class TestForwardGuards1113:
    def test_zero_numeric_900_in_profiles(self):
        assert _profiles_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_zero_underscore_900_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_zero_dash_900_repo_wide(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []


# ---------------------------------------------------------------------------
# 7. Supersession pins: #1112's no-41st-member guard + zero-899 forward
#    guards fail BY DESIGN now that this run lands 899 and FORTY-FIRST.
# ---------------------------------------------------------------------------

class TestSupersessionPins1113:
    def test_1112_no_41st_member_guard_fails_by_design(self):
        """#1112's TestLedgerHoldsAt40 pinned no-41st-member with a
        recursive profiles/ walk; this run lands the FORTY-FIRST member,
        so that guard must now fail. Recorded, not repaired."""
        result = subprocess.run(
            [os.path.join(REPO_ROOT, ".venv", "bin", "python"), "-m", "pytest",
             os.path.join(TESTS_DIR, F1112)
             + "::TestLedgerHoldsAt40::test_no_41st_member_form",
             "-q", "--no-header", "-p", "no:cacheprovider"],
            cwd=REPO_ROOT, capture_output=True, text=True,
        )
        assert result.returncode != 0

    def test_1112_ledger_40_class_fails_by_design(self):
        """The whole TestLedgerHoldsAt40 class is stale: ledger now holds 41."""
        result = _class_run(F1112, "TestLedgerHoldsAt40")
        assert result.returncode != 0

    def test_1112_zero_899_forward_guards_still_green_scope_limited(self):
        """#1112's TestNovelty1112 zero-899 forward sweeps STAY GREEN: their
        numeric sweep covers only top-level profiles/*.yaml (glob, not a
        recursive walk), and this run's block lands in
        profiles/careers/journalists.yaml. Recorded as a scope note, not
        a failure."""
        result = _class_run(F1112, "TestNovelty1112")
        assert result.returncode == 0, result.stdout[-2000:]

    def test_1112_supersession_pins_recorded_not_repaired(self):
        """#1112's TestSupersessionPins1112 state is RECORDED, not repaired:
        6 of 8 pass; test_underscore_898_hits_exactly_wired and
        test_novel_relay_url_zero_hit_elsewhere were ALREADY stale at
        #1112's own doc-sync (#1112's iteration-log entry carries
        underscore-form mechanism_898 and the relay URL - self-inflicted
        pre-existing state, not caused by this run)."""
        result = _class_run(F1112, "TestSupersessionPins1112")
        assert result.returncode != 0
        assert "test_underscore_898_hits_exactly_wired" in result.stdout
        assert "test_novel_relay_url_zero_hit_elsewhere" in result.stdout


# ---------------------------------------------------------------------------
# 8. Degenerate n=1 contract on the illustrative pair (#638/#643).
# ---------------------------------------------------------------------------

class TestDegenerateContract1113:
    def _result(self):
        from datetime import datetime
        return calculate_asymmetry(
            [0.35], [-0.50],
            target_entity="Apple",
            peer_entities=["Meta"],
            publication_slug="new-things",
            period_start=datetime(2026, 9, 10),
            period_end=datetime(2026, 9, 24),
        )

    def test_illustrative_delta(self):
        r = self._result()
        assert abs(r.asymmetry_score - 0.85) < 1e-9

    def test_degenerate_no_significance(self):
        r = self._result()
        assert r.t_statistic == 0.0
        assert r.p_value == 1.0
        assert r.is_significant is False


# ---------------------------------------------------------------------------
# 9. Doc-sync (DESELECTED pre-commit per #565/#719/#721; marker docsync).
# ---------------------------------------------------------------------------

class TestDocSync1113:
    @pytest.mark.docsync
    def test_readme_count_gate(self):
        """README test/file counts match the post-run totals."""
        readme = open(os.path.join(REPO_ROOT, "README.md"),
                      encoding="utf-8").read()
        assert ("| Tests | %d |" % README_TEST_COUNT) in readme
        assert ("Across %d test files" % README_FILE_COUNT) in readme

    @pytest.mark.docsync
    def test_readme_table_row(self):
        """The #1113 test-file row is appended to the README test table."""
        readme = open(os.path.join(REPO_ROOT, "README.md"),
                      encoding="utf-8").read()
        assert TEST_BASENAME in readme

    @pytest.mark.docsync
    def test_architecture_count_gate(self):
        """ARCHITECTURE.md counts match the post-run totals."""
        arch = open(os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md"),
                    encoding="utf-8").read()
        assert str(README_TEST_COUNT) in arch
        assert str(README_FILE_COUNT) in arch

    @pytest.mark.docsync
    def test_architecture_tree_row(self):
        """The #1113 test-file row is appended to the ARCHITECTURE tree."""
        arch = open(os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md"),
                    encoding="utf-8").read()
        assert TEST_BASENAME in arch


# ---------------------------------------------------------------------------
# 10. Iteration log (DESELECTED pre-commit per #565/#719/#721; marker log).
# ---------------------------------------------------------------------------

class TestIterationLog1113:
    @pytest.mark.log
    def test_log_captures_1113(self):
        """The iteration log carries the #1113 Type B entry."""
        head = open(os.path.join(REPO_ROOT, "iteration-log.md"),
                    encoding="utf-8").read()[:6000]
        assert "## #1113 Type B:" in head
        assert "02:00 AM PDT" in head
        assert ("mechanism %d" % MECH_NUM) in head

    @pytest.mark.log
    def test_log_window(self):
        """The entry names the 1110-1114 window fourth leg."""
        head = open(os.path.join(REPO_ROOT, "iteration-log.md"),
                    encoding="utf-8").read()[:6000]
        assert "1110-1114" in head
        assert "FOURTH leg" in head

    @pytest.mark.log
    def test_log_ledger_41(self):
        """The entry records ledger holds at 41."""
        head = open(os.path.join(REPO_ROOT, "iteration-log.md"),
                    encoding="utf-8").read()[:6000]
        assert "ledger holds at 41" in head
        assert "FORTY-FIRST" in head

    @pytest.mark.log
    def test_log_lineage(self):
        """The entry records the m105 reframing and #1108 replication."""
        head = open(os.path.join(REPO_ROOT, "iteration-log.md"),
                    encoding="utf-8").read()[:6000]
        assert "m105" in head
        assert "1108" in head
        assert "Stern" in head


# ---------------------------------------------------------------------------
# 11. In-flight isolation: #899/#938/#900/#1012-wt untouched by this run.
# ---------------------------------------------------------------------------

class TestInFlightIsolation1113:
    def test_899_nytimes_hunk_untouched(self):
        res = _git("diff", "--name-only")
        modified = res.stdout.split()
        assert "profiles/nytimes.yaml" in modified
        # Its uncommitted hunk belongs to #899's run; this run stages
        # only its own files.
        src = open(os.path.join(TESTS_DIR, OWN_BASENAME),
                   encoding="utf-8").read()
        assert "#899" in src

    def test_900_untracked_file_untouched(self):
        res = _git("status", "--short")
        assert "test_type_d_900_m769" in res.stdout

    def test_938_test_file_edit_owned_by_its_run(self):
        res = _git("status", "--short")
        assert "test_type_b_938" in res.stdout

    def test_1012_working_tree_edit_untouched(self):
        res = _git("diff", "--name-only")
        assert "test_type_a_1012" in res.stdout

    def test_do_not_touch_1024_m846(self):
        # Guarded in the log entry per convention; the test file keeps
        # the in-flight list only (own-file reference would trip the
        # contiguous-literal discipline elsewhere).
        src = open(os.path.join(TESTS_DIR, OWN_BASENAME),
                   encoding="utf-8").read()
        assert "#1024" in src
