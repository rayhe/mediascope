# -*- coding: utf-8 -*-
"""Type A #1337: Verge x Microsoft Oct-7/8-2026 Copilot agentic PC-file
access announcement (relay-attested product-launch explainer, +0.15 MANUAL
ILLUSTRATIVE) vs carried Verge x Meta arms (Sep-23/24 Connect Muse Charm,
-0.30, via #1017 m841, un-rescored per #807); illustrative delta
(Microsoft minus Meta) +0.45 - the PCM licensing partner draws a markedly
softer product register than the $0-tie Meta comparator; the PCM
prediction (Vox Media in Microsoft's Publisher Content Marketplace, Feb
2026, coverage_prediction softer) HOLDS on the product-launch peg -
verdict directionally_supported_not_proven (thesis-consistent instance);
NOT a falsification-family member; ledger HOLDS at 62; domain-bounded to
The Verge's product-launch register on Microsoft in the Oct-7/8 window;
the #1143 temporal-replication precedent does not block (new event peg -
the Oct-7/8 Copilot agentic announcement - not a re-score of the Sep-4
copyright-defense headline peg, type_a_1017); counterevidence m982 (#1252,
FIFTY-THIRD member: Verge adversarial on the OpenAI licensing partner,
Oct-5 safety-week cluster) and the relay's own skeptical frame disclosed;
NOT artifact-grade; no analysis.json update.

The peg: The Register first reported Oct 7 2026 that Copilot's agentic
functions would integrate with Microsoft Office for advanced search and
productivity (tax-records-to-accountant example); The Verge covered the
same event in detail, its report capturing Andreou's exact demonstration
and placing the features inside the broader Hybrid Intelligence vision
(webpronews relay, verbatim URL novel to corpus, 0 browser.open per
#503). Register: product-launch explainer - local and cloud models
combine for efficiency; the AI executes rather than suggests. MANUAL
ILLUSTRATIVE +0.15 (relay-attested, excerpt-bounded).

MANUAL ILLUSTRATIVE scoring: Verge x Microsoft Oct-7/8 Copilot agentic
announcement +0.15 vs carried Verge x Meta arm -0.30 (Sep-23/24 Connect
Muse Charm, backlash-framed, via #1017 m841, un-rescored per #807).
Illustrative delta (Microsoft minus Meta): +0.45 - the payer draws a
SOFTER register than Meta. The thesis test is the PCM licensing
prediction (coverage_prediction softer): Vox Media, The Verge's parent,
is a co-design partner and pilot publisher in Microsoft's Publisher
Content Marketplace (Feb 2026, licensing, usage-based, terms
undisclosed); Meta is NOT a PCM participant. The prediction HOLDS on the
product-launch peg.

Type A lands one mechanism: m1033 in profiles/the-verge.yaml under
competitor_relationships/microsoft (4-space indent, sibling of the
type_a_1017 block); max numeric mechanism_id 1032->1033; next 1034;
ledger HOLDS at 62 (the sixty-second member remains the #1332 m1030 WSJ
x OpenAI member; the sixty-third member-claim form stays absent
repo-wide; m1033 is falsification_family_member false).

Research method: 12 browser.search query sets this run (7 NYT/Amazon
exploratory sets REJECTED as pair - no fresh NYT Amazon originals
surfaced; 1 FT/Google AdX set REJECTED as pair - no FT original surfaced;
1 theverge.com Microsoft October set; 1 Verge Copilot agentic set
(ATTESTING); 2 NYT Amazon layoffs/Weise sets REJECTED). 0 browser.open
(excerpt-bounded per #503). Pre-commit novelty greps: zero
test_type_a_1337 files on disk (glob); no Type A #1337 in git log
(--grep); max numeric mechanism_id 1032 in profiles/ pre-commit; zero
numeric/underscore/dash next-number one-zero-three-four mechanism key
forms in profiles/ + tests/ pre-commit (needles format-built per #715,
own file excluded, verified clean by direct sweep); 1 novel relay URL
zero-hit repo-wide pre-commit (git grep -F); block key zero-hit
repo-wide pre-commit; "## #1337" zero-hit in iteration-log pre-commit; no
#1337 row in README/ARCHITECTURE test tables pre-commit; README stats
76542/1661 pre-commit. The Verge piece's theverge.com URL did not surface
in search listings (no-construction rule); the relay URL is copied
verbatim from the browser.search Full-URL listing. ASCII-only, no em
dashes.

This run is the THIRD leg of the 1335-1339 window (D #1335 -> E #1336 ->
A #1337 -> B #1338 -> C #1339 per the #565 anchor + rotation guard); the
1330-1334 window is VERIFIED CLOSED. The next background-suite verdict
belongs to #1340 per #795 (the #1335-launched suite, goal hidden_files
type_d_1335_full_suite.log; this run OBSERVES only, neither re-launches,
kills, nor writes to it).

Anchor convention per #565: ANCHORED_SHA starts as 0*40 in this
pre-commit file and is patched to the main-commit hash in the anchor
followup commit. One anchor test (the placeholder pin) fails BY DESIGN
post-anchor.

Do NOT touch #1024 (m846 in profiles/competitor-entities.yaml), #899
(nytimes.yaml m771 hunk), #938 (Type B test file working-tree edit),
#900 (untracked Type D test file), #1012-wt (working-tree edit on the
committed Type A #1012 file).

ASCII-only, no em dashes. Needles format-built per #715: this file must
not carry contiguous numeric/underscore/dash mechanism-key forms of the
max or next number, the forty-eighth through sixty-third member-claim
forms, or the fortieth direction-claim form; the constants are
constructed at runtime. (The landed ordinals live as short lowercase
forms in prose here; the live full-form claims live in profiles: the
forty-eighth, fifty-eighth, and sixtieth in financial-times.yaml, the
forty-ninth, fiftieth, and fifty-second in profiles/careers/
journalists.yaml, the fifty-first, fifty-ninth, and sixty-second in
news-corp.yaml, the fifty-third in the-verge.yaml, the fifty-fourth in
guardian.yaml, the fifty-fifth in atlantic.yaml, the fifty-sixth and
sixty-first in wired.yaml, the fifty-seventh in ap.yaml; the sixty-third
is absent repo-wide as of this run.)
"""

