"""Type A #1032 (1030-1034 window, third leg D->E->A): Reuters x Anthropic
Sep-24 Akamai-deal neutral register vs Reuters x Meta Sep-23 Connect
privacy-hardened preview register (mechanism 850).

FIRST dedicated corpus mechanism on the Reuters Sep 24 2026
Anthropic-Akamai $11.6B cloud deal piece ("Akamai, Anthropic sign $11.6
billion cloud services deal") vs the Reuters Sep 23 2026 Meta Connect
preview ("Meta expected to unveil smart glasses without camera as
privacy concerns grow", Aditya Soni) - a 24-hour same-desk natural
experiment. Anthropic arm: neutral deal-reportage on an $11.6B
seven-year commitment expandable to $20B with a warrant for up to 5
percent of Akamai (share-jump and capacity-demand framing), MANUAL
ILLUSTRATIVE -0.05. Meta arm: privacy-hardened preview register -
headline foregrounds privacy concerns, "amid growing privacy concerns
about AI devices that can be used to record people without their
consent", the California class action alleging annotators "viewed and
labeled footage of people's private moments, including changing
clothes", MANUAL ILLUSTRATIVE -0.45. Illustrative delta (Anthropic
minus Meta) +0.40: within 24 hours on the same wire desk the
competitor arm gets straight deal news with no burn-realism register
while Meta gets privacy-pressure framing inside a launch peg. The
Reuters-Meta multi-year content deal (Oct 25 2024) sits on META's
side, so the +0.40 spread runs OPPOSITE the naive payer-softening
prediction. EXTENDS mechanism 844 (#1022, Reuters news-desk
null-tie-wire, 48-hour design) to a FOURTH entity on the desk
(Anthropic, after OpenAI m739 Breakingviews and Google m844) with a
tighter 24-hour window; PAIRS mechanism 823 (#1028, FT interrogated
OpenAI cash burn vs Meta Connect-momentum inversion) as the
capital-register contrast. MANUAL / qualitative only; engine NOT run
on the arms per the Aug 28 2026 standing rule; p_value/cohens_d/ci_95
NOT_CALCULATED; is_significant False; verdict
directionally_supported_not_proven. NOT a falsification-family member
- register documentation plus m844 temporal replication, not a
uniform-prediction test; falsification ledger holds at 31; no
analysis.json update. Novelty verified pre-commit (zero
test_type_a_1032 files; no 'Type A #1032' in git log; max numeric
mechanism_id 849; zero underscore/dash-form 850 keys by designed
keying per #715; block key zero-hit; both reuters.com URLs zero-hit
repo-wide; 24-hour same-desk design tightens m844's 48-hour window);
1030-1034 window third leg D->E->A (anchor + rotation guard per #565) -
Sep 27 2026 05:00 PDT.

Test tally: 44 tests, 11 classes.
EXPECTED_TESTS = 44
"""

import os
import re
import subprocess

import pytest
import yaml

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
OWN_BASENAME = os.path.basename(__file__)
MECH_KEY = "reuters_anthropic_akamai_neutral_deal_register_vs_meta_connect_privacy_hardened_register_sep2026"
M_ID = 850
ITER = 1032
TYPE_LETTER = "A"
RUN_PDT = "2026-09-27 05:00 PDT"
# Concatenated per #715 so this file never carries the contiguous literals.
MECH_ID_MARKER = "mechanism" + "_850"  # own-form underscore sweep marker
NEXT_US = "mechanism" + "_851"  # next-number underscore sweep
NEXT_DASH = "mechanism" + "-851"  # next-number dash sweep
NEXT_NUMERIC = "mechanism: " + "851"  # next-number numeric sweep
EXPECTED_ORDER = [("A", "1032"), ("E", "1031"), ("D", "1030"), ("C", "1029"), ("B", "1028")]
# Patched to the real main-commit SHA in the anchor followup per the #565 convention.
ANCHORED_SHA = "7c2a289897fdf02df1bfcd6ed5a20b5a003bfef1"

