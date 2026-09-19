"""Type A #852 (850-854 window, third leg D->E->A): MIT Technology Review x
OpenAI Sep-15 Regalado biology-data philanthropy-positive register vs MIT TR
x Meta carried ironic-diminishment arms (mechanism 742).

FIRST dedicated corpus mechanism on Antonio Regalado's Sep 15 2026 piece
"AI models need more data about biology, and OpenAI is paying to create
it": the OpenAI Foundation paying to create "high-quality scientific
datasets" (Public Data for Health; $40M UNC Chapel Hill novel-cancer-vaccine
data program; $500k Ruxandra Teslo "biotech's lost archive" via 1Day Sooner;
OpenAdmet) with a philanthropy-positive/opportunity register (MANUAL
ILLUSTRATIVE +0.35). The piece never juxtaposes "OpenAI pays for biology
data" against OpenAI's unpaid publisher training-data posture, even as MIT
TR's own Sep 18 Download relays publisher-scraping survival anxiety. Meta
arms carried un-rescored from mechanism 619 per the #807 pattern
(-0.40, -0.35, -0.55, avg -0.4333: security-failure diminishment,
ironic-diminishment, accountability-adversarial); illustrative OpenAI-minus-
Meta delta 0.7833. REPLICATES the m637 peg-follows-register pattern (register
by news peg, not entity); EXTENDS the MIT TR x OpenAI family to the
philanthropy peg. connects_to: [637, 619]. MANUAL / qualitative only; engine
NOT run per the Aug 28 2026 standing rule; p_value/cohens_d/ci_95
NOT_CALCULATED; is_significant False; verdict directionally_supported_not_
proven; no_analysis_json_update: true; NOT artifact-grade; NOT a
falsification-family member - register documentation plus replication, not a
uniform-prediction test; falsification ledger holds at 26. Novelty verified
pre-commit (zero test_type_a_852 files; no 'Type A #852' in git log; max
numeric mechanism_id 741; zero underscore-form 742 keys by designed keying
per #715; block key zero-hit; the 1144129 URL zero-hit repo-wide; rejected
candidates: Verge OpenAI agent-safety primary, WIRED Anthropic Claude-hack
no-WIRED-arm, Verge Meta French-probe no-comparator-arm); count_stats gate
(delta = this file exactly); 850-854 window third leg D->E->A (anchor patched
post-commit per #565) - Sep 19 2026 07:00 PDT.
"""

import os
import re
import subprocess

import pytest
import yaml

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
TESTS_DIR = os.path.join(REPO_ROOT, "tests")
OWN_BASENAME = "test_type_a_852_mittr_openai_biology_data_philanthropy_register_vs_meta_ironic_diminishment_sep19_7am.py"
MECH_KEY = "mechanism_742_mittr_openai_biology_data_philanthropy_register_vs_meta_ironic_diminishment_sep19_2026"
M_ID = 742
ITER = 852
TYPE_LETTER = "A"
# Concatenated so this file never contains the literal marker itself.
MECH_ID_MARKER = "mechanism" + "_742"
NEXT_ID_MARKER = "mechanism" + "_743"
NEXT_ID_NUMERIC = "mechanism_id: " + "743"
EXPECTED_ORDER = [("A", "852"), ("E", "851"), ("D", "850"), ("C", "849"), ("B", "848")]
# Patched to the real main-commit SHA in the anchor followup per the #565 convention.
ANCHORED_SHA = "PATCH_ME_IN_FOLLOWUP"

REGALADO_URL = "https://www.technologyreview.com/2026/09/15/1144129/ai-models-need-more-data-about-biology-and-openai-is-paying-to-create-it/"
META_URLS = [
    "https://www.technologyreview.com/2026/06/05/1138452/the-download-ai-hacking-mythos-chatbots-brain-impacts/",
    "https://www.technologyreview.com/2025/02/07/1111292/meta-has-an-ai-for-brain-typing-but-its-stuck-in-the-lab/",
    "https://www.technologyreview.com/2025/01/29/1110630/three-reasons-meta-will-struggle-with-community-fact-checking/",
]
EXPECTED_URLS = [REGALADO_URL] + META_URLS

