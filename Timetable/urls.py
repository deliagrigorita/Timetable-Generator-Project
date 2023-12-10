from django.urls import path, include
from django.contrib import admin
from django.http import HttpResponse
from .views.index_view import index
from .views.add_student_view import add_student
from .views.add_student_view import update_student
from .views.add_student_view import delete_student
from .views.add_student_view import get_student
from .views.add_student_view import get_all_students
from .views.add_teacher_view import add_teacher
from .views.add_teacher_view import update_teacher
from .views.add_teacher_view import delete_teacher
from .views.add_teacher_view import get_all_teachers
from .views.add_resource_view import add_resource
from .views.add_resource_view import update_resource
from .views.add_resource_view import delete_resource
from .views.add_resource_view import get_all_resources
from .views.add_schedule_vie import add_schedule
from .views.add_schedule_vie import update_schedule
from .views.add_schedule_vie import delete_schedule
from .views.add_schedule_vie import get_all_schedules
from .views.add_timetable_view import add_timetable
from .views.add_timetable_view import update_timetable
from .views.add_timetable_view import delete_timetable
from .views.add_timetable_view import get_all_timetables
from .views.auth_view import login, user_logout




urlpatterns = [
    path('', index, name='index'),
    path('add_student/', add_student, name='add_student'),
    path('update_student/<int:student_id>/', update_student, name='update_student'),
    path('delete_student/<int:student_id>/', delete_student, name='delete_student'),
    path('get_student/<int:user_id>/', get_student, name='get_student'),
    path('get_students/', get_all_students, name='get_students'),  

    path('favicon.ico', lambda x: HttpResponse(status=204)),

    path('add_teacher/', add_teacher, name='add_teacher'),
    path('update_teacher/<int:teacher_id>/', update_teacher, name='update_teacher'),
    path('delete_teacher/<int:teacher_id>/', delete_teacher, name='delete_teacher'),
    path('get_teachers/', get_all_teachers, name='get_teachers'),

    path('add_resource/', add_resource, name='add_resource'),
    path('update_resource/<int:resource_id>/', update_resource, name='update_resource'),
    path('delete_resource/<int:resource_id>/', delete_resource, name='delete_resource'),
    path('get_resources/', get_all_resources, name='get_resources'),


    path('add_schedule/', add_schedule, name='add_schedule'),
    path('update_schedule/<int:schedule_id>/', update_schedule, name='update_schedule'),
    path('delete_schedule/<int:schedule_id>/', delete_schedule, name='delete_schedule'),
    path('get_schedules/', get_all_schedules, name='get_schedules'),

    path('add_timetable/', add_timetable, name='add_timetable'),
    path('update_timetable/<int:timetable_id>/', update_timetable, name='update_timetable'),
    path('delete_timetable/<int:timetable_id>/', delete_timetable, name='delete_timetable'),
    path('get_timetables/', get_all_timetables, name='get_timetables'),

    path('auth/', login, name='login'),
    path('logout/', user_logout, name='logout'), 
    


]