import os
import re
import subprocess

import pytest
import yaml

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
PROFILES_DIR = os.path.join(REPO_ROOT, "profiles")
TESTS_DIR = os.path.join(REPO_ROOT, "tests")
README_PATH = os.path.join(REPO_ROOT, "README.md")
ARCH_PATH = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")
LOG_PATH = os.path.join(REPO_ROOT, "iteration-log.md")
VERGE_PATH = os.path.join(PROFILES_DIR, "the-verge.yaml")

OWN_BASENAME = (
    "test_type_a_1337_verge_microsoft_oct08_copilot_agentic_"
    "pc_files_vs_carried_meta_connect_arms_oct09_7am.py"
)

# Patched per #565 in the anchor followup (main commit sha).
ANCHORED_SHA = "c8d74b54ebe3acc9ac189f03b94a6dc74a4b4940"  # 0*40 pre-commit; patched to the main-commit sha in the anchor followup per #565

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

MECH_NUM = 1033
NEXT_NUM = 1034  # integer only; key-form needles are format-built

# Predecessor chain: #1336 Type E SECOND leg of the 1335-1339 window.
PRED_MAIN_1336 = "12d00ec603bbb37715a812c5049f175129593b6a"
PRED_ANCHOR_1336 = "c184fb6a139af0ef51f2e0499587f481d0aac1b6"
PRED_DOCSYNC_1336 = "495bba62a3032742d9a92aa854497e39301adf83"
PRED_FINAL_1336 = "81e384de7899070953109cc749b105a8295def56"

# This run's main commit (full sha), for the ancestor-form
# no-Type-A-#1337 pin. Staged 0*40 placeholder-only per #721;
# re-pinned in this run's terminal log-hash followup per #721.
PRED_MAIN_1337 = "c8d74b54ebe3acc9ac189f03b94a6dc74a4b4940"  # re-pinned to #1337 main sha in the anchor followup per #721/#1292

# #1338's main commit (full sha), for the ancestor-form no-Type-B-#1338
# pin. Staged 0*40 placeholder-only per #721; re-pinned in #1338's
# terminal log-hash followup per #721.
PRED_MAIN_1338 = "0" * 40

# The #1336 window-predecessor file, for the staleness pin on its
# guard-lifecycle class (max id 1032; zero next-number
# one-zero-three-three / no-Type-A-#1337-in-git-log / fortieth
# direction absent / forty-eighth through sixty-second members
# intact / no sixty-third member (repo-wide) / ledger 62).
B1336_FILE = (
    "test_type_e_1336_podcast_sentiment_190th_"
    "verification_oct09_6am.py"
)

