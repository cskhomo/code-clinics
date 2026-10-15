import json
import os
from datetime import datetime, timedelta

IDENTITY = os.environ.get('IDENTITY')
beta_calendar_id = "c_78ed3a66f79f4b5fbd0dec8ac32598298f02c32801cd64443faa247a60ef5a91@group.calendar.google.com"

def create(service):
    """
    Create a new event.
    """
    with open(IDENTITY, 'r') as f:
        identity = json.load(f)

    if identity['role'] != 'Volunteer':
        print(f"❌ {identity['role']} cannot perform this action")
        return

    event_name = input("Specify event name: ")
    date_str = input("Enter event date (YYYY-MM-DD): ")
    time_str = input("Enter start time (HH:MM in 24-hour format): ")
    duration_minutes = input("Enter duration in minutes (default is 30): ") or "30"

    start = datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M")
    duration = timedelta(minutes=float(duration_minutes))
    end = start + duration

    event = {
        'summary': event_name,
        'description': 'Volunteering',
        'start': {
            'dateTime': start.isoformat(),
            'timeZone': 'Africa/Johannesburg',
        },
        'end': {
            'dateTime': end.isoformat(),
            'timeZone': 'Africa/Johannesburg',
        },
        'attendees': [], 
        'guestsCanModify': True,  
    }

    service.events().insert(calendarId=beta_calendar_id, body=event).execute()
    print(f"Event created: {event_name}")

def delete(service):
    """
    Delete an event by name.
    """
    with open(IDENTITY, 'r') as f:
        identity = json.load(f)

    if identity['role'] != 'Volunteer':
        print(f"❌ {identity['role']} cannot perform this action")
        return

    event_name = input("Specify the name of the event to be deleted: ")

    events_result = service.events().list(calendarId=beta_calendar_id).execute()
    events = events_result.get('items', [])

    event_id = None
    for event in events:
        if event['summary'] == event_name:
            event_id = event['id']
            break

    if event_id is None:
        print(f"Event '{event_name}' not found.")
        return

    service.events().delete(calendarId=beta_calendar_id, eventId=event_id).execute()
    print(f"Event deleted: {event_name}")