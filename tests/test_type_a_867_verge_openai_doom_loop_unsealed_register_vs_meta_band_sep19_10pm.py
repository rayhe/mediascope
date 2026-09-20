"""Type A iteration 867: The Verge x OpenAI Sep-18 2026 "doom loop" unsealed-NYT-filing
accountability-adversarial register vs the Meta glasses band (mechanism 751),
THIRD leg of the 865-869 rotation window.

Type A contract (per the standing rotation doctrine): add ONE mechanism block keyed under
profiles/<publication>.yaml competitor_relationships, covering a publication x competitor
pair that is fresh this run, with attribution URLs verified against a real search, and
cross-reference the existing comparator register from an earlier Type A on the same
outlet. This run: The Verge x OpenAI.

Publication focus: The Verge (Vox Media). Competitor: OpenAI. Comparison entities: Meta,
Microsoft (second deal partner in the same piece). Financial context: financial_tie
licensing (undisclosed), direction strategic partnership, coverage_prediction softer
(this profile, competitor_relationships.openai) - so the deal prediction is uniform
softening on the deal partner; the observed register falsifies it at the legal layer.

OpenAI arm (FRESH this run, mechanism 751): Terrence O'Brien's Sep-18 2026 piece
"OpenAI and Microsoft knew they were starting a 'doom loop' for the web" (Verge byline
21:07 UTC attested by savedelete digest and the wesearch.press mirror listing,
"theverge.com - Google News"; theverge.com policy-blocked for browser.open per standing
rule, so excerpt-bounded per #503, 0 browser.open this run). Register: accountability-
adversarial legal-filing register. MANUAL ILLUSTRATIVE tone -0.55: lede "Recently
unsealed court documents in the New York Times' case against OpenAI and Microsoft are
pretty damning"; own-docs quotes "doom loop", "largest theft of labor in human history",
"complete mockery of the idea of fair use"; moderated by included rebuttals (Alex
Haurek: "These comments reflect one employee's individual perspective, are not a legal
analysis, and do not represent the company's views"; Jordan Usdan filing).

Comparator arms (CARRIED, un-rescored per the #807 pattern):
- Meta band from #592: same-outlet same-window glasses set [-0.55, -0.6, -0.5], avg -0.55.
- OpenAI arm from m598: Sep-4/5 wiki-incident adversarial delayed-disclosure register, -0.65.
- Selection temporal from m673: Sep-13 bounded absence of the PRO-partner DOJ SOI story.

Illustrative deltas: OpenAI-minus-Meta 0.00 (-0.55 - (-0.55)); OpenAI-minus-Microsoft
0.00. The deal partner is covered at exact parity with the $0-tie Meta baseline, and the
second deal partner (Microsoft, licensing usage-based, prediction softer) draws the same
adversarial register in the same piece. These are MANUAL ILLUSTRATIVE ONLY per the Aug
28 2026 standing rule: engine NOT run; p_value, cohens_d, ci_95 all NOT_CALCULATED;
is_significant False; NOT artifact-grade; NO analysis.json update.

Findings: the Vox-deal uniform-softening prediction is falsified at the copyright-legal
layer - TWENTY-SEVENTH falsification-family member (ledger 26->27). COMPLETES the m673
selection test: Sep-13 bounded absence of the pro-partner intervention story vs Sep-18
adversarial legal-filing coverage of the same beat - within 5 days the operative margin
is TONE not SELECTION, and the tone available on the deal partner is adversarial.
REPLICATES the m598 falsification at a new legal peg; EXTENDS #607 with a second
falsification-family member at the same outlet x entity. Correlation is not causation.

Research: 3 browser.search query sets this run + 1 corroboration pass. REJECTED
candidates: FT x Anthropic (no fresh Sep-18/19 piece surfaced with verbatim URL);
theverge.com canonical URL for the piece (no theverge.com URL in any Full-URL listing,
mirrors only - attested verbatim). Novelty verified pre-commit (zero test_type_a_867
files on disk; no "Type A #867" in git log; the doom-loop-for-1bc0911d and
2026-09-18-microsoft-openai-nyt-theft-of-labor-unsealed URLs zero-hit repo-wide; block
key zero-hit pre-commit; max numeric mechanism_id 750; zero underscore-form 751/752 keys
by designed keying per #715). Falsification ledger 26->27 (this block is the member).

Rotation: 865-869 window THIRD leg, D(#865) -> E(#866) -> A(#867) (anchor patched
post-commit per #565). Sep 19 2026 22:00 PDT. 51 tests, 11 classes.
"""

