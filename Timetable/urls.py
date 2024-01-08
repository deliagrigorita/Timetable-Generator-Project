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
from .views.add_schedule_view import add_schedule
from .views.add_schedule_view import update_schedule
from .views.add_timetable_view import add_timetable
from .views.add_timetable_view import update_timetable
from .views.add_timetable_view import delete_timetable
from .views.add_timetable_view import get_all_timetables
from .views.auth_view import login, user_logout
from .views.add_subject_view import add_subject
from .views.add_subject_view import update_subject
from .views.add_subject_view import delete_subject
from .views.add_subject_view import get_all_subjects
from .views.add_classroom_view import add_classroom
from .views.add_classroom_view import update_classroom
from .views.add_classroom_view import delete_classroom
from .views.add_classroom_view import get_all_classrooms
from .views.add_class_view import add_class
from .views.add_class_view import update_class
from .views.add_class_view import delete_class
from .views.add_class_view import get_all_classes
from .views.add_admin_view import add_admin
from .views.add_admin_view import update_admin
from .views.add_admin_view import delete_admin
from .views.add_admin_view import get_all_admins


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

    path('add_timetable/', add_timetable, name='add_timetable'),
    path('update_timetable/<int:timetable_id>/', update_timetable, name='update_timetable'),
    path('delete_timetable/<int:timetable_id>/', delete_timetable, name='delete_timetable'),
    path('get_timetables/', get_all_timetables, name='get_timetables'),

    path('auth/', login, name='login'),
    path('logout/', user_logout, name='logout'), 
    

    path('add_subject/', add_subject, name='add_subject'),
    path('update_subject/<int:subject_id>/', update_subject, name='update_subject'),
    path('delete_subject/<int:subject_id>/', delete_subject, name='delete_subject'),
    path('get_subjects/', get_all_subjects, name='get_subjects'),

    path('add_classroom/', add_classroom, name='add_classroom'),
    path('update_classroom/<int:classroom_id>/', update_classroom, name='update_classroom'),
    path('delete_classroom/<int:classroom_id>/', delete_classroom, name='delete_classroom'),
    path('get_classrooms/', get_all_classrooms, name='get_classrooms'),

    path('add_class/', add_class, name='add_class'),
    path('update_class/<int:class_id>/', update_class, name='update_class'),
    path('delete_class/<int:class_id>/', delete_class, name='delete_class'),
    path('get_classes/', get_all_classes, name='get_classes'),

    path('add_admin/', add_admin, name='add_admin'),
    path('update_admin/<int:admin_id>/', update_admin, name='update_admin'),
    path('delete_admin/<int:admin_id>/', delete_admin, name='delete_admin'),
    path('get_admins/', get_all_admins, name='get_admins'),
]


