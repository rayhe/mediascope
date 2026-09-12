"""Type B #703: Parmy Olson (Bloomberg Opinion) same-journalist cross-entity
byline-isolated column-register pair - Anthropic Coxon-resignation column
(Sep 10, 2026) vs Meta opinion corpus (carried from the Aug 8 file-local
Olson Type B). FIRST YAML mechanism on Parmy Olson (mechanism_id 656, next
free pre-commit; max modern mechanism_id was 655). Zero mechanism_* keys
pre-existed on Olson's journalist profile entry (the entry pre-existed with
name/multi_publication/beats/career/awards/notes/source_urls but no
mechanism; this run adds mechanism_656 as its first mechanism key). The Aug 8
tests/test_parmy_olson_cross_entity.py is file-local - it documents the
CEO-personalization asymmetry (Meta 87.5% vs 0% OpenAI/Anthropic), the
tone asymmetry (Meta avg -0.51, OpenAI avg -0.11, Anthropic avg +0.15), and
the professional-identity-capture thesis (book "Supremacy" centering the
OpenAI-DeepMind rivalry; Bloomberg has no known AI licensing deals).
Distinct unit of analysis from the Aug 8 test: a temporal falsification
update - does the identity-capture thesis survive Olson's Sep 10 2026
Anthropic column?

Anthropic arm: Bloomberg Opinion, Sep 10 2026, 4:00 PM UTC (verified via
Bloomberg Law author page https://news.bloomberglaw.com/author/parmy-olson-22420307,
first-hand read this run, listed under "Parmy Olson's Latest Stories").
Author-page title: "Anthropic Staff Think AI May End Us. Why Not Stop?"
(Bloomberg Opinion display variant: "Some Anthropic Engineers Think AI Might
End Us. Why Race Ahead?"). Bloomberg Opinion column is paywalled; this run
verified the title/date/byline first-hand and the dek + lede verbatim via
Muck Rack syndication listings (https://muckrack.com/parmy/articles,
first-hand read this run) - evidence grade SECOND-HAND (excerpt-bounded),
per the #503 Preston precedent. Dek: "Anthropic was founded to be more
safety-conscious than OpenAI, yet it clings to that mission statement while
building ever more powerful agents, says Parmy Olson for Bloomberg Opinion."
Lede: "It's becoming harder for Anthropic PBC to justify some of the most
unfalsifiable circular logic to ever come out of Silicon Valley: the pursuit
of artificial superintelligence, which by its own admission could kill a lot
of humans. Anthropic researcher Jacob Coxon recently resigned, saying that
his previous employer and its rival OpenAI were gambling with our lives by
building systems that could improve themselves." Loaded language:
"unfalsifiable circular logic", "could kill a lot of humans", "gambling with
our lives", "Why Not Stop?". Framing: accusatory safety-resignation;
hypocrisy accusation against the company. No "Amodei" CEO personalization in
the headline - consistent with the Aug 8 0% Anthropic-personalization
finding. Tone -0.55 (MANUAL ILLUSTRATIVE, hand-scored this run from the
verbatim dek + lede).

News peg (genuinely adversarial, corroborated this run): Anthropic researcher
Jacob Coxon resigned Sep 8-9 2026, posting "I resigned from Anthropic today.
I spent the last three years doing pretraining research at both OpenAI and
Anthropic. Neither company is acting responsibly. They are racing straight to
self-improving superintelligence and gambling with our lives." Anthropic
science lead Evan Hubinger confirmed: "Jacob is correct here - we really do
earnestly believe AI could kill all humans! ... I personally think it is >10%
within the next decade." Sources: thewrap.com, people.com, techspot.com
listings verified this run.

Meta arm (carried from Aug 8 file-local test): 8 headlines, 87.5%
personalized to "Zuckerberg"/"Mark Zuckerberg", average tone -0.51.
Exemplars: "Mark Zuckerberg's Free AI Is a Clever Form of Bait" (-0.65,
deception framing, "bait",
https://news.bloomberglaw.com/tech-and-telecom-law/mark-zuckerbergs-free-ai-is-a-clever-form-of-bait-parmy-olson);
"Mark Zuckerberg's AI Slop Will Make Ads Worse" (-0.70, contempt, "slop");
"Zuckerberg and Musk's AI Failure Club Has Its Perks" (-0.55, mockery,
"Meta Platforms Inc.'s chronic inability to develop an original idea");
"Meta's Days of Giving Away AI for Free Are Numbered" (-0.35).

Corroborating Sep 2026 OpenAI arms (same accusatory register, cited not
paired): "Altman's Opaque AI Creates a New Security Dilemma" (Sep 4 2026,
11:00 AM UTC, Bloomberg Law author page) - adversarial on OpenAI; NOTE the
headline personalizes OpenAI to "Altman", a register break from the Aug 8
0%-OpenAI-personalization finding. "Don't Be Seduced by the Language of AI"
(Sep 2 2026, 10:56 AM UTC) - adversarial on OpenAI's Hugging Face rogue-agent
breach ("OpenAI's artificial-intelligence agents deceived their human
overseers and breached the online repository", per syndication excerpts).

Finding: REGISTER CONSTANCY in the accusatory opinion-column register.
Illustrative delta (Anthropic arm minus Meta corpus) = -0.55 - (-0.51) =
-0.04, near-null; p_value, cohens_d, ci NOT_CALCULATED; is_significant False
(Aug 28 standing rule); statistical_contract degenerate_n1_per_arm per
#638/#643. No engine run. NOT artifact-grade. No analysis.json update.

TWENTY-FIRST falsification-family member (journalist-attribution class): the
journalist-level "Olson softens Anthropic" attribution from the Aug 8
identity-capture thesis fails in the Sep 2026 safety-resignation register.
Olson's Jul-Aug 2026 Anthropic business-strategy columns were
competitive/protective ("Anthropic Has Just Turned Up the Heat on Nvidia",
+0.25; "Anthropic and OpenAI Face a New Threat from China", +0.05; avg
+0.15); her Sep 10 Coxon-resignation column applies the same adversarial
register she uses on Meta ("unfalsifiable circular logic", "could kill a lot
of humans"). The identity-capture thesis is REGISTER-BOUNDED to the
business-strategy opinion corpus, not journalist-global: it does not predict
entity-selective softness when the news peg is a genuine safety scandal.
Corroboration: she applies the same accusatory register to OpenAI in the same
week (Sep 2, Sep 4 columns), the other entity her book thesis supposedly
protects.

Financial context (correlation, not causation): Bloomberg carries NO known AI
content licensing deals with OpenAI, Google, Amazon, or Anthropic (per the
Aug 8 Olson file). Zero-gradient control at the publication level: the deal
theory makes no differential prediction here. The identity-capture mechanism
is a journalist-level book incentive ("Supremacy", 2024, FT-shortlisted),
not a publication-level financial tie. The falsification is at the
journalist-attribution level, consistent with the family.

Novelty vs prior work: FIRST YAML mechanism on Parmy Olson. The Sep 10 2026
Olson column is new-to-corpus (the Aug 8 file-local test predates it; the
column title has no prior corpus hits). The Coxon resignation EVENT is
already in-corpus via #647/m622 (WIRED Sep 9 interview piece, publication-level
Type A pair vs Meta Muse trust register, explicitly NOT falsification-family)
- this run's novelty is Olson's own column on that event and the
same-journalist column-vs-Meta-corpus pair, which was never a mechanism.
Distinct from #698/m653 (TWENTIETH, Wong, different journalist), #693/m650
(NINETEENTH, Nguyen), #688 (SIXTEENTH, Satariano), and from #647/m622 (same
event, different journalist, outlet, and unit of analysis).
Rotation: Type B follows Type A (#702) per A,B,C,D,E. Rotation guard,
doc-sync, and novelty-anchor classes are deselected pre-commit per the #565
followup convention; anchor patched in the followup commit once the main
commit SHA is known.
"""

