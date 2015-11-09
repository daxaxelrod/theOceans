from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader




def hello_fishy(request):
    #template = render(request, "index.html" )
    return render(request, "index.html")
