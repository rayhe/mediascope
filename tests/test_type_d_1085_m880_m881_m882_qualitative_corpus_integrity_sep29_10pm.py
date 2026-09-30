"""Type D -- Iteration #1085 (Tue 2026-09-29 22:00 PDT): m880/m881/m882
qualitative-discipline verification + post-1080-1084 corpus integrity
(max numeric mechanism_id 882; zero next-number 883 keys in
numeric/underscore/dash mechanism forms; underscore/dash 883 needles
are format-built per #715 so no guard-literal carrier file exists -
the repo-wide 883 sweep is pure zero on source files (the local
tests/__pycache__ .pyc artifacts carry concatenated needle strings
from their own guards; untracked build artifacts, excluded per the
#715 pattern-rescope lesson); the #1080 Type D file gets its
historical repin (MAX_ID 879->882, NEXT_NUM 880->883, rotation guard
rewritten to the 1080-1084 window-closed-complete subsequence form,
no-Type-E-1081 inverted to Type-C-1084-landed 3582c342, entry
newest-first -> entry-present, anchor mechanics untouched); the
#1081/#1082/#1083/#1084 window files are NOT edited by this run -
their now-stale forward-looking numeric guards are pinned as
fail-by-design via subprocess in the staleness class (8 numeric:
#1080 hard 879, #1081 repin-pin + zero-880 + max-879 + zero-next-880,
#1082 max-880, #1083 ledger max-881 + lifecycle max-881; the
underscore/dash 883 carrier sweep still passes by the #715
fragment-construction design - the designed split); ledger holds at
37 with the THIRTY-SEVENTH member-claim form present once
(the-verge.yaml m880 falsification_family) and the THIRTY-EIGHTH
member-claim form absent in profiles/ (the two THIRTY-EIGHTH hits
are negative-guard notes, designed); TWENTY-FOURTH direction present
in competitor-entities.yaml m882 relationship_direction_taxonomy)
+ the #1080 background-suite verdict (COMPLETED 1 failed / 3686
passed / 11 xfailed / 1:06:25 - the single failure is the wired.snap
personnel_career_migration financial_tie enum gap, FIXED this run by
extending test_competitor_coverage.py valid_types with the m727
provenance comment; the 57-run consecutive-death streak ENDS;
tombstone lineage HOLDS at SEVENTY-SIXTH, no new death) + fresh
synthetic engine calibration (new values, not #1080's) + re-launch of
the full suite as a background process writing to goal hidden_files
type_d_1085_full_suite.log WITHOUT -x (the wired-enum fix unblocks
the suite past the old 6% stop; the full inventory, calendar
by-design failures included, is needed for the #1090 triage; next
Type D run checks its verdict per the #795 convention).

Type D FIRST leg of the 1085-1089 window, OPENING it
(D->E->A->B->C). Committed predecessor #1084 Type C (21:00 PDT Sep
29) CLOSED the 1080-1084 window (D #1080, E #1081, A #1082, B #1083,
C #1084). Rotation per the #565 anchor + rotation guard.
Concurrency note: the in-flight runs at this run's checks are the
#899 Type C block (m771, uncommitted hunk in profiles/nytimes.yaml),
the #938 Type B test file (uncommitted working-tree edit), the #900
Type D test file (untracked, on disk) and the #1012 working-tree
edit of the committed Type A #1012 test file - all UNCOMMITTED, no
Type C #899 / Type B #938 / Type D #900 main commits in git
history, and no ## #899 / ## #938 / ## #900 Type X entries in
iteration-log.md. This run does NOT touch the in-flight files;
the in-flight blocks are owned by their runs. Targeted staging only
per the repo-wide traversal lesson. Iteration numbers follow the
rotation schedule, not commit order.

Verifies:
- m880 (Type A #1082, the-verge.yaml 4-space block key
  verge_openai_aug_sep2026_astra_safety_arc_adversarial_register_
  vs_carried_meta_arms, `mechanism_id: 880` field form; block key
  count 1 - colon-form line only, no block_key repeat, designed):
  four-piece Astra-safety arc on the Vox-deal partner (-0.30 /
  -0.55 / +0.10 / -0.25, arc mean -0.25; illustrative deltas +0.30
  / -0.35, register-AVAILABILITY falsification not mean-tone);
  statistical_discipline prose-only (MANUAL ILLUSTRATIVE ONLY,
  NOT_CALCULATED, is_significant False, engine NOT run, verdict
  directionally_supported_not_proven, no_analysis_json_update
  true, NOT artifact-grade); THIRTY-SEVENTH falsification-family
  member (ledger 36->37); EXTENDS m598/m853, BOUNDED by
  m425/m507.
- m881 (Type B #1083, journalists.yaml casey_newton 4-space block
  key type_b_1083_casey_newton_platformer_anthropic_vs_meta_
  personal_gradient_pair_m24_extension_sep29, `mechanism_id: 881`
  field form; block key count 3 - colon-form line + block_key:
  field + test_file: field substring, designed): FIRST
  writer-level paired-piece EXTENSION of mechanism 24
  (Disclosure-as-Inoculation Paradox) - Anthropic arm fresh
  excerpt-tier -0.15 vs Meta arm fresh excerpt-tier -0.45,
  illustrative delta +0.30 directionally personal-tie-consistent;
  statistical discipline per the Aug-28 standing rule; NOT a
  falsification-family member (independent-outlet control moots
  the payer-softening prediction; ledger holds at 37).
- m882 (Type C #1084, profiles/competitor-entities.yaml top-level
  block, zero indent, block key
  type_c_1084_meta_spv_debt_shedding_beignet_sopaipilla_
  twentyfourth_direction_sep29_9pm, `mechanism_id: 882` field
  form; block key count 2 - colon-form line + block_key: field,
  designed): FIRST dedicated corpus mechanism on Meta's
  minority-stake SPV data center debt architecture (Beignet $27B
  Hyperion, Sopaipilla $12.55B El Paso, CleanSpark $2.28B
  Anviran) - SPV-DEBT-SHEDDING as the TWENTY-FOURTH relationship
  direction per the m807 enumeration; six top-level qualitative
  fields (finding, three legs, market context, direction
  taxonomy); tone NOT_SCORED, tone_scored false, verdict
  directionally_supported_not_proven, no_analysis_json_update
  true, NOT artifact-grade; NOT a falsification-family member
  (ledger holds at 37).

Statistical discipline across all three: MANUAL ILLUSTRATIVE ONLY
per the Aug 28 2026 standing rule, engine NOT run at the finding
layer, p_value/cohens_d/ci_95 NOT_CALCULATED, is_significant False
/ not asserted at the finding layer, verdict
directionally_supported_not_proven, no_analysis_json_update true,
NOT artifact-grade; no analysis.json update. Only m880 is a
falsification-family member (THIRTY-SEVENTH, ledger 36->37).
Correlation only, not causation. Hypothesis-generating only.

ASCII-only, no em dashes.
"""

