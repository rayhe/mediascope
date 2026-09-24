"""Type B iteration #953 (Sep 23 2026, 7pm PDT): Katie Notopoulos
(Business Insider senior correspondent) Meta glasses vs Apple Watch Audio
Intelligence register constancy (mechanism 803), the fourth leg of the
950-954 window.

D #950 -> E #951 -> A #952 -> B #953 -> C (#954 to follow).

FINDING: Katie Notopoulos (Business Insider, senior correspondent,
technology and culture) applies an entity-neutral register to Meta and
Apple ambient-sensing wearables in the same week (Sep 9-18 2026): a
constancy case that BOUNDS the differential thesis. Her Sep 9 2026
first-person Apple Watch piece "The new Apple Watch can listen in on
your conversations and take notes. That makes me feel weird." (byline
attested via her Muck Rack author page and a Flipboard "Business
Insider - By Katie Notopoulos" listing; BI original paywalled, so the
piece was read via a full-text relay mirror, exceeding the #503 excerpt
floor) hedges hard: Siri Recap / Live Rewind are "convenient and cool,
but also a little ... weird" and "very un-Appley"; she concedes "you
can turn this off", "it doesn't store raw audio recordings", and
"end-to-end encryption", and ends "I don't feel like an eavesdropper
wearing an Apple Watch. Unstylish, maybe, but not creepy." Her Meta
arms the same week: (1) the Sep 16-18 Bosworth AMA report "Meta's CTO
doesn't want a few 'bad actors' to spoil your view of Meta glasses"
(carried executive-defense relay, mechanism 745, un-rescored per #807,
+0.10); (2) "Meta bricked the cameras on thousands of its AI glasses"
(byline via the same Muck Rack author page; enforcement-news register:
Meta software-bricks cameras when the recording-indicator light is
covered or removed) -0.15. MANUAL ILLUSTRATIVE only: Meta arm avg
(+0.10 + -0.15)/2 = -0.025 vs Apple arm 0.00, illustrative cross-entity
constancy delta -0.025, inside the neutral band. p_value/cohens_d/ci_95
NOT_CALCULATED, is_significant False, engine NOT run, NOT
artifact-grade. Verdict directionally_supported_not_proven; NOT a
falsification-family member; ledger holds at 29. Distinct from #948
(Gorringe): Gorringe's constancy sits in the adversarial band (-0.55 /
-0.60); Notopoulos's sits in the neutral band. This is a second,
register-neutral writer-level control: the journalist who proved the
Meta LED could be taped over in 2021 (BuzzFeed) still writes both
entities in the neutral register in Sep 2026, so neutral Meta coverage
alone does not imply a differential.

Novelty verified pre-commit (zero test_type_b_953 files; no 'Type B
#953' in git log; max numeric mechanism_id 802; zero underscore-form
803 keys per #715; block key zero-hit repo-wide; katie_notopoulos key
zero-hit repo-wide (Katie Drummond hits are a different person); the
Muck Rack profile URL and the full-text relay URL zero-hit repo-wide; 2
browser.search query sets + 2 browser.open first-hand reads this run);
count_stats gate (delta = this file exactly); 950-954 window fourth leg
D->E->A->B (anchor + rotation deselected pre-commit per #565, patched
green in the anchor followup).
"""

import glob
import os
import re
import subprocess
from functools import lru_cache

import pytest
import yaml

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TESTS_DIR = os.path.join(REPO, "tests")
OWN_BASENAME = "test_type_b_953_katie_notopoulos_bi_meta_glasses_vs_apple_watch_audio_constancy_sep23_7pm.py"
RUN_PDT = "2026-09-23 19:00 PDT"

# Concatenated so this file never contains the literal marker itself.
MECH_ID_MARKER = "mechanism" + "_803"
NEXT_ID_MARKER = "mechanism" + "_804"
NEXT_ID_NUMERIC = "mechanism_id: " + "804"
EXPECTED_ORDER = [("B", "953"), ("A", "952"), ("E", "951"), ("D", "950"), ("C", "949")]
# Patched to the real main-commit SHA in the anchor followup per #565.
ANCHORED_SHA = "4755fa180e9aa3e9f6edcf9a683027599589ff6a"

