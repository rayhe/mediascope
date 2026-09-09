"""Type C #629: Anthropic $1.5B settlement distribution-phase payout fight.

FIRST dedicated distribution-phase mechanism in the corpus (mechanism_id 612,
next free pre-commit; max numeric mechanism_id was 611). Built from the Sep 6
2026 TechCrunch piece by Anthony Ha (weekend editor), read first-hand via
browser.open this run:

- Settlement terms: nearly 500,000 titles, $3,000 per pirated work; 50-50
  author/publisher split if still in print with a traditional publisher;
  100 percent to the author if self-published or rights reverted. Final
  approval in July (corpus author_settlement_detail: Jul 20 2026, Judge
  Araceli Martinez-Olguin). Payments moving forward circa Aug 10 2026 in up
  to 3 installments.
- Named example: April Henry (mystery/thriller author) says HarperCollins
  claimed a book reverted at least 17 years ago, plus a credit alert adding
  HarperCollins as her employer (which they never were).
- Writers Beware (Victoria Strauss): two complaint categories (reverted-rights
  claims; 100 percent claims where 50 percent owed); reluctant to attribute to
  malice what poor recordkeeping explains; systemic-pattern flag from two days
  of identical-error reports.
- Authors Guild CEO Mary Rasenberger to NYT: not a grab by the publishers;
  predictable result of bad recordkeeping and a confusing settlement process.
- Literary agencies also claiming (Strauss: agents are not rightsholders);
  Courtney Milan (pen name of Heidi Bond) blunt Bluesky post.
- Dispute mechanics: reversion must predate Aug 10 2022 (the download date)
  for a 100 percent author claim.

Financial-incentive mapping: the 50-50 rule converts each in-print work into
a circa $1,500 publisher claim, a standing incentive to claim broadly; the
voluntary comparator is HarperCollins-Microsoft $5,000/title ($2,500/$2,500,
mechanism 524, Nov 2024); News Corp Thomson Feb 5 2026 Q2 call expectation
("we and our authors at HarperCollins naturally expect to receive our fair
share of that payout") materialized as the Sep 2026 claims fight.

Theory prediction: involuntary litigation payout in the adversarial direction
(Anthropic pays under court order after a shadow-library piracy finding),
predicts NO coverage softening. Falsification-family BOUNDARY member, not a
pin. No coverage-tone claim. tone_scores NOT_SCORED; p_value/cohens_d
NOT_CALCULATED; is_significant False (Aug 28 standing rule).

Rotation: Type C follows Type B (#628) per A,B,C,D,E. Rotation guard
deselected pre-commit per the #565 followup convention; anchor patched in
the followup commit once the main commit SHA is known.
"""

import ast
import glob
import os
import re
import subprocess

import pytest
import yaml

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENTITIES_PATH = os.path.join(REPO_ROOT, "profiles", "competitor-entities.yaml")
README_PATH = os.path.join(REPO_ROOT, "README.md")
ARCH_PATH = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")
TESTS_DIR = os.path.join(REPO_ROOT, "tests")
LOG_PATH = os.path.join(REPO_ROOT, "iteration-log.md")

MECH_KEY = "anthropic_settlement_distribution_phase_payout_fight_629"
FILENAME = "test_type_c_629_anthropic_settlement_distribution_payout_fight_sep09_8am.py"

TECHCRUNCH_URL = "https://techcrunch.com/2026/09/06/authors-push-back-as-publishers-and-agents-seek-share-of-anthropic-settlement/"


def _entities():
    with open(ENTITIES_PATH) as f:
        return yaml.safe_load(f)


def _mechanism():
    anth = _entities()["entities"]["anthropic"]
    assert MECH_KEY in anth, f"{MECH_KEY} missing from anthropic entity"
    return anth[MECH_KEY]


def _block_text():
    raw = open(ENTITIES_PATH, encoding="utf-8").read()
    start = raw.index(MECH_KEY)
    end = raw.index("  amazon:")
    return raw[start:end]


