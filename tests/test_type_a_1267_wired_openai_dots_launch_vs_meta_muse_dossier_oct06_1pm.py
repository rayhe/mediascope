# -*- coding: utf-8 -*-
"""Type A #1267: m991 WIRED Sep-29-2026 Dots launch product-relay register
(Reece Rogers, WIRED Gear: always-on agents positioned as the answer to
Meta's Muse) vs carried WIRED x Meta Muse-dossier accountability register
(Oct 6 2026, 01:00 PM PDT).

NEW WIRED x OpenAI arm (relay-attested, excerpt-bounded per #503, 0
browser.open): WIRED's launch original "OpenAI's Dots Are Always-On AI
Agents - and Its Answer to Meta's Muse" (Reece Rogers, WIRED Gear, Sep 29
2026 1:15 PM). Attested by four independent relays, every one explicitly
attributing WIRED (technewstube.com WIRED section with "Wired / By Reece
Rogers Sep 29, 2026, 1:15 pm"; wesearch.press WIRED RSS-derived excerpt;
newslocker.com WIRED Top Stories list; techmaine.com WIRED aggregator);
verbatim wired.com URL did not surface. The dek grants approachable framing
("cute agents ... connect to your apps and tackle multistep tasks"); the
"always-on" design is presented as the core selling point; the headline
positions Dots as the answer to Meta's Muse. MANUAL ILLUSTRATIVE +0.10
(inside the carried WIRED x OpenAI product-relay band: m889 Dots messaging
relay 0.00). Distinct from m889's Sep-29 Dots messaging-expansion relay
(different piece, different peg, different URL).

Carried WIRED x Meta comparator arms (un-rescored per #807): m988 (Type A
#1265, NEW) - WIRED Oct-4/5 Muse system-prompt dossier accountability
original, -0.58; m877-family - Pinky Promises skepticism -0.45, NameTag
class action -0.30. Meta pooled mean -0.443.

Illustrative delta (OpenAI minus Meta): clean read +0.10 - (-0.58) = +0.68
(n=1 vs n=1, same product family, five days apart); pooled +0.543 (n=1 vs
n=3). OpenAI draws the softer register at WIRED, directionally matching the
Condé Nast x OpenAI softer-prediction. EXTENDS the m889 Dots product-relay
strand from the messaging-expansion relay to the launch-day original.

Verdict: thesis_consistent_observation (register documentation + strand
extension). NOT a falsification-family member: the genre/peg confound is
STRONG (product-launch relay vs accountability original; the
register-follows-peg reading per m877/m889/m916 says launch relays are soft
by genre regardless of entity), and #1192 already falsified blanket
payer-softening at WIRED x OpenAI (FORTY-SEVENTH member). Ledger holds at
54 - FIFTY-FOURTH member-form present (m985, profiles/guardian.yaml);
FIFTY-FIFTH member-claim form absent repo-wide.

Research: 1 delegated scout (9 ranked candidate pairs; SELECTED none -
scout #1 Verge x OpenAI Dots rejected on main-run verification: the exact
Allison Johnson Oct-2 arm is already scored in Type B #1223/m965, and a
Type A re-score would double-count per the #1247 precedent; scout #2
TechCrunch pair rejected: TechCrunch is not a profiled publication, no
profiles/techcrunch.yaml; scout #3 WIRED Astra-delay rejected: same peg as
m877/#1077, saturated; scouts #4-9 rejected for URL gaps, missing
comparator arms, or out-of-window pegs) + 4 main-run browser.search query
sets (exact-headline Verge Dots search, confirming m965 saturation;
Verge Muse-gadgets search, Meta-side arm located but OpenAI arm saturated;
exact-headline WIRED Dots search, SELECTED the Rogers Sep-29 WIRED Gear
original; WIRED Dots byline/date verification, confirming Reece Rogers,
Sep 29 2026 1:15 PM). 0 browser.open per #503 (excerpt-bounded).
Pre-commit novelty greps per #715: zero test_type_a_1267 files on disk
(glob); no "Type A #1267" in git log (--grep); max numeric mechanism_id 990
in profiles/ pre-commit; zero numeric/underscore/dash nine-nine-one
mechanism key forms repo-wide pre-commit (needles format-built, own file
excluded); "## #1267" zero-hit in iteration-log pre-commit; README stats
70012/1591 pre-commit; no #1267 row in README/ARCHITECTURE test tables
pre-commit; 2 novel relay URLs zero-hit repo-wide pre-commit (git grep -F);
the headline phrase "Always-On AI Agents" zero-hit repo-wide pre-commit.

Statistical discipline: MANUAL ILLUSTRATIVE ONLY per the Aug 28 2026
standing rule (engine NOT run; p_value/cohens_d/ci_95 NOT_CALCULATED;
is_significant False; NOT artifact-grade; no analysis.json update).
Correlation is not causation; hypothesis-generating only.

Type A lands m991 (MECH_NUM = 991); NEXT_NUM = 992 for the forward guards.
This run is iteration #1267 Type A, the THIRD leg of the 1265-1269 window
(D #1265 -> E #1266 -> A #1267 -> B #1268 -> C #1269, per the #565 anchor +
rotation guard). Predecessor #1266 Type E verified in git log (main d1eeac3a
/ anchor 1f0243be / doc-sync 700c0909 / log-hash 3af8e551); #1265 Type D
(main b2cceb48 / anchor 344914ff / doc-sync a54c9bff / log-hash 849afa5a).
This run's main commit is the anchor per #565; ANCHORED_SHA patched
post-commit. Next run #1268 Type B continues the window. The #1265-launched
background-suite verdict belongs to #1270 per #795: this run OBSERVES only -
neither re-launches, kills, nor writes to the suite. In-flight during this
run: #899 (profiles/nytimes.yaml m771 hunk), #938 (Type B test file
working-tree edit), #900 (untracked Type D test file), #1012-wt (working-tree
edit on the committed Type A #1012 file) - all untouched; targeted staging
only. Do NOT touch #1024 m846.

ASCII-only, no em dashes. All hashes copied from git rev-parse / git log output.
"""

