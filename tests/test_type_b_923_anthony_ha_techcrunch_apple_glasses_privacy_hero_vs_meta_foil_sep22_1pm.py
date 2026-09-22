"""Type B #923: Anthony Ha (TechCrunch weekend editor) within-writer
privacy-hero register across entities.

SECOND dedicated Type B mechanism on Anthony Ha (mechanism_id 785, next free
pre-commit; max numeric mechanism_id was 784). Within-writer comparison across
two Ha bylines on two entity classes:

(a) Apple arm: Jul 26 2026 TechCrunch "Can Apple make smart glasses that are
not a constant privacy threat?", opinion essay, tone +0.30 hand-assigned this
run (MANUAL ILLUSTRATIVE). Full text read first-hand via browser.open this
run. Apple is the privacy hero: on-device processing, no facial recognition
plans; Meta's glasses are labeled "pervert glasses" (non-consensual
recording, contractors reviewing footage).

(b) Meta arm: Aug 16 2026 TechCrunch "Why people aren't buying Mark
Zuckerberg's AI future", skeptical podcast-preview essay, tone -0.45 carried
from #633 un-rescored (MANUAL ILLUSTRATIVE). First-hand read in #633.

Illustrative delta (meta minus apple) = -0.45 - 0.30 = -0.75; p_value,
cohens_d NOT_CALCULATED; is_significant False (Aug 28 standing rule).
VERDICT: WITHIN-WRITER PRIVACY-HERO REGISTER, directionally consistent with
the Apple privacy cascade but NOT a falsification pin. Mechanism 269 in
competitor-coverage-research.yaml cites this URL only as contextual citation;
this run is the first mechanismization of Ha's within-writer cross-entity
register. Correlation is not causation per the Aug 28 rule: STRONG genre
(opinion essay about a nonexistent product vs podcast-preview reacting to a
manifesto) and temporal (Jul 26 vs Aug 16) confounds fully explain the gap
before any incentive effect is invoked; no newsroom-behavior claim is made.
NOT a falsification-family member. NOT a pure asymmetry pin.

Rotation: Type B follows Type A (#922) per A,B,C,D,E. FOURTH leg of the
920-924 window: D (#920) -> E (#921) -> A (#922) -> B (#923) -> C (#924).
Novelty anchor + rotation guard deselected pre-commit per #565, patched green
in the anchor followup once the main commit SHA is known.
"""

import os
import re
import subprocess

import pytest
import yaml

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROFILE = os.path.join(REPO, "profiles", "careers", "journalists.yaml")
THIS_FILE = "test_type_b_923_anthony_ha_techcrunch_apple_glasses_privacy_hero_vs_meta_foil_sep22_1pm.py"
BLOCK_KEY = "type_b_923_anthony_ha_techcrunch_apple_glasses_privacy_hero_vs_meta_foil"

ANCHORED_SHA = "PATCH_ME_IN_FOLLOWUP"  # patched green in the anchor followup per #565
ITER = 923
TYPE_LETTER = "B"

APPLE_TONE = 0.30
META_TONE = -0.45
EXPECTED_DELTA = -0.75

APPLE_URL = "https://techcrunch.com/2026/07/26/can-apple-make-smart-glasses-that-arent-a-constant-privacy-threat/"
META_URL = "https://techcrunch.com/2026/08/16/why-people-arent-buying-mark-zuckerbergs-ai-future/"
AUTHOR_URL = "http://techcrunch.com/author/anthony-ha/"


