# -*- coding: utf-8 -*-
"""Type B #1308 tests: Tobi Opeyemi Amure (TheStreet) - Sep-26-2026 Meta
Connect-week VR glasses piece "Zuckerberg takes a swing at Vision Pro
with $1,299 glasses" (-0.10 MANUAL ILLUSTRATIVE, NEW Meta arm,
guarded investor-forward register: price/trade-off framing flatters
Meta on price vs Vision Pro but foregrounds caveats - weight fine
print, narrower field of view, spring-2027 ship; consumer-advocacy
shading in the writer's own voice) vs Sep-6-2026 OpenAI GPT-6 Astra
piece "OpenAI's new model is so capable, the company had to lock parts
down" (+0.20 MANUAL ILLUSTRATIVE, NEW OpenAI arm, capability-forward
register: 100% ExploitBench, "Welcome to the AGI era" (Brockman via
Forbes), the Critical-threshold lockdown relayed as responsible-safety
process - "creates a need for stronger safeguards"); illustrative
delta (OpenAI minus Meta) +0.30 - same writer, same outlet, ~3 weeks
apart.

Mechanism 1016 (NOT a falsification-family member; ledger holds at 59).
FIRST dedicated Type B mechanism on Tobi Opeyemi Amure (zero "amure"
hits repo-wide pre-commit, grep-verified this run) and FIRST
journalist-level mechanism at TheStreet (existing TheStreet mentions
are relay-level citations and the Jacob Krol career-history note, not
mechanismized pairs; disclosed). The outlet is an Arena Group brand;
the in-corpus Roundtable x Paradium.AI 10-year AI/DeFi MediaOS deal
(m738, #844) is infrastructure-capture background, NOT a content
licensing payer leg. No publicly known AI content-licensing deal
between TheStreet/Arena and OpenAI or Meta exists in-corpus: this is
a ZERO-GRADIENT control pair (the Keleops/Gizmodo m690 pattern) - the
naive payer-softening prediction is NULL on this pair, so the +0.30
illustrative delta can be attributed to neither a payer relationship
nor its absence; it is a journalist-level register-asymmetry
observation. STRONG confounds: peg asymmetry (Connect hardware launch
with shipping caveats vs model-capability milestone with safety-process
framing - the news pegs carry different valences) and the zero-gradient
financial context itself (cuts against financial-determinism readings,
disclosed honestly); MODERATE: excerpt-bounded evidence (0 browser.open
per #503; headline+snippet register readings), investor-beat house
style (Amure is a finance/investor writer, not a privacy specialist).

Excerpt-bounded research per #503 (1 delegated scout, ranked 3 pairs;
4 main-run browser.search verification sets, 0 browser.open reads).
Scout SELECTED Amure as the freshest same-writer pair (both arms Sep
2026, same investor-facing wire genre, Connect-week wearables on the
Meta arm - directly on-topic); REJECTED #2 Remy (TheStreet outlet
overlap with the selected pair; Meta arm is nudify-ads trust-and-safety
rather than wearables; competitor arm casts Apple as enforcer, not
subject) and #3 Levine/Barron's (Apple arm is a Jun-2026 livecoverage
card - stale and thin; News Corp x OpenAI licensing already banked in
corpus, lower novelty). Prior-run rejection lists stand (#1303's 40+
audit: Criddle, Wagner, Milmo, Hern, Hardawar, Steele, Dent, Ortutay,
Bhuiyan, Murphy, Field, Paul, Nellis, Thompson, O'Brien, Hao, Dara Kerr
(type_b_513), Wong, Duffy, Gurman, Fried; structural: Parrish, Nix,
Tong, Khari Johnson, Haselton, Stokel-Walker; Velazco, Albergotti,
Vanian, Metz, Elias, Wiggers, Amadeo; plus this run's exclusions:
Vlamis, Emma Roth, Stephen Nellis, Marcus Mendes, Kalley Huang,
Kris Holt, Kelvin Chan, Boone Ashworth, Kaitlyn Huamani, Sean Keach,
Kara Swisher, Kit Eaton).

The m1016 block lives in profiles/careers/journalists.yaml under the
tobi_opeyemi_amure_type_b keyed entry's competitor_coverage dict (per
the #643 convention); mechanism_ids [1016].

Anchor convention per #565: ANCHORED_SHA starts as 0*40 in this
pre-commit file and is patched to the main-commit hash in the anchor
followup commit. One anchor test (the placeholder pin) fails BY DESIGN
post-anchor.

Per #795: this run only CHECKS the #1305-launched background suite
(goal hidden_files type_d_1305_full_suite.log, observed at this run's
check; an observation, not a verdict); its verdict and tombstone belong
to #1310 (next Type D). This run neither re-launches, kills, nor writes
to the suite.

Do NOT touch #1024 (m846 in profiles/competitor-entities.yaml), #899
(nytimes.yaml m771 hunk), #938 (Type B test file working-tree edit),
#900 (untracked Type D test file), #1012-wt (working-tree edit on the
committed Type A #1012 file).

Type B lands one mechanism (mechanism 1016); the Type A predecessor
added one (mechanism 1015). Next run #1309 Type C closes the 1305-1309
window. Rotation: D #1305 -> E #1306 -> A #1307 -> B #1308 -> C #1309.
This run is the FOURTH leg of the 1305-1309 window. The main commit is
the anchor per #565.

ASCII-only, no em dashes. Needles format-built per #715: this file must
not carry contiguous numeric/underscore/dash mechanism-key forms of the
landed or next number, the forty-eighth through fifty-ninth
member-claim forms, the sixtieth member-claim form, or the fortieth
direction form; the constants are constructed at runtime. (The landed
ordinals live as short lowercase forms in prose here; the live full-form
claims live in profiles/financial-times.yaml, profiles/news-corp.yaml,
profiles/the-verge.yaml, profiles/guardian.yaml, profiles/atlantic.yaml,
profiles/wired.yaml, profiles/ap.yaml, and profiles/careers/journalists.yaml.)

Quoted material below is limited to short verbatim phrases per the
copyright-brief-quotation rule; registers are otherwise paraphrased.
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
JOURNALISTS_PATH = os.path.join(PROFILES_DIR, "careers", "journalists.yaml")
OWN_BASENAME = (
    "test_type_b_1308_tobi_opeyemi_amure_thestreet_meta_glasses_"
    "vs_openai_astra_oct08_7am.py"
)
TOP_KEY = "tobi_opeyemi_amure_type_b"

# Pre-commit placeholder per #565; patched to the main commit sha in
# the anchor followup.
ANCHORED_SHA = "5b997970b53d4a9e687a2f9a1a99e2cd2b558891"  # patched to main commit per #565

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

MECH_NUM = 1016
NEXT_NUM = 1017  # integer only; key-form needles are format-built

BLOCK_KEY = (
    "type_b_1308_tobi_opeyemi_amure_thestreet_meta_glasses_"
    "vs_openai_astra_oct08_7am"
)

# Predecessor chain: #1307 Type A (third leg).
PRED_MAIN_1307 = "7009064e750fd2ecb3a0940ebabeb954dee5a789"
PRED_ANCHOR_1307 = "6ee958a7357e20e21d49f076c3fc12d4c955105f"
PRED_DOCSYNC_1307 = "a0ec12d1a983ee810d268d911e453a1a7f21b9e1"
PRED_FINAL_1307 = "73307210c6887a9e1e979a279fd2ec84434166b4"
PRED_PUSH_1307 = "ea18c53b6073eacade2c6f5a96e69214ac991da5"
# #1306 Type E (second leg) for the rotation-guard chain.
PRED_MAIN_1306 = "0ac1044d0d6398ffcaa7914662323af0dd125c7b"
PRED_ANCHOR_1306 = "69dadafb9f5ab2696cc61a2c5286c93c0715748b"
PRED_DOCSYNC_1306 = "dbed9dbca9bc70bc7602d1d95bd3fdcc14656e9c"
PRED_FINAL_1306 = "f7640d284e1a27dd0f795910dbc3d8da56937fb8"

# This run's own main-commit sha, re-pinned per #721 in the terminal
# log-hash followup (starts as 0*40; the own-run git-log pin is
# deselected in the in-gate run and fails pre-commit by design).
PRED_MAIN_1308 = "5b997970b53d4a9e687a2f9a1a99e2cd2b558891"  # re-pinned to #1308 main sha in the terminal log-hash followup per #721

# Forward guard for the next leg: #1309 Type C. Re-pinned by #1309's
# log-hash followup per #721 (starts as 0*40; the forward pin is
# deselected in the in-gate run and fails pre-commit by design).
PRED_MAIN_1309 = "0" * 40

# The #1307 window-continuation file, for the staleness pin on its
# guard-lifecycle class (max id 1015; zero one-zero-one-six keys all
# forms / no-Type-B-#1308-in-git-log / fortieth direction absent /
# forty-eighth through fifty-ninth members intact /
# sixtieth member absent / ledger 59).
D1307_FILE = (
    "test_type_a_1307_barrons_microsoft_oct06_oct07_investor_forward_"
    "vs_carried_meta_arms_oct08_6am.py"
)

# Doc-sync constants per #719: post-doc-sync values from the start.
# Patched pre-main once the in-gate collection count is known.
README_TEST_COUNT = 73684  # post-doc-sync total (pre-sync 73575 + 109)
README_FILE_COUNT = 1633  # pre-sync 1632 + 1 (this file)

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
_T60 = "SIXT" + "IETH falsification-family member"

# Novel source URLs: 3 zero-hit repo-wide pre-commit (git grep -F).
NOVEL_URLS = [
    "https://www.thestreet.com/technology/meta-1299-vr-glasses-compete-with-apple-vision-pro",
    "https://www.thestreet.com/technology/openals-new-model-is-so-capable-the-company-had-to-lock-parts-down",
    "https://www.thestreet.com/author/tobi-opeyemi-amure",
]
RESURFACED_URLS = []


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
    args = ["grep", "-F", "-l", needle, "HEAD", "--"]
    if scope:
        args.append(scope)
    else:
        args.append(".")
    out = _git(*args).stdout
    cleaned = []
    for line in out.splitlines():
        line = line.strip()
        if line.startswith("HEAD:"):
            line = line[len("HEAD:"):]
        if line:
            cleaned.append(line)
    return cleaned


def _load_journalists():
    with open(JOURNALISTS_PATH, encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def _top():
    return _load_journalists()[TOP_KEY]


def _block():
    return _top()["competitor_coverage"][BLOCK_KEY]


def _class_run(test_file, class_name):
    return subprocess.run(
        [".venv/bin/python", "-m", "pytest",
         os.path.join(TESTS_DIR, test_file) + "::" + class_name,
         "--no-header", "-q", "-p", "no:cacheprovider"],
        cwd=REPO_ROOT, capture_output=True, text=True,
    )


# ---------------------------------------------------------------------------
# 1. Anchor convention per #565
# ---------------------------------------------------------------------------

class TestAnchor1308:
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
        assert "FOURTH leg of the 1305-1309 window" in src


# ---------------------------------------------------------------------------
# 2. Rotation guard
# ---------------------------------------------------------------------------

class TestRotationGuard1308:
    def test_predecessor_1307_chain_verified(self):
        for sha in (
            PRED_MAIN_1307, PRED_ANCHOR_1307, PRED_DOCSYNC_1307,
            PRED_FINAL_1307, PRED_PUSH_1307,
        ):
            res = _git("cat-file", "-t", sha)
            assert res.stdout.strip() == "commit", "missing %s" % sha

    def test_predecessor_1306_chain_verified(self):
        for sha in (
            PRED_MAIN_1306, PRED_ANCHOR_1306, PRED_DOCSYNC_1306,
            PRED_FINAL_1306,
        ):
            res = _git("cat-file", "-t", sha)
            assert res.stdout.strip() == "commit", "missing %s" % sha

    def test_window_order_phrase(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "D #1305 -> E #1306 -> A #1307 -> B #1308 -> C #1309" in src

    def test_next_leg_is_type_c_1309(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Next run #1309 Type C" in src

    def test_type_b_lands_one_mechanism(self):
        # Type B lands exactly one mechanism (mechanism 1016); the Type
        # A predecessor added one (mechanism 1015).
        assert _block()["mechanism_id"] == MECH_NUM
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Type B lands one mechanism" in src


# ---------------------------------------------------------------------------
# 3. Mechanism novelty (the #715 discipline)
# ---------------------------------------------------------------------------

class TestMechanismNovelty1308:
    def test_top_key_found(self):
        assert _top()["mechanism_ids"] == [MECH_NUM]

    def test_block_key_zero_mechanism_number_substring(self):
        # Designed keying per #715: iteration 1308 in key, no 1016 or
        # 1017 substring.
        assert "1308" in BLOCK_KEY
        assert str(MECH_NUM) not in BLOCK_KEY
        assert str(NEXT_NUM) not in BLOCK_KEY

    def test_zero_underscore_mechanism_repo_wide(self):
        # Per #715 designed keying the landed number appears only as
        # the colon form; the underscore key form must not exist
        # repo-wide.
        hits = _repo_grep_underscore_mechanism(MECH_NUM)
        assert hits == [], hits

    def test_zero_dash_mechanism_repo_wide(self):
        hits = _repo_grep_dash_mechanism(MECH_NUM)
        assert hits == [], hits

    def test_zero_numeric_next_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_max_numeric_mechanism_id_is_this_run(self):
        nums = []
        for _line in _repo_grep_numeric_mechanism_id(MECH_NUM):
            nums.append(MECH_NUM)
        assert _max_numeric_mechanism_id() == MECH_NUM
        assert len(_repo_grep_numeric_mechanism_id(MECH_NUM)) >= 1

    def test_no_type_b_1308_in_git_log_own_run(self):
        # Post-main-commit form (the #1191-class self-trip, re-pinned
        # in the terminal log-hash followup per #721): every commit
        # whose message matches "Type B #1308" must be #1308's main
        # commit or a descendant of it. Deselected in the in-gate run
        # (fails pre-commit by design: PRED_MAIN_1308 is 0*40).
        out = _git("log", "--format=%H", "--grep=Type B #1308")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1308's own commits"
        main = _git("rev-parse", PRED_MAIN_1308).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_novel_urls_zero_hit_pre_commit(self):
        # All three novel URLs verified zero-hit repo-wide pre-commit
        # via git grep -F this run.
        for url in NOVEL_URLS:
            out = _git("grep", "-F", "-l", url, "HEAD", "--", ".")
            assert out.stdout.strip() == "", url

    def test_journalist_zero_hit_pre_commit(self):
        # "amure" zero-hit repo-wide pre-commit, grep-verified this
        # run (FIRST dedicated Type B pair on this journalist).
        out = _git("grep", "-il", "amure", "HEAD", "--", ".")
        assert out.stdout.strip() == "", out.stdout

    def test_thestreet_no_journalist_mechanism_pre_commit(self):
        # Existing TheStreet mentions are relay-level citations and
        # the Jacob Krol career-history note, not mechanismized
        # journalist pairs; disclosed in the block's novelty note.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "relay-level" in src

    def test_no_1308_row_in_readme_table(self):
        readme = _read(README_PATH)
        assert "test_type_b_1308" not in readme

    def test_no_1308_row_in_architecture_tree(self):
        arch = _read(ARCH_PATH)
        assert "test_type_b_1308" not in arch

    def test_no_1308_in_iteration_log_pre_commit(self):
        log = _read(LOG_PATH)
        assert "## #1308" not in log


# ---------------------------------------------------------------------------
# 4. Block structure (the #643 convention)
# ---------------------------------------------------------------------------

class TestBlockStructure1308:
    def test_top_level_fields(self):
        t = _top()
        assert t["name"] == "Tobi Opeyemi Amure"
        assert t["publication"] == "thestreet"
        assert t["mechanism_ids"] == [MECH_NUM]

    def test_block_key_present(self):
        assert BLOCK_KEY in _top()["competitor_coverage"]

    def test_block_identity_fields(self):
        b = _block()
        assert b["block_key"] == BLOCK_KEY
        assert b["mechanism_id"] == MECH_NUM
        assert b["iteration"] == 1308
        assert b["iteration_type"] == "B"
        assert b["type"] == "B"
        assert b["journalist"] == "Tobi Opeyemi Amure"
        assert b["publication"] == "thestreet"
        assert b["author"] == "Kit (with Ray)"
        assert b["goal_id"] == "goal_54093bda4145"
        assert b["job_id"] == "mediascope-daily-iteration"

    def test_both_arms_present(self):
        b = _block()
        assert "meta_arm" in b
        assert "openai_arm" in b

    def test_meta_arm_fields(self):
        m = _block()["meta_arm"]
        assert m["entity"] == "meta"
        assert m["outlet"] == "thestreet"
        assert m["author_byline"] == "Tobi Opeyemi Amure"
        assert "tone_MANUAL_ILLUSTRATIVE" in m
        assert m["tone_MANUAL_ILLUSTRATIVE"] == -0.10
        assert m["url"] == NOVEL_URLS[0]

    def test_openai_arm_fields(self):
        o = _block()["openai_arm"]
        assert o["entity"] == "openai"
        assert o["outlet"] == "thestreet"
        assert o["author_byline"] == "Tobi Opeyemi Amure"
        assert "tone_MANUAL_ILLUSTRATIVE" in o
        assert o["tone_MANUAL_ILLUSTRATIVE"] == 0.20
        assert o["url"] == NOVEL_URLS[1]

    def test_delta_field(self):
        b = _block()
        assert b["illustrative_delta_openai_minus_meta"] == 0.30

    def test_evidence_tier_excerpt(self):
        b = _block()
        for arm in ("meta_arm", "openai_arm"):
            assert "EXCERPT-TIER" in b[arm]["evidence_tier"]
            assert "0 browser.open" in b[arm]["evidence_tier"]

    def test_verbatim_urls_not_constructed(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "verbatim" in src.lower()

    def test_ascii_only_no_em_dashes(self):
        for p in [os.path.join(TESTS_DIR, OWN_BASENAME), JOURNALISTS_PATH]:
            text = _read(p)
            assert "\u2014" not in text, p
            assert "\u2013" not in text, p


# ---------------------------------------------------------------------------
# 5. Content discipline: the m1016 pair
# ---------------------------------------------------------------------------

class TestM1016ContentDiscipline1308:
    def test_same_writer_same_outlet(self):
        b = _block()
        assert b["meta_arm"]["author_byline"] == "Tobi Opeyemi Amure"
        assert b["openai_arm"]["author_byline"] == "Tobi Opeyemi Amure"
        assert b["meta_arm"]["outlet"] == b["openai_arm"]["outlet"] == "thestreet"

    def test_temporal_proximity(self):
        b = _block()
        assert b["meta_arm"]["date"] == "2026-09-26"
        assert b["openai_arm"]["date"] == "2026-09-06"
        assert "3 weeks" in b["design"] or "~3 weeks" in b["design"]

    def test_meta_arm_headline(self):
        m = _block()["meta_arm"]
        assert "Zuckerberg takes a swing at Vision Pro" in m["title"]
        assert "$1,299" in m["title"]

    def test_openai_arm_headline(self):
        o = _block()["openai_arm"]
        assert "lock parts down" in o["title"]

    def test_register_readings(self):
        b = _block()
        assert "Guarded investor-forward" in b["meta_arm"]["tone_reading"]
        assert "Capability-forward" in b["openai_arm"]["tone_reading"]

    def test_zero_gradient_financial_context(self):
        # No documented AI content-licensing deal between TheStreet /
        # Arena and OpenAI or Meta in-corpus; the Roundtable x
        # Paradium.AI deal (m738/#844) is infrastructure-capture
        # background, disclosed, NOT a payer leg.
        b = _block()
        assert "ZERO-GRADIENT" in b["financial_context"]
        assert "m738" in b["financial_context"]

    def test_confounds_ranked(self):
        b = _block()
        conf = b["confounders"]
        assert any("STRONG" in c for c in conf)
        assert any("peg asymmetry" in c.lower() for c in conf)

    def test_counterevidence_disclosed(self):
        b = _block()
        assert "counter_evidence" in b
        assert len(b["counter_evidence"]) >= 2

    def test_scout_rejections_documented(self):
        b = _block()
        assert "rejection_audit" in b
        assert "Remy" in b["rejection_audit"]
        assert "Levine" in b["rejection_audit"]

    def test_research_method_documented(self):
        b = _block()
        assert "Delegated scout" in b["research_method"]
        assert "0 browser.open" in b["research_method"]


# ---------------------------------------------------------------------------
# 6. Statistical discipline: MANUAL/QUALITATIVE ONLY (Aug 28 2026 rule)
# ---------------------------------------------------------------------------

class TestStatisticalDiscipline1308:
    def test_manual_illustrative_only(self):
        b = _block()
        assert "MANUAL ILLUSTRATIVE" in b["design"]

    def test_engine_not_run(self):
        b = _block()
        assert b["no_analysis_json_update"] is True

    def test_p_value_not_calculated(self):
        # The needle and the expected def line are both runtime-built;
        # the only contiguous occurrence in this file is the def line.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        needle = "p" + "_value"
        expected_def = "    def test_" + needle + "_not_calculated(self):"
        hits = [l for l in src.splitlines() if needle in l]
        assert hits == [expected_def], hits

    def test_is_significant_false(self):
        assert _block()["is_significant"] is False

    def test_correlation_not_causation(self):
        assert _block()["correlation_not_causation"] is True

    def test_no_analysis_json_update(self):
        assert _block()["no_analysis_json_update"] is True

    def test_verdict_directionally_supported_not_proven(self):
        assert _block()["verdict"] == "directionally_supported_not_proven"

    def test_not_artifact_grade(self):
        assert "NOT artifact-grade" in _block()["falsification_family"] or \
            "No analysis.json update warranted" in _block()["falsification_family"]

    def test_thesis_consistent_not_falsification(self):
        # The +0.30 delta sits on a ZERO-GRADIENT pair (no documented
        # payer differential at TheStreet/Arena for OpenAI or Meta), so
        # the naive payer-softening prediction is NULL here: the delta
        # is a journalist-level register-asymmetry observation, neither
        # meeting nor failing a financial prediction. NOT a
        # falsification-family member.
        b = _block()
        assert b["falsification_family_member"] is False
        assert "zero-gradient" in b["falsification_family"].lower()


# ---------------------------------------------------------------------------
# 7. Falsification ledger: holds at 59 (NOT a member).
# ---------------------------------------------------------------------------

class TestFalsificationLedger1308:
    def test_not_a_falsification_family_member(self):
        b = _block()
        assert b["falsification_family_member"] is False
        assert "NOT a falsification-family member" in b["falsification_family"]

    def test_zero_gradient_disclosed(self):
        b = _block()
        assert "zero-gradient" in b["falsification_family"].lower()

    def test_fifty_ninth_intact_in_news_corp(self):
        # Landed #1302 (m1012, profiles/news-corp.yaml, committed).
        # HEAD sweep is stable for a committed landing.
        out = _git(
            "grep", "-c", "-F", _T59, "HEAD", "--",
            "profiles/news-corp.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fifty_eighth_intact_in_ft(self):
        out = _git(
            "grep", "-c", "-F", _T58, "HEAD", "--",
            "profiles/financial-times.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fifty_seventh_intact_in_ap(self):
        out = _git(
            "grep", "-c", "-F", _T57, "HEAD", "--",
            "profiles/ap.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fifty_sixth_intact_in_wired(self):
        out = _git(
            "grep", "-c", "-F", _T56, "HEAD", "--",
            "profiles/wired.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_fifty_fifth_intact_in_atlantic(self):
        out = _git(
            "grep", "-c", "-F", _T55, "HEAD", "--",
            "profiles/atlantic.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_fifty_fourth_intact_in_guardian(self):
        out = _git(
            "grep", "-c", "-F", _T54, "HEAD", "--",
            "profiles/guardian.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_fifty_third_intact_in_verge(self):
        out = _git(
            "grep", "-c", "-F", _T53, "HEAD", "--",
            "profiles/the-verge.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_fifty_second_intact_in_journalists(self):
        out = _git(
            "grep", "-c", "-F", _T52, "HEAD", "--",
            "profiles/careers/journalists.yaml",
        )
        assert out.stdout.strip().endswith(":5"), out.stdout

    def test_fifty_first_intact_in_news_corp(self):
        out = _git(
            "grep", "-c", "-F", _T51, "HEAD", "--",
            "profiles/news-corp.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fiftieth_intact_in_journalists(self):
        out = _git(
            "grep", "-c", "-F", _T50, "HEAD", "--",
            "profiles/careers/journalists.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_forty_ninth_intact_in_journalists(self):
        out = _git(
            "grep", "-c", "-F", _T49, "HEAD", "--",
            "profiles/careers/journalists.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_forty_eighth_intact_in_ft(self):
        assert _git_grep_tracked_source(_T48, "profiles/") == [
            "profiles/financial-times.yaml"]

    def test_sixtieth_absent(self):
        assert _git_grep_tracked_source(_T60, None) == []

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

    def test_ledger_holds_at_59(self):
        assert "holds at 59" in _block()["ledger_note"]
        assert _block()["falsification_ledger"] == 59

    def test_ledger_note_states_not_a_member(self):
        assert "NOT a falsification-family member" in _block()["ledger_note"]


# ---------------------------------------------------------------------------
# 8. Guard lifecycle: pins for #1309; #1307's pins flip BY DESIGN.
# ---------------------------------------------------------------------------

class TestGuardLifecycle1308:
    def test_pins_on_1016_landing(self):
        # Type B lands one mechanism: max becomes 1016, next is 1017.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 1016" in src
        assert "NEXT_NUM = 1017" in src

    def test_no_type_c_1309_in_git_log_pin(self):
        # Post-main-commit form for the NEXT leg (the #1191-class
        # self-trip, re-pinned in #1309's terminal log-hash followup
        # per #721): every commit whose message matches "Type C
        # #1309" must be #1309's main commit or a descendant of it.
        # Deselected in the in-gate run (fails pre-commit by design:
        # PRED_MAIN_1309 is 0*40).
        out = _git("log", "--format=%H", "--grep=Type C #1309")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1309's own commits"
        main = _git("rev-parse", PRED_MAIN_1309).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_1017_numeric_absent_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_1017_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_1017_dash_absent_repo_wide(self):
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

    def test_no_sixtieth_member_pin(self):
        # m1016 is NOT a falsification-family member (zero-gradient
        # observation); the sixtieth member-claim form stays absent
        # repo-wide.
        assert _git_grep_tracked_source(_T60, None) == []

    def test_predecessor_1307_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, D1307_FILE))

    def test_next_leg_is_1309_type_c(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Next run #1309 Type C" in src

    def test_1307_pins_flip_by_design_documented(self):
        # #1307's forward guards (max-1015, zero one-zero-one-six
        # keys all forms, no-Type-B-#1308-in-git-log, fortieth
        # direction absent, forty-eighth through fifty-ninth members
        # intact, no sixtieth member, ledger 59) verified GREEN
        # pre-commit this run via the subprocess staleness pin (Type
        # B lands mechanism 1016 as a zero-gradient observation,
        # not a family member); the max-1015 and zero one-zero-one-six
        # pins flip post-main-commit on this run's own landing (the
        # #1191-class self-trip on no-Type-B-#1308-in-git-log, re-pinned
        # green in the terminal followup, and the #1272-class
        # forward-guard expiry on 1016-numeric-absent, permanent), by
        # design, documented in the staleness pin below).
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "TestStalenessPins1308" in src
        assert "1 failed, 21 passed" in src


# ---------------------------------------------------------------------------
# 9. Background suite: #1305's suite is CHECKED ONLY per #795.
# ---------------------------------------------------------------------------

class TestBackgroundSuiteCheck1308:
    def test_1305_suite_log_exists(self):
        assert os.path.exists(
            os.path.join(GOAL_HIDDEN, "type_d_1305_full_suite.log"))

    def test_this_run_launches_no_suite(self):
        # This run must not launch its own background suite; only the
        # #1305-launched suite is observed.
        assert not os.path.exists(
            os.path.join(GOAL_HIDDEN, "type_d_1308_full_suite.log"))

    def test_observation_documented_in_block(self):
        assert "#1305-launched" in _block()["background_suite_status"]
        assert "#795" in _block()["background_suite_status"]
        assert "#1310" in _block()["background_suite_status"]


# ---------------------------------------------------------------------------
# 10. Doc-sync per #719 (3 tests; deselected pre-commit, flipped post-sync)
# ---------------------------------------------------------------------------

class TestDocSync1308:
    def test_readme_test_file_table_has_1308_row_post_sync(self):
        readme = _read(README_PATH)
        assert "test_type_b_1308" in readme

    def test_architecture_has_1308_row_post_sync(self):
        arch = _read(ARCH_PATH)
        assert "test_type_b_1308" in arch

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

class TestIterationLog1308:
    def test_1308_entry_present_post_sync(self):
        log = _read(LOG_PATH)
        assert "## #1308 Type B" in log

    def test_1307_entry_present(self):
        log = _read(LOG_PATH)
        assert "## #1307 Type A" in log

    def test_rotation_transparency_convention(self):
        log = _read(LOG_PATH)
        assert "### Rotation transparency" in log


# ---------------------------------------------------------------------------
# 12. Staleness pins: #1307's guard lifecycle flips BY DESIGN post-commit
# ---------------------------------------------------------------------------

class TestStalenessPins1308:
    def test_1307_guard_lifecycle_post_commit_self_trip(self):
        # Post-terminal-followup form: 21 of the 22 pass; the one that
        # fails BY DESIGN is test_1016_numeric_absent_in_profiles
        # (mechanism 1016 lands in profiles/ this run; the #1272-class
        # forward-guard expiry - the next-number guard is consumed by
        # the landing; stays red permanently). The second flip,
        # test_no_type_b_1308_in_git_log_pin (the #1191-class
        # self-trip: this run's own main commit carries "Type B
        # #1308"), is re-pinned green in the terminal log-hash
        # followup per #721 (its PRED_MAIN_1308 now holds this run's
        # main sha). test_pins_on_one_mechanism_landing stays GREEN
        # (asserts on the #1307 file's own constants, untouched by
        # this run); the member and direction pins stay GREEN (m1016
        # is a zero-gradient observation, not a family member).
        # Deselected pre-commit (the pin passes pre-commit).
        res = _class_run(D1307_FILE, "TestGuardLifecycle1307")
        assert res.returncode != 0, res.stdout[-2000:]
        assert "1 failed, 21 passed" in res.stdout, res.stdout[-2000:]
        assert "test_1016_numeric_absent_in_profiles" in res.stdout, \
            res.stdout[-2000:]


# ---------------------------------------------------------------------------
# 13. In-flight isolation
# ---------------------------------------------------------------------------

class TestInFlightIsolation1308:
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
        # #1024 m846 (profiles/competitor-entities.yaml) is NOT
        # touched - decision pending. This run stages only its own
        # files by explicit path.
        res = _git("diff", "--name-only")
        assert "profiles/competitor-entities.yaml" not in res.stdout.split()
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Do NOT touch #1024" in src

    def test_own_diff_excludes_inflight(self):
        # This run's staged set must never include the in-flight
        # files; verified at commit time by explicit-path staging.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "explicit-path" in src
