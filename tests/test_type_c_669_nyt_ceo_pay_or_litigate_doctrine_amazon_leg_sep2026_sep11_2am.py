"""Type C #669: NYT CEO pay-or-litigate doctrine (Sep 2026 Status Summit) -
on-record commercial-agreement demand as addendum to the Amazon x NYT
$20-25M/yr leg (mechanism 559).

FIRST dedicated mechanism on the NYT CEO's Sep 2026 on-record doctrine
(mechanism_id 636, next free pre-commit; max numeric mechanism_id was 635).
At the Status Summit in New York (~Sep 9 2026), Meredith Kopit Levien told
AI model makers "They have to pay us": any company using Times journalism
for generative AI tools needs a commercial agreement; "We're not letting
anybody off"; the Times will enforce its rights. Conditions: the Times'
permission, control over how journalism is used, fair and sustainable
compensation. The Times runs a two-pronged posture: copyright litigation
against OpenAI, Microsoft, and Perplexity, plus commercial deals (the
Amazon 2025 AI licensing deal, mechanism 559). $4.2M spent on AI-related
litigation in Q1 2026. On Google: Darcy pressed, Levien declined to discuss
any company not addressed publicly - bounded absence of a Google leg.

Analytical hook: the doctrine is the publisher-side on-record statement of
the mechanism by which the NYT claims licensing payment does NOT purchase
editorial softness - payment is a conditional commercial transaction
("We have done a partnership with Amazon because it met those conditions,"
Q1 2026 earnings). It is the falsification-adjacent addendum to mechanism
559 and to the nytimes.yaml competitor_relationships.amazon block (#562),
where the NYT applies an ADVERSARIAL register to Amazon despite Amazon
being the $20-25M/yr payer: money-sympathy INVERTED for the actual payer.
The doctrine is consistent with the sue-one-lab-license-another
bifurcation (mechanism 559) and the News Corp woo-and-sue doctrine
(mechanism 549). NOT a coverage-tone pin: qualitative Type C mapping, no
scorer run, no tone scores, is_significant False, no analysis.json update.

Also documented: the FinancialContent/tokenring syndicated piece claiming a
confidential Anthropic x NYT settlement is a flagged-but-unverified
sponsored surface - NOT asserted as fact (contradicts Adweek Aug 2026
zero-deal reporting); it cannot enter sources/ per the flagged-surface
discipline.

Research method: browser.search this run (3 query sets) + browser.open on
the TheWrap piece first-hand (32 lines rendered; headline, quotes, $4.2M
figure, event context all attested from the page itself). No canonical URLs
constructed; no zero-coverage claims per the iteration-492 rule.

Rotation: Type C follows Type B (#668) per A,B,C,D,E. Rotation guard and
doc-sync classes deselected pre-commit per the #565 followup convention;
anchor patched in the followup commit once the main commit SHA is known.
The novelty-anchor test (exactly one "Type C #669:" main commit
post-followup) is likewise deselected pre-commit.
"""

import ast
import glob
import os
import re
import subprocess

import pytest
import yaml

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENTITIES_PATH = os.path.join(REPO_ROOT, "profiles", "competitor-entities.yaml")
README_PATH = os.path.join(REPO_ROOT, "README.md")
ARCH_PATH = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")
TESTS_DIR = os.path.join(REPO_ROOT, "tests")
LOG_PATH = os.path.join(REPO_ROOT, "iteration-log.md")

MECH_KEY = "mechanism_636_nyt_ceo_pay_or_litigate_doctrine_sep2026"
FILENAME = "test_type_c_669_nyt_ceo_pay_or_litigate_doctrine_amazon_leg_sep2026_sep11_2am.py"

THEWRAP_URL = "https://www.thewrap.com/media-platforms/journalism/nyt-ai-companies-pay/"

# Patched in the followup commit per the #565 convention once the main
# commit SHA is known. The rotation-guard class is deselected pre-commit.
ANCHORED_SHA = "9e39f09"


def _entities():
    with open(ENTITIES_PATH) as f:
        return yaml.safe_load(f)


def _amazon():
    return _entities()["entities"]["amazon"]


