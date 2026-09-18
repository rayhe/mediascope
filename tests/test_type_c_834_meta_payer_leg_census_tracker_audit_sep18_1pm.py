"""Type C #834 (830-834 window, fifth leg D->E->A->B->C, CLOSING the window):
Meta AI payer-leg census reconciliation and publisher-deal tracker audit,
Sep 2026 (mechanism 732).

FIRST corpus reconciliation of Meta's AI-content payer legs against the
publisher-deal trackers. First-hand browser.open read of the Press Gazette
Who is suing, who is signing tracker (Sep 18 2026, 1641 rendered lines):
the signed-deals index lists exactly three Meta entries - News Corp - Meta
(Mar 2026, up to $50M per year), CNN, Fox News, People Inc and more - Meta
(Dec 5 2025 bundle, collapsed into one row), Reuters - Meta (Oct 25 2024).

CORRECTION: the corpus claim at competitor-entities.yaml mechanism 489
meta_leg_status (Press Gazette Sep 2026 tracker maps only Reuters - Meta on
the Meta column) is STALE and is superseded by this read; the tracker maps
three Meta entries, not one.

Reconciled census of corpus-documented Meta payer legs (13 named
counterparties, ALL ACTIVE per the #599/#609 bounded-absence convention):
(1) Reuters Oct 25 2024 multiyear AI news licensing (m633); (2-9) Dec 5 2025
seven-publisher bundle (m331): CNN, Fox News, Fox Sports, Le Monde Group,
People Inc, The Daily Caller, The Washington Examiner, USA Today + USA
Today Network; (10) News Corp Mar 2026 up to $50M/yr, at least three years
(m549); (11-13) Mar 2026 European bundle: Le Figaro, Prisa, Sueddeutsche
Zeitung.

Tracker divergence: Press Gazette 3 entries (bundle collapsed, European
bundle absent) vs LLM Pulse Sep 2026 9 named Meta partners. Single-tracker
universes undercount Meta's payer footprint 4x to 13x; the reconciled
census is the authoritative base for payer-softening tests.

Sue-ledger additions (verified new to corpus pre-commit): Editorial Perfil
vs OpenAI/Microsoft (Aug 26 2026, first Spanish-language publisher suit);
Wikihow vs OpenAI (Aug 22 2026).

MANUAL / qualitative only; census and tracker audit, not a tone test;
scorer none; tone NOT_SCORED; p_value/cohens_d/ci_95 NOT_CALCULATED;
is_significant False; verdict census_reconciled_correction_issued; NOT a
falsification-family member (tracker audit + source-freshness correction,
not a uniform-prediction test); ledger holds at 26; no analysis.json
update. Novelty verified pre-commit (zero test_type_c_834 files; no
Type C #834 in git log; max numeric mechanism_id 731; zero underscore-form
732 keys by designed keying per #715; block key zero-hit; zero Editorial
Perfil / Wikihow hits repo-wide; mpost.io/meta-finalizes and tradingview
gurufocus:fea467ea9094b zero-hit repo-wide); count_stats gate (delta =
this file exactly); 830-834 window fifth leg D->E->A->B->C, CLOSING the
window (anchor patched post-commit per #565) - Sep 18 2026 13:00 PDT.
"""

import re
import subprocess
from pathlib import Path

import pytest
import yaml

TEST_BASENAME = "test_type_c_834_meta_payer_leg_census_tracker_audit_sep18_1pm.py"
MECH_KEY = "meta_payer_leg_census_and_tracker_audit_sep2026"
M_ID = 732
ITER = 834
TYPE_LETTER = "C"
# Concatenated so this file never contains the literal marker itself.
MECH_ID_MARKER = "mechanism" + "_732"
NEXT_ID_MARKER = "mechanism" + "_733"
NEXT_ID_NUMERIC = "mechanism_id: 733"
EXPECTED_ORDER = [("C", "834"), ("B", "833"), ("A", "832"), ("E", "831"), ("D", "830")]
# Patched to the real main-commit SHA in the anchor followup per the #565 convention.
ANCHORED_SHA = "5a2bad706fea659adebaabcaddda1274f98a1dd0"

EXPECTED_URLS = [
    "https://pressgazette.co.uk/platforms/news-publisher-ai-deals-lawsuits-openai-google/",
    "https://www.wsj.com/business/media/news-corp-meta-in-ai-content-licensing-deal-worth-up-to-50-million-a-year-d4fbf244",
    "https://techcrunch.com/2025/12/05/meta-signs-commercial-ai-data-agreements-with-publishers-to-offer-real-time-news-on-meta-ai/",
    "https://mpost.io/meta-finalizes-ai-licensing-deals-with-major-publishers-to-deliver-real-time-news-in-meta-ai/",
    "https://www.tradingview.com/news/gurufocus:fea467ea9094b:0-meta-platforms-signs-multiple-ai-content-deals-with-major-news-publishers/",
]