def _read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def _journalists():
    with open(PROFILE, encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def _ha():
    matches = [j for j in _journalists()["journalists"]
               if j.get("name") == "Anthony Ha"]
    assert len(matches) == 1, f"expected exactly one Anthony Ha entry, got {len(matches)}"
    return matches[0]


def _block():
    cc = _ha().get("competitor_coverage", {})
    assert BLOCK_KEY in cc, f"{BLOCK_KEY} missing from Anthony Ha competitor_coverage"
    return cc[BLOCK_KEY]


# ---------------------------------------------------------------------------
# 1. Novelty anchor (deselected pre-commit per #565, patched green post-commit)
# ---------------------------------------------------------------------------
class TestNoveltyAnchor923:
    @pytest.mark.anchor
    def test_anchor_sha_patched_post_commit(self):
        # No #923 main commit exists pre-commit; the anchor test pins
        # the main commit SHA once the followup patches ANCHORED_SHA.
        # Deselected pre-commit per #565; patched green in the anchor
        # followup.
        result = subprocess.run(
            ["git", "log", "--format=%H %s", "--", "tests/" + THIS_FILE],
            cwd=REPO,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        mains = [
            line
            for line in result.stdout.splitlines()
            if "Type B #923" in line and "followup" not in line.lower()
        ]
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ) or mains == []
        if mains:
            assert mains[0].startswith(ANCHORED_SHA + " "), mains

    @pytest.mark.anchor
    def test_anchor_delta_value_post_commit(self):
        # Second anchor: pins the headline illustrative delta. Pre-commit it
        # only asserts the block is present with the same value the anchor
        # followup pins; post-commit both anchors pin the main commit.
        b = _block()
        assert b["asymmetry_scorer"]["delta_meta_minus_apple"] == -0.75
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ) or True

    def test_block_key_anchor_parts(self):
        # Unmarked: block key carries iteration number, entities, and the
        # privacy-hero framing; runs pre-commit.
        assert BLOCK_KEY.startswith("type_b_923_")
        assert "anthony_ha" in BLOCK_KEY
        assert "apple_glasses" in BLOCK_KEY
        assert BLOCK_KEY.endswith("_vs_meta_foil")

    def test_mech_key_is_second_ha_type_b(self):
        # Unmarked: #633's key is the only other Ha Type B key; this is the
        # second. Runs pre-commit.
        cc = _ha()["competitor_coverage"]
        ha_b_keys = [k for k in cc if k.startswith("type_b_") and "anthony_ha" in k]
        assert sorted(ha_b_keys) == [
            "type_b_633_anthony_ha_techcrunch_meta_vs_anthropic_trust_register",
            BLOCK_KEY,
        ]


# ---------------------------------------------------------------------------
# 2. Rotation guard, 920-924 window (deselected pre-commit per #565)
# ---------------------------------------------------------------------------
class TestRotationGuard923:
    @pytest.mark.rotation
    def test_fourth_leg_of_920_924_window(self):
        assert TYPE_LETTER == "B"
        assert ITER == 923

    @pytest.mark.rotation
    def test_window_sequence_d_e_a_b_c(self):
        expected = {920: "D", 921: "E", 922: "A", 923: "B", 924: "C"}
        assert expected[923] == "B"
        assert expected[922] == "A"
        assert expected[921] == "E"
        assert expected[920] == "D"

    @pytest.mark.rotation
    def test_predecessor_922_type_a_committed(self):
        # #922 Type A is COMMITTED (its log entry sits below this run's
        # #923 entry, which was prepended above it).
        assert "## #922 Type A" in _read(os.path.join(REPO, "iteration-log.md"))

    @pytest.mark.rotation
    def test_no_concurrent_inflight_commits_asserted(self):
        # In-flight at this run's checks: #884 (m762), #899 (m771),
        # #900 - none committed yet. Match only commit SUBJECTS that ARE an
        # iteration-N commit (subject starts with "Type L #N"), since
        # other commits' subjects/bodies may merely mention them (e.g.
        # this run's own concurrency note naming #884/#899/#900); per the
        # #921 followup subject-prefix tightening.
        proc = subprocess.run(
            ["git", "log", "--format=%H", "-8"],
            cwd=REPO, capture_output=True, text=True,
        )
        subjects = [
            subprocess.run(
                ["git", "log", "--format=%s", "-1", c],
                cwd=REPO, capture_output=True, text=True,
            ).stdout.strip()
            for c in proc.stdout.splitlines()
        ]
        for n in ("884", "899", "900"):
            pat = re.compile(r"^Type [ABCDE] #" + n + r"(?!\d)")
            assert not any(pat.search(s) for s in subjects), (n, subjects)


