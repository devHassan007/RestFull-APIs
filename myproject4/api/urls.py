from django.urls import path
from .views import StudentListCreateAPI, StudentRetrieveUpdateDeleteAPI

urlpatterns = [
    path('student/', StudentListCreateAPI.as_view()), 
    path('student/<int:pk>/', StudentRetrieveUpdateDeleteAPI.as_view()), 
]