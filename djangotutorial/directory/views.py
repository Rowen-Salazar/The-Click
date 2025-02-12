
from django.shortcuts import render
from directory.models import Map
#from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def mapview(request, maps):
    maps = Map.objects.all()
    return render(request, 'mapview.html', {'mapview/':maps})

def buildingview(request):
    return render(request, 'buildingview.html')
