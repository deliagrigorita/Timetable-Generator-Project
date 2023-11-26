from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return self.email


class Admin(User):
    # Additional fields for Admin if needed

    class Meta:
        verbose_name = 'Admin'
        verbose_name_plural = 'Admins'


class Student(User):
    # Additional fields for Student if needed

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'


class Teacher(User):

    class Meta:
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'


class Resource(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    classroom = models.ForeignKey('Classroom', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Classroom(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Schedule(models.Model):
    id = models.AutoField(primary_key=True)
    day = models.CharField(max_length=15)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.day} - {self.start_time} to {self.end_time}"


class Class(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Timetable(models.Model):
    id = models.AutoField(primary_key=True)
    classes = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return f"Timetable {self.id}"
