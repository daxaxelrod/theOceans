from django.shortcuts import render
from django.http import HttpResponse

def hello_fishy(request):
    return HttpResponse("hello fish")
    
