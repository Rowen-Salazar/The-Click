from django.urls import path

from . import views

app_name = "directory"
urlpatterns = [
    path("", views.home, name="home"),
    #/mapview/untmap
    path("<str:map_name>/", views.mapview, name="mapview"),
]
