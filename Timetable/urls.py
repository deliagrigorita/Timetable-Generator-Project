from django.urls import path
from .views.index import index
from .views.add_student import add_student

urlpatterns = [
    path('', index, name='index'),
    path('add_student/', add_student, name='add_student'),
]
