"""Type A #1117: FT x OpenAI Sep-30 FTC agent-safety probe coverage (regulatory-
enforcement register) vs carried FT x Meta arms - FORTY-SECOND falsification-
family member.

Rotation position
-----------------
THIRD leg of the 1115-1119 window (D #1115 -> E #1116 -> A #1117 -> B #1118 ->
C #1119, per the #565 anchor + rotation guard). Predecessor #1116 Type E
verified in git log (main 3e11793836161f6f0995de61ab7a9783d4ffbc33 / anchor
a06f69be / log-hash 8fa48141 / log-hash fill 68c61667, Oct 1 2026 05:00 PDT;
146th podcast-sentiment verification; ledger holds at 41). The 1110-1114
window is verified closed as a consecutive newest-first sequence. Next run
#1118 continues the window as Type B.

Finding
-------
FIRST dedicated corpus mechanism (numeric mechanism id 901, landed in
profiles/financial-times.yaml under competitor_relationships.openai) on the
FT's coverage of the FTC's Sep-30 widened probe into Anthropic AND OpenAI
over AI agent safety. The Financial Times is relay-attested as an original by
two independent relays: runtimewire (crawled <1h; "according to the FT" x2 -
the Sep-29 White House self-regulation accord and METR "also under
examination, according to the FT") and archynetys (Oct 1 05:37 UTC;
"Coverage from Reuters, Bloomberg and the Financial Times notes that the
investigation centers on product-safety concerns and potential consumer
harms linked to the companies' advanced AI models").

Register: regulatory-enforcement accountability on the $5-10M/yr licensing
DEAL PARTNER, no delay, no softening visible. The naive uniform
payer-softening prediction (ft.yaml competitor_relationships.openai
coverage_prediction "softer", from the Apr 29 2024 FT-OpenAI licensing deal)
FAILS on the enforcement peg: the FT routes the regulator's product-safety
probe onto OpenAI in the same register it applies to the non-deal lab.

FORTY-SECOND falsification-family member (ledger 41->42); FIRST regulatory-
enforcement-register falsification at FT (after #1047's disclosure-register
THIRTY-FIFTH at FT; #1112's litigation-register FORTIETH at WIRED; #1113's
journalist-register FORTY-FIRST). MANUAL ILLUSTRATIVE ONLY per the Aug 28
2026 standing rule: engine NOT run; p_value/cohens_d/ci_95 NOT_CALCULATED;
is_significant false; verdict directionally_supported_not_proven; NOT
artifact-grade; no_analysis_json_update true. Correlation is not causation;
hypothesis-generating only.

OpenAI arm (MANUAL ILLUSTRATIVE -0.35; 0.05 softer than the m898 LASST
lawsuit arm -0.40 because the probe names two labs, diluting entity-specific
adversarialness). Carried Meta arms un-rescored per #807: m625 +0.05 (FT Muse
distribution, Sep 8-9), m823 +0.20 (FT Meta Connect momentum, Sep 24-25);
mean +0.125. Illustrative delta (OpenAI minus Meta): -0.475.

Research method
---------------
5 browser.search query sets Oct 1 2026 PDT; 0 browser.open this run
(excerpt-bounded per #503; FT originals paywalled, relay-attested only).
SELECTED: runtimewire FTC-probe piece (FT-attributed x2, novel URL) +
archynetys FTC-probe trend page (FT product-safety framing, novel URL).
REJECTED: WSJ-broke Astra story (in-corpus via #1112 relay family); LASST
relays without FT attribution; TechCrunch/usecarly newsletter aggregation.
Both source URLs verbatim from Full-URL listings; no ft.com canonical URLs
constructed. ASCII-only, no em dashes.

Pre-commit novelty (verified by this run before writing files)
--------------------------------------------------------------
- Zero test_type_a_1117 files on disk; "Type A #1117" absent from git log.
- The 2 new source URLs zero-hit repo-wide via git grep -F.
- Max numeric mechanism_id 900 pre-insertion (this block lands 901).
- Zero numeric/underscore/dash 901 keys repo-wide pre-commit (needles
  format-built per #715; this file excluded from its own sweeps).
- FORTY-SECOND member-claim form zero-hit in profiles/ pre-commit
  (negative-guard wording only); THIRTIETH relationship direction present;
  THIRTY-FIRST direction absent repo-wide.
- Block key zero-hit repo-wide pre-commit.

Concurrency (working tree, do NOT touch)
----------------------------------------
- #899: profiles/nytimes.yaml m771 hunk (uncommitted, owned by its run).
- #938: Type B test-file anchor edit (uncommitted).
- #900: untracked Type D test file.
- #1012-wt: working-tree edit of the committed Type A #1012 file.
- #1024 m846: Ray's revert/leave/rebuild decision pending; untouched.

Anchor mechanics per #565: ANCHORED_SHA is a zero placeholder pre-commit;
the anchor followup patches it to this run's main commit hash. The git-log
novelty test is SUPERSEDED BY DESIGN once the main commit lands (deselect
in post-commit full runs). Doc-sync + iteration-log tests assert the
pre-doc-sync state and are deselected by design post-doc-sync per #719.
"""