CENSUS_NAMES = [
    "Reuters",
    "CNN",
    "Fox News",
    "Fox Sports",
    "Le Monde Group",
    "People Inc",
    "The Daily Caller",
    "The Washington Examiner",
    "USA Today",
    "News Corp",
    "Le Figaro",
    "Prisa",
    "Sueddeutsche Zeitung",
]


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def _entities_text() -> str:
    return (_repo_root() / "profiles" / "competitor-entities.yaml").read_text()


def _block() -> str:
    text = _entities_text()
    start = text.index(MECH_KEY)
    end = text.index("\nadvance_dual_asset_monetization:")
    return text[start:end]


def _mech() -> dict:
    d = yaml.safe_load(_entities_text())
    return d["marketplace_intermediary_landscape"][MECH_KEY]


def _corpus_ids() -> list:
    ids = []
    for p in (_repo_root() / "profiles").rglob("*.yaml"):
        for m in re.finditer(r"mechanism_id:\s*(\d+)", p.read_text(errors="ignore")):
            ids.append(int(m.group(1)))
    return ids


def _repo_grep(needle: str, roots=("profiles", "tests")) -> list:
    hits = []
    root = _repo_root()
    for r in roots:
        for p in (root / r).rglob("*"):
            if p.is_file() and p.suffix in (".py", ".yaml", ".md", ".json"):
                try:
                    if needle in p.read_text(errors="ignore"):
                        hits.append(str(p.relative_to(root)))
                except OSError:
                    pass
    return hits


def _git(*args: str) -> str:
    return subprocess.run(
        ["git", *args],
        cwd=_repo_root(),
        capture_output=True,
        text=True,
        check=True,
    ).stdout


def _git_log_mains(qualifier: str) -> dict:
    out = _git("log", "--all", "--format=%H %s", "--grep", qualifier)
    mains = {}
    for line in out.splitlines():
        if not line.strip():
            continue
        sha, _, subject = line.partition(" ")
        if "Type C #834" in subject:
            mains[sha] = subject
    return mains


def _window(n: int = 40) -> list:
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


def _iteration_log_tail() -> str:
    return (_repo_root() / "iteration-log.md").read_text()[-12000:]


class TestNovelty834:
    def test_single_test_type_c_834_file(self):
        files = list((_repo_root() / "tests").glob("test_type_c_834*"))
        assert files == [Path(__file__)], (
            "exactly one test_type_c_834 file (this one) must exist"
        )

    def test_type_c_834_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 followup convention; patched
        # green post-commit. Novelty was verified pre-commit by shell
        # greps (zero test_type_c_834 files, no #834 in git log, max numeric
        # mechanism_id 731, zero underscore-form 732 keys, block key
        # zero-hit, zero Editorial Perfil / Wikihow hits, two new source
        # URLs zero-hit); this test pins that no duplicate #834 main commit
        # ever appears.
        mains = _git_log_mains("Type C #834: Meta payer")
        assert len(mains) == 1, f"exactly one Type C #834 main commit, got {mains}"
        assert ANCHORED_SHA in mains, (
            "patched SHA must match a real Type C #834 main commit"
        )


class TestRotationCycleGuard834:
    ORDER = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}

    def test_window_is_830_834_fifth_leg(self):
        window = _window()
        assert window[: len(EXPECTED_ORDER)] == EXPECTED_ORDER, (
            f"830-834 window fifth leg D->E->A->B->C: expected {EXPECTED_ORDER}, "
            f"got {window[: len(EXPECTED_ORDER)]}"
        )

    def test_rotation_adjacency_cycle_valid(self):
        window = _window()
        for (t1, n1), (t2, n2) in zip(window, window[1:]):
            assert int(n1) == int(n2) + 1
            assert (self.ORDER[t1] - self.ORDER[t2]) % 5 == 1, (t1, t2)

    def test_predecessor_is_type_b_833(self):
        window = _window()
        assert window[1] == ("B", "833"), (
            f"immediate predecessor must be Type B #833, got {window[1]}"
        )

    def test_anchor_sha_matches_head(self):
        mains = _git_log_mains("Type C #834: Meta payer")
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ), mains
        newest_sha = next(iter(mains))
        assert newest_sha == ANCHORED_SHA, mains


