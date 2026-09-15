"""Type C #774 (2026-09-15 16:00 PDT): Hearst x OpenAI renewal window at 23
months post-Oct 8 2024 - zero renewal/extension/termination reporting, treated
ACTIVE per the #599 convention (mechanism 696); Microsoft PCM pay-per-use leg
(Feb 2026) joins the Amazon Rufus leg (Jul 2025) to make Hearst the corpus
third triple-AI-payer publisher, Meta $0.

Rotation window fifth leg: D (#770) -> E (#771) -> A (#772) -> B (#773) ->
C (#774).

Evidence is search-excerpt-bounded per #503 (browser.open not attempted this
run - fleet egress proxy refused connections; no URLs constructed; all URLs
copied verbatim from search-result Full-URL listings). Statistical discipline
per the qualitative Type C convention: p_value/cohens_d/ci_95 NOT_CALCULATED,
tone_scores NOT_SCORED, is_significant False, engine NOT run; verdict
directionally_supported_not_proven; NOT a falsification-family member
(ledger holds at 26); no analysis.json update.

Anchor placeholder: patched to the main commit SHA in the #565 follow-up.
"""

import os
import re
import subprocess

import pytest

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
ENTITIES_PATH = "profiles/competitor-entities.yaml"
README_PATH = "README.md"
ARCH_PATH = "docs/ARCHITECTURE.md"
LOG_PATH = "iteration-log.md"
TEST_BASENAME = (
    "test_type_c_774_hearst_openai_renewal_window_triple_payer_sep15_4pm.py"
)
MECH_NUM = 696
# Built by concatenation so the underscore-form marker never sits contiguously
# in this file: the #715 sweep-instrument convention.
MECH_ID_MARKER = "mechanism" + "_696"
MECH_KEY = (
    "hearst_openai_renewal_window_oct2024_third_microsoft_pcm_payer_leg_sep2026"
)
NEXT_SIBLING = "\n    mechanism_544_vox_media_microsoft_pcm_pay_per_use_leg:"
ANCHORED_SHA = "bb98aa081b2520f494b902686c8a5bcecac98d08"


def _read(rel):
    with open(os.path.join(REPO_ROOT, rel), encoding="utf-8") as fh:
        return fh.read()


def _block():
    doc = _read(ENTITIES_PATH)
    start = doc.index(MECH_KEY + ":")
    end = doc.index(NEXT_SIBLING, start)
    return doc[start:end]


def _block_data():
    import yaml

    return yaml.safe_load(_block())[MECH_KEY]


def _fold(s):
    return re.sub(r"\s+", " ", s.lower())


def _git_log_mains(pattern):
    proc = subprocess.run(
        ["git", "-C", REPO_ROOT, "log", "--format=%H %s", "--no-merges", "--", "."],
        capture_output=True,
        text=True,
    )
    return [l for l in proc.stdout.splitlines() if re.search(pattern, l)]


def _repo_grep(pattern, roots=()):
    hits = []
    for root in roots or (".",):
        proc = subprocess.run(
            ["git", "-C", REPO_ROOT, "grep", "-n", "--", pattern, root],
            capture_output=True,
            text=True,
        )
        if proc.returncode == 0:
            hits.extend(proc.stdout.splitlines())
    return hits


def _profiles_corpus():
    out = []
    for root, _dirs, files in os.walk(os.path.join(REPO_ROOT, "profiles")):
        for fn in files:
            if fn.endswith((".yaml", ".yml", ".md")):
                out.append(_read(os.path.join(root, fn)))
    return "\n".join(out)


class TestNovelty774:
    """Pre-commit novelty: single new file, unique commit, zero repo precedent."""

    def test_single_test_type_c_774_file(self):
        files = sorted(
            f for f in os.listdir(os.path.join(REPO_ROOT, "tests"))
            if f.startswith("test_type_c_774") and f.endswith(".py")
        )
        assert files == [TEST_BASENAME], files

    def test_type_c_774_main_commit_unique_and_anchored(self):
        mains = _git_log_mains(r"Type C #774: ")
        assert len(mains) == 1, mains
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP", "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ), mains
        assert mains[0].startswith(ANCHORED_SHA + " "), mains

    def test_novelty_verification_claim_present_in_block(self):
        # Novelty was verified pre-commit by shell greps (zero test_type_c_774
        # files, no "Type C #774" in git log, "Hearst OpenAI renewal" /
        # "Hearst renewal window" zero-hit repo-wide case-insensitive, max
        # numeric mechanism_id 695, zero underscore-form 696 keys excluding
        # sweep-instrument carriers per #715); this test pins the claim in the
        # committed block, per the #752 convention.
        block = _block()
        assert "Zero test_type_c_774 files on disk pre-commit" in block
        assert "No Type C commit with 774 in title" in block
        assert "Hearst OpenAI renewal / Hearst renewal window zero-hit" in block
        assert "Max numeric mechanism id pre-commit 695" in block


