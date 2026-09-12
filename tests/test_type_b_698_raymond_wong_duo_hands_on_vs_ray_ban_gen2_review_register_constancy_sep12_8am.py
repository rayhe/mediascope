"""Type B #698: Raymond Wong (Gizmodo) same-journalist cross-entity byline-isolated
review-register pair - Apple iPhone Duo hands-on (Sep 9, 2026) vs Meta
Ray-Ban Meta Gen 2 review (~Apr 2026), both hands-on product-review registers,
both read first-hand this run.

FIRST dedicated Type B pair mechanism on Raymond Wong (mechanism_id 653, next
free pre-commit; max modern mechanism_id was 652). Zero mechanism_* keys
pre-existed on Wong's journalist profile entry (the entry pre-existed in the
journalists list with career/beats/notes/education but no mechanism; this run
adds mechanism_653 as its first mechanism key. The Aug 24
test_raymond_wong_gizmodo_cross_entity_camera_privacy_vocabulary_concentration
test is file-local - #282 documents a vocabulary-concentration finding, not a
YAML mechanism and not a byline-isolated pair). Distinct unit of analysis from
#282: paired review-register comparison, not vocabulary concentration.

Apple arm: Gizmodo Sep 9 2026 (Ray Wong SOLE byline, listed on
https://gizmodo.com/author/raywong page 1 verified first-hand this run;
read first-hand in #697, 78 rendered lines,
https://gizmodo.com/iphone-duo-hands-on-2000808932, in corpus via #697) -
"iPhone Duo Hands-On: The Inner Screen Looks Like Real Paper". Register =
celebratory hands-on: "the iPhone Duo is a stunning device to hold in your
hands", "I immediately marveled at the iPhone Duo's thinness", matte
nano-texture inner screen "absolutely gorgeous. It looks like paper",
"Apple may have made the most desirable foldable ever created". Moderated by
reviewer caveats: "the crease is not completely invisible", "The loss of Face
ID is going to take some getting used to", "Is it worth $2,000 or more? I
don't have an answer for that yet". Tone +0.45 (MANUAL ILLUSTRATIVE, carried
from #697's hand score).

Meta arm: Gizmodo ~Apr 2026 (byline attribution PARTIAL - photo credits all
"@ Raymond Wong / Gizmodo" and first-person long-term-owner voice read
first-hand this run, 120 rendered lines,
https://gizmodo.com/ray-ban-meta-gen-2-review-still-the-best-non-display-smart-glasses-2000664295;
URL in corpus via profiles/gizmodo.yaml examples, no mechanism; the sibling
Meta Ray-Ban Display review disambiguates authorship: its author texts "my
colleague, Ray Wong", so THAT review is not his and this one, with all-Wong
photo credits and no such reference, is) - "Ray-Ban Meta Gen 2 Review: Still
the Best Non-Display Smart Glasses". Register = hands-on product review with
verdict box (3.5): "Ray-Ban Meta AI Glasses Gen 2 aren't exciting but they're
better then the original". "These are the best pair of Ray-Ban Meta AI glasses
you can buy without a screen. Period." "best battery in a pair of non-display
Ray-Ban Meta AI glasses yet." Moderated by Meta-AI caveats: Meta AI "still
finicky at best", the Meta AI app "loves to promote AI slop", privacy caveat
"Meta has a pretty bad track record on that front... you'd best steer clear".
Tone +0.30 (MANUAL ILLUSTRATIVE, hand-scored this run).

Finding: REGISTER CONSTANCY in the review register. Illustrative delta
(Apple minus Meta) = +0.45 - (+0.30) = +0.15; p_value, cohens_d, ci
NOT_CALCULATED; is_significant False (Aug 28 standing rule);
statistical_contract degenerate_n1_per_arm per #638/#643. No engine run. NOT
artifact-grade.

TWENTIETH falsification-family member: the journalist-level "Wong goes hard
on Meta" attribution fails in his review register - his Meta review is
product-positive ("Still the Best", verdict 3.5, "best pair... Period"). This
bounds #282's vocabulary-concentration finding to the news/opinion register
(where alarm vocabulary concentrates on Meta): register-specific, not
reviewer-level. The +0.15 gap tracks product novelty (first-gen foldable
delight vs iterative "aren't exciting but improved" refresh), not entity.

Financial context (correlation, not causation): Gizmodo (Keleops AG) carries
NO known AI licensing deal with Apple or Meta (both financial_tie none in
profiles/gizmodo.yaml competitor_relationships, per #697) - zero-gradient
control: the deal theory makes no differential prediction, and the observed
constancy cannot be attributed to a deal gradient. Finding is at the
journalist-attribution level, consistent with the family.

Novelty vs prior work: FIRST byline-isolated pair mechanism on Raymond Wong.
Distinct from #282 (vocabulary concentration, no pair, no YAML mechanism),
from the Nguyen (#693), Satariano (#688) and Hart (#653) constancy pins
(different journalists), and from #697 (publication-level pair, same Apple
arm, different Meta arm and different unit of analysis).

Rotation: Type B follows Type A (#697) per A,B,C,D,E. Rotation guard,
doc-sync, and novelty-anchor classes are deselected pre-commit per the #565
followup convention; anchor patched in the followup commit once the main
commit SHA is known.
"""

