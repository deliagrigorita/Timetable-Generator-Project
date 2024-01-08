from django.shortcuts import render
from ..google_calendar.utils import get_google_calendar_service, create_event


def add_to_google_calendar(request):
    # Get required event details from your Django model or form
    summary = 'Class Name'
    location = 'Class Location'
    start_time = '2024-01-13T08:00:00'  # Example start time
    end_time = '2024-01-13T09:30:00'    # Example end time

    # Authenticate with Google Calendar API
    service = get_google_calendar_service()

    # Create the event in Google Calendar
    create_event(service, summary, location, start_time, end_time)

    # Add any additional logic or response handling here
    return render(request, 'index.html')
