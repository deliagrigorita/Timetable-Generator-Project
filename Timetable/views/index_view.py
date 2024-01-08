from Timetable.student_monitor import StudentCountMonitor
from ..models import Student, User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from ..forms import StudentForm, LoginForm
from ..student_monitor import simulate_student_addition
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password

def index(request):

    return render(request, 'index.html')
