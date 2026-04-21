from src.bigquery_client import get_client
from src.query_runner import load_query


def test_no_negative_views():
    client = get_client()

    query = load_query("queries/test_no_negative_views.sql")

    results = list(client.query(query))

    assert len(results) == 0, (
        f"FAILED: Found {len(results)} rows with negative view_count"
    )