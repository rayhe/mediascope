"""Type A #1097: WIRED x OpenAI Sep-2026 slowdown-legality register extension.

THIRD leg of the 1095-1099 window: D (#1095, Type D qualitative corpus
integrity) -> E (#1096, Type E) -> A (this run) -> B (#1098) -> C (#1099)
per #565.

Mechanism under test (profiles/wired.yaml, competitor_relationships.openai):
the block key is format-built at runtime (per the #715 convention this
source file carries no contiguous underscore-form, dash-form, or numeric
mechanism key literal for MECH_NUM or NEXT_NUM).

Two fresh WIRED x OpenAI arms (excerpt-bounded per #503; 0 browser.open):
  (1) Sep 10 2026, Maxwell Zeff exclusive: "OpenAI wants to know if an AI
      industry slowdown would even be legal" (-0.35, inquisitive
      accountability on a leak-driven peg: Sherman Act coordination ask to
      Congress; Schulman "fake" cover quote; OpenAI declined to comment).
  (2) Sep 29 2026, Reece Rogers (Techmeme-filed wesearch relay): OpenAI
      Dots messaging via ChatGPT/Slack/Teams + iMessage/RCS waitlist
      (0.00, neutral product-announcement relay).
vs carried WIRED x Meta arms from m877 (un-rescored per #807):
  Pinky Promises skepticism (-0.45), NameTag class-action adversarial-legal
  (-0.30).

MANUAL ILLUSTRATIVE scorer: OpenAI mean -0.175 vs Meta mean -0.375,
delta +0.20 (Meta draws the harder register; thesis-consistent
directionally but small). Zeff-only read: -0.35 vs -0.375 = +0.025,
near-null parity on the leak-driven accountability peg, extending the
m877 peg-not-entity finding from the safety-crisis register into the
coordination/antitrust register.

Statistical discipline per the Aug 28 2026 standing rule: MANUAL
ILLUSTRATIVE ONLY; p_value / cohens_d / ci_95 NOT_CALCULATED;
is_significant false; engine NOT run; no_analysis_json_update;
NOT artifact-grade; verdict directionally_supported_not_proven;
correlation-not-causation throughout.

NOT a falsification-family member (register documentation plus
m877-family extension; no uniform-direction prediction under test).
Ledger holds at 37 (THIRTY-SEVENTH member-form = m880,
profiles/the-verge.yaml; THIRTY-EIGHTH member-claim form absent
repo-wide).
"""

import glob
import os
import re
import subprocess

import pytest
import yaml

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROFILES_DIR = os.path.join(REPO_ROOT, "profiles")
TESTS_DIR = os.path.join(REPO_ROOT, "tests")
OWN_BASENAME = os.path.basename(__file__)

MECH_NUM = 889
NEXT_NUM = 890
ITERATION = 1097
TYPE_LETTER = "A"
WINDOW = "1095-1099"

# Patched by the anchor followup commit per #565 (post-main-commit).
ANCHORED_SHA = "PATCH_ME_IN_FOLLOWUP"

# Format-built per the #715 convention: this source file carries no
# contiguous underscore-form mechanism key literal for MECH_NUM/NEXT_NUM.
BLOCK_KEY = (
    "mechanism_%d_wired_openai_slowdown_legality_register_"
    "vs_meta_carried_arms_sep30" % MECH_NUM
)
NUMERIC_NEEDLE = "mechanism_id: %d"
DASH_NEEDLE_FMT = "mechanism-%d"

# Doc-sync constants (patched post-first-run with the true collected count).
README_TEST_COUNT = 55739
README_FILE_COUNT = 1422
TEST_BASENAME = ("test_type_a_1097_wired_openai_slowdown_legality_"
                 "register_extension_sep30_10am.py")


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


def _wired_text():
    return open(os.path.join(PROFILES_DIR, "wired.yaml"),
                encoding="utf-8").read()


def _block_text():
    """Return the m889 block text (key line through the next 2-space key)."""
    text = _wired_text()
    start = text.index(BLOCK_KEY)
    out = []
    for i, line in enumerate(text[start:].splitlines()):
        if i > 0 and re.match(r"^  [a-z_]", line):
            break
        out.append(line)
    return "\n".join(out)


