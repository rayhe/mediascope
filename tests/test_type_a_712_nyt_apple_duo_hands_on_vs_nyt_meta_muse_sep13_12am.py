"""Type A #712 (2026-09-13 00:00 PDT): NYT x Apple iPhone Duo
hands-on value review vs NYT x Meta Muse capability listing
(mechanism 661).

First dedicated NYT x Apple Duo Type A mechanism; first YAML mechanism
under competitor_relationships.apple in nytimes.yaml; first NYT x Meta
Muse mechanism. Seventh publication in the Duo launch-genre series (WSJ
#662, Verge #687, Reuters #692, Gizmodo #697, Fast Company #702,
Bloomberg #707).

Apple arm (The New York Times, consumer-tech hands-on by lead consumer
technology writer Brian X. Chen, photos by Jason Henry; searched/crawled
Sep 13 2026): "Why is Apple's New Foldable iPhone Duo $1,999?" -
verbatim NYT text carried on a mirror
(https://www.armwoodtechnology.com/2026/09/why-is-apples-new-foldable-iphone-duo.html)
and corroborated by two independent syndications
(https://nypost.com/2026/09/12/lifestyle/left-handed-users-slam-apples-iphone-duo-over-awkward-design/
and
https://timesnewsnetworks.com/left-handed-apple-users-cry-discrimination-as-new-foldable-iphone-duo-designed-for-right-handers/):
'In my tests, when opened, the iPhone Duo was extremely thin, measuring
two-tenths of an inch. I liked that a Netflix video took up the full
screen instead of showing black bars on the sides, which has been the
case with other foldables.'; 'Closed up, the phone felt dainty and was
about the size of a passport. It also felt less chunky in my pocket than
other foldables I have tested, such as the $1,900 Google Pixel 11 Pro
Fold.'; 'The inner screen has a matte texture to reduce glare. Still, I
occasionally noticed the crease in the center where the screen folds. I
did not mind it, but that might bother nit-pickers.'; 'Apple also had to
leave out some components to make a phone this thin - the iPhone Duo
lacks the advanced camera system featured in the $1,199 iPhone 18 Pro
phones. It also does not have a face scanner for unlocking the device,
relying instead on a fingerprint sensor on the side of the phone.';
'The iPhone Duo appears to be addressing some of the shortcomings of
previous foldable phones.'; consumer value-review register (price
skepticism in the title + trade-off listing + mild positive hands-on);
scored +0.15.

Meta arm (The New York Times, Muse launch day Sep 8 2026; no verbatim
nytimes.com URL surfaced; nytimes.com blocked by policy in this
environment): attested by two independent secondary sources -
https://www.mitrade.com/au/insights/news/live-news/article-3-2069276-20260909
('According to the New York Times, Muse has access to services like
Gmail, Spotify, Ticketmaster, OpenTable, and Shopify.') and
https://techseen.com/story/meta-bets-on-ai-agent-muse-to-catch-up-in-ai-race-d6f6510
(story history: 'The New York Times added a related source record'
Sep 8 2026 13:05 PDT, confirming day-one launch coverage); neutral
capability listing; scored +0.05.

Scorer (MANUAL ILLUSTRATIVE, standing rule Aug 28 2026; arithmetic
only): Apple [+0.15] vs Meta [+0.05]. Delta (Apple minus Meta) +0.10 -
the smallest positive delta in the Duo launch-genre series.
p_value NOT_CALCULATED, cohens_d NOT_CALCULATED, ci NOT_CALCULATED,
is_significant False, artifact_grade False. Classic degenerate
statistical contract per the #638/#643 convention (n=1 vs n=1, t=0.0,
p=1.0, d=0.0); engine NOT run; no divergence pin.

Financial context (correlation, not causation): NYT x Apple carries NO
known AI licensing deal on record (financial_tie mixed, estimated
minimal, mutual direction: NYT left Apple News in 2020; Wirecutter and
The Athletic still appear in Apple News; Apple Podcasts subscription
partnership; no AI content deal; coverage_prediction neutral). This is a
MINIMAL-GRADIENT CONTROL: the incentive theory makes no differential
prediction, and the observed +0.10 gap is consistent with the neutral
prediction, so the pair cannot contradict the theory. NOT a
falsification-family member; the ledger stands at 22 after #708's
TWENTY-SECOND (m659). The price-first trade-off-listing register lands
well below the launch-celebration norm of tech/business press (WSJ
+0.45, Verge +0.38 avg, Gizmodo +0.325 avg, Fast Company +0.35,
Bloomberg +0.40) and beside the wire's skepticism (Reuters -0.05 avg).

Strongest counterarguments (accepted as major counterweights): (1) the
pair is second-hand bounded - nytimes.com is blocked by policy and no
verbatim nytimes.com URL surfaced in 5 browser.search query sets this
run, so both arms are read from verbatim NYT passages carried by
secondary surfaces (mirror + two independent syndications for the Duo
arm; two independent attributions for the Muse arm) per #503 and the
m471 secondary-attestation precedent; both tones are attestation-
bounded, not body-verified; (2) genre asymmetry - consumer-tech
hands-on value review (Chen) vs day-one launch business coverage (desk
unattested); (3) NYT Meta bifurcation (mechanism #69) - Muse sits in
the AI-execution domain where the Times runs adversarial, but the
attested Muse register is neutral; the +0.05 read may miss adversarial
passages beyond the attestations. Claim stays bounded, directional,
correlation-only, MANUAL ILLUSTRATIVE.

Evidence hygiene: all six attestation URLs copied verbatim from this
run's Full-URL listings; no canonical NYT URLs invented; no zero-
coverage claims; no em dashes; ASCII-only.

Designed supersession: #710's test_max_mechanism_id_is_660,
test_zero_mechanism_661_keys_in_profiles and
test_zero_mechanism_661_references_in_tests fail by design this run
(same convention as #705's 657/658, #697's 651/652, #702's 654/655,
#703's 655/656, #704's 656/657 supersessions); this file's
TestSweepSupersession712 pins the new state (max mechanism 661,
exactly one mechanism_661 key under nytimes.yaml
competitor_relationships.apple).

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
PROFILE_PATH = os.path.join(REPO_ROOT, "profiles", "nytimes.yaml")
LOG_PATH = os.path.join(REPO_ROOT, "iteration-log.md")

MECH_KEY = "mechanism_661_nyt_apple_duo_hands_on_value_review_vs_nyt_meta_muse_capability_list_sep13"

DUO_ATTEST_URL = "https://www.armwoodtechnology.com/2026/09/why-is-apples-new-foldable-iphone-duo.html"
DUO_CORROB_1 = "https://nypost.com/2026/09/12/lifestyle/left-handed-users-slam-apples-iphone-duo-over-awkward-design/"
DUO_CORROB_2 = "https://timesnewsnetworks.com/left-handed-apple-users-cry-discrimination-as-new-foldable-iphone-duo-designed-for-right-handers/"
MUSE_ATTEST_1 = "https://www.mitrade.com/au/insights/news/live-news/article-3-2069276-20260909"
MUSE_ATTEST_2 = "https://techseen.com/story/meta-bets-on-ai-agent-muse-to-catch-up-in-ai-race-d6f6510"

TARGET_SCORES = [0.15]
PEER_SCORES = [0.05]
TARGET_AVG = 0.15
PEER_AVG = 0.05
EXPECTED_DELTA = 0.1


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
    return _profile()["competitor_relationships"]["apple"]


def _mechanism():
    return _entity()[MECH_KEY]


def _read(path):
    with open(path) as f:
        return f.read()


class TestNovelty712:
    """Iteration 712 is new; nothing with this number existed pre-commit."""

    def test_single_type_a_712_file(self):
        matches = glob.glob(os.path.join(REPO_ROOT, "tests", "test_type_a_712*.py"))
        assert len(matches) == 1, "expected exactly this file, got %r" % (matches,)
        assert matches[0].endswith(TEST_BASENAME)

    def test_type_a_712_main_commit_unique_and_anchored(self):
        # Runs green only post-main-commit per the #565 followup convention.
        # Deselect pre-commit; the followup patches ANCHORED_SHA to the real
        # main-commit SHA. Novelty was verified pre-commit by shell greps
        # (zero test_type_a_712 files, no #712 in git log, zero real
        # mechanism_661 keys in profiles/ pre-commit - text refs confined to
        # #710's sweep-test assertions, max numeric mechanism 660, all six
        # attestation URLs new to corpus repo-wide).
        out = _run_git("log", "--format=%H %s")
        mains = [
            line
            for line in out.stdout.splitlines()
            if re.match(r"^[0-9a-f]{40} Type A #712:", line)
        ]
        assert len(mains) == 1, "expected exactly one Type A #712 main commit, got %r" % (mains,)
        sha = mains[0].split()[0]
        assert sha == TestRotationCycleGuard712.ANCHORED_SHA, (
            "anchor patched in followup per #565 convention"
        )


class TestMechanismExistsAndShape:
    def test_mechanism_key_present_under_apple_entity(self):
        assert MECH_KEY in _entity()

    def test_mechanism_id_is_next_free(self):
        assert _mechanism()["mechanism_id"] == 661

    def test_identity_fields(self):
        m = _mechanism()
        assert m["iteration"] == 712
        assert m["iteration_type"] == "A"
        assert m["date_analyzed"] == "2026-09-13"
        assert m["publication_focus"] == "nytimes"
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

    def test_no_em_dashes_in_block(self):
        text = _read(PROFILE_PATH)
        start = text.index(MECH_KEY)
        end = text.index("\n  google:", start)
        assert "\u2014" not in text[start:end]

    def test_test_file_field_matches_this_file(self):
        assert _mechanism()["test_file"].endswith(TEST_BASENAME)

    def test_event_frame(self):
        m = _mechanism()
        assert "iPhone Duo" in m["event"]
        assert "Muse" in m["event"]
        assert "NYT" in m["event"]


class TestAppleArm:
    def test_one_item(self):
        items = _mechanism()["apple_arm"]["items"]
        assert len(items) == 1

    def test_nyt_chen_byline_attested(self):
        item = _mechanism()["apple_arm"]["items"][0]
        assert "Brian X. Chen" in item["byline"]
        assert "Why is Apple's New Foldable iPhone Duo $1,999?" in item["title"]

    def test_attesting_urls_verbatim(self):
        item = _mechanism()["apple_arm"]["items"][0]
        assert item["attesting_url"] == DUO_ATTEST_URL
        # YAML list items carry annotation suffixes; assert URL-prefix membership.
        assert any(x.startswith(DUO_CORROB_1) for x in item["corroborating_attestations"])
        assert any(x.startswith(DUO_CORROB_2) for x in item["corroborating_attestations"])

    def test_duo_register_tone_and_quotes(self):
        item = _mechanism()["apple_arm"]["items"][0]
        assert item["register"] == "consumer_value_review"
        assert item["manual_illustrative_tone"] == 0.15
        assert "extremely thin" in item["key_framing"]
        assert "dainty" in item["key_framing"]
        assert "lacks the advanced camera system" in item["key_framing"]
        assert "nit-pickers" in item["key_framing"]

    def test_second_hand_bounded_documented(self):
        item = _mechanism()["apple_arm"]["items"][0]
        assert "blocked by policy" in item["source_note"]
        assert "No canonical NYT URL invented" in item["source_note"]

    def test_apple_arm_average(self):
        assert _mechanism()["apple_arm"]["average_manual_illustrative"] == TARGET_AVG


class TestMetaArm:
    def test_new_to_corpus_this_run(self):
        assert "no prior NYT x Meta Muse mechanism" in _mechanism()["meta_arm"]["carried_from"]

    def test_one_item(self):
        items = _mechanism()["meta_arm"]["items"]
        assert len(items) == 1

    def test_attesting_urls_verbatim(self):
        item = _mechanism()["meta_arm"]["items"][0]
        assert item["attesting_urls"] == [MUSE_ATTEST_1, MUSE_ATTEST_2]

    def test_muse_register_tone_and_quotes(self):
        item = _mechanism()["meta_arm"]["items"][0]
        assert item["register"] == "neutral_capability_listing"
        assert item["manual_illustrative_tone"] == 0.05
        assert "Gmail, Spotify, Ticketmaster, OpenTable, and Shopify" in item["key_framing"]

    def test_attestation_bounded_documented(self):
        item = _mechanism()["meta_arm"]["items"][0]
        assert "attestation-bounded" in item["source_note"]
        assert "No canonical NYT URL invented" in item["source_note"]

    def test_meta_arm_average(self):
        assert _mechanism()["meta_arm"]["average_manual_illustrative"] == PEER_AVG


class TestScorer712:
    def test_arrays(self):
        s = _mechanism()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert s["target_scores_MANUAL_ILLUSTRATIVE"] == TARGET_SCORES
        assert s["peer_scores_MANUAL_ILLUSTRATIVE"] == PEER_SCORES

    def test_arithmetic(self):
        s = _mechanism()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert s["target_avg"] == TARGET_AVG
        assert s["peer_avg"] == PEER_AVG
        assert abs(s["delta_manual_illustrative"] - EXPECTED_DELTA) < 1e-9
        assert s["delta_calc"] == "0.15 - 0.05 = 0.10"

    def test_manual_illustrative_guards(self):
        s = _mechanism()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert "DO NOT claim empirical significance" in s["methodology"]
        assert "degenerate" in s["engine_degenerate"]
        assert "Engine NOT run" in s["engine_degenerate"]

    def test_finding_layer_not_significant(self):
        finding = _mechanism()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]["finding_layer"]
        assert "NOT_CALCULATED" in finding
        assert "is_significant False" in finding

    def test_no_divergence_pin(self):
        s = _mechanism()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert "no divergence pin" in s["engine_degenerate"]

    def test_artifact_grade_false(self):
        assert _mechanism()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]["artifact_grade"] is False


class TestFalsificationFamily712:
    def test_not_a_member_minimal_gradient_control(self):
        fam = _mechanism()["falsification_family"]["membership"]
        assert "NOT a falsification-family member" in fam
        assert "minimal-gradient control" in fam

    def test_prediction_silent(self):
        assert "no differential prediction" in _mechanism()["falsification_family"]["prediction"]

    def test_observed_gap_not_contradiction(self):
        fam = _mechanism()["falsification_family"]["observed"]
        assert "+0.10" in fam
        assert "consistent with the neutral prediction" in fam

    def test_no_within_arm_range(self):
        assert "n=1 vs n=1" in _mechanism()["falsification_family"]["within_arm_range_vs_gap"]

    def test_publication_genre_boundary_seventh(self):
        boundary = _mechanism()["falsification_family"]["publication_genre_boundary"]
        assert "seventh publication" in boundary
        for tag in ["#662", "#687", "#692", "#697", "#702", "#707"]:
            assert tag in boundary, tag

    def test_financial_context_minimal_tie(self):
        fc = _mechanism()["financial_context"]
        assert fc["predictor"] == "minimal_gradient_control"
        assert "left Apple News in 2020" in fc["chain"]
        assert "NO AI content deal on record" in fc["chain"]


class TestConfoundersAndCrossRefs:
    def test_confounders_present(self):
        c = _mechanism()["confounders_ranked"]
        assert len(c["strong"]) == 3
        assert len(c["moderate"]) == 3
        assert len(c["weak"]) == 2

    def test_strongest_counterarguments_accepted(self):
        strong = " ".join(_mechanism()["confounders_ranked"]["strong"])
        assert "Second-hand bounded" in strong
        assert "Genre asymmetry" in strong
        assert "mechanism #69" in strong

    def test_counterevidence_present(self):
        ce = " ".join(_mechanism()["counterevidence"])
        assert "Reuters #692" in ce
        assert "m567" in ce
        assert "Nicole Nguyen" in ce

    def test_cross_references(self):
        refs = " ".join(_mechanism()["cross_references"])
        for tag in ["#662", "#687", "#692", "#697", "#702", "#707", "#708", "#69", "#567", "#471", "#638/#643", "iteration-492", "#503", "#710 convention", "#565 convention"]:
            assert tag in refs, tag

    def test_novelty_documents_supersession(self):
        nov = _mechanism()["novelty"]
        assert "First dedicated NYT x Apple Duo Type A mechanism" in nov
        assert "mechanism 661" in nov
        assert "designed supersession" in nov
        assert "no journalist career mechanism added" in nov

    def test_research_method_documents_second_hand_bounded(self):
        rm = _mechanism()["research_method"]
        assert "5 browser.search query sets" in rm
        assert "no zero-coverage claims" in rm
        assert "ASCII-only" in rm


class TestIterationLog712:
    def test_log_starts_with_712(self):
        text = _read(LOG_PATH)
        first = re.search(r"(?m)^#\d+ ", text)
        assert first is not None
        assert first.group(0) == "#712 "

    def test_log_entry_relative_order(self):
        text = _read(LOG_PATH)
        ids = re.findall(r"(?m)^#(\d+) Type [A-E]:", text)
        assert ids[0] == "712"
        assert ids[1] == "711"
        assert ids[2] == "710"

    def test_log_entry_content(self):
        text = _read(LOG_PATH)
        start = text.index("#712 Type A")
        entry = text[start:start + 9000]
        assert "mechanism 661" in entry
        assert "NOT a falsification-family member" in entry
        assert "MANUAL ILLUSTRATIVE" in entry
        assert "+0.10" in entry
        assert "NYT" in entry


class TestRotationCycleGuard712:
    """Rotation window 708-712 closes E->A. Anchor patched in followup per #565."""

    ANCHORED_SHA = "PENDING_FOLLOWUP_PATCH"

    def _window(self):
        text = _read(LOG_PATH)
        heads = re.findall(r"(?m)^#(\d+) Type ([A-E]):", text)
        return [(int(n), t) for n, t in heads]

    def test_window_708_712_closes_e_to_a(self):
        window = self._window()[:5]
        assert window == [(712, "A"), (711, "E"), (710, "D"), (709, "C"), (708, "B")], window

    def test_rotation_adjacency_cycle_valid(self):
        order = {"A": "B", "B": "C", "C": "D", "D": "E", "E": "A"}
        window = self._window()[:5]
        for (n_newer, t_newer), (n_older, t_older) in zip(window, window[1:]):
            assert order[t_older] == t_newer, (n_newer, t_newer, n_older, t_older)

    def test_anchor_is_main_commit_patched_in_followup(self):
        pytest.skip("anchor patched in followup per #565 convention")


class TestDocSync712:
    def test_readme_has_row(self):
        text = _read(os.path.join(REPO_ROOT, "README.md"))
        assert TEST_BASENAME in text

    def test_architecture_has_row(self):
        text = _read(os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md"))
        assert TEST_BASENAME in text


class TestSweepSupersession712:
    """Pins the post-#712 state; documents #710's no-661 sweep designed supersession."""

    def test_max_mechanism_id_is_661(self):
        text = _read(PROFILE_PATH)
        ids = [int(x) for x in re.findall(r"mechanism_id:\s*(\d+)\b", text)]
        modern = [i for i in ids if i >= 600]
        assert max(modern) == 661, max(modern)

    def test_exactly_one_mechanism_661_key_under_apple(self):
        text = _read(PROFILE_PATH)
        keys = re.findall(r"(?m)^    mechanism_661_\w+:", text)
        assert keys == [
            "    mechanism_661_nyt_apple_duo_hands_on_value_review_vs_nyt_meta_muse_capability_list_sep13:"
        ], keys

    def test_661_key_is_first_apple_mechanism(self):
        ent = _entity()
        mech_keys = [k for k in ent.keys() if k.startswith("mechanism_")]
        assert mech_keys == [MECH_KEY], mech_keys
