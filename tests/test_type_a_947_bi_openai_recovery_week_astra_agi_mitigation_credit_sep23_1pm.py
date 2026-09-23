"""Type A #947 (2026-09-23 13:00 PDT): Business Insider x OpenAI Sep 15-18 2026
"recovery week" - FIRST dedicated corpus mechanism on BI's OpenAI register in
the Sep 15-18 window: three fresh BI OpenAI arms (all zero-hit in the BI
profile pre-commit) run an aspirational/mitigation register - (1) Sep 15:
"Nvidia's Jensen Huang Says 'AGI Has Arrived' and Congratulates OpenAI"
(symby.com coverage pack), third-party-validator celebration of the Sep 3
GPT-6 Astra launch, MANUAL ILLUSTRATIVE +0.40; (2) Sep 16-17: "OpenAI
launches a new framework to track and investigate rogue AI agents" (two
wesearch.press records), mitigation-credit framing of OpenAI as the
safety-responsible actor two weeks after the Sep 4 Hugging Face agent-hack
incident, +0.30; (3) Sep 18: "OpenAI is offering robotics engineers up to
$500,000. Here's what its new job listings reveal" (wesearch.press),
talent-war/growth register, +0.25. OpenAI arm avg +0.3167 vs the carried
#857 same-window Meta arms (+0.10 Bosworth AMA executive-defense relay,
-0.30 Luna "Google Glass moment" liability framing, -0.15 creator-bans
accountability news, avg -0.1167, un-rescored per #807): illustrative delta
(OpenAI minus Meta) +0.4333. TEMPORAL INVERSION on mechanism 399 (BI Aug 30
profitability skepticism on the PAYER, -0.42): inversion delta +0.7367 in 16
days - same publication, same entity, same parent-level licensing deal.
EXTENDS mechanism 790 (Type A #932, Sep 12 slowdown-rally arm +0.15 vs Luna
-0.25, n=1/n=1): the inversion is a week-long register, not a single-story
artifact - four OpenAI arms across Sep 12-18 (m790's +0.15 carried) average
+0.275. The Axel Springer-OpenAI licensing deal (tens of millions euros,
3-year, Bloomberg Law, carried) predicts softer coverage; the prediction is
MET this week and VIOLATED at m399 (-0.42), so the tie buys no STABLE
softness - the register follows the news peg (launch/milestone vs
fundraising-skepticism), not the deal. NOT a falsification-family member
(temporal-inversion extension of m790, which is itself not a falsification
member; the softer-prediction is met in this window, so no uniform-prediction
test fails). Ledger holds at 29. Correlation is not causation.
Hypothesis-generating only. NOT artifact-grade.

Rotation window THIRD leg: D (#945) -> E (#946) -> A (#947 this run) ->
B (#948) -> C (#949), continuing the 945-949 window.

Evidence: 3 browser.search query sets this run (Business Insider OpenAI
September 2026 - SELECTED the Huang/AGI piece, the rogue-agent framework
piece x2 records, the robotics $500K piece, and the Burry slowdown-criticism
relay as counterevidence; MIT Technology Review OpenAI September 2026 -
REJECTED as primary: the Sep-14 "doomer turn" piece is a multi-lab
accountability register, not a clean publication x entity pair, and MIT TR's
tie is indirect/undisclosed). 0 browser.open per #503; BI paywalled; all arms
attested-secondaries with explicit provenance. Pre-commit novelty greps per
#715: max numeric mechanism_id 798 in-tree; zero test_type_a_947 files on
disk (glob); no "Type A #947" in git log (--grep); block key zero-hit
repo-wide (git grep); all 5 secondary URLs zero-hit repo-wide (git grep -F);
zero underscore-form 799 mechanism key strings in profiles/ (format-built
needles); zero numeric 799 mechanism_id keys in profiles/.

Statistical discipline per the Aug 28 2026 standing rule: MANUAL
ILLUSTRATIVE scores only, p_value/cohens_d/ci_95 NOT_CALCULATED,
is_significant False, engine NOT run; verdict directionally_supported_not_proven;
no analysis.json update; NOT artifact-grade.

Deselected pre-commit per the #565 convention: anchor 2 + rotation guard 4
(patched green in the anchor followup); iteration-log entry tests 2 fail by
design pre-commit, go green with the entry per #719; doc-sync 3 green
post-doc-sync.

Anchor placeholder: patched to the main commit SHA in the #565 follow-up.
"""

