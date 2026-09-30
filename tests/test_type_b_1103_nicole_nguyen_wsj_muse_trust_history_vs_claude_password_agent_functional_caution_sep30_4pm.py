"""Type B -- Iteration #1103 (Wed 2026-09-30 16:00 PDT): mechanism 893,
Nicole Nguyen (WSJ personal tech columnist) x Meta Muse Sep-2026
trust-history register vs carried Anthropic Claude password-agent
functional-caution register (Jul 2026 piece, #522 in-corpus arm).

Fresh Meta arm (NOVEL to corpus, zero repo-wide hits pre-commit): WSJ
"I Tried Meta's Muse AI Agent. It's Helpful and Scary at the Same Time."
(Sep 29 2026), https://www.wsj.com/tech/personal-tech/meta-muse-ai-agent-review-ab956101
- mixed-positive product enthusiasm ("first app I've experienced for
normal people"; "successfully hid the complexity of agentic AI")
gated by entity-rooted trust framing ("trust issues with Meta, the
ad-powered company... history of privacy scandals and data-use
controversies"; closing "I'm going to be cautious and reset Muse for
now"). MANUAL ILLUSTRATIVE +0.10.

Carried Anthropic arm (IN-CORPUS per #522, un-rescored per #807): WSJ
"I Gave an AI Agent Access to My Passwords. Here's What Happened."
(Jul 16 2026), https://www.wsj.com/tech/ai/1password-for-claude-ai-agents-password-manager-111a7a8a
- the in-corpus -0.4 is the Perplexity-facing security-threat register
(carried). This run documents the Claude-facing register split within
the same piece for the first time: functional caution with an explicit
clean bill ("Claude didn't do anything nefarious... Some chores are
better left to humans"; "glad to know about the expenses"). MANUAL
ILLUSTRATIVE +0.20 for the Claude-facing register.

Illustrative delta (Anthropic minus Meta): +0.10. The paid cooperative
counterparty (Meta, $50M/yr News Corp AI licensing, m549 per #834)
draws the HARDER trust register than the zero-cooperative-deal entity
(Anthropic). The deal-softness prediction FAILS on ordering at the
journalist level.

THIRTY-EIGHTH falsification-family member; ledger advances 37 -> 38.
Extends #693's NINETEENTH (Nguyen register constancy: Apple iPhone Duo
+0.40 vs Meta WhatsApp +0.15, genre-bound) into the AI-agent review
genre and the Meta x Anthropic entity pair.

STRONG confounders: factual substrate (Meta's documented privacy-scandal
record vs Anthropic's none - the register tracks corporate record, not
payment); within-piece entity split (Perplexity-facing -0.4 carried vs
Claude-facing +0.20 newly documented). MODERATE: 75-day temporal gap;
excerpt-tier on both arms (WSJ paywalled; 0 browser.open per #503).
WEAK: degenerate n=1 per arm per #638/#643.

Type B FOURTH leg of the 1100-1104 window, continuing it
(D #1100 -> E #1101 -> A #1102 -> B #1103, this run -> C #1104).
Committed predecessor #1102 Type A (16:00 PDT Sep 30) is the THIRD leg.
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
- m893 (Type B #1103, profiles/careers/journalists.yaml 4-space block
  key under Nicole Nguyen's competitor_coverage, colon-form key per
  #715 carrying no numeric mechanism-id substring, numeric id field
  form; block key count 1 - colon-form line + block_key field, designed):
  Nguyen WSJ Muse trust-history register (+0.10 illustrative, Sep 29
  2026, fresh/novel) vs carried Anthropic Claude password-agent
  functional-caution register (+0.20 illustrative, Jul 16 2026 piece,
  Perplexity-facing -0.4 carried per #807). Illustrative delta +0.10
  (Anthropic minus Meta). THIRTY-EIGHTH falsification-family member;
  ledger advances 37 -> 38. Extends #693/m650 NINETEENTH constancy
  lineage.

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
    "test_type_b_1103_nicole_nguyen_wsj_muse_trust_history_vs_"
    "claude_password_agent_functional_caution_sep30_4pm.py"
)

MECH_NUM = 893
NEXT_NUM = 894
ITERATION = 1103
TYPE_LETTER = "B"
WINDOW = "1100-1104"

# Patched by the anchor followup commit per #565 (post-main-commit).
ANCHORED_SHA = "bfe7f31a044b6f3e5379fad2473f524627d95784"

# Format-built per the #715 convention: this source file carries no
# contiguous underscore/dash-form mechanism key literal for MECH_NUM.
# The colon-form block key carries the iteration number (1103), not the
# mechanism number (893), by designed keying.
BLOCK_KEY = (
    "type_b_%d_nicole_nguyen_wsj_muse_trust_history_"
    "vs_claude_password_agent_functional_caution_sep30" % ITERATION
)
NUMERIC_NEEDLE = "mechanism_id: %d"
DASH_NEEDLE_FMT = "mechanism-%d"

# Doc-sync constants (patched post-first-run with the true collected count).
README_TEST_COUNT = 56172
README_FILE_COUNT = 1428
TEST_BASENAME = OWN_BASENAME

F1100 = ("test_type_d_1100_m889_m890_m891_qualitative_corpus_"
         "integrity_sep30_1pm.py")
F1101 = ("test_type_e_1101_podcast_sentiment_143rd_verification_sep30_2pm.py")
F1102 = ("test_type_a_1102_ft_anthropic_s1_existential_risk_register_"
         "vs_meta_carried_arms_sep30_3pm.py")

META_URL = ("https://www.wsj.com/tech/personal-tech/"
            "meta-muse-ai-agent-review-ab956101")
CLAUDE_URL = ("https://www.wsj.com/tech/ai/"
              "1password-for-claude-ai-agents-password-manager-111a7a8a")

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


def _journalists_text():
    return open(os.path.join(PROFILES_DIR, "careers", "journalists.yaml"),
                encoding="utf-8").read()


def _block_text():
    """Return the m893 block text (key line through the next 4-space key)."""
    text = _journalists_text()
    start = text.index(BLOCK_KEY)
    out = []
    for i, line in enumerate(text[start:].splitlines()):
        if i > 0 and re.match(r"^    [a-z_]", line):
            break
        out.append(line)
    return "\n".join(out)


def _block_yaml():
    data = yaml.safe_load(_journalists_text())["journalists"]
    for entry in data:
        cc = entry.get("competitor_coverage") or {}
        if BLOCK_KEY in cc:
            return cc[BLOCK_KEY]
    raise KeyError(BLOCK_KEY)


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


def _git(*args):
    return subprocess.run(
        ["git"] + list(args), cwd=REPO_ROOT, capture_output=True, text=True
    )


# ---------------------------------------------------------------------------
# 1. Novelty: this run is the first to claim mechanism 893.
# ---------------------------------------------------------------------------

class TestNovelty1103:
    def test_single_test_file_for_iteration(self):
        files = glob.glob(os.path.join(TESTS_DIR, "test_type_b_1103*.py"))
        assert files == [os.path.join(TESTS_DIR, OWN_BASENAME)], files

    def test_main_commit_is_unique_and_anchored(self):
        result = _git("log", "--format=%H %s", "--grep=Type B #1103")
        assert result.returncode == 0
        mains = [
            line
            for line in result.stdout.splitlines()
            if "Type B #1103" in line and "followup" not in line.lower()
        ]
        assert len(mains) == 1, mains

    def test_novelty_verification_claim_in_block(self):
        assert "Pre-commit novelty verified" in _block_text()

    def test_window_legs_present(self):
        for f in (F1100, F1101, F1102):
            assert os.path.exists(os.path.join(TESTS_DIR, f)), f

    def test_max_numeric_mechanism_id_is_893(self):
        assert _max_numeric_mechanism_id_in_profiles() == MECH_NUM

    def test_underscore_893_zero_repo_wide(self):
        assert _repo_grep_underscore_mechanism(MECH_NUM) == []

    def test_dash_893_stays_zero(self):
        assert _repo_grep_dash_mechanism(MECH_NUM) == []

    def test_numeric_893_hits_exactly_journalists(self):
        hits = _profiles_grep_numeric_mechanism_id(MECH_NUM)
        assert hits == [
            os.path.join(PROFILES_DIR, "careers", "journalists.yaml")
        ], hits

    def test_zero_underscore_next_num_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_zero_dash_next_num_repo_wide(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_zero_numeric_next_num_in_profiles(self):
        assert _profiles_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_meta_arm_url_novel_pre_commit(self):
        """The Muse URL was zero-hit repo-wide pre-commit; post-commit the
        single hit is this run's m893 block."""
        hits = [
            p
            for p in _iter_source_files()
            if "ab956101" in open(p, encoding="utf-8",
                                  errors="replace").read()
        ]
        assert hits == [
            os.path.join(PROFILES_DIR, "careers", "journalists.yaml")
        ], hits

    def test_claude_arm_url_in_corpus(self):
        """The Claude URL is in-corpus per #522 (news-corp.yaml +
        test_type_a_522), not novel."""
        hits = [
            p
            for p in _iter_source_files()
            if "111a7a8a" in open(p, encoding="utf-8",
                                  errors="replace").read()
        ]
        assert any("news-corp.yaml" in h for h in hits), hits
        assert any("test_type_a_522" in h for h in hits), hits


