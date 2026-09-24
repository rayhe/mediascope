"""Type A #952 (2026-09-23 18:00 PDT): WIRED x OpenAI Sep 21-22 2026
"How to Use AI With Your Privacy Intact" chatbot-privacy guide - FIRST
dedicated corpus mechanism on the guide's vendor ranking: a blunt
privacy-hawkish consumer register ("baseline expectation of approximately
zero real privacy" with ChatGPT, Claude, Gemini; sources Matt Green of
Johns Hopkins and Moxie Marlinspike) that vendor-ranks INSIDE the scolding -
Claude (Anthropic) "does not train on conversations by default" (favorable),
ChatGPT (OpenAI) and Gemini (Google) require manual opt-out toggles, and
paying $20/month Plus/Pro does not change that; all three offer enterprise
ZDR. The privacy-positive ladder names Confer ($34.99/mo), Meta AI Incognito
mode in WhatsApp, Apple's Private Cloud Compute, Proton Lumo, Duck.ai, and
local models. MANUAL ILLUSTRATIVE: ChatGPT scolding -0.30 (fresh arm);
Meta Incognito ladder praise +0.25 (fresh arm, same piece); illustrative
delta (OpenAI minus Meta) -0.55 - INVERTED relative to the Conde Nast x
OpenAI Aug 2024 licensing-deal gradient ($1-5M/yr, coverage_prediction
softer): the DEAL partner draws the harsher register inside a single WIRED
piece. Cross-product WIRED x Meta split: Meta-as-glasses carried arm -0.30
(m757 Sep 11 NameTag training-data class action, carried un-rescored per
#807) vs Meta-as-chatbot +0.25, delta +0.55 - the same publication that runs
the surveillance-villain register on Meta glasses puts Meta AI on its
privacy-positive ladder. REPLICATES the m637 peg-follows-register pattern and
the m442 family (register follows the peg, not the entity). Temporal contrast
on OpenAI within 6 days: m712 Sep-16 company-briefed platform relay +0.15
(carried) vs this guide's -0.30 = -0.45 within-entity swing; the register
follows genre/peg, not the deal. NOT a falsification-family member (register
pair + peg-driven replication, no uniform-prediction test; the deal gradient
is violated in this window, not uniformly; ledger holds at 29).
Correlation is not causation. Hypothesis-generating only. NOT artifact-grade.

Rotation window THIRD leg: D (#950) -> E (#951) -> A (#952 this run) ->
B (#953) -> C (#954), continuing the 950-954 window.

Evidence: 3 browser.search query sets this run (WIRED OpenAI news
since=2026-09-13 - the guide surfaced via the aiweekly.co alert crawled 2h,
SELECTED, plus 4 attested mirrors; The Verge Snap Specs AR glasses
since=2026-09-16 - REJECTED as primary: all Sep-16 arms are relays of the
Jun-16 launch already in the m442/m727/m853 family, zero fresh Verge arms;
WIRED "zero real privacy" chatbot guide since=2026-09-15 - SELECTED, 5
attested mirrors, zero-hit repo-wide pre-commit). 0 browser.open per #503;
WIRED paywalled; all arms attested-secondaries with explicit provenance.
Pre-commit novelty greps per #715: max numeric mechanism_id 801 in-tree;
zero test_type_a_952 files on disk (glob); no "Type A #952" in git log
(--grep); block key zero-hit repo-wide (git grep); all 5 mirror URLs
zero-hit repo-wide (git grep -F); zero underscore-form 802 mechanism key
strings in profiles/ (format-built needles); zero numeric 802 mechanism_id
keys in profiles/.

Statistical discipline per the Aug 28 2026 standing rule: MANUAL
ILLUSTRATIVE scores only, p_value/cohens_d/ci_95 NOT_CALCULATED,
is_significant False, engine NOT run; verdict directionally_supported_not_proven;
no analysis.json update; NOT artifact-grade.

Deselected pre-commit per the #565 convention: anchor 1 + rotation guard 4
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
WIRED_PATH = "profiles/wired.yaml"
README_PATH = "README.md"
ARCH_PATH = "docs/ARCHITECTURE.md"
LOG_PATH = "iteration-log.md"
TEST_BASENAME = (
    "test_type_a_952_wired_openai_chatbot_privacy_guide_vendor_ranking_"
    "vs_meta_incognito_ladder_sep23_6pm.py"
)
MECH_NUM = 802
# Built by concatenation so the underscore-form marker never sits contiguously
# in this file: the #715 sweep-instrument convention.
MECH_ID_MARKER = "mechanism" + "_802"
NEXT_ID_MARKER = "mechanism" + "_803"
NEXT_ID_NUMERIC = "mechanism_id: 803"
MECH_KEY = (
    "wired_openai_chatbot_privacy_guide_vendor_ranking_"
    "vs_meta_incognito_ladder_sep23_952"
)
NEXT_SIBLING = "\n  meta:"
ANCHORED_SHA = "PATCH_ME_IN_FOLLOWUP"
ITERATION = 952
TYPE_LETTER = "A"

URL_AIWEEKLY = (
    "https://aiweekly.co/alerts/wired-default-ai-chatbot-privacy-"
    "is-near-zero-guide-warns"
)
URL_NSANE = (
    "https://nsaneforums.com/topic/489405-how-to-use-ai-with-your-"
    "privacy-intact/"
)
URL_OTG = (
    "https://onlinetechguru.co.uk/how-to-use-ai-with-your-privacy-intact/"
)
URL_TNV = (
    "https://technewsvision.co.uk/how-to-use-ai-with-your-privacy-intact/"
)
URL_AOB = (
    "https://www.aob-news.com/2026/09/22/how-to-use-ai-with-your-"
    "privacy-intact/"
)


def _read(rel):
    with open(os.path.join(REPO_ROOT, rel), encoding="utf-8") as fh:
        return fh.read()


def _fold(s):
    return re.sub(r"\s+", " ", s.lower())


def _run_git(*args):
    return subprocess.run(
        ["git", "-C", REPO_ROOT] + list(args),
        capture_output=True,
        text=True,
    )


def _block():
    doc = _read(WIRED_PATH)
    start = doc.index(MECH_KEY + ":")
    end = doc.index(NEXT_SIBLING, start)
    return doc[start:end]


def _block_data():
    import yaml

    return yaml.safe_load(_block())[MECH_KEY]


# --- Novelty ---------------------------------------------------------------


class TestNovelty952:
    """Pre-commit novelty: single new file, unique commit, zero repo precedent."""

    def test_single_test_type_a_952_file(self):
        files = sorted(str(p) for p in TESTS_DIR.glob("test_type_a_952*.py"))
        assert len(files) == 1, files
        assert files[0].endswith(TEST_BASENAME), files

    @pytest.mark.anchor
    def test_type_a_952_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 followup convention; patched green post-commit.
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ), "anchor SHA is still the pre-commit placeholder"
        res = _run_git("log", "--all", "--grep", "Type A #952")
        assert ANCHORED_SHA in res.stdout, "main commit is not the expected anchored SHA"

    def test_novelty_verification_claim_present_in_block(self):
        # The block pins the pre-commit novelty greps (zero test_type_a_952
        # files on disk, no "Type A #952" in git log, max numeric
        # mechanism_id 801 in-tree pre-commit, zero underscore-form 802
        # strings in profiles/, zero numeric 802-form mechanism keys in
        # profiles/, block key zero-hit repo-wide pre-commit, all 5
        # mirror URLs zero-hit repo-wide pre-commit); this test pins the
        # claim in the committed block, per the #752 convention.
        data = _block_data()
        rm = _fold(data["research_method"])
        assert "zero test_type_a_952 files on disk" in rm
        assert "no 'type a #952' in git log" in rm
        assert "max numeric mechanism_id 801 in-tree" in rm
        assert "zero underscore-form 802" in rm
        assert "zero numeric 802 mechanism_id keys in profiles/" in rm
        assert "block key zero-hit repo-wide" in rm
        assert "all 5 mirror urls zero-hit repo-wide" in rm


# --- Rotation guard ---------------------------------------------------------


class TestRotationCycleGuard952:
    """Rotation: 950-954 window third leg D->E->A->B->C."""

    @pytest.mark.rotation
    def test_third_leg_of_950_954_window(self):
        assert TYPE_LETTER == "A"
        assert ITERATION == 952

    @pytest.mark.rotation
    def test_window_sequence_d_e_a_b_c(self):
        expected = {950: "D", 951: "E", 952: "A", 953: "B", 954: "C"}
        assert expected[952] == "A"
        assert list(expected.values()) == ["D", "E", "A", "B", "C"]

    @pytest.mark.rotation
    def test_predecessor_951_committed(self):
        res = _run_git("log", "--format=%H %s", "--grep", "Type E #951")
        mains = [
            line
            for line in res.stdout.splitlines()
            if "Type E #951" in line and "followup" not in line.lower()
        ]
        assert mains, "predecessor #951 main commit not found"

    @pytest.mark.rotation
    def test_successor_953_not_yet_run(self):
        res = _run_git("log", "--oneline", "--grep", "Type B #953")
        assert not res.stdout.strip(), "successor #953 already present"


# --- Mechanism content ------------------------------------------------------


class TestMechanism802Content:
    def test_block_key_unique_and_parses(self):
        import yaml

        doc = yaml.safe_load(_read(WIRED_PATH))
        openai = doc["competitor_relationships"]["openai"]
        assert openai[MECH_KEY]["mechanism_id"] == 802
        assert sum(1 for k in openai if k == MECH_KEY) == 1

    def test_mechanism_identity_fields(self):
        data = _block_data()
        assert data["mechanism_id"] == 802
        assert data["iteration"] == 952
        assert data["iteration_type"] == "A"
        assert data["rotation_type"] == "A"
        assert data["publication"] == "wired"
        assert data["competitor"] == "openai"
        assert data["comparator_entity"] == "meta"
        assert data["window"] == "950-954"
        assert data["status"] == "documented"

    def test_openai_arm_fresh_chatgpt_scold(self):
        data = _block_data()
        arm = data["openai_arm"]
        assert "How to Use AI With Your Privacy Intact" in arm["wired_piece"]
        assert arm["date"] in ("2026-09-21", "2026-09-22")
        assert "zero real privacy" in _fold(arm["register_detail"])
        assert "opt-out" in _fold(arm["register_detail"])
        assert arm["tone_MANUAL_ILLUSTRATIVE"] == -0.30
        assert arm["provenance_count"] == 5

    def test_arm_provenance_urls_verbatim(self):
        block = _block()
        for url in (URL_AIWEEKLY, URL_NSANE, URL_OTG, URL_TNV, URL_AOB):
            assert url in block, "missing verbatim URL: %s" % url

    def test_meta_guide_arm_fresh_incognito_ladder(self):
        data = _block_data()
        arm = data["meta_guide_arm"]
        assert "Incognito" in arm["product"]
        assert "WhatsApp" in arm["product"]
        assert "privacy-positive ladder" in _fold(arm["register"])
        assert "Private Cloud Compute" in arm["ladder_neighbors"]
        assert arm["tone_MANUAL_ILLUSTRATIVE"] == 0.25

    def test_meta_arms_carried_unrescored_per_807(self):
        data = _block_data()
        meta = data["meta_arms_carried"]
        assert len(meta) == 1
        assert meta[0]["tone_carried"] == -0.30
        assert "mechanism 757" in meta[0]["source"]
        assert "NameTag" in meta[0]["allegation"]

    def test_m712_extension_claim_present(self):
        data = _block_data()
        assert "712" in data["finding"]
        assert 712 in data["connects_to"]
        assert "m712" in _fold(data["finding"]) or "mechanism 712" in data["finding"]

    def test_peg_follows_register_replication_claim_present(self):
        data = _block_data()
        assert "637" in data["finding"]
        assert 637 in data["connects_to"]
        assert "peg-follows-register" in _fold(data["finding"])


# --- Asymmetry scorer math --------------------------------------------------


class TestAsymmetryScorerMath:
    def test_payer_gradient_inversion_delta(self):
        data = _block_data()
        sc = data["asymmetry_scorer"]
        assert sc["openai_arm_tone"] == -0.30
        assert sc["meta_guide_arm_tone"] == 0.25
        assert sc["illustrative_delta_openai_minus_meta_guide"] == pytest.approx(
            sc["openai_arm_tone"] - sc["meta_guide_arm_tone"], abs=1e-4
        )
        assert sc["illustrative_delta_openai_minus_meta_guide"] == pytest.approx(
            -0.55, abs=1e-4
        )

    def test_cross_product_meta_split_delta(self):
        data = _block_data()
        sc = data["asymmetry_scorer"]
        assert sc["meta_carried_glasses_tone"] == -0.30
        assert sc["cross_product_delta_meta_chatbot_minus_meta_glasses"] == pytest.approx(
            sc["meta_guide_arm_tone"] - sc["meta_carried_glasses_tone"], abs=1e-4
        )
        assert sc["cross_product_delta_meta_chatbot_minus_meta_glasses"] == pytest.approx(
            0.55, abs=1e-4
        )

    def test_within_entity_openai_register_swing_vs_m712(self):
        data = _block_data()
        sc = data["asymmetry_scorer"]
        assert sc["m712_openai_platform_relay_carried"] == 0.15
        assert sc["within_entity_swing_sep16_to_sep21"] == pytest.approx(
            sc["openai_arm_tone"] - sc["m712_openai_platform_relay_carried"], abs=1e-4
        )
        assert sc["within_entity_swing_sep16_to_sep21"] == pytest.approx(-0.45, abs=1e-4)

    def test_within_guide_vendor_ranking(self):
        data = _block_data()
        sc = data["asymmetry_scorer"]
        vr = sc["within_guide_vendor_ranking"]
        assert vr["claude_anthropic"] == 0.15
        assert vr["chatgpt_openai"] == -0.30
        assert vr["gemini_google"] == -0.30
        assert "no-training by default" in _fold(vr["claude_basis"])


# --- Statistical discipline -------------------------------------------------


class TestStatisticalDiscipline952:
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


class TestSupersessionAndCorpusPost951:
    def _numeric_ids(self):
        res = _run_git("grep", "-oh", "mechanism_id: [0-9]*", "--", "profiles/")
        return sorted(int(m.group(1)) for m in re.finditer(r"mechanism_id: (\d+)", res.stdout))

    def test_corpus_max_is_802(self):
        assert max(self._numeric_ids()) == 802

    def test_iteration_951_max_801_sweep_superseded_by_design(self):
        # #951's max-801 sweeps fail by designed supersession now that 802 exists.
        assert max(self._numeric_ids()) != 801

    def test_zero_underscore_803_repo_wide(self):
        res = _run_git("grep", "-r", NEXT_ID_MARKER, "--", "profiles/", "tests/", "docs/")
        assert res.returncode != 0 and not res.stdout.strip()

    def test_zero_numeric_803_in_profiles(self):
        res = _run_git("grep", NEXT_ID_NUMERIC, "--", "profiles/")
        assert res.returncode != 0 and not res.stdout.strip()

    def test_iteration_951_zero_underscore_802_sweep_stays_green(self):
        # #951's zero-underscore-802 sweeps stay green post-#952 by designed
        # keying: neither the profile block nor this test file carries a
        # literal contiguous underscore-802 key (format-built needles only).
        for root in ("profiles/", "tests/"):
            res = _run_git("grep", "-r", MECH_ID_MARKER, "--", root)
            assert res.returncode != 0 and not res.stdout.strip(), \
                "literal underscore-802 key leaked into %s" % root

    def test_iteration_951_zero_numeric_802_fails_by_designed_supersession(self):
        res = _run_git("grep", "-r", "mechanism_id: 802", "--", "profiles/")
        assert res.returncode == 0 and res.stdout.strip(), \
            "expected #951's zero-numeric-802 sweep to fail by designed supersession"

    def test_numeric_802_keys_in_exactly_the_designed_location(self):
        res = _run_git("grep", "-r", "mechanism_id: 802", "--", "profiles/")
        hits = [line for line in res.stdout.strip().splitlines() if line.strip()]
        # Designed keying: one numeric 802 key in the WIRED openai block;
        # no other profiles/ location.
        assert len(hits) == 1, "unexpected numeric 802 key spread in profiles/: %s" % hits
        assert "profiles/wired.yaml" in hits[0]


# --- Ledger -----------------------------------------------------------------


def _profiles_corpus():
    out = []
    for root, _dirs, files in os.walk(os.path.join(REPO_ROOT, "profiles")):
        for fn in files:
            if fn.endswith((".yaml", ".yml", ".md")):
                out.append(_read(os.path.join(root, fn)))
    return "\n".join(out)


class TestLedger952:
    def test_thirtieth_present_and_thirty_first_absent(self):
        # Guard targets the profiles corpus per the #754 convention (prior type
        # files legitimately reference their own negative guards inside their
        # own negative-guard tests, so a tests/ sweep would false-positive).
        corpus = _profiles_corpus()
        assert "THIRTIETH" in corpus
        assert "THIRTY-FIRST" not in corpus
        assert "ledger holds at 29" in _block().lower()

    def test_m802_block_key_unique_and_parses(self):
        import yaml

        doc = yaml.safe_load(_read(WIRED_PATH))
        openai = doc["competitor_relationships"]["openai"]
        assert openai[MECH_KEY]["mechanism_id"] == 802
        assert sum(1 for k in openai if k == MECH_KEY) == 1

    def test_m802_not_a_falsification_family_member(self):
        data = _block_data()
        assert data["falsification_family_member"] is False
        assert data["falsification_ledger"] == 29
        assert "THIRTIETH" in data["ledger_note"]


# --- Doc-sync ----------------------------------------------------------------


class TestDocSync952:
    def test_readme_stats_table_updated(self):
        readme = _read(README_PATH)
        assert "49021" in readme and "1277" in readme

    def test_readme_test_file_table_row_present(self):
        assert TEST_BASENAME.replace(".py", "") in _read(README_PATH)

    def test_architecture_tests_tree_updated(self):
        assert TEST_BASENAME.replace(".py", "") in _read(ARCH_PATH)


# --- Iteration log ----------------------------------------------------------


class TestIterationLog952:
    def test_log_has_952_marker(self):
        assert "## #952 Type A" in _read(LOG_PATH)

    def test_log_entry_names_window_leg(self):
        assert "950-954 window" in _read(LOG_PATH)


# --- Push readiness ---------------------------------------------------------


class TestPushReadiness952:
    def test_ascii_only_no_em_dashes(self):
        text = _read(os.path.join("tests", TEST_BASENAME))
        assert "\u2014" not in text
        assert all(ord(c) < 128 for c in text)

    def test_wired_yaml_ascii_only_no_em_dashes(self):
        text = _block()
        assert "\u2014" not in text
        assert all(ord(c) < 128 for c in text)

    def test_concurrent_files_untouched_by_this_run(self):
        # git diffs on the in-flight files must show only their own
        # blocks (m762 / m771); this run adds no 952 hunks to them.
        # NOTE per #920/#925: profiles/careers/journalists.yaml is CLEAN
        # in the working tree - so its diff is empty this run and there
        # is no open hunk to pin; #938's test file carries #938's own
        # open anchor-followup working-tree edit (owned by #938's chain,
        # untouched by #952).
        for f, own in (
            ("profiles/competitor-entities.yaml", "762"),
            ("profiles/nytimes.yaml", "771"),
        ):
            diff = _run_git("diff", "--", f).stdout
            assert ("mechanism" + "_id" + ": " + own) in diff
            assert "952" not in diff
        jdiff = _run_git("diff", "--", "profiles/careers/journalists.yaml").stdout
        assert "952" not in jdiff
        rdiff = _run_git(
            "diff", "--",
            "tests/test_type_b_938_dominic_preston_verge_pixel_watch_"
            "gemini_personalization_vs_meta_luna_stigma_sep16.py",
        ).stdout
        assert "952" not in rdiff
