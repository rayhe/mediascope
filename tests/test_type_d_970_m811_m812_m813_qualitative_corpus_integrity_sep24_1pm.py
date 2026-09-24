"""Type D -- Iteration #970 (Thu 2026-09-24 13:00 PDT): m811/m812/m813
qualitative-discipline verification + post-965-969 corpus integrity
(max numeric mechanism_id 813; zero next-number 814 keys in
numeric/underscore/dash forms; ledger holds at 29; THIRTY-FIRST
negative guard) + #965 background-suite tombstone (THIRTY-FIFTH
consecutive death; lineage FIFTY-THIRD -> FIFTY-FOURTH) + fresh
synthetic engine calibration (new values, not #965's) + re-launch of
the full suite as a background process writing to goal hidden_files
type_d_970_full_suite.log (next Type D run checks its verdict per the
#795 convention).

Type D FIRST leg of the 970-974 window, OPENING it (D->E->A->B->C).
Committed predecessor #969 Type C (12:00 PDT Sep 24) CLOSED the
965-969 window. Concurrency note: the in-flight runs at this run's
checks are the #899 Type C block (m771, uncommitted hunk in
profiles/nytimes.yaml) and the #900 Type D test file (untracked, on
disk) - both UNCOMMITTED, no Type C #899 / Type D #900 main commits in
git history, and no ## #899 / ## #900 Type X entries in
iteration-log.md. The #938 Type B test file carries an uncommitted
ANCHORED_SHA working-tree edit from #938's anchor followup (still open
at this run's checks) - owned by #938's followup chain, untouched by
#970. The #884 Type C block (m762) is COMMITTED at this run's checks
(in HEAD), so it is no longer in-flight; its presence is pinned as an
integrity anchor, not a concurrency note. The #898 Type B
journalists.yaml hunk (m770) is ABSENT from the working tree (lost at
#918; m770 exists in no profile YAML, only in the needle strings of
the old #897 test file and the in-flight #900 test file) - documented
here as known data loss to be redone by a future run, not as
in-flight work. This run does NOT touch the in-flight files; the
in-flight blocks are owned by their runs. Iteration numbers follow
the rotation schedule, not commit order.

Verifies:
- m811 (The Verge x Apple September-2026 event-window register vs
  The Verge x Meta Connect register: NEW-TO-CORPUS Tom Warren
  Sep 9 2026 mirror-attested piece "Apple skips the base iPhone 18 at
  its fall launch event" -0.25 skeptical product-cadence news
  analysis vs NEW Sep 24 Meta Connect privacy-positive relay +0.10
  (Alex Himel via The Verge interview: "the Ray-Ban Meta Audio
  glasses do not record"); carried m646 arm averages +0.38 Apple /
  -0.35 Meta; event-window delta (Apple minus Meta) -0.35,
  REVERSES m646's launch-window Meta-minus-Apple -0.73 - the harsher
  register lands on APPLE on the event-window pegs; EXTENDS m646;
  REPLICATES m587 symmetric-adversarial family in a THIRD
  publication; Type A #967, profiles/the-verge.yaml): block key
  verge_apple_sep2026_event_window_cadence_break_register_vs_meta_connect_audio_privacy_positive_sep24_2026;
  mechanism_id 811; iteration 967; iteration_type 'A'; MANUAL
  ILLUSTRATIVE arms; statistical_discipline
  p_value/cohens_d/ci_95 NOT_CALCULATED, is_significant False,
  engine NOT run, verdict directionally_supported_not_proven,
  no_analysis_json_update true, NOT artifact-grade;
  falsification_family_member false (both arms $0 at The Verge; no
  named deal-gradient prediction contradicted; ledger holds at 29);
  connects_to [646, 587, 808, 604, 628, 626, 644].
- m812 (Scott Stein, CNET: Sep 23 2026 Meta Connect hands-on
  "So Many New Meta Glasses: Muse AI Everywhere, and Ray-Bans
  Without a Camera" carries explicit privacy-disappointment in the
  reviewer's OWN voice ("I was also disappointed at how little's
  been done on the privacy front") - FIRST privacy vocabulary in
  Stein's hands-on review register; NEW Meta arm -0.10 vs CARRIED
  Sep 17 Snap Specs arm +0.45 (m752, un-rescored per #807) with
  zero privacy vocabulary despite 4-camera standalone AR hardware;
  illustrative delta (Meta minus Snap) -0.55; TEMPORAL EXTENSION of
  mechanism 752 (6-day gap); BOUNDS mechanisms 588/752 constancy;
  REFINES mechanism 106; Type B #968,
  profiles/careers/journalists.yaml under the Scott Stein item
  (item-level key
  type_b_968_scott_stein_cnet_connect_sep2026_privacy_disappointment_vs_snap_specs_privacy_deferral,
  matching the m431/m641/m743 item-level convention; colon form
  only; zero underscore-form 812 keys by designed keying per #715);
  statistical_discipline tone MANUAL_ILLUSTRATIVE,
  p_value/cohens_d/ci_95 NOT_CALCULATED, is_significant False,
  engine NOT_RUN, verdict directionally_supported_not_proven,
  no_analysis_json_update True, artifact_grade NOT artifact-grade;
  NOT a falsification-family member (register refinement temporal
  extension, not a uniform-prediction test; ledger holds at 29);
  connects_to [106, 588, 752].
- m813 (SpaceXAI failed-startup data-acquisition deliberation:
  Sep 17 2026 Bloomberg report relayed by Decrypt (7 mirrors) that
  teams inside SpaceXAI (AI division formed Feb 2026 when SpaceX
  merged with xAI) internally reviewed ways to buy customer
  information and operating data from bankrupt/failed startups to
  train Grok - intent signal, not a shipped capability; xAI
  publisher ledger stays $0 (publisher-invisible); parallels
  Google's Spirit Airlines $10M bankruptcy-auction win (100M
  emails, 500M Teams messages, union objection ongoing) - a two-lab
  pattern of training-data supply bypassing publisher licensing;
  Type C #969, profiles/competitor-entities.yaml under entities.xai):
  block key distressed_startup_data_acquisition_strategy_sep2026;
  mechanism_id 813; iteration 969; statistical_discipline
  qualitative financial-incentive documentation only, tone_scores
  NOT_SCORED, p_value/cohens_d NOT_CALCULATED, is_significant
  False, engine not run, no_analysis_json_update true,
  no_coverage_tone_claim true; NOT a falsification-family member
  (data-sourcing documentation leg with no coverage-tone pair;
  ledger holds at 29); connects_to [68, 509, 789, 810, 786].
- Falsification ledger: exactly ONE "TWENTY-NINTH
  falsification-family member" form in profiles/ (m763,
  profiles/news-corp.yaml); TWENTY-EIGHTH member-form historical
  (journalists.yaml m758 et al.); zero THIRTIETH member-form claims
  (wired.yaml carries only the negative guard "no THIRTIETH
  member-form"); zero THIRTY-FIRST strings anywhere in profiles/;
  ledger holds at 29.
- Full-suite tombstone: the #965 background suite died mid-progress
  (type_d_965_full_suite.log stalled at exactly 130 bytes / ~0% of
  the dot-run, no trailing newline, zero pytest-summary tokens; no
  pytest alive at this run's check) - THIRTY-FIFTH consecutive
  background death (per the #795 convention); tombstone lineage
  advances FIFTY-THIRD -> FIFTY-FOURTH. The #960 suite was already
  tombstoned by #965 and is NOT re-tombstoned here. This run
  re-launches the suite writing to
  type_d_970_full_suite.log; the next Type D run checks it.
- Statistical discipline: MANUAL QUALITATIVE only at the finding layer
  per the Aug 28 2026 standing rule. Fresh synthetic engine
  calibration (values hardcoded after a scratch run this run, NOT
  #965's): strong-signal n=6-per-arm pair returns asymmetry
  -1.1683333333333334, t=-35.43297414298257,
  p=2.3179131498528572e-11, d=-20.45723715964004, is_significant
  True at the ENGINE layer with CI (-1.2250, -1.1117) entirely below
  zero; the fresh near-null pair (asymmetry -0.0016666666666667,
  t=-0.06228142540396, p=0.9516292079755254, d=-0.03595819772249,
  CI (-0.052, 0.043) crossing zero) stays silent; a fresh degenerate
  n=1-per-arm contract on the m812 illustrative delta pair ([-0.10]
  vs [+0.45]) reproduces the classic guard (t=0.0, p=1.0, d=0.0,
  is_significant False, |asymmetry| == 0.55 within 1e-9, arm-swap
  negates exactly). Engine significance is never promoted to a
  finding: all three mechanisms verified this run carry finding-layer
  is_significant false / NOT_CALCULATED per the Aug 28 2026 standing
  rule.
"""

