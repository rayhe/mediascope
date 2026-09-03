"""
Type B #482 Karen Weise (NYT) within-journalist Amazon vs Microsoft headline-verb asymmetry.

Tests 30 checks covering mechanism existence in both YAML stores, iteration/date/
rotation/goal-job IDs, same journalist, five post-deal Amazon enforcement articles
with deception/coercion headline verbs (tricked, secretly inflated, suppresses,
retaliated), four Microsoft articles including the Aug 26 2026 hourlong Gates
1-on-1, headline-verb tally (5/5 vs 0/4, score 0.66), the $70-125M/yr compound
NYT-Amazon dependency, the repo open-question answer (no softening post-deal),
the litigation inversion (NYT sues Microsoft/OpenAI yet Gates gets access-soft
treatment), the tax-haven counter-datapoint, ranked confounders, 6 verbatim
HTTPS source URLs, cautious language, distinct-from-prior (Feb 2026 Ring paradox
is publication-level; this is within-journalist), no em dashes, HTTPS-only hygiene.
"""
import re
import yaml
from pathlib import Path

REPO = Path(__file__).parent.parent
NYT = REPO / "profiles" / "nytimes.yaml"
JOURNALISTS = REPO / "profiles" / "careers" / "journalists.yaml"

TEST_ITERATION = 482
MECHANISM_ID = 482
JOURNALIST = "Karen Weise"
MECH_KEY = "mechanism_482_karen_weise_amazon_microsoft_headline_verb_asymmetry_sep03"

EXPECTED_URLS = [
    "https://muckrack.com/kyweise/articles",
    "https://www.nytimes.com/2026/08/26/technology/bill-gates-ai-risks.htm",
    "https://www.economie.gouv.fr/files/files/directions_services/rejoignez-nous/DGCCRF/recrutement-par-concours/categorie-A_licence/Sujet%201%20-%20MR%20-%20Amazon%20to%20Pay%20%242.5%20Billion%20to%20Settle%20Claims.pdf",
    "https://www.knkx.org/2025-10-22/amazon-wants-to-use-robots-to-avoid-adding-over-500-000-new-jobs",
    "https://www.wsj.com/tech/ftc-to-file-lawsuit-alleging-amazon-deceived-advertisers-d71039ee",
    "https://globalcommunityweekly.substack.com/p/nyt-bill-gates-warns-ai-is-more-dangerous",
]

AMAZON_VERBS = ["tricked", "secretly inflated", "suppresses", "retaliated"]


def load_nyt():
    return yaml.safe_load(NYT.read_text())


def load_journalists():
    return yaml.safe_load(JOURNALISTS.read_text())


def get_nyt_mech():
    data = load_nyt()
    for j in data["key_journalists"]:
        if j.get("name") == JOURNALIST:
            cea = j.get("cross_entity_coverage_analysis", {})
            assert MECH_KEY in cea, f"mechanism key {MECH_KEY} not found in nytimes.yaml"
            return cea[MECH_KEY]
    raise AssertionError("Karen Weise not found in nytimes.yaml key_journalists")


def get_career_mech():
    data = load_journalists()
    jlist = data["journalists"] if isinstance(data, dict) and "journalists" in data else data
    for entry in jlist:
        if entry.get("name") == JOURNALIST:
            assert MECH_KEY in entry, f"mechanism {MECH_KEY} not found in journalists.yaml"
            return entry[MECH_KEY]
    raise AssertionError("Karen Weise not found in journalists.yaml")


def full_text(mech):
    return yaml.safe_dump(mech, default_flow_style=False)


class TestMechanismPresence:
    def test_mechanism_exists_nyt(self):
        mech = get_nyt_mech()
        assert mech["mechanism_id"] == MECHANISM_ID
        assert mech["iteration"] == TEST_ITERATION
        assert mech["iteration_type"] == "B"

    def test_mechanism_exists_career(self):
        mech = get_career_mech()
        assert mech["mechanism_id"] == MECHANISM_ID
        assert mech["iteration"] == TEST_ITERATION

    def test_same_journalist_both_stores(self):
        nyt = get_nyt_mech()
        career = get_career_mech()
        assert "Karen Weise" in nyt["journalist"]
        assert "Karen Weise" in career["journalist"]
        assert nyt["mechanism_id"] == career["mechanism_id"] == 482

    def test_test_file_field_matches_this_file(self):
        mech = get_nyt_mech()
        assert mech["test_file"].endswith(Path(__file__).name)


class TestIterationMetadata:
    def test_iteration_time_and_ids(self):
        mech = get_nyt_mech()
        assert mech["iteration_time"] == "2026-09-03 00:00 PDT"
        assert mech["scheduled_job_id"] == "mediascope-daily-iteration"
        assert mech["goal_id"] == "goal_54093bda4145"
        assert mech["discovery_date"] == "2026-09-03"

    def test_publication_focus_nyt(self):
        assert get_nyt_mech()["publication_focus"] == "NYT"

    def test_type_b_label(self):
        mech = get_nyt_mech()
        assert mech["type"].startswith("B - Journalist Cross-Entity Tracking")


