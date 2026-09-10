"""Type B #658: Reece Rogers (WIRED) same-day register asymmetry.

FIRST dedicated Type B mechanism on Reece Rogers (mechanism_id 629, next
free pre-commit; max numeric mechanism_id was 628). Prior repo presence is
only mechanism_431_crossref_boone_ashworth (co-author context) plus
wired.yaml publication-level Rogers coverage notes. New angle, new arms:

(a) Meta arm: Jul 7 2026 WIRED "Meta Now Lets Anyone Use Your Instagram
Photos in AI Images, Unless You Opt Out" (byline Reece Rogers per his Muck
Rack profile). Register = opt-out alarm / consent-violation: "public
Instagram profiles are now automatically opted into being fodder for
generative AI remixes", "tag your account's profile in a prompt ... and
they can use Meta AI to generate an image using your likeness", plus the
how-to-opt-out service walkthrough ("Allow people to use your content on
Instagram and with AI features on Meta"). Tone -0.45 hand-assigned this run
(MANUAL ILLUSTRATIVE). Snippet-bounded via Muck Rack snippets plus verbatim
mirror reprints (WIRED paywalled, not opened first-hand this run). Within
three days Meta removed the feature amid CAA/SAG-AFTRA backlash, which
vindicates the alarm and strengthens the news-peg confound.

(b) Anthropic arm: Jul 7 2026 WIRED "Shut Those Laptops! Anthropic Puts Its
Claude Cowork Agent on Your Phone" (byline Reece Rogers per his Muck Rack
profile; Tuesday July 7 2026 06:00 PM per en.zicos.com mirror). Register =
playful product enthusiasm: "Shut Those Laptops!", "The era of
half-cracking a laptop to keep AI agents running comes to a close", with
ZERO alarm vocabulary despite Cowork pulling data from "email threads,
Slack channels, meeting transcripts, and recent online chatter". Tone +0.10
hand-assigned this run (MANUAL ILLUSTRATIVE). Snippet-bounded via Muck Rack
snippets plus verbatim mirror reprints.

Finding: gradient-consistent but peg-confounded register asymmetry. Same
journalist, SAME day (both Tuesday July 7 2026), same AI-product category:
Meta gets the consent-violation alarm register, Anthropic gets the playful
product-enthusiasm register with zero alarm vocabulary on an agent that
ingests email, Slack, and meeting transcripts. Directionally consistent with
the Conde Nast competitor-payment gradient (Anthropic is a Meta
competitor; Meta pays $0), but the STRONG news-peg confound (a genuine
default-opt-in likeness-harvesting policy, vindicated by Meta's 3-day
reversal under CAA/SAG-AFTRA pressure) bounds the entity-bias reading.
NOT a falsification-family member. NOT a pure asymmetry pin. Correlation
only, not causation. NOT a causal claim about editorial influence.

Illustrative delta (Anthropic minus Meta) = 0.10 - (-0.45) = +0.55;
p_value, cohens_d, ci_95 NOT_CALCULATED; is_significant False (Aug 28
standing rule); statistical_contract degenerate_n1_per_arm.

Novelty vs prior work: FIRST dedicated Type B on Reece Rogers; the Claude
Cowork Jul 7 2026 piece is new-to-corpus (zero mechanism references
pre-commit); the Muse Image piece existed only at publication level
(wired.yaml notes) never in a same-journalist cross-entity mechanism. A
same-day same-journalist same-category pair is a first for the corpus.
Distinct from #648 (Paresh Dave, different journalist, actor-selection
angle, mechanism 623) and #653 (Robert Hart, different publication,
Muse-agent launch not Muse Image).

Rotation: Type B follows Type A (#657) per A,B,C,D,E. Rotation guard
deselected pre-commit per the #565 followup convention; anchor patched in
the followup commit once the main commit SHA is known.
"""

import ast
import glob
import os
import re
import subprocess

