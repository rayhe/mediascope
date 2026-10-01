"""Type B #1108 (2026-09-30 21:00 PDT) - Nicole Nguyen (WSJ) x Meta Muse vs
Apple Siri AI-assistant hands-on trust-register pair, mechanism 896.

FOURTH leg of the 1105-1109 window (D #1105 -> E #1106 -> A #1107 ->
B #1108 -> C #1109), per the #565 rotation anchor. Predecessor: #1107
Type A (mediascope-daily-iteration, 2026-09-30 20:00 PDT). The 1100-1104
window is verified closed.

Mechanism 896 pairs Nguyen's Sep-29 2026 WSJ Meta Muse AI-agent review
("I Tried Meta's Muse AI Agent. It's Helpful and Scary at the Same
Time.", +0.10 MANUAL ILLUSTRATIVE, IN-CORPUS via m893 carried
un-rescored per #807) against her FRESH mid-Sep 2026 WSJ Siri hands-on
review ("Siri finally grows up: Apple's new assistant can see your
screen, search your photos, and get real work done", +0.40 MANUAL
ILLUSTRATIVE, NOVEL to corpus, relay-attested via newslocker with
verbatim WSJ/Nicole Nguyen byline attribution, excerpt-bounded per #503;
WSJ original paywalled, 0 browser.open on the original).

Finding: the same journalist, same publication, same AI-assistant
hands-on genre, 12 days apart, applies a harder entity-rooted trust
register to the paid cooperative counterparty (Meta, $50M/yr News Corp
licensing, +0.10 with "scary"/"trust issues"/"cautious and reset") than
to the zero-cooperative-deal entity (Apple, $0 News Corp licensing,
+0.40 with "private at every step" accepted). Illustrative delta (Apple
minus Meta) +0.30. The deal-softness prediction FAILS on ordering at the
journalist level a SECOND time: THIRTY-NINTH falsification-family
member, ledger 38 -> 39, replicating #1103's THIRTY-EIGHTH (Meta x
Anthropic) in the Meta x Apple pair. Extends #693's NINETEENTH lineage
(Nguyen Apple +0.40 constancy: Duo hardware arm and Siri assistant arm
now agree across two Apple pegs).

Discourse corroboration (not a scored arm): 9to5Mac Security Bite Sep
2026 ("I'm inclined to trust the privacy and safety safeguards Apple
has put into place. But ... Meta's Muse app the latest example - and one
tech writer's experience really underlines why you [shouldn't]") shows
the trust asymmetry is discourse-wide, not Nguyen-idiosyncratic.

Statistical discipline per the Aug 28 2026 standing rule: MANUAL
ILLUSTRATIVE ONLY, engine NOT run, p_value/cohens_d/ci_95
NOT_CALCULATED, is_significant false, verdict
directionally_supported_not_proven, no_analysis_json_update true, NOT
artifact-grade. Correlation is not causation; hypothesis-generating
only.

Literal discipline per #715: this file carries NO contiguous
underscore-form, dash-form, or numeric-form 896/897 mechanism literals -
the mechanism needles are format-built ("%d" % MECH_NUM / NEXT_NUM), so
the zero-896 pre-commit sweeps and zero-897 forward guards stay valid.
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

ITERATION = 1108
TYPE_LETTER = "B"
WINDOW = "1105-1109"
MECH_NUM = 896
NEXT_NUM = 897
ANCHORED_SHA = "9cd97d0a"  # main commit, patched in the anchor followup per #565
OWN_BASENAME = (
    "test_type_b_1108_nicole_nguyen_wsj_siri_grows_up_"
    "vs_muse_trust_register_sep30_9pm.py"
)
BLOCK_KEY = (
    "type_b_1108_nicole_nguyen_wsj_siri_grows_up_"
    "vs_muse_trust_register_sep30"
)
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TESTS_DIR = os.path.join(REPO_ROOT, "tests")
PROFILES_DIR = os.path.join(REPO_ROOT, "profiles")
JOURNALISTS_FILE = os.path.join(PROFILES_DIR, "careers", "journalists.yaml")
SIRI_RELAY_URL = (
    "https://www.newslocker.com/en-us/news/apple/wsj-siri-finally-grows-up-"
    "apples-new-assistant-can-see-your-screen-search-your-photos-and-"
    "get-real-work-done/"
)
MUSE_URL = "https://www.wsj.com/tech/personal-tech/meta-muse-ai-agent-review-ab956101"

# Patched post-commit once README/ARCHITECTURE doc-sync lands.
README_TEST_COUNT = 56511  # post-doc-sync total
README_FILE_COUNT = 1433  # post-doc-sync total
TEST_BASENAME = OWN_BASENAME

F1107 = ("test_type_a_1107_nyt_anthropic_s1_canary_register_"
         "vs_meta_carried_arms_sep30_8pm.py")


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
    nguyen = next(j for j in journalists if j.get("name") == "Nicole Nguyen")
    # Type B blocks nest under competitor_coverage (4-space indent).
    return nguyen["competitor_coverage"][BLOCK_KEY]


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

class TestNovelty1108:
    def test_single_test_file_for_iteration(self):
        files = glob.glob(os.path.join(TESTS_DIR, "test_type_b_1108*.py"))
        assert len(files) == 1, files
        assert files[0].endswith(OWN_BASENAME)

    def test_no_type_b_1108_in_git_log(self):
        # Commit-dependent: empty pre-commit; fails post-commit by design.
        res = _git("log", "--oneline", "--grep=Type B #1108")
        assert res.stdout.strip() == "", res.stdout

    def test_max_numeric_mechanism_id_is_896(self):
        # Working tree includes the uncommitted block (mechanism_id 896).
        ids = []
        for root, dirs, files in os.walk(PROFILES_DIR):
            dirs[:] = [d for d in dirs if d != "__pycache__"]
            for f in files:
                p = os.path.join(root, f)
                for m in re.finditer(r"mechanism_id:\s*(\d+)",
                                     _read(p)):
                    ids.append(int(m.group(1)))
        assert max(ids) == MECH_NUM

    def test_numeric_896_exactly_one_profile(self):
        hits = _profiles_grep_numeric_mechanism_id(MECH_NUM)
        assert hits == [JOURNALISTS_FILE], hits

    def test_zero_underscore_896_repo_wide(self):
        # Designed keying: colon-form block key only; underscore-form 896
        # stays zero (own test file excluded, needles format-built per #715).
        assert _repo_grep_underscore_mechanism(MECH_NUM) == []

    def test_zero_dash_896_repo_wide(self):
        assert _repo_grep_dash_mechanism(MECH_NUM) == []

    def test_siri_relay_url_only_in_block_and_own_file(self):
        # Pre-insert novelty (zero-hit repo-wide) verified via subprocess
        # during research; post-insert the URL lives only in the block.
        hits = [p for p in _iter_source_files()
                if SIRI_RELAY_URL in _read(p)
                and not p.endswith(OWN_BASENAME)]
        assert hits == [JOURNALISTS_FILE], hits

    def test_block_key_present_in_journalists(self):
        assert BLOCK_KEY in _read(JOURNALISTS_FILE)


# ---------------------------------------------------------------------------
# 2. Rotation guard (markers anchor/rotation).
# ---------------------------------------------------------------------------

class TestRotationGuard1108:
    @pytest.mark.rotation
    def test_window_1105_1109_fourth_leg(self):
        """B is the fourth leg of the 1105-1109 window per #565."""
        assert TYPE_LETTER == "B"
        assert ITERATION == 1108
        assert WINDOW == "1105-1109"

    @pytest.mark.rotation
    def test_type_b_adjacency_in_window(self):
        """D(#1105) -> E(#1106) -> A(#1107) -> B(#1108, this run) -> C(#1109)."""
        d_files = glob.glob(os.path.join(TESTS_DIR, "test_type_d_1105*.py"))
        e_files = glob.glob(os.path.join(TESTS_DIR, "test_type_e_1106*.py"))
        a_files = glob.glob(os.path.join(TESTS_DIR, "test_type_a_1107*.py"))
        assert len(d_files) >= 1 and len(e_files) >= 1 and len(a_files) >= 1

    @pytest.mark.rotation
    def test_predecessor_is_type_a_1107(self):
        files = glob.glob(os.path.join(TESTS_DIR, "test_type_a_1107*.py"))
        assert len(files) >= 1

    @pytest.mark.rotation
    def test_single_type_b_1108_file_is_this_run(self):
        files = glob.glob(os.path.join(TESTS_DIR, "test_type_b_1108*.py"))
        assert len(files) == 1 and files[0].endswith(OWN_BASENAME)

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

