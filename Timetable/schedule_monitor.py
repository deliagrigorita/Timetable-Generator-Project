import re
from datetime import timedelta, datetime
from .models import Schedule


def check_overlapping_schedule(new_schedule):
    print("Checking for overlapping schedules...")
    existing_schedules = Schedule.objects.filter(
        day=new_schedule.day,
        start_time__lt=new_schedule.end_time,
        end_time__gt=new_schedule.start_time
    )

    if existing_schedules.exists():
        return True
    return False


day_support = {
    "Monday": 0,
    "Tuesday": 1,
    "Wednesday": 2,
    "Thursday": 3,
    "Friday": 4,
    "Saturday": 5
}

reversed_day_support = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday"
}


def get_next_schedule(new_schedule):
    all_schedules = Schedule.objects.all()
    start_time = re.split(r'\s', str(new_schedule.start_time))[1]
    start_time = int(re.split(r':', start_time)[0])

    found_today = False
    for hour in range(start_time, 19, 2):
        valid = True
        for schedule in all_schedules:
            start_hour = int(re.split(r':', str(schedule.start_time))[0])
            if new_schedule.day == schedule.day and hour == start_hour:
                valid = False
                break
        if valid:
            new_schedule.start_time = datetime(2023, 1, 1, hour, 0)
            new_schedule.end_time = datetime(2023, 1, 1, (hour + 2), 0)
            found_today = True
            break
            
    if not found_today:
        for day in range(day_support[new_schedule.day] + 1, 6):
            found_today = False
            for hour in range(8, 19, 2):
                valid = True
                for schedule in all_schedules:
                    start_hour = int(re.split(r':', str(schedule.start_time))[0])
                    if new_schedule.day == schedule.day and hour == start_hour:
                        valid = False
                        break
                if valid:
                    new_schedule.day = reversed_day_support[day]
                    new_schedule.start_time = datetime(2023, 1, 1, hour, 0)
                    new_schedule.end_time = datetime(2023, 1, 1, (hour + 2), 0)
                    found_today = True
                    break
            if found_today:
                break
    return new_schedule


def handle_overlapping_schedule(new_schedule):
    get_next_schedule(new_schedule)
    print(f'{new_schedule.day} {new_schedule.start_time} {new_schedule.end_time}')
    # new_schedule.save()
    # new_schedule.start_time += timedelta(hours=1)
    # new_schedule.end_time += timedelta(hours=1)
    # new_schedule.save()
    # print("Handling overlapping schedule...")