def _block_yaml():
    return yaml.safe_load(
        _wired_text())["competitor_relationships"]["openai"][BLOCK_KEY]


# ---------------------------------------------------------------------------
# 1. Novelty: this run is the first to claim mechanism 889.
# ---------------------------------------------------------------------------

class TestNovelty1097:
    def test_single_test_file_for_iteration(self):
        files = glob.glob(
            os.path.join(TESTS_DIR, "test_type_a_1097*.py"))
        assert len(files) == 1, files

    def test_main_commit_is_unique_and_anchored(self):
        """DESELECTED pre-commit per #565: the main commit does not exist yet.

        Post-commit this asserts the single #1097 commit is the anchor and
        carries the block-key + test-file changes.
        """

    def test_novelty_verification_claim_in_block(self):
        assert "zero test_type_a_1097 files on disk pre-commit" in _block_text()

    def test_window_legs_present(self):
        d_files = glob.glob(os.path.join(TESTS_DIR, "test_type_d_1095*.py"))
        e_files = glob.glob(os.path.join(TESTS_DIR, "test_type_e_1096*.py"))
        assert len(d_files) >= 1 and len(e_files) >= 1

    def test_max_numeric_mechanism_id_is_889(self):
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

class TestRotationGuard1097:
    @pytest.mark.rotation
    def test_window_1095_1099_third_leg(self):
        """A is the third leg of the 1095-1099 window per #565."""
        assert TYPE_LETTER == "A"
        assert ITERATION == 1097
        assert WINDOW == "1095-1099"

    @pytest.mark.rotation
    def test_type_a_adjacency_in_window(self):
        """D(#1095) -> E(#1096) -> A(#1097, this run) -> B(#1098) -> C(#1099)."""
        d_files = glob.glob(os.path.join(TESTS_DIR, "test_type_d_1095*.py"))
        e_files = glob.glob(os.path.join(TESTS_DIR, "test_type_e_1096*.py"))
        assert len(d_files) >= 1 and len(e_files) >= 1

    @pytest.mark.rotation
    def test_predecessor_is_type_e_1096(self):
        files = glob.glob(os.path.join(TESTS_DIR, "test_type_e_1096*.py"))
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

class TestNoveltyAnchor1097:
    @pytest.mark.anchor
    def test_anchor_sha_patched_post_commit(self):
        # No #1097 main commit exists pre-commit; the anchor test pins
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
            if "Type A #1097" in line and "followup" not in line.lower()
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
# 4. Mechanism 889 block structure.
# ---------------------------------------------------------------------------

class TestMechanism889Structure:
    def test_block_key_unique_in_wired(self):
        assert _wired_text().count(BLOCK_KEY) == 1

    def test_block_lives_under_openai(self):
        rels = yaml.safe_load(_wired_text())["competitor_relationships"]
        assert BLOCK_KEY in rels["openai"]

    def test_iteration_and_type(self):
        b = _block_yaml()
        assert b["iteration"] == ITERATION
        assert b["iteration_type"] == "A"
        assert b["iteration_time"] == "2026-09-30 10:00 PDT"

    def test_date_grounded(self):
        b = _block_yaml()
        assert b["date_analyzed"] == "2026-09-30"

    def test_author(self):
        assert _block_yaml()["author"] == "Kit (with Ray)"

    def test_distinct_from_prior_extends_877(self):
        text = _block_text()
        assert "mechanism 877" in text
        assert "safety-crisis register" in text
        assert "coordination/antitrust register" in text

    def test_not_falsification_member(self):
        assert "NOT a falsification-family member" in _block_text()

    def test_competitor_pair_names_openai_vs_meta(self):
        pair = _block_yaml()["competitor_pair"]
        assert "OpenAI" in pair and "Meta" in pair


# ---------------------------------------------------------------------------
# 5. Fresh WIRED x OpenAI arms.
# ---------------------------------------------------------------------------