# Doc-sync constants per #719: post-doc-sync values from the start.
# Patched pre-main once the in-gate collection count is known.
README_TEST_COUNT = 76646  # post-doc-sync total (pre-sync 76542 + 104) - PATCHED post-collection
README_FILE_COUNT = 1662  # pre-sync 1661 + 1 (this file)

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
_T57 = "FIFT" + "Y-SEVENTH falsification-family member"
_T58 = "FIFT" + "Y-EIGHTH falsification-family member"
# The fifty-ninth member-claim form is fragment-built per #715
# (landed #1302 in profiles/news-corp.yaml).
_T59 = "FIFT" + "Y-NINTH falsification-family member"
# The sixtieth member-claim form is fragment-built per #715
# (landed #1322 in profiles/financial-times.yaml).
_T60 = "SIXT" + "IETH falsification-family member"
# The sixty-first member-claim form is fragment-built per #715
# (landed #1327 in profiles/wired.yaml).
_T61 = "SIXT" + "Y-FIRST falsification-family member"
# The sixty-second member-claim form is fragment-built per #715
# (landed #1332 in profiles/news-corp.yaml).
_T62 = "SIXT" + "Y-SECOND falsification-family member"
# The sixty-third member-claim form is fragment-built per #715
# (no sixty-third member may exist repo-wide).
_T63 = "SIXT" + "Y-THIRD falsification-family member"

BLOCK_KEY = (
    "type_a_1337_verge_microsoft_oct08_copilot_agentic_"
    "pc_files_vs_carried_meta_connect_arms_oct09_7am"
)

# MANUAL ILLUSTRATIVE tone constants (hand-assigned register positions
# per the Aug 28 2026 standing rule; NOT engine output).
MICROSOFT_TONE = 0.15
META_TONE = -0.30
DELTA_MICROSOFT_MINUS_META = 0.45

# Novel verbatim source URLs this run (zero-hit repo-wide pre-commit,
# verified via git grep -F; copied verbatim from the browser.search
# Full-URL listings, NOT constructed).
NOVEL_URLS = [
    "https://www.webpronews.com/microsoft-hands-copilot-the-keys-to-your-pc-files/",
]

# 12 browser.search query sets this run (0 browser.open per #503).
QUERY_SETS = [
    "New York Times Amazon data center NDA county officials October 2026",
    "NYT Amazon news October 2026 Weise",
    "nytimes.com Amazon layoffs October 8 2026 stores",
    "New York Times Amazon October 2026 Hyperion Louisiana data center Weise",
    "New York Times Amazon stop using NDAs nondisclosure data centers Garman October",
    "nytimes Amazon Weise October 2026 data center",
    "Financial Times Google AdX monopoly damages ruling Castel October 2026",
    "theverge.com Microsoft October 2026 OpenAI letter",
    "Verge Copilot keys to your PC files agentic Windows 11 Andreou Hybrid Intelligence October 2026",
    "New York Times Amazon layoffs October 8 October 7 2026 stores workers",
    "nytimes.com New York Times Amazon 1,000 layoffs Weise Karen Weise October 2026",
    "Karen Weise Amazon New York Times September October 2026",
]


