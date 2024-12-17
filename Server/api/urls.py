from django.urls import path
from . import views

urlpatterns = [
    path ('module/', views.ModuleListCreate.as_view(), name='module-list-create'), # this url is to create a module
    path ('module/<int:pk>/', views.ModuleDeleteView.as_view(), name='module-delete'), # this is to delete a module
    path('module/list/', views.ModuleListView.as_view(), name='module-list'), # this is to list all modules
    path('lecturer/list/', views.GetLecturerView.as_view(), name='create-lecturer'), # this is to create a lecturer
    path('assignment/', views.AssignmentListCreate.as_view(), name='assignment-list-create'), # this is to create an assignment
    path('assignment/<int:pk>/', views.AssignmentDeleteView.as_view(), name='assignment-delete'), # this is to delete an assignment
    path('assignment/list/', views.AssignmentListView.as_view(), name='assignment-list'), # this is to list all assignments
]