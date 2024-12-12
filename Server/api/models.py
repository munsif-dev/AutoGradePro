from django.db import models
from django.contrib.auth.models import User  # Import Django's built-in User model

# Lecturer model
class Lecturer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)  # Specify User as the related model
    lecturer_name = models.CharField(max_length=100)
    lecturer_email = models.EmailField()
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.lecturer_name







# Course model