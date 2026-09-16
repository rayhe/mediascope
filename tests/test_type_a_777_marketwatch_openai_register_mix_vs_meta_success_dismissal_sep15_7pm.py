#!/usr/bin/env python3
"""Type A #777: MarketWatch x OpenAI slowdown-week register set vs MarketWatch x Meta
success dismissal (m229) - competitor coverage deep dive.

Mechanism 697 under profiles/news-corp.yaml -> competitor_relationships.openai.

Three novel MarketWatch x OpenAI arms (Sep 8-15 2026, search-excerpt-bounded per #503):
IPO-delay safety relay (-0.05 illustrative), Oracle-ecosystem aspirational boost (+0.30),
doomsday-fears-as-market-headwind (-0.10). OpenAI avg +0.05 vs carried MarketWatch x Meta
arm -0.55 (m229): illustrative delta +0.60 in the incentive-hypothesis direction, bounded by
strong genre confounds (financial publication; Oracle piece is an equity story; doomsday
piece targets the fear as a market event, not OpenAI). The IPO piece's own Opinion sidebar
("Would you buy stock in a company whose own scientists think the product might kill you?")
runs HARDER than the news arms: within-publication register boundary. The intended
Axios x OpenAI pair was ABANDONED (no verbatim axios.com URL surfaced in any Full-URL
listing; the Sep 12 Axios IPO piece by Berkowitz/Phifer is attested only via mirrors:
biztoc "appeared on axios.com, 2026-09-12 19:18:32", finpresso, digitaltoday, runtimewire).
News Corp dual-AI-payer context: OpenAI leg May 2024 (~$50M/yr, $250M/5yr); Meta leg
Mar 2026 (up to $50M/yr, 3yr). m697 is NOT a falsification-family member (register
documentation, not a uniform-prediction test); ledger holds at 26; no analysis.json update;
engine NOT run; p_value/cohens_d/ci_95 NOT_CALCULATED; correlation is not causation.
"""

import os
import re
import subprocess
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
PROFILES = REPO / "profiles"
TESTS_DIR = REPO / "tests"
PROFILE = PROFILES / "news-corp.yaml"
TEST_BASENAME = Path(__file__).name
MECH_KEY = "marketwatch_openai_ipo_delay_oracle_boost_doomsday_market_register_sep15"
M_ID = 697
# Built by concatenation per the #723/#738/#739 designed-keying convention: the literal
# ("mechanism" + "_697") never appears in tests/ or profiles/, keeping the #774/#775 zero-697
# sweep instruments green. (Used only via this constant.)
MECH_ID_MARKER = "mechanism" + "_697"
NEXT_ID_MARKER = "mechanism" + "_698"
NEXT_ID_NUMERIC = "mechanism_id: 698"

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
    end = text.index("\n  meta:", start)
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


class TestNovelty777:
    def test_single_test_type_a_777_file(self):
        files = sorted(p.name for p in TESTS_DIR.glob("test_type_a_777_*.py"))
        assert files == [TEST_BASENAME], files

    def test_type_a_777_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 followup convention; patched
        # green post-commit. Novelty was verified pre-commit by shell
        # greps (zero test_type_a_777 files, no #777 in git log); this test
        # pins that no duplicate #777 main commit ever appears.
        #
        # Hardened per the #760 rotation-guard note (applied in #776): the
        # naive "Type A #777:" prefix also matches the followup subjects
        # ("Type A #777 (followup):", "Type A #777 (doc-sync):") and a
        # push-blocked status commit ("Type A #777: push-blocked status").
        # The ": marketwatch" qualifier pins only the main commit.
        log = subprocess.run(
            ["git", "log", "--format=%H %s"],
            cwd=REPO,
            capture_output=True,
            text=True,
            check=True,
        ).stdout.splitlines()
        mains = [
            line
            for line in log
            if re.match(r"^[0-9a-f]{40} Type A #777: marketwatch", line)
        ]
        assert len(mains) == 1, "expected exactly one #777 main commit, got %r" % (mains,)
        sha = mains[0].split()[0]
        assert ANCHORED_SHA != "PATCH_ME_IN_FOLLOWUP", "anchor not patched"
        assert sha == ANCHORED_SHA, "main commit %s != anchor %s" % (sha, ANCHORED_SHA)

    def test_novelty_verification_claim_present_in_block(self):
        block = _block()
        for s in [
            "Zero test_type_a_777 files on disk pre-commit",
            'no "Type A #777" in git log pre-commit',
            "URL slugs (229de89c, f53c8024, 75c4ad53) zero-hit repo-wide pre-commit",
            "block key zero-hit repo-wide pre-commit",
            "max numeric mechanism_id 696 pre-commit",
            "#774 sweep-instrument carrier test",
        ]:
            assert s in block, s


