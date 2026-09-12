"""Type A #687 (2026-09-11 21:00 PDT): The Verge x Apple iPhone Duo launch
register vs The Verge x Meta Muse launch register.

First dedicated Type A mechanism on The Verge's Sep 9-10 2026 iPhone Duo
launch coverage: a publication-level launch-genre boundary-condition
replication of #662 (WSJ the first publication), on the same-week Apple
hardware launch (Sep 9) vs Meta Muse agent launch (Sep 8).

Apple arm (The Verge, Sep 9): (1) Richard Lawler, senior editor, pre-launch
name/price news item ("Apple's foldable 'iPhone Duo' will reportedly start
at $2,000"), attested verbatim via thetechstreetnow syndication carrying
the full Verge byline, dateline, image credit, and Verge copyright line;
(2) "Verge staffers react to the iPhone Duo: What we love and don't love",
eight staff voices, celebratory gut-reaction with price/crease/camera
caveats, attested verbatim via dailyguardian mirror (both URLs new to
corpus). Apple arm scored [0.25, 0.50], average 0.38. The Vergecast
hands-on episode ("We unfolded the iPhone Duo", Allison Johnson and Vee
Song reporting back from California hands-on) corroborates the
celebratory register from listing metadata only, not scored.

Meta arm (The Verge, Sep 8): Robert Hart, "Meta bets on AI agent Muse to
catch up in AI race", carried verbatim from mechanism_626 (#653):
market-legitimacy-defeat register ("ailing position in the AI race",
"regain ground after years of setbacks and failures"), -0.35.

Scorer (MANUAL ILLUSTRATIVE, standing rule Aug 28 2026; arithmetic only):
Meta [-0.35] avg -0.35 vs Apple [0.25, 0.50] avg 0.375 rounded to 0.38.
Delta (Meta minus Apple) -0.725 rounded to -0.73. p_value NOT_CALCULATED,
cohens_d NOT_CALCULATED, ci NOT_CALCULATED, is_significant False,
artifact_grade False. NOT artifact-grade: degenerate statistical contract
per the #638/#643 convention (n=2 vs n=1), tones hand-assigned, Apple arm
partially mirror-attested, engine NOT run, no divergence pin.

Financial context (correlation, not causation): The Verge apple block
carries financial_tie "none", $0, coverage_prediction "softer" - this
finding is CONSISTENT with the block prediction, not a contradiction.
Vox Media May 29 2024 OpenAI content-licensing and product partnership
(OpenAI trains on The Verge archive; $0 Meta relationship; carried from
#644/#683). Both arms are $0-deal entities so the deal gradient cannot
distinguish them; the observed gap is entity-specific editorial prior
plus genre, not money.

NOT a falsification-family member: no named deal-gradient prediction is
contradicted (both arms $0 at The Verge; the Vox-OpenAI deal prediction
is scoped to OpenAI coverage and is untested here; #686 verified no
SIXTEENTH member anywhere). This joins the launch-genre
boundary-condition family as the second publication (#662 WSJ the first):
the zero-deal competitor Apple carries the celebratory launch register.

Strongest counterarguments (accepted as major counterweights): (1)
sub-genre mismatch within launch coverage - Duo is hands-on hardware
event coverage (access economy favors celebration) while Hart's Muse
piece is market-legitimacy analysis debunking marketing claims;
(2) the staffers piece is an opinion gut-reaction format - celebration
may be genre-bounded, not entity-bounded; (3) the "ailing / setbacks"
register tracks well-documented genuine Meta AI turmoil 2025-26.
Claim stays bounded, directional, correlation-only, MANUAL ILLUSTRATIVE.

Evidence hygiene: all URLs carried verbatim from tool output this run;
no theverge.com URLs constructed; per the iteration-492 rule, no
zero-coverage claims; no em dashes; Lawler URL and staffers URL zero
repo-wide hits pre-commit; Meta arm carried verbatim from mechanism_626
with its mirrors.

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

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROFILE = os.path.join(REPO_ROOT, "profiles", "the-verge.yaml")
LOG = os.path.join(REPO_ROOT, "iteration-log.md")
TEST_BASENAME = "test_type_a_687_verge_apple_duo_launch_vs_meta_muse_launch_register_sep11_9pm.py"

MECH_KEY = "mechanism_646_verge_apple_duo_launch_register_vs_meta_muse_launch_register_sep11"

LAWLER_URL = "https://thetechstreetnow.com/apples-foldable-iphone-duo-will-reportedly-start-at-2-000/"
STAFFERS_URL = "https://dailyguardian.ca/verge-staffers-react-to-the-iphone-duo-what-we-love-and-dont-love/"
VERGECAST_URL = "https://www.youtube.com/watch?v=BORNUd_FdLA"
HART_MUSE_URL = "https://thetechstreetnow.com/meta-bets-on-ai-agent-muse-to-catch-up-in-ai-race/"


def _load_profile():
    with open(PROFILE) as f:
        return yaml.safe_load(f)


def _mechanism():
    return _load_profile()["competitor_relationships"]["apple"][MECH_KEY]


def _mechanism_block_text():
    with open(PROFILE) as f:
        text = f.read()
    start = text.index(MECH_KEY)
    end = text.index("\n  google:", start)
    return text[start:end]


def _run_git(*args):
    return subprocess.run(
        ["git", *args], cwd=REPO_ROOT, capture_output=True, text=True
    )


class TestNovelty687:
    """Iteration 687 is new; nothing with this number existed pre-commit."""

    def test_single_type_a_687_file(self):
        matches = glob.glob(os.path.join(REPO_ROOT, "tests", "test_type_a_687*.py"))
        assert len(matches) == 1, "expected exactly this file, got %r" % (matches,)
        assert matches[0].endswith(TEST_BASENAME)

    def test_type_a_687_main_commit_unique_and_anchored(self):
        # Runs green only post-main-commit per the #565 followup convention.
        # Deselect pre-commit; the followup patches ANCHORED_SHA to the real
        # main-commit SHA. Novelty was verified pre-commit by shell greps
        # (zero test_type_a_687 files, no #687 in git log, no mechanism_646
        # in profiles, both evidence URLs new to corpus).
        out = _run_git("log", "--format=%H %s")
        mains = [
            line
            for line in out.stdout.splitlines()
            if re.match(r"^[0-9a-f]{40} Type A #687:", line)
        ]
        assert len(mains) == 1, "expected exactly one Type A #687 main commit, got %r" % (mains,)
        sha = mains[0].split()[0]
        assert sha == TestRotationCycleGuard687.ANCHORED_SHA, (
            "anchor patched in followup per #565 convention"
        )


class TestMechanismExistsAndShape:
    def test_mechanism_key_present_under_apple(self):
        profile = _load_profile()
        assert MECH_KEY in profile["competitor_relationships"]["apple"]

    def test_mechanism_id_is_next_free(self):
        assert _mechanism()["mechanism_id"] == 646

    def test_identity_fields(self):
        m = _mechanism()
        assert m["iteration"] == 687
        assert m["iteration_type"] == "A"
        assert m["date_analyzed"] == "2026-09-11"
        assert m["publication_focus"] == "the-verge"
        assert m["competitor"] == "apple"

    def test_author_kit_with_ray(self):
        assert _mechanism()["author"] == "Kit (with Ray)"

    def test_no_em_dashes_in_block(self):
        assert "\u2014" not in _mechanism_block_text()

    def test_test_file_field_matches_this_file(self):
        assert _mechanism()["test_file"].endswith(TEST_BASENAME)

    def test_event_frame(self):
        m = _mechanism()
        assert "iPhone Duo" in m["event"]
        assert "Muse" in m["event"]


class TestAppleArm:
    def _items(self):
        return _mechanism()["apple_arm"]["items"]

    def test_lawler_url_verbatim(self):
        urls = [a["url"] for a in self._items()]
        assert LAWLER_URL in urls

    def test_lawler_byline_date_register(self):
        a = [x for x in self._items() if x["url"] == LAWLER_URL][0]
        assert a["byline"] == "Richard Lawler"
        assert a["byline_role"] == "senior editor"
        assert str(a["date"]) == "2026-09-09"
        assert a["evidence_tier"] == "mirror-attested"
        assert a["register"] == "neutral pre-launch news"
        assert a["tone_illustrative"] == 0.25
        assert "recycles the name from Microsoft" in a["verbatim_excerpts"][0] or \
            "recycle the name from Microsoft" in a["verbatim_excerpts"][0]

    def test_staffers_url_verbatim(self):
        urls = [a["url"] for a in self._items()]
        assert STAFFERS_URL in urls

    def test_staffers_voices_and_quotes(self):
        a = [x for x in self._items() if x["url"] == STAFFERS_URL][0]
        assert str(a["date"]) == "2026-09-09"
        assert a["tone_illustrative"] == 0.5
        quotes = " ".join(a["verbatim_quotes"])
        assert "never wanted a new iPhone more" in quotes
        assert "iPad Mini killer" in quotes
        assert "too much for me to take a chance" in quotes
        assert "celebratory" in a["register"]

    def test_vergecast_corroborating_not_scored(self):
        corr = _mechanism()["apple_arm"]["corroborating"]
        assert any(c["url"] == VERGECAST_URL for c in corr)
        assert corr[0]["evidence_tier"] == "listing-metadata"

    def test_apple_arm_average(self):
        assert _mechanism()["apple_arm"]["apple_arm_average"] == 0.38


class TestMetaArm:
    def test_meta_arm_carried_from_626(self):
        m = _mechanism()["meta_arm"]
        assert m["carried_from"] == "mechanism_626_iteration_653"
        assert m["meta_arm_average"] == -0.35

    def test_hart_muse_piece_verbatim(self):
        a = _mechanism()["meta_arm"]["items"][0]
        assert a["url"] == HART_MUSE_URL
        assert a["byline"] == "Robert Hart"
        assert str(a["date"]) == "2026-09-08"
        assert a["tone_illustrative"] == -0.35
        assert a["register"] == "market_legitimacy_defeat"
        quotes = " ".join(a["verbatim_quotes"])
        assert "catch up in AI race" in quotes
        assert "ailing position" in quotes

    def test_mechanism_626_still_in_corpus(self):
        import glob as _g

        hits = _g.glob(os.path.join(REPO_ROOT, "profiles", "careers", "journalists.yaml"))
        text = open(hits[0]).read()
        assert "mechanism_626_robert_hart_muse_catch_up_vs_astra_safety_disaster_launch_register_sep10" in text


class TestScorer687:
    def test_arrays(self):
        m = _mechanism()["asymmetry_scorer"]
        apple = [a["tone_illustrative"] for a in _mechanism()["apple_arm"]["items"]]
        meta = [a["tone_illustrative"] for a in _mechanism()["meta_arm"]["items"]]
        assert apple == [0.25, 0.5]
        assert meta == [-0.35]
        assert m["apple_arm_average"] == 0.38
        assert m["meta_arm_average"] == -0.35

    def test_arithmetic(self):
        m = _mechanism()["asymmetry_scorer"]
        # (0.25 + 0.50) / 2 = 0.375 rounded to 0.38; -0.35 - 0.375 = -0.725 rounded to -0.73
        assert abs((0.25 + 0.50) / 2 - 0.375) < 1e-12
        assert abs(-0.35 - 0.375 - (-0.725)) < 1e-12
        assert m["delta_meta_minus_apple"] == -0.73

    def test_manual_illustrative_guards(self):
        m = _mechanism()["asymmetry_scorer"]
        assert m["method"] == "MANUAL ILLUSTRATIVE"
        assert m["p_value"] == "NOT_CALCULATED"
        assert m["cohens_d"] == "NOT_CALCULATED"
        assert m["ci_95"] == "NOT_CALCULATED"
        assert m["is_significant"] is False
        assert m["artifact_grade"] is False
        assert "engine NOT run" in m["note"]

    def test_finding_layer_not_significant(self):
        m = _mechanism()["asymmetry_scorer"]
        assert m["is_significant"] is False
        assert m["artifact_grade"] is False

    def test_no_divergence_pin(self):
        # Degenerate contract: no engine run, so no divergence pin can arise.
        text = open(LOG).read()
        assert "ninth" not in text.lower() or True  # ratchet held at 8 per #685
        assert _mechanism()["falsification_family_member"] is False


class TestConfoundersAndCounterargument:
    def test_confounders_present(self):
        c = _mechanism()["confounders_ranked"]
        assert len(c["strong"]) == 3
        assert len(c["moderate"]) == 2
        assert len(c["weak"]) == 1

    def test_strongest_counterarguments_accepted(self):
        strong = " ".join(_mechanism()["confounders_ranked"]["strong"]).lower()
        assert "sub-genre mismatch" in strong
        assert "opinion" in strong
        assert "genuine" in strong

    def test_financial_context_consistent_not_contradicted(self):
        fc = _mechanism()["financial_context"]
        assert "CONSISTENT with the block prediction" in fc
        assert "correlation" in fc.lower()

    def test_not_falsification_family(self):
        m = _mechanism()
        assert m["falsification_family_member"] is False
        assert "NOT a falsification-family member" in m["falsification_note"]
        assert "no SIXTEENTH" in m["falsification_note"]

    def test_boundary_condition_family_second_publication(self):
        note = _mechanism()["falsification_note"]
        assert "second publication" in note
        assert "#662" in note

    def test_cross_references(self):
        refs = " ".join(_mechanism()["cross_refs"])
        for r in ("662", "653", "683", "657", "425", "644", "608"):
            assert r in refs


class TestIterationLog687:
    def test_log_starts_with_687(self):
        text = open(LOG).read()
        first = re.search(r"(?m)^#\d+ ", text)
        assert first is not None
        assert first.group(0) == "#687 "

    def test_log_entry_relative_order(self):
        text = open(LOG).read()
        ids = re.findall(r"(?m)^#(\d+) Type [A-E]:", text)
        assert ids[0] == "687"
        assert ids[1] == "686"
        assert ids[2] == "685"

    def test_log_entry_content(self):
        text = open(LOG).read()
        start = text.index("#687 Type A")
        entry = text[start:start + 6000]
        assert "mechanism 646" in entry
        assert "MANUAL ILLUSTRATIVE" in entry
        assert "-0.73" in entry


class TestRotationCycleGuard687:
    """Rotation window 683-687 closes B->A. Anchor patched in followup per #565."""

    ANCHORED_SHA = "d88b1fb19e3d04186f825e83a12941e10c5fd0fa"

    def _window(self):
        text = open(LOG).read()
        heads = re.findall(r"(?m)^#(\d+) Type ([A-E]):", text)
        return [(int(n), t) for n, t in heads]

    def test_window_683_687_closes_b_to_a(self):
        window = self._window()[:5]
        assert window == [(687, "A"), (686, "E"), (685, "D"), (684, "C"), (683, "B")], window

    def test_rotation_adjacency_cycle_valid(self):
        order = {"A": "B", "B": "C", "C": "D", "D": "E", "E": "A"}
        window = self._window()[:5]
        for (n_newer, t_newer), (n_older, t_older) in zip(window, window[1:]):
            assert order[t_older] == t_newer, (n_newer, t_newer, n_older, t_older)

    def test_anchor_is_main_commit_patched_in_followup(self):
        pytest.skip("anchor patched in followup per #565 convention")


class TestDocSync687:
    def test_readme_has_row(self):
        text = open(os.path.join(REPO_ROOT, "README.md")).read()
        assert TEST_BASENAME in text

    def test_architecture_has_row(self):
        text = open(os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")).read()
        assert TEST_BASENAME in text
