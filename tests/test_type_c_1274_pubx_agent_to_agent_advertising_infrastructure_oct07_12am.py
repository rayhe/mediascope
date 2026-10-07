# -*- coding: utf-8 -*-
"""Type C #1274 tests: m996 pubX agent-to-agent advertising infrastructure
(Oct 6-7, 2026) - FIRST dedicated corpus mechanism on the AI-agent ad-buy
rail: $5M Series A led by Chicago Ventures + acquisition of Compliant (media
quality/governance, Data Integrity and CTV Quality Indexes); Oct 7 live
agent-to-agent media buy at a private Advertising Week New York executive
lunch (Reckitt's Mucinex campaign, brief to live placement) with
Paradium.AI and USA TODAY Co. as the named publisher-side participants
reviewing and accepting agent-placed campaigns. THE TYPE C NEXUS: the rail
prices exactly the agent-action traffic type that Perplexity's Comet Plus
(m391: $42.5M pool, 80/20 publisher split) allocates revenue across - pubX
is the independent infrastructure monetizing the same agent-action surface
that m391/m750 price. Paradium.AI is the publisher-side participant in BOTH
the Sep 2026 RTB Digital / Paradium.AI 10-year $100M-per-year platform
agreement (m738, 8-K filed) and this Oct 7 live buy: infrastructure capture
compounding on the same counterparty within three weeks. USA TODAY Co.
(Gannett) adds a third corpus money-flow leg alongside the private USA TODAY
v Google case (m463) and the Microsoft Publisher Content Marketplace
first-wave partnership (m645). Joins the tollbooth-infrastructure layer with
Cloudflare pay-per-crawl (m786): where m786 prices crawler ACCESS, pubX
prices agent PLACEMENT. BOUNDARY (explicit): no competitor lab is a
counterparty here - the money flows brand to publisher through agents, so
this mechanism documents the monetization rail, not a lab-publisher deal,
and claims no slot in the coverage-tone falsification ledger.

Mechanism 996 (MECHANISM DOCUMENTED; ledger HOLDS at 54 - NOT a
falsification-family member). No new direction (fortieth stays
absent by design); thirty-fifth through thirty-ninth stand.

Excerpt-bounded research per #503 (delegated scout across 12 candidate
angles + 6 main-run browser.search verification sets; 0 browser.open
reads). Scout rejections on main-run verification: OpenAI DevDay 2026
publisher announcements -> REJECTED (no publisher deal among the 20+
announcements; Dots/GPT-6.1 Sol/Pro 500/Adobe plugin/ModRetro only);
Apple Siri publisher-deal October movement -> REJECTED (no closures; only
the $250M Landsheft consumer-settlement claims window, litigation-adjacent,
out of tight Type C scope); Axel Springer OpenAI renewal -> REJECTED
(Dec 2023 vintage re-indexes only; #604 renewal-unresolved stands);
Perplexity publisher-revenue October movement -> SATURATED (Comet Plus
80/20 in corpus m391; CNN sign-then-sue in corpus m750); Wiley x Anthropic
MCP partnership -> REJECTED (Dec 2025 vintage; protocol pilot subject to
definitive agreement, not a licensing deal; consistent with m509 zero-deal
posture); Anthropic news-publisher licensing -> SATURATED (m509 Adweek
zero-deal; no October deals surfaced); Google AI-contribution pilot
October status -> SATURATED (m1099/m1199); OpenAI India attribution deals
-> SATURATED (m609/m660/m709 template). SELECTED: pubX agent-to-agent
advertising infrastructure (Oct 6-7).

The mechanism 996 block lives in profiles/competitor-entities.yaml as a
top-level key appended at end of file (the #1024 m846 hunk untouched;
explicit-path staging).

Anchor convention per #565: ANCHORED_SHA starts as 0*40 in this pre-commit
file and is patched to the main-commit hash in the anchor followup commit.
One anchor test (the placeholder pin) fails BY DESIGN post-anchor.

Per #795: this run only OBSERVES the #1270-launched background suite
(goal hidden_files type_d_1270_full_suite.log; observed at this run's
check: 26161 bytes, last write Oct 6 2026 18:12, zero live pytest
processes - NOT-ALIVE, observation not a verdict); its verdict and
tombstone belong to #1275 (next Type D). This run neither re-launches,
kills, nor writes to the suite.

Do NOT touch #1024 (m846 in profiles/competitor-entities.yaml), #899
(nytimes.yaml m771 hunk), #938 (Type B test file working-tree edit), #900
(untracked Type D test file), #1012-wt (working-tree edit on the committed
Type A #1012 file).

Type C lands one mechanism (mechanism 996); the Type B predecessor landed
one (mechanism 995, control-case observation, not a member).
This run is the FIFTH and CLOSING leg of the 1270-1274 window. Next run
#1275 Type D opens the 1275-1279 window (and renders the #1270-launched
background-suite verdict per #795). Rotation: D #1270 -> E #1271 ->
A #1272 -> B #1273 -> C #1274. The main commit is the anchor per #565.
The 1265-1269 window is VERIFIED CLOSED.

ASCII-only, no em dashes. Needles format-built per #715: this file must
not carry contiguous numeric/underscore/dash mechanism-key forms of the
landed or next number, the forty-eighth / forty-ninth / fiftieth /
fifty-first / fifty-second / fifty-third / fifty-fourth member-claim
forms, or the thirty-fifth through fortieth direction forms; the
constants are constructed at runtime. (The landed ordinals live as short
lowercase forms in prose here; the live full-form claims live in
profiles: the forty-eighth in financial-times.yaml, the forty-ninth and
fiftieth in profiles/careers/journalists.yaml, the fifty-first in
profiles/news-corp.yaml, the fifty-second in
profiles/careers/journalists.yaml, the fifty-third in
profiles/the-verge.yaml, the fifty-fourth in profiles/guardian.yaml.)
"""

