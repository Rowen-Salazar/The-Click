import datetime

from django.db import models
from django.utils import timezone
    
class Map(models.Model):
    name = models.CharField(max_length=50)
    display_name = models.CharField(max_length=200, blank=True)
    map_image = models.ImageField(null=True, blank=True, upload_to="images/")
    #Google API Stuff
    zoom = models.IntegerField(blank=False, default=17)
    center = models.CharField(max_length=1000, blank=True)
    map_id = models.CharField(max_length=1000, blank=True)
    def __str__(self):
        return self.display_name

class Building(models.Model):
    name = models.CharField(max_length=50)
    display_name = models.CharField(max_length=200, blank=True)
    floors = models.IntegerField(blank=False, default=1)
    floor_plan = models.ImageField(null=True, blank=True, upload_to="images/")
    on_map = models.ForeignKey(Map, on_delete=models.CASCADE)
    #for sidebar
    address = models.CharField(max_length=225, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='images/buildingSearchBox/')
    slug = models.SlugField(unique=True, null=True, blank=True)
    
    def __str__(self):
        return self.display_name
    
class Filter(models.Model):
    MAP = "Map"
    BUILDING = "Building"
    ACCOUNT_TYPE_CHOICES = {
        MAP: "Map",
        BUILDING: "Building",
    }
    name = models.CharField(max_length=100)
    display_name = models.CharField(max_length=200, blank=True)
    page_type = models.CharField(
        max_length=100,
        choices=ACCOUNT_TYPE_CHOICES,
        default=MAP,
    )
    def __str__(self):
        return self.name
    
class Location(models.Model):
    name = models.CharField(max_length=100)
    display_name = models.CharField(max_length=200, blank=True)
    zipcode = models.CharField(max_length=200,blank=True, null=True)
    city = models.CharField(max_length=200,blank=True, null=True)
    adress = models.CharField(max_length=200,blank=True, null=True)
    latitude = models.CharField(max_length=1000, blank=True)
    longitude = models.CharField(max_length=1000, blank=True)
    filter_category = models.ForeignKey(Filter, on_delete=models.CASCADE, null=True)
    #Optional if on a building on the building page
    on_building = models.ForeignKey(Building, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.display_name
