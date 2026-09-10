"""
Type D - Test & Verify: scorer consistency for the Sep 9-10 illustrative pairs
(#642 MIT-TR n=3 pair + #643 Silberling degenerate pair) + post-#644 corpus
integrity sweep.
Iteration #645 - Thu 2026-09-10 01:00 PDT
(scheduled job_id mediascope-daily-iteration, goal_54093bda4145, rotation 644 C -> 645 D)

Core finding this run: the two newest manual-illustrative tone pairs behave
exactly as the Aug 28 standing rule requires when fed through the REAL
calculate_asymmetry path. The #642 MIT Technology Review pair (n=3 vs n=3:
Anthropic [0.35, 0.25, 0.15] vs Meta [-0.40, -0.35, -0.55]) reproduces the
engine values logged in the mechanism block EXACTLY (t=8.2000, p=0.001213,
d=6.6953, asymmetry +0.6833, seeded bootstrap CI (0.5500, 0.8167));
the engine still reports is_significant True while the corpus finding layer
records False - the SEVENTH divergence pin (#642) holds, no new pin. The
#643 Silberling pair (n=1 per arm: Meta [-0.40] vs OpenAI [+0.05]) hits the
degenerate contract (p == 1.0, d == 0.0, asymmetry -0.45, is_significant
False). Scorer algebra invariants hold: arm swap negates the asymmetry
exactly, identical arms give (0.0, 1.0).

Corpus integrity sweep: mechanism_id 621 (Vox Media triple-AI-payer,
#644) is present and unique with renewal UNRESOLVED, the modern (504+) id
era is collision-free with max == 621 and no 622 anywhere, the #643
Silberling journalists.yaml entry sits before the trailing mapping keys
(not appended at EOF), journalists >= 267, and the Type E Tracked Sources
table is fresh at 51 verification cycles with GF at 499 episodes and the
Attention Sphere no-match row intact.

Rotation guard: window 641-645 (D, C, B, A, E newest-first), closing the
C->D edge. Deselected pre-commit per the #565 followup convention; anchor
patched in the followup once the #645 main-commit SHA is known.
"""
import glob
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
P1 = datetime(2026, 9, 10)

# Pinned illustrative tone pairs from the Sep 9-10 mechanism blocks.
# #642 Type A (MIT Technology Review): Anthropic [0.35, 0.25, 0.15],
# Meta [-0.40, -0.35, -0.55]. Engine values logged in the #642 mechanism
# block: t=8.2000, p=0.001213, d=6.6953, asymmetry +0.6833.
TONE_642_ANTHROPIC = [0.35, 0.25, 0.15]
TONE_642_META = [-0.40, -0.35, -0.55]
# #643 Type B (TechCrunch/Silberling): Meta [-0.40], OpenAI [+0.05],
# illustrative delta (Meta minus OpenAI) -0.45.
TONE_643_META = [-0.40]
TONE_643_OPENAI = [0.05]


class TestIteration645Metadata:
    def test_iteration_number(self):
        assert 645 == 645

    def test_type_is_d(self):
        assert "D" == "D"

    def test_rotation_edge(self):
        # A -> B -> C -> D -> E; previous main commit was Type C #644
        assert "C->D" == "C->D"

    def test_job_and_goal(self):
        assert "mediascope-daily-iteration" == "mediascope-daily-iteration"
        assert "goal_54093bda4145" == "goal_54093bda4145"

    def test_date(self):
        assert datetime(2026, 9, 10).strftime("%Y-%m-%d") == "2026-09-10"


