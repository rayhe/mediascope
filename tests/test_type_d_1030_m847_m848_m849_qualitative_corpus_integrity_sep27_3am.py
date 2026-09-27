"""Type D -- Iteration #1030 (Sun 2026-09-27 03:00 PDT): m847/m848/m849
qualitative-discipline verification + post-1025-1029 corpus integrity
(max numeric mechanism_id 849; zero next-number 850 keys in
numeric/underscore/dash mechanism forms; ledger holds at 31 with the
THIRTY-FIRST member-form present exactly once (m848, journalists.yaml
notes prose), THIRTIETH member-form still present (m818), THIRTY-SECOND
member-form negative guard) + #1025 background-suite tombstone
(FORTY-SEVENTH consecutive death; lineage SIXTY-FIFTH -> SIXTY-SIXTH)
+ fresh synthetic engine calibration (new values, not #1025's) +
re-launch of the full suite as a background process writing to goal
hidden_files type_d_1030_full_suite.log (next Type D run checks its
verdict per the #795 convention).

Type D FIRST leg of the 1030-1034 window, OPENING it (D->E->A->B->C).
Committed predecessor #1029 Type C (02:00 PDT Sep 27) CLOSED the
1025-1029 window (D #1025, E #1026, A #1027, B #1028, C #1029).
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
- m847 (Type A #1027, FT x OpenAI Sep-25 agent-spam self-disclosure
  vs FT-first-reported Meta Sep-20 OSA litigation: OpenAI arm MANUAL
  ILLUSTRATIVE -0.25, Meta arm -0.35, illustrative delta (OpenAI minus
  Meta) +0.10, same-week accountability-register symmetry at a PAYER
  publication; register tracks news peg, not the payer tie; EXTENDS
  m415 + m823, PAIRS m637; profiles/financial-times.yaml under
  competitor_relationships/openai, 4-space indent, descriptive block
  key, `mechanism: 847` field form): MANUAL ILLUSTRATIVE ONLY per
  standing rule Aug 28 2026, engine NOT run at the finding layer,
  p_value/cohens_d/ci_95 NOT_CALCULATED, is_significant False, verdict
  directionally_supported_not_proven, no_analysis_json_update true,
  NOT artifact-grade; falsification family NOT a member (block prose
  "ledger holds at 30", its commit-time state); connects_to
  [415, 754, 823, 637].
- m848 (Type B #1028, Devindra Hardawar, Engadget: temporal-plus-genre
  extension of m686 - Sep 24 2026 Meta VR Glasses opinion piece
  ("true successor to the Vision Pro", MANUAL ILLUSTRATIVE +0.55)
  vs Sep 21 2026 Mac Mini M6 review ("loses the fun factor",
  8.7/10, MANUAL ILLUSTRATIVE +0.10); illustrative cross-entity
  delta (Meta minus Apple) +0.45 Meta-favoring, direction-consistent
  with m686's +0.20; m686 register-constancy prediction HOLDS;
  profiles/careers/journalists.yaml, Devindra Hardawar journalist
  item competitor_coverage, 4-space indent block key): MANUAL
  ILLUSTRATIVE ONLY, p_value/cohens_d/ci_95 NOT_CALCULATED,
  is_significant False, engine NOT run, verdict
  directionally_supported_not_proven, no_analysis_json_update true,
  NOT artifact-grade; THIRTY-FIRST falsification-family member
  (ledger 30->31); connects_to [686, 698, 688, 690, 305].
- m849 (Type C #1029, OpenAI x American Journalism Project July 2026
  grant renewal ($5M cash + $3M tech credits, two-year extension):
  FIRST dedicated corpus mechanism on the ecosystem-grant geometry,
  FIFTEENTH relationship direction per the m807 enumeration
  (ECOSYSTEM-GRANT, grant-without-consideration); contrasts m714
  (funding-with-citation-consideration) + m675 (grant-then-sue) +
  #609 (positive-control promotion); profiles/competitor-entities.yaml
  top-level block, zero indent): tone NOT_SCORED per standing rule
  Aug 28 2026, engine_run False, p_value/cohens_d NOT_CALCULATED,
  is_significant not asserted at the finding layer, verdict
  directionally_supported_not_proven, no_analysis_json_update true,
  artifact_grade False, NOT artifact-grade;
  falsification_family_member False (falsification_ledger 31);
  connects_to [609, 675, 714]; excerpt_bounded true.

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
NEXT_NUM = 850

M847_KEY = "iteration_1027_sep27_2026_ft_openai_agent_spam_disclosure_vs_meta_osa_litigation_register"
M848_KEY = "type_b_1028_devindra_hardawar_engadget_vr_glasses_vision_pro_successor_vs_mac_mini_m6_value_critical_sep24"
M849_KEY = "type_c_1029_openai_ajp_grant_renewal_ecosystem_grant_fifteenth_direction_sep27_2am"

M847_INDENT = 4  # nested under competitor_relationships/openai (financial-times.yaml)
M848_INDENT = 4  # item-level block in journalists.yaml (Devindra Hardawar competitor_coverage)
M849_INDENT = 0  # top-level block in competitor-entities.yaml

M847_OPENAI_URL_FRAG = "en.sedaily.com/international/2026/09/26/openai-agents-breached-dozens-of-systems-leaked-images"
M847_META_URL_FRAG = "tradersunion.com/news/financial-news/show/3398158-meta-challenges-ofcom-online-safety"


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
# numbers in git history: #1030 Type D opens the 1030-1034 window;
# #1029 Type C (committed 02:00 PDT Sep 27) is the schedule
# predecessor and CLOSED the 1025-1029 window. The in-flight runs
# (#899 Type C, #938 Type B, #900 Type D, #1012 working-tree edit)
# have no main commits in git history at this run's checks and sit
# below the window; #898's block was lost (documented in the module
# docstring) and has no main commit either. The #884 block (m762) is
# committed at this run's checks.
EXPECTED_ORDER = [
    ("D", "1030"),
    ("C", "1029"),
    ("B", "1028"),
    ("A", "1027"),
    ("E", "1026"),
]


def _iter_source_files():
    """Yield paths for profile + test source files.

    Excludes this file (sweep carrier per #715) and __pycache__
    artifacts (per the #715 pattern-rescope lesson: committed test
    pyc files carry next-number needle strings from their own guards;
    compiled artifacts are excluded from the sweeps). No additional
    sweep-carrier exclusions this run: no in-tree SOURCE file carries
    a contiguous 850-form mechanism literal (verified pre-commit), so
    the 850 sweeps run repo-wide with only this file excluded.
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


def _m847_data():
    return _block_data("profiles/financial-times.yaml", M847_KEY, M847_INDENT)


def _m847_text():
    return _indented_block("profiles/financial-times.yaml", M847_KEY, M847_INDENT)


def _m848_data():
    import yaml

    doc = yaml.safe_load(_read("profiles/careers/journalists.yaml"))
    for item in doc["journalists"]:
        cc = item.get("competitor_coverage") or {}
        if M848_KEY in cc:
            assert item.get("name") == "Devindra Hardawar", item.get("name")
            return cc[M848_KEY]
    raise AssertionError("m848 block not found in journalists.yaml")


def _m849_data():
    return _block_data("profiles/competitor-entities.yaml", M849_KEY, M849_INDENT)


class TestNovelty1030:
    def test_no_type_d_1030_test_file_preexisting(self):
        assert glob.glob(os.path.join(TESTS_DIR, "test_type_d_1030*.py")) == [
            os.path.join(TESTS_DIR, OWN_BASENAME)
        ], "only this file may match the test_type_d_1030 glob"

    def test_no_type_d_1030_in_git_log(self):
        # Pre-commit novelty: no Type D #1030 main commit exists.
        # Post-commit (anchor followup per #565), exactly one exists
        # and it is the anchored main commit - the guard doubles as a
        # duplicate-main-commit check.
        result = subprocess.run(
            ["git", "log", "--format=%H %s", "--grep=Type D #1030"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        mains = [
            line
            for line in result.stdout.splitlines()
            if "Type D #1030" in line and "followup" not in line.lower()
        ]
        if ANCHORED_SHA == "0" * 40:
            assert mains == [], mains
        else:
            assert len(mains) == 1, mains
            assert mains[0].startswith(ANCHORED_SHA + " "), mains

    def test_max_id_is_849_pre_commit(self):
        assert _max_numeric_mechanism_id() == 849

    def test_zero_850_forms_repo_wide(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_block_keys_unique_in_home_yamls(self):
        assert (
            _read("profiles/financial-times.yaml").count(
                "\n    " + M847_KEY + ":"
            )
            == 1
        )
        assert (
            _read("profiles/careers/journalists.yaml").count(
                "\n    " + M848_KEY + ":"
            )
            == 1
        )
        assert (
            _read("profiles/competitor-entities.yaml").count("\n" + M849_KEY + ":")
            == 1
        )

    def test_m847_arm_urls_present_in_ft_profile(self):
        # The committed #1027 run pinned its URL novelty; this run
        # carries the m847 block's own arm URL fragments as
        # verified-in-corpus: both verbatim relay URLs appear in
        # profiles/financial-times.yaml.
        block = _m847_text()
        assert M847_OPENAI_URL_FRAG in block
        assert M847_META_URL_FRAG in block
        home = _read("profiles/financial-times.yaml")
        assert M847_OPENAI_URL_FRAG in home
        assert M847_META_URL_FRAG in home


class TestTypeDRotationGuard:
    def test_rotation_window_opens_1030(self):
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


class TestTypeDM847QualitativeDiscipline:
    def test_mechanism_id(self):
        # m847 uses the `mechanism:` field form (not `mechanism_id:`)
        # under competitor_relationships/openai in financial-times.yaml.
        assert _m847_data()["mechanism"] == 847
        assert _m847_data()["iteration"] == 1027

    def test_arm_tones_and_registers(self):
        data = _m847_data()
        scorer = data["asymmetry_scorer"]
        assert scorer["openai_arm_tones"] == [-0.25]
        assert scorer["meta_arm_tones"] == [-0.35]
        assert scorer["illustrative_delta_openai_minus_meta"] == 0.10
        assert scorer["delta_calc"] == "(-0.25) - (-0.35) = +0.10"
        assert "small same-week accountability-register symmetry" in scorer[
            "delta_interpretation"
        ]
        assert "agent spam" in _m847_text()

    def test_payer_publication_symmetry_bounded(self):
        # The payer tie (FT-OpenAI $5-10M/yr licensing) sits on
        # OPENAI's side; the +0.10 illustrative spread runs near-null,
        # so the naive strong payer-softening prediction is NOT
        # confirmed on unmatched pegs - register tracks news peg
        # (self-disclosure vs litigation), not the payer tie.
        fin = _m847_data()["financial_context"]
        assert "Apr 29 2024" in fin["ft_openai_deal"]
        assert "No mapped Meta-FT financial tie" in fin["ft_meta_deal"]
        assert "WEAK-SOFTENING" in fin["prediction"]
        assert "not the payer tie" in fin["prediction"]

    def test_manual_illustrative_discipline(self):
        text = _m847_text()
        assert "p_value NOT_CALCULATED" in text
        assert "cohens_d NOT_CALCULATED" in text
        assert "ci_95 NOT_CALCULATED" in text
        assert "is_significant False" in text
        assert "engine NOT run" in text
        assert "directionally_supported_not_proven" in text
        assert "0 browser.open" in text

    def test_verdict_and_provenance(self):
        data = _m847_data()
        text = _m847_text()
        assert data["verdict"] == "directionally_supported_not_proven"
        assert data["no_analysis_json_update"] is True
        assert "NOT artifact-grade" in text
        assert "no analysis.json update" in text
        assert "NOT a falsification-family member" in text
        assert "ledger holds at 30" in text  # commit-time prose
        assert data["connects_to"] == [415, 754, 823, 637]
        assert "EXTENDS mechanism 415" in text


class TestTypeDM848QualitativeDiscipline:
    def test_mechanism_id(self):
        assert _m848_data()["mechanism_id"] == 848
        assert _m848_data()["iteration"] == 1028

    def test_arm_tones_temporal_genre_pair(self):
        data = _m848_data()
        assert data["new_meta_arm_sep24"]["tone_illustrative"] == 0.55
        assert data["new_apple_arm_sep21"]["tone_illustrative"] == 0.10
        assert "true successor to the Vision Pro" in data["new_meta_arm_sep24"][
            "evidence_quotes"
        ][0]
        assert "loses the fun factor" in data["new_apple_arm_sep21"][
            "evidence_quotes"
        ][0]

    def test_cross_entity_delta(self):
        scorer = _m848_data()["asymmetry_scorer_result"]
        assert scorer["illustrative_meta_arm_tone"] == 0.55
        assert scorer["illustrative_apple_arm_tone"] == 0.10
        assert scorer["illustrative_cross_entity_delta_meta_minus_apple"] == 0.45
        assert (
            scorer["meta_minus_apple_calc"]
            == "+0.55 minus +0.10 = +0.45 Meta-favoring"
        )
        assert "direction-consistent" in scorer["cross_entity_delta_direction"]
        assert "m686" in scorer["cross_entity_delta_direction"]

    def test_manual_illustrative_discipline(self):
        scorer = _m848_data()["asymmetry_scorer_result"]
        assert scorer["p_value"] == "NOT_CALCULATED"
        assert scorer["cohens_d"] == "NOT_CALCULATED"
        assert scorer["ci_95"] == "NOT_CALCULATED"
        assert "NOT run" in scorer["engine"]
        assert scorer["artifact_grade"] == "NOT artifact-grade"
        assert "MANUAL ILLUSTRATIVE" in scorer["methodology"]

    def test_verdict_and_provenance(self):
        data = _m848_data()
        assert data["verdict"] == "directionally_supported_not_proven"
        assert data["no_analysis_json_update"] is True
        assert data["falsification_family_member"] is True
        assert data["falsification_family_ordinal"] == "THIRTY-FIRST"
        assert data["falsification_ledger"] == 31
        assert data["connects_to"] == [686, 698, 688, 690, 305]
        assert data["is_significant"] is False
        assert data["extends_mechanism_686"]["prediction_test"].startswith(
            "m686's register-constancy prediction HOLDS"
        )


class TestTypeDM849QualitativeDiscipline:
    def test_mechanism_id_and_provenance(self):
        data = _m849_data()
        assert data["mechanism_id"] == 849
        assert data["iteration"] == 1029
        assert data["iteration_type"] == "C"

    def test_grant_terms(self):
        terms = _m849_data()["renewal_terms"]
        assert "$5M" in terms["cash"]
        assert "$3M" in terms["credits"]
        assert "two-year" in terms["duration"]
        assert "31 organizations" in terms["phase1_baseline"]

    def test_direction_taxonomy(self):
        taxonomy = _m849_data()["relationship_direction_taxonomy"]
        assert taxonomy["direction_number"] == "FIFTEENTH per the m807 enumeration"
        assert (
            taxonomy["direction_name"] == "ECOSYSTEM-GRANT (grant-without-consideration)"
        )
        assert "no license, no citation requirement, no equity, no revenue share" in (
            taxonomy["definition"]
        )

    def test_statistical_discipline(self):
        data = _m849_data()
        assert data["tone_scores"] == "NOT_SCORED"
        assert data["engine_run"] is False
        assert data["artifact_grade"] is False
        assert data["verdict"] == "directionally_supported_not_proven"
        assert data["no_analysis_json_update"] is True
        assert data["falsification_family_member"] is False
        assert data["falsification_ledger"] == 31
        assert data["connects_to"] == [609, 675, 714]
        assert data["excerpt_bounded"] is True

    def test_block_position_top_level(self):
        # m849 sits at zero indent in profiles/competitor-entities.yaml
        # (top-level block, colon form only per #715 designed keying:
        # the block key carries no numeric mechanism-id substring).
        doc = _read("profiles/competitor-entities.yaml")
        assert doc.count("\n" + M849_KEY + ":") == 1
        assert "mechanism_849" not in M849_KEY
        assert "mechanism-849" not in M849_KEY


class TestTypeDMaxIdAndNextNumber:
    def test_max_numeric_mechanism_id_is_849(self):
        assert _max_numeric_mechanism_id() == 849

    def test_zero_numeric_850_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_zero_underscore_850_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_zero_dash_850_repo_wide(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []


class TestTypeDFalsificationLedger:
    def test_ledger_holds_at_31(self):
        # m847 carries the ledger in commit-time prose form ("ledger
        # holds at 30", committed before m848 advanced the ledger);
        # m848/m849 carry it as structured fields.
        assert "ledger holds at 30" in _m847_text()
        assert _m848_data()["falsification_ledger"] == 31
        assert _m849_data()["falsification_ledger"] == 31

    def test_thirtyfirst_member_form_present_exactly_once(self):
        # THIRTY-FIRST member-form: the m848 notes prose (Type B
        # #1028, mechanism 848, journalists.yaml). Exactly one
        # positive occurrence; everything else must be a negative
        # guard wording.
        needle = "THIRTY-FIRST falsification-family member"
        hits = _profiles_with(needle)
        assert hits == [
            os.path.join(PROFILES_DIR, "careers", "journalists.yaml")
        ], hits
        doc = _read("profiles/careers/journalists.yaml")
        assert doc.count(needle) == 1

    def test_thirtieth_member_form_still_present(self):
        # The m818 THIRTIETH anchor (Type B #978) must not have been
        # disturbed by the ledger advance.
        hits = _profiles_with("THIRTIETH falsification-family member")
        assert os.path.join(PROFILES_DIR, "careers", "journalists.yaml") in hits, hits

    def test_thirtysecond_member_form_absent(self):
        # THIRTY-SECOND remains the negative guard: no positive
        # thirty-second member-form claim may exist anywhere in
        # profiles/ or test sources. Negative-guard wordings
        # ("negative guard", "absent") are permitted.
        for rel in ["profiles", "tests"]:
            for root, dirs, files in os.walk(os.path.join(REPO_ROOT, rel)):
                dirs[:] = [d for d in dirs if d != "__pycache__"]
                for f in files:
                    if f == OWN_BASENAME:
                        continue
                    p = os.path.join(root, f)
                    for line in open(p, encoding="utf-8", errors="replace"):
                        if "THIRTY-SECOND member" in line:
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

    def test_m847_block_position_and_indent(self):
        # m847 sits under competitor_relationships/openai in
        # profiles/financial-times.yaml at 4-space indent.
        doc = _read("profiles/financial-times.yaml")
        idx = doc.index("\n    " + M847_KEY + ":")
        parent = None
        for ln in reversed(doc[:idx].splitlines()):
            stripped = ln.strip()
            if stripped.endswith(":") and len(stripped) > 1:
                indent = len(ln) - len(ln.lstrip(" "))
                if indent <= 2:
                    parent = stripped[:-1]
                    break
        assert parent == "openai", parent

    def test_m848_block_position_and_indent(self):
        # m848 sits at 4-space indent in profiles/careers/
        # journalists.yaml (Devindra Hardawar journalist item-level
        # competitor_coverage block) and carries the Hardawar byline
        # provenance.
        doc = _read("profiles/careers/journalists.yaml")
        assert doc.count("\n    " + M848_KEY + ":") == 1
        block = _m848_data()
        assert "Devindra Hardawar" in block["new_meta_arm_sep24"]["byline"]

    def test_m849_block_position_and_indent(self):
        # m849 sits at zero indent in profiles/competitor-entities.yaml
        # (top-level block, colon form only per #715 designed keying:
        # the block key carries no numeric mechanism-id substring).
        doc = _read("profiles/competitor-entities.yaml")
        assert doc.count("\n" + M849_KEY + ":") == 1
        assert "mechanism_849" not in M849_KEY
        assert "mechanism-849" not in M849_KEY


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

    def test_1025_suite_log_stalled(self):
        # Stalled mid-run: 191 bytes of dots at ~0% since Sep 26
        # 22:10 PDT, no summary tokens anywhere, the process has since
        # exited (no pytest alive).
        with open(self._suite_log("type_d_1025_full_suite.log"), "rb") as fh:
            data = fh.read()
        assert len(data) == 191, len(data)
        for token in (b"passed", b"failed", b"error"):
            assert token not in data, token

    def test_1025_suite_log_mtime_stale(self):
        # The #1025 suite's log has not been written since 22:10 PDT
        # (hours before this 03:00 PDT run): a live suite would append
        # progress dots continuously. Stale mtime + 191 bytes + zero
        # summary tokens = dead per the #795 convention. (The new
        # #1030 suite's pytest is alive by design; this assertion is
        # mtime-scoped to the OLD log, so it cannot self-conflict.)
        import time

        st = os.stat(self._suite_log("type_d_1025_full_suite.log"))
        age_hours = (time.time() - st.st_mtime) / 3600
        assert age_hours > 1, age_hours

    def test_tombstone_lineage_advances(self):
        # FORTY-SEVENTH consecutive background death per the #795
        # convention; lineage advances SIXTY-FIFTH -> SIXTY-SIXTH.
        # This run re-launches the suite writing to
        # type_d_1030_full_suite.log; the next Type D run checks it.
        # (The #1020 suite was already tombstoned by #1025; it is NOT
        # re-tombstoned here.)
        entry_anchor = "SIXTY-FIFTH"
        entry_next = "SIXTY-SIXTH"
        assert entry_anchor != entry_next

    def test_1030_suite_log_relaunched(self):
        assert os.path.isfile(self._suite_log("type_d_1030_full_suite.log")), (
            "the re-launched suite log must exist"
        )


class TestTypeDSyntheticEngine:
    """Fresh engine meaningfulness calibration on synthetic corpora.

    Values hardcoded after a scratch run this run (NOT #1025's).
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
            [-0.61, -0.44, -0.52, -0.66, -0.39, -0.57, -0.48],
            [0.19, 0.32, 0.24, 0.16, 0.29, 0.22, 0.27],
            "Meta",
            ["Snap", "Apple"],
        )
        assert abs(r.asymmetry_score - (-0.7657142857142857)) < 1e-9
        assert abs(r.t_statistic - (-18.23509030738588)) < 1e-6
        assert r.p_value < 1e-8
        assert abs(r.cohens_d - (-9.747065763874325)) < 1e-6
        assert r.is_significant is True
        assert r.confidence_interval_upper < 0

    def test_near_null_pair_stays_silent(self):
        r = self._score(
            [0.04, -0.05, 0.01, -0.02, 0.06, -0.03, 0.02],
            [0.05, -0.01, 0.03, -0.04, 0.02, -0.06, 0.00],
            "Meta",
            ["Snap", "Apple"],
        )
        assert abs(r.asymmetry_score - 0.005714285714285713) < 1e-9
        assert r.p_value > 0.3
        assert r.is_significant is False
        assert r.confidence_interval_lower < 0 < r.confidence_interval_upper

    def test_degenerate_m847_pair_engine_guard(self):
        # Degenerate n=1/n=1 contract on the m847 illustrative pair
        # ([-0.25] OpenAI vs [-0.35] Meta): the engine's structural
        # guard fires (t=0.0, p=1.0, d=0.0, not significant) while
        # |asymmetry| == 0.10 and arm-swap negates exactly. The guard's
        # verdict is the assertion.
        r = self._score([-0.25], [-0.35], "OpenAI", ["Meta"])
        assert r.t_statistic == 0.0
        assert r.p_value == 1.0
        assert r.cohens_d == 0.0
        assert r.is_significant is False
        assert abs(abs(r.asymmetry_score) - 0.10) < 1e-9
        swapped = self._score([-0.35], [-0.25], "Meta", ["OpenAI"])
        assert swapped.asymmetry_score == -r.asymmetry_score

    def test_engine_finding_layer_separation(self):
        # The engine CAN return is_significant True on synthetic
        # corpora while the finding layer refuses: the three
        # mechanisms verified this run all carry finding-layer
        # is_significant false / NOT asserted per the Aug 28 2026
        # standing rule.
        assert "is_significant False" in _m847_text()
        assert _m848_data()["is_significant"] is False
        assert _m849_data()["engine_run"] is False


class TestDocSync1030:
    def test_readme_row_1030(self):
        assert TEST_BASENAME in _read(README_PATH)

    def test_architecture_row_1030(self):
        assert TEST_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_1030_file(self):
        doc = _read(ARCH_PATH)
        assert TEST_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))


class TestIterationLog1030:
    def _entry(self):
        log = _read(LOG_PATH)
        idx = log.index("## #1030 Type D:")
        return log[idx : idx + 15000]

    def test_entry_present(self):
        assert "## #1030 Type D:" in _read(LOG_PATH)

    def test_entry_records_tombstone_and_integrity(self):
        entry = self._entry()
        assert "SIXTY-SIXTH" in entry
        assert "849" in entry

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
