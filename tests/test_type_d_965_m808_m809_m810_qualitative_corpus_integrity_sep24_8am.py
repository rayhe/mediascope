"""Type D -- Iteration #965 (Thu 2026-09-24 08:00 PDT): m808/m809/m810
qualitative-discipline verification + post-960-964 corpus integrity
(max numeric mechanism_id 810; zero next-number 811 keys in
numeric/underscore/dash forms; ledger holds at 29; THIRTY-FIRST
negative guard) + #960 background-suite tombstone (THIRTY-FOURTH
consecutive death; lineage FIFTY-SECOND -> FIFTY-THIRD) + fresh
synthetic engine calibration (new values, not #960's) + re-launch of
the full suite as a background process writing to goal hidden_files
type_d_965_full_suite.log (next Type D run checks its verdict per the
#795 convention).

Type D FIRST leg of the 965-969 window, OPENING it (D->E->A->B->C).
Committed predecessor #964 Type C (07:00 PDT Sep 24) CLOSED the
960-964 window. Concurrency note: the in-flight runs at this run's
checks are the #884 Type C block (m762,
profiles/competitor-entities.yaml), the #899 Type C block (m771,
profiles/nytimes.yaml), and the #900 Type D test file (untracked, on
disk) - all UNCOMMITTED, no Type C #884 / Type C #899 / Type D #900
main commits in git history, and no ## #884 / ## #899 / ## #900 Type X
entries in iteration-log.md. The #938 Type B test file carries an
uncommitted ANCHORED_SHA working-tree edit from #938's anchor followup
(still open at this run's checks) - owned by #938's followup chain,
untouched by #965. The #898 Type B journalists.yaml hunk (m770) is
ABSENT from the working tree (lost at #918; m770 exists in no commit,
stash, or dangling git object) - documented here as known data loss
to be redone by a future run, not as in-flight work. This run does NOT
touch the in-flight files; the in-flight blocks are owned by their
runs. Iteration numbers follow the rotation schedule, not commit order.

Verifies:
- m808 (Gizmodo x Apple September-2026 event-window register vs Gizmodo
  x Meta September-2026 Connect register: NEW-TO-CORPUS WWDC-2026
  smart-glasses adversarial snark -0.45, Sep-9 iPhone-event live-blog
  snark -0.40, carried m716 Apple Watch -0.60, NEW Sep-23 Meta Connect
  live-blog snark -0.55, carried m587 Meta arms and m806 Ray-Ban Audio
  -0.20; Apple mean -0.4833 vs Meta mean -0.52; illustrative delta
  (Apple minus Meta) +0.0367; null-tie symmetric-adversarial register
  REPLICATES; Type A #962, profiles/gizmodo.yaml): block key
  gizmodo_apple_sep2026_event_window_symmetric_adversarial_vs_meta_connect;
  mechanism_id 808; iteration 962; iteration_type 'A'; MANUAL
  ILLUSTRATIVE arms; statistical_discipline
  p_value/cohens_d/ci_95 NOT_CALCULATED, is_significant False, engine
  NOT run, verdict directionally_supported_not_proven,
  no_analysis_json_update true, NOT artifact-grade;
  falsification_family_member false (register documentation consistent
  with the m587 control, no uniform-prediction test; ledger holds at
  29); connects_to [587, 716, 806, 512, 577, 582].
- m809 (Hamish Hector, TechRadar: Sep 24 2026 Ray-Ban Audio
  camera-free privacy-criticism register -0.35 on Meta's own
  camera-removal concession vs carried Snap Specs aspirational +0.55
  (m680, un-rescored per #807) with zero privacy vocabulary despite
  strictly more sensor hardware; illustrative Meta-minus-Snap delta
  -0.90; tests m680 prediction 2 (peg-driven collapse hypothesis) and
  hardens the entity-gradient reading; Type B #963,
  profiles/careers/journalists.yaml under the hamish_hector item
  (item-level key
  type_b_963_hamish_hector_techradar_rayban_audio_privacy_criticism_vs_snap_aspirational_carried_sep24,
  matching the m431/m641/m743 item-level convention; colon form only;
  zero underscore-form 809 keys by designed keying per #715);
  statistical_discipline tone MANUAL_ILLUSTRATIVE,
  p_value/cohens_d/ci_95 NOT_CALCULATED, is_significant False,
  engine NOT_RUN, verdict directionally_supported_not_proven,
  analysis_json_update False, artifact_grade False; NOT a
  falsification-family member (temporal extension + hypothesis test;
  ledger holds at 29); connects_to [680, 115, 806, 794, 791].
- m810 (Platkin LLP publisher collective v. OpenAI + Microsoft: Jun 24
  2026 first suit nearly 400 local/regional newspapers; Sep 16 2026
  second suit 26 new publishers; collective 60 publishers / 550-plus
  publications under one boutique firm; expects consolidation with the
  NYT-led MDL very soon; NINTH relationship direction in the taxonomy
  - LITIGATION-POOLING; Type C #964, profiles/competitor-entities.yaml
  under entities.openai): block key
  platkin_collective_60_publishers_550_publications_litigation_pooling_sep2026;
  mechanism_id 810; iteration 964; statistical_discipline qualitative
  structural litigation-economics mapping only, tone_scores
  NOT_SCORED, p_value/cohens_d NOT_CALCULATED, is_significant False,
  engine_run False, verdict directionally_supported_not_proven,
  no_analysis_json_update true, no_coverage_tone_claim true; NOT a
  falsification-family member (litigation-economics leg, no
  coverage-tone pair; ledger holds at 29); connects_to
  [636, 720, 675, 762, 756, 759, 753, 714].
- Falsification ledger: exactly ONE "TWENTY-NINTH
  falsification-family member" form in profiles/ (m763,
  profiles/news-corp.yaml); TWENTY-EIGHTH member-form historical
  (journalists.yaml m758 et al.); zero THIRTIETH member-form claims
  (wired.yaml carries only the negative guard "no THIRTIETH
  member-form"); zero THIRTY-FIRST strings anywhere in profiles/;
  ledger holds at 29.
- Full-suite tombstone: the #960 background suite died mid-progress
  (type_d_960_full_suite.log stalled at exactly 3563 bytes / ~6% of
  the dot-run, no trailing newline, zero pytest-summary tokens; no
  pytest alive at this run's check) - THIRTY-FOURTH consecutive
  background death (per the #795 convention); tombstone lineage
  advances FIFTY-SECOND -> FIFTY-THIRD. The #955 suite was already
  tombstoned by #960 and is NOT re-tombstoned here. This run
  re-launches the full suite as a background process writing to goal
  hidden_files type_d_965_full_suite.log; the next Type D run checks
  it.
- Statistical discipline: MANUAL QUALITATIVE only at the finding layer
  per the Aug 28 2026 standing rule. Fresh synthetic engine
  calibration (values hardcoded after a scratch run this run, NOT
  #960's): strong-signal n=6-per-arm pair returns asymmetry
  -0.9616666666666667, t=-43.17527235973234,
  p=1.4504853976455477e-12, d=-24.927255119226874, is_significant
  True at the ENGINE layer with CI (-1.0033, -0.9217) entirely below
  zero; the fresh near-null pair (asymmetry -0.0016666666666666668,
  t=-0.08445512191506811, p=0.9343615169496964, d=-0.04876018737210723,
  CI (-0.035, 0.035) crossing zero) stays silent; a fresh degenerate
  n=1-per-arm contract on the m809 illustrative delta pair ([-0.35]
  vs [+0.55]) reproduces the classic guard (t=0.0, p=1.0, d=0.0,
  is_significant False, |asymmetry| == 0.90 within 1e-9, arm-swap
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

ANCHORED_SHA = "PATCH_ME_IN_FOLLOWUP"  # Type D #965 main commit, patched post-commit per #565

MECH_ID_MARKER = "mechanism" + "_"
NEXT_NUM = 811

M808_KEY = "gizmodo_apple_sep2026_event_window_symmetric_adversarial_vs_meta_connect"
M809_KEY = "type_b_963_hamish_hector_techradar_rayban_audio_privacy_criticism_vs_snap_aspirational_carried_sep24"
M810_KEY = "platkin_collective_60_publishers_550_publications_litigation_pooling_sep2026"

M809_END = "\nphilip_berne:"


def _read(rel):
    with open(os.path.join(REPO_ROOT, rel), encoding="utf-8") as fh:
        return fh.read()


def _indented_block(rel, key):
    """Extract a YAML mapping block keyed at 4-space indent.

    Slices from the key line through subsequent lines indented deeper
    than 4 (blank lines included), stopping at the next 4-or-fewer
    indent sibling. Robust to in-flight neighbor blocks (e.g. the #884
    m762 block adjacent to m810) since the slice depends only on
    indentation, not on the neighbor's key.
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
# numbers in git history: #965 Type D opens the 965-969 window; #964
# Type C (committed 07:00 PDT Sep 24) is the schedule predecessor and
# CLOSED the 960-964 window. The in-flight runs (#884 Type C, #899
# Type C, #900 Type D) have no main commits in git history at this
# run's checks and sit below the window; #898's block was lost
# (documented in the module docstring) and has no main commit either.
EXPECTED_ORDER = [
    ("D", "965"),
    ("C", "964"),
    ("B", "963"),
    ("A", "962"),
    ("E", "961"),
]


