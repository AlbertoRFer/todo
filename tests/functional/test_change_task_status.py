from click import testing

from . import cli_commands


def test_change_task_status(runner: testing.CliRunner) -> None:
    with runner.isolated_filesystem():
        # Given a list of tasks that were just added
        cli_commands.create_task(runner, "First Task")
        cli_commands.create_task(runner, "Second Task")

        # When the user list the tasks
        result = cli_commands.list_tasks(runner)
        assert result.exit_code == 0
        lines = result.output.splitlines()
        # Then an indicator that the tasks are not completed is shown
        assert "[ ]" in lines[0]
        assert "[ ]" in lines[1]

        # When the user changes the status of the first task (completing it)
        result = cli_commands.change_task_status(runner, "1")
        assert result.exit_code == 0

        result = cli_commands.list_tasks(runner)
        assert result.exit_code == 0
        lines = result.output.splitlines()
        # Then the indicator that the first task was completed is shown
        assert "[x]" in lines[0]
        assert "[ ]" in lines[1]

        # When the user changes the status of the first task (uncompleting it)
        result = cli_commands.change_task_status(runner, "1")
        assert result.exit_code == 0

        result = cli_commands.list_tasks(runner)
        assert result.exit_code == 0
        lines = result.output.splitlines()
        # Then the indicator that the first task was not completed is shown
        assert "[ ]" in lines[0]
        assert "[ ]" in lines[1]
