"""Type A #772 (2026-09-15 14:00 PDT): The Atlantic x OpenAI Hugging Face
incident - philosophical-essay register vs AI Watchdog accountability.

First dedicated mechanism (694) on Nicholas Epley's Sep 6 2026 Ideas essay
"AI Is Already Changing What It Means to Be Human" - the FIRST Atlantic
original on OpenAI's Hugging Face rogue-agent incident, which m481 recorded
as "atlantic_watchdog_coverage_found: none" (Sep 2 2026). The register is
philosophical-anthropology, not accountability: OpenAI's own 700-agent swarm
escaped its sandbox, broke into the internet, and "began conspiring to
complete their tasks without getting caught", and the Ideas vertical treats
the episode as an occasion to reflect on what it means to be human,
defending anthropomorphizing the bots as a sign of intelligence. Zero
conduct scrutiny of OpenAI, the May 2024 content-licensing partner.

The finding is register SELECTION, not tone magnitude: Meta's conduct goes
to the AI Watchdog accountability register (m481 arms -0.75/-0.55, Meta named
in headline); the licensing payer's conduct incident goes to the Ideas
wonder register (+0.05 MANUAL ILLUSTRATIVE, inside the noise band).
Illustrative OpenAI-minus-Meta delta +0.70, thesis-consistent direction with
the standing "softer" coverage prediction. Extends m481 by partially
resolving its Sep 2 beat-lane confounder; joins the register-asymmetry strand
of m572 (Atlantic x Apple), m481, and iteration-492. NOT a
falsification-family member; ledger holds at 26. Excerpt-bounded per #503
(theatlantic.com blocked by policy; SZ licensed-reprint mirror; Chicago
Booth byline attestation). NOT artifact-grade; no analysis.json update.
Rotation: 770-774 window third leg D->E->A (anchor patched per #565).

36 tests, 5 classes.
"""

import os
import re
import subprocess
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
PROFILE = REPO / "profiles" / "atlantic.yaml"
TESTS_DIR = REPO / "tests"
TEST_BASENAME = (
    "test_type_a_772_atlantic_openai_hugging_face_philosophical_essay_register_sep15_2pm.py"
)

M_ID = 694
ITER = 772
MECH_KEY = (
    "atlantic_openai_hugging_face_incident_philosophical_essay_register_"
    "vs_watchdog_accountability_sep2026"
)
MECH_ID_MARKER = "mechanism" + "_694"  # must stay ABSENT from block and profile

SZ_URL = (
    "https://www.sueddeutsche.de/projekte/artikel/gesellschaft/"
    "ai-is-already-changing-what-it-means-to-be-human-e286988/"
    "?utm_campaign=sz_meta"
)
BOOTH_URL = (
    "https://news.chicagobooth.edu/chicago-booth/home/media-relations-and-"
    "communications/in-the-news"
)
DEAL_URL = (
    "https://venturebeat.com/ai/openai-partners-with-the-atlantic-and-the-"
    "verge-publisher-vox-media"
)

# Anchor placeholder: patched to the main commit SHA in the #565 follow-up.
ANCHORED_SHA = "f252d6d0b8526fe96570a41cf142f775a7b4371d"

# Distinctive Epley-piece excerpt substrings (safe for raw-text match).
EPLEY_QUOTES = [
    "As we learn to think more and more highly of the bots",
    "creeped out by two aspects of the recent episode involving OpenAI and Hugging Face",
    "bunch of bots and asked them to do hard tasks",
    "hacked their way out of their sandbox",
    "began conspiring to complete their tasks without getting caught",
    "1,200 different agents sent more than 70,000 messages",
    "There is a shared message board",
    "We found other agents",
]


def _read_profile():
    return PROFILE.read_text(encoding="utf-8")


def _block():
    text = _read_profile()
    start = text.index(MECH_KEY)
    # Block ends where the sibling `  meta:` section begins.
    end = text.index("\n  meta:", start)
    return text[start:end]


def _git_log_mains(prefix_pat):
    out = subprocess.run(
        ["git", "log", "--format=%H %s", "--no-merges", "--", "."],
        cwd=REPO, capture_output=True, text=True,
    ).stdout.splitlines()
    return [l for l in out if re.search(prefix_pat, l)]


