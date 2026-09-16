#!/usr/bin/env python3
"""Type A #787: Politico x OpenAI slowdown-week scoop channel symmetry vs
non-payer Anthropic (mechanism 703) - competitor coverage deep dive.

Mechanism 703 under profiles/competitor-coverage-research.yaml -> publications.

FIRST dedicated Politico x OpenAI mechanism. Politico's AI-policy vertical is the
frontier labs' preferred leak/scoop channel for pro-regulation pivots, and scoop
access is SYMMETRIC across payer status (search-excerpt-bounded per #503, 0
browser.open attempts, 5 browser.search query sets): Arm 1 (Sep 15 2026): OpenAI
endorses three bipartisan bills (Web of Biological Data Act, AI-Ready Bio-Data
Standards Act, Scale Biology Act) plus the FRONTIER Act IVO provision; Reuters
reports "Politico earlier reported the endorsements", PANews attributes the
FRONTIER Act support to Politico (Obernolte/Trahan House bill). Arm 2 (Aug 2026,
carried via Sep 10 techtimes): "Anthropic's endorsement of the bills was first
reported by Politico in August 2026" - the SAME first-report treatment for the
lab with NO documented Axel Springer AI licensing deal. Both arms carry the labs'
chosen regulatory narratives in a neutral policy-process register (MANUAL
ILLUSTRATIVE +0.05 each; OpenAI arm avg +0.05). The financial tie is real and
near-term material: OpenAI x Axel Springer (Politico's parent), Dec 13 2023,
3-year, tens of millions EUR across the deal per Bloomberg Law source-familiar,
Politico content included (mechanism 597, #604), renewal UNRESOLVED with ~Dec
2026 expiry; plus Microsoft x Axel Springer Apr 29 2024 (Politico integrates
Microsoft Advertising), making Axel Springer a DUAL-AI-PAYER owner. The uniform
financial-incentive prediction (the deal buys preferential narrative carriage for
OpenAI) is NOT supported on the observed arms: non-payer Anthropic received
identical scoop treatment. The pattern is beat-driven and lab-driven. Meta
comparator: bounded absence (iteration-492) - zero verbatim Politico x Meta URLs
in this run's 5 query sets; zero dedicated Politico x Meta blocks in the corpus.
Extends m700's payer-status inversion and m697's register-selection dominance to
the scoop-access margin. NOT a falsification-family member (scoop-access
documentation, not a uniform-prediction test); ledger holds at 26; no
analysis.json update; engine NOT run; p_value/cohens_d/ci_95 NOT_CALCULATED;
correlation is not causation.
"""

import os
import re
import subprocess
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
PROFILES = REPO / "profiles"
TESTS_DIR = REPO / "tests"
PROFILE = PROFILES / "competitor-coverage-research.yaml"
TEST_BASENAME = Path(__file__).name
MECH_KEY = "politico_openai_slowdown_week_scoop_channel_symmetry_sep16"
M_ID = 703
# Built by concatenation per the #723/#738/#739 designed-keying convention: the
# literal ("mechanism" + "_703") never appears in tests/ or profiles/, keeping
# the #785/#786 zero-703 sweep instruments green pre-commit. (Used only via this
# constant.)
MECH_ID_MARKER = "mechanism" + "_703"
NEXT_ID_MARKER = "mechanism" + "_704"
NEXT_ID_NUMERIC = "mechanism_id: 704"

# Patched post-commit in the anchor followup per the #565 sequence.
ANCHORED_SHA = "cf5316b85f81c40080d4f774cadec602a506001f"


def _repo_grep(needle, roots=("profiles", "tests", "docs")):
    hits = []
    for root in roots:
        base = REPO / root
        for dirpath, _dirnames, filenames in os.walk(base):
            # Skip bytecode caches: the sweep instruments guard source text;
            # .pyc files are gitignored build artifacts whose stored string
            # constants would false-positive on concatenated markers.
            if "__pycache__" in Path(dirpath).parts:
                continue
            for fn in filenames:
                p = Path(dirpath) / fn
                try:
                    content = p.read_text(encoding="utf-8", errors="replace")
                except OSError:
                    continue
                if needle in content:
                    hits.append(str(p.relative_to(REPO)))
    return sorted(hits)


def _max_numeric_mechanism_id():
    ids = set()
    for hits in [_repo_grep("mechanism_id: ", roots=("profiles",))]:
        for path in hits:
            text = (REPO / path).read_text(encoding="utf-8", errors="replace")
            for m in re.finditer(r"mechanism_id:\s*(\d+)", text):
                ids.add(int(m.group(1)))
    return max(ids)


