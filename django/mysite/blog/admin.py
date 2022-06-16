from django.contrib import admin
from .models import post
# Register your models here.
class postAdmin(admin.ModelAdmin):
    list_display=['title','date_created','author']

admin.site.register(post,postAdmin)