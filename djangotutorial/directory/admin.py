from django.contrib import admin

from .models import Map, Building, Filter, Location, POIFilter, BuildingCategoryImage

admin.site.register(Map)
admin.site.register(Building)
admin.site.register(Filter)
admin.site.register(Location)
admin.site.register(POIFilter)
admin.site.register(BuildingCategoryImage)

# Register your models here.
