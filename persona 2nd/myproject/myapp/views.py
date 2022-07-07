from django.shortcuts import render
from rest_framework import generics
from myapp.serializers import studentserializer
from myapp.models import Student
# Create your views here.

class Studentlist(generics.ListCreateAPIView):
    queryset=Student.objects.all()
    serializer_class=studentserializer

class Studentdeatils(generics.RetrieveUpdateDestroyAPIView):
    queryset=Student
    serializer_class=studentserializer
