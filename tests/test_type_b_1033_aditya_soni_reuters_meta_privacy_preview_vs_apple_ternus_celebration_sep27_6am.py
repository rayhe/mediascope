"""Type B #1033 (Sep 27 2026, 06:00 PDT): Aditya Soni (Reuters, Bengaluru)
within-writer register asymmetry - Meta Connect privacy-hardened preview
(Sep 23 2026, -0.45 carried from m850 per #807) vs Apple Cook-to-Ternus
legacy-celebration piece (Sep 1 2026, +0.30 manual illustrative);
illustrative delta (Apple minus Meta) +0.75. The Reuters-Meta Oct 25 2024
content deal sits on Meta's side, so the spread runs OPPOSITE the naive
payer-softening prediction. Resolves m850's flagged writer-vs-desk
confounder within-writer.

Novelty verification (pre-commit, per #565 / #715):
- zero
test_type_b_1033 files (glob) in tests/
- max numeric
mechanism_id 850 across profiles/ (so 851 is next)
- block key zero-hit repo-wide (colon-form key, designed keying per #715)
- three relay URLs zero-hit repo-wide (froggyweb Meta corroboration relay,
getty.pp.ua Apple relay, northlandnewsradio foldable relay); the reuters.com
Meta canonical is carried from #1032, not novel
- no "Type B #1033" in git log (--grep) pre-commit

Anchored to main commit ANCHORED_SHA (patched post-commit per #565).

Test tally: 44 tests, 11 classes.
"""

import os
import re
import subprocess

import yaml

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OWN_BASENAME = os.path.basename(__file__)
JOURNALISTS_YAML = os.path.join(REPO_ROOT, "profiles", "careers", "journalists.yaml")

ITER = 1033
TYPE_LETTER = "B"
M_ID = 851
NEXT_NUMERIC = "852"
NEXT_US = "mechanism" + "_852"          # own-form forward marker; never literal in block
NEXT_DASH = "mechanism" + "-852"
MECH_ID_MARKER = "mechanism" + "_851"   # own-form marker; never literal in block
MECH_KEY = "type_b_1033_aditya_soni_reuters_meta_privacy_preview_vs_apple_ternus_celebration_sep27"
ANCHORED_SHA = "8b58e3c438caf4ce43fef3a58f4258984909d4ff"  # patched post-commit per #565

EXPECTED_ORDER = [("B", "1033"), ("A", "1032"), ("E", "1031"), ("D", "1030"), ("C", "1029")]

EXPECTED_URLS = [
    "https://www.reuters.com/business/meta-expected-unveil-smart-glasses-without-camera-privacy-concerns-grow-2026-09-23/",
    "https://froggyweb.com/2026/09/23/meta-expected-to-unveil-smart-glasses-without-camera-as-privacy-concerns-grow/",
    "https://latest.getty.pp.ua/blog/cook-hands-apple-to-ternus-bigger-and-richer-but-c-cook-hands-apple-ternus-bigger-101359000/",
    "https://northlandnewsradio.com/2026/09/09/as-apple-prepares-to-make-a-splash-a-brief-history-of-foldable-phones/",
]

INFLIGHT = frozenset(
    [
        "profiles/nytimes.yaml",
        "tests/test_type_a_1012_mittr_anthropic_sep2026_doomer_turn_agenda_setting_register_vs_carried_meta_india_havoc_m817_pairing_sep26_7am.py",
        "tests/test_type_b_938_dominic_preston_verge_pixel_watch_gemini_personalization_vs_meta_luna_stigma_sep16.py",
        "tests/test_type_d_900_m769_qualitative_corpus_integrity_sep21_1pm.py",
    ]
)

README_TESTS_BEFORE = 53012
README_TESTS_AFTER = 53056
README_FILES_BEFORE = 1357
README_FILES_AFTER = 1358
EXPECTED_TESTS = 44


def run_git(*args):
    return subprocess.run(
        ["git", "-C", REPO_ROOT, *args],
        capture_output=True,
        text=True,
        timeout=60,
    )


def _read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def _profiles_text():
    return _read(JOURNALISTS_YAML)


def _block():
    text = _profiles_text()
    start = text.index("    " + MECH_KEY + ":")
    rest = text[start:]
    m = re.search(r"^ {0,2}[a-z][a-z0-9_]*:$", rest, re.M)
    return rest[: m.start()] if m else rest


def _item():
    d = yaml.safe_load(_profiles_text())
    return d["aditya_soni"]


