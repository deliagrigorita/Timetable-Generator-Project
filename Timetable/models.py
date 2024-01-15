from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=2555, unique=True)
    password = models.CharField(max_length=128)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField(null=True)

    def __str__(self):
        return self.email


class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    admin_code = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username  

    class Meta:
        verbose_name = 'Admin'
        verbose_name_plural = 'Admins'



class Student(User):
    matricol = models.CharField(max_length=128, default='111222333444')

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Teacher(User):
    name = models.ManyToManyField(Subject)
    # Additional fields for Teacher if needed

    # class Meta:
    #     verbose_name = 'Teacher'
    #     verbose_name_plural = 'Teachers'
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


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

class Type(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.type
    
class StudentYear(models.Model):
    id = models.AutoField(primary_key=True)
    year = models.CharField(max_length=50)

    def __str__(self):
        return self.year
    
class StudentSemian(models.Model):
    id = models.AutoField(primary_key=True)
    semian = models.CharField(max_length=50)

    def __str__(self):
        return self.semian
    
class StudentGroup(models.Model):
    id = models.AutoField(primary_key=True)
    group = models.CharField(max_length=50)

    def __str__(self):
        return self.group

class Class(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE, related_name='classes')
    classroom = models.ForeignKey('Classroom', on_delete=models.CASCADE, related_name='classes')
    schedule = models.ForeignKey('Schedule', on_delete=models.CASCADE, related_name='classes')
    group = models.ForeignKey('StudentGroup', on_delete=models.CASCADE, default='group', related_name='classes', null=True)
    semian = models.ForeignKey('StudentSemian', on_delete=models.CASCADE, default='semian', related_name='classes', null=True)
    year =  models.ForeignKey('StudentYear', on_delete=models.CASCADE, default='year', related_name='classes', null=True)
    type =  models.ForeignKey('Type', on_delete=models.CASCADE, default='type', related_name='classes', null=True)

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
    