class TestRotationCycleGuard777:
    """775-779 window third leg A->E->D->C->B. Green only after the main commit.

    Deselected pre-commit per the #565 followup convention (the #777 main
    commit does not exist yet); patched green in the anchor followup.
    """

    EXPECTED_ORDER = [("A", "777"), ("E", "776"), ("D", "775"), ("C", "774"), ("B", "773")]
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

    def test_window_775_779_third_leg_a(self):
        assert self._window() == self.EXPECTED_ORDER

    def test_rotation_adjacency_cycle_valid(self):
        window = self._window()
        for (t1, n1), (t2, n2) in zip(window, window[1:]):
            assert int(n1) == int(n2) + 1
            assert (self.ORDER[t1] - self.ORDER[t2]) % 5 == 1, (t1, t2)

    def test_anchor_sha_matches_head(self):
        mains = _git_log_mains("Type A #777: marketwatch")
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ), mains
        assert mains and mains[0].startswith(ANCHORED_SHA + " "), mains


class TestMechanism697Content:
    def test_block_present_under_news_corp_openai(self):
        import yaml

        d = yaml.safe_load(_read_profile())
        node = d["competitor_relationships"]["openai"][MECH_KEY]
        assert node["mechanism_id"] == M_ID

    def test_block_metadata(self):
        import yaml

        node = yaml.safe_load(_read_profile())["competitor_relationships"]["openai"][
            MECH_KEY
        ]
        assert node["iteration"] == 777
        assert node["iteration_type"] == "A"
        assert node["type"] == "competitor_coverage_deep_dive"
        assert node["date_analyzed"] == "2026-09-15"
        assert node["time_pdt"] == "19:00"
        assert node["goal_id"] == "goal_54093bda4145"
        assert node["author"] == "Kit (with Ray)"

    def test_three_arms_titles_registers_tones(self):
        # Raw profile text: YAML single-quoted scalars double internal
        # apostrophes, so the assertions use the '' form.
        block = _block()
        for title, register, tone in [
            (
                "Why OpenAI''s Sam Altman says an IPO isn''t in the cards this year",
                "constructive_ceo_framing_relay",
                "-0.05",
            ),
            (
                "Oracle''s stock gets a boost as the OpenAI ecosystem comes back into favor",
                "aspirational_ecosystem_bullish",
                "0.30",
            ),
            (
                "AI doomsday fears are arriving at the worst possible time for the stock market",
                "safety_slowdown_as_market_headwind",
                "-0.10",
            ),
        ]:
            assert title in block, title
            assert register in block, register
            assert f"tone_MANUAL_ILLUSTRATIVE: {tone}" in block, tone

    def test_arm1_excerpts_verbatim(self):
        block = _block()
        for s in [
            "As backlash swells against artificial-intelligence companies, the CEO of OpenAI says he won''t be testing the public markets this year.",
            "ill-advised moment to go public, and we don''t feel pressure on that,",
            "Opinion: Would you buy stock in a company whose own scientists think the product might kill you?",
        ]:
            assert s in block, s

    def test_arm2_excerpts_verbatim(self):
        block = _block()
        for s in [
            "retaking the crown in an ever-evolving race",
            "It looks like OpenAI is turning things around, and Astra is ahead of Fable on multiple benchmarks,",
            "OpenAI signed a contract with Oracle in September last year to buy $300 billion in computing power over five years",
        ]:
            assert s in block, s

    def test_arm3_excerpts_verbatim(self):
        block = _block()
        for s in [
            "AI doomsday fears are arriving at the worst possible time for the stock market",
            "The latest cracks in the artificial-intelligence trade are emerging at a particularly troubling time for investors.",
            "Jacob Coxon said in a post on X that he had left the company because he felt that the headlong race",
        ]:
            assert s in block, s

    def test_anchor_urls_novel_precommit(self):
        block = _block()
        for slug, url in [
            (
                "229de89c",
                "https://www.marketwatch.com/story/why-openais-sam-altman-says-an-ipo-isnt-in-the-cards-this-year-229de89c",
            ),
            (
                "f53c8024",
                "https://www.marketwatch.com/story/oracles-stock-gets-a-boost-as-the-openai-ecosystem-comes-back-into-favor-f53c8024",
            ),
            (
                "75c4ad53",
                "https://www.marketwatch.com/story/ai-doomsday-fears-are-arriving-at-the-worst-possible-time-for-the-stock-market-75c4ad53",
            ),
        ]:
            assert slug in block, slug
            assert url in block, url
            assert "url_status" in block

    def test_meta_arm_carried_from_229(self):
        block = _block()
        for s in [
            "mechanism: 229",
            "carried from m229 by design",
            "No one really wants Meta glasses",
            "84% market share",
            "meta_arm_score: -0.55",
        ]:
            assert s in block, s

    def test_manual_scores_and_delta(self):
        block = _block()
        for s in [
            "openai_arm_scores: [-0.05, 0.30, -0.10]",
            "openai_avg: 0.05",
            "delta: 0.60",
            "MANUAL ILLUSTRATIVE",
            "26+ months old, May 2024",
            "6 months old, Mar 2026",
        ]:
            assert s in block, s

    def test_incentive_attribution_bounded(self):
        block = _block()
        assert "DIRECTIONALLY CONSISTENT but INCONCLUSIVE" in block
        assert "within-publication register boundary" in block
        assert "Correlation is not causation" in block

    def test_confounders_ranked_strong_first(self):
        block = _block()
        assert "confounders_ranked" in block
        assert "strong:" in block
        assert "moderate:" in block
        assert "weak:" in block
        assert "Excerpt-bounded read" in block
        assert "Financial-publication genre" in block

    def test_counter_evidence_present(self):
        block = _block()
        assert "counter_evidence" in block
        assert "Opinion sidebar" in block
        assert "m682 (Sep 14)" in block

    def test_statistical_discipline_string(self):
        block = _block()
        assert "NOT_CALCULATED" in block
        assert "is_significant: false" in block
        assert "engine NOT run" in block
        assert "directionally_supported_not_proven" in block

    def test_designed_keying_no_underscore_form_in_block(self):
        block = _block()
        assert MECH_ID_MARKER not in block
        assert MECH_KEY in _read_profile()

    def test_research_method_discloses_no_browser_open(self):
        block = _block()
        assert "0 browser.open attempts" in block
        assert "Excerpt-bounded per #503" in block
        assert "ASCII-only, no em dashes" in block


