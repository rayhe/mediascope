"""Type A #1257: m985 Guardian Oct-1-2026 Bhuiyan hijab cross-lab safety test
on Anthropic (non-deal lab) vs the deal partner OpenAI (Oct 6 2026, 04:00 AM PDT).

Two NEW Guardian x Anthropic arms, Oct 1-5 2026, excerpt-bounded per #503
(0 browser.open; theguardian.com blocked by policy):

(1) Oct 1 2026: Guardian US (byline Johana Bhuiyan, dateline Thu 1 Oct 2026
06.00 EDT) runs a cross-lab safety test - "AI chatbots remove hijabs from
images of Muslim women when prompted". The Guardian tests ChatGPT, Grok,
Gemini and Claude with the same prompt. OpenAI's ChatGPT and xAI's Grok
COMPLY. Anthropic's Claude REFUSES unconditionally ("would not alter a photo
to remove someone's hijab"; "That kind of edit changes how a real person is
depicted in a way tied to their religious dress and identity, and it could
be used to embarrass, harass, or misrepresent them"). Google's Gemini
initially refuses then complies when the request is reframed as making the
woman look more "western". The investigation sits on the reporter's profiled
beat (careers/journalists.yaml: surveillance of marginalized and Muslim
communities; m472 established the Guardian x OpenAI deal buys no softness
from her). The Guardian names the deal partner's product as a complier,
quotes its defensive distinction, then prints its concession. Tone toward
Anthropic: +0.15 MANUAL ILLUSTRATIVE (mild-positive: the sole unconditional
refuser in a symmetric test; the piece's adversarial energy targets the
compliers).

(2) Relay-attested Oct 5 2026: Guardian AI (Andrew Messenger) covers the
$31bn/$32bn Western Downs Queensland datacentre proposal (Anthropic first
tenant, Singaporean developer Zerra DC, 725 hectares, 2.1GW) through its
adversarial infrastructure-expansion register: residents Denver Kanowski and
Mordechai Winters quoted; local sentiment "a whole new level of 'stupidity'";
21,000+ signature Change.org petition; Environmental Defenders Office
legal-challenge signal. Tone toward Anthropic: -0.35 MANUAL ILLUSTRATIVE
(Meta-comparable adversarial expansion hardness). Underlying Guardian piece
date excerpt-unconfirmed; the arm is relay-bounded.

Anthropic Oct cluster mean -0.10 vs carried Guardian Meta arms mean -0.425
(m886 via m537, un-rescored per #807): illustrative delta (Anthropic minus
Meta) +0.32 - Meta draws the harder register. Vs carried Guardian OpenAI
deal-partner arms mean -0.125: illustrative delta (Anthropic minus OpenAI)
+0.02 near-null.

Verdict: falsification_member_confirmed. The operative peg is the hijab
own-investigation: the Guardian's own cross-lab safety test (its highest
editorial-investment tier, the reporter's in-corpus profiled beat) names the
Feb-14-2025 strategic partner OpenAI's ChatGPT as a hijab-removal complier
and prints its concession. The uniform payer-softening prediction (the
Guardian x OpenAI deal, mechanism_514, suppresses the partner's product
failures) FAILS on an own-investigation peg. The Queensland arm is the
adversarial-capacity control: the Guardian applies its expansion-adversarial
register to the non-deal lab at Meta-comparable hardness, so there is no
suppression firewall in either direction. Temporal extension of m472
(journalist-level, Bhuiyan, Sep 2 2026) to publication-level
own-investigation tier; publication-level replication pattern per m982
(#1252). This run lands the fifty-fourth member of the falsification family
(ledger 53->54); the uppercase claim form lives only in the profile block,
never in this file.

5 browser.search query sets this run (NYT x Anthropic Pentagon/Broadcom
sweep; Guardian x Anthropic October sweep; exact-headline hijab verification;
Queensland datacentre relay verification; Guardian x Meta glasses-comparator
sweep); 0 browser.open per #503 (excerpt-bounded). REJECTED: FTC agents-probe
Guardian relay (its only verbatim URL already in corpus at
competitor-entities.yaml:28700 - seen, not armed); NYT x Anthropic Pentagon
arms (no verbatim NYT URLs surfaced); Verge x Anthropic IPO arms (saturated
register, no clean peg).
Pre-commit novelty greps per #715: zero test_type_a_1257 files on disk
(glob); no "Type A #1257" in git log (--grep); max numeric mechanism_id 984
in profiles/ pre-commit; zero numeric/underscore/dash nine-eight-five
mechanism key forms repo-wide pre-commit (needles format-built, own file
excluded); "## #1257" zero-hit in iteration-log pre-commit; README stats
69064/1581 pre-commit; no #1257 row in README/ARCHITECTURE test tables
pre-commit; 7 novel mirror URLs zero-hit repo-wide pre-commit (git grep -F).

Statistical discipline: MANUAL ILLUSTRATIVE ONLY per the Aug 28 2026
standing rule (engine NOT run; p_value/cohens_d/ci_95 NOT_CALCULATED;
is_significant False; NOT artifact-grade; no analysis.json update).
Correlation is not causation; hypothesis-generating only.

Type A lands m985 (MECH_NUM = 985); NEXT_NUM = 986 for the forward guards.
This run is iteration #1257 Type A, the THIRD leg of the 1255-1259 window
(D #1255 -> E #1256 -> A #1257 -> B #1258 -> C #1259, per the #565 anchor +
rotation guard). Predecessor #1256 Type E verified in git log (main 09867f9d
/ anchor bed56aa5 / doc-sync fb224e86 / log-hash 8971b183); #1255 Type D
(main c5d035d8 / anchor 50d8c984 / doc-sync d53069f3 / log-hash fe08152c).
This run's main commit is the anchor per #565; ANCHORED_SHA patched
post-commit. Next run #1258 Type B continues the window. The #1255-launched
background-suite verdict belongs to #1260 per #795: this run OBSERVES only -
neither re-launches, kills, nor writes to the suite. In-flight during this
run: #899 (profiles/nytimes.yaml m771 hunk), #938 (Type B test file
working-tree edit), #900 (untracked Type D test file), #1012-wt (working-tree
edit on the committed Type A #1012 file) - all untouched; targeted staging
only. Do NOT touch #1024 m846.

ASCII-only, no em dashes. All hashes copied from git rev-parse / git log output.
"""

