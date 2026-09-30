"""Type C #1099: Google AI-contribution pilot rate disclosure (The Information Sep 29 2026, relayed Sep 30) -
UNILATERAL PRICING as the TWENTY-SEVENTH relationship direction (mechanism 891 in profiles/competitor-entities.yaml).

Run summary: FIFTH and CLOSING leg of the 1095-1099 window (D #1095 -> E #1096 -> A #1097 -> B #1098 -> C #1099 per #565).
Research: 3 browser.search sets (The Information publisher-payment story; AI earnings Search Console widget;
rate-quantum corroboration) + 1 browser.open first-hand (PYMNTS Sep 30 relay, 46 lines) per #503. Five relay URLs,
all zero-hit repo-wide pre-commit: pymnts google-begins-paying-publishers-for-ai-overview-answers;
anythingengineoptimization SERT wire; aiweekly googles-ai-overviews-pilot-pays-100-publishers-one-over-1m;
thedesk google-paying-news-publishers-ai-search-results; techstartups top-tech-news-today-september-30-2026.
Finding: Google is PAYING around 100 publishers for content driving AI Overviews/AI Mode/Gemini answers - the first
disclosed payment rate for the pilot that m702 (Digiday, ~Sep 14) and m708 (Bloomberg Law, Jul 2026) documented without
rates: under $1,000 over several months (tail) to over $1M/yr (one early entrant); under 0.1% of ad revenue for
small-to-midsize participants; Google "determines for itself what that content is worth" (participating publisher
executive via The Information/PYMNTS); opting out of the payment does not stop Google using the content (AI Weekly).
UNILATERAL PRICING is the twenty-seventh relationship direction per the m807 enumeration: payer-set micro-compensation
decoupled from consent (distinct from #2 pay-or-litigate m636, #12 regulatory-bargaining m1004, #15 ecosystem-grant
m1029, and the pay-per-use template m156/m443/m702). Falsifiable via: large publishers joining at current rates;
Google disclosing or negotiating the pricing formula; opt-out-of-payment ever gating use. Carries the m737
taxonomy-count tension note. NOT a falsification-family member; ledger holds at 37, THIRTY-EIGHTH member-claim form
absent repo-wide.
Statistical discipline per the Aug 28 2026 standing rule: tone NOT_SCORED, engine NOT run, p_value/cohens_d
NOT_CALCULATED, is_significant False, verdict directionally_supported_not_proven, no_analysis_json_update True,
artifact NOT artifact-grade.
Anchor: ANCHORED_SHA patched to the Type C #1099 main-commit SHA by the anchor followup per #565 ("0"*40 placeholder
pre-commit).
Rotation guard: #1095 Type D main ed8c9cf2/anchor 188b15f6/log-hash 75243d3f; #1096 Type E main f94f88a2/anchor
547bbfc7/log-hash a87ddccc; #1097 Type A main 13f857c0/anchor 423f92a9/log-hash 1cd17264; #1098 Type B main e454a736/
anchor 2cf9467a/log-hash 52716790 - all verified present via git log before this run's commit.
Guard lifecycle per #715: all 891 needles fragment-built in this file; the #1095 Type D file's twenty-seventh-direction
absence needle (TestTypeDFalsificationLedger1095::test_twenty_sixth_direction_present) and the #1098 Type B file's
max-890 (TestGuardLifecycle890Lands::test_max_numeric_id_is_890_not_889) and zero-numeric-891
(TestGuardLifecycle890Lands::test_zero_numeric_891_keys_in_profiles) needles fail BY DESIGN at this run - pinned as
forward-looking staleness via subprocess in the staleness class; the #1100 Type D run pins the zero-892 guards.
Do NOT touch #1024's m846 (FOURTEENTH, exclusionary-diversion): self-flagged sourcing-constraint violation; Ray's
revert/leave/rebuild-from-primary decision pending.
"""

import glob
import os
import re
import subprocess

