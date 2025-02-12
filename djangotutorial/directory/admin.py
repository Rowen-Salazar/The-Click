from django.contrib import admin

from .models import Map, Building, Filter

admin.site.register(Map)
admin.site.register(Building)
admin.site.register(Filter)

# Register your models here.