README_PATH = os.path.join(REPO_ROOT, "README.md")
ARCH_PATH = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")
LOG_PATH = os.path.join(REPO_ROOT, "iteration-log.md")


def _read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def _profiles_text():
    return _read(os.path.join(REPO_ROOT, "profiles", "mit-tech-review.yaml"))


def _block():
    text = _profiles_text()
    start = text.index(MECH_KEY)
    end = text.index("  meta:", start)
    return text[start:end]


def _corpus_ids():
    ids = []
    for root, _, files in os.walk(os.path.join(REPO_ROOT, "profiles")):
        for fn in files:
            if fn.endswith(".yaml"):
                text = _read(os.path.join(root, fn))
                for m in re.finditer(r"mechanism_id:\s*(\d+)", text):
                    ids.append(int(m.group(1)))
    return ids


def _repo_grep(needle, roots=("profiles", "tests")):
    hits = []
    for r in roots:
        base = os.path.join(REPO_ROOT, r)
        for root, _, files in os.walk(base):
            for fn in files:
                if fn.rsplit(".", 1)[-1] in ("py", "yaml", "md", "json"):
                    p = os.path.join(root, fn)
                    try:
                        if needle in _read(p):
                            hits.append(os.path.relpath(p, REPO_ROOT))
                    except OSError:
                        pass
    return hits


def _git(*args):
    return subprocess.run(
        ["git", *args],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=True,
    ).stdout


def _window(n=40):
    subjects = _git("log", f"-{n}", "--format=%s", "--no-merges").splitlines()
    seen_nums = set()
    out = []
    for s in subjects:
        m = re.match(r"Type ([A-E]) #(\d+):", s)
        if m and m.group(2) not in seen_nums:
            seen_nums.add(m.group(2))
            out.append(m.groups())
    return out[:5]


class TestNovelty852:
    def test_single_test_type_a_852_file(self):
        matches = [
            f
            for f in os.listdir(TESTS_DIR)
            if f.startswith("test_type_a_852") and f.endswith(".py")
        ]
        assert matches == [OWN_BASENAME], matches

    def test_type_a_852_main_commit_unique_and_anchored(self):
        # No #852 main commit exists pre-commit; the anchor test pins
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
            if "Type A #852" in line and "followup" not in line.lower()
        ]
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ) or mains == []
        if mains:
            assert mains[0].startswith(ANCHORED_SHA + " "), mains

    def test_novelty_verification_claim(self):
        # This run ADDS mechanism 742: post-commit max is 742, zero 743
        # keys anywhere. Pre-commit sweeps verified max 741, zero
        # underscore-form 742 keys (designed keying per #715), block key
        # zero-hit, 1144129 URL zero-hit repo-wide.
        assert max(_corpus_ids()) == 742
        assert _repo_grep(NEXT_ID_MARKER) == []
        assert _repo_grep(NEXT_ID_NUMERIC, roots=("profiles",)) == []

    def test_850_854_window_legs_present_prior_to_852(self):
        log = _read(LOG_PATH)
        for marker in (
            "## #850 Type D:",
            "#851 Type E:",
        ):
            assert marker in log, marker


class TestRotationGuard852:
    """#852 is the Type A third leg of window 850-854: D->E->A."""

    ORDER = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}

    def test_window_is_850_854_third_leg(self):
        # Deselected pre-commit per #565 (the #852 main commit does not
        # exist yet); patched green in the anchor followup.
        window = _window()
        assert window[: len(EXPECTED_ORDER)] == EXPECTED_ORDER, (
            f"850-854 window third leg D->E->A: expected {EXPECTED_ORDER}, "
            f"got {window[: len(EXPECTED_ORDER)]}"
        )

    def test_rotation_adjacency_cycle_valid(self):
        # Deselected pre-commit per #565; patched green in the followup.
        window = _window()
        for (t1, n1), (t2, n2) in zip(window, window[1:]):
            assert int(n1) == int(n2) + 1
            assert (self.ORDER[t1] - self.ORDER[t2]) % 5 == 1, (t1, t2)

    def test_predecessor_is_type_e_851(self):
        # Deselected pre-commit per #565; patched green in the followup.
        window = _window()
        assert window[1] == ("E", "851"), (
            f"immediate predecessor must be Type E #851, got {window[1]}"
        )

    def test_anchor_sha_matches_head(self):
        # Patched to the real main-commit SHA in the anchor followup per
        # the #565 convention; deselected pre-commit at the pytest CLI.
        result = subprocess.run(
            ["git", "log", "--format=%H %s", "--", "tests/" + OWN_BASENAME],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ), result.stdout
        mains = [
            line
            for line in result.stdout.splitlines()
            if "Type A #852" in line and "followup" not in line.lower()
        ]
        assert mains and mains[0].startswith(ANCHORED_SHA + " "), mains