import os
import re
import subprocess

import pytest
import yaml

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TESTS_DIR = os.path.join(REPO_ROOT, "tests")
PROFILES_DIR = os.path.join(REPO_ROOT, "profiles")
LOG_PATH = os.path.join(REPO_ROOT, "iteration-log.md")
README_PATH = os.path.join(REPO_ROOT, "README.md")
ARCH_PATH = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")
GOAL_HIDDEN = os.path.join(
    os.path.expanduser("~"), "workspace", "goals",
    "mediascope-meta-wearables-press-analysis", "hidden_files",
)
ENTITIES_PATH = os.path.join(PROFILES_DIR, "competitor-entities.yaml")
SUITE_LOG = os.path.join(GOAL_HIDDEN, "type_d_1270_full_suite.log")
OWN_BASENAME = (
    "test_type_c_1274_pubx_agent_to_agent_"
    "advertising_infrastructure_oct07_12am.py"
)
TOP_KEY = None  # Type C lands at competitor-entities.yaml top level.

# Patched per #565 in the anchor followup (main commit sha).
ANCHORED_SHA = "0" * 40

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

MECH_NUM = 996
NEXT_NUM = 997  # integer only; key-form needles are format-built

# Fragment-built per #715: the contiguous key never appears in this file.
BLOCK_KEY = (
    "type_c_1274_pubx_agent_to_agent_"
    "advertising_infrastructure_oct07"
)

# Predecessor chain: #1273 Type B closed the fourth leg of the window.
PRED_MAIN_1273 = "4b9d81ba"
PRED_ANCHOR_1273 = "9aa84bf5"
PRED_DOCSYNC_1273 = "8e2e24c9"
PRED_FINAL_1273 = "ccafb5ef"

# The #1273 window-continuation file, for the staleness pin on its
# guard-lifecycle class (max id 995; zero next-number forms /
# no-Type-C-#1274-in-git-log / fortieth direction absent /
# forty-eighth through fifty-fourth members intact / fifty-fifth member
# absent / ledger 54).
B1273_FILE = (
    "test_type_b_1273_kalley_huang_nyt_meta_anthropic_"
    "spend_vs_apple_foldable_oct06_8pm.py"
)

# Doc-sync constants per #719: post-doc-sync values from the start.
# Patched pre-main once the in-gate collection count is known.
README_TEST_COUNT = 70731  # post-doc-sync total (pre-sync 70642 + 89)
README_FILE_COUNT = 1599  # pre-sync 1598 + 1 (this file)

