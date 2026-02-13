from unittest import mock

import pytest
import pytest_cases
from click import testing

from todo import cli, exceptions, todo_app


@pytest.fixture
def runner() -> testing.CliRunner:
    return testing.CliRunner()


@pytest.fixture
def app_stub() -> mock.Mock:
    return mock.Mock(todo_app.TodoApp)


@pytest_cases.parametrize(
    "exc",
    [
        exceptions.InvalidTaskDescriptionError,
        exceptions.DuplicateTaskDescriptionError,
    ],
    ids=["empty task description", "duplicate task description"],
)
def test_create_task_propagates_errors_as_cli_failure(
    runner: testing.CliRunner,
    app_stub: mock.Mock,
    exc: Exception,
) -> None:
    # Given an app that raises an exception on create_task api call
    app_stub.create_task.side_effect = exc
    with runner.isolated_filesystem():
        # When the user creates a task
        result = runner.invoke(
            cli.cli, ["create-task", ""], catch_exceptions=False, obj=app_stub
        )
        # Then the command fails in the expected way
        assert result.exit_code == 2