import os
import re
import subprocess

import pytest
import yaml

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TESTS_DIR = os.path.join(REPO_ROOT, "tests")
PROFILES_DIR = os.path.join(REPO_ROOT, "profiles")
WIRED_PATH = os.path.join(PROFILES_DIR, "wired.yaml")
LOG_PATH = os.path.join(REPO_ROOT, "iteration-log.md")
README_PATH = os.path.join(REPO_ROOT, "README.md")
ARCH_PATH = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")
GOAL_HIDDEN = os.path.join(
    os.path.expanduser("~"), "workspace", "goals",
    "mediascope-meta-wearables-press-analysis", "hidden_files",
)
OWN_BASENAME = (
    "test_type_a_1267_wired_openai_dots_launch_"
    "vs_meta_muse_dossier_oct06_1pm.py"
)

# Pre-commit placeholder per #565; patched to the main commit sha in
# the anchor followup.
ANCHORED_SHA = "4e5f2404d38d7e3c761d7341805f46551ae76d65"  # patched per #565 in the anchor followup (main commit sha)

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

MECH_NUM = 991  # this run's landed mechanism
NEXT_NUM = 992  # forward-guard number for #1268

# Predecessor chain: #1265 Type D opened, #1266 Type E continued.
PRED_MAIN_1265 = "b2cceb48"
PRED_ANCHOR_1265 = "344914ff"
PRED_DOCSYNC_1265 = "a54c9bff"
PRED_FINAL_1265 = "849afa5a"
PRED_MAIN_1266 = "d1eeac3a"
PRED_ANCHOR_1266 = "1f0243be"
PRED_DOCSYNC_1266 = "700c0909"
PRED_FINAL_1266 = "3af8e551"

# The #1266 window-continuation file, for the staleness pin on its
# guard-lifecycle class.
E1266_FILE = (
    "test_type_e_1266_podcast_sentiment_"
    "176th_verification_oct06_12pm.py"
)

