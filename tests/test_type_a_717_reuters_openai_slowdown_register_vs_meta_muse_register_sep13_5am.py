"""Type A #717 (2026-09-13 05:00 PDT): Reuters x OpenAI slowdown-week
register vs Reuters x Meta Muse accountability register (mechanism 664).

SECOND Reuters x OpenAI Type A mechanism (first was m634, iteration
#667, Sep 11 2026: Reuters x OpenAI enterprise-news arms vs the same
Reuters x Meta Muse -0.45 arm, FOURTEENTH falsification-family member,
delta +0.625); FIRST slowdown-week Type A; FIRST dedicated mechanism on
the Altman "not 2026" IPO safety-framing at any tracked publication.
This block is a same-pair replication test of m634's payer-penalty pin
in a new genre (CEO safety-virtue interview vs enterprise/product news).

OpenAI arm (Reuters, Sep 12 2026, Lisa Baertlein): "OpenAI IPO will not
happen in 2026 amid AI safety fears, Altman says"
(https://www.reuters.com/legal/litigation/openai-ipo-will-not-happen-2026-amid-ai-safety-fears-altman-says-2026-09-12/,
new to corpus pre-commit, excerpt-bounded per #503): Altman tells
Fortune a 2026 IPO would be an "ill-advised moment" given AI safety;
"I would say not 2026. Yeah, we got a lot of stuff to do, like meeting
this moment of what is going to be required for safety and alignment";
Altman suggests OpenAI and peers "may be close to announcing an
agreement to slow AI development"; Altman posted agreement with
Amodei's "pace the frontier" call. Earnest safety-virtue relay, zero
skepticism markers; scored +0.30.

Meta arm (Reuters, Sep 8 2026, Katie Paul, carried from m633 via m649):
Muse launch piece runs a hard accountability register - "despite
internal concerns that the technology mismanages its access to
sensitive personal data," "RAISING THE STAKES FOR SAFETY" section
header; scored -0.45.

Scorer (MANUAL ILLUSTRATIVE, standing rule Aug 28 2026; arithmetic
only): OpenAI [+0.30] vs Meta [-0.45]. Delta (OpenAI minus Meta) +0.75.
p_value NOT_CALCULATED, cohens_d NOT_CALCULATED, ci NOT_CALCULATED,
is_significant False, artifact_grade False. Classic degenerate
statistical contract per the #638/#643 convention (n=1 vs n=1, t=0.0,
p=1.0, d=0.0); engine NOT run; no divergence pin.

Financial context (correlation, not causation): Reuters is PAID BY Meta
under the Oct 25 2024 multiyear AI news licensing deal (mechanism 633,
ACTIVE per the #599/#609 convention - no renewal, extension,
renegotiation, or termination reporting surfaced); no Reuters x OpenAI
AI licensing deal on record (bounded absence per the iteration-492
rule; Thomson Reuters CEO Steve Hasker confirmed only licensing TALKS
with multiple AI providers - talks are not deals). The incentive theory
predicts softer coverage of the payer than of the non-payer at the same
wire; the observed direction is opposite. TWENTY-THIRD
falsification-family member (ledger stood at 22 after #708's
TWENTY-SECOND, m659); #715's TWENTY-THIRD-absent sweep fails by
designed supersession (per the #710 convention).

Strongest counterargument (accepted as a major counterweight): genre
mismatch is load-bearing - Altman's self-framed safety interview (the
news peg IS Altman's own statement) vs a product launch with internal
privacy concerns; different pegs default to different registers
independent of outlet incentives. Altman self-framing advantage is the
second strong confound. Correlation only; no causal claim.
"""

import glob
import os
import re
import subprocess
from datetime import datetime

import pytest
import yaml

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
PROFILE_PATH = os.path.join(REPO_ROOT, "profiles", "competitor-entities.yaml")
LOG_PATH = os.path.join(REPO_ROOT, "iteration-log.md")
TEST_BASENAME = os.path.basename(__file__)
MECH_KEY = "mechanism_664_reuters_openai_slowdown_week_register_vs_meta_muse_accountability_sep13"
ALTMAN_URL = "https://www.reuters.com/legal/litigation/openai-ipo-will-not-happen-2026-amid-ai-safety-fears-altman-says-2026-09-12/"
MUSE_URL = "https://www.reuters.com/business/meta-launches-ai-agent-that-can-access-other-apps-send-emails-make-payments-2026-09-08/"


def _read(path):
    with open(path, "r", encoding="utf-8") as fh:
        return fh.read()