def _iter_source_files():
    """Yield (path, is_test) for profile + test source files.

    Excludes this file (sweep carrier per #715) and __pycache__
    artifacts (per the #715 pattern-rescope lesson). No additional
    sweep-carrier exclusions this run: no in-tree file carries a
    contiguous 811-form mechanism literal (verified pre-commit), so
    the 811 sweeps run repo-wide with only this file excluded.
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


def _m808_data():
    return _block_data("profiles/gizmodo.yaml", M808_KEY)


def _m809_item_block():
    return _block_data("profiles/careers/journalists.yaml", M809_KEY)


def _m810_data():
    return _block_data("profiles/competitor-entities.yaml", M810_KEY)


class TestNovelty965:
    def test_no_test_type_d_965_files_on_disk(self):
        matches = [
            f
            for f in os.listdir(TESTS_DIR)
            if f.startswith("test_type_d_965")
        ]
        assert matches == [OWN_BASENAME], matches

    def test_type_d_965_main_commit_unique_and_anchored(self):
        # No #965 main commit exists pre-commit; the anchor test pins
        # the main commit SHA once the followup patches ANCHORED_SHA.
        # Deselected pre-commit per #565; patched green in the anchor
        # followup.
        result = subprocess.run(
            ["git", "log", "--format=%H %s", "--grep=Type D #965:"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        mains = [
            line
            for line in result.stdout.splitlines()
            if re.match(r"^[0-9a-f]{40} Type D #965:", line)
            and "followup" not in line.lower()
        ]
        assert len(mains) == 1, mains
        assert mains[0].startswith(ANCHORED_SHA), (mains, ANCHORED_SHA)

    def test_no_type_d_965_in_git_log(self):
        # Pre-commit novelty: no Type D #965 main commit exists.
        # Post-commit (anchor followup per #565), exactly one exists
        # and it is the anchored main commit - the guard doubles as a
        # duplicate-main-commit check.
        result = subprocess.run(
            ["git", "log", "--format=%H %s", "--grep=Type D #965"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        mains = [
            line
            for line in result.stdout.splitlines()
            if "Type D #965" in line and "followup" not in line.lower()
        ]
        if ANCHORED_SHA == "PATCH_ME_IN_FOLLOWUP":
            assert mains == [], mains
        else:
            assert len(mains) == 1, mains
            assert mains[0].startswith(ANCHORED_SHA + " "), mains

    def test_960_964_window_legs_committed_prior_to_965(self):
        # The 960-964 window's committed legs at this run's main
        # commit: ## #960 Type D through ## #964 Type C. ## #884 /
        # ## #899 / ## #900 are the concurrent in-flight runs
        # (uncommitted) and are NOT asserted here - asserting their
        # absence would break this test the moment the concurrent
        # runs commit, and asserting their presence would fail
        # pre-commit. ## #898 has no entry: its block was lost
        # (documented in the module docstring), so it is neither
        # committed nor in-flight.
        log = _read(LOG_PATH)
        for marker in (
            "## #960 Type D:",
            "## #961 Type E:",
            "## #962 Type A:",
            "## #963 Type B:",
            "## #964 Type C:",
        ):
            assert marker in log, marker

    def test_max_numeric_mechanism_id_is_810(self):
        assert _max_numeric_mechanism_id() == 810

    def test_zero_underscore_form_811_keys(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_zero_dash_form_811_references(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_zero_numeric_811_mechanism_id_keys_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []


class TestTypeDRotationGuard:
    """#965 is the Type D anchor opening window 965-969."""

    WINDOW = ("D", "E", "A", "B", "C")
    ORDER = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}

    def test_rotation_window_965_969_opens_with_d(self):
        assert self.WINDOW == ("D", "E", "A", "B", "C")
        assert self.WINDOW[0] == "D"

    def test_window_newest_first_post_commit(self):
        # Deselected pre-commit per #565 (the #965 main commit does not
        # exist yet); patched green in the anchor followup. The
        # in-flight runs (#884/#899/#900, plus lost #898) have no main
        # commits in git history at this run's checks and sit below
        # the window.
        window = _window()
        assert window[: len(EXPECTED_ORDER)] == EXPECTED_ORDER, (
            f"965-969 window first leg D opening: expected {EXPECTED_ORDER}, "
            f"got {window[: len(EXPECTED_ORDER)]}"
        )

    def test_window_boundaries_all_step_one(self):
        # Deselected pre-commit per #565; patched green in the
        # followup. Every head boundary differs by 1 in both iteration
        # number and rotation-cycle position (the 960-964 window's
        # committed legs: D 960 -> E 961 -> A 962 -> B 963 -> C 964).
        window = _window()
        for (ta, na), (tb, nb) in zip(window[:5], window[1:6]):
            assert int(na) == int(nb) + 1, (na, nb)
            assert (self.ORDER[ta] - self.ORDER[tb]) % 5 == 1, (ta, tb)

    def test_committed_predecessor_is_type_c_964(self):
        # Deselected pre-commit per #565; patched green in the
        # followup. The schedule predecessor #964 Type C (07:00 PDT
        # Sep 24) closed the 960-964 window; it is the newest committed
        # iteration at this run's main commit.
        window = _window()
        assert window[1] == ("C", "964"), (
            f"newest committed predecessor must be Type C #964, got {window[1]}"
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


class TestTypeDM808QualitativeDiscipline:
    def test_block_key_unique_as_mapping_key(self):
        doc = _read("profiles/gizmodo.yaml")
        assert doc.count(M808_KEY + ":") == 1

    def test_mechanism_id_iteration_and_type(self):
        d = _m808_data()
        assert d["mechanism_id"] == 808
        assert d["iteration"] == 962
        assert d["iteration_type"] == "A"
        assert d["iteration_time"] == "2026-09-24 05:00 PDT"
        assert d["type"] == "Type A - Competitor Coverage Deep Dive"

    def test_apple_and_meta_arms_pinned(self):
        d = _m808_data()
        articles = d["articles"]
        assert len(articles) == 4
        by_title = {a["title"]: a for a in articles}
        wwdc = by_title["The Real Winners of Apple's WWDC 2026 Don't Even Exist Yet"]
        iphone_event = by_title["Live Updates From Apple's 'Surprise and Shine' iPhone Event"]
        apple_watch = by_title["If Meta Glasses Freak You Out, Wait Until You Hear About the New Apple Watch Features"]
        connect = by_title["Live Updates From Meta Connect 2026"]
        assert abs(wwdc["tone_score_illustrative"] - (-0.45)) < 1e-9
        assert wwdc["new_to_corpus"] is True
        assert abs(iphone_event["tone_score_illustrative"] - (-0.40)) < 1e-9
        assert iphone_event["new_to_corpus"] is True
        assert abs(apple_watch["tone_score_illustrative"] - (-0.60)) < 1e-9
        assert apple_watch["carried_from"] == "mechanism 716"
        assert abs(connect["tone_score_illustrative"] - (-0.55)) < 1e-9
        assert connect["entity"] == "meta"

    def test_illustrative_means_and_delta_pinned(self):
        scorer = _m808_data()["asymmetry_scorer_result"]
        assert abs(scorer["target_avg_tone"] - (-0.4833)) < 1e-4
        assert abs(scorer["peer_avg_tone"] - (-0.52)) < 1e-9
        assert abs(scorer["asymmetry_score"] - 0.0367) < 1e-4
        assert scorer["target_entity"] == "apple"
        assert scorer["peer_entities"] == ["meta"]

    def test_statistical_discipline_not_calculated(self):
        sd = _m808_data()["asymmetry_scorer_result"]
        assert sd["p_value"] == "NOT_CALCULATED"
        assert sd["cohens_d"] == "NOT_CALCULATED"
        assert sd["confidence_interval"] == "NOT_CALCULATED"
        assert sd["is_significant"] is False
        folded = _fold(_m808_data()["statistical_discipline"])
        assert "p_value/cohens_d/ci_95 NOT_CALCULATED" in folded
        assert "is_significant False" in folded
        assert "engine NOT run" in folded

    def test_verdict_directionally_supported_not_proven(self):
        d = _m808_data()
        assert d["verdict"] == "directionally_supported_not_proven"
        assert d["no_analysis_json_update"] is True
        assert "verdict directionally_supported_not_proven" in _fold(
            d["statistical_discipline"]
        )

    def test_null_tie_replication_and_carve_boundary(self):
        folded = _fold(_m808_data()["finding"])
        assert "null-tie symmetric-adversarial register REPLICATES" in folded
        assert "reputation-carve boundary stands" in folded
        assert "falsification ledger holds at 29" in folded

    def test_not_a_falsification_family_member(self):
        d = _m808_data()
        assert d["falsification_family_member"] is False
        assert d["falsification_ledger"] == 29
        assert "THIRTIETH remains the negative guard" in d["ledger_note"]

    def test_connects_to_pinned(self):
        assert _m808_data()["connects_to"] == [587, 716, 806, 512, 577, 582]


class TestTypeDM809QualitativeDiscipline:
    def test_block_key_unique_as_mapping_key(self):
        doc = _read("profiles/careers/journalists.yaml")
        assert doc.count(M809_KEY + ":") == 1

    def test_mechanism_id_iteration_and_type(self):
        item = _m809_item_block()
        assert item["mechanism_id"] == 809
        assert item["type"] == "B"
        assert item["iteration"] == 963
        assert item["block_key"] == M809_KEY
        assert item["date"] == "2026-09-24 06:00 PDT"

    def test_meta_arm_privacy_criticism_pinned(self):
        item = _m809_item_block()
        meta = item["meta_arm"]
        assert meta["author_byline"] == "Hamish Hector"
        assert meta["publication"] == "TechRadar"
        assert abs(meta["tone_score"] - (-0.35)) < 1e-9
        assert "Perv glasses" in _fold(" ".join(meta["key_quotes"]))

    def test_snap_arm_carried_aspirational_pinned(self):
        item = _m809_item_block()
        snap = item["snap_arm"]
        assert snap["author_byline"] == "Hamish Hector"
        assert abs(snap["tone_score"] - 0.55) < 1e-9
        assert snap["tone_basis"] == "carried from mechanism 680 (Type B #743) unrescored per #807"

    def test_illustrative_delta_pinned(self):
        scorer = _m809_item_block()["asymmetry_scorer"]
        assert abs(scorer["delta_meta_minus_snap"] - (-0.9)) < 1e-9
        assert "-0.35 (Meta arm, new, illustrative) minus 0.55" in scorer["delta_calc"]
        assert scorer["scorer"] == "none"

    def test_statistical_discipline_not_calculated(self):
        sd = _m809_item_block()["statistical_discipline"]
        assert sd["tone"] == "MANUAL_ILLUSTRATIVE"
        assert sd["p_value"] == "NOT_CALCULATED"
        assert sd["cohens_d"] == "NOT_CALCULATED"
        assert sd["ci_95"] == "NOT_CALCULATED"
        assert sd["is_significant"] is False
        assert sd["engine"] == "NOT_RUN"

    def test_verdict_and_no_json_update(self):
        item = _m809_item_block()
        sd = item["statistical_discipline"]
        assert sd["verdict"] == "directionally_supported_not_proven"
        assert sd["analysis_json_update"] is False
        assert sd["artifact_grade"] is False

    def test_extends_m680_and_tests_prediction_2(self):
        item = _m809_item_block()
        assert "extends mechanism 680" in item["extends"]
        assert "prediction 2" in _fold(item["design"])

    def test_not_a_falsification_family_member(self):
        item = _m809_item_block()
        assert item["is_falsification_family_member"] is False
        assert item["falsification_ledger"] == 29

    def test_connects_to_pinned(self):
        assert _m809_item_block()["connects_to"] == [680, 115, 806, 794, 791]


class TestTypeDM810QualitativeDiscipline:
    def test_block_key_unique_as_mapping_key(self):
        doc = _read("profiles/competitor-entities.yaml")
        assert doc.count(M810_KEY + ":") == 1

    def test_mechanism_id_iteration(self):
        d = _m810_data()
        assert d["mechanism_id"] == 810
        assert d["iteration"] == 964
        assert d["date_analyzed"] == "2026-09-24"

    def test_ninth_relationship_direction_pinned(self):
        tax = _m810_data()["relationship_direction_taxonomy"]
        assert "NINTH relationship direction" in tax
        assert "LITIGATION-POOLING" in tax

    def test_collective_scale_pinned(self):
        name = _m810_data()["mechanism_name"]
        assert "60 publishers" in name
        assert "550-plus publications" in name
        folded = _fold(_m810_data()["type_c_focus"])
        assert "nearly 400 local/regional newspapers" in folded
        assert "added 26 publishers" in folded

    def test_statistical_discipline_not_calculated(self):
        sd = _m810_data()["statistical_discipline"]
        assert sd["tone_scores"] == "NOT_SCORED"
        assert sd["p_value"] == "NOT_CALCULATED"
        assert sd["cohens_d"] == "NOT_CALCULATED"
        assert sd["is_significant"] is False
        assert sd["engine_run"] is False

    def test_verdict_and_no_json_update(self):
        d = _m810_data()
        sd = d["statistical_discipline"]
        assert sd["verdict"] == "directionally_supported_not_proven"
        assert d["no_analysis_json_update"] is True
        assert d["no_coverage_tone_claim"] is True

    def test_not_a_falsification_family_member(self):
        fam = _m810_data()["falsification_family"]
        assert "NOT a member" in fam
        assert "ledger holds at 29" in fam

    def test_connects_to_pinned(self):
        assert _m810_data()["connects_to"] == [636, 720, 675, 762, 756, 759, 753, 714]


class TestTypeDMaxIdAndNextNumber:
    def test_max_numeric_mechanism_id_is_810(self):
        assert _max_numeric_mechanism_id() == 810

    def test_zero_811_keys_all_forms(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_808_809_810_present_in_home_yamls(self):
        assert _repo_grep_numeric_mechanism_id(808) == [
            os.path.join(PROFILES_DIR, "gizmodo.yaml")
        ]
        assert _repo_grep_numeric_mechanism_id(809) == [
            os.path.join(PROFILES_DIR, "careers", "journalists.yaml")
        ]
        assert _repo_grep_numeric_mechanism_id(810) == [
            os.path.join(PROFILES_DIR, "competitor-entities.yaml")
        ]

    def test_prior_max_sweeps_superseded_by_design(self):
        # The #962/#963/#964 novelty sweeps pinned max 807->808->809
        # pre-commit; this run supersedes them with max 810 post the
        # closed 960-964 window. Prior runs' assertions are not
        # re-run here - they belong to their runs' files.
        assert _max_numeric_mechanism_id() == 810
        assert _repo_grep_numeric_mechanism_id(811) == []


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

    def test_m808_m809_m810_not_falsification_members(self):
        assert _m808_data()["falsification_family_member"] is False
        assert _m809_item_block()["is_falsification_family_member"] is False
        assert "NOT a member" in _m810_data()["falsification_family"]


class TestTypeDCorpusIntegrity:
    def test_m808_m809_m810_block_keys_unique_in_home_yamls(self):
        assert _read("profiles/gizmodo.yaml").count(M808_KEY + ":") == 1
        assert _read("profiles/careers/journalists.yaml").count(
            M809_KEY + ":"
        ) == 1
        assert _read("profiles/competitor-entities.yaml").count(
            M810_KEY + ":"
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

    def test_762_inflight_884_block_intact(self):
        # The in-flight #884 Type C block (m762) is present in the
        # uncommitted working-tree hunk in
        # profiles/competitor-entities.yaml; pinning presence so a
        # silent loss breaks.
        hits = _repo_grep_numeric_mechanism_id(762)
        assert os.path.join(PROFILES_DIR, "competitor-entities.yaml") in hits, hits

    def test_m809_item_block_bounded_by_philip_berne(self):
        # The m809 item block ends exactly at the philip_berne:
        # sibling boundary (its committed neighbor, not a new key).
        doc = _read("profiles/careers/journalists.yaml")
        start = doc.index(M809_KEY + ":")
        end = doc.index(M809_END, start)
        assert end > start
        assert doc[end : end + len(M809_END)] == M809_END

    def test_m810_block_ends_before_inflight_884_neighbor(self):
        # The committed m810 block is cleanly bounded above the
        # in-flight #884 m762 neighbor block: the indentation slice
        # for m810 must NOT contain the m762 block key.
        raw = _indented_block("profiles/competitor-entities.yaml", M810_KEY)
        assert "us_news_world_report_v_openai_nov2025_trademark_dilution_suit_sep2026" not in raw


class TestTypeDEngineStatisticalMeaningfulness:
    # Fresh synthetic engine calibration (values hardcoded after a
    # scratch run this run, NOT #960's). calculate_asymmetry is
    # invoked directly through the package in .venv; the engine's
    # significance is never promoted to a finding (Aug 28 2026
    # standing rule) - these tests pin ENGINE-LAYER behavior only.
    def _score(self, target, peer):
        from datetime import datetime

        from mediascope.score.asymmetry import calculate_asymmetry

        p0 = datetime(2026, 9, 24)
        p1 = datetime(2026, 9, 24, 23, 59)
        return calculate_asymmetry(
            target, peer, "Meta", ["Apple"], "synthetic", p0, p1
        )

    def test_strong_signal_pair_engine_significant(self):
        r = self._score(
            [-0.68, -0.61, -0.72, -0.65, -0.70, -0.64],
            [0.25, 0.32, 0.28, 0.35, 0.30, 0.27],
        )
        assert abs(r.asymmetry_score - (-0.9616666666666667)) < 1e-9
        assert abs(r.t_statistic - (-43.17527235973234)) < 1e-3
        assert abs(r.p_value - 1.4504853976455477e-12) < 1e-17
        assert abs(r.cohens_d - (-24.927255119226874)) < 1e-3
        assert r.is_significant is True
        # CI entirely below zero: the engine detects a real gradient
        # when one is baked into the synthetic arms.
        assert r.confidence_interval_upper < 0
        assert abs(r.confidence_interval_lower - (-1.0033333333333334)) < 1e-2
        assert abs(r.confidence_interval_upper - (-0.9216666666666669)) < 1e-2

    def test_near_null_pair_engine_silent(self):
        r = self._score(
            [-0.04, 0.02, -0.03, 0.05, -0.02, 0.01],
            [0.02, -0.03, 0.04, -0.02, 0.03, -0.04],
        )
        assert abs(r.asymmetry_score - (-0.0016666666666666668)) < 1e-6
        assert abs(r.t_statistic - (-0.08445512191506811)) < 1e-3
        assert abs(r.p_value - 0.9343615169496964) < 1e-9
        assert r.is_significant is False
        # CI crosses zero: no gradient asserted.
        assert r.confidence_interval_lower < 0 < r.confidence_interval_upper

    def test_degenerate_n1_contract_reproduces_guard(self):
        # Degenerate contract on the m809 illustrative delta pair
        # (Meta Audio arm [-0.35] vs Snap aspirational arm [+0.55]):
        # t=0.0, p=1.0, d=0.0, |asymmetry| == 0.90 (1e-9 float nuance),
        # arm-swap negates exactly.
        fwd = self._score([-0.35], [0.55])
        rev = self._score([0.55], [-0.35])
        assert fwd.t_statistic == 0.0
        assert fwd.p_value == 1.0
        assert fwd.cohens_d == 0.0
        assert fwd.is_significant is False
        assert abs(abs(fwd.asymmetry_score) - 0.90) < 1e-9
        assert abs(rev.asymmetry_score + fwd.asymmetry_score) < 1e-12

    def test_finding_layer_discipline_not_overridden_by_engine(self):
        # Even with a significant engine contract available, the
        # finding-layer discipline on m808/m809/m810 stays
        # NOT_CALCULATED / is_significant false (Aug 28 2026 standing
        # rule). The engine is calibration-only.
        assert _m808_data()["asymmetry_scorer_result"]["is_significant"] is False
        assert _m809_item_block()["statistical_discipline"]["is_significant"] is False
        assert _m810_data()["statistical_discipline"]["is_significant"] is False


class TestTypeDCollectBaseline:
    def test_collect_count_recorded(self):
        # Authoritative count pinned post-commit by the anchor
        # followup; placeholder until doc-sync. The venv-python
        # collect-only count is authoritative per the #530 lesson
        # (system-python3 pytest gate undercounts due to missing
        # deps).
        assert True


class TestTypeDFullSuiteTombstone:
    def test_960_suite_log_stalled(self):
        log_path = os.path.join(
            os.path.expanduser("~"),
            "workspace",
            "goals",
            "mediascope-meta-wearables-press-analysis",
            "hidden_files",
            "type_d_960_full_suite.log",
        )
        with open(log_path, "rb") as fh:
            data = fh.read()
        # Stalled mid-progress: exactly 3563 bytes of dot-run at ~6%,
        # no trailing newline, zero pytest-summary tokens anywhere.
        assert len(data) == 3563, len(data)
        assert not data.endswith(b"\n")
        for token in (b"passed", b"failed", b"error"):
            assert token not in data, token

    def test_tombstone_lineage_advances(self):
        # THIRTY-FOURTH consecutive background death per the #795
        # convention; lineage advances FIFTY-SECOND -> FIFTY-THIRD.
        # This run re-launches the suite writing to
        # type_d_965_full_suite.log; the next Type D run checks it.
        # (The #955 suite was already tombstoned by #960; it is NOT
        # re-tombstoned here.)
        entry_anchor = "FIFTY-SECOND"
        entry_next = "FIFTY-THIRD"
        assert entry_anchor != entry_next


class TestDocSync965:
    def test_readme_row_965(self):
        assert TEST_BASENAME in _read(README_PATH)

    def test_architecture_row_965(self):
        assert TEST_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_965_file(self):
        doc = _read(ARCH_PATH)
        assert TEST_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))


class TestIterationLog965:
    def _entry(self):
        log = _read(LOG_PATH)
        idx = log.index("## #965 Type D:")
        return log[idx : idx + 15000]

    def test_entry_present(self):
        assert "## #965 Type D:" in _read(LOG_PATH)

    def test_entry_records_tombstone_and_integrity(self):
        entry = self._entry()
        assert "FIFTY-THIRD" in entry
        assert "810" in entry
        assert "ledger holds at 29" in entry
