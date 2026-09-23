"""Type C #944 (2026-09-23 10:00 PDT): OpenAI x India attribution-deal fee
estimates - FIRST corpus dollar figures on the Sep 7-8 2026 India template:
exchange4media (Kanchan Srivastava, Sep 23 2026, first-hand browser.open read
this run, 86 lines) reports industry-source estimates of ~$5M/yr for the BCCL
(Times of India / Economic Times) partnership and ~$3M/yr for the Indian
Express Group deal; all three parties (BCCL, Indian Express Group, OpenAI)
declined to disclose terms, so the figures are estimates, not confirmed fees.
The Press Gazette AI news-publisher deals/lawsuits tracker relays the same
two figures the same day. This REFINES mechanism 660's "zero-fee-disclosed"
template to fee-undisclosed-by-parties with first public estimates mid-band
(the $5M BCCL figure lands at the TOP of The Information's 2024 $1-5M/yr
OpenAI offer band; the $3M Indian Express figure mid-band). Combined ~$8M/yr
for India's two largest English newspaper groups vs News Corp's $250M/5yr
($50M/yr reported) - roughly 16% of the News Corp annual rate. Bandwagon leg:
the e4m piece documents other Indian publishers now approaching OpenAI after
the twin deals - the published estimates function as a price signal pulling
publishers into the sign tier.

Rotation window FIFTH leg: D (#940) -> E (#941) -> A (#942) -> B (#943) ->
C (#944), CLOSING the 940-944 window.

Evidence: 3 browser.search query sets this run + 1 browser.open first-hand
read (exchange4media Sep 23 2026, 86 lines, Kanchan Srivastava); Press Gazette
tracker relay excerpt-bounded per #503; rejected candidates logged (Amazon x
Anthropic Sep 2026 re-reports = Apr 2026 event already in corpus; RTB Digital
x Paradium.AI = non-competitor counterparty; UMG x ElevenLabs / Suno x
Warner-BMG = music vertical, out of scope). Statistical discipline per the
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
    "test_type_c_944_openai_india_attribution_deal_fee_estimates_e4m_sep23_10am.py"
)
MECH_NUM = 798
# Built by concatenation so the underscore-form marker never sits contiguously
# in this file: the #715 sweep-instrument convention.
MECH_ID_MARKER = "mechanism" + "_798"
NEXT_ID_MARKER = "mechanism" + "_799"
NEXT_ID_NUMERIC = "mechanism_id: 799"
MECH_KEY = "openai_india_attribution_deal_fee_estimates_e4m_sep2026"
URL_E4M = "https://www.exchange4media.com/digital-news/openais-toi-ie-deals-spark-wider-interest-among-news-publishers-158488.html"
URL_PRESS_GAZETTE = "https://pressgazette.co.uk/platforms/news-publisher-ai-deals-lawsuits-openai-google/"
NEXT_SIBLING = "\n    mechanism_664_reuters_openai_slowdown_week_register_vs_meta_muse_accountability_sep13:"
ANCHORED_SHA = "3c1111f2347e54a10240b986f11c7e2742d3eaf2"


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


class TestNovelty944:
    """Pre-commit novelty: single new file, unique commit, zero repo precedent."""

    def test_single_test_type_c_944_file(self):
        files = sorted(
            str(p) for p in TESTS_DIR.glob("test_type_c_944*.py")
        )
        assert len(files) == 1, files
        assert files[0].endswith(TEST_BASENAME), files

    def test_type_c_944_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 followup convention; patched green post-commit.
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP", "POST_COMMIT_ANCHORED", "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ), "anchor SHA is still the pre-commit placeholder"
        res = _run_git("log", "--all", "--grep", "Type C #944")
        assert ANCHORED_SHA in res.stdout, "main commit is not the expected anchored SHA"

    def test_novelty_verification_claim_present_in_block(self):
        # The block pins the pre-commit novelty greps (zero test_type_c_944
        # files on disk, no "Type C #944" in git log, max numeric
        # mechanism_id 797 pre-commit, zero underscore-form 798 strings
        # repo-wide, zero numeric 798-form mechanism keys repo-wide, block key
        # zero-hit repo-wide pre-commit, the e4m 158488 url zero-hit
        # repo-wide pre-commit); this test pins the claim in the committed
        # block, per the #752 convention.
        data = _block_data()
        rm = _fold(data["research_method"])
        assert "zero test_type_c_944 files on disk" in rm
        assert 'no "type c #944" in git log' in rm
        assert "max numeric mechanism_id 797 in-tree pre-commit" in rm
        assert "zero underscore-form 798" in rm
        assert "zero numeric 798-form mechanism keys" in rm
        assert "block key zero-hit repo-wide pre-commit" in rm
        assert "e4m 158488 url zero-hit repo-wide pre-commit" in rm


# --- Rotation guard ---------------------------------------------------------


class TestRotationCycleGuard944:
    """Rotation: 940-944 window fifth leg D->E->A->B->C, closing the window."""

    EXPECTED_ORDER = [
        ("C", "944"), ("B", "943"), ("A", "942"), ("E", "941"), ("D", "940"),
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
        # subject opens the #944 window-closing leg (HEAD drifts past it with
        # the anchor/doc-sync/push-status followups, per the #565 convention).
        res = _run_git("log", "--format=%H %s", "--all")
        hits = [l for l in res.stdout.splitlines()
                if l.startswith(ANCHORED_SHA + " ")]
        assert len(hits) == 1, hits
        assert "Type C #944: " in hits[0], hits


# --- Mechanism content -------------------------------------------------------


class TestMechanism798Content:
    def test_block_present_in_entities(self):
        import yaml

        doc = yaml.safe_load(_read(ENTITIES_PATH))
        assert doc["entities"]["openai"][MECH_KEY]["mechanism_id"] == MECH_NUM

    def test_iteration_metadata(self):
        data = _block_data()
        assert data["iteration"] == 944
        assert data["iteration_type"] == "C"
        assert data["rotation"] == "Type C"
        assert data["type"] == "financial_incentive_mapping"
        assert data["date_analyzed"] == "2026-09-23"
        assert data["time_pdt"] == "10:00"
        assert data["job_id"] == "mediascope-daily-iteration"
        assert data["goal_id"] == "goal_54093bda4145"
        assert data["block_key"] == "type_c_944_openai_india_attribution_deal_fee_estimates_e4m_sep23_10am"
        assert data["test_file"] == "tests/" + TEST_BASENAME

    def test_bccl_5m_annual_estimate(self):
        data = _block_data()
        fees = " ".join(data["fee_estimates"])
        assert "$5 million annually" in fees
        assert "BCCL" in fees
        assert "Times of India" in fees
        assert "Economic Times" in fees

    def test_indian_express_3m_annual_estimate(self):
        data = _block_data()
        fees = " ".join(data["fee_estimates"])
        assert "$3 million a year" in fees
        assert "Indian Express Group" in fees
        assert "seven languages" in fees

    def test_top_of_band_reading(self):
        data = _block_data()
        fees = " ".join(data["fee_estimates"])
        assert "$1-5M/yr" in fees
        focus = data["type_c_focus"]
        assert "TOP of The Information" in focus or "TOP of the" in focus

    def test_news_corp_ratio_leg(self):
        data = _block_data()
        fees = " ".join(data["fee_estimates"])
        assert "16%" in fees
        assert "News Corp" in fees
        assert "$50M/yr" in fees

    def test_non_disclosure_caveat(self):
        data = _block_data()
        nd = " ".join(data["non_disclosure_caveat"])
        assert "none disclosed the value of the agreements" in nd
        assert "estimates" in nd
        assert "unconfirmed" in nd

    def test_template_refinement_leg(self):
        data = _block_data()
        focus = data["type_c_focus"]
        assert "fee-undisclosed-BY-THE-PARTIES" in focus or "fee-undisclosed" in focus
        assert "zero-fee-disclosed" in focus
        assert "mid-band" in focus

    def test_first_hand_read_recorded(self):
        data = _block_data()
        src = " ".join(data["sources"])
        assert "Kanchan Srivastava" in src
        assert "FIRST-HAND browser.open read this run, 86 lines" in src
        rm = _fold(data["research_method"])
        assert "1 browser.open first-hand read" in rm

    def test_bandwagon_leg(self):
        data = _block_data()
        bw = " ".join(data["bandwagon_leg"])
        assert "prompted other Indian publishers to step up" in bw
        assert "price signal" in bw

    def test_press_gazette_relay_same_day(self):
        data = _block_data()
        src = " ".join(data["sources"])
        assert "Press Gazette" in src
        assert "23 September 2026" in src
        assert "$5m per year" in src
        assert "$3m per year" in src

    def test_global_scale_tension_flagged(self):
        data = _block_data()
        gs = " ".join(data["global_scale_leg"])
        assert "$2.92 billion" in gs
        assert "January 2025" in gs
        assert "DATA TENSION" in gs
        assert "$25 million a year" in gs

    def test_connects_to(self):
        data = _block_data()
        refs = " ".join(data["cross_references"])
        for m in ("609", "660", "657", "654", "714"):
            assert "mechanism %s" % m in refs, m

    def test_source_urls_verbatim(self):
        data = _block_data()
        assert URL_E4M in data["source_urls"]
        assert URL_PRESS_GAZETTE in data["source_urls"]

    def test_no_tone_claim(self):
        data = _block_data()
        assert data["no_coverage_tone_claim"] is True
        assert data["statistical_discipline"]["tone_scores"] == "NOT_SCORED"


# --- Statistical discipline -------------------------------------------------


class TestStatisticalDiscipline944:
    def test_statistical_discipline_type_c(self):
        data = _block_data()
        sd = data["statistical_discipline"]
        assert sd["p_value"] == "NOT_CALCULATED"
        assert sd["cohens_d"] == "NOT_CALCULATED"
        assert sd["ci_95"] == "NOT_CALCULATED"
        assert sd["is_significant"] is False
        assert sd["engine_run"] is False
        assert sd["verdict"] == "directionally_supported_not_proven"
        assert sd["qualitative_only"] is True
        assert data["cautious_language_required"] is True

    def test_verdict_ledger_and_source_urls(self):
        data = _block_data()
        assert data["statistical_discipline"]["verdict"] == "directionally_supported_not_proven"
        assert "ledger holds at 29" in data["falsification_family"]
        assert data["no_analysis_json_update"] is True
        assert len(data["source_urls"]) == 2

    def test_designed_keying_no_underscore_form_in_block(self):
        # Per the #715 convention the committed block carries the numeric
        # mechanism_id form only; the underscore form must not appear.
        assert MECH_ID_MARKER not in _block()

    def test_ranked_confounders_and_counterargument(self):
        data = _block_data()
        confs = data["ranked_confounders"]
        assert len(confs) == 5
        strengths = [c["strength"] for c in confs]
        assert strengths[:2] == ["strong", "strong"]
        assert [c["rank"] for c in confs] == [1, 2, 3, 4, 5]
        top = confs[0]["confounder"]
        top_low = top.lower()
        assert "estimates" in top_low and "unconfirmed" in top_low
        absences = " ".join(data["bounded_absences"])
        assert "declined" in absences


# --- Supersession -----------------------------------------------------------


class TestSupersessionAndCorpusPost943:
    def _numeric_ids(self):
        res = _run_git("grep", "-oh", "mechanism_id: [0-9]*", "--", "profiles/")
        return sorted(int(m.group(1)) for m in re.finditer(r"mechanism_id: (\d+)", res.stdout))

    def test_corpus_max_is_798(self):
        assert max(self._numeric_ids()) == 798

    def test_iteration_943_max_797_sweep_superseded_by_design(self):
        # #943's max-797 sweeps fail by designed supersession now that 798 exists.
        assert max(self._numeric_ids()) != 797

    def test_zero_underscore_799_repo_wide(self):
        res = _run_git("grep", "-r", NEXT_ID_MARKER, "--", "profiles/", "tests/", "docs/")
        assert res.returncode != 0 and not res.stdout.strip()

    def test_zero_numeric_799_in_profiles(self):
        res = _run_git("grep", NEXT_ID_NUMERIC, "--", "profiles/")
        assert res.returncode != 0 and not res.stdout.strip()

    def test_iteration_943_zero_underscore_798_sweep_stays_green(self):
        # The #943 zero-underscore-798 sweeps stay green post-#944 by designed keying:
        # neither the profile block nor this test file carries a literal underscore-798 key.
        for root in ("profiles/", "tests/"):
            res = _run_git("grep", "-r", MECH_ID_MARKER, "--", root)
            assert res.returncode != 0 and not res.stdout.strip(), \
                "literal underscore-798 key leaked into %s" % root

    def test_iteration_943_zero_numeric_798_fails_by_designed_supersession(self):
        res = _run_git("grep", "-r", "mechanism_id: 798", "--", "profiles/")
        assert res.returncode == 0 and res.stdout.strip(), \
            "expected #943's zero-numeric-798 sweep to fail by designed supersession"

    def test_numeric_798_keys_in_exactly_the_designed_location(self):
        res = _run_git("grep", "-r", "mechanism_id: 798", "--", "profiles/")
        hits = [l for l in res.stdout.strip().splitlines() if l.strip()]
        # Designed keying: one numeric 798 key in the entities.openai block;
        # no other profiles/ location.
        assert len(hits) == 1, "unexpected numeric 798 key spread in profiles/: %s" % hits
        assert "profiles/competitor-entities.yaml" in hits[0]


# --- Ledger -----------------------------------------------------------------


def _profiles_corpus():
    out = []
    for root, _dirs, files in os.walk(os.path.join(REPO_ROOT, "profiles")):
        for fn in files:
            if fn.endswith((".yaml", ".yml", ".md")):
                out.append(_read(os.path.join(root, fn)))
    return "\n".join(out)


class TestLedger944:
    def test_thirtieth_present_and_thirty_first_absent(self):
        # Guard targets the profiles corpus per the #754 convention (prior type
        # files legitimately reference their own negative guards inside their
        # own negative-guard tests, so a tests/ sweep would false-positive).
        corpus = _profiles_corpus()
        assert "THIRTIETH" in corpus
        assert "THIRTY-FIRST" not in corpus
        assert "ledger holds at 29" in _block()

    def test_m798_block_key_unique_and_entities_parse(self):
        import yaml

        doc = yaml.safe_load(_read(ENTITIES_PATH))
        assert doc["entities"]["openai"][MECH_KEY]["mechanism_id"] == 798
        keys = [
            k for k in doc["entities"]["openai"] if k == MECH_KEY
        ]
        assert len(keys) == 1

    def test_m798_not_a_falsification_family_member(self):
        data = _block_data()
        assert data["falsification_family"].startswith("NOT a member")

    def test_no_analysis_json_update_claimed(self):
        data = _block_data()
        assert data["no_analysis_json_update"] is True
        assert data["artifact_grade"] is False
        assert data["statistical_discipline"]["verdict"] == "directionally_supported_not_proven"


# --- Doc-sync ----------------------------------------------------------------


class TestDocSync944:
    def test_readme_row_944(self):
        assert TEST_BASENAME in _read(README_PATH)

    def test_architecture_row_944(self):
        assert TEST_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_944_file(self):
        text = _read(ARCH_PATH)
        assert "tests/" + TEST_BASENAME in text


# --- Iteration log ------------------------------------------------------------


class TestIterationLog944:
    def _log(self):
        return _read(LOG_PATH)

    def test_log_entry_present(self):
        assert "## #944 Type C:" in self._log()

    def test_log_mechanism_number_and_topic(self):
        log = self._log()
        idx = log.index("## #944 Type C:")
        entry = log[idx:idx + 9000]
        assert "mechanism 798" in entry
        assert "India" in entry
        assert "fee estimates" in entry

    def test_sep_23_2026_is_wednesday(self):
        import datetime

        assert datetime.date(2026, 9, 23).strftime("%A") == "Wednesday"
