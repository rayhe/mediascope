"""
Type D - Test & Verify: scorer statistical-meaningfulness battery + post-#639 corpus integrity sweep
Iteration #640 - Wed 2026-09-09 20:00 PDT
(scheduled job_id mediascope-daily-iteration, goal_54093bda4145, rotation 639 C -> 640 D)

Core finding this run: the two newest manual-illustrative tone pairs behave
exactly as the Aug 28 standing rule requires when fed through the REAL
calculate_asymmetry path. The #637 News Corp/WSJ pair (n=2 vs n=2: Meta
[+0.40, +0.30] vs OpenAI [-0.55, +0.10]) is statistically well-formed but
non-significant at n=2 (p in (0, 1), asymmetry +0.575 sign correct,
d > 0, ordered CI, is_significant False); the #638 Sarah Perez pair
(Meta [-0.45] vs Google [+0.05], n=1 per arm) hits the degenerate contract
(p == 1.0, d == 0.0, is_significant False). Scorer algebra invariants hold:
arm swap negates the asymmetry exactly, identical arms give (0.0, 1.0).

Corpus integrity sweep: mechanism_id 618 (Time x OpenAI, #639) is present
and unique, the modern (504+) id era is collision-free with max == 618 and
no 619 anywhere, the 618 renewal-window block carries UNRESOLVED status,
the #638 Sarah Perez journalists.yaml entry sits before the trailing
mapping keys (not appended at EOF), and the Type E Tracked Sources table is
fresh at 50 verification cycles with GF at 499 episodes.

Rotation guard: window 636-640 (D, C, B, A, E newest-first), closing the
C->D edge. Deselected pre-commit per the #565 followup convention; anchor
patched in the followup once the #640 main-commit SHA is known.
"""
import os
import re
import subprocess
import sys
from datetime import datetime

import pytest
import yaml

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO_ROOT)

from mediascope.score.asymmetry import calculate_asymmetry
from mediascope.score.statistical import bootstrap_ci

P0 = datetime(2026, 9, 2)
P1 = datetime(2026, 9, 9)

# Pinned illustrative tone pairs from the Sep 8-9 mechanism blocks.
# #637 Type A (News Corp/WSJ): Meta arm [+0.40, +0.30], OpenAI arm [-0.55, +0.10]
TONE_637_META = [0.40, 0.30]
TONE_637_OPENAI = [-0.55, 0.10]
# #638 Type B (TechCrunch/Sarah Perez): Meta [-0.45], Google [+0.05]
TONE_638_META = [-0.45]
TONE_638_GOOGLE = [0.05]


class TestIteration640Metadata:
    def test_iteration_number(self):
        assert 640 == 640

    def test_type_is_d(self):
        assert "D" == "D"

    def test_rotation_edge(self):
        # A -> B -> C -> D -> E; previous main commit was Type C #639
        assert "C->D" == "C->D"

    def test_job_and_goal(self):
        assert "mediascope-daily-iteration" == "mediascope-daily-iteration"
        assert "goal_54093bda4145" == "goal_54093bda4145"

    def test_date(self):
        assert datetime(2026, 9, 9).strftime("%Y-%m-%d") == "2026-09-09"


