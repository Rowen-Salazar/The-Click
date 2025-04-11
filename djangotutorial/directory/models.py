import datetime

from django.db import models
from django.utils import timezone
    
class Map(models.Model):
    name = models.CharField(max_length=50)
    display_name = models.CharField(max_length=200, blank=True)
    map_color = models.CharField('Map Color', max_length=6, default="000000")
    map_image = models.ImageField(null=True, blank=True, upload_to="images/")
    #Google API Integration
    zoom = models.IntegerField(blank=False, default=17)
    center = models.CharField(max_length=1000, blank=True)
    map_id = models.CharField(max_length=1000, blank=True)
    def __str__(self):
        return self.display_name

class Building(models.Model):
    display_name = models.CharField(max_length=200, blank=True)
    class Meta:
        ordering = ['display_name']  # ensures alphabetical order by name
    slug = models.SlugField(default="", null=False, unique=True)
    #floor plans
    floors = models.IntegerField(blank=False, default=1)
    has_ground_floor = models.BooleanField(default=False)
    ground_floor = models.ImageField(null=True, blank=True, upload_to="images/buildingFloors")
    #Floor one is NOT optional, all others are
    floor_1 = models.ImageField(null=True, upload_to="images/buildingFloors")
    floor_2 = models.ImageField(null=True, blank=True, upload_to="images/buildingFloors")
    floor_3 = models.ImageField(null=True, blank=True, upload_to="images/buildingFloors")
    floor_4 = models.ImageField(null=True, blank=True, upload_to="images/buildingFloors")
    floor_5 = models.ImageField(null=True, blank=True, upload_to="images/buildingFloors")
    #For DP
    floor_6 = models.ImageField(null=True, blank=True, upload_to="images/buildingFloors")
    floor_7 = models.ImageField(null=True, blank=True, upload_to="images/buildingFloors")
    on_map = models.ForeignKey(Map, on_delete=models.CASCADE)
    #for sidebar
    address = models.CharField(max_length=225, blank=True)
    mnemonic = models.CharField(max_length=10, blank=True)
    sidebar_image = models.ImageField(null=True, upload_to='images/buildingSearchBox/')
    def __str__(self):
        return self.display_name
    
class Filter(models.Model):
    MAP = "Map"
    BUILDING = "Building"
    ACCOUNT_TYPE_CHOICES = {
        MAP: "Map",
        BUILDING: "Building",
    }
    name = models.CharField('Option Name', max_length=100)
    display_name = models.CharField(max_length=200, blank=True)
    page_type = models.CharField(
        max_length=100,
        choices=ACCOUNT_TYPE_CHOICES,
        default=MAP,
    )
    def __str__(self):
        return self.name

class POIFilter(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to="images/POI_Icons/", null=True, blank=True)

    def __str__(self):
        return self.name

class POI(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    category = models.ForeignKey(POIFilter, on_delete=models.CASCADE, default=1)
    floor = models.IntegerField()
    x_coord = models.FloatField(help_text="X coordinate as percentage (0–100)")
    y_coord = models.FloatField(help_text="Y coordinate as percentage (0–100)")
    label = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.label} - {self.building.display_name} (Floor {self.floor})"

class Location(models.Model):
    name = models.CharField(max_length=500,blank=True, null=True)
    zipcode = models.CharField(max_length=200,blank=True, null=True)
    city = models.CharField(max_length=200,blank=True, null=True)
    adress = models.CharField(max_length=200,blank=True, null=True)
    latitude = models.CharField(max_length=1000, blank=True)
    longitude = models.CharField(max_length=1000, blank=True)
    filter_category = models.ForeignKey(Filter, on_delete=models.CASCADE, null=True)
    #Optional if on a building on the building page
    on_building = models.ForeignKey(Building, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.name
