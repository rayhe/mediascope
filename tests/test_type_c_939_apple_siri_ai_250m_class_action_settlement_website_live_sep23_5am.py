"""Type C #939 (2026-09-23 05:00 PDT): Apple Siri AI delayed-launch $250M
class-action settlement - FIRST dedicated corpus mechanism mapping the
OBSERVABLE Siri-AI failure-cost leg: Apple's May 2026 agreement to pay $250
million to settle the U.S. false-advertising class action over the delayed
personalized Siri launch; settlement website live Sep 20 2026 (MacRumors,
first-hand read, 113 lines); claims window Sep 21-Dec 21 2026 at ~$25 per
eligible device (up to $95). The twin nine-figure leg to mechanisms 156/606's
publisher-content negotiation (Aug 12 2026 WSJ origin, variable pay-per-use,
nine-figure budget discussed, zero signed closures as of Sep 17 2026): the
settlement prices Apple's cost-of-failure; the negotiation prices Apple's
cost-of-content for the same Siri AI rebuild. Observable counterpart to
mechanism 792's sealed X Corp/SpaceXAI resolution (observable vs
unobservable pair).

Rotation window FIFTH leg: D (#935) -> E (#936) -> A (#937) -> B (#938) ->
C (#939), CLOSING the 935-939 window.

Evidence: 2 browser.search query sets this run + 1 browser.open first-hand
read (MacRumors Sep 20 2026, 113 lines, Joe Rossignol); rejected candidates
logged (Princeton UP x Cashmere m663-family, ANI v. OpenAI Sep 15 m717,
News Corp additional arrangements m630 watch, AWS AI Content Marketplace
in-corpus, Apple Siri publisher closures zero m606 watch). Statistical
discipline per the qualitative Type C convention: p_value/cohens_d/ci_95
NOT_CALCULATED, tone_scores NOT_SCORED, is_significant False, engine NOT
run; verdict directionally_supported_not_proven; NOT a falsification-family
member (ledger holds at 29, THIRTIETH remains the negative guard); no
analysis.json update.

Deselected pre-commit per the #565 convention: anchor 1 + rotation guard 3
(patched green in the anchor followup); iteration-log entry tests 2 fail by
design pre-commit, go green in the log-hash followup (the weekday check is
entry-independent and green pre-commit); doc-sync 3 green post-doc-sync.

Anchor placeholder: patched to the main commit SHA in the #565 follow-up.
"""

import os
import re
import subprocess
from pathlib import Path

import pytest

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TESTS_DIR = Path(REPO_ROOT) / "tests"
REPO = Path(REPO_ROOT)
ENTITIES_PATH = "profiles/competitor-entities.yaml"
README_PATH = "README.md"
ARCH_PATH = "docs/ARCHITECTURE.md"
LOG_PATH = "iteration-log.md"
TEST_BASENAME = (
    "test_type_c_939_apple_siri_ai_250m_class_action_settlement_website_live_sep23_5am.py"
)
MECH_NUM = 795
# Built by concatenation so the underscore-form marker never sits contiguously
# in this file: the #715 sweep-instrument convention.
MECH_ID_MARKER = "mechanism" + "_795"
NEXT_ID_MARKER = "mechanism" + "_796"
NEXT_ID_NUMERIC = "mechanism_id: 796"
MECH_KEY = "apple_siri_ai_250m_delayed_launch_class_action_settlement_website_live_sep2026"
URL_SEP20 = "https://www.macrumors.com/2026/09/20/siri-ai-settlement-website-now-live/"
URL_SEP22 = "https://www.macrumors.com/2026/09/22/apple-iphone-siri-ai-settlement-submit-claim/"
URL_MAY05 = "https://www.macrumors.com/2026/05/05/apple-class-action-siri-lawsuit-settlement/"
NEXT_SIBLING = "\n    q3_fy26_earnings:"
ANCHORED_SHA = "PATCH_ME_IN_FOLLOWUP"


def _read(rel):
    with open(os.path.join(REPO_ROOT, rel), encoding="utf-8") as fh:
        return fh.read()


def _block():
    doc = _read(ENTITIES_PATH)
    start = doc.index(MECH_KEY + ":")
    end = doc.index(NEXT_SIBLING, start)
    return doc[start:end]


def _block_data():
    import yaml

    return yaml.safe_load(_block())[MECH_KEY]


def _fold(s):
    return re.sub(r"\s+", " ", s.lower())


def _run_git(*args):
    return subprocess.run(
        ["git", "-C", REPO_ROOT] + list(args),
        capture_output=True,
        text=True,
    )


# --- Novelty ---------------------------------------------------------------


