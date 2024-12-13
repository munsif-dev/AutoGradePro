from django.db import models
from django.contrib.auth.models import User


# Lecturer model
class Lecturer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    University = models.CharField(max_length=100 ,null=True)
    Department = models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.lecturer_name


# Student model
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    University = models.CharField(max_length=100, null=True)
    Index_number = models.CharField(max_length=100, null=True)
    

    def __str__(self):
        return self.student_name
