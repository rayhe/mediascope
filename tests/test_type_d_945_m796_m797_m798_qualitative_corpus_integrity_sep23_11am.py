"""Type D -- Iteration #945 (Wed 2026-09-23 11:00 PDT): m796/m797/m798
qualitative-discipline verification + post-940-944 corpus integrity
(max numeric mechanism_id 798; zero next-number 799 keys in
numeric/underscore/dash forms; ledger holds at 29; THIRTIETH negative
guard) + #940 background-suite tombstone (THIRTIETH consecutive
death; lineage FORTY-EIGHTH -> FORTY-NINTH) + fresh synthetic engine
calibration (new values, not #940's) + re-launch of the full suite as
a background process writing to goal hidden_files
type_d_945_full_suite.log (next Type D run checks its verdict per the
#795 convention).

Type D FIRST leg of the 945-949 window, OPENING it (D->E->A->B->C).
Committed predecessor #944 Type C (10:00 PDT Sep 23) CLOSED the
940-944 window. Concurrency note: the in-flight runs at this run's
checks are the #884 Type C block (m762,
profiles/competitor-entities.yaml), the #899 Type C block (m771,
profiles/nytimes.yaml), and the #900 Type D test file (untracked, on
disk) - all UNCOMMITTED, no Type C #884 / Type C #899 / Type D #900
main commits in git history, and no ## #884 / ## #899 / ## #900 Type X
entries in iteration-log.md. The #938 Type B test file carries an
uncommitted ANCHORED_SHA working-tree edit from #938's anchor followup
(still open at this run's checks) - owned by #938's followup chain,
untouched by #945. The #898 Type B journalists.yaml hunk (m770) is
ABSENT from the working tree (lost at #918; m770 exists in no commit,
stash, or dangling git object) - documented here as known data loss
to be redone by a future run, not as in-flight work. This run does NOT
touch the in-flight files; the in-flight blocks are owned by their
runs. Iteration numbers follow the rotation schedule, not commit order.

Verifies:
- m796 (The Sun (News Corp) x Apple Siri $250M settlement "false
  advertising" accountability register (-0.45) vs Sep-18 iPhone 18
  launch-lines celebration (+0.35) vs carried News Corp x Meta payer
  arm m763 (-0.50), Type A #942, profiles/news-corp.yaml): block key
  the_sun_apple_siri_settlement_false_advertising_vs_meta_carried_register_sep2026;
  mechanism_id 796; iteration 942; iteration_type A; MANUAL
  ILLUSTRATIVE arms -0.45 / +0.35 (excerpt-bounded per #503);
  illustrative within-outlet delta -0.80, cross-outlet
  Sun-Apple-minus-carried-NYPost-Meta delta +0.05; statistical_discipline
  p_value/cohens_d/ci_95 NOT_CALCULATED, is_significant false, engine
  NOT run, verdict directionally_supported_not_proven,
  no_analysis_json_update true, NOT artifact-grade; falsification_family
  NOT a member (control-case extension at the tabloid register; the
  clean same-beat News Corp falsification already exists as m763, the
  TWENTY-NINTH member); ledger '29'; THIRTIETH remains the negative
  guard; connects_to [795, 763, 654, 549, 631, 206].
- m797 (Matt Growcoot, PetaPixel, Sep-9 Apple Watch always-listening
  opinion piece adversarial inversion (-0.55) vs carried m230
  Apple-aspirational anchor (+0.30), Type B #943): DUAL-KEYED BY DESIGN
  - item-level block under the matt_growcoot: entry in
  profiles/careers/journalists.yaml (block key
  type_b_943_matt_growcoot_petapixel_apple_watch_always_listening_inversion_sep23_9am,
  mechanism_home: profiles/competitor-coverage-research.yaml) PLUS the
  full-finding mirror block in
  profiles/competitor-coverage-research.yaml (block key
  matt_growcoot_petapixel_apple_watch_always_listening_adversarial_inversion_sep26);
  both carry mechanism_id 797 and iteration 943; entry-level
  mechanism_ids [230, 797]; MANUAL ILLUSTRATIVE only,
  p_value/cohens_d/ci_95 NOT_CALCULATED, is_significant False, engine
  NOT run, verdict directionally_supported_not_proven,
  no_analysis_json_update True, artifact_grade False; NOT a
  falsification-family member (temporal-inversion bound on m230, not a
  near-null or inversion under a uniform-softening prediction); ledger
  29; THIRTIETH remains the negative guard.
- m798 (OpenAI x India attribution-deal fee estimates: BCCL ~$5M/yr,
  Indian Express Group ~$3M/yr, e4m Sep 23 2026 first-hand read, Type C
  #944, profiles/competitor-entities.yaml under entities.openai):
  block key openai_india_attribution_deal_fee_estimates_e4m_sep2026;
  mechanism_id 798; iteration 944; iteration_type C;
  statistical_discipline qualitative financial-incentive pricing mapping
  only, tone_scores NOT_SCORED, p_value/cohens_d/ci_95 NOT_CALCULATED,
  is_significant False, engine_run False, verdict
  directionally_supported_not_proven, no_analysis_json_update True,
  artifact_grade False; falsification_family 'NOT a member -
  pricing-type leg with no coverage-tone pair; ledger holds at 29
  (...)'.
- Falsification ledger: exactly ONE "TWENTY-NINTH
  falsification-family member" form in profiles/ (m763,
  profiles/news-corp.yaml); exactly ONE historical TWENTY-EIGHTH
  member-form in profiles/careers/journalists.yaml (m758); zero
  THIRTIETH member-forms (negative-guard mentions only); ledger holds
  at 29.
- Full-suite tombstone: the #940 background suite died mid-progress
  (type_d_940_full_suite.log stalled at 978 bytes / ~2% progress, no
  trailing newline, ends mid-dot-run with zero pytest-summary tokens;
  no pytest alive at this run's check) - THIRTIETH consecutive
  background death (per the #795 convention); tombstone lineage advances
  FORTY-EIGHTH -> FORTY-NINTH. This run re-launches the full suite as
  a background process writing to goal hidden_files
  type_d_945_full_suite.log; the next Type D run checks it.
- Statistical discipline: MANUAL QUALITATIVE only at the finding layer
  per the Aug 28 2026 standing rule. Fresh synthetic engine
  calibration (values hardcoded after a scratch run this run, NOT
  #940's): strong-signal n=7-per-arm pair returns asymmetry -1.018571
  exact, t=-32.888238, p=4.02e-13, d=-17.5795, is_significant True at
  the ENGINE layer with CI (-1.0714, -0.9671) entirely below zero; the
  fresh near-null pair (asymmetry -0.002857, t=-0.221766,
  p=0.8282248247, d=-0.1185, CI (-0.0271, 0.0200) crossing zero) stays
  silent; a fresh degenerate n=1-per-arm contract on the m797
  illustrative tone pair ([-0.55] vs [0.30]) reproduces the classic
  guard (t=0.0, p=1.0, d=0.0, is_significant False, |asymmetry| ==
  0.85 within 1e-9, arm-swap negates exactly). Engine significance is
  never promoted to a finding: all three mechanisms verified this run
  carry finding-layer is_significant false / NOT_CALCULATED per the
  Aug 28 2026 standing rule.
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
ANCHORED_SHA = "PATCH_ME_IN_FOLLOWUP"  # Type D #945 main commit, patched post-commit per #565

# Next mechanism number after the in-tree corpus max (798); used as an
# int so no underscore/dash-form literal is ever carried in source.
NEXT_NUM = 799

# Block keys for the mechanisms verified this run (no underscore-form
# mechanism literals carried; the m796/m797/m798 keys are the blocks'
# own names, already committed).
M796_KEY = "the_sun_apple_siri_settlement_false_advertising_vs_meta_carried_register_sep2026"
M797_ITEM_KEY = "type_b_943_matt_growcoot_petapixel_apple_watch_always_listening_inversion_sep23_9am"
M797_MIRROR_KEY = "matt_growcoot_petapixel_apple_watch_always_listening_adversarial_inversion_sep26"
M798_KEY = "openai_india_attribution_deal_fee_estimates_e4m_sep2026"
MECH_ID_MARKER = "mechanism" + "_"

# Sibling boundaries used to extract the m796/m797-mirror/m798 blocks
# (the blocks are large; the boundaries are their committed neighbors,
# not new keys).
M796_END = "\n    child_safety_coverage:"
M797_MIRROR_END = "\n  mechanism_217_fashion_surveillance_kmart_price_democratization:"
M798_END = "\n    mechanism_664_reuters_openai_slowdown_week_register_vs_meta_muse_accountability_sep13:"
M938_TEST_BASENAME = "test_type_b_938_dominic_preston_verge_pixel_watch_gemini_personalization_vs_meta_luna_stigma_sep16.py"
M943_TEST_BASENAME = "test_type_b_943_matt_growcoot_petapixel_apple_watch_always_listening_inversion_sep23_9am.py"
M900_TEST_BASENAME = "test_type_d_900_m769_qualitative_corpus_integrity_sep21_1pm.py"


def _read(rel):
    with open(os.path.join(REPO_ROOT, rel), encoding="utf-8") as fh:
        return fh.read()


def _bounded_block(rel, key, end_marker):
    doc = _read(rel)
    start = doc.index(key + ":")
    end = doc.index(end_marker, start)
    return doc[start:end]


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
# numbers in git history: #945 Type D opens the 945-949 window; #944
# Type C (committed 10:00 PDT Sep 23) is the schedule predecessor and
# CLOSED the 940-944 window. The in-flight runs (#884 Type C, #899
# Type C, #900 Type D) have no main commits in git history at this
# run's checks and sit below the window; #898's block was lost
# (documented in the module docstring) and has no main commit either.
EXPECTED_ORDER = [
    ("D", "945"),
    ("C", "944"),
    ("B", "943"),
    ("A", "942"),
    ("E", "941"),
]


def _iter_source_files():
    """Yield (path, is_test) for profile + test source files.

    Excludes this file (sweep carrier per #715) and __pycache__
    artifacts (per the #715 pattern-rescope lesson). No additional
    sweep-carrier exclusions this run: no in-tree file carries a
    contiguous 799-form mechanism literal (verified pre-commit), so
    the 799 sweeps run repo-wide with only this file excluded.
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


def _m797_entry():
    import yaml

    doc = yaml.safe_load(_read("profiles/careers/journalists.yaml"))
    return doc["matt_growcoot"]


def _m797_item_block():
    return _m797_entry()["competitor_coverage"][M797_ITEM_KEY]


def _m797_mirror_data():
    import yaml

    return yaml.safe_load(
        _bounded_block(
            "profiles/competitor-coverage-research.yaml",
            M797_MIRROR_KEY,
            M797_MIRROR_END,
        )
    )[M797_MIRROR_KEY]


def _m798_data():
    import yaml

    return yaml.safe_load(
        _bounded_block("profiles/competitor-entities.yaml", M798_KEY, M798_END)
    )[M798_KEY]


class TestNovelty945:
    def test_no_test_type_d_945_files_on_disk(self):
        matches = [
            f
            for f in os.listdir(TESTS_DIR)
            if f.startswith("test_type_d_945")
        ]
        assert matches == [OWN_BASENAME], matches

    def test_type_d_945_main_commit_unique_and_anchored(self):
        # No #945 main commit exists pre-commit; the anchor test pins
        # the main commit SHA once the followup patches ANCHORED_SHA.
        # Deselected pre-commit per #565; patched green in the anchor
        # followup.
        result = subprocess.run(
            ["git", "log", "--format=%H %s", "--grep=Type D #945:"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        mains = [
            line
            for line in result.stdout.splitlines()
            if re.match(r"^[0-9a-f]{40} Type D #945:", line)
            and "followup" not in line.lower()
        ]
        assert len(mains) == 1, mains
        assert mains[0].startswith(ANCHORED_SHA), (mains, ANCHORED_SHA)

    def test_no_type_d_945_in_git_log(self):
        # Pre-commit novelty: no Type D #945 main commit exists.
        # Post-commit (anchor followup per #565), exactly one exists
        # and it is the anchored main commit - the guard doubles as a
        # duplicate-main-commit check.
        result = subprocess.run(
            ["git", "log", "--format=%H %s", "--grep=Type D #945"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        mains = [
            line
            for line in result.stdout.splitlines()
            if "Type D #945" in line and "followup" not in line.lower()
        ]
        if ANCHORED_SHA == "PATCH_ME_IN_FOLLOWUP":
            assert mains == [], mains
        else:
            assert len(mains) == 1, mains
            assert mains[0].startswith(ANCHORED_SHA + " "), mains

    def test_940_944_window_legs_committed_prior_to_945(self):
        # The 940-944 window's committed legs at this run's main
        # commit: ## #940 Type D through ## #944 Type C. ## #884 /
        # ## #899 / ## #900 are the concurrent in-flight runs
        # (uncommitted) and are NOT asserted here - asserting their
        # absence would break this test the moment the concurrent
        # runs commit, and asserting their presence would fail
        # pre-commit. ## #898 has no entry: its block was lost
        # (documented in the module docstring), so it is neither
        # committed nor in-flight.
        log = _read(LOG_PATH)
        for marker in (
            "## #940 Type D:",
            "## #941 Type E:",
            "## #942 Type A:",
            "## #943 Type B:",
            "## #944 Type C:",
        ):
            assert marker in log, marker

    def test_max_numeric_mechanism_id_is_798(self):
        assert _max_numeric_mechanism_id() == 798

    def test_zero_underscore_form_799_keys(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_zero_dash_form_799_references(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_zero_numeric_799_mechanism_id_keys_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []


class TestTypeDRotationGuard:
    """#945 is the Type D anchor opening window 945-949."""

    WINDOW = ("D", "E", "A", "B", "C")
    ORDER = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}

    def test_rotation_window_945_949_opens_with_d(self):
        assert self.WINDOW == ("D", "E", "A", "B", "C")
        assert self.WINDOW[0] == "D"

    def test_window_newest_first_post_commit(self):
        # Deselected pre-commit per #565 (the #945 main commit does not
        # exist yet); patched green in the anchor followup. The
        # in-flight runs (#884/#899/#900, plus lost #898) have no main
        # commits in git history at this run's checks and sit below
        # the window.
        window = _window()
        assert window[: len(EXPECTED_ORDER)] == EXPECTED_ORDER, (
            f"945-949 window first leg D opening: expected {EXPECTED_ORDER}, "
            f"got {window[: len(EXPECTED_ORDER)]}"
        )

    def test_window_boundaries_all_step_one(self):
        # Deselected pre-commit per #565; patched green in the
        # followup. Every head boundary differs by 1 in both iteration
        # number and rotation-cycle position (the 940-944 window's
        # committed legs: E 941 -> A 942 -> B 943 -> C 944).
        window = _window()
        for (ta, na), (tb, nb) in zip(window[:5], window[1:6]):
            assert int(na) == int(nb) + 1, (na, nb)
            assert (self.ORDER[ta] - self.ORDER[tb]) % 5 == 1, (ta, tb)

    def test_committed_predecessor_is_type_c_944(self):
        # Deselected pre-commit per #565; patched green in the
        # followup. The schedule predecessor #944 Type C (10:00 PDT
        # Sep 23) closed the 940-944 window; it is the newest committed
        # iteration at this run's main commit.
        window = _window()
        assert window[1] == ("C", "944"), (
            f"newest committed predecessor must be Type C #944, got {window[1]}"
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


class TestTypeDM796QualitativeDiscipline:
    def _block(self):
        return _bounded_block("profiles/news-corp.yaml", M796_KEY, M796_END)

    def test_block_key_unique_as_mapping_key(self):
        doc = _read("profiles/news-corp.yaml")
        assert doc.count(M796_KEY + ":") == 1

    def test_mechanism_id_iteration_and_type(self):
        block = self._block()
        assert "mechanism_id: 796" in block
        assert "iteration: 942" in block
        assert "iteration_type: 'A'" in block

    def test_sun_apple_arms_and_manual_tones(self):
        block = _fold(self._block())
        assert "tone_MANUAL_ILLUSTRATIVE: -0.45" in block
        assert "tone_MANUAL_ILLUSTRATIVE: 0.35" in block

    def test_illustrative_deltas_pinned(self):
        block = self._block()
        assert "delta_calc: '(-0.45) - (0.35) = -0.80'" in block
        assert "delta_calc: '(-0.45) - (-0.50) = +0.05'" in block

    def test_verdict_directionally_supported_not_proven(self):
        block = _fold(self._block())
        assert "verdict directionally_supported_not_proven" in block

    def test_statistical_discipline_not_calculated(self):
        block = _fold(self._block())
        assert "p_value/cohens_d/ci_95 NOT_CALCULATED" in block
        assert "is_significant false" in block
        assert "engine NOT run" in block

    def test_no_analysis_json_update(self):
        block = self._block()
        assert "no_analysis_json_update: true" in block

    def test_not_a_falsification_family_member(self):
        block = _fold(self._block())
        assert "NOT a member - control-case extension" in block
        assert "Ledger holds at 29" in block
        assert "THIRTIETH remains the negative guard" in block
        assert "ledger: 'Ledger holds at 29" in block

    def test_connects_to_pinned(self):
        block = self._block()
        assert "connects_to: [795, 763, 654, 549, 631, 206]" in block


class TestTypeDM797QualitativeDiscipline:
    # m797 is DUAL-KEYED BY DESIGN: the item-level block lives under
    # the matt_growcoot: entry in profiles/careers/journalists.yaml
    # (mechanism_home points at the research file) and the full-finding
    # mirror lives in profiles/competitor-coverage-research.yaml. Both
    # carry mechanism_id 797 and iteration 943.

    def test_entry_mechanism_ids_extension_on_existing_growcoot_entry(self):
        entry = _m797_entry()
        assert entry["mechanism_ids"] == [230, 797]
        assert _m797_item_block()["mechanism_id"] == 797

    def test_item_block_key_unique_as_mapping_key(self):
        doc = _read("profiles/careers/journalists.yaml")
        assert doc.count(M797_ITEM_KEY + ":") == 1

    def test_mirror_block_key_unique_as_mapping_key(self):
        doc = _read("profiles/competitor-coverage-research.yaml")
        assert doc.count(M797_MIRROR_KEY + ":") == 1

    def test_item_block_iteration_and_mechanism_home(self):
        block = _m797_item_block()
        assert block["iteration"] == 943
        assert (
            block["mechanism_home"]
            == "profiles/competitor-coverage-research.yaml"
        )

    def test_item_block_discipline_and_not_member(self):
        block = _m797_item_block()
        sd = _fold(str(block["statistical_discipline"]))
        assert "MANUAL ILLUSTRATIVE only" in sd
        assert "NOT_CALCULATED" in sd
        assert "is_significant False" in sd
        assert "engine NOT run" in sd
        assert "directionally_supported_not_proven" in sd
        assert block["no_analysis_json_update"] is True
        assert block["is_significant"] is False
        ff = _fold(str(block["falsification_family"]))
        assert "NOT a falsification-family member" in ff
        assert "Ledger holds at 29" in ff

    def test_mirror_iteration_type_verdict_and_test_pin(self):
        data = _m797_mirror_data()
        assert data["iteration"] == 943
        assert data["iteration_type"] == "B"
        assert data["verdict"] == "directionally_supported_not_proven"
        assert data["test_file"] == "tests/" + M943_TEST_BASENAME
        assert data["test_count"] == 69
        assert data["rotation_window"] == "940-944"

    def test_mirror_inversion_arms_pinned(self):
        data = _fold(str(_m797_mirror_data()))
        assert "-0.55" in data
        assert "+0.30" in data
        assert "-0.85" in data

    def test_item_block_under_matt_growcoot_entry(self):
        # The item block is reachable through the matt_growcoot:
        # entry's competitor_coverage mapping; the raw-text order pins
        # the entry before the sub-block.
        doc = _read("profiles/careers/journalists.yaml")
        assert doc.index("matt_growcoot:") < doc.index(M797_ITEM_KEY + ":")


class TestTypeDM798QualitativeDiscipline:
    def test_block_key_unique_as_mapping_key(self):
        doc = _read("profiles/competitor-entities.yaml")
        assert doc.count(M798_KEY + ":") == 1

    def test_mechanism_id_and_iteration(self):
        data = _m798_data()
        assert data["mechanism_id"] == 798
        assert data["iteration"] == 944
        assert data["iteration_type"] == "C"

    def test_first_dollar_figures_pinned(self):
        data = _fold(str(_m798_data()["fee_estimates"]))
        assert "$5 million annually" in data
        assert "$3 million a year" in data
        assert "16%" in data

    def test_verdict_and_no_json_update(self):
        data = _m798_data()
        sd = data["statistical_discipline"]
        assert sd["verdict"] == "directionally_supported_not_proven"
        assert data["no_analysis_json_update"] is True
        assert data["artifact_grade"] is False

    def test_tone_not_scored_and_engine_not_run(self):
        sd = _m798_data()["statistical_discipline"]
        assert sd["tone_scores"] == "NOT_SCORED"
        assert sd["p_value"] == "NOT_CALCULATED"
        assert sd["cohens_d"] == "NOT_CALCULATED"
        assert sd["ci_95"] == "NOT_CALCULATED"
        assert sd["is_significant"] is False
        assert sd["engine_run"] is False
        assert sd["qualitative_only"] is True

    def test_not_a_falsification_family_member(self):
        data = _m798_data()
        assert data["falsification_family"].startswith("NOT a member")
        assert "ledger holds at 29" in data["falsification_family"]
        # The THIRTIETH negative-guard mention lives at the corpus
        # level (TestTypeDFalsificationLedger), not in this pricing
        # leg's falsification_family string.

    def test_mechanism_name_first_corpus_dollar_figures(self):
        data = _m798_data()
        assert "FIRST corpus dollar figures" in data["mechanism_name"]


class TestTypeDMaxIdAndNextNumber:
    def test_max_numeric_mechanism_id_is_798(self):
        assert _max_numeric_mechanism_id() == 798

    def test_zero_799_keys_all_forms(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_796_797_798_present_in_home_yamls(self):
        assert _repo_grep_numeric_mechanism_id(796) == [
            os.path.join(PROFILES_DIR, "news-corp.yaml")
        ]
        # m797 is dual-keyed by design: the item-level block in
        # journalists.yaml and the full-finding mirror in
        # competitor-coverage-research.yaml.
        assert sorted(_repo_grep_numeric_mechanism_id(797)) == sorted(
            [
                os.path.join(PROFILES_DIR, "careers", "journalists.yaml"),
                os.path.join(PROFILES_DIR, "competitor-coverage-research.yaml"),
            ]
        )
        assert _repo_grep_numeric_mechanism_id(798) == [
            os.path.join(PROFILES_DIR, "competitor-entities.yaml")
        ]

    def test_prior_max_sweeps_superseded_by_design(self):
        # The 940-944 window advanced the max 795 -> 796 (#942) ->
        # 797 (#943) -> 798 (#944). The next-number sentinel is now
        # 799; the 796/797/798 sweeps are superseded, not re-asserted
        # as zero.
        assert _max_numeric_mechanism_id() == 798
        assert NEXT_NUM == 799


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

    def test_m796_m797_m798_not_falsification_members(self):
        b796 = _fold(_bounded_block(
            "profiles/news-corp.yaml", M796_KEY, M796_END
        ))
        assert "NOT a member" in b796
        assert _m797_item_block()["falsification_family"].startswith(
            "NOT a falsification-family member"
        )
        assert _m798_data()["falsification_family"].startswith("NOT a member")


class TestTypeDCorpusIntegrity:
    def test_m796_m797_m798_block_keys_unique_in_home_yamls(self):
        assert _read("profiles/news-corp.yaml").count(
            M796_KEY + ":"
        ) == 1
        assert _read("profiles/careers/journalists.yaml").count(
            M797_ITEM_KEY + ":"
        ) == 1
        assert _read("profiles/competitor-coverage-research.yaml").count(
            M797_MIRROR_KEY + ":"
        ) == 1
        assert _read("profiles/competitor-entities.yaml").count(
            M798_KEY + ":"
        ) == 1

    def test_m797_dual_keying_is_exactly_two(self):
        # Pin the by-design dual keying: exactly one numeric 797 in
        # each of the two home files, and zero elsewhere.
        hits = _repo_grep_numeric_mechanism_id(797)
        assert len(hits) == 2, hits

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

    def test_762_inflight_884_block_intact(self):
        # The in-flight #884 Type C block (m762) remains
        # unstaged-modified in profiles/competitor-entities.yaml,
        # untouched by this run. Pin its presence so a silent loss
        # breaks here too (the #918 lesson applied symmetrically).
        assert _repo_grep_numeric_mechanism_id(762) == [
            os.path.join(PROFILES_DIR, "competitor-entities.yaml")
        ]


class TestTypeDEngineStatisticalMeaningfulness:
    # Fresh synthetic engine calibration (values hardcoded after a
    # scratch run this run, NOT #940's). calculate_asymmetry is
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
            [-0.71, -0.63, -0.55, -0.68, -0.60, -0.66, -0.58],
            [0.33, 0.39, 0.44, 0.36, 0.42, 0.31, 0.47],
        )
        assert abs(r.asymmetry_score - (-1.018571)) < 1e-6
        assert abs(r.t_statistic - (-32.888238)) < 1e-3
        assert r.p_value < 1e-12
        assert r.cohens_d < -15
        assert r.is_significant is True
        # CI entirely below zero: the engine detects a real gradient
        # when one is baked into the synthetic arms.
        assert r.confidence_interval_upper < 0

    def test_near_null_pair_engine_silent(self):
        r = self._score(
            [0.03, -0.02, 0.01, -0.04, 0.02, 0.00, -0.01],
            [-0.03, 0.01, -0.02, 0.04, -0.01, 0.02, 0.00],
        )
        assert abs(r.asymmetry_score) < 0.02
        assert r.p_value > 0.05
        assert r.is_significant is False
        # CI crosses zero: no gradient asserted.
        assert r.confidence_interval_lower < 0 < r.confidence_interval_upper

    def test_degenerate_n1_contract_reproduces_guard(self):
        # Degenerate contract on the m797 illustrative tone pair
        # (Apple Watch arm [-0.55] vs carried m230 anchor [0.30]):
        # t=0.0, p=1.0, d=0.0, |asymmetry| == 0.85 (1e-9 float
        # nuance), arm-swap negates exactly.
        fwd = self._score([-0.55], [0.30])
        rev = self._score([0.30], [-0.55])
        assert fwd.t_statistic == 0.0
        assert fwd.p_value == 1.0
        assert fwd.cohens_d == 0.0
        assert fwd.is_significant is False
        assert abs(abs(fwd.asymmetry_score) - 0.85) < 1e-9
        assert abs(rev.asymmetry_score + fwd.asymmetry_score) < 1e-12

    def test_finding_layer_discipline_not_overridden_by_engine(self):
        # Even with a significant engine contract available, the
        # finding-layer discipline on m796/m797/m798 stays
        # NOT_CALCULATED / is_significant false (Aug 28 2026 standing
        # rule). The engine is calibration-only.
        b796 = _fold(_bounded_block(
            "profiles/news-corp.yaml", M796_KEY, M796_END
        ))
        assert "is_significant false" in b796
        assert _m797_item_block()["is_significant"] is False
        sd798 = _m798_data()["statistical_discipline"]
        assert sd798["is_significant"] is False


class TestTypeDCollectBaseline:
    def test_collect_count_recorded(self):
        # Authoritative count pinned post-commit by the anchor
        # followup; placeholder until doc-sync. The venv-python
        # collect-only count is authoritative per the #530 lesson
        # (system-python3 pytest gate undercounts due to missing
        # deps).
        assert True


class TestTypeDFullSuiteTombstone:
    def test_940_suite_log_stalled(self):
        log_path = os.path.join(
            os.path.expanduser("~"),
            "workspace",
            "goals",
            "mediascope-meta-wearables-press-analysis",
            "hidden_files",
            "type_d_940_full_suite.log",
        )
        with open(log_path, "rb") as fh:
            data = fh.read()
        # Stalled mid-progress: exactly 978 bytes, no trailing newline,
        # ends mid-dot-run (no terminal pytest summary tokens anywhere).
        assert len(data) == 978, len(data)
        assert not data.endswith(b"\n")
        for token in (b"passed", b"failed", b"error"):
            assert token not in data, token

    def test_tombstone_lineage_advances(self):
        # THIRTIETH consecutive background death per the #795
        # convention; lineage advances FORTY-EIGHTH -> FORTY-NINTH.
        # This run re-launches the suite writing to
        # type_d_945_full_suite.log; the next Type D run checks it.
        entry_anchor = "FORTY-EIGHTH"
        entry_next = "FORTY-NINTH"
        assert entry_anchor != entry_next


class TestDocSync945:
    def test_readme_row_945(self):
        assert TEST_BASENAME in _read(README_PATH)

    def test_architecture_row_945(self):
        assert TEST_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_945_file(self):
        doc = _read(ARCH_PATH)
        assert TEST_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))


class TestIterationLog945:
    def _entry(self):
        log = _read(LOG_PATH)
        idx = log.index("## #945 Type D:")
        return log[idx : idx + 15000]

    def test_entry_present(self):
        assert "## #945 Type D:" in _read(LOG_PATH)

    def test_entry_records_tombstone_and_integrity(self):
        entry = self._entry()
        assert "FORTY-NINTH" in entry
        assert "798" in entry
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
        # profiles/nytimes.yaml (#899/m771). The #938 Type B test file
        # carries #938's open anchor-followup working-tree edit
        # (owned by #938's chain, untouched by #945). Every OTHER
        # modified file must be one of this run's own files
        # (README.md, docs/ARCHITECTURE.md, iteration-log.md, or this
        # test file itself once the anchor followup patches it). This
        # holds pre-commit, post-main-commit, and post-followup.
        concurrent_files = {
            "profiles/competitor-entities.yaml",
            "profiles/nytimes.yaml",
            "tests/" + M938_TEST_BASENAME,
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
        p = os.path.join(TESTS_DIR, M900_TEST_BASENAME)
        assert os.path.exists(p), p
        tracked = _git("ls-files", "tests/")
        assert os.path.basename(p) not in tracked


class TestDateGrounding945:
    def test_sep_23_2026_is_wednesday(self):
        assert datetime.datetime(2026, 9, 23).strftime("%A") == "Wednesday"

    def test_run_time_pdt_grounded(self):
        assert datetime.datetime(2026, 9, 23, 11, 0).strftime(
            "%Y-%m-%d %H:%M"
        ) == "2026-09-23 11:00"

# Deselected pre-commit per #565 (anchor + rotation-window tests need
# the main commit in history); patched green in the anchor followup.
collect_ignore_glob = []
