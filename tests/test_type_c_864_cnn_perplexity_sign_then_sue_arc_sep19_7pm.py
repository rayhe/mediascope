"""Type C #864 (860-864 window, fifth leg D->E->A->B->C, CLOSING the window):
CNN x Perplexity sign-then-sue arc - Comet Plus revenue-share launch
partner (Oct/Nov 2025) sues the SAME AI lab for copyright infringement
(S.D.N.Y. 1:26-cv-04427, filed May 28 2026). FIRST dedicated corpus
mechanism (mechanism 750) of a publisher suing the same AI lab it had
signed a revenue-share deal with. Sequence: CNN signs as Comet Plus
launch partner (Press Gazette: CNN, Conde Nast, Fortune, LA Times, WaPo
in the US; Le Monde and Le Figaro in France; 80% of Comet Plus revenue
to publishers, allocated by human visits, search citations, agent
actions) -> late 2024/early 2025 licensing negotiations collapse (no
terms incl. bot-access restrictions) -> Dec 10 2025 cease-and-desist
to Perplexity Head of Legal Nathan Barksdale (no response) -> early
2026 CNN blocks PerplexityBot (alleged continued access via
third-party hosts) -> May 28 2026 suit: Cable News Network, Inc. v.
Perplexity AI, Inc., S.D.N.Y. No. 1:26-cv-04427, 54-page complaint,
17,000+ works, input-stage + output-stage infringement, trademark
dilution (15 U.S.C. 1125) and infringement (15 U.S.C. 1114), seeking
injunction, statutory damages (up to $150K per willful work; ~$2.5B
theoretical), actual/treble damages, restitution, attorneys' fees.
Perplexity: "You can't copyright facts" (Jesse Dwyer). CNN remains
open to "sensible licensing arrangements"; existing AI partnerships
incl. Meta (Dec 2025). Status LIVE as of Sep 2026 (bounded absence of
settlement/motion/ruling reporting per iteration-492). Analytical
framing: INVERTS mechanism 609's sue-then-sign arc (Indian Express
sought to join anti-OpenAI suit Feb 2025, signed OpenAI Sep 2026);
REPLICATES mechanism 675's grant-then-sue finding (money did not buy
litigation immunity); COMPLEMENTS mechanism 663's sign-one-sue-other
bifurcation (same-counterparty sign-AND-sue is the stronger form);
same-counterparty precedent Dow Jones/NY Post v. Perplexity
1:24-cv-07984-KPF (MTD denied Aug 21 2025). Analyst quote: Lisk
(Medium): "Perplexity points to its publisher revenue-sharing program
as evidence of good faith; the publishers suing it have called that
program inadequate compensation offered after the taking." Financial
reading: 80/20 share was structurally insufficient consideration to
resolve the dispute; revenue-share buys a payment rail, not a covenant
not to sue. MANUAL qualitative only, engine NOT run,
p_value/cohens_d/ci_95 NOT_CALCULATED, is_significant False, verdict
directionally_supported_not_proven; NOT falsification-family, ledger
holds at 26; no analysis.json update. Novelty verified pre-commit
(zero test_type_c_864 files; no 'Type C #864' in git log; max numeric
mechanism_id 749; zero underscore-form 750 keys by designed keying per
#715; block key zero-hit; zero dedicated CNN x Perplexity mechanisms
pre-commit - only m391's unnamed Comet Plus partner roster and m663's
passing "Conde Nast/CNN suits" mention; case number 1:26-cv-04427
zero-hit repo-wide; all 8 source URLs zero-hit repo-wide); 860-864
window fifth leg D->E->A->B->C CLOSING it (anchor patched post-commit
per #565) - Sep 19 2026 19:00 PDT.
"""

import os
import re
import subprocess
import datetime

