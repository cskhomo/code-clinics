import click
from pydoc import pager
from src.commands.help import volunteers
from src.interface import available
from src.interface import allocated
from src.api.account import login
from src.storage import data
import src.api.session as session


@click.group(help=volunteers["description"], short_help=volunteers["hint"])
def volunteer():
    pass


@volunteer.command(help=volunteers["slots"]["description"], short_help=volunteers["slots"]["hint"])
def slots():
    service = login('Volunteer')
    data.refresh(service)
    pager(available.slots())


@volunteer.command(help=volunteers["sessions"]["description"], short_help=volunteers["sessions"]["hint"])
def sessions():
    service = login('Volunteer')
    data.refresh(service)
    click.echo(allocated.sessions())


@volunteer.command(help=volunteers["create"]["description"], short_help=volunteers["create"]["hint"])
def book():
    service = login('Volunteer')
    session.create(service)
    data.refresh(service)


@volunteer.command(help=volunteers["cancel"]["description"], short_help=volunteers["cancel"]["hint"])
def cancel():
    service = login('Volunteer')
    session.delete(service)
    data.refresh(service)


if __name__ == "__main__":
    volunteer()