def _count_def_tests():
    path = os.path.join(TESTS_DIR, FILENAME)
    tree = ast.parse(open(path).read())
    return sum(
        isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))
        and n.name.startswith("test_")
        for n in ast.walk(tree)
    )


def read_readme():
    with open(README_PATH) as f:
        return f.read()


def read_arch():
    with open(ARCH_PATH) as f:
        return f.read()


class TestIterationMetadata629:
    def test_iteration_number(self):
        assert _mechanism()["iteration"] == 629

    def test_mechanism_id_next_free(self):
        assert _mechanism()["mechanism_id"] == 612

    def test_mechanism_id_unique_repo_wide(self):
        seen = {}
        for path in glob.glob(os.path.join(REPO_ROOT, "profiles", "**", "*.yaml"), recursive=True):
            text = open(path, encoding="utf-8", errors="replace").read()
            for m in re.finditer(r"mechanism_id:\s*(\d+)", text):
                mid = int(m.group(1))
                seen.setdefault(mid, []).append(path)
        assert len(seen[612]) == 1, f"mechanism_id 612 not unique: {seen[612]}"

    def test_rotation_type_c(self):
        assert _mechanism()["rotation"] == "Type C"

    def test_scheduled_job_id(self):
        assert _mechanism()["job_id"] == "mediascope-daily-iteration"

    def test_goal_id(self):
        assert _mechanism()["goal_id"] == "goal_54093bda4145"


class TestSettlementTerms629:
    def test_settlement_amount_1_5b(self):
        assert "$1.5B" in _mechanism()["mechanism_name"]

    def test_per_work_3000(self):
        assert "$3,000" in _mechanism()["distribution_mechanics"]["per_work_amount"]

    def test_works_on_list_482460(self):
        assert "482,460" in _mechanism()["distribution_mechanics"]["per_work_amount"]

    def test_in_print_split_50_50(self):
        assert "50-50" in _mechanism()["distribution_mechanics"]["in_print_split"]

    def test_reverted_100_percent_author(self):
        assert "100 percent" in _mechanism()["distribution_mechanics"]["reverted_or_self_published"]

    def test_final_approval_jul_20_2026(self):
        assert "Jul 20 2026" in _mechanism()["distribution_mechanics"]["final_approval"]

    def test_download_date_cutoff_aug_10_2022(self):
        assert "August 10, 2022" in _mechanism()["distribution_mechanics"]["download_date_cutoff"]


class TestTechCrunchPiece629:
    def test_url_verbatim(self):
        assert _mechanism()["sources"][0] == TECHCRUNCH_URL

    def test_url_https(self):
        assert TECHCRUNCH_URL.startswith("https://techcrunch.com/2026/09/06/")

    def test_piece_date_sep_6_2026(self):
        assert "Sep 6 2026" in _mechanism()["overview"]

    def test_author_anthony_ha(self):
        assert "Anthony Ha" in _mechanism()["overview"]

    def test_april_henry_named(self):
        assert "April Henry" in _mechanism()["overview"]

    def test_henry_17_years_reverted(self):
        assert "17 years" in _mechanism()["overview"]

    def test_henry_employer_credit_alert(self):
        assert "credit alert" in _mechanism()["overview"]

    def test_strauss_two_categories(self):
        assert "two complaint categories" in _mechanism()["overview"]

    def test_strauss_systemic_quote(self):
        assert "widespread and systemic" in _mechanism()["overview"]

    def test_rasenberger_not_a_grab(self):
        assert "not see this as" in _mechanism()["overview"]

    def test_milan_bluesky(self):
        assert "Courtney Milan" in _mechanism()["overview"]
        assert "Heidi Bond" in _mechanism()["overview"]


class TestClaimCategories629:
    def test_three_categories(self):
        assert len(_mechanism()["claim_categories"]) == 3

    def test_reverted_rights_category(self):
        cats = " ".join(_mechanism()["claim_categories"])
        assert "Reverted-rights claims" in cats

    def test_share_inflation_category(self):
        cats = " ".join(_mechanism()["claim_categories"])
        assert "Share inflation" in cats

    def test_agency_category(self):
        cats = " ".join(_mechanism()["claim_categories"])
        assert "Non-rightsholder claims" in cats


