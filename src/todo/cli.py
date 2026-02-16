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
            status = "[x]" if task.is_done else "[ ]"
            click.echo(f"{n}.- {status} {task.description}")

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


@cli.command()
@click.pass_obj
@click.argument("task_id", required=True)
def change_task_status(app: todo_app.TodoApp, task_id: str) -> None:
    todo = app.list_tasks()
    task_to_update = todo.tasks[int(task_id) - 1]

    app.update_task_status(task_to_update.id, not task_to_update.is_done)

    click.echo("Task status updated successfully.")
