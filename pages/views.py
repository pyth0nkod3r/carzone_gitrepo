from django.shortcuts import render
from .models import Team

# Create your views here.

def homepage(request):
    teams = Team.objects.all()
    data = {'team': teams}
    return render(request, 'pages/homepage.html', data)

def about(request):
    teams = Team.objects.all()
    data = {'team': teams}
    return render(request, 'pages/about.html', data)

def services(request):
    return render(request, 'pages/services.html')

def contact(request):
    return render(request, 'pages/contact.html')