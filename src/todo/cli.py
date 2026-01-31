import click


@click.group()
def cli() -> None:
    pass


@cli.command()
def list_tasks() -> None:
    click.echo("There are no tasks currently.")
