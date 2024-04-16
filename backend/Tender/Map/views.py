from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.


def Render_Main(request):
    return render(request, "Map/Main.html")


def Render_Map(request):
    return render(request, "Map/russia_map.html")