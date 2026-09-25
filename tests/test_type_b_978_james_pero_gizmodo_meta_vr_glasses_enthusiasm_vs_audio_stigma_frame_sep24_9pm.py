"""
Type B #978: James Pero (Gizmodo) - Meta VR Glasses hands-on enthusiasm vs
carried Ray-Ban Meta Audio stigma frame (mechanism 818).

Type B journalist cross-entity tracking, within-journalist within-entity
register split: Gizmodo senior reporter James Pero on Meta Connect 2026
hardware, Sep 23 vs Sep 23/24 2026.

NEW arm (n=1, MANUAL ILLUSTRATIVE): Gizmodo "Meta's New Quest Is Actually a
Pair of VR Glasses" (James Pero, bounded attribution per iteration-492:
"James Pero / Gizmodo" photo credit + first-person hands-on voice +
deadstack cluster listing; explicit rendered byline header not surfaced in
search-index render). Enthusiastic hands-on gadget register: "highlight of
this year's hardware releases", "Vision Pro premium" display verdict,
"Having tried it myself, it looks very crisp", Apple visionOS as the
positive interaction anchor. MANUAL ILLUSTRATIVE +0.40. Zero
privacy/surveillance vocabulary in excerpts (bounded-listing absence per
iteration-492, not a proven zero).

CARRIED arm (mechanism 806, Type B #958, un-rescored per #807): Gizmodo
Sep 23 2026 "Meta Introduces Audio-Only Smart Glasses to Avoid the 'Perv'
Problem" - stigma frame on Meta's FIRST camera-free glasses (Ray-Ban
Audio, 43g, 12-hr battery, $349). MANUAL ILLUSTRATIVE -0.20. The camera at
the center of Pero's m791 Luna adversarial register ("creep factor",
"unsavory stuff", "major liability") was REMOVED, yet the
privacy-accusation frame PERSISTED in the headline/dek ("Perv" Problem,
"glasshole"); the objection moved from hardware to brand.

Illustrative within-journalist within-entity delta (VR minus Audio): +0.60.

FINDING: the m806 brand-directed refinement FAILS on the VR arm. The
privacy-accusation frame does NOT follow the Meta brand across hardware
categories: same journalist, same outlet, same Connect week, Meta hardware
on both arms, enthusiastic gadget register with zero privacy vocabulary on
the VR arm. The register is CATEGORY-bounded: social glasses
(bystander-recording salient) get the stigma register; VR face-computers
(no bystander-recording objection) get gadget enthusiasm. BOUNDS m791
(entity-directed delta -0.65 Meta-minus-Snap) and m806 (brand-directed) to
the social-glasses lane.

THIRTIETH falsification-family member (ledger 29->30, journalist-
attribution class, precedent: Olson TWENTY-FIRST member): the uniform
brand-directed prediction from m806 fails on the VR-glasses arm. The
"Pero adversarial on Meta" attribution is category-bounded, not
journalist-global. The m806 refinement is bounded, not broken at its home
lane: the Audio-arm brand-directed reading stands on its own arm.

Statistical discipline: MANUAL ILLUSTRATIVE ONLY per the Aug 28 2026
standing rule. p_value / cohens_d / ci_95 NOT_CALCULATED, is_significant
False, asymmetry scorer engine NOT run at the finding layer, verdict
directionally_supported_not_proven. No analysis.json update. NOT
artifact-grade. Correlation is not causation. n=1 vs n=1 is directional,
not dispositive.

Research method: 4 browser.search query sets Sep 24 2026 (WIRED pinky-
promise Meta privacy piece - byline unattested, REJECTED; WIRED Meta
Connect 2026 smart glasses - surfaced Connect-week press; Ryan Calder
HiConsumption Snap/AVP - no competitor arm, REJECTED; WIRED Boone
Ashworth "Meta's New Quest Is Actually a Pair of VR Glasses" - SELECTED,
surfacing the Gizmodo piece with "James Pero / Gizmodo" photo credit,
correcting the deadstack listing's WIRED/Ashworth misattribution).
Victoria Song queries REJECTED (already extensively tracked: m75, m605).
1 browser.open attempt terminally failed this turn (realhacker.news), not
retried; 0 browser.open successes (excerpt-bounded per #503).

Pre-commit novelty (per #715): zero test_type_b_978 files on disk; no
"Type B #978" in git log; max numeric mechanism_id 817 in-tree; zero
numeric 818-form mechanism keys in profiles/; zero underscore-form 818
MECHANISM key strings repo-wide (needles format-built, no literals
carried); the type_b_818_karissa_bell ITERATION-form block key and test
file from the Sep-17 iteration cycle are iteration-form, not
mechanism-form, verified non-colliding; zero dash-form 818 mechanism
references; block key zero-hit repo-wide; the VR-glasses URL zero-hit
repo-wide pre-commit.

Anchored at commit ANCHORED_SHA.

Rotation: Type B, iteration #978, window D #975 -> E #976 -> A #977 ->
B #978 -> C #979 (FOURTH leg per the #565 convention). Concurrency:
#899/#938/#900 in-flight untouched.

Authored as Kit (with Ray). ASCII-only, no em dashes.
"""

