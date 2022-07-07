
from django.urls import path,include
from studentapp.api import views

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('students', views.StudentListView)

urlpatterns = [
    path('', include(router.urls)),
]