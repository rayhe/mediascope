"""Type C #794 (2026-09-16 21:00 PDT): Google publisher AI-licensing talks
(Bloomberg Law, ~Jul 2026) - FIRST dedicated corpus mechanism documenting the
~20-national-news-outlet pilot scope figure; the Jul 2026 precursor of the
Digiday-reported pay-per-use AI licensing pilot (mechanism 702, Type C #784).

Rotation window fifth leg: D (#790) -> E (#791) -> A (#792) -> B (#793) ->
C (#794), CLOSING the 790-794 window.

Evidence is search-excerpt-bounded per #503 (8 browser.search query sets, 0
browser.open; all URLs copied verbatim from search-result Full-URL
listings; no canonical URLs constructed). Statistical discipline per the
qualitative Type C convention: p_value/cohens_d/ci_95 NOT_CALCULATED,
tone_scores NOT_SCORED, is_significant False, engine NOT run; verdict
directionally_supported_not_proven; NOT a falsification-family member
(ledger holds at 26); no analysis.json update.

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
    "test_type_c_794_google_publisher_licensing_talks_bloomberg_sep16_9pm.py"
)
MECH_NUM = 708
# Built by concatenation so the underscore-form marker never sits contiguously
# in this file: the #715 sweep-instrument convention.
MECH_ID_MARKER = "mechanism" + "_708"
NEXT_ID_MARKER = "mechanism" + "_709"
NEXT_ID_NUMERIC = "mechanism_id: 709"
MECH_KEY = "google_publisher_licensing_talks_bloomberg_20_outlets_jul2026"
BLOOMBERG_URL = (
    "news.bloomberglaw.com/tech-and-telecom-law/"
    "google-in-licensing-talks-with-news-groups-following-ai-rivals"
)
NEXT_SIBLING = "\n  x_twitter:"
ANCHORED_SHA = "39ba859241ea555e7ab6592258519e69315b6616"


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


def _git_log_mains(pattern):
    proc = subprocess.run(
        ["git", "-C", REPO_ROOT, "log", "--format=%H %s", "--no-merges", "--", "."],
        capture_output=True,
        text=True,
    )
    return [l for l in proc.stdout.splitlines() if re.search(pattern, l)]


def _run_git(*args):
    return subprocess.run(
        ["git", "-C", REPO_ROOT] + list(args),
        capture_output=True,
        text=True,
    )


def _repo_grep(pattern, roots=()):
    hits = []
    for root in roots or (".",):
        proc = subprocess.run(
            ["git", "-C", REPO_ROOT, "grep", "-n", "--", pattern, root],
            capture_output=True,
            text=True,
        )
        if proc.returncode == 0:
            hits.extend(proc.stdout.splitlines())
    return hits


class TestNovelty794:
    """Pre-commit novelty: single new file, unique commit, zero repo precedent."""

    def test_single_test_type_c_794_file(self):
        files = sorted(
            str(p) for p in TESTS_DIR.glob("test_type_c_794*.py")
        )
        assert len(files) == 1, files
        assert files[0].endswith(TEST_BASENAME), files

    def test_type_c_794_main_commit_unique(self):
        mains = _git_log_mains(r"Type C #794: ")
        # Pre-commit there is no #794 main commit yet; at most one may exist.
        assert len(mains) <= 1, mains

    def test_novelty_verification_claim_present_in_block(self):
        # The block pins the pre-commit novelty greps (zero files on disk, no
        # Type C #794 in git log, Bloomberg URL zero-hit, 20-outlet figure
        # zero-hit, zero underscore-form 708 keys, max numeric mechanism_id
        # 707); this test pins the claim in the committed block, per the
        # #752 convention.
        block = _block()
        assert "Zero test_type_c_794 files on disk pre-commit" in block
        assert "No Type C #794 in git log pre-commit" in block
        assert "20 national news outlets" in block
        assert "Max numeric mechanism_id 707 pre-commit" in block


class TestRotationCycleGuard794:
    """Rotation: 790-794 window fifth leg D->E->A->B->C, closing the window."""

    EXPECTED_ORDER = [
        ("C", "794"), ("B", "793"), ("A", "792"), ("E", "791"), ("D", "790"),
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
        mains = _git_log_mains(r"Type C #794: ")
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP", "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ), mains
        assert mains and mains[0].startswith(ANCHORED_SHA + " "), mains


class TestMechanism708Content:
    def test_block_present_in_entities(self):
        block = _block()
        assert block.strip().startswith(MECH_KEY + ":")

    def test_iteration_metadata(self):
        data = _block_data()
        assert data["mechanism_id"] == MECH_NUM
        assert data["iteration"] == 794
        assert data["iteration_type"] == "C"
        assert data["date_analyzed"] == "2026-09-16"
        assert data["time_pdt"] == "21:00"
        assert data["job_id"] == "mediascope-daily-iteration"

    def test_deal_parties_and_announcement(self):
        data = _block_data()
        parties = data["deal_parties"]
        assert parties["payer"].startswith("Google")
        assert "20 national news outlets" in parties["counterparty"]
        assert data["announcement"]["first_reported"] == "Bloomberg Law, ~Jul 2026"

    def test_scope_figure_and_progression(self):
        data = _block_data()
        struct = data["deal_structure"]
        assert struct["initial_scope"].startswith(
            "About 20 national news outlets")
        assert "dozens of publishers approached" in struct["scale_progression"]
        assert "702" in struct["pricing_model"]

    def test_google_statement_and_motive(self):
        block = _fold(_block())
        assert "exploring and experimenting with new types of partnerships" in block
        assert "strengthen strained ties" in block

    def test_cross_references(self):
        block = _block()
        for ref in ("Mechanism 702", "Mechanism 539", "Mechanism 666",
                    "Mechanism 64", "Mechanism 412"):
            assert ref in block, ref

    def test_excerpt_bounded_per_503(self):
        block = _fold(_block())
        assert "search-excerpt-bounded per #503" in block
        assert "0 browser.open first-hand reads" in block

    def test_source_url_verbatim(self):
        data = _block_data()
        assert data["source_urls"] == [
            "https://" + BLOOMBERG_URL,
        ]


class TestStatisticalDiscipline794:
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
        assert "ledger holds at 26" in data["falsification_family"]

    def test_designed_keying_no_underscore_form_in_block(self):
        # Per the #715/#723/#738/#739 designed-keying convention, the block
        # key and block text must never carry the contiguous underscore-form
        # marker; the needle is format-built so this test carries no literal.
        block = _block()
        needle = MECH_ID_MARKER
        assert needle not in block
        assert MECH_KEY.count("_" + "708") == 0

    def test_ranked_confounders_and_counterargument(self):
        data = _block_data()
        conf = data["ranked_confounders"]
        assert len(conf) == 5
        assert [c["rank"] for c in conf] == [1, 2, 3, 4, 5]
        assert [c["strength"] for c in conf] == [
            "strong", "strong", "moderate", "moderate", "weak",
        ]
        assert "strongest_counterargument" in data
        assert "defense material" in _fold(data["strongest_counterargument"])


# --- Supersession and corpus post-#793 --------------------------------------


class TestSupersessionAndCorpusPost793:
    def _numeric_ids(self):
        res = _run_git("grep", "-oh", "mechanism_id: [0-9]*", "--", "profiles/")
        return sorted(int(m.group(1)) for m in re.finditer(r"mechanism_id: (\d+)", res.stdout))

    def test_corpus_max_is_708(self):
        assert max(self._numeric_ids()) == 708

    def test_iteration_793_max_707_sweep_superseded_by_design(self):
        # #793's max-707 sweep fails by designed supersession now that 708 exists.
        assert max(self._numeric_ids()) != 707

    def test_zero_underscore_708_profiles_stays_green(self):
        # #794's own underscore-form sweeps stay green by designed keying.
        res = _run_git("grep", "-r", MECH_ID_MARKER, "--", "profiles/")
        assert res.returncode != 0 and not res.stdout.strip()

    def test_zero_underscore_708_tests_stays_green(self):
        res = _run_git("grep", "-r", MECH_ID_MARKER, "--", "tests/")
        assert res.returncode != 0 and not res.stdout.strip()

    def test_zero_underscore_708_docs_stays_green(self):
        res = _run_git("grep", "-r", MECH_ID_MARKER, "--", "docs/")
        assert res.returncode != 0 and not res.stdout.strip()

    def test_zero_numeric_709_in_profiles(self):
        res = _run_git("grep", NEXT_ID_NUMERIC, "--", "profiles/")
        assert res.returncode != 0 and not res.stdout.strip()

    def test_iteration_793_zero_underscore_707_profiles_sweep_stays_green(self):
        res = _run_git("grep", "-r", "mechanism" + "_707", "--", "profiles/")
        assert res.returncode != 0 and not res.stdout.strip()

    def test_iteration_793_zero_underscore_707_tests_sweep_stays_green(self):
        res = _run_git("grep", "-r", "mechanism" + "_707", "--", "tests/")
        assert res.returncode != 0 and not res.stdout.strip()

    def test_iteration_793_zero_numeric_707_fails_by_designed_supersession(self):
        res = _run_git("grep", "-r", "mechanism_id: 707", "--", "profiles/")
        assert res.returncode == 0 and res.stdout.strip(), \
            "expected #793's zero-numeric-707 sweep to fail by designed supersession"


# --- Ledger -----------------------------------------------------------------


def _profiles_corpus():
    out = []
    for root, _dirs, files in os.walk(os.path.join(REPO_ROOT, "profiles")):
        for fn in files:
            if fn.endswith((".yaml", ".yml", ".md")):
                out.append(_read(os.path.join(root, fn)))
    return "\n".join(out)


class TestLedger794:
    def test_twenty_sixth_present_and_twenty_seventh_absent(self):
        # Guard targets the profiles corpus per the #754 convention (prior type
        # files legitimately reference "TWENTY-SEVENTH" inside their own
        # negative guards, so a tests/ sweep would false-positive).
        corpus = _profiles_corpus()
        assert "TWENTY-SIXTH" in corpus
        assert "TWENTY-SEVENTH" not in corpus
        assert "ledger holds at 26" in _block()

    def test_m708_block_key_unique_and_entities_parse(self):
        import yaml

        doc = yaml.safe_load(_read(ENTITIES_PATH))
        assert doc["entities"]["google"][MECH_KEY]["mechanism_id"] == 708
        keys = [
            k for k in doc["entities"]["google"] if k == MECH_KEY
        ]
        assert len(keys) == 1

    def test_m708_not_a_falsification_family_member(self):
        data = _block_data()
        assert data["falsification_family"].startswith("NOT a member")

    def test_no_analysis_json_update_claimed(self):
        data = _block_data()
        assert data["no_analysis_json_update"] is True
        assert "No analysis.json update warranted" in data["artifact_readiness"]


# --- Doc-sync ----------------------------------------------------------------


class TestDocSync794:
    def test_readme_row_794(self):
        assert TEST_BASENAME in _read(README_PATH)

    def test_architecture_row_794(self):
        assert TEST_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_794_file(self):
        text = _read(ARCH_PATH)
        assert "tests/" + TEST_BASENAME in text


# --- Iteration log ------------------------------------------------------------


class TestIterationLog794:
    def _log(self):
        return _read(LOG_PATH)

    def test_log_entry_present(self):
        assert "## #794 Type C:" in self._log()

    def test_log_mechanism_number_and_topic(self):
        log = self._log()
        idx = log.index("## #794 Type C:")
        entry = log[idx:idx + 4000]
        assert "mechanism 708" in entry
        assert "Bloomberg" in entry
        assert "20 national news outlets" in entry

    def test_sep_16_2026_is_wednesday(self):
        import datetime

        assert datetime.date(2026, 9, 16).strftime("%A") == "Wednesday"
