from django import forms
from .models import Student
from .models import Teacher
from .models import Resource
from .models import Schedule
from .models import Timetable

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['email', 'password', 'first_name', 'last_name']

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher 
        fields = ['email', 'password', 'first_name', 'last_name']

class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ['name', 'description', 'classroom', 'availability']

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['day', 'start_time', 'end_time']

class TimetableForm(forms.ModelForm):
    class Meta:
        model = Timetable
        fields = ['classes', 'semester', 'academic_year', 'is_published']
        exclude = ['created_at', 'updated_at']