def _mech():
    return _item()["competitor_coverage"][MECH_KEY]


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
class TestNoveltyAnchorTypeB1033:
    def test_single_test_type_b_1033_file(self):
        files = [
            fn
            for fn in os.listdir(os.path.join(REPO_ROOT, "tests"))
            if fn.startswith("test_type_b_1033")
        ]
        assert files == [OWN_BASENAME]

    def test_anchor_sha_patched_post_commit(self):
        # Deselected pre-commit per #565: ANCHORED_SHA carries a placeholder
        # until the anchor followup patches it to the real main commit SHA.
        assert ANCHORED_SHA != "0" * 40
        assert re.fullmatch(r"[0-9a-f]{40}", ANCHORED_SHA)
        r = run_git("rev-parse", ANCHORED_SHA)
        assert r.returncode == 0 and r.stdout.strip() == ANCHORED_SHA

    def test_novelty_verification_claim(self):
        doc = __doc__
        for claim in (
            "zero\ntest_type_b_1033 files",
            "max numeric\nmechanism_id 850",
            "block key zero-hit",
            "three relay URLs zero-hit",
        ):
            assert claim.replace("\n", " ") in doc.replace("\n", " ")


# ---------------------------------------------------------------------------
# 2. Rotation guard: 1030-1034 window, fourth leg D->E->A->B
# ---------------------------------------------------------------------------
class TestRotationGuard1030_1034Window:
    ORDER = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}

    def test_window_is_1030_1034_fourth_leg(self):
        assert _window() == EXPECTED_ORDER

    def test_rotation_adjacency_cycle_valid(self):
        window = _window()
        for (t1, n1), (t2, n2) in zip(window, window[1:]):
            assert int(n1) == int(n2) + 1
            assert (self.ORDER[t1] - self.ORDER[t2]) % 5 == 1, (t1, t2)

    def test_predecessor_is_type_a_1032(self):
        order = _window()
        assert order[1] == ("A", "1032")
        r = run_git("log", "--grep", "Type A #1032:", "--format=%H", "--no-merges")
        assert r.stdout.strip(), "no Type A #1032 main commit found"

    def test_no_concurrent_inflight_commits_asserted(self):
        r = run_git("log", "--grep", "Type B #1033:", "--format=%H", "--no-merges")
        assert len(r.stdout.split()) == 1, "expected exactly one Type B #1033 main commit"


# ---------------------------------------------------------------------------
# 3. Mechanism 851 block structure
# ---------------------------------------------------------------------------
class TestMechanism851Structure:
    def test_block_key_exists_in_journalists_yaml(self):
        assert ("    " + MECH_KEY + ":") in _profiles_text()

    def test_block_key_unique(self):
        assert _profiles_text().count("    " + MECH_KEY + ":") == 1

    def test_iteration_and_type_and_time_pdt(self):
        m = _mech()
        assert m["iteration"] == ITER
        assert m["iteration_type"] == TYPE_LETTER
        assert m["mechanism_id"] == M_ID
        assert m["date"] == "2026-09-27 06:00 PDT"

    def test_journalist_and_entities(self):
        m = _mech()
        assert m["journalist"] == "Aditya Soni"
        assert m["publication"] == "Reuters"
        assert m["primary_entity"] == "Meta"
        assert m["comparator_entity"] == "Apple"
        assert m["finding_type"] == "journalist_cross_entity_register_asymmetry"

    def test_designed_keying_no_underscore_851_in_block_key(self):
        assert "851" not in MECH_KEY
        assert MECH_ID_MARKER not in MECH_KEY
        assert "mechanism_id: 851" in _block()


# ---------------------------------------------------------------------------
# 4. Arms: Meta Connect preview vs Apple Cook-to-Ternus piece
# ---------------------------------------------------------------------------
class TestMechanism851Arms:
    def test_one_meta_arm_one_apple_arm(self):
        m = _mech()
        assert set(m.keys()) >= {"meta_arm", "apple_arm"}
        assert isinstance(m["meta_arm"], dict)
        assert isinstance(m["apple_arm"], dict)

    def test_meta_arm_metadata(self):
        arm = _mech()["meta_arm"]
        assert arm["title"] == "Meta expected to unveil smart glasses without camera as privacy concerns grow"
        assert arm["date"] == "2026-09-23"
        assert arm["register"] == "privacy_hardened_product_preview"
        assert arm["tone_illustrative"] == -0.45
        assert "Aditya Soni" in arm["byline"]

    def test_meta_key_language_verbatim(self):
        quotes = _mech()["meta_arm"]["evidence_quotes"]
        assert any("covertly record people" in q for q in quotes)
        assert any("changing clothes" in q for q in quotes)

    def test_apple_arm_metadata(self):
        arm = _mech()["apple_arm"]
        assert arm["title"] == "Cook hands Apple to Ternus: bigger and richer, but catching up in AI race"
        assert arm["date"] == "2026-09-01"
        assert arm["register"] == "legacy_celebration_leadership_transition"
        assert arm["tone_illustrative"] == 0.30
        assert "Aditya Soni" in arm["byline"]

    def test_apple_key_language_verbatim(self):
        quotes = _mech()["apple_arm"]["evidence_quotes"]
        assert any("$4.5 trillion behemoth" in q for q in quotes)
        assert any("most consequential CEO tenures ever" in q for q in quotes)
        assert any("catching up in AI race" in q for q in quotes)

    def test_all_source_urls_verbatim(self):
        assert _item()["source_urls"] == EXPECTED_URLS
        assert _mech()["meta_arm"]["url_attestation"]
        assert _mech()["apple_arm"]["url_attestation"]

    def test_zero_browser_open_attested(self):
        text = _block()
        assert "0 browser.open" in text


