
from django.db import models



gender_choices=[
    ('M','Male'),
    ('F','Female')
]
# Create your models here.
class Student(models.Model):
    image=models.ImageField()
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    gender=models.CharField(choices=gender_choices,max_length=10
    )
    age=models.IntegerField()
    location=models.CharField(max_length=200)
    occupation=models.CharField(max_length=100)
    uploaded_by=models.CharField(max_length=100)
    uploaded_on=models.DateTimeField(auto_now_add=True)
    no_of_downloads=models.IntegerField()

    def __str__(self):
        return self.first_name 
