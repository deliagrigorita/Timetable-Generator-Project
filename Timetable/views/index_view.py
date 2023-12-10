from Timetable.student_monitor import StudentCountMonitor
from ..models import Student, User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from ..forms import StudentForm, LoginForm
from ..student_monitor import simulate_student_addition
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password

student_monitor = StudentCountMonitor()

def add_student(request):
    if request.method == 'POST':
        student_monitor.student_count = len(Student.objects.all())
        if not student_monitor.max_student_count():
            student_monitor.violation_handler('max_student_count')

        return redirect('index')  
    else:
        form = StudentForm()

    return render(request, 'index.html', {'form': form})


def index(request):
    simulate_student_addition(student_monitor)
    return render(request, 'index.html', context={'user_name': '[REDACTED]', 'items': ['item1', 'item2']})
