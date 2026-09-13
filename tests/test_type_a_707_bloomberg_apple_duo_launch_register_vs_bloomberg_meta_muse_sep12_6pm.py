"""Type A #707 (2026-09-12 18:00 PDT): Bloomberg x Apple iPhone Duo
launch register vs Bloomberg x Meta Muse register (mechanism 658).

First dedicated Bloomberg x Apple Duo Type A mechanism; first Bloomberg x
Meta Muse mechanism. Sixth publication in the Duo launch-genre series (WSJ
#662, Verge #687, Reuters #692, Gizmodo #697, Fast Company #702).

Apple arm (Bloomberg News via Bloomberg Law syndication, Sep 9, excerpt-
bounded this run: browser.open failed upstream, terminal per turn, so the
verbatim title, lede and Full-URL listing were read from the search result
per the #503 second-hand evidence-grade precedent; the syndication page is
gated beyond the lede): "Apple Debuts Foldable Duo in Biggest-Ever iPhone
Revamp (1)" (https://news.bloomberglaw.com/artificial-intelligence/apple-debuts-iphone-pro-airpods-ahead-of-foldable-unveiling-1):
'Apple Inc. unveiled the company's first foldable smartphone during a
wide-ranging event Wednesday, betting that a new category can energize
growth for its biggest-selling lineup'; 'The device, called the iPhone
Duo, will improve on rivals' foldable models, newly appointed Chief
Executive Officer John Ternus said, mocking competing handsets as "two
phones awkwardly stuck together"'; 'The Duo unfolds to reveal a 7.6-inch
(19.3-centimeter) screen, the largest display ever on an iPhone';
business-growth launch-celebration register; scored +0.40.

Meta arm (Bloomberg News via Bloomberg Tax syndication, Sep 8, excerpt-
bounded this run, same terminal browser.open failure): "Meta Debuts AI
Assistant for Personal Tasks and Organization" (https://news.bloombergtax.com/artificial-intelligence/meta-debuts-ai-assistant-for-personal-tasks-and-organization):
'Meta Platforms Inc. unveiled a new artificial intelligence agent designed
to carry out tasks on a user's behalf, advancing Mark Zuckerberg's vision
of a future where people each have a personalized AI assistant'; 'Called
Muse, the new agent shares its name with the series of models Meta's AI
lab is developing and can help automate a variety of tasks'; neutral
capability listing (shopping, tickets, scheduling), no trust/surveillance
caveats visible in the accessible lede; scored +0.05.

Scorer (MANUAL ILLUSTRATIVE, standing rule Aug 28 2026; arithmetic
only): Apple [+0.40] vs Meta [+0.05]. Delta (Apple minus Meta) +0.35.
p_value NOT_CALCULATED, cohens_d NOT_CALCULATED, ci NOT_CALCULATED,
is_significant False, artifact_grade False. Classic degenerate
statistical contract per the #638/#643 convention (n=1 vs n=1, t=0.0,
p=1.0, d=0.0); engine NOT run; no divergence pin.

Financial context (correlation, not causation): Bloomberg LP carries NO
known AI licensing deal with Apple or Meta on record (bounded absence
this run). This is a ZERO-GRADIENT CONTROL: the incentive theory makes
no differential prediction, so the observed +0.35 gap cannot contradict
it. NOT a falsification-family member; the ledger stands at 21 after
#703's TWENTY-FIRST (m656). Parmy Olson's Bloomberg Opinion register-
constancy finding (#703/m656) is a journalist-level book incentive at a
distinct desk from Bloomberg News launch coverage.

Publication-genre boundary: sixth publication in the Duo launch-genre
series - WSJ celebrated (+0.45, #662/m631), The Verge celebrated (+0.38
avg, #687/m646), Reuters ran skeptical (-0.05 avg, #692/m649), Gizmodo
celebrated (+0.325 avg, #697/m652), Fast Company celebrated (+0.35,
#702/m655), Bloomberg celebrated (+0.40). The launch-celebration register
holds at tech/business press and breaks at the wire.

Strongest counterarguments (accepted as major counterweights): (1) the
pair is excerpt-bounded - both pieces are gated behind Bloomberg Law/Tax
login walls and browser.open failed upstream this run, so moderating
passages (including trust/surveillance caveats in the Muse piece) may
exist beyond the ledes; the +0.05 Meta read is lede-pinned, not
body-verified, per #503; (2) syndication-surface mismatch - the Apple
arm was served from Bloomberg Law's AI vertical and the Meta arm from
Bloomberg Tax's AI vertical, so the underlying Bloomberg News desks may
differ; (3) provenance advantage - the Duo naming scoop itself came from
Bloomberg's Mark Gurman, so own-scoop pride may inflate the celebratory
register independent of entity preference; (4) hardware vs software
launch genre mismatch may carry part of the register gap. Claim stays
bounded, directional, correlation-only, MANUAL ILLUSTRATIVE.

Evidence hygiene: both URLs copied verbatim from this run's Full-URL
listings; no canonical URLs invented; no zero-coverage claims; no em
dashes; ASCII-only.

Designed supersession: #705's test_no_mechanism_658_in_profiles and
test_no_mechanism_658_in_tests fail by design this run (same convention
as #650's 624/625, #695's 649, #697's 652, #702's 655, #703's 656, and
#704's 657 supersession); this file's TestSweepSupersession707 pins the
new state (max mechanism 658, exactly one mechanism_658 key).

Durable conventions (from #495): line-anchored (^, re.MULTILINE) heading
search in iteration-log.md; relative newest-first ordering between
neighbors, never absolute-top or fixed head slices.
"""