class TestMechanism742Structure:
    def test_block_key_exists_in_mittr_profile(self):
        assert MECH_KEY in _profiles_text()

    def test_block_key_unique_in_profile(self):
        assert _profiles_text().count(MECH_KEY) == 1

    def test_block_lives_under_openai_competitor_relationship(self):
        d = yaml.safe_load(open(os.path.join(REPO_ROOT, "profiles", "mit-tech-review.yaml")))
        assert MECH_KEY in d["competitor_relationships"]["openai"]

    def test_mechanism_id_742_adjacent_to_key(self):
        text = _profiles_text()
        start = text.index(MECH_KEY)
        assert "mechanism_id: 742" in text[start : start + 400]

    def test_pair_and_iteration_fields(self):
        block = _block()
        assert 'pair: "MIT Technology Review x OpenAI (vs Meta)"' in block
        assert "iteration: 852" in block
        assert 'iteration_type: "A"' in block
        assert "goal_54093bda4145" in block
        assert "mediascope-daily-iteration" in block


class TestMechanism742Arms:
    def test_openai_article_identity_fields(self):
        d = yaml.safe_load(open(os.path.join(REPO_ROOT, "profiles", "mit-tech-review.yaml")))
        arm = d["competitor_relationships"]["openai"][MECH_KEY]["openai_article"]
        assert arm["title"] == "AI models need more data about biology, and OpenAI is paying to create it"
        assert arm["journalist"] == "Antonio Regalado"
        assert arm["date"] == "2026-09-15"
        assert arm["url"] == REGALADO_URL
        assert arm["register"] == "philanthropy_positive_opportunity"
        assert arm["manual_illustrative_tone"] == 0.35

    def test_regalado_url_verbatim_in_block(self):
        assert REGALADO_URL in _block()

    def test_regalado_url_zero_elsewhere_in_corpus(self):
        hits = _repo_grep("1144129", roots=("profiles",))
        assert hits == ["profiles/mit-tech-review.yaml"], hits

    def test_meta_arms_carried_from_619(self):
        d = yaml.safe_load(open(os.path.join(REPO_ROOT, "profiles", "mit-tech-review.yaml")))
        arms = d["competitor_relationships"]["openai"][MECH_KEY]["meta_articles_carried_un_rescored"]
        assert [a["manual_illustrative_tone"] for a in arms] == [-0.40, -0.35, -0.55]
        assert all("#807" in a["source_note"] for a in arms)

    def test_meta_arm_urls_verbatim(self):
        block = _block()
        for url in META_URLS:
            assert url in block, url

    def test_meta_registers_named(self):
        block = _block()
        for reg in ("security_failure_diminishment", "ironic_diminishment", "accountability_adversarial"):
            assert reg in block, reg


