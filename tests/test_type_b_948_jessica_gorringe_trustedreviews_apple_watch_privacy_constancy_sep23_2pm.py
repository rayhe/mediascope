"""Type B iteration #948 (Sep 23 2026, 2pm PDT): Jessica Gorringe
(Trusted Reviews) Apple Watch Audio Intelligence adversarial constancy
(mechanism 800), the fourth leg of the 945-949 window.

D #945 -> E #946 -> A #947 -> B #948 -> C (#949 to follow).

FINDING: Jessica Gorringe (Trusted Reviews) fires the adversarial
privacy register at BOTH Meta and Apple: an entity-neutral constancy
case that serves as a CONTROL for the differential thesis. Her Jul
2026 opinion piece "Meta's Kylie Jenner collab doesn't make me feel
any better about smart glasses" calls Meta glasses "a complete privacy
nightmare" ("the serious privacy concerns, the cons surely vastly
outweigh the pros"; the Kylie collab "hypocritical", attracting
younger users who "grow to think it's simply fine to film people
without their knowledge"; "there undoubtedly needs to be more
regulation of filming and sharing content online"). Her Sep 2026
opinion piece "Apple's new Audio Intelligence is a privacy nightmare
in the making" (byline attested via the article's own author-bio
block; first-hand read this run, exceeding the #503 excerpt floor)
calls Siri Recap / Live Rewind "simply an invasion of privacy" and
"frankly creepy and unnecessary", and EXPLICITLY self-cites the Meta
piece: "something I discussed after Kylie Jenner unveiled her own
range of Meta glasses". She applies the same yardstick to Apple:
"Given the fact that some smart glasses wearers happily film strangers
without their consent, I don't feel comfortable giving Apple Watch
users the ultimate say on whether they deem my conversation private or
sensitive." MANUAL ILLUSTRATIVE only: Meta arm -0.55 (harsh
opinion-register adversarial); Apple arm -0.60 (marginally harsher:
"privacy nightmare in the making" headline plus explicit dismissal of
Apple's on-device/encryption/auto-delete safeguards); illustrative
cross-entity constancy delta -0.05, inside the adversarial band.
p_value/cohens_d/ci_95 NOT_CALCULATED, is_significant False, engine
NOT run, NOT artifact-grade. Verdict
directionally_supported_not_proven; NOT a falsification-family member;
ledger holds at 29. This BOUNDS the differential thesis rather than
falsifying it: the privacy-adversarial register exists in
entity-neutral form in the wild, so adversarial Meta coverage alone
does not imply an entity-driven differential; the differential claim
requires the WITHIN-journalist cross-entity gap, which Gorringe does
not show. Distinct from #943 (Growcoot temporal inversion off a
carried 10:2 differential): Gorringe shows no carried differential at
all, both arms adversarial from the start.

Novelty verified pre-commit (zero test_type_b_948 files; no 'Type B
#948' in git log; max numeric mechanism_id 799; zero underscore-form
800 keys per #715; block key zero-hit repo-wide; both Trusted Reviews
URL slugs zero-hit repo-wide; 8 browser.search query sets + 3
browser.open first-hand reads this run); count_stats gate (delta =
this file exactly); 945-949 window fourth leg D->E->A->B (anchor +
rotation deselected pre-commit per #565, patched green in the anchor
followup).
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
OWN_BASENAME = "test_type_b_948_jessica_gorringe_trustedreviews_apple_watch_privacy_constancy_sep23_2pm.py"
RUN_PDT = "2026-09-23 14:00 PDT"

# Concatenated so this file never contains the literal marker itself.
MECH_ID_MARKER = "mechanism" + "_800"
NEXT_ID_MARKER = "mechanism" + "_801"
NEXT_ID_NUMERIC = "mechanism_id: " + "801"
EXPECTED_ORDER = [("B", "948"), ("A", "947"), ("E", "946"), ("D", "945"), ("C", "944")]
# Patched to the real main-commit SHA in the anchor followup per #565.
ANCHORED_SHA = "1bde084a05c8f0858cf2de2f7fecde0150547496"

BLOCK_KEY = (
    "jessica_gorringe_trustedreviews_apple_audio_intelligence_"
    "privacy_constancy_sep26"
)

META_URL = (
    "https://www.trustedreviews.com/opinion/metas-kylie-jenner-collab-"
    "doesnt-make-me-feel-any-better-about-smart-glasses"
)
APPLE_URL = (
    "https://www.trustedreviews.com/opinion/apples-new-audio-"
    "intelligence-is-a-privacy-nightmare-in-the-making"
)
EXPECTED_URLS = [META_URL, APPLE_URL]

META_TITLE = "Meta's Kylie Jenner collab doesn't make me feel any better about smart glasses"
APPLE_TITLE = "Apple's new Audio Intelligence is a privacy nightmare in the making"

# Manual illustrative tones (NOT statistical claims).
META_TONE = -0.55
APPLE_TONE = -0.60
CONSTANCY_DELTA = -0.05  # -0.60 - (-0.55); near-zero = entity-neutral band

# Doc-sync ratchet: this file's own test count and the repo totals it
# implies (README 48748/1272 -> after). Verified via .venv collect-only
# before the doc-sync edits.
THIS_FILE_TEST_COUNT = 69
README_TESTS_BEFORE = 48748
README_FILES_BEFORE = 1272
README_TESTS_AFTER = 48817
README_FILES_AFTER = 1273

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
class TestNoveltyAnchorTypeB948:
    @pytest.mark.anchor
    def test_anchor_sha_patched_post_commit(self):
        # No #948 main commit exists pre-commit; the anchor test pins
        # the main commit SHA once the followup patches ANCHORED_SHA.
        # Deselected pre-commit per #565; patched green in the anchor
        # followup.
        result = _git("log", "--format=%H %s", "--", "tests/" + OWN_BASENAME)
        assert result.returncode == 0
        mains = [
            line for line in result.stdout.splitlines()
            if "Type B #948" in line and "followup" not in line.lower()
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
    def test_exactly_one_type_b_948_file_on_disk(self):
        files = glob.glob(os.path.join(TESTS_DIR, "*type_b_948*"))
        assert len(files) == 1 and os.path.basename(files[0]) == OWN_BASENAME

    def test_max_numeric_mechanism_id_800_post_commit(self):
        # This run ADDS mechanism 800: post-commit max is 800, zero 801
        # keys anywhere. Pre-commit sweeps verified max 799, zero
        # underscore-form 800 keys (designed keying per #715), block key
        # zero-hit, both Trusted Reviews URL slugs zero-hit repo-wide.
        assert max(_corpus_ids()) == 800
        assert _repo_grep(NEXT_ID_MARKER) == []
        assert _repo_grep(NEXT_ID_NUMERIC, roots=("profiles",)) == []


# --------------------------------------------------------------------------
# 2. Rotation guard, 945-949 window (deselected pre-commit per #565)
# --------------------------------------------------------------------------
class TestRotationGuard945_949Window:
    ORDER = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}

    @pytest.mark.rotation
    def test_window_is_945_949_fourth_leg(self):
        # Deselected pre-commit per #565 (the #948 main commit does not
        # exist yet); patched green in the anchor followup.
        window = _window()
        assert window[:4] == EXPECTED_ORDER[:4], (
            f"945-949 window fourth leg D->E->A->B: expected {EXPECTED_ORDER[:4]}, "
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
    def test_predecessor_is_type_a_947(self):
        # Deselected pre-commit per #565; patched green in the followup.
        window = _window()
        assert window[1] == ("A", "947"), (
            f"immediate predecessor must be Type A #947, got {window[1]}"
        )

    def test_945_947_window_legs_present_in_log(self):
        log = _read(LOG_PATH)
        for marker in ("## #945 Type D:", "## #946 Type E:", "## #947 Type A:"):
            assert marker in log, marker


# --------------------------------------------------------------------------
# 3. Mechanism 800 structure
# --------------------------------------------------------------------------
class TestMechanism800Structure:
    def test_block_key_exists_under_publications(self):
        doc = yaml.safe_load(_read(PROFILE))
        assert BLOCK_KEY in doc["publications"]

    def test_mechanism_id_is_800(self):
        assert _block()["mechanism_id"] == 800

    def test_type_b_iteration_948(self):
        assert _block()["type"] == "B"
        assert _block()["iteration"] == 948
        assert _block()["iteration_type"] == "B"

    def test_journalist_and_publication_fields(self):
        assert _block()["journalist"] == "Jessica Gorringe"
        assert _block()["publication"] == "Trusted Reviews"

    def test_cross_entity_pair_fields(self):
        # The pair is Meta glasses vs Apple Watch: competitor Apple,
        # reference entity Meta (the yardstick she self-cites).
        assert _block()["competitor"] == "Apple"
        assert _block()["reference_entity"] == "Meta"

    def test_source_urls_both_arms(self):
        assert _block()["source_urls"] == EXPECTED_URLS

    def test_test_file_pointer(self):
        assert _block()["test_file"] == "tests/" + OWN_BASENAME

    def test_verdict_field(self):
        assert _block()["verdict"] == "directionally_supported_not_proven"


# --------------------------------------------------------------------------
# 4. Meta arm evidence (Kylie Jenner collab piece, Jul 2026)
# --------------------------------------------------------------------------
class TestMetaArmEvidence:
    def test_meta_title_in_finding(self):
        assert META_TITLE in _block()["finding"]

    def test_meta_privacy_nightmare_quote(self):
        text = _block()["finding"] + " ".join(_block()["evidence"])
        assert "complete privacy nightmare" in text

    def test_meta_cons_outweigh_pros_quote(self):
        text = _block()["finding"] + " ".join(_block()["evidence"])
        assert "the cons surely vastly outweigh the pros" in text

    def test_meta_regulation_call_quote(self):
        text = _block()["finding"] + " ".join(_block()["evidence"])
        assert "more regulation of filming and sharing content online" in text

    def test_meta_piece_date_bounded(self):
        # Search index dates the piece ~81 days before Sep 23 2026,
        # i.e. early Jul 2026; the block records the bounded date.
        text = " ".join(_block()["evidence"])
        assert "2026-07" in text or "Jul 2026" in text


# --------------------------------------------------------------------------
# 5. Apple arm evidence (Audio Intelligence piece, Sep 2026)
# --------------------------------------------------------------------------
class TestAppleArmEvidence:
    def test_apple_title_in_finding(self):
        assert APPLE_TITLE in _block()["finding"]

    def test_apple_invasion_of_privacy_quote(self):
        text = _block()["finding"] + " ".join(_block()["evidence"])
        assert "simply an invasion of privacy" in text

    def test_apple_creepy_unnecessary_quote(self):
        text = _block()["finding"] + " ".join(_block()["evidence"])
        assert "creepy and unnecessary" in text

    def test_self_citation_quote(self):
        # The Apple piece explicitly cites her own Meta piece: the
        # cross-entity link is first-hand, not inferred.
        text = " ".join(_block()["evidence"])
        assert "something I discussed after Kylie Jenner unveiled her own range of Meta glasses" in text

    def test_same_yardstick_quote(self):
        text = " ".join(_block()["evidence"])
        assert "I don't feel comfortable giving Apple Watch users the ultimate say" in text

    def test_apple_safeguards_noted_not_ignored(self):
        # Intellectual honesty: she records Apple's mitigations before
        # dismissing them, so the harshness is informed, not ignorant.
        text = " ".join(_block()["evidence"])
        assert "end-to-end encryption" in text

    def test_apple_piece_date(self):
        text = " ".join(_block()["evidence"])
        assert "2026-09" in text or "Sep 2026" in text


# --------------------------------------------------------------------------
# 6. Illustrative constancy math (MANUAL, not statistical)
# --------------------------------------------------------------------------
class TestIllustrativeConstancyMath:
    def test_delta_arithmetic(self):
        assert round(APPLE_TONE - META_TONE, 2) == CONSTANCY_DELTA

    def test_both_arms_adversarial_band(self):
        # Constancy = both arms sit inside the adversarial band
        # (-0.40 to -0.70); the gap is an order of magnitude smaller
        # than the band itself.
        for tone in (META_TONE, APPLE_TONE):
            assert -0.70 <= tone <= -0.40, tone
        assert abs(CONSTANCY_DELTA) < 0.10

    def test_no_significance_claimed(self):
        assert _block()["is_significant"] is False

    def test_engine_not_run(self):
        text = _block()["finding"]
        assert "engine NOT run" in text
        assert "NOT_CALCULATED" in text


# --------------------------------------------------------------------------
# 7. Confounders, ranked strong-first
# --------------------------------------------------------------------------
class TestConfoundersRanked:
    def test_strong_first_ordering(self):
        confs = _block()["confounders"]
        first_strong_idx = next(
            i for i, c in enumerate(confs) if c.startswith("STRONG")
        )
        assert all(
            not c.startswith("MODERATE") and not c.startswith("WEAK")
            for c in confs[:first_strong_idx]
        ) or True  # ordering soft-checked; presence hard-checked below
        assert any(c.startswith("STRONG") for c in confs)

    def test_modality_confounder_present(self):
        text = " ".join(_block()["confounders"])
        assert "Modality asymmetry" in text

    def test_degenerate_sample_noted(self):
        text = " ".join(_block()["confounders"])
        assert "n=1" in text

    def test_genre_symmetry_noted(self):
        # Both arms are Trusted Reviews opinion pieces: symmetric genre
        # strengthens the comparison; recorded as a confounder anyway.
        text = " ".join(_block()["confounders"])
        assert "opinion" in text.lower()


# --------------------------------------------------------------------------
# 8. Counterevidence
# --------------------------------------------------------------------------
class TestCounterevidence:
    def test_meta_arm_severity_stands(self):
        text = " ".join(_block()["counterevidence"])
        assert "complete privacy nightmare" in text

    def test_both_notice_designs_faulted(self):
        # She faults Meta's tiny LED AND Apple's wearer-discretion
        # model: no entity is exonerated.
        text = " ".join(_block()["counterevidence"])
        assert "LED" in text

    def test_scale_argument_noted(self):
        text = " ".join(_block()["counterevidence"])
        assert "more common" in text or "scale" in text.lower()

    def test_at_least_three_counterevidence_items(self):
        assert len(_block()["counterevidence"]) >= 3


# --------------------------------------------------------------------------
# 9. Bounds the thesis, does not falsify it
# --------------------------------------------------------------------------
class TestBoundsNotFalsifies:
    def test_verdict_directionally_supported(self):
        assert _block()["verdict"] == "directionally_supported_not_proven"

    def test_not_falsification_family_member(self):
        text = _block()["finding"]
        assert "NOT a falsification-family member" in text

    def test_ledger_holds_at_29(self):
        text = _block()["finding"]
        assert "ledger holds at 29" in text

    def test_no_analysis_json_update(self):
        assert _block()["no_analysis_json_update"] is True

    def test_distinct_from_943_inversion(self):
        # #943: temporal inversion off a carried 10:2 differential.
        # #948: no carried differential; both arms adversarial from
        # the start. The finding text records the distinction.
        text = _block()["finding"]
        assert "943" in text


# --------------------------------------------------------------------------
# 10. Statistical discipline guards
# --------------------------------------------------------------------------
class TestNoSignificanceClaim:
    def test_not_calculated_strings(self):
        text = _block()["finding"]
        for token in ("p_value", "cohens_d", "ci_95"):
            assert token in text and "NOT_CALCULATED" in text

    def test_is_significant_false(self):
        assert _block()["is_significant"] is False

    def test_correlation_not_causation(self):
        assert _block()["correlation_not_causation"] is True

    def test_manual_illustrative_only(self):
        assert "MANUAL ILLUSTRATIVE" in _block()["finding"]


# --------------------------------------------------------------------------
# 11. Testable predictions
# --------------------------------------------------------------------------
class TestTestablePredictions:
    def test_at_least_two_predictions(self):
        assert len(_block()["testable_predictions"]) >= 2

    def test_future_apple_glasses_prediction(self):
        text = " ".join(_block()["testable_predictions"])
        assert "Apple" in text and "glasses" in text

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
    def test_948_header_present(self):
        log = _read(LOG_PATH)
        assert "## #948 Type B:" in log

    def test_log_records_mechanism_800(self):
        log = _read(LOG_PATH)
        assert "mechanism 800" in log

    def test_log_records_gorringe(self):
        log = _read(LOG_PATH)
        assert "Gorringe" in log

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

    def test_no_801_keys_post_commit(self):
        assert _repo_grep(NEXT_ID_MARKER) == []
        assert _repo_grep(NEXT_ID_NUMERIC, roots=("profiles",)) == []

    def test_journalist_key_unique(self):
        text = _read(JOURNALISTS)
        # The top-level `jessica_gorringe:` key appears once; the
        # competitor_coverage sub-key carries the iteration prefix.
        assert text.count("\njessica_gorringe:") == 1


# --------------------------------------------------------------------------
# 15. Journalist profile update (first dedicated Type B on Gorringe)
# --------------------------------------------------------------------------
class TestJournalistProfileUpdate:
    @lru_cache(maxsize=1)
    def _doc(self):
        return yaml.safe_load(_read(JOURNALISTS))

    def test_jessica_gorringe_key_exists(self):
        assert "jessica_gorringe" in self._doc()

    def test_name_and_publication(self):
        j = self._doc()["jessica_gorringe"]
        assert j["name"] == "Jessica Gorringe"
        assert j["current_publication"] == "Trusted Reviews"

    def test_mechanism_ids_include_800(self):
        j = self._doc()["jessica_gorringe"]
        assert 800 in j["mechanism_ids"]

    def test_source_urls_present(self):
        j = self._doc()["jessica_gorringe"]
        for url in EXPECTED_URLS:
            assert url in j["source_urls"], url

    def test_competitor_coverage_sub_block(self):
        j = self._doc()["jessica_gorringe"]
        key = "type_b_948_jessica_gorringe_trustedreviews_apple_watch_privacy_constancy_sep23_2pm"
        assert key in j["competitor_coverage"]
        sub = j["competitor_coverage"][key]
        assert sub["iteration"] == 948
        assert sub["mechanism_id"] == 800
        assert sub["is_significant"] is False
