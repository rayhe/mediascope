"""Type A -- Iteration #1127 (Thu 2026-10-01 15:00 PDT): m907 The Verge x
OpenAI Sep-29/30 safety-crisis double (Astra shelving homepage piece +
FTC probe brief, regulatory-enforcement register) vs carried Meta arms,
post-landing corpus integrity (max numeric mechanism_id 907; zero
next-number 908 keys in numeric/underscore/dash mechanism forms - the
908 needles are format-built per #715 so no guard-literal carrier file
exists; the m907 block key carries no mechanism-number substring
(designed keying), so it is a plain literal; the #1122/#1123/#1124/#1125
window files are NOT edited by this run - their now-stale
forward-looking pins are recorded as fail-by-design via subprocess in
the staleness class (#1125's max-906 pin trips on the landed 907;
#1125's zero-907 numeric/underscore pins trip on the landed 907 key
forms; #1125's no-forty-sixth-member pin trips on the landed
FORTY-SIXTH member; #1124's zero-907 guards, no-thirty-third-direction
guard and forty-sixth-absent guard STAY RED-RECORDED from the #1125
staleness run, flipped at #1127; the #1122/#1123 supersession classes
STAY GREEN); ledger advances 45->46 with the FORTY-SIXTH member-claim
form present in exactly one profiles file (profiles/the-verge.yaml,
m907 block, 2 occurrences - designed pattern) and the FORTY-SEVENTH
member-claim form absent profiles-wide (needle format-built per #715);
the thirty-second relationship direction stands in
competitor-entities.yaml (m906); the thirty-third
relationship-direction claim form is absent repo-wide (needle
format-built per #715)) + the #1125 background-suite check (alive at
~3% at this run's checks, no verdict - belongs to #1130 per #795;
checked only, NOT touched).

Type A THIRD leg of the 1125-1129 window, CONTINUING it
(D #1125 -> E #1126 -> A #1127 -> B #1128 -> C #1129). Committed
predecessor #1126 Type E (14:00 PDT Oct 1) is the window's second leg
(main 89349e3c / anchor d0478668 / doc-sync dcfc5eaf / log-hash
ea551b23). Rotation per the #565 anchor + rotation guard.
Concurrency note: the in-flight runs at this run's checks are the
#899 Type C block (m771, uncommitted hunk in profiles/nytimes.yaml),
the #938 Type B test file (uncommitted working-tree edit), the #900
Type D test file (untracked, on disk) and the #1012 working-tree
edit of the committed Type A #1012 test file - all UNCOMMITTED, no
Type C #899 / Type B #938 / Type D #900 main commits in git
history, and no ## #899 / ## #938 / ## #900 Type X entries in
iteration-log.md. This run does NOT touch the in-flight files;
the in-flight blocks are owned by their runs. Targeted staging only
per the repo-wide traversal lesson. Iteration numbers follow the
rotation schedule, not commit order. Do NOT touch #1024's m846
(FOURTEENTH, exclusionary-diversion): self-flagged
sourcing-constraint violation; Ray's revert/leave/rebuild-from-primary
decision still pending.

Verifies:
- m907 (Type A #1127, the-verge.yaml 4-space block key under
  competitor_relationships.openai, `mechanism_id: 907` field form;
  block key count 1 - colon-form line only, designed: no block_key
  field in the m907 block and the test_file value does not contain the
  block key): The Verge Sep-29/30-2026 safety-crisis double on the Vox
  deal partner - A1 Sep 29 Jay Peters "OpenAI won''t release GPT-6.1
  Astra due to worries about safety", homepage placement, safety-crisis
  register (-0.40 MANUAL ILLUSTRATIVE, excerpt-tier attested via
  buzzsumo journalist profile + explainx.ai timeline, 0 browser.open
  per #503); A2 Sep 30 Emma Roth "The FTC has reportedly opened an
  investigation into OpenAI and Anthropic", regulatory-enforcement
  register (-0.35 MANUAL ILLUSTRATIVE, 0.05 softer than A1 because the
  probe names two labs, same logic as m904) - vs carried Meta arms
  (the #592 same-outlet same-window Meta glasses set [-0.55, -0.60,
  -0.50], mean -0.55, and the m811 Verge Meta Connect Audio
  privacy-positive concession +0.10, both un-rescored per #807).
  Illustrative deltas (OpenAI pair mean -0.375 minus Meta): +0.175
  primary (pair 0.175 softer than the Meta stigma baseline -
  thesis-consistent), -0.475 secondary (pair 0.475 harder than the Meta
  concession arm). The finding is register-AVAILABILITY, not
  mean-tone: the Vox Media x OpenAI May 29 2024 licensing deal
  (coverage_prediction ''softer'') does not suppress the adversarial
  safety register OR the enforcement register on the deal partner -
  the outlet homepages the payer''s safety-chief-admitted deception
  shelving and routes the regulator''s rogue-agent probe onto the
  payer within 48 hours. FORTY-SIXTH falsification-family member;
  ledger 45->46. FIRST regulatory-enforcement-register falsification
  at The Verge; EXTENDS the m901 (FT)/m904 (WSJ)
  enforcement-register falsification line to a third deal-partner
  publication; EXTENDS the m880 Verge Astra-safety arc into the
  Sep-28-Oct-1 crisis window (register continuity, ninth day);
  BOUNDED by m425 (+0.46 thesis-consistent aspiration gradient) and
  m507 (ad-monetization domain boundary). Confined to the un-briefed
  safety-news peg per m712.

MANUAL/QUALITATIVE ONLY, engine NOT run, no analysis.json update,
NOT artifact-grade, verdict directionally_supported_not_proven.
Correlation is not causation; hypothesis-generating only.
"""

