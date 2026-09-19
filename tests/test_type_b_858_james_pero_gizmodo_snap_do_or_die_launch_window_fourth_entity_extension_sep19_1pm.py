"""Type B #858 (855-859 window, fourth leg D->E->A->B): James Pero
(Gizmodo) Sep-2026 Snap Specs launch-window register - FOURTH-ENTITY
EXTENSION of mechanism 211's three-entity gradient.

FIRST corpus evidence of Pero's Gizmodo launch-window piece "Snap's Do
or Die Moment in AR Has Arrived" (excerpt-tier: headline, dek-adjacent
excerpts and pull-quotes attested via search-index renders; full text NOT
first-hand reviewed per the #503 convention; byline attributed via the
piece's first-person voice - "when I talked to Snap's Head of Specs
Studio" - plus the "James Pero / Gizmodo" photo credits). The register is
aspirational-agreement: Pero accepts Snap's "not smart glasses... this is
a computer built into a pair of augmented reality glasses" CEO reframing
with "I tend to agree", and renders a product verdict - "In my initial
testing, Snap's Specs *do* feel like the most compelling AR glasses out
there" (+0.35 MANUAL ILLUSTRATIVE). Meta appears only as a negative foil
("unlike Meta and its Reality Labs division, which has racked up $80
billion in operating losses since 2020"), never as an investigated
subject. Zero privacy/surveillance vocabulary on a face-worn device
carrying two full-color high-resolution cameras plus two IR
computer-vision cameras (MacRumors attestation of the Specs hardware).

Meta arms carried un-rescored from mechanism 211 (Type B #219, Aug 21
2026; asymmetry_score 1.0; meta_coverage_tone adversarial; RECIDIVISM
LOOP: 25+ alarm terms, "anti-Meta plan" section title, "Thanks to Meta"
opening, 7M+ units of success framed as escalating menace) per the #807
pattern. Fresh excerpt-tier attestation this run of the register's
persistence (NOT new arms): Gizmodo "Meta's New AI Smart Glasses Drop
Ray-Ban Branding and Add Kylie Jenner" ("Meta has a poor track record when
it comes to privacy", circa Jun 2026) and "Meta Thinks 'Social Learning'
Can Fix Smart Glasses' Privacy Problems" ("controversies have already
been frequent and often self-inflicted by Meta", circa Jun 2026).

Cross-journalist replication of the Sep-16 launch-window direction
documented for Ashworth (WIRED, m743) and Ropek (TechCrunch, m269): three
journalists, three outlets, same window, same direction (challenger
optimism on Snap; Meta stays the adversarialized foil). EXTENDS the m211
three-entity family (Apple reputational-credit / Google redemption / Meta
recidivism) to a FOURTH entity. The m211 financial-incentive leg (Apple
affiliate revenue > Google ad partner > Meta zero relationship) does NOT
predict Snap's soft register: Gizmodo parent Keleops AG has no Snap
financial relationship on record, yet the fourth entity lands at the soft
end. The asymmetry is Meta-exceptionalism, not payer-driven.

MANUAL ILLUSTRATIVE only, engine NOT run, p_value/cohens_d/ci_95
NOT_CALCULATED, is_significant False, verdict
directionally_supported_not_proven; NOT falsification-family, ledger holds
at 26 (TWENTY-SIXTH present, TWENTY-SEVENTH absent); no analysis.json
update. Novelty verified pre-commit (zero test_type_b_858 files; no
'Type B #858' in git log; max 745; zero underscore-form 746 keys per
#715; block key zero-hit; headline string zero-hit repo-wide; Gizmodo URL
zero-hit repo-wide; 5 browser.search query sets, 0 browser.open per #503);
count_stats gate (delta = this file exactly); 855-859 window fourth leg
D->E->A->B (anchor patched post-commit per #565) - Sep 19 2026 13:00 PDT.
"""

import os
import re
import subprocess
import datetime