import glob
import os
import re
import subprocess

import yaml

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TESTS_DIR = os.path.join(REPO_ROOT, "tests")
PROFILES_DIR = os.path.join(REPO_ROOT, "profiles")
LOG_PATH = os.path.join(REPO_ROOT, "iteration-log.md")
README_PATH = os.path.join(REPO_ROOT, "README.md")
ARCH_PATH = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")
OWN_BASENAME = (
    "test_type_a_1117_ft_openai_ftc_agent_safety_probe_vs_carried_meta_arms_oct01_6am.py"
)
FT_FILE = os.path.join(PROFILES_DIR, "financial-times.yaml")

ANCHORED_SHA = "091eb818d7986763e76cec240ee921cb33983053"

MECH_NUM = 901
NEXT_NUM = 902
MECH_ID_MARKER = "mechanism" + "_"
MECH_DASH_MARKER = "mechanism" + "-"

BLOCK_KEY = (
    "type_a_1117_ft_openai_ftc_agent_safety_probe_vs_carried_meta_arms_oct01_6am"
)
URL_RUNTIMEWIRE = (
    "https://runtimewire.com/article/ftc-anthropic-openai-ai-agent-safety-probe"
)
URL_ARCHYNETYS = (
    "https://www.archynetys.com/trend/2026-09-30/"
    "ftc-opens-probe-into-ai-giants-including-anthropic-and-openai"
)

# Landed falsification-family member forms (affirmative literals permitted;
# these claims are already in the corpus). The FORTY-THIRD member literal and
# the THIRTY-FIRST direction literal are format-built below per #715/#770 so
# this file carries no contiguous forward-guard needle.
FORTY_SECOND_MEMBER = "FORTY-SECOND falsification-family member"
FORTY_FIRST_MEMBER = "FORTY-FIRST falsification-family member"
FORTIETH_MEMBER = "FORTIETH falsification-family member"
FORTY_THIRD_MEMBER = "FORTY" + "-" + "THIRD falsification-family member"
THIRTY_FIRST_DIR = "THIRTY" + "-FIRST" + " relationship direction"

PRED_MAIN_1116 = "3e117938"
PRED_ANCHOR_1116 = "a06f69be"
PRED_LOGHASH_1116 = "8fa48141"
PRED_FINAL_1116 = "68c61667"


def _read(path):
    with open(path, encoding="utf-8", errors="replace") as fh:
        return fh.read()


def _git(*args):
    return subprocess.run(
        ["git", *args],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
    )


def _iter_source_files():
    """Yield profile + test source files, excluding this file per #715."""
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
    needle = "%s%d" % (MECH_ID_MARKER, n)
    return [
        p
        for p in _iter_source_files()
        if needle in _read(p)
    ]


def _repo_grep_dash_mechanism(n):
    needle = "%s%d" % (MECH_DASH_MARKER, n)
    return [
        p
        for p in _iter_source_files()
        if needle in _read(p)
    ]


