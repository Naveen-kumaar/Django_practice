from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def create(request):
    message="<h1> vanakkam doi </h1>"
    return HttpResponse(message)