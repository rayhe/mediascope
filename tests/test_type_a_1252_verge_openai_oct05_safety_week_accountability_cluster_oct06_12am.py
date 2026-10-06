"""Type A #1252: m982 The Verge Oct-5-2026 safety-week accountability cluster
on the Vox-deal partner OpenAI (Oct 6 2026, 12:00 AM PDT).

Three NEW Oct-5-2026 Verge arms on OpenAI, all mirror-attested (no
verbatim theverge.com canonical URLs surfaced; not constructed per
rule): (1) Emma Roth ~12:55 PM, "OpenAI PR tells journalist to 'move
on' while asking Sam Altman about a ChatGPT user's suicide" -
adversarial accountability on PR-deflection (-0.60); (2) Robert Hart
~12:44 PM, "Sam Altman says 'some bad things' will happen but AI is
totally worth it" - critical cost-benefit framing (-0.45); (3) Jay
Peters, "Wikipedia operator says OpenAI's 'rogue' bots may be linked
to a May outage" - adversarial third-party safety relay (-0.50).
Cluster mean -0.52 vs carried Meta arms mean -0.55 (#592 via m880,
un-rescored per #807); illustrative delta (OpenAI minus Meta) +0.03
near-null symmetric adversarial (m974-class).

Verdict: falsification_member_confirmed. The Vox Media x OpenAI
May-2024 content-licensing + product deal (active per Sep 2026
verification, the-verge.yaml financial metadata) predicts softer
coverage of the deal partner; The Verge applies its adversarial
accountability register to OpenAI at the same hardness as to Meta.
The naive uniform payer-softening prediction FAILS at The Verge
(publication level). This run lands the fifty-third member of the
falsification family (ledger 52->53); the uppercase claim form lives
only in the profile block, never in this file. Publication-level
replication of the m974 journalist-level finding; temporal extension
of m880's Aug-Sep Astra-safety arc into October.

1 delegated scout (10 browser.search query sets across 8 candidate
pairs; SELECTED the Verge Oct-5 triple; REJECTED 8 with exact corpus
locations) + 3 main-run browser.search verification sets
(exact-headline "move on" Guiducci; exact-headline "some bad things";
canonical-URL hunt). 0 browser.open per #503 (excerpt-bounded).
Pre-commit novelty greps per #715: zero test_type_a_1252 files on
disk (glob); no "Type A #1252" in git log (--grep); max numeric
mechanism_id 981 in profiles/ pre-commit; zero numeric/underscore/
dash 982 mechanism key forms repo-wide pre-commit (needles
format-built, own file excluded); block key zero-hit repo-wide
pre-commit; 4 mirror URLs zero-hit repo-wide pre-commit (git grep -F);
"## #1252" zero-hit in iteration-log pre-commit; README stats
68608/1576 pre-commit; no #1252 row in README/ARCHITECTURE test
tables pre-commit.

Statistical discipline: MANUAL ILLUSTRATIVE ONLY per the Aug 28 2026
standing rule (engine NOT run; p_value/cohens_d/ci_95 NOT_CALCULATED;
is_significant False; NOT artifact-grade; no analysis.json update).
Correlation is not causation; hypothesis-generating only.

Type A lands m982 (MECH_NUM = 982); NEXT_NUM = 983 for the forward
guards. This run is iteration #1252 Type A, the THIRD leg of the
1250-1254 window (D #1250 -> E #1251 -> A #1252 -> B #1253 -> C #1254,
per the #565 anchor + rotation guard). Predecessor #1251 Type E
verified in git log (main ff9f8723 / anchor ffbc7210 / doc-sync
e1d22ee5 / log-hash 0f53fde7); #1250 Type D (main 3f986128 / anchor
5bee1864 / doc-sync 11827f60 / log-hash 431dd0f1). This run's main
commit is the anchor per #565; ANCHORED_SHA patched post-commit.
Next run #1253 Type B continues the window. The #1245-launched
background-suite verdict belongs to #1255 per #795: this run
OBSERVES only - neither re-launches, kills, nor writes to the suite.
In-flight during this run: #899 (profiles/nytimes.yaml m771 hunk),
#938 (Type B test file working-tree edit), #900 (untracked Type D
test file), #1012-wt (working-tree edit on the committed Type A
#1012 file) - all untouched; targeted staging only. Do NOT touch
#1024 m846.

ASCII-only, no em dashes. All hashes copied from git rev-parse /
git log output.
"""

