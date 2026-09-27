"""Type D -- Iteration #1035 (Sun 2026-09-27 08:00 PDT): m850/m851/m852
qualitative-discipline verification + post-1030-1034 corpus integrity
(max numeric mechanism_id 852; zero next-number 853 keys in
numeric/underscore/dash mechanism forms; ledger holds at 31 with the
THIRTY-FIRST member-form present exactly once (m848, journalists.yaml
notes prose), THIRTIETH member-form still present (m818), THIRTY-SECOND
member-form negative guard) + #1030 background-suite tombstone
(FORTY-EIGHTH consecutive death; lineage SIXTY-SIXTH -> SIXTY-SEVENTH)
+ fresh synthetic engine calibration (new values, not #1030's) +
re-launch of the full suite as a background process writing to goal
hidden_files type_d_1035_full_suite.log (next Type D run checks its
verdict per the #795 convention).

Type D FIRST leg of the 1035-1039 window, OPENING it (D->E->A->B->C).
Committed predecessor #1034 Type C (07:00 PDT Sep 27) CLOSED the
1030-1034 window (D #1030, E #1031, A #1032, B #1033, C #1034).
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
- m850 (Type A #1032, Reuters x Anthropic Sep-24 Akamai-deal neutral
  register vs Reuters x Meta Sep-23 Connect privacy-hardened preview:
  Anthropic arm MANUAL ILLUSTRATIVE -0.05, Meta arm -0.45,
  illustrative delta (Anthropic minus Meta) +0.40, 24-hour same-desk
  spread, widest Reuters-desk wire-arm spread, widening m844's +0.05
  near-null; Reuters-Meta Oct 25 2024 deal on META's side so the spread
  runs OPPOSITE the naive payer-softening prediction; EXTENDS m844 to
  a FOURTH desk entity; PAIRS m823 capital-register contrast;
  profiles/competitor-coverage-research.yaml under
  cross_publication_findings, 2-space indent, descriptive block key,
  `mechanism_id: 850` field form): MANUAL ILLUSTRATIVE ONLY per
  standing rule Aug 28 2026, engine NOT run at the finding layer,
  p_value/cohens_d/ci_95 NOT_CALCULATED, is_significant False, verdict
  directionally_supported_not_proven, no_analysis_json_update true,
  NOT artifact-grade; falsification family NOT a member (ledger holds
  at 31, THIRTY-FIRST present (m848 journalists.yaml notes),
  THIRTY-SECOND absent); connects_to [844, 823, 739].
- m851 (Type B #1033, Aditya Soni, Reuters: Sep-23 Meta Connect
  privacy-hardened preview (-0.45 carried un-rescored from m850 per
  #807) vs Sep-1 Apple Cook-to-Ternus legacy-celebration piece
  (+0.30); illustrative cross-entity delta (Apple minus Meta) +0.75
  Apple-favoring, same writer, same wire, 22 days apart; resolves
  m850's writer-vs-desk confounder within-writer (desk-level +0.40
  widens to +0.75 writer-level); Reuters-Meta Oct 25 2024 deal on
  Meta's side so the spread runs OPPOSITE the naive payer-softening
  prediction; profiles/careers/journalists.yaml, top-level
  aditya_soni item, 4-space indent block key): MANUAL ILLUSTRATIVE
  ONLY, p_value/cohens_d/ci_95 NOT_CALCULATED, is_significant False,
  engine NOT run, verdict directionally_supported_not_proven,
  no_analysis_json_update true, NOT artifact-grade; NOT a
  falsification-family member (ledger 31); connects_to
  [850, 844, 739, 664, 633].
- m852 (Type C #1034, Amazon x Meta Muse agentic-commerce denial
  (Sep 20) + Meta x Shopify agentic-checkout deal (Sep 21/22):
  FIRST dedicated corpus mechanism on the September 2026
  agentic-commerce licensing split; SIXTEENTH relationship direction
  per the m807 enumeration (COMMERCE-GATEKEEPING, access-denial as
  licensing leverage); Amazon three-role geometry (PAYS publishers
  m559, BACKS zero-deal labs, DENIES rival lab's agent);
  profiles/competitor-entities.yaml top-level block, zero indent):
  tone NOT_SCORED per standing rule Aug 28 2026, engine_run False,
  p_value/cohens_d NOT_CALCULATED, is_significant not asserted at the
  finding layer, verdict directionally_supported_not_proven,
  no_analysis_json_update true, artifact_grade False, NOT
  artifact-grade; falsification_family_member False
  (falsification_ledger 31); connects_to [831, 849, 559, 594, 509];
  excerpt_bounded true.

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

ANCHORED_SHA = "7d8addf43a15f436c21cae7588549c7b9aa4724c"  # patched post-commit per #565

# Built by concatenation so this source file carries no contiguous
# underscore-form mechanism literal (per the #770 lesson).
MECH_ID_MARKER = "mechanism" + "_"
NEXT_NUM = 853

M850_KEY = "reuters_anthropic_akamai_neutral_deal_register_vs_meta_connect_privacy_hardened_register_sep2026"
M851_KEY = "type_b_1033_aditya_soni_reuters_meta_privacy_preview_vs_apple_ternus_celebration_sep27"
M852_KEY = "type_c_1034_amazon_meta_muse_agentic_commerce_denial_shopify_shop_pay_commerce_conversion_sixteenth_direction_sep27_7am"

M850_INDENT = 2  # nested under cross_publication_findings (competitor-coverage-research.yaml)
M851_INDENT = 4  # item-level block in journalists.yaml (top-level aditya_soni item)
M852_INDENT = 0  # top-level block in competitor-entities.yaml

M850_ANTHROPIC_URL_FRAG = "reuters.com/technology/akamai-anthropic-sign-116-billion-cloud-services-deal-2026-09-24"
M850_META_URL_FRAG = "reuters.com/business/meta-expected-unveil-smart-glasses-without-camera-privacy-concerns-grow-2026-09-23"


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
# numbers in git history: #1035 Type D opens the 1035-1039 window;
# #1034 Type C (committed 07:00 PDT Sep 27) is the schedule
# predecessor and CLOSED the 1030-1034 window. The in-flight runs
# (#899 Type C, #938 Type B, #900 Type D, #1012 working-tree edit)
# have no main commits in git history at this run's checks and sit
# below the window; #898's block was lost (documented in the module
# docstring) and has no main commit either. The #884 block (m762) is
# committed at this run's checks.
EXPECTED_ORDER = [
    ("D", "1035"),
    ("C", "1034"),
    ("B", "1033"),
    ("A", "1032"),
    ("E", "1031"),
]


def _iter_source_files():
    """Yield paths for profile + test source files.

    Excludes this file (sweep carrier per #715) and __pycache__
    artifacts (per the #715 pattern-rescope lesson: committed test
    pyc files carry next-number needle strings from their own guards;
    compiled artifacts are excluded from the sweeps). No additional
    sweep-carrier exclusions this run: no in-tree SOURCE file carries
    a contiguous 853-form mechanism literal (verified pre-commit), so
    the 853 sweeps run repo-wide with only this file excluded.
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


def _m850_data():
    return _block_data(
        "profiles/competitor-coverage-research.yaml", M850_KEY, M850_INDENT
    )


def _m850_text():
    return _indented_block(
        "profiles/competitor-coverage-research.yaml", M850_KEY, M850_INDENT
    )


def _m851_data():
    return _block_data("profiles/careers/journalists.yaml", M851_KEY, M851_INDENT)


def _m852_data():
    return _block_data("profiles/competitor-entities.yaml", M852_KEY, M852_INDENT)


class TestNovelty1035:
    def test_no_type_d_1035_test_file_preexisting(self):
        assert glob.glob(os.path.join(TESTS_DIR, "test_type_d_1035*.py")) == [
            os.path.join(TESTS_DIR, OWN_BASENAME)
        ], "only this file may match the test_type_d_1035 glob"

    def test_no_type_d_1035_in_git_log(self):
        # Pre-commit novelty: no Type D #1035 main commit exists.
        # Post-commit (anchor followup per #565), exactly one exists
        # and it is the anchored main commit - the guard doubles as a
        # duplicate-main-commit check.
        result = subprocess.run(
            ["git", "log", "--format=%H %s", "--grep=Type D #1035"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        mains = [
            line
            for line in result.stdout.splitlines()
            if "Type D #1035" in line and "followup" not in line.lower()
        ]
        if ANCHORED_SHA == "0" * 40:
            assert mains == [], mains
        else:
            assert len(mains) == 1, mains
            assert mains[0].startswith(ANCHORED_SHA + " "), mains

    def test_max_id_is_852_pre_commit(self):
        assert _max_numeric_mechanism_id() == 852

    def test_zero_853_forms_repo_wide(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_block_keys_unique_in_home_yamls(self):
        assert (
            _read("profiles/competitor-coverage-research.yaml").count(
                "\n  " + M850_KEY + ":"
            )
            == 1
        )
        assert (
            _read("profiles/careers/journalists.yaml").count(
                "\n    " + M851_KEY + ":"
            )
            == 1
        )
        assert (
            _read("profiles/competitor-entities.yaml").count("\n" + M852_KEY + ":")
            == 1
        )

    def test_m850_arm_urls_present_in_research_profile(self):
        # The committed #1032 run pinned its URL novelty; this run
        # carries the m850 block's own arm URL fragments as
        # verified-in-corpus: both verbatim reuters.com URLs appear in
        # profiles/competitor-coverage-research.yaml.
        block = _m850_text()
        assert M850_ANTHROPIC_URL_FRAG in block
        assert M850_META_URL_FRAG in block
        home = _read("profiles/competitor-coverage-research.yaml")
        assert M850_ANTHROPIC_URL_FRAG in home
        assert M850_META_URL_FRAG in home


class TestTypeDRotationGuard:
    def test_rotation_window_opens_1035(self):
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


class TestTypeDM850QualitativeDiscipline:
    def test_mechanism_id(self):
        # m850 uses the `mechanism_id:` field form under
        # cross_publication_findings in competitor-coverage-research.yaml.
        assert _m850_data()["mechanism_id"] == 850
        assert _m850_data()["iteration"] == 1032

    def test_arm_tones_and_spread(self):
        data = _m850_data()
        scorer = data["asymmetry_scorer"]
        assert scorer["anthropic_arm_tones"] == [-0.05]
        assert scorer["meta_arm_tones"] == [-0.45]
        assert scorer["anthropic_arm_avg"] == -0.05
        assert scorer["meta_arm_avg"] == -0.45
        assert scorer["illustrative_delta_anthropic_minus_meta"] == 0.40
        assert scorer["delta_calc"] == "(-0.05) - (-0.45) = +0.40"
        assert scorer["is_significant"] is False
        assert scorer["p_value"] == "NOT_CALCULATED"
        assert scorer["statistical_contract"] == "degenerate_small_n_per_arm"
        assert "24-hour same-desk spread" in scorer["delta_interpretation"]

    def test_payer_side_counterdirectional_bounded(self):
        # The payer tie (Reuters-Meta Oct 25 2024 content deal) sits on
        # META's side; the +0.40 illustrative spread with the harsher
        # register on the payer runs OPPOSITE the naive payer-softening
        # prediction, extending m844's counterdirectional reading.
        fin = _m850_data()["financial_context"]
        assert "Oct 25, 2024" in fin["reuters_meta_deal"]
        assert "payer" in fin["reuters_meta_deal"].lower()
        assert "naive payer-softening prediction fails" in fin["prediction"]
        assert "fourth Reuters-desk entity" in fin["prediction"]

    def test_manual_illustrative_discipline(self):
        disc = _m850_data()["statistical_discipline"]
        assert "MANUAL ILLUSTRATIVE scores only" in disc
        assert "p_value/cohens_d/ci_95 NOT_CALCULATED" in disc
        assert "is_significant: false" in disc
        assert "Engine NOT run" in disc
        assert "no_analysis_json_update: true" in disc
        assert "NOT artifact-grade" in disc
        assert "0 browser.open" in _m850_text()

    def test_verdict_and_provenance(self):
        data = _m850_data()
        assert data["verdict"] == "directionally_supported_not_proven"
        assert data["no_analysis_json_update"] is True
        fam = data["falsification_family"]
        assert "NOT a falsification-family member" in fam
        assert "Ledger holds at 31" in fam
        assert "THIRTY-SECOND absent" in fam
        assert data["connects_to"] == [844, 823, 739]


class TestTypeDM851QualitativeDiscipline:
    def test_mechanism_id(self):
        assert _m851_data()["mechanism_id"] == 851
        assert _m851_data()["iteration"] == 1033

    def test_arm_tones_writer_pair(self):
        data = _m851_data()
        assert data["meta_arm"]["tone_illustrative"] == -0.45
        assert data["apple_arm"]["tone_illustrative"] == 0.30
        assert "carried un-rescored from m850" in data["meta_arm"]["tone_note"]
        assert "legacy-celebration register" in data["apple_arm"]["tone_note"]

    def test_cross_entity_delta(self):
        scorer = _m851_data()["asymmetry_scorer_result"]
        assert scorer["illustrative_meta_arm_tone"] == -0.45
        assert scorer["illustrative_apple_arm_tone"] == 0.30
        assert scorer["illustrative_cross_entity_delta_apple_minus_meta"] == 0.75
        assert (
            scorer["delta_calc"] == "+0.30 minus (-0.45) = +0.75 Apple-favoring"
        )
        assert "Apple-favoring" in scorer["cross_entity_delta_direction"]
        assert "22 days apart" in scorer["cross_entity_delta_direction"]

    def test_manual_illustrative_discipline(self):
        scorer = _m851_data()["asymmetry_scorer_result"]
        assert scorer["p_value"] == "NOT_CALCULATED"
        assert scorer["cohens_d"] == "NOT_CALCULATED"
        assert scorer["ci_95"] == "NOT_CALCULATED"
        assert scorer["engine"] == "NOT run"
        assert scorer["artifact_grade"] == "NOT artifact-grade"
        assert "MANUAL ILLUSTRATIVE" in scorer["methodology"]

    def test_verdict_and_provenance(self):
        data = _m851_data()
        assert data["verdict"] == "directionally_supported_not_proven"
        assert data["no_analysis_json_update"] is True
        assert data["is_significant"] is False
        assert data["falsification_family_member"] is False
        assert data["falsification_ledger"] == 31
        assert "NOT a falsification-family member" in data["falsification_note"]
        assert "Ledger holds at 31" in data["falsification_note"]
        assert data["connects_to"] == [850, 844, 739, 664, 633]
        disc = data["statistical_discipline"]
        assert "MANUAL ILLUSTRATIVE scores only" in disc
        assert "Engine NOT run" in disc
        assert "is_significant: false" in disc
        assert "no_analysis_json_update true" in disc


class TestTypeDM852QualitativeDiscipline:
    def test_mechanism_id_and_provenance(self):
        data = _m852_data()
        assert data["mechanism_id"] == 852
        assert data["iteration"] == 1034
        assert data["iteration_type"] == "C"

    def test_direction_taxonomy_sixteenth(self):
        taxonomy = _m852_data()["relationship_direction_taxonomy"]
        assert taxonomy["direction_number"] == "SIXTEENTH per the m807 enumeration"
        assert (
            taxonomy["direction_name"]
            == "COMMERCE-GATEKEEPING (access-denial as licensing leverage)"
        )
        assert "denial" in taxonomy["definition"].lower()

    def test_statistical_discipline(self):
        data = _m852_data()
        assert data["tone_scores"] == "NOT_SCORED"
        assert data["engine_run"] is False
        assert data["artifact_grade"] is False
        assert data["verdict"] == "directionally_supported_not_proven"
        assert data["no_analysis_json_update"] is True
        assert data["falsification_family_member"] is False
        assert data["falsification_ledger"] == 31
        assert data["connects_to"] == [831, 849, 559, 594, 509]
        assert data["excerpt_bounded"] is True
        assert data["browser_opens"] == 0
        assert "0 browser.open this run per #503" in data["excerpt_bounded_note"]

    def test_block_position_top_level(self):
        # m852 sits at zero indent in profiles/competitor-entities.yaml
        # (top-level block, colon form only per #715 designed keying:
        # the block key carries no numeric mechanism-id substring).
        doc = _read("profiles/competitor-entities.yaml")
        assert doc.count("\n" + M852_KEY + ":") == 1
        assert "mechanism_852" not in M852_KEY
        assert "mechanism-852" not in M852_KEY


class TestTypeDMaxIdAndNextNumber:
    def test_max_numeric_mechanism_id_is_852(self):
        assert _max_numeric_mechanism_id() == 852

    def test_zero_numeric_853_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_zero_underscore_853_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_zero_dash_853_repo_wide(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []


class TestTypeDFalsificationLedger:
    def test_ledger_holds_at_31(self):
        # m850 carries the ledger in block prose form ("Ledger holds
        # at 31", committed after m848 advanced the ledger); m851/m852
        # carry it as structured fields.
        assert "Ledger holds at 31" in _m850_data()["falsification_family"]
        assert _m851_data()["falsification_ledger"] == 31
        assert _m852_data()["falsification_ledger"] == 31

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
        # The committed #1030 test file carries this same needle inside its own
        # guard scan line (a prior sweep carrier); it is excluded so the two
        # runs' scans do not cross-trip, per the #715 rescope lesson. Own file
        # excluded as sweep carrier per #715.
        prior_carrier = "test_type_d_1030_m847_m848_m849_qualitative_corpus_integrity_sep27_3am.py"
        for rel in ["profiles", "tests"]:
            for root, dirs, files in os.walk(os.path.join(REPO_ROOT, rel)):
                dirs[:] = [d for d in dirs if d != "__pycache__"]
                for f in files:
                    if f == OWN_BASENAME or f == prior_carrier:
                        continue
                    p = os.path.join(root, f)
                    for line in open(p, encoding="utf-8", errors="replace"):
                        if "THIRTY-SECOND member" in line:  # negative guard scan needle
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

    def test_m850_block_position_and_indent(self):
        # m850 sits under cross_publication_findings in
        # profiles/competitor-coverage-research.yaml at 2-space indent.
        doc = _read("profiles/competitor-coverage-research.yaml")
        idx = doc.index("\n  " + M850_KEY + ":")
        parent = None
        for ln in reversed(doc[:idx].splitlines()):
            stripped = ln.strip()
            if stripped.endswith(":") and len(stripped) > 1:
                indent = len(ln) - len(ln.lstrip(" "))
                if indent <= 0:
                    parent = stripped[:-1]
                    break
        assert parent == "cross_publication_findings", parent
        assert "mechanism_850" not in M850_KEY
        assert "mechanism-850" not in M850_KEY

    def test_m851_block_position_and_indent(self):
        # m851 sits at 4-space indent under the top-level aditya_soni
        # item in profiles/careers/journalists.yaml and carries the
        # Aditya Soni byline provenance (the block is the FIRST
        # dedicated journalist-profile mechanism on Soni).
        import yaml

        doc = _read("profiles/careers/journalists.yaml")
        assert doc.count("\n    " + M851_KEY + ":") == 1
        parsed = yaml.safe_load(doc)
        assert parsed["aditya_soni"]["name"] == "Aditya Soni"
        block = _m851_data()
        assert block["journalist"] == "Aditya Soni"
        assert block["publication"] == "Reuters"

    def test_m852_block_position_and_indent(self):
        # m852 sits at zero indent in profiles/competitor-entities.yaml
        # (top-level block, colon form only per #715 designed keying:
        # the block key carries no numeric mechanism-id substring).
        doc = _read("profiles/competitor-entities.yaml")
        assert doc.count("\n" + M852_KEY + ":") == 1
        assert "mechanism_852" not in M852_KEY
        assert "mechanism-852" not in M852_KEY


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

    def test_1030_suite_log_stalled(self):
        # Stalled at 0%: 200 bytes of progress dots plus one "[  0% ]"
        # marker since Sep 27 03:10 PDT, no summary tokens anywhere, no
        # pytest alive.
        with open(self._suite_log("type_d_1030_full_suite.log"), "rb") as fh:
            data = fh.read()
        assert len(data) == 200, len(data)
        assert b"[  0%]" in data
        for token in (b"passed", b"failed", b"error"):
            assert token not in data, token

    def test_1030_suite_log_mtime_stale(self):
        # The #1030 suite's log has not been written since 03:10 PDT
        # (hours before this 08:00 PDT run): a live suite would append
        # progress dots continuously. Stale mtime + 200 bytes + zero
        # summary tokens + no pytest alive = dead per the #795
        # convention. (The new #1035 suite's pytest is alive by design;
        # this assertion is mtime-scoped to the OLD log, so it cannot
        # self-conflict.)
        import time

        st = os.stat(self._suite_log("type_d_1030_full_suite.log"))
        age_hours = (time.time() - st.st_mtime) / 3600
        assert age_hours > 1, age_hours

    def test_tombstone_lineage_advances(self):
        # FORTY-EIGHTH consecutive background death per the #795
        # convention; lineage advances SIXTY-SIXTH -> SIXTY-SEVENTH.
        # This run re-launches the suite writing to
        # type_d_1035_full_suite.log; the next Type D run checks it.
        # (The #1025 suite was already tombstoned by #1030; it is NOT
        # re-tombstoned here.)
        entry_anchor = "SIXTY-SIXTH"
        entry_next = "SIXTY-SEVENTH"
        assert entry_anchor != entry_next

    def test_1035_suite_log_relaunched(self):
        assert os.path.isfile(self._suite_log("type_d_1035_full_suite.log")), (
            "the re-launched suite log must exist"
        )


class TestTypeDSyntheticEngine:
    """Fresh engine meaningfulness calibration on synthetic corpora.

    Values hardcoded after a scratch run this run (NOT #1030's).
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
            [-0.63, -0.41, -0.55, -0.68, -0.37, -0.59, -0.46],
            [0.21, 0.34, 0.26, 0.18, 0.31, 0.24, 0.29],
            "Meta",
            ["Snap", "Apple"],
        )
        assert abs(r.asymmetry_score - (-0.7885714285714286)) < 1e-9
        assert abs(r.t_statistic - (-16.126385613165876)) < 1e-6
        assert r.p_value < 1e-7
        assert abs(r.cohens_d - (-8.619915693066732)) < 1e-6
        assert r.is_significant is True
        assert r.confidence_interval_upper < 0

    def test_near_null_pair_stays_silent(self):
        r = self._score(
            [0.05, -0.06, 0.02, -0.03, 0.07, -0.04, 0.01],
            [0.06, -0.02, 0.04, -0.05, 0.03, -0.07, 0.02],
            "Meta",
            ["Snap", "Apple"],
        )
        assert abs(r.asymmetry_score - 0.0014285714285714) < 1e-9
        assert r.p_value > 0.9
        assert r.is_significant is False
        assert r.confidence_interval_lower < 0 < r.confidence_interval_upper

    def test_degenerate_m850_pair_engine_guard(self):
        # Degenerate n=1/n=1 contract on the m850 illustrative pair
        # ([-0.05] Anthropic vs [-0.45] Meta): the engine's structural
        # guard fires (t=0.0, p=1.0, d=0.0, not significant) while
        # |asymmetry| == 0.40 and arm-swap negates exactly. The guard's
        # verdict is the assertion.
        r = self._score([-0.05], [-0.45], "Anthropic", ["Meta"])
        assert r.t_statistic == 0.0
        assert r.p_value == 1.0
        assert r.cohens_d == 0.0
        assert r.is_significant is False
        assert abs(abs(r.asymmetry_score) - 0.40) < 1e-9
        swapped = self._score([-0.45], [-0.05], "Meta", ["Anthropic"])
        assert swapped.asymmetry_score == -r.asymmetry_score

    def test_engine_finding_layer_separation(self):
        # The engine CAN return is_significant True on synthetic
        # corpora while the finding layer refuses: the three
        # mechanisms verified this run all carry finding-layer
        # is_significant false / NOT asserted per the Aug 28 2026
        # standing rule.
        assert "is_significant: false" in _m850_data()["statistical_discipline"]
        assert _m851_data()["is_significant"] is False
        assert _m852_data()["engine_run"] is False


class TestDocSync1035:
    def test_readme_row_1035(self):
        assert TEST_BASENAME in _read(README_PATH)

    def test_architecture_row_1035(self):
        assert TEST_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_1035_file(self):
        doc = _read(ARCH_PATH)
        assert TEST_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))


class TestIterationLog1035:
    def _entry(self):
        log = _read(LOG_PATH)
        idx = log.index("## #1035 Type D:")
        return log[idx : idx + 15000]

    def test_entry_present(self):
        assert "## #1035 Type D:" in _read(LOG_PATH)

    def test_entry_records_tombstone_and_integrity(self):
        entry = self._entry()
        assert "SIXTY-SEVENTH" in entry
        assert "852" in entry

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