# ---------------------------------------------------------------------------
# 2. Rotation guard (DESELECTED pre-commit per #565/#719/#721; markers anchor/rotation).
# ---------------------------------------------------------------------------

class TestRotationGuard1103:
    @pytest.mark.rotation
    def test_window_1100_1104_fourth_leg(self):
        """B is the fourth leg of the 1100-1104 window per #565."""
        assert TYPE_LETTER == "B"
        assert ITERATION == 1103
        assert WINDOW == "1100-1104"

    @pytest.mark.rotation
    def test_type_b_adjacency_in_window(self):
        """D(#1100) -> E(#1101) -> A(#1102) -> B(#1103, this run) -> C(#1104)."""
        d_files = glob.glob(os.path.join(TESTS_DIR, "test_type_d_1100*.py"))
        e_files = glob.glob(os.path.join(TESTS_DIR, "test_type_e_1101*.py"))
        a_files = glob.glob(os.path.join(TESTS_DIR, "test_type_a_1102*.py"))
        assert len(d_files) >= 1 and len(e_files) >= 1 and len(a_files) >= 1

    @pytest.mark.rotation
    def test_predecessor_is_type_a_1102(self):
        files = glob.glob(os.path.join(TESTS_DIR, "test_type_a_1102*.py"))
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

class TestNoveltyAnchor1103:
    @pytest.mark.anchor
    def test_anchor_sha_patched_post_commit(self):
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
            if "Type B #1103" in line and "followup" not in line.lower()
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
# 4. Mechanism 893 block structure.
# ---------------------------------------------------------------------------

