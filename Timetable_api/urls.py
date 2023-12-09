# from django.conf.urls import url
from django.urls import path, include
from .views import (
    StudentListApiView,
    StudentDetailApiView
)

urlpatterns = [
    path('api/students', StudentListApiView.as_view()),
    path('api/students/<int:student_id>/', StudentDetailApiView.as_view()),
]
