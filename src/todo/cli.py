import pathlib

import click

from todo import storage, task_repository


@click.group()
@click.pass_context
def cli(ctx: click.Context) -> None:
    tasks_file_path = pathlib.Path.cwd() / "tasks.json"
    json_storage = storage.JsonStorage(tasks_file_path)
    ctx.obj = task_repository.TaskRepository(json_storage)


@cli.command()
@click.pass_obj
def list_tasks(repo: task_repository.TaskRepository) -> None:
    tasks = repo.list_tasks()
    if tasks:
        for n, task in enumerate(tasks, start=1):
            click.echo(f"{n}.- {task}")
    else:
        click.echo("There are no tasks currently.")


@cli.command()
@click.pass_obj
@click.argument("description", required=True)
def create_task(repo: task_repository.TaskRepository, description: str) -> None:
    if not description.strip():
        raise click.BadArgumentUsage("Task description must be a non empty string")

    todo_list = repo.list_tasks()
    todo_list.append(description)
    repo.add_todo_list(todo_list)
    click.echo("Task added successfully.")