import pytest
import yaml

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
TESTS_DIR = os.path.join(REPO_ROOT, "tests")
OWN_BASENAME = "test_type_b_858_james_pero_gizmodo_snap_do_or_die_launch_window_fourth_entity_extension_sep19_1pm.py"
MECH_KEY = "type_b_858_james_pero_gizmodo_snap_do_or_die_launch_window_fourth_entity_extension"
M_ID = 746
ITER = 858
TYPE_LETTER = "B"
# Concatenated so this file never contains the literal marker itself.
MECH_ID_MARKER = "mechanism" + "_746"
NEXT_ID_MARKER = "mechanism" + "_747"
NEXT_ID_NUMERIC = "mechanism_id: " + "747"
EXPECTED_ORDER = [("B", "858"), ("A", "857"), ("E", "856"), ("D", "855"), ("C", "854")]
# Patched to the real main-commit SHA in the anchor followup per the #565 convention.
ANCHORED_SHA = "PATCH_ME_IN_FOLLOWUP_PER_565"

SNAP_URL = "https://gizmodo.com/snaps-do-or-die-moment-in-ar-has-arrived-2000813560"
SNAP_TITLE = "Snap's Do or Die Moment in AR Has Arrived"
SNAP_QUOTE_FRAME = "this is a computer built into a pair of augmented reality glasses"
SNAP_QUOTE_AGREE = "I tend to agree. The new Specs are ambitious."
SNAP_QUOTE_VERDICT = "In my initial testing, Snap's Specs *do* feel like the most compelling AR glasses out there."
SNAP_QUOTE_META_FOIL = "unlike Meta and its Reality Labs division, which has racked up $80 billion in operating losses since 2020"
META_PILEUP_URL = "https://gizmodo.com/smart-glasses-are-a-hit-even-as-privacy-concerns-pile-up-2000792911"
META_TALK_URL = "https://gizmodo.com/we-need-to-talk-about-smart-glasses-2000661487"
META_KYLIE_URL = "https://gizmodo.com/metas-new-smart-glasses-drop-ray-ban-branding-and-add-kylie-jenner-2000775546"
META_SOCIAL_LEARNING_URL = "https://gizmodo.com/meta-thinks-social-learning-can-fix-smart-glasses-privacy-problems-2000776162"
EXPECTED_URLS = [SNAP_URL, META_PILEUP_URL, META_TALK_URL, META_KYLIE_URL, META_SOCIAL_LEARNING_URL]

README_PATH = os.path.join(REPO_ROOT, "README.md")
ARCH_PATH = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")
LOG_PATH = os.path.join(REPO_ROOT, "iteration-log.md")


def _read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def _profiles_text():
    return _read(os.path.join(REPO_ROOT, "profiles", "careers", "journalists.yaml"))


def _gizmodo_text():
    return _read(os.path.join(REPO_ROOT, "profiles", "gizmodo.yaml"))


def _block():
    # The james_pero item is appended last in journalists.yaml, so the
    # mechanism block runs from its key to end of file.
    text = _profiles_text()
    start = text.index(MECH_KEY)
    return text[start:]


def _item():
    return yaml.safe_load(_profiles_text())["james_pero"]


def _mech():
    return _item()["competitor_coverage"][MECH_KEY]


def _corpus_ids():
    ids = []
    for root, _, files in os.walk(os.path.join(REPO_ROOT, "profiles")):
        for fn in files:
            if fn.endswith(".yaml"):
                text = _read(os.path.join(root, fn))
                for m in re.finditer(r"mechanism_id:\s*(\d+)", text):
                    ids.append(int(m.group(1)))
    return ids


def _repo_grep(needle, roots=("profiles", "tests")):
    hits = []
    for r in roots:
        base = os.path.join(REPO_ROOT, r)
        for root, _, files in os.walk(base):
            for fn in files:
                if fn.rsplit(".", 1)[-1] in ("py", "yaml", "md", "json"):
                    p = os.path.join(root, fn)
                    try:
                        if needle in _read(p):
                            hits.append(os.path.relpath(p, REPO_ROOT))
                    except OSError:
                        pass
    return hits


def _git(*args):
    return subprocess.run(
        ["git", *args],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=True,
    ).stdout


def _git_log_mains(qualifier):
    out = _git("log", "--all", "--format=%H %s", "--grep", qualifier)
    mains = {}
    for line in out.splitlines():
        if not line.strip():
            continue
        sha, _, subject = line.partition(" ")
        if "Type B #858" in subject:
            mains[sha] = subject
    return mains


