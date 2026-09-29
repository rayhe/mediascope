"""Type B -- Iteration #1068 (Tue 2026-09-29 05:00 PDT): Cherlynn Low (Engadget) Apple Watch Series 12 Audio Intelligence permissive register vs Meta Glasses hands-on warm register - register constancy (mechanism 872).

1065-1069 window, fourth leg D->E->A->B->C - Sep 29 2026 05:00 AM PDT.

Novelty: zero test_type_b_1068 files; no "Type B #1068" in git log; max numeric
mechanism_id 871 pre-commit; zero underscore-form 872 keys repo-wide pre-commit
(format-built needles per #715); zero dash-form 872 keys repo-wide pre-commit;
zero cherlynn_low YAML key in profiles/careers/journalists.yaml pre-commit (per
the #643 convention); block key zero-hit. FIRST dedicated Type B mechanism on
Cherlynn Low in journalists.yaml (prior corpus treatment is m150 in
profiles/competitor-coverage-research.yaml: her Jun-2026 Meta Glasses hands-on
and AWE Snap Specs liveblog as a beat-assignment control case).

Finding: within-journalist register CONSTANCY (null asymmetry) - TEMPORAL
EXTENSION of m150's control-case finding to a third entity (Apple) and a new
sensor modality (always-listening audio). APPLE ARM (carried from m1008/m1043's
source set, re-read first-hand this run, 95 rendered lines): Low's Sep 9/10
2026 Apple Watch Series 12 hands-on states the permissive principle explicitly
- "I'm also not against AI wearables that listen to your surroundings and
conversations, as long as done responsibly and with accountability, so I'm
intrigued by things like Siri Recap and Live Rewind" - accepts Apple's denial
"(Short answer: No.)", careful secure-exclave privacy-architecture relay;
MANUAL ILLUSTRATIVE +0.35. META ARM (carried from m150 with disclosure,
re-read first-hand this run, 111 rendered lines): Low's Jun 23 2026 Meta
Glasses hands-on - warm, playful, fashion-forward ("slightly obsessed with the
Starfire style", "I left the event mostly pleased"), ZERO privacy/surveillance
vocabulary across the full text despite 3K video cameras and multi-array mics,
bounded honest caveats (battery 96 to 66 percent in an hour, "most of the
features here aren't novel", AI misrecognition); MANUAL ILLUSTRATIVE +0.30.
Illustrative delta (Apple minus Meta) +0.05 = 0.35 - 0.30: no cross-entity
asymmetry detected. If anything the scrutiny asymmetry runs Meta-favorable:
the Apple piece carries a dedicated "Audio Intelligence, AI and privacy
concerns" section while the Meta piece has no privacy section at all. STRONG
confounder: 11-week temporal gap (Jun 23 vs Sep 9/10). Counterevidence: her
own Sep-17 Apple Watch review headline ("Catching up and catching heat",
"controversial audio features") is more adversarial than the hands-on; m150's
AWE liveblog amplified Spiegel's anti-Meta "copycats up north" dig. NOT a
falsification-family member, ledger holds at 35. MANUAL ILLUSTRATIVE ONLY,
engine NOT run, no analysis.json, NOT artifact-grade, verdict
directionally_supported_not_proven. Correlation is not causation.

Test tally: 56 tests, 13 classes.
"""

import os
import re
import subprocess

import yaml

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OWN_BASENAME = os.path.basename(__file__)
PROFILE = "profiles/careers/journalists.yaml"
JOURNALIST_KEY = "cherlynn_low"
MECH_KEY = "type_b_1068_cherlynn_low_engadget_apple_watch_audio_intelligence_vs_meta_glasses_hands_on_register_constancy_sep29"
M_ID = 872
OWN_M_ID = 872  # own mechanism for this file's structure tests; M_ID tracks the corpus max
ITER = 1068
TYPE_LETTER = "B"
RUN_PDT = "2026-09-29 05:00 PDT"
MECH_ID_MARKER = "mechanism" + "_872"  # own-mechanism marker (underscore form)
NEXT_US = "mechanism" + "_873"  # next-number underscore sweep
NEXT_DASH = "mechanism" + "-873"  # next-number dash sweep
NEXT_NUMERIC = "mechanism_id: " + "873"  # next-number numeric sweep
OWN_STAGED_SET = {
    "profiles/careers/journalists.yaml",
    "tests/test_type_b_1068_cherlynn_low_engadget_apple_watch_audio_intelligence_vs_meta_glasses_hands_on_register_constancy_sep29_5am.py",
    "README.md",
    "docs/ARCHITECTURE.md",
    "iteration-log.md",
}
INFLIGHT = {
    "profiles/nytimes.yaml",  # #899
    "tests/test_type_b_938_dominic_preston_verge_pixel_watch_gemini_personalization_vs_meta_luna_stigma_sep16.py",  # #938
    "tests/test_type_d_900_m769_qualitative_corpus_integrity_sep21_1pm.py",  # #900
    "tests/test_type_a_1012_mittr_anthropic_sep2026_doomer_turn_agenda_setting_register_vs_carried_meta_india_havoc_m817_pairing_sep26_7am.py",  # #1012-wt
}
ANCHORED_SHA = "0" * 40  # patched in the anchor followup per #565

