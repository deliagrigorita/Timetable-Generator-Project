from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from Timetable.models import Student
from .serializers import StudentSerializer


class StudentListApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            'email': request.data.get('email'),
            'password': request.data.get('password'),
            'first_name': request.data.get('first_name'),
            'last_name': request.data.get('last_name'),
            'matricol': request.data.get('matricol')
        }
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentDetailApiView(APIView):
    def get_object(self, student_id):
        try:
            return Student.objects.get(id=student_id)
        except Student.DoesNotExist:
            return None

    def get(self, request, student_id, *args, **kwargs):
        student_instance = self.get_object(student_id)
        if not student_instance:
            return Response(
                {"res": "Student with id does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = StudentSerializer(student_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, student_id, *args, **kwargs):
        student_instance = self.get_object(student_id)
        if not student_instance:
            return Response(
                {"res": "Student with id does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            "email": request.data.get('email'),
            "password": request.data.get('password'),
            "first_name": request.data.get('first_name'),
            "last_name": request.data.get('last_name'),
            "matricol": request.data.get('matricol')
        }
        serializer = StudentSerializer(instance=student_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
