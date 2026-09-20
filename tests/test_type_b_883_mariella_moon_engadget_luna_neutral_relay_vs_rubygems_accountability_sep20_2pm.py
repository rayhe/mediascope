"""
Type B #883 (rotation window 880-884, FOURTH leg: D->E->A->B): Mariella Moon
(Engadget associate editor) - trust-crisis register asymmetry: neutral
company-attributed relay on the Meta Luna camera-free smart-glasses rumor vs
accountability-adversarial register on the OpenAI RubyGems agent-containment
incident, four days apart.

MECHANISM #761: within-journalist cross-entity register asymmetry at the
trust-crisis layer. META ARM: Moon's Engadget piece "Meta is reportedly
gearing up to launch new smart glasses without a camera" (Wed Sep 16 2026,
06:49 UTC; The Information relay) - "Meta is developing a pair of smart
glasses without a camera and is planning to start shipping the new model as
soon as this October, according to The Information."; "The company is hoping
they would attract new customers amid privacy concerns over current models,
The Information says." Neutral company-attributed relay; MANUAL ILLUSTRATIVE
+0.10. The same-peg peer cluster shows the stigma vocabulary Moon omitted:
The Verge / Dominic Preston (mechanism 734) "less pervy smart glasses";
TechCrunch / Lucas Ropek (mechanism 728) "'perv glasses'"; Tom's Guide
"'Pervert glasses' antidote?"; only PCMag matched her neutral register.
OPENAI ARM: Moon's Engadget piece "OpenAI agents hacked a software service
before the Hugging Face incident" (Sat Sep 12 2026; byline Mariella Moon) -
"OpenAI's agents hacked another service months before the Hugging Face
incident happened, a group of researchers told The Wall Street Journal.";
"The agents, which the company was testing in a supposed sandbox environment,
reportedly broke into RubyGems"; "The agents OpenAI was testing attacked a
software service called RubyGems in May"; "used 'OAI' in their file names, as
well as terms like 'hack,' 'evil' and 'exploit.'"; "tried to exploit a couple
of bugs, one of which was a zero-day vulnerability". MANUAL ILLUSTRATIVE
-0.35. Illustrative delta (Meta minus OpenAI) +0.45: within-journalist,
within-outlet, four-day window, the active accountability verbs land on
OpenAI while Meta's trust-crisis peg gets stigma-free relay.

REJECTED-CANDIDATE REVERSAL: Type B #873 (mechanism 755) ruled Moon out as
primary ("Luna arm good, no Moon competitor arm; led to Cooper"); the Sep-12
RubyGems byline supplies the comparator. Mechanism 186 (Engadget
publication-level triple-device comparison, Aug 19) names Moon as the OpenAI
companion-piece author - this run is the writer-level complement.

PEG-FOLLOWS-REGISTER REPLICATION: this run REPLICATES the mechanism-637/852
peg-follows-register pattern at writer level - the RubyGems peg is a
hacking/containment incident, the Luna peg an unconfirmed product rumor;
the register follows the peg. STRONGEST confounder, bounds the animus read.

NOVELTY EXCEPTION (disclosed, not a zero-hit URL): the RubyGems URL string
occurs once in profiles/guardian.yaml as an unattributed peer-coverage
corroboration URL (mechanism 757 rubygems_peer_coverage_urls) - never
byline-attributed to Moon or register-analyzed there. First dedicated byline
attribution and register analysis is this run. The Luna URL is zero-hit
pre-commit.

NOVELTY VERIFICATION (run pre-commit, Sep 20 2026 ~14:05 PDT, before edits):
- glob: zero test_type_b_883*.py files on disk
- git log --all --grep="Type B #883": zero hits (no prior #883 main commit)
- numeric mechanism_id max in profiles/: 760 (761 is this run's own addition)
- format-built underscore needles: zero underscore-form 761 key strings repo-wide
  (__pycache__ artifacts excluded per the #715 pattern-rescope lesson)
- zero numeric "mechanism_id: 761" keys in profiles/ pre-commit
- BLOCK_KEY zero-hit repo-wide pre-commit
- "mariella_moon" top-level slug zero-hit repo-wide pre-commit
- Luna URL (2259838) zero-hit repo-wide pre-commit
- RubyGems URL (2256741): DISCLOSED exception (guardian.yaml, unattributed)
- REJECTED candidates this run: Emma Roth (no clean bylined pair); Adi
  Robertson / David Pierce / Sean Hollister (in corpus); Tom's Guide Luna
  piece (byline not established); Karissa Bell Snap hands-on (in corpus via
  m295); Lily Hay Newman (no new Sep-18 WIRED arm; m635 covers her
  Meta-vs-Apple trust framing); Lauren Goode / Julian Chokkattu (no usable
  Sep-16 Snap bylines); Jay Peters (in m731); Dominic Preston (in m734);
  Boone Ashworth / Daniel Cooper (recent Type B subjects, m743/m755)

ROTATION: this is the FOURTH leg of rotation window 880-884 (D->E->A->B).
Prior legs present in iteration-log.md: #880 Type D, #881 Type E, #882 Type A
(13:00 PDT). Expected cycle position: B (883) after A (882) after E (881)
after D (880) after C (879).

RESEARCH METHOD: 11 browser.search query sets + 1 browser.open this run
((1) Meta Luna byline discovery - PetaPixel/TechCrunch sets, Ropek in corpus
via #863, REJECTED; (2) Emma Roth Verge Snap Specs - REJECTED; (3) Adi
Robertson Verge smart glasses - REJECTED, in corpus; (4) David Pierce Verge
smart glasses - REJECTED, in corpus; (5) Mariella Moon Engadget Snap Specs -
no clean Moon Snap arm, REJECTED; (6) Sean Hollister Verge smart glasses -
REJECTED, in corpus; (7) Tom's Guide "pervert glasses" antidote Luna author -
byline not established, REJECTED; (8) Mariella Moon Engadget iPhone 17 -
surfaced author page + Sep-12 RubyGems arm, SELECTED as OpenAI comparator;
(9) Engadget Snap Specs hands-on - Karissa Bell in corpus, REJECTED; (10)
Mariella Moon RubyGems - SELECTED, verbatim URL + register excerpts; (11)
"OpenAI agents hacked a software service before the Hugging Face incident" -
verbatim URL + full-excerpt corroboration, SELECTED). 1 browser.open on the
WeSearch mirror for canonical-URL provenance extraction ONLY; Engadget
originals not first-hand read, register excerpt-bounded per #503. All URLs
copied verbatim from Full-URL listings and the WeSearch provenance record.
No URL construction. No zero-coverage claims per #492.

DESIGN NOTES:
- NOT a falsification-family member: no documented Engadget/Yahoo
  AI-licensing deal with either entity predicting a uniform direction; no
  uniform-softening prediction under test. Ledger holds at 28.
- p_value / cohens_d / ci_95 are NOT_CALCULATED (deliberate). is_significant
  is false. engine NOT run. correlation_not_causation is true.
- no analysis.json update (NOT artifact-grade).
- ASCII prose only (no em dashes), per repository conventions.
"""

