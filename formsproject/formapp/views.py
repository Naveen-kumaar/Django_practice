from django.shortcuts import render
from . import forms

# Create your views here.
def studentsDetails(request):
    stuinfo = forms.StudentInfoForm()
    studentinfo ={'form':stuinfo}
    return render(request,'formapp/index.html',context=studentinfo)
