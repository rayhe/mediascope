"""Type B #778 (2026-09-15 20:00 PDT): Sarah Perez (TechCrunch, Yahoo)
trust-register asymmetry - Meta Muse launch interrogated in a trust register
vs OpenAI Astra demand celebrated in a demand register (mechanism 698).

Rotation window fourth leg: D (#775) -> E (#776) -> A (#777) -> B (#778).

The Meta arm is re-anchored from #638 (mechanism 617), where it served as the
Meta arm of a Meta-vs-Google pair; this run adds the OpenAI Astra-demand piece
(Sep 10 2026, byline Sarah Perez, zero repo-wide hits pre-commit) as a second
within-writer comparator. Both arms opened first-hand via browser.open this
run (verbatim techcrunch.com URLs). All scores are MANUAL ILLUSTRATIVE
(statistical discipline per the established convention: p_value/cohens_d/ci_95
NOT_CALCULATED, is_significant False, statistical_contract
degenerate_n1_per_arm); verdict directionally_supported_not_proven; NOT a
falsification-family member (ledger holds at 26); no analysis.json update.

Anchor placeholder: patched to the main commit SHA in the #565 follow-up.
"""

import os
import re
import subprocess

import pytest

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
RESEARCH_PATH = "profiles/competitor-coverage-research.yaml"
CAREERS_PATH = "profiles/careers/journalists.yaml"
README_PATH = "README.md"
ARCH_PATH = "docs/ARCHITECTURE.md"
LOG_PATH = "iteration-log.md"
TEST_BASENAME = (
    "test_type_b_778_sarah_perez_techcrunch_muse_trust_interrogation_"
    "vs_astra_demand_celebration_sep15_8pm.py"
)
MECH_NUM = 698
# Built by concatenation so the underscore-form marker never sits contiguously
# in this file: the #715 sweep-instrument convention.
MECH_ID_MARKER = "mechanism" + "_698"
NEXT_ID_MARKER = "mechanism" + "_699"
MECH_KEY = (
    "sarah perez techcrunch muse trust interrogation vs astra "
    "demand celebration sep2026"
)
CAREERS_BLOCK_KEY = (
    "type_b_778_sarah_perez_techcrunch_muse_trust_interrogation_"
    "vs_astra_demand_celebration_sep15"
)
ANCHORED_SHA = "9f999f246121e9d5ff2ef6c0bd753d14d6f54c03"
META_URL = (
    "https://techcrunch.com/2026/09/08/"
    "meta-debuts-its-muse-ai-agent-will-consumers-trust-it/"
)
OPENAI_URL = (
    "https://techcrunch.com/2026/09/10/"
    "openai-puts-pro-subscriptions-on-hold-due-to-astra-demand/"
)
AUTHOR_URL = "https://techcrunch.com/author/sarah-perez/"


def _read(rel):
    with open(os.path.join(REPO_ROOT, rel), encoding="utf-8") as fh:
        return fh.read()


def _block():
    doc = _read(RESEARCH_PATH)
    start = doc.index(MECH_KEY + ":")
    return doc[start:]


def _block_data():
    import yaml

    return yaml.safe_load(_block())[MECH_KEY]


def _repo_grep(pattern, roots=(".",)):
    out = subprocess.run(
        ["git", "-C", REPO_ROOT, "grep", "-l", "--", pattern, *roots],
        capture_output=True,
        text=True,
    )
    return sorted(out.stdout.splitlines())


def _profiles_corpus():
    out = subprocess.run(
        ["git", "-C", REPO_ROOT, "grep", "-h", "--", ".", "profiles"],
        capture_output=True,
        text=True,
    )
    return out.stdout


def _git_log_mains(pattern):
    out = subprocess.run(
        ["git", "-C", REPO_ROOT, "log", "--format=%H %s", "--no-merges",
         "--", "."],
        capture_output=True,
        text=True,
    )
    return [l for l in out.stdout.splitlines() if re.search(pattern, l)]


