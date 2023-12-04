from datetime import timedelta
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


def handle_overlapping_schedule(new_schedule):
    new_schedule.start_time += timedelta(hours=1)
    new_schedule.end_time += timedelta(hours=1)
    new_schedule.save()
    print("Handling overlapping schedule...")
