from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def good_m(request):
    return HttpResponse('<h1> GOOD MORNING </h1>')
def good_a(request):
    return HttpResponse('<h1> GOOD AFTERNOON </h1>')
def good_n(request):
    return HttpResponse('<h1> GOOD NIGHT </h1>')