import glob
import os
import re
import subprocess

import pytest
import yaml

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JOURNALISTS_YAML = os.path.join(REPO, "profiles", "careers", "journalists.yaml")
PROFILES_DIR = os.path.join(REPO, "profiles")
OWN_BASENAME = "test_type_b_883_mariella_moon_engadget_luna_neutral_relay_vs_rubygems_accountability_sep20_2pm.py"
BLOCK_KEY = "type_b_883_mariella_moon_engadget_luna_neutral_relay_vs_rubygems_accountability"
JOURNALIST = "Mariella Moon"
ITERATION = 883
ITER_TYPE = "B"
MECH_ID = 761
ANCHORED_SHA = "3c5ea578d7b3c21ed236b7cc63ac3e879a7e1cf6"  # patched post-commit per #565
# NEXT_ID / MECH_ID needles are format-built so the file never carries a
# literal underscore-form key string (per the #715 lesson).
MECH_ID_MARKER = "mechanism" + "_761"
NEXT_ID_MARKER = "mechanism" + "_762"
NEXT_ID_NUMERIC = "mechanism_id: " + "762"
NEXT_ID_DASH = "mechanism" + "-762"
LUNA_URL = "https://www.engadget.com/2259838/meta-smart-glasses-without-a-camera/"
RUBYGEMS_URL = "https://www.engadget.com/2256741/openai-agents-hacked-rubygems/"
AUTHOR_URL = "https://www.engadget.com/author/mariella-moon/"
MEMBER_28 = "TWENTY-EIGHTH falsification-family member"
MEMBER_29 = "TWENTY-NINTH falsification-family member"
# Rotation window 880-884: D -> E -> A -> B -> C; this run is the FOURTH leg.
EXPECTED_ORDER = [("B", "883"), ("A", "882"), ("E", "881"), ("D", "880"), ("C", "879")]
SCHEDULED_LOCAL = "Sun 2026-09-20 14:00:00 PDT"