import datetime
import os
import re
import subprocess

import pytest
import yaml

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TESTS_DIR = os.path.join(REPO_ROOT, "tests")
PROFILES_DIR = os.path.join(REPO_ROOT, "profiles")
VERGE_PATH = os.path.join(PROFILES_DIR, "the-verge.yaml")
LOG_PATH = os.path.join(REPO_ROOT, "iteration-log.md")
README_PATH = os.path.join(REPO_ROOT, "README.md")
ARCH_PATH = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")
GOAL_HIDDEN = os.path.join(
    os.path.expanduser("~"), "workspace", "goals",
    "mediascope-meta-wearables-press-analysis", "hidden_files",
)
OWN_BASENAME = (
    "test_type_a_1252_verge_openai_oct05_safety_week_"
    "accountability_cluster_oct06_12am.py"
)

# Pre-commit placeholder per #565; patched to the main commit sha in
# the anchor followup.
ANCHORED_SHA = "c7ef58911032a54e7b3be67835e72703c08c50c4"  # patched per #565 in the anchor followup (main commit sha)

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

MECH_NUM = 982  # this run's landed mechanism
NEXT_NUM = 983  # forward-guard number for #1253

# Predecessor chain: #1250 Type D opened, #1251 Type E continued.
PRED_MAIN_1250 = "3f986128"
PRED_ANCHOR_1250 = "5bee1864"
PRED_DOCSYNC_1250 = "11827f60"
PRED_FINAL_1250 = "431dd0f1"
PRED_MAIN_1251 = "ff9f8723"
PRED_ANCHOR_1251 = "ffbc7210"
PRED_DOCSYNC_1251 = "e1d22ee5"
PRED_FINAL_1251 = "0f53fde7"

# The #1251 window-continuation file, for the staleness pin on its
# guard-lifecycle class.
E1251_FILE = (
    "test_type_e_1251_podcast_sentiment_173rd_"
    "verification_oct05_11pm.py"
)

# Doc-sync constants per #719: post-doc-sync values from the start.
# Patched pre-main once the in-gate collection count is known.
README_TEST_COUNT = 68685  # post-doc-sync total (pre-sync 68608 + 77)
README_FILE_COUNT = 1577  # pre-sync 1576 + 1

# The forward-guard needles are fragment-built per #715 so this file
# carries no contiguous literal of a forward-guard claim form. The
# fifty-third member claim lives ONLY in the profile block (working
# tree pre-commit, HEAD post-commit); this file references it via
# fragments.
_T40 = "FORT" + "IETH relationship direction"
_T48 = "FORT" + "Y-EIGHTH falsification-family member"
_T49 = "FORT" + "Y-NINTH falsification-family member"
_T50 = "FIFT" + "IETH falsification-family member"
_T51 = "FIFT" + "Y-FIRST falsification-family member"
_T52 = "FIFT" + "Y-SECOND falsification-family member"
_T53 = "FIFT" + "Y-THIRD falsification-family member"
_T54 = "FIFT" + "Y-FOURTH falsification-family member"

BLOCK_KEY = (
    "type_a_1252_verge_openai_oct05_safety_week_"
    "accountability_cluster_vs_carried_meta_arms"
)

# The four mirror URLs (verbatim from Full-URL listings); all
# zero-hit repo-wide pre-commit via git grep -F.
NOVEL_URLS = [
    "https://newslink360.online/openai-pr-tells-journalist-to-move-on-while-asking-sam-altman-about-a-chatgpt-users-suicide/",
    "https://scoopfeeds.com/article/42435a6e-bfe9-5d5e-90e0-329a7810df1e",
    "https://newslink360.online/sam-altman-says-some-bad-things-will-happen-but-ai-is-totally-worth-it/",
    "https://rocketnews.com/2026/10/sam-altman-says-some-bad-things-will-happen-but-ai-is-totally-worth-it/",
]