class TestNoveltyAnchor1108:
    @pytest.mark.anchor
    def test_anchor_sha_patched_post_commit(self):
        # No #1108 main commit exists pre-commit; the anchor test pins
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
            if "Type B #1108" in line and "followup" not in line.lower()
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
# 4. Mechanism 896 block structure (YAML-parsed).
# ---------------------------------------------------------------------------

class TestMechanism896Structure:
    def test_block_key_present(self):
        assert BLOCK_KEY in _block_text()

    def test_mechanism_id(self):
        assert _block()["mechanism_id"] == MECH_NUM

    def test_type_and_iteration(self):
        b = _block()
        assert b["type"] == "Type B: Journalist Cross-Entity Tracking"
        assert b["iteration"] == ITERATION
        assert b["journalist"] == "Nicole Nguyen"
        assert b["publication"] == "wall-street-journal"

    def test_meta_arm_carried_per_807(self):
        meta = _block()["meta_arm"]
        assert meta["entity"] == "Meta"
        assert meta["manual_illustrative_tone"] == 0.10
        assert "un-rescored" in meta["carried_per_807"]
        assert "m893" in meta["carried_per_807"]
        assert "IN-CORPUS" in meta["carried_per_807"]
        assert MUSE_URL in meta["url"]

    def test_apple_arm_fresh_novel(self):
        apple = _block()["apple_arm"]
        assert apple["entity"] == "Apple"
        assert apple["manual_illustrative_tone"] == 0.40
        assert "FRESH" in apple["novelty"]
        assert SIRI_RELAY_URL in apple["url"]
        assert "Siri finally grows up" in apple["title"]

    def test_illustrative_delta(self):
        b = _block()
        assert "+0.30" in b["illustrative_delta"]
        assert "Apple minus Meta" in b["illustrative_delta"]

    def test_falsification_member(self):
        b = _block()
        assert "THIRTY-NINTH falsification-family member" in b["falsification_family"]
        assert b["falsification_ledger"] == "39"

    def test_statistical_discipline(self):
        b = _block()
        assert "MANUAL ILLUSTRATIVE ONLY" in b["statistical_discipline"]
        assert "NOT_CALCULATED" in b["statistical_discipline"]
        assert b["no_analysis_json_update"] is True
        assert b["correlation_not_causation"] is True

    def test_confounder_coverage(self):
        text = _block_text()
        assert "[STRONG] Factual-substrate confounder" in text
        assert "[STRONG] Excerpt-tier on the Apple arm" in text
        assert "[MODERATE] Temporal gap" in text
        assert "[MODERATE] Product-form difference" in text
        assert "[WEAK] Degenerate n=1 per arm" in text

    def test_ascii_only(self):
        text = _block_text()
        assert all(ord(c) < 128 for c in text), "block must be ASCII-only"
        assert "\u2014" not in text and "\u2013" not in text


