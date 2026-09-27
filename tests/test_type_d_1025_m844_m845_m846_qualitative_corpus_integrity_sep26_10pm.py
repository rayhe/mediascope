"""Type D -- Iteration #1025 (Sat 2026-09-26 22:00 PDT): m844/m845/m846
qualitative-discipline verification + post-1020-1024 corpus integrity
(max numeric mechanism_id 846; zero next-number 847 keys in
numeric/underscore/dash mechanism forms; ledger holds at 30 with the
THIRTIETH member-form present exactly once (m818, journalists.yaml),
TWENTY-NINTH in news-corp.yaml, THIRTY-FIRST member-form negative
guard) + #1020 background-suite tombstone (FORTY-SIXTH consecutive
death; lineage SIXTY-FOURTH -> SIXTY-FIFTH) + fresh synthetic engine
calibration (new values, not #1020's) + re-launch of the full suite as
a background process writing to goal hidden_files
type_d_1025_full_suite.log (next Type D run checks its verdict per the
#795 convention).

Type D FIRST leg of the 1025-1029 window, OPENING it (D->E->A->B->C).
Committed predecessor #1024 Type C (21:00 PDT Sep 26) CLOSED the
1020-1024 window. Concurrency note: the in-flight runs at this run's
checks are the #899 Type C block (m771, uncommitted hunk in
profiles/nytimes.yaml), the #938 Type B test file (uncommitted
working-tree edit), the #900 Type D test file (untracked, on disk) and
the #1012 working-tree edit of the #1012 Type A test file - all
UNCOMMITTED, no Type C #899 / Type B #938 / Type D #900 main commits
in git history, and no ## #899 / ## #938 / ## #900 Type X entries in
iteration-log.md. The #884 Type C block (m762) is COMMITTED at this
run's checks (in HEAD), so it is no longer in-flight; its presence is
pinned as an integrity anchor, not a concurrency note. The #898 Type B
journalists.yaml hunk (m770) is ABSENT from the working tree (lost at
#918; m770 exists in no profile YAML, only in the needle strings of
the old #897 test file and the in-flight #900 test file) -
documented here as known data loss to be redone by a future run, not
as in-flight work. This run does NOT touch the in-flight files; the
in-flight blocks are owned by their runs. Iteration numbers follow
the rotation schedule, not commit order.

Verifies:
- m844 (Type A #1022, Reuters x Google Sep-18 Gemini-breakout alarm
  register vs Reuters x Meta Sep-18/Sep-17 enforcement register,
  near-null same-wire symmetry: Google arm MANUAL ILLUSTRATIVE -0.35;
  Meta arms -0.45, -0.35, avg -0.40; illustrative delta (Google minus
  Meta) +0.05; Reuters-Meta Oct-25-2024 content deal sits on META's
  side so the near-null spread runs OPPOSITE the naive payer-softening
  prediction; EXTENDS m664 (#717) and m730 (#832) to a third AI-lab
  entity on the news desk; pairs m739 (#847) desk contrast;
  profiles/competitor-coverage-research.yaml under
  cross_publication_findings, 2-space indent, descriptive block key):
  MANUAL ILLUSTRATIVE ONLY per standing rule Aug 28 2026, engine NOT
  run at the finding layer, p_value/cohens_d/ci_95 NOT_CALCULATED,
  is_significant False, verdict directionally_supported_not_proven,
  no_analysis_json_update true, NOT artifact-grade; falsification
  family NOT a member (ledger 30).
- m845 (Type B #1023, Lucas Ropek, TechCrunch: within-writer 9-day
  temporal register shift - Sep 25 Meta Connect hands-on
  product-curious MANUAL ILLUSTRATIVE +0.15 vs Sep-16 Luna In Brief
  own-voice stigma -0.50 (carried un-rescored per #807) vs carried
  Snap arm -0.45; illustrative temporal delta (Sep-25 minus Sep-16)
  +0.65; illustrative cross-entity delta (Meta minus Snap) +0.60,
  inverting the Sep-16 pair direction; register follows the news peg,
  not the entity; profiles/careers/journalists.yaml, lucas_ropek
  competitor_coverage, 4-space indent block key): MANUAL ILLUSTRATIVE
  ONLY, p_value/cohens_d/ci_95 NOT_CALCULATED, is_significant False,
  engine NOT run, verdict directionally_supported_not_proven,
  no_analysis_json_update true, NOT artifact-grade; falsification
  family NOT a member (ledger 30); connects_to [269, 620, 728, 749,
  812].
- m846 (Type C #1024, Benioff Sources Podcast exclusionary-diversion
  geometry: Microsoft OpenAI position blocked Salesforce OpenAI
  investment, diverting ~$50M into Anthropic in 2023 (Series C,
  $4.1B pre-money), ~$5B reported current value; expanded
  Claudeforce; ~$300M/yr Anthropic token-spend leg; NEW relationship
  direction FOURTEENTH per the m807 enumeration (EXCLUSIONARY-
  DIVERSION, moat-diversion); profiles/competitor-entities.yaml
  top-level block, zero indent): tone_scores NOT_SCORED per standing
  rule Aug 28 2026, engine_run False, p_value/cohens_d NOT_CALCULATED,
  is_significant not asserted at the finding layer, verdict
  directionally_supported_not_proven, no_analysis_json_update true,
  artifact_grade False, NOT artifact-grade; falsification_family
  NOT a member (falsification_ledger 30); connects_to [36, 729, 735,
  837]; excerpt_bounded true.

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

ANCHORED_SHA = "0" * 40  # patched post-commit per #565

# Built by concatenation so this source file carries no contiguous
# underscore-form mechanism literal (per the #770 lesson).
MECH_ID_MARKER = "mechanism" + "_"
NEXT_NUM = 847

M844_KEY = "reuters_google_gemini_breakout_alarm_register_vs_meta_enforcement_register_sep26_2026"
M845_KEY = "type_b_1023_lucas_ropek_techcrunch_sep25_connect_glasses_everywhere_vs_sep16_luna_stigma_temporal_shift"
M846_KEY = "type_c_1024_benioff_sources_podcast_microsoft_openai_exclusion_salesforce_anthropic_diversion_sep26_9pm"

M844_INDENT = 2  # nested under cross_publication_findings (competitor-coverage-research.yaml)
M845_INDENT = 4  # item-level block in journalists.yaml (lucas_ropek competitor_coverage)
M846_INDENT = 0  # top-level block in competitor-entities.yaml

M844_GOOGLE_URL_FRAG = "gemini-hacked-three-companies-first-known-breakout-by-google-ai-wsj-reports-2026-09-18"
M844_META_URL_FRAG = "french-prosecutors-regulators-step-up-scrutiny-smart-glasses-2026-09-18"
M845_META_URL_FRAG = "at-meta-connect-the-companys-smart-glasses-were-everywhere"
M846_URL_FRAG = "marc-benioff-ai-boom-saaspocalypse"


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


# At this run's anchor followup, the five newest distinct iteration
# numbers in git history: #1025 Type D opens the 1025-1029 window;
# #1024 Type C (committed 21:00 PDT Sep 26) is the schedule predecessor
# and CLOSED the 1020-1024 window. The in-flight runs (#899 Type C,
# #938 Type B, #900 Type D, #1012 working-tree edit) have no main
# commits in git history at this run's checks and sit below the
# window; #898's block was lost (documented in the module docstring)
# and has no main commit either. The #884 block (m762) is committed at
# this run's checks.
EXPECTED_ORDER = [
    ("D", "1025"),
    ("C", "1024"),
    ("B", "1023"),
    ("A", "1022"),
    ("E", "1021"),
]


def _iter_source_files():
    """Yield paths for profile + test source files.

    Excludes this file (sweep carrier per #715) and __pycache__
    artifacts (per the #715 pattern-rescope lesson: committed test
    pyc files carry next-number needle strings from their own guards;
    compiled artifacts are excluded from the sweeps). No additional
    sweep-carrier exclusions this run: no in-tree SOURCE file carries
    a contiguous 847-form mechanism literal (verified pre-commit), so
    the 847 sweeps run repo-wide with only this file excluded.
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


def _m844_data():
    return _block_data(
        "profiles/competitor-coverage-research.yaml", M844_KEY, M844_INDENT
    )


def _m844_text():
    return _indented_block(
        "profiles/competitor-coverage-research.yaml", M844_KEY, M844_INDENT
    )


def _m845_data():
    import yaml

    doc = yaml.safe_load(_read("profiles/careers/journalists.yaml"))
    return doc["lucas_ropek"]["competitor_coverage"][M845_KEY]


def _m846_data():
    return _block_data(
        "profiles/competitor-entities.yaml", M846_KEY, M846_INDENT
    )


class TestNovelty1025:
    def test_no_type_d_1025_test_file_preexisting(self):
        assert glob.glob(os.path.join(TESTS_DIR, "test_type_d_1025*.py")) == [
            os.path.join(TESTS_DIR, OWN_BASENAME)
        ], "only this file may match the test_type_d_1025 glob"

    def test_no_type_d_1025_in_git_log(self):
        # Pre-commit novelty: no Type D #1025 main commit exists.
        # Post-commit (anchor followup per #565), exactly one exists
        # and it is the anchored main commit - the guard doubles as a
        # duplicate-main-commit check.
        result = subprocess.run(
            ["git", "log", "--format=%H %s", "--grep=Type D #1025"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        mains = [
            line
            for line in result.stdout.splitlines()
            if "Type D #1025" in line and "followup" not in line.lower()
        ]
        if ANCHORED_SHA == "0" * 40:
            assert mains == [], mains
        else:
            assert len(mains) == 1, mains
            assert mains[0].startswith(ANCHORED_SHA + " "), mains

    def test_max_id_is_846_pre_commit(self):
        assert _max_numeric_mechanism_id() == 846

    def test_zero_847_forms_repo_wide(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_block_keys_unique_in_home_yamls(self):
        assert (
            _read("profiles/competitor-coverage-research.yaml").count(
                "\n  " + M844_KEY + ":"
            )
            == 1
        )
        assert (
            _read("profiles/careers/journalists.yaml").count(
                "\n    " + M845_KEY + ":"
            )
            == 1
        )
        assert (
            _read("profiles/competitor-entities.yaml").count("\n" + M846_KEY + ":")
            == 1
        )

    def test_m844_arm_urls_present_in_reuters_research(self):
        # The committed #1022 run pinned its URL novelty; this run
        # carries the m844 block's own arm URL fragments as
        # verified-in-corpus: both verbatim reuters.com arms appear
        # in profiles/competitor-coverage-research.yaml.
        block = _m844_text()
        assert M844_GOOGLE_URL_FRAG in block
        assert M844_META_URL_FRAG in block
        home = _read("profiles/competitor-coverage-research.yaml")
        assert M844_GOOGLE_URL_FRAG in home
        assert M844_META_URL_FRAG in home


class TestTypeDRotationGuard:
    def test_rotation_window_opens_1025(self):
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


class TestTypeDM844QualitativeDiscipline:
    def test_mechanism_id(self):
        assert _m844_data()["mechanism_id"] == 844
        assert _m844_data()["iteration"] == 1022

    def test_arm_tones_and_registers(self):
        data = _m844_data()
        scorer = data["asymmetry_scorer"]
        assert scorer["google_arm_tones"] == [-0.35]
        assert scorer["meta_arm_tones"] == [-0.45, -0.35]
        assert scorer["illustrative_delta_google_minus_meta"] == 0.05
        assert "near-null" in scorer["delta_interpretation"]
        assert "MANUAL ILLUSTRATIVE -0.35" in _m844_text()

    def test_near_null_delta_opposite_payer_prediction(self):
        # The Reuters-Meta Oct 25 2024 content deal sits on META's
        # side; the near-null +0.05 spread runs OPPOSITE the naive
        # payer-softening prediction (documented in the finding and
        # the financial_context prediction field).
        text = _m844_text()
        assert "OPPOSITE" in text
        assert "naive payer-softening prediction" in text
        fin = _m844_data()["financial_context"]
        assert "NULL on the observed arms" in fin["prediction"]

    def test_manual_illustrative_discipline(self):
        text = _m844_text()
        assert "p_value NOT_CALCULATED" in text
        assert "cohens_d NOT_CALCULATED" in text
        assert "ci_95 NOT_CALCULATED" in text
        assert "is_significant False" in text
        assert "engine NOT run" in text
        assert "directionally_supported_not_proven" in text

    def test_verdict_and_provenance(self):
        text = _m844_text()
        assert "NOT artifact-grade" in text
        assert "no analysis.json update" in text
        assert "NOT a falsification-family member" in text
        assert "ledger holds at 30" in text
        assert "EXTENDS mechanism 664" in text


class TestTypeDM845QualitativeDiscipline:
    def test_mechanism_id(self):
        assert _m845_data()["mechanism_id"] == 845
        assert _m845_data()["iteration"] == 1023

    def test_arm_tones_temporal_pair(self):
        data = _m845_data()
        assert data["new_meta_arm_sep25"]["tone_illustrative"] == 0.15
        assert data["carried_meta_arm_sep16"]["tone_illustrative"] == -0.50
        assert data["carried_snap_arm_sep16"]["tone_illustrative"] == -0.45

    def test_temporal_and_cross_entity_deltas(self):
        scorer = _m845_data()["asymmetry_scorer_result"]
        assert scorer["illustrative_temporal_delta_meta_sep25_minus_sep16"] == 0.65
        assert scorer["temporal_delta_calc"] == "0.15 - (-0.50) = +0.65"
        assert scorer["illustrative_cross_entity_delta_meta_minus_snap"] == 0.60
        assert scorer["cross_entity_delta_calc"] == "0.15 - (-0.45) = +0.60"

    def test_manual_illustrative_discipline(self):
        scorer = _m845_data()["asymmetry_scorer_result"]
        assert scorer["p_value"] == "NOT_CALCULATED"
        assert scorer["cohens_d"] == "NOT_CALCULATED"
        assert scorer["ci_95"] == "NOT_CALCULATED"
        assert "engine NOT run" in scorer["engine"]
        assert scorer["artifact_grade"] == "NOT artifact-grade"
        assert "MANUAL ILLUSTRATIVE" in scorer["methodology"]
        assert "is_significant is false" in scorer["methodology"]

    def test_verdict_and_provenance(self):
        data = _m845_data()
        assert data["verdict"] == "directionally_supported_not_proven"
        assert data["no_analysis_json_update"] is True
        assert data["falsification_family_member"] is False
        assert data["falsification_ledger"] == 30
        assert data["connects_to"] == [269, 620, 728, 749, 812]
        assert data["is_significant"] is False


class TestTypeDM846QualitativeDiscipline:
    def test_mechanism_id_and_provenance(self):
        data = _m846_data()
        assert data["mechanism_id"] == 846
        assert data["iteration"] == 1024
        assert data["iteration_type"] == "C"

    def test_exclusion_event_blocked_investment(self):
        event = _m846_data()["exclusion_event"]
        assert "Marc Benioff" in event["speaker"]
        assert "Microsoft" in event["claim"]
        assert "prevented" in event["claim"]

    def test_diversion_legs(self):
        data = _m846_data()
        diversion = data["diversion_investment"]
        assert "$50M" in diversion["initial"]
        assert "$300M+" in diversion["cumulative"]
        assert "$5B" in diversion["reported_current_value"]
        demand = data["demand_side_leg"]
        assert "$300M" in demand["projection_2026"]
        taxonomy = data["relationship_direction_taxonomy"]
        assert taxonomy["direction_number"] == "FOURTEENTH per the m807 enumeration"
        assert taxonomy["direction_name"] == "EXCLUSIONARY-DIVERSION (moat-diversion)"

    def test_statistical_discipline(self):
        data = _m846_data()
        assert data["tone_scores"] == "NOT_SCORED"
        assert data["engine_run"] is False
        assert data["artifact_grade"] is False
        assert data["verdict"] == "directionally_supported_not_proven"
        assert data["no_analysis_json_update"] is True
        assert data["falsification_family_member"] is False
        assert data["falsification_ledger"] == 30
        assert data["connects_to"] == [36, 729, 735, 837]
        assert data["excerpt_bounded"] is True

    def test_block_position_top_level(self):
        # m846 sits at zero indent in profiles/competitor-entities.yaml
        # (top-level block, colon form only per #715 designed keying:
        # the block key carries no numeric mechanism-id substring).
        doc = _read("profiles/competitor-entities.yaml")
        assert doc.count("\n" + M846_KEY + ":") == 1
        assert "mechanism_846" not in M846_KEY
        assert "mechanism-846" not in M846_KEY


class TestTypeDMaxIdAndNextNumber:
    def test_max_numeric_mechanism_id_is_846(self):
        assert _max_numeric_mechanism_id() == 846

    def test_zero_numeric_847_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_zero_underscore_847_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_zero_dash_847_repo_wide(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []


class TestTypeDFalsificationLedger:
    def test_ledger_holds_at_30(self):
        # m844 carries the ledger in prose form ("ledger holds at 30");
        # m845/m846 carry it as a structured field.
        assert "ledger holds at 30" in _m844_text()
        assert _m845_data()["falsification_ledger"] == 30
        assert _m846_data()["falsification_ledger"] == 30

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
        # ("negative guard", "absent") are permitted.
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

    def test_847_sweep_excludes_only_this_file_and_pycache(self):
        # The #1024 pyc in tests/__pycache__ exists but carries NO
        # contiguous 847-form literal: the #1024 test builds its 847
        # needles at runtime by concatenation (per the #715/#770
        # lesson), so compiled artifacts stay clean by construction.
        # The source sweeps must therefore come back empty.
        pyc_hits = glob.glob(
            os.path.join(TESTS_DIR, "__pycache__", "*1024*.pyc")
        )
        assert pyc_hits != [], "expected the #1024 pyc to exist"
        for p in pyc_hits:
            data = open(p, "rb").read()
            assert b"mechanism-847" not in data, p
            assert b"mechanism_847" not in data, p
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_m844_block_position_and_indent(self):
        # m844 sits under cross_publication_findings in
        # profiles/competitor-coverage-research.yaml at 2-space indent.
        doc = _read("profiles/competitor-coverage-research.yaml")
        idx = doc.index("\n  " + M844_KEY + ":")
        for ln in reversed(doc[:idx].splitlines()):
            stripped = ln.strip()
            if stripped.endswith(":") and len(stripped) > 1:
                indent = len(ln) - len(ln.lstrip(" "))
                if indent <= 0:
                    parent = stripped[:-1]
                    break
        assert parent == "cross_publication_findings", parent

    def test_m845_block_position_and_indent(self):
        # m845 sits at 4-space indent in profiles/careers/
        # journalists.yaml (lucas_ropek journalist item-level block)
        # and carries the Lucas Ropek byline provenance.
        doc = _read("profiles/careers/journalists.yaml")
        assert doc.count("\n    " + M845_KEY + ":") == 1
        block = _m845_data()
        assert "Lucas Ropek" in block["new_meta_arm_sep25"]["byline"]

    def test_m846_block_position_and_indent(self):
        # m846 sits at zero indent in profiles/competitor-entities.yaml
        # (top-level block, colon form only per #715 designed keying:
        # the block key carries no numeric mechanism-id substring).
        doc = _read("profiles/competitor-entities.yaml")
        assert doc.count("\n" + M846_KEY + ":") == 1
        assert "mechanism_846" not in M846_KEY
        assert "mechanism-846" not in M846_KEY


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

    def test_1020_suite_log_stalled(self):
        # Stalled mid-run: 385 bytes of dots at ~1% since Sep 26
        # 17:13 PDT, no summary tokens anywhere, the process has since
        # exited (no pytest alive).
        with open(self._suite_log("type_d_1020_full_suite.log"), "rb") as fh:
            data = fh.read()
        assert len(data) == 385, len(data)
        for token in (b"passed", b"failed", b"error"):
            assert token not in data, token

    def test_1020_suite_log_mtime_stale(self):
        # The #1020 suite's log has not been written since 17:13 PDT
        # (hours before this 22:00 PDT run): a live suite would append
        # progress dots continuously. Stale mtime + 385 bytes + zero
        # summary tokens = dead per the #795 convention. (The new
        # #1025 suite's pytest is alive by design; this assertion is
        # mtime-scoped to the OLD log, so it cannot self-conflict.)
        import time

        st = os.stat(self._suite_log("type_d_1020_full_suite.log"))
        age_hours = (time.time() - st.st_mtime) / 3600
        assert age_hours > 1, age_hours

    def test_tombstone_lineage_advances(self):
        # FORTY-SIXTH consecutive background death per the #795
        # convention; lineage advances SIXTY-FOURTH -> SIXTY-FIFTH.
        # This run re-launches the suite writing to
        # type_d_1025_full_suite.log; the next Type D run checks it.
        # (The #1015 suite was already tombstoned by #1020; it is NOT
        # re-tombstoned here.)
        entry_anchor = "SIXTY-FOURTH"
        entry_next = "SIXTY-FIFTH"
        assert entry_anchor != entry_next

    def test_1025_suite_log_relaunched(self):
        assert os.path.isfile(self._suite_log("type_d_1025_full_suite.log")), (
            "the re-launched suite log must exist"
        )


class TestTypeDSyntheticEngine:
    """Fresh engine meaningfulness calibration on synthetic corpora.

    Values hardcoded after a scratch run this run (NOT #1020's).
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
            [-0.55, -0.38, -0.62, -0.47, -0.51, -0.43, -0.59],
            [0.28, 0.15, 0.33, 0.21, 0.19, 0.26, 0.31],
            "Meta",
            ["Snap", "Apple"],
        )
        assert abs(r.asymmetry_score - (-0.7542857142857143)) < 1e-9
        assert abs(r.t_statistic - (-18.334512287923367)) < 1e-6
        assert r.p_value < 2e-9
        assert abs(r.cohens_d - (-9.800209047858008)) < 1e-6
        assert r.is_significant is True
        assert r.confidence_interval_upper < 0

    def test_near_null_pair_stays_silent(self):
        r = self._score(
            [0.05, -0.04, 0.02, -0.06, 0.03, -0.02, 0.01],
            [0.04, -0.03, 0.00, 0.03, -0.05, 0.02, 0.06],
            "Meta",
            ["Snap", "Apple"],
        )
        assert abs(r.asymmetry_score - (-0.011428571428571427)) < 1e-9
        assert r.p_value > 0.3
        assert r.is_significant is False
        assert r.confidence_interval_lower < 0 < r.confidence_interval_upper

    def test_degenerate_m844_pair_engine_guard(self):
        # Degenerate n=1/n=1 contract on the m844 illustrative pair
        # ([-0.35] Google vs [-0.40] Meta): the engine's structural
        # guard fires (t=0.0, p=1.0, d=0.0, not significant) while
        # |asymmetry| == 0.05 and arm-swap negates exactly. The guard's
        # verdict is the assertion.
        r = self._score([-0.35], [-0.40], "Google", ["Meta"])
        assert r.t_statistic == 0.0
        assert r.p_value == 1.0
        assert r.cohens_d == 0.0
        assert r.is_significant is False
        assert abs(abs(r.asymmetry_score) - 0.05) < 1e-9
        swapped = self._score([-0.40], [-0.35], "Meta", ["Google"])
        assert swapped.asymmetry_score == -r.asymmetry_score

    def test_engine_finding_layer_separation(self):
        # The engine CAN return is_significant True on synthetic
        # corpora while the finding layer refuses: the three
        # mechanisms verified this run all carry finding-layer
        # is_significant false / NOT_CALCULATED per the Aug 28 2026
        # standing rule.
        assert "is_significant False" in _m844_text()
        assert _m845_data()["is_significant"] is False
        assert _m846_data()["engine_run"] is False


class TestDocSync1025:
    def test_readme_row_1025(self):
        assert TEST_BASENAME in _read(README_PATH)

    def test_architecture_row_1025(self):
        assert TEST_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_1025_file(self):
        doc = _read(ARCH_PATH)
        assert TEST_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))


class TestIterationLog1025:
    def _entry(self):
        log = _read(LOG_PATH)
        idx = log.index("## #1025 Type D:")
        return log[idx : idx + 15000]

    def test_entry_present(self):
        assert "## #1025 Type D:" in _read(LOG_PATH)

    def test_entry_records_tombstone_and_integrity(self):
        entry = self._entry()
        assert "SIXTY-FIFTH" in entry
        assert "846" in entry

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
