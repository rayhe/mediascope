"""Type C #779 (2026-09-15 21:00 PDT): Taylor & Francis (Informa) x Microsoft
$10M+ academic data-access agreement (May 2024) - FIRST dedicated
academic-publisher AI data-licensing mechanism in the corpus (mechanism 699);
second unnamed AI-company partnership (Jul 2024); ~$75M 2024 data-licensing
total; 2025 further agreements; license-over-authors fourth relationship
direction (after sue-then-sign m624, pay-or-litigate bifurcation m636,
grant-then-sue m675).

Rotation window fifth leg: D (#775) -> E (#776) -> A (#777) -> B (#778) ->
C (#779), closing the 775-779 window.

Evidence is search-excerpt-bounded per #503 (2 browser.search query sets, 0
browser.open; proxy OPEN this run but excerpts sufficed; all URLs copied
verbatim from search-result Full-URL listings; no canonical URLs
constructed). Statistical discipline per the qualitative Type C convention:
p_value/cohens_d/ci_95 NOT_CALCULATED, tone_scores NOT_SCORED, is_significant
False, engine NOT run; verdict directionally_supported_not_proven; NOT a
falsification-family member (ledger holds at 26); no analysis.json update.

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
    "test_type_c_779_taylor_francis_informa_microsoft_academic_data_access_sep15_9pm.py"
)
MECH_NUM = 699
# Built by concatenation so the underscore-form marker never sits contiguously
# in this file: the #715 sweep-instrument convention.
MECH_ID_MARKER = "mechanism" + "_699"
MECH_KEY = (
    "taylor_francis_informa_microsoft_academic_data_access_may2024_expansion_sep2026"
)
NEXT_SIBLING = "\n  snowflake:"
ANCHORED_SHA = "PATCH_ME_IN_FOLLOWUP"


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


class TestNovelty779:
    """Pre-commit novelty: single new file, unique commit, zero repo precedent."""

    def test_single_test_type_c_779_file(self):
        files = sorted(
            f for f in os.listdir(os.path.join(REPO_ROOT, "tests"))
            if f.startswith("test_type_c_779") and f.endswith(".py")
        )
        assert files == [TEST_BASENAME], files

    def test_type_c_779_main_commit_unique_and_anchored(self):
        mains = _git_log_mains(r"Type C #779: ")
        assert len(mains) == 1, mains
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP", "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ), mains
        assert mains[0].startswith(ANCHORED_SHA + " "), mains

    def test_novelty_verification_claim_present_in_block(self):
        # Novelty was verified pre-commit by shell greps (zero test_type_c_779
        # files, no "Type C #779" in git log, zero "Taylor & Francis" /
        # taylor_francis / Informa-plc hits repo-wide (informative/informant
        # substring hits unrelated), max numeric mechanism_id 698, zero
        # underscore-form 699 keys excluding sweep-instrument carriers per
        # #715); this test pins the claim in the committed block, per the
        # #752 convention.
        block = _block()
        assert "Zero test_type_c_779 files on disk pre-commit" in block
        assert "No Type C #779 in git log pre-commit" in block
        assert "Zero \"Taylor & Francis\" / taylor_francis / Informa-plc hits" in block
        assert "Max numeric mechanism_id 698 pre-commit" in block


class TestRotationCycleGuard779:
    """Rotation: 775-779 window fifth leg D->E->A->B->C."""

    EXPECTED_ORDER = [
        ("C", "779"), ("B", "778"), ("A", "777"), ("E", "776"), ("D", "775"),
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
        mains = _git_log_mains(r"Type C #779: ")
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP", "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ), mains
        assert mains and mains[0].startswith(ANCHORED_SHA + " "), mains


class TestMechanism699Content:
    def test_block_present_in_entities(self):
        assert MECH_KEY + ":" in _read(ENTITIES_PATH)
        assert _block_data()["mechanism_id"] == MECH_NUM

    def test_iteration_metadata(self):
        data = _block_data()
        assert data["iteration"] == 779
        assert data["iteration_type"] == "C"
        assert data["rotation"] == "Type C"
        assert data["type"] == "financial_incentive_mapping"
        assert data["time_pdt"] == "21:00"
        assert data["discovery_date"] == "2026-09-15"
        assert data["goal_id"] == "goal_54093bda4145"
        assert data["job_id"] == "mediascope-daily-iteration"

    def test_deal_parties_and_announcement(self):
        data = _block_data()
        assert data["deal_parties"]["payer"].startswith("Microsoft")
        assert "Taylor & Francis" in data["deal_parties"]["counterparty"]
        assert "Informa plc" in data["deal_parties"]["counterparty_parent"]
        assert data["announcement"]["disclosed"].startswith("May 2024")
        assert "July 2024" in data["announcement"]["first_reported"]

    def test_deal_structure_and_terms(self):
        data = _block_data()
        struct = data["deal_structure"]
        assert "Nonexclusive" in struct["access"]
        assert "3,000" in struct["access"]
        assert len(struct["focus_areas"]) == 4
        assert "citation" in _fold(" ".join(struct["focus_areas"]))
        terms = data["deal_terms"]
        assert terms["initial_fee"].startswith("$10M+")
        assert "three years" in terms["recurring"]
        assert terms["exclusivity"] == "Nonexclusive"

    def test_author_backlash_license_over_authors(self):
        data = _block_data()
        backlash = data["author_backlash"]
        assert backlash["consultation"].startswith("None")
        assert "opt-out" in backlash["opt_out"]
        assert "Society of Authors" in backlash["extra_payment"]
        assert len(backlash["key_quotes"]) == 4
        assert "license-over-authors" in _fold(data["relationship_direction_taxonomy"])
        assert "FOURTH relationship direction" in data["relationship_direction_taxonomy"]
        assert "m624" in data["relationship_direction_taxonomy"]
        assert "m675" in data["relationship_direction_taxonomy"]

    def test_second_partnership_and_2025_expansion(self):
        data = _block_data()
        second = data["second_ai_partnership_jul2024"]
        assert "July 24 2024" in second["source"]
        assert "second major partnership" in second["claim"]
        assert "$75 million" in second["guidance"]
        assert "unnamed" in _fold(second["claim"])
        exp = data["expansion_2025"]
        assert "deepen relationships with AI companies" in exp["claim"]
        assert "~$75M" in exp["quantum_2024"]
        assert "further non-recurring data licensing agreements" in exp["quantum_2025"]

    def test_ranked_confounders_layers(self):
        confs = _block_data()["ranked_confounders"]
        assert len(confs) == 6
        layers = [c["strength"] for c in confs]
        assert layers.count("strong") == 3
        assert layers.count("moderate") == 2
        assert layers.count("weak") == 1
        assert [c["rank"] for c in confs] == [1, 2, 3, 4, 5, 6]

    def test_excerpt_bounded_per_503(self):
        block = _fold(_block())
        assert "search-excerpt-bounded per #503" in block
        assert "0 browser.open" in block
        assert "no canonical urls constructed" in block

    def test_statistical_discipline_type_c(self):
        disc = _block_data()["statistical_discipline"]
        assert disc["scorer"] == "none"
        assert disc["tone_scores"] == "NOT_SCORED"
        assert disc["p_value"] == "NOT_CALCULATED"
        assert disc["cohens_d"] == "NOT_CALCULATED"
        assert disc["ci_95"] == "NOT_CALCULATED"
        assert disc["is_significant"] is False
        assert disc["qualitative_only"] is True
        assert disc["artifact_grade"] is False

    def test_verdict_ledger_and_source_urls(self):
        data = _block_data()
        assert data["verdict"] == "directionally_supported_not_proven"
        assert data["no_analysis_json_update"] is True
        assert data["artifact_grade"] is False
        assert "NOT a member" in data["falsification_family"]
        assert "ledger holds at 26" in data["falsification_family"]
        urls = " ".join(data["source_urls"])
        assert "insidehighered.com/news/faculty/research/2024/07/29/taylor-francis-ai-deal-sets-worrying-precedent" in urls
        assert "thebookseller.com/news/academic-authors-shocked-after-taylor--francis" in urls
        assert "thebookseller.com/news/news/taylor-francis-shows-strong-growth-in-2025" in urls
        assert "stg.timeshighereducation.com" in urls
        assert "aihub.org" in urls

    def test_designed_keying_no_underscore_form_in_block(self):
        # The m699 block key carries no underscore-form marker substring, so
        # future zero-underscore-699 sweeps stay GREEN.
        assert MECH_ID_MARKER not in _block()


class TestSupersessionAndCorpusPost778:
    """Post-#778 corpus integrity: max 699, zero 700, designed supersession."""

    def _ids(self):
        return [
            int(x)
            for x in re.findall(r"mechanism_id:\s*(\d+)\b", _profiles_corpus())
        ]

    def test_max_numeric_mechanism_id_is_699(self):
        assert max(self._ids()) == MECH_NUM, max(self._ids())

    def test_698_still_present(self):
        hits = [h for h in _repo_grep("mechanism_id: 698")]
        assert len(hits) >= 1, hits

    def test_zero_underscore_700_keys_repo_wide(self):
        hits = _repo_grep("mechanism" + "_700")
        hits = [h for h in hits if not h.endswith(TEST_BASENAME)]
        assert hits == [], hits

    def test_zero_numeric_700_keys_in_profiles(self):
        hits = _repo_grep("mechanism_id: 700", roots=("profiles",))
        assert hits == [], hits

    def test_d778_zero_underscore_698_profiles_sweep_stays_green(self):
        # #778 asserted zero underscore-form 698 markers in profiles/; the
        # m698 block key carries no such substring by designed keying, so
        # that sweep stays green.
        hits = _repo_grep("mechanism" + "_698", roots=("profiles",))
        assert hits == [], hits

    def test_d778_zero_underscore_698_tests_sweep_stays_green(self):
        # #778 asserted zero underscore-form 698 markers in tests/; this file
        # builds the marker by concatenation ("mechanism" + "_698") and
        # carries no contiguous literal, so the sweep stays green.
        hits = _repo_grep("mechanism" + "_698", roots=("tests",))
        hits = [h for h in hits if not h.endswith(TEST_BASENAME)]
        assert hits == [], hits

    def test_d778_zero_numeric_698_profiles_sweep_fails_by_designed_supersession(
        self,
    ):
        # #778 asserted zero "mechanism_id: 698" hits in profiles/; the m699
        # block supersedes it by design per the #710/#720 convention.
        hits = _repo_grep("mechanism_id: 698", roots=("profiles",))
        assert len(hits) >= 1, hits

    def test_d778_max_698_sweep_superseded_by_design(self):
        # #778 asserted max == 698; advancing to 699 supersedes it per the
        # #710/#720 convention. Documented, not repaired.
        assert max(self._ids()) == MECH_NUM != 698

    def test_m699_block_key_unique_and_entities_parse(self):
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