def _mechanism():
    am = _amazon()
    assert MECH_KEY in am, f"{MECH_KEY} missing from entities.amazon"
    return am[MECH_KEY]


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


def read_log_start():
    with open(LOG_PATH) as f:
        return f.read()


class TestIterationMetadata669:
    def test_iteration_number(self):
        assert _mechanism()["iteration"] == 669

    def test_mechanism_id_next_free(self):
        assert _mechanism()["mechanism_id"] == 636

    def test_mechanism_id_unique_repo_wide(self):
        seen = {}
        for path in glob.glob(os.path.join(REPO_ROOT, "profiles", "**", "*.yaml"), recursive=True):
            text = open(path, encoding="utf-8", errors="replace").read()
            for m in re.finditer(r"mechanism_id:\s*(\d+)", text):
                if int(m.group(1)) == 636:
                    seen.setdefault(636, []).append(path)
        assert len(seen.get(636, [])) == 1, f"mechanism_id 636 not unique: {seen.get(636)}"

    def test_type_c_rotation_and_mapping_type(self):
        m = _mechanism()
        assert m["rotation"] == "Type C"
        assert m["type"] == "financial_incentive_mapping"

    def test_goal_and_job_ids(self):
        m = _mechanism()
        assert m["goal_id"] == "goal_54093bda4145"
        assert m["job_id"] == "mediascope-daily-iteration"
        assert m["scheduled_job_id"] == "mediascope-daily-iteration"

    def test_block_key_matches(self):
        assert _mechanism()["block_key"] == "type_c_669_nyt_ceo_pay_or_litigate_doctrine_amazon_leg_sep2026"

    def test_no_duplicate_669_file(self):
        others = [p for p in glob.glob(os.path.join(TESTS_DIR, "test_type_c_669_*.py"))
                  if os.path.basename(p) != FILENAME]
        assert not others, f"duplicate #669 test files: {others}"

    def test_no_type_c_669_commit_pre_commit(self):
        out = subprocess.run(
            ["git", "log", "--format=%s", "--grep=Type C #669"],
            cwd=str(REPO_ROOT),
            capture_output=True,
            text=True,
            check=True,
        ).stdout.strip()
        assert out == "", f"Type C #669 already in git log pre-commit: {out!r}"


class TestDoctrineFacts669:
    def test_event_venue_and_date(self):
        ev = _mechanism()["event"]
        assert ev["venue"] == "Status Summit, New York (panel discussion)"
        assert ev["event_date"] == "2026-09-09"
        assert ev["speaker"] == "Meredith Kopit Levien, NYT CEO"
        assert ev["questioner"] == "Oliver Darcy, Status founder"

    def test_pay_us_quote_verbatim(self):
        assert _mechanism()["doctrine_quotes"]["pay_us"] == "They have to pay us."

    def test_commercial_agreement_quote_verbatim(self):
        q = _mechanism()["doctrine_quotes"]["commercial_agreement_required"]
        assert "need a commercial agreement with us" in q
        assert "model maker" in q

    def test_enforce_rights_quote_verbatim(self):
        q = _mechanism()["doctrine_quotes"]["enforce_rights"]
        assert "not letting anybody off" in q
        assert "prepared to enforce our rights" in q

    def test_conditions_three_parts(self):
        c = _mechanism()["doctrine_quotes"]["conditions"]
        assert "permission" in c
        assert "control over how its journalism is used" in c
        assert "fair and sustainable" in c

    def test_two_pronged_posture(self):
        tp = _mechanism()["two_pronged_posture"]
        assert "OpenAI" in tp["litigation"]
        assert "Microsoft" in tp["litigation"]
        assert "Perplexity" in tp["litigation"]
        assert "Amazon" in tp["commercial_deals"]
        assert "2025" in tp["commercial_deals"]

    def test_litigation_spend(self):
        assert "4.2" in _mechanism()["two_pronged_posture"]["litigation_spend"]
        assert "Q1 2026" in _mechanism()["two_pronged_posture"]["litigation_spend"]

    def test_google_exchange_bounded_absence(self):
        g = _mechanism()["google_exchange"]
        assert "declined to discuss" in g["levien_response"]
        assert "iteration-492" in g["google_leg_status"]
        assert "bounded absence" in g["google_leg_status"]

    def test_big_tech_quote_present(self):
        q = _mechanism()["doctrine_quotes"]["big_tech_role"]
        assert "Google" in q
        assert "enormous responsibility" in q


