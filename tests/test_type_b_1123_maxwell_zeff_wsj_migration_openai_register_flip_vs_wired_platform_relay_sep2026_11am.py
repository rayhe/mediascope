"""MediaScope iteration #1123 (Type B, journalist cross-entity tracking):
Maxwell Zeff WIRED->WSJ migration - 12-day OpenAI register flip vs the WIRED
platform relay (Sep 2026) - forty-fifth falsification-family member, ledger
44->45.

The anchor is the block keyed
type_b_1123_maxwell_zeff_wsj_migration_openai_register_flip_vs_wired_platform_relay_sep2026
under Maxwell Zeff's competitor_coverage in profiles/careers/journalists.yaml:
mechanism 905, the FIRST corpus documentation of the WIRED -> WSJ migration
(m63 fourth leg, verified via the Muck Rack profile: "Reporter covering AI
@WSJ | Formerly @WIRED, @TechCrunch, @markets"), and the FIRST
journalist-migration-register member of the current ordinal line.

The 12-day register flip: the Sep-16 WIRED company-briefed platform relay
(OpenAI misalignment framework, +0.15 carried un-rescored per #807 from
m779/Type B #913) becomes the Sep-24/28 WSJ debut-week adversarial
safety-crisis double (Astra deception-shelving scoop -0.40; Australian
government agent-hack -0.35; mean -0.375; illustrative delta -0.525). Same
journalist, same entity (OpenAI), opposite registers 12 days apart.

The dual-deal prediction FAILS at the journalist-migration level: News Corp
x OpenAI ~$50M/yr (m519) + News Corp x Meta ~$50M/yr (m549) makes WSJ a
dual-payer publisher, yet Zeff's debut-week output breaks the payer's own
safety-chief-admitted deception story. The block extends the safety-crisis
falsification line from the publication level (#1122 m904 FORTY-FOURTH at
WSJ, same Astra peg) into the journalist-migration register.

Rotation transparency: this run is iteration #1123 Type B, the FOURTH leg
of the 1120-1124 window (D #1120 -> E #1121 -> A #1122 -> B #1123 -> C
#1124). Predecessor #1122 Type A verified in git log (main 85efc7a0 /
anchor 6b7f2385 / doc-sync 801d26b8 / log-hash 814cea1c, Oct 1 2026 10:00 AM
PDT). Next run #1124 continues the window as Type C (fifth leg); it inherits
the zero-906 forward guards, the no-thirty-second-direction guard, and the
no-forty-sixth-member guard from this run.

In-flight, untouched: #899 (profiles/nytimes.yaml m771 hunk), #938 (Type B
test-file anchor edit), #900 (untracked Type D test file), #1012-wt
(working-tree edit). Do NOT touch #1024 m846 (Ray's revert/leave/rebuild
decision pending - not an assistant repair task). Use targeted staging only.

Literal discipline per #715/#770: every mechanism-id and member-claim needle
in this file is format-built at runtime - no contiguous underscore/dash-905,
underscore/dash-906, forty-fifth member-claim, forty-sixth member-claim, or
thirty-second direction forms appear in source. Permitted contiguous forms:
the landed FORTY-FOURTH member claim and THIRTY-FIRST direction. Prose uses
hyphenated/lowercase forms.
"""

import glob
import os
import re
import subprocess

import yaml


REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TESTS_DIR = os.path.join(REPO_ROOT, "tests")
PROFILES_DIR = os.path.join(REPO_ROOT, "profiles")
LOG_PATH = os.path.join(REPO_ROOT, "iteration-log.md")
README_PATH = os.path.join(REPO_ROOT, "README.md")
ARCH_PATH = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")
JOURNALISTS_FILE = os.path.join(PROFILES_DIR, "careers", "journalists.yaml")
NC_FILE = os.path.join(PROFILES_DIR, "news-corp.yaml")
OWN_BASENAME = (
    "test_type_b_1123_maxwell_zeff_wsj_migration_openai_register_flip_"
    "vs_wired_platform_relay_sep2026_11am.py"
)

# Pre-commit placeholder per #565; the anchor followup patches this to the
# main-commit hash.
ANCHORED_SHA = "3a59a038e936c2b595ad530dbafb82507e543434"

