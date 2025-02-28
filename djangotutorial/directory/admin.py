from django.contrib import admin

from .models import Map, Building, Filter, Location

admin.site.register(Map)
admin.site.register(Building)
admin.site.register(Filter)
admin.site.register(Location)

# Register your models here.
