from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def whattime(request):
    time = datetime.datetime.now()
    return HttpResponse('<h1> what is time Now :' +(str(time))+ '</h1>')