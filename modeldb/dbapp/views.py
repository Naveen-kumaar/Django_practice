from django.shortcuts import render
from dbapp.models import students

# Create your views here.
def student(request):
    stud_data = students.objects.all()
    stud_dict = {'stud_list':stud_data}
    return render(request,'dbapp/index.html',context= stud_dict)