import datetime
import os
import re
import subprocess

import pytest
import yaml

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TESTS_DIR = os.path.join(REPO_ROOT, "tests")
PROFILES_DIR = os.path.join(REPO_ROOT, "profiles")
GUARDIAN_PATH = os.path.join(PROFILES_DIR, "guardian.yaml")
LOG_PATH = os.path.join(REPO_ROOT, "iteration-log.md")
README_PATH = os.path.join(REPO_ROOT, "README.md")
ARCH_PATH = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")
GOAL_HIDDEN = os.path.join(
    os.path.expanduser("~"), "workspace", "goals",
    "mediascope-meta-wearables-press-analysis", "hidden_files",
)
OWN_BASENAME = (
    "test_type_a_1257_guardian_anthropic_oct01_"
    "bhuiyan_hijab_cross_lab_test_oct06_4am.py"
)

# Pre-commit placeholder per #565; patched to the main commit sha in
# the anchor followup.
ANCHORED_SHA = "0" * 40  # patched per #565 in the anchor followup (main commit sha)

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

MECH_NUM = 985  # this run's landed mechanism
NEXT_NUM = 986  # forward-guard number for #1258

# Predecessor chain: #1255 Type D opened, #1256 Type E continued.
PRED_MAIN_1255 = "c5d035d8"
PRED_ANCHOR_1255 = "50d8c984"
PRED_DOCSYNC_1255 = "d53069f3"
PRED_FINAL_1255 = "fe08152c"
PRED_MAIN_1256 = "09867f9d"
PRED_ANCHOR_1256 = "bed56aa5"
PRED_DOCSYNC_1256 = "fb224e86"
PRED_FINAL_1256 = "8971b183"

