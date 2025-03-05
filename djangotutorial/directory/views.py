
from django.shortcuts import get_object_or_404, render
from directory.models import Map, Building, Filter, Location
from django.conf import settings
from django.views import View

def home(request):
    map_list = Map.objects.all()
    return render(request, 'home.html', {'map_list': map_list})

def mapview(request, map_name):
    full_map = get_object_or_404(Map, name=map_name)
    all_locations = Location.objects.all()
    all_filters = Filter.objects.all()
    context = {
        'full_map': full_map,
        'all_locations': all_locations,
        'all_filters': all_filters
    }
    return render(request, 'mapview.html', context)

def buildinglist(request):
    building_list = Building.objects.all()
    return render(request, 'buildingview.html', {'building_list': building_list})

def buildingview(request, building_name):
    full_building = get_object_or_404(Building, name=building_name)
    all_filters = Filter.objects.all()
    context = {
        'full_building': full_building,
        'all_filters': all_filters
    }
    return render(request, 'buildingview.html', context)

def my_view(request):
    return render(request, 'home.html', {'MEDIA_URL': settings.MEDIA_URL})
