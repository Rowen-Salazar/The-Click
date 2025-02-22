import datetime

from django.db import models
from django.utils import timezone

class Map(models.Model):
    name = models.CharField(max_length=20, unique=True)
    map_color = models.CharField('Map Color', max_length=6, default="000000")
    #Placeholder for Google API Integration
    map_image = models.ImageField(null=True, blank=True, upload_to="images/")
    def __str__(self):
        return self.name

class Building(models.Model):
    name = models.CharField(max_length=200)
    floors = models.IntegerField(blank=False, default=1)
    floor_plan = models.ImageField(null=True, blank=True, upload_to="images/")
    on_map = models.ForeignKey(Map, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Filter(models.Model):
    name = models.CharField('Option Name', max_length=100)
    onmaps = models.BooleanField('Included In Map Page?')
    onbuildings = models.BooleanField('Included In Building Page?')
    def __str__(self):
        return self.name