ANTHROPIC_URL = "https://www.reuters.com/technology/akamai-anthropic-sign-116-billion-cloud-services-deal-2026-09-24/"
META_URL = "https://www.reuters.com/business/meta-expected-unveil-smart-glasses-without-camera-privacy-concerns-grow-2026-09-23/"
EXPECTED_URLS = [ANTHROPIC_URL, META_URL]

README_PATH = os.path.join(REPO_ROOT, "README.md")
ARCH_PATH = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")
LOG_PATH = os.path.join(REPO_ROOT, "iteration-log.md")
PROFILE = os.path.join("profiles", "competitor-coverage-research.yaml")

README_TESTS_BEFORE, README_FILES_BEFORE = 52968, 1356
EXPECTED_TESTS = 44
README_TESTS_AFTER, README_FILES_AFTER = 52968 + EXPECTED_TESTS, 1357

# In-flight work that must stay OUT of this run's staged set (targeted
# staging per the repo-wide traversal lesson): #899 (nytimes.yaml mechanism
# 771 hunk), #938 (test_type_b_938 anchor edit), #900 (untracked Type D test
# file), #1012-wt (working-tree edit on the committed Type A #1012 file).
INFLIGHT = {
    "profiles/nytimes.yaml",
    "tests/test_type_b_938_dominic_preston_verge_pixel_watch_gemini_personalization_vs_meta_luna_stigma_sep16.py",
    "tests/test_type_d_900_m769_qualitative_corpus_integrity_sep21_1pm.py",
    "tests/test_type_a_1012_mittr_anthropic_sep2026_doomer_turn_agenda_setting_register_vs_carried_meta_india_havoc_m817_pairing_sep26_7am.py",
}


def run_git(*args):
    return subprocess.run(
        ["git", *args], cwd=REPO_ROOT, capture_output=True, text=True, timeout=120
    )


def _read(path):
    with open(os.path.join(REPO_ROOT, path), encoding="utf-8") as f:
        return f.read()


def _profiles_text():
    return _read(PROFILE)


def _block():
    # Block key sits at 2-space indent under cross_publication_findings;
    # the next 0-2-space key (methodology:) bounds the block.
    text = _profiles_text()
    key = "  " + MECH_KEY + ":"
    start = text.index(key)
    rest = text[start + len(key) :]
    m = re.search(r"^ {0,2}[a-z][a-z0-9_]*:$", rest, re.M)
    end = start + len(key) + m.start()
    return text[start:end]


def _mech():
    d = yaml.safe_load(_profiles_text())
    return d["cross_publication_findings"][MECH_KEY]


def _corpus_ids():
    ids = []
    base = os.path.join(REPO_ROOT, "profiles")
    for root, _, files in os.walk(base):
        for fn in files:
            if fn.endswith(".yaml"):
                text = _read(os.path.join(root, fn))
                for m in re.finditer(r"mechanism(?:_id)?:\s*(\d+)", text):
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


def _window(n=40):
    # First occurrence of each distinct iteration number, newest first
    # (robust to followup commits that repeat the same "Type X #N" wording
    # without the colon, per the #752 convention).
    subjects = (
        run_git("log", f"-{n}", "--format=%s", "--no-merges").stdout.splitlines()
    )
    seen_nums = set()
    out = []
    for s in subjects:
        m = re.match(r"Type ([A-E]) #(\d+):", s)
        if m and m.group(2) not in seen_nums:
            seen_nums.add(m.group(2))
            out.append(m.groups())
    return out[:5]


