from rest_framework import serializers
from myapp.models import Student

class studentserializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields="__all__"