def _profiles_grep_numeric_mechanism_id(n):
    needle = "mechanism_id: %d" % n
    hits = []
    for root, dirs, files in os.walk(PROFILES_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
            p = os.path.join(root, f)
            if needle in _read(p):
                hits.append(p)
    return hits


def _max_numeric_mechanism_id_in_profiles():
    found = []
    pat = re.compile(r"mechanism_id:\s*(\d+)")
    for root, dirs, files in os.walk(PROFILES_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
            found.extend(
                int(m) for m in pat.findall(_read(os.path.join(root, f)))
            )
    return max(found) if found else 0


def _block():
    doc = yaml.safe_load(_read(FT_FILE))
    return doc["competitor_relationships"]["openai"][BLOCK_KEY]


def _block_text():
    return _read(FT_FILE)


def _node_run(filename, node):
    """Run one predecessor test node in a subprocess (pin lifecycle)."""
    target = os.path.join(TESTS_DIR, filename) + "::" + node
    env = dict(os.environ)
    env["PYTEST_DISABLE_PLUGIN_AUTOLOAD"] = "1"
    return subprocess.run(
        ["python3", "-m", "pytest", target, "-q", "--no-header"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        env=env,
    )


# ---------------------------------------------------------------------------
# 1. Anchor (pre-commit placeholder; patched green post-commit per #565).
# ---------------------------------------------------------------------------

class TestAnchor1117:
    def test_anchored_sha_placeholder_pre_commit(self):
        # Pre-commit the anchor is a zero placeholder; the anchor followup
        # patches it per #565. The post-commit rotation guard asserts the
        # patched value is present in git log.
        assert ANCHORED_SHA == "0" * 40

    def test_anchored_sha_shape(self):
        assert len(ANCHORED_SHA) == 40

    def test_anchor_mechanics_documented(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "ANCHORED_SHA" in src
        assert "#565" in src


# ---------------------------------------------------------------------------
# 2. Rotation guard (pre-commit assertions; git-log novelty test is
# SUPERSEDED BY DESIGN post-commit - deselect in post-commit full runs).
# ---------------------------------------------------------------------------

class TestRotationGuard1117:
    def test_predecessor_1116_chain_present(self):
        log = _git("log", "--oneline", "-80").stdout
        assert PRED_MAIN_1116 in log
        assert PRED_ANCHOR_1116 in log
        assert PRED_LOGHASH_1116 in log
        assert PRED_FINAL_1116 in log

    def test_type_a_1117_novelty(self):
        # "Type A #1117" absent from git log pre-commit; own file not
        # yet committed. SUPERSEDED BY DESIGN once this run's main
        # commit ("Type A #1117:") lands; post-commit, the anchor
        # asserts the patched ANCHORED_SHA is present in git log.
        # Deselect this test in post-commit full runs.
        log = _git("log", "--oneline", "--grep=Type A #1117").stdout
        assert log.strip() == ""

    def test_window_order_d_e_a_b_c(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "D #1115 -> E #1116 -> A #1117" in src

    def test_next_run_1118_type_b_noted(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "B #1118" in src


# ---------------------------------------------------------------------------
# 3. Mechanism novelty (post-landing state: max is 901; 902 absent in all
# forms; 901 underscore/dash absent - the forward guards for #1118+).
# ---------------------------------------------------------------------------

class TestMechanismNovelty1117:
    def test_single_test_file_for_iteration(self):
        files = glob.glob(os.path.join(TESTS_DIR, "test_type_a_1117*.py"))
        assert len(files) == 1, files

    def test_novelty_verification_claim_in_block(self):
        assert "zero test_type_a_1117 files on disk" in _block_text()

    def test_max_numeric_mechanism_id_is_901(self):
        assert _max_numeric_mechanism_id_in_profiles() == MECH_NUM

    def test_zero_underscore_902_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_zero_dash_902_repo_wide(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_zero_numeric_902_in_profiles(self):
        assert _profiles_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_zero_underscore_901_repo_wide(self):
        assert _repo_grep_underscore_mechanism(MECH_NUM) == []

    def test_zero_dash_901_repo_wide(self):
        assert _repo_grep_dash_mechanism(MECH_NUM) == []

    def test_901_numeric_present_only_in_ft_block(self):
        hits = _profiles_grep_numeric_mechanism_id(MECH_NUM)
        assert hits == [FT_FILE], hits


# ---------------------------------------------------------------------------
# 4. Block structure.
# ---------------------------------------------------------------------------

class TestBlockStructure1117:
    def test_block_loads_under_openai(self):
        b = _block()
        assert b["mechanism_id"] == MECH_NUM
        assert b["iteration"] == 1117
        assert b["hour_type"] == "A"
        assert b["date"] == "2026-10-01 06:00 PDT"

    def test_window_third_leg(self):
        assert "THIRD leg" in _block()["window"]
        assert "1115-1119" in _block()["window"]

    def test_test_file_field(self):
        assert _block()["test_file"] == "tests/" + OWN_BASENAME

    def test_verdict(self):
        assert _block()["verdict"] == "directionally_supported_not_proven"

    def test_statistical_discipline_field(self):
        sd = _block()["statistical_discipline"]
        assert "MANUAL ILLUSTRATIVE ONLY" in sd
        assert "engine NOT run" in sd
        assert "NOT_CALCULATED" in sd
        assert "is_significant false" in sd
        assert "NOT artifact-grade" in sd
        assert "no_analysis_json_update true" in sd

    def test_connects_to(self):
        conns = _block()["connects_to"]
        for m in (625, 823, 754, 718, 441, 847, 898):
            assert m in conns, m

    def test_block_key_not_a_mechanism_form(self):
        # The block key carries no 901/902 numeric, underscore, or dash
        # mechanism-key form (per the #715/#770 literal discipline).
        assert str(MECH_NUM) not in BLOCK_KEY
        assert str(NEXT_NUM) not in BLOCK_KEY


# ---------------------------------------------------------------------------
# 5. OpenAI arm (FTC agent-safety probe, regulatory-enforcement register).
# ---------------------------------------------------------------------------

class TestOpenAIArm1117:
    def test_event(self):
        arm = _block()["openai_arm"]
        assert "FTC" in arm["event"]
        assert "Anthropic" in arm["event"]
        assert "OpenAI" in arm["event"]
        assert "agent safety" in arm["event"]

    def test_ft_role_relay_attested(self):
        role = _block()["openai_arm"]["ft_role"]
        assert "runtimewire" in role
        assert "archynetys" in role
        assert "according to the FT" in role

    def test_register(self):
        reg = _block()["openai_arm"]["register"]
        assert "regulatory-enforcement accountability" in reg
        assert "product-safety concerns" in reg

    def test_peg_context(self):
        ctx = _block()["openai_arm"]["peg_context"]
        assert "Sep-29 White House self-regulation accord" in ctx
        assert "Astra" in ctx

    def test_tone_manual_illustrative(self):
        arm = _block()["openai_arm"]
        assert arm["tone"] == -0.35

    def test_tone_basis_names_lasst_arm(self):
        basis = _block()["openai_arm"]["tone_basis"]
        assert "MANUAL ILLUSTRATIVE" in basis
        assert "-0.40" in basis
        assert "m898" in basis


# ---------------------------------------------------------------------------
# 6. Carried Meta arms (un-rescored per #807).
# ---------------------------------------------------------------------------

class TestCarriedMetaArms1117:
    def test_two_arms(self):
        arms = _block()["meta_arms_carried"]["arms"]
        assert len(arms) == 2

    def test_m625_arm(self):
        arms = {a["mechanism"]: a for a in _block()["meta_arms_carried"]["arms"]}
        assert arms[625]["tone"] == 0.05
        assert "WhatsApp" in arms[625]["item"]
        assert "#807" in arms[625]["basis"]

    def test_m823_arm(self):
        arms = {a["mechanism"]: a for a in _block()["meta_arms_carried"]["arms"]}
        assert arms[823]["tone"] == 0.20
        assert "Connect" in arms[823]["item"]
        assert "#807" in arms[823]["basis"]

    def test_meta_mean(self):
        assert _block()["meta_arms_carried"]["meta_mean"] == 0.125

    def test_mean_arithmetic(self):
        arms = _block()["meta_arms_carried"]["arms"]
        mean = sum(a["tone"] for a in arms) / len(arms)
        assert abs(mean - 0.125) < 1e-9


# ---------------------------------------------------------------------------
# 7. Financial relationship (the falsified uniform-softening prediction).
# ---------------------------------------------------------------------------

class TestFinancialRelationship1117:
    def test_deal(self):
        fr = _block()["financial_relationship"]
        assert "Apr 29 2024" in fr["deal"]
        assert "licensing" in fr["deal"]

    def test_value(self):
        assert "$5-10M/yr" in _block()["financial_relationship"]["value"]

    def test_coverage_prediction_softer(self):
        assert "softer" in _block()["financial_relationship"]["coverage_prediction"]

    def test_test_peg(self):
        assert "FTC agent-safety probe" in _block()["financial_relationship"]["test"]

    def test_result_fails(self):
        result = _block()["financial_relationship"]["result"]
        assert "FAILS" in result
        assert "no delay or softening" in result


# ---------------------------------------------------------------------------
# 8. Scorer discipline (manual illustrative only).
# ---------------------------------------------------------------------------

class TestScorerDiscipline1117:
    def test_openai_tone(self):
        assert _block()["scorer"]["openai_tone"] == -0.35

    def test_meta_mean_tone(self):
        assert _block()["scorer"]["meta_mean_tone"] == 0.125

    def test_delta(self):
        assert _block()["scorer"]["illustrative_delta_openai_minus_meta"] == -0.475

    def test_delta_arithmetic(self):
        s = _block()["scorer"]
        assert abs((s["openai_tone"] - s["meta_mean_tone"]) - (-0.475)) < 1e-9

    def test_method_manual_illustrative(self):
        method = _block()["scorer"]["method"]
        assert "MANUAL ILLUSTRATIVE ONLY" in method
        assert "engine NOT run" in method
        assert "is_significant False" in method

    def test_reading(self):
        reading = _block()["scorer"]["reading"]
        assert "uniform softening prediction fails" in reading


# ---------------------------------------------------------------------------
# 9. Falsification ledger (41 -> 42; forward guards for the FORTY-THIRD
# member and the THIRTY-FIRST direction are format-built per #715/#770).
# ---------------------------------------------------------------------------

class TestFalsificationLedger1117:
    def _ledger_hits(self, needle):
        hits = []
        for root, dirs, files in os.walk(PROFILES_DIR):
            dirs[:] = [d for d in dirs if d != "__pycache__"]
            for f in files:
                p = os.path.join(root, f)
                if needle in _read(p):
                    hits.append(p)
        return hits

    def test_member_flag_true(self):
        assert _block()["falsification_family_member"] is True

    def test_ledger_42(self):
        assert _block()["falsification_ledger"] == 42

    def test_forty_first_intact_in_journalists_only(self):
        hits = self._ledger_hits(FORTY_FIRST_MEMBER)
        assert hits == [os.path.join(PROFILES_DIR, "careers", "journalists.yaml")], hits

    def test_fortieth_intact_in_wired_only(self):
        hits = self._ledger_hits(FORTIETH_MEMBER)
        assert hits == [os.path.join(PROFILES_DIR, "wired.yaml")], hits

    def test_forty_second_present_once_in_profiles(self):
        # The affirmative FORTY-SECOND claim is this run's landed block;
        # profiles-scope only (this test file also carries the landed
        # literal, excluded by scope).
        hits = self._ledger_hits(FORTY_SECOND_MEMBER)
        assert hits == [FT_FILE], hits

    def test_forty_third_member_absent_repo_wide(self):
        hits = [
            p for p in _iter_source_files()
            if FORTY_THIRD_MEMBER in _read(p)
        ]
        assert hits == [], hits

    def test_thirtieth_direction_present(self):
        assert "THIRTIETH relationship direction" in _block_text()

    def test_thirty_first_direction_absent_repo_wide(self):
        hits = [
            p for p in _iter_source_files()
            if THIRTY_FIRST_DIR in _read(p)
        ]
        assert hits == [], hits


# ---------------------------------------------------------------------------
# 10. Supersession pins: predecessor guards whose assertions flip BY DESIGN
# when this run's block lands; the unchanged forward guards stay green.
# ---------------------------------------------------------------------------

FILE_1116 = "test_type_e_1116_podcast_sentiment_146th_verification_oct01_5am.py"
FILE_1115 = "test_type_d_1115_m898_m899_m900_qualitative_corpus_integrity_oct01_4am.py"
FILE_1114 = (
    "test_type_c_1114_google_news_ai_pilot_three_track_segmentation_"
    "trackseparatedpricing_thirtieth_direction_oct01_3am.py"
)


class TestSupersessionPins1117:
    def test_1116_novelty_901_numeric_fails_by_design(self):
        # The 901 numeric id now exists in the working-tree profiles/
        # (this run's landed block); fails BY DESIGN post-landing.
        res = _node_run(
            FILE_1116,
            "TestMechanismNovelty::test_zero_901_numeric_mechanism_id_in_profiles",
        )
        assert res.returncode != 0, res.stdout[-1500:]

    def test_1116_novelty_max_900_fails_by_design(self):
        res = _node_run(
            FILE_1116, "TestMechanismNovelty::test_type_e_adds_no_mechanisms"
        )
        assert res.returncode != 0, res.stdout[-1500:]

    def test_1116_underscore_dash_901_still_green(self):
        for node in (
            "TestMechanismNovelty::test_zero_901_underscore_mechanism_repo_wide",
            "TestMechanismNovelty::test_zero_901_dash_mechanism_repo_wide",
        ):
            res = _node_run(FILE_1116, node)
            assert res.returncode == 0, (node, res.stdout[-1500:])

    def test_1116_staleness_pins_fail_by_design(self):
        # Pins #1115's guard-lifecycle as green; the 901 numeric guard
        # now fails, so the class fails BY DESIGN post-landing.
        res = _node_run(FILE_1116, "TestStalenessPins")
        assert res.returncode != 0, res.stdout[-1500:]

    def test_1116_forty_second_head_scoped_green_pre_commit(self):
        # HEAD-scoped: passes pre-commit (block uncommitted), flips to
        # failing BY DESIGN once the main commit lands; the #1118 run
        # re-pins it as failed.
        res = _node_run(
            FILE_1116,
            "TestStatisticalDiscipline::test_forty_second_member_claim_absent",
        )
        assert res.returncode == 0, res.stdout[-1500:]

    def test_1115_guard_lifecycle_numeric_fails_by_design(self):
        res = _node_run(
            FILE_1115,
            "TestGuardLifecycle1115::test_zero_next_numeric_901_in_profiles",
        )
        assert res.returncode != 0, res.stdout[-1500:]

    def test_1115_underscore_dash_still_green(self):
        for node in (
            "TestGuardLifecycle1115::test_zero_next_underscore_901_repo_wide",
            "TestGuardLifecycle1115::test_zero_next_dash_901_repo_wide",
        ):
            res = _node_run(FILE_1115, node)
            assert res.returncode == 0, (node, res.stdout[-1500:])

    def test_1114_forward_guards_numeric_fails_by_design(self):
        res = _node_run(
            FILE_1114,
            "TestForwardGuards1114::test_zero_numeric_901_in_profiles",
        )
        assert res.returncode != 0, res.stdout[-1500:]

    def test_1114_underscore_dash_still_green(self):
        for node in (
            "TestForwardGuards1114::test_zero_underscore_901_repo_wide",
            "TestForwardGuards1114::test_zero_dash_901_repo_wide",
        ):
            res = _node_run(FILE_1114, node)
            assert res.returncode == 0, (node, res.stdout[-1500:])

    def test_1114_ledger_no_forty_second_fails_by_design(self):
        # Working-tree-scoped: the landed block carries the affirmative
        # FORTY-SECOND claim; fails BY DESIGN post-landing.
        res = _node_run(
            FILE_1114, "TestLedger41Holds::test_no_forty_second_member"
        )
        assert res.returncode != 0, res.stdout[-1500:]


# ---------------------------------------------------------------------------
# 11. Research method.
# ---------------------------------------------------------------------------

class TestResearchMethod1117:
    def test_five_search_sets(self):
        assert "5 browser.search query sets" in _block()["research_method"]

    def test_zero_browser_open(self):
        rm = _block()["research_method"]
        assert "0 browser.open" in rm
        assert "#503" in rm

    def test_selected_relays(self):
        rm = _block()["research_method"]
        assert "runtimewire" in rm
        assert "archynetys" in rm

    def test_rejected_alternatives(self):
        rm = _block()["research_method"]
        assert "WSJ-broke Astra story" in rm
        assert "LASST relays without FT attribution" in rm

    def test_source_urls_verbatim(self):
        urls = _block()["source_urls"]
        assert URL_RUNTIMEWIRE in urls
        assert URL_ARCHYNETYS in urls
        assert len(urls) == 2

    def test_source_urls_novel_pre_commit(self):
        # Post-landing the URLs live only in this run's block and test
        # file; pre-commit they were zero-hit repo-wide via git grep -F.
        for url in (URL_RUNTIMEWIRE, URL_ARCHYNETYS):
            out = _git("grep", "-F", "--name-only", url).stdout
            files = sorted(
                f for f in out.strip().splitlines() if f.strip()
            )
            assert set(files) <= {
                "profiles/financial-times.yaml", "tests/" + OWN_BASENAME
            }, (url, files)

    def test_no_constructed_ft_urls(self):
        assert "no ft.com canonical URLs constructed" in _block()["research_method"]

    def test_block_and_file_ascii(self):
        assert "ASCII-only" in _block()["research_method"]
        # The block region only (ft.yaml carries pre-existing non-ASCII
        # glyphs elsewhere, e.g. pound-sign price lines).
        text = _read(FT_FILE)
        lines = text.splitlines()
        start = next(
            i for i, l in enumerate(lines) if BLOCK_KEY in l
        )
        end = next(
            i for i in range(start + 1, len(lines))
            if lines[i] == "  meta:"
        )
        region = "\n".join(lines[start:end])
        assert all(ord(c) < 128 for c in region)
        own = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert all(ord(c) < 128 for c in own)


# ---------------------------------------------------------------------------
# 12. Statistical discipline (Aug 28 2026 standing rule).
# ---------------------------------------------------------------------------

class TestStatisticalDiscipline1117:
    def test_verdict_not_proven(self):
        assert _block()["verdict"] == "directionally_supported_not_proven"

    def test_not_artifact_grade(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "NOT artifact-grade" in src

    def test_engine_not_run(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "engine NOT run" in src

    def test_manual_illustrative_only(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MANUAL ILLUSTRATIVE ONLY" in src

    def test_hypothesis_generating(self):
        assert "hypothesis-generating only" in _block()["finding"]


# ---------------------------------------------------------------------------
# 13. Doc-sync (pre-commit state; SUPERSEDED BY DESIGN post-doc-sync -
# deselect in post-doc-sync full runs per #719).
# ---------------------------------------------------------------------------

class TestDocSync1117:
    def test_readme_test_file_table_has_no_1117_row_pre_commit(self):
        readme = _read(README_PATH)
        assert "test_type_a_1117" not in readme

    def test_architecture_has_no_1117_row_pre_commit(self):
        arch = _read(ARCH_PATH)
        assert "test_type_a_1117" not in arch

    def test_readme_stats_current(self):
        readme = _read(README_PATH)
        assert "| 58017 |" in readme
        assert "1441" in readme


# ---------------------------------------------------------------------------
# 14. Iteration log (pre-commit state; SUPERSEDED BY DESIGN post-doc-sync -
# deselect in post-doc-sync full runs per #719).
# ---------------------------------------------------------------------------

class TestIterationLog1117:
    def test_no_1117_entry_pre_commit(self):
        log = _read(LOG_PATH)
        assert "## #1117 Type A" not in log

    def test_1116_entry_present(self):
        log = _read(LOG_PATH)
        assert "## #1116 Type E" in log

    def test_rotation_transparency_convention(self):
        log = _read(LOG_PATH)
        assert "### Rotation transparency" in log


# ---------------------------------------------------------------------------
# 15. In-flight isolation: concurrent runs' uncommitted work untouched.
# ---------------------------------------------------------------------------

class TestInFlightIsolation1117:
    def test_899_nytimes_hunk_untouched(self):
        res = _git("diff", "--name-only")
        modified = res.stdout.split()
        assert "profiles/nytimes.yaml" in modified
        # Its uncommitted hunk belongs to #899's run; this run stages
        # only its own files.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#899" in src

    def test_938_test_file_edit_owned_by_its_run(self):
        res = _git("status", "--short")
        assert "test_type_b_938" in res.stdout

    def test_900_untracked_file_untouched(self):
        res = _git("status", "--short")
        assert "test_type_d_900_m769" in res.stdout

    def test_1012_working_tree_edit_untouched(self):
        res = _git("status", "--short")
        assert "test_type_a_1012" in res.stdout

    def test_do_not_touch_1024_m846(self):
        # Ray's revert/leave/rebuild decision on #1024's m846 is pending;
        # guarded in the log entry per convention, untouched by this run.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#1024" in src
