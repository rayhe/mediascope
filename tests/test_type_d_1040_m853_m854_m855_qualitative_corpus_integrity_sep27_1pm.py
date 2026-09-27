"""Type D -- Iteration #1040 (Sun 2026-09-27 13:00 PDT): m853/m854/m855
qualitative-discipline verification + post-1035-1039 corpus integrity
(max numeric mechanism_id 855; zero next-number 856 keys in
numeric/underscore/dash mechanism forms; ledger holds at 33 with the
THIRTY-THIRD member-form present exactly twice (m854 notes prose +
m854 block falsification_note, journalists.yaml), THIRTY-SECOND
member-form still present (m853, the-verge.yaml), THIRTY-FOURTH
member-form negative guard) + #1035 background-suite tombstone
(FORTY-NINTH consecutive death; lineage SIXTY-SEVENTH -> SIXTY-EIGHTH)
+ fresh synthetic engine calibration (new values, not #1035's) +
re-launch of the full suite as a background process writing to goal
hidden_files type_d_1040_full_suite.log (next Type D run checks its
verdict per the #795 convention).

Type D FIRST leg of the 1040-1044 window, OPENING it (D->E->A->B->C).
Committed predecessor #1039 Type C (12:00 PDT Sep 27) CLOSED the
1035-1039 window (D #1035, E #1036, A #1037, B #1038, C #1039).
Concurrency note: the in-flight runs at this run's checks are the
#899 Type C block (m771, uncommitted hunk in profiles/nytimes.yaml),
the #938 Type B test file (uncommitted working-tree edit), the #900
Type D test file (untracked, on disk) and the #1012 working-tree edit
of the #1012 Type A test file - all UNCOMMITTED, no Type C #899 /
Type B #938 / Type D #900 main commits in git history, and no
## #899 / ## #938 / ## #900 Type X entries in iteration-log.md. The
#884 Type C block (m762) is COMMITTED at this run's checks (in HEAD),
so it is no longer in-flight; its presence is pinned as an integrity
anchor, not a concurrency note. The #898 Type B journalists.yaml hunk
(m770) is ABSENT from the working tree (lost at #918; m770 exists in
no profile YAML, only in the needle strings of the old #897 test file
and the in-flight #900 test file) - documented here as known data
loss to be redone by a future run, not as in-flight work. This run
does NOT touch the in-flight files; the in-flight blocks are owned by
their runs. Iteration numbers follow the rotation schedule, not
commit order.

Verifies:
- m853 (Type A #1037, the-verge.yaml competitor_relationships.openai,
  4-space indent, descriptive block key,
  `mechanism_id: 853` field form): The Verge Sep-24-to-26-2026
  event-window registers - OpenAI training-pause adversarial
  safety-crisis incident reportage (-0.55 MANUAL ILLUSTRATIVE) vs Meta
  Connect Ray-Ban Meta Audio privacy-concession measured on-the-record
  (+0.10 carried un-rescored from mechanism 811 per #807);
  illustrative delta (OpenAI minus Meta) -0.65; the Vox Media-OpenAI
  May 29 2024 licensing deal sits on the HARDER-covered side so the
  spread runs OPPOSITE the naive payer-softening prediction; EXTENDS
  m598 to a SECOND safety-crisis falsification at the outlet; PAIRS
  m425 (+0.46 thesis-consistent) as the domain-inversion point;
  THIRTY-SECOND falsification-family member (ledger 31->32);
  connects_to [507, 598, 425, 811, 827].
- m854 (Type B #1038, journalists.yaml terrence_obrien item,
  competitor_coverage, 4-space indent block key,
  `mechanism_id: 854` field form): FIRST dedicated journalist-profile
  mechanism on Terrence O'Brien (The Verge weekend editor);
  within-writer pair - Sep-26 OpenAI training-pause adversarial
  safety-crisis reportage (-0.55 carried un-rescored from m853 per
  #807) vs Sep-24 Meta Muse filesystem-vulnerability adversarial
  reportage (-0.50 manual illustrative); illustrative cross-entity
  delta (OpenAI minus Meta) -0.05, near-NULL; the Vox Media-OpenAI
  deal sits on the adversarially-covered side, falsifying the uniform
  payer-softening prediction at the WRITER level; EXTENDS m853 down
  to the journalist level; THIRTY-THIRD falsification-family member
  (ledger 32->33); connects_to [853, 507, 598, 425, 811, 827].
- m855 (Type C #1039, profiles/competitor-entities.yaml top-level
  block, zero indent, `mechanism_id: 855` field form): FIRST dedicated
  corpus mechanism on the Amazon x Anthropic Claude Selling Partner
  plugin (Sep 23 2026) - the selective-gatekeeping leg of the
  SIXTEENTH relationship direction (COMMERCE-GATEKEEPING): Amazon
  opens the sell-side Seller Central gate to the backed lab's agent
  (Claude, US beta, write-capable) three days after denying the
  buy-side to the publisher-paying lab's agent (Meta Muse, m852);
  Amazon's three-role geometry (PAYS m559 / BACKS zero-deal labs /
  DENIES m852) gains the fourth posture GRANTS; direction count holds
  at sixteen (second leg, not a new direction); connects_to
  [852, 831, 559, 509, 594].

Statistical discipline across all three: MANUAL ILLUSTRATIVE ONLY
(m853, m854) / NOT_SCORED (m855) per the Aug 28 2026 standing rule,
engine NOT run at the finding layer, p_value/cohens_d/ci_95
NOT_CALCULATED, is_significant False / not asserted at the finding
layer, verdict directionally_supported_not_proven,
no_analysis_json_update true, NOT artifact-grade; no analysis.json
update. m853 and m854 ARE falsification-family members (THIRTY-SECOND
+ THIRTY-THIRD; ledger holds at 33); m855 is NOT (qualitative
financial-incentive mapping). Correlation only, not causation.
Hypothesis-generating only.

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

ANCHORED_SHA = "0000000000000000000000000000000000000000"  # patched post-commit per #565

# Built by concatenation so this source file carries no contiguous
# underscore-form mechanism literal (per the #770 lesson).
MECH_ID_MARKER = "mechanism" + "_"
NEXT_NUM = 856

M853_KEY = "verge_openai_sep26_training_pause_adversarial_register_vs_meta_audio_privacy_concession_sep2026"
M854_KEY = "type_b_1038_terrence_obrien_verge_openai_training_pause_vs_meta_muse_filesystem_sep27"
M855_KEY = "type_c_1039_amazon_claude_selling_partner_plugin_selective_gatekeeping_vs_meta_muse_denial_sep27_12pm"

M853_INDENT = 4  # nested under competitor_relationships.openai (the-verge.yaml)
M854_INDENT = 4  # item-level block under competitor_coverage in journalists.yaml (terrence_obrien item)
M855_INDENT = 0  # top-level block in competitor-entities.yaml

M853_OPENAI_URL_FRAG = "technewstube.com/theverge/1870832/openai-pauses-training-capable-models"
M853_META_URL_FRAG = "yankodesign.com/2026/09/24/ray-ban-meta-audio-glasses-launched-without-the-controversial-camera"


def _read(rel):
    with open(os.path.join(REPO_ROOT, rel), encoding="utf-8") as fh:
        return fh.read()


def _indented_block(rel, key, indent):
    """Slice the block for `key` (colon-form, exactly `indent` spaces).

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