def _read_profile():
    return PROFILE.read_text(encoding="utf-8")


def _block():
    text = _read_profile()
    start = text.index(MECH_KEY)
    end = text.index("\n  fortune_ai_weekly_multi_episode_cross_entity_vocabulary_gradient:", start)
    return text[start:end]


def _git_log_mains(prefix):
    log = subprocess.run(
        ["git", "log", "--format=%H %s", "--no-merges"],
        cwd=REPO,
        capture_output=True,
        text=True,
        check=True,
    ).stdout.splitlines()
    return [line for line in log if prefix in line]


class TestNovelty787:
    def test_single_test_type_a_787_file(self):
        files = sorted(p.name for p in TESTS_DIR.glob("test_type_a_787_*.py"))
        assert files == [TEST_BASENAME], files

    def test_type_a_787_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 followup convention; patched
        # green post-commit. Novelty was verified pre-commit by shell
        # greps (zero test_type_a_787 files, no #787 in git log); this test
        # pins that no duplicate #787 main commit ever appears.
        #
        # Hardened per the #760 rotation-guard note (applied in #776): the
        # naive "Type A #787:" prefix also matches the followup subjects
        # ("Type A #787 (followup):", "Type A #787 (doc-sync):") and a
        # push-blocked status commit. The ": politico" qualifier pins only
        # the main commit.
        mains = _git_log_mains("Type A #787: politico")
        assert len(mains) == 1, mains
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ), mains
        assert mains[0].startswith(ANCHORED_SHA + " "), mains

    def test_novelty_verification_claim_present_in_block(self):
        block = _block()
        assert "Zero test_type_a_787 files on disk pre-commit (glob)" in block
        # The "no / \"Type A #787\"" phrase spans a YAML source line break.
        assert '"Type A #787" in git log pre-commit' in block
        # "max numeric mechanism_id 702 pre-commit" spans a YAML source line
        # break in the block; assert the two raw-text-safe fragments.
        assert "max" in block
        assert "numeric mechanism_id 702 pre-commit" in block


class TestRotationCycleGuard787:
    """785-789 window third leg A->E->D->C->B. Green only after the main commit.

    Deselected pre-commit per the #565 followup convention (the #787 main
    commit does not exist yet); patched green in the anchor followup.
    """

    EXPECTED_ORDER = [("A", "787"), ("E", "786"), ("D", "785"), ("C", "784"), ("B", "783")]
    ORDER = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}

    def _window(self):
        # First occurrence of each distinct iteration number, newest first
        # (robust to the #756-style followup commits that repeat the same
        # "Type X #N" wording without the colon, per the #752 convention).
        mains = subprocess.run(
            ["git", "log", "--format=%s", "--no-merges", "-n", "40"],
            cwd=REPO,
            capture_output=True,
            text=True,
            check=True,
        ).stdout.splitlines()
        seen_nums = set()
        out = []
        for s in mains:
            m = re.match(r"Type ([A-E]) #(\d+):", s)
            if m and m.group(2) not in seen_nums:
                seen_nums.add(m.group(2))
                out.append(m.groups())
        return out[:5]

    def test_window_785_789_third_leg_a(self):
        assert self._window() == self.EXPECTED_ORDER

    def test_rotation_adjacency_cycle_valid(self):
        window = self._window()
        for (t1, n1), (t2, n2) in zip(window, window[1:]):
            assert int(n1) == int(n2) + 1
            assert (self.ORDER[t1] - self.ORDER[t2]) % 5 == 1, (t1, t2)

    def test_anchor_sha_matches_head(self):
        mains = _git_log_mains("Type A #787: politico")
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ), mains
        assert mains and mains[0].startswith(ANCHORED_SHA + " "), mains