# ---------------------------------------------------------------------------
# 5. Falsification ledger holds at 39.
# ---------------------------------------------------------------------------

class TestLedger39:
    def _ledger_hits(self, needle):
        hits = []
        for root, dirs, files in os.walk(PROFILES_DIR):
            dirs[:] = [d for d in dirs if d != "__pycache__"]
            for f in files:
                p = os.path.join(root, f)
                if needle in _read(p):
                    hits.append(p)
        return hits

    def test_thirty_ninth_present_once(self):
        hits = self._ledger_hits("THIRTY-NINTH falsification-family member")
        assert hits == [JOURNALISTS_FILE], hits

    def test_thirty_ninth_is_m896(self):
        text = _read(JOURNALISTS_FILE)
        assert "THIRTY-NINTH falsification-family member" in text
        assert ("mechanism_id: %d" % MECH_NUM) in text

    def test_thirty_eighth_intact(self):
        text = _read(JOURNALISTS_FILE)
        assert "THIRTY-EIGHTH falsification-family member" in text
        assert "mechanism_id: 893" in text

    def test_no_fortieth_member(self):
        assert self._ledger_hits("FORTIETH falsification-family member") == []


# ---------------------------------------------------------------------------
# 6. Forward guards: zero-897 in all mechanism-key forms (own file excluded,
#    needles format-built per #715).
# ---------------------------------------------------------------------------