import pytest
import yaml

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MECH_KEY = (
    "type_c_1099_google_ai_contribution_pilot_rate_disclosure_"
    "unilateral_pricing_twentyseventh_direction_sep30_12pm"
)
FILE_STEM = (
    "test_type_c_1099_google_ai_contribution_pilot_rate_disclosure_"
    "unilateral_pricing_twentyseventh_direction_sep30_12pm"
)
M_HOME = os.path.join("profiles", "competitor-entities.yaml")

# Guard needles are fragment-built per #715 so this file never adds a
# contiguous literal the earlier zero-guards scan for.
M_NUM = "8" + "91"
MID_891 = "mechanism_id: " + M_NUM
US_891 = "mechanism_" + M_NUM
DASH_891 = "mechanism-" + M_NUM
NEXT_NUM = "8" + "92"
MID_892 = "mechanism_id: " + NEXT_NUM
US_892 = "mechanism_" + NEXT_NUM
DASH_892 = "mechanism-" + NEXT_NUM
TW27 = "TWENTY-" + "SEVENTH relationship direction"
TW28 = "TWENTY-" + "EIGHTH relationship direction"

ANCHORED_SHA = "0" * 40  # patched to the main-commit SHA by the anchor followup per #565
ITERATION = 1099

PREDECESSORS = [
    ("D", "1095", "ed8c9cf2", "188b15f6", "75243d3f"),
    ("E", "1096", "f94f88a2", "547bbfc7", "a87ddccc"),
    ("A", "1097", "13f857c0", "423f92a9", "1cd17264"),
    ("B", "1098", "e454a736", "2cf9467a", "52716790"),
]

NOVEL_URLS = [
    "https://www.pymnts.com/google/2026/google-begins-paying-publishers-for-ai-overview-answers/",
    "https://anythingengineoptimization.com/item/2026-09-30-google-s-ai-contribution-pilot-pays-publishers-under-0-1-of-ad-revenue/",
    "https://aiweekly.co/alerts/googles-ai-overviews-pilot-pays-100-publishers-one-over-1m",
    "https://thedesk.net/2026/09/google-paying-news-publishers-ai-search-results/",
    "https://techstartups.com/2026/09/30/top-tech-news-today-september-30-2026-deepseek-anthropic-google-meta-openai-robinhood-more/",
]

D1095_FILE = (
    "tests/test_type_d_1095_m886_m887_m888_qualitative_"
    "corpus_integrity_sep30_8am.py"
)
B1098_FILE = (
    "tests/test_type_b_1098_reece_rogers_wired_muse_weeklong_"
    "data_alarm_vs_claude_cowork_m629_temporal_extension_sep30_11am.py"
)


def run_git(*args):
    return subprocess.run(
        ["git", *args], cwd=REPO, capture_output=True, text=True, timeout=120
    )


def load_all_docs():
    with open(os.path.join(REPO, M_HOME), encoding="utf-8") as fh:
        return list(yaml.safe_load_all(fh))


def get_block():
    docs = load_all_docs()
    for doc in docs:
        if isinstance(doc, dict) and MECH_KEY in doc:
            return doc[MECH_KEY]
    raise AssertionError("mechanism 891 block key not found in " + M_HOME)


def block_text():
    with open(os.path.join(REPO, M_HOME), encoding="utf-8") as fh:
        return fh.read()


# ---------------------------------------------------------------------------
# 1. Novelty anchor (per #565)
# ---------------------------------------------------------------------------
@pytest.mark.anchor
class TestNoveltyAnchorTypeC1099:
    def test_type_c_1099_commit_title_in_history(self):
        # The main commit subject must name the rotation slot.
        out = run_git("log", "--format=%s", "--grep=Type C #1099").stdout
        assert "Type C #1099" in out

    def test_anchor_sha_40hex(self):
        assert re.fullmatch(r"[0-9a-f]{40}", ANCHORED_SHA)

    def test_anchor_sha_matches_type_c_1099_main_commit(self):
        out = run_git("log", "--format=%H %s", "--grep=Type C #1099").stdout
        assert ANCHORED_SHA in out

    def test_anchor_sha_in_committed_tree(self):
        out = run_git("log", "--all", "--format=%H").stdout
        assert ANCHORED_SHA in out.splitlines()