def _profiles():
    with open(PROFILE_PATH, "r", encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def _entity():
    return _profiles()["entities"]["openai"]


def _mechanism():
    return _entity()[MECH_KEY]


def _run_git(*args):
    return subprocess.run(
        ["git", "-C", REPO_ROOT, *args],
        capture_output=True,
        text=True,
        timeout=60,
    )


class TestNovelty717:
    """Iteration 717 is new; mechanism 664 is the next free id."""

    def test_single_type_a_717_file(self):
        matches = glob.glob(os.path.join(REPO_ROOT, "tests", "test_type_a_717*.py"))
        assert len(matches) == 1, "expected exactly this file, got %r" % (matches,)
        assert matches[0].endswith(TEST_BASENAME)

    def test_type_a_717_main_commit_unique_and_anchored(self):
        # Runs green only post-main-commit per the #565 followup convention.
        # Deselect pre-commit; the followup patches ANCHORED_SHA to the real
        # main-commit SHA. Novelty was verified pre-commit by shell greps
        # (zero test_type_a_717 files, no #717 in git log, zero
        # mechanism_664 keys in profiles/ and tests/ pre-commit - the
        # historical test_type_c_664 file carries iteration 664 via
        # _mechanism()["iteration"], not a mechanism_664 key, per #715;
        # max numeric mechanism 663, Altman URL zero-hit repo-wide).
        out = _run_git("log", "--format=%H %s")
        mains = [
            line
            for line in out.stdout.splitlines()
            if re.match(r"^[0-9a-f]{40} Type A #717:", line)
        ]
        assert len(mains) == 1, "expected exactly one Type A #717 main commit, got %r" % (mains,)
        sha = mains[0].split()[0]
        assert sha == TestRotationCycleGuard717.ANCHORED_SHA, (
            "anchor patched in followup per #565 convention"
        )


class TestMechanismExistsAndShape:
    def test_mechanism_key_present_under_openai_entity(self):
        assert MECH_KEY in _entity()

    def test_mechanism_id_is_next_free(self):
        assert _mechanism()["mechanism_id"] == 664

    def test_identity_fields(self):
        m = _mechanism()
        assert m["iteration"] == 717
        assert m["iteration_type"] == "A"
        assert m["date_analyzed"] == "2026-09-13"
        assert m["publication_focus"] == "reuters"
        assert m["competitor"] == "openai"

    def test_author_kit_with_ray(self):
        assert _mechanism()["author"] == "Kit (with Ray)"

    def test_no_line_separators_in_block(self):
        # Guards the 2026-09-10 muse.write U+2028/U+2029 lesson.
        text = _read(PROFILE_PATH)
        start = text.index(MECH_KEY)
        end = text.index("\n  anthropic:", start)
        assert " " not in text[start:end]
        assert " " not in text[start:end]

    def test_no_em_dashes_in_block(self):
        text = _read(PROFILE_PATH)
        start = text.index(MECH_KEY)
        end = text.index("\n  anthropic:", start)
        assert "—" not in text[start:end]

    def test_test_file_field_matches_this_file(self):
        assert _mechanism()["test_file"].endswith(TEST_BASENAME)

    def test_event_frame(self):
        m = _mechanism()
        assert "slowdown" in m["event"].lower()
        assert "Muse" in m["event"]
        assert "Reuters" in m["event"]


class TestOpenAIArm:
    def test_url_verbatim(self):
        assert _mechanism()["openai_arm"]["url"] == ALTMAN_URL

    def test_byline_and_date(self):
        arm = _mechanism()["openai_arm"]
        assert arm["byline"] == "Lisa Baertlein"
        assert arm["date"].startswith("2026-09-12")

    def test_register_and_tone(self):
        arm = _mechanism()["openai_arm"]
        assert arm["register"] == "safety_virtue_earnest_relay"
        assert arm["manual_illustrative_tone"] == pytest.approx(0.30)

    def test_key_framing_quotes(self):
        framing = _mechanism()["openai_arm"]["key_framing"]
        assert "ill-advised moment" in framing
        assert "not 2026" in framing
        assert "pace the frontier" in framing

    def test_excerpt_bounded_disclosed(self):
        assert "excerpt-bounded" in _mechanism()["openai_arm"]["source_note"]

    def test_altman_url_new_to_corpus_elsewhere(self):
        # The Altman URL may appear only in the m664 block and this test
        # file (both added this run). Any other occurrence would mean it
        # was not actually new to the corpus pre-commit.
        hits = []
        for root, _dirs, files in os.walk(REPO_ROOT):
            if ".git" in root or "__pycache__" in root or ".venv" in root:
                continue
            for fn in files:
                if not (fn.endswith(".yaml") or fn.endswith(".py") or fn.endswith(".md")):
                    continue
                p = os.path.join(root, fn)
                if ALTMAN_URL in _read(p):
                    hits.append(os.path.relpath(p, REPO_ROOT))
        allowed = {
            os.path.join("profiles", "competitor-entities.yaml"),
            os.path.join("tests", TEST_BASENAME),
        }
        assert set(hits) == allowed, hits


class TestMetaArm:
    def test_url_verbatim(self):
        assert _mechanism()["meta_arm"]["url"] == MUSE_URL

    def test_register_and_tone_carried(self):
        arm = _mechanism()["meta_arm"]
        assert arm["register"] == "hard_accountability"
        assert arm["manual_illustrative_tone"] == pytest.approx(-0.45)

    def test_key_framing_accountability_markers(self):
        framing = _mechanism()["meta_arm"]["key_framing"]
        assert "despite internal concerns" in framing
        assert "RAISING THE STAKES FOR SAFETY" in framing

    def test_carried_lineage(self):
        assert "mechanism 633" in _mechanism()["meta_arm"]["source_note"]
        assert "mechanism 649" in _mechanism()["meta_arm"]["source_note"]


class TestScorer717:
    """Degenerate-boundary contract through the real calculate_asymmetry path."""

    def _run(self, target, peer):
        import sys

        sys.path.insert(0, REPO_ROOT)
        from mediascope.score.asymmetry import calculate_asymmetry

        return calculate_asymmetry(
            target,
            peer,
            "openai",
            ["meta"],
            "reuters",
            datetime(2026, 9, 8),
            datetime(2026, 9, 12),
        )

    def test_delta_matches_pinned_illustrative(self):
        r = self._run([0.30], [-0.45])
        assert abs(r.asymmetry_score - 0.75) < 1e-9
        assert abs(r.asymmetry_score - _mechanism()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]["delta_manual_illustrative"]) < 1e-9

    def test_degenerate_contract(self):
        r = self._run([0.30], [-0.45])
        assert r.t_statistic == 0.0
        assert r.p_value == 1.0
        assert r.cohens_d == 0.0
        assert r.is_significant is False

    def test_arm_swap_negates_exactly(self):
        r = self._run([-0.45], [0.30])
        assert abs(r.asymmetry_score - (-0.75)) < 1e-9

    def test_delta_calc_string(self):
        assert _mechanism()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]["delta_calc"] == "0.30 - (-0.45) = 0.75"

    def test_engine_not_run(self):
        assert _mechanism()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]["engine_run"] is False

    def test_statistical_discipline(self):
        sd = _mechanism()["statistical_discipline"]
        assert sd["p_value"] == "NOT_CALCULATED"
        assert sd["is_significant"] is False
        assert "MANUAL ILLUSTRATIVE" in sd["scope"]