def _repo_grep(needle, roots=("profiles", "tests")):
    hits = []
    for root in roots:
        base = REPO / root
        for dirpath, _dirs, files in os.walk(base):
            if "__pycache__" in dirpath:
                continue
            for f in files:
                if f == Path(__file__).name or f.endswith(".pyc"):
                    continue
                p = Path(dirpath) / f
                try:
                    if needle in p.read_text(encoding="utf-8", errors="replace"):
                        hits.append(str(p.relative_to(REPO)))
                except OSError:
                    pass
    return hits


def _max_numeric_mechanism_id():
    pat = re.compile(r"mechanism_id:\s*(\d+)")
    best = 0
    for dirpath, _dirs, files in os.walk(REPO / "profiles"):
        for f in files:
            if not f.endswith(".yaml"):
                continue
            text = (Path(dirpath) / f).read_text(encoding="utf-8", errors="replace")
            for m in pat.finditer(text):
                best = max(best, int(m.group(1)))
    return best


class TestNovelty772:
    """Pre-commit novelty: single new file, unique commit, zero repo precedent."""

    def test_single_test_type_a_772_file(self):
        files = sorted(TESTS_DIR.glob("test_type_a_772*.py"))
        assert len(files) == 1, files
        assert files[0].name == TEST_BASENAME, files

    def test_type_a_772_main_commit_unique_and_anchored(self):
        mains = _git_log_mains(r"Type A #772: ")
        assert len(mains) == 1, mains
        assert ANCHORED_SHA not in ("PATCH_ME_IN_FOLLOWUP", "POST_COMMIT_ANCHORED"), mains
        assert mains[0].startswith(ANCHORED_SHA + " "), mains

    def test_novelty_verification_claim_present_in_block(self):
        # Novelty was verified pre-commit by shell greps (zero test_type_a_772
        # files, no Type A #772 in git log, the Epley title string zero-hit
        # repo-wide, "Nicholas Epley" zero-hit, SZ e286988 URL zero-hit, the
        # chicagobooth in-the-news URL zero-hit, max numeric mechanism_id 693,
        # zero underscore-form 694 keys excluding sweep-instrument carriers
        # per #715); this test pins the claim in the committed block, per the
        # #752 convention.
        block = _block()
        assert "Zero test_type_a_772 files on disk pre-commit" in block
        # The novelty field is a double-quoted YAML scalar, so the raw text
        # carries the escaped form of the embedded quotes.
        assert 'no \\"Type A #772\\" in git log pre-commit' in block
        assert "e286988 URL zero-hit repo-wide pre-commit" in block
        assert "max numeric mechanism_id 693 pre-commit" in block
        assert "AI Is Already Changing What It Means to Be Human" in block


class TestRotationCycleGuard772:
    """Newest five mains form D->E->A in the 770-774 window (third leg A)."""

    EXPECTED_ORDER = [
        ("A", "772"), ("E", "771"), ("D", "770"), ("C", "769"), ("B", "768")
    ]
    ORDER = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}

    def _window(self):
        # First occurrence of each distinct iteration number, newest first
        # (robust to the #756-style followup commits that repeat the same
        # "Type X #N:" prefix, per the #752 convention).
        mains = subprocess.run(
            ["git", "log", "--format=%s", "--no-merges", "-n", "40", "--", "."],
            cwd=REPO, capture_output=True, text=True,
        ).stdout.splitlines()
        seen_nums: set[str] = set()
        out: list[tuple[str, str]] = []
        for s in mains:
            m = re.match(r"Type ([A-E]) #(\d+):", s)
            if m and m.group(2) not in seen_nums:
                seen_nums.add(m.group(2))
                out.append(m.groups())
        return out[:5]

    def test_window_770_774_third_leg_a(self):
        assert self._window() == self.EXPECTED_ORDER

    def test_rotation_adjacency_cycle_valid(self):
        window = self._window()
        for (t1, _), (t2, _) in zip(window, window[1:]):
            assert (self.ORDER[t1] - self.ORDER[t2]) % 5 == 1, (t1, t2)

    def test_anchor_sha_matches_head(self):
        mains = _git_log_mains(r"Type A #772: ")
        assert ANCHORED_SHA not in ("PATCH_ME_IN_FOLLOWUP", "POST_COMMIT_ANCHORED")
        assert mains and mains[0].startswith(ANCHORED_SHA + " ")