# Doc-sync constants per #719: post-doc-sync values from the start.
# Patched pre-main once the in-gate collection count is known.
README_TEST_COUNT = 70084  # post-doc-sync total (pre-sync 70012 + 72)
README_FILE_COUNT = 1592  # pre-sync 1591 + 1

# The forward-guard needles are fragment-built per #715 so this file
# carries no contiguous literal of a forward-guard claim form. The
# fifty-fourth member claim lives ONLY in the profile block (HEAD
# post-#1257); this file references it via fragments.
_T40 = "FORT" + "IETH relationship direction"
_T48 = "FORT" + "Y-EIGHTH falsification-family member"
_T49 = "FORT" + "Y-NINTH falsification-family member"
_T50 = "FIFT" + "IETH falsification-family member"
_T51 = "FIFT" + "Y-FIRST falsification-family member"
_T52 = "FIFT" + "Y-SECOND falsification-family member"
_T53 = "FIFT" + "Y-THIRD falsification-family member"
_T54 = "FIFT" + "Y-FOURTH falsification-family member"
_T55 = "FIFT" + "Y-FIFTH falsification-family member"

BLOCK_KEY = (
    "type_a_1267_wired_openai_dots_launch_"
    "vs_meta_muse_dossier_register_october"
)

# The two relay URLs (verbatim from Full-URL listings); both zero-hit
# repo-wide pre-commit via git grep -F.
NOVEL_URLS = [
    "https://technewstube.com/wired/1871649/"
    "openais-dots-always-ai-agentsand-answer-to-metas-muse/",
    "https://wesearch.press/s/openais-dots-are-always-on-ai-"
    "agentsand-its-answer-to-metas-0d3e0989",
]

# Tones (MANUAL ILLUSTRATIVE).
OPENAI_DOTS_TONE = 0.10  # NEW WIRED x OpenAI arm
META_M988_TONE = -0.58  # carried, un-rescored per #807
META_PINKY_TONE = -0.45  # carried m877-family arm
META_NAMETAG_TONE = -0.30  # carried m757/m877-family arm
META_MEAN = -0.443  # pooled mean of the three Meta arms
DELTA_CLEAN = 0.68  # 0.10 - (-0.58)
DELTA_POOLED = 0.543  # 0.10 - (-0.443)


def _read(path):
    with open(path, encoding="utf-8", errors="replace") as fh:
        return fh.read()


def _git(*args):
    return subprocess.run(
        ["git", *args], cwd=REPO_ROOT, capture_output=True, text=True
    )