class TestFinancialContext717:
    def test_payer_leg(self):
        fc = _mechanism()["financial_context"]
        assert "Meta PAYS Reuters" in fc["gradient"]
        assert "Oct 25 2024" in fc["gradient"]

    def test_prediction_direction(self):
        fc = _mechanism()["financial_context"]
        assert fc["prediction"] == "softer Meta coverage than OpenAI coverage at the same wire"

    def test_observed_opposite(self):
        fc = _mechanism()["financial_context"]
        assert fc["observed"].startswith("opposite:")

    def test_openai_deal_absence_bounded(self):
        absence = _mechanism()["financial_context"]["reuters_openai_deal_absence"]
        assert "iteration-492" in absence
        assert "talks are not deals" in absence

    def test_m633_cross_reference(self):
        refs = " ".join(_mechanism()["cross_references"])
        assert "mechanism 633" in refs
        assert "mechanism 649" in refs


class TestFalsificationFamily717:
    def test_twenty_third_membership_claimed(self):
        ff = _mechanism()["falsification_family"]
        assert "TWENTY-THIRD" in ff["membership"]

    def test_ledger_baseline(self):
        ff = _mechanism()["falsification_family"]
        assert "22" in ff["membership"]
        assert "m659" in ff["membership"]

    def test_rationale_names_gradient_and_direction(self):
        rationale = _mechanism()["falsification_family"]["rationale"]
        assert "financial gradient" in rationale
        assert "opposite direction" in rationale


class TestConfoundersAndCrossRefs717:
    def test_genre_mismatch_ranked_first_and_strong(self):
        confs = _mechanism()["ranked_confounders"]
        first = min(confs, key=lambda c: c["rank"])
        assert first["rank"] == 1
        assert first["strength"] == "strong"
        assert "genre mismatch" in first["confounder"]

    def test_altman_self_framing_ranked_second(self):
        confs = {c["rank"]: c for c in _mechanism()["ranked_confounders"]}
        assert confs[2]["strength"] == "strong"
        assert "self-framing" in confs[2]["confounder"]

    def test_four_confounders(self):
        assert len(_mechanism()["ranked_confounders"]) == 4

    def test_correlational_note_no_causal_claim(self):
        assert "No causal claim" in _mechanism()["correlational_note"]


