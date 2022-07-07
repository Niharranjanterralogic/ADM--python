from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from. forms import createuserform
# Create your views here.


def registerview(request):
    if request.method=='POST':
        form=createuserform(request.POST)
        if form.is_valid():
            form.save()                                               
            return redirect("home") #here if register id successfull then move to ist page                    #register page view
    else:
        form=createuserform()
    context={
        "form":form
    }
    return render(request,'common/register.html',context)

def homeview(request):
    return render(request,'common/home.html')  # where the login register forgotpasss

def welcomeview(request):
    return render(request,'common/welcome.html')