EXPECTED_ORDER = [("B", "1068"), ("A", "1067"), ("E", "1066"), ("D", "1065"), ("C", "1064")]
EXPECTED_TESTS = 56

# Evidence URLs, verbatim Full-URL listings from this run's browser.search sets.
APPLE_URL = "https://www.engadget.com/2254467/apple-watch-series-12-hands-on-siri-recap-transcribe-live-rewind-health-sensing/"
META_URL = "https://www.engadget.com/2199519/meta-ai-glasses-hands-on-kylie-jenner-edition/"
AUTHOR_URL = "https://www.engadget.com/author/cherlynn-low/"


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
    # cherlynn_low is the last key in journalists.yaml; the block runs to EOF.
    text = _profiles_text()
    key = JOURNALIST_KEY + ":"
    start = text.index("\n" + key)
    return text[start:]


def _journalist():
    d = yaml.safe_load(_profiles_text())
    return d[JOURNALIST_KEY]


def _mech():
    return _journalist()["competitor_coverage"][MECH_KEY]


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
class TestNoveltyAnchorTypeB1068:
    def test_single_test_type_b_1068_file(self):
        files = [
            fn
            for fn in os.listdir(os.path.join(REPO_ROOT, "tests"))
            if fn.startswith("test_type_b_1068")
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
            "zero test_type_b_1068 files",
            "max numeric mechanism_id 871 pre-commit",
            "block key zero-hit",
            "FIRST dedicated Type B mechanism on Cherlynn Low",
            "Apple Watch Series 12",
        ):
            assert claim in doc.replace("\n", " ")


# ---------------------------------------------------------------------------
# 2. Rotation guard: 1065-1069 window, fourth leg D->E->A->B->C
# ---------------------------------------------------------------------------
class TestRotationGuard1065_1069Window:
    ORDER = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}

    def test_window_is_1065_1069_fourth_leg(self):
        # Deselected pre-commit per #565: this run's own main commit does not
        # exist yet; goes green post-commit.
        assert _window() == EXPECTED_ORDER

    def test_rotation_adjacency_cycle_valid(self):
        window = [p for p in _window() if int(p[1]) >= 1064]
        assert len(window) >= 4, window
        for (t1, n1), (t2, n2) in zip(window, window[1:]):
            assert int(n1) == int(n2) + 1
            assert (self.ORDER[t1] - self.ORDER[t2]) % 5 == 1, (t1, t2)

    def test_predecessor_is_type_a_1067(self):
        # Deselected pre-commit per #565 alongside the window-order test.
        order = _window()
        assert order[1] == ("A", "1067")
        r = run_git("log", "--grep", "Type A #1067:", "--format=%H", "--no-merges")
        assert r.stdout.strip(), "no Type A #1067 main commit found"

    def test_exactly_one_type_b_1068_main_commit(self):
        # Deselected pre-commit per #565 alongside the window-order test.
        r = run_git("log", "--grep", "Type B #1068:", "--format=%H", "--no-merges")
        assert len(r.stdout.split()) == 1, "expected exactly one Type B #1068 main commit"


# ---------------------------------------------------------------------------
# 3. Mechanism 872 block structure
# ---------------------------------------------------------------------------
class TestMechanism872Structure:
    def test_journalist_key_present(self):
        d = yaml.safe_load(_profiles_text())
        assert JOURNALIST_KEY in d

    def test_block_key_indent_4_under_competitor_coverage(self):
        text = _profiles_text()
        assert "  competitor_coverage:\n" in _block()
        assert "    " + MECH_KEY + ":" in text

    def test_block_key_descriptive_no_872(self):
        assert "872" not in MECH_KEY
        assert MECH_KEY == (
            "type_b_1068_cherlynn_low_engadget_apple_watch_audio_intelligence_"
            "vs_meta_glasses_hands_on_register_constancy_sep29"
        )

    def test_iteration_fields_1068_b(self):
        m = _mech()
        assert m["mechanism_id"] == OWN_M_ID
        assert m["iteration"] == ITER
        assert m["type"] == TYPE_LETTER
        assert m["date"] == RUN_PDT
        assert m["scheduled_job_id"] == "mediascope-daily-iteration"
        assert m["goal_id"] == "goal_54093bda4145"
        assert m["author"] == "Kit (with Ray)"

    def test_mechanism_ids_carries_872(self):
        assert 872 in _journalist()["mechanism_ids"]

    def test_test_file_points_at_own_basename(self):
        assert _mech()["test_file"] == "tests/" + OWN_BASENAME

    def test_block_key_field_matches(self):
        assert _mech()["block_key"] == MECH_KEY

    def test_no_analysis_json_update(self):
        assert _mech()["no_analysis_json_update"] is True


