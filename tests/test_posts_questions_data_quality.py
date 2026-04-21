from src.bigquery_client import get_client
from src.query_runner import load_query


def test_posts_questions_data_quality():
    client = get_client()

    query = load_query("queries/test_posts_questions_data_quality.sql")

    results = list(client.query(query))

    if results:
        print("\nFAILED ROWS:")
        for row in results[:10]:  # limit output
            print(dict(row))

    assert len(results) == 0, (
        f"FAILED: {len(results)} data quality issues found"
    )