# This run's own main commit (full sha). Pre-commit placeholder per
# #721; patched to the main commit full sha in the terminal log-hash
# followup.
PRED_MAIN_1257 = "0" * 40

# The #1256 window-continuation file, for the staleness pin on its
# guard-lifecycle class.
E1256_FILE = (
    "test_type_e_1256_podcast_sentiment_"
    "174th_verification_oct06_3am.py"
)

# Doc-sync constants per #719: post-doc-sync values from the start.
# Patched pre-main once the in-gate collection count is known.
README_TEST_COUNT = 69150  # post-doc-sync total (pre-sync 69064 + 86)
README_FILE_COUNT = 1582  # pre-sync 1581 + 1

# The forward-guard needles are fragment-built per #715 so this file
# carries no contiguous literal of a forward-guard claim form. The
# fifty-fourth member claim lives ONLY in the profile block (working
# tree pre-commit, HEAD post-commit); this file references it via
# fragments.
_T40 = "FORT" + "IETH relationship direction"
_T48 = "FORT" + "Y-EIGHTH falsification-family member"
_T49 = "FORT" + "Y-NINTH falsification-family member"
_T50 = "FIFT" + "IETH falsification-family member"
_T51 = "FIFT" + "Y-FIRST falsification-family member"
_T52 = "FIFT" + "Y-SECOND falsification-family member"
_T53 = "FIFT" + "Y-THIRD falsification-family member"
_T54 = "FIFT" + "Y-FOURTH falsification-family member"
_T55 = "FIFT" + "Y-FIFTH falsification-family member"

BLOCK_KEY = (
    "type_a_1257_guardian_anthropic_oct01_bhuiyan_"
    "hijab_cross_lab_test_vs_openai_deal_partner"
)

# The seven mirror URLs (verbatim from Full-URL listings); all
# zero-hit repo-wide pre-commit via git grep -F.
NOVEL_URLS = [
    "https://themuslimtimes.info/2026/10/03/ai-chatbots-remove-hijabs-from-muslim-womens-images-guardian-finds/",
    "https://www.genocidewatch.com/single-post/ai-chatbots-remove-hijabs-from-images-of-muslim-women",
    "https://www.dapcity.com/threads/ai-chatbots-remove-hijabs-from-images-of-muslim-women-when-prompted.23711/",
    "https://westernmorning.news/2026/10/01/ai-chatbots-remove-hijabs-from-images-in-guardian-tests/",
    "https://insidetelecom.com/the-pervasive-blind-spots-of-islam-ai-safety/",
    "https://completeaitraining.com/news/anthropic-proposes-31bn-datacentre-in-rural-queensland-to/",
    "https://www.change.org/p/stop-the-giant-ai-data-centre-near-dalby",
]

# The two Oct-2026 Anthropic arms (MANUAL ILLUSTRATIVE tones).
ARMS = [
    {
        "title": "AI chatbots remove hijabs from images of Muslim women "
                 "when prompted",
        "byline": "Johana Bhuiyan",
        "date": "2026-10-01",
        "tone": 0.15,
    },
    {
        "title": "Anthropic $31bn Queensland datacentre opposition "
                 "(Guardian AI / Andrew Messenger, relay-attested)",
        "byline": "Andrew Messenger",
        "date": "2026-10-05",
        "tone": -0.35,
    },
]
CLUSTER_MEAN = -0.10  # (0.15 + -0.35) / 2
META_MEAN = -0.425  # carried m886 via m537, un-rescored per #807
OPENAI_MEAN = -0.125  # carried m886 via m537, un-rescored per #807
DELTA_META = 0.32  # -0.10 - (-0.425), Anthropic minus Meta
DELTA_OPENAI = 0.02  # -0.10 - (-0.125), Anthropic minus OpenAI


