from django.db import models

# Create your models here.
class Student(models.Model):
    image=models.ImageField(null=True)
    firstName=models.CharField(max_length=100)
    lastName=models.CharField(max_length=100)
    gender=models.CharField(max_length=10)
    age=models.IntegerField()
    location=models.CharField(max_length=200)
    occupation=models.CharField(max_length=100)
    uploadedby=models.CharField(max_length=100)
    uploadedon=models.DateTimeField(auto_now_add=True)
    noofdownloads=models.IntegerField()

    def __str__(self):
        return self.firstName 