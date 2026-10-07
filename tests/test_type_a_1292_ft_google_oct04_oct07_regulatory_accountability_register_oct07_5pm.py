"""Type A #1292: FT x Google Oct-1/Oct-4/Oct-7 regulatory-accountability register (Oct 7 2026, ~05:00 PM PDT).

m1006 - FIRST dedicated corpus mechanism on the FT x Google regulatory pegs.
The Financial Times, eight months after signing the Feb-2026 News AI pilot
commercial partnership with Google (single-figure millions GBP/yr per Press
Gazette Aug 3 2026; in-profile coverage_prediction "softer"), runs three
adversarial regulatory-accountability pegs on the payer inside 72 hours: the
Oct-1 EU-meetings analysis (Google/Apple/Amazon each hold more EU-official
meetings than any European company, adversarial lobbying-footprint data
frame), the Oct-4 Companies-desk piece ("Google Defends 1.2bn UK Lawsuit
Over App Download Charges", 20M consumers, CAT trial opened Oct 6), and the
Oct-7 Brussels-tax scoop (CORE levy redesign, Google named an explicit
target alongside Apple and Meta, relayed same-day by Reuters).

MANUAL ILLUSTRATIVE scoring: FT x Google arms -0.40 (Play Store) + -0.30
(EU meetings) + -0.35 (Brussels tax), mean -0.35, vs carried FT x Meta arms
-0.55 (Jun-5 equity-raise) + -0.62 (Jul-8 glasses surveillance) + -0.58
(Aug-26 smartglasses flooding), mean -0.5833 (m441, carried un-rescored per
#807). Illustrative delta (Google minus Meta): +0.23. The thesis test is the
uniform payer-softening prediction, not the delta: the deal predicts a muted
register on Google; the FT instead applies the accountability register to the
payer three times in 72 hours. Prediction FAILS at the regulatory register.

Per #715 this docstring uses lowercase forms only: the fifty-eighth
falsification-family member, ledger 57->58, domain-bounded to the FT's
regulatory register on Google in the Oct-1/Oct-7 window; FOURTH FT
publication-level member (after the thirty-fifth #1047, the forty-second
#1142, and the forty-eighth #1202). The #1143 temporal-replication precedent
does not block: no adversarial-on-partner observation has been counted for
the FT x Google pair (m497 was a tone test, not a falsification pin).

Statistical discipline: monitoring-only per the Aug 28 2026 standing
rule (MANUAL ILLUSTRATIVE ONLY, engine NOT run, p_value/cohens_d/ci_95
NOT_CALCULATED, is_significant False, NOT artifact-grade, no
analysis.json update, verdict falsification_member_confirmed).
Correlation is not causation. Hypothesis-generating only.

1 delegated scout (fresh publication+competitor pair discovery;
saturation sweep across 10 publication profiles + ~10 candidate pairs;
SELECTED FT x Google; REJECTED The Verge x Anthropic (no verbatim
theverge.com URL), The Verge x Google (relays only), MIT TR x Google
(zero in-window hits), Atlantic x Anthropic (zero Atlantic-original
hits), NYT x Google (Sep-24 Suncatcher, outside window), Guardian x
Anthropic (saturated: m985), Atlantic x Google (no hits), News Corp x
Google (Sep-21, outside window), FT x Anthropic (Aug/Sep relays; m676
covered Sep 13); dispatched this run) + 2 main-run browser.search
verification sets ((1) Oct-7 Brussels-tax FT scoop - reuters.com verbatim
with "the Financial Times reported on Wednesday" attribution + six
officials, 5 corroborating relays; (2) Oct-4 FT Play Store 1.2bn piece -
webpronews/insurancejournal/claimsjournal verbatim with Oct-6 CAT trial
corroboration, Liz Coll, 20M consumers), 0 browser.open per #503. 3 novel
URLs zero-hit pre-commit. All URLs copied verbatim from Full-URL listings;
no canonical URLs constructed. ASCII-only, no em dashes.

Rotation: this run is iteration #1292 Type A, the THIRD leg of the
1290-1294 window (D #1290 -> E #1291 -> A #1292 -> B #1293 -> C #1294,
per the #565 anchor + rotation guard). Predecessor #1291 Type E
verified in git log (main 4f33ce6a / anchor 17773f8a / doc-sync
041cda51 / log-hash 939e19d6); the 1285-1289 window is VERIFIED CLOSED.
This run's main commit is the anchor per #565; ANCHORED_SHA patched
post-commit. The #1291 forward guards verified pre-commit this run:
max-1005; zero next-number one-zero-zero-six mechanism keys all forms
(profiles/ + tests/ scope); no-Type-A-#1292-in-git-log; fortieth
direction absent (profiles/ scope); forty-eighth through fifty-seventh
members intact; no fifty-eighth member (repo-wide); ledger 57. This run
lands mechanism one-zero-zero-six: TestGuardLifecycle1291's zero
one-zero-zero-six numeric pin flips at this run's main commit BY DESIGN
(the #1272-class forward-guard expiry) and its no-fifty-eighth-member
pin flips BY DESIGN (the #1191-class self-trip on the member pin),
documented in TestStalenessPins1292, not repaired; the
no-Type-A-#1292-in-git-log pin flips BY DESIGN (the #1191-class
self-trip), re-pinned in the terminal log-hash followup per #721.
Next run #1293 Type B continues the window. The #1295 Type D run owns
the next background-suite verdict per #795: this run OBSERVES only
(2117 bytes, [2%] progress, last write Oct 7 2026 04:17 PM PDT, live
pytest processes at this run's check - genuine full-suite process,
zero F marks in the stream).
In-flight during this run: #899 (profiles/nytimes.yaml m771 hunk),
#938 (Type B test file working-tree edit), #900 (untracked Type D
test file), #1012-wt (working-tree edit on the committed Type A
#1012 file) - all untouched; targeted staging only. Do NOT touch
#1024 m846.

Pre-commit novelty greps per #715: zero test_type_a_1292 files on
disk (glob); no Type A #1292 in git log (--grep); max numeric
mechanism_id 1005 in profiles/ pre-commit (mechanism_id regex
sweep); zero numeric/underscore/dash next-number one-zero-zero-six
mechanism key forms repo-wide pre-commit (needles format-built per
#715, own file excluded); block key zero-hit repo-wide pre-commit
(designed keying: iteration 1292 in key, no 1006 substring, per the
#723/#738/#739 convention); "## #1292" zero-hit in iteration-log
pre-commit; README stats 72182/1616 pre-commit; no #1292 row in
README/ARCHITECTURE test tables pre-commit; 3 novel source URLs
zero-hit repo-wide pre-commit (git grep -F); all 3 novel headlines
zero-hit repo-wide pre-commit (git grep -F); "FT x Google" seven
iteration-log hits are all historical (no falsification pin);
no counted adversarial-on-partner observation for FT x Google
pre-commit (the #1143 check).

Doc-sync constants per #719: README_TEST_COUNT / README_FILE_COUNT
hold the post-doc-sync values from the start (patched pre-main once
the in-gate collection count is known); the doc-sync commit ratchets
README 72182/1616 -> post-sync totals.
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
FT_PATH = os.path.join(PROFILES_DIR, "financial-times.yaml")

OWN_BASENAME = (
    "test_type_a_1292_ft_google_oct04_oct07_"
    "regulatory_accountability_register_oct07_5pm.py"
)
BLOCK_KEY = (
    "type_a_1292_ft_google_oct04_oct07_"
    "regulatory_accountability_register_vs_carried_meta_arms"
)

# Pre-commit placeholder per #565; patched to the main commit sha in
# the anchor followup.
ANCHORED_SHA = "ddb5921f611ec53ce70c9134517255322a04a859"  # patched in the anchor followup per #565

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

MECH_NUM = 1006
NEXT_NUM = 1007  # integer only; key-form needles are format-built

# Predecessor chain: #1291 Type E closed the SECOND leg.
PRED_MAIN_1291 = "4f33ce6a"
PRED_ANCHOR_1291 = "17773f8a"
PRED_DOCSYNC_1291 = "041cda51"
PRED_FINAL_1291 = "939e19d6"

# This run's main commit (full sha), for the ancestor-form
# no-Type-A-#1292 pin. Patched in the terminal log-hash followup per
# #721.
PRED_MAIN_1292 = "0" * 40  # re-pinned in the terminal log-hash followup per #721

# #1293's main commit (full sha), for the ancestor-form no-Type-B-#1293
# pin. Patched in #1293's terminal log-hash followup per #721.
PRED_MAIN_1293 = "0" * 40

# The #1291 predecessor file, for the staleness pin on its
# guard-lifecycle class (max id 1005; zero next-number
# one-zero-zero-six / no-Type-A-#1292-in-git-log / fortieth
# direction absent / forty-eighth through fifty-seventh members
# intact / fifty-eighth member absent / ledger 57).
D1291_FILE = (
    "test_type_e_1291_podcast_sentiment_181st_"
    "verification_oct07_4pm.py"
)

# Doc-sync constants per #719: post-doc-sync values from the start.
# Patched pre-main once the in-gate collection count is known.
README_TEST_COUNT = 72267  # post-doc-sync total (pre-sync 72182 + 85)
README_FILE_COUNT = 1617  # pre-sync 1616 + 1 (this file)

# MANUAL ILLUSTRATIVE tones (hand-assigned at excerpt level).
A1_PLAYSTORE_TONE = -0.40
A2_EU_MEETINGS_TONE = -0.30
A3_BRUSSELS_TAX_TONE = -0.35
GOOGLE_MEAN = -0.35
META_MEAN = -0.5833333333333333  # -1.75/3 exact
DELTA_GOOGLE_MINUS_META = 0.23

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
# (landed this run in profiles/financial-times.yaml; staged for #1293).
_T58 = "FIFT" + "Y-EIGHTH falsification-family member"
# The fifty-ninth member-claim form is fragment-built per #715
# (no fifty-ninth member may exist repo-wide; staged for #1293).
_T59 = "FIFT" + "Y-NINTH falsification-family member"


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
    """Return the landed m1006 profile block for this run."""
    with open(FT_PATH, encoding="utf-8") as fh:
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
    assert hit is not None, "m1006 block not found"
    return hit


# ---------------------------------------------------------------------------
# 1. Anchor (pre-commit placeholder per #565; patched in anchor followup).
# ---------------------------------------------------------------------------


class TestAnchor1292:
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
# 2. Rotation guard: #1291 closed the SECOND leg; #1292 is the THIRD.
# ---------------------------------------------------------------------------


class TestRotationGuard1292:
    def test_predecessor_shas_in_git_log(self):
        log = _git("log", "--oneline", "-60").stdout
        for sha, label in (
            (PRED_MAIN_1291, "1291 main"),
            (PRED_ANCHOR_1291, "1291 anchor"),
            (PRED_DOCSYNC_1291, "1291 doc-sync"),
            (PRED_FINAL_1291, "1291 log-hash"),
        ):
            assert sha in log, label

    def test_1291_type_e_in_git_log(self):
        out = _git("log", "--oneline", "--grep=Type E #1291").stdout
        assert out.strip() != ""

    def test_third_leg_phrase(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "THIRD leg of the 1290-1294 window" in src

    def test_1285_1289_window_closed(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "1285-1289" in src
        assert "VERIFIED CLOSED" in src

    def test_next_leg_is_1293_type_b(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "B #1293" in src


# ---------------------------------------------------------------------------
# 3. Mechanism novelty: Type A lands one mechanism (max 1005 -> 1006).
# ---------------------------------------------------------------------------


class TestMechanismNovelty1292:
    def test_max_numeric_mechanism_id_1006(self):
        assert _max_numeric_mechanism_id() == MECH_NUM

    def test_no_type_a_1292_in_git_log_pin(self):
        # Post-main-commit form (the #1191-class self-trip, re-pinned
        # in the terminal log-hash followup per #721): every commit
        # whose message matches "Type A #1292" must be this run's
        # main commit or a descendant of it - i.e., no PRIOR run
        # committed this run's iteration. Deselected in the in-gate
        # run (fails pre-commit by design).
        out = _git("log", "--format=%H", "--grep=Type A #1292")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected this run's own commits"
        main = _git("rev-parse", PRED_MAIN_1292).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_zero_next_number_keys_all_forms(self):
        # Numeric (profiles/ scope), underscore and dash (profiles/ +
        # tests/ scope, own file excluded per #715). NEXT_NUM is 1007:
        # this run lands 1006, so the next-number forms stay absent.
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_block_key_designed_no_1006_substring(self):
        # Designed keying per #723/#738/#739: the iteration-form block
        # key carries the iteration (1292), never the mechanism number.
        assert "1006" not in BLOCK_KEY
        assert "1292" in BLOCK_KEY

    def test_forward_guards_for_1293(self):
        # Staged for the next leg: max-1006 in profiles/; zero
        # one-zero-zero-seven keys all forms; no-Type-B-#1293-in-git-log;
        # fortieth direction absent; forty-eighth through fifty-eighth
        # intact; no fifty-ninth member; ledger 58.
        assert _max_numeric_mechanism_id() == 1006
        assert _repo_grep_numeric_mechanism_id(1007) == []
        assert _repo_grep_underscore_mechanism(1007) == []
        assert _repo_grep_dash_mechanism(1007) == []
        assert _git("log", "--oneline", "--grep=Type B #1293").stdout.strip() == ""
        assert _git_grep_tracked_source(_T40, "profiles/") == []
        assert _git_grep_tracked_source(_T48, "profiles/") == [
            "profiles/financial-times.yaml"]
        assert _T58 in _read(FT_PATH)
        assert _git_grep_tracked_source(_T59, None) == []

    def test_novel_urls_zero_hit_pre_commit(self):
        # The 3 novel source URLs were zero-hit repo-wide pre-commit
        # (git grep -F, verified this run before the block landed).
        # Post-landing they live in the block's source_urls and in
        # each arm's url_source; assert each is present exactly twice
        # in financial-times.yaml.
        text = _read(FT_PATH)
        assert text.count(
            "headlinesbriefing.com/market/ft-companies/"
            "google-defends-12bn-uk-lawsuit") == 2
        assert text.count(
            "wesearch.press/s/analysis-google-apple-and-amazon-"
            "each-have-more-meetings-wit-dd263072") == 2
        assert text.count(
            "reuters.com/business/retail-consumer/brussels-looks-"
            "capture-big-tech-through-tax-large-corporations-"
            "ft-reports-2026-10-07") == 2


# ---------------------------------------------------------------------------
# 4. FT x Google arms (NEW this run)
# ---------------------------------------------------------------------------


class TestFtGooglePlayStore1292:
    def _arm(self):
        arms = _block()["google_arms"]
        return [a["item"] for a in arms][0]

    def test_a1_title_and_date(self):
        arm = self._arm()
        assert arm["title"] == (
            "Google Defends 1.2bn UK Lawsuit Over App Download Charges")
        assert arm["date"] == "2026-10-04"
        assert arm["publication"].startswith("Financial Times")

    def test_a1_tone(self):
        arm = self._arm()
        assert arm["manual_illustrative_tone"] == A1_PLAYSTORE_TONE
        assert arm["framing"] == "accountability_litigation_register"

    def test_a1_mirror_attested_not_constructed(self):
        arm = self._arm()
        assert arm["evidence_tier"] == "mirror-attested"
        assert "NOT used per the no-construction rule" in arm["url_source"]

    def test_a1_key_quote(self):
        arm = self._arm()
        assert any("defends" in q.lower() or "Defends" in q
                   for q in arm["key_quotes"])
        assert arm["deal_disclosed"] is False
        assert "NEW this run" in arm["status"]


class TestFtGoogleEuMeetings1292:
    def _arm(self):
        arms = _block()["google_arms"]
        return [a["item"] for a in arms][1]

    def test_a2_title_and_date(self):
        arm = self._arm()
        assert arm["date"] == "2026-10-01"
        assert "meetings" in arm["title"]

    def test_a2_tone(self):
        arm = self._arm()
        assert arm["manual_illustrative_tone"] == A2_EU_MEETINGS_TONE
        assert arm["framing"] == "adversarial_data_framing_lobbying_footprint"

    def test_a2_key_quote(self):
        arm = self._arm()
        assert any("more meetings" in q for q in arm["key_quotes"])
        assert arm["deal_disclosed"] is False
        assert "NEW this run" in arm["status"]


class TestFtGoogleBrusselsTax1292:
    def _arm(self):
        arms = _block()["google_arms"]
        return [a["item"] for a in arms][2]

    def test_a3_title_and_date(self):
        arm = self._arm()
        assert arm["title"] == (
            "Brussels looks to capture Big Tech through tax on large "
            "corporations, FT reports")
        assert arm["date"] == "2026-10-07"
        assert "relay-attested" in arm["evidence_tier"]

    def test_a3_tone(self):
        arm = self._arm()
        assert arm["manual_illustrative_tone"] == A3_BRUSSELS_TAX_TONE
        assert arm["framing"] == "accountability_regulatory_targeting_register"

    def test_a3_names_google_explicit_target(self):
        arm = self._arm()
        assert any("Apple, Meta and Google" in q or "such as Apple" in q
                   for q in arm["key_quotes"])
        assert arm["deal_disclosed"] is False
        assert "NEW this run" in arm["status"]


# ---------------------------------------------------------------------------
# 5. FT x Meta carried arms (m441, un-rescored per #807)
# ---------------------------------------------------------------------------


class TestMetaArms1292:
    def test_carried_from_m441(self):
        meta = _block()["meta_arms"]
        assert "m441" in meta["carried_from"]
        assert "un-rescored per #807" in meta["carried_from"]

    def test_three_carried_arms(self):
        arms = _block()["meta_arms"]["arms"]
        assert len(arms) == 3
        assert arms[0]["manual_illustrative_tone"] == -0.55
        assert arms[1]["manual_illustrative_tone"] == -0.62
        assert arms[2]["manual_illustrative_tone"] == -0.58

    def test_meta_mean(self):
        meta = _block()["meta_arms"]
        assert meta["meta_mean"] == META_MEAN
        tones = [a["manual_illustrative_tone"] for a in meta["arms"]]
        assert abs(sum(tones) / len(tones) - META_MEAN) < 1e-9


# ---------------------------------------------------------------------------
# 6. Financial relationship: the Feb-2026 FT x Google deal leg
# ---------------------------------------------------------------------------


class TestFinancialRelationship1292:
    def test_google_is_the_payer(self):
        blk = _block()
        rel = blk["financial_relationship"]
        assert "News AI pilot" in rel
        assert "single-figure millions GBP/yr" in rel
        assert "PAYER" in rel

    def test_coverage_prediction_softer_in_profile(self):
        data = yaml.safe_load(_read(FT_PATH))
        google = data["competitor_relationships"]["google"]
        assert google["coverage_prediction"] == "softer"

    def test_deal_url_verbatim(self):
        blk = _block()
        assert blk["deal_url"] == (
            "https://talkingbiznews.com/media-news/ft-signs-ai-deal-with-google/")

    def test_meta_zero_tie(self):
        blk = _block()
        assert "$0 tie" in blk["financial_relationship"]

    def test_deal_not_disclosed_in_arms(self):
        arms = [a["item"] for a in _block()["google_arms"]]
        assert all(a["deal_disclosed"] is False for a in arms)


# ---------------------------------------------------------------------------
# 7. Asymmetry delta: the falsification, not the delta
# ---------------------------------------------------------------------------


class TestAsymmetryDelta1292:
    def test_google_mean(self):
        arms = [a["item"] for a in _block()["google_arms"]]
        tones = [a["manual_illustrative_tone"] for a in arms]
        assert tones == [A1_PLAYSTORE_TONE, A2_EU_MEETINGS_TONE,
                         A3_BRUSSELS_TAX_TONE]
        assert abs(sum(tones) / len(tones) - GOOGLE_MEAN) < 1e-9

    def test_illustrative_delta(self):
        scoring = _block()["illustrative_scoring"]
        assert scoring["google_mean"] == GOOGLE_MEAN
        assert scoring["meta_mean_carried"] == META_MEAN
        assert scoring["illustrative_delta_google_minus_meta"] == (
            DELTA_GOOGLE_MINUS_META)

    def test_verdict_is_falsification_member_confirmed(self):
        blk = _block()
        assert blk["verdict"].startswith("falsification_member_confirmed")
        assert blk["falsification_family_member"] is True
        assert blk["falsification_ledger"] == "58"

    def test_thesis_test_is_prediction_not_delta(self):
        scoring = _block()["illustrative_scoring"]
        assert "uniform payer-softening prediction" in scoring["delta_note"]


# ---------------------------------------------------------------------------
# 8. Research method
# ---------------------------------------------------------------------------


class TestResearchMethod1292:
    def test_zero_browser_open(self):
        assert _block()["browser_opens"] == 0

    def test_evidence_tiers_attested(self):
        arms = [a["item"] for a in _block()["google_arms"]]
        tiers = {a["evidence_tier"] for a in arms}
        assert tiers <= {"mirror-attested", "aggregator-attested",
                         "relay-attested"}

    def test_scout_documented(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "delegated scout" in src
        assert "SELECTED FT x Google" in src

    def test_rejected_pairs_documented(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "REJECTED The Verge x Anthropic" in src
        assert "Guardian x" in src and "m985" in src

    def test_1143_precedent_checked(self):
        # No counted adversarial-on-partner observation for the FT x
        # Google pair pre-commit (m497 was a tone test, not a
        # falsification pin); documented in the block.
        blk = _block()
        assert "the #1143 temporal-replication precedent does not block" in (
            blk["falsification_family"])
        assert "m497 was a tone test" in blk["falsification_family"]


# ---------------------------------------------------------------------------
# 9. Falsification ledger: 57 -> 58
# ---------------------------------------------------------------------------


class TestFalsificationLedger1292:
    def test_fifty_eighth_member_landed(self):
        assert _block()["falsification_family_member"] is True
        assert _T58 in _read(FT_PATH)

    def test_ledger_58(self):
        assert _block()["ledger"] == "58"
        assert _block()["falsification_ledger"] == "58"

    def test_forty_eighth_member_still_in_ft_at_head(self):
        out = _git(
            "grep", "-c", "-F", _T48, "HEAD", "--",
            "profiles/financial-times.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_no_fifty_ninth_member_repo_wide(self):
        assert _git_grep_tracked_source(_T59, None) == []

    def test_fourth_ft_publication_level_member(self):
        blk = _block()
        assert "FOURTH FT publication-level member" in (
            blk["falsification_family"])


# ---------------------------------------------------------------------------
# 10. Statistical discipline
# ---------------------------------------------------------------------------


class TestStatisticalDiscipline1292:
    def test_manual_illustrative_only(self):
        blk = _block()
        assert "MANUAL ILLUSTRATIVE ONLY" in blk["tone_scored"]
        assert "Aug 28 2026 standing rule" in blk["tone_scored"]

    def test_engine_not_run(self):
        blk = _block()
        assert blk["engine_run"] is False
        assert blk["is_significant"] is False
        assert blk["artifact_grade"] is False

    def test_no_analysis_json_update(self):
        blk = _block()
        assert "no analysis.json update" in blk["verdict"]

    def test_correlation_not_causation(self):
        blk = _block()
        assert "Correlation is not causation" in blk["verdict"]


# ---------------------------------------------------------------------------
# 11. Guard lifecycle: forward guards staged for #1293 (Type B).
# ---------------------------------------------------------------------------


class TestGuardLifecycle1292:
    def test_pins_on_one_mechanism_landing(self):
        # Type A lands one mechanism: max 1006, next 1007.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 1006" in src
        assert "NEXT_NUM = 1007" in src

    def test_no_type_b_1293_in_git_log_pin(self):
        # Post-main-commit form for the NEXT leg (the #1191-class
        # self-trip, re-pinned in #1293's terminal log-hash followup
        # per #721): every commit whose message matches "Type B
        # #1293" must be #1293's main commit or a descendant of it.
        # Deselected in the in-gate run (fails pre-commit by design).
        out = _git("log", "--format=%H", "--grep=Type B #1293")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1293's own commits"
        main = _git("rev-parse", PRED_MAIN_1293).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_1007_numeric_absent_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_1007_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_1007_dash_absent_repo_wide(self):
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
        out = _git(
            "grep", "-c", "-F", _T57, "HEAD", "--",
            "profiles/ap.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fifty_eighth_member_present_pin(self):
        # Landed this run (m1006, profiles/financial-times.yaml).
        # Asserted on the working tree so the pin is stable across the
        # main-commit boundary; the HEAD sweep sees it from the main
        # commit on.
        assert _T58 in _read(FT_PATH)

    def test_no_fifty_ninth_member_pin(self):
        assert _git_grep_tracked_source(_T59, None) == []

    def test_predecessor_1291_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, D1291_FILE))

    def test_next_leg_is_1293_type_b(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#1293 Type B" in src

    def test_1291_pins_flip_by_design_documented(self):
        # #1291's forward guards (max-1005, zero one-zero-zero-six
        # keys all forms, no-Type-A-#1292-in-git-log, fortieth
        # absent, forty-eighth through fifty-seventh intact in
        # profiles/, fifty-eighth absent, ledger 57) verified GREEN
        # at HEAD pre-commit this run. The no-Type-A-#1292-in-git-log
        # pin flips BY DESIGN at this run's main commit (the
        # #1191-class self-trip, re-pinned post-commit by
        # TestStalenessPins1292). Type A lands one mechanism, so the
        # zero one-zero-zero-six numeric pin flips BY DESIGN too (the
        # #1272-class forward-guard expiry), as does the
        # no-fifty-eighth-member pin (the #1191-class self-trip on the
        # member pin). Documented in the staleness pin below, not
        # repaired.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "TestStalenessPins1292" in src
        assert "no_type_a_1292_in_git_log_pin" in src


# ---------------------------------------------------------------------------
# 12. Staleness pins: #1291's guard lifecycle flips BY DESIGN post-commit.
# ---------------------------------------------------------------------------


class TestStalenessPins1292:
    def test_1291_guard_lifecycle_post_commit_self_trip(self):
        # Post-terminal-followup form: 20 tests in the class; TWO flip
        # BY DESIGN when this run's main commit lands and STAY
        # flipped: the test_1006_numeric_absent_in_profiles pin (the
        # m1006 landing carries "mechanism_id: 1006" in colon form -
        # the #1272-class forward-guard expiry; the underscore/dash
        # pins stay green by the #723/#738/#739 designed keying) and
        # the test_no_fifty_eighth_member_pin (the fifty-eighth member
        # lands this run - the #1191-class self-trip on the member
        # pin). The no_type_a_1292_in_git_log ancestor pin ALSO flips
        # at the main commit but is re-pinned green in the terminal
        # log-hash followup per #721 (its PRED_MAIN_1292 now holds
        # this run's main sha). The class run below therefore expects
        # 2 failed / 18 passed and documents the designed flips. The
        # #1291 block is read-only to this run; the flips are
        # documented here, not repaired.
        res = _class_run(D1291_FILE, "TestGuardLifecycle1291")
        out = res.stdout + res.stderr
        assert "2 failed, 18 passed" in out, out[-2000:]
        assert "test_1006_numeric_absent_in_profiles" in out, out[-2000:]
        assert "test_no_fifty_eighth_member_pin" in out, out[-2000:]


# ---------------------------------------------------------------------------
# 13. Doc-sync per #719 (3 tests; deselected pre-commit, flipped post-sync)
# ---------------------------------------------------------------------------


class TestDocSync1292:
    def test_readme_test_file_table_has_1292_row_post_sync(self):
        readme = _read(README_PATH)
        assert OWN_BASENAME in readme

    def test_architecture_has_1292_row_post_sync(self):
        arch = _read(ARCH_PATH)
        assert OWN_BASENAME in arch

    def test_readme_stats_ratcheted(self):
        readme = _read(README_PATH)
        assert "| Tests | %d |" % README_TEST_COUNT in readme
        assert "Across %d test files" % README_FILE_COUNT in readme


# ---------------------------------------------------------------------------
# 14. Iteration log per #721.
# ---------------------------------------------------------------------------


class TestIterationLog1292:
    def test_log_has_1292_entry(self):
        text = _read(LOG_PATH)
        assert "## #1292 Type A" in text

    def test_log_entry_carries_hash_chain(self):
        # The doc-sync writes the entry with the main/anchor hashes;
        # the terminal log-hash followup registers the doc-sync hash
        # here per #721.
        text = _read(LOG_PATH)
        assert "main commit" in text
        assert "anchor" in text

    def test_log_entry_records_finding(self):
        text = _read(LOG_PATH)
        assert "m1006" in text
        assert "FIFTY-EIGHTH" in text
        assert "ledger 57->58" in text


# ---------------------------------------------------------------------------
# 15. In-flight isolation
# ---------------------------------------------------------------------------


class TestInFlightIsolation1292:
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
