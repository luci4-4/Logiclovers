from django.urls import path
from . import views

urlpatterns = [
    path("", views.Render_Main),
    path("Map", views.Render_Map)
]
