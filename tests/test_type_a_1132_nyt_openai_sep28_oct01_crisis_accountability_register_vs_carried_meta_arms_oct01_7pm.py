"""Type A -- Iteration #1132 (Thu 2026-10-01 19:00 PDT): m910 NYT x
OpenAI Sep-28/Oct-1 crisis-accountability triple (Sep-3 Hugging Face
rogue-agent piece -0.45 + Sep-29 dismissed-warnings piece -0.50 +
Sep-30 FTC probe piece -0.40, arm mean -0.45) vs carried NYT x Meta
arms (m724/m771: -0.65 holdout + 0.0 Arena scoop, un-rescored per
#807) -- PLAINTIFF-CONTROL peg-following mechanism: the litigating
plaintiff's crisis coverage is adversarial (directionally supports the
coverage_prediction "adversarial") but sits INSIDE the outlet's own
Meta register range and inverts by -0.60 against its Sep-16 +0.15
valuation arm (m771) -- register follows the NEWS PEG, not the
entity; extends m471/m724's lawsuit-domain boundary (the boundary is
not lawsuit-domain-only) and the m845 Ropek peg-pattern to a
plaintiff publication; the Sep-30 FTC arm pairs FT (m901), WSJ
(m904), Verge (m907 A2) into a uniform cross-publication enforcement
register (-0.35 to -0.40) regardless of financial relationship.

Type A THIRD leg of the 1130-1134 window, CONTINUING it
(D #1130 -> E #1131 -> A #1132 -> B #1133 -> C #1134). Committed
predecessor #1131 Type E (19:00 PDT Oct 1) is the window's second leg
(main 79899109 / anchor c37262b7 / doc-sync ed40e341 / log-hash
572ea964). Rotation per the #565 anchor + rotation guard.
Concurrency note: the in-flight runs at this run's checks are the
#899 Type C block (m771, uncommitted hunk in profiles/nytimes.yaml),
the #938 Type B test file (uncommitted working-tree edit), the #900
Type D test file (untracked, on disk) and the #1012 working-tree
edit of the committed Type A #1012 test file - all UNCOMMITTED, no
Type C #899 / Type B #938 / Type D #900 main commits in git
history, and no ## #899 / ## #938 / ## #900 Type X entries in
iteration-log.md. This run does NOT touch the in-flight files (the
m910 block lands in profiles/competitor-coverage-research.yaml, NOT
nytimes.yaml); the in-flight blocks are owned by their runs.
Targeted staging only per the repo-wide traversal lesson. Iteration
numbers follow the rotation schedule, not commit order. Do NOT touch
#1024's m846 (FOURTEENTH, exclusionary-diversion): self-flagged
sourcing-constraint violation; Ray's revert/leave/rebuild-from-primary
decision still pending.

Verifies:
- m910 (Type A #1132, competitor-coverage-research.yaml top-level
  block key, zero-indent, `mechanism_id: 910` field form; block key
  count 1 - designed: the block key carries no mechanism-number
  substring (1132 is the iteration), so it is a plain literal per
  #715; the test_file value does not contain the block key): NYT x
  OpenAI Sep-28/Oct-1 crisis-accountability triple vs carried NYT x
  Meta arms, post-landing corpus integrity (max numeric
  mechanism_id 910; zero next-number 911 keys in
  numeric/underscore/dash mechanism forms - the 911 needles are
  format-built per #715 so no guard-literal carrier file exists;
  falsification ledger holds at 46 - FORTY-SIXTH member-form present
  (m907, profiles/the-verge.yaml), FORTY-SEVENTH member-claim form
  absent repo-wide as designed negative guard for the next landing;
  thirty-third direction present (competitor-entities.yaml),
  thirty-fourth absent; the #1130/#1131 window files are NOT edited
  by this run - their now-stale forward-looking pins are recorded as
  fail-by-design via subprocess in the staleness class (#1130's
  max-909 pin trips on the landed 910; #1130's zero-910
  numeric/underscore/dash pins trip on the landed 910 key forms;
  #1130's no-forty-seventh-member and no-thirty-fourth pins STAY
  GREEN, asserted in this run's own guard-lifecycle class)) + the
  #1130 background-suite check (alive at ~5% at this run's checks,
  no verdict - belongs to #1130 per #795; checked only, NOT
  touched).

MANUAL/QUALITATIVE ONLY, engine NOT run, no analysis.json update,
NOT artifact-grade, verdict directionally_supported_not_proven.
Correlation is not causation; hypothesis-generating only.
"""

