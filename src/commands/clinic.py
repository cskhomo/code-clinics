import click
from src.api import account
from src.storage import data
from src.commands.help import login, logout, status
from src.commands.volunteer import volunteer
from src.commands.student import student


@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    """
Code Clinic Booking System CLI Tool

A command-line interface for managing 'Clinic' help sessions and bookings.
Allowing volunteers and students to connect and support each other.

Volunteers:

  - View available time slots                                               - Create and manage help sessions

Students:

  - View available help sessions                                             - Create and Manage booked sessions
"""

    if ctx.invoked_subcommand is None:
        click.echo(ctx.get_help())


@cli.command(help=login["description"], short_help=login["hint"])
@click.argument("role", type=click.Choice(["student", "volunteer"]))
def login(role):
    service = account.login(role)
    data.refresh(service)


@cli.command(help=logout["description"], short_help=logout["hint"])
def logout():
    account.logout()


@cli.command(help=status["description"], short_help=status["hint"])
def status():
    click.echo(account.status())

cli.add_command(volunteer)
cli.add_command(student)


if __name__ == "__main__":
    cli()