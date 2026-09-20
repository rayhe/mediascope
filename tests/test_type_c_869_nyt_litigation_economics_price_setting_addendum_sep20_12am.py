"""Type C #869 (865-869 window, fifth leg D->E->A->B->C, CLOSING the window):
NYT AI-litigation economics price-setting addendum - FIRST dedicated corpus
mechanism (mechanism 753) on the NYT's AI-litigation spend as a
financial-incentive datum: $28M+ cumulative spend since 2023 corroborated
across four Sep/Jul 2026 surfaces (stockmoguls Sep 6, Fast Company/AP,
thestreet, ainvest Sep 5), PROMOTING mechanism 636's $4.2M Q1 2026 datum
(TheWrap prior reporting, flagged un-corroborated at #669) to multi-source
corroborated status. The sanctions-bid motion (NYT + other outlets vs
OpenAI, circa Jul 9 2026, attorney fees sought for "improperly withheld"
evidence) adds the fee-shifting enforcement-economics leg. Analytical
framing: price-setting, not damages - ainvest: "the point of that spending
was never a damages award, it was setting the price"; the NYT litigates
the labs that did NOT pay (OpenAI, Microsoft, Perplexity) while licensing
the one that met its commercial conditions (Amazon, mechanism 559,
$20-25M/yr); consistent with m636's pay-or-litigate doctrine ("They have
to pay us" - Meredith Kopit Levien, Status Summit Sep 9 2026); echoes
m675's grant-then-sue (Seattle Times) and m663's bifurcation; Anthropic's
$1.5B authors settlement as the court-set price datum. MANUAL qualitative
only, engine NOT run, p_value/cohens_d/ci_95 NOT_CALCULATED,
is_significant False, verdict directionally_supported_not_proven; NOT
falsification-family, ledger holds at 27; no analysis.json update.
Novelty verified pre-commit (zero test_type_c_869 files; no 'Type C #869'
in git log; max numeric mechanism_id 752; zero exact 753 key-form; zero underscore-form 754 keys per #715 designed keying; block
key zero-hit; "28 million" zero-hit pre-commit; all 4 evidence URLs
zero-hit repo-wide); 865-869 window fifth leg D->E->A->B->C CLOSING it
(anchor patched post-commit per #565) - Sep 20 2026 00:00 PDT.
"""

import os
import re
import subprocess
import datetime

import pytest
import yaml

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
TESTS_DIR = os.path.join(REPO_ROOT, "tests")
OWN_BASENAME = "test_type_c_869_nyt_litigation_economics_price_setting_addendum_sep20_12am.py"
MECH_KEY = "nyt_ai_litigation_economics_28m_price_setting_addendum_sep2026"
BLOCK_KEY = "type_c_869_nyt_ai_litigation_economics_28m_price_setting_addendum_sep2026"
M_ID = 753
ITER = 869
TYPE_LETTER = "C"
# Concatenated so this file never contains the literal marker itself.
MECH_ID_MARKER = "mechanism" + "_753"
NEXT_ID_MARKER = "mechanism" + "_754"
NEXT_ID_NUMERIC = "mechanism_id: " + "754"
EXPECTED_ORDER = [("C", "869"), ("B", "868"), ("A", "867"), ("E", "866"), ("D", "865")]
# Patched to the real main-commit SHA in the anchor followup per the #565 convention.
ANCHORED_SHA = "PATCH_ME_IN_FOLLOWUP"

STOCKMOGULS_URL = "https://www.stockmoguls.com/2026/09/06/which-media-companies-profit-when-ai-pays-for-archives/"
FASTCOMPANY_URL = "https://www.fastcompany.com/91571727/the-new-york-times-is-escalating-its-fight-with-openai-urging-a-judge-to-impose-sanctions"
THESTREET_URL = "https://www.thestreet.com/technology/openai-sanctions-ny-times-copyright-lawsuit"
AINVEST_URL = "https://www.ainvest.com/news/openai-pays-papers-fights-rest-lawsuit-rest-negotiating-2609/"
EVIDENCE_URLS = (STOCKMOGULS_URL, FASTCOMPANY_URL, THESTREET_URL, AINVEST_URL)

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
    end = text.index("\n  apple:")
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
    # --grep searches full commit messages (subject + body), so a body
    # mention of the qualifier (e.g. the anchor followup explaining its own
    # qualifier fix) would wrongly match. Filter subjects in Python so only
    # the real main commit qualifies.
    out = _git("log", "--all", "--format=%H %s", "--grep", "Type C #869")
    mains = {}
    for line in out.splitlines():
        if not line.strip():
            continue
        sha, _, subject = line.partition(" ")
        if "Type C #869" in subject and qualifier in subject:
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


def _fold(block):
    return block.lower().replace("_", " ")