import os
import re
import subprocess

import pytest
import yaml

TEST_FILE = __file__
OWN_BASENAME = "test_type_a_867_verge_openai_doom_loop_unsealed_register_vs_meta_band_sep19_10pm.py"
MECH_KEY = "verge_openai_doom_loop_unsealed_nyt_filing_register_vs_meta_band_sep19_2026"
M_ID = 751
ITER = 867
TYPE_LETTER = "A"
ANCHORED_SHA = "236906056fac6fd89dc7ac53e7a5394d17f8f5e7"

MECH_ID_MARKER = "mechanism" + "_751"
NEXT_ID_MARKER = "mechanism" + "_752"
NEXT_ID_NUMERIC = "mechanism_id: " + "752"
NEXT_ID_DASH = "mechanism" + "-752"

WESEARCH_URL = "https://wesearch.press/s/openai-and-microsoft-knew-they-were-starting-a-doom-loop-for-1bc0911d"
SAVEDELETE_URL = "https://savedelete.com/news/archive/2026/09/18/"
TEMPERATURE2_URL = "https://temperature2.com/p/2026-09-18-microsoft-openai-nyt-theft-of-labor-unsealed/"

# Type A #867 is the THIRD leg of the 865-869 window: D(#865) -> E(#866) -> A(#867).
EXPECTED_ORDER = [("A", "867"), ("E", "866"), ("D", "865"), ("C", "864"), ("B", "863")]


def _repo_root():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _read(relpath):
    with open(os.path.join(_repo_root(), relpath), "r", encoding="utf-8") as fh:
        return fh.read()


def _yaml_block():
    text = _read("profiles/the-verge.yaml")
    start = text.index(MECH_KEY)
    end = text.index("\n  meta:", start)
    return text[start:end]


def _block_yaml():
    data = yaml.safe_load(_read("profiles/the-verge.yaml"))
    return data["competitor_relationships"]["openai"][MECH_KEY]


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


class TestNovelty867:
    def test_single_test_type_a_867_file(self):
        files = [f for f in os.listdir(os.path.join(_repo_root(), "tests"))
                 if f.startswith("test_type_a_867")]
        assert files == [OWN_BASENAME]

    def test_type_a_867_main_commit_unique_and_anchored(self):
        # DESELECTED pre-commit (per #565): the commit does not exist yet.
        proc = _git("log", "--format=%H %s", "--grep", "Type A #867")
        mains = [ln for ln in proc.stdout.splitlines()
                 if re.search(r"Type A #867(?::| )", ln)
                 and "anchor followup" not in ln and "log-hash followup" not in ln]
        assert len(mains) == 1
        assert ANCHORED_SHA not in ("PATCH_ME_IN_FOLLOWUP", "POST_COMMIT_ANCHORED", "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565")
        assert mains[0].startswith(ANCHORED_SHA + " ")

    def test_novelty_verification_claim(self):
        blk = _block_yaml()
        novelty = blk["novelty"]
        assert "Zero test_type_a_867 files" in novelty
        assert 'no "Type A #867" in git log pre-commit' in novelty
        assert "doom-loop-for-1bc0911d" in novelty
        assert "block key zero-hit pre-commit" in novelty
        assert "max numeric mechanism_id 750 pre-commit" in novelty
        assert "zero underscore-form 751/752 keys" in novelty

    def test_865_869_window_legs_present_prior_to_867(self):
        log = _read("iteration-log.md")
        assert "## #865 Type D:" in log
        assert "## #866 Type E:" in log
        idx_865 = log.index("## #865 Type D:")
        idx_866 = log.index("## #866 Type E:")
        assert idx_866 < idx_865