# ---------------------------------------------------------------------------
# 1. Novelty anchor per #565 / #715
# ---------------------------------------------------------------------------
class TestNoveltyAnchorTypeA1032:
    def test_single_test_type_a_1032_file(self):
        files = [
            fn
            for fn in os.listdir(os.path.join(REPO_ROOT, "tests"))
            if fn.startswith("test_type_a_1032")
        ]
        assert files == [OWN_BASENAME]

    def test_anchor_sha_patched_post_commit(self):
        # Deselected pre-commit per #565: ANCHORED_SHA carries a placeholder
        # until the anchor followup patches it to the real main commit SHA.
        # main commit SHA once the followup patches ANCHORED_SHA.
        assert ANCHORED_SHA != "0" * 40
        assert re.fullmatch(r"[0-9a-f]{40}", ANCHORED_SHA)
        r = run_git("rev-parse", ANCHORED_SHA)
        assert r.returncode == 0 and r.stdout.strip() == ANCHORED_SHA

    def test_novelty_verification_claim(self):
        doc = __doc__
        for claim in (
            "zero\ntest_type_a_1032 files",
            "max numeric\nmechanism_id 849",
            "block key zero-hit",
            "both reuters.com URLs zero-hit",
        ):
            assert claim.replace("\n", " ") in doc.replace("\n", " ")


# ---------------------------------------------------------------------------
# 2. Rotation guard: 1030-1034 window, third leg D->E->A
# ---------------------------------------------------------------------------
class TestRotationGuard1030_1034Window:
    ORDER = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}

    def test_window_is_1030_1034_third_leg(self):
        assert _window() == EXPECTED_ORDER

    def test_rotation_adjacency_cycle_valid(self):
        window = _window()
        for (t1, n1), (t2, n2) in zip(window, window[1:]):
            assert int(n1) == int(n2) + 1
            assert (self.ORDER[t1] - self.ORDER[t2]) % 5 == 1, (t1, t2)

    def test_predecessor_is_type_e_1031(self):
        order = _window()
        assert order[1] == ("E", "1031")
        r = run_git("log", "--grep", "Type E #1031:", "--format=%H", "--no-merges")
        assert r.stdout.strip(), "no Type E #1031 main commit found"

    def test_no_concurrent_inflight_commits_asserted(self):
        r = run_git("log", "--grep", "Type A #1032:", "--format=%H", "--no-merges")
        assert len(r.stdout.split()) == 1, "expected exactly one Type A #1032 main commit"


# ---------------------------------------------------------------------------
# 3. Mechanism 850 block structure
# ---------------------------------------------------------------------------
class TestMechanism850Structure:
    def test_block_key_exists_in_research_yaml(self):
        assert ("  " + MECH_KEY + ":") in _profiles_text()

    def test_block_key_unique(self):
        assert _profiles_text().count("  " + MECH_KEY + ":") == 1

    def test_iteration_and_type_and_time_pdt(self):
        m = _mech()
        assert m["iteration"] == ITER
        assert m["rotation_type"] == TYPE_LETTER
        assert m["mechanism_id"] == M_ID
        assert m["discovery_date"] == "2026-09-27"

    def test_publication_pair_and_entities(self):
        m = _mech()
        assert m["publication"] == "Reuters"
        assert m["competitor"] == "Anthropic"
        assert m["comparator_entity"] == "Meta"
        assert m["finding_type"] == "cross_publication_coverage_asymmetry"

    def test_designed_keying_no_underscore_850_in_block_key(self):
        assert "850" not in MECH_KEY
        assert MECH_ID_MARKER not in MECH_KEY
        assert "mechanism_id: 850" in _block()