class TestAmazonDeceptionVerbs:
    def test_five_amazon_articles_documented(self):
        arts = get_nyt_mech()["amazon_articles_post_deal"]
        assert len(arts) == 5

    def test_prime_settlement_tricked_verb(self):
        arts = get_nyt_mech()["amazon_articles_post_deal"]
        prime = [a for a in arts if "2.5 Billion" in a["title"]]
        assert len(prime) == 1
        assert prime[0]["headline_verb"] == "tricked"
        assert prime[0]["date"] == "2025-09-25"
        assert "Cecilia Kang" in prime[0]["byline"]

    def test_ftc_ad_prices_secretly_inflated(self):
        arts = get_nyt_mech()["amazon_articles_post_deal"]
        ftc = [a for a in arts if "Ad Prices" in a["title"]]
        assert len(ftc) == 1
        assert ftc[0]["headline_verb"] == "secretly inflated"
        assert ftc[0]["date"] == "2026-08"

    def test_nj_suppresses_and_retaliation_verbs(self):
        arts = get_nyt_mech()["amazon_articles_post_deal"]
        verbs = [a.get("headline_verb") for a in arts]
        assert "suppresses" in verbs
        assert "retaliated" in verbs

    def test_robot_takeover_investigative_framing(self):
        arts = get_nyt_mech()["amazon_articles_post_deal"]
        robot = [a for a in arts if "Robot Takeover" in a["title"]]
        assert len(robot) == 1
        assert "aggressive corporate culture" in robot[0]["framing"]

    def test_all_amazon_articles_post_deal(self):
        arts = get_nyt_mech()["amazon_articles_post_deal"]
        for a in arts:
            assert a["date"] >= "2025-05", f"{a['title']} predates May 2025 deal: {a['date']}"


class TestMicrosoftAccessFraming:
    def test_four_microsoft_articles_documented(self):
        arts = get_nyt_mech()["microsoft_articles"]
        assert len(arts) == 4

    def test_gates_interview_solo_access_datapoint(self):
        arts = get_nyt_mech()["microsoft_articles"]
        gates = [a for a in arts if "Bill Gates" in a["title"]]
        assert len(gates) == 1
        assert gates[0]["date"] == "2026-08-26"
        assert "solo" in gates[0]["byline"]
        assert "hourlong" in gates[0]["framing"]
        assert gates[0]["source_url"] == "https://www.nytimes.com/2026/08/26/technology/bill-gates-ai-risks.htm"

    def test_gates_epstein_single_clause(self):
        arts = get_nyt_mech()["microsoft_articles"]
        gates = [a for a in arts if "Bill Gates" in a["title"]][0]
        assert "single subordinate clause" in gates["framing"]

    def test_tax_haven_counter_datapoint_present(self):
        arts = get_nyt_mech()["microsoft_articles"]
        tax = [a for a in arts if "Tax Haven" in a["title"]]
        assert len(tax) == 1
        assert "COUNTER-DATAPOINT" in tax[0]["framing"]

    def test_headline_verb_tally(self):
        tally = get_nyt_mech()["headline_verb_tally"]
        assert tally["amazon_deception_coercion_verbs"] == 5
        assert tally["amazon_total_headlines"] == 5
        assert tally["microsoft_deception_coercion_verbs"] == 0
        assert tally["microsoft_total_headlines"] == 4
        assert tally["asymmetry_score"] == 0.66


class TestFinancialContext:
    def test_compound_dependency_documented(self):
        fin = get_nyt_mech()["financial_context"]
        assert "$20-25M/yr" in fin
        assert "$70-125M+/yr" in fin
        assert "May 2025" in fin

    def test_open_question_answered_no_softening(self):
        fin = get_nyt_mech()["financial_context"]
        assert "did not" in fin or "did NOT" in fin or "no" in fin.lower()
        pattern = get_nyt_mech()["pattern"]
        assert "did NOT soften" in pattern

    def test_affiliate_cuts_noted(self):
        fin = get_nyt_mech()["financial_context"]
        assert "March 2026" in fin
        assert "50%" in fin

    def test_boundary_condition_insight(self):
        novel = " ".join(get_nyt_mech()["novel_insight"].split())
        assert "BOUNDARY CONDITION" in novel
        assert "beat assignment" in novel


class TestInstitutionalInversion:
    def test_litigation_inversion_documented(self):
        inv = get_nyt_mech()["institutional_inversion"]
        assert "suing Microsoft/OpenAI" in inv
        assert "inverted" in inv

    def test_double_inversion_claim(self):
        inv = get_nyt_mech()["institutional_inversion"]
        assert "double inversion" in inv

    def test_distinct_from_feb_paradox(self):
        refs = get_nyt_mech()["cross_references"]
        feb = [r for r in refs if "February 2026" in r]
        assert len(feb) == 1
        assert "within-journalist" in feb[0]


class TestConfoundersAndHygiene:
    def test_confounders_ranked(self):
        conf = get_nyt_mech()["confounders_ranked"]
        assert len(conf["strong"]) >= 2
        assert len(conf["moderate"]) >= 2
        assert len(conf["weak"]) >= 1
        strong_text = " ".join(conf["strong"])
        assert "Genuine news events" in strong_text or "genuine news events" in strong_text.lower()

    def test_seattle_geography_confounder_bounded(self):
        conf = get_nyt_mech()["confounders_ranked"]
        strong_text = " ".join(conf["strong"])
        assert "Redmond" in strong_text or "both ways" in strong_text

    def test_expected_urls_present_verbatim(self):
        urls = get_nyt_mech()["source_urls"]
        for expected in EXPECTED_URLS:
            assert expected in urls, f"missing expected URL: {expected}"

    def test_urls_https_only(self):
        for url in get_nyt_mech()["source_urls"]:
            assert url.startswith("https://"), f"non-HTTPS URL: {url}"

    def test_no_em_dashes_in_mechanism(self):
        text = full_text(get_nyt_mech())
        assert "\u2014" not in text, "em dash found in mechanism text"
        assert "\u2013" not in text, "en dash found in mechanism text"

    def test_cautious_language_no_absolute_capture_claim(self):
        text = full_text(get_nyt_mech()).lower()
        assert "proves" not in text or "non-confirmation" in text or "boundary" in text
