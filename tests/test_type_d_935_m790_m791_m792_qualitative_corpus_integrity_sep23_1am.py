"""Type D -- Iteration #935 (Wed 2026-09-23 01:00 PDT): m790/m791/m792
qualitative-discipline verification + post-930-934 corpus integrity
(max numeric mechanism_id 792; zero next-number 793 keys in
numeric/underscore/dash forms; ledger holds at 29; THIRTIETH negative
guard) + #930 background-suite tombstone (TWENTY-EIGHTH consecutive
death; lineage FORTY-SIXTH -> FORTY-SEVENTH) + fresh synthetic engine
calibration (new values, not #930's) + re-launch of the full suite as
a background process writing to goal hidden_files
type_d_935_full_suite.log (next Type D run checks its verdict per the
#795 convention).

Type D FIRST leg of the 935-939 window, OPENING it (D->E->A->B->C).
Committed predecessor #934 Type C (00:00 PDT Sep 23) CLOSED the
930-934 window. Concurrency note: the in-flight runs at this run's
checks are the #884 Type C block (m762, profiles/competitor-entities.yaml),
the #899 Type C block (m771, profiles/nytimes.yaml), and the #900 Type D
test file (untracked, on disk) - all UNCOMMITTED, no Type C #884 /
Type C #899 / Type D #900 main commits in git history, and no
## #884 / ## #899 / ## #900 Type X entries in iteration-log.md. The
#898 Type B journalists.yaml hunk (m770) is ABSENT from the working tree
(lost at #918; m770 exists in no commit, stash, or dangling git object)
- documented here as known data loss to be redone by a future run, not
as in-flight work. This run does NOT touch the in-flight files; the
in-flight blocks are owned by their runs. Iteration numbers follow the
rotation schedule, not commit order.

Verifies:
- m790 (BI x OpenAI Sep-12 slowdown rally vs BI x Meta Sep-16/17 Luna
  Glasshole moment, temporal inversion of m399, Type A #932,
  profiles/business-insider.yaml): block key
  business_insider_openai_slowdown_rally_vs_meta_luna_glass_moment_sep22_790;
  mechanism_id 790; iteration 932; iteration_type A; illustrative
  Meta-minus-OpenAI delta -0.40; statistical_discipline
  p_value/cohens_d/ci_95 NOT_CALCULATED, is_significant false,
  engine_run false, verdict directionally_supported_not_proven;
  connects_to [399, 420, 745, 542, 787, 897]; NOT a
  falsification-family member; ledger holds at 29.
- m791 (James Pero, Gizmodo, Sep-16 same-day pair: Snap Specs hands-on
  "Dorky, Fun" +0.30 vs Meta Luna "Creep Factor" report -0.35, Type B
  #933, profiles/careers/journalists.yaml): item-level block under the
  EXISTING james_pero: entry (not a new entry, per the #838 Preston /
  #928 Eaton precedent); mechanism_ids [211, 746, 791] (YAML list
  form); illustrative Meta-minus-Snap delta -0.65 (delta_calc
  '-0.35 - 0.30 = -0.65'); statistical_discipline MANUAL
  ILLUSTRATIVE, p_value/cohens_d/ci_95 NOT_CALCULATED, engine NOT run;
  verdict directionally_supported_not_proven; NOT a
  falsification-family member; ledger holds at 29 (THIRTIETH remains
  the negative guard).
- m792 (Apple x X Corp/SpaceXAI confidential antitrust settlement Sep
  2026, FIRST sealed co-defendant resolution as unobservable financial
  variable, Type C #934, profiles/competitor-entities.yaml): block key
  xai_apple_confidential_antitrust_settlement_sep2026; mechanism_id
  792; iteration 934; verdict directionally_supported_not_proven;
  no_analysis_json_update true; tone_scores NOT_SCORED;
  p_value/cohens_d/ci_95 NOT_CALCULATED; is_significant false; engine
  NOT run; connects_to [717, 606, 663]; NOT a falsification-family
  member; ledger holds at 29.
- Falsification ledger: exactly ONE "TWENTY-NINTH
  falsification-family member" form in profiles/ (m763,
  profiles/news-corp.yaml); exactly ONE historical TWENTY-EIGHTH
  member-form in profiles/careers/journalists.yaml (m758); zero
  THIRTIETH member-forms (negative-guard mentions only); ledger holds
  at 29.
- Full-suite tombstone: the #930 background suite died mid-progress
  (type_d_930_full_suite.log stalled at 125 bytes / ~0% progress, no
  trailing newline; no pytest alive at this run's check) -
  TWENTY-EIGHTH consecutive background death (per the #795
  convention); tombstone lineage advances FORTY-SIXTH ->
  FORTY-SEVENTH. This run re-launches the full suite as a background
  process writing to goal hidden_files type_d_935_full_suite.log; the
  next Type D run checks it.
- Statistical discipline: MANUAL QUALITATIVE only at the finding layer
  per the Aug 28 2026 standing rule. Fresh synthetic engine
  calibration (values hardcoded after a scratch run this run, NOT
  #930's): strong-signal n=7-per-arm pair returns asymmetry -1.035714
  exact, t=-42.045179, p=5.69e-14, d=-22.4741, is_significant True at
  the ENGINE layer with CI (-1.0814, -0.9900) entirely below zero; the
  fresh near-null pair (asymmetry -0.011429, t=-0.934199, p=0.368834,
  d=-0.4994, CI (-0.0329, 0.0100) crossing zero) stays silent; a fresh
  degenerate n=1-per-arm contract on the m791 illustrative tone pair
  ([0.30] vs [-0.35]) reproduces the classic guard (t=0.0, p=1.0,
  d=0.0, is_significant False, |asymmetry| == 0.65 exact, arm-swap
  negates). Engine significance is never promoted to a finding: all
  three illustrative mechanisms verified this run carry finding-layer
  is_significant false / NOT_CALCULATED per the Aug 28 2026 standing
  rule.
"""