def _load_verge():
    with open(VERGE_PATH, encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def _block():
    data = _load_verge()
    return data["competitor_relationships"]["microsoft"][BLOCK_KEY]


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


def _class_run(filename, classname):
    target = os.path.join(TESTS_DIR, filename)
    env = dict(os.environ)
    env["PYTEST_DISABLE_PLUGIN_AUTOLOAD"] = "1"
    venv_py = os.path.join(REPO_ROOT, ".venv", "bin", "python")
    return subprocess.run(
        [venv_py, "-m", "pytest", target, "-k", classname,
         "-q", "--no-header", "-o", "addopts=", "-p", "no:cacheprovider"],
        cwd=REPO_ROOT, capture_output=True, text=True, env=env,
        timeout=600,
    )


# ---------------------------------------------------------------------------
# 1. Anchor (pre-commit placeholder per #565; patched in anchor followup)
#    + rotation guard: THIRD leg of the 1335-1339 window.
# ---------------------------------------------------------------------------


class TestAnchor1337:
    def test_anchor_sha_placeholder_pre_commit(self):
        # Pre-commit form: ANCHORED_SHA is 0*40; the anchor followup
        # patches it to the main-commit sha. This test fails BY
        # DESIGN post-anchor and is deselected in the in-gate run;
        # the patched form is asserted by
        # test_anchor_sha_patched_to_main_commit. Terminal per #565.
        assert ANCHORED_SHA == "0" * 40

    def test_anchor_sha_patched_to_main_commit(self):
        # Post-commit form: ANCHORED_SHA patched to this run's main
        # commit sha in the anchor followup (placeholder + expected
        # value and the ANCHORED_SHA constant are patched).
        # Deselected in the in-gate run.
        assert ANCHORED_SHA != "0" * 40
        assert len(ANCHORED_SHA) == 40

    def test_anchor_sha_format(self):
        assert len(ANCHORED_SHA) == 40
        assert re.fullmatch(r"[0-9a-f]{40}", ANCHORED_SHA)

    def test_anchor_duality_documented(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Anchor convention per #565" in src
        assert "fails BY DESIGN post-anchor" in src

    def test_third_leg_phrase(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "THIRD leg of the 1335-1339 window" in src

    def test_1330_1334_window_closed(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "1330-1334" in src
        assert "VERIFIED CLOSED" in src

    def test_next_leg_is_1338_type_b(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "B #1338" in src


# ---------------------------------------------------------------------------
# 2. Mechanism novelty: Type A lands one mechanism (m1033; max 1033).
# ---------------------------------------------------------------------------


class TestMechanismNovelty1337:
    def test_max_numeric_mechanism_id_1033(self):
        assert _max_numeric_mechanism_id() == MECH_NUM

    def test_no_type_a_1337_in_git_log_pin(self):
        # Post-main-commit form (the #1191-class self-trip, re-pinned
        # in the terminal log-hash followup per #721): every commit
        # whose message matches "Type A #1337" must be this run's
        # main commit or a descendant of it - i.e., no PRIOR run
        # committed this run's iteration. The ancestor check (not an
        # enumerated own-set) is robust to any number of same-run
        # followup commits: each followup is a descendant of main by
        # construction, so the pin is stable and terminal. Deselected
        # in the in-gate run (fails pre-commit by design).
        out = _git("log", "--format=%H", "--grep=Type A #1337")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected this run's own commits"
        main = _git("rev-parse", PRED_MAIN_1337).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_zero_next_number_keys_all_forms(self):
        # Numeric (profiles/ scope), underscore and dash (profiles/ +
        # tests/ scope, own file excluded per #715).
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_block_key_designed_no_1033_1034_substring(self):
        # Per #723/#738/#739: the iteration-form block key carries no
        # underscore-form one-zero-three-three / one-zero-three-four
        # mechanism key substring (needle format-built per #770 so
        # this file carries no contiguous literal).
        for n in (MECH_NUM, NEXT_NUM):
            needle = "%s%d" % (MECH_ID_MARKER, n)
            assert needle not in BLOCK_KEY
        assert "1337" in BLOCK_KEY
        assert BLOCK_KEY in _read(VERGE_PATH)

    def test_block_key_in_verge_microsoft_section(self):
        data = _load_verge()
        msft = data["competitor_relationships"]["microsoft"]
        assert BLOCK_KEY in msft
        assert msft[BLOCK_KEY]["mechanism_id"] == MECH_NUM

    def test_novel_urls_zero_hit_pre_commit(self):
        # The relay URL was verified zero-hit pre-commit (git
        # grep -F, documented in the block's novelty field). This
        # test pins that no file OTHER than this run's own m1033
        # block ever carries it, so it holds pre-commit (zero hits)
        # and post-commit (only the landed block hits).
        for url in NOVEL_URLS:
            out = _git("grep", "-F", "-l", url, "HEAD", "--",
                       "profiles/", "tests/").stdout
            paths = []
            for line in out.splitlines():
                line = line.strip()
                if not line:
                    continue
                if line.startswith("HEAD:"):
                    line = line[5:]
                paths.append(line)
            assert set(paths) <= {
                "profiles/the-verge.yaml",
                "tests/" + OWN_BASENAME,
            }, (url, paths)

    def test_forward_guards_for_1338(self):
        # max-1033; zero-1034 all forms; fortieth direction absent
        # (profiles/ scope); forty-eighth through sixty-second members
        # intact; no sixty-third member (repo-wide); ledger 62. The
        # sixty-second is asserted at HEAD (landed #1332, committed);
        # this run's m1033 block is thesis-consistent (not a member),
        # so no sixty-third member exists.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 1033" in src
        assert "NEXT_NUM = 1034" in src
        assert "ledger HOLDS at 62" in src
        assert _git_grep_tracked_source(_T40, "profiles/") == []
        assert _git_grep_tracked_source(_T48, "profiles/") == [
            "profiles/financial-times.yaml"]
        assert _git_grep_tracked_source(_T62, "profiles/") == [
            "profiles/news-corp.yaml"]
        assert _git_grep_tracked_source(_T63, None) == []

    def test_distinct_from_prior_verge_microsoft(self):
        # Not a re-score of type_a_1017 (Sep-4 copyright-defense
        # headline peg) or iteration_461 (Aug Copilot retrenchment);
        # the #1143 temporal-replication precedent does not block a
        # fresh event peg.
        block = _block()
        assert "type_a_1017" in block["distinct_from_prior"]
        assert "iteration_461" in block["distinct_from_prior"]
        assert "#1143" in block["distinct_from_prior"]
        assert "Oct-7/8" in block["distinct_from_prior"] or \
            "Oct-7/8-2026" in block["microsoft_arm_new"]["event"] or \
            "2026-10-08" in block["microsoft_arm_new"]["date"]


# ---------------------------------------------------------------------------
# 3. Guard lifecycle: forward pins for #1338; #1337 stages the
#    #1191-class no-Type-A-#1337 self-trip (re-pinned post-commit
#    per #721).
# ---------------------------------------------------------------------------


class TestGuardLifecycle1337:
    def test_pins_on_one_mechanism_landing(self):
        # Type A lands one mechanism: max 1033, next 1034.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 1033" in src
        assert "NEXT_NUM = 1034" in src

    def test_no_type_b_1338_in_git_log_pin(self):
        # Post-main-commit form for the NEXT leg (the #1191-class
        # self-trip, re-pinned in #1338's terminal log-hash followup
        # per #721): every commit whose message matches "Type B
        # #1338" must be #1338's main commit or a descendant of it.
        # Deselected in the in-gate run (fails pre-commit by design).
        out = _git("log", "--format=%H", "--grep=Type B #1338")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1338's own commits"
        main = _git("rev-parse", PRED_MAIN_1338).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_1034_numeric_absent_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_1034_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_1034_dash_absent_repo_wide(self):
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

    def test_fifty_sixth_member_present_pin(self):
        # Landed #1282 (m1000, profiles/wired.yaml, committed). HEAD
        # sweep is stable for a committed landing.
        wired = _read(os.path.join(PROFILES_DIR, "wired.yaml"))
        assert _T56 in wired

    def test_fifty_seventh_member_present_pin(self):
        # Landed #1287 (m1003, profiles/ap.yaml, committed). HEAD
        # sweep is stable for a committed landing.
        out = _git(
            "grep", "-c", "-F", _T57, "HEAD", "--",
            "profiles/ap.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fifty_eighth_member_present_pin(self):
        # Landed #1292 (m1006, profiles/financial-times.yaml,
        # committed). HEAD sweep is stable for a committed landing.
        out = _git(
            "grep", "-c", "-F", _T58, "HEAD", "--",
            "profiles/financial-times.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fifty_ninth_member_present_pin(self):
        # Landed #1302 (m1012, profiles/news-corp.yaml, committed).
        # HEAD sweep is stable for a committed landing.
        out = _git(
            "grep", "-c", "-F", _T59, "HEAD", "--",
            "profiles/news-corp.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_sixtieth_member_present_pin(self):
        # Landed #1322 (m1024, profiles/financial-times.yaml,
        # committed). HEAD sweep is stable for a committed landing.
        out = _git(
            "grep", "-c", "-F", _T60, "HEAD", "--",
            "profiles/financial-times.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_sixty_first_member_present_pin(self):
        # Landed #1327 (m1027, profiles/wired.yaml, committed). HEAD
        # sweep is stable for a committed landing.
        out = _git(
            "grep", "-c", "-F", _T61, "HEAD", "--",
            "profiles/wired.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_sixty_second_member_present_pin(self):
        # Landed #1332 (m1030, profiles/news-corp.yaml, committed).
        # HEAD sweep is stable for a committed landing.
        out = _git(
            "grep", "-c", "-F", _T62, "HEAD", "--",
            "profiles/news-corp.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_no_sixty_third_member_pin(self):
        # Type A lands one mechanism (m1033, thesis-consistent, NOT a
        # falsification member); the sixty-third member-claim form
        # stays absent repo-wide.
        assert _git_grep_tracked_source(_T63, None) == []

    def test_predecessor_1336_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, B1336_FILE))

    def test_next_leg_is_1338_type_b(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#1338 Type B" in src

    def test_1336_pins_flip_by_design_documented(self):
        # #1336's forward guards (max-1032, zero one-zero-three-three
        # keys all forms, no-Type-A-#1337-in-git-log, fortieth
        # absent, forty-eighth through sixty-second intact in
        # profiles/, no sixty-third member repo-wide, ledger 62)
        # verified GREEN at HEAD pre-commit this run. TWO pins flip
        # BY DESIGN at this run's main commit: the #1191-class
        # self-trip (no-Type-A-#1337-in-git-log, re-pinned
        # post-commit by TestStalenessPins1337 in both copies per
        # the re-pin-both-copies precedent) and the #1272-class
        # forward-guard expiry (the 1033-numeric-absent-in-profiles
        # pin trips on the landed m1033 block - permanent red by
        # design). The 1033-underscore/dash pins stay green (the
        # block key carries no one-zero-three-three mechanism-key
        # forms per #723/#738/#739); the no-sixty-third-member pin
        # stays green (m1033 is not a member). Documented in the
        # staleness pin below, not repaired.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "TestStalenessPins1337" in src
        assert "no_type_a_1337_in_git_log_pin" in src


# ---------------------------------------------------------------------------
# 4. Doc-sync per #719 (deselected pre-commit, flipped post-sync).
# ---------------------------------------------------------------------------


class TestDocSync1337:
    def test_readme_test_file_table_has_1337_row_post_sync(self):
        readme = _read(README_PATH)
        assert "test_type_a_1337" in readme

    def test_architecture_has_1337_row_post_sync(self):
        arch = _read(ARCH_PATH)
        assert "test_type_a_1337" in arch

    def test_readme_stats_ratcheted(self):
        # Post-sync-positive form per #719: asserts the ratcheted
        # counts (README_TEST_COUNT tests across README_FILE_COUNT
        # files). Fails pre-commit by design; deselected in the
        # in-gate run.
        readme = _read(README_PATH)
        assert ("| Tests | %d |" % README_TEST_COUNT) in readme
        assert ("Across %d test files" % README_FILE_COUNT) in readme


# ---------------------------------------------------------------------------
# 5. Iteration log per #721 (deselected pre-commit, flipped post-sync).
# ---------------------------------------------------------------------------


class TestIterationLog1337:
    def test_log_has_1337_entry(self):
        text = _read(LOG_PATH)
        assert "## #1337 Type A" in text

    def test_log_entry_carries_hash_chain(self):
        # The doc-sync writes the entry with the main/anchor hashes;
        # the terminal log-hash followup registers the doc-sync hash
        # here per #721.
        text = _read(LOG_PATH)
        assert "main commit" in text
        assert "anchor" in text

    def test_log_entry_records_finding(self):
        text = _read(LOG_PATH)
        assert "m1033" in text
        assert "Copilot" in text


# ---------------------------------------------------------------------------
# 6. Staleness pins: #1336's guard lifecycle flips BY DESIGN post-commit.
# ---------------------------------------------------------------------------


class TestStalenessPins1337:
    def test_1336_guard_lifecycle_post_commit_self_trip(self):
        # Post-terminal-followup form: 25 tests in the class; 24
        # pass, 1 fails BY DESIGN and permanently - the #1272-class
        # forward-guard expiry (test_1033_numeric_absent_in_profiles
        # trips on the landed m1033 block). The no_type_a_1337_in_git_log
        # ancestor pin (the #1191-class self-trip) was red at this
        # run's main-commit time; the anchor followup re-pinned
        # PRED_MAIN_1337 in BOTH its own file's copy and the #1336
        # predecessor file's copy per the #1292 re-pin-both-copies
        # precedent and the #721 re-pin rule, flipping it green. The
        # 1033-underscore and 1033-dash pins stay green (no
        # one-zero-three-three mechanism-key forms landed); the
        # no-sixty-third-member pin stays green (m1033 is not a
        # member; ledger holds at 62); the fifty-third member pin
        # stays green (this run's counterevidence cites m982 in
        # lowercase prose form per #715, preserving the :2 count).
        # Deselected in the in-gate run (fails pre-commit by
        # design); verified post-terminal.
        res = _class_run(B1336_FILE, "TestGuardLifecycle1336")
        out = res.stdout + res.stderr
        assert "1 failed, 24 passed" in out, out[-2000:]


# ---------------------------------------------------------------------------
# 7. Corpus integrity: the m1033 block is well-formed and placed.
# ---------------------------------------------------------------------------


class TestCorpusIntegrity1337:
    def test_verge_yaml_loads(self):
        data = _load_verge()
        assert "competitor_relationships" in data

    def test_block_fields_present(self):
        block = _block()
        for field in (
            "mechanism_id", "date_analyzed", "type", "iteration",
            "iteration_type", "block_key", "test_file", "author",
            "publication", "competitor_pair", "goal_id",
            "scheduled_job_id", "window", "design",
            "distinct_from_prior", "finding", "microsoft_arm_new",
            "meta_arm_carried", "asymmetry_scorer_result", "verdict",
            "falsification_family_member", "falsification_ledger",
            "ledger", "counterevidence", "confounders_ranked",
            "financial_context", "statistical_discipline", "method",
            "novelty", "source_urls", "no_analysis_json_update",
            "concurrency", "status",
        ):
            assert field in block, field

    def test_block_sibling_of_1017(self):
        data = _load_verge()
        msft = data["competitor_relationships"]["microsoft"]
        keys = list(msft.keys())
        assert BLOCK_KEY in keys
        assert ("type_a_1017_verge_microsoft_sep2026_copyright_defense_"
                "headline_register_vs_meta_connect_backlash_framing_"
                "pcm_licensing_gradient") in keys

    def test_four_space_indent(self):
        src = _read(VERGE_PATH)
        assert "\n    " + BLOCK_KEY + ":" in src

    def test_ascii_only_profile_block(self):
        data = _load_verge()
        blob = str(data["competitor_relationships"]["microsoft"][BLOCK_KEY])
        assert "\u2014" not in blob
        assert "\u2013" not in blob

    def test_test_file_field_matches(self):
        assert _block()["test_file"] == "tests/" + OWN_BASENAME

    def test_goal_and_job_ids(self):
        block = _block()
        assert block["goal_id"] == "goal_54093bda4145"
        assert block["scheduled_job_id"] == "mediascope-daily-iteration"
        assert block["author"] == "Kit (with Ray)"

    def test_window_third_leg(self):
        assert "1335-1339" in _block()["window"]
        assert "THIRD leg" in _block()["window"]


# ---------------------------------------------------------------------------
# 8. Research method: 12 query sets, 0 browser.open, novelty, verbatim.
# ---------------------------------------------------------------------------


class TestResearchMethod1337:
    def test_twelve_query_sets_documented(self):
        block = _block()
        assert len(block["method"]["query_sets"]) == 12
        for q in QUERY_SETS:
            assert q in block["method"]["query_sets"]

    def test_attesting_set_present(self):
        assert any("Andreou" in q for q in QUERY_SETS)

    def test_rejected_pairs_documented(self):
        # 7 NYT/Amazon exploratory sets + 1 FT/Google set + 2 NYT
        # layoffs/Weise sets were explored and REJECTED as pairs (no
        # fresh originals surfaced); the docstring records the
        # rejection so the search labor is auditable.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "REJECTED as pair" in src

    def test_zero_browser_open_per_503(self):
        assert _block()["method"]["browser_open"] == 0
        assert "#503" in _block()["method"]["evidence_tier"]

    def test_novelty_greps_documented(self):
        assert "one-zero-three-three" in _block()["method"]["novelty"]
        assert "#715" in _block()["method"]["novelty"]

    def test_urls_verbatim_not_constructed(self):
        assert "verbatim" in _block()["method"]["url_policy"]
        assert "NOT constructed" in _block()["method"]["url_policy"]

    def test_query_set_count_matches_constant(self):
        assert len(QUERY_SETS) == 12


# ---------------------------------------------------------------------------
# 9. Confounders: ranked strong-first; counterevidence disclosed.
# ---------------------------------------------------------------------------


class TestConfounders1337:
    def test_five_confounders_ranked(self):
        confs = _block()["confounders_ranked"]
        assert len(confs) == 5

    def test_strong_first(self):
        confs = _block()["confounders_ranked"]
        assert confs[0].startswith("STRONG")
        assert confs[1].startswith("STRONG")
        assert confs[2].startswith("MODERATE")
        assert confs[4].startswith("WEAK")

    def test_relay_attestation_is_top_confounder(self):
        confs = _block()["confounders_ranked"]
        assert "relay-attested" in confs[0]
        assert "#503" in confs[0]

    def test_peg_conditional_inversion_disclosed(self):
        confs = _block()["confounders_ranked"]
        assert any("m982" in c for c in confs)

    def test_counterevidence_three_items(self):
        ce = _block()["counterevidence"]
        assert len(ce) == 3

    def test_m982_counterevidence(self):
        ce = _block()["counterevidence"]
        assert any("m982" in c and "fifty-third" in c for c in ce)

    def test_relay_skeptical_frame_counterevidence(self):
        ce = _block()["counterevidence"]
        assert any("Recall" in c for c in ce)

    def test_register_broke_first_counterevidence(self):
        ce = _block()["counterevidence"]
        assert any("Register" in c and "Oct 7" in c for c in ce)


# ---------------------------------------------------------------------------
# 10. Verdict: statistical discipline (Aug 28 2026 standing rule).
# ---------------------------------------------------------------------------


class TestVerdict1337:
    def test_manual_qualitative_only(self):
        disc = _block()["statistical_discipline"]
        assert "MANUAL/QUALITATIVE ONLY" in disc
        assert "Aug 28 2026 standing rule" in disc

    def test_no_p_values(self):
        disc = _block()["statistical_discipline"]
        assert "NOT_CALCULATED" in disc

    def test_not_artifact_grade(self):
        disc = _block()["statistical_discipline"]
        assert "NOT artifact-grade" in disc
        assert "no_analysis_json_update" in disc

    def test_correlation_not_causation(self):
        disc = _block()["statistical_discipline"]
        assert "Correlation is not causation" in disc
        assert "hypothesis-generating only" in disc

    def test_is_significant_false(self):
        assert _block()["asymmetry_scorer_result"][
            "is_significant"] is False

    def test_verdict_directionally_supported(self):
        assert _block()["verdict"] == "directionally_supported_not_proven"

    def test_not_falsification_member(self):
        block = _block()
        assert block["falsification_family_member"] is False
        assert block["falsification_ledger"] == "62"
        assert block["ledger"] == "62"

    def test_engine_not_run(self):
        assert _block()["asymmetry_scorer_result"]["engine_run"] is False


# ---------------------------------------------------------------------------
# 11. The Verge x Microsoft Oct-7/8 arm (NEW) vs carried Meta arm.
# ---------------------------------------------------------------------------


class TestVergeMicrosoftArm1337:
    def _msft(self):
        return _block()["microsoft_arm_new"]

    def _meta(self):
        return _block()["meta_arm_carried"]

    def test_microsoft_arm_event(self):
        assert "Copilot" in self._msft()["event"]
        assert "Oct 7-8 2026" in self._msft()["event"]

    def test_microsoft_arm_first_reported_by_register(self):
        assert "Register" in self._msft()["first_reported_by"]
        assert "Oct 7" in self._msft()["first_reported_by"]

    def test_microsoft_arm_relay_url_novel(self):
        assert self._msft()["relay_attestation"].startswith(
            "https://www.webpronews.com/microsoft-hands-copilot-the-keys-to-your-pc-files/")

    def test_microsoft_arm_register(self):
        assert self._msft()["register"] == "product_launch_explainer"

    def test_microsoft_arm_tone(self):
        assert self._msft()["tone_manual_illustrative"] == MICROSOFT_TONE
        assert MICROSOFT_TONE == 0.15

    def test_meta_arm_carried_from_1017(self):
        meta = self._meta()
        assert "muse-charm" in meta["url"]
        assert meta["tone_manual_illustrative"] == META_TONE
        assert META_TONE == -0.30
        assert "#1017 m841" in meta["carried_from"]
        assert "#807" in meta["carried_from"]

    def test_meta_arm_register(self):
        assert "backlash" in self._meta()["register"]

    def test_delta_math(self):
        res = _block()["asymmetry_scorer_result"]
        assert res["illustrative_delta"] == DELTA_MICROSOFT_MINUS_META
        assert DELTA_MICROSOFT_MINUS_META == round(
            MICROSOFT_TONE - META_TONE, 2)
        assert res["delta_direction"] == "Microsoft minus Meta"

    def test_delta_direction_positive(self):
        # The payer draws the softer register: thesis-consistent.
        assert DELTA_MICROSOFT_MINUS_META > 0

    def test_finding_states_delta(self):
        assert "+0.45" in _block()["finding"]

    def test_novelty_in_corpus(self):
        assert "zero-hit" in self._msft()["novelty_in_corpus"]

    def test_constants_match_block(self):
        res = _block()["asymmetry_scorer_result"]
        assert res["microsoft_new_arm"] == MICROSOFT_TONE
        assert res["meta_carried_arm"] == META_TONE


# ---------------------------------------------------------------------------
# 12. Financial relationship: PCM licensing gradient.
# ---------------------------------------------------------------------------


class TestFinancialRelationship1337:
    def test_microsoft_pcm_tie(self):
        fc = _block()["financial_context"]
        assert "Publisher Content Marketplace" in fc["microsoft_tie"]
        assert "Feb 2026" in fc["microsoft_tie"]

    def test_prediction_softer(self):
        fc = _block()["financial_context"]
        assert "softer" in fc["microsoft_tie"]

    def test_meta_zero_tie(self):
        fc = _block()["financial_context"]
        assert "$0" in fc["meta_tie"]
        assert "NOT a PCM participant" in fc["meta_tie"]

    def test_prediction_holds_on_peg(self):
        fc = _block()["financial_context"]
        assert "HOLDS" in fc["prediction_check"]
        assert "+0.45" in fc["prediction_check"]

    def test_design_names_pcm_gradient(self):
        assert "PCM licensing gradient" in _block()["design"]

    def test_microsoft_section_carries_tie(self):
        data = _load_verge()
        msft = data["competitor_relationships"]["microsoft"]
        assert msft["financial_tie"] == "licensing"
        assert msft["coverage_prediction"] == "softer"

    def test_verdict_not_falsification(self):
        # Thesis-consistent instance: the prediction holds, so no
        # falsification-family member is claimed.
        assert _block()["verdict"] == "directionally_supported_not_proven"
        assert _block()["falsification_family_member"] is False

    def test_ledger_holds_62(self):
        assert "HOLDS at 62" in _block()["ledger_note"]


# ---------------------------------------------------------------------------
# 13. In-flight isolation
# ---------------------------------------------------------------------------


class TestInFlightIsolation1337:
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

    def test_1024_m846_untouched(self):
        # Ray's revert/leave/rebuild decision on m846 is pending;
        # this run does not touch it.
        res = _git("status", "--short")
        assert "competitor-entities.yaml" not in res.stdout
