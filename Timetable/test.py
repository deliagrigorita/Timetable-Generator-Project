import os
from datetime import datetime, timedelta
from .models import Schedule
from django.core.wsgi import get_wsgi_application
from .schedule_monitor import check_overlapping_schedule, handle_overlapping_schedule

application = get_wsgi_application()
os.environ['DJANGO_SETTINGS_MODULE'] = 'Timetable_generator_project.settings'


def create_schedule(day, start_time, end_time):
    return Schedule.objects.create(day=day, start_time=start_time, end_time=end_time)

def test_schedule_functions():
    # Test Case 1: Non-overlapping schedules
    # print("Test Case 1: Non-overlapping schedules\n")
    #
    schedule = Schedule(day='Monday', start_time=datetime(2023, 1, 1, 10, 0), end_time=datetime(2023, 1, 1, 12, 0))
    # print("schedule = " + str(schedule.day) + ", " + str(schedule.start_time) + ", " + str(schedule.end_time))
    #
    # if not check_overlapping_schedule(schedule):
    #     new_schedule = create_schedule('Monday', datetime(2023, 1, 1, 10, 0), datetime(2023, 1, 1, 12, 0))
    #     new_schedule.save()
    #     print("Schedule saved successfully.\n")
    # else:
    #     print("Overlap detected. Schedule not saved.\n")


    # Test Case 2: Overlapping schedules
    print("Test Case 2: Overlapping schedules\n")

    existing_schedule = schedule
    print("schedule = " + str(schedule.day) + ", " + str(schedule.start_time) + ", " + str(schedule.end_time))

    if check_overlapping_schedule(schedule):
        print("Overlap detected. Schedule not saved.\n")
    else:
        print("Should be overlap.\n")


    # Test Case 3: Handling overlapping schedule
    print("Test Case 3: Handling overlapping schedule\n")
    
    handle_overlapping_schedule(existing_schedule)
    # existing_schedule.refresh_from_db()
    print("Overlapping resolved\n")

