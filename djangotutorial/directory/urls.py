from django.urls import path

from . import views

app_name = "directory"
urlpatterns = [
    path("mapview/", views.home, name="home"),
    path('about/', views.about, name="about"),
    path("buildingview/", views.buildinglist, name="buildinglist"),
    #/mapview/untmap
    path("mapview/<str:map_name>/", views.mapview, name="mapview"),
    path("buildingview/<str:building_name>/", views.buildingview, name="buildingview"),

]