import ast
import glob
import os
import re
import subprocess

import pytest
import yaml

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CAREERS_PATH = os.path.join(REPO_ROOT, "profiles", "careers", "journalists.yaml")
GIZMODO_PATH = os.path.join(REPO_ROOT, "profiles", "gizmodo.yaml")
README_PATH = os.path.join(REPO_ROOT, "README.md")
ARCH_PATH = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")
TESTS_DIR = os.path.join(REPO_ROOT, "tests")
LOG_PATH = os.path.join(REPO_ROOT, "iteration-log.md")

MECH_KEY = "mechanism_653_raymond_wong_duo_hands_on_vs_ray_ban_gen2_review_register_constancy_sep12"
TEST_BASENAME = "test_type_b_698_raymond_wong_duo_hands_on_vs_ray_ban_gen2_review_register_constancy_sep12_8am.py"

APPLE_TONE = 0.45
META_TONE = 0.30
EXPECTED_DELTA = 0.15

APPLE_URL = "https://gizmodo.com/iphone-duo-hands-on-2000808932"
META_URL = "https://gizmodo.com/ray-ban-meta-gen-2-review-still-the-best-non-display-smart-glasses-2000664295"
AUTHOR_PAGE = "https://gizmodo.com/author/raywong"

# Patched in the followup commit per the #565 convention once the main
# commit SHA is known. The rotation-guard class is deselected pre-commit.
ANCHORED_SHA = "a7f061751058c7cbfd7859f2d349992e11755120"


def _careers():
    with open(CAREERS_PATH) as f:
        return yaml.safe_load(f)["journalists"]


def _wong():
    matches = []
    for j in _careers():
        if isinstance(j, dict) and j.get("name") == "Raymond Wong":
            matches.append(j)
    assert len(matches) == 1, "expected exactly one Raymond Wong entry, got %d" % len(matches)
    return matches[0]


def _mechanism():
    w = _wong()
    assert MECH_KEY in w, "%s missing from Raymond Wong entry" % MECH_KEY
    return w[MECH_KEY]


def _mechanism_text():
    return yaml.safe_dump(_mechanism(), allow_unicode=True)


def _count_def_tests():
    path = os.path.join(TESTS_DIR, TEST_BASENAME)
    tree = ast.parse(open(path).read())
    return sum(
        isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))
        and n.name.startswith("test_")
        for n in ast.walk(tree)
    )


