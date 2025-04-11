from django.contrib import admin

from .models import Map, Building, Filter, Location, POI, POIFilter

admin.site.register(Map)
admin.site.register(Building)
admin.site.register(Filter)
admin.site.register(Location)
admin.site.register(POI)
admin.site.register(POIFilter)

# Register your models here.