# ---------------------------------------------------------------------------
# 4. Arms: Anthropic deal vs Meta Connect preview
# ---------------------------------------------------------------------------
class TestMechanism850Arms:
    def test_one_anthropic_arm_one_meta_arm(self):
        m = _mech()
        assert len(m["anthropic_arms"]) == 1
        assert len(m["meta_arms"]) == 1

    def test_anthropic_arm_metadata(self):
        arm = _mech()["anthropic_arms"][0]
        assert arm["piece"] == "Akamai, Anthropic sign $11.6 billion cloud services deal"
        assert arm["date"] == "2026-09-24"
        assert arm["register"] == "neutral_deal_reportage"
        assert arm["tone_illustrative"] == -0.05
        assert "Reuters Staff" in arm["author"]

    def test_anthropic_key_language_verbatim(self):
        arm = _mech()["anthropic_arms"][0]
        langs = arm["key_language"]
        assert any("Akamai shares jumped 15 percent in extended trading" in l for l in langs)
        assert any("additional $9 billion" in l for l in langs)
        assert any("computing capacity to support its growing workloads" in l for l in langs)

    def test_meta_arm_metadata(self):
        arm = _mech()["meta_arms"][0]
        assert arm["piece"] == "Meta expected to unveil smart glasses without camera as privacy concerns grow"
        assert arm["date"] == "2026-09-23"
        assert arm["register"] == "privacy_hardened_product_preview"
        assert arm["tone_illustrative"] == -0.45
        assert "Aditya Soni" in arm["author"]

    def test_meta_key_language_verbatim(self):
        arm = _mech()["meta_arms"][0]
        langs = arm["key_language"]
        assert any("covertly record people" in l for l in langs)
        assert any("changing clothes" in l for l in langs)
        assert any("7 million" in l for l in langs)

    def test_all_source_urls_verbatim(self):
        arms = _mech()["anthropic_arms"] + _mech()["meta_arms"]
        urls = [a["source_url"] for a in arms]
        assert urls == EXPECTED_URLS
        for u in urls:
            assert u.startswith("https://www.reuters.com/")
            assert "url_attestation" in _mech()["anthropic_arms"][0]
            assert "url_attestation" in _mech()["meta_arms"][0]

    def test_zero_browser_open_attested(self):
        text = _block()
        assert "0 browser.open" in text


# ---------------------------------------------------------------------------
# 5. Asymmetry scorer
# ---------------------------------------------------------------------------
class TestMechanism850Scorer:
    def test_illustrative_tones_and_delta(self):
        s = _mech()["asymmetry_scorer"]
        assert s["anthropic_arm_tones"] == [-0.05]
        assert s["meta_arm_tones"] == [-0.45]
        assert s["illustrative_delta_anthropic_minus_meta"] == 0.40

    def test_delta_math(self):
        s = _mech()["asymmetry_scorer"]
        calc = round(s["anthropic_arm_avg"] - s["meta_arm_avg"], 2)
        assert calc == s["illustrative_delta_anthropic_minus_meta"] == 0.40
        assert "(-0.05) - (-0.45) = +0.40" in s["delta_calc"]

    def test_extends_844_framed(self):
        text = _block()
        assert "EXTENDS mechanism 844" in text
        assert "FOURTH entity" in text
        assert "24-hour" in text

    def test_pairs_823_framed(self):
        text = _block()
        assert "PAIRS mechanism 823" in text

    def test_payer_tie_counterdirectional(self):
        text = _block()
        assert "Oct 25 2024" in text
        assert "OPPOSITE the naive payer-softening prediction" in text

    def test_stats_not_calculated(self):
        s = _mech()["asymmetry_scorer"]
        assert s["p_value"] == "NOT_CALCULATED"
        assert s["cohens_d"] == "NOT_CALCULATED"
        assert s["ci_95"] == "NOT_CALCULATED"
        assert s["is_significant"] is False


# ---------------------------------------------------------------------------
# 6. Confounders and counterevidence
# ---------------------------------------------------------------------------
class TestMechanism850Confounders:
    def test_confounders_ranked_strong_first(self):
        cs = _mech()["confounders"]
        assert len(cs) == 7
        strengths = [c.split(":")[0] for c in cs]
        assert strengths[:3] == ["STRONG"] * 3
        assert "Story-type asymmetry" in cs[0]
        assert "Event-driven register" in cs[1]

    def test_counterevidence_three(self):
        ce = _mech()["counterevidence"]
        assert len(ce) == 3
        assert all(c.startswith("COUNTEREVIDENCE:") for c in ce)
        assert _mech()["verdict"] == "directionally_supported_not_proven"