import pytest
import yaml

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CAREERS_PATH = os.path.join(REPO_ROOT, "profiles", "careers", "journalists.yaml")
README_PATH = os.path.join(REPO_ROOT, "README.md")
ARCH_PATH = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")
TESTS_DIR = os.path.join(REPO_ROOT, "tests")
LOG_PATH = os.path.join(REPO_ROOT, "iteration-log.md")

MECH_KEY = "mechanism_629_reece_rogers_muse_image_opt_out_alarm_vs_claude_cowork_playful_register_jul07"
FILENAME = "test_type_b_658_reece_rogers_muse_image_opt_out_alarm_vs_claude_cowork_playful_register_sep10_3pm.py"

META_TONE = -0.45
ANTHROPIC_TONE = 0.10
EXPECTED_DELTA = 0.55

META_URLS = [
    "https://www.wired.com/story/meta-now-lets-anyone-use-your-instagram-photos-in-ai-images-unless-you-opt-out/",
    "https://technologistmag.com/meta-now-lets-anyone-use-your-instagram-photos-in-ai-images-unless-you-opt-out/",
    "https://technewsvision.co.uk/meta-now-lets-anyone-use-your-instagram-photos-in-ai-images-unless-you-opt-out/",
    "https://www.ohiosap.org/news/meta-now-lets-anyone-use-your-instagram-photos-in-ai-images",
    "https://tech.slashdot.org/story/26/07/07/2239255/meta-now-lets-anyone-use-your-instagram-photos-in-ai-images",
]
ANTHROPIC_URLS = [
    "https://www.wired.com/story/shut-those-laptops-anthropic-puts-its-claude-cowork-agent-on-your-phone/",
    "https://thetechstreetnow.com/shut-those-laptops-anthropic-puts-its-claude-cowork-agent-on-your-phone/",
    "https://newsheadlinealert.com/news/shut-those-laptops-anthropic-puts-its-claude-cowork-agent-on-your-phone-6a4d6801e8fdc",
    "https://aibreaking.news/news/shut-those-laptops-anthropic-puts-its-claude-cowork-agent-on-your-phone",
]

# Patched in the followup commit per the #565 convention once the main
# commit SHA is known. The rotation-guard class is deselected pre-commit.
ANCHORED_SHA = "954011b"


def _careers():
    with open(CAREERS_PATH) as f:
        return yaml.safe_load(f)


def _rogers():
    matches = []
    for j in _careers()["journalists"]:
        if isinstance(j, dict) and j.get("name") == "Reece Rogers":
            matches.append(j)
    assert len(matches) == 1, f"expected exactly one Reece Rogers entry, got {len(matches)}"
    return matches[0]


def _mechanism():
    rogers = _rogers()
    assert MECH_KEY in rogers, f"{MECH_KEY} missing from Reece Rogers entry"
    return rogers[MECH_KEY]


def _mechanism_text():
    return yaml.safe_dump(_mechanism(), allow_unicode=True)


def _count_def_tests():
    path = os.path.join(TESTS_DIR, FILENAME)
    tree = ast.parse(open(path).read())
    return sum(
        isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))
        and n.name.startswith("test_")
        for n in ast.walk(tree)
    )


def read_readme():
    with open(README_PATH) as f:
        return f.read()


def read_arch():
    with open(ARCH_PATH) as f:
        return f.read()


