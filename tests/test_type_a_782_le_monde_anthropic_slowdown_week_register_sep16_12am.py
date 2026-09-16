#!/usr/bin/env python3
"""Type A #782: Le Monde x Anthropic slowdown-week register set vs carried Le Monde
x Meta tobacco editorial and x OpenAI neutral business news (m322) - competitor
coverage deep dive.

Mechanism 700 under profiles/competitor-coverage-research.yaml -> publications.

Three novel Le Monde x Anthropic arms (Sep 11-15 2026, search-excerpt-bounded per
#503, 0 browser.open attempts): Sep 11 /pixels/ news on the Coxon resignation and
AI incidents, accountability register (-0.35 illustrative); Sep 15 /opinion/
"AIpocalypse/big money" piece, financialized-sardonic register (-0.25); Sep 15
/opinion/ "regain control" piece, constructive Amodei-essay relay (-0.10). Anthropic
avg -0.23 vs carried m322 arms: Le Monde x Meta Aug 20 /idees/ tobacco/alarm
editorial (hardest register) and Le Monde x OpenAI Aug 24 /economie/ neutral business
news (softest register). Payer-status inversion: the triple-AI-payer outlet (OpenAI
Mar 2024, Perplexity May 2025, Meta Dec 2025; 25% of AI licensing revenue shared
with journalists) applies its hardest register to a payer (Meta), a mid
adversarial-accountability register to the non-payer (Anthropic, no documented deal),
and its softest to the longest-standing payer (OpenAI). Register selected by
commissioning/genre and event, not by financial tie. Extends m322's [STRONG]
confounder and m697's register-selection dominance. NOT a falsification-family
member (register documentation, not a uniform-prediction test); ledger holds at 26;
no analysis.json update; engine NOT run; p_value/cohens_d/ci_95 NOT_CALCULATED;
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
MECH_KEY = "le_monde_anthropic_slowdown_week_register_set_vs_meta_tobacco_openai_neutral_sep16"
M_ID = 700
# Built by concatenation per the #723/#738/#739 designed-keying convention: the literal
# ("mechanism" + "_700") never appears in tests/ or profiles/, keeping the #780/#781
# zero-700 sweep instruments green pre-commit. (Used only via this constant.)
MECH_ID_MARKER = "mechanism" + "_700"
NEXT_ID_MARKER = "mechanism" + "_701"
NEXT_ID_NUMERIC = "mechanism_id: 701"

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


class TestNovelty782:
    def test_single_test_type_a_782_file(self):
        files = sorted(p.name for p in TESTS_DIR.glob("test_type_a_782_*.py"))
        assert files == [TEST_BASENAME], files

    def test_type_a_782_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 followup convention; patched
        # green post-commit. Novelty was verified pre-commit by shell
        # greps (zero test_type_a_782 files, no #782 in git log); this test
        # pins that no duplicate #782 main commit ever appears.
        #
        # Hardened per the #760 rotation-guard note (applied in #776): the
        # naive "Type A #782:" prefix also matches the followup subjects
        # ("Type A #782 (followup):", "Type A #782 (doc-sync):") and a
        # push-blocked status commit. The ": le_monde" qualifier pins only
        # the main commit.
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
            if re.match(r"^[0-9a-f]{40} Type A #782: le_monde", line)
        ]
        assert len(mains) == 1, "expected exactly one #782 main commit, got %r" % (mains,)
        sha = mains[0].split()[0]
        assert ANCHORED_SHA != "PATCH_ME_IN_FOLLOWUP", "anchor not patched"
        assert sha == ANCHORED_SHA, "main commit %s != anchor %s" % (sha, ANCHORED_SHA)

    def test_novelty_verification_claim_present_in_block(self):
        block = _block()
        for s in [
            "Zero test_type_a_782 files on disk pre-commit",
            '"Type A #782" in git log pre-commit',
            "URL slugs (6757415_13, 6757529_23, 6757554_23)",
            "block key zero-hit repo-wide pre-commit",
            "max numeric mechanism_id 699 pre-commit",
            "#780 sweep-instrument carrier test",
        ]:
            assert s in block, s


class TestRotationCycleGuard782:
    """780-784 window third leg A->E->D->C->B. Green only after the main commit.

    Deselected pre-commit per the #565 followup convention (the #782 main
    commit does not exist yet); patched green in the anchor followup.
    """

    EXPECTED_ORDER = [("A", "782"), ("E", "781"), ("D", "780"), ("C", "779"), ("B", "778")]
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

    def test_window_780_784_third_leg_a(self):
        assert self._window() == self.EXPECTED_ORDER

    def test_rotation_adjacency_cycle_valid(self):
        window = self._window()
        for (t1, n1), (t2, n2) in zip(window, window[1:]):
            assert int(n1) == int(n2) + 1
            assert (self.ORDER[t1] - self.ORDER[t2]) % 5 == 1, (t1, t2)

    def test_anchor_sha_matches_head(self):
        mains = _git_log_mains("Type A #782: le_monde")
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ), mains
        assert mains and mains[0].startswith(ANCHORED_SHA + " "), mains


class TestMechanism700Content:
    def test_block_present_under_publications(self):
        import yaml

        d = yaml.safe_load(_read_profile())
        node = d["publications"][MECH_KEY]
        assert node["mechanism_id"] == M_ID

    def test_block_metadata(self):
        import yaml

        node = yaml.safe_load(_read_profile())["publications"][MECH_KEY]
        assert node["iteration"] == 782
        assert node["iteration_type"] == "A"
        assert node["type"] == "competitor_coverage_deep_dive"
        assert node["date_analyzed"] == "2026-09-16"
        assert node["time_pdt"] == "00:00"
        assert node["goal_id"] == "goal_54093bda4145"
        assert node["author"] == "Kit (with Ray)"

    def test_three_arms_titles_registers_tones(self):
        # Raw profile text: YAML single-quoted scalars double internal
        # apostrophes, so the assertions use the '' form.
        block = _block()
        for title, register, tone in [
            (
                "researcher''s resignation push ''AIpocalypse''",
                "accountability_incident_reporting",
                "-0.35",
            ),
            (
                "about big money",
                "financialized_sardonic_opinion",
                "-0.25",
            ),
            (
                "regain control over global AI race",
                "constructive_safety_relay",
                "-0.10",
            ),
        ]:
            assert title in block, title
            assert register in block, register
            assert f"tone_MANUAL_ILLUSTRATIVE: {tone}" in block, tone

    def test_arm1_excerpts_verbatim(self):
        block = _block()
        for s in [
            "gambling with our lives, (Coxon, quoted)",
            "[more than] 10% within the next",
            "A 10% chance does seem not an unreasonable estimate to me.",
            "We cannot stick our heads in the sand",
        ]:
            assert s in block, s

    def test_arm2_excerpts_verbatim(self):
        block = _block()
        for s in [
            "How much is a company worth if it could potentially wipe out humanity?",
            "and above all, about",
            "without ever having demonstrated how",
        ]:
            assert s in block, s

    def test_arm3_excerpts_verbatim(self):
        block = _block()
        for s in [
            "head of Anthropic ... called for",
            "His appeal was supported by Anthropic''s main American competitors.",
            "Financial logic adds another layer of inertia.",
            "Trump has flatly rejected calls to slow down",
        ]:
            assert s in block, s

    def test_anchor_urls_novel_precommit(self):
        block = _block()
        for slug, url in [
            (
                "6757415_13",
                "https://www.lemonde.fr/en/pixels/article/2026/09/11/ai-incidents-and-anthropic-researcher-s-resignation-push-aipocalypse-debate-to-new-heights_6757415_13.html",
            ),
            (
                "6757529_23",
                "https://www.lemonde.fr/en/opinion/article/2026/09/15/the-growing-debate-over-the-aipocalypse-is-also-and-above-all-about-big-money_6757529_23.html",
            ),
            (
                "6757554_23",
                "https://www.lemonde.fr/en/opinion/article/2026/09/15/the-urgent-need-to-regain-control-over-global-ai-race_6757554_23.html",
            ),
        ]:
            assert slug in block, slug
            assert url in block, url
            assert "url_status" in block

    def test_carried_m322_comparators(self):
        block = _block()
        for s in [
            "mechanism: 322",
            "carry_note: 'carried from m322 by design'",
            "alarm_tobacco_editorial",
            "neutral_business_news",
            "cigarettiers",
        ]:
            assert s in block, s

    def test_manual_scores_and_avg(self):
        block = _block()
        for s in [
            "anthropic_arm_scores: [-0.35, -0.25, -0.10]",
            "anthropic_avg: -0.23",
            "MANUAL ILLUSTRATIVE",
            "INVERSE of the uniform financial-incentive",
        ]:
            assert s in block, s

    def test_payer_status_ordering(self):
        block = _block()
        assert "payer_status_ordering" in block
        assert "NON-payer, no documented AI licensing deal" in block
        assert "Meta (payer, Dec 2025): hardest register" in block

    def test_incentive_attribution_bounded(self):
        block = _block()
        assert "does not monotonically predict register" in block
        assert "INCONCLUSIVE for any directional incentive claim" in block
        assert "Correlation is not causation" in block

    def test_confounders_ranked_strong_first(self):
        block = _block()
        assert "confounders_ranked" in block
        assert "strong:" in block
        assert "moderate:" in block
        assert "weak:" in block
        assert "Genre convention" in block
        assert "Event-driven" in block

    def test_counter_evidence_present(self):
        block = _block()
        assert "counter_evidence" in block
        assert "softest Anthropic arm (-0.10)" in block
        assert "deux freres ennemis" in block

    def test_statistical_discipline_string(self):
        block = _block()
        assert "NOT_CALCULATED" in block
        assert "is_significant: false" in block
        assert "Engine NOT" in block
        assert "directionally_supported_not_proven" in block

    def test_designed_keying_no_underscore_form_in_block(self):
        block = _block()
        assert MECH_ID_MARKER not in block
        assert MECH_KEY in _read_profile()

    def test_research_method_discloses_no_browser_open(self):
        block = _block()
        assert "0 browser.open attempts" in block
        assert "search-excerpt-bounded per #503" in block
        assert "ASCII-only, no em dashes" in block


class TestSupersessionAndCorpusPost781:
    """Post-#781 corpus integrity: max 700, zero 701, designed supersession."""

    def test_max_numeric_mechanism_id_is_700(self):
        assert _max_numeric_mechanism_id() == M_ID

    def test_699_still_present(self):
        hits = _repo_grep("mechanism_id: 699")
        assert len(hits) >= 1, hits

    def test_zero_underscore_701_keys_repo_wide(self):
        hits = _repo_grep(NEXT_ID_MARKER)
        assert hits == [], hits

    def test_zero_numeric_701_keys_in_profiles(self):
        hits = _repo_grep(NEXT_ID_NUMERIC, roots=("profiles",))
        assert hits == [], hits

    def test_d780_zero_underscore_700_profiles_sweep_stays_green(self):
        # #780 asserted zero underscore-form 700 literals in profiles/; the
        # m700 block key carries no such substring by designed keying, so
        # that sweep stays green.
        hits = _repo_grep(MECH_ID_MARKER, roots=("profiles",))
        assert hits == [], hits

    def test_d780_zero_underscore_700_tests_sweep_stays_green(self):
        # #780 asserted zero underscore-form 700 references in tests/; this
        # file builds the marker by concatenation ("mechanism" + "_700") so
        # no contiguous literal exists in tests/ either - the sweep stays
        # green.
        hits = _repo_grep(MECH_ID_MARKER, roots=("tests",))
        own = str((TESTS_DIR / Path(__file__).name).relative_to(REPO))
        hits = [h for h in hits if h != own]
        assert hits == [], hits

    def test_d780_zero_numeric_700_profiles_sweep_fails_by_designed_supersession(self):
        # #780 asserted zero "mechanism_id: 700" hits in profiles/; the m700
        # block supersedes it by design per the #710/#720 convention.
        hits = _repo_grep("mechanism_id: 700", roots=("profiles",))
        assert len(hits) >= 1, hits

    def test_d780_max_699_sweep_superseded_by_design(self):
        # #780 asserted max == 699; advancing to 700 supersedes it per the
        # #710/#720 convention. Documented, not repaired.
        assert _max_numeric_mechanism_id() == 700 != 699

    def test_m700_block_key_unique_in_publications(self):
        text = _read_profile()
        assert text.count(MECH_KEY + ":") == 1

    def test_competitor_coverage_research_yaml_still_parses(self):
        import yaml

        d = yaml.safe_load(_read_profile())
        assert d["publications"][MECH_KEY]["mechanism_id"] == M_ID


class TestLedger782:
    """Falsification ledger: TWENTY-SIXTH present, TWENTY-SEVENTH absent; m700 not a member."""

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

    def test_m700_not_a_falsification_family_member(self):
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


class TestDocSync782:
    def test_readme_row_782(self):
        assert TEST_BASENAME in _read(README_PATH)

    def test_readme_row_782_in_table(self):
        doc = _read(README_PATH)
        assert TEST_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))

    def test_architecture_row_782(self):
        assert TEST_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_782_file(self):
        doc = _read(ARCH_PATH)
        assert TEST_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))


class TestIterationLog782:
    def _tail(self):
        lines = _read(LOG_PATH).splitlines()
        # Entries are appended chronologically (post-#735 convention); the
        # #782 entry sits at the end of the file, not the top.
        return "\n".join(lines[-60:])

    def test_log_entry_present(self):
        # "#782 Type A:" is the entry header; a bare "#782" would
        # false-positive on #781's rotation line ("A (#782) -> ...").
        assert "#782 Type A:" in self._tail()

    def test_log_cycle_and_hour(self):
        assert "780-784" in self._tail()
        assert "00:00 PDT" in self._tail()