# ---------------------------------------------------------------------------
# 2. Rotation guard: 1095-1099 window, CLOSING leg
# ---------------------------------------------------------------------------
@pytest.mark.rotation
class TestRotationGuard1095_1099Window:
    def test_predecessor_chains_present_in_history(self):
        log = run_git("log", "--format=%h %s").stdout
        for letter, num, main, anchor, loghash in PREDECESSORS:
            assert ("Type %s #%s" % (letter, num)) in log, (
                "predecessor Type %s #%s missing from history" % (letter, num)
            )
            for sha in (main, anchor, loghash):
                assert sha in log, (
                    "predecessor #%s chain sha %s missing from history" % (num, sha)
                )

    def test_window_order_d_e_a_b_c(self):
        # The 1095-1099 window runs D->E->A->B->C per #565; this run is the
        # CLOSING leg. git log is newest-first, so the window order maps to
        # descending log positions.
        log = run_git("log", "--format=%s").stdout
        idx = [log.index("Type %s #%s" % (letter, num)) for letter, num, *_ in PREDECESSORS]
        assert idx == sorted(idx, reverse=True), "window order D->E->A->B violated"

    def test_no_type_c_1099_before_this_run(self):
        # Pre-commit novelty guard: no earlier commit may claim the slot.
        # Superseded by design once this run's main commit lands.
        out = run_git("log", "--format=%s", "--grep=Type C #1099").stdout.strip()
        assert out == ""

# ---------------------------------------------------------------------------
# 3. Mechanism 891 block structure
# ---------------------------------------------------------------------------
class TestMechanism891Structure:
    def test_block_key_unique_at_column_zero(self):
        text = block_text()
        lines = [l for l in text.splitlines() if l.startswith(MECH_KEY + ":")]
        assert len(lines) == 1, "block key must appear exactly once at column zero"

    def test_block_key_field_repeats_key(self):
        blk = get_block()
        assert blk["block_key"] == MECH_KEY

    def test_mechanism_id_numeric_891(self):
        blk = get_block()
        assert blk["mechanism_id"] == 891

    def test_type_fields(self):
        blk = get_block()
        assert blk["type"] == "financial_incentive_mapping"
        assert blk["type_label"] == "Financial Incentive Mapping"
        assert blk["iteration"] == ITERATION
        assert blk["iteration_type"] == "C"
        assert blk["iteration_time"] == "2026-09-30 12:00 PDT"
        assert blk["goal_id"] == "goal_54093bda4145"
        assert blk["scheduled_job_id"] == "mediascope-daily-iteration"

    def test_connects_to(self):
        blk = get_block()
        assert blk["connects_to"] == [702, 708, 539, 666]

    def test_discipline_fields(self):
        blk = get_block()
        assert blk["tone_scored"] is False
        assert blk["engine_run"] is False
        assert blk["is_significant"] is False
        assert blk["verdict"] == "directionally_supported_not_proven"
        assert blk["no_analysis_json_update"] is True
        assert blk["artifact_grade"] is False
        assert blk["falsification_family_member"] is False

    def test_sources_structure(self):
        blk = get_block()
        srcs = blk["sources"]
        assert len(srcs) == 5
        for s in srcs:
            assert s["novel"] is True
            assert s["accessed"] == "2026-09-30"
            assert s["url"].startswith("https://")
        assert [s["url"] for s in srcs] == NOVEL_URLS

    def test_mechanism_name_mentions_direction(self):
        blk = get_block()
        assert TW27 in blk["mechanism_name"]
        assert "UNILATERAL PRICING" in blk["mechanism_name"]


