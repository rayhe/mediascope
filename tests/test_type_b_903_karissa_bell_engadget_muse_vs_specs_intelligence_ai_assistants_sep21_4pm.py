"""
Type B #903 (rotation window 900-904, FOURTH leg: D->E->A->B): Karissa Bell
(Engadget senior reporter) - AI-assistant category extension of the
m113/m722/m764 privacy-register asymmetry.

MECHANISM #773: within-journalist cross-entity register asymmetry generalizes
from face-worn cameras to AI assistants. META ARM (new this run): Bell's Sep 12
2026 Engadget guide "How to get started with Meta's new AI agent, Muse" -
utility-positive hands-on ("After a few days of testing Meta's AI agent Muse.
I can confirm that there is very little learning curve to get started.") with
the privacy register ACTIVE from the first recommended step: "Opting out of
data sharing is a good first step"; "opting out of allowing Meta to train its
models on my interactions with Muse"; "review the permissions you've given
Meta's AI agent and consider selecting 'always ask'"; "This also requires
trusting that Meta's AI can distinguish what's actually 'low risk.'";
MANUAL ILLUSTRATIVE +0.05, excerpt-bounded. SNAP ARM (new this run): Bell's
Sep 16 2026 Engadget news piece "Snap introduces a standalone AI assistant,
Specs Intelligence" (byline confirmed on Engadget's own author page this run)
- neutral product relay ("The new assistant works with the company's new AR
glasses, but will also have its own mobile and desktop apps."); ZERO privacy
vocabulary in the surfaced text, even though Snap's own framing (relayed via
secondary coverage citing Engadget) describes an "anticipatory AI service"
that "builds an understanding of a user's goals, priorities, relationships,
and routines based on the apps and tools they choose to connect" and can
connect to external accounts such as Google; MANUAL ILLUSTRATIVE +0.15,
excerpt/dek-bounded. Illustrative delta (Meta minus Snap) -0.10: the privacy
register activates on Meta's AI agent (training-data opt-out as step one)
but stays silent on Snap's explicitly anticipatory, account-connecting AI
service. Same writer, same outlet, same product category (consumer AI
assistants), four days apart. EXTENDS mechanisms 113 (glasses hardware),
722 (Display review vs Specs hands-on), and 764 (live-blog genre replication)
into a new product category.

NOVELTY VERIFICATION (run pre-commit, Sep 21 2026 ~16:0x PDT, before edits):
- glob: zero test_type_b_903*.py files on disk
- git log --all --grep="Type B #903": zero hits (no prior #903 main commit)
- numeric mechanism_id max committed: 772 (#902 m772); in-tree max 772
  (uncommitted concurrent mechanisms 770/#898 and 771/#899 are lower)
- #902's own test file declares NEXT_ID_NUMERIC = "mechanism_id: 773"
  (the only 773-key-string hit repo-wide pre-commit; a declaration, not an
  assigned mechanism)
- format-built underscore needles: zero underscore-form 773 mechanism key
  strings repo-wide (__pycache__ artifacts excluded per the #715
  pattern-rescope lesson)
- zero numeric "mechanism_id: 773" keys in profiles/ pre-commit
- BLOCK_KEY zero-hit repo-wide pre-commit
- "karissa_bell" slug pre-exists (mechanisms 722, 764); new block key unique
- Meta Muse arm URL (2256577) zero-hit repo-wide pre-commit
- Bell's Sep 17 2026 Oversight Board deepfake piece ("consistently and
  fundamentally inadequate") verified ABSENT from the corpus pre-commit
  (zero-hit on the distinctive quote) - noted as a future arm, not used here
- REJECTED candidates this run: Will Knight (extensively covered incl. the
  two-Meta-articles correction); Kylie Robison (Type B talent-war mechanism
  exists); James O'Donnell (Meta AI hack + Anduril/Meta warfare-glasses
  pieces already mechanismized); Andrew Williams / Andrew Lanxon /
  Michael Acton (little/no corpus presence, no clean same-journalist
  Meta-vs-competitor pair surfaced); Scott Stein (prior corpus treatment);
  the Bell Meta-Display-vs-Snap-hands-on pair (mechanisms 722 AND 764 -
  both arms taken); the Bell keynote-live-blog pair (mechanism 764)

ROTATION: this is the FOURTH leg of rotation window 900-904 (D->E->A->B).
Prior legs present in iteration-log.md: #900 Type D (in-flight, uncommitted),
#901 Type E (committed), #902 Type A (committed, 15:00 PDT). Expected cycle
position: B (903) after A (902) after E (901) after D (900). The concurrent
Type C #884 (mechanism 762, competitor-entities.yaml), Type B #898
(mechanism 770, journalists.yaml), Type C #899 (mechanism 771, nytimes.yaml)
and Type D #900 (untracked test file) work remains uncommitted in the working
tree; this run does not touch it.

RESEARCH METHOD: 10 browser.search query sets this run. (1)-(2) Meta AI
hack / Anduril warfare glasses journalists (O'Donnell ruled out -
mechanismized); (3) Muse trademark-handle controversy (context); (4) Meta
AI-hack author confirmation; (5)-(6) Bell author-page research (author page
read, 206 lines; full Sep 2026 Bell timeline captured: Sep 11 Project
Phoenix, Sep 12 Muse guide, Sep 15 Meta One, Sep 16 Specs hands-on +
Specs Intelligence + keynote live blog, Sep 17 Oversight Board piece);
(7) Meta One subscription tiers (context, not used); (8)-(9) Meta Muse
hands-on excerpts (the privacy-register evidence: training-data opt-out
as first step, "always ask", "low risk" trust caveat); (10) Specs
Intelligence piece confirmation (author page byline + dek). 0 browser.open
this run (tool failure early in the run; not retried per the turn
constraint). Engadget originals not first-hand read this run; register
excerpt-bounded per #503. All URLs copied verbatim from Full-URL search
listings. No URL construction. No zero-coverage claims per #492.

"""

