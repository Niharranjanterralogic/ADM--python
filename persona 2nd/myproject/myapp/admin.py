# Register your models here.
from django.contrib import admin
from . models import Student
# Register your models here.
@admin.register(Student)
class studentAdmin(admin.ModelAdmin):
    list_display=['id','image','firstName','lastName','gender','age','location','occupation','uploadedby','uploadedon','noofdownloads']