import pytest
import yaml

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
TESTS_DIR = os.path.join(REPO_ROOT, "tests")
OWN_BASENAME = "test_type_c_864_cnn_perplexity_sign_then_sue_arc_sep19_7pm.py"
MECH_KEY = "cnn_perplexity_sign_then_sue_arc_sep2026"
M_ID = 750
ITER = 864
TYPE_LETTER = "C"
# Concatenated so this file never contains the literal marker itself.
MECH_ID_MARKER = "mechanism" + "_750"
NEXT_ID_MARKER = "mechanism" + "_751"
NEXT_ID_NUMERIC = "mechanism_id: " + "751"
EXPECTED_ORDER = [("D", "860"), ("E", "861"), ("A", "862"), ("B", "863"), ("C", "864")]
# Patched to the real main-commit SHA in the anchor followup per the #565 convention.
ANCHORED_SHA = "PATCH_ME_IN_FOLLOWUP"

PRESSGAZETTE_URL = "https://pressgazette.co.uk/newsletters/perplexitys-comet-browser-assistant-goes-free-for-all-with-publisher-pay-up/"
COURTLISTENER_URL = "https://www.courtlistener.com/recap/gov.uscourts.nysd.664916/gov.uscourts.nysd.664916.1.0.pdf"
PPCLAND_URL = "https://ppc.land/cnn-sues-perplexity-for-copying-17-000-works-in-landmark-ai-copyright-case/"
ACCELERATEIP_URL = "https://accelerateip.com/cnn-v-perplexity-ai-what-the-lawsuit-means-for-your-business-and-your-content/"
BGOV_URL = "https://news.bgov.com/crypto/cnn-latest-news-outlet-to-sue-perplexity-ai-over-data-scraping"
MARKETINGINTERACTIVE_URL = "https://www.marketing-interactive.com/cnn-reportedly-sues-perplexity-over-alleged-ai-copyright-infringement"
DECISIONLAW_URL = "https://decisionandlaw.com/news/cnn-v-perplexity-ai-skip-links-fair-use-rag"
MEDIUM_URL = "https://medium.com/@jacq.lisk82/the-answer-engine-on-trial-11e2f83129f4"

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
    end = text.index("\n  srmg_pif_pmc_dual_revenue_anti_meta_mechanism_422:")
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
    out = _git("log", "--all", "--format=%H %s", "--grep", "Type C #864")
    mains = {}
    for line in out.splitlines():
        if not line.strip():
            continue
        sha, _, subject = line.partition(" ")
        if "Type C #864" in subject and qualifier in subject:
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


class TestNovelty864:
    def test_single_test_type_c_864_file(self):
        files = [
            fn
            for fn in os.listdir(TESTS_DIR)
            if fn.startswith("test_type_c_864")
        ]
        assert files == [OWN_BASENAME], files

    def test_type_c_864_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per #565 (the #864 main commit does not
        # exist yet); patched green in the anchor followup.
        mains = _git_log_mains("CNN x Perplexity")
        assert len(mains) == 1, mains
        assert ANCHORED_SHA in mains, mains

    def test_novelty_verification_claim(self):
        # The docstring novelty claim must be honest: no dedicated
        # CNN x Perplexity mechanism existed pre-commit.
        hits = _repo_grep(MECH_KEY, roots=("profiles",))
        assert hits == ["profiles/competitor-entities.yaml"], hits

    def test_860_864_window_legs_present_prior_to_864(self):
        # Deselected pre-commit per #565; patched green in the followup.
        for fn in (
            "test_type_d_860_",
            "test_type_e_861_",
            "test_type_a_862_",
            "test_type_b_863_",
        ):
            matches = [f for f in os.listdir(TESTS_DIR) if f.startswith(fn)]
            assert len(matches) == 1, (fn, matches)


class TestRotationGuard864:
    """#864 is the Type C fifth leg of window 860-864: D->E->A->B->C, CLOSING it."""

    ORDER = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}

    def test_window_is_860_864_fifth_leg(self):
        # Deselected pre-commit per #565 (the #864 main commit does not
        # exist yet); patched green in the anchor followup.
        window = _window()
        assert window[: len(EXPECTED_ORDER)] == EXPECTED_ORDER, (
            f"860-864 window fifth leg D->E->A->B->C: expected {EXPECTED_ORDER}, "
            f"got {window[: len(EXPECTED_ORDER)]}"
        )

    def test_rotation_adjacency_cycle_valid(self):
        # Deselected pre-commit per #565; patched green in the followup.
        window = _window()
        for (t1, n1), (t2, n2) in zip(window, window[1:]):
            assert int(n1) == int(n2) + 1
            assert (self.ORDER[t1] - self.ORDER[t2]) % 5 == 1, (t1, t2)

    def test_predecessor_is_type_b_863(self):
        # Deselected pre-commit per #565; patched green in the followup.
        window = _window()
        assert window[1] == ("B", "863"), (
            f"immediate predecessor must be Type B #863, got {window[1]}"
        )

    def test_anchor_sha_matches_head(self):
        # Patched to the real main-commit SHA in the anchor followup per
        # the #565 convention; deselected pre-commit at the pytest CLI.
        mains = _git_log_mains("CNN x Perplexity")
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ), mains
        newest_sha = next(iter(mains))
        assert newest_sha == ANCHORED_SHA, mains


