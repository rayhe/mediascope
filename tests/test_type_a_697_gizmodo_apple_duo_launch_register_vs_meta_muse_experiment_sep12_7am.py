"""Type A #697 (2026-09-12 07:00 PDT): Gizmodo x Apple iPhone Duo launch
register vs Gizmodo x Meta Muse experiment register (mechanism 652).

First dedicated Gizmodo x Apple Duo Type A mechanism; second Gizmodo x
Apple Type A overall (after #587's Sep 7 null-tie control, old schema
under profiles/gizmodo.yaml). Fourth publication in the Duo
launch-genre series (WSJ #662, Verge #687, Reuters #692).

Apple arm (Gizmodo, Sep 9, both read first-hand this run): (1) launch
news "Apple's Foldable iPhone Is Officially Called the iPhone Duo"
(https://gizmodo.com/iphone-duo-2000808898, 42 rendered lines):
'one more thing' at the 'Surprise and Shine' event, 'the first wholly
new iPhone form factor', 'Apple being Apple, of course, the corners are
rounded', thinnest iPhone ever unfolded, 5.4-inch outer / 7.6-inch inner
screens, iOS 27 dock moved right, Pencil support later, A20 chip,
'Color choices aren't much to write home about... But alas, dark and
light is all we get', 256GB 'start at a whopping $1,999', pre-order Oct
16 / sales Oct 23, correction note (7.6 not 7.8 inches); scored +0.20.
(2) hands-on "iPhone Duo Hands-On: The Inner Screen Looks Like Real
Paper" by Ray Wong (https://gizmodo.com/iphone-duo-hands-on-2000808932,
78 rendered lines): 'a stunning device to hold in your hands',
'immediately marveled at the iPhone Duo's thinness', inner screen
'absolutely gorgeous. It looks like paper; it's not reflective at all',
'Holy shit the nano texture inner screen on iPhone Duo looks like
paper', 'I can't stop thinking about the transition animation',
'Apple may have made the most desirable foldable ever created';
caveats: 'the crease is not completely invisible', Face ID loss 'feels
like a step backward', '$2,000 or more' unanswered; scored +0.45.
Apple arm average +0.325.

Meta arm (Gizmodo, Sep 9, read first-hand this run, 90 rendered lines):
"Meta's Muse Let Me Waste a Mind-Boggling Amount of Free Compute on
Nothing in Particular"
(https://gizmodo.com/metas-muse-let-me-waste-a-mind-boggling-amount-of-free-compute-on-nothing-in-particular-2000808945):
100M free tokens/week; 'Meta is shoveling ungodly amounts of money into
compute' ($145B capex, 91% FCF drop); Kantrowitz: Meta AI users
'bumping into it instead' of seeking it out; 'I don't have any busywork
that I trust an agent to do'; author tokenmaxxed, 'astonished that I
wasn't even getting close to being cut off'; agents 'splatter out the
bare minimum'; 'it's still a very bad game'; 'the sheer volume of slop
Meta is letting free users generate'; 'None of this should be mistaken
for a product review'; capability admitted ('The Paint application
works', three games plus a bootable fake Mac). Scored -0.25.

Scorer (MANUAL ILLUSTRATIVE, standing rule Aug 28 2026; arithmetic
only): Apple [0.20, 0.45] avg +0.325 vs Meta [-0.25] avg -0.25. Delta
(Apple minus Meta) +0.575. p_value NOT_CALCULATED, cohens_d
NOT_CALCULATED, ci NOT_CALCULATED, is_significant False, artifact_grade
False. Degenerate statistical contract per the #638/#643 convention
(n=2 vs n=1); engine NOT run; no divergence pin.

Financial context (correlation, not causation): Gizmodo carries NO known
AI licensing deal with either Apple or Meta (both financial_tie none in
profiles/gizmodo.yaml competitor_relationships). This is a
ZERO-GRADIENT CONTROL: the incentive theory makes no differential
prediction, so the observed +0.575 gap cannot contradict it. NOT a
falsification-family member; the ledger stands at 19 after #693's
NINETEENTH.

Publication-genre boundary: fourth publication in the Duo launch-genre
series - WSJ celebrated (+0.45, #662/m631), The Verge celebrated (+0.38
avg, #687/m646), Reuters ran skeptical (-0.05 avg, #692/m649), Gizmodo
celebrated (+0.325 avg). The launch-celebration register holds at tech
press and breaks at the wire.

Strongest counterarguments (accepted as major counterweights): (1) the
genre mismatch dominates the gap - the Meta arm is a playful
experiment/essay that explicitly disclaims review status while the Apple
arms are straight launch news and an on-site hands-on; the #627
verbatim-URL discipline does not fix genre asymmetry; (2) news-peg
valence skew - the Muse piece is anchored on Meta's free-compute
economics and capex-overbuild critique while the Duo pieces are anchored
on hardware delight at a launch event; (3) the access economy - both Duo
pieces were filed from Apple's Steve Jobs Theater event while the Muse
piece was a desk experiment on a free account. Unlike #637/#692, the
within-Apple-arm range (0.25) is SMALLER than the gap (0.575), so
internal variance does not account for the delta; the genre-mismatch
confound carries the load. Claim stays bounded, directional,
correlation-only, MANUAL ILLUSTRATIVE.

Evidence hygiene: FT, Guardian, WIRED, and Business Insider queries did
not surface usable same-publication Apple Duo and Meta Muse pairs
(bounded search-result absence per iteration-492, not noncoverage); the
run pivoted to Gizmodo where verbatim URLs for both pegs surfaced in
this run's Full-URL listings and all three pieces were read first-hand;
no canonical URLs invented; no zero-coverage claims; no em dashes;
ASCII-only.

Designed supersession: #695's test_max_modern_mechanism_id_is_651,
test_no_mechanism_652_in_profiles, test_no_mechanism_652_key_in_profiles,
and test_no_mechanism_652_in_tests fail by design this run (same
convention as #650's 624/625 and #695's own 649 supersession); this
file's TestSweepSupersession697 pins the new state (max mechanism 652,
exactly one mechanism_652).

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

MECH_KEY = "mechanism_652_gizmodo_apple_duo_launch_register_vs_gizmodo_meta_muse_experiment_sep12"

DUO_LAUNCH_URL = "https://gizmodo.com/iphone-duo-2000808898"
DUO_HANDSON_URL = "https://gizmodo.com/iphone-duo-hands-on-2000808932"
MUSE_URL = "https://gizmodo.com/metas-muse-let-me-waste-a-mind-boggling-amount-of-free-compute-on-nothing-in-particular-2000808945"

TARGET_SCORES = [0.2, 0.45]
PEER_SCORES = [-0.25]
TARGET_AVG = 0.325
PEER_AVG = -0.25
EXPECTED_DELTA = 0.575


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


class TestNovelty697:
    """Iteration 697 is new; nothing with this number existed pre-commit."""

    def test_single_type_a_697_file(self):
        matches = glob.glob(os.path.join(REPO_ROOT, "tests", "test_type_a_697*.py"))
        assert len(matches) == 1, "expected exactly this file, got %r" % (matches,)
        assert matches[0].endswith(TEST_BASENAME)

    def test_type_a_697_main_commit_unique_and_anchored(self):
        # Runs green only post-main-commit per the #565 followup convention.
        # Deselect pre-commit; the followup patches ANCHORED_SHA to the real
        # main-commit SHA. Novelty was verified pre-commit by shell greps
        # (zero test_type_a_697 files, no #697 in git log, zero
        # mechanism_652 keys in profiles/, no dedicated Gizmodo x Apple
        # Duo Type A; all three Gizmodo URLs new to corpus).
        out = _run_git("log", "--format=%H %s")
        mains = [
            line
            for line in out.stdout.splitlines()
            if re.match(r"^[0-9a-f]{40} Type A #697:", line)
        ]
        assert len(mains) == 1, "expected exactly one Type A #697 main commit, got %r" % (mains,)
        sha = mains[0].split()[0]
        assert sha == TestRotationCycleGuard697.ANCHORED_SHA, (
            "anchor patched in followup per #565 convention"
        )


class TestMechanismExistsAndShape:
    def test_mechanism_key_present_under_apple_entity(self):
        assert MECH_KEY in _entity()

    def test_mechanism_id_is_next_free(self):
        assert _mechanism()["mechanism_id"] == 652

    def test_identity_fields(self):
        m = _mechanism()
        assert m["iteration"] == 697
        assert m["iteration_type"] == "A"
        assert m["date_analyzed"] == "2026-09-12"
        assert m["publication_focus"] == "gizmodo"
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


class TestAppleArm:
    def _items(self):
        return _mechanism()["apple_arm"]["items"]

    def test_two_items(self):
        assert len(self._items()) == 2

    def test_launch_url_verbatim(self):
        assert self._items()[0]["url"] == DUO_LAUNCH_URL

    def test_launch_register_and_tone(self):
        item = self._items()[0]
        assert item["register"] == "product_launch_forward"
        assert item["manual_illustrative_tone"] == 0.2
        assert "first wholly new iPhone form factor" in item["key_framing"]
        assert "Apple being Apple" in item["key_framing"]
        assert "whopping $1,999" in item["key_framing"]
        assert "first-hand" in item["source_note"]
        assert "42 rendered lines" in item["source_note"]

    def test_handson_url_verbatim(self):
        assert self._items()[1]["url"] == DUO_HANDSON_URL

    def test_handson_byline_ray_wong(self):
        assert "Ray Wong" in self._items()[1]["byline"]

    def test_handson_register_tone_and_quotes(self):
        item = self._items()[1]
        assert item["register"] == "celebratory_hands_on"
        assert item["manual_illustrative_tone"] == 0.45
        assert "stunning device to hold in your hands" in item["key_framing"]
        assert "looks like paper" in item["key_framing"]
        assert "most desirable foldable ever created" in item["key_framing"]
        assert "step backward" in item["key_framing"]
        assert "78 rendered lines" in item["source_note"]

    def test_apple_arm_average(self):
        assert _mechanism()["apple_arm"]["average_manual_illustrative"] == TARGET_AVG


class TestMetaArm:
    def _items(self):
        return _mechanism()["meta_arm"]["items"]

    def test_new_to_corpus_this_run(self):
        assert "new to corpus this run" in _mechanism()["meta_arm"]["carried_from"]

    def test_muse_url_verbatim(self):
        assert self._items()[0]["url"] == MUSE_URL

    def test_muse_register_tone_and_quotes(self):
        item = self._items()[0]
        assert item["register"] == "skeptical_playful_experiment"
        assert item["manual_illustrative_tone"] == -0.25
        assert "shoveling ungodly amounts of money into compute" in item["key_framing"]
        assert "slop Meta is letting free users generate" in item["key_framing"]
        assert "None of this should be mistaken for a product review" in item["key_framing"]
        assert "90 rendered lines" in item["source_note"]

    def test_meta_arm_average(self):
        assert _mechanism()["meta_arm"]["average_manual_illustrative"] == PEER_AVG


class TestScorer697:
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
        assert s["delta_calc"] == "0.325 - (-0.25) = 0.575"

    def test_manual_illustrative_guards(self):
        s = self._s()
        assert "MANUAL ILLUSTRATIVE" in s["methodology"]
        assert "DO NOT claim empirical significance" in s["methodology"]
        assert "degenerate statistical contract" in s["engine_degenerate"]
        assert "Engine NOT run" in s["engine_degenerate"]

    def test_finding_layer_not_significant(self):
        layer = self._s()["finding_layer"]
        assert "NOT_CALCULATED" in layer
        assert "is_significant False" in layer

    def test_no_divergence_pin(self):
        assert "no divergence pin" in self._s()["engine_degenerate"]

    def test_artifact_grade_false(self):
        assert self._s()["artifact_grade"] is False


class TestFalsificationFamily697:
    def _f(self):
        return _mechanism()["falsification_family"]

    def test_not_a_member_zero_gradient_control(self):
        assert "NOT a falsification-family member" in self._f()["membership"]
        assert "zero-gradient control" in self._f()["membership"]
        assert "Ledger stands at 19" in self._f()["membership"]

    def test_prediction_silent(self):
        assert "no differential prediction" in self._f()["prediction"]
        assert "financial_tie none" in self._f()["prediction"]

    def test_observed_gap_not_contradiction(self):
        assert "+0.575" in self._f()["observed"]
        assert "not a theory contradiction" in self._f()["observed"]

    def test_within_arm_range_smaller_than_gap(self):
        assert "SMALLER than the between-entity gap" in self._f()["within_arm_range_vs_gap"]
        assert "0.25" in self._f()["within_arm_range_vs_gap"]

    def test_publication_genre_boundary_fourth(self):
        b = self._f()["publication_genre_boundary"]
        assert "fourth publication" in b
        assert "#662" in b and "#687" in b and "#692" in b

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
        assert len(c["weak"]) == 3

    def test_strongest_counterarguments_accepted(self):
        strong = " ".join(_mechanism()["confounders_ranked"]["strong"])
        assert "conflates genre with entity preference" in strong
        assert "track their news pegs" in strong
        assert "access differential" in strong

    def test_counterevidence_present(self):
        ce = _mechanism()["counterevidence"]
        assert len(ce) == 4
        assert any("#587" in x for x in ce)
        assert any("#692" in x for x in ce)

    def test_cross_references(self):
        cr = _mechanism()["cross_references"]
        text = " ".join(cr)
        for ref in ["#662", "#687", "#692", "#587", "#627", "#693", "#638", "#695", "#565"]:
            assert ref in text, "missing cross-reference %s" % ref

    def test_novelty_documents_supersession(self):
        n = _mechanism()["novelty"]
        assert "First dedicated Gizmodo x Apple Duo Type A mechanism" in n
        assert "designed supersession" in n
        assert "mechanism 652" in n

    def test_research_method_documents_ft_guardian_wired_bi_pivot(self):
        rm = _mechanism()["research_method"]
        assert "FT" in rm and "Guardian" in rm and "Wired" in rm
        assert "iteration-492 rule" in rm
        assert "first-hand browser.opens" in rm


class TestIterationLog697:
    def test_log_starts_with_697(self):
        text = _read(LOG_PATH)
        first = re.search(r"(?m)^#\d+ ", text)
        assert first is not None
        assert first.group(0) == "#697 "

    def test_log_entry_relative_order(self):
        text = _read(LOG_PATH)
        ids = re.findall(r"(?m)^#(\d+) Type [A-E]:", text)
        assert ids[0] == "697"
        assert ids[1] == "696"
        assert ids[2] == "695"

    def test_log_entry_content(self):
        text = _read(LOG_PATH)
        start = text.index("#697 Type A")
        entry = text[start:start + 9000]
        assert "mechanism 652" in entry
        assert "NOT a falsification-family member" in entry
        assert "MANUAL ILLUSTRATIVE" in entry
        assert "+0.575" in entry


class TestRotationCycleGuard697:
    """Rotation window 693-697 closes E->A. Anchor patched in followup per #565."""

    ANCHORED_SHA = "0000000000000000000000000000000000000000"

    def _window(self):
        text = _read(LOG_PATH)
        heads = re.findall(r"(?m)^#(\d+) Type ([A-E]):", text)
        return [(int(n), t) for n, t in heads]

    def test_window_693_697_closes_e_to_a(self):
        window = self._window()[:5]
        assert window == [(697, "A"), (696, "E"), (695, "D"), (694, "C"), (693, "B")], window

    def test_rotation_adjacency_cycle_valid(self):
        order = {"A": "B", "B": "C", "C": "D", "D": "E", "E": "A"}
        window = self._window()[:5]
        for (n_newer, t_newer), (n_older, t_older) in zip(window, window[1:]):
            assert order[t_older] == t_newer, (n_newer, t_newer, n_older, t_older)

    def test_anchor_is_main_commit_patched_in_followup(self):
        pytest.skip("anchor patched in followup per #565 convention")


class TestDocSync697:
    def test_readme_has_row(self):
        text = _read(os.path.join(REPO_ROOT, "README.md"))
        assert TEST_BASENAME in text

    def test_architecture_has_row(self):
        text = _read(os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md"))
        assert TEST_BASENAME in text


class TestSweepSupersession697:
    """Pins the post-#697 state; documents #695's no-652 sweep designed supersession."""

    def test_max_mechanism_id_is_652(self):
        text = _read(PROFILE_PATH)
        ids = [int(x) for x in re.findall(r"mechanism_id:\s*(\d+)\b", text)]
        modern = [i for i in ids if i >= 600]
        assert max(modern) == 652, max(modern)

    def test_exactly_one_mechanism_652_key(self):
        text = _read(PROFILE_PATH)
        keys = re.findall(r"(?m)^    mechanism_652_\w+:", text)
        assert keys == [
            "    mechanism_652_gizmodo_apple_duo_launch_register_vs_gizmodo_meta_muse_experiment_sep12:"
        ], keys

    def test_695_sweep_supersession_documented_in_novelty(self):
        assert "superseded by design" in _mechanism()["novelty"]
