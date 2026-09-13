"""Type A #722 (2026-09-13 10:00 PDT): The Atlantic x Google adversarial-posture
litigation-domain boundary replication (mechanism 667) - FIRST dedicated
mechanism under competitor_relationships.google in atlantic.yaml.

The Atlantic sued Google in SDNY on Tue Jan 13 2026 (Case 1:26-cv-00272) for
adtech antitrust violations - "$30 billion from manipulating auctions"
(2022), auction manipulations "inherently unfair," ~40% clearing-price
suppression - while admitting in its complaint that it "cannot forgo the
significant revenue it earns from the Google Ads demand available only
through AdX." coverage_prediction is adversarial. The naive prediction is
adversarial Google coverage across all domains. Observed: the adversarial
posture holds ONLY within the litigation domain.

Google arm (non-litigation, n=2, MANUAL ILLUSTRATIVE): (1) Alex Reisner
AI Watchdog "AI's Memorization Crisis" (Fri Jan 9 2026): Stanford/Yale
study shows four labs' models (OpenAI GPT, Anthropic Claude, Google
Gemini, xAI Grok) store and reproduce large portions of books they trained
on; quotes Google's 2023 letter to the US Copyright Office ("there is no
copy of the training data, whether text, images, or other formats,
present in the model itself") and contradicts it via the study - adversarial
investigation register applied entity-generically, Google one of four, no
entity-targeted Google investigation; mirror-excerpt-bounded
(https://technologiesdigest.com/ais-memorization-crisis-the-atlantic/,
theatlantic.com direct fetch failed this run, terminal tool failure, no
retry per convention); scored -0.45. (2) "Inside the Dirty, Dystopian
World of AI Data Centers" (Apr 2026, Atlantic magazine): xAI Colossus
target; names Amazon, Microsoft, Meta, and Google in the "$600 billion"-
plus capex stack; industry-generic; listing-bounded via
https://web.archive.org/web/20260503001248/https://www.theatlantic.com/magazine/2026/04/ai-data-centers-energy-demands/686064/;
scored -0.10. Google target avg -0.275.

Meta arm (carried in-corpus from mechanism 481, n=2, MANUAL ILLUSTRATIVE):
"Why Would Meta Download So Much Porn?" (Fri Jul 24 2026, AI Watchdog,
Meta named in headline, -0.75) vs "The Unbelievable Scale of AI's
Pirated-Books Problem" (Mar 2025, Meta foregrounded, -0.65). Meta peer
avg -0.70. Delta (Google target minus Meta peer) +0.425. p_value /
cohens_d / ci_95 NOT_CALCULATED, is_significant False per the Aug 28 2026
standing rule; engine NOT run; NOT artifact-grade; no divergence pin.

Verdict: THIRD adversarial-posture litigation-domain boundary replication
pin after #471 (NYT x OpenAI) and #592 (Verge x Google): adversarial
financial posture predicts adversarial tone WITHIN the litigation domain
only; outside it, The Atlantic's non-litigation Google coverage runs less
adversarial than its Meta coverage despite The Atlantic actively suing
Google. NOT a falsification-family member (ledger holds at 24);
boundary family 2->3. directionally_supported_not_proven. Correlation is
not causation.

Bounded absence per the iteration-492 rule: no dedicated Atlantic AI
Watchdog or equivalent accountability investigation isolating Google on
training-data memorization surfaced in bounded searches; no Atlantic
editorial treatment of Google Android XR glasses surfaced in bounded
searches - stated as bounded search-result absence, not a proven zero.

Strongest confounds: (1) entity dilution - Google arm never isolates
Google (one of four labs; one of four in capex stack) while Meta arm is
entity-targeted in the headline; (2) genre skew - investigative feature vs
accountability investigation with entity accusation; (3) news-peg asymmetry -
Meta items rest on filed lawsuits with dramatic court evidence (Strike 3
file-transfer lists, unsealed LibGen comms), Google had no equivalent 2026
accountability news peg. Moderate: OpenAI-licensing cross-incentive (The
Atlantic licenses to OpenAI, Google's direct AI rival - alternative
incentive story not ruled out), timing skew, post-hoc domain definition.
No analysis.json update warranted. No em dashes in any new prose.
"""

import glob
import os
import re
import subprocess

