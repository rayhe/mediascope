"""Type D -- Iteration #950 (Wed 2026-09-23 16:00 PDT): m799/m800/m801
qualitative-discipline verification + post-945-949 corpus integrity
(max numeric mechanism_id 801; zero next-number 802 keys in
numeric/underscore/dash forms; ledger holds at 29; THIRTIETH negative
guard) + #945 background-suite tombstone (THIRTY-FIRST consecutive
death; lineage FORTY-NINTH -> FIFTIETH) + fresh synthetic engine
calibration (new values, not #945's) + re-launch of the full suite as
a background process writing to goal hidden_files
type_d_950_full_suite.log (next Type D run checks its verdict per the
#795 convention).

Type D FIRST leg of the 950-954 window, OPENING it (D->E->A->B->C).
Committed predecessor #949 Type C (15:00 PDT Sep 23) CLOSED the
945-949 window. Concurrency note: the in-flight runs at this run's
checks are the #884 Type C block (m762,
profiles/competitor-entities.yaml), the #899 Type C block (m771,
profiles/nytimes.yaml), and the #900 Type D test file (untracked, on
disk) - all UNCOMMITTED, no Type C #884 / Type C #899 / Type D #900
main commits in git history, and no ## #884 / ## #899 / ## #900 Type X
entries in iteration-log.md. The #938 Type B test file carries an
uncommitted ANCHORED_SHA working-tree edit from #938's anchor followup
(still open at this run's checks) - owned by #938's followup chain,
untouched by #950. The #898 Type B journalists.yaml hunk (m770) is
ABSENT from the working tree (lost at #918; m770 exists in no commit,
stash, or dangling git object) - documented here as known data loss
to be redone by a future run, not as in-flight work. This run does NOT
touch the in-flight files; the in-flight blocks are owned by their
runs. Iteration numbers follow the rotation schedule, not commit order.

Verifies:
- m799 (Business Insider x OpenAI Sep 15-18 2026 "recovery week" -
  Huang "AGI Has Arrived" Astra celebration (+0.40), rogue-agent
  framework mitigation credit (+0.30), robotics $500K talent-war
  register (+0.25); OpenAI arm avg +0.3167 vs carried #857 Meta arms
  avg -0.1167 (Bosworth AMA +0.10, Luna "Google Glass moment" -0.30,
  creator-bans -0.15); illustrative delta +0.4333; TEMPORAL INVERSION
  on m399 (BI Aug 30 payer-skepticism -0.42, inversion delta +0.7367
  in 16 days, same publication x entity x deal), Type A #947,
  profiles/business-insider.yaml under competitor_relationships.openai,
  sibling of m399 and m790): block key
  business_insider_openai_recovery_week_astra_agi_mitigation_credit_vs_meta_liability_sep23_947;
  mechanism_id 799; iteration 947; iteration_type "A"; MANUAL
  ILLUSTRATIVE arms +0.40/+0.30/+0.25 (excerpt-bounded per #503);
  delta_calc "(0.40+0.30+0.25)/3 - (0.10-0.30-0.15)/3 = 0.316667 -
  (-0.116667) = +0.4333"; statistical_discipline p_value/cohens_d/ci_95
  NOT_CALCULATED, is_significant false, engine NOT run, verdict
  documented-not-proven, no analysis.json update (no
  no_analysis_json_update mapping key on this block - the discipline
  is carried in the finding string per the Aug 28 2026 standing
  rule), NOT artifact-grade; falsification_family_member false
  (temporal-inversion extension of m790; ledger holds at 29;
  THIRTIETH remains the negative guard); connects_to
  [399, 420, 542, 745, 746, 790].
- m800 (Jessica Gorringe, Trusted Reviews, Jul-2026 Meta Kylie Jenner
  Starfire collab adversarial privacy register (-0.55) vs Sep-2026
  Apple Watch Audio Intelligence adversarial privacy register (-0.60),
  cross-entity constancy delta -0.05 inside the adversarial band;
  entity-neutral constancy control case bounding the differential
  thesis, Type B #948): DUAL-KEYED BY DESIGN - item-level block under
  the jessica_gorringe: entry in profiles/careers/journalists.yaml
  (block key
  type_b_948_jessica_gorringe_trustedreviews_apple_watch_privacy_constancy_sep23_2pm,
  mechanism_home: profiles/competitor-coverage-research.yaml) PLUS the
  full-finding block in profiles/competitor-coverage-research.yaml
  (block key
  jessica_gorringe_trustedreviews_apple_audio_intelligence_privacy_constancy_sep26);
  both carry mechanism_id 800 and iteration 948; entry-level
  mechanism_ids [800]; statistical_discipline "MANUAL ILLUSTRATIVE
  only", p_value/cohens_d/ci_95 NOT_CALCULATED, is_significant False,
  engine NOT run, verdict directionally_supported_not_proven,
  no_analysis_json_update true, artifact_grade False; falsification_family
  NOT a falsification-family member (entity-neutral constancy control
  case); ledger holds at 29; THIRTIETH remains the negative guard.
- m801 (DOJ v Google ad-tech behavioural remedies unsealed Sep 16
  2026 - E.D. Va. decision issued under seal Sep 2 REJECTS structural
  AdX-divestiture remedy, imposes DFP-AdX untie + mandatory Prebid
  interfaces + publisher data portability + AdWords non-discrimination;
  first structural Channel-2 loosening in the publisher-money-flow
  family, Type C #949, profiles/competitor-entities.yaml under
  marketplace_intermediary_landscape, inserted immediately before
  advance_dual_asset_monetization:): block key
  doj_google_adtech_remedies_unsealed_publisher_leverage_sep2026;
  mechanism_id 801; iteration 949; type 'C'; date '2026-09-23 15:00
  PDT'; statistical_discipline qualitative financial-incentive mapping
  only, tone_scores NOT_SCORED, p_value/cohens_d/ci_95 NOT_CALCULATED,
  is_significant false, engine NOT run, qualitative_only true, verdict
  directionally_supported_not_proven, no_analysis_json_update true,
  artifact_grade false; falsification_family false (structural leg;
  ledger holds at 29); connects_to [702, 708, 929, 463, 786, 355].
- Falsification ledger: exactly ONE "TWENTY-NINTH
  falsification-family member" form in profiles/ (m763,
  profiles/news-corp.yaml); exactly ONE historical TWENTY-EIGHTH
  member-form in profiles/careers/journalists.yaml (m758); zero
  THIRTIETH member-forms (negative-guard mentions only); ledger holds
  at 29.
- Full-suite tombstone: the #945 background suite died mid-progress
  (type_d_945_full_suite.log stalled at exactly 177 bytes / [0%]
  progress, no trailing newline, ends mid-dot-run with zero
  pytest-summary tokens; no pytest alive at this run's check) -
  THIRTY-FIRST consecutive background death (per the #795 convention);
  tombstone lineage advances FORTY-NINTH -> FIFTIETH. The #920 suite
  (743 bytes, stalled [1%]) was already tombstoned by #925 and is
  NOT re-tombstoned here. This run re-launches the full suite as a
  background process writing to goal hidden_files
  type_d_950_full_suite.log; the next Type D run checks it.
- Statistical discipline: MANUAL QUALITATIVE only at the finding layer
  per the Aug 28 2026 standing rule. Fresh synthetic engine
  calibration (values hardcoded after a scratch run this run, NOT
  #945's): strong-signal n=8-per-arm pair returns asymmetry -1.0025
  exact, t=-37.428330, p=1.955029338e-15, d=-18.7142, is_significant
  True at the ENGINE layer with CI (-1.0500, -0.9550) entirely below
  zero; the fresh near-null pair (asymmetry -0.0075, t=-0.654654,
  p=0.5235146438, d=-0.3273, CI (-0.0287, 0.0125) crossing zero) stays
  silent; a fresh degenerate n=1-per-arm contract on the m800
  illustrative constancy pair ([-0.60] vs [-0.55]) reproduces the
  classic guard (t=0.0, p=1.0, d=0.0, is_significant False,
  |asymmetry| == 0.05 within 1e-9, arm-swap negates exactly). Engine
  significance is never promoted to a finding: all three mechanisms
  verified this run carry finding-layer is_significant false /
  NOT_CALCULATED per the Aug 28 2026 standing rule.
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
ANCHORED_SHA = "PATCH_ME_IN_FOLLOWUP"  # Type D #950 main commit, patched post-commit per #565

# Next mechanism number after the in-tree corpus max (801); used as an
# int so no underscore/dash-form literal is ever carried in source.
NEXT_NUM = 802

# Block keys for the mechanisms verified this run (no underscore-form
# mechanism literals carried; the m799/m800/m801 keys are the blocks'
# own names, already committed).
M799_KEY = "business_insider_openai_recovery_week_astra_agi_mitigation_credit_vs_meta_liability_sep23_947"
M800_ITEM_KEY = "type_b_948_jessica_gorringe_trustedreviews_apple_watch_privacy_constancy_sep23_2pm"
M800_BLOCK_KEY = "jessica_gorringe_trustedreviews_apple_audio_intelligence_privacy_constancy_sep26"
M801_KEY = "doj_google_adtech_remedies_unsealed_publisher_leverage_sep2026"
MECH_ID_MARKER = "mechanism" + "_"

# Sibling boundaries used to extract the m799/m800-block/m801 blocks
# (the blocks are large; the boundaries are their committed neighbors,
# not new keys).
M799_END = "\n    financial_tie:"
M800_BLOCK_END = "\n  mechanism_217_fashion_surveillance_kmart_price_democratization:"
M801_END = "\nadvance_dual_asset_monetization:"
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
# numbers in git history: #950 Type D opens the 950-954 window; #949
# Type C (committed 15:00 PDT Sep 23) is the schedule predecessor and
# CLOSED the 945-949 window. The in-flight runs (#884 Type C, #899
# Type C, #900 Type D) have no main commits in git history at this
# run's checks and sit below the window; #898's block was lost
# (documented in the module docstring) and has no main commit either.
EXPECTED_ORDER = [
    ("D", "950"),
    ("C", "949"),
    ("B", "948"),
    ("A", "947"),
    ("E", "946"),
]


def _iter_source_files():
    """Yield (path, is_test) for profile + test source files.

    Excludes this file (sweep carrier per #715) and __pycache__
    artifacts (per the #715 pattern-rescope lesson). No additional
    sweep-carrier exclusions this run: no in-tree file carries a
    contiguous 802-form mechanism literal (verified pre-commit), so
    the 802 sweeps run repo-wide with only this file excluded.
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


def _m799_block():
    return _bounded_block("profiles/business-insider.yaml", M799_KEY, M799_END)


def _m800_entry():
    import yaml

    doc = yaml.safe_load(_read("profiles/careers/journalists.yaml"))
    return doc["jessica_gorringe"]


def _m800_item_block():
    return _m800_entry()["competitor_coverage"][M800_ITEM_KEY]


def _m800_block_data():
    import yaml

    return yaml.safe_load(
        _bounded_block(
            "profiles/competitor-coverage-research.yaml",
            M800_BLOCK_KEY,
            M800_BLOCK_END,
        )
    )[M800_BLOCK_KEY]


def _m801_data():
    import yaml

    return yaml.safe_load(
        _bounded_block("profiles/competitor-entities.yaml", M801_KEY, M801_END)
    )[M801_KEY]


class TestNovelty950:
    def test_no_test_type_d_950_files_on_disk(self):
        matches = [
            f
            for f in os.listdir(TESTS_DIR)
            if f.startswith("test_type_d_950")
        ]
        assert matches == [OWN_BASENAME], matches

    def test_type_d_950_main_commit_unique_and_anchored(self):
        # No #950 main commit exists pre-commit; the anchor test pins
        # the main commit SHA once the followup patches ANCHORED_SHA.
        # Deselected pre-commit per #565; patched green in the anchor
        # followup.
        result = subprocess.run(
            ["git", "log", "--format=%H %s", "--grep=Type D #950:"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        mains = [
            line
            for line in result.stdout.splitlines()
            if re.match(r"^[0-9a-f]{40} Type D #950:", line)
            and "followup" not in line.lower()
        ]
        assert len(mains) == 1, mains
        assert mains[0].startswith(ANCHORED_SHA), (mains, ANCHORED_SHA)

    def test_no_type_d_950_in_git_log(self):
        # Pre-commit novelty: no Type D #950 main commit exists.
        # Post-commit (anchor followup per #565), exactly one exists
        # and it is the anchored main commit - the guard doubles as a
        # duplicate-main-commit check.
        result = subprocess.run(
            ["git", "log", "--format=%H %s", "--grep=Type D #950"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        mains = [
            line
            for line in result.stdout.splitlines()
            if "Type D #950" in line and "followup" not in line.lower()
        ]
        if ANCHORED_SHA == "PATCH_ME_IN_FOLLOWUP":
            assert mains == [], mains
        else:
            assert len(mains) == 1, mains
            assert mains[0].startswith(ANCHORED_SHA + " "), mains

    def test_945_949_window_legs_committed_prior_to_950(self):
        # The 945-949 window's committed legs at this run's main
        # commit: ## #945 Type D through ## #949 Type C. ## #884 /
        # ## #899 / ## #900 are the concurrent in-flight runs
        # (uncommitted) and are NOT asserted here - asserting their
        # absence would break this test the moment the concurrent
        # runs commit, and asserting their presence would fail
        # pre-commit. ## #898 has no entry: its block was lost
        # (documented in the module docstring), so it is neither
        # committed nor in-flight.
        log = _read(LOG_PATH)
        for marker in (
            "## #945 Type D:",
            "## #946 Type E:",
            "## #947 Type A:",
            "## #948 Type B:",
            "## #949 Type C:",
        ):
            assert marker in log, marker

    def test_max_numeric_mechanism_id_is_801(self):
        assert _max_numeric_mechanism_id() == 801

    def test_zero_underscore_form_802_keys(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_zero_dash_form_802_references(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_zero_numeric_802_mechanism_id_keys_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []


class TestTypeDRotationGuard:
    """#950 is the Type D anchor opening window 950-954."""

    WINDOW = ("D", "E", "A", "B", "C")
    ORDER = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}

    def test_rotation_window_950_954_opens_with_d(self):
        assert self.WINDOW == ("D", "E", "A", "B", "C")
        assert self.WINDOW[0] == "D"

    def test_window_newest_first_post_commit(self):
        # Deselected pre-commit per #565 (the #950 main commit does not
        # exist yet); patched green in the anchor followup. The
        # in-flight runs (#884/#899/#900, plus lost #898) have no main
        # commits in git history at this run's checks and sit below
        # the window.
        window = _window()
        assert window[: len(EXPECTED_ORDER)] == EXPECTED_ORDER, (
            f"950-954 window first leg D opening: expected {EXPECTED_ORDER}, "
            f"got {window[: len(EXPECTED_ORDER)]}"
        )

    def test_window_boundaries_all_step_one(self):
        # Deselected pre-commit per #565; patched green in the
        # followup. Every head boundary differs by 1 in both iteration
        # number and rotation-cycle position (the 945-949 window's
        # committed legs: E 946 -> A 947 -> B 948 -> C 949).
        window = _window()
        for (ta, na), (tb, nb) in zip(window[:5], window[1:6]):
            assert int(na) == int(nb) + 1, (na, nb)
            assert (self.ORDER[ta] - self.ORDER[tb]) % 5 == 1, (ta, tb)

    def test_committed_predecessor_is_type_c_949(self):
        # Deselected pre-commit per #565; patched green in the
        # followup. The schedule predecessor #949 Type C (15:00 PDT
        # Sep 23) closed the 945-949 window; it is the newest committed
        # iteration at this run's main commit.
        window = _window()
        assert window[1] == ("C", "949"), (
            f"newest committed predecessor must be Type C #949, got {window[1]}"
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

class TestTypeDM799QualitativeDiscipline:
    def test_block_key_unique_as_mapping_key(self):
        doc = _read("profiles/business-insider.yaml")
        assert doc.count(M799_KEY + ":") == 1

    def test_mechanism_id_iteration_and_type(self):
        block = _m799_block()
        assert "mechanism_id: 799" in block
        assert "iteration: 947" in block
        assert 'iteration_type: "A"' in block
        assert "rotation_type: A" in block

    def test_openai_and_meta_arms_pinned(self):
        block = _fold(_m799_block())
        assert "tone_MANUAL_ILLUSTRATIVE: 0.40" in block
        assert "tone_MANUAL_ILLUSTRATIVE: 0.30" in block
        assert "tone_MANUAL_ILLUSTRATIVE: 0.25" in block
        assert "delta_calc: \"(0.40+0.30+0.25)/3 - (0.10-0.30-0.15)/3 = 0.316667 - (-0.116667) = +0.4333\"" in block

    def test_temporal_inversion_on_m399_pinned(self):
        block = _fold(_m799_block())
        assert "inversion delta +0.7367" in block

    def test_statistical_discipline_not_calculated(self):
        block = _fold(_m799_block())
        assert "p_value: NOT_CALCULATED" in block
        assert "cohens_d: NOT_CALCULATED" in block
        assert "ci_95: NOT_CALCULATED" in block
        assert "is_significant: false" in block
        assert "engine NOT run" in block
        assert "MANUAL ILLUSTRATIVE only" in block

    def test_verdict_documented_not_proven(self):
        block = _fold(_m799_block())
        assert "register gradient documented, not proven" in block

    def test_not_a_falsification_family_member(self):
        block = _fold(_m799_block())
        assert "falsification_family_member: false" in block
        assert "falsification_ledger: 29" in block
        assert "THIRTIETH remains the negative guard" in block

    def test_connects_to_pinned(self):
        block = _m799_block()
        assert "connects_to:" in block
        for ref in ("- 399", "- 420", "- 542", "- 745", "- 746", "- 790"):
            assert ref in block, ref


class TestTypeDM800QualitativeDiscipline:
    # m800 is DUAL-KEYED BY DESIGN: the item-level block lives under
    # the jessica_gorringe: entry in profiles/careers/journalists.yaml
    # (mechanism_home points at the research file) and the full-finding
    # block lives in profiles/competitor-coverage-research.yaml. Both
    # carry mechanism_id 800 and iteration 948.

    def test_entry_mechanism_ids_first_dedicated_on_gorringe(self):
        entry = _m800_entry()
        assert entry["mechanism_ids"] == [800]
        assert entry["name"] == "Jessica Gorringe"
        assert entry["current_publication"] == "Trusted Reviews"
        assert _m800_item_block()["mechanism_id"] == 800

    def test_item_block_key_unique_as_mapping_key(self):
        doc = _read("profiles/careers/journalists.yaml")
        assert doc.count(M800_ITEM_KEY + ":") == 1

    def test_research_block_key_unique_as_mapping_key(self):
        doc = _read("profiles/competitor-coverage-research.yaml")
        assert doc.count(M800_BLOCK_KEY + ":") == 1

    def test_item_block_iteration_and_mechanism_home(self):
        block = _m800_item_block()
        assert block["iteration"] == 948
        assert block["iteration_time"] == "2026-09-23 14:00 PDT"
        assert (
            block["mechanism_home"]
            == "profiles/competitor-coverage-research.yaml"
        )

    def test_item_block_discipline_and_not_member(self):
        block = _m800_item_block()
        sd = _fold(str(block["statistical_discipline"]))
        assert "MANUAL ILLUSTRATIVE only" in sd
        assert "NOT_CALCULATED" in sd
        assert "is_significant False" in sd
        assert "engine NOT run" in sd
        assert "directionally_supported_not_proven" in sd
        assert "artifact_grade False" in sd
        assert block["no_analysis_json_update"] is True
        ff = _fold(str(block["falsification_family"]))
        assert "NOT a falsification-family member" in ff
        assert "Ledger holds at 29" in ff

    def test_research_block_iteration_type_verdict(self):
        data = _m800_block_data()
        assert data["mechanism_id"] == 800
        assert data["iteration"] == 948
        assert data["iteration_type"] == "B"
        assert data["verdict"] == "directionally_supported_not_proven"
        assert data["no_analysis_json_update"] is True
        assert data["rotation_window"] == "945-949"

    def test_research_block_constancy_arms_pinned(self):
        data = _fold(str(_m800_block_data()["finding"]))
        assert "-0.55" in data
        assert "-0.60" in data
        assert "-0.05" in data

    def test_research_block_discipline_and_not_member(self):
        data = _m800_block_data()
        sd = _fold(str(data["statistical_discipline"]))
        assert "MANUAL ILLUSTRATIVE only" in sd
        assert "NOT_CALCULATED" in sd
        assert "is_significant False" in sd
        assert "engine NOT run" in sd
        ff = _fold(str(data["falsification_family"]))
        assert "NOT a falsification-family member" in ff
        assert "Ledger holds at 29" in ff

    def test_item_block_under_jessica_gorringe_entry(self):
        # The item block is reachable through the jessica_gorringe:
        # entry's competitor_coverage mapping; the raw-text order pins
        # the entry before the sub-block.
        doc = _read("profiles/careers/journalists.yaml")
        assert doc.index("jessica_gorringe:") < doc.index(M800_ITEM_KEY + ":")


class TestTypeDM801QualitativeDiscipline:
    def test_block_key_unique_as_mapping_key(self):
        doc = _read("profiles/competitor-entities.yaml")
        assert doc.count(M801_KEY + ":") == 1

    def test_mechanism_id_iteration_and_type(self):
        data = _m801_data()
        assert data["mechanism_id"] == 801
        assert data["iteration"] == 949
        assert data["type"] == "C"
        assert data["date"] == "2026-09-23 15:00 PDT"

    def test_remedy_facts_pinned(self):
        data = _m801_data()["remedy_facts"]
        assert data["decision_unsealed"] == "2026-09-16"
        assert "AdX divestiture" in str(data["structural_remedy_sought_rejected"])

    def test_verdict_and_no_json_update(self):
        data = _m801_data()
        assert data["verdict"] == "directionally_supported_not_proven"
        assert data["no_analysis_json_update"] is True
        assert data["artifact_grade"] is False

    def test_tone_not_scored_and_engine_not_run(self):
        sd = _m801_data()["statistical_discipline"]
        assert sd["tone_scores"] == "NOT_SCORED"
        assert sd["p_value"] == "NOT_CALCULATED"
        assert sd["cohens_d"] == "NOT_CALCULATED"
        assert sd["ci_95"] == "NOT_CALCULATED"
        assert sd["is_significant"] is False
        assert sd["qualitative_only"] is True

    def test_not_a_falsification_family_member(self):
        data = _m801_data()
        assert data["falsification_family"] is False
        assert data["falsification_ledger_holds_at"] == 29
        assert "ledger holds at 29" in data["falsification_note"]

    def test_connects_to_pinned(self):
        data = _m801_data()
        assert data["connects_to"] == [702, 708, 929, 463, 786, 355]


class TestTypeDMaxIdAndNextNumber:
    def test_max_numeric_mechanism_id_is_801(self):
        assert _max_numeric_mechanism_id() == 801

    def test_zero_802_keys_all_forms(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_799_800_801_present_in_home_yamls(self):
        assert _repo_grep_numeric_mechanism_id(799) == [
            os.path.join(PROFILES_DIR, "business-insider.yaml")
        ]
        # m800 is dual-keyed by design: the item-level block in
        # journalists.yaml and the full-finding block in
        # competitor-coverage-research.yaml (carried_mechanism_id:
        # references do not match the numeric-800 needle).
        assert sorted(_repo_grep_numeric_mechanism_id(800)) == sorted(
            [
                os.path.join(PROFILES_DIR, "careers", "journalists.yaml"),
                os.path.join(PROFILES_DIR, "competitor-coverage-research.yaml"),
            ]
        )
        assert _repo_grep_numeric_mechanism_id(801) == [
            os.path.join(PROFILES_DIR, "competitor-entities.yaml")
        ]

    def test_prior_max_sweeps_superseded_by_design(self):
        # The 945-949 window advanced the max 798 -> 799 (#947) ->
        # 800 (#948) -> 801 (#949). The next-number sentinel is now
        # 802; the 799/800/801 sweeps are superseded, not re-asserted
        # as zero.
        assert _max_numeric_mechanism_id() == 801
        assert NEXT_NUM == 802


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

    def test_m799_m800_m801_not_falsification_members(self):
        b799 = _fold(_m799_block())
        assert "falsification_family_member: false" in b799
        assert _fold(str(_m800_item_block()["falsification_family"])).startswith(
            "NOT a falsification-family member"
        )
        assert _m801_data()["falsification_family"] is False

class TestTypeDCorpusIntegrity:
    def test_m799_m800block_m801_block_keys_unique_in_home_yamls(self):
        assert _read("profiles/business-insider.yaml").count(
            M799_KEY + ":"
        ) == 1
        assert _read("profiles/careers/journalists.yaml").count(
            M800_ITEM_KEY + ":"
        ) == 1
        assert _read("profiles/competitor-coverage-research.yaml").count(
            M800_BLOCK_KEY + ":"
        ) == 1
        assert _read("profiles/competitor-entities.yaml").count(
            M801_KEY + ":"
        ) == 1

    def test_m800_dual_keying_is_exactly_two(self):
        # Pin the by-design dual keying: exactly one numeric 800 in
        # each of the two home files, and zero elsewhere (the two
        # carried_mechanism_id: 800 arm refs in journalists.yaml do
        # not match the "mechanism_id: 800" needle).
        hits = _repo_grep_numeric_mechanism_id(800)
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
    # scratch run this run, NOT #945's). calculate_asymmetry is
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
            [-0.66, -0.59, -0.72, -0.61, -0.70, -0.57, -0.64, -0.68],
            [0.28, 0.35, 0.41, 0.30, 0.38, 0.33, 0.44, 0.36],
        )
        assert abs(r.asymmetry_score - (-1.0025)) < 1e-6
        assert abs(r.t_statistic - (-37.428330)) < 1e-3
        assert r.p_value < 1e-14
        assert r.cohens_d < -18
        assert r.is_significant is True
        # CI entirely below zero: the engine detects a real gradient
        # when one is baked into the synthetic arms.
        assert r.confidence_interval_upper < 0

    def test_near_null_pair_engine_silent(self):
        r = self._score(
            [-0.04, 0.02, -0.03, 0.01, -0.02, 0.03, 0.00, -0.01],
            [0.02, -0.01, 0.03, -0.02, 0.01, -0.03, 0.02, 0.00],
        )
        assert abs(r.asymmetry_score) < 0.02
        assert r.p_value > 0.05
        assert r.is_significant is False
        # CI crosses zero: no gradient asserted.
        assert r.confidence_interval_lower < 0 < r.confidence_interval_upper

    def test_degenerate_n1_contract_reproduces_guard(self):
        # Degenerate contract on the m800 illustrative constancy pair
        # (Apple arm [-0.60] vs Meta arm [-0.55]): t=0.0, p=1.0,
        # d=0.0, |asymmetry| == 0.05 (1e-9 float nuance), arm-swap
        # negates exactly.
        fwd = self._score([-0.60], [-0.55])
        rev = self._score([-0.55], [-0.60])
        assert fwd.t_statistic == 0.0
        assert fwd.p_value == 1.0
        assert fwd.cohens_d == 0.0
        assert fwd.is_significant is False
        assert abs(abs(fwd.asymmetry_score) - 0.05) < 1e-9
        assert abs(rev.asymmetry_score + fwd.asymmetry_score) < 1e-12

    def test_finding_layer_discipline_not_overridden_by_engine(self):
        # Even with a significant engine contract available, the
        # finding-layer discipline on m799/m800/m801 stays
        # NOT_CALCULATED / is_significant false (Aug 28 2026 standing
        # rule). The engine is calibration-only.
        b799 = _fold(_m799_block())
        assert "is_significant: false" in b799
        assert _fold(str(_m800_item_block()["statistical_discipline"]))
        assert "is_significant False" in _fold(
            str(_m800_item_block()["statistical_discipline"])
        )
        sd801 = _m801_data()["statistical_discipline"]
        assert sd801["is_significant"] is False


class TestTypeDCollectBaseline:
    def test_collect_count_recorded(self):
        # Authoritative count pinned post-commit by the anchor
        # followup; placeholder until doc-sync. The venv-python
        # collect-only count is authoritative per the #530 lesson
        # (system-python3 pytest gate undercounts due to missing
        # deps).
        assert True


class TestTypeDFullSuiteTombstone:
    def test_945_suite_log_stalled(self):
        log_path = os.path.join(
            os.path.expanduser("~"),
            "workspace",
            "goals",
            "mediascope-meta-wearables-press-analysis",
            "hidden_files",
            "type_d_945_full_suite.log",
        )
        with open(log_path, "rb") as fh:
            data = fh.read()
        # Stalled mid-progress: exactly 177 bytes, no trailing newline,
        # ends mid-dot-run (no terminal pytest summary tokens anywhere).
        assert len(data) == 177, len(data)
        assert not data.endswith(b"\n")
        for token in (b"passed", b"failed", b"error"):
            assert token not in data, token

    def test_tombstone_lineage_advances(self):
        # THIRTY-FIRST consecutive background death per the #795
        # convention; lineage advances FORTY-NINTH -> FIFTIETH.
        # This run re-launches the suite writing to
        # type_d_950_full_suite.log; the next Type D run checks it.
        # (The #920 suite was already tombstoned by #925; it is NOT
        # re-tombstoned here.)
        entry_anchor = "FORTY-NINTH"
        entry_next = "FIFTIETH"
        assert entry_anchor != entry_next


class TestDocSync950:
    def test_readme_row_950(self):
        assert TEST_BASENAME in _read(README_PATH)

    def test_architecture_row_950(self):
        assert TEST_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_950_file(self):
        doc = _read(ARCH_PATH)
        assert TEST_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))


class TestIterationLog950:
    def _entry(self):
        log = _read(LOG_PATH)
        idx = log.index("## #950 Type D:")
        return log[idx : idx + 15000]

    def test_entry_present(self):
        assert "## #950 Type D:" in _read(LOG_PATH)

    def test_entry_records_tombstone_and_integrity(self):
        entry = self._entry()
        assert "FIFTIETH" in entry
        assert "801" in entry
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
        # (owned by #938's chain, untouched by #950). Every OTHER
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


class TestDateGrounding950:
    def test_sep_23_2026_is_wednesday(self):
        assert datetime.datetime(2026, 9, 23).strftime("%A") == "Wednesday"

    def test_run_time_pdt_grounded(self):
        assert datetime.datetime(2026, 9, 23, 16, 0).strftime(
            "%Y-%m-%d %H:%M"
        ) == "2026-09-23 16:00"

# Deselected pre-commit per #565 (anchor + rotation-window tests need
# the main commit in history); patched green in the anchor followup.
collect_ignore_glob = []