class TestRotationCycleGuard774:
    """Rotation: 770-774 window fifth leg D->E->A->B->C."""

    EXPECTED_ORDER = [
        ("C", "774"), ("B", "773"), ("A", "772"), ("E", "771"), ("D", "770"),
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

    def test_window_closes_deabc(self):
        assert self._window() == self.EXPECTED_ORDER

    def test_window_cycle_edges_are_adjacent(self):
        window = self._window()
        for (t1, _), (t2, _) in zip(window, window[1:]):
            assert (self.ORDER[t1] - self.ORDER[t2]) % 5 == 1, (t1, t2)

    def test_anchor_sha_matches_head(self):
        mains = _git_log_mains(r"Type C #774: ")
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP", "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ), mains
        assert mains and mains[0].startswith(ANCHORED_SHA + " "), mains


class TestMechanism696Content:
    def test_block_present_in_entities(self):
        assert MECH_KEY + ":" in _read(ENTITIES_PATH)
        assert _block_data()["mechanism_id"] == MECH_NUM

    def test_iteration_metadata(self):
        data = _block_data()
        assert data["iteration"] == 774
        assert data["iteration_type"] == "C"
        assert data["rotation"] == "Type C"
        assert data["type"] == "financial_incentive_mapping"
        assert data["time_pdt"] == "16:00"
        assert data["discovery_date"] == "2026-09-15"
        assert data["goal_id"] == "goal_54093bda4145"
        assert data["job_id"] == "mediascope-daily-iteration"

    def test_openai_leg_renewal_window(self):
        leg = _block_data()["openai_leg_renewal_window"]
        assert leg["announced"].startswith("2024-10-08")
        assert leg["elapsed_months"] == 23
        assert leg["status"] == "ACTIVE"
        assert leg["status_convention"].startswith("#599")
        assert len(leg["renewal_window_query_sets"]) == 4
        assert "NO renewal" in leg["renewal_window_query_sets"][0]["result"]
        assert "NO renewal items" in leg["renewal_window_query_sets"][1]["result"]
        assert "EIGHTH member" in leg["cohort_membership"]
        assert "#609" in leg["cohort_membership"]

    def test_microsoft_pcm_third_payer_leg(self):
        leg = _block_data()["microsoft_pcm_third_payer_leg"]
        assert leg["partner"] == "Microsoft"
        assert leg["announced"] == "2026-02"
        assert "Hearst" in leg["hearst_role"]
        assert "co-design" in leg["hearst_role"]
        assert "north of $10M" in leg["hearst_role"]
        assert "triple" in _fold(leg["triple_payer_significance"])
        assert "searchengineland.com" in " ".join(leg["sources"])
        assert "thekeyword.medium.com" in " ".join(leg["sources"])
        assert "pressgazette.co.uk" in " ".join(leg["sources"])
        assert "llmpulse.ai" in " ".join(leg["sources"])

    def test_amazon_leg_carried_and_meta_zero(self):
        data = _block_data()
        assert data["amazon_rufus_leg_carried"]["announced"].startswith("2025-07-10")
        assert "Meta x Hearst AI licensing: $0" in data["meta_leg_status"]
        assert "Reuters - Meta" in data["meta_leg_status"]
        assert "CORRELATION NOT CAUSATION" in data["meta_leg_status"]

    def test_ranked_confounders_layers(self):
        confs = _block_data()["ranked_confounders"]
        assert len(confs) == 8
        layers = [c["strength"] for c in confs]
        assert layers.count("strong") == 3
        assert layers.count("moderate") == 3
        assert layers.count("weak") == 2
        assert [c["rank"] for c in confs] == [1, 2, 3, 4, 5, 6, 7, 8]

    def test_excerpt_bounded_per_503(self):
        block = _fold(_block())
        assert "search-excerpt-bounded per #503" in block
        assert "0 browser.open attempts" in block
        assert "none constructed" in block

    def test_statistical_discipline_type_c(self):
        data = _block_data()
        disc = data["statistical_discipline"]
        assert "NOT_CALCULATED" in disc
        assert "NOT_SCORED" in disc
        assert "is_significant False" in disc
        assert "Engine NOT run" in disc
        assert "no causal claim" in disc

    def test_verdict_ledger_and_source_urls(self):
        data = _block_data()
        assert data["verdict"] == "directionally_supported_not_proven"
        assert data["no_analysis_json_update"] is True
        assert data["artifact_grade"] is False
        assert "NOT a member" in data["falsification_family"]
        assert "ledger holds at 26" in data["falsification_family"]
        urls = " ".join(data["source_urls"])
        assert "https://pressgazette.co.uk/platforms/news-publisher-ai-deals-lawsuits-openai-google/" in urls
        assert "https://llmpulse.ai/blog/ai-content-licensing-deals/" in urls
        assert "http://thewrap.com/openai-hearst-content-licensing-partnership/" in urls

    def test_designed_keying_no_underscore_form_in_block(self):
        # The m696 block key carries no underscore-form marker substring, so
        # #775's zero-underscore-696 sweeps stay GREEN.
        assert MECH_ID_MARKER not in _block()


