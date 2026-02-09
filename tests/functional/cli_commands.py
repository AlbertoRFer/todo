from click import testing

from todo import cli


def create_task(runner: testing.CliRunner, description: str) -> testing.Result:
    return runner.invoke(cli.cli, ["create-task", description])


def list_tasks(runner: testing.CliRunner) -> testing.Result:
    return runner.invoke(cli.cli, ["list-tasks"])
