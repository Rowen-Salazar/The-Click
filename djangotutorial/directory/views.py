
from django.shortcuts import get_object_or_404, render
from directory.models import Map
#from django.http import HttpResponse

def home(request):
    map_list = Map.objects.all()
    return render(request, 'home.html', {'map_list': map_list})

def about(request):
    return render(request, 'about.html')

def mapview(request, map_name):
    full_map = get_object_or_404(Map, name=map_name)
    return render(request, 'mapview.html', {'full_map': full_map})

def buildingview(request):
    return render(request, 'buildingview.html')