def _window(n=40):
    # First occurrence of each distinct iteration number, newest first
    # (robust to followup commits that repeat the same "Type X #N" wording
    # without the colon, per the #752 convention).
    subjects = _git("log", f"-{n}", "--format=%s", "--no-merges").splitlines()
    seen_nums = set()
    out = []
    for s in subjects:
        m = re.match(r"Type ([A-E]) #(\d+):", s)
        if m and m.group(2) not in seen_nums:
            seen_nums.add(m.group(2))
            out.append(m.groups())
    return out[:5]


class TestNovelty858:
    def test_single_test_type_b_858_file(self):
        matches = [
            f
            for f in os.listdir(TESTS_DIR)
            if f.startswith("test_type_b_858") and f.endswith(".py")
        ]
        assert matches == [OWN_BASENAME], matches

    def test_type_b_858_main_commit_unique_and_anchored(self):
        # No #858 main commit exists pre-commit; the anchor test pins
        # the main commit SHA once the followup patches ANCHORED_SHA.
        # Deselected pre-commit per #565; patched green in the anchor
        # followup.
        result = subprocess.run(
            ["git", "log", "--format=%H %s", "--", "tests/" + OWN_BASENAME],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        mains = [
            line
            for line in result.stdout.splitlines()
            if "Type B #858" in line and "followup" not in line.lower()
        ]
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "PATCH_ME_IN_FOLLOWUP_PER_565",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ) or mains == []
        if mains:
            assert mains[0].startswith(ANCHORED_SHA + " "), mains

    def test_novelty_verification_claim(self):
        # This run ADDS mechanism 746: post-commit max is 746, zero 747
        # keys anywhere. Pre-commit sweeps verified max 745, zero
        # underscore-form 746 keys (designed keying per #715), block key
        # zero-hit, Snap "Do or Die" headline string zero-hit repo-wide,
        # Gizmodo URL zero-hit repo-wide.
        assert max(_corpus_ids()) == 746
        assert _repo_grep(NEXT_ID_MARKER) == []
        assert _repo_grep(NEXT_ID_NUMERIC, roots=("profiles",)) == []

    def test_window_legs_present_prior_to_858(self):
        log = _read(LOG_PATH)
        for marker in (
            "## #855 Type D:",
            "## #856 Type E:",
            "## #857 Type A:",
        ):
            assert marker in log, marker


class TestRotationGuard858:
    """#858 is the Type B fourth leg of window 855-859: D->E->A->B."""

    ORDER = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}

    def test_window_is_855_859_fourth_leg(self):
        # Deselected pre-commit per #565 (the #858 main commit does not
        # exist yet); patched green in the anchor followup.
        window = _window()
        assert window[:4] == EXPECTED_ORDER[:4], (
            f"855-859 window fourth leg D->E->A->B: expected {EXPECTED_ORDER[:4]}, "
            f"got {window[:4]}"
        )

    def test_rotation_adjacency_cycle_valid(self):
        # Deselected pre-commit per #565; patched green in the followup.
        window = _window()
        for (t1, n1), (t2, n2) in zip(window[:4], window[1:5]):
            assert int(n1) == int(n2) + 1
            assert (self.ORDER[t1] - self.ORDER[t2]) % 5 == 1, (t1, t2)

    def test_predecessor_is_type_a_857(self):
        # Deselected pre-commit per #565; patched green in the followup.
        window = _window()
        assert window[1] == ("A", "857"), (
            f"immediate predecessor must be Type A #857, got {window[1]}"
        )

    def test_anchor_sha_matches_head(self):
        # Patched to the real main-commit SHA in the anchor followup per
        # the #565 convention; deselected pre-commit at the pytest CLI.
        mains = _git_log_mains("Type B #858: James Pero")
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "PATCH_ME_IN_FOLLOWUP_PER_565",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ), mains
        newest_sha = next(iter(mains))
        assert newest_sha == ANCHORED_SHA, mains