class TestRecordkeepingVsStrategy629:
    def test_strauss_position_present(self):
        assert "recordkeeping" in _mechanism()["recordkeeping_vs_strategy"]["strauss_position"]

    def test_rasenberger_position_present(self):
        assert "recordkeeping" in _mechanism()["recordkeeping_vs_strategy"]["rasenberger_position"]

    def test_status_unresolved(self):
        assert "Unresolved" in _mechanism()["recordkeeping_vs_strategy"]["status"]


class TestFinancialIncentiveMapping629:
    def test_publisher_claim_value_1500(self):
        fim = _mechanism()["financial_incentive_mapping"]
        assert "$1,500" in fim["publisher_claim_value"]

    def test_over_claim_arbitrage(self):
        fim = _mechanism()["financial_incentive_mapping"]
        assert "profitable unless disputed" in fim["over_claim_arbitrage"]

    def test_voluntary_comparator_5k(self):
        fim = _mechanism()["financial_incentive_mapping"]
        assert "$5,000" in fim["voluntary_comparator"]
        assert "mechanism 524" in fim["voluntary_comparator"]

    def test_voluntary_comparator_split(self):
        fim = _mechanism()["financial_incentive_mapping"]
        assert "$2,500" in fim["voluntary_comparator"]

    def test_news_corp_thomson_quote(self):
        fim = _mechanism()["financial_incentive_mapping"]
        assert "Feb 5 2026" in fim["news_corp_angle"]
        assert "fair share" in fim["news_corp_angle"]

    def test_harpercollins_named_over_claimer(self):
        fim = _mechanism()["financial_incentive_mapping"]
        assert "named over-claimer" in fim["news_corp_angle"]
        assert "reported not adjudicated" in fim["news_corp_angle"]


class TestTheoryPrediction629:
    def test_direction_adversarial_involuntary(self):
        tp = _mechanism()["theory_prediction"]
        assert "involuntary" in tp["direction"].lower()

    def test_predicts_no_softening(self):
        tp = _mechanism()["theory_prediction"]
        assert "NO coverage softening" in tp["prediction"]

    def test_falsification_boundary_member_not_pin(self):
        tp = _mechanism()["theory_prediction"]
        assert "Boundary member, not a new pin" in tp["falsification_family"]

    def test_tone_not_scored(self):
        assert _mechanism()["tone_scores"] == "NOT_SCORED"

    def test_no_p_value(self):
        assert "NOT_CALCULATED" in _mechanism()["statistical_discipline"]

    def test_is_significant_false(self):
        assert "is_significant False" in _mechanism()["statistical_discipline"]


class TestConfounders629:
    def test_four_confounders(self):
        assert len(_mechanism()["confounders"]) == 4

    def test_strong_single_author_allegation(self):
        confs = " ".join(_mechanism()["confounders"])
        assert "single-author allegation" in confs

    def test_strong_recordkeeping_consensus(self):
        confs = " ".join(_mechanism()["confounders"])
        assert "not strategy" in confs

    def test_moderate_lawful_50_percent(self):
        confs = " ".join(_mechanism()["confounders"])
        assert "lawful 50 percent" in confs

    def test_weak_single_outlet(self):
        confs = " ".join(_mechanism()["confounders"])
        assert "Single-outlet primary reporting" in confs

    def test_cautious_language_required(self):
        assert _mechanism()["cautious_language_required"] is True