# ---------------------------------------------------------------------------
# 4. Mechanism 891 legs
# ---------------------------------------------------------------------------
class TestMechanism891Legs:
    def test_finding_peg(self):
        blk = get_block()
        f = blk["finding"]
        for needle in (
            "around 100 publishers",
            "The Information Sep 29 2026",
            "PYMNTS Sep 30 relay opened first-hand",
            "past position was that it should not pay publishers",
            "20.02% to 9.69%",
            "Pew found only 1%",
            "m666",
        ):
            assert needle in f, needle

    def test_rate_disclosure_leg(self):
        blk = get_block()
        leg = blk["rate_disclosure_leg"]
        for needle in (
            "First disclosed payment rate",
            "under $1,000 over several months",
            "$50,000-$60,000",
            "more than $1M in a year",
            "less than 0.1% of their ad revenue",
            "AI earnings",
            "Accumulate earnings when your content contributes significantly",
            "not how the number was calculated",
        ):
            assert needle in leg, needle

    def test_unilateral_pricing_leg(self):
        blk = get_block()
        leg = blk["unilateral_pricing_leg"]
        for needle in (
            "determines for itself what that content is worth",
            "holding out",
            "no disclosed formula and no negotiation",
            "m702",
            "extremely collaborative",
        ):
            assert needle in leg, needle

    def test_decoupling_leg(self):
        blk = get_block()
        leg = blk["decoupling_leg"]
        for needle in (
            "opting out of the payment does not stop Google",
            "the two controls are independent",
            "payment buys no consideration",
            "20.02%-to-9.69%",
        ):
            assert needle in leg, needle

    def test_corpus_lineage(self):
        blk = get_block()
        leg = blk["corpus_lineage"]
        for needle in (
            "m708 (Bloomberg Law Jul 2026",
            "m702 (Digiday ~Sep 14 2026",
            "Inverts m702",
            "m539",
            "m666",
            "m64",
        ):
            assert needle in leg, needle

    def test_incentive_geometry(self):
        blk = get_block()
        g = blk["incentive_geometry"]
        for needle in (
            "Monopsony pricing",
            "destroyed the old consideration",
            "below-noticeability",
            "dashboard metric",
            "the platform holds the menu",
        ):
            assert needle in g, needle

    def test_coverage_nexus_no_tone(self):
        blk = get_block()
        n = blk["coverage_nexus"]
        assert "tone NOT_SCORED" in n
        assert "first disclosed payment rate" in n

    def test_legs_distinct(self):
        blk = get_block()
        legs = [
            blk["finding"],
            blk["rate_disclosure_leg"],
            blk["unilateral_pricing_leg"],
            blk["decoupling_leg"],
            blk["corpus_lineage"],
            blk["incentive_geometry"],
        ]
        assert len(set(legs)) == len(legs), "legs must not repeat each other"


# ---------------------------------------------------------------------------
# 5. TWENTY-SEVENTH relationship direction taxonomy
# ---------------------------------------------------------------------------
class TestMechanism891Taxonomy:
    def test_twenty_seventh_direction_present(self):
        text = block_text()
        assert TW27 in text
        blk = get_block()
        assert TW27 in blk["relationship_direction_taxonomy"]

    def test_enumeration_covers_1_through_26(self):
        tax = get_block()["relationship_direction_taxonomy"]
        for n, name in (
            ("1", "sue-then-sign m624"),
            ("2", "pay-or-litigate bifurcation m636"),
            ("12", "regulatory-bargaining m1004"),
            ("15", "ecosystem-grant m1029"),
            ("26", "dual-role recycling m888"),
        ):
            assert ("%s %s" % (n, name)) in tax, n

    def test_distinct_from_pay_or_litigate(self):
        tax = get_block()["relationship_direction_taxonomy"]
        assert "no sue-or-sign menu at all" in tax
        assert "use is non-contingent" in tax

    def test_distinct_from_regulatory_bargaining(self):
        tax = get_block()["relationship_direction_taxonomy"]
        assert "the PLATFORM sets the price, no state in the loop" in tax

    def test_mirror_of_ecosystem_grant(self):
        tax = get_block()["relationship_direction_taxonomy"]
        assert "the PAYER pays without RECEIVING consideration" in tax

    def test_distinct_from_pay_per_use_template(self):
        tax = get_block()["relationship_direction_taxonomy"]
        assert "the FORM is pay-per-use" in tax
        assert "WHO prices and the consent-decoupling" in tax

    def test_falsifiable_and_tension_carried(self):
        tax = get_block()["relationship_direction_taxonomy"]
        assert "Falsifiable:" in tax
        assert "large publishers join at current rates" in tax
        assert "Taxonomy-count tension carried" in tax
        assert "m737" in tax