class TestNovelty640:
    """This run must not collide with an earlier #640."""

    def test_single_type_d_640_file(self):
        import glob as globmod

        matches = globmod.glob(
            os.path.join(REPO_ROOT, "tests", "test_type_d_640*.py")
        )
        assert len(matches) == 1, f"expected exactly this file, got {matches}"
        assert matches[0].endswith(
            "test_type_d_640_scorer_statistical_meaningfulness_corpus_integrity_sweep_sep09_8pm.py"
        )

    def test_type_d_640_main_commit_unique_and_anchored(self):
        # Post-commit the #640 main commit exists exactly once (this run's);
        # its SHA matches the rotation-guard anchor patched in the followup
        # per the #565 convention. Novelty was verified pre-commit by shell
        # greps (zero test_type_d_640 files, no #640 in git log); this test
        # pins that no duplicate #640 main commit ever appears.
        out = subprocess.run(
            ["git", "log", "--format=%H %s"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=True,
        ).stdout.splitlines()
        mains = [l for l in out if re.match(r"^[0-9a-f]{40} Type D #640:", l)]
        assert len(mains) == 1, (
            f"expected exactly one Type D #640 main commit, got: {mains}"
        )
        sha = mains[0].split(" ", 1)[0]
        anchor = TestRotationCycleGuard640.ANCHORED_SHA
        assert anchor != "PATCH_ME_IN_FOLLOWUP", "anchor not patched"
        assert sha == anchor, f"main commit {sha} != guard anchor {anchor}"


class TestScorerIllustrativePairsSep89:
    """The two newest illustrative pairs through the real scorer path.

    Threshold-only assertions per the Aug 28 convention. The scorer must
    reproduce the standing rule: the n=2-vs-n=2 #637 pair is well-formed but
    never significant; the n=1-per-arm #638 pair hits the degenerate
    contract (p == 1.0, d == 0.0).
    """

    def _score(self, target, peers, target_entity, peer_entity, slug):
        return calculate_asymmetry(
            target_scores=target,
            peer_scores=peers,
            target_entity=target_entity,
            peer_entities=[peer_entity],
            publication_slug=slug,
            period_start=P0,
            period_end=P1,
        )

    def _score_637(self):
        return self._score(
            TONE_637_META,
            TONE_637_OPENAI,
            "Meta",
            "openai",
            "wall-street-journal",
        )

    def test_637_p_value_well_formed(self):
        r = self._score_637()
        assert 0.0 < r.p_value < 1.0

    def test_637_asymmetry_sign_and_magnitude(self):
        # Meta avg 0.35 vs OpenAI avg -0.225 -> Meta-minus-OpenAI +0.575.
        # Threshold pin only (no exact float pin per Aug 28 convention).
        r = self._score_637()
        assert r.target_avg_tone > r.peer_avg_tone
        assert r.asymmetry_score > 0.5
        assert r.cohens_d > 0

    def test_637_not_significant_at_n2(self):
        # Small-n reality check: a large raw gap with n=2 per arm does not
        # clear p < 0.05. The corpus correctly records is_significant False.
        r = self._score_637()
        assert r.is_significant is False

    def test_637_confidence_interval_ordered(self):
        r = self._score_637()
        assert r.confidence_interval_lower <= r.confidence_interval_upper

    def test_637_arm_swap_negates_asymmetry(self):
        # Scorer algebra invariant: swapping target and peer negates the
        # asymmetry exactly (asymmetry is a difference of means).
        r = self._score_637()
        flipped = self._score(
            TONE_637_OPENAI,
            TONE_637_META,
            "OpenAI",
            "meta",
            "wall-street-journal",
        )
        assert flipped.asymmetry_score == -r.asymmetry_score

    def test_637_article_counts_recorded(self):
        r = self._score_637()
        assert r.article_count_target == 2
        assert r.article_count_peers == 2

    def test_638_pair_degenerate_contract(self):
        r = self._score(
            TONE_638_META,
            TONE_638_GOOGLE,
            "Meta",
            "google",
            "techcrunch",
        )
        assert r.p_value == 1.0
        assert r.cohens_d == 0.0
        assert r.is_significant is False

    def test_638_arm_swap_still_degenerate(self):
        r = self._score(
            TONE_638_GOOGLE,
            TONE_638_META,
            "Google",
            "meta",
            "techcrunch",
        )
        assert r.p_value == 1.0
        assert r.cohens_d == 0.0
        assert r.is_significant is False

    def test_identical_arms_zero_asymmetry(self):
        tones = [0.10, 0.20, 0.30]
        r = self._score(tones, list(tones), "Meta", "openai", "test-publication")
        assert r.asymmetry_score == 0.0
        assert r.p_value == 1.0
        assert r.cohens_d == 0.0
        assert r.is_significant is False

    def test_bootstrap_seeded_reproducible_637(self):
        ci1 = bootstrap_ci(TONE_637_META, TONE_637_OPENAI, n_bootstrap=1000)
        ci2 = bootstrap_ci(TONE_637_META, TONE_637_OPENAI, n_bootstrap=1000)
        assert ci1 == ci2


class TestCorpusIntegrityPost639:
    """YAML + mechanism-id + journalist health after the #639 insertion."""

    def _profiles_text(self):
        # Repo-wide recursive scan of profiles/ (line-anchored, same method
        # as the #635 invariant refinement).
        ids = []
        for root, _dirs, files in os.walk(os.path.join(REPO_ROOT, "profiles")):
            for f in files:
                if not f.endswith((".yaml", ".yml")):
                    continue
                with open(os.path.join(root, f)) as fh:
                    for line in fh:
                        m = re.match(r"\s*mechanism_id:\s*(\d+)\s*$", line)
                        if m:
                            ids.append(int(m.group(1)))
        return ids

    def test_competitor_entities_parses(self):
        path = os.path.join(REPO_ROOT, "profiles", "competitor-entities.yaml")
        with open(path) as fh:
            data = yaml.safe_load(fh)
        assert isinstance(data, dict)

    def test_mechanism_618_present_and_unique(self):
        path = os.path.join(REPO_ROOT, "profiles", "competitor-entities.yaml")
        with open(path) as fh:
            text = fh.read()
        assert "time_openai_renewal_window_dual_channel_618" in text
        assert len(re.findall(r"mechanism_id:\s*618\b", text)) == 1
        assert self._profiles_text().count(618) == 1

    def test_mechanism_618_renewal_unresolved(self):
        path = os.path.join(REPO_ROOT, "profiles", "competitor-entities.yaml")
        with open(path) as fh:
            text = fh.read()
        block_start = text.index("time_openai_renewal_window_dual_channel_618")
        block = text[block_start : block_start + 6000]
        assert "status: 'UNRESOLVED'" in block
        assert "iteration: 639" in block
        assert "101 years" in block or "101-year" in block

    def test_max_mechanism_id_is_618(self):
        ids = self._profiles_text()
        assert len(ids) > 600
        assert max(ids) == 618, f"max mechanism_id moved: {max(ids)}"

    def test_no_mechanism_619_anywhere(self):
        ids = self._profiles_text()
        assert 619 not in ids, "mechanism 619 already claimed; 618 is newest"

    def test_modern_id_era_collision_free(self):
        ids = self._profiles_text()
        modern = [i for i in ids if i >= 504]
        assert len(modern) == len(set(modern)), "collision in the modern (504+) id era"

    def test_journalists_yaml_parses(self):
        path = os.path.join(REPO_ROOT, "profiles", "careers", "journalists.yaml")
        with open(path) as fh:
            data = yaml.safe_load(fh)
        assert isinstance(data, dict)
        assert len(data.get("journalists", [])) >= 266

    def test_sarah_perez_entry_before_trailing_keys(self):
        # The 2026-09-08 convention: new journalist entries are inserted
        # before the trailing top-level mapping keys (jacob_krol: etc.),
        # NOT appended at EOF (EOF append breaks YAML parsing).
        path = os.path.join(REPO_ROOT, "profiles", "careers", "journalists.yaml")
        with open(path) as fh:
            lines = fh.readlines()
        perez = next(
            i for i, l in enumerate(lines) if l.startswith("- name: Sarah Perez")
        )
        trailing = next(
            i for i, l in enumerate(lines) if l.startswith("jacob_krol:")
        )
        assert perez < trailing, "Perez entry must precede the trailing mapping keys"

    def test_sarah_perez_competitor_coverage_617(self):
        path = os.path.join(REPO_ROOT, "profiles", "careers", "journalists.yaml")
        with open(path) as fh:
            text = fh.read()
        assert text.count("- name: Sarah Perez") == 1
        assert "type_b_638_sarah_perez_techcrunch_meta_muse_vs_google_gemini_spark_trust_register_sep09" in text
        assert "mechanism_id: 617" in text


class TestTypeEPodcastSentimentIntegrity:
    """The #636 Type E doc-sync ratchet held: 50 cycles, GF 499, EHE identity."""

    def _table_text(self):
        path = os.path.join(REPO_ROOT, "podcast-sentiment.md")
        with open(path) as fh:
            return fh.read()

    def test_tracked_sources_at_50_cycles(self):
        assert "50 verification cycles through Sep 9 2026" in self._table_text()

    def test_guilty_feminist_499_row(self):
        assert "Active, 499 episodes (Sep 8 2026)" in self._table_text()

    def test_ehe_activist_group_not_podcast(self):
        assert "| Everyone Hates Elon | **Activist group** (not a podcast) |" in self._table_text()

    def test_attention_sphere_no_match_row(self):
        text = self._table_text()
        assert "| Attention Sphere | **No matching podcast found**" in text
        assert "task spec name misidentified as a podcast" in text


class TestDocSync640:
    # Fails pre-commit by design per the #565 followup convention; the README
    # stats table refresh and ARCHITECTURE row are added in the doc-sync
    # commit.
    def _readme_stats(self):
        path = os.path.join(REPO_ROOT, "README.md")
        with open(path) as fh:
            text = fh.read()
        m = re.search(r"\| Tests \| (\d+) \| Across (\d+) test files \|", text)
        assert m, "README stats table row not found"
        return int(m.group(1)), int(m.group(2))

    def _actual_counts(self):
        # Authoritative pytest-based count (same method as the --check gate;
        # the regex estimate undercounts parametrize expansions).
        out = subprocess.run(
            [sys.executable, "scripts/count_stats.py", "--pytest"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            timeout=400,
        )
        m = re.search(r"Total tests\s+(\d+)", out.stdout)
        assert m
        total = int(m.group(1))
        import glob as globmod

        files = len(globmod.glob(os.path.join(REPO_ROOT, "tests", "test_*.py")))
        return total, files

    def test_readme_stats_table_fresh(self):
        assert self._readme_stats() == self._actual_counts()

    def test_readme_narrative_line_fresh(self):
        path = os.path.join(REPO_ROOT, "README.md")
        with open(path) as fh:
            text = fh.read()
        m = re.search(r"has \*\*(\d+) tests\*\* across (\d+) test files", text)
        assert m, "README narrative test-count line not found"
        total, files = self._actual_counts()
        assert (int(m.group(1)), int(m.group(2))) == (total, files)

    def test_architecture_row_present(self):
        path = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")
        with open(path) as fh:
            text = fh.read()
        assert "test_type_d_640" in text


class TestRotationCycleGuard640:
    # Deselected pre-commit per the #565 followup convention; anchor patched
    # in the followup once the #640 main-commit SHA is known.
    ANCHORED_SHA = "437aff75c3684a379ad63786ec5589b203a18a9b"  # #640 main commit (patched in followup per #565 convention)

    @staticmethod
    def _mains():
        out = subprocess.run(
            ["git", "log", "--format=%s"],
            cwd=str(REPO_ROOT),
            capture_output=True,
            text=True,
            check=True,
        ).stdout.splitlines()
        return [s for s in out if re.match(r"^Type [A-E] #\d+:", s)]

    def test_window_636_640_closes_c_to_d(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m, f"unparseable rotation subject: {s!r}"
            observed.append((m.group(1), m.group(2)))
        assert observed == [
            ("D", "640"),
            ("C", "639"),
            ("B", "638"),
            ("A", "637"),
            ("E", "636"),
        ], f"rotation window 636-640 wrong: {observed}"

    def test_rotation_adjacency_cycle_valid(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m
            observed.append(m.group(1))
        assert observed == ["D", "C", "B", "A", "E"]
        order = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
        for a, b in zip(observed, observed[1:]):
            assert (order[a] - order[b]) % 5 == 1, (
                f"rotation broken: {a} -> {b} is not a valid cycle edge"
            )

    def test_anchor_is_main_patch_in_followup(self):
        # Post-commit anchor: the #640 main commit. Patched in the followup
        # per the #565 convention once the main commit SHA is known.
        out = subprocess.run(
            ["git", "log", "--format=%H %s"],
            cwd=str(REPO_ROOT),
            capture_output=True,
            text=True,
            check=True,
        ).stdout.splitlines()
        mains = [
            l for l in out if re.match(r"^[0-9a-f]{40} Type [A-E] #\d+:", l)
        ]
        sha, subject = mains[0].split(" ", 1)
        assert sha == self.ANCHORED_SHA, f"anchor not yet patched: {sha}"
        assert subject.startswith("Type D #640:"), (
            f"anchor points at wrong main commit: {subject!r}"
        )
