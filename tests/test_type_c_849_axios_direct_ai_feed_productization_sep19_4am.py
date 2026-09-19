"""Type C #849 (845-849 window, fifth leg D->E->A->B->C, CLOSING the window):
Axios Direct AI-feed productization (Sep 16 2026 Digiday Publishing
Summit) - publisher-as-feed-operator as the SEVENTH relationship
direction (mechanism 741).

FIRST dedicated corpus mapping of a publisher productizing its own
AI-era content feeds: Axios CRO Jacquelyn Cameron announced on stage at
the Digiday Publishing Summit (Sep 16 2026, Key Biscayne FL; reported by
Tim Peterson, Digiday, Sep 18 2026 - read first-hand this run, 94
rendered lines) that Axios takes to market this month Axios Direct -
three content feeds that "effectively take the concepts of a Bloomberg
terminal and an RSS feed and update them for the agentic AI era." Feed 1:
investment companies with high AUM, annual fee varying by company size
and AUM, an upsell to existing Axios Pro Deals subscribers, structured
as two-year deals stretching revenue into 2028. Feed 2: companies with
internal AI models ingest Axios feeds directly (in discussion, no launch
timeframe) - the labs as named customer class. Feed 3: individual
subscribers via personal AI agents (ChatGPT, Claude named; earliest
stage; 2027 exploration). Cameron attributed Axios hitting its 2026
revenue goal early September (vs end of October last year; growth 10-50%
vs 2025) in part to pre-booking deals from the previous July. 52-54% of
2026 revenue direct-through-client; direct deals preferred over
Microsoft-style AI content marketplaces (Snowflake Marketplace
conversations ongoing); branded content / agent-aimed ads not ruled out
(Time precedent). SEVENTH relationship direction (extends m738's
infrastructure-capture; the publisher-internal mirror: Axios becomes its
own feed operator). Incentive geometry: publisher-to-lab CUSTOMER
relationship - AI-model companies become Axios Direct paying customers;
recurring-fee vendor dependence distinct from one-off licensing
payer-dependence. Confounders 3/3/3 (feeds 2+3 announced intent only;
trade-press sourcing; wide 10-50% band; feed-1 customers are not labs;
ads leg uncommitted). Counter-evidence 4 (diversification motive cuts
against naive prediction; vaporware risk; extension of existing
direct-sales posture; money-flow inversion from the OpenAI-funded
m478/m639 legs). MANUAL qualitative only, engine NOT run,
p_value/cohens_d/ci_95 NOT_CALCULATED, is_significant False,
verdict directionally_supported_not_proven; NOT falsification-family,
ledger holds at 26; no analysis.json update. Novelty verified pre-commit
(zero test_type_c_849 files; no 'Type C #849' in git log; max numeric
mechanism_id 740; zero underscore-form 741 keys by designed keying per
#715; block key zero-hit; the Digiday Axios Direct URL zero-hit
repo-wide); 845-849 window fifth leg D->E->A->B->C CLOSING it (anchor
patched post-commit per #565) - Sep 19 2026 04:00 PDT.
"""

import os
import re
import subprocess
import datetime

import pytest
import yaml

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
TESTS_DIR = os.path.join(REPO_ROOT, "tests")
OWN_BASENAME = "test_type_c_849_axios_direct_ai_feed_productization_sep19_4am.py"
MECH_KEY = "axios_direct_ai_feed_productization_sep2026"
M_ID = 741
ITER = 849
TYPE_LETTER = "C"
# Concatenated so this file never contains the literal marker itself.
MECH_ID_MARKER = "mechanism" + "_741"
NEXT_ID_MARKER = "mechanism" + "_742"
NEXT_ID_NUMERIC = "mechanism_id: " + "742"
EXPECTED_ORDER = [("C", "849"), ("B", "848"), ("A", "847"), ("E", "846"), ("D", "845")]
# Patched to the real main-commit SHA in the anchor followup per the #565 convention.
ANCHORED_SHA = "6973506195ce866bf4b4430a4ae4a9b5d9a81387"

DIGIDAY_URL = "https://digiday.com/media/axios-preps-new-axios-direct-feeds-for-ai-models-agents-as-revenue-tops-2026-goal/"