# ---------------------------------------------------------------------------
# 6. Confounders, counterargument, falsification ledger
# ---------------------------------------------------------------------------
class TestMechanism891Confounders:
    def test_confounder_count_and_order(self):
        confs = get_block()["confounders"]
        assert [c["strength"] for c in confs] == [
            "STRONG",
            "STRONG",
            "STRONG",
            "MEDIUM",
            "MEDIUM",
            "WEAK",
        ]

    def test_strong_confounders(self):
        confs = get_block()["confounders"]
        strong = " ".join(c["text"] for c in confs if c["strength"] == "STRONG")
        for needle in (
            "Single reporting chain, excerpt-bounded",
            "paywalled",
            "46 lines",
            "Distribution opacity",
            "Pilot-phase rates",
        ):
            assert needle in strong, needle

    def test_medium_and_weak_confounders(self):
        confs = get_block()["confounders"]
        rest = " ".join(c["text"] for c in confs if c["strength"] != "STRONG")
        for needle in (
            "Holdout leverage unproven",
            "Relay fidelity",
            "m702-collapse risk",
        ):
            assert needle in rest, needle

    def test_counterargument_collapse_condition(self):
        ca = get_block()["counterargument"]
        assert "collapses into it" in ca
        assert "m702" in ca
        assert "payment becomes consideration again" in ca

    def test_falsification_ledger_holds_at_37(self):
        ff = get_block()["falsification_family"]
        assert "ledger holds at 37" in ff
        assert "THIRTY-SEVENTH in profiles/the-verge.yaml" in ff
        assert "THIRTY-EIGHTH member-claim form absent repo-wide" in ff
        # The block must not contain a member-claim form needle.
        assert "THIRTY-" + "EIGHTH falsification-family member" not in block_text()


# ---------------------------------------------------------------------------
# 7. Research method
# ---------------------------------------------------------------------------
class TestResearchMethodTypeC1099:
    def test_five_novel_urls_verbatim(self):
        assert len(NOVEL_URLS) == 5
        assert NOVEL_URLS[0].startswith("https://www.pymnts.com/google/2026/")
        assert "ai-overview-answers" in NOVEL_URLS[0]
        assert "anythingengineoptimization.com/item/2026-09-30" in NOVEL_URLS[1]
        assert "aiweekly.co/alerts/" in NOVEL_URLS[2]
        assert "thedesk.net/2026/09/" in NOVEL_URLS[3]
        assert "techstartups.com/2026/09/30/" in NOVEL_URLS[4]

    def test_novelty_claim_documents_sources(self):
        nov = get_block()["novelty"]
        assert "5 relay URLs" in nov
        assert "FIRST dedicated corpus mechanism" in nov
        assert "TWENTY-SEVENTH relationship direction" in nov

    def test_rotation_transparency_in_block(self):
        rt = get_block()["rotation_transparency"]
        assert "FIFTH and CLOSING leg of the 1095-1099 window" in rt
        for num, main, anchor, loghash in (
            ("1095", "ed8c9cf2", "188b15f6", "75243d3f"),
            ("1096", "f94f88a2", "547bbfc7", "a87ddccc"),
            ("1097", "13f857c0", "423f92a9", "1cd17264"),
            ("1098", "e454a736", "2cf9467a", "52716790"),
        ):
            assert ("#%s Type" % num) in rt
            for sha in (main, anchor, loghash):
                assert sha in rt
        assert "#1100 Type D, opening the 1100-1104 window" in rt

