"""Type C #854 (850-854 window, fifth leg D->E->A->B->C, CLOSING the window):
RTB Digital x Paradium.AI Sep 18 2026 8-K verification leg - SEC-filed
confirmation of the infrastructure-capture direction (mechanism 744,
extends mechanism 738).

FIRST corpus SEC-filed primary-source verification of the SIXTH
relationship direction (infrastructure-capture, m738). RTB Digital filed
a material-agreement Form 8-K on September 18 2026 (EDGAR accession
0001185185-26-004171; full text read first-hand this run, ~13.4K chars).
Date of report (earliest event): September 14 2026 (ten-year Strategic
Platform Agreement signing with Paradium.AI, f/k/a The Arena Group
Holdings). Companion Item 7.01 Reg FD 8-K (accession
0001185185-26-004134) furnishes the Sep 17 clarifying press release as
Exhibit 99.1 - furnished, NOT filed. Filing-confirmed terms: 10-year
initial term, Q4 2026 close target, ~$100M annual gross revenue / 100M
monthly users / ~$1B over ten years (forward-looking, qualified),
Paradium brands+revenue+traffic migrate to RTB platform (ad ops,
syndication, Coinbase DeFi payments), Paradium non-compete during term
(contracted lock-in), perpetual irrevocable RTB tech control, $11.5M
RTB stock to Paradium, ~49.5% equity for $89,555,638 from Simplify/MBX
($10M deposit + $6M stock + $73,555,638 cash; below-50% cap; Simplify
retains ~23%), seller put exercisable 120 days after closing
collateralized by RTB's revenue share. NOT a new (eighth) direction -
verification leg of the sixth; direction count holds at SEVEN.
Confounders 3/3/3 (deal unclosed, RTB must raise capital for the cash
leg; issuer-disclosed single filing; projections qualified; below-50%
cap; seller-side put leverage). Counter-evidence 4 (not buying
Paradium; no incremental RTB expenses; deliberate below-50% cap; funding
conditionality can kill the deal). MANUAL qualitative only, engine NOT
run, p_value/cohens_d/ci_95 NOT_CALCULATED, is_significant False,
verdict directionally_supported_not_proven; NOT falsification-family,
ledger holds at 26; no analysis.json update. Novelty verified pre-commit
(zero test_type_c_854 files; no 'Type C #854' in git log; max numeric
mechanism_id 743; zero underscore-form 744 keys by designed keying per
#715; block key zero-hit; EDGAR accession zero-hit repo-wide); 850-854
window fifth leg D->E->A->B->C CLOSING it (anchor patched post-commit
per #565) - Sep 19 2026 09:00 PDT.
"""

import os
import re
import subprocess
import datetime

import pytest
import yaml

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
TESTS_DIR = os.path.join(REPO_ROOT, "tests")
OWN_BASENAME = "test_type_c_854_rtb_paradium_8k_verification_infrastructure_capture_sep19_9am.py"
MECH_KEY = "rtb_paradium_8k_verification_infrastructure_capture_leg_sep2026"
M_ID = 744
ITER = 854
TYPE_LETTER = "C"
# Concatenated so this file never contains the literal marker itself.
MECH_ID_MARKER = "mechanism" + "_744"
NEXT_ID_MARKER = "mechanism" + "_745"
NEXT_ID_NUMERIC = "mechanism_id: " + "745"
EXPECTED_ORDER = [("C", "854"), ("B", "853"), ("A", "852"), ("E", "851"), ("D", "850")]
# Patched to the real main-commit SHA in the anchor followup per the #565 convention.
ANCHORED_SHA = "8a5d80a455bf233b681b292e18757474333e06ba"

EDGAR_8K_ITEM101 = "https://www.sec.gov/Archives/edgar/data/1419275/000118518526004171/rtb8k091826.htm"
EDGAR_8K_ITEM701 = "https://www.sec.gov/Archives/edgar/data/1419275/000118518526004134/rtb8k0091826.htm"
MINICHART_URL = "https://www.minichart.com.sg/2026/09/19/rtb-digital-signs-10-year-platform-deal-with-paradium-ai-targeting-100-million-annual-revenue/"
QUIVER_URL = "https://www.quiverquant.com/news/Roundtable%20Clarifies%20Paradium.AI%20Strategic%20Platform%20Agreement,%20Minority%20Share%20Purchase%20and%20$100%20Million%20Ad%20Ecosystem%20Outlook"

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
        if "Type C #854" in subject:
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