class TestIterationMetadata658:
    def test_iteration_number(self):
        assert _mechanism()["iteration"] == 658

    def test_mechanism_id_next_free(self):
        assert _mechanism()["mechanism_id"] == 629

    def test_mechanism_id_unique_repo_wide(self):
        seen = {}
        for path in glob.glob(os.path.join(REPO_ROOT, "profiles", "**", "*.yaml"), recursive=True):
            text = open(path, encoding="utf-8", errors="replace").read()
            for m in re.finditer(r"mechanism_id:\s*(\d+)", text):
                if int(m.group(1)) == 629:
                    seen.setdefault(629, []).append(path)
        assert len(seen.get(629, [])) == 1, f"mechanism_id 629 not unique: {seen.get(629)}"

    def test_type_is_b(self):
        assert _mechanism()["type"] == "B"

    def test_goal_and_job_ids(self):
        m = _mechanism()
        assert m["goal_id"] == "goal_54093bda4145"
        assert m["job_id"] == "mediascope-daily-iteration"
        assert m["scheduled_job_id"] == "mediascope-daily-iteration"

    def test_block_key_matches(self):
        assert _mechanism()["block_key"] == "type_b_658_reece_rogers_muse_image_opt_out_alarm_vs_claude_cowork_playful_register_jul07"

    def test_first_dedicated_type_b_on_rogers(self):
        rogers = _rogers()
        assert "mechanism_431_crossref_boone_ashworth" in rogers, \
            "mechanism 431 cross-ref context must still be present as prior context"
        dedicated = [k for k in rogers
                     if k.startswith("mechanism_") and "crossref" not in k and "cross_ref" not in k]
        assert dedicated == [MECH_KEY], \
            f"expected exactly one dedicated Rogers mechanism, got {dedicated}"

    def test_no_duplicate_658_file(self):
        others = [p for p in glob.glob(os.path.join(TESTS_DIR, "test_type_b_658_*.py"))
                  if os.path.basename(p) != FILENAME]
        assert not others, f"duplicate #658 test files: {others}"


class TestRogersArms658:
    def test_meta_arm_date_and_byline(self):
        meta = _mechanism()["meta_arm"]
        assert meta["date"] == "2026-07-07"
        assert "Reece Rogers" in meta["piece"]
        assert "WIRED" in meta["piece"]

    def test_meta_arm_urls_verbatim(self):
        urls = _mechanism()["meta_arm"]["source_urls"]
        for u in META_URLS:
            assert u in urls, f"meta URL missing: {u}"

    def test_meta_arm_opt_out_quotes(self):
        quotes = _mechanism()["meta_arm"]["evidence_quotes"]
        assert any("inaugural AI image model" in q for q in quotes)
        assert any("fodder for generative AI remixes" in q for q in quotes)
        assert any("tag your account" in q for q in quotes)
        assert any("Allow people to use your content" in q for q in quotes)

    def test_meta_arm_register_is_opt_out_alarm(self):
        assert _mechanism()["meta_arm"]["register"] == "opt_out_alarm"

    def test_meta_arm_aftermath_vindication(self):
        aftermath = _mechanism()["meta_arm"]["aftermath"]
        assert "three days" in aftermath
        assert "CAA" in aftermath

    def test_anthropic_arm_date_and_byline(self):
        anth = _mechanism()["anthropic_arm"]
        assert anth["date"] == "2026-07-07"
        assert "Reece Rogers" in anth["piece"]
        assert "WIRED" in anth["piece"]

    def test_anthropic_arm_urls_verbatim(self):
        urls = _mechanism()["anthropic_arm"]["source_urls"]
        for u in ANTHROPIC_URLS:
            assert u in urls, f"anthropic URL missing: {u}"

    def test_anthropic_arm_playful_quotes(self):
        quotes = _mechanism()["anthropic_arm"]["evidence_quotes"]
        assert any("Shut Those Laptops" in q for q in quotes)
        assert any("half-cracking a laptop" in q for q in quotes)
        assert any("email threads" in q for q in quotes)

    def test_anthropic_arm_register_is_playful(self):
        assert _mechanism()["anthropic_arm"]["register"] == "playful_product_enthusiasm"

    def test_same_day_pair(self):
        assert _mechanism()["meta_arm"]["date"] == _mechanism()["anthropic_arm"]["date"] == "2026-07-07"

    def test_snippet_bounded_label_on_both_arms(self):
        assert "Snippet-bounded" in _mechanism()["meta_arm"]["source_note"]
        assert "Snippet-bounded" in _mechanism()["anthropic_arm"]["source_note"]