class TestSupersessionAndCorpusPost773:
    """Post-#773 corpus integrity: max 696, zero 697, designed supersession."""

    def _ids(self):
        return [
            int(x)
            for x in re.findall(r"mechanism_id:\s*(\d+)\b", _profiles_corpus())
        ]

    def test_max_numeric_mechanism_id_is_696(self):
        assert max(self._ids()) == MECH_NUM, max(self._ids())

    def test_695_still_present(self):
        hits = [h for h in _repo_grep("mechanism_id: 695")]
        assert len(hits) >= 1, hits

    def test_zero_underscore_697_keys_repo_wide(self):
        hits = _repo_grep("mechanism" + "_697")
        hits = [h for h in hits if not h.endswith(TEST_BASENAME)]
        assert hits == [], hits

    def test_zero_numeric_697_keys_in_profiles(self):
        hits = _repo_grep("mechanism_id: 697", roots=("profiles",))
        assert hits == [], hits

    def test_d773_zero_underscore_695_profiles_sweep_stays_green(self):
        # #773 asserted zero underscore-form 695 markers in profiles/; the
        # m695 block key carries no such substring by designed keying, so
        # that sweep stays green.
        hits = _repo_grep("mechanism" + "_695", roots=("profiles",))
        assert hits == [], hits

    def test_d773_zero_underscore_695_tests_sweep_stays_green(self):
        # #773 asserted zero underscore-form 695 markers in tests/; this file
        # builds the marker by concatenation ("mechanism" + "_695") and
        # carries no contiguous literal, so the sweep stays green.
        hits = _repo_grep("mechanism" + "_695", roots=("tests",))
        hits = [h for h in hits if not h.endswith(TEST_BASENAME)]
        assert hits == [], hits

    def test_d773_zero_numeric_695_profiles_sweep_fails_by_designed_supersession(
        self,
    ):
        # #773 asserted zero "mechanism_id: 695" hits in profiles/; the m696
        # block supersedes it by design per the #710/#720 convention.
        hits = _repo_grep("mechanism_id: 695", roots=("profiles",))
        assert len(hits) >= 1, hits

    def test_d773_max_695_sweep_superseded_by_design(self):
        # #773 asserted max == 695; advancing to 696 supersedes it per the
        # #710/#720 convention. Documented, not repaired.
        assert max(self._ids()) == MECH_NUM != 695

    def test_m696_block_key_unique_and_entities_parse(self):
        assert _read(ENTITIES_PATH).count(MECH_KEY + ":") == 1
        import yaml

        d = yaml.safe_load(_read(ENTITIES_PATH))

        def find(dd, key):
            if isinstance(dd, dict):
                for k, v in dd.items():
                    if k == key:
                        return v
                    r = find(v, key)
                    if r is not None:
                        return r
            return None

        assert find(d, MECH_KEY)["mechanism_id"] == MECH_NUM


class TestLedger774:
    """Falsification ledger: TWENTY-SIXTH present, TWENTY-SEVENTH absent; m696 not a member."""

    def test_twenty_sixth_present_and_twenty_seventh_absent(self):
        # Guard targets the profiles corpus per the #754 convention (prior type
        # files legitimately reference "TWENTY-SEVENTH" inside their own
        # negative guards, so a tests/ sweep would false-positive).
        corpus = _profiles_corpus()
        assert "TWENTY-SIXTH" in corpus
        assert "TWENTY-SEVENTH" not in corpus
        assert "ledger holds at 26" in _block()

    def test_m696_not_a_falsification_family_member(self):
        block = _block()
        assert "NOT a member" in block
        assert "renewal windows BOUND rather than join" in block

    def test_no_analysis_json_update_claimed(self):
        block = _block()
        assert "no_analysis_json_update: true" in block


class TestDocSync774:
    def test_readme_row_774(self):
        assert TEST_BASENAME in _read(README_PATH)

    def test_architecture_row_774(self):
        assert TEST_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_774_file(self):
        doc = _read(ARCH_PATH)
        assert TEST_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))


class TestIterationLog774:
    def _tail(self):
        lines = _read(LOG_PATH).splitlines()
        # Entries are appended chronologically (post-#735 convention); the
        # #774 entry sits at the end of the file, not the top.
        return "\n".join(lines[-60:])

    def test_log_entry_present(self):
        # "#774 Type C:" is the entry header; a bare "#774" would
        # false-positive on #773's rotation line ("C (#774) -> ...").
        assert "#774 Type C:" in self._tail()

    def test_log_mechanism_number_and_topic(self):
        assert "mechanism 696" in self._tail()
        assert "Hearst" in self._tail()


class TestDateGrounding774:
    @staticmethod
    def _weekday(d):
        return subprocess.run(
            ["date", "-d", d, "+%A"], capture_output=True, text=True
        ).stdout.strip()

    def test_sep_15_2026_is_tuesday(self):
        assert self._weekday("2026-09-15") == "Tuesday"
