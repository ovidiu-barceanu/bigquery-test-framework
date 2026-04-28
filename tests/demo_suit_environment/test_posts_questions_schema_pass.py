from src.bigquery_client import get_client
from src.query_runner import load_query
from pathlib import Path
import pytest
import allure


@pytest.mark.envdemo
@allure.title("Demo test for environment setup")
def test_demo_environment(env_config):
    with allure.step("Connect to BigQuery"):
        client = get_client()

    query = load_query("queries/test_environment_setup.sql")

    # Replace environment placeholders from config
    query = query.replace("{{project}}", env_config["project"])

    results = list(client.query(query))

    if results:
        print("\nSCHEMA DIFFERENCES:")
        for row in results:
            print(dict(row))

    with allure.step("Assert case"):
        assert len(results) != 0, (
            f"FAILED: Schema mismatch found ({len(results)} issues)"
        )