class TestMechanism732Content:
    def test_block_key_exists_in_competitor_entities(self):
        assert MECH_KEY in _entities_text()

    def test_mechanism_id_is_732(self):
        assert _mech()["mechanism_id"] == M_ID

    def test_max_numeric_id_is_732_no_733(self):
        assert max(_corpus_ids()) == 732
        assert not any(
            NEXT_ID_NUMERIC in p.read_text(errors="ignore")
            for p in (_repo_root() / "profiles").rglob("*.yaml")
        ), "no numeric 733 mechanism id may exist pre #835"

    def test_census_totals_13_named_counterparties(self):
        mech = _mech()
        assert mech["census"]["total_named_counterparties"] == 13
        block = _block()
        for name in CENSUS_NAMES:
            assert name in block, f"mechanism block must name {name}"

    def test_tracker_read_first_hand_three_meta_entries(self):
        block = _block()
        assert "1641 rendered lines" in block
        assert "News Corp - Meta" in block
        assert "CNN, Fox News, People Inc and more - Meta" in block
        assert "Reuters - Meta" in block

    def test_stale_claim_correction_present(self):
        block = _block()
        assert "maps only Reuters - Meta on the Meta column" in block
        assert "STALE" in block
        assert "THREE Meta entries" in block

    def test_editorial_perfil_ledger_entry(self):
        block = _block()
        assert "Editorial Perfil" in block
        assert "Aug 26 2026" in block
        assert "first Spanish-language publisher" in block

    def test_wikihow_ledger_entry(self):
        block = _block()
        assert "Wikihow" in block
        assert "Aug 22 2026" in block

    def test_tracker_divergence_llm_pulse_nine(self):
        block = _block()
        assert "9 named Meta partners" in block
        assert "European bundle absent" in block
        assert "4x to 13x" in block

    def test_verdict_census_reconciled(self):
        assert _mech()["verdict"] == "census_reconciled_correction_issued"

    def test_no_analysis_json_update(self):
        mech = _mech()
        assert mech["no_analysis_json_update"] is True
        assert mech["artifact_grade"] is False

    def test_statistical_discipline_qualitative(self):
        sd = _mech()["statistical_discipline"]
        assert sd["scorer"] == "none"
        assert sd["tone_scores"] == "NOT_SCORED"
        assert sd["p_value"] == "NOT_CALCULATED"
        assert sd["cohens_d"] == "NOT_CALCULATED"
        assert sd["ci_95"] == "NOT_CALCULATED"
        assert sd["is_significant"] is False
        assert sd["qualitative_only"] is True

    def test_new_source_urls_present(self):
        block = _block()
        for url in EXPECTED_URLS:
            assert url in block, f"source URL must be cited: {url}"

    def test_verification_block(self):
        v = _mech()["verification"]
        assert v["iteration"] == 834
        assert v["type"] == "C"
        assert v["date"] == "2026-09-18 13:00 PDT"
        assert v["yaml_parse_clean"] is True
        assert v["ascii_only"] is True


class TestSupersession834:
    def test_m489_stale_block_preserved_not_rewritten(self):
        # History is preserved: the stale one-leg claim still exists in
        # mechanism 489's block; the correction lives in the new m732
        # block rather than rewriting the old record.
        text = _entities_text()
        assert "maps only Reuters - Meta on the Meta column" in text
        block = _block()
        assert "mechanism 489 meta_leg_status" in block

    def test_correction_references_stale_location(self):
        corr = _mech()["stale_claim_correction"]
        assert "mechanism 489" in corr["stale_location"]
        assert "competitor-entities.yaml" in corr["stale_location"]

    def test_extends_prior_meta_payer_mechanisms(self):
        block = _block()
        assert "mechanism 633" in block
        assert "mechanism 331" in block
        assert "mechanism 549" in block

    def test_european_bundle_legs_named(self):
        block = _block()
        assert "Le Figaro" in block
        assert "Prisa" in block
        assert "Sueddeutsche Zeitung" in block


class TestLedger834:
    def test_twenty_sixth_present_no_twenty_seventh(self):
        corpus = _repo_grep("TWENTY-SIXTH", roots=("profiles",))
        assert len(corpus) >= 1, "TWENTY-SIXTH must be present in profiles/"
        assert _repo_grep("TWENTY-SEVENTH", roots=("profiles",)) == [], (
            "TWENTY-SEVENTH must be absent in profiles/"
        )

    def test_block_states_ledger_holds_at_26(self):
        assert "holds at 26" in _block()

    def test_not_a_falsification_member(self):
        block = _block()
        assert "NOT a member of the falsification family" in block


class TestDocSync834:
    def test_readme_test_count_gate(self):
        readme = (_repo_root() / "README.md").read_text()
        assert "| Tests | 42642 |" in readme
        assert "Across 1162 test files" in readme

    def test_readme_type_c_table_row(self):
        assert TEST_BASENAME in (_repo_root() / "README.md").read_text()

    def test_architecture_test_count_gate(self):
        arch = (_repo_root() / "docs" / "ARCHITECTURE.md").read_text()
        assert "42642" in arch and "1162" in arch

    def test_architecture_tree_row(self):
        assert TEST_BASENAME in (_repo_root() / "docs" / "ARCHITECTURE.md").read_text()


class TestIterationLog834:
    def test_log_captures_iteration_834(self):
        tail = _iteration_log_tail()
        assert "#834 Type C:" in tail
        assert "13:00 PDT" in tail
        assert "m732" in tail

    def test_log_states_830_834_window(self):
        assert "830-834" in _iteration_log_tail()