class TestRotationGuard867:
    # All rotation-guard tests are DESELECTED pre-commit (per #565).
    def test_window_is_865_869_third_leg(self):
        subjects = _git("log", "--format=%s").stdout.splitlines()
        order = []
        for s in subjects:
            m = re.search(r"Type ([A-E]) #(\d+)(?::| )", s)
            if m and m.group(2) in ("863", "864", "865", "866", "867"):
                # Followups and test-fixups are not rotation legs. The
                # push-status followup commit type (introduced at #864)
                # is excluded alongside anchor/log-hash followups.
                if ("anchor followup" not in s and "log-hash followup" not in s
                        and "push-status followup" not in s and "test fixup" not in s):
                    order.append((m.group(1), m.group(2)))
        for expected, got in zip(EXPECTED_ORDER, order):
            assert expected == got

    def test_rotation_adjacency_cycle_valid(self):
        cycle = ["D", "E", "A", "B", "C"]
        got = [t for t, _n in EXPECTED_ORDER]
        assert got == ["A", "E", "D", "C", "B"]
        assert cycle[cycle.index("D") + 1] == "E"
        assert cycle[cycle.index("E") + 1] == "A"

    def test_predecessor_is_type_e_866(self):
        proc = _git("log", "--oneline", "--grep", "Type E #866", "--all")
        mains = [ln for ln in proc.stdout.splitlines()
                 if "anchor followup" not in ln and "log-hash followup" not in ln]
        assert len(mains) >= 1

    def test_anchor_sha_matches_head(self):
        head = _git("rev-parse", "HEAD").stdout.strip()
        assert ANCHORED_SHA == head


class TestNoveltyAnchor867:
    def test_block_key_absent_before_this_run(self):
        # The designed block key must not collide with any earlier
        # mechanism key; uniqueness is asserted structurally in
        # TestMechanism751Structure, this anchors the novelty claim text.
        assert "verge_openai_doom_loop" in MECH_KEY
        assert MECH_KEY.endswith("sep19_2026")


class TestMechanism751Structure:
    def test_block_key_exists_in_verge_profile(self):
        text = _read("profiles/the-verge.yaml")
        assert text.count(MECH_KEY) == 1
        block = _yaml_block()
        assert block.startswith(MECH_KEY)

    def test_block_key_unique_in_profile(self):
        text = _read("profiles/the-verge.yaml")
        assert text.count(MECH_KEY) == 1

    def test_block_lives_under_openai_competitor_relationship(self):
        blk = _block_yaml()
        assert blk["mechanism_id"] == M_ID
        assert blk["competitor"] == "openai"
        assert blk["iteration"] == ITER
        assert blk["iteration_type"] == TYPE_LETTER

    def test_mechanism_id_751_adjacent_to_key(self):
        text = _read("profiles/the-verge.yaml")
        start = text.index(MECH_KEY)
        assert "mechanism_id: 751" in text[start:start + 400]

    def test_pair_and_iteration_fields(self):
        blk = _block_yaml()
        assert blk["pair"] == "The Verge x OpenAI (vs Meta)"
        assert blk["iteration_time"] == "2026-09-19 22:00 PDT"
        assert blk["scheduled_job_id"] == "mediascope-daily-iteration"
        assert blk["goal_id"] == "goal_54093bda4145"
        assert blk["type"] == "Type A - Competitor Coverage Deep Dive"
        assert set(blk["comparison_entities"]) == {"meta", "microsoft"}

    def test_m598_block_still_present(self):
        # The wiki-incident comparator mechanism must survive this edit.
        text = _read("profiles/the-verge.yaml")
        assert "mechanism_598_verge_openai_wiki_incident_adversarial_register_vox_deal_falsification_sep08" in text
        assert "mechanism_id: 598" in text

    def test_m673_block_still_present(self):
        text = _read("profiles/the-verge.yaml")
        assert "mechanism_673_verge_openai_doj_soi_coverage_selection_test_sep13" in text
        assert "mechanism_id: 673" in text


