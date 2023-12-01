from Timetable.student_monitor import StudentCountMonitor
from ..models import Student
from django.shortcuts import render, redirect
from django.http import HttpResponse
from ..forms import StudentForm
from ..student_monitor import simulate_student_addition

# Create an instance of the StudentCountMonitor
student_monitor = StudentCountMonitor()

def add_student(request):
    #global student_monitor  
    if request.method == 'POST':
        # Update student count and check the property
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
