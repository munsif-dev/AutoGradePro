from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import LecturerSerializer, StudentSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Lecturer, Student

# Create your views here.
class CreateLecturerView(generics.CreateAPIView):
    queryset = Lecturer.objects.all()
    serializer_class = LecturerSerializer
    permission_classes = [AllowAny]

# View for creating a Student
class CreateStudentView(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [AllowAny]