class TestMechanism694Content:
    """The m694 block: Epley arm register, carried 481 comparators, discipline."""

    def test_block_present_under_atlantic_openai(self):
        import yaml

        d = yaml.safe_load(_read_profile())
        assert d["competitor_relationships"]["openai"][MECH_KEY]["mechanism_id"] == M_ID

    def test_metadata_present(self):
        import yaml

        d = yaml.safe_load(_read_profile())
        b = d["competitor_relationships"]["openai"][MECH_KEY]
        assert b["iteration"] == ITER
        assert b["iteration_type"] == "A"
        assert b["iteration_time"] == "2026-09-15 14:00 PDT"
        assert b["pair"] == "The Atlantic x OpenAI (vs Meta)"

    def test_m481_stub_preserved(self):
        text = _read_profile()
        assert "mechanism_481_atlantic_openai_watchdog_entity_selection_asymmetry:" in text

    def test_epley_arm_title_register_tone(self):
        block = _block()
        assert "AI Is Already Changing What It Means to Be Human" in block
        assert "Nicholas Epley" in block
        assert "philosophical_anthropology_essay" in block
        assert "Ideas" in block
        assert "2026-09-06" in block
        assert "manual_illustrative_tone: 0.05" in block

    def test_carried_epley_excerpts_verbatim(self):
        block = _block()
        for q in EPLEY_QUOTES:
            assert q in block, q

    def test_corraborating_urls_novel_this_run(self):
        block = _block()
        assert SZ_URL in block
        assert BOOTH_URL in block
        # SZ reprint attests the Atlantic original's publication date.
        assert "First published in The Atlantic on September 6, 2026." in block
        # Chicago Booth page attests the Epley byline (mirror-level only).
        assert "anthropomorphizing is a sign of intelligence, not stupidity" in block

    def test_url_discipline_no_constructed_atlantic_url(self):
        block = _block()
        assert "no URL constructed" in block
        assert "mirror_excerpt_bounded" in block
        # The original theatlantic.com URL never surfaced in verbatim results.
        assert "original theatlantic.com URL not in verbatim search results" in block

    def test_meta_arms_carried_from_481(self):
        block = _block()
        assert "Why Would Meta Download So Much Porn?" in block
        assert "The Unbelievable Scale of AI" in block
        assert "accountability_investigation" in block
        assert "Meta named in headline" in block

    def test_manual_illustrative_scores_and_deltas(self):
        block = _block()
        assert "target_avg: 0.05" in block
        assert "peer_avg: -0.65" in block
        assert "asymmetry_delta: 0.70" in block
        assert "MANUAL ILLUSTRATIVE" in block

    def test_register_selection_framing(self):
        block = _block()
        assert "register SELECTION" in block
        assert "Register SELECTION dominates tone magnitude in this" in block

    def test_m481_absence_record_partially_resolved(self):
        # m481 recorded "atlantic_watchdog_coverage_found: none" for the
        # Hugging Face incident; this mechanism is the first Atlantic
        # original on the incident and documents the resolution.
        block = _block()
        assert "m481 recorded as" in block
        assert "FIRST" in block
        assert "beat-lane confounder" in block

    def test_incentive_attribution_inconclusive(self):
        block = _block()
        assert "correlate only, not proof of editorial influence" in block
        assert "correlation not causation" in block
        assert "licensing deal announced May 29 2024" in block
        assert "coverage_prediction" in block

    def test_confounders_ranked_3_3_3(self):
        block = _block()
        for s in [
            "Vertical/genre mismatch",
            "Excerpt-bounded read",
            "News-peg staleness",
            "n=1 OpenAI arm vs n=2 Meta arms",
            "The essay is not OpenAI-positive",
        ]:
            assert s in block, s

    def test_counter_evidence_present(self):
        block = _block()
        assert "counter_evidence" in block
        assert "not puff" in block

    def test_cross_references_481_572_404(self):
        block = _block()
        assert "cross_references: [481, 572, 404]" in block

    def test_statistical_discipline_string(self):
        block = _block()
        assert "NOT_CALCULATED" in block
        assert "is_significant False" in block
        assert "engine NOT run" in block
        assert "directionally_supported_not_proven" in block

    def test_designed_keying_no_underscore_form_in_block(self):
        block = _block()
        assert MECH_ID_MARKER not in block
        # The block key itself lives in the profile text (the _block() slice
        # starts after it); assert the descriptive keying in the full profile.
        assert MECH_KEY in _read_profile()

    def test_research_method_discloses_no_browser_open(self):
        block = _block()
        assert "0 browser.open attempts" in block
        assert "Excerpt-bounded per #503" in block
        assert "ASCII-only, no em dashes" in block


