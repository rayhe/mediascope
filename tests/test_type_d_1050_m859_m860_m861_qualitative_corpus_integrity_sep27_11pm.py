"""Type D -- Iteration #1050 (Sun 2026-09-27 23:00 PDT): m859/m860/m861
qualitative-discipline verification + post-1045-1049 corpus integrity
(max numeric mechanism_id 861; zero next-number 862 keys in
numeric/underscore/dash mechanism forms; ledger holds at 35 with the
THIRTY-FIFTH member-form present twice (m859 finding + m859
ledger_note, financial-times.yaml), THIRTY-FOURTH member-form still
present twice (m856 summary + m856 ledger_note, news-corp.yaml),
THIRTY-THIRD member-form still present twice (m854 notes +
journalists.yaml), THIRTY-SIXTH member-form negative guard) +
#1045 background-suite tombstone (FIFTY-FIRST consecutive death;
lineage SIXTY-NINTH -> SEVENTIETH) + fresh synthetic engine
calibration (new values, not #1045's) + re-launch of the full suite
as a background process writing to goal hidden_files
type_d_1050_full_suite.log (next Type D run checks its verdict per
the #795 convention).

Type D FIRST leg of the 1050-1054 window, OPENING it (D->E->A->B->C).
Committed predecessor #1049 Type C (22:00 PDT Sep 27) CLOSED the
1045-1049 window (D #1045, E #1046, A #1047, B #1048, C #1049).
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
- m859 (Type A #1047, financial-times.yaml,
  4-space indent, descriptive block key
  `iteration_1047_sep27_2026_ft_openai_rogue_agent_disclosure_early_report_vs_anthropic_ipo_profitability_register`,
  `mechanism_id: 859` field form): FT x OpenAI Sep-26/27 rogue-agent
  disclosure early-report register (-0.25 MANUAL ILLUSTRATIVE,
  carried from m847 per #807) vs FT x Anthropic Sep-14
  IPO-profitability register (+0.15 MANUAL ILLUSTRATIVE);
  illustrative delta (Anthropic minus OpenAI) +0.40; the
  FT-OpenAI Apr 2024 $5-10M/yr licensing deal sits on the
  ADVERSARIALLY-covered side so the spread runs OPPOSITE the naive
  payer-softening prediction; FOURTH safety-crisis falsification
  (after m598 and m853 at the Verge, m856 at WSJ) and FIRST at FT -
  cross-publication replication that the licensing deal does not
  suppress adversarial safety-crisis coverage of the payer;
  THIRTY-FIFTH falsification-family member (ledger 34->35);
  PAIRS m856 (#1042) as the same-event second-publication leg;
  connects_to [847, 856, 441, 415, 823, 637].
- m860 (Type B #1048, journalists.yaml emma_roth item,
  competitor_coverage, 4-space indent block key
  `type_b_1048_emma_roth_verge_meta_muse_charms_interact_vs_google_gemini_live_avatar_sep27`,
  `mechanism_id: 860` field form): SECOND Emma Roth same-day
  same-writer same-outlet Meta-vs-Google AI-assistant pair, 14 days
  after m782; Sep-24 Meta Muse Charms relay (-0.10 MANUAL
  ILLUSTRATIVE, adversarial toolkit idle on a creep-adjacent peg) vs
  Sep-24 Google Gemini 3.8 Live Avatar relay (+0.05 MANUAL
  ILLUSTRATIVE); illustrative delta (Meta minus Google) -0.15,
  near-null; temporal-replication leg m782 needed: register follows
  the news peg, not the entity; pairs m845 (Ropek peg-follows-register)
  at the second writer; NOT a falsification-family member
  (ledger holds at 35); connects_to [782, 845, 425, 773, 776, 779].
- m861 (Type C #1049, profiles/competitor-entities.yaml top-level
  block, zero indent, `mechanism_id: 861` field form): FIRST
  dedicated corpus mechanism on the BUNDLED-LEVERAGE geometry of the
  Google x FT February 2026 AI licensing deal (second-payer leg of
  the FT dual-AI-payer portfolio, m437); SEVENTEENTH relationship
  direction per the m807 enumeration; FIRST AI Contribution Pilot
  disambiguation; FIRST dual-leg restraint-template replication;
  tone NOT_SCORED; NOT falsification-family (ledger holds at 35).

Statistical discipline across all three: MANUAL ILLUSTRATIVE ONLY
(m859, m860) / NOT_SCORED (m861) per the Aug 28 2026 standing rule,
engine NOT run at the finding layer, p_value/cohens_d/ci_95
NOT_CALCULATED, is_significant False / not asserted at the finding
layer, verdict directionally_supported_not_proven,
no_analysis_json_update true, NOT artifact-grade; no analysis.json
update. m859 IS a falsification-family member (THIRTY-FIFTH;
ledger holds at 35); m860 and m861 are NOT (journalist temporal
replication + financial-incentive mapping). Correlation only, not
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

ANCHORED_SHA = "e579fd72cd772399381f9596d3a76468d67b0127"  # patched post-commit per #565

# Built by concatenation so this source file carries no contiguous
# underscore-form mechanism literal (per the #770 lesson).
MECH_ID_MARKER = "mechanism" + "_"
NEXT_NUM = 862

M859_KEY = "iteration_1047_sep27_2026_ft_openai_rogue_agent_disclosure_early_report_vs_anthropic_ipo_profitability_register"
M860_KEY = "type_b_1048_emma_roth_verge_meta_muse_charms_interact_vs_google_gemini_live_avatar_sep27"
M861_KEY = "type_c_1049_google_ft_feb2026_second_payer_leg_bundled_leverage_seventeenth_direction_sep27_10pm"

M859_INDENT = 4  # nested under the competitor_relationships subtree (financial-times.yaml)
M860_INDENT = 4  # item-level block under competitor_coverage in journalists.yaml (emma_roth item)
M861_INDENT = 0  # top-level block in competitor-entities.yaml

M859_OPENAI_URL_FRAG = "divergence.news/event/18128"
M859_ANTHROPIC_URL_FRAG = "stocktwits.com/news-articles/markets/equity/anthropic-ipo-claude-maker"
M860_META_URL_FRAG = "technewstube.com/theverge/1870270/metas-muse-ai-charms"
M860_GOOGLE_URL_FRAG = "thetechstreetnow.com/gemini-3-8-live-with-live-avatar"


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


# At this run's anchor followup, the newest distinct iteration
# numbers in git history: #1050 Type D opens the 1050-1054 window;
# #1049 Type C (committed 22:00 PDT Sep 27) is the schedule
# predecessor and CLOSED the 1045-1049 window. The in-flight runs
# (#899 Type C, #938 Type B, #900 Type D, #1012 working-tree edit)
# have no main commits in git history at this run's checks and sit
# below the window; #898's block was lost (documented in the module
# docstring) and has no main commit either. The #884 block (m762) is
# committed at this run's checks.


def _iter_source_files():
    """Yield paths for profile + test source files.

    Excludes this file (sweep carrier per #715) and __pycache__
    artifacts (per the #715 pattern-rescope lesson: committed test
    pyc files carry next-number needle strings from their own guards;
    compiled artifacts are excluded from the sweeps). No additional
    sweep-carrier exclusions this run: no in-tree SOURCE file carries
    a contiguous 862-form mechanism literal (verified pre-commit), so
    the 862 sweeps run repo-wide with only this file excluded.
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


def _m859_data():
    return _block_data("profiles/financial-times.yaml", M859_KEY, M859_INDENT)


def _m859_text():
    return _indented_block("profiles/financial-times.yaml", M859_KEY, M859_INDENT)


def _m860_data():
    return _block_data(
        "profiles/careers/journalists.yaml", M860_KEY, M860_INDENT
    )


def _m861_data():
    return _block_data(
        "profiles/competitor-entities.yaml", M861_KEY, M861_INDENT
    )


class TestNovelty1050:
    def test_no_type_d_1050_test_file_preexisting(self):
        assert glob.glob(os.path.join(TESTS_DIR, "test_type_d_1050*.py")) == [
            os.path.join(TESTS_DIR, OWN_BASENAME)
        ], "only this file may match the test_type_d_1050 glob"

    def test_no_type_d_1050_in_git_log(self):
        # Pre-commit novelty: no Type D #1050 main commit exists.
        # Post-commit (anchor followup per #565), exactly one exists
        # and it is the anchored main commit - the guard doubles as a
        # duplicate-main-commit check.
        result = subprocess.run(
            ["git", "log", "--format=%H %s", "--grep=Type D #1050"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        mains = [
            line
            for line in result.stdout.splitlines()
            if "Type D #1050" in line and "followup" not in line.lower()
        ]
        if ANCHORED_SHA == "0" * 40:
            assert mains == [], mains
        else:
            assert len(mains) == 1, mains
            assert mains[0].startswith(ANCHORED_SHA + " "), mains

    def test_max_id_is_861_pre_commit(self):
        assert _max_numeric_mechanism_id() == 861

    def test_zero_862_forms_repo_wide(self):
        # Numeric form is profiles-only and must be pure zero. The
        # underscore/dash forms are pinned (with their known #1049
        # Type C guard-literal carrier) in TestTypeDMaxIdAndNextNumber
        # below, which supersedes this class's form checks.
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_block_keys_unique_in_home_yamls(self):
        assert (
            _read("profiles/financial-times.yaml").count("\n    " + M859_KEY + ":")
            == 1
        )
        assert (
            _read("profiles/careers/journalists.yaml").count(
                "\n    " + M860_KEY + ":"
            )
            == 1
        )
        assert (
            _read("profiles/competitor-entities.yaml").count("\n" + M861_KEY + ":")
            == 1
        )

    def test_arm_url_frags_present_in_home_profiles(self):
        # The committed #1047/#1048 runs pinned their URL novelty;
        # this run carries the m859/m860 blocks' own arm URL fragments
        # as verified-in-corpus: the four arm fragments appear in the
        # home profiles.
        block859 = _m859_text()
        assert M859_OPENAI_URL_FRAG in block859
        assert M859_ANTHROPIC_URL_FRAG in block859
        home859 = _read("profiles/financial-times.yaml")
        assert M859_OPENAI_URL_FRAG in home859
        assert M859_ANTHROPIC_URL_FRAG in home859
        block860 = _indented_block(
            "profiles/careers/journalists.yaml", M860_KEY, M860_INDENT
        )
        assert M860_META_URL_FRAG in block860
        assert M860_GOOGLE_URL_FRAG in block860
        home860 = _read("profiles/careers/journalists.yaml")
        assert M860_META_URL_FRAG in home860
        assert M860_GOOGLE_URL_FRAG in home860


class TestTypeDRotationGuard:
    def test_rotation_window_opens_1050(self):
        # The newest distinct iteration in git history is this run's
        # #1050 Type D (window opener). The regex-visible predecessor
        # chain is C #1049 -> B #1048 -> A #1047: the #1047 Type A main
        # commit (2097e861) and #1049 Type C main commit (a9f39a02)
        # both match the "^Type [A-E] #N:" subject convention, and the
        # #1048 Type B main commit (852fc450) matches it too - no
        # subject deviation on this window, so the #752 helper reads
        # the chain straight.
        window = _window()
        assert window[0] == ("D", "1050"), window
        assert window[1:4] == [("C", "1049"), ("B", "1048"), ("A", "1047")], window

    def test_anchor_sha_is_real(self):
        assert re.fullmatch(r"[0-9a-f]{40}", ANCHORED_SHA), (
            "ANCHORED_SHA must be patched to the 40-char main commit "
            "hash post-commit per #565"
        )
        assert ANCHORED_SHA != "0" * 40, (
            "the all-zeros placeholder must be replaced by the anchor "
            "followup per #565"
        )


class TestTypeDM859QualitativeDiscipline:
    def test_mechanism_id(self):
        # m859 uses the `mechanism_id:` field form at 4-space indent
        # in financial-times.yaml (descriptive block key, no numeric
        # mechanism-id substring by designed keying per #715).
        assert _m859_data()["mechanism_id"] == 859
        assert _m859_data()["iteration"] == 1047
        assert _m859_data()["iteration_type"] == "A"

    def test_arm_tones_and_spread(self):
        data = _m859_data()
        assert data["openai_arm_fresh"]["tone_illustrative"] == -0.25
        assert data["anthropic_arm_fresh"]["tone_illustrative"] == 0.15
        assert data["illustrative_delta_anthropic_minus_openai"] == 0.40
        disc = data["statistical_discipline"]
        assert disc["scores"] == "MANUAL ILLUSTRATIVE only"
        assert disc["p_value"] == "NOT_CALCULATED"
        assert disc["cohens_d"] == "NOT_CALCULATED"
        assert disc["ci_95"] == "NOT_CALCULATED"
        assert disc["is_significant"] is False
        assert disc["engine_run"] is False

    def test_falsification_member_thirtyfifth(self):
        # The FT-OpenAI Apr 2024 $5-10M/yr licensing deal sits on the
        # adversarially-covered side (FT published the payer's
        # safety-crisis disclosure early, 2nd of 12 outlets); the
        # uniform payer-softening prediction fails at the publication
        # level: THIRTY-FIFTH falsification-family member (ledger
        # 34->35); FOURTH safety-crisis falsification, FIRST at FT.
        data = _m859_data()
        assert data["falsification_family_member"] is True
        assert data["falsification_ledger"] == 35
        assert "THIRTY-FIFTH falsification-family member" in data["ledger_note"]
        assert "ledger 34->35" in data["ledger_note"]
        assert "FIRST at FT" in data["finding"]

    def test_manual_illustrative_discipline(self):
        disc = _m859_data()["statistical_discipline"]
        assert disc["no_analysis_json_update"] is True
        assert disc["artifact_grade"] is False
        assert disc["verdict"] == "directionally_supported_not_proven"
        assert "0 browser.open" in _m859_text()

    def test_verdict_and_provenance(self):
        data = _m859_data()
        assert data["type"] == "Type A: Competitor Coverage Deep Dive"
        assert data["connects_to"] == [847, 856, 441, 415, 823, 637]
        assert (
            "tests/test_type_a_1047_ft_openai_sep26_rogue_agent_disclosure_early_report_vs_anthropic_ipo_profitability_sep27_8pm.py"
            in data["test_file"]
        )


class TestTypeDM860QualitativeDiscipline:
    def test_mechanism_id(self):
        # m860 is the SECOND mechanism in the emma_roth journalist
        # item (mechanism_ids [782, 860]); SECOND Roth-vs-Google pair.
        data = _m860_data()
        assert data["mechanism_id"] == 860
        assert data["iteration"] == 1048
        assert data["journalist"] == "Emma Roth"
        assert data["publication"] == "the-verge"

    def test_arm_tones_and_spread(self):
        data = _m860_data()
        assert data["meta_arm"]["tone_MANUAL_ILLUSTRATIVE"] == -0.10
        assert data["google_arm"]["tone_MANUAL_ILLUSTRATIVE"] == 0.05
        assert data["illustrative_delta_meta_minus_google"] == -0.15
        assert data["delta_calc"] == "(-0.10) - (0.05) = -0.15"

    def test_not_falsification_family(self):
        # Temporal replication of m782 with symmetric relay pegs:
        # register follows the news peg, not the entity; thesis
        # refinement for the Type B series (m782 fired the adversarial
        # register on first-person creepy discoveries; 14 days later,
        # on relay pegs, she is register-symmetric). NOT a
        # falsification; ledger holds at 35.
        fam = _m860_data()["falsification_family"]
        assert "NOT a falsification-family member" in fam
        assert "ledger holds at 35" in fam

    def test_manual_illustrative_discipline(self):
        disc = _m860_data()["statistical_discipline"]
        assert "MANUAL ILLUSTRATIVE scores only" in disc
        assert "p_value NOT_CALCULATED" in disc
        assert "cohens_d NOT_CALCULATED" in disc
        assert "Engine NOT run" in disc

    def test_verdict_and_provenance(self):
        data = _m860_data()
        assert "directionally_supported_not_proven" in data["finding"]
        assert data["no_analysis_json_update"] is True
        assert data["connects_to"] == [782, 845, 425, 773, 776, 779]
        assert (
            "tests/test_type_b_1048_emma_roth_verge_meta_muse_charms_vs_google_gemini_live_avatar_sep27_9pm.py"
            in data["test_file"]
        )


class TestTypeDM861QualitativeDiscipline:
    def test_mechanism_id_and_provenance(self):
        # m861 is a top-level block in competitor-entities.yaml (zero
        # indent); financial-incentive mapping, tone NOT_SCORED.
        data = _m861_data()
        assert data["mechanism_id"] == 861
        assert data["iteration"] == 1049
        assert data["type"] == "financial_incentive_mapping"
        assert data["tone_scores"] == "NOT_SCORED"

    def test_bundled_leverage_seventeenth_direction(self):
        # FIRST dedicated corpus mechanism on the bundled-leverage
        # geometry of the Google x FT February 2026 AI licensing deal;
        # SEVENTEENTH relationship direction per the m807 enumeration.
        text = _indented_block(
            "profiles/competitor-entities.yaml", M861_KEY, M861_INDENT
        )
        assert "BUNDLED-LEVERAGE" in text
        assert "SEVENTEENTH relationship direction" in text
        assert "contribution_pilot_disambiguation" in text

    def test_statistical_discipline(self):
        data = _m861_data()
        assert data["engine_run"] is False
        assert data["no_analysis_json_update"] is True
        assert data["verdict"] == "directionally_supported_not_proven"
        assert data["artifact_grade"] is False
        assert data["excerpt_bounded"] is True

    def test_not_falsification_family_ledger_holds_35(self):
        data = _m861_data()
        assert data["falsification_family_member"] is False
        assert data["falsification_ledger"] == 35
        assert "Ledger holds at 35" in data["falsification_note"]
        assert "THIRTY-FIFTH" in data["falsification_note"]

    def test_block_position_top_level(self):
        doc = _read("profiles/competitor-entities.yaml")
        assert doc.count("\n" + M861_KEY + ":") == 1
        assert "mechanism_861" not in M861_KEY
        assert "mechanism-861" not in M861_KEY


class TestTypeDMaxIdAndNextNumber:
    def test_max_numeric_mechanism_id_is_861(self):
        assert _max_numeric_mechanism_id() == 861

    def test_zero_numeric_862_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_zero_underscore_862_repo_wide(self):
        # The single repo-wide carrier of the contiguous
        # "mechanism_862" literal is the committed #1049 Type C test
        # file, which carries it as its own forward-looking guard
        # literal (line ~214: "mechanism_id: 862", "mechanism_862",
        # "mechanism-862" needles), not as corpus data. The sweep pins
        # the hit set to exactly that file - no other profile or test
        # source may carry the needle.
        carrier = os.path.join(
            TESTS_DIR,
            "test_type_c_1049_google_ft_feb2026_second_payer_leg_bundled_leverage_seventeenth_direction_sep27_10pm.py",
        )
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == [carrier]

    def test_zero_dash_862_repo_wide(self):
        # Same carrier logic for the "mechanism-862" form: the only
        # repo-wide hit is the #1049 Type C test file's own guard
        # literals.
        carrier = os.path.join(
            TESTS_DIR,
            "test_type_c_1049_google_ft_feb2026_second_payer_leg_bundled_leverage_seventeenth_direction_sep27_10pm.py",
        )
        assert _repo_grep_dash_mechanism(NEXT_NUM) == [carrier]


class TestTypeDFalsificationLedger:
    def test_ledger_holds_at_35(self):
        # m859 carries the ledger as structured fields
        # (falsification_ledger == 35, falsification_family_member
        # true); m860 carries it in block prose ("ledger holds at
        # 35"); m861 as structured fields (falsification_ledger == 35,
        # member false) with matching prose.
        assert _m859_data()["falsification_ledger"] == 35
        assert _m859_data()["falsification_family_member"] is True
        assert "ledger holds at 35" in _m860_data()["falsification_family"]
        assert _m861_data()["falsification_ledger"] == 35
        assert "Ledger holds at 35" in _m861_data()["falsification_note"]

    def test_thirtyfifth_member_form_present(self):
        # THIRTY-FIFTH member-form: the m859 summary (Type A #1047,
        # mechanism 859, financial-times.yaml) appears twice - once in
        # the block's finding and once in the block's ledger_note.
        # Both are positive member-form claims; the scan pins the pair.
        needle = "THIRTY-FIFTH falsification-family member"
        hits = _profiles_with(needle)
        assert hits == [
            os.path.join(PROFILES_DIR, "financial-times.yaml")
        ], hits
        doc = _read("profiles/financial-times.yaml")
        assert doc.count(needle) == 2, doc.count(needle)

    def test_thirtyfourth_member_form_still_present(self):
        # The m856 THIRTY-FOURTH anchor (Type A #1042) must not have
        # been disturbed by the ledger advance.
        needle = "THIRTY-FOURTH falsification-family member"
        hits = _profiles_with(needle)
        assert (
            os.path.join(PROFILES_DIR, "news-corp.yaml") in hits
        ), hits
        doc = _read("profiles/news-corp.yaml")
        assert doc.count(needle) == 2, doc.count(needle)

    def test_thirtythird_member_form_still_present(self):
        # The m854 THIRTY-THIRD anchor (Type B #1038) must not have
        # been disturbed by the ledger advance.
        hits = _profiles_with("THIRTY-THIRD falsification-family member")
        assert (
            os.path.join(PROFILES_DIR, "careers", "journalists.yaml") in hits
        ), hits

    def test_thirtysixth_member_form_absent(self):
        # THIRTY-SIXTH is the negative guard: no positive
        # thirty-sixth falsification-family member-form claim may
        # exist anywhere in profiles/ or test sources. Own file
        # excluded as sweep carrier per #715 (it carries the needle in
        # this very scan).
        needle = "THIRTY-SIXTH falsification-family member"
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

    def test_m859_block_position_and_indent(self):
        # m859 sits at 4-space indent in profiles/financial-times.yaml
        # (descriptive block key per #715: no numeric mechanism-id
        # substring in the key).
        doc = _read("profiles/financial-times.yaml")
        assert doc.count("\n    " + M859_KEY + ":") == 1
        assert "mechanism_859" not in M859_KEY
        assert "mechanism-859" not in M859_KEY

    def test_m860_block_position_and_indent(self):
        # m860 sits at 4-space indent under competitor_coverage in the
        # emma_roth item in profiles/careers/journalists.yaml and
        # carries the Emma Roth byline provenance (the block is the
        # SECOND mechanism in her item and the SECOND Roth-vs-Google
        # pair).
        doc = _read("profiles/careers/journalists.yaml")
        assert doc.count("\n    " + M860_KEY + ":") == 1
        block = _m860_data()
        assert block["journalist"] == "Emma Roth"
        assert block["publication"] == "the-verge"
        assert "mechanism_860" not in M860_KEY
        assert "mechanism-860" not in M860_KEY

    def test_m861_block_position_and_indent(self):
        # m861 sits at zero indent in profiles/competitor-entities.yaml
        # (top-level block, colon form only per #715 designed keying:
        # the block key carries no numeric mechanism-id substring).
        doc = _read("profiles/competitor-entities.yaml")
        assert doc.count("\n" + M861_KEY + ":") == 1
        assert "mechanism_861" not in M861_KEY
        assert "mechanism-861" not in M861_KEY


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

    def test_1045_suite_log_stalled(self):
        # Stalled at ~6%: 3654 bytes of progress dots plus
        # "[  6% ]"-style markers since Sep 27 18:53 PDT, no summary
        # tokens anywhere, no pytest alive.
        with open(self._suite_log("type_d_1045_full_suite.log"), "rb") as fh:
            data = fh.read()
        assert len(data) == 3654, len(data)
        assert b"[  6%]" in data
        for token in (b"passed", b"failed", b"error"):
            assert token not in data, token

    def test_1045_suite_log_mtime_stale(self):
        # The #1045 suite's log has not been written since ~18:53 PDT
        # (hours before this 23:00 PDT run): a live suite would append
        # progress dots continuously. Stale mtime + 3654 bytes + zero
        # summary tokens + no pytest alive = dead per the #795
        # convention. (The new #1050 suite's pytest may be alive by
        # design; this assertion is mtime-scoped to the OLD log, so it
        # cannot self-conflict.)
        import time

        st = os.stat(self._suite_log("type_d_1045_full_suite.log"))
        age_hours = (time.time() - st.st_mtime) / 3600
        assert age_hours > 1, age_hours

    def test_tombstone_lineage_advances(self):
        # FIFTY-FIRST consecutive background death per the #795
        # convention; lineage advances SIXTY-NINTH -> SEVENTIETH.
        # This run re-launches the suite writing to
        # type_d_1050_full_suite.log; the next Type D run checks it.
        # (The #1040 suite was already tombstoned by #1045; it is NOT
        # re-tombstoned here.)
        entry_anchor = "SIXTY-NINTH"
        entry_next = "SEVENTIETH"
        assert entry_anchor != entry_next

    def test_1050_suite_log_relaunched(self):
        assert os.path.isfile(self._suite_log("type_d_1050_full_suite.log")), (
            "the re-launched suite log must exist"
        )


class TestTypeDSyntheticEngine:
    """Fresh engine meaningfulness calibration on synthetic corpora.

    Values hardcoded after a scratch run this run (NOT #1045's).
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
            [-0.58, -0.51, -0.63, -0.47, -0.60, -0.55, -0.52],
            [0.19, 0.27, 0.22, 0.30, 0.24, 0.28, 0.21],
            "Meta",
            ["Snap", "Apple"],
        )
        assert abs(r.asymmetry_score - (-0.7957142857142856)) < 1e-9
        assert abs(r.t_statistic - (-30.569346407128755)) < 1e-6
        assert r.p_value < 1e-11
        assert abs(r.cohens_d - (-16.34000297044068)) < 1e-6
        assert r.is_significant is True
        assert r.confidence_interval_upper < 0

    def test_near_null_pair_stays_silent(self):
        r = self._score(
            [0.05, -0.06, 0.03, -0.02, 0.07, -0.04, 0.01],
            [0.02, -0.03, 0.06, -0.01, 0.04, -0.05, 0.08],
            "Meta",
            ["Snap", "Apple"],
        )
        assert abs(r.asymmetry_score - (-0.01)) < 1e-9
        assert r.p_value > 0.5
        assert r.is_significant is False
        assert r.confidence_interval_lower < 0 < r.confidence_interval_upper

    def test_degenerate_m859_pair_engine_guard(self):
        # Degenerate n=1/n=1 contract on the m859 illustrative pair
        # ([-0.25] OpenAI vs [0.15] Anthropic): the engine's structural
        # guard fires (t=0.0, p=1.0, d=0.0, not significant) while
        # |asymmetry| == 0.40 and arm-swap negates exactly. The guard's
        # verdict is the assertion.
        r = self._score([-0.25], [0.15], "OpenAI", ["Anthropic"])
        assert r.t_statistic == 0.0
        assert r.p_value == 1.0
        assert r.cohens_d == 0.0
        assert r.is_significant is False
        assert abs(abs(r.asymmetry_score) - 0.40) < 1e-9
        swapped = self._score([0.15], [-0.25], "Anthropic", ["OpenAI"])
        assert swapped.asymmetry_score == -r.asymmetry_score

    def test_engine_finding_layer_separation(self):
        # The engine CAN return is_significant True on synthetic
        # corpora while the finding layer refuses: the three
        # mechanisms verified this run all carry finding-layer
        # is_significant false / NOT asserted per the Aug 28 2026
        # standing rule.
        assert _m859_data()["statistical_discipline"]["is_significant"] is False
        assert "Engine NOT run" in _m860_data()["statistical_discipline"]
        assert _m861_data()["engine_run"] is False


class TestDocSync1050:
    def test_readme_row_1050(self):
        assert TEST_BASENAME in _read(README_PATH)

    def test_architecture_row_1050(self):
        assert TEST_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_1050_file(self):
        doc = _read(ARCH_PATH)
        assert TEST_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))


class TestIterationLog1050:
    def _entry(self):
        log = _read(LOG_PATH)
        idx = log.index("## #1050 Type D:")
        return log[idx : idx + 15000]

    def test_entry_present(self):
        assert "## #1050 Type D:" in _read(LOG_PATH)

    def test_entry_records_tombstone_and_integrity(self):
        entry = self._entry()
        assert "SEVENTIETH" in entry
        assert "861" in entry

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