import glob
import os
import re
import subprocess

import pytest
import yaml

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TEST_BASENAME = os.path.basename(__file__)
PROFILE_PATH = os.path.join(REPO_ROOT, "profiles", "competitor-entities.yaml")
LOG_PATH = os.path.join(REPO_ROOT, "iteration-log.md")

MECH_KEY = "mechanism_658_bloomberg_apple_duo_launch_register_vs_bloomberg_meta_muse_register_sep12"

DUO_URL = "https://news.bloomberglaw.com/artificial-intelligence/apple-debuts-iphone-pro-airpods-ahead-of-foldable-unveiling-1"
MUSE_URL = "https://news.bloombergtax.com/artificial-intelligence/meta-debuts-ai-assistant-for-personal-tasks-and-organization"

TARGET_SCORES = [0.4]
PEER_SCORES = [0.05]
TARGET_AVG = 0.4
PEER_AVG = 0.05
EXPECTED_DELTA = 0.35


def _run_git(*args):
    return subprocess.run(
        ["git", "-C", REPO_ROOT, *args],
        capture_output=True,
        text=True,
    )


def _profile():
    with open(PROFILE_PATH) as f:
        return yaml.safe_load(f)


def _entity():
    return _profile()["entities"]["apple"]


def _mechanism():
    return _entity()[MECH_KEY]


def _read(path):
    with open(path) as f:
        return f.read()


class TestNovelty707:
    """Iteration 707 is new; nothing with this number existed pre-commit."""

    def test_single_type_a_707_file(self):
        matches = glob.glob(os.path.join(REPO_ROOT, "tests", "test_type_a_707*.py"))
        assert len(matches) == 1, "expected exactly this file, got %r" % (matches,)
        assert matches[0].endswith(TEST_BASENAME)

    def test_type_a_707_main_commit_unique_and_anchored(self):
        # Runs green only post-main-commit per the #565 followup convention.
        # Deselect pre-commit; the followup patches ANCHORED_SHA to the real
        # main-commit SHA. Novelty was verified pre-commit by shell greps
        # (zero test_type_a_707 files, no #707 in git log, zero
        # mechanism_658 keys in profiles/ pre-commit, max mechanism 657,
        # both Bloomberg URLs new to corpus repo-wide).
        out = _run_git("log", "--format=%H %s")
        mains = [
            line
            for line in out.stdout.splitlines()
            if re.match(r"^[0-9a-f]{40} Type A #707:", line)
        ]
        assert len(mains) == 1, "expected exactly one Type A #707 main commit, got %r" % (mains,)
        sha = mains[0].split()[0]
        assert sha == TestRotationCycleGuard707.ANCHORED_SHA, (
            "anchor patched in followup per #565 convention"
        )


class TestMechanismExistsAndShape:
    def test_mechanism_key_present_under_apple_entity(self):
        assert MECH_KEY in _entity()

    def test_mechanism_id_is_next_free(self):
        assert _mechanism()["mechanism_id"] == 658

    def test_identity_fields(self):
        m = _mechanism()
        assert m["iteration"] == 707
        assert m["iteration_type"] == "A"
        assert m["date_analyzed"] == "2026-09-12"
        assert m["publication_focus"] == "bloomberg"
        assert m["competitor"] == "apple"

    def test_author_kit_with_ray(self):
        assert _mechanism()["author"] == "Kit (with Ray)"

    def test_no_line_separators_in_block(self):
        # Guards the 2026-09-10 muse.write U+2028/U+2029 lesson.
        text = _read(PROFILE_PATH)
        start = text.index(MECH_KEY)
        end = text.index("\n  google:", start)
        assert " " not in text[start:end]
        assert " " not in text[start:end]

    def test_test_file_field_matches_this_file(self):
        assert _mechanism()["test_file"].endswith(TEST_BASENAME)

    def test_event_frame(self):
        m = _mechanism()
        assert "iPhone Duo" in m["event"]
        assert "Muse" in m["event"]
        assert "Bloomberg" in m["event"]


