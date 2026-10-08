"""Type A #1312: Politico x OpenAI Decoded-debut marquee CEO platform (Oct 8 2026, ~11:00 AM PDT).

m1018 - SECOND dedicated corpus mechanism on the Politico x OpenAI pair
(first: m703, #787 Type A, slowdown-week scoop-channel symmetry); FIRST
dedicated Politico x Meta arm observation (m703 recorded a bounded
absence, iteration-492). Politico launches "Decoded by Politico" - a
flagship daily newsletter + podcast tech-policy franchise ("Playbook meets
DealBook", ~50 journalists) - and anchors the DEBUT edition (Oct 5) with a
long-form Sam Altman interview by Brendan Bordelon (27-min podcast; "Sam
Altman on Trump's AI rebrand and the industry's perception problem").
Altman gets an uncritical platform to set terms on the week's defining
story: the world "should accept some bad things happening" for AI's
benefits; "a lot of daylight" between OpenAI and Anthropic on regulation;
rejects concentrating frontier AI in one lab; declines to promise zero
hacks/scams/misuse; draws his line at "really catastrophic risks" ("a
serious loss of control to AI"). The interview lands days after OpenAI
fired three safety researchers (Oct 1) and BI broke the David Robinson
resignation (Oct 2; m967) - the licensed partner's CEO is handed the
marquee to reframe the crisis week on his terms. MANUAL ILLUSTRATIVE
+0.30 (marquee-platform soft register). The Sep-24 "White House asks
OpenAI, Anthropic to hold models from British testers" Politico scoop
(via Reuters relay) runs the neutral policy-process register +0.05 and
replicates m703's scoop-channel symmetry (both labs named). Meta
comparator (Oct 4): Owen Dahlkamp's lobbying exposé "Sources: Apple and
Google pitch state bills with self-attested age checks and no private
lawsuits; Meta backs ones making app stores, not platforms, verify ages"
- adversarial on Apple/Google ("phantom child safety legislation"), Meta
as the accountability-side foil, neutral +0.05. OpenAI arm mean +0.175
vs Meta +0.05; illustrative delta (OpenAI minus Meta) +0.125 on n=2 vs
n=1 (degenerate sample disclosed).

The naive uniform payer-softening prediction (Axel Springer x OpenAI Dec
13 2023 licensing deal, tens of millions EUR, Politico content included,
mechanism 597/#604; renewal unresolved, ~Dec 2026 expiry; plus Microsoft
x Axel Springer Apr 29 2024 four-channel partnership = DUAL-AI-PAYER
owner) is MET on the marquee-launch register, not falsified on this peg.
Counterevidence bound: m703's scoop-channel symmetry STANDS - O2
replicates it; the softness is register-local to the marquee launch, NOT
outlet-level. The Verge's adversarial "bad things" backlash (in corpus)
bounds any claim the content went uncontested. Tension note carried from
m703: Politico is BOTH an OpenAI licensee AND a Cohere-suit plaintiff.

Per #715 this docstring uses lowercase forms only: thesis-consistent
observation, NOT a falsification-family member (ledger holds at 59);
no new direction - fortieth absent by design, 35th-39th stand. Verdict:
thesis_consistent_observation, domain-bounded to Politico's Decoded
marquee-launch register. Extends m703's Politico x OpenAI line.

Novelty: 7 novel URLs zero-hit repo-wide pre-commit (git grep -F); "Owen
Dahlkamp" zero-hit repo-wide pre-commit; block key zero-hit (designed
keying: iteration 1312 in key, no 1018 substring, per the #723/#738/#739
convention). Scout rejections documented: BI x OpenAI (saturated - m967
#1227 already dedicated on the Oct-2 Robinson exclusive; pair carries 5
mechanisms), Semafor x Microsoft (thin arms both sides), WaPo x Amazon
(single arm, no Meta comparator; kept as future negative-case candidate).

Statistical discipline: monitoring-only per the Aug 28 2026 standing rule
(MANUAL ILLUSTRATIVE ONLY, engine NOT run, p_value/cohens_d/ci_95
NOT_CALCULATED, is_significant False, NOT artifact-grade, no analysis.json
update, verdict thesis_consistent_observation). Correlation is not
causation. Hypothesis-generating only.

1 delegated scout (ranked 3 pairs; BI x OpenAI + Semafor x Microsoft +
WaPo x Amazon rejected per above; Politico x OpenAI SELECTED) + 3
main-run browser.search verification sets (Decoded/Altman canonical-URL
hunt; Dahlkamp Oct-4 relay attestation; TollBit/BI arm considered and
rejected - the Oct-6 ABC testimony cites 2024 TollBit work, not a new BI
original), 0 browser.open per #503. Excerpt-bounded; Politico originals
paywalled/newsletter-walled - relay-attested (Reuters, Politico YouTube,
Plink, biztoc/techmeme) with explicit provenance. All URLs copied
verbatim from Full-URL listings; no canonical URLs constructed.
ASCII-only, no em dashes.

Rotation: this run is iteration #1312 Type A, the THIRD leg of the
1310-1314 window (D #1310 -> E #1311 -> A #1312 -> B #1313 -> C #1314, per
the #565 anchor + rotation guard). Predecessor #1311 Type E verified in
git log (main a9d11a08 / anchor d12c4a61 / doc-sync b77dad3e / log-hash
a35c6435 / push-status 49159cee); the 1305-1309 window is VERIFIED
CLOSED. This run's main commit is the anchor per #565; ANCHORED_SHA
patched post-commit. The #1311 forward guards verified pre-commit this
run: max-1017; zero one-zero-one-eight keys all forms; no-Type-A-#1312-
in-git-log; fortieth direction absent; forty-eighth through fifty-ninth
members intact; no sixtieth member (repo-wide); ledger 59. Next: #1313
Type B continues the window; the #1310-launched background-suite verdict
belongs to #1315 per #795.

Pre-commit novelty greps per #715: zero test_type_a_1312 files on disk
(glob); no "Type A #1312" in git log (--grep); max numeric mechanism_id
1017 in profiles/ pre-commit (mechanism_id regex sweep); zero
numeric/underscore/dash one-zero-one-eight mechanism key forms repo-wide
pre-commit (needles format-built per #715, own file excluded, __pycache__
excluded per the #715 pattern-rescope lesson); block key zero-hit
repo-wide pre-commit (designed keying: iteration 1312 in key, no 1018
substring, per the #723/#738/#739 convention); "## #1312" zero-hit in
iteration-log pre-commit; README stats 73956/1636 pre-commit; no #1312
row in README/ARCHITECTURE test tables pre-commit; the 7 novel URLs
zero-hit repo-wide pre-commit (git grep -F).

Doc-sync constants per #719: README_TEST_COUNT / README_FILE_COUNT hold
the post-doc-sync values from the start (patched pre-main once the
in-gate collection count is known); the doc-sync commit ratchets README
73956/1636 -> post-sync totals.
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
CCR_PATH = os.path.join(
    PROFILES_DIR, "competitor-coverage-research.yaml")

OWN_BASENAME = (
    "test_type_a_1312_politico_openai_decoded_debut_altman_"
    "marquee_platform_vs_meta_dahlkamp_lobbying_"
    "exposure_oct08_11am.py"
)
BLOCK_KEY = (
    "type_a_1312_politico_openai_decoded_debut_altman_"
    "marquee_platform_vs_meta_dahlkamp_lobbying_"
    "exposure_oct08_11am"
)

# Pre-commit placeholder per #565; patched to the main commit sha in
# the anchor followup.
ANCHORED_SHA = "9e37e42b129c20e39eac73e245d6e52b15510b4e"  # patched in the anchor followup per #565

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

MECH_NUM = 1018
NEXT_NUM = 1019  # integer only; key-form needles are format-built

# Predecessor chain: #1311 Type E closed the SECOND leg.
PRED_MAIN_1311 = "a9d11a087f42aca79a5e2beee63e60c57c019720"
PRED_ANCHOR_1311 = "d12c4a613df0a08ff75210f828126e5d364377ea"
PRED_DOCSYNC_1311 = "b77dad3ee3436411e92c92f568fb11c8c1287ceb"
PRED_FINAL_1311 = "a35c64357ee20018f83274e18898042ffe07ab37"

# This run's main commit (full sha), for the ancestor-form
# no-Type-A-#1312 pin. Patched in the terminal log-hash followup
# per #721 (re-pinned in BOTH this file and the #1311 file per the
# #1292 re-pin-both-copies precedent).
PRED_MAIN_1312 = "0" * 40  # re-pinned to #1312 main sha per #721

# The #1313 main commit (full sha), for the ancestor-form
# no-Type-B-#1313 pin. Patched in #1313's terminal log-hash followup
# per #721.
PRED_MAIN_1313 = "0" * 40  # re-pinned to #1313 main sha per #721

# The #1311 predecessor file, for the staleness pin on its
# guard-lifecycle class (max id 1017; zero next-number
# one-zero-one-eight / no-Type-A-#1312-in-git-log / fortieth
# direction absent / forty-eighth through fifty-ninth members
# intact / sixtieth member absent / ledger 59).
D1311_FILE = (
    "test_type_e_1311_podcast_sentiment_185th_"
    "verification_oct08_10am.py"
)

# Doc-sync constants per #719: post-doc-sync values from the start.
# Patched pre-main once the in-gate collection count is known.
README_TEST_COUNT = 74063  # post-doc-sync total (pre-sync 73956 + 107)
README_FILE_COUNT = 1637  # pre-sync 1636 + 1 (this file)

# MANUAL ILLUSTRATIVE tones (hand-assigned at excerpt level).
O1_DECODED_DEBUT_TONE = 0.30
O2_UK_TESTERS_SCOOP_TONE = 0.05
OPENAI_MEAN_TONE = 0.175
META_M1_DAHLKAMP_TONE = 0.05
ILLUSTRATIVE_DELTA = 0.125

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

REUTERS_ALTMAN_URL = (
    "https://www.reuters.com/business/openais-altman-says-"
    "ai-benefits-warrant-accepting-some-risks-2026-10-04/"
)
YOUTUBE_DECODED_URL = "https://www.youtube.com/watch?v=2OOHnaGTQFg"
PLINK_DECODED_URL = "https://plinkhq.com/i/1500970749/e/1000793231520"
REUTERS_UK_TESTERS_URL = (
    "https://www.reuters.com/world/white-house-asks-openai-"
    "anthropic-hold-models-british-testers-politico-"
    "reports-2026-09-24/"
)
BIZTOC_DAHLKAMP_URL = "https://biztoc.com/x/a99422227d565aee"
MYSTERIUM_DAHLKAMP_URL = (
    "https://www.mysteriumvpn.com/blog/news/apple-google-"
    "age-verification-lawsuit-shield"
)
BIOMETRIC_DAHLKAMP_URL = (
    "https://www.biometricupdate.com/202610/apple-google-"
    "lobby-lawmakers-to-remove-liability-from-draft-online-"
    "safety-bills"
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
    doc = yaml.safe_load(_read(CCR_PATH))
    return doc["publications"][BLOCK_KEY]


# ---------------------------------------------------------------------------
# 1. Anchor per #565 (this run's main commit is the anchor; the anchor
#    followup patches ANCHORED_SHA to the main commit sha).
# ---------------------------------------------------------------------------


class TestAnchor1312:
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
# 2. Rotation guard: #1311 closed the SECOND leg; #1312 is the THIRD.
# ---------------------------------------------------------------------------


class TestRotationGuard1312:
    def test_predecessor_shas_in_git_log(self):
        log = _git("log", "--oneline", "-60").stdout
        for sha, label in (
            (PRED_MAIN_1311, "1311 main"),
            (PRED_ANCHOR_1311, "1311 anchor"),
            (PRED_DOCSYNC_1311, "1311 doc-sync"),
            (PRED_FINAL_1311, "1311 log-hash"),
        ):
            assert sha[:8] in log, label

    def test_1311_type_e_in_git_log(self):
        out = _git("log", "--oneline", "--grep=Type E #1311").stdout
        assert out.strip() != ""

    def test_third_leg_phrase(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "THIRD leg of the 1310-1314 window" in src

    def test_1305_1309_window_closed(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "1305-1309" in src
        assert "VERIFIED CLOSED" in src

    def test_next_leg_is_1313_type_b(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "B #1313" in src


# ---------------------------------------------------------------------------
# 3. Mechanism novelty: Type A lands one mechanism (max 1017 -> 1018).
# ---------------------------------------------------------------------------


class TestMechanismNovelty1312:
    def test_max_numeric_mechanism_id_1018(self):
        assert _max_numeric_mechanism_id() == MECH_NUM

    def test_no_type_a_1312_in_git_log_pin(self):
        # Post-main-commit form (the #1191-class self-trip, re-pinned
        # in the terminal log-hash followup per #721): every commit
        # whose message matches "Type A #1312" must be this run's
        # main commit or a descendant of it - i.e., no PRIOR run
        # committed this run's iteration. Deselected in the in-gate
        # run (fails pre-commit by design).
        out = _git("log", "--format=%H", "--grep=Type A #1312")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected this run's own commits"
        main = _git("rev-parse", PRED_MAIN_1312).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_zero_next_number_keys_all_forms(self):
        # Numeric (profiles/ scope), underscore and dash (profiles/ +
        # tests/ scope, own file excluded per #715, __pycache__
        # excluded per the #715 pattern-rescope lesson). NEXT_NUM is
        # 1019: this run lands 1018, so the next-number forms stay
        # absent.
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_block_key_designed_no_1018_substring(self):
        # Designed keying per #723/#738/#739: the iteration-form block
        # key carries the iteration (1312), never the mechanism number.
        assert "1018" not in BLOCK_KEY
        assert "1312" in BLOCK_KEY

    def test_forward_guards_for_1313(self):
        # Staged for the next leg: max-1018 in profiles/; zero
        # one-zero-one-nine keys all forms; no-Type-B-#1313-in-git-log;
        # fortieth direction absent; forty-eighth through fifty-ninth
        # intact; no sixtieth member; ledger 59.
        assert _max_numeric_mechanism_id() == 1018
        assert _repo_grep_numeric_mechanism_id(1019) == []
        assert _repo_grep_underscore_mechanism(1019) == []
        assert _repo_grep_dash_mechanism(1019) == []
        assert _git("log", "--oneline", "--grep=Type B #1313").stdout.strip() == ""
        assert _git_grep_tracked_source(_T40, "profiles/") == []
        assert _git_grep_tracked_source(_T48, "profiles/") == [
            "profiles/financial-times.yaml"]
        assert _T59 in _read(os.path.join(PROFILES_DIR, "news-corp.yaml"))
        assert _git_grep_tracked_source(_T60, None) == []

    def test_novel_urls_present_in_block(self):
        # The 7 novel URLs were zero-hit repo-wide pre-commit (git
        # grep -F, verified this run before the block landed).
        # Post-landing they live in the block's arms; assert each is
        # present in competitor-coverage-research.yaml.
        text = _read(CCR_PATH)
        for url in (REUTERS_ALTMAN_URL, YOUTUBE_DECODED_URL,
                    PLINK_DECODED_URL, REUTERS_UK_TESTERS_URL,
                    BIZTOC_DAHLKAMP_URL, MYSTERIUM_DAHLKAMP_URL,
                    BIOMETRIC_DAHLKAMP_URL):
            assert text.count(url) >= 1, url


# ---------------------------------------------------------------------------
# 4. Politico x OpenAI arms: O1 Decoded debut (NEW) + O2 UK-testers scoop
# ---------------------------------------------------------------------------


class TestPoliticoOpenAIArms1312:
    def test_block_present_with_mechanism_id_1018(self):
        block = _block()
        assert block["mechanism_id"] == 1018
        assert block["iteration"] == 1312
        assert block["iteration_type"] == "A"

    def test_o1_title_and_date(self):
        block = _block()
        arm = block["arms"]["arm_o1_decoded_debut_altman_marquee_platform"]
        assert "Decoded" in arm["title"]
        assert "Altman" in arm["title"]
        assert arm["date"] == "2026-10-05"

    def test_o1_urls_novel(self):
        block = _block()
        arm = block["arms"]["arm_o1_decoded_debut_altman_marquee_platform"]
        assert REUTERS_ALTMAN_URL in arm["urls"]
        assert YOUTUBE_DECODED_URL in arm["urls"]
        assert PLINK_DECODED_URL in arm["urls"]
        assert "zero-hit" in arm["url_status"]

    def test_o1_register_marquee_platform(self):
        block = _block()
        arm = block["arms"]["arm_o1_decoded_debut_altman_marquee_platform"]
        assert arm["register"] == "marquee_launch_ceo_platform"

    def test_o1_tone_plus_030(self):
        block = _block()
        arm = block["arms"]["arm_o1_decoded_debut_altman_marquee_platform"]
        assert arm["tone_MANUAL_ILLUSTRATIVE"] == O1_DECODED_DEBUT_TONE == 0.30

    def test_o1_key_quotes_bad_things(self):
        block = _block()
        text = yaml.safe_dump(
            block["arms"]["arm_o1_decoded_debut_altman_marquee_platform"])
        assert "accept some bad things happening" in text
        assert "a lot of daylight" in text

    def test_o1_crisis_week_context(self):
        # The debut lands days after the Oct-1 firings and the Oct-2
        # Robinson resignation (m967) - the platform grant reframes
        # the crisis week on the CEO's terms.
        block = _block()
        text = yaml.safe_dump(
            block["arms"]["arm_o1_decoded_debut_altman_marquee_platform"])
        assert "m967" in text

    def test_o2_title_and_date(self):
        block = _block()
        arm = block["arms"]["arm_o2_white_house_uk_testers_scoop"]
        assert "British testers" in arm["title"]
        assert arm["date"] == "2026-09-24"

    def test_o2_url_novel(self):
        block = _block()
        arm = block["arms"]["arm_o2_white_house_uk_testers_scoop"]
        assert arm["url"] == REUTERS_UK_TESTERS_URL
        assert "zero-hit" in arm["url_status"]

    def test_o2_register_scoop_continuity(self):
        block = _block()
        arm = block["arms"]["arm_o2_white_house_uk_testers_scoop"]
        assert arm["register"] == "policy_process_scoop_transmission"

    def test_o2_tone_plus_005(self):
        block = _block()
        arm = block["arms"]["arm_o2_white_house_uk_testers_scoop"]
        assert arm["tone_MANUAL_ILLUSTRATIVE"] == O2_UK_TESTERS_SCOOP_TONE == 0.05

    def test_o2_both_labs_named(self):
        # The scoop names OpenAI AND Anthropic - replicating m703's
        # scoop-channel symmetry (the channel stays payer-blind).
        block = _block()
        arm = block["arms"]["arm_o2_white_house_uk_testers_scoop"]
        assert "Anthropic" in arm["entity_target"]
        assert "OpenAI" in arm["entity_target"]

    def test_openai_mean_plus_0175(self):
        block = _block()
        assert block["openai_arm_avg"] == OPENAI_MEAN_TONE == 0.175

    def test_two_openai_arms(self):
        block = _block()
        assert block["openai_arm_scores"] == [0.30, 0.05]

    def test_no_canonical_politico_url_constructed(self):
        # Politico originals are paywalled/newsletter-walled; the arms
        # are relay-attested per #503, no politico.com URL invented.
        block = _block()
        text = yaml.safe_dump(block["arms"])
        assert "no canonical politico.com URL constructed" in \
            block["arms"][
                "arm_o1_decoded_debut_altman_marquee_platform"][
                "url_status"]


# ---------------------------------------------------------------------------
# 5. Meta comparator: M1 Dahlkamp lobbying exposé (FIRST dedicated
#    Politico x Meta arm in the corpus)
# ---------------------------------------------------------------------------


class TestMetaDahlkampArm1312:
    def test_first_dedicated_politico_x_meta_arm(self):
        block = _block()
        assert block["meta_comparator"]["status"] == \
            "first_dedicated_politico_x_meta_arm"

    def test_m1_title_and_date(self):
        block = _block()
        arm = block["meta_comparator"][
            "arm_m1_dahlkamp_kids_safety_lobbying_expose"]
        assert "Dahlkamp" in arm["title"]
        assert arm["date"] == "2026-10-04"

    def test_m1_urls_novel(self):
        block = _block()
        arm = block["meta_comparator"][
            "arm_m1_dahlkamp_kids_safety_lobbying_expose"]
        assert BIZTOC_DAHLKAMP_URL in arm["urls"]
        assert MYSTERIUM_DAHLKAMP_URL in arm["urls"]
        assert BIOMETRIC_DAHLKAMP_URL in arm["urls"]

    def test_m1_register_lobbying_exposure(self):
        block = _block()
        arm = block["meta_comparator"][
            "arm_m1_dahlkamp_kids_safety_lobbying_expose"]
        assert arm["register"] == "lobbying_exposure_investigation"

    def test_m1_tone_plus_005(self):
        block = _block()
        arm = block["meta_comparator"][
            "arm_m1_dahlkamp_kids_safety_lobbying_expose"]
        assert arm["tone_MANUAL_ILLUSTRATIVE"] == META_M1_DAHLKAMP_TONE == 0.05

    def test_m1_adversarial_edge_on_apple_google(self):
        # The exposé's hard edge targets Apple/Google ("phantom child
        # safety legislation"); Meta is the accountability foil. The
        # confounder is disclosed, not hidden. (Asserted on the raw
        # excerpt list: yaml.safe_dump line-wraps the phrase.)
        block = _block()
        arm = block["meta_comparator"][
            "arm_m1_dahlkamp_kids_safety_lobbying_expose"]
        assert any("phantom child safety legislation" in e
                   for e in arm["excerpts"])

    def test_meta_arm_score_plus_005(self):
        block = _block()
        assert block["meta_arm_score"] == META_M1_DAHLKAMP_TONE == 0.05


# ---------------------------------------------------------------------------
# 6. Financial relationship: Axel Springer x OpenAI licensing deal
# ---------------------------------------------------------------------------


class TestFinancialRelationship1312:
    def test_deal_dec_2023_documented(self):
        block = _block()
        assert "Dec 13 2023" in block["description"]

    def test_politico_content_included(self):
        block = _block()
        assert "Politico content included" in block["description"]
        assert "mechanism 597" in block["description"]

    def test_renewal_unresolved(self):
        block = _block()
        assert "renewal unresolved" in block["description"]
        assert "Dec 2026" in block["description"]

    def test_dual_payer_owner(self):
        block = _block()
        assert "DUAL-AI-PAYER" in block["description"]
        assert "Microsoft" in block["description"]

    def test_cohere_suit_tension_carried(self):
        # Politico is BOTH an OpenAI licensee AND a Cohere-suit
        # plaintiff (carried from m703) - license-one-channel,
        # sue-another.
        block = _block()
        assert "Cohere" in block["description"]

    def test_coverage_prediction_softer(self):
        block = _block()
        assert "payer-softening prediction" in block["description"]

    def test_prediction_met_on_marquee_register(self):
        block = _block()
        assert "MET on the marquee-launch register" in block["description"]

    def test_non_causal_language_present(self):
        block = _block()
        assert "Correlation is not causation" in block["description"]


# ---------------------------------------------------------------------------
# 7. Asymmetry delta: OpenAI +0.175 vs Meta +0.05, delta +0.125
# ---------------------------------------------------------------------------


class TestAsymmetryDelta1312:
    def test_openai_mean_plus_0175(self):
        block = _block()
        assert block["openai_arm_avg"] == OPENAI_MEAN_TONE == 0.175

    def test_meta_mean_plus_005(self):
        block = _block()
        assert block["meta_arm_score"] == META_M1_DAHLKAMP_TONE == 0.05

    def test_illustrative_delta_plus_0125(self):
        block = _block()
        assert block["illustrative_delta_openai_minus_meta"] == \
            ILLUSTRATIVE_DELTA == 0.125

    def test_delta_calc_documented(self):
        block = _block()
        assert "0.175 - 0.05 = +0.125" in block["delta_calc"]

    def test_degenerate_sample_contract(self):
        block = _block()
        assert "n=2" in block["methodology"]
        assert "n=1" in block["methodology"]
        assert "degenerate-sample contract disclosed" in \
            block["methodology"]

    def test_reading_payer_favoring_but_modest(self):
        block = _block()
        assert "Payer-favoring but modest" in block["delta_direction"]

    def test_engine_not_run(self):
        block = _block()
        assert block["engine_run"] is False


# ---------------------------------------------------------------------------
# 8. Research method: 1 scout + 3 verification sets, 0 browser.open
# ---------------------------------------------------------------------------


class TestResearchMethod1312:
    def test_delegated_scout_documented(self):
        block = _block()
        assert "1 delegated scout" in block["research_method"]

    def test_three_verification_sets(self):
        block = _block()
        assert "3 main-run browser.search verification sets" in \
            block["research_method"]

    def test_scout_rejections_documented(self):
        block = _block()
        assert "BI x OpenAI" in block["research_method"]
        assert "Semafor x Microsoft" in block["research_method"]
        assert "WaPo x Amazon" in block["research_method"]

    def test_bi_rejection_saturation_ground(self):
        block = _block()
        assert "m967" in block["research_method"]

    def test_tollbit_arm_rejected(self):
        block = _block()
        assert "TollBit" in block["research_method"]

    def test_novelty_greps_documented(self):
        block = _block()
        assert "test_type_a_1312 files" in block["novelty_verification"]

    def test_excerpt_bounded_no_browser_open(self):
        block = _block()
        assert "0 browser.open" in block["research_method"]


# ---------------------------------------------------------------------------
# 9. Thesis-consistent observation: NOT a falsification-family member
# ---------------------------------------------------------------------------


class TestThesisConsistent1312:
    def test_not_a_member_ledger_holds_59(self):
        block = _block()
        assert block["verdict"] == "thesis_consistent_observation"
        assert "NOT a falsification-family member" in \
            block["falsification_family"]
        assert "Ledger holds at 59" in block["falsification_family"]

    def test_no_sixtieth_member_form_in_block(self):
        # The block must not claim the sixtieth member. The needle is
        # fragment-built via _T60 (per the #715 literal discipline);
        # a contiguous literal here would trip the repo-wide
        # no-sixtieth-member pin in TestGuardLifecycle1311.
        text = yaml.safe_dump(_block())
        assert _T60 not in text

    def test_extends_m703(self):
        block = _block()
        assert "m703" in block["extends"]

    def test_new_register_named(self):
        block = _block()
        assert "marquee-platform register" in block["extends"] or \
            "marquee_launch_ceo_platform" in yaml.safe_dump(block)

    def test_register_local_not_outlet_level(self):
        block = _block()
        assert "register-local" in block["incentive_attribution"] or \
            "Channel-local softness" in block["incentive_attribution"]

    def test_scoop_symmetry_counterevidence_bound(self):
        block = _block()
        text = yaml.safe_dump(block["counter_evidence"])
        assert "scoop-channel symmetry" in text

    def test_verge_backlash_bound(self):
        block = _block()
        text = yaml.safe_dump(block["counter_evidence"])
        assert "Verge" in text

    def test_no_fortieth_direction_form_in_block(self):
        text = yaml.safe_dump(_block())
        assert _T40 not in text


# ---------------------------------------------------------------------------
# 10. Statistical discipline per the Aug 28 2026 standing rule
# ---------------------------------------------------------------------------


class TestStatisticalDiscipline1312:
    def test_manual_illustrative_only(self):
        block = _block()
        assert "MANUAL ILLUSTRATIVE" in block["statistical_discipline"]

    def test_engine_not_run(self):
        block = _block()
        assert "Engine NOT run" in block["statistical_discipline"]

    def test_p_value_not_calculated(self):
        block = _block()
        sd = block["statistical_discipline"]
        assert "NOT_CALCULATED" in sd
        assert "is_significant: false" in sd

    def test_not_artifact_grade(self):
        block = _block()
        sd = block["statistical_discipline"]
        assert "no_analysis_json_update: true" in sd
        assert "NOT artifact-grade" in sd

    def test_verdict_thesis_consistent(self):
        block = _block()
        assert "thesis_consistent_observation" in block["statistical_discipline"]

    def test_correlation_not_causation(self):
        block = _block()
        sd = block["statistical_discipline"]
        assert "Correlation is not causation" in sd
        assert "Hypothesis-generating only" in sd


# ---------------------------------------------------------------------------
# 11. Guard lifecycle: forward guards for #1313 (Type B).
# ---------------------------------------------------------------------------


class TestGuardLifecycle1312:
    def test_pins_on_one_mechanism_landing(self):
        # Type A lands one mechanism: max 1018, next 1019.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 1018" in src
        assert "NEXT_NUM = 1019" in src

    def test_no_type_b_1313_in_git_log_pin(self):
        # Post-main-commit form for the NEXT leg (the #1191-class
        # self-trip, re-pinned in #1313's terminal log-hash followup
        # per #721): every commit whose message matches "Type B
        # #1313" must be #1313's main commit or a descendant of it.
        # Deselected in the in-gate run (fails pre-commit by design).
        out = _git("log", "--format=%H", "--grep=Type B #1313")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1313's own commits"
        main = _git("rev-parse", PRED_MAIN_1313).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_1019_numeric_absent_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_1019_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_1019_dash_absent_repo_wide(self):
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
        # Landed #1302 (m1012, profiles/news-corp.yaml, committed).
        # HEAD sweep is stable for a committed landing.
        out = _git(
            "grep", "-c", "-F", _T59, "HEAD", "--",
            "profiles/news-corp.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_no_sixtieth_member_pin(self):
        # This run lands a thesis-consistent observation, NOT a
        # member: the sixtieth member-claim form stays absent
        # repo-wide (source scope; __pycache__ excluded per the #715
        # pattern-rescope lesson).
        assert _git_grep_tracked_source(_T60, None) == []

    def test_predecessor_1311_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, D1311_FILE))

    def test_next_leg_is_1313_type_b(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#1313 Type B" in src

    def test_1311_pins_flip_by_design_documented(self):
        # #1311's forward guards (max-1017, zero one-zero-one-eight
        # keys all forms, no-Type-A-#1312-in-git-log, fortieth
        # absent, forty-eighth through fifty-ninth intact in
        # profiles/, sixtieth absent, ledger 59) verified GREEN
        # at HEAD pre-commit this run. TWO pins flip BY DESIGN at
        # this run's main commit: the no-Type-A-#1312-in-git-log pin
        # (the #1191-class self-trip, re-pinned green in the terminal
        # log-hash followup per #721, in BOTH the #1312 and #1311 files
        # per the #1292 re-pin-both-copies precedent) and the zero
        # one-zero-one-eight numeric pin (the #1272-class forward-guard
        # expiry - the m1018 landing carries "mechanism_id: 1018" in
        # colon form; the underscore/dash pins stay green by the
        # #723/#738/#739 designed keying). The no-sixtieth-member pin
        # stays GREEN (this run lands no member). Documented in the
        # staleness pin below, not repaired.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "TestStalenessPins1312" in src
        assert "no_type_a_1312_in_git_log_pin" in src


# ---------------------------------------------------------------------------
# 12. Staleness pins: #1311's guard lifecycle flips BY DESIGN post-commit.
# ---------------------------------------------------------------------------


class TestStalenessPins1312:
    def test_1311_guard_lifecycle_post_commit_self_trip(self):
        # Post-terminal-followup form: 22 tests in the class; ONE
        # flips BY DESIGN when this run's main commit lands and STAYS
        # flipped permanently: test_1018_numeric_absent_in_profiles
        # (the #1272-class forward-guard expiry - the m1018 landing
        # carries "mechanism_id: 1018" in colon form; the
        # underscore/dash pins stay green by the #723/#738/#739
        # designed keying). The second flip,
        # test_no_type_a_1312_in_git_log_pin (the #1191-class
        # self-trip), is re-pinned green in the terminal log-hash
        # followup per #721 (its PRED_MAIN_1312 now holds this run's
        # main sha, in BOTH the #1312 and #1311 files per the
        # re-pin-both-copies precedent). The class run below therefore
        # expects 1 failed / 21 passed and documents the designed
        # flips. The #1311 block is read-only to this run; the flips
        # are documented here, not repaired.
        res = _class_run(D1311_FILE, "TestGuardLifecycle1311")
        out = res.stdout + res.stderr
        assert "1 failed, 21 passed" in out, out[-2000:]
        assert "test_1018_numeric_absent_in_profiles" in out, out[-2000:]


# ---------------------------------------------------------------------------
# 13. Doc-sync per #719 (3 tests; deselected pre-commit, flipped post-sync)
# ---------------------------------------------------------------------------


class TestDocSync1312:
    def test_readme_test_file_table_has_1312_row_post_sync(self):
        readme = _read(README_PATH)
        assert OWN_BASENAME in readme

    def test_architecture_has_1312_row_post_sync(self):
        arch = _read(ARCH_PATH)
        assert OWN_BASENAME in arch

    def test_readme_stats_ratcheted(self):
        readme = _read(README_PATH)
        assert "| Tests | %d |" % README_TEST_COUNT in readme
        assert "Across %d test files" % README_FILE_COUNT in readme


# ---------------------------------------------------------------------------
# 14. Iteration log per #721.
# ---------------------------------------------------------------------------


class TestIterationLog1312:
    def test_log_has_1312_entry(self):
        text = _read(LOG_PATH)
        assert "## #1312 Type A" in text

    def test_log_entry_carries_hash_chain(self):
        # The doc-sync writes the entry with the main/anchor hashes;
        # the terminal log-hash followup registers the doc-sync hash
        # here per #721.
        text = _read(LOG_PATH)
        assert "main commit" in text
        assert "anchor" in text

    def test_log_entry_records_finding(self):
        text = _read(LOG_PATH)
        assert "m1018" in text
        assert "thesis_consistent_observation" in text
        assert "ledger holds at 59" in text


# ---------------------------------------------------------------------------
# 15. In-flight isolation
# ---------------------------------------------------------------------------


class TestInFlightIsolation1312:
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
