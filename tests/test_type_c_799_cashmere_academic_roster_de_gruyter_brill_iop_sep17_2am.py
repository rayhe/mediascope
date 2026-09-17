"""Type C #799 (2026-09-17 02:00 PDT): Cashmere September 2026
academic-publisher roster expansion - De Gruyter Brill (Sep 14) + IOP
Publishing (Sep 9) - inference-only, no-training-rights template extends
into the scholarly vertical; the two newest Cashmere premium-data legs
(mechanism 711).

Rotation window fifth leg: D (#795) -> E (#796) -> A (#797) -> B (#798) ->
C (#799), CLOSING the 795-799 window.

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
    "test_type_c_799_cashmere_academic_roster_de_gruyter_brill_iop_sep17_2am.py"
)
MECH_NUM = 711
# Built by concatenation so the underscore-form marker never sits contiguously
# in this file: the #715 sweep-instrument convention.
MECH_ID_MARKER = "mechanism" + "_711"
NEXT_ID_MARKER = "mechanism" + "_712"
NEXT_ID_NUMERIC = "mechanism_id: 712"
MECH_KEY = "cashmere_academic_roster_expansion_de_gruyter_brill_iop_publishing_sep2026"
DGR_URL = (
    "www.degruyterbrill.com/publishing/about-us/news-insights/press-releases/"
    "cashmere-and-de-gruyter-brill-partner-to-bring-trusted-academic-"
    "scholarship-to-ai-platforms-safely-with-control-and-at-scale"
)
EIN_URL = (
    "world.einnews.com/pr_news/941536628/cashmere-de-gruyter-brill-partner-"
    "to-bring-trusted-academic-scholarship-to-ai-platforms-safely-and-"
    "with-control"
)
IOP_URL = (
    "globalbookreview.com/cashmere-and-iop-publishing-to-expand-access-to-"
    "trusted-physical-sciences-research-through-ai/"
)
NEXT_SIBLING = "\n    getty_perplexity_visual_licensing_oct2025_sep14:"
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


class TestNovelty799:
    """Pre-commit novelty: single new file, unique commit, zero repo precedent."""

    def test_single_test_type_c_799_file(self):
        files = sorted(
            str(p) for p in TESTS_DIR.glob("test_type_c_799*.py")
        )
        assert len(files) == 1, files
        assert files[0].endswith(TEST_BASENAME), files

    def test_type_c_799_main_commit_unique(self):
        mains = _git_log_mains(r"Type C #799: ")
        # Pre-commit there is no #799 main commit yet; at most one may exist.
        assert len(mains) <= 1, mains

    def test_novelty_verification_claim_present_in_block(self):
        # The block pins the pre-commit novelty greps (zero files on disk, no
        # Type C #799 in git log, De Gruyter / IOP Publishing zero-hit,
        # source URLs zero-hit, zero underscore-form 711 keys, max numeric
        # mechanism_id 710); this test pins the claim in the committed block,
        # per the #752 convention.
        block = _block()
        assert "test_type_c_799 files on disk" in block
        assert "Type C #799 in git log" in block
        assert "De Gruyter" in block
        assert "IOP Publishing" in block
        assert "941536628" in block
        assert "max numeric mechanism_id 710 pre-commit" in block


class TestRotationCycleGuard799:
    """Rotation: 795-799 window fifth leg D->E->A->B->C, closing the window."""

    EXPECTED_ORDER = [
        ("C", "799"), ("B", "798"), ("A", "797"), ("E", "796"), ("D", "795"),
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
        mains = _git_log_mains(r"Type C #799: ")
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP", "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ), mains
        assert mains and mains[0].startswith(ANCHORED_SHA + " "), mains


class TestMechanism711Content:
    def test_block_present_in_entities(self):
        block = _block()
        assert block.strip().startswith(MECH_KEY + ":")

    def test_iteration_metadata(self):
        data = _block_data()
        assert data["mechanism_id"] == MECH_NUM
        assert data["iteration"] == 799
        assert data["iteration_type"] == "C"
        assert data["date_analyzed"] == "2026-09-17"
        assert data["time_pdt"] == "02:00"
        assert data["job_id"] == "mediascope-daily-iteration"

    def test_deal_parties_and_buyer_side(self):
        data = _block_data()
        parties = data["deal_parties"]
        assert parties["infrastructure_operator"].startswith("Cashmere")
        assert "De Gruyter Brill" in parties["publisher_leg_1"]
        assert "IOP Publishing" in parties["publisher_leg_2"]
        assert "no named AI lab counterparty" in parties["buyer_side"]

    def test_de_gruyter_brill_leg(self):
        data = _block_data()
        leg = data["de_gruyter_brill_leg"]
        assert leg["announced"] == "2026-09-14"
        assert "3,500 books and 800 journals" in leg["catalogue_scale"]
        assert "never used to train large language models" in leg[
            "training_boundary"]
        assert "1749" in leg["provenance"] and "1683" in leg["provenance"]

    def test_iop_publishing_leg(self):
        data = _block_data()
        leg = data["iop_publishing_leg"]
        assert leg["announced"] == "2026-09-09"
        assert "not-for-profit" in _fold(data["deal_parties"]["publisher_leg_2"])
        assert "unauthorised use in LLM training" in leg["training_boundary"]
        assert "licensed for inference, protected from training use" in leg[
            "ceo_quote"]

    def test_cross_references(self):
        block = _fold(_block())
        for ref in ("mechanism 663", "mechanism 699", "mechanism 684"):
            assert ref in block, ref

    def test_excerpt_bounded_per_503(self):
        block = _fold(_block())
        assert "search-excerpt-bounded per #503" in block
        assert "0 browser.open first-hand reads" in block

    def test_source_urls_verbatim(self):
        data = _block_data()
        assert data["source_urls"] == [
            "https://" + DGR_URL,
            "https://" + EIN_URL,
            "https://" + IOP_URL,
        ]


class TestStatisticalDiscipline799:
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
        assert MECH_KEY.count("_" + "711") == 0

    def test_ranked_confounders_and_counterargument(self):
        data = _block_data()
        conf = data["ranked_confounders"]
        assert len(conf) == 5
        assert [c["rank"] for c in conf] == [1, 2, 3, 4, 5]
        assert [c["strength"] for c in conf] == [
            "strong", "strong", "moderate", "moderate", "weak",
        ]
        assert "strongest_counterargument" in data
        assert "anti-extraction template" in _fold(
            data["strongest_counterargument"])


# --- Supersession and corpus post-#798 --------------------------------------


class TestSupersessionAndCorpusPost798:
    def _numeric_ids(self):
        res = _run_git("grep", "-oh", "mechanism_id: [0-9]*", "--", "profiles/")
        return sorted(int(m.group(1)) for m in re.finditer(r"mechanism_id: (\d+)", res.stdout))

    def test_corpus_max_is_711(self):
        assert max(self._numeric_ids()) == 711

    def test_iteration_798_max_710_sweep_superseded_by_design(self):
        # #798's max-710 sweep fails by designed supersession now that 711 exists.
        assert max(self._numeric_ids()) != 710

    def test_zero_underscore_711_profiles_stays_green(self):
        # #799's own underscore-form sweeps stay green by designed keying.
        res = _run_git("grep", "-r", MECH_ID_MARKER, "--", "profiles/")
        assert res.returncode != 0 and not res.stdout.strip()

    def test_zero_underscore_711_tests_stays_green(self):
        res = _run_git("grep", "-r", MECH_ID_MARKER, "--", "tests/")
        assert res.returncode != 0 and not res.stdout.strip()

    def test_zero_underscore_711_docs_stays_green(self):
        res = _run_git("grep", "-r", MECH_ID_MARKER, "--", "docs/")
        assert res.returncode != 0 and not res.stdout.strip()

    def test_zero_numeric_712_in_profiles(self):
        res = _run_git("grep", NEXT_ID_NUMERIC, "--", "profiles/")
        assert res.returncode != 0 and not res.stdout.strip()

    def test_iteration_798_zero_underscore_710_profiles_sweep_stays_green(self):
        res = _run_git("grep", "-r", "mechanism" + "_710", "--", "profiles/")
        assert res.returncode != 0 and not res.stdout.strip()

    def test_iteration_798_zero_underscore_710_tests_sweep_stays_green(self):
        res = _run_git("grep", "-r", "mechanism" + "_710", "--", "tests/")
        assert res.returncode != 0 and not res.stdout.strip()

    def test_iteration_798_zero_numeric_710_fails_by_designed_supersession(self):
        res = _run_git("grep", "-r", "mechanism_id: 710", "--", "profiles/")
        assert res.returncode == 0 and res.stdout.strip(), \
            "expected #798's zero-numeric-710 sweep to fail by designed supersession"


# --- Ledger -----------------------------------------------------------------


def _profiles_corpus():
    out = []
    for root, _dirs, files in os.walk(os.path.join(REPO_ROOT, "profiles")):
        for fn in files:
            if fn.endswith((".yaml", ".yml", ".md")):
                out.append(_read(os.path.join(root, fn)))
    return "\n".join(out)


class TestLedger799:
    def test_twenty_sixth_present_and_twenty_seventh_absent(self):
        # Guard targets the profiles corpus per the #754 convention (prior type
        # files legitimately reference "TWENTY-SEVENTH" inside their own
        # negative guards, so a tests/ sweep would false-positive).
        corpus = _profiles_corpus()
        assert "TWENTY-SIXTH" in corpus
        assert "TWENTY-SEVENTH" not in corpus
        assert "ledger holds at 26" in _block()

    def test_m711_block_key_unique_and_entities_parse(self):
        import yaml

        doc = yaml.safe_load(_read(ENTITIES_PATH))
        assert doc["entities"]["perplexity"][MECH_KEY]["mechanism_id"] == 711
        keys = [
            k for k in doc["entities"]["perplexity"] if k == MECH_KEY
        ]
        assert len(keys) == 1

    def test_m711_not_a_falsification_family_member(self):
        data = _block_data()
        assert data["falsification_family"].startswith("NOT a member")

    def test_no_analysis_json_update_claimed(self):
        data = _block_data()
        assert data["no_analysis_json_update"] is True
        assert "No analysis.json update warranted" in data["artifact_readiness"]


# --- Doc-sync ----------------------------------------------------------------


class TestDocSync799:
    def test_readme_row_799(self):
        assert TEST_BASENAME in _read(README_PATH)

    def test_architecture_row_799(self):
        assert TEST_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_799_file(self):
        text = _read(ARCH_PATH)
        assert "tests/" + TEST_BASENAME in text


# --- Iteration log ------------------------------------------------------------


class TestIterationLog799:
    def _log(self):
        return _read(LOG_PATH)

    def test_log_entry_present(self):
        assert "## #799 Type C:" in self._log()

    def test_log_mechanism_number_and_topic(self):
        log = self._log()
        idx = log.index("## #799 Type C:")
        entry = log[idx:idx + 4000]
        assert "mechanism 711" in entry
        assert "De Gruyter" in entry
        assert "Cashmere" in entry

    def test_sep_17_2026_is_thursday(self):
        import datetime

        assert datetime.date(2026, 9, 17).strftime("%A") == "Thursday"
