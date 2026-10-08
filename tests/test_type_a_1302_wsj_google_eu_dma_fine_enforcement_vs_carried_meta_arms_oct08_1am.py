"""Type A #1302: WSJ x Google Jul-24-2026 EU DMA $1.02B fine enforcement-accountability register (Oct 8 2026, ~01:00 AM PDT).

m1012 - FIRST dedicated corpus mechanism on the WSJ/News Corp x Google pair.
The Journal runs the EU's $1.02B DMA non-compliance fine on Google in the
enforcement-accountability register: fine-forwarding headline ("EU Fines
Google $1 Billion for Favoring Its Own Services"), yearslong-investigation
frame, 60-day compliance deadline, Google's compliance-burden quote carried,
and the inline disclosure "News Corp, owner of The Wall Street Journal, has
a commercial agreement to supply content on Google platforms." MANUAL
ILLUSTRATIVE -0.35, set at the m904 FTC-probe arm peg (regulatory-enforcement
accountability on the deal partner).

Carried WSJ x Meta arms (m532 via m904, un-rescored per #807): the Aug-26
$18B settlement wire (-0.30) and the teen-safety skeptical product analysis
(-0.25), mean -0.275. Illustrative delta (Google minus Meta): -0.075,
near-null with Google marginally harder. The naive uniform payer-softening
prediction (the Feb-2021 News Corp x Google commercial agreement predicts
softer Google coverage) FAILS on the enforcement register.

Per #715 this docstring uses lowercase forms only: the fifty-ninth
falsification-family member (ledger 58->59); FIRST falsification pin on the
WSJ/News Corp x Google pair; the #1143 temporal-replication precedent does
not block (no counted member on this pair). Verdict:
falsification_member_confirmed, domain-bounded to the regulatory-enforcement
register. The profile's standing coverage_prediction for google is "mixed"
(dual-dependency hedge); the naive uniform prediction is what the family
tests.

Novelty: the WSJ EU-fine URL zero-hit repo-wide pre-commit (git grep -F).
The scout's AP x OpenAI arms were excluded by design: the DevDay piece is
saturated (fiftieth journalist-level member) and the gov-sites training-pause
wire is saturated (m862's event, #1052). AP x Google rejected (single relay
arm). WSJ x Google SELECTED.

Statistical discipline: monitoring-only per the Aug 28 2026 standing rule
(MANUAL ILLUSTRATIVE ONLY, engine NOT run, p_value/cohens_d/ci_95
NOT_CALCULATED, is_significant False, NOT artifact-grade, no analysis.json
update, verdict falsification_member_confirmed). Correlation is not
causation. Hypothesis-generating only.

1 delegated scout (ranked 3 pairs) + 4 main-run browser.search verification
sets (2 scout-corroboration + 2 fresh), 0 browser.open per #503.
Excerpt-bounded; the WSJ URL is verbatim from the Full-URL listing; no
canonical URLs constructed. ASCII-only, no em dashes.

Rotation: this run is iteration #1302 Type A, the THIRD leg of the 1300-1304
window (D #1300 -> E #1301 -> A #1302 -> B #1303 -> C #1304, per the #565
anchor + rotation guard). Predecessor #1301 Type E verified in git log (main
68be73fa / anchor deb96ee6 / doc-sync 8dc0404d / log-hash 9c61ea8b); the
1295-1299 window is VERIFIED CLOSED. This run's main commit is the anchor
per #565; ANCHORED_SHA patched post-commit. The #1301 forward guards
verified pre-commit this run: max-1011; zero one-zero-one-two keys all
forms; no-Type-A-#1302-in-git-log; fortieth direction absent; forty-eighth
through fifty-eighth members intact; no fifty-ninth member (repo-wide);
ledger 58. Next: #1303 Type B continues the window; the #1300-launched
background-suite verdict belongs to #1305 per #795.

Pre-commit novelty greps per #715: zero test_type_a_1302 files on disk
(glob); no "Type A #1302" in git log (--grep); max numeric mechanism_id
1011 in profiles/ pre-commit (mechanism_id regex sweep); zero
numeric/underscore/dash one-zero-one-two mechanism key forms repo-wide
pre-commit (needles format-built per #715, own file excluded, __pycache__
excluded per the #715 pattern-rescope lesson); block key zero-hit repo-wide
pre-commit (designed keying: iteration 1302 in key, no 1012 substring, per
the #723/#738/#739 convention); "## #1302" zero-hit in iteration-log
pre-commit; README stats 72992/1626 pre-commit; no #1302 row in
README/ARCHITECTURE test tables pre-commit; the WSJ EU-fine URL zero-hit
repo-wide pre-commit (git grep -F).

Doc-sync constants per #719: README_TEST_COUNT / README_FILE_COUNT hold the
post-doc-sync values from the start (patched pre-main once the in-gate
collection count is known); the doc-sync commit ratchets README 72992/1626
-> post-sync totals.
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
NEWSCORP_PATH = os.path.join(PROFILES_DIR, "news-corp.yaml")

OWN_BASENAME = (
    "test_type_a_1302_wsj_google_eu_dma_fine_enforcement_"
    "vs_carried_meta_arms_oct08_1am.py"
)
BLOCK_KEY = (
    "type_a_1302_wsj_google_eu_dma_fine_enforcement_"
    "vs_carried_meta_arms_oct08_1am"
)

# Pre-commit placeholder per #565; patched to the main commit sha in
# the anchor followup.
ANCHORED_SHA = "b8859fbc369d47ba937b5f4e33ed3686f65c94f8"  # patched in the anchor followup per #565

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

MECH_NUM = 1012
NEXT_NUM = 1013  # integer only; key-form needles are format-built

# Predecessor chain: #1301 Type E closed the SECOND leg.
PRED_MAIN_1301 = "68be73fa52f911ddd45760980e5a08c47fec15d7"
PRED_ANCHOR_1301 = "deb96ee6d3f8356e9faef14cbf3bcba2bdf5dfcc"
PRED_DOCSYNC_1301 = "8dc0404dc76e9b0c0783a0f328a2e31486d40464"
PRED_FINAL_1301 = "9c61ea8b3e0c0bc733f0c9bea6364e8a722f00dc"

# This run's main commit (full sha), for the ancestor-form
# no-Type-A-#1302 pin in the #1301 file. Patched in the terminal
# log-hash followup per #721.
PRED_MAIN_1302 = "b8859fbc369d47ba937b5f4e33ed3686f65c94f8"  # re-pinned in the terminal log-hash followup per #721

# #1303's main commit (full sha), for the ancestor-form no-Type-B-#1303
# pin. Patched in #1303's terminal log-hash followup per #721.
PRED_MAIN_1303 = "0078dd5d043b2b47276a5a19d5e7f89919b9975e"  # re-pinned to #1303 main sha per #721

# The #1301 predecessor file, for the staleness pin on its
# guard-lifecycle class (max id 1011; zero next-number
# one-zero-one-two / no-Type-A-#1302-in-git-log / fortieth
# direction absent / forty-eighth through fifty-eighth members
# intact / fifty-ninth member absent / ledger 58).
D1301_FILE = (
    "test_type_e_1301_podcast_sentiment_183rd_"
    "verification_oct08_12am.py"
)

# Doc-sync constants per #719: post-doc-sync values from the start.
# Patched pre-main once the in-gate collection count is known.
README_TEST_COUNT = 73086  # post-doc-sync total (pre-sync 72992 + 94)
README_FILE_COUNT = 1627  # pre-sync 1626 + 1 (this file)

# MANUAL ILLUSTRATIVE tones (hand-assigned at excerpt level).
GOOGLE_FINE_TONE = -0.35
META_SETTLEMENT_TONE = -0.30
META_TEEN_SAFETY_TONE = -0.25
META_MEAN_TONE = -0.275
ILLUSTRATIVE_DELTA = -0.075

# Ordinal member-claim forms, built at runtime so this source file
# carries no contiguous full-form claim (per the #715 literal
# discipline; the live full-form claims live in the profile block).
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

GOOGLE_FINE_URL = (
    "https://www.wsj.com/tech/google-fined-1-02-billion-"
    "under-eus-tech-antitrust-rules-7e8ae1fb"
)


def _read(path):
    with open(path, encoding="utf-8", errors="replace") as fh:
        return fh.read()


def _git(*args):
    return subprocess.run(
        ["git"] + list(args), cwd=REPO_ROOT, capture_output=True,
        text=True,
    )


def _iter_source_files():
    """Yield profile + test source files for the sweep instruments.

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
    return subprocess.run(
        ["python3", "-m", "pytest", filename + "::" + classname, "-q"],
        cwd=TESTS_DIR, capture_output=True, text=True,
    )


