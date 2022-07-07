from django.http import JsonResponse
from django.shortcuts import render
from .models import Student
from .serializer import StudentSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

# Create your views here.

@csrf_exempt
def studentAPI(request,id=0):
    if request.method=='GET':
        student=Student.objects.all()
        student_Serializer=StudentSerializer(student,many=True)
        return JsonResponse(student_Serializer.data, safe=False)
    elif request.method=='POST':
        student_data=JSONParser().parse(request)
        student_Serializer=StudentSerializer(data=student_data)
        if student_Serializer.is_valid():
            student_Serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Faild to Add",safe=False)
    elif request.method=='PUT':
        student_data=JSONParser().parse(request)
        student=Student.objects.get()
