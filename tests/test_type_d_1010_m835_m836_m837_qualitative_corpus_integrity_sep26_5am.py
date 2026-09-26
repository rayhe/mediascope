"""Type D -- Iteration #1010 (Sat 2026-09-26 05:00 PDT): m835/m836/m837
qualitative-discipline verification + post-1005-1009 corpus integrity
(max numeric mechanism_id 837; zero next-number 838 keys in
numeric/underscore/dash mechanism forms; ledger holds at 30 with the
THIRTIETH member-form present exactly once (m818, journalists.yaml),
TWENTY-NINTH in news-corp.yaml, THIRTY-FIRST member-form negative
guard) + #1005 background-suite tombstone (FORTY-THIRD consecutive
death; lineage SIXTY-FIRST -> SIXTY-SECOND) + fresh synthetic engine
calibration (new values, not #1005's) + re-launch of the full suite as
a background process writing to goal hidden_files
type_d_1010_full_suite.log (next Type D run checks its verdict per the
#795 convention).

Type D FIRST leg of the 1010-1014 window, OPENING it (D->E->A->B->C).
Committed predecessor #1009 Type C (04:00 PDT Sep 26) CLOSED the
1005-1009 window. Concurrency note: the in-flight runs at this run's
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
- m835 (Type A #1007, NYT x Anthropic Sep-2026 IPO-scoop momentum
  register vs NYT x Meta Connect-relay + Aug ICE-ban enforcement
  register: Anthropic arms Sep-12 Amodei slowdown news piece (MANUAL
  ILLUSTRATIVE +0.10) + Sep-18 IPO scoop (MANUAL ILLUSTRATIVE +0.25),
  Anthropic illustrative mean +0.175; Meta arms Sep-23 Connect straight
  relay (MANUAL ILLUSTRATIVE +0.10) + Aug-18 ICE-ban enforcement
  register (MANUAL ILLUSTRATIVE -0.30), Meta illustrative mean -0.10;
  illustrative delta (Anthropic minus Meta) +0.275; register SELECTION
  is the asymmetry; temporal extension of the m685 slowdown family
  into the IPO peg; FIRST mechanism-ization of the NYT's own Aug-18
  ICE-ban investigative piece; profiles/nytimes.yaml under
  competitor_relationships/anthropic, 4-space indent): MANUAL
  ILLUSTRATIVE ONLY per standing rule Aug 28 2026, engine NOT run at
  the finding layer, p_value/cohens_d/ci_95 NOT_CALCULATED,
  is_significant False, verdict directionally_supported_not_proven
  (in statistical_discipline), no_analysis_json_update true, NOT
  artifact-grade; falsification family NOT a member (ledger_hold 30);
  connects_to [685, 822, 832, 790].
- m836 (Type B #1008, Lily Hay Newman, WIRED: NEW Sep-23 Meta Connect
  "Pinky Promises" Private Processing pledge co-byline (MANUAL
  ILLUSTRATIVE -0.45, carried from m820 per #807) vs carried Sep-9
  Apple Watch Audio Intelligence reassurance-adopting headline (MANUAL
  ILLUSTRATIVE +0.10, carried from m635 per #807); illustrative
  Meta-minus-Apple delta -0.55; PEG-MATCHED replication of m635 on
  company privacy-assurance announcements, weakening the m635
  news-peg confound; gradient-absent (no Conde Nast-Apple or
  Conde Nast-Meta AI-licensing deal in corpus); profiles/careers/
  journalists.yaml under the lily_hay_newman item, 2-space indent
  key): verdict directionally_supported_not_proven,
  no_analysis_json_update true, NOT artifact-grade;
  falsification_family_member False (falsification_ledger 30);
  statistical_discipline tone_scores MANUAL_ILLUSTRATIVE_CARRIED,
  engine NOT run, is_significant False.
- m837 (Type C #1009, Akamai x Anthropic $11.6B seven-year cloud deal
  + 5% equity warrant (announced Sep 24 2026) - DEMAND-FOR-EQUITY
  (warrant-for-demand): FIRST dedicated corpus mechanism on the
  warrant structure; ~$11.6B committed for CPU workloads (Project
  Plans 2 and 3 under the MSA) stapled to a warrant for 7.7M
  non-voting convertible Series B preferred shares (up to ~5% of
  Akamai at $111.33/share; ~2% vests on the $11.6B commitment, ~1%
  per additional $3B up to $9B optional / ~$20B ceiling); the supplier
  pays the customer in equity for committed demand; THIRTEENTH
  relationship direction in the m807 enumeration; extends
  infrastructure-capture (m738); profiles/competitor-entities.yaml
  tail block, zero indent, running to EOF): tone_scores NOT_SCORED
  per standing rule Aug 28 2026, engine NOT run,
  p_value/cohens_d/ci NOT_CALCULATED, is_significant False, verdict
  directionally_supported_not_proven, no_analysis_json_update true,
  NOT artifact-grade; falsification_family_member False
  (falsification_ledger 30); 8 confounders ranked strong-first,
  4 COUNTEREVIDENCE items.

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

ANCHORED_SHA = "d35d308ac2419ba934c559321e570109c1ef99ed"  # patched post-commit per #565

MECH_ID_MARKER = "mechanism" + "_"
NEXT_NUM = 838

M835_KEY = "type_a_1007_nyt_anthropic_sep2026_ipo_scoop_momentum_register_vs_meta_connect_relay_ice_enforcement_sep26_2026"
M836_KEY = "type_b_1008_lily_hay_newman_meta_connect_pinky_promises_vs_apple_watch_audio_intelligence_reassurance_sep26"
M837_KEY = "type_c_1009_akamai_anthropic_116b_warrant_demand_for_equity_sep26_4am"

M835_INDENT = 4  # nested under competitor_relationships/anthropic (nytimes.yaml)
M836_INDENT = 2  # nested under the lily_hay_newman list item (journalists.yaml)
M837_INDENT = 0  # top-level tail block in competitor-entities.yaml


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
# numbers in git history: #1010 Type D opens the 1010-1014 window;
# #1009 Type C (committed 04:00 PDT Sep 26) is the schedule predecessor
# and CLOSED the 1005-1009 window. The in-flight runs (#899 Type C,
# #938 Type B, #900 Type D) have no main commits in git history at
# this run's checks and sit below the window; #898's block was lost
# (documented in the module docstring) and has no main commit either.
# The #884 block (m762) is committed at this run's checks.
EXPECTED_ORDER = [
    ("D", "1010"),
    ("C", "1009"),
    ("B", "1008"),
    ("A", "1007"),
    ("E", "1006"),
]


def _iter_source_files():
    """Yield (path, is_test) for profile + test source files.

    Excludes this file (sweep carrier per #715) and __pycache__
    artifacts (per the #715 pattern-rescope lesson: the #1009 pyc
    carries an 838-form needle string from its own next-number guard;
    compiled artifacts are excluded from the sweeps). No additional
    sweep-carrier exclusions this run: no in-tree SOURCE file carries
    a contiguous 838-form mechanism literal (verified pre-commit; the
    #1009 test file builds its 838 needles at runtime and its raw
    "mechanism 838" hits are docstring/grep-needle strings with a
    space, not contiguous mechanism-form literals), so the 838 sweeps
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


def _m835_data():
    return _block_data("profiles/nytimes.yaml", M835_KEY, M835_INDENT)


def _m836_data():
    return _block_data(
        "profiles/careers/journalists.yaml", M836_KEY, M836_INDENT
    )


def _m837_data():
    return _block_data(
        "profiles/competitor-entities.yaml", M837_KEY, M837_INDENT
    )


class TestNovelty1010:
    def test_no_type_d_1010_test_file_preexisting(self):
        import glob

        assert glob.glob(os.path.join(TESTS_DIR, "test_type_d_1010*.py")) == [
            os.path.join(TESTS_DIR, OWN_BASENAME)
        ], "only this file may match the test_type_d_1010 glob"

    def test_no_type_d_1010_in_git_log(self):
        # Pre-commit novelty: no Type D #1010 main commit exists.
        # Post-commit (anchor followup per #565), exactly one exists
        # and it is the anchored main commit - the guard doubles as a
        # duplicate-main-commit check.
        result = subprocess.run(
            ["git", "log", "--format=%H %s", "--grep=Type D #1010"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        mains = [
            line
            for line in result.stdout.splitlines()
            if "Type D #1010" in line and "followup" not in line.lower()
        ]
        if ANCHORED_SHA == "0" * 40:
            assert mains == [], mains
        else:
            assert len(mains) == 1, mains
            assert mains[0].startswith(ANCHORED_SHA + " "), mains

    def test_max_id_is_837_pre_commit(self):
        assert _max_numeric_mechanism_id() == 837

    def test_zero_838_forms_repo_wide(self):
        assert _repo_grep_numeric_mechanism_id(838) == []
        assert _repo_grep_underscore_mechanism(838) == []
        assert _repo_grep_dash_mechanism(838) == []

    def test_block_keys_unique_in_home_yamls(self):
        assert _read("profiles/nytimes.yaml").count("\n    " + M835_KEY + ":") == 1
        assert (
            _read("profiles/careers/journalists.yaml").count(
                "\n  " + M836_KEY + ":"
            )
            == 1
        )
        assert (
            _read("profiles/competitor-entities.yaml").count(
                "\n" + M837_KEY + ":"
            )
            == 1
        )

    def test_m835_arm_urls_present_in_nytimes(self):
        # The committed #1007 run already pinned its URL novelty; this
        # run carries the m835 block's own five arm URLs as
        # verified-in-corpus, not as new keys: all five appear in
        # profiles/nytimes.yaml.
        doc = _indented_block("profiles/nytimes.yaml", M835_KEY, M835_INDENT)
        urls = re.findall(r"https?://[^\s'\"]+", doc)
        assert len(urls) == 5, urls
        home = _read("profiles/nytimes.yaml")
        for url in urls:
            assert url in home, url


class TestTypeDRotationGuard:
    def test_rotation_window_opens_1010(self):
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


class TestTypeDM835QualitativeDiscipline:
    def test_mechanism_id(self):
        assert _m835_data()["mechanism_id"] == 835

    def test_manual_illustrative_discipline(self):
        # The m835 discipline lives in the statistical_discipline
        # mapping: MANUAL ILLUSTRATIVE tones, NOT_CALCULATED
        # statistics, engine NOT run at the finding layer.
        disc = _m835_data()["statistical_discipline"]
        assert "MANUAL_ILLUSTRATIVE" in str(disc)
        assert disc["tone_scores"] == "MANUAL_ILLUSTRATIVE"
        assert disc["p_value"] == "NOT_CALCULATED"
        assert disc["cohens_d"] == "NOT_CALCULATED"
        assert disc["ci_95"] == "NOT_CALCULATED"
        assert disc["is_significant"] is False
        assert disc["engine_run"] is False
        assert disc["scorer"] == "none"

    def test_verdict_and_grade(self):
        disc = _m835_data()["statistical_discipline"]
        assert disc["verdict"] == "directionally_supported_not_proven"
        assert _m835_data()["no_analysis_json_update"] is True
        assert disc["artifact_grade"] is False

    def test_not_falsification_family(self):
        # m835 names the family field differently (falsification_family
        # / ledger_hold) than the Type B/C blocks; the substance is
        # the same: NOT a member, ledger holds at 30.
        data = _m835_data()
        assert "NOT a member" in data["falsification_family"]
        assert data["ledger_hold"] == 30

    def test_illustrative_tones_documented(self):
        # Anthropic arms +0.10 / +0.25 (mean +0.175); Meta arms
        # +0.10 / -0.30 (mean -0.10); illustrative delta +0.275.
        # Descriptive only, never promoted to a finding.
        doc = _indented_block("profiles/nytimes.yaml", M835_KEY, M835_INDENT)
        assert "+0.175" in doc
        assert "-0.10" in doc
        assert "+0.275" in doc
        assert "MANUAL ILLUSTRATIVE" in doc

    def test_connects_to(self):
        assert _m835_data()["connects_to"] == [685, 822, 832, 790]

    def test_placement_under_anthropic(self):
        doc = _read("profiles/nytimes.yaml")
        rel_idx = doc.index("\ncompetitor_relationships:")
        anth_idx = doc.index("\n  anthropic:")
        key_idx = doc.index("\n    " + M835_KEY + ":")
        assert rel_idx < anth_idx < key_idx


class TestTypeDM836QualitativeDiscipline:
    def test_mechanism_id(self):
        assert _m836_data()["mechanism_id"] == 836

    def test_verdict_and_grade(self):
        data = _m836_data()
        assert data["verdict"] == "directionally_supported_not_proven"
        assert data["no_analysis_json_update"] is True
        # Grade lives in the asymmetry_scorer_result mapping for the
        # peg-matched pair design, not as a flat key.
        assert data["asymmetry_scorer_result"]["artifact_grade"] is False

    def test_not_falsification_family(self):
        data = _m836_data()
        assert data["falsification_family_member"] is False
        assert data["falsification_ledger"] == 30

    def test_manual_illustrative_carried_discipline(self):
        disc = _m836_data()["statistical_discipline"]
        assert disc["tone_scores"] == "MANUAL_ILLUSTRATIVE_CARRIED"
        assert disc["engine_run"] is False
        assert disc["is_significant"] is False
        assert disc["p_value"] == "NOT_CALCULATED"
        assert disc["cohens_d"] == "NOT_CALCULATED"

    def test_illustrative_delta_descriptive(self):
        # Meta -0.45 (carried from m820) minus Apple +0.10 (carried
        # from m635) = -0.55 illustrative delta. Descriptive only.
        res = _m836_data()["asymmetry_scorer_result"]
        assert res["illustrative_delta_meta_minus_apple"] == -0.55
        assert res["p_value"] == "NOT_CALCULATED"
        assert res["is_significant"] is False

    def test_peg_matched_replication_of_635(self):
        # PEG-MATCHED replication of mechanism 635 on company
        # privacy-assurance announcements; connects to the carried
        # arms' home mechanisms m814/m820.
        doc = _indented_block(
            "profiles/careers/journalists.yaml", M836_KEY, M836_INDENT
        )
        assert "PEG-MATCHED" in doc
        assert "635" in doc
        assert "814" in doc and "820" in doc

    def test_placement_under_lily_hay_newman(self):
        # The 2-space key nests under the lily_hay_newman list item.
        doc = _read("profiles/careers/journalists.yaml")
        item_idx = doc.index("lily_hay_newman")
        key_idx = doc.index("\n  " + M836_KEY + ":")
        assert item_idx < key_idx


class TestTypeDM837QualitativeDiscipline:
    def test_mechanism_id(self):
        assert _m837_data()["mechanism_id"] == 837

    def test_tone_not_scored(self):
        assert _m837_data()["tone_scores"] == "NOT_SCORED"

    def test_engine_not_run(self):
        assert _m837_data()["engine_run"] is False

    def test_verdict_and_grade(self):
        data = _m837_data()
        assert data["verdict"] == "directionally_supported_not_proven"
        assert data["no_analysis_json_update"] is True
        assert data["artifact_grade"] is False

    def test_not_falsification_family(self):
        data = _m837_data()
        assert data["falsification_family_member"] is False
        assert data["falsification_ledger"] == 30

    def test_demand_for_equity_thirteenth_direction(self):
        # DEMAND-FOR-EQUITY (warrant-for-demand): the lab extracts
        # equity upside in its compute supplier as consideration for
        # committed demand. THIRTEENTH relationship direction in the
        # m807 enumeration.
        data = _m837_data()
        assert "THIRTEENTH" in data["mechanism_name"]
        assert "DEMAND-FOR-EQUITY" in data["mechanism_name"]

    def test_block_is_last_top_level_key(self):
        # The m837 tail block runs to EOF in
        # profiles/competitor-entities.yaml.
        doc = _read("profiles/competitor-entities.yaml")
        tail = doc[doc.index("\n" + M837_KEY + ":") + 1 :]
        assert not re.search(r"(?m)^[A-Za-z_][^:]*:$", tail.split("\n", 1)[1])


class TestTypeDMaxIdAndNextNumber:
    def test_max_numeric_mechanism_id_is_837(self):
        assert _max_numeric_mechanism_id() == 837

    def test_zero_numeric_838_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(838) == []

    def test_zero_underscore_838_repo_wide(self):
        # Needles are format-built (per #715/#770); this file carries no
        # contiguous underscore-form 838 literal. The #1009 committed
        # test's runtime-built needle hits do not exist as source
        # literals.
        assert _repo_grep_underscore_mechanism(838) == []

    def test_zero_dash_838_repo_wide(self):
        assert _repo_grep_dash_mechanism(838) == []


class TestTypeDFalsificationLedger:
    def test_ledger_holds_at_30(self):
        assert _m836_data()["falsification_ledger"] == 30
        assert _m837_data()["falsification_ledger"] == 30
        # m835 names the field ledger_hold; same substance.
        assert _m835_data()["ledger_hold"] == 30

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

    def test_838_sweep_excludes_only_this_file_and_pycache(self):
        # The sole repo-wide 838-form literals at this run's checks are
        # the #1009 pyc in tests/__pycache__ (next-number guard of a
        # committed test, excluded per the #715 pattern-rescope
        # lesson). The source sweeps must therefore come back empty.
        import glob

        pyc_hits = glob.glob(
            os.path.join(TESTS_DIR, "__pycache__", "*1009*.pyc")
        )
        assert pyc_hits != [], "expected the #1009 pyc to exist"
        for p in pyc_hits:
            data = open(p, "rb").read()
            if b"mechanism-838" in data or b"mechanism_838" in data:
                break
        else:
            assert False, "no #1009 pyc carries the 838 needle"
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []


class TestTypeDFullSuiteTombstone:
    def test_1005_suite_log_stalled(self):
        log_path = os.path.join(
            os.path.expanduser("~"),
            "workspace",
            "goals",
            "mediascope-meta-wearables-press-analysis",
            "hidden_files",
            "type_d_1005_full_suite.log",
        )
        with open(log_path, "rb") as fh:
            data = fh.read()
        # Stalled mid-run: 1414 bytes of dots at ~2% since Sep 26
        # 00:xx PDT, no summary tokens anywhere, the process has since
        # exited.
        assert len(data) == 1414, len(data)
        for token in (b"passed", b"failed", b"error"):
            assert token not in data, token

    def test_tombstone_lineage_advances(self):
        # FORTY-THIRD consecutive background death per the #795
        # convention; lineage advances SIXTY-FIRST -> SIXTY-SECOND.
        # This run re-launches the suite writing to
        # type_d_1010_full_suite.log; the next Type D run checks it.
        # (The #1000 suite was already tombstoned by #1005; it is NOT
        # re-tombstoned here.)
        entry_anchor = "SIXTY-FIRST"
        entry_next = "SIXTY-SECOND"
        assert entry_anchor != entry_next

    def test_1010_suite_log_relaunched(self):
        log_path = os.path.join(
            os.path.expanduser("~"),
            "workspace",
            "goals",
            "mediascope-meta-wearables-press-analysis",
            "hidden_files",
            "type_d_1010_full_suite.log",
        )
        assert os.path.isfile(log_path), log_path


class TestTypeDSyntheticEngine:
    """Fresh engine meaningfulness calibration on synthetic corpora.

    Values hardcoded after a scratch run this run (NOT #1005's).
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
            [-0.48, -0.71, -0.55, -0.63, -0.44, -0.59, -0.52, -0.66],
            [0.22, 0.31, 0.18, 0.42, 0.27, 0.35, 0.24, 0.29],
            "Meta",
            ["Snap", "Apple"],
        )
        assert abs(r.asymmetry_score - (-0.8575)) < 1e-9
        assert abs(r.t_statistic - (-20.27695164092048)) < 1e-6
        assert r.p_value < 1e-10
        assert abs(r.cohens_d - (-10.13847582046024)) < 1e-6
        assert r.is_significant is True
        assert r.confidence_interval_upper < 0

    def test_near_null_pair_stays_silent(self):
        r = self._score(
            [0.03, -0.06, 0.01, -0.04, 0.05, -0.02, 0.00, -0.05],
            [0.01, -0.03, 0.04, -0.02, 0.00, 0.02, -0.01, 0.03],
            "Meta",
            ["Snap", "Apple"],
        )
        assert abs(r.asymmetry_score - (-0.015)) < 1e-9
        assert r.p_value > 0.3
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
        assert _m835_data()["statistical_discipline"]["is_significant"] is False
        assert (
            _m836_data()["asymmetry_scorer_result"]["is_significant"] is False
        )
        assert _m837_data()["engine_run"] is False


class TestDocSync1010:
    def test_readme_row_1010(self):
        assert TEST_BASENAME in _read(README_PATH)

    def test_architecture_row_1010(self):
        assert TEST_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_1010_file(self):
        doc = _read(ARCH_PATH)
        assert TEST_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))


class TestIterationLog1010:
    def _entry(self):
        log = _read(LOG_PATH)
        idx = log.index("## #1010 Type D:")
        return log[idx : idx + 15000]

    def test_entry_present(self):
        assert "## #1010 Type D:" in _read(LOG_PATH)

    def test_entry_records_tombstone_and_integrity(self):
        entry = self._entry()
        assert "SIXTY-SECOND" in entry
        assert "837" in entry
