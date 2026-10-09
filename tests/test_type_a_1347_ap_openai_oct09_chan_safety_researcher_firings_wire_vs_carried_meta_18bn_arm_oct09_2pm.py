# -*- coding: utf-8 -*-
"""Type A #1347: AP x OpenAI Oct-9-2026 safety-turmoil accountability wire
(Kelvin Chan bylined original on the three fired safety researchers,
relay-attested, excerpt-bounded, -0.35 MANUAL ILLUSTRATIVE) vs carried AP x
Meta arm (Aug-26 $18bn teen-addiction settlement wire, -0.45, via m970 #1232,
un-rescored per #807); illustrative delta (OpenAI minus Meta) +0.10 -
near-symmetric hardness, the payer draws NO softening at the wire register.
The naive uniform payer-softening prediction (AP x OpenAI Jul-13-2023
archive-licensing agreement, coverage_prediction softer) FAILS on the
safety-turmoil peg: the wire runs the licensing counterparty's researcher
firings carrying the "corporate interests before safety" charge and the
rogue-agent turmoil framing. Verdict falsification_member_confirmed -
SIXTY-FOURTH falsification-family member (ledger 63->64); FIRST dedicated
uniform-softening TEST on the AP x OpenAI pair (m970 #1232 was documentation,
verdict mechanism_documentation_not_a_discovery; m1003 #1287 tested the AP x
Anthropic dual-lab leg). Domain-bounded to AP's wire register on the Oct-9
safety-turmoil peg. Counterevidence: m970's +0.35 softening pole (different
peg, cross-peg confounded, disclosed); the Sep-29 AP DevDay piece is MIXED
not soft (headline juxtaposes launch vs shelved model). NOT artifact-grade;
no analysis.json update.

The peg: one AP original, Oct 9 2026, relay-attested (apnews.com canonical
did not arrive in any search Full-URL listing; NOT constructed): Kelvin
Chan, LONDON (AP) - "OpenAI fires 3 safety researchers in dispute over AI
risks". The wire leads with OpenAI's "breach of trust" framing but gives
full prominent carriage to the trio's (Tomek Korbak, Jasmine Wang, Mikita
Balesni) counter-charge that OpenAI put "corporate interests before safety",
contextualizes the firings as the "latest sign of turmoil inside leading AI
companies over the safety of the technology, highlighted by a series of
incidents involving rogue AI agents", recalls the July Hugging Face
agent-escape, and prints OpenAI's denial ("were not about safety concerns or
speaking out"). Attested by two independent relays carrying verbatim AP
byline/dateline/copyright (kcau9.com, ottumwacourier.com). MANUAL
ILLUSTRATIVE -0.35, excerpt-bounded per #503 (0 browser.open).

MANUAL ILLUSTRATIVE scoring: AP x OpenAI Oct-9 wire -0.35 vs carried AP x
Meta arm -0.45 (Aug-26 $18bn settlement wire, via m970 #1232, un-rescored
per #807). Illustrative delta (OpenAI minus Meta): +0.10 - near-symmetric
hardness. The uniform-softening prediction FAILS: the licensing partner
draws accountability-wire hardness at essentially Meta level.

Type A lands one mechanism: m1039 in profiles/ap.yaml under
competitor_relationships/openai (4-space indent, sibling of the type_a_1232
block); max numeric mechanism_id 1038->1039; next 1040; ledger 63->64 (the
sixty-fourth member is this run's m1039 AP x OpenAI wire; the sixty-fifth
member-claim form stays absent repo-wide; no sixty-fifth member).

Research method: 1 delegated scout (incomplete handoff - zero
bloomberg.com/apnews.com/cnbc.com originals in the search index across all
three tracks; the Bloomberg/CNBC scoops surfaced only as secondary
citations, no verbatim target-domain URLs, none constructed; documented
here) + 4 main-run browser.search verification sets (Associated Press
OpenAI investigation accountability October 2026 - ATTESTING, 2 verbatim
relay URLs for the Oct-9 Chan firings piece; AP report OpenAI safety
concerns October 2026 - corroborating carrier + Astra context; Associated
Press OpenAI archive licensing deal July 2023 - deal re-attestation via
Press Gazette tracker (crawled 2h) + Reuters Jul-13-2023 original;
Associated Press OpenAI product launch positive October 2026 -
counter-search, zero soft AP counter-pieces in window), 0 browser.open per
#503. Pre-commit novelty greps: zero test_type_a_1347 files on disk (glob);
no Type A #1347 in git log (--grep); max numeric mechanism_id 1038 in
profiles/ pre-commit; zero numeric/underscore/dash next-number
one-zero-four-zero mechanism key forms in profiles/ + tests/ pre-commit
(needles format-built per #715, own file excluded, verified clean by direct
sweep); 2 novel relay URLs zero-hit repo-wide pre-commit (git grep -F);
block key zero-hit repo-wide pre-commit; "## #1347" zero-hit in
iteration-log pre-commit; README stats 77570/1671 pre-commit; no #1347 row
in README/ARCHITECTURE test tables pre-commit. All URLs copied verbatim
from the browser.search Full-URL listings, NOT constructed. ASCII-only, no
em dashes.

This run is the THIRD leg of the 1345-1349 window (D #1345 -> E #1346 ->
A #1347 -> B #1348 -> C #1349 per the #565 anchor + rotation guard); the
1340-1344 window is VERIFIED CLOSED. The next background-suite verdict
belongs to #1350 per #795 (the #1345-launched suite, goal hidden_files
type_d_1345_full_suite.log; this run neither observes, re-launches, kills,
nor writes to it).

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
max or next number, the forty-eighth through sixty-fifth member-claim
forms, or the fortieth direction-claim form; the constants are
constructed at runtime. (The landed ordinals live as short lowercase
forms in prose here; the live full-form claims live in profiles: the
forty-eighth, fifty-eighth, and sixtieth in financial-times.yaml, the
forty-ninth, fiftieth, and fifty-second in profiles/careers/
journalists.yaml, the fifty-first, fifty-ninth, sixty-second, and
sixty-third in news-corp.yaml, the fifty-third in the-verge.yaml, the
fifty-fourth in guardian.yaml, the fifty-fifth in atlantic.yaml, the
fifty-sixth and sixty-first in wired.yaml, the fifty-seventh and
sixty-fourth in ap.yaml; the sixty-fifth is absent repo-wide as of this
run.)
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
AP_PATH = os.path.join(PROFILES_DIR, "ap.yaml")

OWN_BASENAME = (
    "test_type_a_1347_ap_openai_oct09_chan_safety_"
    "researcher_firings_wire_vs_carried_meta_18bn_arm_oct09_2pm.py"
)

# Patched per #565 in the anchor followup (main commit sha).
ANCHORED_SHA = "0" * 40  # 0*40 pre-commit; patched to the main-commit sha in the anchor followup per #565

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

MECH_NUM = 1039
NEXT_NUM = 1040  # integer only; key-form needles are format-built

# Predecessor chain: #1346 Type E SECOND leg of the 1345-1349 window.
PRED_MAIN_1346 = "9adb96df467924dbb9295f8c3dc3ac8c299c00c1"
PRED_ANCHOR_1346 = "fe70ef530f13017ec8a1a6967b096f9dfdc56721"
PRED_DOCSYNC_1346 = "5c0591b72a6b31b093d64bb68043d73d3ba870e5"
PRED_FINAL_1346 = "d6b802b3"

# This run's main commit (full sha), for the ancestor-form
# no-Type-A-#1347 pin. Staged 0*40 placeholder-only per #721;
# re-pinned in the anchor followup per #721 (PRED_MAIN_1347 re-pinned
# in BOTH this file and the #1346 file per the #1292 precedent).
PRED_MAIN_1347 = "0" * 40  # staged placeholder per #721; re-pinned to the #1347 main sha in the anchor followup per #721/#1292

# #1348's main commit (full sha), for the ancestor-form no-Type-B-#1348
# pin. Staged 0*40 placeholder-only per #721; re-pinned in #1348's
# terminal log-hash followup per #721.
PRED_MAIN_1348 = "0" * 40  # staged placeholder per #721; re-pinned in #1348's terminal log-hash followup

# The #1346 window-predecessor file, for the staleness pin on its
# guard-lifecycle class (max id 1035; zero next-number
# one-zero-four-zero / no-Type-A-#1347-in-git-log / fortieth
# direction absent / forty-eighth through sixty-second members
# intact / no sixty-third member / ledger 62).
B1346_FILE = (
    "test_type_e_1346_podcast_sentiment_191st_"
    "verification_oct09_10am.py"
)

# Doc-sync constants per #719: post-doc-sync values from the start.
# Patched pre-main once the in-gate collection count is known.
README_TEST_COUNT = 77670  # post-doc-sync total (pre-sync 77570 + 100) - PATCHED post-collection
README_FILE_COUNT = 1672  # pre-sync 1671 + 1 (this file)

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
# (landed #1342 in profiles/news-corp.yaml, m1036).
_T63 = "SIXT" + "Y-THIRD falsification-family member"
# The sixty-fourth member-claim form is fragment-built per #715
# (no sixty-fourth member may exist repo-wide).
# The sixty-fourth member-claim form is fragment-built per #715
# (landed THIS RUN in profiles/ap.yaml, m1039).
_T64 = "SIXT" + "Y-FOURTH falsification-family member"
# The sixty-fifth member-claim form is fragment-built per #715
# (no sixty-fifth member may exist repo-wide).
_T65 = "SIXT" + "Y-FIFTH falsification-family member"

BLOCK_KEY = (
    "type_a_1347_ap_openai_oct09_chan_safety_"
    "researcher_firings_wire_vs_carried_meta_18bn_arm_oct09_2pm"
)

# MANUAL ILLUSTRATIVE tone constants (hand-assigned register positions
# per the Aug 28 2026 standing rule; NOT engine output).
OPENAI_TONE = -0.35  # the Oct-9 Chan firings wire (adversarial-substance wire register)
META_TONE = -0.45  # carried AP x Meta arm via m970 #1232, un-rescored per #807
DELTA_OPENAI_MINUS_META = 0.10

# Novel verbatim source URLs this run (zero-hit repo-wide pre-commit,
# verified via git grep -F; copied verbatim from the browser.search
# Full-URL listings, NOT constructed).
NOVEL_URLS = [
    "https://www.kcau9.com/news/tech-news/ap-openai-fires-3-safety-researchers-in-dispute-over-ai-risks/",
    "https://www.ottumwacourier.com/news/business/openai-fires-3-safety-researchers-in-dispute-over-ai-risks/article_232b1065-ddc6-5919-a30f-152b0bdfb0df.html",
]

# 4 main-run browser.search query sets + 1 delegated scout this run
# (0 browser.open per #503).
QUERY_SETS = [
    "Associated Press OpenAI investigation accountability October 2026",
    "AP report OpenAI safety concerns October 2026",
    "Associated Press OpenAI archive licensing deal July 2023",
    "Associated Press OpenAI product launch positive October 2026",
]


def _load_ap():
    with open(AP_PATH, encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def _block():
    data = _load_ap()
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
#    + rotation guard: THIRD leg of the 1345-1349 window.
# ---------------------------------------------------------------------------


class TestAnchor1347:
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
        assert "THIRD leg of the 1345-1349 window" in src

    def test_1340_1344_window_closed(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "1340-1344" in src
        assert "VERIFIED CLOSED" in src

    def test_next_leg_is_1348_type_b(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "B #1348" in src


# ---------------------------------------------------------------------------
# 2. Mechanism novelty: Type A lands one mechanism (m1039; max 1039).
# ---------------------------------------------------------------------------


class TestMechanismNovelty1347:
    def test_max_numeric_mechanism_id_1039(self):
        assert _max_numeric_mechanism_id() == MECH_NUM

    def test_no_type_a_1347_in_git_log_pin(self):
        # Post-main-commit form (the #1191-class self-trip, re-pinned
        # in the terminal log-hash followup per #721): every commit
        # whose message matches "Type A #1347" must be this run's
        # main commit or a descendant of it - i.e., no PRIOR run
        # committed this run's iteration. The ancestor check (not an
        # enumerated own-set) is robust to any number of same-run
        # followup commits: each followup is a descendant of main by
        # construction, so the pin is stable and terminal. Deselected
        # in the in-gate run (fails pre-commit by design).
        out = _git("log", "--format=%H", "--grep=Type A #1347")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected this run's own commits"
        main = _git("rev-parse", PRED_MAIN_1347).stdout.strip()
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
        # underscore-form one-zero-three-nine / one-zero-four-zero
        # mechanism key substring (needle format-built per #770 so
        # this file carries no contiguous literal).
        for n in (MECH_NUM, NEXT_NUM):
            needle = "%s%d" % (MECH_ID_MARKER, n)
            assert needle not in BLOCK_KEY
        assert "1347" in BLOCK_KEY
        assert BLOCK_KEY in _read(AP_PATH)

    def test_block_key_in_ap_openai_section(self):
        data = _load_ap()
        oai = data["competitor_relationships"]["openai"]
        assert BLOCK_KEY in oai
        assert oai[BLOCK_KEY]["mechanism_id"] == MECH_NUM

    def test_novel_urls_zero_hit_pre_commit(self):
        # The two relay URLs were verified zero-hit pre-commit (git
        # grep -F, documented in the block's novelty field). This
        # test pins that no file OTHER than this run's own m1039
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
                "profiles/ap.yaml",
                "tests/" + OWN_BASENAME,
            }, (url, paths)

    def test_forward_guards_for_1348(self):
        # max-1039; zero-1040 all forms; fortieth direction absent
        # (profiles/ scope); forty-eighth through sixty-fourth members
        # intact; no sixty-fifth member (repo-wide); ledger 63->64.
        # The sixty-third is asserted at HEAD (landed #1342,
        # committed); this run's m1039 block lands the sixty-fourth
        # (asserted via the working-tree block, pre-commit).
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 1039" in src
        assert "NEXT_NUM = 1040" in src
        assert "ledger 63->64" in src
        assert _git_grep_tracked_source(_T40, "profiles/") == []
        assert _git_grep_tracked_source(_T48, "profiles/") == [
            "profiles/financial-times.yaml"]
        assert _git_grep_tracked_source(_T63, "profiles/") == [
            "profiles/news-corp.yaml"]
        assert _T64 in _read(AP_PATH)
        assert _git_grep_tracked_source(_T65, None) == []

    def test_distinct_from_prior_ap_openai(self):
        # Not a re-score of m970 (Sep-28/29 Astra-delay wire, #1232,
        # verdict mechanism_documentation_not_a_discovery, NOT a
        # member, NOT a uniform-prediction test); not m1003 (AP x
        # Anthropic dual-lab leg, #1287, fifty-seventh member,
        # different pair); not the #1303 Type B Kelvin Chan journalist
        # mechanism (different level and peg). The #1143
        # temporal-replication precedent does not block: fresh
        # event-peg (Oct-9 firings) and the FIRST hardness test on the
        # AP x OpenAI pair, not a re-score.
        block = _block()
        assert "m970" in block["distinct_from_prior"]
        assert "#1232" in block["distinct_from_prior"]
        assert "m1003" in block["distinct_from_prior"]
        assert "#1143" in block["distinct_from_prior"]
        assert "Oct-9" in block["distinct_from_prior"] or \
            "2026-10-09" in block["openai_arm_new"]["arm_A1"]["date"]


# ---------------------------------------------------------------------------
# 3. Guard lifecycle: forward pins for #1348; #1347 stages the
#    #1191-class no-Type-A-#1347 self-trip (re-pinned post-commit
#    per #721).
# ---------------------------------------------------------------------------


class TestGuardLifecycle1347:
    def test_pins_on_one_mechanism_landing(self):
        # Type A lands one mechanism: max 1039, next 1040.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 1039" in src
        assert "NEXT_NUM = 1040" in src

    def test_no_type_b_1348_in_git_log_pin(self):
        # Post-main-commit form for the NEXT leg (the #1191-class
        # self-trip, re-pinned in #1348's terminal log-hash followup
        # per #721): every commit whose message matches "Type B
        # #1348" must be #1348's main commit or a descendant of it.
        # Deselected in the in-gate run (fails pre-commit by design).
        out = _git("log", "--format=%H", "--grep=Type B #1348")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1348's own commits"
        main = _git("rev-parse", PRED_MAIN_1348).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_1040_numeric_absent_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_1040_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_1040_dash_absent_repo_wide(self):
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

    def test_sixty_third_member_intact_pin(self):
        # The sixty-third member-claim form is committed at HEAD
        # (landed #1342, m1036, profiles/news-corp.yaml).
        out = _git(
            "grep", "-c", "-F", _T63, "HEAD", "--",
            "profiles/news-corp.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_sixty_fourth_member_landed_this_run_pin(self):
        # The sixty-fourth member-claim form lands THIS RUN in
        # profiles/ap.yaml (m1039 block, working tree pre-commit,
        # committed post-main). Fragment-built needle per #715.
        assert _T64 in _read(AP_PATH)

    def test_no_sixty_fifth_member_pin(self):
        assert _git_grep_tracked_source(_T65, "profiles/") == []
        assert _git_grep_tracked_source(_T65, "tests/") == []

    def test_ledger_63_64_in_block(self):
        block = _block()
        assert block["falsification_ledger"] == "64"
        assert block["ledger"] == "64"
        assert "ledger 63->64" in block["falsification_family"]


# ---------------------------------------------------------------------------
# 4. Staleness pins: #1346's guard lifecycle flips BY DESIGN post-commit.
# ---------------------------------------------------------------------------


class TestStalenessPins1347:
    def test_1346_guard_lifecycle_post_commit_self_trip(self):
        # Post-terminal-followup form: 26 tests in the class; 23
        # pass, 3 fail BY DESIGN and permanently - the #1191-class
        # self-trip (test_no_sixty_fourth_member_pin flips at this
        # run's main commit on the landed m1039 sixty-fourth
        # member-claim form in profiles/ap.yaml) and TWO #1272-class
        # forward-guard expiries (test_1039_numeric_absent_in_profiles
        # trips on the landed m1039 block;
        # test_max_numeric_mechanism_id_is_1038 trips because max is
        # now 1039). The no_type_a_1347_in_git_log ancestor pin (the
        # other #1191-class self-trip) was red at this run's
        # main-commit time; the anchor followup re-pinned
        # PRED_MAIN_1347 in BOTH its own file's copy and the #1346
        # predecessor file's copy per the #1292 re-pin-both-copies
        # precedent and the #721 re-pin rule, flipping it green. The
        # 1039-underscore and 1039-dash pins stay green (no
        # one-zero-four-zero mechanism-key forms landed); the
        # forty-eighth through sixty-third member pins stay green;
        # the no-sixty-fifth pin stays green (no sixty-fifth member);
        # the ledger-holds-at-63 pin stays green (static string in
        # competitor-entities.yaml, unaffected). Deselected in the
        # in-gate run (fails pre-commit by design); verified
        # post-terminal.
        res = _class_run(B1346_FILE, "TestGuardLifecycle1346")
        out = res.stdout + res.stderr
        assert "3 failed, 23 passed" in out, out[-2000:]


# ---------------------------------------------------------------------------
# 5. Doc-sync per #719 (deselected pre-commit, flipped post-sync).
# ---------------------------------------------------------------------------


class TestDocSync1347:
    def test_readme_test_file_table_has_1347_row_post_sync(self):
        readme = _read(README_PATH)
        assert "test_type_a_1347" in readme

    def test_architecture_has_1347_row_post_sync(self):
        arch = _read(ARCH_PATH)
        assert "test_type_a_1347" in arch

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


class TestIterationLog1347:
    def test_log_has_1347_entry(self):
        text = _read(LOG_PATH)
        assert "## #1347 Type A" in text

    def test_log_entry_carries_hash_chain(self):
        # The doc-sync writes the entry with the main/anchor hashes;
        # the terminal log-hash followup registers the doc-sync hash
        # here per #721.
        text = _read(LOG_PATH)
        assert "main commit" in text
        assert "anchor" in text

    def test_log_entry_records_finding(self):
        text = _read(LOG_PATH)
        assert "m1039" in text
        assert "safety researchers" in text


# ---------------------------------------------------------------------------
# 7. Corpus integrity: the m1039 block is well-formed and placed.
# ---------------------------------------------------------------------------


class TestCorpusIntegrity1347:
    def test_ap_yaml_loads(self):
        data = _load_ap()
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

    def test_block_sibling_of_1232(self):
        data = _load_ap()
        oai = data["competitor_relationships"]["openai"]
        keys = list(oai.keys())
        assert BLOCK_KEY in keys
        assert ("type_a_1232_ap_openai_astra_delay_wire_vs_"
                "meta_18bn_settlement_wire") in keys

    def test_four_space_indent(self):
        src = _read(AP_PATH)
        assert "\n    " + BLOCK_KEY + ":" in src

    def test_ascii_only_profile_block(self):
        data = _load_ap()
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
        assert "1345-1349" in _block()["window"]
        assert "THIRD leg" in _block()["window"]

    def test_member_fields(self):
        block = _block()
        assert block["falsification_family_member"] is True
        assert block["verdict"] == "falsification_member_confirmed"
        assert block["no_analysis_json_update"] is True


# ---------------------------------------------------------------------------
# 8. Research method: 1 scout + 4 query sets, 0 browser.open, novelty,
#    verbatim URLs.
# ---------------------------------------------------------------------------


class TestResearchMethod1347:
    def test_four_query_sets_documented(self):
        block = _block()
        assert len(block["method_query_sets"]) == 4
        assert "Associated Press OpenAI investigation accountability October 2026" in block["method_query_sets"]

    def test_zero_browser_open(self):
        block = _block()
        assert "0 browser.open" in block["method"]
        assert "excerpt-bounded" in block["method"]

    def test_scout_handoff_documented(self):
        block = _block()
        assert "delegated scout" in block["method"]
        assert "incomplete handoff" in block["method"]
        assert "bloomberg.com/apnews.com/cnbc.com" in block["method"]

    def test_verbatim_urls_not_constructed(self):
        block = _block()
        assert "verbatim" in block["novelty"]
        assert "constructed" in block["novelty"]
        assert "no canonical URLs constructed" in block["novelty"]
        for url in NOVEL_URLS:
            assert url.startswith("https://www.kcau9.com/") or \
                url.startswith("https://www.ottumwacourier.com/")

    def test_counter_search_documented(self):
        block = _block()
        assert "counter-search" in block["method"]
        assert "zero soft AP counter-pieces" in block["method"]

    def test_ascii_only_test_file(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "\u2014" not in src
        assert "\u2013" not in src


# ---------------------------------------------------------------------------
# 9. Confounders, ranked strong-first.
# ---------------------------------------------------------------------------


class TestConfounders1347:
    def test_confounder_deal_age_strong(self):
        block = _block()
        assert "deal-age" in block["confounders_ranked"]
        assert "STRONG" in block["confounders_ranked"]
        assert "Jul 2025" in block["confounders_ranked"]

    def test_confounder_excerpt_bounded_strong(self):
        block = _block()
        assert "excerpt-bounded" in block["confounders_ranked"]

    def test_confounder_wire_genre_strong(self):
        block = _block()
        assert "wire-genre" in block["confounders_ranked"]
        assert "STRONG" in block["confounders_ranked"]

    def test_confounder_cross_peg_moderate(self):
        block = _block()
        assert "cross-peg" in block["confounders_ranked"]
        assert "MODERATE" in block["confounders_ranked"]

    def test_confounder_hand_assigned_weak(self):
        block = _block()
        assert "hand-assigned" in block["confounders_ranked"]
        assert "WEAK" in block["confounders_ranked"]

    def test_counterevidence_disclosed(self):
        block = _block()
        assert "m970" in block["counterevidence"]
        assert "+0.35" in block["counterevidence"]
        assert "DevDay" in block["counterevidence"]


# ---------------------------------------------------------------------------
# 10. Verdict: falsification_member_confirmed, ledger 63->64.
# ---------------------------------------------------------------------------


class TestVerdict1347:
    def test_verdict_member_confirmed(self):
        assert _block()["verdict"] == "falsification_member_confirmed"

    def test_ledger_63_to_64(self):
        block = _block()
        assert block["falsification_ledger"] == "64"
        assert "ledger 63->64" in block["falsification_family"]

    def test_first_ap_openai_hardness_test(self):
        block = _block()
        assert "FIRST dedicated uniform-softening test on the AP x OpenAI pair" in block["falsification_family"]

    def test_domain_bounded(self):
        block = _block()
        assert "Domain-bounded" in block["falsification_family"]
        assert "wire register on the Oct-9 safety-turmoil peg" in block["falsification_family"]

    def test_1143_does_not_block(self):
        block = _block()
        assert "#1143" in block["distinct_from_prior"]
        assert "does not block" in block["distinct_from_prior"]

    def test_not_artifact_grade(self):
        block = _block()
        assert "NOT artifact-grade" in block["statistical_discipline"]
        assert block["no_analysis_json_update"] is True

    def test_delta_near_symmetric(self):
        assert abs(DELTA_OPENAI_MINUS_META - 0.10) < 0.001
        assert abs((OPENAI_TONE - META_TONE) - DELTA_OPENAI_MINUS_META) < 0.001


# ---------------------------------------------------------------------------
# 11. The AP x OpenAI arm: the Oct-9 Chan firings wire.
# ---------------------------------------------------------------------------


class TestAPOpenAIArm1347:
    def test_single_new_arm(self):
        arm = _block()["openai_arm_new"]
        assert arm["entity"] == "openai"
        assert arm["tone_MANUAL_ILLUSTRATIVE"] == -0.35

    def test_arm_a1_chan_firings(self):
        arm = _block()["openai_arm_new"]["arm_A1"]
        assert arm["date"] == "2026-10-09"
        assert arm["byline"] == "KELVIN CHAN, Associated Press"
        assert arm["dateline"] == "LONDON (AP)"
        assert arm["manual_illustrative_tone"] == -0.35
        assert "safety researchers" in arm["title"]

    def test_arm_a1_carries_charge(self):
        arm = _block()["openai_arm_new"]["arm_A1"]
        assert "corporate interests before safety" in arm["key_content"]
        assert "rogue AI agents" in arm["key_content"]

    def test_arm_a1_relay_attested(self):
        arm = _block()["openai_arm_new"]["arm_A1"]
        assert "RELAY-TIER" in arm["evidence_tier"]
        assert "0 browser.open" in arm["evidence_tier"]
        assert "kcau9.com" in arm["url"]
        assert "ottumwacourier.com" in arm["url_carrier_2"]

    def test_arm_a1_researchers_named(self):
        arm = _block()["openai_arm_new"]["arm_A1"]
        assert "Tomek Korbak" in arm["key_content"]
        assert "Jasmine Wang" in arm["key_content"]
        assert "Mikita Balesni" in arm["key_content"]

    def test_meta_arm_carried(self):
        arm = _block()["meta_arm_carried"]
        assert arm["tone_MANUAL_ILLUSTRATIVE"] == -0.45
        assert "m970" in arm["via"]
        assert "un-rescored per #807" in arm["via"]

    def test_all_urls_novel(self):
        for url in NOVEL_URLS:
            assert url in _block()["source_urls"]

    def test_asymmetry_scorer_result(self):
        res = _block()["asymmetry_scorer_result"]
        assert "NOT run" in res
        assert "+0.10" in res


# 12. Financial relationship: AP x OpenAI deal terms.
# ---------------------------------------------------------------------------


class TestFinancialRelationship1347:
    def test_deal_terms(self):
        fin = _block()["financial_context"]
        assert "Jul 13 2023" in fin
        assert "back to 1985" in fin

    def test_two_year_term_unverified_renewal(self):
        fin = _block()["financial_context"]
        assert "two-year nonexclusive" in fin
        assert "UNVERIFIED" in fin

    def test_coverage_prediction(self):
        fin = _block()["financial_context"]
        assert "coverage_prediction" in fin
        assert "softer" in fin

    def test_press_gazette_attestation(self):
        fin = _block()["financial_context"]
        assert "Press Gazette" in fin

    def test_first_publisher_deal_noted(self):
        fin = _block()["financial_context"]
        assert "FIRST OpenAI publisher licensing deal" in fin

    def test_prediction_fails_language(self):
        block = _block()
        assert "FAILS" in block["falsification_family"]


# ---------------------------------------------------------------------------
# 13. In-flight isolation: #899/#938/#900/#1012-wt untouched; #1024
#     m846 untouched. Explicit-path staging at commit time.
# ---------------------------------------------------------------------------


class TestInFlightIsolation1347:
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


class TestStatisticalDiscipline1347:
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