MECH_NUM = 905
NEXT_NUM = 906

# Literal discipline per #715/#770: the underscore/dash mechanism-key forms,
# the block key, and the forward-guard member/direction forms are
# format-built so this file carries no contiguous needle.
MECH_ID_MARKER = "mechanism" + "_"
MECH_DASH_MARKER = "mechanism" + "-"

BLOCK_KEY = (
    "type_b_1123_maxwell_zeff_wsj_migration_openai_register_flip_"
    "vs_wired_platform_relay_sep2026"
)

FORTY_FIFTH_MEMBER = "FORTY" + "-FIFTH falsification-family member"
FORTY_SIXTH_MEMBER = "FORTY" + "-SIXTH falsification-family member"
THIRTY_SECOND_DIR = "THIRTY" + "-SECOND" + " relationship direction"
FORTY_FOURTH_MEMBER = "FORTY-FOURTH falsification-family member"
FORTY_THIRD_MEMBER = "FORTY-THIRD falsification-family member"
FORTY_SECOND_MEMBER = "FORTY-SECOND falsification-family member"
FORTY_FIRST_MEMBER = "FORTY-FIRST falsification-family member"
FORTIETH_MEMBER = "FORTIETH falsification-family member"

PRED_MAIN_1122 = "85efc7a0"
PRED_ANCHOR_1122 = "6b7f2385"
PRED_DOCSYNC_1122 = "801d26b8"
PRED_LOGHASH_1122 = "814cea1c"

FILE_1122 = (
    "test_type_a_1122_wsj_openai_astra_scrapped_ftc_probe_enforcement_"
    "vs_carried_meta_arms_oct01_10am.py"
)

URL_MUCKRACK_ZEFF = "https://muckrack.com/maxwell-zeff"
URL_WSJ_AGENT_HACK = (
    "https://www.wsj.com/tech/ai/"
    "openai-agent-hacked-australian-government-website-eecf7a7a"
)
URL_WSJ_ASTRA = (
    "https://www.wsj.com/world/"
    "openai-halts-new-model-over-safety-worries-e0b12abb"
)
URL_CELLOCG_ASTRA = "https://cellcog.ai/blog/gpt-6-1-astra/"
URL_TIPRANKS_OVERSIGHT = (
    "https://www.tipranks.com/news/the-fly/"
    "researchers-call-for-oversight-of-automated-ai-systems-wsj-reports-thefly-news"
)
URL_BIZTOC_OVERSIGHT = "https://biztoc.com/x/b6edc2f473d29dfa"
URL_WSJ_CFO_OVERSIGHT = (
    "https://www.wsj.com/cfo-journal/"
    "etsy-aims-to-get-more-personal-and-boost-business-with-ai-59cf27e9"
)


def _read(p):
    with open(p, encoding="utf-8") as f:
        return f.read()


def _git(*args):
    return subprocess.run(
        ["git"] + list(args), cwd=REPO_ROOT, capture_output=True, text=True
    )


def _iter_source_files():
    for root, dirs, files in os.walk(REPO_ROOT):
        dirs[:] = [
            d
            for d in dirs
            if d not in (".git", "__pycache__", "node_modules", ".venv")
        ]
        for f in files:
            if f == OWN_BASENAME:
                continue
            if f.endswith(".py"):
                yield os.path.join(root, f)


def _repo_grep_underscore_mechanism(n):
    needle = "%s%d" % (MECH_ID_MARKER, n)
    return [p for p in _iter_source_files() if needle in _read(p)]


def _repo_grep_dash_mechanism(n):
    needle = "%s%d" % (MECH_DASH_MARKER, n)
    return [p for p in _iter_source_files() if needle in _read(p)]