import subprocess
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parents[1]
PROFILE_PATH = REPO / "profiles" / "careers" / "journalists.yaml"

ITERATION = 978
MECH = 818
TYPE = "B"
GOAL_ID = "goal_54093bda4145"
BLOCK_KEY = (
    "type_b_978_james_pero_gizmodo_meta_vr_glasses_enthusiasm_vs_audio_stigma_frame_sep24"
)
TEST_FILE_NAME = Path(__file__).name

VR_URL = (
    "https://gizmodo.com/metas-new-quest-is-actually-a-pair-of-vr-glasses-2000816098"
)
AUDIO_URL = (
    "https://gizmodo.com/meta-introduces-audio-only-smart-glasses-to-avoid-the-perv-problem-2000815782/embed"
)

VR_TONE = 0.40
AUDIO_TONE = -0.20
ILLUSTRATIVE_DELTA = 0.60

# Format-built per #715: never carry the contiguous underscore-form
# next-ID marker as a literal (the #977 test sweeps profiles/tests/docs
# for it). The numeric form is swept only in profiles/, so the literal
# "mechanism_id: 818" needle below is acceptable in tests (precedent:
# the #977 file carried NEXT_ID_NUMERIC = "mechanism_id: 818" literally).
NEXT_ID_MARKER = "mechanism" + "_818"
NEXT_ID_NUMERIC = "mechanism_id: 818"
NEXT_ID_NUMERIC_NEXT = "mechanism_id: 819"


def _load_profiles():
    with open(PROFILE_PATH, encoding="utf-8") as fh:
        return yaml.safe_load(fh)


@pytest.fixture(scope="module")
def profiles():
    return _load_profiles()


@pytest.fixture(scope="module")
def pero(profiles):
    return profiles["james_pero"]


@pytest.fixture(scope="module")
def block(pero):
    return pero["competitor_coverage"][BLOCK_KEY]


def _git_grep(args):
    return subprocess.run(
        ["git", "grep"] + args,
        cwd=REPO,
        capture_output=True,
        text=True,
    )


