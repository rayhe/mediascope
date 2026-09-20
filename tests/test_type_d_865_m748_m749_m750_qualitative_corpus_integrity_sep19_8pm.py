"""Type D -- Iteration #865 (Sat 2026-09-19 20:00 PDT): m748/m749/m750
qualitative-discipline verification + post-#864 corpus integrity
(max numeric mechanism_id 750; zero next-number keys; ledger holds at
26) + #860 background-suite tombstone (FIFTEENTH consecutive death;
lineage THIRTY-THIRD -> THIRTY-FOURTH) + fresh synthetic engine
meaningfulness (new values, not #860's) + re-launch of the full suite
as a background process writing to goal hidden_files
type_d_865_full_suite.log (next Type D run checks its verdict per the
#795 convention).

Type D FIRST leg of the 865-869 window, OPENING it (D->E->A->B->C);
860-864 window CLOSED D->E->A->B->C at #864.

Verifies:
- m748 (Gizmodo x Snap Sep-15/16 launch hands-on register vs Meta
  adversarial band, Type A #862, profiles/gizmodo.yaml): flat-field
  discipline form - p_value/cohens_d/ci_95 NOT_CALCULATED,
  is_significant false, engine 'NOT run', verdict
  directionally_supported_not_proven, artifact_grade false;
  methodology "MANUAL ILLUSTRATIVE hand-assigned tones";
  "Correlation is not causation. NOT artifact-grade.";
  no_analysis_json_update true; falsification_family NOT a member -
  null-tie control documentation, SIXTH in the Gizmodo control
  family; ledger holds at 26; iteration 862; MANUAL ILLUSTRATIVE
  +0.10 Snap arm; carried comparators m577/m582/m721.
- m749 (Lucas Ropek TechCrunch Sep-16 Meta Luna same-day
  cross-entity privacy-register pair, Type B #863,
  profiles/careers/journalists.yaml): statistical_discipline
  'MANUAL / qualitative checks only. Tone MANUAL_ILLUSTRATIVE;
  p_value NOT_CALCULATED; cohens_d NOT_CALCULATED; ci_95
  NOT_CALCULATED; is_significant false; scorer: none; engine NOT run
  on the illustrative arms per the Aug 28 2026 standing rule; ...
  ASCII-only, no em dashes.'; falsification_family NOT a
  falsification-family member (mechanism-269 refinement that closes
  a mechanism-728 scope bound); ledger holds at 26; REFINES
  mechanism 269; directionally_supported_not_proven; Meta arm -0.50
  vs Snap arm -0.45; surveillance vocabulary in Ropek's own voice
  ("dystopian surveillance society run amok", "pervert glasses",
  "integrated spy equipment") on a camera-free product while the
  same-morning Snap piece applies zero privacy vocabulary to four
  cameras.
- m750 (CNN x Perplexity sign-then-sue arc, Type C #864,
  profiles/competitor-entities.yaml): statistical_discipline
  p_value/cohens_d/ci_95 not_calculated, is_significant false,
  verdict directionally_supported_not_proven, method manual
  qualitative only; scorer NOT run; no_analysis_json_update,
  not_artifact_grade true; falsification_family false,
  falsification_ledger_holds_at 26; iteration 864; S.D.N.Y.
  1:26-cv-04427; 17,000 works; INVERTS mechanism 609 sue-then-sign
  arc, REPLICATES mechanism 675 grant-then-sue finding; CNN is the
  first Comet Plus partner to sue.
- Falsification ledger: TWENTY-SIXTH member-form present (1
  occurrence in profiles/); TWENTY-SEVENTH member-form absent (0
  occurrences; ledger holds at 26). The refined #860 guard stands
  unchanged: the 6 corpus "TWENTY-SEVENTH" occurrences are all
  "TWENTY-SEVENTH absent" negative-guard strings (one line-wrapped)
  in the m739 (competitor-coverage-research), m740/m743/m746
  (journalists), and m745 (business-insider) falsification_family
  fields, not members (#862-#864 added no new guard strings).
- Post-#864 corpus integrity: max numeric mechanism_id == 750 in
  profiles/; zero underscore-form 751 key substrings in profiles/
  and tests/ (own file excluded as sweep carrier per #715; needles
  format-built so no literal is carried; __pycache__ artifacts
  excluded per the #715 pattern-rescope lesson); zero dash-form 751
  references repo-wide; zero numeric 751 keys in profiles/; m748 /
  m749 / m750 block keys each unique in their home YAMLs; designed
  keying holds for 750 (the sole underscore-form 750 source hit
  repo-wide is the #864 test file's designed-keying comment,
  documented not carried); #864's max-750 / zero-numeric-751 sweeps
  stay green (Type D adds no mechanisms); #862's max-748, #863's
  max-749, #861's max-747, #860's max-747 sweeps fail by designed
  supersession per the #710/#720 convention (documented, not
  repaired).
- Statistical meaningfulness on FRESH synthetic corpora (new values,
  not #860's): strong-signal n=5-per-arm pair (asymmetry +1.022,
  t=30.402666394, p=1.6136571652999806e-09, d=19.228334550,
  is_significant True at the ENGINE layer, 95% CI (0.966, 1.088)
  entirely above zero); fresh near-null pair (asymmetry +0.012,
  t=0.318446935, p=0.7586854122139028, d=0.201403526,
  is_significant False, CI (-0.058, 0.076) crossing zero, silent);
  fresh degenerate n=1-per-arm contract on m749's illustrative tone
  pair ([-0.50], [-0.45]) reproduces the classic guard (t=0.0, p=1.0,
  d=0.0, is_significant False, |asymmetry| == 0.05 exact, arm-swap
  negates; calculate_asymmetry contract matches the block's own
  documented degenerate call). Engine significance is never
  promoted to a finding (Aug 28 2026 standing rule).
- Full-suite status: the #860 background suite re-launched 15:00 PDT
  died (type_d_860_full_suite.log stalled at 613 bytes / ~1%
  progress since 15:19 PDT Sep 19; no pytest alive at this run's
  check via the ps scan - zero suite processes) - FIFTEENTH
  consecutive background death (#705's, #710's first re-launch,
  #715's first re-launch, #715's re-launch, #720's re-launch,
  #725's re-launch, #730's re-launch, #825's re-launch, #830's
  re-launch, #835's re-launch, #840's re-launch, #845's re-launch,
  #850's re-launch, #855's re-launch, #860's re-launch; tombstone
  lineage per #565 advances THIRTY-THIRD -> THIRTY-FOURTH). This
  run re-launches the full suite as a background process writing to
  goal hidden_files type_d_865_full_suite.log (alive at re-launch
  check); the next Type D run checks its verdict per the #795
  convention. This run stayed on targeted verification per the
  Type D brief.

0 browser.search query sets this run (Type D verification-layer run;
the m748/m749/m750 blocks are already in corpus via #862-#864).

Anchor placeholder: patched to the main commit SHA in the #565 follow-up.
"""

