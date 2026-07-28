from django.urls import path
from. import views
urlpatterns=[
    path('get/', views.student_list, name='student_list'),
    path('post/', views.add_student, name='add_student'),
    
]