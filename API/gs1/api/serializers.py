from rest_framework import serializers
from .models import Student


class studentserializers(serializers.Serializer):
#     gender_choices=[
#     ('M','Male'),
#     ('F','Female')
# ]

    image=serializers.ImageField()
    first_name=serializers.CharField(max_length=100)
    last_name=serializers.CharField(max_length=100)
    gender=serializers.CharField(max_length=10)
    age=serializers.IntegerField()
    location=serializers.CharField(max_length=200)
    occupation=serializers.CharField(max_length=100)
    uploaded_by=serializers.CharField(max_length=100)
    uploaded_on=serializers.DateTimeField()
    no_of_downloads=serializers.IntegerField()

    def create(self,validated_data):
        return Student.objects.create(**validated_data)

    def update(self,instance,validated_data):
        # print(instance.name)
        instance.image=validated_data.get('image',instance.image)
        # print(instance.name)
        instance.first_name=validated_data.get('first_name',instance.first_name)
        instance.last_name=validated_data.get('last_name',instance.last_name)
        instance.gender=validated_data.get('gender',instance.gender)
        instance.age=validated_data.get('age',instance.age)
        instance.location=validated_data.get('location',instance.location)
        instance.occupation=validated_data.get('occupation',instance.occupation)
        instance.uploaded_by=validated_data.get('uploaded_by',instance.uploaded_by)
        instance.uploaded_on=validated_data.get('uploaded_on',instance.uploaded_on)
        instance.no_of_downloads=validated_data.get('no_of_downloads',instance.no_of_downloads)
        instance.save()
        return instance
# from rest_framework import serializers
# from .models import Student

# class StudentSerializer(serializers.Serializer):
#     class Meta:
#         model=Student
#         fields="__all__"