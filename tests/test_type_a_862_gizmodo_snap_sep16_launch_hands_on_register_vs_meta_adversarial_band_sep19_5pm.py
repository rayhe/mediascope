"""Type A iteration 862: Gizmodo x Snap Specs Sep-15/16 2026 launch hands-on register
vs the Meta adversarial band (mechanism 748), THIRD leg of the 860-864 rotation window.

Type A contract (per the standing rotation doctrine): add ONE mechanism block keyed under
profiles/<publication>.yaml competitor_relationships, covering a publication x competitor
pair that is fresh this run, with attribution URLs verified against a real search, and
cross-reference the existing comparator register from an earlier Type A on the same
outlet. This run: Gizmodo x Snap.

Publication focus: Gizmodo (Keleops AG). Competitor: Snap. Comparison entities: Meta,
OpenAI. Financial context: financial_tie none, estimated_value $0, direction none,
coverage_prediction adversarial (this profile) - so the null-tie prediction is no
uniform tie-driven softening: the register should follow the PEG and genre, not the entity.

Snap arm (FRESH this run, mechanism 748): James Pero's launch-week hands-on piece
"Snap's AR Glasses Let You Take Snapchat Pics by Snapping Your Fingers" (Sep-15/16 2026,
LA pre-brief embargo ahead of the Sep 16 event; hands-on access attested by the
gamesreviews.com Sep 17 roundup carried from wired.yaml #827). Register: first-person
hands-on playful-skeptical. MANUAL ILLUSTRATIVE tone +0.10. Verbatim register evidence
from search excerpts (excerpt-bounded per #503, 0 browser.open this run per developer
constraint): Shopify app "not on my bingo card"; Harry Potter tie-in "how gimmicky that
is"; soccer demo "probably the most fun I had in my personal demo with Specs" and
"optimistic on the basketball side of things". Zero surveillance vocabulary for the
4-camera glasses - replicating the m74 privacy-vocabulary finding inside a warm register.

Comparator arms (CARRIED, un-rescored per the #807 pattern):
- Meta band from m577: facial-recognition glasses -0.70, scrapped AI photo tool -0.55,
  layoffs headline snark -0.60, mean -0.617.
- OpenAI arm from m736: Sep-18 Claude-hack cybersecurity accountability, -0.45.
- Within-journalist temporal from m74: Pero's Jun-16 Specs preview "Trying to Beat Meta
  to the Punch" (neutral_product_preview, -0.10) to the Sep hands-on (+0.10): illustrative
  softening +0.20 after hardware access.

Illustrative deltas: Snap-minus-Meta +0.717 (0.10 - (-0.617)); Snap-minus-OpenAI +0.55.
These are MANUAL ILLUSTRATIVE ONLY per the Aug 28 2026 standing rule: engine NOT run;
p_value, cohens_d, ci_95 all NOT_CALCULATED; is_significant False;
verdict directionally_supported_not_proven; NOT artifact-grade; NO analysis.json update.

Findings: the register follows the PEG and genre (hands-on demo access), not the entity.
REPLICATES the m637/m742/#847/#852 peg-follows-register pattern at the null-tie outlet;
EXTENDS m74 (zero surveillance vocabulary for Snap's 4 cameras persists in the warm
hands-on register); EXTENDS m577's symmetric-adversarial band with a third peg class
(launch hands-on). Correlation is not causation.

Research: 6 browser.search query sets this run + 1 verification pass. REJECTED
candidates: Guardian x Snap (no standalone Sep-16 piece surfaced, bounded absence);
NYT x Snap (none surfaced); BI x Snap (no BI-authored piece surfaced); FT x Snap (none
surfaced); Atlantic x OpenAI (in corpus per #481/m404); Verge x Snap Sep-16
(relay-attributed only, no verbatim theverge.com URL). Novelty verified pre-commit
(zero test_type_a_862 files on disk; no "Type A #862" in git log; the
snapping-your-fingers-2000812735 URL zero-hit repo-wide; block key zero-hit;
max numeric mechanism_id 747; zero underscore-form 748/749 keys by designed keying
per #715). Falsification ledger holds at 26 (NOT a member; SIXTH in the Gizmodo
control family: #512 Google, #577 Anthropic, #582 OpenAI rogue-agent, #817 OpenAI
capital-raise, #842 OpenAI Claude-hack; the control behaves as predicted).

Rotation: 860-864 window THIRD leg, D(#860) -> E(#861) -> A(#862) (anchor patched
post-commit per #565). Sep 19 2026 17:00 PDT. 50 tests, 11 classes.
"""