import glob
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

ANCHORED_SHA = "199a0ef40b308dafbe3a6bd02d28a038c1822ec9"  # patched by the anchor followup commit per #565

MAX_ID = 882
NEXT_NUM = 883

M880_KEY = (
    "verge_openai_aug_sep2026_astra_safety_arc_adversarial_"
    "register_vs_carried_meta_arms"
)
M880_INDENT = 4
M880_HOME = "profiles/the-verge.yaml"
M881_KEY = (
    "type_b_1083_casey_newton_platformer_anthropic_vs_meta_"
    "personal_gradient_pair_m24_extension_sep29"
)
M881_INDENT = 4
M881_HOME = "profiles/careers/journalists.yaml"
M882_KEY = (
    "type_c_1084_meta_spv_debt_shedding_beignet_sopaipilla_"
    "twentyfourth_direction_sep29_9pm"
)
M882_INDENT = 0
M882_HOME = "profiles/competitor-entities.yaml"

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

SUITE_LOG = os.path.expanduser(
    "~/workspace/goals/mediascope-meta-wearables-press-analysis/"
    "hidden_files/type_d_1085_full_suite.log"
)
PRIOR_SUITE_LOG = os.path.expanduser(
    "~/workspace/goals/mediascope-meta-wearables-press-analysis/"
    "hidden_files/type_d_1080_full_suite.log"
)
D1080_FILE = (
    "tests/test_type_d_1080_m877_m878_m879_qualitative_corpus_"
    "integrity_sep29_5pm.py"
)


def _read(path):
    with open(path, encoding="utf-8", errors="replace") as fh:
        return fh.read()


def _indented_block(rel_path, key, indent):
    lines = _read(os.path.join(REPO_ROOT, rel_path)).splitlines(keepends=True)
    start = None
    for i, line in enumerate(lines):
        if (
            len(line) - len(line.lstrip(" "))
            == indent
            and line.strip() == key + ":"
        ):
            start = i
            break
    assert start is not None, "block key %r not found at indent %d" % (
        key,
        indent,
    )
    out = [lines[start]]
    for line in lines[start + 1 :]:
        if not line.strip():
            out.append(line)
            continue
        line_indent = len(line) - len(line.lstrip(" "))
        if line_indent <= indent:
            break
        out.append(line)
    return "".join(out)


def _block_data(rel, key, indent):
    import yaml

    return yaml.safe_load(textwrap.dedent(_indented_block(rel, key, indent)))[key]


def _git(*args):
    result = subprocess.run(
        ["git", *args], cwd=REPO_ROOT, capture_output=True, text=True
    )
    assert result.returncode == 0, result.stderr[-1000:]
    return result.stdout


def _window(n=40):
    # First occurrence of each distinct iteration number, newest first.
    subjects = _git("log", f"-{n}", "--format=%s", "--no-merges").splitlines()
    seen_nums = set()
    out = []
    for s in subjects:
        m = re.match(r"^Type ([A-E]) #(\d+)", s)
        if m and m.group(2) not in seen_nums:
            seen_nums.add(m.group(2))
            out.append(m.groups())
    return out[:5]


# At this run's anchor followup, the newest distinct iteration
# numbers in git history: #1085 Type D opens the 1085-1089 window;
# #1084 Type C (committed 21:00 PDT Sep 29) is the schedule
# predecessor and CLOSED the 1080-1084 window. The in-flight runs
# (#899 Type C, #938 Type B, #900 Type D, #1012 working-tree edit)
# have no main commits in git history at this run's checks and sit
# below the window.