class TestSourcesAndHygiene629:
    def test_sources_verbatim_url(self):
        srcs = _mechanism()["sources"]
        assert len(srcs) == 1
        assert srcs[0] == TECHCRUNCH_URL

    def test_no_em_dashes_in_block(self):
        assert "\u2014" not in _block_text(), "em dash found in mechanism block"

    def test_ascii_only_block(self):
        bad = [c for c in _block_text() if ord(c) > 127]
        assert not bad, f"non-ascii chars in block: {bad[:5]}"

    def test_research_method_mentions_novelty_greps(self):
        assert "mechanism_id 612 next free (max 611)" in _mechanism()["research_method"]

    def test_novelty_five_firsts(self):
        nov = _mechanism()["novelty"]
        assert nov.count("FIRST") >= 5, f"expected 5 FIRST claims, got: {nov[:200]}"

    def test_no_coverage_tone_claim(self):
        assert _mechanism()["no_coverage_tone_claim"] is True

    def test_correlational_note_present(self):
        assert "No causal claim" in _mechanism()["correlational_note"]


class TestRotationCycleGuard629:
    """Rotation guard, deselected pre-commit per the #565 followup convention.

    Asserts the post-commit anchor, so it runs green only in the followup
    commit after the main commit SHA is known. Pre-commit it is deselected.
    """

    def _mains(self):
        out = subprocess.run(
            ["git", "log", "--format=%s"],
            cwd=str(REPO_ROOT),
            capture_output=True,
            text=True,
            check=True,
        ).stdout.splitlines()
        mains = [s for s in out if re.match(r"^Type [A-E] #\d+:", s)]
        assert len(mains) >= 5
        return mains

    def test_window_625_629_closes_d_to_c(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m, f"unparseable rotation subject: {s!r}"
            observed.append((m.group(1), m.group(2)))
        assert observed == [
            ("C", "629"),
            ("B", "628"),
            ("A", "627"),
            ("E", "626"),
            ("D", "625"),
        ], f"rotation window 625-629 wrong: {observed}"

    def test_rotation_adjacency_cycle_valid(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m
            observed.append(m.group(1))
        assert observed == ["C", "B", "A", "E", "D"]
        order = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
        for a, b in zip(observed, observed[1:]):
            assert (order[a] - order[b]) % 5 == 1, (
                f"rotation broken: {a} -> {b} is not a valid cycle edge"
            )

    def test_anchor_is_main_patch_in_followup(self):
        # Post-commit anchor: the #629 main commit. Patched in the followup
        # per the #565 convention once the main commit SHA is known.
        out = subprocess.run(
            ["git", "log", "--format=%H %s"],
            cwd=str(REPO_ROOT),
            capture_output=True,
            text=True,
            check=True,
        ).stdout.splitlines()
        mains = [
            l for l in out if re.match(r"^[0-9a-f]{40} Type [A-E] #\d+:", l)
        ]
        sha, subject = mains[0].split(" ", 1)
        assert sha.startswith("PATCH_IN_FOLLOWUP"), f"anchor drifted: {sha}"
        assert subject.startswith("Type C #629:"), (
            f"post-commit anchor broken: newest main is not #629: {subject!r}"
        )


class TestDocSyncRatchet629:
    def test_readme_has_629_row(self):
        assert re.search(r"#629", read_readme()), "README.md missing the #629 test-table row"

    def test_arch_has_629_row(self):
        assert re.search(r"#629", read_arch()), "docs/ARCHITECTURE.md missing the #629 tree row"

    def test_prior_rows_intact(self):
        readme, arch = read_readme(), read_arch()
        for n in ("624", "625", "626", "627", "628"):
            assert re.search(rf"#{n}", readme), f"README.md lost the #{n} row"
            assert re.search(rf"#{n}", arch), f"docs/ARCHITECTURE.md lost the #{n} row"

    def test_readme_row_test_count_matches(self):
        m = re.search(rf"`{re.escape(FILENAME)}`\s*\|\s*(\d+)\s*\|", read_readme())
        assert m, "README #629 row missing or malformed"
        assert int(m.group(1)) == _count_def_tests(), (
            f"README row says {m.group(1)} but file carries {_count_def_tests()}"
        )

    def test_readme_row_says_629(self):
        line = next(
            (ln for ln in read_readme().splitlines() if FILENAME in ln),
            None,
        )
        assert line is not None, "README missing the #629 row entirely"
        assert "#629" in line, "README #629 row does not mention #629"