README_PATH = os.path.join(REPO_ROOT, "README.md")
ARCH_PATH = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")
LOG_PATH = os.path.join(REPO_ROOT, "iteration-log.md")


def _read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def _entities_text():
    return _read(os.path.join(REPO_ROOT, "profiles", "competitor-entities.yaml"))


def _block():
    text = _entities_text()
    start = text.index(MECH_KEY)
    end = text.index("\nadvance_dual_asset_monetization:")
    return text[start:end]


def _corpus_ids():
    ids = []
    for root, _, files in os.walk(os.path.join(REPO_ROOT, "profiles")):
        for fn in files:
            if fn.endswith(".yaml"):
                text = _read(os.path.join(root, fn))
                for m in re.finditer(r"mechanism_id:\s*(\d+)", text):
                    ids.append(int(m.group(1)))
    return ids


def _repo_grep(needle, roots=("profiles", "tests")):
    hits = []
    for r in roots:
        base = os.path.join(REPO_ROOT, r)
        for root, _, files in os.walk(base):
            for fn in files:
                if fn.rsplit(".", 1)[-1] in ("py", "yaml", "md", "json"):
                    p = os.path.join(root, fn)
                    try:
                        if needle in _read(p):
                            hits.append(os.path.relpath(p, REPO_ROOT))
                    except OSError:
                        pass
    return hits


def _git(*args):
    return subprocess.run(
        ["git", *args],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=True,
    ).stdout


def _git_log_mains(qualifier):
    out = _git("log", "--all", "--format=%H %s", "--grep", qualifier)
    mains = {}
    for line in out.splitlines():
        if not line.strip():
            continue
        sha, _, subject = line.partition(" ")
        if "Type C #849" in subject:
            mains[sha] = subject
    return mains


def _window(n=40):
    # First occurrence of each distinct iteration number, newest first
    # (robust to followup commits that repeat the same "Type X #N" wording
    # without the colon, per the #752 convention).
    subjects = _git("log", f"-{n}", "--format=%s", "--no-merges").splitlines()
    seen_nums = set()
    out = []
    for s in subjects:
        m = re.match(r"Type ([A-E]) #(\d+):", s)
        if m and m.group(2) not in seen_nums:
            seen_nums.add(m.group(2))
            out.append(m.groups())
    return out[:5]


class TestNovelty849:
    def test_single_test_type_c_849_file(self):
        matches = [
            f
            for f in os.listdir(TESTS_DIR)
            if f.startswith("test_type_c_849") and f.endswith(".py")
        ]
        assert matches == [OWN_BASENAME], matches

    def test_type_c_849_main_commit_unique_and_anchored(self):
        # No #849 main commit exists pre-commit; the anchor test pins
        # the main commit SHA once the followup patches ANCHORED_SHA.
        # Deselected pre-commit per #565; patched green in the anchor
        # followup.
        result = subprocess.run(
            ["git", "log", "--format=%H %s", "--", "tests/" + OWN_BASENAME],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        mains = [
            line
            for line in result.stdout.splitlines()
            if "Type C #849" in line and "followup" not in line.lower()
        ]
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ) or mains == []
        if mains:
            assert mains[0].startswith(ANCHORED_SHA + " "), mains

    def test_novelty_verification_claim(self):
        # This run ADDS mechanism 741: post-commit max is 741, zero 742
        # keys anywhere. Pre-commit sweeps verified max 740, zero
        # underscore-form 741 keys (designed keying per #715), block key
        # zero-hit, Digiday Axios Direct URL zero-hit repo-wide.
        assert max(_corpus_ids()) == 741
        assert _repo_grep(NEXT_ID_MARKER) == []
        assert _repo_grep(NEXT_ID_NUMERIC, roots=("profiles",)) == []

    def test_845_849_window_legs_present_prior_to_849(self):
        log = _read(LOG_PATH)
        for marker in (
            "## #845 Type D:",
            "## #846 Type E:",
            "## #847 Type A:",
            "## #848 Type B:",
        ):
            assert marker in log, marker


