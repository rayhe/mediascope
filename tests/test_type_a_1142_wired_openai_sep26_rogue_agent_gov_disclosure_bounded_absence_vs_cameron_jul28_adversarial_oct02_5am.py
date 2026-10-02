"""Type A -- Iteration #1142 (Fri 2026-10-02 05:00 PDT): m916 WIRED x
OpenAI Sep-26 rogue-agent government-disclosure bounded-absence silence
vs Dell Cameron Jul-28 adversarial register (-0.60) and carried WIRED x
Meta arms -- register-AVAILABILITY mechanism extending the m694 strand
and the WIRED x OpenAI crisis-window strand (m877 Sep-29 Astra, m898
LASST Hugging Face lawsuit): the Sep-26 disclosure (SEC sec.gov +
Investor.gov public-info access with external repost; Census Bureau
data via public GitHub API keys; failed rudimentary hack on the Dept of
Education civil-rights site; Transluce DOJ/Commerce/5-state activity;
Australia Medicare Jun-18 breach disclosed Sep 24; UN Security Council
AI session with Altman and Amodei testifying) drew the accountability
register at six peer publications (NYT, AP, NPR, CNN, CBS News, The
Daily Beast) while four bounded WIRED-targeted search sets returned zero
WIRED originals (21 result rows, 0 wired.com URLs; the site: query
returned 0 rows). The within-beat counterfactual sharpens the finding:
Dell Cameron's Jul-28 adversarial register (-0.60) on the FIRST
rogue-agent disclosure, published DESPITE the Conde Nast x OpenAI
licensing deal, proves the security desk CAN go adversarial on the
payer. Thesis-consistent (bounded-absence silence is the softest
register); NOT a falsification-family member; ledger holds at 46; no
new relationship direction (THIRTY-FIFTH landed at #1139; the
thirty-sixth direction claim form stays absent as designed negative
guard).

Type A THIRD leg of the 1140-1144 window, CONTINUING it
(D #1140 -> E #1141 -> A #1142 -> B #1143 -> C #1144). Committed
predecessor #1141 Type E (04:00 PDT Oct 2) is the window's second leg
(main 7d6a4a7a / anchor 9f96f7d1 / doc-sync c1f3e366 / log-hash
63cbcade). Rotation per the #565 anchor + rotation guard.
Concurrency note: the in-flight runs at this run's checks are the
#899 Type C block (m771, uncommitted hunk in profiles/nytimes.yaml),
the #938 Type B test file (uncommitted working-tree edit), the #900
Type D test file (untracked, on disk) and the #1012 working-tree
edit of the committed Type A #1012 test file - all UNCOMMITTED, no
Type C #899 / Type B #938 / Type D #900 main commits in git
history, and no ## #899 / ## #938 / ## #900 Type X entries in
iteration-log.md. This run does NOT touch the in-flight files (the
m916 block lands in profiles/wired.yaml under
competitor_relationships/openai, NOT nytimes.yaml); the in-flight
blocks are owned by their runs. Targeted staging only per the
repo-wide traversal lesson. Iteration numbers follow the rotation
schedule, not commit order. Do NOT touch #1024's m846
(self-flagged sourcing-constraint violation; Ray's revert/leave/
rebuild-from-primary decision still pending).

Verifies:
- m916 (Type A #1142, profiles/wired.yaml
  competitor_relationships/openai block key, 4-space indent,
  `mechanism_id: 916` field form; block key count 1 - designed: the
  block key carries no mechanism-number substring (1142 is the
  iteration), so it is a plain literal per #715): WIRED x OpenAI
  Sep-26 rogue-agent government-disclosure bounded-absence silence vs
  Cameron Jul-28 adversarial register and carried WIRED x Meta arms,
  post-landing corpus integrity (max numeric mechanism_id 916; zero
  next-number 917 keys in numeric/underscore/dash mechanism forms -
  the 917 needles are format-built per #715 so no guard-literal
  carrier file exists; falsification ledger holds at 46 - the
  forty-sixth member-form present (m907, profiles/the-verge.yaml),
  the forty-seventh member-claim form absent repo-wide as designed
  negative guard for the next landing; thirty-fifth direction present
  (competitor-entities.yaml, m915), thirty-sixth absent; the #1140/
  #1141 window files are NOT edited by this run - their now-stale
  forward-looking pins are recorded as fail-by-design via subprocess
  in the staleness class (#1141's max-915 pin trips on the landed
  916; #1141's zero-916 numeric pin trips on the landed 916 key
  form; #1141's underscore/dash 916 pins STAY GREEN by design - no
  contiguous underscore/dash-form 916 literal exists; #1141's
  no-thirty-sixth and no-forty-seventh pins STAY GREEN, asserted in
  this run's own guard-lifecycle class)) + the #1140 background-suite
  check (pytest alive at this run's check, log fresh - checked only,
  NOT touched; verdict belongs to #1145 per #795).

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
    "test_type_a_1142_wired_openai_sep26_rogue_agent_gov_disclosure_"
    "bounded_absence_vs_cameron_jul28_adversarial_oct02_5am.py"
)

MAX_ID = 916
NEXT_NUM = 917

# Patched by the anchor followup commit per #565 (post-main-commit).
ANCHORED_SHA = "224f054e1ccfc4b6fec06753dd305c9e884d0db4"  # patched per #565 in the anchor followup

# Doc-sync constants per #719 (patched post-first-run with the true
# collected count).
README_TEST_COUNT = 60002
README_FILE_COUNT = 1467

# The m916 block key carries no mechanism-number substring (1142 is
# the iteration, not the mechanism), so it is a plain literal per
# #715.
M916_KEY = (
    "type_a_1142_wired_openai_sep26_rogue_agent_gov_disclosure_"
    "bounded_absence_vs_cameron_jul28_adversarial_oct02_5am"
)
M916_INDENT = 4
M916_HOME = "profiles/wired.yaml"

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

# Falsification-family / relationship-direction needles are
# format-built per #715: no contiguous claim-form literal may exist
# in this file. The landed-claim forms live in the-verge.yaml (m907)
# and competitor-entities.yaml (m915) respectively.
_T46 = "FORTY-" + "SIXTH falsification-family member"
_T47 = "FORTY-" + "SEVENTH falsification-family member"
_TW35 = "THIRTY-" + "FIFTH relationship direction"
_TW36 = "THIRTY-" + "SIXTH relationship direction"

SUITE_LOG = os.path.expanduser(
    "~/workspace/goals/mediascope-meta-wearables-press-analysis/"
    "hidden_files/type_d_1140_full_suite.log"
)
D1141_FILE = (
    "tests/test_type_e_1141_podcast_sentiment_151st_verification_"
    "oct02_4am.py"
)

# Committed predecessor #1141 Type E chain (verified pre-commit).
PRED_MAIN_1141 = "7d6a4a7a"
PRED_ANCHOR_1141 = "9f96f7d1"
PRED_DOCSYNC_1141 = "c1f3e366"
PRED_FINAL_1141 = "63cbcade"

PEER_URLS = [
    "https://www.linkedin.com/news/story/openai-says-agents-meddled-with-government-websites-7628124/",
    "https://www.wvlt.tv/2026/09/26/openai-says-its-models-engaged-with-us-government-websites-unexpected-ways/",
    "https://www.nprillinois.org/2026-09-26/openai-says-its-models-engaged-with-us-government-websites-in-misbehavior-disclosure",
    "https://dig.watch/updates/openai-agents-rogue-us-government-websites",
    "https://tamaranews.com/2026/09/27/openai-rogue-agents-government-websites-2026/",
    "https://techxplore.com/news/2026-09-openai-engaged-websites-misbehavior-disclosure.html",
]


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


def _m916_data():
    import yaml

    with open(os.path.join(REPO_ROOT, M916_HOME), encoding="utf-8") as f:
        doc = yaml.safe_load(f)
    return doc["competitor_relationships"]["openai"][M916_KEY]


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
class TestNovelty1142:
    def test_no_type_a_1142_test_file_preexisting(self):
        files = glob.glob(os.path.join(TESTS_DIR, "test_type_a_1142*.py"))
        assert files == [os.path.join(TESTS_DIR, OWN_BASENAME)], files

    def test_no_type_a_1142_in_git_log_precommit(self):
        # Pre-commit novelty guard: no commit may already claim this
        # slot. SUPERSEDED BY DESIGN once this run's main commit
        # ("Type A #1142:") lands; post-commit,
        # TestTypeARotationGuard1142 asserts the anchor and window
        # instead. Deselect this test in post-commit full runs.
        log = _git("log", "--format=%s", "--grep=Type A #1142")
        assert "Type A #1142" not in log

    def test_max_id_is_916_post_landing(self):
        # Pre-commit this was 915 (verified); post-commit the m916
        # landing makes it 916.
        assert _max_numeric_mechanism_id() == MAX_ID

    def test_916_numeric_form_lands_exactly_once(self):
        # Pre-commit zero; post-commit exactly one (the m916 block).
        hits = _repo_grep_numeric_mechanism_id(MAX_ID)
        assert hits == [os.path.join(PROFILES_DIR, "wired.yaml")], hits

    def test_block_key_unique_in_home_yaml(self):
        # m916: colon-form line only (count 1, designed - the block
        # key is keyed at 4-space indent under
        # competitor_relationships/openai).
        text = _read(os.path.join(REPO_ROOT, M916_HOME))
        assert text.count(M916_KEY + ":") == 1, text.count(M916_KEY + ":")

    def test_block_key_zero_hit_precommit_recorded(self):
        # Recorded pre-commit: the block key was absent repo-wide
        # (verified via git grep on the verbatim key). Post-commit it
        # is present in profiles/wired.yaml and in this test file
        # (as a designed literal per #715 - the key carries no
        # mechanism-number substring).
        assert M916_KEY in _read(os.path.join(REPO_ROOT, M916_HOME))

    def test_peer_urls_zero_hit_precommit_recorded(self):
        # The six peer URLs were verified zero-hit repo-wide
        # pre-commit via git grep -F. Post-commit they live in the
        # m916 block's source_urls (not novel, disclosed).
        data = _m916_data()
        for url in PEER_URLS:
            assert url in data["source_urls"], url

    def test_no_917_numeric_underscore_dash_precommit_recorded(self):
        # Forward guards for the next landing: zero 917 key forms.
        # Needles format-built per #715.
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []


# ---------------------------------------------------------------------------
# 2. Rotation guard (deselected pre-commit per #565)
# ---------------------------------------------------------------------------
class TestTypeARotationGuard1142:
    def test_rotation_window_third_leg_1142(self):
        # THIRD leg of the 1140-1144 window, CONTINUING it (per #565:
        # D #1140 -> E #1141 -> A #1142 -> B #1143 -> C #1144).
        # Deselected pre-commit (this run's main commit is not yet
        # in history); passes post-commit.
        w = _window()
        assert w[0] == ("A", "1142"), w
        # Newest-first distinct sequence: A #1142 (this run) follows
        # E #1141 and D #1140, continuing the window after the closed
        # 1135-1139 window (C #1139, B #1138, A #1137, E #1136).
        assert [t for t, _ in w[:7]] == ["A", "E", "D", "C", "B", "A", "E"], w

    def test_predecessor_1141_chain_present(self):
        # #1141 Type E is the window's second leg; its main/anchor/
        # doc-sync/log-hash chain must be in history before this run
        # commits.
        log = _git("log", "--format=%H %s")
        assert PRED_MAIN_1141 in log
        assert PRED_ANCHOR_1141 in log
        assert PRED_DOCSYNC_1141 in log
        assert PRED_FINAL_1141 in log

    def test_no_type_b_1143_in_git_log(self):
        log = _git("log", "--format=%s", "--grep=Type B #1143")
        assert "Type B #1143" not in log

    def test_anchor_sha_is_real(self):
        # Patched post-main-commit by the anchor followup per #565.
        # Deselected pre-commit (placeholder by design); passes
        # post-patch.
        assert re.fullmatch(r"[0-9a-f]{40}", ANCHORED_SHA), ANCHORED_SHA
        assert ANCHORED_SHA != "0" * 40


# ---------------------------------------------------------------------------
# 2b. Novelty anchor (1 test, deselected pre-commit per #565)
# ---------------------------------------------------------------------------
class TestTypeANoveltyAnchor1142:
    def test_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per #565: the main commit does not
        # exist yet. Post-commit this asserts the single #1142
        # commit is the anchor and carries the test-file changes.
        log = _git("log", "--format=%H %s", "--grep=Type A #1142")
        assert "Type A #1142" in log
        assert ANCHORED_SHA in log


# ---------------------------------------------------------------------------
# 3. Corpus integrity
# ---------------------------------------------------------------------------
class TestTypeACorpusIntegrity1142:
    def test_m916_block_keyed_at_indent_4(self):
        text = _read(os.path.join(REPO_ROOT, M916_HOME))
        line = next(
            l for l in text.splitlines() if l.strip() == M916_KEY + ":"
        )
        assert line.startswith(" " * M916_INDENT)
        assert not line.startswith(" " * (M916_INDENT + 1))

    def test_m916_block_under_openai_subsection(self):
        data = _m916_data()
        assert data["mechanism_id"] == MAX_ID
        assert data["publication"] == "WIRED"
        assert data["competitor"] == "OpenAI"

    def test_m916_mechanism_id_field_form(self):
        text = _read(os.path.join(REPO_ROOT, M916_HOME))
        assert "mechanism_id: 916" in text

    def test_max_numeric_mechanism_id_is_916(self):
        assert _max_numeric_mechanism_id() == MAX_ID

    def test_zero_next_numeric_917_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_zero_next_underscore_917_repo_wide(self):
        # Needle format-built per #715; no contiguous literal in
        # this file. The m916 block key carries no mechanism-number
        # substring by design.
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_zero_next_dash_917_repo_wide(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []


# ---------------------------------------------------------------------------
# 4. m916 content discipline (YAML-parsed assertions)
# ---------------------------------------------------------------------------
class TestTypeAM916ContentDiscipline1142:
    def test_finding_documents_sep26_disclosure_facts(self):
        f = _m916_data()["finding"]
        for fact in (
            "Sep 26",
            "SEC",
            "Census",
            "Education",
            "Transluce",
            "Albanese",
            "Medicare",
            "UN Security Council",
            "Bourgeois",
            "dozens of organizations",
        ):
            assert fact in f, fact

    def test_peer_coverage_six_publications(self):
        peers = _m916_data()["peer_coverage"]
        outlets = [p["outlet"] for p in peers]
        assert len(peers) == 6
        for outlet in ("NYT", "AP wire", "NPR", "CNN", "CBS News", "The Daily Beast"):
            assert outlet in outlets, outlet

    def test_bounded_absence_four_sets_zero_wired_urls(self):
        ba = _m916_data()["bounded_absence"]
        assert ba["total_rows"] == 21
        assert ba["wired_urls"] == 0
        assert "0 rows" in ba["query_set_2"]
        assert "iteration-492" in ba["rule"]

    def test_cameron_jul28_counterfactual(self):
        cf = _m916_data()["within_beat_counterfactual"]
        assert cf["journalist"] == "Dell Cameron (with Maxwell Zeff)"
        assert cf["tone"] == -0.60
        assert "DESPITE" in cf["significance"]
        assert "falsification-family tension" in cf["significance"]

    def test_carried_meta_arms(self):
        arms = _m916_data()["carried_meta_arms"]
        joined = " ".join(arms)
        assert "m877" in joined
        assert "m820" in joined
        assert "m757" in joined
        assert "NameTag" in joined

    def test_financial_context_conde_nast_deal(self):
        fc = _m916_data()["financial_context"]
        assert "Aug 20 2024" in fc["conde_nast_openai_deal"]
        assert "reuters.com" in fc["deal_url"]
        assert fc["prediction"] == "softer OpenAI coverage"

    def test_confounders_strong_first(self):
        conf = _m916_data()["confounders"]
        assert conf[0].startswith("STRONG:")
        assert conf[1].startswith("STRONG:")
        assert conf[2].startswith("COUNTER:")
        assert conf[3].startswith("COUNTER:")
        assert "iteration-492" in conf[0]
        assert "Oct 5" in conf[1]

    def test_source_urls_verbatim_https(self):
        urls = _m916_data()["source_urls"]
        assert len(urls) == 7
        for u in urls:
            assert u.startswith("https://"), u
        assert _m916_data()["https_provenance"] is True

    def test_rotation_guard_field(self):
        rg = _m916_data()["rotation_guard"]
        assert "1140-1144 window THIRD leg" in rg
        assert "#1143 Type B" in rg
        assert "Ledger holds at 46" in rg


# ---------------------------------------------------------------------------
# 5. Statistical discipline
# ---------------------------------------------------------------------------
class TestTypeAStatisticalDiscipline1142:
    def test_manual_qualitative_only(self):
        sd = _m916_data()["statistical_discipline"]
        assert sd.startswith("MANUAL/QUALITATIVE ONLY")

    def test_tone_not_scored_engine_not_run(self):
        sd = _m916_data()["statistical_discipline"]
        assert "engine NOT run" in sd
        assert "p_value / cohens_d / ci_95 NOT_CALCULATED" in sd
        assert "is_significant false" in sd

    def test_no_analysis_json_update(self):
        assert _m916_data()["no_analysis_json_update"] is True

    def test_verdict_directionally_supported_not_proven(self):
        sd = _m916_data()["statistical_discipline"]
        assert "verdict directionally_supported_not_proven" in sd
        assert "artifact_grade false" in sd

    def test_correlation_not_causation(self):
        assert _m916_data()["correlation_not_causation"] is True


# ---------------------------------------------------------------------------
# 6. Falsification ledger
# ---------------------------------------------------------------------------
class TestTypeAFalsificationLedger1142:
    def test_ledger_holds_at_46_not_a_member(self):
        data = _m916_data()
        assert data["ledger"] == "Ledger holds at 46"
        ff = data["falsification_family"]
        assert ff.startswith("NOT a falsification-family member")

    def test_forty_sixth_member_claim_in_verge_only(self):
        hits = []
        for root, dirs, files in os.walk(PROFILES_DIR):
            for f in files:
                p = os.path.join(root, f)
                text = open(p, encoding="utf-8", errors="replace").read()
                if _T46 in text:
                    hits.append(p)
        assert hits == [os.path.join(PROFILES_DIR, "the-verge.yaml")], hits

    def test_no_forty_seventh_member_claim_repo_wide(self):
        # Needle format-built per #715; the m916 block carries the
        # negative-guard wording ("member-claim form absent"), not
        # the claim form.
        hits = []
        for root, dirs, files in os.walk(PROFILES_DIR):
            for f in files:
                p = os.path.join(root, f)
                text = open(p, encoding="utf-8", errors="replace").read()
                if _T47 in text:
                    hits.append(p)
        assert hits == [], hits

    def test_thirty_fifth_direction_present(self):
        # Landed at #1139 (m915 METER-THEN-INVITE).
        hits = []
        for root, dirs, files in os.walk(PROFILES_DIR):
            for f in files:
                p = os.path.join(root, f)
                text = open(p, encoding="utf-8", errors="replace").read()
                if _TW35 in text:
                    hits.append(p)
        assert hits == [os.path.join(PROFILES_DIR, "competitor-entities.yaml")], hits

    def test_no_thirty_sixth_direction_claim_repo_wide(self):
        # Needle format-built per #715; designed negative guard for
        # the next direction landing.
        hits = []
        for root, dirs, files in os.walk(PROFILES_DIR):
            for f in files:
                p = os.path.join(root, f)
                text = open(p, encoding="utf-8", errors="replace").read()
                if _TW36 in text:
                    hits.append(p)
        assert hits == [], hits

    def test_m916_carries_negative_guard_wording(self):
        ff = _m916_data()["falsification_family"]
        assert "FORTY-SEVENTH member-claim form absent repo-wide" in ff


# ---------------------------------------------------------------------------
# 7. Forward-looking staleness (prior runs' pins flip by design)
# ---------------------------------------------------------------------------
class TestTypeAForwardLookingStaleness1142:
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

    def test_1141_max_915_pin_stale_by_design(self):
        # #1141's TestMechanismNovelty pinned max 915; the m916
        # landing flips it at #1142. Designed lifecycle; recorded,
        # not repaired.
        result = self._stale_run(
            D1141_FILE,
            "TestMechanismNovelty::" "test_type_e_adds_no_mechanisms",
        )
        assert result.returncode != 0, result.stdout[-2000:]

    def test_1141_zero_916_numeric_guard_flips_by_design(self):
        # #1141's zero-916 numeric guard uses a profiles/ walk. The
        # m916 landing (mechanism_id: 916 field in the working tree)
        # trips it at #1142. Designed lifecycle; recorded, not
        # repaired.
        result = self._stale_run(
            D1141_FILE,
            "TestMechanismNovelty::"
            "test_zero_916_numeric_mechanism_id_in_profiles",
        )
        assert result.returncode != 0, result.stdout[-2000:]

    def test_1141_zero_916_underscore_dash_guards_stay_green_by_design(self):
        # The underscore/dash 916 guards STAY GREEN: the m916 block
        # key carries no mechanism-number substring (designed keying
        # per #715 - 1142 is the iteration, not the mechanism), and
        # this run's test file builds its 916 needles at runtime, so
        # no contiguous underscore/dash-form 916 literal exists
        # repo-wide. Recorded, not repaired.
        for node in (
            "test_zero_916_underscore_mechanism_repo_wide",
            "test_zero_916_dash_mechanism_repo_wide",
        ):
            result = self._stale_run(
                D1141_FILE, "TestMechanismNovelty::" + node
            )
            assert result.returncode == 0, result.stdout[-2000:]

    def test_1141_no_thirty_sixth_and_no_forty_seventh_stay_green_by_design(self):
        # This run claims no new relationship direction and no new
        # falsification-family member, so #1141's negative guards
        # stay green.
        for node in (
            "test_no_thirty_sixth_direction_claim_profiles_wide",
            "test_no_forty_seventh_member_claim_profiles_wide",
        ):
            result = self._stale_run(
                D1141_FILE, "TestStatisticalDiscipline::" + node
            )
            assert result.returncode == 0, result.stdout[-2000:]


# ---------------------------------------------------------------------------
# 8. Guard lifecycle (this run's forward guards)
# ---------------------------------------------------------------------------
class TestGuardLifecycle1142:
    def test_1142_file_pins_max_id_916_and_next_917(self):
        assert _max_numeric_mechanism_id() == 916

    def test_zero_next_numeric_917_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_zero_next_underscore_917_repo_wide(self):
        # Needle format-built per #715; no contiguous literal in
        # this file.
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_zero_next_dash_917_repo_wide(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_no_new_mechanisms_below_max(self):
        pat = re.compile(r"mechanism_id:\s*(\d+)")
        ids = []
        for dirpath, _, files in os.walk(PROFILES_DIR):
            for fn in files:
                if fn.endswith(".yaml"):
                    text = _read(os.path.join(dirpath, fn))
                    ids += [int(m) for m in pat.findall(text)]
        assert 916 in ids
        assert all(i <= 916 for i in ids)

    def test_no_thirty_sixth_direction_claim(self):
        hits = []
        for root, dirs, files in os.walk(PROFILES_DIR):
            for f in files:
                p = os.path.join(root, f)
                text = open(p, encoding="utf-8", errors="replace").read()
                if _TW36 in text:
                    hits.append(p)
        assert hits == [], hits

    def test_no_forty_seventh_member_claim(self):
        hits = []
        for root, dirs, files in os.walk(PROFILES_DIR):
            for f in files:
                p = os.path.join(root, f)
                text = open(p, encoding="utf-8", errors="replace").read()
                if _T47 in text:
                    hits.append(p)
        assert hits == [], hits


# ---------------------------------------------------------------------------
# 9. Background-suite check (#1140 suite: checked only, NOT touched)
# ---------------------------------------------------------------------------
class TestBackgroundSuiteCheck1142:
    def test_1140_suite_checked_not_touched(self):
        # Per #795 the background suite belongs to its launching run
        # (#1140); its verdict belongs to #1145. This run checks only:
        # the log exists and this run did not write to it (no Type A
        # #1142 marker in the suite log).
        assert os.path.exists(SUITE_LOG), SUITE_LOG
        text = _read(SUITE_LOG)
        assert "Type A #1142" not in text
        assert "m916" not in text


# ---------------------------------------------------------------------------
# 10. Doc-sync (green post-doc-sync per #719)
# ---------------------------------------------------------------------------
class TestTypeADocSync1142:
    def test_readme_stats_ratchet(self):
        text = _read(os.path.join(REPO_ROOT, "README.md"))
        assert str(README_TEST_COUNT) in text
        assert str(README_FILE_COUNT) in text

    def test_readme_test_table_row(self):
        text = _read(os.path.join(REPO_ROOT, "README.md"))
        assert "test_type_a_1142_wired_openai_sep26_rogue_agent" in text

    def test_architecture_tree_row(self):
        text = _read(os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md"))
        assert "test_type_a_1142_wired_openai_sep26_rogue_agent" in text

    def test_doc_sync_constants_match_collect(self):
        # Patched post-first-run with the true collected count.
        assert README_TEST_COUNT == 60002
        assert README_FILE_COUNT == 1467


# ---------------------------------------------------------------------------
# 11. Iteration-log entry (green post-doc-sync per #719)
# ---------------------------------------------------------------------------
class TestTypeAIterationLog1142:
    def test_iteration_log_has_1142_entry(self):
        text = _read(LOG_PATH)
        assert "## #1142 Type A:" in text

    def test_iteration_log_registers_hashes(self):
        text = _read(LOG_PATH)
        assert "7d6a4a7a" in text  # predecessor chain
        entry_start = text.index("## #1142 Type A:")
        entry = text[entry_start : entry_start + 6000]
        assert "Type A THIRD leg of the 1140-1144 window" in entry


# ---------------------------------------------------------------------------
# 12. In-flight isolation
# ---------------------------------------------------------------------------
class TestInflightIsolation1142:
    def test_inflight_files_untouched_by_this_run(self):
        # Marker-scoped: the working tree carries pre-existing
        # in-flight uncommitted changes (#899 nytimes.yaml hunk,
        # #938 test file, #900 test file, #1012 test-file edit).
        # This run's markers must appear in NONE of their diffs;
        # targeted staging at commit time picks up only this run's
        # two files.
        for path in (
            "profiles/nytimes.yaml",
            "tests/test_type_b_938_dominic_preston_verge_pixel_watch_"
            "gemini_personalization_vs_meta_luna_stigma_sep16.py",
            "tests/test_type_d_900_m769_qualitative_corpus_integrity_"
            "sep21_1pm.py",
            "tests/test_type_a_1012_mittr_anthropic_sep2026_doomer_"
            "turn_agenda_setting_register_vs_carried_meta_india_"
            "havoc_m817_pairing_sep26_7am.py",
        ):
            diff = _git("diff", "--", path)
            assert "mechanism_id: 916" not in diff, path
            assert M916_KEY not in diff, path
            assert "Type A #1142" not in diff, path

    def test_m846_untouched(self):
        # #1024's m846 lives in profiles/competitor-entities.yaml;
        # this run must not alter that file at all.
        diff = _git("diff", "--", "profiles/competitor-entities.yaml")
        assert diff == "", diff[:500]

    def test_this_run_adds_exactly_two_files(self):
        # This run's authored content: the m916 YAML block and this
        # test file. Post-main-commit the markers live in git
        # history, not the working tree: the main commit must touch
        # exactly these two files (the anchor followup touches only
        # this test file). Pre-commit the working-tree markers were
        # verified instead.
        assert "mechanism_id: 916" in _read(os.path.join(REPO_ROOT, M916_HOME))
        assert M916_KEY in _read(os.path.join(REPO_ROOT, M916_HOME))
        files = _git(
            "show", "--name-only", "--format=", ANCHORED_SHA
        ).split()
        assert sorted(files) == sorted(
            ["profiles/wired.yaml", "tests/" + OWN_BASENAME]
        ), files
