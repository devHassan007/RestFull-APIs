from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status

from .models import Student

@api_view(['GET'])
def student_list(request):
    students=Student.objects.all()
    serializer=StudentSerializer(students, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def add_student(request):
    serializer=StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.error , status=status.HTTP_400_BAD_REQUEST)