import datetime

from django.db import models
from django.utils import timezone

class Mapname(models.Model): #Eventually to be the name of the map
    name = models.CharField(max_length=10)
    map_image = models.ImageField(null=True, blank=True, upload_to="images/")
    def __str__(self):
        return self.name

class Choice(models.Model): #Eventually to be the dropdown choices
    question = models.ForeignKey(Mapname, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    def __str__(self):
        return self.choice_text
