from django.urls import path
from . import views

urlpatterns = [
    path('lecturers/', views.get_lecturers, name='get_lecturers'),
    path('lecturers/create/', views.create_lecturer, name='create_lecturer'),
    path('students/', views.get_students, name='get_students'),
    path('students/create/', views.create_student, name='create_student'),
    path('courses/', views.get_courses, name='get_courses'),
    path('courses/create/', views.create_course, name='create_course'),
    path('assignments/', views.get_assignments, name='get_assignments'),
    path('assignments/create/', views.create_assignment, name='create_assignment'),
    path('submissions/', views.get_submissions, name='get_submissions'),
    path('submissions/create/', views.create_submission, name='create_submission'),
    path('grading-results/', views.get_grading_results, name='get_grading_results'),
    path('grading-results/create/', views.create_grading_result, name='create_grading_result'),
]


