from django.urls import path

from studentapp  import  views

urlpatterns = [

    path('students/', views.StudentListView,
         name="student_list"),

    path('students/create/', views.StudentCreateView,
         name="student_create"),

    path('students/<int:pk>/update/', views.StudentUpdateView,
         name="student_update"),

    path('students/<int:pk>/delete/', views.StudentDeleteView,
         name="student_delete"),

    path('students/<int:pk>/detail/', views.StudentDetailView,
         name="student_detail"),
]