BLOCK_KEY = (
    "katie_notopoulos_bi_apple_watch_audio_unease_"
    "vs_meta_glasses_neutral_constancy_sep23"
)
JOURNALIST_KEY = "katie" + "_" + "notopoulos"
JOURNALIST_SUB_KEY = (
    "type_b_953_katie_notopoulos_bi_meta_glasses_"
    "vs_apple_watch_audio_constancy_sep23_7pm"
)

META_TONE_AMA_CARRIED = 0.10  # mechanism 745, un-rescored per #807
META_TONE_BRICKED = -0.15     # fresh arm, enforcement-news register
META_TONE_AVG = -0.025        # (0.10 + -0.15) / 2
APPLE_TONE = 0.00             # hedged first-person unease, balanced
CONSTANCY_DELTA = -0.025      # -0.025 - 0.00; near-zero = neutral band

# Doc-sync ratchet: this file's own test count and the repo totals it
# implies (README 49021/1277 -> after). Verified via .venv collect-only
# before the doc-sync edits.
THIS_FILE_TEST_COUNT = 83
README_TESTS_BEFORE = 49021
README_FILES_BEFORE = 1277
README_TESTS_AFTER = 49104
README_FILES_AFTER = 1278

EXPECTED_URLS = [
    "https://muckrack.com/katienotopoulos/articles",
    "https://cncbnews.com/article/2026/09/the-new-apple-watch-can-listen-in-on-your-conversations-and-take-notes-that-makes-me-feel-weird",
]

PROFILE = os.path.join(REPO, "profiles", "competitor-coverage-research.yaml")
JOURNALISTS = os.path.join(REPO, "profiles", "careers", "journalists.yaml")
README_PATH = os.path.join(REPO, "README.md")
ARCH_PATH = os.path.join(REPO, "docs", "ARCHITECTURE.md")
LOG_PATH = os.path.join(REPO, "iteration-log.md")


def _git(*args):
    return subprocess.run(
        ["git", "-C", REPO] + list(args),
        capture_output=True, text=True, timeout=120,
    )


def _read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


@lru_cache(maxsize=1)
def _block():
    # Cached: the profile YAML is ~31k lines and a single parse takes
    # ~3.5s, so re-parsing per test made the file take 4+ minutes.
    doc = yaml.safe_load(_read(PROFILE))
    return doc["publications"][BLOCK_KEY]


def _corpus_ids():
    ids = []
    for root, _, files in os.walk(os.path.join(REPO, "profiles")):
        for fn in files:
            if not fn.endswith(".yaml"):
                continue
            text = _read(os.path.join(root, fn))
            ids += [int(x) for x in re.findall(r"mechanism_id:\s*(\d+)", text)]
    return ids


def _repo_grep(needle, roots=("profiles", "tests")):
    hits = []
    for r in roots:
        base = os.path.join(REPO, r)
        for root, _, files in os.walk(base):
            for fn in files:
                if fn.rsplit(".", 1)[-1] not in ("py", "yaml", "md", "json"):
                    continue
                p = os.path.join(root, fn)
                if "__pycache__" in p:
                    continue
                try:
                    if needle in _read(p):
                        hits.append(os.path.relpath(p, REPO))
                except OSError:
                    pass
    return hits


def _window(n=40):
    # First occurrence of each distinct iteration number, newest first
    # (robust to followup commits that repeat the same "Type X #N" wording
    # without the colon, per the #752 convention).
    subjects = _git("log", f"-{n}", "--format=%s", "--no-merges").stdout.splitlines()
    seen_nums = set()
    out = []
    for s in subjects:
        m = re.match(r"Type ([A-E]) #(\d+):", s)
        if m and m.group(2) not in seen_nums:
            seen_nums.add(m.group(2))
            out.append(m.groups())
    return out[:5]


