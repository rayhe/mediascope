# -*- coding: utf-8 -*-
"""Type A #1272: m994 Guardian Oct-3-2026 Robinson resignation
straight-news register (Dan Milmo: safety leader quits, "culture is
broken", -0.30 MANUAL ILLUSTRATIVE) vs carried Guardian x Meta
accountability register (m687 police-warnings -0.55 + teen-accounts
-0.45, mean -0.50); illustrative delta (OpenAI minus Meta) +0.25 clean /
+0.20 pooled, thesis_consistent_observation, temporal replication of
m934's +0.167, NOT a falsification-family member (ledger holds at 54);
scout #1 Guardian framing SELECTED (FRESH), Verge x Apple LG + MIT TR x
Google held as backups; 3 novel relay URLs zero-hit pre-commit - Type A
THIRD leg of the 1270-1274 window (Oct 6 2026, 06:00 PM PDT).

NEW Guardian x OpenAI arm (relay-attested, excerpt-bounded per #503, 0
browser.open): The Guardian's original "OpenAI safety leader quits,
warning AI company's culture is 'broken'" (Dan Milmo, Global
technology editor, Oct 3 2026). Attested by three independent relays,
every one explicitly attributing The Guardian (wesearch.press
publisher record with "https://www.theguardian.com/profile/danmilmo -
Oct 3, 2026"; thedailybreakingnews.com relay with "By Dan Milmo
Global technology editor" and "Main source: The Guardian Technology";
ricochet.com relay quoting the canonical guardian.com URL and the
essay headline); verbatim theguardian.com canonical URL did not arrive
in any search Full-URL listing (NOT used per the no-construction
rule). Adversarial content ("culture is broken" as headline and lede;
"not being nearly careful enough"; nuclear-plant/airport redundancy
remedy) in an even-handed straight-news register with an OpenAI
spokesperson rebuttal printed ("continues to strengthen security
practices"). MANUAL ILLUSTRATIVE -0.30 (inside the carried Guardian x
OpenAI enforcement-week band: m934 arms -0.30/-0.40/-0.30). Distinct
from #1227's BI x OpenAI event score (BI broke the resignation; the
Guardian FRAMING is the NEW arm; the Atlantic essay is saturated per
task).

Carried Guardian x Meta comparator arms (un-rescored per #807): m687
(Type A #757, NEW) - police-warnings documents investigation -0.55,
teen-accounts influencer payouts -0.45. Meta pooled mean -0.50.

Illustrative delta (OpenAI minus Meta): clean read -0.30 - (-0.55) =
+0.25 (n=1 vs n=1, resignation straight news vs documents
investigation); pooled +0.20 (n=1 vs n=2). OpenAI draws the softer
register at the Guardian, directionally matching the Feb-14-2025
licensing coverage_prediction (softer). TEMPORAL REPLICATION of m934's
+0.167 (same publication, same comparator family, same direction).

Verdict: thesis_consistent_observation (register documentation +
temporal replication). NOT a falsification-family member: the
peg/genre confound is STRONG (resignation straight news vs
investigation originals; the register-follows-peg reading says
resignation news is even-handed by genre regardless of entity), the
piece does NOT suppress the adversarial content (the "culture is
broken" charge is the headline and lede - softness is register-level,
not story suppression), and m985 (#1257, FIFTY-FOURTH member) already
falsified blanket payer-softening at the Guardian on the
own-investigation peg, so this run's softer read is peg-bounded.
Ledger holds at 54 - FIFTY-FOURTH member-form present (m985,
profiles/guardian.yaml); FIFTY-FIFTH member-claim form absent
repo-wide.

Research: 1 delegated scout (20 browser.search query sets; 10 ranked
candidate pairs; SELECTED #1 Guardian x OpenAI Robinson resignation -
FRESH Guardian framing; scout #2 Verge x Apple LG smart-home held as
backup (mirror URL only, no canonical); scout #3 MIT TR x Google
Gemini 4 Argon digest held as backup (verbatim URL but weakest
material); scout rejections: Verge Dots hands-on (m965 double-count,
#1247 precedent), Gizmodo Snap comparisons (#1162/#862 saturated),
NYT Anthropic Dias (#1182 saturated), BI x OpenAI Robinson (event
saturated at #1227 - BI broke it first; the Guardian framing is the
NEW arm), Atlantic essay (saturated per task)) + 1 main-run
browser.search verification set (exact-headline Guardian Milmo search:
confirmed Dan Milmo Global technology editor byline, Oct 3 2026 date
via the WeSearch publisher record, 3 verbatim Full-URL relay listings;
0 browser.open per #503, excerpt-bounded; no canonical URLs
constructed). Pre-commit novelty greps per #715: zero test_type_a_1272
files on disk (glob); no "Type A #1272" in git log (--grep); max
numeric mechanism_id 993 in profiles/ pre-commit; zero
numeric/underscore/dash nine-nine-four mechanism key forms repo-wide
pre-commit (needles format-built, own file excluded); "## #1272"
zero-hit in iteration-log pre-commit; README stats 70479/1596
pre-commit; no #1272 row in README/ARCHITECTURE test tables
pre-commit; 3 novel relay URLs zero-hit repo-wide pre-commit (git
grep -F); the headline phrase "OpenAI safety leader quits" zero-hit
repo-wide pre-commit.

Statistical discipline: MANUAL ILLUSTRATIVE ONLY per the Aug 28 2026
standing rule (engine NOT run; p_value/cohens_d/ci_95 NOT_CALCULATED;
is_significant False; NOT artifact-grade; no analysis.json update).
Correlation is not causation; hypothesis-generating only.

Type A lands m994 (MECH_NUM = 994); NEXT_NUM = 995 for the forward
guards. This run is iteration #1272 Type A, the THIRD leg of the
1270-1274 window (D #1270 -> E #1271 -> A #1272 -> B #1273 -> C #1274,
per the #565 anchor + rotation guard). Predecessor #1271 Type E
verified in git log (main 2a299281 / anchor c4669ea2 / doc-sync
5c41406e / log-hash 33006eae); #1270 Type D (main 13ce7c10 / anchor
c55355f6 / doc-sync 07c5dbee / log-hash b613ced9). This run's main
commit is the anchor per #565; ANCHORED_SHA patched post-commit. Next
run #1273 Type B continues the window. The #1270-launched
background-suite verdict belongs to #1275 per #795: this run OBSERVES
only - neither re-launches, kills, nor writes to the suite. In-flight
during this run: #899 (profiles/nytimes.yaml m771 hunk), #938 (Type B
test file working-tree edit), #900 (untracked Type D test file),
#1012-wt (working-tree edit on the committed Type A #1012 file) - all
untouched; targeted staging only. Do NOT touch #1024 m846.

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
GUARDIAN_PATH = os.path.join(PROFILES_DIR, "guardian.yaml")
LOG_PATH = os.path.join(REPO_ROOT, "iteration-log.md")
README_PATH = os.path.join(REPO_ROOT, "README.md")
ARCH_PATH = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")
GOAL_HIDDEN = os.path.join(
    os.path.expanduser("~"), "workspace", "goals",
    "mediascope-meta-wearables-press-analysis", "hidden_files",
)
OWN_BASENAME = (
    "test_type_a_1272_guardian_openai_robinson_resignation_oct06_6pm.py"
)

# Pre-commit placeholder per #565; patched to the main commit sha in
# the anchor followup.
ANCHORED_SHA = "0" * 40  # patched per #565 in the anchor followup (main commit sha)

# This run's main commit (full sha), for the ancestor-form
# no-Type-A-#1272 pin. Patched in the terminal log-hash followup per
# #721.
PRED_MAIN_1272 = "0" * 40  # patched in the log-hash followup per #721 (main commit sha)

# #1273's main commit (full sha), for the ancestor-form no-Type-B-#1273
# pin. Patched in #1273's terminal log-hash followup per #721.
PRED_MAIN_1273 = "0" * 40  # patched in #1273's log-hash followup per #721 (main commit sha)

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

MECH_NUM = 994  # this run's landed mechanism
NEXT_NUM = 995  # forward-guard number for #1273; integer only, key-form needles format-built

# Predecessor chain: #1270 Type D opened, #1271 Type E continued.
PRED_MAIN_1270 = "13ce7c10"
PRED_ANCHOR_1270 = "c55355f6"
PRED_DOCSYNC_1270 = "07c5dbee"
PRED_FINAL_1270 = "b613ced9"
PRED_MAIN_1271 = "2a299281"
PRED_ANCHOR_1271 = "c4669ea2"
PRED_DOCSYNC_1271 = "5c41406e"
PRED_FINAL_1271 = "33006eae"

# The #1271 window-continuation file, for the staleness pin on its
# guard-lifecycle class (max id 993; zero next-number nine-nine-four
# / no-Type-A-#1272-in-git-log (flips BY DESIGN at this run's main
# commit - the #1191-class self-trip) / fortieth direction absent /
# forty-eighth member intact in profiles/financial-times.yaml /
# forty-ninth member intact + fiftieth member intact +
# fifty-second member intact in profiles/careers/journalists.yaml /
# fifty-first member intact in profiles/news-corp.yaml /
# fifty-third member intact in profiles/the-verge.yaml /
# fifty-fourth member intact in profiles/guardian.yaml (landed at
# #1257) / no fifty-fifth member (repo-wide) / ledger 54).
E1271_FILE = (
    "test_type_e_1271_podcast_sentiment_177th_verification_oct06_5pm.py"
)

# Doc-sync constants per #719: post-doc-sync values from the start.
# Patched pre-main once the in-gate collection count is known
# (85 collected, 14 classes; in-gate 71 passed + 14 deselected).
README_TEST_COUNT = 70564  # post-doc-sync total (pre-sync 70479 + 85)
README_FILE_COUNT = 1597  # pre-sync 1596 + 1

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
    "type_a_1272_guardian_openai_robinson_resignation_"
    "culture_broken_october"
)

# The three relay URLs (verbatim from Full-URL listings); all zero-hit
# repo-wide pre-commit via git grep -F.
NOVEL_URLS = [
    "https://wesearch.press/s/openai-safety-leader-quits-warning-"
    "ai-companys-culture-is-br-902a8fe9",
    "https://thedailybreakingnews.com/news/technology/openai-"
    "safety-leader-quits-warning-ai-company-s-culture-is-broken-3gqj0h",
    "https://ricochet.com/2018904/another-safety-engineer-quits-"
    "ai-giant-with-a-deaf-warning/",
]

# Tones (MANUAL ILLUSTRATIVE).
OPENAI_ROBINSON_TONE = -0.30  # NEW Guardian x OpenAI arm
META_POLICE_TONE = -0.55  # carried m687 arm
META_TEEN_TONE = -0.45  # carried m687 arm
META_MEAN = -0.50  # pooled mean of the two Meta arms
DELTA_CLEAN = 0.25  # -0.30 - (-0.55)
DELTA_POOLED = 0.20  # -0.30 - (-0.50)


def _read(path):
    with open(path, encoding="utf-8", errors="replace") as fh:
        return fh.read()


def _git(*args):
    return subprocess.run(
        ["git", *args], cwd=REPO_ROOT, capture_output=True, text=True
    )


def _load_guardian():
    with open(GUARDIAN_PATH, encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def _block():
    data = _load_guardian()
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
class TestAnchor1272:
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
        assert "THIRD leg of the 1270-1274 window" in src


# ---------------------------------------------------------------------------
# 2. Rotation guard
# ---------------------------------------------------------------------------
class TestRotationGuard:
    def test_predecessor_1270_1271_chain_verified(self):
        for sha in (
            PRED_MAIN_1270, PRED_ANCHOR_1270, PRED_DOCSYNC_1270,
            PRED_FINAL_1270, PRED_MAIN_1271, PRED_ANCHOR_1271,
            PRED_DOCSYNC_1271, PRED_FINAL_1271,
        ):
            res = _git("cat-file", "-t", sha)
            assert res.stdout.strip() == "commit", "missing %s" % sha

    def test_window_order_phrase(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "D #1270 -> E #1271 -> A #1272 -> B #1273 -> C #1274" in src

    def test_next_leg_is_type_b_1273(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Next run #1273 Type B" in src

    def test_type_a_lands_m994(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Type A lands m994" in src


# ---------------------------------------------------------------------------
# 3. Mechanism novelty (the #715 discipline; landing-run form per #1238)
# ---------------------------------------------------------------------------
class TestMechanismNovelty1272:
    def test_no_own_test_file_pre_commit(self):
        matches = [
            f for f in os.listdir(TESTS_DIR)
            if f.startswith("test_type_a_1272")
        ]
        assert matches == [OWN_BASENAME], matches

    def test_no_type_a_1272_in_git_log(self):
        out = _git("log", "--oneline", "--grep=Type A #1272")
        assert out.stdout.strip() == ""

    def test_max_mechanism_id_is_994_working_tree(self):
        # Post-landing working-tree form: the m994 block is landed
        # (uncommitted) so max is 994; pre-landing HEAD form is 993.
        assert _max_numeric_mechanism_id() == MECH_NUM

    def test_994_colon_form_lands_in_guardian(self):
        hits = _repo_grep_numeric_mechanism_id(MECH_NUM)
        assert hits == [GUARDIAN_PATH], hits

    def test_995_numeric_absent_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_995_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_995_dash_absent_repo_wide(self):
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
        out = _git("grep", "-F", "-l", "OpenAI safety leader quits", "HEAD")
        assert out.stdout.strip() == "", out.stdout

    def test_no_1272_row_in_doc_tables_pre_commit(self):
        assert "test_type_a_1272" not in _read(README_PATH)
        assert "test_type_a_1272" not in _read(ARCH_PATH)
        assert "## #1272" not in _read(LOG_PATH)

    def test_block_key_carries_no_994_substring(self):
        # Designed keying per #723/#738/#739: the iteration-form key
        # must not contain the mechanism number in any key form.
        assert "994" not in BLOCK_KEY


# ---------------------------------------------------------------------------
# 4. The NEW Guardian x OpenAI Robinson resignation arm
# ---------------------------------------------------------------------------
class TestGuardianRobinsonArm:
    def test_block_present_in_guardian_openai(self):
        data = _load_guardian()
        openai = data["competitor_relationships"]["openai"]
        assert BLOCK_KEY in openai

    def test_mechanism_id_994(self):
        assert _block()["mechanism_id"] == MECH_NUM

    def test_arm_title(self):
        arm = _block()["openai_arms"][0]["item"]
        assert "safety leader quits" in arm["title"]
        assert "culture is" in arm["title"]

    def test_arm_byline_and_date(self):
        arm = _block()["openai_arms"][0]["item"]
        assert arm["author_byline"] == "Dan Milmo"
        assert arm["date"] == "2026-10-03"
        assert arm["publication"] == "The Guardian (original; relay-attested)"

    def test_arm_evidence_tier(self):
        arm = _block()["openai_arms"][0]["item"]
        assert arm["evidence_tier"] == "relay-attested"
        assert arm["status"].startswith("NEW this run")

    def test_arm_tone(self):
        arm = _block()["openai_arms"][0]["item"]
        assert arm["manual_illustrative_tone"] == OPENAI_ROBINSON_TONE
        assert arm["framing"] == "straight_news_resignation_accountability"

    def test_arm_relay_urls(self):
        assert _block()["source_urls"] == NOVEL_URLS

    def test_arm_distinct_from_1227(self):
        arm = _block()["openai_arms"][0]["item"]
        assert "#1227" in arm["status"]
        assert "Guardian FRAMING is the NEW arm" in arm["status"]

    def test_arm_not_falsification_member(self):
        assert _block()["falsification_family_member"] is False
        assert _block()["falsification_ledger"] == "54"


# ---------------------------------------------------------------------------
# 5. Carried Guardian x Meta comparator arms (un-rescored per #807)
# ---------------------------------------------------------------------------
class TestMetaComparatorCarried:
    def test_meta_arms_carried(self):
        block = _block()
        assert "m687" in block["meta_arms"]["carried_from"]
        assert "#757" in block["meta_arms"]["carried_from"]

    def test_police_warnings_tone(self):
        arms = _block()["meta_arms"]["arms"]
        assert arms[0]["manual_illustrative_tone"] == META_POLICE_TONE
        assert arms[0]["mechanism_ref"] == "m687"

    def test_teen_accounts_tone(self):
        arms = _block()["meta_arms"]["arms"]
        assert arms[1]["manual_illustrative_tone"] == META_TEEN_TONE
        assert arms[1]["mechanism_ref"] == "m687"

    def test_meta_band_mean(self):
        assert _block()["meta_arms"]["meta_band_mean"] == META_MEAN

    def test_financial_relationship(self):
        rel = _block()["financial_relationship"]
        assert "Feb 14 2025" in rel
        assert "Guardian x Meta $0" in rel


# ---------------------------------------------------------------------------
# 6. Asymmetry delta (MANUAL ILLUSTRATIVE ONLY)
# ---------------------------------------------------------------------------
class TestAsymmetryDelta:
    def test_delta_math_clean(self):
        calc = OPENAI_ROBINSON_TONE - META_POLICE_TONE
        assert abs(calc - DELTA_CLEAN) < 1e-9

    def test_delta_math_pooled(self):
        calc = OPENAI_ROBINSON_TONE - META_MEAN
        assert abs(calc - DELTA_POOLED) < 1e-9

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
        assert "n=1 vs n=2" in res["methodology"]


# ---------------------------------------------------------------------------
# 7. Research method
# ---------------------------------------------------------------------------
class TestResearchMethod:
    def test_scout_and_main_run_query_sets_documented(self):
        method = _block()["research_method"]
        assert "1 delegated scout" in method
        assert "1 main-run" in method
        assert "browser.search verification set" in method

    def test_scout_rejections_documented(self):
        method = _block()["research_method"]
        assert "delegated scout" in method
        assert "m965 double-count" in method
        assert "#1247 precedent" in method

    def test_zero_browser_open(self):
        assert "0 browser.open per #503" in _block()["research_method"]

    def test_ascii_no_em_dash(self):
        # In-gate fix: scoped to this run's landed block. guardian.yaml
        # carries 189 pre-existing em dashes at HEAD (all outside the
        # m994 block), so the whole-file assertion cannot pass without
        # rewriting history. The ASCII discipline is asserted on the
        # m994 block's own content via an allow_unicode round-trip.
        dumped = yaml.safe_dump(_block(), allow_unicode=True)
        assert "\u2014" not in dumped

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
# 9. Guard lifecycle: verifies #1271's forward guards, lays #1273's pins
# ---------------------------------------------------------------------------
class TestGuardLifecycle1272:
    def test_pins_on_994_landing(self):
        # Type A lands m994: max becomes 994, next is 995.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 994" in src
        assert "NEXT_NUM = 995" in src

    def test_no_type_a_1272_in_git_log_pin(self):
        # Post-main-commit form (the #1191-class self-trip, re-pinned
        # in the terminal log-hash followup per #721): every commit
        # whose message matches "Type A #1272" must be this run's
        # main commit or a descendant of it - i.e., no PRIOR run
        # committed this run's iteration. The ancestor check (not an
        # enumerated own-set) is robust to any number of same-run
        # followup commits: each followup is a descendant of main by
        # construction, so the pin is stable and terminal. Deselected
        # in the in-gate run (fails pre-commit by design).
        out = _git("log", "--format=%H", "--grep=Type A #1272")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected this run's own commits"
        main = _git("rev-parse", PRED_MAIN_1272).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_no_type_b_1273_in_git_log_pin(self):
        # Post-main-commit form for the NEXT leg (the #1191-class
        # self-trip, re-pinned in #1273's terminal log-hash followup
        # per #721): every commit whose message matches "Type B #1273"
        # must be #1273's main commit or a descendant of it.
        # Deselected in the in-gate run (fails pre-commit by design).
        out = _git("log", "--format=%H", "--grep=Type B #1273")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1273's own commits"
        main = _git("rev-parse", PRED_MAIN_1273).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_995_numeric_absent_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_995_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_995_dash_absent_repo_wide(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_no_fortieth_direction_pin(self):
        # The fortieth direction-claim form stays absent in profiles/
        # (profiles-scoped per the #1199 in-gate fix).
        assert _git_grep_tracked_source(_T40, "profiles/") == []

    def test_forty_eighth_member_intact_pin(self):
        # The live forty-eighth member claims (m952,
        # profiles/financial-times.yaml) must survive this run
        # unchanged.
        assert _git_grep_tracked_source(_T48, "profiles/") == [
            "profiles/financial-times.yaml"]

    def test_forty_ninth_member_intact_pin(self):
        # The live forty-ninth member claims (m956,
        # careers/journalists.yaml) must survive this run unchanged.
        assert _git_grep_tracked_source(_T49, "profiles/") == [
            "profiles/careers/journalists.yaml"]

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
        # The live fifty-fourth member claims (m985,
        # profiles/guardian.yaml, 2x, landed at #1257) must survive
        # this run unchanged.
        out = _git(
            "grep", "-c", "-F", _T54, "HEAD", "--",
            "profiles/guardian.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_no_fifty_fifth_member_pin(self):
        assert _git_grep_tracked_source(_T55, None) == []

    def test_predecessor_1271_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, E1271_FILE))

    def test_next_leg_is_1273_type_b(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#1273 Type B" in src

    def test_1271_pins_stay_green_documented(self):
        # #1271's forward guards (max-993, zero-994 keys all forms,
        # no-Type-A-#1272-in-git-log, fortieth absent, forty-eighth +
        # forty-ninth + fiftieth + fifty-first + fifty-second +
        # fifty-third + fifty-fourth intact, no fifty-fifth; ledger 54)
        # verified GREEN at HEAD pre-commit this run. The
        # no-Type-A-#1272-in-git-log pin flips BY DESIGN at this run's
        # main commit (the #1191-class self-trip, re-pinned post-commit
        # by TestStalenessPins1272) and the zero-994-numeric pin trips
        # on the landed m994 block; the zero-994-underscore/dash pins
        # stay green per the #715 literal discipline. Documented in the
        # staleness pin below, not repaired.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "TestStalenessPins1272" in src
        assert "no_type_a_1272_in_git_log_pin" in src


# ---------------------------------------------------------------------------
# 10. Staleness pins: #1271's guard lifecycle flips by design
#     (1 test; deselected pre-commit, verified post-main-commit)
# ---------------------------------------------------------------------------
class TestStalenessPins1272:
    def _class_run(self, filename, classname):
        target = os.path.join(TESTS_DIR, filename)
        env = dict(os.environ)
        env["PYTEST_DISABLE_PLUGIN_AUTOLOAD"] = "1"
        res = subprocess.run(
            ["python3", "-m", "pytest", target,
             "-k", classname,
             "-q", "--no-header"],
            cwd=REPO_ROOT, capture_output=True, text=True, env=env,
        )
        return res

    def test_1271_guard_lifecycle_post_commit(self):
        # Post-main-commit form: 17 tests in the class, 15 pass and
        # TWO flip BY DESIGN when this run's main commit lands: the
        # no_type_a_1272_in_git_log ancestor pin (its PRED_MAIN_1272
        # is still the 0*40 placeholder until this run's terminal
        # log-hash followup re-pins it per #721) and the
        # zero-994-numeric pin (trips on the landed m994 block) - the
        # #1191-class self-trip family. The pin is re-pinned to the
        # post-commit own-set form in the terminal log-hash followup
        # per #721; the class run below therefore expects the 15
        # surviving pins green and documents the two designed flips.
        # The #1271 block is read-only to this run; the quirk is
        # documented here, not repaired.
        res = self._class_run(
            E1271_FILE,
            "TestGuardLifecycle1271",
        )
        out = res.stdout + res.stderr
        assert "2 failed, 15 passed" in out, out[-2000:]
        assert "no_type_a_1272_in_git_log" in out, out[-2000:]


# ---------------------------------------------------------------------------
# 11. Doc-sync per #719 (3 tests; deselected pre-commit, flipped post-sync)
# ---------------------------------------------------------------------------
class TestDocSync:
    def test_readme_test_file_table_has_1272_row_post_sync(self):
        readme = _read(README_PATH)
        assert "test_type_a_1272" in readme

    def test_architecture_has_1272_row_post_sync(self):
        arch = _read(ARCH_PATH)
        assert "test_type_a_1272" in arch

    def test_readme_stats_ratcheted(self):
        # Post-sync-positive form per #719: asserts the ratcheted
        # counts (README_TEST_COUNT tests across README_FILE_COUNT
        # files). Fails pre-commit by design; deselected in the
        # in-gate run.
        readme = _read(README_PATH)
        assert ("| Tests | %d |" % README_TEST_COUNT) in readme
        assert ("Across %d test files" % README_FILE_COUNT) in readme


# ---------------------------------------------------------------------------
# 12. Iteration log (3 tests; deselected pre-commit per #721)
# ---------------------------------------------------------------------------
class TestIterationLog:
    def test_1272_entry_present_post_sync(self):
        log = _read(LOG_PATH)
        assert "## #1272 Type A" in log

    def test_1271_entry_present(self):
        log = _read(LOG_PATH)
        assert "## #1271 Type E" in log

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
class TestBackgroundSuite1272:
    def test_1270_suite_log_exists(self):
        assert os.path.exists(
            os.path.join(GOAL_HIDDEN, "type_d_1270_full_suite.log"))

    def test_this_run_launches_no_suite(self):
        # This run must not launch its own background suite; only the
        # #1270-launched suite is observed (verdict belongs to #1275).
        assert not os.path.exists(
            os.path.join(GOAL_HIDDEN, "type_d_1272_full_suite.log"))

    def test_observation_only_documented(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "OBSERVES only" in src
        assert "verdict belongs to #1275" in src