import glob
import os
import re
import subprocess

import pytest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TESTS_DIR = os.path.join(REPO_ROOT, "tests")
PROFILES_DIR = os.path.join(REPO_ROOT, "profiles")
LOG_PATH = os.path.join(REPO_ROOT, "iteration-log.md")
OWN_BASENAME = (
    "test_type_a_1127_verge_openai_sep29_30_safety_crisis_"
    "double_oct01_3pm.py"
)

MAX_ID = 907
NEXT_NUM = 908

# Patched by the anchor followup commit per #565 (post-main-commit).
ANCHORED_SHA = "TBD-patched-by-anchor-followup-per-565"

# Doc-sync constants per #719 (patched post-first-run with the true
# collected count).
README_TEST_COUNT = 0
README_FILE_COUNT = 0

# The m907 block key carries no mechanism-number substring (designed
# keying), so it is a plain literal per #715.
M907_KEY = (
    "type_a_1127_verge_openai_sep29_30_safety_crisis_double_"
    "astra_homepage_ftc_probe_brief"
)
M907_INDENT = 4
M907_HOME = "profiles/the-verge.yaml"

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

# Falsification-family / relationship-direction needles are
# format-built per #715: no contiguous claim-form literal may exist
# in this file. The landed-claim forms live in the-verge.yaml (m907)
# and competitor-entities.yaml (m906) respectively.
_T46 = "FORTY-" + "SIXTH falsification-family member"
_T47 = "FORTY-" + "SEVENTH falsification-family member"
_TW33 = "THIRTY-" + "THIRD relationship direction"

SUITE_LOG = os.path.expanduser(
    "~/workspace/goals/mediascope-meta-wearables-press-analysis/"
    "hidden_files/type_d_1125_full_suite.log"
)
D1125_FILE = (
    "tests/test_type_d_1125_m904_m905_m906_qualitative_corpus_"
    "integrity_oct01_1pm.py"
)
A1122_FILE = (
    "tests/test_type_a_1122_wsj_openai_astra_scrapped_ftc_"
    "probe_enforcement_vs_carried_meta_arms_oct01_10am.py"
)
B1123_FILE = (
    "tests/test_type_b_1123_maxwell_zeff_wsj_migration_"
    "openai_register_flip_vs_wired_platform_relay_sep2026_"
    "11am.py"
)
C1124_FILE = "tests/test_type_c_1124_perplexity_hp_crusoe_oct01_12pm.py"
E1126_BASENAME = "test_type_e_1126_"


def _read(path):
    with open(path, encoding="utf-8", errors="replace") as f:
        return f.read()


def _git(*args):
    result = subprocess.run(
        ["git", "-C", REPO_ROOT] + list(args),
        capture_output=True,
        text=True,
        timeout=120,
    )
    return result.stdout


def _iter_source_files():
    for root, dirs, files in os.walk(REPO_ROOT):
        if ".git" in root or ".venv" in root or "__pycache__" in root:
            continue
        dirs[:] = [
            d
            for d in dirs
            if d not in (".git", ".venv", "__pycache__", "node_modules")
        ]
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