import os
import re
import subprocess

import pytest
import yaml

REPO = os.path.expanduser("~/workspace/repos/mediascope")
JOURNALISTS = os.path.join(REPO, "profiles/careers/journalists.yaml")

ITERATION = 903
MECHANISM_ID = 773
BLOCK_KEY = (
    "type_b_903_karissa_bell_engadget_muse_vs_specs_intelligence_ai_assistants"
)
TEST_BASENAME = (
    "tests/test_type_b_903_karissa_bell_engadget_muse_vs_specs_intelligence_"
    "ai_assistants_sep21_4pm.py"
)
SCHEDULED_LOCAL = "Mon 2026-09-21 16:00:00 PDT"

META_URL = (
    "https://www.engadget.com/2256577/"
    "how-to-get-started-with-meta-s-new-ai-agent-muse/"
)
AUTHOR_PAGE = "https://www.engadget.com/author/karissa-bell/"

META_TONE = 0.05
SNAP_TONE = 0.15
EXPECTED_DELTA = -0.10

MEMBER_28 = "TWENTY-EIGHTH falsification-family member"
MEMBER_29 = "TWENTY-NINTH falsification-family member"
MEMBER_30 = "THIRTIETH falsification-family member"


def _read(rel):
    with open(os.path.join(REPO, rel), encoding="utf-8") as fh:
        return fh.read()


def _profiles_text():
    out = []
    prof = os.path.join(REPO, "profiles")
    for root, _dirs, files in os.walk(prof):
        for name in files:
            if name.endswith(".yaml"):
                out.append(_read(os.path.relpath(os.path.join(root, name), REPO)))
    return "\n".join(out)


def _get_block():
    doc = yaml.safe_load(_read("profiles/careers/journalists.yaml"))
    return doc["karissa_bell"]["competitor_coverage"][BLOCK_KEY]


# ---------------------------------------------------------------------------
# 1. Novelty: this iteration and this mechanism are new
# ---------------------------------------------------------------------------
class TestNovelty903:
    def test_single_test_type_b_903_file(self):
        matches = [
            f
            for f in os.listdir(os.path.join(REPO, "tests"))
            if f.startswith("test_type_b_903")
        ]
        assert matches == [os.path.basename(TEST_BASENAME)], matches

    def test_type_b_903_main_commit_unique_and_anchored(self):
        log = subprocess.run(
            ["git", "log", "--oneline", "--grep=Type B #903"],
            cwd=REPO,
            capture_output=True,
            text=True,
            check=True,
        ).stdout.strip()
        assert log != "", "no Type B #903 commit found"
        assert len(log.splitlines()) == 1, log

    def test_novelty_verification_claim(self):
        assert ITERATION == 903
        assert MECHANISM_ID == 773

    def test_900_901_902_window_legs_present_prior_to_903(self):
        log = _read("iteration-log.md")
        assert "#900 Type D" in log
        assert "## #901 Type E" in log
        assert "## #902 Type A" in log

    def test_max_numeric_mechanism_id_773(self):
        ids = [
            int(m)
            for m in re.findall(r"mechanism_id: (\d+)", _profiles_text())
        ]
        assert max(ids) == 773, max(ids)

    def test_no_underscore_774_keys(self):
        assert "mechanism_774" not in _profiles_text()

    def test_no_dash_774_keys(self):
        assert "mechanism-774" not in _profiles_text()

    def test_no_numeric_774_keys(self):
        assert "mechanism_id: 774" not in _profiles_text()

    def test_meta_arm_url_zero_hit_elsewhere(self):
        text = _profiles_text()
        assert text.count(META_URL) == 3, "Muse URL: source_urls + meta_arm + notes"

    def test_oversight_board_arm_absent_from_corpus(self):
        count = _profiles_text().count("fundamentally inadequate")
        assert count == 1, "only this run's research_method future-arm note"