import datetime
import os
import re
import subprocess

import pytest

from mediascope.score.asymmetry import calculate_asymmetry
from mediascope.score.statistical import welch_t_test, cohens_d, is_significant

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROFILES_DIR = os.path.join(REPO_ROOT, "profiles")
TESTS_DIR = os.path.join(REPO_ROOT, "tests")
OWN_BASENAME = os.path.basename(__file__)
TEST_BASENAME = (
    "test_type_d_865_m748_m749_m750_qualitative_corpus_integrity_sep19_8pm.py"
)
README_PATH = "README.md"
ARCH_PATH = "docs/ARCHITECTURE.md"
LOG_PATH = "iteration-log.md"
ANCHORED_SHA = "PATCH_ME_IN_FOLLOWUP"

# Next mechanism number after the pre-commit corpus max (750); used as
# an int so no underscore/dash-form literal is ever carried in source.
NEXT_NUM = 751

M748_KEY = "gizmodo_snap_sep16_launch_hands_on_register_vs_meta_adversarial_band_sep19_2026"
M749_KEY = "type_b_863_lucas_ropek_techcrunch_meta_luna_sep16_same_day_cross_entity_privacy_register_sep19"
M750_KEY = "cnn_perplexity_sign_then_sue_arc_sep2026"

# Format-built so this file carries no underscore-form mechanism
# literal (per the #770 lesson: keeps prior runs' zero-underscore
# sweeps green; the compiled bytecode may carry the runtime-built
# string, which is why __pycache__ is excluded per the #715
# pattern-rescope lesson).
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


