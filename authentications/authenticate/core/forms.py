from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class createuserform(UserCreationForm):
    email=forms.EmailField()
                                                      #forms  for to create registrations page
    class Meta:
        model=User
        fields=['username','email','password1','password2']
