import pytest
from pathlib import Path
from src.config_reader import get_env_config


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="dev",
        help="Environment: dev or prod"
    )


@pytest.fixture(scope="session")
def env_config(request):
    env = request.config.getoption("--env")
    return get_env_config(env)


def pytest_sessionstart(session):
    env = session.config.getoption("--env")
    config = get_env_config(env)

    results_dir = Path("allure-results")
    results_dir.mkdir(exist_ok=True)

    with open(results_dir / "environment.properties", "w") as f:
        f.write(f"Environment={env}\n")
        f.write(f"Project={config['project']}\n")

        if "dataset" in config:
            f.write(f"Dataset={config['dataset']}\n")