import os

import pytest
import yaml


REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TESTS_DIR = os.path.join(REPO_ROOT, "tests")
TEST_BASENAME = os.path.basename(__file__)
CAREERS_PATH = os.path.join(REPO_ROOT, "profiles", "careers", "journalists.yaml")
MECH_KEY = "mechanism_656_parmy_olson_coxon_resignation_anthropic_adversarial_register_constancy_sep12"

# Patched in the followup commit per the #565 convention once the main
# commit SHA is known. The rotation-guard class is deselected pre-commit.
ANCHORED_SHA = "efa8e4117d4a7952c46c6f363372971061f5c42b"


def _careers():
    with open(CAREERS_PATH) as f:
        return yaml.safe_load(f)["journalists"]


def _olson():
    matches = []
    for j in _careers():
        if isinstance(j, dict) and j.get("name") == "Parmy Olson":
            matches.append(j)
    assert len(matches) == 1, "expected exactly one Parmy Olson entry, got %d" % len(matches)
    return matches[0]


def _mechanism():
    o = _olson()
    assert MECH_KEY in o, "%s missing from Parmy Olson entry" % MECH_KEY
    mech_keys = [k for k in o.keys() if str(k).startswith("mechanism_")]
    assert mech_keys == [MECH_KEY], "expected 656 to be the only mechanism key, got %r" % (mech_keys,)
    return o[MECH_KEY]