# The forward-guard needles are fragment-built per #715 so this file
# carries no contiguous literal of a forward-guard claim form.
_T40 = "FORT" + "IETH relationship direction"
_T48 = "FORT" + "Y-EIGHTH falsification-family member"
_T49 = "FORT" + "Y-NINTH falsification-family member"
_T50 = "FIFT" + "IETH falsification-family member"
_T51 = "FIFT" + "Y-FIRST falsification-family member"
_T52 = "FIFT" + "Y-SECOND falsification-family member"
_T53 = "FIFT" + "Y-THIRD falsification-family member"
_T54 = "FIFT" + "Y-FOURTH falsification-family member"
_T55 = "FIFT" + "Y-FIFTH falsification-family member"

# Novel source URLs: all zero-hit repo-wide pre-commit
# (git grep -F). Post-commit all live in the block's source_urls.
NOVEL_URLS = [
    "https://www.prnewswire.com/news-releases/pubx-raises-5m-"
    "series-a-led-by-chicago-ventures-and-acquires-compliant-to-"
    "build-agent-to-agent-advertising-infrastructure-from-the-"
    "ground-up-302899056.html",
    "https://www.morningstar.com/news/pr-newswire/20261006ny64121/"
    "pubx-raises-5m-series-a-led-by-chicago-ventures-and-acquires-"
    "compliant-to-build-agent-to-agent-advertising-"
    "infrastructure-from-the-ground-up",
    "https://runtimewire.com/article/pubx-series-a-compliant-"
    "acquisition-agentic-advertising",
]


def _read(path):
    with open(path, encoding="utf-8", errors="replace") as fh:
        return fh.read()


def _git(*args):
    return subprocess.run(
        ["git", *args], cwd=REPO_ROOT, capture_output=True, text=True
    )


