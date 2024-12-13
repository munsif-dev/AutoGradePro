from rest_framework import serializers
from django.contrib.auth.models import User  # Import Django's built-in User model
from .models import Lecturer
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Lecturer, Student


# UserSerializer (handles user creation and updating)
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)  # Create a new user with hashed password
        return user


# LecturerSerializer (handles creation of Lecturer with linked User)
class LecturerSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Lecturer
        fields = ['user', 'lecturer_name', 'lecturer_email']

    def create(self, validated_data):
        user_data = validated_data.pop('user')  # Extract user data
        user = User.objects.create_user(**user_data)  # Create User instance
        lecturer = Lecturer.objects.create(user=user, **validated_data)  # Create Lecturer instance
        return lecturer


# StudentSerializer (handles creation of Student with linked User)
class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Student
        fields = ['user', 'student_name', 'student_email', 'roll_number']

    def create(self, validated_data):
        user_data = validated_data.pop('user')  # Extract user data
        user = User.objects.create_user(**user_data)  # Create User instance
        student = Student.objects.create(user=user, **validated_data)  # Create Student instance
        return student
