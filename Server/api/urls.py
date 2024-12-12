from django.urls import path
from .views import lecturer_list

urlpatterns = [
    path('lecturers/', lecturer_list),
]


