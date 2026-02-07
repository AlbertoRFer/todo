import pathlib

import click

from todo import bootstrap, todo_app


@click.group()
@click.pass_context
def cli(ctx: click.Context) -> None:
    ctx.obj = bootstrap.create_todo_app()


@cli.command()
@click.pass_obj
def list_tasks(app: todo_app.TodoApp) -> None:
    tasks = app.list_tasks()
    if tasks:
        for n, task in enumerate(tasks, start=1):
            click.echo(f"{n}.- {task}")
    else:
        click.echo("There are no tasks currently.")


@cli.command()
@click.pass_obj
@click.argument("description", required=True)
def create_task(app: todo_app.TodoApp, description: str) -> None:
    if not description.strip():
        raise click.BadArgumentUsage("Task description must be a non empty string")

    repo = app.repo
    todo_list = repo.list_tasks()
    todo_list.append(description)
    repo.add_todo_list(todo_list)
    click.echo("Task added successfully.")