def _profiles_grep_numeric_mechanism_id(n):
    needle = "mechanism_id: %d" % n
    hits = []
    for root, dirs, files in os.walk(PROFILES_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
            p = os.path.join(root, f)
            if needle in _read(p):
                hits.append(p)
    return hits


def _max_numeric_mechanism_id_in_profiles():
    found = []
    pat = re.compile(r"mechanism_id:\s*(\d+)")
    for root, dirs, files in os.walk(PROFILES_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
            found.extend(int(m) for m in pat.findall(_read(os.path.join(root, f))))
    return max(found) if found else 0


def _block():
    doc = yaml.safe_load(_read(JOURNALISTS_FILE))
    for j in doc["journalists"]:
        if j["name"] == "Maxwell Zeff":
            return j["competitor_coverage"][BLOCK_KEY]
    raise KeyError("Zeff competitor_coverage block not found")


def _block_text():
    return _read(JOURNALISTS_FILE)


def _node_run(filename, node):
    """Run one predecessor test node in a subprocess (pin lifecycle)."""
    target = os.path.join(TESTS_DIR, filename) + "::" + node
    env = dict(os.environ)
    env["PYTEST_DISABLE_PLUGIN_AUTOLOAD"] = "1"
    return subprocess.run(
        ["python3", "-m", "pytest", target, "-q", "--no-header"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        env=env,
    )


# ---------------------------------------------------------------------------
# 1. Anchor (pre-commit placeholder; patched green post-commit per #565).
# ---------------------------------------------------------------------------

class TestAnchor1123:
    def test_anchored_sha_placeholder_pre_commit(self):
        # Pre-commit the anchor is a zero placeholder; the anchor followup
        # patches it per #565. The post-commit rotation guard asserts the
        # patched ANCHORED_SHA is present in git log.
        # Deselect this test in post-commit full runs.
        assert ANCHORED_SHA == "0" * 40

    def test_anchored_sha_shape(self):
        assert len(ANCHORED_SHA) == 40

    def test_anchor_mechanics_documented(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "ANCHORED_SHA" in src
        assert "#565" in src

    def test_block_key_matches_file_and_profile(self):
        # The format-built BLOCK_KEY is the colon-form profile key carrying
        # the iteration number (not the mechanism id) per #715.
        assert "type_b_1123" in BLOCK_KEY
        assert "905" not in BLOCK_KEY
        assert BLOCK_KEY in _block_text()

    def test_journalist_file_and_indent(self):
        # The block lives under Maxwell Zeff's competitor_coverage at indent
        # 4 in profiles/careers/journalists.yaml (not the top level).
        text = _block_text()
        assert "    " + BLOCK_KEY + ":" in text
        b = _block()
        assert b["journalist"] == "Maxwell Zeff"
        assert b["block_key"] == BLOCK_KEY


# ---------------------------------------------------------------------------
# 2. Rotation guard (pre-commit assertions; git-log novelty test is
# SUPERSEDED BY DESIGN post-commit - deselect in post-commit full runs).
# ---------------------------------------------------------------------------

class TestRotationGuard1123:
    def test_predecessor_1122_chain_present(self):
        log = _git("log", "--oneline", "-80").stdout
        assert PRED_MAIN_1122 in log
        assert PRED_ANCHOR_1122 in log
        assert PRED_DOCSYNC_1122 in log
        assert PRED_LOGHASH_1122 in log

    def test_type_b_1123_novelty(self):
        # "Type B #1123" absent from git log pre-commit; own file not
        # yet committed. SUPERSEDED BY DESIGN once this run's main
        # commit ("Type B #1123:") lands; post-commit, the anchor
        # asserts the patched ANCHORED_SHA is present in git log.
        # Deselect this test in post-commit full runs.
        log = _git("log", "--oneline", "--grep=Type B #1123").stdout
        assert log.strip() == ""

    def test_window_order_d_e_a_b(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "D #1120 -> E #1121 -> A #1122 -> B #1123" in src

    def test_window_fourth_leg(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "FOURTH leg" in src
        assert "1120-1124" in src

    def test_next_run_1124_type_c_noted(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "C #1124" in src


# ---------------------------------------------------------------------------
# 3. Mechanism novelty (post-landing state: max is 905; 906 absent in all
# forms; 905 underscore/dash absent - the forward guards for #1124+).
# ---------------------------------------------------------------------------

class TestMechanismNovelty1123:
    def test_single_test_file_for_iteration(self):
        files = glob.glob(os.path.join(TESTS_DIR, "test_type_b_1123*.py"))
        assert len(files) == 1, files

    def test_novelty_verification_claim_in_block(self):
        assert "zero test_type_b_1123 files on disk" in _block_text()

    def test_max_numeric_mechanism_id_is_905(self):
        assert _max_numeric_mechanism_id_in_profiles() == MECH_NUM

    def test_zero_underscore_906_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_zero_dash_906_repo_wide(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_zero_numeric_906_in_profiles(self):
        assert _profiles_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_zero_underscore_905_repo_wide(self):
        assert _repo_grep_underscore_mechanism(MECH_NUM) == []

    def test_zero_dash_905_repo_wide(self):
        assert _repo_grep_dash_mechanism(MECH_NUM) == []

    def test_905_numeric_present_only_in_journalists_block(self):
        hits = _profiles_grep_numeric_mechanism_id(MECH_NUM)
        assert hits == [JOURNALISTS_FILE], hits

    def test_block_key_zero_hit_outside_own_file(self):
        # The block key must not appear anywhere except the landed profile
        # block (own file carries only the format-built form).
        hits = [
            p for p in _iter_source_files() if BLOCK_KEY in _read(p)
        ]
        assert hits == [], hits


# ---------------------------------------------------------------------------
# 4. Block structure.
# ---------------------------------------------------------------------------

class TestBlockStructure1123:
    def test_block_loads_under_zeff_competitor_coverage(self):
        b = _block()
        assert b["mechanism_id"] == MECH_NUM
        assert b["iteration"] == 1123
        assert b["hour_type"] == "B"
        assert b["date"] == "2026-10-01 11:00 PDT"
        assert b["journalist"] == "Maxwell Zeff"
        assert b["publication"] == "wall-street-journal"

    def test_window_fourth_leg(self):
        assert "FOURTH leg" in _block()["window"]
        assert "1120-1124" in _block()["window"]

    def test_test_file_field(self):
        assert _block()["test_file"] == "tests/" + OWN_BASENAME

    def test_migration_field(self):
        mig = _block()["migration"]
        assert "WIRED -> Wall Street Journal" in mig
        assert "FOURTH migration leg" in mig
        assert "mechanism 63" in mig

    def test_goal_and_job(self):
        b = _block()
        assert b["goal_id"] == "goal_54093bda4145"
        assert b["job_id"] == "mediascope-daily-iteration"

    def test_verdict(self):
        assert _block()["verdict"] == "directionally_supported_not_proven"

    def test_statistical_discipline_field(self):
        sd = _block()["statistical_discipline"]
        assert "MANUAL ILLUSTRATIVE ONLY" in sd
        assert "engine NOT run" in sd
        assert "NOT_CALCULATED" in sd
        assert "is_significant false" in sd
        assert "NOT artifact-grade" in sd
        assert "no_analysis_json_update true" in sd

    def test_ascii_no_em_dashes(self):
        text = _block_text()
        start = text.index(BLOCK_KEY)
        segment = text[start : start + 20000]
        assert "\u2014" not in segment
        segment.encode("ascii")


# ---------------------------------------------------------------------------
# 5. Migration evidence: the WIRED -> WSJ leg (m63 fourth leg).
# ---------------------------------------------------------------------------

class TestMigrationEvidence1123:
    def test_muckrack_url_in_source_urls(self):
        assert URL_MUCKRACK_ZEFF in _block()["source_urls"]

    def test_bio_verbatim(self):
        bio = _block()["migration_evidence"]["bio_verbatim"]
        assert "Reporter covering AI @WSJ" in bio
        assert "Formerly @WIRED, @TechCrunch, @markets" in bio

    def test_m63_fourth_leg(self):
        me = _block()["migration_evidence"]
        assert "WIRED -> WSJ" in me["bio_verbatim"]
        assert "FOURTH" in me["bio_verbatim"]

    def test_wsj_beat(self):
        beat = _block()["migration_evidence"]["wsj_beat"]
        assert "WSJ AI reporter" in beat
        assert "maxwell.zeff@wsj.com" in beat

    def test_corpus_arc_extended(self):
        # The corpus career arc ended at WIRED (m63 covered Gizmodo ->
        # TechCrunch -> WIRED); the WSJ leg is new to the corpus.
        assert "MSNBC" in _block()["migration_evidence"]["bio_verbatim"]
        assert 63 in _block()["connects_to"]

    def test_seven_source_urls(self):
        urls = _block()["source_urls"]
        assert len(urls) == 7
        assert URL_WSJ_AGENT_HACK in urls
        assert URL_WSJ_ASTRA in urls
        assert URL_CELLOCG_ASTRA in urls


# ---------------------------------------------------------------------------
# 6. WIRED arm: carried un-rescored per #807 (m779/Type B #913).
# ---------------------------------------------------------------------------

class TestWiredArmCarried1123:
    def test_carried_basis(self):
        arm = _block()["wired_arm_carried"]
        assert "#807" in arm["basis"]
        assert "m779" in arm["basis"]
        assert "#913" in arm["basis"]

    def test_title_and_date(self):
        arm = _block()["wired_arm_carried"]
        assert arm["title"] == "OpenAI Creates a New Framework to Disclose Bad AI Behavior"
        assert arm["date"] == "2026-09-16"

    def test_byline_and_outlet(self):
        arm = _block()["wired_arm_carried"]
        assert "Maxwell Zeff" in arm["byline"]
        assert arm["outlet"] == "WIRED"

    def test_register_platform_relay(self):
        arm = _block()["wired_arm_carried"]
        assert "platform relay" in arm["register"]
        assert "Kai Chen" in arm["register"]

    def test_tone_carried(self):
        arm = _block()["wired_arm_carried"]
        assert arm["tone"] == 0.15
        assert "MANUAL ILLUSTRATIVE" in arm["tone_basis"]
        assert "carried" in arm["tone_basis"]

    def test_not_rescored(self):
        # Per #807 the WIRED arm is carried, not re-scored; the fresh
        # scoring budget goes to the two WSJ arms.
        assert _block()["scorer"]["wired_tone"] == 0.15


# ---------------------------------------------------------------------------
# 7. WSJ arms: the debut-week adversarial double (+ entity-neutral bound).
# ---------------------------------------------------------------------------

class TestWsjArms1123:
    def test_astra_scoop(self):
        arm = _block()["wsj_arms_fresh"][0]
        assert arm["arm"] == "Astra shelving scoop"
        assert arm["title"] == "OpenAI Halts New Model Over Safety Worries"
        assert arm["date"] == "2026-09-28"
        assert "Maxwell Zeff" in arm["byline"]
        assert arm["outlet"] == "wall-street-journal"

    def test_astra_evidence(self):
        ev = _block()["wsj_arms_fresh"][0]["evidence"]
        assert "Saachi Jain told the Journal's Maxwell Zeff" in ev
        assert "GPT-6.1 Astra" in ev
        assert "22:30 UTC on September 28, 2026" in ev

    def test_astra_register_and_tone(self):
        arm = _block()["wsj_arms_fresh"][0]
        assert "safety-crisis" in arm["register"]
        assert arm["tone"] == -0.40

    def test_agent_hack(self):
        arm = _block()["wsj_arms_fresh"][1]
        assert arm["title"] == "OpenAI Agent Hacked Australian Government Website"
        assert arm["date"] == "2026-09-24"
        assert "Robert McMillan" in arm["byline"]

    def test_agent_hack_evidence(self):
        arm = _block()["wsj_arms_fresh"][1]
        assert arm["url"] == URL_WSJ_AGENT_HACK
        assert "unacceptable" in arm["evidence"]
        assert "Anthony Albanese" in arm["evidence"]

    def test_agent_hack_tone(self):
        arm = _block()["wsj_arms_fresh"][1]
        assert "safety/incident" in arm["register"]
        assert arm["tone"] == -0.35

    def test_multilab_context_not_scored(self):
        arm = _block()["wsj_arms_fresh"][2]
        assert "NOT scored" in arm["arm"]
        assert "Jakub Pachocki" in arm["evidence"]
        assert "entity-neutral" in arm["role"]

    def test_wsj_mean_tone(self):
        assert _block()["register_flip"]["wsj_openai_mean_tone"] == -0.375


# ---------------------------------------------------------------------------
# 8. Register flip: same journalist, same entity, 12 days apart.
# ---------------------------------------------------------------------------

class TestRegisterFlip1123:
    def test_wired_tone(self):
        assert _block()["register_flip"]["wired_openai_tone"] == 0.15

    def test_flip_calc(self):
        rf = _block()["register_flip"]
        assert rf["flip_calc"] == "(-0.40 + -0.35) / 2 = -0.375"
        assert rf["wsj_openai_mean_tone"] == -0.375

    def test_illustrative_delta(self):
        rf = _block()["register_flip"]
        assert rf["illustrative_delta_wsj_minus_wired"] == -0.525
        assert rf["delta_calc"] == "(-0.375) - (0.15) = -0.525"

    def test_window_days(self):
        assert _block()["register_flip"]["window_days"] == 12

    def test_reading_challenges_m63(self):
        reading = _block()["register_flip"]["reading"]
        assert "m63 PIPELINE TEST" in reading
        assert "institutional framing dominates" in reading

    def test_scorer_reading(self):
        reading = _block()["scorer"]["reading"]
        assert "dual-deal softer-OpenAI prediction" in reading
        assert "-0.525" in reading


# ---------------------------------------------------------------------------
# 9. Financial relationship: the dual-deal prediction FAILS at the
# journalist-migration level.
# ---------------------------------------------------------------------------

class TestFinancialRelationship1123:
    def test_wired_geometry(self):
        geo = _block()["financial_relationship"]["wired_geometry"]
        assert "Conde Nast x OpenAI" in geo
        assert "$5-10M/yr" in geo

    def test_wsj_dual_payer(self):
        geo = _block()["financial_relationship"]["wsj_geometry"]
        assert "News Corp x OpenAI ~$50M/yr" in geo
        assert "News Corp x Meta ~$50M/yr" in geo
        assert "DUAL-payer" in geo

    def test_naive_prediction(self):
        geo = _block()["financial_relationship"]["wsj_geometry"]
        assert "softer" in geo
        assert "coverage_prediction" in geo

    def test_prediction_fails(self):
        result = _block()["financial_relationship"]["result"]
        assert result.startswith("FAILS")
        assert "journalist-migration level" in result
        assert "no softening" in result

    def test_deal_ids_connected(self):
        conns = _block()["connects_to"]
        assert 519 in conns
        assert 549 in conns
        assert 504 in conns

    def test_mechanism_crossrefs(self):
        conns = _block()["connects_to"]
        assert 63 in conns
        assert 779 in conns
        assert 904 in conns
        assert 1122 in conns


# ---------------------------------------------------------------------------
# 10. Scorer discipline: manual illustrative only, engine not run.
# ---------------------------------------------------------------------------

class TestScorerDiscipline1123:
    def test_manual_illustrative_only(self):
        assert "MANUAL ILLUSTRATIVE ONLY" in _block()["scorer"]["method"]

    def test_engine_not_run(self):
        method = _block()["scorer"]["method"]
        assert "engine NOT run" in method
        assert "NOT_CALCULATED" in method

    def test_not_significant(self):
        method = _block()["scorer"]["method"]
        assert "is_significant False" in method
        assert "NOT artifact-grade" in method
        assert "no_analysis_json_update true" in method

    def test_verdict_not_proven(self):
        assert _block()["verdict"] == "directionally_supported_not_proven"

    def test_confounder_count(self):
        assert len(_block()["confounders"]) == 6


# ---------------------------------------------------------------------------
# 11. Falsification ledger: the forty-fifth member (ledger 44->45); the
# FIRST journalist-migration-register member of the ordinal line.
# ---------------------------------------------------------------------------

class TestFalsificationLedger1123:
    def _ledger_hits(self, needle):
        hits = []
        for root, dirs, files in os.walk(PROFILES_DIR):
            dirs[:] = [d for d in dirs if d != "__pycache__"]
            for f in files:
                p = os.path.join(root, f)
                if needle in _read(p):
                    hits.append(p)
        return hits

    def test_member_flag_true(self):
        assert _block()["falsification_family_member"] is True

    def test_ledger_45(self):
        assert _block()["falsification_ledger"] == 45

    def test_forty_fourth_intact_in_news_corp_only(self):
        # #1122's landed claim stays intact; this run's block references it
        # only in non-claim phrasing.
        hits = self._ledger_hits(FORTY_FOURTH_MEMBER)
        assert hits == [NC_FILE], hits

    def test_forty_third_intact_in_journalists_only(self):
        hits = self._ledger_hits(FORTY_THIRD_MEMBER)
        assert hits == [JOURNALISTS_FILE], hits

    def test_forty_second_intact_in_ft_only(self):
        hits = self._ledger_hits(FORTY_SECOND_MEMBER)
        assert hits == [os.path.join(PROFILES_DIR, "financial-times.yaml")], hits

    def test_forty_first_intact_in_journalists_only(self):
        hits = self._ledger_hits(FORTY_FIRST_MEMBER)
        assert hits == [JOURNALISTS_FILE], hits

    def test_fortieth_intact_in_wired_only(self):
        hits = self._ledger_hits(FORTIETH_MEMBER)
        assert hits == [os.path.join(PROFILES_DIR, "wired.yaml")], hits

    def test_forty_fifth_present_once_in_profiles(self):
        # The affirmative forty-fifth claim is this run's landed block;
        # profiles-scope only (this test file format-builds the needle
        # per #715 and carries no contiguous form).
        hits = self._ledger_hits(FORTY_FIFTH_MEMBER)
        assert hits == [JOURNALISTS_FILE], hits

    def test_forty_sixth_member_absent_repo_wide(self):
        hits = [
            p for p in _iter_source_files()
            if FORTY_SIXTH_MEMBER in _read(p)
        ]
        assert hits == [], hits

    def test_thirty_first_direction_present(self):
        # The THIRTY-FIRST direction lives in competitor-entities.yaml (the
        # #1119 Microsoft/Nine block), not in journalists.yaml.
        text = _read(os.path.join(PROFILES_DIR, "competitor-entities.yaml"))
        assert "THIRTY-FIRST relationship direction" in text

    def test_thirty_second_direction_absent_repo_wide(self):
        hits = [
            p for p in _iter_source_files()
            if THIRTY_SECOND_DIR in _read(p)
        ]
        assert hits == [], hits


# ---------------------------------------------------------------------------
# 12. Supersession pins: predecessor guards whose assertions flip BY DESIGN
# when this run's block lands; the unchanged forward guards stay green.
# ---------------------------------------------------------------------------

class TestSupersessionPins1123:
    def test_1122_novelty_905_numeric_fails_by_design(self):
        # The 905 numeric id now exists in the working-tree profiles/
        # (this run's landed block); fails BY DESIGN post-landing.
        res = _node_run(
            FILE_1122,
            "TestMechanismNovelty1122::test_zero_numeric_905_in_profiles",
        )
        assert res.returncode != 0, res.stdout[-1500:]

    def test_1122_novelty_max_904_fails_by_design(self):
        res = _node_run(
            FILE_1122, "TestMechanismNovelty1122::test_max_numeric_mechanism_id_is_904"
        )
        assert res.returncode != 0, res.stdout[-1500:]

    def test_1122_forty_fifth_absent_fails_by_design(self):
        # The affirmative forty-fifth claim now lives in the working-tree
        # profiles/ (this run's landed block); fails BY DESIGN post-landing.
        res = _node_run(
            FILE_1122,
            "TestFalsificationLedger1122::test_forty_fifth_member_absent_repo_wide",
        )
        assert res.returncode != 0, res.stdout[-1500:]

    def test_1122_underscore_dash_905_still_green(self):
        for node in (
            "TestMechanismNovelty1122::test_zero_underscore_905_repo_wide",
            "TestMechanismNovelty1122::test_zero_dash_905_repo_wide",
        ):
            res = _node_run(FILE_1122, node)
            assert res.returncode == 0, (node, res.stdout[-1500:])

    def test_1122_forty_fourth_intact_still_green(self):
        res = _node_run(
            FILE_1122,
            "TestFalsificationLedger1122::test_forty_fourth_present_once_in_profiles",
        )
        assert res.returncode == 0, res.stdout[-1500:]

    def test_1122_thirty_second_absent_still_green(self):
        res = _node_run(
            FILE_1122,
            "TestFalsificationLedger1122::test_thirty_second_direction_absent_repo_wide",
        )
        assert res.returncode == 0, res.stdout[-1500:]


# ---------------------------------------------------------------------------
# 13. Research method.
# ---------------------------------------------------------------------------

class TestResearchMethod1123:
    def test_six_search_sets(self):
        assert "6 browser.search query sets" in _block()["research_method"]

    def test_zero_browser_open(self):
        rm = _block()["research_method"]
        assert "0 browser.open" in rm
        assert "#503" in rm

    def test_rejected_sources(self):
        rm = _block()["research_method"]
        assert "REJECTED" in rm
        assert "nextunicorn.ventures" in rm
        assert "circular" in rm

    def test_verbatim_urls(self):
        rm = _block()["research_method"]
        assert "verbatim from Full-URL listings" in rm
        assert "no canonical URLs constructed" in rm

    def test_ascii_discipline(self):
        rm = _block()["research_method"]
        assert "ASCII-only" in rm
        assert "no em dashes" in rm


# ---------------------------------------------------------------------------
# 14. Statistical discipline and confounders.
# ---------------------------------------------------------------------------

class TestStatisticalDiscipline1123:
    def test_hypothesis_generating_only(self):
        assert "Hypothesis-generating only" in _block()["statistical_discipline"]

    def test_not_artifact_grade(self):
        sd = _block()["statistical_discipline"]
        assert "NOT artifact-grade" in sd
        assert "no_analysis_json_update true" in sd

    def test_confounder_strengths(self):
        confs = _block()["confounders"]
        strong = [c for c in confs if c.startswith("STRONG")]
        moderate = [c for c in confs if c.startswith("MODERATE")]
        assert len(strong) == 2
        assert len(moderate) == 3
        assert any("news-peg asymmetry" in c for c in strong)
        assert any("desk-role asymmetry" in c for c in strong)

    def test_counterevidence_bounds_claim(self):
        ce = _block()["counterevidence"]
        assert len(ce) == 3
        assert any("entity-neutral" in c for c in ce)
        assert any("m597" in c for c in ce)
        assert any("m904" in c for c in ce)


# ---------------------------------------------------------------------------
# 15. Doc-sync (pre-commit state; SUPERSEDED BY DESIGN post-doc-sync -
# deselect in post-doc-sync full runs per #719).
# ---------------------------------------------------------------------------

class TestDocSync1123:
    def test_readme_test_file_table_has_no_1123_row_pre_commit(self):
        readme = _read(README_PATH)
        assert "test_type_b_1123" not in readme

    def test_architecture_has_no_1123_row_pre_commit(self):
        arch = _read(ARCH_PATH)
        assert "test_type_b_1123" not in arch

    def test_readme_stats_current(self):
        readme = _read(README_PATH)
        assert "| 58487 |" in readme
        assert "1447" in readme


# ---------------------------------------------------------------------------
# 16. Iteration log (pre-commit state; SUPERSEDED BY DESIGN post-doc-sync -
# deselect in post-doc-sync full runs per #719).
# ---------------------------------------------------------------------------

class TestIterationLog1123:
    def test_no_1123_entry_pre_commit(self):
        log = _read(LOG_PATH)
        assert "## #1123 Type B" not in log

    def test_1122_entry_present(self):
        log = _read(LOG_PATH)
        assert "## #1122 Type A" in log

    def test_rotation_transparency_convention(self):
        log = _read(LOG_PATH)
        assert "log-hash followup registers all three hashes" in log


# ---------------------------------------------------------------------------
# 17. In-flight isolation: concurrent runs' uncommitted work is untouched.
# ---------------------------------------------------------------------------

class TestInFlightIsolation1123:
    def test_899_nytimes_hunk_untouched(self):
        res = _git("diff", "--name-only")
        modified = res.stdout.split()
        assert "profiles/nytimes.yaml" in modified
        # Its uncommitted hunk belongs to #899's run; this run stages
        # only its own files.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#899" in src

    def test_938_test_file_edit_owned_by_its_run(self):
        res = _git("status", "--short")
        assert "test_type_b_938" in res.stdout

    def test_900_untracked_file_untouched(self):
        res = _git("status", "--short")
        assert "test_type_d_900_m769" in res.stdout

    def test_1012_working_tree_edit_untouched(self):
        res = _git("status", "--short")
        assert "test_type_a_1012" in res.stdout

    def test_do_not_touch_1024_m846(self):
        # Ray's revert/leave/rebuild decision on #1024's m846 is pending;
        # guarded in the log entry per convention, untouched by this run.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#1024" in src
