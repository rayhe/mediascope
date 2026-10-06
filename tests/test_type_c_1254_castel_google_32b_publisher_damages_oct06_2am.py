# -*- coding: utf-8 -*-
"""Type C #1254 tests: m984 Sep-30-2026 SDNY damages ruling (Judge P. Kevin
Castel) - USA Today Co., DMGT, and a ~5,000-publisher class cleared to seek
$3.2B+ in AdX-monopoly damages from Google ($1.7B class / $900M USA Today /
$600M DMGT; trebling available); FIRST dedicated corpus mechanism on the
publisher-damages financial pipeline vs Google (connects_to m801).

Mechanism 984 (MECHANISM DOCUMENTED; ledger HOLDS at 53 - NOT a
falsification-family member). Prior corpus coverage: the ruling carried
only as a Type A bounded-absence arm in profiles/guardian.yaml (zero
Guardian originals on the Oct-1 ruling, carried via the newdigitalage Ad
World roundup of the Bloomberg original, Leah Nylen and David Voreacos,
Oct 1); the Sep-16 EDVA behavioral-remedies leverage leg (mechanism 801,
marketplace_intermediary_landscape block); zero dedicated Type C
financial-mechanism block on any publisher-damages pipeline. The ruling:
Sep 30 2026, US District Judge P. Kevin Castel (SDNY), 88-page opinion,
denied Google summary judgment, jury trials move forward on AdX-related
harm, Google bid to contest damage calculations rejected. The numbers:
~$1.7B class, ~$900M USA Today, ~$600M DMGT, over $3.2B combined,
trebling available if liability is proven; GOOG/GOOGL slipped about
1.7% the next day. Google response: dismissed claims for a different
ad-buying tool, will defend the rest in court. Type C nexus: publishers
stand to recover billions from the same company (Google) they negotiate
AI-content licensing terms with - the damages leg completes the Google
publisher-money-flow family alongside the m801 leverage leg. No
coverage-tone pair scored; tone NOT_SCORED. MANUAL / qualitative ONLY per
the Aug 28 2026 standing rule.

Excerpt-bounded research per #503 (delegated scout: 17 browser.search
query sets across 15 angles + 1 main-run browser.search verification set
with 7 corroborating results; 0 browser.open reads). Scout rejections on
verification: Google AI Contribution Pilot payout tiers (in corpus m951);
Penske/Chegg AI Overviews dismissal (in-corpus suit family, not a new
mechanism); Chicago Tribune v Perplexity Oct-1 filing (mirrors in-corpus
Perplexity suits); DOJ fair-use brief in NYT v OpenAI (litigation
development, no new tie); Meta x News Corp $50M/yr (in corpus m549);
Axel Springer x OpenAI renewal (bounded absence, no news); Anthropic
zero-deals posture (in corpus #509/#718); xAI zero deals (in corpus
m813); Microsoft x Nine (Jul 2026, outside window); Apple Siri pay-per-use
(in corpus m156, bounded absence); Reddit-Google $60M renewal (in corpus,
no resolution); Perplexity Comet Plus (in corpus #864); Folha x OpenAI
(May 2026, outside window); News Corp five-leg architecture (in corpus
#594); Cloudflare pay-per-crawl (in corpus m64, July not October); NYT x
Amazon (May 2025, in corpus); Seattle Times/Newsday v OpenAI (in-corpus
m982 family); Round Hill v Anthropic (music, out of scope); Amazon x
Synopsys $1B (non-publisher); OAN AI-lab pact suit (no publisher tie);
Conde Nast portfolio (in corpus #58/#684); OpenAI DevDay Adobe/SoftwareOne
(enterprise, non-publisher). SELECTED: the Castel $3.2B ruling (Sep 30;
7 corroborating relays Oct 1-5: insurancejournal, claimsjournal,
tradingview, biggo, freeaitoolsayoob, zubiqo, videoweek; 3 landed as
block sources, 4 additional zero-hit relays documented).

The mechanism 984 block lives in profiles/competitor-entities.yaml as a
top-level key appended at end of file (explicit-path staging).

Anchor convention per #565: ANCHORED_SHA starts as 0*40 in this pre-commit
file and is patched to the main-commit hash in the anchor followup commit.
One anchor test (the placeholder pin) fails BY DESIGN post-anchor.

Per #795: this run neither re-launches nor checks a live suite. The #1245
suite verdict was rendered at #1250 (ALIVE at 20%; the forty-third death
streak broke; tombstone lineage held at one-hundred-eighth; NO suite
re-launch at #1250, so no type_d_1250 log exists); the next verdict
belongs to #1255. The observation classes below document this.

Do NOT touch #1024 (m846), #899 (nytimes.yaml m771 hunk), #938 (Type B
test file working-tree edit), #900 (untracked Type D test file),
#1012-wt (working-tree edit on the committed Type A #1012 file).

Type C lands one mechanism (mechanism 984); the Type B predecessor landed
one (mechanism 983, thesis-consistent observation, NOT a falsification
member). This run is the FIFTH and CLOSING leg of the 1250-1254 window.
Next run #1255 Type D opens the 1255-1259 window. Rotation: D #1250 ->
E #1251 -> A #1252 -> B #1253 -> C #1254. The main commit is the anchor
per #565. The 1245-1249 window is VERIFIED CLOSED.

ASCII-only, no em dashes. Needles format-built per #715: this file must
not carry contiguous numeric/underscore/dash mechanism-key forms of the
landed or next number, the forty-eighth / forty-ninth / fiftieth /
fifty-first / fifty-second / fifty-third / fifty-fourth falsification
forms, or the fortieth direction form.
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
OWN_BASENAME = (
    "test_type_c_1254_castel_google_32b_publisher_"
    "damages_oct06_2am.py"
)
TOP_KEY = None  # Type C lands at competitor-entities.yaml top level.

# Patched per #565 in the anchor followup (main commit sha).
ANCHORED_SHA = "8ff1eed80f1860b3cf5dbe565933b10e3c9cbc15"  # patched green in the anchor followup per #565

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

MECH_NUM = 984
NEXT_NUM = 985  # integer only; key-form needles are format-built

# Fragment-built per #715: the contiguous key never appears in this file.
BLOCK_KEY = (
    "type_c_1254_castel_google_32b_publisher_"
    "damages_pipeline_oct06_2am"
)

# Predecessor chain: #1253 Type B closed the fourth leg of the window.
PRED_MAIN_1253 = "49b7e7ab"
PRED_ANCHOR_1253 = "d29a1189"
PRED_DOCSYNC_1253 = "19c79d54"
PRED_FINAL_1253 = "d71a8cc5"

# The #1253 window-continuation file, for the staleness pin on its
# guard-lifecycle class (max id 983; zero next-number forms /
# no-Type-C-#1254-in-git-log / fortieth direction absent /
# forty-eighth + forty-ninth + fiftieth + fifty-first + fifty-second +
# fifty-third members intact / fifty-fourth member absent / ledger 53).
E1253_FILE = (
    "test_type_b_1253_kelsey_vlamis_bi_muse_shopping_trust_vs_"
    "openai_cyber_defense_oct06_1am.py"
)

# Doc-sync constants per #719: post-doc-sync values from the start.
# Patched pre-main once the in-gate collection count is known.
README_TEST_COUNT = 68858  # post-doc-sync total (pre-sync 68770 + 88)
README_FILE_COUNT = 1579  # pre-sync 1578 + 1 (this file)

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

# Novel source URLs: all 3 zero-hit repo-wide pre-commit
# (git grep -F). Post-commit all 3 live in the block's source_urls.
NOVEL_URLS = [
    "https://www.insurancejournal.com/news/east/2026/10/05/887945.htm",
    "https://www.claimsjournal.com/news/national/2026/10/02/340522.htm",
    "https://www.tradingview.com/news/stocktwits:2b3fedb2d094b:0-"
    "google-could-face-3-2b-in-damages-over-ad-tech-monopoly-"
    "federal-judge-rules/",
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

class TestAnchor1254:
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
        assert "FIFTH and CLOSING leg of the 1250-1254 window" in src


# ---------------------------------------------------------------------------
# 2. Rotation guard
# ---------------------------------------------------------------------------

class TestRotationGuard1254:
    def test_predecessor_shas_in_git_log(self):
        log = _git("log", "--oneline", "-30").stdout
        for sha, label in (
            (PRED_MAIN_1253, "1253 main"),
            (PRED_ANCHOR_1253, "1253 anchor"),
            (PRED_DOCSYNC_1253, "1253 doc-sync"),
            (PRED_FINAL_1253, "1253 log-hash"),
        ):
            assert sha in log, label

    def test_1253_type_b_in_git_log(self):
        out = _git("log", "--oneline", "--grep=Type B #1253").stdout
        assert out.strip() != ""

    def test_closing_leg_phrase(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "FIFTH and CLOSING leg of the 1250-1254 window" in src

    def test_1245_1249_window_closed(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "1245-1249" in src
        assert "VERIFIED CLOSED" in src

    def test_next_window_opens_1255(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Next run #1255 Type D" in src


# ---------------------------------------------------------------------------
# 3. Mechanism novelty (the #715 discipline)
# ---------------------------------------------------------------------------

class TestMechanismNovelty1254:
    def test_max_mechanism_id_is_984_post_landing(self):
        assert _max_numeric_mechanism_id() == MECH_NUM

    def test_block_key_present(self):
        assert BLOCK_KEY in _load_entities()

    def test_block_key_occurs_twice_in_text(self):
        # Once as the YAML key, once as the block_key field.
        assert _block_text().count(BLOCK_KEY) == 2

    def test_984_numeric_present_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(MECH_NUM) != []

    def test_984_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(MECH_NUM) == []

    def test_984_dash_absent_repo_wide(self):
        assert _repo_grep_dash_mechanism(MECH_NUM) == []

    def test_iteration_field(self):
        assert _block()["iteration"] == 1254

    def test_iteration_type_field(self):
        assert _block()["iteration_type"] == "C"


# ---------------------------------------------------------------------------
# 4. Block structure at the competitor-entities.yaml top level.
# ---------------------------------------------------------------------------

class TestBlockStructure1254:
    def test_block_key_top_level(self):
        data = _load_entities()
        assert BLOCK_KEY in data

    def test_mechanism_id_field(self):
        assert _block()["mechanism_id"] == 984

    def test_required_fields_present(self):
        b = _block()
        for field in (
            "block_key", "mechanism_id", "mechanism_name", "type",
            "iteration", "finding", "sources", "verdict",
            "falsification_family", "novelty", "rotation_transparency",
            "concurrency",
        ):
            assert field in b, field

    def test_connects_to_801(self):
        # m801: the Sep-16 EDVA behavioral-remedies leverage leg (the
        # first Google publisher-money-flow leg) - this run's damages
        # leg completes the family alongside it.
        assert 801 in _block()["connects_to"]

    def test_three_novel_sources(self):
        srcs = _block()["sources"]
        assert len(srcs) == 3
        assert all(s["novel"] is True for s in srcs)

    def test_yaml_parse_clean_flag(self):
        assert _block()["yaml_parse_clean"] is True

    def test_ascii_only_flag(self):
        assert _block()["ascii_only"] is True


# ---------------------------------------------------------------------------
# 5. Content discipline: verbatim excerpts, no constructed URLs.
# ---------------------------------------------------------------------------

class TestM984ContentDiscipline1254:
    def test_novel_urls_in_block_sources(self):
        urls = [s["url"] for s in _block()["sources"]]
        for u in NOVEL_URLS:
            assert u in urls, u

    def test_source_urls_verbatim_shape(self):
        for s in _block()["sources"]:
            assert s["url"].startswith("https://")
            assert " " not in s["url"]

    def test_accessed_dates_oct06(self):
        for s in _block()["sources"]:
            assert s["accessed"] == "2026-10-06"

    def test_browser_opens_zero(self):
        assert _block()["browser_opens"] == 0

    def test_excerpt_bounded_documented(self):
        assert "0 browser.open" in _block()["novelty"]

    def test_scout_rejections_documented(self):
        nov = _block()["novelty"]
        finding = _block()["finding"]
        assert "Scout rejections documented" in nov
        assert "FIRST dedicated corpus mechanism on the Sep-30-2026" in finding

    def test_damages_figures(self):
        finding = _block()["finding"]
        assert "$3.2B" in finding
        assert "$1.7B" in finding
        assert "$900M" in finding
        assert "$600M" in finding

    def test_ruling_facts(self):
        finding = _block()["finding"]
        assert "Sep 30 2026" in finding
        assert "P. Kevin Castel" in finding
        assert "88-page opinion" in finding
        assert "AdX" in finding

    def test_trebling_discipline(self):
        finding = _block()["finding"]
        assert "trebling available" in finding

    def test_damages_not_licensing(self):
        # The damages-not-licensing discipline lives in the strong
        # confounders, not the finding prose.
        texts = [c["text"] for c in _block()["confounders"]]
        assert any("antitrust-damages pipeline" in t for t in texts)

    def test_google_response(self):
        finding = _block()["finding"]
        assert "defend the rest in court" in finding

    def test_type_c_nexus(self):
        finding = _block()["finding"]
        assert "m801" in finding


# ---------------------------------------------------------------------------
# 6. Statistical discipline: MANUAL / qualitative only per Aug 28 2026 rule.
# ---------------------------------------------------------------------------

class TestStatisticalDiscipline1254:
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
# 7. Falsification ledger: NOT a member; ledger holds at 53.
# ---------------------------------------------------------------------------

class TestFalsificationLedger1254:
    def test_ledger_holds_at_53(self):
        assert "ledger holds at 53" in _block()["falsification_family"]

    def test_not_a_member(self):
        b = _block()
        assert b["falsification_family_member"] is False
        assert b["falsification_family"].startswith("NOT a member")

    def test_forty_eighth_intact_in_ft(self):
        assert _git_grep_tracked_source(_T48, "profiles/") == [
            "profiles/financial-times.yaml"]

    def test_forty_ninth_intact_in_journalists(self):
        assert _git_grep_tracked_source(_T49, "profiles/") == [
            "profiles/careers/journalists.yaml"]

    def test_fiftieth_intact_in_journalists(self):
        out = _git(
            "grep", "-c", "-F", _T50, "HEAD", "--",
            "profiles/careers/journalists.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fifty_first_intact_in_newscorp(self):
        out = _git(
            "grep", "-c", "-F", _T51, "HEAD", "--",
            "profiles/news-corp.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fifty_second_intact_in_journalists(self):
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

    def test_no_fifty_fourth_member_pin(self):
        assert _git_grep_tracked_source(_T54, ".") == []

    def test_no_fortieth_direction_pin(self):
        assert _git_grep_tracked_source(_T40, "profiles/") == []

    def test_directions_thirty_fifth_through_thirty_ninth_present(self):
        for needle in (
            "THIRT" + "Y-FIFTH relationship direction",
            "THIRT" + "Y-SIXTH relationship direction",
            "THIRT" + "Y-SEVENTH relationship direction",
            "THIRT" + "Y-EIGHTH relationship direction",
            "THIRT" + "Y-NINTH relationship direction",
        ):
            assert _git_grep_tracked_source(needle, "profiles/") != [], needle


# ---------------------------------------------------------------------------
# 8. Guard lifecycle: forward guards for #1255 (Type D)
# ---------------------------------------------------------------------------

class TestGuardLifecycle1254:
    def test_pins_on_984_landing(self):
        # Type C lands m984: max becomes 984, next is 985.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 984" in src
        assert "NEXT_NUM = 985" in src

    def test_no_type_d_1255_in_git_log_pin(self):
        out = _git("log", "--oneline", "--grep=Type D #1255")
        assert out.stdout.strip() == ""

    def test_985_numeric_absent_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_985_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_985_dash_absent_repo_wide(self):
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

    def test_fifty_third_member_intact_pin(self):
        out = _git(
            "grep", "-c", "-F", _T53, "HEAD", "--",
            "profiles/the-verge.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_no_fifty_fourth_member_pin(self):
        assert _git_grep_tracked_source(_T54, ".") == []

    def test_predecessor_1253_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, E1253_FILE))

    def test_next_leg_is_1255_type_d(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#1255 Type D" in src

    def test_1253_pins_flip_by_design_documented(self):
        # #1253's forward guards (max-983, zero-984 keys all forms,
        # no-Type-C-#1254-in-git-log, fortieth absent, forty-eighth +
        # forty-ninth + fiftieth + fifty-first + fifty-second +
        # fifty-third intact in profiles/, fifty-fourth absent, ledger
        # 53) verified GREEN pre-commit this run via the subprocess
        # staleness pin (Type C lands mechanism 984 as a documentation
        # event, NOT a falsification-family member); the max-983,
        # zero-984-numeric, and no-Type-C-#1254-in-git-log pins flip
        # post-main-commit on this run's own landing (the #1191-class
        # self-trip, by design, documented in the staleness pin below).
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "TestStalenessPins1254" in src
        assert "no_type_c_1254_in_git_log_pin" in src


# ---------------------------------------------------------------------------
# 9. Background suite: no live suite this run per #795.
# ---------------------------------------------------------------------------

class TestBackgroundSuiteCheck1254:
    def test_1245_suite_log_exists(self):
        assert os.path.exists(
            os.path.join(GOAL_HIDDEN, "type_d_1245_full_suite.log"))

    def test_no_1250_suite_log(self):
        # #1250 Type D rendered the #1245 verdict and did NO re-launch,
        # so no #1250 suite log exists. This run neither re-launches,
        # kills, nor writes to any suite.
        assert not os.path.exists(
            os.path.join(GOAL_HIDDEN, "type_d_1250_full_suite.log"))

    def test_this_run_launches_no_suite(self):
        # This run must not launch its own background suite; only
        # observation classes document the suite state.
        assert not os.path.exists(
            os.path.join(GOAL_HIDDEN, "type_d_1254_full_suite.log"))

    def test_verdict_belongs_to_1255(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "belong to #1255" in src


# ---------------------------------------------------------------------------
# 10. Doc-sync (post-sync positive per #719; deselected in-gate).
# ---------------------------------------------------------------------------

class TestDocSync1254:
    def test_readme_test_file_table_has_1254_row_post_sync(self):
        text = _read(README_PATH)
        assert "test_type_c_1254" in text

    def test_architecture_has_1254_row_post_sync(self):
        text = _read(ARCH_PATH)
        assert "test_type_c_1254" in text

    def test_readme_stats_ratcheted(self):
        text = _read(README_PATH)
        assert str(README_TEST_COUNT) in text
        assert str(README_FILE_COUNT) in text


# ---------------------------------------------------------------------------
# 11. Iteration log (post-sync positive per #721; deselected in-gate).
# ---------------------------------------------------------------------------

class TestIterationLog1254:
    def test_1254_entry_present_post_sync(self):
        text = _read(LOG_PATH)
        assert "## #1254" in text

    def test_1253_entry_present(self):
        text = _read(LOG_PATH)
        assert "## #1253" in text

    def test_rotation_transparency_convention(self):
        text = _read(LOG_PATH)
        assert "1250-1254 window" in text


# ---------------------------------------------------------------------------
# 12. Staleness pins: #1253's guard lifecycle flips by design
#      (1 test; deselected pre-commit, verified post-main-commit)
# ---------------------------------------------------------------------------

class TestStalenessPins1254:
    def test_1253_guard_lifecycle_flips_by_design_post_commit(self):
        # Runs the #1253 file's guard-lifecycle class post-commit:
        # its no-Type-C-#1254-in-git-log pin self-trips on this run's
        # own main commit and its zero-984-numeric pin trips on the
        # landed m984 block (both BY DESIGN, the #1191-class self-trip
        # family); the class is expected to report the flips, not to
        # stay green.
        res = _class_run(E1253_FILE, "TestGuardLifecycle1253")
        assert res.returncode != 0, res.stdout[-2000:]
        assert "2 failed, 14 passed" in res.stdout, res.stdout[-2000:]
        assert "test_no_type_c_1254_in_git_log_pin" in res.stdout, res.stdout[-2000:]
        assert "test_984_numeric_absent_in_profiles" in res.stdout, res.stdout[-2000:]


# ---------------------------------------------------------------------------
# 13. In-flight isolation: other runs' working state untouched.
# ---------------------------------------------------------------------------

class TestInFlightIsolation1254:
    def test_899_nytimes_hunk_not_staged(self):
        out = _git("diff", "--cached", "--name-only").stdout
        assert "profiles/nytimes.yaml" not in out

    def test_938_test_file_untouched(self):
        out = _git("diff", "--cached", "--name-only").stdout
        assert "test_type_b_938" not in out

    def test_900_test_file_untracked_not_staged(self):
        out = _git("diff", "--cached", "--name-only").stdout
        assert "test_type_d_900" not in out

    def test_1012_wt_untouched(self):
        out = _git("diff", "--cached", "--name-only").stdout
        assert "test_type_a_1012" not in out

    def test_only_expected_paths_staged(self):
        out = _git("diff", "--cached", "--name-only").stdout
        staged = [l.strip() for l in out.splitlines() if l.strip()]
        allowed = {
            "tests/" + OWN_BASENAME,
            "profiles/competitor-entities.yaml",
        }
        assert set(staged) <= allowed, staged


README_TEST_COUNT = 68858  # patched post-sync per #719
README_FILE_COUNT = 1579  # patched post-sync per #719