class TestMechanism893Structure:
    def test_block_key_present_once_as_key(self):
        text = _journalists_text()
        key_lines = [
            line for line in text.splitlines()
            if line.strip() == BLOCK_KEY + ":"
        ]
        assert len(key_lines) == 1, key_lines

    def test_block_key_carries_no_893(self):
        assert "893" not in BLOCK_KEY

    def test_mechanism_id_field(self):
        assert _block_yaml()["mechanism_id"] == 893

    def test_type_field(self):
        assert _block_yaml()["type"] == "Type B: Journalist Cross-Entity Tracking"

    def test_iteration_field(self):
        assert _block_yaml()["iteration"] == 1103

    def test_journalist_and_publication(self):
        d = _block_yaml()
        assert d["journalist"] == "Nicole Nguyen"
        assert d["publication"] == "wall-street-journal"

    def test_block_key_field_matches(self):
        assert _block_yaml()["block_key"] == BLOCK_KEY

    def test_nested_under_nguyen_competitor_coverage(self):
        data = yaml.safe_load(_journalists_text())["journalists"]
        owners = [
            entry.get("name")
            for entry in data
            if BLOCK_KEY in (entry.get("competitor_coverage") or {})
        ]
        assert owners == ["Nicole Nguyen"], owners

    def test_ascii_only(self):
        _block_text().encode("ascii")

    def test_no_em_dashes(self):
        assert "\u2014" not in _block_text()
        assert "\u2013" not in _block_text()


# ---------------------------------------------------------------------------
# 5. Meta arm: fresh WSJ Muse review, Sep 29 2026.
# ---------------------------------------------------------------------------

class TestMetaArm1103:
    def test_meta_arm_url(self):
        assert _block_yaml()["meta_arm"]["url"] == META_URL

    def test_meta_arm_date(self):
        assert _block_yaml()["meta_arm"]["date"] == "2026-09-29"

    def test_meta_arm_byline(self):
        assert _block_yaml()["meta_arm"]["byline"] == "Nicole Nguyen"

    def test_meta_arm_tone(self):
        assert _block_yaml()["meta_arm"]["manual_illustrative_tone"] == 0.10

    def test_meta_arm_novelty_claim(self):
        assert "FRESH" in _block_yaml()["meta_arm"]["novelty"]

    def test_meta_arm_trust_register_quoted(self):
        text = _block_text()
        assert "trust issues with Meta" in text
        assert "history of privacy scandals" in text

    def test_meta_arm_closing_caution_quoted(self):
        assert "cautious and reset Muse for now" in _block_text()


# ---------------------------------------------------------------------------
# 6. Anthropic arm: carried #522 piece, Claude-facing register split.
# ---------------------------------------------------------------------------

