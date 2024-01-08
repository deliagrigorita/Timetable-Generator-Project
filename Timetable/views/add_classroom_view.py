# add_classroom_view.py
from django.shortcuts import render, redirect, reverse
from ..forms import ClassroomForm 
from ..models import Classroom, Subject, User
from django.http import JsonResponse
import aspectlib
import json

@aspectlib.Aspect
def log_add_classroom(*args, **kwargs):
    print("Adding a classroom...")
    result = yield aspectlib.Proceed
    print("Classroom added successfully.")
    return result

@aspectlib.Aspect
def log_update_classroom(*args, **kwargs):
    print("Update a classroom...")
    result = yield aspectlib.Proceed
    print("Classroom updated successfully.")
    return result

@aspectlib.Aspect
def log_delete_classroom(*args, **kwargs):
    print("Delete a classroom...")
    result = yield aspectlib.Proceed
    print("Classroom deleted successfully.")
    return result

@aspectlib.Aspect
def log_get_classrooms(*args, **kwargs):
    print("Get classrooms...")
    result = yield aspectlib.Proceed
    print("Classrooms received successfully.")
    return result

@log_add_classroom
def add_classroom(request):
    action_url = reverse('add_classroom')
    if request.method == 'POST':
        form = ClassroomForm(request.POST)
        if form.is_valid():
            try:
                classroom = Classroom(
                    name=form.cleaned_data['name'], 
                )
                classroom.save()
                form = ClassroomForm()
                print("Classroom added successfully.")
            except Exception as e:
                print(f"Error saving classroom: {e}")
        else:
            print(form.errors)
    else:
        form = ClassroomForm()

    return render(request, 'classroom.html', {'action_url': action_url})


@log_update_classroom
def update_classroom(request, classroom_id):
    try:
        if request.method == 'PUT':
            print(f"Processing PUT request for classroom ID {classroom_id}")
        else:
            print(f"Invalid request method")
        
        classroom = Classroom.objects.get(id=classroom_id)
        data = json.loads(request.body)
        
        classroom.name = data.get('name', classroom.name)
        
        classroom.save()

        updated_data = {
            'id': classroom.id,
            'name': classroom.name,
        }

        return JsonResponse(updated_data)

    except Classroom.DoesNotExist:
        return JsonResponse({'error': 'Classroom not found'}, status=404)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON data'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@log_delete_classroom
def delete_classroom(request, classroom_id):
    try:
        classroom = Classroom.objects.get(id=classroom_id)
        classroom.delete()
        
        return JsonResponse({'message': 'Classroom deleted successfully'})
    except Classroom.DoesNotExist:
        return JsonResponse({'error': 'Classroom not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@log_get_classrooms
def get_all_classrooms(request):
    classrooms = Classroom.objects.all()
    classrooms_data = []
    for classroom in classrooms:
        classroom_data = {
            'id': classroom.id,
            'name': classroom.name,

        }
        classrooms_data.append(classroom_data)
    return JsonResponse(classrooms_data, safe=False)