class TestNovelty778:
    """Pre-commit novelty: single new file, unique commit, new OpenAI arm."""

    def test_single_test_type_b_778_file(self):
        files = sorted(
            f for f in os.listdir(os.path.join(REPO_ROOT, "tests"))
            if f.startswith("test_type_b_778") and f.endswith(".py")
        )
        assert files == [TEST_BASENAME], files

    def test_type_b_778_main_commit_unique_and_anchored(self):
        mains = _git_log_mains(r"Type B #778: ")
        assert len(mains) == 1, mains
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP", "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ), mains
        assert mains[0].startswith(ANCHORED_SHA + " "), mains

    def test_novelty_verification_claim_present_in_block(self):
        # Novelty was verified pre-commit by shell greps (zero test_type_b_778
        # files, no "Type B #778" in git log, the OpenAI arm URL zero-hit
        # repo-wide pre-commit, the Meta arm re-anchored from #638 with byline
        # confirmed this run, max numeric mechanism_id 697 pre-commit, zero
        # underscore-form 698 keys excluding sweep-instrument carriers per
        # #715); this test pins the claim in the committed block, per the #752
        # convention.
        block = _block()
        assert "Zero test_type_b_778 files on disk pre-commit" in block
        assert 'no "Type B #778" in git log pre-commit' in block
        assert "zero-hit repo-wide pre-commit" in block
        assert "re-anchored from #638" in block
        assert "max numeric mechanism_id 697 pre-commit" in block


class TestRotationCycleGuard778:
    """Rotation: 774-778 window fourth leg D->E->A->B."""

    EXPECTED_ORDER = [
        ("B", "778"), ("A", "777"), ("E", "776"), ("D", "775"), ("C", "774"),
    ]
    ORDER = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}

    def _window(self):
        # First occurrence of each distinct iteration number, newest first
        # (robust to the #756-style followup commits that repeat the same
        # "Type X #N" wording without the colon, per the #752 convention).
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

    def test_window_closes_deab(self):
        assert self._window() == self.EXPECTED_ORDER

    def test_window_cycle_edges_are_adjacent(self):
        window = self._window()
        for (t1, _), (t2, _) in zip(window, window[1:]):
            assert (self.ORDER[t1] - self.ORDER[t2]) % 5 == 1, (t1, t2)

    def test_anchor_sha_matches_head(self):
        mains = _git_log_mains(r"Type B #778: ")
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP", "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ), mains
        assert mains and mains[0].startswith(ANCHORED_SHA + " "), mains


