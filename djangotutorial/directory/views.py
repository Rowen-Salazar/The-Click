
from django.shortcuts import render
from directory.models import Mapname
#from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def mapview(request):
    Maps = Mapname.objects.all()
    return render(request, 'mapview.html', {'Test': Maps})

def mapdetail(request, map_name):
    mapname = get_object_or_404(Mapname, pk=question_id)
    return render(request, 'mapdetail.html', {'mapname': mapname})