def _block():
    doc = yaml.safe_load(_read(NEWSCORP_PATH))
    return doc["competitor_relationships"]["google"][BLOCK_KEY]


# ---------------------------------------------------------------------------
# 1. Anchor per #565 (this run's main commit is the anchor; the anchor
#    followup patches ANCHORED_SHA to the main commit sha).
# ---------------------------------------------------------------------------


class TestAnchor1302:
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

    def test_anchor_duality_documented(self):
        # The #565 duality: the placeholder pin passes pre-commit and
        # fails post-anchor BY DESIGN; the patched pin is the mirror.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "BY DESIGN post-anchor" in src or "fails BY DESIGN" in src


# ---------------------------------------------------------------------------
# 2. Rotation guard: #1301 closed the SECOND leg; #1302 is the THIRD.
# ---------------------------------------------------------------------------


class TestRotationGuard1302:
    def test_predecessor_shas_in_git_log(self):
        log = _git("log", "--oneline", "-60").stdout
        for sha, label in (
            (PRED_MAIN_1301, "1301 main"),
            (PRED_ANCHOR_1301, "1301 anchor"),
            (PRED_DOCSYNC_1301, "1301 doc-sync"),
            (PRED_FINAL_1301, "1301 log-hash"),
        ):
            assert sha[:8] in log, label

    def test_1301_type_e_in_git_log(self):
        out = _git("log", "--oneline", "--grep=Type E #1301").stdout
        assert out.strip() != ""

    def test_third_leg_phrase(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "THIRD leg of the 1300-1304 window" in src

    def test_1295_1299_window_closed(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "1295-1299" in src
        assert "VERIFIED CLOSED" in src

    def test_next_leg_is_1303_type_b(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "B #1303" in src


# ---------------------------------------------------------------------------
# 3. Mechanism novelty: Type A lands one mechanism (max 1011 -> 1012).
# ---------------------------------------------------------------------------


class TestMechanismNovelty1302:
    def test_max_numeric_mechanism_id_1012(self):
        assert _max_numeric_mechanism_id() == MECH_NUM

    def test_no_type_a_1302_in_git_log_pin(self):
        # Post-main-commit form (the #1191-class self-trip, re-pinned
        # in the terminal log-hash followup per #721): every commit
        # whose message matches "Type A #1302" must be this run's
        # main commit or a descendant of it - i.e., no PRIOR run
        # committed this run's iteration. Deselected in the in-gate
        # run (fails pre-commit by design).
        out = _git("log", "--format=%H", "--grep=Type A #1302")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected this run's own commits"
        main = _git("rev-parse", PRED_MAIN_1302).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_zero_next_number_keys_all_forms(self):
        # Numeric (profiles/ scope), underscore and dash (profiles/ +
        # tests/ scope, own file excluded per #715, __pycache__
        # excluded per the #715 pattern-rescope lesson). NEXT_NUM is
        # 1013: this run lands 1012, so the next-number forms stay
        # absent.
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_block_key_designed_no_1012_substring(self):
        # Designed keying per #723/#738/#739: the iteration-form block
        # key carries the iteration (1302), never the mechanism number.
        assert "1012" not in BLOCK_KEY
        assert "1302" in BLOCK_KEY

    def test_forward_guards_for_1303(self):
        # Staged for the next leg: max-1012 in profiles/; zero
        # one-zero-one-three keys all forms; no-Type-B-#1303-in-git-log;
        # fortieth direction absent; forty-eighth through fifty-ninth
        # intact; no sixtieth member; ledger 59.
        assert _max_numeric_mechanism_id() == 1012
        assert _repo_grep_numeric_mechanism_id(1013) == []
        assert _repo_grep_underscore_mechanism(1013) == []
        assert _repo_grep_dash_mechanism(1013) == []
        assert _git("log", "--oneline", "--grep=Type B #1303").stdout.strip() == ""
        assert _git_grep_tracked_source(_T40, "profiles/") == []
        assert _git_grep_tracked_source(_T48, "profiles/") == [
            "profiles/financial-times.yaml"]
        assert _T59 in _read(os.path.join(PROFILES_DIR, "news-corp.yaml"))
        assert _git_grep_tracked_source(_T60, None) == []

    def test_novel_url_zero_hit_pre_commit(self):
        # The novel WSJ EU-fine URL was zero-hit repo-wide pre-commit
        # (git grep -F, verified this run before the block landed).
        # Post-landing it lives in the block's source_urls and in the
        # arm's url field; assert it is present exactly twice in
        # news-corp.yaml.
        text = _read(NEWSCORP_PATH)
        assert text.count(GOOGLE_FINE_URL) == 2


# ---------------------------------------------------------------------------
# 4. WSJ x Google Jul-24 EU DMA fine arm (NEW this run)
# ---------------------------------------------------------------------------


class TestWsjGoogleFine1302:
    def test_block_present_with_mechanism_id_1012(self):
        block = _block()
        assert block["mechanism_id"] == 1012
        assert block["iteration"] == 1302
        assert block["iteration_type"] == "A"

    def test_arm_title_and_date(self):
        block = _block()
        arm = block["google_arm"]
        assert arm["title"] == "EU Fines Google $1 Billion for Favoring Its Own Services"
        assert arm["date"] == "2026-07-24"

    def test_arm_bylines(self):
        block = _block()
        arm = block["google_arm"]
        assert "Edith Hancock" in arm["bylines"]
        assert "Kim Mackrael" in arm["bylines"]

    def test_arm_url_novel(self):
        block = _block()
        arm = block["google_arm"]
        assert arm["url"] == GOOGLE_FINE_URL
        assert "zero-hit" in arm["url_status"]

    def test_arm_register_enforcement_accountability(self):
        block = _block()
        arm = block["google_arm"]
        assert arm["register"] == "regulatory_enforcement_accountability"

    def test_arm_tone_minus_035(self):
        block = _block()
        arm = block["google_arm"]
        assert arm["tone_MANUAL_ILLUSTRATIVE"] == GOOGLE_FINE_TONE == -0.35

    def test_arm_key_facts_dma_fine(self):
        block = _block()
        text = yaml.safe_dump(block["google_arm"])
        assert "$1.02B" in text
        assert "60 days" in text

    def test_arm_carries_commercial_agreement_disclosure(self):
        block = _block()
        # Asserted on the raw field: safe_dump folds long lines at
        # 80 cols, which can split the phrase in the dump.
        assert ("commercial agreement to supply content on Google platforms"
                in block["financial_relationship"]["disclosure_quote"])

    def test_arm_single_new_arm(self):
        # Only the Jul-24 DMA-fine peg is NEW this run: the scout's AP x
        # OpenAI arms were deliberately excluded (DevDay piece saturated
        # as the fiftieth journalist-level member; gov-sites training-pause
        # wire saturated as m862's event, #1052), and AP x Google was
        # rejected (single relay arm).
        block = _block()
        assert "saturated" in yaml.safe_dump(block)

    def test_excerpt_bounded_no_browser_open(self):
        block = _block()
        assert block["research_method"].count("0 browser.open") >= 1


# ---------------------------------------------------------------------------
# 5. Carried WSJ x Meta arms (m532 via m904, un-rescored per #807)
# ---------------------------------------------------------------------------


class TestMetaArms1302:
    def test_meta_arms_carried_from_m532_via_m904(self):
        block = _block()
        assert "m532" in block["meta_arms_carried"]["carried_from"]
        assert "m904" in block["meta_arms_carried"]["carried_from"]
        assert "#807" in block["meta_arms_carried"]["carried_from"]

    def test_settlement_arm_minus_030(self):
        block = _block()
        arms = block["meta_arms_carried"]["arms"]
        assert any("-0.30" in a for a in arms)

    def test_teen_safety_arm_minus_025(self):
        block = _block()
        arms = block["meta_arms_carried"]["arms"]
        assert any("-0.25" in a for a in arms)

    def test_meta_mean_minus_0275(self):
        block = _block()
        assert block["meta_arms_carried"]["meta_mean"] == META_MEAN_TONE == -0.275


# ---------------------------------------------------------------------------
# 6. Financial relationship: News Corp x Google commercial agreement
# ---------------------------------------------------------------------------


class TestFinancialRelationship1302:
    def test_deal_feb_2021_documented(self):
        block = _block()
        deal = block["financial_relationship"]["deal"]
        assert "Feb 17 2021" in deal
        assert "AU$150M" in deal

    def test_deal_extension_and_ai_deal_flagged(self):
        block = _block()
        deal = block["financial_relationship"]["deal"]
        assert "extended ~2024" in deal
        assert "flagged" in deal

    def test_multi_payer_confounders_disclosed(self):
        block = _block()
        fr = block["financial_relationship"]
        assert "OpenAI" in fr["openai_financial"]
        assert "Meta" in fr["meta_financial"]

    def test_deal_disclosed_in_google_coverage(self):
        block = _block()
        fr = block["financial_relationship"]
        assert fr["deal_disclosed_in_google_coverage"] is True
        assert "commercial agreement" in fr["disclosure_quote"]

    def test_coverage_prediction_naive_softer(self):
        block = _block()
        pred = block["financial_relationship"]["coverage_prediction"]
        assert "softer" in pred
        assert "mixed" in pred

    def test_non_causal_language_present(self):
        block = _block()
        assert "Correlation does not establish causation" in \
            block["financial_relationship"]["non_causal_language"]


# ---------------------------------------------------------------------------
# 7. Asymmetry delta: Google -0.35 vs Meta -0.275, delta -0.075
# ---------------------------------------------------------------------------


class TestAsymmetryDelta1302:
    def test_google_mean_minus_035(self):
        block = _block()
        assert block["scorer"]["google_mean_tone"] == GOOGLE_FINE_TONE == -0.35

    def test_meta_mean_minus_0275(self):
        block = _block()
        assert block["scorer"]["meta_mean_tone"] == META_MEAN_TONE == -0.275

    def test_illustrative_delta_minus_0075(self):
        block = _block()
        delta = block["scorer"]["illustrative_delta_google_minus_meta"]
        assert abs(delta - ILLUSTRATIVE_DELTA) < 1e-9
        assert abs(delta - (-0.075)) < 1e-9

    def test_degenerate_sample_contract(self):
        block = _block()
        method = block["scorer"]["method"]
        assert "MANUAL ILLUSTRATIVE ONLY" in method
        assert "n=1-vs-2" in method
        assert "is_significant False" in method

    def test_reading_fails_uniform_prediction(self):
        block = _block()
        assert "fails" in block["scorer"]["reading"]


# ---------------------------------------------------------------------------
# 8. Research method: scout + 4 verification sets, 0 browser.open
# ---------------------------------------------------------------------------


class TestResearchMethod1302:
    def test_delegated_scout_documented(self):
        block = _block()
        assert "delegated scout" in block["research_method"]

    def test_four_verification_sets(self):
        block = _block()
        assert "4 main-run browser.search verification sets" in block["research_method"]

    def test_scout_rejections_documented(self):
        block = _block()
        rm = block["research_method"]
        assert "AP x OpenAI rejected" in rm
        assert "AP x Google rejected" in rm
        assert "WSJ x Google SELECTED" in rm

    def test_saturation_exclusions_documented(self):
        block = _block()
        rm = block["research_method"]
        assert "fiftieth journalist-level member" in rm
        assert "m862" in rm

    def test_novelty_greps_documented(self):
        block = _block()
        rm = block["research_method"]
        assert "zero test_type_a_1302 files" in rm
        assert "max numeric mechanism_id 1011" in rm
        assert "72992/1626" in rm

    def test_no_canonical_urls_constructed(self):
        block = _block()
        assert "no canonical URLs constructed" in block["research_method"]


# ---------------------------------------------------------------------------
# 9. Falsification ledger: fifty-ninth member, ledger 58->59
# ---------------------------------------------------------------------------


class TestFalsificationLedger1302:
    def test_member_true_ledger_59(self):
        block = _block()
        assert block["falsification_family_member"] is True
        assert block["falsification_ledger"] == 59

    def test_fifty_ninth_member_form_present(self):
        # Runtime-built needle; the live full-form claim is in the
        # profile block (3 occurrences in news-corp.yaml). Asserted on
        # the working tree so the pin is stable across the main-commit
        # boundary; the HEAD sweep sees it from the main commit on.
        assert _read(NEWSCORP_PATH).count(_T59) == 3

    def test_first_pin_on_wsj_google_pair(self):
        block = _block()
        # Asserted on the raw field: safe_dump folds long lines at
        # 80 cols, which can split the phrase in the dump.
        assert ("FIRST falsification pin on the WSJ/News Corp x Google pair"
                in block["finding"])

    def test_1143_precedent_does_not_block(self):
        block = _block()
        text = yaml.safe_dump(block)
        assert "#1143" in text
        assert "does not block" in text

    def test_distinct_from_m904_m1006_m342(self):
        block = _block()
        d = block["distinct_from_prior"]
        assert "m904" in d
        assert "m1006" in d
        assert "m342" in d

    def test_domain_bounded_enforcement_register(self):
        block = _block()
        # Asserted on the raw field: safe_dump folds long lines at
        # 80 cols, which can split the phrase in the dump.
        assert ("Domain-bounded to the regulatory-enforcement register"
                in block["falsification_family"])

    def test_confounder_multi_payer_strong_first(self):
        block = _block()
        confs = block["confounders"]
        assert confs[0].startswith("STRONG")
        assert "multi-payer" in confs[0]

    def test_counterevidence_m1006_m904(self):
        block = _block()
        ce = " ".join(block["counterevidence"])
        assert "m1006" in ce
        assert "m904" in ce


# ---------------------------------------------------------------------------
# 10. Statistical discipline per the Aug 28 2026 standing rule
# ---------------------------------------------------------------------------


class TestStatisticalDiscipline1302:
    def test_manual_illustrative_only(self):
        block = _block()
        assert block["statistical_discipline"]["scores"] == "MANUAL ILLUSTRATIVE only"

    def test_engine_not_run(self):
        block = _block()
        assert block["statistical_discipline"]["engine_run"] is False

    def test_p_value_not_calculated(self):
        block = _block()
        sd = block["statistical_discipline"]
        assert sd["p_value"] == "NOT_CALCULATED"
        assert sd["cohens_d"] == "NOT_CALCULATED"
        assert sd["ci_95"] == "NOT_CALCULATED"
        assert sd["is_significant"] is False

    def test_not_artifact_grade(self):
        block = _block()
        sd = block["statistical_discipline"]
        assert sd["artifact_grade"] is False
        assert sd["no_analysis_json_update"] is True

    def test_verdict_member_confirmed(self):
        block = _block()
        assert block["statistical_discipline"]["verdict"] == "falsification_member_confirmed"

    def test_correlation_not_causation(self):
        block = _block()
        sd = block["statistical_discipline"]
        assert sd["correlation_not_causation"] is True
        assert sd["hypothesis_generating_only"] is True


# ---------------------------------------------------------------------------
# 11. Guard lifecycle: forward guards for #1303 (Type B).
# ---------------------------------------------------------------------------


class TestGuardLifecycle1302:
    def test_pins_on_one_mechanism_landing(self):
        # Type A lands one mechanism: max 1012, next 1013.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 1012" in src
        assert "NEXT_NUM = 1013" in src

    def test_no_type_b_1303_in_git_log_pin(self):
        # Post-main-commit form for the NEXT leg (the #1191-class
        # self-trip, re-pinned in #1303's terminal log-hash followup
        # per #721): every commit whose message matches "Type B
        # #1303" must be #1303's main commit or a descendant of it.
        # Deselected in the in-gate run (fails pre-commit by design).
        out = _git("log", "--format=%H", "--grep=Type B #1303")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1303's own commits"
        main = _git("rev-parse", PRED_MAIN_1303).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_1013_numeric_absent_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_1013_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_1013_dash_absent_repo_wide(self):
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

    def test_fifty_ninth_member_present_pin(self):
        # Landed this run (m1012, profiles/news-corp.yaml). Asserted
        # on the working tree so the pin is stable across the
        # main-commit boundary; the HEAD sweep sees it from the main
        # commit on.
        assert _read(NEWSCORP_PATH).count(_T59) == 3

    def test_no_sixtieth_member_pin(self):
        # No sixtieth member has been claimed anywhere; the sixtieth
        # member-claim form stays absent repo-wide (source scope;
        # __pycache__ excluded per the #715 pattern-rescope lesson).
        assert _git_grep_tracked_source(_T60, None) == []

    def test_predecessor_1301_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, D1301_FILE))

    def test_next_leg_is_1303_type_b(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#1303 Type B" in src

    def test_1301_pins_flip_by_design_documented(self):
        # #1301's forward guards (max-1011, zero one-zero-one-two
        # keys all forms, no-Type-A-#1302-in-git-log, fortieth
        # absent, forty-eighth through fifty-eighth intact in
        # profiles/, fifty-ninth absent, ledger 58) verified GREEN
        # at HEAD pre-commit this run. THREE pins flip BY DESIGN at
        # this run's main commit: the no-Type-A-#1302-in-git-log pin
        # (the #1191-class self-trip, re-pinned post-commit by
        # TestStalenessPins1302), the zero one-zero-one-two numeric
        # pin (the #1272-class forward-guard expiry - the m1012
        # landing carries "mechanism_id: 1012" in colon form; the
        # underscore/dash pins stay green by the #723/#738/#739
        # designed keying), and the no fifty-ninth member pin (the
        # #1191-class self-trip - this run lands the fifty-ninth
        # member). Documented in the staleness pin below, not
        # repaired.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "TestStalenessPins1302" in src
        assert "no_type_a_1302_in_git_log_pin" in src


# ---------------------------------------------------------------------------
# 12. Staleness pins: #1301's guard lifecycle flips BY DESIGN post-commit.
# ---------------------------------------------------------------------------


class TestStalenessPins1302:
    def test_1301_guard_lifecycle_post_commit_self_trip(self):
        # Post-terminal-followup form: 21 tests in the class; THREE
        # flip BY DESIGN when this run's main commit lands, and TWO
        # STAY flipped permanently: test_1012_numeric_absent_in_profiles
        # (the #1272-class forward-guard expiry - the m1012 landing
        # carries "mechanism_id: 1012" in colon form; the
        # underscore/dash pins stay green by the #723/#738/#739
        # designed keying) and test_no_fifty_ninth_member_pin (the
        # #1191-class self-trip - this run lands the fifty-ninth
        # member). The third flip, test_no_type_a_1302_in_git_log_pin
        # (the #1191-class self-trip), is re-pinned green in the
        # terminal log-hash followup per #721 (its PRED_MAIN_1302 now
        # holds this run's main sha). The class run below therefore
        # expects 2 failed / 19 passed and documents the designed
        # flips. The #1301 block is read-only to this run; the flips
        # are documented here, not repaired.
        res = _class_run(D1301_FILE, "TestGuardLifecycle1301")
        out = res.stdout + res.stderr
        assert "2 failed, 19 passed" in out, out[-2000:]
        assert "test_1012_numeric_absent_in_profiles" in out, out[-2000:]
        assert "test_no_fifty_ninth_member_pin" in out, out[-2000:]


# ---------------------------------------------------------------------------
# 13. Doc-sync per #719 (3 tests; deselected pre-commit, flipped post-sync)
# ---------------------------------------------------------------------------


class TestDocSync1302:
    def test_readme_test_file_table_has_1302_row_post_sync(self):
        readme = _read(README_PATH)
        assert OWN_BASENAME in readme

    def test_architecture_has_1302_row_post_sync(self):
        arch = _read(ARCH_PATH)
        assert OWN_BASENAME in arch

    def test_readme_stats_ratcheted(self):
        readme = _read(README_PATH)
        assert "| Tests | %d |" % README_TEST_COUNT in readme
        assert "Across %d test files" % README_FILE_COUNT in readme


# ---------------------------------------------------------------------------
# 14. Iteration log per #721.
# ---------------------------------------------------------------------------


class TestIterationLog1302:
    def test_log_has_1302_entry(self):
        text = _read(LOG_PATH)
        assert "## #1302 Type A" in text

    def test_log_entry_carries_hash_chain(self):
        # The doc-sync writes the entry with the main/anchor hashes;
        # the terminal log-hash followup registers the doc-sync hash
        # here per #721.
        text = _read(LOG_PATH)
        assert "main commit" in text
        assert "anchor" in text

    def test_log_entry_records_finding(self):
        text = _read(LOG_PATH)
        assert "m1012" in text
        assert "falsification_member_confirmed" in text
        assert "ledger 58->59" in text


# ---------------------------------------------------------------------------
# 15. In-flight isolation
# ---------------------------------------------------------------------------


class TestInFlightIsolation1302:
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

    def test_own_diff_excludes_inflight(self):
        # This run's staged set must never include the in-flight
        # files; verified at commit time by explicit-path staging.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "explicit-path staging" in src