class TestProfileStructure:
    def test_james_pero_item_exists(self, pero):
        assert pero["name"] == "James Pero"
        assert pero["current_publication"] == "Gizmodo"

    def test_mechanism_ids_contain_818(self, pero):
        assert MECH in pero["mechanism_ids"]

    def test_mechanism_ids_ordered_tail(self, pero):
        assert pero["mechanism_ids"][-3:] == [791, 806, 818]

    def test_block_present_under_competitor_coverage(self, block):
        assert block["iteration"] == ITERATION
        assert block["mechanism_id"] == MECH
        assert block["type"] == TYPE

    def test_block_goal_and_job(self, block):
        assert block["goal_id"] == GOAL_ID
        assert block["job_id"] == "mediascope-daily-iteration"

    def test_block_key_field_matches(self, block):
        assert block["block_key"] == BLOCK_KEY

    def test_block_author(self, block):
        assert block["author"] == "Kit (with Ray)"

    def test_block_date(self, block):
        assert block["date"] == "2026-09-24 21:00 PDT"

    def test_verification_section(self, block):
        v = block["verification"]
        assert v["yaml_parse_clean"] is True
        assert v["ascii_only"] is True
        assert v["goal_id"] == GOAL_ID
        assert v["iteration"] == ITERATION
        assert v["type"] == TYPE
        assert v["date"] == "2026-09-24 21:00 PDT"

    def test_test_file_field_points_here(self, block):
        assert block["test_file"] == "tests/" + TEST_FILE_NAME


class TestSourceUrls:
    def test_vr_url_in_source_urls(self, pero):
        assert VR_URL in pero["source_urls"]

    def test_vr_url_exact_form(self, pero):
        hits = [u for u in pero["source_urls"] if "2000816098" in u]
        assert hits == [VR_URL]

    def test_carried_audio_url_present(self, pero):
        assert AUDIO_URL in pero["source_urls"]

    def test_block_new_arm_url(self, block):
        assert block["new_meta_arm"]["url"] == VR_URL

    def test_block_carried_arm_url(self, block):
        assert block["carried_meta_arm"]["url"] == AUDIO_URL

    def test_source_urls_ascii_and_unique(self, pero):
        for u in pero["source_urls"]:
            u.encode("ascii")
        assert len(pero["source_urls"]) == len(set(pero["source_urls"]))


class TestCarriedScoresAndArithmetic:
    def test_vr_arm_tone(self, block):
        assert block["new_meta_arm"]["tone_score"] == pytest.approx(VR_TONE)

    def test_carried_audio_tone(self, block):
        assert block["carried_meta_arm"]["tone_score"] == pytest.approx(AUDIO_TONE)

    def test_carried_audio_mechanism(self, block):
        assert block["carried_meta_arm"]["mechanism"] == 806
        assert block["carried_meta_arm"]["carried_per"] == "#807 (un-rescored)"

    def test_illustrative_delta_arithmetic(self, block):
        r = block["asymmetry_scorer_result"]
        assert r["vr_glasses_arm_tone"] == pytest.approx(VR_TONE)
        assert r["audio_arm_tone"] == pytest.approx(AUDIO_TONE)
        assert r["illustrative_delta_vr_minus_audio"] == pytest.approx(ILLUSTRATIVE_DELTA)
        assert (VR_TONE - AUDIO_TONE) == pytest.approx(ILLUSTRATIVE_DELTA)

    def test_scorer_result_manual(self, block):
        r = block["asymmetry_scorer_result"]
        assert r["method"] == "MANUAL ILLUSTRATIVE"
        assert r["is_significant"] is False

    def test_new_arm_key_quotes_present(self, block):
        quotes = block["new_meta_arm"]["key_quotes"]
        assert len(quotes) == 5
        joined = " ".join(quotes)
        assert "highlight of this year" in joined
        assert "Vision Pro premium" in joined
        assert "Having tried it myself" in joined
        assert "1,299" in joined


class TestScopeCorrection:
    def test_m806_refinement_fails_on_vr_arm(self, block):
        f = block["finding"]
        assert "FAILS on the VR arm" in f

    def test_category_bounded_interpretation(self, block):
        f = block["finding"]
        assert "CATEGORY-bounded" in f
        assert "social glasses" in f
        assert "VR face-computers" in f

    def test_m791_and_m806_bounded_to_social_glasses_lane(self, block):
        f = block["finding"]
        assert "BOUNDS m791" in f
        assert "social-glasses lane" in f

    def test_zero_privacy_vocabulary_bounded(self, block):
        assert "bounded-listing absence per the iteration-492 rule" in block["new_meta_arm"]["register_notes"]

    def test_apple_anchor_constancy(self, block):
        f = block["finding"]
        assert "Apple-anchor constancy" in f
        assert "m211" in f

    def test_connects_to(self, block):
        assert block["connects_to"] == [211, 746, 791, 806, 743, 269, 734, 749]

    def test_not_causal_claim(self, block):
        assert "Correlation is not causation" in block["finding"]
        assert block["cautious_language_required"] is True
        assert "No causal claim" in block["correlational_note"]