# ---------------------------------------------------------------------------
# 8. Post-commit corpus novelty
# ---------------------------------------------------------------------------
class TestCorpusNoveltyPostCommit:
    def _git_grep_head(self, needle, *roots):
        return run_git("grep", "-F", needle, "HEAD", "--", *roots)

    def test_next_mechanism_892_absent_repo_wide(self):
        # The next mechanism (892) must not exist anywhere in the tree.
        assert self._git_grep_head(US_892, "tests/", "profiles/").returncode != 0

    def test_no_numeric_892_keys_in_profiles(self):
        assert self._git_grep_head(MID_892, "profiles/").returncode != 0

    def test_no_dash_892_references_repo_wide(self):
        assert self._git_grep_head(DASH_892, "tests/", "profiles/").returncode != 0

    def test_no_twenty_eighth_direction(self):
        # The next direction slot must be unclaimed repo-wide.
        assert (
            self._git_grep_head(TW28, "profiles/", "tests/", "iteration-log.md").returncode
            != 0
        )

    def test_891_present_in_committed_tree(self):
        # Commit-dependent: passes only after this run's main commit lands.
        r = self._git_grep_head(MID_891, "profiles/")
        assert r.returncode == 0 and MECH_KEY in r.stdout

    def test_block_key_in_committed_profiles(self):
        r = run_git("grep", "-F", MECH_KEY, "HEAD", "--", "profiles/")
        assert r.returncode == 0

    def test_type_c_1099_entry_in_committed_log(self):
        r = run_git("grep", "-F", "## #1099 Type C:", "HEAD", "--", "iteration-log.md")
        assert r.returncode == 0


# ---------------------------------------------------------------------------
# 9. Forward-looking staleness (per #1060 / #710 / #720)
# ---------------------------------------------------------------------------
D1095_CLASSES = (
    "TestNovelty1095",
    "TestTypeDRotationGuard1095",
    "TestTypeDCorpusIntegrity1095",
    "TestTypeDM886QualitativeDiscipline",
    "TestTypeDM887QualitativeDiscipline",
    "TestTypeDM888QualitativeDiscipline",
    "TestTypeDForwardLookingStaleness1095",
    "TestGuardLifecycle1095",
    "TestBackgroundSuiteVerdict1095",
    "TestSyntheticEngineCalibration1095",
    "TestSuiteRelaunch1095",
    "TestTypeD1095RepinOf1090File",
    "TestTypeDDocSync1095",
    "TestTypeDIterationLog1095",
    "TestInflightIsolation1095",
)

B1098_CLASSES = (
    "TestNoveltyAnchorTypeB1098",
    "TestRotationGuard1095_1099Window",
    "TestCorpusNoveltyGreps",
    "TestMechanism890Structure",
    "TestMetaArmEvidence",
    "TestAnthropicArmEvidence",
    "TestTemporalExtensionAndDelta",
    "TestStatisticalDisciplineStandingRule",
    "TestFalsificationLedger",
    "TestConfoundersRankedStrongFirst",
    "TestCrossReferences",
    "TestResearchMethodPer503",
    "TestDocSyncRatchet",
    "TestIterationLogEntry",
    "TestInflightIsolation",
    "TestBlockHygiene",
)


