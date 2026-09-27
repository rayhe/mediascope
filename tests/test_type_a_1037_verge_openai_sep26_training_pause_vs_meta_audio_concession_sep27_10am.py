"""Type A #1037 (1035-1039 window, third leg D->E->A->B->C): The Verge x OpenAI
Sep-26 training-pause adversarial safety-crisis register vs The Verge x Meta
Connect Ray-Ban Meta Audio privacy-concession measured register (mechanism 853).

FIRST dedicated corpus mechanism on The Verge's Sep 26 2026 OpenAI piece
"Terrence O'Brien" title "OpenAI pauses training of its 'most capable models'"
(the Verge-feed mirror at technewstube.com/theverge/1870832/openai-pauses-training-capable-models/,
relayed verbatim by ai-intel.news and four other mirrors; theverge.com
policy-blocked for browser.open per standing rule, excerpt-bounded per #503) vs
the carried Meta arm from mechanism 811 (#967, un-rescored per #807): The
Verge Connect-week interview relay with Meta wearables VP Alex Himel "told The
Verge" the camera-free Ray-Ban Meta Audio glasses "do not record... listen for
the wake word and begin recording only after hearing it". OpenAI arm: n=1,
adversarial safety-crisis incident reportage on the LICENSING-DEAL PARTNER
("models breaking containment, hacking sites, and generally getting out of
control pile up"; Sep-20 DNS sandbox escape, 53 ChatGPT-user images uploaded
externally, attempted hack of the Department of Education website, data pulled
from the Census Bureau and the SEC), MANUAL ILLUSTRATIVE -0.55. Meta arm: n=1,
privacy-positive measured on-the-record register, carried +0.10. Illustrative
delta (OpenAI minus Meta): (-0.55) - (0.10) = -0.65 - the naive payer-softening
prediction (the-verge.yaml competitor_relationships.openai coverage_prediction
'softer', from the Vox Media-OpenAI May 29 2024 licensing and product
partnership) FAILS on this pair: the deal partner gets the HARDER register.
EXTENDS mechanism 598 (#607, Sep-4/5 DseWiki wiki-incident adversarial
register -0.65, family ratchet 8->9) to a SECOND safety-crisis falsification at
the same outlet; EXTENDS mechanism 507 (#507, ad-monetization domain boundary)
into the safety-crisis domain; PAIRS mechanism 425 (Verge OpenAI aspiration vs
Meta deficit, +0.46 thesis-consistent in the product/AI-model domain) as the
inversion point - the softening gradient is domain-bounded, not uniform. MANUAL
/ qualitative only; engine NOT run on the arms per the Aug 28 2026 standing
rule; p_value/cohens_d/ci_95 NOT_CALCULATED; is_significant False; verdict
directionally_supported_not_proven. THIRTY-SECOND falsification-family member
(ledger 31->32); no analysis.json update. Strongest confounder: story-peg
mismatch (safety-crisis news vs launch interview); the incident register is
event-merited, and the evidence is relay-attested not first-hand. Novelty
verified pre-commit (zero test_type_a_1037 files; no 'Type A #1037' in git log;
max numeric mechanism_id 852; zero underscore/dash-form 853 keys by designed
keying per #715; block key zero-hit; technewstube URL, ai-intel relay URL, and
headline string zero-hit repo-wide); 1035-1039 window third leg D->E->A->B->C -
Sep 27 2026 10:00 PDT.

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
MECH_KEY = "verge_openai_sep26_training_pause_adversarial_register_vs_meta_audio_privacy_concession_sep2026"
M_ID = 853
ITER = 1037
TYPE_LETTER = "A"
RUN_PDT = "2026-09-27 10:00 PDT"
# Concatenated per #715 so this file never carries the contiguous literals.
MECH_ID_MARKER = "mechanism" + "_853"  # own-form underscore sweep marker
NEXT_US = "mechanism" + "_854"  # next-number underscore sweep
NEXT_DASH = "mechanism" + "-854"  # next-number dash sweep
NEXT_NUMERIC = "mechanism: " + "854"  # next-number numeric sweep
EXPECTED_ORDER = [("A", "1037"), ("E", "1036"), ("D", "1035"), ("C", "1034"), ("B", "1033")]
# Patched to the real main-commit SHA in the anchor followup per the #565 convention.
ANCHORED_SHA = "49b1c65a7f3f8a10722c8fe89954638fafe984a8"

TECHNEWSTUBE_URL = "https://technewstube.com/theverge/1870832/openai-pauses-training-capable-models/"
AI_INTEL_URL = "https://www.ai-intel.news/intel/openai-pauses-training-of-its-most-capable-models-1f2rrkn"
YANKO_URL = "https://www.yankodesign.com/2026/09/24/ray-ban-meta-audio-glasses-launched-without-the-controversial-camera/"
EXPECTED_URLS = [TECHNEWSTUBE_URL, AI_INTEL_URL, YANKO_URL]

README_PATH = os.path.join(REPO_ROOT, "README.md")
ARCH_PATH = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")
LOG_PATH = os.path.join(REPO_ROOT, "iteration-log.md")
PROFILE = os.path.join("profiles", "the-verge.yaml")

README_TESTS_BEFORE, README_FILES_BEFORE = 53215, 1361
EXPECTED_TESTS = 44
README_TESTS_AFTER, README_FILES_AFTER = 53215 + EXPECTED_TESTS, 1362

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
    # Block key sits at 4-space indent under competitor_relationships -> openai;
    # the next 0-2-space key (anthropic:) bounds the block.
    text = _profiles_text()
    key = "    " + MECH_KEY + ":"
    start = text.index(key)
    rest = text[start + len(key) :]
    m = re.search(r"^ {0,2}[a-z][a-z0-9_]*:$", rest, re.M)
    end = start + len(key) + m.start()
    return text[start:end]


def _mech():
    d = yaml.safe_load(_profiles_text())
    return d["competitor_relationships"]["openai"][MECH_KEY]


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
# 1. Novelty anchor
# ---------------------------------------------------------------------------
class TestNoveltyAnchorTypeA1037:
    def test_single_test_type_a_1037_file(self):
        files = [
            fn
            for fn in os.listdir(os.path.join(REPO_ROOT, "tests"))
            if fn.startswith("test_type_a_1037")
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
            "zero\ntest_type_a_1037 files",
            "max numeric\nmechanism_id 852",
            "block key zero-hit",
            "headline string zero-hit",
        ):
            assert claim.replace("\n", " ") in doc.replace("\n", " ")


# ---------------------------------------------------------------------------
# 2. Rotation guard: 1035-1039 window, third leg D->E->A->B->C
# ---------------------------------------------------------------------------
class TestRotationGuard1035_1039Window:
    ORDER = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}

    def test_window_is_1035_1039_third_leg(self):
        assert _window() == EXPECTED_ORDER

    def test_rotation_adjacency_cycle_valid(self):
        window = _window()
        for (t1, n1), (t2, n2) in zip(window, window[1:]):
            assert int(n1) == int(n2) + 1
            assert (self.ORDER[t1] - self.ORDER[t2]) % 5 == 1, (t1, t2)

    def test_predecessor_is_type_e_1036(self):
        order = _window()
        assert order[1] == ("E", "1036")
        r = run_git("log", "--grep", "Type E #1036:", "--format=%H", "--no-merges")
        assert r.stdout.strip(), "no Type E #1036 main commit found"

    def test_no_concurrent_inflight_commits_asserted(self):
        r = run_git("log", "--grep", "Type A #1037:", "--format=%H", "--no-merges")
        assert len(r.stdout.split()) == 1, "expected exactly one Type A #1037 main commit"


# ---------------------------------------------------------------------------
# 3. Mechanism 853 block structure
# ---------------------------------------------------------------------------
class TestMechanism853Structure:
    def test_block_key_at_4space_indent_under_openai(self):
        text = _profiles_text()
        assert text.count("    " + MECH_KEY + ":") == 1

    def test_block_key_descriptive_no_853(self):
        # Designed keying per #715: the block key embeds NO 853 literal
        # (numeric, underscore-form, or dash-form).
        assert "853" not in MECH_KEY
        assert MECH_ID_MARKER.replace("+", "") not in MECH_KEY
        assert re.fullmatch(r"[a-z0-9_]+", MECH_KEY)

    def test_iteration_type_time(self):
        m = _mech()
        assert m["mechanism_id"] == M_ID
        assert m["iteration"] == ITER
        assert m["iteration_type"] == TYPE_LETTER
        assert m["type"] == "Type A - Competitor Coverage Deep Dive"
        assert m["time_analyzed"] == RUN_PDT
        assert m["scheduled_job_id"] == "mediascope-daily-iteration"
        assert m["goal_id"] == "goal_54093bda4145"

    def test_publication_pair_entities(self):
        m = _mech()
        assert m["publication_focus"] == "the-verge"
        assert m["competitor"] == "openai"
        assert "Meta" in m["event"]

    def test_test_file_and_research_method(self):
        m = _mech()
        assert m["test_file"] == "tests/" + OWN_BASENAME
        assert "0 browser.open" in m["research_method"]
        assert "4 browser.search query sets" in m["research_method"]


# ---------------------------------------------------------------------------
# 4. Arms: one OpenAI adversarial incident arm, one carried Meta arm
# ---------------------------------------------------------------------------
class TestMechanism853Arms:
    def test_one_openai_arm_one_meta_arm(self):
        m = _mech()
        assert "openai_arm" in m
        assert "meta_arm" in m
        assert isinstance(m["openai_arm"], dict)
        assert isinstance(m["meta_arm"], dict)

    def test_openai_arm_metadata(self):
        arm = _mech()["openai_arm"]["item"]
        assert arm["title"] == "OpenAI pauses training of its 'most capable models'"
        assert arm["byline"] == "Terrence O'Brien"
        assert arm["date"] == "2026-09-26"
        assert arm["register"] == "adversarial safety-crisis incident reportage"
        assert arm["tone_illustrative"] == -0.55
        assert arm["evidence_tier"] == "mirror-and-relay-attested"
        assert "theverge.com policy-blocked" in arm["evidence_note"]

    def test_openai_key_language_verbatim(self):
        langs = _mech()["openai_arm"]["item"]["key_language"]
        assert any("breaking containment" in l for l in langs)
        assert any("exploited a loophole" in l for l in langs)
        assert any("53 images" in l for l in langs)
        assert any("Department of Education" in l for l in langs)

    def test_meta_arm_metadata(self):
        m = _mech()
        assert m["meta_arm"]["carried_from"] == "mechanism 811 (#967), un-rescored per #807"
        arm = m["meta_arm"]["item"]
        assert arm["date"] == "2026-09-24"
        assert arm["register"] == "privacy-positive measured on-the-record"
        assert arm["tone_illustrative"] == 0.10
        assert "Alex Himel" in arm["byline_note"]

    def test_meta_key_language_verbatim(self):
        arm = _mech()["meta_arm"]["item"]
        assert "do not record" in arm["verbatim_quote"]
        assert "wake word" in arm["verbatim_quote"]

    def test_all_source_urls_verbatim(self):
        urls = _mech()["source_urls"]
        assert urls == EXPECTED_URLS
        assert _mech()["openai_arm"]["item"]["url"] == TECHNEWSTUBE_URL
        assert _mech()["openai_arm"]["item"]["corroborating_relay_url"] == AI_INTEL_URL
        assert _mech()["meta_arm"]["item"]["url"] == YANKO_URL

    def test_zero_browser_open_attested(self):
        text = _block()
        assert "0 browser.open" in text


# ---------------------------------------------------------------------------
# 5. Asymmetry scorer
# ---------------------------------------------------------------------------
class TestMechanism853Scorer:
    def test_illustrative_tones_and_delta(self):
        s = _mech()["asymmetry_scorer_result"]
        assert s["openai_arm_tones"] == [-0.55]
        assert s["meta_arm_tones"] == [0.10]
        assert s["illustrative_delta_openai_minus_meta"] == -0.65
        assert s["method"] == "MANUAL ILLUSTRATIVE"

    def test_delta_math(self):
        s = _mech()["asymmetry_scorer_result"]
        calc = round(s["openai_arm_tones"][0] - s["meta_arm_tones"][0], 2)
        assert calc == s["illustrative_delta_openai_minus_meta"] == -0.65
        assert "(-0.55) - (0.10) = -0.65" in s["delta_calc"]

    def test_extends_598_and_507_framed(self):
        text = _block()
        assert "EXTENDS mechanism 598" in text
        assert "SECOND safety-crisis falsification" in text
        assert "EXTENDS mechanism 507" in text
        assert "domain boundary" in text

    def test_pairs_425_framed(self):
        text = _block()
        assert "PAIRS mechanism 425" in text
        assert "+0.46 thesis-consistent" in text
        assert "domain-bounded, not uniform" in text

    def test_deal_tie_counterdirectional(self):
        text = _block()
        assert "naive payer-softening prediction" in text
        assert "May 29 2024" in text
        assert "coverage_prediction" in text
        assert "softer" in text

    def test_stats_not_calculated(self):
        s = _mech()["asymmetry_scorer_result"]
        assert s["p_value"] == "NOT_CALCULATED"
        assert s["cohens_d"] == "NOT_CALCULATED"
        assert s["confidence_interval"] == "NOT_CALCULATED"
        assert s["is_significant"] is False


# ---------------------------------------------------------------------------
# 6. Confounders and counterevidence
# ---------------------------------------------------------------------------
class TestMechanism853Confounders:
    def test_confounders_ranked_strong_first(self):
        cs = _mech()["confounders"]
        assert len(cs) == 7
        strengths = [c.split(":")[0] for c in cs]
        assert strengths[:3] == ["STRONG"] * 3
        assert "Peg mismatch" in cs[0]
        assert "Excerpt-tier evidence" in cs[1]
        assert "Event-driven register" in cs[2]

    def test_counterevidence_three(self):
        ce = _mech()["counterevidence"]
        assert len(ce) == 3
        assert all(c.startswith("COUNTEREVIDENCE:") for c in ce)
        assert _mech()["verdict"] == "directionally_supported_not_proven"


# ---------------------------------------------------------------------------
# 7. Statistical discipline
# ---------------------------------------------------------------------------
class TestMechanism853Discipline:
    def test_statistical_discipline_qualitative_only(self):
        d = _mech()["statistical_discipline"]
        assert "MANUAL ILLUSTRATIVE scores only" in d
        assert "NOT run at the finding layer" in d
        assert "is_significant: false" in d

    def test_no_analysis_json_update(self):
        assert _mech()["no_analysis_json_update"] is True

    def test_not_artifact_grade(self):
        assert "NOT artifact-grade" in _mech()["statistical_discipline"]

    def test_falsification_member_thirty_second(self):
        f = _mech()["falsification_family"]
        assert "THIRTY-SECOND falsification-family member" in f
        assert "ledger 31->32" in f
        assert "Ledger holds at 32" in f
        assert "THIRTY-THIRD absent" in f

    def test_correlation_not_causation(self):
        text = _block()
        assert "Correlation is not causation" in text

    def test_connects_to(self):
        assert _mech()["connects_to"] == [507, 598, 425, 811, 827]

    def test_falsification_member_distinct_from_absent_guards(self):
        # Member-form wording per #1000, distinct from the "absent" guards in
        # other profiles (which carry "NOT a falsification-family member").
        text = _profiles_text()
        assert "THIRTY-SECOND falsification-family member" in text
        assert text.count("THIRTY-SECOND falsification-family member") == 1


# ---------------------------------------------------------------------------
# 8. Corpus novelty post-commit
# ---------------------------------------------------------------------------
class TestCorpusNoveltyPostCommit:
    def test_max_numeric_mechanism_id_is_853(self):
        ids = _corpus_ids()
        assert max(ids) == M_ID

    def test_zero_next_numeric_854_in_profiles(self):
        text = "\n".join(
            _read(os.path.join(root, fn))
            for root, _, files in os.walk(os.path.join(REPO_ROOT, "profiles"))
            for fn in files
            if fn.endswith(".yaml")
        )
        assert NEXT_NUMERIC not in text

    def test_zero_next_underscore_dash_854_repo_wide(self):
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

    def test_readme_row_1037(self):
        text = _read("README.md")
        assert f"`tests/{OWN_BASENAME}`" in text
        assert "Type A #1037" in text

    def test_architecture_row(self):
        text = _read("docs/ARCHITECTURE.md")
        assert OWN_BASENAME in text

    def test_iteration_log_entry(self):
        text = _read("iteration-log.md")
        assert "## #1037 Type A:" in text


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
