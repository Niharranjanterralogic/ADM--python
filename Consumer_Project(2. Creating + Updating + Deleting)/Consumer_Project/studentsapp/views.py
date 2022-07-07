
#  pip install  requests

from django.shortcuts import render,redirect
import requests
import  json
from django.http import HttpResponse
from studentsapp.forms import StudentForm


def StudentListView(request):
    response = requests.get('http://127.0.0.1:9999/api/students/')

    if response.status_code == 200:
        try:
            student_list = json.loads(response.text)
        except ValueError:
            context = {
                "error" : "Sorry, you are not getting JSON response"
            }
            return render(request, 'studentsapp/student_list.html', context)
        else:
            context = {
                "student_list": student_list
            }
            return render(request, 'studentsapp/student_list.html', context)
    else:
        context = {
            "error" : "Requested information not available"
        }
        return render(request,'studentsapp/student_list.html',context)



def StudentDetailView(request,pk):
    response = requests.get("http://127.0.0.1:9999/api/students/"+str(pk)+'/')
    if response.status_code == 200:
        try:
            student = json.loads(response.text)
        except ValueError:
            context = {
                "error" : "Sorry, you are not getting JSON response"
            }
            return render(request, 'studentsapp/student_detail.html', context)
        else:
            context = {
                "student": student
            }
            return render(request, 'studentsapp/student_detail.html', context)
    else:
        context = {
            "error": "Requested Resource not available to get."
        }
        return render(request, 'studentsapp/student_detail.html', context)


def StudentDeleteView(request,pk):
    if request.method=='POST':
        response = requests.delete("http://127.0.0.1:9999/api/students/"+str(pk)+'/')
        if response.status_code == 204:
            return redirect('student_list')
        else:
            context = {
                "error" : "Something wrong. Record not deleted successfully"
            }
            return render(request, 'studentsapp/student_confirm_delete.html', context)

    else:
        response = requests.get("http://127.0.0.1:9999/api/students/"+str(pk)+'/')

        if response.status_code==200:
            try:
                student = json.loads(response.text)
                context = {
                    "student" : student
                }
                return render(request,'studentsapp/student_confirm_delete.html', context)
            except ValueError:
                context = {
                    "error" : json.loads(response.text)
                }
                return render(request,'studentsapp/student_confirm_delete.html',context)

        else:
            context = {
                "error": json.loads(response.text)
            }
            return render(request, 'studentsapp/student_confirm_delete.html', context)


def StudentCreateView(request):
    if request.method=='POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            # sname = request.POST.get("sname")
            # marks = request.POST.get("marks")
            # email = request.POST.get("email")
            # mobile = request.POST.get("mobile")
            # address = request.POST.get("address")

            student_obj = {
                "sname" : request.POST.get("sname"),
                "marks" : request.POST.get("marks"),
                "email" : request.POST.get("email"),
                "mobile" : request.POST.get("mobile"),
                "address" : request.POST.get("address")
            }
            response = requests.post("http://127.0.0.1:9999/api/students/", data=student_obj)
            if response.status_code==201:
                return redirect('student_list')
            else:
                context = {
                    "error" : json.loads(response.text)
                }
                return render(request,'studentsapp/student_form.html',context)

        else:
            context = {
                "error" : "Please send proper data for all fileds"
            }
            return render(request, 'studentsapp/student_form.html', context)
    else:
        form = StudentForm()
        context = {"form" : form}
        return render(request,'studentsapp/student_form.html',context)


def StudentUpdateView(request,pk):
    if request.method=='POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            # sname = request.POST.get("sname")
            # marks = request.POST.get("marks")
            # email = request.POST.get("email")
            # mobile = request.POST.get("mobile")
            # address = request.POST.get("address")

            student_obj = {
                "sname" : request.POST.get("sname"),
                "marks" : request.POST.get("marks"),
                "email" : request.POST.get("email"),
                "mobile" : request.POST.get("mobile"),
                "address" : request.POST.get("address")
            }
            response = requests.put("http://127.0.0.1:9999/api/students/"+str(pk)+'/', data=student_obj)

            if response.status_code==200:
                return redirect('student_list')
            else:
                context = {
                    "error" : json.loads(response.text)
                }
                return render(request,'studentsapp/student_update.html',context)

        else:
            context = {
                "error" : "Please send proper data for all fileds"
            }
            return render(request, 'studentsapp/student_update.html', context)

    else:
        response = requests.get("http://127.0.0.1:9999/api/students/" + str(pk) + '/')
        if response.status_code == 200:
            try:
                student = json.loads(response.text)
            except ValueError:
                context = {
                    "error": "Sorry, you are not getting JSON response"
                }
                return render(request, 'studentsapp/student_update.html', context)
            else:
                context = {
                    "student": student
                }
                return render(request, 'studentsapp/student_update.html', context)
        else:
            context = {
                "error": "Requested Resource not available to get."
            }
            return render(request, 'studentsapp/student_update.html', context)