# ---------------------------------------------------------------------------
# 5. Asymmetry scorer
# ---------------------------------------------------------------------------
class TestMechanism851Scorer:
    def test_illustrative_tones_and_delta(self):
        s = _mech()["asymmetry_scorer_result"]
        assert s["illustrative_meta_arm_tone"] == -0.45
        assert s["illustrative_apple_arm_tone"] == 0.30
        assert s["illustrative_cross_entity_delta_apple_minus_meta"] == 0.75

    def test_delta_math(self):
        s = _mech()["asymmetry_scorer_result"]
        calc = round(s["illustrative_apple_arm_tone"] - s["illustrative_meta_arm_tone"], 2)
        assert calc == s["illustrative_cross_entity_delta_apple_minus_meta"] == 0.75
        assert "+0.30 minus (-0.45) = +0.75" in s["delta_calc"]

    def test_extends_850_framed(self):
        text = _block()
        assert "EXTENDS mechanism 850" in text
        assert "within-writer" in text

    def test_payer_tie_counterdirectional(self):
        text = _block()
        assert "Oct 25 2024" in text
        assert "OPPOSITE the naive payer-softening prediction" in text

    def test_incentive_context_names_soni_deal_role(self):
        text = _block()
        assert "self-report" in text

    def test_stats_not_calculated(self):
        s = _mech()["asymmetry_scorer_result"]
        assert s["p_value"] == "NOT_CALCULATED"
        assert s["cohens_d"] == "NOT_CALCULATED"
        assert s["ci_95"] == "NOT_CALCULATED"
        assert _mech()["is_significant"] is False


# ---------------------------------------------------------------------------
# 6. Confounders and counterevidence
# ---------------------------------------------------------------------------
class TestMechanism851Confounders:
    def test_confounders_ranked_strong_first(self):
        cs = _mech()["confounders_ranked"]
        assert len(cs) == 8
        strengths = [c.split(":")[0] for c in cs]
        assert strengths[:3] == ["STRONG"] * 3
        assert "Story-type asymmetry" in cs[0]
        assert "Event-driven register" in cs[1]

    def test_counterevidence_four(self):
        ce = _mech()["counterevidence"]
        assert len(ce) == 4
        assert _mech()["verdict"] == "directionally_supported_not_proven"


# ---------------------------------------------------------------------------
# 7. Statistical discipline
# ---------------------------------------------------------------------------
class TestMechanism851Discipline:
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
        f = _mech()["falsification_note"]
        assert "NOT a falsification-family member" in f
        assert "Ledger holds at 31" in f

    def test_correlation_not_causation(self):
        text = _block()
        assert "Correlation is not causation" in text

    def test_connects_to(self):
        assert _mech()["connects_to"] == [850, 844, 739, 664, 633]

    def test_test_file_and_research_method(self):
        m = _mech()
        assert m["test_file"] == "tests/" + OWN_BASENAME
        assert "0 browser.open" in m["research_method"]
        assert "6 browser.search query sets" in m["research_method"]


# ---------------------------------------------------------------------------
# 8. Corpus novelty post-commit
# ---------------------------------------------------------------------------
class TestCorpusNoveltyPostCommit:
    def test_max_numeric_mechanism_id_is_851(self):
        ids = _corpus_ids()
        assert max(ids) == M_ID

    def test_zero_next_mechanism_id_852_in_profiles(self):
        # Raw "852" collides pre-existing iteration numbers (e.g. iteration: 852)
        # and connects_to refs, so the forward-collision vector is the colon
        # form actually consumed by _corpus_ids().
        text = "\n".join(
            _read(os.path.join(root, fn))
            for root, _, files in os.walk(os.path.join(REPO_ROOT, "profiles"))
            for fn in files
            if fn.endswith(".yaml")
        )
        assert "mechanism_id: 852" not in text
        assert "mechanism: 852" not in text

    def test_zero_next_underscore_dash_852_repo_wide(self):
        assert _repo_grep(NEXT_US) == []
        assert _repo_grep(NEXT_DASH) == []


# ---------------------------------------------------------------------------
# 9. Doc-sync ratchet per #719 (green post-doc-sync)
# ---------------------------------------------------------------------------
class TestDocSyncRatchet:
    def test_readme_header_stats_bumped(self):
        text = _read(os.path.join(REPO_ROOT, "README.md"))
        assert str(README_TESTS_AFTER) in text
        assert str(README_FILES_AFTER) in text

    def test_readme_row_1033(self):
        text = _read(os.path.join(REPO_ROOT, "README.md"))
        assert f"`tests/{OWN_BASENAME}`" in text
        assert "Type B #1033" in text

    def test_architecture_row(self):
        text = _read(os.path.join(REPO_ROOT, "docs/ARCHITECTURE.md"))
        assert OWN_BASENAME in text

    def test_iteration_log_entry(self):
        text = _read(os.path.join(REPO_ROOT, "iteration-log.md"))
        assert "## #1033 Type B:" in text


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
