"""Type A #702 (2026-09-12 12:00 PDT): Fast Company x Apple iPhone Duo
launch register vs Fast Company x Meta Muse register (mechanism 655).

First dedicated Fast Company x Apple Duo Type A mechanism; first Fast
Company x Meta Muse mechanism (prior FC x Meta mechanisms 103/121 use
glasses pegs). Fifth publication in the Duo launch-genre series (WSJ
#662, Verge #687, Reuters #692, Gizmodo #697).

Apple arm (Fast Company, Sep 9, read first-hand this run, 48 rendered
lines): "Apple's new iPhone Duo changes the dock UI for the first time
ever" by Hunter Schwarz (FC contributor, design/advertising beat)
(https://www.fastcompany.com/91604701/apples-iphone-duo-has-a-new-intuitive-vertical-interface):
'Not only is Apple going foldable with its new iPhone Duo, its user
interface is going vertical too'; 'turning parts of the iPhone's
longtime UI on its head'; the horizontal home-screen dock 'has now been
moved to the side'; 'it puts major controls closer to the user's thumb,
helpful for a phone that folds out longer than it is tall'; 'the first
iPhone to support the Apple Pencil'; 'Despite the changes, Apple said
it designed the new system to feel natural and familiar... it's meant
to be intuitive for longtime iPhone users'; zero caveats in the piece;
scored +0.35.

Meta arm (Fast Company, Sep 9, read first-hand this run, 57 rendered
lines): "Meta wants its new Muse AI agent to run your digital life"
(https://www.fastcompany.com/91603856/meta-wants-its-new-ai-agent-to-run-your-digital-life):
dedicated 'Security and trust' section: 'The biggest barrier to users
handing over their personal affairs to a Meta AI agent may be trust.
Meta's core advertising business is built on harvesting the personal
data of its social app users, and the company has shown a disregard for
the mental health of young users'; 'The more agency and autonomy an AI
possesses, the greater the potential for privacy or security breaches';
Miranda Bogen (CDT): agents could 'damage someone's reputation, leak
sensitive medical information, or even deplete bank accounts'; 'Meta
has spent copious amounts of money on the AI research talent and
computing power'; capability admitted: dedicated Muse Secure VM with own
browser, Sentinel agent privacy thresholds, user-held decryption key,
audit trail, opt-out of ad systems and training, Link wallet
one-time-use cards. Scored -0.30.

Scorer (MANUAL ILLUSTRATIVE, standing rule Aug 28 2026; arithmetic
only): Apple [+0.35] vs Meta [-0.30]. Delta (Apple minus Meta) +0.65.
p_value NOT_CALCULATED, cohens_d NOT_CALCULATED, ci NOT_CALCULATED,
is_significant False, artifact_grade False. Classic degenerate
statistical contract per the #638/#643 convention (n=1 vs n=1, t=0.0,
p=1.0, d=0.0); engine NOT run; no divergence pin.

Financial context (correlation, not causation): Fast Company (Mansueto
Ventures) carries NO known AI licensing deal with Apple or Meta
(bounded absence this run; Mansueto's RSL 1.0 endorsement is an
open-standards endorsement, not a paid deal; mechanism #121's prior
record confirms no FC AI licensing deals). This is a ZERO-GRADIENT
CONTROL: the incentive theory makes no differential prediction, so the
observed +0.65 gap cannot contradict it. NOT a falsification-family
member; the ledger stands at 20 after #698's TWENTIETH.

Publication-genre boundary: fifth publication in the Duo launch-genre
series - WSJ celebrated (+0.45, #662/m631), The Verge celebrated (+0.38
avg, #687/m646), Reuters ran skeptical (-0.05 avg, #692/m649), Gizmodo
celebrated (+0.325 avg, #697/m652), Fast Company celebrated (+0.35).
The launch-celebration register holds at tech/business press and breaks
at the wire.

Strongest counterarguments (accepted as major counterweights): (1) the
desk/register mismatch dominates the gap - the Apple arm is a
design-desk product piece by a design/advertising-beat contributor while
the Meta arm is a tech-policy launch piece with a dedicated 'Security
and trust' section; comparing a design register to a trust register
compares desks, not entity preference; the #627 verbatim-URL discipline
does not fix desk asymmetry; (2) news-peg valence skew - the Muse piece
is anchored on trust and Meta's ad-business surveillance economics while
the Duo piece is anchored on UI design delight at a launch event; (3)
author-level variance is unruled-out - the Duo byline (Hunter Schwarz,
design/advertising beat) is attested while the Muse byline was
unattested in the opened rendered text. n=1 vs n=1: no within-arm range
exists, so the desk-mismatch confound carries the explanatory load.
Claim stays bounded, directional, correlation-only, MANUAL ILLUSTRATIVE.

Evidence hygiene: FT, Guardian, WIRED, and Bloomberg queries did not
surface usable verbatim same-publication Apple Duo and Meta Muse URLs
(bounded search-result absence per iteration-492, not noncoverage); the
Times surfaced a Duo URL but no Times Muse piece; the run pivoted to
Fast Company where verbatim URLs for both pegs surfaced in this run's
Full-URL listings and both pieces were read first-hand; no canonical
URLs invented; no zero-coverage claims; no em dashes; ASCII-only.

Designed supersession: #700's test_max_modern_mechanism_id_is_654,
test_no_mechanism_655_in_profiles, test_no_mechanism_655_key_in_profiles,
and test_no_mechanism_655_in_tests fail by design this run (same
convention as #650's 624/625, #695's 649, and #697's 652 supersession);
this file's TestSweepSupersession702 pins the new state (max mechanism
655, exactly one mechanism_655 key).

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

MECH_KEY = "mechanism_655_fastcompany_apple_duo_launch_register_vs_fastcompany_meta_muse_register_sep12"

DUO_URL = "https://www.fastcompany.com/91604701/apples-iphone-duo-has-a-new-intuitive-vertical-interface"
MUSE_URL = "https://www.fastcompany.com/91603856/meta-wants-its-new-ai-agent-to-run-your-digital-life"

TARGET_SCORES = [0.35]
PEER_SCORES = [-0.3]
TARGET_AVG = 0.35
PEER_AVG = -0.3
EXPECTED_DELTA = 0.65


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


class TestNovelty702:
    """Iteration 702 is new; nothing with this number existed pre-commit."""

    def test_single_type_a_702_file(self):
        matches = glob.glob(os.path.join(REPO_ROOT, "tests", "test_type_a_702*.py"))
        assert len(matches) == 1, "expected exactly this file, got %r" % (matches,)
        assert matches[0].endswith(TEST_BASENAME)

    def test_type_a_702_main_commit_unique_and_anchored(self):
        # Runs green only post-main-commit per the #565 followup convention.
        # Deselect pre-commit; the followup patches ANCHORED_SHA to the real
        # main-commit SHA. Novelty was verified pre-commit by shell greps
        # (zero test_type_a_702 files, no #702 in git log, zero
        # mechanism_655 keys in profiles/ pre-commit, max mechanism 654,
        # both Fast Company URLs new to corpus repo-wide).
        out = _run_git("log", "--format=%H %s")
        mains = [
            line
            for line in out.stdout.splitlines()
            if re.match(r"^[0-9a-f]{40} Type A #702:", line)
        ]
        assert len(mains) == 1, "expected exactly one Type A #702 main commit, got %r" % (mains,)
        sha = mains[0].split()[0]
        assert sha == TestRotationCycleGuard702.ANCHORED_SHA, (
            "anchor patched in followup per #565 convention"
        )


class TestMechanismExistsAndShape:
    def test_mechanism_key_present_under_apple_entity(self):
        assert MECH_KEY in _entity()

    def test_mechanism_id_is_next_free(self):
        assert _mechanism()["mechanism_id"] == 655

    def test_identity_fields(self):
        m = _mechanism()
        assert m["iteration"] == 702
        assert m["iteration_type"] == "A"
        assert m["date_analyzed"] == "2026-09-12"
        assert m["publication_focus"] == "fastcompany"
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

    def test_one_item(self):
        assert len(self._items()) == 1

    def test_duo_url_verbatim(self):
        assert self._items()[0]["url"] == DUO_URL

    def test_duo_register_tone_and_quotes(self):
        item = self._items()[0]
        assert item["register"] == "product_design_forward"
        assert item["manual_illustrative_tone"] == 0.35
        assert "going vertical too" in item["key_framing"]
        assert "moved to the side" in item["key_framing"]
        assert "intuitive for longtime iPhone users" in item["key_framing"]
        assert "first iPhone to support the Apple Pencil" in item["key_framing"]
        assert "first-hand" in item["source_note"]
        assert "48 rendered lines" in item["source_note"]

    def test_duo_byline_hunter_schwarz(self):
        item = self._items()[0]
        assert "Hunter Schwarz" in item["byline"]
        assert "design/advertising beat" in item["byline"]

    def test_apple_arm_average(self):
        assert _mechanism()["apple_arm"]["average_manual_illustrative"] == TARGET_AVG


class TestMetaArm:
    def _items(self):
        return _mechanism()["meta_arm"]["items"]

    def test_new_to_corpus_this_run(self):
        assert "new to corpus this run" in _mechanism()["meta_arm"]["carried_from"]

    def test_one_item(self):
        assert len(self._items()) == 1

    def test_muse_url_verbatim(self):
        assert self._items()[0]["url"] == MUSE_URL

    def test_muse_register_tone_and_quotes(self):
        item = self._items()[0]
        assert item["register"] == "security_anchored_launch_coverage"
        assert item["manual_illustrative_tone"] == -0.3
        assert "biggest barrier" in item["key_framing"]
        assert "harvesting the personal data" in item["key_framing"]
        assert "disregard for the mental health of young users" in item["key_framing"]
        assert "Sentinel agent" in item["key_framing"]
        assert "57 rendered lines" in item["source_note"]

    def test_meta_arm_average(self):
        assert _mechanism()["meta_arm"]["average_manual_illustrative"] == PEER_AVG


class TestScorer702:
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
        assert s["delta_calc"] == "0.35 - (-0.3) = 0.65"

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


class TestFalsificationFamily702:
    def _f(self):
        return _mechanism()["falsification_family"]

    def test_not_a_member_zero_gradient_control(self):
        assert "NOT a falsification-family member" in self._f()["membership"]
        assert "zero-gradient control" in self._f()["membership"]
        assert "Ledger stands at 20" in self._f()["membership"]

    def test_prediction_silent(self):
        assert "no differential prediction" in self._f()["prediction"]
        assert "no known paid AI content licensing deal" in self._f()["prediction"]

    def test_observed_gap_not_contradiction(self):
        assert "+0.65" in self._f()["observed"]
        assert "not a theory contradiction" in self._f()["observed"]

    def test_no_within_arm_range(self):
        assert "no within-arm range exists" in self._f()["within_arm_range_vs_gap"]

    def test_publication_genre_boundary_fifth(self):
        b = self._f()["publication_genre_boundary"]
        assert "fifth publication" in b
        assert "#662" in b and "#687" in b and "#692" in b and "#697" in b

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
        assert "compares desks, not entity preference" in strong
        assert "track their news pegs" in strong
        assert "unruled-out" in strong

    def test_counterevidence_present(self):
        ce = _mechanism()["counterevidence"]
        assert len(ce) == 4
        assert any("#121" in x for x in ce)
        assert any("#692" in x for x in ce)

    def test_cross_references(self):
        cr = _mechanism()["cross_references"]
        text = " ".join(cr)
        for ref in ["#662", "#687", "#692", "#697", "#121", "#587", "#627", "#638", "#700", "#565"]:
            assert ref in text, "missing cross-reference %s" % ref

    def test_novelty_documents_supersession(self):
        n = _mechanism()["novelty"]
        assert "First dedicated Fast Company x Apple Duo Type A mechanism" in n
        assert "designed supersession" in n
        assert "mechanism 655" in n

    def test_research_method_documents_ft_pivot(self):
        rm = _mechanism()["research_method"]
        assert "Financial Times" in rm
        assert "Fast Company" in rm
        assert "iteration-492 rule" in rm
        assert "first-hand browser.opens" in rm


class TestIterationLog702:
    def test_log_starts_with_702(self):
        text = _read(LOG_PATH)
        first = re.search(r"(?m)^#\d+ ", text)
        assert first is not None
        assert first.group(0) == "#702 "

    def test_log_entry_relative_order(self):
        text = _read(LOG_PATH)
        ids = re.findall(r"(?m)^#(\d+) Type [A-E]:", text)
        assert ids[0] == "702"
        assert ids[1] == "701"
        assert ids[2] == "700"

    def test_log_entry_content(self):
        text = _read(LOG_PATH)
        start = text.index("#702 Type A")
        entry = text[start:start + 9000]
        assert "mechanism 655" in entry
        assert "NOT a falsification-family member" in entry
        assert "MANUAL ILLUSTRATIVE" in entry
        assert "+0.65" in entry


class TestRotationCycleGuard702:
    """Rotation window 698-702 closes E->A. Anchor patched in followup per #565."""

    ANCHORED_SHA = "3a19675a15ce9168aeeac7f3f620e0ec2495f5d8"

    def _window(self):
        text = _read(LOG_PATH)
        heads = re.findall(r"(?m)^#(\d+) Type ([A-E]):", text)
        return [(int(n), t) for n, t in heads]

    def test_window_698_702_closes_e_to_a(self):
        window = self._window()[:5]
        assert window == [(702, "A"), (701, "E"), (700, "D"), (699, "C"), (698, "B")], window

    def test_rotation_adjacency_cycle_valid(self):
        order = {"A": "B", "B": "C", "C": "D", "D": "E", "E": "A"}
        window = self._window()[:5]
        for (n_newer, t_newer), (n_older, t_older) in zip(window, window[1:]):
            assert order[t_older] == t_newer, (n_newer, t_newer, n_older, t_older)

    def test_anchor_is_main_commit_patched_in_followup(self):
        pytest.skip("anchor patched in followup per #565 convention")


class TestDocSync702:
    def test_readme_has_row(self):
        text = _read(os.path.join(REPO_ROOT, "README.md"))
        assert TEST_BASENAME in text

    def test_architecture_has_row(self):
        text = _read(os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md"))
        assert TEST_BASENAME in text


class TestSweepSupersession702:
    """Pins the post-#702 state; documents #700's no-655 sweep designed supersession."""

    def test_max_mechanism_id_is_655(self):
        text = _read(PROFILE_PATH)
        ids = [int(x) for x in re.findall(r"mechanism_id:\s*(\d+)\b", text)]
        modern = [i for i in ids if i >= 600]
        assert max(modern) == 655, max(modern)

    def test_exactly_one_mechanism_655_key(self):
        text = _read(PROFILE_PATH)
        keys = re.findall(r"(?m)^    mechanism_655_\w+:", text)
        assert keys == [
            "    mechanism_655_fastcompany_apple_duo_launch_register_vs_fastcompany_meta_muse_register_sep12:"
        ], keys