class TestScorerDelta658:
    def test_delta_math(self):
        s = _mechanism()["asymmetry_scorer"]
        assert s["meta_tone"] == META_TONE
        assert s["anthropic_tone"] == ANTHROPIC_TONE
        assert abs(s["illustrative_delta_anthropic_minus_meta"] - EXPECTED_DELTA) < 1e-9
        assert abs((ANTHROPIC_TONE - META_TONE) - EXPECTED_DELTA) < 1e-9

    def test_manual_illustrative_only(self):
        text = _mechanism_text()
        assert "MANUAL" in text
        s = _mechanism()["asymmetry_scorer"]
        assert s["p_value"] == "NOT_CALCULATED"
        assert s["cohens_d"] == "NOT_CALCULATED"
        assert s["ci_95"] == "NOT_CALCULATED"
        assert s["is_significant"] is False
        assert s["statistical_contract"] == "degenerate_n1_per_arm"

    def test_verdict_boundaries(self):
        verdict = _mechanism()["asymmetry_scorer"]["verdict"]
        assert "NOT a falsification-family member" in verdict
        assert "NOT a pure asymmetry pin" in verdict
        assert "Correlation only, not causation" in verdict

    def test_verdict_gradient_consistent_peg_confounded(self):
        verdict = _mechanism()["asymmetry_scorer"]["verdict"]
        assert "Gradient-consistent" in verdict
        assert "peg-confounded" in verdict

    def test_confounder_strengths_ranked(self):
        c = _mechanism()["confounders_ranked"]
        assert len(c["strong"]) == 2
        assert len(c["moderate"]) == 2
        assert len(c["weak"]) == 2
        assert any("News peg" in s for s in c["strong"])
        assert any("Consent posture" in s for s in c["strong"])
        assert any("editor-written" in s for s in c["moderate"])
        assert any("Snippet-bounded" in s for s in c["moderate"])

    def test_cross_refs_name_prior_work(self):
        refs = _mechanism()["cross_references"]
        joined = " ".join(refs)
        assert "#648" in joined
        assert "#599" in joined
        assert "#365" in joined
        assert "431" in joined


class TestFinancialContext658:
    def test_conde_nast_openai_licensing_named(self):
        fc = _mechanism()["financial_context"]
        assert "$5-10M/yr" in fc
        assert "OpenAI" in fc
        assert "licensing" in fc

    def test_anthropic_named_as_meta_competitor(self):
        fc = _mechanism()["financial_context"]
        assert "Anthropic" in fc
        assert "Meta competitor" in fc

    def test_meta_pays_zero(self):
        fc = _mechanism()["financial_context"]
        assert "$0 from Meta" in fc

    def test_correlation_not_causation(self):
        fc = _mechanism()["financial_context"]
        assert "Correlation, not causation" in fc

    def test_peg_confound_stronger_than_money(self):
        fc = _mechanism()["financial_context"]
        assert "news-peg confound" in fc