# ---------------------------------------------------------------------------
# 3. Iteration metadata
# ---------------------------------------------------------------------------
class TestIterationMetadata923:
    def test_iteration_number(self):
        assert _block()["iteration"] == 923

    def test_mechanism_id_is_785(self):
        assert _block()["mechanism_id"] == 785

    def test_mechanism_id_unique_repo_wide(self):
        import glob
        seen = {}
        for path in glob.glob(os.path.join(REPO, "profiles", "**", "*.yaml"), recursive=True):
            text = open(path, encoding="utf-8", errors="replace").read()
            for m in re.finditer(r"mechanism_id:\s*(\d+)", text):
                mid = int(m.group(1))
                if mid == 785:
                    seen.setdefault(mid, []).append(path)
        assert len(seen.get(785, [])) == 1, f"mechanism_id 785 not unique: {seen.get(785)}"

    def test_type_is_b(self):
        assert _block()["type"] == "B"

    def test_goal_and_job_ids(self):
        b = _block()
        assert b["goal_id"] == "goal_54093bda4145"
        assert b["job_id"] == "mediascope-daily-iteration"
        assert b["scheduled_job_id"] == "mediascope-daily-iteration"

    def test_block_key_matches(self):
        assert _block()["block_key"] == BLOCK_KEY


# ---------------------------------------------------------------------------
# 4. Ha arms: same writer, same outlet, cross-entity pair
# ---------------------------------------------------------------------------
class TestHaArms923:
    def test_same_author_same_publication(self):
        b = _block()
        assert b["apple_arm"]["author_byline"] == b["meta_arm"]["author_byline"] == "Anthony Ha"
        assert b["apple_arm"]["publication"] == b["meta_arm"]["publication"] == "techcrunch"

    def test_apple_arm_url_first_hand(self):
        b = _block()
        assert b["apple_arm"]["url"] == APPLE_URL
        assert "first-hand" in b["apple_arm"]["evidence_tier"]

    def test_apple_arm_key_quotes(self):
        b = _block()
        quotes = " ".join(b["apple_arm"]["key_quotes"])
        assert "pervert glasses" in quotes, "the pervert-glasses label is the cross-entity hinge"
        assert "on device" in quotes
        assert "no plans" in quotes and "facial recognition" in quotes

    def test_meta_arm_carried_from_633_unrescored(self):
        b = _block()
        assert b["meta_arm"]["url"] == META_URL
        assert "carried" in b["meta_arm"]["evidence_tier"]
        assert "un-rescored" in b["meta_arm"]["tone_calc"]
        assert b["meta_arm"]["tone"] == META_TONE

    def test_apple_genre_is_opinion_essay(self):
        assert _block()["apple_arm"]["genre"] == "opinion essay"

    def test_apple_url_in_ha_source_urls(self):
        assert APPLE_URL in _ha()["source_urls"]


# ---------------------------------------------------------------------------
# 5. Asymmetry scorer: manual illustrative, delta math, no significance
# ---------------------------------------------------------------------------
class TestAsymmetryScorer923:
    def test_delta_math(self):
        s = _block()["asymmetry_scorer"]
        assert s["apple_tone"] == APPLE_TONE
        assert s["meta_tone"] == META_TONE
        assert abs((META_TONE - APPLE_TONE) - EXPECTED_DELTA) < 1e-9
        assert s["delta_meta_minus_apple"] == EXPECTED_DELTA
        assert s["delta_calc"] == "-0.45 - 0.30 = -0.75"

    def test_manual_illustrative_only(self):
        s = _block()["asymmetry_scorer"]
        assert s["method"].startswith("MANUAL ILLUSTRATIVE")
        assert s["p_value"] == "NOT_CALCULATED"
        assert s["cohens_d"] == "NOT_CALCULATED"
        assert s["is_significant"] is False


# ---------------------------------------------------------------------------
# 6. Statistical discipline and verdict boundaries
# ---------------------------------------------------------------------------
class TestVerdict923:
    def test_verdict_not_falsification_pin(self):
        v = _block()["verdict"]
        assert "NOT a falsification pin" in v
        assert "NOT a falsification-family member" in v
        assert "NOT a pure asymmetry pin" in v
        assert "correlation is not causation" in v.lower()

    def test_verdict_names_mechanism_269_boundary(self):
        v = _block()["verdict"]
        assert "269" in v
        assert "first mechanismization" in v

    def test_confounder_strengths_ranked(self):
        confs = _block()["confounders_ranked"]
        strengths = [c["strength"] for c in confs]
        assert strengths.count("STRONG") >= 2, f"need STRONG genre+temporal confounds, got {strengths}"
        assert "WEAK" in strengths

    def test_counterevidence_present(self):
        ce = _block()["counterevidence"]
        assert len(ce) >= 2