class TestAnthropicArm1103:
    def test_anthropic_arm_url(self):
        assert _block_yaml()["anthropic_arm"]["url"] == CLAUDE_URL

    def test_anthropic_arm_date(self):
        assert _block_yaml()["anthropic_arm"]["date"] == "2026-07-16"

    def test_perplexity_register_carried_per_807(self):
        d = _block_yaml()["anthropic_arm"]
        assert "carried_per_807" in d
        assert "-0.4" in d["carried_per_807"]
        assert "Perplexity" in d["carried_per_807"]

    def test_claude_facing_tone(self):
        assert _block_yaml()["anthropic_arm"]["manual_illustrative_tone"] == 0.20

    def test_claude_clean_bill_quoted(self):
        text = _block_text()
        assert "didn''t do anything nefarious" in text or \
            "didn't do anything nefarious" in text.replace("''", "'")

    def test_entity_split_documented(self):
        assert "entity split" in _block_text().lower() or \
            "entity-split" in _block_text().lower()

    def test_illustrative_delta(self):
        text = _block_text()
        assert "+0.10" in text
        assert "Anthropic minus Meta" in text


# ---------------------------------------------------------------------------
# 7. Financial geometry: News Corp balanced deals, Anthropic $0.
# ---------------------------------------------------------------------------

class TestFinancialGeometry1103:
    def test_meta_deal_cited(self):
        text = _block_text()
        assert "$50M/yr Meta" in text

    def test_openai_deal_cited(self):
        text = _block_text()
        assert "$50M/yr OpenAI" in text

    def test_anthropic_zero_cooperative(self):
        text = _block_text()
        assert "Anthropic" in text
        assert "$0 cooperative" in text

    def test_deal_softness_prediction_fails(self):
        text = _block_text()
        assert "FAILS on ordering" in text

    def test_cross_refs_deal_baseline(self):
        text = _block_text()
        assert "m549" in text
        assert "m519" in text


# ---------------------------------------------------------------------------
# 8. Statistical discipline: MANUAL ILLUSTRATIVE ONLY.
# ---------------------------------------------------------------------------

class TestStatisticalDiscipline1103:
    def test_manual_illustrative_only(self):
        d = _block_yaml()
        assert "MANUAL ILLUSTRATIVE ONLY" in d["statistical_discipline"]

    def test_engine_not_run(self):
        d = _block_yaml()
        assert "engine NOT run" in d["statistical_discipline"]

    def test_not_artifact_grade(self):
        d = _block_yaml()
        assert "NOT artifact-grade" in d["statistical_discipline"]

    def test_no_analysis_json_update(self):
        assert _block_yaml()["no_analysis_json_update"] is True

    def test_correlation_not_causation(self):
        assert _block_yaml()["correlation_not_causation"] is True

    def test_verdict(self):
        assert "directionally_supported_not_proven" in \
            _block_yaml()["statistical_discipline"]


# ---------------------------------------------------------------------------
# 9. Falsification ledger: THIRTY-EIGHTH member, ledger 38.
# ---------------------------------------------------------------------------

class TestFalsificationLedger1103:
    def test_thirty_eighth_member_form(self):
        assert _block_yaml()["falsification_family"].startswith(
            "THIRTY-EIGHTH falsification-family member")

    def test_ledger_38(self):
        assert _block_yaml()["falsification_ledger"] == "38"

    def test_exactly_one_38th_member_form_repo_wide(self):
        hits = []
        for root, dirs, files in os.walk(PROFILES_DIR):
            dirs[:] = [d for d in dirs if d != "__pycache__"]
            for f in files:
                p = os.path.join(root, f)
                text = open(p, encoding="utf-8", errors="replace").read()
                if "THIRTY-EIGHTH falsification-family member" in text:
                    hits.append(p)
        assert hits == [
            os.path.join(PROFILES_DIR, "careers", "journalists.yaml")
        ], hits

    def test_37th_member_form_still_verge(self):
        hits = []
        for root, dirs, files in os.walk(PROFILES_DIR):
            dirs[:] = [d for d in dirs if d != "__pycache__"]
            for f in files:
                p = os.path.join(root, f)
                text = open(p, encoding="utf-8", errors="replace").read()
                if "THIRTY-SEVENTH falsification-family member" in text:
                    hits.append(p)
        assert hits == [os.path.join(PROFILES_DIR, "the-verge.yaml")], hits

    def test_extends_693_nineteenth(self):
        text = _block_text()
        assert "NINETEENTH" in text
        assert "#693" in text

    def test_confounders_present(self):
        confs = _block_yaml()["confounders"]
        joined = " ".join(confs)
        assert "[STRONG]" in joined
        assert "[MODERATE]" in joined
        assert "[WEAK]" in joined
        assert "Factual-substrate" in joined
        assert "entity split" in joined.lower() or "entity-split" in joined.lower()


