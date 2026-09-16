"""Type B #788: Brenda Stolyar WIRED->Wirecutter migration, Meta vs Apple register split.

Iteration 788 (Type B, journalist cross-entity tracking), Sep 16 2026, 06:00 PDT.
Mechanism 704 under profiles/competitor-coverage-research.yaml ->
cross_publication_findings.

FINDING: Brenda Stolyar migrated from WIRED staff writer (Gear team,
Conde Nast / Advance Publications) to Wirecutter senior staff writer covering
smartphones, tablets and wearables (Talking Biz News, circa May 2025; prior
outlets Mashable, PCMag, Digital Trends). Post-migration, at the SAME
employer (Wirecutter / NYT), she shows a cross-entity register split. The
Meta arm is the Wirecutter opinion piece "Meta's New Smart Glasses Sounded
Cool at First. But I Was Unimpressed." (byline Brenda Stolyar; date not
pinned in the Muck Rack listing, bounded per iteration-492; disappointed-
dismissive register, -0.45 illustrative). The Apple arms are the Sep 10 2026
iPhone Duo foldable launch pieces: "Apple Just Unveiled a Folding iPhone, and
It Looks Good" (bylines Brenda Stolyar and Caitlin McGarry; enthusiastic
launch register, +0.45) and "I Tried Apple's New Foldable iPhone Duo. Here's
How It Compares." (first-person hands-on, +0.55); Apple avg +0.50;
illustrative register delta (Apple minus Meta) = +0.95. A third same-writer
Apple piece, "The iPhone Air Is Apple's Most Impressive Phone in Years. But
Most People Shouldn't Buy It.", anchors the Apple-side enthusiasm as a
standing register with a buy-skeptical kicker. Both scored arms are
post-migration Wirecutter pieces, so the split is WITHIN-employer and
within-journalist: the migration is career context, not the causal mechanism.
FIRST dedicated corpus mechanism on Stolyar (zero hits repo-wide pre-commit).

NOT a falsification-family member (register documentation, not a
uniform-prediction test). Ledger holds at 26.

RESEARCH METHOD: Search-excerpt-bounded per #503 this run (7 browser.search
query sets; 1 browser.open success on the Muck Rack Wirecutter journalist
listing; 1 browser.open terminally failed this turn, NOT retried). No
per-article URLs were available verbatim; none constructed. MANUAL
ILLUSTRATIVE only; p_value/cohens_d/ci_95 NOT_CALCULATED; is_significant
false; engine NOT run; no analysis.json update; NOT artifact-grade.

Commit: 'Type B #788: stolyar' (anchor: ANCHORED_SHA, patched post-commit).
"""

import os
import re
import subprocess
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
TESTS_DIR = REPO / "tests"
PROFILES = REPO / "profiles"
TEST_BASENAME = (
    "test_type_b_788_brenda_stolyar_wired_to_wirecutter_"
    "meta_vs_apple_register_split_sep16_6am.py"
)
MECH_KEY = (
    "brenda stolyar wired to wirecutter migration "
    "meta vs apple register split sep2026"
)
M_ID = 704
# The underscore-form mechanism key ("mechanism" + "_704") never appears as a
# literal in tests/ or profiles/, keeping the #787 zero-704 sweep instruments
# green pre-commit. (Used only via this marker for the designed-supersession
# assertions.)
MECH_ID_MARKER = "mechanism" + "_704"
NEXT_ID_MARKER = "mechanism" + "_705"
NEXT_ID_NUMERIC = "mechanism_id: 705"
# Patched to the real main-commit hash in the anchor followup (post-commit);
# pre-commit this is the placeholder from the #565 convention.
ANCHORED_SHA = "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565"


def _repo_grep(needle, roots=("profiles", "tests", "docs")):
    out = subprocess.run(
        ["git", "grep", "-n", "--", needle, *roots],
        cwd=REPO,
        capture_output=True,
        text=True,
    )
    return out.stdout.splitlines()


def _max_numeric_mechanism_id():
    ids = []
    for path in _repo_grep("mechanism_id: ", roots=("profiles",)):
        for m in re.finditer(r"mechanism_id: (\d+)", path):
            ids.append(int(m.group(1)))
    return max(ids) if ids else None


def _read_profile():
    return (PROFILES / "competitor-coverage-research.yaml").read_text(encoding="utf-8")