import os
import re
import subprocess
from pathlib import Path

import pytest

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TESTS_DIR = Path(REPO_ROOT) / "tests"
BI_PATH = "profiles/business-insider.yaml"
README_PATH = "README.md"
ARCH_PATH = "docs/ARCHITECTURE.md"
LOG_PATH = "iteration-log.md"
TEST_BASENAME = (
    "test_type_a_947_bi_openai_recovery_week_astra_agi_mitigation_credit_sep23_1pm.py"
)
MECH_NUM = 799
# Built by concatenation so the underscore-form marker never sits contiguously
# in this file: the #715 sweep-instrument convention.
MECH_ID_MARKER = "mechanism" + "_799"
NEXT_ID_MARKER = "mechanism" + "_800"
NEXT_ID_NUMERIC = "mechanism_id: 800"
MECH_KEY = (
    "business_insider_openai_recovery_week_astra_agi_mitigation_credit_"
    "vs_meta_liability_sep23_947"
)
NEXT_SIBLING = "\n  anthropic:"
ANCHORED_SHA = "PATCH_ME_IN_FOLLOWUP"
ITERATION = 947
TYPE_LETTER = "A"

URL_SYMBY = "https://symby.com/news?_cid=93349426"
URL_ROGUE_1 = (
    "https://wesearch.press/s/openai-launches-a-new-framework-to-track-and-"
    "investigate-rog-52be87c7"
)
URL_ROGUE_2 = (
    "https://wesearch.press/s/openai-launches-a-new-framework-to-track-and-"
    "investigate-rog-c76d93e1"
)
URL_ROBOTICS = (
    "https://wesearch.press/s/openai-is-offering-robotics-engineers-up-to-"
    "500000-heres-wha-1a0f1ed7"
)
URL_BURRY = (
    "https://gateiolink.net/news/detail/michael-burry-criticizes-openai-"
    "anthropic-ceos-calls-to-slow-ai-development-24266354"
)


def _read(rel):
    with open(os.path.join(REPO_ROOT, rel), encoding="utf-8") as fh:
        return fh.read()


def _block():
    doc = _read(BI_PATH)
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


class TestNovelty947:
    """Pre-commit novelty: single new file, unique commit, zero repo precedent."""

    @pytest.mark.anchor
    def test_single_test_type_a_947_file(self):
        files = sorted(str(p) for p in TESTS_DIR.glob("test_type_a_947*.py"))
        assert len(files) == 1, files
        assert files[0].endswith(TEST_BASENAME), files

    @pytest.mark.anchor
    def test_type_a_947_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 followup convention; patched green post-commit.
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ), "anchor SHA is still the pre-commit placeholder"
        res = _run_git("log", "--all", "--grep", "Type A #947")
        assert ANCHORED_SHA in res.stdout, "main commit is not the expected anchored SHA"

    def test_novelty_verification_claim_present_in_block(self):
        # The block pins the pre-commit novelty greps (zero test_type_a_947
        # files on disk, no "Type A #947" in git log, max numeric
        # mechanism_id 798 in-tree pre-commit, zero underscore-form 799
        # strings in profiles/, zero numeric 799-form mechanism keys in
        # profiles/, block key zero-hit repo-wide pre-commit, all 5
        # secondary URLs zero-hit repo-wide pre-commit); this test pins the
        # claim in the committed block, per the #752 convention.
        data = _block_data()
        rm = _fold(data["research_method"])
        assert "zero test_type_a_947 files on disk" in rm
        assert "no 'type a #947' in git log" in rm
        assert "max numeric mechanism_id 798 in-tree" in rm
        assert "zero underscore-form 799" in rm
        assert "zero numeric 799 mechanism_id keys in profiles/" in rm
        assert "block key zero-hit repo-wide" in rm
        assert "all 5 secondary urls zero-hit repo-wide" in rm


# --- Rotation guard ---------------------------------------------------------


