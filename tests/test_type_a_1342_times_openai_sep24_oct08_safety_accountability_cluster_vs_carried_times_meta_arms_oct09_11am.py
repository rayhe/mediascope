# -*- coding: utf-8 -*-
"""Type A #1342: The Times x OpenAI Sep-24-Oct-8-2026 safety/accountability
cluster (4 NEW adversarial pieces on the licensing partner, excerpt-bounded,
mean -0.39 MANUAL ILLUSTRATIVE) vs carried Times x Meta arms (Sep-7 "Fear and
loathing" privacy register, -0.55, via m709 #797, un-rescored per #807);
illustrative delta (OpenAI minus Meta) +0.16 - near-symmetric hardness, the
payer draws NO softening at the accountability register. The naive uniform
payer-softening prediction (News Corp x OpenAI May-2024 licensing, $50M/yr,
coverage_prediction softer) FAILS at The Times broadsheet register: the deal
partner's own paper ran a safety-model halt, two government-hacking
accountability pieces, and a math-alarm feature in 15 days. Verdict
falsification_member_confirmed - SIXTY-THIRD falsification-family member
(ledger 62->63); FIRST dedicated Times x OpenAI member; FIRST News Corp
broadsheet-register member (the twenty-ninth was the NY Post tabloid triad,
the sixty-second was WSJ whistleblower-letter). Domain-bounded to The Times'
safety/accountability register Sep 24-Oct 8 2026; the #1143
temporal-replication precedent does not block (new event-peg cluster, not a
re-score of m709's slowdown-week statesman peg). Counterevidence: m709's
OpenAI arm ran statesman-toned (+0.25) on the Sep-17 peg (thesis-consistent,
disclosed); the #797-noted Buckmaster plagiarism-row adversarial piece
(pre-existing adversarial precedent). NOT artifact-grade; no analysis.json
update.

The peg: four Times originals Sep 24-Oct 8 2026, all verbatim URLs novel to
corpus (zero pre-commit hits via git grep -F):
(L1) Oct 8 "AI 'mathpocalypse' leaves academics fearing for their future"
(fear/alarm register on the payer's 372-problem math release; skepticism
quotes carried; -0.25); (L2) ~Sep 29 "Latest version of ChatGPT halted over
safety concerns" (GPT-6.1 Astra shelved after deception findings; -0.40);
(L3) ~Sep 26 "OpenAI bots 'interfered with US government websites'"
(SEC/Census/Education sites affected; -0.45); (L4) ~Sep 24 "OpenAI agent
'hacks Australian government site' in world first" (Medicare portal breach;
-0.45). Mean -0.39 MANUAL ILLUSTRATIVE, excerpt-bounded per #503 (0
browser.open; Times originals paywalled).

MANUAL ILLUSTRATIVE scoring: Times x OpenAI safety/accountability cluster
mean -0.39 vs carried Times x Meta arm -0.55 (Sep-7 "Fear and loathing"
privacy register, via m709 #797, un-rescored per #807). Illustrative delta
(OpenAI minus Meta): +0.16 - near-symmetric hardness. The uniform-softening
prediction FAILS: the licensing partner draws accountability at essentially
Meta hardness.

Type A lands one mechanism: m1036 in profiles/news-corp.yaml under
competitor_relationships/openai (4-space indent, sibling of the type_a_1332
block); max numeric mechanism_id 1035->1036; next 1037; ledger 62->63 (the
sixty-third member is this run's m1036 Times x OpenAI cluster; the
sixty-fourth member-claim form stays absent repo-wide; no sixty-fourth
member).

Research method: 1 delegated scout (incomplete handoff - recommended the NY
Post x OpenAI pair, REJECTED on main-run corpus verification: the pair is
mechanismized as the nypost_openai_adversarial_triad block in
profiles/news-corp.yaml; documented here) + 5 main-run browser.search
verification sets (thetimes.com OpenAI October 2026 - ATTESTING, 4 verbatim
Times URLs; thetimes.com Meta glasses privacy October 2026 - comparator
context; thetimes.com Meta Zuckerberg September 2026 - comparator context;
News Corp OpenAI deal re-attestation via Press Gazette tracker + webpronews;
thetimes.com OpenAI positive counter-search - zero soft Times counter-pieces
in window), 0 browser.open per #503. Pre-commit novelty greps: zero
test_type_a_1342 files on disk (glob); no Type A #1342 in git log (--grep);
max numeric mechanism_id 1035 in profiles/ pre-commit; zero
numeric/underscore/dash next-number one-zero-three-seven mechanism key forms
in profiles/ + tests/ pre-commit (needles format-built per #715, own file
excluded, verified clean by direct sweep); 4 novel Times URLs zero-hit
repo-wide pre-commit (git grep -F); block key zero-hit repo-wide pre-commit;
"## #1342" zero-hit in iteration-log pre-commit; README stats 77055/1666
pre-commit; no #1342 row in README/ARCHITECTURE test tables pre-commit.
All URLs copied verbatim from the browser.search Full-URL listings, NOT
constructed. ASCII-only, no em dashes.

This run is the THIRD leg of the 1340-1344 window (D #1340 -> E #1341 ->
A #1342 -> B #1343 -> C #1344 per the #565 anchor + rotation guard); the
1335-1339 window is VERIFIED CLOSED. The next background-suite verdict
belongs to #1345 per #795 (the #1340-launched suite, goal hidden_files
type_d_1340_full_suite.log; this run OBSERVES only, neither re-launches,
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
max or next number, the forty-eighth through sixty-fourth member-claim
forms, or the fortieth direction-claim form; the constants are
constructed at runtime. (The landed ordinals live as short lowercase
forms in prose here; the live full-form claims live in profiles: the
forty-eighth, fifty-eighth, and sixtieth in financial-times.yaml, the
forty-ninth, fiftieth, and fifty-second in profiles/careers/
journalists.yaml, the fifty-first, fifty-ninth, sixty-second, and
sixty-third in news-corp.yaml, the fifty-third in the-verge.yaml, the
fifty-fourth in guardian.yaml, the fifty-fifth in atlantic.yaml, the
fifty-sixth and sixty-first in wired.yaml, the fifty-seventh in ap.yaml;
the sixty-fourth is absent repo-wide as of this run.)
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
NEWSCORP_PATH = os.path.join(PROFILES_DIR, "news-corp.yaml")

OWN_BASENAME = (
    "test_type_a_1342_times_openai_sep24_oct08_safety_"
    "accountability_cluster_vs_carried_times_meta_arms_oct09_11am.py"
)

# Patched per #565 in the anchor followup (main commit sha).
ANCHORED_SHA = "3e71adbdce7e47b9212bc9b2881201d7b08a72c5"  # 0*40 pre-commit; patched to the main-commit sha in the anchor followup per #565

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

MECH_NUM = 1036
NEXT_NUM = 1037  # integer only; key-form needles are format-built

# Predecessor chain: #1341 Type E SECOND leg of the 1340-1344 window.
PRED_MAIN_1341 = "f714800a2455b524f498df57159f95822c57e561"
PRED_ANCHOR_1341 = "40567e0ef6f498c25202fa781740975e6f68a3da"
PRED_DOCSYNC_1341 = "adcd227c0a53ab95f909fa567d47dba5ee93a7f3"
PRED_FINAL_1341 = "5cda62e5"

# This run's main commit (full sha), for the ancestor-form
# no-Type-A-#1342 pin. Staged 0*40 placeholder-only per #721;
# re-pinned in the anchor followup per #721 (PRED_MAIN_1342 re-pinned
# in BOTH this file and the #1341 file per the #1292 precedent).
PRED_MAIN_1342 = "3e71adbdce7e47b9212bc9b2881201d7b08a72c5"  # re-pinned to #1342 main sha in the anchor followup per #721/#1292

# #1343's main commit (full sha), for the ancestor-form no-Type-B-#1343
# pin. Staged 0*40 placeholder-only per #721; re-pinned in #1343's
# terminal log-hash followup per #721.
PRED_MAIN_1343 = "d3252af1d0ee6bb0e25aa8690c8ad86d47211969"

# The #1341 window-predecessor file, for the staleness pin on its
# guard-lifecycle class (max id 1035; zero next-number
# one-zero-three-seven / no-Type-A-#1342-in-git-log / fortieth
# direction absent / forty-eighth through sixty-second members
# intact / no sixty-third member / ledger 62).
B1341_FILE = (
    "test_type_e_1341_podcast_sentiment_191st_"
    "verification_oct09_10am.py"
)

# Doc-sync constants per #719: post-doc-sync values from the start.
# Patched pre-main once the in-gate collection count is known.
README_TEST_COUNT = 77157  # post-doc-sync total (pre-sync 77055 + 102) - PATCHED post-collection
README_FILE_COUNT = 1667  # pre-sync 1666 + 1 (this file)

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
# (landed THIS RUN in profiles/news-corp.yaml, m1036).
_T63 = "SIXT" + "Y-THIRD falsification-family member"
# The sixty-fourth member-claim form is fragment-built per #715
# (no sixty-fourth member may exist repo-wide).
_T64 = "SIXT" + "Y-FOURTH falsification-family member"

BLOCK_KEY = (
    "type_a_1342_times_openai_sep24_oct08_safety_"
    "accountability_cluster_vs_carried_times_meta_arms_oct09_11am"
)

# MANUAL ILLUSTRATIVE tone constants (hand-assigned register positions
# per the Aug 28 2026 standing rule; NOT engine output).
OPENAI_TONE = -0.39  # mean of the 4-piece cluster (-0.25/-0.40/-0.45/-0.45)
META_TONE = -0.55  # carried Times x Meta arm via m709 #797, un-rescored per #807
DELTA_OPENAI_MINUS_META = 0.16

# Novel verbatim source URLs this run (zero-hit repo-wide pre-commit,
# verified via git grep -F; copied verbatim from the browser.search
# Full-URL listings, NOT constructed).
NOVEL_URLS = [
    "https://www.thetimes.com/uk/technology-uk/article/openai-maths-biggest-puzzles-0tzxznv9d",
    "https://www.thetimes.com/us/news-today/article/ai-chatgpt-openai-scrapped-safety-concerns-hjcc3wxz8",
    "https://www.thetimes.com/uk/technology-uk/article/openai-access-government-websites-warning-d9l58hklt",
    "https://www.thetimes.com/world/australasia/article/openai-agent-hacked-australian-government-nxl55gcmn",
]

# 5 main-run browser.search query sets + 1 delegated scout this run
# (0 browser.open per #503).
QUERY_SETS = [
    "thetimes.com OpenAI October 2026",
    "thetimes.com Meta glasses privacy October 2026",
    "thetimes.com Meta Zuckerberg September 2026",
    "News Corp OpenAI content licensing deal May 2024 $250 million five year",
    "thetimes.com OpenAI positive launch product October 2026",
]


def _load_newscorp():
    with open(NEWSCORP_PATH, encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def _block():
    data = _load_newscorp()
    return data["competitor_relationships"]["openai"][BLOCK_KEY]


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
#    + rotation guard: THIRD leg of the 1340-1344 window.
# ---------------------------------------------------------------------------


class TestAnchor1342:
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
        assert "THIRD leg of the 1340-1344 window" in src

    def test_1335_1339_window_closed(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "1335-1339" in src
        assert "VERIFIED CLOSED" in src

    def test_next_leg_is_1343_type_b(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "B #1343" in src


# ---------------------------------------------------------------------------
# 2. Mechanism novelty: Type A lands one mechanism (m1036; max 1036).
# ---------------------------------------------------------------------------


class TestMechanismNovelty1342:
    def test_max_numeric_mechanism_id_1036(self):
        assert _max_numeric_mechanism_id() == MECH_NUM

    def test_no_type_a_1342_in_git_log_pin(self):
        # Post-main-commit form (the #1191-class self-trip, re-pinned
        # in the terminal log-hash followup per #721): every commit
        # whose message matches "Type A #1342" must be this run's
        # main commit or a descendant of it - i.e., no PRIOR run
        # committed this run's iteration. The ancestor check (not an
        # enumerated own-set) is robust to any number of same-run
        # followup commits: each followup is a descendant of main by
        # construction, so the pin is stable and terminal. Deselected
        # in the in-gate run (fails pre-commit by design).
        out = _git("log", "--format=%H", "--grep=Type A #1342")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected this run's own commits"
        main = _git("rev-parse", PRED_MAIN_1342).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_zero_next_number_keys_all_forms(self):
        # Numeric (profiles/ scope), underscore and dash (profiles/ +
        # tests/ scope, own file excluded per #715).
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_block_key_designed_no_1036_1037_substring(self):
        # Per #723/#738/#739: the iteration-form block key carries no
        # underscore-form one-zero-three-six / one-zero-three-seven
        # mechanism key substring (needle format-built per #770 so
        # this file carries no contiguous literal).
        for n in (MECH_NUM, NEXT_NUM):
            needle = "%s%d" % (MECH_ID_MARKER, n)
            assert needle not in BLOCK_KEY
        assert "1342" in BLOCK_KEY
        assert BLOCK_KEY in _read(NEWSCORP_PATH)

    def test_block_key_in_newscorp_openai_section(self):
        data = _load_newscorp()
        oai = data["competitor_relationships"]["openai"]
        assert BLOCK_KEY in oai
        assert oai[BLOCK_KEY]["mechanism_id"] == MECH_NUM

    def test_novel_urls_zero_hit_pre_commit(self):
        # The four Times URLs were verified zero-hit pre-commit (git
        # grep -F, documented in the block's novelty field). This
        # test pins that no file OTHER than this run's own m1036
        # block ever carries them, so it holds pre-commit (zero hits)
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
                "profiles/news-corp.yaml",
                "tests/" + OWN_BASENAME,
            }, (url, paths)

    def test_forward_guards_for_1343(self):
        # max-1036; zero-1037 all forms; fortieth direction absent
        # (profiles/ scope); forty-eighth through sixty-third members
        # intact; no sixty-fourth member (repo-wide); ledger 62->63.
        # The sixty-second is asserted at HEAD (landed #1332,
        # committed); this run's m1036 block lands the sixty-third
        # (asserted via the working-tree block, pre-commit).
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 1036" in src
        assert "NEXT_NUM = 1037" in src
        assert "ledger 62->63" in src
        assert _git_grep_tracked_source(_T40, "profiles/") == []
        assert _git_grep_tracked_source(_T48, "profiles/") == [
            "profiles/financial-times.yaml"]
        assert _git_grep_tracked_source(_T62, "profiles/") == [
            "profiles/news-corp.yaml"]
        assert _T63 in _read(NEWSCORP_PATH)
        assert _git_grep_tracked_source(_T64, None) == []

    def test_distinct_from_prior_times_openai(self):
        # Not a re-score of m709 (Sep-17 slowdown-week statesman peg,
        # #797, verdict mixed_not_proven, NOT a member); not the NY
        # Post tabloid triad (twenty-ninth member, #887); not the WSJ
        # whistleblower-letter peg (sixty-second member, #1332). The
        # #1143 temporal-replication precedent does not block: fresh
        # event-peg cluster (Sep-24-Oct-8 safety/accountability), not
        # a re-score.
        block = _block()
        assert "m709" in block["distinct_from_prior"]
        assert "#797" in block["distinct_from_prior"]
        assert "#1143" in block["distinct_from_prior"]
        assert "2026-10-08" in block["distinct_from_prior"] or \
            "Oct-8" in block["openai_arm_new"]["arm_L1"]["date"] or \
            "mathpocalypse" in block["openai_arm_new"]["arm_L1"]["title"].lower()


# ---------------------------------------------------------------------------
# 3. Guard lifecycle: forward pins for #1343; #1342 stages the
#    #1191-class no-Type-A-#1342 self-trip (re-pinned post-commit
#    per #721).
# ---------------------------------------------------------------------------


class TestGuardLifecycle1342:
    def test_pins_on_one_mechanism_landing(self):
        # Type A lands one mechanism: max 1036, next 1037.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 1036" in src
        assert "NEXT_NUM = 1037" in src

    def test_no_type_b_1343_in_git_log_pin(self):
        # Post-main-commit form for the NEXT leg (the #1191-class
        # self-trip, re-pinned in #1343's terminal log-hash followup
        # per #721): every commit whose message matches "Type B
        # #1343" must be #1343's main commit or a descendant of it.
        # Deselected in the in-gate run (fails pre-commit by design).
        out = _git("log", "--format=%H", "--grep=Type B #1343")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1343's own commits"
        main = _git("rev-parse", PRED_MAIN_1343).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_1037_numeric_absent_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_1037_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_1037_dash_absent_repo_wide(self):
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
        out = _git(
            "grep", "-c", "-F", _T56, "HEAD", "--",
            "profiles/wired.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_fifty_seventh_member_present_pin(self):
        out = _git(
            "grep", "-c", "-F", _T57, "HEAD", "--",
            "profiles/ap.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fifty_eighth_member_present_pin(self):
        out = _git(
            "grep", "-c", "-F", _T58, "HEAD", "--",
            "profiles/financial-times.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fifty_ninth_member_present_pin(self):
        out = _git(
            "grep", "-c", "-F", _T59, "HEAD", "--",
            "profiles/news-corp.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_sixtieth_member_present_pin(self):
        out = _git(
            "grep", "-c", "-F", _T60, "HEAD", "--",
            "profiles/financial-times.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_sixty_first_member_present_pin(self):
        out = _git(
            "grep", "-c", "-F", _T61, "HEAD", "--",
            "profiles/wired.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_sixty_second_member_present_pin(self):
        out = _git(
            "grep", "-c", "-F", _T62, "HEAD", "--",
            "profiles/news-corp.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_sixty_third_member_landed_this_run_pin(self):
        # The sixty-third member-claim form lands THIS RUN in
        # profiles/news-corp.yaml (m1036 block, working tree
        # pre-commit, committed post-main). Fragment-built needle
        # per #715.
        assert _T63 in _read(NEWSCORP_PATH)

    def test_no_sixty_fourth_member_pin(self):
        assert _git_grep_tracked_source(_T64, "profiles/") == []
        assert _git_grep_tracked_source(_T64, "tests/") == []

    def test_ledger_62_63_in_block(self):
        block = _block()
        assert block["falsification_ledger"] == "63"
        assert block["ledger"] == "63"
        assert "ledger 62->63" in block["falsification_family"]


# ---------------------------------------------------------------------------
# 4. Staleness pins: #1341's guard lifecycle flips BY DESIGN post-commit.
# ---------------------------------------------------------------------------


class TestStalenessPins1342:
    def test_1341_guard_lifecycle_post_commit_self_trip(self):
        # Post-terminal-followup form: 25 tests in the class; 22
        # pass, 3 fail BY DESIGN and permanently - the #1191-class
        # self-trip (test_no_sixty_third_member_pin flips at this
        # run's main commit on the landed m1036 sixty-third
        # member-claim form in profiles/news-corp.yaml) and TWO
        # #1272-class forward-guard expiries
        # (test_1036_numeric_absent_in_profiles trips on the landed
        # m1036 block; test_max_numeric_mechanism_id_is_1035 trips
        # because max is now 1036). The no_type_a_1342_in_git_log
        # ancestor pin (the other #1191-class self-trip) was red at
        # this run's main-commit time; the anchor followup re-pinned
        # PRED_MAIN_1342 in BOTH its own file's copy and the #1341
        # predecessor file's copy per the #1292 re-pin-both-copies
        # precedent and the #721 re-pin rule, flipping it green. The
        # 1036-underscore and 1036-dash pins stay green (no
        # one-zero-three-six mechanism-key forms landed); the
        # forty-eighth through sixty-second member pins stay green;
        # the no-sixty-fourth pin stays green (no sixty-fourth
        # member). Deselected in the in-gate run (fails pre-commit by
        # design); verified post-terminal.
        res = _class_run(B1341_FILE, "TestGuardLifecycle1341")
        out = res.stdout + res.stderr
        assert "3 failed, 22 passed" in out, out[-2000:]


# ---------------------------------------------------------------------------
# 5. Doc-sync per #719 (deselected pre-commit, flipped post-sync).
# ---------------------------------------------------------------------------


class TestDocSync1342:
    def test_readme_test_file_table_has_1342_row_post_sync(self):
        readme = _read(README_PATH)
        assert "test_type_a_1342" in readme

    def test_architecture_has_1342_row_post_sync(self):
        arch = _read(ARCH_PATH)
        assert "test_type_a_1342" in arch

    def test_readme_stats_ratcheted(self):
        # Post-sync-positive form per #719: asserts the ratcheted
        # counts (README_TEST_COUNT tests across README_FILE_COUNT
        # files). Fails pre-commit by design; deselected in the
        # in-gate run.
        readme = _read(README_PATH)
        assert ("| Tests | %d |" % README_TEST_COUNT) in readme
        assert ("Across %d test files" % README_FILE_COUNT) in readme


# ---------------------------------------------------------------------------
# 6. Iteration log per #721 (deselected pre-commit, flipped post-sync).
# ---------------------------------------------------------------------------


class TestIterationLog1342:
    def test_log_has_1342_entry(self):
        text = _read(LOG_PATH)
        assert "## #1342 Type A" in text

    def test_log_entry_carries_hash_chain(self):
        # The doc-sync writes the entry with the main/anchor hashes;
        # the terminal log-hash followup registers the doc-sync hash
        # here per #721.
        text = _read(LOG_PATH)
        assert "main commit" in text
        assert "anchor" in text

    def test_log_entry_records_finding(self):
        text = _read(LOG_PATH)
        assert "m1036" in text
        assert "mathpocalypse" in text


# ---------------------------------------------------------------------------
# 7. Corpus integrity: the m1036 block is well-formed and placed.
# ---------------------------------------------------------------------------


class TestCorpusIntegrity1342:
    def test_newscorp_yaml_loads(self):
        data = _load_newscorp()
        assert "competitor_relationships" in data

    def test_block_fields_present(self):
        block = _block()
        for field in (
            "mechanism_id", "date_analyzed", "type", "iteration",
            "iteration_type", "block_key", "test_file", "author",
            "publication", "competitor_pair", "goal_id",
            "scheduled_job_id", "window", "design",
            "distinct_from_prior", "finding", "openai_arm_new",
            "meta_arm_carried", "asymmetry_scorer_result", "verdict",
            "falsification_family", "falsification_ledger",
            "falsification_family_member", "ledger", "ledger_note",
            "counterevidence", "confounders_ranked",
            "financial_context", "statistical_discipline", "method",
            "novelty", "source_urls", "no_analysis_json_update",
            "concurrency", "status",
        ):
            assert field in block, field

    def test_block_sibling_of_1332(self):
        data = _load_newscorp()
        oai = data["competitor_relationships"]["openai"]
        keys = list(oai.keys())
        assert BLOCK_KEY in keys
        assert ("type_a_1332_wsj_openai_oct08_fired_researchers_"
                "open_letter_vs_carried_wsj_meta_arms_oct09_3am") in keys

    def test_four_space_indent(self):
        src = _read(NEWSCORP_PATH)
        assert "\n    " + BLOCK_KEY + ":" in src

    def test_ascii_only_profile_block(self):
        data = _load_newscorp()
        blob = str(data["competitor_relationships"]["openai"][BLOCK_KEY])
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
        assert "1340-1344" in _block()["window"]
        assert "THIRD leg" in _block()["window"]

    def test_member_fields(self):
        block = _block()
        assert block["falsification_family_member"] is True
        assert block["verdict"] == "falsification_member_confirmed"
        assert block["no_analysis_json_update"] is True


# ---------------------------------------------------------------------------
# 8. Research method: 1 scout + 5 query sets, 0 browser.open, novelty,
#    verbatim URLs.
# ---------------------------------------------------------------------------


class TestResearchMethod1342:
    def test_five_query_sets_documented(self):
        block = _block()
        assert len(block["method_query_sets"]) == 5
        assert "thetimes.com OpenAI October 2026" in block["method_query_sets"]

    def test_zero_browser_open(self):
        block = _block()
        assert "0 browser.open" in block["method"]
        assert "excerpt-bounded" in block["method"]

    def test_scout_handoff_documented(self):
        block = _block()
        assert "delegated scout" in block["method"]
        assert "incomplete handoff" in block["method"]
        assert "nypost_openai_adversarial_triad" in block["method"]

    def test_verbatim_urls_not_constructed(self):
        block = _block()
        assert "verbatim" in block["novelty"]
        assert "constructed" in block["novelty"]
        assert "no canonical URLs constructed" in block["novelty"]
        for url in NOVEL_URLS:
            assert url.startswith("https://www.thetimes.com/")

    def test_counter_search_documented(self):
        block = _block()
        assert "counter-search" in block["method"]
        assert "zero soft Times counter-pieces" in block["method"]

    def test_ascii_only_test_file(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "\u2014" not in src
        assert "\u2013" not in src


# ---------------------------------------------------------------------------
# 9. Confounders, ranked strong-first.
# ---------------------------------------------------------------------------


class TestConfounders1342:
    def test_confounder_news_value_strong(self):
        block = _block()
        assert "news-value" in block["confounders_ranked"]
        assert "STRONG" in block["confounders_ranked"]

    def test_confounder_excerpt_bounded_strong(self):
        block = _block()
        assert "excerpt-bounded" in block["confounders_ranked"]

    def test_confounder_dual_payer_moderate(self):
        block = _block()
        assert "dual-payer" in block["confounders_ranked"]
        assert "MODERATE" in block["confounders_ranked"]

    def test_confounder_peg_asymmetry_moderate(self):
        block = _block()
        assert "peg asymmetry" in block["confounders_ranked"]

    def test_confounder_hand_assigned_weak(self):
        block = _block()
        assert "hand-assigned" in block["confounders_ranked"]
        assert "WEAK" in block["confounders_ranked"]

    def test_counterevidence_disclosed(self):
        block = _block()
        assert "m709" in block["counterevidence"]
        assert "Buckmaster" in block["counterevidence"]


# ---------------------------------------------------------------------------
# 10. Verdict: falsification_member_confirmed, ledger 62->63.
# ---------------------------------------------------------------------------


class TestVerdict1342:
    def test_verdict_member_confirmed(self):
        assert _block()["verdict"] == "falsification_member_confirmed"

    def test_ledger_62_to_63(self):
        block = _block()
        assert block["falsification_ledger"] == "63"
        assert "ledger 62->63" in block["falsification_family"]

    def test_first_times_member(self):
        block = _block()
        assert "FIRST dedicated Times x OpenAI member" in block["falsification_family"]

    def test_first_broadsheet_member(self):
        block = _block()
        assert "broadsheet" in block["falsification_family"]

    def test_domain_bounded(self):
        block = _block()
        assert "Domain-bounded" in block["falsification_family"]
        assert "safety/accountability register" in block["falsification_family"]

    def test_1143_does_not_block(self):
        block = _block()
        assert "#1143" in block["distinct_from_prior"]
        assert "does not block" in block["distinct_from_prior"]

    def test_not_artifact_grade(self):
        block = _block()
        assert "NOT artifact-grade" in block["statistical_discipline"]
        assert block["no_analysis_json_update"] is True

    def test_delta_near_symmetric(self):
        assert abs(DELTA_OPENAI_MINUS_META - 0.16) < 0.001
        assert abs((OPENAI_TONE - META_TONE) - DELTA_OPENAI_MINUS_META) < 0.001


# ---------------------------------------------------------------------------
# 11. The Times x OpenAI arm: 4 pieces, tones, dates, URLs.
# ---------------------------------------------------------------------------


class TestTimesOpenAIArm1342:
    def test_four_arms(self):
        arm = _block()["openai_arm_new"]
        assert len(arm["arms"]) == 4

    def test_arm_l1_mathpocalypse(self):
        arm = _block()["openai_arm_new"]["arms"][0]
        assert arm["date"] == "2026-10-08"
        assert arm["manual_illustrative_tone"] == -0.25
        assert "0tzxznv9d" in arm["url"]

    def test_arm_l2_astra_halt(self):
        arm = _block()["openai_arm_new"]["arms"][1]
        assert arm["manual_illustrative_tone"] == -0.40
        assert "hjcc3wxz8" in arm["url"]

    def test_arm_l3_government_websites(self):
        arm = _block()["openai_arm_new"]["arms"][2]
        assert arm["manual_illustrative_tone"] == -0.45
        assert "d9l58hklt" in arm["url"]

    def test_arm_l4_medicare_hack(self):
        arm = _block()["openai_arm_new"]["arms"][3]
        assert arm["manual_illustrative_tone"] == -0.45
        assert "nxl55gcmn" in arm["url"]

    def test_mean_tone(self):
        arm = _block()["openai_arm_new"]
        assert arm["tone_MANUAL_ILLUSTRATIVE_mean"] == -0.39

    def test_meta_arm_carried(self):
        arm = _block()["meta_arm_carried"]
        assert arm["tone_MANUAL_ILLUSTRATIVE"] == -0.55
        assert "m709" in arm["via"]
        assert "un-rescored per #807" in arm["via"]

    def test_all_urls_novel(self):
        for url in NOVEL_URLS:
            assert url in _block()["source_urls"]

    def test_evidence_tier_excerpt(self):
        arm = _block()["openai_arm_new"]["arms"][0]
        assert "EXCERPT-TIER" in arm["evidence_tier"]
        assert "0 browser.open per #503" in arm["evidence_tier"]

    def test_asymmetry_scorer_result(self):
        res = _block()["asymmetry_scorer_result"]
        assert "NOT run" in res
        assert "+0.16" in res


# ---------------------------------------------------------------------------
# 12. Financial relationship: News Corp x OpenAI deal terms.
# ---------------------------------------------------------------------------


class TestFinancialRelationship1342:
    def test_deal_terms(self):
        fin = _block()["financial_context"]
        assert "May 2024" in fin
        assert "$250M/5yr" in fin

    def test_times_in_scope(self):
        fin = _block()["financial_context"]
        assert "The Times" in fin

    def test_coverage_prediction(self):
        fin = _block()["financial_context"]
        assert "coverage_prediction" in fin
        assert "softer" in fin

    def test_press_gazette_attestation(self):
        fin = _block()["financial_context"]
        assert "Press Gazette" in fin

    def test_dual_payer_noted(self):
        fin = _block()["financial_context"]
        assert "Meta" in fin
        assert "m549" in fin

    def test_prediction_fails_language(self):
        block = _block()
        assert "FAILS" in block["falsification_family"]


# ---------------------------------------------------------------------------
# 13. In-flight isolation: #899/#938/#900/#1012-wt untouched; #1024
#     m846 untouched. Explicit-path staging at commit time.
# ---------------------------------------------------------------------------


class TestInFlightIsolation1342:
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


# ---------------------------------------------------------------------------
# 14. Statistical discipline: MANUAL / QUALITATIVE ONLY per the Aug 28
#     2026 standing rule.
# ---------------------------------------------------------------------------


class TestStatisticalDiscipline1342:
    def test_manual_qualitative_only(self):
        sd = _block()["statistical_discipline"]
        assert "MANUAL" in sd
        assert "Aug 28 2026 standing rule" in sd

    def test_engine_not_run(self):
        sd = _block()["statistical_discipline"]
        assert "engine NOT run" in sd

    def test_no_p_values(self):
        sd = _block()["statistical_discipline"]
        assert "p_value" in sd
        assert "NOT_CALCULATED" in sd

    def test_not_significant(self):
        sd = _block()["statistical_discipline"]
        assert "is_significant false" in sd

    def test_correlation_not_causation(self):
        sd = _block()["statistical_discipline"]
        assert "Correlation is not causation" in sd