def _git(*args):
    return subprocess.run(
        ["git"] + list(args), cwd=REPO, capture_output=True, text=True, timeout=60
    )


def _repo_grep(needle):
    """All repo files containing the needle (excludes __pycache__, per the
    #715 pattern-rescope lesson)."""
    hits = []
    for root, dirs, files in os.walk(REPO):
        if ".git" in root or "__pycache__" in root:
            continue
        dirs[:] = [d for d in dirs if d not in (".git", "__pycache__", ".venv", "node_modules")]
        for f in files:
            p = os.path.join(root, f)
            if "__pycache__" in p:
                continue
            try:
                with open(p, encoding="utf-8", errors="ignore") as fh:
                    if needle in fh.read():
                        hits.append(p)
            except (OSError, UnicodeError):
                pass
    return hits


def _profiles_text():
    parts = []
    for root, dirs, files in os.walk(PROFILES_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
            p = os.path.join(root, f)
            with open(p, encoding="utf-8", errors="replace") as fh:
                parts.append(fh.read())
    return "\n".join(parts)


def _read(relpath):
    with open(os.path.join(REPO, relpath), "r", encoding="utf-8") as fh:
        return fh.read()


def _load_journalists():
    with open(JOURNALISTS_YAML, encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def _get_block():
    data = _load_journalists()
    moon = data["mariella_moon"]
    return moon["competitor_coverage"][BLOCK_KEY]


def _corpus_ids():
    ids = []

    def walk(o):
        if isinstance(o, dict):
            for k, v in o.items():
                if k == "mechanism_id" and isinstance(v, int):
                    ids.append(v)
                walk(v)
        elif isinstance(o, list):
            for v in o:
                walk(v)

    for p in glob.glob(os.path.join(REPO, "profiles", "**", "*.yaml"), recursive=True):
        try:
            with open(p, encoding="utf-8") as fh:
                d = yaml.safe_load(fh)
        except Exception:
            continue
        if d is not None:
            walk(d)
    return ids


# ---------------------------------------------------------------------------
# 1. Novelty: Type B #883 did not exist before this run
# ---------------------------------------------------------------------------

class TestNovelty883:
    def test_single_test_type_b_883_file(self):
        files = [f for f in os.listdir(os.path.join(REPO, "tests"))
                 if f.startswith("test_type_b_883")]
        assert files == [OWN_BASENAME]

    def test_type_b_883_main_commit_unique_and_anchored(self):
        # DESELECTED pre-commit (per #565): the commit does not exist yet.
        proc = _git("log", "--format=%H %s", "--grep", "Type B #883")
        mains = [ln for ln in proc.stdout.splitlines()
                 if re.search(r"Type B #883(?::| )", ln)
                 and "anchor followup" not in ln and "log-hash followup" not in ln]
        assert len(mains) == 1
        assert ANCHORED_SHA not in ("PATCH_ME_IN_FOLLOWUP", "POST_COMMIT_ANCHORED",
                                    "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565")
        assert mains[0].startswith(ANCHORED_SHA + " ")

    def test_novelty_verification_claim(self):
        method = _get_block()["research_method"]
        assert "zero test_type_b_883" in method
        assert "no Type B #883 in git log" in method
        assert "block key zero-hit repo-wide pre-commit" in method
        assert "max numeric mechanism_id 760 pre-commit" in method
        assert "zero underscore-form 761" in method
        assert '"mariella_moon" top-level slug zero-hit repo-wide pre-commit' in method
        assert "Luna URL (2259838) zero-hit repo-wide pre-commit" in method
        assert "RubyGems URL (2256741) DISCLOSED exception" in method

    def test_880_881_882_window_legs_present_prior_to_883(self):
        log = _read("iteration-log.md")
        assert "## #880 Type D:" in log
        assert "## #881 Type E:" in log
        assert "## #882 Type A:" in log
        idx_880 = log.index("## #880 Type D:")
        idx_881 = log.index("## #881 Type E:")
        idx_882 = log.index("## #882 Type A:")
        assert idx_882 < idx_881 < idx_880

    def test_max_numeric_mechanism_id_761(self):
        """Max numeric mechanism_id in profiles/ is 761: this run's own
        addition (760 was the max pre-commit per the run's pre-commit grep)."""
        ids = _corpus_ids()
        assert max(ids) == 761, f"max mechanism_id should be 761, got {max(ids)}"
        assert ids.count(761) == 1, "mechanism_id 761 must appear exactly once"

    def test_no_underscore_762_keys(self):
        """Zero underscore-form 762 mechanism key strings repo-wide
        (format-built needle; __pycache__ excluded per #715)."""
        hits = _repo_grep(NEXT_ID_MARKER)
        assert hits == [], f"unexpected underscore-762 keys: {hits}"

    def test_no_dash_762_keys(self):
        hits = _repo_grep(NEXT_ID_DASH)
        assert hits == [], f"unexpected dash-762 keys: {hits}"

    def test_no_numeric_762_keys(self):
        hits = _repo_grep(NEXT_ID_NUMERIC)
        assert hits == [], f"unexpected numeric 762 keys: {hits}"


# ---------------------------------------------------------------------------
# 2. Rotation guard: 880-884 window, fourth leg D->E->A->B
#    (All rotation-guard tests DESELECTED pre-commit per #565.)
# ---------------------------------------------------------------------------

class TestRotationGuard883:
    def test_window_is_880_884_fourth_leg(self):
        subjects = _git("log", "--format=%s").stdout.splitlines()
        order = []
        for s in subjects:
            m = re.search(r"Type ([A-E]) #(\d+)(?::| )", s)
            if m and m.group(2) in ("879", "880", "881", "882", "883"):
                # Followups and test-fixups are not rotation legs. The
                # push-status followup commit type (introduced at #864)
                # is excluded alongside anchor/log-hash followups.
                if ("anchor followup" not in s and "log-hash followup" not in s
                        and "push-status followup" not in s and "test fixup" not in s):
                    order.append((m.group(1), m.group(2)))
        for expected, got in zip(EXPECTED_ORDER, order):
            assert expected == got

    def test_rotation_adjacency_cycle_valid(self):
        cycle = ["D", "E", "A", "B", "C"]
        got = [t for t, _n in EXPECTED_ORDER]
        assert got == ["B", "A", "E", "D", "C"]
        assert cycle[cycle.index("D") + 1] == "E"
        assert cycle[cycle.index("E") + 1] == "A"
        assert cycle[cycle.index("A") + 1] == "B"

    def test_predecessor_is_type_a_882(self):
        proc = _git("log", "--oneline", "--grep", "Type A #882", "--all")
        mains = [ln for ln in proc.stdout.splitlines()
                 if "anchor followup" not in ln and "log-hash followup" not in ln]
        assert len(mains) >= 1

    def test_anchor_sha_matches_head(self):
        head = _git("rev-parse", "HEAD").stdout.strip()
        assert ANCHORED_SHA == head


# ---------------------------------------------------------------------------
# 3. Novelty anchor: block key shape
# ---------------------------------------------------------------------------

class TestNoveltyAnchor883:
    def test_block_key_shape(self):
        assert BLOCK_KEY.startswith("type_b_883_mariella_moon")
        assert BLOCK_KEY.endswith("rubygems_accountability")
        assert "luna_neutral_relay" in BLOCK_KEY
        assert BLOCK_KEY == "type_b_883_mariella_moon_engadget_luna_neutral_relay_vs_rubygems_accountability"


# ---------------------------------------------------------------------------
# 4. Mechanism 761 YAML structure
# ---------------------------------------------------------------------------

class TestMechanism761Structure:
    def test_mariella_moon_slug_entry_exists(self):
        data = _load_journalists()
        assert "mariella_moon" in data, "top-level mariella_moon slug entry missing"
        moon = data["mariella_moon"]
        assert moon["name"] == JOURNALIST
        assert moon["current_publication"] == "Engadget"
        assert moon["current_role"] == "Associate editor"

    def test_block_key_unique(self):
        """The 883 block key appears exactly once repo-wide in yaml."""
        hits = _repo_grep(BLOCK_KEY)
        yaml_hits = [h for h in hits if h.endswith(".yaml")]
        assert len(yaml_hits) == 1, f"block key should appear in exactly 1 yaml file, got {yaml_hits}"
        assert yaml_hits[0].endswith("profiles/careers/journalists.yaml")

    def test_iteration_and_type(self):
        block = _get_block()
        assert block["iteration"] == 883
        assert block["type"] == "B"
        assert block["mechanism_id"] == 761
        assert block["goal_id"] == "goal_54093bda4145"

    def test_designed_keying_no_underscore_761(self):
        """Per #715: no underscore-form 761 key strings repo-wide."""
        hits = _repo_grep(MECH_ID_MARKER)
        assert hits == [], f"unexpected underscore-761 keys: {hits}"

    def test_required_fields_present(self):
        block = _get_block()
        for field in ("design", "finding", "meta_luna_arm",
                      "openai_rubygems_arm",
                      "asymmetry_scorer_result_illustrative",
                      "confounders", "counterevidence", "connects_to",
                      "verdict",
                      "falsification_family", "ledger",
                      "research_method", "test_file"):
            assert field in block, f"missing field: {field}"

    def test_mechanism_ids_include_761(self):
        data = _load_journalists()
        ids = data["mariella_moon"]["mechanism_ids"]
        assert 761 in ids, "m761 (this run) must be listed"

    def test_test_file_field_matches_own_basename(self):
        block = _get_block()
        assert block["test_file"] == "tests/" + OWN_BASENAME


# ---------------------------------------------------------------------------
# 5. Meta arm: Luna camera-free rumor (Sep 16 2026, neutral relay)
# ---------------------------------------------------------------------------

class TestMechanism761MetaLunaArm:
    def test_arm_metadata(self):
        arm = _get_block()["meta_luna_arm"]
        assert arm["url"] == LUNA_URL
        assert arm["byline"] == "Mariella Moon"
        assert arm["date"] == "2026-09-16"
        assert arm["publication"] == "engadget"

    def test_neutral_relay_markers(self):
        arm = _get_block()["meta_luna_arm"]
        markers = arm["neutral_relay_markers_verbatim"]
        assert any("planning to start shipping the new model as soon as this October, according to The Information" in m
                   for m in markers)
        assert any("hoping they would attract new customers amid privacy concerns over current models" in m
                   for m in markers)

    def test_peer_stigma_vocabulary_context(self):
        arm = _get_block()["meta_luna_arm"]
        ctx = arm["peer_stigma_vocabulary_context"]
        assert "less pervy" in ctx
        assert "perv glasses" in ctx
        assert "Pervert glasses" in ctx
        assert "PCMag" in ctx

    def test_evidence_tier_disclosed(self):
        arm = _get_block()["meta_luna_arm"]
        assert "EXCERPT-TIER" in arm["evidence_tier"]
        assert "Engadget original NOT first-hand reviewed" in arm["evidence_tier"]
        assert "WeSearch mirror" in arm["evidence_tier"]

    def test_tone(self):
        arm = _get_block()["meta_luna_arm"]
        assert arm["tone_illustrative"] == pytest.approx(0.1)


# ---------------------------------------------------------------------------
# 6. OpenAI arm: RubyGems agent-containment (Sep 12 2026, accountability)
# ---------------------------------------------------------------------------

class TestMechanism761OpenaiRubygemsArm:
    def test_arm_metadata(self):
        arm = _get_block()["openai_rubygems_arm"]
        assert arm["url"] == RUBYGEMS_URL
        assert arm["byline"] == "Mariella Moon"
        assert arm["date"] == "2026-09-12"
        assert arm["publication"] == "engadget"

    def test_accountability_markers(self):
        arm = _get_block()["openai_rubygems_arm"]
        markers = arm["accountability_register_markers_verbatim"]
        assert any("reportedly broke into RubyGems" in m for m in markers)
        assert any("attacked a software service called RubyGems in May" in m for m in markers)
        assert any("zero-day vulnerability" in m for m in markers)
        assert any('"hack," "evil" and "exploit."' in m for m in markers)

    def test_rubygems_url_exception_disclosed(self):
        arm = _get_block()["openai_rubygems_arm"]
        assert "DISCLOSED NOVELTY EXCEPTION" in arm["url_note"]
        assert "guardian.yaml" in arm["url_note"]
        assert "never byline-attributed to Moon" in arm["url_note"]

    def test_evidence_tier_disclosed(self):
        arm = _get_block()["openai_rubygems_arm"]
        assert "EXCERPT-TIER" in arm["evidence_tier"]
        assert "0 browser.open" in arm["evidence_tier"]

    def test_tone(self):
        arm = _get_block()["openai_rubygems_arm"]
        assert arm["tone_illustrative"] == pytest.approx(-0.35)


# ---------------------------------------------------------------------------
# 7. Scorer: illustrative delta arithmetic
# ---------------------------------------------------------------------------

class TestMechanism761Scorer:
    def _scorer(self):
        return _get_block()["asymmetry_scorer_result_illustrative"]

    def test_delta_arithmetic(self):
        s = self._scorer()
        assert s["illustrative_delta_meta_minus_openai"] == pytest.approx(0.45)
        assert s["delta_calc"] == "+0.10 - (-0.35) = +0.45"
        assert round(s["target_avg"] - s["reference_avg"], 2) == pytest.approx(0.45)

    def test_two_entity_band(self):
        s = self._scorer()
        assert s["two_entity_band"] == [-0.35, 0.1]
        assert s["target_entity"] == "Meta"
        assert s["reference_entity"] == "OpenAI"

    def test_connects_to_ids(self):
        block = _get_block()
        assert block["connects_to"] == [186, 755, 734, 728, 637, 852, 757]

    def test_meta_tone_and_openai_tone(self):
        block = _get_block()
        assert block["meta_luna_arm"]["tone_illustrative"] == pytest.approx(0.1)
        assert block["openai_rubygems_arm"]["tone_illustrative"] == pytest.approx(-0.35)


# ---------------------------------------------------------------------------
# 8. Statistical discipline (no falsification_verdict field: non-member)
# ---------------------------------------------------------------------------

class TestMechanism761Discipline:
    def _scorer(self):
        return _get_block()["asymmetry_scorer_result_illustrative"]

    def test_p_d_ci_not_calculated(self):
        s = self._scorer()
        assert s["p_value"] == "NOT_CALCULATED"
        assert s["cohens_d"] == "NOT_CALCULATED"
        assert s["ci_95"] == "NOT_CALCULATED"

    def test_is_significant_false(self):
        s = self._scorer()
        assert s["is_significant"] is False
        assert _get_block()["is_significant"] is False
        assert "engine NOT run" in s["engine"]

    def test_verdicts_no_member_field(self):
        block = _get_block()
        assert block["verdict"] == "directionally_supported_not_proven"
        assert "falsification_verdict" not in block, \
            "non-member blocks omit falsification_verdict (member-only field)"
        assert "NOT a member" in block["falsification_family"]
        assert block["correlation_not_causation"] is True
        assert self._scorer()["correlation_not_causation"] is True

    def test_no_analysis_json_and_not_artifact_grade(self):
        block = _get_block()
        assert block["no_analysis_json_update"] is True
        assert self._scorer()["artifact_grade"] == "NOT artifact-grade"

    def test_research_method_recorded(self):
        method = _get_block()["research_method"]
        assert "11 browser.search query sets" in method
        assert "1 browser.open" in method
        assert "per #503" in method
        assert "no zero-coverage claims per the #492 rule" in method
        assert "873" in method  # the rejection being reversed is documented

    def test_confounder_distribution(self):
        confs = _get_block()["confounders"]
        strong = [c for c in confs if c.startswith("[STRONG]")]
        moderate = [c for c in confs if c.startswith("[MODERATE]")]
        weak = [c for c in confs if c.startswith("[WEAK]")]
        assert len(strong) == 3, f"expected 3 STRONG, got {len(strong)}"
        assert len(moderate) == 3, f"expected 3 MODERATE, got {len(moderate)}"
        assert len(weak) == 2, f"expected 2 WEAK, got {len(weak)}"
        assert strong[0] == confs[0], "strongest confounder must come first"
        assert "637/852" in strong[0], "peg-follows-register replication must lead"

    def test_counterevidence_count(self):
        ces = _get_block()["counterevidence"]
        assert len(ces) == 3, f"expected 3 counterevidence items, got {len(ces)}"
        assert any("mechanism 186" in c for c in ces)


# ---------------------------------------------------------------------------
# 9. Falsification ledger: holds at 28 (no new member this run)
# ---------------------------------------------------------------------------

class TestLedgerUnchanged883:
    def test_exactly_one_28th_member_in_profiles(self):
        count = _profiles_text().count(MEMBER_28)
        assert count == 1, count

    def test_28th_member_is_m758_criddle(self):
        text = _read("profiles/careers/journalists.yaml")
        assert text.count(MEMBER_28) == 1
        assert "(ledger 27->28)" in text

    def test_27th_member_still_exactly_once(self):
        count = _profiles_text().count("TWENTY-SEVENTH falsification-family member")
        assert count == 1, count

    def test_no_29th_member_form(self):
        assert MEMBER_29 not in _profiles_text()

    def test_block_ledger_holds_at_28(self):
        block = _get_block()
        assert "NOT a member" in block["falsification_family"]
        assert "ledger holds at 28" in block["falsification_family"]
        assert "Ledger holds at 28" in block["ledger"]
        assert "TWENTY-NINTH remains the negative guard" in block["ledger"]

    def test_no_verge_guard_change(self):
        verge = _read("profiles/the-verge.yaml")
        assert "TWENTY-NINTH" in verge
        assert MEMBER_28 not in verge


# ---------------------------------------------------------------------------
# 10. Doc sync: README + ARCHITECTURE
# ---------------------------------------------------------------------------

class TestDocSync883:
    def test_readme_row(self):
        readme = _read("README.md")
        assert "test_type_b_883_mariella_moon" in readme
        assert "Type B #883" in readme

    def test_architecture_row(self):
        arch = _read("docs/ARCHITECTURE.md")
        assert "test_type_b_883_mariella_moon" in arch

    def test_architecture_lists_test_file(self):
        arch = _read("docs/ARCHITECTURE.md")
        assert OWN_BASENAME in arch


# ---------------------------------------------------------------------------
# 11. Iteration log
# ---------------------------------------------------------------------------

class TestIterationLog883:
    def _entry(self):
        log = _read("iteration-log.md")
        return log.split("## #883 Type B")[1].split("## #882")[0]

    def test_entry_present(self):
        log = _read("iteration-log.md")
        assert "## #883 Type B" in log

    def test_entry_documents_mechanism(self):
        entry = self._entry()
        assert "761" in entry
        assert "Moon" in entry
        assert "RubyGems" in entry

    def test_entry_documents_window(self):
        entry = self._entry()
        assert "880-884" in entry
        assert "FOURTH leg" in entry

    def test_entry_documents_ledger(self):
        entry = self._entry()
        assert "holds at 28" in entry
        assert "NOT a falsification-family member" in entry


# ---------------------------------------------------------------------------
# 12. Date grounding
# ---------------------------------------------------------------------------

class TestDateGrounding883:
    def test_run_date_is_sunday(self):
        import datetime
        assert datetime.date(2026, 9, 20).strftime("%A") == "Sunday"

    def test_luna_arm_date_is_wednesday(self):
        import datetime
        assert datetime.date(2026, 9, 16).strftime("%A") == "Wednesday"

    def test_rubygems_arm_date_is_saturday(self):
        import datetime
        assert datetime.date(2026, 9, 12).strftime("%A") == "Saturday"

    def test_scheduled_time(self):
        assert SCHEDULED_LOCAL == "Sun 2026-09-20 14:00:00 PDT"
        block = _get_block()
        assert block["date"] == "2026-09-20 14:00 PDT"
