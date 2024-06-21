from django.shortcuts import render
from patient_detail.models import Patient

# Create your views here.
def home(request):
    return render(request,'home.html')

def register(request):
    if request.method == "POST":
        Aname=request.POST.get('Name')
        Amail=request.POST.get('Email')
        Apwd=request.POST.get('Password')
        Acpwd=request.POST.get('Conform_password')
    return render(request,'register.html')