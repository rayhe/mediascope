"""Type C #934 (2026-09-23 00:00 PDT): Apple x X Corp / SpaceXAI confidential
antitrust settlement (Sep 2026) - FIRST dedicated corpus mechanism mapping a
sealed co-defendant resolution as an unobservable financial variable: Apple
exits on undisclosed terms while OpenAI defends alone. Reuters Sep 16
(first-hand read): Judge Mark Pittman (Fort Worth) ordered X Corp and SpaceXAI
to submit to the court any Apple agreement relating to the resolution of the
plaintiffs' antitrust claims against Apple, after OpenAI (Wachtell) moved to
compel disclosure to bolster its defenses; X had resolved its Apple claims
without revealing terms while continuing against OpenAI; OpenAI argued the
Apple terms could undermine X's effort to seek a monetary payment from OpenAI.
Reuters Sep 18 (first-hand read): after in-camera review Pittman denied
OpenAI's request, concluding the terms "do not present information relevant
to the issues to be decided at summary judgment or trial"; resolution stays
confidential; trial set for January. Consideration undisclosed: no payment is
documented and none is claimed.

Rotation window FIFTH leg: D (#930) -> E (#931) -> A (#932) -> B (#933) ->
C (#934), CLOSING the 930-934 window.

Evidence: 2 browser.search query sets this run + 2 browser.open first-hand
reads (Reuters Sep 16, 34 lines; Reuters Sep 18, 33 lines); rejected candidates
logged (Princeton UP x Cashmere m663-family, ANI Sep 15 appeal m717, Apple
Siri publisher-pay m606 watch, News Corp additional arrangements m630 watch,
AWS AI Content Marketplace in-corpus). Statistical discipline per the
qualitative Type C convention: p_value/cohens_d/ci_95 NOT_CALCULATED,
tone_scores NOT_SCORED, is_significant False, engine NOT run; verdict
directionally_supported_not_proven; NOT a falsification-family member (ledger
holds at 29, THIRTIETH remains the negative guard); no analysis.json update.

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
    "test_type_c_934_xai_apple_confidential_antitrust_settlement_sep23_12am.py"
)
MECH_NUM = 792
# Built by concatenation so the underscore-form marker never sits contiguously
# in this file: the #715 sweep-instrument convention.
MECH_ID_MARKER = "mechanism" + "_792"
NEXT_ID_MARKER = "mechanism" + "_793"
NEXT_ID_NUMERIC = "mechanism_id: 793"
MECH_KEY = "xai_apple_confidential_antitrust_settlement_sep2026"
URL_SEP16 = "https://www.reuters.com/legal/litigation/openai-challenges-secrecy-apple-pact-with-musks-x-spacexai-2026-09-16/"
URL_SEP18 = "https://www.reuters.com/legal/litigation/us-judge-denies-openai-bid-review-x-corps-settlement-with-apple-2026-09-18/"
NEXT_SIBLING = "\n    nadella_retrain_testimony_93pct_clickthrough_sep2026:"
ANCHORED_SHA = "f3d39dbf8d927491aa96aa2d0b06a405fdea98fb"


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


class TestNovelty934:
    """Pre-commit novelty: single new file, unique commit, zero repo precedent."""

    def test_single_test_type_c_934_file(self):
        files = sorted(
            str(p) for p in TESTS_DIR.glob("test_type_c_934*.py")
        )
        assert len(files) == 1, files
        assert files[0].endswith(TEST_BASENAME), files

    def test_type_c_934_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 followup convention; patched green post-commit.
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP", "POST_COMMIT_ANCHORED", "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ), "anchor SHA is still the pre-commit placeholder"
        res = _run_git("log", "--all", "--grep", "Type C #934")
        assert ANCHORED_SHA in res.stdout, "main commit is not the expected anchored SHA"

    def test_novelty_verification_claim_present_in_block(self):
        # The block pins the pre-commit novelty greps (zero test_type_c_934
        # files on disk, no "Type C #934" in git log, max numeric
        # mechanism_id 791 pre-commit, zero underscore-form 792 strings
        # repo-wide, zero numeric 792-form mechanism keys repo-wide, block key
        # zero-hit repo-wide, both Reuters URLs zero-hit repo-wide); this
        # test pins the claim in the committed block, per the #752 convention.
        data = _block_data()
        rm = _fold(data["research_method"])
        assert "zero test_type_c_934 files on disk" in rm
        assert 'no "type c #934" in git log' in rm
        assert "max numeric mechanism_id 791 pre-commit" in rm
        assert "zero underscore-form 792" in rm
        assert "zero numeric 792-form mechanism keys" in rm
        assert "block key zero-hit repo-wide pre-commit" in rm
        assert "both reuters urls zero-hit repo-wide pre-commit" in rm


# --- Rotation guard ---------------------------------------------------------


class TestRotationCycleGuard934:
    """Rotation: 930-934 window fifth leg D->E->A->B->C, closing the window."""

    EXPECTED_ORDER = [
        ("C", "934"), ("B", "933"), ("A", "932"), ("E", "931"), ("D", "930"),
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
        # subject opens the #934 window-closing leg (HEAD drifts past it with
        # the anchor/doc-sync/push-status followups, per the #565 convention).
        res = _run_git("log", "--format=%H %s", "--all")
        hits = [l for l in res.stdout.splitlines()
                if l.startswith(ANCHORED_SHA + " ")]
        assert len(hits) == 1, hits
        assert "Type C #934: " in hits[0], hits


# --- Mechanism content -------------------------------------------------------


class TestMechanism792Content:
    def test_block_present_in_entities(self):
        block = _block()
        assert block.strip().startswith(MECH_KEY + ":")

    def test_iteration_metadata(self):
        data = _block_data()
        assert data["mechanism_id"] == MECH_NUM
        assert data["iteration"] == 934
        assert data["iteration_type"] == "C"
        assert data["date_analyzed"] == "2026-09-23"
        assert data["time_pdt"] == "00:00"
        assert data["job_id"] == "mediascope-daily-iteration"
        assert data["goal_id"] == "goal_54093bda4145"

    def test_court_facts_reuters_sep16(self):
        data = _block_data()
        cf = data["court_facts"]
        assert "Mark Pittman" in cf["sep16_disclosure_order"]
        assert "Wachtell" in cf["sep16_disclosure_order"]
        assert "without revealing terms" in cf["sep16_disclosure_order"]
        assert "monetary payment" in cf["openai_monetary_argument"]
        assert "advocacy, not a finding" in cf["openai_monetary_argument"]

    def test_court_facts_reuters_sep18(self):
        data = _block_data()
        cf = data["court_facts"]
        assert "in-camera review" in cf["sep18_denial"]
        assert "summary judgment" in cf["sep18_denial"]
        assert "confidential" in cf["sep18_denial"]
        assert "January" in cf["trial_calendar"]

    def test_consideration_unknown_boundary(self):
        data = _block_data()
        ov = _fold(data["overview"])
        assert "no payment" in ov
        assert "undisclosed" in ov
        ir = _fold(data["incentive_reading"])
        assert "unobserved" in ir
        assert "no transfer is claimed" in ir
        assert "no magnitude is estimated" in ir

    def test_incentive_reading_asymmetric_posture(self):
        data = _block_data()
        ir = _fold(data["incentive_reading"])
        assert "asymmetric" in ir
        assert "apple" in ir and "openai" in ir
        assert "bounds the inference" in ir

    def test_connects_to(self):
        data = _block_data()
        assert data["connects_to"] == [717, 606, 663]

    def test_source_urls_verbatim(self):
        data = _block_data()
        assert data["source_urls"][0] == URL_SEP16
        assert data["source_urls"][1] == URL_SEP18
        assert len(data["source_urls"]) == 2

    def test_no_tone_claim(self):
        data = _block_data()
        ov = _fold(data["overview"])
        assert "no coverage-tone claim" in ov
        assert "correlation is not causation" in ov


# --- Statistical discipline ---------------------------------------------------


class TestStatisticalDiscipline934:
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
        assert data["verdict"] == "directionally_supported_not_proven"
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
        assert MECH_KEY.count("_" + "792") == 0

    def test_ranked_confounders_and_counterargument(self):
        data = _block_data()
        conf = data["confounders_ranked"] if "confounders_ranked" in data else data["ranked_confounders"]
        assert len(conf) == 5
        assert [c["strength"] for c in conf] == [
            "strong", "strong", "moderate", "moderate", "weak",
        ]
        assert "strongest_counterargument" in data
        assert "procedure, not a financial transfer" in _fold(data["strongest_counterargument"])


# --- Supersession and corpus post-#933 --------------------------------------


class TestSupersessionAndCorpusPost933:
    def _numeric_ids(self):
        res = _run_git("grep", "-oh", "mechanism_id: [0-9]*", "--", "profiles/")
        return sorted(int(m.group(1)) for m in re.finditer(r"mechanism_id: (\d+)", res.stdout))

    def test_corpus_max_is_792(self):
        assert max(self._numeric_ids()) == 792

    def test_iteration_933_max_791_sweep_superseded_by_design(self):
        # #933's max-791 sweeps fail by designed supersession now that 792 exists.
        assert max(self._numeric_ids()) != 791

    def test_zero_underscore_793_repo_wide(self):
        res = _run_git("grep", "-r", NEXT_ID_MARKER, "--", "profiles/", "tests/", "docs/")
        assert res.returncode != 0 and not res.stdout.strip()

    def test_zero_numeric_793_in_profiles(self):
        res = _run_git("grep", NEXT_ID_NUMERIC, "--", "profiles/")
        assert res.returncode != 0 and not res.stdout.strip()

    def test_iteration_933_zero_underscore_792_sweep_stays_green(self):
        # The #933 zero-underscore-792 sweeps stay green post-#934 by designed keying:
        # neither the profile block nor this test file carries a literal underscore-792 key.
        for root in ("profiles/", "tests/"):
            res = _run_git("grep", "-r", MECH_ID_MARKER, "--", root)
            assert res.returncode != 0 and not res.stdout.strip(), \
                "literal underscore-792 key leaked into %s" % root

    def test_iteration_933_zero_numeric_792_fails_by_designed_supersession(self):
        res = _run_git("grep", "-r", "mechanism_id: 792", "--", "profiles/")
        assert res.returncode == 0 and res.stdout.strip(), \
            "expected #933's zero-numeric-792 sweep to fail by designed supersession"

    def test_numeric_792_keys_in_exactly_the_designed_location(self):
        res = _run_git("grep", "-r", "mechanism_id: 792", "--", "profiles/")
        hits = [l for l in res.stdout.strip().splitlines() if l.strip()]
        # Designed keying: one numeric 792 key in the entities.openai block;
        # no other profiles/ location.
        assert len(hits) == 1, "unexpected numeric 792 key spread in profiles/: %s" % hits
        assert "profiles/competitor-entities.yaml" in hits[0]


# --- Ledger -----------------------------------------------------------------


def _profiles_corpus():
    out = []
    for root, _dirs, files in os.walk(os.path.join(REPO_ROOT, "profiles")):
        for fn in files:
            if fn.endswith((".yaml", ".yml", ".md")):
                out.append(_read(os.path.join(root, fn)))
    return "\n".join(out)


class TestLedger934:
    def test_thirtieth_present_and_thirty_first_absent(self):
        # Guard targets the profiles corpus per the #754 convention (prior type
        # files legitimately reference their own negative guards inside their
        # own negative-guard tests, so a tests/ sweep would false-positive).
        corpus = _profiles_corpus()
        assert "THIRTIETH" in corpus
        assert "THIRTY-FIRST" not in corpus
        assert "ledger holds at 29" in _block()

    def test_m792_block_key_unique_and_entities_parse(self):
        import yaml

        doc = yaml.safe_load(_read(ENTITIES_PATH))
        assert doc["entities"]["openai"][MECH_KEY]["mechanism_id"] == 792
        keys = [
            k for k in doc["entities"]["openai"] if k == MECH_KEY
        ]
        assert len(keys) == 1

    def test_m792_not_a_falsification_family_member(self):
        data = _block_data()
        assert data["falsification_family"].startswith("NOT a member")

    def test_no_analysis_json_update_claimed(self):
        data = _block_data()
        assert data["no_analysis_json_update"] is True
        assert data["artifact_grade"] is False
        assert data["verdict"] == "directionally_supported_not_proven"


# --- Doc-sync ----------------------------------------------------------------


class TestDocSync934:
    def test_readme_row_934(self):
        assert TEST_BASENAME in _read(README_PATH)

    def test_architecture_row_934(self):
        assert TEST_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_934_file(self):
        text = _read(ARCH_PATH)
        assert "tests/" + TEST_BASENAME in text


# --- Iteration log ------------------------------------------------------------


class TestIterationLog934:
    def _log(self):
        return _read(LOG_PATH)

    def test_log_entry_present(self):
        assert "## #934 Type C:" in self._log()

    def test_log_mechanism_number_and_topic(self):
        log = self._log()
        idx = log.index("## #934 Type C:")
        entry = log[idx:idx + 9000]
        assert "mechanism 792" in entry
        assert "Apple" in entry
        assert "settlement" in entry

    def test_sep_23_2026_is_wednesday(self):
        import datetime

        assert datetime.date(2026, 9, 23).strftime("%A") == "Wednesday"