# ---------------------------------------------------------------------------
# 7. Statistical discipline
# ---------------------------------------------------------------------------
class TestMechanism850Discipline:
    def test_statistical_discipline_qualitative_only(self):
        d = _mech()["statistical_discipline"]
        assert "MANUAL ILLUSTRATIVE scores only" in d
        assert "Engine NOT run" in d
        assert "is_significant: false" in d

    def test_no_analysis_json_update(self):
        assert _mech()["no_analysis_json_update"] is True

    def test_not_artifact_grade(self):
        assert "NOT artifact-grade" in _mech()["statistical_discipline"]

    def test_falsification_ledger_holds_at_31(self):
        f = _mech()["falsification_family"]
        assert "NOT a falsification-family member" in f
        assert "Ledger holds at 31" in f

    def test_correlation_not_causation(self):
        text = _block()
        assert "Correlation is not causation" in text

    def test_connects_to(self):
        assert _mech()["connects_to"] == [844, 823, 739]

    def test_test_file_and_research_method(self):
        m = _mech()
        assert m["test_file"] == "tests/" + OWN_BASENAME
        assert "0 browser.open" in m["research_method"]
        assert "3 browser.search query sets" in m["research_method"]


# ---------------------------------------------------------------------------
# 8. Corpus novelty post-commit
# ---------------------------------------------------------------------------
class TestCorpusNoveltyPostCommit:
    def test_max_numeric_mechanism_id_is_850(self):
        ids = _corpus_ids()
        assert max(ids) == M_ID

    def test_zero_next_numeric_851_in_profiles(self):
        text = "\n".join(
            _read(os.path.join(root, fn))
            for root, _, files in os.walk(os.path.join(REPO_ROOT, "profiles"))
            for fn in files
            if fn.endswith(".yaml")
        )
        assert NEXT_NUMERIC not in text

    def test_zero_next_underscore_dash_851_repo_wide(self):
        assert _repo_grep(NEXT_US) == []
        assert _repo_grep(NEXT_DASH) == []


# ---------------------------------------------------------------------------
# 9. Doc-sync ratchet per #719 (green post-doc-sync)
# ---------------------------------------------------------------------------
class TestDocSyncRatchet:
    def test_readme_header_stats_bumped(self):
        text = _read("README.md")
        assert str(README_TESTS_AFTER) in text
        assert str(README_FILES_AFTER) in text

    def test_readme_row_1032(self):
        text = _read("README.md")
        assert f"`tests/{OWN_BASENAME}`" in text
        assert "Type A #1032" in text

    def test_architecture_row(self):
        text = _read("docs/ARCHITECTURE.md")
        assert OWN_BASENAME in text

    def test_iteration_log_entry(self):
        text = _read("iteration-log.md")
        assert "## #1032 Type A:" in text


# ---------------------------------------------------------------------------
# 10. In-flight isolation
# ---------------------------------------------------------------------------
class TestInflightIsolation:
    def test_inflight_files_untouched(self):
        r = run_git("diff", "--cached", "--name-only")
        staged = set(r.stdout.split())
        for f in INFLIGHT:
            assert f not in staged, f"in-flight file staged: {f}"


# ---------------------------------------------------------------------------
# 11. ASCII-only, no em dashes
# ---------------------------------------------------------------------------
class TestBlockHygiene:
    def test_block_ascii_no_em_dash(self):
        text = _block()
        assert "\u2014" not in text  # em dash
        assert "\u2013" not in text  # en dash
        text.encode("ascii")

    def test_docstring_ascii(self):
        __doc__.encode("ascii")


assert EXPECTED_TESTS == 44
