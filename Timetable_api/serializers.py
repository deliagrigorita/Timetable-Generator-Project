from rest_framework import serializers
from Timetable.models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["id", "email", "password", "first_name", "last_name", "date_of_birth", "matricol"]