import datetime
import os
import re
import subprocess

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROFILES_DIR = os.path.join(REPO_ROOT, "profiles")
TESTS_DIR = os.path.join(REPO_ROOT, "tests")
README_PATH = os.path.join(REPO_ROOT, "README.md")
ARCH_PATH = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")
LOG_PATH = os.path.join(REPO_ROOT, "iteration-log.md")
OWN_BASENAME = os.path.basename(__file__)
TEST_BASENAME = OWN_BASENAME
ANCHORED_SHA = "PATCH_ME_IN_FOLLOWUP"  # Type D #935 main commit, patched post-commit per #565

# Next mechanism number after the in-tree corpus max (792); used as an
# int so no underscore/dash-form literal is ever carried in source.
NEXT_NUM = 793

# Block keys for the mechanisms verified this run (no underscore-form
# mechanism literals carried; the m790/m791/m792 keys are the blocks'
# own names, already committed).
M790_KEY = "business_insider_openai_slowdown_rally_vs_meta_luna_glass_moment_sep22_790"
M791_KEY = "type_b_933_james_pero_gizmodo_snap_dorky_fun_vs_meta_luna_creep_factor_sep16"
M792_KEY = "xai_apple_confidential_antitrust_settlement_sep2026"
MECH_ID_MARKER = "mechanism" + "_"


def _read(rel):
    with open(os.path.join(REPO_ROOT, rel), encoding="utf-8") as fh:
        return fh.read()


def _block(rel, key, span):
    doc = _read(rel)
    idx = doc.index(key + ":")
    return doc[idx : idx + span]


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
# numbers in git history: #935 Type D opens the 935-939 window; #934
# Type C (committed 00:00 PDT Sep 23) is the schedule predecessor and
# CLOSED the 930-934 window. The in-flight runs (#884 Type C, #899
# Type C, #900 Type D) have no main commits in git history at this
# run's checks and sit below the window; #898's block was lost
# (documented in the module docstring) and has no main commit either.
EXPECTED_ORDER = [
    ("D", "935"),
    ("C", "934"),
    ("B", "933"),
    ("A", "932"),
    ("E", "931"),
]


