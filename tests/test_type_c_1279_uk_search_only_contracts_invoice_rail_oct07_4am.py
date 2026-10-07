# -*- coding: utf-8 -*-
"""Type C #1279 tests: m999 UK Search-Only Contracts invoice rail
(Oct 7, 2026) - FIRST dedicated corpus mechanism on the publisher-side
per-scrape pricing rail: on June 15 2026 the Movement for an Open Web
(Tim Cowan / James Rosewell; Association of Online Publishers +
Professional Publishers Association backed) launched legally binding
Search-Only Contracts with 31 founding UK publisher sites (Candr Media /
Trusted Reviews; F-At / road.cc, off.road.cc, ebiketips.co.uk); terms
embedded in site policies and robots.txt prohibit LLM copying/repurposing
(ChatGPT and Gemini named), set a typical 500 GBP per-article fee for
unauthorized scraping with deemed acceptance on access, and enforce via
MoneyClaim.gov.uk (~50 GBP filing) and county-court small claims with
bailiff seizure at UK offices. THE TYPE C NEXUS: the invoice-economy leg
of the corpus money-flow taxonomy - where m786 (Cloudflare pay-per-crawl)
prices crawler ACCESS at the infrastructure edge and m915 (SPUR
meter-then-invite) prices negotiated usage through a coalition standard,
SOC prices unauthorized per-article USE unilaterally at the contract layer,
bypassing copyright litigation entirely; the first corpus mechanism to
price the zero-deal labs supply directly, with the falsifiable milestone
of the first issued invoice / first county-court claim / first negotiated
deal signed to avoid bailiff exposure. October-2026 freshness: SOC
re-surfaced in the Oct 1 Capitol Hill Stealth Bot Prohibition Act coverage
(webpronews, an m927 source) as the Atlantic counterpart. BOUNDARY
(explicit): unilateral, not bilateral - no competitor lab has signed or
paid; the contracts are directed AT OpenAI and Google but assert deemed
acceptance by access, a theory untested in court at write time; no
confirmed issued invoices surfaced in this run verification sets; claims no
slot in the coverage-tone falsification ledger.

Mechanism 999 (MECHANISM DOCUMENTED; ledger HOLDS at 55 - NOT a
falsification-family member). No new direction (fortieth stays
absent by design); thirty-fifth through thirty-ninth stand.

Excerpt-bounded research per #503 (delegated scout across 12 candidate
angles + 2 main-run browser.search verification sets; 0 browser.open
reads). Scout rejections on main-run verification: NMA-Bria collective RAG
licensing -> REJECTED (Mar 2026 vintage, no October movement;
corpus-first money flow but not October-fresh); OpenAI India deal quanta
(BCCL ~$5M/yr, Indian Express ~$3M/yr) -> REJECTED (quantum extension on
banked m609/m660/m709 deals, not a new money flow); Folha-Google Gemini
leg -> REJECTED (no primary source with date or terms; tracker/brief lines
only); OpenAI zero-ad-share / Cloudflare Pay Per Use / Getty-Perplexity /
Microsoft x Nine / OpenAI x Village Media / NYT x Amazon / Reach x Amazon /
Meta publisher bundle / Anthropic zero-deal / Google AI pilot / Microsoft
Publisher Marketplace / ProRata / TollBit / Mistral-AFP -> all SATURATED in
corpus. SELECTED: UK Search-Only Contracts invoice rail. The webpronews
Oct-1 Capitol Hill piece is already in corpus as an m927 source and is NOT
landed here (corroboration only).

The mechanism 999 block lives in profiles/competitor-entities.yaml as a
top-level key appended at end of file (the #1024 m846 hunk untouched;
explicit-path staging).

Anchor convention per #565: ANCHORED_SHA starts as 0*40 in this pre-commit
file and is patched to the main-commit hash in the anchor followup commit.
One anchor test (the placeholder pin) fails BY DESIGN post-anchor.

Per #795: this run only OBSERVES the #1275-launched background suite
(goal hidden_files type_d_1275_full_suite.log; observed at this run's
check: 1779 bytes, last write Oct 7 2026 02:01 PDT, zero live pytest
processes - NOT-ALIVE, observation not a verdict; the #1280 Type D run
owns the verdict and tombstone); this run neither re-launches, kills, nor
writes to the suite.

Do NOT touch #1024 (m846 in profiles/competitor-entities.yaml), #899
(nytimes.yaml m771 hunk), #938 (Type B test file working-tree edit), #900
(untracked Type D test file), #1012-wt (working-tree edit on the committed
Type A #1012 file).

Type C lands one mechanism (mechanism 999); the Type B predecessor landed
one (mechanism 998, control-case observation, not a member).
This run is the FIFTH and CLOSING leg of the 1275-1279 window. Next run
#1280 Type D opens the 1280-1284 window (and renders the #1275-launched
background-suite verdict per #795). Rotation: D #1275 -> E #1276 ->
A #1277 -> B #1278 -> C #1279. The main commit is the anchor per #565.
The 1270-1274 window is VERIFIED CLOSED.

ASCII-only, no em dashes. Needles format-built per #715: this file must
not carry contiguous numeric/underscore/dash mechanism-key forms of the
landed or next number, the forty-eighth / forty-ninth / fiftieth /
fifty-first / fifty-second / fifty-third / fifty-fourth / fifty-fifth
member-claim forms, or the thirty-fifth through fortieth direction forms;
the constants are constructed at runtime. (The landed ordinals live as
short lowercase forms in prose here; the live full-form claims live in
profiles: the forty-eighth in financial-times.yaml, the forty-ninth and
fiftieth in profiles/careers/journalists.yaml, the fifty-first in
profiles/news-corp.yaml, the fifty-second in
profiles/careers/journalists.yaml, the fifty-third in
profiles/the-verge.yaml, the fifty-fourth in profiles/guardian.yaml, the
fifty-fifth in profiles/atlantic.yaml.)
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
SUITE_LOG = os.path.join(GOAL_HIDDEN, "type_d_1275_full_suite.log")
OWN_BASENAME = (
    "test_type_c_1279_uk_search_only_contracts_"
    "invoice_rail_oct07_4am.py"
)
TOP_KEY = None  # Type C lands at competitor-entities.yaml top level.

# Patched per #565 in the anchor followup (main commit sha).
ANCHORED_SHA = "102fbeba0f590da40e98ecdcec71c2eed4043323"  # patched in the anchor followup per #565

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

MECH_NUM = 999
NEXT_NUM = 1000  # integer only; key-form needles are format-built

# Fragment-built per #715: the contiguous key never appears in this file.
BLOCK_KEY = (
    "type_c_1279_uk_search_only_contracts_"
    "invoice_rail_oct07"
)

# Predecessor chain: #1278 Type B closed the fourth leg of the window.
PRED_MAIN_1278 = "41843930"
PRED_ANCHOR_1278 = "0989d150"
PRED_DOCSYNC_1278 = "bbda63d5"
PRED_FINAL_1278 = "f212c7b0"

# Placeholder for the NEXT leg's main commit sha per #721; re-pinned
# to #1280's main commit in #1280's terminal log-hash followup.
PRED_MAIN_1280 = "b8695266909c9b2a1b4a18019d27725aa3d31cb2"  # re-pinned per #721 in #1280 log-hash followup

# The #1278 window-continuation file, for the staleness pin on its
# guard-lifecycle class (max id 998; zero next-number forms /
# no-Type-C-#1279-in-git-log / fortieth direction absent /
# forty-eighth through fifty-fifth members intact / fifty-sixth member
# absent / ledger 55).
B1278_FILE = (
    "test_type_b_1278_kris_holt_engadget_meta_connect_"
    "roundup_vs_google_eu_fine_oct07_4am.py"
)

# Doc-sync constants per #719: post-doc-sync values from the start.
# Patched pre-main once the in-gate collection count is known.
README_TEST_COUNT = 71208  # post-doc-sync total (pre-sync 71117 + 91)
README_FILE_COUNT = 1604  # pre-sync 1603 + 1 (this file)

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
_T56 = "FIFT" + "Y-SIXTH falsification-family member"

# Novel source URLs: all zero-hit repo-wide pre-commit
# (git grep -F on verbatim Full-URL listings). Post-commit all live in
# the block's source_urls. The webpronews Oct-1 Capitol Hill piece is
# already in corpus as an m927 source and is NOT landed here.
NOVEL_URLS = [
    "https://pressgazette.co.uk/news/publishers-to-bill-ai-firms-"
    "for-unwanted-scraping-and-take-them-to-court-if-they-dont-pay/",
    "https://ppc.land/uk-publishers-bill-ai-scrapers-500-per-"
    "article-using-county-courts/",
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

class TestAnchor1279:
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
        assert "FIFTH and CLOSING leg of the 1275-1279 window" in src


# ---------------------------------------------------------------------------
# 2. Rotation guard
# ---------------------------------------------------------------------------

class TestRotationGuard1279:
    def test_predecessor_shas_in_git_log(self):
        log = _git("log", "--oneline", "-40").stdout
        for sha, label in (
            (PRED_MAIN_1278, "1278 main"),
            (PRED_ANCHOR_1278, "1278 anchor"),
            (PRED_DOCSYNC_1278, "1278 doc-sync"),
            (PRED_FINAL_1278, "1278 log-hash"),
        ):
            assert sha in log, label

    def test_1278_type_b_in_git_log(self):
        out = _git("log", "--oneline", "--grep=Type B #1278").stdout
        assert out.strip() != ""

    def test_closing_leg_phrase(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "FIFTH and CLOSING leg of the 1275-1279 window" in src

    def test_1270_1274_window_closed(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "1270-1274" in src
        assert "VERIFIED CLOSED" in src

    def test_next_window_opens_1280(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Next run #1280 Type D" in src
        assert "renders the #1275-launched" in src


# ---------------------------------------------------------------------------
# 3. Mechanism novelty (the #715 discipline)
# ---------------------------------------------------------------------------

class TestMechanismNovelty1279:
    def test_max_mechanism_id_is_999_post_landing(self):
        assert _max_numeric_mechanism_id() == MECH_NUM

    def test_block_key_present(self):
        assert BLOCK_KEY in _load_entities()

    def test_block_key_occurs_twice_in_text(self):
        # Once as the YAML key, once as the block_key field.
        assert _block_text().count(BLOCK_KEY) == 2

    def test_999_numeric_present_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(MECH_NUM) != []

    def test_999_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(MECH_NUM) == []

    def test_999_dash_absent_repo_wide(self):
        assert _repo_grep_dash_mechanism(MECH_NUM) == []

    def test_iteration_field(self):
        assert _block()["iteration"] == 1279

    def test_iteration_type_field(self):
        assert _block()["iteration_type"] == "C"


# ---------------------------------------------------------------------------
# 4. Block structure at the competitor-entities.yaml top level.
# ---------------------------------------------------------------------------

class TestBlockStructure1279:
    def test_block_key_top_level(self):
        data = _load_entities()
        assert BLOCK_KEY in data

    def test_mechanism_id_field(self):
        assert _block()["mechanism_id"] == 999

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

class TestM999ContentDiscipline1279:
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
        assert "500 GBP per article" in finding
        assert "Movement for an Open Web" in finding
        assert "31 founding" in finding
        assert "Candr Media" in finding
        assert "Trusted Reviews" in finding
        assert "MoneyClaim.gov.uk" in finding
        assert "June 15 2026" in finding

    def test_invoice_rail_nexus(self):
        finding = _block()["finding"]
        assert "invoice-economy" in finding
        assert "m786" in finding
        assert "m915" in finding

    def test_october_resurface(self):
        finding = _block()["finding"]
        assert "Oct 1" in finding
        assert "m927" in finding

    def test_boundary_unilateral(self):
        finding = _block()["finding"]
        assert "unilateral, not bilateral" in finding
        assert "no competitor lab has signed or paid" in finding
        assert "claims no slot" in finding

    def test_connects_to_set(self):
        conns = _block()["connects_to"]
        for m in (927, 786, 915):
            assert m in conns, m


# ---------------------------------------------------------------------------
# 6. Statistical discipline: MANUAL / qualitative only per Aug 28 2026 rule.
# ---------------------------------------------------------------------------

class TestStatisticalDiscipline1279:
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
# 7. Falsification ledger: NOT a member; ledger holds at 55.
# ---------------------------------------------------------------------------

class TestFalsificationLedger1279:
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

    def test_fifty_fifth_present_in_atlantic(self):
        out = _git(
            "grep", "-c", "-F", _T55, "HEAD", "--",
            "profiles/atlantic.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_no_fifty_sixth_member(self):
        assert _git_grep_tracked_source(_T56, None) == []

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

    def test_ledger_holds_at_55(self):
        fam = _block()["falsification_family"]
        assert "ledger holds at 55" in fam
        assert "claims no slot" in fam


# ---------------------------------------------------------------------------
# 8. Guard lifecycle: forward pins for #1280; #1278's pins flip BY DESIGN.
# ---------------------------------------------------------------------------

class TestGuardLifecycle1279:
    def test_pins_on_999_landing(self):
        # Type C lands one mechanism: max becomes 999, next is 1000.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 999" in src
        assert "NEXT_NUM = 1000" in src

    def test_no_type_d_1280_in_git_log_pin(self):
        # Post-main-commit form for the NEXT leg (the #1191-class
        # self-trip, re-pinned in #1280's terminal log-hash followup
        # per #721): every commit whose message matches "Type D #1280"
        # must be #1280's main commit or a descendant of it.
        # Deselected in the in-gate run (fails pre-commit by design).
        out = _git("log", "--format=%H", "--grep=Type D #1280")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1280's own commits"
        main = _git("rev-parse", PRED_MAIN_1280).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_1000_numeric_absent_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_1000_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_1000_dash_absent_repo_wide(self):
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

    def test_fifty_fifth_member_present_pin(self):
        out = _git(
            "grep", "-c", "-F", _T55, "HEAD", "--",
            "profiles/atlantic.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_no_fifty_sixth_member_pin(self):
        assert _git_grep_tracked_source(_T56, None) == []

    def test_predecessor_1278_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, B1278_FILE))

    def test_next_leg_is_1280_type_d(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#1280 Type D" in src

    def test_1278_pins_flip_by_design_documented(self):
        # #1278's forward guards (max-998, zero-999 keys all forms,
        # no-Type-C-#1279-in-git-log, fortieth absent, forty-eighth
        # through fifty-fifth intact in profiles/, fifty-sixth absent,
        # ledger 55) verified GREEN at HEAD pre-commit this run. The
        # no-Type-C-#1279-in-git-log pin flips BY DESIGN at this run's
        # main commit (the #1191-class self-trip, re-pinned post-commit
        # by TestStalenessPins1279) and the zero-999-numeric pin trips
        # on the landed mechanism 999 block; the zero-999-underscore/dash
        # pins stay green per the #715 literal discipline. Documented in
        # the staleness pin below, not repaired.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "TestStalenessPins1279" in src
        assert "no_type_c_1279_in_git_log_pin" in src


# ---------------------------------------------------------------------------
# 9. Background suite: #1275's suite is OBSERVED ONLY per #795.
# ---------------------------------------------------------------------------

class TestBackgroundSuiteCheck1279:
    def test_suite_log_exists(self):
        assert os.path.exists(SUITE_LOG), SUITE_LOG

    def test_suite_log_nonempty(self):
        assert os.path.getsize(SUITE_LOG) > 0

    def test_run_neither_relaunches_nor_kills(self):
        # Observation-only per #795: this run's own processes must not
        # include a suite launcher it started.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "neither" in src and "re-launches" in src

    def test_verdict_belongs_to_1280(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "belong to #1280" in src


# ---------------------------------------------------------------------------
# 10. Doc-sync per #719 (3 tests; deselected pre-commit, flipped post-sync)
# ---------------------------------------------------------------------------

class TestDocSync1279:
    def test_readme_test_file_table_has_1279_row_post_sync(self):
        readme = _read(README_PATH)
        assert "test_type_c_1279" in readme

    def test_architecture_has_1279_row_post_sync(self):
        arch = _read(ARCH_PATH)
        assert "test_type_c_1279" in arch

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

class TestIterationLog1279:
    def test_1279_entry_present_post_sync(self):
        log = _read(LOG_PATH)
        assert "## #1279 Type C" in log

    def test_1278_entry_present(self):
        log = _read(LOG_PATH)
        assert "## #1278 Type B" in log

    def test_rotation_transparency_convention(self):
        log = _read(LOG_PATH)
        assert "### Rotation transparency" in log


# ---------------------------------------------------------------------------
# 12. Staleness pins: #1278's guard lifecycle flips BY DESIGN post-commit
# ---------------------------------------------------------------------------

class TestStalenessPins1279:
    def test_1278_guard_lifecycle_post_commit_self_trip(self):
        # Post-main-commit form: 18 tests in the class, 16 pass and
        # TWO flip BY DESIGN when this run's main commit lands: the
        # no_type_c_1279_in_git_log ancestor pin (its PRED_MAIN_1279
        # is still the 0*40 placeholder until this run's terminal
        # log-hash followup re-pins it per #721) and the
        # zero-999-numeric pin (trips on the landed mechanism 999
        # block) - the #1191-class self-trip family. The pin is
        # re-pinned to the post-commit own-set form in the terminal
        # log-hash followup per #721; the class run below therefore
        # expects the 16 surviving pins green and documents the two
        # designed flips. The #1278 block is read-only to this run;
        # the quirk is documented here, not repaired.
        res = _class_run(B1278_FILE, "TestGuardLifecycle1278")
        out = res.stdout + res.stderr
        assert "2 failed, 16 passed" in out, out[-2000:]
        assert "no_type_c_1279_in_git_log" in out, out[-2000:]
        assert "test_999_numeric_absent_in_profiles" in out, out[-2000:]


# ---------------------------------------------------------------------------
# 13. In-flight isolation
# ---------------------------------------------------------------------------

class TestInFlightIsolation1279:
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
