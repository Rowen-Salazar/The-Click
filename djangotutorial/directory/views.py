
from django.shortcuts import get_object_or_404, render
from directory.models import Map, Building, Filter, Location, POI, POIFilter
from django.conf import settings
from django.views import View

def home(request):
    map_list = Map.objects.all()
    return render(request, 'home.html', {'map_list': map_list})

def mapview(request, map_name):
    full_map = get_object_or_404(Map, name=map_name)
    all_locations = Location.objects.all()
    all_filters = Filter.objects.all()
    building_list = Building.objects.all() # this makes sure building sidebar content always loads
    context = {
        'full_map': full_map,
        'all_locations': all_locations,
        'all_filters': all_filters,
        'building_list': building_list # this makes sure building sidebar content always loads
    }
    return render(request, 'mapview.html', context)

def buildinglist(request):
    building_list = Building.objects.all()
    return render(request, 'buildingview.html', {'building_list': building_list})

def buildingview(request, building_name):
    full_building = get_object_or_404(Building, slug=building_name)
    all_categories = POIFilter.objects.all()  # Get all POI categories
    building_list = Building.objects.all() # this makes sure building sidebar content always loads
    
    # Handle category filtering
    selected_categories = request.GET.getlist('category')
    if selected_categories:
        pois = POI.objects.filter(building=full_building, category__id__in=selected_categories)
    else:
        pois = POI.objects.filter(building=full_building)  # Show all POIs if no category is selected

    context = {
        'full_building': full_building,
        'building_list': building_list, # this makes sure building sidebar content always loads
        'pois': pois,
        'all_categories': all_categories,
        'selected_categories': selected_categories,    
    }

    return render(request, 'buildingview.html', context)

def my_view(request):
    return render(request, 'home.html', {'MEDIA_URL': settings.MEDIA_URL})