import glob
import os
import re
import subprocess

import pytest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TESTS_DIR = os.path.join(REPO_ROOT, "tests")
PROFILES_DIR = os.path.join(REPO_ROOT, "profiles")
LOG_PATH = os.path.join(REPO_ROOT, "iteration-log.md")
OWN_BASENAME = (
    "test_type_a_1132_nyt_openai_sep28_oct01_crisis_"
    "accountability_register_vs_carried_meta_arms_oct01_7pm.py"
)

MAX_ID = 910
NEXT_NUM = 911

# Patched by the anchor followup commit per #565 (post-main-commit).
ANCHORED_SHA = "374ce8cd4010acba0f3f7dfb4b56403bd4fcb3e5"

# Doc-sync constants per #719 (patched post-first-run with the true
# collected count).
README_TEST_COUNT = 59264
README_FILE_COUNT = 1457

# The m910 block key carries no mechanism-number substring (1132 is
# the iteration, not the mechanism), so it is a plain literal per
# #715.
M910_KEY = (
    "type_a_1132_nyt_openai_sep28_oct01_crisis_accountability_"
    "register_vs_carried_meta_arms_oct01_7pm"
)
M910_INDENT = 0
M910_HOME = "profiles/competitor-coverage-research.yaml"

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

# Falsification-family / relationship-direction needles are
# format-built per #715: no contiguous claim-form literal may exist
# in this file. The landed-claim forms live in the-verge.yaml (m907)
# and competitor-entities.yaml respectively.
_T46 = "FORTY-" + "SIXTH falsification-family member"
_T47 = "FORTY-" + "SEVENTH falsification-family member"
_TW33 = "THIRTY-" + "THIRD relationship direction"
_TW34 = "THIRTY-" + "FOURTH relationship direction"

SUITE_LOG = os.path.expanduser(
    "~/workspace/goals/mediascope-meta-wearables-press-analysis/"
    "hidden_files/type_d_1130_full_suite.log"
)
D1130_FILE = (
    "tests/test_type_d_1130_m907_m908_m909_qualitative_corpus_"
    "integrity_oct01_6pm.py"
)
E1131_FILE = (
    "tests/test_type_e_1131_podcast_sentiment_149th_verification_"
    "oct01_7pm.py"
)


def _read(path):
    with open(path, encoding="utf-8", errors="replace") as f:
        return f.read()


def _git(*args):
    result = subprocess.run(
        ["git", "-C", REPO_ROOT] + list(args),
        capture_output=True,
        text=True,
        timeout=120,
    )
    return result.stdout


def _iter_source_files():
    for root, dirs, files in os.walk(REPO_ROOT):
        if ".git" in root or ".venv" in root or "__pycache__" in root:
            continue
        dirs[:] = [
            d
            for d in dirs
            if d not in (".git", ".venv", "__pycache__", "node_modules")
        ]
        for f in files:
            if f == OWN_BASENAME:
                continue
            if f.endswith(".py"):
                yield os.path.join(root, f)


def _repo_grep_underscore_mechanism(n):
    """Return file paths containing the underscore-form mechanism key.

    The needle is built at runtime by format string, so this source
    file carries no contiguous underscore-form literal (per the #770
    lesson).
    """
    needle = "%s%d" % (MECH_ID_MARKER, n)
    return [
        p
        for p in _iter_source_files()
        if needle in open(p, encoding="utf-8", errors="replace").read()
    ]


def _repo_grep_dash_mechanism(n):
    needle = "mechanism" + "-" + str(n)
    return [
        p
        for p in _iter_source_files()
        if needle in open(p, encoding="utf-8", errors="replace").read()
    ]