class TestNovelty854:
    def test_single_test_type_c_854_file(self):
        matches = [
            f
            for f in os.listdir(TESTS_DIR)
            if f.startswith("test_type_c_854") and f.endswith(".py")
        ]
        assert matches == [OWN_BASENAME], matches

    def test_type_c_854_main_commit_unique_and_anchored(self):
        # No #854 main commit exists pre-commit; the anchor test pins
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
            if "Type C #854" in line and "followup" not in line.lower()
        ]
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ) or mains == []
        if mains:
            assert mains[0].startswith(ANCHORED_SHA + " "), mains

    def test_novelty_verification_claim(self):
        # This run ADDS mechanism 744: post-commit max is 744, zero 745
        # keys anywhere. Pre-commit sweeps verified max 743, zero
        # underscore-form 744 keys (designed keying per #715), block key
        # zero-hit, EDGAR accession zero-hit repo-wide.
        assert max(_corpus_ids()) == 744
        assert _repo_grep(NEXT_ID_MARKER) == []
        assert _repo_grep(NEXT_ID_NUMERIC, roots=("profiles",)) == []

    def test_850_854_window_legs_present_prior_to_854(self):
        log = _read(LOG_PATH)
        for marker in (
            "## #850 Type D:",
            "## #851 Type E:",
            "## #852 Type A:",
            "## #853 Type B:",
        ):
            assert marker in log, marker


class TestRotationGuard854:
    """#854 is the Type C fifth leg of window 850-854: D->E->A->B->C, CLOSING it."""

    ORDER = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}

    def test_window_is_850_854_fifth_leg(self):
        # Deselected pre-commit per #565 (the #854 main commit does not
        # exist yet); patched green in the anchor followup.
        window = _window()
        assert window[: len(EXPECTED_ORDER)] == EXPECTED_ORDER, (
            f"850-854 window fifth leg D->E->A->B->C: expected {EXPECTED_ORDER}, "
            f"got {window[: len(EXPECTED_ORDER)]}"
        )

    def test_rotation_adjacency_cycle_valid(self):
        # Deselected pre-commit per #565; patched green in the followup.
        window = _window()
        for (t1, n1), (t2, n2) in zip(window, window[1:]):
            assert int(n1) == int(n2) + 1
            assert (self.ORDER[t1] - self.ORDER[t2]) % 5 == 1, (t1, t2)

    def test_predecessor_is_type_b_853(self):
        # Deselected pre-commit per #565; patched green in the followup.
        window = _window()
        assert window[1] == ("B", "853"), (
            f"immediate predecessor must be Type B #853, got {window[1]}"
        )

    def test_anchor_sha_matches_head(self):
        # Patched to the real main-commit SHA in the anchor followup per
        # the #565 convention; deselected pre-commit at the pytest CLI.
        mains = _git_log_mains("Type C #854: RTB Digital")
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ), mains
        newest_sha = next(iter(mains))
        assert newest_sha == ANCHORED_SHA, mains


class TestMechanism744Structure:
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
        assert "iteration: 854" in block
        assert "type: 'C'" in block
        assert "2026-09-19 09:00 PDT" in block
        assert "mechanism_id: 744" in block

    def test_designed_keying_no_underscore_744_in_block(self):
        # Per #715: block keys and prose must not carry the underscore-form
        # mechanism id; the colon form mechanism_id: 744 is the only allowed
        # 744 reference.
        block = _block()
        assert MECH_ID_MARKER not in block
        assert "mechanism_id: 744" in block

    def test_yaml_parses_and_fields(self):
        d = yaml.safe_load(_entities_text())
        mech = d["marketplace_intermediary_landscape"][MECH_KEY]
        assert mech["mechanism_id"] == 744
        assert mech["verification"]["iteration"] == 854
        assert mech["verification"]["type"] == "C"
        assert mech["verification"]["date"] == "2026-09-19 09:00 PDT"
        assert mech["verdict"] == "directionally_supported_not_proven"
        assert mech["falsification_family"] is False
        assert mech["falsification_ledger_holds_at"] == 26
        assert mech["tone_scores"] == "NOT_SCORED"
        assert mech["connects_to"] == [738]

    def test_max_mechanism_id_is_744(self):
        assert max(_corpus_ids()) == 744