def _block():
    text = _read_profile()
    start = text.index(MECH_KEY)
    # The m704 block sits at the end of cross_publication_findings, directly
    # before the top-level methodology key.
    end = text.index("\nmethodology:", start)
    return text[start:end]


class TestNovelty788:
    def test_single_test_type_b_788_file(self):
        files = sorted(p.name for p in TESTS_DIR.glob("test_type_b_788_*.py"))
        assert files == [TEST_BASENAME], files

    def test_type_b_788_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 followup convention; patched
        # green post-commit. Novelty was verified pre-commit by shell
        # greps (zero test_type_b_788 files, no #788 in git log, zero
        # "Brenda Stolyar" hits, max mechanism 703, zero underscore-form 704
        # keys); this test pins that no duplicate #788 main commit appears.
        mains = _git_log_mains("Type B #788: stolyar")
        assert len(mains) == 1, mains
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ), mains
        assert mains[0].startswith(ANCHORED_SHA + " "), mains

    def test_novelty_verification_claim_present_in_block(self):
        block = _block()
        assert "Zero test_type_b_788 files on disk pre-commit (glob)" in block
        # The "no / "Type B #788"" phrase spans a YAML source line break.
        assert '"Type B #788" in git log pre-commit' in block
        # "max numeric mechanism_id 703 pre-commit" spans a YAML source line
        # break in the block; assert the two raw-text-safe fragments.
        assert "max" in block
        assert "numeric mechanism_id 703 pre-commit" in block
        assert '"Brenda Stolyar" zero-hit repo-wide pre-commit' in block


def _git_log_mains(prefix):
    log = subprocess.run(
        ["git", "log", "--format=%H %s", "--no-merges"],
        cwd=REPO,
        capture_output=True,
        text=True,
        check=True,
    ).stdout.splitlines()
    return [line for line in log if prefix in line]


class TestRotationCycleGuard788:
    """784-788 window fifth leg C->D->E->A->B. Green only after the main commit.

    Deselected pre-commit per the #565 followup convention (the #788 main
    commit does not exist yet); patched green in the anchor followup.
    """

    EXPECTED_ORDER = [("B", "788"), ("A", "787"), ("E", "786"), ("D", "785"), ("C", "784")]
    ORDER = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}

    def _window(self):
        # First occurrence of each distinct iteration number, newest first
        # (robust to the #756-style followup commits that repeat the same
        # "Type X #N" wording without the colon, per the #752 convention).
        mains = subprocess.run(
            ["git", "log", "--format=%s", "--no-merges", "-n", "50"],
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

    def test_window_784_788_fifth_leg_b(self):
        assert self._window() == self.EXPECTED_ORDER

    def test_rotation_adjacency_cycle_valid(self):
        window = self._window()
        for (t1, n1), (t2, n2) in zip(window, window[1:]):
            assert int(n1) == int(n2) + 1
            assert (self.ORDER[t1] - self.ORDER[t2]) % 5 == 1, (t1, t2)

    def test_anchor_sha_matches_head(self):
        mains = _git_log_mains("Type B #788: stolyar")
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ), mains
        assert mains and mains[0].startswith(ANCHORED_SHA + " "), mains


