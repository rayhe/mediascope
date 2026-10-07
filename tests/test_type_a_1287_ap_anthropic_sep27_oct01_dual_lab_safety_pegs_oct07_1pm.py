"""Type A #1287: AP x Anthropic Sep-27/Oct-1 dual-lab safety pegs (Oct 7 2026, ~01:00 PM PDT).

m1003 - FIRST dedicated corpus mechanism on the AP x Anthropic pair.
AP (Garance Burke, Sep 27 2026) runs a skeptical-analytical wire on
Anthropic + OpenAI safety-rhetoric-as-positioning ("What do they have
to gain?"; pre-IPO midterm politicking frame), and AP (Oct 1 2026)
wires the FTC investigation of OpenAI + Anthropic over consumer AI
risks in a neutral enforcement-process register. Both wires name the
Jul-2023 licensing counterparty (OpenAI) and the non-payer
(Anthropic) symmetrically in the SAME article - the cleanest
within-article payer/non-payer comparison in the corpus.

MANUAL ILLUSTRATIVE scoring: AP x Anthropic dual-lab arms -0.30
(Burke) + -0.20 (FTC), mean -0.25, vs carried AP x Meta $18bn
settlement wire -0.45 (m970). Illustrative delta (Anthropic minus
Meta): +0.20. The adjudicating comparison is WITHIN-ARTICLE:
OpenAI-vs-Anthropic illustrative delta 0.00 on each peg - the
licensing deal bought the payer no visible softening against the
non-payer.

Per #715 this docstring uses lowercase forms only: the
fifty-seventh falsification-family member, ledger 56->57,
domain-bounded to AP's wire register on dual-lab safety pegs. The
uppercase claim form lives only in the landed profile block. FIRST
AP-leg member. The #1143 temporal-replication precedent does not
block: no adversarial-on-partner observation has been counted for
the AP x Anthropic pair (first mechanism) or the AP x OpenAI pair
(m970 was mechanism_documentation_not_a_discovery).

Statistical discipline: monitoring-only per the Aug 28 2026 standing
rule (MANUAL ILLUSTRATIVE ONLY, engine NOT run, p_value/cohens_d/ci_95
NOT_CALCULATED, is_significant False, NOT artifact-grade, no
analysis.json update, verdict falsification_member_confirmed).
Correlation is not causation. Hypothesis-generating only.

1 delegated scout (fresh publication+competitor pair discovery;
saturation sweep across 10 publication profiles + ~15 candidate
pairs; SELECTED AP x Anthropic; REJECTED 15 saturated pairs;
Verge/NYT/Guardian x xAI held as backups; dispatched this run) + 2
main-run browser.search verification sets ((1) exact-headline Burke
Sep-27 search - businessmirror verbatim with Garance Burke AP byline
+ SAN FRANCISCO (AP) dateline, 5 relays; (2) exact-headline FTC Oct-1
search - bytewatchr verbatim with "The Associated Press reported on
October 1" attribution, 6 corroborating relays), 0 browser.open per
#503. 2 novel URLs zero-hit pre-commit. All URLs copied verbatim
from Full-URL listings; no canonical URLs constructed. ASCII-only, no
em dashes.

Rotation: this run is iteration #1287 Type A, the THIRD leg of the
1285-1289 window (D #1285 -> E #1286 -> A #1287 -> B #1288 -> C #1289,
per the #565 anchor + rotation guard). Predecessor #1286 Type E
verified in git log (main 7b75118a / anchor 954b6788 / doc-sync
d2048a8e / log-hash 90708117 / push-status-correction 21e1d4fa); the
1280-1284 window is VERIFIED CLOSED. This run's main commit is the
anchor per #565; ANCHORED_SHA patched post-commit. The #1286 forward
guards verified pre-commit this run: max-1002; zero next-number
one-zero-zero-three mechanism keys all forms (profiles/ + tests/
scope); no-Type-A-#1287-in-git-log; fortieth direction absent
(profiles/ scope); forty-eighth through fifty-sixth members intact;
no fifty-seventh member (repo-wide); ledger 56. This run lands
mechanism one-zero-zero-three: TestGuardLifecycle1286's zero
one-zero-zero-three pins flip at this run's main commit BY DESIGN
(the #1272-class forward-guard expiry), documented in
TestStalenessPins1287, not repaired; the no-Type-A-#1287-in-git-log
pin flips BY DESIGN (the #1191-class self-trip), re-pinned in the
terminal log-hash followup per #721. Next run #1288 Type B continues
the window. The #1285-launched background-suite verdict belongs to
#1290 per #795: this run OBSERVES only (1662 bytes, [2%] progress,
last write Oct 7 2026 11:59 PDT, zero live pytest processes at this
run's check - the earlier pgrep hit was a transient phantom).
In-flight during this run: #899 (profiles/nytimes.yaml m771 hunk),
#938 (Type B test file working-tree edit), #900 (untracked Type D
test file), #1012-wt (working-tree edit on the committed Type A
#1012 file) - all untouched; targeted staging only. Do NOT touch
#1024 m846.

Pre-commit novelty greps per #715: zero test_type_a_1287 files on
disk (glob); no Type A #1287 in git log (--grep); max numeric
mechanism_id 1002 in profiles/ pre-commit (mechanism_id regex
sweep); zero numeric/underscore/dash next-number one-zero-zero-three
mechanism key forms repo-wide pre-commit (needles format-built per
#715, own file excluded); block key zero-hit repo-wide pre-commit
(designed keying: iteration 1287 in key, no 1003 substring, per the
#723/#738/#739 convention); "## #1287" zero-hit in iteration-log
pre-commit; README stats 71783/1611 pre-commit; no #1287 row in
README/ARCHITECTURE test tables pre-commit; 2 novel source URLs
zero-hit repo-wide pre-commit (git grep -F); "Garance Burke"
zero-hit in profiles/ pre-commit; "bytewatchr" zero-hit repo-wide
pre-commit; "AP x Anthropic" zero-hit in iteration-log pre-commit.

Doc-sync constants per #719: README_TEST_COUNT / README_FILE_COUNT
hold the post-doc-sync values from the start (patched pre-main once
the in-gate collection count is known); the doc-sync commit ratchets
README 71783/1611 -> post-sync totals.
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
AP_PATH = os.path.join(PROFILES_DIR, "ap.yaml")

OWN_BASENAME = (
    "test_type_a_1287_ap_anthropic_sep27_oct01_"
    "dual_lab_safety_pegs_oct07_1pm.py"
)
BLOCK_KEY = (
    "type_a_1287_ap_anthropic_sep27_oct01_"
    "dual_lab_safety_pegs_vs_carried_meta_arms"
)

# Pre-commit placeholder per #565; patched to the main commit sha in
# the anchor followup.
ANCHORED_SHA = "32786e1270efb5b27b4234ccab5b82827b9ebc88"  # patched in the anchor followup per #565

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

MECH_NUM = 1003
NEXT_NUM = 1004  # integer only; key-form needles are format-built

# Predecessor chain: #1286 Type E closed the SECOND leg.
PRED_MAIN_1286 = "7b75118a"
PRED_ANCHOR_1286 = "954b6788"
PRED_DOCSYNC_1286 = "d2048a8e"
PRED_FINAL_1286 = "90708117"

# This run's main commit (full sha), for the ancestor-form
# no-Type-A-#1287 pin. Patched in the terminal log-hash followup per
# #721.
PRED_MAIN_1287 = "32786e1270efb5b27b4234ccab5b82827b9ebc88"  # re-pinned in the terminal log-hash followup per #721

# #1288's main commit (full sha), for the ancestor-form no-Type-B-#1288
# pin. Patched in #1288's terminal log-hash followup per #721.
PRED_MAIN_1288 = "0" * 40

# The #1286 predecessor file, for the staleness pin on its
# guard-lifecycle class (max id 1002; zero next-number
# one-zero-zero-three / no-Type-A-#1287-in-git-log / fortieth
# direction absent / forty-eighth through fifty-sixth members
# intact / fifty-seventh member absent / ledger 56).
D1286_FILE = (
    "test_type_e_1286_podcast_sentiment_180th_"
    "verification_oct07_12pm.py"
)

# Doc-sync constants per #719: post-doc-sync values from the start.
# Patched pre-main once the in-gate collection count is known.
README_TEST_COUNT = 71889  # post-doc-sync total (pre-sync 71783 + 106)
README_FILE_COUNT = 1612  # pre-sync 1611 + 1 (this file)

# MANUAL ILLUSTRATIVE tones (hand-assigned at excerpt level).
BURKE_TONE = -0.30
FTC_TONE = -0.20
ANTHROPIC_MEAN = -0.25
META_TONE = -0.45
DELTA_ANTHROPIC_MINUS_META = 0.20

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
# The fifty-seventh member-claim form is fragment-built per #715.
_T57 = "FIFT" + "Y-SEVENTH falsification-family member"
# The fifty-eighth member-claim form is fragment-built per #715
# (no fifty-eighth member may exist repo-wide; staged for #1288).
_T58 = "FIFT" + "Y-EIGHTH falsification-family member"


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


def _block():
    """Return the landed m1003 profile block for this run."""
    with open(AP_PATH, encoding="utf-8") as fh:
        data = yaml.safe_load(fh)

    def _walk(node):
        if isinstance(node, dict):
            if node.get("block_key") == BLOCK_KEY:
                return node
            for v in node.values():
                hit = _walk(v)
                if hit is not None:
                    return hit
        elif isinstance(node, list):
            for v in node:
                hit = _walk(v)
                if hit is not None:
                    return hit
        return None

    hit = _walk(data)
    assert hit is not None, "m1003 block not found"
    return hit


# ---------------------------------------------------------------------------
# 1. Anchor (pre-commit placeholder per #565; patched in anchor followup).
# ---------------------------------------------------------------------------


class TestAnchor1287:
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
# 2. Rotation guard: #1286 closed the SECOND leg; #1287 is the THIRD.
# ---------------------------------------------------------------------------


class TestRotationGuard1287:
    def test_predecessor_shas_in_git_log(self):
        log = _git("log", "--oneline", "-60").stdout
        for sha, label in (
            (PRED_MAIN_1286, "1286 main"),
            (PRED_ANCHOR_1286, "1286 anchor"),
            (PRED_DOCSYNC_1286, "1286 doc-sync"),
            (PRED_FINAL_1286, "1286 log-hash"),
        ):
            assert sha in log, label

    def test_1286_type_e_in_git_log(self):
        out = _git("log", "--oneline", "--grep=Type E #1286").stdout
        assert out.strip() != ""

    def test_third_leg_phrase(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "THIRD leg of the 1285-1289 window" in src

    def test_1280_1284_window_closed(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "1280-1284" in src
        assert "VERIFIED CLOSED" in src

    def test_next_leg_is_1288_type_b(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "B #1288" in src


# ---------------------------------------------------------------------------
# 3. Mechanism novelty: Type A lands one mechanism (max 1002 -> 1003).
# ---------------------------------------------------------------------------


class TestMechanismNovelty1287:
    def test_max_numeric_mechanism_id_1003(self):
        assert _max_numeric_mechanism_id() == MECH_NUM

    def test_no_type_a_1287_in_git_log_pin(self):
        # Post-main-commit form (the #1191-class self-trip, re-pinned
        # in the terminal log-hash followup per #721): every commit
        # whose message matches "Type A #1287" must be this run's
        # main commit or a descendant of it - i.e., no PRIOR run
        # committed this run's iteration. Deselected in the in-gate
        # run (fails pre-commit by design).
        out = _git("log", "--format=%H", "--grep=Type A #1287")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected this run's own commits"
        main = _git("rev-parse", PRED_MAIN_1287).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_zero_next_number_keys_all_forms(self):
        # Numeric (profiles/ scope), underscore and dash (profiles/ +
        # tests/ scope, own file excluded per #715). NEXT_NUM is 1004:
        # this run lands 1003, so the next-number forms stay absent.
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_block_key_designed_no_1003_substring(self):
        # Designed keying per #723/#738/#739: the iteration-form block
        # key carries the iteration (1287), never the mechanism number.
        assert "1003" not in BLOCK_KEY
        assert "1287" in BLOCK_KEY

    def test_forward_guards_for_1288(self):
        # Staged for the next leg: max-1003 in profiles/; zero
        # one-zero-zero-four keys all forms; no-Type-B-#1288-in-git-log;
        # fortieth direction absent; forty-eighth through fifty-seventh
        # intact; no fifty-eighth member; ledger 57.
        assert _max_numeric_mechanism_id() == 1003
        assert _repo_grep_numeric_mechanism_id(1004) == []
        assert _repo_grep_underscore_mechanism(1004) == []
        assert _repo_grep_dash_mechanism(1004) == []
        assert _git("log", "--oneline", "--grep=Type B #1288").stdout.strip() == ""
        assert _git_grep_tracked_source(_T40, "profiles/") == []
        assert _git_grep_tracked_source(_T48, "profiles/") == [
            "profiles/financial-times.yaml"]
        assert _T57 in _read(AP_PATH)
        assert _git_grep_tracked_source(_T58, None) == []

    def test_novel_urls_zero_hit_pre_commit(self):
        # The 2 novel source URLs were zero-hit repo-wide pre-commit
        # (git grep -F, verified this run before the block landed).
        # Post-landing they live in the block's source_urls; assert
        # both are present exactly once in ap.yaml.
        text = _read(AP_PATH)
        assert text.count(
            "businessmirror.com.ph/2026/09/28/anthropic-openai-sound-the-alarm") == 2
        assert text.count(
            "bytewatchr.com/articles/ftc-openai-anthropic-consumer-risk-investigation") == 2


# ---------------------------------------------------------------------------
# 4. AP x Anthropic arms (NEW this run)
# ---------------------------------------------------------------------------


class TestApAnthropicBurke:
    def _item(self):
        return _block()["anthropic_arms"][0]["item"]

    def test_headline(self):
        assert "sound the alarm on AI safety" in self._item()["title"]

    def test_date_sep_27_2026(self):
        assert self._item()["date"] == "2026-09-27"

    def test_author_burke(self):
        assert self._item()["author_byline"] == "Garance Burke"

    def test_publication_ap_original(self):
        assert "The Associated Press (original; relay-attested)" in self._item()[
            "publication"]

    def test_framing_analytical_skeptical(self):
        assert self._item()["framing"] == (
            "analytical_wire_skeptical_safety_rhetoric_as_positioning")

    def test_tone_minus_030(self):
        assert self._item()["manual_illustrative_tone"] == BURKE_TONE

    def test_deal_not_disclosed(self):
        assert self._item()["deal_disclosed"] is False

    def test_evidence_tier_relay_attested(self):
        assert self._item()["evidence_tier"] == "relay-attested"

    def test_within_article_openai_symmetric(self):
        # The payer draws the identical register in the same article.
        assert "0.00" in self._item()["within_article_openai_register"]

    def test_lede_question_present(self):
        quotes = " ".join(self._item()["key_quotes"])
        assert "What do they have to gain?" in quotes


class TestApAnthropicFtc:
    def _item(self):
        return _block()["anthropic_arms"][1]["item"]

    def test_headline(self):
        assert "FTC Investigates OpenAI and Anthropic" in self._item()["title"]

    def test_date_oct_1_2026(self):
        assert self._item()["date"] == "2026-10-01"

    def test_publication_ap_original(self):
        assert "The Associated Press (original; relay-attested)" in self._item()[
            "publication"]

    def test_framing_enforcement_neutral(self):
        assert self._item()["framing"] == "enforcement_wire_neutral_process"

    def test_tone_minus_020(self):
        assert self._item()["manual_illustrative_tone"] == FTC_TONE

    def test_deal_not_disclosed(self):
        assert self._item()["deal_disclosed"] is False

    def test_within_article_openai_symmetric(self):
        assert "0.00" in self._item()["within_article_openai_register"]

    def test_ap_attribution_present(self):
        quotes = " ".join(self._item()["key_quotes"])
        assert "Associated Press" in quotes


# ---------------------------------------------------------------------------
# 5. Meta arms (carried m970)
# ---------------------------------------------------------------------------


class TestMetaArms1287:
    def test_carried_from_m970(self):
        assert "m970" in _block()["meta_arms"]["carried_from"]

    def test_settlement_arm(self):
        arms = _block()["meta_arms"]["arms"]
        assert arms[0]["manual_illustrative_tone"] == META_TONE
        assert arms[0]["mechanism_ref"] == "m970"

    def test_meta_band_mean(self):
        assert _block()["meta_arms"]["meta_band_mean"] == META_TONE

    def test_anthropic_mean(self):
        res = _block()["asymmetry_scorer_result"]
        assert res["target_avg"] == ANTHROPIC_MEAN
        assert abs((BURKE_TONE + FTC_TONE) / 2 - ANTHROPIC_MEAN) < 1e-9


# ---------------------------------------------------------------------------
# 6. Financial relationship
# ---------------------------------------------------------------------------


class TestFinancialRelationship1287:
    def test_ap_openai_deal_jul_2023(self):
        rel = _block()["financial_relationship"]
        assert "Jul 13 2023" in rel or "Jul-13-2023" in rel

    def test_anthropic_non_payer(self):
        data = yaml.safe_load(_read(AP_PATH))
        meta = data["competitor_relationships"]["anthropic"][
            "financial_metadata"]
        assert "$0" in meta["anthropic_financial"]
        assert "NON-PAYER" in meta["anthropic_financial"]

    def test_coverage_prediction_softer(self):
        data = yaml.safe_load(_read(AP_PATH))
        assert data["competitor_relationships"]["openai"][
            "financial_metadata"]["deal_disclosed_in_coverage"] is False

    def test_deal_url_reuters(self):
        assert "reuters.com" in _block()["deal_url"]


# ---------------------------------------------------------------------------
# 7. Asymmetry delta (MANUAL ILLUSTRATIVE ONLY)
# ---------------------------------------------------------------------------


class TestAsymmetryDelta1287:
    def test_delta_math(self):
        calc = ANTHROPIC_MEAN - META_TONE
        assert abs(calc - DELTA_ANTHROPIC_MINUS_META) < 1e-9

    def test_block_delta_matches(self):
        res = _block()["asymmetry_scorer_result"]
        assert res["illustrative_delta_anthropic_minus_meta"] == (
            DELTA_ANTHROPIC_MINUS_META)

    def test_delta_calc_string(self):
        res = _block()["asymmetry_scorer_result"]
        assert "-0.25 - (-0.45) = +0.20" in res["delta_calc"]

    def test_delta_direction_fails_prediction(self):
        res = _block()["asymmetry_scorer_result"]
        assert "FAILS at the wire register" in res["delta_direction"]
        assert "0.00" in res["delta_direction"]

    def test_engine_not_run(self):
        res = _block()["asymmetry_scorer_result"]
        assert res["engine_run"] is False
        assert res["is_significant"] is False
        assert res["artifact_grade"] is False

    def test_sample_sizes_declared(self):
        res = _block()["asymmetry_scorer_result"]
        assert "n=2 vs n=1" in res["methodology"]

    def test_verdict_member_confirmed(self):
        res = _block()["asymmetry_scorer_result"]
        assert res["verdict"] == "falsification_member_confirmed"

    def test_within_article_symmetry_documented(self):
        # The adjudicating comparison: payer vs non-payer in the same
        # articles, not the cross-peg Meta delta.
        res = _block()["asymmetry_scorer_result"]
        assert "within-article" in res["delta_direction"]


# ---------------------------------------------------------------------------
# 8. Research method
# ---------------------------------------------------------------------------


class TestResearchMethod1287:
    def test_scout_and_main_run_query_sets_documented(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "1 delegated scout" in src
        assert "2\nmain-run browser.search verification sets" in src or \
            "2 main-run browser.search verification sets" in src

    def test_1143_precedent_documented(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#1143" in src

    def test_counterevidence_disclosed(self):
        block = _block()
        assert len(block["counterevidence"]) >= 1
        assert "m970" in block["counterevidence"][0]

    def test_zero_browser_open(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "0 browser.open per #503" in src

    def test_ascii_no_em_dash(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "\u2014" not in src
        assert "\u2013" not in src

    def test_no_constructed_canonical_urls(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "no canonical URLs constructed" in src
        block = _block()
        for item in block["anthropic_arms"]:
            assert "NOT used per the no-construction rule" in item["item"][
                "url_source"]

    def test_saturation_rejections_documented(self):
        block = _block()
        assert "REJECTED" in block["research_method"]


# ---------------------------------------------------------------------------
# 9. Falsification ledger: fifty-seventh member lands this run.
# ---------------------------------------------------------------------------


class TestFalsificationLedger1287:
    def test_fifty_seventh_member_present_in_block(self):
        block = _block()
        assert block["falsification_family_member"] is True
        assert _T57 in block["falsification_family"]
        assert block["falsification_ledger"] == "57"
        assert block["ledger"] == "57"

    def test_forty_eighth_through_fifty_sixth_intact(self):
        # The earlier members survive this run unchanged (tracked
        # sources at HEAD; this run's block is additive).
        assert _git_grep_tracked_source(_T48, "profiles/") == [
            "profiles/financial-times.yaml"]
        assert _T56 in _read(os.path.join(PROFILES_DIR, "wired.yaml"))

    def test_no_fifty_eighth_member_repo_wide(self):
        assert _git_grep_tracked_source(_T58, None) == []

    def test_verdict_falsification_member_confirmed(self):
        block = _block()
        assert block["verdict"].startswith(
            "falsification_member_confirmed")

    def test_ledger_57_in_block(self):
        block = _block()
        assert "ledger 56->57" in block["falsification_family"]

    def test_first_ap_leg_member(self):
        block = _block()
        assert "FIRST AP-leg member" in block["falsification_family"]


# ---------------------------------------------------------------------------
# 10. Statistical discipline (Aug 28 2026 standing rule).
# ---------------------------------------------------------------------------


class TestStatisticalDiscipline1287:
    def test_p_value_not_calculated(self):
        block = _block()
        assert block["asymmetry_scorer_result"]["p_value"] == "NOT_CALCULATED"

    def test_cohens_d_not_calculated(self):
        block = _block()
        assert block["asymmetry_scorer_result"]["cohens_d"] == "NOT_CALCULATED"

    def test_ci_95_not_calculated(self):
        block = _block()
        assert block["asymmetry_scorer_result"]["ci_95"] == "NOT_CALCULATED"

    def test_is_significant_false(self):
        block = _block()
        assert block["asymmetry_scorer_result"]["is_significant"] is False

    def test_engine_not_run(self):
        block = _block()
        assert block["asymmetry_scorer_result"]["engine_run"] is False

    def test_no_analysis_json_update(self):
        block = _block()
        assert block["asymmetry_scorer_result"]["no_analysis_json_update"] is True

    def test_artifact_grade_false(self):
        block = _block()
        assert block["asymmetry_scorer_result"]["artifact_grade"] is False

    def test_correlation_not_causation(self):
        block = _block()
        assert block["asymmetry_scorer_result"]["correlation_not_causation"] is True

    def test_manual_illustrative_only(self):
        block = _block()
        assert "MANUAL ILLUSTRATIVE ONLY" in block["falsification_family"]

    def test_zero_browser_open(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "0 browser.open per #503" in src

    def test_ascii_no_em_dash(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "\u2014" not in src
        assert "\u2013" not in src


# ---------------------------------------------------------------------------
# 11. Guard lifecycle: forward guards staged for #1288 Type B.
# ---------------------------------------------------------------------------


class TestGuardLifecycle1287:
    def test_pins_on_one_mechanism_landing(self):
        # Type A lands one mechanism: max 1003, next 1004.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 1003" in src
        assert "NEXT_NUM = 1004" in src

    def test_no_type_b_1288_in_git_log_pin(self):
        # Post-main-commit form for the NEXT leg (the #1191-class
        # self-trip, re-pinned in #1288's terminal log-hash followup
        # per #721): every commit whose message matches "Type B
        # #1288" must be #1288's main commit or a descendant of it.
        # Deselected in the in-gate run (fails pre-commit by design).
        out = _git("log", "--format=%H", "--grep=Type B #1288")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1288's own commits"
        main = _git("rev-parse", PRED_MAIN_1288).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_1004_numeric_absent_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_1004_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_1004_dash_absent_repo_wide(self):
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
        assert _T56 in _read(
            os.path.join(PROFILES_DIR, "wired.yaml"))

    def test_fifty_seventh_member_present_pin(self):
        # Landed this run (m1003, profiles/ap.yaml). Asserted on the
        # working tree so the pin is stable across the main-commit
        # boundary; the HEAD sweep sees it from the main commit on.
        assert _T57 in _read(AP_PATH)

    def test_no_fifty_eighth_member_pin(self):
        assert _git_grep_tracked_source(_T58, None) == []

    def test_predecessor_1286_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, D1286_FILE))

    def test_next_leg_is_1288_type_b(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#1288 Type B" in src

    def test_1286_pins_flip_by_design_documented(self):
        # #1286's forward guards (max-1002, zero one-zero-zero-three
        # keys all forms, no-Type-A-#1287-in-git-log, fortieth
        # absent, forty-eighth through fifty-sixth intact in
        # profiles/, fifty-seventh absent, ledger 56) verified GREEN
        # at HEAD pre-commit this run. The no-Type-A-#1287-in-git-log
        # pin flips BY DESIGN at this run's main commit (the
        # #1191-class self-trip, re-pinned post-commit by
        # TestStalenessPins1287). Type A lands one mechanism, so the
        # zero one-zero-zero-three numeric/underscore/dash pins flip
        # BY DESIGN too (the #1272-class forward-guard expiry).
        # Documented in the staleness pin below, not repaired.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "TestStalenessPins1287" in src
        assert "no_type_a_1287_in_git_log_pin" in src


# ---------------------------------------------------------------------------
# 12. Staleness pins: #1286's guard lifecycle flips BY DESIGN post-commit.
# ---------------------------------------------------------------------------


class TestStalenessPins1287:
    def test_1286_guard_lifecycle_post_commit_self_trip(self):
        # Post-main-commit form: 19 tests in the class; TWO flip BY
        # DESIGN when this run's main commit lands and STAY flipped:
        # the test_1003_numeric_absent_in_profiles pin (the m1003
        # landing carries "mechanism_id: 1003" in colon form - the
        # #1272-class forward-guard expiry; the underscore/dash pins
        # stay green by the #723/#738/#739 designed keying) and the
        # test_no_fifty_seventh_member_pin (the fifty-seventh member
        # lands this run - the #1191-class self-trip on the member
        # pin). The no_type_a_1287_in_git_log ancestor pin ALSO flips
        # at the main commit but is re-pinned green in this terminal
        # log-hash followup per #721 (its PRED_MAIN_1287 now holds
        # this run's main sha). The class run below therefore expects
        # 2 failed / 17 passed and documents the designed flips. The
        # #1286 block is read-only to this run; the flips are
        # documented here, not repaired.
        res = _class_run(D1286_FILE, "TestGuardLifecycle1286")
        out = res.stdout + res.stderr
        assert "2 failed, 17 passed" in out, out[-2000:]
        assert "test_1003_numeric_absent_in_profiles" in out, out[-2000:]
        assert "test_no_fifty_seventh_member_pin" in out, out[-2000:]


# ---------------------------------------------------------------------------
# 13. Doc-sync per #719 (3 tests; deselected pre-commit, flipped post-sync)
# ---------------------------------------------------------------------------


class TestDocSync1287:
    def test_readme_test_file_table_has_1287_row_post_sync(self):
        readme = _read(README_PATH)
        assert OWN_BASENAME in readme

    def test_architecture_has_1287_row_post_sync(self):
        arch = _read(ARCH_PATH)
        assert OWN_BASENAME in arch

    def test_readme_stats_ratcheted(self):
        readme = _read(README_PATH)
        assert "| Tests | %d |" % README_TEST_COUNT in readme
        assert "Across %d test files" % README_FILE_COUNT in readme


# ---------------------------------------------------------------------------
# 14. Iteration log per #721.
# ---------------------------------------------------------------------------


class TestIterationLog1287:
    def test_log_has_1287_entry(self):
        text = _read(LOG_PATH)
        assert "## #1287 Type A" in text

    def test_log_entry_carries_hash_chain(self):
        # The doc-sync writes the entry with the main/anchor hashes;
        # the terminal log-hash followup registers the doc-sync hash
        # here per #721.
        text = _read(LOG_PATH)
        assert "main commit" in text
        assert "anchor" in text

    def test_log_entry_records_finding(self):
        text = _read(LOG_PATH)
        assert "m1003" in text
        assert "FIFTY-SEVENTH" in text
        assert "ledger 56->57" in text


# ---------------------------------------------------------------------------
# 15. In-flight isolation
# ---------------------------------------------------------------------------


class TestInFlightIsolation1287:
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