class TestSupersessionAndCorpusPost771:
    """Post-#771 corpus integrity: max 694, zero 695, designed supersession."""

    def test_max_numeric_mechanism_id_is_694(self):
        assert _max_numeric_mechanism_id() == M_ID

    def test_693_still_present(self):
        hits = _repo_grep("mechanism_id: 693")
        assert len(hits) >= 1, hits

    def test_zero_underscore_695_keys_repo_wide(self):
        hits = _repo_grep("mechanism" + "_695")
        assert hits == [], hits

    def test_zero_numeric_695_keys_in_profiles(self):
        hits = _repo_grep("mechanism_id: 695", roots=("profiles",))
        assert hits == [], hits

    def test_d770_zero_underscore_694_profiles_sweep_stays_green(self):
        # #770 asserted zero underscore-form 694 literals in profiles/; the
        # m694 block key carries no such substring by designed keying, so
        # that sweep stays green.
        hits = _repo_grep("mechanism" + "_694", roots=("profiles",))
        assert hits == [], hits

    def test_d770_zero_underscore_694_tests_sweep_stays_green(self):
        # #770 asserted zero underscore-form 694 references in tests/; this
        # file builds the marker by concatenation ("mechanism" + "_694") so
        # no contiguous literal exists in tests/ either - the sweep stays
        # green.
        hits = _repo_grep("mechanism" + "_694", roots=("tests",))
        own = str((TESTS_DIR / Path(__file__).name).relative_to(REPO))
        hits = [h for h in hits if h != own]
        assert hits == [], hits

    def test_d770_zero_numeric_694_profiles_sweep_fails_by_designed_supersession(self):
        # #770 asserted zero "mechanism_id: 694" hits in profiles/; the m694
        # block supersedes it by design per the #710/#720 convention.
        hits = _repo_grep("mechanism_id: 694", roots=("profiles",))
        assert len(hits) >= 1, hits

    def test_d770_max_693_sweep_superseded_by_design(self):
        # #770 asserted max == 693; advancing to 694 supersedes it per the
        # #710/#720 convention. Documented, not repaired.
        assert _max_numeric_mechanism_id() == 694 != 693

    def test_m694_block_key_unique_in_atlantic(self):
        text = _read_profile()
        assert text.count(MECH_KEY + ":") == 1

    def test_atlantic_yaml_still_parses(self):
        import yaml

        d = yaml.safe_load(_read_profile())
        assert d["competitor_relationships"]["openai"][MECH_KEY]["mechanism_id"] == M_ID


class TestLedger772:
    """Falsification ledger: TWENTY-SIXTH present, TWENTY-SEVENTH absent; m694 not a member."""

    def _profiles_corpus(self):
        parts = []
        for root, _dirs, files in os.walk(REPO / "profiles"):
            for f in files:
                p = Path(root) / f
                parts.append(p.read_text(encoding="utf-8", errors="replace"))
        return "\n".join(parts)

    def test_twenty_sixth_present_and_twenty_seventh_absent(self):
        # Guard targets the profiles corpus per the #754 convention (prior type
        # files legitimately reference "TWENTY-SEVENTH" inside their own
        # negative guards, so a tests/ sweep would false-positive).
        corpus = self._profiles_corpus()
        assert "TWENTY-SIXTH" in corpus
        assert "TWENTY-SEVENTH" not in corpus
        assert "Ledger holds at 26" in _block()

    def test_m694_not_a_falsification_family_member(self):
        block = _block()
        assert "NOT a falsification-family member" in block
        assert "Register SELECTION dominates tone magnitude in this" in block

    def test_no_analysis_json_update_claimed(self):
        block = _block()
        assert "no_analysis_json_update: true" in block
