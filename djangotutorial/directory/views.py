
from django.shortcuts import render, get_object_or_404
from directory.models import Map
#from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

#def mapview(request):
#    maps = Map.objects.all()
#    return render(request, 'mapview.html', {'mapview/': maps})

def untmaincampus(request):
    maps = get_object_or_404(Map, name="UNT Test Map")
    return render(request, 'maincampusview.html', {'maincampusview': maps})

def discoverypark(request):
    maps = get_object_or_404(Map, name="DP Test Map")
    return render(request, 'dpcampusview.html', {'dpcampusview': maps})

def buildings(request):
    return render(request, 'buildingview.html')