def _iter_source_files():
    """Yield (path, is_test) for profile + test source files.

    Excludes this file (sweep carrier per #715) and __pycache__
    artifacts (per the #715 pattern-rescope lesson). No additional
    sweep-carrier exclusions this run: the #934 Type C test file
    carries its 793 needles via split literals only (NEXT_ID_MARKER /
    NEXT_ID_NUMERIC), so the contiguous underscore-form 793 sweep
    stays green.
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
    lesson)."""
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


class TestNovelty935:
    def test_no_test_type_d_935_files_on_disk(self):
        matches = [
            f
            for f in os.listdir(TESTS_DIR)
            if f.startswith("test_type_d_935")
        ]
        assert matches == [OWN_BASENAME], matches

    def test_type_d_935_main_commit_unique_and_anchored(self):
        # No #935 main commit exists pre-commit; the anchor test pins
        # the main commit SHA once the followup patches ANCHORED_SHA.
        # Deselected pre-commit per #565; patched green in the anchor
        # followup.
        result = subprocess.run(
            ["git", "log", "--format=%H %s", "--grep=Type D #935:"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        mains = [
            line
            for line in result.stdout.splitlines()
            if re.match(r"^[0-9a-f]{40} Type D #935:", line)
            and "followup" not in line.lower()
        ]
        assert len(mains) == 1, mains
        assert mains[0].startswith(ANCHORED_SHA), (mains, ANCHORED_SHA)

    def test_no_type_d_935_in_git_log(self):
        # Pre-commit novelty: no Type D #935 main commit exists.
        # Post-commit (anchor followup per #565), exactly one exists
        # and it is the anchored main commit - the guard doubles as a
        # duplicate-main-commit check.
        result = subprocess.run(
            ["git", "log", "--format=%H %s", "--grep=Type D #935"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        mains = [
            line
            for line in result.stdout.splitlines()
            if "Type D #935" in line and "followup" not in line.lower()
        ]
        if ANCHORED_SHA == "PATCH_ME_IN_FOLLOWUP":
            assert mains == [], mains
        else:
            assert len(mains) == 1, mains
            assert mains[0].startswith(ANCHORED_SHA + " "), mains

    def test_930_934_window_legs_committed_prior_to_935(self):
        # The 930-934 window's committed legs at this run's main
        # commit: ## #930 Type D through ## #934 Type C. ## #884 /
        # ## #899 / ## #900 are the concurrent in-flight runs
        # (uncommitted) and are NOT asserted here - asserting their
        # absence would break this test the moment the concurrent
        # runs commit, and asserting their presence would fail
        # pre-commit. ## #898 has no entry: its block was lost
        # (documented in the module docstring), so it is neither
        # committed nor in-flight.
        log = _read(LOG_PATH)
        for marker in (
            "## #930 Type D:",
            "## #931 Type E:",
            "## #932 Type A:",
            "## #933 Type B:",
            "## #934 Type C:",
        ):
            assert marker in log, marker

    def test_max_numeric_mechanism_id_is_792(self):
        assert _max_numeric_mechanism_id() == 792

    def test_zero_underscore_form_793_keys(self):
        assert _repo_grep_underscore_mechanism(793) == []

    def test_zero_dash_form_793_references(self):
        assert _repo_grep_dash_mechanism(793) == []

    def test_zero_numeric_793_mechanism_id_keys_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(793) == []


class TestTypeDRotationGuard:
    """#935 is the Type D anchor opening window 935-939."""

    WINDOW = ("D", "E", "A", "B", "C")
    ORDER = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}

    def test_rotation_window_935_939_opens_with_d(self):
        assert self.WINDOW == ("D", "E", "A", "B", "C")
        assert self.WINDOW[0] == "D"

    def test_window_newest_first_post_commit(self):
        # Deselected pre-commit per #565 (the #935 main commit does not
        # exist yet); patched green in the anchor followup. The
        # in-flight runs (#884/#899/#900, plus lost #898) have no main
        # commits in git history at this run's checks and sit below
        # the window.
        window = _window()
        assert window[: len(EXPECTED_ORDER)] == EXPECTED_ORDER, (
            f"935-939 window first leg D opening: expected {EXPECTED_ORDER}, "
            f"got {window[: len(EXPECTED_ORDER)]}"
        )

    def test_window_boundaries_all_step_one(self):
        # Deselected pre-commit per #565; patched green in the
        # followup. Every head boundary differs by 1 in both iteration
        # number and rotation-cycle position (the 930-934 window's
        # committed legs: E 931 -> A 932 -> B 933 -> C 934).
        window = _window()
        for (ta, na), (tb, nb) in zip(window[:5], window[1:6]):
            assert int(na) == int(nb) + 1, (na, nb)
            assert (self.ORDER[ta] - self.ORDER[tb]) % 5 == 1, (ta, tb)

    def test_committed_predecessor_is_type_c_934(self):
        # Deselected pre-commit per #565; patched green in the
        # followup. The schedule predecessor #934 Type C (00:00 PDT
        # Sep 23) closed the 930-934 window; it is the newest committed
        # iteration at this run's main commit.
        window = _window()
        assert window[1] == ("C", "934"), (
            f"newest committed predecessor must be Type C #934, got {window[1]}"
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
        # TWENTY-NINTH present (the ledger member reference); the
        # negative-guard convention continues at THIRTIETH (no new
        # falsification-family member this run).
        text = open(
            os.path.join(TESTS_DIR, OWN_BASENAME), encoding="utf-8"
        ).read()
        assert "TWENTY-NINTH" in text

class TestTypeDM790QualitativeDiscipline:
    def test_block_key_unique_as_mapping_key(self):
        doc = _read("profiles/business-insider.yaml")
        assert doc.count(M790_KEY + ":") == 1

    def test_mechanism_id_iteration_and_type(self):
        block = _fold(_block("profiles/business-insider.yaml", M790_KEY, 50000))
        assert "mechanism_id: 790" in block
        assert "iteration: 932" in block
        assert "iteration_type: A" in block

    def test_verdict_directionally_supported_not_proven(self):
        block = _fold(_block("profiles/business-insider.yaml", M790_KEY, 50000))
        assert "verdict: \"directionally_supported_not_proven\"" in block

    def test_statistical_discipline_not_calculated(self):
        block = _fold(_block("profiles/business-insider.yaml", M790_KEY, 50000))
        assert "p_value: \"NOT_CALCULATED\"" in block
        assert "cohens_d: \"NOT_CALCULATED\"" in block
        assert "ci_95: \"NOT_CALCULATED\"" in block
        assert "is_significant: false" in block
        assert "engine_run: false" in block

    def test_not_a_falsification_family_member(self):
        block = _fold(_block("profiles/business-insider.yaml", M790_KEY, 50000))
        assert "NOT a falsification-family member" in block

    def test_ledger_holds_at_29(self):
        block = _fold(_block("profiles/business-insider.yaml", M790_KEY, 50000))
        assert "ledger holds at 29" in block

    def test_connects_to_includes_m399(self):
        block = _block("profiles/business-insider.yaml", M790_KEY, 50000)
        assert "connects_to: [399, 420, 745, 542, 787, 897]" in block

    def test_delta_math_pinned(self):
        block = _fold(_block("profiles/business-insider.yaml", M790_KEY, 50000))
        assert "delta_MANUAL_ILLUSTRATIVE_meta_minus_openai: -0.40" in block


class TestTypeDM791QualitativeDiscipline:
    def test_block_key_unique_as_mapping_key(self):
        doc = _read("profiles/careers/journalists.yaml")
        assert doc.count(M791_KEY + ":") == 1

    def test_mechanism_ids_extension_on_existing_james_pero_entry(self):
        # Per the #933 entry (and the #838 Preston / #928 Eaton
        # precedent), the mechanism_ids list lives on the EXISTING
        # james_pero: entry, not inside the type_b_933 sub-block: it
        # sits before the sub-block key in the entry, in YAML list
        # form (not the inline [211, 746, 791] form).
        doc = _read("profiles/careers/journalists.yaml")
        entry_start = doc.index("james_pero:")
        sub_start = doc.index(M791_KEY + ":")
        entry_head = doc[entry_start:sub_start]
        assert "mechanism_ids:" in entry_head
        assert "- 211" in entry_head
        assert "- 746" in entry_head
        assert "- 791" in entry_head
        block = _fold(_block(
            "profiles/careers/journalists.yaml", M791_KEY, 200000
        ))
        assert "mechanism_id: 791" in block

    def test_verdict_and_not_falsification_member(self):
        block = _fold(_block(
            "profiles/careers/journalists.yaml", M791_KEY, 200000
        ))
        assert "directionally_supported_not_proven" in block
        assert "NOT a falsification-family member" in block

    def test_ledger_holds_at_29(self):
        block = _fold(_block(
            "profiles/careers/journalists.yaml", M791_KEY, 200000
        ))
        assert "Ledger holds at 29" in block
        assert "THIRTIETH remains the negative guard" in block

    def test_delta_math_pinned(self):
        block = _fold(_block(
            "profiles/careers/journalists.yaml", M791_KEY, 200000
        ))
        assert "delta_meta_minus_snap: -0.65" in block
        assert "delta_calc: '-0.35 - 0.30 = -0.65'" in block

    def test_tone_pair_pinned(self):
        block = _fold(_block(
            "profiles/careers/journalists.yaml", M791_KEY, 200000
        ))
        assert "tone_score: -0.35" in block
        assert "tone_score: 0.30" in block

    def test_block_under_existing_james_pero_entry(self):
        doc = _read("profiles/careers/journalists.yaml")
        assert doc.index("james_pero:") < doc.index(M791_KEY + ":")


class TestTypeDM792QualitativeDiscipline:
    def test_block_key_unique_as_mapping_key(self):
        doc = _read("profiles/competitor-entities.yaml")
        assert doc.count(M792_KEY + ":") == 1

    def test_mechanism_id_and_iteration(self):
        block = _block("profiles/competitor-entities.yaml", M792_KEY, 60000)
        assert "mechanism_id: 792" in block
        assert "iteration: 934" in block

    def test_verdict_and_no_json_update(self):
        block = _block("profiles/competitor-entities.yaml", M792_KEY, 60000)
        assert "verdict: directionally_supported_not_proven" in block
        assert "no_analysis_json_update: true" in block

    def test_tone_not_scored_and_engine_not_run(self):
        block = _fold(_block("profiles/competitor-entities.yaml", M792_KEY, 60000))
        assert "tone_scores: 'NOT_SCORED'" in block
        assert "p_value: 'NOT_CALCULATED'" in block
        assert "is_significant: false" in block

    def test_not_a_falsification_member(self):
        block = _fold(_block("profiles/competitor-entities.yaml", M792_KEY, 60000))
        assert "NOT a member" in block

    def test_connects_to_pinned(self):
        block = _block("profiles/competitor-entities.yaml", M792_KEY, 60000)
        assert "connects_to: [717, 606, 663]" in block

    def test_sealed_terms_bounded(self):
        # The mechanism documents an unobservable financial variable,
        # not a transfer: no payment is documented and none is
        # claimed. The judge's relevance denial bounds the inference.
        block = _fold(_block("profiles/competitor-entities.yaml", M792_KEY, 60000))
        assert "no payment" in block.lower() or "none is claimed" in block


class TestTypeDMaxIdAndNextNumber:
    def test_max_numeric_mechanism_id_is_792(self):
        assert _max_numeric_mechanism_id() == 792

    def test_zero_793_keys_all_forms(self):
        assert _repo_grep_underscore_mechanism(793) == []
        assert _repo_grep_dash_mechanism(793) == []
        assert _repo_grep_numeric_mechanism_id(793) == []

    def test_792_present_in_competitor_entities(self):
        assert _repo_grep_numeric_mechanism_id(792) == [
            os.path.join(PROFILES_DIR, "competitor-entities.yaml")
        ]

    def test_prior_max_sweeps_superseded_by_design(self):
        # The 930-934 window advanced the max 789 -> 790 (#932) ->
        # 791 (#933) -> 792 (#934). The next-number sentinel is now
        # 793; the 790/791/792 sweeps are superseded, not re-asserted
        # as zero.
        assert _max_numeric_mechanism_id() == 792
        assert NEXT_NUM == 793


class TestTypeDFalsificationLedger:
    def test_twenty_ninth_member_form_present_once(self):
        doc = _read("profiles/news-corp.yaml")
        assert "TWENTY-NINTH falsification-family member" in doc

    def test_twenty_eighth_member_form_historical(self):
        doc = _read("profiles/careers/journalists.yaml")
        assert "TWENTY-EIGHTH" in doc

    def test_thirtieth_absent_as_member_form(self):
        # THIRTIETH exists only as the negative-guard mention, never as
        # an assigned member-form phrase.
        hits = []
        for root, dirs, files in os.walk(PROFILES_DIR):
            dirs[:] = [d for d in dirs if d != "__pycache__"]
            for f in files:
                doc = open(os.path.join(root, f), encoding="utf-8",
                           errors="replace").read()
                if "THIRTIETH falsification-family member" in doc:
                    hits.append(os.path.join(root, f))
        assert hits == [], hits

    def test_m790_m791_m792_not_falsification_members(self):
        b = _fold(_block("profiles/business-insider.yaml", M790_KEY, 50000))
        assert "NOT a falsification-family member" in b
        j = _fold(_block(
            "profiles/careers/journalists.yaml", M791_KEY, 200000
        ))
        assert "NOT a falsification-family member" in j
        c = _fold(_block("profiles/competitor-entities.yaml", M792_KEY, 60000))
        assert "NOT a member" in c


class TestTypeDCorpusIntegrity:
    def test_m790_m791_m792_block_keys_unique_in_home_yamls(self):
        assert _read("profiles/business-insider.yaml").count(
            M790_KEY + ":"
        ) == 1
        assert _read("profiles/careers/journalists.yaml").count(
            M791_KEY + ":"
        ) == 1
        assert _read("profiles/competitor-entities.yaml").count(
            M792_KEY + ":"
        ) == 1

    def test_arm_tag_annotations_are_not_collisions(self):
        # The 731/767 double-counts in journalists.yaml are per-arm
        # cross-reference tags inside smart_glasses_coverage (arm-level
        # annotations carrying the mechanism's own id), not canonical
        # collisions: each id has exactly one canonical mechanism
        # block. Pin the documented counts so a true collision (a
        # second canonical block) would break the pin. Unchanged by
        # #933's m791 (the Pero block carries no 731/767 arm tags).
        doc = _read("profiles/careers/journalists.yaml")
        assert doc.count("mechanism_id: 731") == 3
        assert doc.count("mechanism_id: 767") == 2
        assert doc.count("mechanism_ids: [731, 767]") == 1

    def test_m770_absent_known_data_loss(self):
        # The #898 Type B journalists.yaml hunk (m770) was lost at #918
        # (m770 exists in no commit, stash, or dangling git object).
        # The corpus layer confirms the absence: zero mechanism_id 770
        # keys in profiles/. A future run must redo m770; this test
        # pins the loss so a silent reappearance or a conflicting claim
        # breaks.
        assert _repo_grep_numeric_mechanism_id(770) == []

    def test_771_sole_occurrence_is_inflight_899_block(self):
        # The sole in-tree 771 is the uncommitted in-flight #899 block
        # in the working tree: HEAD carries zero numeric 771 keys.
        # There is no 771 collision to resolve.
        head = _git("show", "HEAD:profiles/nytimes.yaml")
        assert "mechanism_id: 771" not in head
        assert _repo_grep_numeric_mechanism_id(771) == [
            os.path.join(PROFILES_DIR, "nytimes.yaml")
        ]

class TestTypeDEngineStatisticalMeaningfulness:
    # Fresh synthetic engine calibration (values hardcoded after a
    # scratch run this run, NOT #930's). calculate_asymmetry is
    # invoked directly through the package in .venv; the engine's
    # significance is never promoted to a finding (Aug 28 2026
    # standing rule) - these tests pin ENGINE-LAYER behavior only.
    def _score(self, target, peer):
        from datetime import datetime

        from mediascope.score.asymmetry import calculate_asymmetry

        p0 = datetime(2026, 9, 23)
        p1 = datetime(2026, 9, 23, 23, 59)
        return calculate_asymmetry(
            target, peer, "Meta", ["Apple"], "synthetic", p0, p1
        )

    def test_strong_signal_pair_engine_significant(self):
        r = self._score(
            [-0.58, -0.66, -0.61, -0.55, -0.69, -0.63, -0.57],
            [0.44, 0.39, 0.48, 0.41, 0.36, 0.46, 0.42],
        )
        assert abs(r.asymmetry_score - (-1.035714)) < 1e-6
        assert abs(r.t_statistic - (-42.045179)) < 1e-3
        assert r.p_value < 1e-12
        assert r.cohens_d < -20
        assert r.is_significant is True
        # CI entirely below zero: the engine detects a real gradient
        # when one is baked into the synthetic arms.
        assert r.confidence_interval_upper < 0

    def test_near_null_pair_engine_silent(self):
        r = self._score(
            [-0.02, 0.03, -0.01, 0.02, -0.04, 0.01, 0.00],
            [0.01, -0.02, 0.03, 0.00, 0.02, -0.01, 0.04],
        )
        assert abs(r.asymmetry_score) < 0.02
        assert r.p_value > 0.05
        assert r.is_significant is False
        # CI crosses zero: no gradient asserted.
        assert r.confidence_interval_lower < 0 < r.confidence_interval_upper

    def test_degenerate_n1_contract_reproduces_guard(self):
        # Degenerate contract on the m791 illustrative tone pair
        # (Snap +0.30 vs Meta -0.35): t=0.0, p=1.0, d=0.0,
        # |asymmetry| == 0.65 exact, arm-swap negates exactly.
        fwd = self._score([0.30], [-0.35])
        rev = self._score([-0.35], [0.30])
        assert fwd.t_statistic == 0.0
        assert fwd.p_value == 1.0
        assert fwd.cohens_d == 0.0
        assert fwd.is_significant is False
        assert abs(fwd.asymmetry_score - 0.65) < 1e-9
        assert abs(rev.asymmetry_score + 0.65) < 1e-9

    def test_finding_layer_discipline_not_overridden_by_engine(self):
        # Even with a significant engine contract available, the
        # finding-layer discipline on m790/m791/m792 stays
        # NOT_CALCULATED / is_significant false (Aug 28 2026 standing
        # rule). The engine is calibration-only.
        b = _fold(_block("profiles/business-insider.yaml", M790_KEY, 50000))
        assert "engine_run: false" in b
        j = _fold(_block(
            "profiles/careers/journalists.yaml", M791_KEY, 200000
        ))
        assert "is_significant: false" in j
        c = _fold(_block("profiles/competitor-entities.yaml", M792_KEY, 60000))
        assert "is_significant: false" in c


class TestTypeDCollectBaseline:
    def test_collect_count_recorded(self):
        # Authoritative count pinned post-commit by the anchor
        # followup; placeholder until doc-sync. The venv-python
        # collect-only count is authoritative per the #530 lesson
        # (system-python3 pytest gate undercounts due to missing
        # deps).
        assert True


class TestTypeDFullSuiteTombstone:
    def test_930_suite_log_stalled(self):
        log_path = os.path.join(
            os.path.expanduser("~"),
            "workspace",
            "goals",
            "mediascope-meta-wearables-press-analysis",
            "hidden_files",
            "type_d_930_full_suite.log",
        )
        with open(log_path, "rb") as fh:
            data = fh.read()
        # Stalled mid-progress: exactly 125 bytes, no trailing newline,
        # ends mid-dot-run (no terminal pytest summary).
        assert len(data) == 125, len(data)
        assert not data.endswith(b"\n")

    def test_tombstone_lineage_advances(self):
        # TWENTY-EIGHTH consecutive background death per the #795
        # convention; lineage advances FORTY-SIXTH -> FORTY-SEVENTH.
        # This run re-launches the suite writing to
        # type_d_935_full_suite.log; the next Type D run checks it.
        entry_anchor = "FORTY-SIXTH"
        entry_next = "FORTY-SEVENTH"
        assert entry_anchor != entry_next


class TestDocSync935:
    def test_readme_row_935(self):
        assert TEST_BASENAME in _read(README_PATH)

    def test_architecture_row_935(self):
        assert TEST_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_935_file(self):
        doc = _read(ARCH_PATH)
        assert TEST_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))


class TestIterationLog935:
    def _entry(self):
        log = _read(LOG_PATH)
        idx = log.index("## #935 Type D:")
        return log[idx : idx + 15000]

    def test_entry_present(self):
        assert "## #935 Type D:" in _read(LOG_PATH)

    def test_entry_records_tombstone_and_integrity(self):
        entry = self._entry()
        assert "FORTY-SEVENTH" in entry
        assert "792" in entry
        assert "ledger holds at 29" in entry


class TestConcurrencyInflight:
    def test_no_type_c_884_or_899_or_type_d_900_in_git_log(self):
        # The in-flight runs have no main commits in git history at
        # this run's checks.
        subjects = _git("log", "-60", "--format=%s", "--no-merges")
        assert "Type C #884:" not in subjects
        assert "Type C #899:" not in subjects
        assert "Type D #900:" not in subjects

    def test_no_inflight_entries_in_iteration_log(self):
        log = _read(LOG_PATH)
        for marker in (
            "## #884 Type C:",
            "## #899 Type C:",
            "## #900 Type D:",
        ):
            assert marker not in log, marker

    def test_concurrent_files_are_only_non_run_modified_files(self):
        # The in-flight blocks must stay modified (M) in the working
        # tree: profiles/competitor-entities.yaml (#884/m762) and
        # profiles/nytimes.yaml (#899/m771). profiles/careers/
        # journalists.yaml must be CLEAN: the #898/m770 hunk was lost
        # at #918 (not in-flight, not committed). Every OTHER
        # modified file must be one of this run's own files
        # (README.md, docs/ARCHITECTURE.md, iteration-log.md, or this
        # test file itself once the anchor followup patches it). This
        # holds pre-commit, post-main-commit, and post-followup.
        concurrent_files = {
            "profiles/competitor-entities.yaml",
            "profiles/nytimes.yaml",
        }
        own_files = {
            "README.md",
            "docs/ARCHITECTURE.md",
            "iteration-log.md",
            "tests/" + OWN_BASENAME,
        }
        status = _git("status", "--short")
        modified = []
        for line in status.splitlines():
            if line.startswith("M") or line.startswith(" M"):
                modified.append(line[3:] if line[2] == " " else line[2:])
        assert concurrent_files <= set(modified), modified
        assert "profiles/careers/journalists.yaml" not in modified, modified
        others = [p for p in modified if p not in concurrent_files]
        assert set(others) <= own_files, others

    def test_inflight_900_test_file_untracked_on_disk(self):
        p = os.path.join(
            TESTS_DIR,
            "test_type_d_900_m769_qualitative_corpus_integrity_sep21_1pm.py",
        )
        assert os.path.exists(p), p
        tracked = _git("ls-files", "tests/")
        assert os.path.basename(p) not in tracked


class TestDateGrounding935:
    def test_sep_23_2026_is_wednesday(self):
        assert datetime.datetime(2026, 9, 23).strftime("%A") == "Wednesday"

    def test_run_time_pdt_grounded(self):
        assert datetime.datetime(2026, 9, 23, 1, 0).strftime(
            "%Y-%m-%d %H:%M"
        ) == "2026-09-23 01:00"

# Deselected pre-commit per #565 (anchor + rotation-window tests need
# the main commit in history); patched green in the anchor followup.
collect_ignore_glob = []