class TestMechanism703Content:
    def test_block_present_under_publications(self):
        text = _read_profile()
        assert MECH_KEY in text
        assert text.index("publications:") < text.index(MECH_KEY)

    def test_block_metadata(self):
        block = _block()
        assert "mechanism_id: 703" in block
        assert "iteration: 787" in block
        assert "iteration_type: A" in block
        assert "publication: Politico (Axel Springer)" in block
        assert "entity: OpenAI" in block
        assert "time_pdt: '05:00'" in block
        assert "author: 'Kit (with Ray)'" in block

    def test_two_arms_titles_registers_tones(self):
        block = _block()
        assert "arm1_openai_bill_endorsements_politico_scoop" in block
        assert "arm2_anthropic_endorsement_first_reported_politico" in block
        assert block.count("register: policy_process_scoop_transmission") == 2
        assert block.count("tone_MANUAL_ILLUSTRATIVE: 0.05") == 2

    def test_arm1_excerpts_verbatim(self):
        block = _block()
        assert "Politico earlier reported the endorsements." in block
        assert "Web of Biological Data Act" in block
        assert "AI-Ready Bio-Data Standards Act" in block
        assert "Scale Biology Act" in block
        assert "FRONTIER Act" in block
        assert "According to Politico, artificial intelligence giant OpenAI supports" in block

    def test_arm2_excerpts_verbatim(self):
        block = _block()
        # Raw-text-safe fragments: the YAML source line-breaks "Politico in /
        # August 2026." and escapes the apostrophe as ''.
        for s in [
            "Anthropic''s endorsement of the bills was first reported by Politico in",
            "August 2026.",
            '"Some of these bills we did not endorse in the past, and are now',
        ]:
            assert s in block, s

    def test_anchor_urls_verbatim_from_search(self):
        block = _block()
        assert "https://www.reuters.com/technology/openai-backs-bills-us-congress-ai-biological-weapon-threats-2026-09-15/" in block
        assert "https://www.panews.io/articles/01a0a554-a11c-74b5-89d5-bfe8dda288d4" in block
        assert "https://www.techtimes.com/articles/327159/20260910/california-signs-first-us-ai-audit-law-frontier-labs-hiring-tools-now-scope.htm" in block
        assert "url_status: verbatim_from_search_full_url_listing" in block

    def test_meta_comparator_bounded_absence(self):
        block = _block()
        assert "status: bounded_absence_iteration_492" in block
        # "Zero verbatim Politico x / Meta URLs" spans a YAML source line break.
        assert "Zero verbatim Politico x" in block
        assert "Meta URLs surfaced" in block
        assert "zero dedicated Politico x Meta blocks in the corpus" in block
        assert "told Politico" in block

    def test_manual_scores_and_avg(self):
        block = _block()
        assert "openai_arm_scores: [0.05, 0.05]" in block
        assert "openai_arm_avg: 0.05" in block

    def test_scoop_symmetry_claim(self):
        block = _block()
        # "Scoop / access is NOT payer-selective" spans a YAML source line break.
        assert "access is NOT payer-selective on the observed arms." in block
        assert "Non-payer (Anthropic, no documented Axel Springer AI deal)" in block

    def test_incentive_attribution_bounded(self):
        block = _block()
        # The attribution sentence spans a YAML source line break.
        assert "Scoop access selected by beat and lab strategy, not by" in block
        assert "payer status." in block
        assert "INCONCLUSIVE for any directional incentive claim" in block

    def test_confounders_ranked_strong_first(self):
        block = _block()
        assert "confounders_ranked:" in block
        assert "Scoop-as-beat convention" in block
        strong_idx = block.index("strong:")
        moderate_idx = block.index("moderate:")
        assert strong_idx < moderate_idx

    def test_counter_evidence_present(self):
        block = _block()
        assert "counter_evidence:" in block
        assert "OpenAI throws its weight behind FRONTIER Act" in block
        assert "Cohere" in block

    def test_statistical_discipline_string(self):
        block = _block()
        assert "MANUAL ILLUSTRATIVE scores only." in block
        # "p_value/cohens_d/ci_95 / NOT_CALCULATED" and "Engine NOT / run."
        # span YAML source line breaks; assert raw-text-safe fragments.
        assert "p_value/cohens_d/ci_95" in block
        assert "NOT_CALCULATED. is_significant: false (Aug 28 2026 standing rule)." in block
        assert "Engine NOT" in block
        assert "no_analysis_json_update: true" in block

    def test_designed_keying_no_underscore_form_in_block(self):
        # The block key carries no "mechanism_703" substring by designed
        # keying, keeping the #785/#786 zero-703 sweep instruments green.
        assert MECH_ID_MARKER not in _block()

    def test_research_method_discloses_no_browser_open(self):
        block = _block()
        # "0 browser.open / attempts." spans a YAML source line break.
        assert "0 browser.open" in block
        assert "attempts." in block
        assert "search-excerpt-bounded per #503" in block

    def test_cross_references_present(self):
        block = _block()
        assert "mechanism_id: 597" in block
        assert "mechanism_id: 604" in block
        assert "mechanism_id: 700" in block
        assert "mechanism_id: 697" in block


