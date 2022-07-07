
from django import forms

class StudentForm(forms.Form):
    sname = forms.CharField()
    marks = forms.IntegerField()
    email = forms.EmailField()
    mobile = forms.IntegerField()
    address = forms.CharField()