class TestNovelty939:
    """Pre-commit novelty: single new file, unique commit, zero repo precedent."""

    def test_single_test_type_c_939_file(self):
        files = sorted(
            str(p) for p in TESTS_DIR.glob("test_type_c_939*.py")
        )
        assert len(files) == 1, files
        assert files[0].endswith(TEST_BASENAME), files

    def test_type_c_939_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 followup convention; patched green post-commit.
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP", "POST_COMMIT_ANCHORED", "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ), "anchor SHA is still the pre-commit placeholder"
        res = _run_git("log", "--all", "--grep", "Type C #939")
        assert ANCHORED_SHA in res.stdout, "main commit is not the expected anchored SHA"

    def test_novelty_verification_claim_present_in_block(self):
        # The block pins the pre-commit novelty greps (zero test_type_c_939
        # files on disk, no "Type C #939" in git log, max numeric
        # mechanism_id 794 pre-commit, zero underscore-form 795 strings
        # repo-wide, zero numeric 795-form mechanism keys repo-wide, block key
        # zero-hit repo-wide, all three macrumors settlement urls zero-hit
        # repo-wide); this test pins the claim in the committed block, per the
        # #752 convention.
        data = _block_data()
        rm = _fold(data["research_method"])
        assert "zero test_type_c_939 files on disk" in rm
        assert 'no "type c #939" in git log' in rm
        assert "max numeric mechanism_id 794 in-tree pre-commit" in rm
        assert "zero underscore-form 795" in rm
        assert "zero numeric 795-form mechanism keys" in rm
        assert "block key zero-hit repo-wide pre-commit" in rm
        assert "all three macrumors settlement urls zero-hit repo-wide pre-commit" in rm


# --- Rotation guard ---------------------------------------------------------


class TestRotationCycleGuard939:
    """Rotation: 935-939 window fifth leg D->E->A->B->C, closing the window."""

    EXPECTED_ORDER = [
        ("C", "939"), ("B", "938"), ("A", "937"), ("E", "936"), ("D", "935"),
    ]
    ORDER = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}

    def _window(self):
        # First occurrence of each distinct iteration number, newest first
        # (robust to the #756-style followup commits that repeat the same
        # "Type X #N" wording without the colon, per the #752 convention;
        # hardened per the #783 repair to dedupe by iteration number).
        mains = subprocess.run(
            ["git", "-C", REPO_ROOT, "log", "--format=%s", "--no-merges",
             "-n", "40", "--", "."],
            capture_output=True,
            text=True,
        ).stdout.splitlines()
        seen_nums = set()
        out = []
        for s in mains:
            m = re.match(r"Type ([A-E]) #(\d+):", s)
            if m and m.group(2) not in seen_nums:
                seen_nums.add(m.group(2))
                out.append(m.groups())
        return out[:5]

    def test_window_closes_deabc(self):
        assert self._window() == self.EXPECTED_ORDER

    def test_window_cycle_edges_are_adjacent(self):
        window = self._window()
        for (t1, _), (t2, _) in zip(window, window[1:]):
            assert (self.ORDER[t1] - self.ORDER[t2]) % 5 == 1, (t1, t2)

    def test_anchor_sha_matches_head(self):
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP", "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        )
        # Durable post-commit: the anchored main commit is in history and its
        # subject opens the #939 window-closing leg (HEAD drifts past it with
        # the anchor/doc-sync/push-status followups, per the #565 convention).
        res = _run_git("log", "--format=%H %s", "--all")
        hits = [l for l in res.stdout.splitlines()
                if l.startswith(ANCHORED_SHA + " ")]
        assert len(hits) == 1, hits
        assert "Type C #939: " in hits[0], hits


# --- Mechanism content -------------------------------------------------------


