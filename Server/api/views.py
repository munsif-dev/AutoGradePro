from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Lecturer, Student, Course, Assignment, Submission, GradingResult
from django.contrib.auth.models import User
from .serializers import UserSerializer,LecturerSerializer, StudentSerializer, CourseSerializer, AssignmentSerializer, SubmissionSerializer, GradingResultSerializer

# Lecturer Views

@api_view(['GET'])
def get_all_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()  # This calls the `create` method in the serializer
        return Response({"message": "User created successfully", "user": serializer.data}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_lecturers(request):
    lecturers = Lecturer.objects.all()
    if not lecturers:
        return Response({'message': 'No lecturers found.'}, status=status.HTTP_404_NOT_FOUND)
    serialized_lecturers = LecturerSerializer(lecturers, many=True).data
    return Response(serialized_lecturers)

@api_view(['POST'])
def create_lecturer(request):
    serializer = LecturerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Student Views
@api_view(['GET'])
def get_students(request):
    students = Student.objects.all()
    if not students:
        return Response({'message': 'No students found.'}, status=status.HTTP_404_NOT_FOUND)
    serialized_students = StudentSerializer(students, many=True).data
    return Response(serialized_students)

@api_view(['POST'])
def create_student(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Course Views
@api_view(['GET'])
def get_courses(request):
    courses = Course.objects.all()
    if not courses:
        return Response({'message': 'No courses found.'}, status=status.HTTP_404_NOT_FOUND)
    serialized_courses = CourseSerializer(courses, many=True).data
    return Response(serialized_courses)

@api_view(['POST'])
def create_course(request):
    serializer = CourseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Assignment Views
@api_view(['GET'])
def get_assignments(request):
    assignments = Assignment.objects.all()
    if not assignments:
        return Response({'message': 'No assignments found.'}, status=status.HTTP_404_NOT_FOUND)
    serialized_assignments = AssignmentSerializer(assignments, many=True).data
    return Response(serialized_assignments)

@api_view(['POST'])
def create_assignment(request):
    serializer = AssignmentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Submission Views
@api_view(['GET'])
def get_submissions(request):
    submissions = Submission.objects.all()
    if not submissions:
        return Response({'message': 'No submissions found.'}, status=status.HTTP_404_NOT_FOUND)
    serialized_submissions = SubmissionSerializer(submissions, many=True).data
    return Response(serialized_submissions)

@api_view(['POST'])
def create_submission(request):
    serializer = SubmissionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# GradingResult Views
@api_view(['GET'])
def get_grading_results(request):
    grading_results = GradingResult.objects.all()
    if not grading_results:
        return Response({'message': 'No grading results found.'}, status=status.HTTP_404_NOT_FOUND)
    serialized_grading_results = GradingResultSerializer(grading_results, many=True).data
    return Response(serialized_grading_results)

@api_view(['POST'])
def create_grading_result(request):
    serializer = GradingResultSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
