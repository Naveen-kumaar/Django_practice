from django import forms

class StudentInfoForm(forms.Form):
    name = forms.CharField(max_length=30)
    password = forms.CharField(max_length=20)

