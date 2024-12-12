from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Lecturer
from django.contrib.auth.models import User
from .serializers import UserSerializer, LecturerSerializer


@api_view(['GET', 'POST'])
def lecturer_list(request):
    if request.method == 'GET':
        lecturers = Lecturer.objects.all()
        serializer = LecturerSerializer(lecturers, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = LecturerSerializer(data=request.data)
        if serializer.is_valid():
            user_data = serializer.validated_data.pop('user')
            user = User.objects.create_user(**user_data)
            lecturer = Lecturer.objects.create(user=user, **serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)