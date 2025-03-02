from django.urls import path

from . import views

app_name = "directory"
urlpatterns = [
    path("mapview/", views.home, name="home"),
    path("buildingview/", views.buildinglist, name="buildinglist"),
    #/mapview/untmap
    path("mapview/<str:map_name>/", views.mapview, name="mapview"),
    path("buildingview/", views.buildingview, name="buildingview"),

]