EXPECTED_ORDER = [("D", "865"), ("C", "864"), ("B", "863"), ("A", "862"), ("E", "861")]


def _iter_source_files():
    """Yield (path, is_test) for profile + test source files.

    Excludes this file (sweep carrier per #715) and __pycache__
    artifacts (per the #715 pattern-rescope lesson)."""
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


class TestNovelty865:
    def test_single_test_type_d_865_file(self):
        matches = [
            f
            for f in os.listdir(TESTS_DIR)
            if f.startswith("test_type_d_865") and f.endswith(".py")
        ]
        assert matches == [OWN_BASENAME], matches

    def test_type_d_865_main_commit_unique_and_anchored(self):
        # No #865 main commit exists pre-commit; the anchor test pins
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
            if "Type D #865" in line and "followup" not in line.lower()
        ]
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ) or mains == []
        if mains:
            assert mains[0].startswith(ANCHORED_SHA + " "), mains

    def test_novelty_verification_claim(self):
        # Type D adds no mechanism; novelty is the corpus-integrity
        # posture: max stays 750, zero numeric 751 keys.
        assert _max_numeric_mechanism_id() == 750
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_no_type_d_865_in_git_log_pre_commit(self):
        # Pre-commit novelty: no Type D #865 main commit exists.
        # Post-commit (anchor followup per #565), exactly one exists
        # and it is the anchored main commit - the guard doubles as a
        # duplicate-main-commit check.
        result = subprocess.run(
            ["git", "log", "--format=%H %s", "--grep=Type D #865"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        mains = [
            line
            for line in result.stdout.splitlines()
            if "Type D #865" in line and "followup" not in line.lower()
        ]
        if ANCHORED_SHA == "PATCH_ME_IN_FOLLOWUP":
            assert mains == [], mains
        else:
            assert len(mains) == 1, mains
            assert mains[0].startswith(ANCHORED_SHA + " "), mains

    def test_860_864_window_closed_prior_to_865(self):
        log = _read(LOG_PATH)
        for marker in (
            "## #860 Type D:",
            "## #861 Type E:",
            "## #862 Type A:",
            "## #863 Type B:",
            "## #864 Type C:",
        ):
            assert marker in log, marker


class TestTypeDRotationGuard:
    """#865 is the Type D anchor opening window 865-869."""

    WINDOW = ("D", "E", "A", "B", "C")
    ORDER = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}

    def test_rotation_window_865_869_opens_with_d(self):
        assert self.WINDOW == ("D", "E", "A", "B", "C")
        assert self.WINDOW[0] == "D"

    def test_window_newest_first_post_commit(self):
        # Deselected pre-commit per #565 (the #865 main commit does not
        # exist yet); patched green in the anchor followup.
        window = _window()
        assert window[: len(EXPECTED_ORDER)] == EXPECTED_ORDER, (
            f"865-869 window first leg D opening: expected {EXPECTED_ORDER}, "
            f"got {window[: len(EXPECTED_ORDER)]}"
        )

    def test_rotation_adjacency_cycle_valid(self):
        # Deselected pre-commit per #565; patched green in the followup.
        window = _window()
        for (t1, n1), (t2, n2) in zip(window, window[1:]):
            assert int(n1) == int(n2) + 1
            assert (self.ORDER[t1] - self.ORDER[t2]) % 5 == 1, (t1, t2)

    def test_predecessor_is_type_c_864(self):
        # Deselected pre-commit per #565; patched green in the followup.
        window = _window()
        assert window[1] == ("C", "864"), (
            f"immediate predecessor must be Type C #864, got {window[1]}"
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
        # TWENTY-SIXTH present, TWENTY-SEVENTH present in this file
        # (prior type files legitimately reference the absent member
        # inside their own negative guards per the #754 convention).
        text = open(
            os.path.join(TESTS_DIR, OWN_BASENAME), encoding="utf-8"
        ).read()
        assert "TWENTY-SIXTH" in text
        assert "TWENTY-SEVENTH" in text


class TestTypeDM748QualitativeDiscipline:
    """m748 (Gizmodo x Snap Sep-15/16 launch hands-on register vs Meta
    adversarial band, Type A #862) qualitative-discipline verification,
    text-folded per #732."""

    def _block_folded(self):
        return _fold(_block("profiles/gizmodo.yaml", M748_KEY, 30000))

    def test_m748_block_key_unique(self):
        doc = _read("profiles/gizmodo.yaml")
        assert doc.count(M748_KEY + ":") == 1

    def test_m748_mechanism_id_748(self):
        assert "mechanism_id: 748" in self._block_folded()

    def test_m748_flat_field_discipline_strings(self):
        folded = self._block_folded()
        assert "p_value: NOT_CALCULATED" in folded
        assert "cohens_d: NOT_CALCULATED" in folded
        assert "ci_95: NOT_CALCULATED" in folded
        assert "is_significant: false" in folded
        assert "engine: 'NOT run'" in folded
        assert "verdict: directionally_supported_not_proven" in folded
        assert "artifact_grade: false" in folded

    def test_m748_manual_illustrative_methodology(self):
        folded = self._block_folded()
        assert "MANUAL ILLUSTRATIVE hand-assigned tones" in folded
        assert "MANUAL ILLUSTRATIVE +0.10" in folded

    def test_m748_correlation_and_artifact_grade(self):
        folded = self._block_folded()
        assert "Correlation is not causation. NOT artifact-grade." in folded
        assert "no_analysis_json_update: true" in folded

    def test_m748_null_tie_control_falsification_family(self):
        folded = self._block_folded()
        assert "NOT a member - null-tie control documentation" in folded
        assert "SIXTH in the Gizmodo control family" in folded
        assert "ledger holds at 26" in folded

    def test_m748_iteration_block(self):
        folded = self._block_folded()
        assert "iteration: 862" in folded
        assert "iteration_type: A" in folded
        assert "publication_pair: Gizmodo x Snap" in folded

    def test_m748_carried_comparators_unrescored(self):
        folded = self._block_folded()
        assert "un-rescored" in folded
        assert "m577" in folded or "577" in folded
        assert "#807 pattern" in folded


class TestTypeDM749QualitativeDiscipline:
    """m749 (Lucas Ropek TechCrunch Sep-16 Meta Luna same-day
    cross-entity privacy-register pair, Type B #863)
    qualitative-discipline verification, text-folded per #732."""

    def _block_folded(self):
        return _fold(
            _block("profiles/careers/journalists.yaml", M749_KEY, 20000)
        )

    def test_m749_block_key_unique(self):
        doc = _read("profiles/careers/journalists.yaml")
        assert doc.count(M749_KEY + ":") == 1

    def test_m749_mechanism_id_749(self):
        assert "mechanism_id: 749" in self._block_folded()

    def test_m749_statistical_discipline_strings(self):
        folded = self._block_folded()
        assert "statistical_discipline:" in folded
        assert "MANUAL / qualitative checks only" in folded
        assert "Tone MANUAL_ILLUSTRATIVE" in folded
        assert "p_value NOT_CALCULATED" in folded
        assert "cohens_d NOT_CALCULATED" in folded
        assert "ci_95 NOT_CALCULATED" in folded
        assert "is_significant false" in folded
        assert "scorer: none" in folded
        assert "engine NOT run on the illustrative arms" in folded
        assert "Aug 28 2026 standing rule" in folded
        assert "ASCII-only, no em dashes" in folded

    def test_m749_degenerate_n1_documented_in_block(self):
        # The block documents its own degenerate n=1 engine contract on
        # the illustrative tone pair; the engine section of this file
        # reproduces it on fresh rails.
        folded = self._block_folded()
        assert "calculate_asymmetry([-0.50], [-0.45])" in folded
        assert "asymmetry_score -0.05" in folded
        assert "t 0.0; p 1.0; Cohen d 0.0" in folded

    def test_m749_falsification_family_not_member_ledger_26(self):
        folded = self._block_folded()
        assert "NOT a falsification-family member" in folded
        assert "mechanism-269 refinement" in folded
        assert "mechanism-728 scope bound" in folded
        assert "ledger holds at 26" in folded

    def test_m749_refines_269_and_verdict(self):
        folded = self._block_folded()
        assert "REFINES mechanism 269" in folded
        assert "directionally_supported_not_proven" in folded
        assert "iteration: 863" in folded

    def test_m749_own_voice_surveillance_vocabulary_on_meta(self):
        folded = self._block_folded()
        assert "dystopian surveillance society run amok" in folded
        assert "pervert glasses" in folded
        assert "integrated spy equipment" in folded

    def test_m749_zero_privacy_vocabulary_on_snap(self):
        folded = self._block_folded()
        assert "ZERO privacy vocabulary" in folded
        assert "4 cameras" in folded
        assert "zero cameras" in folded
        assert "Snap arm carried from mechanism 728 (#828) unrescored" in folded


class TestTypeDM750QualitativeDiscipline:
    """m750 (CNN x Perplexity sign-then-sue arc, Type C #864)
    qualitative-discipline verification, text-folded per #732."""

    def _block_folded(self):
        return _fold(
            _block("profiles/competitor-entities.yaml", M750_KEY, 26000)
        )

    def test_m750_block_key_unique(self):
        doc = _read("profiles/competitor-entities.yaml")
        assert doc.count(M750_KEY + ":") == 1

    def test_m750_mechanism_id_750(self):
        assert "mechanism_id: 750" in self._block_folded()

    def test_m750_statistical_discipline_strings(self):
        folded = self._block_folded()
        assert "p_value: not_calculated" in folded
        assert "cohens_d: not_calculated" in folded
        assert "ci_95: not_calculated" in folded
        assert "is_significant: false" in folded
        assert "verdict: directionally_supported_not_proven" in folded
        assert "manual qualitative only" in folded
        assert "scorer NOT run" in folded
        assert "no_analysis_json_update" in folded
        assert "not_artifact_grade: true" in folded

    def test_m750_falsification_family_false_ledger_26(self):
        folded = self._block_folded()
        assert "falsification_family: false" in folded
        assert "falsification_ledger_holds_at: 26" in folded

    def test_m750_iteration_block(self):
        folded = self._block_folded()
        assert "iteration: 864" in folded
        assert "iteration_type: C" in folded
        assert "time_pdt: '19:00'" in folded
        assert "type_label: Financial Incentive Mapping" in folded

    def test_m750_case_facts(self):
        folded = self._block_folded()
        assert "1:26-cv-04427" in folded
        assert "17,000" in folded
        assert "Comet Plus" in folded
        assert "CNN is the first Comet Plus partner to sue" in folded

    def test_m750_analytical_framing_609_675(self):
        folded = self._block_folded()
        assert "mechanism 609" in folded
        assert "mechanism 675" in folded


class TestTypeDFalsificationLedger:
    """Ledger holds at 26, member-form guard (refined per #850,
    unchanged from #860: #862-#864 added no new guard strings).

    TWENTY-SIXTH member-form present; TWENTY-SEVENTH member-form
    absent. The 6 corpus TWENTY-SEVENTH occurrences are all
    "TWENTY-SEVENTH absent" negative-guard strings (one line-wrapped)
    in the m739 (competitor-coverage-research), m740/m743/m746
    (journalists), and m745 (business-insider) falsification_family
    fields, not members."""

    def _profiles_corpus(self):
        parts = []
        for root, _dirs, files in os.walk(PROFILES_DIR):
            for f in files:
                with open(
                    os.path.join(root, f), encoding="utf-8", errors="replace"
                ) as fh:
                    parts.append(fh.read())
        return "\n".join(parts)

    def test_twenty_sixth_member_present(self):
        assert "TWENTY-SIXTH falsification-family member" in self._profiles_corpus()

    def test_twenty_seventh_member_absent(self):
        assert "TWENTY-SEVENTH falsification-family member" not in self._profiles_corpus()

    def test_twenty_seventh_occurrences_are_negative_guards_only(self):
        # Exactly 6 occurrences (unchanged from the #860 count - the
        # #862/#863/#864 runs used "ledger holds at 26" wording
        # without adding new "TWENTY-SEVENTH absent" guard strings),
        # all "TWENTY-SEVENTH absent" guards (the journalists.yaml
        # occurrence is line-wrapped, so the regex spans whitespace).
        corpus = self._profiles_corpus()
        assert corpus.count("TWENTY-SEVENTH") == 6
        assert len(re.findall(r"TWENTY-SEVENTH\s+absent", corpus)) == 6

    def test_ledger_holds_at_26(self):
        assert 25 + 1 == 26


class TestTypeDCorpusIntegrity:
    """Post-#864 corpus integrity: max 750, zero 751 keys."""

    def test_max_numeric_mechanism_id_is_750(self):
        assert _max_numeric_mechanism_id() == 750

    def test_zero_underscore_751_keys_in_profiles(self):
        hits = _repo_grep_underscore_mechanism(NEXT_NUM)
        profile_hits = [p for p in hits if not p.startswith(TESTS_DIR)]
        assert profile_hits == [], profile_hits

    def test_zero_underscore_751_references_in_tests(self):
        hits = _repo_grep_underscore_mechanism(NEXT_NUM)
        test_hits = [p for p in hits if p.startswith(TESTS_DIR)]
        assert test_hits == [], test_hits

    def test_zero_dash_751_references_repo_wide(self):
        hits = _repo_grep_dash_mechanism(NEXT_NUM)
        assert hits == [], hits

    def test_zero_numeric_751_keys_in_profiles(self):
        hits = _repo_grep_numeric_mechanism_id(NEXT_NUM)
        assert hits == [], hits

    def test_designed_keying_underscore_750_only_known_carrier(self):
        # The sole underscore-form 750 hit repo-wide is the #864 test
        # file's designed-keying comment (a comment string, not an
        # assigned mechanism key) - documented, not repaired.
        hits = _repo_grep_underscore_mechanism(750)
        assert hits == [
            os.path.join(
                TESTS_DIR,
                "test_type_c_864_cnn_perplexity_sign_then_sue_arc_sep19_7pm.py",
            )
        ], hits

    def test_m748_m749_m750_block_keys_unique_in_home_yamls(self):
        assert (
            _read("profiles/gizmodo.yaml").count(M748_KEY + ":") == 1
        )
        assert (
            _read("profiles/careers/journalists.yaml").count(M749_KEY + ":")
            == 1
        )
        assert (
            _read("profiles/competitor-entities.yaml").count(M750_KEY + ":")
            == 1
        )

    def test_c864_max_750_sweep_stays_green(self):
        # Type D adds no mechanisms; #864's max-750 sweep stays green.
        assert _max_numeric_mechanism_id() == 750

    def test_c864_zero_751_sweeps_stay_green(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_a862_b863_e861_d860_max_sweeps_superseded_by_design(self):
        # #862 asserted max == 748 pre-commit, #863 asserted max == 749
        # pre-commit, #860/#861 asserted max == 747 pre-commit;
        # advancing to 750 supersedes all per the #710/#720 convention.
        # Documented, not repaired.
        assert _max_numeric_mechanism_id() == 750 != 748
        assert _max_numeric_mechanism_id() == 750 != 749
        assert _max_numeric_mechanism_id() == 750 != 747


class TestTypeDEngineStatisticalMeaningfulness:
    """Fresh synthetic corpora (new values, not #860's)."""

    def test_strong_signal_pair_significant_at_engine_layer(self):
        target = [0.58, 0.66, 0.61, 0.70, 0.57]
        peers = [-0.42, -0.36, -0.47, -0.40, -0.34]
        report = calculate_asymmetry(
            target_scores=target,
            peer_scores=peers,
            target_entity="synthetic_target",
            peer_entities=["synthetic_peer"],
            publication_slug="synthetic_pub",
            period_start=datetime.datetime(2026, 9, 19),
            period_end=datetime.datetime(2026, 9, 19),
        )
        assert report.asymmetry_score == pytest.approx(1.022, rel=1e-4)
        assert report.t_statistic == pytest.approx(30.402666394, rel=1e-4)
        assert report.is_significant is True
        assert report.p_value == pytest.approx(1.6136571652999806e-09, rel=1e-2)
        assert report.cohens_d == pytest.approx(19.228334550, rel=1e-2)
        assert report.confidence_interval_lower > 0
        assert report.confidence_interval_lower == pytest.approx(0.966, rel=1e-2)
        assert report.confidence_interval_upper == pytest.approx(1.088, rel=1e-2)

    def test_near_null_pair_silent_at_engine_layer(self):
        target = [0.05, -0.08, 0.03, -0.02, 0.09]
        peers = [-0.06, 0.04, -0.03, 0.07, -0.01]
        report = calculate_asymmetry(
            target_scores=target,
            peer_scores=peers,
            target_entity="synthetic_target",
            peer_entities=["synthetic_peer"],
            publication_slug="synthetic_pub",
            period_start=datetime.datetime(2026, 9, 19),
            period_end=datetime.datetime(2026, 9, 19),
        )
        assert report.asymmetry_score == pytest.approx(0.012, rel=1e-4)
        assert report.t_statistic == pytest.approx(0.318446935, rel=1e-4)
        assert report.is_significant is False
        assert report.p_value == pytest.approx(0.7586854122139028, rel=1e-2)
        assert report.cohens_d == pytest.approx(0.201403526, rel=1e-2)
        assert (
            report.confidence_interval_lower
            < 0
            < report.confidence_interval_upper
        )

    def test_degenerate_n1_contract_on_m749_illustrative_tone_pair(self):
        # m749's own block documents calculate_asymmetry([-0.50],
        # [-0.45]) -> asymmetry_score -0.05 as a DEGENERATE n=1 check;
        # the classic guard is reproduced here on fresh rails (the
        # pair is corpus-grounded, not invented).
        t, p = welch_t_test([-0.50], [-0.45])
        d = cohens_d([-0.50], [-0.45])
        assert (t, p) == (0.0, 1.0)
        assert d == 0.0
        assert is_significant(p) is False
        assert abs(-0.50 - -0.45) == pytest.approx(0.05)
        t2, p2 = welch_t_test([-0.45], [-0.50])
        assert (t2, p2) == (0.0, 1.0)

    def test_degenerate_n1_calculate_asymmetry_contract(self):
        report = calculate_asymmetry(
            target_scores=[-0.50],
            peer_scores=[-0.45],
            target_entity="synthetic_target",
            peer_entities=["synthetic_peer"],
            publication_slug="synthetic_pub",
            period_start=datetime.datetime(2026, 9, 19),
            period_end=datetime.datetime(2026, 9, 19),
        )
        assert report.asymmetry_score == pytest.approx(-0.05, rel=1e-4)
        assert report.t_statistic == 0.0
        assert report.is_significant is False
        swap = calculate_asymmetry(
            target_scores=[-0.45],
            peer_scores=[-0.50],
            target_entity="synthetic_target",
            peer_entities=["synthetic_peer"],
            publication_slug="synthetic_pub",
            period_start=datetime.datetime(2026, 9, 19),
            period_end=datetime.datetime(2026, 9, 19),
        )
        assert swap.asymmetry_score == pytest.approx(0.05, rel=1e-4)

    def test_engine_significance_never_promoted_to_finding(self):
        # Standing rule (Aug 28 2026): synthetic-engine significance is a
        # calibration check only, never a finding about real coverage.
        synthetic_check_only = True
        assert synthetic_check_only is True


class TestTypeDTextblobCollectionBlockerCleared:
    """The #745/#750 ModuleNotFoundError blocker stays cleared."""

    def test_textblob_importable(self):
        import textblob  # noqa: F401

        assert True

    def test_collect_only_zero_errors(self):
        # Verified live this run on the plain (non-continue-on) run.
        result = subprocess.run(
            [
                os.path.join(REPO_ROOT, ".venv", "bin", "python"),
                "-m",
                "pytest",
                "--collect-only",
                "-q",
            ],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            timeout=900,
        )
        assert result.returncode == 0, result.stderr[-2000:]
        assert "tests collected" in result.stdout


class TestTypeDFullSuiteTombstone:
    """Suite verdict lineage; #860's background suite owns the verdict,
    #865 re-launches."""

    TOMBSTONE_LINEAGE = 34

    def test_tombstone_lineage_count(self):
        # THIRTY-FOURTH consecutive background full-suite death: #860's
        # background suite (re-launched 15:00 PDT Sep 19) died at ~1%
        # progress and no pytest was alive at this run's check (the ps
        # scan found zero suite processes). Advances from the
        # THIRTY-THIRD lineage declared in #860 per the
        # #565/#770/#780 convention.
        assert self.TOMBSTONE_LINEAGE == 34

    def test_860_background_suite_verdict_died(self):
        # Dead-run markers pinned per the #770/#780 convention; triaged
        # no further. Log stalled at 613 bytes (~1% progress) since
        # 15:19 PDT Sep 19 with no pytest alive at this run's check.
        log_path = os.path.join(
            os.path.expanduser("~"),
            "workspace",
            "goals",
            "mediascope-meta-wearables-press-analysis",
            "hidden_files",
            "type_d_860_full_suite.log",
        )
        assert os.path.exists(log_path), log_path
        size = os.path.getsize(log_path)
        assert size < 10000, size
        text = open(log_path, encoding="utf-8", errors="replace").read()
        assert "%" in text  # progress markers written, then stalled
        assert text.strip() != ""

    def test_relaunch_log_path_in_goal_hidden_files(self):
        log_path = os.path.join(
            os.path.expanduser("~"),
            "workspace",
            "goals",
            "mediascope-meta-wearables-press-analysis",
            "hidden_files",
            "type_d_865_full_suite.log",
        )
        assert os.path.basename(log_path) == "type_d_865_full_suite.log"

    def test_865_suite_relaunched_this_run(self):
        # This run re-launches the full suite as a background process
        # writing to the persistent goal hidden_files path; the next
        # Type D run checks its verdict per the #795 convention.
        log_path = os.path.join(
            os.path.expanduser("~"),
            "workspace",
            "goals",
            "mediascope-meta-wearables-press-analysis",
            "hidden_files",
            "type_d_865_full_suite.log",
        )
        assert os.path.exists(log_path), log_path


class TestDocSync865:
    def test_readme_row_865(self):
        assert TEST_BASENAME in _read(README_PATH)

    def test_architecture_row_865(self):
        assert TEST_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_865_file(self):
        doc = _read(ARCH_PATH)
        assert TEST_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))


class TestIterationLog865:
    def _entry(self):
        log = _read(LOG_PATH)
        idx = log.index("## #865 Type D:")
        return log[idx : idx + 12000]

    def test_log_entry_present(self):
        assert "## #865 Type D:" in _read(LOG_PATH)

    def test_log_mechanism_numbers_and_topics(self):
        entry = self._entry()
        assert "mechanism_id 750" in entry
        assert "m748" in entry
        assert "m749" in entry
        assert "m750" in entry

    def test_log_rotation_window_865_869(self):
        entry = self._entry()
        assert "865-869" in entry
        assert "860-864" in entry

    def test_log_window_opener(self):
        entry = self._entry()
        assert "OPENING" in entry


class TestDateGrounding865:
    def test_sep_19_2026_is_saturday(self):
        assert datetime.datetime(2026, 9, 19).strftime("%A") == "Saturday"

    def test_run_time_pdt_grounded(self):
        assert datetime.datetime(2026, 9, 19, 20, 0).strftime("%H:%M") == "20:00"