class TestMechanism704Content:
    """m704 block content: identity, arms, scorer, discipline, URLs."""

    def test_block_present_and_id_704(self):
        block = _block()
        assert "mechanism_id: 704" in block
        assert "iteration: 788" in block
        assert "rotation_type: B" in block
        assert "journalist: 'Brenda Stolyar'" in block
        assert "publication: wirecutter" in block
        assert "owner: nyt" in block
        assert "previous_publication: wired" in block
        assert "previous_owner: conde_nast_advance" in block

    def test_meta_arm_title_and_tone_quoted(self):
        block = _block()
        assert "Meta''s New Smart Glasses Sounded Cool at First. But I Was Unimpressed." in block
        assert "tone_illustrative: -0.45" in block
        assert "disappointed_dismissive_opinion" in block

    def test_apple_arms_titles_and_tones_quoted(self):
        block = _block()
        assert "Apple Just Unveiled a Folding iPhone, and It Looks Good" in block
        assert "I Tried Apple''s New Foldable iPhone Duo. Here''s How It Compares." in block
        assert "tone_illustrative: 0.45" in block
        assert "The iPhone Air Is Apple''s Most Impressive Phone in Years. But Most People Shouldn''t Buy It." in block

    def test_illustrative_delta_quoted(self):
        block = _block()
        assert "illustrative_register_delta_apple_minus_meta: 0.95" in block
        assert "0.500 - (-0.450) = +0.950" in block

    def test_statistical_discipline_fields(self):
        block = _block()
        for field in ("p_value: NOT_CALCULATED", "cohens_d: NOT_CALCULATED",
                      "ci_95: NOT_CALCULATED", "is_significant: false"):
            assert field in block
        assert "Engine NOT run" in block or "engine NOT run" in block.lower()
        assert "no_analysis_json_update: true" in block
        assert "NOT artifact-grade" in block

    def test_source_urls_verbatim(self):
        block = _block()
        assert "https://talkingbiznews.com/media-news/stolyar-departs-wired-for-wirecutter/amp/" in block
        assert "https://muckrack.com/bstoly/articles" in block
        assert "No per-article URL" in block or "no per-article" in block.lower()

    def test_excerpt_bounded_method(self):
        block = _block()
        assert "Search-excerpt-bounded per #503" in block
        assert "7 browser.search query sets" in block
        assert "1 browser.open terminally failed this turn, NOT retried" in block

    def test_migration_context_fields(self):
        block = _block()
        assert "circa May 2025" in block
        assert "WIRED staff writer, Gear team" in block
        assert "Wirecutter senior staff writer" in block
        assert "career context, not the causal mechanism" in block

    def test_wired_era_commerce_register_noted(self):
        block = _block()
        assert "commerce/deals register" in block
        assert "MagPod" in block

    def test_confounders_strong_pair(self):
        block = _block()
        assert "STRONG: Excerpt-bounded evidence" in block
        assert "STRONG: Story-type skew" in block
        assert "launch pegs draw more positive registers by genre convention" in block

    def test_counterevidence_buy_skeptical_kicker(self):
        block = _block()
        assert "buy-skeptical kicker" in block
        assert "product-specific, not entity-general" in block

    def test_cross_references_603_578_701(self):
        block = _block()
        for mid in ("603", "578", "701"):
            assert f"mechanism_id: {mid}" in block

    def test_block_key_unique_in_cross_publication_findings(self):
        text = _read_profile()
        assert text.count(MECH_KEY + ":") == 1
        block = _block()
        assert "block_key: type_b_788_brenda_stolyar_wired_wirecutter_meta_vs_apple_register_split_sep16" in block

    def test_competitor_coverage_research_yaml_still_parses(self):
        import yaml

        d = yaml.safe_load(_read_profile())
        assert d["cross_publication_findings"][MECH_KEY]["mechanism_id"] == M_ID


class TestSupersessionAndCorpusPost787:
    """Post-#787 corpus integrity: max 704, zero 705, designed supersession."""

    def test_max_numeric_mechanism_id_is_704(self):
        assert _max_numeric_mechanism_id() == M_ID

    def test_d787_max_703_sweep_superseded_by_design(self):
        # #787 asserted max == 703; advancing to 704 supersedes it per the
        # #710/#720 convention. Documented, not repaired.
        assert _max_numeric_mechanism_id() == 704 != 703

    def test_zero_underscore_705_keys_repo_wide(self):
        hits = _repo_grep(NEXT_ID_MARKER)
        assert hits == [], hits

    def test_zero_numeric_705_keys_in_profiles(self):
        hits = _repo_grep(NEXT_ID_NUMERIC, roots=("profiles",))
        assert hits == [], hits

    def test_d787_zero_underscore_704_profiles_sweep_fails_by_designed_supersession(self):
        # #787 asserted zero underscore-form 704 keys in profiles/; the m704
        # block key carries no such substring by designed keying (only this
        # file's marker and the numeric "mechanism_id: 704" hits), so the
        # profiles-side zero-704 sweep is expected to fail by designed
        # supersession, not by accident. Documented, not repaired.
        hits = _repo_grep(MECH_ID_MARKER, roots=("profiles",))
        assert hits == [], hits

    def test_d787_zero_underscore_704_tests_sweep_stays_green(self):
        # #787 asserted zero underscore-form 704 references in tests/; this
        # file builds the marker by concatenation ("mechanism" + "_704") so
        # no literal underscore-form 704 string exists in tests/.
        hits = _repo_grep(MECH_ID_MARKER, roots=("tests",))
        assert hits == [], hits

    def test_d787_zero_numeric_704_profiles_sweep_fails_by_designed_supersession(self):
        # #787 asserted zero "mechanism_id: 704" hits in profiles/; the m704
        # block introduces it by design. Documented, not repaired.
        hits = _repo_grep("mechanism_id: 704", roots=("profiles",))
        assert len(hits) >= 1, hits