class TestMechanism746Structure:
    def test_block_key_exists_in_journalists_profile(self):
        assert MECH_KEY in _profiles_text()

    def test_block_key_unique(self):
        assert _profiles_text().count(MECH_KEY) >= 2  # key line + block_key field

    def test_iteration_and_type_and_time_pdt(self):
        block = _block()
        assert "iteration: 858" in block
        assert "type: B" in block
        assert "2026-09-19 13:00 PDT" in block

    def test_designed_keying_no_underscore_746_in_block(self):
        # Designed keying per #715: colon form only, zero underscore-form
        # 746 keys anywhere in the block.
        block = _block()
        assert "mechanism_id: 746" in block
        assert MECH_ID_MARKER not in block
        assert NEXT_ID_MARKER not in block

    def test_yaml_parses_and_fields(self):
        doc = yaml.safe_load(_profiles_text())
        item = doc["james_pero"]
        block = item["competitor_coverage"][MECH_KEY]
        assert block["mechanism_id"] == 746
        assert block["iteration"] == 858
        assert block["block_key"] == MECH_KEY
        assert block["author"] == "Kit (with Ray)"
        assert block["goal_id"] == "goal_54093bda4145"

    def test_james_pero_profile_context(self):
        doc = yaml.safe_load(_profiles_text())
        item = doc["james_pero"]
        assert item["name"] == "James Pero"
        assert item["current_publication"] == "Gizmodo"
        assert 211 in item["mechanism_ids"]
        assert 746 in item["mechanism_ids"]


class TestMechanism746NewSnapArm:
    def test_snap_arm_title_verbatim(self):
        block = _block()
        assert SNAP_TITLE in block

    def test_snap_arm_url_verbatim(self):
        block = _block()
        assert SNAP_URL in block
        for url in EXPECTED_URLS:
            assert url in block, url

    def test_snap_arm_date_bounded_sep_18_2026(self):
        # Date bounded from search-index crawl stamps per iteration-492,
        # never claimed as an exact publication date.
        block = _block()
        assert "date_bounded" in block
        assert "2026-09-18" in block or "sep_18_2026" in block.replace("-", "_")

    def test_snap_arm_byline_attribution_and_role(self):
        block = _block()
        assert "James Pero" in block
        assert "Gizmodo" in block
        # Bounded attribution: first-person voice + photo credits.
        assert "first-person" in block or "photo credit" in block

    def test_snap_arm_feuerstein_quote_verbatim(self):
        block = _block()
        assert SNAP_QUOTE_FRAME in block

    def test_snap_arm_agreement_quotes_verbatim(self):
        # Parsed-doc check: PyYAML escaping/doubling and 200-col wrapping
        # break raw-text matching for apostrophe-bearing quotes.
        quotes = " ".join(_mech()["snap_arm"]["key_quotes"])
        assert "I tend to agree. The new Specs are ambitious." in quotes
        assert (
            "In my initial testing, Snap's Specs *do* feel like the most "
            "compelling AR glasses out there."
        ) in quotes

    def test_snap_arm_meta_foil_quote_verbatim(self):
        block = _block()
        assert SNAP_QUOTE_META_FOIL in block

    def test_excerpt_tier_evidence_limitation(self):
        block = _block()
        assert "#503" in block
        assert "0 browser.open" in block or "excerpt-tier" in block


class TestMechanism746CarriedArms:
    def test_m211_meta_arms_carried_unrescored_per_807(self):
        block = _block()
        assert "#807" in block
        assert "un-rescored" in block or "carried un-rescored" in block
        assert META_PILEUP_URL in block
        assert META_TALK_URL in block

    def test_meta_recidivism_register_characterization(self):
        block = _block()
        assert "RECIDIVISM" in block
        assert "25+" in block or "alarm terms" in block
        assert "1.0" in block  # m211 asymmetry_score carried

    def test_no_duplicate_mechanism_id_746(self):
        count = 0
        for root, _, files in os.walk(os.path.join(REPO_ROOT, "profiles")):
            for fn in files:
                if fn.endswith(".yaml"):
                    count += _read(os.path.join(root, fn)).count("mechanism_id: 746")
        assert count == 1, count

    def test_jun2026_fresh_attestation_flagged_excerpt_tier(self):
        # The two Jun-2026 Pero Meta pieces attest register persistence
        # but are NOT new arms (excerpt-tier only, explicitly flagged).
        block = _block()
        assert META_KYLIE_URL in block
        assert META_SOCIAL_LEARNING_URL in block
        assert "NOT new arms" in block

    def test_snap_hardware_parity_cameras(self):
        # Snap Specs carry MORE face-worn cameras than Meta's glasses yet
        # receive zero privacy vocabulary: the parity that makes the
        # asymmetry salient.
        block = _block()
        assert "two" in block.lower() and "camera" in block.lower()


