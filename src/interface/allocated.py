from datetime import datetime
from prettytable import PrettyTable
from src.api import account
from os import environ
import json 


IDENTITY = environ.get("IDENTITY")
CACHE = environ.get("CACHE")


def sessions():
    """Displays sessions created by a volunteer."""

    user = account.role()

    if user != 'Volunteer':
        return f"❌ {user} cannot perform this action"

    with open(IDENTITY) as identity, open(f'{CACHE}/clinic.json') as clinic:
        identity = json.load(identity)
        clinic = json.load(clinic)

    volunteer = identity.get('user', '').strip().lower()
    sessions = PrettyTable()
    sessions.field_names = ["Attendee", "Start Time", "Summary"]

    for event in clinic:
        creator = event.get('creator', '').strip().lower()
        if creator != volunteer:
            continue 

        attendees = event.get('attendees', [])
        if attendees:
            attendee = attendees[0].get('email', '').strip().lower()
            attendee_name = attendee.strip('@student.wethinkcode.co.za').upper()
        else:
            attendee_name = "No Attendee yet"

        start_time = datetime.fromisoformat(event.get('start', '').replace('Z', '+00:00'))
        formatted_start_time = start_time.strftime("%B %d, %Y – %H:%M")

        summary = event.get('summary', '')

        sessions.add_row([attendee_name, formatted_start_time, summary])

    if not sessions._rows:
        return "You haven't created any sessions."

    return sessions.get_string()


def bookings():
    """Displays bookings made by a student."""

    user = account.role()

    if user != 'Student':
        return f"❌ {user} cannot perform this action"

    with open(IDENTITY) as identity, open(f'{CACHE}/clinic.json') as clinic:
        identity = json.load(identity)
        clinic = json.load(clinic)

    student = identity.get('user', '').strip().lower()
    
    bookings = PrettyTable()
    bookings.field_names = ["Creator", "Start Time", "Summary"]

    for event in clinic:
        for attendee in event.get('attendees', []):
            if attendee.get('email', '').strip().lower() == student:
                start_time = datetime.fromisoformat(event.get('start', '').replace('Z', '+00:00'))
                formatted_start_time = start_time.strftime("%B %d, %Y – %H:%M")

                creator_name = event.get('creator', '').strip('@student.wethinkcode.co.za').upper()
                bookings.add_row([
                    creator_name,
                    formatted_start_time,
                    event.get('summary', '')
                ])
                break

    if not bookings._rows:
        return "No events to attend yet"

    return bookings.get_string()