def _run_git(*args):
    return subprocess.run(
        ["git"] + list(args), cwd=REPO_ROOT, capture_output=True, text=True, check=True
    )


def read_readme():
    with open(README_PATH) as f:
        return f.read()


def read_arch():
    with open(ARCH_PATH) as f:
        return f.read()


def read_log_start():
    with open(LOG_PATH) as f:
        return f.read()


class TestIterationMetadata698:
    def test_iteration_number(self):
        assert _mechanism()["iteration"] == 698

    def test_mechanism_id_next_free(self):
        assert _mechanism()["mechanism_id"] == 653

    def test_mechanism_id_unique_repo_wide(self):
        seen = {}
        for path in glob.glob(os.path.join(REPO_ROOT, "profiles", "**", "*.yaml"), recursive=True):
            text = open(path, encoding="utf-8", errors="replace").read()
            for m in re.finditer(r"mechanism_id:\s*(\d+)", text):
                if int(m.group(1)) == 653:
                    seen.setdefault(653, []).append(path)
        assert len(seen.get(653, [])) == 1, "mechanism_id 653 not unique: %r" % (seen.get(653),)

    def test_type_is_b(self):
        assert _mechanism()["type"] == "B"

    def test_goal_and_job_ids(self):
        m = _mechanism()
        assert m["goal_id"] == "goal_54093bda4145"
        assert m["job_id"] == "mediascope-daily-iteration"
        assert m["scheduled_job_id"] == "mediascope-daily-iteration"

    def test_block_key_matches(self):
        assert _mechanism()["block_key"] == "type_b_698_raymond_wong_duo_hands_on_vs_ray_ban_gen2_review_register_constancy_sep12"

    def test_first_pair_mechanism_on_wong(self):
        # #282 (Aug 24 vocabulary-concentration test) is file-local: it is
        # NOT a YAML mechanism key. This is the first YAML pair mechanism.
        w = _wong()
        other_pairs = [k for k in w if k.startswith("mechanism_") and k != MECH_KEY]
        assert not other_pairs, "unexpected second mechanism on Raymond Wong: %r" % (other_pairs,)

    def test_no_duplicate_698_file(self):
        others = [
            p for p in glob.glob(os.path.join(TESTS_DIR, "test_type_b_698_*.py"))
            if os.path.basename(p) != TEST_BASENAME
        ]
        assert not others, "duplicate #698 test files: %r" % (others,)


class TestNovelty698:
    """Iteration 698 is new; nothing with this number existed pre-commit."""

    def test_single_type_b_698_file(self):
        matches = glob.glob(os.path.join(REPO_ROOT, "tests", "test_type_b_698*.py"))
        assert len(matches) == 1, "expected exactly this file, got %r" % (matches,)
        assert matches[0].endswith(TEST_BASENAME)

    def test_type_b_698_main_commit_unique_and_anchored(self):
        # Runs green only post-main-commit per the #565 followup convention.
        # Deselect pre-commit; the followup patches ANCHORED_SHA to the real
        # main-commit SHA. Novelty was verified pre-commit by shell greps
        # (zero test_type_b_698 files, no #698 in git log, zero
        # mechanism_653 keys in profiles/, no YAML mechanism on Wong, no
        # byline-isolated review-register pair mechanism on Wong).
        out = _run_git("log", "--format=%H %s")
        mains = [
            line
            for line in out.stdout.splitlines()
            if re.match(r"^[0-9a-f]{40} Type B #698:", line)
        ]
        assert len(mains) == 1, "expected exactly one Type B #698 main commit, got %r" % (mains,)
        sha = mains[0].split()[0]
        assert sha == TestRotationCycleGuard698.ANCHORED_SHA, (
            "anchor patched in followup per #565 convention"
        )