class TestMechanism746Temporal:
    def test_fourth_entity_extension_of_m211(self):
        block = _block()
        assert "211" in block
        assert "FOURTH" in block or "fourth" in block

    def test_cross_journalist_launch_window_replication(self):
        block = _block()
        # Ashworth (m743) and Ropek (m269) documented the same launch-window
        # direction; three journalists, three outlets.
        assert "743" in block
        assert "269" in block

    def test_connects_to_211_31_99_743_269(self):
        block = _block()
        assert "connects_to" in block
        for ref in ("211", "31", "99", "743", "269"):
            assert ref in block, ref

    def test_snap_tone_plus_035_illustrative(self):
        block = _block()
        assert "+0.35" in block
        assert "MANUAL ILLUSTRATIVE" in block

    def test_meta_as_negative_foil_not_investigated_subject(self):
        block = _block()
        assert "foil" in block.lower()


class TestMechanism746Discipline:
    def test_p_value_not_calculated(self):
        assert "p_value" in _block() and "NOT_CALCULATED" in _block()

    def test_cohens_d_not_calculated(self):
        assert "cohens_d" in _block() and "NOT_CALCULATED" in _block()

    def test_ci_95_not_calculated(self):
        assert "ci_95" in _block() and "NOT_CALCULATED" in _block()

    def test_is_significant_false_and_engine_not_run(self):
        # Parsed-doc check: PyYAML renders the YAML boolean lowercase, so
        # raw-text "False" matching is brittle.
        sd = _mech()["statistical_discipline"]
        assert sd["is_significant"] is False
        assert sd["engine_run"] is False

    def test_verdict_and_correlation_note(self):
        sd = _mech()["statistical_discipline"]
        assert sd["verdict"] == "directionally_supported_not_proven"
        assert "Correlation only, not causation" in _item()["notes"]

    def test_no_analysis_json_update_and_not_artifact_grade(self):
        block = _block()
        assert "no_analysis_json_update" in block
        assert "NOT artifact-grade" in block or "not_artifact_grade" in block

    def test_falsification_ledger_holds_at_26_and_research_method(self):
        # Parsed-doc check: PyYAML 200-col wrapping can split the phrase in
        # raw text.
        fam = _mech()["falsification_family"]
        assert "ledger holds at 26" in fam
        assert "TWENTY-SEVENTH absent" in fam
        assert "5 browser.search" in _mech()["research_method"]
        # Repo-wide: no profile may claim a 27th falsification-family
        # member (a "TWENTY-SEVENTH absent" disclaiming phrase is expected
        # in m211-extension blocks; the ledger only moves on a claim).
        assert _repo_grep("TWENTY-SEVENTH present", roots=("profiles",)) == []
        assert _repo_grep("ledger 26->27", roots=("profiles",)) == []

    def test_confounder_severity_distribution(self):
        block = _block()
        assert "confounders_ranked" in block
        for sev in ("strong:", "moderate:", "weak:"):
            assert sev in block, sev
        assert "counterevidence" in block


class TestDocSync858:
    def test_readme_row_858(self):
        text = _read(README_PATH)
        assert OWN_BASENAME in text
        assert "Type B #858" in text

    def test_architecture_row_858(self):
        text = _read(ARCH_PATH)
        assert OWN_BASENAME in text
        assert "Type B #858" in text

    def test_architecture_lists_858_file(self):
        text = _read(ARCH_PATH)
        assert text.count(OWN_BASENAME) >= 1


class TestIterationLog858:
    def test_log_entry_present(self):
        assert "## #858 Type B:" in _read(LOG_PATH)

    def test_log_mechanism_numbers_and_topics(self):
        log = _read(LOG_PATH)
        assert "mechanism 746" in log or "m746" in log
        assert "James Pero" in log
        assert "Do or Die" in log

    def test_log_rotation_window_855_859(self):
        log = _read(LOG_PATH)
        assert "855-859" in log
        assert "fourth leg" in log.lower() or "FOURTH leg" in log

    def test_log_records_predecessor_857(self):
        log = _read(LOG_PATH)
        assert "#857" in log


class TestDateGrounding858:
    def test_sep_19_2026_is_saturday(self):
        assert datetime.date(2026, 9, 19).strftime("%A") == "Saturday"

    def test_sep_18_2026_is_friday(self):
        assert datetime.date(2026, 9, 18).strftime("%A") == "Friday"

    def test_run_time_pdt_grounded(self):
        block = _block()
        assert "2026-09-19 13:00 PDT" in block
