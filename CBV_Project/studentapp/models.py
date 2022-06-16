
from django.db import models
from django.urls import reverse

class Student(models.Model):
    sname = models.CharField(max_length=30)
    marks = models.IntegerField()
    email = models.EmailField(unique=True)
    mobile = models.BigIntegerField()
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.sname

    def get_absolute_url(self):
        return reverse('student_list')







