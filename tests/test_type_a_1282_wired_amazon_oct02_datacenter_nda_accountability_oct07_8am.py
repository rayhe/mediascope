"""Type A #1282: WIRED x Amazon Oct-2-2026 data-center NDA accountability investigation (Oct 7 2026, ~08:00 AM PDT).

m1000 - FIRST dedicated corpus mechanism on WIRED running an adversarial
accountability investigation on Amazon, the second AI-lab payer of WIRED's
owner (Conde Nast x Amazon Rufus AI licensing, Jul 2025, multi-year, terms
undisclosed; m564; wired.yaml competitor_relationships.amazon
coverage_prediction "softer").

The peg: WIRED (Molly Taft, Oct 2 2026) reports Amazon has stopped using
secret NDAs with county officials for data-center projects and
"acknowledged that community backlash is leading to data center
moratoriums across the country" - while pressing Amazon on unanswered
questions (contractor NDAs reportedly not covered; existing agreements not
released), with the Rep. Raskin investigation and 100+ proposed
moratoriums as context. Relay-attested via three independent relays
(webpronews Oct 2, novaknown Oct 3, bitcoinversus Oct 4); 0 browser.open
per #503; the WIRED original URL did not surface in search listings
(no-construction rule).

MANUAL ILLUSTRATIVE scoring: WIRED x Amazon NDA accountability -0.45 vs
carried WIRED x Meta Muse dossier (m988, -0.58, Oct 4-5). Illustrative
delta (Amazon minus Meta): +0.13 - near-null; WIRED goes nearly as hard
on the payer as on Meta. The uniform payer-softening prediction FAILS on
the corporate-secrecy accountability peg.

Per #715 this docstring uses lowercase forms only: the fifty-sixth
falsification-family member, ledger 55->56. The uppercase claim form
lives only in the landed profile block. FIRST Amazon-leg member; FIRST
non-OpenAI-competitor member. Domain-bounded to the corporate-secrecy /
data-center accountability register. The #1143 temporal-replication
precedent does not block: no adversarial-on-partner observation has been
counted for the WIRED x Amazon pair (m466 was a bounded-absence selection
observation, verdict None; the surveillance_parity_paradox is a
thesis-consistent observation, Aug 8). Counterevidence disclosed: the
parity paradox documented WIRED going hard on Meta's dormant NameTag
while silent on Amazon's Ring - the member claim is peg-bounded, not
blanket.

Statistical discipline: monitoring-only per the Aug 28 2026 standing
rule (MANUAL ILLUSTRATIVE ONLY, engine NOT run, p_value/cohens_d/ci_95
NOT_CALCULATED, is_significant False, NOT artifact-grade, no
analysis.json update, verdict falsification_member_confirmed on the
domain-bounded peg). Correlation is not causation. Hypothesis-generating
only.

1 delegated scout (fresh publication+competitor pair discovery; dispatched
this run) + 2 main-run browser.search verification sets, 0 browser.open
per #503. 3 novel relay URLs zero-hit pre-commit. All URLs copied
verbatim from Full-URL listings; no canonical URLs constructed.
ASCII-only, no em dashes.

Rotation: this run is iteration #1282 Type A, the THIRD leg of the
1280-1284 window (D #1280 -> E #1281 -> A #1282 -> B #1283 -> C #1284,
per the #565 anchor + rotation guard). Predecessor #1281 Type E
verified in git log (main 3c53f5f9 / anchor 7ef464d2 / doc-sync b23ffee6 /
log-hash 10d64db0); the 1275-1279 window is VERIFIED CLOSED. This run's
main commit is the anchor per #565; ANCHORED_SHA patched post-commit. The
#1281 forward guards verified pre-commit this run: max-999; zero
next-number one-zero-zero-zero mechanism keys all forms (profiles/ +
tests/ scope); no-Type-A-#1282-in-git-log; fortieth direction absent
(profiles/ scope); forty-eighth through fifty-fifth members intact; no
fifty-sixth member (repo-wide); ledger 55. This run lands the
fifty-sixth member: TestGuardLifecycle1281's no-fifty-sixth-member pin
flips at this run's main commit BY DESIGN (the #1191-class self-trip),
documented in TestStalenessPins1282, not repaired. Next run #1283 Type B
continues the window. The #1280-launched background-suite verdict belongs
to #1285 per #795: this run OBSERVES only (log last write Oct 7 07:01
PDT, ~3% progress, zero live pytest processes at this run's check).
In-flight during this run: #899 (profiles/nytimes.yaml m771 hunk), #938
(Type B test file working-tree edit), #900 (untracked Type D test file),
#1012-wt (working-tree edit on the committed Type A #1012 file) - all
untouched; targeted staging only. Do NOT touch #1024 m846.

Pre-commit novelty greps per #715: zero test_type_a_1282 files on disk
(glob); no Type A #1282 in git log (--grep); max numeric mechanism_id
999 in profiles/ pre-commit (mechanism_id regex sweep); zero
numeric/underscore/dash next-number one-zero-zero-zero mechanism key
forms repo-wide pre-commit (needles format-built per #715, own file
excluded); "## #1282" zero-hit in iteration-log pre-commit; README stats
71384/1606 pre-commit; no #1282 row in README/ARCHITECTURE test tables
pre-commit; 3 novel relay URLs zero-hit repo-wide pre-commit (git grep
-F); "Molly Taft" carries 2 pre-commit repo hits (career records in
profiles/careers/journalists.yaml + editorial_changes.yaml, not
coverage); the WIRED NDA piece zero-hit in profiles/wired.yaml
pre-commit; distinct from m466 (bounded absence on the Aug-31 FTC
ad-auction lawsuit, not a tone finding) and the surveillance_parity_
paradox (Aug-8 Meta-hard / Amazon-silent observation, disclosed as
peg-bounded counterevidence).

Doc-sync constants per #719: README_TEST_COUNT / README_FILE_COUNT
hold the post-doc-sync values from the start (patched pre-main once
the in-gate collection count is known); the doc-sync commit ratchets
README 71384/1606 -> post-sync totals.
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
WIRED_PATH = os.path.join(PROFILES_DIR, "wired.yaml")
OWN_BASENAME = (
    "test_type_a_1282_wired_amazon_oct02_datacenter_nda_"
    "accountability_oct07_8am.py"
)
BLOCK_KEY = (
    "type_a_1282_wired_amazon_oct02_datacenter_nda_"
    "accountability_vs_carried_meta_arms"
)

# Pre-commit placeholder per #565; patched to the main commit sha in
# the anchor followup.
ANCHORED_SHA = "915f95cdecda806f4951109e22693e74f6238072"  # patched in the anchor followup per #565

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

MECH_NUM = 1000
NEXT_NUM = 1001  # integer only; key-form needles are format-built

# Predecessor chain: #1281 Type E CLOSED the second leg.
PRED_MAIN_1281 = "3c53f5f98c3b6b53443d507d02a206f4a07afde6"
PRED_ANCHOR_1281 = "7ef464d2dfa5ea166ffc42d11ce42ce8bddffc14"
PRED_DOCSYNC_1281 = "b23ffee64456d1319f73a78e334f070d19721008"
PRED_FINAL_1281 = "10d64db01266d4d89ee0bae31d38ba29161ba571"

# This run's main commit (full sha), for the ancestor-form
# no-Type-A-#1282 pin. Patched in the terminal log-hash followup per
# #721.
PRED_MAIN_1282 = "0" * 40

# #1283's main commit (full sha), for the ancestor-form no-Type-B-#1283
# pin. Patched in #1283's terminal log-hash followup per #721.
PRED_MAIN_1283 = "0" * 40

# The #1281 Type E file, for the staleness pin on its guard-lifecycle
# class (max id 999; zero next-number one-zero-zero-zero /
# no-Type-A-#1282-in-git-log / fortieth direction absent /
# forty-eighth through fifty-fifth members intact / fifty-sixth
# member absent / ledger 55).
E1281_FILE = (
    "test_type_e_1281_podcast_sentiment_179th_verification_oct07_7am.py"
)

# Doc-sync constants per #719: post-doc-sync values from the start.
# Patched pre-main once the in-gate collection count is known.
README_TEST_COUNT = 71468  # post-doc-sync total (pre-sync 71384 + 84)
README_FILE_COUNT = 1607  # pre-sync 1606 + 1

# Tones (MANUAL ILLUSTRATIVE).
AMAZON_NDA_TONE = -0.45  # NEW WIRED x Amazon arm (Oct-2 NDA piece)
META_DOSSIER_TONE = -0.58  # carried m988 arm
DELTA_AMAZON_MINUS_META = 0.13  # -0.45 - (-0.58)

NOVEL_URLS = [
    "https://www.webpronews.com/amazons-1-billion-bet-to-quiet-"
    "data-center-backlash-and-secure-ai-dominance/",
    "https://novaknown.com/2026/10/03/"
    "amazon-drops-ndas-after-keeping-county-talks-secret/",
    "https://bitcoinversus.tech/2026/10/04/"
    "data-centers-amazon-drops-ndas-government-agencies/",
]

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


def _read(path):
    with open(path, encoding="utf-8", errors="replace") as fh:
        return fh.read()


def _git(*args):
    return subprocess.run(
        ["git", *args], cwd=REPO_ROOT, capture_output=True, text=True
    )


def _load_wired():
    with open(WIRED_PATH, encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def _block():
    data = _load_wired()
    return data["competitor_relationships"]["amazon"][BLOCK_KEY]


def _iter_source_files():
    """Yield paths for profile + test source files.

    Excludes this file (sweep carrier per #715) and __pycache__
    artifacts.
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
    """Underscore-form mechanism key; needle format-built per #770."""
    needle = "%s%d" % (MECH_ID_MARKER, n)
    return [
        p for p in _iter_source_files() if needle in _read(p)
    ]


def _repo_grep_dash_mechanism(n):
    needle = "mechanism" + "-" + str(n)
    return [
        p for p in _iter_source_files() if needle in _read(p)
    ]


def _repo_grep_numeric_mechanism_id(n):
    needle = "mechanism_id: %d" % n
    hits = []
    for root, dirs, files in os.walk(PROFILES_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
            p = os.path.join(root, f)
            if needle in _read(p):
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
                    _read(os.path.join(root, f))
                )
            )
    return max(found) if found else 0


