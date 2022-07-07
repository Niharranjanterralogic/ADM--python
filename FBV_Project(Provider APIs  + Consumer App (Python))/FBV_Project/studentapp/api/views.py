
from studentapp.models import Student
from studentapp.api.serializers import StudentModelSerializer
from rest_framework import viewsets

class StudentListView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer