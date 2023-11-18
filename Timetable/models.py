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