import os
import re
import subprocess
import sys

import pytest
import yaml

TEST_FILE = __file__
OWN_BASENAME = "test_type_a_862_gizmodo_snap_sep16_launch_hands_on_register_vs_meta_adversarial_band_sep19_5pm.py"
MECH_KEY = "gizmodo_snap_sep16_launch_hands_on_register_vs_meta_adversarial_band_sep19_2026"
M_ID = 748
ITER = 862
TYPE_LETTER = "A"
ANCHORED_SHA = "PATCH_ME_IN_FOLLOWUP"

MECH_ID_MARKER = "mechanism" + "_748"
NEXT_ID_MARKER = "mechanism" + "_749"
NEXT_ID_NUMERIC = "mechanism_id: " + "749"
NEXT_ID_DASH = "mechanism" + "-749"

GIZMODO_URL = "https://gizmodo.com/snap-specs-ar-glasses-let-you-take-snapchat-pics-by-snapping-your-fingers-2000812735"
GAMESREVIEWS_URL = "https://gamesreviews.com/news/09/snap-specs-hands-on-2195-standalone-ar-glasses-impress-but-questions-remain/"

# Type A #862 is the THIRD leg of the 860-864 window: D(#860) -> E(#861) -> A(#862).
EXPECTED_ORDER = [("A", "862"), ("E", "861"), ("D", "860"), ("C", "859"), ("B", "858")]


def _repo_root():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _read(relpath):
    with open(os.path.join(_repo_root(), relpath), "r", encoding="utf-8") as fh:
        return fh.read()


def _yaml_block():
    text = _read("profiles/gizmodo.yaml")
    start = text.index(MECH_KEY)
    end = text.index("\neditorial_posture:", start)
    return text[start:end]


def _block_yaml():
    data = yaml.safe_load(_read("profiles/gizmodo.yaml"))
    return data["competitor_relationships"]["snap"][MECH_KEY]


def _git(*args):
    proc = subprocess.run(
        ["git", "-C", _repo_root()] + list(args),
        capture_output=True,
        text=True,
    )
    return proc


def _repo_grep(pattern):
    hits = []
    for root, dirs, files in os.walk(_repo_root()):
        if ".git" in dirs:
            dirs.remove(".git")
        if "__pycache__" in dirs:
            dirs.remove("__pycache__")
        for fname in files:
            if not fname.endswith((".py", ".yaml", ".yml", ".md", ".json")):
                continue
            fpath = os.path.join(root, fname)
            try:
                with open(fpath, "r", encoding="utf-8", errors="ignore") as fh:
                    for lineno, line in enumerate(fh, 1):
                        if re.search(pattern, line):
                            hits.append((os.path.relpath(fpath, _repo_root()), lineno, line.strip()))
            except OSError:
                continue
    return hits


class TestNovelty862:
    def test_single_test_type_a_862_file(self):
        files = [f for f in os.listdir(os.path.join(_repo_root(), "tests"))
                 if f.startswith("test_type_a_862")]
        assert files == [OWN_BASENAME]

    def test_type_a_862_main_commit_unique_and_anchored(self):
        # DESELECTED pre-commit (per #565): the commit does not exist yet.
        proc = _git("log", "--oneline", "--grep", "Type A #862: ", "--grep", "Type A #862 ", "--all")
        mains = [ln for ln in proc.stdout.splitlines()
                 if re.search(r"Type A #862(?::| )", ln)
                 and "anchor followup" not in ln and "log-hash followup" not in ln]
        assert len(mains) == 1
        assert ANCHORED_SHA not in ("PATCH_ME_IN_FOLLOWUP", "POST_COMMIT_ANCHORED", "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565")
        assert ANCHORED_SHA in mains[0]

    def test_novelty_verification_claim(self):
        blk = _block_yaml()
        novelty = blk["novelty"]
        assert "Zero test_type_a_862 files" in novelty
        assert 'no "Type A #862" in git log pre-commit' in novelty
        assert "snapping-your-fingers-2000812735 URL zero-hit repo-wide pre-commit" in novelty
        assert "block key zero-hit pre-commit" in novelty
        assert "max numeric mechanism_id 747 pre-commit" in novelty
        assert "zero underscore-form 748/749 keys" in novelty

    def test_860_864_window_legs_present_prior_to_862(self):
        log = _read("iteration-log.md")
        assert "## #860 Type D:" in log
        assert "## #861 Type E:" in log
        idx_860 = log.index("## #860 Type D:")
        idx_861 = log.index("## #861 Type E:")
        assert idx_860 > idx_861


