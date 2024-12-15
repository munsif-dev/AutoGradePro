from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import LecturerSerializer, StudentSerializer, ModuleSerializer, AssignmentSerializer, SubmissionSerializer    
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Lecturer, Student, Module, Assignment, Submission  


class ModuleListCreate(generics.ListCreateAPIView):
    serializer_class = ModuleSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        # Only allow the lecturer who owns the module to delete it
        user = self.request.user
        if hasattr(user, 'lecturer'):  # Check if the user is a lecturer
            return Module.objects.filter(lecturer=user.lecturer)
        return Module.objects.none()  # Prevent unauthorized users
    
    
    def perform_create(self, serializer):
        user = self.request.user
        try:
            # Get the associated lecturer
            lecturer = Lecturer.objects.get(user=user)
            # Save the new module with the lecturer
            serializer.save(lecturer=lecturer)
        except Lecturer.DoesNotExist:
            # Raise an error or handle appropriately if no lecturer is found
            raise Exception("The user is not associated with a lecturer.")
        
  
class ModuleDeleteView(generics.DestroyAPIView):
    serializer_class = ModuleSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Only allow the lecturer who owns the module to delete it
        user = self.request.user
        if hasattr(user, 'lecturer'):  # Check if the user is a lecturer
            return Module.objects.filter(lecturer=user.lecturer)
        return Module.objects.none()  # Prevent unauthorized users
    
    
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