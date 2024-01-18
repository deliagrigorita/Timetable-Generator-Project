from django.shortcuts import render, redirect, reverse
from ..forms import ClassForm 
from ..models import Class, Subject, User, Teacher, Classroom, Schedule, StudentGroup, StudentYear, StudentSemian, Type
from django.http import JsonResponse
import aspectlib
import json

@aspectlib.Aspect
def log_add_class(*args, **kwargs):
    print("Adding a class...")
    result = yield aspectlib.Proceed
    print("Class added successfully.")
    return result

@aspectlib.Aspect
def log_update_class(*args, **kwargs):
    print("Update a class...")
    result = yield aspectlib.Proceed
    print("Class updated successfully.")
    return result

@aspectlib.Aspect
def log_delete_class(*args, **kwargs):
    print("Delete a class...")
    result = yield aspectlib.Proceed
    print("Class deleted successfully.")
    return result

@aspectlib.Aspect
def log_get_classes(*args, **kwargs):
    print("Get classes...")
    result = yield aspectlib.Proceed
    print("Classes received successfully.")
    return result

@log_add_class
def add_class(request):
    teachers = Teacher.objects.all()
    classrooms = Classroom.objects.all()
    schedules = Schedule.objects.all()
    groups = StudentGroup.objects.all()
    semiani = StudentSemian.objects.all()
    years = StudentYear.objects.all()
    types = Type.objects.all()
    action_url = reverse('add_class')

    if request.method == 'POST':
        form = ClassForm(request.POST) 
        if form.is_valid():
            print("form.cleaned_data:\n")
            print(form.cleaned_data)
            form.save()
            return redirect('index')  
        else:
            print("form.errors:\n")
            print(form.errors)
    else:
        form = ClassForm()
        
    return render(request, 'class.html', {'classrooms': classrooms, 'teachers': teachers, 'schedules': schedules, 'groups': groups, 'semiani': semiani,'years': years,'types': types, 'action_url': action_url})

 
@log_update_class
def update_class(request, class_id):
    try:
        if request.method == 'PUT':
            print(f"Processing PUT request for class ID {class_id}")
        else:
            print(f"Invalid request method")
        
        classs = Class.objects.get(id=class_id)
        data = json.loads(request.body)

        classs.name = data.get('name' , classs.name)
        classs.teacher = data.get('teacher', classs.teacher)
        classs.students = data.get('students', classs.students)
        classs.classroom = data.get('classroom', classs.classroom)
        classs.schedule = data.get('schedule', classs.schedule)
        classs.resources = data.get('resource', classs.resource)

        classs.save()

        updated_data = {
            'id': classs.id,
            'name' : classs.name,
            'teacher' : classs.teacher,
            'students' : classs.students,
            'classroom' : classs.classroom,
            'schedule': classs.schedule,
            'resource': classs.resources,
        }

        return JsonResponse(updated_data)

    except Class.DoesNotExist:
        return JsonResponse({'error': 'Class not found'}, status=404)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON data'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@log_delete_class
def delete_class(request, class_id):
    try:
        classs = Class.objects.get(id=class_id)
        classs.delete()
        
        return JsonResponse({'message': 'Class deleted successfully'})
    except Class.DoesNotExist:
        return JsonResponse({'error': 'Class not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@log_get_classes
def get_all_classes(request):
    classes = Class.objects.all()
    classes_data = []
    for classs in classes:
        classs_data = {
            'id': classs.id,
            'name' : classs.name,
            'teacher' : classs.teacher,
            'students' : classs.students,
            'classroom' : classs.classroom,
            'schedule': classs.schedule,
            'resource': classs.resources,
        }
        classes_data.append(classs_data)
    return JsonResponse(classes_data, safe=False)
