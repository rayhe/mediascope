"""Type A #692 (2026-09-12 02:00 PDT): Reuters x Apple iPhone Duo launch
register vs Reuters x Meta Muse launch register (mechanism 649).

First dedicated Reuters x Apple Type A mechanism: same-week launch pair
at the Reuters wire - Apple iPhone Duo foldable launch (Sep 9 2026) vs
Meta Muse AI-agent launch (Sep 8 2026).

Apple arm (Reuters): (1) Sep 9 Duo launch news item, verbatim URL slug
dated 2026-09-09 ("Apple debuts $1,999 passport-shaped foldable phone,
called Duo"): biggest design change in years, first launch under new CEO
John Ternus, Pescatore "new premium growth opportunity" quote;
excerpt-bounded from verbatim search-result excerpts, scored +0.15.
(2) Sep 10 skeptical next-day follow-up ("Apple's foldable iPhone poses
a $1,999 question: Who is it for?"), opened first-hand this run (61
rendered lines): "left questioning its appeal beyond wealthy tech
enthusiasts", Milanesi "they really shied away from it", Shah "a little
bit of a lapse in positioning", IDC foldables under 3% of the 2026
market, Vision Pro "stumbled out of the gate in 2023" analogy; scored
-0.25. Apple arm average -0.05.

Meta arm (Reuters, Sep 8): Katie Paul's Muse-launch piece, carried
verbatim from #667/m634 (itself from #664/m633): "despite internal
concerns that the technology mismanages its access to sensitive personal
data", "RAISING THE STAKES FOR SAFETY" header; scored -0.45.

Scorer (MANUAL ILLUSTRATIVE, standing rule Aug 28 2026; arithmetic
only): Apple [0.15, -0.25] avg -0.05 vs Meta [-0.45] avg -0.45. Delta
(Apple minus Meta) +0.40. p_value NOT_CALCULATED, cohens_d
NOT_CALCULATED, ci NOT_CALCULATED, is_significant False, artifact_grade
False. Degenerate statistical contract per the #638/#643 convention
(n=2 vs n=1); engine NOT run; no divergence pin.

Financial context (correlation, not causation): Reuters is PAID BY Meta
under the Oct 25 2024 multiyear AI news licensing deal (mechanism 633,
ACTIVE per #599/#609); no Reuters x Apple AI licensing deal on record
(bounded absence, iteration-492). The incentive theory predicts SOFTER
coverage of the payer than the non-payer; the observed direction is
opposite: the payer's launch piece (-0.45) is the hardest register in
the pair. EIGHTEENTH falsification-family member (ledger stood at 17
after #689's SEVENTEENTH).

Publication-genre boundary: third publication in the Duo launch-genre
series - WSJ celebrated (+0.45, #662/m631), The Verge celebrated (+0.38
avg, #687/m646), Reuters ran a skeptical next-day follow-up (-0.25).
The launch-celebration register is publication-bounded, not universal:
the wire's house skepticism overrides it, on both entities.

Strongest counterarguments (accepted as major counterweights): (1) the
within-Apple-arm register range (0.40) EQUALS the between-entity gap
(0.40) - Reuters' own Apple coverage spans the full gap internally, so
entity favoritism is not needed to explain the delta (the #637
structure); (2) news-peg valence skew - the Muse hardness is
source-driven accountability (Shah's on-record safety admission) while
the Duo skepticism is analyst-driven positioning critique; (3) the
Thomson Reuters Trust Principles independence mandate - the skeptical
register lands on both entities, which is the wire's house style.
Claim stays bounded, directional, correlation-only, MANUAL ILLUSTRATIVE.

Evidence hygiene: the NYT x Apple candidate was rejected on the #627
verbatim-URL discipline (NYT queries surfaced Reuters wire pieces and no
usable NYT verbatim URLs); both Duo URLs copied verbatim from this run's
Full-URL listings (the launch URL in corpus only via #662's news-corp
entries as WSJ-run cross-publication context; first Reuters-Duo Type A
arms); Muse arm carried verbatim from #667/m634; no canonical URLs
invented; no zero-coverage claims per iteration-492; no em dashes;
ASCII-only.

Designed supersession: #690's test_max_modern_mechanism_id_is_648,
test_no_mechanism_649_in_profiles, test_no_mechanism_649_key_in_profiles,
and test_no_mechanism_649_in_tests fail by design this run (same
convention as #650's 624/625 supersession);
this file's TestSweepSupersession692 pins the new state (max mechanism
649, exactly one mechanism_649).

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

MECH_KEY = "mechanism_649_reuters_apple_duo_launch_register_vs_reuters_meta_muse_register_sep12"

DUO_LAUNCH_URL = (
    "https://www.reuters.com/business/retail-consumer/"
    "apple-expected-unveil-first-folding-phone-with-new-ceo-ternus-"
    "command-2026-09-09/"
)
DUO_FOLLOWUP_URL = (
    "https://www.reuters.com/business/retail-consumer/"
    "apples-foldable-iphone-poses-1999-question-who-is-it-2026-09-10/"
)
REUTERS_MUSE_URL = (
    "https://www.reuters.com/business/"
    "meta-launches-ai-agent-that-can-access-other-apps-send-emails-"
    "make-payments-2026-09-08/"
)

TARGET_SCORES = [0.15, -0.25]
PEER_SCORES = [-0.45]
TARGET_AVG = -0.05
PEER_AVG = -0.45
EXPECTED_DELTA = 0.4


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


class TestNovelty692:
    """Iteration 692 is new; nothing with this number existed pre-commit."""

    def test_single_type_a_692_file(self):
        matches = glob.glob(os.path.join(REPO_ROOT, "tests", "test_type_a_692*.py"))
        assert len(matches) == 1, "expected exactly this file, got %r" % (matches,)
        assert matches[0].endswith(TEST_BASENAME)

    def test_type_a_692_main_commit_unique_and_anchored(self):
        # Runs green only post-main-commit per the #565 followup convention.
        # Deselect pre-commit; the followup patches ANCHORED_SHA to the real
        # main-commit SHA. Novelty was verified pre-commit by shell greps
        # (zero test_type_a_692 files, no #692 in git log, zero
        # mechanism_649 keys in profiles/, no dedicated Reuters x Apple
        # Type A; Duo URLs in corpus only via #662 news-corp entries).
        out = _run_git("log", "--format=%H %s")
        mains = [
            line
            for line in out.stdout.splitlines()
            if re.match(r"^[0-9a-f]{40} Type A #692:", line)
        ]
        assert len(mains) == 1, "expected exactly one Type A #692 main commit, got %r" % (mains,)
        sha = mains[0].split()[0]
        assert sha == TestRotationCycleGuard692.ANCHORED_SHA, (
            "anchor patched in followup per #565 convention"
        )


class TestMechanismExistsAndShape:
    def test_mechanism_key_present_under_apple_entity(self):
        assert MECH_KEY in _entity()

    def test_mechanism_id_is_next_free(self):
        assert _mechanism()["mechanism_id"] == 649

    def test_identity_fields(self):
        m = _mechanism()
        assert m["iteration"] == 692
        assert m["iteration_type"] == "A"
        assert m["date_analyzed"] == "2026-09-12"
        assert m["publication_focus"] == "reuters"
        assert m["competitor"] == "apple"

    def test_author_kit_with_ray(self):
        assert _mechanism()["author"] == "Kit (with Ray)"

    def test_no_em_dashes_in_block(self):
        text = _read(PROFILE_PATH)
        start = text.index(MECH_KEY)
        end = text.index("\n  google:", start)
        assert " " not in text[start:end]

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
        assert item["manual_illustrative_tone"] == 0.15
        assert "Ternus" in item["key_framing"]
        assert "new premium growth opportunity" in item["key_framing"]
        assert "excerpt-bounded" in item["source_note"]

    def test_followup_url_verbatim(self):
        assert self._items()[1]["url"] == DUO_FOLLOWUP_URL

    def test_followup_byline_unattested(self):
        assert "unattested" in self._items()[1]["byline"]

    def test_followup_register_tone_and_quotes(self):
        item = self._items()[1]
        assert item["register"] == "skeptical_launch_followup"
        assert item["manual_illustrative_tone"] == -0.25
        assert "wealthy tech enthusiasts" in item["key_framing"]
        assert "lapse in positioning" in item["key_framing"]
        assert "stumbled out of the gate in 2023" in item["key_framing"]
        assert "first-hand" in item["source_note"]

    def test_apple_arm_average(self):
        assert _mechanism()["apple_arm"]["average_manual_illustrative"] == TARGET_AVG


class TestMetaArm:
    def _items(self):
        return _mechanism()["meta_arm"]["items"]

    def test_carried_from_634(self):
        assert "#667/m634" in _mechanism()["meta_arm"]["carried_from"]

    def test_muse_url_verbatim(self):
        assert self._items()[0]["url"] == REUTERS_MUSE_URL

    def test_muse_register_tone_and_quotes(self):
        item = self._items()[0]
        assert item["byline"] == "Katie Paul"
        assert item["register"] == "accountability_launch"
        assert item["manual_illustrative_tone"] == -0.45
        assert "despite internal concerns" in item["key_framing"]
        assert "RAISING THE STAKES FOR SAFETY" in item["key_framing"]

    def test_meta_arm_average(self):
        assert _mechanism()["meta_arm"]["average_manual_illustrative"] == PEER_AVG


class TestScorer692:
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
        assert s["delta_calc"] == "-0.05 - (-0.45) = 0.40"

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


class TestFalsificationFamily692:
    def _f(self):
        return _mechanism()["falsification_family"]

    def test_membership_eighteenth(self):
        assert "EIGHTEENTH falsification-family member" in self._f()["membership"]
        assert "ledger stood at 17" in self._f()["membership"]

    def test_prediction_is_softer_payer(self):
        assert "SOFTER coverage of the payer" in self._f()["prediction"]

    def test_observed_opposite(self):
        assert "opposite" in self._f()["observed"]
        assert "+0.40" in self._f()["observed"]

    def test_within_arm_range_equals_gap(self):
        assert "EQUALS the between-entity gap" in self._f()["within_arm_range_equals_gap"]

    def test_publication_genre_boundary_third(self):
        b = self._f()["publication_genre_boundary"]
        assert "third publication" in b
        assert "#662" in b and "#687" in b

    def test_financial_context_contradicted(self):
        fc = _mechanism()["financial_context"]
        assert fc["predictor"] == "payer_leg_incentive"
        assert "contradicted" in fc["status"]
        assert "EIGHTEENTH" in fc["status"]


class TestConfoundersAndCrossRefs:
    def test_confounders_present(self):
        c = _mechanism()["confounders_ranked"]
        assert len(c["strong"]) == 3
        assert len(c["moderate"]) == 4
        assert len(c["weak"]) == 2

    def test_strongest_counterarguments_accepted(self):
        strong = " ".join(_mechanism()["confounders_ranked"]["strong"])
        assert "is not required" in strong
        assert "source-driven accountability" in strong
        assert "Trust Principles" in strong

    def test_counterevidence_present(self):
        ce = _mechanism()["counterevidence"]
        assert len(ce) == 4
        assert any("#662" in x and "#687" in x for x in ce)

    def test_cross_references(self):
        cr = _mechanism()["cross_references"]
        text = " ".join(cr)
        for ref in ["#667", "#664", "#662", "#687", "#637", "#689", "#638", "#650"]:
            assert ref in text, "missing cross-reference %s" % ref

    def test_novelty_documents_supersession(self):
        n = _mechanism()["novelty"]
        assert "First dedicated Reuters x Apple Type A mechanism" in n
        assert "designed supersession" in n

    def test_research_method_documents_nyt_pivot(self):
        rm = _mechanism()["research_method"]
        assert "NYT x Apple candidate was rejected" in rm
        assert "#627 verbatim-URL discipline" in rm


class TestIterationLog692:
    def test_log_starts_with_692(self):
        text = _read(LOG_PATH)
        first = re.search(r"(?m)^#\d+ ", text)
        assert first is not None
        assert first.group(0) == "#692 "

    def test_log_entry_relative_order(self):
        text = _read(LOG_PATH)
        ids = re.findall(r"(?m)^#(\d+) Type [A-E]:", text)
        assert ids[0] == "692"
        assert ids[1] == "691"
        assert ids[2] == "690"

    def test_log_entry_content(self):
        text = _read(LOG_PATH)
        start = text.index("#692 Type A")
        entry = text[start:start + 8000]
        assert "mechanism 649" in entry
        assert "EIGHTEENTH" in entry
        assert "MANUAL ILLUSTRATIVE" in entry
        assert "+0.40" in entry


class TestRotationCycleGuard692:
    """Rotation window 688-692 closes E->A. Anchor patched in followup per #565."""

    ANCHORED_SHA = "3843b2719d5e76c14ee5941ef6d09d5c2a800f20"

    def _window(self):
        text = _read(LOG_PATH)
        heads = re.findall(r"(?m)^#(\d+) Type ([A-E]):", text)
        return [(int(n), t) for n, t in heads]

    def test_window_688_692_closes_e_to_a(self):
        window = self._window()[:5]
        assert window == [(692, "A"), (691, "E"), (690, "D"), (689, "C"), (688, "B")], window

    def test_rotation_adjacency_cycle_valid(self):
        order = {"A": "B", "B": "C", "C": "D", "D": "E", "E": "A"}
        window = self._window()[:5]
        for (n_newer, t_newer), (n_older, t_older) in zip(window, window[1:]):
            assert order[t_older] == t_newer, (n_newer, t_newer, n_older, t_older)

    def test_anchor_is_main_commit_patched_in_followup(self):
        pytest.skip("anchor patched in followup per #565 convention")


class TestDocSync692:
    def test_readme_has_row(self):
        text = _read(os.path.join(REPO_ROOT, "README.md"))
        assert TEST_BASENAME in text

    def test_architecture_has_row(self):
        text = _read(os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md"))
        assert TEST_BASENAME in text


class TestSweepSupersession692:
    """Pins the post-#692 state; documents #690's no-649 sweep designed supersession."""

    def test_max_mechanism_id_is_649(self):
        text = _read(PROFILE_PATH)
        ids = [int(x) for x in re.findall(r"mechanism_id:\s*(\d+)\b", text)]
        modern = [i for i in ids if i >= 600]
        assert max(modern) == 649, max(modern)

    def test_exactly_one_mechanism_649_key(self):
        text = _read(PROFILE_PATH)
        keys = re.findall(r"(?m)^    mechanism_649_\w+:", text)
        assert keys == [
            "    mechanism_649_reuters_apple_duo_launch_register_vs_reuters_meta_muse_register_sep12:"
        ], keys

    def test_690_sweep_supersession_documented_in_novelty(self):
        assert "superseded by design" in _mechanism()["novelty"]