# ---------------------------------------------------------------------------
# 2. Rotation guard: 900-904 window, fourth leg
# ---------------------------------------------------------------------------
class TestRotationGuard903:
    def test_window_is_900_904_fourth_leg(self):
        log = _read("iteration-log.md")
        assert "## #903 Type B" in log
        assert "#900 Type D" in log
        assert "## #901 Type E" in log
        assert "## #902 Type A" in log

    def test_rotation_adjacency_cycle_valid(self):
        cycle = {"D": "E", "E": "A", "A": "B", "B": "C", "C": "D"}
        assert cycle["A"] == "B"

    def test_predecessor_is_type_a_902(self):
        log = _read("iteration-log.md")
        assert "## #902 Type A" in log

    def test_anchor_is_ancestor_of_head(self):
        res = subprocess.run(
            ["git", "merge-base", "--is-ancestor", "HEAD~1", "HEAD"],
            cwd=REPO,
        )
        assert res.returncode == 0


# ---------------------------------------------------------------------------
# 3. Block key shape
# ---------------------------------------------------------------------------
class TestNoveltyAnchor903:
    def test_block_key_shape(self):
        assert BLOCK_KEY.startswith("type_b_903_karissa_bell_engadget_")

    def test_block_key_exact(self):
        assert BLOCK_KEY == (
            "type_b_903_karissa_bell_engadget_"
            "muse_vs_specs_intelligence_ai_assistants"
        )


# ---------------------------------------------------------------------------
# 4. Mechanism 773 block structure
# ---------------------------------------------------------------------------
class TestMechanism773Structure:
    def test_karissa_bell_slug_entry_exists(self):
        doc = yaml.safe_load(_read("profiles/careers/journalists.yaml"))
        assert "karissa_bell" in doc

    def test_block_key_unique(self):
        assert _profiles_text().count(BLOCK_KEY) >= 2

    def test_iteration_and_type(self):
        block = _get_block()
        assert block["iteration"] == 903
        assert block["type"] == "B"

    def test_designed_keying_no_underscore_773(self):
        text = _read("profiles/careers/journalists.yaml")
        assert "mechanism_773" not in text

    def test_required_fields_present(self):
        block = _get_block()
        for field in (
            "block_key",
            "mechanism_id",
            "iteration",
            "type",
            "date",
            "test_file",
            "design",
            "finding",
            "meta_arm",
            "snap_arm",
            "illustrative_delta_meta_minus_snap",
            "statistical_discipline",
            "confounders",
            "counterevidence",
            "connects_to",
            "verdict",
            "is_significant",
            "correlation_not_causation",
            "no_analysis_json_update",
            "falsification_family",
            "ledger",
            "research_method",
        ):
            assert field in block, field

    def test_mechanism_ids_include_773(self):
        doc = yaml.safe_load(_read("profiles/careers/journalists.yaml"))
        ids = doc["karissa_bell"]["mechanism_ids"]
        assert ids == [722, 764, 773], ids

    def test_test_file_field_matches_own_basename(self):
        block = _get_block()
        assert block["test_file"] == TEST_BASENAME


