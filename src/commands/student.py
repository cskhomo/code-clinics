import click
from src.commands.help import students
from src.interface import available
from src.interface import allocated
from src.api.account import login
from src.storage.data import refresh
import src.api.booking as booking


@click.group(help=students["description"], short_help=students["hint"])
def student():
    pass


@student.command(help=students["sessions"]["description"], short_help=students["sessions"]["hint"])
def sessions():
    service = login('Student')
    refresh(service)
    click.echo(available.sessions())


@student.command(help=students["bookings"]["description"], short_help=students["bookings"]["hint"])
def bookings():
    service = login('Student')
    refresh(service)
    click.echo(allocated.bookings())


@student.command(help=students["book"]["description"], short_help=students["book"]["hint"])
def book():
    service = login('Student')
    booking.create(service)
    refresh(service)


@student.command(help=students["cancel"]["description"], short_help=students["cancel"]["hint"])
def cancel():
    service = login('Student')
    booking.delete(service)
    refresh(service)


if __name__ == "__main__":
    student()