# --------------------------------------------------------------------------
# 1. Novelty anchor (deselected pre-commit per #565, patched green post-commit)
# --------------------------------------------------------------------------
class TestNoveltyAnchorTypeB953:
    @pytest.mark.anchor
    def test_anchor_sha_patched_post_commit(self):
        # No #953 main commit exists pre-commit; the anchor test pins
        # the main commit SHA once the followup patches ANCHORED_SHA.
        # Deselected pre-commit per #565; patched green in the anchor
        # followup.
        result = _git("log", "--format=%H %s", "--", "tests/" + OWN_BASENAME)
        assert result.returncode == 0
        mains = [
            line for line in result.stdout.splitlines()
            if "Type B #953" in line and "followup" not in line.lower()
        ]
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
            "PATCH_ME_IN_FOLLOWUP_PER_565",
        ) or mains == []
        if mains:
            assert mains[0].startswith(ANCHORED_SHA + " "), mains

    @pytest.mark.anchor
    def test_exactly_one_type_b_953_file_on_disk(self):
        files = glob.glob(os.path.join(TESTS_DIR, "*type_b_953*"))
        assert len(files) == 1 and os.path.basename(files[0]) == OWN_BASENAME

    def test_max_numeric_mechanism_id_803_post_commit(self):
        # This run ADDS mechanism 803: post-commit max is 803, zero 804
        # keys anywhere. Pre-commit sweeps verified max 802, zero
        # underscore-form 803 keys (designed keying per #715), block key
        # zero-hit, katie_notopoulos key zero-hit (Katie Drummond hits are
        # a different person), Muck Rack profile URL and relay URL
        # zero-hit repo-wide.
        assert max(_corpus_ids()) == 803
        assert _repo_grep(NEXT_ID_MARKER) == []
        assert _repo_grep(NEXT_ID_NUMERIC, roots=("profiles",)) == []


# --------------------------------------------------------------------------
# 2. Rotation guard, 950-954 window (deselected pre-commit per #565)
# --------------------------------------------------------------------------
class TestRotationGuard950_954Window:
    ORDER = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}

    @pytest.mark.rotation
    def test_window_is_950_954_fourth_leg(self):
        # Deselected pre-commit per #565 (the #953 main commit does not
        # exist yet); patched green in the anchor followup.
        window = _window()
        assert window[:4] == EXPECTED_ORDER[:4], (
            f"950-954 window fourth leg D->E->A->B: expected {EXPECTED_ORDER[:4]}, "
            f"got {window[:4]}"
        )

    @pytest.mark.rotation
    def test_rotation_adjacency_cycle_valid(self):
        # Deselected pre-commit per #565; patched green in the followup.
        window = _window()
        for (t1, n1), (t2, n2) in zip(window[:4], window[1:5]):
            assert int(n1) == int(n2) + 1
            assert (self.ORDER[t1] - self.ORDER[t2]) % 5 == 1, (t1, t2)

    @pytest.mark.rotation
    def test_predecessor_is_type_a_952(self):
        # Deselected pre-commit per #565; patched green in the followup.
        window = _window()
        assert window[1] == ("A", "952"), (
            f"immediate predecessor must be Type A #952, got {window[1]}"
        )

    def test_950_952_window_legs_present_in_log(self):
        log = _read(LOG_PATH)
        for marker in ("## #950 Type D:", "## #951 Type E:", "## #952 Type A:"):
            assert marker in log, marker