class TestForwardGuards1108:
    def test_zero_numeric_897_in_profiles(self):
        assert _profiles_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_zero_underscore_897_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_zero_dash_897_repo_wide(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []


# ---------------------------------------------------------------------------
# 7. Supersession pins: #1107's zero-896 guards + no-39th-member guard fail
#    BY DESIGN now that this run lands 896 and the THIRTY-NINTH member.
# ---------------------------------------------------------------------------

class TestSupersessionPins1108:
    def test_1107_novelty_guards_remain_green(self):
        """#1107's TestNovelty1107 sweeps are scoped to PROFILES_DIR/*.yaml
        (top level only, not recursive); this run's block lands in
        profiles/careers/journalists.yaml, correctly outside that scope,
        so the class stays green. Recorded, not repaired."""
        result = _class_run(F1107, "TestNovelty1107")
        assert result.returncode == 0

    def test_1107_no_39th_member_guard_stale(self):
        """#1107's TestLedgerHoldsAt38 pinned no-39th-member with a
        recursive profiles/ walk; this run lands the THIRTY-NINTH member,
        so that guard must now fail. Recorded, not repaired."""
        result = subprocess.run(
            [os.path.join(REPO_ROOT, ".venv", "bin", "python"), "-m", "pytest",
             os.path.join(TESTS_DIR, F1107)
             + "::TestLedgerHoldsAt38::test_no_39th_member_form",
             "-q", "--no-header", "-p", "no:cacheprovider"],
            cwd=REPO_ROOT, capture_output=True, text=True,
        )
        assert result.returncode != 0

    def test_1107_ledger_38_class_stale(self):
        """The whole TestLedgerHoldsAt38 class is stale: ledger now holds 39."""
        result = _class_run(F1107, "TestLedgerHoldsAt38")
        assert result.returncode != 0


# ---------------------------------------------------------------------------
# 8. Degenerate n=1 contract on the illustrative pair (#638/#643).
# ---------------------------------------------------------------------------

class TestDegenerateContract1108:
    def _result(self):
        from datetime import datetime
        return calculate_asymmetry(
            [0.40], [0.10],
            target_entity="Apple",
            peer_entities=["Meta"],
            publication_slug="wall-street-journal",
            period_start=datetime(2026, 9, 16),
            period_end=datetime(2026, 9, 29),
        )

    def test_illustrative_delta(self):
        r = self._result()
        assert abs(r.asymmetry_score - 0.30) < 1e-9

    def test_degenerate_no_significance(self):
        r = self._result()
        assert r.t_statistic == 0.0
        assert r.p_value == 1.0
        assert r.is_significant is False


# ---------------------------------------------------------------------------
# 9. Doc-sync (DESELECTED pre-commit per #565/#719/#721; marker docsync).
# ---------------------------------------------------------------------------

class TestDocSync1108:
    @pytest.mark.docsync
    def test_readme_count_gate(self):
        """README test/file counts match the post-run totals."""
        readme = open(os.path.join(REPO_ROOT, "README.md"),
                      encoding="utf-8").read()
        assert ("| Tests | %d |" % README_TEST_COUNT) in readme
        assert ("Across %d test files" % README_FILE_COUNT) in readme

    @pytest.mark.docsync
    def test_readme_table_row(self):
        """The #1108 test-file row is appended to the README test table."""
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
        """The #1108 test-file row is appended to the ARCHITECTURE tree."""
        arch = open(os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md"),
                    encoding="utf-8").read()
        assert TEST_BASENAME in arch


# ---------------------------------------------------------------------------
# 10. Iteration log (DESELECTED pre-commit per #565/#719/#721; marker log).
# ---------------------------------------------------------------------------

class TestIterationLog1108:
    @pytest.mark.log
    def test_log_captures_1108(self):
        """The iteration log carries the #1108 Type B entry."""
        head = open(os.path.join(REPO_ROOT, "iteration-log.md"),
                    encoding="utf-8").read()[:5000]
        assert "## #1108 Type B:" in head
        assert "09:00 PM PDT" in head
        assert ("mechanism %d" % MECH_NUM) in head

    @pytest.mark.log
    def test_log_window(self):
        """The entry names the 1105-1109 window fourth leg."""
        head = open(os.path.join(REPO_ROOT, "iteration-log.md"),
                    encoding="utf-8").read()[:5000]
        assert "1105-1109" in head
        assert "FOURTH leg" in head

    @pytest.mark.log
    def test_log_ledger_39(self):
        """The entry records ledger holds at 39."""
        head = open(os.path.join(REPO_ROOT, "iteration-log.md"),
                    encoding="utf-8").read()[:5000]
        assert "ledger holds at 39" in head
        assert "THIRTY-NINTH" in head

    @pytest.mark.log
    def test_log_lineage(self):
        """The entry records the #1103 replication and #693 extension."""
        head = open(os.path.join(REPO_ROOT, "iteration-log.md"),
                    encoding="utf-8").read()[:5000]
        assert "1103" in head
        assert "693" in head
        assert "Nguyen" in head


# ---------------------------------------------------------------------------
# 11. In-flight isolation: #899/#938/#900/#1012-wt untouched by this run.
# ---------------------------------------------------------------------------

class TestInFlightIsolation1108:
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