class TestMechanism750Structure:
    def test_block_key_exists_in_competitor_entities(self):
        assert MECH_KEY in _entities_text()

    def test_block_key_unique(self):
        assert _entities_text().count(MECH_KEY) == 1

    def test_block_nests_under_perplexity_entity(self):
        entities = yaml.safe_load(_entities_text())
        px = entities["entities"]["perplexity"]
        assert MECH_KEY in px, list(px.keys())

    def test_iteration_and_type_and_time_pdt(self):
        block = _block()
        assert "iteration: 864" in block
        assert "iteration_type: C" in block
        assert "rotation: 'Type C'" in block
        assert "date_analyzed: '2026-09-19'" in block
        assert "time_pdt: '19:00'" in block
        assert "job_id: mediascope-daily-iteration" in block
        assert "goal_id: goal_54093bda4145" in block

    def test_designed_keying_no_underscore_750_in_block(self):
        # Per the #715 convention, the block key carries no
        # underscore-form "mechanism_750" marker.
        assert NEXT_ID_MARKER not in _block().replace(MECH_KEY, "")
        assert MECH_ID_MARKER not in _block().replace(MECH_KEY, "")

    def test_yaml_parses_and_fields(self):
        entities = yaml.safe_load(_entities_text())
        b = entities["entities"]["perplexity"][MECH_KEY]
        assert b["mechanism_id"] == 750
        assert b["type"] == "financial_incentive_mapping"
        assert len(b["source_urls"]) == 8

    def test_max_mechanism_id_is_750(self):
        ids = _corpus_ids()
        assert max(ids) == 750, max(ids)
        assert ids.count(750) == 1

    def test_no_751_anywhere(self):
        assert NEXT_ID_NUMERIC not in _entities_text()


class TestMechanism750DealFacts:
    def test_comet_plus_launch_partner_cnn(self):
        block = _fold(_block())
        assert "cnn" in block
        assert "comet plus" in block
        assert "80" in block and "publisher" in block

    def test_case_number_and_filing_date(self):
        block = _block()
        assert "1:26-cv-04427" in block
        assert "May 28 2026" in block
        assert "Southern District of New York" in block

    def test_seventeen_thousand_works(self):
        block = _block()
        assert "17,000" in block

    def test_input_stage_and_output_stage(self):
        block = _fold(_block())
        assert "input" in block and "output" in block
        assert "perplexitybot" in block

    def test_trademark_counts(self):
        block = _block()
        assert "15 U.S.C. 1125" in block
        assert "15 U.S.C. 1114" in block

    def test_statutory_damages_exposure(self):
        block = _block()
        assert "$150,000" in block
        assert "$2.5B" in block

    def test_negotiation_collapse_and_cease_and_desist(self):
        block = _block()
        assert "Dec 10 2025" in block
        assert "Nathan Barksdale" in block
        assert "cease-and-desist" in block

    def test_bot_block_early_2026(self):
        block = _fold(_block())
        assert "blocks perplexitybot" in block or "blocked perplexitybot" in block

    def test_perplexity_response_quote(self):
        block = _block()
        assert "You can''t copyright facts" in block or "You can't copyright facts" in block

    def test_cnn_open_to_licensing_and_meta_partnership(self):
        block = _fold(_block())
        assert "sensible licensing arrangements" in block
        assert "meta" in block

    def test_suit_live_bounded_absence(self):
        block = _fold(_block())
        assert "live as of sep 2026" in block
        assert "bounded absence" in block

    def test_all_eight_source_urls_in_block(self):
        block = _block()
        for url in (
            PRESSGAZETTE_URL,
            COURTLISTENER_URL,
            PPCLAND_URL,
            ACCELERATEIP_URL,
            BGOV_URL,
            MARKETINGINTERACTIVE_URL,
            DECISIONLAW_URL,
            MEDIUM_URL,
        ):
            assert url in block, url


