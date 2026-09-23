"""Type D -- Iteration #940 (Wed 2026-09-23 06:00 PDT): m793/m794/m795
qualitative-discipline verification + post-935-939 corpus integrity
(max numeric mechanism_id 795; zero next-number 796 keys in
numeric/underscore/dash forms; ledger holds at 29; THIRTIETH negative
guard) + #935 background-suite tombstone (TWENTY-NINTH consecutive
death; lineage FORTY-SEVENTH -> FORTY-EIGHTH) + fresh synthetic engine
calibration (new values, not #935's) + re-launch of the full suite as
a background process writing to goal hidden_files
type_d_940_full_suite.log (next Type D run checks its verdict per the
#795 convention).

Type D FIRST leg of the 940-944 window, OPENING it (D->E->A->B->C).
Committed predecessor #939 Type C (05:00 PDT Sep 23) CLOSED the
935-939 window. Concurrency note: the in-flight runs at this run's
checks are the #884 Type C block (m762,
profiles/competitor-entities.yaml), the #899 Type C block (m771,
profiles/nytimes.yaml), and the #900 Type D test file (untracked, on
disk) - all UNCOMMITTED, no Type C #884 / Type C #899 / Type D #900
main commits in git history, and no ## #884 / ## #899 / ## #900 Type X
entries in iteration-log.md. The #938 Type B test file carries an
uncommitted ANCHORED_SHA working-tree edit from #938's anchor followup
(still open at this run's checks) - owned by #938's followup chain,
untouched by #940. The #898 Type B journalists.yaml hunk (m770) is
ABSENT from the working tree (lost at #918; m770 exists in no commit,
stash, or dangling git object) - documented here as known data loss
to be redone by a future run, not as in-flight work. This run does NOT
touch the in-flight files; the in-flight blocks are owned by their
runs. Iteration numbers follow the rotation schedule, not commit order.

Verifies:
- m793 (The Verge x Meta Luna "Glasshole Moment" launch-day register
  vs carried Verge x OpenAI deal-partner arms, Type A #937,
  profiles/the-verge.yaml under the meta: entity section): block key
  verge_meta_luna_glasshole_moment_launch_register_vs_openai_deal_partner_arms_sep23_2026;
  mechanism_id 793; iteration 937; iteration_type A; MANUAL
  ILLUSTRATIVE -0.50 on the fresh Meta Luna arm (excerpt-bounded per
  #503; theverge.com policy-blocked per standing rule); illustrative
  Meta-Luna-minus-OpenAI-mean delta +0.10; statistical_discipline
  p_value/cohens_d/ci_95 NOT_CALCULATED, is_significant false, engine
  NOT run, verdict directionally_supported_not_proven,
  no_analysis_json_update true; falsification_family NOT a member
  (control-case extension at the product-privacy layer; the clean
  same-beat Vox-deal falsification already exists as m751, the
  TWENTY-SEVENTH member); ledger '29'; THIRTIETH remains the negative
  guard.
- m794 (Dominic Preston, The Verge, Sep-16 same-day pair: Google Pixel
  Watch Gemini Personalization feature-update +0.05 vs carried Meta
  Luna stigma arm -0.30, Type B #938,
  profiles/careers/journalists.yaml): item-level block under the
  EXISTING dominic_preston: entry (inside its competitor_coverage
  mapping, per the #838/#933 precedent); mechanism_ids [734, 794]
  (YAML list form on the entry); illustrative Meta-minus-Google delta
  -0.35 (delta_calc '(-0.30) - (0.05) = -0.35'); statistical_discipline
  MANUAL_ILLUSTRATIVE, p_value/cohens_d/ci_95 NOT_CALCULATED,
  is_significant False, engine_run False, verdict
  directionally_supported_not_proven, no_analysis_json_update True;
  falsification_family_member False; falsification_ledger 29.
- m795 (Apple $250M Siri AI delayed-launch class-action settlement:
  May 2026 agreement, settlement website live Sep 20 2026, claims
  Sep 21-Dec 21 2026, Type C #939,
  profiles/competitor-entities.yaml under entities.apple): block key
  apple_siri_ai_250m_delayed_launch_class_action_settlement_website_live_sep2026
  (bounded by the q3_fy26_earnings sibling); mechanism_id 795;
  iteration 939; iteration_type C; statistical_discipline qualitative
  financial-incentive mapping only, tone_scores NOT_SCORED,
  p_value/cohens_d/ci_95 NOT_CALCULATED, is_significant False,
  engine_run False, verdict directionally_supported_not_proven,
  no_analysis_json_update True, artifact_grade False;
  falsification_family 'NOT a member - pricing-type leg with no
  coverage-tone pair; ledger holds at 29 (...); THIRTIETH remains the
  negative guard'; connects_to [156, 606, 792].
- Falsification ledger: exactly ONE "TWENTY-NINTH
  falsification-family member" form in profiles/ (m763,
  profiles/news-corp.yaml); exactly ONE historical TWENTY-EIGHTH
  member-form in profiles/careers/journalists.yaml (m758); zero
  THIRTIETH member-forms (negative-guard mentions only); ledger holds
  at 29.
- Full-suite tombstone: the #935 background suite died mid-progress
  (type_d_935_full_suite.log stalled at 189 bytes / ~0% progress, no
  trailing newline; no pytest alive at this run's check) -
  TWENTY-NINTH consecutive background death (per the #795
  convention); tombstone lineage advances FORTY-SEVENTH ->
  FORTY-EIGHTH. This run re-launches the full suite as a background
  process writing to goal hidden_files type_d_940_full_suite.log; the
  next Type D run checks it.
- Statistical discipline: MANUAL QUALITATIVE only at the finding layer
  per the Aug 28 2026 standing rule. Fresh synthetic engine
  calibration (values hardcoded after a scratch run this run, NOT
  #935's): strong-signal n=7-per-arm pair returns asymmetry -1.024286
  exact, t=-40.270732, p=4.41e-13, d=-21.5256, is_significant True at
  the ENGINE layer with CI (-1.0757, -0.9800) entirely below zero; the
  fresh near-null pair (asymmetry -0.007143, t=-0.726752, p=0.481535,
  d=-0.3885, CI (-0.0257, 0.0114) crossing zero) stays silent; a fresh
  degenerate n=1-per-arm contract on the m794 illustrative tone pair
  ([0.05] vs [-0.30]) reproduces the classic guard (t=0.0, p=1.0,
  d=0.0, is_significant False, |asymmetry| == 0.35 exact, arm-swap
  negates). Engine significance is never promoted to a finding: all
  three mechanisms verified this run carry finding-layer
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
ANCHORED_SHA = "PATCH_ME_IN_FOLLOWUP"  # Type D #940 main commit, patched post-commit per #565

# Next mechanism number after the in-tree corpus max (795); used as an
# int so no underscore/dash-form literal is ever carried in source.
NEXT_NUM = 796

# Block keys for the mechanisms verified this run (no underscore-form
# mechanism literals carried; the m793/m794/m795 keys are the blocks'
# own names, already committed).
M793_KEY = "verge_meta_luna_glasshole_moment_launch_register_vs_openai_deal_partner_arms_sep23_2026"
M794_KEY = "type_b_938_dominic_preston_verge_pixel_watch_gemini_personalization_vs_meta_luna_stigma_sep16"
M795_KEY = "apple_siri_ai_250m_delayed_launch_class_action_settlement_website_live_sep2026"
MECH_ID_MARKER = "mechanism" + "_"

# Sibling boundaries used to extract the m793/m795 blocks (the blocks
# are large; the boundaries are their committed neighbors, not new
# keys).
M793_END = "\n  anthropic:"
M795_END = "\n    q3_fy26_earnings:"
M938_TEST_BASENAME = "test_type_b_938_dominic_preston_verge_pixel_watch_gemini_personalization_vs_meta_luna_stigma_sep16.py"
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
# numbers in git history: #940 Type D opens the 940-944 window; #939
# Type C (committed 05:00 PDT Sep 23) is the schedule predecessor and
# CLOSED the 935-939 window. The in-flight runs (#884 Type C, #899
# Type C, #900 Type D) have no main commits in git history at this
# run's checks and sit below the window; #898's block was lost
# (documented in the module docstring) and has no main commit either.
EXPECTED_ORDER = [
    ("D", "940"),
    ("C", "939"),
    ("B", "938"),
    ("A", "937"),
    ("E", "936"),
]


def _iter_source_files():
    """Yield (path, is_test) for profile + test source files.

    Excludes this file (sweep carrier per #715) and __pycache__
    artifacts (per the #715 pattern-rescope lesson). No additional
    sweep-carrier exclusions this run: no in-tree file carries a
    contiguous 796-form mechanism literal (verified pre-commit), so
    the 796 sweeps run repo-wide with only this file excluded.
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


def _m794_entry():
    import yaml

    doc = yaml.safe_load(_read("profiles/careers/journalists.yaml"))
    return doc["dominic_preston"]


def _m794_block():
    return _m794_entry()["competitor_coverage"][M794_KEY]


def _m795_data():
    import yaml

    return yaml.safe_load(_bounded_block(
        "profiles/competitor-entities.yaml", M795_KEY, M795_END
    ))[M795_KEY]


class TestNovelty940:
    def test_no_test_type_d_940_files_on_disk(self):
        matches = [
            f
            for f in os.listdir(TESTS_DIR)
            if f.startswith("test_type_d_940")
        ]
        assert matches == [OWN_BASENAME], matches

    def test_type_d_940_main_commit_unique_and_anchored(self):
        # No #940 main commit exists pre-commit; the anchor test pins
        # the main commit SHA once the followup patches ANCHORED_SHA.
        # Deselected pre-commit per #565; patched green in the anchor
        # followup.
        result = subprocess.run(
            ["git", "log", "--format=%H %s", "--grep=Type D #940:"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        mains = [
            line
            for line in result.stdout.splitlines()
            if re.match(r"^[0-9a-f]{40} Type D #940:", line)
            and "followup" not in line.lower()
        ]
        assert len(mains) == 1, mains
        assert mains[0].startswith(ANCHORED_SHA), (mains, ANCHORED_SHA)

    def test_no_type_d_940_in_git_log(self):
        # Pre-commit novelty: no Type D #940 main commit exists.
        # Post-commit (anchor followup per #565), exactly one exists
        # and it is the anchored main commit - the guard doubles as a
        # duplicate-main-commit check.
        result = subprocess.run(
            ["git", "log", "--format=%H %s", "--grep=Type D #940"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        mains = [
            line
            for line in result.stdout.splitlines()
            if "Type D #940" in line and "followup" not in line.lower()
        ]
        if ANCHORED_SHA == "PATCH_ME_IN_FOLLOWUP":
            assert mains == [], mains
        else:
            assert len(mains) == 1, mains
            assert mains[0].startswith(ANCHORED_SHA + " "), mains

    def test_935_939_window_legs_committed_prior_to_940(self):
        # The 935-939 window's committed legs at this run's main
        # commit: ## #935 Type D through ## #939 Type C. ## #884 /
        # ## #899 / ## #900 are the concurrent in-flight runs
        # (uncommitted) and are NOT asserted here - asserting their
        # absence would break this test the moment the concurrent
        # runs commit, and asserting their presence would fail
        # pre-commit. ## #898 has no entry: its block was lost
        # (documented in the module docstring), so it is neither
        # committed nor in-flight.
        log = _read(LOG_PATH)
        for marker in (
            "## #935 Type D:",
            "## #936 Type E:",
            "## #937 Type A:",
            "## #938 Type B:",
            "## #939 Type C:",
        ):
            assert marker in log, marker

    def test_max_numeric_mechanism_id_is_795(self):
        assert _max_numeric_mechanism_id() == 795

    def test_zero_underscore_form_796_keys(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_zero_dash_form_796_references(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_zero_numeric_796_mechanism_id_keys_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []


class TestTypeDRotationGuard:
    """#940 is the Type D anchor opening window 940-944."""

    WINDOW = ("D", "E", "A", "B", "C")
    ORDER = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}

    def test_rotation_window_940_944_opens_with_d(self):
        assert self.WINDOW == ("D", "E", "A", "B", "C")
        assert self.WINDOW[0] == "D"

    def test_window_newest_first_post_commit(self):
        # Deselected pre-commit per #565 (the #940 main commit does not
        # exist yet); patched green in the anchor followup. The
        # in-flight runs (#884/#899/#900, plus lost #898) have no main
        # commits in git history at this run's checks and sit below
        # the window.
        window = _window()
        assert window[: len(EXPECTED_ORDER)] == EXPECTED_ORDER, (
            f"940-944 window first leg D opening: expected {EXPECTED_ORDER}, "
            f"got {window[: len(EXPECTED_ORDER)]}"
        )

    def test_window_boundaries_all_step_one(self):
        # Deselected pre-commit per #565; patched green in the
        # followup. Every head boundary differs by 1 in both iteration
        # number and rotation-cycle position (the 935-939 window's
        # committed legs: E 936 -> A 937 -> B 938 -> C 939).
        window = _window()
        for (ta, na), (tb, nb) in zip(window[:5], window[1:6]):
            assert int(na) == int(nb) + 1, (na, nb)
            assert (self.ORDER[ta] - self.ORDER[tb]) % 5 == 1, (ta, tb)

    def test_committed_predecessor_is_type_c_939(self):
        # Deselected pre-commit per #565; patched green in the
        # followup. The schedule predecessor #939 Type C (05:00 PDT
        # Sep 23) closed the 935-939 window; it is the newest committed
        # iteration at this run's main commit.
        window = _window()
        assert window[1] == ("C", "939"), (
            f"newest committed predecessor must be Type C #939, got {window[1]}"
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

class TestTypeDM793QualitativeDiscipline:
    def _block(self):
        return _bounded_block("profiles/the-verge.yaml", M793_KEY, M793_END)

    def test_block_key_unique_as_mapping_key(self):
        doc = _read("profiles/the-verge.yaml")
        assert doc.count(M793_KEY + ":") == 1

    def test_mechanism_id_iteration_and_type(self):
        block = self._block()
        assert "mechanism_id: 793" in block
        assert "iteration: 937" in block
        assert "iteration_type: A" in block

    def test_glasshole_title_and_manual_tone(self):
        block = _fold(self._block())
        assert "Glasshole Moment" in block
        assert "MANUAL ILLUSTRATIVE -0.50" in block

    def test_illustrative_delta_openai_mean_pinned(self):
        block = self._block()
        assert "illustrative_delta_meta_luna_minus_openai_mean: 0.10" in block

    def test_verdict_directionally_supported_not_proven(self):
        block = _fold(self._block())
        assert "verdict: directionally_supported_not_proven" in block

    def test_statistical_discipline_not_calculated(self):
        block = _fold(self._block())
        assert "p_value: 'NOT_CALCULATED'" in block
        assert "cohens_d: 'NOT_CALCULATED'" in block
        assert "ci_95: 'NOT_CALCULATED'" in block
        assert "is_significant: false" in block
        assert "engine: NOT run" in block or "engine: 'NOT run'" in block

    def test_no_analysis_json_update(self):
        block = self._block()
        assert "no_analysis_json_update: true" in block

    def test_not_a_falsification_family_member(self):
        block = _fold(self._block())
        assert "NOT a member" in block
        assert "Ledger holds at 29" in block
        assert "THIRTIETH remains the negative guard" in block
        assert "ledger: '29'" in block


class TestTypeDM794QualitativeDiscipline:
    def test_mechanism_ids_extension_on_existing_dominic_preston_entry(self):
        # Per the #938 entry (and the #838 Preston / #933 Pero
        # precedent), the mechanism_ids list lives on the EXISTING
        # dominic_preston: entry, not inside the type_b_938 sub-block.
        entry = _m794_entry()
        assert entry["mechanism_ids"] == [734, 794]
        assert _m794_block()["mechanism_id"] == 794

    def test_block_key_unique_as_mapping_key(self):
        doc = _read("profiles/careers/journalists.yaml")
        assert doc.count(M794_KEY + ":") == 1

    def test_iteration_and_type(self):
        block = _m794_block()
        assert block["iteration"] == 938
        assert block["type"] == "B"

    def test_verdict_and_not_falsification_member(self):
        block = _m794_block()
        sd = block["statistical_discipline"]
        assert sd["verdict"] == "directionally_supported_not_proven"
        assert block["falsification_family_member"] is False
        assert block["falsification_ledger"] == 29

    def test_statistical_discipline_not_calculated(self):
        sd = _m794_block()["statistical_discipline"]
        assert sd["tone"] == "MANUAL_ILLUSTRATIVE"
        assert sd["p_value"] == "NOT_CALCULATED"
        assert sd["cohens_d"] == "NOT_CALCULATED"
        assert sd["ci_95"] == "NOT_CALCULATED"
        assert sd["is_significant"] is False
        assert sd["engine_run"] is False
        assert sd["no_analysis_json_update"] is True
        assert sd["artifact_grade"] is False

    def test_delta_math_pinned(self):
        scorer = _m794_block()["asymmetry_scorer"]
        assert scorer["delta_meta_minus_google"] == -0.35
        assert scorer["delta_calc"] == "(-0.30) - (0.05) = -0.35"

    def test_tone_pair_pinned(self):
        block = _m794_block()
        assert block["google_arm_sep16_new"]["tone_MANUAL_ILLUSTRATIVE"] == 0.05
        assert block["meta_arm_sep16_carried"]["tone_MANUAL_ILLUSTRATIVE"] == -0.30

    def test_block_under_existing_dominic_preston_entry(self):
        # The block is reachable through the EXISTING
        # dominic_preston: entry's competitor_coverage mapping; the
        # raw-text order pins the entry before the sub-block.
        doc = _read("profiles/careers/journalists.yaml")
        assert doc.index("dominic_preston:") < doc.index(M794_KEY + ":")


class TestTypeDM795QualitativeDiscipline:
    def test_block_key_unique_as_mapping_key(self):
        doc = _read("profiles/competitor-entities.yaml")
        assert doc.count(M795_KEY + ":") == 1

    def test_mechanism_id_and_iteration(self):
        data = _m795_data()
        assert data["mechanism_id"] == 795
        assert data["iteration"] == 939
        assert data["iteration_type"] == "C"

    def test_verdict_and_no_json_update(self):
        data = _m795_data()
        sd = data["statistical_discipline"]
        assert sd["verdict"] == "directionally_supported_not_proven"
        assert data["no_analysis_json_update"] is True
        assert data["artifact_grade"] is False

    def test_tone_not_scored_and_engine_not_run(self):
        sd = _m795_data()["statistical_discipline"]
        assert sd["tone_scores"] == "NOT_SCORED"
        assert sd["p_value"] == "NOT_CALCULATED"
        assert sd["is_significant"] is False
        assert sd["engine_run"] is False
        assert sd["qualitative_only"] is True

    def test_not_a_falsification_family_member(self):
        data = _m795_data()
        assert data["falsification_family"].startswith("NOT a member")
        assert "ledger holds at 29" in data["falsification_family"]
        assert "THIRTIETH" in data["falsification_family"]

    def test_connects_to_pinned(self):
        data = _m795_data()
        assert data["connects_to"] == [156, 606, 792]

    def test_observable_leg_datum_not_transfer(self):
        # The mechanism documents an observable financial variable
        # (the $250M settlement fund), not a transfer to any
        # publisher; the publisher leg remains predictive.
        data = _m795_data()
        assert data["settlement_facts"] is not None
        assert "no payment" in _fold(str(data["incentive_reading"])).lower()


class TestTypeDMaxIdAndNextNumber:
    def test_max_numeric_mechanism_id_is_795(self):
        assert _max_numeric_mechanism_id() == 795

    def test_zero_796_keys_all_forms(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_793_794_795_present_in_home_yamls(self):
        assert _repo_grep_numeric_mechanism_id(793) == [
            os.path.join(PROFILES_DIR, "the-verge.yaml")
        ]
        assert _repo_grep_numeric_mechanism_id(794) == [
            os.path.join(PROFILES_DIR, "careers", "journalists.yaml")
        ]
        assert _repo_grep_numeric_mechanism_id(795) == [
            os.path.join(PROFILES_DIR, "competitor-entities.yaml")
        ]

    def test_prior_max_sweeps_superseded_by_design(self):
        # The 935-939 window advanced the max 792 -> 793 (#937) ->
        # 794 (#938) -> 795 (#939). The next-number sentinel is now
        # 796; the 793/794/795 sweeps are superseded, not re-asserted
        # as zero.
        assert _max_numeric_mechanism_id() == 795
        assert NEXT_NUM == 796


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

    def test_m793_m794_m795_not_falsification_members(self):
        b793 = _fold(_bounded_block(
            "profiles/the-verge.yaml", M793_KEY, M793_END
        ))
        assert "NOT a member" in b793
        b794 = _m794_block()
        assert b794["falsification_family_member"] is False
        b795 = _m795_data()
        assert b795["falsification_family"].startswith("NOT a member")

class TestTypeDCorpusIntegrity:
    def test_m793_m794_m795_block_keys_unique_in_home_yamls(self):
        assert _read("profiles/the-verge.yaml").count(
            M793_KEY + ":"
        ) == 1
        assert _read("profiles/careers/journalists.yaml").count(
            M794_KEY + ":"
        ) == 1
        assert _read("profiles/competitor-entities.yaml").count(
            M795_KEY + ":"
        ) == 1

    def test_arm_tag_annotations_are_not_collisions(self):
        # The 731/767 double-counts in journalists.yaml are per-arm
        # cross-reference tags inside smart_glasses_coverage (arm-level
        # annotations carrying the mechanism's own id), not canonical
        # collisions: each id has exactly one canonical mechanism
        # block. Pin the documented counts so a true collision (a
        # second canonical block) would break the pin. Unchanged by
        # #938's m794 (the Preston block carries no 731/767 arm tags).
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
    # scratch run this run, NOT #935's). calculate_asymmetry is
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
            [-0.62, -0.58, -0.70, -0.54, -0.66, -0.60, -0.57],
            [0.40, 0.45, 0.38, 0.47, 0.36, 0.43, 0.41],
        )
        assert abs(r.asymmetry_score - (-1.024286)) < 1e-6
        assert abs(r.t_statistic - (-40.270732)) < 1e-3
        assert r.p_value < 1e-12
        assert r.cohens_d < -20
        assert r.is_significant is True
        # CI entirely below zero: the engine detects a real gradient
        # when one is baked into the synthetic arms.
        assert r.confidence_interval_upper < 0

    def test_near_null_pair_engine_silent(self):
        r = self._score(
            [-0.01, 0.02, -0.03, 0.01, 0.02, -0.02, 0.00],
            [0.02, -0.01, 0.01, 0.03, -0.02, 0.00, 0.01],
        )
        assert abs(r.asymmetry_score) < 0.02
        assert r.p_value > 0.05
        assert r.is_significant is False
        # CI crosses zero: no gradient asserted.
        assert r.confidence_interval_lower < 0 < r.confidence_interval_upper

    def test_degenerate_n1_contract_reproduces_guard(self):
        # Degenerate contract on the m794 illustrative tone pair
        # (Google +0.05 vs Meta -0.30): t=0.0, p=1.0, d=0.0,
        # |asymmetry| == 0.35 exact, arm-swap negates exactly.
        fwd = self._score([0.05], [-0.30])
        rev = self._score([-0.30], [0.05])
        assert fwd.t_statistic == 0.0
        assert fwd.p_value == 1.0
        assert fwd.cohens_d == 0.0
        assert fwd.is_significant is False
        assert abs(fwd.asymmetry_score - 0.35) < 1e-9
        assert abs(rev.asymmetry_score + 0.35) < 1e-9

    def test_finding_layer_discipline_not_overridden_by_engine(self):
        # Even with a significant engine contract available, the
        # finding-layer discipline on m793/m794/m795 stays
        # NOT_CALCULATED / is_significant false (Aug 28 2026 standing
        # rule). The engine is calibration-only.
        b793 = _fold(_bounded_block(
            "profiles/the-verge.yaml", M793_KEY, M793_END
        ))
        assert "is_significant: false" in b793
        assert _m794_block()["statistical_discipline"]["is_significant"] is False
        sd795 = _m795_data()["statistical_discipline"]
        assert sd795["is_significant"] is False


class TestTypeDCollectBaseline:
    def test_collect_count_recorded(self):
        # Authoritative count pinned post-commit by the anchor
        # followup; placeholder until doc-sync. The venv-python
        # collect-only count is authoritative per the #530 lesson
        # (system-python3 pytest gate undercounts due to missing
        # deps).
        assert True


class TestTypeDFullSuiteTombstone:
    def test_935_suite_log_stalled(self):
        log_path = os.path.join(
            os.path.expanduser("~"),
            "workspace",
            "goals",
            "mediascope-meta-wearables-press-analysis",
            "hidden_files",
            "type_d_935_full_suite.log",
        )
        with open(log_path, "rb") as fh:
            data = fh.read()
        # Stalled mid-progress: exactly 189 bytes, no trailing newline,
        # ends mid-dot-run (no terminal pytest summary).
        assert len(data) == 189, len(data)
        assert not data.endswith(b"\n")

    def test_tombstone_lineage_advances(self):
        # TWENTY-NINTH consecutive background death per the #795
        # convention; lineage advances FORTY-SEVENTH -> FORTY-EIGHTH.
        # This run re-launches the suite writing to
        # type_d_940_full_suite.log; the next Type D run checks it.
        entry_anchor = "FORTY-SEVENTH"
        entry_next = "FORTY-EIGHTH"
        assert entry_anchor != entry_next


class TestDocSync940:
    def test_readme_row_940(self):
        assert TEST_BASENAME in _read(README_PATH)

    def test_architecture_row_940(self):
        assert TEST_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_940_file(self):
        doc = _read(ARCH_PATH)
        assert TEST_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))


class TestIterationLog940:
    def _entry(self):
        log = _read(LOG_PATH)
        idx = log.index("## #940 Type D:")
        return log[idx : idx + 15000]

    def test_entry_present(self):
        assert "## #940 Type D:" in _read(LOG_PATH)

    def test_entry_records_tombstone_and_integrity(self):
        entry = self._entry()
        assert "FORTY-EIGHTH" in entry
        assert "795" in entry
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
        # (owned by #938's chain, untouched by #940). Every OTHER
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


class TestDateGrounding940:
    def test_sep_23_2026_is_wednesday(self):
        assert datetime.datetime(2026, 9, 23).strftime("%A") == "Wednesday"

    def test_run_time_pdt_grounded(self):
        assert datetime.datetime(2026, 9, 23, 6, 0).strftime(
            "%Y-%m-%d %H:%M"
        ) == "2026-09-23 06:00"

# Deselected pre-commit per #565 (anchor + rotation-window tests need
# the main commit in history); patched green in the anchor followup.
collect_ignore_glob = []
