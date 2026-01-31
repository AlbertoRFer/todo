import click


@click.group()
def cli() -> None:
    pass


@cli.command()
def list_tasks() -> None:
    click.echo("There are no tasks currently.")


@cli.command()
@click.argument("description")
def create_task(description: str) -> None:
    click.echo("Task added successfully.")