class TestMechanism751OpenAIArms:
    def test_one_fresh_openai_arm(self):
        blk = _block_yaml()
        assert len(blk["openai_arms"]) == 1

    def test_obrien_arm_identity(self):
        blk = _block_yaml()
        arm = blk["openai_arms"][0]
        assert arm["author"] == "Terrence O'Brien"
        assert arm["date"] == "2026-09-18"
        assert arm["register"] == "accountability-adversarial legal-filing register"
        assert arm["manual_illustrative_tone"] == pytest.approx(-0.55)
        assert "doom loop" in arm["title"]

    def test_attribution_urls_verbatim_in_block(self):
        block = _yaml_block()
        assert WESEARCH_URL in block
        assert SAVEDELETE_URL in block
        assert TEMPERATURE2_URL in block

    def test_verge_attribution_evidence(self):
        block = _yaml_block()
        assert "theverge.com - Google News" in block
        assert "9:07 PM UTC" in block
        assert "Terrence O'Brien" in block

    def test_key_language(self):
        block = _yaml_block()
        assert "pretty damning" in block
        assert "largest theft of labor in human history" in block
        assert "complete mockery of the idea of fair use" in block
        assert "individual perspective" in block

    def test_rebuttal_inclusion_noted(self):
        block = _yaml_block()
        assert "Haurek" in block
        assert "Usdan" in block

    def test_excerpt_bounded_evidence_grade(self):
        blk = _block_yaml()
        arm = blk["openai_arms"][0]
        assert "excerpt-bounded" in arm["evidence_grade"]
        assert "policy-blocked" in arm["url_note"]


class TestMechanism751ComparatorArms:
    def test_meta_band_carried(self):
        blk = _block_yaml()
        meta = blk["meta_arms_carried"]
        assert meta["source_mechanism"] == 592
        tones = [a["manual_illustrative_tone"] for a in meta["arms"]]
        assert tones == pytest.approx([-0.55, -0.60, -0.50])
        assert meta["meta_band_mean"] == pytest.approx(-0.55)

    def test_m598_openai_arm_carried(self):
        blk = _block_yaml()
        arm = blk["openai_arm_carried_m598"]
        assert arm["source_mechanism"] == 598
        assert arm["manual_illustrative_tone"] == pytest.approx(-0.65)
        assert "wiki incident" in arm["description"]

    def test_microsoft_second_deal_partner_arm(self):
        blk = _block_yaml()
        ms = blk["microsoft_arm_in_piece"]
        assert ms["financial_tie"] == "licensing"
        assert ms["coverage_prediction"] == "softer"
        assert ms["manual_illustrative_tone"] == pytest.approx(-0.55)

    def test_carried_unrescored_per_807(self):
        blk = _block_yaml()
        assert blk["meta_arms_carried"]["carried_per"] == "#807 (un-rescored)"
        assert blk["openai_arm_carried_m598"]["carried_per"] == "#807 (un-rescored)"

    def test_selection_temporal_m673(self):
        blk = _block_yaml()
        sel = blk["selection_temporal_m673"]
        assert "bounded absence" in sel["sep13_bounded_absence"]
        assert "adversarial" in sel["sep18_adversarial_selection"]
        assert sel["reading"].startswith("Within 5 days")