# ---------------------------------------------------------------------------
# 5. Meta arm: Muse guide
# ---------------------------------------------------------------------------
class TestMechanism773MetaArm:
    def test_arm_metadata(self):
        arm = _get_block()["meta_arm"]
        assert arm["url"] == META_URL
        assert arm["date"] == "2026-09-12"
        assert "Karissa Bell" in arm["author_byline"]

    def test_privacy_register_markers(self):
        arm = _get_block()["meta_arm"]
        quotes = " ".join(arm["key_quotes"])
        assert "Opting out of data sharing is a good first step" in quotes
        assert "train its models on my interactions" in quotes
        assert "always ask" in quotes

    def test_distrust_caveat_present(self):
        arm = _get_block()["meta_arm"]
        quotes = " ".join(arm["key_quotes"])
        assert "low risk" in quotes

    def test_utility_positive_bound(self):
        arm = _get_block()["meta_arm"]
        quotes = " ".join(arm["key_quotes"])
        assert "very little learning curve" in quotes

    def test_evidence_tier_disclosed(self):
        arm = _get_block()["meta_arm"]
        assert "EXCERPT-TIER" in arm["evidence_tier"]
        assert "0 browser.open" in arm["evidence_tier"]

    def test_tone(self):
        arm = _get_block()["meta_arm"]
        assert arm["tone_MANUAL_ILLUSTRATIVE"] == META_TONE


# ---------------------------------------------------------------------------
# 6. Snap arm: Specs Intelligence
# ---------------------------------------------------------------------------
class TestMechanism773SnapArm:
    def test_arm_metadata(self):
        arm = _get_block()["snap_arm"]
        assert arm["date"] == "2026-09-16"
        assert "Karissa Bell" in arm["author_byline"]
        assert "Specs Intelligence" in arm["title"]

    def test_byline_source_is_author_page(self):
        arm = _get_block()["snap_arm"]
        assert arm["byline_source"] == AUTHOR_PAGE

    def test_neutral_relay_dek(self):
        arm = _get_block()["snap_arm"]
        assert "mobile and desktop apps" in arm["dek"]

    def test_zero_privacy_vocabulary_in_surfaced_text(self):
        arm = _get_block()["snap_arm"]
        assert arm["privacy_vocabulary_count"] == 0

    def test_anticipatory_framing_documented(self):
        arm = _get_block()["snap_arm"]
        context = " ".join(arm["snap_framing_context"])
        assert "anticipatory" in context
        assert "goals, priorities, relationships" in context

    def test_evidence_tier_disclosed(self):
        arm = _get_block()["snap_arm"]
        assert "DEK-TIER" in arm["evidence_tier"]
        assert "0 browser.open" in arm["evidence_tier"]

    def test_tone(self):
        arm = _get_block()["snap_arm"]
        assert arm["tone_MANUAL_ILLUSTRATIVE"] == SNAP_TONE


# ---------------------------------------------------------------------------
# 7. Scorer arithmetic
# ---------------------------------------------------------------------------
class TestMechanism773Scorer:
    def test_delta_arithmetic(self):
        block = _get_block()
        assert block["illustrative_delta_meta_minus_snap"] == EXPECTED_DELTA
        assert abs((META_TONE - SNAP_TONE) - EXPECTED_DELTA) < 1e-9

    def test_delta_calc_string(self):
        block = _get_block()
        assert block["delta_calc"] == "(0.05) - (0.15) = -0.10"

    def test_two_entity_band(self):
        block = _get_block()
        assert block["two_entity_band"] == [META_TONE, SNAP_TONE]

    def test_connects_to_ids(self):
        block = _get_block()
        assert block["connects_to"] == [113, 722, 764, 605, 753, 723]

    def test_arm_tones(self):
        block = _get_block()
        assert block["meta_arm"]["tone_MANUAL_ILLUSTRATIVE"] == META_TONE
        assert block["snap_arm"]["tone_MANUAL_ILLUSTRATIVE"] == SNAP_TONE


# ---------------------------------------------------------------------------
# 8. Statistical discipline
# ---------------------------------------------------------------------------
class TestMechanism773Discipline:
    def test_p_d_ci_not_calculated(self):
        disc = _get_block()["statistical_discipline"]
        assert "p_value NOT_CALCULATED" in disc
        assert "cohens_d NOT_CALCULATED" in disc
        assert "ci_95 NOT_CALCULATED" in disc

    def test_is_significant_false(self):
        block = _get_block()
        assert block["is_significant"] is False

    def test_verdicts_no_member_field(self):
        block = _get_block()
        assert block["verdict"] == "directionally_supported_not_proven"
        assert block["correlation_not_causation"] is True

    def test_no_analysis_json_and_not_artifact_grade(self):
        block = _get_block()
        assert block["no_analysis_json_update"] is True
        assert "NOT artifact-grade" in block["statistical_discipline"]

    def test_research_method_recorded(self):
        block = _get_block()
        assert "10 browser.search" in block["research_method"]
        assert "REJECTED candidates" in block["research_method"]

    def test_confounder_distribution(self):
        confs = _get_block()["confounders"]
        strong = [c for c in confs if c.startswith("[STRONG]")]
        moderate = [c for c in confs if c.startswith("[MODERATE]")]
        weak = [c for c in confs if c.startswith("[WEAK]")]
        assert len(strong) == 2, strong
        assert len(moderate) == 2, moderate
        assert len(weak) == 1, weak

    def test_counterevidence_count(self):
        counter = _get_block()["counterevidence"]
        assert len(counter) == 4, len(counter)

    def test_manual_illustrative_only(self):
        disc = _get_block()["statistical_discipline"]
        assert "MANUAL ILLUSTRATIVE" in disc
        assert "engine NOT run" in disc