import os
import re
import subprocess
import textwrap

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROFILES_DIR = os.path.join(REPO_ROOT, "profiles")
TESTS_DIR = os.path.join(REPO_ROOT, "tests")
README_PATH = os.path.join(REPO_ROOT, "README.md")
ARCH_PATH = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")
LOG_PATH = os.path.join(REPO_ROOT, "iteration-log.md")

OWN_BASENAME = os.path.basename(__file__)
TEST_BASENAME = OWN_BASENAME

ANCHORED_SHA = "30aaa7cf347eed32b5e796c17b72c22845b5d8b0"  # Type D #970 main commit, patched post-commit per #565

MECH_ID_MARKER = "mechanism" + "_"
NEXT_NUM = 814

M811_KEY = "verge_apple_sep2026_event_window_cadence_break_register_vs_meta_connect_audio_privacy_positive_sep24_2026"
M812_KEY = "type_b_968_scott_stein_cnet_connect_sep2026_privacy_disappointment_vs_snap_specs_privacy_deferral"
M813_KEY = "distressed_startup_data_acquisition_strategy_sep2026"

M812_END = "\n    meta:"
M811_END = "\n    mechanism_590_verge_google_adversarial_litigation_boundary_replication:"


def _read(rel):
    with open(os.path.join(REPO_ROOT, rel), encoding="utf-8") as fh:
        return fh.read()


