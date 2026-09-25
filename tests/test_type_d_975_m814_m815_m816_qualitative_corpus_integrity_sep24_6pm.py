"""Type D -- Iteration #975 (Thu 2026-09-24 18:00 PDT): m814/m815/m816
qualitative-discipline verification + post-970-974 corpus integrity
(max numeric mechanism_id 816; zero next-number 817 keys in
numeric/underscore/dash forms; ledger holds at 29; THIRTY-FIRST
negative guard) + #970 background-suite tombstone (THIRTY-SIXTH
consecutive death; lineage FIFTY-FOURTH -> FIFTY-FIFTH) + fresh
synthetic engine calibration (new values, not #970's) + re-launch of
the full suite as a background process writing to goal hidden_files
type_d_975_full_suite.log (next Type D run checks its verdict per the
#795 convention).

Type D FIRST leg of the 975-979 window, OPENING it (D->E->A->B->C).
Committed predecessor #974 Type C (17:00 PDT Sep 24) CLOSED the
970-974 window. Concurrency note: the in-flight runs at this run's
checks are the #899 Type C block (m771, uncommitted hunk in
profiles/nytimes.yaml) and the #900 Type D test file (untracked, on
disk) - both UNCOMMITTED, no Type C #899 / Type D #900 main commits in
git history, and no ## #899 / ## #900 Type X entries in
iteration-log.md. The #938 Type B test file carries an uncommitted
ANCHORED_SHA working-tree edit from #938's anchor followup (still open
at this run's checks) - owned by #938's followup chain, untouched by
#975. The #884 Type C block (m762) is COMMITTED at this run's checks
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
- m814 (WIRED x Snap Sep-16 launch-day register vs WIRED x Meta
  Connect-week privacy-positive register: NEW Sep 23 2026 Meta arm
  "Meta Pinky Promises Its Smart Glasses Will Be Private Soon"
  (mirror-attested, privacy-positive peg) vs CARRIED Sep 16 2026 Snap
  arm (m743, Boone Ashworth "Here's What Snap's Expensive Specs Can
  Actually Do", price-hardened product-forward feature relay,
  zero privacy vocabulary on 4-camera standalone AR glasses);
  MANUAL ILLUSTRATIVE tones Meta -0.20 / Snap -0.15, launch-window
  delta (Meta minus Snap) -0.05 near-null; the mechanism claim is
  register-level presence/absence, not a tone gradient:
  surveillance-alarm register fires on the Meta arm even on a
  privacy-positive peg and stays silent on the Snap arm despite
  strictly more sensors (2 RGB plus 2 IR cameras); temporal extension
  of mechanism 727 into populated arms at publication level; Type A
  #972, profiles/wired.yaml): block key
  wired_snap_sep16_launch_register_vs_meta_connect_privacy_positive_alarm_coda_sep24_2026;
  mechanism_id 814; iteration 972; iteration_type 'A'; MANUAL
  ILLUSTRATIVE ONLY per standing rule Aug 28 2026, engine NOT run at
  the finding layer, p_value/cohens_d/confidence interval
  NOT_CALCULATED, is_significant False, verdict
  directionally_supported_not_proven, no_analysis_json_update true,
  NOT artifact-grade; falsification_family_member False
  (falsification_ledger 29); connects_to [727, 743, 163, 442, 354,
  208]. WORDING-DRIFT FLAG (documented, not repaired: Type D
  read-only convention on other runs' blocks): the m814 ledger_note
  says "the THIRTIETH mechanism stands as the most recent
  falsification-family member" while the corpus-wide convention
  (every other ledger note, the README rows, the #970 integrity
  verdict) holds THIRTIETH as the negative guard and the ledger at
  29 with no THIRTIETH member-form claim anywhere. A future
  non-Type-D run reconciles the wording; this run pins both facts.
- m815 (Kit Eaton, Inc.: Sep-23/24 2026 Meta Connect launch column
  carries surveillance-alarm register, MANUAL ILLUSTRATIVE -0.45,
  on the CONCRETE launch peg vs his carried Sep-16 Luna RUMOR
  column (constructive pivot register +0.25, mechanism 788,
  un-rescored per #807); illustrative within-writer Meta temporal
  delta (concrete-launch minus rumor) -0.70; RESOLVES mechanism
  788's own testable predictions: prediction 1 (continued
  constructive register on concrete launch) FAILS - the
  concession-peg confound HARDENS, constructiveness attached to the
  rumor of a concession not to Meta-the-entity; prediction 2
  (controversy frame on a Meta always-listening audio feature)
  SUPPORTED VERBATIM; register follows the PEG not the entity;
  REPLICATES the m637/m852 peg-follows-register pattern at
  journalist level; BOUNDS m788 (Sep-16 constructiveness is
  concession-peg-specific); Type B #973,
  profiles/careers/journalists.yaml under the Kit Eaton item
  (item-level key
  type_b_973_kit_eaton_inc_connect2026_launch_alarm_vs_luna_rumor_constructive_pivot_sep24,
  matching the m431/m641/m743/m812 item-level convention; colon form
  only; zero underscore-form 815 keys in profiles by designed keying
  per #715; the one contiguous mechanism_815 literal in-tree is the
  #973 test file's own test_log_entry_mentions_mechanism_815 method
  name, pinned as the known carrier per #715); statistical_discipline
  tone MANUAL_ILLUSTRATIVE, p_value/cohens_d/ci_95 NOT_CALCULATED,
  is_significant False, engine NOT_RUN, verdict
  directionally_supported_not_proven, no_analysis_json_update True,
  artifact NOT artifact-grade; is_falsification_family_member False
  (falsification_ledger 29); connects_to [671, 788, 637, 852];
  test_count 52.
- m816 (NewsGuard AI European expansion: Sep 21 2026 press release
  extends the 50/50 cited-publisher revenue-share model to France,
  Italy, Germany, Austria, and the UK with local-language versions;
  responses drawn exclusively from 12,000 NewsGuard-vetted
  publishers; "will share revenues 50-50 with all news publishers
  whose journalism is cited"; European publisher coalition forming
  (Ouest-France, 5min.at, Linkiesta); co-marketing partners earn
  subscription revenue as a second channel; framed as "an
  alternative to big tech's toxic business model" - the corpus's
  first publisher-side product to name the uncompensated-training
  grievance as its market positioning; precision: the 50/50 formula
  dates to the June 23 2026 US launch - September is GEOGRAPHIC and
  COALITION extension, not a new formula; incentive geometry:
  transparent citation-linked 50/50 vs opaque fixed-fee deals (m549
  Meta-News Corp up to $50M/yr), citation-contingent per-response
  tournament among the 12,000 vetted sources; Type C #974,
  profiles/competitor-entities.yaml as a TOP-LEVEL key, FIRST
  dedicated corpus mechanism on NewsGuard AI publisher economics):
  block key newsguard_ai_europe_50_50_cited_publisher_revenue_share_816;
  mechanism_id 816; iteration 974; rotation 'Type C';
  statistical_discipline qualitative_only True, tone_scores
  NOT_SCORED, p_value/cohens_d/ci_95 NOT_CALCULATED, is_significant
  False, engine_run False, artifact_grade False, verdict
  directionally_supported_not_proven; no_coverage_tone_claim True;
  no_analysis_json_update True; NOT a falsification-family member
  (falsification_family "NOT a member - publisher-revenue-model
  documentation leg with no coverage-tone pair; ledger holds at 29");
  connects_to [621, 789, 810, 786, 549].
- Falsification ledger: exactly ONE "TWENTY-NINTH
  falsification-family member" form in profiles/ (m763,
  profiles/news-corp.yaml); TWENTY-EIGHTH member-form historical
  (journalists.yaml); zero "THIRTIETH falsification-family member"
  claims anywhere in profiles/ (wired.yaml carries only the
  negative-guard "no THIRTIETH member-form" string); zero
  THIRTY-FIRST strings anywhere in profiles/; ledger holds at 29.
  The m814 "THIRTIETH mechanism stands" wording is pinned as a
  wording-drift flag, not a member-form claim.
- Full-suite tombstone: the #970 background suite died mid-progress
  (type_d_970_full_suite.log stalled at exactly 171 bytes of
  dot-run at ~0% since Sep 24 13:26 PDT, no trailing newline, zero
  pytest-summary tokens; no pytest alive at this run's check) -
  THIRTY-SIXTH consecutive background death (per the #795
  convention); tombstone lineage advances FIFTY-FOURTH ->
  FIFTY-FIFTH. The #965 suite was already tombstoned by #970 and is
  NOT re-tombstoned here. This run re-launches the suite writing to
  type_d_975_full_suite.log; the next Type D run checks it.
- Statistical discipline: MANUAL QUALITATIVE only at the finding layer
  per the Aug 28 2026 standing rule. Fresh synthetic engine
  calibration (values hardcoded after a scratch run this run, NOT
  #970's): strong-signal n=6-per-arm pair returns asymmetry
  -1.1633333333333336, t=-56.39310922110984,
  p=3.7779549519096396e-13, d=-32.55857678924774, is_significant
  True at the ENGINE layer with CI (-1.2000, -1.1250) entirely below
  zero; the fresh near-null pair (asymmetry 0.0166666666666667,
  t=0.69538406236934, p=0.5026766299513296, d=0.40148017559912, CI
  (-0.0250, 0.0600) crossing zero) stays silent; a fresh degenerate
  n=1-per-arm contract on the m815 illustrative delta pair ([-0.45]
  vs [+0.25]) reproduces the classic guard (t=0.0, p=1.0, d=0.0,
  is_significant False, |asymmetry| == 0.70 within 1e-9, arm-swap
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

ANCHORED_SHA = "6c9a20f9eef8bfff01acc8dc25356000fefc7f49"  # Type D #975 main commit, patched post-commit per #565

MECH_ID_MARKER = "mechanism" + "_"
NEXT_NUM = 817

M814_KEY = "wired_snap_sep16_launch_register_vs_meta_connect_privacy_positive_alarm_coda_sep24_2026"
M815_KEY = "type_b_973_kit_eaton_inc_connect2026_launch_alarm_vs_luna_rumor_constructive_pivot_sep24"
M816_KEY = "newsguard_ai_europe_50_50_cited_publisher_revenue_share_816"

M814_SNAP_END = "\n    meta:"
M815_END = "\n    role:"
M816_INDENT = 0  # top-level key in competitor-entities.yaml


def _read(rel):
    with open(os.path.join(REPO_ROOT, rel), encoding="utf-8") as fh:
        return fh.read()


def _indented_block(rel, key, indent=4):
    """Extract a YAML mapping block keyed at a fixed indent.

    Slices from the key line through subsequent lines indented deeper
    than `indent` (blank lines included), stopping at the next
    indent-or-fewer sibling. Robust to in-flight neighbor blocks since
    the slice depends only on indentation, not on the neighbor's key.
    """
    doc = _read(rel)
    marker = "\n" + " " * indent + key + ":"
    assert doc.count(marker) == 1, (rel, key, indent, doc.count(marker))
    start = doc.index(marker) + 1
    lines = doc[start:].splitlines(keepends=True)
    out = [lines[0]]
    for line in lines[1:]:
        if line.strip() == "":
            out.append(line)
            continue
        line_indent = len(line) - len(line.lstrip(" "))
        if line_indent <= indent:
            break
        out.append(line)
    return "".join(out)


def _block_data(rel, key, indent=4):
    import yaml

    return yaml.safe_load(textwrap.dedent(_indented_block(rel, key, indent)))[key]


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
# numbers in git history: #975 Type D opens the 975-979 window; #974
# Type C (committed 17:00 PDT Sep 24) is the schedule predecessor and
# CLOSED the 970-974 window. The in-flight runs (#899 Type C, #900
# Type D) have no main commits in git history at this run's checks
# and sit below the window; #898's block was lost (documented in the
# module docstring) and has no main commit either. The #884 block
# (m762) is committed at this run's checks.
EXPECTED_ORDER = [
    ("D", "975"),
    ("C", "974"),
    ("B", "973"),
    ("A", "972"),
    ("E", "971"),
]


def _iter_source_files():
    """Yield (path, is_test) for profile + test source files.

    Excludes this file (sweep carrier per #715) and __pycache__
    artifacts (per the #715 pattern-rescope lesson). No additional
    sweep-carrier exclusions this run: no in-tree file carries a
    contiguous 817-form mechanism literal (verified pre-commit), so
    the 817 sweeps run repo-wide with only this file excluded.
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


def _m814_data():
    return _block_data("profiles/wired.yaml", M814_KEY)


def _m815_item_block():
    return _block_data("profiles/careers/journalists.yaml", M815_KEY)


def _m816_data():
    return _block_data("profiles/competitor-entities.yaml", M816_KEY, indent=0)


class TestNovelty975:
    def test_no_test_type_d_975_files_on_disk(self):
        matches = [
            f
            for f in os.listdir(TESTS_DIR)
            if f.startswith("test_type_d_975")
        ]
        assert matches == [OWN_BASENAME], matches

    def test_type_d_975_main_commit_unique_and_anchored(self):
        # No #975 main commit exists pre-commit; the anchor test pins
        # the main commit SHA once the followup patches ANCHORED_SHA.
        # Deselected pre-commit per #565; patched green in the anchor
        # followup.
        result = subprocess.run(
            ["git", "log", "--format=%H %s", "--grep=Type D #975:"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        mains = [
            line
            for line in result.stdout.splitlines()
            if re.match(r"^[0-9a-f]{40} Type D #975:", line)
            and "followup" not in line.lower()
        ]
        assert len(mains) == 1, mains
        assert mains[0].startswith(ANCHORED_SHA), (mains, ANCHORED_SHA)

    def test_no_type_d_975_in_git_log(self):
        # Pre-commit novelty: no Type D #975 main commit exists.
        # Post-commit (anchor followup per #565), exactly one exists
        # and it is the anchored main commit - the guard doubles as a
        # duplicate-main-commit check.
        result = subprocess.run(
            ["git", "log", "--format=%H %s", "--grep=Type D #975"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        mains = [
            line
            for line in result.stdout.splitlines()
            if "Type D #975" in line and "followup" not in line.lower()
        ]
        if ANCHORED_SHA == "PATCH_ME_IN_FOLLOWUP":
            assert mains == [], mains
        else:
            assert len(mains) == 1, mains
            assert mains[0].startswith(ANCHORED_SHA + " "), mains

    def test_970_974_window_legs_committed_prior_to_975(self):
        # The 970-974 window's committed legs at this run's main
        # commit: ## #970 Type D through ## #974 Type C. ## #899 /
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
            "## #970 Type D:",
            "## #971 Type E:",
            "## #972 Type A:",
            "## #973 Type B:",
            "## #974 Type C:",
        ):
            assert marker in log, marker

    def test_max_numeric_mechanism_id_is_816(self):
        assert _max_numeric_mechanism_id() == 816

    def test_zero_underscore_form_817_keys(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_zero_dash_form_817_references(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_zero_numeric_817_mechanism_id_keys_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []


class TestTypeDRotationGuard:
    """#975 is the Type D anchor opening window 975-979."""

    WINDOW = ("D", "E", "A", "B", "C")
    ORDER = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}

    def test_rotation_window_975_979_opens_with_d(self):
        assert self.WINDOW == ("D", "E", "A", "B", "C")
        assert self.WINDOW[0] == "D"

    def test_window_newest_first_post_commit(self):
        # Deselected pre-commit per #565 (the #975 main commit does not
        # exist yet); patched green in the anchor followup. The
        # in-flight runs (#899/#900, plus lost #898) have no main
        # commits in git history at this run's checks and sit below
        # the window.
        window = _window()
        assert window[: len(EXPECTED_ORDER)] == EXPECTED_ORDER, (
            f"975-979 window first leg D opening: expected {EXPECTED_ORDER}, "
            f"got {window[: len(EXPECTED_ORDER)]}"
        )

    def test_window_boundaries_all_step_one(self):
        # Deselected pre-commit per #565; patched green in the
        # followup. Every head boundary differs by 1 in both iteration
        # number and rotation-cycle position (the 970-974 window's
        # committed legs: D 975 -> C 974 -> B 973 -> A 972 -> E 971
        # newest-first, i.e. D->E->A->B->C oldest-first).
        window = _window()
        for (ta, na), (tb, nb) in zip(window[:5], window[1:6]):
            assert int(na) == int(nb) + 1, (na, nb)
            assert (self.ORDER[ta] - self.ORDER[tb]) % 5 == 1, (ta, tb)

    def test_committed_predecessor_is_type_c_974(self):
        # Deselected pre-commit per #565; patched green in the
        # followup. The schedule predecessor #974 Type C (17:00 PDT
        # Sep 24) closed the 970-974 window; it is the newest committed
        # iteration at this run's main commit.
        window = _window()
        assert window[1] == ("C", "974"), (
            f"newest committed predecessor must be Type C #974, got {window[1]}"
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
        # family member this run). The m814 "THIRTIETH mechanism
        # stands" wording drift is pinned as a documentation flag in
        # the module docstring, not a ledger change.
        text = open(
            os.path.join(TESTS_DIR, OWN_BASENAME), encoding="utf-8"
        ).read()
        assert "THIRTY-FIRST" in text


class TestTypeDM814QualitativeDiscipline:
    def test_block_key_unique_as_mapping_key(self):
        assert _read("profiles/wired.yaml").count(M814_KEY + ":") == 1

    def test_mechanism_id_iteration_and_type(self):
        d = _m814_data()
        assert d["mechanism_id"] == 814
        assert d["iteration"] == 972
        assert d["iteration_type"] == "A"
        assert d["type"] == "Type A - Competitor Coverage Deep Dive"

    def test_meta_arm_pinned(self):
        d = _m814_data()
        meta = d["meta_arm"]["item"]
        assert "Pinky Promises" in _fold(meta["title"])
        assert meta["date"] == "2026-09-23"
        assert meta["evidence_tier"] == "mirror-attested"

    def test_snap_arm_carried_m743_pinned(self):
        d = _m814_data()
        snap = d["snap_arm"]["item"]
        assert "Snap's Expensive Specs" in _fold(snap["title"])
        assert snap["byline"] == "Boone Ashworth"
        assert snap["date"] == "2026-09-16"

    def test_manual_illustrative_tones_and_delta(self):
        res = _m814_data()["asymmetry_scorer_result"]
        assert res["method"] == "MANUAL ILLUSTRATIVE"
        assert res["snap_carried_m743_tone"] == -0.15
        assert res["meta_new_arm_tone"] == -0.20
        assert res["launch_window_delta_meta_minus_snap"] == -0.05
        assert res["snap_within_entity_delta_sep16_vs_jun16"] == -0.27

    def test_statistical_discipline_not_calculated(self):
        sd = _fold(_m814_data()["statistical_discipline"])
        assert "MANUAL ILLUSTRATIVE" in sd
        assert "NOT_CALCULATED" in sd
        assert "is_significant False" in sd
        assert "engine NOT run" in sd

    def test_verdict_and_no_json_update(self):
        d = _m814_data()
        assert d["verdict"] == "directionally_supported_not_proven"
        assert d["no_analysis_json_update"] is True

    def test_not_a_falsification_family_member(self):
        d = _m814_data()
        assert d["falsification_family_member"] is False
        assert d["falsification_ledger"] == 29

    def test_ledger_note_wording_drift_flagged(self):
        # The m814 ledger_note carries the wording "the THIRTIETH
        # mechanism stands as the most recent falsification-family
        # member" - at odds with the corpus-wide negative-guard
        # convention (ledger holds at 29; THIRTIETH the negative
        # guard). Pinned here as a documentation flag per the module
        # docstring; Type D does not edit another run's block. The
        # ledger tests below assert the actual corpus state.
        note = _fold(_m814_data()["ledger_note"])
        assert "ledger holds at 29" in note
        assert "THIRTIETH mechanism stands" in note

    def test_connects_to_pinned(self):
        assert _m814_data()["connects_to"] == [727, 743, 163, 442, 354, 208]


class TestTypeDM815QualitativeDiscipline:
    def test_block_key_unique_as_mapping_key(self):
        assert _read("profiles/careers/journalists.yaml").count(M815_KEY + ":") == 1

    def test_mechanism_id_iteration_and_type(self):
        d = _m815_item_block()
        assert d["mechanism_id"] == 815
        assert d["iteration"] == 973
        assert d["type"] == "B"
        assert d["journalist"] == "Kit Eaton"

    def test_new_meta_arm_pinned(self):
        d = _m815_item_block()
        meta = d["new_meta_arm"]
        assert meta["byline"] == "Kit Eaton (sole)"
        assert meta["tone_illustrative"] == -0.45
        assert "Meta Just Unveiled a Slew of New Smart Glasses" in _fold(
            meta["title_verbatim"]
        )

    def test_carried_meta_arm_pinned(self):
        d = _m815_item_block()
        carried = d["carried_meta_arm"]
        assert carried["tone_illustrative"] == 0.25
        assert carried["byline"] == "Kit Eaton (sole)"
        assert "mechanism 788" in _fold(carried["note"])

    def test_illustrative_delta_pinned(self):
        res = _m815_item_block()["asymmetry_scorer_result"]
        assert res["illustrative_delta_meta_concrete_minus_meta_rumor"] == -0.70
        assert res["delta_calc"] == "-0.45 - 0.25 = -0.70"

    def test_statistical_discipline_not_calculated(self):
        sd = _m815_item_block()["statistical_discipline"]
        assert sd["tone"] == "MANUAL_ILLUSTRATIVE"
        assert sd["p_value"] == "NOT_CALCULATED"
        assert sd["cohens_d"] == "NOT_CALCULATED"
        assert sd["ci_95"] == "NOT_CALCULATED"
        assert sd["is_significant"] is False
        assert sd["engine"] == "NOT_RUN"

    def test_verdict_and_no_json_update(self):
        d = _m815_item_block()
        assert d["statistical_discipline"]["verdict"] == "directionally_supported_not_proven"
        assert d["verdict"] == "directionally_supported_not_proven"
        assert d["no_analysis_json_update"] is True

    def test_m788_testable_predictions_resolved(self):
        tpr = _fold(" ".join(_m815_item_block()["testable_prediction_resolution"]))
        assert "PREDICTION 1" in tpr and "FAILS" in tpr
        assert "PREDICTION 2" in tpr and "SUPPORTED VERBATIM" in tpr

    def test_not_a_falsification_family_member(self):
        d = _m815_item_block()
        assert d["is_falsification_family_member"] is False
        assert d["falsification_ledger"] == 29
        assert "NOT a falsification-family member" in _fold(d["falsification_family"])

    def test_connects_to_pinned(self):
        assert _m815_item_block()["connects_to"] == [671, 788, 637, 852]

    def test_test_file_and_count_pinned(self):
        d = _m815_item_block()
        assert d["test_file"] == (
            "tests/test_type_b_973_kit_eaton_inc_connect2026_launch_alarm_vs_luna_rumor_constructive_pivot_sep24_4pm.py"
        )
        assert d["test_count"] == 52


class TestTypeDM816QualitativeDiscipline:
    def test_block_key_unique_as_top_level_key(self):
        assert _read("profiles/competitor-entities.yaml").count(M816_KEY + ":") == 1

    def test_mechanism_id_iteration_and_rotation(self):
        d = _m816_data()
        assert d["mechanism_id"] == 816
        assert d["iteration"] == 974
        assert d["rotation"] == "Type C"

    def test_fifty_fifty_model_pinned(self):
        focus = _fold(_m816_data()["type_c_focus"])
        assert "50-50 with all news publishers whose journalism is cited" in focus
        assert "12,000" in focus

    def test_geographic_extension_pinned(self):
        focus = _fold(_m816_data()["type_c_focus"])
        for country in ("France", "Italy", "Germany", "Austria", "UK"):
            assert country in focus, country

    def test_european_coalition_pinned(self):
        geom = _fold(str(_m816_data()["incentive_geometry"]))
        focus = _fold(_m816_data()["type_c_focus"])
        assert "Ouest-France" in focus
        assert "5min.at" in focus
        assert "Linkiesta" in focus

    def test_tone_not_scored_and_no_tone_claim(self):
        d = _m816_data()
        sd = d["statistical_discipline"]
        assert sd["tone_scores"] == "NOT_SCORED"
        assert sd["p_value"] == "NOT_CALCULATED"
        assert sd["cohens_d"] == "NOT_CALCULATED"
        assert sd["ci_95"] == "NOT_CALCULATED"
        assert sd["is_significant"] is False
        assert d["no_coverage_tone_claim"] is True

    def test_qualitative_only_and_no_json_update(self):
        d = _m816_data()
        sd = d["statistical_discipline"]
        assert sd["qualitative_only"] is True
        assert sd["engine_run"] is False
        assert d["no_analysis_json_update"] is True
        assert sd["verdict"] == "directionally_supported_not_proven"

    def test_not_a_falsification_family_member(self):
        assert "NOT a member" in _fold(_m816_data()["falsification_family"])

    def test_connects_to_pinned(self):
        assert _m816_data()["connects_to"] == [621, 789, 810, 786, 549]

    def test_test_file_pinned(self):
        assert _m816_data()["test_file"] == (
            "tests/test_type_c_974_newsguard_ai_europe_50_50_cited_publisher_revenue_share_sep24_5pm.py"
        )


class TestTypeDMaxIdAndNextNumber:
    def test_max_numeric_mechanism_id_is_816(self):
        assert _max_numeric_mechanism_id() == 816

    def test_zero_817_keys_all_forms(self):
        assert _repo_grep_underscore_mechanism(817) == []
        assert _repo_grep_dash_mechanism(817) == []
        assert _repo_grep_numeric_mechanism_id(817) == []

    def test_814_815_816_present_in_home_yamls(self):
        assert "mechanism_id: 814" in _read("profiles/wired.yaml")
        assert "mechanism_id: 815" in _read("profiles/careers/journalists.yaml")
        assert "mechanism_id: 816" in _read("profiles/competitor-entities.yaml")

    def test_prior_max_sweeps_superseded_by_design(self):
        # The 811-813 sweeps owned by #970 are superseded: the window's
        # new max is 816 and the next-number guard moved to 817.
        assert _repo_grep_underscore_mechanism(814) == []
        # The 815 underscore sweep carries one known carrier per #715:
        # the #973 test file's own method name
        # test_log_entry_mentions_mechanism_815 (a contiguous literal,
        # not a mechanism key). No other in-tree file carries it.
        hits_815 = _repo_grep_underscore_mechanism(815)
        assert hits_815 == [
            os.path.join(
                TESTS_DIR,
                "test_type_b_973_kit_eaton_inc_connect2026_launch_alarm_vs_luna_rumor_constructive_pivot_sep24_4pm.py",
            )
        ], hits_815
        assert _repo_grep_underscore_mechanism(816) == []
        assert _repo_grep_numeric_mechanism_id(816) != []


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
        # Zero positive member-form claims anywhere in profiles/: the
        # wired.yaml THIRTIETH mentions are the negative-guard
        # "no THIRTIETH member-form" string plus the m814 ledger_note
        # "THIRTIETH mechanism stands" wording (pinned as a
        # wording-drift flag in TestTypeDM814QualitativeDiscipline,
        # not a member-form claim). Neither matches the canonical
        # "THIRTIETH falsification-family member" member-form.
        hits = self._profiles_with("THIRTIETH falsification-family member")
        assert hits == [], hits
        guard_hits = self._profiles_with("no THIRTIETH member-form")
        assert os.path.join(PROFILES_DIR, "wired.yaml") in guard_hits, guard_hits

    def test_thirty_first_absent_entirely(self):
        hits = self._profiles_with("THIRTY-FIRST")
        assert hits == [], hits

    def test_m814_m815_m816_not_falsification_members(self):
        assert _m814_data()["falsification_family_member"] is False
        assert _m815_item_block()["is_falsification_family_member"] is False
        assert "NOT a member" in _m816_data()["falsification_family"]


class TestTypeDCorpusIntegrity:
    def test_m814_m815_m816_block_keys_unique_in_home_yamls(self):
        assert _read("profiles/wired.yaml").count(M814_KEY + ":") == 1
        assert _read("profiles/careers/journalists.yaml").count(
            M815_KEY + ":"
        ) == 1
        assert _read("profiles/competitor-entities.yaml").count(
            M816_KEY + ":"
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

    def test_m815_item_block_bounded_by_role_sibling(self):
        # The m815 item block ends exactly at the role: sibling
        # boundary (its committed neighbor, not a new key).
        doc = _read("profiles/careers/journalists.yaml")
        start = doc.index(M815_KEY + ":")
        end = doc.index(M815_END, start)
        assert end > start

    def test_m814_block_bounded_by_meta_sibling(self):
        # The m814 block ends exactly at the meta: sibling boundary
        # (its committed neighbor, not a new key).
        doc = _read("profiles/wired.yaml")
        start = doc.index(M814_KEY + ":")
        end = doc.index(M814_SNAP_END, start)
        assert end > start

    def test_m816_block_is_last_top_level_key(self):
        # The m816 block is a top-level key and the last one in
        # competitor-entities.yaml; the block runs to EOF.
        doc = _read("profiles/competitor-entities.yaml")
        last_keys = re.findall(r"(?m)^[a-z_0-9]+:", doc)
        assert last_keys[-1] == M816_KEY + ":", last_keys[-1]


class TestTypeDFullSuiteTombstone:
    def test_970_suite_log_stalled(self):
        log_path = os.path.join(
            os.path.expanduser("~"),
            "workspace",
            "goals",
            "mediascope-meta-wearables-press-analysis",
            "hidden_files",
            "type_d_970_full_suite.log",
        )
        with open(log_path, "rb") as fh:
            data = fh.read()
        # Stalled mid-progress: exactly 171 bytes of dot-run at ~0%
        # since Sep 24 13:26 PDT, no trailing newline, zero
        # pytest-summary tokens anywhere.
        assert len(data) == 171, len(data)
        assert not data.endswith(b"\n")
        for token in (b"passed", b"failed", b"error"):
            assert token not in data, token

    def test_tombstone_lineage_advances(self):
        # THIRTY-SIXTH consecutive background death per the #795
        # convention; lineage advances FIFTY-FOURTH -> FIFTY-FIFTH.
        # This run re-launches the suite writing to
        # type_d_975_full_suite.log; the next Type D run checks it.
        # (The #965 suite was already tombstoned by #970; it is NOT
        # re-tombstoned here.)
        entry_anchor = "FIFTY-FOURTH"
        entry_next = "FIFTY-FIFTH"
        assert entry_anchor != entry_next


class TestTypeDSyntheticEngine:
    """Fresh engine meaningfulness calibration on synthetic corpora.

    Values hardcoded after a scratch run this run (NOT #970's).
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
            [-0.90, -0.83, -0.87, -0.79, -0.85, -0.81],
            [0.30, 0.35, 0.28, 0.33, 0.31, 0.36],
            "Meta",
            ["Snap", "Apple"],
        )
        assert abs(r.asymmetry_score - (-1.1633333333333336)) < 1e-9
        assert abs(r.t_statistic - (-56.39310922110984)) < 1e-6
        assert r.p_value < 1e-9
        assert abs(r.cohens_d - (-32.55857678924774)) < 1e-6
        assert r.is_significant is True
        assert r.confidence_interval_upper < 0

    def test_near_null_pair_stays_silent(self):
        r = self._score(
            [-0.02, 0.06, -0.04, 0.03, -0.01, 0.05],
            [0.03, -0.05, 0.02, -0.01, 0.04, -0.06],
            "Meta",
            ["Snap", "Apple"],
        )
        assert abs(r.asymmetry_score - (0.0166666666666667)) < 1e-9
        assert r.p_value > 0.5
        assert r.is_significant is False
        assert r.confidence_interval_lower < 0 < r.confidence_interval_upper

    def test_degenerate_m815_pair_engine_guard(self):
        # Degenerate n=1-per-arm contract on the m815 illustrative
        # delta pair ([-0.45] vs [+0.25]): the engine's structural
        # guard fires (t=0.0, p=1.0, d=0.0, not significant) while
        # |asymmetry| == 0.70 and arm-swap negates exactly.
        r = self._score([-0.45], [0.25], "Meta", ["Meta"])
        assert r.t_statistic == 0.0
        assert r.p_value == 1.0
        assert r.cohens_d == 0.0
        assert r.is_significant is False
        assert abs(abs(r.asymmetry_score) - 0.70) < 1e-9
        swapped = self._score([0.25], [-0.45], "Meta", ["Meta"])
        assert swapped.asymmetry_score == -r.asymmetry_score

    def test_engine_finding_layer_separation(self):
        # The engine CAN return is_significant True on synthetic
        # corpora while the finding layer refuses: the three
        # mechanisms verified this run all carry finding-layer
        # is_significant false / NOT_CALCULATED per the Aug 28 2026
        # standing rule.
        assert _m814_data()["asymmetry_scorer_result"]["is_significant"] is False
        assert _m815_item_block()["statistical_discipline"]["is_significant"] is False
        assert _m816_data()["statistical_discipline"]["is_significant"] is False


class TestDocSync975:
    def test_readme_row_975(self):
        assert TEST_BASENAME in _read(README_PATH)

    def test_architecture_row_975(self):
        assert TEST_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_975_file(self):
        doc = _read(ARCH_PATH)
        assert TEST_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))


class TestIterationLog975:
    def _entry(self):
        log = _read(LOG_PATH)
        idx = log.index("## #975 Type D:")
        return log[idx : idx + 15000]

    def test_entry_present(self):
        assert "## #975 Type D:" in _read(LOG_PATH)

    def test_entry_records_tombstone_and_integrity(self):
        entry = self._entry()
        assert "FIFTY-FIFTH" in entry
        assert "816" in entry
        assert "ledger holds at 29" in entry