# --------------------------------------------------------------------------
# 3. Mechanism 803 structure
# --------------------------------------------------------------------------
class TestMechanism803Structure:
    def test_block_key_exists_under_publications(self):
        doc = yaml.safe_load(_read(PROFILE))
        assert BLOCK_KEY in doc["publications"]

    def test_mechanism_id_is_803(self):
        assert _block()["mechanism_id"] == 803

    def test_type_is_b(self):
        assert _block()["type"] == "B"

    def test_iteration_953(self):
        assert _block()["iteration"] == 953
        assert _block()["iteration_time"] == RUN_PDT

    def test_rotation_window_leg(self):
        assert _block()["rotation_window"] == "950-954"
        assert "D #950 -> E #951 -> A #952 -> B #953" in _block()["window_leg"]

    def test_journalist_and_publication(self):
        assert _block()["journalist"] == "Katie Notopoulos"
        assert _block()["publication"] == "Business Insider"

    def test_competitor_and_reference(self):
        assert _block()["competitor"] == "Apple"
        assert _block()["reference_entity"] == "Meta"

    def test_is_not_significant(self):
        assert _block()["is_significant"] is False

    def test_no_analysis_json_update(self):
        assert _block()["no_analysis_json_update"] is True

    def test_verdict_discipline(self):
        assert _block()["verdict"] == "directionally_supported_not_proven"
        assert _block()["correlation_not_causation"] is True

    def test_connects_to_745(self):
        # The carried Bosworth AMA arm (mechanism 745) is a hard link.
        assert 745 in _block()["connects_to"]

    def test_ledger_holds_at_29(self):
        assert "29" in _block()["ledger"]
        assert "falsification" in _block()["falsification_family"].lower()


# --------------------------------------------------------------------------
# 4. Meta arm evidence
# --------------------------------------------------------------------------
class TestMetaArmEvidence:
    def _evidence(self):
        return " ".join(_block()["evidence"]).lower()

    def test_ama_arm_carried_from_745(self):
        assert "745" in self._evidence()

    def test_ama_arm_not_rescored(self):
        # Per #807: carried comparator arms are un-rescored.
        assert "807" in self._evidence()

    def test_ama_headline_present(self):
        assert "bad actors" in self._evidence()

    def test_ama_tone_carried_at_plus_010(self):
        assert "+0.10" in self._evidence()

    def test_bricked_cameras_arm_present(self):
        assert "bricked the cameras" in self._evidence()

    def test_bricked_cameras_register_is_enforcement_news(self):
        assert "enforcement" in self._evidence()

    def test_bricked_arm_led_tamper_detail(self):
        assert "indicator" in self._evidence()

    def test_meta_arm_excerpt_bounded(self):
        assert "503" in self._evidence()


# --------------------------------------------------------------------------
# 5. Apple arm evidence
# --------------------------------------------------------------------------
class TestAppleArmEvidence:
    def _evidence(self):
        return " ".join(_block()["evidence"])

    def test_apple_headline_present(self):
        assert "listen in on your conversations" in self._evidence()

    def test_apple_piece_date_sep_9(self):
        assert "Sep 09 2026" in self._evidence() or "September 09, 2026" in self._evidence()

    def test_apple_byline_via_muck_rack(self):
        assert "Muck Rack" in self._evidence()

    def test_apple_byline_flipboard_attribution(self):
        assert "Flipboard" in self._evidence()

    def test_hedged_register_quoted(self):
        assert "very un-Appley" in self._evidence()

    def test_concession_quoted(self):
        assert "turn this off" in self._evidence()

    def test_not_creepy_quote(self):
        assert "not creepy" in self._evidence()

    def test_apple_arm_no_villain_vocabulary(self):
        finding = _block()["finding"].lower()
        for word in ("perv", "villain", "criminal"):
            assert word not in finding, word

    def test_apple_arm_first_person(self):
        assert "first-person" in self._evidence()

    def test_relay_mirror_provenance(self):
        assert "relay" in self._evidence()


# --------------------------------------------------------------------------
# 6. Illustrative constancy math
# --------------------------------------------------------------------------
class TestIllustrativeConstancyMath:
    def test_meta_avg_is_minus_0025(self):
        assert abs(META_TONE_AVG - ((META_TONE_AMA_CARRIED + META_TONE_BRICKED) / 2)) < 1e-9

    def test_constancy_delta_near_zero(self):
        assert abs(CONSTANCY_DELTA - (META_TONE_AVG - APPLE_TONE)) < 1e-9

    def test_delta_inside_neutral_band(self):
        assert abs(CONSTANCY_DELTA) < 0.10

    def test_block_records_manual_illustrative_only(self):
        disc = _block()["statistical_discipline"]
        assert "MANUAL ILLUSTRATIVE" in disc

    def test_no_pvalue_or_effect_size(self):
        disc = _block()["statistical_discipline"]
        assert "NOT_CALCULATED" in disc
        assert _block()["is_significant"] is False

    def test_engine_not_run(self):
        assert "engine NOT run" in _block()["statistical_discipline"]


