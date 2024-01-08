from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build


def get_google_calendar_service():
    flow = InstalledAppFlow.from_client_secrets_file(
        'Timetable/google_calendar/client_secret_315725404428-e6m6o5gk311lgsel702i7e3cvilr03bs.apps.googleusercontent.com.json',
        scopes=['https://www.googleapis.com/auth/calendar', 'https://www.googleapis.com/auth/calendar.readonly'],
    )
    credentials = flow.run_local_server(port=0)
    return build('calendar', 'v3', credentials=credentials)


def create_event(service, summary, location, start_time, end_time):
    event = {
        'summary': summary,
        'location': location,
        'start': {
            'dateTime': start_time,
            'timeZone': 'Europe/Bucharest',
        },
        'end': {
            'dateTime': end_time,
            'timeZone': 'Europe/Bucharest',
        },
    }
    event = service.events().insert(calendarId='primary', body=event).execute()
    print(f'Event created: {event.get("htmlLink")}')
