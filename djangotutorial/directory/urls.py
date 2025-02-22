from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = "directory"
urlpatterns = [
    path("", views.home, name="home"),
    #/mapview/untmap
    #path("<str:map_name>/", views.mapview, name="mapview"),
    path("discoverypark/<str:map_name>/", views.discoverypark, name="discoverypark"),
    path("untmaincampus/<str:map_name>/", views.untmaincampus, name="untmaincampus"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)