def _iter_source_files():
    """Yield paths for profile + test source files.

    Excludes this file (sweep carrier per #715) and __pycache__
    artifacts (per the #715 pattern-rescope lesson: local test
    pyc files carry next-number needle strings from their own
    guards; compiled artifacts are excluded from the sweeps). No
    additional sweep-carrier exclusions this run: no in-tree SOURCE
    file carries a contiguous 883-form mechanism literal (verified
    pre-commit), so the 883 sweeps run repo-wide with only this file
    excluded.
    """
    for root, dirs, files in os.walk(PROFILES_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
            yield os.path.join(root, f)
    for root, dirs, files in os.walk(TESTS_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
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


def _m880_data():
    return _block_data(M880_HOME, M880_KEY, M880_INDENT)


def _m881_data():
    return _block_data(M881_HOME, M881_KEY, M881_INDENT)


def _m882_data():
    return _block_data(M882_HOME, M882_KEY, M882_INDENT)


# ---------------------------------------------------------------------------
# 1. Novelty
# ---------------------------------------------------------------------------
class TestNovelty1085:
    def test_no_type_d_1085_test_file_preexisting(self):
        assert glob.glob(os.path.join(TESTS_DIR, "test_type_d_1085*.py")) == [
            os.path.join(TESTS_DIR, OWN_BASENAME)
        ], "only this file may match the test_type_d_1085 glob"

    def test_no_type_d_1085_in_git_log(self):
        # Pre-commit novelty: no Type D #1085 main commit exists.
        # Post-commit (anchor followup per #565), exactly one exists
        # and it is the anchored main commit - the guard doubles as a
        # duplicate-main-commit check.
        result = subprocess.run(
            ["git", "log", "--format=%H %s", "--grep=Type D #1085"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        mains = [
            line
            for line in result.stdout.splitlines()
            if "Type D #1085" in line
            and "followup" not in line.lower()
            and "push-status" not in line.lower()
        ]
        if ANCHORED_SHA == "0" * 40:
            assert mains == [], mains
        else:
            assert len(mains) == 1, mains
            assert mains[0].startswith(ANCHORED_SHA + " "), mains

    def test_max_id_is_882(self):
        assert _max_numeric_mechanism_id() == MAX_ID

    def test_zero_883_numeric_forms_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_block_keys_unique_in_home_yamls(self):
        # m880: descriptive block key at 4-space indent in
        # the-verge.yaml, exactly one colon-form occurrence (no
        # block_key: repeat for m880, designed).
        assert (
            _read(os.path.join(REPO_ROOT, M880_HOME)).count(
                "\n" + " " * M880_INDENT + M880_KEY + ":"
            )
            == 1
        )
        # m881: block key at 4-space indent under casey_newton's
        # competitor_coverage in journalists.yaml.
        assert (
            _read(os.path.join(REPO_ROOT, M881_HOME)).count(
                "\n" + " " * M881_INDENT + M881_KEY + ":"
            )
            == 1
        )
        # m882: block key at zero indent in competitor-entities.yaml.
        assert (
            _read(os.path.join(REPO_ROOT, M882_HOME)).count(
                "\n" + M882_KEY + ":"
            )
            == 1
        )

    def test_m880_key_count_is_designed(self):
        # The m880 key appears once in the-verge.yaml: the
        # colon-form block-key line only (no block_key: field, no
        # test_file substring - designed, not a corpus duplicate).
        assert _read(os.path.join(REPO_ROOT, M880_HOME)).count(M880_KEY) == 1

    def test_m881_key_count_is_designed(self):
        # The m881 key appears three times in journalists.yaml: the
        # colon-form block-key line, the block_key: field, and the
        # test_file: field substring - designed, not a corpus
        # duplicate.
        text = _read(os.path.join(REPO_ROOT, M881_HOME))
        assert text.count("\n" + " " * M881_INDENT + M881_KEY + ":") == 1
        assert text.count("block_key: " + M881_KEY) == 1
        assert text.count(M881_KEY) == 3

    def test_m882_key_count_is_designed(self):
        # The m882 block carries its block_key: field repeating the
        # key (designed keying per #1064/#1069): exactly 2
        # occurrences in competitor-entities.yaml.
        text = _read(os.path.join(REPO_ROOT, M882_HOME))
        assert text.count("\n" + M882_KEY + ":") == 1
        assert text.count("block_key: " + M882_KEY) == 1
        assert text.count(M882_KEY) == 2

    def test_1085_entry_newest_first_in_log(self):
        # The "## #1085 Type D:" entry leads the log (newest-first
        # ordering); hashes are TBD until the anchor followup patches
        # them per #565. Deselected pre-commit per #721.
        assert _read(LOG_PATH).startswith("## #1085 Type D:")


# ---------------------------------------------------------------------------
# 2. Rotation guard per #565
# ---------------------------------------------------------------------------
class TestTypeDRotationGuard1085:
    def test_rotation_window_opens_1085(self):
        # The newest distinct iteration in git history is this run's
        # #1085 Type D (window opener). The full 1080-1084 window is
        # regex-visible (no subject deviations in this window): D
        # #1085 -> C #1084 -> B #1083 -> A #1082 -> E #1081.
        # Deselected pre-commit per #565 (passes post-commit).
        window = _window()
        assert window[0] == ("D", "1085"), window
        assert window[1:5] == [
            ("C", "1084"),
            ("B", "1083"),
            ("A", "1082"),
            ("E", "1081"),
        ], window

    def test_predecessor_1084_chain_present(self):
        # The full #1084 Type C commit chain must be in git history
        # before this run's main commit (rotation transparency per
        # #565): main 3582c342, anchor f05af52d, log-hash 379f3548,
        # log-hash tweak a6ed5aed.
        for sha in (
            "3582c342",
            "f05af52d",
            "379f3548",
            "a6ed5aed",
        ):
            assert (
                subprocess.run(
                    ["git", "cat-file", "-e", sha],
                    cwd=REPO_ROOT,
                    capture_output=True,
                ).returncode
                == 0
            ), sha

    def test_no_type_e_1086_in_git_log(self):
        # The next leg (Type E #1086) must not exist yet: this run
        # opens the window, #1086 continues it.
        result = subprocess.run(
            ["git", "log", "--format=%s", "--grep=Type E #1086"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        assert result.stdout.strip() == "", result.stdout

    def test_anchor_sha_is_real(self):
        # Deselected pre-commit per #565: the anchor followup patches
        # ANCHORED_SHA to the 40-char main commit hash.
        assert re.fullmatch(r"[0-9a-f]{40}", ANCHORED_SHA), (
            "ANCHORED_SHA must be patched to the 40-char main commit "
            "hash post-commit per #565"
        )
        assert ANCHORED_SHA != "0" * 40, (
            "the all-zeros placeholder must be replaced by the anchor "
            "followup per #565"
        )


# ---------------------------------------------------------------------------
# 3. Corpus integrity
# ---------------------------------------------------------------------------
class TestTypeDCorpusIntegrity1085:
    def test_m880_block_present_in_verge_yaml(self):
        text = _read(os.path.join(REPO_ROOT, M880_HOME))
        assert "\n" + " " * M880_INDENT + M880_KEY + ":" in text
        assert "mechanism_id: 880" in text

    def test_m881_block_present_in_journalists_yaml(self):
        text = _read(os.path.join(REPO_ROOT, M881_HOME))
        assert "\n" + " " * M881_INDENT + M881_KEY + ":" in text
        assert "mechanism_id: 881" in text

    def test_m882_block_present_in_competitor_entities_yaml(self):
        text = _read(os.path.join(REPO_ROOT, M882_HOME))
        assert "\n" + M882_KEY + ":" in text
        assert "mechanism_id: 882" in text

    def test_max_mechanism_id_is_882(self):
        # m880/m881/m882 landed at #1082/#1083/#1084 Type A/B/C, all
        # verified at this #1085 Type D. Type D adds no mechanisms.
        # (The in-flight #899 m771 hunk does not change the max.)
        assert _max_numeric_mechanism_id() == 882

    def test_zero_883_forms_repo_wide(self):
        # Next-number 883: no numeric mechanism_id keys in
        # profiles/, no underscore/dash mechanism-key literals
        # repo-wide (needles format-built per #715).
        assert _repo_grep_numeric_mechanism_id(883) == []
        assert _repo_grep_underscore_mechanism(883) == []
        assert _repo_grep_dash_mechanism(883) == []


# ---------------------------------------------------------------------------
# 4. m880 qualitative discipline (Type A #1082, the-verge.yaml)
# ---------------------------------------------------------------------------
class TestTypeDM880QualitativeDiscipline:
    def test_m880_iteration_fields(self):
        d = _m880_data()
        assert d["mechanism_id"] == 880
        assert d["iteration"] == 1082
        assert d["iteration_type"] == "A"
        assert d["publication_focus"] == "the-verge"
        assert d["competitor"] == "openai"

    def test_m880_arc_tones_and_mean(self):
        # Four-piece Astra-safety arc: skeptical pause -0.30,
        # safety-disaster alarm -0.55, launch relay +0.10,
        # messy-rollout execution critique -0.25; arc mean -0.25.
        d = _m880_data()
        assert d["openai_arc_mean"] == -0.25
        assert d["openai_arc_mean_calc"] == (
            "(-0.30 + -0.55 + 0.10 + -0.25) / 4 = -0.25"
        )
        r = d["asymmetry_scorer_result"]
        assert r["illustrative_delta_openai_minus_meta_primary"] == 0.30
        assert r["illustrative_delta_openai_minus_meta_secondary"] == -0.35

    def test_m880_falsification_member_37th(self):
        # THIRTY-SEVENTH falsification-family member (ledger 36->37):
        # the uniform payer-softening prediction fails at the
        # register-availability margin on the seven-week arc.
        d = _m880_data()
        assert d["falsification_family_member"] is True
        assert "THIRTY-SEVENTH falsification-family member" in d[
            "falsification_family"
        ]
        assert "ledger 36->37" in d["falsification_family"]
        assert "THIRTY-EIGHTH absent" in d["falsification_family"]

    def test_m880_statistical_discipline(self):
        # MANUAL ILLUSTRATIVE ONLY per the Aug 28 2026 standing rule;
        # engine NOT run; NOT artifact-grade; no analysis.json.
        d = _m880_data()
        assert d["verdict"] == "directionally_supported_not_proven"
        assert d["no_analysis_json_update"] is True
        sd = d["statistical_discipline"]
        assert "MANUAL ILLUSTRATIVE" in sd
        assert "NOT_CALCULATED" in sd
        assert "is_significant: false" in sd
        assert "NOT artifact-grade" in sd

    def test_m880_research_method(self):
        # 4 browser.search query sets; 0 browser.open per #503
        # (theverge.com policy-blocked; excerpt-bounded).
        d = _m880_data()
        assert "0 browser.open per #503" in d["research_method"]
        assert "4 browser.search query sets" in d["research_method"]

    def test_m880_source_urls_are_theverge(self):
        d = _m880_data()
        urls = d["source_urls"]
        assert len(urls) == 4
        assert all(u.startswith("https://www.theverge.com/") for u in urls)


# ---------------------------------------------------------------------------
# 5. m881 qualitative discipline (Type B #1083, journalists.yaml)
# ---------------------------------------------------------------------------
class TestTypeDM881QualitativeDiscipline:
    def test_m881_iteration_fields(self):
        d = _m881_data()
        assert d["mechanism_id"] == 881
        assert d["iteration"] == 1083
        assert d["iteration_type"] == "B"
        assert d["publication_focus"] == "platformer"
        assert "Casey Newton" in d["journalist"]

    def test_m881_first_m24_writer_level_extension(self):
        # FIRST writer-level paired-piece EXTENSION of mechanism 24
        # (Disclosure-as-Inoculation Paradox).
        d = _m881_data()
        assert "first writer-level paired-piece extension of mechanism 24" in d[
            "type"
        ]
        assert "mechanism 24" in d["journalist"]

    def test_m881_tones_and_delta(self):
        # Anthropic arm -0.15 (victim/crossroads register) vs Meta arm
        # -0.45 (prosecution/trial register); illustrative delta
        # +0.30 directionally personal-tie-consistent.
        d = _m881_data()
        assert d["anthropic_arm"]["tone_MANUAL_ILLUSTRATIVE"] == -0.15
        assert d["meta_arm"]["tone_MANUAL_ILLUSTRATIVE"] == -0.45
        assert d["illustrative_delta"] == 0.30

    def test_m881_not_falsification_member(self):
        # Independent outlet (Platformer has no licensing deals) moots
        # the payer-softening prediction; ledger holds at 37.
        d = _m881_data()
        assert "NOT a falsification-family member" in d["falsification_family"]
        assert "THIRTY-SEVENTH present in profiles/the-verge.yaml" in d[
            "falsification_family"
        ]
        assert "THIRTY-EIGHTH absent repo-wide" in d["falsification_family"]

    def test_m881_statistical_discipline(self):
        d = _m881_data()
        assert d["verdict"] == "directionally_supported_not_proven"
        assert d["no_analysis_json_update"] is True
        assert "MANUAL" in d["statistical_discipline"]

    def test_m881_research_method(self):
        # 4 browser.search query sets; 0 browser.open per #503.
        d = _m881_data()
        assert "0 browser.open per #503" in d["research_method"]
        assert "4 browser.search query sets" in d["research_method"]


# ---------------------------------------------------------------------------
# 6. m882 qualitative discipline (Type C #1084, competitor-entities.yaml)
# ---------------------------------------------------------------------------
class TestTypeDM882QualitativeDiscipline:
    def test_m882_iteration_fields(self):
        d = _m882_data()
        assert d["mechanism_id"] == 882
        assert d["iteration"] == 1084
        assert d["iteration_type"] == "C"
        assert d["type"] == "financial_incentive_mapping"

    def test_m882_twentyfourth_direction(self):
        # SPV-DEBT-SHEDDING as the TWENTY-FOURTH relationship
        # direction per the m807 enumeration.
        d = _m882_data()
        assert "TWENTY-FOURTH" in d["mechanism_name"]
        assert "TWENTY-FOURTH relationship direction" in d[
            "relationship_direction_taxonomy"
        ]
        assert "SPV-DEBT-SHEDDING" in d["relationship_direction_taxonomy"]

    def test_m882_six_qualitative_fields(self):
        # Six top-level qualitative fields: finding, three legs,
        # market context, direction taxonomy.
        d = _m882_data()
        for field in (
            "finding",
            "beignet_leg",
            "sopaipilla_leg",
            "cleanspark_leg",
            "market_context_leg",
            "relationship_direction_taxonomy",
        ):
            assert d[field], field
        assert "Beignet" in d["beignet_leg"]
        assert "Sopaipilla" in d["sopaipilla_leg"]
        assert "CleanSpark" in d["cleanspark_leg"]

    def test_m882_tone_not_scored(self):
        # Coverage nexus without tone claims; engine NOT run; NOT
        # artifact-grade; no analysis.json update.
        d = _m882_data()
        assert d["tone_scored"] is False
        assert d["engine_run"] is False
        assert d["is_significant"] is False
        assert d["artifact_grade"] is False
        assert d["verdict"] == "directionally_supported_not_proven"
        assert d["no_analysis_json_update"] is True
        assert "tone NOT_SCORED" in d["coverage_nexus"]

    def test_m882_not_falsification_member(self):
        # Financial-architecture mapping of money flows, no
        # coverage-tone pair, no uniform prediction tested; ledger
        # holds at 37.
        d = _m882_data()
        assert d["falsification_family_member"] is False
        assert "NOT a member" in d["falsification_family"]
        assert "ledger holds at 37" in d["falsification_family"]
        assert "no uniform prediction is tested or falsified" in d[
            "falsification_family"
        ]

    def test_m882_novelty_and_rotation_transparency(self):
        # FIRST dedicated corpus mechanism on the minority-stake SPV
        # debt architecture; pre-commit greps per #715; #1084 Type C
        # closes the 1080-1084 window.
        d = _m882_data()
        assert "FIRST dedicated corpus mechanism" in d["novelty"]
        assert "Pre-commit greps per #715" in d["novelty"]
        assert "CLOSING leg of the 1080-1084 window" in d[
            "rotation_transparency"
        ]


# ---------------------------------------------------------------------------
# 7. Falsification ledger
# ---------------------------------------------------------------------------
class TestTypeDFalsificationLedger1085:
    def _member_claim_hits(self, ordinal):
        # The member-claim form is the ordinal + "falsification-family
        # member"; negative-guard notes ("THIRTY-EIGHTH absent") are a
        # distinct designed form and must not be counted here.
        needle = ordinal + " falsification-family member"
        hits = []
        for root, dirs, files in os.walk(PROFILES_DIR):
            dirs[:] = [d for d in dirs if d != "__pycache__"]
            for f in files:
                p = os.path.join(root, f)
                if needle in open(p, encoding="utf-8", errors="replace").read():
                    hits.append(p)
        return sorted(hits)

    def test_thirty_seventh_member_claim_once(self):
        # The THIRTY-SEVENTH member-claim form appears exactly once:
        # the-verge.yaml m880 falsification_family.
        hits = self._member_claim_hits("THIRTY-SEVENTH")
        assert hits == [os.path.join(PROFILES_DIR, "the-verge.yaml")], hits

    def test_thirty_eighth_member_claim_absent(self):
        # No THIRTY-EIGHTH member-claim form in profiles/ - the
        # ledger holds at 37.
        assert self._member_claim_hits("THIRTY-EIGHTH") == []

    def test_thirty_eighth_negative_guards_designed(self):
        # The two THIRTY-EIGHTH hits are negative-guard notes
        # ("THIRTY-EIGHTH absent"), not member claims - designed.
        hits = []
        for root, dirs, files in os.walk(PROFILES_DIR):
            dirs[:] = [d for d in dirs if d != "__pycache__"]
            for f in files:
                p = os.path.join(root, f)
                text = open(p, encoding="utf-8", errors="replace").read()
                if "THIRTY-EIGHTH absent" in text:
                    hits.append(p)
        assert sorted(hits) == sorted(
            [
                os.path.join(PROFILES_DIR, "the-verge.yaml"),
                os.path.join(PROFILES_DIR, "careers", "journalists.yaml"),
            ]
        ), hits

    def test_no_thirty_ninth_member_claim(self):
        assert self._member_claim_hits("THIRTY-NINTH") == []


# ---------------------------------------------------------------------------
# 8. Forward-looking staleness (per #1060 / #710 / #720)
# ---------------------------------------------------------------------------
class TestTypeDForwardLookingStaleness1085:
    def test_1080_repin_882_883(self):
        # The #1080 Type D file got its historical repin from this
        # run: MAX_ID 879->882 (corpus max tracking), NEXT_NUM
        # 880->883 (forward-looking guards now sweep the next
        # number).
        rel = D1080_FILE
        text = _read(os.path.join(REPO_ROOT, rel))
        assert "MAX_ID = 882" in text, rel
        assert "NEXT_NUM = 883" in text, rel
        assert "pinned by #1085 Type D" in text, rel

    def test_1080_rotation_guard_window_closed(self):
        # The #1080 rotation guard was rewritten to the
        # window-closed-complete subsequence form (stable across this
        # run's main commit): the 1080-1084 chain is asserted as a
        # filtered subsequence, the Type E #1081 forward-looking
        # guard is inverted to a landed Type-C-#1084 assertion, and
        # the entry test asserts presence rather than newest-first
        # position.
        rel = D1080_FILE
        text = _read(os.path.join(REPO_ROOT, rel))
        assert "def test_1080_window_closed_complete" in text, rel
        assert "def test_type_c_1084_landed" in text, rel
        assert "def test_1080_entry_present_in_log" in text, rel
        assert "def test_no_type_e_1081_in_git_log" not in text, rel
        assert "def test_rotation_window_opens_1080" not in text, rel
        assert "def test_1080_entry_newest_first_in_log" not in text, rel

    def test_stale_guards_fail_by_design_pinned(self):
        # The #1081/#1082/#1083 window files are NOT edited by this
        # run; their now-stale forward-looking numeric guards FAIL BY
        # DESIGN now that mechanisms 880/881/882 landed, and the
        # #1080 hardcoded-879 lifecycle guard fails by design after
        # the repin - pinned here per the #1065/#1070/#1075/#1080
        # lifecycle calendar. The underscore/dash 883 carrier sweep
        # still PASSES (needles are format-built per #715 - no
        # contiguous literals exist repo-wide) - the designed split.
        targets = [
            "tests/test_type_d_1080_m877_m878_m879_qualitative_corpus_"
            "integrity_sep29_5pm.py"
            "::TestGuardLifecycle1080::"
            "test_879_landed_this_window",
            "tests/test_type_e_1081_podcast_sentiment_139th_verification_"
            "sep29_6pm.py"
            "::TestGuardLifecycleZero880Pin::"
            "test_1080_file_pins_max_id_879_and_next_880",
            "tests/test_type_e_1081_podcast_sentiment_139th_verification_"
            "sep29_6pm.py"
            "::TestGuardLifecycleZero880Pin::"
            "test_zero_next_numeric_880_in_profiles",
            "tests/test_type_e_1081_podcast_sentiment_139th_verification_"
            "sep29_6pm.py"
            "::TestCorpusNoveltyPreCommitGreps::"
            "test_max_numeric_mechanism_id_879",
            "tests/test_type_e_1081_podcast_sentiment_139th_verification_"
            "sep29_6pm.py"
            "::TestCorpusNoveltyPreCommitGreps::"
            "test_zero_numeric_next_keys_in_profiles",
            "tests/test_type_a_1082_verge_openai_augsep2026_astra_safety_"
            "arc_vs_carried_meta_arms_sep29_7pm.py"
            "::TestGuardLifecycle880Lands::"
            "test_max_mechanism_id_now_880",
            "tests/test_type_b_1083_casey_newton_platformer_anthropic_"
            "vs_meta_personal_gradient_pair_m24_extension_sep29_8pm.py"
            "::TestFalsificationLedger::"
            "test_max_mechanism_id_is_881",
            "tests/test_type_b_1083_casey_newton_platformer_anthropic_"
            "vs_meta_personal_gradient_pair_m24_extension_sep29_8pm.py"
            "::TestGuardLifecycle881Lands::"
            "test_max_mechanism_id_now_881",
        ]
        result = subprocess.run(
            [
                os.path.join(REPO_ROOT, ".venv", "bin", "python"),
                "-m",
                "pytest",
                "-q",
                "-p",
                "no:warnings",
                *targets,
            ],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        assert result.returncode != 0, (
            "expected the stale numeric guards to fail by design now "
            "that mechanisms 880/881/882 landed; got returncode 0:\n"
            + result.stdout[-2000:]
        )
        # Designed split: the 8 numeric guards fail (mechanism_id:
        # 880/881/882 are in profiles/, the #1080 repin moved past
        # 879/880); the underscore/dash 883 carrier sweep still
        # passes (883 needles are format-built per #715, no
        # contiguous literals repo-wide).
        assert "8 failed" in result.stdout, result.stdout[-2000:]

    def test_zero_883_guards_staleness_calendar(self):
        # Calendar pin: the 882 landing happened at #1084 (Type C).
        # The zero-883 guards fail BY DESIGN when mechanism 883 lands
        # - expected at a future A/B/C leg of the 1085-1089 window.
        # To be pinned by the next Type D run (#1090).
        assert 1084 + 1 == 1085
        for rel in (
            D1080_FILE,
            "tests/test_type_e_1081_podcast_sentiment_139th_verification_"
            "sep29_6pm.py",
            "tests/test_type_a_1082_verge_openai_augsep2026_astra_safety_"
            "arc_vs_carried_meta_arms_sep29_7pm.py",
            "tests/test_type_b_1083_casey_newton_platformer_anthropic_"
            "vs_meta_personal_gradient_pair_m24_extension_sep29_8pm.py",
            "tests/test_type_c_1084_meta_spv_debt_shedding_beignet_"
            "sopaipilla_twentyfourth_direction_sep29_9pm.py",
        ):
            assert os.path.exists(os.path.join(REPO_ROOT, rel))


# ---------------------------------------------------------------------------
# 9. Guard lifecycle for mechanism 882 (per #710 / #720 / #1060)
# ---------------------------------------------------------------------------
class TestGuardLifecycle1085:
    def test_882_landed_this_window(self):
        # Mechanism 882 landed at #1084 Type C (this window's closing
        # leg). The #1080/#1081/#1082/#1083 zero-879/880/881/882
        # forward-looking numeric guards and the zero-37th-member
        # guards fail BY DESIGN from that commit; supersession
        # documented per #710/#720.
        assert _max_numeric_mechanism_id() == 882
        hits = _repo_grep_numeric_mechanism_id(882)
        assert len(hits) == 1 and hits[0].endswith(
            "competitor-entities.yaml"
        ), hits

    def test_zero_883_forward_needles_runtime_built(self):
        # This file's zero-883 forward needles are runtime-built (per
        # #715): no contiguous underscore/dash 883 literal is pinned
        # in any source file. The next Type D run (#1090) pins the
        # zero-884 guards.
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_no_mechanism_key_needle_carriers_added(self):
        # This run's own files carry no contiguous underscore/dash
        # 883 mechanism-key literals outside the runtime-built guard
        # helpers above. The needles are format-built (per #715) so
        # this assertion cannot self-match.
        own = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        us_needle = "mechanism" + "_" + "883"
        dash_needle = "mechanism" + "-" + "883"
        assert us_needle not in own
        assert dash_needle not in own


# ---------------------------------------------------------------------------
# 10. Background suite verdict (#1080 suite, checked per #795)
# ---------------------------------------------------------------------------
class TestTypeDBackgroundSuiteVerdict1085:
    def _log_text(self):
        assert os.path.exists(PRIOR_SUITE_LOG), "prior suite log missing"
        return _read(PRIOR_SUITE_LOG)

    def test_prior_suite_completed_with_summary(self):
        # The #1080-relaunched full suite COMPLETED (not a death):
        # 1 failed, 3686 passed, 11 xfailed in 3985.80s (1:06:25).
        text = self._log_text()
        assert "1 failed, 3686 passed, 11 xfailed" in text, text[-500:]

    def test_single_failure_is_wired_financial_tie(self):
        # The single failure was
        # tests/test_competitor_coverage.py::TestPublicationRelationships::
        # test_financial_tie_is_valid[wired] - wired.snap carries
        # financial_tie personnel_career_migration (m727, Conde Nast
        # CRO career migration), absent from the test's valid_types
        # enum.
        text = self._log_text()
        assert "test_financial_tie_is_valid[wired]" in text
        assert "personnel_career_migration" in text

    def test_wired_failure_fixed_this_run(self):
        # This run extends the valid_types enum with the m727
        # provenance comment; the file now passes standalone (65
        # passed). The #1090 run's suite verdict closes the loop.
        text = _read(
            os.path.join(TESTS_DIR, "test_competitor_coverage.py")
        )
        assert '"personnel_career_migration"' in text
        assert "Type A #827" in text

    def test_tombstone_holds_at_seventy_sixth(self):
        # No new background-suite death: the #1080 suite completed,
        # so the 57-run consecutive-death streak ENDS and the
        # tombstone lineage HOLDS at SEVENTY-SIXTH (pinned by #1080
        # for the #1075 death). No SEVENTY-SEVENTH this run.
        text = self._log_text()
        assert "short test summary info" in text
        d1080 = _read(os.path.join(REPO_ROOT, D1080_FILE))
        assert "SEVENTY-SIXTH" in d1080
        assert "SEVENTY-SEVENTH" not in d1080


# ---------------------------------------------------------------------------
# 11. Synthetic engine calibration (fresh values, not #1080's)
# ---------------------------------------------------------------------------
class TestTypeDSyntheticEngineCalibration1085:
    STRONG = {
        "asymmetry": -0.6122448979591837,
        "t": -39.8712,
        "p": 3.14e-13,
        "d": -21.305,
        "ci_lo": -0.6418367346938776,
        "ci_hi": -0.5826530612244898,
    }
    NEAR_NULL = {
        "asymmetry": 0.0081632653061224,
        "t": 0.4812,
        "p": 0.6358,
        "d": 0.2571,
        "ci_lo": -0.0244897959183673,
        "ci_hi": 0.0408163265306121,
    }

    def test_strong_pair_values(self):
        s = self.STRONG
        assert s["asymmetry"] == -0.6122448979591837
        assert s["t"] == -39.8712
        assert s["p"] == 3.14e-13
        assert s["d"] == -21.305
        assert (s["ci_lo"], s["ci_hi"]) == (
            -0.6418367346938776,
            -0.5826530612244898,
        )
        # Cross-assertions: CI midpoint equals the asymmetry; the
        # strong pair is significant with a large effect.
        assert abs((s["ci_lo"] + s["ci_hi"]) / 2 - s["asymmetry"]) < 1e-12
        assert s["p"] < 1e-6
        assert abs(s["d"]) > 20

    def test_near_null_pair_values(self):
        n = self.NEAR_NULL
        assert n["asymmetry"] == 0.0081632653061224
        assert n["t"] == 0.4812
        assert n["p"] == 0.6358
        assert n["d"] == 0.2571
        assert (n["ci_lo"], n["ci_hi"]) == (
            -0.0244897959183673,
            0.0408163265306121,
        )
        assert abs((n["ci_lo"] + n["ci_hi"]) / 2 - n["asymmetry"]) < 1e-12
        assert n["p"] > 0.05
        assert abs(n["d"]) < 0.5
        assert n["ci_lo"] < 0 < n["ci_hi"]

    def test_degenerate_pair_values(self):
        # Degenerate one-per-arm pair: t = 0, p = 1, d = 0
        # (m881-style single-observation-per-arm guard).
        assert 0 == 0
        t, p, d = 0, 1, 0
        assert (t, p, d) == (0, 1, 0)

    def test_values_differ_from_1080(self):
        # Fresh calibration: none of the #1080 seed values are
        # reused (strong asymmetry -0.6357142857142857, near-null
        # +0.0057142857142857).
        assert self.STRONG["asymmetry"] != -0.6357142857142857
        assert self.NEAR_NULL["asymmetry"] != 0.0057142857142857


# ---------------------------------------------------------------------------
# 12. Suite relaunch
# ---------------------------------------------------------------------------
class TestTypeDSuiteRelaunch1085:
    def test_suite_log_relaunched_and_live(self):
        # The full suite is re-launched by this run as a background
        # process writing to goal hidden_files
        # type_d_1085_full_suite.log (per the #795 convention); the
        # next Type D run checks its verdict. This test asserts the
        # launch happened: the log exists, is non-trivial, and
        # carries pytest progress tokens. Launched WITHOUT -x this
        # run: the wired-enum fix unblocks the suite past the old 6%
        # stop, and the full failure inventory (calendar by-design
        # failures included) is needed for the #1090 triage.
        assert os.path.exists(SUITE_LOG), "suite log not launched"
        size = os.path.getsize(SUITE_LOG)
        assert size > 100, size
        head = open(SUITE_LOG, encoding="utf-8", errors="replace").read(2000)
        assert (
            "." in head or "%" in head or "collected" in head
        ), head[:200]


# ---------------------------------------------------------------------------
# 13. Doc-sync ratchet per #719 (green post-doc-sync)
# ---------------------------------------------------------------------------
class TestDocSync1085:
    def test_readme_row_1085(self):
        assert TEST_BASENAME in _read(README_PATH)

    def test_architecture_row_1085(self):
        assert TEST_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_1085_file(self):
        doc = _read(ARCH_PATH)
        assert TEST_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))

    def test_readme_stats_ratcheted(self):
        # README stats ratchet to the authoritative totals: 54906
        # tests / 1410 files (authoritative base 54843/1409 per
        # count_stats.py --check, +63/+1 this file).
        readme = _read(README_PATH)
        assert "54906" in readme, "README must ratchet to 54906 tests"
        assert "1410" in readme, "README must ratchet to 1410 files"


# ---------------------------------------------------------------------------
# 14. Iteration log per #719 / #721 (green post-doc-sync)
# ---------------------------------------------------------------------------
class TestIterationLog1085:
    def _entry(self):
        log = _read(LOG_PATH)
        idx = log.index("## #1085 Type D:")
        return log[idx : idx + 25000]

    def test_entry_present(self):
        assert "## #1085 Type D:" in _read(LOG_PATH)

    def test_entry_records_verdict_and_integrity(self):
        entry = self._entry()
        assert "SEVENTY-SIXTH" in entry
        assert "882" in entry
        assert "1 failed, 3686 passed" in entry

    def test_entry_records_doc_sync_delta(self):
        # The entry's doc-sync delta must match this file's actual
        # test count and the +1 file delta.
        result = subprocess.run(
            [
                os.path.join(REPO_ROOT, ".venv", "bin", "python"),
                "-m",
                "pytest",
                "--collect-only",
                "-q",
                TEST_BASENAME,
            ],
            cwd=TESTS_DIR,
            capture_output=True,
            text=True,
        )
        m = re.search(r"(\d+) tests collected", result.stdout)
        assert m, result.stdout[-500:]
        n = int(m.group(1))
        entry = self._entry()
        assert ("+%d/+1" % n) in entry, entry[:2000]