# --------------------------------------------------------------------------
# 7. Confounders ranked strongest-first
# --------------------------------------------------------------------------
class TestConfoundersRanked:
    def _confounders(self):
        return _block()["confounders"]

    def test_at_least_four_confounders(self):
        assert len(self._confounders()) >= 4

    def test_strong_confounder_first(self):
        assert self._confounders()[0].startswith("[STRONG]")

    def test_second_strong_before_moderate(self):
        tags = []
        for c in self._confounders():
            if c.startswith("[STRONG]"):
                tags.append("STRONG")
            elif c.startswith("[MODERATE"):
                tags.append("MODERATE")
            else:
                tags.append("OTHER")
        first_moderate = next(
            (i for i, t in enumerate(tags) if t == "MODERATE"), len(tags)
        )
        strong_count = sum(1 for t in tags[:first_moderate] if t == "STRONG")
        assert strong_count >= 2

    def test_excerpt_bounded_confounder(self):
        text = " ".join(self._confounders())
        assert "excerpt" in text

    def test_genre_asymmetry_confounder(self):
        text = " ".join(self._confounders())
        assert "genre" in text.lower()

    def test_sample_size_confounder(self):
        text = " ".join(self._confounders())
        assert "n=1" in text


# --------------------------------------------------------------------------
# 8. Counter-evidence
# --------------------------------------------------------------------------
class TestCounterevidence:
    def test_at_least_three_counterevidence(self):
        assert len(_block()["counterevidence"]) >= 3

    def test_2021_buzzfeed_counterevidence(self):
        text = " ".join(_block()["counterevidence"])
        assert "2021" in text and "BuzzFeed" in text

    def test_register_counterevidence(self):
        text = " ".join(_block()["counterevidence"])
        assert "Register" in text

    def test_gorringe_counterevidence(self):
        text = " ".join(_block()["counterevidence"])
        assert "Gorringe" in text or "948" in text


# --------------------------------------------------------------------------
# 9. Bounds, does not falsify
# --------------------------------------------------------------------------
class TestBoundsNotFalsifies:
    def test_not_falsification_family_member(self):
        fam = _block()["falsification_family"]
        assert "NOT a falsification-family member" in fam

    def test_bounds_language_present(self):
        fam = _block()["falsification_family"]
        assert "bound" in fam.lower()

    def test_ledger_not_incremented(self):
        assert "holds at 29" in _block()["ledger"]

    def test_not_artifact_grade(self):
        assert "NOT artifact-grade" in _block()["finding"]

    def test_distinct_from_gorringe_948(self):
        finding = _block()["finding"]
        assert "Gorringe" in finding or "948" in finding


# --------------------------------------------------------------------------
# 10. No significance claim
# --------------------------------------------------------------------------
class TestNoSignificanceClaim:
    def test_is_significant_false_in_block(self):
        assert _block()["is_significant"] is False

    def test_no_analysis_json_update_true(self):
        assert _block()["no_analysis_json_update"] is True

    def test_correlation_not_causation_true(self):
        assert _block()["correlation_not_causation"] is True

    def test_n1_pair_disclosed(self):
        text = " ".join(_block()["confounders"])
        assert "n=1" in text


# --------------------------------------------------------------------------
# 11. Testable predictions
# --------------------------------------------------------------------------
class TestTestablePredictions:
    def test_at_least_two_predictions(self):
        assert len(_block()["testable_predictions"]) >= 2

    def test_future_apple_piece_prediction(self):
        text = " ".join(_block()["testable_predictions"])
        assert "Apple" in text

    def test_future_meta_piece_prediction(self):
        text = " ".join(_block()["testable_predictions"])
        assert "Meta" in text


