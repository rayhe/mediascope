#!/usr/bin/env python3
"""Type A #797: The Times x OpenAI slowdown-week statesman register vs
Anthropic motive-questioning vs Meta glasses adversarial (mechanism 709) -
competitor coverage deep dive.

Mechanism 709 under profiles/competitor-coverage-research.yaml -> publications.

FIRST dedicated Times x OpenAI slowdown-week mechanism. Arm 1 (Sep 16 2026):
The Times "Mathematicians fear AI curbs may come too late to save humanity" -
Altman given the sober-statesman platform ("people were justifiably concerned
about the risks from his technology, while adding that the company was working
to make AI safe"; "I think the world is right to be afraid of this"); the
piece's attack vector lands on ANTHROPIC via Microsoft AI chief Mustafa
Suleyman ("disastrous impact on the wellbeing of humanity"). MANUAL
ILLUSTRATIVE +0.25. Arm 2 (Sep 11 2026): The Times "Brains are needed to
manage AI risk" - motive-questioning register on Anthropic ("bizarre
pre-flotation strategy"; "the furore is proving to be useful PR for Anthropic,
which wants AI regulation amid the pressing threat of cheaper Chinese
rivals"). MANUAL ILLUSTRATIVE -0.20. Illustrative OpenAI-minus-Anthropic delta
+0.45 on the SAME slowdown-week peg. Meta comparator (same publication,
in-corpus URL): The Times "Fear and loathing on the streets of London with
Meta smart glasses" (~Sep 7 2026) - adversarial privacy register ("pervert
glasses"; "Ban them, stamp on the b*******"; "freaky", "sneaky"), tone -0.55;
illustrative OpenAI-minus-Meta delta +0.80. Financial tie: News Corp x OpenAI
$250M/5yr content licensing deal (May 22 2024; $50M/yr; training +
answer-surfacing; treated ACTIVE per #599, m627). STATED CAVEAT: News Corp is a
DUAL-payer owner (Meta news licensing up to $50M/yr, Mar 2026, m519), so the
corpus's own symmetric-softening prediction FAILS on the Meta leg - the Times
gives Meta glasses the hardest register (-0.55) of the three arms despite
Meta's payer status. Anthropic is on News Corp's adversarial ledger ($1.5B
Bartz settlement revenue share). Verdict mixed_not_proven: the
OpenAI-vs-Anthropic leg is directionally consistent with the payer-vs-sued
gradient, but the Meta leg contradicts dual-payer symmetry, so no uniform
incentive claim is supported. NOT a falsification-family member; ledger holds
at 26; no analysis.json update; engine NOT run; p_value/cohens_d/ci_95
NOT_CALCULATED; correlation is not causation. Research: 9 browser.search query
sets, search-excerpt-bounded per #503, 0 browser.open attempts. The ft.com and
wired.com site queries surfaced no usable verbatim URLs (bounded absence per
iteration-492); pivoted to The Times where verbatim thetimes.com URLs surfaced
for all three arms. All anchor URLs verbatim from search Full-URL listings; no
canonical URLs constructed.
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
MECH_KEY = "times_openai_slowdown_week_statesman_register_sep17"
M_ID = 709
# Built by concatenation per the #723/#738/#739 designed-keying convention: the
# literal ("mechanism" + "_709") never appears in tests/ or profiles/, keeping
# the #794 zero-709 sweep instruments green pre-commit. (Used only via this
# constant.)
MECH_ID_MARKER = "mechanism" + "_709"
NEXT_ID_MARKER = "mechanism" + "_710"
NEXT_ID_NUMERIC = "mechanism_id: 710"

# Patched post-commit in the anchor followup per the #565 sequence.
ANCHORED_SHA = "06673822a6e46c38eb943c8cff9d98991727bcb7"


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
    end = text.index(
        "\n  fortune_ai_weekly_multi_episode_cross_entity_vocabulary_gradient:", start
    )
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


class TestNovelty797:
    def test_single_test_type_a_797_file(self):
        files = sorted(p.name for p in TESTS_DIR.glob("test_type_a_797_*.py"))
        assert files == [TEST_BASENAME], files

    def test_type_a_797_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 followup convention; patched
        # green post-commit. Novelty was verified pre-commit by shell
        # greps (zero test_type_a_797 files, no #797 in git log); this test
        # pins that no duplicate #797 main commit ever appears.
        #
        # Hardened per the #760 rotation-guard note (applied in #776): the
        # naive "Type A #797:" prefix also matches the followup subjects
        # ("Type A #797 (followup):", "Type A #797 (doc-sync):") and a
        # push-blocked status commit. The ": times" qualifier pins only
        # the main commit.
        mains = _git_log_mains("Type A #797: times")
        assert len(mains) == 1, mains
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ), mains
        assert mains[0].startswith(ANCHORED_SHA + " "), mains

    def test_novelty_verification_claim_present_in_block(self):
        block = _block()
        assert "Zero test_type_a_797 files on disk pre-commit (glob)" in block
        assert '"Type A #797" in git log pre-commit' in block
        assert "max numeric mechanism_id 708 pre-commit" in block
        assert "zero underscore-form" in block
        assert "709 mechanism key substrings repo-wide pre-commit." in block
        assert "zero times_openai_slowdown_week mechanism keys" in block


class TestRotationCycleGuard797:
    """795-799 window third leg D->E->A. Green only after the main commit.

    Deselected pre-commit per the #565 followup convention (the #797 main
    commit does not exist yet); patched green in the anchor followup.
    """

    EXPECTED_ORDER = [("A", "797"), ("E", "796"), ("D", "795"), ("C", "794"), ("B", "793")]
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

    def test_window_795_799_third_leg_a(self):
        assert self._window() == self.EXPECTED_ORDER

    def test_rotation_adjacency_cycle_valid(self):
        window = self._window()
        for (t1, n1), (t2, n2) in zip(window, window[1:]):
            assert int(n1) == int(n2) + 1
            assert (self.ORDER[t1] - self.ORDER[t2]) % 5 == 1, (t1, t2)

    def test_anchor_sha_matches_head(self):
        mains = _git_log_mains("Type A #797: times")
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ), mains
        assert mains and mains[0].startswith(ANCHORED_SHA + " "), mains


class TestMechanism709Content:
    def test_block_present_under_publications(self):
        text = _read_profile()
        assert MECH_KEY in text
        assert text.index("publications:") < text.index(MECH_KEY)

    def test_block_metadata(self):
        block = _block()
        assert "mechanism_id: 709" in block
        assert "iteration: 797" in block
        assert "iteration_type: A" in block
        assert "publication: The Times (News Corp / News UK)" in block
        assert "entity: OpenAI" in block
        assert "time_pdt: '00:00'" in block
        assert "author: 'Kit (with Ray)'" in block

    def test_two_arms_registers_tones(self):
        block = _block()
        assert "arm1_times_openai_mathematicians_emergency:" in block
        assert "arm2_times_anthropic_ai_risk_float:" in block
        assert "register: statesman_platform" in block
        assert "register: motive_questioning_skeptical" in block
        assert "tone_MANUAL_ILLUSTRATIVE: 0.25" in block
        assert "tone_MANUAL_ILLUSTRATIVE: -0.20" in block

    def test_arm1_openai_excerpts_verbatim(self):
        block = _block()
        # YAML source line-breaks split these; assert raw-text-safe fragments.
        assert "justifiably" in block
        assert "working to make AI safe" in block
        assert "world is right to be afraid" in block
        assert "disastrous" in block
        assert "impact on the wellbeing of humanity" in block
        assert "attack" in block and "lands on Anthropic" in block

    def test_arm2_anthropic_excerpts_verbatim(self):
        block = _block()
        assert "bizarre pre-flotation strategy" in block
        assert "useful PR for Anthropic" in block
        assert "cheaper Chinese rivals" in block

    def test_anchor_urls_verbatim_from_search(self):
        block = _block()
        assert "https://www.thetimes.com/uk/technology-uk/article/mathematician-emergency-ai-sam-altman-royal-society-chpmkvfs0" in block
        assert "https://www.thetimes.com/business/economics/article/ai-risk-anthropic-float-rtfrdh52j" in block
        assert "https://www.thetimes.com/uk/science/article/openai-maths-millennium-navier-stokes-problem-bgmkm7rff" in block
        assert "https://www.thetimes.com/business/companies-markets/article/softbank-shares-ai-elon-musk-crvttsb0h" in block
        assert block.count("url_status: verbatim_from_search_full_url_listing") == 2

    def test_meta_comparator_and_deltas(self):
        block = _block()
        assert "meta_comparator:" in block
        assert "in_corpus_url_already_documented" in block
        assert "meta_glasses_tone_MANUAL_ILLUSTRATIVE: -0.55" in block
        assert "pervert glasses" in block
        assert "illustrative_openai_minus_anthropic_delta: 0.45" in block
        assert "illustrative_register_delta_openai_minus_meta: 0.80" in block
        assert "SAME slowdown-week news peg" in block

    def test_manual_scores_bounded(self):
        block = _block()
        assert "openai_arm_scores: [0.25]" in block
        assert "anthropic_arm_scores: [-0.20]" in block

    def test_financial_tie_with_dual_payer_caveat(self):
        block = _block()
        assert "financial_tie:" in block
        assert "$250M over 5 years" in block
        assert "dual-payer owner" in block
        assert "up to $50M per year" in block
        assert "Bartz" in block
        # The corpus's own symmetric-softening prediction is stated as FAILED.
        assert "FAILS on the Meta" in block
        assert "does not transmit uniformly" in block

    def test_verdict_mixed_not_proven(self):
        block = _block()
        assert "mixed_not_proven" in block
        assert "no uniform" in block and "incentive claim is supported" in block

    def test_confounders_ranked_strong_first(self):
        block = _block()
        assert "confounders_ranked:" in block
        assert "Dual-payer owner neutralizes" in block
        assert "Beat and genre asymmetry" in block
        strong_idx = block.index("strong:")
        moderate_idx = block.index("moderate:")
        assert strong_idx < moderate_idx

    def test_counter_evidence_present(self):
        block = _block()
        assert "counter_evidence:" in block
        assert "plagiarism" in block
        assert "SoftBank" in block
        assert "symmetric business register" in block

    def test_statistical_discipline_string(self):
        block = _block()
        assert "MANUAL ILLUSTRATIVE scores only." in block
        assert "DEGENERATE n=1 check" in block
        # Engine output on the n=1 arms: inferential stats degenerate, no
        # significance claimed. Raw text is YAML line-broken; assert
        # raw-text-safe fragments.
        assert "t 0.0 / p 1.0 / Cohen d 0.0" in block
        assert "is_significant false" in block
        assert "no significance claimed (Aug 28" in block
        assert "2026 standing rule)." in block
        assert "no_analysis_json_update: true" in block

    def test_designed_keying_no_underscore_form_in_block(self):
        # The block key carries no underscore-form 709 substring by designed
        # keying, keeping the #794 zero-709 sweep instruments green.
        assert MECH_ID_MARKER not in _block()

    def test_research_method_discloses_no_browser_open(self):
        block = _block()
        assert "0 browser.open attempts." in block
        assert "search-excerpt-bounded per #503" in block
        assert "9 browser.search" in block
        assert "ft.com" in block
        assert "wired.com" in block
        assert "bounded search-result absence per the iteration-492" in block

    def test_cross_references_present(self):
        block = _block()
        assert "mechanism_id: 519" in block
        assert "mechanism_id: 627" in block
        assert "mechanism_id: 703" in block
        assert "mechanism_id: 706" in block


class TestSupersessionAndCorpusPost796:
    """Post-#796 corpus integrity: max 709, zero 710, designed supersession."""

    def test_max_numeric_mechanism_id_is_709(self):
        assert _max_numeric_mechanism_id() == M_ID

    def test_708_still_present(self):
        hits = _repo_grep("mechanism_id: 708")
        assert len(hits) >= 1, hits

    def test_zero_underscore_710_keys_repo_wide(self):
        hits = _repo_grep(NEXT_ID_MARKER)
        assert hits == [], hits

    def test_zero_numeric_710_keys_in_profiles(self):
        hits = _repo_grep(NEXT_ID_NUMERIC, roots=("profiles",))
        assert hits == [], hits

    def test_d794_zero_underscore_709_profiles_sweep_stays_green(self):
        # #794 asserted zero underscore-form 709 literals in profiles/; the
        # m709 block key carries no such substring by designed keying, so
        # that sweep stays green. (#795's Type D and #796's Type E sweeps,
        # same assertion, also stay green; Type D/E add no mechanisms.)
        hits = _repo_grep(MECH_ID_MARKER, roots=("profiles",))
        assert hits == [], hits

    def test_d794_zero_underscore_709_tests_sweep_stays_green(self):
        # #794 asserted zero underscore-form 709 references in tests/; this
        # file builds the marker by concatenation ("mechanism" + "_709") so
        # no contiguous literal exists in tests/ either - the sweep stays
        # green. Own file excluded as sweep carrier per the #715
        # pattern-rescope lesson.
        hits = _repo_grep(MECH_ID_MARKER, roots=("tests",))
        own = str((TESTS_DIR / Path(__file__).name).relative_to(REPO))
        hits = [h for h in hits if h != own]
        assert hits == [], hits

    def test_d794_zero_numeric_709_profiles_sweep_fails_by_designed_supersession(self):
        # #794 asserted zero "mechanism_id: 709" hits in profiles/; the m709
        # block supersedes it by design per the #710/#720 convention. (#795's
        # Type D and #796's Type E sweeps, same assertion, are superseded the
        # same way.)
        hits = _repo_grep("mechanism_id: 709", roots=("profiles",))
        assert len(hits) >= 1, hits

    def test_d794_max_708_sweep_superseded_by_design(self):
        # #794 (and #795/#796) asserted max == 708; advancing to 709
        # supersedes it per the #710/#720 convention. Documented, not
        # repaired.
        assert _max_numeric_mechanism_id() == 709 != 708

    def test_m709_block_key_unique_in_publications(self):
        text = _read_profile()
        assert text.count(MECH_KEY + ":") == 1

    def test_competitor_coverage_research_yaml_still_parses(self):
        import yaml

        d = yaml.safe_load(_read_profile())
        assert d["publications"][MECH_KEY]["mechanism_id"] == M_ID