class TestRotationCycleGuard947:
    """Rotation: 945-949 window third leg D->E->A->B->C."""

    @pytest.mark.rotation
    def test_third_leg_of_945_949_window(self):
        assert TYPE_LETTER == "A"
        assert ITERATION == 947

    @pytest.mark.rotation
    def test_window_sequence_d_e_a_b_c(self):
        expected = {945: "D", 946: "E", 947: "A", 948: "B", 949: "C"}
        assert expected[947] == "A"
        assert list(expected.values()) == ["D", "E", "A", "B", "C"]

    @pytest.mark.rotation
    def test_predecessor_946_committed(self):
        res = _run_git("log", "--format=%H %s", "--grep", "Type E #946")
        mains = [
            line
            for line in res.stdout.splitlines()
            if "Type E #946" in line and "followup" not in line.lower()
        ]
        assert mains, "predecessor #946 main commit not found"

    @pytest.mark.rotation
    def test_successor_948_not_yet_run(self):
        res = _run_git("log", "--oneline", "--grep", "Type B #948")
        assert not res.stdout.strip(), "successor #948 already present"


# --- Mechanism content ------------------------------------------------------


class TestMechanism799Content:
    def test_block_key_unique_and_parses(self):
        import yaml

        doc = yaml.safe_load(_read(BI_PATH))
        openai = doc["competitor_relationships"]["openai"]
        assert openai[MECH_KEY]["mechanism_id"] == 799
        assert sum(1 for k in openai if k == MECH_KEY) == 1

    def test_mechanism_identity_fields(self):
        data = _block_data()
        assert data["mechanism_id"] == 799
        assert data["iteration"] == 947
        assert data["iteration_type"] == "A"
        assert data["rotation_type"] == "A"
        assert data["publication"] == "business-insider"
        assert data["competitor"] == "openai"
        assert data["comparator_entity"] == "meta"
        assert data["window"] == "945-949"
        assert data["status"] == "documented"

    def test_three_openai_arms_fresh_and_dated(self):
        data = _block_data()
        arms = data["openai_arms"]
        assert len(arms) == 3
        assert arms[0]["date"] == "2026-09-15"
        assert "AGI Has Arrived" in arms[0]["piece"]
        assert arms[0]["tone_MANUAL_ILLUSTRATIVE"] == 0.40
        assert arms[1]["date"] == "2026-09-16"
        assert "rogue AI agents" in arms[1]["piece"]
        assert arms[1]["tone_MANUAL_ILLUSTRATIVE"] == 0.30
        assert arms[2]["date"] == "2026-09-18"
        assert "robotics engineers" in arms[2]["piece"]
        assert arms[2]["tone_MANUAL_ILLUSTRATIVE"] == 0.25
        for arm in arms:
            assert "provenance" in arm and "http" in arm["provenance"]

    def test_arm_provenance_urls_verbatim(self):
        block = _block()
        for url in (URL_SYMBY, URL_ROGUE_1, URL_ROGUE_2, URL_ROBOTICS, URL_BURRY):
            assert url in block, "missing verbatim URL: %s" % url

    def test_meta_arms_carried_unrescored_per_807(self):
        data = _block_data()
        meta = data["meta_arms_carried"]
        assert len(meta) == 3
        assert [m["tone_carried"] for m in meta] == [0.10, -0.30, -0.15]
        assert all("mechanism 745" in m["source"] for m in meta)

    def test_burry_counterevidence_present(self):
        data = _block_data()
        ce = data["counterevidence"]
        assert any("Burry" in c for c in ce)
        assert any("m399" in c for c in ce)

    def test_m790_extension_claim_present(self):
        data = _block_data()
        assert "790" in data["finding"]
        assert 790 in data["connects_to"]
        assert "m790" in _fold(data["finding"]) or "mechanism 790" in data["finding"]

    def test_temporal_inversion_claim_present(self):
        data = _block_data()
        assert "399" in data["finding"]
        assert 399 in data["connects_to"]
        assert data["asymmetry_scorer"]["temporal_inversion_vs_m399"] == 0.7367


# --- Asymmetry scorer math --------------------------------------------------


