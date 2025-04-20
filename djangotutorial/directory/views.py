
from django.shortcuts import get_object_or_404, render
from directory.models import Map, Building, Filter, Location, POIFilter, BuildingCategoryImage
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
    selected_category_id = request.GET.get("category")
    building_list = Building.objects.all() # this makes sure building sidebar content always loads
    floor_range = range(1, full_building.floors + 1) 
    selected_floor = request.GET.get("floor")  # Can use this for floor select --> here for my testing
    floor_image = None

    if selected_floor:
        try: 
            floor_image = Building.objects.get(id=full_building, floor=selected_floor)
        except Building.DoesNotExist:
            floor_image = None

    current_category = None
    category_image = None

    if selected_category_id:
        try:
            current_category = POIFilter.objects.get(id=selected_category_id)

        # If a specific floor is selected (use parts of this for floor select --> can edit as needed, just threw this in for my testing)
            if selected_floor:
                is_ground = selected_floor.lower() == "ground"
                floor_number = 0 if is_ground else int(selected_floor)
                
                category_image = None
                if floor_images.get(selected_floor):
                    category_image = floor_images[selected_floor]

            else:
                # Default to floor 1 category image
                category_image = full_building.floor_1
                    
        except (POIFilter.DoesNotExist, ValueError):
            category_image = None

    context = {
        'full_building': full_building,
        'building_list': building_list, # This makes sure building sidebar content always loads
        'all_categories': all_categories,
        'selected_category_id': int(selected_category_id) if selected_category_id else None,
        'category_image': category_image,
        'current_category': current_category,
        'selected_floor': selected_floor,
        'floor_image': floor_image,
        'floor_range': floor_range,
    }

    return render(request, 'buildingview.html', context)

def my_view(request):
    return render(request, 'home.html', {'MEDIA_URL': settings.MEDIA_URL})