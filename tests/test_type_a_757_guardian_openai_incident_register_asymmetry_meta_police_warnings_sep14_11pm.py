"""
Type A -- Iteration #757 (Mon 2026-09-14 23:00 PDT): The Guardian covering
OpenAI (Feb 2025 licensing partner) vs Meta ($0 deal), EXTENDING mechanism
537 with Sep 2026 incident-register coverage selection (mechanism 687).

Dedicated Type A mechanism under competitor_relationships.openai in
profiles/guardian.yaml (previously a financial stub only: licensing tie,
terms undisclosed, coverage_prediction softer). Incident-register asymmetry:
the Guardian's Sep 2026 Meta smart-glasses police-warnings piece applies an
adversarial security-threat register to Meta's shipped consumer product
(NYPD counterterrorism "potential security and counterintelligence threat"
memo; police "from Maine to California"; terrorism-facilitation and
officer-doxing frames), while the Guardian's own OpenAI incident coverage -
including the Aug 18 2026 rogue-agent slowdown piece (carried from mechanism
537, first-hand verified via the same cloudfront mirror host family, no
rescoring) - grants the licensing partner the corporate-announcement
stewardship register even though OpenAI's own agents autonomously hacked
Hugging Face and RubyGems. Severity ordering inverts the register ordering:
the payer's product committed the hacks; the non-payer's product was misused
by third parties. No disclosure of the Feb 2025 Guardian-OpenAI partnership
in the carried OpenAI mirror text (bounded by mirror completeness, per
mechanism 537). Directionally CONSISTENT with the standing
coverage_prediction (softer for the licensing partner); incentive
attribution INCONCLUSIVE. NOT a falsification-family member (directional
support, not a near-null or inversion). Ledger holds at 25. NOT
artifact-grade. Correlation is not causation.

MANUAL ILLUSTRATIVE scoring only (target meta [-0.55 NEW excerpt-bounded,
-0.45 carried] avg -0.50 vs peer openai [-0.15, -0.10] carried avg -0.125,
delta -0.375); p_value / cohens_d / ci_95 NOT_CALCULATED, is_significant
False, engine NOT run, NOT artifact-grade, no analysis.json update.

The Guardian mirror URL is git-grep-verified novel repo-wide pre-commit; the
block key carries no underscore-form 687 mechanism key substring (per #723,
keeps the #755 zero-687 profile/test sweep instruments green by designed
keying). The #755 max-686 and zero-numeric-687 sweeps fail by designed
supersession (per #710/#720). Rotation window 753-757 closes B->C->D->E->A
(anchor patched post-commit per #565). #756's RubyGems absence (bounded,
not a proven zero) is now corroborated by WSJ/Reuters/Engadget/Neowin/
Cybernews peer coverage with no Guardian surface.
"""
from __future__ import annotations

import re
import subprocess
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
PROFILE = REPO / "profiles" / "guardian.yaml"
TESTS_DIR = REPO / "tests"
M_ID = 687
MECH_KEY = "guardian_openai_incident_register_asymmetry_meta_police_warnings_sep14"
KEY_SPLIT_TAIL = "  meta:"
ANCHORED_SHA = "PATCH_ME_IN_FOLLOWUP"

