import pytest
from click import testing


@pytest.fixture
def runner() -> testing.CliRunner:
    return testing.CliRunner()