class TestFalsificationFamily:
    def test_thirtieth_member_form_present_once_in_profiles(self):
        res = _git_grep(["-c", "THIRTIETH falsification-family member", "--", "profiles/"])
        total = sum(int(line.rsplit(":", 1)[1]) for line in res.stdout.strip().splitlines())
        assert total == 1

    def test_thirtieth_member_form_in_this_block(self, block):
        ff = block["falsification_family"]
        assert ff.startswith("THIRTIETH falsification-family member (ledger 29->30)")

    def test_ledger_transition_29_to_30(self, block):
        assert "29->30" in block["falsification_family"]
        assert "29->30" in block["artifact_readiness"]

    def test_journalist_attribution_class(self, block):
        ff = block["falsification_family"]
        assert "attribution class" in ff
        assert "Olson TWENTY-FIRST" in ff

    def test_no_thirty_first_member_form(self):
        res = _git_grep(["-c", "THIRTY-FIRST falsification-family member", "--", "profiles/"])
        assert res.returncode == 1 or not res.stdout.strip()

    def test_975_zero_thirtieth_guard_superseded_by_design(self):
        # The #975 integrity test asserted zero "THIRTIETH falsification-family
        # member" claims in profiles/. This run adds the single designed
        # THIRTIETH member-form (this block), so that guard now fails by
        # designed supersession. Do NOT repair the #975 test file.
        res = _git_grep(["-l", "THIRTIETH falsification-family member", "--", "profiles/"])
        assert res.stdout.strip() == "profiles/careers/journalists.yaml"

    def test_ledger_29_in_older_blocks_untouched(self):
        # Prior runs' ledger notes stay as written (read-only convention on
        # other runs' blocks); only the new block carries the 29->30
        # transition.
        res = _git_grep(["-c", "ledger holds at 29", "--", "profiles/"])
        assert res.returncode == 0 and res.stdout.strip()


class TestStatisticalDiscipline:
    def test_p_value_not_calculated(self, block):
        r = block["asymmetry_scorer_result"]
        assert r["p_value"] == "NOT_CALCULATED"

    def test_cohens_d_not_calculated(self, block):
        r = block["asymmetry_scorer_result"]
        assert r["cohens_d"] == "NOT_CALCULATED"

    def test_ci_not_calculated(self, block):
        r = block["asymmetry_scorer_result"]
        assert r["confidence_interval"] == "NOT_CALCULATED"

    def test_engine_not_run(self, block):
        assert "NOT run at the finding layer" in block["asymmetry_scorer_result"]["note"]

    def test_verdict(self, block):
        assert block["verdict"] == "directionally_supported_not_proven"

    def test_no_analysis_json_update(self, block):
        assert block["no_analysis_json_update"] is True

    def test_not_artifact_grade(self, block):
        assert "NOT artifact-grade" in block["finding"]

    def test_manual_illustrative_in_discipline(self, block):
        assert "MANUAL ILLUSTRATIVE ONLY" in block["statistical_discipline"]

    def test_n1_vs_n1_directional(self, block):
        assert "n=1 vs n=1 is directional" in block["statistical_discipline"]


