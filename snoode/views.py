from django.shortcuts import render

def hello_fishy(request):
    return render(request, 'index.html')
