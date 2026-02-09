from click import testing

from . import cli_commands

NO_TASKS_OUTPUT = "There are no tasks currently.\n"


def test_create_task_successfully(runner: testing.CliRunner) -> None:
    first_description = "First Task"
    second_description = "Second Task"

    success_output = "Task added successfully.\n"

    with runner.isolated_filesystem():
        # GIVEN the application has no tasks stored yet
        result = cli_commands.list_tasks(runner)
        assert result.exit_code == 0
        assert result.output == NO_TASKS_OUTPUT

        # WHEN the user creates a task with a non-empty description
        result = cli_commands.create_task(runner, first_description)
        # THEN the task is saved successfully and the user gets feedback
        assert result.exit_code == 0
        assert result.output == success_output

        # WHEN the user lists tasks
        result = cli_commands.list_tasks(runner)
        # THEN the created task is visible and numbered starting from 1
        assert result.exit_code == 0
        lines = result.output.splitlines()
        assert len(lines) == 1
        assert lines[0].startswith("1")
        assert first_description in lines[0]

        # WHEN the user creates a second task
        result = cli_commands.create_task(runner, second_description)
        # THEN the second task is saved successfully and the user gets feedback
        assert result.exit_code == 0
        assert result.output == success_output

        # WHEN the user lists tasks again
        result = cli_commands.list_tasks(runner)
        # THEN both tasks are visible in creation order and numbered sequentially
        assert result.exit_code == 0
        lines = result.output.splitlines()
        assert len(lines) == 2
        assert lines[0].startswith("1")
        assert first_description in lines[0]
        assert lines[1].startswith("2")
        assert second_description in lines[1]
