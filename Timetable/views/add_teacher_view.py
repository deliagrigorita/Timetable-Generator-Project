# add_teacher_view.py
from django.shortcuts import render, redirect, reverse 
from ..forms import TeacherForm 
from ..models import Teacher, Subject, User
from django.http import JsonResponse
import aspectlib
import json

@aspectlib.Aspect
def log_add_teacher(*args, **kwargs):
    print("Adding a teacher...")
    result = yield aspectlib.Proceed
    print("Teacher added successfully.")
    return result

@aspectlib.Aspect
def log_update_teacher(*args, **kwargs):
    print("Update a teacher...")
    result = yield aspectlib.Proceed
    print("Teacher updated successfully.")
    return result

@aspectlib.Aspect
def log_delete_teacher(*args, **kwargs):
    print("Delete a teacher...")
    result = yield aspectlib.Proceed
    print("Teacher deleted successfully.")
    return result

@aspectlib.Aspect
def log_get_teachers(*args, **kwargs):
    print("Get teachers...")
    result = yield aspectlib.Proceed
    print("Teachers received successfully.")
    return result

@log_add_teacher
def add_teacher(request):
    action_url = reverse('add_teacher')  # Ensure that 'add_teacher' is the correct URL name
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            print("form.cleaned_data:\n")
            print(form.cleaned_data)
            teacher = form.save()
            print(f"Teacher with ID {teacher.id} added successfully.")
            return redirect('index')
        else:
            print("form.errors:\n")
            print(form.errors)
    else:
        form = TeacherForm()

    return render(request, 'teacher.html', {'action_url': action_url, 'form': form})


@log_update_teacher
def update_teacher(request, teacher_id):
    try:
        if request.method == 'PUT':
            print(f"Processing PUT request for teacher ID {teacher_id}")
        else:
            print(f"Invalid request method")
        
        teacher = Teacher.objects.get(id=teacher_id)
        data = json.loads(request.body)

        teacher.email = data.get('email', teacher.email)
        teacher.password = data.get('password', teacher.password)

        teacher.save()

        updated_data = {
            'id': teacher.id,
            'email': teacher.email,
            'password': teacher.password,
        }

        return JsonResponse(updated_data)

    except Teacher.DoesNotExist:
        return JsonResponse({'error': 'Teacher not found'}, status=404)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON data'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@log_delete_teacher
def delete_teacher(request, teacher_id):
    try:
        teacher = Teacher.objects.get(id=teacher_id)
        teacher.delete()
        
        return JsonResponse({'message': 'Teacher deleted successfully'})
    except Teacher.DoesNotExist:
        return JsonResponse({'error': 'Teacher not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@log_get_teachers
def get_all_teachers(request):
    teachers = Teacher.objects.all()
    teachers_data = []
    for teacher in teachers:
        teacher_data = {
            'id': teacher.id,
            'email': teacher.email,
            'password': teacher.password,
        }
        teachers_data.append(teacher_data)
    return JsonResponse(teachers_data, safe=False)