class TestWongArms698:
    def test_apple_arm_url(self):
        assert _mechanism()["apple_arm"]["url"] == APPLE_URL

    def test_apple_arm_date(self):
        assert _mechanism()["apple_arm"]["date"] == "2026-09-09"

    def test_apple_arm_byline(self):
        arm = _mechanism()["apple_arm"]
        assert arm["byline"] == "Ray Wong (sole)"
        assert arm["byline_attribution"].startswith("full")

    def test_apple_arm_register(self):
        assert _mechanism()["apple_arm"]["register"] == "celebratory hands-on review"

    def test_apple_arm_tone(self):
        assert _mechanism()["apple_arm"]["tone_illustrative"] == APPLE_TONE

    def test_apple_arm_author_page_listed(self):
        # Verified first-hand this run: the Duo hands-on is listed on
        # https://gizmodo.com/author/raywong page 1 with the Sep 9 date.
        assert _mechanism()["apple_arm"]["author_page"] == AUTHOR_PAGE

    def test_meta_arm_url(self):
        assert _mechanism()["meta_arm"]["url"] == META_URL

    def test_meta_arm_date(self):
        assert _mechanism()["meta_arm"]["date"] == "2026-04"

    def test_meta_arm_byline_partial(self):
        arm = _mechanism()["meta_arm"]
        assert arm["byline"] == "Raymond Wong (sole)"
        # Byline header not captured in this run's render; attribution is
        # partial: photo credits + first-person voice + corpus + the
        # colleague-RW disambiguator in the sibling Display review.
        assert arm["byline_attribution"].startswith("partial")

    def test_meta_arm_register(self):
        assert _mechanism()["meta_arm"]["register"] == "hands-on product review with verdict box"

    def test_meta_arm_tone(self):
        assert _mechanism()["meta_arm"]["tone_illustrative"] == META_TONE

    def test_meta_arm_verdict_box(self):
        assert _mechanism()["meta_arm"]["verdict_score"] == 3.5

    def test_both_arms_review_register(self):
        # Genre-matched pair: both arms are hands-on review registers, unlike
        # #697's opinion-experiment vs straight-news/hands-on genre mismatch.
        m = _mechanism()
        assert "review" in m["apple_arm"]["register"]
        assert "review" in m["meta_arm"]["register"]

    def test_both_arms_read_first_hand_this_run(self):
        m = _mechanism()
        assert "first-hand" in m["apple_arm"]["evidence_grade"]
        assert "first-hand" in m["meta_arm"]["evidence_grade"]


class TestRegisterBound698:
    def test_282_test_file_exists(self):
        matches = glob.glob(
            os.path.join(TESTS_DIR, "test_raymond_wong_gizmodo_cross_entity_camera_privacy_vocabulary_concentration_aug24.py")
        )
        assert len(matches) == 1, "the #282 vocabulary-concentration test file is missing"

    def test_282_not_a_yaml_mechanism(self):
        # #282's finding is file-local; it never became a YAML mechanism key,
        # so it cannot collide with mechanism_653.
        hits = []
        for path in glob.glob(os.path.join(REPO_ROOT, "profiles", "**", "*.yaml"), recursive=True):
            text = open(path, encoding="utf-8", errors="replace").read()
            if "mechanism_282" in text:
                hits.append(path)
        assert not hits, "unexpected mechanism_282 YAML key: %r" % (hits,)

    def test_register_bound_note_present(self):
        note = _mechanism()["register_bound_note"]
        assert "news/opinion" in note["register_282"]
        assert "review" in note["register_698"]

    def test_282_bounded_not_contradicted(self):
        # The constancy found here does not extend to Wong's news/opinion
        # register, where #282's alarm-vocabulary concentration stands.
        assert _mechanism()["register_bound_note"]["contradiction"] is False

    def test_meta_positive_product_arm_in_corpus(self):
        # Wong's Jul 30 2026 "Dumb Smart Glasses AI Is Dumb No More" Meta-positive
        # product piece (in-corpus profiles/gizmodo.yaml) shows register variance
        # within his Meta coverage: alarm vocabulary is not his only Meta register.
        note = _mechanism()["register_bound_note"]
        assert "2000791752" in note["corroborating_meta_positive_url"]