# --------------------------------------------------------------------------
# 12. Doc-sync ratchet
# --------------------------------------------------------------------------
class TestDocSyncRatchet:
    def test_readme_stats_table_updated(self):
        text = _read(README_PATH)
        assert f"| Tests | {README_TESTS_AFTER} |" in text
        assert f"Across {README_FILES_AFTER} test files" in text

    def test_readme_test_file_row(self):
        text = _read(README_PATH)
        assert OWN_BASENAME in text

    def test_architecture_stats_updated(self):
        text = _read(ARCH_PATH)
        assert str(README_TESTS_AFTER) in text

    def test_architecture_tree_row(self):
        text = _read(ARCH_PATH)
        assert OWN_BASENAME in text

    def test_counts_match_collect_only(self):
        # The README totals must equal the pre-commit collect-only
        # counts plus exactly this file's tests and one file.
        assert README_TESTS_AFTER == README_TESTS_BEFORE + THIS_FILE_TEST_COUNT
        assert README_FILES_AFTER == README_FILES_BEFORE + 1


# --------------------------------------------------------------------------
# 13. Iteration-log entry
# --------------------------------------------------------------------------
class TestIterationLogEntry:
    def test_953_header_present(self):
        log = _read(LOG_PATH)
        assert "## #953 Type B:" in log

    def test_log_records_mechanism_803(self):
        log = _read(LOG_PATH)
        assert "mechanism 803" in log

    def test_log_records_notopoulos(self):
        log = _read(LOG_PATH)
        assert "Notopoulos" in log

    def test_log_records_push_status(self):
        log = _read(LOG_PATH)
        assert "Push status" in log


# --------------------------------------------------------------------------
# 14. Corpus novelty post-commit greps
# --------------------------------------------------------------------------
class TestCorpusNoveltyPostCommitGreps:
    def test_block_key_unique_in_home_yaml(self):
        text = _read(PROFILE)
        assert text.count(BLOCK_KEY) == 1

    def test_both_urls_present_post_commit(self):
        text = _read(PROFILE)
        for url in EXPECTED_URLS:
            assert url in text, url

    def test_no_804_keys_post_commit(self):
        assert _repo_grep(NEXT_ID_MARKER) == []
        assert _repo_grep(NEXT_ID_NUMERIC, roots=("profiles",)) == []

    def test_journalist_key_unique(self):
        text = _read(JOURNALISTS)
        # The top-level `katie_notopoulos:` key appears once; the
        # competitor_coverage sub-key carries the iteration prefix.
        assert text.count("\n" + JOURNALIST_KEY + ":") == 1


# --------------------------------------------------------------------------
# 15. Journalist profile update (first dedicated Type B on Notopoulos)
# --------------------------------------------------------------------------
class TestJournalistProfileUpdate:
    @lru_cache(maxsize=1)
    def _doc(self):
        return yaml.safe_load(_read(JOURNALISTS))

    def test_katie_notopoulos_key_exists(self):
        assert JOURNALIST_KEY in self._doc()

    def test_name_and_publication(self):
        j = self._doc()[JOURNALIST_KEY]
        assert j["name"] == "Katie Notopoulos"
        assert j["current_publication"] == "Business Insider"

    def test_mechanism_ids_include_803(self):
        j = self._doc()[JOURNALIST_KEY]
        assert 803 in j["mechanism_ids"]

    def test_source_urls_present(self):
        j = self._doc()[JOURNALIST_KEY]
        for url in EXPECTED_URLS:
            assert url in j["source_urls"], url

    def test_competitor_coverage_sub_block(self):
        j = self._doc()[JOURNALIST_KEY]
        assert JOURNALIST_SUB_KEY in j["competitor_coverage"]
        sub = j["competitor_coverage"][JOURNALIST_SUB_KEY]
        assert sub["iteration"] == 953
        assert sub["mechanism_id"] == 803
        assert sub["is_significant"] is False
