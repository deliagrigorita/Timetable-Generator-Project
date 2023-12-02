from django.urls import path
from django.http import HttpResponse
from .views.index_view import index
from .views.add_student_view import add_student
from .views.add_student_view import update_student
from .views.add_student_view import delete_student
from .views.add_student_view import get_student
from .views.add_student_view import get_all_students


urlpatterns = [
    path('', index, name='index'),
    path('add_student/', add_student, name='add_student'),
    path('update_student/<int:student_id>/', update_student, name='update_student'),
    path('delete_student/<int:student_id>/', delete_student, name='delete_student'),
    path('get_student/<int:user_id>/', get_student, name='get_student'),
    path('get_students/', get_all_students, name='get_students'),  

    path('favicon.ico', lambda x: HttpResponse(status=204)),
]
