
from django.shortcuts import render
from directory.models import Map
from django.views.generic import ListView
from .models import *
#from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

class HomeView(ListView):
    template_name = "directory/templates/home.html"
    context_object = 'my_data'
    model = Locations
    success_url = "/"


def about(request):
    return render(request, 'about.html')
    
#def mapview(request, maps):
    #maps = Map.objects.all()
    #return render(request, 'mapview.html', {'mapview/':maps})

def mapview(request):
    return render(request, 'mapview.html')

def buildingview(request):
    return render(request, 'buildingview.html')