class TestRotationCycleGuard658:
    @staticmethod
    def _mains():
        out = subprocess.run(
            ["git", "log", "--format=%s"],
            cwd=str(REPO_ROOT),
            capture_output=True,
            text=True,
            check=True,
        ).stdout.splitlines()
        return [s for s in out if re.match(r"^Type [A-E] #\d+:", s)]

    def test_window_654_658_closes_a_to_b(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m, f"unparseable rotation subject: {s!r}"
            observed.append((m.group(1), m.group(2)))
        assert observed == [
            ("B", "658"),
            ("A", "657"),
            ("E", "656"),
            ("D", "655"),
            ("C", "654"),
        ], f"rotation window 654-658 wrong: {observed}"

    def test_rotation_adjacency_cycle_valid(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m
            observed.append(m.group(1))
        assert observed == ["B", "A", "E", "D", "C"]
        order = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
        for a, b in zip(observed, observed[1:]):
            assert (order[a] - order[b]) % 5 == 1, (
                f"rotation broken: {a} -> {b} is not a valid cycle edge"
            )

    def test_anchor_is_main_patch_in_followup(self):
        # Post-commit anchor: the #658 main commit. Patched in the followup
        # per the #565 convention once the main commit SHA is known.
        out = subprocess.run(
            ["git", "log", "--format=%H %s"],
            cwd=str(REPO_ROOT),
            capture_output=True,
            text=True,
            check=True,
        ).stdout.splitlines()
        mains = [
            l for l in out if re.match(r"^[0-9a-f]{40} Type [A-E] #\d+:", l)
        ]
        sha, subject = mains[0].split(" ", 1)
        assert sha.startswith(ANCHORED_SHA), f"anchor not yet patched: {sha}"
        assert subject.startswith("Type B #658:"), (
            f"post-commit anchor broken: newest main is not #658: {subject!r}"
        )

    def test_rotation_guard_regex_actually_matches(self):
        # #632 process note: a rotation guard whose regex never matches is a
        # silent no-op. Verify the guard regexes match a real main-commit
        # subject (the double-backslash r"...#(\\d+)..." form silently matches
        # nothing). Written as a semantic check rather than a literal-pattern
        # check so the test cannot defeat itself by containing the pattern.
        src = open(os.path.join(TESTS_DIR, FILENAME)).read()
        patterns = re.findall(r're\.search\(r"([^"]+)"', src)
        guard_patterns = [p for p in patterns if p.startswith("Type (")]
        assert guard_patterns, "no rotation-guard regex found in this file"
        sample = "Type B #658: Reece Rogers same-day register asymmetry"
        for p in guard_patterns:
            m = re.search(p, sample)
            assert m and m.group(1) == "B" and m.group(2) == "658", (
                f"rotation regex {p!r} fails to match a real subject "
                "(double-backslash bug?)"
            )


class TestDocSyncRatchet658:
    def test_readme_has_658_row(self):
        assert "#658" in read_readme()

    def test_arch_has_658_row(self):
        assert "658" in read_arch()

    def test_readme_row_mentions_rogers(self):
        assert "Reece Rogers" in read_readme()

    def test_log_starts_with_658(self):
        assert read_log_start().startswith("#658 Type B:")

    def test_def_test_count_matches(self):
        # The README row for #658 must carry this file's own def-test count.
        n = _count_def_tests()
        assert str(n) in read_readme(), (
            f"README #658 row should mention this file's def-test count {n}"
        )


def read_log_start():
    with open(LOG_PATH) as f:
        return f.read()


class TestNoBrittlePatterns658:
    def test_yaml_reparses_clean(self):
        rogers = _rogers()
        m = rogers[MECH_KEY]
        assert isinstance(m["mechanism_id"], int)
        assert isinstance(m["meta_arm"]["tone_illustrative"], float)
        assert isinstance(m["anthropic_arm"]["tone_illustrative"], float)
        assert isinstance(m["asymmetry_scorer"]["is_significant"], bool)

    def test_no_em_dash_in_mechanism(self):
        assert "\u2014" not in _mechanism_text()
        src = open(os.path.join(TESTS_DIR, FILENAME)).read()
        assert "\u2014" not in src

    def test_all_urls_http_or_https(self):
        urls = list(_mechanism()["meta_arm"]["source_urls"]) + \
            list(_mechanism()["anthropic_arm"]["source_urls"])
        assert urls, "no URLs recorded"
        for u in urls:
            assert u.startswith(("http://", "https://")), f"bad URL: {u!r}"

    def test_no_zero_coverage_claims(self):
        text = _mechanism_text().lower()
        assert "zero coverage" not in text
        assert "no coverage" not in text

    def test_no_engine_significance_claims(self):
        text = _mechanism_text().lower()
        assert "statistically significant" not in text
        assert "p < 0.05" not in text
        assert "p<0.05" not in text

    def test_research_method_names_evidence_tiers(self):
        rm = _mechanism()["research_method"]
        assert "Snippet-bounded" in rm or "snippet-bounded" in rm
        assert "verbatim" in rm

    def test_artifact_readiness_present(self):
        assert "analysis.json" in _mechanism()["artifact_readiness"]