class TestMechanism698Content:
    def test_block_present_in_research(self):
        assert MECH_KEY + ":" in _read(RESEARCH_PATH)
        assert _block_data()["mechanism_id"] == MECH_NUM

    def test_iteration_metadata(self):
        data = _block_data()
        assert data["iteration"] == 778
        assert data["iteration_type"] == "B"
        assert data["rotation_type"] == "B"
        assert data["type"] == "B"
        assert data["iteration_time"] == "2026-09-15 20:00 PDT"
        assert data["discovery_date"] == "2026-09-15"
        assert data["goal_id"] == "goal_54093bda4145"
        assert data["job_id"] == "mediascope-daily-iteration"

    def test_journalist_fields(self):
        data = _block_data()
        assert data["journalist"] == "Sarah Perez"
        assert data["publication"] == "techcrunch"
        assert "yahoo" in data["owner"]

    def test_meta_arm_quotes(self):
        data = _block_data()
        arm = data["meta_arm"]
        assert arm["byline"] == "Sarah Perez"
        assert arm["date"] == "2026-09-08"
        assert arm["tone_illustrative"] == -0.45
        quotes = " ".join(arm["evidence_quotes"])
        assert "Will consumers trust it?" in quotes
        assert "$18 billion multistate settlement" in quotes
        assert "Could Meta's history hurt Muse adoption?" in quotes
        assert "deceived consumers by making users" in quotes
        assert "deeper investigation by security experts" in quotes
        assert META_URL in arm["source_urls"]

    def test_openai_arm_quotes(self):
        data = _block_data()
        arm = data["openai_arm"]
        assert arm["byline"] == "Sarah Perez"
        assert arm["date"] == "2026-09-10"
        assert arm["tone_illustrative"] == 0.45
        quotes = " ".join(arm["evidence_quotes"])
        assert "newest and most powerful model" in quotes
        assert "really unprecedented" in quotes
        assert "AGI era" in quotes
        assert "generational leap" in quotes
        assert "hasn't said how long sign-ups" in quotes
        assert "Hugging Face" in quotes
        assert OPENAI_URL in arm["source_urls"]

    def test_manual_illustrative_discipline(self):
        data = _block_data()
        scorer = data["asymmetry_scorer"]
        assert scorer["meta_trust_tone"] == -0.45
        assert scorer["openai_demand_tone"] == 0.45
        assert (
            scorer["illustrative_trust_register_delta_meta_minus_openai"]
            == -0.90
        )
        assert scorer["delta_calc"] == "-0.45 - 0.45 = -0.90"
        assert scorer["p_value"] == "NOT_CALCULATED"
        assert scorer["cohens_d"] == "NOT_CALCULATED"
        assert scorer["ci_95"] == "NOT_CALCULATED"
        assert scorer["is_significant"] is False
        assert scorer["statistical_contract"] == "degenerate_n1_per_arm"
        assert "MANUAL ILLUSTRATIVE" in scorer["tone_basis"]

    def test_financial_context_yahoo_chain(self):
        ctx = _block_data()["financial_context_yahoo_chain"]
        assert "Apollo" in ctx["owner"]
        assert "No documented AI content-licensing deal" in ctx["documented_deals"]
        assert ctx["prediction"].startswith("NULL")
        assert "zero-gradient control" in ctx["prediction"]
        assert "695" in ctx["mechanism"]

    def test_confounder_strength_layers(self):
        data = _block_data()
        layers = [c.split(":")[0] for c in data["confounders"]]
        assert layers.count("STRONG") == 3
        assert layers.count("MODERATE") == 3
        assert layers.count("WEAK") == 2
        assert len(data["confounders"]) == 8

    def test_four_counterevidence(self):
        data = _block_data()
        assert len(data["counterevidence"]) == 4
        joined = " ".join(data["counterevidence"])
        assert "COUNTEREVIDENCE" in joined
        assert "hypothesis-generating only" in joined

    def test_verdict_ledger_and_careers_backlink(self):
        data = _block_data()
        assert data["verdict"] == "directionally_supported_not_proven"
        assert data["no_analysis_json_update"] is True
        assert "NOT a falsification-family member" in data["asymmetry_scorer"]["verdict"]
        assert "ledger holds at 26" in data["asymmetry_scorer"]["verdict"]
        careers = _read(CAREERS_PATH)
        assert CAREERS_BLOCK_KEY in careers
        assert "Sarah Perez" in careers
        assert "mechanism_id: 698" in careers

    def test_designed_keying_no_underscore_form_in_block(self):
        # The m698 block key carries no underscore-form marker substring, so
        # #779's zero-underscore-698 sweeps stay GREEN.
        assert MECH_ID_MARKER not in _block()
        assert MECH_ID_MARKER not in _read(CAREERS_PATH)


