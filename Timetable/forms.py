from django import forms
from .models import Student
from .models import Teacher
from .models import Resource
from .models import Schedule
from .models import Timetable
from .models import Subject
from .models import Classroom
from .models import Class
from .models import Admin, User


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['email', 'password', 'first_name', 'last_name']

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher 
        fields = ['email', 'password', 'first_name', 'last_name']

class ResourceForm(forms.ModelForm):
    classroom = forms.ModelChoiceField(queryset=Classroom.objects.all(), empty_label="Select Classroom")
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

class LoginForm(forms.Form):
    email = forms.CharField(max_length=255, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    
class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name']

class ClassroomForm(forms.ModelForm):
    class Meta:
        model = Classroom
        fields = ['name']

class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ['name', 'teacher', 'classroom', 'schedule', 'group', 'semian', 'year', 'type']


class AdminForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = ['user', 'admin_code']

    user = forms.ModelChoiceField(queryset=User.objects.all(), to_field_name='email')

