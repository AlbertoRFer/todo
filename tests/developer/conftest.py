import pytest

from todo import repository

from . import fakes


@pytest.fixture
def fake_repo() -> repository.Repository:
    return fakes.FakeRepository()