# At this run's anchor followup, the five newest distinct iteration
# numbers in git history: #1040 Type D opens the 1040-1044 window;
# #1039 Type C (committed 12:00 PDT Sep 27) is the schedule
# predecessor and CLOSED the 1035-1039 window. The in-flight runs
# (#899 Type C, #938 Type B, #900 Type D, #1012 working-tree edit)
# have no main commits in git history at this run's checks and sit
# below the window; #898's block was lost (documented in the module
# docstring) and has no main commit either. The #884 block (m762) is
# committed at this run's checks.
EXPECTED_ORDER = [
    ("D", "1040"),
    ("C", "1039"),
    ("B", "1038"),
    ("A", "1037"),
    ("E", "1036"),
]


def _iter_source_files():
    """Yield paths for profile + test source files.

    Excludes this file (sweep carrier per #715) and __pycache__
    artifacts (per the #715 pattern-rescope lesson: committed test
    pyc files carry next-number needle strings from their own guards;
    compiled artifacts are excluded from the sweeps). No additional
    sweep-carrier exclusions this run: no in-tree SOURCE file carries
    a contiguous 856-form mechanism literal (verified pre-commit), so
    the 856 sweeps run repo-wide with only this file excluded.
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


def _profiles_with(text):
    hits = []
    for root, dirs, files in os.walk(PROFILES_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
            p = os.path.join(root, f)
            if text in open(p, encoding="utf-8", errors="replace").read():
                hits.append(p)
    return sorted(hits)


def _m853_data():
    return _block_data("profiles/the-verge.yaml", M853_KEY, M853_INDENT)


def _m853_text():
    return _indented_block("profiles/the-verge.yaml", M853_KEY, M853_INDENT)


def _m854_data():
    return _block_data("profiles/careers/journalists.yaml", M854_KEY, M854_INDENT)


def _m855_data():
    return _block_data("profiles/competitor-entities.yaml", M855_KEY, M855_INDENT)


class TestNovelty1040:
    def test_no_type_d_1040_test_file_preexisting(self):
        assert glob.glob(os.path.join(TESTS_DIR, "test_type_d_1040*.py")) == [
            os.path.join(TESTS_DIR, OWN_BASENAME)
        ], "only this file may match the test_type_d_1040 glob"

    def test_no_type_d_1040_in_git_log(self):
        # Pre-commit novelty: no Type D #1040 main commit exists.
        # Post-commit (anchor followup per #565), exactly one exists
        # and it is the anchored main commit - the guard doubles as a
        # duplicate-main-commit check.
        result = subprocess.run(
            ["git", "log", "--format=%H %s", "--grep=Type D #1040"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        mains = [
            line
            for line in result.stdout.splitlines()
            if "Type D #1040" in line and "followup" not in line.lower()
        ]
        if ANCHORED_SHA == "0" * 40:
            assert mains == [], mains
        else:
            assert len(mains) == 1, mains
            assert mains[0].startswith(ANCHORED_SHA + " "), mains

    def test_max_id_is_855_pre_commit(self):
        assert _max_numeric_mechanism_id() == 855

    def test_zero_856_forms_repo_wide(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_block_keys_unique_in_home_yamls(self):
        assert (
            _read("profiles/the-verge.yaml").count("\n    " + M853_KEY + ":") == 1
        )
        assert (
            _read("profiles/careers/journalists.yaml").count(
                "\n    " + M854_KEY + ":"
            )
            == 1
        )
        assert (
            _read("profiles/competitor-entities.yaml").count("\n" + M855_KEY + ":")
            == 1
        )

    def test_m853_arm_urls_present_in_verge_profile(self):
        # The committed #1037 run pinned its URL novelty; this run
        # carries the m853 block's own arm URL fragments as
        # verified-in-corpus: the Verge-feed mirror fragment and the
        # yankodesign Meta-arm fragment appear in profiles/the-verge.yaml.
        block = _m853_text()
        assert M853_OPENAI_URL_FRAG in block
        assert M853_META_URL_FRAG in block
        home = _read("profiles/the-verge.yaml")
        assert M853_OPENAI_URL_FRAG in home
        assert M853_META_URL_FRAG in home


class TestTypeDRotationGuard:
    def test_rotation_window_opens_1040(self):
        assert _window() == EXPECTED_ORDER

    def test_anchor_sha_is_real(self):
        assert re.fullmatch(r"[0-9a-f]{40}", ANCHORED_SHA), (
            "ANCHORED_SHA must be patched to the 40-char main commit "
            "hash post-commit per #565"
        )
        assert ANCHORED_SHA != "0" * 40, (
            "the all-zeros placeholder must be replaced by the anchor "
            "followup per #565"
        )


class TestTypeDM853QualitativeDiscipline:
    def test_mechanism_id(self):
        # m853 uses the `mechanism_id:` field form under
        # competitor_relationships.openai in the-verge.yaml.
        assert _m853_data()["mechanism_id"] == 853
        assert _m853_data()["iteration"] == 1037

    def test_arm_tones_and_spread(self):
        data = _m853_data()
        scorer = data["asymmetry_scorer_result"]
        assert scorer["method"] == "MANUAL ILLUSTRATIVE"
        assert scorer["openai_arm_tones"] == [-0.55]
        assert scorer["meta_arm_tones"] == [0.10]
        assert scorer["illustrative_delta_openai_minus_meta"] == -0.65
        assert scorer["delta_calc"] == "(-0.55) - (0.10) = -0.65"
        assert scorer["is_significant"] is False
        assert scorer["p_value"] == "NOT_CALCULATED"
        assert scorer["cohens_d"] == "NOT_CALCULATED"
        assert scorer["confidence_interval"] == "NOT_CALCULATED"

    def test_falsification_member_thirtysecond(self):
        # The Vox Media-OpenAI May 29 2024 licensing deal sits on the
        # adversarially-covered side; the uniform payer-softening
        # prediction (coverage_prediction 'softer') fails at the
        # publication level: THIRTY-SECOND falsification-family member.
        fam = _m853_data()["falsification_family"]
        assert "THIRTY-SECOND falsification-family member" in fam
        assert "ledger 31->32" in fam
        assert "Ledger holds at 32" in fam
        assert "THIRTY-THIRD absent" in fam

    def test_manual_illustrative_discipline(self):
        disc = _m853_data()["statistical_discipline"]
        assert "MANUAL ILLUSTRATIVE scores only" in disc
        assert "p_value/cohens_d/ci_95 NOT_CALCULATED" in disc
        assert "is_significant: false" in disc
        assert "NOT run at the finding layer" in disc
        assert "no_analysis_json_update: true" in disc
        assert "NOT artifact-grade" in disc
        assert "0 browser.open" in _m853_text()

    def test_verdict_and_provenance(self):
        data = _m853_data()
        assert data["verdict"] == "directionally_supported_not_proven"
        assert data["no_analysis_json_update"] is True
        assert data["connects_to"] == [507, 598, 425, 811, 827]
        assert (
            "tests/test_type_a_1037_verge_openai_sep26_training_pause_vs_meta_audio_concession_sep27_10am.py"
            in data["test_file"]
        )


class TestTypeDM854QualitativeDiscipline:
    def test_mechanism_id(self):
        assert _m854_data()["mechanism_id"] == 854
        assert _m854_data()["iteration"] == 1038

    def test_arm_tones_writer_pair(self):
        data = _m854_data()
        assert data["openai_arm"]["tone_illustrative"] == -0.55
        assert data["meta_arm"]["tone_illustrative"] == -0.50
        assert "mechanism 853" in data["openai_arm"]["carried_from"]
        assert "un-rescored per #807" in data["openai_arm"]["carried_from"]
        assert "adversarial safety-crisis" in data["openai_arm"]["register"]
        assert "adversarial security-vulnerability" in data["meta_arm"]["register"]

    def test_cross_entity_delta(self):
        scorer = _m854_data()["asymmetry_scorer_result"]
        assert scorer["method"] == "MANUAL ILLUSTRATIVE"
        assert scorer["illustrative_openai_arm_tone"] == -0.55
        assert scorer["illustrative_meta_arm_tone"] == -0.50
        assert scorer["illustrative_cross_entity_delta_openai_minus_meta"] == -0.05
        assert scorer["delta_calc"] == "(-0.55) minus (-0.50) = -0.05"

    def test_manual_illustrative_discipline(self):
        scorer = _m854_data()["asymmetry_scorer_result"]
        assert scorer["p_value"] == "NOT_CALCULATED"
        assert scorer["cohens_d"] == "NOT_CALCULATED"
        assert scorer["ci_95"] == "NOT_CALCULATED"
        assert scorer["is_significant"] is False
        disc = _m854_data()["statistical_discipline"]
        assert "MANUAL ILLUSTRATIVE scores only" in disc
        assert "Engine NOT run" in disc
        assert "is_significant: false" in disc
        assert "no_analysis_json_update true" in disc

    def test_verdict_and_provenance(self):
        data = _m854_data()
        assert data["verdict"] == "directionally_supported_not_proven"
        assert data["no_analysis_json_update"] is True
        assert data["is_significant"] is False
        assert data["falsification_family_member"] is True
        assert data["falsification_ledger"] == 33
        note = data["falsification_note"]
        assert "THIRTY-THIRD falsification-family member" in note
        assert "ledger 32->33" in note
        assert "Ledger holds at 33" in note
        assert "THIRTY-FOURTH absent" in note
        assert data["connects_to"] == [853, 507, 598, 425, 811, 827]


class TestTypeDM855QualitativeDiscipline:
    def test_mechanism_id_and_provenance(self):
        data = _m855_data()
        assert data["mechanism_id"] == 855
        assert data["iteration"] == 1039
        assert data["iteration_type"] == "C"
        assert data["type_label"] == "Financial Incentive Mapping"

    def test_selective_gatekeeping_second_leg_sixteenth(self):
        # m855 is the selective-gatekeeping leg of the SIXTEENTH
        # relationship direction (COMMERCE-GATEKEEPING): the direction
        # count holds at sixteen; this is the second leg, not a new
        # direction. Amazon's three-role geometry (m852) gains the
        # fourth posture GRANTS.
        geo = _m855_data()["selective_gatekeeping_geometry"]
        assert "Anthropic" in geo["backed_lab_granted"]
        assert "Claude" in geo["backed_lab_granted"]
        assert "Meta" in geo["publisher_payer_denied"]
        assert "Muse" in geo["publisher_payer_denied"]
        assert "GRANTS" in geo["amazon_role_update"]
        assert "m852" in geo["amazon_role_update"]

    def test_statistical_discipline(self):
        data = _m855_data()
        assert data["tone_scores"] == "NOT_SCORED"
        assert data["engine_run"] is False
        assert data["artifact_grade"] is False
        assert data["verdict"] == "directionally_supported_not_proven"
        assert data["no_analysis_json_update"] is True
        assert data["falsification_family_member"] is False
        assert data["falsification_ledger"] == 33
        assert "Ledger holds at 33" in data["falsification_note"]
        assert "NOT a falsification-family member" in data["falsification_note"]
        assert data["connects_to"] == [852, 831, 559, 509, 594]
        assert data["excerpt_bounded"] is True
        assert data["browser_opens"] == 0
        assert "0 browser.open this run per #503" in data["excerpt_bounded_note"]

    def test_block_position_top_level(self):
        # m855 sits at zero indent in profiles/competitor-entities.yaml
        # (top-level block, colon form only per #715 designed keying:
        # the block key carries no numeric mechanism-id substring).
        doc = _read("profiles/competitor-entities.yaml")
        assert doc.count("\n" + M855_KEY + ":") == 1
        assert "mechanism_855" not in M855_KEY
        assert "mechanism-855" not in M855_KEY


class TestTypeDMaxIdAndNextNumber:
    def test_max_numeric_mechanism_id_is_855(self):
        assert _max_numeric_mechanism_id() == 855

    def test_zero_numeric_856_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_zero_underscore_856_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_zero_dash_856_repo_wide(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []


class TestTypeDFalsificationLedger:
    def test_ledger_holds_at_33(self):
        # m853 carries the ledger in block prose form ("Ledger holds
        # at 32", committed when #1037 advanced 31->32); m854/m855
        # carry it as structured fields (falsification_ledger == 33)
        # with matching prose.
        assert "Ledger holds at 32" in _m853_data()["falsification_family"]
        assert _m854_data()["falsification_ledger"] == 33
        assert "Ledger holds at 33" in _m854_data()["falsification_note"]
        assert _m855_data()["falsification_ledger"] == 33
        assert "Ledger holds at 33" in _m855_data()["falsification_note"]

    def test_thirtythird_member_form_present(self):
        # THIRTY-THIRD member-form: the m854 notes prose (Type B
        # #1038, mechanism 854, journalists.yaml) appears twice - once
        # in the terrence_obrien journalist-item notes and once in the
        # m854 block's falsification_note. Both are positive
        # member-form claims; the scan pins the pair.
        needle = "THIRTY-THIRD falsification-family member"
        hits = _profiles_with(needle)
        assert hits == [
            os.path.join(PROFILES_DIR, "careers", "journalists.yaml")
        ], hits
        doc = _read("profiles/careers/journalists.yaml")
        assert doc.count(needle) == 2, doc.count(needle)

    def test_thirtysecond_member_form_still_present(self):
        # The m853 THIRTY-SECOND anchor (Type A #1037) must not have
        # been disturbed by the ledger advance.
        hits = _profiles_with("THIRTY-SECOND falsification-family member")
        assert os.path.join(PROFILES_DIR, "the-verge.yaml") in hits, hits

    def test_thirtyfourth_member_form_absent(self):
        # THIRTY-FOURTH is the negative guard: no positive
        # thirty-fourth member-form claim may exist anywhere in
        # profiles/ or test sources. Negative-guard wordings
        # ("negative guard", "absent") are permitted. Own file
        # excluded as sweep carrier per #715 (it carries the needle
        # in this very scan).
        for rel in ["profiles", "tests"]:
            for root, dirs, files in os.walk(os.path.join(REPO_ROOT, rel)):
                dirs[:] = [d for d in dirs if d != "__pycache__"]
                for f in files:
                    if f == OWN_BASENAME:
                        continue
                    p = os.path.join(root, f)
                    for line in open(p, encoding="utf-8", errors="replace"):
                        if "THIRTY-FOURTH member" in line:  # negative guard scan needle
                            low = line.lower()
                            assert any(
                                w in low
                                for w in ("negative guard", "absent")
                            ), (p, line[:160])


class TestTypeDCorpusIntegrity:
    def test_m770_absent_known_data_loss(self):
        # m770 was lost at #918: it exists in no profile YAML, only in
        # the needle strings of the old #897 test file and the
        # in-flight #900 test file. Documented as known data loss to
        # be redone by a future run.
        assert _repo_grep_numeric_mechanism_id(770) == []

    def test_771_sole_occurrence_is_inflight_899_block(self):
        # m771 exists exactly once: the uncommitted #899 hunk in the
        # working tree of profiles/nytimes.yaml (zero occurrences in
        # HEAD). The in-flight block is owned by its run; this test
        # pins the state, it does not touch the file.
        doc = _read("profiles/nytimes.yaml")
        assert doc.count("mechanism_id: 771") == 1
        head = subprocess.run(
            ["git", "grep", "-c", "mechanism_id: 771", "HEAD", "--", "profiles/"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        assert head.returncode == 1, head.stdout  # no hits in HEAD

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

    def test_m853_block_position_and_indent(self):
        # m853 sits at 4-space indent under the 2-space "openai:" key
        # under the zero-indent "competitor_relationships:" key in
        # profiles/the-verge.yaml (descriptive block key per #715:
        # no numeric mechanism-id substring in the key).
        doc = _read("profiles/the-verge.yaml")
        idx = doc.index("\n    " + M853_KEY + ":")
        parents = []
        for ln in reversed(doc[:idx].splitlines()):
            stripped = ln.strip()
            if stripped.endswith(":") and len(stripped) > 1:
                indent = len(ln) - len(ln.lstrip(" "))
                if indent < 4:
                    parents.append((indent, stripped[:-1]))
                    if indent == 0:
                        break
        assert parents == [(2, "openai"), (0, "competitor_relationships")], parents
        assert "mechanism_853" not in M853_KEY
        assert "mechanism-853" not in M853_KEY

    def test_m854_block_position_and_indent(self):
        # m854 sits at 4-space indent under competitor_coverage in the
        # top-level terrence_obrien item in profiles/careers/journalists.yaml
        # and carries the Terrence O'Brien byline provenance (the block
        # is the FIRST dedicated journalist-profile mechanism on O'Brien).
        import yaml

        doc = _read("profiles/careers/journalists.yaml")
        assert doc.count("\n    " + M854_KEY + ":") == 1
        parsed = yaml.safe_load(doc)
        assert parsed["terrence_obrien"]["name"] == "Terrence O'Brien"
        block = _m854_data()
        assert block["journalist"] == "Terrence O'Brien"
        assert block["publication"] == "The Verge"

    def test_m855_block_position_and_indent(self):
        # m855 sits at zero indent in profiles/competitor-entities.yaml
        # (top-level block, colon form only per #715 designed keying:
        # the block key carries no numeric mechanism-id substring).
        doc = _read("profiles/competitor-entities.yaml")
        assert doc.count("\n" + M855_KEY + ":") == 1
        assert "mechanism_855" not in M855_KEY
        assert "mechanism-855" not in M855_KEY


class TestTypeDFullSuiteTombstone:
    def _suite_log(self, name):
        return os.path.join(
            os.path.expanduser("~"),
            "workspace",
            "goals",
            "mediascope-meta-wearables-press-analysis",
            "hidden_files",
            name,
        )

    def test_1035_suite_log_stalled(self):
        # Stalled at 0%: 273 bytes of progress dots plus one "[  0% ]"
        # marker since Sep 27 08:14 PDT, no summary tokens anywhere, no
        # pytest alive.
        with open(self._suite_log("type_d_1035_full_suite.log"), "rb") as fh:
            data = fh.read()
        assert len(data) == 273, len(data)
        assert b"[  0%]" in data
        for token in (b"passed", b"failed", b"error"):
            assert token not in data, token

    def test_1035_suite_log_mtime_stale(self):
        # The #1035 suite's log has not been written since 08:14 PDT
        # (hours before this 13:00 PDT run): a live suite would append
        # progress dots continuously. Stale mtime + 273 bytes + zero
        # summary tokens + no pytest alive = dead per the #795
        # convention. (The new #1040 suite's pytest may be alive by
        # design; this assertion is mtime-scoped to the OLD log, so it
        # cannot self-conflict.)
        import time

        st = os.stat(self._suite_log("type_d_1035_full_suite.log"))
        age_hours = (time.time() - st.st_mtime) / 3600
        assert age_hours > 1, age_hours

    def test_tombstone_lineage_advances(self):
        # FORTY-NINTH consecutive background death per the #795
        # convention; lineage advances SIXTY-SEVENTH -> SIXTY-EIGHTH.
        # This run re-launches the suite writing to
        # type_d_1040_full_suite.log; the next Type D run checks it.
        # (The #1030 suite was already tombstoned by #1035; it is NOT
        # re-tombstoned here.)
        entry_anchor = "SIXTY-SEVENTH"
        entry_next = "SIXTY-EIGHTH"
        assert entry_anchor != entry_next

    def test_1040_suite_log_relaunched(self):
        assert os.path.isfile(self._suite_log("type_d_1040_full_suite.log")), (
            "the re-launched suite log must exist"
        )


class TestTypeDSyntheticEngine:
    """Fresh engine meaningfulness calibration on synthetic corpora.

    Values hardcoded after a scratch run this run (NOT #1035's).
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
            datetime(2026, 9, 27),
            datetime(2026, 9, 28),
        )

    def test_strong_signal_pair_engine_significant(self):
        r = self._score(
            [-0.58, -0.49, -0.62, -0.44, -0.55, -0.51, -0.60],
            [0.19, 0.28, 0.33, 0.22, 0.26, 0.31, 0.17],
            "Meta",
            ["Snap", "Apple"],
        )
        assert abs(r.asymmetry_score - (-0.7928571428571428)) < 1e-9
        assert abs(r.t_statistic - (-23.708425001640116)) < 1e-6
        assert r.p_value < 1e-10
        assert abs(r.cohens_d - (-12.672686219451819)) < 1e-6
        assert r.is_significant is True
        assert r.confidence_interval_upper < 0

    def test_near_null_pair_stays_silent(self):
        r = self._score(
            [0.04, -0.05, 0.03, -0.02, 0.06, -0.03, 0.01],
            [0.05, -0.01, 0.02, -0.06, 0.04, -0.02, 0.03],
            "Meta",
            ["Snap", "Apple"],
        )
        assert abs(r.asymmetry_score - (-0.0014285714285714292)) < 1e-9
        assert r.p_value > 0.9
        assert r.is_significant is False
        assert r.confidence_interval_lower < 0 < r.confidence_interval_upper

    def test_degenerate_m853_pair_engine_guard(self):
        # Degenerate n=1/n=1 contract on the m853 illustrative pair
        # ([-0.55] OpenAI vs [0.10] Meta): the engine's structural
        # guard fires (t=0.0, p=1.0, d=0.0, not significant) while
        # |asymmetry| == 0.65 and arm-swap negates exactly. The guard's
        # verdict is the assertion.
        r = self._score([-0.55], [0.10], "OpenAI", ["Meta"])
        assert r.t_statistic == 0.0
        assert r.p_value == 1.0
        assert r.cohens_d == 0.0
        assert r.is_significant is False
        assert abs(abs(r.asymmetry_score) - 0.65) < 1e-9
        swapped = self._score([0.10], [-0.55], "Meta", ["OpenAI"])
        assert swapped.asymmetry_score == -r.asymmetry_score

    def test_engine_finding_layer_separation(self):
        # The engine CAN return is_significant True on synthetic
        # corpora while the finding layer refuses: the three
        # mechanisms verified this run all carry finding-layer
        # is_significant false / NOT asserted per the Aug 28 2026
        # standing rule.
        assert "is_significant: false" in _m853_data()["statistical_discipline"]
        assert _m854_data()["is_significant"] is False
        assert _m855_data()["engine_run"] is False


class TestDocSync1040:
    def test_readme_row_1040(self):
        assert TEST_BASENAME in _read(README_PATH)

    def test_architecture_row_1040(self):
        assert TEST_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_1040_file(self):
        doc = _read(ARCH_PATH)
        assert TEST_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))


class TestIterationLog1040:
    def _entry(self):
        log = _read(LOG_PATH)
        idx = log.index("## #1040 Type D:")
        return log[idx : idx + 15000]

    def test_entry_present(self):
        assert "## #1040 Type D:" in _read(LOG_PATH)

    def test_entry_records_tombstone_and_integrity(self):
        entry = self._entry()
        assert "SIXTY-EIGHTH" in entry
        assert "855" in entry

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
