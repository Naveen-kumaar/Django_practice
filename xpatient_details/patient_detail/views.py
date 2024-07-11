from django.shortcuts import render,redirect
from patient_detail.models import Patient
from patient_detail.forms import Patientform
from patient_detail.forms import Loginform

# # Create your views here.
# def home(request):
#     return render(request,'home.html')

# def register(request):
    # if request.method == "POST":
    #     Aname=request.POST.get('Name')
    #     Amail=request.POST.get('Email')
    #     Apwd=request.POST.get('Password')
    #     Acpwd=request.POST.get('Conform_password')
    # return render(request,'register.html')

def select_view(request):
    patient1 = Patient.objects.all()
    patient2 = {'patient':patient1}

    return render(request,"base.html",context=patient2)

def create_view(request):
    form = Patientform()
    if request.method =='POST':
        form =Patientform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/check')
        return render(request,'home.html',{'form':form})
def login(request):
    form = Loginform()
    if request.method =='POST':
        form = Loginform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/check')
        return render(request,'login.html',{'form':form})