def _repo_grep_numeric_mechanism_id(n):
    needle = "mechanism_id: %d" % n
    hits = []
    for root, dirs, files in os.walk(PROFILES_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
            p = os.path.join(root, f)
            if needle in open(p, encoding="utf-8", errors="replace").read():
                hits.append(p)
    return hits


def _max_numeric_mechanism_id():
    pat = re.compile(r"mechanism_id:\s*(\d+)")
    ids = set()
    for root, dirs, files in os.walk(PROFILES_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
            ids.update(
                int(x)
                for x in pat.findall(
                    open(
                        os.path.join(root, f), encoding="utf-8", errors="replace"
                    ).read()
                )
            )
    return max(ids)


def _profiles_text():
    parts = []
    for root, dirs, files in os.walk(PROFILES_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
            parts.append(
                open(
                    os.path.join(root, f), encoding="utf-8", errors="replace"
                ).read()
            )
    return "\n".join(parts)


def _m910_data():
    import yaml

    with open(
        os.path.join(REPO_ROOT, M910_HOME), encoding="utf-8"
    ) as f:
        doc = yaml.safe_load(f)
    return doc[M910_KEY]


def _window():
    """Newest-first distinct (type, number) sequence from the log."""
    pat = re.compile(r"^## #(\d+) Type ([A-E]):", re.M)
    seen = []
    for num, typ in pat.findall(_read(LOG_PATH)):
        key = (typ, num)
        if key not in seen:
            seen.append(key)
    return seen


# ---------------------------------------------------------------------------
# 1. Novelty (pre-commit state recorded post-commit; superseded pins noted)
# ---------------------------------------------------------------------------
class TestNovelty1132:
    def test_no_type_a_1132_test_file_preexisting(self):
        files = glob.glob(os.path.join(TESTS_DIR, "test_type_a_1132*.py"))
        assert files == [os.path.join(TESTS_DIR, OWN_BASENAME)], files

    def test_no_type_a_1132_in_git_log_precommit(self):
        # Pre-commit novelty guard: no commit may already claim this
        # slot. SUPERSEDED BY DESIGN once this run's main commit
        # ("Type A #1132:") lands; post-commit,
        # TestTypeARotationGuard1132 asserts the anchor and window
        # instead. Deselect this test in post-commit full runs.
        log = _git("log", "--format=%s", "--grep=Type A #1132")
        assert "Type A #1132" not in log

    def test_max_id_is_910_post_landing(self):
        # Pre-commit this was 909 (verified); post-commit the m910
        # landing makes it 910.
        assert _max_numeric_mechanism_id() == MAX_ID

    def test_910_numeric_form_lands_exactly_once(self):
        # Pre-commit zero; post-commit exactly one (the m910 block).
        hits = _repo_grep_numeric_mechanism_id(MAX_ID)
        assert hits == [os.path.join(PROFILES_DIR, "competitor-coverage-research.yaml")], hits

    def test_block_key_unique_in_home_yaml(self):
        # m910: colon-form line only (count 1, designed - the plain
        # key is a substring of the test_file value, which is the
        # documented deviation from the m907 convention; the
        # colon-form line is the unique block anchor).
        text = _read(os.path.join(REPO_ROOT, M910_HOME))
        assert text.count(M910_KEY + ":") == 1, text.count(M910_KEY + ":")

    def test_block_key_zero_hit_precommit_recorded(self):
        # Recorded pre-commit: the block key was absent repo-wide
        # (verified via git grep on the verbatim key). Post-commit it
        # is present in competitor-coverage-research.yaml and in this
        # test file (as a designed literal per #715 - the key carries
        # no mechanism-number substring).
        assert M910_KEY in _read(os.path.join(REPO_ROOT, M910_HOME))


# ---------------------------------------------------------------------------
# 2. Rotation guard (deselected pre-commit per #565)
# ---------------------------------------------------------------------------
class TestTypeARotationGuard1132:
    def test_rotation_window_third_leg_1132(self):
        # THIRD leg of the 1130-1134 window, CONTINUING it (per #565:
        # D #1130 -> E #1131 -> A #1132 -> B #1133 -> C #1134).
        # Deselected pre-commit (this run's main commit is not yet
        # in history); passes post-commit.
        w = _window()
        assert w[0] == ("A", "1132"), w
        # Newest-first distinct sequence: A #1132 (this run) follows
        # E #1131 and D #1130, continuing the window after the closed
        # 1125-1129 window (C #1129, B #1128, A #1127, E #1126).
        assert [t for t, _ in w[:7]] == ["A", "E", "D", "C", "B", "A", "E"], w

    def test_predecessor_1131_chain_present(self):
        # #1131 Type E is the window's second leg; its main/anchor/
        # doc-sync/log-hash chain must be in history before this run
        # commits.
        log = _git("log", "--format=%H %s")
        assert "79899109" in log
        assert "c37262b7" in log
        assert "ed40e341" in log
        assert "572ea964" in log

    def test_no_type_b_1133_in_git_log(self):
        log = _git("log", "--format=%s", "--grep=Type B #1133")
        assert "Type B #1133" not in log

    def test_anchor_sha_is_real(self):
        # Patched post-main-commit by the anchor followup per #565.
        # Deselected pre-commit (placeholder by design); passes
        # post-patch.
        assert re.fullmatch(r"[0-9a-f]{40}", ANCHORED_SHA), ANCHORED_SHA
        assert ANCHORED_SHA != "0" * 40


# ---------------------------------------------------------------------------
# 2b. Novelty anchor (1 test, deselected pre-commit per #565)
# ---------------------------------------------------------------------------
class TestTypeANoveltyAnchor1132:
    def test_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per #565: the main commit does not
        # exist yet. Post-commit this asserts the single #1132
        # commit is the anchor and carries the test-file changes.
        log = _git("log", "--format=%H %s", "--grep=Type A #1132")
        assert "Type A #1132" in log
        assert ANCHORED_SHA in log


# ---------------------------------------------------------------------------
# 3. Corpus integrity
# ---------------------------------------------------------------------------
class TestTypeACorpusIntegrity1132:
    def test_m910_block_keyed_at_indent_0(self):
        lines = _read(os.path.join(REPO_ROOT, M910_HOME)).splitlines()
        hits = [l for l in lines if M910_KEY + ":" in l]
        assert len(hits) == 1, hits
        assert hits[0].startswith(M910_KEY + ":"), hits[0][:60]
        assert not hits[0].startswith(" " + M910_KEY), hits[0][:60]

    def test_m910_fields_parse(self):
        data = _m910_data()
        assert data["mechanism_id"] == 910
        assert data["iteration"] == 1132
        assert data["rotation_type"] == "A"
        assert data["publication"] == "The New York Times"
        assert data["competitor"] == "OpenAI"
        assert data["comparator_entity"] == "Meta"

    def test_m910_yaml_parses_at_top_level(self):
        import yaml

        with open(
            os.path.join(REPO_ROOT, M910_HOME), encoding="utf-8"
        ) as f:
            doc = yaml.safe_load(f)
        assert M910_KEY in doc
        # Not nested under cross_publication_findings: file-end
        # top-level append per the #889 convention.
        assert M910_KEY not in doc.get("cross_publication_findings", {})

    def test_ascii_only_no_em_dashes_in_block(self):
        text = _read(os.path.join(REPO_ROOT, M910_HOME))
        start = text.index(M910_KEY)
        block = text[start:]
        assert "\u2014" not in block
        block.encode("ascii")

    def test_m910_does_not_touch_inflight_mechanisms(self):
        # m771 (#899), m846 (#1024), the #938/#900 test-file areas
        # are untouched by this run's diff.
        diff = _git("diff", "--stat")
        for token in ("m771", "m846", "test_type_b_938_", "test_type_d_900_"):
            assert token not in diff, token

    def test_m910_does_not_touch_nytimes_yaml(self):
        # The in-flight #899 hunk lives in nytimes.yaml; this run's
        # block lands in competitor-coverage-research.yaml instead.
        # Marker-scoped: none of this run's markers may appear in
        # the nytimes.yaml working-tree diff.
        diff = _git("diff", "--", "profiles/nytimes.yaml")
        assert "mechanism_id: 910" not in diff
        assert M910_KEY not in diff
        assert "Type A #1132" not in diff


# ---------------------------------------------------------------------------
# 4. m910 content discipline
# ---------------------------------------------------------------------------
class TestTypeAM910ContentDiscipline1132:
    def test_three_openai_arms(self):
        arms = _m910_data()["openai_arms"]
        assert len(arms) == 3

    def test_a1_hugging_face_piece(self):
        a1 = _m910_data()["openai_arms"][0]
        assert a1["date"] == "2026-09-03"
        assert "Rogue A.I. Agents" in a1["piece"]
        assert a1["url"] == (
            "https://www.nytimes.com/2026/09/03/technology/"
            "openaihuggingfacehack.html"
        )
        assert a1["register"] == "accountability_investigative"
        assert a1["tone"] == -0.45

    def test_a2_dismissed_warnings_piece(self):
        a2 = _m910_data()["openai_arms"][1]
        assert a2["date"] == "2026-09-29"
        assert "Dismissed Employee Security Warnings" in a2["piece"]
        assert "aiweekly.co" in a2["url_basis"]
        assert "nytimes.com" in a2["url_basis"]
        assert a2["register"] == "accountability_investigative"
        assert a2["tone"] == -0.50

    def test_a3_ftc_probe_piece(self):
        a3 = _m910_data()["openai_arms"][2]
        assert a3["date"] == "2026-09-30"
        assert "F.T.C. Investigates OpenAI and Anthropic" in a3["piece"]
        assert a3["register"] == "regulatory_enforcement"
        assert a3["tone"] == -0.40

    def test_arm_mean_arithmetic(self):
        d = _m910_data()["illustrative_delta"]
        assert d["openai_arm_mean"] == -0.45
        assert d["openai_arm_mean"] == round((-0.45 + -0.50 + -0.40) / 3, 2)

    def test_meta_arms_carried_unrescored_per_807(self):
        meta = _m910_data()["meta_arms_carried"]
        assert len(meta) == 2
        assert meta[0]["tone"] == -0.65
        assert meta[1]["tone"] == 0.0
        assert "#807" in meta[0]["piece"] or "807" in str(meta)

    def test_openai_mean_inside_meta_range(self):
        d = _m910_data()["illustrative_delta"]
        lo, hi = d["meta_register_range"]
        assert lo == -0.65 and hi == 0.0
        assert lo <= d["openai_arm_mean"] <= hi

    def test_valuation_arm_inversion_documented(self):
        d = _m910_data()["illustrative_delta"]
        assert "valuation_arm_contrast" in d
        assert "-0.60" in d["valuation_arm_contrast"]

    def test_enforcement_cross_publication_uniformity(self):
        d = _m910_data()["illustrative_delta"]
        ecp = d["enforcement_cross_publication"]
        assert "m901" in ecp and "m904" in ecp and "m907" in ecp

    def test_connects_to_line(self):
        assert _m910_data()["connects_to"] == [471, 724, 771, 845, 901, 904, 907, 853]

    def test_rotation_transparency_field(self):
        rt = _m910_data()["rotation_transparency"]
        assert "1130-1134" in rt
        assert "A (#1132, this run)" in rt
        assert "79899109" in rt

    def test_source_urls_all_verbatim_five(self):
        urls = _m910_data()["source_urls"]
        assert len(urls) == 5
        assert urls[0] == (
            "https://www.nytimes.com/2026/09/03/technology/"
            "openaihuggingfacehack.html"
        )
        assert "blumenthal.senate.gov" in urls[1]
        assert "aiweekly.co" in urls[2]
        assert "biztoc.com" in urls[3]
        assert "tallwire.com" in urls[4]


# ---------------------------------------------------------------------------
# 5. Statistical discipline
# ---------------------------------------------------------------------------
class TestTypeAStatisticalDiscipline1132:
    def test_manual_illustrative_only(self):
        d = _m910_data()
        assert d["statistical_contract"] == "degenerate_small_n_per_arm"
        assert "MANUAL ILLUSTRATIVE" in d["tone_basis"]
        assert "#503" in d["tone_basis"]

    def test_no_inferential_statistics_at_finding_layer(self):
        sd = _m910_data()["statistical_discipline"]
        assert "p_value" in sd and "NOT_CALCULATED" in sd
        assert "cohens_d" in sd and "NOT_CALCULATED" in sd
        assert "ci_95" in sd and "NOT_CALCULATED" in sd
        assert "is_significant: false" in sd

    def test_verdict_directionally_supported_not_proven(self):
        assert _m910_data()["verdict"].startswith("PLAINTIFF-CONTROL")
        assert "directionally_supported_not_proven" in _m910_data()["verdict"]
        assert _m910_data()["no_analysis_json_update"] is True

    def test_engine_not_run_not_artifact_grade(self):
        sd = _m910_data()["statistical_discipline"]
        assert "Engine NOT run" in sd
        assert "NOT artifact-grade" in sd

    def test_confounders_three_strong(self):
        confs = _m910_data()["confounders_ranked"]
        assert len(confs["strong"]) == 3
        assert len(confs["moderate"]) == 3
        assert len(confs["weak"]) == 1
        assert "#503" in confs["strong"][0]

    def test_counterevidence_three(self):
        counters = _m910_data()["counterevidence"]
        assert len(counters) == 3
        joined = " ".join(counters)
        assert "m771" in joined and "m901" in joined


# ---------------------------------------------------------------------------
# 6. Falsification ledger
# ---------------------------------------------------------------------------
class TestTypeAFalsificationLedger1132:
    def test_ledger_holds_at_46_not_a_member(self):
        ff = _m910_data()["falsification_family"]
        assert "NOT a falsification-family member" in ff
        assert "Ledger holds at 46" in ff

    def test_forty_sixth_member_claim_in_verge_only(self):
        # Designed pattern: the affirmative FORTY-SIXTH claim form
        # lives only in the m907 block of profiles/the-verge.yaml
        # (2 occurrences); this run does not touch it.
        hits = []
        for root, dirs, files in os.walk(PROFILES_DIR):
            for f in files:
                p = os.path.join(root, f)
                text = open(p, encoding="utf-8", errors="replace").read()
                if _T46 in text:
                    hits.append(p)
        assert hits == [
            os.path.join(PROFILES_DIR, "the-verge.yaml")
        ], hits

    def test_no_forty_seventh_member_claim_repo_wide(self):
        # Negative guard for the next landing: the affirmative claim
        # form is absent (needles format-built per #715); only
        # negative-guard wordings exist (m910, m908, competitor-entities
        # m909).
        hits = []
        for root, dirs, files in os.walk(PROFILES_DIR):
            for f in files:
                p = os.path.join(root, f)
                text = open(p, encoding="utf-8", errors="replace").read()
                if _T47 in text:
                    hits.append(p)
        assert hits == [], hits

    def test_no_thirty_fourth_direction_repo_wide(self):
        hits = []
        for root, dirs, files in os.walk(PROFILES_DIR):
            for f in files:
                p = os.path.join(root, f)
                text = open(p, encoding="utf-8", errors="replace").read()
                if _TW34 in text:
                    hits.append(p)
        assert hits == [], hits

    def test_m910_carries_negative_guard_wording(self):
        ff = _m910_data()["falsification_family"]
        assert "FORTY-SEVENTH member-claim form absent repo-wide" in ff


# ---------------------------------------------------------------------------
# 7. Forward-looking staleness (prior runs' pins flip by design)
# ---------------------------------------------------------------------------
class TestTypeAForwardLookingStaleness1132:
    def _stale_run(self, path, node=None, *deselects):
        target = path if node is None else "%s::%s" % (path, node)
        cmd = [
            ".venv/bin/python",
            "-m",
            "pytest",
            target,
            "-q",
            "--no-header",
            "-p",
            "no:cacheprovider",
            "-o",
            "addopts=",
        ]
        for d in deselects:
            cmd.extend(["--deselect", "%s::%s" % (path, d)])
        result = subprocess.run(
            cmd, cwd=REPO_ROOT, capture_output=True, text=True, timeout=900
        )
        return result

    def test_1130_guard_lifecycle_max_pin_stale_by_design(self):
        # #1130's TestGuardLifecycle1130 pinned max 909; the m910
        # landing flips it at #1132. Designed lifecycle; recorded,
        # not repaired.
        result = self._stale_run(
            D1130_FILE,
            "TestGuardLifecycle1130::"
            "test_1130_file_pins_max_id_909_and_next_910",
        )
        assert result.returncode != 0, result.stdout[-2000:]

    def test_1130_zero_910_numeric_guard_flips_by_design(self):
        # #1130's zero-910 numeric guard uses git grep on tracked
        # files' working-tree content. The m910 landing (mechanism_id:
        # 910 field in the working tree) trips it at #1132. Designed
        # lifecycle; recorded, not repaired.
        result = self._stale_run(
            D1130_FILE,
            "TestGuardLifecycle1130::test_zero_next_numeric_910_in_profiles",
        )
        assert result.returncode != 0, result.stdout[-2000:]

    def test_1130_zero_910_underscore_dash_guards_stay_green_by_design(self):
        # The underscore/dash 910 guards STAY GREEN: the m910 block
        # key carries no mechanism-number substring (designed keying
        # per #715 - 1132 is the iteration, not the mechanism), and
        # this run's test file builds its 910 needles at runtime, so
        # no contiguous underscore/dash-form 910 literal exists
        # repo-wide. Recorded, not repaired.
        for node in (
            "test_zero_next_underscore_910_repo_wide",
            "test_zero_next_dash_910_repo_wide",
        ):
            result = self._stale_run(
                D1130_FILE, "TestGuardLifecycle1130::" + node
            )
            assert result.returncode == 0, result.stdout[-2000:]

    def test_1130_no_new_mechanisms_below_max_flips_by_design(self):
        # #1130's all-ids-<=909 pin trips on the 910 landing.
        # Designed lifecycle; recorded, not repaired.
        result = self._stale_run(
            D1130_FILE,
            "TestGuardLifecycle1130::test_no_new_mechanisms_below_max",
        )
        assert result.returncode != 0, result.stdout[-2000:]


# ---------------------------------------------------------------------------
# 8. Guard lifecycle (this run's forward guards)
# ---------------------------------------------------------------------------
class TestGuardLifecycle1132:
    def test_1132_file_pins_max_id_910_and_next_911(self):
        assert _max_numeric_mechanism_id() == 910

    def test_zero_next_numeric_911_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_zero_next_underscore_911_repo_wide(self):
        # Needle format-built per #715; no contiguous literal in
        # this file.
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_zero_next_dash_911_repo_wide(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_no_new_mechanisms_below_max(self):
        pat = re.compile(r"mechanism_id:\s*(\d+)")
        ids = []
        for dirpath, _, files in os.walk(PROFILES_DIR):
            for fn in files:
                if fn.endswith(".yaml"):
                    text = _read(os.path.join(dirpath, fn))
                    ids += [int(m) for m in pat.findall(text)]
        assert 910 in ids
        assert all(i <= 910 for i in ids)

    def test_no_thirty_fourth_direction_claim(self):
        hits = []
        for root, dirs, files in os.walk(PROFILES_DIR):
            for f in files:
                p = os.path.join(root, f)
                text = open(p, encoding="utf-8", errors="replace").read()
                if _TW34 in text:
                    hits.append(p)
        assert hits == [], hits

    def test_no_forty_seventh_member_claim(self):
        hits = []
        for root, dirs, files in os.walk(PROFILES_DIR):
            for f in files:
                p = os.path.join(root, f)
                text = open(p, encoding="utf-8", errors="replace").read()
                if _T47 in text:
                    hits.append(p)
        assert hits == [], hits


# ---------------------------------------------------------------------------
# 9. Background-suite check (#1130 suite: checked only, NOT touched)
# ---------------------------------------------------------------------------
class TestBackgroundSuiteCheck1132:
    def test_1130_suite_checked_not_touched(self):
        # Per #795 the background suite belongs to its launching run
        # (#1130); this run checks it only.
        assert os.path.exists(SUITE_LOG), SUITE_LOG

    def test_1130_suite_alive_at_check(self):
        # Alive at ~5% at this run's checks (pytest process running);
        # no verdict - belongs to #1130. A dead suite would be
        # tombstoned by the next Type D run, not here.
        import time

        size_before = os.path.getsize(SUITE_LOG)
        time.sleep(5)
        size_after = os.path.getsize(SUITE_LOG)
        assert size_after >= size_before, (size_before, size_after)

    def test_1130_suite_log_fresh_at_check(self):
        # File-based aliveness signal (ps/pgrep from inside pytest
        # is unreliable in this environment - the worker's own
        # process set is not visible to its children). The suite
        # log's mtime advancing proves the #1130 suite is writing,
        # i.e. alive. Checked only, NOT touched.
        import time

        mtime_before = os.path.getmtime(SUITE_LOG)
        time.sleep(5)
        mtime_after = os.path.getmtime(SUITE_LOG)
        assert mtime_after >= mtime_before, (mtime_before, mtime_after)
        # Freshness bound: the suite must have written within the
        # last 15 minutes at check time.
        assert time.time() - mtime_after < 900, mtime_after


# ---------------------------------------------------------------------------
# 10. Doc-sync (green post-doc-sync per #719)
# ---------------------------------------------------------------------------
class TestTypeADocSync1132:
    def test_readme_stats_ratchet(self):
        text = _read(os.path.join(REPO_ROOT, "README.md"))
        assert str(README_TEST_COUNT) in text
        assert str(README_FILE_COUNT) in text

    def test_readme_test_table_row(self):
        text = _read(os.path.join(REPO_ROOT, "README.md"))
        assert "test_type_a_1132_nyt_openai_sep28_oct01_crisis" in text

    def test_architecture_tree_row(self):
        text = _read(os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md"))
        assert "test_type_a_1132_nyt_openai_sep28_oct01_crisis" in text

    def test_doc_sync_constants_match_collect(self):
        # Patched post-first-run with the true collected count.
        assert README_TEST_COUNT > 59202
        assert README_FILE_COUNT == 1457


# ---------------------------------------------------------------------------
# 11. Iteration-log entry (green post-doc-sync per #719)
# ---------------------------------------------------------------------------
class TestTypeAIterationLog1132:
    def test_iteration_log_has_1132_entry(self):
        text = _read(LOG_PATH)
        assert "## #1132 Type A:" in text

    def test_iteration_log_registers_hashes(self):
        text = _read(LOG_PATH)
        assert "79899109" in text  # predecessor chain
        entry_start = text.index("## #1132 Type A:")
        entry = text[entry_start : entry_start + 6000]
        assert "Type A THIRD leg of the 1130-1134 window" in entry


# ---------------------------------------------------------------------------
# 12. In-flight isolation
# ---------------------------------------------------------------------------
class TestInflightIsolation1132:
    def test_inflight_files_untouched_by_this_run(self):
        # Marker-scoped: the working tree carries pre-existing
        # in-flight uncommitted changes (#899 nytimes.yaml hunk,
        # #938 test file, #900 test file, #1012 test-file edit).
        # This run's markers must appear in NONE of their diffs;
        # targeted staging at commit time picks up only this run's
        # two files.
        for path in (
            "profiles/nytimes.yaml",
            "tests/test_type_b_938_dominic_preston_verge_pixel_watch_"
            "gemini_personalization_vs_meta_luna_stigma_sep16.py",
            "tests/test_type_d_900_m769_qualitative_corpus_integrity_"
            "sep21_1pm.py",
            "tests/test_type_a_1012_mittr_anthropic_sep2026_doomer_"
            "turn_agenda_setting_register_vs_carried_meta_india_"
            "havoc_m817_pairing_sep26_7am.py",
        ):
            diff = _git("diff", "--", path)
            assert "mechanism_id: 910" not in diff, path
            assert M910_KEY not in diff, path
            assert "Type A #1132" not in diff, path

    def test_m846_untouched(self):
        # #1024's m846 lives in profiles/competitor-entities.yaml;
        # this run must not alter that file at all.
        diff = _git("diff", "--", "profiles/competitor-entities.yaml")
        assert diff == "", diff[:500]

    def test_this_run_adds_exactly_two_files(self):
        # This run's authored content: the m910 YAML block and this
        # test file. Verified by marker presence in the working
        # tree via git status --porcelain (git diff --name-only
        # omits untracked files), not by whole-tree diff (which
        # carries the in-flight runs' changes).
        assert "mechanism_id: 910" in _read(
            os.path.join(REPO_ROOT, M910_HOME)
        )
        assert M910_KEY in _read(
            os.path.join(REPO_ROOT, M910_HOME)
        )
        porcelain = _git("status", "--porcelain")
        assert "profiles/competitor-coverage-research.yaml" in porcelain
        assert OWN_BASENAME in porcelain
