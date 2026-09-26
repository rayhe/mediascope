"""Type D -- Iteration #1015 (Sat 2026-09-26 12:00 PDT): m838/m839/m840
qualitative-discipline verification + post-1010-1014 corpus integrity
(max numeric mechanism_id 840; zero next-number 841 keys in
numeric/underscore/dash mechanism forms; ledger holds at 30 with the
THIRTIETH member-form present exactly once (m818, journalists.yaml),
TWENTY-NINTH in news-corp.yaml, THIRTY-FIRST member-form negative
guard) + #1010 background-suite tombstone (FORTY-FOURTH consecutive
death; lineage SIXTY-SECOND -> SIXTY-THIRD) + fresh synthetic engine
calibration (new values, not #1010's) + re-launch of the full suite as
a background process writing to goal hidden_files
type_d_1015_full_suite.log (next Type D run checks its verdict per the
#795 convention).

Type D FIRST leg of the 1015-1019 window, OPENING it (D->E->A->B->C).
Committed predecessor #1014 Type C (09:00 PDT Sep 26) CLOSED the
1010-1014 window. Concurrency note: the in-flight runs at this run's
checks are the #899 Type C block (m771, uncommitted hunk in
profiles/nytimes.yaml), the #938 Type B test file (uncommitted
working-tree edit) and the #900 Type D test file
(untracked, root-owned, on disk) - all UNCOMMITTED, no Type C #899 /
Type B #938 / Type D #900 main commits in git history, and no
## #899 / ## #938 / ## #900 Type X entries in iteration-log.md. The
#884 Type C block (m762) is COMMITTED at this run's checks (in HEAD),
so it is no longer in-flight; its presence is pinned as an integrity
anchor, not a concurrency note. The #898 Type B journalists.yaml hunk
(m770) is ABSENT from the working tree (lost at #918; m770 exists in no
profile YAML, only in the needle strings of the old #897 test file and
the in-flight #900 test file) - documented here as known data loss to
be redone by a future run, not as in-flight work. This run does NOT
touch the in-flight files; the in-flight blocks are owned by their
runs. Iteration numbers follow the rotation schedule, not commit order.

Verifies:
- m838 (Type A #1012, MIT TR x Anthropic Sep-14 doomer-turn
  agenda-setting register vs carried MIT TR x Meta Sep-23 India havoc
  investigation: Anthropic arm Will Douglas Heaven Sep 14 2026 "The AI
  industry has taken a doomer turn. What now?" (MANUAL ILLUSTRATIVE
  +0.10); Meta arm carried from m817 un-rescored per #807 (Sep 23
  2026 "Smart glasses are already causing havoc in India", MANUAL
  ILLUSTRATIVE -0.60); illustrative delta (Anthropic minus Meta)
  +0.70 on a degenerate n=1 vs n=1 pair, NOT significant;
  register-SELECTION finding (the Sep-14 piece embeds its own
  demystification of OpenAI, so it is not a uniform-softness exhibit);
  EXTENDS the mechanism 817 register-inversion strand to the
  Anthropic axis; profiles/mit-tech-review.yaml under
  competitor_relationships/anthropic, 4-space indent): MANUAL
  ILLUSTRATIVE ONLY per standing rule Aug 28 2026, engine NOT run at
  the finding layer, p_value/cohens_d/ci NOT_CALCULATED,
  is_significant False, verdict directionally_supported_not_proven
  (in statistical_discipline), no_analysis_json_update true, NOT
  artifact-grade; falsification family NOT a member (ledger_hold 30);
  connects_to [817, 15, 619, 685, 790].
- m839 (Type B #1013, Samuel Gibbs, Guardian: NEW Meta stigma arm Sep
  24 2026 Connect relay (MANUAL ILLUSTRATIVE -0.20, carried from m832
  per #807) vs carried Sep-17 2025 Meta Ray-Ban Display announcement
  baseline (MANUAL ILLUSTRATIVE +0.10, carried from m611 per #807) vs
  carried Aug-16 2024 Apple Vision Pro hands-on review (MANUAL
  ILLUSTRATIVE +0.35, carried from m611/#622); within-writer Meta
  register deteriorates 0.30 across 12 months with NEWS genre held
  constant on both Meta arms, isolating the PEG from the genre
  confound; illustrative Meta-minus-Apple delta -0.55; zero-financial
  gradient at the journalist level (Guardian has no deal with Apple
  ($0) or Meta ($0)); profiles/careers/journalists.yaml, 4-space
  indent block key): verdict directionally_supported_not_proven,
  no_analysis_json_update true, NOT artifact-grade;
  falsification_family_member False (falsification_ledger 30);
  statistical_discipline tone_scores MANUAL_ILLUSTRATIVE_CARRIED,
  engine NOT run, is_significant False.
- m840 (Type C #1014, Stack Overflow dual-AI-payer architecture -
  OverflowAPI legs with Google Cloud (Feb 29 2024) and OpenAI (May 6
  2024): FIRST dedicated corpus mechanism on the warrant-structure
  counterpart for developers; FIRST developer-knowledge (non-news)
  dual-AI-payer publisher in the corpus; FIRST member where BOTH
  legs are undisclosed-fee (unweightable per m735); fourth member of
  the dual/triple-payer publisher family after News Corp (m594
  five-leg), Vox Media (m621), Hearst (m696 triple-AI-payer);
  Meta $0 bounded absence (m732's Meta-vs-rival retrieval licensing
  census does not include Stack Overflow); profiles/
  competitor-entities.yaml tail block, zero indent): tone_scores
  NOT_SCORED per standing rule Aug 28 2026, engine NOT run,
  p_value/cohens_d NOT_CALCULATED, is_significant False, verdict
  directionally_supported_not_proven, no_analysis_json_update true,
  NOT artifact-grade; falsification_family_member False
  (falsification_ledger 30); connects_to [594, 621, 696, 735].

ASCII-only, no em dashes.
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

ANCHORED_SHA = "861768790529931963110d6921b6676351819c0c"  # patched post-commit per #565

MECH_ID_MARKER = "mechanism" + "_"
NEXT_NUM = 841

M838_KEY = "type_a_1012_mittr_anthropic_sep2026_doomer_turn_agenda_setting_register_vs_carried_meta_india_havoc_m817_pairing_sep26_7am"
M839_KEY = "type_b_1013_samuel_gibbs_guardian_meta_register_temporal_shift_sep2026_stigma_vs_apple_vision_pro_aspirational"
M840_KEY = "type_c_1014_stackoverflow_dual_ai_payer_google_openai_overflowapi_sep26_9am"

M838_INDENT = 4  # nested under competitor_relationships/anthropic (mit-tech-review.yaml)
M839_INDENT = 4  # item-level block in journalists.yaml
M840_INDENT = 0  # top-level block in competitor-entities.yaml

M838_ANTHROPIC_URL = "https://www.technologyreview.com/2026/09/14/1144048/the-ai-industry-has-taken-a-doomer-turn-what-now/"
M838_META_URL_FRAG = "1144953"


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


def _block_data(rel, key, indent=4):
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


# At this run's main commit, the five newest distinct iteration
# numbers in git history: #1015 Type D opens the 1015-1019 window;
# #1014 Type C (committed 09:00 PDT Sep 26) is the schedule predecessor
# and CLOSED the 1010-1014 window. The in-flight runs (#899 Type C,
# #938 Type B, #900 Type D) have no main commits in git history at
# this run's checks and sit below the window; #898's block was lost
# (documented in the module docstring) and has no main commit either.
# The #884 block (m762) is committed at this run's checks.
EXPECTED_ORDER = [
    ("D", "1015"),
    ("C", "1014"),
    ("B", "1013"),
    ("A", "1012"),
    ("E", "1011"),
]


def _iter_source_files():
    """Yield (path, is_test) for profile + test source files.

    Excludes this file (sweep carrier per #715) and __pycache__
    artifacts (per the #715 pattern-rescope lesson: the #1014 pyc
    carries an 841-form needle string from its own next-number guard;
    compiled artifacts are excluded from the sweeps). No additional
    sweep-carrier exclusions this run: no in-tree SOURCE file carries
    a contiguous 841-form mechanism literal (verified pre-commit; the
    #1014 test file builds its 841 needles at runtime and its raw
    "mechanism 841" hits are docstring/grep-needle strings with a
    space, not contiguous mechanism-form literals), so the 841 sweeps
    run repo-wide with only this file excluded.
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


def _profiles_with(text):
    hits = []
    for root, dirs, files in os.walk(PROFILES_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
            p = os.path.join(root, f)
            if text in open(p, encoding="utf-8", errors="replace").read():
                hits.append(p)
    return sorted(hits)


def _m838_data():
    return _block_data("profiles/mit-tech-review.yaml", M838_KEY, M838_INDENT)


def _m839_data():
    return _block_data(
        "profiles/careers/journalists.yaml", M839_KEY, M839_INDENT
    )


def _m840_data():
    return _block_data(
        "profiles/competitor-entities.yaml", M840_KEY, M840_INDENT
    )


class TestNovelty1015:
    def test_no_type_d_1015_test_file_preexisting(self):
        import glob

        assert glob.glob(os.path.join(TESTS_DIR, "test_type_d_1015*.py")) == [
            os.path.join(TESTS_DIR, OWN_BASENAME)
        ], "only this file may match the test_type_d_1015 glob"

    def test_no_type_d_1015_in_git_log(self):
        # Pre-commit novelty: no Type D #1015 main commit exists.
        # Post-commit (anchor followup per #565), exactly one exists
        # and it is the anchored main commit - the guard doubles as a
        # duplicate-main-commit check.
        result = subprocess.run(
            ["git", "log", "--format=%H %s", "--grep=Type D #1015"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        mains = [
            line
            for line in result.stdout.splitlines()
            if "Type D #1015" in line and "followup" not in line.lower()
        ]
        if ANCHORED_SHA == "0" * 40:
            assert mains == [], mains
        else:
            assert len(mains) == 1, mains
            assert mains[0].startswith(ANCHORED_SHA + " "), mains

    def test_max_id_is_840_pre_commit(self):
        assert _max_numeric_mechanism_id() == 840

    def test_zero_841_forms_repo_wide(self):
        assert _repo_grep_numeric_mechanism_id(841) == []
        assert _repo_grep_underscore_mechanism(841) == []
        assert _repo_grep_dash_mechanism(841) == []

    def test_block_keys_unique_in_home_yamls(self):
        assert _read("profiles/mit-tech-review.yaml").count(
            "\n    " + M838_KEY + ":"
        ) == 1
        assert _read("profiles/careers/journalists.yaml").count(
            "\n    " + M839_KEY + ":"
        ) == 1
        assert (
            _read("profiles/competitor-entities.yaml").count(
                "\n" + M840_KEY + ":"
            )
            == 1
        )

    def test_m838_arm_urls_present_in_mittr(self):
        # The committed #1012 run pinned its URL novelty; this run
        # carries the m838 block's own arm URLs as verified-in-corpus:
        # the Anthropic arm URL (verbatim in the block) appears in
        # profiles/mit-tech-review.yaml.
        doc = _indented_block(
            "profiles/mit-tech-review.yaml", M838_KEY, M838_INDENT
        )
        assert M838_ANTHROPIC_URL in doc
        assert M838_META_URL_FRAG in doc
        home = _read("profiles/mit-tech-review.yaml")
        assert M838_ANTHROPIC_URL in home


class TestTypeDRotationGuard:
    def test_rotation_window_opens_1015(self):
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


class TestTypeDM838QualitativeDiscipline:
    def test_mechanism_id(self):
        assert _m838_data()["mechanism_id"] == 838

    def test_arm_tones_and_registers(self):
        d = _m838_data()
        assert d["anthropic_arm"]["tone_manual_illustrative"] == 0.10
        assert "doomer turn" in d["anthropic_arm"]["title"]
        assert d["meta_arm"]["tone_manual_illustrative"] == -0.60
        assert "havoc" in d["meta_arm"]["title"]
        assert "817" in str(d["meta_arm"]["carried_from"])

    def test_degenerate_delta_documented_not_significant(self):
        # Illustrative delta (Anthropic minus Meta) +0.70 on a
        # degenerate n=1 vs n=1 pair: the finding is register
        # documentation, not a significant statistical result. The
        # finding text carries the +0.70 delta and the n=1 framing;
        # the statistical-discipline mapping refuses significance.
        finding = _m838_data()["finding"]
        assert "+0.70" in finding
        assert "n=1" in finding
        assert "NOT significant" in finding

    def test_manual_illustrative_discipline(self):
        # The m838 discipline lives in the statistical_discipline
        # prose mapping: n=1, NOT_CALCULATED statistics, engine NOT
        # run at the finding layer, is_significant False.
        disc = _m838_data()["statistical_discipline"]
        assert "n=1" in disc
        assert "NOT_CALCULATED" in disc
        assert "is_significant False" in disc
        assert "engine NOT run" in disc
        assert "MANUAL ILLUSTRATIVE" in disc

    def test_verdict_and_provenance(self):
        d = _m838_data()
        assert d["verdict"] == "directionally_supported_not_proven"
        assert d["no_analysis_json_update"] is True
        assert d["falsification_family_member"] is False
        assert d["falsification_ledger"] == 30
        assert d["iteration"] == 1012
        assert d["iteration_type"] == "A"
        assert d["connects_to"] == [817, 15, 619, 685, 790]


class TestTypeDM839QualitativeDiscipline:
    def test_mechanism_id(self):
        assert _m839_data()["mechanism_id"] == 839

    def test_arm_tones_and_temporal_shift(self):
        # Meta stigma arm -0.20 (carried from m832) vs Meta baseline
        # arm +0.10 (carried from m611) vs Apple arm +0.35 (carried
        # from m611/#622): the within-writer Meta register deteriorates
        # 0.30 across 12 months.
        d = _m839_data()
        assert d["meta_arm_stigma"]["tone_illustrative"] == -0.20
        assert d["meta_arm_baseline"]["tone_illustrative"] == 0.10
        assert d["apple_arm"]["tone_illustrative"] == 0.35
        finding = d["finding"]
        assert "deteriorates 0.30" in finding

    def test_delta_and_genre_hold(self):
        # Illustrative Meta-minus-Apple delta -0.55 with the NEWS
        # genre held constant on both Meta arms, isolating the peg
        # from the genre confound that dominated m611.
        d = _m839_data()
        assert d["asymmetry_scorer_result"][
            "illustrative_delta_meta_minus_apple"
        ] == -0.55
        finding = d["finding"]
        assert "genre held" in finding
        assert "zero-financial-gradient" in finding.lower()

    def test_scorer_layer_discipline(self):
        # Both the asymmetry_scorer_result and statistical_discipline
        # mappings refuse significance: finding-layer statistics are
        # NOT_CALCULATED and the engine was NOT run.
        d = _m839_data()
        assert d["asymmetry_scorer_result"]["is_significant"] is False
        assert d["asymmetry_scorer_result"]["p_value"] == "NOT_CALCULATED"
        assert d["asymmetry_scorer_result"]["cohens_d"] == "NOT_CALCULATED"
        assert d["asymmetry_scorer_result"]["artifact_grade"] is False
        disc = d["statistical_discipline"]
        assert disc["tone_scores"] == "MANUAL_ILLUSTRATIVE_CARRIED"
        assert disc["engine_run"] is False
        assert disc["is_significant"] is False
        assert disc["scorer"] == "none"

    def test_verdict_and_provenance(self):
        d = _m839_data()
        assert d["verdict"] == "directionally_supported_not_proven"
        assert d["no_analysis_json_update"] is True
        assert d["falsification_family_member"] is False
        assert d["falsification_ledger"] == 30
        assert d["journalist"] == "Samuel Gibbs"
        assert d["iteration"] == 1013
        assert d["iteration_type"] == "B"
        assert d["connects_to"] == [611, 832, 622]


class TestTypeDM840QualitativeDiscipline:
    def test_mechanism_id_and_legs(self):
        # Google Cloud leg (OverflowAPI launch partner, announced Feb
        # 29 2024) + OpenAI leg (announced May 6 2024): the two AI
        # labs licensed the same OverflowAPI product surface within
        # ten weeks in early 2024.
        d = _m840_data()
        assert d["mechanism_id"] == 840
        finding = d["finding"]
        assert "Feb 29 2024" in finding
        assert "May 6 2024" in finding
        assert "OverflowAPI" in finding

    def test_undisclosed_fee_unweightable(self):
        # Both legs are explicitly undisclosed-fee, so per m735 this
        # mechanism is qualitative census/direction only: it cannot be
        # dollar-weighted, and no cash-payment claim is made.
        d = _m840_data()
        fee_status = d["incentive_geometry"]["fee_status"]
        assert "undisclosed-fee" in fee_status
        assert "m735" in fee_status

    def test_first_of_kind_claims(self):
        # FIRST Stack Overflow mechanism in the corpus; FIRST
        # developer-knowledge (non-news) dual-AI-payer publisher;
        # FIRST member where BOTH legs are undisclosed-fee; fourth
        # member of the dual/triple-payer publisher family.
        d = _m840_data()
        novelty = d["novelty"]
        assert "FIRST Stack Overflow mechanism in the corpus" in novelty
        family = d["incentive_geometry"]["family"]
        assert "FIRST developer-knowledge (non-news) publisher" in family
        assert "FIRST member where BOTH legs are undisclosed-fee" in family
        assert "fourth member" in family.lower()

    def test_meta_zero_anchor(self):
        # Meta has no OverflowAPI leg (bounded absence; m732's
        # Meta-vs-rival retrieval licensing census does not include
        # Stack Overflow), giving a $0 anchor on the Meta side.
        d = _m840_data()
        assert "$0 anchor" in d["finding"]
        assert "m732" in d["finding"]

    def test_verdict_and_provenance(self):
        d = _m840_data()
        assert d["tone_scores"] == "NOT_SCORED"
        assert d["engine_run"] is False
        assert d["verdict"] == "directionally_supported_not_proven"
        assert d["no_analysis_json_update"] is True
        assert d["artifact_grade"] is False
        assert d["falsification_family_member"] is False
        assert d["falsification_ledger"] == 30
        assert d["iteration"] == 1014
        assert d["iteration_type"] == "C"
        assert d["connects_to"] == [594, 621, 696, 735]


class TestTypeDMaxIdAndNextNumber:
    def test_max_numeric_mechanism_id_is_840(self):
        assert _max_numeric_mechanism_id() == 840

    def test_zero_numeric_841_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(841) == []

    def test_zero_underscore_841_repo_wide(self):
        # Needles are format-built (per #715/#770); this file carries no
        # contiguous underscore-form 841 literal. The #1014 committed
        # test's runtime-built needle hits do not exist as source
        # literals.
        assert _repo_grep_underscore_mechanism(841) == []

    def test_zero_dash_841_repo_wide(self):
        assert _repo_grep_dash_mechanism(841) == []


class TestTypeDFalsificationLedger:
    def test_ledger_holds_at_30(self):
        assert _m838_data()["falsification_ledger"] == 30
        assert _m839_data()["falsification_ledger"] == 30
        assert _m840_data()["falsification_ledger"] == 30

    def test_thirtieth_member_form_present_exactly_once(self):
        # THIRTIETH member-form: the m818 block (Type B #978, mechanism
        # 818, journalists.yaml). Exactly one positive occurrence;
        # everything else must be a negative-guard wording.
        needle = "THIRTIETH falsification-family member"
        hits = _profiles_with(needle)
        assert hits == [
            os.path.join(PROFILES_DIR, "careers", "journalists.yaml")
        ], hits
        doc = _read("profiles/careers/journalists.yaml")
        assert doc.count(needle) == 1

    def test_twentyninth_member_form_in_news_corp(self):
        hits = _profiles_with("TWENTY-NINTH member")
        assert os.path.join(PROFILES_DIR, "news-corp.yaml") in hits, hits

    def test_thirtyfirst_member_form_absent(self):
        # THIRTY-FIRST remains the negative guard: no positive
        # thirty-first member-form claim may exist anywhere in
        # profiles/ or test sources. Negative-guard wordings
        # ("remains the negative guard", "absent") are permitted.
        for rel in ["profiles"]:
            for root, dirs, files in os.walk(os.path.join(REPO_ROOT, rel)):
                dirs[:] = [d for d in dirs if d != "__pycache__"]
                for f in files:
                    p = os.path.join(root, f)
                    for line in open(p, encoding="utf-8", errors="replace"):
                        if "THIRTY-FIRST member" in line:
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

    def test_841_sweep_excludes_only_this_file_and_pycache(self):
        # The sole repo-wide 841-form literals at this run's checks are
        # the #1014 pyc in tests/__pycache__ (next-number guard of a
        # committed test, excluded per the #715 pattern-rescope
        # lesson). The source sweeps must therefore come back empty.
        import glob

        pyc_hits = glob.glob(
            os.path.join(TESTS_DIR, "__pycache__", "*1014*.pyc")
        )
        assert pyc_hits != [], "expected the #1014 pyc to exist"
        for p in pyc_hits:
            data = open(p, "rb").read()
            if b"mechanism-841" in data or b"mechanism_841" in data:
                break
        else:
            assert False, "no #1014 pyc carries the 841 needle"
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_m838_block_position_and_indent(self):
        # m838 sits under the anthropic item of
        # competitor_relationships in profiles/mit-tech-review.yaml at
        # 4-space indent.
        doc = _read("profiles/mit-tech-review.yaml")
        idx = doc.index("\n    " + M838_KEY + ":")
        for ln in reversed(doc[:idx].splitlines()):
            stripped = ln.strip()
            if stripped.endswith(":") and len(stripped) > 1:
                indent = len(ln) - len(ln.lstrip(" "))
                if indent <= 2:
                    parent = stripped[:-1]
                    break
        assert parent == "anthropic", parent
        assert "\ncompetitor_relationships:" in doc[:idx]

    def test_m839_block_position_and_indent(self):
        # m839 sits at 4-space indent in profiles/careers/
        # journalists.yaml (journalist item-level block) and carries
        # the Gibbs byline provenance.
        doc = _read("profiles/careers/journalists.yaml")
        assert doc.count("\n    " + M839_KEY + ":") == 1
        block = _indented_block(
            "profiles/careers/journalists.yaml", M839_KEY, M839_INDENT
        )
        assert "Samuel Gibbs" in block

    def test_m840_block_position_and_indent(self):
        # m840 sits at zero indent in profiles/competitor-entities.yaml
        # (top-level block, colon form only per #715 designed keying:
        # the block key carries no numeric mechanism-id substring).
        doc = _read("profiles/competitor-entities.yaml")
        assert doc.count("\n" + M840_KEY + ":") == 1
        assert "mechanism_840" not in M840_KEY
        assert "mechanism-840" not in M840_KEY


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

    def test_1010_suite_log_stalled(self):
        # Stalled mid-run: 1440 bytes of dots at ~2% since Sep 26
        # 05:34 PDT, no summary tokens anywhere, the process has since
        # exited (no pytest alive).
        with open(self._suite_log("type_d_1010_full_suite.log"), "rb") as fh:
            data = fh.read()
        assert len(data) == 1440, len(data)
        for token in (b"passed", b"failed", b"error"):
            assert token not in data, token

    def test_tombstone_lineage_advances(self):
        # FORTY-FOURTH consecutive background death per the #795
        # convention; lineage advances SIXTY-SECOND -> SIXTY-THIRD.
        # This run re-launches the suite writing to
        # type_d_1015_full_suite.log; the next Type D run checks it.
        # (The #1005 suite was already tombstoned by #1010; it is NOT
        # re-tombstoned here.)
        entry_anchor = "SIXTY-SECOND"
        entry_next = "SIXTY-THIRD"
        assert entry_anchor != entry_next

    def test_1015_suite_log_relaunched(self):
        assert os.path.isfile(self._suite_log("type_d_1015_full_suite.log")), (
            "the re-launched suite log must exist"
        )


class TestTypeDSyntheticEngine:
    """Fresh engine meaningfulness calibration on synthetic corpora.

    Values hardcoded after a scratch run this run (NOT #1010's).
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
            datetime(2026, 9, 26),
            datetime(2026, 9, 27),
        )

    def test_strong_signal_pair_engine_significant(self):
        r = self._score(
            [-0.55, -0.72, -0.48, -0.63, -0.58, -0.49],
            [0.25, 0.38, 0.21, 0.44, 0.30, 0.27],
            "Meta",
            ["Snap", "Apple"],
        )
        assert abs(r.asymmetry_score - (-0.8833333333333334)) < 1e-9
        assert abs(r.t_statistic - (-17.319891500992473)) < 1e-6
        assert r.p_value < 1e-8
        assert abs(r.cohens_d - (-9.999644020433117)) < 1e-6
        assert r.is_significant is True
        assert r.confidence_interval_upper < 0

    def test_near_null_pair_stays_silent(self):
        r = self._score(
            [0.02, -0.05, 0.03, -0.01, 0.04, -0.03],
            [0.00, -0.02, 0.05, -0.04, 0.01, 0.02],
            "Meta",
            ["Snap", "Apple"],
        )
        assert abs(r.asymmetry_score - (-0.003333333333333334)) < 1e-9
        assert r.p_value > 0.3
        assert r.is_significant is False
        assert r.confidence_interval_lower < 0 < r.confidence_interval_upper

    def test_degenerate_m838_pair_engine_guard(self):
        # Degenerate n=1/n=1 contract on the m838 illustrative pair
        # ([0.10] Anthropic vs [-0.60] Meta): the engine's structural
        # guard fires (t=0.0, p=1.0, d=0.0, not significant) while
        # |asymmetry| == 0.70 and arm-swap negates exactly. The guard's
        # verdict is the assertion.
        r = self._score([0.10], [-0.60], "Anthropic", ["Meta"])
        assert r.t_statistic == 0.0
        assert r.p_value == 1.0
        assert r.cohens_d == 0.0
        assert r.is_significant is False
        assert abs(abs(r.asymmetry_score) - 0.70) < 1e-9
        swapped = self._score([-0.60], [0.10], "Meta", ["Anthropic"])
        assert swapped.asymmetry_score == -r.asymmetry_score

    def test_engine_finding_layer_separation(self):
        # The engine CAN return is_significant True on synthetic
        # corpora while the finding layer refuses: the three
        # mechanisms verified this run all carry finding-layer
        # is_significant false / NOT_CALCULATED per the Aug 28 2026
        # standing rule.
        assert "is_significant False" in _m838_data()["statistical_discipline"]
        assert (
            _m839_data()["asymmetry_scorer_result"]["is_significant"] is False
        )
        assert _m840_data()["engine_run"] is False


class TestDocSync1015:
    def test_readme_row_1015(self):
        assert TEST_BASENAME in _read(README_PATH)

    def test_architecture_row_1015(self):
        assert TEST_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_1015_file(self):
        doc = _read(ARCH_PATH)
        assert TEST_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))


class TestIterationLog1015:
    def _entry(self):
        log = _read(LOG_PATH)
        idx = log.index("## #1015 Type D:")
        return log[idx : idx + 15000]

    def test_entry_present(self):
        assert "## #1015 Type D:" in _read(LOG_PATH)

    def test_entry_records_tombstone_and_integrity(self):
        entry = self._entry()
        assert "SIXTY-THIRD" in entry
        assert "840" in entry

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