class TestMechanism795Content:
    def test_block_present_in_entities(self):
        block = _block()
        assert block.strip().startswith(MECH_KEY + ":")

    def test_iteration_metadata(self):
        data = _block_data()
        assert data["mechanism_id"] == MECH_NUM
        assert data["iteration"] == 939
        assert data["iteration_type"] == "C"
        assert data["date_analyzed"] == "2026-09-23"
        assert data["time_pdt"] == "05:00"
        assert data["job_id"] == "mediascope-daily-iteration"
        assert data["goal_id"] == "goal_54093bda4145"

    def test_settlement_website_live_sep20_first_hand_read(self):
        data = _block_data()
        facts = data["settlement_facts"]
        wl = _fold(facts["sep20_website_live"])
        assert "joe rossignol" in wl
        assert "first-hand read" in wl
        assert "113 lines" in wl
        assert "$250 million" in wl
        assert "smartphoneaisettlement.com" in wl

    def test_settlement_magnitude_and_claim_terms(self):
        data = _block_data()
        facts = data["settlement_facts"]
        ct = _fold(facts["claim_terms"])
        assert "$25 per eligible iphone" in ct
        assert "$95" in ct
        assert "sep 21" in ct and "dec 21 2026" in ct
        assert "feb 24 2027" in ct

    def test_eligibility_terms(self):
        data = _block_data()
        facts = data["settlement_facts"]
        el = _fold(facts["eligibility"])
        assert "u.s. residents" in el
        assert "iphone 15 pro" in el
        assert "iphone 16e" in el
        assert "june 10 2024" in el and "march 29 2025" in el

    def test_false_advertising_background(self):
        data = _block_data()
        facts = data["settlement_facts"]
        sb = _fold(facts["suit_background"])
        assert "june 2024" in sb
        assert "march 2025" in sb
        assert "false advertising" in sb
        assert "bella ramsey" in sb
        assert "denies all allegations" in sb

    def test_twin_nine_figure_incentive_reading(self):
        data = _block_data()
        ir = data["incentive_reading"]
        tn = _fold(ir["twin_nine_figure_legs"])
        assert "two documented nine-figure cost legs" in tn
        assert "$250m" in tn
        assert "pays consumers for the delay" in tn
        assert "would pay publishers for current-news content" in tn
        ps = _fold(ir["payer_side_documentation"])
        assert "committed payer-side counterparty" in ps

    def test_observable_vs_sealed_settlement_contrast(self):
        data = _block_data()
        ir = data["incentive_reading"]
        oc = _fold(ir["observable_vs_sealed_contrast"])
        assert "mechanism 792" in oc
        assert "unobservable" in oc
        assert "observable counterpart" in oc
        nt = _fold(ir["no_transfer_claimed_between_publishers"])
        assert "no payment to any publisher is documented" in nt

    def test_connects_to(self):
        data = _block_data()
        assert data["connects_to"] == [156, 606, 792]

    def test_source_urls_verbatim(self):
        data = _block_data()
        assert data["source_urls"][0] == URL_SEP20
        assert data["source_urls"][1] == URL_SEP22
        assert data["source_urls"][2] == URL_MAY05
        assert len(data["source_urls"]) == 3

    def test_no_tone_claim(self):
        data = _block_data()
        assert data["no_coverage_tone_claim"] is True
        tf = _fold(data["type_c_focus"])
        assert "no coverage-tone claim" in tf
        assert "correlation is not causation" in tf


# --- Statistical discipline ---------------------------------------------------


class TestStatisticalDiscipline939:
    def test_statistical_discipline_type_c(self):
        data = _block_data()
        sd = data["statistical_discipline"]
        assert sd["scorer"] == "none"
        assert sd["tone_scores"] == "NOT_SCORED"
        assert sd["p_value"] == "NOT_CALCULATED"
        assert sd["cohens_d"] == "NOT_CALCULATED"
        assert sd["ci_95"] == "NOT_CALCULATED"
        assert sd["is_significant"] is False
        assert sd["qualitative_only"] is True
        assert sd["correlation_not_causation"] is True
        assert sd["artifact_grade"] is False

    def test_verdict_ledger_and_source_urls(self):
        data = _block_data()
        assert data["statistical_discipline"]["verdict"] == "directionally_supported_not_proven"
        assert data["no_analysis_json_update"] is True
        assert data["artifact_grade"] is False
        assert "ledger holds at 29" in data["falsification_family"]
        assert "THIRTIETH" in data["falsification_family"]

    def test_designed_keying_no_underscore_form_in_block(self):
        # Per the #715/#723/#738/#739 designed-keying convention, the block
        # key and block text must never carry the contiguous underscore-form
        # marker; the needle is format-built so this test carries no literal.
        block = _block()
        needle = MECH_ID_MARKER
        assert needle not in block
        assert MECH_KEY.count("_" + "795") == 0

    def test_ranked_confounders_and_counterargument(self):
        data = _block_data()
        conf = data["confounders_ranked"]
        assert len(conf) == 5
        assert [c["strength"] for c in conf] == [
            "strong", "strong", "moderate", "moderate", "weak",
        ]
        assert "strongest_counterargument" in data
        assert "consumer-litigation noise" in _fold(data["strongest_counterargument"])


# --- Supersession and corpus post-#938 --------------------------------------


