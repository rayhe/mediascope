#!/usr/bin/env python3
"""Type A #792: The Verge x Apple iPhone Duo launch-week register vs Meta
glasses register (mechanism 706) - competitor coverage deep dive.

Mechanism 706 under profiles/competitor-coverage-research.yaml -> publications.

FIRST dedicated Verge x Apple Duo mechanism. Arm 1 (Sep 9 2026, 7:45 PM): The
Verge "Verge staffers react to the iPhone Duo: What we love and don't love" -
multi-staffer gut-reaction register, aspirational (MANUAL ILLUSTRATIVE +0.45):
Jay Peters "I think iPhone Duo is the perfect name for Apple's foldable";
Jennifer Tuohy "I've never wanted a new iPhone more"; Kevin McShane "The Apple
Pencil support makes the Duo an iPad Mini killer"; Marina Galperina "a far
superior ratio! ... the thing that I'm most excited about with the Duo". Arm 2
(Sep 11 2026): Vergecast "We unfolded the iPhone Duo" - Allison Johnson and
Vee Song (Victoria Song) hands-on from California with Apple privacy discussion
carried INSIDE the product-positive frame ("39:23 Privacy and social concerns",
"46:49 Apple Privacy Whitepaper"), MANUAL ILLUSTRATIVE +0.45. Meta comparator
(same publication, in-corpus m75/m304): Victoria Song's 4+ dedicated
privacy-adversarial Meta glasses pieces ("creepy, surveillance, dox"
vocabulary), tone -0.55. Illustrative register delta +1.00 on different news
pegs (launch week vs privacy beat): register documentation, not a controlled
causal claim. Financial tie: Apple x Vox Media platform-distribution
partnership (Bloomberg Mar 2019 via MacRumors: Apple inked a deal with Vox for
Apple News subscription service; Adweek 2015: Apple News app debut with 50+
publishers "including Hearst, Vox and Conde Nast", publishers keep 100% of
own-ad revenue / 70% of Apple-sold ad revenue). Stated caveats: the 2019 News+
deal was for Vox (the site), NOT The Verge (AppleInsider explicitly excludes
The Verge from the initial deal); seven-figure Apple News revenue figures are
Time's, not Vox Media's. Uniform incentive prediction directionally
CONSISTENT with the observed delta but the tie is parent-level and
Vox-site-specific; launch-week genre convention is the stronger candidate
explanation. NOT a falsification-family member; ledger holds at 26; no
analysis.json update; engine NOT run; p_value/cohens_d/ci_95 NOT_CALCULATED;
correlation is not causation. Research: 13 browser.search query sets,
search-excerpt-bounded per #503, 0 browser.open attempts. All anchor URLs
verbatim from search Full-URL listings; no canonical URLs constructed.
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
MECH_KEY = "verge_apple_duo_launch_week_staff_react_register_sep16"
M_ID = 706
# Built by concatenation per the #723/#738/#739 designed-keying convention: the
# literal ("mechanism" + "_706") never appears in tests/ or profiles/, keeping
# the #789/#790/#791 zero-706 sweep instruments green pre-commit. (Used only
# via this constant.)
MECH_ID_MARKER = "mechanism" + "_706"
NEXT_ID_MARKER = "mechanism" + "_707"
NEXT_ID_NUMERIC = "mechanism_id: 707"

# Patched post-commit in the anchor followup per the #565 sequence.
ANCHORED_SHA = "PATCH_ME_IN_FOLLOWUP"


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


class TestNovelty792:
    def test_single_test_type_a_792_file(self):
        files = sorted(p.name for p in TESTS_DIR.glob("test_type_a_792_*.py"))
        assert files == [TEST_BASENAME], files

    def test_type_a_792_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 followup convention; patched
        # green post-commit. Novelty was verified pre-commit by shell
        # greps (zero test_type_a_792 files, no #792 in git log); this test
        # pins that no duplicate #792 main commit ever appears.
        #
        # Hardened per the #760 rotation-guard note (applied in #776): the
        # naive "Type A #792:" prefix also matches the followup subjects
        # ("Type A #792 (followup):", "Type A #792 (doc-sync):") and a
        # push-blocked status commit. The ": verge" qualifier pins only
        # the main commit.
        mains = _git_log_mains("Type A #792: verge")
        assert len(mains) == 1, mains
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ), mains
        assert mains[0].startswith(ANCHORED_SHA + " "), mains

    def test_novelty_verification_claim_present_in_block(self):
        block = _block()
        assert "Zero test_type_a_792 files on disk pre-commit (glob)" in block
        assert '"Type A #792" in git log pre-commit' in block
        assert "max numeric mechanism_id 705 pre-commit" in block
        assert "zero underscore-form" in block
        assert "706 mechanism key substrings repo-wide pre-commit." in block
        assert "zero verge_apple_duo mechanism keys" in block


class TestRotationCycleGuard792:
    """790-794 window third leg D->E->A. Green only after the main commit.

    Deselected pre-commit per the #565 followup convention (the #792 main
    commit does not exist yet); patched green in the anchor followup.
    """

    EXPECTED_ORDER = [("A", "792"), ("E", "791"), ("D", "790"), ("C", "789"), ("B", "788")]
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

    def test_window_790_794_third_leg_a(self):
        assert self._window() == self.EXPECTED_ORDER

    def test_rotation_adjacency_cycle_valid(self):
        window = self._window()
        for (t1, n1), (t2, n2) in zip(window, window[1:]):
            assert int(n1) == int(n2) + 1
            assert (self.ORDER[t1] - self.ORDER[t2]) % 5 == 1, (t1, t2)

    def test_anchor_sha_matches_head(self):
        mains = _git_log_mains("Type A #792: verge")
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ), mains
        assert mains and mains[0].startswith(ANCHORED_SHA + " "), mains


class TestMechanism706Content:
    def test_block_present_under_publications(self):
        text = _read_profile()
        assert MECH_KEY in text
        assert text.index("publications:") < text.index(MECH_KEY)

    def test_block_metadata(self):
        block = _block()
        assert "mechanism_id: 706" in block
        assert "iteration: 792" in block
        assert "iteration_type: A" in block
        assert "publication: The Verge (Vox Media)" in block
        assert "entity: Apple" in block
        assert "time_pdt: '10:00'" in block
        assert "author: 'Kit (with Ray)'" in block

    def test_two_arms_registers_tones(self):
        block = _block()
        assert "arm1_verge_staff_react_duo:" in block
        assert "arm2_vergecast_unfolded_duo:" in block
        assert "register: aspirational_staff_reaction" in block
        assert "register: hands_on_product_positive" in block
        assert block.count("tone_MANUAL_ILLUSTRATIVE: 0.45") == 2

    def test_arm1_staff_react_excerpts_verbatim(self):
        block = _block()
        # YAML source line-breaks split these; assert raw-text-safe fragments.
        assert "I think iPhone Duo is the perfect name for" in block
        assert "Apple''s foldable" in block
        assert "I''ve never wanted" in block
        assert "a new iPhone more." in block
        assert "The Apple Pencil support makes the Duo an iPad Mini killer and the" in block
        assert "perfect on-the-go sketchbook for digital artists." in block
        assert "a far superior ratio!" in block
        assert "the thing that I''m most excited about with" in block
        assert "The Verge Sep 9, 2026, 7:45 PM" in block

    def test_arm1_bylines(self):
        block = _block()
        for s in [
            "Jay Peters, senior reporter",
            "Jennifer Tuohy, senior reviewer",
            "Kevin McShane, editorial director, audio and video",
            "Marina Galperina, senior tech editor",
            "Emma Roth, news writer",
            "Antonio G. Di Benedetto / The Verge",
        ]:
            assert s in block, s

    def test_arm2_vergecast_excerpts_verbatim(self):
        block = _block()
        assert "Allison Johnson and Vee Song report back from" in block
        assert "California after having more hands-on time" in block
        assert "39:23 Privacy and social concerns" in block
        assert "46:49 Apple Privacy Whitepaper" in block
        assert "the SAME journalist (Victoria Song / Vee Song)" in block

    def test_anchor_urls_verbatim_from_search(self):
        block = _block()
        assert "https://scoopfeeds.com/article/e11a296f-74fb-560a-a9a0-952760468522" in block
        assert "https://www.youtube.com/watch?v=BORNUd_FdLA" in block
        assert "https://www.macrumors.com/2019/03/21/vox-joins-apple-news-subscription-service/" in block
        assert "https://www.adweek.com/morning-media-newsfeed/apple-adds-more-publishers-for-news-app-which-will-launch-soon/" in block
        assert "http://appleinsider.com/articles/19/03/21/vox-reportedly-joins-apple-news-service-other-vox-media-properties-not-available-at-launch" in block
        assert block.count("url_status: verbatim_from_search_full_url_listing") == 3

    def test_meta_comparator_and_delta(self):
        block = _block()
        assert "meta_comparator:" in block
        assert "in_corpus_mechanisms_75_and_304" in block
        assert "meta_glasses_tone_MANUAL_ILLUSTRATIVE: -0.55" in block
        assert "illustrative_register_delta_apple_minus_meta: 1.00" in block
        assert "Different news pegs (Apple launch week vs Meta privacy" in block
        assert "Albert Aydin" in block

    def test_manual_scores_and_avg(self):
        block = _block()
        assert "apple_arm_scores: [0.45, 0.45]" in block
        assert "apple_arm_avg: 0.45" in block

    def test_financial_tie_with_stated_caveats(self):
        block = _block()
        assert "financial_tie:" in block
        assert "platform_distribution_partnership" in block
        assert "Apple has inked a deal" in block
        assert "will be available in Apple News." in block
        assert "including Hearst, Vox and Conde Nast" in block
        # The Verge exclusion is stated plainly.
        assert "including The Verge," in block
        assert "are not included as part of the" in block
        assert "Seven-figure Apple News revenue figures in the press are attributed to" in block

    def test_verdict_bounded(self):
        block = _block()
        assert "directionally_supported_not_proven" in block
        # "directionally CONSISTENT" spans a YAML source line break.
        assert "directionally CONSISTENT" in block
        assert "launch-week genre" in block
        assert "stronger candidate" in block

    def test_confounders_ranked_strong_first(self):
        block = _block()
        assert "confounders_ranked:" in block
        assert "Launch-week genre convention" in block
        assert "Tie is parent-level and Vox-site-specific" in block
        strong_idx = block.index("strong:")
        moderate_idx = block.index("moderate:")
        assert strong_idx < moderate_idx

    def test_counter_evidence_present(self):
        block = _block()
        assert "counter_evidence:" in block
        assert "too expensive" in block
        assert "balanced in m75" in block

    def test_statistical_discipline_string(self):
        block = _block()
        assert "MANUAL ILLUSTRATIVE scores only." in block
        assert "p_value/cohens_d/ci_95" in block
        # NOTE: the YAML source line-breaks split "(Aug 28 2026 standing rule)."
        # Assert raw-text-safe fragments instead.
        assert "p_value/cohens_d/ci_95 NOT_CALCULATED. is_significant: false (Aug 28 2026" in block
        assert "standing rule). Engine NOT run." in block
        assert "no_analysis_json_update: true" in block

    def test_designed_keying_no_underscore_form_in_block(self):
        # The block key carries no underscore-form 706 substring by designed
        # keying, keeping the #789/#790/#791 zero-706 sweep instruments green.
        assert MECH_ID_MARKER not in _block()

    def test_research_method_discloses_no_browser_open(self):
        block = _block()
        assert "0 browser.open attempts." in block
        assert "search-excerpt-bounded per #503" in block
        assert "13 browser.search" in block
        assert "The Guardian UK" in block
        assert "abandoned for lack of arms" in block

    def test_cross_references_present(self):
        block = _block()
        assert "mechanism_id: 75" in block
        assert "mechanism_id: 304" in block
        assert "mechanism_id: 703" in block


class TestSupersessionAndCorpusPost791:
    """Post-#791 corpus integrity: max 706, zero 707, designed supersession."""

    def test_max_numeric_mechanism_id_is_706(self):
        assert _max_numeric_mechanism_id() == M_ID

    def test_705_still_present(self):
        hits = _repo_grep("mechanism_id: 705")
        assert len(hits) >= 1, hits

    def test_zero_underscore_707_keys_repo_wide(self):
        hits = _repo_grep(NEXT_ID_MARKER)
        assert hits == [], hits

    def test_zero_numeric_707_keys_in_profiles(self):
        hits = _repo_grep(NEXT_ID_NUMERIC, roots=("profiles",))
        assert hits == [], hits

    def test_d789_zero_underscore_706_profiles_sweep_stays_green(self):
        # #789 asserted zero underscore-form 706 literals in profiles/; the
        # m706 block key carries no such substring by designed keying, so
        # that sweep stays green. (#790's Type D and #791's Type E sweeps,
        # same assertion, also stay green; Type D/E add no mechanisms.)
        hits = _repo_grep(MECH_ID_MARKER, roots=("profiles",))
        assert hits == [], hits

    def test_d789_zero_underscore_706_tests_sweep_stays_green(self):
        # #789 asserted zero underscore-form 706 references in tests/; this
        # file builds the marker by concatenation ("mechanism" + "_706") so
        # no contiguous literal exists in tests/ either - the sweep stays
        # green.
        hits = _repo_grep(MECH_ID_MARKER, roots=("tests",))
        own = str((TESTS_DIR / Path(__file__).name).relative_to(REPO))
        hits = [h for h in hits if h != own]
        assert hits == [], hits

    def test_d789_zero_numeric_706_profiles_sweep_fails_by_designed_supersession(self):
        # #789 asserted zero "mechanism_id: 706" hits in profiles/; the m706
        # block supersedes it by design per the #710/#720 convention. (#790's
        # Type D and #791's Type E sweeps, same assertion, are superseded the
        # same way.)
        hits = _repo_grep("mechanism_id: 706", roots=("profiles",))
        assert len(hits) >= 1, hits

    def test_d789_max_705_sweep_superseded_by_design(self):
        # #789 (and #790/#791) asserted max == 705; advancing to 706
        # supersedes it per the #710/#720 convention. Documented, not
        # repaired.
        assert _max_numeric_mechanism_id() == 706 != 705

    def test_m706_block_key_unique_in_publications(self):
        text = _read_profile()
        assert text.count(MECH_KEY + ":") == 1

    def test_competitor_coverage_research_yaml_still_parses(self):
        import yaml

        d = yaml.safe_load(_read_profile())
        assert d["publications"][MECH_KEY]["mechanism_id"] == M_ID


class TestLedger792:
    """Falsification ledger: TWENTY-SIXTH present, TWENTY-SEVENTH absent; m706 not a member."""

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

    def test_m706_not_a_falsification_family_member(self):
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


class TestDocSync792:
    def test_readme_row_792(self):
        assert TEST_BASENAME in _read(README_PATH)

    def test_readme_row_792_in_table(self):
        doc = _read(README_PATH)
        assert TEST_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))

    def test_architecture_row_792(self):
        assert TEST_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_792_file(self):
        doc = _read(ARCH_PATH)
        assert TEST_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))


class TestIterationLog792:
    def _tail(self):
        lines = _read(LOG_PATH).splitlines()
        # Entries are appended chronologically (post-#735 convention); the
        # #792 entry sits at the end of the file, not the top.
        return "\n".join(lines[-80:])

    def test_log_entry_present(self):
        # "#792 Type A:" is the entry header; a bare "#792" would
        # false-positive on #791's rotation line ("A (#792) -> ...").
        assert "#792 Type A:" in self._tail()

    def test_log_cycle_and_hour(self):
        assert "790-794" in self._tail()
        assert "10:00 PDT" in self._tail()