class TestStalenessPins1099:
    """Pins the by-design stale guards superseded by mechanism 891."""

    def _stale_run(self, path, *deselects):
        cmd = [
            ".venv/bin/python",
            "-m",
            "pytest",
            path,
            "-q",
            "--no-header",
            "-p",
            "no:cacheprovider",
            "-o",
            "addopts=",
        ]
        for d in deselects:
            cmd.extend(["--deselect", "%s::%s" % (path, d)])
        return subprocess.run(
            cmd, cwd=REPO, capture_output=True, text=True, timeout=300
        )

    def _failed(self, result):
        return [
            line for line in result.stdout.splitlines() if line.startswith("FAILED")
        ]

    def test_1095_twenty_seventh_absence_failed_by_design(self):
        # The #1095 Type D file's twenty-seventh-direction absence guard must
        # FAIL in a subprocess: mechanism 891 registers UNILATERAL PRICING as
        # the twenty-seventh relationship direction. Pinned as fail-by-design
        # so it is never silently ignored; the #1100 Type D run owns the next
        # guard cycle.
        result = self._stale_run(D1095_FILE, *D1095_CLASSES)
        assert result.returncode != 0
        failed = self._failed(result)
        name = "TestTypeDFalsificationLedger1095::test_twenty_sixth_direction_present"
        assert any(name in line for line in failed), failed

    def test_1098_max_890_guard_failed_by_design(self):
        # The #1098 Type B file's max-890 guard must FAIL: the max numeric
        # mechanism_id is now 891.
        result = self._stale_run(B1098_FILE, *B1098_CLASSES)
        assert result.returncode != 0
        failed = self._failed(result)
        name = "TestGuardLifecycle890Lands::test_max_numeric_id_is_890_not_889"
        assert any(name in line for line in failed), failed

    def test_1098_zero_numeric_891_guard_failed_by_design(self):
        # The #1098 zero-numeric-891 guard must FAIL: profiles now carries a
        # numeric 891 key. The underscore-891 and dash-891 guards keep passing
        # (no contiguous literals added).
        result = self._stale_run(B1098_FILE, *B1098_CLASSES)
        assert result.returncode != 0
        failed = self._failed(result)
        name = "TestGuardLifecycle890Lands::test_zero_numeric_891_keys_in_profiles"
        assert any(name in line for line in failed), failed


# ---------------------------------------------------------------------------
# 10. Doc-sync ratchet
# ---------------------------------------------------------------------------
BASE_TESTS = 55831
BASE_FILES = 1423
OWN_TESTS = 64
EXPECT_TESTS = BASE_TESTS + OWN_TESTS  # 55895
EXPECT_FILES = BASE_FILES + 1  # 1424


class TestDocSyncRatchet:
    def _readme(self):
        with open(os.path.join(REPO, "README.md"), encoding="utf-8") as fh:
            return fh.read()

    def test_readme_stats_line_ratchet(self):
        m = re.search(
            r"\|\s*Tests\s*\|\s*(\d+)\s*\|\s*Across\s*(\d+)\s*test files",
            self._readme(),
        )
        assert m is not None, "README stats line missing"
        assert (int(m.group(1)), int(m.group(2))) == (EXPECT_TESTS, EXPECT_FILES)

    def test_readme_table_row_present(self):
        row = [l for l in self._readme().splitlines() if FILE_STEM in l]
        assert len(row) == 1, "README test-table row missing"
        assert "Type C #1099" in row[0]
        assert "64 tests, 13 classes" in row[0]

    def test_architecture_tree_row_present(self):
        with open(
            os.path.join(REPO, "docs", "ARCHITECTURE.md"), encoding="utf-8"
        ) as fh:
            text = fh.read()
        row = [l for l in text.splitlines() if FILE_STEM in l]
        assert len(row) == 1, "ARCHITECTURE tree row missing"
        assert "1095-1099 window FIFTH leg" in row[0]

    def test_collected_count_matches_expected(self):
        result = subprocess.run(
            [
                ".venv/bin/python",
                "-m",
                "pytest",
                os.path.join("tests", FILE_STEM + ".py"),
                "--collect-only",
                "-q",
                "--no-header",
                "-p",
                "no:cacheprovider",
                "-o",
                "addopts=",
            ],
            cwd=REPO,
            capture_output=True,
            text=True,
            timeout=300,
        )
        lines = [
            l
            for l in result.stdout.splitlines()
            if l.startswith("tests/") and "::" in l
        ]
        assert len(lines) == OWN_TESTS, (
            "collected %d tests, expected %d" % (len(lines), OWN_TESTS)
        )