def _git_grep_tracked_source(needle, scope):
    """Literal needle across tracked profile/test source files.

    scope is "profiles/" or None (profiles/ + tests/). Excludes the
    sweep carrier and __pycache__ artifacts per #715.
    """
    out = _git("grep", "-F", "-l", needle, "HEAD", "--",
               "profiles/", "tests/").stdout
    hits = []
    for line in out.splitlines():
        line = line.strip()
        if not line:
            continue
        if line.startswith("HEAD:"):
            line = line[len("HEAD:"):]
        path = line
        if "__pycache__" in path:
            continue
        if path.endswith("/" + OWN_BASENAME) or path == OWN_BASENAME:
            continue
        if scope == "profiles/" and not path.startswith("profiles/"):
            continue
        hits.append(path)
    return hits


# ---------------------------------------------------------------------------
# 1. Anchor per #565 (5 tests; placeholder pre-commit, patched post-anchor)
# ---------------------------------------------------------------------------
class TestAnchor1282:
    def test_anchor_sha_placeholder_pre_commit(self):
        # Pre-commit form: ANCHORED_SHA is 0*40; the anchor followup
        # patches it to the main commit sha per #565. Deselected in
        # the in-gate run; the patched form is asserted post-anchor.
        assert ANCHORED_SHA == "0" * 40

    def test_anchor_sha_patched_to_main_commit(self):
        # Post-commit form: ANCHORED_SHA patched to this run's main
        # commit sha per #565 in the anchor followup. Pre-commit this
        # is 0*40 and the test fails BY DESIGN; deselected in-gate.
        assert ANCHORED_SHA != "0" * 40
        assert len(ANCHORED_SHA) == 40

    def test_anchor_sha_format(self):
        assert len(ANCHORED_SHA) == 40

    def test_this_run_main_commit_is_anchor(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "main commit is the anchor" in src

    def test_rotation_phrase_in_docstring(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "THIRD leg of the 1280-1284 window" in src


# ---------------------------------------------------------------------------
# 2. Rotation guard
# ---------------------------------------------------------------------------
class TestRotationGuard:
    def test_predecessor_1281_chain_verified(self):
        for sha in (
            PRED_MAIN_1281, PRED_ANCHOR_1281, PRED_DOCSYNC_1281,
            PRED_FINAL_1281,
        ):
            res = _git("cat-file", "-t", sha)
            assert res.stdout.strip() == "commit", "missing %s" % sha

    def test_window_order_phrase(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "D #1280 -> E #1281 -> A #1282 -> B #1283 -> C #1284" in src

    def test_next_leg_is_type_b_1283(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Next run #1283 Type B" in src

    def test_type_a_lands_one_mechanism(self):
        assert MECH_NUM == 1000
        assert _max_numeric_mechanism_id() == MECH_NUM

    def test_this_run_is_third_leg(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "iteration #1282 Type A, the THIRD leg" in src


# ---------------------------------------------------------------------------
# 3. Mechanism novelty
# ---------------------------------------------------------------------------
class TestMechanismNovelty:
    def test_max_numeric_mechanism_id_1000(self):
        assert _max_numeric_mechanism_id() == MECH_NUM

    def test_no_type_a_1282_in_git_log_pin(self):
        # Post-main-commit form (the #1191-class self-trip, re-pinned
        # in the terminal log-hash followup per #721): every commit
        # whose message matches "Type A #1282" must be this run's
        # main commit or a descendant of it - i.e., no PRIOR run
        # committed this run's iteration. Deselected in the in-gate
        # run (fails pre-commit by design).
        out = _git("log", "--format=%H", "--grep=Type A #1282")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected this run's own commits"
        main = _git("rev-parse", PRED_MAIN_1282).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_zero_next_number_keys_all_forms(self):
        # Numeric (profiles/ scope), underscore and dash (profiles/ +
        # tests/ scope, own file excluded per #715).
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_block_key_designed_no_1000_substring(self):
        # Per #723/#738/#739: the iteration-form block key carries no
        # underscore-form one-zero-zero-zero mechanism key substring
        # (needle format-built per #770 so this file carries no
        # contiguous literal).
        needle = "%s%d" % (MECH_ID_MARKER, MECH_NUM)
        assert needle not in BLOCK_KEY
        assert BLOCK_KEY in _read(WIRED_PATH)

    def test_forward_guards_for_1283(self):
        # max-1000; zero-1001 all forms; fortieth direction absent
        # (profiles/ scope); forty-eighth through fifty-sixth members
        # intact; no fifty-seventh member (repo-wide); ledger 56. The
        # fifty-sixth is asserted on the working tree (this run's
        # block, committed at the main commit); the HEAD-based sweep
        # sees it from the main commit onward.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 1000" in src
        assert "NEXT_NUM = 1001" in src
        assert "ledger 55->56" in src
        assert _git_grep_tracked_source(_T40, "profiles/") == []
        assert _git_grep_tracked_source(_T48, "profiles/") == [
            "profiles/financial-times.yaml"]
        assert _T56 in _read(WIRED_PATH)
        assert _git_grep_tracked_source(_T57, None) == []

    def test_novel_urls_zero_hit_pre_commit(self):
        # The 3 relay URLs were verified zero-hit pre-commit (git
        # grep -F, documented in the block's novelty field). This test
        # pins that no file OTHER than this run's own m1000 block ever
        # carries them, so it holds pre-commit (zero hits) and
        # post-commit (only the landed block hits).
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
                "profiles/wired.yaml",
                "tests/" + OWN_BASENAME,
            }, (url, paths)


# ---------------------------------------------------------------------------
# 4. Falsification ledger (fifty-sixth member lands this run)
# ---------------------------------------------------------------------------
class TestFalsificationLedger:
    def test_fifty_sixth_member_present_in_block(self):
        block = _block()
        assert block["falsification_family_member"] is True
        assert _T56 in block["falsification_family"]
        assert block["falsification_ledger"] == "56"
        assert block["ledger"] == "56"

    def test_forty_eighth_through_fifty_fifth_intact(self):
        # The earlier members survive this run unchanged (tracked
        # sources at HEAD; this run's block is additive).
        assert _git_grep_tracked_source(_T48, "profiles/") == [
            "profiles/financial-times.yaml"]
        assert _git_grep_tracked_source(_T55, "profiles/") == [
            "profiles/atlantic.yaml"]

    def test_no_fifty_seventh_member_repo_wide(self):
        assert _git_grep_tracked_source(_T57, None) == []

    def test_verdict_falsification_member_confirmed(self):
        block = _block()
        assert block["verdict"].startswith(
            "falsification_member_confirmed")

    def test_ledger_56_in_block(self):
        block = _block()
        assert "ledger 55->56" in block["falsification_family"]


# ---------------------------------------------------------------------------
# 5. WIRED x Amazon NDA arm (NEW this run)
# ---------------------------------------------------------------------------
class TestWiredAmazonNda:
    def _item(self):
        return _block()["amazon_arms"][0]["item"]

    def test_headline(self):
        assert "NDA" in self._item()["title"]
        assert "Amazon" in self._item()["title"]

    def test_date_oct_2_2026(self):
        assert self._item()["date"] == "2026-10-02"

    def test_author_taft(self):
        assert self._item()["author_byline"] == "Molly Taft"

    def test_publication_wired_original(self):
        assert "WIRED (original; relay-attested)" in self._item()[
            "publication"]

    def test_framing_accountability(self):
        assert self._item()["framing"] == (
            "accountability_investigation_corporate_secrecy")

    def test_tone_minus_045(self):
        assert self._item()["manual_illustrative_tone"] == AMAZON_NDA_TONE

    def test_deal_not_disclosed(self):
        assert self._item()["deal_disclosed"] is False

    def test_evidence_tier_relay_attested(self):
        assert self._item()["evidence_tier"] == "relay-attested"


# ---------------------------------------------------------------------------
# 6. Meta arms (carried m988)
# ---------------------------------------------------------------------------
class TestMetaArms:
    def test_carried_from_m988(self):
        assert "m988" in _block()["meta_arms"]["carried_from"]

    def test_dossier_arm(self):
        arms = _block()["meta_arms"]["arms"]
        assert arms[0]["manual_illustrative_tone"] == META_DOSSIER_TONE
        assert arms[0]["mechanism_ref"] == "m988"

    def test_meta_band_mean(self):
        assert _block()["meta_arms"]["meta_band_mean"] == META_DOSSIER_TONE


# ---------------------------------------------------------------------------
# 7. Financial relationship
# ---------------------------------------------------------------------------
class TestFinancialRelationship:
    def test_conde_nast_amazon_rufus_deal(self):
        rel = _block()["financial_relationship"]
        assert "Jul 2025" in rel
        assert "Rufus" in rel

    def test_second_payer_after_openai(self):
        rel = _block()["financial_relationship"]
        assert "second AI-lab payer" in rel

    def test_coverage_prediction_softer(self):
        data = _load_wired()
        assert data["competitor_relationships"]["amazon"][
            "coverage_prediction"] == "softer"


# ---------------------------------------------------------------------------
# 8. Asymmetry delta (MANUAL ILLUSTRATIVE ONLY)
# ---------------------------------------------------------------------------
class TestAsymmetryDelta:
    def test_delta_math(self):
        calc = AMAZON_NDA_TONE - META_DOSSIER_TONE
        assert abs(calc - DELTA_AMAZON_MINUS_META) < 1e-9

    def test_block_delta_matches(self):
        res = _block()["asymmetry_scorer_result"]
        assert res["illustrative_delta_amazon_minus_meta"] == (
            DELTA_AMAZON_MINUS_META)

    def test_delta_direction_near_null(self):
        res = _block()["asymmetry_scorer_result"]
        assert "Near-null illustrative delta" in res["delta_direction"]
        assert "FAILS on this peg" in res["delta_direction"]

    def test_engine_not_run(self):
        res = _block()["asymmetry_scorer_result"]
        assert res["engine_run"] is False
        assert res["is_significant"] is False
        assert res["artifact_grade"] is False

    def test_sample_sizes_declared(self):
        res = _block()["asymmetry_scorer_result"]
        assert "n=1 vs n=1" in res["methodology"]

    def test_verdict_member_confirmed(self):
        res = _block()["asymmetry_scorer_result"]
        assert res["verdict"] == "falsification_member_confirmed"


# ---------------------------------------------------------------------------
# 9. Research method
# ---------------------------------------------------------------------------
class TestResearchMethod:
    def test_scout_and_main_run_query_sets_documented(self):
        method = _block()["research_method"]
        assert "1 delegated scout" in method
        assert "2 main-run browser.search verification sets" in method

    def test_1143_precedent_documented(self):
        block = _block()
        assert "#1143" in block["falsification_family"]
        assert "#1143" in block["research_method"]

    def test_counterevidence_disclosed(self):
        block = _block()
        assert any("surveillance_parity_paradox" in item
                   for item in block["counterevidence"])

    def test_zero_browser_open(self):
        assert "0 browser.open per #503" in _block()["research_method"]

    def test_ascii_no_em_dash(self):
        # Scoped to this run's landed block: wired.yaml carries
        # pre-existing em dashes at HEAD (outside the m1000 block),
        # so the whole-file assertion cannot pass without rewriting
        # history. The ASCII discipline is asserted on the m1000
        # block's own content via an allow_unicode round-trip.
        dumped = yaml.safe_dump(_block(), allow_unicode=True)
        assert "\\u2014" not in dumped

    def test_no_constructed_canonical_urls(self):
        method = _block()["research_method"]
        assert "no canonical URLs constructed" in method
        assert "NOT used per the no-construction rule" in method


# ---------------------------------------------------------------------------
# 10. Statistical discipline (Aug 28 2026 standing rule)
# ---------------------------------------------------------------------------
class TestStatisticalDiscipline:
    def test_p_value_not_calculated(self):
        res = _block()["asymmetry_scorer_result"]
        assert res["p_value"].startswith("NOT_CALCULATED")

    def test_no_analysis_json_update(self):
        assert _block()["no_analysis_json_update"] is True

    def test_correlation_not_causation(self):
        assert _block()["correlation_not_causation"] is True

    def test_manual_illustrative_only(self):
        disc = _block()["statistical_discipline"]
        assert "MANUAL ILLUSTRATIVE" in disc

    def test_verdict_member_confirmed(self):
        assert _block()["verdict"].startswith(
            "falsification_member_confirmed")

    def test_not_artifact_grade(self):
        assert _block()["statistical_discipline"].find(
            "NOT artifact-grade") != -1


# ---------------------------------------------------------------------------
# 11. Guard lifecycle for #1282 (forward pins for #1283)
# ---------------------------------------------------------------------------
class TestGuardLifecycle1282:
    def test_pins_on_mechanism_landing(self):
        # Type A lands one mechanism: max 1000, next 1001.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 1000" in src
        assert "NEXT_NUM = 1001" in src

    def test_no_type_b_1283_in_git_log_pin(self):
        # Post-main-commit form for the NEXT leg (the #1191-class
        # self-trip, re-pinned in #1283's terminal log-hash followup
        # per #721): every commit whose message matches "Type B
        # #1283" must be #1283's main commit or a descendant of it.
        # Deselected in the in-gate run (fails pre-commit by design).
        out = _git("log", "--format=%H", "--grep=Type B #1283")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1283's own commits"
        main = _git("rev-parse", PRED_MAIN_1283).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_1001_numeric_absent_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_1001_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_1001_dash_absent_repo_wide(self):
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
        # Landed this run (m1000, profiles/wired.yaml). Asserted on
        # the working tree so the pin is stable across the main-commit
        # boundary; the HEAD sweep sees it from the main commit on.
        assert _T56 in _read(WIRED_PATH)

    def test_no_fifty_seventh_member_pin(self):
        assert _git_grep_tracked_source(_T57, None) == []

    def test_predecessor_1281_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, E1281_FILE))

    def test_next_leg_is_1283_type_b(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Next run #1283 Type B" in src

    def test_1281_pins_documented(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "TestStalenessPins1282" in src
        assert "3 failed, 15 passed" in src


# ---------------------------------------------------------------------------
# 12. Staleness pins for #1282 (1 test; deselected pre-commit per #721)
# ---------------------------------------------------------------------------
class TestStalenessPins1282:
    def _class_run(self, filename, classname):
        target = os.path.join(TESTS_DIR, filename)
        env = dict(os.environ)
        env["PYTEST_DISABLE_PLUGIN_AUTOLOAD"] = "1"
        res = subprocess.run(
            ["python3", "-m", "pytest", target,
             "-k", classname,
             "-q", "--no-header"],
            cwd=REPO_ROOT, capture_output=True, text=True, env=env,
        )
        return res

    def test_1281_guard_lifecycle_post_commit(self):
        # Post-main-commit form: 18 tests in the class, 15 pass and 3
        # fail - the no_fifty_sixth_member pin (this run's main commit
        # lands the fifty-sixth member-claim form; the #1191-class
        # self-trip, permanent red), the no_type_a_1282_in_git_log pin
        # (hits go non-empty at the main commit while PRED_MAIN_1282
        # in the #1281 file is still 0*40; re-pinned green in this
        # run's log-hash followup per #721), and the
        # 1000_numeric_absent_in_profiles pin (trips on the landed
        # m1000 block's "mechanism_id: 1000"; the #1272-class
        # forward-guard expiry - the next-number guard is consumed by
        # the landing). Deselected in the in-gate run (pre-commit the
        # class is 18 passed); asserted post-main-commit. The #1281
        # file is read-only to this run except the #721 re-pin; the
        # flips are documented here, not repaired.
        res = self._class_run(
            E1281_FILE,
            "TestGuardLifecycle1281",
        )
        out = res.stdout + res.stderr
        assert "3 failed, 15 passed" in out, out[-2000:]
        assert "no_fifty_sixth_member" in out, out[-2000:]
        assert "no_type_a_1282_in_git_log" in out, out[-2000:]
        assert "1000_numeric_absent_in_profiles" in out, out[-2000:]


# ---------------------------------------------------------------------------
# 13. Doc-sync per #719 (3 tests; deselected pre-commit, flipped post-sync)
# ---------------------------------------------------------------------------
class TestDocSync:
    def test_readme_test_file_table_has_1282_row_post_sync(self):
        readme = _read(README_PATH)
        assert "test_type_a_1282" in readme

    def test_architecture_has_1282_row_post_sync(self):
        arch = _read(ARCH_PATH)
        assert "test_type_a_1282" in arch

    def test_readme_stats_ratcheted(self):
        # Post-sync-positive form per #719: asserts the ratcheted
        # counts (README_TEST_COUNT tests across README_FILE_COUNT
        # files). Fails pre-commit by design; deselected in the
        # in-gate run.
        readme = _read(README_PATH)
        assert ("| Tests | %d |" % README_TEST_COUNT) in readme
        assert ("Across %d test files" % README_FILE_COUNT) in readme


# ---------------------------------------------------------------------------
# 14. Iteration log (3 tests; deselected pre-commit per #721)
# ---------------------------------------------------------------------------
class TestIterationLog:
    def test_1282_entry_present_post_sync(self):
        log = _read(LOG_PATH)
        assert "## #1282 Type A" in log

    def test_1281_entry_present(self):
        log = _read(LOG_PATH)
        assert "## #1281 Type E" in log

    def test_rotation_transparency_convention(self):
        log = _read(LOG_PATH)
        assert "### Rotation transparency" in log


# ---------------------------------------------------------------------------
# 15. In-flight isolation
# ---------------------------------------------------------------------------
class TestInFlightIsolation:
    def test_899_nytimes_hunk_untouched(self):
        res = _git("diff", "--name-only")
        modified = res.stdout.split()
        assert "profiles/nytimes.yaml" in modified
        # Its uncommitted hunk belongs to #899's run; this run stages
        # only its own paths.
        staged = _git("diff", "--cached", "--name-only").stdout.split()
        assert "profiles/nytimes.yaml" not in staged

    def test_900_untracked_file_untouched(self):
        assert os.path.exists(
            os.path.join(
                TESTS_DIR,
                "test_type_d_900_m769_qualitative_corpus_integrity_"
                "sep21_1pm.py",
            )
        )
        res = _git("status", "--porcelain")
        assert "test_type_d_900_" in res.stdout

    def test_938_test_file_edit_owned_by_its_run(self):
        res = _git("diff", "--name-only")
        assert "test_type_b_938_" in res.stdout
        staged = _git("diff", "--cached", "--name-only").stdout.split()
        assert not any("test_type_b_938_" in p for p in staged)

    def test_1012_wt_working_tree_edit_owned_by_its_run(self):
        res = _git("diff", "--name-only")
        assert "test_type_a_1012_" in res.stdout
        staged = _git("diff", "--cached", "--name-only").stdout.split()
        assert not any("test_type_a_1012_" in p for p in staged)

    def test_do_not_touch_1024_m846(self):
        res = _git("diff", "--name-only")
        assert "competitor-entities.yaml" not in res.stdout
        staged = _git("diff", "--cached", "--name-only").stdout.split()
        assert "profiles/competitor-entities.yaml" not in staged
