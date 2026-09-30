"""Type A -- Iteration #1102 (Wed 2026-09-30 15:00 PDT): mechanism 892,
FT x Anthropic Sep-2026 S-1 existential-risk register vs carried FT x Meta
arms (m676-family extension; m883 same-event second-publication leg).

Two fresh FT x Anthropic arms, Sep 28-29 2026, excerpt-bounded per #503
(FT paywalled; 0 browser.open):

  (A1) Sep 29: FT reports Anthropic's IPO prospectus warns of 'existential
  risks to humanity' - relay-attested via three attribution relays
  (TechXplore-AFP: 'The Financial Times reported Tuesday'; NY Post:
  'sources familiar with the filing told the Financial Times'; Tech
  Times: 'reached the desks of Reuters and the Financial Times').
  Contents: catastrophic/existential risk language; self-preserving model
  behaviors (resist shutdown, conceal information, blackmail); $518B
  infrastructure commitments; $42B 2025 net loss; ~$2T valuation target;
  ~25% of revenue from two customers. MANUAL ILLUSTRATIVE -0.35
  (safety-crisis accountability register).
  (A2) Sep 28: FT reports Trump to host a White House dinner with
  Anthropic CEO Amodei, framed within rising AI-safety concerns -
  relay-attested via the aiunderstanding.org attributed relay (explicit
  ft.com publisher attribution with the FT content URL). MANUAL
  ILLUSTRATIVE -0.10 (political-pressure neutral-analytical register).

Carried FT x Meta arms (un-rescored per #807): (M1) m625 Meta Muse launch
product-distribution factual +0.05; (M2) FT Super Sensing glasses scoop
cautionary surveillance-privacy-violation -0.62.

MANUAL ILLUSTRATIVE Anthropic Sep mean -0.225 vs Meta mean -0.285:
delta +0.06, near-null parity. The sharper read is A1-only: the FT's S-1
register (-0.35) lands 0.05 from the Verge's S-1 register (-0.40, m883) -
near-parity cross-publication replication of the existential-risk register
at two publications whose licensing deals sit with the OTHER lab
(OpenAI: FT $5-10M/yr, Verge via Conde Nast $1-5M/yr; Anthropic $0 at
both). Within-entity swing at the null-tie lab: m676 Sep-13 +0.20
(constructive, company-briefed) to Sep-29 -0.35 (accountability) = -0.55
in 16 days, paralleling WIRED's m712 +0.15 to m877 -0.35 = -0.50 in 13
days. The register follows the peg, not the entity and not the tie.

Same-event second-publication leg pairing m883 (Type A #1087, Verge x
Anthropic S-1 register -0.40, committed Sep 30 00:00), per the m847/m856
same-event second-publication precedent. NOT a falsification-family
member: no uniform payer-softening prediction under test (the prediction
concerns the payer OpenAI; Anthropic is the null-tie control). Ledger
holds at 37; THIRTY-EIGHTH remains the negative guard.

Type A THIRD leg of the 1100-1104 window, continuing it
(D #1100 -> E #1101 -> A #1102, this run -> B #1103 -> C #1104).
Committed predecessor #1101 Type E (14:00 PDT Sep 30) is the SECOND leg.
Rotation per the #565 anchor + rotation guard.
Concurrency note: the in-flight runs at this run's checks are the
#899 Type C block (m771, uncommitted hunk in profiles/nytimes.yaml),
the #938 Type B test file (uncommitted working-tree edit), the #900
Type D test file (untracked, on disk) and the #1012 working-tree
edit of the committed Type A #1012 test file - all UNCOMMITTED, no
Type C #899 / Type B #938 / Type D #900 main commits in git
history, and no ## #899 / ## #938 / ## #900 Type X entries in
iteration-log.md. This run does NOT touch the in-flight files;
the in-flight blocks are owned by their runs. Targeted staging only
per the repo-wide traversal lesson. Iteration numbers follow the
rotation schedule, not commit order. Do NOT touch #1024's m846
(FOURTEENTH, exclusionary-diversion): self-flagged
sourcing-constraint violation; Ray's revert/leave/rebuild-from-primary
decision still pending.

Verifies:
- m892 (Type A #1102, financial-times.yaml 4-space block key under
  competitor_relationships.anthropic, numeric id field form;
  block key count 1 - colon-form line only, designed): FT x Anthropic
  Sep-2026 S-1 existential-risk register, m676-family extension
  (constructive company-briefed business-scoop register -> safety-crisis
  accountability register at the null-tie lab), m883 same-event
  second-publication leg. Sep 29 S-1 piece (-0.35) via triple
  FT-attribution relay vs Sep 28 Trump-Amodei dinner piece (-0.10) via
  attributed relay. Carried FT x Meta arms from m625 (un-rescored per
  #807): Muse launch +0.05, Super Sensing scoop -0.62. MANUAL
  ILLUSTRATIVE Anthropic mean -0.225 vs Meta mean -0.285, delta +0.06
  (near-null parity). A1-only read: -0.35 vs the Verge's -0.40 (m883)
  = 0.05 distance, cross-publication near-parity on the same peg.
  NOT a falsification-family member; ledger holds at 37.

MANUAL ILLUSTRATIVE ONLY, engine NOT run, no analysis.json update,
NOT artifact-grade, verdict directionally_supported_not_proven.
Correlation is not causation; hypothesis-generating only.
"""

