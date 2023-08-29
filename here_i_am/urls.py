from django.urls import path

from . import views

urlpatterns = [
    path("", views.intersections_index, name="intersections"),
]