# ---------------------------------------------------------------------------
# 4. Mechanism 872 arms
# ---------------------------------------------------------------------------
class TestMechanism872Arms:
    def test_apple_arm_url_verbatim(self):
        assert _mech()["apple_url"] == APPLE_URL

    def test_meta_arm_url_verbatim(self):
        assert _mech()["meta_url"] == META_URL
        assert _mech()["author_url"] == AUTHOR_URL

    def test_apple_arm_carried_with_reread_disclosure(self):
        arm = _mech()["apple_arm"]
        assert "carried from m1008/m1043" in arm
        assert "re-read first-hand this run" in arm

    def test_meta_arm_carried_with_disclosure(self):
        arm = _mech()["meta_arm"]
        assert "carried from m150 with disclosure" in arm
        assert "re-read first-hand this run" in arm

    def test_apple_arm_permissive_principle_quoted(self):
        arm = _mech()["apple_arm"]
        assert "not against AI wearables that listen to your surroundings" in arm
        assert "Short answer: No." in arm

    def test_meta_arm_zero_privacy_vocabulary_claim(self):
        arm = _mech()["meta_arm"]
        assert "ZERO privacy/surveillance vocabulary" in arm
        assert "slightly obsessed with the Starfire style" in arm

    def test_both_arms_same_writer_outlet_genre(self):
        design = _mech()["design"]
        assert "Same writer, same outlet, same genre (hands-on), both wearables" in design


# ---------------------------------------------------------------------------
# 5. Mechanism 872 scorer
# ---------------------------------------------------------------------------
class TestMechanism872Scorer:
    def test_apple_score_plus_035(self):
        assert "+0.35" in _mech()["apple_arm"]

    def test_meta_score_plus_030(self):
        assert "+0.30" in _mech()["meta_arm"]

    def test_delta_apple_minus_meta_005(self):
        assert _mech()["illustrative_delta_apple_minus_meta"] == 0.05

    def test_delta_calc_exact(self):
        assert "0.35 - 0.30 = 0.05" in _mech()["delta_calc"]

    def test_manual_illustrative_both_arms(self):
        assert "MANUAL ILLUSTRATIVE +0.35" in _mech()["apple_arm"]
        assert "MANUAL ILLUSTRATIVE +0.30" in _mech()["meta_arm"]

    def test_meta_favorable_scrutiny_nuance(self):
        assert "Meta-favorable" in _mech()["delta_calc"]


# ---------------------------------------------------------------------------
# 6. Mechanism 872 confounders and counterevidence
# ---------------------------------------------------------------------------
class TestMechanism872Confounders:
    def test_four_confounders_ranked(self):
        assert len(_mech()["confounders_ranked"]) == 4

    def test_strongest_confounder_temporal_gap(self):
        first = _mech()["confounders_ranked"][0]
        assert first.startswith("STRONG")
        assert "11-week temporal gap" in first

    def test_three_counterevidence_items(self):
        assert len(_mech()["counterevidence"]) == 3

    def test_review_headline_caveat_present(self):
        ce = " ".join(_mech()["counterevidence"])
        assert "Catching up and catching heat" in ce
        assert "controversial audio features" in ce

    def test_m150_liveblog_counterevidence_present(self):
        ce = " ".join(_mech()["counterevidence"])
        assert "copycats up north" in ce


