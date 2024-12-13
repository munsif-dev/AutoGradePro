from django.db import models
from django.contrib.auth.models import User


# Lecturer model
class Lecturer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    lecturer_name = models.CharField(max_length=100)
    lecturer_email = models.EmailField()

    def __str__(self):
        return self.lecturer_name


# Student model
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    student_name = models.CharField(max_length=100)
    student_email = models.EmailField()
    roll_number = models.CharField(max_length=100)

    def __str__(self):
        return self.student_name
