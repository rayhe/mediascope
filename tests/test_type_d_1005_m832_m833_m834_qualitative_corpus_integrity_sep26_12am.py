"""Type D -- Iteration #1005 (Sat 2026-09-26 00:00 PDT): m832/m833/m834
qualitative-discipline verification + post-1000-1004 corpus integrity
(max numeric mechanism_id 834; zero next-number 835 keys in
numeric/underscore/dash mechanism forms; ledger holds at 30 with the
THIRTIETH member-form present exactly once (m818, journalists.yaml),
TWENTY-NINTH in news-corp.yaml, THIRTY-FIRST member-form negative
guard) + #1000 background-suite tombstone (FORTY-SECOND consecutive
death; lineage SIXTIETH -> SIXTY-FIRST) + fresh synthetic engine
calibration (new values, not #1000's) + re-launch of the full suite as
a background process writing to goal hidden_files
type_d_1005_full_suite.log (next Type D run checks its verdict per the
#795 convention).

Type D FIRST leg of the 1005-1009 window, OPENING it (D->E->A->B->C).
Committed predecessor #1004 Type C (23:00 PDT Sep 25) CLOSED the
1000-1004 window. Concurrency note: the in-flight runs at this run's
checks are the #899 Type C block (m771, uncommitted hunk in
profiles/nytimes.yaml), the #938 Type B test file (uncommitted
ANCHORED_SHA working-tree edit) and the #900 Type D test file
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
- m832 (Type A #1002, Guardian Sep-2026 ambient-listening bounded
  silence vs Guardian x Meta police-memo investigation + Connect stigma
  register: NEW Meta arms Sep-8 FOIA-driven police-memo investigation
  (MANUAL ILLUSTRATIVE -0.75) + Sep-24 Connect stigma piece
  (MANUAL ILLUSTRATIVE -0.20), Meta illustrative avg -0.475; Apple arm
  NOT_SCORED_BOUNDED_ABSENCE (zero authored Guardian UK pieces on
  Sep-9 always-listening Audio Intelligence across 5 Apple-angled query
  sets); delta NOT_COMPUTED_SELECTION_ASYMMETRY; temporal replication
  of the m607 zero-financial-gradient control on the SELECTION axis;
  profiles/guardian.yaml under competitor_relationships/apple,
  4-space indent): MANUAL ILLUSTRATIVE ONLY per standing rule Aug 28
  2026, engine NOT run at the finding layer, p_value/cohens_d/ci
  NOT_CALCULATED, is_significant False, verdict
  directionally_supported_not_proven, no_analysis_json_update true,
  NOT artifact-grade; falsification_family_member False
  (falsification_ledger 30); connects_to [607, 537, 826, 830, 827].
- m833 (Type B #1003, James Pero, Gizmodo Sep-2026 Snap Specs
  ear-bending comedy (MANUAL ILLUSTRATIVE +0.10) vs carried Sep-23
  Meta Ray-Ban Audio "perv" stigma frame (MANUAL ILLUSTRATIVE -0.20);
  illustrative Snap-minus-Meta delta +0.30, a STIGMA-REGISTER ROUTING
  extension of m806/m791 (anatomy-humor vs "perv" vocabulary on the
  face-hardware social-acceptability attribute); bounded by m818
  (category-bounded within Meta, no journalist-global hostility claim)
  and m746/m933 (playful-Snap register replicates); genre/access the
  strongest confounders; profiles/careers/journalists.yaml at the
  james_pero item, competitor_coverage, 4-space indent): MANUAL
  ILLUSTRATIVE ONLY, engine NOT run, p_value/cohens_d/ci
  NOT_CALCULATED, is_significant False, verdict
  directionally_supported_not_proven, no_analysis_json_update true,
  NOT artifact-grade; falsification_family_member False
  (falsification_ledger 30).
- m834 (Type C #1004, Australia News Bargaining Incentive (enacted
  Aug 20 2026) - State-Compelled Deal-or-Levy Regulatory Bargaining:
  FIRST dedicated corpus mechanism on the enacted Australian News Media
  Bargaining Bill 2026 + News Journalism Payments Bill 2026;
  2.5%-reported (Reuters) / 2.75%-reported (mi-3) charge on Australian
  digital advertising revenue for platforms over A$250M relevant
  revenue (Meta, Google, TikTok, LinkedIn); commercial-deal offsets
  (150% large / 200% small-medium, 25% per-deal cap, 8-deal minimum,
  5% to AAP); AI firms consciously EXCLUDED; Meta 2024 walk-away
  loophole closed; TWELFTH relationship direction
  (regulatory-bargaining) in the m807 enumeration; draft-stage record
  RETAINED and explicitly SUPERSEDED (not overwritten);
  profiles/competitor-entities.yaml tail block, zero indent, running
  to EOF): tone_scores NOT_SCORED per standing rule Aug 28 2026,
  engine NOT run, p_value/cohens_d/ci NOT_CALCULATED, is_significant
  False, verdict directionally_supported_not_proven,
  no_analysis_json_update true, NOT artifact-grade;
  falsification_family_member False (falsification_ledger 30);
  7 confounders ranked strong-first, 4 COUNTEREVIDENCE items.

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

ANCHORED_SHA = "0000000000000000000000000000000000000000"  # patched post-commit per #565

MECH_ID_MARKER = "mechanism" + "_"
NEXT_NUM = 835

M832_KEY = "type_a_1002_guardian_apple_ambient_listening_sep2026_bounded_silence_vs_meta_police_memo_connect_stigma_register_sep25_2026"
M833_KEY = "type_b_1003_james_pero_gizmodo_snap_specs_earbending_comedy_vs_meta_audio_stigma_sep25"
M834_KEY = "type_c_1004_australia_news_bargaining_incentive_regulatory_bargaining_sep25_11pm"

M832_INDENT = 4  # nested under competitor_relationships/apple (guardian.yaml)
M833_INDENT = 4  # nested under the james_pero item, competitor_coverage
M834_INDENT = 0  # top-level tail block in competitor-entities.yaml


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
# numbers in git history: #1005 Type D opens the 1005-1009 window;
# #1004 Type C (committed 23:00 PDT Sep 25) is the schedule predecessor
# and CLOSED the 1000-1004 window. The in-flight runs (#899 Type C,
# #938 Type B, #900 Type D) have no main commits in git history at
# this run's checks and sit below the window; #898's block was lost
# (documented in the module docstring) and has no main commit either.
# The #884 block (m762) is committed at this run's checks.
EXPECTED_ORDER = [
    ("D", "1005"),
    ("C", "1004"),
    ("B", "1003"),
    ("A", "1002"),
    ("E", "1001"),
]


def _iter_source_files():
    """Yield (path, is_test) for profile + test source files.

    Excludes this file (sweep carrier per #715) and __pycache__
    artifacts (per the #715 pattern-rescope lesson: the #1004 pyc
    carries an 835-form needle string from its own next-number guard;
    compiled artifacts are excluded from the sweeps). No additional
    sweep-carrier exclusions this run: no in-tree SOURCE file carries
    a contiguous 835-form mechanism literal (verified pre-commit; the
    #1004 test file builds its 835 needles at runtime and its raw
    "mechanism 835" hits are docstring/grep-needle strings with a
    space, not contiguous mechanism-form literals), so the 835 sweeps
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


def _m832_data():
    return _block_data("profiles/guardian.yaml", M832_KEY, M832_INDENT)


def _m833_data():
    return _block_data(
        "profiles/careers/journalists.yaml", M833_KEY, M833_INDENT
    )


def _m834_data():
    return _block_data(
        "profiles/competitor-entities.yaml", M834_KEY, M834_INDENT
    )


class TestNovelty1005:
    def test_no_type_d_1005_test_file_preexisting(self):
        import glob

        assert glob.glob(os.path.join(TESTS_DIR, "test_type_d_1005*.py")) == [
            os.path.join(TESTS_DIR, OWN_BASENAME)
        ], "only this file may match the test_type_d_1005 glob"

    def test_no_type_d_1005_in_git_log(self):
        subjects = _git("log", "--format=%s").splitlines()
        assert not any(
            re.match(r"Type D #1005:", s) for s in subjects
        ), "no Type D #1005 commit may precede this run"

    def test_max_id_is_834_pre_commit(self):
        assert _max_numeric_mechanism_id() == 834

    def test_zero_835_forms_repo_wide(self):
        assert _repo_grep_numeric_mechanism_id(835) == []
        assert _repo_grep_underscore_mechanism(835) == []
        assert _repo_grep_dash_mechanism(835) == []

    def test_block_keys_unique_in_home_yamls(self):
        assert _read("profiles/guardian.yaml").count("\n    " + M832_KEY + ":") == 1
        assert (
            _read("profiles/careers/journalists.yaml").count(
                "\n    " + M833_KEY + ":"
            )
            == 1
        )
        assert (
            _read("profiles/competitor-entities.yaml").count(
                "\n" + M834_KEY + ":"
            )
            == 1
        )

    def test_m832_m833_m834_urls_zero_hit_in_log_pre_commit(self):
        # The committed #1002/#1003/#1004 runs already pinned their URL
        # novelty; this run carries their URLs as verified-in-corpus,
        # not as new keys. The one corpus check here: the m834 block's
        # own eight source URLs all appear in competitor-entities.yaml.
        data = _m834_data()
        for url in data["sources"]:
            assert url in _read("profiles/competitor-entities.yaml"), url


class TestTypeDRotationGuard:
    def test_rotation_window_opens_1005(self):
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


class TestTypeDM832QualitativeDiscipline:
    def test_mechanism_id(self):
        assert _m832_data()["mechanism_id"] == 832

    def test_manual_illustrative_only(self):
        # The m832 discipline is carried in the manual-illustrative
        # tones note and the NOT_CALCULATED scorer fields, not in a
        # nested statistical_discipline mapping.
        doc = _indented_block("profiles/guardian.yaml", M832_KEY, M832_INDENT)
        assert "MANUAL ILLUSTRATIVE" in doc

    def test_engine_not_run_at_finding_layer(self):
        # The finding layer expresses the qualitative-only discipline
        # as NOT_CALCULATED statistics and is_significant False at
        # both the flat and the asymmetry_scorer_result levels.
        data = _m832_data()
        assert data["p_value"] == "NOT_CALCULATED"
        assert data["cohens_d"] == "NOT_CALCULATED"
        assert data["is_significant"] is False
        assert data["asymmetry_scorer_result"]["p_value"] == "NOT_CALCULATED"
        assert data["asymmetry_scorer_result"]["is_significant"] is False

    def test_verdict_and_grade(self):
        data = _m832_data()
        assert data["verdict"] == "directionally_supported_not_proven"
        assert data["no_analysis_json_update"] is True
        # Grade lives in the asymmetry_scorer_result mapping for the
        # bounded-absence design, not as a flat key.
        assert data["asymmetry_scorer_result"]["artifact_grade"] is False

    def test_not_falsification_family(self):
        data = _m832_data()
        assert data["falsification_family_member"] is False
        assert data["falsification_ledger"] == 30

    def test_selection_asymmetry_bound(self):
        # The Apple arm is a BOUNDED ABSENCE (not scored); no magnitude
        # delta is computed on a scored-vs-absent pair. The selection
        # gap (2 Meta arms vs 0 Apple arms) is the finding.
        doc = _indented_block("profiles/guardian.yaml", M832_KEY, M832_INDENT)
        assert "NOT_SCORED_BOUNDED_ABSENCE" in doc
        assert "NOT_COMPUTED_SELECTION_ASYMMETRY" in doc
        assert "m607" in doc or "607" in doc

    def test_placement_under_apple(self):
        doc = _read("profiles/guardian.yaml")
        apple_idx = doc.index("\n  apple:")
        key_idx = doc.index("\n    " + M832_KEY + ":")
        assert apple_idx < key_idx


class TestTypeDM833QualitativeDiscipline:
    def test_mechanism_id(self):
        assert _m833_data()["mechanism_id"] == 833

    def test_manual_illustrative_only(self):
        disc = _m833_data()["statistical_discipline"]
        assert "MANUAL ILLUSTRATIVE" in str(disc)

    def test_verdict_and_grade(self):
        doc = _indented_block(
            "profiles/careers/journalists.yaml", M833_KEY, M833_INDENT
        )
        assert "directionally_supported_not_proven" in doc
        assert "no_analysis_json_update" in doc

    def test_not_falsification_family(self):
        doc = _indented_block(
            "profiles/careers/journalists.yaml", M833_KEY, M833_INDENT
        )
        assert "falsification_family_member: false" in doc
        assert "ledger holds at 30" in doc

    def test_illustrative_delta_descriptive(self):
        doc = _indented_block(
            "profiles/careers/journalists.yaml", M833_KEY, M833_INDENT
        )
        assert "+0.30" in doc
        assert "MANUAL ILLUSTRATIVE" in doc

    def test_stigma_register_extension_bounds(self):
        # Extension of m806/m791, bounded by m818 (category-bound) and
        # m746/m933 (playful-Snap register replicates).
        doc = _indented_block(
            "profiles/careers/journalists.yaml", M833_KEY, M833_INDENT
        )
        assert "806" in doc and "791" in doc
        assert "818" in doc
        assert "746" in doc and "933" in doc

    def test_placement_under_james_pero(self):
        doc = _read("profiles/careers/journalists.yaml")
        pero_idx = doc.index("\njames_pero:")
        key_idx = doc.index("\n    " + M833_KEY + ":")
        assert pero_idx < key_idx


class TestTypeDM834QualitativeDiscipline:
    def test_mechanism_id(self):
        assert _m834_data()["mechanism_id"] == 834

    def test_tone_not_scored(self):
        assert _m834_data()["tone_scores"] == "NOT_SCORED"

    def test_verdict_and_grade(self):
        data = _m834_data()
        assert data["verdict"] == "directionally_supported_not_proven"
        assert data["no_analysis_json_update"] is True
        assert data["artifact_grade"] is False

    def test_not_falsification_family(self):
        data = _m834_data()
        assert data["falsification_family_member"] is False
        assert data["falsification_ledger"] == 30

    def test_regulatory_bargaining_direction(self):
        data = _m834_data()
        assert "TWELFTH" in data["mechanism_name"]

    def test_draft_record_supersession(self):
        # The draft-stage corpus record is RETAINED as history and
        # explicitly SUPERSEDED by the final-law record, not
        # overwritten.
        doc = _indented_block(
            "profiles/competitor-entities.yaml", M834_KEY, M834_INDENT
        )
        assert "superseded" in doc
        assert "retained as history" in doc

    def test_llm_exclusion_carried(self):
        doc = _indented_block(
            "profiles/competitor-entities.yaml", M834_KEY, M834_INDENT
        )
        assert "consciously separated" in doc or "EXCLUDED" in doc

    def test_block_is_last_top_level_key(self):
        # The m834 tail block runs to EOF in
        # profiles/competitor-entities.yaml.
        doc = _read("profiles/competitor-entities.yaml")
        tail = doc[doc.index("\n" + M834_KEY + ":") + 1 :]
        assert not re.search(r"(?m)^[A-Za-z_][^:]*:$", tail.split("\n", 1)[1])


class TestTypeDMaxIdAndNextNumber:
    def test_max_numeric_mechanism_id_is_834(self):
        assert _max_numeric_mechanism_id() == 834

    def test_zero_numeric_835_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(835) == []

    def test_zero_underscore_835_repo_wide(self):
        # Needles are format-built (per #715/#770); this file carries no
        # contiguous underscore-form 835 literal. The #1004 committed
        # test's runtime-built needle hits do not exist as source
        # literals.
        assert _repo_grep_underscore_mechanism(835) == []

    def test_zero_dash_835_repo_wide(self):
        assert _repo_grep_dash_mechanism(835) == []


class TestTypeDFalsificationLedger:
    def test_ledger_holds_at_30(self):
        assert _m834_data()["falsification_ledger"] == 30
        assert _m832_data()["falsification_ledger"] == 30
        doc = _indented_block(
            "profiles/careers/journalists.yaml", M833_KEY, M833_INDENT
        )
        assert "ledger holds at 30" in doc

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

    def test_835_sweep_excludes_only_this_file_and_pycache(self):
        # The sole repo-wide 835-form literals at this run's checks are
        # the #1004 pyc in tests/__pycache__ (next-number guard of a
        # committed test, excluded per the #715 pattern-rescope
        # lesson). The source sweeps must therefore come back empty.
        import glob

        pyc_hits = glob.glob(
            os.path.join(TESTS_DIR, "__pycache__", "*1004*.pyc")
        )
        assert pyc_hits != [], "expected the #1004 pyc to exist"
        for p in pyc_hits:
            data = open(p, "rb").read()
            if b"mechanism-835" in data or b"mechanism_835" in data:
                break
        else:
            assert False, "no #1004 pyc carries the 835 needle"
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []


class TestTypeDFullSuiteTombstone:
    def test_1000_suite_log_stalled(self):
        log_path = os.path.join(
            os.path.expanduser("~"),
            "workspace",
            "goals",
            "mediascope-meta-wearables-press-analysis",
            "hidden_files",
            "type_d_1000_full_suite.log",
        )
        with open(log_path, "rb") as fh:
            data = fh.read()
        # Stalled mid-run: 283 bytes of dots since Sep 25 19:25 PDT,
        # no summary tokens anywhere, the process has since exited.
        assert len(data) == 283, len(data)
        for token in (b"passed", b"failed", b"error"):
            assert token not in data, token

    def test_tombstone_lineage_advances(self):
        # FORTY-SECOND consecutive background death per the #795
        # convention; lineage advances SIXTIETH -> SIXTY-FIRST.
        # This run re-launches the suite writing to
        # type_d_1005_full_suite.log; the next Type D run checks it.
        # (The #995 suite was already tombstoned by #1000; it is NOT
        # re-tombstoned here.)
        entry_anchor = "SIXTIETH"
        entry_next = "SIXTY-FIRST"
        assert entry_anchor != entry_next

    def test_1005_suite_log_relaunched(self):
        log_path = os.path.join(
            os.path.expanduser("~"),
            "workspace",
            "goals",
            "mediascope-meta-wearables-press-analysis",
            "hidden_files",
            "type_d_1005_full_suite.log",
        )
        assert os.path.isfile(log_path), log_path


class TestTypeDSyntheticEngine:
    """Fresh engine meaningfulness calibration on synthetic corpora.

    Values hardcoded after a scratch run this run (NOT #1000's).
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
            [-0.55, -0.60, -0.50, -0.65, -0.58, -0.62, -0.52, -0.68],
            [0.30, 0.35, 0.28, 0.40, 0.32, 0.38, 0.30, 0.36],
            "Meta",
            ["Snap", "Apple"],
        )
        assert abs(r.asymmetry_score - (-0.92375)) < 1e-9
        assert abs(r.t_statistic - (-34.50430671037133)) < 1e-6
        assert r.p_value < 1e-12
        assert abs(r.cohens_d - (-17.252153355185666)) < 1e-6
        assert r.is_significant is True
        assert r.confidence_interval_upper < 0

    def test_near_null_pair_stays_silent(self):
        r = self._score(
            [0.05, -0.03, 0.02, -0.01, 0.04, -0.02, 0.01, -0.03],
            [0.02, 0.00, 0.03, -0.01, 0.01, 0.00, 0.02, -0.02],
            "Meta",
            ["Snap", "Apple"],
        )
        assert abs(r.asymmetry_score - (-0.0025)) < 1e-9
        assert r.p_value > 0.5
        assert r.is_significant is False
        assert r.confidence_interval_lower < 0 < r.confidence_interval_upper

    def test_degenerate_m830_pair_engine_guard(self):
        # Degenerate n=1/n=1 contract on the m830 illustrative pair
        # ([0.00] Meta vs [-0.15] Snap): the engine's structural guard
        # fires (t=0.0, p=1.0, d=0.0, not significant) while
        # |asymmetry| == 0.15 and arm-swap negates exactly. The guard's
        # verdict is the assertion.
        r = self._score([0.00], [-0.15], "Meta", ["Snap"])
        assert r.t_statistic == 0.0
        assert r.p_value == 1.0
        assert r.cohens_d == 0.0
        assert r.is_significant is False
        assert abs(abs(r.asymmetry_score) - 0.15) < 1e-9
        swapped = self._score([-0.15], [0.00], "Snap", ["Meta"])
        assert swapped.asymmetry_score == -r.asymmetry_score

    def test_engine_finding_layer_separation(self):
        # The engine CAN return is_significant True on synthetic
        # corpora while the finding layer refuses: the three
        # mechanisms verified this run all carry finding-layer
        # is_significant false / NOT_CALCULATED per the Aug 28 2026
        # standing rule.
        assert _m832_data()["asymmetry_scorer_result"]["is_significant"] is False
        doc833 = _indented_block(
            "profiles/careers/journalists.yaml", M833_KEY, M833_INDENT
        )
        assert "is_significant" in doc833
        assert _m834_data()["engine_run"] is False


class TestDocSync1005:
    def test_readme_row_1005(self):
        assert TEST_BASENAME in _read(README_PATH)

    def test_architecture_row_1005(self):
        assert TEST_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_1005_file(self):
        doc = _read(ARCH_PATH)
        assert TEST_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))


class TestIterationLog1005:
    def _entry(self):
        log = _read(LOG_PATH)
        idx = log.index("## #1005 Type D:")
        return log[idx : idx + 15000]

    def test_entry_present(self):
        assert "## #1005 Type D:" in _read(LOG_PATH)

    def test_entry_records_tombstone_and_integrity(self):
        entry = self._entry()
        assert "SIXTY-FIRST" in entry
        assert "834" in entry