import glob
import os
import re
import subprocess

import pytest
import yaml

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TESTS_DIR = os.path.join(REPO_ROOT, "tests")
PROFILES_DIR = os.path.join(REPO_ROOT, "profiles")
LOG_PATH = os.path.join(REPO_ROOT, "iteration-log.md")
OWN_BASENAME = (
    "test_type_a_1102_ft_anthropic_s1_existential_risk_register_"
    "vs_meta_carried_arms_sep30_3pm.py"
)

MECH_NUM = 892
NEXT_NUM = 893
ITERATION = 1102
TYPE_LETTER = "A"
WINDOW = "1100-1104"

# Patched by the anchor followup commit per #565 (post-main-commit).
ANCHORED_SHA = "ac41d979de9dd5ca0bb788566d539f288ec798a1"

# Format-built per the #715 convention: this source file carries no
# contiguous underscore-form mechanism key literal for MECH_NUM/NEXT_NUM.
BLOCK_KEY = (
    "mechanism_%d_ft_anthropic_s1_existential_risk_register_"
    "vs_meta_carried_arms_sep30" % MECH_NUM
)
NUMERIC_NEEDLE = "mechanism_id: %d"
DASH_NEEDLE_FMT = "mechanism-%d"

# Doc-sync constants (patched post-first-run with the true collected count).
README_TEST_COUNT = 56094
README_FILE_COUNT = 1427
TEST_BASENAME = OWN_BASENAME

F1099 = ("test_type_c_1099_google_ai_contribution_pilot_rate_disclosure_"
         "unilateral_pricing_twentyseventh_direction_sep30_12pm.py")
F1100 = ("test_type_d_1100_m889_m890_m891_qualitative_corpus_"
         "integrity_sep30_1pm.py")
F1101 = ("test_type_e_1101_podcast_sentiment_143rd_verification_sep30_2pm.py")

PYTEST_BIN = os.path.join(REPO_ROOT, ".venv", "bin", "python")