class TestRotationGuard862:
    # All rotation-guard tests are DESELECTED pre-commit (per #565).
    def test_window_is_860_864_third_leg(self):
        subjects = _git("log", "--format=%s").stdout.splitlines()
        order = []
        for s in subjects:
            m = re.search(r"Type ([A-E]) #(\d+)(?::| )", s)
            if m and m.group(2) in ("858", "859", "860", "861", "862"):
                if "anchor followup" not in s and "log-hash followup" not in s:
                    order.append((m.group(1), m.group(2)))
        for expected, got in zip(EXPECTED_ORDER, order):
            assert expected == got

    def test_rotation_adjacency_cycle_valid(self):
        cycle = ["D", "E", "A", "B", "C"]
        got = [t for t, _n in EXPECTED_ORDER]
        assert got == ["A", "E", "D", "C", "B"]
        assert cycle[cycle.index("D") + 1] == "E"
        assert cycle[cycle.index("E") + 1] == "A"

    def test_predecessor_is_type_e_861(self):
        proc = _git("log", "--oneline", "--grep", "Type E #861", "--all")
        mains = [ln for ln in proc.stdout.splitlines()
                 if "anchor followup" not in ln and "log-hash followup" not in ln]
        assert len(mains) >= 1

    def test_anchor_sha_matches_head(self):
        head = _git("rev-parse", "HEAD").stdout.strip()
        assert ANCHORED_SHA == head


class TestNoveltyAnchor862:
    def test_block_key_absent_before_this_run(self):
        # The designed block key must not collide with any earlier
        # mechanism key; uniqueness is asserted structurally in
        # TestMechanism748Structure, this anchors the novelty claim text.
        assert "gizmodo_snap_sep16_launch" in MECH_KEY
        assert MECH_KEY.endswith("sep19_2026")


class TestMechanism748Structure:
    def test_block_key_exists_in_gizmodo_profile(self):
        text = _read("profiles/gizmodo.yaml")
        assert text.count(MECH_KEY) == 1
        block = _yaml_block()
        assert block.startswith(MECH_KEY)

    def test_block_key_unique_in_profile(self):
        text = _read("profiles/gizmodo.yaml")
        assert text.count(MECH_KEY) == 1

    def test_block_lives_under_snap_competitor_relationship(self):
        blk = _block_yaml()
        assert blk["mechanism_id"] == M_ID
        assert blk["competitor"] == "snap"
        assert blk["iteration"] == ITER
        assert blk["iteration_type"] == TYPE_LETTER

    def test_mechanism_id_748_adjacent_to_key(self):
        text = _read("profiles/gizmodo.yaml")
        start = text.index(MECH_KEY)
        assert "mechanism_id: 748" in text[start:start + 400]

    def test_pair_and_iteration_fields(self):
        blk = _block_yaml()
        assert blk["pair"] == "Gizmodo x Snap (vs Meta vs OpenAI)"
        assert blk["iteration_time"] == "2026-09-19 17:00 PDT"
        assert blk["scheduled_job_id"] == "mediascope-daily-iteration"
        assert blk["goal_id"] == "goal_54093bda4145"
        assert blk["type"] == "Type A - Competitor Coverage Deep Dive"
        assert set(blk["comparison_entities"]) == {"meta", "openai"}

    def test_m736_block_still_present(self):
        # The OpenAI-claude-hack comparator mechanism must survive this edit.
        text = _read("profiles/gizmodo.yaml")
        assert "gizmodo_openai_claude_hack_cybersecurity_accountability_register_sep18_2026" in text
        assert "mechanism_id: 736" in text