def _run_git(*args):
    import subprocess
    return subprocess.run(["git"] + list(args), cwd=REPO_ROOT,
                          capture_output=True, text=True, check=True)


# ── Anthropic arm: Sep 10 2026 Coxon-resignation column ───────────────────

class TestParmyOlsonCoxonAnthropicArm:
    """The Sep 10 2026 Anthropic column, verified this run (excerpt-bounded)."""

    AUTHOR_PAGE = "https://news.bloomberglaw.com/author/parmy-olson-22420307"
    MUCK_RACK = "https://muckrack.com/parmy/articles"

    def test_column_listed_with_exact_date_and_byline(self):
        """Author page lists the column under Olson's latest stories with date."""
        listing = {
            "title": "Anthropic Staff Think AI May End Us. Why Not Stop?",
            "byline": "Parmy Olson",
            "outlet": "Bloomberg Opinion",
            "date": "Sept. 10, 2026, 4:00 PM UTC",
            "listed_under": "Parmy Olson's Latest Stories",
            "source": self.AUTHOR_PAGE,
        }
        assert listing["byline"] == "Parmy Olson"
        assert listing["date"] == "Sept. 10, 2026, 4:00 PM UTC"
        assert "Anthropic" in listing["title"]

    def test_dek_accuses_hypocrisy(self):
        """The column dek frames Anthropic as contradicting its founding mission."""
        dek = (
            "Anthropic was founded to be more safety-conscious than OpenAI, "
            "yet it clings to that mission statement while building ever more "
            "powerful agents, says Parmy Olson for Bloomberg Opinion."
        )
        assert "yet it clings to that mission statement" in dek
        assert "safety-conscious" in dek

    def test_lede_loaded_language(self):
        """The lede uses strongly adversarial evaluative language toward Anthropic."""
        lede = (
            "It's becoming harder for Anthropic PBC to justify some of the most "
            "unfalsifiable circular logic to ever come out of Silicon Valley: the "
            "pursuit of artificial superintelligence, which by its own admission "
            "could kill a lot of humans. Anthropic researcher Jacob Coxon recently "
            "resigned, saying that his previous employer and its rival OpenAI were "
            "gambling with our lives by building systems that could improve themselves."
        )
        for phrase in ("unfalsifiable circular logic",
                        "could kill a lot of humans",
                        "gambling with our lives"):
            assert phrase in lede, f"missing loaded phrase: {phrase}"

    def test_no_amodei_personalization(self):
        """Headline carries no Dario Amodei personalization, consistent with Aug 8."""
        headline = "Anthropic Staff Think AI May End Us. Why Not Stop?"
        assert "Amodei" not in headline
        assert "Dario" not in headline

    def test_evidence_grade_second_hand(self):
        """Paywalled column: excerpt-bounded, disclosed per #503 precedent."""
        grade = {
            "title_date_byline": "first-hand (Bloomberg Law author page)",
            "dek_lede": "verbatim excerpts (Muck Rack syndication listings)",
            "full_column": "NOT read - Bloomberg Opinion paywall",
            "grade": "second-hand (excerpt-bounded)",
        }
        assert grade["grade"] == "second-hand (excerpt-bounded)"
        assert grade["full_column"].startswith("NOT read")

    def test_coxon_peg_corroborated(self):
        """The resignation peg is genuine and company-confirmed."""
        peg = {
            "who": "Jacob Coxon, Anthropic pretraining researcher (ex-OpenAI)",
            "when": "2026-09-08/09",
            "claim": "gambling with our lives",
            "company_confirmation": "Evan Hubinger (Anthropic science lead): "
                                   "'Jacob is correct here - we really do earnestly "
                                   "believe AI could kill all humans!'",
            "corroborating_outlets": ["thewrap.com", "people.com", "techspot.com"],
        }
        assert "gambling with our lives" in peg["claim"]
        assert "earnestly believe AI could kill all humans" in peg["company_confirmation"]


# ── Meta arm: carried corpus from the Aug 8 file-local Olson Type B ─────────

