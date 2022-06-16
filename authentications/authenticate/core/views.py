from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from. forms import createuserform
# Create your views here.


def registerview(request):
    if request.method=='POST':
        form=createuserform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form=createuserform()
    context={
        "form":form
    }
    return render(request,'common/register.html',context)

def homeview(request):
    return render(request,'common/home.html')

def welcomeview(request):
    return render(request,'common/welcome.html')