from src.bigquery_client import get_client
from src.query_runner import load_query
import pytest

@pytest.mark.regression
def test_posts_questions_schema():
    client = get_client()

    query = load_query("queries/test_posts_questions_schema.sql")

    results = list(client.query(query))

    if results:
        print("\nSCHEMA DIFFERENCES:")
        for row in results:
            print(dict(row))

    assert len(results) == 0, (
        f"FAILED: Schema mismatch found ({len(results)} issues)"
    )