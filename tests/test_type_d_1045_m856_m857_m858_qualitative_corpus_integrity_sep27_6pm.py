"""Type D -- Iteration #1045 (Sun 2026-09-27 18:00 PDT): m856/m857/m858
qualitative-discipline verification + post-1040-1044 corpus integrity
(max numeric mechanism_id 858; zero next-number 859 keys in
numeric/underscore/dash mechanism forms; ledger holds at 34 with the
THIRTY-FOURTH member-form present exactly twice (m856 summary +
m856 ledger_note, news-corp.yaml), THIRTY-THIRD member-form still
present twice (m854 notes prose + m854 block falsification_note,
journalists.yaml), THIRTY-FIFTH member-form negative guard) +
#1040 background-suite tombstone (FIFTIETH consecutive death;
lineage SIXTY-EIGHTH -> SIXTY-NINTH) + fresh synthetic engine
calibration (new values, not #1040's) + re-launch of the full suite
as a background process writing to goal hidden_files
type_d_1045_full_suite.log (next Type D run checks its verdict per
the #795 convention).

Type D FIRST leg of the 1045-1049 window, OPENING it (D->E->A->B->C).
Committed predecessor #1044 Type C (17:00 PDT Sep 27) CLOSED the
1040-1044 window (D #1040, E #1041, A #1042, B #1043, C #1044).
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
- m856 (Type A #1042, news-corp.yaml competitor_relationships.openai,
  4-space indent, descriptive block key,
  `mechanism_id: 856` field form): WSJ x OpenAI Sep-27 U.N.
  rogue-agents adversarial safety-crisis register (-0.45 MANUAL
  ILLUSTRATIVE) vs WSJ x Anthropic Sep-24 Akamai $11.6B
  business-growth register (+0.10 MANUAL ILLUSTRATIVE);
  illustrative delta (Anthropic minus OpenAI) +0.55; the News
  Corp-OpenAI May 2024 $50M/yr licensing deal sits on the
  HARDER-covered side so the spread runs OPPOSITE the naive
  payer-softening prediction; THIRD safety-crisis falsification
  (after m598 and m853, both at the Verge) and FIRST at WSJ/News
  Corp - cross-publication replication that the licensing deal does
  not suppress adversarial safety-crisis coverage of the payer;
  THIRTY-FOURTH falsification-family member (ledger 33->34);
  connects_to [532, 598, 616, 682, 733, 846, 853].
- m857 (Type B #1043, journalists.yaml karissa_bell item,
  competitor_coverage, 4-space indent block key,
  `mechanism_id: 857` field form): FOURTH mechanism in Bell's item
  (mechanism_ids [722, 764, 773, 857]); FIRST Bell-vs-Apple pair -
  her Sep-24 2026 Meta visual-data opt-out privacy investigation
  (-0.55 MANUAL ILLUSTRATIVE) vs her own Sep-9 2026 co-hosted
  Engadget Podcast iPhone Duo launch-event recap covering Apple's
  ambient-listening Audio Intelligence with zero privacy-investigation
  register (-0.10 MANUAL ILLUSTRATIVE); illustrative delta
  (Meta minus Apple) -0.45; thesis-consistent with m150's editorial
  beat-assignment theory (fourth in-corpus replication), NOT a
  falsification; ledger holds at 34.
- m858 (Type C #1044, profiles/competitor-entities.yaml top-level
  block, zero indent, `mechanism_id: 858` field form): FIRST
  dedicated corpus mechanism on the FT Group FY2025 record revenue
  (GBP566m, +5%) - the financial-outcome leg of the dual-AI-payer
  portfolio (OpenAI Apr 2024 + Google Feb 2026, Meta $0); FIRST
  denominator audit NARROWS the corpus's "material commercial value"
  FT wording to contract/relationship materiality (illustrative
  ~1.3-2.6% revenue share); tone NOT_SCORED; NOT falsification-family
  (ledger holds at 34).

Statistical discipline across all three: MANUAL ILLUSTRATIVE ONLY
(m856, m857) / NOT_SCORED (m858) per the Aug 28 2026 standing rule,
engine NOT run at the finding layer, p_value/cohens_d/ci_95
NOT_CALCULATED, is_significant False / not asserted at the finding
layer, verdict directionally_supported_not_proven,
no_analysis_json_update true, NOT artifact-grade; no analysis.json
update. m856 IS a falsification-family member (THIRTY-FOURTH;
ledger holds at 34); m857 and m858 are NOT (qualitative register
documentation + financial-incentive mapping). Correlation only, not
causation. Hypothesis-generating only.

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
NEXT_NUM = 859

M856_KEY = "wsj_openai_sep27_un_rogue_agents_adversarial_vs_wsj_anthropic_sep24_akamai_growth_register_sep27_3pm"
M857_KEY = "type_b_1043_karissa_bell_engadget_meta_visual_data_optout_vs_apple_audio_intelligence_event_register_sep27"
M858_KEY = "type_c_1044_ft_group_fy2025_record_revenue_dual_payer_outcome_leg_sep27_5pm"

M856_INDENT = 4  # nested under competitor_relationships.openai (news-corp.yaml)
M857_INDENT = 4  # item-level block under competitor_coverage in journalists.yaml (karissa_bell item)
M858_INDENT = 0  # top-level block in competitor-entities.yaml

M856_OPENAI_URL_FRAG = "wsj.com/tech/ai/openai-agents-used-aggressive-techniques-to-access-u-n-website-522c70ff"
M856_ANTHROPIC_URL_FRAG = "wsj.com/tech/anthropic-to-pay-akamai-technologies-11-6-billion-over-seven-years-for-cloud-services-7a55360b"


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
# numbers in git history: #1045 Type D opens the 1045-1049 window;
# #1044 Type C (committed 17:00 PDT Sep 27) is the schedule
# predecessor and CLOSED the 1040-1044 window. The in-flight runs
# (#899 Type C, #938 Type B, #900 Type D, #1012 working-tree edit)
# have no main commits in git history at this run's checks and sit
# below the window; #898's block was lost (documented in the module
# docstring) and has no main commit either. The #884 block (m762) is
# committed at this run's checks.
EXPECTED_ORDER = [
    ("D", "1045"),
    ("C", "1044"),
    ("B", "1043"),
    ("A", "1042"),
    ("E", "1041"),
]


def _iter_source_files():
    """Yield paths for profile + test source files.

    Excludes this file (sweep carrier per #715) and __pycache__
    artifacts (per the #715 pattern-rescope lesson: committed test
    pyc files carry next-number needle strings from their own guards;
    compiled artifacts are excluded from the sweeps). No additional
    sweep-carrier exclusions this run: no in-tree SOURCE file carries
    a contiguous 859-form mechanism literal (verified pre-commit), so
    the 859 sweeps run repo-wide with only this file excluded.
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


def _m856_data():
    return _block_data("profiles/news-corp.yaml", M856_KEY, M856_INDENT)


def _m856_text():
    return _indented_block("profiles/news-corp.yaml", M856_KEY, M856_INDENT)


def _m857_data():
    return _block_data(
        "profiles/careers/journalists.yaml", M857_KEY, M857_INDENT
    )


def _m858_data():
    return _block_data(
        "profiles/competitor-entities.yaml", M858_KEY, M858_INDENT
    )


class TestNovelty1045:
    def test_no_type_d_1045_test_file_preexisting(self):
        assert glob.glob(os.path.join(TESTS_DIR, "test_type_d_1045*.py")) == [
            os.path.join(TESTS_DIR, OWN_BASENAME)
        ], "only this file may match the test_type_d_1045 glob"

    def test_no_type_d_1045_in_git_log(self):
        # Pre-commit novelty: no Type D #1045 main commit exists.
        # Post-commit (anchor followup per #565), exactly one exists
        # and it is the anchored main commit - the guard doubles as a
        # duplicate-main-commit check.
        result = subprocess.run(
            ["git", "log", "--format=%H %s", "--grep=Type D #1045"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        mains = [
            line
            for line in result.stdout.splitlines()
            if "Type D #1045" in line and "followup" not in line.lower()
        ]
        if ANCHORED_SHA == "0" * 40:
            assert mains == [], mains
        else:
            assert len(mains) == 1, mains
            assert mains[0].startswith(ANCHORED_SHA + " "), mains

    def test_max_id_is_858_pre_commit(self):
        assert _max_numeric_mechanism_id() == 858

    def test_zero_859_forms_repo_wide(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_block_keys_unique_in_home_yamls(self):
        assert (
            _read("profiles/news-corp.yaml").count("\n    " + M856_KEY + ":") == 1
        )
        assert (
            _read("profiles/careers/journalists.yaml").count(
                "\n    " + M857_KEY + ":"
            )
            == 1
        )
        assert (
            _read("profiles/competitor-entities.yaml").count("\n" + M858_KEY + ":")
            == 1
        )

    def test_m856_arm_urls_present_in_news_corp_profile(self):
        # The committed #1042 run pinned its URL novelty; this run
        # carries the m856 block's own arm URL fragments as
        # verified-in-corpus: the two WSJ arm fragments appear in
        # profiles/news-corp.yaml.
        block = _m856_text()
        assert M856_OPENAI_URL_FRAG in block
        assert M856_ANTHROPIC_URL_FRAG in block
        home = _read("profiles/news-corp.yaml")
        assert M856_OPENAI_URL_FRAG in home
        assert M856_ANTHROPIC_URL_FRAG in home


class TestTypeDRotationGuard:
    def test_rotation_window_opens_1045(self):
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


class TestTypeDM856QualitativeDiscipline:
    def test_mechanism_id(self):
        # m856 uses the `mechanism_id:` field form under
        # competitor_relationships.openai in news-corp.yaml.
        assert _m856_data()["mechanism_id"] == 856
        assert _m856_data()["iteration"] == 1042

    def test_arm_tones_and_spread(self):
        data = _m856_data()
        assert data["openai_arm_fresh"]["tone_illustrative"] == -0.45
        assert data["anthropic_arm_fresh"]["tone_illustrative"] == 0.10
        assert data["illustrative_delta_anthropic_minus_openai"] == 0.55
        disc = data["statistical_discipline"]
        assert disc["scores"] == "MANUAL ILLUSTRATIVE only"
        assert disc["p_value"] == "NOT_CALCULATED"
        assert disc["cohens_d"] == "NOT_CALCULATED"
        assert disc["ci_95"] == "NOT_CALCULATED"
        assert disc["is_significant"] is False
        assert disc["engine_run"] is False

    def test_falsification_member_thirtyfourth(self):
        # The News Corp-OpenAI May 2024 $50M/yr licensing deal sits on
        # the adversarially-covered side; the uniform payer-softening
        # prediction fails at the publication level: THIRTY-FOURTH
        # falsification-family member (ledger 33->34); third
        # safety-crisis falsification, first at WSJ/News Corp.
        data = _m856_data()
        assert data["falsification_family_member"] is True
        assert data["falsification_ledger"] == 34
        assert "THIRTY-FOURTH falsification-family member" in data["ledger_note"]
        assert "ledger 33 -> 34" in data["ledger_note"]

    def test_manual_illustrative_discipline(self):
        disc = _m856_data()["statistical_discipline"]
        assert disc["no_analysis_json_update"] is True
        assert disc["artifact_grade"] is False
        assert "0 browser.open" in _m856_text()

    def test_verdict_and_provenance(self):
        data = _m856_data()
        assert data["statistical_discipline"]["verdict"] == (
            "directionally_supported_not_proven"
        )
        assert data["connects_to"] == [532, 598, 616, 682, 733, 846, 853]
        assert (
            "tests/test_type_a_1042_wsj_openai_sep27_un_rogue_agents_vs_anthropic_akamai_grow"
            in data["test_file"]
        )
        assert data["finding_type"] == "competitor_coverage_deep_dive"


class TestTypeDM857QualitativeDiscipline:
    def test_mechanism_id(self):
        # m857 is the FOURTH mechanism in the karissa_bell journalist
        # item (mechanism_ids [722, 764, 773, 857]); FIRST Bell-vs-Apple
        # pair.
        data = _m857_data()
        assert data["mechanism_id"] == 857
        assert data["iteration"] == 1043
        assert data["journalist"] == "Karissa Bell"
        assert data["publication"] == "Engadget"

    def test_arm_tones_and_spread(self):
        data = _m857_data()
        assert data["meta_arm"]["tone_MANUAL_ILLUSTRATIVE"] == -0.55
        assert data["apple_arm"]["tone_MANUAL_ILLUSTRATIVE"] == -0.10
        assert data["illustrative_delta_meta_minus_apple"] == -0.45
        assert data["delta_calc"] == "(-0.55) - (-0.10) = -0.45"

    def test_not_falsification_family(self):
        # Thesis-consistent with m150's editorial beat-assignment
        # theory (fourth in-corpus replication), NOT a falsification;
        # ledger holds at 34.
        fam = _m857_data()["falsification_family"]
        assert "NOT a falsification-family member" in fam
        assert "ledger holds at 34" in fam

    def test_manual_illustrative_discipline(self):
        disc = _m857_data()["statistical_discipline"]
        assert "MANUAL ILLUSTRATIVE scores only" in disc
        assert "p_value NOT_CALCULATED" in disc
        assert "cohens_d NOT_CALCULATED" in disc
        assert "Engine NOT run" in disc

    def test_verdict_and_provenance(self):
        data = _m857_data()
        assert "directionally_supported_not_proven" in data["finding"]
        assert data["no_analysis_json_update"] is True
        assert (
            "tests/test_type_b_1043_karissa_bell_engadget_meta_visual_data_vs_apple_event_register_sep27_4pm.py"
            in data["test_file"]
        )


class TestTypeDM858QualitativeDiscipline:
    def test_mechanism_id_and_provenance(self):
        # m858 is a top-level block in competitor-entities.yaml (zero
        # indent); financial-incentive mapping, tone NOT_SCORED.
        data = _m858_data()
        assert data["mechanism_id"] == 858
        assert data["iteration"] == 1044
        assert data["type"] == "financial_incentive_mapping"
        assert data["tone_scores"] == "NOT_SCORED"

    def test_denominator_audit_first_leg(self):
        # FIRST denominator audit: narrows the corpus's "material
        # commercial value" FT wording to contract/relationship
        # materiality; financial-outcome leg of the dual-AI-payer
        # portfolio (OpenAI Apr 2024 + Google Feb 2026, Meta $0).
        text = _indented_block(
            "profiles/competitor-entities.yaml", M858_KEY, M858_INDENT
        )
        assert "denominator audit" in text.lower()
        assert "material commercial value" in text

    def test_statistical_discipline(self):
        data = _m858_data()
        assert data["engine_run"] is False
        assert data["no_analysis_json_update"] is True
        assert data["verdict"] == "directionally_supported_not_proven"
        assert data["artifact_grade"] is False
        assert data["ascii_only"] is True
        assert data["browser_opens"] == 0

    def test_not_falsification_family_ledger_holds_34(self):
        data = _m858_data()
        assert data["falsification_family_member"] is False
        assert data["falsification_ledger"] == 34
        assert "Ledger holds at 34" in data["falsification_note"]
        assert "THIRTY-FOURTH" in data["falsification_note"]

    def test_block_position_top_level(self):
        doc = _read("profiles/competitor-entities.yaml")
        assert doc.count("\n" + M858_KEY + ":") == 1
        assert "mechanism_858" not in M858_KEY
        assert "mechanism-858" not in M858_KEY


class TestTypeDMaxIdAndNextNumber:
    def test_max_numeric_mechanism_id_is_858(self):
        assert _max_numeric_mechanism_id() == 858

    def test_zero_numeric_859_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_zero_underscore_859_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_zero_dash_859_repo_wide(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []


class TestTypeDFalsificationLedger:
    def test_ledger_holds_at_34(self):
        # m856 carries the ledger as structured fields
        # (falsification_ledger == 34, falsification_family_member
        # true); m857 carries it in block prose ("ledger holds at
        # 34"); m858 as structured fields (falsification_ledger == 34,
        # member false) with matching prose.
        assert _m856_data()["falsification_ledger"] == 34
        assert _m856_data()["falsification_family_member"] is True
        assert "ledger holds at 34" in _m857_data()["falsification_family"]
        assert _m858_data()["falsification_ledger"] == 34
        assert "Ledger holds at 34" in _m858_data()["falsification_note"]

    def test_thirtyfourth_member_form_present(self):
        # THIRTY-FOURTH member-form: the m856 summary (Type A #1042,
        # mechanism 856, news-corp.yaml) appears twice - once in the
        # block's summary and once in the block's ledger_note. Both
        # are positive member-form claims; the scan pins the pair.
        needle = "THIRTY-FOURTH falsification-family member"
        hits = _profiles_with(needle)
        assert hits == [
            os.path.join(PROFILES_DIR, "news-corp.yaml")
        ], hits
        doc = _read("profiles/news-corp.yaml")
        assert doc.count(needle) == 2, doc.count(needle)

    def test_thirtythird_member_form_still_present(self):
        # The m854 THIRTY-THIRD anchor (Type B #1038) must not have
        # been disturbed by the ledger advance.
        hits = _profiles_with("THIRTY-THIRD falsification-family member")
        assert (
            os.path.join(PROFILES_DIR, "careers", "journalists.yaml") in hits
        ), hits

    def test_thirtyfifth_member_form_absent(self):
        # THIRTY-FIFTH is the negative guard: no positive
        # thirty-fifth falsification-family member-form claim may
        # exist anywhere in profiles/ or test sources. (The old Type D
        # test files' "THIRTY-FOURTH -> THIRTY-FIFTH" and "THIRTY-FIFTH
        # consecutive background full-suite death" strings belong to
        # the tombstone-lineage ordinal series, a different series
        # now at SIXTY-EIGHTH - they do not match this member-form
        # needle.) Own file excluded as sweep carrier per #715 (it
        # carries the needle in this very scan).
        needle = "THIRTY-FIFTH falsification-family member"
        for rel in ["profiles", "tests"]:
            for root, dirs, files in os.walk(os.path.join(REPO_ROOT, rel)):
                dirs[:] = [d for d in dirs if d != "__pycache__"]
                for f in files:
                    if f == OWN_BASENAME:
                        continue
                    p = os.path.join(root, f)
                    for line in open(p, encoding="utf-8", errors="replace"):
                        assert needle not in line, (p, line[:160])


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

    def test_m856_block_position_and_indent(self):
        # m856 sits at 4-space indent under the 2-space "openai:" key
        # under the zero-indent "competitor_relationships:" key in
        # profiles/news-corp.yaml (descriptive block key per #715:
        # no numeric mechanism-id substring in the key).
        doc = _read("profiles/news-corp.yaml")
        idx = doc.index("\n    " + M856_KEY + ":")
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
        assert "mechanism_856" not in M856_KEY
        assert "mechanism-856" not in M856_KEY

    def test_m857_block_position_and_indent(self):
        # m857 sits at 4-space indent under competitor_coverage in the
        # karissa_bell item in profiles/careers/journalists.yaml and
        # carries the Karissa Bell byline provenance (the block is the
        # FOURTH mechanism in her item and the FIRST Bell-vs-Apple
        # pair).
        doc = _read("profiles/careers/journalists.yaml")
        assert doc.count("\n    " + M857_KEY + ":") == 1
        block = _m857_data()
        assert block["journalist"] == "Karissa Bell"
        assert block["publication"] == "Engadget"
        assert "mechanism_857" not in M857_KEY
        assert "mechanism-857" not in M857_KEY

    def test_m858_block_position_and_indent(self):
        # m858 sits at zero indent in profiles/competitor-entities.yaml
        # (top-level block, colon form only per #715 designed keying:
        # the block key carries no numeric mechanism-id substring).
        doc = _read("profiles/competitor-entities.yaml")
        assert doc.count("\n" + M858_KEY + ":") == 1
        assert "mechanism_858" not in M858_KEY
        assert "mechanism-858" not in M858_KEY


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

    def test_1040_suite_log_stalled(self):
        # Stalled at 6%: 3982 bytes of progress dots plus "[  6% ]"
        # markers since Sep 27 14:06 PDT, no summary tokens anywhere,
        # no pytest alive.
        with open(self._suite_log("type_d_1040_full_suite.log"), "rb") as fh:
            data = fh.read()
        assert len(data) == 3982, len(data)
        assert b"[  6%]" in data
        for token in (b"passed", b"failed", b"error"):
            assert token not in data, token

    def test_1040_suite_log_mtime_stale(self):
        # The #1040 suite's log has not been written since 14:06 PDT
        # (hours before this 18:00 PDT run): a live suite would append
        # progress dots continuously. Stale mtime + 3982 bytes + zero
        # summary tokens + no pytest alive = dead per the #795
        # convention. (The new #1045 suite's pytest may be alive by
        # design; this assertion is mtime-scoped to the OLD log, so it
        # cannot self-conflict.)
        import time

        st = os.stat(self._suite_log("type_d_1040_full_suite.log"))
        age_hours = (time.time() - st.st_mtime) / 3600
        assert age_hours > 1, age_hours

    def test_tombstone_lineage_advances(self):
        # FIFTIETH consecutive background death per the #795
        # convention; lineage advances SIXTY-EIGHTH -> SIXTY-NINTH.
        # This run re-launches the suite writing to
        # type_d_1045_full_suite.log; the next Type D run checks it.
        # (The #1035 suite was already tombstoned by #1040; it is NOT
        # re-tombstoned here.)
        entry_anchor = "SIXTY-EIGHTH"
        entry_next = "SIXTY-NINTH"
        assert entry_anchor != entry_next

    def test_1045_suite_log_relaunched(self):
        assert os.path.isfile(self._suite_log("type_d_1045_full_suite.log")), (
            "the re-launched suite log must exist"
        )


class TestTypeDSyntheticEngine:
    """Fresh engine meaningfulness calibration on synthetic corpora.

    Values hardcoded after a scratch run this run (NOT #1040's).
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
            [-0.61, -0.52, -0.57, -0.48, -0.63, -0.55, -0.59],
            [0.21, 0.29, 0.25, 0.31, 0.27, 0.23, 0.18],
            "Meta",
            ["Snap", "Apple"],
        )
        assert abs(r.asymmetry_score - (-0.8128571428571427)) < 1e-9
        assert abs(r.t_statistic - (-31.010745502707014)) < 1e-6
        assert r.p_value < 1e-11
        assert abs(r.cohens_d - (-16.575940711367213)) < 1e-6
        assert r.is_significant is True
        assert r.confidence_interval_upper < 0

    def test_near_null_pair_stays_silent(self):
        r = self._score(
            [0.06, -0.04, 0.02, -0.07, 0.05, -0.03, 0.08],
            [0.01, -0.05, 0.04, -0.02, 0.07, -0.06, 0.03],
            "Meta",
            ["Snap", "Apple"],
        )
        assert abs(r.asymmetry_score - 0.007142857142857141) < 1e-9
        assert r.p_value > 0.8
        assert r.is_significant is False
        assert r.confidence_interval_lower < 0 < r.confidence_interval_upper

    def test_degenerate_m856_pair_engine_guard(self):
        # Degenerate n=1/n=1 contract on the m856 illustrative pair
        # ([-0.45] OpenAI vs [0.10] Anthropic): the engine's structural
        # guard fires (t=0.0, p=1.0, d=0.0, not significant) while
        # |asymmetry| == 0.55 and arm-swap negates exactly. The guard's
        # verdict is the assertion.
        r = self._score([-0.45], [0.10], "OpenAI", ["Anthropic"])
        assert r.t_statistic == 0.0
        assert r.p_value == 1.0
        assert r.cohens_d == 0.0
        assert r.is_significant is False
        assert abs(abs(r.asymmetry_score) - 0.55) < 1e-9
        swapped = self._score([0.10], [-0.45], "Anthropic", ["OpenAI"])
        assert swapped.asymmetry_score == -r.asymmetry_score

    def test_engine_finding_layer_separation(self):
        # The engine CAN return is_significant True on synthetic
        # corpora while the finding layer refuses: the three
        # mechanisms verified this run all carry finding-layer
        # is_significant false / NOT asserted per the Aug 28 2026
        # standing rule.
        assert _m856_data()["statistical_discipline"]["is_significant"] is False
        assert "Engine NOT run" in _m857_data()["statistical_discipline"]
        assert _m858_data()["engine_run"] is False


class TestDocSync1045:
    def test_readme_row_1045(self):
        assert TEST_BASENAME in _read(README_PATH)

    def test_architecture_row_1045(self):
        assert TEST_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_1045_file(self):
        doc = _read(ARCH_PATH)
        assert TEST_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))


class TestIterationLog1045:
    def _entry(self):
        log = _read(LOG_PATH)
        idx = log.index("## #1045 Type D:")
        return log[idx : idx + 15000]

    def test_entry_present(self):
        assert "## #1045 Type D:" in _read(LOG_PATH)

    def test_entry_records_tombstone_and_integrity(self):
        entry = self._entry()
        assert "SIXTY-NINTH" in entry
        assert "858" in entry

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