class TestAsymmetryScorerMath:
    def test_openai_avg(self):
        data = _block_data()
        tones = data["asymmetry_scorer"]["openai_arm_tones"]
        assert tones == [0.40, 0.30, 0.25]
        assert data["asymmetry_scorer"]["openai_arm_avg"] == pytest.approx(
            sum(tones) / 3, abs=1e-4
        )
        assert data["asymmetry_scorer"]["openai_arm_avg"] == pytest.approx(0.3167, abs=1e-4)

    def test_meta_avg_carried(self):
        data = _block_data()
        tones = data["asymmetry_scorer"]["meta_arm_tones"]
        assert tones == [0.10, -0.30, -0.15]
        assert data["asymmetry_scorer"]["meta_arm_avg"] == pytest.approx(
            sum(tones) / 3, abs=1e-4
        )
        assert data["asymmetry_scorer"]["meta_arm_avg"] == pytest.approx(-0.1167, abs=1e-4)

    def test_illustrative_delta(self):
        data = _block_data()
        sc = data["asymmetry_scorer"]
        assert sc["illustrative_delta_openai_minus_meta"] == pytest.approx(
            sc["openai_arm_avg"] - sc["meta_arm_avg"], abs=1e-4
        )
        assert sc["illustrative_delta_openai_minus_meta"] == pytest.approx(0.4333, abs=1e-4)

    def test_inversion_delta_vs_m399(self):
        data = _block_data()
        sc = data["asymmetry_scorer"]
        assert sc["temporal_inversion_vs_m399"] == pytest.approx(
            sc["openai_arm_avg"] - (-0.42), abs=1e-4
        )

    def test_extended_window_avg_with_m790(self):
        data = _block_data()
        sc = data["asymmetry_scorer"]
        assert sc["extended_window_avg_with_m790"] == pytest.approx(
            (0.15 + 0.40 + 0.30 + 0.25) / 4, abs=1e-4
        )
        assert sc["extended_window_avg_with_m790"] == pytest.approx(0.275, abs=1e-4)


# --- Statistical discipline -------------------------------------------------


class TestStatisticalDiscipline947:
    def test_manual_illustrative_only(self):
        sc = _block_data()["asymmetry_scorer"]
        assert sc["p_value"] == "NOT_CALCULATED"
        assert sc["cohens_d"] == "NOT_CALCULATED"
        assert sc["ci_95"] == "NOT_CALCULATED"
        assert sc["is_significant"] is False
        assert "MANUAL ILLUSTRATIVE" in sc["tone_basis"]

    def test_engine_not_run_no_significance(self):
        data = _block_data()
        assert "engine NOT run" in data["finding"]
        sc = data["asymmetry_scorer"]
        assert sc["is_significant"] is False
        assert sc["statistical_contract"] == "degenerate_small_n_per_arm"

    def test_not_artifact_grade_correlation_not_causation(self):
        data = _block_data()
        assert "NOT artifact-grade" in data["finding"]
        assert "Correlation is not causation" in data["finding"]
        assert "Hypothesis-generating only" in data["finding"]

    def test_verdict_directionally_supported_not_proven(self):
        data = _block_data()
        assert "not proven" in _fold(data["asymmetry_scorer"]["verdict"])


# --- Supersession -----------------------------------------------------------


class TestSupersessionAndCorpusPost946:
    def _numeric_ids(self):
        res = _run_git("grep", "-oh", "mechanism_id: [0-9]*", "--", "profiles/")
        return sorted(int(m.group(1)) for m in re.finditer(r"mechanism_id: (\d+)", res.stdout))

    def test_corpus_max_is_799(self):
        assert max(self._numeric_ids()) == 799

    def test_iteration_946_max_798_sweep_superseded_by_design(self):
        # #946's max-798 sweeps fail by designed supersession now that 799 exists.
        assert max(self._numeric_ids()) != 798

    def test_zero_underscore_800_repo_wide(self):
        res = _run_git("grep", "-r", NEXT_ID_MARKER, "--", "profiles/", "tests/", "docs/")
        assert res.returncode != 0 and not res.stdout.strip()

    def test_zero_numeric_800_in_profiles(self):
        res = _run_git("grep", NEXT_ID_NUMERIC, "--", "profiles/")
        assert res.returncode != 0 and not res.stdout.strip()

    def test_iteration_946_zero_underscore_799_sweep_stays_green(self):
        # #946's zero-underscore-799 sweeps stay green post-#947 by designed
        # keying: neither the profile block nor this test file carries a
        # literal contiguous underscore-799 key (format-built needles only).
        for root in ("profiles/", "tests/"):
            res = _run_git("grep", "-r", MECH_ID_MARKER, "--", root)
            assert res.returncode != 0 and not res.stdout.strip(), \
                "literal underscore-799 key leaked into %s" % root

    def test_iteration_946_zero_numeric_799_fails_by_designed_supersession(self):
        res = _run_git("grep", "-r", "mechanism_id: 799", "--", "profiles/")
        assert res.returncode == 0 and res.stdout.strip(), \
            "expected #946's zero-numeric-799 sweep to fail by designed supersession"

    def test_numeric_799_keys_in_exactly_the_designed_location(self):
        res = _run_git("grep", "-r", "mechanism_id: 799", "--", "profiles/")
        hits = [line for line in res.stdout.strip().splitlines() if line.strip()]
        # Designed keying: one numeric 799 key in the BI openai block;
        # no other profiles/ location.
        assert len(hits) == 1, "unexpected numeric 799 key spread in profiles/: %s" % hits
        assert "profiles/business-insider.yaml" in hits[0]


