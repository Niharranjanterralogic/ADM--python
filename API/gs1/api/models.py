from django.db import models

# gender_choices=[
#     ('M','Male'),
#     ('F','Female')
# ]
# Create your models here.
class Student(models.Model):
    # gender_choices=[
    # ('M','Male'),
    # ('F','Female')
# ]
    image=models.ImageField()
    first_name=models.CharField(max_length=100,null=True)
    last_name=models.CharField(max_length=100,null=True)
    gender=models.CharField(max_length=10)
    age=models.IntegerField(null=True)
    location=models.CharField(max_length=200,null=True)
    occupation=models.CharField(max_length=100,null=True)
    uploaded_by=models.CharField(max_length=100,null=True)
    uploaded_on=models.DateTimeField(auto_now_add=True,null=True)
    no_of_downloads=models.IntegerField(null=True)

    def __str__(self):
        return self.first_name 

    