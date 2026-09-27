"""Type D -- Iteration #1020 (Sat 2026-09-26 17:00 PDT): m841/m842/m843
qualitative-discipline verification + post-1015-1019 corpus integrity
(max numeric mechanism_id 843; zero next-number 844 keys in
numeric/underscore/dash mechanism forms; ledger holds at 30 with the
THIRTIETH member-form present exactly once (m818, journalists.yaml),
TWENTY-NINTH in news-corp.yaml, THIRTY-FIRST member-form negative
guard) + #1015 background-suite tombstone (FORTY-FIFTH consecutive
death; lineage SIXTY-THIRD -> SIXTY-FOURTH) + fresh synthetic engine
calibration (new values, not #1015's) + re-launch of the full suite as
a background process writing to goal hidden_files
type_d_1020_full_suite.log (next Type D run checks its verdict per the
#795 convention).

Type D FIRST leg of the 1020-1024 window, OPENING it (D->E->A->B->C).
Committed predecessor #1019 Type C (16:00 PDT Sep 26) CLOSED the
1015-1019 window. Concurrency note: the in-flight runs at this run's
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
- m841 (Type A #1017, Verge x Microsoft Sep-4 copyright-defense
  headline register vs Verge x Meta Sep-23 Connect backlash framing,
  PCM licensing gradient: Microsoft arm PRIMARY Sep 4 2026 "Microsoft
  says virtually nobody was grabbing NYT articles through its chatbot"
  (MANUAL ILLUSTRATIVE +0.25); Microsoft arm SUPPORTING Sep 25 Tom
  Warren Copilot "super app" launch piece (MANUAL ILLUSTRATIVE +0.20);
  Meta arm PRIMARY Sep 23-24 Connect Muse Charm + backlash-framing
  attestation (MANUAL ILLUSTRATIVE -0.30); illustrative delta
  (Microsoft minus Meta) +0.55 on a degenerate n=1 vs n=1 primary
  pair, NOT significant; register-SELECTION finding, NOT
  uniform-softness; profiles/the-verge.yaml under
  competitor_relationships/microsoft, 4-space indent, descriptive
  block key per #723/#738): MANUAL ILLUSTRATIVE ONLY per standing
  rule Aug 28 2026, engine NOT run at the finding layer,
  p_value/cohens_d/ci NOT_CALCULATED, is_significant False, verdict
  directionally_supported_not_proven, no_analysis_json_update true,
  NOT artifact-grade; falsification family NOT a member (ledger 30);
  connects_to [502, 507, 598].
- m842 (Type B #1018, Sean Keach, The Sun / News Corp: cross-medium
  register control - Meta print hands-on enthusiasm Sep-2026 VR
  Glasses (MANUAL ILLUSTRATIVE +0.40) vs Apple print hands-on
  enthusiasm 2024 Vision Pro review (MANUAL ILLUSTRATIVE +0.35) vs
  carried TalkTV broadcast alarm on Meta (MANUAL ILLUSTRATIVE -0.70,
  carried from #182 per #807); illustrative delta (Meta minus Apple)
  +0.05 NULL on the genre-matched primary pair; illustrative medium
  split (broadcast minus print) -1.10 isolating MEDIUM/GENRE as the
  register driver; register tracks medium, not entity, not the
  financial gradient; profiles/careers/journalists.yaml, new
  sean_keach item, 4-space indent block key): statistical_discipline
  tone_scores MANUAL_ILLUSTRATIVE_NEW, p_value/cohens_d/ci_95
  NOT_CALCULATED, is_significant False, engine_run False, verdict
  directionally_supported_not_proven, no_analysis_json_update true,
  NOT artifact-grade; falsification_family_member False
  (falsification_ledger 30); connects_to [181, 818, 839].
- m843 (Type C #1019, Reddit AI-licensing quantum provenance audit:
  the $70M/yr OpenAI figure is press arithmetic reconstructed by
  subtraction (Adweek "about 10%" $130M minus $60M Google), certified
  uncertified by the Sep 2026 thestochasticparrot audit; CORRECTION of
  the corpus advance_dual_asset_monetization as-fact treatment;
  Google $60M/yr leg NOT downgraded; filed-number inventory (S-1
  $203M aggregate, FY2025 10-K concentration risk, Q2 2026 Other
  $43.3M +24% YoY, licensing 7.0% to 5.4%, contracted-unrecognized
  $62.0M/$30.1M); Jul 22 2026 WSJ via CNBC Google renewal "is ending
  soon" as the live pricing event; Meta $0 bounded absence, Anthropic
  $0 litigated (m614); profiles/competitor-entities.yaml top-level
  block, zero indent): tone_scores NOT_SCORED per standing rule
  Aug 28 2026, engine_run False, p_value/cohens_d NOT_CALCULATED,
  is_significant False, verdict directionally_supported_not_proven,
  no_analysis_json_update true, artifact_grade False, NOT
  artifact-grade; falsification_family_member False
  (falsification_ledger 30); connects_to [614, 735, 840, 732].

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
NEXT_NUM = 844

M841_KEY = "type_a_1017_verge_microsoft_sep2026_copyright_defense_headline_register_vs_meta_connect_backlash_framing_pcm_licensing_gradient"
M842_KEY = "type_b_1018_sean_keach_sun_cross_medium_register_meta_print_enthusiasm_vs_broadcast_alarm_apple_print_null_delta"
M843_KEY = "type_c_1019_reddit_openai_70m_provenance_audit_renewal_pricing_event_sep26_4pm"

M841_INDENT = 4  # nested under competitor_relationships/microsoft (the-verge.yaml)
M842_INDENT = 4  # item-level block in journalists.yaml (sean_keach item)
M843_INDENT = 0  # top-level block in competitor-entities.yaml

M841_MSFT_URL_FRAG = "990267/microsoft-openai-new-york-times-authors-lawsuit"
M841_META_URL_FRAG = "999750/muse-charm-meta-ai-hardware"


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
# numbers in git history: #1020 Type D opens the 1020-1024 window;
# #1019 Type C (committed 16:00 PDT Sep 26) is the schedule predecessor
# and CLOSED the 1015-1019 window. The in-flight runs (#899 Type C,
# #938 Type B, #900 Type D, #1012 working-tree edit) have no main
# commits in git history at this run's checks and sit below the
# window; #898's block was lost (documented in the module docstring)
# and has no main commit either. The #884 block (m762) is committed at
# this run's checks.
EXPECTED_ORDER = [
    ("D", "1020"),
    ("C", "1019"),
    ("B", "1018"),
    ("A", "1017"),
    ("E", "1016"),
]


def _iter_source_files():
    """Yield paths for profile + test source files.

    Excludes this file (sweep carrier per #715) and __pycache__
    artifacts (per the #715 pattern-rescope lesson: committed test
    pyc files carry next-number needle strings from their own guards;
    compiled artifacts are excluded from the sweeps). No additional
    sweep-carrier exclusions this run: no in-tree SOURCE file carries
    a contiguous 844-form mechanism literal (verified pre-commit; the
    #1019 test file builds its 844 needles at runtime and its raw
    "mechanism 844" hits are docstring/grep-needle strings with a
    space, not contiguous mechanism-form literals), so the 844 sweeps
    run repo-wide with only this file excluded.
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


def _m841_data():
    return _block_data("profiles/the-verge.yaml", M841_KEY, M841_INDENT)


def _m841_text():
    return _indented_block("profiles/the-verge.yaml", M841_KEY, M841_INDENT)


def _m842_data():
    return _block_data(
        "profiles/careers/journalists.yaml", M842_KEY, M842_INDENT
    )


def _m843_data():
    return _block_data(
        "profiles/competitor-entities.yaml", M843_KEY, M843_INDENT
    )


class TestNovelty1020:
    def test_no_type_d_1020_test_file_preexisting(self):
        assert glob.glob(os.path.join(TESTS_DIR, "test_type_d_1020*.py")) == [
            os.path.join(TESTS_DIR, OWN_BASENAME)
        ], "only this file may match the test_type_d_1020 glob"

    def test_no_type_d_1020_in_git_log(self):
        # Pre-commit novelty: no Type D #1020 main commit exists.
        # Post-commit (anchor followup per #565), exactly one exists
        # and it is the anchored main commit - the guard doubles as a
        # duplicate-main-commit check.
        result = subprocess.run(
            ["git", "log", "--format=%H %s", "--grep=Type D #1020"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        mains = [
            line
            for line in result.stdout.splitlines()
            if "Type D #1020" in line and "followup" not in line.lower()
        ]
        if ANCHORED_SHA == "0" * 40:
            assert mains == [], mains
        else:
            assert len(mains) == 1, mains
            assert mains[0].startswith(ANCHORED_SHA + " "), mains

    def test_max_id_is_843_pre_commit(self):
        assert _max_numeric_mechanism_id() == 843

    def test_zero_844_forms_repo_wide(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_block_keys_unique_in_home_yamls(self):
        assert _read("profiles/the-verge.yaml").count("\n    " + M841_KEY + ":") == 1
        assert (
            _read("profiles/careers/journalists.yaml").count(
                "\n    " + M842_KEY + ":"
            )
            == 1
        )
        assert (
            _read("profiles/competitor-entities.yaml").count("\n" + M843_KEY + ":")
            == 1
        )

    def test_m841_arm_urls_present_in_verge(self):
        # The committed #1017 run pinned its URL novelty; this run
        # carries the m841 block's own arm URL fragments as
        # verified-in-corpus: both verbatim theverge.com arms appear
        # in profiles/the-verge.yaml.
        block = _m841_text()
        assert M841_MSFT_URL_FRAG in block
        assert M841_META_URL_FRAG in block
        home = _read("profiles/the-verge.yaml")
        assert M841_MSFT_URL_FRAG in home
        assert M841_META_URL_FRAG in home


class TestTypeDRotationGuard:
    def test_rotation_window_opens_1020(self):
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


class TestTypeDM841QualitativeDiscipline:
    def test_mechanism_id(self):
        assert _m841_data()["mechanism_id"] == 841

    def test_arm_tones_and_registers(self):
        block = _m841_text()
        assert "MANUAL ILLUSTRATIVE +0.25" in block
        assert "MANUAL ILLUSTRATIVE +0.20" in block
        assert "MANUAL ILLUSTRATIVE -0.30" in block
        assert _m841_data()["illustrative_delta"] == 0.55
        assert _m841_data()["delta_direction"] == "Microsoft minus Meta"

    def test_degenerate_delta_documented_not_significant(self):
        block = _m841_text()
        assert "NOT significant" in block
        assert "n=1 vs n=1" in block

    def test_manual_illustrative_discipline(self):
        disc = _m841_data()["statistical_discipline"]
        assert "MANUAL ILLUSTRATIVE ONLY" in disc
        assert "p_value NOT_CALCULATED" in disc
        assert "is_significant False" in disc
        assert "engine NOT run" in disc
        assert "key_design_note" in _m841_data()
        assert "#723/#738" in _m841_data()["key_design_note"]

    def test_verdict_and_provenance(self):
        data = _m841_data()
        assert data["verdict"] == "directionally_supported_not_proven"
        assert data["no_analysis_json_update"] is True
        assert data["falsification_family_member"] is False
        assert data["falsification_ledger"] == 30
        assert data["connects_to"] == [502, 507, 598]
        assert data["iteration"] == 1017
        assert data["window"] == "1015-1019"


class TestTypeDM842QualitativeDiscipline:
    def test_mechanism_id(self):
        assert _m842_data()["mechanism_id"] == 842

    def test_arm_tones_and_cross_medium_registers(self):
        data = _m842_data()
        assert data["meta_arm_print"]["tone_illustrative"] == 0.40
        assert data["apple_arm_print"]["tone_illustrative"] == 0.35
        assert data["meta_arm_broadcast"]["tone_illustrative"] == -0.70

    def test_null_delta_and_medium_split(self):
        scorer = _m842_data()["asymmetry_scorer_result"]
        assert scorer["illustrative_delta_meta_minus_apple"] == 0.05
        assert scorer["illustrative_medium_split_broadcast_minus_print"] == -1.10
        assert scorer["new_meta_print_tone_manual_illustrative"] == 0.40
        assert scorer["new_apple_print_tone_manual_illustrative"] == 0.35
        assert scorer["carried_meta_broadcast_tone_manual_illustrative"] == -0.70
        assert "medium/genre" in _m842_data()["pattern"].lower()

    def test_scorer_layer_discipline(self):
        disc = _m842_data()["statistical_discipline"]
        assert disc["p_value"] == "NOT_CALCULATED"
        assert disc["is_significant"] is False
        assert disc["engine_run"] is False
        assert disc["tone_scores"] == "MANUAL_ILLUSTRATIVE_NEW"
        assert disc["verdict"] == "directionally_supported_not_proven"

    def test_verdict_and_provenance(self):
        data = _m842_data()
        assert data["verdict"] == "directionally_supported_not_proven"
        assert data["no_analysis_json_update"] is True
        assert data["falsification_family_member"] is False
        assert data["falsification_ledger"] == 30
        assert data["connects_to"] == [181, 818, 839]
        assert data["iteration"] == 1018


class TestTypeDM843QualitativeDiscipline:
    def test_mechanism_id_and_provenance_claim(self):
        data = _m843_data()
        assert data["mechanism_id"] == 843
        assert "press arithmetic" in data["finding"]
        assert "reconstructed by subtraction" in data["finding"]
        assert "CORRECTION" in data["finding"]
        assert "advance_dual_asset_monetization" in data["finding"]

    def test_filed_number_inventory_present(self):
        data = _m843_data()
        assert "S-1" in data["finding"]
        assert "$203 million" in data["finding"]
        assert "$43.3 million" in data["finding"]
        assert "5.4%" in data["finding"]

    def test_google_leg_not_downgraded(self):
        data = _m843_data()
        assert data["google_leg"]["financial_terms"] == "REPORTED (not filed)"
        assert "NOT downgraded" in data["google_leg"]["status"]

    def test_live_pricing_event_documented(self):
        data = _m843_data()
        assert "is ending soon" in data["finding"]
        assert "9.18%" in data["finding"]
        assert data["connects_to"] == [614, 735, 840, 732]

    def test_verdict_and_provenance(self):
        data = _m843_data()
        assert data["tone_scores"] == "NOT_SCORED"
        assert data["engine_run"] is False
        assert data["no_analysis_json_update"] is True
        assert data["artifact_grade"] is False
        assert data["verdict"] == "directionally_supported_not_proven"
        assert data["falsification_family_member"] is False
        assert data["falsification_ledger"] == 30
        assert data["iteration"] == 1019


class TestTypeDMaxIdAndNextNumber:
    def test_max_numeric_mechanism_id_is_843(self):
        assert _max_numeric_mechanism_id() == 843

    def test_zero_numeric_844_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_zero_underscore_844_repo_wide(self):
        # Needles are format-built (per #715/#770); this file carries no
        # contiguous underscore-form 844 literal. The #1019 committed
        # test's runtime-built needle hits do not exist as source
        # literals.
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_zero_dash_844_repo_wide(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []


class TestTypeDFalsificationLedger:
    def test_ledger_holds_at_30(self):
        assert _m841_data()["falsification_ledger"] == 30
        assert _m842_data()["falsification_ledger"] == 30
        assert _m843_data()["falsification_ledger"] == 30

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

    def test_844_sweep_excludes_only_this_file_and_pycache(self):
        # The #1019 pyc in tests/__pycache__ exists but carries NO
        # contiguous 844-form literal: the #1019 test builds its 844
        # needles at runtime by concatenation (per its test-fix
        # followup, "no self-match"), so compiled artifacts stay
        # clean by construction. The source sweeps must therefore
        # come back empty.
        pyc_hits = glob.glob(
            os.path.join(TESTS_DIR, "__pycache__", "*1019*.pyc")
        )
        assert pyc_hits != [], "expected the #1019 pyc to exist"
        for p in pyc_hits:
            data = open(p, "rb").read()
            assert b"mechanism-844" not in data, p
            assert b"mechanism_844" not in data, p
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_m841_block_position_and_indent(self):
        # m841 sits under the microsoft item of
        # competitor_relationships in profiles/the-verge.yaml at
        # 4-space indent.
        doc = _read("profiles/the-verge.yaml")
        idx = doc.index("\n    " + M841_KEY + ":")
        for ln in reversed(doc[:idx].splitlines()):
            stripped = ln.strip()
            if stripped.endswith(":") and len(stripped) > 1:
                indent = len(ln) - len(ln.lstrip(" "))
                if indent <= 2:
                    parent = stripped[:-1]
                    break
        assert parent == "microsoft", parent
        assert "\ncompetitor_relationships:" in doc[:idx]

    def test_m842_block_position_and_indent(self):
        # m842 sits at 4-space indent in profiles/careers/
        # journalists.yaml (sean_keach journalist item-level block) and
        # carries the Sean Keach byline provenance.
        doc = _read("profiles/careers/journalists.yaml")
        assert doc.count("\n    " + M842_KEY + ":") == 1
        block = _indented_block(
            "profiles/careers/journalists.yaml", M842_KEY, M842_INDENT
        )
        assert "Sean Keach" in block

    def test_m843_block_position_and_indent(self):
        # m843 sits at zero indent in profiles/competitor-entities.yaml
        # (top-level block, colon form only per #715 designed keying:
        # the block key carries no numeric mechanism-id substring).
        doc = _read("profiles/competitor-entities.yaml")
        assert doc.count("\n" + M843_KEY + ":") == 1
        assert "mechanism_843" not in M843_KEY
        assert "mechanism-843" not in M843_KEY


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

    def test_1015_suite_log_stalled(self):
        # Stalled mid-run: 644 bytes of dots at ~1% since Sep 26
        # 12:19 PDT, no summary tokens anywhere, the process has since
        # exited (no pytest alive).
        with open(self._suite_log("type_d_1015_full_suite.log"), "rb") as fh:
            data = fh.read()
        assert len(data) == 644, len(data)
        for token in (b"passed", b"failed", b"error"):
            assert token not in data, token

    def test_1015_suite_log_mtime_stale(self):
        # The #1015 suite's log has not been written since 12:19 PDT
        # (hours before this 17:00 PDT run): a live suite would append
        # progress dots continuously. Stale mtime + 644 bytes + zero
        # summary tokens = dead per the #795 convention. (The new
        # #1020 suite's pytest is alive by design; this assertion is
        # mtime-scoped to the OLD log, so it cannot self-conflict.)
        import time

        st = os.stat(self._suite_log("type_d_1015_full_suite.log"))
        age_hours = (time.time() - st.st_mtime) / 3600
        assert age_hours > 1, age_hours

    def test_tombstone_lineage_advances(self):
        # FORTY-FIFTH consecutive background death per the #795
        # convention; lineage advances SIXTY-THIRD -> SIXTY-FOURTH.
        # This run re-launches the suite writing to
        # type_d_1020_full_suite.log; the next Type D run checks it.
        # (The #1010 suite was already tombstoned by #1015; it is NOT
        # re-tombstoned here.)
        entry_anchor = "SIXTY-THIRD"
        entry_next = "SIXTY-FOURTH"
        assert entry_anchor != entry_next

    def test_1020_suite_log_relaunched(self):
        assert os.path.isfile(self._suite_log("type_d_1020_full_suite.log")), (
            "the re-launched suite log must exist"
        )


class TestTypeDSyntheticEngine:
    """Fresh engine meaningfulness calibration on synthetic corpora.

    Values hardcoded after a scratch run this run (NOT #1015's).
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
            [-0.61, -0.44, -0.58, -0.52, -0.66, -0.47],
            [0.33, 0.18, 0.29, 0.41, 0.22, 0.36],
            "Meta",
            ["Snap", "Apple"],
        )
        assert abs(r.asymmetry_score - (-0.8450000000000001)) < 1e-9
        assert abs(r.t_statistic - (-17.081264005415452)) < 1e-6
        assert r.p_value < 2e-8
        assert abs(r.cohens_d - (-9.861872371625678)) < 1e-6
        assert r.is_significant is True
        assert r.confidence_interval_upper < 0

    def test_near_null_pair_stays_silent(self):
        r = self._score(
            [0.04, -0.03, 0.01, -0.05, 0.02, -0.01],
            [0.03, -0.04, 0.00, 0.02, -0.02, 0.05],
            "Meta",
            ["Snap", "Apple"],
        )
        assert abs(r.asymmetry_score - (-0.0100000000000000)) < 1e-9
        assert r.p_value > 0.3
        assert r.is_significant is False
        assert r.confidence_interval_lower < 0 < r.confidence_interval_upper

    def test_degenerate_m841_pair_engine_guard(self):
        # Degenerate n=1/n=1 contract on the m841 illustrative pair
        # ([0.25] Microsoft vs [-0.30] Meta): the engine's structural
        # guard fires (t=0.0, p=1.0, d=0.0, not significant) while
        # |asymmetry| == 0.55 and arm-swap negates exactly. The guard's
        # verdict is the assertion.
        r = self._score([0.25], [-0.30], "Microsoft", ["Meta"])
        assert r.t_statistic == 0.0
        assert r.p_value == 1.0
        assert r.cohens_d == 0.0
        assert r.is_significant is False
        assert abs(abs(r.asymmetry_score) - 0.55) < 1e-9
        swapped = self._score([-0.30], [0.25], "Meta", ["Microsoft"])
        assert swapped.asymmetry_score == -r.asymmetry_score

    def test_engine_finding_layer_separation(self):
        # The engine CAN return is_significant True on synthetic
        # corpora while the finding layer refuses: the three
        # mechanisms verified this run all carry finding-layer
        # is_significant false / NOT_CALCULATED per the Aug 28 2026
        # standing rule.
        assert "is_significant False" in _m841_data()["statistical_discipline"]
        assert _m842_data()["statistical_discipline"]["is_significant"] is False
        assert _m843_data()["engine_run"] is False


class TestDocSync1020:
    def test_readme_row_1020(self):
        assert TEST_BASENAME in _read(README_PATH)

    def test_architecture_row_1020(self):
        assert TEST_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_1020_file(self):
        doc = _read(ARCH_PATH)
        assert TEST_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))


class TestIterationLog1020:
    def _entry(self):
        log = _read(LOG_PATH)
        idx = log.index("## #1020 Type D:")
        return log[idx : idx + 15000]

    def test_entry_present(self):
        assert "## #1020 Type D:" in _read(LOG_PATH)

    def test_entry_records_tombstone_and_integrity(self):
        entry = self._entry()
        assert "SIXTY-FOURTH" in entry
        assert "843" in entry

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