# --- Ledger -----------------------------------------------------------------


def _profiles_corpus():
    out = []
    for root, _dirs, files in os.walk(os.path.join(REPO_ROOT, "profiles")):
        for fn in files:
            if fn.endswith((".yaml", ".yml", ".md")):
                out.append(_read(os.path.join(root, fn)))
    return "\n".join(out)


class TestLedger947:
    def test_thirtieth_present_and_thirty_first_absent(self):
        # Guard targets the profiles corpus per the #754 convention (prior type
        # files legitimately reference their own negative guards inside their
        # own negative-guard tests, so a tests/ sweep would false-positive).
        corpus = _profiles_corpus()
        assert "THIRTIETH" in corpus
        assert "THIRTY-FIRST" not in corpus
        assert "ledger holds at 29" in _block().lower()

    def test_m799_block_key_unique_and_parses(self):
        import yaml

        doc = yaml.safe_load(_read(BI_PATH))
        openai = doc["competitor_relationships"]["openai"]
        assert openai[MECH_KEY]["mechanism_id"] == 799
        assert sum(1 for k in openai if k == MECH_KEY) == 1

    def test_m799_not_a_falsification_family_member(self):
        data = _block_data()
        assert data["falsification_family_member"] is False
        assert data["falsification_ledger"] == 29
        assert "THIRTIETH" in data["ledger_note"]


# --- Doc-sync ----------------------------------------------------------------


class TestDocSync947:
    def test_readme_stats_table_updated(self):
        readme = _read(README_PATH)
        assert "48748" in readme and "1272" in readme

    def test_readme_test_file_table_row_present(self):
        assert TEST_BASENAME.replace(".py", "") in _read(README_PATH)

    def test_architecture_tests_tree_updated(self):
        assert TEST_BASENAME.replace(".py", "") in _read(ARCH_PATH)


# --- Iteration log ----------------------------------------------------------


class TestIterationLog947:
    def test_log_has_947_marker(self):
        assert "## #947 Type A" in _read(LOG_PATH)

    def test_log_entry_names_window_leg(self):
        assert "945-949 window" in _read(LOG_PATH)


# --- Push readiness ---------------------------------------------------------


class TestPushReadiness947:
    def test_ascii_only_no_em_dashes(self):
        text = _read(os.path.join("tests", TEST_BASENAME))
        assert "\u2014" not in text
        assert all(ord(c) < 128 for c in text)

    def test_bi_yaml_ascii_only_no_em_dashes(self):
        text = _block()
        assert "\u2014" not in text
        assert all(ord(c) < 128 for c in text)

    def test_concurrent_files_untouched_by_this_run(self):
        # git diffs on the in-flight files must show only their own
        # blocks (m762 / m771); this run adds no 947 hunks to them.
        # NOTE per #920/#925: profiles/careers/journalists.yaml is CLEAN
        # in the working tree (#898/m770 hunk lost at #918, confirmed
        # absent at the corpus layer) - so its diff is empty this run
        # and there is no 770 hunk to pin.
        for f, own in (
            ("profiles/competitor-entities.yaml", "762"),
            ("profiles/nytimes.yaml", "771"),
        ):
            diff = _run_git("diff", "--", f).stdout
            assert ("mechanism" + "_id" + ": " + own) in diff
            assert "947" not in diff
        jdiff = _run_git("diff", "--", "profiles/careers/journalists.yaml").stdout
        assert "947" not in jdiff
        rdiff = _run_git(
            "diff", "--",
            "tests/test_type_b_938_dominic_preston_verge_pixel_watch_"
            "gemini_personalization_vs_meta_luna_stigma_sep16.py",
        ).stdout
        assert "947" not in rdiff