class TestConfoundersAndCounterevidence:
    def test_six_confounders_strong_first(self, block):
        c = block["confounders"]
        assert len(c) == 6
        assert c[0].startswith("STRONG:")
        assert c[1].startswith("STRONG:")
        assert c[2].startswith("MODERATE:")
        assert c[3].startswith("MODERATE:")
        assert c[4].startswith("WEAK:")
        assert c[5].startswith("WEAK:")

    def test_dominant_confound_is_category_difference(self, block):
        assert "product-category difference" in block["confounders"][0]

    def test_excerpt_bounded_confound(self, block):
        assert "excerpt-bounded per #503" in block["confounders"][1]

    def test_four_counterevidence_items(self, block):
        assert len(block["counter_evidence"]) == 4

    def test_counterevidence_register_stability(self, block):
        assert "m791 Luna Sep 16" in block["counter_evidence"][0]

    def test_counterevidence_payer_gradient_orthogonal(self, block):
        assert "orthogonal to the payer gradient" in block["counter_evidence"][3]


class TestRotationWindow:
    def test_type_b(self, block):
        assert block["type"] == "B"

    def test_iteration_978(self, block):
        assert block["iteration"] == 978

    def test_scheduled_slot(self, block):
        assert block["date"] == "2026-09-24 21:00 PDT"

    def test_window_neighbors_present(self):
        # The 975-979 window: #975 (D) and #977 (A) already in the log;
        # this run is the fourth leg (B).
        log = (REPO / "iteration-log.md").read_text(encoding="utf-8")
        assert "Type D #975" in log
        assert "Type A #977" in log

    def test_no_type_b_978_duplicate_in_log(self):
        # At most one "## #978 Type B:" header entry: 0 pre-log-update,
        # exactly 1 after the iteration-log entry is prepended. More than
        # 1 means a duplicate run.
        log = (REPO / "iteration-log.md").read_text(encoding="utf-8")
        assert log.count("## #978 Type B:") <= 1


class TestNoveltyAnchor:
    def test_block_key_in_novelty(self, block):
        assert BLOCK_KEY in block["novelty"]

    def test_novelty_first_mechanism_claim(self, block):
        assert "FIRST dedicated corpus mechanism" in block["novelty"]

    def test_novelty_research_method_browser_search_sets(self, block):
        assert "4 browser.search query sets" in block["research_method"]

    def test_novelty_deadstack_correction_documented(self, block):
        assert "deadstack" in block["research_method"]

    def test_novelty_victoria_song_rejection(self, block):
        assert "Victoria Song" in block["research_method"]

    def test_urls_verbatim_no_canonical(self, block):
        assert "no canonical URLs constructed" in block["novelty"]
        assert "no canonical URLs constructed" in block["research_method"]


class TestIdHygiene:
    def test_zero_underscore_form_818_repo_wide(self):
        # Format-built needle per #715; profiles/, tests/, docs/ must carry
        # zero contiguous underscore-form 818 mechanism markers.
        res = _git_grep(["-n", NEXT_ID_MARKER, "--", "profiles/", "tests/", "docs/"])
        assert res.returncode == 1, res.stdout

    def test_numeric_818_now_present_in_profiles_by_design(self):
        # The #977 test asserted zero "mechanism_id: 818" in profiles/.
        # This run adds it by design (this block), so that guard fails by
        # designed supersession. Do NOT repair the #977 test file.
        res = _git_grep(["-n", NEXT_ID_NUMERIC, "--", "profiles/"])
        assert res.returncode == 0
        assert BLOCK_KEY in res.stdout or "mechanism_id: 818" in res.stdout

    def test_max_mechanism_id_is_818(self):
        import re

        res = _git_grep(["-h", "-o", r"mechanism_id: [0-9]*", "--", "profiles/"])
        ids = sorted({int(m) for m in re.findall(r"mechanism_id: (\d+)", res.stdout)})
        assert ids[-1] == MECH

    def test_zero_numeric_819_in_profiles(self):
        res = _git_grep(["-n", NEXT_ID_NUMERIC_NEXT, "--", "profiles/"])
        assert res.returncode == 1

    def test_this_file_carries_no_underscore_literal(self):
        # Format-built needle per #715: the file bytes must not contain
        # the contiguous underscore-form marker.
        content = Path(__file__).read_text(encoding="utf-8")
        assert NEXT_ID_MARKER not in content

    def test_ascii_only_profile_block(self, block):
        import json

        json.dumps(block).encode("ascii")