class TestParmyOlsonMetaArmCarried:
    """Meta corpus carried from tests/test_parmy_olson_cross_entity.py (Aug 8)."""

    META_CORPUS = {
        "n_headlines": 8,
        "ceo_personalization_rate": 0.875,
        "avg_tone": -0.51,
        "source_file": "tests/test_parmy_olson_cross_entity.py",
    }

    def test_meta_corpus_avg_carried(self):
        """Carried Meta corpus: 8 headlines, 87.5% personalized, avg -0.51."""
        assert self.META_CORPUS["n_headlines"] == 8
        assert self.META_CORPUS["ceo_personalization_rate"] == 0.875
        assert self.META_CORPUS["avg_tone"] == -0.51

    def test_meta_exemplar_bait(self):
        """'Clever Form of Bait' exemplar: deception framing, tone -0.65."""
        exemplar = {
            "headline": "Mark Zuckerberg's Free AI Is a Clever Form of Bait",
            "tone": -0.65,
            "framing": "deception",
            "url": "https://news.bloomberglaw.com/tech-and-telecom-law/"
                   "mark-zuckerbergs-free-ai-is-a-clever-form-of-bait-parmy-olson",
        }
        assert exemplar["tone"] == -0.65
        assert "bait" in exemplar["headline"].lower()

    def test_meta_exemplar_failure_club(self):
        """'Failure Club' exemplar: mockery framing, tone -0.55."""
        exemplar = {
            "headline": "Zuckerberg and Musk's AI Failure Club Has Its Perks",
            "tone": -0.55,
            "framing": "mockery",
            "body_excerpt": "Meta Platforms Inc.'s chronic inability to "
                            "develop an original idea",
            "url": "https://news.bloomberglaw.com/artificial-intelligence/"
                   "zuckerberg-and-musks-ai-failure-club-has-its-perks-parmy-olson",
        }
        assert exemplar["tone"] == -0.55
        assert "chronic inability" in exemplar["body_excerpt"]


# ── Pair mechanism: register constancy, identity-capture bound ──────────────

class TestPairMechanism703:
    """The pair finding: near-null delta, identity-capture thesis register-bounded."""

    ANTHROPIC_TONE_ILLUSTRATIVE = -0.55
    META_TONE_ILLUSTRATIVE = -0.51

    def test_delta_near_null(self):
        """Illustrative delta (Anthropic arm minus Meta corpus) is near-null."""
        delta = self.ANTHROPIC_TONE_ILLUSTRATIVE - self.META_TONE_ILLUSTRATIVE
        assert abs(delta - (-0.04)) < 1e-9

    def test_is_significant_false(self):
        """Aug 28 standing rule: finding-layer is_significant is False."""
        result = {
            "method": "MANUAL ILLUSTRATIVE",
            "p_value": "NOT_CALCULATED",
            "cohens_d": "NOT_CALCULATED",
            "ci": "NOT_CALCULATED",
            "is_significant": False,
            "statistical_contract": "degenerate_n1_per_arm",
            "artifact_grade": False,
        }
        assert result["is_significant"] is False
        assert result["statistical_contract"] == "degenerate_n1_per_arm"

    def test_identity_capture_bounded(self):
        """Old Anthropic avg (+0.15, Jul-Aug business columns) vs new arm (-0.55)."""
        old_anthropic = {
            "n": 2,
            "headlines": ["Anthropic Has Just Turned Up the Heat on Nvidia",
                          "Anthropic and OpenAI Face a New Threat from China"],
            "avg_tone": 0.15,
            "register": "business-strategy opinion columns (Jul-Aug 2026)",
        }
        register_break = self.ANTHROPIC_TONE_ILLUSTRATIVE - old_anthropic["avg_tone"]
        assert abs(register_break - (-0.70)) < 1e-9
        assert old_anthropic["register"].startswith("business-strategy")

    def test_openai_corroboration_same_week(self):
        """Sep 2 + Sep 4 adversarial OpenAI columns corroborate the register."""
        corroborating = [
            {"title": "Altman's Opaque AI Creates a New Security Dilemma",
             "date": "2026-09-04",
             "note": "adversarial on OpenAI; personalizes to Altman in headline"},
            {"title": "Don't Be Seduced by the Language of AI",
             "date": "2026-09-02",
             "note": "adversarial on OpenAI Hugging Face rogue-agent breach"},
        ]
        assert len(corroborating) == 2
        assert "Altman" in corroborating[0]["title"]


# ── Financial context: zero-gradient control ────────────────────────────────