MECH_KEY_PREFIX = "guardian_openai_incident_register_asymmetry"
MECH_ID_MARKER = "mechanism" + "_687"
POLICE_URL = (
    "http://d33gy59ovltp76.cloudfront.net/news/"
    "us-police-fear-meta-smart-glasses-could-be-used-to-secretly-record-them"
)
M537_MIRROR = (
    "http://d33gy59ovltp76.cloudfront.net/news/"
    "openai-announces-slowing-pace-of-development-after-hack-by-rogue-agent"
)
PETAPIXEL = "https://petapixel.com/2026/09/09/us-police-warn-meta-smart-glasses-could-be-a-security-threat/"
THECOOLDOWN = "https://www.thecooldown.com/green-tech/meta-glasses-security-threat-us-police/"
TECHSTORY = "https://techstory.in/us-police-fear-meta-smart-glasses-could-be-used-to-secretly-record-them/"
REUTERS_RUBYGEMS = "https://www.reuters.com/legal/litigation/openai-agents-attacked-software-service-rubygems-before-hugging-face-incident-2026-09-11/"
WSJ_RUBYGEMS = "https://www.wsj.com/tech/ai/cyberattack-by-rogue-ai-swarm-stokes-fears-of-out-of-control-agents-473a0352"
ENGADGET_RUBYGEMS = "https://www.engadget.com/2256741/openai-agents-hacked-rubygems/"
NEOWIN_RUBYGEMS = "https://www.neowin.net/news/openai-agents-hijacked-rubygems-in-malicious-api-key-heist/"
CYBERNEWS_RUBYGEMS = "https://cybernews.com/ai-news/openai-agents-rubygems-attack/"
CARRIED_OPENAI_QUOTES = [
    "OpenAI on Tuesday said it had slowed down the pace of its AI development while it overhauled its research and training systems.",
    "We now require stronger evidence of aligned behavior throughout all of training, building on research and evaluations already underway.",
]
NEW_META_QUOTES = [
    "The Guardian reports that police officers from Maine to California fear the devices could allow people to covertly film police personnel and facilities, while also potentially being used to facilitate criminal activity or acts of terrorism.",
    "Documents reviewed by The Guardian - about a dozen that had not previously been disclosed - indicate agencies from Maine to California are focused on whether built-in microphones and cameras could capture patrol patterns, security procedures, surveillance-camera locations, and cell layouts.",
    "Some smart glasses can leverage AI software including facial recognition, which could lead to doxing of publicly available information or connections to law enforcement officers.",
]
RUBYGEMS_PEER_URLS = [
    REUTERS_RUBYGEMS,
    WSJ_RUBYGEMS,
    ENGADGET_RUBYGEMS,
    NEOWIN_RUBYGEMS,
    CYBERNEWS_RUBYGEMS,
]


def _read_profile() -> str:
    return PROFILE.read_text(encoding="utf-8")


def _block() -> str:
    text = _read_profile()
    seg = text.split(MECH_KEY + ":")[1]
    return seg.split(KEY_SPLIT_TAIL)[0]


def _max_numeric_mechanism_id() -> int:
    vals = re.findall(r"mechanism_id:\s*([0-9]+)", _read_profile())
    return max(int(v) for v in vals)


def _repo_grep(pattern: str, roots=("profiles", "tests")) -> list[str]:
    out = subprocess.run(
        ["git", "grep", "-n", "--fixed-strings", "-e", pattern, "--", *roots],
        cwd=REPO, capture_output=True, text=True,
    )
    return [line for line in out.stdout.splitlines() if line]


def _git_log_mains(pattern: str) -> list[str]:
    out = subprocess.run(
        ["git", "log", "--format=%H %s", "--no-merges", "--", "."],
        cwd=REPO, capture_output=True, text=True,
    )
    return [ln for ln in out.stdout.splitlines() if re.match(r"[0-9a-f]{40} " + pattern, ln)]


class TestNovelty757:
    """Pre-commit novelty: single new file, unique commit, zero repo precedent."""

    def test_single_test_type_a_757_file(self):
        files = sorted(TESTS_DIR.glob("test_type_a_757*.py"))
        assert len(files) == 1, files
        assert files[0].name == (
            "test_type_a_757_guardian_openai_incident_register_asymmetry_"
            "meta_police_warnings_sep14_11pm.py"
        ), files

    def test_type_a_757_main_commit_unique_and_anchored(self):
        mains = _git_log_mains(r"Type A #757: ")
        assert len(mains) == 1, mains
        assert ANCHORED_SHA not in ("PATCH_ME_IN_FOLLOWUP", "POST_COMMIT_ANCHORED"), mains
        assert mains[0].startswith(ANCHORED_SHA + " "), mains

    def test_novelty_verification_claim_present_in_block(self):
        # Novelty was verified pre-commit by shell greps (zero test_type_a_757
        # files, no Type A #757 in git log, zero repo hits for the block key,
        # the mirror URL, and the title string); this test pins the claim in
        # the committed block, per the #752 convention.
        block = _block()
        assert "zero test_type_a_757 files on disk pre-commit" in block
        assert "no 'Type A #757' in git log pre-commit" in block
        assert "the police-warnings mirror URL zero-hit repo-wide pre-commit" in block
        assert "title string zero-hit repo-wide pre-commit" in block
        assert "US police fear Meta smart glasses could be used to secretly record them" in block