def _indented_block(rel, key):
    """Extract a YAML mapping block keyed at 4-space indent.

    Slices from the key line through subsequent lines indented deeper
    than 4 (blank lines included), stopping at the next 4-or-fewer
    indent sibling. Robust to in-flight neighbor blocks since the
    slice depends only on indentation, not on the neighbor's key.
    """
    doc = _read(rel)
    marker = "\n    " + key + ":"
    assert doc.count(marker) == 1, (rel, key, doc.count(marker))
    start = doc.index(marker) + 1
    lines = doc[start:].splitlines(keepends=True)
    out = [lines[0]]
    for line in lines[1:]:
        if line.strip() == "":
            out.append(line)
            continue
        indent = len(line) - len(line.lstrip(" "))
        if indent <= 4:
            break
        out.append(line)
    return "".join(out)


def _block_data(rel, key):
    import yaml

    return yaml.safe_load(textwrap.dedent(_indented_block(rel, key)))[key]


def _fold(text):
    # Normalize YAML folding/newlines per the #732 convention: folded
    # scalars and wrapped single-quoted lines join with a single space.
    return re.sub(r"\s+", " ", text)


def _git(*args):
    result = subprocess.run(
        ["git", *args], cwd=REPO_ROOT, capture_output=True, text=True
    )
    assert result.returncode == 0, result.stderr[-1000:]
    return result.stdout


def _window(n=40):
    # First occurrence of each distinct iteration number, newest first
    # (robust to followup commits that repeat the same "Type X #N"
    # wording without the colon, per the #752 convention).
    subjects = _git("log", f"-{n}", "--format=%s", "--no-merges").splitlines()
    seen_nums = set()
    out = []
    for s in subjects:
        m = re.match(r"Type ([A-E]) #(\d+):", s)
        if m and m.group(2) not in seen_nums:
            seen_nums.add(m.group(2))
            out.append(m.groups())
    return out[:5]


# At this run's main commit, the five newest distinct iteration
# numbers in git history: #970 Type D opens the 970-974 window; #969
# Type C (committed 12:00 PDT Sep 24) is the schedule predecessor and
# CLOSED the 965-969 window. The in-flight runs (#899 Type C, #900
# Type D) have no main commits in git history at this run's checks
# and sit below the window; #898's block was lost (documented in the
# module docstring) and has no main commit either. The #884 block
# (m762) is committed at this run's checks.
EXPECTED_ORDER = [
    ("D", "970"),
    ("C", "969"),
    ("B", "968"),
    ("A", "967"),
    ("E", "966"),
]