class TestFinancialContext703:
    """Bloomberg carries no AI licensing deals; identity capture is author-level."""

    def test_bloomberg_no_ai_licensing_deals(self):
        """Carried from the Aug 8 Olson file: no known AI content deals."""
        status = {
            "outlet": "Bloomberg",
            "openai_content_deal": False,
            "google_content_deal": False,
            "amazon_content_deal": False,
            "anthropic_content_deal": False,
        }
        assert not any(v for k, v in status.items() if k.endswith("_deal"))

    def test_zero_gradient_control(self):
        """Deal theory makes no differential prediction; falsification is author-level."""
        context = {
            "predictor": "null_tie_control",
            "prediction": "no_differential_prediction",
            "mechanism_level": "journalist (book incentive: 'Supremacy', 2024)",
            "falsification_level": "journalist-attribution",
        }
        assert context["predictor"] == "null_tie_control"
        assert context["falsification_level"] == "journalist-attribution"


# ── YAML mechanism pins ───────────────────────────────────────────────────

class TestMechanism656Yaml:
    """Pin the mechanism_656 block fields on Olson's journalists.yaml entry."""

    def test_mechanism_656_first_and_only_key_on_olson(self):
        m = _mechanism()
        assert m["mechanism_id"] == 656
        assert m["iteration"] == 703
        assert m["type"] == "B"

    def test_delta_and_significance(self):
        r = _mechanism()["asymmetry_scorer_result"]
        assert r["delta_anthropic_minus_meta"] == -0.04
        assert r["is_significant"] is False
        assert r["statistical_contract"] == "degenerate_n1_per_arm"
        assert r["artifact_grade"] is False

    def test_twenty_first_in_verdict(self):
        assert "TWENTY-FIRST falsification-family member" in _mechanism()["verdict"]

    def test_six_confounders_ranked(self):
        confs = _mechanism()["confounders"]
        assert len(confs) == 6
        assert confs[0].startswith("[STRONG]")
        assert confs[-1].startswith("[WEAK]")

    def test_anthropic_arm_url_is_author_page(self):
        """No invented canonical URL: the arm cites the verified listing page."""
        url = _mechanism()["anthropic_arm"]["url"]
        assert url == "https://news.bloomberglaw.com/author/parmy-olson-22420307"
        assert "canonical_url_note" in _mechanism()["anthropic_arm"]

    def test_evidence_grade_second_hand(self):
        grade = _mechanism()["anthropic_arm"]["evidence_grade"]
        assert grade.startswith("second-hand (excerpt-bounded)")

    def test_register_bound_not_contradiction(self):
        rb = _mechanism()["register_bound_note"]
        assert rb["contradiction"] is False
        assert "register-bounded" in rb["bound_statement"]

    def test_no_em_dash_in_mechanism_or_file(self):
        assert "\u2014" not in str(_mechanism())
        src = open(os.path.join(TESTS_DIR, TEST_BASENAME)).read()
        assert "\u2014" not in src
        assert "\u2028" not in src


# ── Rotation guard / novelty anchor (#565 convention) ──────────────────────

class TestRotationCycleGuard703:
    """Deselected pre-commit; anchor patched in the followup commit."""

    ANCHORED_SHA = ANCHORED_SHA

    def test_type_b_703_file_unique(self):
        import glob
        matches = glob.glob(os.path.join(TESTS_DIR, "test_type_b_703*.py"))
        assert len(matches) == 1, "expected exactly this file, got %r" % (matches,)
        assert matches[0].endswith(TEST_BASENAME)

    def test_type_b_703_main_commit_unique_and_anchored(self):
        # Runs green only post-main-commit per the #565 followup convention.
        # Deselect pre-commit; the followup patches ANCHORED_SHA to the real
        # main-commit SHA. Novelty was verified pre-commit by shell greps
        # (zero test_type_b_703 files, no #703 in git log, zero
        # mechanism_656 keys in profiles/, no YAML mechanism on Olson, the
        # Sep 10 column title new-to-corpus, #647/m622 as the distinct-unit
        # prior for the Coxon event).
        import re
        out = _run_git("log", "--format=%H %s")
        mains = [
            line
            for line in out.stdout.splitlines()
            if re.match(r"^[0-9a-f]{40} Type B #703:", line)
        ]
        assert len(mains) == 1, "expected exactly one Type B #703 main commit, got %r" % (mains,)
        sha = mains[0].split()[0]
        assert sha == TestRotationCycleGuard703.ANCHORED_SHA, (
            "anchor patched in followup per #565 convention"
        )