class TestMechanism751Scorer:
    def _scorer(self):
        return _block_yaml()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]

    def test_illustrative_tones(self):
        s = self._scorer()
        assert s["openai_fresh_arm_tone"] == pytest.approx(-0.55)
        assert s["meta_band_carried_592"] == pytest.approx(-0.55)
        assert s["microsoft_arm_tone"] == pytest.approx(-0.55)
        assert s["openai_arm_carried_m598"] == pytest.approx(-0.65)

    def test_delta_openai_minus_meta_is_zero(self):
        s = self._scorer()
        assert s["illustrative_delta_openai_minus_meta"] == pytest.approx(0.00)

    def test_delta_openai_minus_microsoft_is_zero(self):
        s = self._scorer()
        assert s["illustrative_delta_openai_minus_microsoft"] == pytest.approx(0.00)

    def test_deltas_logged_match_arithmetic(self):
        s = self._scorer()
        assert s["delta_arithmetic_openai_meta"] == "-0.55 - (-0.55) = 0.00"

    def test_engine_not_run(self):
        s = self._scorer()
        assert s["engine"] == "NOT run"

    def test_convention_target_minus_peer(self):
        s = self._scorer()
        assert s["target_entity"] == "openai"
        assert set(s["peer_entities"]) == {"meta", "microsoft"}
        assert "Target-minus-peer convention" in s["methodology"]

    def test_tone_basis_manual_illustrative(self):
        s = self._scorer()
        assert "MANUAL ILLUSTRATIVE" in s["methodology"]
        assert "not empirical corpus scores" in s["methodology"]


class TestMechanism751Discipline:
    def test_stats_not_calculated(self):
        s = _block_yaml()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert s["p_value"] == "NOT_CALCULATED"
        assert s["cohens_d"] == "NOT_CALCULATED"
        assert s["ci_95"] == "NOT_CALCULATED"

    def test_is_significant_false_and_verdict(self):
        s = _block_yaml()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert s["is_significant"] is False
        assert s["verdict"] == "directionally_supported_not_proven"
        assert _block_yaml()["falsification_verdict"] == "falsified_softer_prediction"

    def test_no_analysis_json_update_and_not_artifact_grade(self):
        blk = _block_yaml()
        assert blk["no_analysis_json_update"] is True
        assert blk["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]["artifact_grade"] is False

    def test_twenty_seventh_falsification_family_member(self):
        blk = _block_yaml()
        assert "TWENTY-SEVENTH falsification-family member" in blk["falsification_family"]
        assert "ledger 26->27" in blk["falsification_family"]
        assert "ledger 26->27" in blk["ledger"].lower()

    def test_confounders_and_counterevidence_present(self):
        blk = _block_yaml()
        conf = blk["confounders_ranked"]
        assert set(conf.keys()) == {"strong", "moderate", "weak"}
        assert len(conf["strong"]) >= 3
        assert len(conf["moderate"]) >= 4
        assert len(conf["weak"]) >= 3
        assert len(blk["counter_evidence"]) >= 5

    def test_connects_claims(self):
        block = _yaml_block()
        assert "REPLICATES" in block
        assert "EXTENDS" in block
        assert "COMPLETES" in block
        assert "correlation is not causation" in block.lower()


class TestNoCrossContamination867:
    def test_block_ascii_only_no_em_dashes(self):
        block = _yaml_block()
        block.encode("ascii")
        assert "\u2014" not in block
        assert "\u2013" not in block

    def test_no_literal_752_mechanism_keys(self):
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


class TestDocSync867:
    def test_readme_test_file_row_present(self):
        readme = _read("README.md")
        assert OWN_BASENAME in readme
        assert "Type A #867" in readme

    def test_readme_stats_table_updated(self):
        readme = _read("README.md")
        assert "| Tests | 44323 |" in readme
        assert "Across 1195 test files" in readme

    def test_architecture_row_present(self):
        arch = _read("docs/ARCHITECTURE.md")
        assert OWN_BASENAME in arch
        assert "Type A #867" in arch

    def test_iteration_log_entry_present(self):
        log = _read("iteration-log.md")
        assert "## #867 Type A:" in log
        assert "Type A #867" in log


class TestDateGrounding867:
    def test_iteration_time_present(self):
        block = _yaml_block()
        assert "2026-09-19 22:00 PDT" in block

    def test_arm_dates_present(self):
        block = _yaml_block()
        assert "2026-09-18" in block
        assert "2026-09-19" in block

    def test_window_reference_in_file(self):
        block = _yaml_block()
        assert "865-869" in block
        assert "THIRD leg" in block
        assert "D->E->A" in block
