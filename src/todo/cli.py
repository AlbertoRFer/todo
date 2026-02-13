import click

from todo import bootstrap, exceptions, todo_app, todo_list


@click.group()
@click.pass_context
def cli(ctx: click.Context) -> None:
    if ctx.obj is None:
        ctx.obj = bootstrap.create_todo_app()


@cli.command()
@click.pass_obj
def list_tasks(app: todo_app.TodoApp) -> None:
    todo: todo_list.TodoList = app.list_tasks()

    if todo.tasks:
        for n, task in enumerate(todo.tasks, start=1):
            click.echo(f"{n}.- {task.description}")
    else:
        click.echo("There are no tasks currently.")


@cli.command()
@click.pass_obj
@click.argument("description", required=True)
def create_task(app: todo_app.TodoApp, description: str) -> None:
    try:
        app.create_task(description)
    except (
        exceptions.InvalidTaskDescriptionError,
        exceptions.DuplicateTaskDescriptionError,
    ) as err:
        raise click.BadArgumentUsage(str(err)) from err

    click.echo("Task added successfully.")
