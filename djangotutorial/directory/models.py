import datetime

from django.db import models
from django.utils import timezone

class Location(models.Model):
    name = models.CharField(max_length=100)
    display_name = models.CharField(max_length=200, blank=True)
    coordinates = models.CharField(max_length=1000, blank=True)
    def __str__(self):
        return self.display_name
    
class Filter(models.Model):
    name = models.CharField(max_length=100)
    display_name = models.CharField(max_length=200, blank=True)
    def __str__(self):
        return self.name
    
class Map(models.Model):
    name = models.CharField(max_length=50)
    display_name = models.CharField(max_length=200, blank=True)
    #Placeholder for Google API Integration
    map_image = models.ImageField(null=True, blank=True, upload_to="images/")
    #Google API Stuff
    zoom = models.IntegerField(blank=False, default=17)
    center = models.CharField(max_length=1000, blank=True)
    map_id = models.CharField(max_length=1000, blank=True)
    filters = models.ManyToManyField(Filter, blank=True)
    def __str__(self):
        return self.display_name

class Building(models.Model):
    name = models.CharField(max_length=50)
    display_name = models.CharField(max_length=200, blank=True)
    floors = models.IntegerField(blank=False, default=1)
    floor_plan = models.ImageField(null=True, blank=True, upload_to="images/")
    on_map = models.ForeignKey(Map, on_delete=models.CASCADE)
    
    #for sidebar
    #address = models.CharField(max_length=225)
    #image = models.ImageField(upload_to='images/buildingSearchBox/')
    #slug = models.SlugField(unique=True)
    
    def __str__(self):
        return self.display_name