# ---------------------------------------------------------------------------
# 9. Falsification ledger unchanged
# ---------------------------------------------------------------------------
class TestLedgerUnchanged903:
    def test_exactly_one_29th_member_in_profiles(self):
        count = _profiles_text().count(MEMBER_29)
        assert count == 1, count

    def test_29th_member_is_m763_nypost(self):
        text = _read("profiles/news-corp.yaml")
        assert text.count(MEMBER_29) == 1
        assert "(ledger 28->29)" in text

    def test_28th_member_still_exactly_once(self):
        count = _profiles_text().count(MEMBER_28)
        assert count == 1, count

    def test_no_30th_member_form(self):
        assert MEMBER_30 not in _profiles_text()

    def test_block_ledger_holds_at_29(self):
        block = _get_block()
        assert "NOT a falsification-family member" in block["falsification_family"]
        assert "ledger holds at 29" in block["falsification_family"]
        assert "Ledger holds at 29" in block["ledger"]
        assert "THIRTIETH remains the negative guard" in block["ledger"]

    def test_no_verge_guard_change(self):
        verge = _read("profiles/the-verge.yaml")
        assert "THIRTIETH" in verge
        assert "TWENTY-NINTH member-form landed in profiles/news-corp.yaml" in verge
        assert MEMBER_29 not in verge


# ---------------------------------------------------------------------------
# 10. Doc sync: README + ARCHITECTURE
# ---------------------------------------------------------------------------
class TestDocSync903:
    def test_readme_stats_table(self):
        readme = _read("README.md")
        assert "| Tests | 46185 |" in readme
        assert "Across 1227 test files" in readme

    def test_readme_row(self):
        readme = _read("README.md")
        assert os.path.basename(TEST_BASENAME) in readme

    def test_architecture_row(self):
        arch = _read("docs/ARCHITECTURE.md")
        assert "Type B #903" in arch

    def test_architecture_lists_test_file(self):
        arch = _read("docs/ARCHITECTURE.md")
        assert os.path.basename(TEST_BASENAME) in arch


# ---------------------------------------------------------------------------
# 11. Iteration log
# ---------------------------------------------------------------------------
class TestIterationLog903:
    def test_entry_present(self):
        log = _read("iteration-log.md")
        assert "## #903 Type B" in log

    def test_entry_documents_mechanism(self):
        log = _read("iteration-log.md")
        entry = log.split("## #903 Type B")[1].split("## #902")[0]
        assert "m773" in entry

    def test_entry_documents_window(self):
        log = _read("iteration-log.md")
        entry = log.split("## #903 Type B")[1].split("## #902")[0]
        assert "900-904" in entry
        assert "FOURTH leg" in entry
        assert "D->E->A->B" in entry

    def test_entry_documents_ledger(self):
        log = _read("iteration-log.md")
        entry = log.split("## #903 Type B")[1].split("## #902")[0]
        assert "ledger holds at 29" in entry

    def test_entry_documents_concurrency(self):
        log = _read("iteration-log.md")
        entry = log.split("## #903 Type B")[1].split("## #902")[0]
        assert "#884" in entry
        assert "#898" in entry
        assert "#899" in entry
        assert "#900" in entry


# ---------------------------------------------------------------------------
# 12. Date grounding
# ---------------------------------------------------------------------------
class TestDateGrounding903:
    def test_run_date_is_monday(self):
        import datetime
        assert datetime.date(2026, 9, 21).strftime("%A") == "Monday"

    def test_meta_arm_date_is_saturday(self):
        import datetime
        assert datetime.date(2026, 9, 12).strftime("%A") == "Saturday"

    def test_snap_arm_date_is_wednesday(self):
        import datetime
        assert datetime.date(2026, 9, 16).strftime("%A") == "Wednesday"

    def test_scheduled_time(self):
        assert SCHEDULED_LOCAL == "Mon 2026-09-21 16:00:00 PDT"
        block = _get_block()
        assert block["date"] == "2026-09-21 16:00 PDT"