import pytest
import yaml

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
PROFILE_PATH = os.path.join(REPO_ROOT, "profiles", "atlantic.yaml")
LOG_PATH = os.path.join(REPO_ROOT, "iteration-log.md")
TEST_BASENAME = os.path.basename(__file__)
MECH_KEY = (
    "mechanism_667_atlantic_google_adversarial_posture_litigation_domain_boundary_replication_sep13"
)
MEMO_URL = "https://technologiesdigest.com/ais-memorization-crisis-the-atlantic/"
DATACENTERS_URL = (
    "https://web.archive.org/web/20260503001248/"
    "https://www.theatlantic.com/magazine/2026/04/ai-data-centers-energy-demands/686064/"
)
THEWRAP_URL = "https://www.thewrap.com/industry-news/business/the-atlantic-google-alphabet-lawsuit/"
META_PORN_URL = (
    "https://web.archive.org/web/20260724235323/"
    "https://www.theatlantic.com/technology/2026/07/meta-strike-3-porn-lawsuit/688023/"
)


def _read(path):
    with open(path, "r", encoding="utf-8") as fh:
        return fh.read()


def _profile():
    with open(PROFILE_PATH, "r", encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def _google_block():
    return _profile()["competitor_relationships"]["google"]


def _mechanism():
    return _google_block()[MECH_KEY]


def _run_git(*args):
    return subprocess.run(
        ["git", "-C", REPO_ROOT, *args],
        capture_output=True,
        text=True,
        timeout=120,
    )


class TestNovelty722:
    """Iteration 722 is new; mechanism 667 is the next free id."""

    def test_single_type_a_722_file(self):
        matches = glob.glob(os.path.join(REPO_ROOT, "tests", "test_type_a_722*.py"))
        assert len(matches) == 1, "expected exactly this file, got %r" % (matches,)
        assert matches[0].endswith(TEST_BASENAME)

    def test_type_a_722_main_commit_unique(self):
        # Green post-main-commit; novelty verified pre-commit by shell greps
        # (zero test_type_a_722 files, no "Type A #722" in git log, zero
        # mechanism_667 keys repo-wide, max numeric mechanism 666).
        out = _run_git("log", "--format=%s")
        assert out.returncode == 0
        mains = [s for s in out.stdout.splitlines() if s.startswith("Type A #722:")]
        assert len(mains) == 1, "expected exactly one Type A #722 main commit, got %r" % (mains,)

    def test_first_atlantic_google_mechanism(self):
        # Zero mechanism keys under competitor_relationships.google pre-run;
        # this run adds exactly one.
        keys = [k for k in _google_block() if k.startswith("mechanism_")]
        assert keys == [MECH_KEY], keys

    def test_mechanism_id_is_667(self):
        assert _mechanism()["mechanism_id"] == 667
        assert _mechanism()["iteration"] == 722


class TestMechanism722Content:
    def test_pair_and_title(self):
        m = _mechanism()
        assert m["pair"] == "The Atlantic x Google (vs Meta)"
        assert m["iteration_type"] == "A"
        assert m["iteration_time"] == "2026-09-13 10:00 PDT"
        assert m["goal_id"] == "goal_54093bda4145"
        assert m["scheduled_job_id"] == "mediascope-daily-iteration"

    def test_financial_stub_untouched(self):
        g = _google_block()
        assert g["financial_tie"] == "adversarial_litigation"
        assert g["direction"] == "adversarial"
        assert g["coverage_prediction"] == "adversarial"

    def test_google_arm_items(self):
        items = _mechanism()["google_articles"]
        assert len(items) == 2
        assert items[0]["url"] == MEMO_URL
        assert items[0]["tone_MANUAL_ILLUSTRATIVE"] == -0.45
        assert items[0]["evidence_tier"] == "mirror_excerpt_bounded"
        assert items[0]["weekday"] == "Friday"
        assert items[0]["date"] == "2026-01-09"
        assert items[1]["url"] == DATACENTERS_URL
        assert items[1]["tone_MANUAL_ILLUSTRATIVE"] == -0.1
        assert items[1]["evidence_tier"] == "listing_bounded"

    def test_memorization_quotes_verbatim(self):
        item = _mechanism()["google_articles"][0]
        quotes = " ".join(item["key_quotes"])
        assert "Google's Gemini" in quotes
        assert "there is no copy of the training data" in quotes
        assert "there are such copies in AI models" in quotes

    def test_meta_arm_carried(self):
        items = _mechanism()["meta_articles"]
        assert len(items) == 2
        assert items[0]["url"] == META_PORN_URL
        assert items[0]["tone_MANUAL_ILLUSTRATIVE"] == -0.75
        assert items[0]["carried_from"] == "mechanism 481 (in-corpus)"
        assert items[1]["tone_MANUAL_ILLUSTRATIVE"] == -0.65

    def test_no_em_dashes_in_mechanism_prose(self):
        text = yaml.safe_dump(_mechanism(), allow_unicode=False)
        assert "\u2014" not in text
        assert "\u2013" not in text


class TestToneComparison722:
    def test_delta_arithmetic(self):
        tc = _mechanism()["tone_comparison"]
        g = tc["google_target_tones_MANUAL_ILLUSTRATIVE"]
        p = tc["meta_peer_tones_MANUAL_ILLUSTRATIVE"]
        assert g == [-0.45, -0.1]
        assert p == [-0.75, -0.65]
        assert abs(tc["google_target_avg"] - (-0.275)) < 1e-9
        assert abs(tc["meta_peer_avg"] - (-0.7)) < 1e-9
        assert abs(tc["delta_target_minus_peer_MANUAL_ILLUSTRATIVE"] - 0.425) < 1e-9
        assert abs((sum(g) / 2) - (sum(p) / 2) - 0.425) < 1e-9

    def test_statistical_contract_not_calculated(self):
        tc = _mechanism()["tone_comparison"]
        assert tc["p_value"] == "NOT_CALCULATED"
        assert tc["cohens_d"] == "NOT_CALCULATED"
        assert tc["ci_95"] == "NOT_CALCULATED"
        assert tc["is_significant"] is False
        assert tc["artifact_grade"] is False
        assert tc["engine_run"] is False
        assert tc["engine_divergence_pin"] is False
        assert "Do not claim statistical significance" in tc["methodology"]


class TestLitigationDomainAnchor722:
    def test_anchor_fields(self):
        a = _mechanism()["litigation_domain_anchor"]
        assert a["venue"] == "SDNY"
        assert a["case_number"] == "1:26-cv-00272"
        assert a["filed"] == "2026-01-13"
        assert a["weekday_filed"] == "Tuesday"
        assert a["scored"] is False

    def test_anchor_reporting_urls_verbatim(self):
        a = _mechanism()["litigation_domain_anchor"]
        assert THEWRAP_URL in a["reporting"]
        assert any("pressgazette" in u for u in a["reporting"])
        assert any("digiday" in u for u in a["reporting"])
        assert "ppc.land" in a["complaint_pdf"]

    def test_anchor_quotes(self):
        quotes = " ".join(_mechanism()["litigation_domain_anchor"]["key_quotes"])
        assert "$30 billion from manipulating auctions" in quotes
        assert "inherently unfair" in quotes
        assert "cannot forgo the significant revenue" in _mechanism()["litigation_domain_anchor"]["adx_dependency_quote"]


class TestBoundaryFamily722:
    def test_third_boundary_pin_claimed(self):
        m = _mechanism()
        assert m["boundary_family"] == "THIRD adversarial-posture litigation-domain boundary pin"
        refs = " ".join(m["cross_references"])
        assert "mechanism 471" in refs
        assert "mechanism 592" in refs

    def test_not_falsification_member(self):
        m = _mechanism()
        assert m["falsification_family_member"] is False
        assert m["verdict"] == "directionally_supported_not_proven"

    def test_distinct_from_sibling_boundary_pins(self):
        # #471 is NYT x OpenAI (different publication), #592 is Verge x
        # Google (different publication). This is the first Atlantic x
        # Google; the novelty field names the lineage.
        assert "592" in _mechanism()["novelty"] or "Verge" in _mechanism()["novelty"]
        assert "481" in _mechanism()["novelty"]


class TestConfoundersAndCounterevidence722:
    def test_confounders_ranked_3_3_3(self):
        c = _mechanism()["confounders_ranked"]
        assert len(c["strong"]) == 3
        assert len(c["moderate"]) == 3
        assert len(c["weak"]) == 3
        assert "entity dilution" in c["strong"][0].lower()
        assert "genre skew" in c["strong"][1].lower()
        assert "news-peg asymmetry" in c["strong"][2].lower()
        assert "cross-incentive" in c["moderate"][0].lower()
        assert "licenses content to openai" in c["moderate"][0].lower()

    def test_four_counterevidence(self):
        ce = _mechanism()["counterevidence"]
        assert len(ce) == 4
        assert "strongest possible adversarial act" in ce[0]
        assert "entity-diluted, not absent" in ce[1]

    def test_correlational_note_no_causal_claim(self):
        m = _mechanism()
        assert "Correlation is not causation" in m["finding"]
        assert "correlation, not causation" in m["financial_context"].lower() or "Correlation, not causation" in m["financial_context"]


class TestIterationLog722:
    def test_log_has_722_entry(self):
        text = _read(LOG_PATH)
        heads = re.findall(r"(?m)^#(\d+) Type ([A-E]):", text)
        assert ("722", "A") in heads

    def test_log_entry_names_mechanism_667(self):
        text = _read(LOG_PATH)
        head = text.split("#722 Type A:")[1]
        assert "mechanism 667" in head or "mechanism_667" in head

    def test_log_entry_names_boundary_family(self):
        text = _read(LOG_PATH)
        head = text.split("#722 Type A:")[1].split("\n\n\n")[0]
        assert "boundary" in head.lower()


class TestRotationCycleGuard722:
    """Rotation: distinct-mains window test, #716-style.

    Robust to the #678 history artifact and the #565 followup convention:
    first occurrence of each distinct iteration number, newest first.
    """

    ANCHORED_SHA = "f64d154106fcb6a04693cc54454a5a5e4dcf1350"

    @staticmethod
    def _mains():
        out = subprocess.run(
            ["git", "-C", REPO_ROOT, "log", "--format=%s"],
            capture_output=True,
            text=True,
            check=True,
        ).stdout.splitlines()
        seen = set()
        mains = []
        for s in out:
            m = re.match(r"^Type [A-E] #(\d+):", s)
            if m and m.group(1) not in seen:
                seen.add(m.group(1))
                mains.append(s)
        return mains

    def test_window_718_722_closes_e_to_a(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m, "unparseable rotation subject: %r" % (s,)
            observed.append((m.group(1), m.group(2)))
        assert observed == [
            ("A", "722"),
            ("E", "721"),
            ("D", "720"),
            ("C", "719"),
            ("B", "718"),
        ], "rotation window 718-722 wrong: %r" % (observed,)

    def test_rotation_adjacency_cycle_valid(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m
            observed.append(m.group(1))
        assert observed == ["A", "E", "D", "C", "B"]
        order = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
        for newer, older in zip(observed, observed[1:]):
            assert (order[newer] - order[older]) % 5 == 1, (
                "rotation broken: %s (older) -> %s (newer) is not a valid cycle edge" % (older, newer)
            )

    def test_anchor_is_main_commit_patched_in_followup(self):
        """Rotation window 718-722 closes E->A. Anchor patched in followup per #565."""
        result = _run_git("log", "--format=%H %s")
        assert result.returncode == 0
        mains = [
            line for line in result.stdout.splitlines() if "Type A #722:" in line
        ]
        main = mains[0].split()[0] if mains else ""
        assert self.ANCHORED_SHA == main, (
            "anchor patched in followup per #565 convention"
        )


class TestDocSync722:
    def test_readme_has_row(self):
        text = _read(os.path.join(REPO_ROOT, "README.md"))
        assert TEST_BASENAME in text

    def test_architecture_has_row(self):
        text = _read(os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md"))
        assert TEST_BASENAME in text


class TestSweepSupersession722:
    """Pins the post-#722 state: max mechanism_id 667; ledger holds at 24."""

    def test_max_mechanism_id_is_667(self):
        text = _read(PROFILE_PATH)
        ids = [int(x) for x in re.findall(r"mechanism_id:\s*(\d+)\b", text)]
        modern = [i for i in ids if i >= 600]
        assert max(modern) == 667, max(modern)

    def test_zero_mechanism_668_keys_repo_wide(self):
        for root, _, files in os.walk(os.path.join(REPO_ROOT, "profiles")):
            for f in files:
                if f.endswith((".yaml", ".yml")):
                    t = _read(os.path.join(root, f))
                    assert "mechanism_668" not in t, f

    def test_zero_mechanism_667_keys_in_other_test_files(self):
        # Own file excluded from the sweep per the #715 pattern-rescope
        # lesson: MECH_KEY legitimately names mechanism_667 here.
        # #720's sweep prose ("zero mechanism_667 keys") legitimately
        # mentions the string and fails by designed supersession per the
        # #710 convention; this sweep targets actual mechanism KEY
        # definitions (mechanism_667_<identifier>), not mentions.
        key_re = re.compile(r"\bmechanism_667_[a-z0-9_]")
        for f in glob.glob(os.path.join(REPO_ROOT, "tests", "test_*.py")):
            if os.path.basename(f) == TEST_BASENAME:
                continue
            assert not key_re.search(_read(f)), f

    def test_exactly_one_mechanism_667_key_under_google(self):
        text = _read(PROFILE_PATH)
        keys = re.findall(r"(?m)^    mechanism_667_\w+:", text)
        assert keys == [
            "    mechanism_667_atlantic_google_adversarial_posture_litigation_domain_boundary_replication_sep13:"
        ], keys

    def test_falsification_ledger_holds_at_24(self):
        texts = []
        for root, _, files in os.walk(os.path.join(REPO_ROOT, "profiles")):
            for f in files:
                if f.endswith((".yaml", ".yml")):
                    texts.append(_read(os.path.join(root, f)))
        corpus = "\n".join(texts)
        assert "TWENTY-FOURTH" in corpus
        assert "TWENTY-FIFTH" not in corpus
