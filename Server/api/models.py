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



# Student model
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)  # Specify User as the related model
    student_name = models.CharField(max_length=100)
    student_email = models.EmailField(null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    semester = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.student_name
    
"""
# Course model
class Course(models.Model):
    course_name = models.CharField(max_length=100)
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE, related_name="courses")
    semester = models.IntegerField()
    year = models.IntegerField()

    def __str__(self):
        return self.course_name


# Assignment model
class Assignment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="assignments")
    assignment_title = models.CharField(max_length=100)
    due_date = models.DateField()
    description = models.TextField()
    total_marks = models.IntegerField()

    def __str__(self):
        return self.assignment_title

# Submission model

class Submission(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name="submissions")
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="submissions")
    submission_file = models.FileField(upload_to="submissions/")
    submitted_at = models.DateTimeField(auto_now_add=True)
    grade = models.FloatField(null=True, blank=True)  # Store the grade after evaluation
    graded_at = models.DateTimeField(null=True, blank=True)  # Track when the grading occurred
    feedback = models.TextField(null=True, blank=True)  # Provide feedback or remarks
    status = models.CharField(
        max_length=20,
        choices=[('Pending', 'Pending'), ('Graded', 'Graded')],
        default='Pending'
    )

    def __str__(self):
        return f"Submission {self.pk} for {self.assignment}"


# GradingResult model
class GradingResult(models.Model):
    submission = models.OneToOneField(Submission, on_delete=models.CASCADE, related_name="grading_result")
    grade = models.CharField(max_length=10)
    feedback = models.TextField()
    graded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Grade: {self.grade} for Submission {self.submission.pk}"



"""