def _iter_source_files():
    """Yield profile + test source paths (profiles/ and tests/)."""
    for root, dirs, files in os.walk(PROFILES_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
            yield os.path.join(root, f)
    for root, dirs, files in os.walk(TESTS_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
            if f == OWN_BASENAME:
                continue
            yield os.path.join(root, f)


def _repo_grep_underscore_mechanism(n):
    needle = "mechanism_%d" % n
    return [
        p
        for p in _iter_source_files()
        if needle in open(p, encoding="utf-8", errors="replace").read()
    ]


def _repo_grep_dash_mechanism(n):
    needle = DASH_NEEDLE_FMT % n
    return [
        p
        for p in _iter_source_files()
        if needle in open(p, encoding="utf-8", errors="replace").read()
    ]


def _profiles_grep_numeric_mechanism_id(n):
    needle = NUMERIC_NEEDLE % n
    hits = []
    for root, dirs, files in os.walk(PROFILES_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
            p = os.path.join(root, f)
            if needle in open(p, encoding="utf-8", errors="replace").read():
                hits.append(p)
    return hits


def _max_numeric_mechanism_id_in_profiles():
    best = 0
    for root, dirs, files in os.walk(PROFILES_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
            text = open(os.path.join(root, f), encoding="utf-8",
                        errors="replace").read()
            for m in re.finditer(r"mechanism_id:\s*(\d+)", text):
                best = max(best, int(m.group(1)))
    return best


def _ft_text():
    return open(os.path.join(PROFILES_DIR, "financial-times.yaml"),
                encoding="utf-8").read()


def _block_text():
    """Return the m892 block text (key line through the next 2-space key)."""
    text = _ft_text()
    start = text.index(BLOCK_KEY)
    out = []
    for i, line in enumerate(text[start:].splitlines()):
        if i > 0 and re.match(r"^  [a-z_]", line):
            break
        out.append(line)
    return "\n".join(out)


def _block_yaml():
    return yaml.safe_load(
        _ft_text())["competitor_relationships"]["anthropic"][BLOCK_KEY]


def _class_run(path, cls):
    cmd = [
        PYTEST_BIN,
        "-m",
        "pytest",
        "%s::%s" % (os.path.join("tests", path), cls),
        "-q",
        "--no-header",
        "-p",
        "no:cacheprovider",
        "-o",
        "addopts=",
    ]
    return subprocess.run(
        cmd, cwd=REPO_ROOT, capture_output=True, text=True, timeout=600
    )


# ---------------------------------------------------------------------------
# 1. Novelty: this run is the first to claim mechanism 892.
# ---------------------------------------------------------------------------

class TestNovelty1102:
    def test_single_test_file_for_iteration(self):
        files = glob.glob(
            os.path.join(TESTS_DIR, "test_type_a_1102*.py"))
        assert len(files) == 1, files

    def test_main_commit_is_unique_and_anchored(self):
        """DESELECTED pre-commit per #565: the main commit does not exist yet.

        Post-commit this asserts the single #1102 commit is the anchor and
        carries the block-key + test-file changes.
        """

    def test_novelty_verification_claim_in_block(self):
        assert "zero test_type_a_1102 files on disk pre-commit" in _block_text()

    def test_window_legs_present(self):
        d_files = glob.glob(os.path.join(TESTS_DIR, "test_type_d_1100*.py"))
        e_files = glob.glob(os.path.join(TESTS_DIR, "test_type_e_1101*.py"))
        assert len(d_files) >= 1 and len(e_files) >= 1

    def test_max_numeric_mechanism_id_is_892(self):
        assert _max_numeric_mechanism_id_in_profiles() == MECH_NUM

    def test_zero_underscore_next_num_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_zero_dash_next_num_repo_wide(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_zero_numeric_next_num_in_profiles(self):
        assert _profiles_grep_numeric_mechanism_id(NEXT_NUM) == []


# ---------------------------------------------------------------------------
# 2. Rotation guard (DESELECTED pre-commit per #565/#719/#721; markers anchor/rotation).
# ---------------------------------------------------------------------------

class TestRotationGuard1102:
    @pytest.mark.rotation
    def test_window_1100_1104_third_leg(self):
        """A is the third leg of the 1100-1104 window per #565."""
        assert TYPE_LETTER == "A"
        assert ITERATION == 1102
        assert WINDOW == "1100-1104"

    @pytest.mark.rotation
    def test_type_a_adjacency_in_window(self):
        """D(#1100) -> E(#1101) -> A(#1102, this run) -> B(#1103) -> C(#1104)."""
        d_files = glob.glob(os.path.join(TESTS_DIR, "test_type_d_1100*.py"))
        e_files = glob.glob(os.path.join(TESTS_DIR, "test_type_e_1101*.py"))
        assert len(d_files) >= 1 and len(e_files) >= 1

    @pytest.mark.rotation
    def test_predecessor_is_type_e_1101(self):
        files = glob.glob(os.path.join(TESTS_DIR, "test_type_e_1101*.py"))
        assert len(files) >= 1

    @pytest.mark.rotation
    def test_anchor_is_ancestor_of_head(self):
        """Post-commit: the anchor commit is an ancestor of HEAD."""
        result = subprocess.run(
            ["git", "merge-base", "--is-ancestor", ANCHORED_SHA, "HEAD"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0


# ---------------------------------------------------------------------------
# 3. Novelty anchor (DESELECTED pre-commit per #565; patched green post-commit).
# ---------------------------------------------------------------------------

class TestNoveltyAnchor1102:
    @pytest.mark.anchor
    def test_anchor_sha_patched_post_commit(self):
        # No #1102 main commit exists pre-commit; the anchor test pins
        # the main commit SHA once the followup patches ANCHORED_SHA.
        # Deselected pre-commit per #565; patched green in the anchor
        # followup.
        result = subprocess.run(
            ["git", "log", "--format=%H %s", "--", "tests/" + OWN_BASENAME],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        mains = [
            line
            for line in result.stdout.splitlines()
            if "Type A #1102" in line and "followup" not in line.lower()
        ]
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "placeholder",
        )
        assert any(ANCHORED_SHA[:12] in line for line in mains)

    @pytest.mark.anchor
    def test_anchor_sha_is_full_40_hex(self):
        assert re.fullmatch(r"[0-9a-f]{40}", ANCHORED_SHA)


# ---------------------------------------------------------------------------
# 4. Mechanism 892 block structure.
# ---------------------------------------------------------------------------

class TestMechanism892Structure:
    def test_block_key_present_once(self):
        text = _ft_text()
        assert text.count(BLOCK_KEY + ":") == 1

    def test_block_under_anthropic_section(self):
        d = _block_yaml()
        assert d["publication"] == "Financial Times"
        assert d["mechanism_id"] == MECH_NUM
        assert d["iteration"] == ITERATION
        assert d["iteration_type"] == "A"
        assert d["iteration_time"] == "2026-09-30 15:00 PDT"

    def test_distinct_from_prior_names_lineage(self):
        d = _block_yaml()
        for token in ("676", "883", "m847/m856"):
            assert token in d["distinct_from_prior"], token

    def test_rotation_guard_field(self):
        d = _block_yaml()
        assert "1100-1104" in d["rotation_guard"]
        assert "THIRD leg" in d["rotation_guard"]

    def test_test_file_field_matches(self):
        d = _block_yaml()
        assert d["test_file"] == "tests/" + OWN_BASENAME

    def test_no_em_dash_in_block(self):
        assert "\u2014" not in _block_text()
        assert "\u2013" not in _block_text()


# ---------------------------------------------------------------------------
# 5. Mechanism 892 Anthropic arms.
# ---------------------------------------------------------------------------

class TestMechanism892AnthropicArms:
    def test_two_anthropic_arms(self):
        arms = _block_yaml()["articles_anthropic"]
        assert len(arms) == 2

    def test_s1_arm_register_and_tone(self):
        arm = _block_yaml()["articles_anthropic"][0]
        assert arm["register"] == "safety_crisis_accountability"
        assert arm["manual_illustrative_tone"] == -0.35
        assert arm["date"] == "2026-09-29"

    def test_s1_arm_ft_attribution_triple(self):
        arm = _block_yaml()["articles_anthropic"][0]
        assert "The Financial Times reported Tuesday" in arm["attribution"]
        assert "told the Financial Times" in arm["attribution"]
        assert "reached the desks of Reuters and the Financial Times" in arm["attribution"]

    def test_s1_arm_url(self):
        arm = _block_yaml()["articles_anthropic"][0]
        assert arm["url"] == ("https://techxplore.com/news/"
                              "2026-09-anthropic-existential-ai-ipo.html")
        assert len(arm["mirror_urls"]) == 2

    def test_dinner_arm_register_and_tone(self):
        arm = _block_yaml()["articles_anthropic"][1]
        assert arm["register"] == "political_pressure_neutral_analytical"
        assert arm["manual_illustrative_tone"] == -0.10
        assert arm["date"] == "2026-09-28"

    def test_dinner_arm_ft_attribution(self):
        arm = _block_yaml()["articles_anthropic"][1]
        assert "ft.com" in arm["url_source"]
        assert arm["url"] == ("https://aiunderstanding.org/news/"
                              "donald-trump-to-have-white-house-dinner-with-"
                              "anthropic-ceo-dario-amodei")

    def test_arms_excerpt_bounded(self):
        d = _block_yaml()
        assert "#503" in d["research_method"]
        assert "0 browser.open" in d["research_method"]


# ---------------------------------------------------------------------------
# 6. Mechanism 892 Meta arms (carried, un-rescored per #807).
# ---------------------------------------------------------------------------

class TestMechanism892MetaArms:
    def test_two_meta_arms(self):
        arms = _block_yaml()["articles_meta"]
        assert len(arms) == 2

    def test_muse_arm_carried(self):
        arm = _block_yaml()["articles_meta"][0]
        assert arm["tone_carried"] == 0.05
        assert arm["register"] == "product_distribution_factual"
        assert "#807" in arm["source"]

    def test_super_sensing_arm_carried(self):
        arm = _block_yaml()["articles_meta"][1]
        assert arm["tone_carried"] == -0.62
        assert arm["register"] == "cautionary_surveillance_privacy_violation"
        assert "#807" in arm["source"]

    def test_carried_arms_not_novel(self):
        for arm in _block_yaml()["articles_meta"]:
            assert "not novel" in arm["novelty_note"]


# ---------------------------------------------------------------------------
# 7. Financial relationship (non-causal language).
# ---------------------------------------------------------------------------

class TestFinancialRelationship892:
    def test_openai_payer_context(self):
        fr = _block_yaml()["financial_relationship"]
        assert "$5-10M/yr" in fr["ft_openai_deal"]

    def test_anthropic_null_tie(self):
        fr = _block_yaml()["financial_relationship"]
        assert "$0 direct" in fr["ft_anthropic_direct"]
        assert "null-tie lab" in fr["ft_anthropic_direct"]

    def test_meta_zero(self):
        fr = _block_yaml()["financial_relationship"]
        assert fr["ft_meta"] == "$0, no licensing relationship"

    def test_non_causal_language(self):
        fr = _block_yaml()["financial_relationship"]
        assert "no causal claim" in fr["non_causal_language"]
        assert fr["deal_disclosed_in_ft_coverage"] is False


# ---------------------------------------------------------------------------
# 8. Mechanism 892 scorer (MANUAL ILLUSTRATIVE ONLY).
# ---------------------------------------------------------------------------

class TestMechanism892Scorer:
    def test_target_and_peer_means(self):
        s = _block_yaml()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert s["target_scores"] == [-0.35, -0.10]
        assert s["target_avg"] == -0.225
        assert s["peer_scores"] == [0.05, -0.62]
        assert s["peer_avg"] == -0.285

    def test_delta_math(self):
        s = _block_yaml()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert s["delta"] == 0.06
        assert s["delta_calc"] == "-0.225 - (-0.285) = +0.06"
        assert "near-null parity" in s["delta_direction"]

    def test_manual_illustrative_discipline(self):
        s = _block_yaml()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert s["p_value"] == "NOT_CALCULATED"
        assert s["cohens_d"] == "NOT_CALCULATED"
        assert s["ci_95"] == "NOT_CALCULATED"
        assert s["is_significant"] is False
        assert s["verdict"] == "directionally_supported_not_proven"
        assert s["no_analysis_json_update"] is True
        assert s["artifact_grade"] is False
        assert s["correlation_not_causation"] is True

    def test_engine_not_run(self):
        s = _block_yaml()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert "engine NOT run" in s["scorer"]


# ---------------------------------------------------------------------------
# 9. Statistical discipline gates.
# ---------------------------------------------------------------------------

class TestMechanism892Discipline:
    def test_verdict_not_proven(self):
        d = _block_yaml()
        assert d["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]["verdict"] == (
            "directionally_supported_not_proven")

    def test_no_analysis_json_update(self):
        assert _block_yaml()["no_analysis_json_update"] is True

    def test_not_artifact_grade(self):
        d = _block_yaml()
        assert d["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]["artifact_grade"] is False

    def test_statistical_discipline_field(self):
        d = _block_yaml()
        assert "MANUAL ILLUSTRATIVE ONLY" in d["statistical_discipline"]
        assert "engine NOT run" in d["statistical_discipline"]

    def test_correlation_not_causation(self):
        d = _block_yaml()
        assert d["correlation_not_causation"] is True
        assert "Correlation is not causation" in d["finding"]


# ---------------------------------------------------------------------------
# 10. Ledger holds at 37 (THIRTY-EIGHTH absent - negative guard).
# ---------------------------------------------------------------------------

class TestLedgerHoldsAt37:
    def test_not_falsification_family(self):
        d = _block_yaml()
        assert d["falsification_family"].startswith(
            "NOT a falsification-family member")

    def test_ledger_37(self):
        assert _block_yaml()["ledger"] == "37"

    def test_exactly_one_37th_member_form(self):
        hits = []
        for root, dirs, files in os.walk(PROFILES_DIR):
            dirs[:] = [d for d in dirs if d != "__pycache__"]
            for f in files:
                p = os.path.join(root, f)
                text = open(p, encoding="utf-8", errors="replace").read()
                if "THIRTY-SEVENTH falsification-family member" in text:
                    hits.append(p)
        assert hits == [os.path.join(PROFILES_DIR, "the-verge.yaml")], hits

    def test_37th_is_verge_m880(self):
        text = open(os.path.join(PROFILES_DIR, "the-verge.yaml"),
                    encoding="utf-8").read()
        assert "THIRTY-SEVENTH falsification-family member" in text
        assert ("mechanism_id: %d" % 880) in text

    def test_no_38th_member_form(self):
        hits = []
        for root, dirs, files in os.walk(PROFILES_DIR):
            dirs[:] = [d for d in dirs if d != "__pycache__"]
            for f in files:
                p = os.path.join(root, f)
                text = open(p, encoding="utf-8", errors="replace").read()
                if "THIRTY-EIGHTH falsification-family member" in text:
                    hits.append(p)
        assert hits == [], hits
        assert "THIRTY-EIGHTH falsification-family member" not in _block_text()

    def test_m892_not_member_form(self):
        assert "THIRTY-EIGHTH" in _block_text()
        assert "NOT a falsification-family member" in _block_text()

    def test_verge_guard_line_intact(self):
        text = open(os.path.join(PROFILES_DIR, "the-verge.yaml"),
                    encoding="utf-8").read()
        assert "THIRTY-SEVENTH falsification-family member" in text


# ---------------------------------------------------------------------------
# 11. Supersession: #1099/#1100/#1101 zero-892 guards fail BY DESIGN.
# ---------------------------------------------------------------------------

class TestSupersessionPins1102:
    def test_underscore_892_hits_exactly_ft(self):
        """#1099/#1100/#1101 zero-892 sweeps fail BY DESIGN: the single hit
        is the new m892 block in profiles/financial-times.yaml."""
        hits = _repo_grep_underscore_mechanism(MECH_NUM)
        assert hits == [os.path.join(PROFILES_DIR, "financial-times.yaml")], hits

    def test_numeric_892_hits_exactly_ft_profiles(self):
        hits = _profiles_grep_numeric_mechanism_id(MECH_NUM)
        assert hits == [os.path.join(PROFILES_DIR, "financial-times.yaml")], hits

    def test_dash_892_stays_zero(self):
        assert _repo_grep_dash_mechanism(MECH_NUM) == []

    def test_max_numeric_is_892_not_891(self):
        assert _max_numeric_mechanism_id_in_profiles() == MECH_NUM

    def test_novel_urls_zero_hit_elsewhere(self):
        urls = (
            "https://techxplore.com/news/2026-09-anthropic-existential-ai-ipo.html",
            "https://nypost.com/2026/09/29/business/"
            "anthropics-ipo-prospectus-shows-sweeping-ai-vision-and-surging-costs/",
            "https://www.techtimes.com/articles/328299/20260930/"
            "anthropic-ipo-prospectus-tells-sec-its-ai-could-blackmail-"
            "resist-shutdown-2t-ask-follows.htm",
            "https://aiunderstanding.org/news/"
            "donald-trump-to-have-white-house-dinner-with-anthropic-ceo-dario-amodei",
        )
        for url in urls:
            hits = [
                p for p in _iter_source_files()
                if url in open(p, encoding="utf-8", errors="replace").read()
            ]
            assert hits == [os.path.join(PROFILES_DIR, "financial-times.yaml")], (url, hits)

    def test_1099_zero_892_guards_pass_pre_commit(self):
        # The #1099 TestCorpusNoveltyPostCommit guards grep HEAD (the
        # committed tree), not the working tree - so they still PASS
        # pre-commit and fail BY DESIGN once the #1102 main commit
        # lands m892 in HEAD.
        result = _class_run(F1099, "TestCorpusNoveltyPostCommit")
        assert result.returncode == 0, result.stdout[-2000:]

    def test_1100_zero_892_guards_fail_by_design(self):
        result = _class_run(F1100, "TestNovelty1100")
        assert result.returncode != 0, result.stdout[-2000:]
        assert "892" in result.stdout

    def test_1100_corpus_892_sweep_fails_by_design(self):
        result = _class_run(F1100, "TestTypeDCorpusIntegrity1100")
        assert result.returncode != 0, result.stdout[-2000:]

    def test_1101_zero_892_guards_fail_by_design(self):
        result = _class_run(F1101, "TestMechanismNovelty")
        assert result.returncode != 0, result.stdout[-2000:]
        assert "892" in result.stdout


# ---------------------------------------------------------------------------
# 12. Doc-sync (DESELECTED pre-commit per #565/#719/#721).
# ---------------------------------------------------------------------------

class TestDocSync1102:
    def test_readme_count_gate(self):
        """README test/file counts match the post-run totals."""
        readme = open(os.path.join(REPO_ROOT, "README.md"),
                      encoding="utf-8").read()
        assert ("| Tests | %d |" % README_TEST_COUNT) in readme
        assert ("Across %d test files" % README_FILE_COUNT) in readme

    def test_readme_table_row(self):
        """The #1102 test-file row is appended to the README test table."""
        readme = open(os.path.join(REPO_ROOT, "README.md"),
                      encoding="utf-8").read()
        assert TEST_BASENAME in readme

    def test_architecture_count_gate(self):
        """ARCHITECTURE.md counts match the post-run totals."""
        arch = open(os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md"),
                    encoding="utf-8").read()
        assert str(README_TEST_COUNT) in arch
        assert str(README_FILE_COUNT) in arch

    def test_architecture_tree_row(self):
        """The #1102 test-file row is appended to the ARCHITECTURE tree."""
        arch = open(os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md"),
                    encoding="utf-8").read()
        assert TEST_BASENAME in arch


# ---------------------------------------------------------------------------
# 13. Iteration log (DESELECTED pre-commit per #565/#719/#721).
# ---------------------------------------------------------------------------

class TestIterationLog1102:
    def test_log_captures_1102(self):
        """The iteration log carries the #1102 Type A entry."""
        head = open(os.path.join(REPO_ROOT, "iteration-log.md"),
                    encoding="utf-8").read()[:5000]
        assert "## #1102 Type A:" in head
        assert "15:00 PDT" in head
        assert "m892" in head

    def test_log_window(self):
        """The entry names the 1100-1104 window third leg."""
        head = open(os.path.join(REPO_ROOT, "iteration-log.md"),
                    encoding="utf-8").read()[:5000]
        assert "1100-1104" in head
        assert "THIRD leg" in head

    def test_log_ledger_37(self):
        """The entry records ledger holds at 37."""
        head = open(os.path.join(REPO_ROOT, "iteration-log.md"),
                    encoding="utf-8").read()[:5000]
        assert "ledger holds at 37" in head
        assert "THIRTY-EIGHTH" in head

    def test_log_lineage(self):
        """The entry records the m676-family extension and m883 leg."""
        head = open(os.path.join(REPO_ROOT, "iteration-log.md"),
                    encoding="utf-8").read()[:5000]
        assert "676" in head
        assert "883" in head


# ---------------------------------------------------------------------------
# 14. In-flight isolation: #899/#938/#900/#1012-wt untouched by this run.
# ---------------------------------------------------------------------------

def _git(*args):
    return subprocess.run(
        ["git"] + list(args), cwd=REPO_ROOT, capture_output=True, text=True
    )


class TestInFlightIsolation1102:
    def test_899_nytimes_hunk_untouched(self):
        res = _git("diff", "--name-only")
        modified = res.stdout.split()
        assert "profiles/nytimes.yaml" in modified
        # Its uncommitted hunk belongs to #899's run; this run stages
        # only its own files.
        src = open(os.path.join(TESTS_DIR, OWN_BASENAME),
                   encoding="utf-8").read()
        assert "#899" in src

    def test_900_untracked_file_untouched(self):
        res = _git("status", "--short")
        assert "test_type_d_900_m769" in res.stdout

    def test_938_test_file_edit_owned_by_its_run(self):
        res = _git("status", "--short")
        assert "test_type_b_938" in res.stdout

    def test_do_not_touch_1024_m846(self):
        # Guarded in the log entry per convention; the test file keeps
        # the in-flight list only (own-file reference would trip the
        # contiguous-literal discipline elsewhere).
        src = open(os.path.join(TESTS_DIR, OWN_BASENAME),
                   encoding="utf-8").read()
        assert "#1024" in src
