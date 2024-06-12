from django.shortcuts import render,redirect
from medz_app.forms import CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages



# Create your views here.
def home(request):
    return render(request,'medz_app/home.html')

def register(request):
    if request.method== 'POST':
        name =request.POST['username']
        # email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            user =User.objects.create_user(username=name,password= password1)
            user.save()
            messages.success(request,'your account has been created successfully...!')
            return redirect('login')
        else:
            messages.warning(request,'Password Mismatching...!!!')
            return redirect('register')
    else:
        form = CreateUserForm()
        return render(request,'medz_app/register.html',{'form':form})

def login(request):
    return render(request,'medz_app/login.html')