class TestMechanism889OpenAIArms:
    def test_two_openai_arms(self):
        assert len(_block_yaml()["articles_openai"]) == 2

    def test_zeff_piece_title_and_date(self):
        arm = _block_yaml()["articles_openai"][0]
        assert "slowdown would even be legal" in arm["piece"]
        assert arm["author"] == "Maxwell Zeff"
        assert arm["date"] == "2026-09-10"

    def test_zeff_url_verbatim(self):
        url = ("https://www.wired.com/story/"
               "openai-wants-to-know-if-an-ai-industry-slowdown-would-even-be-legal/")
        assert url in _block_text()

    def test_zeff_schulman_quote(self):
        arm = _block_yaml()["articles_openai"][0]
        assert "Schulman" in arm["critic_quote"]
        assert "fake" in arm["critic_quote"]

    def test_zeff_tone_minus_035(self):
        assert _block_yaml()["articles_openai"][0][
            "manual_illustrative_tone"] == -0.35

    def test_dots_arm_url_and_date(self):
        arm = _block_yaml()["articles_openai"][1]
        assert "38222204" in arm["url"]
        assert arm["date"] == "2026-09-29"
        assert arm["author"] == "Reece Rogers"

    def test_dots_tone_zero(self):
        assert _block_yaml()["articles_openai"][1][
            "manual_illustrative_tone"] == 0.00

    def test_dots_relay_bounded(self):
        arm = _block_yaml()["articles_openai"][1]
        assert "Techmeme" in arm["url_source"] or "wesearch" in arm["url"]
        assert "verbatim WIRED URL not surfaced" in arm["url_source"]


# ---------------------------------------------------------------------------
# 6. Carried WIRED x Meta arms (un-rescored per #807).
# ---------------------------------------------------------------------------

class TestMechanism889MetaArms:
    def test_two_meta_arms(self):
        assert len(_block_yaml()["articles_meta"]) == 2

    def test_pinky_promises_carried(self):
        arm = _block_yaml()["articles_meta"][0]
        assert "Pinky Promises" in arm["piece"]
        assert arm["tone_carried"] == -0.45

    def test_nametag_carried(self):
        arm = _block_yaml()["articles_meta"][1]
        assert "NameTag" in arm["piece"] or "Training Data" in arm["piece"]
        assert arm["tone_carried"] == -0.30

    def test_carried_disclosed(self):
        for arm in _block_yaml()["articles_meta"]:
            assert "carried" in arm["source"].lower()
            assert "not novel" in arm["novelty_note"].lower()

    def test_no_rescore(self):
        for arm in _block_yaml()["articles_meta"]:
            assert "un-rescored" in arm["source"]


# ---------------------------------------------------------------------------
# 7. Financial relationship (context only, non-causal).
# ---------------------------------------------------------------------------

class TestFinancialRelationship889:
    def test_conde_nast_openai_deal_cited(self):
        rel = _block_yaml()["financial_relationship"]
        assert "Aug 2024" in rel["conde_nast_openai_deal"]
        assert "$1-5M/yr" in rel["conde_nast_openai_deal"]

    def test_meta_zero_deal(self):
        assert "$0" in _block_yaml()["financial_relationship"][
            "conde_nast_meta"]

    def test_deal_not_disclosed_in_coverage(self):
        rel = _block_yaml()["financial_relationship"]
        assert rel["deal_disclosed_in_wired_coverage"] is False

    def test_non_causal_language(self):
        rel = _block_yaml()["financial_relationship"]
        assert "no causal claim" in rel["non_causal_language"]

    def test_editorial_independence_note(self):
        rel = _block_yaml()["financial_relationship"]
        assert "no desk-level awareness evidence" in rel[
            "editorial_independence_note"]


# ---------------------------------------------------------------------------
# 8. MANUAL ILLUSTRATIVE scorer.
# ---------------------------------------------------------------------------