class TestAppleArm:
    def _arm(self):
        return _mechanism()["apple_arm"]

    def test_one_item(self):
        assert len(self._arm()["items"]) == 1

    def test_duo_url_verbatim(self):
        assert self._arm()["items"][0]["url"] == DUO_URL

    def test_duo_register_tone_and_quotes(self):
        item = self._arm()["items"][0]
        assert item["register"] == "business_growth_launch_celebration"
        assert item["manual_illustrative_tone"] == 0.4
        assert "Biggest-Ever iPhone Revamp" in item["title"]
        assert "energize growth" in item["key_framing"]
        assert "two phones awkwardly stuck together" in item["key_framing"]
        assert "largest display ever on an iPhone" in item["key_framing"]
        assert "John Ternus" in item["key_framing"]
        assert "excerpt-bounded" in item["source_note"]

    def test_apple_arm_average(self):
        assert self._arm()["average_manual_illustrative"] == TARGET_AVG


class TestMetaArm:
    def _arm(self):
        return _mechanism()["meta_arm"]

    def test_new_to_corpus_this_run(self):
        assert "new to corpus this run" in self._arm()["carried_from"]

    def test_one_item(self):
        assert len(self._arm()["items"]) == 1

    def test_muse_url_verbatim(self):
        assert self._arm()["items"][0]["url"] == MUSE_URL

    def test_muse_register_tone_and_quotes(self):
        item = self._arm()["items"][0]
        assert item["register"] == "neutral_capability_listing"
        assert item["manual_illustrative_tone"] == 0.05
        assert "AI Assistant for Personal Tasks and Organization" in item["title"]
        assert "advancing Mark Zuckerberg" in item["key_framing"]
        assert "carry out tasks on a user" in item["key_framing"]
        assert "no trust/surveillance caveats visible in the accessible lede" in item["key_framing"]
        assert "excerpt-bounded" in item["source_note"]

    def test_meta_arm_average(self):
        assert self._arm()["average_manual_illustrative"] == PEER_AVG


class TestScorer707:
    def _s(self):
        return _mechanism()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]

    def test_arrays(self):
        s = self._s()
        assert s["target_scores_MANUAL_ILLUSTRATIVE"] == TARGET_SCORES
        assert s["peer_scores_MANUAL_ILLUSTRATIVE"] == PEER_SCORES
        assert s["target_avg"] == TARGET_AVG
        assert s["peer_avg"] == PEER_AVG

    def test_arithmetic(self):
        s = self._s()
        assert s["delta_manual_illustrative"] == EXPECTED_DELTA
        assert abs((s["target_avg"] - s["peer_avg"]) - EXPECTED_DELTA) < 1e-9
        assert s["delta_calc"] == "0.4 - 0.05 = 0.35"

    def test_manual_illustrative_guards(self):
        s = self._s()
        assert "MANUAL ILLUSTRATIVE" in s["methodology"]
        assert "DO NOT claim empirical significance" in s["methodology"]
        assert "classic degenerate statistical contract" in s["engine_degenerate"]
        assert "Engine NOT run" in s["engine_degenerate"]

    def test_finding_layer_not_significant(self):
        layer = self._s()["finding_layer"]
        assert "NOT_CALCULATED" in layer
        assert "is_significant False" in layer

    def test_no_divergence_pin(self):
        assert "no divergence pin" in self._s()["engine_degenerate"]

    def test_artifact_grade_false(self):
        assert self._s()["artifact_grade"] is False


class TestFalsificationFamily707:
    def _f(self):
        return _mechanism()["falsification_family"]

    def test_not_a_member_zero_gradient_control(self):
        assert "NOT a falsification-family member" in self._f()["membership"]
        assert "zero-gradient control" in self._f()["membership"]
        assert "Ledger stands at 21" in self._f()["membership"]

    def test_prediction_silent(self):
        assert "no differential prediction" in self._f()["prediction"]
        assert "no known paid AI content licensing deal" in self._f()["prediction"]

    def test_observed_gap_not_contradiction(self):
        assert "+0.35" in self._f()["observed"]
        assert "not a theory contradiction" in self._f()["observed"]

    def test_no_within_arm_range(self):
        assert "no within-arm range exists" in self._f()["within_arm_range_vs_gap"]

    def test_publication_genre_boundary_sixth(self):
        b = self._f()["publication_genre_boundary"]
        assert "sixth publication" in b
        assert "#662" in b and "#687" in b and "#692" in b and "#697" in b and "#702" in b

    def test_financial_context_null_tie(self):
        fc = _mechanism()["financial_context"]
        assert fc["predictor"] == "null_tie_control"
        assert fc["prediction"] == "no_differential_prediction"
        assert "NOT a falsification-family member" in fc["status"]


