from datetime import datetime, timedelta
from os import environ, path
from json import dump

CACHE = environ.get("CACHE")
HASH = environ.get("HASH")

CALENDAR_IDS = {
    "primary": "primary",
    "clinic": "c_78ed3a66f79f4b5fbd0dec8ac32598298f02c32801cd64443faa247a60ef5a91@group.calendar.google.com",
}


def refresh(service):
    """Download and store events for the next 7 days."""

    now = datetime.utcnow()
    end_time = now + timedelta(days=7)

    for calendar, id in CALENDAR_IDS.items():

        events = (
            service.events()
            .list(
                calendarId=id,
                timeMin=now.isoformat() + 'Z',
                timeMax=end_time.isoformat() + 'Z',
                singleEvents=True,
                orderBy="startTime",
            )
            .execute()
        )

        events = events.get("items", [])
        relevant_events = []
        
        for event in events:
        
            relevant_event = {
                "id": event["id"],
                "start": event["start"].get("dateTime", event["start"].get("date")),
                "end": event["end"].get("dateTime", event["end"].get("date")),
                "summary": event["summary"],
                "creator": event.get("creator", {}).get("email", ""),
            }

            if calendar == "clinic":
                relevant_event["attendees"] = event.get("attendees", [])

            relevant_events.append(relevant_event)

        cache = path.join(CACHE, f"{calendar}.json")
        
        with open(cache, "w") as file:
            dump(relevant_events, file, indent=4)