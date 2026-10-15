from src.api import account
from os import environ
from datetime import datetime, timedelta
from prettytable import PrettyTable
import json 

IDENTITY = environ.get("IDENTITY")
CACHE = environ.get("CACHE")


def slots():
    """Displays available time slots for a volunteer."""

    user = account.role()

    if user != 'Volunteer':
        return f"❌ {user} cannot perform this action"

    with open(IDENTITY) as identity, open(f'{CACHE}/clinic.json') as clinic:
        identity = json.load(identity)
        clinic = json.load(clinic)

    volunteer = identity.get('user', '').strip().lower()

    # Define time range
    start_time = datetime.strptime("08:00", "%H:%M").time()
    end_time = datetime.strptime("17:00", "%H:%M").time()

    # Get today's date and calculate date range for the next 7 days
    today = datetime.today().date()
    date_range = [(today + timedelta(days=n)) for n in range(7)]

    output = ""

    for date in date_range:
        start = datetime.combine(date, start_time)
        end = datetime.combine(date, end_time)

        busy_time_slots = []

        for event in clinic:
            event_creator = event.get('creator', '').strip().lower()
            if event_creator == volunteer:
                event_start = datetime.fromisoformat(event.get('start', '').replace('Z', '+00:00')).replace(tzinfo=None)
                event_end = datetime.fromisoformat(event.get('end', '').replace('Z', '+00:00')).replace(tzinfo=None)

                if event_start.date() == date and event_start < end and event_end > start:
                    busy_time_slots.append((max(event_start, start), min(event_end, end)))

        available_time_slots = []
        current_time = start
        busy_time_slots.sort(key=lambda x: x[0])

        for busy_slot in busy_time_slots:
            if current_time < busy_slot[0]:
                available_time_slots.append((current_time, busy_slot[0]))
            current_time = max(current_time, busy_slot[1])

        if current_time < end:
            available_time_slots.append((current_time, end))

        if not busy_time_slots:
            available_time_slots = [(start, end)]

        table = PrettyTable()
        table.field_names = ["Start Time", "End Time"]
        table.title = date.strftime("%A, %B %d, %Y")

        for slot in available_time_slots:
            table.add_row([
                slot[0].strftime("%H:%M"),
                slot[1].strftime("%H:%M")
            ])

        if table._rows:
            output += table.get_string() + "\n\n"
        else:
            output += f"No available time slots for {date.strftime('%A, %B %d, %Y')}\n\n"

    return output.strip()


def sessions():
    """Displays upcoming sessions for a student."""

    user = account.role()

    if user != 'Student':
        return f"❌ {user} cannot perform this action"

    with open(IDENTITY) as identity, open(f'{CACHE}/clinic.json') as clinic:
        identity = json.load(identity)
        clinic = json.load(clinic)

    student = identity.get('user', '').strip().lower()

    sessions = PrettyTable()
    sessions.field_names = ["Creator", "Start Time", "Summary"]

    for event in clinic:
        volunteer = event.get('creator', '').strip().lower()
        attendees = event.get('attendees', [])

        if student == volunteer:
            continue

        attendee = [attendee.get('email', '').strip().lower() for attendee in attendees]
        if student in attendee:
            continue

        start_time = datetime.fromisoformat(event.get('start', '').replace('Z', '+00:00'))
        formatted_start_time = start_time.strftime("%B %d, %Y – %H:%M")

        creator_name = event.get('creator', '').replace('@student.wethinkcode.co.za', '').upper().strip()
        sessions.add_row([
            creator_name,
            formatted_start_time,
            event.get('summary', '')
        ])

    if not sessions._rows:
        return "No upcoming sessions found."

    return sessions.get_string()