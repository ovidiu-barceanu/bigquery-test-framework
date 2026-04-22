from src.bigquery_client import get_client
from src.query_runner import load_query
import allure


# def test_no_negative_views():
#     client = get_client()
#
#     query = load_query("queries/test_no_negative_views.sql")
#
#     results = list(client.query(query))
#
#     assert len(results) == 0, (
#         f"FAILED: Found {len(results)} rows with negative view_count"
#     )

@allure.title("Validate posts_questions has no negative views")
def test_no_negative_views():

    with allure.step("Connect to BigQuery"):
        client = get_client()

    query = load_query("queries/test_no_negative_views.sql")

    with allure.step("Run SQL validation"):
        results = list(client.query(query))

    with allure.step("Verify zero invalid rows"):
        assert len(results) == 0