class TestLedger797:
    """Falsification ledger: TWENTY-SIXTH present, TWENTY-SEVENTH absent; m709 not a member."""

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
        assert "holds at 26." in _block()

    def test_m709_not_a_falsification_family_member(self):
        block = _block()
        assert "NOT a member - register documentation with" in block
        assert "no uniform-prediction test run." in block

    def test_no_analysis_json_update_claimed(self):
        block = _block()
        assert "no_analysis_json_update: true" in block


README_PATH = REPO / "README.md"
ARCH_PATH = REPO / "docs" / "ARCHITECTURE.md"
LOG_PATH = REPO / "iteration-log.md"


def _read(p):
    return p.read_text(encoding="utf-8")


class TestDocSync797:
    def test_readme_row_797(self):
        assert TEST_BASENAME in _read(README_PATH)

    def test_readme_row_797_in_table(self):
        doc = _read(README_PATH)
        assert TEST_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))

    def test_architecture_row_797(self):
        assert TEST_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_797_file(self):
        doc = _read(ARCH_PATH)
        assert TEST_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))


class TestIterationLog797:
    def _tail(self):
        lines = _read(LOG_PATH).splitlines()
        # Entries are appended chronologically (post-#735 convention); the
        # #797 entry sits at the end of the file, not the top.
        return "\n".join(lines[-80:])

    def test_log_entry_present(self):
        # "#797 Type A:" is the entry header; a bare "#797" would
        # false-positive on #796's rotation line ("A (#797) -> ...").
        assert "#797 Type A:" in self._tail()

    def test_log_cycle_and_hour(self):
        assert "795-799" in self._tail()
        assert "00:00 PDT" in self._tail()