class TestScorerDelta698:
    def test_delta_arithmetic(self):
        m = _mechanism()["asymmetry_scorer_result"]
        assert abs((APPLE_TONE - META_TONE) - EXPECTED_DELTA) < 1e-9
        assert m["delta_apple_minus_meta"] == EXPECTED_DELTA

    def test_stats_not_calculated(self):
        m = _mechanism()["asymmetry_scorer_result"]
        assert m["p_value"] == "NOT_CALCULATED"
        assert m["cohens_d"] == "NOT_CALCULATED"
        assert m["ci"] == "NOT_CALCULATED"

    def test_not_significant(self):
        assert _mechanism()["asymmetry_scorer_result"]["is_significant"] is False

    def test_degenerate_contract(self):
        assert _mechanism()["asymmetry_scorer_result"]["statistical_contract"] == "degenerate_n1_per_arm"

    def test_no_engine_run(self):
        assert "no engine run" in _mechanism()["asymmetry_scorer_result"]["method"]

    def test_not_artifact_grade(self):
        assert _mechanism()["asymmetry_scorer_result"]["artifact_grade"] is False

    def test_twentieth_member(self):
        assert "TWENTIETH" in _mechanism()["verdict"]


class TestFinancialContext698:
    def test_gizmodo_financial_tie_none_both(self):
        fc = _mechanism()["financial_context"]
        assert fc["predictor"] == "null_tie_control"
        assert fc["prediction"] == "no_differential_prediction"

    def test_keleops_ownership_noted(self):
        assert "Keleops" in _mechanism()["financial_context"]["detail"]

    def test_zero_gradient_control(self):
        assert "zero-gradient" in _mechanism()["financial_context"]["detail"]

    def test_correlation_not_causation(self):
        assert "Correlation, not causation" in _mechanism()["financial_context"]["detail"]

    def test_journalist_attribution_level(self):
        # The falsification here is at the journalist-attribution level
        # (Wong's byline), not the deal-gradient level (no gradient exists).
        assert "journalist-attribution" in _mechanism()["financial_context"]["detail"]


class TestConfounders698:
    def test_confounder_count(self):
        assert len(_mechanism()["confounders"]) == 7

    def test_strong_confounds_ranked_first(self):
        confs = _mechanism()["confounders"]
        assert confs[0].startswith("[STRONG]")
        assert confs[1].startswith("[STRONG]")
        assert confs[2].startswith("[STRONG]")

    def test_partial_byline_is_strong_confound(self):
        confs = _mechanism()["confounders"]
        assert "partial" in confs[0].lower() or "byline" in confs[0].lower()

    def test_moderate_confounds_present(self):
        confs = _mechanism()["confounders"]
        mods = [c for c in confs if c.startswith("[MODERATE]")]
        assert len(mods) == 3

    def test_weak_confound_present(self):
        confs = _mechanism()["confounders"]
        weaks = [c for c in confs if c.startswith("[WEAK]")]
        assert len(weaks) == 1

    def test_register_bound_among_confounds(self):
        assert any("#282" in c for c in _mechanism()["confounders"])