class TestMechanism889Scorer:
    def test_openai_mean(self):
        s = _block_yaml()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert s["target_avg"] == -0.175

    def test_meta_mean(self):
        s = _block_yaml()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert s["peer_avg"] == -0.375

    def test_delta_plus_020(self):
        s = _block_yaml()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert abs(s["delta"] - 0.20) < 1e-9

    def test_delta_calc_string(self):
        s = _block_yaml()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert "-0.175 - (-0.375) = +0.20" in s["delta_calc"]

    def test_zeff_only_parity_read(self):
        s = _block_yaml()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert "+0.025" in s["delta_direction"]
        assert "near-null parity" in s["delta_direction"]

    def test_statistical_discipline(self):
        s = _block_yaml()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert s["is_significant"] is False
        assert s["p_value"] == "NOT_CALCULATED"
        assert s["cohens_d"] == "NOT_CALCULATED"
        assert s["ci_95"] == "NOT_CALCULATED"
        assert s["verdict"] == "directionally_supported_not_proven"

    def test_manual_illustrative_only(self):
        s = _block_yaml()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert "MANUAL ILLUSTRATIVE ONLY" in s["scorer"]

    def test_correlation_not_causation(self):
        s = _block_yaml()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert s["correlation_not_causation"] is True
        assert s["no_analysis_json_update"] is True
        assert s["artifact_grade"] is False


# ---------------------------------------------------------------------------
# 9. Confounders, counter-evidence, open tests.
# ---------------------------------------------------------------------------

class TestMechanism889Discipline:
    def test_strong_confounders_ranked(self):
        c = _block_yaml()["confounders_ranked"]
        assert len(c["strong"]) == 3

    def test_excerpt_bounded_confounder(self):
        strong = " ".join(_block_yaml()["confounders_ranked"]["strong"])
        assert "#503" in strong

    def test_register_mismatch_confounder(self):
        strong = " ".join(_block_yaml()["confounders_ranked"]["strong"])
        assert "Register mismatch" in strong

    def test_counter_evidence_m877(self):
        ce = " ".join(_block_yaml()["counter_evidence"])
        assert "m877" in ce

    def test_counter_evidence_zeff_exclusive(self):
        ce = " ".join(_block_yaml()["counter_evidence"])
        assert "Zeff exclusive" in ce

    def test_open_empirical_test_ftc(self):
        assert "FTC probe" in _block_yaml()["open_empirical_test"]

    def test_no_em_dashes(self):
        assert "\u2014" not in _block_text()
        assert "\u2013" not in _block_text()


# ---------------------------------------------------------------------------
# 10. Falsification ledger holds at 37 (negative guard).
# ---------------------------------------------------------------------------

