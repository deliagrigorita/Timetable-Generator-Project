from django.shortcuts import render, redirect
from ..forms import ScheduleForm  
from ..models import Schedule
from django.http import JsonResponse
import aspectlib
import json

@aspectlib.Aspect
def log_add_schedule(*args, **kwargs):
    print("Adding a schedule...")
    result = yield aspectlib.Proceed
    print("Schedule added successfully.")
    return result

@aspectlib.Aspect
def log_update_schedule(*args, **kwargs):
    print("Update a schedule...")
    result = yield aspectlib.Proceed
    print("Schedule updated successfully.")
    return result

@aspectlib.Aspect
def log_delete_schedule(*args, **kwargs):
    print("Delete a schedule...")
    result = yield aspectlib.Proceed
    print("Schedule deleted successfully.")
    return result

@aspectlib.Aspect
def log_get_schedules(*args, **kwargs):
    print("Get schedules...")
    result = yield aspectlib.Proceed
    print("Schedules received successfully.")
    return result

@log_add_schedule
def add_schedule(request):
    if request.method == 'POST':
        form = ScheduleForm(request.POST)  
        if form.is_valid():
            schedule = form.save()
            return redirect('index')  
    else:
        form = ScheduleForm()  
    return render(request, 'schedule.html', {'form': form})

@log_update_schedule
def update_schedule(request, schedule_id):
    try:
        if request.method == 'PUT':
            print(f"Processing PUT request for schedule ID {schedule_id}")
        else:
            print(f"Invalid request method")
        
        schedule = Schedule.objects.get(id=schedule_id)
        data = json.loads(request.body)

        schedule.day = data.get('day', schedule.day)
        schedule.start_time = data.get('start_time', schedule.start_time)
        schedule.end_time = data.get('end_time', schedule.end_time)

        schedule.save()

        updated_data = {
            'id': schedule.id,
            'day': schedule.day,
            'start_time': schedule.start_time.strftime('%H:%M:%S'),
            'end_time': schedule.end_time.strftime('%H:%M:%S'),
        }

        return JsonResponse(updated_data)

    except Schedule.DoesNotExist:
        return JsonResponse({'error': 'Schedule not found'}, status=404)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON data'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@log_delete_schedule
def delete_schedule(request, schedule_id):
    try:
        schedule = Schedule.objects.get(id=schedule_id)
        schedule.delete()
        
        return JsonResponse({'message': 'Schedule deleted successfully'})
    except Schedule.DoesNotExist:
        return JsonResponse({'error': 'Schedule not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@log_get_schedules
def get_all_schedules(request):
    schedules = Schedule.objects.all()
    schedules_data = []
    for schedule in schedules:
        schedule_data = {
            'id': schedule.id,
            'day': schedule.day,
            'start_time': schedule.start_time.strftime('%H:%M:%S'),
            'end_time': schedule.end_time.strftime('%H:%M:%S'),
        }
        schedules_data.append(schedule_data)
    return JsonResponse(schedules_data, safe=False)
