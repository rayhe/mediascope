"""Type C #804 (2026-09-17 07:00 PDT): OpenAI x Village Media first Canadian
news deal (announced Sep 16 2026, Axios/Sara Fischer) - funding + API
credits + technical support for the Open Door community navigator in
exchange for attributed citation in ChatGPT; the OpenAI local-news
template crosses into Canada (mechanism 714).

Rotation window fifth leg: D (#800) -> E (#801) -> A (#802) -> B (#803) ->
C (#804), CLOSING the 800-804 window.

Evidence is search-excerpt-bounded per #503 (3 browser.search query sets, 0
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
    "test_type_c_804_openai_village_media_first_canada_news_deal_sep17_7am.py"
)
MECH_NUM = 714
# Built by concatenation so the underscore-form marker never sits contiguously
# in this file: the #715 sweep-instrument convention.
MECH_ID_MARKER = "mechanism" + "_714"
NEXT_ID_MARKER = "mechanism" + "_715"
NEXT_ID_NUMERIC = "mechanism_id: 715"
MECH_KEY = "openai_village_media_first_canada_news_deal_sep2026"
EP_URL = (
    "www.editorandpublisher.com/stories/"
    "openai-strikes-first-news-deal-in-canada,263557"
)
PG_URL = (
    "pressgazette.co.uk/platforms/"
    "news-publisher-ai-deals-lawsuits-openai-google/"
)
NEXT_SIBLING = "\n  anthropic:"
ANCHORED_SHA = "ffcd0c73c56e994d5ebe2d3cf2bdc0fe72f12dda"


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


# --- Novelty ---------------------------------------------------------------


class TestNovelty804:
    """Pre-commit novelty: single new file, unique commit, zero repo precedent."""

    def test_single_test_type_c_804_file(self):
        files = sorted(
            str(p) for p in TESTS_DIR.glob("test_type_c_804*.py")
        )
        assert len(files) == 1, files
        assert files[0].endswith(TEST_BASENAME), files

    def test_type_c_804_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 followup convention; patched green post-commit.
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP", "POST_COMMIT_ANCHORED", "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ), "anchor SHA is still the pre-commit placeholder"
        res = _run_git("log", "--all", "--grep", "Type C #804")
        assert ANCHORED_SHA in res.stdout, "main commit is not the expected anchored SHA"

    def test_novelty_verification_claim_present_in_block(self):
        # The block pins the pre-commit novelty greps (zero Village Media /
        # Open Door hits, source URLs zero-hit, zero underscore-form 714
        # keys, max numeric mechanism_id 713); this test pins the claim in
        # the committed block, per the #752 convention.
        block = _block()
        assert "test_type_c_804" in block
        assert "Village Media" in block
        assert "Open Door" in block
        assert "max numeric mechanism_id 713 pre-commit" in block


# --- Rotation cycle guard ---------------------------------------------------


class TestRotationCycleGuard804:
    """Rotation: 800-804 window fifth leg D->E->A->B->C, closing the window."""

    EXPECTED_ORDER = [
        ("C", "804"), ("B", "803"), ("A", "802"), ("E", "801"), ("D", "800"),
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
        # subject opens the #804 window-closing leg (HEAD drifts past it with
        # the anchor/doc-sync/push-status followups, per the #565 convention).
        res = _run_git("log", "--format=%H %s", "--all")
        hits = [l for l in res.stdout.splitlines()
                if l.startswith(ANCHORED_SHA + " ")]
        assert len(hits) == 1, hits
        assert "Type C #804: " in hits[0], hits


# --- Mechanism content -------------------------------------------------------


class TestMechanism714Content:
    def test_block_present_in_entities(self):
        block = _block()
        assert block.strip().startswith(MECH_KEY + ":")

    def test_iteration_metadata(self):
        data = _block_data()
        assert data["mechanism_id"] == MECH_NUM
        assert data["iteration"] == 804
        assert data["iteration_type"] == "C"
        assert data["date_analyzed"] == "2026-09-17"
        assert data["time_pdt"] == "07:00"
        assert data["job_id"] == "mediascope-daily-iteration"

    def test_deal_parties(self):
        data = _block_data()
        parties = data["deal_parties"]
        assert "Village Media" in parties["publisher_counterparty"]
        assert "30 local news websites" in parties["publisher_counterparty"]
        assert "OpenAI" in parties["payer_counterparty"]
        assert "Varun Shetty" in parties["payer_counterparty"]
        assert "API credits" in parties["consideration_openai"]
        assert "citation of Village Media content in ChatGPT" in parties[
            "consideration_village_media"]
        assert "Sault Ste. Marie" in parties["product"]

    def test_local_news_template_leg(self):
        data = _block_data()
        block = _fold(data["local_news_template"])
        assert "axios" in block
        assert "jan 2025" in block
        assert "open door" in block
        assert "attribution-discovery" in block

    def test_bounded_absences(self):
        data = _block_data()
        joined = _fold(" ".join(data["bounded_absences_this_run"]))
        assert "mechanism 630" in joined
        assert "mechanism 606" in joined
        assert "mechanisms 702/708" in joined
        assert "umg" in joined and "elevenlabs" in joined

    def test_cross_references(self):
        block = _fold(_block())
        for ref in ("mechanism 519", "mechanism 630", "mechanism 606"):
            assert ref in block, ref

    def test_excerpt_bounded_per_503(self):
        block = _fold(_block())
        assert "search-excerpt-bounded per #503" in block
        assert "0 browser.open first-hand reads" in block

    def test_source_urls_verbatim(self):
        data = _block_data()
        assert data["source_urls"] == [
            "https://" + EP_URL,
            "https://" + PG_URL,
        ]


# --- Statistical discipline ---------------------------------------------------


class TestStatisticalDiscipline804:
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
        assert MECH_KEY.count("_" + "714") == 0

    def test_ranked_confounders_and_counterargument(self):
        data = _block_data()
        conf = data["ranked_confounders"]
        assert len(conf) == 5
        assert [c["rank"] for c in conf] == [1, 2, 3, 4, 5]
        assert [c["strength"] for c in conf] == [
            "strong", "strong", "moderate", "moderate", "weak",
        ]
        assert "strongest_counterargument" in data
        assert "survival play" in _fold(data["strongest_counterargument"])


# --- Supersession and corpus post-#803 --------------------------------------


class TestSupersessionAndCorpusPost803:
    def _numeric_ids(self):
        res = _run_git("grep", "-oh", "mechanism_id: [0-9]*", "--", "profiles/")
        return sorted(int(m.group(1)) for m in re.finditer(r"mechanism_id: (\d+)", res.stdout))

    def test_corpus_max_is_714(self):
        assert max(self._numeric_ids()) == 714

    def test_iteration_803_max_713_sweep_superseded_by_design(self):
        # #803's max-713 sweep fails by designed supersession now that 714 exists.
        assert max(self._numeric_ids()) != 713

    def test_zero_underscore_714_profiles_stays_green(self):
        # #804's own underscore-form sweeps stay green by designed keying.
        res = _run_git("grep", "-r", MECH_ID_MARKER, "--", "profiles/")
        assert res.returncode != 0 and not res.stdout.strip()

    def test_zero_underscore_714_tests_stays_green(self):
        res = _run_git("grep", "-r", MECH_ID_MARKER, "--", "tests/")
        assert res.returncode != 0 and not res.stdout.strip()

    def test_zero_underscore_714_docs_stays_green(self):
        res = _run_git("grep", "-r", MECH_ID_MARKER, "--", "docs/")
        assert res.returncode != 0 and not res.stdout.strip()

    def test_zero_numeric_715_in_profiles(self):
        res = _run_git("grep", NEXT_ID_NUMERIC, "--", "profiles/")
        assert res.returncode != 0 and not res.stdout.strip()

    def test_iteration_803_zero_underscore_713_profiles_sweep_stays_green(self):
        res = _run_git("grep", "-r", "mechanism" + "_713", "--", "profiles/")
        assert res.returncode != 0 and not res.stdout.strip()

    def test_iteration_803_zero_underscore_713_tests_sweep_stays_green(self):
        res = _run_git("grep", "-r", "mechanism" + "_713", "--", "tests/")
        assert res.returncode != 0 and not res.stdout.strip()

    def test_iteration_803_zero_numeric_713_fails_by_designed_supersession(self):
        res = _run_git("grep", "-r", "mechanism_id: 713", "--", "profiles/")
        assert res.returncode == 0 and res.stdout.strip(), \
            "expected #803's zero-numeric-713 sweep to fail by designed supersession"


# --- Ledger -----------------------------------------------------------------


def _profiles_corpus():
    out = []
    for root, _dirs, files in os.walk(os.path.join(REPO_ROOT, "profiles")):
        for fn in files:
            if fn.endswith((".yaml", ".yml", ".md")):
                out.append(_read(os.path.join(root, fn)))
    return "\n".join(out)


class TestLedger804:
    def test_twenty_sixth_present_and_twenty_seventh_absent(self):
        # Guard targets the profiles corpus per the #754 convention (prior type
        # files legitimately reference "TWENTY-SEVENTH" inside their own
        # negative guards, so a tests/ sweep would false-positive).
        corpus = _profiles_corpus()
        assert "TWENTY-SIXTH" in corpus
        assert "TWENTY-SEVENTH" not in corpus
        assert "ledger holds at 26" in _block()

    def test_m714_block_key_unique_and_entities_parse(self):
        import yaml

        doc = yaml.safe_load(_read(ENTITIES_PATH))
        assert doc["entities"]["openai"][MECH_KEY]["mechanism_id"] == 714
        keys = [
            k for k in doc["entities"]["openai"] if k == MECH_KEY
        ]
        assert len(keys) == 1

    def test_m714_not_a_falsification_family_member(self):
        data = _block_data()
        assert data["falsification_family"].startswith("NOT a member")

    def test_no_analysis_json_update_claimed(self):
        data = _block_data()
        assert data["no_analysis_json_update"] is True
        assert "No analysis.json update warranted" in data["artifact_readiness"]


# --- Doc-sync ----------------------------------------------------------------


class TestDocSync804:
    def test_readme_row_804(self):
        assert TEST_BASENAME in _read(README_PATH)

    def test_architecture_row_804(self):
        assert TEST_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_804_file(self):
        text = _read(ARCH_PATH)
        assert "tests/" + TEST_BASENAME in text


# --- Iteration log ------------------------------------------------------------


class TestIterationLog804:
    def _log(self):
        return _read(LOG_PATH)

    def test_log_entry_present(self):
        assert "## #804 Type C:" in self._log()

    def test_log_mechanism_number_and_topic(self):
        log = self._log()
        idx = log.index("## #804 Type C:")
        entry = log[idx:idx + 8000]
        assert "mechanism_id 714" in entry
        assert "Village Media" in entry
        assert "Open Door" in entry

    def test_sep_17_2026_is_thursday(self):
        import datetime

        assert datetime.date(2026, 9, 17).strftime("%A") == "Thursday"