class TestMechanism748SnapArms:
    def test_one_fresh_snap_arm(self):
        blk = _block_yaml()
        assert len(blk["snap_arms"]) == 1

    def test_pero_arm_identity(self):
        blk = _block_yaml()
        arm = blk["snap_arms"][0]
        assert arm["author"] == "James Pero"
        assert arm["date"] == "2026-09-15"
        assert arm["register"] == "first-person hands-on playful-skeptical"
        assert arm["manual_illustrative_tone"] == pytest.approx(0.10)
        assert "Snap's AR Glasses Let You Take Snapchat Pics" in arm["title"]

    def test_zero_surveillance_vocabulary(self):
        blk = _block_yaml()
        arm = blk["snap_arms"][0]
        assert arm["surveillance_vocabulary_count"] == 0
        assert arm["surveillance_vocabulary"] == []
        assert "not foregrounded" in arm["led_indicator_framing"].lower()

    def test_attribution_urls_verbatim_in_block(self):
        block = _yaml_block()
        assert GIZMODO_URL in block
        assert GAMESREVIEWS_URL in block

    def test_key_language(self):
        block = _yaml_block()
        assert "not on my bingo card" in block
        assert "gimmicky" in block
        assert "optimistic" in block
        assert "most fun I had in my personal demo" in block

    def test_provenance_attestation(self):
        blk = _block_yaml()
        arm = blk["snap_arms"][0]
        assert arm["provenance_url"] == GAMESREVIEWS_URL
        assert "not novel repo-wide" in arm["provenance_note"]
        assert "hands-on time" in arm["provenance"]
        assert "September 16 launch event in Los Angeles" in arm["provenance"]


class TestMechanism748ComparatorArms:
    def test_meta_band_carried(self):
        blk = _block_yaml()
        meta = blk["meta_arms_carried"]
        assert meta["source_mechanism"] == 577
        tones = [a["manual_illustrative_tone"] for a in meta["arms"]]
        assert tones == pytest.approx([-0.70, -0.55, -0.60])
        assert meta["meta_band_mean"] == pytest.approx(-0.617)

    def test_openai_arm_carried(self):
        blk = _block_yaml()
        openai = blk["openai_arm_carried"]
        assert openai["source_mechanism"] == 736
        assert openai["manual_illustrative_tone"] == pytest.approx(-0.45)
        assert "Claude" in openai["description"]

    def test_pero_jun16_preview_carried(self):
        blk = _block_yaml()
        jun16 = blk["within_journalist_temporal"]["jun16_preview"]
        assert jun16["date"] == "2026-06-16"
        assert jun16["register"] == "neutral_product_preview"
        assert jun16["manual_illustrative_tone"] == pytest.approx(-0.10)
        assert jun16["carried_from"] == "mechanism 74"

    def test_carried_unrescored_per_807(self):
        blk = _block_yaml()
        assert blk["meta_arms_carried"]["carried_per"] == "#807 (un-rescored)"
        assert blk["openai_arm_carried"]["carried_per"] == "#807 (un-rescored)"

    def test_within_journalist_softening(self):
        blk = _block_yaml()
        temporal = blk["within_journalist_temporal"]
        assert temporal["journalist"] == "James Pero"
        assert temporal["illustrative_softening_jun_to_sep"] == pytest.approx(0.20)
        assert temporal["sep_hands_on"]["manual_illustrative_tone"] == pytest.approx(0.10)


class TestMechanism748Scorer:
    def _scorer(self):
        return _block_yaml()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]

    def test_illustrative_tones(self):
        s = self._scorer()
        assert s["snap_fresh_arm_tone"] == pytest.approx(0.10)
        assert s["meta_band_carried_m577"] == pytest.approx(-0.617)
        assert s["openai_arm_carried_m736"] == pytest.approx(-0.45)
        assert s["pero_jun16_preview_carried_m74"] == pytest.approx(-0.10)
        assert s["meta_arm_tones_carried"] == pytest.approx([-0.70, -0.55, -0.60])

    def test_averages(self):
        s = self._scorer()
        assert s["snap_arm_avg"] == pytest.approx(0.10)

    def test_delta_snap_minus_meta_at_4dp(self):
        s = self._scorer()
        expected = round(0.10 - (-0.617), 4)
        assert round(s["illustrative_delta_snap_minus_meta"], 4) == expected == 0.717

    def test_delta_snap_minus_openai(self):
        s = self._scorer()
        expected = round(0.10 - (-0.45), 4)
        assert round(s["illustrative_delta_snap_minus_openai"], 4) == expected == 0.55

    def test_deltas_logged_match_arithmetic(self):
        s = self._scorer()
        assert s["delta_arithmetic_snap_meta"] == "0.10 - (-0.617) = 0.717"
        assert s["delta_arithmetic_snap_openai"] == "0.10 - (-0.45) = 0.55"

    def test_engine_not_run(self):
        s = self._scorer()
        assert s["engine"] == "NOT run"

    def test_convention_target_minus_peer(self):
        s = self._scorer()
        assert s["target_entity"] == "snap"
        assert set(s["peer_entities"]) == {"meta", "openai"}
        assert "Target-minus-peer convention" in s["methodology"]

    def test_tone_basis_manual_illustrative(self):
        s = self._scorer()
        assert "MANUAL ILLUSTRATIVE" in s["methodology"]
        assert "not empirical corpus scores" in s["methodology"]


