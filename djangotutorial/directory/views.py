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
    
    selected_floor = request.GET.get("floor")  # Can use this for floor select --> here for my testing
    current_category = None
    category_image = None
    default_floor_image = None # FL

    # Detect which floors exist for this building
    available_floors = []
    if full_building.ground_floor:
        available_floors.append("Ground")
    for i in range(1, 8):
        floor_attr = f'floor_{i}'
        if getattr(full_building, floor_attr):
            available_floors.append(str(i))
    
    # Reorder floor display on dropdown if building is Discovery Park
    if full_building.slug == 'dp':
        def dp_floor_sort_key(floor):
            if floor == "1":
                return 0
            elif floor == "ground":
                return 1
            else:
                return 2 
        available_floors = sorted(available_floors, key=dp_floor_sort_key)

    # Always set the default floor image based on selected floor (fallback for when no category is selcted)
    if selected_floor:
        if selected_floor.lower() == "ground":
            default_floor_image = full_building.ground_floor
        else:
            floor_attr = f'floor_{selected_floor}'
            default_floor_image = getattr(full_building, floor_attr, None)
    else:
        default_floor_image = full_building.floor_1

    # Category + floor-specific image code (if selected on buildingview)
    if selected_category_id:
        try:
            current_category = POIFilter.objects.get(id=selected_category_id)

            # If a specific floor is selected (use parts of this for floor select --> can edit as needed, just threw this in for my testing)
            if selected_floor:
                is_ground = selected_floor.lower() == "ground"
                floor_number = 0 if is_ground else int(selected_floor)

                category_image = BuildingCategoryImage.objects.get(
                    building=full_building,
                    category=current_category,
                    floor=floor_number
                    # is_ground_floor=is_ground,
                    # floor=None if is_ground else floor_number
                )
            else:
                # Default to floor 1 category image
                category_image = BuildingCategoryImage.objects.get(
                    building=full_building,
                    category=current_category,
                    # is_ground_floor=False,
                    floor=1
                )
        except (POIFilter.DoesNotExist, BuildingCategoryImage.DoesNotExist, ValueError):
            category_image = None

    context = {
        'full_building': full_building,
        'building_list': building_list, # This makes sure building sidebar content always loads
        'all_categories': all_categories,
        'selected_category_id': int(selected_category_id) if selected_category_id else None,
        'category_image': category_image,
        'current_category': current_category,
        'available_floors': available_floors,       # NEW
        'selected_floor': selected_floor,           # NEW
        'default_floor_image': default_floor_image, # NEW
    }

    return render(request, 'buildingview.html', context)

def my_view(request):
    return render(request, 'home.html', {'MEDIA_URL': settings.MEDIA_URL})