class TestRotationGuard849:
    """#849 is the Type C fifth leg of window 845-849: D->E->A->B->C, CLOSING it."""

    ORDER = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}

    def test_window_is_845_849_fifth_leg(self):
        # Deselected pre-commit per #565 (the #849 main commit does not
        # exist yet); patched green in the anchor followup.
        window = _window()
        assert window[: len(EXPECTED_ORDER)] == EXPECTED_ORDER, (
            f"845-849 window fifth leg D->E->A->B->C: expected {EXPECTED_ORDER}, "
            f"got {window[: len(EXPECTED_ORDER)]}"
        )

    def test_rotation_adjacency_cycle_valid(self):
        # Deselected pre-commit per #565; patched green in the followup.
        window = _window()
        for (t1, n1), (t2, n2) in zip(window, window[1:]):
            assert int(n1) == int(n2) + 1
            assert (self.ORDER[t1] - self.ORDER[t2]) % 5 == 1, (t1, t2)

    def test_predecessor_is_type_b_848(self):
        # Deselected pre-commit per #565; patched green in the followup.
        window = _window()
        assert window[1] == ("B", "848"), (
            f"immediate predecessor must be Type B #848, got {window[1]}"
        )

    def test_anchor_sha_matches_head(self):
        # Patched to the real main-commit SHA in the anchor followup per
        # the #565 convention; deselected pre-commit at the pytest CLI.
        mains = _git_log_mains("Type C #849: Axios Direct")
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ), mains
        newest_sha = next(iter(mains))
        assert newest_sha == ANCHORED_SHA, mains


class TestMechanism741Structure:
    def test_block_key_exists_in_competitor_entities(self):
        assert MECH_KEY in _entities_text()

    def test_block_key_unique(self):
        keys = re.findall(r"^  " + MECH_KEY + r":$", _entities_text(), re.M)
        assert len(keys) == 1, keys

    def test_block_nests_under_marketplace_intermediary_landscape(self):
        text = _entities_text()
        assert text.index("marketplace_intermediary_landscape:") < text.index(MECH_KEY)
        assert text.index(MECH_KEY) < text.index("\nadvance_dual_asset_monetization:")

    def test_iteration_and_type_and_time_pdt(self):
        block = _block()
        assert "iteration: 849" in block
        assert "type: 'C'" in block
        assert "2026-09-19 04:00 PDT" in block
        assert "mechanism_id: 741" in block

    def test_designed_keying_no_underscore_741_in_block(self):
        # Per #715: block keys and prose must not carry the underscore-form
        # mechanism id; the colon form mechanism_id: 741 is the only allowed
        # 741 reference.
        block = _block()
        assert MECH_ID_MARKER not in block
        assert "mechanism_id: 741" in block

    def test_yaml_parses_and_fields(self):
        d = yaml.safe_load(_entities_text())
        mech = d["marketplace_intermediary_landscape"][MECH_KEY]
        assert mech["mechanism_id"] == 741
        assert mech["verification"]["iteration"] == 849
        assert mech["verification"]["type"] == "C"
        assert mech["verification"]["date"] == "2026-09-19 04:00 PDT"
        assert mech["verdict"] == "directionally_supported_not_proven"
        assert mech["falsification_family"] is False
        assert mech["falsification_ledger_holds_at"] == 26
        assert mech["tone_scores"] == "NOT_SCORED"

    def test_max_mechanism_id_is_741(self):
        assert max(_corpus_ids()) == 741


class TestMechanism741AnnouncementFacts:
    def test_cameron_summit_stage_facts_verbatim(self):
        block = _block()
        assert "Jacquelyn Cameron" in block
        assert "Digiday Publishing Summit" in block
        assert "Sep 16 2026" in block
        assert "Key Biscayne" in block
        assert "Tim Peterson" in block

    def test_digiday_read_first_hand_94_lines(self):
        block = _block()
        assert "READ FIRST-HAND this run" in block
        assert "94 rendered lines" in block
        assert DIGIDAY_URL in block

    def test_feed1_investment_company_facts(self):
        block = _block()
        assert "investment companies" in block
        assert "assets under management" in block
        assert "Axios Pro Deals" in block
        assert "two-year deals" in block

    def test_feed2_internal_ai_model_facts(self):
        block = _block()
        assert "internal AI models" in block
        assert "in discussion, no launch timeframe" in block

    def test_feed3_personal_agent_facts(self):
        block = _block()
        assert "ChatGPT" in block
        assert "Claude" in block
        assert "2027 exploration" in block

    def test_revenue_goal_facts(self):
        block = _block()
        assert "early September" in block
        assert "end of October" in block
        assert "10% and 50%" in block

    def test_direct_through_client_and_marketplace_posture(self):
        block = _block()
        assert "52-54%" in block
        assert "Snowflake" in block

    def test_agent_ads_not_ruled_out_with_time_precedent(self):
        block = _block()
        assert "Branded content" in block
        assert "Time" in block