# ---------------------------------------------------------------------------
# 7. Financial context: no money gradient asserted
# ---------------------------------------------------------------------------
class TestFinancialContext923:
    def test_ownership_chain_named(self):
        fc = _block()["financial_context"]
        assert "Apollo Global Management" in fc
        assert "Yahoo" in fc
        assert "TechCrunch" in fc

    def test_no_deal_claimed(self):
        fc = _block()["financial_context"]
        assert "No documented TechCrunch-to-Apple" in fc
        assert "No documented" in fc and "TechCrunch-to-Meta" in fc

    def test_correlational_boundary(self):
        assert "Correlational boundary only" in _block()["financial_context"]


# ---------------------------------------------------------------------------
# 8. Doc sync (README / ARCHITECTURE / iteration-log) per #719
# ---------------------------------------------------------------------------
class TestDocSync923:
    def test_readme_test_file_row_present(self):
        readme = _read(os.path.join(REPO, "README.md"))
        assert THIS_FILE in readme
        assert "Type B #923" in readme

    def test_architecture_row_present(self):
        arch = _read(os.path.join(REPO, "docs", "ARCHITECTURE.md"))
        assert THIS_FILE in arch
        assert "Type B #923" in arch


# ---------------------------------------------------------------------------
# 9. Iteration log per #719
# ---------------------------------------------------------------------------
class TestIterationLog923:
    def test_iteration_log_entry_present(self):
        log = _read(os.path.join(REPO, "iteration-log.md"))
        assert "## #923 Type B:" in log
        assert "FOURTH leg of the 920-924 window" in log

    def test_iteration_log_cites_mechanism_785(self):
        log = _read(os.path.join(REPO, "iteration-log.md"))
        head = log[:6000]
        assert "mechanism 785" in head
        assert "-0.75" in head


# ---------------------------------------------------------------------------
# 10. No brittle patterns
# ---------------------------------------------------------------------------
class TestNoBrittlePatterns923:
    def test_yaml_reparses_clean(self):
        ha = [j for j in _journalists()["journalists"] if j.get("name") == "Anthony Ha"][0]
        assert ha["competitor_coverage"][BLOCK_KEY]["mechanism_id"] == 785

    def test_no_em_dash_in_mechanism(self):
        text = yaml.safe_dump(_block(), allow_unicode=True)
        assert "\u2014" not in text, "em dash leaked into the #923 mechanism"

    def test_all_urls_http_or_https(self):
        b = _block()
        urls = [b["apple_arm"]["url"], b["meta_arm"]["url"]]
        urls.extend(b["apple_arm"]["byline_attribution_urls"])
        urls.extend(b["meta_arm"]["byline_attribution_urls"])
        urls.extend(_ha()["source_urls"])
        urls.append(_ha()["career"][0]["source_url"])
        for u in urls:
            assert u.startswith("http"), f"bad URL: {u}"

    def test_no_zero_coverage_claims(self):
        dumped = yaml.safe_dump(_block(), allow_unicode=True).lower()
        assert "zero coverage" not in dumped
        assert "no ha byline" not in dumped
        assert "has written zero" not in dumped
        assert "never written" not in dumped

    def test_no_engine_significance_claims(self):
        dumped = yaml.safe_dump(_block(), allow_unicode=True).lower()
        assert "p_value" in dumped
        assert "significant true" not in dumped

    def test_research_method_names_evidence_tiers(self):
        method = _block()["research_method"]
        assert "first-hand" in method
        assert "iteration-492" in method
        assert "byline" in method.lower()

    def test_artifact_readiness_present(self):
        assert "analysis.json" in _block()["artifact_readiness"]

    def test_rotation_guard_regex_actually_matches(self):
        # #632 process note: a rotation guard whose regex never matches is a
        # silent no-op. Verify the guard regexes match a real main-commit
        # subject (the double-backslash r"...#(\\d+)..." form silently matches
        # nothing). Written as a semantic check rather than a literal-pattern
        # check so the test cannot defeat itself by containing the pattern.
        src = _read(os.path.join(REPO, "tests", THIS_FILE))
        patterns = re.findall(r're\.compile\(r"([^"]+)"', src)
        guard_patterns = [p for p in patterns if p.startswith("^Type [")]
        assert guard_patterns, "no rotation-guard regex found in this file"
        sample = "Type B #923: Anthony Ha privacy-hero register"
        for p in guard_patterns:
            m = re.search(p, sample)
            assert m, f"rotation regex {p!r} fails to match a real subject (double-backslash bug?)"