# ---------------------------------------------------------------------------
# 11. Iteration-log entry
# ---------------------------------------------------------------------------
class TestIterationLogEntry:
    def _log(self):
        with open(os.path.join(REPO, "iteration-log.md"), encoding="utf-8") as fh:
            return fh.read()

    def test_entry_header_present(self):
        text = self._log()
        assert "## #1099 Type C:" in text
        assert "Type C FIFTH leg of the 1095-1099 window, CLOSING it" in text

    def test_entry_rotation_transparency(self):
        text = self._log()
        assert "1095-1099 window FIFTH leg" in text
        for num, main, anchor, loghash in (
            ("1095", "ed8c9cf2", "188b15f6", "75243d3f"),
            ("1096", "f94f88a2", "547bbfc7", "a87ddccc"),
            ("1097", "13f857c0", "423f92a9", "1cd17264"),
            ("1098", "e454a736", "2cf9467a", "52716790"),
        ):
            assert ("#%s Type" % num) in text

    def test_entry_finding_summary(self):
        text = self._log()
        assert "UNILATERAL PRICING" in text
        assert "around 100 publishers" in text
        assert "first disclosed payment rate" in text

    def test_entry_method(self):
        text = self._log()
        assert "3 search sets" in text
        assert "1 browser.open" in text
        assert "PYMNTS" in text

    def test_entry_doc_sync_ratchet(self):
        text = self._log()
        assert "55831/1423 -> 55895/1424 (+64/+1)" in text

    def test_anchor_sha_pinned_and_logged(self):
        # Commit-dependent: passes after the anchor followup patches
        # ANCHORED_SHA to the main-commit SHA and the log-hash followup
        # registers the hashes in the entry header per #721.
        assert ANCHORED_SHA[:8] in self._log()


# ---------------------------------------------------------------------------
# 12. In-flight isolation: never touch concurrent workers' files
# ---------------------------------------------------------------------------
class TestInflightIsolation:
    def test_no_concurrent_inflight_iteration_commits_staged(self):
        # The in-flight #899/#938/#900/#1012-wt working-tree edits are
        # owned by their runs; this run stages only its own files.
        status = run_git("status", "--short").stdout
        staged = [l for l in status.splitlines() if l.startswith(("M ", "A "))]
        for f in ("nytimes.yaml", "test_type_b_938_", "test_type_d_900_", "test_type_a_1012_"):
            assert not any(f in l for l in staged)

    def test_this_run_stages_only_own_files(self):
        status = run_git("status", "--short").stdout
        staged = [l for l in status.splitlines() if l.startswith(("M ", "A "))]
        allowed = (
            "profiles/competitor-entities.yaml",
            "test_type_c_1099_",
            "README.md",
            "docs/ARCHITECTURE.md",
            "iteration-log.md",
        )
        for l in staged:
            assert any(a in l for a in allowed), l


# ---------------------------------------------------------------------------
# 13. Block hygiene
# ---------------------------------------------------------------------------
class TestBlockHygiene:
    def test_yaml_single_document(self):
        assert len(load_all_docs()) == 1

    def test_block_round_trips(self):
        blk = get_block()
        assert blk["yaml_parse_clean"] is True
        assert blk["ascii_only"] is True
        assert isinstance(blk["confounders"], list)
        assert isinstance(blk["sources"], list)

    def test_ascii_only_block(self):
        text = block_text()
        start = text.index(MECH_KEY + ":")
        segment = text[start:]
        assert not re.search(r"[^\x00-\x7F]", segment), "non-ASCII bytes in block"

    def test_no_em_dashes_in_block(self):
        text = block_text()
        start = text.index(MECH_KEY + ":")
        assert "\u2014" not in text[start:]
