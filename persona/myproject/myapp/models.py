from django.db import models

# Create your models here.
class Student(models.Model):
    image=models.ImageField(null=True)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    gender=models.CharField(max_length=10)
    age=models.IntegerField()
    location=models.CharField(max_length=200)
    occupation=models.CharField(max_length=100)
    uploaded_by=models.CharField(max_length=100)
    uploaded_on=models.DateTimeField(auto_now_add=True)
    no_of_downloads=models.IntegerField()

    def __str__(self):
        return self.first_name 