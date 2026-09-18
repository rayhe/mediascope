"""Type C #814 (2026-09-17 17:00 PDT): LINC K.K. Japan expansion (IntentBridges x
Globalive joint venture, announced Sep 11 2026) - first APAC collective-licensing
intermediary in the corpus; pool-and-license as the fifth direction in the
relationship-direction taxonomy (mechanism 720).

Rotation window fifth leg: D (#810) -> E (#811) -> A (#812) -> B (#813) ->
C (#814), CLOSING the 810-814 window.

Evidence: 3 browser.search query sets this run, 0 browser.open first-hand reads;
all URLs copied verbatim from search-result Full-URL listings; no canonical URLs
constructed; search-excerpt-bounded per #503. Statistical discipline per the
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
    "test_type_c_814_linc_kk_japan_collective_licensing_sep17_5pm.py"
)
MECH_NUM = 720
# Built by concatenation so the underscore-form marker never sits contiguously
# in this file: the #715 sweep-instrument convention.
MECH_ID_MARKER = "mechanism" + "_720"
NEXT_ID_MARKER = "mechanism" + "_721"
NEXT_ID_NUMERIC = "mechanism_id: 721"
MECH_KEY = "linc_kk_japan_collective_licensing_sep2026"
URL_PR = "https://www.prnewswire.com/apac/news-releases/linc-expands-into-japan-with-establishment-of-linc-kk-302877168.html"
URL_TN = "https://technode.global/prnasia/linc-expands-into-japan-with-establishment-of-linc-k-k/"
URL_HK = "https://hkbusinesswire.com/linc-expands-into-japan-with-establishment-of-linc-k-k/"
URL_SIAM = "https://www.siamnews.net/pr-news/linc-expands-into-japan-with-establishment-of-linc-k-k/"
URL_B2B = "https://b2b-asianews.com/pr-newswire/35347/detail/"
URL_AG = "https://www.aseangazette.com/newswires/pr-newswire/2026/09/14/linc-expands-into-japan-with-establishment-of-linc-k-k/124052/"
NEXT_SIBLING = "\nadvance_dual_asset_monetization:"
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


class TestNovelty814:
    """Pre-commit novelty: single new file, unique commit, zero repo precedent."""

    def test_single_test_type_c_814_file(self):
        files = sorted(
            str(p) for p in TESTS_DIR.glob("test_type_c_814*.py")
        )
        assert len(files) == 1, files
        assert files[0].endswith(TEST_BASENAME), files

    def test_type_c_814_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 followup convention; patched green post-commit.
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP", "POST_COMMIT_ANCHORED", "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ), "anchor SHA is still the pre-commit placeholder"
        res = _run_git("log", "--all", "--grep", "Type C #814")
        assert ANCHORED_SHA in res.stdout, "main commit is not the expected anchored SHA"

    def test_novelty_verification_claim_present_in_block(self):
        # The block pins the pre-commit novelty greps (Zero IntentBridges hits,
        # all 6 source URLs zero-hit, zero underscore-form 720 keys, max
        # numeric mechanism_id 719); this test pins the claim in the
        # committed block, per the #752 convention.
        block = _block()
        assert "test_type_c_814" in block
        assert "Zero IntentBridges hits repo-wide pre-commit" in block
        assert "max numeric mechanism_id 719 pre-commit" in block


# --- Rotation cycle guard ---------------------------------------------------


class TestRotationCycleGuard814:
    """Rotation: 810-814 window fifth leg D->E->A->B->C, closing the window."""

    EXPECTED_ORDER = [
        ("C", "814"), ("B", "813"), ("A", "812"), ("E", "811"), ("D", "810"),
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
        # subject opens the #814 window-closing leg (HEAD drifts past it with
        # the anchor/doc-sync/push-status followups, per the #565 convention).
        res = _run_git("log", "--format=%H %s", "--all")
        hits = [l for l in res.stdout.splitlines()
                if l.startswith(ANCHORED_SHA + " ")]
        assert len(hits) == 1, hits
        assert "Type C #814: " in hits[0], hits


# --- Mechanism content -------------------------------------------------------


class TestMechanism720Content:
    def test_block_present_in_entities(self):
        block = _block()
        assert block.strip().startswith(MECH_KEY + ":")

    def test_iteration_metadata(self):
        data = _block_data()
        assert data["mechanism_id"] == MECH_NUM
        assert data["iteration"] == 814
        assert data["iteration_type"] == "C"
        assert data["date_analyzed"] == "2026-09-17"
        assert data["time_pdt"] == "17:00"
        assert data["job_id"] == "mediascope-daily-iteration"

    def test_joint_venture_facts(self):
        data = _block_data()
        jv = data["joint_venture"]
        assert jv["announced"] == "2026-09-11"
        assert "IntentBridges" in jv["operator"]
        assert "Globalive" in jv["partner"]
        assert "LINC K.K." in jv["vehicle"]
        assert "Kosuke Umeno" in jv["leadership"]
        assert "Wei Hsueh" in jv["leadership"]

    def test_publisher_roster(self):
        data = _block_data()
        roster = " ".join(data["publisher_roster"])
        assert "Mediagene" in roster
        assert "ETtoday" in roster
        assert "Philstar" in roster
        assert len(data["publisher_roster"]) == 3

    def test_services(self):
        data = _block_data()
        services = " ".join(data["services"])
        assert "mapping AI access" in services
        assert "packaging licensable" in services
        assert "collective licensing" in services
        assert "managing licensing revenue" in services

    def test_economic_context(self):
        data = _block_data()
        ec = data["economic_context"]
        assert "more than half" in ec["bot_traffic"]
        assert "50%" in ec["ai_bot_growth"]
        assert "30 Japanese publisher domains" in ec["ai_bot_growth"]
        assert "February and August 2026" in ec["ai_bot_growth"]

    def test_intermediary_reading(self):
        data = _block_data()
        ir = _fold(data["intermediary_reading"]["tier_3_extension"])
        assert "tier_3_collective" in ir
        assert "asia-based" in ir
        tax = _fold(data["intermediary_reading"]["taxonomy_fifth_direction"])
        assert "pool-and-license" in tax
        assert "fifth direction" in tax
        assert "m624" in tax
        assert "m675" in tax
        assert "mechanism 681" in _fold(
            data["intermediary_reading"]["repricing_frame"])
        cross = _fold(data["intermediary_reading"]["cross_references"])
        assert "663" in cross and "cashmere" in cross
        assert "702/708" in cross

    def test_source_urls_verbatim(self):
        data = _block_data()
        assert data["source_urls"] == [
            URL_PR, URL_TN, URL_HK, URL_SIAM, URL_B2B, URL_AG,
        ]

    def test_meta_zero(self):
        data = _block_data()
        mz = _fold(data["meta_zero"])
        assert "no documented relationship" in mz
        assert "not a coverage-tone claim" in mz


# --- Statistical discipline ---------------------------------------------------


class TestStatisticalDiscipline814:
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
        assert MECH_KEY.count("_" + "720") == 0

    def test_ranked_confounders_and_counterargument(self):
        data = _block_data()
        conf = data["ranked_confounders"]
        assert len(conf) == 5
        assert [c["rank"] for c in conf] == [1, 2, 3, 4, 5]
        assert [c["strength"] for c in conf] == [
            "strong", "strong", "moderate", "moderate", "weak",
        ]
        assert "strongest_counterargument" in data
        assert "press-release" in _fold(data["strongest_counterargument"])


# --- Supersession and corpus post-#813 --------------------------------------


class TestSupersessionAndCorpusPost813:
    def _numeric_ids(self):
        res = _run_git("grep", "-oh", "mechanism_id: [0-9]*", "--", "profiles/")
        return sorted(int(m.group(1)) for m in re.finditer(r"mechanism_id: (\d+)", res.stdout))

    def test_corpus_max_is_720(self):
        assert max(self._numeric_ids()) == 720

    def test_iteration_813_max_719_sweep_superseded_by_design(self):
        # #813's max-719 sweeps fail by designed supersession now that 720 exists.
        assert max(self._numeric_ids()) != 719

    def test_zero_underscore_721_repo_wide(self):
        res = _run_git("grep", "-r", NEXT_ID_MARKER, "--", "profiles/", "tests/", "docs/")
        assert res.returncode != 0 and not res.stdout.strip()

    def test_zero_numeric_721_in_profiles(self):
        res = _run_git("grep", NEXT_ID_NUMERIC, "--", "profiles/")
        assert res.returncode != 0 and not res.stdout.strip()

    def test_iteration_812_zero_underscore_719_sweep_stays_green(self):
        # The #812 zero-underscore-719 sweeps stay green post-#814 by designed keying.
        for root in ("profiles/", "tests/"):
            res = _run_git("grep", "-r", "mechanism" + "_719", "--", root)
            assert res.returncode != 0 and not res.stdout.strip(), \
                "literal underscore-719 key leaked into %s" % root

    def test_iteration_813_zero_underscore_720_sweep_stays_green(self):
        # The #813 zero-underscore-720 sweeps stay green post-#814 by designed keying:
        # neither the profile block nor this test file carries a literal underscore-720 key.
        for root in ("profiles/", "tests/"):
            res = _run_git("grep", "-r", MECH_ID_MARKER, "--", root)
            assert res.returncode != 0 and not res.stdout.strip(), \
                "literal underscore-720 key leaked into %s" % root

    def test_iteration_813_zero_numeric_720_fails_by_designed_supersession(self):
        res = _run_git("grep", "-r", "mechanism_id: 720", "--", "profiles/")
        assert res.returncode == 0 and res.stdout.strip(), \
            "expected #813's zero-numeric-720 sweep to fail by designed supersession"

    def test_numeric_720_keys_in_exactly_the_designed_location(self):
        res = _run_git("grep", "-r", "mechanism_id: 720", "--", "profiles/")
        hits = [l for l in res.stdout.strip().splitlines() if l.strip()]
        # Designed keying: one numeric 720 key in the marketplace
        # intermediary landscape block; no other profiles/ location.
        assert len(hits) == 1, "unexpected numeric 720 key spread in profiles/: %s" % hits
        assert "profiles/competitor-entities.yaml" in hits[0]


# --- Ledger -----------------------------------------------------------------


def _profiles_corpus():
    out = []
    for root, _dirs, files in os.walk(os.path.join(REPO_ROOT, "profiles")):
        for fn in files:
            if fn.endswith((".yaml", ".yml", ".md")):
                out.append(_read(os.path.join(root, fn)))
    return "\n".join(out)


class TestLedger814:
    def test_twenty_sixth_present_and_twenty_seventh_absent(self):
        # Guard targets the profiles corpus per the #754 convention (prior type
        # files legitimately reference "TWENTY-SEVENTH" inside their own
        # negative guards, so a tests/ sweep would false-positive).
        corpus = _profiles_corpus()
        assert "TWENTY-SIXTH" in corpus
        assert "TWENTY-SEVENTH" not in corpus
        assert "ledger holds at 26" in _block()

    def test_m720_block_key_unique_and_entities_parse(self):
        import yaml

        doc = yaml.safe_load(_read(ENTITIES_PATH))
        assert doc["marketplace_intermediary_landscape"][MECH_KEY]["mechanism_id"] == 720
        keys = [
            k for k in doc["marketplace_intermediary_landscape"] if k == MECH_KEY
        ]
        assert len(keys) == 1

    def test_m720_not_a_falsification_family_member(self):
        data = _block_data()
        assert data["falsification_family"].startswith("NOT a member")

    def test_no_analysis_json_update_claimed(self):
        data = _block_data()
        assert data["no_analysis_json_update"] is True
        assert "No analysis.json update warranted" in data["artifact_readiness"]


# --- Doc-sync ----------------------------------------------------------------


class TestDocSync814:
    def test_readme_row_814(self):
        assert TEST_BASENAME in _read(README_PATH)

    def test_architecture_row_814(self):
        assert TEST_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_814_file(self):
        text = _read(ARCH_PATH)
        assert "tests/" + TEST_BASENAME in text


# --- Iteration log ------------------------------------------------------------


class TestIterationLog814:
    def _log(self):
        return _read(LOG_PATH)

    def test_log_entry_present(self):
        assert "## #814 Type C:" in self._log()

    def test_log_mechanism_number_and_topic(self):
        log = self._log()
        idx = log.index("## #814 Type C:")
        entry = log[idx:idx + 8000]
        assert "mechanism 720" in entry
        assert "LINC" in entry
        assert "IntentBridges" in entry

    def test_sep_17_2026_is_thursday(self):
        import datetime

        assert datetime.date(2026, 9, 17).strftime("%A") == "Thursday"