class TestSupersessionAndCorpusPost938:
    def _numeric_ids(self):
        res = _run_git("grep", "-oh", "mechanism_id: [0-9]*", "--", "profiles/")
        return sorted(int(m.group(1)) for m in re.finditer(r"mechanism_id: (\d+)", res.stdout))

    def test_corpus_max_is_795(self):
        assert max(self._numeric_ids()) == 795

    def test_iteration_938_max_794_sweep_superseded_by_design(self):
        # #938's max-794 sweeps fail by designed supersession now that 795 exists.
        assert max(self._numeric_ids()) != 794

    def test_zero_underscore_796_repo_wide(self):
        res = _run_git("grep", "-r", NEXT_ID_MARKER, "--", "profiles/", "tests/", "docs/")
        assert res.returncode != 0 and not res.stdout.strip()

    def test_zero_numeric_796_in_profiles(self):
        res = _run_git("grep", NEXT_ID_NUMERIC, "--", "profiles/")
        assert res.returncode != 0 and not res.stdout.strip()

    def test_iteration_938_zero_underscore_795_sweep_stays_green(self):
        # The #938 zero-underscore-795 sweeps stay green post-#939 by designed keying:
        # neither the profile block nor this test file carries a literal underscore-795 key.
        for root in ("profiles/", "tests/"):
            res = _run_git("grep", "-r", MECH_ID_MARKER, "--", root)
            assert res.returncode != 0 and not res.stdout.strip(), \
                "literal underscore-795 key leaked into %s" % root

    def test_iteration_938_zero_numeric_795_fails_by_designed_supersession(self):
        res = _run_git("grep", "-r", "mechanism_id: 795", "--", "profiles/")
        assert res.returncode == 0 and res.stdout.strip(), \
            "expected #938's zero-numeric-795 sweep to fail by designed supersession"

    def test_numeric_795_keys_in_exactly_the_designed_location(self):
        res = _run_git("grep", "-r", "mechanism_id: 795", "--", "profiles/")
        hits = [l for l in res.stdout.strip().splitlines() if l.strip()]
        # Designed keying: one numeric 795 key in the entities.apple block;
        # no other profiles/ location.
        assert len(hits) == 1, "unexpected numeric 795 key spread in profiles/: %s" % hits
        assert "profiles/competitor-entities.yaml" in hits[0]


# --- Ledger -----------------------------------------------------------------


def _profiles_corpus():
    out = []
    for root, _dirs, files in os.walk(os.path.join(REPO_ROOT, "profiles")):
        for fn in files:
            if fn.endswith((".yaml", ".yml", ".md")):
                out.append(_read(os.path.join(root, fn)))
    return "\n".join(out)


class TestLedger939:
    def test_thirtieth_present_and_thirty_first_absent(self):
        # Guard targets the profiles corpus per the #754 convention (prior type
        # files legitimately reference their own negative guards inside their
        # own negative-guard tests, so a tests/ sweep would false-positive).
        corpus = _profiles_corpus()
        assert "THIRTIETH" in corpus
        assert "THIRTY-FIRST" not in corpus
        assert "ledger holds at 29" in _block()

    def test_m795_block_key_unique_and_entities_parse(self):
        import yaml

        doc = yaml.safe_load(_read(ENTITIES_PATH))
        assert doc["entities"]["apple"][MECH_KEY]["mechanism_id"] == 795
        keys = [
            k for k in doc["entities"]["apple"] if k == MECH_KEY
        ]
        assert len(keys) == 1

    def test_m795_not_a_falsification_family_member(self):
        data = _block_data()
        assert data["falsification_family"].startswith("NOT a member")

    def test_no_analysis_json_update_claimed(self):
        data = _block_data()
        assert data["no_analysis_json_update"] is True
        assert data["artifact_grade"] is False
        assert data["statistical_discipline"]["verdict"] == "directionally_supported_not_proven"


# --- Doc-sync ----------------------------------------------------------------


class TestDocSync939:
    def test_readme_row_939(self):
        assert TEST_BASENAME in _read(README_PATH)

    def test_architecture_row_939(self):
        assert TEST_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_939_file(self):
        text = _read(ARCH_PATH)
        assert "tests/" + TEST_BASENAME in text


# --- Iteration log ------------------------------------------------------------


class TestIterationLog939:
    def _log(self):
        return _read(LOG_PATH)

    def test_log_entry_present(self):
        assert "## #939 Type C:" in self._log()

    def test_log_mechanism_number_and_topic(self):
        log = self._log()
        idx = log.index("## #939 Type C:")
        entry = log[idx:idx + 9000]
        assert "mechanism 795" in entry
        assert "Siri AI" in entry
        assert "settlement" in entry

    def test_sep_23_2026_is_wednesday(self):
        import datetime

        assert datetime.date(2026, 9, 23).strftime("%A") == "Wednesday"