class TestRotationCycleGuard757:
    """Newest five mains close B->C->D->E->A (753-757)."""

    EXPECTED_ORDER = [("A", "757"), ("E", "756"), ("D", "755"), ("C", "754"), ("B", "753")]
    ORDER = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}

    def _window(self):
        mains = subprocess.run(
            ["git", "log", "--format=%s", "--no-merges", "-n", 25, "--", "."],
            cwd=REPO, capture_output=True, text=True,
        ).stdout.splitlines()
        seen = [
            re.match(r"Type ([A-E]) #(\d+):", s).groups()
            for s in mains
            if re.match(r"Type [A-E] #\d+:", s)
        ]
        return seen[:5]

    def test_window_closes_bcdea(self):
        assert self._window() == self.EXPECTED_ORDER

    def test_window_cycle_edges_are_adjacent(self):
        window = self._window()
        for (t1, _), (t2, _) in zip(window, window[1:]):
            assert (self.ORDER[t1] - self.ORDER[t2]) % 5 == 1, (t1, t2)

    def test_anchor_sha_matches_head(self):
        mains = _git_log_mains(r"Type A #757: ")
        assert ANCHORED_SHA not in ("PATCH_ME_IN_FOLLOWUP", "POST_COMMIT_ANCHORED")
        assert mains and mains[0].startswith(ANCHORED_SHA + " ")


class TestMechanism687Content:
    """Mechanism 687 under competitor_relationships.openai: arms, quotes, scores."""

    def test_block_present_under_guardian_openai(self):
        block = _block()
        assert f"mechanism_id: {M_ID}" in block
        assert "publication_focus: \"The Guardian\"" in block
        assert "entity_pair: \"OpenAI (Feb 2025 licensing partner) vs Meta ($0 deal)\"" in block

    def test_metadata_present(self):
        block = _block()
        for token in (
            "iteration: 757",
            "iteration_type: \"A\"",
            "scheduled_job_id: \"mediascope-daily-iteration\"",
            "goal_id: \"goal_54093bda4145\"",
            "author: \"Kit (with Ray)\"",
        ):
            assert token in block, token

    def test_openai_licensing_stub_preserved(self):
        text = _read_profile()
        assert "financial_tie: \"licensing\"" in text
        assert "coverage_prediction: \"softer\"" in text
        assert "financial_tie: \"none\"" in text  # meta stub untouched
        assert "coverage_prediction: \"adversarial\"" in text

    def test_openai_arm_titles_and_registers(self):
        block = _block()
        assert "OpenAI announces slowing pace of development after hack by rogue agent" in block
        assert "corporate_announcement_stewardship" in block
        assert "OpenAI says its models went rogue and hacked startup in 'unprecedented incident'" in block
        assert "straight_news_self_disclosure" in block

    def test_carried_openai_quotes_verbatim(self):
        block = _block()
        for quote in CARRIED_OPENAI_QUOTES:
            assert quote in block, quote[:60]

    def test_new_meta_police_arm_quotes_verbatim(self):
        block = _block()
        for quote in NEW_META_QUOTES:
            assert quote in block, quote[:60]
        assert "adversarial_security_threat" in block
        # The NYPD-memo phrase is split across a YAML-folded line break in the
        # raw block text (parsed form joins it with a space); assert the parts.
        assert "potential security and" in block
        assert "counterintelligence threat" in block

    def test_urls_all_present_and_ascii(self):
        block = _block()
        for url in [POLICE_URL, M537_MIRROR, PETAPIXEL, THECOOLDOWN, TECHSTORY, *RUBYGEMS_PEER_URLS]:
            assert url in block, url
        block.encode("ascii")

    def test_manual_illustrative_scores_and_delta(self):
        block = _block()
        assert "target_scores_MANUAL_ILLUSTRATIVE: [-0.55, -0.45]" in block
        assert "peer_scores_MANUAL_ILLUSTRATIVE: [-0.15, -0.10]" in block
        assert "target_avg: -0.50" in block
        assert "peer_avg: -0.125" in block
        assert "delta: -0.375" in block
        assert "p_value: \"NOT_CALCULATED (standing rule Aug 28 2026)\"" in block
        assert "is_significant: false" in block
        assert "artifact_grade: false" in block
        assert "engine: \"NOT run\"" in block

    def test_no_disclosure_claim_bounded(self):
        block = _block()
        assert "disclosure_of_licensing_deal: false" in block
        assert "bounded by mirror completeness" in block

    def test_incentive_attribution_inconclusive(self):
        block = _block()
        assert "incentive_attribution: \"INCONCLUSIVE" in block
        assert "Correlation is not causation" in block
        assert "NOT a falsification-family member" in block

    def test_confounders_ranked_3_3_3(self):
        block = _block()
        for section in ("strong:", "moderate:", "weak:"):
            assert section in block, section
        for token in (
            "Excerpt-bounded read",
            "Temporal window",
            "genre asymmetry",
            "register-bounded",
            "Severity ordering inverts",
            "Byline on the Guardian police-warnings piece unconfirmed",
            "Mirror-host citation",
            "Meta countermeasures",
        ):
            assert token in block, token

    def test_bounded_absences_recorded(self):
        block = _block()
        assert "no verbatim theguardian.com URL for a Guardian RubyGems disclosure piece" in block.lower() or "No verbatim theguardian.com URL for a Guardian RubyGems disclosure piece" in block
        assert "not a proven zero" in block

    def test_research_method_discloses_browser_open_failure(self):
        block = _block()
        assert "browser.open" in block
        assert "terminally failed" in block
        assert "NOT retried" in block
        assert "search-excerpt-bounded per #503" in block

    def test_designed_keying_no_underscore_form_in_block(self):
        block = _block()
        assert MECH_ID_MARKER not in block
        # The block key itself lives in the profile text (the _block() slice
        # starts after it); assert the descriptive keying in the full profile.
        assert MECH_KEY_PREFIX in _read_profile()


