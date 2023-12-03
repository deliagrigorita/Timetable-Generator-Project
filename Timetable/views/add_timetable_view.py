from django.shortcuts import render, redirect
from ..forms import TimetableForm 
from ..models import Timetable, Class
from django.http import JsonResponse
import aspectlib
import json

@aspectlib.Aspect
def log_add_timetable(*args, **kwargs):
    print("Adding a timetable...")
    result = yield aspectlib.Proceed
    print("Timetable added successfully.")
    return result

@aspectlib.Aspect
def log_update_timetable(*args, **kwargs):
    print("Update a timetable...")
    result = yield aspectlib.Proceed
    print("Timetable updated successfully.")
    return result

@aspectlib.Aspect
def log_delete_timetable(*args, **kwargs):
    print("Delete a timetable...")
    result = yield aspectlib.Proceed
    print("Timetable deleted successfully.")
    return result

@aspectlib.Aspect
def log_get_timetables(*args, **kwargs):
    print("Get timetables...")
    result = yield aspectlib.Proceed
    print("Timetables received successfully.")
    return result

@log_add_timetable
def add_timetable(request):
    if request.method == 'POST':
        form = TimetableForm(request.POST)  
        if form.is_valid():
            timetable = form.save()
            return redirect('index')  
    else:
        form = TimetableForm()  

    return render(request, 'index.html', {'form': form})

@log_update_timetable
def update_timetable(request, timetable_id):
    try:
        if request.method == 'PUT':
            print(f"Processing PUT request for timetable ID {timetable_id}")
        else:
            print(f"Invalid request method")
        
        timetable = Timetable.objects.get(id=timetable_id)
        data = json.loads(request.body)

        timetable.semester = data.get('semester', timetable.semester)
        timetable.academic_year = data.get('academic_year', timetable.academic_year)
        timetable.is_published = data.get('is_published', timetable.is_published)

        timetable.save()

        updated_data = {
            'id': timetable.id,
            'semester': timetable.semester,
            'academic_year': timetable.academic_year,
            'is_published': timetable.is_published,
        }

        return JsonResponse(updated_data)

    except Timetable.DoesNotExist:
        return JsonResponse({'error': 'Timetable not found'}, status=404)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON data'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@log_delete_timetable
def delete_timetable(request, timetable_id):
    try:
        timetable = Timetable.objects.get(id=timetable_id)
        timetable.delete()
        
        return JsonResponse({'message': 'Timetable deleted successfully'})
    except Timetable.DoesNotExist:
        return JsonResponse({'error': 'Timetable not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@log_get_timetables
def get_all_timetables(request):
    timetables = Timetable.objects.all()
    timetables_data = []
    for timetable in timetables:
        timetable_data = {
            'id': timetable.id,
            'classes': timetable.classes.name,
            'semester': timetable.semester,
            'academic_year': timetable.academic_year,
            'is_published': timetable.is_published,
            'created_at': timetable.created_at.strftime('%Y-%m-%d %H:%M:%S') if timetable.created_at else None,
            'updated_at': timetable.updated_at.strftime('%Y-%m-%d %H:%M:%S') if timetable.updated_at else None,
        }
        timetables_data.append(timetable_data)
    return JsonResponse(timetables_data, safe=False)
