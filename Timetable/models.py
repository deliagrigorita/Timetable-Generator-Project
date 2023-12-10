from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=2555, unique=True)
    password = models.CharField(max_length=128)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField(null=True)
    #profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)

    def __str__(self):
        return self.email


class Admin(User):
    # admin_code = models.CharField(max_length=20)
    # Additional fields for Admin if needed

    class Meta:
        verbose_name = 'Admin'
        verbose_name_plural = 'Admins'


class Student(User):
    matricol = models.CharField(max_length=128, default='111222333444')
    # Additional fields for Student if needed

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

class Subject(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Teacher(User):
    name = models.ManyToManyField(Subject)
    # Additional fields for Teacher if needed

    class Meta:
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'


class Resource(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=128, default='Please add description')
    classroom = models.ForeignKey('Classroom', on_delete=models.CASCADE)
    availability = models.BooleanField(default=True)

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
    resources = models.ManyToManyField(Resource)

    def __str__(self):
        return self.name


class Timetable(models.Model):
    id = models.AutoField(primary_key=True)
    classes = models.ForeignKey(Class, on_delete=models.CASCADE)
    semester = models.CharField(max_length=20, null=True)
    academic_year = models.CharField(max_length=10, null=True)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f"Timetable {self.id} - {self.classes.name}"