# The three Oct-5 arms (MANUAL ILLUSTRATIVE tones).
ARMS = [
    {
        "title": "OpenAI PR tells journalist to 'move on' while asking "
                 "Sam Altman about a ChatGPT user's suicide",
        "byline": "Emma Roth",
        "tone": -0.60,
    },
    {
        "title": "Sam Altman says 'some bad things' will happen but AI "
                 "is totally worth it",
        "byline": "Robert Hart",
        "tone": -0.45,
    },
    {
        "title": "Wikipedia operator says OpenAI's 'rogue' bots may be "
                 "linked to a May outage",
        "byline": "Jay Peters",
        "tone": -0.50,
    },
]
CLUSTER_MEAN = -0.52  # (-0.60 + -0.45 + -0.50) / 3 = -0.5167
META_MEAN = -0.55  # carried #592 via m880, un-rescored per #807
DELTA = 0.03  # -0.52 - (-0.55), OpenAI minus Meta


def _read(path):
    with open(path, encoding="utf-8", errors="replace") as fh:
        return fh.read()


def _git(*args):
    return subprocess.run(
        ["git", *args], cwd=REPO_ROOT, capture_output=True, text=True
    )


def _load_verge():
    with open(VERGE_PATH, encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def _block():
    data = _load_verge()
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


def _working_tree_grep_profiles(needle):
    """Grep working-tree profiles/ for a literal needle.

    Used for the fifty-third member pin: the landed claim lives in
    the uncommitted block pre-commit.
    """
    hits = []
    for root, dirs, files in os.walk(PROFILES_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
            p = os.path.join(root, f)
            if needle in open(p, encoding="utf-8", errors="replace").read():
                hits.append(p)
    return hits


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

class TestAnchor1252:
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
        assert "THIRD leg of the 1250-1254 window" in src


# ---------------------------------------------------------------------------
# 2. Rotation guard
# ---------------------------------------------------------------------------
class TestRotationGuard:
    def test_predecessor_1250_1251_chain_verified(self):
        for sha in (
            PRED_MAIN_1250, PRED_ANCHOR_1250, PRED_DOCSYNC_1250,
            PRED_FINAL_1250, PRED_MAIN_1251, PRED_ANCHOR_1251,
            PRED_DOCSYNC_1251, PRED_FINAL_1251,
        ):
            res = _git("cat-file", "-t", sha)
            assert res.stdout.strip() == "commit", "missing %s" % sha

    def test_window_order_phrase(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "D #1250 -> E #1251 -> A #1252 -> B #1253 -> C #1254" in src

    def test_next_leg_is_type_b_1253(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Next run #1253 Type B" in src

    def test_type_a_lands_m982(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Type A lands m982" in src


# ---------------------------------------------------------------------------
# 3. Mechanism novelty (the #715 discipline; landing-run form per #1238)
# ---------------------------------------------------------------------------
class TestMechanismNovelty1252:
    def test_max_numeric_mechanism_id_is_this_run(self):
        # The landed mechanism (982) is present in working-tree
        # profiles/ via the uncommitted block; nothing above it.
        assert _max_numeric_mechanism_id() == MECH_NUM
        for n in range(MECH_NUM + 1, MECH_NUM + 20):
            assert _repo_grep_numeric_mechanism_id(n) == [], n

    def test_block_key_zero_mechanism_number_substring(self):
        # Designed keying per #723/#738/#739: iteration 1252 in key,
        # no 982 or 983 substring.
        assert "1252" in BLOCK_KEY
        assert str(MECH_NUM) not in BLOCK_KEY
        assert str(NEXT_NUM) not in BLOCK_KEY

    def test_zero_underscore_mechanism_repo_wide(self):
        hits = _repo_grep_underscore_mechanism(MECH_NUM)
        assert hits == [], hits

    def test_zero_dash_mechanism_repo_wide(self):
        hits = _repo_grep_dash_mechanism(MECH_NUM)
        assert hits == [], hits

    def test_zero_numeric_next_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_no_duplicate_block_key(self):
        text = _read(VERGE_PATH)
        assert text.count(BLOCK_KEY + ":") == 1

    def test_novel_urls_in_block_source_urls_verbatim(self):
        urls = _block()["source_urls"]
        for novel in NOVEL_URLS:
            assert novel in urls, novel

    def test_fifty_third_member_present_in_block(self):
        # Working-tree form: the landed claim lives in the
        # uncommitted block pre-commit; exactly one file, twice.
        hits = _working_tree_grep_profiles(_T53)
        assert hits == [VERGE_PATH], hits
        text = _read(VERGE_PATH)
        assert text.count(_T53) == 2, text.count(_T53)

    def test_no_type_a_1252_in_git_log_pin(self):
        # Post-main-commit form (the #1191-class self-trip, re-pinned
        # in the terminal log-hash followup per #721): the ONLY
        # matches are this run's own commits, whose messages carry
        # the run's own iteration subject (the followup commits match
        # the grep, so they join the own set; HEAD is admitted for
        # any same-run followup). The pin's substance - no PRIOR run
        # committed this run's iteration - holds.
        out = _git("log", "--format=%H %s", "--grep=Type A #1252")
        own = {
            "c7ef5891", "9b9b0d16", "a9e340b2",
        }
        head = _git("rev-parse", "HEAD").stdout.strip()[:8]
        hits = [line for line in out.stdout.splitlines() if line.strip()]
        assert hits, "expected this run's own commits"
        for line in hits:
            assert (line.split()[0][:8] in own
                    or line.split()[0][:8] == head), line

    def test_1251_forward_guards_green_pre_commit(self):
        # #1251's forward pins for this run hold pre-commit: max-981
        # at HEAD, zero-982 all forms at HEAD, no-Type-A-#1252 in git
        # log, fortieth direction absent, 48th-52nd members intact,
        # no-53rd at HEAD, ledger 52.
        assert _git_grep_tracked_source(_T40, "profiles/") == []
        assert _git_grep_tracked_source(_T48, "profiles/") == [
            "profiles/financial-times.yaml"]
        assert _git_grep_tracked_source(_T49, "profiles/") == [
            "profiles/careers/journalists.yaml"]
        assert _git_grep_tracked_source(_T53, None) == []
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "ledger 52" in src


# ---------------------------------------------------------------------------
# 4. Finding: the Oct-5 Verge x OpenAI cluster
# ---------------------------------------------------------------------------
class TestVergeOct05Cluster:
    def test_block_lands_in_verge_openai(self):
        data = _load_verge()
        assert BLOCK_KEY in data["competitor_relationships"]["openai"]

    def test_mechanism_id_982(self):
        assert _block()["mechanism_id"] == MECH_NUM

    def test_three_arms(self):
        arms = _block()["openai_arms"]
        assert len(arms) == 3

    def test_arm_titles(self):
        titles = [a["item"]["title"] for a in _block()["openai_arms"]]
        for arm in ARMS:
            assert arm["title"] in titles, arm["title"]

    def test_arm_tones(self):
        tones = [a["item"]["manual_illustrative_tone"]
                 for a in _block()["openai_arms"]]
        assert tones == [-0.60, -0.45, -0.50]

    def test_cluster_mean_arithmetic(self):
        assert _block()["openai_cluster_mean"] == CLUSTER_MEAN
        calc = round(sum(a["tone"] for a in ARMS) / 3, 2)
        assert calc == -0.52

    def test_arm_dates_oct05(self):
        for a in _block()["openai_arms"]:
            assert a["item"]["date"] == "2026-10-05"

    def test_mirror_attested_tier(self):
        for a in _block()["openai_arms"]:
            assert a["item"]["evidence_tier"] == "mirror-attested"

    def test_novel_urls_zero_hit_pre_commit(self):
        # All four mirror URLs are this run's novel evidence; they
        # must not exist anywhere else in the working tree (the
        # block's own source_urls excepted).
        for url in NOVEL_URLS:
            out = _git("grep", "-F", "-l", url, "HEAD", "--", ".")
            assert out.stdout.strip() == "", url

    def test_vox_deal_active_disclosed(self):
        rel = _block()["financial_relationship"]
        assert "May 29 2024" in rel
        assert "ACTIVE" in rel


# ---------------------------------------------------------------------------
# 5. Meta comparator (carried, un-rescored per #807)
# ---------------------------------------------------------------------------
class TestMetaComparatorCarried:
    def test_carried_from_880(self):
        carried = _block()["meta_arms"]["carried_from"]
        assert "880" in carried
        assert "592" in carried

    def test_meta_band_mean(self):
        assert _block()["meta_arms"]["meta_band_mean"] == META_MEAN

    def test_three_meta_arms(self):
        assert len(_block()["meta_arms"]["arms"]) == 3


# ---------------------------------------------------------------------------
# 6. Asymmetry delta and falsification adjudication
# ---------------------------------------------------------------------------
class TestAsymmetryDelta:
    def test_delta_arithmetic(self):
        assert _block()["asymmetry_scorer_result"][
            "illustrative_delta_openai_minus_meta"] == DELTA
        assert round(CLUSTER_MEAN - META_MEAN, 2) == DELTA

    def test_near_null_symmetric(self):
        assert abs(DELTA) <= 0.05

    def test_falsification_member_true(self):
        assert _block()["falsification_family_member"] is True
        assert _block()["falsification_ledger"] == 53

    def test_engine_not_run(self):
        res = _block()["asymmetry_scorer_result"]
        assert res["engine_run"] is False
        assert res["p_value"] == "NOT_CALCULATED"
        assert res["is_significant"] is False

    def test_verdict_form(self):
        assert _block()["verdict"].startswith(
            "falsification_member_confirmed")


# ---------------------------------------------------------------------------
# 7. Research method
# ---------------------------------------------------------------------------
class TestResearchMethod:
    def test_scout_and_main_run_sets_documented(self):
        method = _block()["research_method"]
        assert "delegated scout" in method
        assert "3 main-run browser.search verification sets" in method
        assert "0 browser.open per #503" in method

    def test_eight_rejections_logged(self):
        method = _block()["research_method"]
        assert "REJECTED 8" in method

    def test_no_canonical_urls_constructed(self):
        method = _block()["research_method"]
        assert "no canonical URLs constructed" in method

    def test_ascii_only_no_em_dashes(self):
        # Only this run's appended block must be ASCII; the legacy
        # file carries pre-existing non-ASCII elsewhere (the #1238
        # precedent).
        text = _read(VERGE_PATH)
        assert "\u2014" not in text
        start = text.index(BLOCK_KEY + ":")
        block_text = text[start:]
        # The block runs to the end of the openai section (the next
        # top-level "  meta:" key).
        end = block_text.index("\n  meta:\n")
        block_text = block_text[:end]
        block_text.encode("ascii")
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "\u2014" not in src
        src.encode("ascii")


# ---------------------------------------------------------------------------
# 8. Statistical discipline
# ---------------------------------------------------------------------------
class TestStatisticalDiscipline:
    def test_manual_illustrative_only(self):
        disc = _block()["statistical_discipline"] if "statistical_discipline" in _block() else ""
        verdict = _block()["verdict"]
        assert "MANUAL ILLUSTRATIVE ONLY" in verdict

    def test_not_artifact_grade(self):
        assert _block()["asymmetry_scorer_result"][
            "artifact_grade"] is False

    def test_no_analysis_json_update(self):
        assert _block()["asymmetry_scorer_result"][
            "no_analysis_json_update"] is True

    def test_ledger_52_to_53(self):
        assert "ledger 52->53" in _block()["verdict"]

    def test_correlation_not_causation(self):
        assert "Correlation is not causation" in _block()["verdict"]


# ---------------------------------------------------------------------------
# 9. Guard lifecycle: forward pins for #1253 (Type B)
# ---------------------------------------------------------------------------
class TestGuardLifecycle1252:
    def test_pins_on_982_landing(self):
        # Type A lands m982: max becomes 982, next is 983.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 982" in src
        assert "NEXT_NUM = 983" in src

    def test_no_type_b_1253_in_git_log_pin(self):
        out = _git("log", "--oneline", "--grep=Type B #1253")
        assert out.stdout.strip() == ""

    def test_983_numeric_absent_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_983_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_983_dash_absent_repo_wide(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_no_fortieth_direction_pin(self):
        # The fortieth direction-claim form stays absent in profiles/.
        assert _git_grep_tracked_source(_T40, "profiles/") == []

    def test_forty_eighth_member_intact_pin(self):
        assert _git_grep_tracked_source(_T48, "profiles/") == [
            "profiles/financial-times.yaml"]

    def test_forty_ninth_member_intact_pin(self):
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

    def test_fifty_third_member_present_pin(self):
        # Working-tree form (the landed claim lives in the
        # uncommitted block pre-commit): present in exactly one
        # file, twice.
        hits = _working_tree_grep_profiles(_T53)
        assert hits == [VERGE_PATH], hits
        text = _read(VERGE_PATH)
        assert text.count(_T53) == 2, text.count(_T53)

    def test_no_fifty_fourth_member_pin(self):
        assert _git_grep_tracked_source(_T54, None) == []

    def test_predecessor_1251_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, E1251_FILE))

    def test_next_leg_is_1253_type_b(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#1253 Type B" in src

    def test_1251_pins_flip_by_design_documented(self):
        # #1251's forward guards (max-981, zero-982 keys all forms,
        # no-Type-A-#1252-in-git-log, fortieth absent, forty-eighth +
        # forty-ninth + fiftieth + fifty-first + fifty-second intact
        # in profiles/, no fifty-third) verified GREEN pre-commit
        # this run via the subprocess staleness pin (Type A lands
        # m982 as the fifty-third falsification-family member); the
        # max-981, zero-982-numeric, no-Type-A-#1252-in-git-log, and
        # no-fifty-third pins flip post-main-commit on this run's own
        # landing (the #1191-class self-trip, by design, documented in
        # the staleness pin below).
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "TestStalenessPins1252" in src
        assert "no_type_a_1252_in_git_log_pin" in src


# ---------------------------------------------------------------------------
# 10. Staleness pins: #1251's guard lifecycle flips by design
#      (1 test; deselected pre-commit, verified post-main-commit)
# ---------------------------------------------------------------------------
class TestStalenessPins1252:
    def test_1251_guard_lifecycle_flips_by_design_post_commit(self):
        # Runs the #1251 file's guard-lifecycle class post-commit:
        # its no-Type-A-#1252-in-git-log pin self-trips on this run's
        # own main commit, its zero-982-numeric pin trips on the
        # landed m982 block, and its no-fifty-third pin trips on the
        # landed fifty-third member claim (all BY DESIGN, the
        # #1191-class self-trip family); the class is expected to
        # report the flips, not to stay green.
        res = _class_run(E1251_FILE, "TestGuardLifecycle1251")
        assert res.returncode != 0, res.stdout[-2000:]
        assert "failed" in res.stdout, res.stdout[-2000:]


# ---------------------------------------------------------------------------
# 11. Doc-sync per #719 (3 tests; deselected pre-commit, flipped post-sync)
# ---------------------------------------------------------------------------
class TestDocSync:
    def test_readme_test_file_table_has_1252_row_post_sync(self):
        readme = _read(README_PATH)
        assert "test_type_a_1252" in readme

    def test_architecture_has_1252_row_post_sync(self):
        arch = _read(ARCH_PATH)
        assert "test_type_a_1252" in arch

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
    def test_1252_entry_present_post_sync(self):
        log = _read(LOG_PATH)
        assert "## #1252 Type A" in log

    def test_1251_entry_present(self):
        log = _read(LOG_PATH)
        assert "## #1251 Type E" in log

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
class TestBackgroundSuite1252:
    def test_1245_suite_log_exists(self):
        assert os.path.exists(
            os.path.join(GOAL_HIDDEN, "type_d_1245_full_suite.log"))

    def test_this_run_launches_no_suite(self):
        # This run must not launch its own background suite; only the
        # #1245-launched suite is observed (verdict belongs to #1255).
        assert not os.path.exists(
            os.path.join(GOAL_HIDDEN, "type_d_1252_full_suite.log"))

    def test_observation_only_documented(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "OBSERVES only" in src
        assert "verdict belongs to #1255" in src
