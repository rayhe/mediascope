"""Type B iteration #943 (Sep 23 2026, 9am PDT): Matt Growcoot (PetaPixel)
Apple Watch always-listening adversarial inversion (mechanism 797),
the fourth leg of the 940-944 window.

D #940 -> E #941 -> A #942 -> B #943 -> C (#944 to follow).

FINDING: Matt Growcoot (PetaPixel) activates the adversarial privacy
register he spent Jan-Aug 2026 aiming at Meta camera glasses against
APPLE's shipped always-listening wearable. His Sep 9, 2026 opinion
piece "Your Apple Watch Is Always Listening, Will Anyone Ever Be
Honest Again?" (byline attested via his PetaPixel author archive
listing) calls Siri Recap / Live Rewind "truly a Black Mirror episode"
and "the idea that some weirdo watch wearer is going through the notes
of a conversation they had with me that I thought was private is
repellent". Within the same article he explicitly ranks Meta's notice
design ABOVE Apple's: "At least Meta's glasses have a blinking LED
light that lets others know they are recording ... How will anyone ever
know that a smartwatch is recording their conversation? Apple makes no
mention of any recording light, nor does it mention the other parties'
consent." This is a TEMPORAL INVERSION of mechanism 230's Jan-Aug 2026
pattern (10 Meta-adversarial vs 2 Apple-aspirational smart-glasses
articles): once Apple shipped an actual always-listening device,
Growcoot's adversarial register fired on Apple at equal-or-greater
intensity while crediting Meta's LED safeguard. This BOUNDS mechanism
230 rather than falsifying it: the Meta-adversarial / Apple-aspirational
gap was conditional on Apple's glasses being hypothetical. Growcoot's
register tracks shipped ambient-sensing reality more than entity
identity. MANUAL ILLUSTRATIVE only: new Apple Watch arm -0.55 (harsh
opinion-register adversarial); carried m230 Apple-aspirational anchor
+0.30 illustrative (hand-scored this run from m230's documented
vocabulary); illustrative Apple-temporal inversion delta -0.85.
Carried m230 Meta arm un-rescored per the #807 pattern (m230
asymmetry_score 0.76 stands). p_value/cohens_d/ci_95 NOT_CALCULATED,
is_significant False, engine NOT run, NOT artifact-grade. Verdict
directionally_supported_not_proven; NOT a falsification-family member;
ledger holds at 29.

Novelty verified pre-commit (zero test_type_b_943 files; no 'Type B
#943' in git log; max numeric mechanism_id 796; zero underscore-form
797 keys per #715; block key zero-hit repo-wide; always-listening URL
slug zero-hit repo-wide; 16 browser.search query sets this run, 0
browser.open per #503); count_stats gate (delta = this file exactly);
940-944 window fourth leg D->E->A->B (anchor + rotation deselected
pre-commit per #565, patched green in the anchor followup).
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
OWN_BASENAME = "test_type_b_943_matt_growcoot_petapixel_apple_watch_always_listening_inversion_sep23_9am.py"
RUN_PDT = "2026-09-23 09:00 PDT"

# Concatenated so this file never contains the literal marker itself.
MECH_ID_MARKER = "mechanism" + "_797"
NEXT_ID_MARKER = "mechanism" + "_798"
NEXT_ID_NUMERIC = "mechanism_id: " + "798"
EXPECTED_ORDER = [("B", "943"), ("A", "942"), ("E", "941"), ("D", "940"), ("C", "939")]
# Patched to the real main-commit SHA in the anchor followup per #565.
ANCHORED_SHA = "84b933cffd8822af8887487eb1c1979a363268f7"

BLOCK_KEY = (
    "matt_growcoot_petapixel_apple_watch_always_listening_"
    "adversarial_inversion_sep26"
)

APPLE_WATCH_URL = (
    "https://petapixel.com/2026/09/09/your-apple-watch-is-always-"
    "listening-will-anyone-ever-be-honest-again/"
)
AUTHOR_ARCHIVE_URL = "https://petapixel.com/author/mattgrowcoot/"
M230_APPLE_URL = (
    "https://petapixel.com/2026/07/27/apple-frets-over-smart-glasses-"
    "bad-reputation-as-2027-launch-looms/"
)
M230_META_URL = (
    "https://petapixel.com/2026/08/10/uk-venues-ban-meta-smart-glasses-en-masse/"
)
EXPECTED_URLS = [APPLE_WATCH_URL, AUTHOR_ARCHIVE_URL, M230_APPLE_URL, M230_META_URL]

ARTICLE_TITLE = "Your Apple Watch Is Always Listening, Will Anyone Ever Be Honest Again?"

# Manual illustrative tones (NOT statistical claims).
APPLE_WATCH_TONE = -0.55
M230_APPLE_ASPIRATIONAL_TONE = 0.30
INVERSION_DELTA = -0.85  # -0.55 - 0.30

# Doc-sync ratchet: this file's own test count and the repo totals it
# implies (README 48476/1267 -> after). Verified via .venv collect-only
# before the doc-sync edits.
THIS_FILE_TEST_COUNT = 69
README_TESTS_BEFORE = 48476
README_FILES_BEFORE = 1267
README_TESTS_AFTER = 48545
README_FILES_AFTER = 1268

PROFILE = os.path.join(REPO, "profiles", "competitor-coverage-research.yaml")
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
class TestNoveltyAnchorTypeB943:
    @pytest.mark.anchor
    def test_anchor_sha_patched_post_commit(self):
        # No #943 main commit exists pre-commit; the anchor test pins
        # the main commit SHA once the followup patches ANCHORED_SHA.
        # Deselected pre-commit per #565; patched green in the anchor
        # followup.
        result = _git("log", "--format=%H %s", "--", "tests/" + OWN_BASENAME)
        assert result.returncode == 0
        mains = [
            line for line in result.stdout.splitlines()
            if "Type B #943" in line and "followup" not in line.lower()
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
    def test_exactly_one_type_b_943_file_on_disk(self):
        files = glob.glob(os.path.join(TESTS_DIR, "*type_b_943*"))
        assert len(files) == 1 and os.path.basename(files[0]) == OWN_BASENAME

    def test_max_numeric_mechanism_id_797_post_commit(self):
        # This run ADDS mechanism 797: post-commit max is 797, zero 798
        # keys anywhere. Pre-commit sweeps verified max 796, zero
        # underscore-form 797 keys (designed keying per #715), block key
        # zero-hit, always-listening URL slug zero-hit repo-wide.
        assert max(_corpus_ids()) == 797
        assert _repo_grep(NEXT_ID_MARKER) == []
        assert _repo_grep(NEXT_ID_NUMERIC, roots=("profiles",)) == []


# --------------------------------------------------------------------------
# 2. Rotation guard, 940-944 window (deselected pre-commit per #565)
# --------------------------------------------------------------------------
class TestRotationGuard940_944Window:
    ORDER = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}

    @pytest.mark.rotation
    def test_window_is_940_944_fourth_leg(self):
        # Deselected pre-commit per #565 (the #943 main commit does not
        # exist yet); patched green in the anchor followup.
        window = _window()
        assert window[:4] == EXPECTED_ORDER[:4], (
            f"940-944 window fourth leg D->E->A->B: expected {EXPECTED_ORDER[:4]}, "
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
    def test_predecessor_is_type_a_942(self):
        # Deselected pre-commit per #565; patched green in the followup.
        window = _window()
        assert window[1] == ("A", "942"), (
            f"immediate predecessor must be Type A #942, got {window[1]}"
        )

    def test_940_942_window_legs_present_in_log(self):
        log = _read(LOG_PATH)
        for marker in ("## #940 Type D:", "## #941 Type E:", "## #942 Type A:"):
            assert marker in log, marker


# --------------------------------------------------------------------------
# 3. Mechanism 797 structure
# --------------------------------------------------------------------------
class TestMechanism797Structure:
    def test_block_key_exists_under_publications(self):
        doc = yaml.safe_load(_read(PROFILE))
        assert BLOCK_KEY in doc["publications"]

    def test_block_key_unique_repo_wide(self):
        hits = _repo_grep(BLOCK_KEY)
        assert hits == [os.path.join("profiles", "competitor-coverage-research.yaml")], hits

    def test_mechanism_id_797(self):
        assert _block()["mechanism_id"] == 797

    def test_iteration_and_type_and_time_pdt(self):
        b = _block()
        assert b["iteration"] == 943
        assert b["iteration_type"] == "B"
        assert b["type"] == "B"
        assert b["iteration_time"] == RUN_PDT

    def test_journalist_and_publication(self):
        b = _block()
        assert b["journalist"] == "Matt Growcoot"
        assert b["publication"] == "PetaPixel"
        assert b["competitor"] == "Apple"
        assert b["reference_entity"] == "Meta"

    def test_rotation_window_leg(self):
        b = _block()
        assert b["rotation_window"] == "940-944"
        assert "B #943" in b["window_leg"]

    def test_ascii_only_no_em_dashes(self):
        raw = _read(PROFILE)
        start = raw.index(BLOCK_KEY)
        end = raw.index("mechanism_217_fashion_surveillance_kmart_price_democratization:")
        chunk = raw[start:end]
        assert "\u2014" not in chunk, "em dash forbidden in repo additions"
        chunk.encode("ascii")

    def test_test_file_field_names_this_file(self):
        assert _block()["test_file"] == "tests/" + OWN_BASENAME


# --------------------------------------------------------------------------
# 4. Apple Watch arm evidence (search-excerpt-bounded per #503)
# --------------------------------------------------------------------------
class TestAppleWatchArmEvidence:
    def test_article_title_verbatim(self):
        assert ARTICLE_TITLE in _block()["finding"]

    def test_article_date_sep_9_2026(self):
        ev = " ".join(_block()["evidence"])
        assert "2026/09/09" in ev

    def test_byline_attribution_via_author_archive(self):
        ev = " ".join(_block()["evidence"])
        assert "Matt Growcoot" in ev
        assert AUTHOR_ARCHIVE_URL in _block()["source_urls"]

    def test_excerpt_tier_evidence_limitation(self):
        ev = " ".join(_block()["evidence"])
        assert "search-excerpt-bounded" in ev
        assert "browser.open unavailable" in ev

    def test_opinion_genre_noted(self):
        assert "opinion" in _block()["finding"].lower()

    def test_black_mirror_quote_present(self):
        text = _block()["finding"] + " ".join(_block()["evidence"])
        assert "Black Mirror" in text

    def test_repellent_quote_present(self):
        text = _block()["finding"] + " ".join(_block()["evidence"])
        assert "repellent" in text

    def test_within_article_meta_led_comparison(self):
        text = _block()["finding"] + " ".join(_block()["evidence"])
        assert "blinking LED" in text
        assert "no mention of any recording light" in text

    def test_apple_watch_url_in_source_urls(self):
        assert APPLE_WATCH_URL in _block()["source_urls"]

    def test_apple_watch_tone_minus_055_illustrative(self):
        assert "Apple Watch arm -0.55" in _block()["finding"]
        assert APPLE_WATCH_TONE == -0.55


# --------------------------------------------------------------------------
# 5. Carried Meta arm discipline per #807 (no rescoring)
# --------------------------------------------------------------------------
class TestCarriedMetaArm807:
    def test_mechanism_230_referenced(self):
        assert 230 in _block()["connects_to"]

    def test_m230_asymmetry_score_carried(self):
        text = _block()["finding"] + " ".join(_block()["evidence"])
        assert "asymmetry_score 0.76" in text

    def test_m230_corpus_ratio_documented(self):
        text = " ".join(_block()["evidence"])
        assert "10+ Meta-adversarial" in text
        assert "2 Apple-aspirational" in text

    def test_unrescored_per_807_stated(self):
        text = _block()["finding"] + " ".join(_block()["evidence"])
        assert "un-rescored per #807" in text

    def test_m230_meta_url_in_source_urls(self):
        assert M230_META_URL in _block()["source_urls"]

    def test_m230_apple_url_in_source_urls(self):
        assert M230_APPLE_URL in _block()["source_urls"]


# --------------------------------------------------------------------------
# 6. Illustrative delta math (manual, NOT statistical)
# --------------------------------------------------------------------------
class TestIllustrativeDeltaMath:
    def test_inversion_delta_math(self):
        assert round(APPLE_WATCH_TONE - M230_APPLE_ASPIRATIONAL_TONE, 2) == INVERSION_DELTA

    def test_aspirational_anchor_labeled_illustrative(self):
        assert "+0.30 illustrative" in _block()["finding"]

    def test_delta_in_finding(self):
        assert "inversion delta -0.85" in _block()["finding"]

    def test_manual_illustrative_banner(self):
        assert "MANUAL ILLUSTRATIVE" in _block()["finding"]


# --------------------------------------------------------------------------
# 7. Ranked confounders
# --------------------------------------------------------------------------
class TestConfoundersRanked:
    def test_seven_confounders(self):
        assert len(_block()["confounders"]) == 7

    def test_strong_confounders_first(self):
        confs = _block()["confounders"]
        strengths = [c.split(":")[0] for c in confs]
        assert strengths[:3] == ["STRONG", "STRONG", "STRONG"], strengths

    def test_modality_confounder_present(self):
        assert any("Modality asymmetry" in c for c in _block()["confounders"])

    def test_genre_confounder_present(self):
        assert any("Genre asymmetry" in c for c in _block()["confounders"])


# --------------------------------------------------------------------------
# 8. Counterevidence
# --------------------------------------------------------------------------
class TestCounterevidence:
    def test_three_counterevidence_items(self):
        assert len(_block()["counterevidence"]) == 3

    def test_m230_pattern_stands_noted(self):
        assert any("10:2 Jan-Aug pattern stands" in c for c in _block()["counterevidence"])

    def test_meta_register_persists_noted(self):
        assert any("relativized not reversed" in c for c in _block()["counterevidence"])

    def test_news_peg_counterevidence_noted(self):
        assert any("news-peg reality" in c for c in _block()["counterevidence"])


# --------------------------------------------------------------------------
# 9. Bounds mechanism 230; NOT a falsification-family member
# --------------------------------------------------------------------------
class TestBoundsNotFalsifies:
    def test_finding_states_bounds_not_falsifies(self):
        assert "BOUNDS mechanism 230 rather than falsifying it" in _block()["finding"]

    def test_verdict_directionally_supported_not_proven(self):
        assert _block()["verdict"] == "directionally_supported_not_proven"

    def test_not_falsification_family(self):
        assert "NOT a falsification-family member" in _block()["finding"]

    def test_ledger_holds_at_29(self):
        assert "ledger holds at 29" in _block()["finding"]

    def test_correlation_not_causation(self):
        assert "Correlation is not causation" in _block()["finding"]


# --------------------------------------------------------------------------
# 10. No statistical significance claims; not artifact-grade
# --------------------------------------------------------------------------
class TestNoSignificanceClaim:
    def test_p_value_not_calculated(self):
        assert "p_value NOT_CALCULATED" in _block()["finding"]

    def test_cohens_d_not_calculated(self):
        assert "cohens_d NOT_CALCULATED" in _block()["finding"]

    def test_ci_95_not_calculated(self):
        assert "ci_95 NOT_CALCULATED" in _block()["finding"]

    def test_is_significant_false(self):
        assert "is_significant False" in _block()["finding"]

    def test_engine_not_run_not_artifact_grade(self):
        finding = _block()["finding"]
        assert "engine NOT run" in finding
        assert "NOT artifact-grade" in finding


# --------------------------------------------------------------------------
# 11. Testable predictions
# --------------------------------------------------------------------------
class TestTestablePredictions:
    def test_three_predictions(self):
        assert len(_block()["testable_predictions"]) == 3

    def test_apple_camera_glasses_prediction(self):
        assert any("2027" in p for p in _block()["testable_predictions"])

    def test_meta_register_persists_prediction(self):
        assert any("continue the adversarial register" in p for p in _block()["testable_predictions"])


# --------------------------------------------------------------------------
# 12. Doc-sync ratchet per #719
# --------------------------------------------------------------------------
class TestDocSyncRatchet:
    def test_readme_stats_table_updated(self):
        readme = _read(README_PATH)
        assert str(README_TESTS_AFTER) in readme
        assert str(README_FILES_AFTER) in readme

    def test_readme_test_file_table_row_present(self):
        assert OWN_BASENAME.replace(".py", "") in _read(README_PATH)

    def test_architecture_tests_tree_updated(self):
        assert OWN_BASENAME.replace(".py", "") in _read(ARCH_PATH)


# --------------------------------------------------------------------------
# 13. Iteration-log entry per #719
# --------------------------------------------------------------------------
class TestIterationLogEntry:
    def test_log_has_943_marker(self):
        assert "## #943 Type B" in _read(LOG_PATH)

    def test_log_entry_names_window_leg(self):
        assert "940-944 window" in _read(LOG_PATH)

    def test_log_entry_names_mechanism_797(self):
        assert "mechanism 797" in _read(LOG_PATH)


# --------------------------------------------------------------------------
# 14. Corpus novelty greps (post-commit form)
# --------------------------------------------------------------------------
class TestCorpusNoveltyPostCommitGreps:
    def test_this_file_test_count_matches_collect(self):
        # The doc-sync ratchet constants stay honest: THIS_FILE holds
        # exactly THIS_FILE_TEST_COUNT tests (collect-only, no -m).
        result = subprocess.run(
            [os.path.join(REPO, ".venv", "bin", "pytest"), "--collect-only",
             "-q", "tests/" + OWN_BASENAME],
            cwd=REPO, capture_output=True, text=True, timeout=120,
        )
        m = re.search(r"(\d+) tests? collected", result.stdout)
        assert m and int(m.group(1)) == THIS_FILE_TEST_COUNT, result.stdout[-500:]

    def test_no_duplicate_mechanism_id_797(self):
        count = len(re.findall(r"mechanism_id:\s*797\b", _read(PROFILE)))
        assert count == 1, count

    def test_url_slug_zero_hit_outside_block(self):
        # The slug legitimately appears in three places: the mechanism block
        # (competitor-coverage-research.yaml), the new matt_growcoot
        # journalist entry's source_urls (journalists.yaml), and this test
        # file's own URL constants.
        hits = _repo_grep("your-apple-watch-is-always-listening-will-anyone-ever-be-honest-again")
        assert sorted(hits) == sorted([
            os.path.join("profiles", "competitor-coverage-research.yaml"),
            os.path.join("profiles", "careers", "journalists.yaml"),
            os.path.join("tests", OWN_BASENAME),
        ]), hits


# --------------------------------------------------------------------------
# 15. Journalist-profile update (per the Type B #868 convention)
# --------------------------------------------------------------------------
class TestJournalistProfileUpdate:
    def _journalists(self):
        return yaml.safe_load(_read(os.path.join(REPO, "profiles", "careers", "journalists.yaml")))

    def test_matt_growcoot_entry_exists(self):
        assert "matt_growcoot" in self._journalists()

    def test_mechanism_ids_carry_230_add_797(self):
        assert self._journalists()["matt_growcoot"]["mechanism_ids"] == [230, 797]

    def test_cross_entity_examples_present(self):
        text = self._journalists()["matt_growcoot"]["notes"]
        assert "10+ Meta-adversarial" in text
        assert "Black Mirror" in text
        assert "blinking LED" in text

    def test_verdict_and_ledger(self):
        j = self._journalists()["matt_growcoot"]
        assert j["verdict"] == "directionally_supported_not_proven"
        assert j["ledger"] == "29"
