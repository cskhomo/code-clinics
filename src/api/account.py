from json import dump, load
from os import environ, path, unlink
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/calendar"]

CREDENTIALS = environ.get('CREDENTIALS')
IDENTITY = environ.get("IDENTITY")
TOKEN = environ.get('TOKEN')       


def login(role):
    """Authenticate and return a Google Calendar service client."""

    if role.title() not in ['Student', 'Volunteer']:
        raise ValueError("Invalid role")
    
    creds = None

    if path.exists(TOKEN):
        creds = Credentials.from_authorized_user_file(TOKEN, SCOPES)

    if not creds or not creds.valid:

        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())


        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS, SCOPES)
            creds = flow.run_local_server(port=0)
        
    service = build("calendar", "v3", credentials=creds)

    calendar = service.calendarList().get(calendarId='primary').execute()
    user = calendar['id']
    
    write_secrets(role, user, creds)

    return service


def logout():
    """Remove all local authentication."""

    if path.exists(TOKEN):
        unlink(TOKEN)

    if path.exists(IDENTITY):
        unlink(IDENTITY)


def write_secrets(role, user, creds):
    """Write user role and credentials to secret files."""

    with open(IDENTITY,'w') as file:
        dump({'role': role.title(), 'user':user}, file)

    with open(TOKEN, "w") as token:
        token.write(creds.to_json())


def status():
    """Return login status based on stored role."""

    user = role()

    if user in ["Student", "Volunteer"]:
        status = f"✅ Logged in as {user}"
    else:
        status = "❌ Not logged in"

    return status


def role():
    """Return the user's role based on the identity file."""

    if not IDENTITY or not path.exists(IDENTITY):
        return "Unidentified User."

    with open(IDENTITY, 'r') as file:
        identity = load(file)
        return identity.get('role')