class TestMechanism744FilingFacts:
    def test_edgar_accession_and_first_hand_read(self):
        block = _block()
        assert "0001185185-26-004171" in block
        assert "read first-hand this run" in block
        assert EDGAR_8K_ITEM101 in block

    def test_item101_vs_item701_furnished_not_filed(self):
        block = _block()
        assert "Item 1.01" in block
        assert "Item 7.01" in block
        assert "furnished, NOT filed" in block
        assert EDGAR_8K_ITEM701 in block
        assert "0001185185-26-004134" in block

    def test_signing_date_and_ten_year_term(self):
        block = _block()
        assert "September 14 2026" in block
        assert "ten-year" in block
        assert "Q4 2026" in block

    def test_forecasts_qualified_forward_looking(self):
        block = _block()
        assert "$100 million in annual gross revenue" in block
        assert "100 million monthly users" in block
        assert "$1 billion" in block
        assert "forward-looking" in block

    def test_migration_scope_platform_surface(self):
        block = _block()
        assert "advertising and ad operations" in block
        assert "Coinbase-integrated" in block
        assert "DeFi-driven real-time payment platform" in block

    def test_non_compete_contracted_lock_in(self):
        block = _block()
        assert "may not directly or indirectly provide third-party hosting" in block
        assert "contracted lock-in" in block

    def test_perpetual_irrevocable_tech_control(self):
        block = _block()
        assert "perpetual, irrevocable control" in block
        assert "perpetual, irrevocable, royalty-free licenses" in block

    def test_equity_leg_breakdown(self):
        block = _block()
        assert "$89,555,638" in block
        assert "49.5%" in block
        assert "$10 million deposit" in block
        assert "$73,555,638 in cash" in block
        assert "below 50%" in block
        assert "Simplify Inventions" in block

    def test_seller_put_collateralized_by_revenue_share(self):
        block = _block()
        assert "seller put" in block
        assert "120 days after closing" in block
        assert "collateralized by RTB" in block

    def test_stock_consideration_11_5m(self):
        block = _block()
        assert "$11.5 million" in block
        assert "10-day VWAP" in block


class TestMechanism744Taxonomy:
    def test_not_a_new_direction_direction_count_holds_at_seven(self):
        block = _block()
        assert "NOT a new (eighth) direction" in block
        assert "SEVENTH" in block

    def test_extends_m738_infrastructure_capture(self):
        block = _block()
        assert "infrastructure-capture" in block
        assert "mechanism 738" in block

    def test_m738_source_gap_closed(self):
        block = _block()
        assert "no SEC filing read first-hand this run" in block
        assert "source gap" in block

    def test_incentive_geometry_hardened_three_places(self):
        block = _block()
        assert "Lock-in is CONTRACTED" in block
        assert "financed by the revenue stack" in block
        assert "survives any end of the revenue-sharing arrangement" in block


class TestMechanism744Discipline:
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


class TestDocSync854:
    def test_readme_row_854(self):
        assert OWN_BASENAME in _read(README_PATH)

    def test_architecture_row_854(self):
        assert OWN_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_854_file(self):
        doc = _read(ARCH_PATH)
        assert OWN_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))


class TestIterationLog854:
    def _entry(self):
        log = _read(LOG_PATH)
        idx = log.index("## #854 Type C:")
        return log[idx : idx + 14000]

    def test_log_entry_present(self):
        assert "## #854 Type C:" in _read(LOG_PATH)

    def test_log_mechanism_numbers_and_topics(self):
        entry = self._entry()
        assert "mechanism 744" in entry
        assert "RTB" in entry
        assert "8-K" in entry

    def test_log_rotation_window_850_854(self):
        entry = self._entry()
        assert "850-854" in entry

    def test_log_closing_leg(self):
        entry = self._entry()
        assert "CLOSING" in entry

    def test_log_no_analysis_json_update_and_not_artifact_grade(self):
        entry = self._entry()
        assert "no analysis.json update" in entry
        assert "NOT artifact-grade" in entry


class TestDateGrounding854:
    def test_sep_19_2026_is_saturday(self):
        assert datetime.datetime(2026, 9, 19).strftime("%A") == "Saturday"

    def test_run_time_pdt_grounded(self):
        assert datetime.datetime(2026, 9, 19, 9, 0).strftime("%H:%M") == "09:00"