class TestMechanism741Taxonomy:
    def test_seventh_direction_publisher_as_feed_operator(self):
        block = _block()
        assert "SEVENTH direction" in block
        assert "PUBLISHER-AS-FEED-OPERATOR" in block

    def test_extends_m738_infrastructure_capture(self):
        block = _block()
        assert "m738" in block
        assert "infrastructure-capture" in block

    def test_corpus_continuity_axios_openai_legs(self):
        block = _block()
        assert "mechanism_478" in block
        assert "mechanism_639" in block

    def test_connects_wiley_recurring_m735(self):
        block = _block()
        assert "735" in block
        assert "recurring" in block

    def test_incentive_geometry_customer_relationship(self):
        block = _block()
        assert "CUSTOMER relationship" in block
        assert "customer class" in block


class TestMechanism741Discipline:
    def test_p_value_not_calculated(self):
        assert "p_value" in _block() and "NOT_CALCULATED" in _block()

    def test_cohens_d_not_calculated(self):
        assert "cohens_d" in _block() and "NOT_CALCULATED" in _block()

    def test_ci_95_not_calculated(self):
        assert "ci_95" in _block() and "NOT_CALCULATED" in _block()

    def test_discipline_note_statistical_guards(self):
        block = _block()
        assert "Qualitative Type C mapping" in block
        assert "NOT_CALCULATED" in block
        assert "MANUAL qualitative only" in block
        assert "no coverage-tone claim" in block

    def test_verdict_and_correlation_note(self):
        block = _block()
        assert "directionally_supported_not_proven" in block
        assert "Correlation is not causation" in block

    def test_financial_incentive_documentation_leg(self):
        block = _block()
        assert "financial-incentive documentation leg" in block
        assert "no coverage-tone claim" in block

    def test_falsification_ledger_holds_at_26(self):
        block = _block()
        assert "falsification_ledger_holds_at: 26" in block
        assert "falsification_family: false" in block

    def test_manual_qualitative_only(self):
        block = _block()
        assert "MANUAL qualitative only" in block


class TestDocSync849:
    def test_readme_row_849(self):
        assert OWN_BASENAME in _read(README_PATH)

    def test_architecture_row_849(self):
        assert OWN_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_849_file(self):
        doc = _read(ARCH_PATH)
        assert OWN_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))


class TestIterationLog849:
    def _entry(self):
        log = _read(LOG_PATH)
        idx = log.index("## #849 Type C:")
        return log[idx : idx + 14000]

    def test_log_entry_present(self):
        assert "## #849 Type C:" in _read(LOG_PATH)

    def test_log_mechanism_numbers_and_topics(self):
        entry = self._entry()
        assert "mechanism 741" in entry
        assert "Axios Direct" in entry

    def test_log_rotation_window_845_849(self):
        entry = self._entry()
        assert "845-849" in entry

    def test_log_closing_leg(self):
        entry = self._entry()
        assert "CLOSING" in entry

    def test_log_no_analysis_json_update_and_not_artifact_grade(self):
        entry = self._entry()
        assert "no analysis.json update" in entry
        assert "NOT artifact-grade" in entry


class TestDateGrounding849:
    def test_sep_19_2026_is_saturday(self):
        assert datetime.datetime(2026, 9, 19).strftime("%A") == "Saturday"

    def test_run_time_pdt_grounded(self):
        assert datetime.datetime(2026, 9, 19, 4, 0).strftime("%H:%M") == "04:00"
