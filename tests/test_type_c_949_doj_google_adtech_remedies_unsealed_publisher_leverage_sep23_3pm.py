"""Type C #949 (2026-09-23 15:00 PDT): DOJ v Google ad-tech behavioural remedies
unsealed Sep 16 2026 - the first structural publisher-leverage repricing in the
corpus. The U.S. District Court for the Eastern District of Virginia unsealed
its Sep 2 2026 remedies decision: (i) DFP-AdX untie, no First Look/Last Look
reinstatement, no Unified Pricing Rules on indirect DFP transactions;
(ii) mandatory Prebid interfaces (AdX real-time bids to Prebid, DFP-Prebid
connection, AdX real-time bids to rival publisher ad servers); (iii) publisher
data portability (historical + configuration DFP data, ongoing AdX bid data,
exportable to rival ad servers, open-web display); (iv) AdWords barred from
direct DFP bidding and from favouring Google-owned/affiliated tools. The court
REJECTED the sought structural remedy (AdX divestiture). 6-year judgment,
effective 60 days after entry; monitor + 3-member technical committee
immediate. Incentive geometry: first corpus event that LOOSENS Channel 2 of
the publisher_ai_deal_revolt dual-channel model (ad-revenue dependency); the
structural counterweight to mechanism 929's flow inversion (publishers paying
Google while the AI Contribution Pilot pays peanuts via a black box formula,
mechanisms 702/708); new lever for the scarcity-pricing thesis (who can
withhold what). Explicitly do-not-conflate with mechanism 463 (USA TODAY Co.
v Google PRIVATE case, different track).

Rotation window FIFTH leg: D (#945) -> E (#946) -> A (#947) -> B (#948) ->
C (#949), CLOSING the 945-949 window.

Evidence: 4 browser.search query sets this run + 1 browser.open first-hand
read (dig.watch Sep 16 2026 remedies piece, 39 lines); DOJ substantial-relief
release excerpt-bounded per #503; rejected candidates logged (Apple Siri
publisher closures - zero new, m606 watch stands; Google pay-per-value pilot -
no new status, m702/708; India/Village Media/RTB - all in corpus; Getty v
Stability AI / Ziff Davis v OpenAI Sep-2026 - no results surfaced). Statistical
discipline per the qualitative Type C convention: p_value/cohens_d/ci_95
NOT_CALCULATED, tone_scores NOT_SCORED, is_significant False, engine NOT run;
verdict directionally_supported_not_proven; NOT a falsification-family member
(ledger holds at 29, THIRTIETH remains the negative guard);
no analysis.json update.

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
    "test_type_c_949_doj_google_adtech_remedies_unsealed_publisher_leverage_sep23_3pm.py"
)
MECH_NUM = 801
# Built by concatenation so the underscore-form marker never sits contiguously
# in this file: the #715 sweep-instrument convention.
MECH_ID_MARKER = "mechanism" + "_801"
NEXT_ID_MARKER = "mechanism" + "_802"
NEXT_ID_NUMERIC = "mechanism_id: 802"
MECH_KEY = "doj_google_adtech_remedies_unsealed_publisher_leverage_sep2026"
URL_DIGWATCH = "https://dig.watch/updates/court-unsealed-decision-on-remedies-set-on-google"
URL_DOJ = "https://www.justice.gov/opa/pr/department-justice-again-wins-substantial-relief-against-google"
NEXT_SIBLING = "advance_dual_asset_monetization:"
ANCHORED_SHA = "PATCH_ME_IN_FOLLOWUP"


def _read(rel):
    with open(os.path.join(REPO_ROOT, rel), encoding="utf-8") as fh:
        return fh.read()


def _block():
    doc = _read(ENTITIES_PATH)
    start = doc.index("  " + MECH_KEY + ":")
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


class TestNovelty949:
    """Pre-commit novelty: single new file, unique commit, zero repo precedent."""

    def test_single_test_type_c_949_file(self):
        files = sorted(
            str(p) for p in TESTS_DIR.glob("test_type_c_949*.py")
        )
        assert len(files) == 1, files
        assert files[0].endswith(TEST_BASENAME), files

    def test_type_c_949_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 followup convention; patched green post-commit.
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP", "POST_COMMIT_ANCHORED", "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ), "anchor SHA is still the pre-commit placeholder"
        res = _run_git("log", "--all", "--grep", "Type C #949")
        assert ANCHORED_SHA in res.stdout, "main commit is not the expected anchored SHA"

    def test_novelty_verification_claim_present_in_block(self):
        # The block pins the pre-commit novelty greps (zero test_type_c_949
        # files on disk, no "Type C #949" in git log, max numeric
        # mechanism_id 800 in-tree pre-commit, zero underscore-form 801
        # strings repo-wide, zero numeric 801-form mechanism keys repo-wide,
        # block key zero-hit repo-wide pre-commit, both evidence URLs
        # zero-hit repo-wide pre-commit, zero prebid hits repo-wide
        # pre-commit); this test pins the claim in the committed block, per
        # the #752 convention.
        data = _block_data()
        rm = _fold(data["research_method"])
        assert "zero test_type_c_949 files on disk" in rm
        assert 'no "type c #949" in git log' in rm
        assert "max numeric mechanism_id 800 in-tree pre-commit" in rm
        assert "zero underscore-form 801" in rm
        assert "zero numeric 801-form mechanism keys" in rm
        assert "block key doj_google_adtech_remedies_unsealed_publisher_leverage_sep2026 zero-hit repo-wide pre-commit" in rm
        assert "both evidence urls zero-hit repo-wide pre-commit" in rm
        assert "zero prebid hits repo-wide pre-commit" in rm


# --- Rotation guard ---------------------------------------------------------


class TestRotationCycleGuard949:
    """Rotation: 945-949 window fifth leg D->E->A->B->C, closing the window."""

    EXPECTED_ORDER = [
        ("C", "949"), ("B", "948"), ("A", "947"), ("E", "946"), ("D", "945"),
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
        # subject opens the #949 window-closing leg (HEAD drifts past it with
        # the anchor/doc-sync/push-status followups, per the #565 convention).
        res = _run_git("log", "--format=%H %s", "--all")
        hits = [l for l in res.stdout.splitlines()
                if l.startswith(ANCHORED_SHA + " ")]
        assert len(hits) == 1, hits
        assert "Type C #949: " in hits[0], hits


# --- Mechanism content -------------------------------------------------------


class TestMechanism801Content:
    def test_block_present_in_entities(self):
        import yaml

        doc = yaml.safe_load(_read(ENTITIES_PATH))
        assert MECH_KEY in doc["marketplace_intermediary_landscape"]
        assert (
            doc["marketplace_intermediary_landscape"][MECH_KEY]["mechanism_id"]
            == MECH_NUM
        )

    def test_iteration_metadata(self):
        data = _block_data()
        assert data["iteration"] == 949
        assert data["type"] == "C"
        assert data["date"] == "2026-09-23 15:00 PDT"

    def test_decision_dates(self):
        data = _block_data()
        facts = data["remedy_facts"]
        assert facts["decision_issued_under_seal"] == "2026-09-02"
        assert facts["decision_unsealed"] == "2026-09-16"

    def test_court_e_d_va(self):
        data = _block_data()
        assert "Eastern District of Virginia" in data["remedy_facts"]["court"]

    def test_structural_remedy_rejected(self):
        data = _block_data()
        facts = data["remedy_facts"]
        assert "AdX divestiture" in facts["structural_remedy_sought_rejected"]
        assert "rejected" in _fold(facts["structural_remedy_sought_rejected"])

    def test_remedy_i_untie(self):
        facts = _block_data()["remedy_facts"]
        text = _fold(facts["remedy_i_untie"])
        assert "dfp" in text and "adx" in text
        assert "first look" in text and "last look" in text
        assert "unified pricing rules" in text

    def test_remedy_ii_prebid(self):
        facts = _block_data()["remedy_facts"]
        text = _fold(facts["remedy_ii_prebid"])
        assert "prebid" in text
        assert "real-time bids" in text
        assert "rival publisher ad servers" in text

    def test_remedy_iii_data_portability(self):
        facts = _block_data()["remedy_facts"]
        text = _fold(facts["remedy_iii_data_portability"])
        assert "historical and configuration data" in text
        assert "ongoing adx bid data" in text
        assert "open-web display" in text

    def test_remedy_iv_adwords(self):
        facts = _block_data()["remedy_facts"]
        text = _fold(facts["remedy_iv_adwords"])
        assert "adwords" in text
        assert "bidding directly into dfp" in text
        assert "favouring google-owned or google-affiliated tools" in text

    def test_oversight_monitor_six_years(self):
        data = _block_data()
        text = _fold(data["remedy_facts"]["oversight"])
        assert "monitor" in text
        assert "3-member technical committee" in text
        assert "6-year judgment" in text
        assert "60 days after entry" in text

    def test_connects_to(self):
        data = _block_data()
        assert data["connects_to"] == [702, 708, 929, 463, 786, 355]

    def test_source_urls_verbatim(self):
        data = _block_data()
        src = " ".join(data["sources"])
        assert URL_DIGWATCH in src
        assert URL_DOJ in src

    def test_first_hand_read_recorded(self):
        data = _block_data()
        src = " ".join(data["sources"])
        assert "first-hand browser.open read this run, 39 lines" in src

    def test_do_not_conflate_m463(self):
        data = _block_data()
        conf = " ".join(c["text"] for c in data["confounders_ranked"])
        assert "do-not-conflate" in _fold(conf)
        assert "private case" in _fold(conf)
        assert "mechanism 463" in _fold(conf)

    def test_no_tone_claim(self):
        data = _block_data()
        note = _fold(data["statistical_discipline_note"])
        assert "no coverage-tone claim" in note
        assert data["tone_scores"] == "NOT_SCORED"


# --- Statistical discipline --------------------------------------------------


class TestStatisticalDiscipline949:
    def test_statistical_discipline_type_c(self):
        sd = _block_data()["statistical_discipline"]
        assert sd["p_value"] == "NOT_CALCULATED"
        assert sd["cohens_d"] == "NOT_CALCULATED"
        assert sd["ci_95"] == "NOT_CALCULATED"
        assert sd["is_significant"] is False
        assert sd["qualitative_only"] is True
        assert sd["correlation_not_causation"] is True

    def test_verdict_ledger_and_source_urls(self):
        data = _block_data()
        assert data["verdict"] == "directionally_supported_not_proven"
        assert data["no_analysis_json_update"] is True
        assert data["artifact_grade"] is False

    def test_designed_keying_no_underscore_form_in_block(self):
        # The block key carries no _801 marker (colon form only per #715);
        # the numeric mechanism_id field is the single source of truth.
        assert "_801" not in MECH_KEY
        assert MECH_ID_MARKER not in _block()

    def test_ranked_confounders_and_counterargument(self):
        data = _block_data()
        strengths = [c["strength"] for c in data["confounders_ranked"]]
        assert strengths.count("STRONG") == 2
        assert strengths.count("MODERATE") == 2
        assert strengths.count("WEAK") == 1
        assert len(data["counterevidence"]) == 2
        assert "margin, not structurally" in _fold(
            data["strongest_counterargument"]
        )

    def test_channel_2_loosening_leg(self):
        geo = _block_data()["incentive_geometry"]
        text = _fold(geo["channel_2_loosening"])
        assert "channel 2" in text
        assert "loosens" in text

    def test_flow_inversion_counterweight_leg(self):
        geo = _block_data()["incentive_geometry"]
        text = _fold(geo["flow_inversion_counterweight"])
        assert "flow inversion" in text
        assert "peanuts" in text
        assert "black box" in text


# --- Supersession ------------------------------------------------------------


class TestSupersessionAndCorpusPost948:
    def _numeric_ids(self):
        res = _run_git("grep", "-oh", "mechanism_id: [0-9]*", "--", "profiles/")
        return sorted(int(m.group(1)) for m in re.finditer(r"mechanism_id: (\d+)", res.stdout))

    def test_corpus_max_is_801(self):
        assert max(self._numeric_ids()) == 801

    def test_iteration_948_max_800_sweep_superseded_by_design(self):
        # #948's max-800 sweeps fail by designed supersession now that 801 exists.
        assert max(self._numeric_ids()) != 800

    def test_zero_underscore_802_repo_wide(self):
        res = _run_git("grep", "-r", NEXT_ID_MARKER, "--", "profiles/", "tests/", "docs/")
        assert res.returncode != 0 and not res.stdout.strip()

    def test_zero_numeric_802_in_profiles(self):
        res = _run_git("grep", NEXT_ID_NUMERIC, "--", "profiles/")
        assert res.returncode != 0 and not res.stdout.strip()

    def test_iteration_948_zero_underscore_801_sweep_stays_green(self):
        # The #948 zero-underscore-801 sweeps stay green post-#949 by designed keying:
        # neither the profile block nor this test file carries a literal underscore-801 key.
        for root in ("profiles/", "tests/"):
            res = _run_git("grep", "-r", MECH_ID_MARKER, "--", root)
            assert res.returncode != 0 and not res.stdout.strip(), \
                "literal underscore-801 key leaked into %s" % root

    def test_iteration_948_zero_numeric_801_fails_by_designed_supersession(self):
        res = _run_git("grep", "-r", "mechanism_id: 801", "--", "profiles/")
        assert res.returncode == 0 and res.stdout.strip(), \
            "expected #948's zero-numeric-801 sweep to fail by designed supersession"

    def test_numeric_801_keys_in_exactly_the_designed_location(self):
        res = _run_git("grep", "-r", "mechanism_id: 801", "--", "profiles/")
        hits = [l for l in res.stdout.strip().splitlines() if l.strip()]
        # Designed keying: one numeric 801 key in the
        # marketplace_intermediary_landscape block; no other profiles/ location.
        assert len(hits) == 1, "unexpected numeric 801 key spread in profiles/: %s" % hits
        assert "profiles/competitor-entities.yaml" in hits[0]


# --- Ledger -----------------------------------------------------------------


def _profiles_corpus():
    out = []
    for root, _dirs, files in os.walk(os.path.join(REPO_ROOT, "profiles")):
        for fn in files:
            if fn.endswith((".yaml", ".yml", ".md")):
                out.append(_read(os.path.join(root, fn)))
    return "\n".join(out)


class TestLedger949:
    def test_thirtieth_present_and_thirty_first_absent(self):
        # Guard targets the profiles corpus per the #754 convention (prior type
        # files legitimately reference their own negative guards inside their
        # own negative-guard tests, so a tests/ sweep would false-positive).
        corpus = _profiles_corpus()
        assert "THIRTIETH" in corpus
        assert "THIRTY-FIRST" not in corpus
        assert "ledger holds at 29" in _block()

    def test_m801_block_key_unique_and_entities_parse(self):
        import yaml

        doc = yaml.safe_load(_read(ENTITIES_PATH))
        assert doc["marketplace_intermediary_landscape"][MECH_KEY]["mechanism_id"] == 801
        keys = [
            k for k in doc["marketplace_intermediary_landscape"] if k == MECH_KEY
        ]
        assert len(keys) == 1

    def test_m801_not_a_falsification_family_member(self):
        data = _block_data()
        assert data["falsification_family"] is False

    def test_no_analysis_json_update_claimed(self):
        data = _block_data()
        assert data["no_analysis_json_update"] is True
        assert data["artifact_grade"] is False
        assert data["verdict"] == "directionally_supported_not_proven"


# --- Doc-sync ----------------------------------------------------------------


class TestDocSync949:
    def test_readme_row_949(self):
        assert TEST_BASENAME in _read(README_PATH)

    def test_architecture_row_949(self):
        assert TEST_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_949_file(self):
        text = _read(ARCH_PATH)
        assert "tests/" + TEST_BASENAME in text


# --- Iteration log ------------------------------------------------------------


class TestIterationLog949:
    def _log(self):
        return _read(LOG_PATH)

    def test_log_entry_present(self):
        assert "## #949 Type C:" in self._log()

    def test_log_mechanism_number_and_topic(self):
        log = self._log()
        idx = log.index("## #949 Type C:")
        entry = log[idx:idx + 9000]
        assert "mechanism 801" in entry
        assert "remedies" in entry
        assert "Prebid" in entry

    def test_sep_23_2026_is_wednesday(self):
        import datetime

        assert datetime.date(2026, 9, 23).strftime("%A") == "Wednesday"