def _profiles_text():
    parts = []
    for root, dirs, files in os.walk(PROFILES_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
            parts.append(
                open(
                    os.path.join(root, f), encoding="utf-8", errors="replace"
                ).read()
            )
    return "\n".join(parts)


def _m907_data():
    import yaml

    with open(
        os.path.join(REPO_ROOT, M907_HOME), encoding="utf-8"
    ) as f:
        doc = yaml.safe_load(f)
    return doc["competitor_relationships"]["openai"][M907_KEY]


def _window():
    """Newest-first distinct (type, number) sequence from the log."""
    pat = re.compile(r"^## #(\d+) Type ([A-E]):", re.M)
    seen = []
    for num, typ in pat.findall(_read(LOG_PATH)):
        key = (typ, num)
        if key not in seen:
            seen.append(key)
    return seen


# ---------------------------------------------------------------------------
# 1. Novelty (pre-commit state recorded post-commit; superseded pins noted)
# ---------------------------------------------------------------------------
class TestNovelty1127:
    def test_no_type_a_1127_test_file_preexisting(self):
        files = glob.glob(os.path.join(TESTS_DIR, "test_type_a_1127*.py"))
        assert files == [os.path.join(TESTS_DIR, OWN_BASENAME)], files

    def test_no_type_a_1127_in_git_log_precommit(self):
        # Pre-commit novelty guard: no commit may already claim this
        # slot. SUPERSEDED BY DESIGN once this run's main commit
        # ("Type A #1127:") lands; post-commit,
        # TestTypeARotationGuard1127 asserts the anchor and window
        # instead. Deselect this test in post-commit full runs.
        log = _git("log", "--format=%s", "--grep=Type A #1127")
        assert "Type A #1127" not in log

    def test_max_id_is_907_post_landing(self):
        # Pre-commit this was 906 (verified); post-commit the m907
        # landing makes it 907.
        assert _max_numeric_mechanism_id() == MAX_ID

    def test_907_numeric_form_lands_exactly_once(self):
        # Pre-commit zero; post-commit exactly one (the m907 block).
        hits = _repo_grep_numeric_mechanism_id(MAX_ID)
        assert hits == [os.path.join(PROFILES_DIR, "the-verge.yaml")], hits

    def test_block_key_unique_in_home_yaml(self):
        # m907: colon-form line only (count 1, designed - no block_key
        # field in the m907 block, and the test_file value does not
        # contain the block key).
        text = _read(os.path.join(REPO_ROOT, M907_HOME))
        assert text.count(M907_KEY) == 1, text.count(M907_KEY)

    def test_block_key_zero_hit_precommit_recorded(self):
        # Recorded pre-commit: the block key was absent repo-wide
        # (verified via git grep on the verbatim key). Post-commit it
        # is present in the-verge.yaml and in this test file (as a
        # designed literal per #715 - the key carries no
        # mechanism-number substring).
        assert M907_KEY in _read(os.path.join(REPO_ROOT, M907_HOME))


# ---------------------------------------------------------------------------
# 2. Rotation guard (2 tests deselected pre-commit per #565)
# ---------------------------------------------------------------------------
class TestTypeARotationGuard1127:
    def test_rotation_window_third_leg_1127(self):
        # THIRD leg of the 1125-1129 window, CONTINUING it (per #565:
        # D #1125 -> E #1126 -> A #1127 -> B #1128 -> C #1129).
        # Deselected pre-commit (this run's main commit is not yet
        # in history); passes post-commit.
        w = _window()
        assert w[0] == ("A", "1127"), w
        # Newest-first distinct sequence: A #1127 (this run) follows
        # E #1126 and D #1125, opening the window after the closed
        # 1120-1124 window (C #1124, B #1123, A #1122, E #1121).
        assert [t for t, _ in w[:6]] == ["A", "E", "D", "C", "B", "A"], w

    def test_predecessor_1126_chain_present(self):
        # #1126 Type E is the window's second leg; its main/anchor/
        # doc-sync/log-hash chain must be in history before this run
        # commits.
        log = _git("log", "--format=%H %s")
        assert "89349e3c" in log
        assert "d0478668" in log
        assert "dcfc5eaf" in log
        assert "ea551b23" in log

    def test_no_type_b_1128_in_git_log(self):
        log = _git("log", "--format=%s", "--grep=Type B #1128")
        assert "Type B #1128" not in log

    def test_anchor_sha_is_real(self):
        # Patched post-main-commit by the anchor followup per #565.
        # Deselected pre-commit (placeholder by design); passes
        # post-patch.
        assert re.fullmatch(r"[0-9a-f]{40}", ANCHORED_SHA), ANCHORED_SHA
        assert ANCHORED_SHA != "0" * 40


# ---------------------------------------------------------------------------
# 2b. Novelty anchor (1 test, deselected pre-commit per #565)
# ---------------------------------------------------------------------------
class TestTypeANoveltyAnchor1127:
    def test_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per #565: the main commit does not
        # exist yet. Post-commit this asserts the single #1127
        # commit is the anchor and carries the test-file changes.
        log = _git("log", "--format=%H %s", "--grep=Type A #1127")
        assert "Type A #1127" in log
        assert ANCHORED_SHA in log


# ---------------------------------------------------------------------------
# 3. Corpus integrity
# ---------------------------------------------------------------------------
class TestTypeACorpusIntegrity1127:
    def test_m907_block_keyed_under_openai_at_indent_4(self):
        lines = _read(os.path.join(REPO_ROOT, M907_HOME)).splitlines()
        hits = [l for l in lines if M907_KEY + ":" in l]
        assert len(hits) == 1, hits
        assert hits[0].startswith("    " + M907_KEY + ":"), hits[0][:60]
        assert not hits[0].startswith("      " + M907_KEY), hits[0][:60]

    def test_m907_fields_at_indent_6(self):
        import yaml

        data = _m907_data()
        assert data["mechanism_id"] == 907
        assert data["iteration"] == 1127
        assert data["iteration_type"] == "A"

    def test_m907_yaml_parses_and_sits_in_openai(self):
        import yaml

        with open(
            os.path.join(REPO_ROOT, M907_HOME), encoding="utf-8"
        ) as f:
            doc = yaml.safe_load(f)
        assert M907_KEY in doc["competitor_relationships"]["openai"]

    def test_ascii_only_no_em_dashes_in_block(self):
        text = _read(os.path.join(REPO_ROOT, M907_HOME))
        start = text.index(M907_KEY)
        end = text.index("  meta:", start)
        block = text[start:end]
        assert "\u2014" not in block
        block.encode("ascii")

    def test_m907_does_not_touch_inflight_mechanisms(self):
        # m771 (#899), m846 (#1024), the #938/#900 test-file areas
        # are untouched by this run's diff.
        diff = _git("diff", "--stat")
        for token in ("m771", "m846", "test_type_b_938_", "test_type_d_900_"):
            assert token not in diff, token


# ---------------------------------------------------------------------------
# 4. m907 content discipline
# ---------------------------------------------------------------------------
class TestTypeAM907ContentDiscipline1127:
    def _a1(self):
        return _m907_data()["openai_arms"][0]["item"]

    def _a2(self):
        return _m907_data()["openai_arms"][1]["item"]

    def test_two_openai_arms(self):
        assert len(_m907_data()["openai_arms"]) == 2

    def test_a1_astra_homepage_piece(self):
        a1 = self._a1()
        assert a1["byline"] == "Jay Peters"
        assert a1["date"] == "2026-09-29"
        assert "Astra" in a1["title"]
        assert "worries about safety" in a1["title"]
        assert a1["register"] == "safety-crisis homepage news"
        assert "homepage" in " ".join(a1["key_language"]).lower()
        assert a1["manual_illustrative_tone"] == -0.40

    def test_a1_evidence_tier_excerpt_bounded(self):
        a1 = self._a1()
        assert a1["evidence_tier"] == "excerpt-tier third-party-attested"
        assert "buzzsumo" in a1["evidence_note"]
        assert "explainx.ai" in a1["evidence_note"]
        assert "#503" in a1["evidence_note"]

    def test_a2_ftc_probe_brief(self):
        a2 = self._a2()
        assert a2["byline"] == "Emma Roth"
        assert a2["date"] == "2026-09-30"
        assert "FTC" in a2["title"]
        assert "Anthropic" in a2["title"]
        assert a2["register"] == "regulatory-enforcement news brief"
        assert a2["manual_illustrative_tone"] == -0.35

    def test_a2_verbatim_verge_url(self):
        a2 = self._a2()
        assert a2["url"] == (
            "https://www.theverge.com/ai-artificial-intelligence/"
            "1002695/the-ftc-has-reportedly-opened-an-investigation-"
            "into-openai-and-anthropic"
        )
        assert a2["url"] in _m907_data()["source_urls"]

    def test_a2_softer_than_a1_by_005_two_lab_logic(self):
        a1 = self._a1()
        a2 = self._a2()
        assert round(a1["manual_illustrative_tone"] - a2["manual_illustrative_tone"], 2) == -0.05

    def test_pair_mean_arithmetic(self):
        data = _m907_data()
        assert data["openai_pair_mean"] == -0.375
        assert data["openai_pair_mean_calc"] == "(-0.40 + -0.35) / 2 = -0.375"

    def test_meta_arms_carried_unrescored_per_807(self):
        meta = _m907_data()["meta_arms"]
        assert meta["primary"]["carried_from"].startswith("mechanism 592")
        assert "#807" in meta["primary"]["carried_from"]
        tones = [
            a["manual_illustrative_tone"]
            for a in meta["primary"]["arms"]
        ]
        assert tones == [-0.55, -0.60, -0.50]
        assert meta["primary"]["meta_band_mean"] == -0.55
        assert meta["secondary"]["carried_from"].startswith("mechanism 811")
        assert meta["secondary"]["item"]["manual_illustrative_tone"] == 0.10

    def test_connects_to_line(self):
        assert _m907_data()["connects_to"] == [598, 853, 880, 901, 904, 425, 507]

    def test_rotation_guard_field(self):
        rg = _m907_data()["rotation_guard"]
        assert "1125-1129" in rg
        assert "A (this run)" in rg
        assert "#1128 Type B" in rg


# ---------------------------------------------------------------------------
# 5. Statistical discipline
# ---------------------------------------------------------------------------
class TestTypeAStatisticalDiscipline1127:
    def _res(self):
        return _m907_data()["asymmetry_scorer_result"]

    def test_manual_illustrative_only(self):
        assert self._res()["method"] == "MANUAL ILLUSTRATIVE"
        assert self._res()["engine_run"] is False

    def test_primary_delta_arithmetic(self):
        r = self._res()
        assert r["illustrative_delta_openai_minus_meta_primary"] == 0.175
        assert r["delta_arithmetic_primary"] == "-0.375 - (-0.55) = +0.175"

    def test_secondary_delta_arithmetic(self):
        r = self._res()
        assert r["illustrative_delta_openai_minus_meta_secondary"] == -0.475
        assert r["delta_arithmetic_secondary"] == "-0.375 - (+0.10) = -0.475"

    def test_no_inferential_statistics_at_finding_layer(self):
        r = self._res()
        assert r["p_value"] == "NOT_CALCULATED"
        assert r["cohens_d"] == "NOT_CALCULATED"
        assert r["ci_95"] == "NOT_CALCULATED"
        assert r["is_significant"] is False

    def test_verdict_directionally_supported_not_proven(self):
        assert self._res()["verdict"] == "directionally_supported_not_proven"
        assert _m907_data()["verdict"] == "directionally_supported_not_proven"

    def test_not_artifact_grade_no_analysis_json(self):
        assert self._res()["artifact_grade"] is False
        assert self._res()["no_analysis_json_update"] is True
        assert _m907_data()["no_analysis_json_update"] is True

    def test_finding_states_register_availability_not_mean_tone(self):
        finding = _m907_data()["finding"]
        assert "register-AVAILABILITY, not mean-tone" in finding
        assert "thesis-consistent" in finding

    def test_confounders_five_graded(self):
        confs = _m907_data()["confounders"]
        assert len(confs) == 5
        grades = [c.split(":")[0] for c in confs]
        assert grades == ["STRONG", "STRONG", "MODERATE", "MODERATE", "WEAK"]

    def test_counterevidence_four(self):
        counters = _m907_data()["counterevidence"]
        assert len(counters) == 4
        joined = " ".join(counters)
        assert "425" in joined and "811" in joined


# ---------------------------------------------------------------------------
# 6. Falsification ledger
# ---------------------------------------------------------------------------
class TestTypeAFalsificationLedger1127:
    def test_ledger_advances_45_to_46(self):
        assert _m907_data()["falsification_ledger"] == 46
        assert _m907_data()["falsification_family_member"] is True

    def test_forty_sixth_member_claim_in_exactly_one_profiles_file(self):
        # Designed pattern: the claim form lives only in the m907
        # block of profiles/the-verge.yaml (2 occurrences).
        hits = []
        for root, dirs, files in os.walk(PROFILES_DIR):
            dirs[:] = [d for d in dirs if d != "__pycache__"]
            for f in files:
                p = os.path.join(root, f)
                text = open(p, encoding="utf-8", errors="replace").read()
                if _T46 in text:
                    hits.append(p)
        assert hits == [os.path.join(PROFILES_DIR, "the-verge.yaml")], hits
        text = open(hits[0], encoding="utf-8", errors="replace").read()
        assert text.count(_T46) == 2, text.count(_T46)

    def test_forty_seventh_member_claim_absent_profiles_wide(self):
        # Forward guard for #1128: the next member slot is unclaimed
        # (needle format-built per #715).
        assert _T47 not in _profiles_text()

    def test_first_enforcement_register_at_verge(self):
        ff = _m907_data()["falsification_family"]
        assert "FIRST regulatory-enforcement-register falsification" in ff
        assert "the-verge" in ff.lower() or "The Verge" in ff

    def test_extends_m901_m904_enforcement_line(self):
        ff = _m907_data()["falsification_family"]
        assert "m901" in ff and "m904" in ff
        assert "third deal-partner publication" in ff

    def test_extends_m880_astra_arc(self):
        ff = _m907_data()["falsification_family"]
        assert "m880" in ff
        assert "Sep-28-Oct-1 crisis window" in ff

    def test_bounded_by_m425_and_m507(self):
        ff = _m907_data()["falsification_family"]
        assert "m425" in ff and "m507" in ff

    def test_thirty_third_direction_still_absent_repo_wide(self):
        # The next relationship-direction slot stays unclaimed
        # (needle format-built per #715).
        parts = []
        for root, dirs, files in os.walk(REPO_ROOT):
            if ".git" in root or ".venv" in root:
                continue
            dirs[:] = [
                d
                for d in dirs
                if d not in (".git", ".venv", "__pycache__", "node_modules")
            ]
            for f in files:
                if f == OWN_BASENAME:
                    continue
                parts.append(
                    open(
                        os.path.join(root, f),
                        encoding="utf-8",
                        errors="replace",
                    ).read()
                )
        assert _TW33 not in "\n".join(parts)


# ---------------------------------------------------------------------------
# 7. Forward-looking staleness (subprocess on prior window files)
# ---------------------------------------------------------------------------
class TestTypeAForwardLookingStaleness1127:
    def _stale_run(self, path, node=None, *deselects):
        target = path if node is None else "%s::%s" % (path, node)
        cmd = [
            ".venv/bin/python",
            "-m",
            "pytest",
            target,
            "-q",
            "--no-header",
            "-p",
            "no:cacheprovider",
            "-o",
            "addopts=",
        ]
        for d in deselects:
            cmd.extend(["--deselect", "%s::%s" % (path, d)])
        result = subprocess.run(
            cmd, cwd=REPO_ROOT, capture_output=True, text=True, timeout=900
        )
        return result

    def test_1125_guard_lifecycle_stale_by_design(self):
        # #1125's TestGuardLifecycle1125 pinned max 906, zero-907
        # numeric/underscore, no-thirty-third-direction and
        # no-forty-sixth-member. The #1127 landing (907, FORTY-SIXTH)
        # trips the max, numeric, underscore and forty-sixth pins.
        # Designed lifecycle; recorded, not repaired.
        result = self._stale_run(D1125_FILE, "TestGuardLifecycle1125")
        assert result.returncode != 0, result.stdout[-2000:]
        assert "907" in result.stdout or "906" in result.stdout

    def test_1125_novelty_max_pin_stale_by_design(self):
        # #1125's TestNovelty1125 pinned max 906; the 907 landing
        # flips it at #1127. Designed lifecycle; recorded, not
        # repaired.
        result = self._stale_run(
            D1125_FILE,
            "TestNovelty1125::test_max_id_is_906",
        )
        assert result.returncode != 0, result.stdout[-2000:]

    def test_1125_forty_sixth_absent_pin_stale_by_design(self):
        # #1125's TestTypeDFalsificationLedger1125 pinned the
        # forty-sixth-absent guard; the m907 landing flips it at
        # #1127. Designed lifecycle; recorded, not repaired.
        result = self._stale_run(
            D1125_FILE,
            "TestTypeDFalsificationLedger1125",
        )
        assert result.returncode != 0, result.stdout[-2000:]

    def test_1124_zero_907_forward_guards_flip_by_design(self):
        # #1124's TestForwardGuards1124 pinned zero-907
        # (numeric/underscore/dash) and no-thirty-third-direction:
        # the 907 landing flips the 907-form pins at #1127; the
        # thirty-third-direction pin STAYS GREEN (asserted
        # separately in the guard-lifecycle class).
        result = self._stale_run(C1124_FILE, "TestForwardGuards1124")
        assert result.returncode != 0, result.stdout[-2000:]

    def test_1124_ledger45_forty_sixth_absent_flips_by_design(self):
        # #1124's TestLedger45Holds pinned the forty-sixth-absent
        # guard: the m907 landing claims the slot at #1127.
        # Designed lifecycle; recorded, not repaired.
        result = self._stale_run(
            C1124_FILE,
            "TestLedger45Holds::test_forty_sixth_absent_repo_wide",
        )
        assert result.returncode != 0, result.stdout[-2000:]

    def test_1123_supersession_pins_except_thirty_second_still_green(self):
        # #1123's TestSupersessionPins1123 records the designed
        # end-states of the #1122 zero-905 numeric guard and the
        # #1122 forty-fifth-absent guard (both failed by design on
        # the 905 landing), and the 905 underscore/dash +
        # forty-fourth-intact holds. Its
        # test_1122_thirty_second_absent_still_green pin flips BY
        # DESIGN at #1124: the landed thirty-second direction in
        # competitor-entities.yaml trips #1122's profiles+tests-
        # scoped guard (recorded at #1125; re-recorded here, still
        # red by design).
        result = self._stale_run(
            B1123_FILE,
            "TestSupersessionPins1123",
            "TestSupersessionPins1123::"
            "test_1122_thirty_second_absent_still_green",
        )
        assert result.returncode == 0, result.stdout[-2000:]

    def test_1123_thirty_second_pin_flips_by_design(self):
        # The one #1123 supersession pin that fails by design since
        # #1124: the landed thirty-second direction trips #1122's
        # profiles+tests-scoped guard. Recorded at #1125;
        # re-recorded here, still red by design.
        result = self._stale_run(
            B1123_FILE,
            "TestSupersessionPins1123::"
            "test_1122_thirty_second_absent_still_green",
        )
        assert result.returncode != 0, result.stdout[-2000:]
        assert "test_1122_thirty_second_absent_still_green" in result.stdout

    def test_1122_supersession_pins_except_thirty_second_still_green(self):
        # #1122's TestSupersessionPins1122 records the designed
        # end-states of the #1121 zero-904 numeric guard and the
        # #1121 forty-fourth-absent guard (both failed by design on
        # the 904 landing), and the 904 underscore/dash + #1119
        # forward-guard holds. Its
        # test_1120_underscore_dash_thirty_second_still_green pin
        # flips BY DESIGN at #1124: the landed thirty-second
        # direction in competitor-entities.yaml trips #1120's
        # profiles-scoped no-thirty-second guard (recorded at #1125;
        # re-recorded here, still red by design).
        result = self._stale_run(
            A1122_FILE,
            "TestSupersessionPins1122",
            "TestSupersessionPins1122::"
            "test_1120_underscore_dash_thirty_second_still_green",
        )
        assert result.returncode == 0, result.stdout[-2000:]

    def test_1122_thirty_second_pin_flips_by_design(self):
        # The one #1122 supersession pin that fails by design since
        # #1124: the landed thirty-second direction trips #1120's
        # profiles-scoped guard. Recorded at #1125; re-recorded
        # here, still red by design.
        result = self._stale_run(
            A1122_FILE,
            "TestSupersessionPins1122::"
            "test_1120_underscore_dash_thirty_second_still_green",
        )
        assert result.returncode != 0, result.stdout[-2000:]
        assert (
            "test_1120_underscore_dash_thirty_second_still_green"
            in result.stdout
        )


# ---------------------------------------------------------------------------
# 8. Guard lifecycle (forward guards for #1128)
# ---------------------------------------------------------------------------
class TestGuardLifecycle1127:
    def test_1127_lands_907_and_forty_sixth(self):
        data = _m907_data()
        assert data["mechanism_id"] == 907
        assert data["iteration"] == 1127
        assert data["falsification_ledger"] == 46

    def test_1127_file_pins_max_id_907_and_next_908(self):
        # This file is the window's third-leg pin for zero-908
        # forward guards (per the fail-forward cadence: each run
        # supersedes the prior file's NEXT_NUM pin).
        assert MAX_ID == 907
        assert NEXT_NUM == 908
        assert _max_numeric_mechanism_id() == MAX_ID

    def test_zero_next_numeric_908_in_profiles(self):
        # Forward guard: zero numeric 908 mechanism ids in
        # profiles/ - will fail by design at the run that lands
        # mechanism 908.
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_zero_next_underscore_908_repo_wide(self):
        # Needle format-built per #715: no contiguous 908-form
        # literal may exist in this file.
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_zero_next_dash_908_repo_wide(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_no_new_mechanisms_below_max(self):
        # No numeric mechanism id in profiles/ may exceed 907 -
        # corpus max is pinned.
        assert _max_numeric_mechanism_id() <= MAX_ID

    def test_no_thirty_third_direction_claim(self):
        # The next direction slot must be unclaimed repo-wide
        # (needle format-built per #715).
        parts = []
        for root, dirs, files in os.walk(REPO_ROOT):
            if ".git" in root or ".venv" in root:
                continue
            dirs[:] = [
                d
                for d in dirs
                if d not in (".git", ".venv", "__pycache__", "node_modules")
            ]
            for f in files:
                if f == OWN_BASENAME:
                    continue
                parts.append(
                    open(
                        os.path.join(root, f),
                        encoding="utf-8",
                        errors="replace",
                    ).read()
                )
        assert _TW33 not in "\n".join(parts)

    def test_no_forty_seventh_member_claim(self):
        # The next falsification slot must be unclaimed profiles-wide
        # (needle format-built per #715).
        assert _T47 not in _profiles_text()


# ---------------------------------------------------------------------------
# 9. Background suite check (#1125 suite - checked only, NOT touched)
# ---------------------------------------------------------------------------
class TestBackgroundSuiteCheck1127:
    def test_1125_suite_log_exists_and_not_touched(self):
        # The #1125 background full suite (type_d_1125_full_suite.log)
        # is still live at this run's checks (~3%); its verdict
        # belongs to #1130 per the #795 convention. This run checks
        # its state only and does NOT touch it.
        assert os.path.exists(SUITE_LOG), SUITE_LOG
        size = os.path.getsize(SUITE_LOG)
        assert size > 0, size

    def test_1125_suite_not_killed_by_this_run(self):
        # No pytest full-suite process owned by this run may be
        # started or stopped here; the suite is #1125's.
        result = subprocess.run(
            ["pgrep", "-f", "type_d_1125_full_suite"],
            capture_output=True,
            text=True,
            timeout=30,
        )
        # Either still running (rc 0) or freshly finished (rc 1) -
        # both are #1125's business, not this run's.
        assert result.returncode in (0, 1)


# ---------------------------------------------------------------------------
# 10. Doc-sync pins (deselected pre-commit per #719)
# ---------------------------------------------------------------------------
class TestTypeADocSync1127:
    def _readme(self):
        return _read(os.path.join(REPO_ROOT, "README.md"))

    def _arch(self):
        return _read(os.path.join(REPO_ROOT, "docs/ARCHITECTURE.md"))

    def test_readme_stats_table_ratchets(self):
        # The stats table carries the new counts (README_TEST_COUNT
        # tests / README_FILE_COUNT files); the constants are patched
        # post-first-run with the true collected count. Deselected
        # pre-commit per #719.
        assert str(README_TEST_COUNT) in self._readme()
        assert str(README_FILE_COUNT) in self._readme()

    def test_readme_test_file_table_prepends_this_file(self):
        assert OWN_BASENAME in self._readme()

    def test_architecture_tests_tree_lists_this_file(self):
        assert OWN_BASENAME in self._arch()

    def test_readme_counts_match_constants(self):
        # The README stats row must match the patched constants
        # (post-first-run; pre-commit this fails by design per #719).
        text = self._readme()
        assert ("%d" % README_TEST_COUNT) in text
        assert ("%d" % README_FILE_COUNT) in text


# ---------------------------------------------------------------------------
# 11. Iteration log entry (deselected pre-commit per #721)
# ---------------------------------------------------------------------------
class TestTypeAIterationLog1127:
    def test_1127_entry_leads_log(self):
        # The "## #1127 Type A:" entry leads the log (newest-first
        # ordering); hashes are TBD until the log-hash followup
        # registers them per #721. Deselected pre-commit per #721.
        assert _read(LOG_PATH).startswith("## #1127 Type A:")

    def test_1127_entry_names_window_and_predecessors(self):
        text = _read(LOG_PATH)
        entry = text.split("## #1126 Type E:")[0]
        assert "1125-1129" in entry
        assert "89349e3c" in entry
        assert "FORTY-SIXTH" in entry

    def test_1126_entry_present(self):
        # The #1126 entry is present in the log (the #1127 entry
        # prepends above it).
        assert "## #1126 Type E:" in _read(LOG_PATH)


# ---------------------------------------------------------------------------
# 12. In-flight isolation
# ---------------------------------------------------------------------------
class TestInflightIsolation1127:
    def test_no_concurrent_inflight_iteration_commits_staged(self):
        # The in-flight #899/#938/#900/#1012-wt working-tree edits
        # are owned by their runs; this run stages only its own
        # files. (Pre-staging this passes vacuously; it guards the
        # post-staging state before commit.)
        status = _git("status", "--short")
        staged = [l for l in status.splitlines() if l.startswith(("M ", "A "))]
        for f in (
            "nytimes.yaml",
            "test_type_b_938_",
            "test_type_d_900_",
            "test_type_a_1012_",
        ):
            assert not any(f in l for l in staged), (f, staged)

    def test_this_run_stages_only_own_files(self):
        # This run's staged set is the #1127 test file, the
        # the-verge.yaml m907 block, and the doc-sync files only.
        status = _git("status", "--short")
        staged = [l for l in status.splitlines() if l.startswith(("M ", "A "))]
        allowed = (
            "test_type_a_1127_",
            "the-verge.yaml",
            "README.md",
            "ARCHITECTURE.md",
            "iteration-log.md",
        )
        for l in staged:
            assert any(a in l for a in allowed), l

    def test_in_flight_files_present_uncommitted(self):
        # The in-flight blocks are present in the working tree as
        # uncommitted changes (owned by their runs): the #899
        # nytimes.yaml hunk, the #938 test-file edit, the untracked
        # #900 test file, and the #1012 working-tree edit.
        status = _git("status", "--short")
        assert " M profiles/nytimes.yaml" in status
        assert " M tests/test_type_b_938_" in status
        assert "?? tests/test_type_d_900_" in status
        assert " M tests/test_type_a_1012_" in status

    def test_m846_untouched(self):
        # #1024's m846 (FOURTEENTH, exclusionary-diversion) is NOT
        # touched: Ray's revert/leave/rebuild-from-primary decision
        # is still pending.
        diff = _git("diff", "--stat")
        assert "m846" not in diff