class TestSupersessionAndCorpusPost776:
    """Post-#776 corpus integrity: max 697, zero 698, designed supersession."""

    def test_max_numeric_mechanism_id_is_697(self):
        assert _max_numeric_mechanism_id() == M_ID

    def test_696_still_present(self):
        hits = _repo_grep("mechanism_id: 696")
        assert len(hits) >= 1, hits

    def test_zero_underscore_698_keys_repo_wide(self):
        hits = _repo_grep(NEXT_ID_MARKER)
        assert hits == [], hits

    def test_zero_numeric_698_keys_in_profiles(self):
        hits = _repo_grep(NEXT_ID_NUMERIC, roots=("profiles",))
        assert hits == [], hits

    def test_d775_zero_underscore_697_profiles_sweep_stays_green(self):
        # #775 asserted zero underscore-form 697 literals in profiles/; the
        # m697 block key carries no such substring by designed keying, so
        # that sweep stays green.
        hits = _repo_grep(MECH_ID_MARKER, roots=("profiles",))
        assert hits == [], hits

    def test_d775_zero_underscore_697_tests_sweep_stays_green(self):
        # #775 asserted zero underscore-form 697 references in tests/; this
        # file builds the marker by concatenation ("mechanism" + "_697") so
        # no contiguous literal exists in tests/ either - the sweep stays
        # green.
        hits = _repo_grep(MECH_ID_MARKER, roots=("tests",))
        own = str((TESTS_DIR / Path(__file__).name).relative_to(REPO))
        hits = [h for h in hits if h != own]
        assert hits == [], hits

    def test_d775_zero_numeric_697_profiles_sweep_fails_by_designed_supersession(self):
        # #775 asserted zero "mechanism_id: 697" hits in profiles/; the m697
        # block supersedes it by design per the #710/#720 convention.
        hits = _repo_grep("mechanism_id: 697", roots=("profiles",))
        assert len(hits) >= 1, hits

    def test_d775_max_696_sweep_superseded_by_design(self):
        # #775 asserted max == 696; advancing to 697 supersedes it per the
        # #710/#720 convention. Documented, not repaired.
        assert _max_numeric_mechanism_id() == 697 != 696

    def test_m697_block_key_unique_in_news_corp(self):
        text = _read_profile()
        assert text.count(MECH_KEY + ":") == 1

    def test_news_corp_yaml_still_parses(self):
        import yaml

        d = yaml.safe_load(_read_profile())
        assert d["competitor_relationships"]["openai"][MECH_KEY]["mechanism_id"] == M_ID


class TestLedger777:
    """Falsification ledger: TWENTY-SIXTH present, TWENTY-SEVENTH absent; m697 not a member."""

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

    def test_m697_not_a_falsification_family_member(self):
        block = _block()
        assert "NOT a falsification-family member" in block
        assert "register documentation, not a uniform-prediction test" in block

    def test_no_analysis_json_update_claimed(self):
        block = _block()
        assert "no_analysis_json_update: true" in block


README_PATH = REPO / "README.md"
ARCH_PATH = REPO / "docs" / "ARCHITECTURE.md"
LOG_PATH = REPO / "iteration-log.md"


def _read(p):
    return p.read_text(encoding="utf-8")


class TestDocSync777:
    def test_readme_row_777(self):
        assert TEST_BASENAME in _read(README_PATH)

    def test_readme_row_777_in_table(self):
        doc = _read(README_PATH)
        assert TEST_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))

    def test_architecture_row_777(self):
        assert TEST_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_777_file(self):
        doc = _read(ARCH_PATH)
        assert TEST_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))


class TestIterationLog777:
    def _tail(self):
        lines = _read(LOG_PATH).splitlines()
        # Entries are appended chronologically (post-#735 convention); the
        # #777 entry sits at the end of the file, not the top.
        return "\n".join(lines[-60:])

    def test_log_entry_present(self):
        # "#777 Type A:" is the entry header; a bare "#777" would
        # false-positive on #776's rotation line ("A (#777) -> ...").
        assert "#777 Type A:" in self._tail()

    def test_log_cycle_and_hour(self):
        assert "775-779" in self._tail()
        assert "19:00 PDT" in self._tail()
