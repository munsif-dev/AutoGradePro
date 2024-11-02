from rest_framework import serializers
from django.contrib.auth.models import User  # Import Django's built-in User model
from .models import Lecturer, Student, Course, Assignment, Submission, GradingResult

class UserSerializer(serializers.ModelSerializer):
    """Serializer for the User model, if additional fields are needed."""

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']  # Use only necessary fields


class LecturerSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Lecturer
        fields = ['user', 'lecturer_name', 'lecturer_email', 'department']


class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Student
        fields = ['user', 'student_name', 'student_email', 'year', 'semester']


class CourseSerializer(serializers.ModelSerializer):
    lecturer = LecturerSerializer()

    class Meta:
        model = Course
        fields = ['id', 'course_name', 'lecturer', 'semester', 'year']


class AssignmentSerializer(serializers.ModelSerializer):
    course = CourseSerializer()

    class Meta:
        model = Assignment
        fields = ['id', 'assignment_title', 'course', 'due_date', 'description', 'total_marks']


class SubmissionSerializer(serializers.ModelSerializer):
    assignment = AssignmentSerializer()
    student = StudentSerializer()

    class Meta:
        model = Submission
        fields = ['id', 'assignment', 'student', 'submission_file_path', 'submitted_at']


class GradingResultSerializer(serializers.ModelSerializer):
    submission = SubmissionSerializer()

    class Meta:
        model = GradingResult
        fields = ['id', 'submission', 'grade', 'feedback', 'graded_at']
