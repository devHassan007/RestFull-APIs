from django.urls import path
from . import views
urlpatterns = [
    path('student/', views.Student_List, name='Student_List'),   
]