class TestIterationLog717:
    def test_log_has_717_entry(self):
        text = _read(LOG_PATH)
        assert re.search(r"(?m)^#717 Type A:", text), "iteration-log.md missing #717 Type A entry"

    def test_log_entry_names_mechanism_664(self):
        text = _read(LOG_PATH)
        head = text[:6000]
        assert "mechanism 664" in head
        assert "#717" in head


class TestRotationCycleGuard717:
    """Rotation window 713-717 closes E->A. Anchor patched in followup per #565."""

    ANCHORED_SHA = "28d7f576a65bd6c90adb6f8d3b1c9113a4cf75c1"

    def _window(self):
        text = _read(LOG_PATH)
        heads = re.findall(r"(?m)^#(\d+) Type ([A-E]):", text)
        return [(int(n), t) for n, t in heads]

    def test_window_713_717_closes_e_to_a(self):
        window = self._window()[:5]
        assert window == [(717, "A"), (716, "E"), (715, "D"), (714, "C"), (713, "B")], window

    def test_rotation_adjacency_cycle_valid(self):
        order = {"A": "B", "B": "C", "C": "D", "D": "E", "E": "A"}
        window = self._window()[:5]
        for (n_newer, t_newer), (n_older, t_older) in zip(window, window[1:]):
            assert order[t_older] == t_newer, (n_newer, t_newer, n_older, t_older)

    def test_anchor_is_main_commit_patched_in_followup(self):
        result = _run_git("log", "--format=%H %s")
        assert result.returncode == 0
        mains = [
            line for line in result.stdout.splitlines() if "Type A #717:" in line
        ]
        main = mains[0].split()[0] if mains else ""
        assert ANCHORED_SHA == main, (
            "anchor patched in followup per #565 convention"
        )


class TestDocSync717:
    def test_readme_has_row(self):
        text = _read(os.path.join(REPO_ROOT, "README.md"))
        assert TEST_BASENAME in text

    def test_architecture_has_row(self):
        text = _read(os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md"))
        assert TEST_BASENAME in text


class TestSweepSupersession717:
    """Pins the post-#717 state; documents #715's TWENTY-THIRD-absent sweep
    designed supersession (per the #710 convention)."""

    def test_max_mechanism_id_is_664(self):
        text = _read(PROFILE_PATH)
        ids = [int(x) for x in re.findall(r"mechanism_id:\s*(\d+)\b", text)]
        modern = [i for i in ids if i >= 600]
        assert max(modern) == 664, max(modern)

    def test_exactly_one_mechanism_664_key_under_openai(self):
        text = _read(PROFILE_PATH)
        keys = re.findall(r"(?m)^    mechanism_664_\w+:", text)
        assert keys == [
            "    mechanism_664_reuters_openai_slowdown_week_register_vs_meta_muse_accountability_sep13:"
        ], keys

    def test_distinct_from_m634_same_pair_predecessor(self):
        # m634 (#667) was the FIRST Reuters x OpenAI Type A (enterprise-news
        # arms, FOURTEENTH member). This block must not duplicate its peg or
        # register: different OpenAI arm (Altman slowdown-week interview),
        # different novelty claim, explicit cross-reference.
        m634 = _entity()["mechanism_634_reuters_openai_sep_week_register_vs_reuters_meta_muse_register"]
        assert m634["mechanism_id"] == 634
        m664 = _mechanism()
        assert m664["openai_arm"]["url"] != m634["openai_articles"][0]["url"]
        assert "m634" in m664["novelty"]
        assert "SECOND Reuters x OpenAI" in m664["novelty"]
        refs = " ".join(m664["cross_references"])
        assert "mechanism 634" in refs

    def test_twenty_third_now_present_somewhere(self):
        # #715's sweep asserted TWENTY-THIRD absent repo-wide; this run
        # supersedes it by design with m664's membership claim.
        text = _read(PROFILE_PATH)
        assert "TWENTY-THIRD" in text

    def test_no_bare_664_collision_with_historical_iteration_file(self):
        # Guards the #715 lesson: test_type_c_664 carries iteration 664 via
        # _mechanism()["iteration"], not a mechanism_664 key. Our key pattern
        # must not match it.
        text = _read(os.path.join(REPO_ROOT, "tests", "test_type_c_664_meta_reuters_ai_chatbot_deal_falsification_sep10_9pm.py"))
        assert "mechanism_664_" not in text