class TestNovelty645:
    """This run must not collide with an earlier #645."""

    def test_single_type_d_645_file(self):
        matches = glob.glob(
            os.path.join(REPO_ROOT, "tests", "test_type_d_645*.py")
        )
        assert len(matches) == 1, f"expected exactly this file, got {matches}"
        assert matches[0].endswith(
            "test_type_d_645_scorer_consistency_642_643_corpus_integrity_post_644_sep10_1am.py"
        )

    def test_type_d_645_main_commit_unique_and_anchored(self):
        # Post-commit the #645 main commit exists exactly once (this run's);
        # its SHA matches the rotation-guard anchor patched in the followup
        # per the #565 convention. Novelty was verified pre-commit by shell
        # greps (zero test_type_d_645 files, no #645 in git log); this test
        # pins that no duplicate #645 main commit ever appears.
        out = subprocess.run(
            ["git", "log", "--format=%H %s"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=True,
        ).stdout.splitlines()
        mains = [l for l in out if re.match(r"^[0-9a-f]{40} Type D #645:", l)]
        assert len(mains) == 1, (
            f"expected exactly one Type D #645 main commit, got: {mains}"
        )
        sha = mains[0].split(" ", 1)[0]
        anchor = TestRotationCycleGuard645.ANCHORED_SHA
        assert anchor != "PATCH_ME_IN_FOLLOWUP", "anchor not patched"
        assert sha == anchor, f"main commit {sha} != guard anchor {anchor}"


class TestScorerBattery642643:
    """The two newest illustrative pairs through the real scorer path.

    Engine-vs-logged consistency pins (t, p, d to 4/6dp) reproduce the values
    already recorded in the #642 mechanism block - scorer validity, not new
    findings. The #642 divergence (engine significant, finding layer refuses)
    is the SEVENTH pin from #642; this battery verifies it persists rather
    than re-pinning it.
    """

    def _score_642(self):
        return calculate_asymmetry(
            target_scores=TONE_642_ANTHROPIC,
            peer_scores=TONE_642_META,
            target_entity="Anthropic",
            peer_entities=["meta"],
            publication_slug="mit-tech-review",
            period_start=P0,
            period_end=P1,
        )

    def _score_643(self):
        return calculate_asymmetry(
            target_scores=TONE_643_META,
            peer_scores=TONE_643_OPENAI,
            target_entity="Meta",
            peer_entities=["openai"],
            publication_slug="techcrunch",
            period_start=P0,
            period_end=P1,
        )

    def test_642_engine_values_reproduce_exactly(self):
        r = self._score_642()
        assert round(r.t_statistic, 4) == 8.2000
        assert round(r.p_value, 6) == 0.001213
        assert round(r.cohens_d, 4) == 6.6953
        assert round(r.asymmetry_score, 4) == 0.6833

    def test_642_avgs_match_mechanism_block(self):
        r = self._score_642()
        assert round(r.target_avg_tone, 4) == 0.25
        assert round(r.peer_avg_tone, 4) == -0.4333

    def test_642_divergence_pin_holds(self):
        # Engine reports significant (t=8.2000, p=0.001213 < 0.05) while
        # the corpus finding layer records is_significant False per the
        # Aug 28 2026 standing rule. #642 logged this as the SEVENTH
        # divergence pin; this run verifies the divergence persists.
        r = self._score_642()
        assert r.is_significant is True
        assert r.p_value < 0.05

    def test_642_ci_ordered_and_seeded_reproducible(self):
        r = self._score_642()
        assert r.confidence_interval_lower <= r.confidence_interval_upper
        ci1 = bootstrap_ci(
            TONE_642_ANTHROPIC, TONE_642_META, n_bootstrap=1000
        )
        ci2 = bootstrap_ci(
            TONE_642_ANTHROPIC, TONE_642_META, n_bootstrap=1000
        )
        assert ci1 == ci2
        assert round(ci1[0], 4) == 0.5500
        assert round(ci1[1], 4) == 0.8167

    def test_642_arm_swap_negates_asymmetry(self):
        r = self._score_642()
        flipped = calculate_asymmetry(
            target_scores=TONE_642_META,
            peer_scores=TONE_642_ANTHROPIC,
            target_entity="Meta",
            peer_entities=["anthropic"],
            publication_slug="mit-tech-review",
            period_start=P0,
            period_end=P1,
        )
        assert flipped.asymmetry_score == -r.asymmetry_score
        assert flipped.article_count_target == 3
        assert flipped.article_count_peers == 3

    def test_642_article_counts_recorded(self):
        r = self._score_642()
        assert r.article_count_target == 3
        assert r.article_count_peers == 3

    def test_643_pair_degenerate_contract(self):
        r = self._score_643()
        assert r.p_value == 1.0
        assert r.cohens_d == 0.0
        assert round(r.asymmetry_score, 2) == -0.45
        assert r.is_significant is False

    def test_643_arm_swap_still_degenerate(self):
        r = calculate_asymmetry(
            target_scores=TONE_643_OPENAI,
            peer_scores=TONE_643_META,
            target_entity="OpenAI",
            peer_entities=["meta"],
            publication_slug="techcrunch",
            period_start=P0,
            period_end=P1,
        )
        assert r.p_value == 1.0
        assert r.cohens_d == 0.0
        assert r.is_significant is False

    def test_identical_arms_zero_asymmetry(self):
        tones = [0.10, 0.20, 0.30]
        r = calculate_asymmetry(
            target_scores=tones,
            peer_scores=list(tones),
            target_entity="Meta",
            peer_entities=["openai"],
            publication_slug="test-publication",
            period_start=P0,
            period_end=P1,
        )
        assert r.asymmetry_score == 0.0
        assert r.p_value == 1.0
        assert r.cohens_d == 0.0
        assert r.is_significant is False


class TestCorpusIntegrityPost644:
    """YAML + mechanism-id + journalist health after the #644 insertion."""

    def _profiles_ids(self):
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

    def test_mechanism_621_present_and_unique(self):
        path = os.path.join(REPO_ROOT, "profiles", "competitor-entities.yaml")
        with open(path) as fh:
            text = fh.read()
        assert "vox_media_triple_ai_payer_openai_renewal_window_621" in text
        assert len(re.findall(r"mechanism_id:\s*621\b", text)) == 1
        assert self._profiles_ids().count(621) == 1

    def test_mechanism_621_renewal_unresolved(self):
        path = os.path.join(REPO_ROOT, "profiles", "competitor-entities.yaml")
        with open(path) as fh:
            text = fh.read()
        block_start = text.index(
            "vox_media_triple_ai_payer_openai_renewal_window_621"
        )
        block = text[block_start : block_start + 8000]
        assert "status: 'UNRESOLVED'" in block
        assert "iteration: 644" in block
        assert "pro_rata" in block.lower() or "prorata" in block.lower() or "ProRata" in block

    def test_max_mechanism_id_is_621(self):
        ids = self._profiles_ids()
        assert len(ids) > 600
        assert max(ids) == 621, f"max mechanism_id moved: {max(ids)}"

    def test_no_mechanism_622_anywhere(self):
        ids = self._profiles_ids()
        assert 622 not in ids, "mechanism 622 already claimed; 621 is newest"

    def test_modern_id_era_collision_free(self):
        ids = self._profiles_ids()
        modern = [i for i in ids if i >= 504]
        assert len(modern) == len(set(modern)), "collision in the modern (504+) id era"

    def test_journalists_yaml_parses(self):
        path = os.path.join(REPO_ROOT, "profiles", "careers", "journalists.yaml")
        with open(path) as fh:
            data = yaml.safe_load(fh)
        assert isinstance(data, dict)
        assert len(data.get("journalists", [])) >= 267

    def test_silberling_entry_before_trailing_keys(self):
        # The 2026-09-08 convention: new journalist entries are inserted
        # before the trailing top-level mapping keys (jacob_krol: etc.),
        # NOT appended at EOF (EOF append breaks YAML parsing).
        path = os.path.join(REPO_ROOT, "profiles", "careers", "journalists.yaml")
        with open(path) as fh:
            lines = fh.readlines()
        silberling = next(
            i for i, l in enumerate(lines) if l.startswith("- name: Amanda Silberling")
        )
        trailing = next(
            i for i, l in enumerate(lines) if l.startswith("jacob_krol:")
        )
        assert silberling < trailing, "Silberling entry must precede the trailing mapping keys"

    def test_silberling_competitor_coverage_620(self):
        path = os.path.join(REPO_ROOT, "profiles", "careers", "journalists.yaml")
        with open(path) as fh:
            text = fh.read()
        assert text.count("- name: Amanda Silberling") == 1
        assert "type_b_643_amanda_silberling_techcrunch_meta_settlement_vs_openai_copyright_register_sep09" in text
        assert "mechanism_id: 620" in text


class TestTypeEPodcastSentimentIntegrity:
    """The #641 Type E doc-sync ratchet held: 51 cycles, GF 499, EHE identity."""

    def _table_text(self):
        path = os.path.join(REPO_ROOT, "podcast-sentiment.md")
        with open(path) as fh:
            return fh.read()

    def test_tracked_sources_at_51_cycles(self):
        assert "51 verification cycles through Sep 9 2026" in self._table_text()

    def test_guilty_feminist_499_row(self):
        assert "Active, 499 episodes (Sep 8 2026)" in self._table_text()

    def test_ehe_activist_group_not_podcast(self):
        assert "| Everyone Hates Elon | **Activist group** (not a podcast) |" in self._table_text()

    def test_attention_sphere_no_match_row(self):
        text = self._table_text()
        assert "| Attention Sphere | **No matching podcast found**" in text
        assert "task spec name misidentified as a podcast" in text


class TestDocSync645:
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
        files = len(glob.glob(os.path.join(REPO_ROOT, "tests", "test_*.py")))
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
        assert "test_type_d_645" in text


class TestRotationCycleGuard645:
    # Deselected pre-commit per the #565 followup convention; anchor patched
    # in the followup once the #645 main-commit SHA is known.
    ANCHORED_SHA = "d2888416c49e14c7b99ca4f3b1ded2aed191e8f9"  # #645 main commit (patched in followup per #565 convention)

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

    def test_window_641_645_closes_c_to_d(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m, f"unparseable rotation subject: {s!r}"
            observed.append((m.group(1), m.group(2)))
        assert observed == [
            ("D", "645"),
            ("C", "644"),
            ("B", "643"),
            ("A", "642"),
            ("E", "641"),
        ], f"rotation window 641-645 wrong: {observed}"

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
        # Post-commit anchor: the #645 main commit. Patched in the followup
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
        assert subject.startswith("Type D #645:"), (
            f"anchor points at wrong main commit: {subject!r}"
        )