class TestMechanism742Scorer:
    def test_illustrative_arrays(self):
        d = yaml.safe_load(open(os.path.join(REPO_ROOT, "profiles", "mit-tech-review.yaml")))
        s = d["competitor_relationships"]["openai"][MECH_KEY]["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert s["target_scores_MANUAL_ILLUSTRATIVE"] == [0.35]
        assert s["peer_scores_MANUAL_ILLUSTRATIVE"] == [-0.40, -0.35, -0.55]

    def test_averages(self):
        d = yaml.safe_load(open(os.path.join(REPO_ROOT, "profiles", "mit-tech-review.yaml")))
        s = d["competitor_relationships"]["openai"][MECH_KEY]["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert s["target_avg"] == 0.35
        assert s["peer_avg"] == -0.4333

    def test_delta_arithmetic_at_4dp(self):
        target = 0.35
        peer = sum([-0.40, -0.35, -0.55]) / 3
        assert round(target - peer, 4) == 0.7833

    def test_delta_logged_matches_arithmetic(self):
        d = yaml.safe_load(open(os.path.join(REPO_ROOT, "profiles", "mit-tech-review.yaml")))
        s = d["competitor_relationships"]["openai"][MECH_KEY]["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert s["delta_manual_illustrative"] == 0.7833

    def test_engine_not_run(self):
        block = _block()
        assert "engine NOT run" in block

    def test_convention_target_minus_peer(self):
        block = _block()
        assert "target-minus-peer" in block


class TestMechanism742Discipline:
    def test_stats_not_calculated(self):
        block = _block()
        for token in ("p_value NOT_CALCULATED", "cohens_d NOT_CALCULATED", "ci_95 NOT_CALCULATED"):
            assert token in block, token

    def test_is_significant_false_and_verdict(self):
        block = _block()
        assert "is_significant False" in block
        assert "directionally_supported_not_proven" in block

    def test_no_analysis_json_update_and_not_artifact_grade(self):
        block = _block()
        assert "no_analysis_json_update: true" in block
        assert "NOT artifact-grade" in block

    def test_not_falsification_family_ledger_holds(self):
        block = _block()
        assert "NOT a falsification-family member" in block
        assert "ledger holds at 26" in block

    def test_confounders_and_counterevidence_present(self):
        d = yaml.safe_load(open(os.path.join(REPO_ROOT, "profiles", "mit-tech-review.yaml")))
        b = d["competitor_relationships"]["openai"][MECH_KEY]
        assert set(b["confounders_ranked"].keys()) == {"strong", "moderate", "weak"}
        assert len(b["counterevidence"]) == 2

    def test_excerpt_bounded_source_note(self):
        block = _block()
        assert "search-excerpt bounded per #503" in block
        assert "0 browser.open" in block or "direct fetch not attempted" in block


class TestNoCrossContamination852:
    def test_block_ascii_only_no_em_dashes(self):
        block = _block()
        assert all(ord(c) < 128 for c in block), "non-ASCII found in new block"
        assert "\u2014" not in block

    def test_no_literal_743_mechanism_keys(self):
        assert _repo_grep(NEXT_ID_MARKER, roots=("profiles", "tests")) == []
        assert _repo_grep("mechanism" + "-743", roots=("profiles", "tests")) == []

    def test_block_key_absent_from_other_test_files(self):
        # Own file carries MECH_KEY as a literal (this file's convention;
        # the marker is never duplicated across other test files).
        hits = [
            h
            for h in _repo_grep(MECH_KEY, roots=("tests",))
            if h != os.path.join("tests", OWN_BASENAME)
        ]
        assert hits == []

    def test_anchors_and_meta_not_confused(self):
        block = _block()
        assert "connects_to: [637, 619]" in block


class TestDocSync852:
    def test_readme_test_file_row_present(self):
        assert OWN_BASENAME in _read(README_PATH)

    def test_readme_stats_table_updated(self):
        text = _read(README_PATH)
        assert "43564" in text
        assert "1180" in text

    def test_architecture_stats_updated(self):
        text = _read(ARCH_PATH)
        assert "43564" in text or "1180" in text

    def test_iteration_log_entry_present(self):
        assert "## #852 Type A:" in _read(LOG_PATH)

    def test_type_a_852_mentioned_in_readme_row(self):
        text = _read(README_PATH)
        row_start = text.index(OWN_BASENAME)
        assert "Type A #852" in text[row_start : row_start + 4000]


class TestDateGrounding852:
    def test_iteration_time_present(self):
        assert "2026-09-19 07:00 PDT" in _block()

    def test_openai_article_date_present(self):
        assert 'date: "2026-09-15"' in _block()

    def test_window_reference_in_file(self):
        own = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "850-854" in own
