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
    return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'PATCH'])
def updateStudent(request,pk):
    try:
        student=Student.objects.get(id=pk)
    except Student.DoesNotExist:
        return Response("Not Found")
    if request.method=='PATCH':
        serializer=StudentSerializer(student,data=request.data, partial=True)
    else:
        serializer=StudentSerializer(student , data=request.data)
        
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response("Error")




@api_view(['DELETE'])
def del_student(request, pk):
    try:
        student=Student.objects.get(id=pk)
    except Student.DoesNotExist:
        return Response("Not Found")
    student.delete()
    return Response("Deleted Successfully")