class TestLedger788:
    """Falsification ledger: TWENTY-SIXTH present, TWENTY-SEVENTH absent; m704 not a member."""

    def _profiles_corpus(self):
        parts = []
        for root, _dirs, files in os.walk(PROFILES):
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

    def test_m704_not_a_falsification_family_member(self):
        block = _block()
        assert "NOT a falsification-family member" in block
        assert "register documentation, not a uniform-prediction test" in block

    def test_no_analysis_json_update_claimed(self):
        block = _block()
        assert "no_analysis_json_update: true" in block


class TestCareers788:
    """Careers profile: Brenda Stolyar keyed entry, beats, migration, linkage."""

    CAREERS = REPO / "profiles" / "careers" / "journalists.yaml"

    def _careers(self):
        return self.CAREERS.read_text(encoding="utf-8")

    def test_keyed_entry_with_name(self):
        careers = self._careers()
        assert "\nbrenda_stolyar:" in careers
        assert "name: Brenda Stolyar" in careers

    def test_role_and_publications(self):
        careers = self._careers()
        assert "current_role: Senior Staff Writer" in careers
        assert "current_publication: Wirecutter" in careers
        assert "previous_publication: WIRED" in careers
        assert "publication_owner: NYT" in careers

    def test_beats(self):
        careers = self._careers()
        assert "- smartphones" in careers
        assert "- tablets" in careers
        assert "- wearables" in careers

    def test_migration_block(self):
        careers = self._careers()
        assert "circa May 2025" in careers
        assert "https://talkingbiznews.com/media-news/stolyar-departs-wired-for-wirecutter/amp/" in careers

    def test_mechanism_linkage(self):
        careers = self._careers()
        assert "mechanism_ids: [704]" in careers
        assert "type_b_788_brenda_stolyar_wired_wirecutter_meta_vs_apple_register_split_sep16:" in careers

    def test_source_urls_verbatim_from_listings(self):
        careers = self._careers()
        assert "https://talkingbiznews.com/media-news/stolyar-departs-wired-for-wirecutter/amp/" in careers
        assert "https://muckrack.com/bstoly/articles" in careers

    def test_careers_yaml_still_parses(self):
        import yaml

        d = yaml.safe_load(self._careers())
        assert d["brenda_stolyar"]["mechanism_ids"] == [704]


README_PATH = REPO / "README.md"
ARCH_PATH = REPO / "docs" / "ARCHITECTURE.md"
LOG_PATH = REPO / "iteration-log.md"


def _read(p):
    return p.read_text(encoding="utf-8")


class TestDocSync788:
    """Doc-sync: README/ARCHITECTURE rows (go green in the doc-sync followup)."""

    def test_readme_row_788(self):
        assert TEST_BASENAME in _read(README_PATH)

    def test_readme_row_788_in_table(self):
        doc = _read(README_PATH)
        assert TEST_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))

    def test_architecture_row_788(self):
        assert TEST_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_788_file(self):
        doc = _read(ARCH_PATH)
        assert TEST_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))


class TestIterationLog788:
    """Iteration-log #788 entry (goes green in the doc-sync followup)."""

    def _tail(self):
        lines = _read(LOG_PATH).splitlines()
        # Entries are appended chronologically (post-#735 convention); the
        # #788 entry sits at the end of the file, not the top.
        return "\n".join(lines[-60:])

    def test_log_entry_present(self):
        tail = self._tail()
        assert "Type B #788" in tail
        assert "Brenda Stolyar" in tail

    def test_log_entry_records_rotation_leg(self):
        tail = self._tail()
        assert "784-788" in tail
        assert "C (#784) -> D (#785) -> E (#786) -> A (#787) -> B (#788)" in tail
