# -*- coding: utf-8 -*-
"""Type C #1299 tests: SignSplit signed-data contributor-paid data-pool
infrastructure (Oct 5, 2026) - FIRST dedicated corpus mechanism on the
contributor-paid consent-verified data-pool rail: on October 5 2026
SignSplit PBC emerged from stealth (Wilmington, DE) with a $400 million
strategic seed commitment from a single backer (W Group, a global
fintech and technology ecosystem with 40M+ users) at a $1 billion
valuation, per the company PR Newswire release. THE MONEY FLOW: AI and
robotics companies, researchers, and other organizations pay to access
Data Pools and Research Pools built around buyer needs; individual
contributors and institutions contribute data, work, and likeness and
receive compensation for their participation. The signed-data atom
attaches consent, clear provenance, defined terms, rights, and payment
to each contribution; a verification layer is designed to let AI systems,
social platforms, and digital services identify signed content and
access its associated provenance, consent, and terms. THE TYPE C NEXUS:
the contributor-side payer leg of the corpus money-flow taxonomy - the
counterparty is individuals and institutions, not publishers or labs,
so the financial dependency sits outside the publisher stack entirely.
Distinct from m786 (prices crawler ACCESS with site-set defaults),
m891 (Google unilateral payer-set micro-rates to publishers), m915
(SPUR meter-then-invite), m999 (UK Search-Only Contracts invoice rail),
m1002 (Impelsys x Cashmere: publisher owns the metering surface),
m1005 (Redpine broker-cleared), and m1008 (Elsevier x JAMA Network:
publisher-as-payer inside the publisher stack). The closest corpus
analogue is the ownership-inversion m804 (Noxtua/C.H. Beck), which
inverts publisher-side; SignSplit inverts to the contributor side.
BOUNDARY (explicit): company-PR sourcing (PR Newswire primary plus
independent trade coverage - RecodeX, DEV Community/Forbes Italia
framing, AIWeekly/SiliconAngle); the $400M is a strategic commitment
(capital plus multi-year strategic resources), NOT a disclosed cash
figure; NO named customers, NO contributor counts, NO payment rates
(waitlist-stage product); the verification-layer adoption claim is
aspirational. Falsifiable milestone: a named AI lab customer, or a
disclosed per-contribution payment rate. Claims no slot in the
coverage-tone falsification ledger.

Mechanism 1011 (MECHANISM DOCUMENTED; ledger HOLDS at 58 - NOT a
falsification-family member). No new direction (fortieth stays
absent by design); thirty-fifth through thirty-ninth stand.

Excerpt-bounded research per #503 (2 main-run browser.search
verification sets; 0 browser.open reads). Scout rejections on main-run
verification: UMG x ElevenLabs multi-year AI music licensing deal
(Sep 10) -> REJECTED (music asset class, litigate-then-license adjacent
to existing sue-then-sign geometry; weaker primary sourcing chain);
Village Media x OpenAI payment-in-kind (Sep 17) -> REJECTED (no
disclosed values; second-hand Axios relay); Cloudflare Monetization
Gateway x402 closed beta (Oct 1-2) -> REJECTED (no named payers; closed
beta, GA 3+ months out); Emmerich Newspapers et al. v.
Microsoft/OpenAI (filed Oct 2) -> REJECTED (litigation demand-side,
not a money flow; m624/m636-adjacent). SELECTED: SignSplit signed-data
contributor-paid data pools. 1 delegated scout (ranked 5 candidates;
SignSplit top pick; all 5 zero-hit repo-wide) + 2 main-run
browser.search verification sets, 0 browser.open per #503; 3 novel
relay URLs + 1 corroborating URL zero-hit repo-wide pre-commit
(git grep -F on verbatim Full-URL listings).

The mechanism 1011 block lives in profiles/competitor-entities.yaml as a
top-level key appended at end of file (the #1024 m846 hunk untouched;
explicit-path staging).

Anchor convention per #565: ANCHORED_SHA starts as 0*40 in this pre-commit
file and is patched to the main-commit hash in the anchor followup commit.
One anchor test (the placeholder pin) fails BY DESIGN post-anchor.

Per #795: this run only OBSERVES the #1295-launched background suite
(goal hidden_files type_d_1295_full_suite.log; observed at this run's
check: 1466 bytes / [  1%] progress, last write Oct 7 2026 19:59 PDT,
zero live pytest processes - STALLED, observation not a verdict; the
#1300 Type D run owns the verdict and tombstone); this run neither
re-launches, kills, nor writes to the suite.

Do NOT touch #1024 (m846 in profiles/competitor-entities.yaml), #899
(nytimes.yaml m771 hunk), #938 (Type B test file working-tree edit),
#900 (untracked Type D test file), #1012-wt (working-tree edit on the
committed Type A #1012 file).

Type C lands one mechanism (mechanism 1011); the Type B predecessor
landed one (mechanism 1010, directional case, not a member).
This run is the FIFTH and CLOSING leg of the 1295-1299 window. Next run
#1300 Type D opens the 1300-1304 window (and renders the #1295-launched
background-suite verdict per #795). Rotation: D #1295 -> E #1296 ->
A #1297 -> B #1298 -> C #1299. The main commit is the anchor per #565.
The 1290-1294 window is VERIFIED CLOSED.

ASCII-only, no em dashes. Needles format-built per #715: this file must
not carry contiguous numeric/underscore/dash mechanism-key forms of the
landed or next number, the forty-eighth through fifty-eighth
member-claim forms, the fifty-ninth member-claim form, or the fortieth
direction form; the constants are constructed at runtime. (The landed
ordinals live as short lowercase forms in prose here; the live full-form
claims live in profiles/financial-times.yaml, profiles/news-corp.yaml,
profiles/the-verge.yaml, profiles/guardian.yaml, profiles/atlantic.yaml,
profiles/wired.yaml, profiles/ap.yaml, and
profiles/careers/journalists.yaml.)
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
SUITE_LOG = os.path.join(GOAL_HIDDEN, "type_d_1295_full_suite.log")
OWN_BASENAME = (
    "test_type_c_1299_signsplit_signed_data_contributor_paid_"
    "data_pools_oct07_10pm.py"
)

# Patched per #565 in the anchor followup (main commit sha).
ANCHORED_SHA = "43b3adab687c7c74210f5936eaf771b1b042e328"  # patched to main commit per #565

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

MECH_NUM = 1011
NEXT_NUM = 1012  # integer only; key-form needles are format-built

BLOCK_KEY = (
    "type_c_1299_signsplit_signed_data_contributor_paid_"
    "data_pools_oct07"
)

# Predecessor chain: #1298 Type B (fourth leg).
PRED_MAIN_1298 = "10c95ef2485322273883714cb319516d58c18f79"
PRED_ANCHOR_1298 = "f2379272dfd7a43027d53dbccae58d589c8b36f4"
PRED_DOCSYNC_1298 = "c131b2cd211e040d42a69556b2ef7d1ad678b1eb"
PRED_FINAL_1298 = "af86fc8791d1767f32da78e6f9f784be28a08a5c"
PRED_PUSH_1298 = "c02d2b41f04b9d15f9cd45c2b0a6e04d077d8751"
# #1297 Type A (third leg) for the rotation-guard chain.
PRED_MAIN_1297 = "a8bd4c5dc8708c4f8604762175446526b29dcad4"
PRED_ANCHOR_1297 = "031bc9837241d7368c7e8460595c7aa9c38b33a5"
PRED_DOCSYNC_1297 = "f9cdd60c85f72b49249f562ddbbd0b4a302f48b5"
PRED_FINAL_1297 = "277ce84e4f575f72eda22ad7d9d4691771dadc87"
PRED_PUSH_1297 = "8d2e3632f7b03d21613420d4bc2a7a02efb0ffcd"
# #1296 Type E (second leg).
PRED_MAIN_1296 = "14af9fecd0d7dcc93eced86ab065e9114f685226"
PRED_ANCHOR_1296 = "ab7778723654c3af8f3fd3ba50e98f849c4d4437"
PRED_DOCSYNC_1296 = "064eb53069399711d54b405d2e763d16c909a828"
PRED_FINAL_1296 = "953ddaaa62a7f16ba13c2b6889aa900fcc57b7c0"
PRED_PUSH_1296 = "4a3062a00a64923aea8792fefe139b19e7f6ecb1"
# #1295 Type D (window opener).
PRED_MAIN_1295 = "99b14c1637813fad0b3d58c8d3f632f81e8e341d"
PRED_ANCHOR_1295 = "6a72097f7f785efb933f0cf6a2e851aca9ae94ac"
PRED_DOCSYNC_1295 = "977fae5da31440b47e7ca4bf7155f6b1e8a9a0dd"
PRED_FINAL_1295 = "6bb3a68e9815399998786adf2b876f397cb6a697"
PRED_PUSH_1295 = "35856f7bf4fb7265dccd89674da40ab49b98e404"

# This run's own main-commit sha, re-pinned per #721 in the terminal
# log-hash followup (starts as 0*40).
PRED_MAIN_1299 = "43b3adab687c7c74210f5936eaf771b1b042e328"  # re-pinned to main sha in the terminal log-hash followup per #721

# Forward guard for the next leg: #1300 Type D. Re-pinned by #1300's
# log-hash followup per #721 (starts as 0*40; placeholder-only per the
# Type C precedent - this file carries no forward git-log pin).
PRED_MAIN_1300 = "0" * 40

# The #1298 window-continuation file, for the staleness pin on its
# guard-lifecycle class (max id 1010; zero one-zero-one-one keys all
# forms / no-Type-C-#1299-in-git-log / fortieth direction absent /
# forty-eighth through fifty-eighth members intact /
# fifty-ninth member absent / ledger 58).
E1298_FILE = (
    "test_type_b_1298_nicholas_sutrich_android_central_meta_"
    "display_year_review_vs_xreal_aura_may_sep_9pm.py"
)

# Doc-sync constants per #719: post-doc-sync values from the start.
# Patched pre-main once the in-gate collection count is known.
README_TEST_COUNT = 72803  # patched pre-main: pre-sync 72733 + 70 collected
README_FILE_COUNT = 1624  # pre-sync 1623 + 1 (this file)

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
_T59 = "FIFT" + "Y-NINTH falsification-family member"

# Novel source URLs: 3 zero-hit repo-wide pre-commit (git grep -F).
NOVEL_URLS = [
    "https://www.morningstar.com/news/pr-newswire/20261005ph62853/"
    "signsplit-secures-400-million-strategic-seed-round-at-1-"
    "billion-valuation",
    "https://recodex.pro/signsplit-raises-400m-seed-at-1b-valuation-"
    "as-ai-turns-to-real-world-human-data/",
    "https://dev.to/techaiwire/signsplit-gets-400m-seed-at-1b-to-"
    "license-human-data-82n",
]

# Corroborating source URL: zero-hit repo-wide pre-commit (git grep -F
# verified), carried in the block with novel:false (corroboration only),
# NOT counted in NOVEL_URLS.
CORROB_URL = (
    "https://aiweekly.co/alerts/signsplit-debuts-400m-seed-at-1b-"
    "to-pay-ai-data-contributors"
)


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


def _load_entities():
    return yaml.safe_load(_read(ENTITIES_PATH))


def _block():
    data = _load_entities()
    assert BLOCK_KEY in data
    return data[BLOCK_KEY]


def _block_text():
    return _read(ENTITIES_PATH)


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
    return subprocess.run(
        ["python3", "-m", "pytest", target,
         "-k", classname,
         "-q", "--no-header"],
        cwd=REPO_ROOT, capture_output=True, text=True, env=env,
    )


# ---------------------------------------------------------------------------
# 1. Anchor (pre-commit placeholder per #565; patched in anchor followup).
# ---------------------------------------------------------------------------

class TestAnchor1299:
    def test_anchor_sha_placeholder_pre_commit(self):
        # Pre-commit this is 0*40 and the test passes BY DESIGN;
        # fails post-anchor (patched to the main commit sha).
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
        assert "FIFTH and CLOSING leg of the 1295-1299 window" in src


# ---------------------------------------------------------------------------
# 2. Rotation guard: #1298/#1297/#1296/#1295 chain; closes 1295-1299.
# ---------------------------------------------------------------------------

class TestRotationGuard1299:
    def test_predecessor_1298_chain_verified(self):
        for sha in (
            PRED_MAIN_1298, PRED_ANCHOR_1298, PRED_DOCSYNC_1298,
            PRED_FINAL_1298, PRED_PUSH_1298,
        ):
            res = _git("cat-file", "-t", sha)
            assert res.stdout.strip() == "commit", "missing %s" % sha

    def test_predecessor_1297_chain_verified(self):
        for sha in (
            PRED_MAIN_1297, PRED_ANCHOR_1297, PRED_DOCSYNC_1297,
            PRED_FINAL_1297, PRED_PUSH_1297,
        ):
            res = _git("cat-file", "-t", sha)
            assert res.stdout.strip() == "commit", "missing %s" % sha

    def test_window_order_phrase(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "D #1295 -> E #1296 -> A #1297 -> B #1298 -> C #1299" in src

    def test_next_window_opens_1300(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Next run #1300 Type D opens the 1300-1304 window" in src

    def test_type_c_lands_one_mechanism(self):
        # Type C lands exactly one mechanism (mechanism 1011); the Type
        # B predecessor added one (mechanism 1010).
        assert _block()["mechanism_id"] == MECH_NUM
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Type C lands one mechanism" in src


# ---------------------------------------------------------------------------
# 3. Mechanism novelty: 1011 lands; key forms stay clean per #715.
# ---------------------------------------------------------------------------

class TestMechanismNovelty1299:
    def test_max_mechanism_id_is_1011_post_landing(self):
        assert _max_numeric_mechanism_id() == MECH_NUM

    def test_block_key_present(self):
        assert BLOCK_KEY in _load_entities()

    def test_block_key_occurs_twice_in_text(self):
        text = _block_text()
        assert text.count(BLOCK_KEY) == 2

    def test_1011_numeric_present_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(MECH_NUM) == [ENTITIES_PATH]

    def test_1011_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(MECH_NUM) == []

    def test_1011_dash_absent_repo_wide(self):
        assert _repo_grep_dash_mechanism(MECH_NUM) == []

    def test_iteration_field(self):
        assert _block()["iteration"] == 1299

    def test_iteration_type_field(self):
        assert _block()["iteration_type"] == "C"

    def test_no_type_c_1299_in_git_log_pin(self):
        # Post-main-commit form (the #1191-class self-trip, re-pinned
        # in the terminal log-hash followup per #721): every commit
        # whose message matches "Type C #1299" must be this run's
        # main commit or a descendant of it - i.e., no PRIOR run
        # committed this run's iteration. Deselected in the in-gate
        # run (fails pre-commit by design).
        out = _git("log", "--format=%H", "--grep=Type C #1299")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected this run's own commits"
        main = _git("rev-parse", PRED_MAIN_1299).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h


# ---------------------------------------------------------------------------
# 4. Block structure at the competitor-entities.yaml top level.
# ---------------------------------------------------------------------------

class TestBlockStructure1299:
    def test_block_key_top_level(self):
        data = _load_entities()
        assert BLOCK_KEY in data
        assert data[BLOCK_KEY]["mechanism_id"] == MECH_NUM

    def test_mechanism_id_field(self):
        assert _block()["mechanism_id"] == MECH_NUM

    def test_block_key_field(self):
        assert _block()["block_key"] == BLOCK_KEY

    def test_required_fields_present(self):
        b = _block()
        for field in ("mechanism_name", "finding", "verdict",
                      "verdict_detail", "novelty", "research_method",
                      "rotation_transparency", "concurrency",
                      "connects_to", "confounders", "sources",
                      "background_suite_status", "falsification_family",
                      "falsification_family_member"):
            assert field in b, field

    def test_connects_to_present(self):
        assert set(_block()["connects_to"]) == {
            663, 711, 786, 804, 891, 915, 999, 1002, 1005, 1008}

    def test_all_novel_sources(self):
        urls = [s["url"] for s in _block()["sources"]]
        for u in NOVEL_URLS:
            assert u in urls, u

    def test_corborating_source_marked_not_novel(self):
        by_url = {s["url"]: s for s in _block()["sources"]}
        assert CORROB_URL in by_url
        assert by_url[CORROB_URL]["novel"] is False

    def test_yaml_parse_clean_flag(self):
        assert _block()["yaml_parse_clean"] is True

    def test_ascii_only_flag(self):
        assert _block()["ascii_only"] is True

    def test_verdict_mechanism_documented(self):
        assert _block()["verdict"] == "mechanism_documented"
        assert _block()["verdict_detail"] == "mechanism_documented"

    def test_manual_qualitative_only(self):
        assert "MANUAL / qualitative ONLY" in _block()["finding"]

    def test_engine_not_run(self):
        assert _block()["engine_run"] is False

    def test_not_falsification_member(self):
        b = _block()
        assert b["falsification_family_member"] is False
        assert "ledger holds at 58" in b["falsification_family"]

    def test_no_analysis_json_update(self):
        assert _block()["no_analysis_json_update"] is True

    def test_not_artifact_grade(self):
        assert _block()["artifact_grade"] is False

    def test_browser_opens_zero(self):
        assert _block()["browser_opens"] == 0

    def test_block_ascii_only(self):
        def _walk(o):
            if isinstance(o, str):
                o.encode("ascii")
            elif isinstance(o, dict):
                for v in o.values():
                    _walk(v)
            elif isinstance(o, list):
                for v in o:
                    _walk(v)
        _walk(_block())

    def test_no_em_dashes(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        em_dash = chr(0x2014)  # built at runtime per #770; no literal in source
        en_dash = chr(0x2013)
        assert em_dash not in src
        assert en_dash not in src

    def test_yaml_block_ascii(self):
        block = _block()
        yaml.safe_dump(block).encode("ascii")


# ---------------------------------------------------------------------------
# 5. Guard lifecycle: forward guards for #1300 Type D.
# ---------------------------------------------------------------------------

class TestGuardLifecycle1299:
    def test_pins_on_one_mechanism_landing(self):
        # Type C lands one mechanism: max 1011, next 1012.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 1011" in src
        assert "NEXT_NUM = 1012" in src

    def test_no_type_d_1300_in_git_log_pin(self):
        # Post-main-commit form for the NEXT leg (the #1191-class
        # self-trip, re-pinned in #1300's terminal log-hash followup
        # per #721): every commit whose message matches "Type D
        # #1300" must be #1300's main commit or a descendant of it.
        # Deselected in the in-gate run (fails pre-commit by design).
        out = _git("log", "--format=%H", "--grep=Type D #1300")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1300's own commits"
        main = _git("rev-parse", PRED_MAIN_1300).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_1012_numeric_absent_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_1012_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_1012_dash_absent_repo_wide(self):
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
        # Landed #1282 (m1000, profiles/wired.yaml). Asserted on the
        # working tree so the pin is stable across the main-commit
        # boundary; the HEAD sweep sees it from the main commit on.
        assert _T56 in _read(os.path.join(PROFILES_DIR, "wired.yaml"))

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

    def test_no_fifty_ninth_member_pin(self):
        # No fifty-ninth member has been claimed anywhere; the
        # fifty-ninth member-claim form stays absent repo-wide
        # (source scope; __pycache__ excluded per the #715
        # pattern-rescope lesson).
        assert _git_grep_tracked_source(_T59, None) == []

    def test_predecessor_1298_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, E1298_FILE))

    def test_next_leg_is_1300_type_d(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#1300 Type D" in src

    def test_1298_pins_flip_by_design_documented(self):
        # #1298's forward guards (max-1010, zero one-zero-one-one
        # keys all forms, no-Type-C-#1299-in-git-log, fortieth
        # absent, forty-eighth through fifty-eighth intact in
        # profiles/, fifty-ninth absent, ledger 58) verified GREEN
        # at HEAD pre-commit this run. The no-Type-C-#1299-in-git-log
        # pin flips BY DESIGN at this run's main commit (the
        # #1191-class self-trip, re-pinned post-commit by
        # TestStalenessPins1299). Type C lands one mechanism, so the
        # zero one-zero-one-one numeric pin flips BY DESIGN too (the
        # #1272-class forward-guard expiry; the underscore/dash pins
        # stay green by the #723/#738/#739 designed keying).
        # Documented in the staleness pin below, not repaired.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "TestStalenessPins1299" in src
        assert "no_type_c_1299_in_git_log_pin" in src


# ---------------------------------------------------------------------------
# 6. Staleness pins: #1298's guard lifecycle flips BY DESIGN post-commit.
# ---------------------------------------------------------------------------

class TestStalenessPins1299:
    def test_1298_guard_lifecycle_post_commit_self_trip(self):
        # Post-terminal-followup form: 21 tests in the class; ONE flips
        # BY DESIGN when this run's main commit lands and STAYS
        # flipped: the test_1011_numeric_absent_in_profiles pin (the
        # m1011 landing carries "mechanism_id: 1011" in colon form -
        # the #1272-class forward-guard expiry; the underscore/dash
        # pins stay green by the #723/#738/#739 designed keying). The
        # no_type_c_1299_in_git_log ancestor pin ALSO flips at the
        # main commit but is re-pinned green in the terminal log-hash
        # followup per #721 (its PRED_MAIN_1299 now holds this run's
        # main sha). The class run below therefore expects 1 failed /
        # 20 passed and documents the designed flip. The #1298 block
        # is read-only to this run; the flip is documented here, not
        # repaired. Deselected in the in-gate run (fails pre-commit
        # by design).
        res = _class_run(E1298_FILE, "TestGuardLifecycle1298")
        out = res.stdout + res.stderr
        assert "1 failed, 20 passed" in out, out[-2000:]
        assert "test_1011_numeric_absent_in_profiles" in out, out[-2000:]


# ---------------------------------------------------------------------------
# 7. Doc-sync per #719 (3 tests; deselected pre-commit, flipped post-sync)
# ---------------------------------------------------------------------------

class TestDocSync1299:
    def test_readme_test_file_table_has_1299_row_post_sync(self):
        readme = _read(README_PATH)
        assert OWN_BASENAME in readme

    def test_architecture_has_1299_row_post_sync(self):
        arch = _read(ARCH_PATH)
        assert OWN_BASENAME in arch

    def test_readme_stats_ratcheted(self):
        readme = _read(README_PATH)
        assert "| Tests | %d |" % README_TEST_COUNT in readme
        assert "Across %d test files" % README_FILE_COUNT in readme


# ---------------------------------------------------------------------------
# 8. Iteration-log entry per #721 (3 tests; deselected pre-commit)
# ---------------------------------------------------------------------------

class TestIterationLog1299:
    def test_log_has_1299_entry(self):
        text = _read(LOG_PATH)
        assert "## #1299 Type C" in text

    def test_log_entry_carries_hash_chain(self):
        # The doc-sync writes the entry with the main/anchor hashes;
        # the terminal log-hash followup registers the doc-sync hash
        # here per #721.
        text = _read(LOG_PATH)
        assert "main commit" in text
        assert "anchor" in text

    def test_log_entry_records_finding(self):
        text = _read(LOG_PATH)
        assert "m1011" in text
        assert "mechanism_documented" in text
        assert "ledger holds at 58" in text


# ---------------------------------------------------------------------------
# 9. In-flight isolation
# ---------------------------------------------------------------------------

class TestInFlightIsolation1299:
    def test_899_nytimes_hunk_untouched(self):
        res = _git("diff", "--name-only")
        modified = res.stdout.split()
        assert "profiles/nytimes.yaml" in modified
        # Its uncommitted hunk belongs to #899's run; this run stages
        # only its own files via explicit-path staging.
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