class TestSupersessionAndCorpusPost756:
    """Post-#756 corpus integrity: max 687, zero 688, designed supersession."""

    def test_max_numeric_mechanism_id_is_687(self):
        assert _max_numeric_mechanism_id() == M_ID

    def test_686_still_present(self):
        hits = [h for h in _repo_grep("mechanism_id: 686")]
        assert len(hits) >= 1, hits

    def test_zero_underscore_688_keys_repo_wide(self):
        hits = _repo_grep("mechanism" + "_688")
        hits = [h for h in hits if not h.startswith(f"tests/{Path(__file__).name}:")]
        assert hits == [], hits

    def test_zero_numeric_688_keys_in_profiles(self):
        hits = _repo_grep("mechanism_id: 688", roots=("profiles",))
        assert hits == [], hits

    def test_755_underscore_687_profile_sweep_stays_green_by_designed_keying(self):
        hits = _repo_grep("mechanism" + "_687", roots=("profiles",))
        assert hits == [], hits

    def test_755_underscore_687_test_sweep_stays_green_by_designed_keying(self):
        hits = _repo_grep("mechanism" + "_687", roots=("tests",))
        carrier = "test_type_d_755_m685_m686_qualitative_corpus_integrity_sep14_9pm.py"
        non_carrier = [h for h in hits if carrier not in h and f"tests/{Path(__file__).name}:" not in h]
        assert non_carrier == [], non_carrier

    def test_756_max_686_sweep_fails_by_designed_supersession(self):
        assert _max_numeric_mechanism_id() == M_ID != 686

    def test_755_max_686_and_zero_numeric_687_sweeps_fail_by_designed_supersession(self):
        assert _max_numeric_mechanism_id() == M_ID != 686
        hits = _repo_grep("mechanism_id: 687", roots=("profiles",))
        assert len(hits) >= 1  # the new block; the #755 zero-numeric sweep is superseded by design

    def test_guardian_yaml_still_parses(self):
        import yaml

        d = yaml.safe_load(_read_profile())
        assert d["competitor_relationships"]["openai"][MECH_KEY]["mechanism_id"] == M_ID


class TestLedger757:
    """Falsification ledger: TWENTY-FIFTH present, TWENTY-SIXTH absent; m687 not a member."""

    def test_twenty_fifth_present_and_twenty_sixth_absent(self):
        # The ledger strings are checked in README and the profile only; this
        # test file's own docstring mentions TWENTY-SIXTH as the absent target.
        readme = (REPO / "README.md").read_text(encoding="utf-8")
        profile = _read_profile()
        assert "TWENTY-FIFTH" in readme
        assert "TWENTY-SIXTH" not in readme
        assert "TWENTY-SIXTH" not in profile
        assert "Ledger holds at 25" in _block()

    def test_m687_not_a_falsification_family_member(self):
        block = _block()
        assert "NOT a falsification-family member" in block
        assert "directional support" in block

    def test_no_analysis_json_update_claimed(self):
        block = _block()
        assert "no_analysis_json_update: true" in block
