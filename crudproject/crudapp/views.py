from django.shortcuts import render,redirect
from crudapp.models import student
from crudapp.forms import studentform

# Create your views here.
def select_view(request):
    student1 = student.objects.all()
    student2 = {'student':student1}

    return render(request,'crudapp/index.html',context=student2)

def create_view(request):
    form = studentform()
    if request.method =='POST':
        form =studentform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/check')
        return render(request,'crudapp/create.html',{'form':form})
    
def delete_view(request,id):
    students = student.objects.get(id=id)
    students.delete()
    return redirect('/check')

def update_view(request,id):
    students = student.objects.get(id=id)
    if request.method == 'POST':
        form = studentform(request.POST,instance = student)
        if form.is_valid():
            form.save()
            return redirect('/check')
    return render(request,'crudapp/update.html',{'student':students})
