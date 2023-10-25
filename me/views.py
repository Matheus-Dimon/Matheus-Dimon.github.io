from django.shortcuts import render

def index(request):
    return render(request, 'templates/index.html')

def welcome(request):
    return render(request, 'templates/welcome.html')
