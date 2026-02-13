from click import testing

from todo import cli


def invoke_runner(runner: testing.CliRunner, cmd: str, *args: str) -> testing.Result:
    return runner.invoke(cli.cli, [cmd, *args], standalone_mode=False)


def create_task(runner: testing.CliRunner, description: str) -> testing.Result:
    cmd = "create-task"

    return invoke_runner(runner, cmd, description)


def list_tasks(runner: testing.CliRunner) -> testing.Result:
    cmd = "list-tasks"

    return invoke_runner(runner, cmd)


def change_task_status(runner: testing.CliRunner, task_id: str) -> testing.Result:
    cmd = "change-task-status"

    return invoke_runner(runner, cmd, task_id)
