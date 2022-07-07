from django.contrib import admin
from . models import Student
# Register your models here.
@admin.register(Student)
class studentAdmin(admin.ModelAdmin):
    list_display=['id','image','first_name','last_name','gender','age','location','occupation','uploaded_by','uploaded_on','no_of_downloads']