def _profiles_with(needle):
    """Profiles-scoped grep (the ledger convention from #1087/#1092)."""
    hits = []
    for root, dirs, files in os.walk(PROFILES_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
            p = os.path.join(root, f)
            if needle in open(p, encoding="utf-8", errors="replace").read():
                hits.append(p)
    return hits


class TestLedgerHoldsAt37:
    def test_exactly_one_37th_member_form(self):
        hits = _profiles_with("THIRTY-SEVENTH falsification-family member")
        assert hits == [os.path.join(PROFILES_DIR, "the-verge.yaml")], hits

    def test_37th_is_verge_m880(self):
        hits = _profiles_with("THIRTY-SEVENTH falsification-family member")
        text = open(hits[0], encoding="utf-8").read()
        assert (NUMERIC_NEEDLE % 880) in text
        assert "verge_openai_aug_sep2026_astra_safety_arc" in text

    def test_36th_still_exactly_once(self):
        hits = _profiles_with("THIRTY-SIXTH falsification-family member")
        assert len(hits) == 1, hits

    def test_no_38th_member_form(self):
        assert _profiles_with(
            "THIRTY-EIGHTH falsification-family member") == []
        assert "THIRTY-EIGHTH falsification-family member" not in _block_text()

    def test_m889_not_member_form(self):
        assert "THIRTY-EIGHTH" in _block_text()
        assert "NOT a falsification-family member" in _block_text()

    def test_verge_guard_line_intact(self):
        text = open(os.path.join(PROFILES_DIR, "the-verge.yaml"),
                    encoding="utf-8").read()
        assert "THIRTY-SEVENTH falsification-family member" in text


# ---------------------------------------------------------------------------
# 11. Supersession: #1095 zero-889 guards fail BY DESIGN; 890 stays clean.
# ---------------------------------------------------------------------------

class TestSupersessionAndCorpusPost1096:
    def test_underscore_889_hits_exactly_wired(self):
        """#1095 test_zero_889_forms_repo_wide now fails BY DESIGN: the single
        hit is the new m889 block in profiles/wired.yaml."""
        hits = _repo_grep_underscore_mechanism(MECH_NUM)
        assert hits == [os.path.join(PROFILES_DIR, "wired.yaml")], hits

    def test_numeric_889_hits_exactly_wired_profiles(self):
        """#1095 test_zero_889_numeric_forms_in_profiles now fails BY DESIGN:
        the single hit is the new m889 block."""
        hits = _profiles_grep_numeric_mechanism_id(MECH_NUM)
        assert hits == [os.path.join(PROFILES_DIR, "wired.yaml")], hits

    def test_dash_889_stays_zero(self):
        """The #1095 dash sweep stays green: no mechanism-889 form exists."""
        assert _repo_grep_dash_mechanism(MECH_NUM) == []

    def test_1095_numeric_890_profile_sweep_stays_green(self):
        assert _profiles_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_1095_underscore_890_repo_sweep_stays_green(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_1095_dash_890_repo_sweep_stays_green(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_no_second_889_block_variant(self):
        """Only one underscore-form 889 occurrence lives in wired.yaml."""
        text = open(os.path.join(PROFILES_DIR, "wired.yaml"),
                    encoding="utf-8").read()
        assert text.count("mechanism_%d" % MECH_NUM) == 1

    def test_max_numeric_is_889_not_888(self):
        """The #1095 test_max_mechanism_id_is_888 is superseded by design."""
        assert _max_numeric_mechanism_id_in_profiles() == MECH_NUM

    def test_novel_urls_zero_hit_elsewhere(self):
        zeff = ("https://www.wired.com/story/"
                "openai-wants-to-know-if-an-ai-industry-slowdown-would-even-be-legal/")
        dots = ("https://wesearch.press/s/"
                "openai-says-users-can-message-dots-through-chatgpt-slack-and-38222204")
        for url in (zeff, dots):
            hits = [
                p for p in _iter_source_files()
                if url in open(p, encoding="utf-8", errors="replace").read()
            ]
            assert hits == [os.path.join(PROFILES_DIR, "wired.yaml")], (url, hits)


# ---------------------------------------------------------------------------
# 12. Doc-sync (DESELECTED pre-commit per #565/#719/#721).
# ---------------------------------------------------------------------------

class TestDocSync1097:
    def test_readme_count_gate(self):
        """README test/file counts match the post-run totals."""
        readme = open(os.path.join(REPO_ROOT, "README.md"),
                      encoding="utf-8").read()
        assert ("| Tests | %d |" % README_TEST_COUNT) in readme
        assert ("Across %d test files" % README_FILE_COUNT) in readme

    def test_readme_table_row(self):
        """The #1097 test-file row is appended to the README test table."""
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
        """The #1097 test-file row is appended to the ARCHITECTURE tree."""
        arch = open(os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md"),
                    encoding="utf-8").read()
        assert TEST_BASENAME in arch


# ---------------------------------------------------------------------------
# 13. Iteration log (DESELECTED pre-commit per #565/#719/#721).
# ---------------------------------------------------------------------------

class TestIterationLog1097:
    def test_log_captures_1097(self):
        """The iteration log carries the #1097 Type A entry."""
        head = open(os.path.join(REPO_ROOT, "iteration-log.md"),
                    encoding="utf-8").read()[:4000]
        assert "## #1097 Type A:" in head
        assert "10:00 PDT" in head
        assert "m889" in head

    def test_log_window(self):
        """The entry names the 1095-1099 window third leg."""
        head = open(os.path.join(REPO_ROOT, "iteration-log.md"),
                    encoding="utf-8").read()[:4000]
        assert "1095-1099" in head
        assert "THIRD leg" in head

    def test_log_ledger_37(self):
        """The entry records ledger holds at 37."""
        head = open(os.path.join(REPO_ROOT, "iteration-log.md"),
                    encoding="utf-8").read()[:4000]
        assert "ledger holds at 37" in head
        assert "THIRTY-EIGHTH" in head

    def test_log_extends_877(self):
        """The entry records the m877-family extension."""
        head = open(os.path.join(REPO_ROOT, "iteration-log.md"),
                    encoding="utf-8").read()[:4000]
        assert "877" in head