# ---------------------------------------------------------------------------
# 7. Statistical discipline
# ---------------------------------------------------------------------------
class TestMechanism872Discipline:
    def test_manual_illustrative_only(self):
        disc = _mech()["statistical_discipline"]
        assert "MANUAL_ILLUSTRATIVE" in disc
        assert "p_value NOT_CALCULATED" in disc
        assert "cohens_d NOT_CALCULATED" in disc
        assert "ci_95 NOT_CALCULATED" in disc
        assert "is_significant false" in disc

    def test_engine_not_run(self):
        assert "engine NOT run" in _mech()["statistical_discipline"]

    def test_verdict_directionally_supported(self):
        assert _mech()["verdict"].startswith("directionally_supported_not_proven")

    def test_correlation_not_causation(self):
        assert "Correlation is not causation" in __doc__

    def test_not_falsification_family_ledger_35(self):
        ff = _mech()["falsification_family"]
        assert "NOT a falsification-family member" in ff
        assert "ledger holds at 35" in ff

    def test_research_method_documents_sources(self):
        rm = _mech()["research_method"]
        assert "7 browser.search" in rm
        assert "5 browser.open" in rm
        assert "ASCII-only, no em dashes" in rm


# ---------------------------------------------------------------------------
# 8. Post-commit corpus novelty: 872 is max, 873 is zero
# ---------------------------------------------------------------------------
class TestCorpusNoveltyPostCommit:
    def test_max_numeric_mechanism_id_is_872(self):
        ids = _corpus_ids()
        assert max(ids) == M_ID

    def test_zero_next_numeric_873_in_profiles(self):
        base = os.path.join(REPO_ROOT, "profiles")
        for root, _, files in os.walk(base):
            for fn in files:
                if fn.endswith(".yaml"):
                    text = _read(os.path.join(root, fn))
                    assert NEXT_NUMERIC not in text

    def test_zero_next_underscore_dash_873_repo_wide(self):
        assert _repo_grep(NEXT_US) == []
        assert _repo_grep(NEXT_DASH) == []

    def test_four_cross_refs(self):
        assert len(_mech()["cross_refs"]) == 4


# ---------------------------------------------------------------------------
# 9. Doc-sync ratchet per #719 (README stats, row, ARCH row, log entry)
# ---------------------------------------------------------------------------
class TestDocSyncRatchet1068:
    def test_readme_stats_bumped(self):
        text = _read("README.md")
        assert "| Tests | 54813 | Across 1393 test files |" in text

    def test_readme_new_row(self):
        text = _read("README.md")
        assert "#1068" in text and "Cherlynn Low" in text

    def test_arch_tree_new_row(self):
        text = _read("docs/ARCHITECTURE.md")
        assert "1068" in text and "Cherlynn Low" in text

    def test_iteration_log_new_entry(self):
        text = _read("iteration-log.md")
        assert "Type B #1068" in text and "mechanism 872" in text


# ---------------------------------------------------------------------------
# 10. Targeted staging + in-flight isolation
# ---------------------------------------------------------------------------
class TestTargetedStaging1068:
    def test_staged_set_equals_own(self):
        # Fails pre-staging by design: only passes once the exact five
        # basenames are staged and nothing else.
        r = run_git("diff", "--cached", "--name-only")
        staged = {os.path.basename(p) for p in r.stdout.split()}
        assert staged == {
            "journalists.yaml",
            "test_type_b_1068_cherlynn_low_engadget_apple_watch_audio_intelligence_vs_meta_glasses_hands_on_register_constancy_sep29_5am.py",
            "README.md",
            "ARCHITECTURE.md",
            "iteration-log.md",
        }, staged

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
        assert "\u2013" not in text  # en dash
        assert "\u2014" not in text  # em dash
        text.encode("ascii")

    def test_docstring_ascii(self):
        __doc__.encode("ascii")


# ---------------------------------------------------------------------------
# 12. Guard carriers: underscore/dash 872 needles are pure zero post-commit
# ---------------------------------------------------------------------------
class TestGuardCarriersPinned:
    def test_underscore_872_pure_zero(self):
        # Own-mechanism underscore-form 872 needles are pure zero repo-wide:
        # the block uses the numeric field form and the new file builds its
        # 872 marker at runtime (per #715), so no contiguous literal exists.
        assert _repo_grep(MECH_ID_MARKER) == []

    def test_dash_872_pure_zero(self):
        dash = "mechanism" + "-872"
        assert _repo_grep(dash) == []


# ---------------------------------------------------------------------------
# 13. Journalist entry integrity
# ---------------------------------------------------------------------------
class TestJournalistEntryIntegrity:
    def test_name_role_publication(self):
        j = _journalist()
        assert j["name"] == "Cherlynn Low"
        assert j["current_role"] == "Executive Editor"
        assert j["current_publication"] == "Engadget"
        assert j["publication_owner"] == "Yahoo"

    def test_beat_includes_wearables(self):
        assert "wearables" in _journalist()["beat"]

    def test_single_competitor_coverage_block(self):
        cc = _journalist()["competitor_coverage"]
        assert list(cc) == [MECH_KEY]
