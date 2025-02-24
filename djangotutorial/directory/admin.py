from django.contrib import admin

from .models import Map, Building, Filter, Locations

admin.site.register(Map)
admin.site.register(Building)
admin.site.register(Filter)
admin.site.register(Locations)

# Register your models here.
