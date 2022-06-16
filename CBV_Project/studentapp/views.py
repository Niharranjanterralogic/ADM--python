
from django.shortcuts import render
from studentapp.models import Student

from django.views.generic import (
    ListView,DetailView,CreateView,UpdateView,DeleteView
)

class StudentListView(ListView):
    model = Student  #  Student.objects.all()
    context_object_name = 'student_list'  # [] |  [{},{},{}]
    template_name = 'studentapp/student_list.html'


class StudentDetailView(DetailView):
    model = Student  #  Student.objects.all()
    context_object_name = 'student'  # [] |  [{},{},{}]
    template_name = 'studentapp/student_detail.html'


class StudentCreateView(CreateView):
    model = Student  # Student.objects.create(f1=v1, f2=v2,...)
    fields = '__all__'
    context_object_name = 'form'
    template_name = 'studentapp/student_form.html'


class StudentUpdateView(UpdateView):
    model = Student  # Student.objects.create(f1=v1, f2=v2,...)
    fields = '__all__'
    context_object_name = 'form'
    template_name = 'studentapp/student_form.html'


class StudentDeleteView(DeleteView):
    model = Student
    success_url = '/students/'

    context_object_name = 'student'
    template_name = 'studentapp/student_confirm_delete.html'