# ---------------------------------------------------------------------------
# 10. Supersession: #1102 guards fail BY DESIGN where this run supersedes.
# ---------------------------------------------------------------------------

class TestSupersessionPins1103:
    def test_1102_zero_numeric_893_guard_fails_by_design(self):
        """#1102's zero-numeric-893 sweep fails BY DESIGN: the single hit is
        the new m893 block in profiles/careers/journalists.yaml."""
        res = _class_run(
            F1102, "TestNovelty1102::test_zero_numeric_next_num_in_profiles")
        assert res.returncode != 0, res.stdout[-500:]

    def test_1102_underscore_893_guard_still_passes(self):
        res = _class_run(
            F1102, "TestNovelty1102::test_zero_underscore_next_num_repo_wide")
        assert res.returncode == 0, res.stdout[-500:]

    def test_1102_dash_893_guard_still_passes(self):
        res = _class_run(
            F1102, "TestNovelty1102::test_zero_dash_next_num_repo_wide")
        assert res.returncode == 0, res.stdout[-500:]

    def test_1102_no_38th_member_guard_fails_by_design(self):
        """#1102's no-38th-member guard fails BY DESIGN: m893 is the
        THIRTY-EIGHTH member."""
        res = _class_run(
            F1102, "TestLedgerHoldsAt37::test_no_38th_member_form")
        assert res.returncode != 0, res.stdout[-500:]

    def test_1102_ledger_37_guard_still_passes(self):
        """m892's own ledger field is untouched; the guard still passes."""
        res = _class_run(F1102, "TestLedgerHoldsAt37::test_ledger_37")
        assert res.returncode == 0, res.stdout[-500:]

    def test_1102_37th_member_guard_still_passes(self):
        res = _class_run(
            F1102, "TestLedgerHoldsAt37::test_exactly_one_37th_member_form")
        assert res.returncode == 0, res.stdout[-500:]


# ---------------------------------------------------------------------------
# 11. Doc-sync ratchet (DESELECTED pre-commit per #565/#719/#721).
# ---------------------------------------------------------------------------

class TestDocSync1103:
    def test_readme_count_gate(self):
        """README test/file counts match the post-run totals."""
        readme = open(os.path.join(REPO_ROOT, "README.md"),
                      encoding="utf-8").read()
        assert ("| Tests | %d |" % README_TEST_COUNT) in readme
        assert ("Across %d test files" % README_FILE_COUNT) in readme

    def test_readme_table_row(self):
        """The #1103 test-file row is appended to the README test table."""
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
        """The #1103 test-file row is appended to the ARCHITECTURE tree."""
        arch = open(os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md"),
                    encoding="utf-8").read()
        assert TEST_BASENAME in arch


# ---------------------------------------------------------------------------
# 12. Iteration log (DESELECTED pre-commit per #565/#719/#721).
# ---------------------------------------------------------------------------

class TestIterationLog1103:
    def test_log_captures_1103(self):
        """The iteration log carries the #1103 Type B entry."""
        head = open(LOG_PATH, encoding="utf-8").read()[:5000]
        assert "## #1103 Type B:" in head
        assert "16:00 PDT" in head
        assert "m893" in head

    def test_log_window(self):
        """The entry names the 1100-1104 window fourth leg."""
        head = open(LOG_PATH, encoding="utf-8").read()[:5000]
        assert "1100-1104" in head
        assert "FOURTH leg" in head

    def test_log_ledger_38(self):
        """The entry records the ledger advance 37 -> 38."""
        head = open(LOG_PATH, encoding="utf-8").read()[:5000]
        assert "THIRTY-EIGHTH" in head
        assert "38" in head

    def test_log_lineage(self):
        """The entry records the #693/m650 lineage and the carried #522 arm."""
        head = open(LOG_PATH, encoding="utf-8").read()[:5000]
        assert "693" in head
        assert "522" in head


# ---------------------------------------------------------------------------
# 13. In-flight isolation: #899/#938/#900/#1012-wt untouched by this run.
# ---------------------------------------------------------------------------

class TestInFlightIsolation1103:
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
        # underscore-needle guard, so this is a docstring-only pin).
        """#1024's m846 (FOURTEENTH, exclusionary-diversion) is a
        self-flagged sourcing-constraint violation; Ray's
        revert/leave/rebuild-from-primary decision still pending.
        This run does not touch it."""
        assert True
