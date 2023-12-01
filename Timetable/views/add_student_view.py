from django.shortcuts import render, redirect
from Timetable.student_monitor import StudentCountMonitor
from ..forms import StudentForm
from ..models import Student
from django.http import JsonResponse
import aspectlib
import json


@aspectlib.Aspect
def log_add_student(*args, **kwargs):
    print("Adding a student...")
    result = yield aspectlib.Proceed
    print("Student added successfully.")
    return result


@aspectlib.Aspect
def log_update_student(*args, **kwargs):
    print("Update a student...")
    result = yield aspectlib.Proceed
    print("Student updated successfully.")
    return result


@aspectlib.Aspect
def log_delete_student(*args, **kwargs):
    print("Delete a student...")
    result = yield aspectlib.Proceed
    print("Student deleted successfully.")
    return result


@aspectlib.Aspect
def log_get_students(*args, **kwargs):
    print("Get students...")
    result = yield aspectlib.Proceed
    print("Student received successfully.")
    return result

student_monitor = StudentCountMonitor()

@log_add_student
def add_student(request):
    #global student_monitor
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = Student(
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                #date_of_birth=form.cleaned_data['date_of_birth']
            )
            student.save()
            #return redirect('index')  
           
        student_monitor.student_count = len(Student.objects.all())
        if not student_monitor.max_student_count():
             student_monitor.violation_handler('max_student_count')
        return redirect('index')
    else:
        form = StudentForm()

    return render(request, 'index.html', {'form': form})


@log_update_student
def update_student(request, student_id):
    try:
        if request.method == 'PUT':
            print(f"Processing PUT request for student ID {student_id}")
        else:
            print(f"nu e put")
        
        student = Student.objects.get(id=student_id)

        data = json.loads(request.body)

        print(data)
        student.email = data.get('email', student.email)
        student.password = data.get('password', student.password)
        student.first_name = data.get('first_name', student.first_name)
        student.last_name = data.get('last_name', student.last_name)
        student.date_of_birth = data.get('date_of_birth', student.date_of_birth)

        student.save()  

        updated_data = {
                'id': student.id,
                'email': student.email,
                'password': student.password,
                'first_name': student.first_name,
                'last_name': student.last_name,
                'date_of_birth': student.date_of_birth.isoformat() if student.date_of_birth else None,
            }
        
        print(updated_data)
        return JsonResponse(updated_data)

    except Student.DoesNotExist:
        return JsonResponse({'error': 'Student not found'}, status=404)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON data'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


@log_delete_student
def delete_student(request, student_id):
    try:
        student = Student.objects.get(id=student_id)
        student.delete()
        
        return JsonResponse({'message': 'Student deleted successfully'})
    except Student.DoesNotExist:
        return JsonResponse({'error': 'Student not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


def get_student(request, user_id):
    try:
        student = Student.objects.get(id=user_id)
        student_data = {
            'id': student.id,
            'email': student.email,
            'password': student.password,
            'first_name': student.first_name,
            'last_name': student.last_name,
            'date_of_birth': student.date_of_birth.isoformat() if student.date_of_birth else None,
        }
        return JsonResponse(student_data)
    except Student.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)
    

@log_get_students
def get_all_students(request):
    students = Student.objects.all()
    students_data = []
    for student in students:
        student_data = {
            'id': student.id,
            'email': student.email,
            'password': student.password,
            'first_name': student.first_name,
            'last_name': student.last_name,
            'date_of_birth': student.date_of_birth.isoformat() if student.date_of_birth else None,
        }
        students_data.append(student_data)
    return JsonResponse(students_data, safe=False)