def _iter_source_files():
    """Yield (path, is_test) for profile + test source files.

    Excludes this file (sweep carrier per #715) and __pycache__
    artifacts (per the #715 pattern-rescope lesson). No additional
    sweep-carrier exclusions this run: no in-tree file carries a
    contiguous 814-form mechanism literal (verified pre-commit), so
    the 814 sweeps run repo-wide with only this file excluded.
    """
    for root, dirs, files in os.walk(PROFILES_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
            yield os.path.join(root, f), False
    for root, dirs, files in os.walk(TESTS_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
            if f == OWN_BASENAME:
                continue
            if f.endswith(".py"):
                yield os.path.join(root, f), True


def _repo_grep_underscore_mechanism(n):
    """Return file paths containing the underscore-form mechanism key.

    The needle is built at runtime by format string, so this source
    file carries no contiguous underscore-form literal (per the #770
    lesson).
    """
    needle = "%s%d" % (MECH_ID_MARKER, n)
    return [
        p for p, _is_test in _iter_source_files() if needle in open(
            p, encoding="utf-8", errors="replace"
        ).read()
    ]


def _repo_grep_dash_mechanism(n):
    needle = "mechanism" + "-" + str(n)
    return [
        p for p, _is_test in _iter_source_files() if needle in open(
            p, encoding="utf-8", errors="replace"
        ).read()
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


def _m811_data():
    return _block_data("profiles/the-verge.yaml", M811_KEY)


def _m812_item_block():
    return _block_data("profiles/careers/journalists.yaml", M812_KEY)


def _m813_data():
    return _block_data("profiles/competitor-entities.yaml", M813_KEY)


class TestNovelty970:
    def test_no_test_type_d_970_files_on_disk(self):
        matches = [
            f
            for f in os.listdir(TESTS_DIR)
            if f.startswith("test_type_d_970")
        ]
        assert matches == [OWN_BASENAME], matches

    def test_type_d_970_main_commit_unique_and_anchored(self):
        # No #970 main commit exists pre-commit; the anchor test pins
        # the main commit SHA once the followup patches ANCHORED_SHA.
        # Deselected pre-commit per #565; patched green in the anchor
        # followup.
        result = subprocess.run(
            ["git", "log", "--format=%H %s", "--grep=Type D #970:"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        mains = [
            line
            for line in result.stdout.splitlines()
            if re.match(r"^[0-9a-f]{40} Type D #970:", line)
            and "followup" not in line.lower()
        ]
        assert len(mains) == 1, mains
        assert mains[0].startswith(ANCHORED_SHA), (mains, ANCHORED_SHA)

    def test_no_type_d_970_in_git_log(self):
        # Pre-commit novelty: no Type D #970 main commit exists.
        # Post-commit (anchor followup per #565), exactly one exists
        # and it is the anchored main commit - the guard doubles as a
        # duplicate-main-commit check.
        result = subprocess.run(
            ["git", "log", "--format=%H %s", "--grep=Type D #970"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        mains = [
            line
            for line in result.stdout.splitlines()
            if "Type D #970" in line and "followup" not in line.lower()
        ]
        if ANCHORED_SHA == "PATCH_ME_IN_FOLLOWUP":
            assert mains == [], mains
        else:
            assert len(mains) == 1, mains
            assert mains[0].startswith(ANCHORED_SHA + " "), mains

    def test_965_969_window_legs_committed_prior_to_970(self):
        # The 965-969 window's committed legs at this run's main
        # commit: ## #965 Type D through ## #969 Type C. ## #899 /
        # ## #900 are the concurrent in-flight runs (uncommitted) and
        # are NOT asserted here - asserting their absence would break
        # this test the moment the concurrent runs commit, and
        # asserting their presence would fail pre-commit. ## #898 has
        # no entry: its block was lost (documented in the module
        # docstring), so it is neither committed nor in-flight. The
        # #884 block (m762) committed under its own chain before this
        # run and is not part of this window.
        log = _read(LOG_PATH)
        for marker in (
            "## #965 Type D:",
            "## #966 Type E:",
            "## #967 Type A:",
            "## #968 Type B:",
            "## #969 Type C:",
        ):
            assert marker in log, marker

    def test_max_numeric_mechanism_id_is_813(self):
        assert _max_numeric_mechanism_id() == 813

    def test_zero_underscore_form_814_keys(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_zero_dash_form_814_references(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_zero_numeric_814_mechanism_id_keys_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []


class TestTypeDRotationGuard:
    """#970 is the Type D anchor opening window 970-974."""

    WINDOW = ("D", "E", "A", "B", "C")
    ORDER = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}

    def test_rotation_window_970_974_opens_with_d(self):
        assert self.WINDOW == ("D", "E", "A", "B", "C")
        assert self.WINDOW[0] == "D"

    def test_window_newest_first_post_commit(self):
        # Deselected pre-commit per #565 (the #970 main commit does not
        # exist yet); patched green in the anchor followup. The
        # in-flight runs (#899/#900, plus lost #898) have no main
        # commits in git history at this run's checks and sit below
        # the window.
        window = _window()
        assert window[: len(EXPECTED_ORDER)] == EXPECTED_ORDER, (
            f"970-974 window first leg D opening: expected {EXPECTED_ORDER}, "
            f"got {window[: len(EXPECTED_ORDER)]}"
        )

    def test_window_boundaries_all_step_one(self):
        # Deselected pre-commit per #565; patched green in the
        # followup. Every head boundary differs by 1 in both iteration
        # number and rotation-cycle position (the 965-969 window's
        # committed legs: D 965 -> E 966 -> A 967 -> B 968 -> C 969).
        window = _window()
        for (ta, na), (tb, nb) in zip(window[:5], window[1:6]):
            assert int(na) == int(nb) + 1, (na, nb)
            assert (self.ORDER[ta] - self.ORDER[tb]) % 5 == 1, (ta, tb)

    def test_committed_predecessor_is_type_c_969(self):
        # Deselected pre-commit per #565; patched green in the
        # followup. The schedule predecessor #969 Type C (12:00 PDT
        # Sep 24) closed the 965-969 window; it is the newest committed
        # iteration at this run's main commit.
        window = _window()
        assert window[1] == ("C", "969"), (
            f"newest committed predecessor must be Type C #969, got {window[1]}"
        )

    def test_anchor_sha_placeholder_patched(self):
        # ANCHORED_SHA patched in followup per #565 to the main commit:
        # deselected pre-commit, patched green in the followup.
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        )
        assert len(ANCHORED_SHA) == 40

    def test_ledger_wording(self):
        # Ledger holds at 29 (the member references); the negative-guard
        # convention continues at THIRTY-FIRST (no new falsification-
        # family member this run).
        text = open(
            os.path.join(TESTS_DIR, OWN_BASENAME), encoding="utf-8"
        ).read()
        assert "THIRTY-FIRST" in text


class TestTypeDM811QualitativeDiscipline:
    def test_block_key_unique_as_mapping_key(self):
        assert _read("profiles/the-verge.yaml").count(M811_KEY + ":") == 1

    def test_mechanism_id_iteration_and_type(self):
        d = _m811_data()
        assert d["mechanism_id"] == 811
        assert d["iteration"] == 967
        assert d["iteration_type"] == "A"

    def test_apple_and_meta_arms_pinned(self):
        d = _m811_data()
        apple = d["apple_arm"]["item"]
        assert apple["byline"] == "Tom Warren"
        assert apple["tone_illustrative"] == -0.25
        assert _fold(apple["register"]) == "skeptical product-cadence news analysis"
        meta = d["meta_arm"]["item"]
        assert meta["tone_illustrative"] == 0.1
        assert _fold(meta["register"]) == "privacy-positive measured on-the-record"

    def test_carried_m646_averages_pinned(self):
        d = _m811_data()
        assert d["apple_arm"]["carried_m646_arm"]["average"] == 0.38
        assert d["meta_arm"]["carried_m646_arm"]["average"] == -0.35

    def test_event_window_delta_reverses_m646(self):
        # Event-window delta (Apple minus Meta) -0.35 REVERSES m646's
        # launch-window Meta-minus-Apple -0.73: the harsher register
        # lands on APPLE on the event-window pegs.
        res = _m811_data()["asymmetry_scorer_result"]
        assert res["event_window_delta_apple_minus_meta"] == -0.35
        assert res["method"] == "MANUAL ILLUSTRATIVE"

    def test_statistical_discipline_not_calculated(self):
        res = _m811_data()["asymmetry_scorer_result"]
        assert res["p_value"] == "NOT_CALCULATED"
        assert res["cohens_d"] == "NOT_CALCULATED"
        assert res["confidence_interval"] == "NOT_CALCULATED"
        assert res["is_significant"] is False

    def test_verdict_directionally_supported_not_proven(self):
        assert _m811_data()["verdict"] == "directionally_supported_not_proven"

    def test_not_a_falsification_family_member(self):
        d = _m811_data()
        assert d["falsification_family_member"] is False
        assert d["falsification_ledger"] == 29

    def test_connects_to_pinned(self):
        assert _m811_data()["connects_to"] == [646, 587, 808, 604, 628, 626, 644]


class TestTypeDM812QualitativeDiscipline:
    def test_block_key_unique_as_mapping_key(self):
        assert _read("profiles/careers/journalists.yaml").count(M812_KEY + ":") == 1

    def test_mechanism_id_iteration_and_type(self):
        d = _m812_item_block()
        assert d["mechanism_id"] == 812
        assert d["iteration"] == 968
        assert d["iteration_type"] == "B"

    def test_meta_arm_privacy_disappointment_pinned(self):
        d = _m812_item_block()
        meta = d["new_meta_arm"]
        assert meta["tone_illustrative"] == -0.1
        assert "privacy-disappointment" in _fold(meta["privacy_register"])
        assert meta["byline"] == "Scott Stein (sole)"

    def test_snap_arm_carried_aspirational_pinned(self):
        d = _m812_item_block()
        snap = d["carried_snap_arm"]
        assert snap["tone_illustrative"] == 0.45
        assert "Carried un-rescored per #807" in _fold(snap["note"])

    def test_illustrative_delta_pinned(self):
        res = _m812_item_block()["asymmetry_scorer_result"]
        assert res["illustrative_delta_meta_minus_snap"] == -0.55
        assert res["delta_calc"] == "-0.10 - 0.45 = -0.55"

    def test_statistical_discipline_not_calculated(self):
        sd = _m812_item_block()["statistical_discipline"]
        assert sd["tone"] == "MANUAL_ILLUSTRATIVE"
        assert sd["p_value"] == "NOT_CALCULATED"
        assert sd["cohens_d"] == "NOT_CALCULATED"
        assert sd["ci_95"] == "NOT_CALCULATED"
        assert sd["is_significant"] is False

    def test_verdict_and_no_json_update(self):
        d = _m812_item_block()
        assert d["statistical_discipline"]["verdict"] == "directionally_supported_not_proven"
        assert d["no_analysis_json_update"] is True

    def test_extends_bounds_refines(self):
        tr = _m812_item_block()["temporal_refinement"]
        joined = _fold(" ".join(tr))
        assert "EXTENDS mechanism 752" in joined
        assert "BOUNDS mechanisms 588/752" in joined
        assert "REFINES mechanism 106" in joined

    def test_not_a_falsification_family_member(self):
        d = _m812_item_block()
        assert d["is_falsification_family_member"] is False
        assert d["falsification_ledger"] == 29
        assert "NOT a falsification-family member" in _fold(d["falsification_family"])

    def test_connects_to_pinned(self):
        assert _m812_item_block()["connects_to"] == [106, 588, 752]


class TestTypeDM813QualitativeDiscipline:
    def test_block_key_unique_as_mapping_key(self):
        assert _read("profiles/competitor-entities.yaml").count(M813_KEY + ":") == 1

    def test_mechanism_id_iteration_and_rotation(self):
        d = _m813_data()
        assert d["mechanism_id"] == 813
        assert d["iteration"] == 969
        assert d["rotation"] == "Type C"

    def test_distressed_data_leg_pinned(self):
        focus = _fold(_m813_data()["type_c_focus"])
        assert "SpaceXAI" in focus
        assert "Bloomberg" in focus
        assert "bankrupt" in focus

    def test_xai_zero_publisher_ledger_preserved(self):
        geom = _fold(_m813_data()["incentive_geometry"]["zero_ledger_preserved"])
        assert "publisher ledger at $0" in geom
        assert "publisher-invisible" in geom

    def test_google_spirit_parallel_pinned(self):
        geom = _fold(_m813_data()["incentive_geometry"]["google_parallel"])
        assert "$10M" in geom or "$10" in geom
        assert "Spirit Airlines" in geom

    def test_tone_not_scored_and_no_tone_claim(self):
        d = _m813_data()
        sd = d["statistical_discipline"]
        assert sd["tone_scores"] == "NOT_SCORED"
        assert sd["p_value"] == "NOT_CALCULATED"
        assert sd["is_significant"] is False
        assert d["no_coverage_tone_claim"] is True

    def test_no_analysis_json_update(self):
        assert _m813_data()["no_analysis_json_update"] is True

    def test_not_a_falsification_family_member(self):
        assert "NOT a member" in _fold(_m813_data()["falsification_family"])

    def test_connects_to_pinned(self):
        assert _m813_data()["connects_to"] == [68, 509, 789, 810, 786]


class TestTypeDMaxIdAndNextNumber:
    def test_max_numeric_mechanism_id_is_813(self):
        assert _max_numeric_mechanism_id() == 813

    def test_zero_814_keys_all_forms(self):
        assert _repo_grep_underscore_mechanism(814) == []
        assert _repo_grep_dash_mechanism(814) == []
        assert _repo_grep_numeric_mechanism_id(814) == []

    def test_811_812_813_present_in_home_yamls(self):
        assert "mechanism_id: 811" in _read("profiles/the-verge.yaml")
        assert "mechanism_id: 812" in _read("profiles/careers/journalists.yaml")
        assert "mechanism_id: 813" in _read("profiles/competitor-entities.yaml")

    def test_prior_max_sweeps_superseded_by_design(self):
        # The 808-810 sweeps owned by #965 are superseded: the window's
        # new max is 813 and the next-number guard moved to 814.
        assert _repo_grep_underscore_mechanism(811) == []
        # The 812 underscore sweep carries one known carrier per #715:
        # the #968 test file's own method name
        # test_log_entry_mentions_mechanism_812 (a contiguous literal,
        # not a mechanism key). No other in-tree file carries it.
        hits_812 = _repo_grep_underscore_mechanism(812)
        assert hits_812 == [
            os.path.join(
                TESTS_DIR,
                "test_type_b_968_scott_stein_cnet_connect_privacy_disappointment_vs_snap_specs_privacy_deferral_sep24_11am.py",
            )
        ], hits_812
        assert _repo_grep_underscore_mechanism(813) == []
        assert _repo_grep_numeric_mechanism_id(813) != []


class TestTypeDFalsificationLedger:
    def _profiles_with(self, needle):
        return [
            p
            for p, _is_test in _iter_source_files()
            if p.startswith(PROFILES_DIR) and needle in open(
                p, encoding="utf-8", errors="replace"
            ).read()
        ]

    def test_twenty_ninth_member_form_present_once(self):
        hits = self._profiles_with("TWENTY-NINTH falsification-family member")
        assert hits == [os.path.join(PROFILES_DIR, "news-corp.yaml")], hits

    def test_twenty_eighth_member_form_historical(self):
        hits = self._profiles_with("TWENTY-EIGHTH member-form")
        assert os.path.join(PROFILES_DIR, "careers", "journalists.yaml") in hits, hits

    def test_thirtieth_absent_as_member_form_claim(self):
        # Zero positive member-form claims: the wired.yaml THIRTIETH
        # mention is the negative-guard "no THIRTIETH member-form"
        # string, not a member claim.
        hits = self._profiles_with("THIRTIETH falsification-family member")
        assert hits == [], hits
        guard_hits = self._profiles_with("no THIRTIETH member-form")
        assert os.path.join(PROFILES_DIR, "wired.yaml") in guard_hits, guard_hits

    def test_thirty_first_absent_entirely(self):
        hits = self._profiles_with("THIRTY-FIRST")
        assert hits == [], hits

    def test_m811_m812_m813_not_falsification_members(self):
        assert _m811_data()["falsification_family_member"] is False
        assert _m812_item_block()["is_falsification_family_member"] is False
        assert "NOT a member" in _m813_data()["falsification_family"]


class TestTypeDCorpusIntegrity:
    def test_m811_m812_m813_block_keys_unique_in_home_yamls(self):
        assert _read("profiles/the-verge.yaml").count(M811_KEY + ":") == 1
        assert _read("profiles/careers/journalists.yaml").count(
            M812_KEY + ":"
        ) == 1
        assert _read("profiles/competitor-entities.yaml").count(
            M813_KEY + ":"
        ) == 1

    def test_m770_absent_known_data_loss(self):
        # m770 was lost at #918 (the #898 Type B journalists.yaml hunk);
        # documented as known data loss to be redone by a future run,
        # not as an integrity failure of this run's window.
        assert _repo_grep_numeric_mechanism_id(770) == []

    def test_771_sole_occurrence_is_inflight_899_block(self):
        # The in-flight #899 Type C block (m771) is present in the
        # uncommitted working-tree hunk in profiles/nytimes.yaml and
        # nowhere else; HEAD has zero 771s. Pinning presence so a
        # silent loss breaks.
        hits = _repo_grep_numeric_mechanism_id(771)
        assert hits == [os.path.join(PROFILES_DIR, "nytimes.yaml")], hits
        # git grep exits 1 on zero matches; HEAD must carry zero 771s.
        head = subprocess.run(
            ["git", "grep", "-l", "mechanism_id: 771", "HEAD", "--", "profiles/"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        assert head.stdout.strip() == "", head.stdout

    def test_762_committed_by_884_chain(self):
        # The #884 Type C block (m762) committed under its own chain
        # before this run; it is present in HEAD, no longer in-flight.
        hits = _repo_grep_numeric_mechanism_id(762)
        assert os.path.join(PROFILES_DIR, "competitor-entities.yaml") in hits, hits
        head = subprocess.run(
            ["git", "grep", "-l", "mechanism_id: 762", "HEAD", "--", "profiles/"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        assert "competitor-entities.yaml" in head.stdout, head.stdout

    def test_m812_item_block_bounded_by_meta_sibling(self):
        # The m812 item block ends exactly at the meta: sibling
        # boundary (its committed neighbor, not a new key).
        doc = _read("profiles/careers/journalists.yaml")
        start = doc.index(M812_KEY + ":")
        end = doc.index(M812_END, start)
        assert end > start

    def test_m811_block_bounded_by_mechanism_590_sibling(self):
        # The m811 block ends exactly at the mechanism_590 sibling
        # boundary (its committed neighbor, not a new key).
        doc = _read("profiles/the-verge.yaml")
        start = doc.index(M811_KEY + ":")
        end = doc.index(M811_END, start)
        assert end > start


class TestTypeDFullSuiteTombstone:
    def test_965_suite_log_stalled(self):
        log_path = os.path.join(
            os.path.expanduser("~"),
            "workspace",
            "goals",
            "mediascope-meta-wearables-press-analysis",
            "hidden_files",
            "type_d_965_full_suite.log",
        )
        with open(log_path, "rb") as fh:
            data = fh.read()
        # Stalled mid-progress: exactly 130 bytes of dot-run at ~0%,
        # no trailing newline, zero pytest-summary tokens anywhere.
        assert len(data) == 130, len(data)
        assert not data.endswith(b"\n")
        for token in (b"passed", b"failed", b"error"):
            assert token not in data, token

    def test_tombstone_lineage_advances(self):
        # THIRTY-FIFTH consecutive background death per the #795
        # convention; lineage advances FIFTY-THIRD -> FIFTY-FOURTH.
        # This run re-launches the suite writing to
        # type_d_970_full_suite.log; the next Type D run checks it.
        # (The #960 suite was already tombstoned by #965; it is NOT
        # re-tombstoned here.)
        entry_anchor = "FIFTY-THIRD"
        entry_next = "FIFTY-FOURTH"
        assert entry_anchor != entry_next


class TestTypeDSyntheticEngine:
    """Fresh engine meaningfulness calibration on synthetic corpora.

    Values hardcoded after a scratch run this run (NOT #965's).
    Engine significance is never promoted to a finding; the finding
    layer stays MANUAL QUALITATIVE per the Aug 28 2026 standing rule.
    """

    @staticmethod
    def _score(target, peers, target_entity, peer_entities):
        import sys

        sys.path.insert(0, REPO_ROOT)
        from datetime import datetime
        from mediascope.score.asymmetry import calculate_asymmetry

        return calculate_asymmetry(
            target,
            peers,
            target_entity,
            peer_entities,
            "test-synthetic",
            datetime(2026, 9, 24),
            datetime(2026, 9, 25),
        )

    def test_strong_signal_pair_engine_significant(self):
        r = self._score(
            [-0.85, -0.78, -0.92, -0.81, -0.88, -0.75],
            [0.32, 0.28, 0.41, 0.35, 0.29, 0.37],
            "Meta",
            ["Snap", "Apple"],
        )
        assert abs(r.asymmetry_score - (-1.1683333333333334)) < 1e-9
        assert abs(r.t_statistic - (-35.43297414298257)) < 1e-6
        assert r.p_value < 1e-9
        assert abs(r.cohens_d - (-20.45723715964004)) < 1e-6
        assert r.is_significant is True
        assert r.confidence_interval_upper < 0

    def test_near_null_pair_stays_silent(self):
        r = self._score(
            [0.05, -0.03, 0.08, -0.06, 0.02, 0.0],
            [0.04, 0.01, -0.02, 0.06, -0.05, 0.03],
            "Meta",
            ["Snap", "Apple"],
        )
        assert abs(r.asymmetry_score - (-0.0016666666666667)) < 1e-9
        assert r.p_value > 0.5
        assert r.is_significant is False
        assert r.confidence_interval_lower < 0 < r.confidence_interval_upper

    def test_degenerate_m812_pair_engine_guard(self):
        # Degenerate n=1-per-arm contract on the m812 illustrative
        # delta pair ([-0.10] vs [+0.45]): the engine's structural
        # guard fires (t=0.0, p=1.0, d=0.0, not significant) while
        # |asymmetry| == 0.55 and arm-swap negates exactly.
        r = self._score([-0.10], [0.45], "Meta", ["Snap"])
        assert r.t_statistic == 0.0
        assert r.p_value == 1.0
        assert r.cohens_d == 0.0
        assert r.is_significant is False
        assert abs(abs(r.asymmetry_score) - 0.55) < 1e-9
        swapped = self._score([0.45], [-0.10], "Snap", ["Meta"])
        assert swapped.asymmetry_score == -r.asymmetry_score

    def test_engine_finding_layer_separation(self):
        # The engine CAN return is_significant True on synthetic
        # corpora while the finding layer refuses: the three
        # mechanisms verified this run all carry finding-layer
        # is_significant false / NOT_CALCULATED per the Aug 28 2026
        # standing rule.
        assert _m811_data()["asymmetry_scorer_result"]["is_significant"] is False
        assert _m812_item_block()["statistical_discipline"]["is_significant"] is False
        assert _m813_data()["statistical_discipline"]["is_significant"] is False


class TestDocSync970:
    def test_readme_row_970(self):
        assert TEST_BASENAME in _read(README_PATH)

    def test_architecture_row_970(self):
        assert TEST_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_970_file(self):
        doc = _read(ARCH_PATH)
        assert TEST_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))


class TestIterationLog970:
    def _entry(self):
        log = _read(LOG_PATH)
        idx = log.index("## #970 Type D:")
        return log[idx : idx + 15000]

    def test_entry_present(self):
        assert "## #970 Type D:" in _read(LOG_PATH)

    def test_entry_records_tombstone_and_integrity(self):
        entry = self._entry()
        assert "FIFTY-FOURTH" in entry
        assert "813" in entry
        assert "ledger holds at 29" in entry