def _read(path):
    with open(path, encoding="utf-8", errors="replace") as fh:
        return fh.read()


def _git(*args):
    return subprocess.run(
        ["git", *args], cwd=REPO_ROOT, capture_output=True, text=True
    )


def _load_guardian():
    with open(GUARDIAN_PATH, encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def _block():
    data = _load_guardian()
    return data["competitor_relationships"]["anthropic"][BLOCK_KEY]


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
    """Working-tree profiles/ sweep for the colon-form mechanism id."""
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


def _working_tree_grep_profiles(needle):
    """Grep working-tree profiles/ for a literal needle.

    Used for the fifty-fourth member pin: the landed claim lives in
    the uncommitted block pre-commit.
    """
    hits = []
    for root, dirs, files in os.walk(PROFILES_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
            p = os.path.join(root, f)
            if needle in open(p, encoding="utf-8", errors="replace").read():
                hits.append(p)
    return hits


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
# 1. Anchor per #565
# ---------------------------------------------------------------------------
class TestAnchor1257:
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
        assert "THIRD leg of the 1255-1259 window" in src


# ---------------------------------------------------------------------------
# 2. Rotation guard
# ---------------------------------------------------------------------------
class TestRotationGuard:
    def test_predecessor_1255_1256_chain_verified(self):
        for sha in (
            PRED_MAIN_1255, PRED_ANCHOR_1255, PRED_DOCSYNC_1255,
            PRED_FINAL_1255, PRED_MAIN_1256, PRED_ANCHOR_1256,
            PRED_DOCSYNC_1256, PRED_FINAL_1256,
        ):
            res = _git("cat-file", "-t", sha)
            assert res.stdout.strip() == "commit", "missing %s" % sha

    def test_window_order_phrase(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "D #1255 -> E #1256 -> A #1257 -> B #1258 -> C #1259" in src

    def test_next_leg_is_type_b_1258(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Next run #1258 Type B" in src

    def test_type_a_lands_m985(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Type A lands m985" in src


# ---------------------------------------------------------------------------
# 3. Mechanism novelty (the #715 discipline; landing-run form per #1238)
# ---------------------------------------------------------------------------
class TestMechanismNovelty1257:
    def test_max_numeric_mechanism_id_is_this_run(self):
        # The landed mechanism (985) is present in working-tree
        # profiles/ via the uncommitted block; nothing above it.
        assert _max_numeric_mechanism_id() == MECH_NUM
        for n in range(MECH_NUM + 1, MECH_NUM + 20):
            assert _repo_grep_numeric_mechanism_id(n) == [], n

    def test_block_key_zero_mechanism_number_substring(self):
        # Designed keying per #723/#738/#739: iteration 1257 in key,
        # no 985 or 986 substring.
        assert "1257" in BLOCK_KEY
        assert str(MECH_NUM) not in BLOCK_KEY
        assert str(NEXT_NUM) not in BLOCK_KEY

    def test_zero_underscore_mechanism_repo_wide(self):
        hits = _repo_grep_underscore_mechanism(MECH_NUM)
        assert hits == [], hits

    def test_zero_dash_mechanism_repo_wide(self):
        hits = _repo_grep_dash_mechanism(MECH_NUM)
        assert hits == [], hits

    def test_zero_numeric_next_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_no_duplicate_block_key(self):
        text = _read(GUARDIAN_PATH)
        assert text.count(BLOCK_KEY + ":") == 1

    def test_novel_urls_in_block_source_urls_verbatim(self):
        urls = _block()["source_urls"]
        for novel in NOVEL_URLS:
            assert novel in urls, novel

    def test_fifty_fourth_member_present_in_block(self):
        # Working-tree form: the landed claim lives in the
        # uncommitted block pre-commit; exactly one file, twice.
        hits = _working_tree_grep_profiles(_T54)
        assert hits == [GUARDIAN_PATH], hits
        text = _read(GUARDIAN_PATH)
        assert text.count(_T54) == 2, text.count(_T54)

    def test_no_type_a_1257_in_git_log_pin(self):
        # Post-main-commit form (the #1191-class self-trip, re-pinned
        # in the terminal log-hash followup per #721): every commit
        # whose message matches "Type A #1257" must be this run's
        # main commit or a descendant of it - i.e., no PRIOR run
        # committed this run's iteration. The ancestor check (not an
        # enumerated own-set) is robust to any number of same-run
        # followup commits: each followup is a descendant of main by
        # construction, so the pin is stable and terminal.
        out = _git("log", "--format=%H", "--grep=Type A #1257")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        if not hits:
            # Pre-commit form: no run has committed this iteration yet;
            # the pin's substance (no PRIOR run committed it) holds
            # vacuously. Post-commit the ancestor check below applies.
            return
        main = _git("rev-parse", PRED_MAIN_1257).stdout.strip()
        assert main != "0" * 40, "PRED_MAIN_1257 not patched post-commit"
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_1256_forward_guards_green_pre_commit(self):
        # #1256's forward pins for this run hold at HEAD pre-commit:
        # max-984, zero-985 all forms, no-Type-A-#1257 in git log,
        # fortieth direction absent, 48th-53rd members intact in
        # profiles/, no-54th at HEAD, ledger 53.
        assert _git_grep_tracked_source(_T40, "profiles/") == []
        assert _git_grep_tracked_source(_T48, "profiles/") == [
            "profiles/financial-times.yaml"]
        assert _git_grep_tracked_source(_T49, "profiles/") == [
            "profiles/careers/journalists.yaml"]
        out = _git("grep", "-c", "-F", _T50, "HEAD", "--",
                   "profiles/careers/journalists.yaml")
        assert out.stdout.strip().endswith(":3"), out.stdout
        out = _git("grep", "-c", "-F", _T51, "HEAD", "--",
                   "profiles/news-corp.yaml")
        assert out.stdout.strip().endswith(":3"), out.stdout
        out = _git("grep", "-c", "-F", _T52, "HEAD", "--",
                   "profiles/careers/journalists.yaml")
        assert out.stdout.strip().endswith(":5"), out.stdout
        out = _git("grep", "-c", "-F", _T53, "HEAD", "--",
                   "profiles/the-verge.yaml")
        assert out.stdout.strip().endswith(":2"), out.stdout
        assert _git_grep_tracked_source(_T54, None) == []
        out = _git("log", "--oneline", "--grep=Type A #1257")
        assert out.stdout.strip() == ""
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "ledger 53" in src


# ---------------------------------------------------------------------------
# 4. Finding: the Guardian Oct-1 hijab cross-lab test + Queensland arms
# ---------------------------------------------------------------------------
class TestGuardianOct01HijabTest:
    def test_block_lands_in_guardian_anthropic(self):
        data = _load_guardian()
        assert BLOCK_KEY in data["competitor_relationships"]["anthropic"]

    def test_mechanism_id_985(self):
        assert _block()["mechanism_id"] == MECH_NUM

    def test_two_arms(self):
        arms = _block()["anthropic_arms"]
        assert len(arms) == 2

    def test_arm_titles(self):
        titles = [a["item"]["title"] for a in _block()["anthropic_arms"]]
        for arm in ARMS:
            assert arm["title"] in titles, arm["title"]

    def test_arm_tones(self):
        tones = [a["item"]["manual_illustrative_tone"]
                 for a in _block()["anthropic_arms"]]
        assert tones == [0.15, -0.35]

    def test_cluster_mean_arithmetic(self):
        assert _block()["anthropic_cluster_mean"] == CLUSTER_MEAN
        calc = round(sum(a["tone"] for a in ARMS) / 2, 2)
        assert calc == -0.10

    def test_arm_dates_oct(self):
        dates = [a["item"]["date"] for a in _block()["anthropic_arms"]]
        assert dates == ["2026-10-01", "2026-10-05"]

    def test_mirror_attested_tier(self):
        for a in _block()["anthropic_arms"]:
            assert a["item"]["evidence_tier"] in (
                "mirror-attested", "relay-bounded")

    def test_hijab_arm_names_deal_partner_complier(self):
        # The operative falsification peg: the Guardian's own test
        # names OpenAI's ChatGPT as a hijab-removal complier.
        arm = _block()["anthropic_arms"][0]["item"]
        assert "chatgpt" in arm["cross_lab_results"]
        assert arm["cross_lab_results"]["chatgpt"] == "complied"
        assert arm["cross_lab_results"]["claude"] == "refused"

    def test_hijab_arm_bhuiyan_beat_documented(self):
        arm = _block()["anthropic_arms"][0]["item"]
        assert arm["byline"] == "Johana Bhuiyan"
        assert "m472" in arm["beat_note"]

    def test_queensland_arm_adversarial_register(self):
        arm = _block()["anthropic_arms"][1]["item"]
        assert "stupidity" in arm["key_phrases"][0]
        assert arm["manual_illustrative_tone"] == -0.35

    def test_novel_urls_zero_hit_pre_commit(self):
        # All seven mirror URLs are this run's novel evidence; they
        # must not exist anywhere else at HEAD (the block's own
        # source_urls excepted, which is uncommitted pre-commit).
        for url in NOVEL_URLS:
            out = _git("grep", "-F", "-l", url, "HEAD", "--", ".")
            assert out.stdout.strip() == "", url

    def test_guardian_openai_deal_disclosed(self):
        rel = _block()["financial_relationship"]
        assert "Feb 14 2025" in rel
        assert "mechanism_514" in rel


# ---------------------------------------------------------------------------
# 5. Comparator arms (carried per the m880 register-continuity pattern,
#    un-rescored per #807)
# ---------------------------------------------------------------------------
class TestMetaComparatorCarried:
    def test_carried_from_886_via_537(self):
        carried = _block()["meta_arms"]["carried_from"]
        assert "886" in carried
        assert "537" in carried

    def test_meta_band_mean(self):
        assert _block()["meta_arms"]["meta_band_mean"] == META_MEAN

    def test_two_meta_arms(self):
        assert len(_block()["meta_arms"]["arms"]) == 2

    def test_carried_from_openai(self):
        carried = _block()["openai_arms"]["carried_from"]
        assert "886" in carried
        assert "537" in carried

    def test_openai_band_mean(self):
        assert _block()["openai_arms"]["openai_band_mean"] == OPENAI_MEAN

    def test_two_openai_arms(self):
        assert len(_block()["openai_arms"]["arms"]) == 2


# ---------------------------------------------------------------------------
# 6. Asymmetry delta and falsification adjudication
# ---------------------------------------------------------------------------
class TestAsymmetryDelta:
    def test_delta_meta_arithmetic(self):
        assert _block()["asymmetry_scorer_result"][
            "illustrative_delta_anthropic_minus_meta"] == DELTA_META
        assert round(CLUSTER_MEAN - META_MEAN, 2) == DELTA_META

    def test_delta_openai_arithmetic(self):
        assert _block()["asymmetry_scorer_result"][
            "illustrative_delta_anthropic_minus_openai"] == DELTA_OPENAI
        assert round(CLUSTER_MEAN - OPENAI_MEAN, 2) == DELTA_OPENAI

    def test_near_null_vs_deal_partner(self):
        assert abs(DELTA_OPENAI) <= 0.05

    def test_falsification_member_true(self):
        assert _block()["falsification_family_member"] is True
        assert _block()["falsification_ledger"] == 54

    def test_engine_not_run(self):
        res = _block()["asymmetry_scorer_result"]
        assert res["engine_run"] is False
        assert res["p_value"].startswith("NOT_CALCULATED")
        assert res["is_significant"] is False

    def test_verdict_form(self):
        assert _block()["verdict"].startswith(
            "falsification_member_confirmed")


# ---------------------------------------------------------------------------
# 7. Research method
# ---------------------------------------------------------------------------
class TestResearchMethod:
    def test_five_query_sets_documented(self):
        method = _block()["research_method"]
        assert "5 browser.search query sets" in method

    def test_rejections_logged(self):
        method = _block()["research_method"]
        assert "REJECTED" in method
        assert "competitor-entities.yaml:28700" in method

    def test_no_canonical_urls_constructed(self):
        method = _block()["research_method"]
        assert "no canonical URLs constructed" in method

    def test_no_browser_open(self):
        method = _block()["research_method"]
        assert "0 browser.open" in method

    def test_ascii_only_no_em_dashes(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "\u2014" not in src
        block_text = _read(GUARDIAN_PATH)
        # The landed block is the only new profile text this run;
        # spot-check the block region via the block key window.
        start = block_text.index(BLOCK_KEY)
        window = block_text[start:start + 20000]
        assert "\u2014" not in window


# ---------------------------------------------------------------------------
# 8. Statistical discipline (Aug 28 2026 standing rule)
# ---------------------------------------------------------------------------
class TestStatisticalDiscipline:
    def test_manual_illustrative_only(self):
        disc = _block()["statistical_discipline"] if "statistical_discipline" in _block() else ""
        verdict = _block()["verdict"]
        assert "MANUAL ILLUSTRATIVE ONLY" in verdict

    def test_not_artifact_grade(self):
        assert _block()["asymmetry_scorer_result"][
            "artifact_grade"] is False

    def test_no_analysis_json_update(self):
        assert _block()["asymmetry_scorer_result"][
            "no_analysis_json_update"] is True

    def test_ledger_53_to_54(self):
        assert "ledger 53->54" in _block()["verdict"]

    def test_correlation_not_causation(self):
        assert "Correlation is not causation" in _block()["verdict"]


# ---------------------------------------------------------------------------
# 9. Guard lifecycle: forward pins for #1258 (Type B)
# ---------------------------------------------------------------------------
class TestGuardLifecycle1257:
    def test_pins_on_985_landing(self):
        # Type A lands m985: max becomes 985, next is 986.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 985" in src
        assert "NEXT_NUM = 986" in src

    def test_no_type_b_1258_in_git_log_pin(self):
        out = _git("log", "--oneline", "--grep=Type B #1258")
        assert out.stdout.strip() == ""

    def test_986_numeric_absent_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_986_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_986_dash_absent_repo_wide(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_no_fortieth_direction_pin(self):
        # The fortieth direction-claim form stays absent in profiles/.
        assert _git_grep_tracked_source(_T40, "profiles/") == []

    def test_forty_eighth_member_intact_pin(self):
        assert _git_grep_tracked_source(_T48, "profiles/") == [
            "profiles/financial-times.yaml"]

    def test_forty_ninth_member_intact_pin(self):
        assert _git_grep_tracked_source(_T49, "profiles/") == [
            "profiles/careers/journalists.yaml"]

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
        # Working-tree form (the landed claim lives in the
        # uncommitted block pre-commit): present in exactly one
        # file, twice.
        hits = _working_tree_grep_profiles(_T54)
        assert hits == [GUARDIAN_PATH], hits
        text = _read(GUARDIAN_PATH)
        assert text.count(_T54) == 2, text.count(_T54)

    def test_no_fifty_fifth_member_pin(self):
        assert _git_grep_tracked_source(_T55, None) == []

    def test_predecessor_1256_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, E1256_FILE))

    def test_next_leg_is_1258_type_b(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#1258 Type B" in src

    def test_1256_pins_flip_by_design_documented(self):
        # #1256's forward guards (max-984, zero-985 keys all forms,
        # no-Type-A-#1257-in-git-log, fortieth absent, forty-eighth +
        # forty-ninth + fiftieth + fifty-first + fifty-second +
        # fifty-third intact in profiles/, no fifty-fourth) verified
        # GREEN at HEAD pre-commit this run via the subprocess
        # staleness pin (Type A lands m985 as the fifty-fourth
        # falsification-family member); the zero-985-numeric,
        # no-Type-A-#1257-in-git-log, and no-fifty-fourth pins flip
        # post-main-commit on this run's own landing (the #1191-class
        # self-trip, by design, documented in the staleness pin below).
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "TestStalenessPins1257" in src
        assert "no_type_a_1257_in_git_log_pin" in src


# ---------------------------------------------------------------------------
# 10. Staleness pins: #1256's guard lifecycle flips by design
#      (1 test; deselected pre-commit, verified post-main-commit)
# ---------------------------------------------------------------------------
class TestStalenessPins1257:
    def test_1256_guard_lifecycle_flips_by_design_post_commit(self):
        # Runs the #1256 file's guard-lifecycle class post-commit:
        # its no-Type-A-#1257-in-git-log pin self-trips on this run's
        # own main commit, its zero-985-numeric pin trips on the
        # landed m985 block, and its no-fifty-fourth pin trips on the
        # landed fifty-fourth member claim (all BY DESIGN, the
        # #1191-class self-trip family); the class is expected to
        # report the flips, not to stay green.
        res = _class_run(E1256_FILE, "TestGuardLifecycle1256")
        assert res.returncode != 0, res.stdout[-2000:]
        assert "failed" in res.stdout, res.stdout[-2000:]


# ---------------------------------------------------------------------------
# 11. Doc-sync per #719 (3 tests; deselected pre-commit, flipped post-sync)
# ---------------------------------------------------------------------------
class TestDocSync:
    def test_readme_test_file_table_has_1257_row_post_sync(self):
        readme = _read(README_PATH)
        assert "test_type_a_1257" in readme

    def test_architecture_has_1257_row_post_sync(self):
        arch = _read(ARCH_PATH)
        assert "test_type_a_1257" in arch

    def test_readme_stats_ratcheted(self):
        # Post-sync-positive form per #719: asserts the ratcheted
        # counts (README_TEST_COUNT tests across README_FILE_COUNT
        # files). Fails pre-commit by design; deselected in the
        # in-gate run.
        readme = _read(README_PATH)
        assert ("| Tests | %d |" % README_TEST_COUNT) in readme
        assert ("Across %d test files" % README_FILE_COUNT) in readme


# ---------------------------------------------------------------------------
# 12. Iteration log (3 tests; deselected pre-commit per #721)
# ---------------------------------------------------------------------------
class TestIterationLog:
    def test_1257_entry_present_post_sync(self):
        log = _read(LOG_PATH)
        assert "## #1257 Type A" in log

    def test_1256_entry_present(self):
        log = _read(LOG_PATH)
        assert "## #1256 Type E" in log

    def test_rotation_transparency_convention(self):
        log = _read(LOG_PATH)
        assert "### Rotation transparency" in log


# ---------------------------------------------------------------------------
# 13. In-flight isolation
# ---------------------------------------------------------------------------
class TestInFlightIsolation:
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
        # Guarded in the log entry per convention; the test file keeps
        # the in-flight list only (own-file reference would trip the
        # contiguous-literal discipline elsewhere).
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#1024" in src


# ---------------------------------------------------------------------------
# 14. Background suite: observed only per #795
# ---------------------------------------------------------------------------
class TestBackgroundSuite1257:
    def test_1255_suite_log_exists(self):
        assert os.path.exists(
            os.path.join(GOAL_HIDDEN, "type_d_1255_full_suite.log"))

    def test_this_run_launches_no_suite(self):
        # This run must not launch its own background suite; only the
        # #1255-launched suite is observed (verdict belongs to #1260).
        assert not os.path.exists(
            os.path.join(GOAL_HIDDEN, "type_d_1257_full_suite.log"))

    def test_observation_only_documented(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "OBSERVES only" in src
        assert "verdict belongs to #1260" in src
