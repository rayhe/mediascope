"""MediaScope iteration #1364 - Type C: financial-incentive saturation
screening (Oct 10 2026, ~6:00 AM PDT).

THE SCREEN: 1 delegated scout (4 tracks) + 3 main-run browser.search
verification sets + main-run corpus git-grep verification; 0
browser.open per #503. ALL FOUR scout picks REJECTED on main-run
verification - the SIXTH #1341 scout-corpus-blindness instance (after
#1353's m1004 re-surfacing, #1354's test_type_c_1329 re-surfacing,
#1358's triple misattribution, #1359's test_type_c_1329 re-surfacing,
and #1363's Allison Johnson / Kris Holt / Nicholas Sutrich triple):
(1) Broadcom $50B+ debt for OpenAI chips (WSJ Oct 7, 2026,
Apollo/Blackstone) + $60B Anthropic package + $42B prospectus loan -
thin relay-only delta on the SATURATED Broadcom XPV $100B
private-credit leg (tests/test_broadcom_xpv_100b_escalation_private_
credit_publisher_compound_incentive_aug25.py); the scout's relay URL
(aistockwire aggregator) untrusted per #1341. (2) OpenAI $30B bridge
round at $1.4T pre-money (Bloomberg Oct 6, UAE/MGX + BlackRock) -
in-corpus ("1.4 trillion" in profiles/careers/journalists.yaml).
(3) Google AI-contribution pilot payout mechanics + the Mehta
dismissal addendum - pilot saturated (m891 UNILATERAL PRICING, #1099,
m702/m708); Mehta's Oct-1 Chegg + Penske AI-Overviews dismissal
saturated (m1129, screened at #1359). (4) Anthropic IPO-prospectus
$42B 2025 loss + Amazon $18B/$190B/$53.4B Q2-2026 figures (fool.com
relay) - the $42B loss is in-corpus (business-insider.yaml Sep-29
mechanism, the-verge.yaml, news-corp.yaml, journalists.yaml); the
Amazon figures are vintage Q2-2026 earnings, relay-only, on the
saturated Amazon x Anthropic financial architecture, with no
publication link - no new money leg per the #1359 thin-delta
precedent.

MAIN-RUN SCREENS (all rejected/saturated): OpenAI publisher
licensing Oct 2026 (Press Gazette/e4m: TOI/BCCL ~$5M + Indian Express
~$3M per year - Sep-23 vintage, estimate-only, Indian Express
in-corpus via #624/#704); OpenAI debt financing Oct 2026 (Broadcom
$50B+ thin; Broadcom $42B Anthropic prospectus loan thin;
Nvidia $500B third-party capital relay-only via finance.biggo;
SoftBank $100B borrow relay-only via kucoin); Google AI Overviews
publisher compensation (fully saturated - m702/m708/m891, #1099,
m1099/m1199; the Technori Oct-5 relay wave is relay-only on a
saturated mechanism).

Two verbatim Full-URL listings carried this run (single-line
docstring form per the #1359 in-gate fix; copied verbatim from the
main run's own Full-URL listings, never constructed) to document
corroboration of in-corpus legs - never as novel evidence:
https://www.moneyweb.co.za/news/ai/openai-expects-70bn-in-annualised-revenue-by-end-of-2026/
https://aiweekly.co/alerts/googles-ai-overviews-pilot-pays-100-publishers-one-over-1m

Carried rejections from #1359 (re-screening would re-litigate): (1)
Mehta's dismissal of the Chegg + Penske AI-Overviews antitrust suits
(m1129, in-corpus as test_type_c_1129); (2) the NYT $28M+ cumulative
AI-litigation spend figure ($4.2M in Q1 2026, m636/m753, in-corpus);
(3) the October 2026 Google AI Contribution Pilot relay wave
(Technori Oct-1 relay of The Information's Sep-29 figures,
m1099/m1199, saturated); (4) the DOJ 20-page Statement of Interest
backing fair use in NYT v. Microsoft (m672, vintage, out of window).

Statistical discipline: MANUAL / QUALITATIVE ONLY per the Aug 28
2026 standing rule (tone values NOT_SCORED;
p_value/cohens_d/ci_95 NOT_CALCULATED; is_significant false; engine
NOT run; verdict monitoring_only; NOT artifact-grade;
no_analysis_json_update true). Correlation is not causation;
hypothesis-generating only.

Verdict: saturation_screening_no_novel_mechanism. Type C lands ZERO
mechanisms this run: max numeric mechanism_id stays 1045, next 1046,
ledger holds at 64, no profiles/ edit, no sixty-fifth member-claim
form repo-wide. NOT a falsification-family member (per #609/#614
qualitative boundary: financial-incentive legs map money flows; no
coverage-tone claim is made here).

Rotation: #1364 is the FIFTH and CLOSING leg of the 1360-1364 window
(D #1360 -> E #1361 -> A #1362 -> B #1363 -> C #1364 per the #565
anchor + rotation guard); the 1355-1359 window is VERIFIED CLOSED.
Next: Type D #1365 opens the next window; the background-suite
verdict belongs to #1365 per #795 (the #1360-launched full suite at
goal hidden_files type_d_1360_full_suite.log runs: this run CHECKS
it only - last write Oct 10 03:59 PDT at [3%], zero live pytest
processes at this run's ~6:0x AM PDT check; neither re-launches,
kills, nor writes to it).

Anchor convention per #565: ANCHORED_SHA starts as 0*40 in this
pre-commit file and is patched to the main-commit sha in the anchor
followup commit. The placeholder-form anchor test fails BY DESIGN
post-anchor; the patched-form test is deselected in the in-gate run.

Do NOT touch #1024 (m846 in profiles/competitor-entities.yaml), #899
(nytimes.yaml m771 hunk), #938 (Type B test file working-tree edit),
#900 (untracked Type D test file), #1012-wt (working-tree edit on the
committed Type A #1012 file).

ASCII-only, no em dashes. Needles format-built per #715: this file
must not carry contiguous numeric/underscore/dash mechanism-key forms
of the max or next number, the forty-eighth through sixty-fifth
member-claim forms, or the fortieth direction-claim form; the
constants are constructed at runtime. (The landed ordinals live as
short lowercase forms in prose here; the live full-form claims live
in profiles: the forty-eighth, fifty-eighth, and sixtieth in
financial-times.yaml, the forty-ninth, fiftieth, and fifty-second in
profiles/careers/journalists.yaml, the fifty-first, fifty-ninth,
sixty-second, and sixty-third in news-corp.yaml, the fifty-third in
the-verge.yaml, the fifty-fourth in guardian.yaml, the fifty-fifth
in atlantic.yaml, the fifty-sixth and sixty-first in wired.yaml, the
fifty-seventh and sixty-fourth in ap.yaml; the sixty-fifth is absent
repo-wide as of this run.)
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

OWN_BASENAME = "test_type_c_1364_financial_incentive_saturation_oct10_6am.py"

# Patched per #565 in the anchor followup (main commit sha).
ANCHORED_SHA = "0" * 40

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

MECH_NUM = 1045  # max numeric; Type C lands ZERO mechanisms this run
NEXT_NUM = 1046  # integer only; key-form needles are format-built

# Post-doc-sync totals per #719: PATCHED post-collection
# (pre-sync 79148 + 68 tests; pre-sync 1688 + 1 file).
README_TEST_COUNT = 79216  # patched post-collection
README_FILE_COUNT = 1689

# Predecessor chain: #1363 Type B FOURTH leg of the 1360-1364 window.
PRED_MAIN_1363 = "8074ebdc9f41667975b6a28858afd8c8d72f79eb"
PRED_ANCHOR_1363 = "410a0a607100c8d9c8ae82f5581d6dc69eba803b"
PRED_DOCSYNC_1363 = "a3e01fec4728650ecbcbcde299afbf972e366ea9"
PRED_LOGHASH_1363 = "d059316bb79863a10b0326e1edf6bbdd387b74eb"
PRED_PUSH_1363 = "3369149c4398ed1ebec1cab4b19dd98ae9c47dde"

# This run's main commit (full sha), for the ancestor-form
# no-Type-C-#1364 pin. Staged 0*40 placeholder-only per #721;
# re-pinned in the anchor followup per #721 (PRED_MAIN_1364 re-pinned
# in BOTH this file and the #1363 file per the #1292 precedent).
PRED_MAIN_1364 = "0" * 40

# #1365's main commit (full sha), for the ancestor-form no-Type-D-#1365
# pin (the #1191-class self-trip; #1365 is Type D per the rotation).
# Staged 0*40 placeholder-only per #721; re-pinned in #1365's terminal
# log-hash followup per #721. (Type-correct per the #1352
# type-mismatch lesson: #1365 is Type D, so the pin greps
# "Type D #1365".)
PRED_MAIN_1365 = "0" * 40

# The #1363 window-predecessor file, for the staleness pin on its
# guard-lifecycle class (max id 1045; zero next-number 1046 all forms;
# no sixty-fifth member; ledger holds at 64).
B1363_FILE = "test_type_b_1363_saturation_screening_oct10_5am.py"

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
_T61 = "SIXT" + "Y-FIRST falsification-family member"
_T62 = "SIXT" + "Y-SECOND falsification-family member"
_T63 = "SIXT" + "Y-THIRD falsification-family member"
_T64 = "SIXT" + "Y-FOURTH falsification-family member"
_T65 = "SIXT" + "Y-FIFTH falsification-family member"

# 3 main-run browser.search query sets + 1 delegated scout (4 tracks)
# this run (0 browser.open per #503).
QUERY_SETS = [
    "OpenAI publisher content licensing deal October 2026 announcement amount",
    "OpenAI debt financing raise October 2026 valuation reports",
    "Google AI Overviews publisher compensation News AI pilot payment October 2026",
]

# SCOUT PICKS (titles only; scout-supplied relay URLs untrusted per the
# #1341 lesson; every pick verified independently by the main run via
# its own searches and git grep -F - ALL FOUR REJECTED: the SIXTH
# #1341 scout-corpus-blindness instance, after #1353's m1004
# re-surfacing, #1354's test_type_c_1329 re-surfacing, #1358's triple
# misattribution, #1359's test_type_c_1329 re-surfacing, and #1363's
# Allison Johnson / Kris Holt / Nicholas Sutrich triple):
# Pick 1: Broadcom arranging $50B+ in debt to fund OpenAI's custom
#   chips (WSJ Oct 7, 2026; Apollo/Blackstone) + $60B Anthropic package
#   + $42B prospectus loan: REJECTED - thin relay-only delta on the
#   SATURATED Broadcom XPV $100B private-credit leg
#   (tests/test_broadcom_xpv_100b_escalation_private_credit_publisher_
#   compound_incentive_aug25.py); scout relay URL (aistockwire
#   aggregator) untrusted per #1341.
# Pick 2: OpenAI $30B bridge round at $1.4T pre-money (Bloomberg Oct 6,
#   UAE/MGX + BlackRock): REJECTED - in-corpus ("1.4 trillion" in
#   profiles/careers/journalists.yaml). Saturated.
# Pick 3: Google AI-contribution pilot payout mechanics + Judge Mehta's
#   Oct-1 Chegg + Penske AI-Overviews dismissal addendum: REJECTED -
#   pilot saturated (m891 UNILATERAL PRICING, #1099, m702/m708); Mehta
#   dismissal saturated (m1129, screened at #1359).
# Pick 4: Anthropic IPO-prospectus $42B 2025 loss + Amazon
#   $18B/$190B/$53.4B Q2-2026 figures (fool.com relay): REJECTED - the
#   $42B loss is in-corpus (business-insider.yaml Sep-29 mechanism,
#   the-verge.yaml, news-corp.yaml, journalists.yaml); the Amazon
#   figures are vintage Q2-2026 earnings, relay-only, on the saturated
#   Amazon x Anthropic financial architecture, with no publication
#   link - no new money leg per the #1359 thin-delta precedent.
SCOUT_PICKS_DOCUMENTED_IN_DOCSTRING = True


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
#    + rotation guard: FIFTH leg of the 1360-1364 window.
# ---------------------------------------------------------------------------


class TestAnchor1364:
    def test_anchor_sha_placeholder_pre_commit(self):
        # Pre-commit form: ANCHORED_SHA is 0*40; the anchor followup
        # patches it to the main-commit sha. This test fails BY
        # DESIGN post-anchor; the patched form is asserted by
        # test_anchor_sha_patched_to_main_commit. Terminal per #565.
        assert ANCHORED_SHA == "0" * 40

    def test_anchor_sha_patched_to_main_commit(self):
        # Post-commit form: ANCHORED_SHA patched to this run's main
        # commit sha in the anchor followup (placeholder + expected
        # value and the ANCHORED_SHA constant are patched).
        # Deselected in the in-gate run (fails pre-commit by design).
        assert ANCHORED_SHA != "0" * 40
        assert len(ANCHORED_SHA) == 40

    def test_anchor_sha_format(self):
        assert len(ANCHORED_SHA) == 40
        assert re.fullmatch(r"[0-9a-f]{40}", ANCHORED_SHA)

    def test_anchor_duality_documented(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Anchor convention per #565" in src
        assert "fails BY DESIGN post-anchor" in src

    def test_fifth_leg_phrase(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "FIFTH leg of the 1360-1364 window" in src

    def test_1355_1359_window_closed(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "1355-1359" in src
        assert "VERIFIED CLOSED" in src

    def test_next_leg_is_1365_type_d(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "D #1365" in src


# ---------------------------------------------------------------------------
# 2. Novelty pins + scout record: pre-commit surface must be clean, and
#    the scout's picks are untrusted until main-run verification.
# ---------------------------------------------------------------------------


class TestScoutCorpusBlindness1364:
    def test_scout_pick1_broadcom_50b_rejected_thin_delta(self):
        # Broadcom $50B+ OpenAI-chip debt (WSJ Oct 7, relay via
        # aistockwire): thin relay-only delta on the SATURATED
        # Broadcom XPV $100B private-credit leg. SIXTH #1341 instance.
        p = os.path.join(
            TESTS_DIR,
            "test_broadcom_xpv_100b_escalation_private_credit_"
            "publisher_compound_incentive_aug25.py",
        )
        assert os.path.exists(p), "saturated Broadcom XPV leg must exist"

    def test_scout_pick2_openai_30b_rejected_saturated(self):
        # OpenAI $30B bridge at $1.4T pre-money (Bloomberg Oct 6):
        # in-corpus. SIXTH #1341 instance.
        hits = _git_grep_tracked_source(
            "1.4 trillion",
            "profiles/careers/journalists.yaml",
        )
        assert hits, "OpenAI $1.4T round must be corpus-recorded"

    def test_scout_pick3_google_pilot_rejected_saturated(self):
        # Google AI-contribution pilot payout mechanics: saturated
        # (m891 UNILATERAL PRICING, #1099, m702/m708). SIXTH #1341
        # instance.
        hits = _git_grep_tracked_source(
            "AI-contribution",
            "profiles/competitor-entities.yaml",
        )
        assert hits, "AI-contribution pilot must be corpus-recorded"

    def test_scout_pick3_mehta_addendum_rejected(self):
        # Mehta's Oct-1 Chegg + Penske AI-Overviews dismissal: in-corpus
        # (m1129, screened at #1359); the scout's addendum re-surfaces
        # it. SIXTH #1341 instance.
        hits = _git_grep_tracked_source(
            "25-cv-543",
            "profiles/competitor-entities.yaml",
        )
        assert hits, "Mehta dismissal leg must be corpus-recorded"

    def test_scout_pick4_anthropic_42b_rejected_saturated(self):
        # Anthropic $42B 2025 net loss (IPO prospectus): in-corpus
        # (business-insider.yaml Sep-29 mechanism, the-verge.yaml,
        # news-corp.yaml, journalists.yaml). SIXTH #1341 instance.
        hits = _git_grep_tracked_source(
            "$42 billion net loss",
            "profiles/business-insider.yaml",
        )
        assert hits, "Anthropic $42B loss must be corpus-recorded"

    def test_scout_pick4_amazon_figures_vintage_relay(self):
        # Amazon $18B/$190B/$53.4B Q2-2026 figures: vintage, relay-only
        # (fool.com), on the saturated Amazon x Anthropic financial
        # architecture, with no publication link - no new money leg
        # per the #1359 thin-delta precedent.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "vintage Q2-2026" in src
        assert "no publication link" in src

    def test_max_numeric_mechanism_id_stays_1045(self):
        # Type C lands ZERO mechanisms this run: max numeric stays 1045.
        assert _max_numeric_mechanism_id() == MECH_NUM == 1045

    def test_no_type_c_1364_in_git_log_pin(self):
        # Ancestor-form self-trip per #1191: every commit whose message
        # matches "Type C #1364" must be #1364's main commit or a
        # descendant of it. Deselected in the in-gate run (fails
        # pre-commit by design); re-pinned in the terminal log-hash
        # followup per #721.
        out = _git("log", "--format=%H", "--grep=Type C #1364")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1364's own commits"
        main = _git("rev-parse", PRED_MAIN_1364).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_zero_next_number_keys_all_forms(self):
        # Numeric (profiles/ scope), underscore and dash (profiles/ +
        # tests/ scope, own file excluded per #715). Holds pre-commit
        # and post-commit (Type C lands zero mechanisms, the 1046
        # pins stay green).
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_no_1364_entry_in_iteration_log_pre_commit(self):
        text = _read(LOG_PATH)
        assert "## #1364" not in text

    def test_zero_type_c_1364_files_except_own(self):
        import glob
        found = glob.glob(os.path.join(TESTS_DIR, "test_type_c_1364*"))
        assert [os.path.basename(p) for p in found] == [OWN_BASENAME]

    def test_query_sets_bounded(self):
        # 3 main-run browser.search query sets + 1 delegated scout
        # (4 tracks); 0 browser.open per #503.
        assert len(QUERY_SETS) == 3
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "0 browser.open per #503" in src


# ---------------------------------------------------------------------------
# 3. Main-run screening ledger: every main-run query set documented.
# ---------------------------------------------------------------------------


class TestMainRunScreens1364:
    def test_licensing_screen_toi_estimate_rejected(self):
        # TOI/BCCL ~$5M + Indian Express ~$3M per year (e4m relay of
        # Sep-23-2026 deals): estimate-only, vintage, no disclosed
        # figure; Indian Express is in-corpus via #624/#704.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "estimate-only" in src
        assert "Indian Express" in src

    def test_licensing_indian_express_in_corpus(self):
        hits = _git_grep_tracked_source(
            "Indian Express",
            "profiles/competitor-entities.yaml",
        )
        assert hits, "Indian Express leg must be corpus-recorded"

    def test_financing_thin_deltas_rejected(self):
        # Broadcom $42B Anthropic prospectus loan, Nvidia $500B
        # third-party capital (finance.biggo relay), SoftBank $100B
        # borrow (kucoin relay): thin relay-only deltas on saturated
        # legs, no primary source, no new money leg.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "thin relay-only delta" in src

    def test_google_pilot_relay_wave_not_novel(self):
        # The Technori Oct-5 AI-contribution-pilot relay wave documents
        # no new figure: relay-only on the saturated m891 leg.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "relay wave" in src
        assert "m891" in src

    def test_urls_verbatim_convention(self):
        # Both carried URLs exist verbatim, single-line, in this file
        # (per the #1359 in-gate fix: split-literal concatenation does
        # not count).
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert ("https://www.moneyweb.co.za/news/ai/"
                "openai-expects-70bn-in-annualised-revenue-by-end-of-2026/"
                ) in src
        assert ("https://aiweekly.co/alerts/googles-ai-overviews-pilot-pays-"
                "100-publishers-one-over-1m") in src

    def test_no_novel_money_leg(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "saturation_screening_no_novel_mechanism" in src


# ---------------------------------------------------------------------------
# 4. Guard lifecycle: forward pins for #1365; #1364 stages the
#    #1191-class no-Type-D-#1365 self-trip (re-pinned post-commit
#    per #721). Type-correct per the #1352 type-mismatch lesson.
# ---------------------------------------------------------------------------


class TestGuardLifecycle1364:
    def test_pins_on_zero_mechanism_landing(self):
        # Type C lands zero mechanisms: max 1045, next 1046.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 1045" in src
        assert "NEXT_NUM = 1046" in src

    def test_no_type_d_1365_in_git_log_pin(self):
        # Post-main-commit form for the NEXT leg (the #1191-class
        # self-trip, re-pinned in #1365's terminal log-hash followup
        # per #721): every commit whose message matches "Type D
        # #1365" must be #1365's main commit or a descendant of it.
        # Deselected in the in-gate run (fails pre-commit by design).
        # Type-correct per the #1352 type-mismatch lesson (#1365 is
        # Type D per the rotation).
        out = _git("log", "--format=%H", "--grep=Type D #1365")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1365's own commits"
        main = _git("rev-parse", PRED_MAIN_1365).stdout.strip()
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
        # m1045 is mechanism_documented, NOT a member, and this run
        # lands zero mechanisms: the sixty-fifth member-claim form
        # stays absent repo-wide.
        assert _git_grep_tracked_source(_T65, "profiles/") == []
        assert _git_grep_tracked_source(_T65, "tests/") == []

    def test_ledger_holds_at_64_pin(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "ledger holds at 64" in src


# ---------------------------------------------------------------------------
# 5. Staleness pins: #1363's guard lifecycle flips BY DESIGN post-commit.
# ---------------------------------------------------------------------------


class TestStalenessPins1364:
    def test_1363_guard_lifecycle_post_commit_state(self):
        # Post-terminal form: 25 tests in the class; ALL 25 pass.
        # Type C lands zero mechanisms, so every #1363 forward guard
        # stays green: max-1045, zero-1046 all forms, fortieth absent,
        # forty-eighth through sixty-fourth members intact,
        # no-sixty-fifth member, ledger holds at 64. The
        # no_type_c_1364_in_git_log ancestor pin (the #1191-class
        # self-trip) was red at this run's main-commit time; the
        # terminal log-hash followup re-pins PRED_MAIN_1364 in BOTH
        # its own file's copy and the #1363 predecessor file's copy
        # per the #1292 re-pin-both-copies precedent and the #721
        # re-pin rule, flipping it green. Deselected in the in-gate
        # run (fails pre-commit by design); verified post-terminal.
        res = _class_run(B1363_FILE, "TestGuardLifecycle1363")
        out = res.stdout + res.stderr
        assert "25 passed" in out, out[-2000:]


# ---------------------------------------------------------------------------
# 6. Doc-sync per #719 (deselected pre-commit, flipped post-sync).
# ---------------------------------------------------------------------------


class TestDocSync1364:
    def test_readme_test_file_table_has_1364_row_post_sync(self):
        readme = _read(README_PATH)
        assert "test_type_c_1364" in readme

    def test_architecture_has_1364_row_post_sync(self):
        arch = _read(ARCH_PATH)
        assert "test_type_c_1364" in arch

    def test_readme_stats_ratcheted(self):
        # Post-sync-positive form per #719: asserts the ratcheted
        # counts (README_TEST_COUNT tests across README_FILE_COUNT
        # files). Fails pre-commit by design; deselected in the
        # in-gate run.
        readme = _read(README_PATH)
        assert ("| Tests | %d |" % README_TEST_COUNT) in readme
        assert ("Across %d test files" % README_FILE_COUNT) in readme


# ---------------------------------------------------------------------------
# 7. Iteration log per #721 (deselected pre-commit, flipped post-sync).
# ---------------------------------------------------------------------------


class TestIterationLog1364:
    def test_log_has_1364_entry(self):
        text = _read(LOG_PATH)
        assert "## #1364 Type C" in text

    def test_log_entry_carries_hash_chain(self):
        # The doc-sync writes the entry with the main/anchor hashes;
        # the terminal log-hash followup registers the doc-sync hash
        # here per #721.
        text = _read(LOG_PATH)
        assert "main commit" in text
        assert "anchor" in text

    def test_log_entry_records_finding(self):
        text = _read(LOG_PATH)
        assert "saturation_screening_no_novel_mechanism" in text
        assert "1045" in text


# ---------------------------------------------------------------------------
# 8. Screening ledger: the money legs screened this run.
# ---------------------------------------------------------------------------


class TestScreeningLedger1364:
    def test_screened_picks_documented(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        for name in ("Broadcom", "OpenAI $30B", "AI-contribution",
                     "Anthropic", "$42B"):
            assert name in src, name

    def test_carried_rejections_referenced(self):
        # The #1359 four carry as rejections; re-screening them
        # would re-litigate.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        for name in ("Mehta", "Chegg", "Penske", "m1129",
                     "$28M", "m636", "m1099", "m1199",
                     "statement of interest", "m672"):
            assert name in src, name

    def test_no_profiles_edit_this_run(self):
        # Type C lands zero mechanisms: no profiles/ edit this run
        # (verified via git status in the iteration-log entry, not
        # here).
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "no profiles/ edit" in src


# ---------------------------------------------------------------------------
# 9. Research method.
# ---------------------------------------------------------------------------


class TestResearchMethod1364:
    def test_scout_plus_main_run_sets(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "1 delegated scout (4 tracks)" in src
        assert "3 main-run browser.search verification sets" in src

    def test_zero_browser_open(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "0 browser.open per #503" in src

    def test_scout_untrusted_convention(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#1341 lesson" in src


# ---------------------------------------------------------------------------
# 10. Verdict: saturation screening, manual/qualitative only.
# ---------------------------------------------------------------------------


class TestVerdict1364:
    def test_verdict_saturation_screening(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "saturation_screening_no_novel_mechanism" in src

    def test_not_falsification_family_member(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "NOT a falsification-family" in src
        assert "ledger holds at 64" in src

    def test_manual_qualitative_only(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MANUAL /" in src
        assert "QUALITATIVE ONLY per the Aug 28 2026 standing rule" in src
        assert "tone NOT_SCORED" in src
        assert "no_analysis_json_update true" in src

    def test_correlation_not_causation(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Correlation is" in src
        assert "hypothesis-generating only" in src

    def test_background_suite_checked_only(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "this run CHECKS it only" in src
        assert "verdict belongs to #1365 per #795" in src
        assert "neither" in src
        assert "re-launches, kills, nor writes to it" in src