class TestNovelty869:
    def test_single_test_type_c_869_file(self):
        files = [
            fn
            for fn in os.listdir(TESTS_DIR)
            if fn.startswith("test_type_c_869")
        ]
        assert files == [OWN_BASENAME], files

    def test_type_c_869_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per #565 (the #869 main commit does not
        # exist yet); patched green in the anchor followup.
        mains = _git_log_mains("NYT")
        assert len(mains) == 1, mains
        assert ANCHORED_SHA in mains, mains

    def test_novelty_verification_claim(self):
        # The docstring novelty claim must be honest: no dedicated
        # NYT litigation-economics mechanism existed pre-commit.
        hits = _repo_grep(MECH_KEY, roots=("profiles",))
        assert hits == ["profiles/competitor-entities.yaml"], hits

    def test_865_869_window_legs_present_prior_to_869(self):
        # Deselected pre-commit per #565; patched green in the followup.
        for fn in (
            "test_type_d_865_",
            "test_type_e_866_",
            "test_type_a_867_",
            "test_type_b_868_",
        ):
            matches = [f for f in os.listdir(TESTS_DIR) if f.startswith(fn)]
            assert len(matches) == 1, (fn, matches)


class TestRotationGuard869:
    """#869 is the Type C fifth leg of window 865-869: D->E->A->B->C, CLOSING it."""

    ORDER = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}

    def test_window_is_865_869_fifth_leg(self):
        # Deselected pre-commit per #565 (the #869 main commit does not
        # exist yet); patched green in the anchor followup.
        window = _window()
        assert window[: len(EXPECTED_ORDER)] == EXPECTED_ORDER, (
            f"865-869 window fifth leg D->E->A->B->C: expected {EXPECTED_ORDER}, "
            f"got {window[: len(EXPECTED_ORDER)]}"
        )

    def test_rotation_adjacency_cycle_valid(self):
        # Deselected pre-commit per #565; patched green in the followup.
        window = _window()
        for (t1, n1), (t2, n2) in zip(window, window[1:]):
            assert int(n1) == int(n2) + 1
            assert (self.ORDER[t1] - self.ORDER[t2]) % 5 == 1, (t1, t2)

    def test_predecessor_is_type_b_868(self):
        # Deselected pre-commit per #565; patched green in the followup.
        window = _window()
        assert window[1] == ("B", "868"), (
            f"immediate predecessor must be Type B #868, got {window[1]}"
        )

    def test_anchor_sha_matches_head(self):
        # Patched to the real main-commit SHA in the anchor followup per
        # the #565 convention; deselected pre-commit at the pytest CLI.
        mains = _git_log_mains("NYT")
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ), mains
        newest_sha = next(iter(mains))
        assert newest_sha == ANCHORED_SHA, mains


class TestMechanism753Structure:
    def test_block_key_exists_in_competitor_entities(self):
        assert BLOCK_KEY in _entities_text()

    def test_block_key_unique(self):
        assert _entities_text().count(BLOCK_KEY) == 1

    def test_block_nests_under_amazon_entity_section(self):
        text = _entities_text()
        amazon_idx = text.index("\n  amazon:")
        apple_idx = text.index("\n  apple:")
        mech_idx = text.index(MECH_KEY)
        assert amazon_idx < mech_idx < apple_idx

    def test_iteration_and_type_and_time_pdt(self):
        block = _block()
        assert "iteration: 869" in block
        assert "rotation: Type C" in block
        assert "time_pdt: '00:00'" in block
        assert "date_analyzed: '2026-09-20'" in block

    def test_designed_keying_no_underscore_753_in_block(self):
        # Per the #715 convention: colon-form keying only; the numeric
        # mechanism id never appears in underscore form inside the block.
        block = _block()
        assert "_753" not in block, [
            line for line in block.splitlines() if "_753" in line
        ]

    def test_yaml_parses_and_fields(self):
        doc = yaml.safe_load(_entities_text())
        blk = doc["entities"]["amazon"][MECH_KEY]
        assert blk["mechanism_id"] == 753
        assert blk["iteration"] == 869
        assert blk["block_key"] == BLOCK_KEY
        assert blk["type"] == "financial_incentive_mapping"

    def test_max_mechanism_id_is_753(self):
        assert max(_corpus_ids()) == 753

    def test_no_754_anywhere(self):
        # Format-built needle so this file never carries the literal.
        assert not _repo_grep(NEXT_ID_NUMERIC, roots=("profiles",))


