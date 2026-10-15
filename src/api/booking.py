from os import environ
import json 

IDENTITY = environ.get("IDENTITY")
beta_calendar_id = "c_78ed3a66f79f4b5fbd0dec8ac32598298f02c32801cd64443faa247a60ef5a91@group.calendar.google.com"

def create(service):
    """
    Book a session by adding student email to the event's attendees list.
    """
    with open(IDENTITY, 'r') as f:
        identity = json.load(f)

    if identity['role'] != 'Student':
        print(f"❌ {identity['role']} cannot perform this action")
        return

    user_email = identity.get('user')  
    if not user_email:
        print("Please login first")
        return

    event_name = input("Enter the event name: ").strip()

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

    event = service.events().get(calendarId=beta_calendar_id, eventId=event_id).execute()
    event["attendees"] = [{"email": user_email}]
    service.events().update(
        calendarId=beta_calendar_id,
        eventId=event_id,
        body=event
    ).execute()
    print(f"✅ {user_email} successfully booked on '{event_name}'.")


def delete(service):
    """
    Cancel student booking by removing their email from the event's attendees list.
    """
    with open(IDENTITY, 'r') as f:
        identity = json.load(f)

    if identity['role'] != 'Student':
        print(f"❌ {identity['role']} cannot perform this action")
        return

    user_email = identity.get('user')  
    if not user_email:
        print("Please login first")
        return

    event_name = input("Specify the name of the booked event to be cancelled: ").strip()

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

    event = service.events().get(calendarId=beta_calendar_id, eventId=event_id).execute()
    event["attendees"] = []
    service.events().update(calendarId=beta_calendar_id, eventId=event_id, body=event).execute()
    print(f"Your booking has been cancelled for: {event_name}")