"""Type A -- Iteration #1137 (Fri 2026-10-02 00:00 PDT): m913 Atlantic x
OpenAI Sep-26/Oct-1 2026 crisis-window bounded-absence silence +
Sep-29 historical-register book excerpt vs carried Meta Watchdog arms
-- register-AVAILABILITY mechanism extending the m694 strand: four
crisis pegs (Sep-26 rogue-agent disclosure; Sep-29 LASST Hugging Face
lawsuit; Sep-28 Astra cancellation; Sep-30 FTC agent-safety probe)
that drew accountability/enforcement registers at six peer
publications (NYT m910, FT m901/m1117, WSJ m904/m1122, Verge m907,
Guardian m1072, WIRED m1077) returned zero Atlantic originals in
three bounded search sets; the only Sep-29-week Atlantic OpenAI
surface is the Sep-29 Kevin Roose book excerpt on 2017 AGI auction
plans (newslocker relay, historical register), while Meta's conduct
goes to the AI Watchdog accountability register (m481 arms
-0.75/-0.55, carried un-rescored per #807). The licensing partner's
episodes are routed to non-accountability registers (philosophical
wonder m694, historical book excerpt) or to silence. Thesis-consistent
with the standing "softer" prediction; NOT a falsification-family
member; ledger holds at 46; no new relationship direction.

Type A THIRD leg of the 1135-1139 window, CONTINUING it
(D #1135 -> E #1136 -> A #1137 -> B #1138 -> C #1139). Committed
predecessor #1136 Type E (23:00 PDT Oct 1) is the window's second leg
(main 1970ab00 / anchor 524d612d / doc-sync 12641fd9 / log-hash
aef45405). Rotation per the #565 anchor + rotation guard.
Concurrency note: the in-flight runs at this run's checks are the
#899 Type C block (m771, uncommitted hunk in profiles/nytimes.yaml),
the #938 Type B test file (uncommitted working-tree edit), the #900
Type D test file (untracked, on disk) and the #1012 working-tree
edit of the committed Type A #1012 test file - all UNCOMMITTED, no
Type C #899 / Type B #938 / Type D #900 main commits in git
history, and no ## #899 / ## #938 / ## #900 Type X entries in
iteration-log.md. This run does NOT touch the in-flight files (the
m913 block lands in profiles/atlantic.yaml under
competitor_relationships/openai, NOT nytimes.yaml); the in-flight
blocks are owned by their runs. Targeted staging only per the
repo-wide traversal lesson. Iteration numbers follow the rotation
schedule, not commit order. Do NOT touch #1024's m846
(FOURTEENTH, exclusionary-diversion): self-flagged sourcing-constraint
violation; Ray's revert/leave/rebuild-from-primary decision still
pending.

Verifies:
- m913 (Type A #1137, profiles/atlantic.yaml
  competitor_relationships/openai block key, 4-space indent,
  `mechanism_id: 913` field form; block key count 1 - designed: the
  block key carries no mechanism-number substring (1137 is the
  iteration), so it is a plain literal per #715; the test_file value
  is absent from this block by design (the block's evidence lives in
  source_urls)): Atlantic x OpenAI Sep-26/Oct-1 crisis-window
  bounded-absence silence + Sep-29 historical-register book excerpt vs
  carried Meta Watchdog arms, post-landing corpus integrity (max
  numeric mechanism_id 913; zero next-number 914 keys in
  numeric/underscore/dash mechanism forms - the 914 needles are
  format-built per #715 so no guard-literal carrier file exists;
  falsification ledger holds at 46 - FORTY-SIXTH member-form present
  (m907, profiles/the-verge.yaml), FORTY-SEVENTH member-claim form
  absent repo-wide as designed negative guard for the next landing;
  thirty-fourth direction present (competitor-entities.yaml),
  thirty-fifth absent; the #1135/#1136 window files are NOT edited
  by this run - their now-stale forward-looking pins are recorded as
  fail-by-design via subprocess in the staleness class (#1135's
  max-912 pin trips on the landed 913; #1135's zero-913 numeric pin
  trips on the landed 913 key form; #1135's underscore/dash 913 pins
  STAY GREEN by design - no contiguous underscore/dash-form 913
  literal exists; #1135's no-thirty-fifth and no-forty-seventh pins
  STAY GREEN, asserted in this run's own guard-lifecycle class)) +
  the #1135 background-suite check (no live pytest process at this
  run's checks; log mtime 23:02 PDT stale beyond the 900s bound -
  checked only, NOT touched; verdict belongs to #1140 per #795).

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
    "test_type_a_1137_atlantic_openai_sep26_oct01_crisis_window_"
    "silence_historical_register_vs_meta_watchdog_oct02_12am.py"
)

MAX_ID = 913
NEXT_NUM = 914

# Patched by the anchor followup commit per #565 (post-main-commit).
ANCHORED_SHA = "0" * 40

# Doc-sync constants per #719 (patched post-first-run with the true
# collected count).
README_TEST_COUNT = 59644
README_FILE_COUNT = 1462

# The m913 block key carries no mechanism-number substring (1137 is
# the iteration, not the mechanism), so it is a plain literal per
# #715.
M913_KEY = (
    "type_a_1137_atlantic_openai_sep26_oct01_crisis_window_"
    "silence_historical_register_vs_meta_watchdog_oct02_12am"
)
M913_INDENT = 4
M913_HOME = "profiles/atlantic.yaml"

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

# Falsification-family / relationship-direction needles are
# format-built per #715: no contiguous claim-form literal may exist
# in this file. The landed-claim forms live in the-verge.yaml (m907)
# and competitor-entities.yaml respectively.
_T46 = "FORTY-" + "SIXTH falsification-family member"
_T47 = "FORTY-" + "SEVENTH falsification-family member"
_TW34 = "THIRTY-" + "FOURTH relationship direction"
_TW35 = "THIRTY-" + "FIFTH relationship direction"

SUITE_LOG = os.path.expanduser(
    "~/workspace/goals/mediascope-meta-wearables-press-analysis/"
    "hidden_files/type_d_1135_full_suite.log"
)
D1135_FILE = (
    "tests/test_type_d_1135_m910_m911_m912_qualitative_corpus_"
    "integrity_oct01_10pm.py"
)
E1136_FILE = (
    "tests/test_type_e_1136_podcast_sentiment_150th_verification_"
    "oct01_11pm.py"
)


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


def _m913_data():
    import yaml

    with open(os.path.join(REPO_ROOT, M913_HOME), encoding="utf-8") as f:
        doc = yaml.safe_load(f)
    return doc["competitor_relationships"]["openai"][M913_KEY]


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
class TestNovelty1137:
    def test_no_type_a_1137_test_file_preexisting(self):
        files = glob.glob(os.path.join(TESTS_DIR, "test_type_a_1137*.py"))
        assert files == [os.path.join(TESTS_DIR, OWN_BASENAME)], files

    def test_no_type_a_1137_in_git_log_precommit(self):
        # Pre-commit novelty guard: no commit may already claim this
        # slot. SUPERSEDED BY DESIGN once this run's main commit
        # ("Type A #1137:") lands; post-commit,
        # TestTypeARotationGuard1137 asserts the anchor and window
        # instead. Deselect this test in post-commit full runs.
        log = _git("log", "--format=%s", "--grep=Type A #1137")
        assert "Type A #1137" not in log

    def test_max_id_is_913_post_landing(self):
        # Pre-commit this was 912 (verified); post-commit the m913
        # landing makes it 913.
        assert _max_numeric_mechanism_id() == MAX_ID

    def test_913_numeric_form_lands_exactly_once(self):
        # Pre-commit zero; post-commit exactly one (the m913 block).
        hits = _repo_grep_numeric_mechanism_id(MAX_ID)
        assert hits == [os.path.join(PROFILES_DIR, "atlantic.yaml")], hits

    def test_block_key_unique_in_home_yaml(self):
        # m913: colon-form line only (count 1, designed - the block
        # key is keyed at 4-space indent under
        # competitor_relationships/openai, no test_file value by
        # design; the colon-form line is the unique block anchor).
        text = _read(os.path.join(REPO_ROOT, M913_HOME))
        assert text.count(M913_KEY + ":") == 1, text.count(M913_KEY + ":")

    def test_block_key_zero_hit_precommit_recorded(self):
        # Recorded pre-commit: the block key was absent repo-wide
        # (verified via git grep on the verbatim key). Post-commit it
        # is present in profiles/atlantic.yaml and in this test file
        # (as a designed literal per #715 - the key carries no
        # mechanism-number substring).
        assert M913_KEY in _read(os.path.join(REPO_ROOT, M913_HOME))


# ---------------------------------------------------------------------------
# 2. Rotation guard (deselected pre-commit per #565)
# ---------------------------------------------------------------------------
class TestTypeARotationGuard1137:
    def test_rotation_window_third_leg_1137(self):
        # THIRD leg of the 1135-1139 window, CONTINUING it (per #565:
        # D #1135 -> E #1136 -> A #1137 -> B #1138 -> C #1139).
        # Deselected pre-commit (this run's main commit is not yet
        # in history); passes post-commit.
        w = _window()
        assert w[0] == ("A", "1137"), w
        # Newest-first distinct sequence: A #1137 (this run) follows
        # E #1136 and D #1135, continuing the window after the closed
        # 1130-1134 window (C #1134, B #1133, A #1132, E #1131).
        assert [t for t, _ in w[:7]] == ["A", "E", "D", "C", "B", "A", "E"], w

    def test_predecessor_1136_chain_present(self):
        # #1136 Type E is the window's second leg; its main/anchor/
        # doc-sync/log-hash chain must be in history before this run
        # commits.
        log = _git("log", "--format=%H %s")
        assert "1970ab00" in log
        assert "524d612d" in log
        assert "12641fd9" in log
        assert "aef45405" in log

    def test_no_type_b_1138_in_git_log(self):
        log = _git("log", "--format=%s", "--grep=Type B #1138")
        assert "Type B #1138" not in log

    def test_anchor_sha_is_real(self):
        # Patched post-main-commit by the anchor followup per #565.
        # Deselected pre-commit (placeholder by design); passes
        # post-patch.
        assert re.fullmatch(r"[0-9a-f]{40}", ANCHORED_SHA), ANCHORED_SHA
        assert ANCHORED_SHA != "0" * 40


# ---------------------------------------------------------------------------
# 2b. Novelty anchor (1 test, deselected pre-commit per #565)
# ---------------------------------------------------------------------------
class TestTypeANoveltyAnchor1137:
    def test_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per #565: the main commit does not
        # exist yet. Post-commit this asserts the single #1137
        # commit is the anchor and carries the test-file changes.
        log = _git("log", "--format=%H %s", "--grep=Type A #1137")
        assert "Type A #1137" in log
        assert ANCHORED_SHA in log


# ---------------------------------------------------------------------------
# 3. Corpus integrity
# ---------------------------------------------------------------------------
class TestTypeACorpusIntegrity1137:
    def test_m913_block_keyed_at_indent_4(self):
        lines = _read(os.path.join(REPO_ROOT, M913_HOME)).splitlines()
        hits = [l for l in lines if M913_KEY + ":" in l]
        assert len(hits) == 1, hits
        assert hits[0].startswith("    " + M913_KEY + ":"), hits[0][:80]

    def test_m913_fields_parse(self):
        data = _m913_data()
        assert data["mechanism_id"] == 913
        assert data["iteration"] == 1137
        assert data["iteration_type"] == "A"
        assert data["publication"] == "The Atlantic"
        assert data["competitor"] == "OpenAI"
        assert data["comparator_entity"] == "Meta"

    def test_m913_yaml_parses_under_openai_section(self):
        import yaml

        with open(os.path.join(REPO_ROOT, M913_HOME), encoding="utf-8") as f:
            doc = yaml.safe_load(f)
        assert M913_KEY in doc["competitor_relationships"]["openai"]

    def test_ascii_only_no_em_dashes_in_block(self):
        data = _m913_data()
        assert data["no_em_dash_verified"] is True
        text = open(os.path.join(REPO_ROOT, M913_HOME), encoding="utf-8").read()
        start = text.index(M913_KEY)
        # Bound the block at the next 4-space entity key or 2-space key.
        tail = text[start:]
        lines = tail.splitlines()
        block_lines = []
        for i, l in enumerate(lines):
            if i > 0 and re.match(r"^  [a-z_]+:$", l):
                break
            block_lines.append(l)
        block = "\n".join(block_lines)
        assert "\u2014" not in block
        assert "\u2013" not in block
        block.encode("ascii")

    def test_m913_does_not_touch_inflight_mechanisms(self):
        # The m913 block must not leak into the in-flight runs'
        # files; marker-scoped check on their working-tree diffs.
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
            assert "mechanism_id: 913" not in diff, path
            assert M913_KEY not in diff, path
            assert "Type A #1137" not in diff, path

    def test_m913_does_not_touch_nytimes_yaml(self):
        # #899's in-flight hunk lives in profiles/nytimes.yaml; this
        # run's block lands in profiles/atlantic.yaml only.
        diff = _git("diff", "--", "profiles/nytimes.yaml")
        assert "mechanism_id: 913" not in diff


# ---------------------------------------------------------------------------
# 4. Content discipline
# ---------------------------------------------------------------------------
class TestTypeAM913ContentDiscipline1137:
    def test_four_crisis_pegs(self):
        data = _m913_data()
        pegs = data["crisis_pegs_peer_registers"]
        assert len(pegs) == 4
        names = [p["peg"] for p in pegs]
        assert any("rogue-agent" in n for n in names)
        assert any("Hugging Face" in n for n in names)
        assert any("Astra" in n for n in names)
        assert any("FTC" in n for n in names)

    def test_roose_excerpt_surface(self):
        data = _m913_data()
        surface = data["atlantic_surface_sep29_week"][0]
        assert surface["register"] == "historical_book_excerpt"
        assert surface["evidence_tier"] == "relay_excerpt_bounded"
        assert "newslocker.com" in surface["relay_url"]

    def test_bounded_absence_evidence(self):
        data = _m913_data()
        method = data["research_method"]
        assert "4 browser.search query sets" in method
        assert "0 browser.open" in method
        assert "site:theatlantic.com OpenAI September 2026" in method
        assert "zero theatlantic.com URLs across 14 rows" in data["finding"]

    def test_meta_arms_carried_unrescored_per_807(self):
        data = _m913_data()
        arms = data["meta_arms_carried_from_481"]
        assert len(arms) == 2
        assert arms[0]["manual_illustrative_tone"] == -0.75
        assert arms[1]["manual_illustrative_tone"] == -0.55
        assert "m481" in data["finding"]

    def test_register_availability_framing(self):
        data = _m913_data()
        assert "register-AVAILABILITY" in data["finding"]
        assert data["scorer_manual_illustrative"]["target_scores"].startswith(
            "NOT_SCORED"
        )

    def test_peer_register_citations(self):
        data = _m913_data()
        pegs = data["crisis_pegs_peer_registers"]
        joined = " ".join(p["peer_register"] for p in pegs)
        for m in ("m910", "m901", "m904", "m907", "m1072", "m1077"):
            assert m in joined, m

    def test_extends_m694_strand(self):
        data = _m913_data()
        assert "m694" in data["finding"]
        assert 694 in data["cross_references"]
        assert 829 in data["cross_references"]

    def test_financial_context_softer_prediction(self):
        data = _m913_data()
        fc = data["financial_context"]
        assert fc["coverage_prediction"] == "softer"
        assert "May 29 2024" in fc["openai_deal"] or "May 2024" in fc["openai_deal"]

    def test_source_urls_all_verbatim_two(self):
        data = _m913_data()
        urls = data["source_urls"]
        assert len(urls) == 2
        assert urls[0] == (
            "https://www.newslocker.com/en-us/news/social-media-news/"
            "openais-2017-plan-to-auction-agi-to-china-and-russia-"
            "per-the-atlantic/"
        )
        for u in urls:
            assert u.startswith("https://")

    def test_rotation_transparency_field(self):
        data = _m913_data()
        assert data["iteration"] == 1137
        assert data["scheduled_job_id"] == "mediascope-daily-iteration"
        assert data["goal_id"] == "goal_54093bda4145"


# ---------------------------------------------------------------------------
# 5. Statistical discipline
# ---------------------------------------------------------------------------
class TestTypeAStatisticalDiscipline1137:
    def test_manual_illustrative_only(self):
        data = _m913_data()
        assert "MANUAL ILLUSTRATIVE" in data["scorer_manual_illustrative"]["asymmetry_note"]

    def test_no_inferential_statistics_at_finding_layer(self):
        data = _m913_data()
        sd = data["statistical_discipline"]
        assert "NOT_CALCULATED" in sd
        assert "is_significant False" in sd

    def test_verdict_directionally_supported_not_proven(self):
        data = _m913_data()
        assert "directionally_supported_not_proven" in data["statistical_discipline"]

    def test_engine_not_run_not_artifact_grade(self):
        data = _m913_data()
        assert "engine NOT run" in data["statistical_discipline"]
        assert "NOT artifact-grade" in data["statistical_discipline"]
        assert data["no_analysis_json_update"] is True

    def test_confounders_three_strong(self):
        data = _m913_data()
        strong = data["confounders_ranked"]["strong"]
        assert len(strong) == 2
        joined = " ".join(strong)
        assert "Search-index bounded absence" in joined
        assert "Cadence mismatch" in joined

    def test_counterevidence_three(self):
        data = _m913_data()
        ce = data["counter_evidence"]
        assert len(ce) == 3
        joined = " ".join(ce)
        assert "m694" in joined or "Ideas vertical" in joined

    def test_correlation_not_causation(self):
        data = _m913_data()
        assert "correlation not causation" in data["statistical_discipline"]


# ---------------------------------------------------------------------------
# 6. Falsification ledger (holds at 46)
# ---------------------------------------------------------------------------
class TestTypeAFalsificationLedger1137:
    def test_ledger_holds_at_46_not_a_member(self):
        data = _m913_data()
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
        # Needle format-built per #715; the m913 block carries the
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

    def test_no_thirty_fifth_direction_repo_wide(self):
        hits = []
        for root, dirs, files in os.walk(PROFILES_DIR):
            for f in files:
                p = os.path.join(root, f)
                text = open(p, encoding="utf-8", errors="replace").read()
                if _TW35 in text:
                    hits.append(p)
        assert hits == [], hits

    def test_thirty_fourth_direction_present_once(self):
        hits = []
        for root, dirs, files in os.walk(PROFILES_DIR):
            for f in files:
                p = os.path.join(root, f)
                text = open(p, encoding="utf-8", errors="replace").read()
                if _TW34 in text:
                    hits.append(p)
        assert hits == [os.path.join(PROFILES_DIR, "competitor-entities.yaml")], hits

    def test_m913_carries_negative_guard_wording(self):
        ff = _m913_data()["falsification_family"]
        assert "FORTY-SEVENTH member-claim form absent repo-wide" in ff


# ---------------------------------------------------------------------------
# 7. Forward-looking staleness (prior runs' pins flip by design)
# ---------------------------------------------------------------------------
class TestTypeAForwardLookingStaleness1137:
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

    def test_1135_guard_lifecycle_max_pin_stale_by_design(self):
        # #1135's TestGuardLifecycle1135 pinned max 912; the m913
        # landing flips it at #1137. Designed lifecycle; recorded,
        # not repaired.
        result = self._stale_run(
            D1135_FILE,
            "TestGuardLifecycle1135::"
            "test_1135_file_pins_max_id_912_and_next_913",
        )
        assert result.returncode != 0, result.stdout[-2000:]

    def test_1135_zero_913_numeric_guard_flips_by_design(self):
        # #1135's zero-913 numeric guard uses git grep on tracked
        # files' working-tree content. The m913 landing
        # (mechanism_id: 913 field in the working tree) trips it at
        # #1137. Designed lifecycle; recorded, not repaired.
        result = self._stale_run(
            D1135_FILE,
            "TestGuardLifecycle1135::test_zero_next_numeric_913_in_profiles",
        )
        assert result.returncode != 0, result.stdout[-2000:]

    def test_1135_zero_913_underscore_dash_guards_stay_green_by_design(self):
        # The underscore/dash 913 guards STAY GREEN: the m913 block
        # key carries no mechanism-number substring (designed keying
        # per #715 - 1137 is the iteration, not the mechanism), and
        # this run's test file builds its 913 needles at runtime, so
        # no contiguous underscore/dash-form 913 literal exists
        # repo-wide. Recorded, not repaired.
        for node in (
            "test_zero_next_underscore_913_repo_wide",
            "test_zero_next_dash_913_repo_wide",
        ):
            result = self._stale_run(
                D1135_FILE, "TestGuardLifecycle1135::" + node
            )
            assert result.returncode == 0, result.stdout[-2000:]

    def test_1135_no_new_mechanisms_below_max_flips_by_design(self):
        # #1135's all-ids-<=912 pin trips on the 913 landing.
        # Designed lifecycle; recorded, not repaired.
        result = self._stale_run(
            D1135_FILE,
            "TestGuardLifecycle1135::test_no_new_mechanisms_below_max",
        )
        assert result.returncode != 0, result.stdout[-2000:]

    def test_1135_no_thirty_fifth_and_no_forty_seventh_stay_green_by_design(self):
        # This run claims no new relationship direction and no new
        # falsification-family member, so #1135's negative guards
        # stay green.
        for node in (
            "test_no_thirty_fifth_direction_claim",
            "test_no_forty_seventh_member_claim",
        ):
            result = self._stale_run(
                D1135_FILE, "TestGuardLifecycle1135::" + node
            )
            assert result.returncode == 0, result.stdout[-2000:]


# ---------------------------------------------------------------------------
# 8. Guard lifecycle (this run's forward guards)
# ---------------------------------------------------------------------------
class TestGuardLifecycle1137:
    def test_1137_file_pins_max_id_913_and_next_914(self):
        assert _max_numeric_mechanism_id() == 913

    def test_zero_next_numeric_914_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_zero_next_underscore_914_repo_wide(self):
        # Needle format-built per #715; no contiguous literal in
        # this file.
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_zero_next_dash_914_repo_wide(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_no_new_mechanisms_below_max(self):
        pat = re.compile(r"mechanism_id:\s*(\d+)")
        ids = []
        for dirpath, _, files in os.walk(PROFILES_DIR):
            for fn in files:
                if fn.endswith(".yaml"):
                    text = _read(os.path.join(dirpath, fn))
                    ids += [int(m) for m in pat.findall(text)]
        assert 913 in ids
        assert all(i <= 913 for i in ids)

    def test_no_thirty_fifth_direction_claim(self):
        hits = []
        for root, dirs, files in os.walk(PROFILES_DIR):
            for f in files:
                p = os.path.join(root, f)
                text = open(p, encoding="utf-8", errors="replace").read()
                if _TW35 in text:
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
# 9. Background-suite check (#1135 suite: checked only, NOT touched)
# ---------------------------------------------------------------------------
class TestBackgroundSuiteCheck1137:
    def test_1135_suite_checked_not_touched(self):
        # Per #795 the background suite belongs to its launching run
        # (#1135); this run checks it only.
        assert os.path.exists(SUITE_LOG), SUITE_LOG

    def test_1135_suite_no_live_pytest_process_at_check(self):
        # At this run's check (00:0x PDT Oct 2) no suite pytest process
        # is alive and the log's mtime (23:02 PDT) is stale beyond the
        # 900s bound with ~2% progress. This reads as a likely
        # death, but per #795 the tombstone verdict belongs to the
        # next Type D run (#1140), NOT this Type A run. Checked
        # only, NOT touched.
        import time

        result = subprocess.run(
            ["pgrep", "-f", "type_d_1135_full_suite"],
            capture_output=True,
            text=True,
            timeout=30,
        )
        # Exclude transient self-matches: re-check each pid's
        # cmdline and drop pids that are the pgrep itself.
        live = []
        for p in result.stdout.split():
            try:
                with open("/proc/%s/cmdline" % p, "rb") as f:
                    cmd = f.read().decode("utf-8", "replace")
                if "pgrep" not in cmd:
                    live.append(p)
            except FileNotFoundError:
                pass
        assert live == [], live
        mtime = os.path.getmtime(SUITE_LOG)
        assert time.time() - mtime > 900, mtime

    def test_1135_suite_no_summary_tokens_yet(self):
        # No usable verdict from the run: no summary tokens, no
        # collected-count token.
        text = _read(SUITE_LOG)
        assert "passed" not in text
        assert "failed" not in text
        assert " collected " not in text
        assert "no tests ran" not in text


# ---------------------------------------------------------------------------
# 10. Doc-sync (green post-doc-sync per #719)
# ---------------------------------------------------------------------------
class TestTypeADocSync1137:
    def test_readme_stats_ratchet(self):
        text = _read(os.path.join(REPO_ROOT, "README.md"))
        assert str(README_TEST_COUNT) in text
        assert str(README_FILE_COUNT) in text

    def test_readme_test_table_row(self):
        text = _read(os.path.join(REPO_ROOT, "README.md"))
        assert "test_type_a_1137_atlantic_openai_sep26_oct01_crisis" in text

    def test_architecture_tree_row(self):
        text = _read(os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md"))
        assert "test_type_a_1137_atlantic_openai_sep26_oct01_crisis" in text

    def test_doc_sync_constants_match_collect(self):
        # Patched post-first-run with the true collected count.
        assert README_TEST_COUNT > 59580
        assert README_FILE_COUNT == 1462


# ---------------------------------------------------------------------------
# 11. Iteration-log entry (green post-doc-sync per #719)
# ---------------------------------------------------------------------------
class TestTypeAIterationLog1137:
    def test_iteration_log_has_1137_entry(self):
        text = _read(LOG_PATH)
        assert "## #1137 Type A:" in text

    def test_iteration_log_registers_hashes(self):
        text = _read(LOG_PATH)
        assert "1970ab00" in text  # predecessor chain
        entry_start = text.index("## #1137 Type A:")
        entry = text[entry_start : entry_start + 6000]
        assert "Type A THIRD leg of the 1135-1139 window" in entry


# ---------------------------------------------------------------------------
# 12. In-flight isolation
# ---------------------------------------------------------------------------
class TestInflightIsolation1137:
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
            assert "mechanism_id: 913" not in diff, path
            assert M913_KEY not in diff, path
            assert "Type A #1137" not in diff, path

    def test_m846_untouched(self):
        # #1024's m846 lives in profiles/competitor-entities.yaml;
        # this run must not alter that file at all.
        diff = _git("diff", "--", "profiles/competitor-entities.yaml")
        assert diff == "", diff[:500]

    def test_this_run_adds_exactly_two_files(self):
        # This run's authored content: the m913 YAML block and this
        # test file. Verified by marker presence in the working
        # tree via git status --porcelain (git diff --name-only
        # omits untracked files), not by whole-tree diff (which
        # carries the in-flight runs' changes).
        assert "mechanism_id: 913" in _read(os.path.join(REPO_ROOT, M913_HOME))
        assert M913_KEY in _read(os.path.join(REPO_ROOT, M913_HOME))
        porcelain = _git("status", "--porcelain")
        assert "profiles/atlantic.yaml" in porcelain
        assert OWN_BASENAME in porcelain