class TestMechanism750Taxonomy:
    def test_inverts_m609_sue_then_sign(self):
        block = _fold(_block())
        assert "609" in block
        assert "sue-then-sign" in block
        assert "indian express" in block

    def test_replicates_m675_grant_then_sue(self):
        block = _fold(_block())
        assert "675" in block
        assert "grant-then-sue" in block

    def test_complements_m663_bifurcation(self):
        block = _fold(_block())
        assert "663" in block
        assert "sign-one-sue-other" in block

    def test_dow_jones_precedent_cited(self):
        block = _block()
        assert "1:24-cv-07984" in block
        assert "Aug 21 2025" in block

    def test_analyst_quote_lisk(self):
        block = _block()
        assert "inadequate compensation offered after the taking" in block

    def test_financial_incentive_reading_present(self):
        block = _fold(_block())
        assert "payment rail, not a covenant not to sue" in block

    def test_first_dedicated_mechanism_claim(self):
        block = _fold(_block())
        assert "first dedicated corpus mechanism" in block


class TestMechanism750Discipline:
    def test_p_value_not_calculated(self):
        assert "p_value: not_calculated" in _block()

    def test_cohens_d_not_calculated(self):
        assert "cohens_d: not_calculated" in _block()

    def test_ci_95_not_calculated(self):
        assert "ci_95: not_calculated" in _block()

    def test_discipline_note_statistical_guards(self):
        block = _fold(_block())
        assert "manual qualitative only" in block
        assert "is_significant: false" in _block()

    def test_verdict_and_correlation_note(self):
        block = _fold(_block())
        assert "directionally supported not proven" in block
        assert "no causal claim" in block

    def test_financial_incentive_documentation_leg(self):
        block = _fold(_block())
        assert "financial relationships are correlational structural incentives" in block

    def test_falsification_ledger_holds_at_26(self):
        assert "falsification_ledger_holds_at: 26" in _block()

    def test_no_analysis_json_update(self):
        block = _fold(_block())
        assert "no analysis json update" in block

    def test_not_artifact_grade(self):
        assert "not_artifact_grade: true" in _block()

    def test_press_gazette_excerpt_bounded_caveat(self):
        block = _fold(_block())
        assert "excerpt-bounded" in block


class TestDocSync864:
    def test_readme_row_864(self):
        assert OWN_BASENAME in _read(README_PATH)

    def test_architecture_row_864(self):
        assert OWN_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_864_file(self):
        doc = _read(ARCH_PATH)
        assert OWN_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))


class TestIterationLog864:
    def _entry(self):
        log = _read(LOG_PATH)
        idx = log.index("## #864 Type C:")
        return log[idx : idx + 14000]

    def test_log_entry_present(self):
        assert "## #864 Type C:" in _read(LOG_PATH)

    def test_log_mechanism_numbers_and_topics(self):
        entry = self._entry()
        assert "mechanism 750" in entry
        assert "CNN" in entry
        assert "Perplexity" in entry

    def test_log_rotation_window_860_864(self):
        entry = self._entry()
        assert "860-864" in entry

    def test_log_closing_leg(self):
        entry = self._entry()
        assert "CLOSING" in entry

    def test_log_no_analysis_json_update_and_not_artifact_grade(self):
        entry = self._entry()
        assert "no analysis.json update" in entry
        assert "NOT artifact-grade" in entry


class TestDateGrounding864:
    def test_sep_19_2026_is_saturday(self):
        assert datetime.datetime(2026, 9, 19).strftime("%A") == "Saturday"

    def test_run_time_pdt_grounded(self):
        assert datetime.datetime(2026, 9, 19, 19, 0).strftime("%H:%M") == "19:00"