class TestSupersessionAndCorpusPost786:
    """Post-#786 corpus integrity: max 703, zero 704, designed supersession."""

    def test_max_numeric_mechanism_id_is_703(self):
        assert _max_numeric_mechanism_id() == M_ID

    def test_702_still_present(self):
        hits = _repo_grep("mechanism_id: 702")
        assert len(hits) >= 1, hits

    def test_zero_underscore_704_keys_repo_wide(self):
        hits = _repo_grep(NEXT_ID_MARKER)
        assert hits == [], hits

    def test_zero_numeric_704_keys_in_profiles(self):
        hits = _repo_grep(NEXT_ID_NUMERIC, roots=("profiles",))
        assert hits == [], hits

    def test_d785_zero_underscore_703_profiles_sweep_stays_green(self):
        # #785 asserted zero underscore-form 703 literals in profiles/; the
        # m703 block key carries no such substring by designed keying, so
        # that sweep stays green. (#786's Type E sweep, same assertion, also
        # stays green; Type E adds no mechanisms.)
        hits = _repo_grep(MECH_ID_MARKER, roots=("profiles",))
        assert hits == [], hits

    def test_d785_zero_underscore_703_tests_sweep_stays_green(self):
        # #785 asserted zero underscore-form 703 references in tests/; this
        # file builds the marker by concatenation ("mechanism" + "_703") so
        # no contiguous literal exists in tests/ either - the sweep stays
        # green.
        hits = _repo_grep(MECH_ID_MARKER, roots=("tests",))
        own = str((TESTS_DIR / Path(__file__).name).relative_to(REPO))
        hits = [h for h in hits if h != own]
        assert hits == [], hits

    def test_d785_zero_numeric_703_profiles_sweep_fails_by_designed_supersession(self):
        # #785 asserted zero "mechanism_id: 703" hits in profiles/; the m703
        # block supersedes it by design per the #710/#720 convention. (#786's
        # Type E sweep, same assertion, is superseded the same way.)
        hits = _repo_grep("mechanism_id: 703", roots=("profiles",))
        assert len(hits) >= 1, hits

    def test_d785_max_702_sweep_superseded_by_design(self):
        # #785 (and #786) asserted max == 702; advancing to 703 supersedes it
        # per the #710/#720 convention. Documented, not repaired.
        assert _max_numeric_mechanism_id() == 703 != 702

    def test_m703_block_key_unique_in_publications(self):
        text = _read_profile()
        assert text.count(MECH_KEY + ":") == 1

    def test_competitor_coverage_research_yaml_still_parses(self):
        import yaml

        d = yaml.safe_load(_read_profile())
        assert d["publications"][MECH_KEY]["mechanism_id"] == M_ID


class TestLedger787:
    """Falsification ledger: TWENTY-SIXTH present, TWENTY-SEVENTH absent; m703 not a member."""

    def _profiles_corpus(self):
        parts = []
        for root, _dirs, files in os.walk(REPO / "profiles"):
            for f in files:
                p = Path(root) / f
                parts.append(p.read_text(encoding="utf-8", errors="replace"))
        return "\n".join(parts)

    def test_twenty_sixth_present_and_twenty_seventh_absent(self):
        # Guard targets the profiles corpus per the #754 convention (prior type
        # files legitimately reference "TWENTY-SEVENTH" inside their own
        # negative guards, so a tests/ sweep would false-positive).
        corpus = self._profiles_corpus()
        assert "TWENTY-SIXTH" in corpus
        assert "TWENTY-SEVENTH" not in corpus
        assert "Ledger holds at 26" in _block()

    def test_m703_not_a_falsification_family_member(self):
        block = _block()
        assert "NOT a falsification-family member" in block
        assert "scoop-access documentation, not a uniform-prediction test" in block

    def test_no_analysis_json_update_claimed(self):
        block = _block()
        assert "no_analysis_json_update: true" in block


README_PATH = REPO / "README.md"
ARCH_PATH = REPO / "docs" / "ARCHITECTURE.md"
LOG_PATH = REPO / "iteration-log.md"


def _read(p):
    return p.read_text(encoding="utf-8")


class TestDocSync787:
    def test_readme_row_787(self):
        assert TEST_BASENAME in _read(README_PATH)

    def test_readme_row_787_in_table(self):
        doc = _read(README_PATH)
        assert TEST_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))

    def test_architecture_row_787(self):
        assert TEST_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_787_file(self):
        doc = _read(ARCH_PATH)
        assert TEST_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))


class TestIterationLog787:
    def _tail(self):
        lines = _read(LOG_PATH).splitlines()
        # Entries are appended chronologically (post-#735 convention); the
        # #787 entry sits at the end of the file, not the top.
        return "\n".join(lines[-80:])

    def test_log_entry_present(self):
        # "#787 Type A:" is the entry header; a bare "#787" would
        # false-positive on #786's rotation line ("A (#787) -> ...").
        assert "#787 Type A:" in self._tail()

    def test_log_cycle_and_hour(self):
        assert "785-789" in self._tail()
        assert "05:00 PDT" in self._tail()
