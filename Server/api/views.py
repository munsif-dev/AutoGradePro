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
        
class ModuleListView(generics.ListAPIView):
    """
    API view to fetch all modules associated with the authenticated lecturer.
    """
    serializer_class = ModuleSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if hasattr(user, 'lecturer'):  # Check if the user is a lecturer
            return Module.objects.filter(lecturer=user.lecturer)
        return Module.objects.none()  # Return empty queryset if not a lecturer
    
class ModuleDeleteView(generics.DestroyAPIView):
    serializer_class = ModuleSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Only allow the lecturer who owns the module to delete it
        user = self.request.user
        if hasattr(user, 'lecturer'):  # Check if the user is a lecturer
            return Module.objects.filter(lecturer=user.lecturer)
        return Module.objects.none()  # Prevent unauthorized users
    

class AssignmentListCreate(generics.ListCreateAPIView):
    """
    API view to list and create assignments for a specific module.
    Only lecturers associated with the module can perform these actions.
    """
    serializer_class = AssignmentSerializer
    permission_classes = [AllowAny]  # Ensure only authenticated users can access this view

    def get_queryset(self):
        user = self.request.user
        module_id = self.request.query_params.get('module_id')  # Get the module_id from the query parameters

        if module_id and hasattr(user, 'lecturer'):  # Check if the user is a lecturer
            # Fetch assignments for the specified module owned by the lecturer
            return Assignment.objects.filter(module__lecturer=user.lecturer, module__id=module_id)
        
        # If no module_id or unauthorized access, return empty queryset
        return Assignment.objects.none()

    def perform_create(self, serializer):
        """
        Create a new assignment under the module the lecturer owns.
        """
        user = self.request.user
        module_id = self.request.data.get("module_id")
        try:
            # Check if the lecturer owns the specified module
            module = Module.objects.get(id=module_id, lecturer=user.lecturer)
            # Save the assignment with the module
            serializer.save(module=module)
        except Module.DoesNotExist:
            raise Exception("You do not have permission to add assignments to this module.")

class AssignmentListView(generics.ListAPIView):
    """
    API view to fetch all assignments for the modules owned by the authenticated lecturer.
    """
    serializer_class = AssignmentSerializer
    permission_classes = [AllowAny]
    def get_queryset(self):
            user = self.request.user
            module_id = self.request.query_params.get('module_id')  # Get the module_id from the query parameters

            if module_id and hasattr(user, 'lecturer'):  # Check if the user is a lecturer
                # Fetch assignments for the specified module owned by the lecturer
                return Assignment.objects.filter(module__lecturer=user.lecturer, module__id=module_id)
            
            # If no module_id or unauthorized access, return empty queryset
            return Assignment.objects.none()

class AssignmentDeleteView(generics.DestroyAPIView):
    """
    API view to delete an assignment.
    Only the lecturer associated with the module can delete its assignments.
    """
    serializer_class = AssignmentSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        user = self.request.user
        if hasattr(user, 'lecturer'):  # Check if the user is a lecturer
            # Fetch assignments for modules owned by the lecturer
            return Assignment.objects.filter(module__lecturer=user.lecturer)
        return Assignment.objects.none()  # Prevent unauthorized users
    
# Create your views here.
class GetLecturerView(generics.ListAPIView):
    queryset = Lecturer.objects.all()
    serializer_class = LecturerSerializer
    permission_classes = [AllowAny]
    
class CreateLecturerView(generics.CreateAPIView):
    queryset = Lecturer.objects.all()
    serializer_class = LecturerSerializer
    permission_classes = [AllowAny]

# View for creating a Student
class CreateStudentView(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [AllowAny]