class TestConfoundersAndCrossRefs:
    def test_confounders_present(self):
        c = _mechanism()["confounders_ranked"]
        assert len(c["strong"]) == 3
        assert len(c["moderate"]) == 4
        assert len(c["weak"]) == 2

    def test_strongest_counterarguments_accepted(self):
        strong = " ".join(_mechanism()["confounders_ranked"]["strong"])
        assert "excerpt-bounded" in strong
        assert "browser.open failed upstream" in strong
        assert "own-scoop pride" in strong

    def test_counterevidence_present(self):
        ce = _mechanism()["counterevidence"]
        assert len(ce) == 4
        assert any("#692" in x for x in ce)
        assert any("#703" in x for x in ce)

    def test_cross_references(self):
        cr = _mechanism()["cross_references"]
        text = " ".join(cr)
        for ref in ["#662", "#687", "#692", "#697", "#702", "#703", "#593", "#587", "#627", "#638", "#503", "#705", "#565"]:
            assert ref in text, "missing cross-reference %s" % ref

    def test_novelty_documents_supersession(self):
        n = _mechanism()["novelty"]
        assert "First dedicated Bloomberg x Apple Duo Type A mechanism" in n
        assert "designed supersession" in n
        assert "mechanism 658" in n

    def test_research_method_documents_excerpt_bounded(self):
        rm = _mechanism()["research_method"]
        assert "browser.open attempts" in rm
        assert "failed upstream" in rm
        assert "excerpt-bounded" in rm
        assert "Bloomberg" in rm
        assert "iteration-492 rule" in rm


class TestIterationLog707:
    def test_log_starts_with_707(self):
        text = _read(LOG_PATH)
        first = re.search(r"(?m)^#\d+ ", text)
        assert first is not None
        assert first.group(0) == "#707 "

    def test_log_entry_relative_order(self):
        text = _read(LOG_PATH)
        ids = re.findall(r"(?m)^#(\d+) Type [A-E]:", text)
        assert ids[0] == "707"
        assert ids[1] == "706"
        assert ids[2] == "705"

    def test_log_entry_content(self):
        text = _read(LOG_PATH)
        start = text.index("#707 Type A")
        entry = text[start:start + 9000]
        assert "mechanism 658" in entry
        assert "NOT a falsification-family member" in entry
        assert "MANUAL ILLUSTRATIVE" in entry
        assert "+0.35" in entry


class TestRotationCycleGuard707:
    """Rotation window 703-707 closes B->A. Anchor patched in followup per #565."""

    ANCHORED_SHA = "PLACEHOLDER_PATCHED_IN_FOLLOWUP"

    def _window(self):
        text = _read(LOG_PATH)
        heads = re.findall(r"(?m)^#(\d+) Type ([A-E]):", text)
        return [(int(n), t) for n, t in heads]

    def test_window_703_707_closes_b_to_a(self):
        window = self._window()[:5]
        assert window == [(707, "A"), (706, "E"), (705, "D"), (704, "C"), (703, "B")], window

    def test_rotation_adjacency_cycle_valid(self):
        order = {"A": "B", "B": "C", "C": "D", "D": "E", "E": "A"}
        window = self._window()[:5]
        for (n_newer, t_newer), (n_older, t_older) in zip(window, window[1:]):
            assert order[t_older] == t_newer, (n_newer, t_newer, n_older, t_older)

    def test_anchor_is_main_commit_patched_in_followup(self):
        pytest.skip("anchor patched in followup per #565 convention")


class TestDocSync707:
    def test_readme_has_row(self):
        text = _read(os.path.join(REPO_ROOT, "README.md"))
        assert TEST_BASENAME in text

    def test_architecture_has_row(self):
        text = _read(os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md"))
        assert TEST_BASENAME in text


class TestSweepSupersession707:
    """Pins the post-#707 state; documents #705's no-658 sweep designed supersession."""

    def test_max_mechanism_id_is_658(self):
        text = _read(PROFILE_PATH)
        ids = [int(x) for x in re.findall(r"mechanism_id:\s*(\d+)\b", text)]
        modern = [i for i in ids if i >= 600]
        assert max(modern) == 658, max(modern)

    def test_exactly_one_mechanism_658_key(self):
        text = _read(PROFILE_PATH)
        keys = re.findall(r"(?m)^    mechanism_658_\w+:", text)
        assert keys == [
            "    mechanism_658_bloomberg_apple_duo_launch_register_vs_bloomberg_meta_muse_register_sep12:"
        ], keys