class TestRotationCycleGuard698:
    # Deselected pre-commit per the #565 followup convention; the rotation
    # window only closes once the #698 main commit exists.
    ANCHORED_SHA = "a7f061751058c7cbfd7859f2d349992e11755120"

    @staticmethod
    def _mains():
        out = _run_git("log", "--format=%s")
        return [s for s in out.stdout.splitlines() if re.match(r"^Type [A-E] #\d+:", s)]

    def test_window_694_698_closes_a_to_b(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m, "unparseable rotation subject: %r" % (s,)
            observed.append((m.group(1), m.group(2)))
        assert observed == [
            ("B", "698"),
            ("A", "697"),
            ("E", "696"),
            ("D", "695"),
            ("C", "694"),
        ], "rotation window 694-698 wrong: %r" % (observed,)

    def test_rotation_adjacency_cycle_valid(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m
            observed.append(m.group(1))
        assert observed == ["B", "A", "E", "D", "C"]
        order = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
        for a, b in zip(observed, observed[1:]):
            assert (order[a] - order[b]) % 5 == 1, (
                "rotation broken: %s -> %s is not a valid cycle edge" % (a, b)
            )

    def test_anchor_is_main_patch_in_followup(self):
        # Post-commit anchor: the #698 main commit. Patched in the followup
        # per the #565 convention once the main commit SHA is known.
        pytest.skip("anchor patched in followup per #565 convention")

    def test_rotation_guard_regex_actually_matches(self):
        # #632 process note: a rotation guard whose regex never matches is a
        # silent no-op. Verify the guard regexes match a real main-commit
        # subject (the double-backslash r"...#(\d+)..." form silently matches
        # nothing). Written as a semantic check rather than a literal-pattern
        # check so the test cannot defeat itself by containing the pattern.
        src = open(os.path.join(TESTS_DIR, TEST_BASENAME)).read()
        patterns = re.findall(r're\.search\(r"([^"]+)"', src)
        guard_patterns = [p for p in patterns if p.startswith("Type (")]
        assert guard_patterns, "no rotation-guard regex found in this file"
        sample = "Type B #698: Raymond Wong Duo hands-on vs Ray-Ban Gen 2 review register constancy"
        for p in guard_patterns:
            m = re.search(p, sample)
            assert m and m.group(1) == "B" and m.group(2) == "698", (
                "rotation regex %r fails to match a real subject "
                "(double-backslash bug?)" % (p,)
            )


class TestDocSyncRatchet698:
    # Fails pre-commit by design per the #565 followup convention; the README
    # test-file table row and ARCHITECTURE tree row land in the doc-sync commit.
    def test_readme_has_698_row(self):
        assert "test_type_b_698" in read_readme()

    def test_arch_has_698_row(self):
        assert "test_type_b_698" in read_arch()

    def test_readme_row_mentions_wong(self):
        assert "Raymond Wong" in read_readme()

    def test_log_starts_with_698(self):
        assert read_log_start().startswith("#698 Type B:")

    def test_def_test_count_matches(self):
        # The README row for #698 must carry this file's own def-test count.
        n = _count_def_tests()
        assert str(n) in read_readme(), (
            "README #698 row should mention this file's def-test count %d" % n
        )


class TestNoBrittlePatterns698:
    def test_yaml_reparses_clean(self):
        w = _wong()
        m = w[MECH_KEY]
        assert isinstance(m["mechanism_id"], int)
        assert isinstance(m["apple_arm"]["tone_illustrative"], float)
        assert isinstance(m["meta_arm"]["tone_illustrative"], float)
        assert isinstance(m["asymmetry_scorer_result"]["is_significant"], bool)

    def test_no_em_dash_in_mechanism(self):
        assert "\u2014" not in _mechanism_text()
        assert "\u2028" not in _mechanism_text()
        src = open(os.path.join(TESTS_DIR, TEST_BASENAME)).read()
        assert "\u2014" not in src
        assert "\u2028" not in src

    def test_all_urls_http_or_https(self):
        urls = [
            _mechanism()["apple_arm"]["url"],
            _mechanism()["meta_arm"]["url"],
            _mechanism()["apple_arm"]["author_page"],
            _mechanism()["register_bound_note"]["corroborating_meta_positive_url"],
        ]
        for u in urls:
            assert u.startswith("http"), "non-http URL: %r" % (u,)

    def test_pair_shape_declared(self):
        assert _mechanism()["pair_shape"] == "same-journalist cross-entity byline-isolated review-register pair"