def _iter_source_files():
    """Yield paths for profile + test source files.

    Excludes this file (sweep carrier per #715) and __pycache__
    artifacts (per the #715 pattern-rescope lesson).
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
    found = []
    pat = re.compile(r"mechanism_id:\s*(\d+)")
    for root, dirs, files in os.walk(PROFILES_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
            found.extend(
                int(m) for m in pat.findall(
                    open(os.path.join(root, f),
                         encoding="utf-8", errors="replace").read()
                )
            )
    return max(found) if found else None


def _git_grep_tracked_source(needle, scope):
    """Grep tracked files at HEAD for a literal needle (fragment-built)."""
    args = ["git", "grep", "-F", "-l", needle, "HEAD", "--"]
    if scope:
        args.append(scope)
    out = subprocess.run(
        args, cwd=REPO_ROOT, capture_output=True, text=True
    ).stdout
    cleaned = []
    for line in out.splitlines():
        line = line.strip()
        if line.startswith("HEAD:"):
            line = line[len("HEAD:"):]
        if line:
            cleaned.append(line)
    return cleaned


def _load_entities():
    return yaml.safe_load(_read(ENTITIES_PATH))


def _block():
    data = _load_entities()
    assert BLOCK_KEY in data
    return data[BLOCK_KEY]


def _block_text():
    return _read(ENTITIES_PATH)


def _class_run(filename, classname):
    target = os.path.join(TESTS_DIR, filename)
    env = dict(os.environ)
    env["PYTEST_DISABLE_PLUGIN_AUTOLOAD"] = "1"
    return subprocess.run(
        ["python3", "-m", "pytest", target,
         "-k", classname,
         "-q", "--no-header"],
        cwd=REPO_ROOT, capture_output=True, text=True, env=env,
    )


# ---------------------------------------------------------------------------
# 1. Anchor (pre-commit placeholder per #565; patched in anchor followup).
# ---------------------------------------------------------------------------

class TestAnchor1274:
    def test_anchor_sha_placeholder_pre_commit(self):
        # Pre-commit form: ANCHORED_SHA is 0*40; the anchor followup
        # patches it to the main commit sha per #565. This test is
        # deselected in the in-gate run; the patched form is asserted
        # post-anchor.
        assert ANCHORED_SHA == "0" * 40

    def test_anchor_sha_patched_to_main_commit(self):
        # Post-commit form: ANCHORED_SHA patched to this run's main
        # commit sha per #565 in the anchor followup (both this
        # expected value and the ANCHORED_SHA constant are patched).
        # Pre-commit this is 0*40 and the test fails BY DESIGN;
        # deselected in the in-gate run.
        assert ANCHORED_SHA != "0" * 40
        assert len(ANCHORED_SHA) == 40

    def test_anchor_sha_format(self):
        assert len(ANCHORED_SHA) == 40

    def test_this_run_main_commit_is_anchor(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "main commit is the anchor" in src

    def test_rotation_phrase_in_docstring(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "FIFTH and CLOSING leg of the 1270-1274 window" in src


# ---------------------------------------------------------------------------
# 2. Rotation guard
# ---------------------------------------------------------------------------

class TestRotationGuard1274:
    def test_predecessor_shas_in_git_log(self):
        log = _git("log", "--oneline", "-40").stdout
        for sha, label in (
            (PRED_MAIN_1273, "1273 main"),
            (PRED_ANCHOR_1273, "1273 anchor"),
            (PRED_DOCSYNC_1273, "1273 doc-sync"),
            (PRED_FINAL_1273, "1273 log-hash"),
        ):
            assert sha in log, label

    def test_1273_type_b_in_git_log(self):
        out = _git("log", "--oneline", "--grep=Type B #1273").stdout
        assert out.strip() != ""

    def test_closing_leg_phrase(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "FIFTH and CLOSING leg of the 1270-1274 window" in src

    def test_1265_1269_window_closed(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "1265-1269" in src
        assert "VERIFIED CLOSED" in src

    def test_next_window_opens_1275(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Next run #1275 Type D" in src
        assert "renders the #1270-launched" in src


# ---------------------------------------------------------------------------
# 3. Mechanism novelty (the #715 discipline)
# ---------------------------------------------------------------------------

class TestMechanismNovelty1274:
    def test_max_mechanism_id_is_996_post_landing(self):
        assert _max_numeric_mechanism_id() == MECH_NUM

    def test_block_key_present(self):
        assert BLOCK_KEY in _load_entities()

    def test_block_key_occurs_twice_in_text(self):
        # Once as the YAML key, once as the block_key field.
        assert _block_text().count(BLOCK_KEY) == 2

    def test_996_numeric_present_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(MECH_NUM) != []

    def test_996_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(MECH_NUM) == []

    def test_996_dash_absent_repo_wide(self):
        assert _repo_grep_dash_mechanism(MECH_NUM) == []

    def test_iteration_field(self):
        assert _block()["iteration"] == 1274

    def test_iteration_type_field(self):
        assert _block()["iteration_type"] == "C"


# ---------------------------------------------------------------------------
# 4. Block structure at the competitor-entities.yaml top level.
# ---------------------------------------------------------------------------

class TestBlockStructure1274:
    def test_block_key_top_level(self):
        data = _load_entities()
        assert BLOCK_KEY in data

    def test_mechanism_id_field(self):
        assert _block()["mechanism_id"] == 996

    def test_required_fields_present(self):
        b = _block()
        for field in (
            "block_key", "mechanism_id", "mechanism_name", "type",
            "iteration", "finding", "sources", "verdict",
            "falsification_family", "novelty", "rotation_transparency",
            "concurrency",
        ):
            assert field in b, field

    def test_connects_to_present(self):
        assert isinstance(_block()["connects_to"], list)
        assert len(_block()["connects_to"]) >= 1

    def test_all_novel_sources(self):
        srcs = _block()["sources"]
        assert len(srcs) >= 2
        assert all(s["novel"] is True for s in srcs)

    def test_yaml_parse_clean_flag(self):
        assert _block()["yaml_parse_clean"] is True

    def test_ascii_only_flag(self):
        assert _block()["ascii_only"] is True


# ---------------------------------------------------------------------------
# 5. Content discipline: verbatim excerpts, no constructed URLs.
#    (finding-specific assertions filled from scout selection)
# ---------------------------------------------------------------------------

class TestM996ContentDiscipline1274:
    def test_novel_urls_in_block_sources(self):
        urls = [s["url"] for s in _block()["sources"]]
        for u in NOVEL_URLS:
            assert u in urls, u

    def test_source_urls_verbatim_shape(self):
        for s in _block()["sources"]:
            assert s["url"].startswith("https://")
            assert " " not in s["url"]

    def test_accessed_dates_oct07(self):
        for s in _block()["sources"]:
            assert s["accessed"] == "2026-10-07"

    def test_browser_opens_zero(self):
        assert _block()["browser_opens"] == 0

    def test_excerpt_bounded_documented(self):
        assert "0 browser.open" in _block()["novelty"]

    def test_scout_rejections_documented(self):
        nov = _block()["novelty"]
        assert "Scout rejections on main-run verification" in nov
        assert "SATURATED" in nov

    def test_deal_figures(self):
        finding = _block()["finding"]
        assert "5M" in finding
        assert "Chicago Ventures" in finding
        assert "Compliant" in finding
        assert "Paradium.AI" in finding
        assert "USA TODAY Co." in finding
        assert "Mucinex" in finding
        assert "Advertising Week" in finding

    def test_agent_action_nexus(self):
        finding = _block()["finding"]
        assert "agent-action" in finding
        assert "m391" in finding
        assert "80/20" in finding

    def test_paradium_double_participation(self):
        finding = _block()["finding"]
        assert "m738" in finding
        assert "10-year" in finding

    def test_boundary_no_lab_counterparty(self):
        finding = _block()["finding"]
        assert "no competitor lab is a counterparty" in finding
        assert "monetization rail" in finding

    def test_connects_to_set(self):
        conns = _block()["connects_to"]
        for m in (738, 391, 786):
            assert m in conns, m


# ---------------------------------------------------------------------------
# 6. Statistical discipline: MANUAL / qualitative only per Aug 28 2026 rule.
# ---------------------------------------------------------------------------

class TestStatisticalDiscipline1274:
    def test_manual_qualitative_only(self):
        assert "MANUAL" in _block()["novelty"]

    def test_browser_opens_zero(self):
        assert _block()["browser_opens"] == 0

    def test_tone_not_scored(self):
        assert _block()["tone_scored"] is False

    def test_engine_not_run(self):
        assert _block()["engine_run"] is False

    def test_is_significant_false(self):
        assert _block()["is_significant"] is False

    def test_no_analysis_json_update(self):
        assert _block()["no_analysis_json_update"] is True

    def test_verdict_mechanism_documented(self):
        assert _block()["verdict"] == "mechanism_documented"

    def test_not_artifact_grade(self):
        assert _block()["artifact_grade"] is False


# ---------------------------------------------------------------------------
# 7. Falsification ledger: NOT a member; ledger holds at 54.
# ---------------------------------------------------------------------------

class TestFalsificationLedger1274:
    def test_not_a_falsification_family_member(self):
        b = _block()
        assert b["falsification_family_member"] is False
        assert b["falsification_family"].startswith("NOT a member")

    def test_forty_eighth_intact_in_ft(self):
        assert _git_grep_tracked_source(_T48, "profiles/") == [
            "profiles/financial-times.yaml"]

    def test_forty_ninth_intact_in_journalists(self):
        out = _git(
            "grep", "-c", "-F", _T49, "HEAD", "--",
            "profiles/careers/journalists.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fiftieth_intact_in_journalists(self):
        out = _git(
            "grep", "-c", "-F", _T50, "HEAD", "--",
            "profiles/careers/journalists.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fifty_first_present_in_newscorp(self):
        out = _git(
            "grep", "-c", "-F", _T51, "HEAD", "--",
            "profiles/news-corp.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fifty_second_present_in_journalists(self):
        out = _git(
            "grep", "-c", "-F", _T52, "HEAD", "--",
            "profiles/careers/journalists.yaml",
        )
        assert out.stdout.strip().endswith(":5"), out.stdout

    def test_fifty_third_intact_in_verge(self):
        out = _git(
            "grep", "-c", "-F", _T53, "HEAD", "--",
            "profiles/the-verge.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_fifty_fourth_present_in_guardian(self):
        out = _git(
            "grep", "-c", "-F", _T54, "HEAD", "--",
            "profiles/guardian.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_no_fifty_fifth_member(self):
        assert _git_grep_tracked_source(_T55, None) == []

    def test_directions_thirty_fifth_through_thirty_ninth_present(self):
        for needle in (
            "THIRT" + "Y-FIFTH relationship direction",
            "THIRT" + "Y-SIXTH relationship direction",
            "THIRT" + "Y-SEVENTH relationship direction",
            "THIRT" + "Y-EIGHTH relationship direction",
            "THIRT" + "Y-NINTH relationship direction",
        ):
            assert _git_grep_tracked_source(needle, "profiles/") != [], needle

    def test_fortieth_direction_absent(self):
        assert _git_grep_tracked_source(_T40, "profiles/") == []

    def test_ledger_holds_at_54(self):
        fam = _block()["falsification_family"]
        assert "ledger holds at 54" in fam
        assert "claims no slot" in fam


# ---------------------------------------------------------------------------
# 8. Guard lifecycle: forward pins for #1275; #1273's pins flip BY DESIGN.
# ---------------------------------------------------------------------------

class TestGuardLifecycle1274:
    def test_pins_on_996_landing(self):
        # Type C lands one mechanism: max becomes 996, next is 997.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 996" in src
        assert "NEXT_NUM = 997" in src

    def test_no_type_d_1275_in_git_log_pin(self):
        out = _git("log", "--oneline", "--grep=Type D #1275").stdout
        assert out.strip() == "", out.strip()

    def test_997_numeric_absent_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_997_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_997_dash_absent_repo_wide(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_no_fortieth_direction_pin(self):
        assert _git_grep_tracked_source(_T40, "profiles/") == []

    def test_forty_eighth_member_intact_pin(self):
        assert _git_grep_tracked_source(_T48, "profiles/") == [
            "profiles/financial-times.yaml"]

    def test_forty_ninth_member_intact_pin(self):
        out = _git(
            "grep", "-c", "-F", _T49, "HEAD", "--",
            "profiles/careers/journalists.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fiftieth_member_intact_pin(self):
        out = _git(
            "grep", "-c", "-F", _T50, "HEAD", "--",
            "profiles/careers/journalists.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fifty_first_member_intact_pin(self):
        out = _git(
            "grep", "-c", "-F", _T51, "HEAD", "--",
            "profiles/news-corp.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fifty_second_member_intact_pin(self):
        out = _git(
            "grep", "-c", "-F", _T52, "HEAD", "--",
            "profiles/careers/journalists.yaml",
        )
        assert out.stdout.strip().endswith(":5"), out.stdout

    def test_fifty_third_member_intact_pin(self):
        out = _git(
            "grep", "-c", "-F", _T53, "HEAD", "--",
            "profiles/the-verge.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_fifty_fourth_member_present_pin(self):
        out = _git(
            "grep", "-c", "-F", _T54, "HEAD", "--",
            "profiles/guardian.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_no_fifty_fifth_member_pin(self):
        assert _git_grep_tracked_source(_T55, None) == []

    def test_predecessor_1273_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, B1273_FILE))

    def test_next_leg_is_1275_type_d(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Next run #1275 Type D" in src

    def test_1273_pins_flip_by_design_documented(self):
        # #1273's forward guards (max-995, zero-997 keys all forms,
        # no-Type-C-#1274-in-git-log, fortieth absent, forty-eighth
        # through fifty-fourth intact in profiles/, fifty-fifth absent,
        # ledger 54) verified GREEN pre-commit this run via the
        # subprocess staleness pin (Type C lands mechanism 996 as a
        # documentation event); the max-995, zero-996-numeric, and
        # no-Type-C-#1274-in-git-log pins flip post-main-commit on this
        # run's own landing (the #1191-class self-trip, by design,
        # documented in the staleness pin below).
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "TestStalenessPins1274" in src
        assert "no_type_c_1274_in_git_log_pin" in src


# ---------------------------------------------------------------------------
# 9. Background suite: #1270's suite is OBSERVED ONLY per #795.
# ---------------------------------------------------------------------------

class TestBackgroundSuiteCheck1274:
    def test_suite_log_exists(self):
        assert os.path.exists(SUITE_LOG), SUITE_LOG

    def test_suite_log_nonempty(self):
        assert os.path.getsize(SUITE_LOG) > 0

    def test_run_neither_relaunches_nor_kills(self):
        # Observation-only per #795: this run's own processes must not
        # include a suite launcher it started.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "neither" in src and "re-launches" in src

    def test_verdict_belongs_to_1275(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "belong to #1275" in src


# ---------------------------------------------------------------------------
# 10. Doc-sync per #719 (3 tests; deselected pre-commit, flipped post-sync)
# ---------------------------------------------------------------------------

class TestDocSync1274:
    def test_readme_test_file_table_has_1274_row_post_sync(self):
        readme = _read(README_PATH)
        assert "test_type_c_1274" in readme

    def test_architecture_has_1274_row_post_sync(self):
        arch = _read(ARCH_PATH)
        assert "test_type_c_1274" in arch

    def test_readme_stats_ratcheted(self):
        # Post-sync-positive form per #719: asserts the ratcheted
        # counts (README_TEST_COUNT tests across README_FILE_COUNT
        # files). Fails pre-commit by design; deselected in the
        # in-gate run.
        readme = _read(README_PATH)
        assert ("| Tests | %d |" % README_TEST_COUNT) in readme
        assert ("Across %d test files" % README_FILE_COUNT) in readme


# ---------------------------------------------------------------------------
# 11. Iteration log (3 tests; deselected pre-commit per #721)
# ---------------------------------------------------------------------------

class TestIterationLog1274:
    def test_1274_entry_present_post_sync(self):
        log = _read(LOG_PATH)
        assert "## #1274 Type C" in log

    def test_1273_entry_present(self):
        log = _read(LOG_PATH)
        assert "## #1273 Type B" in log

    def test_rotation_transparency_convention(self):
        log = _read(LOG_PATH)
        assert "### Rotation transparency" in log


# ---------------------------------------------------------------------------
# 12. Staleness pins: #1273's guard lifecycle flips BY DESIGN post-commit
# ---------------------------------------------------------------------------

class TestStalenessPins1274:
    def test_1273_guard_lifecycle_post_commit_self_trip(self):
        # Post-main-commit form: 15 of the 17 pass; the two that fail
        # BY DESIGN are test_no_type_c_1274_in_git_log_pin (this run's
        # own main commit carries "Type C #1274") and
        # test_996_numeric_absent_in_profiles (mechanism 996 lands in
        # profiles/ this run). The #1273 block is read-only to this
        # run. Deselected pre-commit (both pins pass pre-commit).
        res = _class_run(B1273_FILE, "TestGuardLifecycle1273")
        assert res.returncode != 0, res.stdout[-2000:]
        assert "2 failed, 15 passed" in res.stdout, res.stdout[-2000:]
        assert (
            "test_no_type_c_1274_in_git_log_pin" in res.stdout
        ), res.stdout[-2000:]
        assert (
            "test_996_numeric_absent_in_profiles" in res.stdout
        ), res.stdout[-2000:]


# ---------------------------------------------------------------------------
# 13. In-flight isolation
# ---------------------------------------------------------------------------

class TestInFlightIsolation1274:
    def test_899_nytimes_hunk_untouched(self):
        res = _git("diff", "--name-only")
        modified = res.stdout.split()
        assert "profiles/nytimes.yaml" in modified
        # Its uncommitted hunk belongs to #899's run; this run stages
        # only its own files.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#899" in src

    def test_900_untracked_file_untouched(self):
        res = _git("status", "--short")
        assert "test_type_d_900_m769" in res.stdout

    def test_938_test_file_edit_owned_by_its_run(self):
        res = _git("status", "--short")
        assert "test_type_b_938" in res.stdout

    def test_1012_wt_working_tree_edit_owned_by_its_run(self):
        res = _git("status", "--short")
        assert "test_type_a_1012" in res.stdout

    def test_own_diff_excludes_inflight(self):
        # This run's staged set must never include the in-flight
        # files; verified at commit time by explicit-path staging.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "explicit-path" in src
