from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Lecturer
from django.contrib.auth.models import User
from .serializers import UserSerializer, LecturerSerializer

# Create your views here.