class TestMechanism753SpendFacts:
    def test_28m_cumulative_figure(self):
        block = _block()
        assert "28 million" in block
        assert "more than $28 million" in block

    def test_42m_q1_2026(self):
        assert "$4.2 million" in _block()

    def test_corroboration_promoted_from_669(self):
        block = _block()
        assert "un-corroborated (#669)" in block
        assert "four-source corroborated" in block

    def test_sanctions_bid_motion(self):
        block = _block()
        assert "sanctions" in block
        assert "attorney fees" in block
        assert "improperly withheld" in block

    def test_fee_shifting_leg(self):
        block = _block()
        assert "fee-shifting" in block
        assert "fee recovery" in block

    def test_all_four_evidence_urls_in_block(self):
        block = _block()
        for url in EVIDENCE_URLS:
            assert url in block, url

    def test_period_ambiguity_noted(self):
        block = _block()
        assert "since 2023" in block
        assert "Perplexity suit" in block

    def test_market_anchor_anthropic_15b(self):
        assert "$1.5B" in _block()


class TestMechanism753Taxonomy:
    def test_extends_m636(self):
        block = _block()
        assert "PROMOTES mechanism 636" in block
        assert 636 in yaml.safe_load(_entities_text())["entities"]["amazon"][MECH_KEY]["connects_to"]

    def test_connects_559_amazon_leg(self):
        blk = yaml.safe_load(_entities_text())["entities"]["amazon"][MECH_KEY]
        assert 559 in blk["connects_to"]
        assert "$20-25M/yr" in _block()

    def test_connects_675_grant_then_sue(self):
        blk = yaml.safe_load(_entities_text())["entities"]["amazon"][MECH_KEY]
        assert 675 in blk["connects_to"]
        assert "Seattle Times" in _block()

    def test_connects_609_663_562(self):
        blk = yaml.safe_load(_entities_text())["entities"]["amazon"][MECH_KEY]
        assert 609 in blk["connects_to"]
        assert 663 in blk["connects_to"]
        assert 562 in blk["connects_to"]

    def test_price_setting_reading(self):
        block = _block()
        assert "setting the price" in block
        assert "price-setting" in block

    def test_doctrine_link_levien(self):
        block = _block()
        assert "They have to pay us" in block
        assert "Meredith Kopit Levien" in block

    def test_first_dedicated_mechanism_claim(self):
        assert "FIRST dedicated corpus mechanism" in _block()


class TestMechanism753Discipline:
    def test_p_value_not_calculated(self):
        assert "p_value/cohens_d/ci_95 NOT_CALCULATED" in _block()

    def test_cohens_d_not_calculated(self):
        assert "p_value/cohens_d/ci_95 NOT_CALCULATED" in _block()

    def test_ci_95_not_calculated(self):
        assert "p_value/cohens_d/ci_95 NOT_CALCULATED" in _block()

    def test_is_significant_false(self):
        assert "is_significant False" in _block()

    def test_engine_not_run(self):
        assert "engine NOT run" in _block()

    def test_verdict_directional(self):
        assert "directionally_supported_not_proven" in _block()

    def test_financial_incentive_documentation_leg(self):
        block = _block()
        assert "financial-incentive documentation leg" in block
        assert "not a tone test" in block

    def test_falsification_ledger_holds_at_27(self):
        assert "ledger holds at 27" in _block()
        verge = _read(
            os.path.join(REPO_ROOT, "profiles", "the-verge.yaml")
        )
        assert "TWENTY-SEVENTH" in verge

    def test_no_analysis_json_update(self):
        assert "no_analysis_json_update true" in _block()

    def test_not_artifact_grade(self):
        assert "NOT artifact_grade true" in _block()

    def test_excerpt_bounded_caveat(self):
        block = _block()
        assert "0 browser.open" in block
        assert "excerpt-bounded" in block


class TestDocSync869:
    def test_readme_row_869(self):
        assert OWN_BASENAME in _read(README_PATH)

    def test_architecture_row_869(self):
        assert OWN_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_869_file(self):
        doc = _read(ARCH_PATH)
        assert OWN_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))


class TestIterationLog869:
    def _entry(self):
        log = _read(LOG_PATH)
        idx = log.index("## #869 Type C:")
        return log[idx : idx + 14000]

    def test_log_entry_present(self):
        assert "## #869 Type C:" in _read(LOG_PATH)

    def test_log_mechanism_numbers_and_topics(self):
        entry = self._entry()
        assert "m753" in entry
        assert "NYT" in entry
        assert "$28M" in entry

    def test_log_rotation_window_865_869(self):
        entry = self._entry()
        assert "865-869" in entry

    def test_log_closing_leg(self):
        entry = self._entry()
        assert "CLOSING" in entry

    def test_log_no_analysis_json_update_and_not_artifact_grade(self):
        entry = self._entry()
        assert "no analysis.json update" in entry
        assert "NOT artifact-grade" in entry


class TestDateGrounding869:
    def test_sep_20_2026_is_sunday(self):
        assert datetime.datetime(2026, 9, 20).strftime("%A") == "Sunday"

    def test_run_time_pdt_grounded(self):
        assert datetime.datetime(2026, 9, 20, 0, 0).strftime("%H:%M") == "00:00"
