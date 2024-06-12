from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def test(request):
    result='<h1> Hai Chellooo!</h1>'
    return HttpResponse(result)