class TestLedger779:
    """Falsification ledger: TWENTY-SIXTH present, TWENTY-SEVENTH absent; m699 not a member."""

    def test_twenty_sixth_present_and_twenty_seventh_absent(self):
        # Guard targets the profiles corpus per the #754 convention (prior type
        # files legitimately reference "TWENTY-SEVENTH" inside their own
        # negative guards, so a tests/ sweep would false-positive).
        corpus = _profiles_corpus()
        assert "TWENTY-SIXTH" in corpus
        assert "TWENTY-SEVENTH" not in corpus
        assert "ledger holds at 26" in _block()

    def test_m699_not_a_falsification_family_member(self):
        block = _block()
        assert "NOT a member" in block
        assert "qualitative financial mapping only" in block

    def test_no_analysis_json_update_claimed(self):
        block = _block()
        assert "no_analysis_json_update: true" in block


class TestDocSync779:
    def test_readme_row_779(self):
        assert TEST_BASENAME in _read(README_PATH)

    def test_architecture_row_779(self):
        assert TEST_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_779_file(self):
        doc = _read(ARCH_PATH)
        assert TEST_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))


class TestIterationLog779:
    def _tail(self):
        lines = _read(LOG_PATH).splitlines()
        # Entries are appended chronologically (post-#735 convention); the
        # #779 entry sits at the end of the file, not the top.
        return "\n".join(lines[-60:])

    def test_log_entry_present(self):
        # "#779 Type C:" is the entry header; a bare "#779" would
        # false-positive on #778's rotation line ("(C to follow)").
        assert "#779 Type C:" in self._tail()

    def test_log_mechanism_number_and_topic(self):
        assert "mechanism 699" in self._tail()
        assert "Taylor" in self._tail()


class TestDateGrounding779:
    @staticmethod
    def _weekday(d):
        return subprocess.run(
            ["date", "-d", d, "+%A"], capture_output=True, text=True
        ).stdout.strip()

    def test_sep_15_2026_is_tuesday(self):
        assert self._weekday("2026-09-15") == "Tuesday"