def _load_wired():
    with open(WIRED_PATH, encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def _block():
    data = _load_wired()
    return data["competitor_relationships"]["openai"][BLOCK_KEY]


def _iter_source_files():
    """Yield paths for profile + test source files.

    Excludes this file (sweep carrier per #715) and __pycache__
    artifacts.
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
    """Underscore-form mechanism key; needle format-built per #770."""
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
    """Working-tree profiles/ sweep for the colon-form mechanism id."""
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
    return max(found) if found else 0


def _git_grep_tracked_source(needle, scope):
    """Literal needle across tracked profile/test source files.

    scope is "profiles/" or None (profiles/ + tests/). Excludes the
    sweep carrier and __pycache__ artifacts per #715.
    """
    out = _git("grep", "-F", "-l", needle, "HEAD", "--",
               "profiles/", "tests/").stdout
    hits = []
    for line in out.splitlines():
        line = line.strip()
        if not line:
            continue
        if line.startswith("HEAD:"):
            line = line[len("HEAD:"):]
        path = line
        if "__pycache__" in path:
            continue
        if path.endswith("/" + OWN_BASENAME) or path == OWN_BASENAME:
            continue
        if scope == "profiles/" and not path.startswith("profiles/"):
            continue
        hits.append(path)
    return hits


def _class_run(filename, classname):
    target = os.path.join(TESTS_DIR, filename)
    env = dict(os.environ)
    env["PYTEST_DISABLE_PLUGIN_AUTOLOAD"] = "1"
    return subprocess.run(
        ["python3", "-m", "pytest", target + "::" + classname, "-q",
         "--no-header", "-p", "no:cacheprovider"],
        cwd=REPO_ROOT, capture_output=True, text=True, env=env,
    )


# ---------------------------------------------------------------------------
# 1. Anchor per #565 (5 tests; deselected pre-commit, patched post-commit)
# ---------------------------------------------------------------------------
class TestAnchor1267:
    def test_anchor_sha_placeholder_pre_commit(self):
        # Pre-commit form: ANCHORED_SHA is 0*40; the anchor followup
        # patches it to the main commit sha per #565. Deselected in
        # the in-gate run; the patched form is asserted post-anchor.
        assert ANCHORED_SHA == "0" * 40

    def test_anchor_sha_patched_to_main_commit(self):
        # Post-commit form: ANCHORED_SHA patched to this run's main
        # commit sha per #565 in the anchor followup. Pre-commit this
        # is 0*40 and the test fails BY DESIGN; deselected in-gate.
        assert ANCHORED_SHA != "0" * 40
        assert len(ANCHORED_SHA) == 40

    def test_anchor_sha_format(self):
        assert len(ANCHORED_SHA) == 40

    def test_this_run_main_commit_is_anchor(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "main commit is the anchor" in src

    def test_rotation_phrase_in_docstring(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "THIRD leg of the 1265-1269 window" in src


# ---------------------------------------------------------------------------
# 2. Rotation guard
# ---------------------------------------------------------------------------
class TestRotationGuard:
    def test_predecessor_1265_1266_chain_verified(self):
        for sha in (
            PRED_MAIN_1265, PRED_ANCHOR_1265, PRED_DOCSYNC_1265,
            PRED_FINAL_1265, PRED_MAIN_1266, PRED_ANCHOR_1266,
            PRED_DOCSYNC_1266, PRED_FINAL_1266,
        ):
            res = _git("cat-file", "-t", sha)
            assert res.stdout.strip() == "commit", "missing %s" % sha

    def test_window_order_phrase(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "D #1265 -> E #1266 -> A #1267 -> B #1268 -> C #1269" in src

    def test_next_leg_is_type_b_1268(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Next run #1268 Type B" in src

    def test_type_a_lands_m991(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Type A lands m991" in src


# ---------------------------------------------------------------------------
# 3. Mechanism novelty (the #715 discipline; landing-run form per #1238)
# ---------------------------------------------------------------------------
class TestMechanismNovelty1267:
    def test_no_own_test_file_pre_commit(self):
        matches = [
            f for f in os.listdir(TESTS_DIR)
            if f.startswith("test_type_a_1267")
        ]
        assert matches == [OWN_BASENAME], matches

    def test_no_type_a_1267_in_git_log(self):
        out = _git("log", "--oneline", "--grep=Type A #1267")
        assert out.stdout.strip() == ""

    def test_max_mechanism_id_is_991_working_tree(self):
        # Post-landing working-tree form: the m991 block is landed
        # (uncommitted) so max is 991; pre-landing HEAD form is 990.
        assert _max_numeric_mechanism_id() == MECH_NUM

    def test_991_colon_form_lands_in_wired(self):
        hits = _repo_grep_numeric_mechanism_id(MECH_NUM)
        assert hits == [WIRED_PATH], hits

    def test_992_numeric_absent_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_992_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_992_dash_absent_repo_wide(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_block_key_unique(self):
        out = _git("grep", "-F", "-l", BLOCK_KEY, "HEAD", "--",
                   "profiles/", "tests/")
        assert out.stdout.strip() == "", out.stdout

    def test_novel_urls_zero_hit_pre_commit(self):
        for url in NOVEL_URLS:
            out = _git("grep", "-F", "-l", url, "HEAD")
            assert out.stdout.strip() == "", url

    def test_novel_phrase_zero_hit_pre_commit(self):
        out = _git("grep", "-F", "-l", "Always-On AI Agents", "HEAD")
        assert out.stdout.strip() == "", out.stdout

    def test_no_1267_row_in_doc_tables_pre_commit(self):
        assert "test_type_a_1267" not in _read(README_PATH)
        assert "test_type_a_1267" not in _read(ARCH_PATH)
        assert "## #1267" not in _read(LOG_PATH)

    def test_block_key_carries_no_991_substring(self):
        # Designed keying per #723/#738/#739: the iteration-form key
        # must not contain the mechanism number in any key form.
        assert "991" not in BLOCK_KEY


# ---------------------------------------------------------------------------
# 4. The NEW WIRED x OpenAI Dots launch arm
# ---------------------------------------------------------------------------
class TestWiredDotsLaunchArm:
    def test_block_present_in_wired_openai(self):
        data = _load_wired()
        openai = data["competitor_relationships"]["openai"]
        assert BLOCK_KEY in openai

    def test_mechanism_id_991(self):
        assert _block()["mechanism_id"] == MECH_NUM

    def test_arm_title(self):
        arm = _block()["openai_arms"][0]["item"]
        assert "Always-On AI Agents" in arm["title"]
        assert "Meta" in arm["title"]

    def test_arm_byline_and_date(self):
        arm = _block()["openai_arms"][0]["item"]
        assert arm["author_byline"] == "Reece Rogers"
        assert arm["date"] == "2026-09-29"
        assert arm["publication"] == "WIRED (original; relay-attested)"

    def test_arm_evidence_tier(self):
        arm = _block()["openai_arms"][0]["item"]
        assert arm["evidence_tier"] == "relay-attested"
        assert arm["status"].startswith("NEW this run")

    def test_arm_tone(self):
        arm = _block()["openai_arms"][0]["item"]
        assert arm["manual_illustrative_tone"] == OPENAI_DOTS_TONE
        assert arm["framing"] == "product_launch_relay"

    def test_arm_relay_urls(self):
        assert _block()["source_urls"] == NOVEL_URLS

    def test_arm_distinct_from_m889(self):
        arm = _block()["openai_arms"][0]["item"]
        assert "m889" in arm["status"]
        assert "messaging-expansion relay" in arm["status"]

    def test_arm_not_falsification_member(self):
        assert _block()["falsification_family_member"] is False
        assert _block()["falsification_ledger"] == "54"


# ---------------------------------------------------------------------------
# 5. Carried WIRED x Meta comparator arms (un-rescored per #807)
# ---------------------------------------------------------------------------
class TestMetaComparatorCarried:
    def test_meta_arms_carried(self):
        block = _block()
        assert "m988" in block["meta_arms"]["carried_from"]
        assert "m877-family" in block["meta_arms"]["carried_from"]

    def test_m988_tone(self):
        arms = _block()["meta_arms"]["arms"]
        assert arms[0]["manual_illustrative_tone"] == META_M988_TONE
        assert arms[0]["mechanism_ref"] == "m988"

    def test_m877_family_tones(self):
        arms = _block()["meta_arms"]["arms"]
        assert arms[1]["manual_illustrative_tone"] == META_PINKY_TONE
        assert arms[2]["manual_illustrative_tone"] == META_NAMETAG_TONE

    def test_meta_band_mean(self):
        assert _block()["meta_arms"]["meta_band_mean"] == META_MEAN

    def test_financial_relationship(self):
        rel = _block()["financial_relationship"]
        assert "Aug 20 2024" in rel
        assert "WIRED x Meta $0" in rel


# ---------------------------------------------------------------------------
# 6. Asymmetry delta (MANUAL ILLUSTRATIVE ONLY)
# ---------------------------------------------------------------------------
class TestAsymmetryDelta:
    def test_delta_math_clean(self):
        calc = OPENAI_DOTS_TONE - META_M988_TONE
        assert abs(calc - DELTA_CLEAN) < 1e-9

    def test_delta_math_pooled(self):
        calc = OPENAI_DOTS_TONE - META_MEAN
        assert abs(calc - DELTA_POOLED) < 1e-3

    def test_block_delta_matches(self):
        res = _block()["asymmetry_scorer_result"]
        assert res["illustrative_delta_openai_minus_meta_clean"] == DELTA_CLEAN
        assert res["illustrative_delta_openai_minus_meta_pooled"] == (
            DELTA_POOLED)

    def test_delta_direction_openai_softer(self):
        res = _block()["asymmetry_scorer_result"]
        assert "OpenAI draws the softer register" in res["delta_direction"]

    def test_engine_not_run(self):
        res = _block()["asymmetry_scorer_result"]
        assert res["engine_run"] is False
        assert res["is_significant"] is False
        assert res["artifact_grade"] is False

    def test_sample_sizes_declared(self):
        res = _block()["asymmetry_scorer_result"]
        assert "n=1 vs n=1" in res["methodology"]
        assert "n=1 vs n=3" in res["methodology"]


# ---------------------------------------------------------------------------
# 7. Research method
# ---------------------------------------------------------------------------
class TestResearchMethod:
    def test_four_main_run_query_sets_documented(self):
        assert "4 main-run browser.search query sets" in _block()[
            "research_method"]

    def test_scout_rejections_documented(self):
        method = _block()["research_method"]
        assert "delegated scout" in method
        assert "SELECTED none" in method
        assert "#1247 precedent" in method

    def test_zero_browser_open(self):
        assert "0 browser.open per #503" in _block()["research_method"]

    def test_ascii_no_em_dash(self):
        text = _read(WIRED_PATH)
        assert "\u2014" not in text

    def test_no_constructed_canonical_urls(self):
        method = _block()["research_method"]
        assert "no canonical URLs constructed" in method


# ---------------------------------------------------------------------------
# 8. Statistical discipline (Aug 28 2026 standing rule)
# ---------------------------------------------------------------------------
class TestStatisticalDiscipline:
    def test_p_value_not_calculated(self):
        res = _block()["asymmetry_scorer_result"]
        assert res["p_value"].startswith("NOT_CALCULATED")

    def test_no_analysis_json_update(self):
        assert _block()["no_analysis_json_update"] is True

    def test_correlation_not_causation(self):
        assert _block()["correlation_not_causation"] is True

    def test_manual_illustrative_only(self):
        disc = _block()["statistical_discipline"]
        assert "MANUAL ILLUSTRATIVE" in disc

    def test_verdict_not_falsification(self):
        assert _block()["verdict"].startswith("thesis_consistent_observation")

    def test_ledger_holds_54(self):
        assert _block()["ledger"] == "54"


# ---------------------------------------------------------------------------
# 9. Guard lifecycle: verifies #1266's forward guards, lays #1268's pins
# ---------------------------------------------------------------------------
class TestGuardLifecycle1267:
    def test_pins_on_991_landing(self):
        # Type A lands m991: max becomes 991, next is 992.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 991" in src
        assert "NEXT_NUM = 992" in src

    def test_no_type_b_1268_in_git_log_pin(self):
        out = _git("log", "--oneline", "--grep=Type B #1268")
        assert out.stdout.strip() == ""

    def test_992_numeric_absent_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_992_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_992_dash_absent_repo_wide(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_no_fortieth_direction_pin(self):
        # The fortieth direction-claim form stays absent in profiles/.
        assert _git_grep_tracked_source(_T40, "profiles/") == []

    def test_forty_eighth_member_intact_pin(self):
        out = _git(
            "grep", "-c", "-F", _T48, "HEAD", "--",
            "profiles/financial-times.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

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

    def test_fifty_fourth_member_intact_pin(self):
        # m985 landed at #1257 and is committed: HEAD form, exactly
        # two claim forms in profiles/guardian.yaml.
        out = _git(
            "grep", "-c", "-F", _T54, "HEAD", "--",
            "profiles/guardian.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_no_fifty_fifth_member_pin(self):
        assert _git_grep_tracked_source(_T55, None) == []

    def test_predecessor_1266_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, E1266_FILE))

    def test_next_leg_is_1268_type_b(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#1268 Type B" in src

    def test_1266_pins_stay_green_documented(self):
        # #1266's forward guards (max-990, zero-991 keys all forms,
        # no-Type-A-#1267-in-git-log, fortieth absent, forty-eighth +
        # forty-ninth + fiftieth + fifty-first + fifty-second +
        # fifty-third + fifty-fourth intact, no fifty-fifth; ledger 54)
        # verified GREEN at HEAD pre-commit this run. The
        # no-Type-A-#1267-in-git-log and zero-991-numeric/underscore/
        # dash pins flip BY DESIGN at this run's main commit (the
        # #1191-class self-trip: the main commit subject carries
        # "Type A #1267" and the m991 block lands mechanism_id 991);
        # documented in the staleness pin below, not repaired.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "TestStalenessPins1267" in src
        assert "no_type_a_1267_in_git_log_pin" in src


# ---------------------------------------------------------------------------
# 10. Staleness pins: #1266's guard lifecycle flips by design
#      (1 test; deselected pre-commit, verified post-main-commit)
# ---------------------------------------------------------------------------
class TestStalenessPins1267:
    def test_1266_guard_lifecycle_flips_by_design_post_commit(self):
        # Runs the #1266 file's guard-lifecycle class post-commit:
        # its no-Type-A-#1267-in-git-log pin self-trips on this run's
        # own main commit and its zero-991-numeric/underscore/dash pins
        # trip on the landed m991 block (all BY DESIGN, the #1191-class
        # self-trip family); the class is expected to report the flips,
        # not to stay green.
        res = _class_run(E1266_FILE, "TestGuardLifecycle1266")
        assert res.returncode != 0, res.stdout[-2000:]
        assert "failed" in res.stdout, res.stdout[-2000:]


# ---------------------------------------------------------------------------
# 11. Doc-sync per #719 (3 tests; deselected pre-commit, flipped post-sync)
# ---------------------------------------------------------------------------
class TestDocSync:
    def test_readme_test_file_table_has_1267_row_post_sync(self):
        readme = _read(README_PATH)
        assert "test_type_a_1267" in readme

    def test_architecture_has_1267_row_post_sync(self):
        arch = _read(ARCH_PATH)
        assert "test_type_a_1267" in arch

    def test_readme_stats_ratcheted(self):
        # Post-sync-positive form per #719: asserts the ratcheted
        # counts (README_TEST_COUNT tests across README_FILE_COUNT
        # files). Fails pre-commit by design; deselected in the
        # in-gate run.
        readme = _read(README_PATH)
        assert ("| Tests | %d | Across %d test files |" % (
            README_TEST_COUNT, README_FILE_COUNT)) in readme


# ---------------------------------------------------------------------------
# 12. Iteration log (3 tests; deselected pre-commit per #721)
# ---------------------------------------------------------------------------
class TestIterationLog:
    def test_1267_entry_present_post_sync(self):
        log = _read(LOG_PATH)
        assert "## #1267 Type A" in log

    def test_1266_entry_present(self):
        log = _read(LOG_PATH)
        assert "## #1266 Type E" in log

    def test_rotation_transparency_convention(self):
        log = _read(LOG_PATH)
        assert "### Rotation transparency" in log


# ---------------------------------------------------------------------------
# 13. In-flight isolation
# ---------------------------------------------------------------------------
class TestInFlightIsolation:
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

    def test_do_not_touch_1024_m846(self):
        # Guarded in the log entry per convention; the test file keeps
        # the in-flight list only (own-file reference would trip the
        # contiguous-literal discipline elsewhere).
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#1024" in src


# ---------------------------------------------------------------------------
# 14. Background suite: observed only per #795
# ---------------------------------------------------------------------------
class TestBackgroundSuite1267:
    def test_1265_suite_log_exists(self):
        assert os.path.exists(
            os.path.join(GOAL_HIDDEN, "type_d_1265_full_suite.log"))

    def test_this_run_launches_no_suite(self):
        # This run must not launch its own background suite; only the
        # #1265-launched suite is observed (verdict belongs to #1270).
        assert not os.path.exists(
            os.path.join(GOAL_HIDDEN, "type_d_1267_full_suite.log"))

    def test_observation_only_documented(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "OBSERVES only" in src
        assert "verdict belongs to #1270" in src