class TestFinancialIncentiveContext669:
    def test_adjacent_to_mechanism_559(self):
        fa = _mechanism()["falsification_adjacency"]
        txt = yaml.safe_dump(fa)
        assert "mechanism 559" in txt
        assert "20-25M" in txt

    def test_nytimes_562_adversarial_on_payer(self):
        fa = _mechanism()["falsification_adjacency"]
        assert "562" in fa["adjacent_pin"]
        assert "ADVERSARIAL" in fa["adjacent_pin"]
        assert "INVERTED" in fa["adjacent_pin"]

    def test_doctrine_consistency(self):
        fa = _mechanism()["falsification_adjacency"]
        assert "549" in fa["doctrine_consistency"]
        assert "559" in fa["doctrine_consistency"]

    def test_no_coverage_tone_claim(self):
        m = _mechanism()
        assert m["no_coverage_tone_claim"] is True
        assert m["statistical_discipline"]["tone_scores"] == "NOT_SCORED"
        assert m["statistical_discipline"]["engine_run"] is False
        assert m["statistical_discipline"]["is_significant"] is False

    def test_analysis_json_not_updated(self):
        assert _mechanism()["analysis_json_update"] is False

    def test_anthropic_contrast(self):
        txt = yaml.safe_dump(_mechanism()["falsification_adjacency"])
        assert "Adweek" in txt
        assert "509" in txt
        assert "did NOT pay" in txt

    def test_flagged_but_unverified_not_asserted(self):
        f = _mechanism()["flagged_but_unverified"]
        assert "NOT asserted as fact" in f["verdict"]
        assert "tokenring" in f["url_path_channel"]
        assert f["content_claimed"] is not None
        srcs = _mechanism()["sources"]
        assert all("tokenring" not in s and "financialcontent" not in s for s in srcs), (
            "flagged surface must not enter sources/"
        )

    def test_q1_earnings_conditions_linkage(self):
        q = _mechanism()["doctrine_to_deal_linkage"]["q1_2026_earnings_conditions"]
        assert "met those conditions" in q
        assert "May 6 2026" in q


class TestResearchMethod669:
    def test_thewrap_url_in_sources(self):
        assert THEWRAP_URL in _mechanism()["sources"]

    def test_first_hand_browser_open_documented(self):
        rm = _mechanism()["research_method"]
        assert "opened first-hand this run" in rm
        assert "32 lines" in rm

    def test_adweek_second_hand_noted(self):
        rm = _mechanism()["research_method"]
        assert "Adweek" in rm
        assert "second-hand" in rm

    def test_iteration_492_bounded_absence(self):
        rm = _mechanism()["research_method"]
        assert "iteration-492" in rm
        assert "no zero-coverage claims" in rm

    def test_verification_block(self):
        v = _mechanism()["verification"]
        assert v["yaml_parse_clean"] is True
        assert v["goal_id"] == "goal_54093bda4145"
        assert v["iteration"] == 669
        assert v["type"] == "C"
        assert "2026-09-11" in v["date"]

    def test_novelty_block(self):
        n = _mechanism()["novelty"]
        assert "Sep 2026 Status Summit" in n["dedicated_mechanism_on_sep2026_doctrine"]
        assert "new to corpus" in n["thewrap_sep2026_url"]
        assert "do-not-cite" in n["flag_tokenring_surface"]
        assert "559" in n["distinct_from"]


class TestConfoundersRanked669:
    def test_five_ranked_confounders(self):
        cs = _mechanism()["ranked_confounders"]
        assert len(cs) == 5
        assert [c["rank"] for c in cs] == [1, 2, 3, 4, 5]
        assert {c["strength"] for c in cs} == {"strong", "moderate", "weak"}

    def test_strong_confounders_two(self):
        cs = _mechanism()["ranked_confounders"]
        strong = [c for c in cs if c["strength"] == "strong"]
        assert len(strong) == 2
        assert any("performative" in c["confounder"] for c in strong)
        assert any("second-hand" in c["confounder"] for c in strong)

    def test_statistical_discipline(self):
        sd = _mechanism()["statistical_discipline"]
        assert sd["p_value"] == "NOT_CALCULATED"
        assert sd["cohens_d"] == "NOT_CALCULATED"
        assert sd["correlation_not_causation"] is True

    def test_cautious_language(self):
        m = _mechanism()
        assert m["cautious_language_required"] is True
        assert "No causal claim" in m["correlational_note"]