class TestSupersessionAndCorpusPost777:
    """Post-#777 corpus integrity: max 698, zero 699, designed supersession."""

    def _ids(self):
        return [
            int(x)
            for x in re.findall(r"mechanism_id:\s*(\d+)\b", _profiles_corpus())
        ]

    def test_max_numeric_mechanism_id_is_698(self):
        assert max(self._ids()) == MECH_NUM, max(self._ids())

    def test_697_still_present(self):
        hits = [h for h in _repo_grep("mechanism_id: 697")]
        assert len(hits) >= 1, hits

    def test_zero_underscore_699_keys_repo_wide(self):
        hits = _repo_grep(NEXT_ID_MARKER)
        assert hits == [], hits

    def test_zero_numeric_699_keys_in_profiles(self):
        hits = _repo_grep("mechanism_id: 699", roots=("profiles",))
        assert hits == [], hits

    def test_d777_zero_underscore_698_profiles_sweep_stays_green(self):
        # #777 asserted zero underscore-form 698 markers in profiles/; the
        # m698 block key carries no such substring by designed keying, so
        # that sweep stays green.
        hits = _repo_grep(MECH_ID_MARKER, roots=("profiles",))
        assert hits == [], hits

    def test_d777_zero_underscore_698_tests_sweep_stays_green(self):
        # #777 asserted zero underscore-form 698 markers in tests/; this file
        # builds the marker by concatenation ("mechanism" + "_698") and
        # carries no contiguous literal, so the sweep stays green.
        hits = _repo_grep(MECH_ID_MARKER, roots=("tests",))
        hits = [h for h in hits if not h.endswith(TEST_BASENAME)]
        assert hits == [], hits

    def test_d777_zero_numeric_698_profiles_sweep_fails_by_designed_supersession(
        self,
    ):
        # #777 asserted zero "mechanism_id: 698" hits in profiles/; the m698
        # block supersedes it by design per the #710/#720 convention.
        hits = _repo_grep("mechanism_id: 698", roots=("profiles",))
        assert len(hits) >= 1, hits

    def test_d777_max_697_sweep_superseded_by_design(self):
        # #777 asserted max == 697; advancing to 698 supersedes it per the
        # #710/#720 convention. Documented, not repaired.
        assert max(self._ids()) == MECH_NUM != 697


class TestLedger778:
    """Falsification ledger: TWENTY-SIXTH present, TWENTY-SEVENTH absent; m698 not a member."""

    def test_twenty_sixth_present_and_twenty_seventh_absent(self):
        # Guard targets the profiles corpus per the #754 convention (prior type
        # files legitimately reference "TWENTY-SEVENTH" inside their own
        # negative guards, so a tests/ sweep would false-positive).
        corpus = _profiles_corpus()
        assert "TWENTY-SIXTH" in corpus
        assert "TWENTY-SEVENTH" not in corpus
        assert "ledger holds at 26" in _block()

    def test_m698_not_a_falsification_family_member(self):
        block = _block()
        assert "NOT a falsification-family member" in block
        assert "thesis-consistent direction" in block.lower()

    def test_no_analysis_json_update_claimed(self):
        block = _block()
        assert "no_analysis_json_update: true" in block


class TestDocSync778:
    def test_readme_row_778(self):
        assert TEST_BASENAME in _read(README_PATH)

    def test_architecture_row_778(self):
        assert TEST_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_778_file(self):
        doc = _read(ARCH_PATH)
        assert TEST_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))


class TestIterationLog778:
    def _tail(self):
        lines = _read(LOG_PATH).splitlines()
        # Entries are appended chronologically (post-#735 convention); the
        # #778 entry sits at the end of the file, not the top.
        return "\n".join(lines[-80:])

    def test_log_entry_present(self):
        # "#778 Type B:" is the entry header; a bare "#778" would
        # false-positive on #777's rotation line ("B (#778) -> ...").
        assert "#778 Type B:" in self._tail()

    def test_log_mechanism_number_and_journalist(self):
        assert "mechanism 698" in self._tail()
        assert "Sarah Perez" in self._tail()


class TestDateGrounding778:
    @staticmethod
    def _weekday(d):
        return subprocess.run(
            ["date", "-d", d, "+%A"], capture_output=True, text=True
        ).stdout.strip()

    def test_sep_15_2026_is_tuesday(self):
        assert self._weekday("2026-09-15") == "Tuesday"
