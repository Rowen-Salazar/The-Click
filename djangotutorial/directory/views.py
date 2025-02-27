
from django.shortcuts import get_object_or_404, render
from directory.models import Map, Location
from django.conf import settings
from django.views import View
#from django.http import HttpResponse

def home(request):
    map_list = Map.objects.all()
    return render(request, 'home.html', {'map_list': map_list})

#def about(request):
#    return render(request, 'about.html')

def mapview(request, map_name):
    full_map = get_object_or_404(Map, name=map_name)
    all_locations = Location.objects.all()
    context = {
        'full_map': full_map,
        'all_locations': all_locations
    }
    return render(request, 'mapview.html', context)

def buildingview(request):
    return render(request, 'buildingview.html')

def my_view(request):
    return render(request, 'home.html', {'MEDIA_URL': settings.MEDIA_URL})