class TestRotationCycleGuard669:
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

    def test_window_665_669_closes_b_to_c(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m, f"unparseable rotation subject: {s!r}"
            observed.append((m.group(1), m.group(2)))
        assert observed == [
            ("C", "669"),
            ("B", "668"),
            ("A", "667"),
            ("E", "666"),
            ("D", "665"),
        ], f"rotation window 665-669 wrong: {observed}"

    def test_rotation_adjacency_cycle_valid(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m
            observed.append(m.group(1))
        assert observed == ["C", "B", "A", "E", "D"]
        order = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
        for a, b in zip(observed, observed[1:]):
            assert (order[a] - order[b]) % 5 == 1, (
                f"rotation broken: {a} -> {b} is not a valid cycle edge"
            )

    def test_anchor_is_main_patch_in_followup(self):
        # Post-commit anchor: the #669 main commit. Patched in the followup
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
        assert subject.startswith("Type C #669:"), (
            f"post-commit anchor broken: newest main is not #669: {subject!r}"
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
        sample = "Type C #669: NYT CEO pay-or-litigate doctrine vs Amazon leg"
        for p in guard_patterns:
            m = re.search(p, sample)
            assert m and m.group(1) == "C" and m.group(2) == "669", (
                f"rotation regex {p!r} fails to match a real subject "
                "(double-backslash bug?)"
            )


class TestDocSyncRatchet669:
    def test_readme_has_669_row(self):
        assert "#669" in read_readme()

    def test_arch_has_669_row(self):
        assert "669" in read_arch()

    def test_readme_row_mentions_doctrine(self):
        assert "pay-or-litigate" in read_readme()

    def test_log_starts_with_669(self):
        assert read_log_start().startswith("#669 Type C:")

    def test_def_test_count_matches(self):
        # The README row for #669 must carry this file's own def-test count.
        n = _count_def_tests()
        assert str(n) in read_readme(), (
            f"README #669 row should mention this file's def-test count {n}"
        )


class TestNoBrittlePatterns669:
    def test_yaml_reparses_clean(self):
        m = _mechanism()
        assert isinstance(m["mechanism_id"], int)
        assert isinstance(m["iteration"], int)
        assert isinstance(m["ranked_confounders"], list)

    def test_mechanism_key_naming(self):
        assert MECH_KEY.startswith("mechanism_636_")
        assert MECH_KEY in _amazon()

    def test_no_em_dash_or_curly_quotes_in_mechanism(self):
        text = _mechanism_text()
        assert "\u2014" not in text, "em dash found in mechanism block"
        assert "\u2018" not in text and "\u2019" not in text, "curly quote in mechanism block"

    def test_mechanism_text_ascii_only(self):
        text = _mechanism_text()
        bad = [c for c in text if ord(c) > 127]
        assert not bad, f"non-ASCII chars in mechanism block: {set(bad)!r}"

    def test_type_c_669_main_commit_unique_and_anchored(self):
        # Novelty anchor: exactly one "Type C #669:" main commit post-followup
        # (deselected pre-commit per the #565 convention; the followup and
        # doc-sync commits are "Type C #669 followup:" / "Type C #669
        # doc-sync:" and do NOT match the main-commit filter).
        out = subprocess.run(
            ["git", "log", "--format=%H %s"],
            cwd=str(REPO_ROOT),
            capture_output=True,
            text=True,
            check=True,
        ).stdout.splitlines()
        mains = [l for l in out if re.match(r"^[0-9a-f]{40} Type C #669:", l)]
        assert len(mains) == 1, f"expected exactly one Type C #669 main commit, got {len(mains)}"
        assert mains[0].startswith(ANCHORED_SHA), (
            f"main commit SHA does not match patched anchor: {mains[0][:12]}"
        )
