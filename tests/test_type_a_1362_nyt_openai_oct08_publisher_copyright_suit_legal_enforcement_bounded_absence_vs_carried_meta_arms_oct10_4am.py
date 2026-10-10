# -*- coding: utf-8 -*-
"""Type A #1362: NYT x OpenAI Oct-8-2026 publisher-copyright-suit
legal-enforcement bounded absence (selection asymmetry vs carried NYT x
Meta arms).

The Oct-8-2026 USA TODAY Co. v OpenAI publisher-copyright suit (SDNY
1:26-cv-08892; fourteen Gannett-related plaintiffs; 19 publications;
79-page complaint; three causes of action - direct copyright
infringement 17 USC 501, vicarious infringement, intentional DMCA 1202
CMI removal, the same three claims that remain in the NYT's own suit;
>$250M sought plus model/training-set destruction; GPT-5.6 output
exhibits; statement of relatedness to the consolidated OpenAI copyright
MDL; plaintiffs' counsel Steven Lieberman; the Gannett complaint cites
the NYT's own unsealed summary-judgment motion; Reuters wire same day)
draws ZERO NYT originals inside a ~60-row bounded surface (1 delegated
scout: 10 searches, ~40 rows, three site:nytimes.com queries with two
returning literally "No results found"; 3 main-run browser.search
verification sets, ~22 rows; zero nytimes.com URLs; zero NYT bylines;
zero NYT-hosted wires; 0 browser.open per #503, excerpt-bounded).

The structural contrast runs opposite to #1357 (FT leg, m1044): the NYT
is OpenAI's ADVERSARIAL plaintiff (Dec 2023, billions sought,
coverage_prediction "adversarial") and the m471 boundary condition
predicts adversarial posture inside the litigation domain - yet the
newsroom shows no indexed original on a fellow publisher's suit against
its own litigation adversary. The same publication selects Meta
legal/enforcement pegs in the carried arms (Aug-18-2026 memo-sourced
ICE-ban-on-Meta-glasses investigative, -0.30; carried un-rescored per
#807; the Sep-23 Connect relay at +0.10 bounds any uniform
Meta-adversarial read).

The cross-publication pattern is the finding: the FT (licensed partner,
m1044) and the NYT (adversarial plaintiff, this run) BOTH show bounded
absence on the same peg - the selection absence is NOT predicted by the
financial-relationship gradient in either direction. This is a SYMMETRIC
boundary condition: it bounds the m471 adversarial-posture prediction to
the tone axis (the NYT's own lawsuit-domain language IS adversarial)
and documents that the Oct-8 publisher-suit peg draws bounded absence at
both ends of the posture gradient. Verdict mechanism_documented - NOT a
falsification-family member; the finding bounds rather than tests the
theory. Ledger holds at 64; no sixty-fifth member.

Type A lands one mechanism: m1045 in profiles/nytimes.yaml under
competitor_relationships/openai (4-space indent, sibling of the m471 /
m724 blocks, ahead of the meta: section); max numeric mechanism_id
1044->1045; next 1046; ledger holds at 64 (the sixty-fourth member
stays m1039 ap.yaml; the sixty-fifth member-claim form stays absent
repo-wide).

Research method: 1 delegated scout (10 searches, ~40 rows; scout
returned raw verbatim URLs WITHOUT novelty characterization per the
#1341 post-hoc lesson - the main run verified corpus novelty via git
grep -F) + 3 main-run browser.search verification sets (site:nytimes.com
scoped sweep - attesting, 0 results; NYT-coverage sweep - attesting, 8
rows, zero nytimes.com URLs; nytimes.com comparison sweep - attesting, 7
rows, zero nytimes.com URLs), 0 browser.open per #503. Pre-commit
novelty greps: zero test_type_a_1362 files on disk (glob); no Type A
#1362 in git log (--grep); max numeric mechanism_id 1044 in profiles/
pre-commit; zero numeric/underscore/dash next-number one-zero-four-five
mechanism key forms in profiles/ + tests/ pre-commit (needles
format-built per #715, own file excluded, verified clean by direct
sweep); 7 novel verbatim source URLs zero-hit repo-wide pre-commit (git
grep -F; the Reuters Oct-8 wire, dig.watch, and unite.ai URLs are
in-corpus via test_type_c_1329/#1357; the chatgptiseatingtheworld.com
deep dive, p4sc4l.substack, and rightstech.substack URLs are in-corpus
via competitor-entities.yaml); block key zero-hit repo-wide pre-commit
(git grep -F; designed keying: iteration 1362 in key, no 1045 or
one-zero-four-five substring); "## #1362" zero-hit in iteration-log
pre-commit; README stats 78988/1686 pre-commit; no #1362 row in
README/ARCHITECTURE test tables pre-commit; "publisher-copyright-suit
legal-enforcement bounded absence" NYT-leg framing zero-hit repo-wide
pre-commit. All URLs copied verbatim from the browser.search Full-URL
listings, NOT constructed. ASCII-only, no em dashes.

This run is the THIRD leg of the 1360-1364 window (D #1360 -> E #1361
-> A #1362 -> B #1363 -> C #1364 per the #565 anchor + rotation guard);
the 1355-1359 window is VERIFIED CLOSED. The next background-suite
verdict belongs to #1365 per #795 (the #1360-launched suite, goal
hidden_files type_d_1360_full_suite.log; this run CHECKS it only).

Anchor convention per #565: ANCHORED_SHA starts as 0*40 in this
pre-commit file and is patched to the main-commit hash in the anchor
followup commit. One anchor test (the placeholder pin) fails BY DESIGN
post-anchor.

Do NOT touch #1024 (m846 in profiles/competitor-entities.yaml), #899
(nytimes.yaml m771 hunk), #938 (Type B test file working-tree edit),
#900 (untracked Type D test file), #1012-wt (working-tree edit on the
committed Type A #1012 file). This run appends its m1045 hunk to
profiles/nytimes.yaml (which also carries the in-flight #899 m771
hunk) - stage ONLY the m1045 hunk via a filtered patch applied with
git apply --cached; never stage the whole file.

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
NYT_PATH = os.path.join(PROFILES_DIR, "nytimes.yaml")

OWN_BASENAME = (
    "test_type_a_1362_nyt_openai_oct08_publisher_copyright_suit_"
    "legal_enforcement_bounded_absence_vs_carried_meta_arms_oct10_4am.py"
)

# Patched per #565 in the anchor followup (main commit sha).
ANCHORED_SHA = "330f55d0660e3b7686c8abb07b64f5310845b3b8"  # patched to the main-commit sha in the anchor followup per #565

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

MECH_NUM = 1045
NEXT_NUM = 1046  # integer only; key-form needles are format-built

# Predecessor chain: #1361 Type E SECOND leg of the 1360-1364 window.
PRED_MAIN_1361 = "790f4f7469e34dd5197628db5bd34c2ccd80bbeb"
PRED_ANCHOR_1361 = "bb07ccbd"
PRED_DOCSYNC_1361 = "fc74675b"

# This run's main commit (full sha), for the ancestor-form
# no-Type-A-#1362 pin. Staged 0*40 placeholder-only per #721;
# re-pinned in the anchor followup per #721 (PRED_MAIN_1362 re-pinned
# in BOTH this file and the #1361 file per the #1292 precedent).
PRED_MAIN_1362 = "330f55d0660e3b7686c8abb07b64f5310845b3b8"

# #1363's main commit (full sha), for the ancestor-form no-Type-B-#1363
# pin. Staged 0*40 placeholder-only per #721; re-pinned in #1363's
# terminal log-hash followup per #721. (Type-correct per the #1352
# type-mismatch lesson: #1363 is Type B, so the pin greps
# "Type B #1363".)
PRED_MAIN_1363 = "0" * 40

# The #1361 window-predecessor file, for the staleness pin on its
# guard-lifecycle class (max id 1043; zero next-number
# one-zero-four-five / no-Type-A-#1362-in-git-log / fortieth
# direction absent / forty-eighth through sixty-fourth members
# intact / no sixty-fifth member / ledger holds at 64).
B1361_FILE = (
    "test_type_e_1361_podcast_sentiment_195th_"
    "verification_oct10_4am.py"
)

# Doc-sync constants per #719: post-doc-sync values from the start.
# Patched pre-main once the in-gate collection count is known.
README_TEST_COUNT = 79085  # post-doc-sync total (pre-sync 78988 + 97) - PATCHED post-collection
README_FILE_COUNT = 1687  # pre-sync 1686 + 1 (this file)

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
# (landed #1347 in profiles/ap.yaml, m1039).
_T64 = "SIXT" + "Y-FOURTH falsification-family member"
# The sixty-fifth member-claim form is fragment-built per #715
# (no sixty-fifth member may exist repo-wide).
_T65 = "SIXT" + "Y-FIFTH falsification-family member"

BLOCK_KEY = (
    "type_a_1362_nyt_openai_oct08_publisher_copyright_suit_"
    "legal_enforcement_bounded_absence_vs_carried_meta_arms"
)

# Novel verbatim source URLs this run (zero-hit repo-wide pre-commit,
# verified via git grep -F; copied verbatim from the browser.search
# Full-URL listings, NOT constructed). The Reuters Oct-8 wire,
# dig.watch, and unite.ai URLs are in-corpus via test_type_c_1329 /
# #1357; the chatgptiseatingtheworld.com deep dive, p4sc4l.substack,
# and rightstech.substack URLs are in-corpus via competitor-entities.yaml.
NOVEL_URLS = [
    "https://www.wkyufm.org/2026-10-09/usa-today-network-including-courier-journal-sue-openai",
    "https://chatgptiseatingtheworld.substack.com/p/usa-today-sues-openai-in-yet-another",
    "https://cryptobriefing.com/usa-today-sues-openai-copyright-250m/",
    "https://trademarklawyermagazine.com/usa-today-newspapers-sue-openai-for-more-than-250-million-over-ai-training/",
    "https://fourweekmba.com/ai-usa-today-co-sues-openai-seeks-over-250m-for-19-papers/",
    "https://www.reuters.com/legal/litigation/openai-new-york-times-case-tees-up-key-test-ai-training-under-copyright-law-2026-09-08/",
    "https://techxplore.com/news/2026-09-sides-openai-york-copyright-lawsuit.html",
]

# 3 main-run browser.search query sets + 1 delegated scout this run
# (0 browser.open per #503).
QUERY_SETS = [
    "site:nytimes.com OpenAI Gannett \"USA Today\" copyright lawsuit",
    "New York Times coverage \"USA Today\" sues OpenAI copyright October 2026",
    "nytimes.com OpenAI October 2026 copyright lawsuit Meta comparison",
]


def _load_nyt():
    with open(NYT_PATH, encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def _block():
    data = _load_nyt()
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
#    + rotation guard: THIRD leg of the 1360-1364 window.
# ---------------------------------------------------------------------------


class TestAnchor1362:
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
        assert "THIRD leg of the 1360-1364 window" in src

    def test_1350_1354_window_closed(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "1355-1359" in src
        assert "VERIFIED CLOSED" in src

    def test_next_leg_is_1363_type_b(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "B #1363" in src


# ---------------------------------------------------------------------------
# 2. Mechanism novelty: Type A lands one mechanism (m1045; max 1045).
# ---------------------------------------------------------------------------


class TestMechanismNovelty1362:
    def test_max_numeric_mechanism_id_1045(self):
        # Post-landing form: the m1045 block is in the working tree
        # pre-commit (landed before the in-gate run). Deselected in
        # the in-gate run (fails pre-landing by design).
        assert _max_numeric_mechanism_id() == MECH_NUM

    def test_no_type_a_1362_in_git_log_pin(self):
        # Post-main-commit form (the #1191-class self-trip, re-pinned
        # in the anchor followup per #721): every commit whose message
        # matches "Type A #1362" must be this run's main commit or a
        # descendant of it - i.e., no PRIOR run committed this run's
        # iteration. Deselected in the in-gate run (fails pre-commit
        # by design).
        out = _git("log", "--format=%H", "--grep=Type A #1362")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected this run's own commits"
        main = _git("rev-parse", PRED_MAIN_1362).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_zero_next_number_keys_all_forms(self):
        # Numeric (profiles/ scope), underscore and dash (profiles/ +
        # tests/ scope, own file excluded per #715). Holds pre-commit
        # and post-commit (Type A lands one mechanism, the 1045
        # pins stay green).
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_block_key_designed_no_1044_1045_substring(self):
        # Per #723/#738/#739: the iteration-form block key carries no
        # underscore-form one-zero-four-five / one-zero-four-six
        # mechanism key substring (needle format-built per #770 so
        # this file carries no contiguous literal).
        for n in (MECH_NUM, NEXT_NUM):
            needle = "%s%d" % (MECH_ID_MARKER, n)
            assert needle not in BLOCK_KEY
        assert "1362" in BLOCK_KEY
        assert BLOCK_KEY in _read(NYT_PATH)

    def test_block_key_in_nytimes_openai_section(self):
        # Post-landing form: the m1045 block sits under
        # competitor_relationships.openai in profiles/nytimes.yaml.
        # Deselected in the in-gate run (fails pre-landing by design).
        data = _load_nyt()
        oai = data["competitor_relationships"]["openai"]
        assert BLOCK_KEY in oai
        assert oai[BLOCK_KEY]["mechanism_id"] == MECH_NUM

    def test_novel_urls_zero_hit_pre_commit(self):
        # The source URL was verified zero-hit pre-commit
        # (git grep -F, documented in the block's novelty field). This
        # test pins that no file OTHER than this run's own m1045
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
                "profiles/nytimes.yaml",
                "tests/" + OWN_BASENAME,
            }, (url, paths)

    def test_forward_guards_for_1363(self):
        # max-1045; zero-1046 all forms; fortieth direction absent
        # (profiles/ scope); forty-eighth through sixty-fourth members
        # intact; no sixty-fifth member (repo-wide); ledger holds
        # at 64 (m1045 is mechanism_documented, NOT a member).
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 1045" in src
        assert "NEXT_NUM = 1046" in src
        assert "ledger holds at 64" in src
        assert _git_grep_tracked_source(_T40, "profiles/") == []
        assert _git_grep_tracked_source(_T48, "profiles/") == [
            "profiles/financial-times.yaml"]
        # The sixty-fourth form is referenced in ap.yaml (the member,
        # m1039) and in wired.yaml (the m1042 block's
        # falsification_family cross-reference) at HEAD.
        assert set(_git_grep_tracked_source(_T64, "profiles/")) == {
            "profiles/ap.yaml", "profiles/wired.yaml"}
        assert _git_grep_tracked_source(_T65, None) == []

    def test_distinct_from_prior(self):
        # Not a re-score of m1044 (#1362's sister leg: FT x OpenAI on
        # the SAME suit peg, bounded absence, mechanism_documented) -
        # this is the cross-publication replication from the opposite
        # posture; not m471 (#471, NYT x OpenAI litigation-posture
        # boundary condition, TONE axis); not m1036 (#1342, Times x
        # OpenAI safety cluster, different publication); not m1039
        # (#1347, AP x OpenAI firings wire, different publication,
        # tone axis). The #1143 temporal-replication precedent does
        # not block: fresh publication+posture (NYT adversarial
        # plaintiff) on the selection axis, not a re-score.
        block = _block()
        assert "m1044" in block["distinct_from_prior"]
        assert "m471" in block["distinct_from_prior"]
        assert "m1036" in block["distinct_from_prior"]
        assert "m1039" in block["distinct_from_prior"]
        assert "#1143" in block["distinct_from_prior"]


# ---------------------------------------------------------------------------
# 3. Guard lifecycle: forward pins for #1363; #1362 stages the
#    #1191-class no-Type-B-#1363 self-trip (re-pinned post-commit
#    per #721). Type-correct per the #1352 type-mismatch lesson.
# ---------------------------------------------------------------------------


class TestGuardLifecycle1362:
    def test_pins_on_one_mechanism_landing(self):
        # Type A lands one mechanism: max 1045, next 1046.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 1045" in src
        assert "NEXT_NUM = 1046" in src

    def test_no_type_b_1363_in_git_log_pin(self):
        # Post-main-commit form for the NEXT leg (the #1191-class
        # self-trip, re-pinned in #1363's terminal log-hash followup
        # per #721): every commit whose message matches "Type B
        # #1363" must be #1363's main commit or a descendant of it.
        # Deselected in the in-gate run (fails pre-commit by design).
        out = _git("log", "--format=%H", "--grep=Type B #1363")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1363's own commits"
        main = _git("rev-parse", PRED_MAIN_1363).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_1046_numeric_absent_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_1046_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_1046_dash_absent_repo_wide(self):
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

    def test_sixty_fourth_member_present_pin(self):
        # The sixty-fourth member-claim form is committed at HEAD
        # (landed #1347, m1039, profiles/ap.yaml).
        out = _git(
            "grep", "-c", "-F", _T64, "HEAD", "--",
            "profiles/ap.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_no_sixty_fifth_member_pin(self):
        # m1045 is mechanism_documented, NOT a member: the
        # sixty-fifth member-claim form stays absent repo-wide.
        assert _git_grep_tracked_source(_T65, "profiles/") == []
        assert _git_grep_tracked_source(_T65, "tests/") == []

    def test_ledger_holds_at_64_pin(self):
        block = _block()
        assert block["falsification_ledger"] == "64"
        assert block["ledger"] == "64"
        assert "Ledger holds at 64" in block["falsification_family"]


# ---------------------------------------------------------------------------
# 4. Staleness pins: #1361's guard lifecycle flips BY DESIGN post-commit.
# ---------------------------------------------------------------------------


class TestStalenessPins1362:
    def test_1361_guard_lifecycle_post_commit_expiry(self):
        # Post-terminal-followup form: 25 tests in the class; 24
        # pass, 1 fails BY DESIGN - ONE #1272-class forward-guard
        # expiry (test_1045_numeric_absent_in_profiles trips on the
        # landed m1045 block in profiles/nytimes.yaml; the max-1044
        # pins stay green because they assert the file's own
        # constants, and the 1045-underscore/dash pins stay green -
        # no one-zero-four-five mechanism-key forms landed).
        # The no_type_a_1362_in_git_log ancestor pin (the #1191-class
        # self-trip) was red at this run's main-commit time; the
        # terminal log-hash followup re-pinned PRED_MAIN_1362 in BOTH
        # its own file's copy and the #1361 predecessor file's copy
        # per the #1292 re-pin-both-copies precedent and the #721
        # re-pin rule, flipping it green. The forty-eighth through
        # sixty-fourth member pins stay green; the no-sixty-fifth pin
        # stays green (m1045 is not a member); the ledger-holds-at-64
        # pin stays green.
        # Deselected in the in-gate run (fails pre-commit by design);
        # verified post-terminal.
        res = _class_run(B1361_FILE, "TestGuardLifecycle1361")
        out = res.stdout + res.stderr
        assert "1 failed, 24 passed" in out, out[-2000:]


# ---------------------------------------------------------------------------
# 5. Doc-sync per #719 (deselected pre-commit, flipped post-sync).
# ---------------------------------------------------------------------------


class TestDocSync1362:
    def test_readme_test_file_table_has_1362_row_post_sync(self):
        readme = _read(README_PATH)
        assert "test_type_a_1362" in readme

    def test_architecture_has_1362_row_post_sync(self):
        arch = _read(ARCH_PATH)
        assert "test_type_a_1362" in arch

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


class TestIterationLog1362:
    def test_log_has_1362_entry(self):
        text = _read(LOG_PATH)
        assert "## #1362 Type A" in text

    def test_log_entry_carries_hash_chain(self):
        # The doc-sync writes the entry with the main/anchor hashes;
        # the terminal log-hash followup registers the doc-sync hash
        # here per #721.
        text = _read(LOG_PATH)
        assert "main commit" in text
        assert "anchor" in text

    def test_log_entry_records_finding(self):
        text = _read(LOG_PATH)
        assert "m1045" in text
        assert "bounded absence" in text


# ---------------------------------------------------------------------------
# 7. Corpus integrity: the m1045 block is well-formed and placed.
# ---------------------------------------------------------------------------


class TestCorpusIntegrity1362:
    def test_nyt_yaml_loads(self):
        data = _load_nyt()
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
            "financial_context", "posture_url", "statistical_discipline",
            "method", "method_query_sets", "research_method",
            "novelty", "source_urls", "no_analysis_json_update",
            "concurrency", "status",
        ):
            assert field in block, field

    def test_block_sibling_of_m471(self):
        data = _load_nyt()
        oai = data["competitor_relationships"]["openai"]
        keys = list(oai.keys())
        assert BLOCK_KEY in keys
        assert "nyt_openai_litigation_posture_boundary_condition_471" \
            in keys

    def test_four_space_indent(self):
        src = _read(NYT_PATH)
        assert "\n    " + BLOCK_KEY + ":" in src

    def test_ascii_only_profile_block(self):
        data = _load_nyt()
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
        assert "1360-1364" in _block()["window"]
        assert "THIRD leg" in _block()["window"]

    def test_not_a_member_fields(self):
        block = _block()
        assert block["falsification_family_member"] is False
        assert block["verdict"] == "mechanism_documented"
        assert block["no_analysis_json_update"] is True


# ---------------------------------------------------------------------------
# 8. Research method: 1 scout + 3 query sets, 0 browser.open, novelty,
#    verbatim URLs, bounded-absence surface.
# ---------------------------------------------------------------------------


class TestResearchMethod1362:
    def test_three_query_sets_documented(self):
        block = _block()
        assert len(block["method_query_sets"]) == 3
        assert "site:nytimes.com OpenAI Gannett" in \
            block["method_query_sets"][0]

    def test_zero_browser_open(self):
        block = _block()
        assert "0 browser.open" in block["method"]
        assert "excerpt-bounded" in block["method"]

    def test_scout_handoff_documented(self):
        block = _block()
        assert "delegated scout" in block["research_method"]
        assert "raw verbatim URLs WITHOUT novelty characterization" in \
            block["research_method"]
        assert "#1341 post-hoc lesson" in block["research_method"]

    def test_verbatim_urls_not_constructed(self):
        block = _block()
        assert "verbatim" in block["novelty"]
        assert "constructed" in block["novelty"]
        assert "NOT constructed" in block["method"]
        for url in NOVEL_URLS:
            assert url.startswith("https://")
            assert " " not in url

    def test_bounded_absence_surface_documented(self):
        block = _block()
        assert "bounded surface" in block["finding"]
        assert "~60-row" in block["finding"]
        assert "zero nytimes.com URLs" in block["openai_arm_new"][
            "bounded_surface"]

    def test_site_nyt_scoped_zero_results(self):
        # The site:nytimes.com scoped queries returned "No results
        # found" - the sharpest bounded-absence signal this run.
        block = _block()
        assert "site:nytimes.com" in block["method_query_sets"][0]
        assert "No results found" in block["openai_arm_new"][
            "bounded_surface"]

    def test_ascii_only_test_file(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "\u2014" not in src
        assert "\u2013" not in src


# ---------------------------------------------------------------------------
# 9. Confounders, ranked strong-first.
# ---------------------------------------------------------------------------


class TestConfounders1362:
    def test_confounder_church_state_recusal_strong(self):
        # Pre-registered in m471: the NYT newsroom historically limits
        # coverage of Times Company litigation as an interested party;
        # the Gannett complaint cites the NYT's own unsealed
        # summary-judgment motion, putting the newsroom inside the
        # story. The absence may be recusal, not softening.
        block = _block()
        assert "Church-state/self-coverage recusal" in block[
            "confounders_ranked"]["strong"][0]
        assert "m471" in block["confounders_ranked"]["strong"][0]

    def test_confounder_excerpt_bounded_strong(self):
        block = _block()
        assert "Excerpt-bounded" in block["confounders_ranked"]["strong"][1]

    def test_confounder_tag_along_moderate(self):
        block = _block()
        assert "Tag-along" in block["confounders_ranked"]["moderate"][0]

    def test_confounder_wire_sufficiency_moderate(self):
        block = _block()
        assert "Wire-sufficiency" in block["confounders_ranked"][
            "moderate"][1]

    def test_confounder_illustrative_tones_weak(self):
        block = _block()
        assert "Illustrative" in block["confounders_ranked"]["weak"][0]


# ---------------------------------------------------------------------------
# 10. Verdict: mechanism_documented, not a member, ledger holds at 64.
# ---------------------------------------------------------------------------


class TestVerdict1362:
    def test_verdict_mechanism_documented(self):
        assert _block()["verdict"] == "mechanism_documented"

    def test_not_a_falsification_member(self):
        block = _block()
        assert block["falsification_family_member"] is False
        assert "NOT a falsification-family member" in block[
            "falsification_family"]

    def test_ledger_holds_at_64(self):
        block = _block()
        assert block["falsification_ledger"] == "64"
        assert block["ledger"] == "64"

    def test_no_sixty_fifth_member_claimed(self):
        block = _block()
        assert "sixty-fifth member-claim form stays absent repo-wide" in \
            block["ledger_note"]

    def test_bounds_m471(self):
        # The finding bounds rather than extends the m471
        # adversarial-posture prediction: m471 predicts adversarial
        # TONE within the litigation domain; this run documents that
        # the Oct-8 publisher-suit peg draws bounded absence on the
        # SELECTION axis at both ends of the posture gradient (FT
        # licensed partner m1044, NYT adversarial plaintiff m1045).
        block = _block()
        assert "BOUNDS the m471" in block["falsification_family"]

    def test_no_analysis_json_update(self):
        assert _block()["no_analysis_json_update"] is True


# ---------------------------------------------------------------------------
# 11. Arms: the Oct-8 publisher-suit peg (zero FT originals) vs carried
#     FT x Meta accountability arms.
# ---------------------------------------------------------------------------


class TestNYTOpenAILegalEnforcementArms1362:
    def test_suit_peg_attested(self):
        block = _block()
        arm = block["openai_arm_new"]
        assert "1:26-cv-08892" in arm["peg"]
        assert "Oct 8 2026" in arm["peg"]
        assert "in excess of $250 million" in arm["detail"]
        assert "79-page" in arm["detail"]

    def test_zero_nyt_originals(self):
        block = _block()
        assert block["openai_arm_new"]["nyt_originals"] == 0
        assert "zero nytimes.com URLs" in block["openai_arm_new"][
            "bounded_surface"]

    def test_covered_by_attests_peg(self):
        block = _block()
        covered = block["openai_arm_new"]["covered_by"]
        assert "Reuters Oct-8 wire" in covered
        assert "test_type_c_1329" in covered
        assert "The Verge covered the suit" in covered

    def test_carried_meta_arms(self):
        block = _block()
        arms = block["meta_arm_carried"]["arms"]
        assert len(arms) == 2
        assert arms[0]["manual_illustrative_tone"] == -0.30
        assert arms[1]["manual_illustrative_tone"] == 0.10

    def test_ice_ban_arm_is_enforcement_register(self):
        block = _block()
        arms = block["meta_arm_carried"]["arms"]
        assert arms[0]["framing"] == "enforcement_register_memo_sourced"
        assert "2026/08/18" in arms[0]["url"]

    def test_selection_delta_documented(self):
        block = _block()
        assert "0 of 1" in block["asymmetry_scorer_result"]

    def test_tone_not_scored(self):
        block = _block()
        assert "NOT_SCORED" in block["asymmetry_scorer_result"]

    def test_scorer_engine_not_run(self):
        block = _block()
        assert "Engine NOT run" in block["asymmetry_scorer_result"]


# ---------------------------------------------------------------------------
# 12. Financial relationship: NYT x OpenAI adversarial posture context.
# ---------------------------------------------------------------------------


class TestFinancialRelationship1362:
    def test_adversarial_posture_attested(self):
        block = _block()
        assert "Dec 2023" in block["financial_context"]
        assert "billions sought" in block["financial_context"]

    def test_no_licensing_deal(self):
        block = _block()
        assert "no licensing deal" in block["financial_context"]

    def test_coverage_prediction_adversarial(self):
        block = _block()
        assert 'coverage_prediction "adversarial"' in block[
            "financial_context"]

    def test_meta_zero_licensing(self):
        block = _block()
        assert "$0 licensing" in block["financial_context"]

    def test_posture_url_verbatim(self):
        block = _block()
        assert block["posture_url"] == (
            "https://www.nytimes.com/2023/12/27/business/media/"
            "new-york-times-open-ai-microsoft-lawsuit.html"
        )

    def test_symmetric_boundary_documented(self):
        # The peg draws bounded absence at BOTH ends of the posture
        # gradient: FT licensed partner (m1044) and NYT adversarial
        # plaintiff (m1045).
        block = _block()
        assert "both ends of the posture gradient" in block[
            "financial_context"]
        assert "m1044" in block["financial_context"]


# ---------------------------------------------------------------------------
# 13. In-flight isolation: #899/#938/#900/#1012-wt and #1024 untouched.
# ---------------------------------------------------------------------------


class TestInFlightIsolation1362:
    def test_in_flight_listed(self):
        block = _block()
        for tag in ("#899", "#938", "#900", "#1012-wt", "#1024"):
            assert tag in block["concurrency"]

    def test_nytimes_hunk_isolation(self):
        # profiles/nytimes.yaml carries this run's m1045 hunk (staged
        # via a filtered patch, git apply --cached, so the in-flight
        # #899 m771 hunk never entered this run's index) alongside the
        # still-uncommitted #899 hunk. Isolation proof: the main
        # commit's nytimes.yaml diff is a pure addition (zero removed
        # lines) containing BLOCK_KEY, and the #899 block key remains
        # present in the working-tree file unmodified.
        assert BLOCK_KEY in _read(NYT_PATH)
        assert "spur_licensing_market_exists_coalition_founder_datum" in \
            _read(NYT_PATH)
        main = _git("rev-parse", PRED_MAIN_1362).stdout.strip()
        assert len(main) == 40 and main != "0" * 40
        out = _git("show", main, "--format=", "--",
                   "profiles/nytimes.yaml").stdout
        assert BLOCK_KEY in out
        removed = [l for l in out.splitlines()
                   if l.startswith("-") and not l.startswith("---")]
        assert removed == [], removed[:5]

    def test_competitor_entities_untouched(self):
        out = _git("status", "--short")
        assert "profiles/competitor-entities.yaml" not in out.stdout

    def test_only_expected_paths_dirty(self):
        # git status --short prefixes each path with a 3-char status
        # field (" M " / "?? "); slice the RAW line, not the
        # stripped one (stripping first shifts the slice).
        out = _git("status", "--short").stdout
        allowed = {
            "profiles/nytimes.yaml",
            "tests/" + OWN_BASENAME,
        }
        in_flight = {
            "tests/test_type_a_1012_mittr_anthropic_sep2026_doomer_turn_agenda_setting_register_vs_carried_meta_india_havoc_m817_pairing_sep26_7am.py",
            "tests/test_type_b_938_dominic_preston_verge_pixel_watch_gemini_personalization_vs_meta_luna_stigma_sep16.py",
            "tests/test_type_d_900_m769_qualitative_corpus_integrity_sep21_1pm.py",
        }
        for raw in out.splitlines():
            if not raw.strip():
                continue
            path = raw[3:]
            assert path in allowed or path in in_flight, path


# ---------------------------------------------------------------------------
# 14. Statistical discipline: MANUAL / QUALITATIVE ONLY.
# ---------------------------------------------------------------------------


class TestStatisticalDiscipline1362:
    def test_manual_qualitative_only(self):
        block = _block()
        assert "MANUAL" in block["statistical_discipline"]
        assert "QUALITATIVE ONLY" in block["statistical_discipline"]

    def test_no_p_values(self):
        block = _block()
        assert "NOT_CALCULATED" in block["statistical_discipline"]

    def test_not_significant(self):
        block = _block()
        assert "is_significant false" in block["statistical_discipline"]

    def test_not_artifact_grade(self):
        block = _block()
        assert "NOT artifact-grade" in block["statistical_discipline"]

    def test_correlation_not_causation(self):
        block = _block()
        assert "Correlation is not causation" in block[
            "statistical_discipline"]
        assert "hypothesis-generating only" in block[
            "statistical_discipline"]