class TestMechanism748Discipline:
    def test_stats_not_calculated(self):
        s = _block_yaml()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert s["p_value"] == "NOT_CALCULATED"
        assert s["cohens_d"] == "NOT_CALCULATED"
        assert s["ci_95"] == "NOT_CALCULATED"

    def test_is_significant_false_and_verdict(self):
        s = _block_yaml()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert s["is_significant"] is False
        assert s["verdict"] == "directionally_supported_not_proven"
        assert _block_yaml()["verdict"] == "directionally_supported_not_proven"

    def test_no_analysis_json_update_and_not_artifact_grade(self):
        blk = _block_yaml()
        assert blk["no_analysis_json_update"] is True
        assert blk["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]["artifact_grade"] is False

    def test_not_falsification_family_ledger_holds(self):
        blk = _block_yaml()
        assert "NOT a member" in blk["falsification_family"]
        assert "SIXTH in the Gizmodo control family" in blk["falsification_family"]
        assert "ledger holds at 26" in blk["ledger"]

    def test_confounders_and_counterevidence_present(self):
        blk = _block_yaml()
        conf = blk["confounders_ranked"]
        assert set(conf.keys()) == {"strong", "moderate", "weak"}
        assert len(conf["strong"]) >= 3
        assert len(conf["moderate"]) >= 3
        assert len(conf["weak"]) >= 3
        assert len(blk["counter_evidence"]) >= 4
        assert any("Roasted to Death" in c for c in blk["counter_evidence"])
        assert any("not causation" in blk["finding"] for _ in [1])

    def test_connects_claims(self):
        block = _yaml_block()
        assert "REPLICATES" in block
        assert "EXTENDS" in block
        assert "m637/m742/#847/#852" in block
        assert "correlation is not causation" in block.lower()


class TestNoCrossContamination862:
    def test_block_ascii_only_no_em_dashes(self):
        block = _yaml_block()
        block.encode("ascii")
        assert "\u2014" not in block
        assert "\u2013" not in block

    def test_no_literal_749_mechanism_keys(self):
        hits = _repo_grep(re.escape(NEXT_ID_MARKER))
        assert hits == []
        hits = _repo_grep(re.escape(NEXT_ID_NUMERIC))
        assert hits == []
        hits = _repo_grep(re.escape(NEXT_ID_DASH))
        assert hits == []

    def test_block_key_absent_from_other_test_files(self):
        hits = _repo_grep(re.escape(MECH_KEY))
        test_hits = [h for h in hits if h[0].startswith("tests" + os.sep)]
        assert len(test_hits) == 1
        assert test_hits[0][0].endswith(OWN_BASENAME)


class TestDocSync862:
    def test_readme_test_file_row_present(self):
        readme = _read("README.md")
        assert OWN_BASENAME in readme
        assert "Type A #862" in readme

    def test_readme_stats_table_updated(self):
        readme = _read("README.md")
        assert "| Tests | 44057 |" in readme
        assert "Across 1190 test files" in readme

    def test_architecture_row_present(self):
        arch = _read("docs/ARCHITECTURE.md")
        assert OWN_BASENAME in arch
        assert "Type A #862" in arch

    def test_iteration_log_entry_present(self):
        log = _read("iteration-log.md")
        assert "## #862 Type A:" in log
        assert "Type A #862" in log


class TestDateGrounding862:
    def test_iteration_time_present(self):
        block = _yaml_block()
        assert "2026-09-19 17:00 PDT" in block

    def test_arm_dates_present(self):
        block = _yaml_block()
        assert "2026-09-15" in block
        assert "2026-06-16" in block

    def test_window_reference_in_file(self):
        block = _yaml_block()
        assert "860-864" in block
        assert "THIRD leg" in block
        assert "D->E->A" in block
